# Ant Colony Simulation Literature Corpus 100+

This corpus is generated from Crossref queries plus the paper-condition seed set already used by the simulator validation suite.
It is a triage index, not a claim that every paper is already quantitatively reproduced.

- Count: `120`
- JSON: `outputs/literature_corpus_100.json`
- CSV: `outputs/literature_corpus_100.csv`

## Readiness

- `direct_or_near_term`: 118
- `needs_new_condition`: 2

## Categories

- `pheromone_trail_foraging`: 81
- `computational_swarm_model`: 70
- `networks_interactions`: 30
- `task_allocation_division_labor`: 25
- `traffic_collective_motion`: 22
- `army_ant_raids_mills`: 17
- `food_quality_choice`: 16
- `nest_relocation_house_hunting`: 8
- `brood_nest_microclimate`: 6
- `misleading_negative_pheromone`: 6
- `necrophoresis_social_immunity`: 2

## Papers

### 1. Modeling tropotaxis in ant colonies: recruitment and trail formation

- Year: 2018
- Authors: Ramirez et al.
- Venue: arXiv
- DOI: 10.48550/arxiv.1811.00590
- URL: https://arxiv.org/abs/1811.00590
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 2. A Model for Foraging Ants, Controlled by Spiking Neural Networks and Double Pheromones

- Year: 2015
- Authors: Jimenez-Romero et al.
- Venue: arXiv
- DOI: 10.48550/arxiv.1507.08467
- URL: https://arxiv.org/abs/1507.08467
- Categories: pheromone_trail_foraging, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 3. A continuous model of ant foraging with pheromones and trail formation

- Year: 2014
- Authors: Amorim
- Venue: arXiv
- DOI: 10.48550/arxiv.1402.5611
- URL: https://arxiv.org/abs/1402.5611
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 4. A stochastic model of ant trail following with two pheromones

- Year: 2015
- Authors: Malickova, Yates & Bodova
- Venue: arXiv
- DOI: 10.48550/arxiv.1508.06816
- URL: https://arxiv.org/abs/1508.06816
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 5. Trafficlike collective movement of ants on trails: absence of a jammed phase

- Year: 2009
- Authors: John et al.
- Venue: Physical Review Letters / arXiv
- DOI: 10.1103/physrevlett.102.108001
- URL: https://arxiv.org/abs/0903.2717
- Categories: pheromone_trail_foraging, traffic_collective_motion
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe
- Source query: `seed`

### 6. Applying Social Network Analysis to Agent-Based Models: A Case Study of Task Allocation in Swarm Robotics Inspired by Ant Foraging Behavior

- Year: 2019
- Authors: Georgina Montserrat Reséndiz-Benhumea, Tom Froese, Gabriel Ramos-Fernández, Sandra E. Smith-Aguilar
- Venue: The 2019 Conference on Artificial Life
- DOI: 10.1162/isal_a_00229
- URL: https://doi.org/10.1162/isal_a_00229
- Categories: pheromone_trail_foraging, task_allocation_division_labor, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe
- Source query: `ant social insect network task allocation`

### 7. Modeling no-jam traffic in ant trails: a pheromone-controlled approach

- Year: 2018
- Authors: Ning Guo, Mao-Bin Hu, Rui Jiang, Jianxun Ding, et al.
- Venue: Journal of Statistical Mechanics: Theory and Experiment
- DOI: 10.1088/1742-5468/aabfc7
- URL: https://doi.org/10.1088/1742-5468/aabfc7
- Categories: pheromone_trail_foraging, traffic_collective_motion, food_quality_choice, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe, needs_food_quality_resource_model
- Source query: `ant double bridge experiment pheromone`

### 8. Optimal and Resilient Pheromone Utilization in Ant Foraging

- Year: 2015
- Authors: Afek, Kecher & Sulamy
- Venue: arXiv
- DOI: 10.48550/arxiv.1507.00772
- URL: https://arxiv.org/abs/1507.00772
- Categories: pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 9. Optimal traffic organisation in ants under crowded conditions

- Year: 2004
- Authors: Dussutour et al.
- Venue: Nature
- DOI: 10.1038/nature02585
- URL: https://arxiv.org/abs/cond-mat/0403142
- Categories: traffic_collective_motion
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `seed`

### 10. Phase Transitions in Ant Traffic Driven by Density-Dependent Pheromone Feedback

- Year: 2026
- Authors: Ozhan Kayacan, Salih Yalcinbas
- Venue: Elsevier BV
- DOI: 10.2139/ssrn.6619462
- URL: https://doi.org/10.2139/ssrn.6619462
- Categories: pheromone_trail_foraging, traffic_collective_motion, necrophoresis_social_immunity, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe, extend_corpse_cleanup_probe
- Source query: `ant foraging pheromone model`

### 11. Hacking the Colony: On the Disruptive Effect of Misleading Pheromone and How to Defend Against It

- Year: 2022
- Authors: Aswale et al.
- Venue: AAMAS / arXiv
- DOI: 10.48550/arxiv.2202.01808
- URL: https://arxiv.org/abs/2202.01808
- Categories: misleading_negative_pheromone, pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_negative_pheromone_probe, existing_or_extend_trail_probe
- Source query: `seed`

### 12. Diverse Stochasticity Leads a Colony of Ants to Optimal Foraging

- Year: 2018
- Authors: Shiraishi et al.
- Venue: arXiv
- DOI: 10.48550/arxiv.1805.05598
- URL: https://arxiv.org/abs/1805.05598
- Categories: pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 13. Individual rules for trail pattern formation in Argentine ants (Linepithema humile)

- Year: 2012
- Authors: Perna et al.
- Venue: PLoS Computational Biology / arXiv
- DOI: 10.1371/journal.pcbi.1002592
- URL: https://arxiv.org/abs/1201.5827
- Categories: pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `seed`

### 14. Heterogeneous multi-agent task allocation based on graph neural network ant colony optimization algorithms

- Year: 2023
- Authors: Ziyuan Ma, Huajun Gong
- Venue: Intelligence &amp; Robotics
- DOI: 10.20517/ir.2023.33
- URL: https://doi.org/10.20517/ir.2023.33
- Categories: task_allocation_division_labor, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 15. Small differences in learning speed for different food qualities can drive efficient collective foraging in ant colonies

- Year: 2018
- Authors: F. B. Oberhauser, A. Koch, T. J. Czaczkes
- Venue: openRxiv
- DOI: 10.1101/274209
- URL: https://doi.org/10.1101/274209
- Categories: pheromone_trail_foraging, food_quality_choice, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `army ant raid collective behavior model`

### 16. Analysis of Cooperative Perception in Ant Traffic and Its Effects on Transportation System by Using a Congestion-Free Ant-Trail Model

