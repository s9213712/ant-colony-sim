#!/usr/bin/env python3
import argparse
import json
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


def free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def start_server():
    port = free_port()
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "http.server",
            str(port),
            "--bind",
            "127.0.0.1",
            "--directory",
            str(ROOT),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    url = f"http://127.0.0.1:{port}/"
    deadline = time.time() + 8
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=0.5) as response:
                if response.status == 200:
                    return proc, url
        except Exception:
            time.sleep(0.1)
    proc.terminate()
    raise RuntimeError("local HTTP server did not start")


PERF_JS = """
async (config) => {
  const results = [];
  const round = (value) => Math.round(value * 1000) / 1000;
  const percentile = (values, p) => {
    const sorted = [...values].sort((a, b) => a - b);
    return sorted[Math.min(sorted.length - 1, Math.floor((sorted.length - 1) * p))];
  };
  const setupAnts = (count) => {
    antSim.setSeed(20260701);
    antSim.setupMatureColony();
    world.running = false;
    ui.playPause.textContent = '▶';
    world.ants = [];
    world.food = [];
    world.water = [];
    world.corpses = [];
    world.enemies = [];
    world.mills = [];
    antSim.clearPheromones();
    antSim.addFood(250, 180, 5000);
    antSim.addWater(320, 180, 5000);
    const started = performance.now();
    for (let i = 0; i < count; i++) world.ants.push(createAnt(i + 1));
    ui.antCount.value = Math.min(count, Number(ui.antCount.max));
    syncLabels();
    return performance.now() - started;
  };
  const measureBlock = (iterations, fn) => {
    const samples = [];
    for (let i = 0; i < iterations; i++) {
      const start = performance.now();
      fn();
      samples.push(performance.now() - start);
    }
    const total = samples.reduce((sum, value) => sum + value, 0);
    return {
      mean_ms: round(total / samples.length),
      p95_ms: round(percentile(samples, 0.95)),
      max_ms: round(Math.max(...samples))
    };
  };

  for (const count of config.counts) {
    const createMs = setupAnts(count);
    render();
    const updateStats = measureBlock(config.updateIterations, () => update(config.dt));
    const renderStats = measureBlock(config.renderIterations, () => render());
    const frameStats = measureBlock(config.frameIterations, () => {
      update(config.dt);
      render();
    });
    const snapshot = antSim.collectStatsSnapshot();
    results.push({
      ants: count,
      create_ms: round(createMs),
      create_ms_per_ant: round(createMs / count),
      update_mean_ms: updateStats.mean_ms,
      update_p95_ms: updateStats.p95_ms,
      update_max_ms: updateStats.max_ms,
      render_mean_ms: renderStats.mean_ms,
      render_p95_ms: renderStats.p95_ms,
      render_max_ms: renderStats.max_ms,
      frame_mean_ms: frameStats.mean_ms,
      frame_p95_ms: frameStats.p95_ms,
      frame_max_ms: frameStats.max_ms,
      approx_fps_from_frame_mean: round(1000 / frameStats.mean_ms),
      food_trips: snapshot.food_trips,
      water_trips: snapshot.water_trips,
      food_pheromone: snapshot.food_pheromone,
      water_pheromone: snapshot.water_pheromone
    });
  }
  return results;
}
"""


def main():
    parser = argparse.ArgumentParser(description="Measure Ant-Colony-Sim construction/update/render performance.")
    parser.add_argument("--counts", default="1000,3000,8000", help="Comma-separated ant counts")
    parser.add_argument("--dt", type=float, default=1.4, help="Simulation dt per measured update")
    parser.add_argument("--update-iterations", type=int, default=40)
    parser.add_argument("--render-iterations", type=int, default=40)
    parser.add_argument("--frame-iterations", type=int, default=40)
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "performance_probe.json")
    args = parser.parse_args()

    counts = [int(item.strip()) for item in args.counts.split(",") if item.strip()]
    server, url = start_server()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            errors = []
            page.on("pageerror", lambda exc: errors.append(str(exc)))
            page.goto(url)
            page.wait_for_timeout(250)
            results = page.evaluate(
                PERF_JS,
                {
                    "counts": counts,
                    "dt": args.dt,
                    "updateIterations": args.update_iterations,
                    "renderIterations": args.render_iterations,
                    "frameIterations": args.frame_iterations,
                },
            )
            browser.close()
            if errors:
                raise RuntimeError("page errors: " + "; ".join(errors))
    finally:
        server.terminate()
        try:
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server.kill()

    payload = {
        "counts": counts,
        "dt": args.dt,
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
