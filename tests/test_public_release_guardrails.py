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
    # Renamed in post-review cleanup: old directory and manifest names must not reappear.
    "forensic_evidence",
    "FORENSIC_EXPORT_MANIFEST",
    # Renamed in S2 cleanup: old d_class_eng_* field names must not reappear.
    "d_class_eng_source_doc",
    "d_class_eng_source_section",
    "d_class_eng_verified_by",
    "d_class_eng_verified_date",
    "d_class_eng_entity",
)

SKIP_DIRS = {
    ".git",
    ".obsidian",
    ".pytest_cache",
    "__pycache__",
}

# Retrospective planning documents that describe pre-remediation naming.
# They are archival records of what changed and why; sanitizing them would
# destroy their audit value.  They are intentionally excluded from the
# denylist check.
SKIP_FILES = {
    "REVIEW_REPORT_v1.md",
    "P1_REMEDIATION_PLAN.md",
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
        if rel.name in SKIP_FILES:
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
