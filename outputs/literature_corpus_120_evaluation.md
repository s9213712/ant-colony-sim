# 120-Paper Sequential Simulation Evaluation

This file evaluates every paper in the 120-paper corpus against the simulator's current validation conditions.

Important interpretation rules:

- `pass` means qualitative alignment under an exact paper-condition probe, not fitted quantitative reproduction.
- `partial` means a generic proxy exists, but key paper-specific measurements are missing.
- `not_covered` means the simulator or validation suite lacks the condition required by that paper.
- `not_biological_target` means the paper is mainly algorithmic/robotics/ACO and should not be treated as direct biological validation.

- Corpus: `outputs/literature_corpus_100.json`
- Condition source: `outputs/paper_conditions_v5.json`
- CSV: `outputs/literature_corpus_120_evaluation.csv`
- JSON: `outputs/literature_corpus_120_evaluation.json`

## Summary

### status

- `partial`: 73
- `not_biological_target`: 34
- `pass`: 13

### scope

- `category_proxy`: 69
- `algorithmic_or_robotics_analogy`: 34
- `exact_paper_condition`: 17

### verdict

- `covered_by_generic_proxy`: 69
- `not_a_direct_biology_validation`: 34
- `aligned_qualitative`: 13
- `partial_alignment`: 4

## Sequential Results

### 1. Modeling tropotaxis in ant colonies: recruitment and trail formation

- Year: 2018
- DOI: 10.48550/arxiv.1811.00590
- URL: https://arxiv.org/abs/1811.00590
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `exact_paper_condition`
- Status: `partial`
- Verdict: `partial_alignment`
- Matched condition: tropotaxis_gradient_response_proxy
- Evidence paper id: ramirez_2018
- Gap: The model uses left/right/front sampling and forms trails, but does not yet export local gradient vectors or per-step orientation changes needed to fit the tropotaxis equations.

### 2. A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones

- Year: 2015
- DOI: 10.48550/arxiv.1507.08467
- URL: https://arxiv.org/abs/1507.08467
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Scope: `exact_paper_condition`
- Status: `partial`
- Verdict: `partial_alignment`
- Matched condition: negative_pheromone_forbidden_path
- Evidence paper id: jimenez_romero_2015
- Gap: The simulator has an avoid field, but it is not yet paired with individual learning or neural-controller adaptation as in the paper.

### 3. A continuous model of ant foraging with pheromones and trail formation

- Year: 2014
- DOI: 10.48550/arxiv.1402.5611
- URL: https://arxiv.org/abs/1402.5611
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: rain_food_removal_washout
- Evidence paper id: amorim_2014
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### 4. A stochastic model of ant trail following with two pheromones

- Year: 2015
- DOI: 10.48550/arxiv.1508.06816
- URL: https://arxiv.org/abs/1508.06816
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: two-cue adaptation proxy
- Evidence paper id: malickova_2015
- Gap: The simulator separates food/nest/water fields, but it is not yet the exact two-pheromone mathematical model and lacks direct synchronization metrics.

### 5. Trafficlike collective movement of ants on trails: absence of a jammed phase

- Year: 2009
- DOI: 10.1103/physrevlett.102.108001
- URL: https://arxiv.org/abs/0903.2717
- Categories: pheromone_trail_foraging;traffic_collective_motion
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: no_jam_density_speed
- Evidence paper id: john_2009
- Gap: This is only a displacement proxy. Proper validation needs trail-segment speed/flow-density measurements and body-contact rules.

### 6. Applying Social Network Analysis to Agent-Based Models: A Case Study of Task Allocation in Swarm Robotics Inspired by Ant Foraging Behavior

- Year: 2019
- DOI: 10.1162/isal_a_00229
- URL: https://doi.org/10.1162/isal_a_00229
- Categories: pheromone_trail_foraging;task_allocation_division_labor;networks_interactions;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 7. Modeling no-jam traffic in ant trails: a pheromone-controlled approach

- Year: 2018
- DOI: 10.1088/1742-5468/aabfc7
- URL: https://doi.org/10.1088/1742-5468/aabfc7
- Categories: pheromone_trail_foraging;traffic_collective_motion;food_quality_choice;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 8. Optimal and Resilient Pheromone Utilization in Ant Foraging

- Year: 2015
- DOI: 10.48550/arxiv.1507.00772
- URL: https://arxiv.org/abs/1507.00772
- Categories: pheromone_trail_foraging
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: fail_stop_foraging_resilience
- Evidence paper id: afek_2015
- Gap: Afek et al. is an algorithmic pheromone model; this ABM only tests biological-style degradation, not asymptotic pheromone lower bounds or proof-level optimality.

### 9. Optimal traffic organisation in ants under crowded conditions

