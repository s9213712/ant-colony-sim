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

SOURCES = [
    {
        "id": "perna_2012",
        "paper": "Perna et al. 2012, Individual rules for trail pattern formation in Argentine ants",
        "url": "https://arxiv.org/abs/1201.5827",
    },
    {
        "id": "deneubourg_goss_bridge",
        "paper": "Deneubourg/Goss/Beckers double-bridge trail-selection paradigm, cited and summarized in Perna et al. 2012",
        "url": "https://arxiv.org/abs/1201.5827",
    },
    {
        "id": "dussutour_2004",
        "paper": "Dussutour et al. 2004, Optimal traffic organisation in ants under crowded conditions",
        "url": "https://arxiv.org/abs/cond-mat/0403142",
    },
    {
        "id": "john_2009",
        "paper": "John et al. 2009, Trafficlike collective movement of ants on trails: absence of jammed phase",
        "url": "https://arxiv.org/abs/0903.2717",
    },
    {
        "id": "shiraishi_2018",
        "paper": "Shiraishi et al. 2018, Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging",
        "url": "https://arxiv.org/abs/1805.05598",
    },
    {
        "id": "amorim_2014",
        "paper": "Amorim 2014, A continuous model of ant foraging with pheromones and trail formation",
        "url": "https://arxiv.org/abs/1402.5611",
    },
    {
        "id": "malickova_2015",
        "paper": "Malickova, Yates & Bodova 2015, A stochastic model of ant trail following with two pheromones",
        "url": "https://arxiv.org/abs/1508.06816",
    },
]


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


def mean(values):
    values = list(values)
    return sum(values) / len(values) if values else 0


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


