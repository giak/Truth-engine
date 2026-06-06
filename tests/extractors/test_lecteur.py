from unittest.mock import patch
from tools.engines.sublimator.extractors.llm_lecteur import lecteur_cursif


@patch("tools.engines.sublimator.extractors.llm_lecteur.call_llm")
def test_lecteur_cursif_returns_11_sections(mock_llm):
    mock_llm.return_value = """{
      "these_centrale": "Test these",
      "theses_implicites": ["t1", "t2", "t3"],
      "acteurs": ["Urukagina", "Hammurabi"],
      "causalites": [{"liens": ["A", "B", "C"]}],
      "perspectives_dialectiques": {"auteur": "...", "adverse": "...", "arbitre": "..."},
      "limites": ["l1", "l2"],
      "wolves": ["w1", "w2"],
      "iceberg": ["i1", "i2"],
      "chronologie": [{"date": "2400 av. J.-C.", "fait": "Urukagina"}],
      "domaines": ["dette", "droit"],
      "urls_prioritaires": ["https://..."]
    }"""
    text = "# §1 RÉSUMÉ\nContenu enquête..."
    result = lecteur_cursif(text, civ_prefix="S")
    assert result["these_centrale"] == "Test these"
    assert len(result["theses_implicites"]) == 3
    assert len(result["acteurs"]) == 2
    mock_llm.assert_called_once()


@patch("tools.engines.sublimator.extractors.llm_lecteur.call_llm")
def test_lecteur_cursif_truncates_text(mock_llm):
    mock_llm.return_value = '{"these_centrale": "x", "theses_implicites": [], "acteurs": [], "causalites": [], "perspectives_dialectiques": {}, "limites": [], "wolves": [], "iceberg": [], "chronologie": [], "domaines": [], "urls_prioritaires": []}'
    long_text = "x" * 100000
    lecteur_cursif(long_text, civ_prefix="S")
    args, _ = mock_llm.call_args
    assert len(args[0]) < 60000  # tronqué à 50K
