# Ant Colony Sim

[![validation](https://github.com/s9213712/ant-colony-sim/actions/workflows/validation.yml/badge.svg)](https://github.com/s9213712/ant-colony-sim/actions/workflows/validation.yml)

Behavior-level ant colony simulation for exploring pheromone-mediated foraging, resource pressure, brood care, necrophoresis, traffic costs and stochasticity-driven adaptation.

The current model is a qualitative research aid and teaching tool. It is not calibrated for numerical prediction of real ant colonies.

Current scientific validation level: behavior-level ABM with four fit-ready primary-source target files, two passing independent traffic/contact holdouts, one formal-CI external holdout, one partial social-immunity survival endpoint, fit-curve bootstrap uncertainty, three-point traffic curve validation, and replicate-level uncertainty for paper-condition probes, estimated Level 4.6 toward Level 5. The 120-paper corpus separates simulator-condition passes from biological calibration: 86 records still require paper-level quantitative curves or species-specific data, while 34 engineering/ACO references are screened out as non-biological targets.

## Run

Open `index.html` directly in a browser, or serve the folder:

```bash
python3 -m http.server 8876 --bind 127.0.0.1 --directory .
```

## Validation

Core probes:

```bash
python3 behavior_probe.py
python3 experiments/qa_report_probe.py
python3 experiments/literature_alignment_probe.py
python3 experiments/stochasticity_probe.py --seeds 1-8 --pre-days 4 --post-days 4 --adaptation-days 0.5 --profiles low,medium,high,diverse --output outputs/stochasticity_probe_v4.csv
python3 experiments/generate_validation_report.py --stochasticity-csv outputs/stochasticity_probe_v4.csv --output outputs/biological_validation_report_v4.md
```

See `BIOLOGICAL_VALIDATION.md`, `PARAMETER_PROVENANCE.md`, and `experiments/README.md` for model boundaries, parameter provenance and reproducible experiment workflows.

Digitized biological curves for Level 4+ calibration belong in `targets/digitized_curves/`; run `python3 experiments/digitized_curve_inventory.py` to check fit-ready and holdout-ready curves. Run `python3 experiments/level5_replicate_statistics.py` to attach bootstrap CIs to paper-condition replicate outputs.

## Continuous Validation

GitHub Actions runs `.github/workflows/validation.yml` on pushes and pull requests. It installs Playwright Chromium, runs syntax checks, API/UI QA, literature-alignment probes, a short stochasticity smoke experiment, and uploads generated validation artifacts.
