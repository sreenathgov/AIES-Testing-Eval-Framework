---
agent: PTA
component: Combo Power Electronics Unit
entity_id: ent_267
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
material_composition: Single cast-aluminum enclosure containing OBC (AC→DC charger), DC-DC converter (HV→LV), and potentially a Power Distribution Unit
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8504.40.70"
gri_path: GRI_3b
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8504 — static converters; subheading 8504.40.70 (battery chargers)
ruling_flag: "None specific — OBC-dominant combo unit; battery charger subheading applies when OBC is essential character"
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — all sub-components (OBC, DC-DC, PDU) are Chapter 85 electrical apparatus; Chapter 87 vetoed. The composite unit classifies within Chapter 85. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

**GRI 1 fails**: No heading covers "OBC + DC-DC converter + PDU in a single enclosure."

**GRI 3(a)**: OBC → 8504.40 (battery charger/static converter), DC-DC → 8504.40 (static converter), PDU → 8537.10 (control board). Three competing headings: 8504.40 and 8537.10. GRI 3(a) "most specific" test: 8504.40 is more specific for the dominant sub-components.

**GRI 3(b) — Essential Character**:

The Combo Power Electronics Unit is defined by its two primary conversion functions:
- **OBC**: AC input (from charging station) → regulated DC output to HV battery. This is the highest-power function (7–22kW typical) and highest-value sub-component.
- **DC-DC converter**: HV bus → LV bus (12/48V). Lower power (1–3kW).
- **PDU** (if present): switching/distribution; ancillary to the conversion functions.

By bulk, value, and primary commercial function, the OBC gives the assembly its essential character. The Combo Unit's commercial identity is primarily as an integrated charging module with DC-DC conversion capability.

OBC = battery charger = heading 8504.40, subheading **8504.40.70** (battery chargers — defined as static converters used to supply energy to storage batteries).

**Note**: If the DC-DC converter dominates by value (unusual for typical Combo Units), the heading remains 8504.40 but subheading would shift to 8504.40.95 (Other static converters). In either case, heading-level classification is 8504.40.

## Classification

- **Heading**: 8504.40
- **Subheading**: 8504.40.70 — battery chargers (OBC essential character)
- **Code**: 8504.40.70
- **Basis**: GRI 3(b); OBC gives essential character; 8504.40.70 covers battery chargers

## Graph Links

- `classification_node` → [[product_component-combo-power-electronics-unit]]
- `engineering_anchor` → [[combo-power-electronics-unit]]
- `classified_as` → [[hs_code-8504-40-70-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