- Year: 2021
- Authors: Prafull Kasture, Hidekazu Nishimura
- Venue: Sensors
- DOI: 10.3390/s21072393
- URL: https://doi.org/10.3390/s21072393
- Categories: pheromone_trail_foraging, traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 17. A Pheromone-Based Utility Model for Collaborative Foraging

- Year: 2004
- Authors: Liviu Panait, Sean Luke
- Venue: International Joint Conference on Autonomous Agents and Multiagent Systems
- DOI: 10.65109/aoay8418
- URL: https://doi.org/10.65109/aoay8418
- Categories: pheromone_trail_foraging, food_quality_choice, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `ant foraging pheromone model`

### 18. A Pheromone-Based Utility Model for Collaborative Foraging

- Year: 2004
- Authors: Liviu Panait, Sean Luke
- Venue: International Joint Conference on Autonomous Agents and Multiagent Systems
- DOI: 10.65109/ivir1553
- URL: https://doi.org/10.65109/ivir1553
- Categories: pheromone_trail_foraging, food_quality_choice, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `ant foraging pheromone model`

### 19. Development of Task Allocation Method for Swarm Robotic Systems Using Optimal Foraging Theory and Ant Colony Labor Division Model

- Year: 2021
- Authors: Takuya YAMASHITA, Kohei YAMAGISHI, Tsuyoshi SUZUKI
- Venue: The Proceedings of JSME annual Conference on Robotics and Mechatronics (Robomec)
- DOI: 10.1299/jsmermd.2021.1p2-f03
- URL: https://doi.org/10.1299/jsmermd.2021.1p2-f03
- Categories: pheromone_trail_foraging, task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe
- Source query: `ant division of labor task allocation model`

### 20. Dynamical models of task organization in social insect colonies

- Year: 2015
- Authors: Kang & Theraulaz
- Venue: arXiv
- DOI: 10.48550/arxiv.1511.04769
- URL: https://arxiv.org/abs/1511.04769
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `seed`

### 21. Energetics of Trail Running, Load Carriage, and Emigration in the Column-Raiding Army Ant Eciton hamatum

- Year: 1988
- Authors: George A. Bartholomew, John R. B. Lighton, Donald H. Feener
- Venue: Physiological Zoology
- DOI: 10.1086/physzool.61.1.30163737
- URL: https://doi.org/10.1086/physzool.61.1.30163737
- Categories: pheromone_trail_foraging, nest_relocation_house_hunting, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe
- Source query: `Eciton army ant raid trail pheromone`

### 22. Spatiotemporal chemotactic model for ant foraging

- Year: 2014
- Authors: Subramanian Ramakrishnan, Thomas Laurent, Manish Kumar, Andrea L. Bertozzi
- Venue: Modern Physics Letters B
- DOI: 10.1142/s0217984914502388
- URL: https://doi.org/10.1142/s0217984914502388
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 23. Trail traffic flow prediction by contact frequency among individual ants

- Year: 2013
- Authors: Hideyasu Sasaki, Ho-fung Leung
- Venue: Swarm Intelligence
- DOI: 10.1007/s11721-013-0085-8
- URL: https://doi.org/10.1007/s11721-013-0085-8
- Categories: pheromone_trail_foraging, traffic_collective_motion, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 24. Congestion-Free Ant Traffic: Jam Absorption Mechanism in Multiple Platoons

- Year: 2019
- Authors: Prafull Kasture, Hidekazu Nishimura
- Venue: Applied Sciences
- DOI: 10.3390/app9142918
- URL: https://doi.org/10.3390/app9142918
- Categories: pheromone_trail_foraging, traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe
- Source query: `ant trail traffic jam density`

### 25. Interactions and information: Exploring task allocation in ant colonies using network analysis

- Year: 2021
- Authors: Anshuman Swain, Sara D. Williams, Louisa J. Di Felice, Elizabeth A. Hobson
- Venue: openRxiv
- DOI: 10.1101/2021.03.29.437501
- URL: https://doi.org/10.1101/2021.03.29.437501
- Categories: pheromone_trail_foraging, traffic_collective_motion, task_allocation_division_labor, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe, existing_traffic_density_probe
- Source query: `ant task allocation response threshold`

### 26. The Neuro-ethology of Collective Decision-Making in Ant Colonies: A Case Study on Formica Rufa

- Year: 2025
- Authors: Nasar Ahmed khan
- Venue: International Journal for Multidimensional Research Perspectives
- DOI: 10.61877/ijmrp.v3i9.303
- URL: https://doi.org/10.61877/ijmrp.v3i9.303
- Categories: pheromone_trail_foraging, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant collective decision making foraging`

### 27. Modulation of pheromone trail strength with food quality in Pharaoh's ant, Monomorium pharaonis

- Year: 2007
- Authors: Duncan E. Jackson, Nicolas Châline
- Venue: Animal Behaviour
- DOI: 10.1016/j.anbehav.2006.11.027
- URL: https://doi.org/10.1016/j.anbehav.2006.11.027
- Categories: pheromone_trail_foraging, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `ant pheromone trail foraging`

### 28. A cellular automata ant memory model of foraging in a swarm of robots

- Year: 2017
- Authors: Danielli A. Lima, Gina M. B. Oliveira
- Venue: Applied Mathematical Modelling
- DOI: 10.1016/j.apm.2017.03.021
- URL: https://doi.org/10.1016/j.apm.2017.03.021
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 29. An agent-based model to investigate the roles of attractive and repellent pheromones in ant decision making during foraging

- Year: 2008
- Authors: Elva J.H. Robinson, Francis L.W. Ratnieks, M. Holcombe
- Venue: Journal of Theoretical Biology
- DOI: 10.1016/j.jtbi.2008.08.015
- URL: https://doi.org/10.1016/j.jtbi.2008.08.015
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant collective decision making foraging`

### 30. Trail Pheromone Disruption of Argentine Ant Trail Formation and Foraging

- Year: 2010
- Authors: David Maxwell Suckling, Robert W. Peck, Lloyd D. Stringer, Kirsten Snook, et al.
- Venue: Journal of Chemical Ecology
- DOI: 10.1007/s10886-009-9734-1
- URL: https://doi.org/10.1007/s10886-009-9734-1
- Categories: misleading_negative_pheromone, pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_negative_pheromone_probe, existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 31. The foraging ecology of the army ant Eciton rapax: an ergonomic enigma?

