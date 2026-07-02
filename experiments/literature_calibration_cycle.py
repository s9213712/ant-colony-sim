#!/usr/bin/env python3
"""Evaluate sensitivity results against literature-guided calibration constraints."""

import argparse
import csv
import json
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def to_float(value):
    if value in (None, ""):
        return None
    try:
        return float(value)
    except ValueError:
        return None


def find_effect_row(rows, treatment, scenario):
    for row in rows:
        if row.get("treatment") == treatment and row.get("scenario") == scenario:
            return row
    return None


def evaluate_constraint(constraint, rows):
    row = find_effect_row(rows, constraint["treatment"], constraint["scenario"])
    result = {
        "constraint_id": constraint["id"],
        "priority": constraint.get("priority", "P2"),
        "treatment": constraint["treatment"],
        "scenario": constraint["scenario"],
        "metric": constraint["metric"],
        "min": constraint.get("min"),
        "max": constraint.get("max"),
        "meaning": constraint.get("meaning", ""),
    }
    if not row:
        result.update({
            "status": "missing",
            "observed": None,
            "gap": "Sensitivity result row is missing for this treatment/scenario.",
            "recommended_action": "Run actual_biology_sensitivity.py with the required treatment and scenario.",
        })
        return result
    observed = to_float(row.get(constraint["metric"]))
    result["observed"] = observed
    if observed is None:
        result.update({
            "status": "missing",
            "gap": "Metric value is missing or undefined.",
            "recommended_action": "Increase replicate length/seeds or choose a metric that is defined when baseline is non-zero.",
        })
        return result
    failures = []
    if "min" in constraint and observed < float(constraint["min"]):
        failures.append(f"observed {observed:.6f} < min {float(constraint['min']):.6f}")
    if "max" in constraint and observed > float(constraint["max"]):
        failures.append(f"observed {observed:.6f} > max {float(constraint['max']):.6f}")
    if failures:
        result.update({
            "status": "fail",
            "gap": "; ".join(failures),
            "recommended_action": recommend_action(constraint),
        })
    else:
        result.update({
            "status": "pass",
            "gap": "",
            "recommended_action": "",
        })
    return result


def recommend_action(constraint):
    metric = constraint["metric"]
    treatment = constraint["treatment"]
    if treatment == "persistent_pheromone":
        return (
            "Narrow the plausible persistence/sense-threshold range, then fit evaporationRate "
            "and senseThreshold against digitized trail-decay and recruitment data."
        )
    if "diffusion" in treatment or "pheromone" in metric:
        return "Calibrate diffusion/evaporation jointly; report model-unit trail half-life before biological claims."
    if "brood" in treatment or "brood" in metric:
        return "Run a brood-demand sweep and compare task allocation plus brood survival against species-specific data."
    return "Add a parameter sweep or digitized paper target for this metric."


def write_csv(path, rows):
    if not rows:
        raise RuntimeError(f"no rows for {path}")
    headers = []
    for row in rows:
        for key in row:
            if key not in headers:
                headers.append(key)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path, target, rows, args):
    payload = {
        "suite": "literature_calibration_cycle_v1",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "target_id": target["id"],
        "target_status": target.get("status"),
        "claim_level": "literature_guided_constraint_screen_not_digitized_curve_fit",
        "sources": target.get("sources", []),
        "input_effects": str(args.effects.relative_to(ROOT)) if args.effects.is_relative_to(ROOT) else str(args.effects),
        "summary": summarize(rows),
        "results": rows,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def summarize(rows):
    summary = {"total": len(rows), "pass": 0, "fail": 0, "missing": 0, "by_priority": {}}
    for row in rows:
        status = row["status"]
        summary[status] = summary.get(status, 0) + 1
        priority = row.get("priority", "P2")
        summary["by_priority"].setdefault(priority, {"pass": 0, "fail": 0, "missing": 0})
        summary["by_priority"][priority][status] = summary["by_priority"][priority].get(status, 0) + 1
    return summary


def write_report(path, target, rows, args):
    summary = summarize(rows)
    lines = [
        "# Literature Calibration Cycle v1",
        "",
        "This report evaluates the latest biological sensitivity output against literature-guided constraints.",
        "",
        "## Claim Level",
        "",
        "This is a qualitative constraint screen. It is not yet a digitized paper-curve fit or a physical pheromone half-life calibration.",
        "",
        "## Sources Used",
        "",
        "| Source | Used for | URL |",
        "|---|---|---|",
    ]
    for source in target.get("sources", []):
        lines.append(f"| {source['id']} | {source['used_for']} | {source['url']} |")
    lines.extend([
        "",
        "## Summary",
        "",
        f"- total constraints: `{summary['total']}`",
        f"- pass: `{summary.get('pass', 0)}`",
        f"- fail: `{summary.get('fail', 0)}`",
        f"- missing: `{summary.get('missing', 0)}`",
        "",
        "## Results",
        "",
        "| Status | Priority | Constraint | Treatment | Scenario | Metric | Observed | Range | Next action |",
        "|---|---|---|---|---|---|---:|---|---|",
    ])
    for row in rows:
        observed = "n/a" if row["observed"] is None else f"{row['observed']:.6f}"
        lower = "" if row.get("min") is None else str(row["min"])
        upper = "" if row.get("max") is None else str(row["max"])
        allowed = f"[{lower}, {upper}]"
        lines.append(
            f"| `{row['status']}` | `{row['priority']}` | `{row['constraint_id']}` | "
            f"`{row['treatment']}` | `{row['scenario']}` | `{row['metric']}` | "
            f"{observed} | `{allowed}` | {row['recommended_action']} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- Any `fail` row remains an active calibration issue.",
        "- When this report reaches zero `fail` and zero `missing`, the next loop should replace qualitative bands with digitized curves.",
        "- Current constraints deliberately target pheromone persistence/sensing/diffusion because the sensitivity screen showed these parameters move foraging and brood-stress outputs.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Evaluate literature-guided calibration constraints.")
    parser.add_argument("--targets", type=Path, default=ROOT / "targets" / "literature_pheromone_constraints.json")
    parser.add_argument("--effects", type=Path, default=ROOT / "outputs" / "actual_biology_sensitivity_effects.csv")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "literature_calibration_cycle.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "literature_calibration_cycle.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "literature_calibration_cycle.md")
    parser.add_argument("--fail-on-issues", action="store_true", help="Exit non-zero when any constraint fails or is missing.")
    args = parser.parse_args()

    target = read_json(args.targets)
    effects = read_csv(args.effects)
    rows = [evaluate_constraint(constraint, effects) for constraint in target["constraints"]]
    write_csv(args.csv_output, rows)
    write_json(args.json_output, target, rows, args)
    write_report(args.report_output, target, rows, args)
    summary = summarize(rows)
    print(f"wrote {len(rows)} calibration rows to {args.csv_output}")
    print(f"fail={summary.get('fail', 0)} missing={summary.get('missing', 0)} pass={summary.get('pass', 0)}")
    if args.fail_on_issues and (summary.get("fail", 0) or summary.get("missing", 0)):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
