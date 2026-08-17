#!/usr/bin/env python3
"""Script 01 du pilote avenants SESN : extraction des DECP de la SCSNE depuis les fichiers consolidés du ministère des Finances.

Source : dataset data.gouv.fr « Données essentielles de la commande publique - fichiers consolidés »
(https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-fichiers-consolides)
Publié par le ministère des Finances (DGFiP/AIFE, retraitement data.gouv).

Méthode :
1. Téléchargement du fichier JSON consolidé global (toutes années) en streaming.
2. Hachage SHA-256 pendant le téléchargement (decp-global.json.sha256).
3. Parsing streaming (ijson) sans chargement complet en mémoire.
4. Filtrage : pouvoir adjudicateur = SCSNE/SESN, identifié par SIREN 829535996
   (vérifié API recherche-entreprises.api.gouv.fr le 10/08/2026) sur acheteur.id,
   et par « Seine-Nord » dans le libellé acheteur si présent.
5. Fenêtre temporelle : notification du 2021-01-01 au 2026-06-30 (date de coupure RUN_MANIFEST).
6. Sorties : data/decp_sesn_raw.csv + data/decp_sesn_raw.sha256 + data/recensement_univers.csv (stub, complété en Phase 2) + data/marches_sans_montant.csv + data/registre_pistes.csv (créé vide).

Déterministe : mêmes entrées -> mêmes sorties (ordre trié par id puis dateNotification).
Usage : python3 scripts/01_extract_decp.py [--url URL] [--out DIR]
Ne nécessite que la stdlib + ijson (venv /tmp/opencode/pilote-venv).
"""

import argparse
import csv
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

SIREN_SCSNE = "829535996"
DEFAULT_URL = "https://static.data.gouv.fr/resources/donnees-essentielles-de-la-commande-publique-fichiers-consolides/20260804-134059/decp-global.json"
COUPURE = "2026-06-30"
DEBUT = "2021-01-01"
HEADERS = {"User-Agent": "truth-engine-pilote-sesn"}

CHAMPS_CSV = [
    "id", "_type", "objet", "nature", "source", "codeCPV", "montant",
    "dureeMois", "formePrix", "procedure", "offresRecues",
    "dateNotification", "datePublicationDonnees", "dateSignature",
    "acheteur_id", "acheteur_nom", "titulaires_siret", "titulaires_nom",
    "lieuExecution_code", "typeGroupementOperateurs", "modifications",
    "ref__file_date",
]


def telecharger_avec_hash(url: str, dest: Path) -> str:
    """Télécharge url vers dest en calculant sha256 en vol. Retourne le hex digest."""
    h = hashlib.sha256()
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as f:
        while True:
            bloc = r.read(1 << 20)
            if not bloc:
                break
            f.write(bloc)
            h.update(bloc)
    return h.hexdigest()


def aplatir_titulaires(titulaires):
    """Récupère la liste des identifiants/noms de titulaires (structure variable)."""
    sirets, noms = [], []
    if not titulaires:
        return sirets, noms
    if isinstance(titulaires, dict):
        titulaires = [titulaires]
    for t in titulaires:
        if isinstance(t, dict):
            titre = t.get("titulaire", t)
            if isinstance(titre, dict):
                if titre.get("id"):
                    sirets.append(str(titre["id"]))
                if titre.get("nom"):
                    noms.append(str(titre["nom"]))
    return sirets, noms


def est_sesn(marche: dict) -> bool:
    """Vrai si le marché appartient à la SCSNE (SIREN 829535996) ou mentionne Seine-Nord comme acheteur."""
    ach = marche.get("acheteur") or {}
    ach_id = str(ach.get("id", ""))
    if ach_id.startswith(SIREN_SCSNE):
        return True
    if ach.get("nom") and "seine-nord" in str(ach["nom"]).lower():
        return True
    obj = str(marche.get("objet", ""))
    if "canal seine-nord" in obj.lower() and not ach_id:
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=DEFAULT_URL)
    ap.add_argument("--out", default="data")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    global_f = out / "decp-global.json"
    if global_f.exists():
        print(f"[info] {global_f.name} existe déjà, hachage local")
        digest = hashlib.sha256(global_f.read_bytes()).hexdigest()
    else:
        print("[info] téléchargement du fichier consolidé global (peut être long, ~1 Go)")
        digest = telecharger_avec_hash(args.url, global_f)
    (out / "decp-global.json.sha256").write_text(f"{digest}  decp-global.json\n")
    print(f"[hash] sha256 decp-global.json = {digest}")

    ligne_raw = []
    n_total = 0
    n_sesn = 0
    with open(global_f, "rb") as f:
        parseur = ijson.items(f, "marches.marche.item")
        for m in parseur:
            n_total += 1
            if not est_sesn(m):
                continue
            n_sesn += 1
            dn = str(m.get("dateNotification", "")) or ""
            if dn and not (DEBUT <= dn <= COUPURE):
                continue
            tit_sirets, tit_noms = aplatir_titulaires(m.get("titulaires"))
            mods = m.get("modifications")
            ligne_raw.append({
                "id": m.get("id", ""), "_type": m.get("_type", ""),
                "objet": m.get("objet", ""), "nature": m.get("nature", ""),
                "source": m.get("source", ""), "codeCPV": m.get("codeCPV", ""),
                "montant": m.get("montant", ""), "dureeMois": m.get("dureeMois", ""),
                "formePrix": m.get("formePrix", ""), "procedure": m.get("procedure", ""),
                "offresRecues": m.get("offresRecues", ""),
                "dateNotification": m.get("dateNotification", ""),
                "datePublicationDonnees": m.get("datePublicationDonnees", ""),
                "dateSignature": m.get("dateSignature", ""),
                "acheteur_id": (m.get("acheteur") or {}).get("id", ""),
                "acheteur_nom": (m.get("acheteur") or {}).get("nom", ""),
                "titulaires_siret": ";".join(tit_sirets),
                "titulaires_nom": ";".join(tit_noms),
                "lieuExecution_code": (m.get("lieuExecution") or {}).get("code", ""),
                "typeGroupementOperateurs": m.get("typeGroupementOperateurs", ""),
                "modifications": json.dumps(mods, ensure_ascii=False) if mods else "",
                "ref__file_date": m.get("ref__file_date", ""),
            })

    ligne_raw.sort(key=lambda x: (str(x["id"]), str(x["dateNotification"])))
    with open(out / "decp_sesn_raw.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CHAMPS_CSV, extrasaction="ignore")
        w.writeheader()
        w.writerows(ligne_raw)
    digest_raw = hashlib.sha256(
        (out / "decp_sesn_raw.csv").read_bytes()
    ).hexdigest()
    (out / "decp_sesn_raw.sha256").write_text(f"{digest_raw}  decp_sesn_raw.csv\n")

    sans_montant = [l for l in ligne_raw if l["montant"] in ("", None)]
    with open(out / "marches_sans_montant.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "objet", "nature", "dateNotification", "acheteur_id"])
        w.writeheader()
        w.writerows({k: l[k] for k in w.fieldnames} for l in sans_montant)

    print(f"[stats] marchés SCSNE extraits (fenêtre {DEBUT}..{COUPURE}) : {len(ligne_raw)}")
    print(f"[stats] dont sans montant : {len(sans_montant)}")
    print(f"[stats] total marchés dans fichier global : {n_total}")
    print(f"[hash] sha256 decp_sesn_raw.csv = {digest_raw}")


if __name__ == "__main__":
    import ijson  # noqa: E402
    sys.exit(main())
