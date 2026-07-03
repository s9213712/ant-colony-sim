# Necrophoresis Survival Holdout Validation

This report validates the generic nest-corpse social-immunity pressure against Diez, Lejeune & Detrain 2014.

- target CSV: `/home/s92137/ant_colony_sim/targets/digitized_curves/diez_2014_necrophoresis_worker_survival.csv`
- model source: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`
- source: Diez et al. 2014, Keep the nest clean: survival advantages of corpse removal in ants, https://pmc.ncbi.nlm.nih.gov/articles/PMC4126623/

## Result

- status: `partial`
- target survival delta free-restricted: `0.06599999999999995`
- target 95% CI: `[0.0035213811505620807, 0.12847861884943781]`
- model survival delta free-restricted: `0.0`
- model survival 95% CI: `[0.0, 0.0]`
- model health delta free-restricted: `7.836666666666669`
- model health 95% CI: `[4.808000000000007, 10.272999999999996]`
- model pressure delta restricted-free: `12.917`

## Checks

- `target_free_survival_exceeds_restricted`: `True`
- `model_free_survival_exceeds_restricted`: `False`
- `model_free_health_exceeds_restricted`: `True`
- `model_survival_ci_overlaps_target_ci`: `False`

## Interpretation

The model reproduces a health-cost precursor under restricted corpse removal, but not yet a full worker-survival endpoint.

Caveat: the target endpoint is a 50-day Myrmica rubra experiment, while the current model uses internal simulated days. Raw supplementary time-series fitting is still required before this becomes a strict species-level survival predictor.