PAPER_CONDITIONS_JS = """
(config) => {
  const pheroSum = (name) =>
    Math.round(antSim.world.pheromones[name].data.reduce((sum, value) => sum + value, 0));
  const sampleBranchPheromone = (y) => {
    let total = 0;
    for (let x = 620; x <= 960; x += 24) total += antSim.world.pheromones.food.sample(x, y);
    return Math.round(total);
  };
  const clearResources = () => {
    antSim.world.food = [];
    antSim.world.water = [];
    antSim.world.enemies = [];
    antSim.world.corpses = [];
    antSim.world.mills = [];
    antSim.world.rocks = [];
  };
  const baseMature = (seed, ants = 260) => {
    antSim.setSeed(seed);
    antSim.setParam('species', 'lasius');
    antSim.setParam('speed', 60);
    antSim.setParam('pheromoneStrength', 120);
    antSim.setParam('diffusionRate', 110);
    antSim.setParam('evaporationRate', 80);
    antSim.setParam('senseThreshold', 10);
    antSim.setParam('temperature', 26);
    antSim.setParam('humidity', 58);
    antSim.setParam('hunger', 95);
    antSim.setParam('broodDemand', 0);
    antSim.setupMatureColony();
    antSim.setParam('antCount', ants);
    clearResources();
    antSim.world.foodStore = 80;
    antSim.world.waterStore = 2000;
    antSim.world.eggs = 0;
    antSim.world.larvae = 0;
    antSim.world.pupae = 0;
    antSim.clearPheromones();
    antSim.addWater(320, 180, 5000);
  };
  const displacementProbe = (days, dt) => {
    const before = new Map();
    for (const ant of antSim.world.ants) before.set(ant.id, { x: ant.x, y: ant.y });
    antSim.runDays(days, dt);
    const distances = [];
    for (const ant of antSim.world.ants) {
      const prev = before.get(ant.id);
      if (prev) distances.push(Math.hypot(ant.x - prev.x, ant.y - prev.y));
    }
    return distances.length ? distances.reduce((a, b) => a + b, 0) / distances.length : 0;
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
  const runDoubleBridge = (seed, ants, biasBranch = null, biasStrength = 0) => {
    const gateX = 760;
    const midY = 390;
    baseMature(seed, ants);
    antSim.world.water = [];
    antSim.addFood(980, 390, config.foodAmount);
    for (let y = 310; y <= 470; y += 24) antSim.world.rocks.push({ x: gateX, y, r: 22 });
    seedBranch(biasBranch, biasStrength);
    const previous = new Map();
    for (const ant of antSim.world.ants) previous.set(ant.id, { x: ant.x, y: ant.y });
    const counts = { upper: 0, lower: 0, upperReturn: 0, lowerReturn: 0 };
    const chunks = Math.max(1, Math.round(config.bridgeDays / config.sampleDays));
    for (let i = 0; i < chunks; i++) {
      antSim.runDays(config.sampleDays, config.dt);
      for (const ant of antSim.world.ants) {
        const prev = previous.get(ant.id);
        if (prev && ((prev.x < gateX && ant.x >= gateX) || (prev.x > gateX && ant.x <= gateX))) {
          const branch = ant.y < midY ? 'upper' : 'lower';
          counts[branch] += 1;
          if (ant.carrying || ant.state === 'carrying food') counts[`${branch}Return`] += 1;
        }
        previous.set(ant.id, { x: ant.x, y: ant.y });
      }
    }
    const total = counts.upper + counts.lower;
    const returnTotal = counts.upperReturn + counts.lowerReturn;
    return {
      seed,
      ants,
      upper_crossings: counts.upper,
      lower_crossings: counts.lower,
      total_crossings: total,
      upper_return_crossings: counts.upperReturn,
      lower_return_crossings: counts.lowerReturn,
      return_crossings: returnTotal,
      selected_branch: counts.upper === counts.lower ? 'tie' : counts.upper > counts.lower ? 'upper' : 'lower',
      dominance: total ? Math.abs(counts.upper - counts.lower) / total : 0,
      return_dominance: returnTotal ? Math.abs(counts.upperReturn - counts.lowerReturn) / returnTotal : 0,
      food_trips: antSim.world.stats.foodTrips,
      food_collected: Math.round(antSim.world.stats.foodCollected),
      food_pheromone: pheroSum('food'),
      upper_food_pheromone: sampleBranchPheromone(260),
      lower_food_pheromone: sampleBranchPheromone(520),
      avg_traffic_load: antSim.collectStatsSnapshot().avg_traffic_load,
      traffic_max_cell: antSim.collectStatsSnapshot().traffic_max_cell,
    };
  };
  const applyNoiseProfile = (profile) => {
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

  const rows = [];

  for (const seed of config.seeds) {
    baseMature(seed, config.ants);
    antSim.addFood(980, 390, config.foodAmount);
    antSim.runDays(config.trailDays, config.dt);
    const trail = antSim.collectStatsSnapshot();
    rows.push({
      condition: 'single_food_trail',
      seed,
      ants: config.ants,
      food_trips: trail.food_trips,
      food_collected: trail.food_collected,
      carrying_food: trail.carrying_food,
      state_following_food_trail: trail.state_following_food_trail || 0,
      food_pheromone: trail.food_pheromone,
      nest_pheromone: trail.nest_pheromone,
      avg_traffic_load: trail.avg_traffic_load,
      traffic_max_cell: trail.traffic_max_cell,
    });

    const beforeFood = trail.food_pheromone;
    const beforeNest = trail.nest_pheromone;
    antSim.world.food = [];
    antSim.triggerRain();
    antSim.runDays(config.washoutDays, config.dt);
    const washout = antSim.collectStatsSnapshot();
    rows.push({
      condition: 'rain_food_removal_washout',
      seed,
      ants: antSim.world.ants.length,
      before_food_pheromone: beforeFood,
      after_food_pheromone: washout.food_pheromone,
      food_pheromone_ratio: beforeFood ? washout.food_pheromone / beforeFood : 0,
      before_nest_pheromone: beforeNest,
      after_nest_pheromone: washout.nest_pheromone,
      nest_pheromone_ratio: beforeNest ? washout.nest_pheromone / beforeNest : 0,
      food_trips: washout.food_trips,
      food_collected: washout.food_collected,
    });

    const biased = runDoubleBridge(seed, config.ants, 'upper', 350);
    rows.push({ condition: 'double_bridge_upper_bias', ...biased });

    const lowTraffic = runDoubleBridge(seed, config.lowDensityAnts, null, 0);
    rows.push({ condition: 'crowding_low_density_bridge', ...lowTraffic });
    const highTraffic = runDoubleBridge(seed, config.highDensityAnts, null, 0);
    rows.push({ condition: 'crowding_high_density_bridge', ...highTraffic });

    baseMature(seed, config.lowDensityAnts);
    antSim.addFood(980, 390, config.foodAmount);
    const lowSpeed = displacementProbe(config.speedProbeDays, config.dt);
    const lowSnap = antSim.collectStatsSnapshot();
    rows.push({
      condition: 'no_jam_low_density',
      seed,
      ants: config.lowDensityAnts,
      mean_displacement: lowSpeed,
      food_trips: lowSnap.food_trips,
      avg_traffic_load: lowSnap.avg_traffic_load,
      traffic_max_cell: lowSnap.traffic_max_cell,
    });

    baseMature(seed, config.highDensityAnts);
    antSim.addFood(980, 390, config.foodAmount);
    const highSpeed = displacementProbe(config.speedProbeDays, config.dt);
    const highSnap = antSim.collectStatsSnapshot();
    rows.push({
      condition: 'no_jam_high_density',
      seed,
      ants: config.highDensityAnts,
      mean_displacement: highSpeed,
      food_trips: highSnap.food_trips,
      avg_traffic_load: highSnap.avg_traffic_load,
      traffic_max_cell: highSnap.traffic_max_cell,
    });

    for (const profile of config.noiseProfiles) {
      baseMature(seed, config.ants);
      applyNoiseProfile(profile);
      antSim.addFood(config.initialFoodX, config.initialFoodY, config.foodAmount);
      const startInitialTrips = antSim.world.stats.foodTrips;
      antSim.runDays(config.stochasticPreDays, config.dt);
      const initial = antSim.collectStatsSnapshot();
      const initialTrips = initial.food_trips - startInitialTrips;
      antSim.world.food = [];
      antSim.addFood(config.relocatedFoodX, config.relocatedFoodY, config.foodAmount);
      const startRelocatedTrips = antSim.world.stats.foodTrips;
      antSim.runDays(config.adaptationDays, config.dt);
      const early = antSim.collectStatsSnapshot();
      const earlyTrips = early.food_trips - startRelocatedTrips;
      rows.push({
        condition: 'stochasticity_relocation',
        seed,
        profile,
        ants: config.ants,
        initial_food_trips: initialTrips,
        relocated_early_trips: earlyTrips,
        trips_vs_initial: initialTrips ? earlyTrips / initialTrips : 0,
        avg_turn_noise: early.avg_turn_noise,
        avg_base_turn_noise: early.avg_base_turn_noise,
        avg_exploration_drive: early.avg_exploration_drive,
        avg_traffic_load: early.avg_traffic_load,
        food_pheromone: early.food_pheromone,
        ants_with_food_memory: early.ants_with_food_memory,
      });
    }
  }
  return rows;
}
"""


