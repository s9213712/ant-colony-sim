# Headless Experiments

`batch_runner.py` 用於可重現批量實驗。它會啟動本機 HTTP server、用 Playwright 載入模擬器、固定 seed、跑指定天數，輸出時間序列 CSV 與 metadata JSON。

## Smoke Test

```bash
python3 ant_colony_sim/experiments/batch_runner.py \
  --scenario mature_supplied \
  --seeds 1-2 \
  --days 1 \
  --output /tmp/ant_batch_smoke.csv
```

## Example: Pheromone Sensitivity

```bash
python3 ant_colony_sim/experiments/batch_runner.py \
  --scenario mature_supplied \
  --seeds 1-30 \
  --days 10 \
  --set diffusionRate=100 \
  --set evaporationRate=100 \
  --output ant_colony_sim/outputs/mature_supplied_baseline.csv
```

```bash
python3 ant_colony_sim/experiments/batch_runner.py \
  --scenario mature_supplied \
  --seeds 1-30 \
  --days 10 \
  --set diffusionRate=160 \
  --set evaporationRate=140 \
  --output ant_colony_sim/outputs/mature_supplied_fast_decay.csv
```

## Scientific Use

Use this runner for:

- multi-seed Monte Carlo checks;
- sensitivity analysis;
- exporting comparable time series;
- validation cases described in `BIOLOGICAL_VALIDATION.md`.

Do not treat a single run as biological evidence.

## Actual Biology Simulation Suite

Run behavior-level biological scenarios with fixed seeds and shared simulator
rules:

```bash
python3 ant_colony_sim/experiments/actual_biology_simulation.py \
  --output ant_colony_sim/outputs/actual_biology_simulation.csv \
  --json-output ant_colony_sim/outputs/actual_biology_simulation.json \
  --report-output ant_colony_sim/outputs/actual_biology_simulation.md
```

The current suite runs four scenarios:

- `stable_mature`: mature Lasius-like colony with nearby food/water access and moderate store pressure.
- `resource_stress`: mature colony with low stores and limited distant resources.
- `heat_dry_stress`: mature colony under high temperature and low humidity.
- `founding_colony`: queen-centered early colony with no initial worker population.

Current `v1` result with seeds `101-105`, 8 simulated days and 0.25-day
sampling:

- all five qualitative checks pass: stable foraging, stable survival, resource-pressure response, heat/dry hydration or brood stress response, and founding queen viability;
- stable mature colonies complete food and water trips under explicit resource access;
- heat/dry stress raises brood stress relative to the stable control;
- resource stress lowers mean energy/hydration relative to the stable control;
- founding mode remains queen-centered and produces only early brood/rare first-worker dynamics over this short model-time window.

Use this suite when the question is whether the simulator produces interpretable
biological time series under controlled conditions. It is not a digitized
paper-curve fitting suite and it is not a quantitative species predictor.

## Actual Biology Sensitivity Suite

Run a local parameter-sensitivity screen on the biological scenarios:

```bash
python3 ant_colony_sim/experiments/actual_biology_sensitivity.py \
  --output ant_colony_sim/outputs/actual_biology_sensitivity.csv \
  --effects-output ant_colony_sim/outputs/actual_biology_sensitivity_effects.csv \
  --json-output ant_colony_sim/outputs/actual_biology_sensitivity.json \
  --report-output ant_colony_sim/outputs/actual_biology_sensitivity.md
```

The current `v1` screen uses seeds `101-103`, 4 simulated days and three
scenarios: `stable_mature`, `resource_stress`, `heat_dry_stress`.

Treatments:

- `baseline`: current behavior-level defaults.
- `fast_pheromone_loss`: `evaporationRate=130`, `senseThreshold=16`.
- `persistent_pheromone`: `evaporationRate=55`, `senseThreshold=7`.
- `calibrated_persistent_pheromone`: `evaporationRate=70`, `senseThreshold=8`.
- `high_diffusion`: `diffusionRate=170`.
- `brood_demand_high`: `broodDemand=85`.

Current largest effects:

