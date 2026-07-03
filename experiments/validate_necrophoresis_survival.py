#!/usr/bin/env python3
"""Validate social-immunity survival effects against Diez et al. 2014."""

import argparse
import csv
import json
import math
import random
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_target_rows(path, target_id):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("target_id") == target_id]
    if len(rows) != 2:
        raise RuntimeError(f"expected two {target_id} rows in {path}, found {len(rows)}")
    by_label = {row["x_unit"]: row for row in rows}
    restricted = by_label["restricted removal LR"]
    free = by_label["free removal FR"]
    return {
        "source_id": free["source_id"],
        "target_id": target_id,
        "species": free["species"],
        "free_mean": float(free["y_value"]),
        "free_sd": float(free["variance_value"]),
        "free_n": int(free["n"]),
        "restricted_mean": float(restricted["y_value"]),
        "restricted_sd": float(restricted["variance_value"]),
        "restricted_n": int(restricted["n"]),
        "source_url": free["source_url"],
        "figure_or_table": free["figure_or_table"],
    }


def read_model_pairs(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    by_condition = {}
    for row in data.get("raw_rows", []):
        condition = row.get("condition")
        if condition in {"necrophoresis_survival_free_removal", "necrophoresis_survival_restricted_removal"}:
            by_condition.setdefault(condition, {})[str(row.get("seed"))] = row
    free = by_condition.get("necrophoresis_survival_free_removal", {})
    restricted = by_condition.get("necrophoresis_survival_restricted_removal", {})
    pairs = []
    for seed in sorted(set(free) & set(restricted), key=lambda item: int(float(item))):
        free_row = free[seed]
        restricted_row = restricted[seed]
        pairs.append({
            "seed": seed,
            "free_survival": float(free_row["survival_fraction"]),
            "restricted_survival": float(restricted_row["survival_fraction"]),
            "survival_delta_free_minus_restricted": float(free_row["survival_fraction"]) - float(restricted_row["survival_fraction"]),
            "free_avg_health": float(free_row["avg_health"]),
            "restricted_avg_health": float(restricted_row["avg_health"]),
            "health_delta_free_minus_restricted": float(free_row["avg_health"]) - float(restricted_row["avg_health"]),
            "free_nest_corpse_pressure": float(free_row["nest_corpse_pressure"]),
            "restricted_nest_corpse_pressure": float(restricted_row["nest_corpse_pressure"]),
            "pressure_delta_restricted_minus_free": float(restricted_row["nest_corpse_pressure"]) - float(free_row["nest_corpse_pressure"]),
        })
    if not pairs:
        raise RuntimeError("no paired necrophoresis survival model rows found")
    return pairs


def mean(values):
    return sum(values) / len(values) if values else 0


def sample_sd(values):
    if len(values) < 2:
        return None
    avg = mean(values)
    return math.sqrt(sum((value - avg) ** 2 for value in values) / (len(values) - 1))


def percentile(values, p):
    ordered = sorted(values)
    index = (len(ordered) - 1) * p
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[int(index)]
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def bootstrap_ci(values, samples, seed):
    if len(values) < 2:
        return [values[0], values[0]]
    rng = random.Random(seed)
    boot = []
    for _ in range(samples):
        draw = [values[rng.randrange(len(values))] for _ in values]
        boot.append(mean(draw))
    return [percentile(boot, 0.025), percentile(boot, 0.975)]


def target_delta_ci(target):
    delta = target["free_mean"] - target["restricted_mean"]
    se = math.sqrt(target["free_sd"] ** 2 / target["free_n"] + target["restricted_sd"] ** 2 / target["restricted_n"])
    return delta, [delta - 1.96 * se, delta + 1.96 * se]


def validate(target, pairs, bootstrap_samples, bootstrap_seed):
    target_delta, target_ci = target_delta_ci(target)
    survival_deltas = [row["survival_delta_free_minus_restricted"] for row in pairs]
    health_deltas = [row["health_delta_free_minus_restricted"] for row in pairs]
    pressure_deltas = [row["pressure_delta_restricted_minus_free"] for row in pairs]
    model_survival_delta = mean(survival_deltas)
    model_survival_ci = bootstrap_ci(survival_deltas, bootstrap_samples, bootstrap_seed)
    model_health_delta = mean(health_deltas)
    model_health_ci = bootstrap_ci(health_deltas, bootstrap_samples, bootstrap_seed + 17)
    model_pressure_delta = mean(pressure_deltas)
    survival_direction = model_survival_delta > 0
    health_surrogate_direction = model_health_delta > 0 and model_pressure_delta > 1
    target_direction = target_delta > 0 and target_ci[1] > 0
    survival_ci_overlap = not (model_survival_ci[1] < target_ci[0] or model_survival_ci[0] > target_ci[1])
    checks = {
        "target_free_survival_exceeds_restricted": target_direction,
        "model_free_survival_exceeds_restricted": survival_direction,
        "model_free_health_exceeds_restricted": health_surrogate_direction,
        "model_survival_ci_overlaps_target_ci": survival_ci_overlap,
    }
    if checks["target_free_survival_exceeds_restricted"] and checks["model_free_survival_exceeds_restricted"]:
        status = "pass"
        interpretation = "The generic nest-corpse social-immunity pressure reproduces the direction of the Diez et al. worker-survival advantage."
    elif checks["target_free_survival_exceeds_restricted"] and checks["model_free_health_exceeds_restricted"]:
        status = "partial"
        interpretation = "The model reproduces a health-cost precursor under restricted corpse removal, but not yet a full worker-survival endpoint."
    else:
        status = "needs_work"
        interpretation = "The model does not yet reproduce the Diez et al. worker-survival advantage."
    return {
        "status": status,
        "checks": checks,
        "target": {
            **target,
            "survival_delta_free_minus_restricted": target_delta,
            "survival_delta_ci95": target_ci,
        },
        "model": {
            "replicates": len(pairs),
            "survival_delta_free_minus_restricted": model_survival_delta,
            "survival_delta_ci95": model_survival_ci,
            "health_delta_free_minus_restricted": model_health_delta,
            "health_delta_ci95": model_health_ci,
            "pressure_delta_restricted_minus_free": model_pressure_delta,
        },
        "replicate_rows": pairs,
        "interpretation": interpretation,
    }


def write_csv(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "status": result["status"],
        "target_delta": result["target"]["survival_delta_free_minus_restricted"],
        "target_ci95_low": result["target"]["survival_delta_ci95"][0],
        "target_ci95_high": result["target"]["survival_delta_ci95"][1],
        "model_survival_delta": result["model"]["survival_delta_free_minus_restricted"],
        "model_survival_ci95_low": result["model"]["survival_delta_ci95"][0],
        "model_survival_ci95_high": result["model"]["survival_delta_ci95"][1],
        "model_health_delta": result["model"]["health_delta_free_minus_restricted"],
        "model_health_ci95_low": result["model"]["health_delta_ci95"][0],
        "model_health_ci95_high": result["model"]["health_delta_ci95"][1],
        "model_pressure_delta": result["model"]["pressure_delta_restricted_minus_free"],
        "replicates": result["model"]["replicates"],
    }
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)


