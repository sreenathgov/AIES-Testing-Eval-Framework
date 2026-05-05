---
agent: PTA
component: Hyper-Integrated E-Axle
entity_id: ent_269
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
material_composition: 8-in-1 sealed housing merging motor, gearbox, inverter, DC-DC converter, OBC, PDU, VCU, and BMS
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8708.99.68"
gri_path: GRI_3b_or_3c
stability: stable
confidence: high
source_doc: usitc_hts_ch87_2026_complex.md
source_section: Heading 8708 — parts and accessories for motor vehicles; 8708.99 other
ruling_flag: "No CBP ruling directly on 8-in-1 hyper-integrated unit. N329827 principle (vehicular drivetrain essential character) extends to this article by a fortiori. GRI 3(c) fallback available if 3(b) is indeterminate."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | Composite good containing multiple Chapter 85 sub-assemblies plus mechanical drivetrain. Note 2(f) does not veto 8708 for composite goods where mechanical drivetrain gives essential character. Same analysis as Integrated E-Axle. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

**GRI 1 fails**: An 8-in-1 unit merging motor (8501), inverter (8504), DC-DC (8504), OBC (8504), PDU (8537), VCU (8537), BMS (8537), and gearbox (8483) in a single chassis-mounted housing — no heading text covers this article.

**GRI 3(a) fails**: All competing headings describe only part of the composite. Equally specific under "part only" rule.

**GRI 3(b) — Essential Character Analysis**:

The hyper-integrated e-axle contains sub-components from headings 8501, 8504, 8537, 8483, and 8708. The essential character test requires identifying the dominant component.

For a standard integrated e-axle, the vehicular drivetrain (motor + gearbox + housing) was the essential character (see N329827 analysis). For the hyper-integrated unit, the argument for vehicular drivetrain essential character is even stronger: the physical integration of 8 systems into a single chassis-mounted housing definitively transforms the assembly from an electrical machine into a purpose-designed vehicular drivetrain module.

However, one can argue the OBC + BMS + VCU + PDU components (4 of 8 sub-systems) together give the assembly an electrical apparatus character that dilutes the drivetrain essential character. In such a case, GRI 3(b) may be indeterminate.

**GRI 3(c) fallback** (if 3(b) is indeterminate): When equally-merit headings cannot be resolved by 3(b), the heading occurring last in numerical order governs. Competing headings: 8483 (gearboxes), 8501 (motors), 8504 (inverters/converters), 8537 (control boards), 8708 (vehicle parts). **8708 occurs last** → 8708.99.

**AA determination**: Either GRI 3(b) (vehicular drivetrain) or GRI 3(c) (last heading numerically) resolves at 8708.99. Both pathways yield the same code. Confidence: high.

## Classification

- **Heading**: 8708.99
- **Code**: 8708.99.68
- **Basis**: GRI 3(b) or GRI 3(c); both resolve at 8708.99; vehicular drivetrain + GRI 3(c) fallback = 8708.99

## Graph Links

- `classification_node` → [[product_component-hyper-integrated-e-axle]]
- `engineering_anchor` → [[hyper-integrated-e-axle]]
- `classified_as` → [[hs_code-8708-99-us]]
- `source_doc` → [[usitc_hts_ch87_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
