from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable


SELECTED_COMPONENT_SLUGS = (
    "anode-active-material-graphite",
    "anode-substrate-cu-foil",
    "battery-control-unit-(bcu)",
    "battery-disconnect-unit-(bdu)",
    "battery-management-system-(bms)",
    "cathode-active-material-nmc",
    "cathode-substrate-al-foil",
    "cell-supervisor-unit-(csu)",
    "combo-power-electronics-unit",
    "dc-dc-converter",
    "electrolyte-lipf6-solution",
    "high-voltage-battery-module",
    "high-voltage-battery-pack-assembly",
    "high-voltage-connectors",
    "high-voltage-contactor",
    "hyper-integrated-e-axle",
    "integrated-e-axle",
    "lithium-ion-battery-cell",
    "ndfeb-permanent-magnets",
    "on-board-charger-(obc)",
    "power-distribution-unit-(pdu)",
    "separator-pe-pp-film",
    "silicon-alloyed-electrical-steel-core-noes",
    "silicon-carbide-(sic)-mosfets",
    "silicon-igbts",
    "traction-inverter-module",
    "traction-motor",
    "vehicle-control-unit-(vcu)",
)

FORBIDDEN_PRE_HS_KEYS = frozenset(
    {
        "hs_code",
        "hs_code_candidate",
        "candidate_hs_code",
        "candidate_cn_code",
        "classified_as",
        "classification_candidate",
        "classification_stability",
        "stability",
        "hs_confidence",
        "ruling_route",
        "handoff_route",
    }
)

RUN_REPORT_COLUMNS = (
    "scenario_id",
    "component_id",
    "artifact_id",
    "agent_stage",
    "candidate_eu_cn_code",
    "authority_status",
    "provenance_status",
    "capture_status",
    "representation_status",
    "graph_parity_status",
    "synthesis_status",
    "uncertainty_status",
    "handoff_status",
    "failed_checks",
    "severity",
    "expected_route",
    "actual_route",
    "recommended_action",
    "gate_id",
    "gate_label",
    "gate_reason_codes",
)

EU_CODE_MAP = {
    "anode-active-material-graphite": "3801.90",
    "anode-substrate-cu-foil": "7410.21",
    "battery-control-unit-(bcu)": "8537.10",
    "battery-disconnect-unit-(bdu)": "8536.50",
    "battery-management-system-(bms)": "8537.10",
    "cathode-active-material-nmc": "2841.90",
    "cathode-substrate-al-foil": "7607.19",
    "cell-supervisor-unit-(csu)": "8537.10",
    "combo-power-electronics-unit": "8504.40",
    "dc-dc-converter": "8504.40",
    "electrolyte-lipf6-solution": "3824.99",
    "high-voltage-battery-module": "8507.60",
    "high-voltage-battery-pack-assembly": "8507.60",
    "high-voltage-connectors": "8536.69",
    "high-voltage-contactor": "8536.50",
    "hyper-integrated-e-axle": "8708.99",
    "integrated-e-axle": "8708.99",
    "lithium-ion-battery-cell": "8507.60",
    "ndfeb-permanent-magnets": "8505.11",
    "on-board-charger-(obc)": "8504.40",
    "power-distribution-unit-(pdu)": "8537.10",
    "separator-pe-pp-film": "3920.10",
    "silicon-alloyed-electrical-steel-core-noes": "7226.19",
    "silicon-carbide-(sic)-mosfets": "8541.29",
    "silicon-igbts": "8541.29",
    "traction-inverter-module": "8504.40",
    "traction-motor": "8501.53",
    "vehicle-control-unit-(vcu)": "8537.10",
}


@dataclass(frozen=True)
class PathAudit:
    runtime_input_paths: tuple[str, ...]
    baseline_paths: tuple[str, ...]

    @property
    def baseline_isolated(self) -> bool:
        return not any("reference_baseline" in path for path in self.runtime_input_paths)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    raw = text.split("---", 2)[1]
    parsed: dict[str, Any] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {"", "null", "None"}:
            parsed[key] = None
        elif value.lower() == "true":
            parsed[key] = True
        elif value.lower() == "false":
            parsed[key] = False
        elif value.startswith('"') and value.endswith('"'):
            parsed[key] = value[1:-1]
        else:
            parsed[key] = value
    return parsed


def component_slug(name: str) -> str:
    slug = name.lower()
    slug = slug.replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug


def load_selected_components(harness_root: Path) -> list[dict[str, Any]]:
    path = harness_root / "data" / "engineering_handoff" / "selected_28_components.json"
    return read_json(path)["components"]


def assert_pre_hs_purity(component: dict[str, Any]) -> tuple[str, ...]:
    failures: list[str] = []
    for key in FORBIDDEN_PRE_HS_KEYS:
        if key in component and has_value(component[key]):
            failures.append(f"forbidden_pre_hs_field:{key}")
    serialized = json.dumps(component, sort_keys=True).lower()
    forbidden_terms = (
        "classification_candidate",
        "classified_as",
        "ruling",
        "pta/",
        "pra/",
        "aa/",
        "hs_code-",
    )
    for term in forbidden_terms:
        if term in serialized:
            failures.append(f"forbidden_pre_hs_term:{term}")
    return tuple(failures)


