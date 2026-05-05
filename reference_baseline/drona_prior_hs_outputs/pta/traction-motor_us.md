---
agent: PTA
component: Traction Motor
entity_id: ent_221
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
is_composite_flagged: false
hs_code_candidate: "8501.53"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8501 — electric motors; subheading 8501.53 AC multi-phase >75kW
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electric motor is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Analysis

**Resolved at GRI 1.**

Heading 8501 covers electric motors and generators. Traction motor = electric motor. Subheading 8501.53 for AC multi-phase motors exceeding 75 kW.

**Competing headings**: 8708 excluded by Section XVII Note 2(f).

> **Subheading note**: 8501.32 covers AC multi-phase motors ≤75 kW. 8501.53 covers AC multi-phase motors >75 kW. These are mutually exclusive by power output — not alternatives. A traction motor (typically 150–300 kW) classifies in 8501.53 only.

## Classification

- **Code**: 8501.53
- **Subheading text**: Other AC motors, multi-phase, of an output exceeding 75 kW
- **Heading text**: Electric motors and generators (excluding generating sets)
