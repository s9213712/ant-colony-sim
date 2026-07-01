#!/usr/bin/env python3
import argparse
import csv
import json
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


def parse_seeds(text):
    seeds = []
    for part in text.split(","):
        item = part.strip()
        if not item:
            continue
        if "-" in item:
            start, end = item.split("-", 1)
            seeds.extend(range(int(start), int(end) + 1))
        else:
            seeds.append(int(item))
    if not seeds:
        raise ValueError("at least one seed is required")
    return seeds


def parse_params(pairs):
    params = {}
    for pair in pairs:
        if "=" not in pair:
            raise ValueError(f"parameter override must be name=value, got {pair!r}")
        key, raw = pair.split("=", 1)
        raw = raw.strip()
        if raw.lower() in {"true", "false"}:
            value = raw.lower() == "true"
        else:
            try:
                value = int(raw) if raw.isdigit() else float(raw)
            except ValueError:
                value = raw
        params[key.strip()] = value
    return params


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


def write_csv(path, rows):
    if not rows:
        raise RuntimeError("no rows produced")
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = []
    for row in rows:
        for key in row:
            if key not in headers:
                headers.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def build_eval_payload(args, seed, params):
    return {
        "scenario": args.scenario,
        "seed": seed,
        "days": args.days,
        "dt": args.dt,
        "params": params,
        "foodAmount": args.food_amount,
        "waterAmount": args.water_amount,
        "foodX": args.food_x,
        "foodY": args.food_y,
        "waterX": args.water_x,
        "waterY": args.water_y,
        "individualLimit": args.individual_limit if args.individual_limit > 0 else (1000000000 if args.individual_output else 0),
    }


RUN_EXPERIMENT_JS = """
(config) => {
  const resetControls = () => {
    antSim.setParam('species', config.params.species || 'lasius');
    antSim.setParam('speed', config.params.speed ?? 1.4);
    antSim.setParam('pheromoneStrength', config.params.pheromoneStrength ?? 120);
    antSim.setParam('diffusionRate', config.params.diffusionRate ?? 100);
    antSim.setParam('evaporationRate', config.params.evaporationRate ?? 80);
    antSim.setParam('senseThreshold', config.params.senseThreshold ?? 10);
    antSim.setParam('temperature', config.params.temperature ?? 26);
    antSim.setParam('humidity', config.params.humidity ?? 58);
    antSim.setParam('foodSpawn', config.params.foodSpawn ?? 45);
    antSim.setParam('threatPressure', config.params.threatPressure ?? 25);
    antSim.setParam('hunger', config.params.hunger ?? 35);
    antSim.setParam('broodDemand', config.params.broodDemand ?? 50);
    antSim.setParam('soldierRatio', config.params.soldierRatio ?? 12);
  };

  antSim.setSeed(config.seed);
  resetControls();
  if (config.scenario === 'founding_supplied') {
    antSim.setupFoundingColony();
    world.food = [];
    world.water = [];
    antSim.addFood(config.foodX, config.foodY, config.foodAmount);
    antSim.addWater(config.waterX, config.waterY, config.waterAmount);
  } else if (config.scenario === 'mature_no_resources') {
    antSim.setupMatureColony();
    world.food = [];
    world.water = [];
    world.foodStore = 0;
    world.waterStore = 0;
  } else if (config.scenario === 'mature_hot_dry') {
    antSim.setParam('temperature', config.params.temperature ?? 40);
    antSim.setParam('humidity', config.params.humidity ?? 20);
    antSim.setupMatureColony();
    world.food = [];
    world.water = [];
    antSim.addFood(config.foodX, config.foodY, config.foodAmount);
    antSim.addWater(config.waterX, config.waterY, config.waterAmount);
  } else {
    antSim.setupMatureColony();
    world.food = [];
    world.water = [];
    antSim.addFood(config.foodX, config.foodY, config.foodAmount);
    antSim.addWater(config.waterX, config.waterY, config.waterAmount);
  }

  world.statsHistory = [];
  world.lastStatsDay = world.day;
  const started = performance.now();
  antSim.runDays(config.days, config.dt);
  const elapsed = Math.round(performance.now() - started);
  const final = antSim.collectStatsSnapshot();
  const rows = world.statsHistory.slice();
  if (!rows.length || rows[rows.length - 1].day !== final.day) rows.push(final);
  return {
    rows: rows.map((row, index) => ({
    scenario: config.scenario,
    replicate: config.seed,
    row_index: index,
    elapsed_ms: elapsed,
    ...row
    })),
    individuals: antSim.collectIndividualSnapshot(config.individualLimit).map((row, index) => ({
      scenario: config.scenario,
      replicate: config.seed,
      row_index: index,
      ...row
    }))
  };
}
"""


def run_batch(args):
    seeds = parse_seeds(args.seeds)
    params = parse_params(args.set)
    server, url = start_server()
    rows = []
    individual_rows = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            errors = []
            page.on("pageerror", lambda exc: errors.append(str(exc)))
            page.goto(url)
            page.wait_for_timeout(250)
            for seed in seeds:
                payload = build_eval_payload(args, seed, params)
                result = page.evaluate(RUN_EXPERIMENT_JS, payload)
                rows.extend(result["rows"])
                individual_rows.extend(result["individuals"])
            browser.close()
            if errors:
                raise RuntimeError("page errors: " + "; ".join(errors))
    finally:
        server.terminate()
        try:
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server.kill()
    return rows, individual_rows


def main():
    parser = argparse.ArgumentParser(description="Run Ant-Colony-Sim headless batch experiments.")
    parser.add_argument("--scenario", choices=["mature_supplied", "mature_no_resources", "mature_hot_dry", "founding_supplied"], default="mature_supplied")
    parser.add_argument("--seeds", default="1-5", help="Comma list or ranges, e.g. 1,2,5-10")
    parser.add_argument("--days", type=float, default=10)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--set", action="append", default=[], help="Scriptable parameter override, e.g. --set diffusionRate=140")
    parser.add_argument("--food-amount", type=float, default=1200)
    parser.add_argument("--water-amount", type=float, default=1200)
    parser.add_argument("--food-x", type=float, default=250)
    parser.add_argument("--food-y", type=float, default=180)
    parser.add_argument("--water-x", type=float, default=320)
    parser.add_argument("--water-y", type=float, default=180)
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "batch_results.csv")
    parser.add_argument("--individual-output", type=Path, default=None)
    parser.add_argument("--individual-limit", type=int, default=0, help="Number of ants per seed to export when --individual-output is set; 0 disables individual rows")
    parser.add_argument("--metadata", type=Path, default=None)
    args = parser.parse_args()

    rows, individual_rows = run_batch(args)
    write_csv(args.output, rows)
    if args.individual_output:
        write_csv(args.individual_output, individual_rows)
    metadata_path = args.metadata or args.output.with_suffix(".json")
    metadata = {
        "scenario": args.scenario,
        "seeds": parse_seeds(args.seeds),
        "days": args.days,
        "dt": args.dt,
        "params": parse_params(args.set),
        "rows": len(rows),
        "individual_rows": len(individual_rows),
        "output": str(args.output),
        "individual_output": str(args.individual_output) if args.individual_output else None,
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(rows)} rows to {args.output}")
    if args.individual_output:
        print(f"wrote {len(individual_rows)} individual rows to {args.individual_output}")
    print(f"wrote metadata to {metadata_path}")


if __name__ == "__main__":
    main()