def aggregate(raw_rows):
    by_condition = {}
    for row in raw_rows:
        by_condition.setdefault(row["condition"], []).append(row)

    summaries = []

    trail_rows = by_condition["single_food_trail"]
    trail_metrics = {
        "mean_food_trips": round(mean(float(r["food_trips"]) for r in trail_rows), 3),
        "mean_food_collected": round(mean(float(r["food_collected"]) for r in trail_rows), 3),
        "mean_food_pheromone": round(mean(float(r["food_pheromone"]) for r in trail_rows), 3),
        "mean_following_food_trail": round(mean(float(r["state_following_food_trail"]) for r in trail_rows), 3),
    }
    trail_pass = (
        trail_metrics["mean_food_trips"] >= 8
        and trail_metrics["mean_food_pheromone"] >= 5000
        and trail_metrics["mean_food_collected"] >= 15
    )
    summaries.append({
        "paper_id": "perna_2012",
        "paper": "Perna et al. 2012",
        "condition": "single_food_trail",
        "expected": "Local pheromone following should create food-trail recruitment and measurable trail reinforcement.",
        "status": "partial" if trail_pass else "fail",
        "observed": json.dumps(trail_metrics, ensure_ascii=False),
        "gap": "Matches trail reinforcement qualitatively, but the model does not yet export turn-angle vs. local left/right pheromone samples, so Weber-law response cannot be quantitatively tested.",
    })

    washout_rows = by_condition["rain_food_removal_washout"]
    washout_metrics = {
        "mean_food_pheromone_ratio": round(mean(float(r["food_pheromone_ratio"]) for r in washout_rows), 4),
        "mean_nest_pheromone_ratio": round(mean(float(r["nest_pheromone_ratio"]) for r in washout_rows), 4),
    }
    washout_status = "pass" if washout_metrics["mean_food_pheromone_ratio"] <= 0.45 else "partial"
    summaries.append({
        "paper_id": "amorim_2014",
        "paper": "Amorim 2014",
        "condition": "rain_food_removal_washout",
        "expected": "Food-trail field should rise during exploitation and decay when food is removed or chemical field is washed out.",
        "status": washout_status,
        "observed": json.dumps(washout_metrics, ensure_ascii=False),
        "gap": "Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.",
    })

    bridge_rows = by_condition["double_bridge_upper_bias"]
    upper_fraction = mean(1 if r["selected_branch"] == "upper" else 0 for r in bridge_rows)
    bridge_metrics = {
        "upper_selected_fraction": round(upper_fraction, 3),
        "mean_dominance": round(mean(float(r["dominance"]) for r in bridge_rows), 4),
        "mean_food_trips": round(mean(float(r["food_trips"]) for r in bridge_rows), 3),
    }
    bridge_status = "pass" if upper_fraction >= 0.67 and bridge_metrics["mean_dominance"] >= 0.2 else "partial"
    summaries.append({
        "paper_id": "deneubourg_goss_bridge",
        "paper": "Deneubourg/Goss/Beckers double-bridge paradigm",
        "condition": "double_bridge_upper_bias",
        "expected": "A connected initial trail bias should increase selection of the biased bridge through positive feedback.",
        "status": bridge_status,
        "observed": json.dumps(bridge_metrics, ensure_ascii=False),
        "gap": "Direction is testable, but validation still lacks digitized branch-choice probability curves from the original experiments.",
    })

    low_rows = by_condition["crowding_low_density_bridge"]
    high_rows = by_condition["crowding_high_density_bridge"]
    low_dom = mean(float(r["dominance"]) for r in low_rows)
    high_dom = mean(float(r["dominance"]) for r in high_rows)
    traffic_metrics = {
        "low_mean_dominance": round(low_dom, 4),
        "high_mean_dominance": round(high_dom, 4),
        "low_mean_crossings": round(mean(float(r["total_crossings"]) for r in low_rows), 3),
        "high_mean_crossings": round(mean(float(r["total_crossings"]) for r in high_rows), 3),
        "low_avg_traffic_load": round(mean(float(r["avg_traffic_load"]) for r in low_rows), 4),
        "high_avg_traffic_load": round(mean(float(r["avg_traffic_load"]) for r in high_rows), 4),
    }
    traffic_status = "pass" if high_dom <= low_dom + 0.15 and traffic_metrics["high_mean_crossings"] > traffic_metrics["low_mean_crossings"] else "partial"
    summaries.append({
        "paper_id": "dussutour_2004",
        "paper": "Dussutour et al. 2004",
        "condition": "crowding_bridge_density_shift",
        "expected": "Crowded foragers should use alternative traffic organization before food-return throughput collapses.",
        "status": traffic_status,
        "observed": json.dumps(traffic_metrics, ensure_ascii=False),
        "gap": "The model has traffic load and detours, but lacks explicit antennal contacts, lane discipline and collision-avoidance rules measured in crowded ant trails.",
    })

    low_speed_rows = by_condition["no_jam_low_density"]
    high_speed_rows = by_condition["no_jam_high_density"]
    low_disp = mean(float(r["mean_displacement"]) for r in low_speed_rows)
    high_disp = mean(float(r["mean_displacement"]) for r in high_speed_rows)
    speed_ratio = high_disp / low_disp if low_disp else 0
    speed_metrics = {
        "low_mean_displacement": round(low_disp, 4),
        "high_mean_displacement": round(high_disp, 4),
        "high_vs_low_displacement_ratio": round(speed_ratio, 4),
        "low_food_trips": round(mean(float(r["food_trips"]) for r in low_speed_rows), 3),
        "high_food_trips": round(mean(float(r["food_trips"]) for r in high_speed_rows), 3),
    }
    if speed_ratio >= 0.45:
        speed_status = "pass"
    elif speed_ratio >= 0.25:
        speed_status = "partial"
    else:
        speed_status = "fail"
    summaries.append({
        "paper_id": "john_2009",
        "paper": "John et al. 2009",
        "condition": "no_jam_density_speed",
        "expected": "Increasing trail density should not create a hard jammed phase; movement should degrade mildly, not collapse.",
        "status": speed_status,
        "observed": json.dumps(speed_metrics, ensure_ascii=False),
        "gap": "This is only a displacement proxy. Proper validation needs trail-segment speed/flow-density measurements and body-contact rules.",
    })

    stoch_rows = by_condition["stochasticity_relocation"]
    profile_metrics = {}
    for profile in sorted({r["profile"] for r in stoch_rows}):
        items = [r for r in stoch_rows if r["profile"] == profile]
        profile_metrics[profile] = {
            "mean_initial_food_trips": round(mean(float(r["initial_food_trips"]) for r in items), 3),
            "mean_relocated_early_trips": round(mean(float(r["relocated_early_trips"]) for r in items), 3),
            "mean_trips_vs_initial": round(mean(float(r["trips_vs_initial"]) for r in items), 4),
        }
    low_ratio = profile_metrics.get("low", {}).get("mean_trips_vs_initial", 0)
    diverse_ratio = profile_metrics.get("diverse", {}).get("mean_trips_vs_initial", 0)
    stoch_status = "pass" if diverse_ratio > low_ratio + 0.05 else "partial" if diverse_ratio >= low_ratio else "fail"
    summaries.append({
        "paper_id": "shiraishi_2018",
        "paper": "Shiraishi et al. 2018",
        "condition": "stochasticity_relocation",
        "expected": "A heterogeneous stochasticity distribution should improve adaptation after food relocation under some environments.",
        "status": stoch_status,
        "observed": json.dumps(profile_metrics, ensure_ascii=False),
        "gap": "The current check measures relative relocation adaptation. It does not yet fit the paper's environment-dependent optimal stochasticity distribution.",
    })

    summaries.append({
        "paper_id": "malickova_2015",
        "paper": "Malickova, Yates & Bodova 2015",
        "condition": "two-cue adaptation proxy",
        "expected": "Random motion plus pheromone signalling should permit adaptation to changed external conditions.",
        "status": stoch_status if washout_status == "pass" else "partial",
        "observed": json.dumps({
            "relocation_profiles": profile_metrics,
            "washout": washout_metrics,
        }, ensure_ascii=False),
        "gap": "The simulator separates food/nest/water fields, but it is not yet the exact two-pheromone mathematical model and lacks direct synchronization metrics.",
    })

    return summaries


