"""Tests pour gates.py — 7 checks H0-H6 (Sublimator v34 Léger)."""

import pytest
import yaml
import tempfile
from pathlib import Path
from tools.engines.sublimator.extractors.gates import validate


def _write_yaml(data: dict) -> str:
    """Écrit un YAML temporaire et retourne le chemin."""
    tmp = tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w")
    yaml.dump(data, tmp)
    tmp.close()
    return tmp.name


def _base_quintessence() -> dict:
    """Retourne une quintessence minimale valide pour les tests (schema v35 allege)."""
    # v35 (2026-07-05) : 6 REQUISES + 6 optionnelles. Le helper inclut les 6 requises + 0 optionnelles.
    return {
        "enquete_id": "test_id",
        "enquete_source": "investigations/test/test_id_INVESTIGATION.md",
        "these_centrale": "une thèse de test",
        "faits_atomiques": [],
        "urls_prioritaires": [],
        "shadow_factor": 3.0,
    }


def _base_quintessence_v34_legacy() -> dict:
    """Helper retro-compat : quintessence avec l'ancien schema 12 cles v34 (incomplet pour v35)."""
    keys = [
        "these_centrale", "theses_implicites", "faits_atomiques",
        "acteurs", "causalites", "perspectives_dialectiques",
        "limites", "wolves", "iceberg", "chronologie",
        "domaines", "urls_prioritaires",
    ]
    data = {k: [] for k in keys}
    data["these_centrale"] = "une these de test"
    return data


# --- H0: YAML parsable ---

def test_h0_yaml_valide():
    path = _write_yaml({"these_centrale": "test"})
    passed, msgs = validate(path, "quintessence")
    assert passed is False  # manque d'autres clés, mais H0 passe
    assert not any("H0" in m for m in msgs)


def test_h0_fichier_introuvable():
    passed, msgs = validate("/tmp/nexiste_pas_12345.yaml", "quintessence")
    assert passed is False
    assert any("H0" in m for m in msgs)


def test_h0_yaml_invalide():
    tmp = tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w")
    tmp.write("ceci n'est pas: du: yaml: valide: [")
    tmp.close()
    passed, msgs = validate(tmp.name, "quintessence")
    assert passed is False
    assert any("H0" in m for m in msgs)


# --- H1: clés obligatoires ---

def test_h1_quintessence_complete():
    data = _base_quintessence()
    data["these_centrale"] = "une these"
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Echecs: {msgs}"


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
    path = _write_yaml(data)
    passed, msgs = validate(path, "synthese")
    assert passed is True


def test_h1_cles_manquantes():
    data = {"these_centrale": "seule clé"}
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H1" in m for m in msgs)


# --- H2: types valides ---

def test_h2_type_invalide():
    data = _base_quintessence()
    data["these_centrale"] = 42  # devrait etre str
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H2" in m for m in msgs)


# --- H3: glyphes valides ---

def test_h3_glyphe_valide():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001", "glyphe": "✦"}]
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True

def test_h3_glyphe_invalide():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001", "glyphe": "X"}]
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H3" in m for m in msgs)


# --- H4: IDs uniques ---

def test_h4_ids_uniques():
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001", "glyphe": "✦"}, {"id": "F-002", "glyphe": "✧"}]
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Échecs: {msgs}"

def test_h4_fait_duplique():
    data = _base_quintessence()
    data["faits_atomiques"] = [
        {"id": "F-001"}, {"id": "F-001"}
    ]
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H4" in m for m in msgs)


# --- H5: thèse ≥ 3 F## ---

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
    path = _write_yaml(data)
    passed, msgs = validate(path, "synthese")
    assert passed is False
    assert any("H5" in m for m in msgs)


# --- H6: coherence inter-sections (quintessence uniquement) ---

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
    path = _write_yaml(data)
    passed, msgs = validate(path, "synthese")
    assert passed is True, f"Échecs inattendus: {msgs}"


def test_h6_reference_orpheline_quintessence():
    """H6 attrape un F## reference dans transversalites mais absent de faits_atomiques."""
    data = _base_quintessence()
    data["faits_atomiques"] = [{"id": "F-001"}]
    data["transversalites"] = [
        {"concept": "test", "faits_communs": ["F-999"]}
    ]
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is False
    assert any("H6" in m for m in msgs)


# --- Test d'intégration: YAML complet valide passe tous les checks ---

def test_integration_quintessence_valide():
    data = _base_quintessence()
    data["these_centrale"] = "Une these centrale plausible"
    data["faits_atomiques"] = [
        {"id": "F-001", "glyphe": "✦"},
        {"id": "F-002", "glyphe": "✧"},
        {"id": "F-003", "glyphe": "❧"},
    ]
    path = _write_yaml(data)
    passed, msgs = validate(path, "quintessence")
    assert passed is True, f"Echecs: {msgs}"
