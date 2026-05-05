# Sanitization Log

The forensic evidence bundle contains a small reviewer-safe sample of internal extraction artifacts and graph artifacts.

Sanitization actions:
- Internal product/company names are neutralized where present.
- Absolute local paths and email-like strings are removed.
- A reviewer banner is added to each sanitized text artifact.
- Files are included only to evidence artifact origin, graph shape, or known failure modes.

These artifacts are not external legal authority. Legal authority is represented only by `legal_authority_chain` entries pointing to EU/WCO/BTI source anchors.
