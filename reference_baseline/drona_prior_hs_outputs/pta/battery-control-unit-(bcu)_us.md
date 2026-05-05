---
agent: PTA
component: Battery Control Unit (BCU)
entity_id: ent_169
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Centralized multilayer PCBA with microcontrollers, cell-balancing circuits, protection ICs, and communication interfaces housed in plastic or die-cast aluminum enclosure
is_composite_flagged: false
hs_code_candidate: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8537 — boards and panels for electric control ≤1,000V; subheading 8537.10.91 (programmable controllers/dedicated control boards)
ruling_flag: "None — standalone BCU PCBA; CBP H155376 does not apply (that ruling addressed battery pack as composite good)"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 (vehicles/parts) vetoed |
| Section XV Note 2 | No | PCBA is not a part of general use as defined by Note 2 to Section XV |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL function confirmed; BCU acts on battery state measurements (switching, protection, balancing) — measurement inputs serve the control function; Chapter 90 not applicable |
| Chapter 84 Note 5(E) | **Yes** | BCU is a dedicated controller — firmware executes battery management algorithms; not a general-purpose ADP machine; heading 8471 is excluded |

## GRI Analysis

**Resolved at GRI 1** per [[usitc_hts_ch85_2026_complex]].

Heading [[hs_code-8537-10-global]] covers "boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity." A standalone BCU PCBA is an assembly of:
- Protection MOSFETs and solid-state relays (heading 8536 — apparatus for making/breaking circuits)
- Cell-balancing switches (heading 8536 — switching apparatus)
- Microcontrollers executing control firmware (not the principal apparatus but the control brain)

Two-or-more-apparatus threshold: met. Protection devices + balancing switches both fall within heading 8536.

**Competing heading 8507** (storage batteries): EN 85.07 notes that a battery management circuit presented together with battery cells as a single article may classify as 8507 under GRI 3(b). **This does not apply here**: a standalone BCU PCBA is not presented with battery cells. It is traded as a discrete assembly at the component level, not as a battery article.

**Competing heading 8471** (ADP machines): Chapter 84 Note 5(E) excludes dedicated controllers that perform specific non-data-processing functions. The BCU executes battery state monitoring, protection switching, and cell balancing — functions specific to battery management. Note 5(E) exclusion confirmed; 8471 does not apply.

**Resolved at GRI 1**: Heading [[hs_code-8537-10-global]] is the specific and complete provision for a standalone battery control PCBA at ≤1,000V.

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.91 — programmable controllers or other dedicated control boards, for a voltage not exceeding 1,000V
- **Code**: 8537.10.91
- **Basis**: GRI 1; heading 8537 covers the article by specific text; subheading 8537.10.91 captures dedicated control boards at ≤1,000V

## Ruling Flag

No applicable CBP ruling for standalone BCU PCBA. CBP HQ H155376 (battery pack + BMS + cells → 8507.80) is not applicable; H155376 addresses a composite article including cells. A standalone BCU PCBA without battery cells is not a storage battery.

## Graph Links

- `classification_node` → [[product_component-battery-control-unit-bcu]]
- `engineering_anchor` → [[battery-control-unit-(bcu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
