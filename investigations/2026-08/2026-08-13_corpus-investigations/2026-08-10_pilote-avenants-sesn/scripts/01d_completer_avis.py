#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script 01d du pilote avenants SESN : enrichissement des 5 avis widget (Phase 1-bis).

Entrée  : data/recensement_univers_v2.csv (116 lignes, sha256 73a23a23...)
Sortie  : data/recensement_univers_v3.csv + data/recensement_univers_v3.csv.sha256
Principe : déterministe (0 LLM), enrichit les lignes EXISTANTES par numero_marche
(M404, M405, M522, M524, MC04) avec les données lues en source primaire le
10/08/2026. JAMAIS de doublon : une ligne par numero_marche. Constat documenté
pour les idweb widget inexistants dans le flux DILA 2026.

Sources primaires lues (10/08/2026) :
- M404 : BOAMP XML DILA 25-130941 (2025/11/26, HTTP 200, 14 557 o)
  https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/2025/11/26/25-130941.xml
- M405 : BOAMP XML DILA 25-124779 (2025/11/09, HTTP 200, 63 539 o) + TED UDL
  747456-2025 (22 013 o) : avis de consultation, pas de montant
- M522 : TED UDL 389639-2026 (21 137 o) : avis de consultation (InternalID F-PF-1831411)
- M524 : TED UDL 485750-2026 (30 960 o) : avis de consultation 2 étapes (T-PF-1842014)
- MC04 : BOAMP XML DILA 26-72063 (2026/07/21, HTTP 200, 66 103 o) + TED UDL
  502268-2026 (22 750 o) : AVIS D'ATTRIBUTION, montant 498 522,46 EUR (option
  « Prestations d'Ecologue » 16 475,00 EUR), attributaire PINSON PAYSAGE (Andilly 95580)

