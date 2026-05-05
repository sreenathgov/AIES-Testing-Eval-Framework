# Disclosure Boundary

This repository is a bounded evaluation artifact for a legal extraction paper.
It is not the full production architecture, not a complete knowledge compiler,
and not a migration of any internal graph.

The repository has two paper-facing layers:

1. A pre-HS-run slice containing clean engineering inputs, source records, and
   DRONA-shaped agent specifications for the bounded EU/WCO/BTI run.
2. A deterministic evaluator that can test generated artifacts for external
   authority, source anchors, uncertainty, graph parity, and safe handoff
   behavior.

The repository excludes:

- internal doctrine documents,
- company strategy documents,
- full memory or orchestration state,
- full staging folders,
- full graph exports,
- downstream product routing logic,
- unrelated live model prompts outside the D-CLASS-HS slice,
- API-backed live LLM execution by default.

Internal extraction artifacts may appear only as sanitized `artifact_origin`
references. They cannot satisfy the `legal_authority_chain` for a legal
proposition.

Prior DRONA D-CLASS-HS outputs are sealed under `reference_baseline/` and are
comparison-only. Runtime inputs must never point into that folder.