- Year: 1985
- Authors: JAMES L. BURTON, NIGEL R. FRANKS
- Venue: Ecological Entomology
- DOI: 10.1111/j.1365-2311.1985.tb00542.x
- URL: https://doi.org/10.1111/j.1365-2311.1985.tb00542.x
- Categories: pheromone_trail_foraging, nest_relocation_house_hunting, army_ant_raids_mills, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Eciton army ant raid trail pheromone`

### 32. A probabilistic cellular automata ant memory model for a swarm of foraging robots

- Year: 2016
- Authors: Danielli A. Lima, Gina M. B. Oliveira
- Venue: 2016 14th International Conference on Control, Automation, Robotics and Vision (ICARCV)
- DOI: 10.1109/icarcv.2016.7838615
- URL: https://doi.org/10.1109/icarcv.2016.7838615
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 33. Ants (Lasius niger) deposit more pheromone close to food sources and further from the nest but do not attempt to update erroneous pheromone trails

- Year: 2024
- Authors: Tomer J. Czaczkes, Federico-Javier Olivera-Rodriguez, Laure-Anne Poissonnier
- Venue: Insectes Sociaux
- DOI: 10.1007/s00040-024-00995-y
- URL: https://doi.org/10.1007/s00040-024-00995-y
- Categories: pheromone_trail_foraging, food_quality_choice, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Lasius niger food recruitment pheromone`

### 34. Aerosol delivery of trail pheromone disrupts the foraging of the red imported fire ant, <i>Solenopsis invicta</i>

- Year: 2012
- Authors: David Maxwell Suckling, Lloyd D Stringer, Joshua E Corn, Barry Bunn, et al.
- Venue: Pest Management Science
- DOI: 10.1002/ps.3349
- URL: https://doi.org/10.1002/ps.3349
- Categories: misleading_negative_pheromone, pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_negative_pheromone_probe, existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 35. Formal analysis in a cellular automata ant model using swarm intelligence in robotics foraging task

- Year: 2017
- Authors: Danielli A. Lima, Gina M. B. Oliveira
- Venue: 2017 IEEE International Conference on Systems, Man, and Cybernetics (SMC)
- DOI: 10.1109/smc.2017.8122876
- URL: https://doi.org/10.1109/smc.2017.8122876
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 36. Ant Colony Optimization Based Model Checking Extended by Smell-like Pheromone

- Year: 2016
- Authors: Tsutomu Kumazawa, Chihiro Yokoyama, Munehiro Takimoto, Yasushi Kambayashi
- Venue: EAI Endorsed Transactions on Industrial Networks and Intelligent Systems
- DOI: 10.4108/eai.21-4-2016.151156
- URL: https://doi.org/10.4108/eai.21-4-2016.151156
- Categories: pheromone_trail_foraging, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 37. Walk this way: modeling foraging ant dynamics in multiple food source environments

- Year: 2024
- Authors: Sean Hartman, Shawn D. Ryan, Bhargav R. Karamched
- Venue: Journal of Mathematical Biology
- DOI: 10.1007/s00285-024-02136-2
- URL: https://doi.org/10.1007/s00285-024-02136-2
- Categories: pheromone_trail_foraging, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging food quality recruitment`

### 38. A continuous model of ant foraging with pheromones and trail formation

- Year: 2015
- Authors: Paulo Amorim
- Venue: Proceeding Series of the Brazilian Society of Computational and Applied Mathematics
- DOI: 10.5540/03.2015.003.01.0323
- URL: https://doi.org/10.5540/03.2015.003.01.0323
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 39. Distributed Task Allocation in Network of Agents Based on Ant Colony Foraging Behavior

- Year: 2023
- Authors: Dorian Minarolli
- Venue: Proceedings of the 24th International Conference on Computer Systems and Technologies
- DOI: 10.1145/3606305.3606324
- URL: https://doi.org/10.1145/3606305.3606324
- Categories: pheromone_trail_foraging, task_allocation_division_labor, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 40. Avoiding traffic jams: Hitchhiking behavior as a strategy to reduce ant workers’ traffic on the foraging trail

- Year: 2018
- Authors: Isabel Neto Hastenreiter, Juliane Floriano Santos Lopes, Roberto da Silva Camargo, Luiz Carlos Forti
- Venue: Behavioural Processes
- DOI: 10.1016/j.beproc.2018.08.015
- URL: https://doi.org/10.1016/j.beproc.2018.08.015
- Categories: pheromone_trail_foraging, traffic_collective_motion
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 41. Effect of trail pheromones and weather on the moving behaviour of the army ant Eciton burchellii

- Year: 2011
- Authors: D. Califano, J. Chaves-Campos
- Venue: Insectes Sociaux
- DOI: 10.1007/s00040-010-0140-z
- URL: https://doi.org/10.1007/s00040-010-0140-z
- Categories: pheromone_trail_foraging, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe
- Source query: `Eciton army ant raid trail pheromone`

### 42. Delay-Induced Hopf Bifurcation and Entropy-Based Distributional Uncertainty in a Stochastic Time-Delay Pheromone Feedback Model of Ant Foraging Dynamics

- Year: 2026
- Authors: Jiaxin Zhu, Luyan Wang, Qiubao Wang
- Venue: Entropy
- DOI: 10.3390/e28070751
- URL: https://doi.org/10.3390/e28070751
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 43. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Year: 2026
- Authors: L.-A. Poissonnier, D. Winter, F.‑J. Olivera‑Rodriguez, C. Werneke, et al.
- Venue: Insectes Sociaux
- DOI: 10.1007/s00040-026-01106-9
- URL: https://doi.org/10.1007/s00040-026-01106-9
- Categories: pheromone_trail_foraging, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Lasius niger food recruitment pheromone`

### 44. Building a polydomous colony: nest network expansion by Linepithema humile

- Year: 2026
- Authors: P. Nonacs
- Venue: Insectes Sociaux
- DOI: 10.1007/s00040-026-01081-1
- URL: https://doi.org/10.1007/s00040-026-01081-1
- Categories: pheromone_trail_foraging, brood_nest_microclimate, nest_relocation_house_hunting, food_quality_choice, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, extend_brood_microclimate_probe, needs_food_quality_resource_model
- Source query: `Linepithema humile trail pheromone foraging`

### 45. Pheromone trail following is not modulated by previous visit to food location, distance travelled, or travel direction in the ant Lasius niger

