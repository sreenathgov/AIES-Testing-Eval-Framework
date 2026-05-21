from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def fixture_paths(repo_root: Path) -> dict[str, Path]:
    return {
        "good": repo_root / "data" / "graph_fixtures" / "nodes_good.json",
        "bad": repo_root / "data" / "graph_fixtures" / "nodes_bad.json",
        "borderline": repo_root / "data" / "graph_fixtures" / "nodes_borderline.json",
        "edges": repo_root / "data" / "graph_fixtures" / "edges.json",
        "source_manifest": repo_root / "data" / "fixtures" / "source_manifest.json",
        "gold_cases": repo_root / "data" / "fixtures" / "gold_cases.json",
        "lineage_map": repo_root / "data" / "fixtures" / "FIXTURE_LINEAGE_MAP.json",
        "source_asset_manifest": repo_root / "data" / "source_corpus" / "SOURCE_ASSET_MANIFEST.json",
        "forensic_manifest": repo_root / "data" / "origin_evidence" / "ORIGIN_EXPORT_MANIFEST.json",
        "control_framework": repo_root / "protocol" / "control_framework.json",
    }


def load_fixtures(repo_root: Path) -> list[dict[str, Any]]:
    paths = fixture_paths(repo_root)
    fixtures: list[dict[str, Any]] = []
    for key in ("good", "bad", "borderline"):
        fixtures.extend(load_json(paths[key]))
    return fixtures


def load_edges(repo_root: Path) -> list[dict[str, Any]]:
    return load_json(fixture_paths(repo_root)["edges"])


def load_source_manifest(repo_root: Path) -> dict[str, Any]:
    return load_json(fixture_paths(repo_root)["source_manifest"])


def load_gold_cases(repo_root: Path) -> list[dict[str, Any]]:
    return load_json(fixture_paths(repo_root)["gold_cases"])


def load_lineage_map(repo_root: Path) -> list[dict[str, Any]]:
    return load_json(fixture_paths(repo_root)["lineage_map"])


def load_source_asset_manifest(repo_root: Path) -> dict[str, Any]:
    return load_json(fixture_paths(repo_root)["source_asset_manifest"])


def load_forensic_manifest(repo_root: Path) -> dict[str, Any]:
    return load_json(fixture_paths(repo_root)["forensic_manifest"])


def load_control_framework(repo_root: Path) -> dict[str, Any]:
    return load_json(fixture_paths(repo_root)["control_framework"])
