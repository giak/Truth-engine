#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script 02 du pilote avenants SESN : normalisation SIREN/SIRET (Phase 2).

Entree : data/decp_sesn_dedup.csv (45 lignes, cumul deduplique 103 578 507,98 EUR).
Sorties :
- data/decp_sesn_norm.csv : lignes + colonnes normalisees
- data/decp_sesn_norm.csv.sha256
- data/titulaires_rne.csv : rapprochement RNE/API recherche-entreprises par SIREN
- data/siren_non_resolus.csv : SIREN non resolus (echec API, SIRET invalide)

Normalisation (regle anti-fausse-precision : deterministe pur, AUCUN LLM) :
1. SIRET titulaires : suppression espaces/points, garde 14 chiffres,
   cles de Luhn (SIRET 14 chiffres puis SIREN 9 chiffres).
2. Dedoublonnage par cle (id, acheteur_id, source) ; pour les id degrades
   (id = '000'...) la cle est (id, objet_normalise, acheteur_id, source)
   car plusieurs marches distincts partagent l'id degrade. JAMAIS par
   (SIREN, objet, montant) qui fusionnerait des lots distincts.
3. Rapprochement des titulaires par SIREN via API recherche-entreprises
   (api.gouv.fr) pour completer les noms manquants (colonne titulaires_nom
   est vide dans la source) et verifier l'existence des SIREN.

