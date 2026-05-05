---
agent: AA
component: Cathode Substrate (Al Foil)
entity_id: ent_tb3_05
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
ruling_anchor_us: "CBP NY N303974 (bare Al foil → 7607.11); HTSUS Chapter 76 (foil ≤0.2mm)"
ruling_anchor_eu: "EU CN Chapter 76; Section XV Note 2; EU CN 7607.11.10 (<0.021mm)"
ruling_anchor_india: "ITC-HS Section XV Note 2; ITC-HS 7607.11.10 (≤0.1mm)"
---

## Reconciliation

### Source Inputs
- PTA (US): `cathode-substrate-al-foil_us.md` — 7607.11.6000, CBP NY N303974
- PTA (EU): `cathode-substrate-al-foil_eu.md` — 7607.11.10, EU CN 8-digit thickness split
- PTA (India): `cathode-substrate-al-foil_india.md` — 7607.11.10, ITC-HS thickness split
- DA: `da_memo_tb3_battery_materials.md` — no divergence; all three converge on heading 7607.11

### Pre-GRI Exclusion Filter

**Section XV Note 2 — FIRED**:
Aluminum foil is a material/article of general use (food packaging, industrial, pharmaceutical, electrical) → Chapter 76 mandatory. Chapter 85 battery parts route is blocked for bare Al foil imported as standalone material.

Sections XVII Note 2(f) and Chapter 90 Note 2: not applicable.

### GRI Cascade

**Section XV Note 2 resolves classification before GRI cascade**: bare Al foil → Chapter 76.

GRI 1: Heading 7607 — "Aluminium foil... of a thickness (excluding any backing) not exceeding 0.2mm."
Subheading 7607.11: "Not backed: Rolled but not further worked."

Battery-grade cathode Al foil: 10-20μm thickness (<0.2mm), bare, not backed, rolled → heading 7607.11 confirmed across all jurisdictions.

**8-digit subheading variation by jurisdiction**:
- US HTSUS: splits at 0.01mm → 7607.11.6000 (≥0.01mm; 10-20μm qualifies)
- EU CN: splits at 0.021mm → 7607.11.10 (<0.021mm; 10-20μm < 0.021mm qualifies)
- ITC-HS: splits at 0.1mm → 7607.11.10 (≤0.1mm; 10-20μm qualifies)

All three resolve to the respective <-threshold 8-digit subheading.

**CBP NY N303974 qualifier**: Bare foil → 7607.11. Coated (with electrode active material) → 8507.90. Battery-grade cathode Al foil is imported as bare roll (coating applied in-house during cell manufacturing).

### US Classification

**Code**: 7607.11.6000 (US HTSUS)
**GRI path**: Section XV Note 2 → GRI 1
**Basis**: Section XV Note 2 (general use → Ch76); heading 7607.11 (bare, rolled, ≤0.2mm); CBP NY N303974
**Classified as**: → [[hs_code-7607-11-us]]

### EU Classification

**Code**: 7607.11.10 (EU CN — Al foil <0.021mm, not backed, rolled)
**GRI path**: Section XV Note 2 → GRI 1 + GRI 6
**Basis**: Section XV Note 2; heading 7607.11; EU CN 8-digit split at 0.021mm; battery foil (10-20μm) < 0.021mm → 7607.11.10
**Classified as**: → [[hs_code-7607-11-eu]]

### India Classification

**Code**: 7607.11.10 (ITC-HS — Al foil ≤0.1mm, not backed, rolled)
**GRI path**: Section XV Note 2 → GRI 1 + GRI 6
**Basis**: ITC-HS Section XV Note 2; heading 7607.11; ITC-HS split at 0.1mm; battery foil (10-20μm) → 7607.11.10
**Classified as**: → [[hs_code-7607-11-in]]

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 7607.11.6000 | Section XV Note 2 → Ch76; 7607.11 (bare, ≤0.2mm); CBP NY N303974 | stable | high |
| EU | 7607.11.10 | Section XV Note 2 → Ch76; 7607.11; EU CN <0.021mm split | stable | high |
| India | 7607.11.10 | Section XV Note 2 → Ch76; 7607.11; ITC-HS ≤0.1mm split | stable | high |

## Corpus Gap Status

D2-GAP-005: **CLOSED** — Section XV Note 2 analysis complete; Chapter 76 routing confirmed; CBP NY N303974 basis; all three jurisdictions resolved.

## Graph Links

- `classification_node` → [[product_component-cathode-substrate-al-foil]]
- `classified_as (US)` → [[hs_code-7607-11-us]]
- `classified_as (EU)` → [[hs_code-7607-11-eu]]
- `classified_as (IN)` → [[hs_code-7607-11-in]]
- `ruling_anchor (US)` → CBP NY N303974
- `graph_index` → [[d-class-hs_gate1_graph_index]]