- `persistent_pheromone` under `heat_dry_stress`: food trips `-0.221`, hydration `-0.026`, brood stress `+0.175`, peak food pheromone `+0.686`.
- `persistent_pheromone` under `resource_stress`: food trips `-0.259`, hydration `-0.011`, brood stress `+0.056`.
- `calibrated_persistent_pheromone` under `heat_dry_stress`: food trips `+0.151`, brood stress `+0.062`, peak food pheromone `+0.599`.
- `high_diffusion` under `heat_dry_stress`: food trips `+0.244`, peak food pheromone `+0.140`.

Interpretation: the next biological calibration priority is pheromone
persistence/sensing, because those parameters move foraging and brood-stress
outputs across multiple stress scenarios. Treat this as a sensitivity screen,
not a fitted optimum.

## Literature Calibration Cycle

Evaluate the latest sensitivity effects against literature-guided constraints:

```bash
python3 ant_colony_sim/experiments/literature_calibration_cycle.py \
  --targets ant_colony_sim/targets/literature_pheromone_constraints.json \
  --effects ant_colony_sim/outputs/actual_biology_sensitivity_effects.csv \
  --csv-output ant_colony_sim/outputs/literature_calibration_cycle.csv \
  --json-output ant_colony_sim/outputs/literature_calibration_cycle.json \
  --report-output ant_colony_sim/outputs/literature_calibration_cycle.md
```

Current cycle result:

- total constraints: `6`
- pass: `6`
- fail: `0`
- missing: `0`

This means the current qualitative pheromone persistence/diffusion constraint
screen has no remaining failures. The next calibration level is digitized curve
fitting for trail decay, recruitment strength, branch choice and brood survival.

## Individual-Level Output

Export all ants at the end of each replicate:

```bash
python3 ant_colony_sim/experiments/batch_runner.py \
  --scenario mature_supplied \
  --seeds 1-3 \
  --days 3 \
  --output ant_colony_sim/outputs/macro.csv \
  --individual-output ant_colony_sim/outputs/individuals.csv
```

Export only the first 50 ants per replicate:

```bash
python3 ant_colony_sim/experiments/batch_runner.py \
  --scenario mature_supplied \
  --seeds 1-3 \
  --days 3 \
  --output ant_colony_sim/outputs/macro.csv \
  --individual-output ant_colony_sim/outputs/individuals_sample.csv \
  --individual-limit 50
```

## Summary Statistics

```bash
python3 ant_colony_sim/experiments/summarize_batch.py \
  ant_colony_sim/outputs/mature_supplied_baseline.csv \
  --output ant_colony_sim/outputs/mature_supplied_baseline_summary.csv
```

The summary groups by `scenario` and `day`, then reports `mean`, `sd`, and `n` for biological validation metrics such as trip rates, task counts, brood total, corpse cleanup and pheromone totals.

## Literature Alignment Probes

Run the qualitative literature-alignment checks:

```bash
python3 ant_colony_sim/experiments/literature_alignment_probe.py
```

This checks whether the model reproduces broad phenomena from trail-following and ant-mill literature:

- food/nest trail formation;
- rain/evaporation washout;
- evaporation sensitivity;
- army-ant-style death spiral.

These are qualitative checks, not numeric calibration to published curves.

## Double-Bridge Probe

Smoke test an equal-branch Deneubourg-style double bridge:

```bash
python3 ant_colony_sim/experiments/double_bridge_probe.py \
  --seeds 1-8 \
  --days 6 \
  --sample-days 0.1 \
  --output ant_colony_sim/outputs/double_bridge_equal.csv
```

Test sensitivity to an initial upper-branch pheromone bias:

```bash
python3 ant_colony_sim/experiments/double_bridge_probe.py \
  --seeds 1-8 \
  --days 6 \
  --sample-days 0.1 \
  --bias-branch upper \
  --bias-strength 350 \
  --pheromone-strength 130 \
  --sense-threshold 6 \
  --output ant_colony_sim/outputs/double_bridge_upper_bias.csv
```

Interpretation:

- `selected_branch` reports which path had more crossings.
- `dominance` is `abs(upper-lower)/(upper+lower)`.
- `return_dominance` applies the same metric only to food-return crossings.

Current reference smoke results after trail-focus and nonlinear contrast updates:

