# Level 5 Uncertainty Audit

This audit tracks whether the Level 4 curves have enough uncertainty information for Level 5-style quantitative claims.

## Summary

- estimated level: `4.6`
- Level 5 ready: `False`
- blocker: External holdout synthesis passes, but not every primary holdout has formal target confidence intervals.

## Checks

- `fit_curve_bootstrap_ci`: `True`
- `holdout_curve_present`: `True`
- `traffic_three_point_curve`: `True`
- `holdout_has_variance_values`: `True`
- `paper_condition_replicate_ci`: `True`
- `independent_pushing_redirect_holdout`: `True`
- `external_holdout_synthesis`: `True`
- `formal_ci_holdout_available`: `True`
- `all_primary_holdouts_have_formal_ci`: `False`

## Fit-Curve Uncertainty

- bootstrap status: `available`
- bootstrap samples used: `2000`
- A 95% CI: `[25.644804680614893, 54.10139162862759]`
- beta 95% CI: `[0.9642773503525394, 1.0957540168460371]`
- R2 95% CI: `[0.9952695078201317, 0.999996555818152]`

## Holdout Uncertainty

- holdout status: `pass`
- low-density speed SD: `1.58`
- high-density speed SD: `0.6`
- low-density n: `None`
- medium-density speed SD: `0.95`
- medium-density n: `None`
- high-density n: `None`
- normalized speed RMSE: `0.04382437294697602`
- target normalized speed curve: `[1.0, 0.8225806451612903, 0.7483870967741935]`
- model normalized speed curve: `[1.0, 0.8234351693276615, 0.6724858663425594]`
- formal CI available: `False`
- note: Figure 4 reports Gaussian-fit SD values, but the density-bin sample sizes are not present in the committed target rows; formal confidence intervals are therefore not computed.

## Paper-Condition Replicate Uncertainty

- replicate status: `pass`
- condition count: `30`
- summary pass fraction: `0.9444`
- core metrics with CI: `62` / `62`
- minimum replicate count: `3`
- underpowered core metrics: `[]`

## Pushing Redirect Holdout

- holdout status: `pass`
- source: Dussutour et al. 2004
- target probability: `0.571`
- target 95% CI: `[0.5139999999999999, 0.628]`
- model mean redirect per encounter: `0.6121666666666666`
- model 95% CI: `[0.595, 0.6234]`
- replicates: `3`

## External Holdout Synthesis

- synthesis status: `pass`
- holdout count: `2`
- independent source count: `2`
- distinct process count: `2`
- pass count: `2`
- formal-CI holdout count: `1`
- all holdouts have formal CI: `False`
- blocker: External holdout synthesis passes; Level 5 still needs more paper-level quantitative curves across behavior classes.

## Interpretation

The simulator has moved beyond Level 4 by attaching bootstrap uncertainty to the fitted individual-response curve, replicate uncertainty to paper-condition probes, a multi-source external holdout synthesis, and an independent crowded-traffic pushing holdout with formal CI overlap. It is still not Level 5 because not every primary holdout has formal target confidence intervals and broader paper-level quantitative curves are still needed.
