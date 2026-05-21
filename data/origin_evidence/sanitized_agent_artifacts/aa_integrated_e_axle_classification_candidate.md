<!-- Reviewer-safe sanitized forensic artifact. This file evidences artifact origin only and is not external legal authority. -->

---
agent: AA
component: Integrated E-Axle
entity_id: ent_187
batch: TB-2
jurisdiction_divergence: true
stability_us: stable
stability_eu: stable
stability_india: contested
confidence_us: high
confidence_eu: high
confidence_india: medium
gri_path: GRI_3b
i4_flag: true
essential_character_reasoning: "Vehicular drivetrain housing integrates motor + gearbox + inverter in a single article; drivetrain function gives essential character (US/EU → 8708.99). India contested: motor-dominant essential character per secondary sources → 8501.53.30; but CAAR VCU/PCU ruling and CAAR BEV Axle denial create genuine legal uncertainty."
eu_8digit_confirmed: "8708.99.97"
eu_8digit_basis: "Analogical: EU OJ tariff suspension records classify complex multi-component drivetrain assemblies (transfer cases, gearboxes in aluminum housings) under 8708.99.97 'Other'. 8708.99.93 excluded (not closed-die forged steel). 8708.99.10 excluded (no end-use authorization). Default cascade → 8708.99.97."
eu_8digit_gap_status: "D2-GAP-008 closed"
india_monitor_flag: true
india_monitor_reason: "Bombay HC BEV axle classification judgment pending — could flip India position from 8501.53.30 to 8708.99.00"
founder_override_provenance: true
founder_override_scope: "missing_primary_text_india_case_law"
founder_override_basis: "ey_pwc_secondary_authority"
founder_override_note: "Founder-approved temporary provenance bridge for missing Indian primary text. EY and PwC secondary summaries are accepted for the test run only and must be replaced when the underlying India judgments/orders are acquired."
primary_text_status: "not_yet_acquired"
secondary_authority_sources:
  - {"source": "EY / ACMA Tax & Regulatory Alert (Aug 2022)", "citation": "CAAR/Del/Volvo Auto/08/2022", "forum": "CAAR (Delhi)", "date": "2022-08", "holding_summary": "EV kits presented together in CKD form treated as complete vehicle under GRI 2(a); used as secondary aggregation support for India EV drivetrain analysis.", "source_type": "secondary", "source_publisher": "EY", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
  - {"source": "PwC Customs & Trade Newsletter (Oct 2024)", "citation": "Iljin Automotive Pvt. Ltd. / hub assembly axle logic", "forum": "CESTAT (Chennai)", "date": "2025-08-21", "holding_summary": "Hub assembly classified with axle system, reinforcing axle-system reasoning relevant to integrated EV drive assemblies.", "source_type": "secondary", "source_publisher": "PwC", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
override_applies_to_jurisdictions: [IN]
override_review_required_when_primary_acquired: true
date: 2026-04-02
refinement_date: "2026-04-06"
---

## Reconciliation

### Source Inputs
- PTA (US): [[integrated-e-axle_us]] — 8708.99.68, GRI 3(b), NY N329827
- PTA (EU): [[integrated-e-axle_eu]] — 8708.99 heading-level, pending EU CN 8-digit
- PTA (India): [[integrated-e-axle_india]] — 8501.53.30, contested/medium, CAAR BEV Axle denied
- DA-F4: NY N329827 governs US; H329719 inapplicable (different fact pattern)
- DA-F5: India legally unsettled; CAAR VCU/PCU counter-signal documented
- DA-F6: EU aligns with US ruling direction; no EU-specific ruling found

### US Classification

**Code**: 8708.99.68
**GRI path**: GRI 3(b) — essential character
**Essential character**: The Integrated E-Axle is a unified structural housing containing a traction motor, single-speed reduction gearbox, and power inverter. The housing is a vehicular drivetrain module designed to replace the traditional axle + motor + gearbox architecture. Its commercial identity and primary function are automotive drivetrain, not standalone electrical apparatus.

**Ruling authority**: NY N329827 (CBP) — e-axle with chassis-integrated housing = 8708.99. The fact pattern is directly applicable: unified housing, motor + gearbox + inverter, vehicular function.

**H329719 distinction**: CBP HQ H329719 (8501.53 for EDU where gearbox interfaces with separate transmission) is inapplicable. ent_187 has a unified structural housing and does not connect to a separate transmission — it IS the complete drivetrain.

**Classified as**: → [[hs_code-8708-99-68-us]]

### EU Classification

**Code**: 8708.99.97 (8-digit confirmed — D2-GAP-008 closed)
**GRI path**: GRI 3(b) — essential character, same analysis as US; GRI 6 at subheading level
**Essential character**: Same vehicular drivetrain reasoning applies. EU CN does not have a US-parallel ruling but the WCO-harmonized heading 8708 structure supports the same conclusion.

**8-digit resolution**: EU OJ tariff suspension records classify complex multi-component drivetrain assemblies (transfer cases, gearboxes in cast aluminum housings) under 8708.99.97 "Other". 8708.99.93 excluded (not closed-die forged steel). 8708.99.10 excluded (no end-use authorization). Default cascade → **8708.99.97**. Resolution basis: highly persuasive analogy.

**Classified as**: → [[hs_code-8708-99-97-eu]]

### India Classification

**Code**: 8501.53.30 (CONTESTED)
**GRI path**: GRI 3(b) — essential character (motor-dominant per secondary sources)
**Stability**: contested
**Confidence**: medium

**Position**: India secondary sources classify motor-dominant integrated assemblies under heading 8501 (traction motor essential character → 8501.53). India ITC-HS 8501.53.30 applies (3-phase AC motors > 750W).

**CAAR BEV Axle conflict**: CAAR declined to issue an advance ruling on BEV integrated axle classification. The matter is pending before Bombay High Court. No binding India ruling exists.

**CAAR VCU/PCU counter-signal**: CAAR Valco ruled VCU/PCU = 8708.99.00 (vehicular parts), resisting Chapter 85 routing for EV electronics. This creates indirect pressure toward 8708.99.00 for the e-axle, though the VCU/PCU ruling does not directly govern electro-mechanical assemblies.

**Alternative India position**: 8708.99.00 (vehicular parts, analogous to CAAR VCU/PCU ruling direction; US N329827 as persuasive comparator). This alternative remains legally plausible until Bombay HC decides.

**Classified as**: → [[hs_code-8501-53-30-in]] (contested; alternative 8708.99.00 documented)

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 8708.99.68 | GRI 3(b); NY N329827; vehicular drivetrain essential character | stable | high |
| EU | 8708.99.97 | GRI 3(b); vehicular drivetrain essential character; EU OJ analogy (D2-GAP-008 closed) | stable | high |
| India | 8501.53.30 | GRI 3(b); motor-dominant secondary sources; CONTESTED (monitor: Bombay HC) | contested | medium |

## Jurisdiction Divergence Note

India diverges from US/EU at the heading level (8501 vs. 8708). The divergence reflects:
1. Absence of a binding India ruling (CAAR denied, Bombay HC pending)
2. Competing essential character analyses: motor-dominant (8501) vs. vehicular drivetrain (8708)
3. CAAR's demonstrated willingness to route EV components toward 8708 (VCU/PCU ruling)

Post-domain protocol: Monitor Bombay HC judgment. If 8708.99.00 is affirmed, update India to 8708.99.00 stable/high.

## Graph Links

- `classification_node` → [[product_component-integrated-e-axle-assembly-combining-electric-traction-motor-and-power-inverter]]
- `classified_as (US)` → [[hs_code-8708-99-68-us]]
- `classified_as (EU)` → [[hs_code-8708-99-97-eu]]
- `classified_as (IN)` → [[hs_code-8501-53-30-in]]
- `ruling_anchor (US)` → [[hs_code-8708-99-global]]
- `da_source` → [[da_memo_tb2_e_axle]]
- `graph_index` → [[hs-slice_gate1_graph_index]]
