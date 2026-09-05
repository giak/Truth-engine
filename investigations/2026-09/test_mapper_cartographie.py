"""Tests du mapper de campagne 2026-09 (fixtures temporaires, jamais les données réelles)."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mapper_cartographie as mc


def build_fixture(tmp_path: Path) -> Path:
    base = tmp_path / "campagne"
    base.mkdir()

    kernel = base / "2026-09-05_achat-de-vote-france-ue"
    kernel.mkdir()
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_INVESTIGATION.md").write_text(
        "# Achat de vote - France et UE\n\nCorps du rapport.\n", encoding="utf-8"
    )
    run_state = {
        "schema": 1,
        "engine": "2.10.6",
        "run": {"id": "20260905-1100-achat-de-vote-france-ue"},
        "facts": [
            {
                "key": "achat de vote documenté",
                "value": "Affaire X : paiement constaté.",
                "epi": "FACT",
                "tier": "✦",
                "families": ["A", "B"],
                "url": "https://example.org/achat",
                "memory_id": "mem-0001",
            },
            {
                "key": "corruption locale hypothétique",
                "value": "Cas Y non tranché.",
                "epi": "FACT",
                "tier": "✧",
                "families": ["D"],
                "url": "https://example.org/corruption",
                "memory_id": "mem-0002",
            },
        ],
        "actions": [
            {"id": "ACT-001", "status": "PENDING", "text": "Saisir les juridictions."},
            {"id": "ACT-002", "status": "DONE", "text": "Déjà fait."},
        ],
        "causal": [
            {
                "id": "CAU-001",
                "status": "GAP",
                "gap_type": "EVIDENCE_GAP",
                "text": "Causalité non quantifiable.",
            }
        ],
        "leads": [
            {"id": "LED-001", "status": "OPEN", "priority": "HIGH", "subject": "Vérifier le cas Y."}
        ],
    }
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_RUN_STATE.json").write_text(
        json.dumps(run_state, ensure_ascii=False), encoding="utf-8"
    )
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_CERTIFICATION.json").write_text(
        json.dumps({"verdict": "PASS", "kernel_contract": "delivery"}), encoding="utf-8"
    )
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_INPUT.txt").write_text("input", encoding="utf-8")
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_NARRATIVE.tmp.md").write_text("n", encoding="utf-8")
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_MNEMO_SNAPSHOT.json").write_text(
        json.dumps({"snapshot_schema": 1}), encoding="utf-8"
    )

    partial = base / "2026-09-05_uk-brexit-v2"
    partial.mkdir()
    (partial / "2026-09-05_12-00_uk-brexit-v2_RUN_STATE.json").write_text(
        json.dumps({"facts": []}), encoding="utf-8"
    )

    bare = base / "2026-09-05_justice-deux-vitesses-weaponisation-judiciaire"
    bare.mkdir()
    (bare / "2026-09-05_justice-deux-vitesses_INVESTIGATION.md").write_text(
        "# Justice à deux vitesses\n", encoding="utf-8"
    )

    empty = base / "2026-09-05_uk-brexit-dark-money-flux-financiers"
    empty.mkdir()

    # Fichiers de sortie que le script doit ignorer (fichiers, pas dossiers)
    (base / mc.OUT_JSON).write_text("{}", encoding="utf-8")
    (base / mc.OUT_MD).write_text("x", encoding="utf-8")

    return base


# --- scan_dirs ---


def test_scan_dirs_retourne_dossiers_tries(tmp_path):
    base = build_fixture(tmp_path)
    dirs = mc.scan_dirs(base)
    assert dirs == sorted(dirs)
    assert len(dirs) == 4
    assert "2026-09-05_achat-de-vote-france-ue" in dirs


def test_scan_dirs_exclut_les_dossiers_prives(tmp_path):
    base = build_fixture(tmp_path)
    (base / "__pycache__").mkdir()
    (base / "__pycache__" / "mapper_cartographie.cpython-312.pyc").write_text("x", encoding="utf-8")
    dirs = mc.scan_dirs(base)
    assert "__pycache__" not in dirs
    assert len(dirs) == 4


def test_scan_dirs_exclut_les_dossiers_point_et_underscore(tmp_path):
    base = build_fixture(tmp_path)
    (base / "_replay_backups").mkdir()
    (base / "_repair_backups").mkdir()
    (base / ".hidden").mkdir()
    dirs = mc.scan_dirs(base)
    assert "_replay_backups" not in dirs
    assert "_repair_backups" not in dirs
    assert ".hidden" not in dirs
    assert len(dirs) == 4


# --- classify_dir ---


def test_classify_dir_kinds(tmp_path):
    base = build_fixture(tmp_path)
    assert mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")["kind"] == "kernel"
    assert mc.classify_dir(base, "2026-09-05_uk-brexit-v2")["kind"] == "partial"
    assert mc.classify_dir(base, "2026-09-05_justice-deux-vitesses-weaponisation-judiciaire")["kind"] == "bare"
    assert mc.classify_dir(base, "2026-09-05_uk-brexit-dark-money-flux-financiers")["kind"] == "empty"


def test_classify_dir_returns_expected_keys(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    assert set(info.keys()) == {"name", "kind", "files", "inv_file", "run_file", "cert_file"}
    assert info["name"] == "2026-09-05_achat-de-vote-france-ue"
    assert isinstance(info["files"], int)
    assert info["inv_file"] is not None
    assert info["run_file"] is not None
    assert info["cert_file"] is not None


def test_classify_dir_partial_has_run_only(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_uk-brexit-v2")
    assert info["kind"] == "partial"
    assert info["run_file"] is not None
    assert info["inv_file"] is None
    assert info["cert_file"] is None


def test_classify_dir_empty_has_zero_files(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_uk-brexit-dark-money-flux-financiers")
    assert info["kind"] == "empty"
    assert info["files"] == 0
    assert info["inv_file"] is None
    assert info["run_file"] is None
    assert info["cert_file"] is None


# --- load_json ---


def test_load_json_returns_none_for_none():
    assert mc.load_json(None) is None


def test_load_json_returns_dict_for_valid_file(tmp_path):
    p = tmp_path / "data.json"
    p.write_text(json.dumps({"key": "value"}), encoding="utf-8")
    assert mc.load_json(p) == {"key": "value"}


def test_load_json_returns_none_for_missing_file(tmp_path):
    assert mc.load_json(tmp_path / "nonexistent.json") is None


def test_load_json_returns_none_for_invalid_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("NOT JSON {{{", encoding="utf-8")
    assert mc.load_json(p) is None


# --- extraction functions ---


def test_extract_facts_sentinelles_normalisees():
    """Les sentinelles \"-\" et \"N/A\" (legacy) doivent donner \"\" pour memory_id et url."""
    run_state = {
        "facts": [
            {
                "subject": "Fait avec mem sentinel",
                "value": "test",
                "tier": "✦",
                "families": ["A"],
                "url": "https://example.org/ok",
                "mem": "-",
            },
            {
                "subject": "Fait avec url sentinel",
                "value": "test",
                "tier": "✦",
                "families": ["B"],
                "url": "N/A",
                "memory_id": "mem-0003",
            },
            {
                "subject": "Fait vide mémoire",
                "value": "test",
                "tier": "✦",
                "families": ["C"],
                "url": "",
                "mem": "",
            },
            {
                "subject": "Fait avec espaces",
                "value": "test",
                "tier": "✦",
                "families": ["D"],
                "url": "  ",
                "mem": "  -  ",
            },
        ]
    }
    facts = mc.extract_facts(run_state, "run-test", "2026-09-05_test")
    assert len(facts) == 4
    # mem="-" → memory_id ""
    assert facts[0]["memory_id"] == ""
    assert facts[0]["url"] == "https://example.org/ok"
    # url="N/A" → url ""
    assert facts[1]["url"] == ""
    assert facts[1]["memory_id"] == "mem-0003"
    # empty strings stay empty
    assert facts[2]["memory_id"] == ""
    assert facts[2]["url"] == ""
    # whitespace-only → empty
    assert facts[3]["memory_id"] == ""
    assert facts[3]["url"] == ""