Constat (corrigé après revue 14:05) : les idweb BOAMP du widget M522 (26-55339)
et M524 (26-69739) N'EXISTENT PAS dans le flux DILA 2026 (404 sur dates
plausibles, absents des index 06/05 et 07/10). Le idweb MC04 (26-72063) EXISTE
au 2026/07/21 (HTTP 200, 66 103 o) : c'est l'avis d'attribution du MC04 (erreur
corrigée de ma première passe, signalée par revue). Hypothèse pour les absents :
idweb widget = identifiants plateforme AWS (Idm), pas BOAMP.
"""

import csv
import hashlib
import sys
from collections import OrderedDict

SRC = "data/recensement_univers_v2.csv"
DST = "data/recensement_univers_v3.csv"

# Données vérifiées en source primaire (10/08/2026)
# numero_marche -> {objet, montant_initial, date_notification, supports, idweb_boamp, notice_ted, version_schema}
ENRICH = OrderedDict([
    ("M404", {
        "objet": "Travaux de réhabilitation du quai travaux d'Havrincourt, dit quai de Graincourt (rive Est, canal du Nord, PK17.900, 62147 Havrincourt) - travaux préparatoires CSNE (avis BOAMP 25-130941)",
        "montant_initial": "",
        "date_notification": "2025-11-26",
        "supports": "BOAMP",
        "idweb_boamp": "25-130941",
        "notice_ted": "",
        "version_schema": "",
        "nature": "carte widget SCSNE enrichie BOAMP XML (consultation)",
    }),
    ("M405", {
        "objet": "Travaux de déboisement dans le cadre des travaux préparatoires du projet de construction du secteur 4 du CSNE (avis BOAMP 25-124779 / TED 747456-2025, CPV 77211400)",
        "montant_initial": "",
        "date_notification": "2025-11-09",
        "supports": "BOAMP;TED",
        "idweb_boamp": "25-124779",
        "notice_ted": "747456-2025",
        "version_schema": "",
        "nature": "carte widget SCSNE enrichie BOAMP+TED XML (consultation)",
    }),
    ("M522", {
        "objet": "Fabrication et amenée à pied d'oeuvre des vérins oléohydrauliques pour les portes amont des écluses (CPV 44212383/45248100) - CSNE (notice TED 389639-2026 ; idweb widget 26-55339 INEXISTANT dans flux DILA 2026)",
        "montant_initial": "",
        "date_notification": "2026-06-08",
        "supports": "TED",
        "idweb_boamp": "26-55339",
        "notice_ted": "389639-2026",
        "version_schema": "",
        "nature": "carte widget SCSNE enrichie TED XML (consultation)",
    }),
    ("M524", {
        "objet": "Travaux 4 métiers : équipements hydrauliques et pompage, courants forts et éclairage, courants faibles et systèmes (CPV 45310000/34990000/45232152/45248000), CA requis 80 M EUR HT - CSNE (notice TED 485750-2026, procédure 2 étapes ; idweb widget 26-69739 INEXISTANT dans flux DILA 2026)",
        "montant_initial": "",
        "date_notification": "2026-07-14",
        "supports": "TED",
        "idweb_boamp": "26-69739",
        "notice_ted": "485750-2026",
        "version_schema": "",
        "nature": "carte widget SCSNE enrichie TED XML (consultation 2 étapes)",
    }),
    ("MC04", {
        "objet": "Marché de prestations de services d'aménagements de génie écologique et de petits terrassements (mesures compensatoires hors emprises du CSNE, Ex-B131 Lot B) - ATTRIBUTION à PINSON PAYSAGE (Andilly 95580), 3 offres, CPV 90710000, option Prestations d'Ecologue 16 475,00 EUR (avis BOAMP 26-72063 / TED 502268-2026)",
        "montant_initial": "498522.46",
        "date_notification": "2026-07-21",
        "supports": "BOAMP;TED",
        "idweb_boamp": "26-72063",
        "notice_ted": "502268-2026",
        "version_schema": "",
        "nature": "carte widget SCSNE enrichie BOAMP+TED XML (attribution)",
    }),
])


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    # Garde-fou d'entrée : le v2 ne doit pas déjà contenir les enrichissements
    with open(SRC, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())
    assert len(rows) == 116, f"entrée inattendue : {len(rows)} lignes (attendu 116)"

    # Vérification de pré-conditions : aucune des 5 lignes ne doit déjà être enrichie
    for nm in ENRICH:
        found = [r for r in rows if r["numero_marche"] == nm]
        assert len(found) == 1, f"{nm} : {len(found)} occurrences (attendu 1)"
        r = found[0]
        assert r["objet"] == "", f"{nm} déjà enrichi ? objet={r['objet'][:40]!r}"

    # Application des enrichissements
    for r in rows:
        if r["numero_marche"] in ENRICH:
            e = ENRICH[r["numero_marche"]]
            for k, v in e.items():
                if v != "":
                    r[k] = v
            r["source_entree"] = "BOAMP-TED-widget-enrichi"

    # Dédup de sécurité : une ligne par numero_marche non vide
    seen = set()
    for r in rows:
        nm = r["numero_marche"].strip()
        if nm and nm != "000":
            assert nm not in seen, f"doublon numero_marche {nm}"
            seen.add(nm)

    with open(DST, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    digest = sha256_file(DST)
    with open(DST + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{digest}  {DST}\n")

    # Cumul dédupliqué (hors doublons marqués) - cohérent avec 01c
    from decimal import Decimal
    tot = Decimal("0")
    n = 0
    for r in rows:
        if r["montant_initial"] and not r["objet"].startswith("[DOUBLON_DEFECTUEUX"):
            tot += Decimal(r["montant_initial"])
            n += 1

    print(f"lignes: {len(rows)}")
    print(f"sha256: {digest}")
    print(f"cumul deduplique (montants renseignes, hors doublons marques): {n} lignes, {tot} EUR")
    return 0


if __name__ == "__main__":
    sys.exit(main())
