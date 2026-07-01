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


DOUBLE_BRIDGE_JS = """
(config) => {
  const gateX = 760;
  const midY = 390;
  const pheroSum = (name) =>
    Math.round(antSim.world.pheromones[name].data.reduce((sum, value) => sum + value, 0));
  const sampleBranchPheromone = (y) => {
    let total = 0;
    for (let x = 620; x <= 960; x += 24) total += antSim.world.pheromones.food.sample(x, y);
    return Math.round(total);
  };
  const seedBranch = (branch, strength) => {
    if (!branch || strength <= 0) return;
    const y = branch === 'upper' ? 260 : 520;
    const points = [
      [antSim.world.nest.x, antSim.world.nest.y],
      [690, y],
      [880, y],
      [980, 390],
    ];
    for (let p = 0; p < points.length - 1; p++) {
      const [x1, y1] = points[p];
      const [x2, y2] = points[p + 1];
      const steps = Math.max(1, Math.ceil(Math.hypot(x2 - x1, y2 - y1) / 14));
      for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        antSim.world.pheromones.food.add(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, strength);
      }
    }
  };

  antSim.setSeed(config.seed);
  antSim.setParam('species', config.species);
  antSim.setParam('speed', config.speed);
  antSim.setParam('pheromoneStrength', config.pheromoneStrength);
  antSim.setParam('diffusionRate', config.diffusionRate);
  antSim.setParam('evaporationRate', config.evaporationRate);
  antSim.setParam('senseThreshold', config.senseThreshold);
  antSim.setParam('temperature', 26);
  antSim.setParam('humidity', 58);
  antSim.setParam('hunger', 95);
  antSim.setParam('broodDemand', 0);
  antSim.setupMatureColony();
  antSim.setParam('antCount', config.ants);
  antSim.world.food = [];
  antSim.world.water = [];
  antSim.world.enemies = [];
  antSim.world.corpses = [];
  antSim.world.mills = [];
  antSim.world.rocks = [];
  antSim.world.eggs = 0;
  antSim.world.larvae = 0;
  antSim.world.pupae = 0;
  antSim.world.foodStore = 80;
  antSim.world.waterStore = 1200;
  antSim.clearPheromones();
  antSim.addFood(980, 390, config.foodAmount);

  for (let y = 310; y <= 470; y += 24) {
    antSim.world.rocks.push({ x: gateX, y, r: 22 });
  }
  seedBranch(config.biasBranch, config.biasStrength);

  const previous = new Map();
  for (const ant of antSim.world.ants) previous.set(ant.id, { x: ant.x, y: ant.y });
  const counts = { upper: 0, lower: 0, upperReturn: 0, lowerReturn: 0, upperOut: 0, lowerOut: 0 };
  const chunks = Math.max(1, Math.round(config.days / config.sampleDays));
  for (let i = 0; i < chunks; i++) {
    antSim.runDays(config.sampleDays, config.dt);
    for (const ant of antSim.world.ants) {
      const prev = previous.get(ant.id);
      if (prev && ((prev.x < gateX && ant.x >= gateX) || (prev.x > gateX && ant.x <= gateX))) {
        const branch = ant.y < midY ? 'upper' : 'lower';
        counts[branch] += 1;
        if (ant.carrying || ant.state === 'carrying food') counts[`${branch}Return`] += 1;
        else counts[`${branch}Out`] += 1;
      }
      previous.set(ant.id, { x: ant.x, y: ant.y });
    }
  }

  const total = counts.upper + counts.lower;
  const returnTotal = counts.upperReturn + counts.lowerReturn;
  const selectedBranch = counts.upper === counts.lower ? 'tie' : counts.upper > counts.lower ? 'upper' : 'lower';
  const returnSelectedBranch = counts.upperReturn === counts.lowerReturn ? 'tie' : counts.upperReturn > counts.lowerReturn ? 'upper' : 'lower';
  return {
    seed: config.seed,
    species: config.species,
    ants: antSim.world.ants.length,
    days: config.days,
    bias_branch: config.biasBranch || 'none',
    bias_strength: config.biasStrength,
    upper_crossings: counts.upper,
    lower_crossings: counts.lower,
    total_crossings: total,
    upper_return_crossings: counts.upperReturn,
    lower_return_crossings: counts.lowerReturn,
    return_crossings: returnTotal,
    selected_branch: selectedBranch,
    return_selected_branch: returnSelectedBranch,
    dominance: total ? Number((Math.abs(counts.upper - counts.lower) / total).toFixed(4)) : 0,
    return_dominance: returnTotal ? Number((Math.abs(counts.upperReturn - counts.lowerReturn) / returnTotal).toFixed(4)) : 0,
    food_trips: antSim.world.stats.foodTrips,
    food_collected: Math.round(antSim.world.stats.foodCollected),
    food_pheromone: pheroSum('food'),
    upper_food_pheromone: sampleBranchPheromone(260),
    lower_food_pheromone: sampleBranchPheromone(520),
    final_ants: antSim.world.ants.length,
    dead: antSim.world.corpses.length
  };
}
"""


