# Metric Summary

Diagnostic metrics explain the control profile. They do not override blocker or review gates.

| metric_id | name | score | numerator | denominator | status | formula | blocker_override_applied | stress_test_type | linked_validator | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| authority_boundary_compliance | Authority-Boundary Compliance | 0.9889 | 178 | 180 | warning | permitted_agent_source_uses / total_agent_source_uses | True | cross_source_agent_misuse | agent_role_validator | Checks whether each agent used only source classes permitted by its legal role. |
| material_legal_capture | Material Legal Capture | 0.9858 | 208 | 211 | warning | weighted_used_required_items / weighted_total_required_items | True | missing_decisive_gri_rule | material_capture_validator | Reframes recall as legally material capture rather than generic text recall. |
| provenance_sufficiency | Provenance Sufficiency | 0.9474 | 36 | 38 | review_trigger | claims_with_verifiable_trace / total_material_claims | True | missing_source_anchor | provenance_validator | Tests claim-to-source traceability below document level where possible. |
| primary_authority_sufficiency | Primary-Authority Sufficiency | 0.9737 | 37 | 38 | warning | decisions_with_required_primary_or_interpretive_authority / total_decisions | True | secondary_only_authority_chain | authority_boundary_validator | Uses authority sufficiency rather than a crude authority ratio. |
| critical_omission_rate | Critical Omission Rate | 0.9778 | 1 | 45 | warning | missing_decisive_rules / total_decisive_rules | True | counterfactual_rule_removal | material_capture_validator | Detects missing rules that could change the legal outcome. |
| unsupported_synthesis_rate | Unsupported Synthesis Rate | 0.9744 | 2 | 78 | warning | unsupported_inference_edges / total_inference_edges | True | ungrounded_therefore_inference | supported_synthesis_validator | Flags reasoning jumps that are not supported by source or method. |
| false_certainty_rate | False-Certainty Rate | 0.8571 | 1 | 7 | review_trigger | high_confidence_unsafe_ambiguous_outputs / total_ambiguous_cases | True | high_confidence_ambiguous_case | uncertainty_validator | Tests whether uncertainty is preserved instead of collapsed. |
| conflict_preservation | Conflict Preservation | 0.8571 | 6 | 7 | review_trigger | conflict_cases_preserved / total_conflict_cases | True | collapsed_conflict | uncertainty_validator | Ensures competing legal interpretations are preserved. |
| evidence_gap_detection | Evidence-Gap Detection | 0.0 | 0 | 1 | blocker | correctly_flagged_incomplete_cases / total_incomplete_cases | True | missing_material_composition | review_trigger_validator | Tests whether the system abstains or escalates when key facts are missing. |
| handoff_safety | Handoff Safety | 0.75 | 6 | 8 | blocker | unsafe_outputs_intercepted / total_unsafe_outputs | True | unsafe_promotion | handoff_validator | Checks whether unsafe artifacts are stopped before downstream use. |
| human_review_trigger_correctness | Human-Review Trigger Correctness | 0.75 | 6 | 8 | blocker | correct_escalations / total_cases_requiring_escalation | True | missing_review_trigger | review_trigger_validator | Validates that review conditions are turned into explicit route decisions. |
| field_completeness_rate | Field Completeness Rate | 0.9977 | 860 | 862 | warning | required_fields_present / total_required_fields | True | missing_required_handoff_field | schema_and_required_field_trace | Measures whether every agent handoff artifact is structurally complete enough for downstream use. |
| abstention_rate | Abstention Rate | 0.8571 | 6 | 7 | review_trigger | correct_abstentions / evidence_insufficient_cases | True | corpus_gap_requires_abstention | handoff_validator | Treats correct refusal or escalation as a success behavior when the corpus is insufficient. |
| graph_artifact_parity | Graph-Artifact Parity | 0.9912 | 113 | 114 | warning | aligned_graph_items / total_graph_items | True | malformed_graph_edge | graph_adapter | Checks structural equivalence between generated artifacts and the graph representation. |
| human_research_burden | Human Research Burden | 0.5789 | 16 | 38 | diagnostic | 1 - (review_or_block_tickets / total_artifacts) | False | over_escalation_burden | review_trigger_validator | Quantifies the human review load created by safe governance decisions. |
| rerun_delta_rate | Rerun Delta Rate | 0.5 | 1 | 2 | comparison_only | 1 - (changed_baseline_comparable_outputs / total_baseline_comparable_outputs) | False | rerun_delta_threshold_breach | reference_baseline_comparator | Future-ready comparison metric for detecting regressions after corpus augmentation. |

Metrics evaluated: 16
