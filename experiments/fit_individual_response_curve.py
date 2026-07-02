#!/usr/bin/env python3
"""Fit primary-source individual pheromone response curves."""

import argparse
import csv
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_rows(path, target_id):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = [
            row for row in csv.DictReader(handle)
            if row.get("target_id") == target_id
        ]
    if len(rows) < 3:
        raise RuntimeError(f"need at least 3 rows for {target_id}, found {len(rows)}")
    return rows


def fit_power_law(rows):
    xs = [float(row["x_value"]) for row in rows]
    ys = [float(row["y_value"]) for row in rows]
    log_x = [math.log(x) for x in xs]
    log_y = [math.log(y) for y in ys]
    n = len(rows)
    mean_x = sum(log_x) / n
    mean_y = sum(log_y) / n
    sxx = sum((x - mean_x) ** 2 for x in log_x)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(log_x, log_y))
    slope = sxy / sxx
    intercept = mean_y - slope * mean_x
    beta = -slope
    amplitude = math.exp(intercept)
    predictions = [amplitude * (x ** -beta) for x in xs]
    ss_res = sum((math.log(y) - math.log(pred)) ** 2 for y, pred in zip(ys, predictions))
    ss_tot = sum((y - mean_y) ** 2 for y in log_y)
    r2 = 1 - ss_res / ss_tot if ss_tot else 1
    residual_rows = []
    for row, x, y, pred in zip(rows, xs, ys, predictions):
        residual_rows.append({
            "source_id": row["source_id"],
            "target_id": row["target_id"],
            "x_value": x,
            "observed_y": y,
            "predicted_y": pred,
            "relative_error": (pred - y) / y if y else None,
        })
    return {
        "amplitude_A": amplitude,
        "beta": beta,
        "r2_log_space": r2,
        "n": n,
        "residual_rows": residual_rows,
    }


def summarize_fit(fit):
    figure6_a_ci = {
        "amplitude_A_low": 36.90,
        "amplitude_A_high": 48.74,
        "beta_low": 1.037,
        "beta_high": 1.079,
        "reported_r2": 0.9982,
    }
    strict_a_ok = figure6_a_ci["amplitude_A_low"] <= fit["amplitude_A"] <= figure6_a_ci["amplitude_A_high"]
    strict_beta_ok = figure6_a_ci["beta_low"] <= fit["beta"] <= figure6_a_ci["beta_high"]
    r2_ok = fit["r2_log_space"] >= 0.995
    rounding_a_ok = abs(fit["amplitude_A"] - 42.41) / 42.41 <= 0.20
    rounding_beta_ok = abs(fit["beta"] - 1.058) <= 0.05
    pass_with_reconstruction = rounding_a_ok and rounding_beta_ok and r2_ok
    return {
        "status": "pass" if pass_with_reconstruction else "needs_review",
        "strict_ci_status": "pass" if strict_a_ok and strict_beta_ok and r2_ok else "needs_review",
        "checks": {
            "amplitude_in_reported_ci": strict_a_ok,
            "beta_in_reported_ci": strict_beta_ok,
            "amplitude_within_20pct_of_reported": rounding_a_ok,
            "beta_within_0_05_of_reported": rounding_beta_ok,
            "r2_at_least_0_995": r2_ok,
        },
        "reported_reference": figure6_a_ci,
        "interpretation": (
            "Fit is usable as a rounded/bin-reconstructed Perna et al. Figure 5 response target; strict Figure 6 confidence-interval reproduction still needs raw x/y data."
            if pass_with_reconstruction
            else "Fit does not meet the rounded/bin-reconstruction tolerance; inspect source rows before using for calibration."
        ),
    }


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = ["source_id", "target_id", "x_value", "observed_y", "predicted_y", "relative_error"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_report(path, target_path, fit, summary):
    lines = [
        "# Individual Pheromone Response Fit",
        "",
        "This report fits a primary-source individual pheromone response target from Perna et al. 2012.",
        "",
        f"- Target CSV: `{target_path}`",
        "- Source: Perna et al. 2012, Individual rules for trail pattern formation in Argentine ants (Linepithema humile), https://arxiv.org/abs/1201.5827",
        "- Data provenance: Figure 5 legend gives the six slope values; Figure 6 reports the no-evaporation power-law fit and confidence interval.",
        "",
        "## Fit",
        "",
        f"- status: `{summary['status']}`",
        f"- strict CI status: `{summary['strict_ci_status']}`",
        f"- fitted A: `{fit['amplitude_A']:.4f}`",
        f"- fitted beta: `{fit['beta']:.4f}`",
        f"- log-space R2: `{fit['r2_log_space']:.5f}`",
        f"- rows: `{fit['n']}`",
        "",
        "## Reference Interval",
        "",
        "- Reported Figure 6 no-evaporation fit: A = 42.41 with 95% CI [36.90, 48.74].",
        "- Reported beta = 1.058 with 95% CI [1.037, 1.079].",
        "- Reported R2 = 0.9982.",
        "",
        "## Interpretation",
        "",
        summary["interpretation"],
        "",
        "Caveat: the target CSV reconstructs x-values from the Figure 5 pheromone-bin ranges using geometric midpoints and uses rounded slope values from the figure legend. This is fit-ready for submodel calibration, but exact strict-CI reproduction requires raw figure data or author-provided data.",
        "",
        "This is a quantitative target for the individual pheromone-response submodel. It does not yet validate full colony-level food retrieval, physical pheromone half-life, or a separate holdout curve.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Fit individual pheromone response curve targets.")
    parser.add_argument("--target-csv", type=Path, default=ROOT / "targets" / "digitized_curves" / "perna_2012_individual_pheromone_response.csv")
    parser.add_argument("--target-id", default="individual_pheromone_response_curve")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "individual_response_curve_fit.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "individual_response_curve_fit.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "individual_response_curve_fit.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    args = parser.parse_args()

    rows = read_rows(args.target_csv, args.target_id)
    fit = fit_power_law(rows)
    summary = summarize_fit(fit)
    write_csv(args.csv_output, fit["residual_rows"])
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "target_csv": str(args.target_csv),
                "target_id": args.target_id,
                "fit": {key: value for key, value in fit.items() if key != "residual_rows"},
                "summary": summary,
                "residual_rows": fit["residual_rows"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(args.report_output, args.target_csv, fit, summary)
    print(
        f"fit {args.target_id}: status={summary['status']} "
        f"A={fit['amplitude_A']:.4f} beta={fit['beta']:.4f} r2={fit['r2_log_space']:.5f}"
    )
    if args.fail_on_issues and summary["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