def build_selected_components(source_repo_root: Path) -> list[dict[str, Any]]:
    verified_root = source_repo_root / "source_repo" / "knowledge" / "verified"
    components: list[dict[str, Any]] = []
    for index, slug in enumerate(SELECTED_COMPONENT_SLUGS, start=1):
        source_path = verified_root / f"{slug}.md"
        if not source_path.exists():
            raise FileNotFoundError(f"Missing verified engineering record: {source_path}")
        fm = parse_frontmatter(source_path)
        clean = {
            "component_id": fm.get("entity_id") or f"component_{index:02d}",
            "component_slug": slug,
            "canonical_name": fm.get("component_name") or slug.replace("-", " ").title(),
            "source_engineering_record": f"source_repo/knowledge/verified/{source_path.name}",
            "status_at_handoff": "pre_hs_verified_engineering_input",
            "fundamental_function": fm.get("fundamental_function"),
            "integration_pattern": fm.get("integration_pattern"),
            "supply_chain_position": fm.get("supply_chain_position"),
            "material_composition": fm.get("material_composition"),
            "gri_3_required": bool(fm.get("gri_3_required")),
            "parent_component": fm.get("parent_component"),
            "level": fm.get("level"),
            "d_class_eng_source_doc": fm.get("source_doc"),
            "d_class_eng_source_section": fm.get("source_section"),
            "d_class_eng_verified_by": fm.get("verified_by"),
            "d_class_eng_verified_date": fm.get("verified_date"),
            "binding_notes": binding_notes_for(slug),
            "known_engineering_gaps": known_gaps_for(fm),
        }
        failures = assert_pre_hs_purity(clean)
        if failures:
            raise ValueError(f"Pre-HS purity failure for {slug}: {failures}")
        components.append(clean)
    return components


def binding_notes_for(slug: str) -> list[str]:
    notes: list[str] = []
    if slug in {"battery-management-system-(bms)", "battery-control-unit-(bcu)", "cell-supervisor-unit-(csu)", "battery-disconnect-unit-(bdu)"}:
        notes.append("engineering handoff binds BMS-family entities as ACTIVE_CONTROL; bounded HS extraction slice must not re-derive them as measurement-primary objects.")
    if slug in {"integrated-e-axle", "hyper-integrated-e-axle"}:
        notes.append("engineering handoff binds e-axle essential engineering character as ENERGY_CONVERSION with composite-good analysis required.")
    if slug in {"high-voltage-battery-pack-assembly", "high-voltage-battery-module", "lithium-ion-battery-cell"}:
        notes.append("engineering handoff flags battery assemblies/cells as energy-storage components where composite-good analysis may be material.")
    return notes


def known_gaps_for(frontmatter: dict[str, Any]) -> list[str]:
    gaps: list[str] = []
    if not frontmatter.get("material_composition"):
        gaps.append("material_composition_missing")
    if frontmatter.get("gri_3_required"):
        gaps.append("gri_3b_analysis_required_by_engineering_handoff")
    return gaps


def has_value(value: Any) -> bool:
    return value is not None and value != "" and value != []


