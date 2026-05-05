---
agent: AA
component: HV Battery Module
entity_id: ent_133
batch: TB-2
jurisdiction_divergence: false
stability_us: stable
stability_eu: stable
stability_india: stable
confidence_us: high
confidence_eu: high
confidence_india: high
gri_path: GRI_3b
i4_flag: true
essential_character_reasoning: "Li-ion cells give essential character to the module (GRI 3(b)). Cell Contacting System and Cell Module Controller are ancillary. Module is sub-assembly of Battery Pack; same cells-dominant analysis applies at the sub-assembly level. H155376 applicable by analogy."
date: 2026-04-02
---

## Reconciliation

### Source Inputs
- PTA (US): [[high-voltage-battery-module_us]] — 8507.60.00, GRI 3(b)
- PTA (EU): [[high-voltage-battery-module_eu]] — 8507.60.00, GRI 3(b)
- PTA (India): [[high-voltage-battery-module_india]] — 8507.60.00, GRI 3(b)
- DA-F7/F8: H155376 + H309485 support cells-essential-character principle applicable to sub-assemblies
- DA-F9: WCO-harmonized 8507.60.00 across EU and India

### Classification Analysis

**GRI 3(b) — Essential Character**:
The Battery Module contains: Li-ion prismatic or pouch cells (typically 12–24 cells), Cell Contacting System (CCS — busbars, voltage taps, temperature sensors), and a Cell Module Controller (CMC — monitors cell voltages, reports to pack-level BMS).

The Li-ion cells are the energy storage elements. The CCS and CMC are integration and monitoring elements that serve the cells. The module's commercial identity is an energy storage sub-assembly; it is sold/traded as a Li-ion battery module. Cells give essential character.

**Sub-assembly relationship**: The Battery Module is a component of the Battery Pack Assembly. Both are classified at 8507.60.00. This is consistent — a pack-level Li-ion assembly and its module-level sub-assemblies share the same heading when both are traded as discrete articles.

**Ruling applicability**: H155376 covers the pack-level assembly. The cells-give-essential-character principle from H155376 applies by analogy at the module level. H309485 additionally confirms that the 8507.60.00 classification is robust across scales and configurations.

**Cross-jurisdiction consistency**: Same as Battery Pack Assembly. 8507.60.00 is the only 8-digit subheading in all three jurisdictions.

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 8507.60.00 | GRI 3(b); cells essential character; H155376 by analogy | stable | high |
| EU | 8507.60.00 | GRI 3(b); cells essential character; EU CN single 8-digit | stable | high |
| India | 8507.60.00 | GRI 3(b); cells essential character; India ITC-HS single 8-digit | stable | high |

## Graph Links

- `classification_node` → [[product_component-hv-battery-module]]
- `classified_as (US)` → [[hs_code-8507-60-00-us]]
- `classified_as (EU)` → [[hs_code-8507-60-00-eu]]
- `classified_as (IN)` → [[hs_code-8507-60-00-in]]
- `ruling_anchor` → [[hs_code-8507-60-global]]
- `da_source` → [[da_memo_tb2_battery_pack]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
