---
agent: PTA
component: Combo Power Electronics Unit
entity_id: ent_267
jurisdiction: India
fundamental_function: ENERGY_CONVERSION
material_composition: OBC + DC-DC converter + PDU in single cast-aluminum enclosure
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8504.40.90"
gri_path: GRI_3b
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8504 — static converters; India ITC-HS 8504.40.90 (Other static converters)
ruling_flag: "CAAR Valco (Inverter → 8504.40.10): inverter is 8504.40.10 (electric inverter). OBC and DC-DC are not electric inverters (DC→AC) in India's ITC-HS sense → 8504.40.90."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

GRI 3(b): OBC gives essential character → 8504.40. India ITC-HS structure: 8504.40.10 (Electric inverter — DC→AC) vs 8504.40.90 (Other). The OBC is an AC→DC rectifier/charger, not a DC→AC inverter. DC-DC is also a non-inverter static converter. Both sub-components → 8504.40.90. India code: **8504.40.90**.

**Note on CAAR Valco**: CAAR confirmed the EV inverter (DC→AC) = 8504.40.10. This supports the distinction: 8504.40.10 is for DC→AC converters; the OBC (AC→DC) and DC-DC (DC→DC) are 8504.40.90.

## Classification

- **Code**: 8504.40.90 — Other static converters
- **Basis**: GRI 3(b); OBC essential character; India 8504.40.10 only covers DC→AC inverters; OBC is AC→DC charger → 8504.40.90

## Graph Links

- `classification_node` → [[product_component-combo-power-electronics-unit]]
- `engineering_anchor` → [[combo-power-electronics-unit]]
- `classified_as` → [[hs_code-8504-40-90-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