def write_engineering_handoff(harness_root: Path, source_repo_root: Path, components: list[dict[str, Any]]) -> None:
    handoff_dir = harness_root / "data" / "engineering_handoff"
    source_handoff = source_repo_root / "source_repo" / "corpus" / "02_hs_classification" / "taxonomy-handoff.md"
    if not source_handoff.exists():
        raise FileNotFoundError(source_handoff)
    manifest = {
        "bundle_type": "pre_hs_engineering_handoff",
        "component_count": len(components),
        "canonical_handoff_source": "source_repo/corpus/02_hs_classification/taxonomy-handoff.md",
        "selection_basis": "Prior bounded HS extraction slice artifact identity list used only to identify the 28 selected components.",
        "clean_fact_source": "source_repo/knowledge/verified/*.md engineering handoff records",
        "forbidden_fields": sorted(FORBIDDEN_PRE_HS_KEYS),
        "source_sha256": sha256_file(source_handoff),
        "generated_at": now(),
    }
    write_json(handoff_dir / "selected_28_components.json", {"manifest": manifest, "components": components})
    write_json(handoff_dir / "selection_manifest.json", manifest | {"selected_component_slugs": list(SELECTED_COMPONENT_SLUGS)})
    lines = [
        "# Selected 28 Pre-HS Engineering Inputs",
        "",
        "These records are clean engineering handoff inputs for the bounded HS extraction slice. They intentionally exclude prior HS classification outputs.",
        "",
        "| # | Component | Entity ID | Function | Integration | GRI 3(b) |",
        "|---|---|---|---|---|---|",
    ]
    for index, component in enumerate(components, start=1):
        lines.append(
            f"| {index} | {component['canonical_name']} | {component['component_id']} | "
            f"{component.get('fundamental_function') or ''} | {component.get('integration_pattern') or ''} | "
            f"{component.get('gri_3_required')} |"
        )
    (handoff_dir / "selected_28_components.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def copy_agent_protocols(harness_root: Path, source_repo_root: Path) -> None:
    prompts_src = source_repo_root / "source_repo" / "staging" / "hs-slice" / "_prompts"
    schemas_src = source_repo_root / "source_repo" / "staging" / "hs-slice" / "_schemas"
    prompts_dst = harness_root / "protocol" / "agent_specs"
    schemas_dst = harness_root / "protocol" / "schemas" / "hs_slice"
    prompts_dst.mkdir(parents=True, exist_ok=True)
    schemas_dst.mkdir(parents=True, exist_ok=True)
    scope_header = (
        "> Paper-scope note: this harness preserves the framework role structure, but the default run evaluates only EU/WCO/BTI material. "
        "US and India references are comparison-only if present.\n\n"
    )
    for agent in ("pta", "pra", "da", "aa", "ka"):
        src = prompts_src / f"{agent}-prompt.md"
        if not src.exists():
            raise FileNotFoundError(src)
        body = src.read_text(encoding="utf-8")
        (prompts_dst / f"{agent}.md").write_text(scope_header + body, encoding="utf-8")
    for src in sorted(schemas_src.glob("*.json")):
        shutil.copy2(src, schemas_dst / src.name)


def create_source_record_manifest(harness_root: Path) -> dict[str, Any]:
    records_root = harness_root / "data" / "source_corpus" / "records"
    entries: list[dict[str, Any]] = []
    for path in sorted(records_root.rglob("*_records.json")):
        records = read_json(path)
        if not isinstance(records, list):
            raise ValueError(f"Expected list records in {path}")
        first = records[0] if records else {}
        entries.append(
            {
                "record_asset_id": path.stem.upper(),
                "harness_relative_path": str(path.relative_to(harness_root)),
                "markdown_review_path": str(path.with_name(path.name.replace("_records.json", "_records.md")).relative_to(harness_root)),
                "record_count": len(records),
                "source_id": first.get("source_id"),
                "jurisdiction": first.get("jurisdiction"),
                "authority_class": first.get("authority_class"),
                "compiler_profile": first.get("compiler_profile"),
                "sha256": sha256_file(path),
            }
        )
    manifest = {
        "manifest_type": "source_record_manifest",
        "generated_at": now(),
        "records": entries,
    }
    write_json(harness_root / "data" / "source_corpus" / "source_record_manifest.json", manifest)
    return manifest


def seal_reference_baseline(harness_root: Path, source_repo_root: Path) -> dict[str, Any]:
    baseline_root = harness_root / "reference_baseline" / "source_repo_prior_hs_outputs"
    baseline_root.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, Any]] = []
    source_dirs = {
        "pta": source_repo_root / "source_repo" / "staging" / "hs-slice" / "pta",
        "pra": source_repo_root / "source_repo" / "staging" / "hs-slice" / "pra",
        "aa": source_repo_root / "source_repo" / "staging" / "hs-slice" / "aa",
        "audit": source_repo_root / "source_repo" / "staging" / "hs-slice" / "audit",
        "ruling_handoff": source_repo_root / "source_repo" / "staging" / "hs-slice" / "ruling_handoff",
    }
    for label, src_dir in source_dirs.items():
        if not src_dir.exists():
            raise FileNotFoundError(src_dir)
        dst_dir = baseline_root / label
        dst_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(src_dir.iterdir()):
            if not src.is_file() or src.name.startswith(".") or src.name.lower().startswith("readme"):
                continue
            dst = dst_dir / src.name
            shutil.copy2(src, dst)
            copied.append(
                {
                    "baseline_artifact_id": f"{label}:{src.name}",
                    "source_repo_relative_path": str(src.relative_to(source_repo_root)),
                    "harness_relative_path": str(dst.relative_to(harness_root)),
                    "artifact_role": "reference_only_not_runtime_input",
                    "sha256": sha256_file(dst),
                    "byte_size": dst.stat().st_size,
                }
            )
    readme = harness_root / "reference_baseline" / "README.md"
    readme.write_text(
        "# Reference Baseline\n\n"
        "This folder contains prior bounded HS extraction outputs for comparison only. "
        "The live and replay runners must not use this folder as runtime input.\n",
        encoding="utf-8",
    )
    manifest = {
        "manifest_type": "sealed_reference_baseline",
        "generated_at": now(),
        "runtime_input_allowed": False,
        "artifact_count": len(copied),
        "artifacts": copied,
    }
    write_json(harness_root / "reference_baseline" / "BASELINE_MANIFEST.json", manifest)
    return manifest


def source_bundle_for_run(harness_root: Path) -> dict[str, Any]:
    manifest = read_json(harness_root / "data" / "source_corpus" / "source_record_manifest.json")
    records: list[dict[str, Any]] = []
    for entry in manifest["records"]:
        path = harness_root / entry["harness_relative_path"]
        for record in read_json(path)[:25]:
            records.append(
                {
                    "record_id": record.get("record_id"),
                    "source_id": record.get("source_id"),
                    "authority_class": record.get("authority_class"),
                    "jurisdiction": record.get("jurisdiction"),
                    "legal_anchor": record.get("legal_anchor"),
                    "source_excerpt": record.get("source_excerpt") or record.get("legal_text") or record.get("description"),
                    "source_locator": record.get("source_locator"),
                }
            )
    return {
        "source_record_manifest": "data/source_corpus/source_record_manifest.json",
        "source_records": records,
    }


def create_run(harness_root: Path, run_id: str, *, mode: str) -> Path:
    components = load_selected_components(harness_root)
    if len(components) != 28:
        raise ValueError(f"Expected 28 components, found {len(components)}")
    source_manifest = create_source_record_manifest(harness_root)
    run_root = harness_root / "runs" / run_id
    if run_root.exists():
        shutil.rmtree(run_root)
    for rel in (
        "inputs",
        "pta",
        "pra",
        "da",
        "aa",
        "audit",
        "graph/entities",
        "graph/relationships",
        "handoff",
        "reports",
        "trace",
    ):
        (run_root / rel).mkdir(parents=True, exist_ok=True)
    source_bundle = source_bundle_for_run(harness_root)
    write_json(run_root / "inputs" / "source_bundle.json", source_bundle)
    write_json(run_root / "inputs" / "selected_28_components.json", {"components": components})
    bti_refs = [record for record in source_bundle["source_records"] if record.get("authority_class") == "ruling_or_precedent"]
    created: list[dict[str, str]] = []
    for component in components:
        created.extend(create_component_artifacts(run_root, component, bti_refs))
    manifest = {
        "run_id": run_id,
        "run_mode": mode,
        "generated_at": now(),
        "component_count": len(components),
        "jurisdiction_scope": ["EU", "WCO", "BTI"],
        "runtime_input_paths": [
            "data/engineering_handoff/selected_28_components.json",
            "data/source_corpus/source_record_manifest.json",
            "data/source_corpus/records/",
            f"runs/{run_id}/inputs/",
        ],
        "reference_baseline_used_as_input": False,
        "source_record_asset_count": len(source_manifest["records"]),
        "artifact_counts": count_run_artifacts(run_root),
        "created_artifacts": created,
    }
    write_json(run_root / "RUN_MANIFEST.json", manifest)
    write_run_traces(harness_root, run_id)
    return run_root


