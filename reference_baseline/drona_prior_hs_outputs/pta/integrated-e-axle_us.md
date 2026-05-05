---
agent: PTA
component: Integrated E-Axle
entity_id: ent_187
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
material_composition: Integrated electromechanical system combining a traction motor, reduction gearbox, and power electronics in a unified structural housing designed for vehicle chassis mounting
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8708.99.68"
gri_path: GRI_3b
stability: stable
confidence: high
classification_stability_note: "CBP N329827 (Dec 2022) classified an e-axle with reduction gearbox and chassis-mounting housing at 8708.99; vehicular drivetrain essential character"
source_doc: usitc_hts_ch87_2026_complex.md
source_section: Heading 8708 — parts and accessories for motor vehicles; 8708.99 other
ruling_flag: "CBP N329827 (Dec 2022): e-axle → 8708.99.68.90 (drivetrain essential character). CBP H329719 (Aug 2023): EDU with simple gearbox → 8501.53.40 (motor essential character). N329827 applies to integrated e-axle with chassis-integrated housing."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | Note 2(f) excludes electrical machinery (Chapter 85) from Chapter 87 classification. However, the integrated e-axle is a COMPOSITE GOOD — not purely electrical apparatus. The question is which heading gives it essential character. Note 2(f) is not a blanket veto of 8708 for composite goods; it only vetoes pure Chapter 85 articles. The GRI cascade proceeds. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Cascade

**GRI 1 fails**: No single heading text covers an integrated e-axle (motor + gearbox + inverter + housing). The assembly is prima facie classifiable under heading 8501 (electric motor), 8504 (power inverter/static converter), 8483 (gearboxes), and 8708 (motor vehicle drivetrain parts).

**GRI 3(a) fails**: All of 8501, 8504, 8483, and 8708 describe only part of the integrated assembly. Under the "part only" rule of GRI 3(a), they are deemed equally specific. GRI 3(a) does not resolve.

**GRI 3(b) — Essential Character Analysis**:

The essential character of the Integrated E-Axle is assessed by examining bulk, weight, value, and the role of each component in the overall function of the good.

*Arguments for motor (8501) essential character*:
- The traction motor is the primary energy conversion element — without the motor, the assembly cannot propel the vehicle
- CBP H329719 (Aug 2023) held that an Electric Drive Unit (motor + gearbox + inverter) has essential character in the motor (8501.53.40) when the gearbox merely transfers torque output to the vehicle transmission

*Arguments for vehicular drivetrain (8708) essential character*:
- CBP N329827 (Dec 2022): E-axle assembly with reduction gearbox, differential, and chassis-mounting housing → 8708.99. CBP held that when an e-axle includes hardware designed specifically for vehicular mounting and wheel torque distribution, it crosses beyond the scope of Chapter 85.
- The integrated e-axle in this entity description has a "unified, rigid structural housing" and is a "STANDALONE_UNIT" designed for direct chassis installation — this is the defining physical characteristic of N329827's vehicular drivetrain finding.
- The WCO HSC has noted that the degree of mechanical integration (specifically chassis-mounting hardware) is the threshold at which an electric motor legally transforms into a motor vehicle part.

**AA Determination**: The N329827 rationale applies to the Integrated E-Axle because the unified structural housing is designed for vehicle chassis mounting — it is not a modular electrical machine that happens to have a gearbox attached. The essential character is the vehicular drivetrain. GRI 3(b) resolves at heading **8708.99**.

## Classification

- **Heading**: 8708.99
- **Subheading**: 8708.99.68 — parts and accessories for bodies of motor vehicles, other parts
- **Code**: 8708.99.68
- **Basis**: GRI 3(b); vehicular drivetrain essential character per CBP N329827 analysis

## Ruling Flags

**CBP N329827** (Dec 27, 2022): E-axle → 8708.99.6890 (US). Directly applicable.
**CBP H329719** (Aug 15, 2023): EDU (motor + gearbox + inverter, gearbox interfaces with separate vehicle transmission) → 8501.53.40. Distinguished: in H329719 the gearbox was not part of the chassis-mounting structure; the EDU interfaced with an existing vehicle transmission. The Integrated E-Axle here has its own reduction gearbox and unified structural housing — closer to N329827.

## Graph Links

- `classification_node` → [[product_component-integrated-e-axle]]
- `engineering_anchor` → [[integrated-e-axle]]
- `classified_as` → [[hs_code-8708-99-us]]
- `ruling_reference` → [[cbp_n329827_e_axle]] (DA-sourced)
- `source_doc` → [[usitc_hts_ch87_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
