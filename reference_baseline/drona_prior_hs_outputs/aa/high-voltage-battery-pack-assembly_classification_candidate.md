---
agent: AA
component: HV Battery Pack Assembly
entity_id: ent_100
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
essential_character_reasoning: "Li-ion cells give essential character to the pack assembly (GRI 3(b)). BMS, thermal management, structural enclosure, and HV wiring harness are ancillary. CBP HQ H155376 and H309485 both confirm 8507.60.00. EU CN and India ITC-HS have single 8-digit under 8507.60 → 8507.60.00."
date: 2026-04-02
---

## Reconciliation

### Source Inputs
- PTA (US): [[high-voltage-battery-pack-assembly_us]] — 8507.60.00, GRI 3(b), H155376 + H309485
- PTA (EU): [[high-voltage-battery-pack-assembly_eu]] — 8507.60.00, GRI 3(b)
- PTA (India): [[high-voltage-battery-pack-assembly_india]] — 8507.60.00, GRI 3(b)
- DA-F7: H155376 directly supports 8507.60.00; cells = essential character
- DA-F8: H309485 corroborates across configurations
- DA-F9: WCO-harmonized 8507.60 → single 8-digit (8507.60.00) across EU and India

### Classification Analysis

**GRI 3(b) — Essential Character**:
The HV Battery Pack Assembly contains: Li-ion cells (multiple modules), Battery Management System (BMS), thermal management system (liquid cooling plates, coolant manifolds), HV junction box, wiring harness, and structural aluminum enclosure.

The Li-ion cells are the energy storage medium — they constitute the primary mass, value, and functional purpose of the assembly. The BMS, thermal management, and structural enclosure are necessary supporting elements but they do not change what the article fundamentally is: a lithium-ion energy storage assembly. Cells give essential character.

**Ruling corroboration**:
- CBP HQ H155376: Li-ion battery pack with BMS electronics = 8507.60.00. Direct match.
- CBP HQ H309485: Li-ion rack assembly = 8507.60.00. Confirms heading independence from configuration.

**Cross-jurisdiction consistency**:
- EU CN: 8507.60 has single 8-digit 8507.60.00. No EU ruling needed; tariff text is unambiguous.
- India ITC-HS: 8507.60.00 is the single 8-digit under this heading. No subdivision.
- All three jurisdictions = 8507.60.00.

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 8507.60.00 | GRI 3(b); cells essential character; H155376 + H309485 | stable | high |
| EU | 8507.60.00 | GRI 3(b); cells essential character; EU CN single 8-digit | stable | high |
| India | 8507.60.00 | GRI 3(b); cells essential character; India ITC-HS single 8-digit | stable | high |

## Graph Links

- `classification_node` → [[product_component-hv-battery-pack-assembly]]
- `classified_as (US)` → [[hs_code-8507-60-00-us]]
- `classified_as (EU)` → [[hs_code-8507-60-00-eu]]
- `classified_as (IN)` → [[hs_code-8507-60-00-in]]
- `ruling_anchor` → [[hs_code-8507-60-global]]
- `da_source` → [[da_memo_tb2_battery_pack]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
