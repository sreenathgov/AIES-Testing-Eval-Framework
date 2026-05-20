from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

from .pre_hs_slice import assert_pre_hs_purity, audit_runtime_paths, load_selected_components
from .source_authority_registry import (
    SOURCE_AUTHORITIES,
    canonical_authority_class,
    concrete_source_ids,
    registry_mismatches_for_record_manifest_entry,
    registry_mismatches_for_source,
)


DEFAULT_UPSTREAM_RELATIVE = Path("..") / "source-repo"

GRAPH_NODE_TYPES = {
    "product_component",
    "engineering_identity_record",
    "classification_candidate",
    "statutory_classification_record",
    "ruling_record",
    "audit_report",
    "handoff_package",
    "hs_code",
    "source",
    "legal_proposition",
    "artifact_origin",
    "comparison_metadata",
}

GRAPH_EDGE_TYPES = {
    "artifact_origin",
    "describes",
    "proposes_code",
    "classified_as",
    "supported_by",
    "contains",
    "evaluates",
    "routes",
    "comparison_only",
}


@dataclass(frozen=True)
class ReadinessIssue:
    severity: str
    code: str
    message: str
    path: str | None = None


@dataclass(frozen=True)
class ReadinessReport:
    status: str
    blocker_count: int
    warning_count: int
    info_count: int
    issues: tuple[ReadinessIssue, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "blocker_count": self.blocker_count,
            "warning_count": self.warning_count,
            "info_count": self.info_count,
            "issues": [asdict(issue) for issue in self.issues],
        }


def run_readiness_check(repo_root: Path, upstream_root: Path | None = None, *, run_id: str = "paper_frozen_run") -> ReadinessReport:
    repo_root = repo_root.resolve()
    issues: list[ReadinessIssue] = []

    if upstream_root is not None:
        _check_upstream_contract(upstream_root.resolve(), issues)
    else:
        issues.append(_issue("info", "upstream_source_repo_not_checked", "No upstream source repository was supplied; checked-in bounded source bundle was validated instead."))
    _check_engineering_handoff(repo_root, issues)
    _check_source_bundle(repo_root, issues)
    _check_source_authority_consistency(repo_root, issues)
    _check_runtime_isolation(repo_root, run_id, issues)
    _check_run_graph_schema(repo_root, run_id, issues)
    _check_knowledge_evidence_registry(repo_root, issues)

    blockers = sum(1 for issue in issues if issue.severity == "blocker")
    warnings = sum(1 for issue in issues if issue.severity == "warning")
    infos = sum(1 for issue in issues if issue.severity == "info")
    return ReadinessReport(
        status="ready" if blockers == 0 else "blocked",
        blocker_count=blockers,
        warning_count=warnings,
        info_count=infos,
        issues=tuple(issues),
    )


def _infer_upstream_root(repo_root: Path) -> Path:
    sibling = (repo_root / DEFAULT_UPSTREAM_RELATIVE).resolve()
    return sibling


def _check_upstream_contract(upstream_root: Path, issues: list[ReadinessIssue]) -> None:
    required_dirs = [
        upstream_root / "source_repo" / "staging" / "hs-slice" / "_prompts",
        upstream_root / "source_repo" / "staging" / "hs-slice" / "_schemas",
        upstream_root / "source_repo" / "staging" / "hs-slice" / "pta",
        upstream_root / "source_repo" / "staging" / "hs-slice" / "pra",
        upstream_root / "source_repo" / "staging" / "hs-slice" / "aa",
        upstream_root / "source_repo" / "staging" / "hs-slice" / "audit",
        upstream_root / "source_repo" / "corpus" / "02_hs_classification",
        upstream_root / "source_repo" / "knowledge" / "verified",
    ]
    for path in required_dirs:
        if not path.exists():
            issues.append(_issue("blocker", "upstream_hs_path_missing", "Required upstream source extraction system HS path is missing.", path))

    prompt_dir = upstream_root / "source_repo" / "staging" / "hs-slice" / "_prompts"
    schema_dir = upstream_root / "source_repo" / "staging" / "hs-slice" / "_schemas"
    for prompt in ("pta-prompt.md", "pra-prompt.md", "da-prompt.md", "aa-prompt.md", "ka-prompt.md"):
        if not (prompt_dir / prompt).exists():
            issues.append(_issue("blocker", "upstream_prompt_missing", "Required upstream HS prompt is missing.", prompt_dir / prompt))
    for schema in (
        "StatutoryClassificationRecord.json",
        "RulingRecord.json",
        "ClassificationCandidate.json",
        "AuditReport.json",
        "RulingHandoffPackage.json",
    ):
        if not (schema_dir / schema).exists():
            issues.append(_issue("blocker", "upstream_schema_missing", "Required upstream HS schema is missing.", schema_dir / schema))


