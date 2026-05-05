---
agent: PTA
component: Battery Disconnect Unit (BDU)
entity_id: ent_171
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Heavy-duty electromechanical assembly housing high-voltage contactors, pyrotechnic fuses (pyrofuse), and current shunts on a dedicated power board, in a metal or reinforced plastic housing
is_composite_flagged: false
hs_code_candidate: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8537 — boards and panels for electric control ≤1,000V; subheading 8537.10.91 (dedicated control boards)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — electrical switching/protection apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | HV contactors and fuses are not parts of general use as defined by Note 2 to Section XV |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL function; current shunt measurement serves the protection/disconnection control function |

## GRI Analysis

**Resolved at GRI 1** per [[usitc_hts_ch85_2026_complex]].

Heading [[hs_code-8537-10-global]] covers boards, panels, and bases "equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity."

The BDU assembly contains:
- **HV contactors** → heading 8536.49 (contactors for circuits ≤1,000V)
- **Pyrotechnic fuse (pyrofuse)** → heading 8536.50 (other switches; pyrofuses are single-use protective switching devices)
- Current shunts (passive measurement elements, not classified as primary apparatus but as accessories to the board)

Two-or-more-apparatus threshold: met. HV contactors (8536.49) and pyrofuse (8536.50) are each apparatus of heading 8536, present on the same power board. The board as a whole is a switching/protection assembly for electric control — it controls battery pack isolation in response to fault conditions and operational commands.

**Competing heading 8536** (individual apparatus): Individual contactors and fuses would be classified under 8536. However, the BDU is a **combined assembly** integrating multiple 8536 apparatus onto a single board/housing designed to function as a unit for electric control. This is precisely the class of article heading 8537 was created to capture. GRI 1 resolves directly at 8537.10.

**Competing heading 8543** (electrical apparatus not elsewhere specified): 8543 is residual. Heading 8537 specifically covers multi-apparatus electrical control boards; 8543 does not apply.

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.91 — programmable controllers or other dedicated control boards, for a voltage not exceeding 1,000V
- **Code**: 8537.10.91
- **Basis**: GRI 1; BDU is a dedicated protection/control board with ≥2 apparatus of 8536; "other dedicated control boards" captures protection-function assemblies

## Graph Links

- `classification_node` → [[product_component-battery-disconnect-unit-bdu]]
- `engineering_anchor` → [[battery-disconnect-unit-(bdu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