- Year: 2004
- DOI: 10.1038/nature02585
- URL: https://arxiv.org/abs/cond-mat/0403142
- Categories: traffic_collective_motion
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: crowding_bridge_density_shift
- Evidence paper id: dussutour_2004
- Gap: The model has traffic load and detours, but lacks explicit antennal contacts, lane discipline and collision-avoidance rules measured in crowded ant trails.

### 10. Phase Transitions in Ant Traffic Driven by Density-Dependent Pheromone Feedback

- Year: 2026
- DOI: 10.2139/ssrn.6619462
- URL: https://doi.org/10.2139/ssrn.6619462
- Categories: pheromone_trail_foraging;traffic_collective_motion;necrophoresis_social_immunity;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: necrophoresis_cleanup_latency
- Evidence paper id: avanzi_2024
- Gap: Corpse cleanup is now testable, but generic corpse-management papers still need corpse-age chemistry, pathogen state and interaction-network validation.

### 11. Hacking the Colony: On the Disruptive Effect of Misleading Pheromone and How to Defend Against It

- Year: 2022
- DOI: 10.48550/arxiv.2202.01808
- URL: https://arxiv.org/abs/2202.01808
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Scope: `exact_paper_condition`
- Status: `partial`
- Verdict: `partial_alignment`
- Matched condition: misleading_pheromone_attack_and_caution
- Evidence paper id: aswale_2022
- Gap: The current attack is a static fake trail rather than active detractor agents, and the avoid field is only a proxy for cautionary pheromone.

### 12. Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging

- Year: 2018
- DOI: 10.48550/arxiv.1805.05598
- URL: https://arxiv.org/abs/1805.05598
- Categories: pheromone_trail_foraging
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: stochasticity_relocation
- Evidence paper id: shiraishi_2018
- Gap: The current check measures relative relocation adaptation. It does not yet fit the paper's environment-dependent optimal stochasticity distribution.

### 13. Individual rules for trail pattern formation in Argentine ants (Linepithema humile)

- Year: 2012
- DOI: 10.1371/journal.pcbi.1002592
- URL: https://arxiv.org/abs/1201.5827
- Categories: pheromone_trail_foraging
- Scope: `exact_paper_condition`
- Status: `partial`
- Verdict: `partial_alignment`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Matches trail reinforcement qualitatively, but the model does not yet export turn-angle vs. local left/right pheromone samples, so Weber-law response cannot be quantitatively tested.

### 14. Heterogeneous multi-agent task allocation based on graph neural network ant colony optimization algorithms

- Year: 2023
- DOI: 10.20517/ir.2023.33
- URL: https://doi.org/10.20517/ir.2023.33
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 15. Small differences in learning speed for different food qualities can drive efficient collective foraging in ant colonies

- Year: 2018
- DOI: 10.1101/274209
- URL: https://doi.org/10.1101/274209
- Categories: pheromone_trail_foraging;food_quality_choice;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 16. Analysis of Cooperative Perception in Ant Traffic and Its Effects on Transportation System by Using a Congestion-Free Ant-Trail Model

- Year: 2021
- DOI: 10.3390/s21072393
- URL: https://doi.org/10.3390/s21072393
- Categories: pheromone_trail_foraging;traffic_collective_motion;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 17. A Pheromone-Based Utility Model for Collaborative Foraging

- Year: 2004
- DOI: 10.65109/aoay8418
- URL: https://doi.org/10.65109/aoay8418
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 18. A Pheromone-Based Utility Model for Collaborative Foraging

- Year: 2004
- DOI: 10.65109/ivir1553
- URL: https://doi.org/10.65109/ivir1553
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 19. Development of Task Allocation Method for Swarm Robotic Systems Using Optimal Foraging Theory and Ant Colony Labor Division Model

- Year: 2021
- DOI: 10.1299/jsmermd.2021.1p2-f03
- URL: https://doi.org/10.1299/jsmermd.2021.1p2-f03
- Categories: pheromone_trail_foraging;task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 20. Dynamical models of task organization in social insect colonies

- Year: 2015
- DOI: 10.48550/arxiv.1511.04769
- URL: https://arxiv.org/abs/1511.04769
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: The model has response-threshold-like task switching, but does not yet estimate worker-worker contact matrices or explicit task-switching rates.

### 21. Energetics of Trail Running, Load Carriage, and Emigration in the Column-Raiding Army Ant Eciton hamatum

- Year: 1988
- DOI: 10.1086/physzool.61.1.30163737
- URL: https://doi.org/10.1086/physzool.61.1.30163737
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting;army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 22. Spatiotemporal chemotactic model for ant foraging

- Year: 2014
- DOI: 10.1142/s0217984914502388
- URL: https://doi.org/10.1142/s0217984914502388
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 23. Trail traffic flow prediction by contact frequency among individual ants

