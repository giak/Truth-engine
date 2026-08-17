#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script 01c du pilote avenants SESN : completion du recensement univers.

Objectif (demande utilisateur 2026-08-10 13:05) : fermer le gap de couverture
DECP sur les quais fluviaux en ajoutant le lot Q1-M213 (SPIE Batignolles Nord,
2 999 530,10 EUR HT), absent des DECP consolidees mais documente dans l'avis
d'attribution BOAMP 25-132968 / JOUE 806579-2025 (marche M215, conclu 20/11/2025).

Traitements (deterministe pur, 0 LLM) :
1. Corriger la ligne AWS id=000 « réhabilitation de 4 quais » du recensement :
   montant 422 841 600,00 -> 4 228 416,00 (erreur d'unite x100, voir TRANCHÉ
   2026-08-10 12:47 du REGISTRE) et prefixer l'objet par [DOUBLON_DEFECTUEUX de
   2844722] pour la tracabilite (la ligne PLACE 2844722 = M214-Q2 fait reference).
2. Ajouter la ligne Q1-M213 depuis l'avis BOAMP (source_entree = BOAMP-TED).

Entree : data/recensement_univers.csv (v1, produit par 01b, 115 lignes data).
Sortie : data/recensement_univers_v2.csv (117 lignes data : +1 Q1-M213, ligne
AWS corrigee) + .sha256.

Usage : python3 scripts/01c_completer_recensement.py
"""

import csv
import hashlib
import sys
from pathlib import Path

SRC = "data/recensement_univers.csv"
DST = "data/recensement_univers_v2.csv"

LIGNE_Q1 = {
    "numero_marche": "M213",
    "objet": "Lot Q1 - M213 : réhabilitation de quais existants (Pont l'Évêque, "
             "Languevoisin, Rouy-le-Petit, Péronne) - Canal du Nord Secteur 2 - "
             "travaux préparatoires CSNE (avis BOAMP 25-132968)",
    "montant_initial": "2999530.10",
    "date_notification": "2025-11-20",
    "nature": "Marché",
    "acheteur": "82953599600039",
    "supports": "BOAMP;TED",
    "idweb_boamp": "25-132968",
    "notice_ted": "806579-2025",
    "aws_idm": "",
    "version_schema": "",
    "source_entree": "BOAMP-TED",
}

# PERIMETRE DE SOMME : toute somme du recensement DOIT exclure les lignes
# marquees DOUBLON_DEFECTUEUX (conservees pour tracabilite, jamais additionnees).
def est_doublon_defectueux(r: dict) -> bool:
    return (r.get("objet") or "").startswith("[DOUBLON_DEFECTUEUX")


def cumul_montants(rows, exclure_doublons: bool = True):
    """Somme des montants_initial renseignes. Si exclure_doublons, les lignes
    marquees DOUBLON_DEFECTUEUX ne sont pas comptees (regle anti-double-compte)."""
    from decimal import Decimal
    tot = Decimal("0")
    nb = 0
    for r in rows:
        if not r.get("montant_initial"):
            continue
        if exclure_doublons and est_doublon_defectueux(r):
            continue
        tot += Decimal(r["montant_initial"])
        nb += 1
    return tot, nb


def main() -> int:
    if not Path(SRC).exists():
        raise SystemExit("FICHIER MANQUANT: " + SRC)

    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    print("lignes entree (data):", len(rows))

    corr_aws = 0
    for r in rows:
        if r.get("numero_marche") == "000" and "réhabilitation de 4 quais" in (r.get("objet") or ""):
            assert r.get("montant_initial") == "422841600.0", "montant AWS inattendu: %s" % r.get("montant_initial")
            r["montant_initial"] = "4228416.0"
            r["objet"] = "[DOUBLON_DEFECTUEUX de 2844722 (M214-Q2)] " + r["objet"]
            corr_aws += 1

    # dedup : ne pas ajouter Q1 si une ligne M213 existe deja (garde defensive :
    # SRC est fige sur v1 qui ne contient jamais M213, mais on protege une
    # eventuelle re-execution sur un fichier deja complete).
    deja = any(r.get("numero_marche") == "M213" for r in rows)
    if deja:
        print("M213 deja present : ligne non ajoutee")
    else:
        rows.append(LIGNE_Q1)

    fieldnames = list(rows[0].keys())
    with open(DST, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    raw = open(DST, "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    Path(DST + ".sha256").write_text(h + "  " + DST + "\n", encoding="utf-8")

    tot, nb = cumul_montants(rows)
    tot_brut, nb_brut = cumul_montants(rows, exclure_doublons=False)
    print("lignes sortie (data):", len(rows))
    print("corrections AWS:", corr_aws)
    print("Q1-M213 ajoute:", not deja)
    print("cumul montants renseignes (hors doublons marques):", tot, "(", nb, "lignes )")
    print("cumul brut (avec doublons, a NE PAS utiliser):", tot_brut, "(", nb_brut, "lignes )")
    print("sha256:", h)
    return 0


if __name__ == "__main__":
    sys.exit(main())
