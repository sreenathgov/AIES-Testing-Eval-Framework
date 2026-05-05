---
agent: AA
component: Anode Substrate (Cu Foil)
entity_id: ent_tb3_06
batch: TB-3
jurisdiction_divergence: false
stability_us: stable
stability_eu: stable
stability_india: stable
confidence_us: high
confidence_eu: high
confidence_india: high
gri_path: GRI_1
i4_flag: false
section_xv_note_2_fired: true
date: "2026-04-06"
refinement_run: "2026-04-06"
ruling_anchor_us: "CBP N090878 (Cu foil of refined copper → 7410.11.0000)"
ruling_anchor_eu: "EU CN Chapter 74 Note (refined copper ≥99.85%); EU CN 7410.11.00"
ruling_anchor_india: "ITC-HS Section XV Note 2; ITC-HS 7410.11.10 (thickness ≤0.1mm)"
---

## Reconciliation

### Source Inputs
- PTA (US): `anode-substrate-cu-foil_us.md` — 7410.11.0000, CBP N090878
- PTA (EU): `anode-substrate-cu-foil_eu.md` — 7410.11.00, EU CN
- PTA (India): `anode-substrate-cu-foil_india.md` — 7410.11.10, ITC-HS thickness split
- DA: `da_memo_tb3_battery_materials.md` — no divergence; all three converge on heading 7410.11

### Pre-GRI Exclusion Filter

**Section XV Note 2 — FIRED**:
Copper foil is a base metal article of general use → Chapter 74 mandatory. Chapter 85 battery parts route is blocked.

### GRI Cascade

**Section XV Note 2 resolves classification**: bare Cu foil → Chapter 74.

**Purity threshold**: Chapter 74 Note 1 defines "refined copper" as ≥99.85% purity by weight. Battery-grade electrodeposited Cu foil is typically ≥99.97% → threshold met by a wide margin.

GRI 1: Heading 7410 — "Copper foil (whether or not backed): Not exceeding 0.15mm in thickness."
Subheading 7410.11: "Of refined copper."

Battery-grade Cu foil: 6-12μm thickness (<0.15mm), bare, not backed, refined copper → heading 7410.11 confirmed across all jurisdictions.

**8-digit variation**:
- US HTSUS: 7410.11.0000 (single subheading)
- EU CN: 7410.11.00 (single subheading — no further EU CN split)
- ITC-HS: splits at 0.1mm → 7410.11.10 (≤0.1mm); battery foil (6-12μm) → 7410.11.10

**CBP N090878**: Cu foil of refined copper (electrolytic, thickness ≤0.15mm, not backed) → **7410.11.0000**.

### US Classification

**Code**: 7410.11.0000 (US HTSUS, per CBP N090878)
**GRI path**: Section XV Note 2 → GRI 1
**Classified as**: → [[hs_code-7410-11-us]]

### EU Classification

**Code**: 7410.11.00 (EU CN)
**GRI path**: Section XV Note 2 → GRI 1 + GRI 6
**Classified as**: → [[hs_code-7410-11-eu]]

### India Classification

**Code**: 7410.11.10 (ITC-HS — Cu foil ≤0.1mm)
**GRI path**: Section XV Note 2 → GRI 1 + GRI 6
**Classified as**: → [[hs_code-7410-11-in]]

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 7410.11.0000 | Section XV Note 2 → Ch74; refined Cu (≥99.85%); 7410.11; CBP N090878 binding | stable | high |
| EU | 7410.11.00 | Section XV Note 2 → Ch74; refined Cu; EU CN 7410.11.00 | stable | high |
| India | 7410.11.10 | Section XV Note 2 → Ch74; refined Cu; ITC-HS <0.1mm split | stable | high |

## Corpus Gap Status

D2-GAP-006: **CLOSED** — Section XV Note 2 analysis complete; purity threshold confirmed; CBP N090878 basis; all three jurisdictions resolved.

## Graph Links

- `classification_node` → [[product_component-anode-substrate-cu-foil]]
- `classified_as (US)` → [[hs_code-7410-11-us]]
- `classified_as (EU)` → [[hs_code-7410-11-eu]]
- `classified_as (IN)` → [[hs_code-7410-11-in]]
- `ruling_anchor (US)` → CBP N090878
- `graph_index` → [[d-class-hs_gate1_graph_index]]