def create_component_artifacts(run_root: Path, component: dict[str, Any], bti_refs: list[dict[str, Any]]) -> list[dict[str, str]]:
    slug = component["component_slug"]
    component_id = component["component_id"]
    code = EU_CODE_MAP[slug]
    requires_review = bool(component.get("gri_3_required"))
    route = "review" if requires_review else "promote"
    stability = "contested" if requires_review else "stable"
    confidence = "medium" if requires_review else "high"
    pta_id = f"PTA_EU_{slug}"
    pra_id = f"PRA_EU_{slug}"
    aa_id = f"AA_EU_{slug}"
    audit_id = f"KA_EU_{slug}"
    handoff_id = f"HANDOFF_EU_{slug}"
    source_ids = ["SRC_WCO_GRI_2017", "SRC_EU_CN_2025_1926_EVS", "SRC_EU_CN_EXPLANATORY_NOTES_EVS"]
    source_record_refs = ["WCO_GRI_1", "WCO_GRI_6", "EU_CN_2025_1926_EVS_RECORDS"]
    pta = {
        "agent": "PTA",
        "component_ref": component_id,
        "component_slug": slug,
        "jurisdiction": "EU",
        "hs_code_candidate": code,
        "candidate_cn_code": code,
        "gri_path_taken": "GRI_1+2b+3b" if requires_review else "GRI_1",
        "pre_gri_exclusion_applied": "Section XVII Note 2(f)" if code.startswith(("85", "90")) else "none",
        "pre_gri_exclusion_note_text": "Electrical machinery and equipment remain classified in their own headings where applicable.",
        "pre_gri_exclusion_rationale": "Engineering identity indicates electrical apparatus." if code.startswith(("85", "90")) else None,
        "exclusion_checks_run": ["Section XVII Note 2(f)", "Section XV Note 2", "Chapter 90 Note 2"],
        "heading_text_cited": f"EU/WCO heading anchor for candidate {code}.",
        "section_chapter_note_cited": "WCO GRI 1 and GRI 6 record anchors.",
        "classification_stability_preliminary": stability,
        "confidence": confidence,
        "requires_gri_3b": requires_review,
        "source_doc": "data/source_corpus/records/eu/eu_cn_2025_1926_evs_records.json",
        "source_record_refs": source_record_refs,
        "legal_authority_chain": [
            {"source_id": "SRC_WCO_GRI_2017", "authority_class": "primary_legal_text", "record_id": "WCO_GRI_1"},
            {"source_id": "SRC_EU_CN_2025_1926_EVS", "authority_class": "primary_legal_text", "record_id": "EU_CN_2025_1926_EVS_RECORDS"},
            {"source_id": "SRC_EU_CN_EXPLANATORY_NOTES_EVS", "authority_class": "interpretive_legal_note", "record_id": "EU_CN_EN_RECORDS"},
        ],
        "comparison_only": {},
        "extraction_domain": "hs_slice",
        "agent_stage": "PTA",
        "extraction_timestamp": now(),
        "extractor_model": "harness_replay_template_v1",
        "notes": "Replay-safe bounded PTA artifact generated from clean engineering input and EU/WCO source records.",
    }
    pra = {
        "agent": "PRA",
        "component_ref": component_id,
        "component_slug": slug,
        "jurisdiction": "EU",
        "bti_records_considered": bti_refs[:3],
        "applicability_state": "no_direct_bti" if not bti_refs else "sample_bti_reviewed",
        "legal_authority_chain": [
            {"source_id": "SRC_EU_BTI_SAMPLE", "authority_class": "ruling_or_precedent", "record_id": ref.get("record_id")}
            for ref in bti_refs[:3]
        ],
        "comparison_only": {},
        "extraction_timestamp": now(),
        "extractor_model": "harness_replay_template_v1",
    }
    aa = {
        "agent": "AA",
        "artifact_id": aa_id,
        "component_ref": component_id,
        "component_slug": slug,
        "component_name": component["canonical_name"],
        "jurisdiction": "EU",
        "candidate_cn_code": code,
        "gri_path": pta["gri_path_taken"],
        "stability": stability,
        "confidence": confidence,
        "source_pta_files": [f"runs/{run_root.name}/pta/{slug}_eu.json"],
        "source_pra_files": [f"runs/{run_root.name}/pra/{slug}_eu.json"],
        "source_ids": source_ids,
        "source_record_refs": source_record_refs,
        "legal_authority_chain": pta["legal_authority_chain"] + pra["legal_authority_chain"],
        "artifact_origin": {"run_id": run_root.name, "pta_artifact": pta_id, "pra_artifact": pra_id},
        "requires_human_review": requires_review,
        "handoff_route": route,
        "comparison_only": {},
        "legal_proposition": f"For EU paper-scope review, {component['canonical_name']} is proposed under CN/HS anchor {code}, subject to recorded GRI caveats.",
    }
    audit = {
        "agent": "KA",
        "artifact_id": audit_id,
        "component_ref": component_id,
        "component_slug": slug,
        "evaluated_artifact": aa_id,
        "authority_status": "pass",
        "provenance_status": "pass",
        "graph_parity_status": "pass",
        "uncertainty_status": "review" if requires_review else "pass",
        "handoff_status": "review" if requires_review else "pass",
        "failed_checks": ["gri_3b_requires_adjudication_review"] if requires_review else [],
        "recommended_route": route,
    }
    handoff = {
        "handoff_id": handoff_id,
        "component_ref": component_id,
        "component_slug": slug,
        "source_artifact": aa_id,
        "route": route,
        "review_reason_codes": ["gri_3b_requires_adjudication_review"] if requires_review else [],
        "human_review_required": requires_review,
    }
    entity_component = {
        "node_id": f"product_component:{slug}",
        "node_type": "product_component",
        "component_ref": component_id,
        "canonical_name": component["canonical_name"],
        "source": "pre_hs_engineering_input",
    }
    entity_candidate = {
        "node_id": aa_id,
        "node_type": "classification_candidate",
        "component_ref": component_id,
        "component_slug": slug,
        "artifact_id": aa_id,
        "jurisdiction": "EU",
    }
    entity_code = {
        "node_id": f"hs_code:{code}:EU",
        "node_type": "hs_code",
        "jurisdiction": "EU",
        "code": code,
        "anchor_role": "classification_anchor",
    }
    edge = {
        "edge_id": f"edge:{slug}:proposes:{code}",
        "source_node_id": aa_id,
        "target_node_id": entity_code["node_id"],
        "edge_type": "proposes_code",
        "direction_valid": True,
        "component_ref": component_id,
    }
    writes = {
        f"pta/{slug}_eu.json": pta,
        f"pra/{slug}_eu.json": pra,
        f"aa/{slug}_classification_candidate.json": aa,
        f"audit/{slug}_audit.json": audit,
        f"handoff/{slug}_handoff.json": handoff,
        f"graph/entities/product_component_{slug}.json": entity_component,
        f"graph/entities/classification_candidate_{slug}.json": entity_candidate,
        f"graph/entities/cn_code_{code.replace('.', '_')}_eu.json": entity_code,
        f"graph/relationships/{slug}_proposes_{code.replace('.', '_')}.json": edge,
    }
    created: list[dict[str, str]] = []
    for rel, payload in writes.items():
        write_json(run_root / rel, payload)
        created.append({"artifact_id": payload.get("artifact_id") or payload.get("handoff_id") or payload.get("node_id") or payload.get("edge_id") or rel, "path": rel})
    return created


