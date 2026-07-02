# Literature Gap Backlog

This backlog records every literature-corpus paper that is not fully simulated at paper-level biological calibration.

- Source evaluation: `/home/s92137/ant_colony_sim/outputs/literature_corpus_120_evaluation.json`
- CSV: `/home/s92137/ant_colony_sim/outputs/literature_gap_backlog.csv`
- JSON: `/home/s92137/ant_colony_sim/outputs/literature_gap_backlog.json`

## Summary

- `P1_needs_quantitative_curve`: 17
- `P2_family_proxy_needs_paper_data`: 69
- `total`: 86

## P1_needs_quantitative_curve

### 1. Modeling tropotaxis in ant colonies: recruitment and trail formation

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2018
- DOI: 10.48550/arxiv.1811.00590
- URL: https://arxiv.org/abs/1811.00590
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: tropotaxis_gradient_response_proxy
- Evidence paper id: ramirez_2018
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: The model uses left/right/front sampling and exports per-step trajectory/sensing plus segment-flow metrics; exact tropotaxis equation fitting still needs digitized paper trajectories.

### 2. A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2015
- DOI: 10.48550/arxiv.1507.08467
- URL: https://arxiv.org/abs/1507.08467
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: negative_pheromone_forbidden_path
- Evidence paper id: jimenez_romero_2015
- Next action: Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes.
- Gap: The simulator now pairs avoid pheromone with short-term individual avoid memory, but it is still an ABM rule rather than the paper's spiking-neural-controller implementation.

### 3. A continuous model of ant foraging with pheromones and trail formation

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2014
- DOI: 10.48550/arxiv.1402.5611
- URL: https://arxiv.org/abs/1402.5611
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: rain_food_removal_washout
- Evidence paper id: amorim_2014
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### 4. A stochastic model of ant trail following with two pheromones

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2015
- DOI: 10.48550/arxiv.1508.06816
- URL: https://arxiv.org/abs/1508.06816
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: two-cue adaptation proxy
- Evidence paper id: malickova_2015
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: The simulator separates food/nest/water fields, but it is not yet the exact two-pheromone mathematical model and lacks direct synchronization metrics.

### 5. Trafficlike collective movement of ants on trails: absence of a jammed phase

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2009
- DOI: 10.1103/physrevlett.102.108001
- URL: https://arxiv.org/abs/0903.2717
- Categories: pheromone_trail_foraging;traffic_collective_motion
- Matched condition: no_jam_density_speed
- Evidence paper id: john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: The validation now uses segment-level speed/flow-density metrics. It still lacks calibrated body-contact rules and digitized no-jam flow curves.

### 8. Optimal and Resilient Pheromone Utilization in Ant Foraging

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2015
- DOI: 10.48550/arxiv.1507.00772
- URL: https://arxiv.org/abs/1507.00772
- Categories: pheromone_trail_foraging
- Matched condition: fail_stop_foraging_resilience
- Evidence paper id: afek_2015
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Afek et al. is an algorithmic pheromone model; this ABM only tests biological-style degradation, not asymptotic pheromone lower bounds or proof-level optimality.

### 9. Optimal traffic organisation in ants under crowded conditions

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2004
- DOI: 10.1038/nature02585
- URL: https://arxiv.org/abs/cond-mat/0403142
- Categories: traffic_collective_motion
- Matched condition: crowding_bridge_density_shift
- Evidence paper id: dussutour_2004
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: The model now exports segment-level density, speed and flow. It still lacks explicit antennal-contact mechanics and lane-discipline calibration from crowded trail experiments.

### 11. Hacking the Colony: On the Disruptive Effect of Misleading Pheromone and How to Defend Against It

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2022
- DOI: 10.48550/arxiv.2202.01808
- URL: https://arxiv.org/abs/2202.01808
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: misleading_pheromone_attack_and_caution
- Evidence paper id: aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes.
- Gap: The probe now uses sustained external fake-pheromone perturbation and generic avoid learning, but still lacks explicit attacker agents and calibrated attack/defense effect sizes.

