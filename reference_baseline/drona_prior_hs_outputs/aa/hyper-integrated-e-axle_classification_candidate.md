---
agent: AA
component: Hyper-Integrated E-Axle
entity_id: ent_269
batch: TB-2
jurisdiction_divergence: true
stability_us: stable
stability_eu: stable
stability_india: contested
confidence_us: high
confidence_eu: high
confidence_india: medium
gri_path: GRI_3b_with_GRI_3c_fallback
i4_flag: true
essential_character_reasoning: "8-in-1 assembly (motor + gearbox + inverter + OBC + DC-DC + BDU + suspension + steering actuators) in a single vehicular chassis platform. GRI 3(b): vehicular drivetrain/chassis platform essential character → 8708.99 (US/EU). GRI 3(c) fallback documented: competing headings 8483/8501/8504/8537/8708 — 8708 is last numerically → 8708.99 governs by GRI 3(c) if 3(b) indeterminate. India: same contested position as Integrated E-Axle."
eu_8digit_confirmed: "8708.99.97"
eu_8digit_basis: "Same as Integrated E-Axle. 8-in-1 assembly is a fortiori vehicular drivetrain. EU OJ tariff suspension records confirm 8708.99.97 for complex multi-component drivetrain assemblies in aluminum housings. 8708.99.93 excluded (multi-material — not closed-die forged steel). Default cascade → 8708.99.97."
eu_8digit_gap_status: "D2-GAP-008 closed"
india_monitor_flag: true
india_monitor_reason: "Bombay HC BEV axle classification judgment pending — could flip India position from 8501.53.30 to 8708.99.00. GRI 3(c) path (8708.99.00) arguably stronger for 8-in-1 than for 3-in-1."
founder_override_provenance: true
founder_override_scope: "missing_primary_text_india_case_law"
founder_override_basis: "ey_pwc_secondary_authority"
founder_override_note: "Founder-approved temporary provenance bridge for missing Indian primary text. EY and PwC secondary summaries are accepted for the test run only and must be replaced when the underlying India judgments/orders are acquired."
primary_text_status: "not_yet_acquired"
secondary_authority_sources:
  - {"source": "EY / ACMA Tax & Regulatory Alert (Aug 2022)", "citation": "CAAR/Del/Volvo Auto/08/2022", "forum": "CAAR (Delhi)", "date": "2022-08", "holding_summary": "EV kits presented together in CKD form treated as complete vehicle under GRI 2(a); used as secondary aggregation support for highly integrated EV powertrain imports.", "source_type": "secondary", "source_publisher": "EY", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
  - {"source": "PwC Customs & Trade Newsletter (Oct 2024)", "citation": "CAAR/MUM/ARC/153/2024", "forum": "CAAR (Mumbai)", "date": "2024-10", "holding_summary": "CAAR applied Section XVI Note 2(b) part-classification logic, providing secondary interpretive support for part-vs-independent-article analysis in integrated systems.", "source_type": "secondary", "source_publisher": "PwC", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
override_applies_to_jurisdictions: [IN]
override_review_required_when_primary_acquired: true
date: 2026-04-02
refinement_date: "2026-04-06"
---

## Reconciliation

### Source Inputs
- PTA (US): [[hyper-integrated-e-axle_us]] — 8708.99.68, GRI 3(b)/3(c), NY N329827 by analogy
- PTA (EU): [[hyper-integrated-e-axle_eu]] — 8708.99 heading-level, pending EU CN 8-digit
- PTA (India): [[hyper-integrated-e-axle_india]] — 8501.53.30, contested/medium, GRI 3(c) alternative = 8708.99.00
- DA-F4: NY N329827 applies by analogy; H329719 inapplicable
- DA-F5: India legally unsettled; CAAR VCU/PCU counter-signal; same uncertainty as Integrated E-Axle

### US Classification

**Code**: 8708.99.68
**GRI path**: GRI 3(b) primary; GRI 3(c) fallback documented

**GRI 3(b) analysis**:
The 8-in-1 assembly integrates: (1) traction motor + gearbox + inverter (the core drivetrain — same as Integrated E-Axle), (2) OBC + DC-DC (power electronics), (3) BDU (HV distribution), (4) suspension + steering actuators. The article is a complete vehicle chassis platform with integrated propulsion, charging, and chassis control. Its commercial identity is a vehicular platform, not any single electrical component.

Essential character: vehicular chassis/drivetrain platform → heading 8708 (parts and accessories of motor vehicles). NY N329827 supports this by analogy: if a 3-in-1 e-axle is 8708.99, an 8-in-1 assembly is a fortiori vehicular.

**GRI 3(c) fallback**: If a tribunal finds GRI 3(b) indeterminate (because no single function clearly dominates an 8-function assembly), GRI 3(c) governs: the heading occurring last numerically. Competing headings: 8483 (gearbox), 8501 (motor), 8504 (OBC + DC-DC), 8537 (BDU), 8708 (vehicular). 8708 is last numerically → 8708.99 governs. Both GRI 3(b) and 3(c) resolve identically at 8708.99.

**Classified as**: → [[hs_code-8708-99-68-us]]

### EU Classification

**Code**: 8708.99.97 (8-digit confirmed — D2-GAP-008 closed)
**GRI path**: GRI 3(b) primary; GRI 3(c) fallback — same as US analysis; GRI 6 at subheading level
**8-digit resolution**: EU OJ tariff suspension records confirm 8708.99.97 for complex multi-component drivetrain assemblies in aluminum housings. 8708.99.93 excluded (multi-material — not closed-die forged steel). Default cascade → **8708.99.97**. Resolution basis: highly persuasive analogy (a fortiori from 3-in-1).

**Classified as**: → [[hs_code-8708-99-97-eu]]

### India Classification

**Code**: 8501.53.30 (CONTESTED)
**GRI path**: GRI 3(b) — motor-dominant secondary source position
**Stability**: contested
**Confidence**: medium

**Position**: Same contested analysis as Integrated E-Axle. India secondary sources favor 8501.53 for motor-dominant assemblies. However, the 8-in-1 configuration makes the motor-dominant essential character analysis weaker: with 8 sub-functions, the "dominant" function is less obvious than in a 3-in-1 assembly.

**GRI 3(c) alternative India**: If GRI 3(b) is indeterminate (8-in-1 makes essential character analysis genuinely ambiguous), GRI 3(c) applies: competing headings 8483/8501/8504/8537/8708 → 8708 last numerically → **8708.99.00**. This GRI 3(c) route is the more defensible India position for the hyper-integrated configuration.

**CAAR context**: Same as Integrated E-Axle — no binding ruling, CAAR VCU/PCU creates indirect 8708 pressure.

**Classified as**: → [[hs_code-8501-53-30-in]] (contested; GRI 3(c) alternative = 8708.99.00 documented)

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 8708.99.68 | GRI 3(b); vehicular platform essential character; NY N329827 analogy | stable | high |
| EU | 8708.99.97 | GRI 3(b); vehicular platform; EU OJ analogy (D2-GAP-008 closed) | stable | high |
| India | 8501.53.30 | GRI 3(b); motor-dominant; CONTESTED (GRI 3(c) → 8708.99.00; monitor: Bombay HC) | contested | medium |

## Jurisdiction Divergence Note

Same heading-level divergence as Integrated E-Axle. Notably, the GRI 3(c) path (8708.99.00) is arguably stronger for the hyper-integrated configuration than for the standard Integrated E-Axle, because the 8-in-1 makes motor-dominant essential character less defensible. Post-domain protocol: Monitor Bombay HC judgment.

## Graph Links

- `classification_node` → [[product_component-hyper-integrated-e-axle]]
- `classified_as (US)` → [[hs_code-8708-99-68-us]]
- `classified_as (EU)` → [[hs_code-8708-99-97-eu]]
- `classified_as (IN)` → [[hs_code-8501-53-30-in]]
- `ruling_anchor (US)` → [[hs_code-8708-99-global]]
- `da_source` → [[da_memo_tb2_e_axle]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
