#!/usr/bin/env python3
import argparse
import csv
import itertools
import json
import math
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


def parse_grid(items):
    grid = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"grid item must be name=a,b,c, got {item!r}")
        name, values = item.split("=", 1)
        parsed = []
        for raw in values.split(","):
            raw = raw.strip()
            if not raw:
                continue
            try:
                parsed.append(int(raw) if raw.isdigit() else float(raw))
            except ValueError:
                parsed.append(raw)
        if not parsed:
            raise ValueError(f"no values for grid item {name!r}")
        grid[name.strip()] = parsed
    return grid


def iter_param_sets(grid):
    names = list(grid)
    for values in itertools.product(*(grid[name] for name in names)):
        yield dict(zip(names, values))


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
        raise RuntimeError(f"no rows for {path}")
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


CALIBRATION_JS = """
(config) => {
  const applyParams = () => {
    antSim.setParam('species', config.params.species || 'lasius');
    antSim.setParam('speed', config.params.speed ?? 1.4);
    antSim.setParam('pheromoneStrength', config.params.pheromoneStrength ?? 80);
    antSim.setParam('diffusionRate', config.params.diffusionRate ?? 100);
    antSim.setParam('evaporationRate', config.params.evaporationRate ?? 100);
    antSim.setParam('senseThreshold', config.params.senseThreshold ?? 18);
    antSim.setParam('temperature', config.params.temperature ?? 26);
    antSim.setParam('humidity', config.params.humidity ?? 58);
    antSim.setParam('foodSpawn', config.params.foodSpawn ?? 45);
    antSim.setParam('threatPressure', config.params.threatPressure ?? 25);
    antSim.setParam('hunger', config.params.hunger ?? 35);
    antSim.setParam('broodDemand', config.params.broodDemand ?? 50);
    antSim.setParam('soldierRatio', config.params.soldierRatio ?? 12);
  };
  const sample = () => antSim.collectStatsSnapshot();
  const runQuarter = () => antSim.runDays(0.25, config.dt);

  antSim.setSeed(config.seed);
  applyParams();
  antSim.setupMatureColony();
  world.food = [];
  world.water = [];
  antSim.addFood(config.foodX, config.foodY, config.foodAmount);
  antSim.addWater(config.waterX, config.waterY, config.waterAmount);
  world.statsHistory = [];
  world.lastStatsDay = world.day;

  let firstFoodDay = null;
  let foodTripsBeforeRemoval = 0;
  let foodTaskCountBeforeRemoval = 0;
  let peakFoodPheromone = 0;
  const samples = [];

  for (let i = 0; i < Math.round(config.preDays / 0.25); i++) {
    runQuarter();
    const row = sample();
    samples.push(row);
    peakFoodPheromone = Math.max(peakFoodPheromone, row.food_pheromone);
    if (firstFoodDay == null && row.food_trips > 0) firstFoodDay = row.day;
    foodTripsBeforeRemoval = row.food_trips;
    foodTaskCountBeforeRemoval = row.task_food;
  }

  world.food = [];
  const removalDay = world.day;
  let pheromoneAfter1d = null;
  let halfLifeDay = null;
  for (let i = 0; i < Math.round(config.postDays / 0.25); i++) {
    runQuarter();
    const row = sample();
    samples.push(row);
    if (pheromoneAfter1d == null && row.day >= removalDay + 1) pheromoneAfter1d = row.food_pheromone;
    if (halfLifeDay == null && peakFoodPheromone > 0 && row.food_pheromone <= peakFoodPheromone * 0.5) {
      halfLifeDay = row.day - removalDay;
    }
  }

  const final = sample();
  return {
    seed: config.seed,
    first_food_day: firstFoodDay == null ? config.preDays + config.postDays : firstFoodDay,
    food_trips_before_removal: foodTripsBeforeRemoval,
    food_task_count_before_removal: foodTaskCountBeforeRemoval,
    peak_food_pheromone: peakFoodPheromone,
    pheromone_after_1d: pheromoneAfter1d ?? final.food_pheromone,
    trail_decay_fraction_after_1d: peakFoodPheromone > 0 ? (pheromoneAfter1d ?? final.food_pheromone) / peakFoodPheromone : 0,
    trail_half_life_after_removal: halfLifeDay ?? config.postDays,
    brood_total_after_3d: final.brood_total,
    avg_energy_after_3d: final.avg_energy,
    avg_hydration_after_3d: final.avg_hydration,
    final_ants: final.ants,
    final_food_pheromone: final.food_pheromone,
    final_water_pheromone: final.water_pheromone
  };
}
"""