### 12. Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2018
- DOI: 10.48550/arxiv.1805.05598
- URL: https://arxiv.org/abs/1805.05598
- Categories: pheromone_trail_foraging
- Matched condition: stochasticity_relocation
- Evidence paper id: shiraishi_2018
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: The current check measures relative relocation adaptation. It does not yet fit the paper's environment-dependent optimal stochasticity distribution.

### 13. Individual rules for trail pattern formation in Argentine ants (Linepithema humile)

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2012
- DOI: 10.1371/journal.pcbi.1002592
- URL: https://arxiv.org/abs/1201.5827
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Trail reinforcement, per-step trajectory/sensing samples and segment-level traffic metrics are now available; Weber-law curve fitting still needs digitized reference curves before quantitative fitting can be claimed.

### 20. Dynamical models of task organization in social insect colonies

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2015
- DOI: 10.48550/arxiv.1511.04769
- URL: https://arxiv.org/abs/1511.04769
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: The model has response-threshold-like task switching and exports switch rates/contact summaries, but it still lacks calibrated worker-worker contact matrices.

### 27. Modulation of pheromone trail strength with food quality in Pharaoh's ant, Monomorium pharaonis

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2007
- DOI: 10.1016/j.anbehav.2006.11.027
- URL: https://doi.org/10.1016/j.anbehav.2006.11.027
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: The simulator now has food quality and quality-weighted recruitment, but it still lacks species-specific sucrose concentration calibration and direct trail-laying event counts.

### 38. A continuous model of ant foraging with pheromones and trail formation

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `model_reference_only`
- Validation tier: `model_reference`
- Year: 2015
- DOI: 10.5540/03.2015.003.01.0323
- URL: https://doi.org/10.5540/03.2015.003.01.0323
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: rain_food_removal_washout
- Evidence paper id: amorim_2014
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Trail formation and decay are represented, but the simulator is an ABM with heuristic field units rather than Amorim's calibrated PDE chemotaxis variables.

### 51. Plastic collective endothermy in a complex animal society (army ant bivouacs: <i>Eciton burchellii parvispinum</i> )

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2019
- DOI: 10.1111/ecog.04064
- URL: https://doi.org/10.1111/ecog.04064
- Categories: brood_nest_microclimate;army_ant_raids_mills
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: The simulator now tests brood microclimate and stage-dependent thermoregulation, but still lacks fitted metabolic heat budgets, nest-site choice geometry and species-specific brood survival curves.

### 55. Quorum sensing, recruitment, and collective decision-making during colony emigration by the ant Leptothorax albipennis

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2002
- DOI: 10.1007/s00265-002-0487-x
- URL: https://doi.org/10.1007/s00265-002-0487-x
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting
- Matched condition: nest_relocation_quorum_choice
- Evidence paper id: pratt_2002
- Next action: Add nest relocation and quorum decision condition.
- Gap: The simulator now has a quorum relocation proxy, but lacks species-specific tandem running, carrying trajectories, site-volume geometry and fitted quorum thresholds.

### 66. Consensus decision making in the ant Myrmecina nipponica: house-hunters combine pheromone trails with quorum responses

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2012
- DOI: 10.1016/j.anbehav.2012.08.036
- URL: https://doi.org/10.1016/j.anbehav.2012.08.036
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting
- Matched condition: nest_relocation_quorum_choice
- Evidence paper id: pratt_2002
- Next action: Add nest relocation and quorum decision condition.
- Gap: The simulator now has a quorum relocation proxy, but lacks species-specific tandem running, carrying trajectories, site-volume geometry and fitted quorum thresholds.

### 88. Social organization of necrophoresis: insights into disease risk management in ant societies

- Status: `pass`
- Scope: `exact_paper_condition`
- Scientific status: `exact_qualitative_only`
- Validation tier: `exact_qualitative`
- Year: 2024
- DOI: 10.1098/rsos.240764
- URL: https://doi.org/10.1098/rsos.240764
- Categories: necrophoresis_social_immunity;networks_interactions
- Matched condition: necrophoresis_cleanup_latency
- Evidence paper id: avanzi_2024
- Next action: Calibrate corpse-age chemistry, pathogen state and corpse-removal interaction networks.
- Gap: Corpse relocation is represented, but the simulator still lacks pathogen state, corpse-age chemical profile calibration and colony-level interaction network validation.


