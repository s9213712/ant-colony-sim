#!/usr/bin/env python3
import argparse
import csv
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CROSSREF_API = "https://api.crossref.org/works"


QUERIES = [
    "ant pheromone trail foraging",
    "ant trail pheromone recruitment foraging",
    "ant foraging pheromone model",
    "ant colony foraging model pheromone",
    "ant tropotaxis pheromone trail",
    "Lasius niger food recruitment pheromone",
    "Linepithema humile trail pheromone foraging",
    "Argentine ant trail pheromone foraging",
    "ant double bridge experiment pheromone",
    "ant traffic trail density flow",
    "ant trail traffic jam density",
    "ant task allocation response threshold",
    "social insect task allocation ants response threshold",
    "ant division of labor task allocation model",
    "ant necrophoresis corpse removal chemical",
    "ant corpse management necrophoresis",
    "ant brood care temperature humidity",
    "ant colony thermoregulation brood",
    "ant nest relocation quorum Temnothorax",
    "ant house hunting quorum decision",
    "army ant raid collective behavior model",
    "Eciton army ant raid trail pheromone",
    "ant mill circular trail following",
    "ant stochasticity foraging pheromone",
    "ant negative pheromone foraging",
    "ant misleading pheromone trail foraging",
    "ant colony resilience foraging pheromone",
    "ant foraging food quality recruitment",
    "ant foraging distance food quality pheromone",
    "ant social insect network task allocation",
    "ant collective decision making foraging",
    "ant pathogen social immunity corpse removal",
]


SEED_WORKS = [
    {
        "id": "perna_2012",
        "title": "Individual rules for trail pattern formation in Argentine ants (Linepithema humile)",
        "year": 2012,
        "authors": "Perna et al.",
        "venue": "PLoS Computational Biology / arXiv",
        "doi": "10.1371/journal.pcbi.1002592",
        "url": "https://arxiv.org/abs/1201.5827",
        "source_query": "seed",
    },
    {
        "id": "dussutour_2004",
        "title": "Optimal traffic organisation in ants under crowded conditions",
        "year": 2004,
        "authors": "Dussutour et al.",
        "venue": "Nature",
        "doi": "10.1038/nature02585",
        "url": "https://arxiv.org/abs/cond-mat/0403142",
        "source_query": "seed",
    },
    {
        "id": "john_2009",
        "title": "Trafficlike collective movement of ants on trails: absence of a jammed phase",
        "year": 2009,
        "authors": "John et al.",
        "venue": "Physical Review Letters / arXiv",
        "doi": "10.1103/PhysRevLett.102.108001",
        "url": "https://arxiv.org/abs/0903.2717",
        "source_query": "seed",
    },
    {
        "id": "shiraishi_2018",
        "title": "Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging",
        "year": 2018,
        "authors": "Shiraishi et al.",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1805.05598",
        "url": "https://arxiv.org/abs/1805.05598",
        "source_query": "seed",
    },
    {
        "id": "amorim_2014",
        "title": "A continuous model of ant foraging with pheromones and trail formation",
        "year": 2014,
        "authors": "Amorim",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1402.5611",
        "url": "https://arxiv.org/abs/1402.5611",
        "source_query": "seed",
    },
    {
        "id": "malickova_2015",
        "title": "A stochastic model of ant trail following with two pheromones",
        "year": 2015,
        "authors": "Malickova, Yates & Bodova",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1508.06816",
        "url": "https://arxiv.org/abs/1508.06816",
        "source_query": "seed",
    },
    {
        "id": "kang_theraulaz_2015",
        "title": "Dynamical models of task organization in social insect colonies",
        "year": 2015,
        "authors": "Kang & Theraulaz",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1511.04769",
        "url": "https://arxiv.org/abs/1511.04769",
        "source_query": "seed",
    },
    {
        "id": "afek_2015",
        "title": "Optimal and Resilient Pheromone Utilization in Ant Foraging",
        "year": 2015,
        "authors": "Afek, Kecher & Sulamy",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1507.00772",
        "url": "https://arxiv.org/abs/1507.00772",
        "source_query": "seed",
    },
    {
        "id": "jimenez_romero_2015",
        "title": "A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones",
        "year": 2015,
        "authors": "Jimenez-Romero et al.",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1507.08467",
        "url": "https://arxiv.org/abs/1507.08467",
        "source_query": "seed",
    },
    {
        "id": "aswale_2022",
        "title": "Hacking the Colony: On the Disruptive Effect of Misleading Pheromone and How to Defend Against It",
        "year": 2022,
        "authors": "Aswale et al.",
        "venue": "AAMAS / arXiv",
        "doi": "10.48550/arXiv.2202.01808",
        "url": "https://arxiv.org/abs/2202.01808",
        "source_query": "seed",
    },
    {
        "id": "ramirez_2018",
        "title": "Modeling tropotaxis in ant colonies: recruitment and trail formation",
        "year": 2018,
        "authors": "Ramirez et al.",
        "venue": "arXiv",
        "doi": "10.48550/arXiv.1811.00590",
        "url": "https://arxiv.org/abs/1811.00590",
        "source_query": "seed",
    },
]


