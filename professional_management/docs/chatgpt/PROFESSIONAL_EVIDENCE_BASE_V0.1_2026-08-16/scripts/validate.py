#!/usr/bin/env python3
from pathlib import Path
import csv, sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data"

def rows(name):
    with open(D/name, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

sources = rows("sources.csv")
claims = rows("claims.csv")
edges = rows("evidence_edges.csv")
metrics = rows("metrics.csv")
decisions = rows("decisions.csv")

errors = []
warnings = []

def unique(rs, key):
    vals = [r[key] for r in rs]
    dup = [v for v,c in Counter(vals).items() if c > 1]
    if dup:
        errors.append(f"{key}: duplicate IDs {dup}")

unique(sources,"source_id")
unique(claims,"claim_id")
unique(edges,"edge_id")
unique(metrics,"metric_id")
unique(decisions,"decision_id")

sids = {r["source_id"] for r in sources}
cids = {r["claim_id"] for r in claims}

for e in edges:
    if e["source_id"] not in sids:
        errors.append(f"{e['edge_id']}: unknown source {e['source_id']}")
    if e["claim_id"] not in cids:
        errors.append(f"{e['edge_id']}: unknown claim {e['claim_id']}")

support_by_claim = Counter(e["claim_id"] for e in edges if e["relation"] in {"SUPPORTS","PARTIALLY_SUPPORTS"})
for c in claims:
    if c["commercial_value"] == "HIGH" and support_by_claim[c["claim_id"]] == 0:
        warnings.append(f"{c['claim_id']}: HIGH without supporting edge")
    if c["publicability"] == "YES" and c["epistemic_status"] in {"UNSUPPORTED","UNKNOWN","CONFLICTED"}:
        errors.append(f"{c['claim_id']}: public YES with status {c['epistemic_status']}")

print(f"sources={len(sources)} claims={len(claims)} edges={len(edges)} metrics={len(metrics)} decisions={len(decisions)}")
if warnings:
    print("WARNINGS:")
    for x in warnings: print(" -", x)
if errors:
    print("ERRORS:")
    for x in errors: print(" -", x)
    sys.exit(1)
print("OK")
