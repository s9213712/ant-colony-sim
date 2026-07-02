# Literature Gap Backlog

This backlog records every literature-corpus paper that is not fully simulated by the current validation matrix.

- Source evaluation: `outputs/literature_corpus_120_evaluation.json`
- CSV: `outputs/literature_gap_backlog.csv`
- JSON: `outputs/literature_gap_backlog.json`

## Summary

- `P2_proxy_only`: 69
- `P3_algorithmic_reference_only`: 34
- `total`: 103

## P2_proxy_only

### 7. Modeling no-jam traffic in ant trails: a pheromone-controlled approach

- Status: `partial`
- Scope: `category_proxy`
- Year: 2018
- DOI: 10.1088/1742-5468/aabfc7
- URL: https://doi.org/10.1088/1742-5468/aabfc7
- Categories: pheromone_trail_foraging;traffic_collective_motion;food_quality_choice;networks_interactions;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 10. Phase Transitions in Ant Traffic Driven by Density-Dependent Pheromone Feedback

- Status: `partial`
- Scope: `category_proxy`
- Year: 2026
- DOI: 10.2139/ssrn.6619462
- URL: https://doi.org/10.2139/ssrn.6619462
- Categories: pheromone_trail_foraging;traffic_collective_motion;necrophoresis_social_immunity;computational_swarm_model
- Matched condition: necrophoresis_cleanup_latency
- Evidence paper id: avanzi_2024
- Next action: Calibrate corpse-age chemistry, pathogen state and corpse-removal interaction networks.
- Gap: Corpse cleanup is now testable, but generic corpse-management papers still need corpse-age chemistry, pathogen state and interaction-network validation.

### 15. Small differences in learning speed for different food qualities can drive efficient collective foraging in ant colonies

- Status: `partial`
- Scope: `category_proxy`
- Year: 2018
- DOI: 10.1101/274209
- URL: https://doi.org/10.1101/274209
- Categories: pheromone_trail_foraging;food_quality_choice;networks_interactions;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 16. Analysis of Cooperative Perception in Ant Traffic and Its Effects on Transportation System by Using a Congestion-Free Ant-Trail Model

- Status: `partial`
- Scope: `category_proxy`
- Year: 2021
- DOI: 10.3390/s21072393
- URL: https://doi.org/10.3390/s21072393
- Categories: pheromone_trail_foraging;traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 17. A Pheromone-Based Utility Model for Collaborative Foraging

- Status: `partial`
- Scope: `category_proxy`
- Year: 2004
- DOI: 10.65109/aoay8418
- URL: https://doi.org/10.65109/aoay8418
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 18. A Pheromone-Based Utility Model for Collaborative Foraging

- Status: `partial`
- Scope: `category_proxy`
- Year: 2004
- DOI: 10.65109/ivir1553
- URL: https://doi.org/10.65109/ivir1553
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 21. Energetics of Trail Running, Load Carriage, and Emigration in the Column-Raiding Army Ant Eciton hamatum

- Status: `partial`
- Scope: `category_proxy`
- Year: 1988
- DOI: 10.1086/physzool.61.1.30163737
- URL: https://doi.org/10.1086/physzool.61.1.30163737
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting;army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 22. Spatiotemporal chemotactic model for ant foraging

- Status: `partial`
- Scope: `category_proxy`
- Year: 2014
- DOI: 10.1142/s0217984914502388
- URL: https://doi.org/10.1142/s0217984914502388
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 23. Trail traffic flow prediction by contact frequency among individual ants

- Status: `partial`
- Scope: `category_proxy`
- Year: 2013
- DOI: 10.1007/s11721-013-0085-8
- URL: https://doi.org/10.1007/s11721-013-0085-8
- Categories: pheromone_trail_foraging;traffic_collective_motion;networks_interactions;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 24. Congestion-Free Ant Traffic: Jam Absorption Mechanism in Multiple Platoons

- Status: `partial`
- Scope: `category_proxy`
- Year: 2019
- DOI: 10.3390/app9142918
- URL: https://doi.org/10.3390/app9142918
- Categories: pheromone_trail_foraging;traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 25. Interactions and information: Exploring task allocation in ant colonies using network analysis

