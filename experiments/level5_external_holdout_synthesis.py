#!/usr/bin/env python3
"""Synthesize independent external holdouts for Level 5 readiness."""

import argparse
import csv
import json
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def bool_status(value):
    return "yes" if value else "no"


def traffic_row(path, data):
    result = data.get("result", {})
    target = result.get("target", {})
    model = result.get("model", {})
    formal_ci = bool(target.get("formal_ci_available"))
    return {
        "holdout_id": "john_2009_traffic_velocity_density",
        "source": "John et al. 2009",
        "species": target.get("species", "Leptogenys processionalis"),
        "process": "traffic_velocity_density",
        "source_path": str(path),
        "status": result.get("status", "missing"),
        "target_metric": "normalized_speed_curve_rmse",
        "target_value": 0,
        "model_value": model.get("normalized_speed_rmse"),
        "pass": result.get("status") == "pass",
        "formal_ci_available": formal_ci,
        "ci_source": "missing_density_bin_sample_sizes",
        "limitation": result.get("uncertainty_note") or "Normalized curve holdout; density-bin n is unavailable.",
    }


def pushing_row(path, data):
    result = data.get("result", {})
    target = result.get("target", {})
    model = result.get("model", {})
    target_low = target.get("ci95_low")
    target_high = target.get("ci95_high")
    model_ci = model.get("ci95_redirect_per_encounter") or [None, None]
    formal_ci = target_low is not None and target_high is not None and model_ci[0] is not None and model_ci[1] is not None
    return {
        "holdout_id": "dussutour_2004_pushing_redirect",
        "source": "Dussutour et al. 2004",
        "species": target.get("species", "Lasius niger"),
        "process": "crowded_traffic_contact_redirect",
        "source_path": str(path),
        "status": result.get("status", "missing"),
        "target_metric": "redirect_probability_per_encounter",
        "target_value": target.get("value"),
        "model_value": model.get("mean_redirect_per_encounter"),
        "pass": result.get("status") == "pass",
        "formal_ci_available": formal_ci,
        "ci_source": "published_target_ci_and_model_bootstrap_ci" if formal_ci else "missing_ci",
        "limitation": "Mechanism-level body-contact holdout; not the full bridge-width flow-density transition.",
    }


def synthesize(traffic_holdout=None, pushing_redirect=None):
    rows = []
    if traffic_holdout:
        rows.append(traffic_row(traffic_holdout, read_json(traffic_holdout)))
    if pushing_redirect:
        rows.append(pushing_row(pushing_redirect, read_json(pushing_redirect)))
    pass_count = sum(1 for row in rows if row["pass"])
    formal_ci_count = sum(1 for row in rows if row["formal_ci_available"])
    limitation_count = sum(1 for row in rows if row["limitation"])
    process_count = len({row["process"] for row in rows})
    source_count = len({row["source"] for row in rows})
    checks = {
        "independent_holdouts_at_least_2": len(rows) >= 2 and source_count >= 2,
        "holdout_pass_fraction_1_0": bool(rows) and pass_count == len(rows),
        "formal_ci_holdouts_at_least_1": formal_ci_count >= 1,
        "distinct_processes_at_least_2": process_count >= 2,
        "source_limitations_documented": limitation_count == len(rows),
    }
    status = "pass" if all(checks.values()) else "needs_work"
    blocker = None
    if not checks["independent_holdouts_at_least_2"]:
        blocker = "Needs at least two independent empirical holdout sources."
    elif not checks["formal_ci_holdouts_at_least_1"]:
        blocker = "Needs at least one empirical holdout with target and model confidence intervals."
    elif not checks["holdout_pass_fraction_1_0"]:
        blocker = "At least one independent empirical holdout is not passing."
    else:
        blocker = "External holdout synthesis passes; Level 5 still needs more paper-level quantitative curves across behavior classes."
    return {
        "status": status,
        "checks": checks,
        "summary": {
            "holdout_count": len(rows),
            "source_count": source_count,
            "process_count": process_count,
            "pass_count": pass_count,
            "formal_ci_count": formal_ci_count,
            "all_holdouts_have_formal_ci": bool(rows) and formal_ci_count == len(rows),
            "blocker": blocker,
        },
        "holdouts": rows,
    }


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "holdout_id",
        "source",
        "species",
        "process",
        "status",
        "target_metric",
        "target_value",
        "model_value",
        "pass",
        "formal_ci_available",
        "ci_source",
        "limitation",
        "source_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_report(path, result):
    summary = result["summary"]
    lines = [
        "# Level 5 External Holdout Synthesis",
        "",
        "This report separates independent empirical holdout evidence from fitted or qualitative paper-condition probes.",
        "",
        "## Summary",
        "",
        f"- status: `{result['status']}`",
        f"- holdout count: `{summary['holdout_count']}`",
        f"- independent source count: `{summary['source_count']}`",
        f"- distinct process count: `{summary['process_count']}`",
        f"- pass count: `{summary['pass_count']}`",
        f"- formal-CI holdout count: `{summary['formal_ci_count']}`",
        f"- all holdouts have formal CI: `{summary['all_holdouts_have_formal_ci']}`",
        f"- blocker: {summary['blocker']}",
        "",
        "## Checks",
        "",
    ]
    for key, value in result["checks"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend([
        "",
        "## Holdouts",
        "",
        "| Holdout | Source | Process | Status | Metric | Target | Model | Formal CI | Limitation |",
        "|---|---|---|---|---|---:|---:|---|---|",
    ])
    for row in result["holdouts"]:
        lines.append(
            f"| `{row['holdout_id']}` | {row['source']} | {row['process']} | `{row['status']}` | "
            f"{row['target_metric']} | {row['target_value']} | {row['model_value']} | "
            f"`{row['formal_ci_available']}` | {row['limitation']} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "This synthesis is a Level 5 evidence gate: passing it means the simulator has more than one independent empirical holdout and at least one formal-CI holdout. It does not by itself prove species-level predictive validity.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Synthesize Level 5 external holdout evidence.")
    parser.add_argument("--traffic-holdout", type=Path, default=ROOT / "outputs" / "traffic_holdout_validation.json")
    parser.add_argument("--pushing-redirect", type=Path, default=ROOT / "outputs" / "pushing_redirect_validation.json")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "level5_external_holdout_synthesis.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "level5_external_holdout_synthesis.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "level5_external_holdout_synthesis.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    args = parser.parse_args()

    result = synthesize(args.traffic_holdout, args.pushing_redirect)
    write_csv(args.csv_output, result["holdouts"])
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "traffic_holdout": str(args.traffic_holdout),
                "pushing_redirect": str(args.pushing_redirect),
                "result": result,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(args.report_output, result)
    print(
        f"external holdout synthesis {result['status']}: "
        f"holdouts={result['summary']['holdout_count']} "
        f"formal_ci={result['summary']['formal_ci_count']}"
    )
    if args.fail_on_issues and result["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