Usage : python3 scripts/02_normalize_siren.py [--api]  (--api : appelle l'API,
sans : mode hors-ligne, colonnes rne_statut = NON_TENTE)
"""

import argparse
import csv
import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

SRC = "data/decp_sesn_dedup.csv"
DST = "data/decp_sesn_norm.csv"
DST_RNE = "data/titulaires_rne.csv"
DST_NON_RESOLUS = "data/siren_non_resolus.csv"
HEADERS = {"User-Agent": "truth-engine-pilote-sesn"}
API = "https://recherche-entreprises.api.gouv.fr/search?q={}&per_page=1"

def luhn(num: str) -> bool:
    """Cle de Luhn (standard SIREN/SIRET). num = string de chiffres, cle incluse."""
    digits = [int(c) for c in num]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def normaliser_siret(v: str) -> str:
    """Supprime espaces/points/tirets, ne garde que les chiffres."""
    return "".join(c for c in v if c.isdigit())


def normaliser_objet(v: str) -> str:
    """Objet normalise pour les cles de dedup des id degrades : minuscules,
    espaces multiples reduits, sans accents (cle de comparaison interne)."""
    import unicodedata

    s = v.lower().strip()
    s = " ".join(s.split())
    s = "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )
    return s


def api_siren(siren: str) -> dict:
    """Interroge l'API recherche-entreprises pour un SIREN. Retourne
    {'nom', 'siege_siret', 'nature_juridique', 'date_creation', 'etat'} ou {}."""
    url = API.format(siren)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode("utf-8"))
        if not data.get("results"):
            return {}
        # anti-fausse-precision : ne retenir que le resultat dont le champ siren
        # correspond EXACTEMENT au SIREN interroge (l'API trie par pertinence,
        # results[0] peut etre un homonyme sur un fragment de nom).
        res = next((r for r in data["results"] if r.get("siren") == siren), None)
        if res is None:
            return {}
        return {
            "nom": res.get("nom_complet", ""),
            "siege_siret": (res.get("siege") or {}).get("siret", ""),
            "nature_juridique": res.get("nature_juridique", ""),
            "date_creation": res.get("date_creation", ""),
            "etat": res.get("etat_administratif", ""),
        }
    except Exception as exc:  # pragma: no cover - dependance reseau
        return {"erreur": str(exc)[:120]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--api", action="store_true", help="Appeler l'API recherche-entreprises")
    args = ap.parse_args()

    if not Path(SRC).exists():
        print("FICHIER MANQUANT:", SRC, file=sys.stderr)
        return 1

    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))

    # garde-fou : l'entree DOIT etre la table dedupliquee (jamais raw_v2, qui
    # contiendrait la ligne AWS DOUBLON_DEFECTUEUX et reinflaterait le cumul).
    if "correction_doublon" in rows[0] and any(
        (r.get("correction_doublon") or "").startswith("DOUBLON_DEFECTUEUX") for r in rows
    ):
        print("ERREUR : entree contenant des lignes DOUBLON_DEFECTUEUX (utiliser decp_sesn_dedup.csv)", file=sys.stderr)
        return 1
    print("lignes entree:", len(rows))

    seen = {}
    out = []
    for r in rows:
        # --- acheteur ---
        a_id = (r.get("acheteur_id") or "").strip()
        a_siret = normaliser_siret(a_id)
        a_siren = a_siret[:9] if len(a_siret) >= 9 else a_siret
        a_luhn = luhn(a_siret) if len(a_siret) == 14 else (luhn(a_siren) if len(a_siren) == 9 else False)

        # --- titulaires ---
        t_raw = (r.get("titulaires_siret") or "").strip()
        tit_bruts = [s.strip() for s in t_raw.split(";") if s.strip()]
        tit_sirets = []
        tit_luhn = []
        for s in tit_bruts:
            nums = normaliser_siret(s)
            if not nums:
                # SIRET non numerique (lettres, « N/A », vide) : signale, jamais
                # supprime silencieusement (discipline forensique).
                tit_sirets.append("")
                tit_luhn.append("NON_NUMERIQUE")
            else:
                tit_sirets.append(nums)
                if len(nums) == 14:
                    tit_luhn.append("OK" if luhn(nums) else "ERR")
                elif len(nums) == 9:
                    tit_luhn.append("SIREN" if luhn(nums) else "ERR")
                else:
                    tit_luhn.append("LEN" + str(len(nums)))
        tit_sirens = [s[:9] if len(s) >= 9 else s for s in tit_sirets]

        # --- cle de dedup ---
        id_brut = (r.get("id") or "").strip()
        # id degrade : vide, ou placeholder AWS "000" / "000D0390" (plusieurs
        # marches distincts partagent cet id -> la cle inclut l'objet normalise,
        # regle anti-fusion des lots). Les id PLACE (numeriques, ou
        # alphanumeriques type "2026T14842") sont des identifiants pleins.
        if id_brut and not id_brut.startswith("000"):
            cle = (id_brut, a_id, (r.get("source") or "").strip())
        else:
            cle = ("DEGRADE:" + id_brut, normaliser_objet(r.get("objet") or ""), a_id, (r.get("source") or "").strip())

        if cle in seen:
            statut = "DOUBLON_CLE"
        else:
            seen[cle] = True
            statut = "UNIQUE"

        row = dict(r)
        row["acheteur_siren"] = a_siren
        row["acheteur_siret"] = a_siret
        row["acheteur_luhn"] = "OK" if (a_luhn and len(a_siret) == 14) else ("SIREN" if a_luhn and len(a_siren) == 9 else "ERR/VIDE")
        row["titulaires_siret_norm"] = ";".join(tit_sirets)
        row["titulaires_siren"] = ";".join(tit_sirens)
        row["titulaires_luhn"] = ";".join(tit_luhn)
        row["cle_dedup"] = "|".join(cle)
        row["statut_dedup"] = statut
        row["rne_statut"] = ""
        out.append(row)

    n_doublons = sum(1 for r in out if r["statut_dedup"] == "DOUBLON_CLE")
    print("doublons par cle:", n_doublons)

    # --- rapprochement RNE par SIREN (facultatif, --api) ---
    rne_cache = {}
    if args.api:
        sirens = sorted({s for r in out for s in r["titulaires_siren"].split(";") if s})
        print("SIREN titulaires uniques:", len(sirens))
        for s in sirens:
            rne_cache[s] = api_siren(s)
            time.sleep(0.15)
        for r in out:
            statuts = []
            for s in r["titulaires_siren"].split(";"):
                if not s:
                    statuts.append("VIDE")
                elif s in rne_cache and rne_cache[s]:
                    statuts.append("RESOLU" if not rne_cache[s].get("erreur") else "API_ERR")
                else:
                    statuts.append("INTROUVABLE")
            r["rne_statut"] = ";".join(statuts)
    else:
        for r in out:
            r["rne_statut"] = "NON_TENTE" if r["titulaires_siren"] else "VIDE"

    # --- ecritures ---
    fieldnames = list(out[0].keys())
    with open(DST, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out)
    raw = open(DST, "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    Path(DST + ".sha256").write_text(h + "  " + DST + "\n", encoding="utf-8")

    # fichier RNE : 1 ligne par SIREN
    with open(DST_RNE, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["siren", "nom", "siege_siret", "nature_juridique", "date_creation", "etat", "erreur"])
        for s in sorted(rne_cache):
            d = rne_cache[s]
            w.writerow([s, d.get("nom", ""), d.get("siege_siret", ""),
                        d.get("nature_juridique", ""), d.get("date_creation", ""),
                        d.get("etat", ""), d.get("erreur", "")])

    # non resolus
    non_resolus = [s for s, d in rne_cache.items() if not d or d.get("erreur")]
    with open(DST_NON_RESOLUS, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(sorted(non_resolus)) + "\n") if non_resolus else f.write("")

    print("sortie:", DST, "(", len(out), "lignes,", "doublons", n_doublons, ")")
    print("sha256:", h)
    print("SIREN non resolus:", len(non_resolus))
    if args.api:
        print("mode API : rapprochement RNE effectue")
    else:
        print("mode hors-ligne : relancer avec --api pour le rapprochement RNE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