- Status: `partial`
- Scope: `category_proxy`
- Year: 2021
- DOI: 10.1101/2021.03.29.437501
- URL: https://doi.org/10.1101/2021.03.29.437501
- Categories: pheromone_trail_foraging;traffic_collective_motion;task_allocation_division_labor;networks_interactions
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 26. The Neuro-ethology of Collective Decision-Making in Ant Colonies: A Case Study on Formica Rufa

- Status: `partial`
- Scope: `category_proxy`
- Year: 2025
- DOI: 10.61877/ijmrp.v3i9.303
- URL: https://doi.org/10.61877/ijmrp.v3i9.303
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 29. An agent-based model to investigate the roles of attractive and repellent pheromones in ant decision making during foraging

- Status: `partial`
- Scope: `category_proxy`
- Year: 2008
- DOI: 10.1016/j.jtbi.2008.08.015
- URL: https://doi.org/10.1016/j.jtbi.2008.08.015
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 30. Trail Pheromone Disruption of Argentine Ant Trail Formation and Foraging

- Status: `partial`
- Scope: `category_proxy`
- Year: 2010
- DOI: 10.1007/s10886-009-9734-1
- URL: https://doi.org/10.1007/s10886-009-9734-1
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and individual learning around forbidden paths.
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 31. The foraging ecology of the army ant Eciton rapax: an ergonomic enigma?

- Status: `partial`
- Scope: `category_proxy`
- Year: 1985
- DOI: 10.1111/j.1365-2311.1985.tb00542.x
- URL: https://doi.org/10.1111/j.1365-2311.1985.tb00542.x
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting;army_ant_raids_mills;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 33. Ants (Lasius niger) deposit more pheromone close to food sources and further from the nest but do not attempt to update erroneous pheromone trails

- Status: `partial`
- Scope: `category_proxy`
- Year: 2024
- DOI: 10.1007/s00040-024-00995-y
- URL: https://doi.org/10.1007/s00040-024-00995-y
- Categories: pheromone_trail_foraging;food_quality_choice;networks_interactions
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 34. Aerosol delivery of trail pheromone disrupts the foraging of the red imported fire ant, <i>Solenopsis invicta</i>

- Status: `partial`
- Scope: `category_proxy`
- Year: 2012
- DOI: 10.1002/ps.3349
- URL: https://doi.org/10.1002/ps.3349
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and individual learning around forbidden paths.
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 37. Walk this way: modeling foraging ant dynamics in multiple food source environments

- Status: `partial`
- Scope: `category_proxy`
- Year: 2024
- DOI: 10.1007/s00285-024-02136-2
- URL: https://doi.org/10.1007/s00285-024-02136-2
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 39. Distributed Task Allocation in Network of Agents Based on Ant Colony Foraging Behavior

- Status: `partial`
- Scope: `category_proxy`
- Year: 2023
- DOI: 10.1145/3606305.3606324
- URL: https://doi.org/10.1145/3606305.3606324
- Categories: pheromone_trail_foraging;task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 40. Avoiding traffic jams: Hitchhiking behavior as a strategy to reduce ant workers’ traffic on the foraging trail

- Status: `partial`
- Scope: `category_proxy`
- Year: 2018
- DOI: 10.1016/j.beproc.2018.08.015
- URL: https://doi.org/10.1016/j.beproc.2018.08.015
- Categories: pheromone_trail_foraging;traffic_collective_motion
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 41. Effect of trail pheromones and weather on the moving behaviour of the army ant Eciton burchellii

- Status: `partial`
- Scope: `category_proxy`
- Year: 2011
- DOI: 10.1007/s00040-010-0140-z
- URL: https://doi.org/10.1007/s00040-010-0140-z
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 42. Delay-Induced Hopf Bifurcation and Entropy-Based Distributional Uncertainty in a Stochastic Time-Delay Pheromone Feedback Model of Ant Foraging Dynamics

- Status: `partial`
- Scope: `category_proxy`
- Year: 2026
- DOI: 10.3390/e28070751
- URL: https://doi.org/10.3390/e28070751
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 43. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Status: `partial`
- Scope: `category_proxy`
- Year: 2026
- DOI: 10.1007/s00040-026-01106-9
- URL: https://doi.org/10.1007/s00040-026-01106-9
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 44. Building a polydomous colony: nest network expansion by Linepithema humile

