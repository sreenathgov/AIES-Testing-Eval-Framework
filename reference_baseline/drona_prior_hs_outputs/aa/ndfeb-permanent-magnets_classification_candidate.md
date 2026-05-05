---
agent: AA
component: NdFeB Permanent Magnets
entity_id: ent_207
batch: TB-1
jurisdictions: [US, EU, India]
hs_code_us: "8505.11.00"
hs_code_eu: "8505.11.90"
hs_code_india: "8505.11.90"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: none
source_pta_files:
  - pta/ndfeb-permanent-magnets_us.md
  - pta/ndfeb-permanent-magnets_eu.md
  - pta/ndfeb-permanent-magnets_india.md
source_da_file: da/da_memo_tb1_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

NdFeB Permanent Magnets classify at heading 8505.11 (permanent magnets of metal) across all three jurisdictions. This is the one TB-1 component that comes from the TB-3 precursor group but was promoted to TB-1 because heading 8505 is in Chapter 85 and is within the parsed corpus.

- **US**: 8505.11.00 — permanent magnets of metal (US does not subdivide 8505.11 between ferrite and other)
- **EU**: 8505.11.90 — other permanent magnets of metal (NdFeB is not ferrite)
- **India**: 8505.11.90 — other permanent magnets of metal (NdFeB is not ferrite)

The US code (8505.11.00) differs from EU/India (8505.11.90) because US HTS uses a single statistical code at 8505.11.00 without the ferrite/non-ferrite subdivision that EU CN and India ITC-HS apply. This is a structural tariff nomenclature difference, not a classification disagreement. All three jurisdictions agree that NdFeB is a "permanent magnet of metal." `jurisdiction_divergence: false`.

Stability is **stable**.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | No | NdFeB magnets are passive metallic articles; heading 8505 is already in Chapter 85; no Chapter 87 conflict. Note 2(f) is not required to route these items — they are captured directly by heading 8505.11. |
| Section XV Note 2 | No | Not applicable |
| Note 1 to Chapter 73 | **Considered** | Note 1 to Chapter 73 excludes articles of Section XVI. Heading 8505 is in Section XVI (Chapter 85). Iron-alloy components in NdFeB magnets are therefore excluded from Chapter 73. Heading 8505.11 governs. |
| Chapter 90 Note 2 | No | Passive magnetic article; not a measuring instrument |

---

## GRI Cascade

**Resolved at GRI 1.** Heading 8505 specifically covers "permanent magnets and articles designed to become permanent magnets after magnetisation." Subheading 8505.11 narrows to "of metal." NdFeB is a metallic alloy permanent magnet. GRI 1 is completely determinative.

**Competing headings considered**:
- Chapter 73/74/76 (metallic articles): Note 1 to those chapters excludes articles of Section XVI. Heading 8505 captures metallic permanent magnets regardless of the base metal in the alloy.
- Heading 8501 (electric motors/generators): NdFeB magnets traded as discrete components are NOT motors. When embedded in a completed rotor assembly and imported as part of a motor, they would be classified under the motor heading. But discrete magnet components trade as 8505.11 — Section XVI Note 2(b) applies: goods included in 8505 are classified there, not as parts of 8501.
- Heading 2805 (alkali metals, rare earths): This heading covers the chemical elements in their raw form, not manufactured articles. A sintered NdFeB magnet is a manufactured article, not a chemical element.

---

## Reconciliation: PTA vs DA

PTA: 8505.11.00 (US), 8505.11.90 (EU/India). DA-003-F3 ([[da_memo_tb1_remaining]]): Confirms 8505.11 across all jurisdictions; confirms EU/India 8505.11.90 for NdFeB (non-ferrite). Notes trade context: NdFeB magnets are a focal point of IRA FEOC rules (US) and Critical Raw Materials Act (EU). Classification is well-settled.

No conflict. Ruling override not triggered.

## Graph Links

- `classification_node` → [[product_component-ndfeb-permanent-magnets]]
- `engineering_anchor` → [[ndfeb-permanent-magnets]]
- `parent_component` → [[rotor-assembly]]
- `global_anchor` → [[hs_code-8505-11-global]]
- `classified_as` → [[hs_code-8505-11-us]]
- `classified_as` → [[hs_code-8505-11-eu]]
- `classified_as` → [[hs_code-8505-11-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
