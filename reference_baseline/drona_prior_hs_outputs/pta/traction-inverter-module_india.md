---
agent: PTA
component: Traction Inverter Module
entity_id: ent_196
jurisdiction: India
fundamental_function: ENERGY_CONVERSION
is_composite_flagged: false
hs_code_candidate: "8504.40"
india_itc_hs_subheading: "8504.40.10"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_schedule_of_tariff_commitment_ev_complex.md
source_section: Heading 8504.40 — Static Converters; subheading 85044010 — Electric inverter
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — DC/AC conversion is electrical machinery (Chapter 85); Chapter 87 vetoed |
| Section XV Note 2 | No | Not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1.** India ITC-HS heading 8504.40 covers static converters. India has a dedicated subheading for electric inverters: 85044010 "Electric inverter." A traction inverter module is an electric inverter — it converts DC battery voltage to variable-frequency AC for the traction motor.

This is the most specific available India subheading and eliminates subheading-level ambiguity. India's 85044010 dedicated classification for electric inverters provides high confidence.

## Classification

- **Code**: 8504.40.10
- **Subheading text**: Electric inverter
- **Heading text**: Electrical Transformers, Static Converters (For Example, Rectifiers) And Inductors
