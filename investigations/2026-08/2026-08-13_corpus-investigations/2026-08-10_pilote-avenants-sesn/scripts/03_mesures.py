#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script 03 du pilote avenants SESN : mesures quantitatives (Phase 3).

Entrée  : data/decp_sesn_norm.csv (45 lignes, dedup Phase 2, sha256 356d790a...)
          + data/titulaires_rne.csv (noms des attributaires).
Sorties :
- data/mesures_sesn.csv           : mesures par contrat (montant initial/final,
                                    nb modifications, cumul, taux).
- data/concentration_sesn.csv     : concentration par SIREN titulaire + CR5/CR10.
- data/indicateurs_sesn.csv       : indicateurs agreges (procedures, candidatures
                                    uniques, repartition par nature).
Determinisme strict : 100 % calcul, aucun LLM. Zero em-dash.

Methode (protocole Phase 3) :
- Unite d'analyse = contrat. Le champ montant = montant initial (0 modification
  declaree dans les DECP SCSNE : constat GAP-001-P1, voir REGISTRE).
- Concentration : repartition EQUITABLE du montant d'un groupement entre ses
  membres (pas d'hypothese de partage interne).
- Nature derivee du code CPV (division) : 45 = TRAVAUX, 39 = FOURNITURES,
  autres = SERVICES.
- Taux de modification = cumul modifications / montant initial (ici 0 : lacune
  DECP, PAS une absence reelle, a confirmer Phase 4 via PLACE/BOAMP/TED).
"""
import csv
import hashlib
import os
from collections import Counter, OrderedDict
from decimal import Decimal

BASE = "data"
INPUT = f"{BASE}/decp_sesn_norm.csv"
RNE = f"{BASE}/titulaires_rne.csv"
OUT_MESURES = f"{BASE}/mesures_sesn.csv"
OUT_CONC = f"{BASE}/concentration_sesn.csv"
OUT_INDIC = f"{BASE}/indicateurs_sesn.csv"

# Reference attendue (RUN_MANIFEST Phase 3) : 103 578 507,98 EUR HT
TOTAL_REF = Decimal("103578507.98")


def luhn_ok(n):
    """Cle de Luhn sur un SIRET (14 chiffres) ou SIREN (9 chiffres)."""
    n = n.replace(" ", "").strip()
    if not n.isdigit():
        return False
    total = 0
    for i, ch in enumerate(reversed(n)):
        d = int(ch)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def famille_cpv(cpv):
    """Famille derivee de la division CPV (2 premiers chiffres)."""
    c = (cpv or "").strip()
    if not c:
        return "INCONNU"
    div = c[:2]
    if div == "45":
        return "TRAVAUX"
    if div == "39":
        return "FOURNITURES"
    return "SERVICES"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    rows = list(csv.DictReader(open(INPUT, encoding="utf-8")))
    assert len(rows) == 45, f"attendu 45 lignes, trouve {len(rows)}"

    # Charger les noms RNE
    rne = {}
    if os.path.exists(RNE):
        for r in csv.DictReader(open(RNE, encoding="utf-8")):
            rne[r["siren"].strip()] = r["nom"]

    # ---- Mesures par contrat ----
    mesures = []
    total = Decimal("0")
    for r in rows:
        m = Decimal(r["montant"]) if r["montant"] else Decimal("0")
        total += m
        modifs = (r.get("modifications") or "").strip()
        # FAIL-FAST (correction de revue 14:35) : si une DECP de modification
        # apparaissait, le modele evenementiel (nouveau total - valeur precedente)
        # doit etre calcule, jamais remplace par un 0 silencieux.
        assert not modifs, (
            f"DECP de modification non implementee (id {r['id']}) : "
            "modele evenementiel requis (cumul = montant modifie - precedent)"
        )
        n_modif = 0
        cumul = Decimal("0")
        taux = Decimal("0")
        mesures.append({
            "id": r["id"],
            "objet": r["objet"],
            "nature_CPV": famille_cpv(r["codeCPV"]),
            "codeCPV": r["codeCPV"],
            "montant_initial_eur": str(m),
            "montant_final_eur": str(m),  # 0 modif connue
            "nb_evenements_modification": str(n_modif),
            "cumul_modifications_eur": str(cumul),
            "taux_modification": str(taux),
            "procedure": r["procedure"],
            "offres_recues": r["offresRecues"],
            "nb_titulaires": str(len([s for s in r["titulaires_siren"].split(";") if s])),
            "titulaires_siren": r["titulaires_siren"],
            "statut_dedup": r["statut_dedup"],
            "source": r["source"],
        })

    assert total == TOTAL_REF, f"total {total} != reference {TOTAL_REF}"

    with open(OUT_MESURES, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(mesures[0].keys()))
        w.writeheader()
        w.writerows(mesures)

    # ---- Concentration par SIREN (partage equitable des groupements) ----
    conc = OrderedDict()  # siren -> [montant_part, nb_contrats]
    for r in rows:
        m = Decimal(r["montant"]) if r["montant"] else Decimal("0")
        sirens = [s for s in r["titulaires_siren"].split(";") if s]
        if not sirens:
            continue
        part = m / len(sirens)
        for s in sirens:
            if s not in conc:
                conc[s] = [Decimal("0"), 0]
            conc[s][0] += part
            conc[s][1] += 1

    ranked = sorted(conc.items(), key=lambda kv: kv[1][0], reverse=True)
    cumul = Decimal("0")
    conc_rows = []
    for i, (siren, (m, nb)) in enumerate(ranked, 1):
        cumul += m
        conc_rows.append({
            "rang": str(i),
            "siren": siren,
            "nom_rne": rne.get(siren, ""),
            "montant_part_eur": str(m.quantize(Decimal("0.01"))),
            "part_pct": str((m / total * 100).quantize(Decimal("0.01"))),
            "nb_contrats": str(nb),
            "montant_cumule_eur": str(cumul.quantize(Decimal("0.01"))),
            "part_cumulee_pct": str((cumul / total * 100).quantize(Decimal("0.01"))),
        })

    cr5 = sum(Decimal(r["montant_part_eur"]) for r in conc_rows[:5]) / total * 100
    cr10 = sum(Decimal(r["montant_part_eur"]) for r in conc_rows[:10]) / total * 100
    hhi = sum((Decimal(r["montant_part_eur"]) / total * 100) ** 2 for r in conc_rows)

    with open(OUT_CONC, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(conc_rows[0].keys()))
        w.writeheader()
        w.writerows(conc_rows)

    # ---- Indicateurs agreges ----
    proc = Counter(r["procedure"] for r in rows)
    proc_montant = {}
    for r in rows:
        proc_montant[r["procedure"]] = proc_montant.get(r["procedure"], Decimal("0")) + (
            Decimal(r["montant"]) if r["montant"] else Decimal("0"))

    cand_unique = [r for r in rows if r["offresRecues"] == "1"]
    cand_unique_montant = sum(Decimal(r["montant"]) for r in cand_unique)
    nb_cand_unique = len(cand_unique)

    negocie = [r for r in rows if "négociation" in r["procedure"] or "negociation" in r["procedure"]]
    sans_publicite = [r for r in rows if "sans publicité" in r["procedure"] or "sans publicite" in r["procedure"]]

    nature_rows = []
    nature_agg = {}
    for r in rows:
        fam = famille_cpv(r["codeCPV"])
        nature_agg.setdefault(fam, [0, Decimal("0")])
        nature_agg[fam][0] += 1
        nature_agg[fam][1] += Decimal(r["montant"]) if r["montant"] else Decimal("0")

    for fam, (nb, m) in sorted(nature_agg.items(), key=lambda kv: -kv[1][1]):
        nature_rows.append({
            "indicateur": f"repartition_nature_{fam}",
            "valeur": str(nb),
            "montant_eur": str(m.quantize(Decimal("0.01"))),
            "part_montant_pct": str((m / total * 100).quantize(Decimal("0.01"))),
        })

    ind_rows = [
        {"indicateur": "total_contrats", "valeur": str(len(rows)), "montant_eur": str(total.quantize(Decimal("0.01"))), "part_montant_pct": "100"},
        {"indicateur": "total_sirens_titulaires", "valeur": str(len(ranked)), "montant_eur": str(total.quantize(Decimal("0.01"))), "part_montant_pct": "100"},
        {"indicateur": "CR5_pct", "valeur": str(cr5.quantize(Decimal("0.01"))), "montant_eur": "", "part_montant_pct": str(cr5.quantize(Decimal("0.01")))},
        {"indicateur": "CR10_pct", "valeur": str(cr10.quantize(Decimal("0.01"))), "montant_eur": "", "part_montant_pct": str(cr10.quantize(Decimal("0.01")))},
        {"indicateur": "HHI_points", "valeur": str(hhi.quantize(Decimal("1"))), "montant_eur": "", "part_montant_pct": ""},
        {"indicateur": "nb_procedures_negociees", "valeur": str(len(negocie)), "montant_eur": str(sum(Decimal(r["montant"]) for r in negocie).quantize(Decimal("0.01"))), "part_montant_pct": str((sum(Decimal(r["montant"]) for r in negocie) / total * 100).quantize(Decimal("0.01")))},
        {"indicateur": "nb_sans_publicite_ni_mec", "valeur": str(len(sans_publicite)), "montant_eur": str(sum(Decimal(r["montant"]) for r in sans_publicite).quantize(Decimal("0.01"))), "part_montant_pct": str((sum(Decimal(r["montant"]) for r in sans_publicite) / total * 100).quantize(Decimal("0.01")))},
        {"indicateur": "nb_candidatures_uniques", "valeur": str(nb_cand_unique), "montant_eur": str(cand_unique_montant.quantize(Decimal("0.01"))), "part_montant_pct": str((cand_unique_montant / total * 100).quantize(Decimal("0.01")))},
        {"indicateur": "nb_modifications_declarees", "valeur": "0", "montant_eur": "0", "part_montant_pct": "0"},
        {"indicateur": "taux_modification_moyen", "valeur": "0", "montant_eur": "0", "part_montant_pct": "0"},
    ] + nature_rows

    with open(OUT_INDIC, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["indicateur", "valeur", "montant_eur", "part_montant_pct"])
        w.writeheader()
        w.writerows(ind_rows)

    # ---- Rapport console ----
    print("=== MESURES SESN (Phase 3) ===")
    print(f"contrats: {len(rows)} | total: {total} EUR (ref {TOTAL_REF})")
    print(f"SIREN titulaires distincts: {len(ranked)}")
    print(f"CR5: {cr5.quantize(Decimal('0.01'))}% | CR10: {cr10.quantize(Decimal('0.01'))}% | HHI: {hhi.quantize(Decimal('1'))}")
    print("\n=== TOP 10 concentration ===")
    for r in conc_rows[:10]:
        print(f"  {r['rang']}. {r['siren']} {r['nom_rne']}: {r['montant_part_eur']} EUR ({r['part_pct']}%, {r['nb_contrats']} contrats)")
    print("\n=== Procedures ===")
    for p, n in proc.most_common():
        print(f"  {p}: {n} ({proc_montant[p].quantize(Decimal('0.01'))} EUR)")
    print(f"\n=== Candidatures uniques (offres=1) : {nb_cand_unique} ===")
    for r in cand_unique:
        print(f"  {r['id']} | {r['objet'][:70]} | {r['montant']} EUR | {r['procedure']}")
    print("\n=== Repartition par nature (CPV) ===")
    for fam, (nb, m) in sorted(nature_agg.items(), key=lambda kv: -kv[1][1]):
        print(f"  {fam}: {nb} contrats, {m.quantize(Decimal('0.01'))} EUR ({(m/total*100).quantize(Decimal('0.01'))}%)")

    # Hashes
    for p in (OUT_MESURES, OUT_CONC, OUT_INDIC):
        print(f"sha256 {p}: {sha256_file(p)[:16]}...")


if __name__ == "__main__":
    main()