- Year: 2025
- Authors: Laure-Anne Poissonnier, Delia Winter, Federico Federico-Javier Olivera-Rodriguez, Cosmina Werneke, et al.
- Venue: Springer Science and Business Media LLC
- DOI: 10.21203/rs.3.rs-7630446/v1
- URL: https://doi.org/10.21203/rs.3.rs-7630446/v1
- Categories: pheromone_trail_foraging, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Lasius niger food recruitment pheromone`

### 46. Stop and go: exploring alternative mechanisms for task allocation in social insects - response and satisfaction thresholds trade off cost, accuracy, and speed differently

- Year: 2024
- Authors: CM Lynch, RC Wilson, A Dornhaus
- Venue: openRxiv
- DOI: 10.1101/2024.05.13.593812
- URL: https://doi.org/10.1101/2024.05.13.593812
- Categories: pheromone_trail_foraging, task_allocation_division_labor, brood_nest_microclimate, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe, extend_brood_microclimate_probe
- Source query: `social insect task allocation ants response threshold`

### 47. Walk This Way: Modeling Foraging Ant Dynamics in Multiple Food Source Environments

- Year: 2024
- Authors: Sean Hartman, Shawn D. Ryan, Bhargav R. Karamched
- Venue: openRxiv
- DOI: 10.1101/2024.01.20.576461
- URL: https://doi.org/10.1101/2024.01.20.576461
- Categories: pheromone_trail_foraging, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant stochasticity foraging pheromone`

### 48. Ant traffic flow: Raiding swarms with few rules avoid gridlock

- Year: 2002
- Authors: Susan Milius
- Venue: Science News
- DOI: 10.2307/4013963
- URL: https://doi.org/10.2307/4013963
- Categories: traffic_collective_motion, army_ant_raids_mills, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 49. MODELING AND SIMULATION OF ANT COLONY'S LABOR DIVISION WITH CONSTRAINTS FOR TASK ALLOCATION OF RESILIENT SUPPLY CHAINS

- Year: 2012
- Authors: RENBIN XIAO, TONGYANG YU, XIAOGUANG GONG
- Venue: International Journal on Artificial Intelligence Tools
- DOI: 10.1142/s0218213012400143
- URL: https://doi.org/10.1142/s0218213012400143
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant division of labor task allocation model`

### 50. Chemical Releasers of Social Behavior—IV. The Hindgut as the Source of the Odor Trail Pheromone in the Neotropical Army Ant Genus Eciton1

- Year: 1964
- Authors: Murray S. Blum, Cesar A. Portocarrero
- Venue: Annals of the Entomological Society of America
- DOI: 10.1093/aesa/57.6.793
- URL: https://doi.org/10.1093/aesa/57.6.793
- Categories: pheromone_trail_foraging, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe
- Source query: `Eciton army ant raid trail pheromone`

### 51. Plastic collective endothermy in a complex animal society (army ant bivouacs: <i>Eciton burchellii parvispinum</i> )

- Year: 2019
- Authors: Kaitlin M. Baudier, Catherine L. D'Amelio, Elisabeth Sulger, Michael P. O'Connor, et al.
- Venue: Ecography
- DOI: 10.1111/ecog.04064
- URL: https://doi.org/10.1111/ecog.04064
- Categories: brood_nest_microclimate, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, extend_brood_microclimate_probe
- Source query: `army ant raid collective behavior model`

### 52. Multiple-Agent Task Allocation Algorithm Utilizing Ant Colony Optimization

- Year: 2013
- Authors: Kai Zhao
- Venue: Journal of Networks
- DOI: 10.4304/jnw.8.11.2599-2606
- URL: https://doi.org/10.4304/jnw.8.11.2599-2606
- Categories: task_allocation_division_labor, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 53. No evidence that recruitment pheromone modulates olfactory, visual, or spatial learning in the ant Lasius niger

- Year: 2024
- Authors: Alexandra Koch, Melanie Kabas, Tomer J. Czaczkes
- Venue: Behavioral Ecology and Sociobiology
- DOI: 10.1007/s00265-024-03430-1
- URL: https://doi.org/10.1007/s00265-024-03430-1
- Categories: pheromone_trail_foraging, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Lasius niger food recruitment pheromone`

### 54. Reduced foraging investment as an adaptation to patchy food sources: a phasic army ant simulation

- Year: 2017
- Authors: Serafino Teseo, Francesco Delloro
- Venue: openRxiv
- DOI: 10.1101/101600
- URL: https://doi.org/10.1101/101600
- Categories: pheromone_trail_foraging, brood_nest_microclimate, army_ant_raids_mills, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe, extend_brood_microclimate_probe
- Source query: `army ant raid collective behavior model`

### 55. Quorum sensing, recruitment, and collective decision-making during colony emigration by the ant Leptothorax albipennis

- Year: 2002
- Authors: Stephen Pratt, Eamonn Mallon, David Sumpter, Nigel Franks
- Venue: Behavioral Ecology and Sociobiology
- DOI: 10.1007/s00265-002-0487-x
- URL: https://doi.org/10.1007/s00265-002-0487-x
- Categories: pheromone_trail_foraging, nest_relocation_house_hunting
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant house hunting quorum decision`

### 56. Ant-like task allocation and recruitment in cooperative robots

- Year: 2000
- Authors: Michael J. B. Krieger, Jean-Bernard Billeter, Laurent Keller
- Venue: Nature
- DOI: 10.1038/35023164
- URL: https://doi.org/10.1038/35023164
- Categories: pheromone_trail_foraging, task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 57. From nonlinearity to optimality: pheromone trail foraging by ants

- Year: 2003
- Authors: David J.T Sumpter, Madeleine Beekman
- Venue: Animal Behaviour
- DOI: 10.1006/anbe.2003.2224
- URL: https://doi.org/10.1006/anbe.2003.2224
- Categories: pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 58. Trail geometry gives polarity to ant foraging networks

- Year: 2004
- Authors: Duncan E. Jackson, Mike Holcombe, Francis L. W. Ratnieks
- Venue: Nature
- DOI: 10.1038/nature03105
- URL: https://doi.org/10.1038/nature03105
- Categories: pheromone_trail_foraging, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 59. The blind leading the blind in army ant raid patterns: Testing a model of self-organization (Hymenoptera: Formicidae)

- Year: 1991
- Authors: N. R. Franks, N. Gomez, S. Goss, J. L. Deneubourg
- Venue: Journal of Insect Behavior
- DOI: 10.1007/bf01048072
- URL: https://doi.org/10.1007/bf01048072
- Categories: army_ant_raids_mills, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe
- Source query: `army ant raid collective behavior model`

### 60. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Year: 1993
- Authors: Chris Tofts
- Venue: Bulletin of Mathematical Biology
- DOI: 10.1007/bf02460691
- URL: https://doi.org/10.1007/bf02460691
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `social insect task allocation ants response threshold`

### 61. Multi-robot Task Allocation Based on Ant Colony Algorithm

- Year: 2012
- Authors: Jianping Wang, Yuesheng Gu, Xiaomin Li
- Venue: Journal of Computers
- DOI: 10.4304/jcp.7.9.2160-2167
- URL: https://doi.org/10.4304/jcp.7.9.2160-2167
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 62. Spatial and temporal variation in pheromone composition of ant foraging trails

- Year: 2007
- Authors: D. E. Jackson, S. J. Martin, F. L. W. Ratnieks, M. Holcombe
- Venue: Behavioral Ecology
- DOI: 10.1093/beheco/arl104
- URL: https://doi.org/10.1093/beheco/arl104
- Categories: pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 63. A connectionist type model of self-organized foraging and emergent behavior in ant swarms

- Year: 1992
- Authors: Mark M. Millonas
- Venue: Journal of Theoretical Biology
- DOI: 10.1016/s0022-5193(05)80697-6
- URL: https://doi.org/10.1016/s0022-5193(05)80697-6
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 64. Pheromone Disruption of Argentine Ant Trail Integrity

- Year: 2008
- Authors: D. M. Suckling, R. W. Peck, L. M. Manning, L. D. Stringer, et al.
- Venue: Journal of Chemical Ecology
- DOI: 10.1007/s10886-008-9566-4
- URL: https://doi.org/10.1007/s10886-008-9566-4
- Categories: misleading_negative_pheromone, pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_negative_pheromone_probe, existing_or_extend_trail_probe
- Source query: `Argentine ant trail pheromone foraging`

### 65. Colony size does not predict foraging distance in the ant Temnothorax rugatulus: a puzzle for standard scaling models

- Year: 2013
- Authors: S. E. Bengston, A. Dornhaus
- Venue: Insectes Sociaux
- DOI: 10.1007/s00040-012-0272-4
- URL: https://doi.org/10.1007/s00040-012-0272-4
- Categories: pheromone_trail_foraging, food_quality_choice, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `ant foraging distance food quality pheromone`

### 66. Consensus decision making in the ant Myrmecina nipponica: house-hunters combine pheromone trails with quorum responses

- Year: 2012
- Authors: Adam L. Cronin
- Venue: Animal Behaviour
- DOI: 10.1016/j.anbehav.2012.08.036
- URL: https://doi.org/10.1016/j.anbehav.2012.08.036
- Categories: pheromone_trail_foraging, nest_relocation_house_hunting
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant house hunting quorum decision`