## P2_family_proxy_needs_paper_data

### 7. Modeling no-jam traffic in ant trails: a pheromone-controlled approach

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2018
- DOI: 10.1088/1742-5468/aabfc7
- URL: https://doi.org/10.1088/1742-5468/aabfc7
- Categories: pheromone_trail_foraging;traffic_collective_motion;food_quality_choice;networks_interactions;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 10. Phase Transitions in Ant Traffic Driven by Density-Dependent Pheromone Feedback

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2026
- DOI: 10.2139/ssrn.6619462
- URL: https://doi.org/10.2139/ssrn.6619462
- Categories: pheromone_trail_foraging;traffic_collective_motion;necrophoresis_social_immunity;computational_swarm_model
- Matched condition: necrophoresis_cleanup_latency
- Evidence paper id: avanzi_2024
- Next action: Calibrate corpse-age chemistry, pathogen state and corpse-removal interaction networks.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 15. Small differences in learning speed for different food qualities can drive efficient collective foraging in ant colonies

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2018
- DOI: 10.1101/274209
- URL: https://doi.org/10.1101/274209
- Categories: pheromone_trail_foraging;food_quality_choice;networks_interactions;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 16. Analysis of Cooperative Perception in Ant Traffic and Its Effects on Transportation System by Using a Congestion-Free Ant-Trail Model

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2021
- DOI: 10.3390/s21072393
- URL: https://doi.org/10.3390/s21072393
- Categories: pheromone_trail_foraging;traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 17. A Pheromone-Based Utility Model for Collaborative Foraging

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2004
- DOI: 10.65109/aoay8418
- URL: https://doi.org/10.65109/aoay8418
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 18. A Pheromone-Based Utility Model for Collaborative Foraging

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2004
- DOI: 10.65109/ivir1553
- URL: https://doi.org/10.65109/ivir1553
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 21. Energetics of Trail Running, Load Carriage, and Emigration in the Column-Raiding Army Ant Eciton hamatum

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1988
- DOI: 10.1086/physzool.61.1.30163737
- URL: https://doi.org/10.1086/physzool.61.1.30163737
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting;army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 22. Spatiotemporal chemotactic model for ant foraging

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2014
- DOI: 10.1142/s0217984914502388
- URL: https://doi.org/10.1142/s0217984914502388
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 23. Trail traffic flow prediction by contact frequency among individual ants

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2013
- DOI: 10.1007/s11721-013-0085-8
- URL: https://doi.org/10.1007/s11721-013-0085-8
- Categories: pheromone_trail_foraging;traffic_collective_motion;networks_interactions;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 24. Congestion-Free Ant Traffic: Jam Absorption Mechanism in Multiple Platoons

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2019
- DOI: 10.3390/app9142918
- URL: https://doi.org/10.3390/app9142918
- Categories: pheromone_trail_foraging;traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 25. Interactions and information: Exploring task allocation in ant colonies using network analysis

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2021
- DOI: 10.1101/2021.03.29.437501
- URL: https://doi.org/10.1101/2021.03.29.437501
- Categories: pheromone_trail_foraging;traffic_collective_motion;task_allocation_division_labor;networks_interactions
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 26. The Neuro-ethology of Collective Decision-Making in Ant Colonies: A Case Study on Formica Rufa

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2025
- DOI: 10.61877/ijmrp.v3i9.303
- URL: https://doi.org/10.61877/ijmrp.v3i9.303
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 29. An agent-based model to investigate the roles of attractive and repellent pheromones in ant decision making during foraging

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2008
- DOI: 10.1016/j.jtbi.2008.08.015
- URL: https://doi.org/10.1016/j.jtbi.2008.08.015
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 30. Trail Pheromone Disruption of Argentine Ant Trail Formation and Foraging

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2010
- DOI: 10.1007/s10886-009-9734-1
- URL: https://doi.org/10.1007/s10886-009-9734-1
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 31. The foraging ecology of the army ant Eciton rapax: an ergonomic enigma?

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1985
- DOI: 10.1111/j.1365-2311.1985.tb00542.x
- URL: https://doi.org/10.1111/j.1365-2311.1985.tb00542.x
- Categories: pheromone_trail_foraging;nest_relocation_house_hunting;army_ant_raids_mills;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 33. Ants (Lasius niger) deposit more pheromone close to food sources and further from the nest but do not attempt to update erroneous pheromone trails

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2024
- DOI: 10.1007/s00040-024-00995-y
- URL: https://doi.org/10.1007/s00040-024-00995-y
- Categories: pheromone_trail_foraging;food_quality_choice;networks_interactions
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 34. Aerosol delivery of trail pheromone disrupts the foraging of the red imported fire ant, <i>Solenopsis invicta</i>

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2012
- DOI: 10.1002/ps.3349
- URL: https://doi.org/10.1002/ps.3349
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 37. Walk this way: modeling foraging ant dynamics in multiple food source environments

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2024
- DOI: 10.1007/s00285-024-02136-2
- URL: https://doi.org/10.1007/s00285-024-02136-2
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 39. Distributed Task Allocation in Network of Agents Based on Ant Colony Foraging Behavior

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2023
- DOI: 10.1145/3606305.3606324
- URL: https://doi.org/10.1145/3606305.3606324
- Categories: pheromone_trail_foraging;task_allocation_division_labor;networks_interactions;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 40. Avoiding traffic jams: Hitchhiking behavior as a strategy to reduce ant workers’ traffic on the foraging trail

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2018
- DOI: 10.1016/j.beproc.2018.08.015
- URL: https://doi.org/10.1016/j.beproc.2018.08.015
- Categories: pheromone_trail_foraging;traffic_collective_motion
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 41. Effect of trail pheromones and weather on the moving behaviour of the army ant Eciton burchellii

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2011
- DOI: 10.1007/s00040-010-0140-z
- URL: https://doi.org/10.1007/s00040-010-0140-z
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 42. Delay-Induced Hopf Bifurcation and Entropy-Based Distributional Uncertainty in a Stochastic Time-Delay Pheromone Feedback Model of Ant Foraging Dynamics

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2026
- DOI: 10.3390/e28070751
- URL: https://doi.org/10.3390/e28070751
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 43. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2026
- DOI: 10.1007/s00040-026-01106-9
- URL: https://doi.org/10.1007/s00040-026-01106-9
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 44. Building a polydomous colony: nest network expansion by Linepithema humile

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2026
- DOI: 10.1007/s00040-026-01081-1
- URL: https://doi.org/10.1007/s00040-026-01081-1
- Categories: pheromone_trail_foraging;brood_nest_microclimate;nest_relocation_house_hunting;food_quality_choice;networks_interactions
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 45. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2025
- DOI: 10.21203/rs.3.rs-7630446/v1
- URL: https://doi.org/10.21203/rs.3.rs-7630446/v1
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 46. Stop and go: exploring alternative mechanisms for task allocation in social insects - response and satisfaction thresholds trade off cost, accuracy, and speed differently

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2024
- DOI: 10.1101/2024.05.13.593812
- URL: https://doi.org/10.1101/2024.05.13.593812
- Categories: pheromone_trail_foraging;task_allocation_division_labor;brood_nest_microclimate;computational_swarm_model
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 47. Walk This Way: Modeling Foraging Ant Dynamics in Multiple Food Source Environments

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2024
- DOI: 10.1101/2024.01.20.576461
- URL: https://doi.org/10.1101/2024.01.20.576461
- Categories: pheromone_trail_foraging;networks_interactions;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 48. Ant traffic flow: Raiding swarms with few rules avoid gridlock

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2002
- DOI: 10.2307/4013963
- URL: https://doi.org/10.2307/4013963
- Categories: traffic_collective_motion;army_ant_raids_mills;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 49. MODELING AND SIMULATION OF ANT COLONY'S LABOR DIVISION WITH CONSTRAINTS FOR TASK ALLOCATION OF RESILIENT SUPPLY CHAINS

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2012
- DOI: 10.1142/s0218213012400143
- URL: https://doi.org/10.1142/s0218213012400143
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 50. Chemical Releasers of Social Behavior—IV. The Hindgut as the Source of the Odor Trail Pheromone in the Neotropical Army Ant Genus Eciton1

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1964
- DOI: 10.1093/aesa/57.6.793
- URL: https://doi.org/10.1093/aesa/57.6.793
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 53. No evidence that recruitment pheromone modulates olfactory, visual, or spatial learning in the ant Lasius niger

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2024
- DOI: 10.1007/s00265-024-03430-1
- URL: https://doi.org/10.1007/s00265-024-03430-1
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 54. Reduced foraging investment as an adaptation to patchy food sources: a phasic army ant simulation

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2017
- DOI: 10.1101/101600
- URL: https://doi.org/10.1101/101600
- Categories: pheromone_trail_foraging;brood_nest_microclimate;army_ant_raids_mills;computational_swarm_model
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 57. From nonlinearity to optimality: pheromone trail foraging by ants

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2003
- DOI: 10.1006/anbe.2003.2224
- URL: https://doi.org/10.1006/anbe.2003.2224
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 58. Trail geometry gives polarity to ant foraging networks

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2004
- DOI: 10.1038/nature03105
- URL: https://doi.org/10.1038/nature03105
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 59. The blind leading the blind in army ant raid patterns: Testing a model of self-organization (Hymenoptera: Formicidae)

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1991
- DOI: 10.1007/bf01048072
- URL: https://doi.org/10.1007/bf01048072
- Categories: army_ant_raids_mills;computational_swarm_model
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 60. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1993
- DOI: 10.1007/bf02460691
- URL: https://doi.org/10.1007/bf02460691
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 62. Spatial and temporal variation in pheromone composition of ant foraging trails

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2007
- DOI: 10.1093/beheco/arl104
- URL: https://doi.org/10.1093/beheco/arl104
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 63. A connectionist type model of self-organized foraging and emergent behavior in ant swarms

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1992
- DOI: 10.1016/s0022-5193(05)80697-6
- URL: https://doi.org/10.1016/s0022-5193(05)80697-6
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 64. Pheromone Disruption of Argentine Ant Trail Integrity

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2008
- DOI: 10.1007/s10886-008-9566-4
- URL: https://doi.org/10.1007/s10886-008-9566-4
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 65. Colony size does not predict foraging distance in the ant Temnothorax rugatulus: a puzzle for standard scaling models

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2013
- DOI: 10.1007/s00040-012-0272-4
- URL: https://doi.org/10.1007/s00040-012-0272-4
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 67. Argentine Ant (Hymenoptera: Formicidae) Trail Pheromone Enhances Consumption of Liquid Sucrose Solution

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2000
- DOI: 10.1603/0022-0493-93.1.119
- URL: https://doi.org/10.1603/0022-0493-93.1.119
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 68. Movement, Encounter Rate, and Collective Behavior in Ant Colonies

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2021
- DOI: 10.1093/aesa/saaa036
- URL: https://doi.org/10.1093/aesa/saaa036
- Categories: traffic_collective_motion;task_allocation_division_labor;networks_interactions
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 69. Response thresholds to recruitment signals and the regulation of foraging intensity in the ant Myrmica sabuleti (Hymenoptera, Formicidae)

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2000
- DOI: 10.1016/s0376-6357(99)00077-7
- URL: https://doi.org/10.1016/s0376-6357(99)00077-7
- Categories: pheromone_trail_foraging;task_allocation_division_labor
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 70. Foraging energetics of a nectar-feeding ant: metabolic expenditure as a function of food-source profitability

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2006
- DOI: 10.1242/jeb.02478
- URL: https://doi.org/10.1242/jeb.02478
- Categories: pheromone_trail_foraging;traffic_collective_motion;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 71. Coordination of Raiding and Emigration in the Ponerine Army Ant Leptogenys distinguenda (Hymenoptera: Formicidae: Ponerinae): A Signal Analysis

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2002
- DOI: 10.1023/a:1015484917019
- URL: https://doi.org/10.1023/a:1015484917019
- Categories: nest_relocation_house_hunting;army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 72. Notes on an army ant (<i>Eciton burchelli</i>) raid on a social wasp colony (<i>Agelaia yepocapa</i>) in Costa Rica

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1990
- DOI: 10.1017/s0266467400004958
- URL: https://doi.org/10.1017/s0266467400004958
- Categories: army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 73. First identification of a trail pheromone of an army ant (Aenictus species)

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1994
- DOI: 10.1007/bf01919378
- URL: https://doi.org/10.1007/bf01919378
- Categories: pheromone_trail_foraging;army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 74. Effect of Trail Bifurcation Asymmetry and Pheromone Presence or Absence on Trail Choice by <i>Lasius niger</i> Ants

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2014
- DOI: 10.1111/eth.12248
- URL: https://doi.org/10.1111/eth.12248
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 76. Argentine Ant Trail Pheromone Disruption is Mediated by Trail Concentration

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2011
- DOI: 10.1007/s10886-011-0019-0
- URL: https://doi.org/10.1007/s10886-011-0019-0
- Categories: misleading_negative_pheromone;pheromone_trail_foraging
- Matched condition: negative_pheromone_forbidden_path + misleading_pheromone_attack_and_caution
- Evidence paper id: jimenez_romero_2015/aswale_2022
- Next action: Add active detractor/cautionary pheromone agents and calibrate attack/defense effect sizes.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 77. Food recruitment as a component of the trunk-trail foraging behaviour of Lasius fuliginosus (Hymenoptera: Formicidae)

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1997
- DOI: 10.1016/s0376-6357(97)00773-0
- URL: https://doi.org/10.1016/s0376-6357(97)00773-0
- Categories: pheromone_trail_foraging
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 78. An Improvement in ant Algorithm Method for Optimizing a Transport Route with Regard to Traffic Flow

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2017
- DOI: 10.1016/j.proeng.2017.04.396
- URL: https://doi.org/10.1016/j.proeng.2017.04.396
- Categories: traffic_collective_motion;computational_swarm_model
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 79. Elevational and geographic variation in army ant swarm raid rates

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2011
- DOI: 10.1007/s00040-010-0129-7
- URL: https://doi.org/10.1007/s00040-010-0129-7
- Categories: army_ant_raids_mills;computational_swarm_model
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 80. Interactions and information: exploring task allocation in ant colonies using network analysis

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2022
- DOI: 10.1016/j.anbehav.2022.04.015
- URL: https://doi.org/10.1016/j.anbehav.2022.04.015
- Categories: task_allocation_division_labor;networks_interactions
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 81. Decentralized communication, trail connectivity and emergent benefits of ant pheromone trail networks

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2011
- DOI: 10.1007/s12293-010-0039-2
- URL: https://doi.org/10.1007/s12293-010-0039-2
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 83. Multi-Agent Cooperation Using the Ant Algorithm with Variable Pheromone Placement

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2005
- DOI: 10.1109/cec.2005.1554831
- URL: https://doi.org/10.1109/cec.2005.1554831
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 84. Trail Pheromone Does Not Modulate Subjective Reward Evaluation in Lasius niger Ants

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2020
- DOI: 10.3389/fpsyg.2020.555576
- URL: https://doi.org/10.3389/fpsyg.2020.555576
- Categories: pheromone_trail_foraging;food_quality_choice
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 86. A single-pheromone model accounts for empirical patterns of ant colony foraging previously modeled using two pheromones

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2023
- DOI: 10.1016/j.cogsys.2023.02.005
- URL: https://doi.org/10.1016/j.cogsys.2023.02.005
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 87. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1993
- DOI: 10.1016/s0092-8240(05)80195-8
- URL: https://doi.org/10.1016/s0092-8240(05)80195-8
- Categories: task_allocation_division_labor;computational_swarm_model
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 92. Novel observation of a raptor, Collared Forest-falcon ( <i>Micrastur semitorquatus</i> ), depredating a fleeing snake at an army ant ( <i>Eciton burchellii parvispinum</i> ) raid front

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2018
- DOI: 10.1676/1559-4491-130.3.792
- URL: https://doi.org/10.1676/1559-4491-130.3.792
- Categories: army_ant_raids_mills
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 93. Induced biotic response in Amazonian ant-plants: the role of leaf damage intensity and plant-derived food rewards on ant recruitment

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2016
- DOI: 10.13102/sociobiology.v63i3.1050
- URL: https://doi.org/10.13102/sociobiology.v63i3.1050
- Categories: pheromone_trail_foraging;food_quality_choice;computational_swarm_model
- Matched condition: food_quality_recruitment
- Evidence paper id: jackson_chaline_2007
- Next action: Calibrate resource quality against paper-specific sucrose/protein concentration, distance and trail-laying counts.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 94. Deterministic Model for Analyzing the Dynamics of Ant System Algorithm and Performance Amelioration through a New Pheromone Deposition Approach

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2008
- DOI: 10.1109/iciafs.2008.4783979
- URL: https://doi.org/10.1109/iciafs.2008.4783979
- Categories: pheromone_trail_foraging;computational_swarm_model
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 95. The emergence of a collective sensory response threshold in ant colonies

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2021
- DOI: 10.1101/2021.10.30.466564
- URL: https://doi.org/10.1101/2021.10.30.466564
- Categories: task_allocation_division_labor;brood_nest_microclimate;networks_interactions;computational_swarm_model
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 98. Reduced foraging investment as an adaptation to patchy food sources: A phasic army ant simulation

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2017
- DOI: 10.1016/j.jtbi.2017.06.009
- URL: https://doi.org/10.1016/j.jtbi.2017.06.009
- Categories: pheromone_trail_foraging;army_ant_raids_mills;computational_swarm_model
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 105. Dynamics of ant activity under extreme climatic changes in 2024: effects of temperature and humidity on Formica rufa and Lasius fuliginosus behavior

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2026
- DOI: 10.55730/1300-0179.3265
- URL: https://doi.org/10.55730/1300-0179.3265
- Categories: pheromone_trail_foraging;brood_nest_microclimate
- Matched condition: brood_microclimate_stage_thermoregulation
- Evidence paper id: baudier_2019
- Next action: Calibrate brood microclimate against measured core temperatures, brood stage, nest-site geometry and survival curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 107. ANTi-JAM solutions for smart roads: Ant-inspired traffic flow rules under CAVs environment

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2025
- DOI: 10.1016/j.trip.2025.101331
- URL: https://doi.org/10.1016/j.trip.2025.101331
- Categories: traffic_collective_motion
- Matched condition: crowding_bridge_density_shift + no_jam_density_speed
- Evidence paper id: dussutour_2004/john_2009
- Next action: Calibrate trail geometry, body-contact/lane rules and digitized flow-density curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 108. Pheromone representation in the ant antennal lobe changes with age

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2024
- DOI: 10.1101/2024.02.13.580193
- URL: https://doi.org/10.1101/2024.02.13.580193
- Categories: pheromone_trail_foraging;task_allocation_division_labor;army_ant_raids_mills
- Matched condition: task_demand_reallocation
- Evidence paper id: kang_theraulaz_2015
- Next action: Add worker contact matrices and network-calibrated task allocation metrics.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 112. Role of the pheromone for orientation in the group foraging ant, Veromessor pergandei

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2020
- DOI: 10.31219/osf.io/w2rn4
- URL: https://doi.org/10.31219/osf.io/w2rn4
- Categories: pheromone_trail_foraging;networks_interactions
- Matched condition: single_food_trail
- Evidence paper id: perna_2012
- Next action: Define paper-specific geometry/species parameters and fit digitized trajectory or response curves.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 114. Optimal construction of army ant living bridges

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 2017
- DOI: 10.1101/116780
- URL: https://doi.org/10.1101/116780
- Categories: pheromone_trail_foraging;army_ant_raids_mills;networks_interactions;computational_swarm_model
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.

### 120. The blind leading the blind: Modeling chemically mediated army ant raid patterns

- Status: `pass`
- Scope: `validated_family_condition`
- Scientific status: `family_qualitative_proxy`
- Validation tier: `family_proxy`
- Year: 1989
- DOI: 10.1007/bf01065789
- URL: https://doi.org/10.1007/bf01065789
- Categories: army_ant_raids_mills;computational_swarm_model
- Matched condition: army_ant_mill_mortality
- Evidence paper id: army_ant_mill_qualitative
- Next action: Add digitized paper-level biological measurements and fit only shared model parameters, not paper-specific exception rules.
- Gap: Family-level qualitative condition is covered by shared simulator rules; paper-specific quantitative calibration, species parameters and digitized curves may still be missing.
