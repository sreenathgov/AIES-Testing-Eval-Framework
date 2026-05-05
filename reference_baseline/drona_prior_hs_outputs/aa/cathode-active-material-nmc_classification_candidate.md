---
agent: AA
component: Cathode Active Material (NMC)
entity_id: ent_tb3_01
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
ruling_anchor_us: "CBP N323297 (doped LiNiMnCoO₂ → 3824.99.3900)"
ruling_anchor_eu: "EU CN 2026 Reg 2025/1926 (2841.90.40 for pure NMC — confirms a contrario doped NMC → 3824.99)"
ruling_anchor_india: "ITC-HS Chapter 28 Note 1 (specific-use additions eject doped NMC from Ch28)"
---

## Reconciliation

### Source Inputs
- PTA (US): `cathode-active-material-nmc_us.md` — 3824.99.3900, GRI 1, Ch28 Note 1 eject
- PTA (EU): `cathode-active-material-nmc_eu.md` — 3824.99, GRI 1, EU CN 2026 a contrario basis
- PTA (India): `cathode-active-material-nmc_india.md` — 3824.99.00, GRI 1, material-first
- DA: `da_memo_tb3_battery_materials.md` — no divergence; CBP N323297 binding; EU CN 2026 Reg 2025/1926 reinforcing
- Ruling precedent: CBP N323297 binding for US jurisdiction

### Pre-GRI Exclusion Filter Result

All three checks negative. The component is a chemical preparation — not a mechanical part, not electrical machinery, not a measuring instrument. No veto fires.

### GRI Cascade

**GRI 1 applies (heading text alone)**:

Chapter 28, Note 1 analysis (all jurisdictions): Doped NMC (EV-grade) contains Zr/Ti/Al dopants and boron/tungsten coatings that are electrochemical performance modifiers, not preservation stabilisers. These additions render the material "particularly suitable for specific use" (lithium-ion battery cathodes) → Chapter 28 Note 1 boundary violated → **ejected from Chapter 28**.

Heading 3824: "Chemical products and preparations of the chemical or allied industries... not elsewhere specified or included" — the residual for engineered inorganic chemical preparations. GRI 1 routes to 3824.99 (Other: Other) across all three jurisdictions.

**No GRI 3 required** — single heading applies after Chapter 28 ejection.

### US Classification

**Code**: 3824.99.3900 (US HTSUS)
**GRI path**: GRI 1
**Basis**: Chapter 28 Note 1 eject (dopants = specific-use modifiers, not stabilisers); GRI 1 → heading 3824; CBP N323297 binding (doped/Zr-coated/boron-coated LiNiMnCoO₂ → 3824.99.3900)
**Classified as**: → [[hs_code-3824-99-us]]

### EU Classification

**Code**: 3824.99 (EU CN — 8-digit subheading: 3824.99.92 or 3824.99.96, to be confirmed against current EU tariff schedule)
**GRI path**: GRI 1
**Basis**: EU CN Chapter 28 Note 1 identical eject logic; EU CN 2026 Reg 2025/1926 created 2841.90.40 specifically for pure stoichiometric NMC, confirming a contrario that doped/coated NMC does not classify under 2841.90 → routes to 3824.99
**Classified as**: → [[hs_code-3824-99-eu]]

### India Classification

**Code**: 3824.99.00 (ITC-HS)
**GRI path**: GRI 1
**Basis**: ITC-HS Chapter 28 Note 1 identical eject logic; India material-first principle; 3824.99.00 residual chemical preparation subheading
**Classified as**: → [[hs_code-3824-99-in]]

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 3824.99.3900 | GRI 1; Ch28 Note 1 eject; CBP N323297 binding | stable | high |
| EU | 3824.99 (3824.99.92/96 pending 8-digit) | GRI 1; Ch28 Note 1 eject; EU CN 2026 a contrario basis | stable | high |
| India | 3824.99.00 | GRI 1; Ch28 Note 1 eject; material-first residual | stable | high |

## Conditional Classification Note

- IF NMC = pure stoichiometric, undoped, uncoated → US: 2826.90 not applicable (oxide, not fluoride); correct: 2841.90 (oxometallate salts); EU: 2841.90.40 (Reg 2025/1926); India: 2841.90.90
- IF NMC = doped OR surface-coated (EV-grade standard) → 3824.99 all jurisdictions
- **EV-grade NMC default**: 3824.99 (US: .3900; EU: .92/.96; India: .00)

## Corpus Gap Status

D2-GAP-001: **CLOSED** — CBP N323297 ruling confirmed; EU CN 2026 corroborating; Chapter 28 Note 1 analysis complete for all three jurisdictions.

## Graph Links

- `classification_node` → [[product_component-cathode-active-material-nmc]]
- `classified_as (US)` → [[hs_code-3824-99-us]]
- `classified_as (EU)` → [[hs_code-3824-99-eu]]
- `classified_as (IN)` → [[hs_code-3824-99-in]]
- `ruling_anchor (US)` → CBP N323297
- `graph_index` → [[d-class-hs_gate1_graph_index]]
