# Literature Calibration Cycle v1

This report evaluates the latest biological sensitivity output against literature-guided constraints.

## Claim Level

This is a qualitative constraint screen. It is not yet a digitized paper-curve fit or a physical pheromone half-life calibration.

## Sources Used

| Source | Used for | URL |
|---|---|---|
| perna_2012 | Local pheromone response should be a robust individual steering rule; extreme field settings should not be required to make trails work. | https://arxiv.org/abs/1201.5827 |
| malickova_2015 | Diffusion properties can alter collective movement patterns, so sensitivity to diffusion must be reported and bounded. | https://arxiv.org/abs/1508.06816 |
| amorim_2014 | Trail formation and resource removal are coupled; pheromone persistence should support efficient foraging without preventing adaptation. | https://arxiv.org/abs/1402.5611 |

## Summary

- total constraints: `6`
- pass: `6`
- fail: `0`
- missing: `0`

## Results

| Status | Priority | Constraint | Treatment | Scenario | Metric | Observed | Range | Next action |
|---|---|---|---|---|---|---:|---|---|
| `pass` | `P0` | `calibrated_persistent_pheromone_heat_food_trips_not_overcommitted` | `calibrated_persistent_pheromone` | `heat_dry_stress` | `food_trips_mean_relative_effect` | 0.151149 | `[-0.2, 0.35]` |  |
| `pass` | `P0` | `calibrated_persistent_pheromone_heat_brood_stress_not_amplified` | `calibrated_persistent_pheromone` | `heat_dry_stress` | `brood_stress_mean_relative_effect` | 0.062350 | `[-0.25, 0.15]` |  |
| `pass` | `P0` | `calibrated_persistent_pheromone_resource_food_trips_not_suppressed` | `calibrated_persistent_pheromone` | `resource_stress` | `food_trips_mean_relative_effect` | -0.026786 | `[-0.2, 0.35]` |  |
| `pass` | `P1` | `high_diffusion_heat_effect_bounded` | `high_diffusion` | `heat_dry_stress` | `food_trips_mean_relative_effect` | 0.244183 | `[-0.3, 0.3]` |  |
| `pass` | `P1` | `fast_loss_heat_peak_reduces_pheromone` | `fast_pheromone_loss` | `heat_dry_stress` | `food_pheromone_peak_mean_relative_effect` | -0.555931 | `[, -0.2]` |  |
| `pass` | `P1` | `brood_demand_heat_foraging_not_collapsed` | `brood_demand_high` | `heat_dry_stress` | `food_trips_mean_relative_effect` | -0.058150 | `[-0.25, ]` |  |

## Interpretation

- Any `fail` row remains an active calibration issue.
- When this report reaches zero `fail` and zero `missing`, the next loop should replace qualitative bands with digitized curves.
- Current constraints deliberately target pheromone persistence/sensing/diffusion because the sensitivity screen showed these parameters move foraging and brood-stress outputs.
