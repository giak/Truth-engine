#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification des P1 signales par la revue sur la Phase 3."""
import csv
from decimal import Decimal

rows = list(csv.DictReader(open("data/decp_sesn_norm.csv", encoding="utf-8")))

print("=== 1. Somme des candidatures uniques (offresRecues == '1') ===")
cu = [r for r in rows if r["offresRecues"] == "1"]
total_cu = sum(Decimal(r["montant"]) for r in cu)
print("nb:", len(cu))
for r in cu:
    print("  ", r["id"], "|", r["objet"][:55], "|", r["montant"], "|", r["procedure"])
print("SOMME CANDIDATURES UNIQUES:", total_cu)
tot = sum(Decimal(r["montant"]) for r in rows)
print("part pct:", (total_cu / tot * 100).quantize(Decimal("0.01")))

print()
print("=== 2. Valeur ecrite dans indicateurs_sesn.csv ===")
for r in csv.DictReader(open("data/indicateurs_sesn.csv", encoding="utf-8")):
    if "candidatures" in r["indicateur"] or "CR5" in r["indicateur"] or "HHI" in r["indicateur"]:
        print("  ", r["indicateur"], "=", r["valeur"], "|", r["montant_eur"], "|", r["part_montant_pct"])

print()
print("=== 3. CR5 sans SMDA (remplacement par rang 6 = Ets Renard) ===")
agg = {}
for r in rows:
    m = Decimal(r["montant"])
    ss = [s for s in r["titulaires_siren"].split(";") if s]
    part = m / len(ss)
    for s in ss:
        agg[s] = agg.get(s, Decimal("0")) + part
ranked = sorted(agg.items(), key=lambda kv: -kv[1])
cr5 = sum(v for _, v in ranked[:5]) / tot * 100
print("CR5 actuel:", cr5.quantize(Decimal("0.01")), "%")
print("Top 5:", [(s, (v/tot*100).quantize(Decimal("0.01"))) for s, v in ranked[:5]])
# sans SMDA 378998363 : prendre rang 1,3,4,5,6
sans_smda = [v for s, v in ranked if s != "378998363"][:5]
cr5_sans = sum(sans_smda) / tot * 100
print("CR5 sans SMDA (top 5 hors SMDA):", cr5_sans.quantize(Decimal("0.01")), "%")
