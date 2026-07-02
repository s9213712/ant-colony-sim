#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def priority(row):
    scientific_status = row.get("scientific_status", "")
    validation_tier = row.get("validation_tier", "")
    if scientific_status == "not_biological_target":
        return "P4_screened_out_non_biology"
    if row["status"] == "not_covered" and row["scope"] != "algorithmic_or_robotics_analogy":
        return "P0_missing_biology_condition"
    if scientific_status in {"model_reference_only", "exact_qualitative_only"}:
        return "P1_needs_quantitative_curve"
    if row["status"] == "partial" and row["scope"] == "exact_paper_condition":
        return "P1_exact_condition_partial"
    if validation_tier == "family_proxy" or scientific_status == "family_qualitative_proxy":
        return "P2_family_proxy_needs_paper_data"
    if row["status"] == "partial":
        return "P2_proxy_only"
    if row["status"] == "not_biological_target":
        return "P3_algorithmic_reference_only"
    return "P4_other"


def next_action(row):
    condition = row.get("matched_condition", "")
    gap = row.get("gap", "")
    if "food_quality_needed" in condition:
        return "Add resource quality/concentration and compare recruitment or trail strength across food qualities."
    if "food_quality_recruitment" in condition or "food-quality" in gap or "food quality" in gap:
        return "Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts."
    if "brood_microclimate_needed" in condition:
        return "Add brood microclimate validation for temperature/humidity stress and brood survival/development."
    if "brood_microclimate_stage_thermoregulation" in condition or "thermoregulation" in gap:
        return "Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves."
    if "corpse_cleanup" in condition:
        return "Add necrophoresis latency and corpse disposal curve validation."
    if "necrophoresis_cleanup_latency" in condition or "necrophoresis" in gap:
        return "Calibrate corpse-age chemistry, pathogen state and corpse-removal interaction networks."
    if "nest" in condition and "relocation" in condition:
        return "Add nest relocation and quorum decision condition."
    if "misleading" in condition or "negative_pheromone" in condition or "avoid" in condition:
        return "Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes."
    if "traffic" in condition or "no_jam" in condition:
        return "Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves."
    if "task" in condition:
        return "Add worker contact matrices and network-calibrated task allocation metrics."
    if "trail" in condition or "tropotaxis" in condition:
        return "Define paper-specific geometry/species parameters and fit digitized trajectory or response curves."
    if row.get("scientific_status") == "not_biological_target" or row["status"] == "not_biological_target":
        return "Keep as algorithmic inspiration only; do not use as direct biological validation target."
    if row.get("requires_followup") == "yes" and row.get("missing_quantitative_calibration") == "yes":
        return "Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules."
    return "Define a paper-specific simulation condition before claiming alignment."


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "priority",
        "index",
        "status",
        "scope",
        "verdict",
        "scientific_status",
        "validation_tier",
        "requires_followup",
        "missing_quantitative_calibration",
        "title",
        "year",
        "doi",
        "url",
        "categories",
        "matched_condition",
        "evidence_paper_id",
        "next_action",
        "gap",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path, rows, summary, source, csv_path, json_path):
    lines = [
        "# Literature Gap Backlog",
        "",
        "This backlog records every literature-corpus paper that is not fully simulated at paper-level biological calibration.",
        "",
        f"- Source evaluation: `{source}`",
        f"- CSV: `{csv_path}`",
        f"- JSON: `{json_path}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- `{key}`: {value}")
    current = None
    for row in rows:
        if row["priority"] != current:
            current = row["priority"]
            lines.extend(["", f"## {current}", ""])
        lines.extend([
            f"### {row['index']}. {row['title']}",
            "",
            f"- Status: `{row['status']}`",
            f"- Scope: `{row['scope']}`",
            f"- Scientific status: `{row.get('scientific_status', 'unknown')}`",
            f"- Validation tier: `{row.get('validation_tier', 'unknown')}`",
            f"- Year: {row['year']}",
            f"- DOI: {row['doi'] or 'none'}",
            f"- URL: {row['url']}",
            f"- Categories: {row['categories']}",
            f"- Matched condition: {row['matched_condition'] or 'none'}",
            f"- Evidence paper id: {row['evidence_paper_id'] or 'none'}",
            f"- Next action: {row['next_action']}",
            f"- Gap: {row['gap']}",
            "",
        ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate a backlog for literature papers not fully simulated yet.")
    parser.add_argument("--evaluation", default=str(ROOT / "outputs" / "literature_corpus_120_evaluation.json"))
    parser.add_argument("--csv-output", default=str(ROOT / "outputs" / "literature_gap_backlog.csv"))
    parser.add_argument("--json-output", default=str(ROOT / "outputs" / "literature_gap_backlog.json"))
    parser.add_argument("--md-output", default=str(ROOT / "outputs" / "literature_gap_backlog.md"))
    args = parser.parse_args()

    evaluation = json.loads(Path(args.evaluation).read_text(encoding="utf-8"))
    rows = []
    for row in evaluation["rows"]:
        if row.get("requires_followup") != "yes":
            continue
        item = {
            "priority": priority(row),
            "next_action": next_action(row),
            **row,
        }
        rows.append(item)
    priority_order = {
        "P0_missing_biology_condition": 0,
        "P1_needs_quantitative_curve": 1,
        "P1_exact_condition_partial": 2,
        "P2_family_proxy_needs_paper_data": 3,
        "P2_proxy_only": 4,
        "P3_algorithmic_reference_only": 5,
        "P4_screened_out_non_biology": 6,
        "P4_other": 7,
    }
    rows.sort(key=lambda row: (priority_order.get(row["priority"], 99), int(row["index"])))
    summary = {}
    for row in rows:
        summary[row["priority"]] = summary.get(row["priority"], 0) + 1
    summary["total"] = len(rows)

    csv_path = Path(args.csv_output)
    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    write_csv(csv_path, rows)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(
            {
                "source": args.evaluation,
                "summary": summary,
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_markdown(md_path, rows, summary, args.evaluation, csv_path, json_path)
    print(f"Wrote {csv_path}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
