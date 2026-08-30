import importlib.util, json, subprocess, sys, tempfile, unittest, hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent; CLI=HERE/'run_state.py'; VERIFY=HERE.parent/'verify'/'verify.py'
ALWAYS=["definitions/SYMBOLS.md","definitions/PATTERNS.md","definitions/THREATS.md","forensic/GATES.md","forensic/REQUEST_LOG.md"]
REPORT_SECTIONS=[
 "TEMPORAL_STATE","MANIPULATION_REPORT","SCOPING_REPORT","CREDO","COGNITIVE_MAP","DIALECTICAL_MAP",
 "RESOURCE_FLOW_MAP","ACTOR_NETWORK_MAP","IMPACT_MAP","CONTRADICTION_LEDGER","VERIFICATION_REPORT",
 "EDI_REPORT","RESPONSIBILITY_MAP","NEXT_QUERIES",
]

class T(unittest.TestCase):
 def setUp(self):
  self.td=tempfile.TemporaryDirectory(); self.root=Path(self.td.name)
  self.run_id='20260828-0900-test'; self.asof='2026-08-28'; self.slug='test'
  paths=json.loads(self.cli('paths','--run-id',self.run_id,'--as-of',self.asof,'--subject-slug',self.slug,'--truth-engine-root',str(self.root)).stdout)
  self.paths={k:Path(v) for k,v in paths.items()}; self.state=self.paths['state_path']
  self.cli('init','--state',str(self.state),'--run-id',self.run_id,'--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','INLINE_UNSTABLE','--subject-slug',self.slug,'--truth-engine-root',str(self.root),'--complexity','SIMPLE','--complexity-score','2')
  self.cli('archive-input','--state',str(self.state),'--text','same supplied claim')
  self.cli('record-sys','--state',str(self.state),'--result','FOUND','--tool','mnemolite','--ref','-','--call','MNEMO_Q')
  self.cli('memory-probe','--state',str(self.state),'--status','NONE')
  self.cli('set-run','--state',str(self.state),'--json',json.dumps({'scope':'bounded','loaded_modules':ALWAYS}))
  for name in REPORT_SECTIONS: self.cli('set-section','--state',str(self.state),'--name',name,'--json','[]')
  src=self.root/'draft.md'; src.write_text('# Investigation\n\n## Résumé\nTexte.\n'); self.cli('write-narrative','--state',str(self.state),'--source-file',str(src))
 def tearDown(self): self.td.cleanup()
 def cli(self,*a,ok=True,input=None):
  p=subprocess.run([sys.executable,str(CLI),*a],text=True,input=input,capture_output=True,cwd=self.root)
  if ok and p.returncode: self.fail(f'{a}\nSTDOUT={p.stdout}\nSTDERR={p.stderr}')
  return p
 def obj(self,kind,status='SATURATED',**extra):
  payload={'status':status,'text':'x',**extra}; out=self.cli('record-object','--state',str(self.state),'--kind',kind,'--json',json.dumps(payload)).stdout
  return out.split('ids=')[-1].strip().split(',')[0]
 def semantic_min(self): self.obj('LED'); self.obj('AXS'); self.obj('CLM'); self.obj('CAU')
 def evidence(self,hydrate=False):
  if hydrate:
   d=json.loads(self.state.read_text()); fp=d['run']['subject_fingerprint']
   snap=self.root/'prior.json'; snap.write_text(json.dumps({'snapshot_schema':1,'engine':'2.10.5','run_id':'old-run','as_of':'2026-08-27','subject_slug':'old-slug','subject_fingerprint':fp,'input_sha256':'sha256:x','facts':[{'key':'fact','value':'bounded','tier':'✦','epi':'FACT','url':'https://example.org/a','families':['A','D'],'memory_id':'mem-old','verified_at':'2026-08-27','origin_run_id':'old-run'}],'gaps':[]}))
   self.cli('hydrate','--state',str(self.state),'--snapshot',str(snap),'--memory-id','snapshot-mem'); self.cli('delta','--state',str(self.state),'--key','fact','--class','REUSE','--reason','stable')
  a=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.org/a','--query','a','--accept-source','--role','◈','--family','A').stdout.split()
  b=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.net/b','--query','b','--accept-source','--role','◉','--family','D').stdout.split()
  q=self.cli('record-query','--state',str(self.state),'--mode','WEB','--result','NO_RESULT','--query','REFUTATION fact: counter-evidence search').stdout.strip()
  f=self.cli('record-fact','--state',str(self.state),'--epi','FACT','--tier','✦','--url','https://example.org/a','--sources',f'{a[1]},{b[1]}','--date','2026-08-28','--subject','fact','--value','bounded').stdout.strip()
  self.cli('record-refutation','--state',str(self.state),'--fct',f,'--qry',q,'--status','NONE'); return f
 def cps(self):
  for lab,last,nxt in [('SCOPE','7','9'),('SEARCH:AXS-001','9:AXS-001','10'),('FACTS','10','11'),('CAUSAL_GAP','11','13'),('VERIFY','13','17'),('INVESTIGATION_ACCOUNTABILITY','17','18')]: self.cli('checkpoint','--state',str(self.state),'--label',lab,'--last-completed',last,'--next-action',nxt)
 def finalize_pre(self,hydrate=False):
  self.semantic_min(); f=self.evidence(hydrate=hydrate); self.cps(); gates={f'G{i}':'PASS' for i in range(11)}; self.cli('set-gates','--state',str(self.state),'--json',json.dumps(gates)); self.cli('mark-final','--state',str(self.state)); self.cli('validate','--state',str(self.state),'--phase','pre'); self.cli('render','--state',str(self.state),'--phase','pre'); return f,self.paths['investigation_path']

 def test_paths_colocated(self):
  d=json.loads(self.state.read_text()); rd=Path(d['run']['run_dir']);
  for k in ('state_path','narrative_path','snapshot_path','investigation_path','certification_path','input_path'): self.assertEqual(Path(d['run'][k]).parent,rd)
  self.assertTrue(Path(d['run']['input_path']).exists())

 def test_subject_fingerprint_stable_same_text(self):
  d=json.loads(self.state.read_text()); fp=d['run']['subject_fingerprint']; self.assertTrue(fp.startswith('sha256:'))
  other=self.root/'other'; paths=json.loads(self.cli('paths','--run-id','20260828-0901-other','--as-of',self.asof,'--subject-slug','other','--truth-engine-root',str(other)).stdout); st=Path(paths['state_path'])
  self.cli('init','--state',str(st),'--run-id','20260828-0901-other','--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','INLINE_UNSTABLE','--subject-slug','other','--truth-engine-root',str(other),'--complexity','SIMPLE','--complexity-score','2'); self.cli('archive-input','--state',str(st),'--text','  same   supplied\nclaim  ')
  self.assertEqual(fp,json.loads(st.read_text())['run']['subject_fingerprint'])

 def test_subject_fingerprint_typographic_equivalence_raw_sha_distinct(self):
  root2=self.root/'typo'; paths=json.loads(self.cli('paths','--run-id','20260828-0903-typo','--as-of',self.asof,'--subject-slug','typo','--truth-engine-root',str(root2)).stdout); st=Path(paths['state_path'])
  self.cli('init','--state',str(st),'--run-id','20260828-0903-typo','--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','PENDING','--subject-slug','typo','--truth-engine-root',str(root2),'--complexity','SIMPLE','--complexity-score','2')
  self.cli('archive-input','--state',str(st),'--text','d’un pays — «texte» …')
  root3=self.root/'ascii'; paths3=json.loads(self.cli('paths','--run-id','20260828-0904-ascii','--as-of',self.asof,'--subject-slug','ascii','--truth-engine-root',str(root3)).stdout); st3=Path(paths3['state_path'])
  self.cli('init','--state',str(st3),'--run-id','20260828-0904-ascii','--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','INLINE_UNSTABLE','--subject-slug','ascii','--truth-engine-root',str(root3),'--complexity','SIMPLE','--complexity-score','2')
  self.cli('archive-input','--state',str(st3),'--text','d\'un pays - "texte" ...')
  a=json.loads(st.read_text())['run']; b=json.loads(st3.read_text())['run']
  self.assertEqual(a['subject_fingerprint'],b['subject_fingerprint'])
  self.assertNotEqual(a['input_sha256'],b['input_sha256'])
  self.assertEqual(a['original_input_ref'],'INLINE_UNSTABLE')

 def test_2104_legacy_v1_snapshot_bridge(self):
  root2=self.root/'bridge'; paths=json.loads(self.cli('paths','--run-id','20260828-0905-bridge','--as-of',self.asof,'--subject-slug','bridge','--truth-engine-root',str(root2)).stdout); st=Path(paths['state_path'])
  self.cli('init','--state',str(st),'--run-id','20260828-0905-bridge','--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','INLINE_UNSTABLE','--subject-slug','bridge','--truth-engine-root',str(root2),'--complexity','SIMPLE','--complexity-score','2')
  self.cli('archive-input','--state',str(st),'--text','d’un pays')
  d=json.loads(st.read_text()); legacy=d['run']['subject_fingerprint_legacy_v1']; self.assertNotEqual(legacy,d['run']['subject_fingerprint'])
  snap=self.root/'legacy2104.json'; snap.write_text(json.dumps({'snapshot_schema':1,'engine':'2.10.4','run_id':'old-2104','as_of':'2026-08-28','subject_slug':'old','subject_fingerprint':legacy,'input_sha256':'sha256:old','facts':[{'key':'fact','value':'bounded','tier':'✦','epi':'FACT','url':'https://example.org/a','families':['A','D'],'memory_id':'mem-2104','verified_at':'2026-08-28','origin_run_id':'old-2104'}],'gaps':[]}))
  self.cli('hydrate','--state',str(st),'--snapshot',str(snap),'--memory-id','snap-2104')
  x=json.loads(st.read_text()); self.assertEqual(x['hydrated']['fingerprint_match'],'LEGACY_V1_2.10.4'); self.assertEqual(x['memory_probe']['status'],'FOUND')

 def test_final_rejects_unresolved_original_input_ref(self):
  f,inv=self.finalize_pre(); d=json.loads(self.state.read_text()); d['run']['original_input_ref']='PENDING'; self.state.write_text(json.dumps(d))
  p=self.cli('validate','--state',str(self.state),'--phase','pre',ok=False); self.assertIn('original_input_ref',p.stdout)

 def test_noncanonical_state_rejected(self):
  p=self.cli('init','--state',str(self.root/'bad.json'),'--run-id','20260828-0902-bad','--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','NONE','--subject-slug','bad','--truth-engine-root',str(self.root),ok=False); self.assertNotEqual(p.returncode,0); self.assertIn('canonical',p.stderr)

 def test_family_prefix_rejected(self):
  p=self.cli('record-source','--state',str(self.state),'--role','◈','--family','fam:A','--url','https://example.org/x',ok=False); self.assertNotEqual(p.returncode,0)

 def test_memory_probe_required(self):
  d=json.loads(self.state.read_text()); d['memory_probe']['status']='PENDING'; self.state.write_text(json.dumps(d)); p=self.cli('validate','--state',str(self.state),ok=False); self.assertIn('memory probe',p.stdout)

 def test_legacy_snapshot_not_exact_hydrate(self):
  snap=self.root/'legacy.json'; snap.write_text(json.dumps({'snapshot_schema':1,'run_id':'old','facts':[]})); p=self.cli('hydrate','--state',str(self.state),'--snapshot',str(snap),ok=False); self.assertNotEqual(p.returncode,0); self.assertIn('subject_fingerprint',p.stderr)

 def test_hydrate_lineage_update(self):
  self.semantic_min(); f=self.evidence(hydrate=True); d=json.loads(self.state.read_text()); fact=next(x for x in d['facts'] if x['id']==f); self.assertEqual(fact['origin_memory_id'],'mem-old'); self.assertEqual(d['memory_probe']['status'],'FOUND'); self.cps(); gates={f'G{i}':'PASS' for i in range(11)}; self.cli('set-gates','--state',str(self.state),'--json',json.dumps(gates)); self.cli('mark-final','--state',str(self.state)); self.cli('render','--state',str(self.state),'--phase','pre'); self.assertIn(f'{f} | UPDATE | mem-old',self.paths['investigation_path'].read_text())

 def test_semantic_and_checkpoint_guards(self):
  p=self.cli('checkpoint','--state',str(self.state),'--label','SCOPE','--last-completed','7','--next-action','9',ok=False); self.assertIn('AXS',p.stderr)
  self.obj('AXS'); self.cli('checkpoint','--state',str(self.state),'--label','SCOPE','--last-completed','7','--next-action','10'); p=self.cli('checkpoint','--state',str(self.state),'--label','FACTS','--last-completed','10','--next-action','11',ok=False); self.assertNotEqual(p.returncode,0)

 def test_pre_requires_always_load(self):
  self.semantic_min(); self.evidence(); self.cps(); self.cli('set-run','--state',str(self.state),'--json',json.dumps({'loaded_modules':[]})); gates={f'G{i}':'PASS' for i in range(11)}; self.cli('set-gates','--state',str(self.state),'--json',json.dumps(gates)); self.cli('mark-final','--state',str(self.state)); p=self.cli('validate','--state',str(self.state),'--phase','pre',ok=False); self.assertIn('ALWAYS LOAD',p.stdout)

 def test_snapshot_gaps_and_canonical_output(self):
  f,inv=self.finalize_pre(); self.cli('update-object','--state',str(self.state),'--id','CAU-001','--json',json.dumps({'status':'GAP','gap_type':'CAUSALITY','gap':'no chain'}))
  p=self.cli('export-snapshot','--state',str(self.state),ok=False); self.assertIn('persisted memory ids',p.stderr)
  wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]
  self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}}))
  out=self.cli('export-snapshot','--state',str(self.state)).stdout.strip().split(' bytes=')[0]; self.assertEqual(Path(out),self.paths['snapshot_path']); x=json.loads(self.paths['snapshot_path'].read_text()); self.assertTrue(x['subject_fingerprint'].startswith('sha256:')); self.assertTrue(any(g.get('gap_type')=='CAUSALITY' for g in x['gaps'])); self.assertEqual(x['facts'][0]['memory_id'],'mem-f')

 def test_persistence_json_file_and_delivery(self):
  f,inv=self.finalize_pre(); wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]; payload={'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}}; pf=self.root/'p.json'; pf.write_text(json.dumps(payload)); self.cli('set-persistence','--state',str(self.state),'--json-file',str(pf)); self.cli('export-snapshot','--state',str(self.state)); self.cli('validate','--state',str(self.state),'--phase','delivery'); self.cli('render','--state',str(self.state),'--phase','delivery'); self.assertIn('WRITEBACK_ROW:{eligible:1;attempted:1;success:1;failure:0;blocked:0}',inv.read_text())

 def test_archive_certification(self):
  f,inv=self.finalize_pre(); wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]; self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}})); self.cli('export-snapshot','--state',str(self.state)); self.cli('render','--state',str(self.state),'--phase','delivery'); sha=hashlib.sha256(inv.read_bytes()).hexdigest(); result=self.root/'result.json'; result.write_text(json.dumps({'verdict':'PASS','deterministic':'PASS','kernel_contract':'delivery','deliverable':str(inv.relative_to(self.root)),'deliverable_sha256':sha,'state_id':'sha256:test'})); self.cli('archive-certification','--state',str(self.state),'--result',str(result)); self.assertTrue(self.paths['certification_path'].exists())

 def test_delivery_rejects_snapshot_memory_drift(self):
  f,inv=self.finalize_pre(); wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]
  self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}})); self.cli('export-snapshot','--state',str(self.state))
  x=json.loads(self.paths['snapshot_path'].read_text()); x['facts'][0]['memory_id']='wrong'; self.paths['snapshot_path'].write_text(json.dumps(x))
  p=self.cli('validate','--state',str(self.state),'--phase','delivery',ok=False); self.assertIn('snapshot memory_id mismatch',p.stdout)

 def test_family_other_token_preserved_and_verified(self):
  self.semantic_min()
  a=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.org/a','--query','a','--accept-source','--role','◈','--family','A').stdout.split()
  b=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.net/b','--query','b','--accept-source','--role','◉','--family','other:activist').stdout.split()
  q=self.cli('record-query','--state',str(self.state),'--mode','WEB','--result','NO_RESULT','--query','REFUTATION fact: counter-evidence search').stdout.strip()
  f=self.cli('record-fact','--state',str(self.state),'--epi','FACT','--tier','✦','--url','https://example.org/a','--sources',f'{a[1]},{b[1]}','--date','2026-08-28','--subject','fact','--value','bounded').stdout.strip(); self.cli('record-refutation','--state',str(self.state),'--fct',f,'--qry',q,'--status','NONE'); self.cps(); gates={f'G{i}':'PASS' for i in range(11)}; self.cli('set-gates','--state',str(self.state),'--json',json.dumps(gates)); self.cli('mark-final','--state',str(self.state)); self.cli('render','--state',str(self.state),'--phase','pre')
  text=self.paths['investigation_path'].read_text(); self.assertIn('fam:other:activist',text); self.assertIn('A,other:activist',text)
  p=subprocess.run([sys.executable,str(VERIFY),'gate','--file',str(self.paths['investigation_path']),'--kernel-contract','pre'],text=True,capture_output=True,cwd=self.root); out=p.stdout+p.stderr; self.assertIn('kernel:provenance_accounting',out); self.assertIn('2 SRC, 2 familles',out); self.assertNotIn('families déclarées',out)

 def test_exact_second_run_hydrates_snapshot_memory_ids(self):
  f,inv=self.finalize_pre(); wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]; self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}})); self.cli('export-snapshot','--state',str(self.state))
  root2=self.root/'second'; paths=json.loads(self.cli('paths','--run-id','20260828-1000-second','--as-of',self.asof,'--subject-slug','second','--truth-engine-root',str(root2)).stdout); st=Path(paths['state_path'])
  self.cli('init','--state',str(st),'--run-id','20260828-1000-second','--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','INLINE_UNSTABLE','--subject-slug','second','--truth-engine-root',str(root2),'--complexity','SIMPLE','--complexity-score','2'); self.cli('archive-input','--state',str(st),'--text','same supplied claim'); self.cli('hydrate','--state',str(st),'--snapshot',str(self.paths['snapshot_path']),'--memory-id','snap-mem'); self.cli('delta','--state',str(st),'--key','fact','--class','REUSE','--reason','stable')
  a=self.cli('record-query','--state',str(st),'--mode','FETCH','--result','FOUND','--url','https://example.org/a','--query','a','--accept-source','--role','◈','--family','A').stdout.split(); b=self.cli('record-query','--state',str(st),'--mode','FETCH','--result','FOUND','--url','https://example.net/b','--query','b','--accept-source','--role','◉','--family','D').stdout.split(); nf=self.cli('record-fact','--state',str(st),'--epi','FACT','--tier','✦','--url','https://example.org/a','--sources',f'{a[1]},{b[1]}','--date','2026-08-28','--subject','fact','--value','bounded').stdout.strip(); d=json.loads(st.read_text()); fact=next(x for x in d['facts'] if x['id']==nf); self.assertEqual(fact['origin_memory_id'],'mem-f')

 def test_link_query_source_controlled_repair(self):
  self.semantic_min()
  sid=self.cli('record-source','--state',str(self.state),'--role','◈','--family','A','--url','https://example.org/a').stdout.strip()
  qid=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.org/a','--query','a').stdout.strip()
  self.cli('link-query-source','--state',str(self.state),'--qry',qid,'--src',sid)
  d=json.loads(self.state.read_text()); q=next(x for x in d['requests'] if x['id']==qid); self.assertEqual(q['source'],sid)
  p=self.cli('link-query-source','--state',str(self.state),'--qry',qid,'--src',sid,ok=False); self.assertIn('already linked',p.stderr)
  sid2=self.cli('record-source','--state',str(self.state),'--role','◈','--family','A','--url','https://example.org/b').stdout.strip()
  qid2=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.org/c','--query','c').stdout.strip()
  p=self.cli('link-query-source','--state',str(self.state),'--qry',qid2,'--src',sid2,ok=False); self.assertIn('exact QRY.url == SRC.url',p.stderr)

 def test_set_persistence_strict_schema(self):
  p=self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'fact_mems':{'FCT-001':'x'}}),ok=False); self.assertIn('unknown field',p.stderr)
  p=self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'writeback_execution':[{'fct':'FCT-001'}]}),ok=False); self.assertIn('must contain exactly',p.stderr)

 def test_pre_requires_minimum_sys_audit(self):
  self.semantic_min(); self.evidence(); self.cps(); gates={f'G{i}':'PASS' for i in range(11)}; self.cli('set-gates','--state',str(self.state),'--json',json.dumps(gates)); self.cli('mark-final','--state',str(self.state))
  d=json.loads(self.state.read_text()); d['sys_log']=[x for x in d['sys_log'] if x.get('call')!='MNEMO_Q']; d['counters']['SYS']=len(d['sys_log']);
  for i,x in enumerate(d['sys_log'],1): x['id']=f'SYS-{i:03d}'
  self.state.write_text(json.dumps(d))
  p=self.cli('validate','--state',str(self.state),'--phase','pre',ok=False); self.assertIn('exactly one SYS MNEMO_Q',p.stdout)

 def test_snapshot_final_has_no_not_initialized(self):
  f,inv=self.finalize_pre(); wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]
  self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}}))
  self.cli('export-snapshot','--state',str(self.state)); raw=self.paths['snapshot_path'].read_text(); self.assertNotIn('NOT_INITIALIZED',raw); self.assertEqual(json.loads(raw)['contradictions'],[])

 def test_narrative_path_enforced(self):
  f,inv=self.finalize_pre(); bad=self.root/'bad.md'; bad.write_text('# Bad'); p=self.cli('render','--state',str(self.state),'--narrative',str(bad),'--phase','pre',ok=False); self.assertIn('canonical',p.stderr)

 def test_refutation_rejects_failed_or_wrong_subject(self):
  a=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.org/a','--query','support a','--accept-source','--role','◈','--family','A').stdout.split()
  b=self.cli('record-query','--state',str(self.state),'--mode','FETCH','--result','FOUND','--url','https://example.net/b','--query','support b','--accept-source','--role','◉','--family','D').stdout.split()
  f=self.cli('record-fact','--state',str(self.state),'--epi','FACT','--tier','✦','--url','https://example.org/a','--sources',f'{a[1]},{b[1]}','--date','2026-08-28','--subject','chat-control-1','--value','bounded').stdout.strip()
  wrong=self.cli('record-query','--state',str(self.state),'--mode','WEB','--result','NO_RESULT','--query','REFUTATION chat-control-2 counter search').stdout.strip()
  p=self.cli('record-refutation','--state',str(self.state),'--fct',f,'--qry',wrong,'--status','NONE',ok=False); self.assertIn('numeric discriminator',p.stderr)
  failed=self.cli('record-query','--state',str(self.state),'--mode','WEB','--result','FAILED_TIMEOUT','--query','REFUTATION chat-control-1 counter search').stdout.strip()
  p=self.cli('record-refutation','--state',str(self.state),'--fct',f,'--qry',failed,'--status','NONE',ok=False); self.assertIn('not an executed refutation',p.stderr)

 def test_narrative_rejects_volatile_qry(self):
  bad=self.root/'volatile.md'; bad.write_text('# Investigation\n\nVoir QRY-001.\n')
  p=self.cli('write-narrative','--state',str(self.state),'--source-file',str(bad),ok=False); self.assertIn('volatile QRY',p.stderr)

 def test_force_replay_archives_derived_outputs(self):
  for key in ('snapshot_path','investigation_path','certification_path'):
   self.paths[key].write_text(key)
  old_input=Path(json.loads(self.state.read_text())['run']['input_path']); self.assertTrue(old_input.exists())
  self.cli('init','--force','--state',str(self.state),'--run-id',self.run_id,'--as-of',self.asof,'--input-kind','CLAIM','--mission-mode','INVESTIGATION','--input-ref','INLINE_UNSTABLE','--subject-slug',self.slug,'--truth-engine-root',str(self.root),'--complexity','SIMPLE','--complexity-score','2')
  self.assertTrue(self.state.exists())
  for p in (old_input,self.paths['narrative_path'],self.paths['snapshot_path'],self.paths['investigation_path'],self.paths['certification_path']): self.assertFalse(p.exists())
  backups=list((self.paths['run_dir']/'_replay_backups').glob('*')); self.assertEqual(len(backups),1)
  names={p.name for p in backups[0].iterdir()}; self.assertIn(self.paths['investigation_path'].name,names); self.assertIn(old_input.name,names)

 def test_controlled_fact_and_sys_repair_reopens_final(self):
  f,inv=self.finalize_pre(); self.assertTrue(inv.exists())
  self.cli('update-fact','--state',str(self.state),'--id',f,'--json',json.dumps({'value':'corrected bounded value'}))
  d=json.loads(self.state.read_text()); self.assertEqual(d['run']['state'],'OPEN'); self.assertEqual(d['sections']['GATE_STATUS_V1'],'NOT_INITIALIZED'); self.assertFalse(inv.exists()); self.assertEqual(d['sys_log'][-1]['call'],'REPAIR_FACT')
  self.cli('update-sys','--state',str(self.state),'--id','SYS-001','--json',json.dumps({'ref':'corrected-ref'}))
  d=json.loads(self.state.read_text()); self.assertEqual(next(x for x in d['sys_log'] if x['id']=='SYS-001')['ref'],'corrected-ref'); self.assertEqual(d['sys_log'][-1]['call'],'REPAIR_SYS')

 def test_snapshot_container_id_rejected_as_fact_origin(self):
  self.semantic_min(); f=self.evidence(hydrate=True)
  p=self.cli('update-fact','--state',str(self.state),'--id',f,'--json',json.dumps({'origin_memory_id':'snapshot-mem'}),ok=False); self.assertIn('enclosing snapshot',p.stderr)

 def test_untyped_gap_rejected_and_typed_gap_accepted(self):
  oid=self.obj('CAU',status='GAP')
  p=self.cli('validate','--state',str(self.state),ok=False); self.assertIn('untyped GAP',p.stdout)
  self.cli('update-object','--state',str(self.state),'--id',oid,'--json',json.dumps({'gap_type':'CAUSALITY','gap':'bounded search found no supported mechanism'}))
  self.cli('validate','--state',str(self.state))

 def test_persistence_attempt_history_preserves_failure_then_success(self):
  f,inv=self.finalize_pre()
  failed=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':0,'failure':1,'blocked':0,'reason':'INVALID_MEMORY_ID'}]
  self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':0,'failure':1,'blocked':0},'writeback_execution':failed}))
  success=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]
  self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':success,'fact_mem':{f:'mem-f'}}))
  self.cli('export-snapshot','--state',str(self.state)); self.cli('validate','--state',str(self.state),'--phase','delivery'); self.cli('render','--state',str(self.state),'--phase','delivery')
  d=json.loads(self.state.read_text()); self.assertEqual([x['result'] for x in d['persistence']['attempt_history']],['FAIL','PASS']); self.assertEqual([x['result'] for x in d['sys_log'] if x['call']=='PERSIST_REBIND'],['FAIL','PASS'])
  text=inv.read_text(); self.assertIn('ATTEMPT-001 |',text); self.assertIn('"result":"FAIL"',text); self.assertIn('ATTEMPT-002 |',text)

 def test_mark_final_rejects_not_initialized_report_section(self):
  self.cli('set-section','--state',str(self.state),'--name','EDI_REPORT','--json',json.dumps('NOT_INITIALIZED'))
  self.semantic_min(); self.evidence(); self.cps(); gates={f'G{i}':'PASS' for i in range(11)}; self.cli('set-gates','--state',str(self.state),'--json',json.dumps(gates))
  p=self.cli('mark-final','--state',str(self.state),ok=False); self.assertIn('EDI_REPORT',p.stderr)

 def test_set_run_accepts_json_file(self):
  pf=self.root/'run-update.json'; pf.write_text(json.dumps({'scope':'json-file-scope'})); self.cli('set-run','--state',str(self.state),'--json-file',str(pf)); self.assertEqual(json.loads(self.state.read_text())['run']['scope'],'json-file-scope')

 def test_verifier_rejects_semantically_wrong_refutation(self):
  f,inv=self.finalize_pre(); text=inv.read_text(); text=text.replace(f'{f} | QRY-003 | NONE',f'{f} | QRY-001 | NONE'); inv.write_text(text)
  p=subprocess.run([sys.executable,str(VERIFY),'gate','--file',str(inv),'--kernel-contract','pre'],text=True,capture_output=True,cwd=self.root)
  self.assertEqual(p.returncode,1); self.assertIn('sémantiquement mal alignée',p.stdout+p.stderr)

 def test_verifier_accepts_correct_pre_and_delivery_contracts(self):
  spec=importlib.util.spec_from_file_location('truth_verify',VERIFY); verify=importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)
  f,inv=self.finalize_pre(); verdict,rows=verify.check_kernel_contract(str(inv),'pre'); self.assertEqual(verdict,'PASS',rows)
  wb=[{'fct':f,'action':'ELIGIBLE:CONFIRME','attempted':1,'success':1,'failure':0,'blocked':0,'reason':'NONE'}]
  self.cli('set-persistence','--state',str(self.state),'--json',json.dumps({'mnemo_row':'mem-i','writeback_row':{'eligible':1,'attempted':1,'success':1,'failure':0,'blocked':0},'writeback_execution':wb,'fact_mem':{f:'mem-f'}})); self.cli('export-snapshot','--state',str(self.state)); self.cli('render','--state',str(self.state),'--phase','delivery')
  verdict,rows=verify.check_kernel_contract(str(inv),'delivery'); self.assertEqual(verdict,'PASS',rows)

if __name__=='__main__': unittest.main()
