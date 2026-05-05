---
agent: PTA
component: On-Board Charger (OBC)
entity_id: ent_215
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
material_composition: Power electronics assembly for AC to DC conversion
is_composite_flagged: false
hs_code_candidate: "8504.40"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8504 — static converters including rectifiers; subheading 8504.40
pilot_batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — power electronics assembly (rectifier) is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Analysis

**Resolved at GRI 1.** Heading 8504 explicitly names **rectifiers** as examples of static converters. OBC converts AC grid power to DC for battery charging — it is a rectifier. Subheading 8504.40 covers static converters including rectifiers.

**Competing headings considered**:
- 8507 (battery charger parts) — rejected: OBC's primary function is AC-to-DC conversion (rectification), not battery accessory. The battery is the charging target; OBC is the conversion apparatus.
- 8708 — excluded by Section XVII Note 2(f).

## Classification

- **Code**: 8504.40
- **Subheading text**: Static converters
- **Heading text**: Electrical transformers, static converters (for example, rectifiers) and inductors
