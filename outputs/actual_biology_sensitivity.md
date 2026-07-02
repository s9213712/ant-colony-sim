# Actual Biology Sensitivity Suite v1

This report screens whether core biological outputs are robust to parameter changes under the same simulator rules.

## Run Configuration

- Seeds: `101-103`
- Scenarios: `stable_mature,resource_stress,heat_dry_stress`
- Days per replicate: `4`
- Sample interval: `0.25` days

## Treatments

| Treatment | Overrides | Purpose |
|---|---|---|
| `baseline` | `none` | Current default behavior-level parameterization. |
| `fast_pheromone_loss` | `evaporationRate=130, senseThreshold=16` | Higher evaporation and higher sensing threshold; tests trail fragility. |
| `persistent_pheromone` | `evaporationRate=55, senseThreshold=7` | Lower evaporation and lower sensing threshold; tests trail persistence and possible over-commitment. |
| `high_diffusion` | `diffusionRate=170` | Higher diffusion; tests whether broadened gradients reduce trail precision. |
| `brood_demand_high` | `broodDemand=85` | Higher brood-demand pressure; tests foraging versus brood-care tradeoff. |

## Largest Relative Effects

| Treatment | Scenario | Score | Food trips effect | Hydration effect | Brood stress effect | Peak food pheromone effect |
|---|---|---:|---:|---:|---:|---:|
| persistent_pheromone | heat_dry_stress | 0.320 | -0.221 | -0.026 | 0.175 | 0.686 |
| persistent_pheromone | resource_stress | 0.276 | -0.259 | -0.011 | 0.056 | 0.012 |
| high_diffusion | heat_dry_stress | 0.268 | 0.244 | 0.004 | -0.048 | 0.140 |
| high_diffusion | resource_stress | 0.094 | 0.071 | 0.015 | -0.065 | -0.035 |
| brood_demand_high | heat_dry_stress | 0.088 | -0.058 | 0.000 | -0.072 | -0.345 |
| persistent_pheromone | stable_mature | 0.075 | -0.069 | 0.004 | -0.029 | 0.423 |
| brood_demand_high | stable_mature | 0.056 | 0.046 | 0.007 | -0.029 | 0.042 |
| fast_pheromone_loss | resource_stress | 0.054 | -0.036 | 0.015 | 0.028 | -0.367 |

## Interpretation

- Large effects identify parameters that need literature calibration first.
- Small effects suggest the qualitative scenario is robust under this local parameter range.
- This is a sensitivity screen, not an optimizer and not proof of biological correctness.

Treatment notes:
- `brood_demand_high`: Higher brood-demand pressure; tests foraging versus brood-care tradeoff.
- `fast_pheromone_loss`: Higher evaporation and higher sensing threshold; tests trail fragility.
- `high_diffusion`: Higher diffusion; tests whether broadened gradients reduce trail precision.
- `persistent_pheromone`: Lower evaporation and lower sensing threshold; tests trail persistence and possible over-commitment.
