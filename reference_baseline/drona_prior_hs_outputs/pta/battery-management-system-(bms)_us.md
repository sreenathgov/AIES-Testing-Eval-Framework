---
agent: PTA
component: Battery Management System (BMS)
entity_id: ent_217
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Printed circuit board assembly with monitoring ICs, microcontrollers, cell-balancing circuits, communication interfaces (CAN/LIN)
is_composite_flagged: false
hs_code_candidate: "8537.10"
gri_path: GRI_1
stability: stable
confidence: high
confidence_note: CBP H155376 was rejected in WS-6 because it addresses a battery pack, not a standalone BMS PCBA; 8537.10 is established for the present article
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8537 — boards and panels for electric control ≤1,000V; subheading 8537.10
ruling_flag: "CBP HQ H155376 addressed battery PACK (composite good), not standalone BMS PCBA — override rejected"
pilot_batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | NOT APPLICABLE — ACTIVE_CONTROL function; BMS acts on measurements (switching, balancing) rather than purely measuring. Chapter 90 instruments measure; BMS acts on measurements. |

## GRI Analysis

**Resolved at GRI 1.**

Heading 8537 covers boards and panels equipped with two or more apparatus of heading 8535 or 8536, for electric control. A standalone BMS PCBA is an assembly of cell-balancing switches (8536 class), protection devices (8535 class), and control microcontrollers — electric control apparatus.

### Competing heading: 8507 (storage batteries)

EN 85.07 states batteries presented with ancillary monitoring circuits are classifiable in 8507 (composite good, GRI 3(b)). This is the basis for CBP H155376 (8507.80.80).

**Distinction**: This reasoning applies only when the BMS is presented **together with battery cells** as a combined article. A standalone BMS PCBA without battery cells is not a storage battery. EN 85.07 composite rule does not apply.

**Competing heading: 8543** (residual electrical apparatus) — not applicable; 8537 specifically covers this configuration.

## Classification

- **Code**: 8537.10
- **Subheading text**: Boards, panels for electric control — for a voltage not exceeding 1,000V
- **Heading text**: Boards, panels equipped with apparatus of 8535/8536 for electric control

## Ruling Flag

CBP HQ H155376 (June 22, 2011): held BMS+cells+housing → 8507.80.80 as composite good. **PTA position after WS-6 refinement**: H155376 addressed a battery PACK, not a standalone BMS control board. The EN 85.07 ancillary circuit exception applies only when presented with the battery cells as a combined article. Override rejected; 8537.10 stands for the standalone PCBA.
