#!/usr/bin/env python3
import csv, pathlib, sys, datetime
root = pathlib.Path(__file__).resolve().parents[2]
reg = root/'INVESTIGATION_REGISTRY.csv'
tpl = (pathlib.Path(__file__).resolve().parents[1]/'RUN_CARD_TEMPLATE.md').read_text(encoding='utf-8')
if len(sys.argv) != 2:
    raise SystemExit('usage: build_run_card.py INV-010')
inv_id=sys.argv[1]
rows=list(csv.DictReader(reg.open(encoding='utf-8')))
row=next((r for r in rows if r['id']==inv_id),None)
if not row: raise SystemExit(f'unknown INV_ID: {inv_id}')
if row.get('item_type') not in {'PRIMARY','CASE'}: raise SystemExit(f'not directly runnable: {row.get("item_type")}')
if row.get('status') in {'MERGED','DEFERRED','CONDITIONAL','CLOSED'}: raise SystemExit(f'not runnable status: {row.get("status")}')
vals={
 'INV_ID': row['id'], 'TITLE': row['title'], 'ITEM_TYPE': row.get('item_type') or 'PRIMARY',
 'EXECUTION_MODE': row.get('execution_mode') or 'DEEPEN', 'COVERAGE_CURRENT': row.get('coverage_current') or 'UNKNOWN',
 'CORPUS_REFS': row.get('corpus_refs') or 'NONE', 'PARENT_ID': row.get('parent_id') or 'NONE',
 'DEPENDENCIES': row.get('dependencies') or 'NONE', 'AS_OF': datetime.date.today().isoformat(), 'SCOPE_NOTE': 'NONE'
}
for k,v in vals.items(): tpl=tpl.replace('{{'+k+'}}',v)
print(tpl)
