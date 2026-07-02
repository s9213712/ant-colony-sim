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


def normalized(values):
    first = values[0] if values else 0
    return [value / first if first else 0 for value in values]


def rmse(left, right):
    if len(left) != len(right):
        raise ValueError("rmse vectors must have the same length")
    return (sum((a - b) ** 2 for a, b in zip(left, right)) / len(left)) ** 0.5 if left else 0


def validate(curve_rows, model_metrics):
    rows = sorted(curve_rows, key=lambda row: float(row["x_value"]))
    low = rows[0]
    medium = rows[1] if len(rows) > 2 else None
    high = rows[-1]
    target_speeds = [float(row["y_value"]) for row in rows]
    target_low_speed = target_speeds[0]
    target_high_speed = target_speeds[-1]
    target_low_sd = float(low["variance_value"]) if low.get("variance_value") else None
    target_high_sd = float(high["variance_value"]) if high.get("variance_value") else None
    target_low_n = int(low["n"]) if low.get("n") else None
    target_high_n = int(high["n"]) if high.get("n") else None
    target_retention = target_high_speed / target_low_speed if target_low_speed else 0
    model_speeds = [
        float(model_metrics["low_segment_speed"]),
        float(model_metrics.get("medium_segment_speed", model_metrics["high_segment_speed"])),
        float(model_metrics["high_segment_speed"]),
    ]
    model_low_speed = model_speeds[0]
    model_high_speed = model_speeds[-1]
    model_retention = model_high_speed / model_low_speed if model_low_speed else 0
    model_low_flow = float(model_metrics["low_segment_flow"])
    model_medium_flow = float(model_metrics.get("medium_segment_flow", model_metrics["high_segment_flow"]))
    model_high_flow = float(model_metrics["high_segment_flow"])
    target_velocity_drop = 1 - target_retention
    model_velocity_drop = 1 - model_retention
    target_normalized_speed = normalized(target_speeds)
    model_normalized_speed = normalized(model_speeds)
    normalized_speed_rmse = rmse(target_normalized_speed, model_normalized_speed)
    curve = []
    model_density_keys = ["low_segment_density", "medium_segment_density", "high_segment_density"]
    model_flow_keys = ["low_segment_flow", "medium_segment_flow", "high_segment_flow"]
    for index, row in enumerate(rows):
        curve.append({
            "density_bin_midpoint": float(row["x_value"]),
            "target_speed": target_speeds[index],
            "target_normalized_speed": target_normalized_speed[index],
            "target_sd": float(row["variance_value"]) if row.get("variance_value") else None,
            "target_n": int(row["n"]) if row.get("n") else None,
            "model_segment_density": float(model_metrics.get(model_density_keys[index], 0)),
            "model_segment_speed": model_speeds[index],
            "model_normalized_speed": model_normalized_speed[index],
            "model_segment_flow": float(model_metrics.get(model_flow_keys[index], 0)),
        })
    checks = {
        "target_no_jam_retention_at_least_0_70": target_retention >= 0.70,
        "model_high_density_speed_positive": model_high_speed > 0,
        "model_high_density_flow_exceeds_low_density": model_high_flow > model_low_flow,
        "model_velocity_retention_within_holdout_margin": model_retention >= max(0.45, target_retention - 0.25),
        "model_three_point_curve_rmse_within_0_25": normalized_speed_rmse <= 0.25,
    }
    status = "pass" if all(checks.values()) else "needs_work"
    return {
        "status": status,
        "checks": checks,
        "target": {
            "low_density": float(low["x_value"]),
            "medium_density": float(medium["x_value"]) if medium else None,
            "high_density": float(high["x_value"]),
            "low_speed_bl_per_sec": target_low_speed,
            "medium_speed_bl_per_sec": float(medium["y_value"]) if medium else None,
            "high_speed_bl_per_sec": target_high_speed,
            "low_speed_sd": target_low_sd,
            "medium_speed_sd": float(medium["variance_value"]) if medium and medium.get("variance_value") else None,
            "high_speed_sd": target_high_sd,
            "low_n": target_low_n,
            "medium_n": int(medium["n"]) if medium and medium.get("n") else None,
            "high_n": target_high_n,
            "velocity_retention": target_retention,
            "velocity_drop": target_velocity_drop,
            "formal_ci_available": bool(target_low_sd and target_high_sd and target_low_n and target_high_n),
            "normalized_speed_curve": target_normalized_speed,
        },
        "model": {
            "low_segment_density": float(model_metrics["low_segment_density"]),
            "medium_segment_density": float(model_metrics.get("medium_segment_density", 0)),
            "high_segment_density": float(model_metrics["high_segment_density"]),
            "low_segment_speed": model_low_speed,
            "medium_segment_speed": model_speeds[1],
            "high_segment_speed": model_high_speed,
            "velocity_retention": model_retention,
            "velocity_drop": model_velocity_drop,
            "low_segment_flow": model_low_flow,
            "medium_segment_flow": model_medium_flow,
            "high_segment_flow": model_high_flow,
            "normalized_speed_curve": model_normalized_speed,
            "normalized_speed_rmse": normalized_speed_rmse,
            "curve": curve,
        },
        "interpretation": (
            "The independent John 2009 holdout supports the model's qualitative no-jam traffic behavior: speed remains positive and high-density flow does not collapse."
            if status == "pass"
            else "The model fails the John 2009 no-jam holdout; inspect crowding/contact rules before claiming Level 4."
        ),
        "uncertainty_note": (
            "Figure 4 reports Gaussian-fit SD values, but the density-bin sample sizes are not present in the committed target rows; formal confidence intervals are therefore not computed."
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
        "model_normalized_speed_rmse": result["model"]["normalized_speed_rmse"],
        "target_low_speed_sd": result["target"]["low_speed_sd"],
        "target_medium_speed_sd": result["target"]["medium_speed_sd"],
        "target_high_speed_sd": result["target"]["high_speed_sd"],
        "formal_target_ci_available": result["target"]["formal_ci_available"],
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
        f"- normalized speed curve RMSE: `{result['model']['normalized_speed_rmse']:.3f}`",
        f"- model low flow: `{result['model']['low_segment_flow']:.4f}`",
        f"- model medium flow: `{result['model']['medium_segment_flow']:.4f}`",
        f"- model high flow: `{result['model']['high_segment_flow']:.4f}`",
        f"- target low-density speed SD: `{result['target']['low_speed_sd']}`",
        f"- target medium-density speed SD: `{result['target']['medium_speed_sd']}`",
        f"- target high-density speed SD: `{result['target']['high_speed_sd']}`",
        f"- formal target CI available: `{result['target']['formal_ci_available']}`",
        "",
        "## Curve",
        "",
        "| Target density | Target speed | Target normalized | Model density | Model speed | Model normalized | Model flow |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["model"]["curve"]:
        lines.append(
            f"| {row['density_bin_midpoint']} | {row['target_speed']} | {row['target_normalized_speed']:.3f} | "
            f"{row['model_segment_density']:.5f} | {row['model_segment_speed']:.4f} | "
            f"{row['model_normalized_speed']:.3f} | {row['model_segment_flow']:.4f} |"
        )
    lines.extend([
        "",
        "## Checks",
        "",
    ])
    for key, value in result["checks"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend([
        "",
        "## Interpretation",
        "",
        result["interpretation"],
        "",
        result["uncertainty_note"],
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
