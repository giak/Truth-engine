#!/usr/bin/env python3
"""detect_contradictions.py — Détecteur de contradictions du registre des faits (P5).

Compare les faits des blocs FACT_REGISTRY_V1 par leur champ optionnel `sujet` :
même `sujet` normalisé + `valeur` différente = contradiction potentielle, à arbitrer
par la gate humaine. Le script SIGNALE, il ne tranche pas (il ne sait pas quelle
valeur est vraie). Il détecte aussi les collisions d'id (même FCT-### avec contenu
divergent : duplication ou réécriture non tracée).

Limite honnête (assumée, pas masquée) : `sujet` est un slug rempli par l'LLM. Si le
slug est incohérent (« dgsi-effectif » vs « effectif-dgsi »), la contradiction est
invisible au script. Ce filet attrape les contradictions déjà sluggées de façon
cohérente ; l'exhaustivité sémantique reste du ressort de la gate humaine.

Sortie : rapport texte (ou --json) + code retour :
  0 = aucune contradiction
  1 = au moins une contradiction / collision
  2 = aucun registre trouvé

Usage :
  python3 tools/detect_contradictions.py [chemin...] [--json]
  Sans chemin : scanne `investigations/` récursivement.
"""

import argparse
import json
import os
import sys

# Exécution directe (python3 tools/detect_contradictions.py) : rendre `tools` importable.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.verify_facts import (
    extract_registry,
    find_registry_files,
    parse_line,
)


def normalize(s):
    """Normalise un slug/valeur : minuscules, séparateurs non-alphanum → '-', collapse."""
    out = []
    prev_dash = False
    for ch in (s or "").strip().lower():
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif not prev_dash:
            out.append("-")
            prev_dash = True
    return "".join(out).strip("-")


def _clean_valeur(v):
    """Valeur comparable, ou None si vide/placeholder (« - »)."""
    n = normalize(v)
    return n if n else None


def scan(paths):
    """(files, records). records = liste de dicts {file, fid, sujet, valeur}."""
    files = find_registry_files(paths)
    records = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            text = fh.read()
        for ln in extract_registry(text):
            rec = parse_line(ln)
            if rec is None:
                continue
            fid, _epi, _tier, _url, _fam, _date, sujet, valeur = rec
            records.append({
                "file": f,
                "fid": fid,
                "sujet": (sujet or "").strip(),
                "valeur": (valeur or "").strip(),
            })
    return files, records


def detect(records):
    """(contradictions, collisions_id)."""
    by_sujet = {}
    for r in records:
        s = normalize(r["sujet"])
        if not s:
            continue  # pas de sujet : hors périmètre
        by_sujet.setdefault(s, []).append(r)

    contradictions = []
    for s, recs in by_sujet.items():
        valeurs = {_clean_valeur(r["valeur"]) for r in recs}
        valeurs.discard(None)
        if len(valeurs) > 1:
            contradictions.append({
                "sujet": s,
                "valeurs": sorted(valeurs),
                "faits": sorted(
                    (r["fid"], r["valeur"], r["file"]) for r in recs
                ),
            })

    by_id = {}
    for r in records:
        by_id.setdefault(r["fid"], []).append(r)

    collisions = []
    for fid, recs in by_id.items():
        keys = {(normalize(r["sujet"]), _clean_valeur(r["valeur"])) for r in recs}
        if len(keys) > 1:
            collisions.append({
                "fid": fid,
                "faits": sorted(
                    (r["sujet"], r["valeur"], r["file"]) for r in recs
                ),
            })

    return contradictions, collisions


def report_text(files, records, contradictions, collisions):
    if not records:
        print("AUCUN REGISTRE TROUVÉ.")
        return 2
    print("DÉTECTEUR DE CONTRADICTIONS — registre des faits (P5)")
    print("=" * 60)
    n = 0
    for c in contradictions:
        n += 1
        print("CONTRADICTION {0} : sujet « {1} » avec valeurs divergentes {2}".format(
            n, c["sujet"], " / ".join("« {0} »".format(v) for v in c["valeurs"])))
        for fid, val, f in c["faits"]:
            print("   {0} = « {1} »  ({2})".format(fid, val, os.path.basename(f)))
    for c in collisions:
        n += 1
        print("COLLISION ID {0} : {1} (contenu divergent)".format(n, c["fid"]))
        for sujet, val, f in c["faits"]:
            print("   sujet=« {0} » valeur=« {1} »  ({2})".format(
                sujet, val, os.path.basename(f)))
    print("-" * 60)
    n_sujet = sum(1 for r in records if normalize(r["sujet"]))
    print("{0} signal(s) sur {1} fait(s) avec sujet, {2} fichier(s).".format(
        n, n_sujet, len(files)))
    return 1 if (contradictions or collisions) else 0


def report_json(files, records, contradictions, collisions):
    payload = {
        "files": files,
        "contradictions": len(contradictions),
        "collisions": len(collisions),
        "entries": [
            {"type": "contradiction", "sujet": c["sujet"], "valeurs": c["valeurs"],
             "faits": [{"fid": fid, "valeur": v, "file": f} for fid, v, f in c["faits"]]}
            for c in contradictions
        ] + [
            {"type": "collision_id", "fid": c["fid"],
             "faits": [{"sujet": s, "valeur": v, "file": f} for s, v, f in c["faits"]]}
            for c in collisions
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if (contradictions or collisions) else 0


def main(argv):
    ap = argparse.ArgumentParser(description="Détecteur de contradictions du registre.")
    ap.add_argument("paths", nargs="*", default=["investigations/"],
                    help="Fichiers ou dossiers à scanner (défaut : investigations/)")
    ap.add_argument("--json", action="store_true", help="Sortie machine-readable")
    args = ap.parse_args(argv)
    files, records = scan(args.paths)
    contradictions, collisions = detect(records)
    if args.json:
        return report_json(files, records, contradictions, collisions)
    return report_text(files, records, contradictions, collisions)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
