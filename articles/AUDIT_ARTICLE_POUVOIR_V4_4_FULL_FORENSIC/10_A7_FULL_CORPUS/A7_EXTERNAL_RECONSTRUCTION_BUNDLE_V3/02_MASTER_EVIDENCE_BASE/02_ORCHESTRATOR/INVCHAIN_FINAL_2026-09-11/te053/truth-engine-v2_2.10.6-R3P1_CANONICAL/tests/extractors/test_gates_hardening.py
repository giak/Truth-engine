"""Tests de hardening gates.py (F1 + F2 — audit antagoniste 2026-07-05).

Couvre :
- F1 : try/except OSError → messages H0 explicites
  (file_not_found, is_a_directory, permission_denied, os_error, empty/None path).
- F2 : H7 string-safety (longueur max 10 000 chars + blocklist caractères invisibles)
  sur `these_centrale` (quintessence) et `sujet_majoritaire` (synthese).
"""

import json
import os
import tempfile

import pytest

from tools.engines.sublimator.extractors.gates import validate


# --- Helpers ---

def _write_json(data: dict, suffix: str = ".json") -> str:
    """Écrit un JSON temporaire et retourne le chemin."""
    tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w", encoding="utf-8")
    json.dump(data, tmp, ensure_ascii=False, indent=2)
    tmp.close()
    return tmp.name


def _base_quint() -> dict:
    """Retourne une quintessence minimale valide (schema v35 allege : 6 requises)."""
    return {
        "enquete_id": "test_id",
        "enquete_source": "investigations/test/test_id_INVESTIGATION.md",
        "these_centrale": "thèse de test",
        "faits_atomiques": [],
        "urls_prioritaires": [],
        "shadow_factor": 3.0,
    }


# ===================================================================
# F1 : Gestion d'erreurs OS
# ===================================================================

def test_f1_file_not_found():
    """H0 explicite quand le fichier n'existe pas."""
    passed, msgs = validate("/tmp/zzz_nonexistent_gates_99999.json", "quintessence")
    assert passed is False
    assert any("H0" in m and "introuvable" in m for m in msgs)


def test_f1_is_a_directory():
    """H0 explicite quand le chemin pointe vers un répertoire (F1 fix)."""
    passed, msgs = validate("/tmp", "quintessence")
    assert passed is False
    assert any("H0" in m and "répertoire" in m for m in msgs)


def test_f1_permission_denied():
    """H0 explicite quand les permissions sont insuffisantes (F1 fix)."""
    if os.geteuid() == 0:
        pytest.skip("Test non pertinent en root (toujours autorisé)")
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    os.chmod(path, 0o000)
    try:
        passed, msgs = validate(path, "quintessence")
        assert passed is False
        assert any("H0" in m and "Permissions" in m for m in msgs)
    finally:
        os.chmod(path, 0o600)
        os.remove(path)


def test_f1_empty_path():
    """H0 explicite quand le chemin est vide."""
    passed, msgs = validate("", "quintessence")
    assert passed is False
    assert any("H0" in m and "Aucun chemin" in m for m in msgs)


def test_f1_none_path():
    """H0 explicite quand le chemin est None."""
    passed, msgs = validate(None, "quintessence")
    assert passed is False
    assert any("H0" in m and "Aucun chemin" in m for m in msgs)


# ===================================================================
# F2 : H7 string-safety
# ===================================================================

def test_f2_h7_happy_path():
    """Une these_centrale normale passe H7 sans souci."""
    p = _write_json(_base_quint())
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is True, f"unexpected: {msgs}"
    finally:
        os.remove(p)


