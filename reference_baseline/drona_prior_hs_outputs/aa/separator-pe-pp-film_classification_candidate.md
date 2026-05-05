---
agent: AA
component: Separator (PE/PP Film)
entity_id: ent_tb3_04
batch: TB-3
jurisdiction_divergence: true
divergence_type: "heading_level"
divergence_note: "US/India: Chapter 39 (cellular plastics, material-first); EU: Chapter 85 (battery part, function-first, <40μm threshold)"
stability_us: stable
stability_eu: stable
stability_india: stable
confidence_us: high
confidence_eu: high
confidence_india: medium
gri_path: GRI_1
i4_flag: false
d_ruling_handoff: true
founder_override_provenance: true
founder_override_scope: "missing_primary_text_india_case_law"
founder_override_basis: "ey_pwc_secondary_authority"
founder_override_note: "Founder-approved temporary provenance bridge for missing Indian primary case texts discussing separator treatment. EY and PwC secondary summaries are accepted for the test run only and must be replaced when the underlying India judgments/orders are acquired."
primary_text_status: "not_yet_acquired"
secondary_authority_sources:
  - {"source": "PwC Customs & Trade Newsletter / Case law collation", "citation": "Exide Industries Ltd. v. Commissioner of Customs (2007)", "forum": "CESTAT", "date": "2007", "holding_summary": "Battery separators in roll form treated as parts of accumulators rather than plastic articles, providing secondary support for a competing Chapter 85 route.", "source_type": "secondary", "source_publisher": "PwC", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
  - {"source": "PwC Customs & Trade Newsletter / Case law collation", "citation": "HBL Nife Power Systems Ltd. v. Commissioner of Customs (2012)", "forum": "CESTAT (Bangalore)", "date": "2012", "holding_summary": "Followed Exide and treated battery separators as accumulator parts, reinforcing the existence of a live India-side Chapter 85 counter-signal.", "source_type": "secondary", "source_publisher": "PwC", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
override_applies_to_jurisdictions: [IN]
override_review_required_when_primary_acquired: true
date: "2026-04-06"
refinement_run: "2026-04-06"
ruling_anchor_us: "CBP HQ 967313 (microporous PE separator → 3921.19.0000; cellular plastic)"
ruling_anchor_eu: "EU Commission Note C/2025/6096 + EU CN 2026 Reg 2025/1926 (PE/PP separator <40μm → 8507.90.31)"
ruling_anchor_india: "ITC-HS Chapter 39 (material-first, cellular plastics; no Indian carve-out equivalent to EU)"
---

## Reconciliation

### Source Inputs
- PTA (US): `separator-pe-pp-film_us.md` — 3921.19.0000, CBP HQ 967313
- PTA (EU): `separator-pe-pp-film_eu.md` — 8507.90.31, Commission Note C/2025/6096
- PTA (India): `separator-pe-pp-film_india.md` — 3921.19.90, material-first
- DA: `da_memo_tb3_battery_materials.md` — CRITICAL divergence flagged; D-RULING handoff required

### Pre-GRI Exclusion Filter Result

All checks negative for US and India (plastics classification). EU Commission Note overrides the general GRI analysis for the EU jurisdiction — the binding Commission classification regulation takes precedence over the general plastics route for EU imports.

### Classification Analysis

**The fundamental divergence** is a deliberate policy choice between two jurisdiction-specific legal frameworks, not a GRI ambiguity:

**US (CBP HQ 967313)**:
- Approach: Material-first (what is it made of?)
- Analysis: Microporous PE/PP = cellular plastic = Chapter 39, Heading 3921
- Rule applied: HTSUS heading text; battery-use does not override material classification for imports of standalone film rolls
- **Result: 3921.19.0000** (cellular plastic plates/sheets/film, other)

**EU (Commission Note C/2025/6096 + EU CN 2026)**:
- Approach: Function-first for specific dimensional threshold (what is it used for, given its physical specifications?)
- Analysis: PE/PP separator <40μm has no commercial use other than Li-ion battery cells → it is, in effect, exclusively a battery part
- Rule applied: Binding Commission classification regulation; EU CN 2026 codified at 8507.90.31
- **Result: 8507.90.31** (parts of electric accumulators: separators of plastics, thickness <40μm)

**India**:
- Approach: Material-first (follows general WCO/HTSUS-aligned approach; no specific carve-out)
- Analysis: Cellular plastic film → Chapter 39, ITC-HS 3921.19.90
- Note: India's battery sector customs classification is evolving; monitor for CBIC advance ruling
- **Result: 3921.19.90** (cellular plastic plates/sheets/film, other)

### US Classification

**Code**: 3921.19.0000 (US HTSUS)
**GRI path**: GRI 1
**Basis**: CBP HQ 967313 binding; microporous PE/PP = cellular plastic; battery-use does not trigger Chapter 85 for standalone separator film import under HTSUS
**Stability**: stable
**Confidence**: high
**Classified as**: → [[hs_code-3921-19-us]]

### EU Classification

**Code**: 8507.90.31 (EU CN 2026)
**GRI path**: GRI 1 (overridden by binding Commission classification regulation)
**Basis**: EU Commission Note C/2025/6096 (binding); EU CN 2026 Reg 2025/1926 codified at 8507.90.31; thickness <40μm threshold met (commercial battery grade = 10-25μm)
**Stability**: stable
**Confidence**: high
**Classified as**: → [[hs_code-8507-90-31-eu]]

### India Classification

**Code**: 3921.19.90 (ITC-HS)
**GRI path**: GRI 1
**Basis**: ITC-HS material-first; cellular plastic film; no Indian binding regulation creating battery-part carve-out; follows same approach as US
**Stability**: stable
**Confidence**: medium (evolving regulatory landscape; monitor for CBIC circular)
**Classified as**: → [[hs_code-3921-19-in]]

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 3921.19.0000 | GRI 1; material-first cellular plastic; CBP HQ 967313 binding | stable | high |
| EU | 8507.90.31 | Commission Note C/2025/6096 binding; EU CN 2026; <40μm battery separator | stable | high |
| India | 3921.19.90 | GRI 1; material-first; ITC-HS cellular plastic (no Indian carve-out) | stable | medium |

## Jurisdiction Divergence Note

This is a **genuine, legally entrenched, Chapter-level divergence**:
- US/India classify by material composition → Chapter 39 (Plastics)
- EU classifies by function/end-use (with dimensional threshold) → Chapter 85 (Electrical equipment)

Both positions are supported by binding legal authority in their respective jurisdictions. The divergence cannot be resolved by GRI analysis — it reflects different policy choices embedded in national/supranational classification regulations.

**Regulatory impact**: Different tariff rates, different rules of origin calculations, different Section/Chapter add-on provisions apply depending on jurisdiction. Supply chain teams importing separator film into both EU and US/India must apply different HS codes.

**D-RULING handoff**: Required. D-RULING package must document both positions and flag for supply chain advisory.

## Corpus Gap Status

D2-GAP-004: **CLOSED** — Both binding authorities confirmed; jurisdictional divergence fully documented.

## Graph Links

- `classification_node` → [[product_component-separator-pe-pp-film]]
- `classified_as (US)` → [[hs_code-3921-19-us]]
- `classified_as (EU)` → [[hs_code-8507-90-31-eu]]
- `classified_as (IN)` → [[hs_code-3921-19-in]]
- `ruling_anchor (US)` → CBP HQ 967313
- `ruling_anchor (EU)` → EU Commission Note C/2025/6096
- `graph_index` → [[d-class-hs_gate1_graph_index]]
