# Individual Pheromone Response Fit

This report fits a primary-source individual pheromone response target from Perna et al. 2012.

- Target CSV: `/home/s92137/ant_colony_sim/targets/digitized_curves/perna_2012_individual_pheromone_response.csv`
- Source: Perna et al. 2012, Individual rules for trail pattern formation in Argentine ants (Linepithema humile), https://arxiv.org/abs/1201.5827
- Data provenance: Figure 5 legend gives the six slope values; Figure 6 reports the no-evaporation power-law fit and confidence interval.

## Fit

- status: `pass`
- strict CI status: `needs_review`
- fitted A: `35.9277`
- fitted beta: `1.0338`
- log-space R2: `0.99763`
- rows: `6`

## Reference Interval

- Reported Figure 6 no-evaporation fit: A = 42.41 with 95% CI [36.90, 48.74].
- Reported beta = 1.058 with 95% CI [1.037, 1.079].
- Reported R2 = 0.9982.

## Bootstrap Uncertainty

- status: `available`
- samples used: `2000`
- A 95% bootstrap CI: `[25.6448, 54.1014]`
- beta 95% bootstrap CI: `[0.9643, 1.0958]`
- R2 95% bootstrap CI: `[0.99527, 1.00000]`

## Interpretation

Fit is usable as a rounded/bin-reconstructed Perna et al. Figure 5 response target; strict Figure 6 confidence-interval reproduction still needs raw x/y data.

Caveat: the target CSV reconstructs x-values from the Figure 5 pheromone-bin ranges using geometric midpoints and uses rounded slope values from the figure legend. This is fit-ready for submodel calibration, but exact strict-CI reproduction requires raw figure data or author-provided data.

This is a quantitative target for the individual pheromone-response submodel. It does not yet validate full colony-level food retrieval, physical pheromone half-life, or a separate holdout curve.