- Status: `partial`
- Scope: `category_proxy`
- Year: 2026
- DOI: 10.1007/s00040-026-01081-1
- URL: https://doi.org/10.1007/s00040-026-01081-1
- Categories: pheromone_trail_foraging;brood_nest_microclimate;nest_relocation_house_hunting;food_quality_choice;networks_interactions
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 45. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Status: `partial`
- Scope: `category_proxy`
- Year: 2025
- DOI: 10.21203/rs.3.rs-7630446/v1
- URL: https://doi.org/10.21203/rs.3.rs-7630446/v1
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 46. Stop and go: exploring alternative mechanisms for task allocation in social insects - response and satisfaction thresholds trade off cost, accuracy, and speed differently

- Status: `partial`
- Scope: `category_proxy`
- Year: 2024
- DOI: 10.1101/2024.05.13.593812
- URL: https://doi.org/10.1101/2024.05.13.593812
- Categories: pheromone_trail_foraging;task_allocation_division_labor;brood_nest_microclimate;computational_swarm_model
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 47. Walk This Way: Modeling Foraging Ant Dynamics in Multiple Food Source Environments

- Status: `partial`
- Scope: `category_proxy`
- Year: 2024
- DOI: 10.1101/2024.01.20.576461
- URL: https://doi.org/10.1101/2024.01.20.576461
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 48. Ant traffic flow: Raiding swarms with few rules avoid gridlock

- Status: `partial`
- Scope: `category_proxy`
- Year: 2002
- DOI: 10.2307/4013963
- URL: https://doi.org/10.2307/4013963
- Categories: traffic_collective_motion;army_ant_raids_mills;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 49. MODELING AND SIMULATION OF ANT COLONY'S LABOR DIVISION WITH CONSTRAINTS FOR TASK ALLOCATION OF RESILIENT SUPPLY CHAINS

- Status: `partial`
- Scope: `category_proxy`
- Year: 2012
- DOI: 10.1142/s0218213012400143
- URL: https://doi.org/10.1142/s0218213012400143
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 50. Chemical Releasers of Social Behavior—IV. The Hindgut as the Source of the Odor Trail Pheromone in the Neotropical Army Ant Genus Eciton1

- Status: `partial`
- Scope: `category_proxy`
- Year: 1964
- DOI: 10.1093/aesa/57.6.793
- URL: https://doi.org/10.1093/aesa/57.6.793
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 53. No evidence that recruitment pheromone modulates olfactory, visual, or spatial learning in the ant Lasius niger

- Status: `partial`
- Scope: `category_proxy`
- Year: 2024
- DOI: 10.1007/s00265-024-03430-1
- URL: https://doi.org/10.1007/s00265-024-03430-1
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 54. Reduced foraging investment as an adaptation to patchy food sources: a phasic army ant simulation

- Status: `partial`
- Scope: `category_proxy`
- Year: 2017
- DOI: 10.1101/101600
- URL: https://doi.org/10.1101/101600
- Categories: pheromone_trail_foraging;brood_nest_microclimate;army_ant_raids_mills;computational_swarm_model
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 57. From nonlinearity to optimality: pheromone trail foraging by ants

- Status: `partial`
- Scope: `category_proxy`
- Year: 2003
- DOI: 10.1006/anbe.2003.2224
- URL: https://doi.org/10.1006/anbe.2003.2224
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 58. Trail geometry gives polarity to ant foraging networks

- Status: `partial`
- Scope: `category_proxy`
- Year: 2004
- DOI: 10.1038/nature03105
- URL: https://doi.org/10.1038/nature03105
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 59. The blind leading the blind in army ant raid patterns: Testing a model of self-organization (Hymenoptera: Formicidae)

- Status: `partial`
- Scope: `category_proxy`
- Year: 1991
- DOI: 10.1007/bf01048072
- URL: https://doi.org/10.1007/bf01048072
- Categories: army_ant_raids_mills;computational_swarm_model
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 60. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Status: `partial`
- Scope: `category_proxy`
- Year: 1993
- DOI: 10.1007/bf02460691
- URL: https://doi.org/10.1007/bf02460691
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 62. Spatial and temporal variation in pheromone composition of ant foraging trails