def test_extract_facts_sentinelles_inflate_pas_totals():
    """with_url / with_memory_id ne doivent pas compter les sentinelles."""
    run_state = {
        "facts": [
            {"subject": "A", "tier": "✦", "url": "https://example.org", "mem": "mem-001"},
            {"subject": "B", "tier": "✦", "url": "-", "mem": "-"},
            {"subject": "C", "tier": "✦", "url": "N/A", "memory_id": "N/A"},
        ]
    }
    facts = mc.extract_facts(run_state, "run", "dir")
    with_url = sum(1 for f in facts if f["url"])
    with_mem = sum(1 for f in facts if f["memory_id"])
    assert with_url == 1  # only fact A has a real URL
    assert with_mem == 1  # only fact A has a real memory_id


def test_extract_facts_schema_mixte():
    run_state = {
        "facts": [
            {
                "subject": "Rapport Duclos obsolète",
                "value": "Le rapport cite des données dépassées.",
                "tier": "✧",
                "families": ["A"],
                "url": "https://example.org/duclos",
                "mem": "mem-reel-0001",
            },
            {
                "key": "achat de vote documenté",
                "value": "Paiement constaté.",
                "tier": "✦",
                "families": ["B"],
                "url": "https://example.org/achat",
                "memory_id": "mem-0001",
            },
        ]
    }
    facts = mc.extract_facts(run_state, "run-1", "2026-09-05_exemple")
    assert len(facts) == 2
    assert facts[0]["key"] == "Rapport Duclos obsolète"
    assert facts[0]["memory_id"] == "mem-reel-0001"
    assert facts[1]["key"] == "achat de vote documenté"
    assert facts[1]["memory_id"] == "mem-0001"


