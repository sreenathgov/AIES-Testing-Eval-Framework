---
agent: PTA
component: NdFeB Permanent Magnets
entity_id: ent_207
jurisdiction: US
fundamental_function: ENERGY_CONVERSION
material_composition: Neodymium-Iron-Boron alloy with Dysprosium and Terbium diffusion coating; sintered rare-earth permanent magnet
is_composite_flagged: false
hs_code_candidate: "8505.11.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8505 — electromagnets; permanent magnets; subheading 8505.11 (permanent magnets of metal)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | No | Note 2(f) applies to "electrical machinery" (Chapter 85 apparatus); permanent magnets are passive metallic articles, not active electrical apparatus. Note 2(f) does not veto or route these items — heading 8505 itself is in Chapter 85. No Chapter 87 conflict arises. |
| Section XV Note 2 | No | Permanent magnets are not parts of general use as defined by Note 2 to Section XV |
| Note 1 to Chapter 73 (iron/steel articles) | No | Note 1 to Chapter 73 excludes articles of Section XVI (Chapter 85). Heading 8505 is in Chapter 85 (Section XVI). Fe-based alloys used in magnets are excluded from Chapter 73 by this Note and captured in heading 8505.11. |
| Chapter 90 Note 2 | No | Permanent magnets are not measuring instruments |

## GRI Analysis

**Resolved at GRI 1** per [[usitc_hts_ch85_2026_complex]].

Heading 8505 covers "Electromagnets; permanent magnets and articles designed to become permanent magnets after magnetisation; electromagnetic or permanent magnet chucks, clamps and similar holding devices; electromagnetic couplings, clutches and brakes; electromagnetic lifting heads; parts thereof."

Subheading 8505.11 covers "Permanent magnets and articles designed to become permanent magnets after magnetisation: Of metal."

NdFeB (Neodymium-Iron-Boron) permanent magnets are sintered metallic alloy magnets — they are unambiguously "permanent magnets of metal" within subheading 8505.11. GRI 1 is determinative.

**Why not Chapter 73 or Chapter 76 (metallic articles)?**

Note 1 to Chapter 73 excludes articles of Section XVI. Heading 8505 is in Section XVI. NdFeB magnets in their traded form are designed to become or are permanent magnets — they fall within heading 8505.11 regardless of their metallic alloy composition.

**Why not heading 8301 or 8505.90 (parts)?**

8301 covers locks, padlocks, clasps — not applicable. 8505.90 covers parts; NdFeB permanent magnets are the article itself, not a part of another magnet assembly. 8505.11 captures the article directly.

**US statistical code**: US HTS 8505.11.00 — Permanent magnets and articles designed to become permanent magnets after magnetisation, of metal. Single US statistical suffix at the 8-digit level.

## Classification

- **Heading**: 8505
- **Subheading**: 8505.11 — permanent magnets of metal
- **Code**: 8505.11.00
- **Basis**: GRI 1; NdFeB is a metallic permanent magnet; heading 8505.11 is the specific provision

## Graph Links

- `classification_node` → [[product_component-ndfeb-permanent-magnets]]
- `engineering_anchor` → [[ndfeb-permanent-magnets]]
- `parent_component` → [[rotor-assembly]]
- `classified_as` → [[hs_code-8505-11-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
