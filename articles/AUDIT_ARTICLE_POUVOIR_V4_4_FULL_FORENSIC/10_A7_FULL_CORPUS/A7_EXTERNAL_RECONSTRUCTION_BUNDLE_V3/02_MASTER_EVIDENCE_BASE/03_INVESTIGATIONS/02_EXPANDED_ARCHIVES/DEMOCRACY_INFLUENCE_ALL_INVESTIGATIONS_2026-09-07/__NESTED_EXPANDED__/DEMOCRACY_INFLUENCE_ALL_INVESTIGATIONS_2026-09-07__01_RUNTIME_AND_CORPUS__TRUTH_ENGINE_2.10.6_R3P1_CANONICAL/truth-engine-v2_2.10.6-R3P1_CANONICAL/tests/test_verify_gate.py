"""Tests du moteur de vérification (tools/verify/verify.py) : certificat avec findings."""

import json
import os
from datetime import datetime, timedelta, timezone

import pytest

from tools.verify import verify


@pytest.fixture()
def workdir(tmp_path):
    """Un chantier jetable avec une config minimale."""
    (tmp_path / ".verify").mkdir()
    cfg = {
        "version": 1,
        "task": "test-task",
        "protected_branches": [],
        "tests": [],
        "checks": [],
    }
    (tmp_path / ".verify" / "config.json").write_text(
        json.dumps(cfg), encoding="utf-8"
    )
    return tmp_path


def _pending(workdir, deterministic="PASS", task="test-task"):
    (workdir / ".verify" / "pending.json").write_text(
        json.dumps(
            {
                "schema": 1,
                "task": task,
                "deterministic": deterministic,
                "head": "deadbeef",
                "state_id": "stub",
                "created_at": "now",
            }
        ),
        encoding="utf-8",
    )


# --- _load_findings ---


def test_load_findings_absent(workdir):
    findings, err = verify._load_findings(str(workdir), None)
    assert findings == [] and err is None


def test_load_findings_ok(workdir):
    f = workdir / ".verify" / "findings.json"
    f.write_text(
        json.dumps([{"location": "a.md:1", "problem": "p", "evidence": "e"}]),
        encoding="utf-8",
    )
    findings, err = verify._load_findings(str(workdir), ".verify/findings.json")
    assert err is None and len(findings) == 1
    assert findings[0]["location"] == "a.md:1"


def test_load_findings_introuvable(workdir):
    findings, err = verify._load_findings(str(workdir), ".verify/nope.json")
    assert findings == [] and err is not None


def test_load_findings_invalide(workdir):
    f = workdir / ".verify" / "findings.json"
    f.write_text("pas du json", encoding="utf-8")
    findings, err = verify._load_findings(str(workdir), ".verify/findings.json")
    assert findings == [] and err is not None


def test_load_findings_non_liste(workdir):
    f = workdir / ".verify" / "findings.json"
    f.write_text('{"verdict": "FAIL"}', encoding="utf-8")
    findings, err = verify._load_findings(str(workdir), ".verify/findings.json")
    assert findings == [] and err is not None


# --- cmd_certify : persistance des findings ---


def test_certify_persiste_findings(workdir):
    _pending(workdir)
    (workdir / ".verify" / "findings.json").write_text(
        json.dumps([{"location": "a.md:1", "problem": "p", "evidence": "e"}]),
        encoding="utf-8",
    )
    code = verify.cmd_certify(
        {"task": "test-task"}, str(workdir), "FAIL", ".verify/findings.json"
    )
    assert code == 1
    result = json.loads((workdir / ".verify" / "result.json").read_text(encoding="utf-8"))
    assert result["review"] == "FAIL"
    assert result["verdict"] == "FAIL"
    assert "findings" in result
    assert result["findings"][0]["location"] == "a.md:1"


def test_certify_sans_findings_omet_le_champ(workdir):
    _pending(workdir)
    code = verify.cmd_certify({"task": "test-task"}, str(workdir), "FAIL", None)
    assert code == 1
    result = json.loads((workdir / ".verify" / "result.json").read_text(encoding="utf-8"))
    assert "findings" not in result


def test_certify_findings_file_invalide_bloque(workdir):
    _pending(workdir)
    (workdir / ".verify" / "findings.json").write_text("broken", encoding="utf-8")
    code = verify.cmd_certify(
        {"task": "test-task"}, str(workdir), "FAIL", ".verify/findings.json"
    )
    assert code == 2  # BLOCKED, jamais PASS/FAIL silencieux


def test_certify_pending_absent_retourne_2(workdir):
    code = verify.cmd_certify({"task": "test-task"}, str(workdir), "FAIL", None)
    assert code == 2


# --- R3 P1 : portabilité Git / timezone ---

def test_run_checks_sans_git_nest_pas_bloquant(workdir):
    verdict, rows = verify.run_checks({"tests": [], "checks": [], "naming": {"enabled": False}}, str(workdir))
    assert verdict == "PASS"
    git_rows = [r for r in rows if r["name"] == "git"]
    assert len(git_rows) == 1
    assert git_rows[0]["verdict"] == "PASS"
    assert "non bloquant" in git_rows[0]["detail"]


def test_state_id_filesystem_fallback_est_stable_et_sensible(workdir):
    (workdir / "a.txt").write_text("one", encoding="utf-8")
    sid1, head1 = verify.compute_state_id(str(workdir))
    sid2, head2 = verify.compute_state_id(str(workdir))
    assert head1 == head2 == "NO_GIT"
    assert sid1 == sid2

    # Les fichiers runtime .verify sont hors identité; la config reste canonique.
    (workdir / ".verify" / "ephemeral.txt").write_text("ignored", encoding="utf-8")
    sid3, _ = verify.compute_state_id(str(workdir))
    assert sid3 == sid1

    cfg_path = workdir / ".verify" / "config.json"
    original_cfg = cfg_path.read_text(encoding="utf-8")
    cfg_path.write_text(original_cfg + "\n", encoding="utf-8")
    sid_cfg, _ = verify.compute_state_id(str(workdir))
    assert sid_cfg != sid1
    cfg_path.write_text(original_cfg, encoding="utf-8")

    (workdir / "a.txt").write_text("two", encoding="utf-8")
    sid4, _ = verify.compute_state_id(str(workdir))
    assert sid4 != sid1


def test_timestamp_naif_accepte_un_fuseau_valide_sans_dependance_process(tmp_path):
    # Un nom 13h devant UTC peut être l'heure locale courante en UTC+13.
    ts = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=13)
    f = tmp_path / (ts.strftime("%Y-%m-%d_%H-%M_") + "subject_INVESTIGATION.md")
    f.write_text("x", encoding="utf-8")
    verdict, detail = verify.check_deliverable_timestamp(str(f))
    assert verdict == "PASS", detail


def test_timestamp_naif_refuse_un_futur_impossible_dans_tous_les_fuseaux(tmp_path):
    ts = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=15)
    f = tmp_path / (ts.strftime("%Y-%m-%d_%H-%M_") + "subject_INVESTIGATION.md")
    f.write_text("x", encoding="utf-8")
    verdict, detail = verify.check_deliverable_timestamp(str(f))
    assert verdict == "FAIL"
    assert "UTC+14" in detail