CATEGORY_RULES = [
    ("misleading_negative_pheromone", ["misleading", "negative pheromone", "cautionary", "forbidden", "disrupt"]),
    ("pheromone_trail_foraging", ["pheromone", "trail", "foraging", "recruitment", "tropotaxis"]),
    ("traffic_collective_motion", ["traffic", "flow", "density", "jam", "crowded"]),
    ("task_allocation_division_labor", ["task allocation", "division of labor", "response threshold", "polyethism", "task organization"]),
    ("necrophoresis_social_immunity", ["necrophoresis", "corpse", "dead", "social immunity", "hygien"]),
    ("brood_nest_microclimate", ["brood", "temperature", "humidity", "thermoregulation", "microclimate"]),
    ("nest_relocation_house_hunting", ["house hunting", "nest relocation", "quorum", "emigration", "nest-site"]),
    ("army_ant_raids_mills", ["army ant", "eciton", "raid", "ant mill", "circular"]),
    ("food_quality_choice", ["food quality", "sucrose", "reward", "distance", "quality"]),
    ("networks_interactions", ["network", "interaction", "contact", "proximity"]),
    ("computational_swarm_model", ["model", "simulation", "agent", "algorithm", "swarm", "robot"]),
]


DIRECT_TESTABLE = {
    "pheromone_trail_foraging": "existing_or_extend_trail_probe",
    "traffic_collective_motion": "existing_traffic_density_probe",
    "task_allocation_division_labor": "existing_task_demand_probe",
    "necrophoresis_social_immunity": "extend_corpse_cleanup_probe",
    "brood_nest_microclimate": "extend_brood_microclimate_probe",
    "misleading_negative_pheromone": "existing_or_extend_negative_pheromone_probe",
    "food_quality_choice": "needs_food_quality_resource_model",
    "army_ant_raids_mills": "existing_or_extend_ant_mill_probe",
}


def normalize_space(text):
    return re.sub(r"\s+", " ", text or "").strip()


def strip_tags(text):
    return normalize_space(re.sub(r"<[^>]+>", " ", html.unescape(text or "")))


def first_title(item):
    titles = item.get("title") or []
    return normalize_space(titles[0] if titles else "")


def year_from_item(item):
    for key in ("published-print", "published-online", "published", "created", "issued"):
        parts = item.get(key, {}).get("date-parts")
        if parts and parts[0]:
            return parts[0][0]
    return None


def authors_from_item(item, limit=4):
    authors = []
    for author in item.get("author", [])[:limit]:
        name = " ".join(part for part in [author.get("given"), author.get("family")] if part)
        if name:
            authors.append(name)
    if len(item.get("author", [])) > limit:
        authors.append("et al.")
    return ", ".join(authors)


def venue_from_item(item):
    names = item.get("container-title") or item.get("short-container-title") or []
    return normalize_space(names[0] if names else item.get("publisher", ""))


def canonical_key(work):
    doi = normalize_doi(work.get("doi", ""))
    if doi:
        return f"doi:{doi}"
    title = re.sub(r"[^a-z0-9]+", " ", work.get("title", "").lower()).strip()
    return f"title:{title[:140]}"


def normalize_doi(doi):
    text = normalize_space(doi).lower()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text)
    if text.endswith(".xml"):
        text = text[:-4]
    return text


