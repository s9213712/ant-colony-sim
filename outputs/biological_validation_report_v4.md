# Ant-Colony-Sim Biological Validation Report

- model_version: `0.5-adaptive-stochasticity`
- seeds: `8`
- source_csv: `ant_colony_sim/outputs/stochasticity_probe_v4.csv`
- interpretation: `partial: diverse exceeds low on early relocation ratio, while medium is not clearly separated`

## Stochasticity Relocation Probe

This probe is a qualitative comparison against Shiraishi-style diverse stochasticity, not a fitted reproduction of the paper's optimum curve.

### Early Relocation Adaptation

| profile | n | mean trips | trip ratio vs initial | 95% CI | mean traffic | mean exploration drive |
|---|---:|---:|---:|---:|---:|---:|
| diverse | 8 | 11.00 | 0.522 | 0.331-0.714 | 0.104 | 0.103 |
| high | 8 | 4.12 | 0.249 | 0.152-0.346 | 0.004 | 0.017 |
| low | 8 | 30.75 | 0.368 | 0.270-0.466 | 0.290 | 0.235 |
| medium | 8 | 6.50 | 0.372 | 0.218-0.527 | 0.090 | 0.092 |

### Total Relocation Exploitation

| profile | n | mean trips | trip ratio vs initial | 95% CI | mean traffic | mean exploration drive |
|---|---:|---:|---:|---:|---:|---:|
| diverse | 8 | 79.75 | 3.812 | 2.798-4.826 | 0.098 | 0.065 |
| high | 8 | 49.12 | 3.091 | 2.548-3.635 | 0.004 | 0.004 |
| low | 8 | 113.38 | 1.314 | 1.079-1.550 | 0.324 | 0.186 |
| medium | 8 | 36.38 | 1.995 | 1.482-2.508 | 0.136 | 0.093 |

## Scientific Boundary

- Supports: qualitative study of how stochasticity, traffic, memory decay and pheromone feedback interact.
- Does not support: numerical prediction of real ant foraging rates or species-specific parameter claims.
- Current strongest result: diverse stochasticity can exceed low-noise colonies on early relocation adaptation ratio.
- Current unresolved gap: medium stochasticity is not consistently above low in the adaptive-noise v4 run, so the published optimum-shift pattern is not fully reproduced.
