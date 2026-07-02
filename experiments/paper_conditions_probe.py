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
        "id": "ramirez_2018",
        "paper": "Ramirez et al. 2018, Modeling tropotaxis in ant colonies: recruitment and trail formation",
        "url": "https://arxiv.org/abs/1811.00590",
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
    {
        "id": "kang_theraulaz_2015",
        "paper": "Kang & Theraulaz 2015, Dynamical models of task organization in social insect colonies",
        "url": "https://arxiv.org/abs/1511.04769",
    },
    {
        "id": "afek_2015",
        "paper": "Afek, Kecher & Sulamy 2015, Optimal and Resilient Pheromone Utilization in Ant Foraging",
        "url": "https://arxiv.org/abs/1507.00772",
    },
    {
        "id": "jimenez_romero_2015",
        "paper": "Jimenez-Romero et al. 2015, A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones",
        "url": "https://arxiv.org/abs/1507.08467",
    },
    {
        "id": "aswale_2022",
        "paper": "Aswale et al. 2022, Hacking the Colony: On the Disruptive Effect of Misleading Pheromone and How to Defend Against It",
        "url": "https://arxiv.org/abs/2202.01808",
    },
    {
        "id": "jackson_chaline_2007",
        "paper": "Jackson & Chaline 2007, Modulation of pheromone trail strength with food quality in Pharaoh's ant, Monomorium pharaonis",
        "url": "https://doi.org/10.1016/j.anbehav.2006.11.027",
    },
    {
        "id": "avanzi_2024",
        "paper": "Avanzi, Lisart & Detrain 2024, Social organization of necrophoresis: insights into disease risk management in ant societies",
        "url": "https://doi.org/10.1098/rsos.240764",
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
  const addPheromonePath = (fieldName, points, strength, spacing = 12) => {
    const field = antSim.world.pheromones[fieldName];
    for (let p = 0; p < points.length - 1; p++) {
      const [x1, y1] = points[p];
      const [x2, y2] = points[p + 1];
      const steps = Math.max(1, Math.ceil(Math.hypot(x2 - x1, y2 - y1) / spacing));
      for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        field.add(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, strength);
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
  const runTaskDemand = (seed, mode) => {
    baseMature(seed, config.ants);
    if (mode === 'brood') {
      antSim.setParam('broodDemand', 95);
      antSim.setParam('hunger', 20);
      antSim.world.eggs = 190;
      antSim.world.larvae = 140;
      antSim.world.pupae = 90;
      antSim.world.foodStore = 260;
      antSim.world.waterStore = 260;
    } else {
      antSim.setParam('broodDemand', 0);
      antSim.setParam('hunger', 95);
      antSim.world.eggs = 0;
      antSim.world.larvae = 0;
      antSim.world.pupae = 0;
      antSim.world.foodStore = 0;
      antSim.world.waterStore = 0;
      antSim.addFood(970, 300, config.foodAmount);
      antSim.addWater(970, 520, config.foodAmount);
    }
    antSim.runDays(config.taskDemandDays, config.dt);
    const snap = antSim.collectStatsSnapshot();
    return {
      condition: mode === 'brood' ? 'task_demand_brood' : 'task_demand_resource',
      seed,
      ants: snap.ants,
      task_brood: snap.task_brood || 0,
      task_food: snap.task_food || 0,
      task_water: snap.task_water || 0,
      task_corpse: snap.task_corpse || 0,
      state_brood_care: snap.state_brood_care || 0,
      state_following_food_trail: snap.state_following_food_trail || 0,
      state_following_water_trail: snap.state_following_water_trail || 0,
      food_trips: snap.food_trips,
      water_trips: snap.water_trips,
      brood_total: snap.brood_total,
      food_store: snap.food_store,
      water_store: snap.water_store,
    };
  };
  const runFailStopForaging = (seed, kill) => {
    baseMature(seed, config.failStopAnts);
    antSim.addFood(980, 390, config.foodAmount);
    antSim.addWater(320, 180, 5000);
    if (kill) {
      antSim.triggerMassDeath();
      antSim.runDays(0.1, config.dt);
    }
    const afterShock = antSim.collectStatsSnapshot();
    const startTrips = antSim.world.stats.foodTrips;
    const startCollected = antSim.world.stats.foodCollected;
    antSim.runDays(config.failStopDays, config.dt);
    const snap = antSim.collectStatsSnapshot();
    return {
      condition: kill ? 'fail_stop_mass_death' : 'fail_stop_control',
      seed,
      ants_after_shock: afterShock.ants,
      dead_after_shock: afterShock.dead,
      final_ants: snap.ants,
      final_dead: snap.dead,
      phase_food_trips: snap.food_trips - startTrips,
      phase_food_collected: Math.round(snap.food_collected - startCollected),
      corpse_moves: snap.corpse_moves,
      nest_corpses: snap.nest_corpses,
      disposed_corpses: snap.disposed_corpses,
      death_pheromone: snap.death_pheromone,
    };
  };
  const runAvoidSignal = (seed, enabled) => {
    baseMature(seed, config.ants);
    antSim.world.water = [];
    antSim.addFood(980, 390, config.foodAmount);
    if (enabled) {
      for (let y = 210; y <= 570; y += 16) {
        antSim.world.pheromones.avoid.add(620, y, 360);
      }
    }
    let hazardOccupancy = 0;
    let samples = 0;
    const chunks = Math.max(1, Math.round(config.avoidDays / config.sampleDays));
    for (let i = 0; i < chunks; i++) {
      antSim.runDays(config.sampleDays, config.dt);
      hazardOccupancy += antSim.world.ants.filter(ant => Math.abs(ant.x - 620) < 45 && ant.y > 205 && ant.y < 575).length;
      samples += 1;
    }
    const snap = antSim.collectStatsSnapshot();
    return {
      condition: enabled ? 'negative_pheromone_avoid' : 'negative_pheromone_control',
      seed,
      ants: snap.ants,
      mean_hazard_occupancy: samples ? hazardOccupancy / samples : 0,
      food_trips: snap.food_trips,
      food_collected: snap.food_collected,
      avoid_pheromone: snap.avoid_pheromone,
      food_pheromone: snap.food_pheromone,
      avg_traffic_load: snap.avg_traffic_load,
    };
  };
  const runMisleadingPheromone = (seed, mode) => {
    baseMature(seed, config.ants);
    antSim.world.water = [];
    antSim.addFood(980, 545, config.foodAmount);
    const fakePath = [
      [antSim.world.nest.x, antSim.world.nest.y],
      [610, 250],
      [880, 190],
      [1000, 175],
    ];
    if (mode !== 'control') {
      addPheromonePath('food', fakePath, config.fakeTrailStrength, 10);
    }
    if (mode === 'caution') {
      addPheromonePath('avoid', fakePath, config.fakeTrailStrength * 0.92, 10);
    }
    let fakeOccupancy = 0;
    let realApproachOccupancy = 0;
    let samples = 0;
    const chunks = Math.max(1, Math.round(config.misleadingDays / config.sampleDays));
    for (let i = 0; i < chunks; i++) {
      antSim.runDays(config.sampleDays, config.dt);
      fakeOccupancy += antSim.world.ants.filter(ant => ant.y < 285 && ant.x > 520 && ant.x < 1030).length;
      realApproachOccupancy += antSim.world.ants.filter(ant => ant.y > 455 && ant.x > 650 && ant.x < 1030).length;
      samples += 1;
    }
    const snap = antSim.collectStatsSnapshot();
    return {
      condition: `misleading_pheromone_${mode}`,
      seed,
      ants: snap.ants,
      mean_fake_path_occupancy: samples ? fakeOccupancy / samples : 0,
      mean_real_approach_occupancy: samples ? realApproachOccupancy / samples : 0,
      food_trips: snap.food_trips,
      food_collected: snap.food_collected,
      food_pheromone: snap.food_pheromone,
      avoid_pheromone: snap.avoid_pheromone,
    };
  };
  const runFoodQuality = (seed) => {
    baseMature(seed, config.ants);
    antSim.world.water = [];
    antSim.world.foodStore = 0;
    antSim.world.waterStore = 2000;
    antSim.addFood(940, 260, config.foodAmount, { quality: 1.8, label: 'high_quality' });
    antSim.addFood(940, 520, config.foodAmount, { quality: 0.55, label: 'low_quality' });
    antSim.runDays(config.foodQualityDays, config.dt);
    const snap = antSim.collectStatsSnapshot();
    return {
      condition: 'food_quality_recruitment',
      seed,
      ants: snap.ants,
      food_trips: snap.food_trips,
      high_quality_food_trips: snap.high_quality_food_trips,
      low_quality_food_trips: snap.low_quality_food_trips,
      high_quality_food_collected: snap.high_quality_food_collected,
      low_quality_food_collected: snap.low_quality_food_collected,
      avg_collected_food_quality: snap.avg_collected_food_quality,
      high_quality_food_remaining: snap.high_quality_food_remaining,
      low_quality_food_remaining: snap.low_quality_food_remaining,
      food_quality_collected: snap.food_quality_collected,
      food_pheromone: snap.food_pheromone,
      high_source_food_pheromone: Math.round(antSim.world.pheromones.food.sample(940, 260)),
      low_source_food_pheromone: Math.round(antSim.world.pheromones.food.sample(940, 520)),
    };
  };
  const runNecrophoresis = (seed) => {
    baseMature(seed, config.ants);
    antSim.world.food = [];
    antSim.world.water = [];
    antSim.world.foodStore = 260;
    antSim.world.waterStore = 260;
    antSim.world.corpses = [];
    const corpseCount = config.corpseCount;
    for (let i = 0; i < corpseCount; i++) {
      const a = i / corpseCount * Math.PI * 2;
      const r = 38 + (i % 4) * 18;
      const x = antSim.world.nest.x + Math.cos(a) * r;
      const y = antSim.world.nest.y + Math.sin(a) * r;
      antSim.world.corpses.push({
        id: i + 1,
        x,
        y,
        role: 'worker',
        age: 0,
        carriedBy: null,
        disposed: false,
        chemical: 135,
      });
      antSim.world.pheromones.death.add(x, y, 130);
    }
    const start = antSim.collectStatsSnapshot();
    antSim.runDays(config.necrophoresisDays, config.dt);
    const snap = antSim.collectStatsSnapshot();
    return {
      condition: 'necrophoresis_cleanup_latency',
      seed,
      ants: snap.ants,
      initial_corpses: corpseCount,
      initial_nest_corpses: start.nest_corpses,
      final_nest_corpses: snap.nest_corpses,
      disposed_corpses: snap.disposed_corpses,
      corpse_moves: snap.corpse_moves,
      death_pheromone: snap.death_pheromone,
      task_corpse: snap.task_corpse || 0,
      state_corpse_cleanup: snap.state_corpse_cleanup || 0,
      state_carrying_corpse: snap.state_carrying_corpse || 0,
    };
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

    rows.push(runTaskDemand(seed, 'brood'));
    rows.push(runTaskDemand(seed, 'resource'));
    rows.push(runFailStopForaging(seed, false));
    rows.push(runFailStopForaging(seed, true));
    rows.push(runAvoidSignal(seed, false));
    rows.push(runAvoidSignal(seed, true));
    rows.push(runMisleadingPheromone(seed, 'control'));
    rows.push(runMisleadingPheromone(seed, 'attack'));
    rows.push(runMisleadingPheromone(seed, 'caution'));
    rows.push(runFoodQuality(seed));
    rows.push(runNecrophoresis(seed));
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

    summaries.append({
        "paper_id": "ramirez_2018",
        "paper": "Ramirez et al. 2018",
        "condition": "tropotaxis_gradient_response_proxy",
        "expected": "A gradient-sensitive pheromone response should yield recruitment to newly found food sources and colony-level trail networks.",
        "status": "partial" if trail_pass else "fail",
        "observed": json.dumps(trail_metrics, ensure_ascii=False),
        "gap": "The model uses left/right/front sampling and forms trails, but does not yet export local gradient vectors or per-step orientation changes needed to fit the tropotaxis equations.",
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

    brood_rows = by_condition["task_demand_brood"]
    resource_rows = by_condition["task_demand_resource"]
    brood_task = mean(float(r["task_brood"]) for r in brood_rows)
    resource_brood_task = mean(float(r["task_brood"]) for r in resource_rows)
    resource_foraging_task = mean(float(r["task_food"]) + float(r["task_water"]) for r in resource_rows)
    brood_foraging_task = mean(float(r["task_food"]) + float(r["task_water"]) for r in brood_rows)
    task_metrics = {
        "brood_condition_mean_task_brood": round(brood_task, 3),
        "resource_condition_mean_task_brood": round(resource_brood_task, 3),
        "brood_condition_mean_food_water_tasks": round(brood_foraging_task, 3),
        "resource_condition_mean_food_water_tasks": round(resource_foraging_task, 3),
        "brood_condition_mean_brood_total": round(mean(float(r["brood_total"]) for r in brood_rows), 3),
        "resource_condition_mean_food_trips": round(mean(float(r["food_trips"]) for r in resource_rows), 3),
        "resource_condition_mean_water_trips": round(mean(float(r["water_trips"]) for r in resource_rows), 3),
    }
    task_status = "pass" if brood_task > resource_brood_task and resource_foraging_task > brood_foraging_task else "fail"
    summaries.append({
        "paper_id": "kang_theraulaz_2015",
        "paper": "Kang & Theraulaz 2015",
        "condition": "task_demand_reallocation",
        "expected": "Task allocation should shift with external task demand: brood demand should recruit brood work, resource shortage should recruit food/water work.",
        "status": task_status,
        "observed": json.dumps(task_metrics, ensure_ascii=False),
        "gap": "The model has response-threshold-like task switching, but does not yet estimate worker-worker contact matrices or explicit task-switching rates.",
    })

    control_rows = by_condition["fail_stop_control"]
    death_rows = by_condition["fail_stop_mass_death"]
    control_trips = mean(float(r["phase_food_trips"]) for r in control_rows)
    death_trips = mean(float(r["phase_food_trips"]) for r in death_rows)
    resilience_ratio = death_trips / control_trips if control_trips else 0
    fail_stop_metrics = {
        "control_mean_food_trips": round(control_trips, 3),
        "mass_death_mean_food_trips": round(death_trips, 3),
        "trip_resilience_ratio": round(resilience_ratio, 4),
        "mass_death_mean_dead_after_shock": round(mean(float(r["dead_after_shock"]) for r in death_rows), 3),
        "mass_death_mean_corpse_moves": round(mean(float(r["corpse_moves"]) for r in death_rows), 3),
        "mass_death_mean_disposed_corpses": round(mean(float(r["disposed_corpses"]) for r in death_rows), 3),
    }
    fail_stop_status = "pass" if resilience_ratio >= 0.25 and death_trips > 0 else "partial" if death_trips > 0 else "fail"
    summaries.append({
        "paper_id": "afek_2015",
        "paper": "Afek, Kecher & Sulamy 2015",
        "condition": "fail_stop_foraging_resilience",
        "expected": "After a fraction of ants fail-stop, remaining ants should still be able to forage, with reduced but nonzero throughput.",
        "status": fail_stop_status,
        "observed": json.dumps(fail_stop_metrics, ensure_ascii=False),
        "gap": "Afek et al. is an algorithmic pheromone model; this ABM only tests biological-style degradation, not asymptotic pheromone lower bounds or proof-level optimality.",
    })

    avoid_control_rows = by_condition["negative_pheromone_control"]
    avoid_rows = by_condition["negative_pheromone_avoid"]
    control_occupancy = mean(float(r["mean_hazard_occupancy"]) for r in avoid_control_rows)
    avoid_occupancy = mean(float(r["mean_hazard_occupancy"]) for r in avoid_rows)
    occupancy_ratio = avoid_occupancy / control_occupancy if control_occupancy else 0
    avoid_metrics = {
        "control_mean_hazard_occupancy": round(control_occupancy, 3),
        "avoid_mean_hazard_occupancy": round(avoid_occupancy, 3),
        "avoid_vs_control_occupancy_ratio": round(occupancy_ratio, 4),
        "control_mean_food_trips": round(mean(float(r["food_trips"]) for r in avoid_control_rows), 3),
        "avoid_mean_food_trips": round(mean(float(r["food_trips"]) for r in avoid_rows), 3),
        "avoid_mean_avoid_pheromone": round(mean(float(r["avoid_pheromone"]) for r in avoid_rows), 3),
    }
    avoid_status = "pass" if occupancy_ratio <= 0.8 else "partial" if occupancy_ratio <= 1.0 else "fail"
    summaries.append({
        "paper_id": "jimenez_romero_2015",
        "paper": "Jimenez-Romero et al. 2015",
        "condition": "negative_pheromone_forbidden_path",
        "expected": "A second negative pheromone should reduce use of forbidden or unrewarding path regions without permanently blocking foraging.",
        "status": avoid_status,
        "observed": json.dumps(avoid_metrics, ensure_ascii=False),
        "gap": "The simulator has an avoid field, but it is not yet paired with individual learning or neural-controller adaptation as in the paper.",
    })

    mislead_control = by_condition["misleading_pheromone_control"]
    mislead_attack = by_condition["misleading_pheromone_attack"]
    mislead_caution = by_condition["misleading_pheromone_caution"]
    control_trips = mean(float(r["food_trips"]) for r in mislead_control)
    attack_trips = mean(float(r["food_trips"]) for r in mislead_attack)
    caution_trips = mean(float(r["food_trips"]) for r in mislead_caution)
    attack_damage_ratio = attack_trips / control_trips if control_trips else 0
    caution_recovery_ratio = caution_trips / attack_trips if attack_trips else 0
    misleading_metrics = {
        "control_mean_food_trips": round(control_trips, 3),
        "attack_mean_food_trips": round(attack_trips, 3),
        "caution_mean_food_trips": round(caution_trips, 3),
        "attack_vs_control_trip_ratio": round(attack_damage_ratio, 4),
        "caution_vs_attack_trip_ratio": round(caution_recovery_ratio, 4),
        "attack_mean_fake_path_occupancy": round(mean(float(r["mean_fake_path_occupancy"]) for r in mislead_attack), 3),
        "caution_mean_fake_path_occupancy": round(mean(float(r["mean_fake_path_occupancy"]) for r in mislead_caution), 3),
    }
    attack_visible = attack_damage_ratio < 0.92 or misleading_metrics["attack_mean_fake_path_occupancy"] > misleading_metrics["caution_mean_fake_path_occupancy"]
    caution_visible = caution_recovery_ratio > 1.08 or misleading_metrics["caution_mean_fake_path_occupancy"] < misleading_metrics["attack_mean_fake_path_occupancy"] * 0.9
    if attack_visible and caution_visible:
        misleading_status = "pass"
    elif attack_visible or caution_visible:
        misleading_status = "partial"
    else:
        misleading_status = "fail"
    summaries.append({
        "paper_id": "aswale_2022",
        "paper": "Aswale et al. 2022",
        "condition": "misleading_pheromone_attack_and_caution",
        "expected": "Misleading food pheromone should disrupt foraging; a cautionary/avoid signal should limit, but not necessarily eliminate, the disruption.",
        "status": misleading_status,
        "observed": json.dumps(misleading_metrics, ensure_ascii=False),
        "gap": "The current attack is a static fake trail rather than active detractor agents, and the avoid field is only a proxy for cautionary pheromone.",
    })

    const_food_rows = by_condition["food_quality_recruitment"]
    food_quality_metrics = {
        "mean_high_quality_food_trips": round(mean(float(r["high_quality_food_trips"]) for r in const_food_rows), 3),
        "mean_low_quality_food_trips": round(mean(float(r["low_quality_food_trips"]) for r in const_food_rows), 3),
        "mean_avg_collected_food_quality": round(mean(float(r["avg_collected_food_quality"]) for r in const_food_rows), 4),
        "mean_high_source_food_pheromone": round(mean(float(r["high_source_food_pheromone"]) for r in const_food_rows), 3),
        "mean_low_source_food_pheromone": round(mean(float(r["low_source_food_pheromone"]) for r in const_food_rows), 3),
    }
    high_trips = food_quality_metrics["mean_high_quality_food_trips"]
    low_trips = food_quality_metrics["mean_low_quality_food_trips"]
    high_pheromone = food_quality_metrics["mean_high_source_food_pheromone"]
    low_pheromone = food_quality_metrics["mean_low_source_food_pheromone"]
    food_quality_status = "pass" if high_trips > low_trips * 1.15 and food_quality_metrics["mean_avg_collected_food_quality"] > 1.05 else "partial" if high_trips >= low_trips or high_pheromone >= low_pheromone else "fail"
    summaries.append({
        "paper_id": "jackson_chaline_2007",
        "paper": "Jackson & Chaline 2007",
        "condition": "food_quality_recruitment",
        "expected": "Higher-quality food should produce stronger recruitment or higher-quality-biased collection than lower-quality food at comparable access cost.",
        "status": food_quality_status,
        "observed": json.dumps(food_quality_metrics, ensure_ascii=False),
        "gap": "The simulator now has food quality and quality-weighted recruitment, but it still lacks species-specific sucrose concentration calibration and direct trail-laying event counts.",
    })

    corpse_rows = by_condition["necrophoresis_cleanup_latency"]
    corpse_metrics = {
        "mean_initial_nest_corpses": round(mean(float(r["initial_nest_corpses"]) for r in corpse_rows), 3),
        "mean_final_nest_corpses": round(mean(float(r["final_nest_corpses"]) for r in corpse_rows), 3),
        "mean_disposed_corpses": round(mean(float(r["disposed_corpses"]) for r in corpse_rows), 3),
        "mean_corpse_moves": round(mean(float(r["corpse_moves"]) for r in corpse_rows), 3),
        "mean_death_pheromone": round(mean(float(r["death_pheromone"]) for r in corpse_rows), 3),
    }
    corpse_status = "pass" if corpse_metrics["mean_disposed_corpses"] >= 12 and corpse_metrics["mean_final_nest_corpses"] <= corpse_metrics["mean_initial_nest_corpses"] * 0.7 else "partial" if corpse_metrics["mean_corpse_moves"] > 0 else "fail"
    summaries.append({
        "paper_id": "avanzi_2024",
        "paper": "Avanzi, Lisart & Detrain 2024",
        "condition": "necrophoresis_cleanup_latency",
        "expected": "Workers should respond to corpse/death chemical cues and progressively remove corpses from the nest area.",
        "status": corpse_status,
        "observed": json.dumps(corpse_metrics, ensure_ascii=False),
        "gap": "Corpse relocation is represented, but the simulator still lacks pathogen state, corpse-age chemical profile calibration and colony-level interaction network validation.",
    })

    return summaries


def write_markdown(path, summaries, raw_output, json_output):
    lines = [
        "# Paper Condition Validation v4",
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
    parser.add_argument("--output", default=str(ROOT / "outputs" / "paper_conditions_v4.csv"))
    parser.add_argument("--json-output", default=str(ROOT / "outputs" / "paper_conditions_v4.json"))
    parser.add_argument("--report-output", default=str(ROOT / "outputs" / "paper_conditions_report_v4.md"))
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()

    seeds = parse_seeds(args.seeds)
    if args.quick and len(seeds) > 2:
        seeds = seeds[:2]

    config = {
        "seeds": seeds,
        "ants": 180 if args.quick else 280,
        "lowDensityAnts": 90 if args.quick else 160,
        "highDensityAnts": 260 if args.quick else 520,
        "foodAmount": 1200,
        "dt": 9,
        "trailDays": 2.2 if args.quick else 4,
        "washoutDays": 0.7,
        "bridgeDays": 1.8 if args.quick else 3.5,
        "sampleDays": 0.2 if args.quick else 0.1,
        "speedProbeDays": 0.45,
        "noiseProfiles": ["low", "medium", "high", "diverse"],
        "initialFoodX": 980,
        "initialFoodY": 250,
        "relocatedFoodX": 980,
        "relocatedFoodY": 540,
        "stochasticPreDays": 1.8 if args.quick else 3.5,
        "adaptationDays": 0.6,
        "taskDemandDays": 0.6 if args.quick else 1.2,
        "failStopAnts": 200 if args.quick else 320,
        "failStopDays": 0.8 if args.quick else 1.6,
        "avoidDays": 0.8 if args.quick else 1.8,
        "misleadingDays": 0.6 if args.quick else 1.5,
        "foodQualityDays": 1.4 if args.quick else 2.2,
        "corpseCount": 24 if args.quick else 36,
        "necrophoresisDays": 1.2 if args.quick else 2.0,
        "fakeTrailStrength": 700,
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