def ant_relevant(work):
    text = " ".join([
        work.get("title", ""),
        work.get("abstract", ""),
        work.get("venue", ""),
    ]).lower()
    patterns = [
        r"\bants?\b",
        r"\bsocial insects?\b",
        r"\bformicidae\b",
        r"\bformica\b",
        r"\blasius\b",
        r"\blinepithema\b",
        r"\btemnothorax\b",
        r"\beciton\b",
        r"\bsolenopsis\b",
        r"\bmonomorium\b",
        r"\biridomyrmex\b",
        r"\batta\b",
        r"\bmyrmica\b",
        r"\bpharaoh'?s ant\b",
        r"\bargentine ant\b",
        r"\bfire ant\b",
        r"\barmy ant\b",
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def classify(work):
    text = " ".join([
        work.get("title", ""),
        work.get("abstract", ""),
        work.get("venue", ""),
    ]).lower()
    categories = []
    for category, keywords in CATEGORY_RULES:
        if any(keyword in text for keyword in keywords):
            categories.append(category)
    if not categories:
        categories.append("background_general")
    test_mapping = []
    for category in categories:
        if category in DIRECT_TESTABLE:
            test_mapping.append(DIRECT_TESTABLE[category])
    if test_mapping:
        readiness = "direct_or_near_term"
    elif any(category in {"nest_relocation_house_hunting", "networks_interactions", "computational_swarm_model"} for category in categories):
        readiness = "needs_new_condition"
    else:
        readiness = "background_only"
    return categories, sorted(set(test_mapping)), readiness


def score_work(work):
    text = " ".join([work.get("title", ""), work.get("abstract", ""), work.get("venue", "")]).lower()
    score = 0
    for _, keywords in CATEGORY_RULES:
        for keyword in keywords:
            if keyword in text:
                score += 2 if keyword in work.get("title", "").lower() else 1
    if re.search(r"\bants?\b", text) or "formicidae" in text:
        score += 4
    if work.get("doi"):
        score += 1
    if work.get("year") and work["year"] >= 1990:
        score += 1
    return score


def crossref_query(query, rows, mailto=None, retries=2, timeout=10):
    params = {
        "query": query,
        "rows": rows,
        "select": "DOI,title,author,published-print,published-online,published,issued,created,container-title,short-container-title,publisher,type,URL,abstract,is-referenced-by-count",
        "filter": "type:journal-article,type:proceedings-article,type:posted-content",
    }
    if mailto:
        params["mailto"] = mailto
    url = f"{CROSSREF_API}?{urllib.parse.urlencode(params)}"
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": "ant-colony-sim-literature-corpus/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
            return payload.get("message", {}).get("items", [])
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            if attempt == retries:
                print(f"warning: skipped Crossref query after {retries} attempts: {query!r}: {exc}")
                return []
            time.sleep(1.5 * attempt)


def item_to_work(item, query):
    title = first_title(item)
    doi = normalize_space(item.get("DOI", ""))
    url = item.get("URL") or (f"https://doi.org/{doi}" if doi else "")
    return {
        "title": title,
        "year": year_from_item(item),
        "authors": authors_from_item(item),
        "venue": venue_from_item(item),
        "doi": normalize_doi(doi),
        "url": f"https://doi.org/{normalize_doi(doi)}" if doi else url,
        "type": item.get("type", ""),
        "cited_by_crossref": item.get("is-referenced-by-count", 0),
        "abstract": strip_tags(item.get("abstract", "")),
        "source_query": query,
    }


def collect(rows_per_query, target, mailto=None, sleep_s=0.2, retries=2, timeout=10):
    works = {}
    for seed in SEED_WORKS:
        work = dict(seed)
        work["doi"] = normalize_doi(work.get("doi", ""))
        work.setdefault("abstract", "")
        categories, mappings, readiness = classify(work)
        work["categories"] = categories
        work["test_mapping"] = mappings
        work["readiness"] = readiness
        work["relevance_score"] = score_work(work) + 10
        works[canonical_key(work)] = work

    for index, query in enumerate(QUERIES, 1):
        print(f"[{index}/{len(QUERIES)}] Crossref query: {query}")
        items = crossref_query(query, rows_per_query, mailto=mailto, retries=retries, timeout=timeout)
        for item in items:
            work = item_to_work(item, query)
            if not work["title"]:
                continue
            if not ant_relevant(work):
                continue
            categories, mappings, readiness = classify(work)
            work["categories"] = categories
            work["test_mapping"] = mappings
            work["readiness"] = readiness
            work["relevance_score"] = score_work(work)
            key = canonical_key(work)
            old = works.get(key)
            if not old or work["relevance_score"] > old.get("relevance_score", 0):
                works[key] = work
        time.sleep(sleep_s)

    ranked = sorted(
        works.values(),
        key=lambda work: (
            work.get("relevance_score", 0),
            work.get("cited_by_crossref", 0) or 0,
            work.get("year") or 0,
        ),
        reverse=True,
    )
    return ranked[:target]


def summarize(works):
    categories = {}
    readiness = {}
    for work in works:
        readiness[work["readiness"]] = readiness.get(work["readiness"], 0) + 1
        for category in work["categories"]:
            categories[category] = categories.get(category, 0) + 1
    return {
        "count": len(works),
        "readiness": dict(sorted(readiness.items())),
        "categories": dict(sorted(categories.items(), key=lambda item: (-item[1], item[0]))),
    }


def write_csv(path, works):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "index",
        "title",
        "year",
        "authors",
        "venue",
        "doi",
        "url",
        "categories",
        "readiness",
        "test_mapping",
        "source_query",
        "relevance_score",
        "cited_by_crossref",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for index, work in enumerate(works, 1):
            row = {key: work.get(key, "") for key in headers}
            row["index"] = index
            row["categories"] = ";".join(work.get("categories", []))
            row["test_mapping"] = ";".join(work.get("test_mapping", []))
            writer.writerow(row)


def write_markdown(path, works, summary, json_path, csv_path):
    lines = [
        "# Ant Colony Simulation Literature Corpus 100+",
        "",
        "This corpus is generated from Crossref queries plus the paper-condition seed set already used by the simulator validation suite.",
        "It is a triage index, not a claim that every paper is already quantitatively reproduced.",
        "",
        f"- Count: `{summary['count']}`",
        f"- JSON: `{json_path}`",
        f"- CSV: `{csv_path}`",
        "",
        "## Readiness",
        "",
    ]
    for key, count in summary["readiness"].items():
        lines.append(f"- `{key}`: {count}")
    lines.extend(["", "## Categories", ""])
    for key, count in summary["categories"].items():
        lines.append(f"- `{key}`: {count}")
    lines.extend(["", "## Papers", ""])
    for index, work in enumerate(works, 1):
        categories = ", ".join(work.get("categories", []))
        mappings = ", ".join(work.get("test_mapping", [])) or "none"
        year = work.get("year") or "n.d."
        doi = work.get("doi") or "no DOI"
        url = work.get("url") or ""
        title = work.get("title", "Untitled")
        authors = work.get("authors") or "Unknown authors"
        venue = work.get("venue") or "Unknown venue"
        lines.extend([
            f"### {index}. {title}",
            "",
            f"- Year: {year}",
            f"- Authors: {authors}",
            f"- Venue: {venue}",
            f"- DOI: {doi}",
            f"- URL: {url}",
            f"- Categories: {categories}",
            f"- Readiness: `{work.get('readiness')}`",
            f"- Candidate test mapping: {mappings}",
            f"- Source query: `{work.get('source_query')}`",
            "",
        ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build a 100+ paper corpus for ant colony simulation validation.")
    parser.add_argument("--target", type=int, default=120)
    parser.add_argument("--rows-per-query", type=int, default=30)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=8)
    parser.add_argument("--json-output", default=str(ROOT / "outputs" / "literature_corpus_100.json"))
    parser.add_argument("--csv-output", default=str(ROOT / "outputs" / "literature_corpus_100.csv"))
    parser.add_argument("--md-output", default=str(ROOT / "outputs" / "literature_corpus_100.md"))
    parser.add_argument("--mailto", default="")
    args = parser.parse_args()

    works = collect(
        args.rows_per_query,
        args.target,
        mailto=args.mailto or None,
        retries=args.retries,
        timeout=args.timeout,
    )
    summary = summarize(works)
    json_path = Path(args.json_output)
    csv_path = Path(args.csv_output)
    md_path = Path(args.md_output)

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "source": "Crossref REST API plus curated seed works",
                "queries": QUERIES,
                "summary": summary,
                "works": works,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_csv(csv_path, works)
    write_markdown(md_path, works, summary, json_path, csv_path)
    print(f"Wrote {json_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
