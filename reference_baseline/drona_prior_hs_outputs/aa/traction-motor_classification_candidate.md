---
agent: AA
component: Traction Motor
entity_id: ent_221
pilot_batch: TB-4
hs_code_us: "8501.53"
hs_code_eu: "8501.53.50"
hs_code_india: "8501.53.30"
india_itc_hs: "8501.53.30"
india_itc_hs_description: Traction motor (dedicated code)
gri_path: GRI_1
gri_3b_triggered: false
stability: stable
confidence: high
jurisdiction_divergence: false
ruling_override_applied: false
ruling_corroboration: EU BTI CZBTI34/018997/2025-580000-04/01
---

## Classification Summary

**All three jurisdictions: 8501.53 — AC motors, multi-phase, output exceeding 75 kW**

Section XVII Note 2(f) fires (electric motor → Chapter 85; Chapter 87 vetoed). Heading 8501 is unambiguous for traction motors. India has a dedicated ITC-HS 8-digit code (85015330 "Traction motor") eliminating all subheading ambiguity. EU BTI ruling corroborates at 8501.53.50.

---

## Pre-GRI Filter Results

| Filter | Result |
|--------|--------|
| Section XVII Note 2(f) | **FIRED** — electric motor is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | Not applicable |
| Chapter 90 Note 2 | Not applicable |

---

## GRI Analysis

**Resolved at GRI 1.** Heading 8501 covers electric motors and generators. Traction motor = electric motor. Subheading 8501.53 for AC multi-phase motors >75 kW. No competing headings after Section XVII Note 2(f) veto of Chapter 87.

---

## Jurisdictional Classifications

### United States
- **Code**: 8501.53 (6-digit confirmed stable/high)
- **US 8-digit framework (D2-GAP-013)**: Splits are power-threshold-dependent (GRI 6):
  - 8501.53.40 — >75 kW but <149.2 kW (stat suf: .40 civil aircraft, .80 other)
  - 8501.53.60 — 149.2 kW or more but not exceeding 150 kW
  - 8501.53.80 — >150 kW but not exceeding 250 kW
  - 8501.53.85 — >250 kW
  - Precedent: CBP NY N329048 — 375 kW motor → 8501.53.8060; 200 kW motor → 8501.53.8040
- **D2-GAP-013 status**: `data_pending` — 8-digit/10-digit resolution requires confirmed kW rating of the test-run entity (ent_221). Framework documented. No entity kW spec in D-CLASS-ENG corpus. Non-blocking; heading 8501.53 remains stable/high.
- **Source**: `pta/traction-motor_us.md`; `HS - DR - US Traction Motor HTS Classification Refinement.md`

### European Union
- **Code**: 8501.53.50
- **Heading**: AC motors, multi-phase, >75 kW (≤150 kW bracket)
- **Ruling corroboration**: EU BTI CZBTI34/018997/2025-580000-04/01 (Czech Republic, 2025) classified an 80 kW AC traction motor *with integrated inverter* at CN 8501.53.50.10. Standalone motor without inverter → 8501.53.50 with higher confidence (no composite good complexity).
- **Source**: `pta/traction-motor_eu.md`

### India (ITC-HS)
- **Code**: 8501.53.30 — **"Traction motor"** (dedicated code)
- **Heading**: Electric motors — AC multi-phase >75 kW — Traction motor
- **Note**: India ITC-HS created a dedicated 8-digit code explicitly for traction motors. This is the most certain India classification in the entire pilot — eliminates subheading ambiguity entirely.
- **Source**: `pta/traction-motor_india.md`

---

## Ruling Corroboration

EU BTI CZBTI34/018997/2025-580000-04/01 is **corroborating evidence only** — it confirms the PTA classification at 8501.53, it does not override it. No ruling override was applied. The BTI addressed a motor with integrated inverter; standalone motor without inverter is an even cleaner GRI 1 case.

---

## Reconciliation Notes

Clean convergence across all evidence sources. No conflicts. India dedicated code is the model classification for what ITC-HS jurisdiction-specific research can achieve.

## Graph Links

- `classification_node` → [[product_component-traction-motor]]
- `engineering_anchor` → [[traction-motor]]
- `parent_component` → [[electric-drive-unit]]
- `global_anchor` → [[hs_code-8501-53-global]]
- `classified_as` → [[hs_code-8501-53-us]]
- `classified_as` → [[hs_code-8501-53-30-in]]
- `classified_as` → [[hs_code-8501-53-50-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