def summarize(rows):
    if not rows:
        return {}
    total = len(rows)
    upper = sum(1 for row in rows if row["selected_branch"] == "upper")
    lower = sum(1 for row in rows if row["selected_branch"] == "lower")
    ties = total - upper - lower
    mean_dominance = sum(float(row["dominance"]) for row in rows) / total
    mean_trips = sum(float(row["food_trips"]) for row in rows) / total
    return {
        "runs": total,
        "upper_selected": upper,
        "lower_selected": lower,
        "ties": ties,
        "mean_dominance": round(mean_dominance, 4),
        "mean_food_trips": round(mean_trips, 3),
    }


def main():
    parser = argparse.ArgumentParser(description="Run a Deneubourg-style double-bridge alignment probe.")
    parser.add_argument("--seeds", default="1-8")
    parser.add_argument("--days", type=float, default=8)
    parser.add_argument("--sample-days", type=float, default=0.05)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--ants", type=int, default=240)
    parser.add_argument("--species", choices=["lasius", "eciton"], default="lasius")
    parser.add_argument("--food-amount", type=float, default=1800)
    parser.add_argument("--pheromone-strength", type=float, default=95)
    parser.add_argument("--diffusion-rate", type=float, default=100)
    parser.add_argument("--evaporation-rate", type=float, default=90)
    parser.add_argument("--sense-threshold", type=float, default=14)
    parser.add_argument("--bias-branch", choices=["none", "upper", "lower"], default="none")
    parser.add_argument("--bias-strength", type=float, default=0)
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "double_bridge_probe.csv")
    parser.add_argument("--metadata", type=Path, default=None)
    args = parser.parse_args()

    seeds = parse_seeds(args.seeds)
    server, url = start_server()
    rows = []
    try:
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 860})
        errors = []
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.goto(url)
        page.wait_for_function("() => window.antSim && window.antSim.world")
        for seed in seeds:
            row = page.evaluate(
                DOUBLE_BRIDGE_JS,
                {
                    "seed": seed,
                    "days": args.days,
                    "sampleDays": args.sample_days,
                    "dt": args.dt,
                    "ants": args.ants,
                    "species": args.species,
                    "foodAmount": args.food_amount,
                    "pheromoneStrength": args.pheromone_strength,
                    "diffusionRate": args.diffusion_rate,
                    "evaporationRate": args.evaporation_rate,
                    "senseThreshold": args.sense_threshold,
                    "biasBranch": None if args.bias_branch == "none" else args.bias_branch,
                    "biasStrength": args.bias_strength,
                },
            )
            rows.append(row)
        browser.close()
        if errors:
            raise RuntimeError("page errors: " + "; ".join(errors))
    finally:
        server.terminate()
        try:
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server.kill()

    write_csv(args.output, rows)
    summary = {
        "scenario": "double_bridge",
        "literature_target": "Deneubourg-style equal-branch symmetry breaking",
        "parameters": vars(args) | {"output": str(args.output), "metadata": str(args.metadata) if args.metadata else None},
        "summary": summarize(rows),
        "rows": rows,
    }
    metadata_path = args.metadata or args.output.with_suffix(".json")
    metadata_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary["summary"], ensure_ascii=False, indent=2))
    print(f"wrote {len(rows)} rows to {args.output}")
    print(f"wrote metadata to {metadata_path}")


if __name__ == "__main__":
    main()