- Year: 2013
- DOI: 10.1007/s11721-013-0085-8
- URL: https://doi.org/10.1007/s11721-013-0085-8
- Categories: pheromone_trail_foraging;traffic_collective_motion;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 24. Congestion-Free Ant Traffic: Jam Absorption Mechanism in Multiple Platoons

- Year: 2019
- DOI: 10.3390/app9142918
- URL: https://doi.org/10.3390/app9142918
- Categories: pheromone_trail_foraging;traffic_collective_motion;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 25. Interactions and information: Exploring task allocation in ant colonies using network analysis

- Year: 2021
- DOI: 10.1101/2021.03.29.437501
- URL: https://doi.org/10.1101/2021.03.29.437501
- Categories: pheromone_trail_foraging;traffic_collective_motion;task_allocation_division_labor;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 26. The Neuro-ethology of Collective Decision-Making in Ant Colonies: A Case Study on Formica Rufa

- Year: 2025
- DOI: 10.61877/ijmrp.v3i9.303
- URL: https://doi.org/10.61877/ijmrp.v3i9.303
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 27. Modulation of pheromone trail strength with food quality in Pharaoh's ant, Monomorium pharaonis

- Year: 2007
- DOI: 10.1016/j.anbehav.2006.11.027
- URL: https://doi.org/10.1016/j.anbehav.2006.11.027
- Categories: pheromone_trail_foraging;food_quality_choice
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: The simulator now has food quality and quality-weighted recruitment, but it still lacks species-specific sucrose concentration calibration and direct trail-laying event counts.

### 28. A cellular automata ant memory model of foraging in a swarm of robots

- Year: 2017
- DOI: 10.1016/j.apm.2017.03.021
- URL: https://doi.org/10.1016/j.apm.2017.03.021
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 29. An agent-based model to investigate the roles of attractive and repellent pheromones in ant decision making during foraging

- Year: 2008
- DOI: 10.1016/j.jtbi.2008.08.015
- URL: https://doi.org/10.1016/j.jtbi.2008.08.015
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 30. Trail Pheromone Disruption of Argentine Ant Trail Formation and Foraging

- Year: 2010
- DOI: 10.1007/s10886-009-9734-1
- URL: https://doi.org/10.1007/s10886-009-9734-1
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 31. The foraging ecology of the army ant Eciton rapax: an ergonomic enigma?

- Year: 1985
- DOI: 10.1111/j.1365-2311.1985.tb00542.x
- URL: https://doi.org/10.1111/j.1365-2311.1985.tb00542.x
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting;army_ant_raids_mills;food_quality_choice
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 32. A probabilistic cellular automata ant memory model for a swarm of foraging robots

- Year: 2016
- DOI: 10.1109/icarcv.2016.7838615
- URL: https://doi.org/10.1109/icarcv.2016.7838615
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 33. Ants (Lasius niger) deposit more pheromone close to food sources and further from the nest but do not attempt to update erroneous pheromone trails

- Year: 2024
- DOI: 10.1007/s00040-024-00995-y
- URL: https://doi.org/10.1007/s00040-024-00995-y
- Categories: pheromone_trail_foraging;food_quality_choice;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 34. Aerosol delivery of trail pheromone disrupts the foraging of the red imported fire ant, <i>Solenopsis invicta</i>

- Year: 2012
- DOI: 10.1002/ps.3349
- URL: https://doi.org/10.1002/ps.3349
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 35. Formal analysis in a cellular automata ant model using swarm intelligence in robotics foraging task

- Year: 2017
- DOI: 10.1109/smc.2017.8122876
- URL: https://doi.org/10.1109/smc.2017.8122876
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 36. Ant Colony Optimization Based Model Checking Extended by Smell-like Pheromone

- Year: 2016
- DOI: 10.4108/eai.21-4-2016.151156
- URL: https://doi.org/10.4108/eai.21-4-2016.151156
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 37. Walk this way: modeling foraging ant dynamics in multiple food source environments

- Year: 2024
- DOI: 10.1007/s00285-024-02136-2
- URL: https://doi.org/10.1007/s00285-024-02136-2
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 38. A continuous model of ant foraging with pheromones and trail formation

- Year: 2015
- DOI: 10.5540/03.2015.003.01.0323
- URL: https://doi.org/10.5540/03.2015.003.01.0323
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: rain_food_removal_washout
- Evidence paper id: amorim_2014
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### 39. Distributed Task Allocation in Network of Agents Based on Ant Colony Foraging Behavior

- Year: 2023
- DOI: 10.1145/3606305.3606324
- URL: https://doi.org/10.1145/3606305.3606324
- Categories: pheromone_trail_foraging;task_allocation_division_labor;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 40. Avoiding traffic jams: Hitchhiking behavior as a strategy to reduce ant workers’ traffic on the foraging trail

