#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification independante de la selection des cas Phase 4."""
import csv
from decimal import Decimal

rows = list(csv.DictReader(open("data/decp_sesn_norm.csv", encoding="utf-8")))

def d(r):
    return Decimal(r["montant"]) if r["montant"] else Decimal("0")

print("=== A1 : tous les couples (titulaire x CPV complet) avec >= 2 contrats ===")
couples = {}
for r in rows:
    ss = [s for s in r["titulaires_siren"].split(";") if s]
    for s in ss:
        k = (s, (r["codeCPV"] or "").strip())
        couples.setdefault(k, [Decimal("0"), 0])
        couples[k][0] += d(r) / len(ss)
        couples[k][1] += 1
ranked = sorted([(k, v) for k, v in couples.items() if v[1] >= 2], key=lambda kv: -kv[1][0])
for k, v in ranked[:6]:
    print(f"  {k[0]} | {k[1]} | {v[0]:,.2f} EUR | {v[1]} contrats")
print("  A1 attendu = rang 1 :", ranked[0][0], ranked[0][1], ranked[0][1][0])

print()
print("=== A2 : toutes les offres uniques triees ===")
cu = sorted([r for r in rows if r["offresRecues"] == "1"], key=d, reverse=True)
for r in cu:
    print(f"  {r['id']} | {d(r):>12,.2f} | {r['objet'][:50]}")
print("  A2 attendu = rang 1 :", cu[0]["id"])

print()
print("=== A3 : groupes par famille (offres=1, sans publicite) ===")
from collections import defaultdict
g = defaultdict(list)
for r in rows:
    if r["offresRecues"] == "1" and "sans publicité" in r["procedure"]:
        g[(r["codeCPV"] or "")[:2]].append(r["id"])
for f, ids in sorted(g.items(), key=lambda kv: -len(kv[1])):
    print(f"  famille {f} : {len(ids)} contrats {ids}")
print("  A3 attendu = famille a >= 3 contrats")

rows_by_id = {r["id"]: r for r in rows}
print()
print("=== T1 : pool travaux 3-15 M EUR publicite offres>=3, tri par proximite moyenne A1 ===")
a1_moy = (d(rows_by_id["2950343"]) + d(rows_by_id["2950348"])) / 2
t1 = [r for r in rows
      if (r["codeCPV"] or "").startswith("45")
      and 3_000_000 <= d(r) <= 15_000_000
      and r["procedure"] in ("Procédure avec négociation", "Appel d'offres ouvert")
      and r["offresRecues"].isdigit() and int(r["offresRecues"]) >= 3
      and r["id"] not in ("2950343", "2950348")]
t1s = sorted(t1, key=lambda r: abs(d(r) - a1_moy))
for r in t1s[:5]:
    print(f"  {r['id']} | {d(r):>12,.2f} | offres {r['offresRecues']:>2} | ecart {abs(d(r)-a1_moy):>10,.2f} | {r['objet'][:40]}")
print("  T1 attendu = rang 1 :", t1s[0]["id"])

print()
print("=== T2 : pool services 1-6 M EUR publicite offres>=3, max offres ===")
t2 = [r for r in rows
      if not (r["codeCPV"] or "").startswith("45")
      and 1_000_000 <= d(r) <= 6_000_000
      and r["procedure"] in ("Procédure avec négociation", "Appel d'offres ouvert")
      and r["offresRecues"].isdigit() and int(r["offresRecues"]) >= 3]
t2s = sorted(t2, key=lambda r: -int(r["offresRecues"]))
for r in t2s[:5]:
    print(f"  {r['id']} | {d(r):>12,.2f} | offres {r['offresRecues']:>2} | {r['objet'][:45]}")
print("  T2 attendu = rang 1 :", t2s[0]["id"])
