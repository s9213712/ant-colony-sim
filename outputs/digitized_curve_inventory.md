# Digitized Curve Inventory

This report checks whether the repository contains primary-source numeric biological curves ready for quantitative fitting.

## Summary

- `curve_files`: 3
- `fit_ready_files`: 3
- `target_ids_with_digitized_files`: 3
- `source_leads`: 8
- `level_4_blocker`: Level 4 curve prerequisites are present; next blocker is broader external validation and uncertainty for Level 5.

## Curve Files

| Fit ready | Rows | Targets | Methods | Missing columns | File |
|---|---:|---|---|---|---|
| `yes` | 1 | traffic_pushing_redirect_probability | figure_legend_numeric | none | `/home/s92137/ant_colony_sim/targets/digitized_curves/dussutour_2004_pushing_redirect_probability.csv` |
| `yes` | 3 | traffic_velocity_density_holdout | figure_legend_numeric | none | `/home/s92137/ant_colony_sim/targets/digitized_curves/john_2009_traffic_velocity_density_holdout.csv` |
| `yes` | 6 | individual_pheromone_response_curve | figure_legend_numeric | none | `/home/s92137/ant_colony_sim/targets/digitized_curves/perna_2012_individual_pheromone_response.csv` |

## Source Leads

### john_2009_velocity_density

- Target: `traffic_velocity_density_holdout`
- Status: `ready_for_holdout_curve_committed`
- Species: Leptogenys processionalis
- Source: https://arxiv.org/abs/0903.2717
- Notes: Figure 4 reports Gaussian-fit mean velocities for low, intermediate and high density regimes. The committed CSV uses those values as an independent no-jam holdout.

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

### dussutour_2004_pushing_redirect

- Target: `traffic_pushing_redirect_probability`
- Status: `holdout_ready_curve_committed`
- Species: Lasius niger
- Source: https://arxiv.org/abs/cond-mat/0403142
- Notes: Figure 3d legend reports the pushing probability slope J = 0.571 +/- 0.057 CI95; the committed CSV uses it as a mechanism-level traffic holdout.

### john_2009

- Target: `traffic_flow_density_curve`
- Status: `candidate_for_curve_digitization`
- Species: Leptogenys processionalis
- Source: https://doi.org/10.1103/physrevlett.102.108001
- Notes: Candidate independent holdout for no-jam traffic validation after Dussutour-style fitting.
