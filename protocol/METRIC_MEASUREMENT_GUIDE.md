# Metric Measurement Guide

This guide translates the control framework into formulaic diagnostic metrics.
The metrics explain the run; they do not replace the legal control profile.

## Policy

- Control gates remain dispositive: `promote`, `review`, `blocked`, or `unresolved`.
- Metric scores are diagnostic summaries.
- A single blocker, such as missing external legal authority for a material
  claim, cannot be cured by a high aggregate score.
- EU/WCO/BTI are paper-scope. US/India material is comparison-only.

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

## Required Trace Inputs

The metric calculator consumes run-local traces:

- `agent_trace.json`
- `claim_trace.json`
- `rule_invocation_graph.json`
- `gating_decisions.json`
- `uncertainty_signals.json`
- `metric_inputs.json`

These are generated from the DRONA-shaped run artifacts. They are deterministic
and API-free in the paper replay path.
