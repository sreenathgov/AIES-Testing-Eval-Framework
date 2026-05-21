# Legal Extraction Evaluation Harness

This repository is a bounded pre-HS legal extraction slice plus minimum
evaluation protocol for a narrow HS legal extraction paper. It demonstrates how a governed
neuro-symbolic legal extraction pipeline can be evaluated for authority
preservation, provenance sufficiency, role-boundary compliance, graph parity,
uncertainty preservation, contradiction handling, and handoff safety.

This is not a production legal AI system and does not claim to solve HS
classification. It now contains both:

- a clean pre-HS input bundle for the selected 28 engineering components; and
- deterministic fixture/control tests for evaluating generated artifacts.

## Primary Contributor Instructions

This repository should be treated as a research-grade regulatory intelligence
and legal-evaluation codebase, not as a quick prototype. Contributors and
agentic coding assistants should work as co-strategists, systems architects,
and implementation engineers under the direction of the research maintainer.

Default operating principles:

- Design for long-term scalability, correctness, and structural integrity over
  quick MVP shortcuts.
- Explain architectural decisions in clear product-founder terms: what the
  decision does, why it matters, and what risk it reduces.
- Prefer modular backend boundaries, structured data models, explicit schemas,
  and future-extensible evaluation contracts.
- Where multiple approaches are available, state the tradeoffs briefly and
  default to the most robust, maintainable option.
- Flag complexity risks, dependency risks, and maintenance implications before
  they become hidden assumptions.
- Provide annotated code where necessary, and avoid ambiguous or speculative
  implementations.

## Reviewer Quickstart

Use this path to verify the paper result from a clean clone:

```bash
git clone https://github.com/sreenathgov/AIES-Testing-Eval-Framework.git
cd AIES-Testing-Eval-Framework

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
python scripts/reviewer_replay_check.py --repo-root .
```

Expected result:

```text
Reviewer replay check passed.
```

The command is non-mutating by default. It verifies readiness, package imports,
checked-in paper runs, the integrated 40-artifact result, public-release
guardrails, and the full regression suite.

## Scope

- Evaluated jurisdictions and authorities: EU, WCO, and EU BTI only.
- US and India fields are retained only as `comparison_only` metadata.
- Internal extraction artifacts are recorded as `artifact_origin`, never as
  legal authority.
- The default paper runner is fully offline and deterministic.
- Fresh deterministic harness runs are generated under `runs/<run_id>/`.
- API-backed live LLM execution is intentionally not enabled by default.
- Historical comparison baselines are local-only maintainer material and are
  not required for public replay.

## Repository Layout

```text
data/
  engineering_handoff/ Clean pre-HS engineering inputs for 28 components
  sources/          Anchor excerpts and source notes used by fixtures
  source_corpus/    Cited EU/WCO/BTI originals, parsed outputs, and legal-safe record layers
  origin_evidence/  Sanitized artifact-origin and graph evidence
  graph_fixtures/   Curated normalized node/edge snapshot
  fixtures/         Source manifest and gold cases
protocol/schemas/   JSON Schemas for normalized artifacts
protocol/agent_specs/Bounded PTA/PRA/DA/AA/KA role specs
protocol/measurement_framework.json Formulaic measurement overlay
protocol/forbidden_metrics.json Non-dispositive/forbidden metric policy
runs/               Fresh or frozen extraction run workspaces
protocol/           Control framework map and metric dispositions
src/legal_extract_eval/
tests/
scripts/
```

## Control Framework

The active framework is defined in `protocol/control_framework.json` and
explained in `protocol/CONTROL_FRAMEWORK.md`. It consolidates the paper layer
framework, the metric mapping CSV, and observed extraction-control failure modes into
twelve deterministic control families:

