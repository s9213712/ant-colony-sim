#!/usr/bin/env python3
"""Audit uncertainty and external-validation readiness beyond Level 4."""

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


def audit(individual_fit, traffic_holdout):
    bootstrap = individual_fit.get("bootstrap", {})
    traffic = traffic_holdout.get("result", {})
    target = traffic.get("target", {})
    checks = {
        "fit_curve_bootstrap_ci": bootstrap.get("status") == "available",
        "holdout_curve_present": traffic.get("status") == "pass",
        "holdout_has_variance_values": target.get("low_speed_sd") is not None and target.get("high_speed_sd") is not None,
        "holdout_formal_ci_available": bool(target.get("formal_ci_available")),
    }
    level5_ready = all(checks.values())
    estimated_level = 4.2 if checks["fit_curve_bootstrap_ci"] and checks["holdout_has_variance_values"] else 4.0
    if level5_ready:
        blocker = "Needs broader independent external datasets before Level 5 can be claimed."
    elif not checks["holdout_formal_ci_available"]:
        blocker = "Holdout has SD values but lacks density-bin sample sizes, so formal holdout CI is not available."
    else:
        blocker = "Uncertainty evidence is incomplete."
    return {
        "estimated_level": estimated_level,
        "level5_ready": level5_ready,
        "blocker": blocker,
        "checks": checks,
        "fit_uncertainty": {
            "bootstrap_status": bootstrap.get("status", "missing"),
            "bootstrap_samples_used": bootstrap.get("samples_used", 0),
            "amplitude_A_ci_95": bootstrap.get("amplitude_A_ci_95"),
            "beta_ci_95": bootstrap.get("beta_ci_95"),
            "r2_log_space_ci_95": bootstrap.get("r2_log_space_ci_95"),
        },
        "holdout_uncertainty": {
            "status": traffic.get("status"),
            "low_speed_sd": target.get("low_speed_sd"),
            "high_speed_sd": target.get("high_speed_sd"),
            "low_n": target.get("low_n"),
            "high_n": target.get("high_n"),
            "formal_ci_available": target.get("formal_ci_available"),
            "uncertainty_note": traffic.get("uncertainty_note"),
        },
    }


def write_csv(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "check": key,
            "pass": bool_status(value),
        }
        for key, value in result["checks"].items()
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["check", "pass"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_report(path, result):
    fit = result["fit_uncertainty"]
    holdout = result["holdout_uncertainty"]
    lines = [
        "# Level 5 Uncertainty Audit",
        "",
        "This audit tracks whether the Level 4 curves have enough uncertainty information for Level 5-style quantitative claims.",
        "",
        "## Summary",
        "",
        f"- estimated level: `{result['estimated_level']}`",
        f"- Level 5 ready: `{result['level5_ready']}`",
        f"- blocker: {result['blocker']}",
        "",
        "## Checks",
        "",
    ]
    for key, value in result["checks"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend([
        "",
        "## Fit-Curve Uncertainty",
        "",
        f"- bootstrap status: `{fit['bootstrap_status']}`",
        f"- bootstrap samples used: `{fit['bootstrap_samples_used']}`",
        f"- A 95% CI: `{fit['amplitude_A_ci_95']}`",
        f"- beta 95% CI: `{fit['beta_ci_95']}`",
        f"- R2 95% CI: `{fit['r2_log_space_ci_95']}`",
        "",
        "## Holdout Uncertainty",
        "",
        f"- holdout status: `{holdout['status']}`",
        f"- low-density speed SD: `{holdout['low_speed_sd']}`",
        f"- high-density speed SD: `{holdout['high_speed_sd']}`",
        f"- low-density n: `{holdout['low_n']}`",
        f"- high-density n: `{holdout['high_n']}`",
        f"- formal CI available: `{holdout['formal_ci_available']}`",
        f"- note: {holdout['uncertainty_note']}",
        "",
        "## Interpretation",
        "",
        "The simulator has moved beyond Level 4 by attaching bootstrap uncertainty to the fitted individual-response curve. The traffic holdout includes reported SD values, but formal confidence intervals require density-bin sample sizes or raw tracking data from the source experiment.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Audit Level 5 uncertainty readiness.")
    parser.add_argument("--individual-fit", type=Path, default=ROOT / "outputs" / "individual_response_curve_fit.json")
    parser.add_argument("--traffic-holdout", type=Path, default=ROOT / "outputs" / "traffic_holdout_validation.json")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "level5_uncertainty_audit.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "level5_uncertainty_audit.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "level5_uncertainty_audit.md")
    parser.add_argument("--fail-on-regression", action="store_true")
    args = parser.parse_args()

    result = audit(read_json(args.individual_fit), read_json(args.traffic_holdout))
    write_csv(args.csv_output, result)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "individual_fit": str(args.individual_fit),
                "traffic_holdout": str(args.traffic_holdout),
                "result": result,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(args.report_output, result)
    print(
        f"level5 uncertainty audit: estimated_level={result['estimated_level']} "
        f"level5_ready={result['level5_ready']}"
    )
    if args.fail_on_regression and not result["checks"]["fit_curve_bootstrap_ci"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
