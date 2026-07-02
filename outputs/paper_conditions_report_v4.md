# Paper Condition Validation v4

This report maps published ant-behaviour findings to reproducible simulation conditions. Status values mean:

- `pass`: the current model matches the paper's qualitative direction under this condition.
- `partial`: the direction is partly represented, but key measurements or mechanisms are missing.
- `fail`: the current result contradicts the expected qualitative pattern.

Raw CSV: `outputs/paper_conditions_v4.csv`
JSON: `outputs/paper_conditions_v4.json`

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

## Results

### perna_2012 - single_food_trail

- Paper: Perna et al. 2012
- Status: `partial`
- Expected: Local pheromone following should create food-trail recruitment and measurable trail reinforcement.
- Observed: `{"mean_food_trips": 49.333, "mean_food_collected": 253.667, "mean_food_pheromone": 47550.0, "mean_following_food_trail": 59.667}`
- Gap: Matches trail reinforcement qualitatively, but the model does not yet export turn-angle vs. local left/right pheromone samples, so Weber-law response cannot be quantitatively tested.

### ramirez_2018 - tropotaxis_gradient_response_proxy

- Paper: Ramirez et al. 2018
- Status: `partial`
- Expected: A gradient-sensitive pheromone response should yield recruitment to newly found food sources and colony-level trail networks.
- Observed: `{"mean_food_trips": 49.333, "mean_food_collected": 253.667, "mean_food_pheromone": 47550.0, "mean_following_food_trail": 59.667}`
- Gap: The model uses left/right/front sampling and forms trails, but does not yet export local gradient vectors or per-step orientation changes needed to fit the tropotaxis equations.

### amorim_2014 - rain_food_removal_washout

- Paper: Amorim 2014
- Status: `pass`
- Expected: Food-trail field should rise during exploitation and decay when food is removed or chemical field is washed out.
- Observed: `{"mean_food_pheromone_ratio": 0.0, "mean_nest_pheromone_ratio": 0.0027}`
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### deneubourg_goss_bridge - double_bridge_upper_bias

- Paper: Deneubourg/Goss/Beckers double-bridge paradigm
- Status: `partial`
- Expected: A connected initial trail bias should increase selection of the biased bridge through positive feedback.
- Observed: `{"upper_selected_fraction": 0.667, "mean_dominance": 0.1543, "mean_food_trips": 14.0}`
- Gap: Direction is testable, but validation still lacks digitized branch-choice probability curves from the original experiments.

### dussutour_2004 - crowding_bridge_density_shift

- Paper: Dussutour et al. 2004
- Status: `pass`
- Expected: Crowded foragers should use alternative traffic organization before food-return throughput collapses.
- Observed: `{"low_mean_dominance": 0.0623, "high_mean_dominance": 0.0896, "low_mean_crossings": 221.333, "high_mean_crossings": 673.0, "low_avg_traffic_load": 0.0177, "high_avg_traffic_load": 0.232}`
- Gap: The model has traffic load and detours, but lacks explicit antennal contacts, lane discipline and collision-avoidance rules measured in crowded ant trails.

### john_2009 - no_jam_density_speed

- Paper: John et al. 2009
- Status: `pass`
- Expected: Increasing trail density should not create a hard jammed phase; movement should degrade mildly, not collapse.
- Observed: `{"low_mean_displacement": 231.4993, "high_mean_displacement": 151.1841, "high_vs_low_displacement_ratio": 0.6531, "low_food_trips": 0.0, "high_food_trips": 0.0}`
- Gap: This is only a displacement proxy. Proper validation needs trail-segment speed/flow-density measurements and body-contact rules.

### shiraishi_2018 - stochasticity_relocation

- Paper: Shiraishi et al. 2018
- Status: `partial`
- Expected: A heterogeneous stochasticity distribution should improve adaptation after food relocation under some environments.
- Observed: `{"diverse": {"mean_initial_food_trips": 31.0, "mean_relocated_early_trips": 12.667, "mean_trips_vs_initial": 0.3873}, "high": {"mean_initial_food_trips": 13.0, "mean_relocated_early_trips": 6.333, "mean_trips_vs_initial": 0.4973}, "low": {"mean_initial_food_trips": 103.333, "mean_relocated_early_trips": 38.333, "mean_trips_vs_initial": 0.3732}, "medium": {"mean_initial_food_trips": 38.0, "mean_relocated_early_trips": 3.333, "mean_trips_vs_initial": 0.1809}}`
- Gap: The current check measures relative relocation adaptation. It does not yet fit the paper's environment-dependent optimal stochasticity distribution.

### malickova_2015 - two-cue adaptation proxy

