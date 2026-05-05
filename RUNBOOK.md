# Runbook

## Build Or Refresh The Pre-HS Slice

```bash
PYTHONPATH=src python3 scripts/build_pre_hs_slice.py \
  --sector-watch-root /Users/sreenathgovindarajan/Documents/sector-watch \
  --harness-root .
```

This reads Sector Watch in copy-only mode, creates the clean 28-component
engineering handoff, copies DRONA-shaped HS agent specs and schemas, seals prior
HS outputs under `reference_baseline/`, and refreshes `runs/paper_frozen_run/`.

## Evaluate The Frozen Paper Run

```bash
PYTHONPATH=src python3 -m legal_extract_eval.runner --repo-root . --run-id paper_frozen_run
```

Reports are written to:

- `runs/paper_frozen_run/reports/control_profile.json`
- `runs/paper_frozen_run/reports/control_profile.csv`
- `runs/paper_frozen_run/reports/control_profile.md`
- `runs/paper_frozen_run/reports/metric_summary.json`
- `runs/paper_frozen_run/reports/metric_summary.csv`
- `runs/paper_frozen_run/reports/metric_summary.md`
- `runs/paper_frozen_run/reports/metric_stress_tests.json`
- `runs/paper_frozen_run/reports/metric_stress_tests.md`

Trace inputs for the metrics are written under:

- `runs/paper_frozen_run/trace/agent_trace.json`
- `runs/paper_frozen_run/trace/claim_trace.json`
- `runs/paper_frozen_run/trace/rule_invocation_graph.json`
- `runs/paper_frozen_run/trace/gating_decisions.json`
- `runs/paper_frozen_run/trace/uncertainty_signals.json`
- `runs/paper_frozen_run/trace/metric_inputs.json`

## Create A Fresh Deterministic Run

```bash
PYTHONPATH=src python3 -m legal_extract_eval.live_run --repo-root . --run-id fresh_eu_run
```

The current `live_run` entrypoint emits DRONA-shaped artifacts without API calls.
API-backed execution is intentionally disabled by default so the paper bundle is
reviewer-safe and reproducible.

## Regression Tests

```bash
python3 -m pytest
```

Tests cover the pre-HS boundary, source-record availability, agent-spec
presence, baseline isolation, run report shape, metric formulas, trace shape,
stress-test coverage, and the existing fixture evaluator.
