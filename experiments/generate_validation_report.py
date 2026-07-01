#!/usr/bin/env python3
import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def number(value, default=0.0):
    try:
        if value in ("", None):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def mean(values):
    return sum(values) / len(values) if values else 0.0


def sd(values):
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((value - m) ** 2 for value in values) / (len(values) - 1))


def ci95(values):
    if len(values) < 2:
        m = mean(values)
        return m, m
    m = mean(values)
    half_width = 1.96 * sd(values) / math.sqrt(len(values))
    return m - half_width, m + half_width


def fmt(value, digits=3):
    return f"{value:.{digits}f}"


def stochasticity_tables(rows):
    by_profile_seed = defaultdict(dict)
    for row in rows:
        by_profile_seed[(row["profile"], row["seed"])][row["phase"]] = row

    profiles = sorted({row["profile"] for row in rows})
    phases = ["relocated_early", "relocated_total"]
    metrics = {}
    for profile in profiles:
        profile_rows = [items for (p, _seed), items in by_profile_seed.items() if p == profile]
        metrics[profile] = {}
        for phase in phases:
            ratios = []
            trips = []
            collected = []
            traffic = []
            exploration = []
            for items in profile_rows:
                initial = items.get("initial_food")
                current = items.get(phase)
                if not initial or not current:
                    continue
                initial_trips = number(initial.get("phase_food_trips"))
                initial_collected = number(initial.get("phase_food_collected"))
                current_trips = number(current.get("phase_food_trips"))
                current_collected = number(current.get("phase_food_collected"))
                if initial_trips > 0:
                    ratios.append(current_trips / initial_trips)
                trips.append(current_trips)
                collected.append(current_collected / initial_collected if initial_collected > 0 else 0)
                traffic.append(number(current.get("avg_traffic_load")))
                exploration.append(number(current.get("avg_exploration_drive")))
            metrics[profile][phase] = {
                "n": len(trips),
                "trip_ratio_mean": mean(ratios),
                "trip_ratio_ci": ci95(ratios),
                "trip_mean": mean(trips),
                "trip_ci": ci95(trips),
                "collected_ratio_mean": mean(collected),
                "traffic_mean": mean(traffic),
                "exploration_mean": mean(exploration),
            }
    return metrics


def build_report(rows, target_path):
    metrics = stochasticity_tables(rows)
    model_version = next((row.get("model_version") for row in rows if row.get("model_version")), "unknown")
    seed_count = len({row["seed"] for row in rows})
    profiles = sorted(metrics)
    diverse_early = metrics.get("diverse", {}).get("relocated_early", {}).get("trip_ratio_mean", 0)
    low_early = metrics.get("low", {}).get("relocated_early", {}).get("trip_ratio_mean", 0)
    medium_early = metrics.get("medium", {}).get("relocated_early", {}).get("trip_ratio_mean", 0)

    margin = 0.05
    if diverse_early > low_early + margin and medium_early > low_early + margin:
        alignment = "partial-positive: diverse and medium both exceed low by a practical margin on early relocation ratio"
    elif diverse_early > low_early:
        alignment = "partial: diverse exceeds low on early relocation ratio, while medium is not clearly separated"
    else:
        alignment = "mismatch: diverse does not exceed low on early relocation ratio"

    lines = [
        "# Ant-Colony-Sim Biological Validation Report",
        "",
        f"- model_version: `{model_version}`",
        f"- seeds: `{seed_count}`",
        f"- source_csv: `{target_path}`",
        f"- interpretation: `{alignment}`",
        "",
        "## Stochasticity Relocation Probe",
        "",
        "This probe is a qualitative comparison against Shiraishi-style diverse stochasticity, not a fitted reproduction of the paper's optimum curve.",
        "",
        "### Early Relocation Adaptation",
        "",
        "| profile | n | mean trips | trip ratio vs initial | 95% CI | mean traffic | mean exploration drive |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for profile in profiles:
        item = metrics[profile]["relocated_early"]
        low, high = item["trip_ratio_ci"]
        lines.append(
            "| {profile} | {n} | {trips} | {ratio} | {ci_low}-{ci_high} | {traffic} | {explore} |".format(
                profile=profile,
                n=item["n"],
                trips=fmt(item["trip_mean"], 2),
                ratio=fmt(item["trip_ratio_mean"]),
                ci_low=fmt(low),
                ci_high=fmt(high),
                traffic=fmt(item["traffic_mean"]),
                explore=fmt(item["exploration_mean"]),
            )
        )

    lines.extend([
        "",
        "### Total Relocation Exploitation",
        "",
        "| profile | n | mean trips | trip ratio vs initial | 95% CI | mean traffic | mean exploration drive |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ])
    for profile in profiles:
        item = metrics[profile]["relocated_total"]
        low, high = item["trip_ratio_ci"]
        lines.append(
            "| {profile} | {n} | {trips} | {ratio} | {ci_low}-{ci_high} | {traffic} | {explore} |".format(
                profile=profile,
                n=item["n"],
                trips=fmt(item["trip_mean"], 2),
                ratio=fmt(item["trip_ratio_mean"]),
                ci_low=fmt(low),
                ci_high=fmt(high),
                traffic=fmt(item["traffic_mean"]),
                explore=fmt(item["exploration_mean"]),
            )
        )

    lines.extend([
        "",
        "## Scientific Boundary",
        "",
        "- Supports: qualitative study of how stochasticity, traffic, memory decay and pheromone feedback interact.",
        "- Does not support: numerical prediction of real ant foraging rates or species-specific parameter claims.",
        "- Current strongest result: diverse stochasticity can exceed low-noise colonies on early relocation adaptation ratio.",
        "- Current unresolved gap: medium stochasticity is not consistently above low in the adaptive-noise v4 run, so the published optimum-shift pattern is not fully reproduced.",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate a Markdown biological validation report from experiment CSV outputs.")
    parser.add_argument("--stochasticity-csv", type=Path, default=ROOT / "outputs" / "stochasticity_probe_v4.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "biological_validation_report_v4.md")
    parser.add_argument("--json-output", type=Path, default=None)
    args = parser.parse_args()

    rows = read_csv(args.stochasticity_csv)
    report = build_report(rows, args.stochasticity_csv)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")

    metrics = stochasticity_tables(rows)
    json_path = args.json_output or args.output.with_suffix(".json")
    json_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {args.output}")
    print(f"wrote {json_path}")


if __name__ == "__main__":
    main()