def write_markdown(path, summaries, raw_output, json_output):
    lines = [
        "# Paper Condition Validation v1",
        "",
        "This report maps published ant-behaviour findings to reproducible simulation conditions. Status values mean:",
        "",
        "- `pass`: the current model matches the paper's qualitative direction under this condition.",
        "- `partial`: the direction is partly represented, but key measurements or mechanisms are missing.",
        "- `fail`: the current result contradicts the expected qualitative pattern.",
        "",
        f"Raw CSV: `{raw_output}`",
        f"JSON: `{json_output}`",
        "",
        "## Sources",
        "",
    ]
    for source in SOURCES:
        lines.append(f"- {source['id']}: {source['paper']} ({source['url']})")
    lines.extend(["", "## Results", ""])
    for row in summaries:
        lines.extend([
            f"### {row['paper_id']} - {row['condition']}",
            "",
            f"- Paper: {row['paper']}",
            f"- Status: `{row['status']}`",
            f"- Expected: {row['expected']}",
            f"- Observed: `{row['observed']}`",
            f"- Gap: {row['gap']}",
            "",
        ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Validate ant simulator conditions against multiple ant-behaviour papers.")
    parser.add_argument("--seeds", default="1-3")
    parser.add_argument("--output", default=str(ROOT / "outputs" / "paper_conditions_v1.csv"))
    parser.add_argument("--json-output", default=str(ROOT / "outputs" / "paper_conditions_v1.json"))
    parser.add_argument("--report-output", default=str(ROOT / "outputs" / "paper_conditions_report_v1.md"))
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()

    seeds = parse_seeds(args.seeds)
    if args.quick and len(seeds) > 2:
        seeds = seeds[:2]

    config = {
        "seeds": seeds,
        "ants": 240 if args.quick else 280,
        "lowDensityAnts": 120 if args.quick else 160,
        "highDensityAnts": 360 if args.quick else 520,
        "foodAmount": 1200,
        "dt": 9,
        "trailDays": 3 if args.quick else 4,
        "washoutDays": 0.7,
        "bridgeDays": 2.5 if args.quick else 3.5,
        "sampleDays": 0.1,
        "speedProbeDays": 0.45,
        "noiseProfiles": ["low", "medium", "high", "diverse"],
        "initialFoodX": 980,
        "initialFoodY": 250,
        "relocatedFoodX": 980,
        "relocatedFoodY": 540,
        "stochasticPreDays": 2.5 if args.quick else 3.5,
        "adaptationDays": 0.6,
    }

    server = None
    raw_rows = []
    try:
        server, url = start_server()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 820})
            page.goto(url, wait_until="domcontentloaded", timeout=90000)
            page.wait_for_function("window.antSim && window.antSim.runDays", timeout=30000)
            raw_rows = page.evaluate(PAPER_CONDITIONS_JS, config)
            browser.close()
    finally:
        if server:
            server.terminate()
            server.wait(timeout=5)

    summaries = aggregate(raw_rows)
    csv_output = Path(args.output)
    json_output = Path(args.json_output)
    report_output = Path(args.report_output)
    write_csv(csv_output, summaries)
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "config": config,
                "sources": SOURCES,
                "summaries": summaries,
                "raw_rows": raw_rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_markdown(report_output, summaries, csv_output, json_output)

    print(f"Wrote {csv_output}")
    print(f"Wrote {json_output}")
    print(f"Wrote {report_output}")
    for row in summaries:
        print(f"{row['status']:7} {row['paper_id']:24} {row['condition']}")


if __name__ == "__main__":
    main()
