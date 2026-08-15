"""Tests de monitor_urls.py (P4 : moniteur d'URLs mortes du registre des faits)."""

import os

import pytest

from tools.monitor_urls import find_registry_files, report_json, report_text, run, scan_file
from tools.verify_facts import classify_url


@pytest.fixture
def net(monkeypatch):
    """Désactive le DNS/SSRF pour isoler le triage HTTP (status code) du réseau."""
    monkeypatch.setattr("tools.verify_facts._validate_url", lambda url: (True, None))


# --- classify_url : triage de l'URL (dépendance P4) ---

def test_classify_alive(net, monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)
    assert classify_url("https://x.fr/x") == ("alive", "HTTP 200")


def test_classify_dead(net, monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 404)
    assert classify_url("https://x.fr/x") == ("dead", "HTTP 404")


def test_classify_unsafe():
    # Sans net : la vraie _validate_url rejette scheme interdit + loopback.
    assert classify_url("file:///etc/passwd") == ("unsafe", "scheme_not_allowed")
    assert classify_url("http://127.0.0.1/")[0] == "unsafe"


def test_classify_dns_error_unreachable():
    # Domaine non résolu : unreachable (pas unsafe) — le DNS peut être transitoire.
    assert classify_url("https://domaine-inexistant-xyz-12345.fr/")[0] == "unreachable"


def test_classify_unreachable_reseau(net, monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: None)
    assert classify_url("https://x.fr/x")[0] == "unreachable"


def test_classify_head_blocked(net, monkeypatch):
    # 403 = HEAD refusé : pas « alive », pas « dead » — liveness inconnue.
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 403)
    assert classify_url("https://x.fr/x")[0] == "head_blocked"


# --- scan_file / run ---

def _registry(facts):
    return "\n".join(["<!-- FACT_REGISTRY_V1 -->"] + facts + ["<!-- /FACT_REGISTRY_V1 -->"])


def test_scan_file_trie_et_ignore_sans_url(tmp_path, net, monkeypatch):
    f = tmp_path / "x.md"
    f.write_text(_registry([
        "FCT-001 | FACT | ✦ | https://a.fr/x | A,E | 2024-03-07",
        "FCT-002 | FACT | ✦ | https://b.fr/x | A,E |",
        "FCT-003 | FACT | ❧ | - | - |",
    ]))
    monkeypatch.setattr(
        "tools.verify_facts.head_check",
        lambda u, timeout=5: 200 if "a.fr" in u else 404)
    statuses = {e[1]: e[3] for e in scan_file(str(f), timeout=5)}
    assert statuses["FCT-001"] == "alive"
    assert statuses["FCT-002"] == "dead"
    assert "FCT-003" not in statuses  # ❧ sans URL : rien à monitorer


def test_run_offline_skipped(tmp_path):
    (tmp_path / "x.md").write_text(_registry(["FCT-001 | FACT | ✦ | https://x.fr/a | A,E |"]))
    files, entries = run([str(tmp_path)], timeout=5, offline=True)
    assert len(files) == 1 and entries[0][3] == "skipped"


def test_find_registry_files(tmp_path):
    (tmp_path / "avec.md").write_text(_registry(["FCT-001 | FACT | ✦ | https://x.fr/a | A,E |"]))
    (tmp_path / "sans.md").write_text("# pas de registre")
    (tmp_path / "note.txt").write_text("<!-- FACT_REGISTRY_V1 -->")
    files = find_registry_files([str(tmp_path)])
    assert [os.path.basename(f) for f in files] == ["avec.md"]


# --- rapports et codes retour ---

def test_report_text_dead_retourne_1(tmp_path, net, monkeypatch, capsys):
    (tmp_path / "x.md").write_text(_registry(["FCT-001 | FACT | ✦ | https://x.fr/a | A,E |"]))
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 404)
    files, entries = run([str(tmp_path)], timeout=5)
    assert report_text(files, entries) == 1
    out = capsys.readouterr().out
    assert "dead" in out and "re-vérifier" in out


def test_report_json_dead(tmp_path, net, monkeypatch, capsys):
    (tmp_path / "x.md").write_text(_registry(["FCT-001 | FACT | ✦ | https://x.fr/a | A,E |"]))
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 500)
    files, entries = run([str(tmp_path)], timeout=5)
    assert report_json(files, entries) == 1
    out = capsys.readouterr().out
    assert '"problems": 1' in out and '"dead": 1' in out


def test_report_vivant_retourne_0(tmp_path, net, monkeypatch, capsys):
    (tmp_path / "x.md").write_text(_registry(["FCT-001 | FACT | ✦ | https://x.fr/a | A,E |"]))
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)
    files, entries = run([str(tmp_path)], timeout=5)
    assert report_text(files, entries) == 0


def test_report_head_blocked_retourne_0(tmp_path, net, monkeypatch, capsys):
    # HEAD refusé (ex : Légifrance) n'est PAS un problème : pas de faux positif.
    (tmp_path / "x.md").write_text(_registry(["FCT-001 | FACT | ✦ | https://x.fr/a | A,E |"]))
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 403)
    files, entries = run([str(tmp_path)], timeout=5)
    assert report_text(files, entries) == 0
    assert "HEAD-bloqué" in capsys.readouterr().out