def _check_engineering_handoff(repo_root: Path, issues: list[ReadinessIssue]) -> None:
    try:
        components = load_selected_components(repo_root)
    except Exception as exc:
        issues.append(_issue("blocker", "engineering_handoff_unreadable", f"Selected component handoff cannot be read: {exc}", repo_root / "data" / "engineering_handoff"))
        return
    if len(components) != 28:
        issues.append(_issue("blocker", "engineering_handoff_component_count_invalid", f"Expected 28 selected components, found {len(components)}.", repo_root / "data" / "engineering_handoff" / "selected_28_components.json"))
    for component in components:
        failures = assert_pre_hs_purity(component)
        if failures:
            issues.append(_issue("blocker", "engineering_handoff_not_pre_hs_clean", f"{component.get('component_slug')} contains forbidden pre-HS fields: {', '.join(failures)}.", repo_root / "data" / "engineering_handoff" / "selected_28_components.json"))


def _check_source_bundle(repo_root: Path, issues: list[ReadinessIssue]) -> None:
    required = [
        repo_root / "data" / "source_corpus" / "SOURCE_ASSET_MANIFEST.json",
        repo_root / "data" / "source_corpus" / "SOURCE_RECORD_PROFILE_MANIFEST.json",
        repo_root / "data" / "source_corpus" / "source_record_manifest.json",
    ]
    for path in required:
        if not path.exists():
            issues.append(_issue("blocker", "source_manifest_missing", "Required source-corpus manifest is missing.", path))
            return

    profile_manifest = _read_json(repo_root / "data" / "source_corpus" / "SOURCE_RECORD_PROFILE_MANIFEST.json")
    for profile in profile_manifest.get("profiles", []):
        for key in ("original_path", "parsed_json_path", "normalized_json_path"):
            path = repo_root / profile.get(key, "")
            if not path.exists():
                issues.append(_issue("blocker", "source_profile_input_missing", f"Source profile input is missing: {key}.", path))
    for output in profile_manifest.get("compiled_outputs", []):
        for key in ("records_path", "records_markdown_path", "qc_path", "layout_profile_path"):
            path = repo_root / output[key]
            if not path.exists():
                issues.append(_issue("blocker", "source_record_output_missing", f"Compiled source output is missing: {key}.", path))
        records_path = repo_root / output.get("records_path", "")
        qc_path = repo_root / output.get("qc_path", "")
        if records_path.exists() and qc_path.exists():
            records = _read_json(records_path)
            qc = _read_json(qc_path)
            if qc.get("record_count") != len(records):
                issues.append(_issue("blocker", "source_record_qc_count_mismatch", "QC record count does not match compiled source records.", qc_path))
            if output.get("sha256") and _sha256(records_path) != output["sha256"]:
                issues.append(_issue("blocker", "source_record_hash_mismatch", "Compiled source record hash does not match the source record profile manifest.", records_path))

    asset_manifest = _read_json(repo_root / "data" / "source_corpus" / "SOURCE_ASSET_MANIFEST.json")
    for asset in asset_manifest.get("assets", []):
        path = repo_root / asset.get("harness_relative_path", "")
        if not path.exists():
            issues.append(_issue("blocker", "source_asset_file_missing", "Source asset manifest points to a missing file.", path))
            continue
        if asset.get("sha256") and _sha256(path) != asset["sha256"]:
            issues.append(_issue("blocker", "source_asset_hash_mismatch", "Source asset hash does not match the source asset manifest.", path))
        if asset.get("byte_size") is not None and path.stat().st_size != asset["byte_size"]:
            issues.append(_issue("blocker", "source_asset_size_mismatch", "Source asset byte size does not match the source asset manifest.", path))
        if not asset.get("source_id_links"):
            issues.append(_issue("blocker", "source_asset_unlinked", "Source asset has no source authority link.", path))

    record_manifest = _read_json(repo_root / "data" / "source_corpus" / "source_record_manifest.json")
    for record in record_manifest.get("records", []):
        path = repo_root / record.get("harness_relative_path", "")
        if not path.exists():
            issues.append(_issue("blocker", "source_record_manifest_file_missing", "Source record manifest points to a missing record file.", path))
            continue
        if record.get("sha256") and _sha256(path) != record["sha256"]:
            issues.append(_issue("blocker", "source_record_manifest_hash_mismatch", "Source record hash does not match the source record manifest.", path))


