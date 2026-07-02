#!/usr/bin/env python3
"""Run a small sensitivity screen on behavior-level biological scenarios."""

import argparse
import csv
import json
import math
import time
from pathlib import Path
from types import SimpleNamespace

import actual_biology_simulation as biology


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_TREATMENTS = [
    {
        "name": "baseline",
        "description": "Current default behavior-level parameterization.",
        "set": [],
    },
    {
        "name": "fast_pheromone_loss",
        "description": "Higher evaporation and higher sensing threshold; tests trail fragility.",
        "set": ["evaporationRate=130", "senseThreshold=16"],
    },
    {
        "name": "persistent_pheromone",
        "description": "Lower evaporation and lower sensing threshold; tests trail persistence and possible over-commitment.",
        "set": ["evaporationRate=55", "senseThreshold=7"],
    },
    {
        "name": "high_diffusion",
        "description": "Higher diffusion; tests whether broadened gradients reduce trail precision.",
        "set": ["diffusionRate=170"],
    },
    {
        "name": "brood_demand_high",
        "description": "Higher brood-demand pressure; tests foraging versus brood-care tradeoff.",
        "set": ["broodDemand=85"],
    },
]


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


def normalize_effect(value, baseline):
    if baseline in (None, 0) or value is None:
        return None
    return (value - baseline) / abs(baseline)


def score_effects(summary):
    baseline = {
        row["scenario"]: row
        for row in summary.values()
        if row.get("treatment") == "baseline"
    }
    rows = []
    for key, row in sorted(summary.items()):
        scenario = row["scenario"]
        base = baseline.get(scenario)
        if not base:
            continue
        out = {
            "condition_id": key,
            "treatment": row["treatment"],
            "scenario": scenario,
            "replicates": row["replicates"],
            "food_trips_mean": row["food_trips_mean"],
            "water_trips_mean": row["water_trips_mean"],
            "avg_energy_mean": row["avg_energy_mean"],
            "avg_hydration_mean": row["avg_hydration_mean"],
            "brood_stress_mean": row["brood_stress_mean"],
            "brood_delta_mean": row["brood_delta_mean"],
            "food_pheromone_peak_mean": row["food_pheromone_peak_mean"],
        }
        for metric in [
            "food_trips_mean",
            "water_trips_mean",
            "avg_energy_mean",
            "avg_hydration_mean",
            "brood_stress_mean",
            "brood_delta_mean",
            "food_pheromone_peak_mean",
        ]:
            effect = normalize_effect(row.get(metric), base.get(metric))
            out[f"{metric}_relative_effect"] = None if effect is None else round(effect, 6)
        stress_lift = row.get("brood_stress_mean", 0) - base.get("brood_stress_mean", 0)
        trip_lift = normalize_effect(row.get("food_trips_mean"), base.get("food_trips_mean")) or 0
        hydration_lift = normalize_effect(row.get("avg_hydration_mean"), base.get("avg_hydration_mean")) or 0
        out["biological_sensitivity_score"] = round(abs(trip_lift) + abs(hydration_lift) + abs(stress_lift), 6)
        rows.append(out)
    return rows


