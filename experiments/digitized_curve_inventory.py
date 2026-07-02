#!/usr/bin/env python3
"""Inventory digitized biological target curves for quantitative calibration."""

import argparse
import csv
import json
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_COLUMNS = [
    "source_id",
    "target_id",
    "paper_title",
    "source_url",
    "species",
    "figure_or_table",
    "x_name",
    "x_value",
    "x_unit",
    "y_name",
    "y_value",
    "y_unit",
    "digitization_method",
]
NON_FIT_METHODS = {"secondary_lead_only"}


def read_csv_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def numeric_count(rows, key):
    count = 0
    for row in rows:
        try:
            float(row.get(key, ""))
        except (TypeError, ValueError):
            continue
        count += 1
    return count


def inventory_file(path):
    rows = read_csv_rows(path)
    fieldnames = set(rows[0].keys()) if rows else set()
    missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    target_ids = sorted({row.get("target_id", "") for row in rows if row.get("target_id")})
    methods = sorted({row.get("digitization_method", "") for row in rows if row.get("digitization_method")})
    numeric_x = numeric_count(rows, "x_value")
    numeric_y = numeric_count(rows, "y_value")
    fit_ready = (
        bool(rows)
        and not missing
        and numeric_x == len(rows)
        and numeric_y == len(rows)
        and not any(method in NON_FIT_METHODS for method in methods)
    )
    return {
        "file": str(path),
        "row_count": len(rows),
        "target_ids": ";".join(target_ids),
        "digitization_methods": ";".join(methods),
        "missing_required_columns": ";".join(missing),
        "numeric_x_rows": numeric_x,
        "numeric_y_rows": numeric_y,
        "fit_ready": "yes" if fit_ready else "no",
    }


def load_leads(path):
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("leads", [])


def summarize(rows, leads):
    ready = sum(1 for row in rows if row["fit_ready"] == "yes")
    target_ids = set()
    for row in rows:
        target_ids.update(item for item in row["target_ids"].split(";") if item)
    has_fit_target = "individual_pheromone_response_curve" in target_ids
    has_holdout_target = "traffic_velocity_density_holdout" in target_ids
    if ready == 0:
        blocker = "No fit-ready digitized biological curve is available."
    elif has_fit_target and has_holdout_target:
        blocker = "Level 4 curve prerequisites are present; next blocker is broader external validation and uncertainty for Level 5."
    else:
        blocker = "Needs independent holdout validation before Level 4."
    return {
        "curve_files": len(rows),
        "fit_ready_files": ready,
        "target_ids_with_digitized_files": len(target_ids),
        "source_leads": len(leads),
        "level_4_blocker": blocker,
    }


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "file",
        "row_count",
        "target_ids",
        "digitization_methods",
        "missing_required_columns",
        "numeric_x_rows",
        "numeric_y_rows",
        "fit_ready",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path, rows, leads, summary):
    lines = [
        "# Digitized Curve Inventory",
        "",
        "This report checks whether the repository contains primary-source numeric biological curves ready for quantitative fitting.",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Curve Files", ""])
    if rows:
        lines.extend([
            "| Fit ready | Rows | Targets | Methods | Missing columns | File |",
            "|---|---:|---|---|---|---|",
        ])
        for row in rows:
            lines.append(
                f"| `{row['fit_ready']}` | {row['row_count']} | {row['target_ids'] or 'none'} | "
                f"{row['digitization_methods'] or 'none'} | {row['missing_required_columns'] or 'none'} | `{row['file']}` |"
            )
    else:
        lines.append("No digitized curve CSV files were found.")
    lines.extend(["", "## Source Leads", ""])
    for lead in leads:
        lines.extend([
            f"### {lead.get('source_id', 'unknown')}",
            "",
            f"- Target: `{lead.get('target_id', '')}`",
            f"- Status: `{lead.get('status', '')}`",
            f"- Species: {lead.get('species', '')}",
            f"- Source: {lead.get('source_url', '') or 'not located yet'}",
            f"- Notes: {lead.get('notes', '')}",
            "",
        ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Inventory digitized biological target curves.")
    parser.add_argument("--curve-dir", type=Path, default=ROOT / "targets" / "digitized_curves")
    parser.add_argument("--leads", type=Path, default=ROOT / "targets" / "digitized_curves" / "source_leads.json")
    parser.add_argument("--csv-output", type=Path, default=ROOT / "outputs" / "digitized_curve_inventory.csv")
    parser.add_argument("--json-output", type=Path, default=ROOT / "outputs" / "digitized_curve_inventory.json")
    parser.add_argument("--report-output", type=Path, default=ROOT / "outputs" / "digitized_curve_inventory.md")
    args = parser.parse_args()

    curve_files = sorted(
        path for path in args.curve_dir.glob("*.csv")
        if path.name != "curve_schema.csv"
    )
    rows = [inventory_file(path) for path in curve_files]
    leads = load_leads(args.leads)
    summary = summarize(rows, leads)
    write_csv(args.csv_output, rows)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "curve_dir": str(args.curve_dir),
                "summary": summary,
                "rows": rows,
                "source_leads": leads,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_markdown(args.report_output, rows, leads, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