1. `corpus_source_integrity` — corpus and source integrity
2. `source_grounding_anchor_verification` — source grounding and anchor verification
3. `quote_span_fidelity` — quote and parsed-source fidelity
4. `authority_chain_sufficiency` — authority chain sufficiency
5. `agent_role_boundary_compliance` — agent role boundary compliance
6. `material_capture_completeness` — material capture completeness
7. `representation_integrity` — representation integrity
8. `graph_artifact_parity` — graph-artifact parity
9. `legal_method_validity` — GRI, HS/CN, ruling, and temporal validity
10. `supported_synthesis_control` — supported synthesis control
11. `conflict_uncertainty_gap_preservation` — conflict, uncertainty, and gap preservation
12. `handoff_review_governance` — handoff and review governance

## Replay Details

If you cannot install the package, use the source-tree fallback:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.readiness --repo-root .
PYTHONPATH=src python3 -m pytest -q
```

## Paper Replay Runs

The primary paper result is the validator-driven integrated run:

```text
paper_eval_20260520        positive baseline
paper_negative_20260520    controlled fault-injection run
paper_integrated_20260520  primary 40-artifact validator-driven paper run
```

The expected paper-level result is:

- 40 integrated artifacts.
- 28 baseline artifacts and 12 fault-injection artifacts.
- Gate distribution: 22 `pass`, 8 `pass_with_notes`, 8
  `blocked_pending_research`, 2 `blocked_pending_rerun`.
- Fault-injection detection: gate accuracy 1.0, micro recall 1.0, and zero
  false negatives against the registry oracle.

To regenerate reviewer-local copies without overwriting the canonical paper
runs:

```bash
python scripts/reviewer_replay_check.py --repo-root . --regenerate
```

This creates `runs/reviewer_negative_replay/` and
`runs/reviewer_integrated_replay/`, then checks the same paper-level
invariants.

Individual commands are also available:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.readiness --repo-root . --json
PYTHONPATH=src python3 -m legal_extract_eval.negative_run --repo-root . --run-id reviewer_negative_replay --base-run paper_eval_20260520 --force
PYTHONPATH=src python3 -m legal_extract_eval.integrated_run --repo-root . --run-id reviewer_integrated_replay --positive-run paper_eval_20260520 --negative-run reviewer_negative_replay --force
```

For public replay, omit `--source-repo-root`; readiness will validate the
checked-in bounded source bundle without inspecting a private upstream export.

For tests:

```bash
python -m pytest -q
```

The run evaluator writes:

- `runs/<run_id>/reports/control_profile.json`
- `runs/<run_id>/reports/control_profile.csv`
- `runs/<run_id>/reports/control_profile.md`
- `runs/<run_id>/reports/gate_summary.json`
- `runs/<run_id>/reports/gate_summary.csv`
- `runs/<run_id>/reports/gate_summary.md`
- `runs/<run_id>/reports/metric_summary.json`
- `runs/<run_id>/reports/metric_summary.csv`
- `runs/<run_id>/reports/metric_summary.md`
- `runs/<run_id>/reports/metric_stress_test_catalog.json`
- `runs/<run_id>/reports/metric_stress_test_catalog.md`

The integrated result packets are under
`runs/paper_integrated_20260520/reports/`. The evaluator does not produce a
generic accuracy score because the protocol is designed to identify legally
unsafe extraction behavior even when a candidate code appears plausible.

The readiness command is the correct command to use before a paper test run. It
checks the checked-in bounded HS source bundle and, when supplied, the exported
source repository slice; it also checks source-corpus completeness,
authority-class normalization, graph schema conformance, runtime isolation, and
knowledge-evidence coverage without generating a new run.

## Four-Gate Handoff Model

The reviewer-facing route taxonomy is written to `gate_summary.*` and attached
to each control-profile row:

- Gate 1: `pass` for stable, fully sourced, graph-safe promotion.
- Gate 2: `pass_with_notes` for review routes, caveats, contested positions,
  jurisdictional divergence, in-personam ruling limits, or GRI 3(b) complexity.
- Gate 3: `blocked_pending_research` for missing source anchors, missing
  primary authority, evidence gaps, abstention, or corpus insufficiency.
- Gate 4: `blocked_pending_rerun` for graph structural failure, malformed
  nodes, wrong edge direction, ontology drift, or rerun-delta breach.

Control gates are dispositive. Metric scores explain why a route was safe or
unsafe, but they do not override a blocker, DAV-style audit veto, or required
human review.