- Status: `partial`
- Scope: `category_proxy`
- Year: 2007
- DOI: 10.1093/beheco/arl104
- URL: https://doi.org/10.1093/beheco/arl104
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 63. A connectionist type model of self-organized foraging and emergent behavior in ant swarms

- Status: `partial`
- Scope: `category_proxy`
- Year: 1992
- DOI: 10.1016/s0022-5193(05)80697-6
- URL: https://doi.org/10.1016/s0022-5193(05)80697-6
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 64. Pheromone Disruption of Argentine Ant Trail Integrity

- Status: `partial`
- Scope: `category_proxy`
- Year: 2008
- DOI: 10.1007/s10886-008-9566-4
- URL: https://doi.org/10.1007/s10886-008-9566-4
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and individual learning around forbidden paths.
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 65. Colony size does not predict foraging distance in the ant Temnothorax rugatulus: a puzzle for standard scaling models

- Status: `partial`
- Scope: `category_proxy`
- Year: 2013
- DOI: 10.1007/s00040-012-0272-4
- URL: https://doi.org/10.1007/s00040-012-0272-4
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 67. Argentine Ant (Hymenoptera: Formicidae) Trail Pheromone Enhances Consumption of Liquid Sucrose Solution

- Status: `partial`
- Scope: `category_proxy`
- Year: 2000
- DOI: 10.1603/0022-0493-93.1.119
- URL: https://doi.org/10.1603/0022-0493-93.1.119
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 68. Movement, Encounter Rate, and Collective Behavior in Ant Colonies

- Status: `partial`
- Scope: `category_proxy`
- Year: 2021
- DOI: 10.1093/aesa/saaa036
- URL: https://doi.org/10.1093/aesa/saaa036
- Categories: traffic_collective_motion;task_allocation_division_labor;networks_interactions
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 69. Response thresholds to recruitment signals and the regulation of foraging intensity in the ant Myrmica sabuleti (Hymenoptera, Formicidae)

- Status: `partial`
- Scope: `category_proxy`
- Year: 2000
- DOI: 10.1016/s0376-6357(99)00077-7
- URL: https://doi.org/10.1016/s0376-6357(99)00077-7
- Categories: pheromone_trail_foraging;task_allocation_division_labor
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 70. Foraging energetics of a nectar-feeding ant: metabolic expenditure as a function of food-source profitability

- Status: `partial`
- Scope: `category_proxy`
- Year: 2006
- DOI: 10.1242/jeb.02478
- URL: https://doi.org/10.1242/jeb.02478
- Categories: pheromone_trail_foraging;traffic_collective_motion;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 71. Coordination of Raiding and Emigration in the Ponerine Army Ant Leptogenys distinguenda (Hymenoptera: Formicidae: Ponerinae): A Signal Analysis

- Status: `partial`
- Scope: `category_proxy`
- Year: 2002
- DOI: 10.1023/a:1015484917019
- URL: https://doi.org/10.1023/a:1015484917019
- Categories: nest_relocation_house_hunting;army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 72. Notes on an army ant (<i>Eciton burchelli</i>) raid on a social wasp colony (<i>Agelaia yepocapa</i>) in Costa Rica

- Status: `partial`
- Scope: `category_proxy`
- Year: 1990
- DOI: 10.1017/s0266467400004958
- URL: https://doi.org/10.1017/s0266467400004958
- Categories: army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 73. First identification of a trail pheromone of an army ant (Aenictus species)

- Status: `partial`
- Scope: `category_proxy`
- Year: 1994
- DOI: 10.1007/bf01919378
- URL: https://doi.org/10.1007/bf01919378
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 74. Effect of Trail Bifurcation Asymmetry and Pheromone Presence or Absence on Trail Choice by <i>Lasius niger</i> Ants

- Status: `partial`
- Scope: `category_proxy`
- Year: 2014
- DOI: 10.1111/eth.12248
- URL: https://doi.org/10.1111/eth.12248
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 76. Argentine Ant Trail Pheromone Disruption is Mediated by Trail Concentration

- Status: `partial`
- Scope: `category_proxy`
- Year: 2011
- DOI: 10.1007/s10886-011-0019-0
- URL: https://doi.org/10.1007/s10886-011-0019-0
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and individual learning around forbidden paths.
- Gap: Avoid/fake pheromone effects are measurable but lack active detractor agents and individual learning.