### 67. Argentine Ant (Hymenoptera: Formicidae) Trail Pheromone Enhances Consumption of Liquid Sucrose Solution

- Year: 2000
- Authors: Les Greenberg, John H. Klotz
- Venue: Journal of Economic Entomology
- DOI: 10.1603/0022-0493-93.1.119
- URL: https://doi.org/10.1603/0022-0493-93.1.119
- Categories: pheromone_trail_foraging, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Argentine ant trail pheromone foraging`

### 68. Movement, Encounter Rate, and Collective Behavior in Ant Colonies

- Year: 2021
- Authors: Deborah M Gordon
- Venue: Annals of the Entomological Society of America
- DOI: 10.1093/aesa/saaa036
- URL: https://doi.org/10.1093/aesa/saaa036
- Categories: traffic_collective_motion, task_allocation_division_labor, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe, existing_traffic_density_probe
- Source query: `army ant raid collective behavior model`

### 69. Response thresholds to recruitment signals and the regulation of foraging intensity in the ant Myrmica sabuleti (Hymenoptera, Formicidae)

- Year: 2000
- Authors: Jean-Christophe de Biseau, Jacques M. Pasteels
- Venue: Behavioural Processes
- DOI: 10.1016/s0376-6357(99)00077-7
- URL: https://doi.org/10.1016/s0376-6357(99)00077-7
- Categories: pheromone_trail_foraging, task_allocation_division_labor
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_task_demand_probe
- Source query: `ant foraging food quality recruitment`

### 70. Foraging energetics of a nectar-feeding ant: metabolic expenditure as a function of food-source profitability

- Year: 2006
- Authors: Pablo E. Schilman, Flavio Roces
- Venue: Journal of Experimental Biology
- DOI: 10.1242/jeb.02478
- URL: https://doi.org/10.1242/jeb.02478
- Categories: pheromone_trail_foraging, traffic_collective_motion, food_quality_choice, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, existing_traffic_density_probe, needs_food_quality_resource_model
- Source query: `ant foraging food quality recruitment`

### 71. Coordination of Raiding and Emigration in the Ponerine Army Ant Leptogenys distinguenda (Hymenoptera: Formicidae: Ponerinae): A Signal Analysis

- Year: 2002
- Authors: V. Witte, U. Maschwitz
- Venue: Journal of Insect Behavior
- DOI: 10.1023/a:1015484917019
- URL: https://doi.org/10.1023/a:1015484917019
- Categories: nest_relocation_house_hunting, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe
- Source query: `army ant raid collective behavior model`

### 72. Notes on an army ant (<i>Eciton burchelli</i>) raid on a social wasp colony (<i>Agelaia yepocapa</i>) in Costa Rica

- Year: 1990
- Authors: Sean O'Donnell, Robert L. Jeanne
- Venue: Journal of Tropical Ecology
- DOI: 10.1017/s0266467400004958
- URL: https://doi.org/10.1017/s0266467400004958
- Categories: army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe
- Source query: `army ant raid collective behavior model`

### 73. First identification of a trail pheromone of an army ant (Aenictus species)

- Year: 1994
- Authors: N. J. Oldham, E. D. Morgan, B. Gobin, J. Billen
- Venue: Experientia
- DOI: 10.1007/bf01919378
- URL: https://doi.org/10.1007/bf01919378
- Categories: pheromone_trail_foraging, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe
- Source query: `ant tropotaxis pheromone trail`

### 74. Effect of Trail Bifurcation Asymmetry and Pheromone Presence or Absence on Trail Choice by <i>Lasius niger</i> Ants

- Year: 2014
- Authors: Antonia Forster, Tomer J. Czaczkes, Emma Warner, Tom Woodall, et al.
- Venue: Ethology
- DOI: 10.1111/eth.12248
- URL: https://doi.org/10.1111/eth.12248
- Categories: pheromone_trail_foraging, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `Lasius niger food recruitment pheromone`

### 75. Evolving neural networks using ant colony optimization with pheromone trail limits

- Year: 2013
- Authors: Michalis Mavrovouniotis, Shengxiang Yang
- Venue: 2013 13th UK Workshop on Computational Intelligence (UKCI)
- DOI: 10.1109/ukci.2013.6651282
- URL: https://doi.org/10.1109/ukci.2013.6651282
- Categories: pheromone_trail_foraging, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 76. Argentine Ant Trail Pheromone Disruption is Mediated by Trail Concentration

- Year: 2011
- Authors: David Maxwell Suckling, Lloyd D. Stringer, Joshua E. Corn
- Venue: Journal of Chemical Ecology
- DOI: 10.1007/s10886-011-0019-0
- URL: https://doi.org/10.1007/s10886-011-0019-0
- Categories: misleading_negative_pheromone, pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_negative_pheromone_probe, existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 77. Food recruitment as a component of the trunk-trail foraging behaviour of Lasius fuliginosus (Hymenoptera: Formicidae)

- Year: 1997
- Authors: Yves Quinet, Jean-Christophe de Biseau, Jacques M Pasteels
- Venue: Behavioural Processes
- DOI: 10.1016/s0376-6357(97)00773-0
- URL: https://doi.org/10.1016/s0376-6357(97)00773-0
- Categories: pheromone_trail_foraging
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `Lasius niger food recruitment pheromone`

### 78. An Improvement in ant Algorithm Method for Optimizing a Transport Route with Regard to Traffic Flow

- Year: 2017
- Authors: Viktor Danchuk, Olena Bakulich, Vitaliy Svatko
- Venue: Procedia Engineering
- DOI: 10.1016/j.proeng.2017.04.396
- URL: https://doi.org/10.1016/j.proeng.2017.04.396
- Categories: traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 79. Elevational and geographic variation in army ant swarm raid rates

- Year: 2011
- Authors: S. O’Donnell, M. Kaspari, A. Kumar, J. Lattke, et al.
- Venue: Insectes Sociaux
- DOI: 10.1007/s00040-010-0129-7
- URL: https://doi.org/10.1007/s00040-010-0129-7
- Categories: army_ant_raids_mills, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe
- Source query: `army ant raid collective behavior model`

### 80. Interactions and information: exploring task allocation in ant colonies using network analysis

- Year: 2022
- Authors: Anshuman Swain, Sara D. Williams, Louisa J. Di Felice, Elizabeth A. Hobson
- Venue: Animal Behaviour
- DOI: 10.1016/j.anbehav.2022.04.015
- URL: https://doi.org/10.1016/j.anbehav.2022.04.015
- Categories: task_allocation_division_labor, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant social insect network task allocation`

