# Traffic Velocity-Density Holdout Validation

This report validates the traffic no-jam behavior against John et al. 2009 without fitting model parameters to that paper.

- Target CSV: `/home/s92137/ant_colony_sim/targets/digitized_curves/john_2009_traffic_velocity_density_holdout.csv`
- Model summary source: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`
- Source: John et al. 2009, Trafficlike collective movement of ants on trails: absence of a jammed phase, https://arxiv.org/abs/0903.2717

## Result

- status: `pass`
- target velocity retention high/low: `0.748`
- model velocity retention high/low: `0.672`
- normalized speed curve RMSE: `0.044`
- model low flow: `102.8966`
- model medium flow: `261.1257`
- model high flow: `394.2192`
- target low-density speed SD: `1.58`
- target medium-density speed SD: `0.95`
- target high-density speed SD: `0.6`
- formal target CI available: `False`

## Curve

| Target density | Target speed | Target normalized | Model density | Model speed | Model normalized | Model flow |
|---:|---:|---:|---:|---:|---:|---:|
| 0.1 | 6.2 | 1.000 | 0.00094 | 5.4303 | 1.000 | 102.8966 |
| 0.3 | 5.1 | 0.823 | 0.00270 | 4.4715 | 0.823 | 261.1257 |
| 0.6 | 4.64 | 0.748 | 0.00533 | 3.6518 | 0.672 | 394.2192 |

## Checks

- `target_no_jam_retention_at_least_0_70`: `True`
- `model_high_density_speed_positive`: `True`
- `model_high_density_flow_exceeds_low_density`: `True`
- `model_velocity_retention_within_holdout_margin`: `True`
- `model_three_point_curve_rmse_within_0_25`: `True`

## Interpretation

The independent John 2009 holdout supports the model's qualitative no-jam traffic behavior: speed remains positive and high-density flow does not collapse.

Figure 4 reports Gaussian-fit SD values, but the density-bin sample sizes are not present in the committed target rows; formal confidence intervals are therefore not computed.

Caveat: this is a normalized no-jam holdout, not a physical unit match. The target uses body-length/second velocities from a natural Leptogenys processionalis trail, while the simulator uses internal segment-speed units.
