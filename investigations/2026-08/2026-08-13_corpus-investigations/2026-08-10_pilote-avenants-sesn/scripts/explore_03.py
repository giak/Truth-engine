#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exploration des distributions de decp_sesn_norm.csv (Phase 3, avant écriture du script 03).
Usage : python3 scripts/explore_03.py
"""
import csv
from collections import Counter
from decimal import Decimal

PATH = "data/decp_sesn_norm.csv"

rows = list(csv.DictReader(open(PATH, encoding="utf-8")))
print("lignes:", len(rows))

# Montant total
tot = sum(Decimal(r["montant"]) for r in rows if r["montant"])
print("montant total:", tot)

print()
print("=== nature ===")
for k, v in Counter(r["nature"] for r in rows).most_common():
    print(f"  {k!r}: {v}")

print()
print("=== procedure ===")
for k, v in Counter(r["procedure"] for r in rows).most_common():
    print(f"  {k!r}: {v}")

print()
print("=== offresRecues ===")
for k, v in Counter(r["offresRecues"] for r in rows).most_common():
    print(f"  {k!r}: {v}")

print()
print("=== offresRecues vides ? ===")
print("  vides:", sum(1 for r in rows if not r["offresRecues"]))
print("  '1' (candidature unique):", sum(1 for r in rows if r["offresRecues"] == "1"))

print()
print("=== _type ===")
for k, v in Counter(r["_type"] for r in rows).most_common():
    print(f"  {k!r}: {v}")

print()
print("=== typeGroupementOperateurs ===")
for k, v in Counter(r["typeGroupementOperateurs"] for r in rows).most_common():
    print(f"  {k!r}: {v}")

print()
print("=== modifications (champ non vide ?) ===")
nonvide = [r for r in rows if r.get("modifications", "").strip()]
print("  lignes avec modifications non vide:", len(nonvide))
for r in nonvide[:5]:
    print("  ex:", r["id"], "|", r["modifications"][:150])

print()
print("=== source ===")
for k, v in Counter(r["source"] for r in rows).most_common():
    print(f"  {k!r}: {v}")

print()
print("=== titulaires (SIREN multi-valeurs) ===")
multi = [r for r in rows if ";" in r.get("titulaires_siren", "")]
print("  lignes a plusieurs titulaires:", len(multi))
for r in multi[:6]:
    print("  ex:", r["id"], "|", r["titulaires_siren"])

print()
print("=== Top SIREN titulaires par montant cumule ===")
agg = Counter()
by_siren = {}
for r in rows:
    if not r["montant"]:
        continue
    sirens = [s for s in r["titulaires_siren"].split(";") if s]
    n = len(sirens)
    m = Decimal(r["montant"]) / n if n else Decimal(0)
    for s in sirens:
        agg[s] += m
        by_siren.setdefault(s, {"nom": "", "nb": 0})
        by_siren[s]["nb"] += 1

for s, m in agg.most_common(20):
    print(f"  {s}: {m} EUR (sur {by_siren[s]['nb']} lignes)")

print()
print("=== codeCPV premiers chiffres (famille) ===")
fam = Counter((r["codeCPV"][:2] if r["codeCPV"] else "??") for r in rows)
for k, v in fam.most_common():
    print(f"  {k}: {v}")

print()
print("=== exemples d'objets pour calibration familles CPV ===")
for r in rows[:10]:
    print(f"  {r['id']} | CPV {r['codeCPV']} | {r['objet'][:90]}")