- Year: 2018
- DOI: 10.1016/j.beproc.2018.08.015
- URL: https://doi.org/10.1016/j.beproc.2018.08.015
- Categories: pheromone_trail_foraging;traffic_collective_motion
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 41. Effect of trail pheromones and weather on the moving behaviour of the army ant Eciton burchellii

- Year: 2011
- DOI: 10.1007/s00040-010-0140-z
- URL: https://doi.org/10.1007/s00040-010-0140-z
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 42. Delay-Induced Hopf Bifurcation and Entropy-Based Distributional Uncertainty in a Stochastic Time-Delay Pheromone Feedback Model of Ant Foraging Dynamics

- Year: 2026
- DOI: 10.3390/e28070751
- URL: https://doi.org/10.3390/e28070751
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 43. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Year: 2026
- DOI: 10.1007/s00040-026-01106-9
- URL: https://doi.org/10.1007/s00040-026-01106-9
- Categories: pheromone_trail_foraging;food_quality_choice
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 44. Building a polydomous colony: nest network expansion by Linepithema humile

- Year: 2026
- DOI: 10.1007/s00040-026-01081-1
- URL: https://doi.org/10.1007/s00040-026-01081-1
- Categories: pheromone_trail_foraging;brood_nest_microclimate;nest_relocation_house_hunting;food_quality_choice;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 45. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Year: 2025
- DOI: 10.21203/rs.3.rs-7630446/v1
- URL: https://doi.org/10.21203/rs.3.rs-7630446/v1
- Categories: pheromone_trail_foraging;food_quality_choice
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 46. Stop and go: exploring alternative mechanisms for task allocation in social insects - response and satisfaction thresholds trade off cost, accuracy, and speed differently

- Year: 2024
- DOI: 10.1101/2024.05.13.593812
- URL: https://doi.org/10.1101/2024.05.13.593812
- Categories: pheromone_trail_foraging;task_allocation_division_labor;brood_nest_microclimate;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 47. Walk This Way: Modeling Foraging Ant Dynamics in Multiple Food Source Environments

- Year: 2024
- DOI: 10.1101/2024.01.20.576461
- URL: https://doi.org/10.1101/2024.01.20.576461
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 48. Ant traffic flow: Raiding swarms with few rules avoid gridlock

- Year: 2002
- DOI: 10.2307/4013963
- URL: https://doi.org/10.2307/4013963
- Categories: traffic_collective_motion;army_ant_raids_mills;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 49. MODELING AND SIMULATION OF ANT COLONY'S LABOR DIVISION WITH CONSTRAINTS FOR TASK ALLOCATION OF RESILIENT SUPPLY CHAINS

- Year: 2012
- DOI: 10.1142/s0218213012400143
- URL: https://doi.org/10.1142/s0218213012400143
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 50. Chemical Releasers of Social Behavior—IV. The Hindgut as the Source of the Odor Trail Pheromone in the Neotropical Army Ant Genus Eciton1

- Year: 1964
- DOI: 10.1093/aesa/57.6.793
- URL: https://doi.org/10.1093/aesa/57.6.793
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 51. Plastic collective endothermy in a complex animal society (army ant bivouacs: <i>Eciton burchellii parvispinum</i> )

- Year: 2019
- DOI: 10.1111/ecog.04064
- URL: https://doi.org/10.1111/ecog.04064
- Categories: brood_nest_microclimate;army_ant_raids_mills
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Gap: The simulator now tests brood microclimate and stage-dependent thermoregulation, but still lacks fitted metabolic heat budgets, nest-site choice geometry and species-specific brood survival curves.

### 52. Multiple-Agent Task Allocation Algorithm Utilizing Ant Colony Optimization

- Year: 2013
- DOI: 10.4304/jnw.8.11.2599-2606
- URL: https://doi.org/10.4304/jnw.8.11.2599-2606
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 53. No evidence that recruitment pheromone modulates olfactory, visual, or spatial learning in the ant Lasius niger

- Year: 2024
- DOI: 10.1007/s00265-024-03430-1
- URL: https://doi.org/10.1007/s00265-024-03430-1
- Categories: pheromone_trail_foraging;food_quality_choice
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 54. Reduced foraging investment as an adaptation to patchy food sources: a phasic army ant simulation

- Year: 2017
- DOI: 10.1101/101600
- URL: https://doi.org/10.1101/101600
- Categories: pheromone_trail_foraging;brood_nest_microclimate;army_ant_raids_mills;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 55. Quorum sensing, recruitment, and collective decision-making during colony emigration by the ant Leptothorax albipennis

