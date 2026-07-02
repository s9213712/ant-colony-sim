#!/usr/bin/env python3
"""Audit readiness for quantitative species-level calibration."""

import argparse
import csv
import json
import time
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


LEVEL_BY_STATUS = {
    "ready_for_fit": 4.0,
    "model_reference_only": 3.0,
    "qualitative_proxy_only": 2.8,
    "missing_digitized_data": 2.5,
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def target_row(target):
    return {
        "target_id": target["target_id"],
        "priority": target.get("priority", "P2"),
        "status": target["status"],
        "readiness_level": LEVEL_BY_STATUS.get(target["status"], 2.0),
        "biological_process": target["biological_process"],
        "current_proxy": target.get("current_proxy", ""),
        "next_action": target.get("next_action", ""),
        "source_count": len(target.get("source_candidates", [])),
        "required_data": "; ".join(target.get("required_data", [])),
    }


def summarize(rows):
    statuses = Counter(row["status"] for row in rows)
    priorities = Counter(row["priority"] for row in rows if row["status"] != "ready_for_fit")
    ready = statuses.get("ready_for_fit", 0)
    model_reference = statuses.get("model_reference_only", 0)
    qualitative = statuses.get("qualitative_proxy_only", 0)
    missing = statuses.get("missing_digitized_data", 0)
    if ready >= 2:
        level = 4.0
        blocker = "Needs independent holdout validation and species-unit mapping before Level 5."
    elif ready >= 1:
        level = 3.5
        blocker = "Needs at least one independent validation curve and broader species-unit mapping."
    elif model_reference or qualitative:
        level = 3.0
        blocker = "Has model/proxy references but no digitized raw biological curve ready for fitting."
    else:
        level = 2.5
        blocker = "No quantitative digitized curve is ready."
    return {
        "estimated_level": level,
        "level_blocker": blocker,
        "total_targets": len(rows),
        "ready_for_fit": ready,
        "model_reference_only": model_reference,
        "qualitative_proxy_only": qualitative,
        "missing_digitized_data": missing,
        "open_p0": priorities.get("P0", 0),
        "open_p1": priorities.get("P1", 0),
        "status_counts": dict(statuses),
    }


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


def write_json(path, manifest, rows):
    payload = {
        "suite": "quantitative_readiness_audit_v1",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "manifest_id": manifest["id"],
        "claim_level": manifest["claim_level"],
        "summary": summarize(rows),
        "required_for_level_4": manifest.get("required_for_level_4", []),
        "rows": rows,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_report(path, manifest, rows):
    summary = summarize(rows)
    lines = [
        "# Quantitative Calibration Readiness Audit v1",
        "",
        "This audit tracks what is still required before the simulator can be treated as a quantitative species-level biological model.",
        "",
        "## Summary",
        "",
        f"- estimated current level: `{summary['estimated_level']}`",
        f"- blocker: {summary['level_blocker']}",
        f"- total target curves: `{summary['total_targets']}`",
        f"- ready_for_fit: `{summary['ready_for_fit']}`",
        f"- model_reference_only: `{summary['model_reference_only']}`",
        f"- qualitative_proxy_only: `{summary['qualitative_proxy_only']}`",
        f"- missing_digitized_data: `{summary['missing_digitized_data']}`",
        f"- open P0 targets: `{summary['open_p0']}`",
        "",
        "## Required For Level 4",
        "",
    ]
    for item in manifest.get("required_for_level_4", []):
        lines.append(f"- {item}")
    lines.extend([
        "",
        "## Target Curves",
        "",
        "| Priority | Status | Target | Readiness | Current proxy | Next action |",
        "|---|---|---|---:|---|---|",
    ])
    for row in rows:
        lines.append(
            f"| `{row['priority']}` | `{row['status']}` | `{row['target_id']}` | "
            f"{row['readiness_level']:.1f} | {row['current_proxy']} | {row['next_action']} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- Level 4 requires at least one digitized biological target curve ready for fitting plus an independent validation curve.",
        "- Level 5 requires species-specific units, external validation data and uncertainty estimates.",
        "- Current qualitative and model-reference passes remain useful, but they do not replace raw biological curve fitting.",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Audit readiness for quantitative biological calibration.")
    parser.add_argument("--targets", type=Path, default=ROOT / "targets" / "quantitative_curve_targets.json")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "quantitative_readiness_audit.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "quantitative_readiness_audit.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "quantitative_readiness_audit.md")
    args = parser.parse_args()

    manifest = read_json(args.targets)
    rows = [target_row(target) for target in manifest["targets"]]
    write_csv(args.csv_output, rows)
    write_json(args.json_output, manifest, rows)
    write_report(args.report_output, manifest, rows)
    summary = summarize(rows)
    print(
        f"wrote {len(rows)} readiness rows to {args.csv_output}; "
        f"estimated_level={summary['estimated_level']} ready_for_fit={summary['ready_for_fit']}"
    )


if __name__ == "__main__":
    main()
