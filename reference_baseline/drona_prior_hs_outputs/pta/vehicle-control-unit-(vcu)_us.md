---
agent: PTA
component: Vehicle Control Unit (VCU)
entity_id: ent_218
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8537.10"
us_hts_subheading: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8537.10 — Boards and bases equipped with two or more 8535/8536 apparatus, for electric control or distribution, ≤1,000V; Chapter 84 Note 5(E) — dedicated controllers excluded from 8471; subheading 8537.10.91 — Other
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Computational control board with microprocessors is not a part of general use |
| Chapter 90 Note 2 | No | VCU is not a measuring instrument; control is the primary function |

## Pre-Classification Note: 8471 vs 8537 Distinction

Chapter 84 Note 5(E) excludes from heading 8471 (automatic data-processing machines) any machine that is "designed for a specific function other than data processing." A Vehicle Control Unit (VCU) is designed specifically to control EV powertrain and vehicle functions (torque demand, regenerative braking logic, thermal management coordination). It is not a general-purpose computing device.

The VCU therefore does NOT qualify as heading 8471. Classification proceeds to heading 8537.

## GRI Analysis

**Resolved at GRI 1.** US HTS heading 8537 includes "numerical control apparatus." A VCU is precisely numerical control apparatus: a dedicated microprocessor-based controller that executes control algorithms for the vehicle powertrain. It incorporates control boards equipped with multiple electronic components of heading 8536 (switches, relays, protection elements) within a control system architecture.

Heading 8537.10 applies (≤1,000V operating range). Subheading 8537.10.91 (Other) is the correct residual — the VCU is not a motor control center, not assembled for specific domestic appliances.

## Classification

- **Code**: 8537.10.91
- **Subheading text**: Other
- **Heading text**: Boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity, for a voltage not exceeding 1,000 V; including numerical control apparatus
