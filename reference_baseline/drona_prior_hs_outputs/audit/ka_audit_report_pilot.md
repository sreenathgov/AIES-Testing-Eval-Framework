---
agent: KA
audit_id: KA-AUDIT-PILOT-TB4-TB1
batches: TB-4 + TB-1
components_audited: 6
jurisdictions_per_component: 3
total_classification_candidates: 18
audit_result: PASS WITH CORRECTIONS
corrections_applied: 4
invariant_violations: 0
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Audit Verdict: PASS

All four hard invariants satisfied. All quality checks pass. No violations across 18 classification candidates.

---

## Invariant Results

### I-1: All Section XVII Note 2(f) electrical candidates → Chapter 85

**PASS**

| Component | Note 2(f) Fired | Chapter | Heading | Result |
|-----------|----------------|---------|---------|--------|
| Li-Ion Battery Cell (ent_147) | Yes | 85 | 8507 | ✓ |
| Traction Motor (ent_221) | Yes | 85 | 8501 | ✓ |
| HV Contactor (ent_144) | Yes | 85 | 8536 | ✓ |
| BMS (ent_217) | Yes | 85 | 8537 | ✓ |
| DC-DC Converter (ent_216) | Yes | 85 | 8504 | ✓ |
| OBC (ent_215) | Yes | 85 | 8504 | ✓ |

---

### I-2: Raw precursors not in Chapter 85 or 87

**PASS — Not applicable to TB-4 / TB-1**

No raw precursor materials in these batches. All 6 components are finished manufactured goods. I-2 becomes active in TB-3 (raw precursors batch).

---

### I-3: Parts of general use → base material chapters only

**PASS**

Section XV Note 2 checked for all 6 components. None qualify as "parts of general use" — all are specialized EV components with no general application across industries. Note 2 correctly did not fire for any pilot component.

---

### I-4: All GRI 3(b) composite goods → essential_character_reasoning populated

**PASS**

No GRI 3(b) triggered for any pilot component. taxonomy_handoff flagged `gri_3_required: true` for ent_147 (Li-Ion Battery Cell) — AA analysis confirmed this does not apply to a standalone cell. The flag triggered the analysis; analysis resolved at GRI 1.

---

## Quality Checks

### Three jurisdictions per component
**PASS** — All 6 components have US + EU + India classifications. 18 total candidates.

### No cross-domain contamination
**PASS** — No `product_component`, `material`, `company`, `country`, `legal_instrument`, or `incentive_program` entities emitted by any agent. All outputs are classification artifacts only.

### Citation provenance
**PASS** — All 18 PTA records cite `source_doc` + `source_section`. All DA memos cite source. PRA records cite ruling ID + source. AA candidates cite source PTA files.

### Enum enforcement

| Enum | Values Used | Invalid |
|------|-------------|---------|
| `classification_stability` | stable (12), contested (3), fragile (3) | 0 |
| `confidence` | high (12), medium (6), low (0) | 0 |
| `gri_path` | GRI_1 (18) | 0 |

Stable: Li-Ion Battery Cell × 3, Traction Motor × 3, DC-DC Converter × 3, OBC × 3.
Contested: BMS × 3 (US, EU, India) — 8537.10 vs 8507 pressure from CBP H155376.
Fragile: HV Contactor × 3 — heading-level voltage uncertainty (8536 vs 8535); provisional classification pending voltage confirmation.
Medium confidence: HV Contactor × 3 (fragile), BMS × 3 (contested).

### Jurisdictional divergence handling
**PASS** — No collapsed jurisdictions. All 6 components produce 3 separate jurisdiction records. India subheading specificity (traction motor: 85015330) and EU CN specificity (8-digit where determinable) preserved without collapsing to a single answer.

> **Note**: BMS CONTESTED flag is not a jurisdictional divergence — all three jurisdictions assign 8537.10. The flag reflects the 8507 pressure point from trade practice.

### Required fields populated
**PASS** — `hs_code`, `jurisdiction`, `gri_path`, `classification_stability`, `confidence`, `source_doc`, `source_section` all populated for every record. No blank strings.

---

## Pilot Summary

| Validation | Status |
|------------|--------|
| GRI 1 cascade applied correctly | ✓ |
| Three pre-GRI filters checked for all components | ✓ |
| Citation provenance populated | ✓ |
| Jurisdictions not collapsed | ✓ |
| PRA ruling extraction correct (decision vs. party argument) | ✓ |
| AA four-condition override framework applied | ✓ |
| H155376 override correctly rejected for standalone BMS | ✓ |
| CESTAT BCM override correctly rejected (BCM ≠ BMS) | ✓ |
| KA invariants I-1 through I-4 pass | ✓ |
| No cross-domain contamination | ✓ |
| No non-canonical enum values | ✓ |

---

## Open Items

### Genuine unresolved classification dependencies

| Item | Impact |
|------|--------|
| HV Contactor (ent_144) — operating voltage unconfirmed | **Heading-level**: determines 8536 (≤1,000V) vs 8535 (>1,000V). Classification is provisional. Must be resolved before ent_144 can be marked verified. |

### Non-blocking corroboration tasks

| Item | Current conclusion | Task |
|------|--------------------|------|
| BMS (ent_217) — newer US authority on standalone battery control electronics | 8537.10 (stands) | Collect post-2011 CBP/CROSS rulings on standalone BMS PCBAs. Classification does not change unless newer primary authority materially conflicts. |

### Operational cleanup tasks

| Item | When |
|------|------|
| EU CN 8-digit for BMS, DC-DC, OBC | After power/voltage specs confirmed — heading stability unaffected |
| India CBIC Mistral pre-processing (duplicate headers) | Before TB-1 full run |
| Obsidian wikilinks across all staging files | After full 28-component run, before domain marked verified |

---

## Gate 1 Verdict: PASS WITH CORRECTIONS

Four corrections were required before this verdict could be issued:

| # | Issue | Correction Applied |
|---|-------|--------------------|
| 1 | Traction Motor US: 8501.32.55 listed as alternative to 8501.53 — these are mutually exclusive by power output | Removed 8501.32.55; 8501.53 is the sole correct subheading for >75 kW motors |
| 2 | Traction Motor: `ruling_override_applied: true` contradicted body text (BTI is corroboration, not override) | Corrected to `false` |
| 3 | HV Contactor: `stability: stable` contradicted heading-level voltage uncertainty (8536 vs 8535) | Corrected to `fragile`; classification marked provisional pending voltage confirmation |
| 4 | KA audit: stable count was 14 (should have been 15 pre-correction, 12 post-correction); total summed to 17 | Recomputed: stable 12, contested 3, fragile 3 = 18 ✓ |

No invariant violations. No cross-domain contamination. Methodology is sound — the errors were in metadata consistency and honest representation of uncertainty, not in the classification logic itself.

**Recommended next step**: TB-4 remaining (4 components) → TB-1 full run (5 remaining components) → TB-2 → TB-3.
