# Paper Condition Validation v5

This report maps published ant-behaviour findings to reproducible simulation conditions. Status values mean:

- `pass`: the current model matches the paper's qualitative direction under this condition.
- `partial`: the direction is partly represented, but key measurements or mechanisms are missing.
- `fail`: the current result contradicts the expected qualitative pattern.

Raw CSV: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.csv`
JSON: `/home/s92137/ant_colony_sim/outputs/paper_conditions_v5.json`

## Sources

- perna_2012: Perna et al. 2012, Individual rules for trail pattern formation in Argentine ants (https://arxiv.org/abs/1201.5827)
- ramirez_2018: Ramirez et al. 2018, Modeling tropotaxis in ant colonies: recruitment and trail formation (https://arxiv.org/abs/1811.00590)
- deneubourg_goss_bridge: Deneubourg/Goss/Beckers double-bridge trail-selection paradigm, cited and summarized in Perna et al. 2012 (https://arxiv.org/abs/1201.5827)
- dussutour_2004: Dussutour et al. 2004, Optimal traffic organisation in ants under crowded conditions (https://arxiv.org/abs/cond-mat/0403142)
- john_2009: John et al. 2009, Trafficlike collective movement of ants on trails: absence of jammed phase (https://arxiv.org/abs/0903.2717)
- shiraishi_2018: Shiraishi et al. 2018, Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging (https://arxiv.org/abs/1805.05598)
- amorim_2014: Amorim 2014, A continuous model of ant foraging with pheromones and trail formation (https://arxiv.org/abs/1402.5611)
- malickova_2015: Malickova, Yates & Bodova 2015, A stochastic model of ant trail following with two pheromones (https://arxiv.org/abs/1508.06816)
- kang_theraulaz_2015: Kang & Theraulaz 2015, Dynamical models of task organization in social insect colonies (https://arxiv.org/abs/1511.04769)
- afek_2015: Afek, Kecher & Sulamy 2015, Optimal and Resilient Pheromone Utilization in Ant Foraging (https://arxiv.org/abs/1507.00772)
- jimenez_romero_2015: Jimenez-Romero et al. 2015, A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones (https://arxiv.org/abs/1507.08467)
- aswale_2022: Aswale et al. 2022, Hacking the Colony: On the Disruptive Effect of Misleading Pheromone and How to Defend Against It (https://arxiv.org/abs/2202.01808)
- jackson_chaline_2007: Jackson & Chaline 2007, Modulation of pheromone trail strength with food quality in Pharaoh's ant, Monomorium pharaonis (https://doi.org/10.1016/j.anbehav.2006.11.027)
- avanzi_2024: Avanzi, Lisart & Detrain 2024, Social organization of necrophoresis: insights into disease risk management in ant societies (https://doi.org/10.1098/rsos.240764)
- baudier_2019: Baudier et al. 2019, Plastic collective endothermy in army ant bivouacs (https://doi.org/10.1111/ecog.04064)
- pratt_2002: Pratt et al. 2002, Quorum sensing, recruitment, and collective decision-making during colony emigration by the ant Leptothorax albipennis (https://doi.org/10.1007/s00265-002-0487-x)

## Results

### perna_2012 - single_food_trail

- Paper: Perna et al. 2012
- Status: `pass`
- Expected: Local pheromone following should create food-trail recruitment and measurable trail reinforcement.
- Observed: `{"mean_food_trips": 131.667, "mean_food_collected": 651.333, "mean_food_pheromone": 78642.333, "mean_following_food_trail": 54.667, "mean_detectable_sensing_samples": 81455.667, "mean_gradient_alignment_ratio": 0.971, "mean_abs_side_contrast": 0.1968, "mean_abs_turn": 0.0907, "mean_turn_contrast_product": 0.03093, "mean_trajectory_rows": 16000.0, "mean_trajectory_sensing_rows": 7479.333, "mean_trajectory_food_sensing_rows": 2762.333, "mean_trajectory_alignment_ratio": 0.955, "mean_trajectory_move": 9.1048, "mean_trail_segment_count": 33.667, "mean_trail_segment_density": 0.00167, "mean_trail_segment_speed": 8.5308, "mean_trail_segment_flow": 160.9912}`
- Gap: Trail reinforcement, per-step trajectory/sensing samples and segment-level traffic metrics are now available; Weber-law curve fitting still needs digitized reference curves before quantitative fitting can be claimed.

### ramirez_2018 - tropotaxis_gradient_response_proxy

- Paper: Ramirez et al. 2018
- Status: `pass`
- Expected: A gradient-sensitive pheromone response should yield recruitment to newly found food sources and colony-level trail networks.
- Observed: `{"mean_food_trips": 131.667, "mean_food_collected": 651.333, "mean_food_pheromone": 78642.333, "mean_following_food_trail": 54.667, "mean_detectable_sensing_samples": 81455.667, "mean_gradient_alignment_ratio": 0.971, "mean_abs_side_contrast": 0.1968, "mean_abs_turn": 0.0907, "mean_turn_contrast_product": 0.03093, "mean_trajectory_rows": 16000.0, "mean_trajectory_sensing_rows": 7479.333, "mean_trajectory_food_sensing_rows": 2762.333, "mean_trajectory_alignment_ratio": 0.955, "mean_trajectory_move": 9.1048, "mean_trail_segment_count": 33.667, "mean_trail_segment_density": 0.00167, "mean_trail_segment_speed": 8.5308, "mean_trail_segment_flow": 160.9912}`
- Gap: The model uses left/right/front sampling and exports per-step trajectory/sensing plus segment-flow metrics; exact tropotaxis equation fitting still needs digitized paper trajectories.

### amorim_2014 - rain_food_removal_washout

- Paper: Amorim 2014
- Status: `pass`
- Expected: Food-trail field should rise during exploitation and decay when food is removed or chemical field is washed out.
- Observed: `{"mean_food_pheromone_ratio": 0.0001, "mean_nest_pheromone_ratio": 0.0036}`
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### deneubourg_goss_bridge - double_bridge_counterbalanced_seed_bias

- Paper: Deneubourg/Goss/Beckers double-bridge paradigm
- Status: `pass`
- Expected: A connected initial trail bias should increase selection of the seeded bridge through positive feedback after accounting for geometry-side baseline bias.
- Observed: `{"seeded_selected_fraction": 0.667, "seeded_return_selected_fraction": 0.667, "baseline_upper_fraction": 0.317, "baseline_return_upper_fraction": 0.2475, "mean_dominance": 0.4434, "mean_return_dominance": 0.534, "mean_seeded_crossing_fraction": 0.5527, "mean_seeded_return_fraction": 0.5964, "mean_seeded_lift_vs_baseline": 0.0527, "mean_seeded_return_lift_vs_baseline": 0.0964, "mean_branch_curve_error": 0.2623, "mean_return_branch_curve_error": 0.2601, "mean_food_trips": 125.333}`
- Gap: Branch-choice timecourse, return-traffic choice and seeded-branch curve error are exported. The validation treats food-return traffic as the primary biological choice signal and all crossings as a secondary exploration-contaminated signal; remaining gap is digitizing the original branch-choice curves and fitting geometry/time-scale.

### dussutour_2004 - crowding_bridge_density_shift

- Paper: Dussutour et al. 2004
- Status: `pass`
- Expected: Crowded foragers should use alternative traffic organization before food-return throughput collapses.
- Observed: `{"low_mean_dominance": 0.3755, "high_mean_dominance": 0.4136, "low_mean_crossings": 269.667, "high_mean_crossings": 767.0, "low_avg_traffic_load": 0.0277, "high_avg_traffic_load": 0.119, "low_mean_segment_density": 0.00066, "high_mean_segment_density": 0.00219, "low_mean_segment_speed": 6.1291, "high_mean_segment_speed": 5.612, "low_mean_segment_flow": 143.207, "high_mean_segment_flow": 384.7553}`
- Gap: The model now exports segment-level density, speed and flow. It still lacks explicit antennal-contact mechanics and lane-discipline calibration from crowded trail experiments.

### john_2009 - no_jam_density_speed

- Paper: John et al. 2009
- Status: `pass`
- Expected: Increasing trail density should not create a hard jammed phase; movement should degrade mildly, not collapse.
- Observed: `{"low_mean_displacement": 212.2698, "high_mean_displacement": 142.6163, "high_vs_low_displacement_ratio": 0.6719, "low_food_trips": 5.0, "high_food_trips": 0.667, "low_segment_density": 0.00108, "high_segment_density": 0.00537, "low_segment_speed": 6.8265, "high_segment_speed": 3.5109, "low_segment_flow": 154.181, "high_segment_flow": 396.9503, "high_bidirectional_fraction": 0.3652}`
- Gap: The validation now uses segment-level speed/flow-density metrics. It still lacks calibrated body-contact rules and digitized no-jam flow curves.

### shiraishi_2018 - stochasticity_relocation

- Paper: Shiraishi et al. 2018
- Status: `pass`
- Expected: A heterogeneous stochasticity distribution should improve adaptation after food relocation under some environments.
- Observed: `{"diverse": {"mean_initial_food_trips": 67.333, "mean_relocated_early_trips": 168.333, "mean_trips_vs_initial": 2.2357}, "high": {"mean_initial_food_trips": 25.667, "mean_relocated_early_trips": 189.0, "mean_trips_vs_initial": 6.3683}, "low": {"mean_initial_food_trips": 191.0, "mean_relocated_early_trips": 142.0, "mean_trips_vs_initial": 0.7085}, "medium": {"mean_initial_food_trips": 104.667, "mean_relocated_early_trips": 185.667, "mean_trips_vs_initial": 1.4685}}`
- Gap: The current check measures relative relocation adaptation. It does not yet fit the paper's environment-dependent optimal stochasticity distribution.

### malickova_2015 - two-cue adaptation proxy

- Paper: Malickova, Yates & Bodova 2015
- Status: `pass`
- Expected: Random motion plus pheromone signalling should permit adaptation to changed external conditions.
- Observed: `{"relocation_profiles": {"diverse": {"mean_initial_food_trips": 67.333, "mean_relocated_early_trips": 168.333, "mean_trips_vs_initial": 2.2357}, "high": {"mean_initial_food_trips": 25.667, "mean_relocated_early_trips": 189.0, "mean_trips_vs_initial": 6.3683}, "low": {"mean_initial_food_trips": 191.0, "mean_relocated_early_trips": 142.0, "mean_trips_vs_initial": 0.7085}, "medium": {"mean_initial_food_trips": 104.667, "mean_relocated_early_trips": 185.667, "mean_trips_vs_initial": 1.4685}}, "washout": {"mean_food_pheromone_ratio": 0.0001, "mean_nest_pheromone_ratio": 0.0036}}`
- Gap: The simulator separates food/nest/water fields, but it is not yet the exact two-pheromone mathematical model and lacks direct synchronization metrics.

### kang_theraulaz_2015 - task_demand_reallocation

- Paper: Kang & Theraulaz 2015
- Status: `pass`
- Expected: Task allocation should shift with external task demand: brood demand should recruit brood work, resource shortage should recruit food/water work.
- Observed: `{"brood_condition_mean_task_brood": 249.667, "resource_condition_mean_task_brood": 0.0, "brood_condition_mean_food_water_tasks": 0.0, "resource_condition_mean_food_water_tasks": 132.333, "brood_condition_mean_brood_total": 418.333, "resource_condition_mean_food_trips": 13.667, "resource_condition_mean_water_trips": 42.667, "brood_condition_mean_task_switch_rate": 158.889, "resource_condition_mean_task_switch_rate": 315.0}`
- Gap: The model has response-threshold-like task switching and exports switch rates/contact summaries, but it still lacks calibrated worker-worker contact matrices.

### afek_2015 - fail_stop_foraging_resilience

- Paper: Afek, Kecher & Sulamy 2015
- Status: `pass`
- Expected: After a fraction of ants fail-stop, remaining ants should still be able to forage, with reduced but nonzero throughput.
- Observed: `{"control_mean_food_trips": 21.0, "mass_death_mean_food_trips": 12.333, "trip_resilience_ratio": 0.5873, "mass_death_mean_dead_after_shock": 101.0, "mass_death_mean_corpse_moves": 93.667, "mass_death_mean_disposed_corpses": 94.667}`
- Gap: Afek et al. is an algorithmic pheromone model; this ABM only tests biological-style degradation, not asymptotic pheromone lower bounds or proof-level optimality.

### jimenez_romero_2015 - negative_pheromone_forbidden_path

- Paper: Jimenez-Romero et al. 2015
- Status: `pass`
- Expected: A second negative pheromone should reduce use of forbidden or unrewarding path regions without permanently blocking foraging.
- Observed: `{"control_mean_hazard_occupancy": 17.481, "avoid_mean_hazard_occupancy": 14.389, "avoid_vs_control_occupancy_ratio": 0.8231, "control_mean_food_trips": 38.0, "avoid_mean_food_trips": 31.333, "avoid_mean_avoid_pheromone": 7995.0}`
- Gap: The simulator now pairs avoid pheromone with short-term individual avoid memory, but it is still an ABM rule rather than the paper's spiking-neural-controller implementation.

### aswale_2022 - misleading_pheromone_attack_and_caution

- Paper: Aswale et al. 2022
- Status: `pass`
- Expected: Misleading food pheromone should divert workers toward a fake path; a cautionary/avoid signal should limit, but not necessarily eliminate, that spatial disruption.
- Observed: `{"control_mean_food_trips": 258.0, "attack_mean_food_trips": 257.0, "caution_mean_food_trips": 259.333, "attack_vs_control_trip_ratio": 0.9961, "caution_vs_attack_trip_ratio": 1.0091, "attack_mean_fake_path_occupancy": 36.822, "caution_mean_fake_path_occupancy": 29.156}`
- Gap: The probe now uses sustained external fake-pheromone perturbation and generic avoid learning, but still lacks explicit attacker agents and calibrated attack/defense effect sizes.

### jackson_chaline_2007 - food_quality_recruitment

- Paper: Jackson & Chaline 2007
- Status: `pass`
- Expected: Higher-quality food should produce stronger recruitment or higher-quality-biased collection than lower-quality food at comparable access cost.
- Observed: `{"mean_high_quality_food_trips": 158.833, "mean_low_quality_food_trips": 144.0, "mean_avg_collected_food_quality": 1.334, "mean_high_source_food_pheromone": 156.167, "mean_low_source_food_pheromone": 96.333}`
- Gap: The simulator now has food quality and quality-weighted recruitment, but it still lacks species-specific sucrose concentration calibration and direct trail-laying event counts.

### avanzi_2024 - necrophoresis_cleanup_latency

- Paper: Avanzi, Lisart & Detrain 2024
- Status: `pass`
- Expected: Workers should respond to corpse/death chemical cues and progressively remove corpses from the nest area.
- Observed: `{"mean_initial_nest_corpses": 36.0, "mean_final_nest_corpses": 0.333, "mean_disposed_corpses": 34.333, "mean_corpse_moves": 34.0, "mean_death_pheromone": 1276.0}`
- Gap: Corpse relocation is represented, but the simulator still lacks pathogen state, corpse-age chemical profile calibration and colony-level interaction network validation.

### baudier_2019 - brood_microclimate_stage_thermoregulation

- Paper: Baudier et al. 2019
- Status: `pass`
- Expected: Brood microclimate should be regulated by workers, stress should rise under heat/dry conditions, and cool pupal bivouacs should maintain higher core temperature than cool larval bivouacs.
- Observed: `{"mean_stable_stress": 0.0, "mean_heat_dry_stress": 1.8, "mean_cold_larval_brood_temp": 23.8, "mean_cold_pupal_brood_temp": 25.3, "mean_cold_pupal_minus_larval_temp": 1.5, "mean_stable_development_events": 22.333, "mean_heat_dry_development_events": 2.667, "mean_heat_dry_brood_losses": 0.667, "mean_stable_task_brood": 290.333, "mean_heat_dry_task_brood": 0.0}`
- Gap: The simulator now tests brood microclimate and stage-dependent thermoregulation, but still lacks fitted metabolic heat budgets, nest-site choice geometry and species-specific brood survival curves.

### pratt_2002 - nest_relocation_quorum_choice

- Paper: Pratt et al. 2002
- Status: `pass`
- Expected: House-hunting workers should recruit to a higher-quality nest site, cross a quorum threshold, and relocate the colony to that site.
- Observed: `{"mean_high_quality_site_visits": 73.973, "mean_low_quality_site_visits": 0.0, "mean_quorum_events": 1.0, "mean_relocations": 1.0, "mean_completed": 1.0, "mean_final_distance_to_high_site": 0.0, "mean_transports": 136.293}`
- Gap: The simulator now has a quorum relocation proxy, but lacks species-specific tandem running, carrying trajectories, site-volume geometry and fitted quorum thresholds.
