"""P2 — Corpus doré : l'échelle L0→L4 ancrée sur les erreurs réelles de la session.

Ce test verrouille DEUX choses, et les deux sont importantes :

1. **Les gates structurelles attrapent les signatures** des erreurs réelles qui ont
   traversé le pipeline (date plausible fausse, off-by-one, cible-vs-réel). Chaque
   erreur est ancrée sur son cas historique (Squarcini, DGSI, CNIL, art. 89, QPC...).

2. **La frontière honnête** : le vérificateur déterministe ne peut PAS détecter les
   erreurs de CONTENU (date fausse mais plausible, mauvaise cible d'attribution,
   confusion de catégories, arithmétique). Ces erreurs passent structurellement et
   doivent être arrêtées par la gate HUMAINE (relecture de l'extrait fetché, L4).
   Les tests `content_only_*` verrouillent ce non-sur-capture : ils exigent que le
   vérificateur ne PRÉTENDE PAS attraper ce qu'il ne peut pas voir.

Principe (AGENTS.md §4) : le script vérifie la STRUCTURE, jamais la VÉRITÉ.

Mapping des 6 classes d'erreur réelles → signature → couche de détection :

| Erreur réelle (session)                     | Signature structurelle              | Couche qui l'arrête |
|---------------------------------------------|-------------------------------------|---------------------|
| Squarcini DST « 2002-2007 » (fausse)        | ✦ auto-attribué, 1 famille          | ≥2 familles (script)|
| CNIL « 19 déc » → 5 déc (off-by-one)        | 1 source primaire, ✦               | ≥2 familles (script)|
| art. 89 « al. 4 » → al. 5 (off-by-one)      | 1 source (Légifrance)               | ≥2 familles (script)|
| DGSI « 5 500 » cible présentée comme réalisé| EPI=INFERENCE (plan) marqué FACT    | gate EPI (script)   |
| QPC a censuré « X » au lieu de « Y »        | aucune (structure saine)            | gate HUMAINE        |
| interceptions « judiciaires » vs « sécurité »| aucune (structure saine)            | gate HUMAINE        |
| 237 vs 226 (arithmétique)                    | aucune (structure saine)            | gate HUMAINE        |

La leçon : les erreurs de contenu n'ont été possibles QUE parce que le ✦ était
auto-attribué sans ≥2 familles indépendantes. Les gates structurelles ferment cette
porte d'entrée. Le jugement de vérité reste, lui, humain.
"""

import pytest

from tools.verify_facts import verify_record


def _rec(fid="FCT-001", epi="FACT", tier="✦", url="https://legifrance.gouv.fr/x",
         families="A,E", date="2024-03-07"):
    return (fid, epi, tier, url, families, date)


@pytest.fixture
def live(monkeypatch):
    """Toute URL répond 200 : on ne teste que les gates structurelles (hors réseau)."""
    monkeypatch.setattr("tools.verify_facts.head_check", lambda u, timeout=5: 200)


# --- 1. Signatures structurelles des erreurs réelles (détectables) ---

def test_squarcini_date_fausse_une_famille(live):
    # ✦ auto-attribué sur 1 famille : la « corroboration » était des copies internes.
    issues = verify_record(_rec(families="D"))
    assert any("<2" in i for i in issues)


def test_cnil_off_by_one_une_famille(live):
    issues = verify_record(_rec(families="A"))
    assert any("<2" in i for i in issues)


def test_article_89_off_by_one_une_famille(live):
    issues = verify_record(_rec(families="E"))
    assert any("<2" in i for i in issues)


def test_dgsi_cible_presentee_comme_effectif_epi(live):
    # « 5 500 agents » = objectif (plan), pas un effectif réalisé : INFERENCE, pas FACT.
    issues = verify_record(_rec(epi="INFERENCE"))
    assert any("EPI" in i for i in issues)


def test_fait_bien_source_deux_familles_passe(live):
    assert verify_record(_rec()) == []


# --- 2. Frontière honnête : erreurs de contenu NON détectables ---

@pytest.mark.parametrize("name,rec", [
    ("QPC cible d'attribution fausse (structure saine)",
     _rec(url="https://conseil-constitutionnel.fr/decision/2017-680", families="A,E")),
    ("interceptions judiciaires vs sécurité (structure saine)",
     _rec(url="https://legifrance.gouv.fr/loda/id/x", families="B,C")),
    ("237 vs 226 arithmétique (structure saine)",
     _rec(url="https://senat.fr/rapport/139", families="A,D")),
])
def test_content_only_non_detectable(name, rec, live):
    # Le vérificateur ne doit PAS lever de violation : ces erreurs relèvent de la
    # gate humaine (relecture de l'extrait fetché). On verrouille le non-sur-capture.
    assert verify_record(rec) == [], name


# --- 3. Format de date (attrape le malformé, pas le plausible-faux) ---

@pytest.mark.parametrize("date", ["2024-03-07", ""])
def test_date_valide(date, live):
    assert verify_record(_rec(date=date)) == []


def test_date_malformee(live):
    issues = verify_record(_rec(date="5 décembre 2023"))
    assert any("date invalide" in i for i in issues)
