# Metric Measurement Guide

This guide translates the control framework into formulaic diagnostic metrics.
The metrics explain the run; they do not replace the legal control profile.

## Policy

- Control gates remain dispositive: `promote`, `review`, `blocked`, or `unresolved`.
- Metric scores are diagnostic summaries.
- A single blocker, such as missing external legal authority for a material
  claim, cannot be cured by a high aggregate score.
- EU/WCO/BTI are paper-scope. US/India material is comparison-only.
- DAV-style audit veto remains a hard stop.
- Abstention is a success behavior when the corpus does not support a safe
  legal conclusion.
- Forbidden and future-only metrics are documented in
  `protocol/FORBIDDEN_METRICS.md`.

## Metric Families

| Metric | Formula | Diagnostic Meaning |
|---|---|---|
| Authority-Boundary Compliance | permitted agent-source uses / total agent-source uses | Did each agent stay inside its source boundary? |
| Material Legal Capture | weighted used required items / weighted total required items | Did the artifact capture decisive legal rules and facts? |
| Provenance Sufficiency | sourced material claims / total material claims | Can claims be traced to source anchors? |
| Primary-Authority Sufficiency | decisions with required primary/interpretive authority / total decisions | Is the decision grounded in legally sufficient authority? |
| Critical Omission Rate | missing decisive rules / total decisive rules | Did the run miss rules that could alter the result? |
| Unsupported Synthesis Rate | unsupported inference edges / total inference edges | Did reasoning steps have legal or logical support? |
| False-Certainty Rate | unsafe high-confidence ambiguous outputs / ambiguous cases | Did the system overstate certainty? |
| Conflict Preservation | preserved conflict cases / total conflict cases | Did the system surface valid alternatives? |
| Evidence-Gap Detection | correctly flagged incomplete cases / incomplete cases | Did the system abstain or escalate when facts were missing? |
| Handoff Safety | unsafe outputs intercepted / unsafe outputs | Did governance stop unsafe downstream promotion? |
| Human-Review Trigger Correctness | correct escalations / required escalations | Were review conditions converted into route decisions? |
| Field Completeness Rate | present required fields / total required fields | Did PTA/PRA/AA/KA/handoff artifacts preserve required fields? |
| Abstention Rate | correct abstentions / evidence-insufficient cases | Did the system route insufficient evidence to review, blocked, or unresolved? |
| Graph-Artifact Parity | structurally aligned graph items / total graph items | Are product nodes, code nodes, and classification edges structurally safe? |
| Human Research Burden | 1 - (review-or-block tickets / total artifacts) | How much human research load did the run generate? This is diagnostic, not correctness. |
| Rerun Delta Rate | 1 - (changed comparable outputs / comparable outputs) | Comparison-only v1 signal for future baseline drift checks. |

## Required Trace Inputs

The metric calculator consumes run-local traces:

- `agent_trace.json`
- `claim_trace.json`
- `rule_invocation_graph.json`
- `gating_decisions.json`
- `uncertainty_signals.json`
- `metric_inputs.json`
- `field_completeness_trace.json`
- `graph_alignment_trace.json`
- `abstention_trace.json`
- `research_burden_trace.json`
- `rerun_delta_trace.json`

These are generated from the bounded run artifacts. They are deterministic
and API-free in the paper replay path.

## Four-Gate Reporting

Metric summaries are accompanied by `gate_summary.json`, `gate_summary.csv`,
and `gate_summary.md`. The four gates are `pass`, `pass_with_notes`,
`blocked_pending_research`, and `blocked_pending_rerun`. Gate routing is the
reviewer-facing handoff taxonomy; metric scores remain explanatory.
