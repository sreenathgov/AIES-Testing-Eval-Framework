---
agent: PTA
component: Combo Power Electronics Unit
entity_id: ent_267
jurisdiction: EU
fundamental_function: ENERGY_CONVERSION
material_composition: OBC + DC-DC converter + PDU in single cast-aluminum enclosure
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8504.40.60"
gri_path: GRI_3b
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8504 — static converters; EU CN 8504.40.60 (accumulator chargers)
ruling_flag: "EU CN 8504.40.60 specifically covers accumulator chargers — OBC-dominant Combo Unit classifies here"
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — all sub-components are Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

GRI 3(b): OBC gives essential character → 8504.40 (static converters). EU CN 8504.40.60 specifically covers "accumulator chargers." The OBC's function (charging the HV battery) makes the assembly an accumulator charger. EU CN 8504.40.60 is the specific provision.

## Classification

- **Code**: 8504.40.60 — accumulator chargers
- **Basis**: GRI 3(b); OBC essential character; EU CN 8504.40.60 specific provision

## Graph Links

- `classification_node` → [[product_component-combo-power-electronics-unit]]
- `engineering_anchor` → [[combo-power-electronics-unit]]
- `classified_as` → [[hs_code-8504-40-60-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