- Year: 2002
- DOI: 10.1007/s00265-002-0487-x
- URL: https://doi.org/10.1007/s00265-002-0487-x
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: nest_relocation_quorum_choice
- Evidence paper id: pratt_2002
- Gap: The simulator now has a quorum relocation proxy, but lacks species-specific tandem running, carrying trajectories, site-volume geometry and fitted quorum thresholds.

### 56. Ant-like task allocation and recruitment in cooperative robots

- Year: 2000
- DOI: 10.1038/35023164
- URL: https://doi.org/10.1038/35023164
- Categories: pheromone_trail_foraging;task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 57. From nonlinearity to optimality: pheromone trail foraging by ants

- Year: 2003
- DOI: 10.1006/anbe.2003.2224
- URL: https://doi.org/10.1006/anbe.2003.2224
- Categories: pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 58. Trail geometry gives polarity to ant foraging networks

- Year: 2004
- DOI: 10.1038/nature03105
- URL: https://doi.org/10.1038/nature03105
- Categories: pheromone_trail_foraging;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 59. The blind leading the blind in army ant raid patterns: Testing a model of self-organization (Hymenoptera: Formicidae)

- Year: 1991
- DOI: 10.1007/bf01048072
- URL: https://doi.org/10.1007/bf01048072
- Categories: army_ant_raids_mills;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 60. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Year: 1993
- DOI: 10.1007/bf02460691
- URL: https://doi.org/10.1007/bf02460691
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 61. Multi-robot Task Allocation Based on Ant Colony Algorithm

- Year: 2012
- DOI: 10.4304/jcp.7.9.2160-2167
- URL: https://doi.org/10.4304/jcp.7.9.2160-2167
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 62. Spatial and temporal variation in pheromone composition of ant foraging trails

- Year: 2007
- DOI: 10.1093/beheco/arl104
- URL: https://doi.org/10.1093/beheco/arl104
- Categories: pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 63. A connectionist type model of self-organized foraging and emergent behavior in ant swarms

- Year: 1992
- DOI: 10.1016/s0022-5193(05)80697-6
- URL: https://doi.org/10.1016/s0022-5193(05)80697-6
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 64. Pheromone Disruption of Argentine Ant Trail Integrity

- Year: 2008
- DOI: 10.1007/s10886-008-9566-4
- URL: https://doi.org/10.1007/s10886-008-9566-4
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 65. Colony size does not predict foraging distance in the ant Temnothorax rugatulus: a puzzle for standard scaling models

- Year: 2013
- DOI: 10.1007/s00040-012-0272-4
- URL: https://doi.org/10.1007/s00040-012-0272-4
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 66. Consensus decision making in the ant Myrmecina nipponica: house-hunters combine pheromone trails with quorum responses

- Year: 2012
- DOI: 10.1016/j.anbehav.2012.08.036
- URL: https://doi.org/10.1016/j.anbehav.2012.08.036
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: nest_relocation_quorum_choice
- Evidence paper id: pratt_2002
- Gap: The simulator now has a quorum relocation proxy, but lacks species-specific tandem running, carrying trajectories, site-volume geometry and fitted quorum thresholds.

### 67. Argentine Ant (Hymenoptera: Formicidae) Trail Pheromone Enhances Consumption of Liquid Sucrose Solution

- Year: 2000
- DOI: 10.1603/0022-0493-93.1.119
- URL: https://doi.org/10.1603/0022-0493-93.1.119
- Categories: pheromone_trail_foraging;food_quality_choice
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 68. Movement, Encounter Rate, and Collective Behavior in Ant Colonies

- Year: 2021
- DOI: 10.1093/aesa/saaa036
- URL: https://doi.org/10.1093/aesa/saaa036
- Categories: traffic_collective_motion;task_allocation_division_labor;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 69. Response thresholds to recruitment signals and the regulation of foraging intensity in the ant Myrmica sabuleti (Hymenoptera, Formicidae)

- Year: 2000
- DOI: 10.1016/s0376-6357(99)00077-7
- URL: https://doi.org/10.1016/s0376-6357(99)00077-7
- Categories: pheromone_trail_foraging;task_allocation_division_labor
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 70. Foraging energetics of a nectar-feeding ant: metabolic expenditure as a function of food-source profitability

- Year: 2006
- DOI: 10.1242/jeb.02478
- URL: https://doi.org/10.1242/jeb.02478
- Categories: pheromone_trail_foraging;traffic_collective_motion;food_quality_choice;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 71. Coordination of Raiding and Emigration in the Ponerine Army Ant Leptogenys distinguenda (Hymenoptera: Formicidae: Ponerinae): A Signal Analysis

- Year: 2002
- DOI: 10.1023/a:1015484917019
- URL: https://doi.org/10.1023/a:1015484917019
- Categories: nest_relocation_house_hunting;army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 72. Notes on an army ant (<i>Eciton burchelli</i>) raid on a social wasp colony (<i>Agelaia yepocapa</i>) in Costa Rica

