<!-- Reviewer-safe sanitized forensic artifact. This file evidences artifact origin only and is not external legal authority. -->

---
agent: PTA
component: High-Voltage Battery Pack Assembly
entity_id: ent_100
jurisdiction: EU
fundamental_function: ENERGY_STORAGE
material_composition: Li-ion cells, BMS, cooling system, aluminum enclosure, busbars
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8507.60.00"
gri_path: GRI_3b
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8507 — electric storage batteries; 8507.60 (lithium-ion accumulators)
ruling_flag: "No EU BTI ruling on EV battery pack in corpus. EU CN Explanatory Notes confirm Li-ion cells as essential character."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | No | HV Battery Pack is not a vehicle part — it is a storage battery. No Chapter 87 issue. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

GRI 3(b): Li-ion cells give essential character → 8507.60. EU CN Explanatory Notes to heading 8507: storage batteries incorporating ancillary monitoring circuits classify in 8507. BMS in the pack is ancillary. EU CN 8507.60.00 (lithium-ion accumulators).

## Classification

- **Code**: 8507.60.00
- **Basis**: GRI 3(b); Li-ion cells essential character; EU CN EN 8507 confirms ancillary circuit rule

## Graph Links

- `classification_node` → [[product_component-hv-battery-pack-assembly]]
- `engineering_anchor` → [[high-voltage-battery-pack-assembly]]
- `classified_as` → [[hs_code-8507-60-00-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[hs-slice_gate1_graph_index]]
