#!/usr/bin/env python3
import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


DEFAULT_METRICS = [
    "ants",
    "brood_total",
    "food_store",
    "water_store",
    "avg_energy",
    "avg_hydration",
    "food_trips",
    "water_trips",
    "foraging_trips",
    "food_trip_rate",
    "water_trip_rate",
    "corpse_moves",
    "corpse_move_rate",
    "nest_corpses",
    "disposed_corpses",
    "food_pheromone",
    "water_pheromone",
    "death_pheromone",
    "task_food",
    "task_water",
    "task_brood",
    "task_corpse",
    "state_following_food_trail",
    "state_carrying_food",
    "state_corpse_cleanup",
]


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def summarize(rows, metrics):
    grouped = defaultdict(list)
    for row in rows:
        key = (row.get("scenario", ""), row.get("day", ""))
        grouped[key].append(row)

    output = []
    for (scenario, day), group in sorted(grouped.items(), key=lambda item: (item[0][0], float(item[0][1]))):
        summary = {
            "scenario": scenario,
            "day": day,
            "n": len(group),
        }
        for metric in metrics:
            values = [to_float(row.get(metric)) for row in group]
            values = [value for value in values if value is not None]
            if not values:
                continue
            mean = sum(values) / len(values)
            variance = sum((value - mean) ** 2 for value in values) / max(1, len(values) - 1)
            summary[f"{metric}_mean"] = round(mean, 6)
            summary[f"{metric}_sd"] = round(math.sqrt(variance), 6)
        output.append(summary)
    return output


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows):
    if not rows:
        raise RuntimeError("no summary rows produced")
    headers = []
    for row in rows:
        for key in row:
            if key not in headers:
                headers.append(key)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Summarize Ant-Colony-Sim batch CSV by scenario/day.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metric", action="append", default=[], help="Metric to summarize; defaults to biological validation metrics")
    args = parser.parse_args()

    metrics = args.metric or DEFAULT_METRICS
    rows = read_csv(args.input)
    summary = summarize(rows, metrics)
    write_csv(args.output, summary)
    print(f"wrote {len(summary)} summary rows to {args.output}")


if __name__ == "__main__":
    main()
