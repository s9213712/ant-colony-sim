# Model Rules and Validation Boundary

This simulator should be calibrated through general biological rules, not paper-specific exceptions.

## General Rules

- Resource value changes foraging utility, memory strength and recruitment signal strength. A food source with higher quality should tend to produce stronger recruitment, but path geometry and early discovery can still affect trip counts.
- Pheromone fields are shared chemical signals with diffusion, evaporation and thresholded sensing. Validation conditions may place sources differently, but the pheromone update equations must stay common.
- Brood care regulates nest microclimate through worker presence, stored water and brood-stage thermal demand. Pupal-heavy brood can justify stronger thermoregulation than larval-heavy brood under cold stress.
- Extreme heat, dryness and low water stores raise brood stress and can reduce brood development or survival.
- Nest relocation uses general house-hunting rules: scouts evaluate candidate nest quality, visits accumulate social evidence, quorum triggers transport, and relocation completes only after enough brood/queen transport effort.
- Corpse removal uses death/corpse chemical cues and worker cleanup behavior. The same mechanism applies to normal deaths and mass mortality.

## Validation Conditions

Validation scripts may set parameters, initial conditions and environmental states such as food quality, temperature, humidity, corpse count, brood composition or candidate nest sites. These are experimental conditions, not special-case model rules.

Validation scripts must not change per-ant decision rules, overwrite ant task/state to force an outcome, patch simulation functions at runtime, or add behavior that exists only inside a paper probe. If a paper reveals a missing mechanism, the mechanism belongs in the general simulator rules first, then the paper probe can test it by changing conditions.

Counterbalanced tests, such as swapping high- and low-quality food positions, are allowed because they remove spatial bias. They must not change the underlying ant decision rules between treatments.

## Current Boundary

Passing a paper-condition probe means qualitative alignment under these shared rules. It does not mean the simulator has fitted the original paper's numeric parameters, species-specific physiology or full individual trajectory data.
