#!/usr/bin/env python3
"""Validate crowded-traffic encounter redirect probability against Dussutour 2004."""

import argparse
import csv
import json
import math
import random
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_target(path, target_id):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("target_id") == target_id]
    if len(rows) != 1:
        raise RuntimeError(f"expected exactly one {target_id} row in {path}, found {len(rows)}")
    row = rows[0]
    value = float(row["y_value"])
    half_width = float(row["variance_value"]) if row.get("variance_type") == "ci95_half_width" else None
    return {
        "source_id": row["source_id"],
        "target_id": row["target_id"],
        "species": row["species"],
        "figure_or_table": row["figure_or_table"],
        "value": value,
        "ci95_low": value - half_width if half_width is not None else None,
        "ci95_high": value + half_width if half_width is not None else None,
        "ci95_half_width": half_width,
        "n": int(row["n"]) if row.get("n") else None,
        "notes": row.get("notes", ""),
    }


def read_model_values(path, condition):
    data = json.loads(path.read_text(encoding="utf-8"))
    values = []
    rows = []
    for row in data.get("raw_rows", []):
        if row.get("condition") != condition:
            continue
        encounters = float(row.get("traffic_redirect_encounters") or 0)
        value = float(row.get("traffic_redirect_per_encounter") or 0)
        rows.append({
            "seed": row.get("seed"),
            "condition": condition,
            "traffic_redirect_encounters": encounters,
            "traffic_encounter_redirects": float(row.get("traffic_encounter_redirects") or 0),
            "traffic_redirect_per_encounter": value,
        })
        if encounters > 0:
            values.append(value)
    if not values:
        raise RuntimeError(f"no model redirect-per-encounter values found for {condition}")
    return values, rows


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


def validate(target, values, rows, bootstrap_samples, bootstrap_seed):
    model_mean = mean(values)
    model_sd = sample_sd(values)
    model_ci = bootstrap_ci(values, bootstrap_samples, bootstrap_seed)
    target_ci = [target["ci95_low"], target["ci95_high"]]
    ci_overlap = not (model_ci[1] < target_ci[0] or model_ci[0] > target_ci[1])
    absolute_error = abs(model_mean - target["value"])
    checks = {
        "model_has_encounters": sum(row["traffic_redirect_encounters"] for row in rows) > 0,
        "model_ci_overlaps_target_ci": ci_overlap,
        "model_mean_within_0_12_absolute_error": absolute_error <= 0.12,
    }
    status = "pass" if checks["model_has_encounters"] and (checks["model_ci_overlaps_target_ci"] or checks["model_mean_within_0_12_absolute_error"]) else "needs_work"
    return {
        "status": status,
        "checks": checks,
        "target": target,
        "model": {
            "condition": rows[0]["condition"],
            "replicates": len(values),
            "mean_redirect_per_encounter": model_mean,
            "sd_redirect_per_encounter": model_sd,
            "ci95_redirect_per_encounter": model_ci,
            "absolute_error": absolute_error,
            "total_encounters": sum(row["traffic_redirect_encounters"] for row in rows),
            "total_encounter_redirects": sum(row["traffic_encounter_redirects"] for row in rows),
        },
        "replicate_rows": rows,
        "interpretation": (
            "The general frontal-encounter redirect rule is quantitatively aligned with the Dussutour 2004 pushing probability target."
            if status == "pass"
            else "The model does not yet reproduce the Dussutour 2004 pushing probability; keep this as a Level 5 calibration gap."
        ),
    }


def write_csv(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "status": result["status"],
        "target_probability": result["target"]["value"],
        "target_ci95_low": result["target"]["ci95_low"],
        "target_ci95_high": result["target"]["ci95_high"],
        "model_mean_redirect_per_encounter": result["model"]["mean_redirect_per_encounter"],
        "model_ci95_low": result["model"]["ci95_redirect_per_encounter"][0],
        "model_ci95_high": result["model"]["ci95_redirect_per_encounter"][1],
        "absolute_error": result["model"]["absolute_error"],
        "replicates": result["model"]["replicates"],
        "total_encounters": result["model"]["total_encounters"],
        "total_encounter_redirects": result["model"]["total_encounter_redirects"],
    }
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)


def write_report(path, target_csv, model_source, result):
    lines = [
        "# Pushing Redirect Probability Validation",
        "",
        "This report validates the general crowded-traffic frontal-encounter redirect rule against Dussutour et al. 2004.",
        "",
        f"- target CSV: `{target_csv}`",
        f"- model source: `{model_source}`",
        "- source: Dussutour et al. 2004, Optimal traffic organisation in ants under crowded conditions, https://arxiv.org/abs/cond-mat/0403142",
        "",
        "## Result",
        "",
        f"- status: `{result['status']}`",
        f"- target J: `{result['target']['value']}`",
        f"- target 95% CI: `[{result['target']['ci95_low']}, {result['target']['ci95_high']}]`",
        f"- model mean: `{result['model']['mean_redirect_per_encounter']:.4f}`",
        f"- model 95% CI: `{result['model']['ci95_redirect_per_encounter']}`",
        f"- total model encounters: `{result['model']['total_encounters']}`",
        f"- total model encounter redirects: `{result['model']['total_encounter_redirects']}`",
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
        "Caveat: the model uses a spatial traffic-grid proxy for frontal encounters. This validates a general body-contact redirect mechanism, not the full bridge-width transition curve.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Validate Dussutour 2004 pushing/redirect probability.")
    parser.add_argument("--target-csv", type=Path, default=ROOT / "targets" / "digitized_curves" / "dussutour_2004_pushing_redirect_probability.csv")
    parser.add_argument("--target-id", default="traffic_pushing_redirect_probability")
    parser.add_argument("--model-summary", type=Path, default=ROOT / "outputs" / "paper_conditions_v5.json")
    parser.add_argument("--condition", default="crowding_high_density_bridge")
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    parser.add_argument("--bootstrap-seed", type=int, default=77371)
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "pushing_redirect_validation.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "pushing_redirect_validation.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "pushing_redirect_validation.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    args = parser.parse_args()

    target = read_target(args.target_csv, args.target_id)
    values, rows = read_model_values(args.model_summary, args.condition)
    result = validate(target, values, rows, args.bootstrap_samples, args.bootstrap_seed)
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
        f"pushing redirect {result['status']}: "
        f"target={result['target']['value']:.3f} "
        f"model={result['model']['mean_redirect_per_encounter']:.3f}"
    )
    if args.fail_on_issues and result["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
