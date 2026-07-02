# Digitized Curve Inventory

This report checks whether the repository contains primary-source numeric biological curves ready for quantitative fitting.

## Summary

- `curve_files`: 1
- `fit_ready_files`: 1
- `target_ids_with_digitized_files`: 1
- `source_leads`: 6
- `level_4_blocker`: Needs independent holdout validation before Level 4.

## Curve Files

| Fit ready | Rows | Targets | Methods | Missing columns | File |
|---|---:|---|---|---|---|
| `yes` | 6 | individual_pheromone_response_curve | figure_legend_numeric | none | `/home/s92137/ant_colony_sim/targets/digitized_curves/perna_2012_individual_pheromone_response.csv` |

## Source Leads

### perna_2012_individual_response

- Target: `individual_pheromone_response_curve`
- Status: `fit_ready_curve_committed`
- Species: Linepithema humile
- Source: https://arxiv.org/abs/1201.5827
- Notes: Figure 5 legend gives six rounded slope values and Figure 6 reports the no-evaporation power-law fit. The committed CSV reconstructs x values from pheromone-bin geometric midpoints.

### robinson_2008_decay_rates_lead

- Target: `trail_decay_curve`
- Status: `primary_numeric_data_needed`
- Species: Monomorium pharaonis
- Source: not located yet
- Notes: Search found this as a likely primary Insectes Sociaux paper through secondary reference lists. Do not enter decay values until the primary paper, figure or table is available.

### perna_2012

- Target: `trail_decay_curve`
- Status: `candidate_for_response_curve_digitization`
- Species: Linepithema humile
- Source: https://arxiv.org/abs/1201.5827
- Notes: Useful for pheromone-response geometry and Weber-law style response, not a direct decay-rate curve unless figure data are digitized.

### jackson_chaline_2007

- Target: `food_recruitment_strength_curve`
- Status: `primary_numeric_data_needed`
- Species: Monomorium pharaonis
- Source: https://doi.org/10.1016/j.anbehav.2006.11.027
- Notes: High-priority empirical candidate for food-quality to recruitment/trail-laying calibration.

### dussutour_2004

- Target: `traffic_flow_density_curve`
- Status: `candidate_for_curve_digitization`
- Species: Lasius niger
- Source: https://doi.org/10.1038/nature02585
- Notes: Candidate for speed-density or flow-density target curves.

### john_2009

- Target: `traffic_flow_density_curve`
- Status: `candidate_for_curve_digitization`
- Species: Leptogenys processionalis
- Source: https://doi.org/10.1103/physrevlett.102.108001
- Notes: Candidate independent holdout for no-jam traffic validation after Dussutour-style fitting.
