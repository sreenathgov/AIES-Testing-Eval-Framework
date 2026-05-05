---
agent: PTA
component: Traction Inverter Module
entity_id: ent_196
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
is_composite_flagged: false
hs_code_candidate: "8504.40"
us_hts_subheading: "8504.40.40"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8504.40 — Static converters; subheading 8504.40.40 — Speed drive controllers for electric motors
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — DC/AC conversion is electrical machinery (Chapter 85); Chapter 87 vetoed |
| Section XV Note 2 | No | SiC/IGBT semiconductor module on DBC substrate is not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1.** US HTS heading 8504 covers "electrical transformers, static converters (for example, rectifiers) and inductors." A traction inverter module converts DC battery power to variable-frequency AC for the traction motor — this is a static converter by function.

Subheading 8504.40 covers static converters. Within 8504.40, subheading 8504.40.40 covers "speed drive controllers for electric motors." An EV traction inverter is functionally a speed drive controller: it produces variable-frequency, variable-amplitude AC output to control traction motor torque and speed. This is the most specific available US subheading.

Note 2(f) was decisive in routing away from Chapter 87 (vehicle parts). The traction inverter transforms DC → AC electricity regardless of its automotive application.

## Classification

- **Code**: 8504.40.40
- **Subheading text**: Speed drive controllers for electric motors
- **Heading text**: Electrical transformers, static converters (for example, rectifiers) and inductors; parts thereof
