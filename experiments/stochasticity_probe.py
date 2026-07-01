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


STOCHASTICITY_JS = """
(config) => {
  const applyProfile = (profile) => {
    const ants = antSim.world.ants;
    for (let i = 0; i < ants.length; i++) {
      const ant = ants[i];
      if (profile === 'low') ant.turnNoise = 0.018;
      else if (profile === 'medium') ant.turnNoise = 0.055;
      else if (profile === 'high') ant.turnNoise = 0.105;
      else if (profile === 'diverse') {
        const q = i / Math.max(ants.length - 1, 1);
        if (q < 0.3) ant.turnNoise = 0.018;
        else if (q < 0.7) ant.turnNoise = 0.055;
        else ant.turnNoise = 0.11;
      }
      ant.baseTurnNoise = ant.turnNoise;
      ant.explorationDrive = 0;
    }
  };
  const runPhase = (days, foodX, foodY, phase) => {
    const startTrips = antSim.world.stats.foodTrips;
    const startCollected = antSim.world.stats.foodCollected;
    antSim.runDays(days, config.dt);
    const row = antSim.collectStatsSnapshot();
    return {
      phase,
      food_x: foodX,
      food_y: foodY,
      phase_food_trips: row.food_trips - startTrips,
      phase_food_collected: Math.round(row.food_collected - startCollected),
      ...row
    };
  };
  const runBlock = (days, foodX, foodY, phase) => {
    antSim.world.food = [];
    antSim.addFood(foodX, foodY, config.foodAmount);
    return runPhase(days, foodX, foodY, phase);
  };

  antSim.setSeed(config.seed);
  antSim.setParam('species', 'lasius');
  antSim.setParam('pheromoneStrength', config.pheromoneStrength);
  antSim.setParam('evaporationRate', config.evaporationRate);
  antSim.setParam('senseThreshold', config.senseThreshold);
  antSim.setParam('diffusionRate', config.diffusionRate);
  antSim.setParam('hunger', 95);
  antSim.setParam('broodDemand', 0);
  antSim.setupMatureColony();
  antSim.setParam('antCount', config.ants);
  antSim.world.food = [];
  antSim.world.water = [];
  antSim.addWater(320, 180, 5000);
  antSim.world.foodStore = 40;
  antSim.world.waterStore = 2000;
  antSim.world.eggs = 0;
  antSim.world.larvae = 0;
  antSim.world.pupae = 0;
  antSim.clearPheromones();
  applyProfile(config.profile);

  const first = runBlock(config.preDays, config.initialFoodX, config.initialFoodY, 'initial_food');
  antSim.world.food = [];
  if (config.clearOldTrails) {
    for (const field of Object.values(antSim.world.pheromones)) field.data.fill(0);
  }
  antSim.addFood(config.relocatedFoodX, config.relocatedFoodY, config.foodAmount);
  const relocatedStartTrips = antSim.world.stats.foodTrips;
  const relocatedStartCollected = antSim.world.stats.foodCollected;
  const earlyDays = Math.min(config.adaptationDays, config.postDays);
  const early = runPhase(earlyDays, config.relocatedFoodX, config.relocatedFoodY, 'relocated_early');
  const remainingDays = Math.max(0, config.postDays - earlyDays);
  const late = runPhase(remainingDays, config.relocatedFoodX, config.relocatedFoodY, 'relocated_late');
  const finalRow = antSim.collectStatsSnapshot();
  const total = {
    phase: 'relocated_total',
    food_x: config.relocatedFoodX,
    food_y: config.relocatedFoodY,
    phase_food_trips: finalRow.food_trips - relocatedStartTrips,
    phase_food_collected: Math.round(finalRow.food_collected - relocatedStartCollected),
    ...finalRow
  };
  return [first, early, late, total].map((row) => ({
    seed: config.seed,
    profile: config.profile,
    ants_requested: config.ants,
    pre_days: config.preDays,
    post_days: config.postDays,
    adaptation_days: config.adaptationDays,
    ...row
  }));
}
"""


