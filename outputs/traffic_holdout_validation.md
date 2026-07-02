# Traffic Velocity-Density Holdout Validation

This report validates the traffic no-jam behavior against John et al. 2009 without fitting model parameters to that paper.

- Target CSV: `/home/s92137/ant_colony_sim/targets/digitized_curves/john_2009_traffic_velocity_density_holdout.csv`
- Model summary source: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`
- Source: John et al. 2009, Trafficlike collective movement of ants on trails: absence of a jammed phase, https://arxiv.org/abs/0903.2717

## Result

- status: `pass`
- target velocity retention high/low: `0.748`
- model velocity retention high/low: `0.514`
- model low flow: `154.1810`
- model high flow: `396.9503`
- target low-density speed SD: `1.58`
- target high-density speed SD: `0.6`
- formal target CI available: `False`

## Checks

- `target_no_jam_retention_at_least_0_70`: `True`
- `model_high_density_speed_positive`: `True`
- `model_high_density_flow_exceeds_low_density`: `True`
- `model_velocity_retention_within_holdout_margin`: `True`

## Interpretation

The independent John 2009 holdout supports the model's qualitative no-jam traffic behavior: speed remains positive and high-density flow does not collapse.

Figure 4 reports Gaussian-fit SD values, but the density-bin sample sizes are not present in the committed target rows; formal confidence intervals are therefore not computed.

Caveat: this is a normalized no-jam holdout, not a physical unit match. The target uses body-length/second velocities from a natural Leptogenys processionalis trail, while the simulator uses internal segment-speed units.
