from __future__ import annotations

from pathlib import Path


FORBIDDEN_PUBLIC_TERMS = (
    "Drona",
    "DRONA",
    "drona",
    "D-CLASS",
    "d_class_hs",
    "sector-watch",
    "Sector Watch",
    "sector_watch",
    "metric_stress_tests",
    "DRuling",
    "D-RULING",
    "D-REG",
    "D-reg",
    "D-INCENT",
    "d_reg",
    "d_ruling",
)

SKIP_DIRS = {
    ".git",
    ".obsidian",
    ".pytest_cache",
    "__pycache__",
}

TEXT_EXTENSIONS = {
    ".csv",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


def test_public_release_denylist_is_absent_from_paths_and_text(repo_root: Path) -> None:
    violations: list[str] = []
    for path in repo_root.rglob("*"):
        rel = path.relative_to(repo_root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.as_posix() == "tests/test_public_release_guardrails.py":
            continue
        rel_text = rel.as_posix()
        for term in FORBIDDEN_PUBLIC_TERMS:
            if term in rel_text:
                violations.append(f"path:{rel_text}:{term}")
        if not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for term in FORBIDDEN_PUBLIC_TERMS:
            if term in text:
                violations.append(f"text:{rel_text}:{term}")

    assert violations == []