- Year: 1990
- DOI: 10.1017/s0266467400004958
- URL: https://doi.org/10.1017/s0266467400004958
- Categories: army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 73. First identification of a trail pheromone of an army ant (Aenictus species)

- Year: 1994
- DOI: 10.1007/bf01919378
- URL: https://doi.org/10.1007/bf01919378
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 74. Effect of Trail Bifurcation Asymmetry and Pheromone Presence or Absence on Trail Choice by <i>Lasius niger</i> Ants

- Year: 2014
- DOI: 10.1111/eth.12248
- URL: https://doi.org/10.1111/eth.12248
- Categories: pheromone_trail_foraging;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 75. Evolving neural networks using ant colony optimization with pheromone trail limits

- Year: 2013
- DOI: 10.1109/ukci.2013.6651282
- URL: https://doi.org/10.1109/ukci.2013.6651282
- Categories: pheromone_trail_foraging;networks_interactions
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 76. Argentine Ant Trail Pheromone Disruption is Mediated by Trail Concentration

- Year: 2011
- DOI: 10.1007/s10886-011-0019-0
- URL: https://doi.org/10.1007/s10886-011-0019-0
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 77. Food recruitment as a component of the trunk-trail foraging behaviour of Lasius fuliginosus (Hymenoptera: Formicidae)

- Year: 1997
- DOI: 10.1016/s0376-6357(97)00773-0
- URL: https://doi.org/10.1016/s0376-6357(97)00773-0
- Categories: pheromone_trail_foraging
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 78. An Improvement in ant Algorithm Method for Optimizing a Transport Route with Regard to Traffic Flow

- Year: 2017
- DOI: 10.1016/j.proeng.2017.04.396
- URL: https://doi.org/10.1016/j.proeng.2017.04.396
- Categories: traffic_collective_motion;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 79. Elevational and geographic variation in army ant swarm raid rates

- Year: 2011
- DOI: 10.1007/s00040-010-0129-7
- URL: https://doi.org/10.1007/s00040-010-0129-7
- Categories: army_ant_raids_mills;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 80. Interactions and information: exploring task allocation in ant colonies using network analysis

- Year: 2022
- DOI: 10.1016/j.anbehav.2022.04.015
- URL: https://doi.org/10.1016/j.anbehav.2022.04.015
- Categories: task_allocation_division_labor;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 81. Decentralized communication, trail connectivity and emergent benefits of ant pheromone trail networks

- Year: 2011
- DOI: 10.1007/s12293-010-0039-2
- URL: https://doi.org/10.1007/s12293-010-0039-2
- Categories: pheromone_trail_foraging;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 82. Research on task allocation in multiple logistics robots based on an improved ant colony algorithm

- Year: 2016
- DOI: 10.1109/icrae.2016.7738780
- URL: https://doi.org/10.1109/icrae.2016.7738780
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 83. Multi-Agent Cooperation Using the Ant Algorithm with Variable Pheromone Placement

- Year: 2005
- DOI: 10.1109/cec.2005.1554831
- URL: https://doi.org/10.1109/cec.2005.1554831
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 84. Trail Pheromone Does Not Modulate Subjective Reward Evaluation in Lasius niger Ants

- Year: 2020
- DOI: 10.3389/fpsyg.2020.555576
- URL: https://doi.org/10.3389/fpsyg.2020.555576
- Categories: pheromone_trail_foraging;food_quality_choice
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 85. Optimal ant colony algorithm based multi-robot task allocation and processing sequence scheduling

- Year: 2008
- DOI: 10.1109/wcica.2008.4593859
- URL: https://doi.org/10.1109/wcica.2008.4593859
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 86. A single-pheromone model accounts for empirical patterns of ant colony foraging previously modeled using two pheromones

- Year: 2023
- DOI: 10.1016/j.cogsys.2023.02.005
- URL: https://doi.org/10.1016/j.cogsys.2023.02.005
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 87. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Year: 1993
- DOI: 10.1016/s0092-8240(05)80195-8
- URL: https://doi.org/10.1016/s0092-8240(05)80195-8
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 88. Social organization of necrophoresis: insights into disease risk management in ant societies

- Year: 2024
- DOI: 10.1098/rsos.240764
- URL: https://doi.org/10.1098/rsos.240764
- Categories: necrophoresis_social_immunity;networks_interactions
- Scope: `exact_paper_condition`
- Status: `pass`
- Verdict: `aligned_qualitative`
- Matched condition: necrophoresis_cleanup_latency
- Evidence paper id: avanzi_2024
- Gap: Corpse relocation is represented, but the simulator still lacks pathogen state, corpse-age chemical profile calibration and colony-level interaction network validation.

