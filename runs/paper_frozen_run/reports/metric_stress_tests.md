# Metric Stress Tests

| stress_test_type | expected_failed_metric | expected_control_state | linked_metric_id | linked_validator | deterministic_detection_rule | notes |
| --- | --- | --- | --- | --- | --- | --- |
| cross_source_agent_misuse | authority_boundary_compliance | review | authority_boundary_compliance | agent_role_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| missing_decisive_gri_rule | material_legal_capture | review | material_legal_capture | material_capture_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| missing_source_anchor | provenance_sufficiency | blocked | provenance_sufficiency | provenance_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| secondary_only_authority_chain | primary_authority_sufficiency | blocked | primary_authority_sufficiency | authority_boundary_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| counterfactual_rule_removal | critical_omission_rate | review | critical_omission_rate | material_capture_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| ungrounded_therefore_inference | unsupported_synthesis_rate | blocked | unsupported_synthesis_rate | supported_synthesis_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| high_confidence_ambiguous_case | false_certainty_rate | review | false_certainty_rate | uncertainty_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| collapsed_conflict | conflict_preservation | review | conflict_preservation | uncertainty_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| missing_material_composition | evidence_gap_detection | review | evidence_gap_detection | review_trigger_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| unsafe_promotion | handoff_safety | blocked | handoff_safety | handoff_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| missing_review_trigger | human_review_trigger_correctness | review | human_review_trigger_correctness | review_trigger_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| missing_required_handoff_field | field_completeness_rate | blocked | field_completeness_rate | schema_and_required_field_trace | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| corpus_gap_requires_abstention | abstention_rate | review | abstention_rate | handoff_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| malformed_graph_edge | semantic_graph_alignment | blocked | semantic_graph_alignment | graph_adapter | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| over_escalation_burden | human_research_burden | diagnostic | human_research_burden | review_trigger_validator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |
| rerun_delta_threshold_breach | rerun_delta_rate | comparison_only | rerun_delta_rate | reference_baseline_comparator | True | Synthetic perturbation contract for reviewer-facing measurement validation. |

Stress tests specified: 16
