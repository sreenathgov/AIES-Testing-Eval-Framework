# Forbidden Metrics And Guardrails

The v1 DRONA HS evaluation harness does not use generic model-quality metrics
as legal correctness gates. Legal auditability depends on authority,
provenance, source anchors, role boundaries, graph parity, uncertainty
preservation, and handoff safety.

## Forbidden Or Non-Dispositive Metrics

| Metric | Status | Rationale |
|---|---|---|
| Negative Log Likelihood | Forbidden | Token likelihood is not available or legally interpretable in LLM-as-service extraction. |
| Brier Score | Forbidden | Requires calibrated probabilistic forecasts; legal safety is not a probability score. |
| TF-IDF / Entropy | Forbidden | Term-frequency proxies cannot identify legal authority or binding force. |
| Document-Level Citation | Forbidden for material propositions | Too broad when finer source anchors are available. |
| BERTScore | Future diagnostic only | Semantic similarity is not legal correctness. |
| Expected Calibration Error | Deferred | Replaced in v1 by false-certainty and uncertainty-preservation controls. |
| nLog-Distance | Future diagnostic only | Useful later for numeric threshold domains, not core HS v1. |

## Source-Processing Boundary

Do not frame the boundary as a fixed token-count rule. The operational guardrail
is broader:

> Any truncation, chunk-boundary loss, context-window loss, or retrieval-window
> omission must be logged as a source-processing boundary.