### 89. Improved Intelligent Method for Traffic Flow Prediction Based on Artificial Neural Networks and Ant Colony Optimization

- Year: 2012
- DOI: 10.4156/jcit.vol7.issue8.31
- URL: https://doi.org/10.4156/jcit.vol7.issue8.31
- Categories: traffic_collective_motion;networks_interactions
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 90. Research on Improvement of Ant Colony Algorithm for Multi-Robot Task Allocation

- Year: 2019
- DOI: 10.1109/itaic.2019.8785605
- URL: https://doi.org/10.1109/itaic.2019.8785605
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 91. Modeling Ant Nest Relocation at Low Active Ratio by Particle Swarm Optimization

- Year: 2019
- DOI: 10.1109/cec.2019.8789942
- URL: https://doi.org/10.1109/cec.2019.8789942
- Categories: nest_relocation_house_hunting;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: none
- Evidence paper id: none
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 92. Novel observation of a raptor, Collared Forest-falcon ( <i>Micrastur semitorquatus</i> ), depredating a fleeing snake at an army ant ( <i>Eciton burchellii parvispinum</i> ) raid front

- Year: 2018
- DOI: 10.1676/1559-4491-130.3.792
- URL: https://doi.org/10.1676/1559-4491-130.3.792
- Categories: army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 93. Induced biotic response in Amazonian ant-plants: the role of leaf damage intensity and plant-derived food rewards on ant recruitment

- Year: 2016
- DOI: 10.13102/sociobiology.v63i3.1050
- URL: https://doi.org/10.13102/sociobiology.v63i3.1050
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 94. Deterministic Model for Analyzing the Dynamics of Ant System Algorithm and Performance Amelioration through a New Pheromone Deposition Approach

- Year: 2008
- DOI: 10.1109/iciafs.2008.4783979
- URL: https://doi.org/10.1109/iciafs.2008.4783979
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 95. The emergence of a collective sensory response threshold in ant colonies

- Year: 2021
- DOI: 10.1101/2021.10.30.466564
- URL: https://doi.org/10.1101/2021.10.30.466564
- Categories: task_allocation_division_labor;brood_nest_microclimate;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 96. Optimal A* Path Planning with Ant Colony Optimization on Multi-Robot Task Allocation for Manufacturing Model

- Year: 2021
- DOI: 10.1109/iciea52957.2021.9436716
- URL: https://doi.org/10.1109/iciea52957.2021.9436716
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 97. A Novel Improved Ant Colony Algorithm for Multi-Robot Task Allocation

- Year: 2018
- DOI: 10.1109/itoec.2018.8740438
- URL: https://doi.org/10.1109/itoec.2018.8740438
- Categories: task_allocation_division_labor;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 98. Reduced foraging investment as an adaptation to patchy food sources: A phasic army ant simulation

- Year: 2017
- DOI: 10.1016/j.jtbi.2017.06.009
- URL: https://doi.org/10.1016/j.jtbi.2017.06.009
- Categories: pheromone_trail_foraging;army_ant_raids_mills;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 99. Ant Colony Algorithm in Traffic Flow Control

- Year: 2024
- DOI: 10.23939/acps2024.02.158
- URL: https://doi.org/10.23939/acps2024.02.158
- Categories: traffic_collective_motion;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 100. Graph Convolutional Network Based Ant Colony Optimization for Robot Task Allocation

- Year: 2023
- DOI: 10.1109/ssci52147.2023.10372050
- URL: https://doi.org/10.1109/ssci52147.2023.10372050
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 101. Ant Colony Optimization Algorithm for Traffic Flow Estimation

- Year: 2017
- DOI: 10.1145/3134302.3134317
- URL: https://doi.org/10.1145/3134302.3134317
- Categories: traffic_collective_motion;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 102. Traffic Flow Estimation Using Ant Colony Optimization Algorithms

- Year: 2014
- DOI: 10.13053/cys-18-1-2014-017
- URL: https://doi.org/10.13053/cys-18-1-2014-017
- Categories: traffic_collective_motion;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 103. Hybrid Algorithm Based on Ant and Genetic Algorithms for Task Allocation on a Network of Homogeneous Processors

- Year: 2014
- DOI: 10.5121/ijcnc.2014.6113
- URL: https://doi.org/10.5121/ijcnc.2014.6113
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 104. Ant System Algorithm with Negative Pheromone for Course Scheduling Problem

- Year: 2008
- DOI: 10.1109/isda.2008.154
- URL: https://doi.org/10.1109/isda.2008.154
- Categories: misleading_negative_pheromone;pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 105. Dynamics of ant activity under extreme climatic changes in 2024: effects of temperature and humidity on Formica rufa and Lasius fuliginosus behavior

