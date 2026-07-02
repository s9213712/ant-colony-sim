#!/usr/bin/env python3
"""Validate the no-jam traffic holdout curve without fitting model parameters."""

import argparse
import csv
import json
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_curve(path, target_id):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = [
            row for row in csv.DictReader(handle)
            if row.get("target_id") == target_id
        ]
    if len(rows) < 2:
        raise RuntimeError(f"need at least 2 target rows for {target_id}, found {len(rows)}")
    return rows


def read_paper_condition_summary(path, paper_id):
    data = json.loads(path.read_text(encoding="utf-8"))
    for row in data.get("summaries", []):
        if row.get("paper_id") == paper_id:
            return json.loads(row.get("observed", "{}"))
    raise RuntimeError(f"paper condition summary not found: {paper_id}")


def validate(curve_rows, model_metrics):
    rows = sorted(curve_rows, key=lambda row: float(row["x_value"]))
    low = rows[0]
    high = rows[-1]
    target_low_speed = float(low["y_value"])
    target_high_speed = float(high["y_value"])
    target_retention = target_high_speed / target_low_speed if target_low_speed else 0
    model_low_speed = float(model_metrics["low_segment_speed"])
    model_high_speed = float(model_metrics["high_segment_speed"])
    model_retention = model_high_speed / model_low_speed if model_low_speed else 0
    model_low_flow = float(model_metrics["low_segment_flow"])
    model_high_flow = float(model_metrics["high_segment_flow"])
    target_velocity_drop = 1 - target_retention
    model_velocity_drop = 1 - model_retention
    checks = {
        "target_no_jam_retention_at_least_0_70": target_retention >= 0.70,
        "model_high_density_speed_positive": model_high_speed > 0,
        "model_high_density_flow_exceeds_low_density": model_high_flow > model_low_flow,
        "model_velocity_retention_within_holdout_margin": model_retention >= max(0.45, target_retention - 0.25),
    }
    status = "pass" if all(checks.values()) else "needs_work"
    return {
        "status": status,
        "checks": checks,
        "target": {
            "low_density": float(low["x_value"]),
            "high_density": float(high["x_value"]),
            "low_speed_bl_per_sec": target_low_speed,
            "high_speed_bl_per_sec": target_high_speed,
            "velocity_retention": target_retention,
            "velocity_drop": target_velocity_drop,
        },
        "model": {
            "low_segment_density": float(model_metrics["low_segment_density"]),
            "high_segment_density": float(model_metrics["high_segment_density"]),
            "low_segment_speed": model_low_speed,
            "high_segment_speed": model_high_speed,
            "velocity_retention": model_retention,
            "velocity_drop": model_velocity_drop,
            "low_segment_flow": model_low_flow,
            "high_segment_flow": model_high_flow,
        },
        "interpretation": (
            "The independent John 2009 holdout supports the model's qualitative no-jam traffic behavior: speed remains positive and high-density flow does not collapse."
            if status == "pass"
            else "The model fails the John 2009 no-jam holdout; inspect crowding/contact rules before claiming Level 4."
        ),
    }


def write_csv(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "status": result["status"],
        "target_velocity_retention": result["target"]["velocity_retention"],
        "model_velocity_retention": result["model"]["velocity_retention"],
        "target_velocity_drop": result["target"]["velocity_drop"],
        "model_velocity_drop": result["model"]["velocity_drop"],
        "model_low_segment_flow": result["model"]["low_segment_flow"],
        "model_high_segment_flow": result["model"]["high_segment_flow"],
    }
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)


def write_report(path, target_csv, model_source, result):
    lines = [
        "# Traffic Velocity-Density Holdout Validation",
        "",
        "This report validates the traffic no-jam behavior against John et al. 2009 without fitting model parameters to that paper.",
        "",
        f"- Target CSV: `{target_csv}`",
        f"- Model summary source: `{model_source}`",
        "- Source: John et al. 2009, Trafficlike collective movement of ants on trails: absence of a jammed phase, https://arxiv.org/abs/0903.2717",
        "",
        "## Result",
        "",
        f"- status: `{result['status']}`",
        f"- target velocity retention high/low: `{result['target']['velocity_retention']:.3f}`",
        f"- model velocity retention high/low: `{result['model']['velocity_retention']:.3f}`",
        f"- model low flow: `{result['model']['low_segment_flow']:.4f}`",
        f"- model high flow: `{result['model']['high_segment_flow']:.4f}`",
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
        "Caveat: this is a normalized no-jam holdout, not a physical unit match. The target uses body-length/second velocities from a natural Leptogenys processionalis trail, while the simulator uses internal segment-speed units.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Validate no-jam traffic holdout curve.")
    parser.add_argument("--target-csv", type=Path, default=ROOT / "targets" / "digitized_curves" / "john_2009_traffic_velocity_density_holdout.csv")
    parser.add_argument("--target-id", default="traffic_velocity_density_holdout")
    parser.add_argument("--model-summary", type=Path, default=ROOT / "outputs" / "paper_conditions_v5.json")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "traffic_holdout_validation.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "traffic_holdout_validation.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "traffic_holdout_validation.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    args = parser.parse_args()

    curve_rows = read_curve(args.target_csv, args.target_id)
    model_metrics = read_paper_condition_summary(args.model_summary, "john_2009")
    result = validate(curve_rows, model_metrics)
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
        f"traffic holdout {result['status']}: "
        f"target_retention={result['target']['velocity_retention']:.3f} "
        f"model_retention={result['model']['velocity_retention']:.3f}"
    )
    if args.fail_on_issues and result["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