def test_extract_facts_normalise(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    facts = mc.extract_facts(rs, "run-1", "2026-09-05_achat-de-vote-france-ue")
    assert len(facts) == 2
    assert facts[0]["tier"] == "✦"
    assert facts[0]["url"] == "https://example.org/achat"
    assert facts[0]["memory_id"] == "mem-0001"
    assert facts[0]["families"] == ["A", "B"]
    assert facts[0]["origin_run"] == "run-1"
    assert facts[1]["tier"] == "✧"


def test_extract_actions_causal_leads(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    assert mc.extract_actions_pending(rs) == [
        {"id": "ACT-001", "text": "Saisir les juridictions."}
    ]
    gaps = mc.extract_causal_gaps(rs)
    assert len(gaps) == 1 and gaps[0]["id"] == "CAU-001" and gaps[0]["gap_type"] == "EVIDENCE_GAP"
    leads = mc.extract_leads_non_saturated(rs)
    assert len(leads) == 1 and leads[0]["id"] == "LED-001" and leads[0]["subject"] == "Vérifier le cas Y."


def test_extract_run_id(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    assert mc.extract_run_id(rs) == "20260905-1100-achat-de-vote-france-ue"


def test_extract_title(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    assert mc.extract_title(base, info) == "Achat de vote - France et UE"


def test_load_json_absent():
    assert mc.load_json(None) is None
    assert mc.load_json(Path("/nonexistent/path.json")) is None


# --- map_classes ---


def test_map_classes_auto_multi(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    classes = mc.map_classes(info, "Achat de vote - France et UE", rs, {})
    cls = {c["class"]: c for c in classes}
    assert "transactionnelle" in cls
    assert cls["transactionnelle"]["source"] == "auto"
    assert cls["transactionnelle"]["confidence"] == "high"


def test_map_classes_aucun_mot_cle(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_uk-brexit-dark-money-flux-financiers")
    classes = mc.map_classes(info, "", None, {})
    assert classes == []


def test_map_classes_override_prime(tmp_path):
    overrides = {"2026-09-05_achat-de-vote-france-ue": ["coercitive"]}
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    classes = mc.map_classes(info, "Achat de vote - France et UE", rs, overrides)
    assert classes == [{"class": "coercitive", "source": "override", "confidence": "high"}]


def test_campagne_classes_json_seed_valide(tmp_path):
    seed = json.loads(Path(__file__).resolve().parent.joinpath("campagne_classes.json").read_text(encoding="utf-8"))
    assert isinstance(seed, dict)
    for cls_list in seed.values():
        for c in cls_list:
            assert c in mc.CLASSES


# --- derive_gaps ---


def test_derive_gaps(tmp_path):
    base = build_fixture(tmp_path)
    subjects = []
    facts = []
    for name in mc.scan_dirs(base):
        info = mc.classify_dir(base, name)
        rs = mc.load_json(base / name / info["run_file"]) if info["run_file"] else None
        title = mc.extract_title(base, info)
        fcts = mc.extract_facts(rs, mc.extract_run_id(rs), name)
        facts += fcts
        subjects.append(
            {
                "name": name,
                "kind": info["kind"],
                "title": title,
                "actions_pending": mc.extract_actions_pending(rs),
                "causal_gaps": mc.extract_causal_gaps(rs),
                "leads_non_saturated": mc.extract_leads_non_saturated(rs),
            }
        )
    gaps = mc.derive_gaps(subjects, facts)
    assert gaps["planifie_non_execute"] == ["2026-09-05_uk-brexit-dark-money-flux-financiers"]
    assert gaps["hors_protocole"] == ["2026-09-05_justice-deux-vitesses-weaponisation-judiciaire"]
    assert gaps["partiel"] == ["2026-09-05_uk-brexit-v2"]
    assert len(gaps["candidats_elevation"]) == 1
    assert gaps["candidats_elevation"][0]["tier"] == "✧"
    assert len(gaps["actions_pending"]) == 1
    assert len(gaps["questions_ouvertes"]) == 1
    assert len(gaps["leads_a_traiter"]) == 1
    assert isinstance(gaps["angles_morts_classes"], dict)
    assert all(c in mc.CLASSES for c in gaps["angles_morts_classes"])


# --- build_data ---


def test_build_data_structure(tmp_path):
    base = build_fixture(tmp_path)
    data = mc.build_data(base, {})
    assert data["counts"]["dirs"] == 4
    assert data["counts"]["with_full_kernel"] == 1
    assert data["counts"]["with_run_state"] == 2
    assert data["counts"]["empty_dirs"] == 1
    assert data["facts_total"]["n"] == 2
    assert data["facts_total"]["tiers"]["✦"] == 1
    assert data["facts_total"]["tiers"]["✧"] == 1
    assert data["facts_total"]["with_url"] == 2
    assert data["facts_total"]["with_memory_id"] == 2
    assert len(data["subjects"]) == 4
    assert data["runs_topology"][0]["run_id"] == "20260905-1100-achat-de-vote-france-ue"
    assert "transactionnelle" in data["matrix_classes"]


# --- render_markdown ---


def test_render_markdown_sections(tmp_path):
    base = build_fixture(tmp_path)
    data = mc.build_data(base, {})
    md = mc.render_markdown(data)
    for section in (
        "## §1 Vue d'ensemble",
        "## §2 Inventaire des sujets",
        "## §3 Atlas des faits",
        "## §4 Matrice 7 classes x dossiers",
        "## §5 Gaps & leads",
        "## §6 Topographie des runs",
    ):
        assert section in md
    assert "achat de vote documenté" in md


# --- main ---


def test_main_ecrit_les_sorties(tmp_path):
    base = build_fixture(tmp_path)
    out_json = tmp_path / "sortie.json"
    out_md = tmp_path / "sortie.md"
    rc = mc.main(
        [
            "--base", str(base),
            "--overrides", str(tmp_path / "campagne_classes.json"),
            "--out-json", str(out_json),
            "--out-md", str(out_md),
        ]
    )
    assert rc == 0
    assert out_json.exists() and out_md.exists()
    data = json.loads(out_json.read_text(encoding="utf-8"))
    assert "facts" in data and "gaps" in data