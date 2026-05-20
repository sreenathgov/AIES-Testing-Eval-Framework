# HS Evaluation Paper Results Packet

- Run ID: `paper_eval_20260520`
- Generated at: 2026-05-20 16:26:44 IST (+0530)
- Branch: `codex/hs-eval-execution-2026-05-20`
- Current commit at generation: `3805e50d75e06c8425537b1446d3dd8fb6e489c9`
- Pre-execution checkpoint tag commit: `3805e50d75e06c8425537b1446d3dd8fb6e489c9`

## Interpretation Boundary

This packet reports a deterministic minimum evaluation protocol for a bounded EU/WCO/BTI HS extraction trajectory. Metrics are diagnostic. Gates are dispositive. `not_applicable` metric rows have `score: null` and are not treated as perfect passes. The run does not certify final legal correctness and does not claim to solve HS classification.

## Table 1. Run Admissibility

| Check | Result |
| --- | --- |
| Readiness status | ready |
| Readiness blockers | 0 |
| Readiness warnings | 0 |
| Readiness info | 1 |
| Regression suite | 93 passed |
| Public denylist scan | clean |
| Checkpoint tag | checkpoint/pre-execution-readiness-2026-05-20 |

## Table 2. Source Bundle Inventory And Authority Classes

| Source ID | Jurisdiction | Authority Class | Compiler Profile | Records |
| --- | --- | --- | --- | --- |
| SRC_EU_BTI_SAMPLE | EU | ruling_or_precedent | bti_csv_rows | 30 |
| SRC_EU_CN_2025_1926_EVS | EU | primary_legal_text | eu_cn_tariff_table | 952 |
| SRC_EU_CN_EXPLANATORY_NOTES_EVS | EU | interpretive_legal_note | eu_cn_explanatory_notes_layout | 409 |
| SRC_WCO_SECTION_84 | WCO | primary_legal_text | wco_heading_table | 766 |
| SRC_WCO_SECTION_85 | WCO | primary_legal_text | wco_heading_table | 463 |
| SRC_WCO_SECTION_87 | WCO | primary_legal_text | wco_heading_table | 129 |
| SRC_WCO_SECTION_90 | WCO | primary_legal_text | wco_heading_table | 196 |
| SRC_WCO_GRI_2017 | WCO | primary_legal_text | wco_gri_rules | 10 |

## Table 3. Artifact Production Counts

| Layer | Count |
| --- | --- |
| PTA records | 28 |
| PRA records | 28 |
| AA candidates | 28 |
| Audit records | 28 |
| Handoff packages | 28 |
| Graph nodes | 72 |
| Graph edges | 28 |
| Control rows | 28 |
| Metric rows | 16 |
| Stress catalog rows | 16 |

## Table 4. Four-Gate Distribution

| Gate Label | Count | Share |
| --- | --- | --- |
| pass | 22 | 78.6% |
| pass_with_notes | 6 | 21.4% |

## Table 5. Metric Summary

| Metric ID | Numerator | Denominator | Score | Status |
| --- | --- | --- | --- | --- |
| authority_boundary_compliance | 168 | 168 | 1.0 | pass |
| material_legal_capture | 158 | 158 | 1.0 | pass |
| provenance_sufficiency | 28 | 28 | 1.0 | pass |
| primary_authority_sufficiency | 28 | 28 | 1.0 | pass |
| critical_omission_rate | 0 | 34 | 1.0 | pass |
| unsupported_synthesis_rate | 0 | 56 | 1.0 | pass |
| false_certainty_rate | 0 | 6 | 1.0 | pass |
| conflict_preservation | 6 | 6 | 1.0 | pass |
| evidence_gap_detection | 0 | 0 | None | not_applicable |
| handoff_safety | 6 | 6 | 1.0 | pass |
| human_review_trigger_correctness | 6 | 6 | 1.0 | pass |
| field_completeness_rate | 812 | 812 | 1.0 | pass |
| abstention_rate | 6 | 6 | 1.0 | pass |
| graph_artifact_parity | 84 | 84 | 1.0 | pass |
| human_research_burden | 6 | 28 | 0.7857 | diagnostic |
| rerun_delta_rate | 0 | 0 | None | comparison_only |

## Table 6. Component-Level Control Profile

