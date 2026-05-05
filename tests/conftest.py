from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from legal_extract_eval.data_loader import load_edges, load_fixtures, load_gold_cases, load_source_manifest
from legal_extract_eval.evaluator import Evaluator


REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def fixtures() -> list[dict[str, Any]]:
    return load_fixtures(REPO_ROOT)


@pytest.fixture(scope="session")
def fixture_by_id(fixtures: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {fixture["artifact_id"]: fixture for fixture in fixtures}


@pytest.fixture(scope="session")
def edges() -> list[dict[str, Any]]:
    return load_edges(REPO_ROOT)


@pytest.fixture(scope="session")
def source_manifest() -> dict[str, Any]:
    return load_source_manifest(REPO_ROOT)


@pytest.fixture(scope="session")
def gold_cases() -> list[dict[str, Any]]:
    return load_gold_cases(REPO_ROOT)


@pytest.fixture(scope="session")
def gold_by_artifact(gold_cases: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {case["artifact_id"]: case for case in gold_cases}


@pytest.fixture(scope="session")
def evaluator(
    fixtures: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    source_manifest: dict[str, Any],
    gold_cases: list[dict[str, Any]],
) -> Evaluator:
    return Evaluator.from_repo(REPO_ROOT)


@pytest.fixture(scope="session")
def results_by_id(evaluator: Evaluator) -> dict[str, Any]:
    return {result.artifact_id: result for result in evaluator.evaluate_all()}
