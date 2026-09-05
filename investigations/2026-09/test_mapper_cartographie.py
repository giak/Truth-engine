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