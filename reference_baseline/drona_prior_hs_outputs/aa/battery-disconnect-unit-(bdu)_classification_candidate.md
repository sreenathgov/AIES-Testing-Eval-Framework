---
agent: AA
component: Battery Disconnect Unit (BDU)
entity_id: ent_171
batch: TB-1
jurisdictions: [US, EU, India]
hs_code_us: "8537.10.91"
hs_code_eu: "8537.10.98"
hs_code_india: "8537.10.00"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/battery-disconnect-unit-(bdu)_us.md
  - pta/battery-disconnect-unit-(bdu)_eu.md
  - pta/battery-disconnect-unit-(bdu)_india.md
source_da_file: da/da_memo_tb1_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

The Battery Disconnect Unit (BDU) classifies at heading [[hs_code-8537-10-global]] across all three jurisdictions. The BDU is a heavy-duty electromechanical protection assembly housing HV contactors (8536.49), pyrotechnic fuses (8536.50), and current shunts on a dedicated power board. The two-or-more-apparatus threshold is met.

- **US**: 8537.10.91 — dedicated control board ("other dedicated control boards") — protection-function assemblies are captured by the "other" category at 8537.10.91
- **EU**: 8537.10.98 — Other (not "programmable memory controllers"; BDU's primary apparatus are electromechanical contactors)
- **India**: 8537.10.00 — single 8-digit entry

**Note on EU subheading**: The BDU is assigned 8537.10.98 (EU) rather than 8537.10.91 (EU). This is not a heading-level deviation — both BCU and BDU are heading 8537.10. The distinction is that EU CN 8537.10.91 specifically covers "programmable memory controllers" while the BDU's primary identity is an electromechanical protection board. The subheading difference reflects the EU CN's more specific taxonomy. AA adopts 8537.10.98 for BDU in EU.

Stability is **stable**.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL; measurement (current shunts) serves protection control |

---

## GRI Cascade: Two-or-More Apparatus Threshold

**Resolved at GRI 1.** Heading [[hs_code-8537-10-global]] — BDU carries HV contactors (8536.49) and pyrofuse (8536.50) on a single assembly. Both are apparatus of heading 8536. Threshold met.

**Individual 8536 apparatus (contactors/fuses) vs 8537 board**: If the BDU's contactors were imported separately, they would classify at 8536.49. If the pyrofuse were imported separately, 8536.50. However, the BDU as a unit integrates multiple 8536 apparatus in a single housing designed to function as a battery protection/isolation control module. This is the exact article-class heading 8537 was created for. GRI 1 resolves at 8537.10.

---

## Reconciliation: PTA vs DA

PTA: 8537.10.91 (US), 8537.10.98 (EU), 8537.10.00 (India). DA-003-F1 ([[da_memo_tb1_remaining]]): Corroborates 8537.10 for BDU; acknowledges EU subheading distinction as legitimate. No conflicting ruling.

No conflict. Ruling override not triggered.

## Graph Links

- `classification_node` → [[product_component-battery-disconnect-unit-bdu]]
- `engineering_anchor` → [[battery-disconnect-unit-(bdu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `global_anchor` → [[hs_code-8537-10-global]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `classified_as` → [[hs_code-8537-10-98-eu]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
