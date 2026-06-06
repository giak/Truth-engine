from unittest.mock import patch, MagicMock
from tools.engines.sublimator.extractors.curator import curator_fusion, score_fiabilite, jaccard


def test_score_fiabilite_pas_url():
    assert score_fiabilite(url="", tier=None) == "❧"


def test_score_fiabilite_tier1():
    with patch("urllib.request.urlopen") as mock_open:
        mock_open.return_value.__enter__.return_value = MagicMock(status=200)
        assert score_fiabilite(url="https://wikipedia.org/x", tier=1) == "✦"


def test_score_fiabilite_tier2():
    with patch("urllib.request.urlopen") as mock_open:
        mock_open.return_value.__enter__.return_value = MagicMock(status=200)
        assert score_fiabilite(url="https://x.com/y", tier=2) == "✧"


def test_jaccard_identique():
    assert jaccard("dette annulée", "dette annulée") == 1.0


def test_jaccard_disjoint():
    assert jaccard("dette annulée", "guerre civile") == 0.0


def test_curator_fusion_deduplicate():
    candidats_a = [{"fait": "dette annulée"}, {"fait": "guerre civile"}]
    ajouts_b = [{"fait": "Dette annulée par Urukagina"}, {"fait": "clergé scribe"}]
    result = curator_fusion(candidats_a, ajouts_b, civ_prefix="S")
    assert len(result) >= 3
    # Vérifier que scoring est appliqué
    assert all("fiabilite" in r for r in result)
