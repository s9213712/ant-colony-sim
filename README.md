# Ant Colony Sim

Behavior-level ant colony simulation for exploring pheromone-mediated foraging, resource pressure, brood care, necrophoresis, traffic costs and stochasticity-driven adaptation.

The current model is a qualitative research aid and teaching tool. It is not calibrated for numerical prediction of real ant colonies.

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
