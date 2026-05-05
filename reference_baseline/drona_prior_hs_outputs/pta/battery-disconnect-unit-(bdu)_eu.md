---
agent: PTA
component: Battery Disconnect Unit (BDU)
entity_id: ent_171
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
material_composition: Heavy-duty electromechanical assembly housing high-voltage contactors, pyrotechnic fuses, and current shunts on a dedicated power board
is_composite_flagged: false
hs_code_candidate: "8537.10.98"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8537 — boards and panels for electric control; CN 8537.10.98 Other
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — electrical switching/protection apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL function; measurement serves protection control |

## GRI Analysis

**Resolved at GRI 1** per [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]].

Heading [[hs_code-8537-10-global]] — EU CN analysis: The BDU carries HV contactors (heading 8536.49) and pyrofuse (heading 8536.50) as its primary apparatus. Two-or-more threshold met. Board classifies at 8537.10.

**EU CN subheading: 8537.10.91 vs 8537.10.98**

EU CN 8537.10.91 is specifically for "programmable memory controllers" — controllers that store and execute programmable algorithms using non-volatile memory. The BDU's primary apparatus are protection-grade mechanical contactors and a pyrofuse. While a BDU may contain an embedded microcontroller for fault logic coordination, the article as a whole is not described as a "programmable memory controller" — it is a protection/isolation switching assembly. The residual **8537.10.98 (Other)** is the correct EU CN subheading.

**Comparison to BCU**: The BCU's primary identity is a firmware-driven programmable control board → 8537.10.91. The BDU's primary identity is an electromechanical protection assembly with switching devices → 8537.10.98. Heading-level classification is identical; the subheading differs due to EU CN definitional specificity.

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.98 — Other (boards/panels for electric control, not programmable memory controllers)
- **Code**: 8537.10.98
- **Basis**: GRI 1; BDU is a protection-dominant control board; EU CN 8537.10.98 is the correct residual

## Graph Links

- `classification_node` → [[product_component-battery-disconnect-unit-bdu]]
- `engineering_anchor` → [[battery-disconnect-unit-(bdu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-98-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