### 77. Food recruitment as a component of the trunk-trail foraging behaviour of Lasius fuliginosus (Hymenoptera: Formicidae)

- Status: `partial`
- Scope: `category_proxy`
- Year: 1997
- DOI: 10.1016/s0376-6357(97)00773-0
- URL: https://doi.org/10.1016/s0376-6357(97)00773-0
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 78. An Improvement in ant Algorithm Method for Optimizing a Transport Route with Regard to Traffic Flow

- Status: `partial`
- Scope: `category_proxy`
- Year: 2017
- DOI: 10.1016/j.proeng.2017.04.396
- URL: https://doi.org/10.1016/j.proeng.2017.04.396
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 79. Elevational and geographic variation in army ant swarm raid rates

- Status: `partial`
- Scope: `category_proxy`
- Year: 2011
- DOI: 10.1007/s00040-010-0129-7
- URL: https://doi.org/10.1007/s00040-010-0129-7
- Categories: army_ant_raids_mills;computational_swarm_model
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 80. Interactions and information: exploring task allocation in ant colonies using network analysis

- Status: `partial`
- Scope: `category_proxy`
- Year: 2022
- DOI: 10.1016/j.anbehav.2022.04.015
- URL: https://doi.org/10.1016/j.anbehav.2022.04.015
- Categories: task_allocation_division_labor;networks_interactions
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 81. Decentralized communication, trail connectivity and emergent benefits of ant pheromone trail networks

- Status: `partial`
- Scope: `category_proxy`
- Year: 2011
- DOI: 10.1007/s12293-010-0039-2
- URL: https://doi.org/10.1007/s12293-010-0039-2
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 83. Multi-Agent Cooperation Using the Ant Algorithm with Variable Pheromone Placement

- Status: `partial`
- Scope: `category_proxy`
- Year: 2005
- DOI: 10.1109/cec.2005.1554831
- URL: https://doi.org/10.1109/cec.2005.1554831
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 84. Trail Pheromone Does Not Modulate Subjective Reward Evaluation in Lasius niger Ants

- Status: `partial`
- Scope: `category_proxy`
- Year: 2020
- DOI: 10.3389/fpsyg.2020.555576
- URL: https://doi.org/10.3389/fpsyg.2020.555576
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 86. A single-pheromone model accounts for empirical patterns of ant colony foraging previously modeled using two pheromones

- Status: `partial`
- Scope: `category_proxy`
- Year: 2023
- DOI: 10.1016/j.cogsys.2023.02.005
- URL: https://doi.org/10.1016/j.cogsys.2023.02.005
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 87. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Status: `partial`
- Scope: `category_proxy`
- Year: 1993
- DOI: 10.1016/s0092-8240(05)80195-8
- URL: https://doi.org/10.1016/s0092-8240(05)80195-8
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 92. Novel observation of a raptor, Collared Forest-falcon ( <i>Micrastur semitorquatus</i> ), depredating a fleeing snake at an army ant ( <i>Eciton burchellii parvispinum</i> ) raid front

- Status: `partial`
- Scope: `category_proxy`
- Year: 2018
- DOI: 10.1676/1559-4491-130.3.792
- URL: https://doi.org/10.1676/1559-4491-130.3.792
- Categories: army_ant_raids_mills
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 93. Induced biotic response in Amazonian ant-plants: the role of leaf damage intensity and plant-derived food rewards on ant recruitment

- Status: `partial`
- Scope: `category_proxy`
- Year: 2016
- DOI: 10.13102/sociobiology.v63i3.1050
- URL: https://doi.org/10.13102/sociobiology.v63i3.1050
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Food-quality recruitment is now testable, but generic corpus papers still need species-specific concentration, distance and trail-laying calibration.

### 94. Deterministic Model for Analyzing the Dynamics of Ant System Algorithm and Performance Amelioration through a New Pheromone Deposition Approach

- Status: `partial`
- Scope: `category_proxy`
- Year: 2008
- DOI: 10.1109/iciafs.2008.4783979
- URL: https://doi.org/10.1109/iciafs.2008.4783979
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 95. The emergence of a collective sensory response threshold in ant colonies

