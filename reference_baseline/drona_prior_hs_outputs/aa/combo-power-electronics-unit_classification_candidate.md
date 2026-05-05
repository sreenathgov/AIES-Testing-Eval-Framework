---
agent: AA
component: Combo Power Electronics Unit
entity_id: ent_267
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
essential_character_reasoning: "OBC (AC→DC charger, 7–22kW) gives essential character by value, power rating, and commercial function. GRI 3(b) → 8504.40. Jurisdiction-specific subheadings differ by tariff structure: US 8504.40.70 (battery chargers), EU 8504.40.60 (accumulator chargers), India 8504.40.90 (Other — OBC is not a DC→AC inverter per CAAR Valco)."
date: 2026-04-02
---

## Reconciliation

### Source Inputs
- PTA (US): [[combo-power-electronics-unit_us]] — 8504.40.70, GRI 3(b), OBC essential character
- PTA (EU): [[combo-power-electronics-unit_eu]] — 8504.40.60, GRI 3(b), EU CN accumulator charger provision
- PTA (India): [[combo-power-electronics-unit_india]] — 8504.40.90, GRI 3(b), CAAR Valco inverter ruling exculpatory
- DA-F10: CAAR Valco confirms 8504.40.10 = DC→AC only → Combo Unit (AC→DC OBC) = 8504.40.90
- DA-F11: EU CN 8504.40.60 specific provision for accumulator chargers
- DA-F12: US HTS 8504.40.70 covers battery chargers
- DA-F13: No heading-level divergence; subheading differences are tariff-structural

### Classification Analysis

**Section XVII Note 2(f)**: All three sub-components (OBC, DC-DC, PDU) are Chapter 85 electrical apparatus. Chapter 87 is vetoed. Classification is within Chapter 85. [[wco_2022_section_87_complex]] confirms.

**GRI 1 fails**: No single heading covers the combined OBC + DC-DC + PDU assembly as a unified article.

**GRI 3(a)**: OBC → 8504.40 (static converter/charger); DC-DC → 8504.40 (static converter); PDU → 8537.10 (control/distribution board). Two headings compete: 8504.40 and 8537.10. Most specific for the dominant sub-components: 8504.40.

**GRI 3(b) — Essential Character**:
- OBC: 7–22kW, highest power function, highest value sub-component, primary commercial differentiator
- DC-DC: 1–3kW, lower power, secondary function
- PDU: switching/distribution, ancillary

OBC gives essential character by bulk, value, and primary commercial function. The Combo Unit is marketed and traded as an integrated charging module with DC-DC capability. → Heading 8504.40.

**Jurisdiction-specific subheading resolution**:

*US (8504.40.70)*: HTS 8504.40.70 = "battery chargers." OBC charges the HV Li-ion traction battery from AC supply = battery charger. 8504.40.70 applies.

*EU (8504.40.60)*: EU CN 8504.40.60 = "accumulator chargers." OBC charges the HV accumulator (Li-ion traction battery) = accumulator charger. EU CN 8504.40.60 is the specific provision; it applies directly.

*India (8504.40.90)*: India ITC-HS splits 8504.40 as: 8504.40.10 (Electric inverter — DC→AC) vs. 8504.40.90 (Other). CAAR Valco advance ruling confirmed that 8504.40.10 is limited to DC→AC inverters. The OBC is an AC→DC rectifier/charger. The DC-DC converter is a DC→DC step-down converter. Neither is a DC→AC inverter. Both sub-components → 8504.40.90. The Combo Unit = 8504.40.90.

**Subheading divergence classification**: The US/EU/India codes all sit within heading 8504.40. The subheading differences (8504.40.70 / 8504.40.60 / 8504.40.90) reflect different tariff schedule architectures, not substantive disagreement about the article's nature. All three jurisdictions agree: OBC-dominant assembly, heading 8504.40, static converter/charger subheading. `jurisdiction_divergence: false`.

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 8504.40.70 | GRI 3(b); OBC essential character; HTS "battery chargers" provision | stable | high |
| EU | 8504.40.60 | GRI 3(b); OBC essential character; EU CN "accumulator chargers" specific provision | stable | high |
| India | 8504.40.90 | GRI 3(b); OBC essential character; not DC→AC inverter (CAAR Valco) → Other | stable | high |

## Graph Links

- `classification_node` → [[product_component-combo-power-electronics-unit]]
- `classified_as (US)` → [[hs_code-8504-40-70-us]]
- `classified_as (EU)` → [[hs_code-8504-40-60-eu]]
- `classified_as (IN)` → [[hs_code-8504-40-90-in]]
- `ruling_anchor` → [[hs_code-8504-40-global]]
- `da_source` → [[da_memo_tb2_battery_pack]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
