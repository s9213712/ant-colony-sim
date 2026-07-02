#!/usr/bin/env python3
"""Summarize replicate-level uncertainty for literature condition probes."""

import argparse
import csv
import json
import math
import random
import time
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_NUMERIC_FIELDS = {
    "seed",
    "ants",
}

CORE_METRICS = {
    "single_food_trail": [
        "food_trips",
        "food_collected",
        "gradient_alignment_ratio",
        "trail_segment_mean_speed",
    ],
    "rain_food_removal_washout": [
        "food_pheromone_ratio",
        "nest_pheromone_ratio",
    ],
    "double_bridge_unbiased_baseline": [
        "seeded_return_fraction",
        "return_dominance",
        "return_branch_curve_error",
    ],
    "double_bridge_upper_bias": [
        "seeded_return_fraction",
        "seeded_return_crossings",
        "return_dominance",
        "return_branch_curve_error",
    ],
    "double_bridge_lower_bias": [
        "seeded_return_fraction",
        "seeded_return_crossings",
        "return_dominance",
        "return_branch_curve_error",
    ],
    "crowding_low_density_bridge": [
        "total_crossings",
        "avg_traffic_load",
        "upper_segment_flow",
        "lower_segment_flow",
    ],
    "crowding_high_density_bridge": [
        "total_crossings",
        "avg_traffic_load",
        "traffic_redirect_per_encounter",
        "upper_segment_flow",
        "lower_segment_flow",
    ],
    "no_jam_low_density": [
        "mean_displacement",
        "segment_density",
        "segment_abs_forward_speed",
        "segment_flow",
    ],
    "no_jam_high_density": [
        "mean_displacement",
        "segment_density",
        "segment_abs_forward_speed",
        "traffic_redirect_per_encounter",
        "segment_flow",
    ],
    "food_quality_recruitment": [
        "high_quality_food_trips",
        "low_quality_food_trips",
        "avg_collected_food_quality",
    ],
    "necrophoresis_cleanup_latency": [
        "initial_nest_corpses",
        "final_nest_corpses",
        "disposed_corpses",
        "corpse_moves",
    ],
    "army_ant_mill_mortality": [
        "survivor_fraction",
        "corpse_fraction",
        "mills",
    ],
    "nest_relocation_quorum_choice": [
        "high_quality_site_visits",
        "low_quality_site_visits",
        "nest_quorum_events",
        "nest_relocations",
        "nest_relocation_completed",
    ],
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def as_float(value):
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        number = float(value)
    elif isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        try:
            number = float(text)
        except ValueError:
            return None
    else:
        return None
    if math.isfinite(number):
        return number
    return None


def mean(values):
    return sum(values) / len(values) if values else None


def sample_sd(values):
    if len(values) < 2:
        return None
    avg = mean(values)
    variance = sum((value - avg) ** 2 for value in values) / (len(values) - 1)
    return math.sqrt(variance)


def percentile(values, p):
    if not values:
        return None
    ordered = sorted(values)
    index = (len(ordered) - 1) * p
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[int(index)]
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def bootstrap_ci(values, samples, seed):
    if len(values) < 2 or samples <= 0:
        return None
    rng = random.Random(seed)
    boot = []
    for _ in range(samples):
        draw = [values[rng.randrange(len(values))] for _ in values]
        boot.append(mean(draw))
    return [percentile(boot, 0.025), percentile(boot, 0.975)]


def rounded(value, digits=6):
    if value is None:
        return ""
    return round(value, digits)


def stable_offset(*parts):
    text = "::".join(str(part) for part in parts)
    total = 0
    for index, char in enumerate(text, start=1):
        total += index * ord(char)
    return total % 1_000_000


def collect_condition_metrics(raw_rows, include_all_numeric=False):
    grouped = defaultdict(list)
    for row in raw_rows:
        condition = row.get("condition")
        if condition:
            grouped[condition].append(row)

    metric_values = defaultdict(list)
    for condition, rows in grouped.items():
        allowed = set(CORE_METRICS.get(condition, []))
        for row in rows:
            for key, value in row.items():
                if key in EXCLUDED_NUMERIC_FIELDS:
                    continue
                if not include_all_numeric and key not in allowed:
                    continue
                number = as_float(value)
                if number is not None:
                    metric_values[(condition, key)].append(number)
    return grouped, metric_values


def build_rows(payload, samples, seed, include_all_numeric=False):
    raw_rows = payload.get("raw_rows", [])
    summaries = payload.get("summaries", [])
    grouped, metric_values = collect_condition_metrics(raw_rows, include_all_numeric)
    status_by_condition = {row.get("condition"): row.get("status") for row in summaries}

    rows = []
    for (condition, metric), values in sorted(metric_values.items()):
        sd = sample_sd(values)
        sem = sd / math.sqrt(len(values)) if sd is not None else None
        ci = bootstrap_ci(values, samples, seed + stable_offset(condition, metric))
        rows.append({
            "condition": condition,
            "metric": metric,
            "n": len(values),
            "mean": rounded(mean(values)),
            "sd": rounded(sd),
            "sem": rounded(sem),
            "ci95_low": rounded(ci[0]) if ci else "",
            "ci95_high": rounded(ci[1]) if ci else "",
            "summary_status": status_by_condition.get(condition, ""),
            "is_core_metric": "yes" if metric in CORE_METRICS.get(condition, []) else "no",
        })

    condition_counts = [
        {
            "condition": condition,
            "raw_rows": len(rows_for_condition),
            "summary_status": status_by_condition.get(condition, ""),
        }
        for condition, rows_for_condition in sorted(grouped.items())
    ]
    return rows, condition_counts, summaries


def summarize(rows, condition_counts, summaries, min_n):
    core_rows = [row for row in rows if row["is_core_metric"] == "yes"]
    underpowered = [
        f"{row['condition']}:{row['metric']}"
        for row in core_rows
        if int(row["n"]) < min_n
    ]
    ci_ready = [
        row for row in core_rows
        if int(row["n"]) >= min_n and row["ci95_low"] != "" and row["ci95_high"] != ""
    ]
    passed_conditions = sum(1 for row in summaries if row.get("status") == "pass")
    summary_statuses = sum(1 for row in summaries if row.get("status"))
    return {
        "condition_count": len(condition_counts),
        "summary_status_count": summary_statuses,
        "summary_pass_count": passed_conditions,
        "summary_pass_fraction": round(passed_conditions / summary_statuses, 4) if summary_statuses else None,
        "core_metric_count": len(core_rows),
        "core_metric_ci_ready": len(ci_ready),
        "underpowered_core_metrics": underpowered,
        "min_n": min_n,
        "status": "pass" if core_rows and not underpowered else "needs_more_replicates",
    }


def write_csv(path, rows):
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


def write_report(path, summary, rows, source_path):
    lines = [
        "# Level 5 Replicate Statistics",
        "",
        "This report adds replicate-level uncertainty to literature-condition probes without changing simulator rules.",
        "",
        "## Summary",
        "",
        f"- source: `{source_path}`",
        f"- status: `{summary['status']}`",
        f"- condition count: `{summary['condition_count']}`",
        f"- summary pass fraction: `{summary['summary_pass_fraction']}`",
        f"- core metrics with bootstrap CI: `{summary['core_metric_ci_ready']}` / `{summary['core_metric_count']}`",
        f"- minimum replicate count required: `{summary['min_n']}`",
        "",
        "## Core Metric CI",
        "",
        "| Condition | Metric | n | Mean | SD | 95% CI |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        if row["is_core_metric"] != "yes":
            continue
        ci_text = f"[{row['ci95_low']}, {row['ci95_high']}]" if row["ci95_low"] != "" else ""
        lines.append(
            f"| `{row['condition']}` | `{row['metric']}` | {row['n']} | "
            f"{row['mean']} | {row['sd']} | {ci_text} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "Level 5 is not a claim of perfect biological realism. It means the simulator can report uncertainty across repeated stochastic runs, preserve paper-condition raw rows, and expose which claims remain underpowered or only qualitative.",
    ])
    if summary["underpowered_core_metrics"]:
        lines.extend([
            "",
            "## Underpowered Core Metrics",
            "",
        ])
        for item in summary["underpowered_core_metrics"]:
            lines.append(f"- `{item}`")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build Level 5 replicate statistics from paper-condition raw rows.")
    parser.add_argument("--paper-conditions", type=Path, default=ROOT / "outputs" / "paper_conditions_v5.json")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "level5_replicate_statistics.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "level5_replicate_statistics.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "level5_replicate_statistics.md")
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    parser.add_argument("--bootstrap-seed", type=int, default=55123)
    parser.add_argument("--min-n", type=int, default=3)
    parser.add_argument("--include-all-numeric", action="store_true")
    parser.add_argument("--fail-on-underpowered", action="store_true")
    args = parser.parse_args()

    payload = read_json(args.paper_conditions)
    rows, condition_counts, summaries = build_rows(
        payload,
        args.bootstrap_samples,
        args.bootstrap_seed,
        include_all_numeric=args.include_all_numeric,
    )
    summary = summarize(rows, condition_counts, summaries, args.min_n)
    write_csv(args.csv_output, rows)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "source": str(args.paper_conditions),
                "summary": summary,
                "condition_counts": condition_counts,
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_report(args.report_output, summary, rows, args.paper_conditions)
    print(
        "level5 replicate statistics: "
        f"status={summary['status']} "
        f"core_metric_ci_ready={summary['core_metric_ci_ready']}/{summary['core_metric_count']}"
    )
    if args.fail_on_underpowered and summary["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
