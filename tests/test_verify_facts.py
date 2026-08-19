"""Tests de verify_facts.py (P1 : registre des faits machine-readable + gate ✦)."""

import pytest

from tools.verify_facts import (
    _is_safe_ip,
    head_check,
    parse_line,
    verify_record,
    verify_text,
)


# --- _is_safe_ip : SSRF / IP dangereuses ---

@pytest.mark.parametrize("ip,expected", [
    ("127.0.0.1", False), ("127.0.0.53", False), ("10.0.0.1", False),
    ("192.168.1.1", False), ("172.16.0.1", False), ("169.254.169.254", False),
    ("0.0.0.0", False), ("100.64.0.1", False),
    ("::1", False), ("fe80::1", False), ("fc00::1", False), ("fd00::1", False),
    ("::", False), ("ff00::1", False), ("::ffff:127.0.0.1", False),
    ("::ffff:10.0.0.1", False), ("2001:db8::1", False),
    ("8.8.8.8", True), ("1.1.1.1", True), ("93.184.216.34", True),
])
def test_is_safe_ip(ip, expected):
    assert _is_safe_ip(ip) is expected


# --- head_check : refus sans réseau (SSRF) ---

@pytest.mark.parametrize("url", [
    "file:///etc/passwd",
    "ftp://anonymous@example.com/x",
    "data:text/plain,x",
    "javascript:alert(1)",
    "http://localhost/",
    "http://127.0.0.1/",
    "http://10.0.0.1/",
    "http://192.168.1.1/",
    "http://169.254.169.254/latest/meta-data/",
    "http://[::1]/",
    "http://[::ffff:127.0.0.1]/",
])
def test_head_check_ssrf_refuse(url):
    assert head_check(url, timeout=2) is None


def test_head_check_empty_and_no_hostname():
    assert head_check("", timeout=2) is None
    assert head_check("http://", timeout=2) is None


# --- parse_line ---

def test_parse_line_ok():
    assert parse_line("FCT-001 | FACT | ✦ | https://x.fr/a | A,E | 2024-03-07") == \
        ("FCT-001", "FACT", "✦", "https://x.fr/a", "A,E", "2024-03-07", "", "", "")


def test_parse_line_avec_sujet_valeur():
    rec = parse_line("FCT-004 | FACT | ✦ | https://x.fr/c | A,E | 2024-03-07 | dgsi-effectif | 5000")
    assert rec == ("FCT-004", "FACT", "✦", "https://x.fr/c", "A,E",
                   "2024-03-07", "dgsi-effectif", "5000", "")


def test_parse_line_sans_date():
    rec = parse_line("FCT-002 | FACT | ✧ | https://x.fr/b | D |")
    assert rec is not None and rec[0] == "FCT-002" and rec[5] == ""
    assert rec[6] == "" and rec[7] == "" and rec[8] == ""


def test_parse_line_courte_invalide():
    assert parse_line("FCT-001 | FACT") is None


def test_parse_line_avec_mem():
    rec = parse_line("FCT-001 | FACT | ✦ | https://x.fr/a | A,E | 2024-03-07 | dgsi | 5000 | babe834b-7ecc-4453-a4ad-5a755253b7d9")
    assert rec[8] == "babe834b-7ecc-4453-a4ad-5a755253b7d9"


def test_parse_line_mem_dash():
    rec = parse_line("FCT-001 | FACT | ✧ | https://x.fr/a | D | | | | -")
    assert rec[8] == "-"


# --- verify_record : gates ✦ ---

def _rec(tier, epi="FACT", url="https://x.fr/a", families="A,E"):
    return ("FCT-001", epi, tier, url, families, "", "", "", "")


def test_verify_bon_fait_ok(monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)
    assert verify_record(_rec("✦")) == []


def test_verify_famille_unique_bloquee(monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)
    issues = verify_record(_rec("✦", families="D"))
    assert any("<2" in i for i in issues)


def test_verify_epi_inference_bloquee(monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)
    issues = verify_record(_rec("✦", epi="INFERENCE"))
    assert any("EPI" in i for i in issues)


def test_verify_url_morte_bloquee(monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 404)
    issues = verify_record(_rec("✦"))
    assert any("morte" in i for i in issues)


def test_verify_sans_url_bloquee():
    # url="-" : pas de HEAD-check, pas de réseau.
    issues = verify_record(_rec("✦", url="-"))
    assert any("sans URL" in i for i in issues)


def test_verify_secondaire_ok():
    assert verify_record(_rec("✧", families="D")) == []


def test_verify_secondaire_sha256_ok():
    # Locator de contenu (artefact local) : ✧ valide sans URL http(s).
    rec = ("FCT-001", "FACT", "✧", "sha256:" + "a" * 64, "-", "", "", "", "")
    assert verify_record(rec) == []


def test_verify_secondaire_sha256_malforme():
    # Hash non 64-hex : pas un localisateur valide.
    rec = ("FCT-001", "FACT", "✧", "sha256:xyz", "-", "", "", "", "")
    issues = verify_record(rec)
    assert any("sha256" in i for i in issues)


def test_verify_tier_aucune_url_constat():
    assert verify_record(("FCT-003", "FACT", "❧", "-", "-", "", "", "", "")) == []


# --- verify_text : bout en bout ---

def test_verify_text_bout_en_bout(monkeypatch):
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)
    md = "\n".join([
        "<!-- FACT_REGISTRY_V1 -->",
        "FCT-001 | FACT | ✦ | https://x.fr/a | A,E | 2024-03-07",
        "FCT-002 | INFERENCE | ✦ | https://x.fr/b | A,E |",
        "FCT-003 | FACT | ✦ | https://x.fr/c | D |",
        "<!-- /FACT_REGISTRY_V1 -->",
    ])
    lines, results = verify_text(md)
    assert len(lines) == 3
    assert "FCT-002" in results          # EPI ≠ FACT
    assert "FCT-003" in results          # 1 famille
    assert "FCT-001" not in results      # OK


def test_verify_text_sans_registre():
    lines, results = verify_text("# pas de registre ici")
    assert lines == [] and results == {}


def test_verify_text_ligne_malformee():
    md = "\n".join([
        "<!-- FACT_REGISTRY_V1 -->",
        "ligne sans pipes",
        "<!-- /FACT_REGISTRY_V1 -->",
    ])
    _lines, results = verify_text(md)
    assert "_parse" in results