def summarize(rows):
    grouped = {}
    for row in rows:
        key = (row["profile"], row["phase"])
        grouped.setdefault(key, []).append(row)
    out = []
    for (profile, phase), items in sorted(grouped.items()):
        n = len(items)
        out.append({
            "profile": profile,
            "phase": phase,
            "n": n,
            "mean_phase_food_trips": round(sum(float(item["phase_food_trips"]) for item in items) / n, 3),
            "mean_phase_food_collected": round(sum(float(item["phase_food_collected"]) for item in items) / n, 3),
            "mean_avg_turn_noise": round(sum(float(item["avg_turn_noise"]) for item in items) / n, 5),
            "mean_avg_base_turn_noise": round(sum(float(item.get("avg_base_turn_noise") or item["avg_turn_noise"]) for item in items) / n, 5),
            "mean_avg_exploration_drive": round(sum(float(item.get("avg_exploration_drive") or 0) for item in items) / n, 4),
            "mean_avg_traffic_load": round(sum(float(item.get("avg_traffic_load") or 0) for item in items) / n, 4),
            "mean_traffic_max_cell": round(sum(float(item.get("traffic_max_cell") or 0) for item in items) / n, 3),
            "mean_ants_with_food_memory": round(sum(float(item.get("ants_with_food_memory") or 0) for item in items) / n, 3),
            "mean_food_memory_strength": round(sum(float(item.get("avg_food_memory_strength") or 0) for item in items) / n, 4),
            "mean_food_pheromone": round(sum(float(item["food_pheromone"]) for item in items) / n, 3),
        })
    initial_by_profile = {
        row["profile"]: row
        for row in out
        if row["phase"] == "initial_food"
    }
    for row in out:
        initial = initial_by_profile.get(row["profile"])
        if not initial or row["phase"] == "initial_food":
            row["trips_vs_initial"] = 1.0 if row["phase"] == "initial_food" else ""
            row["collected_vs_initial"] = 1.0 if row["phase"] == "initial_food" else ""
            continue
        trips_base = float(initial["mean_phase_food_trips"])
        collected_base = float(initial["mean_phase_food_collected"])
        row["trips_vs_initial"] = round(row["mean_phase_food_trips"] / trips_base, 3) if trips_base else ""
        row["collected_vs_initial"] = round(row["mean_phase_food_collected"] / collected_base, 3) if collected_base else ""
    return out


def main():
    parser = argparse.ArgumentParser(description="Probe diverse stochasticity effects on ant foraging and adaptation.")
    parser.add_argument("--seeds", default="1-8")
    parser.add_argument("--profiles", default="low,medium,high,diverse")
    parser.add_argument("--ants", type=int, default=240)
    parser.add_argument("--pre-days", type=float, default=4)
    parser.add_argument("--post-days", type=float, default=4)
    parser.add_argument("--adaptation-days", type=float, default=0.5)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--food-amount", type=float, default=1800)
    parser.add_argument("--initial-food-x", type=float, default=960)
    parser.add_argument("--initial-food-y", type=float, default=180)
    parser.add_argument("--relocated-food-x", type=float, default=220)
    parser.add_argument("--relocated-food-y", type=float, default=620)
    parser.add_argument("--pheromone-strength", type=float, default=120)
    parser.add_argument("--evaporation-rate", type=float, default=80)
    parser.add_argument("--diffusion-rate", type=float, default=100)
    parser.add_argument("--sense-threshold", type=float, default=10)
    parser.add_argument("--clear-old-trails", action="store_true", help="Clear pheromone fields before relocating food; default preserves obsolete trails")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "stochasticity_probe.csv")
    parser.add_argument("--summary-output", type=Path, default=None)
    args = parser.parse_args()

    seeds = parse_seeds(args.seeds)
    profiles = [item.strip() for item in args.profiles.split(",") if item.strip()]
    server, url = start_server()
    rows = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 860})
            errors = []
            page.on("pageerror", lambda exc: errors.append(str(exc)))
            page.goto(url, wait_until="domcontentloaded", timeout=90000)
            page.wait_for_function("() => window.antSim && window.antSim.world", timeout=90000)
            for profile in profiles:
                for seed in seeds:
                    result = page.evaluate(
                        STOCHASTICITY_JS,
                        {
                            "seed": seed,
                            "profile": profile,
                            "ants": args.ants,
                            "preDays": args.pre_days,
                            "postDays": args.post_days,
                            "adaptationDays": args.adaptation_days,
                            "dt": args.dt,
                            "foodAmount": args.food_amount,
                            "initialFoodX": args.initial_food_x,
                            "initialFoodY": args.initial_food_y,
                            "relocatedFoodX": args.relocated_food_x,
                            "relocatedFoodY": args.relocated_food_y,
                            "pheromoneStrength": args.pheromone_strength,
                            "evaporationRate": args.evaporation_rate,
                            "diffusionRate": args.diffusion_rate,
                            "senseThreshold": args.sense_threshold,
                            "clearOldTrails": args.clear_old_trails,
                        },
                    )
                    rows.extend(result)
            browser.close()
            if errors:
                raise RuntimeError("page errors: " + "; ".join(errors))
    finally:
        server.terminate()
        try:
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server.kill()

    summary = summarize(rows)
    write_csv(args.output, rows)
    summary_path = args.summary_output or args.output.with_name(args.output.stem + "_summary.csv")
    write_csv(summary_path, summary)
    args.output.with_suffix(".json").write_text(
        json.dumps(
            {
                "literature_target": "Shiraishi et al. 2018 diverse stochasticity and adaptive foraging",
                "seeds": seeds,
                "profiles": profiles,
                "clear_old_trails": args.clear_old_trails,
                "rows": len(rows),
                "summary": summary,
                "output": str(args.output),
                "summary_output": str(summary_path),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"wrote {len(rows)} rows to {args.output}")
    print(f"wrote summary to {summary_path}")


if __name__ == "__main__":
    main()
