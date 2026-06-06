import json
from pathlib import Path
from tools.engines.sublimator.extractors.parse_atomic import parse_all
from tools.engines.sublimator.extractors.extract_utile import extract_utile_all


def main():
    src = Path("investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md")
    text = src.read_text()
    print(f"Source : {src}")
    print(f"Taille : {len(text):,} chars / {len(text.splitlines()):,} lignes\n")

    print("=" * 70)
    print("AGENT A — Parseur (Python pur, regex)")
    print("=" * 70)
    candidats = parse_all(text, civ_prefix="S")
    print(f"  F### candidats : {len(candidats)}")
    if candidats:
        print(f"  Premier : {candidats[0]}")
        print(f"  Dernier : {candidats[-1]}")
    formats = {}
    for c in candidats:
        formats[c["input_format"]] = formats.get(c["input_format"], 0) + 1
    print(f"  Répartition par format : {formats}\n")

    print("=" * 70)
    print("AGENT A++ — Extraction article-utile (Python pur, regex étendu)")
    print("=" * 70)
    utile = extract_utile_all(text)
    for key, items in utile.items():
        print(f"  {key:25s} : {len(items):3d}")
    print()

    if utile["dates"]:
        print("  Exemples dates :")
        for d in utile["dates"][:3]:
            print(f"    - {d['date']} ({d['format']}) L{d['line_no']}")
    print()

    if utile["sommes"]:
        print("  Exemples sommes :")
        for s in utile["sommes"][:5]:
            print(f"    - {s['montant']} ({s['format']}) L{s['line_no']}")
    print()

    if utile["citations"]:
        print(f"  Première citation (sur {len(utile['citations'])}):")
        print(f"    « {utile['citations'][0]['citation'][:120]}... »")
        print(f"    L{utile['citations'][0]['line_no']}")
    print()

    if utile["acteurs_nommes"]:
        print(f"  Acteurs nommés (5 premiers sur {len(utile['acteurs_nommes'])}):")
        for a in utile["acteurs_nommes"][:5]:
            print(f"    - {a['nom']} L{a['line_no']}")
    print()

    if utile["urls"]:
        print(f"  URLs (3 premières sur {len(utile['urls'])}):")
        for u in utile["urls"][:3]:
            print(f"    - {u['url']} L{u['line_no']}")
    print()

    if utile["sections_plan"]:
        print(f"  Sections du plan SUBLIMATOR (toutes sur {len(utile['sections_plan'])}):")
        for s in utile["sections_plan"][:10]:
            print(f"    - §{s['section_num']} {s['section_titre']} L{s['section_no'] if 'section_no' in s else s['line_no']}")
        if len(utile["sections_plan"]) > 10:
            print(f"    ... et {len(utile['sections_plan']) - 10} autres")
    print()

    out = Path("/tmp/sumer_extraction_utile.json")
    out.write_text(json.dumps({
        "f_candidats": candidats,
        "utile": {k: v for k, v in utile.items()},
        "stats": {
            "n_f_candidats": len(candidats),
            "n_dates": len(utile["dates"]),
            "n_sommes": len(utile["sommes"]),
            "n_citations": len(utile["citations"]),
            "n_urls": len(utile["urls"]),
            "n_acteurs": len(utile["acteurs_nommes"]),
            "n_marqueurs_causalite": len(utile["marqueurs_causalite"]),
            "n_marqueurs_rhetorique": len(utile["marqueurs_rhetorique"]),
            "n_sections_plan": len(utile["sections_plan"]),
        }
    }, indent=2, ensure_ascii=False))
    print(f"Output complet : {out}")


if __name__ == "__main__":
    main()
