# Submission Manifest

This repository contains the public reproducibility package for the bounded HS
legal extraction evaluation harness. It is a deterministic, API-free replay for
the paper's minimum evaluation protocol.

## Reviewer Command

```bash
python3 scripts/reviewer_replay_check.py --repo-root .
```

Expected result:

```text
Reviewer replay check passed.
```

## Canonical Paper Runs

- `runs/paper_eval_20260520/` - positive baseline run.
- `runs/paper_negative_20260520/` - controlled fault-injection run.
- `runs/paper_integrated_20260520/` - primary integrated paper run.

## Expected Integrated Result

- Total artifacts: `40`.
- Baseline artifacts: `28`.
- Fault-injection artifacts: `12`.
- Gate distribution: `22 pass`, `8 pass_with_notes`, `8 blocked_pending_research`, `2 blocked_pending_rerun`.
- Detection aggregates: gate accuracy `1.0`, micro recall `1.0`, false negatives `0`.

## Primary Evidence Files

- `runs/paper_integrated_20260520/RUN_MANIFEST.json`
- `runs/paper_integrated_20260520/reports/integrated_results_packet.md`
- `runs/paper_integrated_20260520/reports/cohort_gate_distribution.md`
- `runs/paper_integrated_20260520/reports/integrated_detection_matrix.md`
- `runs/paper_integrated_20260520/reports/metric_summary.md`
- `data/negative_cases/negative_case_registry.json`
- `scripts/reviewer_replay_check.py`

## Boundary

The run evaluates a bounded HS legal extraction trajectory under a minimum
protocol. It does not certify final legal correctness, solve HS classification,
or measure live model/API variance.
