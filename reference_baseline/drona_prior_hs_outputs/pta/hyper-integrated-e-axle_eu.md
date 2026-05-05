---
agent: PTA
component: Hyper-Integrated E-Axle
entity_id: ent_269
jurisdiction: EU
fundamental_function: ENERGY_CONVERSION
material_composition: 8-in-1 sealed housing merging motor, gearbox, inverter, DC-DC, OBC, PDU, VCU, BMS
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8708.99"
gri_path: GRI_3b_or_3c
stability: stable
confidence: high
data_gap_note: "EU CN 8-digit for hyper-integrated e-axle requires EU CN lookup; heading-level 8708.99 confirmed"
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8708 — motor vehicle parts; WCO GRI 3(b)/3(c)
ruling_flag: "No EU BTI ruling on hyper-integrated e-axle available in corpus"
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | Same as US — composite good; Note 2(f) does not block 8708 for composite goods with vehicular drivetrain essential character |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

Same analysis as US. GRI 3(b) or GRI 3(c) resolves at 8708.99. EU CN applies WCO GRI identically.

**GRI 3(c) — EU applies same numerical order logic**: 8708 is last numerically among 8483/8501/8504/8537/8708 → 8708.99.

## Classification

- **Heading**: 8708.99
- **Code**: 8708.99 (heading-level; 8-digit pending EU CN lookup)
- **Basis**: GRI 3(b) or GRI 3(c); both resolve at 8708.99

## Graph Links

- `classification_node` → [[product_component-hyper-integrated-e-axle]]
- `engineering_anchor` → [[hyper-integrated-e-axle]]
- `classified_as` → [[hs_code-8708-99-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
