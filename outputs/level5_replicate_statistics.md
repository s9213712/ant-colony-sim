# Level 5 Replicate Statistics

This report adds replicate-level uncertainty to literature-condition probes without changing simulator rules.

## Summary

- source: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`
- status: `pass`
- condition count: `28`
- summary pass fraction: `1.0`
- core metrics with bootstrap CI: `54` / `54`
- minimum replicate count required: `3`

## Core Metric CI

| Condition | Metric | n | Mean | SD | 95% CI |
|---|---|---:|---:|---:|---|
| `army_ant_mill_mortality` | `corpse_fraction` | 3 | 0.753175 | 0.009014 | [0.742857, 0.759524] |
| `army_ant_mill_mortality` | `mills` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `army_ant_mill_mortality` | `survivor_fraction` | 3 | 0.257143 | 0.014483 | [0.247619, 0.27381] |
| `crowding_high_density_bridge` | `avg_traffic_load` | 3 | 0.127333 | 0.08356 | [0.042, 0.209] |
| `crowding_high_density_bridge` | `lower_segment_flow` | 3 | 256.830652 | 54.506486 | [193.910403, 289.609349] |
| `crowding_high_density_bridge` | `total_crossings` | 3 | 752.333333 | 59.91939 | [706.0, 820.0] |
| `crowding_high_density_bridge` | `traffic_redirect_per_encounter` | 3 | 0.612167 | 0.015101 | [0.595, 0.6234] |
| `crowding_high_density_bridge` | `upper_segment_flow` | 3 | 115.387813 | 60.310261 | [73.328226, 184.486006] |
| `crowding_low_density_bridge` | `avg_traffic_load` | 3 | 0.022333 | 0.02318 | [0.007, 0.049] |
| `crowding_low_density_bridge` | `lower_segment_flow` | 3 | 81.438487 | 36.242229 | [39.60282, 103.268406] |
| `crowding_low_density_bridge` | `total_crossings` | 3 | 241.666667 | 29.143324 | [221.0, 275.0] |
| `crowding_low_density_bridge` | `upper_segment_flow` | 3 | 39.545231 | 29.545156 | [20.751354, 73.600006] |
| `double_bridge_lower_bias` | `return_branch_curve_error` | 3 | 0.235634 | 0.061251 | [0.166884, 0.284389] |
| `double_bridge_lower_bias` | `return_dominance` | 3 | 0.615833 | 0.347013 | [0.21519, 0.821782] |
| `double_bridge_lower_bias` | `seeded_return_crossings` | 3 | 91.333333 | 5.033223 | [86.0, 94.666667] |
| `double_bridge_lower_bias` | `seeded_return_fraction` | 3 | 0.807916 | 0.173506 | [0.607595, 0.910891] |
| `double_bridge_unbiased_baseline` | `return_branch_curve_error` | 3 | 0.476473 | 0.249073 | [0.189163, 0.631403] |
| `double_bridge_unbiased_baseline` | `return_dominance` | 3 | 0.584089 | 0.487802 | [0.020833, 0.868421] |
| `double_bridge_unbiased_baseline` | `seeded_return_fraction` | 3 | 0.207955 | 0.243901 | [0.065789, 0.489583] |
| `double_bridge_upper_bias` | `return_branch_curve_error` | 3 | 0.26291 | 0.063702 | [0.190895, 0.311889] |
| `double_bridge_upper_bias` | `return_dominance` | 3 | 0.342579 | 0.200375 | [0.117021, 0.5] |
| `double_bridge_upper_bias` | `seeded_return_crossings` | 3 | 54.666667 | 43.730234 | [26.0, 105.0] |
| `double_bridge_upper_bias` | `seeded_return_fraction` | 3 | 0.367718 | 0.166732 | [0.25, 0.558511] |
| `food_quality_recruitment` | `avg_collected_food_quality` | 6 | 1.246833 | 0.405391 | [0.964833, 1.524667] |
| `food_quality_recruitment` | `high_quality_food_trips` | 6 | 153.5 | 180.311675 | [34.833333, 272.675] |
| `food_quality_recruitment` | `low_quality_food_trips` | 6 | 146.5 | 180.985911 | [24.5, 268.516667] |
| `necrophoresis_cleanup_latency` | `corpse_moves` | 3 | 33.666667 | 1.527525 | [32.0, 35.0] |
| `necrophoresis_cleanup_latency` | `disposed_corpses` | 3 | 33.666667 | 1.527525 | [32.0, 35.0] |
| `necrophoresis_cleanup_latency` | `final_nest_corpses` | 3 | 2.0 | 1.0 | [1.0, 3.0] |
| `necrophoresis_cleanup_latency` | `initial_nest_corpses` | 3 | 36.0 | 0.0 | [36.0, 36.0] |
| `nest_relocation_quorum_choice` | `high_quality_site_visits` | 3 | 76.34 | 3.104497 | [74.39, 79.92] |
| `nest_relocation_quorum_choice` | `low_quality_site_visits` | 3 | 0.0 | 0.0 | [0.0, 0.0] |
| `nest_relocation_quorum_choice` | `nest_quorum_events` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `nest_relocation_quorum_choice` | `nest_relocation_completed` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `nest_relocation_quorum_choice` | `nest_relocations` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `no_jam_high_density` | `mean_displacement` | 3 | 140.176282 | 13.496741 | [131.405289, 155.718134] |
| `no_jam_high_density` | `segment_abs_forward_speed` | 3 | 3.651767 | 0.775342 | [3.1748, 4.5464] |
| `no_jam_high_density` | `segment_density` | 3 | 0.005327 | 0.002717 | [0.00222, 0.00726] |
| `no_jam_high_density` | `segment_flow` | 3 | 394.219167 | 34.727182 | [355.5779, 422.8197] |
| `no_jam_high_density` | `traffic_redirect_per_encounter` | 3 | 0.676533 | 0.009732 | [0.6653, 0.6824] |
| `no_jam_low_density` | `mean_displacement` | 3 | 204.384212 | 18.779185 | [191.961161, 225.987574] |
| `no_jam_low_density` | `segment_abs_forward_speed` | 3 | 5.430267 | 0.098101 | [5.3709, 5.5435] |
| `no_jam_low_density` | `segment_density` | 3 | 0.00094 | 0.000548 | [0.00033, 0.00139] |
| `no_jam_low_density` | `segment_flow` | 3 | 102.8966 | 25.722673 | [77.6092, 129.0335] |
| `no_jam_medium_density` | `mean_displacement` | 3 | 161.899532 | 11.247294 | [153.42563, 174.659766] |
| `no_jam_medium_density` | `segment_abs_forward_speed` | 3 | 4.471467 | 0.482961 | [4.0565, 5.0016] |
| `no_jam_medium_density` | `segment_density` | 3 | 0.002703 | 0.001097 | [0.00144, 0.00342] |
| `no_jam_medium_density` | `segment_flow` | 3 | 261.125667 | 33.826415 | [239.3308, 300.0938] |
| `rain_food_removal_washout` | `food_pheromone_ratio` | 3 | 3.1e-05 | 2.5e-05 | [1.2e-05, 5.9e-05] |
| `rain_food_removal_washout` | `nest_pheromone_ratio` | 3 | 0.003503 | 0.000313 | [0.003147, 0.003734] |
| `single_food_trail` | `food_collected` | 3 | 658.0 | 133.225373 | [513.0, 775.0] |
| `single_food_trail` | `food_trips` | 3 | 134.0 | 28.213472 | [104.0, 160.0] |
| `single_food_trail` | `gradient_alignment_ratio` | 3 | 0.968333 | 0.003055 | [0.965, 0.971] |
| `single_food_trail` | `trail_segment_mean_speed` | 3 | 8.275067 | 0.802586 | [7.4379, 9.0379] |

## Interpretation

Level 5 is not a claim of perfect biological realism. It means the simulator can report uncertainty across repeated stochastic runs, preserve paper-condition raw rows, and expose which claims remain underpowered or only qualitative.