def mean(values):
    return sum(values) / len(values) if values else None


def score_param_set(rows, target):
    metrics = target["metrics"]
    score = 0.0
    out = {}
    for metric, spec in metrics.items():
        values = [float(row[metric]) for row in rows if metric in row and row[metric] is not None]
        if not values:
            continue
        observed = mean(values)
        sd = max(float(spec.get("sd", 1)), 1e-9)
        weight = float(spec.get("weight", 1))
        error = ((observed - float(spec["target"])) / sd) ** 2
        weighted = weight * error
        score += weighted
        out[f"{metric}_mean"] = round(observed, 6)
        out[f"{metric}_loss"] = round(weighted, 6)
    out["loss"] = round(score, 6)
    return out


def run_calibration(args):
    target = json.loads(args.targets.read_text(encoding="utf-8"))
    seeds = parse_seeds(args.seeds)
    grid = parse_grid(args.grid)
    param_sets = list(iter_param_sets(grid))
    server, url = start_server()
    trial_rows = []
    score_rows = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            errors = []
            page.on("pageerror", lambda exc: errors.append(str(exc)))
            page.goto(url)
            page.wait_for_timeout(250)
            for combo_id, params in enumerate(param_sets, start=1):
                combo_rows = []
                for seed in seeds:
                    payload = {
                        "seed": seed,
                        "params": params,
                        "preDays": args.pre_days,
                        "postDays": args.post_days,
                        "dt": args.dt,
                        "foodAmount": args.food_amount,
                        "waterAmount": args.water_amount,
                        "foodX": args.food_x,
                        "foodY": args.food_y,
                        "waterX": args.water_x,
                        "waterY": args.water_y,
                    }
                    result = page.evaluate(CALIBRATION_JS, payload)
                    row = {"combo_id": combo_id, **params, **result}
                    trial_rows.append(row)
                    combo_rows.append(row)
                score_rows.append({"combo_id": combo_id, **params, **score_param_set(combo_rows, target)})
            browser.close()
            if errors:
                raise RuntimeError("page errors: " + "; ".join(errors))
    finally:
        server.terminate()
        try:
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server.kill()
    score_rows.sort(key=lambda row: row["loss"])
    return target, trial_rows, score_rows


def main():
    parser = argparse.ArgumentParser(description="Grid-search calibration for foraging and trail decay.")
    parser.add_argument("--targets", type=Path, default=ROOT / "targets" / "provisional_lasius_foraging.json")
    parser.add_argument("--seeds", default="1-5")
    parser.add_argument("--grid", action="append", default=[
        "diffusionRate=80,120",
        "evaporationRate=80,120",
        "senseThreshold=14,22",
        "pheromoneStrength=70,100",
    ])
    parser.add_argument("--pre-days", type=float, default=2)
    parser.add_argument("--post-days", type=float, default=1.5)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--food-amount", type=float, default=1000)
    parser.add_argument("--water-amount", type=float, default=1000)
    parser.add_argument("--food-x", type=float, default=250)
    parser.add_argument("--food-y", type=float, default=180)
    parser.add_argument("--water-x", type=float, default=320)
    parser.add_argument("--water-y", type=float, default=180)
    parser.add_argument("--trials-output", type=Path, default=ROOT / "calibration_results" / "foraging_trials.csv")
    parser.add_argument("--scores-output", type=Path, default=ROOT / "calibration_results" / "foraging_scores.csv")
    parser.add_argument("--metadata-output", type=Path, default=ROOT / "calibration_results" / "foraging_metadata.json")
    args = parser.parse_args()

    target, trial_rows, score_rows = run_calibration(args)
    write_csv(args.trials_output, trial_rows)
    write_csv(args.scores_output, score_rows)
    metadata = {
        "target_id": target.get("id"),
        "target_status": target.get("status"),
        "seeds": parse_seeds(args.seeds),
        "grid": parse_grid(args.grid),
        "pre_days": args.pre_days,
        "post_days": args.post_days,
        "trial_rows": len(trial_rows),
        "score_rows": len(score_rows),
        "best": score_rows[0] if score_rows else None,
    }
    args.metadata_output.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(trial_rows)} trial rows to {args.trials_output}")
    print(f"wrote {len(score_rows)} score rows to {args.scores_output}")
    print(f"best: {score_rows[0] if score_rows else None}")
    if target.get("status") != "literature_calibrated":
        print("warning: target file is provisional; do not treat this as biological calibration.")


if __name__ == "__main__":
    main()
