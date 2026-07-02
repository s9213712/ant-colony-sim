# Level 5 Replicate Statistics

This report adds replicate-level uncertainty to literature-condition probes without changing simulator rules.

## Summary

- source: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`
- status: `pass`
- condition count: `27`
- summary pass fraction: `1.0`
- core metrics with bootstrap CI: `48` / `48`
- minimum replicate count required: `3`

## Core Metric CI

| Condition | Metric | n | Mean | SD | 95% CI |
|---|---|---:|---:|---:|---|
| `army_ant_mill_mortality` | `corpse_fraction` | 3 | 0.759524 | 0.0 | [0.759524, 0.759524] |
| `army_ant_mill_mortality` | `mills` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `army_ant_mill_mortality` | `survivor_fraction` | 3 | 0.247619 | 0.002381 | [0.245238, 0.25] |
| `crowding_high_density_bridge` | `avg_traffic_load` | 3 | 0.119 | 0.027495 | [0.095, 0.149] |
| `crowding_high_density_bridge` | `lower_segment_flow` | 3 | 265.304936 | 52.516104 | [204.708794, 297.60846] |
| `crowding_high_density_bridge` | `total_crossings` | 3 | 767.0 | 120.465763 | [663.0, 899.0] |
| `crowding_high_density_bridge` | `upper_segment_flow` | 3 | 119.450362 | 71.433753 | [70.245906, 201.384711] |
| `crowding_low_density_bridge` | `avg_traffic_load` | 3 | 0.027667 | 0.023245 | [0.01, 0.054] |
| `crowding_low_density_bridge` | `lower_segment_flow` | 3 | 103.350067 | 35.139764 | [64.835023, 133.664106] |
| `crowding_low_density_bridge` | `total_crossings` | 3 | 269.666667 | 14.153916 | [261.0, 286.0] |
| `crowding_low_density_bridge` | `upper_segment_flow` | 3 | 39.856904 | 29.610799 | [18.926591, 73.736606] |
| `double_bridge_lower_bias` | `return_branch_curve_error` | 3 | 0.258367 | 0.089204 | [0.155642, 0.316285] |
| `double_bridge_lower_bias` | `return_dominance` | 3 | 0.685759 | 0.33434 | [0.3, 0.891892] |
| `double_bridge_lower_bias` | `seeded_return_crossings` | 3 | 90.333333 | 17.953644 | [70.0, 101.666667] |
| `double_bridge_lower_bias` | `seeded_return_fraction` | 3 | 0.842879 | 0.16717 | [0.65, 0.945946] |
| `double_bridge_unbiased_baseline` | `return_branch_curve_error` | 3 | 0.453008 | 0.257291 | [0.155916, 0.60247] |
| `double_bridge_unbiased_baseline` | `return_dominance` | 3 | 0.556366 | 0.415359 | [0.076923, 0.807229] |
| `double_bridge_unbiased_baseline` | `seeded_return_fraction` | 3 | 0.247458 | 0.252078 | [0.096386, 0.538462] |
| `double_bridge_upper_bias` | `return_branch_curve_error` | 3 | 0.26188 | 0.081678 | [0.167599, 0.311167] |
| `double_bridge_upper_bias` | `return_dominance` | 3 | 0.382337 | 0.227077 | [0.123457, 0.547826] |
| `double_bridge_upper_bias` | `seeded_return_crossings` | 3 | 48.0 | 37.242449 | [26.0, 91.0] |
| `double_bridge_upper_bias` | `seeded_return_fraction` | 3 | 0.349984 | 0.18426 | [0.226087, 0.561728] |
| `food_quality_recruitment` | `avg_collected_food_quality` | 6 | 1.334 | 0.433199 | [1.018333, 1.633237] |
| `food_quality_recruitment` | `high_quality_food_trips` | 6 | 158.833333 | 170.785733 | [45.6625, 272.833333] |
| `food_quality_recruitment` | `low_quality_food_trips` | 6 | 144.0 | 184.323628 | [19.666667, 268.333333] |
| `necrophoresis_cleanup_latency` | `corpse_moves` | 3 | 34.0 | 2.0 | [32.0, 36.0] |
| `necrophoresis_cleanup_latency` | `disposed_corpses` | 3 | 34.333333 | 2.081666 | [32.0, 36.0] |
| `necrophoresis_cleanup_latency` | `final_nest_corpses` | 3 | 0.333333 | 0.57735 | [0.0, 1.0] |
| `necrophoresis_cleanup_latency` | `initial_nest_corpses` | 3 | 36.0 | 0.0 | [36.0, 36.0] |
| `nest_relocation_quorum_choice` | `high_quality_site_visits` | 3 | 73.973333 | 12.256661 | [66.54, 88.12] |
| `nest_relocation_quorum_choice` | `low_quality_site_visits` | 3 | 0.0 | 0.0 | [0.0, 0.0] |
| `nest_relocation_quorum_choice` | `nest_quorum_events` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `nest_relocation_quorum_choice` | `nest_relocation_completed` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `nest_relocation_quorum_choice` | `nest_relocations` | 3 | 1.0 | 0.0 | [1.0, 1.0] |
| `no_jam_high_density` | `mean_displacement` | 3 | 142.616325 | 12.979128 | [132.625697, 157.28626] |
| `no_jam_high_density` | `segment_abs_forward_speed` | 3 | 3.510933 | 0.435914 | [3.1494, 3.995] |
| `no_jam_high_density` | `segment_density` | 3 | 0.005367 | 0.002475 | [0.00258, 0.00731] |
| `no_jam_high_density` | `segment_flow` | 3 | 396.950267 | 34.451111 | [362.5602, 431.4621] |
| `no_jam_low_density` | `mean_displacement` | 3 | 212.269832 | 17.119855 | [201.227369, 231.990974] |
| `no_jam_low_density` | `segment_abs_forward_speed` | 3 | 6.826467 | 0.700212 | [6.0183, 7.2517] |
| `no_jam_low_density` | `segment_density` | 3 | 0.001077 | 0.0005 | [0.0005, 0.00139] |
| `no_jam_low_density` | `segment_flow` | 3 | 154.181033 | 10.813137 | [144.4403, 165.8162] |
| `rain_food_removal_washout` | `food_pheromone_ratio` | 3 | 6.8e-05 | 6e-05 | [1.1e-05, 0.000131] |
| `rain_food_removal_washout` | `nest_pheromone_ratio` | 3 | 0.003645 | 0.000893 | [0.002643, 0.004356] |
| `single_food_trail` | `food_collected` | 3 | 651.333333 | 77.487633 | [592.0, 739.0] |
| `single_food_trail` | `food_trips` | 3 | 131.666667 | 13.428825 | [122.0, 147.0] |
| `single_food_trail` | `gradient_alignment_ratio` | 3 | 0.971333 | 0.004041 | [0.967, 0.975] |
| `single_food_trail` | `trail_segment_mean_speed` | 3 | 8.530767 | 0.597495 | [8.1283, 9.2173] |

## Interpretation

Level 5 is not a claim of perfect biological realism. It means the simulator can report uncertainty across repeated stochastic runs, preserve paper-condition raw rows, and expose which claims remain underpowered or only qualitative.
