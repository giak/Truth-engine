#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script 04 du pilote avenants SESN : selection des cas (Phase 4).

Entree : data/decp_sesn_norm.csv (45 lignes) + data/titulaires_rne.csv (noms).
Sortie : data/cas_selection.csv (colonnes protocole : id, voie de selection,
         montant initial, cumul modifications, taux, nature, fondement
         documente, justification, critere preetabli).

REGLES GELÉES (REGISTRE, 2026-08-10 15:05-15:07 CEST, AVANT exécution) :
- A1 : couple (titulaire unique, code CPV complet 8 chiffres) a montant cumule
       maximal avec >= 2 contrats de meme CPV complet (repetition de
       prestations strictement identiques).
- A2 : contrat offresRecues = 1 au montant le plus eleve (concurrence faible).
- A3 : groupe >= 3 contrats de meme famille CPV (division 2 chiffres), tous
       offresRecues = 1, tous « Marché passé sans publicité ni mise en
       concurrence préalable ».
- T1 : travaux (famille CPV 45), montant 3-15 M EUR, procedure avec publicite
       (appel d'offres ouvert ou negociation), offres >= 3, fenetre 2024-2026,
       hors couple A1. Selection : le plus proche en taille des contrats A1.
- T2 : services (famille CPV != 45), montant 1-6 M EUR, procedure avec
       publicite, offres >= 3, fenetre 2024-2026, hors candidats. Selection :
       le plus grand nombre d'offres (concurrence maximale).

Les 3 criteres nominaux du protocole (hausse absolue/relative, violation de
proportionnalite) sont N/A : 0 modification DECP declaree (lacune GAP-001-P1).
La Voie 2 (piste non officielle) est N/A : registre_pistes.csv vide.

Determinisme strict : 100 % calcul, aucun LLM. Zero em-dash.
"""
import csv
from decimal import Decimal

BASE = "data"
INPUT = f"{BASE}/decp_sesn_norm.csv"
RNE = f"{BASE}/titulaires_rne.csv"
OUT = f"{BASE}/cas_selection.csv"

SANS_PUBLICITE = "Marché passé sans publicité ni mise en concurrence préalable"
NEGOCIATION = "Procédure avec négociation"
AO_OUVERT = "Appel d'offres ouvert"
PUBLICITE = (NEGOCIATION, AO_OUVERT)


def famille(cpv):
    return (cpv or "").strip()[:2]


def cpv_base(cpv):
    """Code CPV sans suffixe de schema (retire '-8', '-5'...)."""
    return (cpv or "").strip().split("-")[0]


def main():
    rows = list(csv.DictReader(open(INPUT, encoding="utf-8")))
    assert len(rows) == 45, f"attendu 45 lignes, trouve {len(rows)}"

    rne = {}
    try:
        for r in csv.DictReader(open(RNE, encoding="utf-8")):
            rne[r["siren"].strip()] = r["nom"]
    except FileNotFoundError:
        pass

    by_id = {r["id"]: r for r in rows}

    def dmontant(r):
        return Decimal(r["montant"]) if r["montant"] else Decimal("0")

    # ---- A1 : couple (titulaire, CPV base 8 chiffres) montant cumule max, >= 2 contrats
    # Correction de revue 15:25 : le suffixe de schema ('-8', '-5') est retire
    # avant regroupement (un changement de version de suffixe ne doit pas casser
    # silencieusement le couple).
    couples = {}
    for r in rows:
        for s in [s for s in r["titulaires_siren"].split(";") if s]:
            key = (s, cpv_base(r["codeCPV"]))
            couples.setdefault(key, [Decimal("0"), 0])
            couples[key][0] += dmontant(r) / len([x for x in r["titulaires_siren"].split(";") if x])
            couples[key][1] += 1
    a1_candidats = [(k, v) for k, v in couples.items() if v[1] >= 2]
    a1_candidats.sort(key=lambda kv: -kv[1][0])
    a1_key, a1_val = a1_candidats[0]
    a1_siren, a1_cpv = a1_key
    a1_contrats = [r for r in rows
                   if a1_siren in r["titulaires_siren"].split(";")
                   and cpv_base(r["codeCPV"]) == a1_cpv]
    a1_contrats.sort(key=lambda r: -dmontant(r))

    # ---- A2 : offresRecues = 1, montant max
    a2_pool = [r for r in rows if r["offresRecues"] == "1"]
    a2_contrats = [max(a2_pool, key=dmontant)]

    # ---- A3 : groupe >= 3, meme famille, offres=1, sans publicite
    fam_groups = {}
    for r in rows:
        if r["offresRecues"] == "1" and r["procedure"] == SANS_PUBLICITE:
            fam_groups.setdefault(famille(r["codeCPV"]), []).append(r)
    a3_famille = max(fam_groups, key=lambda f: len(fam_groups[f]))
    a3_contrats = fam_groups[a3_famille]
    assert len(a3_contrats) >= 3, "A3 : attendu >= 3 contrats"
    a3_contrats.sort(key=lambda r: -dmontant(r))

    # ---- T1 : travaux 3-15 M EUR, publicite, offres>=3, fenetre 2024-2026, hors A1
    a1_ids = {r["id"] for r in a1_contrats}
    t1_pool = [r for r in rows
               if famille(r["codeCPV"]) == "45"
               and 3_000_000 <= dmontant(r) <= 15_000_000
               and r["procedure"] in PUBLICITE
               and r["offresRecues"].isdigit() and int(r["offresRecues"]) >= 3
               and (r["dateNotification"] or "") >= "2024-01-01"
               and r["id"] not in a1_ids]
    # le plus proche en taille des contrats A1 (moyenne des montants A1)
    a1_moy = sum(dmontant(r) for r in a1_contrats) / len(a1_contrats)
    t1_contrats = [min(t1_pool, key=lambda r: abs(dmontant(r) - a1_moy))]

    # ---- T2 : services 1-6 M EUR, publicite, offres>=3, hors candidats
    candidat_ids = {r["id"] for r in a1_contrats + a2_contrats + a3_contrats}
    t2_pool = [r for r in rows
               if famille(r["codeCPV"]) != "45"
               and 1_000_000 <= dmontant(r) <= 6_000_000
               and r["procedure"] in PUBLICITE
               and r["offresRecues"].isdigit() and int(r["offresRecues"]) >= 3
               and (r["dateNotification"] or "") >= "2024-01-01"
               and r["id"] not in candidat_ids]
    t2_contrats = [max(t2_pool, key=lambda r: int(r["offresRecues"]))]

    # ---- Assemblage cas_selection.csv
    def ligne(r, voie, critere, justification, fondement):
        return {
            "id": r["id"],
            "voie_selection": voie,
            "montant_initial_eur": str(dmontant(r)),
            "cumul_modifications_eur": "0",
            "taux_modification": "0",
            "nature": famille(r["codeCPV"]),
            "codeCPV": r["codeCPV"],
            "titulaire_siren": r["titulaires_siren"],
            "titulaire_nom": ";".join(rne.get(s, "") for s in r["titulaires_siren"].split(";")),
            "procedure": r["procedure"],
            "offres_recues": r["offresRecues"],
            "date_notification": r["dateNotification"],
            "fondement_documente": fondement,
            "justification": justification,
            "critere_preetabli": critere,
            "objet": r["objet"],
        }

    out = []
    for i, r in enumerate(a1_contrats, 1):
        out.append(ligne(
            r, "V1-A1", "A1 (couple titulaire x CPV complet, cumul max, >= 2 contrats)",
            f"Couple {a1_siren}/{a1_cpv} : {a1_val[0]:,.2f} EUR cumules sur {a1_val[1]} contrats "
            f"(rang 1/{len(a1_candidats)} couples eligibles)",
            "Concentration par repetition de prestations identiques (signal dependance)"))
    for r in a2_contrats:
        out.append(ligne(
            r, "V1-A2", "A2 (offres = 1, montant max)",
            f"Offre unique ({r['offresRecues']}) sur {dmontant(r):,.2f} EUR : plus fort montant "
            f"a concurrence faible du corpus (rang 1/{len(a2_pool)} offres uniques) ; "
            f"objet : {r['objet'][:80]} (id degrade '000' : unicite portee par l'objet)",
            "Concurrence faible averee (offre unique sur montant significatif)"))
    for i, r in enumerate(a3_contrats, 1):
        out.append(ligne(
            r, "V1-A3", "A3 (>= 3 contrats meme famille, offres = 1, sans publicite ni MEC)",
            f"Groupe de {len(a3_contrats)} contrats famille CPV {a3_famille}, tous offres = 1, "
            f"tous sans publicite ni MEC (rang {i}/{len(a3_contrats)}) : legalite de la dispense "
            f"a verifier (hypothese marches subsequents d'accord-cadre ref. 18TRI001B/C, "
            f"fondements derogatoires MOE ; seuil R.2122-8 40 000 EUR HT seulement si contrats autonomes)",
            "Repetition de procedures sans publicite : qualification a verifier (Phase 8)"))
    for r in t1_contrats:
        out.append(ligne(
            r, "TEMOIN-T1", "T1 (travaux 3-15 M EUR, publicite, offres >= 3, taille proche A1)",
            f"Temoin apparie a A1 : {dmontant(r):,.2f} EUR, {r['offresRecues']} offres, "
            f"{r['procedure']} (plus proche de la moyenne A1 {a1_moy:,.2f} EUR)",
            "Contrat comparable avec concurrence reelle et donnees stables"))
    for r in t2_contrats:
        out.append(ligne(
            r, "TEMOIN-T2", "T2 (services 1-6 M EUR, publicite, offres >= 3, concurrence max)",
            f"Temoin apparie a A2 : {dmontant(r):,.2f} EUR, {r['offresRecues']} offres, "
            f"{r['procedure']} (concurrence maximale du pool services)",
            "Contrat comparable avec concurrence reelle et donnees stables"))

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    # ---- Rapport console
    print("=== SELECTION DES CAS (Phase 4, regles gelees 15:05) ===")
    print(f"contrats: {len(rows)} | total: {sum(dmontant(r) for r in rows):,.2f} EUR")
    print(f"\nA1 couple max: {a1_siren} ({a1_cpv}) = {a1_val[0]:,.2f} EUR, {a1_val[1]} contrats")
    for r in a1_contrats:
        print(f"   {r['id']} | {dmontant(r):>14,.2f} | offres {r['offresRecues']} | {r['objet'][:60]}")
    print(f"\nA2: {a2_contrats[0]['id']} | {dmontant(a2_contrats[0]):,.2f} EUR | offres 1 | {a2_contrats[0]['objet'][:60]}")
    print(f"\nA3 famille {a3_famille} ({len(a3_contrats)} contrats):")
    for r in a3_contrats:
        print(f"   {r['id']} | {dmontant(r):>12,.2f} | {r['objet'][:60]}")
    print(f"\nT1: {t1_contrats[0]['id']} | {dmontant(t1_contrats[0]):,.2f} EUR | offres {t1_contrats[0]['offresRecues']} | {t1_contrats[0]['objet'][:60]}")
    print(f"T2: {t2_contrats[0]['id']} | {dmontant(t2_contrats[0]):,.2f} EUR | offres {t2_contrats[0]['offresRecues']} | {t2_contrats[0]['objet'][:60]}")
    print(f"\n-> {OUT} ({len(out)} lignes)")


if __name__ == "__main__":
    main()