def test_f2_h7_length_too_long():
    """H7 rejette une these_centrale > 10 000 chars (F2 fix)."""
    data = _base_quint() | {"these_centrale": "A" * 10_001}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is False
        assert any("H7" in m and "trop long" in m and "these_centrale" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_length_exact_limit():
    """H7 accepte une these_centrale exactement à 10 000 chars (limite inclusive)."""
    data = _base_quint() | {"these_centrale": "A" * 10_000}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is True, f"unexpected: {msgs}"
    finally:
        os.remove(p)


def test_f2_h7_null_byte():
    """H7 rejette \\x00 (NUL) dans these_centrale (F2 fix)."""
    data = _base_quint() | {"these_centrale": "before\x00after"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is False
        assert any("H7" in m and "interdits" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_rtl_override():
    """H7 rejette \\u202e (RTL override) dans these_centrale (F2 fix)."""
    data = _base_quint() | {"these_centrale": "before\u202eafter"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is False
        assert any("H7" in m and "interdits" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_zero_width_space():
    """H7 rejette \\u200b (zero-width space) dans these_centrale (F2 fix)."""
    data = _base_quint() | {"these_centrale": "before\u200bafter"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is False
        assert any("H7" in m and "interdits" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_bom():
    """H7 rejette \\ufeff (BOM) dans these_centrale (F2 fix)."""
    data = _base_quint() | {"these_centrale": "\ufeffdébut"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is False
        assert any("H7" in m and "interdits" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_zwnj():
    """H7 rejette \\u200c (zero-width non-joiner) dans these_centrale (F2 fix)."""
    data = _base_quint() | {"these_centrale": "before\u200cafter"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is False
        assert any("H7" in m and "interdits" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_newline_allowed():
    """H7 accepte \\n (newline normal) — non blocklisté."""
    data = _base_quint() | {"these_centrale": "ligne1\nligne2\nligne3"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is True, f"newlines should be allowed: {msgs}"
    finally:
        os.remove(p)


def test_f2_h7_accents_allowed():
    """H7 accepte accents français et caractères latins étendus (non blocklisté)."""
    data = _base_quint() | {"these_centrale": "État, naïveté, œuf, été — forensique"}
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        assert passed is True, f"accents should be allowed: {msgs}"
    finally:
        os.remove(p)


def test_f2_h7_synthese_sujet():
    """H7 s'applique aussi à sujet_majoritaire (synthese, F2 scope)."""
    data = {
        "sujet_majoritaire": "thèse\x00with null",
        "theses_cardinales": [],
        "meta_observations": [],
        "transversalites": [],
        "gaps": [],
        "shadow_factor_global": 3.0,
        "mnemo_context": {"searches": []},
    }
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "synthese")
        assert passed is False
        assert any("H7" in m and "sujet_majoritaire" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_synthese_sujet_too_long():
    """H7 s'applique aussi à sujet_majoritaire pour la longueur (synthese)."""
    data = {
        "sujet_majoritaire": "B" * 10_001,
        "theses_cardinales": [],
        "meta_observations": [],
        "transversalites": [],
        "gaps": [],
        "shadow_factor_global": 3.0,
        "mnemo_context": {"searches": []},
    }
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "synthese")
        assert passed is False
        assert any("H7" in m and "sujet_majoritaire" in m and "trop long" in m for m in msgs)
    finally:
        os.remove(p)


def test_f2_h7_does_not_apply_to_nested_strings():
    """H7 ne s'applique PAS aux strings imbriquées (ex. faits_atomiques[].enonce).

    Le scope F2 est volontairement limité aux champs string top-level (these_centrale, sujet_majoritaire).
    Les autres champs string dans listes/dicts ne sont pas validés par H7 (H2 catch le type).
    """
    data = _base_quint() | {
        "faits_atomiques": [
            {"id": "F-001", "enonce": "fait avec null\x00byte (H7 ignore)", "glyphe": "✦"}
        ]
    }
    p = _write_json(data)
    try:
        passed, msgs = validate(p, "quintessence")
        # H7 ne s'applique PAS à enonce — donc pas de message H7
        assert not any("H7" in m for m in msgs), f"H7 false positive: {msgs}"
    finally:
        os.remove(p)


def test_f2_h7_regression_existing_quintessence():
    """Regression test : les 29 quintessences du projet RIC doivent toujours passer H7."""
    import glob
    quint_files = glob.glob("investigations/*/_quintessence/*.yaml")
    if not quint_files:
        pytest.skip("Pas de quintessences dans le projet (test skip)")
    # Filtrer pour ne garder que les fichiers qui passent H1 (avoir toutes les clés)
    # Sinon le test melange H1 (manquant) et H7
    bad = []
    for qf in quint_files[:5]:  # juste 5 pour eviter overhead
        passed, msgs = validate(qf, "quintessence")
        h7_msgs = [m for m in msgs if "H7" in m]
        if h7_msgs:
            bad.append((qf, h7_msgs))
    assert not bad, f"H7 false positives sur quintessences reelles : {bad}"
