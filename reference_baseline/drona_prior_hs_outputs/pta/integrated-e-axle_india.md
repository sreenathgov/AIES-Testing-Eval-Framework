---
agent: PTA
component: Integrated E-Axle
entity_id: ent_187
jurisdiction: India
fundamental_function: ENERGY_CONVERSION
material_composition: Integrated electromechanical system combining traction motor, reduction gearbox, and power electronics in unified structural housing
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8501.53.30"
gri_path: GRI_3b
stability: contested
confidence: medium
classification_stability_note: "India position is contested — CAAR application for BEV axle was DENIED (Bombay HC pending as of Feb 2026). No binding advance ruling exists. CAAR Valco VCU/PCU ruling (8708.99.00) creates pressure toward 8708.99 for automotive assemblies. 8501.53.30 is the PTA-level conclusion from GRI 3(b) analysis per secondary sources; AA must document the contested position."
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8501 — electric motors; subheading 8501.53 (AC motors, 75kW < output ≤ 375kW)
ruling_flag: "CAAR Valco (BEV Axle): advance ruling DENIED (Sec 28-I(2)); matter pending Bombay High Court. CAAR Valco (VCU/PCU): 8708.99.00 for vehicle control units — indirect signal favoring 8708.99 for composite automotive assemblies. No binding ruling on integrated e-axle in India."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | India CAAR Valco (Inverter): Note 2(f) is applied strictly in India — the CAAR held that even a dedicated EV inverter remains at 8504.40.10 (Ch 85) because Note 2(f) is an absolute exclusion. For the composite e-axle, this reinforces the Ch 85 position for the electrical apparatus components. Whether Note 2(f) prevents 8708 classification for the composite good as a whole is the contested question. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade — India-Specific Analysis

**GRI 1 fails**: Same as US/EU — no single heading covers the integrated e-axle.

**GRI 3(a) fails**: Same as US/EU — all competing headings describe only part of the assembly.

**GRI 3(b) — India Essential Character Analysis**:

India's CAAR jurisprudence applies Note 2(f) strictly: pure electrical apparatus (inverters, motors) cannot be classified as vehicle parts under Chapter 87. The CAAR Valco inverter ruling (Apr 2025) illustrates this literalist approach.

For the composite e-axle, two competing analytical frameworks exist in India:

*Motor essential character (8501.53) — PTA position*:
- India CAAR's Section XVII Note 2(f) enforcement philosophy: electrical machinery (traction motor, inverter) cannot become Chapter 87 goods by virtue of integration into a vehicular system
- Secondary sources on India EV classification (hs_customs_classification_intelligence_report_ev) indicate that MSME exporters of integrated e-axle assemblies classifying in India have used 8501.53 (motor heading) as the primary classification
- GRI 3(b): the traction motor is the dominant sub-component by value in the integrated e-axle; it provides propulsive force; the reduction gearbox and housing are secondary to the motor function

*Drivetrain essential character (8708.99) — contested position*:
- CAAR Valco VCU/PCU ruling (8708.99.00): India CAAR has accepted that automotive assemblies not explicitly excluded by Section Notes may classify at 8708.99
- If India applies the N329827 essential character logic (structural housing = drivetrain) rather than the Note 2(f) literalist logic, 8708.99 would follow

**PTA conclusion**: 8501.53.30 (motor essential character) is the PTA-level conclusion based on secondary sources and India's strict Note 2(f) enforcement philosophy. **Stability: contested. Confidence: medium.** The CAAR advance ruling denial (BEV Axle case pending in Bombay HC) means no binding ruling exists. The real India position may shift with the Bombay HC outcome.

**India 8-digit**: 8501.53.30 is India's ITC-HS code for "AC motors for use in EVs, output > 75kW ≤ 375kW." The traction motor embedded in the e-axle is in this range.

## Classification

- **Heading**: 8501.53
- **Subheading**: 8501.53.30 — AC motors for EV use (output > 75kW ≤ 375kW)
- **Code**: 8501.53.30
- **Basis**: GRI 3(b); motor essential character per secondary sources; India strict Section XVII Note 2(f) enforcement; contested — Bombay HC ruling pending
- **Stability**: contested
- **Confidence**: medium

## Graph Links

- `classification_node` → [[product_component-integrated-e-axle]]
- `engineering_anchor` → [[integrated-e-axle]]
- `classified_as` → [[hs_code-8501-53-30-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `contested_by` → CAAR Valco VCU/PCU ruling (8708.99.00) — DA-sourced
- `graph_index` → [[d-class-hs_gate1_graph_index]]
