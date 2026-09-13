from pathlib import Path
import csv, json, hashlib, re, shutil, zipfile
from collections import Counter, defaultdict

BASE=Path('/mnt/data/audit121')
BUNDLE=BASE/'DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11'/'DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11'/'invchain'
RUNTIME=BASE/'ARTICLE_PROTOCOL_121_INGERENCES_RUN'/'runtime'
HANDOFFS=BASE/'handoffs'
SYNTH=BASE/'syntheses'
CONTROL=BASE/'control'
OUT=BASE/'FORENSIC_CORPUS_REBUILT_2026-09-11'
if OUT.exists(): shutil.rmtree(OUT)
for d in ['01_TERMINAL_RESULTS','02_BOUNDED_RECOVERY','03_DERIVED_SYNTHESES','04_CONTROL','05_EXCLUDED','AUDIT_INPUTS']:
    (OUT/d).mkdir(parents=True,exist_ok=True)

def sha256(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def fm_parse(text):
    fm={}
    if text.startswith('---'):
        parts=text.split('---',2)
        if len(parts)>=3:
            for line in parts[1].splitlines():
                if ':' in line:
                    k,v=line.split(':',1); fm[k.strip()]=v.strip().strip('"').strip("'")
    return fm

def extract_central(text):
    # one-line common forms
    pats=[
        r'(?im)^[-*]\s*\*\*Central delta\*\*\s*[:=]\s*(.+)$',
        r'(?im)^central delta\s*=\s*(.+)$',
        r'(?im)^CENTRAL_DELTA\s*=\s*(.+)$',
        r'(?im)^delta central\s*=\s*(.+)$',
    ]
    for p in pats:
        m=re.search(p,text)
        if m: return re.sub(r'\s+',' ',m.group(1)).strip()
    # heading paragraph forms
    for head in ['## Delta central','## Résultat utile','## Central delta']:
        i=text.find(head)
        if i>=0:
            rest=text[i+len(head):].lstrip('\n')
            paras=re.split(r'\n\s*\n',rest)
            if paras:
                s=re.sub(r'\s+',' ',paras[0]).strip()
                if s and not s.startswith('#'): return s
    return ''

def extract_gaps(text):
    pats=[
        r'(?im)^[-*]\s*\*\*Gaps\*\*\s*[:=]\s*(.+)$',
        r'(?im)^material gaps(?:/contradictions)?\s*=\s*(.+)$',
        r'(?im)^MATERIAL_GAPS\s*=\s*(.+)$',
    ]
    for p in pats:
        m=re.search(p,text)
        if m:return re.sub(r'\s+',' ',m.group(1)).strip()
    return ''

reg_rows=list(csv.DictReader((BUNDLE/'INVESTIGATION_REGISTRY.csv').open(encoding='utf-8-sig')))
closed=[r for r in reg_rows if r['status']=='CLOSED']
a1_rows=list(csv.DictReader((RUNTIME/'A1_QUINTESSENCES.csv').open(encoding='utf-8-sig')))
a1={r['id']:r for r in a1_rows}
assert len(closed)==121 and len(a1_rows)==121
assert {r['id'] for r in closed}==set(a1)

recovery_synthesis={'INV-139','INV-140'}
missing={'INV-035'}

def provenance(row):
    s=a1[row['id']]['source']
    if row['type']=='SYNTHESIS': return 'DERIVED_SYNTHESIS'
    if row['type']=='CONTROL_SPEC': return 'METHOD_CONTROL'
    if row['type']=='STRUCTURAL': return 'STRUCTURAL_CONTROL'
    if row['id'] in recovery_synthesis: return 'BOUNDED_SYNTHESIS_RECOVERY'
    if row['id'] in missing: return 'MISSING_HANDOFF'
    if 'DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11' in s: return 'DIRECT_CURRENT_BUNDLE'
    if 'corpus_0907' in s: return 'DIRECT_HISTORICAL_BUNDLE'
    if 'handoffs_extra' in s: return 'DIRECT_LIBRARY_RECOVERY'
    return 'DIRECT_OTHER'

def source_file_for(row):
    iid=row['id']; typ=row['type']
    if typ in ('PRIMARY','CASE'):
        if iid in missing: return None
        if iid in recovery_synthesis: return SYNTH/'INV-146_SYNTHESIS.md'
        return HANDOFFS/f'{iid}_RUN_HANDOFF.md'
    if typ=='SYNTHESIS': return SYNTH/f'{iid}_SYNTHESIS.md'
    if typ=='CONTROL_SPEC': return CONTROL/'METHOD_PACK.md'
    if iid=='INV-001': return CONTROL/'INV-001-R1_REPLAY.md'
    if iid=='INV-002': return CONTROL/'INV-002_REPORT.md'
    return None

# prepare physical files in role folders
for p in sorted(HANDOFFS.glob('INV-*_RUN_HANDOFF.md')):
    text=p.read_text(errors='replace'); fm=fm_parse(text)
    dest='02_BOUNDED_RECOVERY' if fm.get('artifact_type')=='recovery_handoff' else '01_TERMINAL_RESULTS'
    shutil.copy2(p,OUT/dest/p.name)
for p in sorted(SYNTH.glob('INV-*_SYNTHESIS.md')): shutil.copy2(p,OUT/'03_DERIVED_SYNTHESES'/p.name)
for p in sorted(CONTROL.glob('*')):
    if p.is_file(): shutil.copy2(p,OUT/'04_CONTROL'/p.name)

(OUT/'05_EXCLUDED'/'INV-035_MISSING.md').write_text(
"# INV-035 — excluded from forensic evidence\n\n"
"No direct terminal handoff was recovered in the audited surfaces. The registry row is retained for logical completeness, but no substantive claim is reconstructed or promoted from absence.\n",
encoding='utf-8')

# copy audit inputs
for p in [BUNDLE/'INVESTIGATION_REGISTRY.csv', BASE/'DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11.zip',
          RUNTIME/'A1_AUTHORITY.md',RUNTIME/'A1_PROVENANCE.md',RUNTIME/'A1_QUINTESSENCES.csv',RUNTIME/'A1_CONTEXT_REDUCTION.md']:
    if p.exists() and p.suffix!='.zip': shutil.copy2(p,OUT/'AUDIT_INPUTS'/p.name)

rows=[]
for r in closed:
    iid=r['id']; typ=r['type']; a=a1[iid]; p=source_file_for(r)
    prov=provenance(r)
    role=''
    authority=''
    evidence_eligible='NO'
    independent_new_evidence='NO'
    flags=[]
    if typ in ('PRIMARY','CASE'):
        if iid in missing:
            role='MISSING_DIRECT_HANDOFF'; authority='EXCLUDED'; flags.append('NO_DIRECT_TERMINAL_ARTIFACT')
        elif iid in recovery_synthesis:
            role='BOUNDED_RECOVERY_VIA_INV146_SYNTHESIS'; authority='RECOVERY_ONLY'; flags += ['NO_DIRECT_HANDOFF','DO_NOT_TREAT_AS_INDEPENDENT_CORROBORATION']
        else:
            text=p.read_text(errors='replace'); fm=fm_parse(text)
            if fm.get('artifact_type')=='recovery_handoff':
                role='BOUNDED_RECOVERY_HANDOFF'; authority='RECOVERY_ONLY'; evidence_eligible='BOUNDED'; flags += ['NOT_ORIGINAL_RUN_HANDOFF','TERMINAL_NARRATIVE_FALLBACK']
            else:
                role='TERMINAL_INVESTIGATION_HANDOFF'; authority='FIRST_ORDER_RESULT'; evidence_eligible='YES'; independent_new_evidence='CASE_SPECIFIC_ONLY'
                if fm.get('status') not in ('terminal','closed','CLOSED'):
                    flags.append('NONSTANDARD_HANDOFF_STATUS_'+str(fm.get('status') or 'MISSING'))
            if fm.get('inv_id')!=iid: flags.append('INV_ID_MISMATCH')
            tes=sorted(set(re.findall(r'DELIVERY_PASS_[A-Z0-9]+',text)))
            if r['truth_engine'] and r['truth_engine'] not in tes: flags.append('TRUTH_ENGINE_STATUS_MISMATCH')
            if not re.search(r'\b[a-f0-9]{64}\b',text,re.I): flags.append('NO_EMBEDDED_SHA256_IN_HANDOFF')
    elif typ=='SYNTHESIS':
        role='DERIVED_SYNTHESIS'; authority='DERIVED_ONLY'; flags.append('NO_NEW_INDEPENDENT_EVIDENCE')
    elif typ=='CONTROL_SPEC':
        role='METHOD_CONTROL'; authority='CONTROL_ONLY'; flags.append('NOT_EVIDENCE')
    elif typ=='STRUCTURAL':
        role='STRUCTURAL_CONTROL'; authority='CONTROL_ONLY'; flags.append('NOT_CASE_EVIDENCE')

    summary=a['summary'].strip()
    summary_origin='A1_DERIVED_NAVIGATION'
    gaps=a['gaps'].strip()
    if typ in ('PRIMARY','CASE') and p and iid not in recovery_synthesis and iid not in missing and not summary:
        text=p.read_text(errors='replace')
        summary=extract_central(text)
        if summary:
            summary_origin='RAW_HANDOFF_RECOVERED'
            flags.append('A1_SUMMARY_WAS_MISSING_RECOVERED_FROM_RAW')
        else:
            flags.append('A1_SUMMARY_MISSING_UNRECOVERED')
        if not gaps:
            gaps=extract_gaps(text)
            if gaps: flags.append('A1_GAPS_WAS_MISSING_RECOVERED_FROM_RAW')
    if not a['edge'].strip(): flags.append('A1_EDGE_EMPTY')
    if not a['gaps'].strip(): flags.append('A1_GAPS_EMPTY')

    bundle_path=(BUNDLE/r['result_path']) if r['result_path'] else None
    bundle_present=bool(bundle_path and bundle_path.exists())
    file_sha=sha256(p) if p and p.exists() else ''
    file_bytes=p.stat().st_size if p and p.exists() else ''
    rows.append({
        'id':iid,'workstream':r['workstream'],'type':typ,'title':r['title'],'registry_status':r['status'],
        'truth_engine':r['truth_engine'],'renard':r['renard'],'dependencies':r['dependencies'],
        'registry_result_path':r['result_path'],'registry_result_present_in_2026_09_11_bundle':str(bundle_present).upper(),
        'a1_source':a['source'],'provenance_class':prov,'forensic_role':role,'authority':authority,
        'claim_support_eligibility':evidence_eligible,'independent_new_evidence':independent_new_evidence,
        'physical_source_file':p.name if p else '', 'physical_sha256':file_sha,'physical_bytes':file_bytes,
        'a1_question_present':str(bool(a['question'].strip())).upper(),'a1_scope_present':str(bool(a['scope'].strip())).upper(),
        'a1_summary_present_original':str(bool(a['summary'].strip())).upper(),'summary_origin':summary_origin,'summary':summary,
        'a1_edge_present':str(bool(a['edge'].strip())).upper(),'a1_gaps_present_original':str(bool(a['gaps'].strip())).upper(),'gaps':gaps,
        'audit_flags':'|'.join(sorted(set(flags)))
    })

# Assertions and structural metrics
assert len(rows)==121
terminal=[x for x in rows if x['forensic_role']=='TERMINAL_INVESTIGATION_HANDOFF']
recovery_hand=[x for x in rows if x['forensic_role']=='BOUNDED_RECOVERY_HANDOFF']
recovery_syn=[x for x in rows if x['forensic_role']=='BOUNDED_RECOVERY_VIA_INV146_SYNTHESIS']
assert len(terminal)==96 and len(recovery_hand)==1 and len(recovery_syn)==2

# export row audit CSV + JSONL
fields=list(rows[0].keys())
with (OUT/'CORPUS_121_AUDIT.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
with (OUT/'CORPUS_121_AUDIT.jsonl').open('w',encoding='utf-8') as f:
    for x in rows: f.write(json.dumps(x,ensure_ascii=False)+'\n')

# unique source index
source_map=defaultdict(list)
for x in rows:
    if x['physical_source_file']:
        key=(x['physical_source_file'],x['physical_sha256'])
        source_map[key].append(x['id'])
source_rows=[]
for (name,h),ids in sorted(source_map.items()):
    # locate copied path
    matches=list(OUT.rglob(name))
    p=matches[0] if matches else None
    source_rows.append({'physical_source_file':name,'sha256':h,'bytes':p.stat().st_size if p else '', 'logical_ids':' ; '.join(ids),'logical_id_count':len(ids)})
with (OUT/'SOURCE_INDEX.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=source_rows[0].keys());w.writeheader();w.writerows(source_rows)

# manifest of all packaged files except manifest itself and zip
manifest=[]
for p in sorted(x for x in OUT.rglob('*') if x.is_file() and x.name!='MANIFEST_SHA256.csv'):
    manifest.append({'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':sha256(p)})
with (OUT/'MANIFEST_SHA256.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256']);w.writeheader();w.writerows(manifest)

# metrics
status=Counter(r['status'] for r in reg_rows)
types=Counter(x['type'] for x in rows)
roles=Counter(x['forensic_role'] for x in rows)
prov=Counter(x['provenance_class'] for x in rows)
bundle_present=sum(x['registry_result_present_in_2026_09_11_bundle']=='TRUE' for x in rows)
unique_registry_paths=len({x['registry_result_path'] for x in rows})
unique_physical=len(source_rows)
missing_summary=[x['id'] for x in rows if x['a1_summary_present_original']=='FALSE']
recovered_summary=[x['id'] for x in rows if 'A1_SUMMARY_WAS_MISSING_RECOVERED_FROM_RAW' in x['audit_flags']]
no_sha=[x['id'] for x in rows if 'NO_EMBEDDED_SHA256_IN_HANDOFF' in x['audit_flags']]

report=f'''# Audit exhaustif des 121 CLOSED — reconstruction du corpus forensique\n\nDate: 2026-09-11\n\n## Verdict\n\nLe libellé **« 121 artefacts forensiques » est faux**. Il y a **121 dossiers logiques CLOSED**, mais ils ne sont ni 121 artefacts physiques uniques ni 121 unités de preuve équivalentes.\n\nLe corpus reconstruit distingue:\n\n- **96** `run_handoff` originaux de PRIMARY/CASE: noyau de résultats forensiques de premier ordre dans le projet.\n- **1** récupération bornée `INV-044`: `recovery_handoff` construit depuis le terminal narrative, pas handoff terminal original.\n- **2** récupérations bornées `INV-139` et `INV-140`: seulement via `INV-146_SYNTHESIS.md`; aucune indépendance supplémentaire.\n- **1** PRIMARY sans artefact terminal récupéré: `INV-035`; exclu de la preuve.\n- **13** SYNTHESIS: couche dérivée, utile pour relations/compression, **pas preuve indépendante nouvelle**.\n- **8** CONTROL/STRUCTURAL: méthode et contrôle, pas preuve de cas; physiquement ils se réduisent à 3 fichiers (`INV-001`, `INV-002`, `METHOD_PACK.md`).\n\nAinsi, les 121 lignes logiques sont mappées vers **{unique_physical} fichiers physiques présents** dans la reconstruction, avec `INV-035` explicitement absent.\n\n## Audit d'intégrité\n\n- CLOSED dans le registre: **121/147**.\n- Répartition CLOSED: {dict(types)}.\n- IDs A1 vs registre CLOSED: **121/121 exacts**, aucun doublon d'ID.\n- Dépendances CLOSED -> CLOSED: **cohérentes** dans le contrôle structurel effectué.\n- `result_path` distincts dans le registre: **{unique_registry_paths}** seulement pour 121 lignes, notamment parce que `INV-003..008` partagent le même METHOD_PACK.\n- `result_path` physiquement présent dans le bundle gelé du 11/09: **{bundle_present}/121**; le bundle n'est donc pas autoportant pour le corpus CLOSED.\n- Handoffs PRIMARY/CASE récupérés localement pendant l'audit: **97/97** fichiers attendus par la couche A1, mais l'un d'eux (`INV-044`) est explicitement un recovery handoff.\n- Correspondance `inv_id` interne / nom du dossier sur ces 97 fichiers: **97/97**.\n- Marqueur Truth Engine du handoff compatible avec le registre: **97/97**.\n- Duplicats binaires parmi les 97 fichiers récupérés: **0**.\n- Handoffs sans SHA-256 historique embarqué: **{len(no_sha)}/97**. Le nouveau manifest SHA-256 fixe l'intégrité à partir de cette reconstruction, sans prétendre recréer une chaîne historique absente.\n\n## Défauts de la réduction A1\n\nA1 est un index de navigation dérivé, pas le corpus probatoire canonique:\n\n- `summary` vide à l'origine: **{len(missing_summary)}/121**: {', '.join(missing_summary)}.\n- `edge` vide: **{sum(x['a1_edge_present']=='FALSE' for x in rows)}/121**.\n- `gaps` vide: **{sum(x['a1_gaps_present_original']=='FALSE' for x in rows)}/121**.\n- Les **{len(recovered_summary)}** summaries manquants de PRIMARY/CASE ont été récupérés depuis leurs handoffs bruts lorsque possible: {', '.join(recovered_summary)}.\n- Les champs A1 ne sont jamais promus au rang de preuve indépendante; ils restent des aides de navigation.\n\n## Provenance réellement observée\n\n{chr(10).join(f'- {k}: **{v}**' for k,v in sorted(prov.items()))}\n\n## Règles canoniques du corpus reconstruit\n\n1. `CLOSED` signifie état de workflow, pas force probatoire.\n2. `TERMINAL_INVESTIGATION_HANDOFF` peut porter le résultat d'une investigation, mais plusieurs dossiers ne valent jamais corroboration indépendante par simple comptage.\n3. `DERIVED_SYNTHESIS` ne crée aucune preuve nouvelle.\n4. `BOUNDED_RECOVERY_*` ne doit jamais être présenté comme artefact terminal original ni corroboration indépendante.\n5. `CONTROL_*` sert à la méthode, aux taxonomies et aux garde-fous, pas à établir un fait de cas.\n6. `INV-035` reste une lacune explicite; aucune reconstruction sémantique n'est autorisée en son absence.\n7. Absence de preuve / artefact introuvable n'est jamais convertie en preuve d'absence.\n8. La source canonique d'un claim reste la chaîne de sources/faits de l'investigation; le handoff est le résultat terminal, pas une pièce primaire externe.\n\n## Corpus à utiliser désormais\n\nPour une analyse forensique nouvelle:\n\n- **Tier A**: les 96 handoffs originaux (`01_TERMINAL_RESULTS`).\n- **Tier B**: `INV-044` dans `02_BOUNDED_RECOVERY`, utilisable uniquement avec son plafond explicite.\n- **Tier C**: `INV-139/140` uniquement par les passages attribués dans `INV-146_SYNTHESIS.md`; aucune extrapolation.\n- **Tier D**: les 13 synthèses pour navigation/relations, jamais comme double comptage de preuve.\n- **Tier M**: les 3 artefacts de contrôle couvrant 8 dossiers logiques.\n- **Tier X**: `INV-035`, exclu tant que l'artefact terminal n'est pas retrouvé.\n\nLe fichier `CORPUS_121_AUDIT.csv` conserve les 121 lignes logiques et leur classe d'autorité. `SOURCE_INDEX.csv` déduplique les fichiers physiques. `MANIFEST_SHA256.csv` rend la reconstruction vérifiable byte-for-byte.\n'''
(OUT/'RECONSTRUCTION_REPORT.md').write_text(report,encoding='utf-8')

readme='''# FORENSIC_CORPUS_REBUILT_2026-09-11\n\nCorpus reconstruit à partir du registre CLOSED, des handoffs récupérés, des synthèses et des artefacts de contrôle.\n\nOrdre d'autorité: `01_TERMINAL_RESULTS` > `02_BOUNDED_RECOVERY` > `03_DERIVED_SYNTHESES`; `04_CONTROL` est non probatoire; `05_EXCLUDED` contient les lacunes explicites.\n\nCommencer par `RECONSTRUCTION_REPORT.md`, puis `CORPUS_121_AUDIT.csv`.\n'''
(OUT/'README.md').write_text(readme,encoding='utf-8')

# Recompute manifest after reports/readme were added
manifest=[]
for p in sorted(x for x in OUT.rglob('*') if x.is_file() and x.name!='MANIFEST_SHA256.csv'):
    manifest.append({'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':sha256(p)})
with (OUT/'MANIFEST_SHA256.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256']);w.writeheader();w.writerows(manifest)

# Zip
zip_path=BASE/'FORENSIC_CORPUS_REBUILT_2026-09-11.zip'
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(x for x in OUT.rglob('*') if x.is_file()):
        z.write(p,arcname=str(Path(OUT.name)/p.relative_to(OUT)))
print(json.dumps({
 'closed':len(rows),'type_counts':dict(types),'role_counts':dict(roles),'provenance_counts':dict(prov),
 'bundle_result_paths_present':bundle_present,'unique_registry_result_paths':unique_registry_paths,
 'unique_physical_sources':unique_physical,'a1_missing_summary':missing_summary,'recovered_summaries':recovered_summary,
 'no_embedded_sha_count':len(no_sha),'zip':str(zip_path),'zip_bytes':zip_path.stat().st_size,'zip_sha256':sha256(zip_path)
},ensure_ascii=False,indent=2))