def write_report(path, target_csv, model_summary, result):
    lines = [
        "# Necrophoresis Survival Holdout Validation",
        "",
        "This report validates the generic nest-corpse social-immunity pressure against Diez, Lejeune & Detrain 2014.",
        "",
        f"- target CSV: `{target_csv}`",
        f"- model source: `{model_summary}`",
        "- source: Diez et al. 2014, Keep the nest clean: survival advantages of corpse removal in ants, https://pmc.ncbi.nlm.nih.gov/articles/PMC4126623/",
        "",
        "## Result",
        "",
        f"- status: `{result['status']}`",
        f"- target survival delta free-restricted: `{result['target']['survival_delta_free_minus_restricted']}`",
        f"- target 95% CI: `{result['target']['survival_delta_ci95']}`",
        f"- model survival delta free-restricted: `{result['model']['survival_delta_free_minus_restricted']}`",
        f"- model survival 95% CI: `{result['model']['survival_delta_ci95']}`",
        f"- model health delta free-restricted: `{result['model']['health_delta_free_minus_restricted']}`",
        f"- model health 95% CI: `{result['model']['health_delta_ci95']}`",
        f"- model pressure delta restricted-free: `{result['model']['pressure_delta_restricted_minus_free']}`",
        "",
        "## Checks",
        "",
    ]
    for key, value in result["checks"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend([
        "",
        "## Interpretation",
        "",
        result["interpretation"],
        "",
        "Caveat: the target endpoint is a 50-day Myrmica rubra experiment, while the current model uses internal simulated days. Raw supplementary time-series fitting is still required before this becomes a strict species-level survival predictor.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Validate Diez 2014 necrophoresis survival endpoint.")
    parser.add_argument("--target-csv", type=Path, default=ROOT / "targets" / "digitized_curves" / "diez_2014_necrophoresis_worker_survival.csv")
    parser.add_argument("--target-id", default="necrophoresis_worker_survival_endpoint")
    parser.add_argument("--model-summary", type=Path, default=ROOT / "outputs" / "paper_conditions_v5.json")
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    parser.add_argument("--bootstrap-seed", type=int, default=88231)
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "necrophoresis_survival_validation.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "necrophoresis_survival_validation.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "necrophoresis_survival_validation.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    args = parser.parse_args()

    target = read_target_rows(args.target_csv, args.target_id)
    pairs = read_model_pairs(args.model_summary)
    result = validate(target, pairs, args.bootstrap_samples, args.bootstrap_seed)
    write_csv(args.csv_output, result)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "target_csv": str(args.target_csv),
                "target_id": args.target_id,
                "model_summary": str(args.model_summary),
                "result": result,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(args.report_output, args.target_csv, args.model_summary, result)
    print(
        f"necrophoresis survival {result['status']}: "
        f"target_delta={result['target']['survival_delta_free_minus_restricted']:.3f} "
        f"model_survival_delta={result['model']['survival_delta_free_minus_restricted']:.3f} "
        f"model_health_delta={result['model']['health_delta_free_minus_restricted']:.3f}"
    )
    if args.fail_on_issues and result["status"] == "needs_work":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
