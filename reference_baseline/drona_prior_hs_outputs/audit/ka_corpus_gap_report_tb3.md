---
agent: KA
audit_id: KA-TB3-CORPUS-GAP
batch: TB-3
type: corpus_gap_report
components_audited: 7
date: 2026-04-02
validation_status: exploratory
result: CORPUS AUGMENTATION REQUIRED — ALL 7 COMPONENTS
---

## Purpose

TB-3 is an explicitly exploratory batch (per approved v3 plan). Standard KA audit invariants do not apply because these classifications are not validated. This report documents the corpus gaps that prevent validation and defines the augmentation requirement.

---

## Corpus Gaps by Chapter

| Chapter | Required For | Status |
|---------|-------------|--------|
| Ch 28 (inorganic chemicals) | Cathode Active Material (NMC) | NOT IN PARSED CORPUS |
| Ch 25 (mineral products) | Anode Active Material (natural graphite variant) | NOT IN PARSED CORPUS |
| Ch 38 (miscellaneous chemicals) | Anode Active Material (synthetic), Electrolyte | NOT IN PARSED CORPUS |
| Ch 39 (plastics) | Separator (PE/PP film) | NOT IN PARSED CORPUS |
| Ch 72 (iron and steel) | Electrical Steel Core (NOES) | NOT IN PARSED CORPUS |
| Ch 74 (copper) | Anode Substrate (Cu Foil) | NOT IN PARSED CORPUS |
| Ch 76 (aluminum) | Cathode Substrate (Al Foil) | NOT IN PARSED CORPUS |

**All 7 TB-3 components require chapter-level corpus augmentation before validation.**

---

## Component Status

| Component | Exploratory Code | Confidence | Primary Corpus Gap |
|-----------|-----------------|------------|-------------------|
| Cathode Active Material (NMC) | 2841.90 | low | Ch 28 (inorganic salts) |
| Anode Active Material (Graphite) | 3801.10 (synthetic) / 2504.10 (natural) | low | Ch 38 / Ch 25 |
| Electrolyte (LiPF6 Solution) | 3824.99 | low | Ch 38 |
| Separator (PE/PP Film) | 3920.20 (PP) / 3920.10 (PE) | low | Ch 39 |
| Cathode Substrate (Al Foil) | 7607.11 | low | Ch 76 |
| Anode Substrate (Cu Foil) | 7410.11 | low | Ch 74 |
| Silicon-Alloyed Electrical Steel Core (NOES) | 7225.19 (≥600mm) / 7226.19 (<600mm) | low | Ch 72 |

---

## Augmentation Plan

**Phase 1 — Priority corpus additions**:
1. USITC HTS Chapters 72, 74, 76 (metals — relatively straightforward material classifications)
2. USITC HTS Chapter 39 (plastics — separator films)
3. USITC HTS Chapter 28/38 (chemicals — most complex; NMC and electrolyte)

**Phase 2 — Validation**:
After corpus augmentation, TB-3 components must be re-run through the full PTA → DA → AA → KA chain with `validation_status: validated`.

**Phase 3 — EU CN + India ITC-HS supplementation**:
EU and India chapter-level documents for Ch 28/38/39/72/74/76 to confirm 8-digit subheadings.

---

## Exploratory Confidence Note

The exploratory codes assigned in TB-3 PTA files represent the best available secondary-source classification based on material identity and WCO-harmonized heading structure. They are internally consistent with the GRI analysis but are NOT validated against parsed source documents. Do not use TB-3 codes for trade or compliance purposes.

---

## Graph Index Instructions

TB-3 components and their exploratory HS code nodes are to be listed in a **separate section** of the graph index under `## Exploratory Batch (TB-3 — corpus augmentation required)`. They must not be counted in the `validated_component_count`.
