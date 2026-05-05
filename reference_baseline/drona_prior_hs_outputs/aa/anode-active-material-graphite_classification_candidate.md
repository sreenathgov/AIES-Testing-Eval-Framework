---
agent: AA
component: Anode Active Material (Graphite)
entity_id: ent_tb3_02
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
date: "2026-04-06"
refinement_run: "2026-04-06"
ruling_anchor_us: "CBP N325161 (surface-modified spherical graphite → 3801.10, not 2504.10)"
ruling_anchor_eu: "EU CN 2026 Reg 2025/1926 (3801.10.10 for battery electrode artificial graphite)"
ruling_anchor_india: "ITC-HS Chapter 25 Note 1 (surface modification exceeds crude mineral boundary)"
---

## Reconciliation

### Source Inputs
- PTA (US): `anode-active-material-graphite_us.md` — 3801.10.0000, CBP N325161
- PTA (EU): `anode-active-material-graphite_eu.md` — 3801.10.10, EU CN 2026 Reg 2025/1926
- PTA (India): `anode-active-material-graphite_india.md` — 3801.10.00, Chapter 25 Note 1 eject
- DA: `da_memo_tb3_battery_materials.md` — no heading-level divergence; EU has battery-specific 8-digit code

### Pre-GRI Exclusion Filter Result

All checks negative. Graphite is a raw material — not electrical machinery, not a measuring instrument, not a mechanical part. No veto fires.

### GRI Cascade

**GRI 1 applies**:

Chapter 25 Note 1 analysis: natural graphite in crude state or merely washed/crushed/ground qualifies under 2504.10. However, battery-grade graphite is either:
(a) Synthetic (Acheson process — petroleum coke heated to ≥2500°C) — not a natural mineral at all → 3801.10 by definition
(b) Surface-modified spherical natural graphite — spheroidized, purified to >99.95% C, carbon-coated → exceeds Chapter 25 Note 1 boundary

CBP N325161: surface-modified spherical graphite → 3801.10 (not 2504.10). Chapter 38, Heading 3801: "Artificial graphite."

**Both synthetic and surface-modified battery-grade graphite → Heading 3801.10** across all jurisdictions.

EU subheading split: EU CN 2026 created 3801.10.10 for battery electrode artificial graphite (vs 3801.10.90 other). US and India have single subheadings.

### US Classification

**Code**: 3801.10.0000 (US HTSUS)
**GRI path**: GRI 1
**Basis**: Chapter 25 Note 1 eject (surface modification beyond crude mineral boundary); GRI 1 → heading 3801; CBP N325161 binding (surface-modified spherical graphite → 3801.10)
**Classified as**: → [[hs_code-3801-10-us]]

### EU Classification

**Code**: 3801.10.10 (EU CN 2026, Reg 2025/1926 — battery electrode artificial graphite)
**GRI path**: GRI 1 + GRI 6
**Basis**: Chapter 25 Note 1 eject; GRI 1 → heading 3801; EU CN 2026 Reg 2025/1926 specific subheading for Li-ion battery electrode graphite
**Classified as**: → [[hs_code-3801-10-eu]]

### India Classification

**Code**: 3801.10.00 (ITC-HS)
**GRI path**: GRI 1
**Basis**: Chapter 25 Note 1 eject; ITC-HS 3801.10.00 for artificial graphite (no battery-specific subheading)
**Classified as**: → [[hs_code-3801-10-in]]

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 3801.10.0000 | GRI 1; Ch25 Note 1 eject; CBP N325161 binding | stable | high |
| EU | 3801.10.10 | GRI 1+6; Ch25 Note 1 eject; EU CN 2026 Reg 2025/1926 battery-electrode specific code | stable | high |
| India | 3801.10.00 | GRI 1; Ch25 Note 1 eject; ITC-HS artificial graphite residual | stable | high |

## Conditional Classification Note

- IF graphite = pure natural flake, unprocessed → US: 2504.10.1000; EU: 2504.10; India: 2504.10.00 (natural graphite)
- IF graphite = synthetic (Acheson) OR surface-modified spherical (battery-grade) → 3801.10 all jurisdictions
- **Battery-grade anode graphite default**: 3801.10

## Corpus Gap Status

D2-GAP-002: **CLOSED** — CBP N325161 ruling confirmed; EU CN 2026 corroborating with specific subheading; Chapter 25 Note 1 analysis complete for all three jurisdictions.

## Graph Links

- `classification_node` → [[product_component-anode-active-material-graphite]]
- `classified_as (US)` → [[hs_code-3801-10-us]]
- `classified_as (EU)` → [[hs_code-3801-10-eu]]
- `classified_as (IN)` → [[hs_code-3801-10-in]]
- `ruling_anchor (US)` → CBP N325161
- `graph_index` → [[d-class-hs_gate1_graph_index]]