def _check_source_authority_consistency(repo_root: Path, issues: list[ReadinessIssue]) -> None:
    source_manifest_path = repo_root / "data" / "fixtures" / "source_manifest.json"
    if not source_manifest_path.exists():
        issues.append(_issue("blocker", "fixture_source_manifest_missing", "Fixture source manifest is missing.", source_manifest_path))
        return
    source_manifest = _read_json(source_manifest_path)
    record_manifest_path = repo_root / "data" / "source_corpus" / "source_record_manifest.json"
    record_source_ids: set[str] = set()
    if record_manifest_path.exists():
        record_manifest = _read_json(record_manifest_path)
        record_source_ids = {entry.get("source_id") for entry in record_manifest.get("records", []) if entry.get("source_id")}

    for source in source_manifest.get("sources", []):
        for mismatch in registry_mismatches_for_source(source):
            issues.append(_issue("blocker", mismatch, f"Source manifest entry is inconsistent with source-authority registry: {source.get('source_id')}.", source_manifest_path))
        if source.get("anchors") and source.get("authority_class") != "internal_generated_candidate":
            concrete_ids = set(concrete_source_ids(source.get("source_id", "")))
            if concrete_ids.isdisjoint(record_source_ids):
                issues.append(_issue("blocker", "source_anchor_record_unresolved", f"Source anchors do not resolve to compiled source records: {source.get('source_id')}.", source_manifest_path))

    if record_manifest_path.exists():
        record_manifest = _read_json(record_manifest_path)
        for entry in record_manifest.get("records", []):
            for mismatch in registry_mismatches_for_record_manifest_entry(entry):
                issues.append(_issue("blocker", mismatch, f"Source record manifest entry is inconsistent with source-authority registry: {entry.get('source_id')}.", record_manifest_path))

    asset_manifest_path = repo_root / "data" / "source_corpus" / "SOURCE_ASSET_MANIFEST.json"
    if asset_manifest_path.exists():
        asset_manifest = _read_json(asset_manifest_path)
        for asset in asset_manifest.get("assets", []):
            for source_id in asset.get("source_id_links", []):
                if source_id not in SOURCE_AUTHORITIES:
                    issues.append(_issue("blocker", "source_asset_link_unregistered", f"Source asset links to an unregistered source ID: {source_id}.", asset_manifest_path))


def _check_runtime_isolation(repo_root: Path, run_id: str, issues: list[ReadinessIssue]) -> None:
    manifest_path = repo_root / "runs" / run_id / "RUN_MANIFEST.json"
    if not manifest_path.exists():
        issues.append(_issue("warning", "run_manifest_absent", "No existing run manifest was found to inspect runtime isolation.", manifest_path))
        return
    try:
        path_audit = audit_runtime_paths(repo_root, run_id)
    except Exception as exc:
        issues.append(_issue("blocker", "runtime_path_audit_failed", f"Runtime path audit failed: {exc}", manifest_path))
        return
    if not path_audit.baseline_isolated:
        issues.append(_issue("blocker", "reference_baseline_used_as_runtime_input", "Runtime inputs must not point into reference_baseline.", manifest_path))
    manifest = _read_json(manifest_path)
    for runtime_path in manifest.get("runtime_input_paths", []):
        if "source_repo/staging/hs-slice" in runtime_path or "reference_baseline" in runtime_path:
            issues.append(_issue("blocker", "old_source_repo_output_used_as_runtime_input", "Runtime inputs must not use old source extraction system outputs or comparison baselines.", manifest_path))


