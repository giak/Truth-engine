from tools.engines.sublimator.extractors.extract_utile import (
    extract_dates, extract_sommes, extract_citations, extract_urls,
    extract_acteurs_nommes, extract_marqueurs_causalite, extract_marqueurs_rhetorique,
    extract_sections_plan, extract_utile_all,
)


def test_extract_dates_iso():
    text = "Le 2024-01-15 fut un jour important."
    dates = extract_dates(text)
    iso_dates = [d for d in dates if d["format"] == "ISO"]
    assert len(iso_dates) == 1
    assert iso_dates[0]["date"] == "2024-01-15"


def test_extract_dates_siecle():
    text = "Au XXe siècle, la France a changé."
    dates = extract_dates(text)
    siecle = [d for d in dates if d["format"] == "SIECLE"]
    assert len(siecle) == 1
    assert "XXe" in siecle[0]["date"]


def test_extract_sommes_milliards():
    text = "La dette atteint 3 416,3 milliards d'euros."
    sommes = extract_sommes(text)
    assert any("3 416" in s["montant"] and s["format"] == "Mds" for s in sommes)


def test_extract_sommes_pct():
    text = "PIB en hausse de 2,5% sur 2024."
    sommes = extract_sommes(text)
    assert any("2,5" in s["montant"] and s["format"] == "pct" for s in sommes)


def test_extract_citations_francaises():
    text = 'Il a dit « la dette est un outil de contrôle » en 2024.'
    cits = extract_citations(text)
    assert len(cits) == 1
    assert "dette" in cits[0]["citation"]


def test_extract_urls():
    text = "Voir https://fr.wikipedia.org/wiki/Sumer pour details."
    urls = extract_urls(text)
    assert len(urls) == 1
    assert "wikipedia.org" in urls[0]["url"]


def test_extract_acteurs_nommes_heuristique():
    text = "Le roi Urukagina de Lagas et le roi Hammurabi de Babylone ont réformé."
    acteurs = extract_acteurs_nommes(text)
    noms = {a["nom"] for a in acteurs}
    assert any("Urukagina" in n for n in noms)
    assert any("Hammurabi" in n for n in noms)


def test_extract_marqueurs_causalite():
    text = "Le roi est mort parce que la guerre a duré."
    marqueurs = extract_marqueurs_causalite(text)
    assert any("parce que" in m["marqueur"] for m in marqueurs)


def test_extract_marqueurs_rhetorique():
    text = "DEM_AGGRESSIVE et BF_FALLACIES sont des patterns."
    marqueurs = extract_marqueurs_rhetorique(text)
    types = {m["type"] for m in marqueurs}
    assert "DEM" in types
    assert "BF" in types


def test_extract_sections_plan_18():
    sections = []
    for i in range(1, 19):
        sections.append(f"## §{i} SECTION TITRE COURT")
    text = "\n\n".join(sections)
    results = extract_sections_plan(text)
    assert len(results) == 18
    nums = {r["section_num"] for r in results}
    assert nums == set(range(1, 19))


def test_extract_utile_all_keys():
    text = '## §1 RÉSUMÉ\nLe 2024-01-15 Urukagina dit « la dette est un outil de contrôle des peuples » sur 100 milliards.'
    result = extract_utile_all(text)
    assert set(result.keys()) == {
        "dates", "sommes", "citations", "urls",
        "acteurs_nommes", "marqueurs_causalite",
        "marqueurs_rhetorique", "sections_plan",
    }
    assert len(result["dates"]) >= 1
    assert len(result["sommes"]) >= 1
    assert len(result["citations"]) >= 1
    assert len(result["sections_plan"]) >= 1
