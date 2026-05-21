# Reviewer Guide

This repository evaluates a governed legal extraction pipeline through a
minimum evaluation protocol. It does not claim that the system solves HS
classification end to end.

The evaluation question is whether a legal extraction pipeline preserves
controls while transforming parsed legal materials into structured,
decision-bearing artifacts. The controls are authority preservation,
provenance sufficiency, agent role boundaries, graph parity, uncertainty
preservation, contradiction handling, and handoff safety.

## What To Inspect

- `data/engineering_handoff/` contains the clean 28-component pre-HS input
  bundle.
- `data/source_corpus/` contains the cited EU/WCO/BTI source subset and parsed
  outputs.
- `protocol/agent_specs/` contains the bounded PTA/PRA/DA/AA/KA role specs.
- `data/negative_cases/negative_case_registry.json` contains the fault
  injection oracle used after validation.
- `runs/paper_eval_20260520/` contains the positive baseline run.
- `runs/paper_negative_20260520/` contains the controlled fault-injection run.
- `runs/paper_integrated_20260520/` contains the primary 40-artifact
  validator-driven paper run.
- `runs/paper_integrated_20260520/reports/integrated_results_packet.md`
  summarizes the paper result.

## Scope Rule

Only EU, WCO, and EU BTI claims affect pass/fail outcomes in this paper run. US
and India references are preserved only as `comparison_only` metadata where
needed to demonstrate divergence handling.

Internal extraction artifacts may explain artifact origin, but they are not
legal authority. Legal authority must come from source anchors in
`legal_authority_chain`.

## Running The Harness

Recommended reviewer path:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
python scripts/reviewer_replay_check.py --repo-root .
```

This verifies the checked-in paper result without mutating the canonical runs.

To regenerate reviewer-local runs:

```bash
python scripts/reviewer_replay_check.py --repo-root . --regenerate
```

The regeneration path creates `reviewer_negative_replay` and
`reviewer_integrated_replay`, then checks them against the same paper-level
invariants.

Expected integrated result:

- 40 artifacts.
- 28 baseline artifacts and 12 fault-injection artifacts.
- Gate distribution: 22 `pass`, 8 `pass_with_notes`, 8
  `blocked_pending_research`, 2 `blocked_pending_rerun`.
- Fault-injection detection: gate accuracy 1.0, micro recall 1.0, and zero
  false negatives against the registry oracle.

## Handoff And Metrics

Each control-profile row is mapped into the Four-Gate handoff model:

- `pass`
- `pass_with_notes`
- `blocked_pending_research`
- `blocked_pending_rerun`

The gates are the dispositive reviewer-facing route. Metrics are explanatory.
They cover authority boundaries, material legal capture, provenance,
primary-authority sufficiency, critical omissions, unsupported synthesis, false
certainty, conflict preservation, evidence-gap detection, handoff safety,
human-review trigger correctness, field completeness, abstention,
graph-artifact parity, human research burden, and rerun delta.

The forbidden-metric policy is explicit. NLL, Brier Score, TF-IDF/entropy
proxies, and document-level citation are not valid v1 legal-control metrics.
BERTScore, ECE, and nLog-Distance are future diagnostics only. Source-processing
losses from truncation, chunk boundaries, context windows, or retrieval windows
must be logged as boundary conditions.
