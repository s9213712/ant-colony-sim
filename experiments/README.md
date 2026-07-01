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
  --output ant_colony_sim/outputs/paper_conditions_v2.csv \
  --json-output ant_colony_sim/outputs/paper_conditions_v2.json \
  --report-output ant_colony_sim/outputs/paper_conditions_report_v2.md
```

The current `v2` matrix covers:

- Perna et al. 2012: local pheromone trail formation and the missing Weber-law turning export;
- Amorim 2014: trail formation plus food-removal/rain washout;
- Deneubourg/Goss/Beckers double bridge: branch bias and positive-feedback sensitivity;
- Dussutour et al. 2004: crowded traffic and alternate route use;
- John et al. 2009: no hard jammed phase using a displacement proxy;
- Shiraishi et al. 2018: diverse stochasticity after food relocation;
- Malickova/Yates/Bodova 2015: random motion plus pheromone signalling under external change.
- Kang & Theraulaz 2015: external task-demand changes and task reallocation;
- Afek/Kecher/Sulamy 2015: fail-stop foraging resilience after mass worker loss;
- Jimenez-Romero et al. 2015: negative pheromone as a forbidden-path signal.

`outputs/paper_conditions_report_v2.md` is the human-readable summary. Treat `pass` as qualitative alignment only; it is not a claim of fitted quantitative agreement with the original experiments.

Current `v2` additions show:

- task-demand reallocation aligns qualitatively with response-threshold task organization;
- fail-stop foraging is only partial because food trips continue after mass death but drop to a low resilience ratio;
- negative pheromone is only partial because it reduces hazard-region occupancy weakly and lacks individual learning.