### 81. Decentralized communication, trail connectivity and emergent benefits of ant pheromone trail networks

- Year: 2011
- Authors: Duncan E. Jackson, Mesude Bicak, Mike Holcombe
- Venue: Memetic Computing
- DOI: 10.1007/s12293-010-0039-2
- URL: https://doi.org/10.1007/s12293-010-0039-2
- Categories: pheromone_trail_foraging, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 82. Research on task allocation in multiple logistics robots based on an improved ant colony algorithm

- Year: 2016
- Authors: Juntao Li, Tingting Dong, Yuanyuan Li
- Venue: 2016 International Conference on Robotics and Automation Engineering (ICRAE)
- DOI: 10.1109/icrae.2016.7738780
- URL: https://doi.org/10.1109/icrae.2016.7738780
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 83. Multi-Agent Cooperation Using the Ant Algorithm with Variable Pheromone Placement

- Year: 2005
- Authors: E. Borzello, L.D. Merkle
- Venue: 2005 IEEE Congress on Evolutionary Computation
- DOI: 10.1109/cec.2005.1554831
- URL: https://doi.org/10.1109/cec.2005.1554831
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant double bridge experiment pheromone`

### 84. Trail Pheromone Does Not Modulate Subjective Reward Evaluation in Lasius niger Ants

- Year: 2020
- Authors: Felix B. Oberhauser, Stephanie Wendt, Tomer J. Czaczkes
- Venue: Frontiers in Psychology
- DOI: 10.3389/fpsyg.2020.555576
- URL: https://doi.org/10.3389/fpsyg.2020.555576
- Categories: pheromone_trail_foraging, food_quality_choice
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `Lasius niger food recruitment pheromone`

### 85. Optimal ant colony algorithm based multi-robot task allocation and processing sequence scheduling

- Year: 2008
- Authors: Taixiong Zheng, Liangyi Yang
- Venue: 2008 7th World Congress on Intelligent Control and Automation
- DOI: 10.1109/wcica.2008.4593859
- URL: https://doi.org/10.1109/wcica.2008.4593859
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 86. A single-pheromone model accounts for empirical patterns of ant colony foraging previously modeled using two pheromones

- Year: 2023
- Authors: Eric Saund, Daniel Ari Friedman
- Venue: Cognitive Systems Research
- DOI: 10.1016/j.cogsys.2023.02.005
- URL: https://doi.org/10.1016/j.cogsys.2023.02.005
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 87. Algorithms for task allocation in ants. (A study of temporal polyethism: Theory)

- Year: 1993
- Authors: C TOFTS
- Venue: Bulletin of Mathematical Biology
- DOI: 10.1016/s0092-8240(05)80195-8
- URL: https://doi.org/10.1016/s0092-8240(05)80195-8
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `social insect task allocation ants response threshold`

### 88. Social organization of necrophoresis: insights into disease risk management in ant societies

- Year: 2024
- Authors: Quentin Avanzi, Léon Lisart, Claire Detrain
- Venue: Royal Society Open Science
- DOI: 10.1098/rsos.240764
- URL: https://doi.org/10.1098/rsos.240764
- Categories: necrophoresis_social_immunity, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: extend_corpse_cleanup_probe
- Source query: `ant necrophoresis corpse removal chemical`

### 89. Improved Intelligent Method for Traffic Flow Prediction Based on Artificial Neural Networks and Ant Colony Optimization

- Year: 2012
- Authors: Lingling Song -
- Venue: Journal of Convergence Information Technology
- DOI: 10.4156/jcit.vol7.issue8.31
- URL: https://doi.org/10.4156/jcit.vol7.issue8.31
- Categories: traffic_collective_motion, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 90. Research on Improvement of Ant Colony Algorithm for Multi-Robot Task Allocation

- Year: 2019
- Authors: Xu Li, Zhengyan Liu
- Venue: 2019 IEEE 8th Joint International Information Technology and Artificial Intelligence Conference (ITAIC)
- DOI: 10.1109/itaic.2019.8785605
- URL: https://doi.org/10.1109/itaic.2019.8785605
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 91. Modeling Ant Nest Relocation at Low Active Ratio by Particle Swarm Optimization

- Year: 2019
- Authors: Hideyasu Sasaki
- Venue: 2019 IEEE Congress on Evolutionary Computation (CEC)
- DOI: 10.1109/cec.2019.8789942
- URL: https://doi.org/10.1109/cec.2019.8789942
- Categories: nest_relocation_house_hunting, computational_swarm_model
- Readiness: `needs_new_condition`
- Candidate test mapping: none
- Source query: `ant nest relocation quorum Temnothorax`

### 92. Novel observation of a raptor, Collared Forest-falcon ( <i>Micrastur semitorquatus</i> ), depredating a fleeing snake at an army ant ( <i>Eciton burchellii parvispinum</i> ) raid front

- Year: 2018
- Authors: Robert J. Driver, Sara DeLeon, Sean O'Donnell
- Venue: The Wilson Journal of Ornithology
- DOI: 10.1676/1559-4491-130.3.792
- URL: https://doi.org/10.1676/1559-4491-130.3.792
- Categories: army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe
- Source query: `army ant raid collective behavior model`

### 93. Induced biotic response in Amazonian ant-plants: the role of leaf damage intensity and plant-derived food rewards on ant recruitment

- Year: 2016
- Authors: Thiago Gonçalves-Souza
- Venue: Sociobiology
- DOI: 10.13102/sociobiology.v63i3.1050
- URL: https://doi.org/10.13102/sociobiology.v63i3.1050
- Categories: pheromone_trail_foraging, food_quality_choice, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, needs_food_quality_resource_model
- Source query: `ant foraging food quality recruitment`

### 94. Deterministic Model for Analyzing the Dynamics of Ant System Algorithm and Performance Amelioration through a New Pheromone Deposition Approach

- Year: 2008
- Authors: Ayan Acharya, Deepyaman Maiti, Amit Konar, Janarthanan Ramadoss
- Venue: 2008 4th International Conference on Information and Automation for Sustainability
- DOI: 10.1109/iciafs.2008.4783979
- URL: https://doi.org/10.1109/iciafs.2008.4783979
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 95. The emergence of a collective sensory response threshold in ant colonies

- Year: 2021
- Authors: Asaf Gal, Daniel J. C. Kronauer
- Venue: openRxiv
- DOI: 10.1101/2021.10.30.466564
- URL: https://doi.org/10.1101/2021.10.30.466564
- Categories: task_allocation_division_labor, brood_nest_microclimate, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe, extend_brood_microclimate_probe
- Source query: `ant task allocation response threshold`

### 96. Optimal A* Path Planning with Ant Colony Optimization on Multi-Robot Task Allocation for Manufacturing Model

- Year: 2021
- Authors: Rawinun Praserttaweelap, Somyot Kiatwanidvilai
- Venue: 2021 IEEE 8th International Conference on Industrial Engineering and Applications (ICIEA)
- DOI: 10.1109/iciea52957.2021.9436716
- URL: https://doi.org/10.1109/iciea52957.2021.9436716
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant division of labor task allocation model`

