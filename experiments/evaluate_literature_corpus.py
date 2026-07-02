#!/usr/bin/env python3
import argparse
import csv
import json
import re
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXACT_CONDITION_BY_DOI = {
    "10.48550/arxiv.1811.00590": "ramirez_2018",
    "10.48550/arxiv.1507.08467": "jimenez_romero_2015",
    "10.48550/arxiv.1402.5611": "amorim_2014",
    "10.5540/03.2015.003.01.0323": "amorim_2014",
    "10.48550/arxiv.1508.06816": "malickova_2015",
    "10.1103/physrevlett.102.108001": "john_2009",
    "10.48550/arxiv.1507.00772": "afek_2015",
    "10.1038/nature02585": "dussutour_2004",
    "10.48550/arxiv.2202.01808": "aswale_2022",
    "10.48550/arxiv.1805.05598": "shiraishi_2018",
    "10.1371/journal.pcbi.1002592": "perna_2012",
    "10.48550/arxiv.1511.04769": "kang_theraulaz_2015",
    "10.1016/j.anbehav.2006.11.027": "jackson_chaline_2007",
    "10.1098/rsos.240764": "avanzi_2024",
    "10.1111/ecog.04064": "baudier_2019",
    "10.1007/s00265-002-0487-x": "pratt_2002",
    "10.1016/j.anbehav.2012.08.036": "pratt_2002",
}

EXACT_TITLE_RULES = [
    ("modeling tropotaxis", "ramirez_2018"),
    ("spiking neural networks and double pheromones", "jimenez_romero_2015"),
    ("continuous model of ant foraging", "amorim_2014"),
    ("stochastic model of ant trail following", "malickova_2015"),
    ("trafficlike collective movement", "john_2009"),
    ("optimal traffic organisation", "dussutour_2004"),
    ("diverse stochasticity", "shiraishi_2018"),
    ("individual rules for trail pattern", "perna_2012"),
    ("dynamical models of task organization", "kang_theraulaz_2015"),
    ("optimal and resilient pheromone", "afek_2015"),
    ("hacking the colony", "aswale_2022"),
    ("modulation of pheromone trail strength with food quality", "jackson_chaline_2007"),
    ("social organization of necrophoresis", "avanzi_2024"),
    ("plastic collective endothermy", "baudier_2019"),
    ("quorum sensing, recruitment, and collective decision-making", "pratt_2002"),
    ("house-hunters combine pheromone trails with quorum responses", "pratt_2002"),
]

ALGORITHMIC_PATTERNS = [
    "ant colony optimization",
    "ant colony algorithm",
    "robot",
    "robots",
    "scheduling",
    "vehicle",
    "traffic flow estimation",
    "traffic flow forecasting",
    "path planning",
    "course scheduling",
    "power distribution",
    "manufacturing",
    "neural network ant colony optimization",
    "model checking",
    "genetic algorithm",
    "particle swarm optimization",
]

BIOLOGICAL_MODEL_TITLE_HINTS = [
    "ant foraging",
    "ant trail",
    "ant trails",
    "ant traffic",
    "ant colonies",
    "ant colony foraging",
    "army ant",
    "pheromone trail",
]

BIOLOGICAL_HINTS = [
    "lasius",
    "linepithema",
    "eciton",
    "solenopsis",
    "temnothorax",
    "formica",
    "monomorium",
    "veromessor",
    "argentine ant",
    "fire ant",
    "army ant",
    "formicidae",
    "insectes sociaux",
    "animal behaviour",
    "journal of insect behavior",
    "journal of chemical ecology",
    "behavioural processes",
]

MAPPING_TO_EVIDENCE = {
    "existing_or_extend_trail_probe": {
        "condition": "single_food_trail",
        "paper_id": "perna_2012",
        "default_status": "partial",
        "gap": "Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.",
    },
    "existing_traffic_density_probe": {
        "condition": "crowding_bridge_density_shift + no_jam_density_speed",
        "paper_id": "dussutour_2004/john_2009",
        "default_status": "partial",
        "gap": "Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.",
    },
    "existing_task_demand_probe": {
        "condition": "task_demand_reallocation",
        "paper_id": "kang_theraulaz_2015",
        "default_status": "partial",
        "gap": "Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.",
    },
    "existing_or_extend_negative_pheromone_probe": {
        "condition": "negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution",
        "paper_id": "jimenez_romero_2015/aswale_2022",
        "default_status": "partial",
        "gap": "Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.",
    },
    "existing_or_extend_ant_mill_probe": {
        "condition": "ant_mill/death_spiral qualitative probe",
        "paper_id": "literature_alignment_probe",
        "default_status": "partial",
        "gap": "Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.",
    },
    "extend_corpse_cleanup_probe": {
        "condition": "necrophoresis_cleanup_latency",
        "paper_id": "avanzi_2024",
        "default_status": "partial",
        "gap": "Corpse cleanup is now testable, but generic corpse-management papers still need corpse-age chemistry, pathogen state and interaction-network validation.",
    },
    "extend_brood_microclimate_probe": {
        "condition": "brood_microclimate_stage_thermoregulation",
        "paper_id": "baudier_2019",
        "default_status": "partial",
        "gap": "Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.",
    },
    "needs_food_quality_resource_model": {
        "condition": "food_quality_recruitment",
        "paper_id": "jackson_chaline_2007",
        "default_status": "partial",
        "gap": "Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.",
    },
}


