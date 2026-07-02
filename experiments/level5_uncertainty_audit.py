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


def audit(individual_fit, traffic_holdout, replicate_statistics=None, pushing_redirect=None):
    bootstrap = individual_fit.get("bootstrap", {})
    traffic = traffic_holdout.get("result", {})
    target = traffic.get("target", {})
    replicate_summary = (replicate_statistics or {}).get("summary", {})
    pushing_result = (pushing_redirect or {}).get("result", {})
    replicate_ci_ready = (
        replicate_summary.get("core_metric_count", 0) > 0
        and replicate_summary.get("core_metric_ci_ready") == replicate_summary.get("core_metric_count")
        and not replicate_summary.get("underpowered_core_metrics")
    )
    pushing_holdout_pass = pushing_result.get("status") == "pass"
    checks = {
        "fit_curve_bootstrap_ci": bootstrap.get("status") == "available",
        "holdout_curve_present": traffic.get("status") == "pass",
        "holdout_has_variance_values": target.get("low_speed_sd") is not None and target.get("high_speed_sd") is not None,
        "paper_condition_replicate_ci": replicate_ci_ready,
        "independent_pushing_redirect_holdout": pushing_holdout_pass,
        "holdout_formal_ci_available": bool(target.get("formal_ci_available")),
    }
    level5_ready = all(checks.values())
    if (
        checks["fit_curve_bootstrap_ci"]
        and checks["holdout_has_variance_values"]
        and checks["paper_condition_replicate_ci"]
        and checks["independent_pushing_redirect_holdout"]
    ):
        estimated_level = 4.4
    elif checks["fit_curve_bootstrap_ci"] and checks["holdout_has_variance_values"] and checks["paper_condition_replicate_ci"]:
        estimated_level = 4.3
    elif checks["fit_curve_bootstrap_ci"] and checks["holdout_has_variance_values"]:
        estimated_level = 4.2
    else:
        estimated_level = 4.0
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
        "replicate_uncertainty": {
            "status": replicate_summary.get("status", "missing"),
            "condition_count": replicate_summary.get("condition_count", 0),
            "summary_pass_fraction": replicate_summary.get("summary_pass_fraction"),
            "core_metric_count": replicate_summary.get("core_metric_count", 0),
            "core_metric_ci_ready": replicate_summary.get("core_metric_ci_ready", 0),
            "min_n": replicate_summary.get("min_n"),
            "underpowered_core_metrics": replicate_summary.get("underpowered_core_metrics", []),
        },
        "pushing_redirect_holdout": {
            "status": pushing_result.get("status", "missing"),
            "target_probability": pushing_result.get("target", {}).get("value"),
            "target_ci95_low": pushing_result.get("target", {}).get("ci95_low"),
            "target_ci95_high": pushing_result.get("target", {}).get("ci95_high"),
            "model_mean_redirect_per_encounter": pushing_result.get("model", {}).get("mean_redirect_per_encounter"),
            "model_ci95_redirect_per_encounter": pushing_result.get("model", {}).get("ci95_redirect_per_encounter"),
            "replicates": pushing_result.get("model", {}).get("replicates"),
            "source": "Dussutour et al. 2004",
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
    replicate = result["replicate_uncertainty"]
    pushing = result["pushing_redirect_holdout"]
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
        "## Paper-Condition Replicate Uncertainty",
        "",
        f"- replicate status: `{replicate['status']}`",
        f"- condition count: `{replicate['condition_count']}`",
        f"- summary pass fraction: `{replicate['summary_pass_fraction']}`",
        f"- core metrics with CI: `{replicate['core_metric_ci_ready']}` / `{replicate['core_metric_count']}`",
        f"- minimum replicate count: `{replicate['min_n']}`",
        f"- underpowered core metrics: `{replicate['underpowered_core_metrics']}`",
        "",
        "## Pushing Redirect Holdout",
        "",
        f"- holdout status: `{pushing['status']}`",
        f"- source: {pushing['source']}",
        f"- target probability: `{pushing['target_probability']}`",
        f"- target 95% CI: `[{pushing['target_ci95_low']}, {pushing['target_ci95_high']}]`",
        f"- model mean redirect per encounter: `{pushing['model_mean_redirect_per_encounter']}`",
        f"- model 95% CI: `{pushing['model_ci95_redirect_per_encounter']}`",
        f"- replicates: `{pushing['replicates']}`",
        "",
        "## Interpretation",
        "",
        "The simulator has moved beyond Level 4 by attaching bootstrap uncertainty to the fitted individual-response curve, replicate uncertainty to paper-condition probes, and an independent crowded-traffic pushing holdout. The traffic speed holdout includes reported SD values, but formal confidence intervals require density-bin sample sizes or raw tracking data from the source experiment.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Audit Level 5 uncertainty readiness.")
    parser.add_argument("--individual-fit", type=Path, default=ROOT / "outputs" / "individual_response_curve_fit.json")
    parser.add_argument("--traffic-holdout", type=Path, default=ROOT / "outputs" / "traffic_holdout_validation.json")
    parser.add_argument("--replicate-statistics", type=Path, default=None)
    parser.add_argument("--pushing-redirect", type=Path, default=None)
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "level5_uncertainty_audit.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "level5_uncertainty_audit.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "level5_uncertainty_audit.md")
    parser.add_argument("--fail-on-regression", action="store_true")
    args = parser.parse_args()

    replicate_statistics = read_json(args.replicate_statistics) if args.replicate_statistics else None
    pushing_redirect = read_json(args.pushing_redirect) if args.pushing_redirect else None
    result = audit(read_json(args.individual_fit), read_json(args.traffic_holdout), replicate_statistics, pushing_redirect)
    write_csv(args.csv_output, result)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "individual_fit": str(args.individual_fit),
                "traffic_holdout": str(args.traffic_holdout),
                "replicate_statistics": str(args.replicate_statistics) if args.replicate_statistics else None,
                "pushing_redirect": str(args.pushing_redirect) if args.pushing_redirect else None,
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
    if args.fail_on_regression:
        if not result["checks"]["fit_curve_bootstrap_ci"]:
            return 1
        if args.replicate_statistics and not result["checks"]["paper_condition_replicate_ci"]:
            return 1
        if args.pushing_redirect and not result["checks"]["independent_pushing_redirect_holdout"]:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
