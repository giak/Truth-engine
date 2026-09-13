import json
p='/mnt/data/inv022_r3/truth-engine-v2_2.10.6-R3P0_CANONICAL/investigations/2026-09/2026-09-06_russie-operations-influence-france/2026-09-06_10-57_russie-operations-influence-france_RUN_STATE.json'
s=json.load(open(p))
rows=[]
for f in s['facts']:
    if f.get('epi')=='FACT' and f.get('tier') in {'✦','✧'}:
        action='ELIGIBLE:CONFIRME' if f['tier']=='✦' else 'ELIGIBLE:VERIFIE'
        rows.append({'fct':f['id'],'action':action,'attempted':0,'success':0,'failure':0,'blocked':1,'reason':'MNEMO_UNAVAILABLE'})
payload={
 'mnemo_row':'FAIL:MNEMO_UNAVAILABLE',
 'self_write_row':'PENDING_AT_SERIALIZATION',
 'writeback_row':{'eligible':len(rows),'attempted':0,'success':0,'failure':0,'blocked':len(rows)},
 'writeback_execution':rows
}
print(json.dumps(payload,ensure_ascii=False))
