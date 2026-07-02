# Quantitative Calibration Readiness Audit v1

This audit tracks what is still required before the simulator can be treated as a quantitative species-level biological model.

## Summary

- estimated current level: `4.0`
- blocker: Level 4 prerequisites are present; Level 5 needs broader external validation, uncertainty estimates and more species-unit mappings.
- total target curves: `9`
- ready_for_fit: `1`
- ready_for_holdout: `2`
- model_reference_only: `1`
- qualitative_proxy_only: `1`
- missing_digitized_data: `4`
- species-mapped ready targets: `3`
- open P0 targets: `6`

## Required For Level 4

- At least one ready_for_fit target for trail dynamics or foraging recruitment.
- At least one independent validation curve not used for parameter fitting.
- Species-specific unit mapping for time, distance and core physiological variables.

## Target Curves

| Priority | Status | Manifest | Target | Fit CSV | Unit map | Readiness | Current proxy | Next action |
|---|---|---|---|---|---|---:|---|---|
| `P0` | `ready_for_holdout` | `ready_for_holdout` | `traffic_velocity_density_holdout` | `yes` | `yes` | 4.0 | paper_conditions_v5 exports no-jam speed and flow metrics; validate_traffic_holdout.py compares normalized speed retention without fitting. | Use as independent holdout while fitting traffic/contact parameters to a separate curve. |
| `P0` | `ready_for_fit` | `ready_for_fit` | `individual_pheromone_response_curve` | `yes` | `yes` | 4.0 | paper_conditions_v5 exports per-step sensing and turning logs but previously lacked a numeric target curve. | Use the Perna 2012 response curve to calibrate shared Weber-style turn-response parameters, then validate against an independent holdout curve. |
| `P0` | `missing_digitized_data` | `missing_digitized_data` | `trail_decay_curve` | `no` | `no` | 2.5 | literature_pheromone_constraints_v1 checks qualitative persistence effects only. | Digitize trail decay or trail occupancy time series and map model day to the paper's time axis. |
| `P0` | `missing_digitized_data` | `missing_digitized_data` | `food_recruitment_strength_curve` | `no` | `no` | 2.5 | paper_conditions_v5 checks high-quality source bias qualitatively. | Digitize food-quality recruitment curves and add a concentration-to-quality mapping. |
| `P0` | `model_reference_only` | `model_reference_only` | `double_bridge_branch_choice_curve` | `no` | `no` | 3.0 | calibrate_double_bridge.py fits a literature model reference, not raw biological counts. | Replace or supplement the model reference with digitized branch-choice curves from a real double-bridge experiment. |
| `P1` | `qualitative_proxy_only` | `qualitative_proxy_only` | `traffic_flow_density_curve` | `no` | `no` | 2.8 | paper_conditions_v5 exports segment speed/flow-density metrics. | Digitize speed-density or flow-density curves and fit contact/crowding parameters. |
| `P0` | `ready_for_holdout` | `ready_for_holdout` | `traffic_pushing_redirect_probability` | `yes` | `yes` | 4.0 | paper_conditions_v5 now exports traffic_redirect_per_encounter from the shared traffic-pressure rule; validate_pushing_redirect.py compares it to the Figure 3d slope. | Keep as a mechanism holdout while fitting traffic/contact parameters to independent traffic curves. |
| `P0` | `missing_digitized_data` | `missing_digitized_data` | `brood_survival_microclimate_curve` | `no` | `no` | 2.5 | paper_conditions_v5 checks brood-stage-sensitive microclimate qualitatively. | Digitize brood survival/development curves or collect lab data for the target species. |
| `P1` | `missing_digitized_data` | `missing_digitized_data` | `founding_worker_emergence_curve` | `no` | `no` | 2.5 | actual_biology_simulation.py has founding_colony viability smoke output only. | Select a target species and add founding-stage laboratory or literature count curves. |

## Interpretation

- Level 4 requires at least one digitized biological target curve ready for fitting plus an independent validation curve.
- Level 5 requires species-specific units, external validation data and uncertainty estimates.
- Current qualitative and model-reference passes remain useful, but they do not replace raw biological curve fitting.