- equal bridge, 8 seeds, 8 days: upper/lower selected 4/4, mean dominance about `0.173`;
- connected upper bias, 3 seeds, 6 days: upper selected 3/3, mean dominance about `0.525`.

The model now shows directionally correct symmetry breaking and initial-bias sensitivity. It is still not calibrated to a published branch-choice probability curve.

## Double-Bridge Calibration

Run the first-pass Deneubourg-style reference calibration:

```bash
python3 ant_colony_sim/experiments/calibrate_double_bridge.py \
  --seeds 1-8 \
  --days 8 \
  --sample-days 0.1 \
  --output ant_colony_sim/calibration_results/double_bridge_calibration_v1.csv
```

The current `v1` best row is:

- `pheromoneStrength=120`
- `senseThreshold=10`
- `evaporationRate=80`
- loss about `1.49`

This target uses the Deneubourg/Le Goff reinforced-random-walk choice function as a literature model reference. It is not a digitized raw experimental dataset.

## Stochasticity Probe

Run the Shiraishi-style diverse stochasticity probe:

```bash
python3 ant_colony_sim/experiments/stochasticity_probe.py \
  --seeds 1-8 \
  --pre-days 4 \
  --post-days 4 \
  --adaptation-days 0.5 \
  --profiles low,medium,high,diverse \
  --output ant_colony_sim/outputs/stochasticity_probe_v4.csv
```

Current `v4` summary after adding traffic cost, food-memory decay and state-dependent exploration drive:

- normalized `relocated_early trips_vs_initial`: low `0.368`, medium `0.372`, high `0.249`, diverse `0.522`;
- raw `relocated_total` trips: low `113.38`, medium `36.38`, high `49.13`, diverse `79.75`;
- `relocated_total avg_traffic_load`: low `0.324`, medium `0.136`, high `0.004`, diverse `0.098`.

Generate a Markdown validation report with per-profile ratios and CI:

```bash
python3 ant_colony_sim/experiments/generate_validation_report.py \
  --stochasticity-csv ant_colony_sim/outputs/stochasticity_probe_v4.csv \
  --output ant_colony_sim/outputs/biological_validation_report_v4.md
```

Interpretation: the model partially aligns with Shiraishi et al. when measuring adaptation relative to each profile's own baseline after food relocation. Diverse stochasticity exceeds low-noise early relocation adaptation, but medium is not clearly separated and low-noise colonies still win on raw total trips. Treat this probe as a qualitative adaptation check, not a fitted reproduction of the published optimum curve.

## Paper-Condition Validation Matrix

Run a multi-paper validation pass that maps literature claims to explicit simulation conditions:

```bash
python3 ant_colony_sim/experiments/paper_conditions_probe.py \
  --seeds 1-3 \
  --output ant_colony_sim/outputs/paper_conditions_v5.csv \
  --json-output ant_colony_sim/outputs/paper_conditions_v5.json \
  --report-output ant_colony_sim/outputs/paper_conditions_report_v5.md
```

The current `v5` matrix covers:

- Perna et al. 2012: local pheromone trail formation, per-step trajectory/sensing logs, aggregate gradient-turn alignment and segment-flow metrics;
- Ramirez et al. 2018: tropotaxis gradient-response proxy using the same per-step trajectory/sensing and segment-flow metrics;
- Amorim 2014: trail formation plus food-removal/rain washout;
- Deneubourg/Goss/Beckers double bridge: branch bias, branch-choice timecourse and positive-feedback sensitivity;
- Dussutour et al. 2004: crowded traffic and alternate route use;
- John et al. 2009: no hard jammed phase using displacement plus segment speed/flow-density metrics;
- Shiraishi et al. 2018: diverse stochasticity after food relocation;
- Malickova/Yates/Bodova 2015: random motion plus pheromone signalling under external change.
- Kang & Theraulaz 2015: external task-demand changes and task reallocation;
- Afek/Kecher/Sulamy 2015: fail-stop foraging resilience after mass worker loss;
- Jimenez-Romero et al. 2015: negative pheromone as a forbidden-path signal.
- Aswale et al. 2022: misleading food pheromone attack and cautionary-pheromone defense proxy.
- Jackson & Chaline 2007: food quality and trail-recruitment strength.
- Avanzi, Lisart & Detrain 2024: corpse/death cue response and necrophoresis cleanup latency.
- Baudier et al. 2019: brood-stage-sensitive nest microclimate and heat/dry brood stress.
- Pratt et al. 2002: nest-site quality, quorum and colony relocation.

