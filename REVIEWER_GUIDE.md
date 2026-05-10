# Reviewer Guide

This repository evaluates a governed legal extraction pipeline. It does not claim that the system solves HS classification end to end.

The evaluation question is whether a legal extraction pipeline preserves controls while transforming parsed legal materials into structured, decision-bearing artifacts. The controls are authority preservation, provenance sufficiency, agent role boundaries, graph parity, uncertainty preservation, contradiction handling, and handoff safety.

## What To Inspect

- `data/engineering_handoff/` contains the clean 28-component pre-HS input bundle.
- `protocol/agent_specs/` contains the DRONA-shaped PTA/PRA/DA/AA/KA role specs used by the bounded run.
- `data/source_corpus/` contains the cited EU/WCO/BTI source subset and parsed outputs.
- `runs/paper_frozen_run/` contains the deterministic paper replay run.
- `reference_baseline/` contains prior DRONA HS outputs for comparison only, never runtime input.
- `data/graph_fixtures/` contains normalized good, bad, and borderline fixture artifacts.
- `data/fixtures/gold_cases.json` defines expected legal-control outcomes.
- `data/fixtures/FIXTURE_LINEAGE_MAP.json` maps each fixture to source assets, parsed anchors, forensic artifacts, graph nodes, graph edges, and expected route.
- `data/forensic_evidence/` contains a small sanitized sample of internal origin artifacts and graph artifacts.

## Scope Rule

Only EU, WCO, and EU BTI claims affect pass/fail outcomes in this paper run. US and India references are preserved only as `comparison_only` metadata where needed to demonstrate divergence handling.

Internal extraction artifacts may explain fixture origin, but they are not legal authority. Legal authority must come from source anchors in `legal_authority_chain`.

## Running The Harness

```bash
PYTHONPATH=src python3 -m legal_extract_eval.runner --repo-root . --run-id paper_frozen_run
python3 -m pytest
```

The runner emits a control-profile report rather than a generic accuracy score.
It also emits a diagnostic metric summary. The metric summary gives formulaic
numerators and denominators for each evaluation family, but it does not override
the control profile. A blocker remains a blocker even if aggregate scores are
high.

## Handoff And Metrics

Each control-profile row is mapped into the DRONA Four-Gate handoff model:

- `pass`
- `pass_with_notes`
- `blocked_pending_research`
- `blocked_pending_rerun`

The gates are the dispositive reviewer-facing route. Metrics are explanatory.
They cover authority boundaries, material legal capture, provenance,
primary-authority sufficiency, critical omissions, unsupported synthesis, false
certainty, conflict preservation, evidence-gap detection, handoff safety,
human-review trigger correctness, field completeness, abstention, semantic graph
alignment, human research burden, and rerun delta.

The forbidden-metric policy is explicit. NLL, Brier Score, TF-IDF/entropy
proxies, and document-level citation are not valid v1 legal-control metrics.
BERTScore, ECE, and nLog-Distance are future diagnostics only. Source-processing
losses from truncation, chunk boundaries, context windows, or retrieval windows
must be logged as boundary conditions.
