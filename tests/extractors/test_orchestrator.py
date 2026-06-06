from unittest.mock import patch
from tools.engines.sublimator.extractors.orchestrator import run_cellule


@patch("tools.engines.sublimator.extractors.orchestrator.lecteur_cursif")
@patch("tools.engines.sublimator.extractors.orchestrator.verifier")
def test_run_cellule_sumer(mock_verifier, mock_lecteur):
    mock_lecteur.return_value = {
        "these_centrale": "Test", "theses_implicites": ["t1"],
        "acteurs": ["Urukagina"], "causalites": [],
        "perspectives_dialectiques": {}, "limites": [], "wolves": [],
        "iceberg": [], "chronologie": [], "domaines": [], "urls_prioritaires": [],
        "ajouts": [],
    }
    mock_verifier.return_value = {
        "f001_manquants": [], "incoherences": [],
        "acteurs_oublies": [], "fausses_urls": [], "iceberg_sous_exploite": [],
    }

    result = run_cellule(
        input_path="investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md",
        civ_prefix="S",
        output_path="/tmp/sumer_test.yaml",
        complexity="APEX",
    )
    assert "exit_code" in result
    assert "matrice" in result
    assert "score" in result
