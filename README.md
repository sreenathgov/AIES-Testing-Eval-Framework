# Legal Extraction Evaluation Harness

This repository is a bounded pre-HS-run DRONA slice plus evaluation harness for
a narrow HS legal extraction paper. It demonstrates how a governed
neuro-symbolic legal extraction pipeline can be evaluated for authority
preservation, provenance sufficiency, role-boundary compliance, graph parity,
uncertainty preservation, contradiction handling, and handoff safety.

This is not a production legal AI system and does not claim to solve HS
classification. It now contains both:

- a clean pre-HS input bundle for the selected 28 engineering components; and
- deterministic fixture/control tests for evaluating generated artifacts.

## Scope

- Evaluated jurisdictions and authorities: EU, WCO, and EU BTI only.
- US and India fields are retained only as `comparison_only` metadata.
- Internal extraction artifacts are recorded as `artifact_origin`, never as
  legal authority.
- The default paper runner is fully offline and deterministic.
- Fresh DRONA-shaped runs are generated under `runs/<run_id>/`.
- API-backed live LLM execution is intentionally not enabled by default.
- Prior DRONA HS outputs are sealed under `reference_baseline/` for comparison
  only and must not be used as runtime input.

## Repository Layout

```text
data/
  engineering_handoff/ Clean pre-HS D-CLASS-ENG inputs for 28 components
  sources/          Anchor excerpts and source notes used by fixtures
  source_corpus/    Cited EU/WCO/BTI originals, parsed outputs, and legal-safe record layers
  forensic_evidence/Sanitized artifact-origin and graph evidence
  graph_fixtures/   Curated normalized node/edge snapshot
  fixtures/         Source manifest and gold cases
protocol/schemas/   JSON Schemas for normalized artifacts
protocol/agent_specs/DRONA-shaped PTA/PRA/DA/AA/KA role specs
protocol/measurement_framework.json Formulaic measurement overlay
reference_baseline/ Prior DRONA HS outputs, sealed as non-input comparison material
runs/               Fresh or frozen extraction run workspaces
protocol/           DRONA control framework map and metric dispositions
src/legal_extract_eval/
tests/
scripts/
```

## DRONA Control Framework

The active framework is defined in `protocol/control_framework.json` and
explained in `protocol/CONTROL_FRAMEWORK.md`. It consolidates the paper layer
framework, the metric mapping CSV, and the real D-CLASS-HS control failures into
deterministic control families:

- corpus/source integrity,
- source grounding and quote fidelity,
- authority and role boundaries,
- material capture,
- representation integrity,
- legal method validity,
- graph-artifact parity,
- supported synthesis,
- uncertainty preservation,
- handoff and review governance.

## Run

Evaluate the frozen paper run:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.runner --repo-root . --run-id paper_frozen_run
```

Create a new deterministic DRONA-shaped run:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.live_run --repo-root . --run-id fresh_eu_run
```

Run the curated fixture regression evaluator:

```bash
PYTHONPATH=src python3 -m legal_extract_eval.runner --repo-root .
```

For tests:

```bash
python3 -m pytest
```

The run evaluator writes:

- `runs/<run_id>/reports/control_profile.json`
- `runs/<run_id>/reports/control_profile.csv`
- `runs/<run_id>/reports/control_profile.md`
- `runs/<run_id>/reports/metric_summary.json`
- `runs/<run_id>/reports/metric_summary.csv`
- `runs/<run_id>/reports/metric_summary.md`
- `runs/<run_id>/reports/metric_stress_tests.json`
- `runs/<run_id>/reports/metric_stress_tests.md`

The runner prints a control-profile table. It does not produce an accuracy
score because the protocol is designed to identify legally unsafe extraction
behavior even when a candidate code appears plausible.

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
- human-review trigger correctness.

These scores are diagnostic. They explain the control profile but do not
override blocker or review gates.

## Build The Pre-HS Slice

The pre-HS slice is built by reading Sector Watch in copy-only mode:

```bash
PYTHONPATH=src python3 scripts/build_pre_hs_slice.py \
  --sector-watch-root /Users/sreenathgovindarajan/Documents/sector-watch \
  --harness-root .
```

This creates:

- `data/engineering_handoff/selected_28_components.json`
- `protocol/agent_specs/*.md`
- `protocol/schemas/drona_hs/*.json`
- `reference_baseline/BASELINE_MANIFEST.json`
- `runs/paper_frozen_run/`

The builder never writes into Sector Watch.

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
PYTHONPATH=src python3 scripts/build_review_bundle.py --sector-watch-root /Users/sreenathgovindarajan/Documents/sector-watch --harness-root . --dry-run
```

Build:

```bash
PYTHONPATH=src python3 scripts/build_review_bundle.py --sector-watch-root /Users/sreenathgovindarajan/Documents/sector-watch --harness-root .
```

After building, inspect:

- `data/source_corpus/SOURCE_ASSET_MANIFEST.json`
- `data/forensic_evidence/FORENSIC_EXPORT_MANIFEST.json`
- `data/fixtures/FIXTURE_LINEAGE_MAP.json`
