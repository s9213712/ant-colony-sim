# Digitized Biological Curves

This directory is the handoff point between literature review and quantitative model fitting.

Rules:

- Store only numeric target data that can be traced to a primary paper, public dataset or newly collected experiment.
- Do not enter values from secondary summaries unless the row is explicitly marked `digitization_method=secondary_lead_only`; those rows cannot be used for fitting.
- Keep paper identity, species, units, figure/table reference and digitization method in every row.
- Use one CSV per biological target curve.
- Fitting scripts may change shared model parameters and initial conditions, but must not add paper-specific exception rules to the simulator.

Required columns for fit-ready curve CSV files:

- `source_id`
- `target_id`
- `paper_title`
- `source_url`
- `species`
- `figure_or_table`
- `x_name`
- `x_value`
- `x_unit`
- `y_name`
- `y_value`
- `y_unit`
- `variance_type`
- `variance_value`
- `n`
- `digitization_method`
- `notes`

Current status: no fit-ready digitized biological curve is committed yet. The next priority is `trail_decay_curve`, followed by `food_recruitment_strength_curve` and `double_bridge_branch_choice_curve`.
