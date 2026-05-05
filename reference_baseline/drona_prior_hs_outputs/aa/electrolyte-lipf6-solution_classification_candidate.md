---
agent: AA
component: Electrolyte (LiPF6 Solution)
entity_id: ent_tb3_03
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
ruling_anchor_us: "CBP N327146 (LiPF6 electrolyte solution → 3824.99.93.97)"
ruling_anchor_eu: "EU CN Chapter 28 Note 1; EU Explanatory Notes 3824 (prepared chemical mixtures for specific industrial use)"
ruling_anchor_india: "ITC-HS Chapter 28 Note 1 (multi-component mixture ≠ single defined compound)"
---

## Reconciliation

### Source Inputs
- PTA (US): `electrolyte-lipf6-solution_us.md` — 3824.99.93.97, CBP N327146
- PTA (EU): `electrolyte-lipf6-solution_eu.md` — 3824.99 (8-digit pending)
- PTA (India): `electrolyte-lipf6-solution_india.md` — 3824.99.00
- DA: `da_memo_tb3_battery_materials.md` — no divergence; all three jurisdictions 3824.99

### Pre-GRI Exclusion Filter Result

All checks negative. LiPF6 electrolyte solution is a chemical preparation — no mechanical part, no electrical machinery, no measuring instrument. No veto fires.

### GRI Cascade

**GRI 1 applies**:

Chapter 28 Note 1 analysis (all jurisdictions): The electrolyte is LiPF6 dissolved in a multi-component organic solvent mixture (EC + DMC + EMC) with performance additives (VC, FEC). This is not a "separate chemically defined compound" — it is a mixture of multiple distinct chemical species. Chapter 28 Note 1 requires a single chemically defined compound. Multi-component mixture → **ejected from Chapter 28**.

(Note: Pure, dry LiPF6 salt alone would be 2826.90 — inorganic fluoride. But the commercial electrolyte is a solution, not a pure compound.)

Heading 3824: "Chemical products and preparations of the chemical or allied industries... not elsewhere specified or included." The LiPF6 electrolyte solution is a preparation formulated for specific use (Li-ion battery ionic conduction) → 3824.99 across all jurisdictions.

**CBP N327146** (binding): LiPF6 electrolyte solution → **3824.99.93.97** (HTSUS — chemical preparations for specific use, other).

### US Classification

**Code**: 3824.99.93.97 (US HTSUS, per CBP N327146)
**GRI path**: GRI 1
**Classified as**: → [[hs_code-3824-99-us]]

### EU Classification

**Code**: 3824.99 (EU CN — 8-digit subheading 3824.99.96 for mixed organic/inorganic preparations, other; pending verification against current EU tariff schedule)
**GRI path**: GRI 1
**Classified as**: → [[hs_code-3824-99-eu]]

### India Classification

**Code**: 3824.99.00 (ITC-HS)
**GRI path**: GRI 1
**Classified as**: → [[hs_code-3824-99-in]]

---

## Final Classification Table

| Jurisdiction | Code | Basis | Stability | Confidence |
|-------------|------|-------|-----------|------------|
| US | 3824.99.93.97 | GRI 1; Ch28 Note 1 eject (multi-component mixture); CBP N327146 binding | stable | high |
| EU | 3824.99 (3824.99.96 candidate) | GRI 1; Ch28 Note 1 eject; EU Explanatory Notes 3824 | stable | high |
| India | 3824.99.00 | GRI 1; Ch28 Note 1 eject; ITC-HS residual | stable | high |

## Note on Import Stream Distinction

Pure LiPF6 (dry salt) imported separately: US 2826.90.9000; EU 2826.90.80; India 2826.90.90. This is a different product entity from the electrolyte solution.

## Corpus Gap Status

D2-GAP-003: **CLOSED** — CBP N327146 binding; multi-component mixture analysis conclusive; all three jurisdictions resolved.

## Graph Links

- `classification_node` → [[product_component-electrolyte-lipf6-solution]]
- `classified_as (US)` → [[hs_code-3824-99-us]]
- `classified_as (EU)` → [[hs_code-3824-99-eu]]
- `classified_as (IN)` → [[hs_code-3824-99-in]]
- `ruling_anchor (US)` → CBP N327146
- `graph_index` → [[d-class-hs_gate1_graph_index]]
