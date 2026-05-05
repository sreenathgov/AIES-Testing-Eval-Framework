---
agent: PTA
component: High-Voltage Contactor
entity_id: ent_144
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Heavy-duty, electrically operated electromagnetic switch
is_composite_flagged: false
hs_code_candidate: "8536.49"
gri_path: GRI_1
stability: stable
confidence: high
confidence_note: Voltage confirmed ≤1,000V via WS-6 refinement; heading 8536.49 is established and heading 8535 is excluded
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8536 — switches/relays ≤1,000V; subheading 8536.49
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electromagnetic switch is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Analysis

**Resolved at GRI 1.**

Heading 8536 covers electrical apparatus for switching or protecting electrical circuits for ≤1,000V. Subheading 8536.49 covers "other relays: for a voltage exceeding 60V but not exceeding 1,000V" — the correct bracket for EV HV contactors on standard 400V/800V architectures.

**Competing headings considered**:
- 8535 — applicable if operating voltage >1,000V; not confirmed by entity data
- 8708 — excluded by Section XVII Note 2(f)

**Voltage resolution**: WS-6 refinement confirmed operating voltage does not exceed 1,000V, keeping the article within heading 8536. Heading 8535 is excluded on the current record.

## Classification

- **Code**: 8536.49
- **Subheading text**: Other relays — for a voltage exceeding 60V but not exceeding 1,000V
- **Heading text**: Electrical apparatus for switching or protecting electrical circuits...for a voltage not exceeding 1,000V