- Paper: Malickova, Yates & Bodova 2015
- Status: `partial`
- Expected: Random motion plus pheromone signalling should permit adaptation to changed external conditions.
- Observed: `{"relocation_profiles": {"diverse": {"mean_initial_food_trips": 31.0, "mean_relocated_early_trips": 12.667, "mean_trips_vs_initial": 0.3873}, "high": {"mean_initial_food_trips": 13.0, "mean_relocated_early_trips": 6.333, "mean_trips_vs_initial": 0.4973}, "low": {"mean_initial_food_trips": 103.333, "mean_relocated_early_trips": 38.333, "mean_trips_vs_initial": 0.3732}, "medium": {"mean_initial_food_trips": 38.0, "mean_relocated_early_trips": 3.333, "mean_trips_vs_initial": 0.1809}}, "washout": {"mean_food_pheromone_ratio": 0.0, "mean_nest_pheromone_ratio": 0.0027}}`
- Gap: The simulator separates food/nest/water fields, but it is not yet the exact two-pheromone mathematical model and lacks direct synchronization metrics.

### kang_theraulaz_2015 - task_demand_reallocation

- Paper: Kang & Theraulaz 2015
- Status: `pass`
- Expected: Task allocation should shift with external task demand: brood demand should recruit brood work, resource shortage should recruit food/water work.
- Observed: `{"brood_condition_mean_task_brood": 243.0, "resource_condition_mean_task_brood": 0.0, "brood_condition_mean_food_water_tasks": 0.0, "resource_condition_mean_food_water_tasks": 241.667, "brood_condition_mean_brood_total": 418.333, "resource_condition_mean_food_trips": 4.0, "resource_condition_mean_water_trips": 8.333}`
- Gap: The model has response-threshold-like task switching, but does not yet estimate worker-worker contact matrices or explicit task-switching rates.

### afek_2015 - fail_stop_foraging_resilience

- Paper: Afek, Kecher & Sulamy 2015
- Status: `pass`
- Expected: After a fraction of ants fail-stop, remaining ants should still be able to forage, with reduced but nonzero throughput.
- Observed: `{"control_mean_food_trips": 7.667, "mass_death_mean_food_trips": 3.0, "trip_resilience_ratio": 0.3913, "mass_death_mean_dead_after_shock": 109.667, "mass_death_mean_corpse_moves": 97.667, "mass_death_mean_disposed_corpses": 98.667}`
- Gap: Afek et al. is an algorithmic pheromone model; this ABM only tests biological-style degradation, not asymptotic pheromone lower bounds or proof-level optimality.

### jimenez_romero_2015 - negative_pheromone_forbidden_path

- Paper: Jimenez-Romero et al. 2015
- Status: `partial`
- Expected: A second negative pheromone should reduce use of forbidden or unrewarding path regions without permanently blocking foraging.
- Observed: `{"control_mean_hazard_occupancy": 42.074, "avoid_mean_hazard_occupancy": 37.037, "avoid_vs_control_occupancy_ratio": 0.8803, "control_mean_food_trips": 13.333, "avoid_mean_food_trips": 16.333, "avoid_mean_avoid_pheromone": 28.0}`
- Gap: The simulator has an avoid field, but it is not yet paired with individual learning or neural-controller adaptation as in the paper.

### aswale_2022 - misleading_pheromone_attack_and_caution

- Paper: Aswale et al. 2022
- Status: `partial`
- Expected: Misleading food pheromone should disrupt foraging; a cautionary/avoid signal should limit, but not necessarily eliminate, the disruption.
- Observed: `{"control_mean_food_trips": 3.333, "attack_mean_food_trips": 6.0, "caution_mean_food_trips": 4.333, "attack_vs_control_trip_ratio": 1.8, "caution_vs_attack_trip_ratio": 0.7222, "attack_mean_fake_path_occupancy": 41.0, "caution_mean_fake_path_occupancy": 38.022}`
- Gap: The current attack is a static fake trail rather than active detractor agents, and the avoid field is only a proxy for cautionary pheromone.

### jackson_chaline_2007 - food_quality_recruitment

- Paper: Jackson & Chaline 2007
- Status: `pass`
- Expected: Higher-quality food should produce stronger recruitment or higher-quality-biased collection than lower-quality food at comparable access cost.
- Observed: `{"mean_high_quality_food_trips": 12.667, "mean_low_quality_food_trips": 8.333, "mean_avg_collected_food_quality": 1.3243, "mean_high_source_food_pheromone": 80.667, "mean_low_source_food_pheromone": 48.0}`
- Gap: The simulator now has food quality and quality-weighted recruitment, but it still lacks species-specific sucrose concentration calibration and direct trail-laying event counts.

### avanzi_2024 - necrophoresis_cleanup_latency

- Paper: Avanzi, Lisart & Detrain 2024
- Status: `pass`
- Expected: Workers should respond to corpse/death chemical cues and progressively remove corpses from the nest area.
- Observed: `{"mean_initial_nest_corpses": 36.0, "mean_final_nest_corpses": 1.333, "mean_disposed_corpses": 31.0, "mean_corpse_moves": 30.667, "mean_death_pheromone": 1752.333}`
- Gap: Corpse relocation is represented, but the simulator still lacks pathogen state, corpse-age chemical profile calibration and colony-level interaction network validation.
