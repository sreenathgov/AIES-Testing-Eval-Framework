# Legal Extraction Evaluation Control Framework

This harness evaluates governed legal extraction, not standalone HS classification accuracy.

The evaluation object is the transformation from parsed EU/WCO/BTI legal material into structured, graph-linked, decision-bearing artifacts. A legally acceptable artifact must preserve source authority, granular provenance, agent role boundaries, material legal method, uncertainty, graph parity, and safe handoff state.

## Framework Sources

- The Layer Selection memo is the conceptual base.
- The metric CSV contributes implementation vocabulary after renaming or demotion.
- Observed extraction-control failures contribute concrete failure modes:
  missing AA fields, missing graph nodes, bad edge direction, missing PTA
  source references, overbroad confidence, jurisdictional divergence, and
  staging/ontology drift.

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

Generic ML metrics are not first-class v1 controls. Negative Log Likelihood,
Brier Score, TF-IDF/entropy relevance proxies, and document-level citation are
forbidden or non-dispositive for material legal propositions. BERTScore,
Expected Calibration Error, and nLog-Distance are future diagnostics only, not
v1 legal-control gates. The v1 protocol uses deterministic legal controls tied
to source anchors, authority hierarchy, role rules, graph parity, and gold
expected routes.

## Measurement Overlay

The formulaic metric layer is defined in `protocol/measurement_framework.json`.
It adopts the metric-by-metric measurement vocabulary as a diagnostic overlay:
authority-boundary compliance, material legal capture, provenance sufficiency,
primary-authority sufficiency, critical omission detection, unsupported
synthesis, false certainty, conflict preservation, evidence-gap detection,
handoff safety, and human-review trigger correctness.

Metric scores explain the control profile. They do not override legal blocker
or review outcomes.

## Four-Gate Handoff

The control profile is also rendered through a Four-Gate handoff model:

1. `pass`: stable, fully sourced, graph-safe, promote route.
2. `pass_with_notes`: review route, contested position, jurisdictional
   divergence, in-personam ruling limits, GRI 3(b), or caveat required.
3. `blocked_pending_research`: missing source, missing primary authority,
   evidence gap, abstention, or corpus insufficiency.
4. `blocked_pending_rerun`: graph structural failure, ontology/rerun drift,
   malformed nodes, wrong edge direction, or rerun-delta breach.

DAV-style audit veto remains a hard stop. Abstention is counted as a success
behavior when corpus evidence is insufficient and the artifact routes to review,
blocked, or unresolved instead of inventing a legal conclusion.
