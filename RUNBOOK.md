# Runbook

## Check Readiness Without Running Evaluation

```bash
PYTHONPATH=src python3 -m legal_extract_eval.readiness \
  --repo-root .
```

This command is a preflight only. It validates the checked-in bounded HS source
bundle, source records, source-authority registry, graph artifact schema,
runtime isolation, and knowledge-evidence registry. It does not create a run,
evaluate artifacts, call an API, or refresh reports.

Maintainers with a private exported source repository can add
`--source-repo-root /path/to/private-source-repo` to check the upstream slice as
well. That path is optional for public replay.

## Build Or Refresh The Pre-HS Slice

```bash
PYTHONPATH=src python3 scripts/build_pre_hs_slice.py \
  --source-repo-root /path/to/private-source-repo \
  --harness-root .
```

This reads a private source repository in copy-only mode, creates the clean
28-component engineering handoff, copies bounded HS agent specs and schemas,
optionally refreshes local-only comparison baselines, and refreshes
`runs/paper_frozen_run/`.

## Evaluate The Frozen Paper Run

```bash
PYTHONPATH=src python3 -m legal_extract_eval.runner --repo-root . --run-id paper_frozen_run
```

Reports are written to:

- `runs/paper_frozen_run/reports/control_profile.json`
- `runs/paper_frozen_run/reports/control_profile.csv`
- `runs/paper_frozen_run/reports/control_profile.md`
- `runs/paper_frozen_run/reports/gate_summary.json`
- `runs/paper_frozen_run/reports/gate_summary.csv`
- `runs/paper_frozen_run/reports/gate_summary.md`
- `runs/paper_frozen_run/reports/metric_summary.json`
- `runs/paper_frozen_run/reports/metric_summary.csv`
- `runs/paper_frozen_run/reports/metric_summary.md`
- `runs/paper_frozen_run/reports/metric_stress_test_catalog.json`
- `runs/paper_frozen_run/reports/metric_stress_test_catalog.md`

Trace inputs for the metrics are written under:

- `runs/paper_frozen_run/trace/agent_trace.json`
- `runs/paper_frozen_run/trace/claim_trace.json`
- `runs/paper_frozen_run/trace/rule_invocation_graph.json`
- `runs/paper_frozen_run/trace/gating_decisions.json`
- `runs/paper_frozen_run/trace/uncertainty_signals.json`
- `runs/paper_frozen_run/trace/metric_inputs.json`
- `runs/paper_frozen_run/trace/field_completeness_trace.json`
- `runs/paper_frozen_run/trace/graph_alignment_trace.json`
- `runs/paper_frozen_run/trace/abstention_trace.json`
- `runs/paper_frozen_run/trace/research_burden_trace.json`
- `runs/paper_frozen_run/trace/rerun_delta_trace.json`

The Four-Gate handoff summary is generated from the same control-profile rows:
`pass`, `pass_with_notes`, `blocked_pending_research`, and
`blocked_pending_rerun`. A gate is a reviewer-facing safety route, not an
accuracy label.

## Create A Fresh Deterministic Run

```bash
PYTHONPATH=src python3 -m legal_extract_eval.live_run --repo-root . --run-id fresh_eu_run
```

The current `live_run` entrypoint emits deterministic harness artifacts without API calls.
API-backed execution is intentionally disabled by default so the paper bundle is
reviewer-safe and reproducible.

## Regression Tests

```bash
python3 -m pytest
```

Tests cover the pre-HS boundary, source-record availability, agent-spec
presence, optional-baseline isolation, run report shape, metric formulas, trace
shape, Four-Gate routing, forbidden metric policy, stress-test coverage, and
the existing fixture evaluator.
