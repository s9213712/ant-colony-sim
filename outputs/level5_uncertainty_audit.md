# Level 5 Uncertainty Audit

This audit tracks whether the Level 4 curves have enough uncertainty information for Level 5-style quantitative claims.

## Summary

- estimated level: `4.4`
- Level 5 ready: `False`
- blocker: Holdout has SD values but lacks density-bin sample sizes, so formal holdout CI is not available.

## Checks

- `fit_curve_bootstrap_ci`: `True`
- `holdout_curve_present`: `True`
- `holdout_has_variance_values`: `True`
- `paper_condition_replicate_ci`: `True`
- `independent_pushing_redirect_holdout`: `True`
- `holdout_formal_ci_available`: `False`

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
- high-density n: `None`
- formal CI available: `False`
- note: Figure 4 reports Gaussian-fit SD values, but the density-bin sample sizes are not present in the committed target rows; formal confidence intervals are therefore not computed.

## Paper-Condition Replicate Uncertainty

- replicate status: `pass`
- condition count: `27`
- summary pass fraction: `1.0`
- core metrics with CI: `50` / `50`
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

## Interpretation

The simulator has moved beyond Level 4 by attaching bootstrap uncertainty to the fitted individual-response curve, replicate uncertainty to paper-condition probes, and an independent crowded-traffic pushing holdout. The traffic speed holdout includes reported SD values, but formal confidence intervals require density-bin sample sizes or raw tracking data from the source experiment.
