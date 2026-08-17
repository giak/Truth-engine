#!/usr/bin/env python3
"""Consolidation Phase 1 du pilote SESN : recensement univers des marchés.

Fusionne les sources collectées :
- DECP consolidées data.gouv (ministère des Finances) filtrees SCSNE (SIREN 829535996)
  -> data/decp_sesn_raw.csv (produit par 01_extract_decp.py)
- Page Marchés publics SCSNE (canal-seine-nord-europe.fr/marches-publics/)
  -> numéros SESN + liens BOAMP/TED extraits du HTML (extraction 10/08/2026, toutes pages)
- Widget SCSNE (120 résultats) -> cartes page 1 (12 cartes, HTML racine)
- Recherche AWS marches-publics.info (10/08/2026) : 1 annonce (M524)

Sortie : data/recensement_univers.csv
Champs : numero_marche, objet, montant_initial, date_notification, nature, acheteur,
         supports, idweb_boamp, notice_ted, aws_idm, version_schema, source_entree
Contrôle qualité : total vs 74-76 marchés (rapport CdC 10/04/2026) : écart documenté.

Déterministe : stdin->stdout, tri par numero_marche.
Usage : python3 scripts/01b_recensement_univers.py
"""

import csv
import json
import sys
from pathlib import Path

OUT = Path("data")
CHAMPS = ["numero_marche", "objet", "montant_initial", "date_notification",
          "nature", "acheteur", "supports", "idweb_boamp", "notice_ted",
          "aws_idm", "version_schema", "source_entree"]


def lire_raw_decp():
    rows = []
    p = OUT / "decp_sesn_raw.csv"
    if not p.exists():
        return rows
    with open(p, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "numero_marche": r.get("id", "").strip(),
                "objet": r.get("objet", "").strip(),
                "montant_initial": r.get("montant", "").strip(),
                "date_notification": r.get("dateNotification", "").strip(),
                "nature": r.get("nature", "").strip(),
                "acheteur": r.get("acheteur_id", "").strip(),
                "supports": r.get("source", "").strip(),
                "version_schema": "2022" if r.get("source") == "AIFE_PLACE" else "2019",
                "source_entree": "DECP-consolides",
                "idweb_boamp": "", "notice_ted": "", "aws_idm": "",
            })
    return rows


def main():
    lignes = lire_raw_decp()
    # Page SCSNE : liste statique des numéros SESN (déjà extraite -> JSON)
    j = "/tmp/opencode/scsne_listes.json"
    try:
        d = json.loads(Path(j).read_text(encoding="utf-8"))
        sesn_list = d.get("sesn", [])
    except Exception:
        sesn_list = []
    for n in sesn_list:
        if any(l["numero_marche"] == n for l in lignes):
            continue
        lignes.append({
            "numero_marche": n, "objet": "", "montant_initial": "",
            "date_notification": "", "nature": "marché (page SCSNE)",
            "acheteur": "SCSNE", "supports": "page-SCSNE",
            "version_schema": "", "source_entree": "page-SCSNE",
            "idweb_boamp": "", "notice_ted": "", "aws_idm": "",
        })
    # Cartes widget SCSNE (12 de la page racine)
    wj = "/tmp/opencode/scsne_widget_p1.json"
    try:
        cartes = json.loads(Path(wj).read_text(encoding="utf-8"))
    except Exception:
        cartes = []
    for c in cartes:
        num = c.get("numero", "")
        if not num or any(l["numero_marche"] == num for l in lignes):
            continue
        lignes.append({
            "numero_marche": num, "objet": "", "montant_initial": "",
            "date_notification": "", "nature": "carte widget SCSNE",
            "acheteur": "SCSNE", "supports": "widget-SCSNE",
            "version_schema": "", "source_entree": "widget-SCSNE",
            "idweb_boamp": c.get("boamp_idweb", ""), "notice_ted": c.get("ted_notice", ""),
            "aws_idm": c.get("aws_idm", ""),
        })

    # Dédoublonnage par (numero_marche) avec trace des supports
    # ATTENTION : les ID dégradés ('000', '000D0390', '') ne sont PAS des clés
    # valides (plusieurs marchés AWS distincts partagent '000') : clé = id + objet.
    ID_DEGRADES = {"000", "000D0390", ""}
    uniques = {}
    for l in lignes:
        if l["numero_marche"] in ID_DEGRADES:
            k = l["numero_marche"] + "#" + l["objet"][:40]
        else:
            k = l["numero_marche"]
        if k in uniques:
            anc = uniques[k]
            anc["supports"] = anc["supports"] + "|" + l["supports"]
            anc["idweb_boamp"] = (anc["idweb_boamp"] + ";" + l["idweb_boamp"]).strip(";")
            anc["notice_ted"] = (anc["notice_ted"] + ";" + l["notice_ted"]).strip(";")
        else:
            uniques[k] = dict(l)

    lignes = list(uniques.values())
    lignes.sort(key=lambda x: (str(x["numero_marche"])))
    with open(OUT / "recensement_univers.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CHAMPS, extrasaction="ignore")
        w.writeheader()
        w.writerows(lignes)

    sans_montant = [l for l in lignes if not l["montant_initial"]]
    with open(OUT / "marches_sans_montant.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["numero_marche", "objet", "nature",
                                          "date_notification", "supports"])
        w.writeheader()
        w.writerows({k: l.get(k, "") for k in w.fieldnames} for l in sans_montant)

    # Registre des pistes : ouvert vide en Phase 1
    if not (OUT / "registre_pistes.csv").exists():
        with open(OUT / "registre_pistes.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id_piste", "date_ouverture", "origine", "formulation_falsifiable",
                        "contrat_designe", "elements_verifiables", "statut", "notes"])

    print(f"recensement total : {len(lignes)}")
    print(f"depuis DECP : {sum(1 for l in lignes if l['source_entree']=='DECP-consolides')}")
    print(f"seulement page-SCSNE : {sum(1 for l in lignes if l['source_entree']=='page-SCSNE')}")
    print(f"widget SCSNE : {sum(1 for l in lignes if l['source_entree']=='widget-SCSNE')}")
    print(f"sans montant : {len(sans_montant)}")
    print("ATTENTION : total attendu 74-76 (rapport CdC 10/04/2026) ; écart à documenter "
          "ligne par ligne (DECP 2021-2023 absentes des consolidés ministère).")


if __name__ == "__main__":
    sys.exit(main())