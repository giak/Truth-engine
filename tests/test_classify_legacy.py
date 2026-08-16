"""Tests du mapper déterministe legacy livre-cst -> FACT_VERIFICATION (§11)."""

import json

from tools.classify_legacy import classify, map_family, map_status

SAMPLE = """# A27-C02

**Article** : A27
**Chapitre** : C5
**Assertion** : Le taux de pauvreté est au plus haut depuis 1996.
**Statut canonique** : C1 — Confirmé
**Source** : https://www.insee.fr/fr/statistiques/8600989
**Classe source** : S3 — Primaire / officielle
**Cluster** : CG0235
**Notes** : -
"""


def test_map_status_c1_is_candidate_not_confirmed():
    verdict, status_tag, epi, action = map_status("C1 — Confirmé")
    assert verdict == "CANDIDAT"
    assert status_tag is None  # jamais status:CONFIRME
    assert "re-fetch" in action


def test_map_status_c5_is_refute():
    verdict, status_tag, epi, action = map_status("C5 — Faux / invalide")
    assert verdict == "REFUTE"
    assert status_tag == "REFUTE"
    assert epi == "FACT"


def test_map_status_typo_c1_confirme():
    verdict, _, _, _ = map_status("C1 — Confirme")
    assert verdict == "CANDIDAT"


def test_map_status_web_and_enfance_are_candidates():
    for s in ("WEB", "WEB — Source externe à arbitrer", "ENFANCE P0 — Lien causal à arbitrer", "LOOP — Lien causal à arbitrer"):
        verdict, status_tag, _, _ = map_status(s)
        assert verdict == "CANDIDAT"
        assert status_tag is None


def test_map_status_c3_c4_c6():
    assert map_status("C3 — Plausible / à tester")[2] == "HYPOTHESIS"
    assert map_status("C4 — Non établi / preuve insuffisante")[2] == "UNKNOWN"
    assert map_status("C6 — Bloqué / source absente")[2] == "UNKNOWN"


def test_map_status_unknown():
    verdict, _, epi, _ = map_status("ZZZ — truc")
    assert verdict == "UNKNOWN"
    assert epi == "UNKNOWN"


def test_map_family():
    assert map_family("S0 — Absente") is None
    assert map_family("S1 — Interne / registre") == "INTERNE"
    assert map_family("S2 — Externe secondaire") == "SECONDAIRE"
    assert map_family("S3 — Primaire / officielle") == "A"
    assert map_family("S3 — Rapport public — Cour des comptes") == "A"


def test_classify_full_sample():
    rec = classify(SAMPLE)
    assert rec["claim_id"] == "A27-C02"
    assert rec["verdict"] == "CANDIDAT"
    assert rec["status_tag"] is None  # la clé : C1 ≠ CONFIRME
    assert rec["famille"] == "A"
    assert rec["claimed_source"].startswith("https://www.insee.fr")


def test_classify_c5_with_s0():
    content = "**Statut canonique** : C5 — Faux / invalide  \n**Classe source** : S0 — Absente  \n"
    rec = classify(content)
    assert rec["verdict"] == "REFUTE"
    assert rec["status_tag"] == "REFUTE"
    assert rec["famille"] is None


def test_classify_empty_returns_unknown():
    rec = classify("")
    assert rec["legacy_status"] is None
    assert rec["verdict"] == "UNKNOWN"


def test_json_serializable():
    rec = classify(SAMPLE)
    json.dumps(rec)  # ne doit pas lever