## Measurement Overlay

The metric layer is defined in:

- `protocol/measurement_framework.json`
- `protocol/METRIC_MEASUREMENT_GUIDE.md`

It adds formulaic measurements for:

- authority-boundary compliance,
- material legal capture,
- provenance sufficiency,
- primary-authority sufficiency,
- critical omission detection,
- unsupported synthesis,
- false certainty,
- conflict preservation,
- evidence-gap detection,
- handoff safety,
- human-review trigger correctness,
- field completeness,
- abstention,
- graph-artifact parity,
- human research burden,
- rerun delta.

These scores are diagnostic. They explain the control profile but do not
override blocker or review gates.

`protocol/FORBIDDEN_METRICS.md` and `protocol/forbidden_metrics.json` define the
metrics that are forbidden, deferred, or future-only for v1. NLL, Brier Score,
TF-IDF/entropy relevance proxies, and document-level citation are not legal
correctness metrics. BERTScore, Expected Calibration Error, and nLog-Distance
are future diagnostics only. Any truncation, chunk-boundary loss,
context-window loss, or retrieval-window omission must be logged as a
source-processing boundary.

## Build The Pre-HS Slice

The pre-HS slice can be rebuilt from a private source repository in copy-only mode:

```bash
PYTHONPATH=src python3 scripts/build_pre_hs_slice.py \
  --source-repo-root /path/to/private-source-repo \
  --harness-root .
```

This maintainer-only rebuild creates:

- `data/engineering_handoff/selected_28_components.json`
- `protocol/agent_specs/*.md`
- `protocol/schemas/hs_slice/*.json`
- a legacy local replay workspace

The builder never writes into the private source repository.

The report includes the advanced control-family statuses plus the expected and
actual route for every fixture.

## Source Record Layer

The generic OCR Markdown projections are browsing aids, not the paper-facing
legal source layer. The harness now compiles each source corpus document into a
document-profiled record layer:

- EU CN regulation: CN/TARIC tariff-table records.
- EU CN Explanatory Notes: layout-aware code/note records.
- EU BTI CSV: one ruling record per source row.
- WCO GRI: one rule record per GRI/sub-rule.
- WCO Sections 84/85/87/90: chapter-note records plus heading/H.S. code table records.

Build all legal-safe source records with:

```bash
PYTHONPATH=src python3 scripts/build_source_records.py --repo-root .
```

Outputs are written under:

- `data/source_corpus/records/eu/`
- `data/source_corpus/records/wco/`
- `data/source_corpus/records/bti/`
- `data/source_corpus/SOURCE_RECORD_PROFILE_MANIFEST.json`

Each compiled source receives:

- `*_records.json`
- `*_records.md`
- `*_qc.json`
- `*_layout_profile.json`

Ambiguity is not silently corrected. For example, merged continuation rows and
heading/subheading rows that need review are flagged in `*_qc.json`.

The EU CN Explanatory Notes compiler can still be run by itself:

```bash
PYTHONPATH=src python3 scripts/build_eu_cn_layout_records.py --repo-root .
```

Outputs:

- `data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_records.json`
- `data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_review.md`
- `data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_qc.json`

These records preserve code ranges, chapter/heading context, page references,
source bounding boxes, note text, and review flags. Downstream extraction should
prefer the record layer over generic Markdown for every source corpus document.

## Regenerate Review Bundle

The review bundle is built by copying a cited subset from the source repository
into this harness. The builder uses copy-only operations and must not mutate the
source repository.

Dry run:

```bash
PYTHONPATH=src python3 scripts/build_review_bundle.py --source-repo-root /path/to/private-source-repo --harness-root . --dry-run
```

Build:

```bash
PYTHONPATH=src python3 scripts/build_review_bundle.py --source-repo-root /path/to/private-source-repo --harness-root .
```

After building, inspect:

- `data/source_corpus/SOURCE_ASSET_MANIFEST.json`
- `data/origin_evidence/ORIGIN_EXPORT_MANIFEST.json`
- `data/fixtures/FIXTURE_LINEAGE_MAP.json`