| Component ID | Artifact ID | Candidate Code | Route | Gate | Failed Checks |
| --- | --- | --- | --- | --- | --- |
| ent_tb3_02 | AA_EU_anode-active-material-graphite | 3801.90 | promote | pass |  |
| ent_tb3_06 | AA_EU_anode-substrate-cu-foil | 7410.21 | promote | pass |  |
| ent_169 | AA_EU_battery-control-unit-(bcu) | 8537.10 | promote | pass |  |
| ent_171 | AA_EU_battery-disconnect-unit-(bdu) | 8536.50 | promote | pass |  |
| ent_217 | AA_EU_battery-management-system-(bms) | 8537.10 | promote | pass |  |
| ent_tb3_01 | AA_EU_cathode-active-material-nmc | 2841.90 | promote | pass |  |
| ent_tb3_05 | AA_EU_cathode-substrate-al-foil | 7607.19 | promote | pass |  |
| ent_170 | AA_EU_cell-supervisor-unit-(csu) | 8537.10 | promote | pass |  |
| ent_267 | AA_EU_combo-power-electronics-unit | 8504.40 | review | pass_with_notes | gri_3b_requires_adjudication_review |
| ent_216 | AA_EU_dc-dc-converter | 8504.40 | promote | pass |  |
| ent_tb3_03 | AA_EU_electrolyte-lipf6-solution | 3824.99 | promote | pass |  |
| ent_133 | AA_EU_high-voltage-battery-module | 8507.60 | review | pass_with_notes | gri_3b_requires_adjudication_review |
| ent_100 | AA_EU_high-voltage-battery-pack-assembly | 8507.60 | review | pass_with_notes | gri_3b_requires_adjudication_review |
| ent_182 | AA_EU_high-voltage-connectors | 8536.69 | promote | pass |  |
| ent_144 | AA_EU_high-voltage-contactor | 8536.50 | promote | pass |  |
| ent_269 | AA_EU_hyper-integrated-e-axle | 8708.99 | review | pass_with_notes | gri_3b_requires_adjudication_review |
| ent_187 | AA_EU_integrated-e-axle | 8708.99 | review | pass_with_notes | gri_3b_requires_adjudication_review |
| ent_147 | AA_EU_lithium-ion-battery-cell | 8507.60 | review | pass_with_notes | gri_3b_requires_adjudication_review |
| ent_207 | AA_EU_ndfeb-permanent-magnets | 8505.11 | promote | pass |  |
| ent_215 | AA_EU_on-board-charger-(obc) | 8504.40 | promote | pass |  |
| ent_219 | AA_EU_power-distribution-unit-(pdu) | 8537.10 | promote | pass |  |
| ent_tb3_04 | AA_EU_separator-pe-pp-film | 3920.10 | promote | pass |  |
| ent_tb3_07 | AA_EU_silicon-alloyed-electrical-steel-core-noes | 7226.19 | promote | pass |  |
| ent_209 | AA_EU_silicon-carbide-(sic)-mosfets | 8541.29 | promote | pass |  |
| ent_210 | AA_EU_silicon-igbts | 8541.29 | promote | pass |  |
| ent_196 | AA_EU_traction-inverter-module | 8504.40 | promote | pass |  |
| ent_221 | AA_EU_traction-motor | 8501.53 | promote | pass |  |
| ent_218 | AA_EU_vehicle-control-unit-(vcu) | 8537.10 | promote | pass |  |

## Table 7. Stress-Test Catalog

| Perturbation Type | Expected Failed Metric | Expected Control State | Linked Validator |
| --- | --- | --- | --- |
| cross_source_agent_misuse | authority_boundary_compliance | review | agent_role_validator |
| missing_decisive_gri_rule | material_legal_capture | review | material_capture_validator |
| missing_source_anchor | provenance_sufficiency | blocked | provenance_validator |
| secondary_only_authority_chain | primary_authority_sufficiency | blocked | authority_boundary_validator |
| counterfactual_rule_removal | critical_omission_rate | review | material_capture_validator |
| ungrounded_therefore_inference | unsupported_synthesis_rate | blocked | supported_synthesis_validator |
| high_confidence_ambiguous_case | false_certainty_rate | review | uncertainty_validator |
| collapsed_conflict | conflict_preservation | review | uncertainty_validator |
| missing_material_composition | evidence_gap_detection | review | review_trigger_validator |
| unsafe_promotion | handoff_safety | blocked | handoff_validator |
| missing_review_trigger | human_review_trigger_correctness | review | review_trigger_validator |
| missing_required_handoff_field | field_completeness_rate | blocked | schema_and_required_field_trace |
| corpus_gap_requires_abstention | abstention_rate | review | handoff_validator |
| malformed_graph_edge | graph_artifact_parity | blocked | graph_adapter |
| over_escalation_burden | human_research_burden | diagnostic | review_trigger_validator |
| rerun_delta_threshold_breach | rerun_delta_rate | comparison_only | reference_baseline_comparator |

## Fresh-vs-Frozen Reproducibility Summary

| Comparison | Result |
| --- | --- |
| artifact_counts_equal | True |
| gate_distribution_equal | True |
| metric_signature_equal | True |
| graph_parity_distribution_equal | True |

The reproducibility comparison is outcome-level: exact timestamped artifact text is not the claim. The claim is that the minimum protocol produces stable paper-level control outcomes.
