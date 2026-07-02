# Level 5 External Holdout Synthesis

This report separates independent empirical holdout evidence from fitted or qualitative paper-condition probes.

## Summary

- status: `pass`
- holdout count: `2`
- independent source count: `2`
- distinct process count: `2`
- pass count: `2`
- formal-CI holdout count: `1`
- all holdouts have formal CI: `False`
- blocker: External holdout synthesis passes; Level 5 still needs more paper-level quantitative curves across behavior classes.

## Checks

- `independent_holdouts_at_least_2`: `True`
- `holdout_pass_fraction_1_0`: `True`
- `formal_ci_holdouts_at_least_1`: `True`
- `distinct_processes_at_least_2`: `True`
- `source_limitations_documented`: `True`

## Holdouts

| Holdout | Source | Process | Status | Metric | Target | Model | Formal CI | Limitation |
|---|---|---|---|---|---:|---:|---|---|
| `john_2009_traffic_velocity_density` | John et al. 2009 | traffic_velocity_density | `pass` | normalized_speed_curve_rmse | 0 | 0.04382437294697602 | `False` | Figure 4 reports Gaussian-fit SD values, but the density-bin sample sizes are not present in the committed target rows; formal confidence intervals are therefore not computed. |
| `dussutour_2004_pushing_redirect` | Dussutour et al. 2004 | crowded_traffic_contact_redirect | `pass` | redirect_probability_per_encounter | 0.571 | 0.6121666666666666 | `True` | Mechanism-level body-contact holdout; not the full bridge-width flow-density transition. |

## Interpretation

This synthesis is a Level 5 evidence gate: passing it means the simulator has more than one independent empirical holdout and at least one formal-CI holdout. It does not by itself prove species-level predictive validity.
