"""Tests parallèles pour gates.py : 7 checks H0-H6 en mode JSON.

Mirror de `test_gates.py` (ciblant YAML legacy) mais pour le format `.json`,
qui devient le format par défaut depuis 2026-07-05.

Validations testées :
- H0 : fichier .json parsable
- H1 : 12 clés quintessence OU 8 clés synthese
- H2 : types valides
- H3 : 4 glyphes acceptés (✦ / ✧ / ⁅ / ❧)
- H4 : IDs uniques
- H5 : theses_cardinales avec ≥ 3 F## justificatifs
- H6 : cohérence inter-sections (F## référencés existent dans faits_atomiques)
"""

import json
import tempfile
import pytest

from tools.engines.sublimator.extractors.gates import validate


def _write_json(data: dict) -> str:
    """Écrit un JSON temporaire (UTF-8, indent=2) et retourne le chemin."""
    tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w", encoding="utf-8")
    json.dump(data, tmp, ensure_ascii=False, indent=2)
    tmp.close()
    return tmp.name


def _base_quintessence() -> dict:
    """Retourne une quintessence JSON minimale valide pour les tests (schema v35 allege)."""
    # v35 (2026-07-05) : 6 REQUISES + 6 optionnelles.
    return {
        "enquete_id": "test_id",
        "enquete_source": "investigations/test/test_id_INVESTIGATION.md",
        "these_centrale": "une these de test",
        "faits_atomiques": [],
        "urls_prioritaires": [],
        "shadow_factor": 3.0,
    }


# --- H0 : JSON parsable ---

def test_h0_json_valide():
    path = _write_json({"these_centrale": "test"})
    passed, msgs = validate(path, "quintessence")
    assert passed is False  # manque d'autres clés, mais H0 passe
    assert not any("H0" in m for m in msgs)


def test_h0_fichier_introuvable():
    passed, msgs = validate("/tmp/nexiste_pas_12345.json", "quintessence")
    assert passed is False
    assert any("H0" in m for m in msgs)


def test_h0_json_invalide():
    tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w", encoding="utf-8")
    tmp.write("{ceci n'est pas du json valide}")
    tmp.close()
    passed, msgs = validate(tmp.name, "quintessence")
    assert passed is False
    assert any("H0" in m for m in msgs)


# --- H1 : 12 ou 8 clés obligatoires ---

def test_h1_quintessence_complete():
    data = _base_quintessence()
    data["these_centrale"] = "une these"
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Échecs: {msgs}"


def test_h1_synthese_complete():
    data = {
        "sujet_majoritaire": "test",
        "theses_cardinales": [],
        "meta_observations": [],
        "transversalites": [],
        "gaps": [],
        "shadow_factor_global": 3.0,
        "mnemo_context": {"searches": []},
    }
    path = _write_json(data)
    passed, msgs = validate(path, "synthese")
    assert passed is True, f"Échecs: {msgs}"


def test_h1_cles_manquantes():
    data = {"these_centrale": "seule cle"}
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H1" in m for m in msgs)


# --- H2 : types valides ---

def test_h2_type_invalide():
    data = _base_quintessence()
    data["these_centrale"] = 42  # devrait être str
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H2" in m for m in msgs)


# --- H3 : 4 glyphes valides ---

def test_h3_glyphe_valide():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001", "glyphe": "✦"}]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Échecs: {msgs}"


def test_h3_glyphes_quatre_acceptes():
    """Les 4 glyphes canoniques sont tous acceptes (tier 1+200 / tier 2+200 / casse / sans URL)."""
    data = _base_quintessence()
    data["faits_atomiques"] = [
        {"id": "F-001", "glyphe": "✦"},
        {"id": "F-002", "glyphe": "✧"},
        {"id": "F-003", "glyphe": "⁅"},
        {"id": "F-004", "glyphe": "❧"},
    ]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Échecs: {msgs}"


def test_h3_glyphe_invalide():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001", "glyphe": "X"}]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H3" in m for m in msgs)


# --- H4 : IDs uniques ---

def test_h4_ids_uniques():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001", "glyphe": "✦"}, {"id": "F-002", "glyphe": "✧"}]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Échecs: {msgs}"


def test_h4_fait_duplique():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001"}, {"id": "F-001"}]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H4" in m for m in msgs)


# --- H5 : these >= 3 F## justificatifs ---

def test_h5_these_sous_referencee():
    data = {
        "sujet_majoritaire": "test",
        "theses_cardinales": [{"titre": "T1", "f_atomiques_justificatifs": ["F-001"]}],
        "meta_observations": [],
        "transversalites": [],
        "gaps": [],
        "shadow_factor_global": 3.0,
        "mnemo_context": {"searches": []},
    }
    path = _write_json(data)
    passed, msgs = validate(path, "synthese")
    assert passed is False
    assert any("H5" in m for m in msgs)


# --- H6 : coherence inter-sections (quintessence uniquement) ---

def test_h6_noop_synthese():
    """H6 ne s'applique pas a la synthese (pas de faits_atomiques)."""
    data = {
        "sujet_majoritaire": "test",
        "theses_cardinales": [{"titre": "T1", "f_atomiques_justificatifs": ["F-001", "F-002", "F-003"]}],
        "transversalites": [],
        "meta_observations": [],
        "gaps": [],
        "shadow_factor_global": 3.0,
        "mnemo_context": {"searches": []},
    }
    path = _write_json(data)
    passed, msgs = validate(path, "synthese")
    assert passed is True, f"Échecs: {msgs}"


def test_h6_reference_orpheline_quintessence():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001"}]
    data["transversalites"] = [{"concept": "test", "faits_communs": ["F-999"]}]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H6" in m for m in msgs)


# --- Integration : quintessence JSON complet valide passe tous les checks ---

def test_integration_quintessence_valide():
    data = _base_quintessence()
    data["these_centrale"] = "Une these centrale plausible"
    data["faits_atomiques"] = [
        {"id": "F-001", "glyphe": "✦", "enonce": "Fait 1"},
        {"id": "F-002", "glyphe": "✧", "enonce": "Fait 2"},
        {"id": "F-003", "glyphe": "❧", "enonce": "Fait 3"},
    ]
    path = _write_json(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Echecs: {msgs}"


# --- Backward compat : YAML legacy lu en fallback ---

def test_backward_yaml_via_validate():
    """Verify the dual-reader: a .yaml file is still read correctly via validate().

    Note v35 : YAML legacy doit toujours etre lisible, mais le schema exige 6 requises.
    Le helper _base_quintessence() inclut deja les 6 requises.
    """
    import yaml
    tmp = tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8")
    data = _base_quintessence()
    data["these_centrale"] = "these yaml legacy"
    yaml.dump(data, tmp, allow_unicode=True)
    tmp.close()
    passed, msgs = validate(tmp.name, "quintessence")
    assert passed is True, f"YAML legacy doit rester valide : {msgs}"
