"""Tests du moteur de vérification (tools/verify/verify.py) : certificat avec findings."""

import json
import os

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