- Year: 2026
- DOI: 10.55730/1300-0179.3265
- URL: https://doi.org/10.55730/1300-0179.3265
- Categories: pheromone_trail_foraging;brood_nest_microclimate
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 106. An Ensemble Ant Colony Optimization Algorithm with a Hybrid Pheromone Model for Learning Rule Lists

- Year: 2025
- DOI: 10.1145/3712256.3726427
- URL: https://doi.org/10.1145/3712256.3726427
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 107. ANTi-JAM solutions for smart roads: Ant-inspired traffic flow rules under CAVs environment

- Year: 2025
- DOI: 10.1016/j.trip.2025.101331
- URL: https://doi.org/10.1016/j.trip.2025.101331
- Categories: traffic_collective_motion
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 108. Pheromone representation in the ant antennal lobe changes with age

- Year: 2024
- DOI: 10.1101/2024.02.13.580193
- URL: https://doi.org/10.1101/2024.02.13.580193
- Categories: pheromone_trail_foraging;task_allocation_division_labor;army_ant_raids_mills
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Gap: Task-demand switching is covered, but network/contact matrices and task-switching rates are not yet exported.

### 109. Anti-Jam Solutions for Smart Roads: Ant-Inspired Traffic Flow Rules Under Cooperative Automated Vehicles Environment

- Year: 2024
- DOI: 10.2139/ssrn.4701534
- URL: https://doi.org/10.2139/ssrn.4701534
- Categories: traffic_collective_motion
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 110. Research on Improved Ant Colony Path Planning Algorithm for Updating Pheromone of Subway Inspection Mobile Robot

- Year: 2023
- DOI: 10.2139/ssrn.4623370
- URL: https://doi.org/10.2139/ssrn.4623370
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 111. Optimization Design of Expressway Traffic Flow Guidance System Based on GIS and Improved Ant Colony Optimization Algorithms

- Year: 2023
- DOI: 10.1109/ictei60496.2023.00104
- URL: https://doi.org/10.1109/ictei60496.2023.00104
- Categories: traffic_collective_motion;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 112. Role of the pheromone for orientation in the group foraging ant, Veromessor pergandei

- Year: 2020
- DOI: 10.31219/osf.io/w2rn4
- URL: https://doi.org/10.31219/osf.io/w2rn4
- Categories: pheromone_trail_foraging;networks_interactions
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 113. Modeling Fast and Robust Ant Nest Relocation using Particle Swarm Optimization

- Year: 2019
- DOI: 10.1162/isal_a_00231
- URL: https://doi.org/10.1162/isal_a_00231
- Categories: nest_relocation_house_hunting;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: none
- Evidence paper id: none
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 114. Optimal construction of army ant living bridges

- Year: 2017
- DOI: 10.1101/116780
- URL: https://doi.org/10.1101/116780
- Categories: pheromone_trail_foraging;army_ant_raids_mills;networks_interactions;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 115. Fault Pheromone Trail Evaporation of Power Distribution Networks using Ant Colony Optimization

- Year: 2014
- DOI: 10.14257/ijhit.2014.7.1.07
- URL: https://doi.org/10.14257/ijhit.2014.7.1.07
- Categories: pheromone_trail_foraging;networks_interactions
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 116. Traffic Flow Estimation Using Ant Colony Optimization Algorithms

- Year: 2014
- DOI: 10.13053/cys-18-1-1581
- URL: https://doi.org/10.13053/cys-18-1-1581
- Categories: traffic_collective_motion;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 117. Pheromone-Based Ant Colony Algorithm for Optimal Proliferation of Research

- Year: 2013
- DOI: 10.4028/www.scientific.net/amr.734-737.3152
- URL: https://doi.org/10.4028/www.scientific.net/amr.734-737.3152
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 118. Ant Colony Algorithm Based on Dynamic Adaptive Pheromone Updating and Its Simulation

- Year: 2013
- DOI: 10.1109/iscid.2013.62
- URL: https://doi.org/10.1109/iscid.2013.62
- Categories: pheromone_trail_foraging;computational_swarm_model
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 119. Traffic flow forecasting based on ant colony neural network

- Year: 2010
- DOI: 10.1109/wcica.2010.5554931
- URL: https://doi.org/10.1109/wcica.2010.5554931
- Categories: traffic_collective_motion;networks_interactions
- Scope: `algorithmic_or_robotics_analogy`
- Status: `not_biological_target`
- Verdict: `not_a_direct_biology_validation`
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 120. The blind leading the blind: Modeling chemically mediated army ant raid patterns

- Year: 1989
- DOI: 10.1007/bf01065789
- URL: https://doi.org/10.1007/bf01065789
- Categories: army_ant_raids_mills;computational_swarm_model
- Scope: `category_proxy`
- Status: `partial`
- Verdict: `covered_by_generic_proxy`
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.