### 97. A Novel Improved Ant Colony Algorithm for Multi-Robot Task Allocation

- Year: 2018
- Authors: Xu Li, Zhengyan Liu, Yan Zhang
- Venue: 2018 IEEE 4th Information Technology and Mechatronics Engineering Conference (ITOEC)
- DOI: 10.1109/itoec.2018.8740438
- URL: https://doi.org/10.1109/itoec.2018.8740438
- Categories: task_allocation_division_labor, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant task allocation response threshold`

### 98. Reduced foraging investment as an adaptation to patchy food sources: A phasic army ant simulation

- Year: 2017
- Authors: Serafino Teseo, Francesco Delloro
- Venue: Journal of Theoretical Biology
- DOI: 10.1016/j.jtbi.2017.06.009
- URL: https://doi.org/10.1016/j.jtbi.2017.06.009
- Categories: pheromone_trail_foraging, army_ant_raids_mills, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe
- Source query: `ant foraging food quality recruitment`

### 99. Ant Colony Algorithm in Traffic Flow Control

- Year: 2024
- Authors: Andrii Danyliuk, Oleksandr Muliarevych
- Venue: Advances in Cyber-Physical Systems
- DOI: 10.23939/acps2024.02.158
- URL: https://doi.org/10.23939/acps2024.02.158
- Categories: traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 100. Graph Convolutional Network Based Ant Colony Optimization for Robot Task Allocation

- Year: 2023
- Authors: Jiang Qiu, Yi Liu, Yilan Yu, Wei Li
- Venue: 2023 IEEE Symposium Series on Computational Intelligence (SSCI)
- DOI: 10.1109/ssci52147.2023.10372050
- URL: https://doi.org/10.1109/ssci52147.2023.10372050
- Categories: task_allocation_division_labor, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant social insect network task allocation`

### 101. Ant Colony Optimization Algorithm for Traffic Flow Estimation

- Year: 2017
- Authors: Milena Karova, Nikola Vasilev, Ivaylo Penev
- Venue: Proceedings of the 18th International Conference on Computer Systems and Technologies
- DOI: 10.1145/3134302.3134317
- URL: https://doi.org/10.1145/3134302.3134317
- Categories: traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 102. Traffic Flow Estimation Using Ant Colony Optimization Algorithms

- Year: 2014
- Authors: Antonio Bolufe Rohler, Juan Manuel Otero Pereira, Sonia Fiol-González
- Venue: Computación y Sistemas
- DOI: 10.13053/cys-18-1-2014-017
- URL: https://doi.org/10.13053/cys-18-1-2014-017
- Categories: traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 103. Hybrid Algorithm Based on Ant and Genetic Algorithms for Task Allocation on a Network of Homogeneous Processors

- Year: 2014
- Authors: Sawsan Yousef Abu Shuqeir, Tamara Amjad Al Qublan
- Venue: International journal of Computer Networks &amp; Communications
- DOI: 10.5121/ijcnc.2014.6113
- URL: https://doi.org/10.5121/ijcnc.2014.6113
- Categories: task_allocation_division_labor, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_task_demand_probe
- Source query: `ant social insect network task allocation`

### 104. Ant System Algorithm with Negative Pheromone for Course Scheduling Problem

- Year: 2008
- Authors: Djasli Djamarus, Ku Ruhana Ku-Mahamud
- Venue: 2008 Eighth International Conference on Intelligent Systems Design and Applications
- DOI: 10.1109/isda.2008.154
- URL: https://doi.org/10.1109/isda.2008.154
- Categories: misleading_negative_pheromone, pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_negative_pheromone_probe, existing_or_extend_trail_probe
- Source query: `ant negative pheromone foraging`

### 105. Dynamics of ant activity under extreme climatic changes in 2024: effects of temperature and humidity on Formica rufa and Lasius fuliginosus behavior

- Year: 2026
- Authors: STANISLAV STUKALYUK, MYKOLA KOZYR, VIRA BALABUKH
- Venue: Turkish Journal of Zoology
- DOI: 10.55730/1300-0179.3265
- URL: https://doi.org/10.55730/1300-0179.3265
- Categories: pheromone_trail_foraging, brood_nest_microclimate
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe, extend_brood_microclimate_probe
- Source query: `ant brood care temperature humidity`

### 106. An Ensemble Ant Colony Optimization Algorithm with a Hybrid Pheromone Model for Learning Rule Lists

