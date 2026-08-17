#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exploration Phase 4 : liste complete des contrats (trie par montant),
groupes par nature CPV, et candidats temoins objectifs. Usage : python3 scripts/explore_04.py
"""
import csv
from decimal import Decimal

rows = list(csv.DictReader(open("data/decp_sesn_norm.csv", encoding="utf-8")))
rows = sorted(rows, key=lambda r: Decimal(r["montant"]), reverse=True)

print(f"=== TOP 15 contrats par montant ({len(rows)} au total) ===")
for r in rows[:15]:
    print(f"  {r['id']:>12} | {Decimal(r['montant']):>14,.2f} | CPV {r['codeCPV'][:8]:8} | offres {r['offresRecues']:>2} | {r['procedure'][:40]:40} | {r['titulaires_siren'][:25]:25} | {r['objet'][:45]}")

print()
print("=== Contrats par nature CPV (famille) ===")
from collections import OrderedDict
fam = OrderedDict()
for r in rows:
    c = (r["codeCPV"] or "")[:2]
    fam.setdefault(c, [])
    fam[c].append(r)
for c, lst in fam.items():
    tot = sum(Decimal(r["montant"]) for r in lst)
    print(f"  CPV {c}: {len(lst)} contrats, {tot:,.2f} EUR")
    for r in lst:
        print(f"      {r['id']:>12} | {Decimal(r['montant']):>14,.2f} | offres {r['offresRecues']:>2} | {r['procedure'][:35]:35} | {r['titulaires_siren'][:22]} | {r['objet'][:40]}")

print()
print("=== Tous les contrats >= 1 M EUR avec offres >= 3 (candidats temoins) ===")
for r in rows:
    m = Decimal(r["montant"])
    if m >= 1_000_000 and r["offresRecues"].isdigit() and int(r["offresRecues"]) >= 3:
        print(f"  {r['id']:>12} | {m:>14,.2f} | offres {r['offresRecues']:>2} | {r['procedure'][:35]:35} | CPV {r['codeCPV'][:8]} | {r['titulaires_siren'][:22]} | {r['objet'][:45]}")

print()
print("=== Details des candidats signales Phase 3 ===")
for r in rows:
    if r["id"] in ("2950343", "2950348", "2706994", "2707054", "2707074") or "Ribécourt" in r["objet"] or "Ribecourt" in r["objet"]:
        print(f"  {r['id']:>12} | {Decimal(r['montant']):>14,.2f} | offres {r['offresRecues']:>2} | {r['procedure'][:40]:40} | {r['titulaires_siren']} | {r['objet']}")
        print(f"            dateNotification={r['dateNotification']} dureeMois={r['dureeMois']} formePrix={r['formePrix']} CPV={r['codeCPV']} lieu={r['lieuExecution_code']} source={r['source']}")
