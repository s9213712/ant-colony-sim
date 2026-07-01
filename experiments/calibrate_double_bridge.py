#!/usr/bin/env python3
import argparse
import csv
import itertools
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "experiments" / "double_bridge_probe.py"


def parse_grid(items):
    grid = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"grid item must be name=a,b,c, got {item!r}")
        name, values = item.split("=", 1)
        parsed = []
        for raw in values.split(","):
            raw = raw.strip()
            if not raw:
                continue
            parsed.append(int(raw) if raw.isdigit() else float(raw))
        if not parsed:
            raise ValueError(f"no values for {name!r}")
        grid[name.strip()] = parsed
    return grid


def iter_param_sets(grid):
    names = list(grid)
    for values in itertools.product(*(grid[name] for name in names)):
        yield dict(zip(names, values))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def run_probe(args, params, scenario_name, bias_branch, bias_strength, output_path):
    cmd = [
        sys.executable,
        str(PROBE),
        "--seeds",
        args.seeds,
        "--days",
        str(args.days),
        "--sample-days",
        str(args.sample_days),
        "--dt",
        str(args.dt),
        "--ants",
        str(args.ants),
        "--pheromone-strength",
        str(params.get("pheromoneStrength", args.pheromone_strength)),
        "--diffusion-rate",
        str(params.get("diffusionRate", args.diffusion_rate)),
        "--evaporation-rate",
        str(params.get("evaporationRate", args.evaporation_rate)),
        "--sense-threshold",
        str(params.get("senseThreshold", args.sense_threshold)),
        "--output",
        str(output_path),
    ]
    if bias_branch != "none":
        cmd.extend(["--bias-branch", bias_branch, "--bias-strength", str(bias_strength)])
    proc = subprocess.run(cmd, cwd=str(ROOT.parent), text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(
            "double_bridge_probe failed\n"
            + "command: "
            + " ".join(cmd)
            + "\nstdout:\n"
            + proc.stdout
            + "\nstderr:\n"
            + proc.stderr
        )
    metadata = read_json(output_path.with_suffix(".json"))
    return {
        "scenario": scenario_name,
        "stdout": proc.stdout,
        "summary": metadata["summary"],
        "rows": metadata["rows"],
        "output": str(output_path),
        "metadata": str(output_path.with_suffix(".json")),
    }


def metric_summary(equal_summary, bias_summary):
    runs = max(equal_summary["runs"], 1)
    equal_upper_rate = equal_summary["upper_selected"] / runs
    equal_balance = 1 - abs(equal_upper_rate - 0.5) * 2
    bias_runs = max(bias_summary["runs"], 1)
    upper_bias_rate = bias_summary["upper_selected"] / bias_runs
    return {
        "equal_branch_selected_balance": equal_balance,
        "equal_branch_upper_selection_rate": equal_upper_rate,
        "equal_branch_mean_dominance": equal_summary["mean_dominance"],
        "upper_bias_selection_rate": upper_bias_rate,
        "upper_bias_mean_dominance": bias_summary["mean_dominance"],
        "biased_vs_equal_dominance_gain": bias_summary["mean_dominance"] - equal_summary["mean_dominance"],
        "equal_mean_food_trips": equal_summary["mean_food_trips"],
        "upper_bias_mean_food_trips": bias_summary["mean_food_trips"],
    }


def score(metrics, target):
    total = 0.0
    parts = {}
    for name, spec in target["metrics"].items():
        value = float(metrics[name])
        target_value = float(spec["target"])
        sd = max(float(spec.get("sd", 1)), 1e-9)
        weight = float(spec.get("weight", 1))
        loss = weight * ((value - target_value) / sd) ** 2
        parts[f"{name}_value"] = round(value, 6)
        parts[f"{name}_target"] = target_value
        parts[f"{name}_loss"] = round(loss, 6)
        total += loss
    parts["loss"] = round(total, 6)
    return parts


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = []
    for row in rows:
        for key in row:
            if key not in headers:
                headers.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Calibrate double-bridge behavior against a Deneubourg-style reference target.")
    parser.add_argument("--targets", type=Path, default=ROOT / "targets" / "deneubourg_choice_reference.json")
    parser.add_argument("--seeds", default="1-8")
    parser.add_argument("--days", type=float, default=8)
    parser.add_argument("--sample-days", type=float, default=0.1)
    parser.add_argument("--dt", type=float, default=9)
    parser.add_argument("--ants", type=int, default=240)
    parser.add_argument("--pheromone-strength", type=float, default=95)
    parser.add_argument("--diffusion-rate", type=float, default=100)
    parser.add_argument("--evaporation-rate", type=float, default=90)
    parser.add_argument("--sense-threshold", type=float, default=14)
    parser.add_argument("--upper-bias-strength", type=float, default=350)
    parser.add_argument("--grid", action="append", default=[
        "pheromoneStrength=95,120",
        "senseThreshold=10,14",
        "evaporationRate=80,100",
    ])
    parser.add_argument("--output", type=Path, default=ROOT / "calibration_results" / "double_bridge_calibration.csv")
    parser.add_argument("--run-dir", type=Path, default=ROOT / "calibration_results" / "double_bridge_runs")
    args = parser.parse_args()

    target = read_json(args.targets)
    grid = parse_grid(args.grid)
    all_rows = []
    run_details = []

    for index, params in enumerate(iter_param_sets(grid), start=1):
        stem = "_".join(f"{key}-{value}" for key, value in params.items())
        equal_path = args.run_dir / f"{index:03d}_{stem}_equal.csv"
        bias_path = args.run_dir / f"{index:03d}_{stem}_upper_bias.csv"
        equal = run_probe(args, params, "equal", "none", 0, equal_path)
        bias = run_probe(args, params, "upper_bias", "upper", args.upper_bias_strength, bias_path)
        metrics = metric_summary(equal["summary"], bias["summary"])
        scored = score(metrics, target)
        row = {
            "run_index": index,
            **params,
            **metrics,
            **scored,
            "equal_output": equal["output"],
            "upper_bias_output": bias["output"],
        }
        all_rows.append(row)
        run_details.append({"params": params, "equal": equal["summary"], "upper_bias": bias["summary"], "metrics": metrics, "score": scored})
        print(json.dumps({"run_index": index, "params": params, "loss": scored["loss"], "metrics": metrics}, ensure_ascii=False))

    all_rows.sort(key=lambda row: row["loss"])
    write_csv(args.output, all_rows)
    metadata = {
        "target": target,
        "grid": grid,
        "seeds": args.seeds,
        "days": args.days,
        "sample_days": args.sample_days,
        "best": all_rows[0] if all_rows else None,
        "runs": run_details,
    }
    args.output.with_suffix(".json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"best: {json.dumps(all_rows[0], ensure_ascii=False)}")
    print(f"wrote {len(all_rows)} calibration rows to {args.output}")
    print(f"wrote metadata to {args.output.with_suffix('.json')}")


if __name__ == "__main__":
    main()