def write_json(path, rows, effects, treatments, args):
    payload = {
        "suite": "actual_biology_sensitivity_v1",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "claim_level": "parameter_sensitivity_screen_not_parameter_fit",
        "rules": [
            "Treatments use the same simulator decision rules.",
            "Treatments change only public scriptable parameters through antSim.setParam.",
            "Effects are measured relative to the baseline treatment within each scenario.",
        ],
        "parameters": {
            "seeds": biology.parse_seeds(args.seeds),
            "scenarios": biology.parse_scenarios(args.scenarios),
            "days": args.days,
            "sample_days": args.sample_days,
            "dt": args.dt,
        },
        "treatments": treatments,
        "time_series_csv": str(args.output.relative_to(ROOT)) if args.output.is_relative_to(ROOT) else str(args.output),
        "effects_csv": str(args.effects_output.relative_to(ROOT)) if args.effects_output.is_relative_to(ROOT) else str(args.effects_output),
        "time_series_rows": len(rows),
        "effect_rows": len(effects),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def top_effects(effects, limit=8):
    candidates = [row for row in effects if row["treatment"] != "baseline"]
    candidates.sort(key=lambda row: row["biological_sensitivity_score"], reverse=True)
    return candidates[:limit]


def fmt_effect(value):
    if value is None:
        return "n/a"
    try:
        if math.isnan(float(value)):
            return "n/a"
    except (TypeError, ValueError):
        return str(value)
    return f"{float(value):.3f}"


def write_report(path, effects, treatments, args):
    treatment_map = {item["name"]: item for item in treatments}
    lines = [
        "# Actual Biology Sensitivity Suite v1",
        "",
        "This report screens whether core biological outputs are robust to parameter changes under the same simulator rules.",
        "",
        "## Run Configuration",
        "",
        f"- Seeds: `{args.seeds}`",
        f"- Scenarios: `{args.scenarios}`",
        f"- Days per replicate: `{args.days}`",
        f"- Sample interval: `{args.sample_days}` days",
        "",
        "## Treatments",
        "",
        "| Treatment | Overrides | Purpose |",
        "|---|---|---|",
    ]
    for treatment in treatments:
        overrides = ", ".join(treatment["set"]) if treatment["set"] else "none"
        lines.append(f"| `{treatment['name']}` | `{overrides}` | {treatment['description']} |")
    lines.extend([
        "",
        "## Largest Relative Effects",
        "",
        "| Treatment | Scenario | Score | Food trips effect | Hydration effect | Brood stress effect | Peak food pheromone effect |",
        "|---|---|---:|---:|---:|---:|---:|",
    ])
    for row in top_effects(effects):
        lines.append(
            f"| {row['treatment']} | {row['scenario']} | {row['biological_sensitivity_score']:.3f} | "
            f"{fmt_effect(row['food_trips_mean_relative_effect'])} | "
            f"{fmt_effect(row['avg_hydration_mean_relative_effect'])} | "
            f"{fmt_effect(row['brood_stress_mean_relative_effect'])} | "
            f"{fmt_effect(row['food_pheromone_peak_mean_relative_effect'])} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- Large effects identify parameters that need literature calibration first.",
        "- Small effects suggest the qualitative scenario is robust under this local parameter range.",
        "- This is a sensitivity screen, not an optimizer and not proof of biological correctness.",
        "",
        "Treatment notes:",
    ])
    for name in sorted({row["treatment"] for row in effects if row["treatment"] != "baseline"}):
        lines.append(f"- `{name}`: {treatment_map[name]['description']}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_treatment(treatment, args):
    run_args = SimpleNamespace(
        seeds=args.seeds,
        scenarios=args.scenarios,
        days=args.days,
        sample_days=args.sample_days,
        dt=args.dt,
        treatment=treatment["name"],
        set=treatment["set"],
        output=args.output,
    )
    return biology.run_suite(run_args)


def main():
    parser = argparse.ArgumentParser(description="Run parameter sensitivity screen for actual biological scenarios.")
    parser.add_argument("--seeds", default="101-103")
    parser.add_argument("--scenarios", default="stable_mature,resource_stress,heat_dry_stress")
    parser.add_argument("--days", type=float, default=4)
    parser.add_argument("--sample-days", type=float, default=0.25)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "actual_biology_sensitivity.csv")
    parser.add_argument("--effects-output", type=Path, default=ROOT / "outputs" / "actual_biology_sensitivity_effects.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "actual_biology_sensitivity.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "actual_biology_sensitivity.md")
    args = parser.parse_args()

    treatments = DEFAULT_TREATMENTS
    if args.quick:
        args.seeds = "101"
        args.days = min(args.days, 1.5)
        treatments = DEFAULT_TREATMENTS[:3]

    rows = []
    for treatment in treatments:
        rows.extend(run_treatment(treatment, args))
    summary = biology.summarize(rows)
    effects = score_effects(summary)
    write_csv(args.output, rows)
    write_csv(args.effects_output, effects)
    write_json(args.json_output, rows, effects, treatments, args)
    write_report(args.report_output, effects, treatments, args)
    print(f"wrote {len(rows)} rows to {args.output}")
    print(f"wrote {len(effects)} effect rows to {args.effects_output}")
    print(f"wrote metadata to {args.json_output}")
    print(f"wrote report to {args.report_output}")


if __name__ == "__main__":
    main()
