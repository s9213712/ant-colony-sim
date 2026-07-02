# Pushing Redirect Probability Validation

This report validates the general crowded-traffic frontal-encounter redirect rule against Dussutour et al. 2004.

- target CSV: `/home/s92137/ant_colony_sim/targets/digitized_curves/dussutour_2004_pushing_redirect_probability.csv`
- model source: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`
- source: Dussutour et al. 2004, Optimal traffic organisation in ants under crowded conditions, https://arxiv.org/abs/cond-mat/0403142

## Result

- status: `pass`
- target J: `0.571`
- target 95% CI: `[0.5139999999999999, 0.628]`
- model mean: `0.6122`
- model 95% CI: `[0.595, 0.6234]`
- total model encounters: `28800.0`
- total model encounter redirects: `17608.0`

## Checks

- `model_has_encounters`: `True`
- `model_ci_overlaps_target_ci`: `True`
- `model_mean_within_0_12_absolute_error`: `True`

## Interpretation

The general frontal-encounter redirect rule is quantitatively aligned with the Dussutour 2004 pushing probability target.

Caveat: the model uses a spatial traffic-grid proxy for frontal encounters. This validates a general body-contact redirect mechanism, not the full bridge-width transition curve.
