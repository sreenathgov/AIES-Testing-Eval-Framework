---
agent: PTA
component: Hyper-Integrated E-Axle
entity_id: ent_269
jurisdiction: India
fundamental_function: ENERGY_CONVERSION
material_composition: 8-in-1 sealed housing merging motor, gearbox, inverter, DC-DC, OBC, PDU, VCU, BMS
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8501.53.30"
gri_path: GRI_3b_or_3c
stability: contested
confidence: medium
classification_stability_note: "India position contested — CAAR BEV Axle ruling denied; Bombay HC pending. For the hyper-integrated 8-in-1, GRI 3(c) creates additional pressure toward 8708.99 even under India's jurisprudence. Contested/medium."
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8501 — electric motors; 8501.53
ruling_flag: "No binding India ruling on hyper-integrated e-axle. CAAR VCU/PCU → 8708.99.00 as indirect signal. CAAR inverter → 8504.40.10 (strict Note 2(f)). India position highly uncertain for 8-in-1."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | India's strict Note 2(f) enforcement prevents reclassification of pure electrical apparatus (motor, inverter) to Chapter 87. For the composite 8-in-1, same theoretical tension as Integrated E-Axle. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade — India

**GRI 1 fails. GRI 3(a) fails.** Same as US/EU.

**GRI 3(b) — Hyper-Integrated E-Axle India**:

For the 8-in-1 unit, the argument for motor essential character is weaker than for the standard integrated e-axle: out of 8 sub-systems, only the motor + gearbox are mechanical drivetrain components; 6 of 8 are electrical apparatus. If India applies weight/value analysis, the motor may not represent sufficient dominance to assign motor essential character.

**GRI 3(c) fallback**: If GRI 3(b) is indeterminate for India (as it may be given the 8-in-1 complexity), GRI 3(c) applies: 8708 is numerically last among 8483/8501/8504/8537/8708 → 8708.99.00 (India).

**PTA note**: The India classification for the hyper-integrated e-axle is MORE uncertain than for the standard integrated e-axle. GRI 3(c) pushes toward 8708.99.00. Secondary sources on India EV classification suggest 8501.53 for motor-dominant composites, but the 8-in-1 dilutes motor dominance. PTA flags this as requiring AA-level judgment. Assigning 8501.53.30 as primary with explicit GRI 3(c) note.

## Classification

- **Heading**: 8501.53 (primary per secondary sources) / 8708.99 (alternative via GRI 3(c))
- **Code**: 8501.53.30 (PTA primary position)
- **Basis**: GRI 3(b) motor essential character — contested; GRI 3(c) alternative = 8708.99.00
- **Stability**: contested; **Confidence**: medium

## Graph Links

- `classification_node` → [[product_component-hyper-integrated-e-axle]]
- `engineering_anchor` → [[hyper-integrated-e-axle]]
- `classified_as` → [[hs_code-8501-53-30-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
