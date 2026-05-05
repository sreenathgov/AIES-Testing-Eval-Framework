# DRONA Legal Extraction Evaluation Control Framework

This harness evaluates governed legal extraction, not standalone HS classification accuracy.

The evaluation object is the transformation from parsed EU/WCO/BTI legal material into structured, graph-linked, decision-bearing artifacts. A legally acceptable artifact must preserve source authority, granular provenance, agent role boundaries, material legal method, uncertainty, graph parity, and safe handoff state.

## Framework Sources

- The Layer Selection memo is the conceptual base.
- The metric CSV contributes implementation vocabulary after renaming or demotion.
- Sector Watch D-CLASS-HS controls contribute real failure modes: missing AA fields, missing graph nodes, bad edge direction, missing PTA source references, overbroad confidence, jurisdictional divergence, and staging/ontology drift.

## Control Families

1. Corpus and source integrity.
2. Source grounding and anchor verification.
3. Quote and parsed-source fidelity.
4. Authority chain sufficiency.
5. Agent role boundary compliance.
6. Material capture completeness.
7. Representation integrity.
8. Graph-artifact parity.
9. Legal method validity.
10. Supported synthesis control.
11. Conflict, uncertainty, and gap preservation.
12. Handoff and review governance.

## Scope Rule

Only EU/WCO/BTI authorities affect pass/fail for the first paper run. US and India entries may appear only under `comparison_only` and cannot repair or invalidate a paper-scope fixture.

## Metric Disposition

Generic ML metrics are not first-class v1 controls. Expected Calibration Error, Post-Edit Distance, authority ratios, and LLM/NLI-as-judge scoring are rejected or deferred. The v1 protocol uses deterministic legal controls tied to source anchors, authority hierarchy, role rules, graph parity, and gold expected routes.

## Measurement Overlay

The formulaic metric layer is defined in `protocol/measurement_framework.json`.
It adopts the metric-by-metric measurement vocabulary as a diagnostic overlay:
authority-boundary compliance, material legal capture, provenance sufficiency,
primary-authority sufficiency, critical omission detection, unsupported
synthesis, false certainty, conflict preservation, evidence-gap detection,
handoff safety, and human-review trigger correctness.

Metric scores explain the control profile. They do not override legal blocker
or review outcomes.
