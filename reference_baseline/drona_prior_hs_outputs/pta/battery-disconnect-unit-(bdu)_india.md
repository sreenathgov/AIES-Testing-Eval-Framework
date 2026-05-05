---
agent: PTA
component: Battery Disconnect Unit (BDU)
entity_id: ent_171
jurisdiction: India
fundamental_function: ACTIVE_CONTROL
material_composition: Heavy-duty electromechanical assembly housing high-voltage contactors, pyrotechnic fuses, and current shunts on a dedicated power board
is_composite_flagged: false
hs_code_candidate: "8537.10.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8537 — boards and panels for electric control; India single 8-digit entry 8537.10.00 (voltage ≤ 1,000V)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL; measurement serves protection control |

## GRI Analysis

**Resolved at GRI 1** per [[cbic_indian_trade_classification_complex]].

Heading [[hs_code-8537-10-global]] — BDU has HV contactors (8536.49) and pyrofuse (8536.50) on a single protection board. Two-or-more threshold met. India does not subdivide heading 8537.10 beyond the single 8-digit entry **8537.10.00** ("for a voltage not exceeding 1,000V"). The BDU operates at battery system voltage within the ≤1,000V specification.

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.00 — for a voltage not exceeding 1,000V
- **Code**: 8537.10.00
- **Basis**: GRI 1; India single 8-digit entry

## Graph Links

- `classification_node` → [[product_component-battery-disconnect-unit-bdu]]
- `engineering_anchor` → [[battery-disconnect-unit-(bdu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
