---
agent: KA
batch: TB-1-remaining
components_audited: 6
audit_date: "2026-04-01"
verdict: PASS
corrections_required: 0
---

# KA Audit Report — TB-1 Remaining

## Scope

Six components: Battery Control Unit (BCU), Battery Disconnect Unit (BDU), Cell Supervisor Unit (CSU), Silicon Carbide (SiC) MOSFETs, Silicon IGBTs, NdFeB Permanent Magnets.

---

## KA Invariants Applied

### I-1: Section XVII Note 2(f) — Must Fire for All Electrical Apparatus

**BCU** (ent_169): Note 2(f) fired. PASS.
**BDU** (ent_171): Note 2(f) fired. PASS.
**CSU** (ent_170): Note 2(f) fired. PASS.
**SiC MOSFETs** (ent_209): Note 2(f) fired. PASS.
**Silicon IGBTs** (ent_210): Note 2(f) fired. PASS.
**NdFeB Permanent Magnets** (ent_207): Note 2(f) reviewed — correctly not fired. NdFeB magnets are passive metallic articles in Chapter 85 by virtue of heading 8505; they are not "electrical apparatus" of the kind Note 2(f) is designed to route. Heading 8505 is a Chapter 85 heading, so Note 2(f) is irrelevant (there is no Chapter 87 conflict for passive magnets). AA noted this correctly. PASS.

**All I-1 results: PASS.**

---

### I-2: Chapter 90 Note 2 — Must Be Analyzed for ACTIVE_CONTROL Components

**BCU**: Ch 90 Note 2 analyzed and correctly not fired (ACTIVE_CONTROL). PASS.
**BDU**: Ch 90 Note 2 analyzed and correctly not fired (ACTIVE_CONTROL). PASS.
**CSU**: Ch 90 Note 2 analyzed in depth — measurement serves control; correctly not fired. The CSU analysis is the most detailed in this batch and correctly resolves the ambiguity. PASS.
**SiC MOSFETs**: Ch 90 Note 2 not applicable (switching device, not measuring instrument). Correct. PASS.
**Silicon IGBTs**: Same as SiC MOSFETs. PASS.
**NdFeB Permanent Magnets**: Ch 90 Note 2 not applicable (passive magnetic article). Correct. PASS.

**All I-2 results: PASS.**

---

### I-3: Two-or-More Apparatus Threshold — Must Be Verified for All 8537.10 Candidates

**BCU**: Protection ICs (8536 class) + cell-balancing switches (8536 class) — threshold met. PASS.
**BDU**: HV contactors (8536.49) + pyrofuse (8536.50) — threshold met. Both are apparatus of heading 8536. PASS.
**CSU**: AFE switching ICs (8536 class) + cell-balancing switches (8536 class) — threshold met. PASS.

**All I-3 results: PASS.**

---

### I-4: GRI 3(b) Essential Character — Not Required for This Batch

No TB-1 components are composite goods requiring GRI 3(b) analysis. All six components resolve at GRI 1. Not applicable.

---

### I-5: Subheading Consistency — EU CN Subheading Selection Must Be Justified

**BCU EU 8537.10.91**: Justified — BCU executes programmable firmware (programmable memory controller). PASS.
**BDU EU 8537.10.98**: Justified — BDU's primary apparatus are electromechanical contactors; not a "programmable memory controller." The AA documentation explains the distinction from BCU/CSU explicitly. PASS.
**CSU EU 8537.10.91**: Justified — CSU executes programmable balancing firmware (same basis as BCU). PASS.
**SiC MOSFETs EU 8541.29.00**: Single EU CN code. No subheading ambiguity. PASS.
**Silicon IGBTs EU 8541.29.00**: Same. PASS.
**NdFeB EU 8505.11.90**: Justified — NdFeB is not ferrite; 8505.11.90 (Other) correctly excludes ferrite category. PASS.

**All I-5 results: PASS.**

---

### I-6: India Subheading Consistency

**BCU/BDU/CSU India 8537.10.00**: India single 8-digit entry. Correct. PASS.
**SiC MOSFETs India 8541.29.90**: India ITC-HS 8541.29.90 (Other — not ADP/telecom type). EV power transistors are not ADP/telecom devices. Justified. PASS.
**Silicon IGBTs India 8541.29.90**: Same justification as SiC MOSFETs. PASS.
**NdFeB India 8505.11.90**: NdFeB is not ferrite. India ITC-HS subdivision confirmed. PASS.

**All I-6 results: PASS.**

---

### I-7: Source Traceability

All PTA files cite primary corpus documents:
- US files: `usitc_hts_ch85_2026_complex.md` ✓
- EU files: `explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md` ✓
- India files: `cbic_indian_trade_classification_complex.md` ✓
- DA: `da_memo_tb1_remaining.md` cites secondary dossiers ✓
- All AA files cite PTA files and DA memo ✓

**I-7: PASS.**

---

### I-8: Graph Links Completeness

All 6 AA files carry:
- `classification_node` → product_component node (forward link — nodes to be created) ✓
- `engineering_anchor` → verified entity file ✓
- `classified_as` → jurisdiction-specific hs_code nodes (forward links) ✓
- No links to `drona/knowledge/misrouted/` ✓
- `graph_index` → [[d-class-hs_gate1_graph_index]] ✓

**I-8: PASS.**

---

## Special Notes

**I-3 Note — BDU**: The BDU carries a pyrotechnic fuse (pyrofuse) which is a single-use irreversible protection device. Classification of pyrofuses within heading 8536 (subheading 8536.50 — "other switches") is the standard practice in EV battery systems trade. If a customs authority characterizes the pyrofuse as an article of heading 8535 (fuses/circuit breakers for protection of circuits) rather than 8536, the two-or-more threshold is still met (contactors at 8536.49 + pyrofuse at 8535.X = apparatus of 8535 and 8536 mixed — heading 8537 covers "two or more apparatus of heading 8535 or 8536"). The BDU's 8537.10 classification is robust regardless of whether the pyrofuse is classified at 8535 or 8536.

**NdFeB Supply Chain Note**: When NdFeB magnets are presented embedded in a completed traction motor or rotor assembly, the classification would be at 8501 (motor). The 8505.11 classification applies specifically to discrete magnet components traded in the supply chain. The entity's supply_chain_position (MIDSTREAM_COMPONENT) confirms the discrete-component trading context.

---

## Verdict

**PASS. 0 corrections required.**

All six TB-1 remaining components are correctly classified. The BMS hierarchy (BCU/BDU/CSU) consistently classifies at heading 8537.10 with appropriate subheading distinctions. Power transistors (SiC MOSFETs/Silicon IGBTs) correctly classify at 8541.29. NdFeB Permanent Magnets correctly classify at 8505.11 with proper ferrite/non-ferrite subheading distinction.

## Graph Links

- `audits` → [[battery-control-unit-(bcu)_classification_candidate]]
- `audits` → [[battery-disconnect-unit-(bdu)_classification_candidate]]
- `audits` → [[cell-supervisor-unit-(csu)_classification_candidate]]
- `audits` → [[silicon-carbide-(sic)-mosfets_classification_candidate]]
- `audits` → [[silicon-igbts_classification_candidate]]
- `audits` → [[ndfeb-permanent-magnets_classification_candidate]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
