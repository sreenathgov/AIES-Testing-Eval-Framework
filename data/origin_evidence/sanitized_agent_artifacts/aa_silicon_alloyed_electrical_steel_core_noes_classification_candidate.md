<!-- Reviewer-safe sanitized forensic artifact. This file evidences artifact origin only and is not external legal authority. -->

---
agent: AA
component: Silicon-Alloyed Electrical Steel Core (NOES)
entity_id: ent_tb3_07
batch: TB-3
jurisdiction_divergence: false
stability_us: stable
stability_eu: stable
stability_india: stable
confidence_us: medium
confidence_eu: medium
confidence_india: medium
gri_path: GRI_1
i4_flag: false
section_xv_note_2_fired: true
width_data_pending: true
width_data_note: "Classification is width-as-imported dependent (600mm threshold). Default: slit coil <600mm → 7226.19. Supply chain team must confirm width."
client_fact_pending: true
client_fact_key: "coil_width_mm"
client_fact_note: "Client or supply-chain documentation must confirm width as imported. If width <600mm use 7226.19; if width >=600mm use 7225.19."
legal_rule_resolved: true
date: "2026-04-06"
refinement_run: "2026-04-06"
ruling_anchor_us: "HTSUS Chapter 72 width split: 7225 (≥600mm) vs 7226 (<600mm)"
ruling_anchor_eu: "EU CN Chapter 72 identical width split; EU CN 7226.19.10 (thickness <0.5mm)"
ruling_anchor_india: "ITC-HS Section XV Note 2; ITC-HS 7226.19.00"
---

## Reconciliation

### Source Inputs
- PTA (US): `silicon-alloyed-electrical-steel-core-noes_us.md` — 7226.19.1000 (default slit coil), 7225.19.0000 (alt master coil)
- PTA (EU): `silicon-alloyed-electrical-steel-core-noes_eu.md` — 7226.19.10 (default), 7225.19.90 (alt)
- PTA (India): `silicon-alloyed-electrical-steel-core-noes_india.md` — 7226.19.00 (default), 7225.19.00 (alt)
- DA: `da_memo_tb3_battery_materials.md` — no legal divergence; width-based technical determination; motor lamination slit coil default <600mm

### Pre-GRI Exclusion Filter

**Section XV Note 2 — FIRED**:
Silicon-alloyed electrical steel (NOES) is a base metal material of general use (used in motors, generators, transformers across multiple industries) → Chapter 72 mandatory. Chapter 85 (electrical machinery) is not the correct chapter for the raw steel material.

### GRI Cascade

**Section XV Note 2 resolves**: NOES → Chapter 72.

**Classification is determined by physical specification (width), not legal ambiguity**:

Chapter 72 width-split is WCO-standard and identical across US, EU, India:
- Width ≥600mm → Heading 7225 (silicon-electrical steel, non-grain-oriented → 7225.19)
- Width <600mm → Heading 7226 (silicon-electrical steel, non-grain-oriented → 7226.19)

**Motor lamination supply chain width analysis**:
EV traction motor stator laminations require punched stampings from slit coil. The slit coil width is determined by the stator outer diameter. Common EV traction motor OD range: 150-350mm → slit coil width: ~200-450mm, i.e., **<600mm** in virtually all motor lamination applications.

Master coil from the steel mill (typically 1000-1500mm wide) is slit to narrow coils before delivery to lamination stamping facilities. If the firm imports slit coil → **7226.19** (width <600mm). If the firm imports master coil and slits in-house → **7225.19** (width ≥600mm as imported).

**Default position**: Motor lamination slit coil → 7226.19.

**Additional EU CN thickness split** (applies within 7226.19):
- 7226.19.10: thickness <0.5mm (motor NOES at 0.27-0.35mm → 7226.19.10)
- 7226.19.80: thickness ≥0.5mm

### US Classification

**Code**: 7226.19.1000 (US HTSUS — primary/default; slit coil <600mm)
**Alt Code**: 7225.19.0000 (if master coil ≥600mm imported)
**GRI path**: Section XV Note 2 → GRI 1
**Confidence**: medium (width confirmation required)
**Classified as**: → [[hs_code-7226-19-us]]

### EU Classification

**Code**: 7226.19.10 (EU CN — primary/default; width <600mm, thickness <0.5mm for motor-grade NOES)
**Alt Code**: 7225.19.90 (if master coil ≥600mm imported)
**GRI path**: Section XV Note 2 → GRI 1 + GRI 6
**Confidence**: medium (width + thickness confirmation required)
**Classified as**: → [[hs_code-7226-19-eu]]

### India Classification

**Code**: 7226.19.00 (ITC-HS — primary/default; slit coil <600mm)
**Alt Code**: 7225.19.00 (if master coil ≥600mm imported)
**GRI path**: Section XV Note 2 → GRI 1 + GRI 6
**Confidence**: medium (width confirmation required)
**Classified as**: → [[hs_code-7226-19-in]]

---

## Final Classification Table

| Jurisdiction | Code (default) | Alt Code (master coil) | Basis | Stability | Confidence |
|-------------|---------------|----------------------|-------|-----------|------------|
| US | 7226.19.1000 | 7225.19.0000 | Sec XV Note 2; Ch72 width split; slit coil <600mm default | stable | medium |
| EU | 7226.19.10 | 7225.19.90 | Sec XV Note 2; Ch72 width split; EU CN 0.5mm thickness split | stable | medium |
| India | 7226.19.00 | 7225.19.00 | Sec XV Note 2; Ch72 width split; ITC-HS single subheading | stable | medium |

## Width Data Note

This is a **technical specification gap**, not a legal ambiguity. The correct heading depends entirely on the width of the NOES as imported. For the firm's specific supply chain:
- Obtain slit coil width specification from procurement/materials specification sheet
- If width <600mm → 7226.19 (primary position)
- If width ≥600mm → 7225.19

No India-specific ruling or CBIC circular on NOES classification identified. The 600mm width split is universally applied.

## Corpus Gap Status

D2-GAP-007: **CLOSED (conditional)** — Chapter 72 width-split analysis complete; Section XV Note 2 confirmed for all jurisdictions; legal framework fully resolved. Residual data gap is technical (width specification), not legal. Default position 7226.19 established for motor lamination supply chain.

## Graph Links

- `classification_node` → [[product_component-silicon-alloyed-electrical-steel-core-noes]]
- `classified_as (US)` → [[hs_code-7226-19-us]]
- `classified_as (EU)` → [[hs_code-7226-19-eu]]
- `classified_as (IN)` → [[hs_code-7226-19-in]]
- `graph_index` → [[hs-slice_gate1_graph_index]]
