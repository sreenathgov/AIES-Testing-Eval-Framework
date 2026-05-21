# HS Negative Evaluation Results Packet

- Run ID: `paper_negative_20260520`
- Positive baseline: `paper_eval_20260520`
- Generated at: 2026-05-20T19:37:18+00:00

## Interpretation Boundary

Controlled deterministic negative evaluation for a bounded HS legal extraction trajectory. It tests fault-line detection and gate routing; it does not certify legal correctness or adversarial robustness.

## Table 1. Positive Baseline Summary

| Check | Result |
| --- | --- |
| Baseline artifacts | 28 |
| Baseline gate distribution | {'pass': 22, 'pass_with_notes': 6} |

## Table 2. Negative Case Design Matrix

| Case | Bundle | Perturbation Layer | Expected Metrics | Expected Gate | Legal Rationale |
| --- | --- | --- | --- | --- | --- |
| NEG_001 | Internal Authority Substitution | artifact;source | authority_boundary_compliance;provenance_sufficiency;unsupported_synthesis_rate | blocked_pending_research | Generated intermediate artifacts may evidence system origin, but they cannot supply legal authority for a material HS proposition. |
| NEG_002 | Missing Granular Source Anchor | source;artifact | provenance_sufficiency;field_completeness_rate | blocked_pending_research | A legal proposition must be traceable to a heading, rule, note, ruling row, or equivalent locator rather than merely to a broad document. |
| NEG_003 | BTI-Only Authority Chain | source;artifact | primary_authority_sufficiency;authority_boundary_compliance | blocked_pending_research | BTI material may support comparison or fact-specific analysis, but it cannot replace the primary CN/WCO authority chain for a reusable artifact. |
| NEG_004 | Decisive GRI Omitted | artifact | material_legal_capture;critical_omission_rate | pass_with_notes | A missing decisive GRI path element can make an otherwise plausible artifact unsafe or review-dependent. |
| NEG_005 | Unsupported Therefore Inference | artifact;trace | unsupported_synthesis_rate;handoff_safety | blocked_pending_research | A conclusion that looks plausible but is unsupported by legal method or source anchors must be blocked before downstream use. |
| NEG_006 | Collapsed Conflict With High Confidence | artifact;handoff | false_certainty_rate;conflict_preservation;human_review_trigger_correctness | blocked_pending_research | Contested or ambiguous legal states must be preserved or routed to review rather than promoted as clean certainty. |
| NEG_007 | Missing Material Product Facts | source;input;artifact | evidence_gap_detection;abstention_rate;handoff_safety | blocked_pending_research | Where product facts or corpus evidence are insufficient, review or abstention is the safe behavior. |
| NEG_008 | Required Handoff Field Missing | artifact;handoff | field_completeness_rate;human_review_trigger_correctness | blocked_pending_rerun | A structurally incomplete handoff package cannot be safely evaluated or routed downstream. |
| NEG_009 | Graph Meaning Corruption | graph | graph_artifact_parity | blocked_pending_rerun | A graph edge can change the legal meaning of the artifact; corrupted graph semantics require rerun or repair. |
| NEG_010 | Over-Escalation And Rerun Delta | source;route;comparison | human_research_burden;rerun_delta_rate | pass_with_notes | Operational burden and rerun deltas are important diagnostics, but they do not override a legally required gate in v1. |

## Table 3. Metric Fault-Detection Matrix

| Metric ID | Numerator | Denominator | Score | Status |
| --- | --- | --- | --- | --- |
| authority_boundary_compliance | 10 | 12 | 0.8333 | review_trigger |
| material_legal_capture | 50 | 53 | 0.9434 | review_trigger |
| provenance_sufficiency | 8 | 10 | 0.8 | review_trigger |
| primary_authority_sufficiency | 9 | 10 | 0.9 | review_trigger |
| critical_omission_rate | 1 | 11 | 0.9091 | review_trigger |
| unsupported_synthesis_rate | 2 | 22 | 0.9091 | review_trigger |
| false_certainty_rate | 1 | 1 | 0.0 | blocker |
| conflict_preservation | 0 | 1 | 0.0 | blocker |
| evidence_gap_detection | 0 | 1 | 0.0 | blocker |
| handoff_safety | 0 | 2 | 0.0 | blocker |
| human_review_trigger_correctness | 0 | 2 | 0.0 | blocker |
| field_completeness_rate | 48 | 50 | 0.96 | warning |
| abstention_rate | 0 | 1 | 0.0 | blocker |
| graph_artifact_parity | 29 | 30 | 0.9667 | warning |
| human_research_burden | 10 | 10 | 0.0 | diagnostic |
| rerun_delta_rate | 1 | 2 | 0.5 | comparison_only |

## Table 4. Negative Gate Distribution

| Gate Label | Count |
| --- | --- |
| blocked_pending_rerun | 2 |
| blocked_pending_research | 6 |
| pass_with_notes | 2 |

## Table 5. Representative Detected Failures

| Case | Observed Gate | Precision | Recall | F1 | Gate Match |
| --- | --- | --- | --- | --- | --- |
| NEG_001 | blocked_pending_research | 1.0 | 1.0 | 1.0 | True |
| NEG_002 | blocked_pending_research | 0.5 | 1.0 | 0.6667 | True |
| NEG_003 | blocked_pending_research | 0.6667 | 1.0 | 0.8 | True |
| NEG_004 | pass_with_notes | 0.6667 | 1.0 | 0.8 | True |
| NEG_005 | blocked_pending_research | 1.0 | 1.0 | 1.0 | True |
| NEG_006 | blocked_pending_research | 0.6 | 1.0 | 0.75 | True |
| NEG_007 | blocked_pending_research | 0.6 | 1.0 | 0.75 | True |
| NEG_008 | blocked_pending_rerun | 0.5 | 1.0 | 0.6667 | True |
| NEG_009 | blocked_pending_rerun | 1.0 | 1.0 | 1.0 | True |
| NEG_010 | pass_with_notes | 0.5 | 1.0 | 0.6667 | True |

## Detection Aggregates

- Gate accuracy: 1.0
- Micro precision: 0.6774
- Micro recall: 1.0
- Micro F1: 0.8077
- Macro precision: 0.7033
- Macro recall: 1.0
- Macro F1: 0.81

The negative study is a controlled fault-injection experiment. It does not claim broad adversarial robustness, final HS correctness, or exhaustive legal failure coverage.
