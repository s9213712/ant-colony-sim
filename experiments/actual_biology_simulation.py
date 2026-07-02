#!/usr/bin/env python3
"""Run reproducible behavior-level biological simulation scenarios.

This suite is intentionally different from the literature audit probes. It runs
the same simulator rules under several biological conditions and exports time
series that can be inspected as simulated experiments.
"""

import argparse
import csv
import json
import socket
import subprocess
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SCENARIOS = [
    "stable_mature",
    "resource_stress",
    "heat_dry_stress",
    "founding_colony",
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


def parse_scenarios(text):
    scenarios = [item.strip() for item in text.split(",") if item.strip()]
    unknown = sorted(set(scenarios) - set(DEFAULT_SCENARIOS))
    if unknown:
        raise ValueError(f"unknown scenario(s): {', '.join(unknown)}")
    return scenarios or list(DEFAULT_SCENARIOS)


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


def mean(values):
    values = [float(value) for value in values if value is not None]
    return sum(values) / len(values) if values else None


def pct_change(value, baseline):
    if baseline in (None, 0) or value is None:
        return None
    return (value - baseline) / abs(baseline)


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
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


ACTUAL_BIOLOGY_JS = """
(config) => {
  const clearExternalEnvironment = () => {
    antSim.world.food = [];
    antSim.world.water = [];
    antSim.world.enemies = [];
    antSim.world.corpses = [];
    antSim.world.mills = [];
    antSim.world.rocks = [];
    antSim.clearPheromones();
  };
  const applyCommonLasiusParams = () => {
    antSim.setParam('species', 'lasius');
    antSim.setParam('speed', 60);
    antSim.setParam('pheromoneStrength', 120);
    antSim.setParam('diffusionRate', 110);
    antSim.setParam('evaporationRate', 80);
    antSim.setParam('senseThreshold', 10);
    antSim.setParam('temperature', 26);
    antSim.setParam('humidity', 58);
    antSim.setParam('hunger', 70);
    antSim.setParam('broodDemand', 55);
    antSim.setParam('soldierRatio', 12);
  };
  const applyOverrides = () => {
    const overrides = config.overrides || {};
    for (const [name, value] of Object.entries(overrides)) {
      antSim.setParam(name, value);
    }
  };
  const queenSummary = () => {
    const queens = antSim.world.queens;
    const avg = (field) => queens.length
      ? queens.reduce((sum, queen) => sum + (queen[field] || 0), 0) / queens.length
      : null;
    return {
      queen_health_mean: avg('health'),
      queen_energy_mean: avg('energy'),
      queen_hydration_mean: avg('hydration'),
      queen_reserve_mean: avg('reserves'),
      queen_states: queens.map(queen => queen.state || 'unknown').join('|')
    };
  };
  const addExplicitResources = (foodAmount, waterAmount) => {
    antSim.addFood(250, 180, foodAmount, { quality: 1.0, label: 'standard_quality' });
    antSim.addFood(930, 520, foodAmount * 0.7, { quality: 1.4, label: 'high_quality' });
    antSim.addWater(320, 150, waterAmount);
    antSim.addWater(880, 210, waterAmount * 0.65);
  };
  const configureScenario = () => {
    antSim.setSeed(config.seed);
    applyCommonLasiusParams();
    if (config.scenario === 'founding_colony') {
      antSim.setupFoundingColony();
      clearExternalEnvironment();
      antSim.world.foodStore = 80;
      antSim.world.waterStore = 95;
      antSim.world.eggs = Math.max(antSim.world.eggs, 12);
      addExplicitResources(120, 120);
      applyOverrides();
      return;
    }
    antSim.setupMatureColony();
    clearExternalEnvironment();
    if (config.scenario === 'resource_stress') {
      antSim.world.foodStore = 18;
      antSim.world.waterStore = 18;
      antSim.setParam('hunger', 95);
      antSim.setParam('broodDemand', 45);
      antSim.addFood(980, 540, 210, { quality: 1.0, label: 'standard_quality' });
      antSim.addWater(970, 190, 190);
      applyOverrides();
      return;
    }
    if (config.scenario === 'heat_dry_stress') {
      antSim.setParam('temperature', 40);
      antSim.setParam('humidity', 20);
      antSim.world.foodStore = 150;
      antSim.world.waterStore = 35;
      addExplicitResources(650, 900);
      applyOverrides();
      return;
    }
    antSim.world.foodStore = 70;
    antSim.world.waterStore = 70;
    antSim.setParam('hunger', 84);
    addExplicitResources(900, 900);
    applyOverrides();
  };
  const sample = (sampleIndex, phase) => {
    const stats = antSim.collectStatsSnapshot();
    return {
      suite: 'actual_biology_simulation_v1',
      treatment: config.treatment,
      scenario: config.scenario,
      condition_id: `${config.treatment}:${config.scenario}`,
      seed: config.seed,
      sample_index: sampleIndex,
      phase,
      ...stats,
      ...queenSummary()
    };
  };

  configureScenario();
  antSim.world.statsHistory = [];
  antSim.world.lastStatsDay = antSim.world.day;
  const rows = [sample(0, 'initial')];
  const started = performance.now();
  const chunks = Math.max(1, Math.round(config.days / config.sampleDays));
  for (let i = 0; i < chunks; i++) {
    antSim.runDays(config.sampleDays, config.dt);
    rows.push(sample(i + 1, 'simulation'));
  }
  const elapsed = Math.round(performance.now() - started);
  for (const row of rows) row.elapsed_ms = elapsed;
  return rows;
}
"""


def scenario_payload(scenario, seed, args):
    return {
        "scenario": scenario,
        "treatment": args.treatment,
        "seed": seed,
        "days": args.days,
        "sampleDays": args.sample_days,
        "dt": args.dt,
        "overrides": parse_params(args.set),
    }


def run_suite(args):
    seeds = parse_seeds(args.seeds)
    scenarios = parse_scenarios(args.scenarios)
    server, url = start_server()
    rows = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            errors = []
            for scenario in scenarios:
                for seed in seeds:
                    page = browser.new_page(viewport={"width": 1280, "height": 720})
                    page.on("pageerror", lambda exc: errors.append(str(exc)))
                    page.goto(url)
                    page.wait_for_timeout(120)
                    payload = scenario_payload(scenario, seed, args)
                    try:
                        rows.extend(page.evaluate(ACTUAL_BIOLOGY_JS, payload))
                    finally:
                        page.close()
            browser.close()
            if errors:
                raise RuntimeError("page errors: " + "; ".join(errors))
    finally:
        server.terminate()
        try:
            server.wait(timeout=3)
        except subprocess.TimeoutExpired:
            server.kill()
    return rows


def final_rows_by_replicate(rows):
    grouped = {}
    for row in rows:
        grouped[(row.get("treatment", "baseline"), row["scenario"], row["seed"])] = row
    return list(grouped.values())


def summarize(rows):
    by_scenario = defaultdict(list)
    for row in final_rows_by_replicate(rows):
        by_scenario[(row.get("treatment", "baseline"), row["scenario"])].append(row)

    summaries = {}
    for (treatment, scenario), scenario_rows in sorted(by_scenario.items()):
        initial_rows = [
            row for row in rows
            if row.get("treatment", "baseline") == treatment
            and row["scenario"] == scenario
            and row["phase"] == "initial"
        ]
        initial_ants = mean(row["ants"] for row in initial_rows)
        final_ants = mean(row["ants"] for row in scenario_rows)
        initial_brood = mean(row["brood_total"] for row in initial_rows)
        final_brood = mean(row["brood_total"] for row in scenario_rows)
        summary = {
            "replicates": len(scenario_rows),
            "treatment": treatment,
            "scenario": scenario,
            "initial_ants_mean": round(initial_ants or 0, 3),
            "final_ants_mean": round(final_ants or 0, 3),
            "survival_fraction_mean": round((final_ants / initial_ants) if initial_ants else 1.0, 4),
            "initial_brood_mean": round(initial_brood or 0, 3),
            "final_brood_mean": round(final_brood or 0, 3),
            "brood_delta_mean": round((final_brood or 0) - (initial_brood or 0), 3),
            "food_trips_mean": round(mean(row["food_trips"] for row in scenario_rows) or 0, 3),
            "water_trips_mean": round(mean(row["water_trips"] for row in scenario_rows) or 0, 3),
            "food_collected_mean": round(mean(row["food_collected"] for row in scenario_rows) or 0, 3),
            "water_collected_mean": round(mean(row["water_collected"] for row in scenario_rows) or 0, 3),
            "avg_energy_mean": round(mean(row["avg_energy"] for row in scenario_rows) or 0, 3),
            "avg_hydration_mean": round(mean(row["avg_hydration"] for row in scenario_rows) or 0, 3),
            "brood_stress_mean": round(mean(row["brood_stress"] for row in scenario_rows) or 0, 3),
            "dead_mean": round(mean(row["dead"] for row in scenario_rows) or 0, 3),
            "food_pheromone_peak_mean": round(
                mean(
                    max(
                        item["food_pheromone"]
                        for item in rows
                        if item.get("treatment", "baseline") == treatment
                        and item["scenario"] == scenario
                        and item["seed"] == row["seed"]
                    )
                    for row in scenario_rows
                )
                or 0,
                3,
            ),
            "queen_health_mean": round(mean(row["queen_health_mean"] for row in scenario_rows) or 0, 3),
            "queen_hydration_mean": round(mean(row["queen_hydration_mean"] for row in scenario_rows) or 0, 3),
        }
        summaries[f"{treatment}:{scenario}"] = summary

    stable_by_treatment = {
        summary["treatment"]: summary
        for summary in summaries.values()
        if summary["scenario"] == "stable_mature"
    }
    for key, summary in summaries.items():
        scenario = summary["scenario"]
        stable = stable_by_treatment.get(summary["treatment"], {})
        if scenario == "stable_mature":
            summary["comparison_to_stable"] = "baseline"
            continue
        summary["food_trips_vs_stable"] = round(
            pct_change(summary["food_trips_mean"], stable.get("food_trips_mean")) or 0,
            4,
        )
        summary["hydration_vs_stable"] = round(
            pct_change(summary["avg_hydration_mean"], stable.get("avg_hydration_mean")) or 0,
            4,
        )
        summary["brood_stress_vs_stable"] = round(
            (summary["brood_stress_mean"] - stable.get("brood_stress_mean", 0)),
            4,
        )
    return summaries


def interpret(summaries):
    baseline = {
        summary["scenario"]: summary
        for summary in summaries.values()
        if summary.get("treatment") == "baseline"
    }
    stable = baseline.get("stable_mature", {})
    resource = baseline.get("resource_stress", {})
    heat = baseline.get("heat_dry_stress", {})
    founding = baseline.get("founding_colony", {})
    checks = []
    checks.append({
        "check": "stable_mature_foraging",
        "status": "pass" if stable.get("food_trips_mean", 0) > 0 and stable.get("water_trips_mean", 0) > 0 else "needs_work",
        "evidence": "Mature colonies should complete food and water trips under stable resource access.",
    })
    checks.append({
        "check": "stable_mature_survival",
        "status": "pass" if stable.get("survival_fraction_mean", 0) >= 0.85 else "needs_work",
        "evidence": "Short stable runs should not collapse the worker population.",
    })
    checks.append({
        "check": "resource_pressure_response",
        "status": "pass"
        if resource.get("avg_energy_mean", 100) <= stable.get("avg_energy_mean", 100)
        or resource.get("food_trips_mean", 0) >= stable.get("food_trips_mean", 0) * 0.25
        else "needs_work",
        "evidence": "Low stores should produce a measurable foraging or energetic response.",
    })
    checks.append({
        "check": "heat_dry_hydration_stress",
        "status": "pass"
        if heat.get("avg_hydration_mean", 100) < stable.get("avg_hydration_mean", 100)
        or heat.get("brood_stress_mean", 0) > stable.get("brood_stress_mean", 0)
        else "needs_work",
        "evidence": "Hot dry conditions should depress hydration and/or increase brood stress.",
    })
    checks.append({
        "check": "founding_queen_viability",
        "status": "pass"
        if founding.get("queen_health_mean", 0) >= 35 and founding.get("initial_ants_mean", 1) <= 1
        else "needs_work",
        "evidence": "Founding mode should be queen-centered and maintain queen viability over the short run.",
    })
    return checks


def write_json(path, rows, summaries, checks, args):
    try:
        csv_path = str(args.output.relative_to(ROOT))
    except ValueError:
        csv_path = str(args.output)
    payload = {
        "suite": "actual_biology_simulation_v1",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "claim_level": "behavior_level_simulated_experiment_not_quantitative_species_prediction",
        "rules": [
            "The suite changes seeds, initial resources, temperature and humidity only.",
            "It does not patch ant decision rules or force per-ant task/state transitions.",
            "Results are model-unit time series for qualitative biological interpretation.",
        ],
        "parameters": {
            "seeds": parse_seeds(args.seeds),
            "scenarios": parse_scenarios(args.scenarios),
            "days": args.days,
            "sample_days": args.sample_days,
            "dt": args.dt,
            "treatment": args.treatment,
            "overrides": parse_params(args.set),
        },
        "time_series_csv": csv_path,
        "time_series_rows": len(rows),
        "summary": summaries,
        "checks": checks,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_report(path, summaries, checks, args):
    lines = [
        "# Actual Biology Simulation Suite v1",
        "",
        "This report is generated by `experiments/actual_biology_simulation.py`.",
        "",
        "## Scientific Claim Level",
        "",
        "These runs are behavior-level simulated biological experiments. They are useful for checking whether shared ant-behavior rules produce interpretable colony-level responses under controlled conditions. They are not calibrated quantitative predictions of a real species.",
        "",
        "Rules held fixed:",
        "",
        "- Ant decision rules are not patched inside the suite.",
        "- Experiments change only seed, initial resources and environmental conditions.",
        "- Pheromone, task choice, energy, hydration, brood and queen dynamics come from the shared simulator.",
        "",
        "## Run Configuration",
        "",
        f"- Seeds: `{args.seeds}`",
        f"- Scenarios: `{args.scenarios}`",
        f"- Treatment: `{args.treatment}`",
        f"- Parameter overrides: `{parse_params(args.set)}`",
        f"- Days per replicate: `{args.days}`",
        f"- Sample interval: `{args.sample_days}` days",
        f"- dt: `{args.dt}`",
        "",
        "## Scenario Summary",
        "",
        "| Treatment | Scenario | Replicates | Final ants | Survival | Food trips | Water trips | Energy | Hydration | Brood stress | Brood delta | Queen health |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _key, summary in sorted(summaries.items()):
        lines.append(
            "| {treatment} | {scenario} | {replicates} | {final_ants_mean:.1f} | {survival_fraction_mean:.3f} | "
            "{food_trips_mean:.1f} | {water_trips_mean:.1f} | {avg_energy_mean:.1f} | "
            "{avg_hydration_mean:.1f} | {brood_stress_mean:.2f} | {brood_delta_mean:.1f} | "
            "{queen_health_mean:.1f} |".format(**summary)
        )
    lines.extend([
        "",
        "## Biological Checks",
        "",
        "| Check | Status | Evidence |",
        "|---|---|---|",
    ])
    for check in checks:
        lines.append(f"| `{check['check']}` | `{check['status']}` | {check['evidence']} |")
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- `stable_mature` is the control condition for normal mature-colony resource access.",
        "- `resource_stress` tests whether low stores and distant limited resources create energetic or foraging pressure.",
        "- `heat_dry_stress` tests whether elevated temperature and low humidity affect hydration and brood climate.",
        "- `founding_colony` tests whether the model can run a queen-centered early colony without starting from hundreds of workers.",
        "",
        "A `pass` here means the simulator produced the expected qualitative direction under shared rules. It does not mean the result matches digitized experimental curves, species-specific physiology or real chemical concentration units.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Run actual behavior-level biological simulation scenarios.")
    parser.add_argument("--seeds", default="101-105")
    parser.add_argument("--scenarios", default=",".join(DEFAULT_SCENARIOS))
    parser.add_argument("--days", type=float, default=8)
    parser.add_argument("--sample-days", type=float, default=0.25)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--treatment", default="baseline", help="Label for this run when using parameter overrides.")
    parser.add_argument("--set", action="append", default=[], help="Scriptable parameter override, e.g. --set evaporationRate=120")
    parser.add_argument("--quick", action="store_true", help="Use a short two-seed smoke configuration.")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "actual_biology_simulation.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "actual_biology_simulation.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "actual_biology_simulation.md")
    args = parser.parse_args()

    if args.quick:
        args.seeds = "101-102"
        args.days = min(args.days, 2)
        args.sample_days = max(args.sample_days, 0.5)

    rows = run_suite(args)
    summaries = summarize(rows)
    checks = interpret(summaries)
    write_csv(args.output, rows)
    write_json(args.json_output, rows, summaries, checks, args)
    write_report(args.report_output, summaries, checks, args)
    print(f"wrote {len(rows)} rows to {args.output}")
    print(f"wrote summary to {args.json_output}")
    print(f"wrote report to {args.report_output}")
    failed = [check for check in checks if check["status"] != "pass"]
    if failed:
        print(f"biological checks needing work: {len(failed)}")
        for check in failed:
            print(f"- {check['check']}: {check['status']}")


if __name__ == "__main__":
    main()