- Status: `partial`
- Scope: `category_proxy`
- Year: 2021
- DOI: 10.1101/2021.10.30.466564
- URL: https://doi.org/10.1101/2021.10.30.466564
- Categories: task_allocation_division_labor;brood_nest_microclimate;networks_interactions;computational_swarm_model
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 98. Reduced foraging investment as an adaptation to patchy food sources: A phasic army ant simulation

- Status: `partial`
- Scope: `category_proxy`
- Year: 2017
- DOI: 10.1016/j.jtbi.2017.06.009
- URL: https://doi.org/10.1016/j.jtbi.2017.06.009
- Categories: pheromone_trail_foraging;army_ant_raids_mills;computational_swarm_model
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 105. Dynamics of ant activity under extreme climatic changes in 2024: effects of temperature and humidity on Formica rufa and Lasius fuliginosus behavior

- Status: `partial`
- Scope: `category_proxy`
- Year: 2026
- DOI: 10.55730/1300-0179.3265
- URL: https://doi.org/10.55730/1300-0179.3265
- Categories: pheromone_trail_foraging;brood_nest_microclimate
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Brood microclimate is now testable, but generic corpus papers still need species-specific thermoregulation, nest-site geometry and brood-survival calibration.

### 107. ANTi-JAM solutions for smart roads: Ant-inspired traffic flow rules under CAVs environment

- Status: `partial`
- Scope: `category_proxy`
- Year: 2025
- DOI: 10.1016/j.trip.2025.101331
- URL: https://doi.org/10.1016/j.trip.2025.101331
- Categories: traffic_collective_motion
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: Traffic direction is covered, but paper-specific validation needs segment-level flow-density and speed curves.

### 108. Pheromone representation in the ant antennal lobe changes with age

- Status: `partial`
- Scope: `category_proxy`
- Year: 2024
- DOI: 10.1101/2024.02.13.580193
- URL: https://doi.org/10.1101/2024.02.13.580193
- Categories: pheromone_trail_foraging;task_allocation_division_labor;army_ant_raids_mills
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Task-demand switching and switch-rate summaries are covered, but worker-contact matrices and network calibration are not yet available.

### 112. Role of the pheromone for orientation in the group foraging ant, Veromessor pergandei

- Status: `partial`
- Scope: `category_proxy`
- Year: 2020
- DOI: 10.31219/osf.io/w2rn4
- URL: https://doi.org/10.31219/osf.io/w2rn4
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: Generic trail formation is covered, but paper-specific curve fitting usually needs individual trajectories, local gradients or digitized reference data.

### 114. Optimal construction of army ant living bridges

- Status: `partial`
- Scope: `category_proxy`
- Year: 2017
- DOI: 10.1101/116780
- URL: https://doi.org/10.1101/116780
- Categories: pheromone_trail_foraging;army_ant_raids_mills;networks_interactions;computational_swarm_model
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.

### 120. The blind leading the blind: Modeling chemically mediated army ant raid patterns

- Status: `partial`
- Scope: `category_proxy`
- Year: 1989
- DOI: 10.1007/bf01065789
- URL: https://doi.org/10.1007/bf01065789
- Categories: army_ant_raids_mills;computational_swarm_model
- Matched condition: ant_mill/death_spiral qualitative probe
- Evidence paper id: literature_alignment_probe
- Next action: Define a paper-specific simulation condition before claiming alignment.
- Gap: Death spiral and army-ant-like trails are qualitative; raid geometry, living bridges and species-specific energetics need new conditions.


## P3_algorithmic_reference_only

