#!/usr/bin/env python3
import csv, collections, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
rows=list(csv.DictReader(open(root/'INVESTIGATION_REGISTRY.csv',encoding='utf-8')))
def C(field): return collections.Counter(r.get(field,'') for r in rows)
def table(c): return '\n'.join(f'| {k or "(vide)"} | {v} |' for k,v in sorted(c.items()))
blocked=[r for r in rows if r['status']=='BLOCKED']
backlog=[r for r in rows if r['status']=='BACKLOG']
review=[r for r in blocked if r['dependencies']=='HUMAN_REVIEW_INV-002']
parts=['# DASHBOARD — Investigation Control v0.5','', '> Généré depuis `INVESTIGATION_REGISTRY.csv`. Ne pas éditer manuellement.','', '## Gate courant','', '**HOLD — revue humaine INV-002 requise.** Aucun Truth Engine suivant n’est lancé automatiquement.','', '## Synthèse','', f'- Total entrées : **{len(rows)}**', f'- CLOSED : **{sum(r["status"]=="CLOSED" for r in rows)}**', f'- BLOCKED : **{len(blocked)}**', f'- BACKLOG : **{len(backlog)}**', f'- DEFERRED : **{sum(r["status"]=="DEFERRED" for r in rows)}**','', '## Couverture corpus courante','', '| Couverture | N |','|---|---:|', table(C('coverage_current')),'', '## Décisions','', '| Décision | N |','|---|---:|', table(C('decision')),'', '## P0 bloqués par revue INV-002','', '| ID | Couverture | Sujet |','|---|---|---|']
for r in review: parts.append(f'| {r["id"]} | {r.get("coverage_current","")} | {r["title"]} |')
parts += ['', '## Nouveaux gaps INV-002','', '| ID | Priorité | Couverture | Sujet |','|---|---|---|---|']
for r in rows:
    try: n=int(r['id'].split('-')[1])
    except: continue
    if n>=125: parts.append(f'| {r["id"]} | {r["priority"]} | {r.get("coverage_current","")} | {r["title"]} |')
parts += ['', '## Artefacts de la dernière étape','', '- `INV-002/INV-002_REPORT.md`','- `INV-002/INV-002_CORPUS_MAP.csv`','- `INV-002/INV-002_INVESTIGATION_COVERAGE.csv`','- `INV-002/INV-002_COVERAGE_CHANGES.csv`','- `INV-002/INV-002_THEME_MATRIX.csv`']
(root/'DASHBOARD.md').write_text('\n'.join(parts)+'\n',encoding='utf-8')
