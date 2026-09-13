import json, subprocess, pathlib, tempfile, os, sys
ROOT=pathlib.Path('/mnt/data/inv022_r3/truth-engine-v2_2.10.6-R3P0_CANONICAL')
STATE=ROOT/'investigations/2026-09/2026-09-06_russie-operations-influence-france/2026-09-06_10-57_russie-operations-influence-france_RUN_STATE.json'
RT=['python3',str(ROOT/'tools/runtime/run_state.py')]

def run(args, payload=None):
    cmd=RT+args
    p=subprocess.run(cmd,input=(json.dumps(payload,ensure_ascii=False) if payload is not None else None),text=True,capture_output=True,cwd=ROOT)
    print('$',' '.join(args[:3]), '->', p.returncode, p.stdout.strip() or p.stderr.strip())
    if p.returncode: raise SystemExit(p.returncode)

def setsec(name,obj):
    run(['set-section','--state',str(STATE),'--name',name,'--stdin'],obj)

def upd(oid,obj,reason):
    run(['update-object','--state',str(STATE),'--id',oid,'--reason',reason,'--stdin'],obj)

# Correct one semantic counter mapping discovered during verification.
upd('CLM-006', {'counter':['FCT-011']}, 'Phase 13 adversarial review: FCT-011 is the actual counter-indicator (some operations can be highly visible/repeated by political actors); prior low-reach facts support the claim rather than contradict it.')

impact={
  'BENEFITS':[{
    'object':'Russian influence operators / distribution systems',
    'result':'Documented operational benefit: persistent capacity to publish, clone media, automate distribution and obtain some attention. No public causal evidence establishes corresponding persuasion or political outcome.',
    'metric_baseline_period':'Portal Kombat: 152,464 articles in <3 months; RRN: 355 spoofing domains; period 2022-2026.',
    'source_ids':['FCT-002','FCT-004','FCT-006','FCT-010','FCT-021'],
    'status':'BOUNDED_RESULT'
  }],
  'COSTS_HARMS':[{
    'object':'Journalists and fact-checkers',
    'result':'Measurable verification workload caused by Operation Overload/Matriochka solicitations.',
    'metric_baseline_period':'>800 organizations targeted; ~2,400 tweets; >200 emails; >250 debunk/fact-check articles in the documented corpus.',
    'source_ids':['FCT-007','FCT-008'],
    'status':'ESTABLISHED'
  },{
    'object':'French candidates, institutions and media identities',
    'result':'Repeated impersonation, fake-domain and fabricated-media attacks created integrity and reputational risk around elections and public debate.',
    'metric_baseline_period':'>100 .fr local-media clone domains pre-positioned in 2026; multiple candidate-targeted operations through Aug 2026.',
    'source_ids':['FCT-012','FCT-013','FCT-015','FCT-024','FCT-026'],
    'status':'ESTABLISHED_RISK_NOT_OUTCOME'
  }],
  'AFFECTED':[{
    'groups':['French audiences','journalists/fact-checkers','media organizations','political candidates/officials','platforms/registrars'],
    'source_ids':['FCT-001','FCT-007','FCT-008','FCT-012','FCT-015','FCT-021','FCT-024','FCT-026'],
    'status':'ESTABLISHED_TARGETING_OR_DIRECT_WORKLOAD'
  }],
  'RESPONSE_CHANGE':[{
    'actor':'AFNIC',
    'result':'Most pre-positioned CopyCop .fr domains described for the 2026 municipal context were suspended.',
    'source_ids':['FCT-013'],
    'status':'OBSERVED'
  },{
    'actor':'Meta',
    'result':'Removed 1,633 accounts, 703 Pages, one group and 29 Instagram accounts from a Russian-origin network targeting Germany and France.',
    'source_ids':['FCT-019'],
    'status':'OBSERVED'
  },{
    'actor':'Google',
    'result':'Blocked/removed domains, YouTube channels and advertising accounts linked to Russian operations including Doppelganger.',
    'source_ids':['FCT-020'],
    'status':'OBSERVED'
  }],
  'PERSUASION_BEHAVIOR_POLITICAL_OUTCOME':{
    'result':'NONE_ESTABLISHED',
    'reason':'Publicly inspected evidence documents targeting, infrastructure, exposure proxies and some operational consequences, but no causal/counterfactual design demonstrates opinion change, behavior change or election-result change attributable to the examined operations.',
    'supporting_limit_ids':['FCT-005','FCT-009','FCT-011','FCT-014','FCT-018','FCT-022','FCT-023','FCT-026','CAU-005'],
    'gap_type':'CAUSALITY'
  }
}
setsec('IMPACT_MAP',impact)

contrad=[{
  'id':'CON-001',
  'object_ids':['CLM-007','FCT-016','FCT-017'],
  'conflicting_propositions':['VIGINUM 2026 presents Storm-1516 as attributed to GRU unit 29155 with CGE support.','VIGINUM technical report 2025 said it could not confirm direct involvement of unit 29155 or Youry Khoroshenky despite close links.'],
  'source_ids':['SRC-005','SRC-018'],
  'resolution_status':'UNRESOLVED_SCOPE_VERSION_DIFFERENCE',
  'resolution':'Treat the 2026 attribution as an official later assessment; do not present the public chain as independently reproducible from the 2025 technical evidence.',
  'remaining_check':'Independent technical/documentary evidence explaining the evidentiary bridge from 2025 links to 2026 direct attribution.',
  'gap_type':'INDEPENDENCE'
}]
setsec('CONTRADICTION_LEDGER',contrad)