### 6. Applying Social Network Analysis to Agent-Based Models: A Case Study of Task Allocation in Swarm Robotics Inspired by Ant Foraging Behavior

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2019
- DOI: 10.1162/isal_a_00229
- URL: https://doi.org/10.1162/isal_a_00229
- Categories: pheromone_trail_foraging;task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 14. Heterogeneous multi-agent task allocation based on graph neural network ant colony optimization algorithms

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2023
- DOI: 10.20517/ir.2023.33
- URL: https://doi.org/10.20517/ir.2023.33
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 19. Development of Task Allocation Method for Swarm Robotic Systems Using Optimal Foraging Theory and Ant Colony Labor Division Model

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2021
- DOI: 10.1299/jsmermd.2021.1p2-f03
- URL: https://doi.org/10.1299/jsmermd.2021.1p2-f03
- Categories: pheromone_trail_foraging;task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 28. A cellular automata ant memory model of foraging in a swarm of robots

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2017
- DOI: 10.1016/j.apm.2017.03.021
- URL: https://doi.org/10.1016/j.apm.2017.03.021
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 32. A probabilistic cellular automata ant memory model for a swarm of foraging robots

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2016
- DOI: 10.1109/icarcv.2016.7838615
- URL: https://doi.org/10.1109/icarcv.2016.7838615
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 35. Formal analysis in a cellular automata ant model using swarm intelligence in robotics foraging task

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2017
- DOI: 10.1109/smc.2017.8122876
- URL: https://doi.org/10.1109/smc.2017.8122876
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 36. Ant Colony Optimization Based Model Checking Extended by Smell-like Pheromone

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2016
- DOI: 10.4108/eai.21-4-2016.151156
- URL: https://doi.org/10.4108/eai.21-4-2016.151156
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 52. Multiple-Agent Task Allocation Algorithm Utilizing Ant Colony Optimization

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2013
- DOI: 10.4304/jnw.8.11.2599-2606
- URL: https://doi.org/10.4304/jnw.8.11.2599-2606
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 56. Ant-like task allocation and recruitment in cooperative robots

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2000
- DOI: 10.1038/35023164
- URL: https://doi.org/10.1038/35023164
- Categories: pheromone_trail_foraging;task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 61. Multi-robot Task Allocation Based on Ant Colony Algorithm

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2012
- DOI: 10.4304/jcp.7.9.2160-2167
- URL: https://doi.org/10.4304/jcp.7.9.2160-2167
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 75. Evolving neural networks using ant colony optimization with pheromone trail limits

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2013
- DOI: 10.1109/ukci.2013.6651282
- URL: https://doi.org/10.1109/ukci.2013.6651282
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 82. Research on task allocation in multiple logistics robots based on an improved ant colony algorithm

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2016
- DOI: 10.1109/icrae.2016.7738780
- URL: https://doi.org/10.1109/icrae.2016.7738780
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 85. Optimal ant colony algorithm based multi-robot task allocation and processing sequence scheduling

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2008
- DOI: 10.1109/wcica.2008.4593859
- URL: https://doi.org/10.1109/wcica.2008.4593859
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 89. Improved Intelligent Method for Traffic Flow Prediction Based on Artificial Neural Networks and Ant Colony Optimization

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2012
- DOI: 10.4156/jcit.vol7.issue8.31
- URL: https://doi.org/10.4156/jcit.vol7.issue8.31
- Categories: traffic_collective_motion;networks_interactions
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 90. Research on Improvement of Ant Colony Algorithm for Multi-Robot Task Allocation

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2019
- DOI: 10.1109/itaic.2019.8785605
- URL: https://doi.org/10.1109/itaic.2019.8785605
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 91. Modeling Ant Nest Relocation at Low Active Ratio by Particle Swarm Optimization

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2019
- DOI: 10.1109/cec.2019.8789942
- URL: https://doi.org/10.1109/cec.2019.8789942
- Categories: nest_relocation_house_hunting;computational_swarm_model
- Matched condition: none
- Evidence paper id: none
- Next action: Keep as algorithmic inspiration only; do not use as direct biological validation target.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 96. Optimal A* Path Planning with Ant Colony Optimization on Multi-Robot Task Allocation for Manufacturing Model

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2021
- DOI: 10.1109/iciea52957.2021.9436716
- URL: https://doi.org/10.1109/iciea52957.2021.9436716
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 97. A Novel Improved Ant Colony Algorithm for Multi-Robot Task Allocation

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2018
- DOI: 10.1109/itoec.2018.8740438
- URL: https://doi.org/10.1109/itoec.2018.8740438
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 99. Ant Colony Algorithm in Traffic Flow Control

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2024
- DOI: 10.23939/acps2024.02.158
- URL: https://doi.org/10.23939/acps2024.02.158
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 100. Graph Convolutional Network Based Ant Colony Optimization for Robot Task Allocation

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2023
- DOI: 10.1109/ssci52147.2023.10372050
- URL: https://doi.org/10.1109/ssci52147.2023.10372050
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 101. Ant Colony Optimization Algorithm for Traffic Flow Estimation

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2017
- DOI: 10.1145/3134302.3134317
- URL: https://doi.org/10.1145/3134302.3134317
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 102. Traffic Flow Estimation Using Ant Colony Optimization Algorithms

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2014
- DOI: 10.13053/cys-18-1-2014-017
- URL: https://doi.org/10.13053/cys-18-1-2014-017
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 103. Hybrid Algorithm Based on Ant and Genetic Algorithms for Task Allocation on a Network of Homogeneous Processors

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2014
- DOI: 10.5121/ijcnc.2014.6113
- URL: https://doi.org/10.5121/ijcnc.2014.6113
- Categories: task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 104. Ant System Algorithm with Negative Pheromone for Course Scheduling Problem

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2008
- DOI: 10.1109/isda.2008.154
- URL: https://doi.org/10.1109/isda.2008.154
- Categories: misleading_negative_pheromone;pheromone_trail_foraging;computational_swarm_model
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and individual learning around forbidden paths.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 106. An Ensemble Ant Colony Optimization Algorithm with a Hybrid Pheromone Model for Learning Rule Lists

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2025
- DOI: 10.1145/3712256.3726427
- URL: https://doi.org/10.1145/3712256.3726427
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 109. Anti-Jam Solutions for Smart Roads: Ant-Inspired Traffic Flow Rules Under Cooperative Automated Vehicles Environment

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2024
- DOI: 10.2139/ssrn.4701534
- URL: https://doi.org/10.2139/ssrn.4701534
- Categories: traffic_collective_motion
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 110. Research on Improved Ant Colony Path Planning Algorithm for Updating Pheromone of Subway Inspection Mobile Robot

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2023
- DOI: 10.2139/ssrn.4623370
- URL: https://doi.org/10.2139/ssrn.4623370
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 111. Optimization Design of Expressway Traffic Flow Guidance System Based on GIS and Improved Ant Colony Optimization Algorithms

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2023
- DOI: 10.1109/ictei60496.2023.00104
- URL: https://doi.org/10.1109/ictei60496.2023.00104
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 113. Modeling Fast and Robust Ant Nest Relocation using Particle Swarm Optimization

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2019
- DOI: 10.1162/isal_a_00231
- URL: https://doi.org/10.1162/isal_a_00231
- Categories: nest_relocation_house_hunting;computational_swarm_model
- Matched condition: none
- Evidence paper id: none
- Next action: Keep as algorithmic inspiration only; do not use as direct biological validation target.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 115. Fault Pheromone Trail Evaporation of Power Distribution Networks using Ant Colony Optimization

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2014
- DOI: 10.14257/ijhit.2014.7.1.07
- URL: https://doi.org/10.14257/ijhit.2014.7.1.07
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 116. Traffic Flow Estimation Using Ant Colony Optimization Algorithms

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2014
- DOI: 10.13053/cys-18-1-1581
- URL: https://doi.org/10.13053/cys-18-1-1581
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 117. Pheromone-Based Ant Colony Algorithm for Optimal Proliferation of Research

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2013
- DOI: 10.4028/www.scientific.net/amr.734-737.3152
- URL: https://doi.org/10.4028/www.scientific.net/amr.734-737.3152
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 118. Ant Colony Algorithm Based on Dynamic Adaptive Pheromone Updating and Its Simulation

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2013
- DOI: 10.1109/iscid.2013.62
- URL: https://doi.org/10.1109/iscid.2013.62
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Add per-step local pheromone samples, gradient vectors and turn-angle logs.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.

### 119. Traffic flow forecasting based on ant colony neural network

- Status: `not_biological_target`
- Scope: `algorithmic_or_robotics_analogy`
- Year: 2010
- DOI: 10.1109/wcica.2010.5554931
- URL: https://doi.org/10.1109/wcica.2010.5554931
- Categories: traffic_collective_motion;networks_interactions
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Add trail-segment flow-density and velocity measurements.
- Gap: This is an algorithmic, robotics or ACO-inspired paper. It may inspire simulation tests, but the ant biology simulator should not be judged as reproducing its engineering objective function.
