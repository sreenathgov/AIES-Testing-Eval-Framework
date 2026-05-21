# Integrated 38-Artifact Evaluation Results Packet

- Run ID: `paper_integrated_20260520`
- Positive run: `paper_eval_20260520`
- Negative run: `paper_negative_20260520`
- Generated at: 2026-05-20T19:38:33+00:00

## Interpretation Boundary

Primary 38-artifact deterministic evaluation with cohort stratification. Aggregate metrics are diagnostic and do not prove legal correctness.

## Table 1. Integrated Run Summary

| Check | Result |
| --- | --- |
| Total artifacts | 38 |
| Baseline artifacts | 28 |
| Fault-injection artifacts | 10 |

## Table 2. Integrated Gate Distribution

| Gate Label | Count |
| --- | --- |
| blocked_pending_rerun | 2 |
| blocked_pending_research | 6 |
| pass | 22 |
| pass_with_notes | 8 |

## Table 3. Cohort Gate Distribution

| Cohort | Gate Label | Count | Share |
| --- | --- | --- | --- |
| baseline | pass | 22 | 0.7857 |
| baseline | pass_with_notes | 6 | 0.2143 |
| fault_injection | blocked_pending_rerun | 2 | 0.2 |
| fault_injection | blocked_pending_research | 6 | 0.6 |
| fault_injection | pass_with_notes | 2 | 0.2 |
| integrated | blocked_pending_rerun | 2 | 0.0526 |
| integrated | blocked_pending_research | 6 | 0.1579 |
| integrated | pass | 22 | 0.5789 |
| integrated | pass_with_notes | 8 | 0.2105 |

## Table 4. Integrated Metric Summary

| Metric ID | Numerator | Denominator | Score | Status |
| --- | --- | --- | --- | --- |
| authority_boundary_compliance | 178 | 180 | 0.9889 | warning |
| material_legal_capture | 208 | 211 | 0.9858 | warning |
| provenance_sufficiency | 36 | 38 | 0.9474 | review_trigger |
| primary_authority_sufficiency | 37 | 38 | 0.9737 | warning |
| critical_omission_rate | 1 | 45 | 0.9778 | warning |
| unsupported_synthesis_rate | 2 | 78 | 0.9744 | warning |
| false_certainty_rate | 1 | 7 | 0.8571 | review_trigger |
| conflict_preservation | 6 | 7 | 0.8571 | review_trigger |
| evidence_gap_detection | 0 | 1 | 0.0 | blocker |
| handoff_safety | 6 | 8 | 0.75 | blocker |
| human_review_trigger_correctness | 6 | 8 | 0.75 | blocker |
| field_completeness_rate | 860 | 862 | 0.9977 | warning |
| abstention_rate | 6 | 7 | 0.8571 | review_trigger |
| graph_artifact_parity | 113 | 114 | 0.9912 | warning |
| human_research_burden | 16 | 38 | 0.5789 | diagnostic |
| rerun_delta_rate | 1 | 2 | 0.5 | comparison_only |

## Table 5. Fault-Injection Detection Matrix

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

## Paper Claim

In a single integrated validator-driven run, the protocol admitted stable baseline artifacts and compared controlled fault-injection detections against a registry oracle.

Do not interpret aggregate metric scores alone as proof of legal correctness. The defensible result is the cohort-stratified gate and detection behavior.
