---
agent: PTA
component: DC-DC Converter
entity_id: ent_216
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
material_composition: Power electronics assembly for high-voltage to low-voltage DC conversion
is_composite_flagged: false
hs_code_candidate: "8504.40"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8504 — transformers and static converters; subheading 8504.40
pilot_batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — power electronics assembly is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Analysis

**Resolved at GRI 1.** Heading 8504 covers electrical transformers, static converters (for example, rectifiers) and inductors. DC-DC Converter = static converter (DC at one voltage → DC at another voltage, no moving parts). Subheading 8504.40 explicitly covers static converters.

**Competing headings**: 8708 excluded by Section XVII Note 2(f). 8543 (residual) not applicable — 8504 specifically covers static converters.

## Classification

- **Code**: 8504.40
- **Subheading text**: Static converters
- **Heading text**: Electrical transformers, static converters (for example, rectifiers) and inductors