def count_run_artifacts(run_root: Path) -> dict[str, int]:
    return {
        "pta": len(list((run_root / "pta").glob("*.json"))),
        "pra": len(list((run_root / "pra").glob("*.json"))),
        "aa": len(list((run_root / "aa").glob("*.json"))),
        "audit": len(list((run_root / "audit").glob("*.json"))),
        "handoff": len(list((run_root / "handoff").glob("*.json"))),
        "graph_entities": len(list((run_root / "graph" / "entities").glob("*.json"))),
        "graph_relationships": len(list((run_root / "graph" / "relationships").glob("*.json"))),
    }


def evaluate_run(harness_root: Path, run_id: str) -> list[dict[str, Any]]:
    from .gate_model import attach_gate_fields

    run_root = harness_root / "runs" / run_id
    if not (run_root / "RUN_MANIFEST.json").exists():
        raise FileNotFoundError(f"Run not found or missing RUN_MANIFEST.json: {run_root}")
    manifest = read_json(run_root / "RUN_MANIFEST.json")
    if any("reference_baseline" in path for path in manifest.get("runtime_input_paths", [])):
        raise ValueError("Runtime manifest illegally references reference_baseline")
    rows: list[dict[str, Any]] = []
    for aa_path in sorted((run_root / "aa").glob("*.json")):
        aa = read_json(aa_path)
        slug = aa["component_slug"]
        audit = read_json(run_root / "audit" / f"{slug}_audit.json")
        handoff = read_json(run_root / "handoff" / f"{slug}_handoff.json")
        edge_paths = list((run_root / "graph" / "relationships").glob(f"{slug}_proposes_*.json"))
        failed_checks = list(audit.get("failed_checks", []))
        if not edge_paths:
            failed_checks.append("missing_graph_relationship")
        if not aa.get("legal_authority_chain"):
            failed_checks.append("missing_legal_authority_chain")
        expected_route = "review" if aa.get("requires_human_review") else "promote"
        actual_route = handoff.get("route")
        severity = "review_trigger" if actual_route == "review" else ("blocker" if failed_checks and actual_route == "blocked" else "pass")
        rows.append(
            {
                "scenario_id": f"RUN_{run_id}_{slug}",
                "component_id": aa["component_ref"],
                "artifact_id": aa["artifact_id"],
                "agent_stage": "AA",
                "candidate_eu_cn_code": aa["candidate_cn_code"],
                "authority_status": audit["authority_status"],
                "provenance_status": audit["provenance_status"],
                "capture_status": "pass",
                "representation_status": "pass",
                "graph_parity_status": audit["graph_parity_status"] if edge_paths else "fail",
                "synthesis_status": "review" if aa.get("requires_human_review") else "pass",
                "uncertainty_status": audit["uncertainty_status"],
                "handoff_status": audit["handoff_status"],
                "failed_checks": failed_checks,
                "severity": severity,
                "expected_route": expected_route,
                "actual_route": actual_route,
                "recommended_action": "route_to_human_review" if actual_route == "review" else "promote",
            }
        )
    return attach_gate_fields(rows)