cog={
 'object_question':'Quelles opérations d’influence attribuables à des acteurs russes ont matériellement visé la France, quelles infrastructures/acteurs les ont soutenues, quelle exposition est documentée et quels effets réels peuvent être établis ?',
 'reasoning_graph':[
   'Attribution/infrastructure: FCT-001 + FCT-003 + FCT-019 + FCT-025 -> CLM-001 -> CAU-001',
   'Volume versus audience: FCT-004 + FCT-005 + FCT-006 -> CLM-002 -> CAU-002',
   'Intermediary workload: FCT-007 + FCT-008 + FCT-009 -> CLM-003 -> CAU-003',
   'Electoral/current targeting: FCT-012..FCT-015 + FCT-024 + FCT-026 -> CLM-004/006',
   'Attribution boundary: FCT-016 versus FCT-017 -> CLM-007 / CON-001 / CAU-006',
   'Mitigation: FCT-013 + FCT-019 + FCT-020 -> CLM-008 / CAU-004',
   'Impact stop: FCT-018 + FCT-022 + FCT-023 + FCT-026 -> CAU-005 / CAUSALITY GAP'
 ],
 'decision_boundaries':['TARGETING != PERSUASION','VOLUME != AUDIENCE','VISIBILITY != POLITICAL_EFFECT','STATE_LINKAGE_FOR_ONE_MOI != UNIFIED_COMMAND_FOR_ALL_MOI','TAKEDOWN != AGGREGATE_DETERRENCE'],
 'central_result':'The strongest public evidence supports persistent France-targeted operations, reusable infrastructure and some state/proxy links; it does not support a quantified causal claim about French opinion, behavior or electoral outcomes.',
 'remaining_uncertainties':['Longitudinal French exposure for Portal Kombat','Independent public reproduction of GRU-29155 attribution for Storm-1516','Causal effect of mitigation on long-run operator capacity','Persuasion/behavior/electoral counterfactuals']
}
setsec('COGNITIVE_MAP',cog)

dialect={
 'thesis':{'proposition':'Russia-linked influence ecosystems repeatedly and adaptively target France using cloned media, automated content, fake accounts, direct media/fact-checker targeting and event/election-specific narratives.','support_ids':['FCT-001','FCT-003','FCT-004','FCT-007','FCT-010','FCT-015','FCT-021','FCT-024','FCT-026']},
 'strongest_counter':{'proposition':'Operational scale and repeated targeting do not demonstrate large audience or successful persuasion; several measured cases had low reach and public attribution is not uniformly independently reproducible.','support_ids':['FCT-005','FCT-009','FCT-014','FCT-017','FCT-018','FCT-022','FCT-023','FCT-025','FCT-026']},
 'arbitration':'The corpus supports existence, targeting, infrastructure, persistence and some bounded operational effects. It supports only limited/heterogeneous exposure measurements and leaves persuasion, behavior and election-result effects unestablished.',
 'steelman_each_side':{'attribution_side':'Multiple independent official/platform/legal families converge for Doppelganger/SDA/Structura, making a purely accidental or invented linkage implausible for that branch.','skeptical_side':'Government/platform reports observe detected activity and enforcement, not the universe of exposure; public evidence can be selective, and official attribution can mature without releasing all underlying evidence.'},
 'status':'BOUNDED_SYNTHESIS'
}
setsec('DIALECTICAL_MAP',dialect)

verification={
 'reopened_ids':['SRC-001','SRC-002','SRC-003','SRC-005','SRC-010','SRC-012','SRC-013','SRC-014','SRC-018','SRC-019','SRC-020','FCT-001','FCT-003'],
 'upgraded_ids':[],
 'downgraded_ids':[],
 'contradiction_ids':['CON-001'],
 'circular_families':[],
 'none_found_claims':['CLM-002','CLM-003','CLM-004','CLM-005'],
 'refutation_searched':{'FCT-001':'QRY-066:NONE','FCT-003':'QRY-067:NONE'},
 'remaining_gaps':['CLM-002:TEMPORAL','CLM-003:CAUSALITY','CLM-005:CAUSALITY','CLM-006:CAUSALITY','CLM-007:INDEPENDENCE','CLM-008:CAUSALITY'],
 'bias_test':{'directness':'Strong for existence/targeting; weaker for downstream effects.','provenance':'Diverse for Doppelganger attribution; concentrated in VIGINUM for several Storm cases.','method':'Audience metrics are sparse and platform/government reports cover observed/detected activity.','interests':'French/US/EU authorities and platforms have institutional interests; independent/press sources provide partial challenge but not a full opposed-source corpus.','independence':'Adequate for some decisive claims, single-family for others.','relevance':'High to France-targeted object; generic Russia operations excluded.'},
 'status':'COMPLETE_WITH_TYPED_GAPS'
}
setsec('VERIFICATION_REPORT',verification)

# checkpoint phase 13
run(['checkpoint','--state',str(STATE),'--label','VERIFY','--last-completed','13','--next-action','14'])