- Year: 2025
- Authors: James Brookhouse, Ayah Helal, Fernando Otero
- Venue: Proceedings of the Genetic and Evolutionary Computation Conference
- DOI: 10.1145/3712256.3726427
- URL: https://doi.org/10.1145/3712256.3726427
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant foraging pheromone model`

### 107. ANTi-JAM solutions for smart roads: Ant-inspired traffic flow rules under CAVs environment

- Year: 2025
- Authors: Marco Guerrieri, Nicola Pugno
- Venue: Transportation Research Interdisciplinary Perspectives
- DOI: 10.1016/j.trip.2025.101331
- URL: https://doi.org/10.1016/j.trip.2025.101331
- Categories: traffic_collective_motion
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant trail traffic jam density`

### 108. Pheromone representation in the ant antennal lobe changes with age

- Year: 2024
- Authors: Taylor Hart, Lindsey E. Lopes, Dominic D. Frank, Daniel J.C. Kronauer
- Venue: openRxiv
- DOI: 10.1101/2024.02.13.580193
- URL: https://doi.org/10.1101/2024.02.13.580193
- Categories: pheromone_trail_foraging, task_allocation_division_labor, army_ant_raids_mills
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe, existing_task_demand_probe
- Source query: `ant double bridge experiment pheromone`

### 109. Anti-Jam Solutions for Smart Roads: Ant-Inspired Traffic Flow Rules Under Cooperative Automated Vehicles Environment

- Year: 2024
- Authors: MARCO GUERRIERI, Nicola Pugno
- Venue: Elsevier BV
- DOI: 10.2139/ssrn.4701534
- URL: https://doi.org/10.2139/ssrn.4701534
- Categories: traffic_collective_motion
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 110. Research on Improved Ant Colony Path Planning Algorithm for Updating Pheromone of Subway Inspection Mobile Robot

- Year: 2023
- Authors: Lina Wang, Xin Yang, Zeling Chen, Binrui Wang
- Venue: Elsevier BV
- DOI: 10.2139/ssrn.4623370
- URL: https://doi.org/10.2139/ssrn.4623370
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant colony foraging model pheromone`

### 111. Optimization Design of Expressway Traffic Flow Guidance System Based on GIS and Improved Ant Colony Optimization Algorithms

- Year: 2023
- Authors: Xiaoying Xia, E Jing
- Venue: 2023 International Conference on Telecommunications, Electronics and Informatics (ICTEI)
- DOI: 10.1109/ictei60496.2023.00104
- URL: https://doi.org/10.1109/ictei60496.2023.00104
- Categories: traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 112. Role of the pheromone for orientation in the group foraging ant, Veromessor pergandei

- Year: 2020
- Authors: Cody A Freas, Marcia L Spetch
- Venue: Center for Open Science
- DOI: 10.31219/osf.io/w2rn4
- URL: https://doi.org/10.31219/osf.io/w2rn4
- Categories: pheromone_trail_foraging, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant pheromone trail foraging`

### 113. Modeling Fast and Robust Ant Nest Relocation using Particle Swarm Optimization

- Year: 2019
- Authors: Hideyasu Sasaki
- Venue: The 2019 Conference on Artificial Life
- DOI: 10.1162/isal_a_00231
- URL: https://doi.org/10.1162/isal_a_00231
- Categories: nest_relocation_house_hunting, computational_swarm_model
- Readiness: `needs_new_condition`
- Candidate test mapping: none
- Source query: `ant nest relocation quorum Temnothorax`

### 114. Optimal construction of army ant living bridges

- Year: 2017
- Authors: Jason M. Graham, Albert B. Kao, Dylana A. Wilhelm, Simon Garnier
- Venue: openRxiv
- DOI: 10.1101/116780
- URL: https://doi.org/10.1101/116780
- Categories: pheromone_trail_foraging, army_ant_raids_mills, networks_interactions, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe, existing_or_extend_trail_probe
- Source query: `army ant raid collective behavior model`

### 115. Fault Pheromone Trail Evaporation of Power Distribution Networks using Ant Colony Optimization

- Year: 2014
- Authors: Ramesh Gamasu, Venkata Ramesh Babu Jasti
- Venue: International Journal of Hybrid Information Technology
- DOI: 10.14257/ijhit.2014.7.1.07
- URL: https://doi.org/10.14257/ijhit.2014.7.1.07
- Categories: pheromone_trail_foraging, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant tropotaxis pheromone trail`

### 116. Traffic Flow Estimation Using Ant Colony Optimization Algorithms

- Year: 2014
- Authors: Antonio Bolufe Rohler, Juan Manuel Otero Pereira, Sonia Fiol-González
- Venue: Computación y Sistemas
- DOI: 10.13053/cys-18-1-1581
- URL: https://doi.org/10.13053/cys-18-1-1581
- Categories: traffic_collective_motion, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 117. Pheromone-Based Ant Colony Algorithm for Optimal Proliferation of Research

- Year: 2013
- Authors: Lei Lei Deng
- Venue: Advanced Materials Research
- DOI: 10.4028/www.scientific.net/amr.734-737.3152
- URL: https://doi.org/10.4028/www.scientific.net/amr.734-737.3152
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant colony foraging model pheromone`

### 118. Ant Colony Algorithm Based on Dynamic Adaptive Pheromone Updating and Its Simulation

- Year: 2013
- Authors: Guiqing Liu, Juxia Xiong
- Venue: 2013 Sixth International Symposium on Computational Intelligence and Design
- DOI: 10.1109/iscid.2013.62
- URL: https://doi.org/10.1109/iscid.2013.62
- Categories: pheromone_trail_foraging, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_trail_probe
- Source query: `ant colony foraging model pheromone`

### 119. Traffic flow forecasting based on ant colony neural network

- Year: 2010
- Authors: Qingle Pang, Min Zhang
- Venue: 2010 8th World Congress on Intelligent Control and Automation
- DOI: 10.1109/wcica.2010.5554931
- URL: https://doi.org/10.1109/wcica.2010.5554931
- Categories: traffic_collective_motion, networks_interactions
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_traffic_density_probe
- Source query: `ant traffic trail density flow`

### 120. The blind leading the blind: Modeling chemically mediated army ant raid patterns

- Year: 1989
- Authors: J. L. Deneubourg, S. Goss, N. Franks, J. M. Pasteels
- Venue: Journal of Insect Behavior
- DOI: 10.1007/bf01065789
- URL: https://doi.org/10.1007/bf01065789
- Categories: army_ant_raids_mills, computational_swarm_model
- Readiness: `direct_or_near_term`
- Candidate test mapping: existing_or_extend_ant_mill_probe
- Source query: `army ant raid collective behavior model`