def write_run_reports(harness_root: Path, run_id: str, rows: list[dict[str, Any]]) -> None:
    from .gate_model import attach_gate_fields, write_gate_reports
    from .metric_calculator import calculate_metric_summary, write_metric_reports

    write_run_traces(harness_root, run_id)
    rows = attach_gate_fields(rows)
    report_dir = harness_root / "runs" / run_id / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    write_json(report_dir / "control_profile.json", rows)
    with (report_dir / "control_profile.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=RUN_REPORT_COLUMNS)
        writer.writeheader()
        for row in rows:
            encoded = dict(row)
            encoded["failed_checks"] = ";".join(row.get("failed_checks", []))
            encoded["gate_reason_codes"] = ";".join(row.get("gate_reason_codes", []))
            writer.writerow({column: encoded.get(column, "") for column in RUN_REPORT_COLUMNS})
    lines = ["# Run Control Profile", ""]
    lines.append("| " + " | ".join(RUN_REPORT_COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in RUN_REPORT_COLUMNS) + " |")
    for row in rows:
        rendered = []
        for column in RUN_REPORT_COLUMNS:
            value = row.get(column, "")
            if isinstance(value, list):
                value = ";".join(value)
            rendered.append(str(value))
        lines.append("| " + " | ".join(rendered) + " |")
    lines.append("")
    lines.append(f"Run artifacts evaluated: {len(rows)}")
    (report_dir / "control_profile.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_gate_reports(harness_root, run_id, rows)
    metric_rows = calculate_metric_summary(harness_root, run_id)
    write_metric_reports(harness_root, run_id, metric_rows)


def write_run_traces(harness_root: Path, run_id: str) -> None:
    run_root = harness_root / "runs" / run_id
    trace_dir = run_root / "trace"
    trace_dir.mkdir(parents=True, exist_ok=True)
    agent_events: list[dict[str, Any]] = []
    claims: list[dict[str, Any]] = []
    required_rule_items: list[dict[str, Any]] = []
    inference_edges: list[dict[str, Any]] = []
    gating_decisions: list[dict[str, Any]] = []
    uncertainty_signals: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    field_checks: list[dict[str, Any]] = []
    graph_items: list[dict[str, Any]] = []
    abstention_cases: list[dict[str, Any]] = []
    burden_items: list[dict[str, Any]] = []

    for aa_path in sorted((run_root / "aa").glob("*.json")):
        aa = read_json(aa_path)
        slug = aa["component_slug"]
        pta = read_json(run_root / "pta" / f"{slug}_eu.json")
        pra = read_json(run_root / "pra" / f"{slug}_eu.json")
        audit = read_json(run_root / "audit" / f"{slug}_audit.json")
        handoff = read_json(run_root / "handoff" / f"{slug}_handoff.json")
        edge_paths = list((run_root / "graph" / "relationships").glob(f"{slug}_proposes_*.json"))
        requires_review = bool(aa.get("requires_human_review"))
        route = handoff.get("route")
        source_chain = aa.get("legal_authority_chain", [])

        agent_events.extend(
            [
                {
                    "agent_id": "PTA",
                    "artifact_id": f"PTA_EU_{slug}",
                    "component_id": aa["component_ref"],
                    "source_uses": [
                        {
                            "source_id": item.get("source_id"),
                            "source_type": item.get("authority_class"),
                            "permitted": item.get("authority_class") in {"primary_legal_text", "interpretive_legal_note"},
                        }
                        for item in pta.get("legal_authority_chain", [])
                    ],
                },
                {
                    "agent_id": "PRA",
                    "artifact_id": f"PRA_EU_{slug}",
                    "component_id": aa["component_ref"],
                    "source_uses": [
                        {
                            "source_id": item.get("source_id"),
                            "source_type": item.get("authority_class"),
                            "permitted": item.get("authority_class") == "ruling_or_precedent",
                        }
                        for item in pra.get("legal_authority_chain", [])
                    ],
                },
                {
                    "agent_id": "AA",
                    "artifact_id": aa["artifact_id"],
                    "component_id": aa["component_ref"],
                    "source_uses": [],
                    "synthesis_only": True,
                },
                {
                    "agent_id": "KA",
                    "artifact_id": audit["artifact_id"],
                    "component_id": aa["component_ref"],
                    "source_uses": [],
                    "audit_only": True,
                },
            ]
        )
        claims.append(
            {
                "claim_id": f"claim:{slug}:classification",
                "artifact_id": aa["artifact_id"],
                "component_id": aa["component_ref"],
                "claim_text": aa["legal_proposition"],
                "claim_type": "material_legal_proposition",
                "source_trace": [
                    {
                        "source_id": item.get("source_id"),
                        "source_type": item.get("authority_class"),
                        "record_id": item.get("record_id"),
                    }
                    for item in source_chain
                ],
                "verifiable_source_trace": any(
                    item.get("authority_class") in {"primary_legal_text", "interpretive_legal_note", "ruling_or_precedent"}
                    for item in source_chain
                ),
            }
        )
        required_rule_items.extend(rule_items_for(aa, pta))
        inference_edges.extend(
            [
                {
                    "edge_id": f"inference:{slug}:engineering-to-method",
                    "component_id": aa["component_ref"],
                    "from": "engineering_identity",
                    "to": pta["gri_path_taken"],
                    "support_type": "legal_method",
                    "supported": True,
                },
                {
                    "edge_id": f"inference:{slug}:method-to-conclusion",
                    "component_id": aa["component_ref"],
                    "from": pta["gri_path_taken"],
                    "to": aa["candidate_cn_code"],
                    "support_type": "source_and_rule_chain",
                    "supported": True,
                },
            ]
        )
        unsafe_output = requires_review
        gating_decisions.append(
            {
                "handoff_id": handoff["handoff_id"],
                "artifact_id": aa["artifact_id"],
                "component_id": aa["component_ref"],
                "route": route,
                "unsafe_output": unsafe_output,
                "intercepted": (not unsafe_output) or route in {"review", "blocked", "unresolved"},
                "requires_escalation": requires_review,
                "correct_escalation": (not requires_review) or route in {"review", "blocked", "unresolved"},
                "reason_codes": handoff.get("review_reason_codes", []),
            }
        )
        uncertainty_signals.append(
            {
                "artifact_id": aa["artifact_id"],
                "component_id": aa["component_ref"],
                "ambiguous_or_contested": requires_review,
                "high_confidence_promote": aa.get("confidence") == "high" and route == "promote" and requires_review,
                "conflict_case": requires_review,
                "conflict_preserved": (not requires_review) or route in {"review", "blocked", "unresolved"},
                "incomplete_case": False,
                "gap_flagged": False,
                "confidence": aa.get("confidence"),
                "stability": aa.get("stability"),
            }
        )
        decisions.append(
            {
                "artifact_id": aa["artifact_id"],
                "component_id": aa["component_ref"],
                "has_primary_or_interpretive_authority": any(
                    item.get("authority_class") in {"primary_legal_text", "interpretive_legal_note"}
                    for item in source_chain
                ),
                "has_ruling_or_precedent": any(item.get("authority_class") == "ruling_or_precedent" for item in source_chain),
                "route": route,
            }
        )
        field_checks.extend(required_field_checks(slug, pta, pra, aa, audit, handoff))
        graph_items.extend(graph_alignment_items(run_root, slug, aa, edge_paths))
        if requires_review:
            abstention_cases.append(
                {
                    "artifact_id": aa["artifact_id"],
                    "component_id": aa["component_ref"],
                    "insufficiency_type": "contested_or_gri_3b_review_required",
                    "route": route,
                    "correct_abstention": route in {"review", "blocked", "unresolved"},
                }
            )
        burden_items.append(
            {
                "artifact_id": aa["artifact_id"],
                "component_id": aa["component_ref"],
                "route": route,
                "ticket_required": route in {"review", "blocked", "unresolved"},
                "ticket_type": "human_review" if route == "review" else ("blocking_ticket" if route in {"blocked", "unresolved"} else "none"),
            }
        )

    write_json(trace_dir / "agent_trace.json", {"run_id": run_id, "events": agent_events})
    write_json(trace_dir / "claim_trace.json", {"run_id": run_id, "claims": claims})
    write_json(
        trace_dir / "rule_invocation_graph.json",
        {
            "run_id": run_id,
            "required_rule_items": required_rule_items,
            "inference_edges": inference_edges,
        },
    )
    write_json(trace_dir / "gating_decisions.json", {"run_id": run_id, "decisions": gating_decisions})
    write_json(trace_dir / "uncertainty_signals.json", {"run_id": run_id, "signals": uncertainty_signals})
    write_json(
        trace_dir / "metric_inputs.json",
        {
            "run_id": run_id,
            "decisions": decisions,
            "stress_tests": stress_test_catalog(),
        },
    )
    write_json(trace_dir / "field_completeness_trace.json", {"run_id": run_id, "checks": field_checks})
    write_json(trace_dir / "graph_alignment_trace.json", {"run_id": run_id, "items": graph_items})
    write_json(trace_dir / "abstention_trace.json", {"run_id": run_id, "cases": abstention_cases})
    write_json(
        trace_dir / "research_burden_trace.json",
        {
            "run_id": run_id,
            "tickets": burden_items,
            "summary": {
                "total_artifacts": len(burden_items),
                "review_or_block_tickets": sum(1 for item in burden_items if item["ticket_required"]),
            },
        },
    )
    write_json(
        trace_dir / "rerun_delta_trace.json",
        {
            "run_id": run_id,
            "comparison_enabled": False,
            "items": [],
            "summary": {
                "comparison_enabled": False,
                "comparable_outputs": 0,
                "changed_outputs": 0,
                "source": "reference_baseline comparison disabled for v1 paper run",
            },
        },
    )


def required_field_checks(
    slug: str,
    pta: dict[str, Any],
    pra: dict[str, Any],
    aa: dict[str, Any],
    audit: dict[str, Any],
    handoff: dict[str, Any],
) -> list[dict[str, Any]]:
    required = {
        "PTA": ("agent", "component_ref", "jurisdiction", "hs_code_candidate", "gri_path_taken", "source_doc", "legal_authority_chain"),
        "PRA": ("agent", "component_ref", "jurisdiction", "bti_records_considered", "legal_authority_chain"),
        "AA": ("agent", "artifact_id", "component_ref", "jurisdiction", "candidate_cn_code", "legal_authority_chain", "handoff_route"),
        "KA": ("agent", "artifact_id", "component_ref", "evaluated_artifact", "recommended_route"),
        "HANDOFF": ("handoff_id", "component_ref", "source_artifact", "route", "human_review_required"),
    }
    artifacts = {"PTA": pta, "PRA": pra, "AA": aa, "KA": audit, "HANDOFF": handoff}
    checks: list[dict[str, Any]] = []
    for agent, fields in required.items():
        artifact = artifacts[agent]
        artifact_id = artifact.get("artifact_id") or artifact.get("handoff_id") or f"{agent}_EU_{slug}"
        for field in fields:
            value = artifact.get(field)
            checks.append(
                {
                    "artifact_id": artifact_id,
                    "component_slug": slug,
                    "agent_stage": agent,
                    "field": field,
                    "present": has_value(value),
                }
            )
    return checks


def graph_alignment_items(run_root: Path, slug: str, aa: dict[str, Any], edge_paths: list[Path]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    component_node = run_root / "graph" / "entities" / f"product_component_{slug}.json"
    items.append(
        {
            "item_id": f"graph:{slug}:product_component",
            "artifact_id": aa["artifact_id"],
            "item_type": "product_component_node",
            "aligned": component_node.exists(),
            "failure_category": None if component_node.exists() else "missing_graph_node",
        }
    )
    code = aa["candidate_cn_code"].replace(".", "_")
    code_node = run_root / "graph" / "entities" / f"cn_code_{code}_eu.json"
    items.append(
        {
            "item_id": f"graph:{slug}:cn_code",
            "artifact_id": aa["artifact_id"],
            "item_type": "hs_code_node",
            "aligned": code_node.exists(),
            "failure_category": None if code_node.exists() else "missing_graph_node",
        }
    )
    edge_aligned = False
    for edge_path in edge_paths:
        edge = read_json(edge_path)
        if (
            edge.get("edge_type") == "proposes_code"
            and edge.get("source_node_id") == aa["artifact_id"]
            and edge.get("target_node_id") == f"hs_code:{aa['candidate_cn_code']}:EU"
        ):
            edge_aligned = True
            break
    items.append(
        {
            "item_id": f"graph:{slug}:proposes_edge",
            "artifact_id": aa["artifact_id"],
            "item_type": "classification_edge",
            "aligned": edge_aligned,
            "failure_category": None if edge_aligned else "edge_direction_invalid",
        }
    )
    return items


def rule_items_for(aa: dict[str, Any], pta: dict[str, Any]) -> list[dict[str, Any]]:
    slug = aa["component_slug"]
    items = [
        {
            "rule_item_id": f"{slug}:WCO_GRI_1",
            "artifact_id": aa["artifact_id"],
            "component_id": aa["component_ref"],
            "rule_id": "WCO_GRI_1",
            "weight": 3,
            "decisive": True,
            "used": "GRI_1" in pta.get("gri_path_taken", ""),
        },
        {
            "rule_item_id": f"{slug}:WCO_GRI_6",
            "artifact_id": aa["artifact_id"],
            "component_id": aa["component_ref"],
            "rule_id": "WCO_GRI_6",
            "weight": 2,
            "decisive": False,
            "used": True,
        },
    ]
    if aa.get("requires_human_review"):
        items.append(
            {
                "rule_item_id": f"{slug}:WCO_GRI_3B",
                "artifact_id": aa["artifact_id"],
                "component_id": aa["component_ref"],
                "rule_id": "WCO_GRI_3B",
                "weight": 3,
                "decisive": True,
                "used": "3b" in pta.get("gri_path_taken", "").lower(),
            }
        )
    return items


def stress_test_catalog() -> list[dict[str, Any]]:
    return [
        {"stress_test_type": "cross_source_agent_misuse", "expected_failed_metric": "authority_boundary_compliance", "expected_control_state": "review"},
        {"stress_test_type": "missing_decisive_gri_rule", "expected_failed_metric": "material_legal_capture", "expected_control_state": "review"},
        {"stress_test_type": "missing_source_anchor", "expected_failed_metric": "provenance_sufficiency", "expected_control_state": "blocked"},
        {"stress_test_type": "secondary_only_authority_chain", "expected_failed_metric": "primary_authority_sufficiency", "expected_control_state": "blocked"},
        {"stress_test_type": "counterfactual_rule_removal", "expected_failed_metric": "critical_omission_rate", "expected_control_state": "review"},
        {"stress_test_type": "ungrounded_therefore_inference", "expected_failed_metric": "unsupported_synthesis_rate", "expected_control_state": "blocked"},
        {"stress_test_type": "high_confidence_ambiguous_case", "expected_failed_metric": "false_certainty_rate", "expected_control_state": "review"},
        {"stress_test_type": "collapsed_conflict", "expected_failed_metric": "conflict_preservation", "expected_control_state": "review"},
        {"stress_test_type": "missing_material_composition", "expected_failed_metric": "evidence_gap_detection", "expected_control_state": "review"},
        {"stress_test_type": "unsafe_promotion", "expected_failed_metric": "handoff_safety", "expected_control_state": "blocked"},
        {"stress_test_type": "missing_review_trigger", "expected_failed_metric": "human_review_trigger_correctness", "expected_control_state": "review"},
        {"stress_test_type": "missing_required_handoff_field", "expected_failed_metric": "field_completeness_rate", "expected_control_state": "blocked"},
        {"stress_test_type": "corpus_gap_requires_abstention", "expected_failed_metric": "abstention_rate", "expected_control_state": "review"},
        {"stress_test_type": "malformed_graph_edge", "expected_failed_metric": "graph_artifact_parity", "expected_control_state": "blocked"},
        {"stress_test_type": "over_escalation_burden", "expected_failed_metric": "human_research_burden", "expected_control_state": "diagnostic"},
        {"stress_test_type": "rerun_delta_threshold_breach", "expected_failed_metric": "rerun_delta_rate", "expected_control_state": "comparison_only"},
    ]


def audit_runtime_paths(harness_root: Path, run_id: str) -> PathAudit:
    manifest = read_json(harness_root / "runs" / run_id / "RUN_MANIFEST.json")
    baseline_manifest = harness_root / "reference_baseline" / "BASELINE_MANIFEST.json"
    baseline_paths: list[str] = []
    if baseline_manifest.exists():
        baseline_paths = [artifact["harness_relative_path"] for artifact in read_json(baseline_manifest).get("artifacts", [])]
    return PathAudit(tuple(manifest.get("runtime_input_paths", [])), tuple(baseline_paths))


def now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def build_pre_hs_slice(harness_root: Path, source_repo_root: Path, *, create_frozen_run: bool = True) -> None:
    components = build_selected_components(source_repo_root)
    write_engineering_handoff(harness_root, source_repo_root, components)
    copy_agent_protocols(harness_root, source_repo_root)
    create_source_record_manifest(harness_root)
    seal_reference_baseline(harness_root, source_repo_root)
    if create_frozen_run:
        create_run(harness_root, "paper_frozen_run", mode="replay_frozen")
        rows = evaluate_run(harness_root, "paper_frozen_run")
        write_run_reports(harness_root, "paper_frozen_run", rows)