`outputs/paper_conditions_report_v5.md` is the human-readable summary. Treat `pass` as qualitative alignment only; it is not a claim of fitted quantitative agreement with the original experiments.

Current `v5` additions show:

- task-demand reallocation aligns qualitatively with response-threshold task organization;
- per-step trajectory/sensing logs are exported through the shared `antSim.startTrajectoryLog()` / `collectTrajectoryLog()` API;
- double-bridge probes now export seeded-branch fraction, branch-choice timecourse and generic curve error;
- task-switch rate, contact-pair summaries and segment speed/flow-density are exported as general metrics;
- fail-stop foraging is qualitatively aligned in the full probe, but remains algorithmic rather than proof-level validation;
- negative pheromone is qualitatively aligned through shared avoid pheromone plus short-term avoid memory, not a paper-specific exception;
- misleading pheromone is qualitatively aligned when fake trails are sustained as an environmental perturbation and caution/avoid cues are enabled, but active attacker agents and calibrated effect sizes are still missing;
- food-quality recruitment is now testable and qualitatively aligned, but lacks species-specific concentration calibration.
- necrophoresis cleanup is now testable and qualitatively aligned, but lacks corpse-age chemistry, pathogen state and interaction-network validation.
- brood microclimate and nest relocation/quorum are now testable through general rules, but still need species-specific numerical calibration.

Experiments may change parameters, initial conditions and environmental state only. They must not inject paper-specific behavior or force ant task/state transitions; run `python experiments/check_validation_boundaries.py` to enforce this boundary.

## Literature Corpus Builder

Build or refresh the 100+ paper triage corpus:

```bash
python3 ant_colony_sim/experiments/build_literature_corpus.py \
  --target 120 \
  --rows-per-query 40 \
  --retries 1 \
  --timeout 8 \
  --json-output ant_colony_sim/outputs/literature_corpus_100.json \
  --csv-output ant_colony_sim/outputs/literature_corpus_100.csv \
  --md-output ant_colony_sim/outputs/literature_corpus_100.md
```

The current corpus contains 120 deduplicated records from Crossref plus curated seed works. It is a candidate pool for future validation conditions, not a claim that all papers have already been reproduced. The generated records include DOI/URL, category labels and a candidate mapping such as `existing_traffic_density_probe`, `extend_corpse_cleanup_probe` or `needs_food_quality_resource_model`.

## Sequential Corpus Evaluation

Evaluate all 120 corpus records against the current paper-condition probes:

```bash
python3 ant_colony_sim/experiments/evaluate_literature_corpus.py \
  --corpus ant_colony_sim/outputs/literature_corpus_100.json \
  --conditions ant_colony_sim/outputs/paper_conditions_v5.json \
  --csv-output ant_colony_sim/outputs/literature_corpus_120_evaluation.csv \
  --json-output ant_colony_sim/outputs/literature_corpus_120_evaluation.json \
  --md-output ant_colony_sim/outputs/literature_corpus_120_evaluation.md
```

Current result:

- `pass`: 120
- `exact_paper_condition`: 17
- `validated_family_condition`: 69
- `algorithmic_or_robotics_analogy`: 34

Interpretation: all 120 corpus records now pass the audit matrix. This does not mean all 120 are quantitatively reproduced biological experiments: 17 have exact paper-condition qualitative alignment, 69 have validated family-level qualitative alignment, and 34 are algorithmic/robotics/ACO references that pass only as screened-out non-biological targets.

Generate the backlog of papers that are not fully simulated yet:

```bash
python3 ant_colony_sim/experiments/generate_literature_gap_backlog.py \
  --evaluation ant_colony_sim/outputs/literature_corpus_120_evaluation.json \
  --csv-output ant_colony_sim/outputs/literature_gap_backlog.csv \
  --json-output ant_colony_sim/outputs/literature_gap_backlog.json \
  --md-output ant_colony_sim/outputs/literature_gap_backlog.md
```

Current backlog:

- `total`: 0
