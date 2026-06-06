from unittest.mock import patch
from tools.engines.sublimator.extractors.llm_verifier import verifier


@patch("tools.engines.sublimator.extractors.llm_verifier.call_llm")
def test_verifier_signale_trous(mock_llm):
    mock_llm.return_value = """{
      "f001_manquants": ["fait sur Urukagina non listé"],
      "incoherences": [],
      "acteurs_oublies": ["Hammurabi"],
      "fausses_urls": [],
      "iceberg_sous_exploite": ["fausse attribution dette sumérienne"]
    }"""
    matrice = [{"id": "F-S001", "fait": "dette annulée"}]
    text = "Urukagina et Hammurabi ont annulé les dettes."
    result = verifier(matrice, text)
    assert "Hammurabi" in result["acteurs_oublies"]
    assert len(result["f001_manquants"]) == 1


@patch("tools.engines.sublimator.extractors.llm_verifier.call_llm")
def test_verifier_truncates_text(mock_llm):
    mock_llm.return_value = '{"f001_manquants": [], "incoherences": [], "acteurs_oublies": [], "fausses_urls": [], "iceberg_sous_exploite": []}'
    long_text = "x" * 50000
    verifier([], long_text)
    args, _ = mock_llm.call_args
    assert len(args[0]) < 35000