def _check_run_graph_schema(repo_root: Path, run_id: str, issues: list[ReadinessIssue]) -> None:
    run_root = repo_root / "runs" / run_id
    graph_root = run_root / "graph"
    if not graph_root.exists():
        issues.append(_issue("warning", "run_graph_absent", "No existing graph artifact directory was found to inspect.", graph_root))
        return
    node_ids: set[str] = set()
    for path in (graph_root / "entities").glob("*.json"):
        node = _read_json(path)
        if not node.get("node_id") or not node.get("node_type"):
            issues.append(_issue("blocker", "graph_node_required_fields_missing", "Graph node is missing node_id or node_type.", path))
            continue
        node_ids.add(node["node_id"])
        if node.get("node_type") not in GRAPH_NODE_TYPES:
            issues.append(_issue("blocker", "graph_node_type_invalid", f"Graph node type is not schema-valid: {node.get('node_type')}.", path))
    for path in (graph_root / "relationships").glob("*.json"):
        edge = _read_json(path)
        if not all(edge.get(key) for key in ("edge_id", "edge_type", "source_node_id", "target_node_id")):
            issues.append(_issue("blocker", "graph_edge_required_fields_missing", "Graph edge is missing required fields.", path))
            continue
        if edge.get("edge_type") not in GRAPH_EDGE_TYPES:
            issues.append(_issue("blocker", "graph_edge_type_invalid", f"Graph edge type is not schema-valid: {edge.get('edge_type')}.", path))
        if edge.get("source_node_id") not in node_ids or edge.get("target_node_id") not in node_ids:
            issues.append(_issue("blocker", "graph_edge_endpoint_unresolved", "Graph edge source or target node is not present in the graph node set.", path))


def _check_knowledge_evidence_registry(repo_root: Path, issues: list[ReadinessIssue]) -> None:
    path = repo_root / "protocol" / "knowledge_evidence_registry.json"
    if not path.exists():
        issues.append(_issue("blocker", "knowledge_evidence_registry_missing", "Knowledge-evidence registry is missing.", path))
        return
    registry = _read_json(path)
    for item in registry.get("entries", []):
        required = ("paper_section", "metric_id", "control_family", "legal_rationale", "supporting_source", "evidence_status")
        missing = [field for field in required if not item.get(field)]
        if missing:
            issues.append(_issue("blocker", "knowledge_evidence_entry_incomplete", f"Knowledge-evidence entry is missing fields: {', '.join(missing)}.", path))
        if canonical_authority_class(item.get("supporting_authority_class")) != item.get("supporting_authority_class"):
            issues.append(_issue("warning", "knowledge_evidence_uses_legacy_authority_alias", "Knowledge-evidence registry should use canonical authority classes.", path))


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _issue(severity: str, code: str, message: str, path: Path | str | None = None) -> ReadinessIssue:
    return ReadinessIssue(severity=severity, code=code, message=message, path=str(path) if path else None)


def render_text(report: ReadinessReport) -> str:
    lines = [
        f"Readiness status: {report.status}",
        f"Blockers: {report.blocker_count}",
        f"Warnings: {report.warning_count}",
        f"Info: {report.info_count}",
    ]
    if report.issues:
        lines.append("")
        for issue in report.issues:
            suffix = f" ({issue.path})" if issue.path else ""
            lines.append(f"- [{issue.severity}] {issue.code}: {issue.message}{suffix}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check whether the bounded HS evaluation harness is ready to run.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--source-repo-root", type=Path)
    parser.add_argument("--run-id", default="paper_frozen_run")
    parser.add_argument("--json", action="store_true")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    report = run_readiness_check(args.repo_root, args.source_repo_root, run_id=args.run_id)
    if args.json:
        print(json.dumps(report.as_dict(), indent=2, sort_keys=True))
    else:
        print(render_text(report))
    return 0 if report.status == "ready" else 1


if __name__ == "__main__":
    raise SystemExit(main())
