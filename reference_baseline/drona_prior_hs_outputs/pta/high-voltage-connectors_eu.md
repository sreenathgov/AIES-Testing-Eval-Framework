---
agent: PTA
component: High-Voltage Connectors
entity_id: ent_182
jurisdiction: EU
fundamental_function: STRUCTURAL
is_composite_flagged: false
hs_code_candidate: "8536.69"
eu_cn_subheading: "8536.69.90"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: eu_hs_commission_implementing_regulation_(eu)_2025_1926_evs.md
source_section: CN heading 8536 — Electrical apparatus for making connections; subheading 8536.69 — Other (not lamp-holders); subheading 8536.69.90 — Other
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical connectors are Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not parts of general use under Section XV Note 2 |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## Important: D-CLASS-ENG Functional Function ≠ HS Classification

Same note as US jurisdiction. `fundamental_function: STRUCTURAL` reflects engineering taxonomy role, not HS classification basis. Heading 8536 explicitly names connectors. Classification is at 8536.69.

## GRI Analysis

**Resolved at GRI 1.** EU CN heading 8536 covers electrical apparatus for making connections, for a voltage not exceeding 1,000V. Heading text explicitly includes plugs, sockets, and other connectors.

Within 8536.69 (Other plugs and sockets):
- 8536.69.10: For coaxial cables — NO
- 8536.69.30: For printed circuits — NO
- **8536.69.90: Other** — EV HV connectors are specialized multi-pin locking connectors, not coaxial and not PCB → 8536.69.90

## Classification

- **Code**: 8536.69.90
- **Subheading text**: Other (plugs and sockets)
- **Heading text**: Electrical apparatus for switching or protecting electrical circuits, or for making connections to or in electrical circuits... for a voltage not exceeding 1,000 V
