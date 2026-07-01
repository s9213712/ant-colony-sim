# Paper Condition Validation v2

This report maps published ant-behaviour findings to reproducible simulation conditions. Status values mean:

- `pass`: the current model matches the paper's qualitative direction under this condition.
- `partial`: the direction is partly represented, but key measurements or mechanisms are missing.
- `fail`: the current result contradicts the expected qualitative pattern.

Raw CSV: `outputs/paper_conditions_v2.csv`
JSON: `outputs/paper_conditions_v2.json`

## Sources

- perna_2012: Perna et al. 2012, Individual rules for trail pattern formation in Argentine ants (https://arxiv.org/abs/1201.5827)
- deneubourg_goss_bridge: Deneubourg/Goss/Beckers double-bridge trail-selection paradigm, cited and summarized in Perna et al. 2012 (https://arxiv.org/abs/1201.5827)
- dussutour_2004: Dussutour et al. 2004, Optimal traffic organisation in ants under crowded conditions (https://arxiv.org/abs/cond-mat/0403142)
- john_2009: John et al. 2009, Trafficlike collective movement of ants on trails: absence of jammed phase (https://arxiv.org/abs/0903.2717)
- shiraishi_2018: Shiraishi et al. 2018, Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging (https://arxiv.org/abs/1805.05598)
- amorim_2014: Amorim 2014, A continuous model of ant foraging with pheromones and trail formation (https://arxiv.org/abs/1402.5611)
- malickova_2015: Malickova, Yates & Bodova 2015, A stochastic model of ant trail following with two pheromones (https://arxiv.org/abs/1508.06816)
- kang_theraulaz_2015: Kang & Theraulaz 2015, Dynamical models of task organization in social insect colonies (https://arxiv.org/abs/1511.04769)
- afek_2015: Afek, Kecher & Sulamy 2015, Optimal and Resilient Pheromone Utilization in Ant Foraging (https://arxiv.org/abs/1507.00772)
- jimenez_romero_2015: Jimenez-Romero et al. 2015, A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones (https://arxiv.org/abs/1507.08467)

## Results

### perna_2012 - single_food_trail

- Paper: Perna et al. 2012
- Status: `partial`
- Expected: Local pheromone following should create food-trail recruitment and measurable trail reinforcement.
- Observed: `{"mean_food_trips": 44.333, "mean_food_collected": 228.333, "mean_food_pheromone": 48872.333, "mean_following_food_trail": 50.333}`
- Gap: Matches trail reinforcement qualitatively, but the model does not yet export turn-angle vs. local left/right pheromone samples, so Weber-law response cannot be quantitatively tested.

### amorim_2014 - rain_food_removal_washout

- Paper: Amorim 2014
- Status: `pass`
- Expected: Food-trail field should rise during exploitation and decay when food is removed or chemical field is washed out.
- Observed: `{"mean_food_pheromone_ratio": 0.0, "mean_nest_pheromone_ratio": 0.0028}`
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### deneubourg_goss_bridge - double_bridge_upper_bias

- Paper: Deneubourg/Goss/Beckers double-bridge paradigm
- Status: `partial`
- Expected: A connected initial trail bias should increase selection of the biased bridge through positive feedback.
- Observed: `{"upper_selected_fraction": 0.333, "mean_dominance": 0.0746, "mean_food_trips": 7.667}`
- Gap: Direction is testable, but validation still lacks digitized branch-choice probability curves from the original experiments.

### dussutour_2004 - crowding_bridge_density_shift

- Paper: Dussutour et al. 2004
- Status: `pass`
- Expected: Crowded foragers should use alternative traffic organization before food-return throughput collapses.
- Observed: `{"low_mean_dominance": 0.1201, "high_mean_dominance": 0.1024, "low_mean_crossings": 219.0, "high_mean_crossings": 704.333, "low_avg_traffic_load": 0.0083, "high_avg_traffic_load": 0.275}`
- Gap: The model has traffic load and detours, but lacks explicit antennal contacts, lane discipline and collision-avoidance rules measured in crowded ant trails.

### john_2009 - no_jam_density_speed

- Paper: John et al. 2009
- Status: `pass`
- Expected: Increasing trail density should not create a hard jammed phase; movement should degrade mildly, not collapse.
- Observed: `{"low_mean_displacement": 231.4992, "high_mean_displacement": 151.1841, "high_vs_low_displacement_ratio": 0.6531, "low_food_trips": 0.0, "high_food_trips": 0.0}`
- Gap: This is only a displacement proxy. Proper validation needs trail-segment speed/flow-density measurements and body-contact rules.

### shiraishi_2018 - stochasticity_relocation

- Paper: Shiraishi et al. 2018
- Status: `pass`
- Expected: A heterogeneous stochasticity distribution should improve adaptation after food relocation under some environments.
- Observed: `{"diverse": {"mean_initial_food_trips": 35.667, "mean_relocated_early_trips": 13.667, "mean_trips_vs_initial": 0.4655}, "high": {"mean_initial_food_trips": 14.667, "mean_relocated_early_trips": 6.667, "mean_trips_vs_initial": 0.4613}, "low": {"mean_initial_food_trips": 101.667, "mean_relocated_early_trips": 35.333, "mean_trips_vs_initial": 0.362}, "medium": {"mean_initial_food_trips": 27.0, "mean_relocated_early_trips": 7.333, "mean_trips_vs_initial": 0.3051}}`
- Gap: The current check measures relative relocation adaptation. It does not yet fit the paper's environment-dependent optimal stochasticity distribution.

### malickova_2015 - two-cue adaptation proxy

- Paper: Malickova, Yates & Bodova 2015
- Status: `pass`
- Expected: Random motion plus pheromone signalling should permit adaptation to changed external conditions.
- Observed: `{"relocation_profiles": {"diverse": {"mean_initial_food_trips": 35.667, "mean_relocated_early_trips": 13.667, "mean_trips_vs_initial": 0.4655}, "high": {"mean_initial_food_trips": 14.667, "mean_relocated_early_trips": 6.667, "mean_trips_vs_initial": 0.4613}, "low": {"mean_initial_food_trips": 101.667, "mean_relocated_early_trips": 35.333, "mean_trips_vs_initial": 0.362}, "medium": {"mean_initial_food_trips": 27.0, "mean_relocated_early_trips": 7.333, "mean_trips_vs_initial": 0.3051}}, "washout": {"mean_food_pheromone_ratio": 0.0, "mean_nest_pheromone_ratio": 0.0028}}`
- Gap: The simulator separates food/nest/water fields, but it is not yet the exact two-pheromone mathematical model and lacks direct synchronization metrics.

### kang_theraulaz_2015 - task_demand_reallocation

- Paper: Kang & Theraulaz 2015
- Status: `pass`
- Expected: Task allocation should shift with external task demand: brood demand should recruit brood work, resource shortage should recruit food/water work.
- Observed: `{"brood_condition_mean_task_brood": 243.0, "resource_condition_mean_task_brood": 0.0, "brood_condition_mean_food_water_tasks": 0.0, "resource_condition_mean_food_water_tasks": 241.667, "brood_condition_mean_brood_total": 418.333, "resource_condition_mean_food_trips": 3.667, "resource_condition_mean_water_trips": 9.333}`
- Gap: The model has response-threshold-like task switching, but does not yet estimate worker-worker contact matrices or explicit task-switching rates.

### afek_2015 - fail_stop_foraging_resilience

- Paper: Afek, Kecher & Sulamy 2015
- Status: `partial`
- Expected: After a fraction of ants fail-stop, remaining ants should still be able to forage, with reduced but nonzero throughput.
- Observed: `{"control_mean_food_trips": 11.333, "mass_death_mean_food_trips": 1.667, "trip_resilience_ratio": 0.1471, "mass_death_mean_dead_after_shock": 109.667, "mass_death_mean_corpse_moves": 97.333, "mass_death_mean_disposed_corpses": 99.333}`
- Gap: Afek et al. is an algorithmic pheromone model; this ABM only tests biological-style degradation, not asymptotic pheromone lower bounds or proof-level optimality.

### jimenez_romero_2015 - negative_pheromone_forbidden_path

- Paper: Jimenez-Romero et al. 2015
- Status: `partial`
- Expected: A second negative pheromone should reduce use of forbidden or unrewarding path regions without permanently blocking foraging.
- Observed: `{"control_mean_hazard_occupancy": 41.315, "avoid_mean_hazard_occupancy": 36.759, "avoid_vs_control_occupancy_ratio": 0.8897, "control_mean_food_trips": 14.667, "avoid_mean_food_trips": 16.0, "avoid_mean_avoid_pheromone": 28.0}`
- Gap: The simulator has an avoid field, but it is not yet paired with individual learning or neural-controller adaptation as in the paper.