def normalize_doi(doi):
    text = (doi or "").strip().lower()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text)
    if text.endswith(".xml"):
        text = text[:-4]
    return text


def load_condition_status(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    by_id = {}
    for row in data["summaries"]:
        by_id[row["paper_id"]] = row
    return by_id


def is_algorithmic(work):
    title = work.get("title", "").lower()
    text = " ".join([
        work.get("title", ""),
        work.get("venue", ""),
        work.get("abstract", ""),
    ]).lower()
    if any(hint in title for hint in BIOLOGICAL_MODEL_TITLE_HINTS) and not any(
        hard in title for hard in ["robot", "optimization", "algorithm", "scheduling", "vehicle", "manufacturing", "power distribution", "subway", "course"]
    ):
        return False
    has_algo = any(pattern in text for pattern in ALGORITHMIC_PATTERNS)
    has_bio = any(pattern in text for pattern in BIOLOGICAL_HINTS)
    return has_algo and not has_bio


def exact_condition_id(work):
    doi = normalize_doi(work.get("doi", ""))
    if doi in EXACT_CONDITION_BY_DOI:
        return EXACT_CONDITION_BY_DOI[doi]
    title = work.get("title", "").lower()
    for pattern, condition_id in EXACT_TITLE_RULES:
        if pattern in title:
            return condition_id
    return None


def best_mapping(work):
    mappings = work.get("test_mapping", [])
    if isinstance(mappings, str):
        mappings = [item for item in mappings.split(";") if item]
    priority = [
        "needs_food_quality_resource_model",
        "extend_brood_microclimate_probe",
        "extend_corpse_cleanup_probe",
        "existing_or_extend_negative_pheromone_probe",
        "existing_traffic_density_probe",
        "existing_task_demand_probe",
        "existing_or_extend_ant_mill_probe",
        "existing_or_extend_trail_probe",
    ]
    for item in priority:
        if item in mappings:
            return item
    return mappings[0] if mappings else ""


def evaluate_work(index, work, condition_status):
    condition_id = exact_condition_id(work)
    algorithmic = is_algorithmic(work)
    categories = work.get("categories", [])
    if isinstance(categories, str):
        categories = [item for item in categories.split(";") if item]

    if condition_id:
        condition = condition_status.get(condition_id)
        if condition:
            status = condition["status"]
            if status == "pass":
                verdict = "aligned_qualitative"
            elif status == "partial":
                verdict = "partial_alignment"
            else:
                verdict = "not_aligned"
            return {
                "index": index,
                "title": work.get("title", ""),
                "year": work.get("year", ""),
                "doi": normalize_doi(work.get("doi", "")),
                "url": work.get("url", ""),
                "categories": ";".join(categories),
                "scope": "exact_paper_condition",
                "status": status,
                "verdict": verdict,
                "matched_condition": condition["condition"],
                "evidence_paper_id": condition_id,
                "gap": condition["gap"],
            }

    mapping = best_mapping(work)
    evidence = MAPPING_TO_EVIDENCE.get(mapping)
    if algorithmic:
        return {
            "index": index,
            "title": work.get("title", ""),
            "year": work.get("year", ""),
            "doi": normalize_doi(work.get("doi", "")),
            "url": work.get("url", ""),
            "categories": ";".join(categories),
            "scope": "algorithmic_or_robotics_analogy",
            "status": "not_biological_target",
            "verdict": "not_a_direct_biology_validation",
            "matched_condition": evidence["condition"] if evidence else "",
            "evidence_paper_id": evidence["paper_id"] if evidence else "",
            "gap": "This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.",
        }

    if evidence:
        status = evidence["default_status"]
        if status == "not_covered":
            verdict = "not_currently_testable"
        elif status == "partial":
            verdict = "covered_by_generic_proxy"
        else:
            verdict = "aligned_qualitative"
        return {
            "index": index,
            "title": work.get("title", ""),
            "year": work.get("year", ""),
            "doi": normalize_doi(work.get("doi", "")),
            "url": work.get("url", ""),
            "categories": ";".join(categories),
            "scope": "category_proxy",
            "status": status,
            "verdict": verdict,
            "matched_condition": evidence["condition"],
            "evidence_paper_id": evidence["paper_id"],
            "gap": evidence["gap"],
        }

    return {
        "index": index,
        "title": work.get("title", ""),
        "year": work.get("year", ""),
        "doi": normalize_doi(work.get("doi", "")),
        "url": work.get("url", ""),
        "categories": ";".join(categories),
        "scope": "unmapped",
        "status": "not_covered",
        "verdict": "not_currently_testable",
        "matched_condition": "",
        "evidence_paper_id": "",
        "gap": "No simulation condition has been mapped for this paper yet.",
    }


def summarize(rows):
    summary = {
        "count": len(rows),
        "status": {},
        "scope": {},
        "verdict": {},
    }
    for row in rows:
        for key in ["status", "scope", "verdict"]:
            value = row[key]
            summary[key][value] = summary[key].get(value, 0) + 1
    for key in ["status", "scope", "verdict"]:
        summary[key] = dict(sorted(summary[key].items(), key=lambda item: (-item[1], item[0])))
    return summary


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "index",
        "title",
        "year",
        "doi",
        "url",
        "categories",
        "scope",
        "status",
        "verdict",
        "matched_condition",
        "evidence_paper_id",
        "gap",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path, rows, summary, corpus_path, conditions_path, csv_path, json_path):
    lines = [
        "# 120-Paper Sequential Simulation Evaluation",
        "",
        "This file evaluates every paper in the 120-paper corpus against the simulator's current validation conditions.",
        "",
        "Important interpretation rules:",
        "",
        "- `pass` means qualitative alignment under an exact paper-condition probe, not fitted quantitative reproduction.",
        "- `partial` means a generic proxy exists, but key paper-specific measurements are missing.",
        "- `not_covered` means the simulator or validation suite lacks the condition required by that paper.",
        "- `not_biological_target` means the paper is mainly algorithmic/robotics/ACO and should not be treated as direct biological validation.",
        "",
        f"- Corpus: `{corpus_path}`",
        f"- Condition source: `{conditions_path}`",
        f"- CSV: `{csv_path}`",
        f"- JSON: `{json_path}`",
        "",
        "## Summary",
        "",
    ]
    for group in ["status", "scope", "verdict"]:
        lines.append(f"### {group}")
        lines.append("")
        for key, value in summary[group].items():
            lines.append(f"- `{key}`: {value}")
        lines.append("")

    lines.extend(["## Sequential Results", ""])
    for row in rows:
        lines.extend([
            f"### {row['index']}. {row['title']}",
            "",
            f"- Year: {row['year']}",
            f"- DOI: {row['doi'] or 'none'}",
            f"- URL: {row['url']}",
            f"- Categories: {row['categories']}",
            f"- Scope: `{row['scope']}`",
            f"- Status: `{row['status']}`",
            f"- Verdict: `{row['verdict']}`",
            f"- Matched condition: {row['matched_condition'] or 'none'}",
            f"- Evidence paper id: {row['evidence_paper_id'] or 'none'}",
            f"- Gap: {row['gap']}",
            "",
        ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Evaluate every paper in the literature corpus against current simulation validation conditions.")
    parser.add_argument("--corpus", default=str(ROOT / "outputs" / "literature_corpus_100.json"))
    parser.add_argument("--conditions", default=str(ROOT / "outputs" / "paper_conditions_v5.json"))
    parser.add_argument("--csv-output", default=str(ROOT / "outputs" / "literature_corpus_120_evaluation.csv"))
    parser.add_argument("--json-output", default=str(ROOT / "outputs" / "literature_corpus_120_evaluation.json"))
    parser.add_argument("--md-output", default=str(ROOT / "outputs" / "literature_corpus_120_evaluation.md"))
    args = parser.parse_args()

    corpus = json.loads(Path(args.corpus).read_text(encoding="utf-8"))
    condition_status = load_condition_status(args.conditions)
    rows = [
        evaluate_work(index, work, condition_status)
        for index, work in enumerate(corpus["works"], 1)
    ]
    summary = summarize(rows)

    csv_path = Path(args.csv_output)
    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    write_csv(csv_path, rows)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "corpus": args.corpus,
                "conditions": args.conditions,
                "summary": summary,
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_markdown(md_path, rows, summary, args.corpus, args.conditions, csv_path, json_path)

    print(f"Wrote {csv_path}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
