# Integrated Four-Gate Handoff Summary

| cohort | negative_case_id | scenario_id | artifact_id | component_id | actual_route | severity | gate_id | gate_label | gate_reason_codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | None | SCN_baseline_AA_EU_anode-active-material-graphite | AA_EU_anode-active-material-graphite | ent_tb3_02 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_anode-substrate-cu-foil | AA_EU_anode-substrate-cu-foil | ent_tb3_06 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_battery-control-unit-(bcu) | AA_EU_battery-control-unit-(bcu) | ent_169 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_battery-disconnect-unit-(bdu) | AA_EU_battery-disconnect-unit-(bdu) | ent_171 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_battery-management-system-(bms) | AA_EU_battery-management-system-(bms) | ent_217 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_cathode-active-material-nmc | AA_EU_cathode-active-material-nmc | ent_tb3_01 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_cathode-substrate-al-foil | AA_EU_cathode-substrate-al-foil | ent_tb3_05 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_cell-supervisor-unit-(csu) | AA_EU_cell-supervisor-unit-(csu) | ent_170 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_combo-power-electronics-unit | AA_EU_combo-power-electronics-unit | ent_267 | review | review_trigger | gate_2 | pass_with_notes | gri_3b_anchor_missing |
| baseline | None | SCN_baseline_AA_EU_dc-dc-converter | AA_EU_dc-dc-converter | ent_216 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_electrolyte-lipf6-solution | AA_EU_electrolyte-lipf6-solution | ent_tb3_03 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_high-voltage-battery-module | AA_EU_high-voltage-battery-module | ent_133 | review | review_trigger | gate_2 | pass_with_notes | gri_3b_anchor_missing |
| baseline | None | SCN_baseline_AA_EU_high-voltage-battery-pack-assembly | AA_EU_high-voltage-battery-pack-assembly | ent_100 | review | review_trigger | gate_2 | pass_with_notes | gri_3b_anchor_missing |
| baseline | None | SCN_baseline_AA_EU_high-voltage-connectors | AA_EU_high-voltage-connectors | ent_182 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_high-voltage-contactor | AA_EU_high-voltage-contactor | ent_144 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_hyper-integrated-e-axle | AA_EU_hyper-integrated-e-axle | ent_269 | review | review_trigger | gate_2 | pass_with_notes | gri_3b_anchor_missing |
| baseline | None | SCN_baseline_AA_EU_integrated-e-axle | AA_EU_integrated-e-axle | ent_187 | review | review_trigger | gate_2 | pass_with_notes | gri_3b_anchor_missing |
| baseline | None | SCN_baseline_AA_EU_lithium-ion-battery-cell | AA_EU_lithium-ion-battery-cell | ent_147 | review | review_trigger | gate_2 | pass_with_notes | gri_3b_anchor_missing |
| baseline | None | SCN_baseline_AA_EU_ndfeb-permanent-magnets | AA_EU_ndfeb-permanent-magnets | ent_207 | promote | pass | gate_1 | pass |  |
| fault_injection | NEG_001 | SCN_fault_injection_NEG_AA_NEG_001 | NEG_AA_NEG_001 | dc-dc-converter | blocked | blocker | gate_3 | blocked_pending_research | internal_source_as_authority;missing_external_authority;unsupported_promotion |
| fault_injection | NEG_002 | SCN_fault_injection_NEG_AA_NEG_002 | NEG_AA_NEG_002 | on-board-charger-(obc) | blocked | blocker | gate_3 | blocked_pending_research | missing_source_anchor;source_anchor_not_resolved |
| fault_injection | NEG_003 | SCN_fault_injection_NEG_AA_NEG_003 | NEG_AA_NEG_003 | high-voltage-battery-pack-assembly | blocked | blocker | gate_3 | blocked_pending_research | required_authority_class_missing;secondary_only_authority_chain |
| fault_injection | NEG_004 | SCN_fault_injection_NEG_AA_NEG_004 | NEG_AA_NEG_004 | combo-power-electronics-unit | review | review_trigger | gate_2 | pass_with_notes | capture_gap_requires_review;critical_omission;required_gri_path_element_missing |
| fault_injection | NEG_005 | SCN_fault_injection_NEG_AA_NEG_005 | NEG_AA_NEG_005 | traction-inverter-module | blocked | blocker | gate_3 | blocked_pending_research | unsupported_promotion |
| fault_injection | NEG_006 | SCN_fault_injection_NEG_AA_NEG_006 | NEG_AA_NEG_006 | separator-pe-pp-film | review | review_trigger | gate_3 | blocked_pending_research | unsupported_promotion |
| fault_injection | NEG_007 | SCN_fault_injection_NEG_AA_NEG_007 | NEG_AA_NEG_007 | silicon-alloyed-electrical-steel-core-noes | blocked | blocker | gate_3 | blocked_pending_research | corpus_gap;evidence_gap;unsupported_promotion |
| fault_injection | NEG_008 | SCN_fault_injection_NEG_AA_NEG_008 | NEG_AA_NEG_008 | battery-management-system-(bms) | blocked | blocker | gate_4 | blocked_pending_rerun | missing_required_handoff_field |
| fault_injection | NEG_009 | SCN_fault_injection_NEG_AA_NEG_009 | NEG_AA_NEG_009 | on-board-charger-(obc) | blocked | blocker | gate_4 | blocked_pending_rerun | edge_direction_invalid;edge_endpoint_unresolved;graph_parity_failure |
| fault_injection | NEG_010 | SCN_fault_injection_NEG_AA_NEG_010 | NEG_AA_NEG_010 | high-voltage-connectors | review | review_trigger | gate_2 | pass_with_notes | over_escalation_burden;review_route_declared |
| baseline | None | SCN_baseline_AA_EU_on-board-charger-(obc) | AA_EU_on-board-charger-(obc) | ent_215 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_power-distribution-unit-(pdu) | AA_EU_power-distribution-unit-(pdu) | ent_219 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_separator-pe-pp-film | AA_EU_separator-pe-pp-film | ent_tb3_04 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_silicon-alloyed-electrical-steel-core-noes | AA_EU_silicon-alloyed-electrical-steel-core-noes | ent_tb3_07 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_silicon-carbide-(sic)-mosfets | AA_EU_silicon-carbide-(sic)-mosfets | ent_209 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_silicon-igbts | AA_EU_silicon-igbts | ent_210 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_traction-inverter-module | AA_EU_traction-inverter-module | ent_196 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_traction-motor | AA_EU_traction-motor | ent_221 | promote | pass | gate_1 | pass |  |
| baseline | None | SCN_baseline_AA_EU_vehicle-control-unit-(vcu) | AA_EU_vehicle-control-unit-(vcu) | ent_218 | promote | pass | gate_1 | pass |  |

Integrated gates evaluated: 38
