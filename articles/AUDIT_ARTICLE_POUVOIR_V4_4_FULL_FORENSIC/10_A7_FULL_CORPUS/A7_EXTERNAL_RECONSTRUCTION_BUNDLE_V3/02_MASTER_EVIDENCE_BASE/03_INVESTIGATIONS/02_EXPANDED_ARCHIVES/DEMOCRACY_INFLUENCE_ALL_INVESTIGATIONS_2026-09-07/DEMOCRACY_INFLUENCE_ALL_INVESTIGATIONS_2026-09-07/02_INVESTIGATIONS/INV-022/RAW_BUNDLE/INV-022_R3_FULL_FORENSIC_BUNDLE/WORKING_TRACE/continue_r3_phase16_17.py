import json, subprocess, pathlib
ROOT=pathlib.Path('/mnt/data/inv022_r3/truth-engine-v2_2.10.6-R3P0_CANONICAL')
STATE=ROOT/'investigations/2026-09/2026-09-06_russie-operations-influence-france/2026-09-06_10-57_russie-operations-influence-france_RUN_STATE.json'
RT=['python3',str(ROOT/'tools/runtime/run_state.py')]

def run(args,payload=None):
 p=subprocess.run(RT+args,input=(json.dumps(payload,ensure_ascii=False) if payload is not None else None),text=True,capture_output=True,cwd=ROOT)
 print('$',args[0],args[3] if len(args)>3 else '', '->',p.returncode,(p.stdout.strip() or p.stderr.strip())[:800])
 if p.returncode: raise SystemExit(p.returncode)
 return p.stdout.strip()
def setsec(name,obj): run(['set-section','--state',str(STATE),'--name',name,'--stdin'],obj)
def rec(kind,rows): run(['record-object','--state',str(STATE),'--kind',kind,'--stdin'],rows)
def upd(oid,obj,reason): run(['update-object','--state',str(STATE),'--id',oid,'--reason',reason,'--stdin'],obj)

# Phase 16: corpus diversity diagnostic. Scores are bounded diagnostics, not truth.
edi={
 'source_counts':{'primary':13,'secondary':7,'other':0,'total':20},
 'edi':{'final':0.70,'raw':0.80,'penalties':0.10,'flags':['MISSING_COUNTER']},
 'dimensions':{'geo':1.00,'lang':0.65,'strat':0.80,'owner':0.80,'persp':0.60,'temp':1.00},
 'corpus':{
   'direct_objects':13,
   'counters':3,
   'coverage':1.00,
   'independence':0.45,
   'circularity':'No accepted support family exceeds 50% of accepted SRC rows; family A is 10/20. Material Storm subclaims remain single-family and are flagged at claim level.',
   'cc':0.0,
   'edi_star':0.74,
   'band':'BROAD',
   'target':'APEX 0.80 not reached; bounded search stopped with explicit gaps rather than score-chasing.'
 },
 'decisive_claim_coverage':[
   {'claim_id':'CLM-001','direct_object':'YES','independent_families':7,'credible_counter':'FOUND','freshness':'CURRENT','gap_type':'NONE'},
   {'claim_id':'CLM-002','direct_object':'YES','independent_families':1,'credible_counter':'NONE_FOUND','freshness':'STALE','gap_type':'TEMPORAL'},
   {'claim_id':'CLM-003','direct_object':'YES','independent_families':2,'credible_counter':'NONE_FOUND','freshness':'CURRENT','gap_type':'CAUSALITY'},
   {'claim_id':'CLM-004','direct_object':'YES','independent_families':1,'credible_counter':'NONE_FOUND','freshness':'CURRENT','gap_type':'NONE'},
   {'claim_id':'CLM-006','direct_object':'YES','independent_families':7,'credible_counter':'FOUND','freshness':'CURRENT','gap_type':'CAUSALITY'}
 ],
 'perspectives':{'dominant_official':'PRESENT','critical_counter':'PRESENT','local_regional':'PRESENT','academic_expert':'MISSING','dissident':'MISSING'},
 'diagnostic_not_truth':True
}
setsec('EDI_REPORT',edi)

# Phase 17: controls first so axes can reference runtime IDs.
controls=[
 {'control':'AFNIC suspension of pre-positioned CopyCop .fr clone domains during the 2026 municipal-election context','support':['FCT-013'],'status':'PASS','limit':'Asset-level removal is established; aggregate deterrence against the wider ecosystem is not.'},
 {'control':'Meta coordinated-inauthentic-behavior enforcement against a Russian-origin network targeting Germany and France','support':['FCT-019'],'status':'PASS','limit':'Removed assets are observed; total unseen activity and downstream persuasion are not measured.'},
 {'control':'Google TAG blocking/removal of domains, YouTube channels and advertising accounts linked to Russian operations including Doppelganger','support':['FCT-020'],'status':'PASS','limit':'Enforcement counts demonstrate intervention, not aggregate ecosystem deterrence.'}
]
rec('CTRL',controls)

actions=[
 {'action':'Operate content/infrastructure associated with the Doppelganger/RRN branch, including cloned-media and influence-distribution assets.','actor':'Social Design Agency / Structura','intent':'CLAIMED','support':['FCT-003'],'status':'PASS','responsibility_scope':'Bounded to the Doppelganger/RRN branch supported by EU/US/platform evidence; does not establish command over every Russia-aligned MOI in the corpus.'},
 {'action':'Suspend most identified .fr domains pre-positioned by CopyCop to imitate local news sites in the 2026 municipal context.','actor':'AFNIC','intent':'CLAIMED','support':['FCT-013'],'status':'PASS','responsibility_scope':'Domain-registry mitigation only; no claim of causal deterrence beyond removed assets.'},
 {'action':'Remove coordinated inauthentic accounts/Pages/group/Instagram assets from a Russian-origin influence network targeting France among other countries.','actor':'Meta','intent':'CLAIMED','support':['FCT-019'],'status':'PASS','responsibility_scope':'Platform enforcement on detected assets.'},
 {'action':'Block or remove domains, YouTube channels and advertising accounts linked to Russian influence operations, including Doppelganger-related batches.','actor':'Google TAG','intent':'CLAIMED','support':['FCT-020'],'status':'PASS','responsibility_scope':'Google ecosystem enforcement on detected assets.'},
 {'action':'Detect, publicly characterize and in some cases attribute France-targeted influence operations including RRN and Storm-1516.','actor':'VIGINUM','intent':'CLAIMED','support':['FCT-001','FCT-024'],'status':'PASS','responsibility_scope':'Detection/public characterization and attribution statements; not proof of downstream political impact.'}
]
rec('ACT',actions)

resource_flow={
 'flows':[
  {'from':'SDA / Structura / Doppelganger-RRN infrastructure','resource':'cloned domains + content + inauthentic accounts','to':'French media lookalikes / platform users','evidence':['FCT-001','FCT-002','FCT-003','FCT-019'],'status':'SUPPORTED'},
  {'from':'Portal Kombat automation','resource':'high-volume articles + SEO/discoverability','to':'pravda-fr / French search users','evidence':['FCT-004','FCT-005','FCT-006'],'status':'SUPPORTED_WITH_LOW_OBSERVED_AUDIENCE'},
  {'from':'Matriochka / Operation Overload','resource':'fake media assets + direct tags/emails','to':'journalists and fact-checkers','evidence':['FCT-007','FCT-008','FCT-009'],'status':'SUPPORTED_WORKLOAD_EFFECT'},
  {'from':'Storm-1516 / CopyCop / Storm-1679','resource':'fake sites, fabricated videos/reports, candidate-specific narratives','to':'French candidates / election debate / Paris-2024 audiences','evidence':['FCT-012','FCT-013','FCT-014','FCT-015','FCT-021','FCT-024','FCT-026'],'status':'SUPPORTED_TARGETING'},
  {'from':'AFNIC / Meta / Google','resource':'suspension / removal / blocking','to':'identified operation assets','evidence':['FCT-013','FCT-019','FCT-020'],'status':'SUPPORTED_MITIGATION'}
 ],
 'financial_flows':'NONE_ESTABLISHED_IN_SCOPE: no comparable France-specific funding flow was required or established for the selected object question.',
 'limits':['Publication volume is not an audience denominator.','Detected/removed assets are not the total ecosystem.','No flow establishes persuasion or electoral effect.']
}
setsec('RESOURCE_FLOW_MAP',resource_flow)

actor_network={
 'graph_schema':{'nodes':'operators/MOI/platforms/registrars/institutions/targets','edge_types':['DIRECTS_OR_SPONSORS_CLAIMED','OPERATES','TECHNICAL_SUPPORT','TARGETS','REMOVES','REPORTS_ON'],'window':'2022-2026','speculative_edges':'excluded'},
 'edges':[
  {'from':'Russian authorities','to':'SDA / Structura','type':'DIRECTS_OR_SPONSORS_CLAIMED','evidence':['FCT-003'],'status':'SUPPORTED_BY_MULTIPLE_OFFICIAL_PLATFORM_FAMILIES'},
  {'from':'SDA / Structura','to':'Doppelganger/RRN','type':'OPERATES','evidence':['FCT-003'],'status':'SUPPORTED'},
  {'from':'Doppelganger/RRN','to':'French audiences/media identities','type':'TARGETS','evidence':['FCT-001','FCT-002','FCT-019','FCT-020'],'status':'SUPPORTED'},
  {'from':'Storm-1516','to':'CopyCop','type':'TECHNICAL_SUPPORT_OR_COMPONENT','evidence':['FCT-012','FCT-024'],'status':'SUPPORTED'},
  {'from':'GRU unit 29155','to':'Storm-1516','type':'DIRECTS_OR_SPONSORS_CLAIMED','evidence':['FCT-016','FCT-017'],'status':'PARTIAL_CONTESTED_PUBLIC_CHAIN'},
  {'from':'Matriochka','to':'French media/fact-checkers/candidates','type':'TARGETS','evidence':['FCT-007','FCT-008','FCT-026'],'status':'SUPPORTED'},
  {'from':'AFNIC','to':'CopyCop .fr assets','type':'REMOVES','evidence':['FCT-013'],'status':'SUPPORTED'},
  {'from':'Meta','to':'Russian-origin influence assets','type':'REMOVES','evidence':['FCT-019'],'status':'SUPPORTED'},
  {'from':'Google TAG','to':'Russian-operation assets','type':'REMOVES','evidence':['FCT-020'],'status':'SUPPORTED'}
 ],
 'metrics':'NOT_COMPUTABLE: graph is an evidence-bounded partial topology, not a complete enumerated network suitable for centrality/density inference.',
 'gatekeepers':['AFNIC for .fr domain availability in documented cases','Meta/Google for platform asset availability in documented cases'],
 'gaps':['No single command edge is established across all MOIs.','GRU29155→Storm-1516 direct public evidentiary bridge remains incomplete.']
}
setsec('ACTOR_NETWORK_MAP',actor_network)

responsibility={
 'actions':['ACT-001','ACT-002','ACT-003','ACT-004','ACT-005'],
 'boundaries':['ACT-001 does not generalize SDA/Structura responsibility to Portal Kombat, Matriochka, Storm-1516 or Storm-1679 absent evidence.','Platform/registrar mitigation responsibility is bounded to observed enforcement actions, not downstream deterrence.','VIGINUM responsibility here is detection/reporting/attribution statements, not the truth of every hidden attribution input or downstream public effect.'],
 'individual_person_responsibility':'NONE_ASSIGNED: public evidence used here does not require naming an individual person to answer the object question.'
}
setsec('RESPONSIBILITY_MAP',responsibility)

# R3 generic module execution envelope. Owner contracts remain in their modules.
me=[
 {'module':'forensic/REASONING.md','trigger':'Ξ=6','reason':'Audience denominators, hidden exposure and persuasion counterfactuals are materially omitted/unknown.','input_ids':['CLM-002','CLM-006','FCT-005','FCT-006','FCT-022','FCT-023'],'operations_applied':['visible-vs-omitted mapping','denominator comparability test','innocent methodological explanation test'],'result_ids':['IMPACT_MAP','CLM-002','CLM-006'],'negative_results':['No comparable total exposure/persuasion denominator across campaigns.'],'not_computable':['ICEBERG_FACTOR / visible share across heterogeneous campaigns'],'gaps':['TEMPORAL','CAUSALITY'],'status':'COMPLETE_WITH_GAPS'},
 {'module':'clusters/ICEBERG.md','trigger':'Ξ=6','reason':'Operational volume could obscure absent audience/effect denominators.','input_ids':['FCT-004','FCT-005','FCT-006','FCT-022','FCT-023'],'operations_applied':['omission map','denominator check','volume-vs-audience comparison'],'result_ids':['CLM-002','IMPACT_MAP'],'negative_results':['High publication volume does not establish high French audience.'],'not_computable':['cross-campaign hidden audience total'],'gaps':['TEMPORAL longitudinal France audience'],'status':'COMPLETE_WITH_GAPS'},
 {'module':'clusters/FRAMING.md','trigger':'Λ=4 lower-mandatory review','reason':'Terms such as influence/impact can collapse targeting, visibility and persuasion.','input_ids':['CLM-006','FCT-009','FCT-011','FCT-023'],'operations_applied':['frame decomposition','alternative-frame reconstruction','context/denominator review'],'result_ids':['DIALECTICAL_MAP','COGNITIVE_MAP'],'negative_results':['No evidence that the analytical framing itself caused audience effects.'],'not_computable':[],'gaps':['CAUSALITY downstream effect'],'status':'COMPLETE'},
 {'module':'clusters/OVERLOAD.md','trigger':'Ψ=7','reason':'Matriochka/Operation Overload explicitly targets newsrooms/fact-checkers with high-volume solicitations.','input_ids':['FCT-007','FCT-008','FCT-009'],'operations_applied':['defined stream/window review','workload evidence check','exposure-effect-intent separation'],'result_ids':['CLM-003','CAU-003','IMPACT_MAP'],'negative_results':['No measured cognitive-fatigue or persuasion effect on the wider French public.'],'not_computable':['public processing-capacity ratio'],'gaps':['CAUSALITY public persuasion'],'status':'COMPLETE_WITH_GAP'},
 {'module':'clusters/FRAGMENTATION.md','trigger':'⫸=6','reason':'Multiple MOIs converge on France but may remain operationally distinct.','input_ids':['CLM-001','CLM-004','CLM-006','CLM-007','FCT-003','FCT-010','FCT-015','FCT-021'],'operations_applied':['hypothesis stated before convergence','upstream-family deduplication','counter-index search','common-cause alternative'],'result_ids':['DIALECTICAL_MAP','ACTOR_NETWORK_MAP'],'negative_results':['No evidence supports a single unified command chain across every MOI in the corpus.'],'not_computable':['convergence ratio across heterogeneous MOIs'],'gaps':['INDEPENDENCE for some attribution edges'],'status':'COMPLETE_WITH_GAP'},
 {'module':'clusters/WAR.md','trigger':'⚔=9','reason':'Persistent coordinated influence operations with infrastructure, targeting and attribution are the investigation object.','input_ids':['FCT-001','FCT-003','FCT-007','FCT-010','FCT-015','FCT-019','FCT-021','FCT-024'],'operations_applied':['content/infrastructure separation','targeting map','capability-sponsorship-command separation','organic/common-cause alternative test'],'result_ids':['ACTOR_NETWORK_MAP','RESOURCE_FLOW_MAP','CLM-001','CLM-007'],'negative_results':['State-level command is not independently reproduced for every MOI.'],'not_computable':[],'gaps':['INDEPENDENCE Storm-1516/GRU29155'],'status':'COMPLETE_WITH_GAP'},
 {'module':'clusters/NETWORK.md','trigger':'🌐=8','reason':'Material actor/infrastructure/platform relations require a typed sourced graph.','input_ids':['FCT-003','FCT-012','FCT-013','FCT-019','FCT-020','FCT-024'],'operations_applied':['typed node/edge construction','edge provenance attachment','speculative-edge exclusion','gatekeeper identification'],'result_ids':['ACTOR_NETWORK_MAP','ACT-001','ACT-002','ACT-003','ACT-004','ACT-005'],'negative_results':['Complete topology and centrality cannot be inferred from the bounded public graph.'],'not_computable':['centrality','density','betweenness'],'gaps':['partial public topology'],'status':'COMPLETE_WITH_GAP'},
 {'module':'clusters/TEMPORAL.md','trigger':'⏰=7','reason':'Operations persist/adapt across elections and events from 2022 through Aug 2026.','input_ids':['FCT-001','FCT-010','FCT-015','FCT-021','FCT-024','FCT-026'],'operations_applied':['sequence normalization','historical-pattern review','mundane/common-cause alternative'],'result_ids':['TEMPORAL_STATE','CLM-004','CLM-006'],'negative_results':['Timing alone does not establish cross-MOI coordination or political effect.'],'not_computable':['P_random without a defensible null model'],'gaps':['no quantified orchestration probability'],'status':'COMPLETE_WITH_GAP'}
]
setsec('MODULE_EXECUTION',me)

nextq=[
 {'gap_owner':'CLM-002','priority':'P1','seek':'Longitudinal France-specific Portal Kombat audience/exposure series beyond Nov 2023','stop':'Update only if comparable independent audience data become available.'},
 {'gap_owner':'CLM-007','priority':'P1','seek':'Independent technical/documentary evidence for the public evidentiary bridge GRU 29155 → Storm-1516','stop':'Do not infer from later official attribution alone.'},
 {'gap_owner':'CLM-006','priority':'P0','seek':'Causal/counterfactual evidence of opinion, behavior or electoral-result change attributable to a specific operation','stop':'Preserve NONE_ESTABLISHED absent a credible design.'},
 {'gap_owner':'CLM-008','priority':'P2','seek':'Longitudinal operator-capacity/audience evidence before and after takedowns to estimate aggregate deterrence','stop':'Asset removal alone is insufficient.'},
 {'gap_owner':'EDI_REPORT','priority':'P2','seek':'Material Russian/opposed or independent academic/expert source engaging the same France-specific attribution/impact claims','stop':'Do not add token perspective citations merely to raise EDI.'}
]
setsec('NEXT_QUERIES',nextq)

# Terminalize all AXS with actual QRY/SRC attempts and FCT/CAU/CTRL/ACT results.
axes={
 'AXS-001':(['QRY-044','QRY-053','QRY-055','QRY-056','QRY-057','QRY-062','QRY-065','QRY-066','QRY-067','SRC-001','SRC-010','SRC-012','SRC-013','SRC-014','SRC-018','SRC-019'],['FCT-001','FCT-003','FCT-016','FCT-017','FCT-025','CAU-006']),
 'AXS-002':(['QRY-044','QRY-045','QRY-046','QRY-047','QRY-048','QRY-049','QRY-051','QRY-060','QRY-062','QRY-069','SRC-001','SRC-002','SRC-003','SRC-004','SRC-005','SRC-006','SRC-008','SRC-017','SRC-018','SRC-020'],['FCT-001','FCT-004','FCT-007','FCT-010','FCT-015','FCT-021','FCT-024','FCT-026']),
 'AXS-003':(['QRY-044','QRY-045','QRY-046','QRY-047','QRY-048','QRY-049','QRY-051','QRY-059','QRY-062','QRY-069'],['FCT-001','FCT-004','FCT-007','FCT-010','FCT-012','FCT-015','FCT-021','FCT-024','FCT-026']),
 'AXS-004':(['QRY-044','QRY-045','QRY-046','QRY-053','QRY-054','QRY-055','QRY-056','QRY-057','QRY-058','QRY-062'],['FCT-002','FCT-003','FCT-004','FCT-006','FCT-007','FCT-010','FCT-019','FCT-020','CAU-001','CAU-002','CAU-003']),
 'AXS-005':(['QRY-044','QRY-045','QRY-046','QRY-047','QRY-048','QRY-052','QRY-058','QRY-060'],['CAU-001','CAU-002','CAU-003','CAU-004','FCT-005','FCT-008','FCT-013','FCT-018','FCT-023']),
 'AXS-006':(['QRY-053','QRY-055','QRY-056','QRY-057','QRY-062','QRY-065','QRY-066','QRY-067'],['FCT-003','FCT-016','FCT-017','FCT-019','FCT-025','CAU-001','CAU-006','ACT-001']),
 'AXS-007':(['QRY-048','QRY-053','QRY-054','QRY-055','QRY-056','QRY-057'],['CTRL-001','CTRL-002','CTRL-003','ACT-002','ACT-003','ACT-004']),
 'AXS-008':(['QRY-045','QRY-046','QRY-048','QRY-052','QRY-058','QRY-060','QRY-069'],['FCT-005','FCT-008','FCT-009','FCT-013','FCT-014','FCT-018','FCT-022','FCT-023','FCT-026','CAU-003','CAU-004','CAU-005']),
 'AXS-009':(['QRY-060','QRY-062','QRY-065','QRY-066','QRY-067','QRY-069'],['FCT-011','FCT-017','FCT-018','FCT-022','FCT-023','FCT-025','FCT-026','CAU-005','CAU-006'])
}
for oid,(attempts,results) in axes.items():
 upd(oid,{'attempt_ids':attempts,'result_ids':results,'status':'SATURATED'},'Phase 17 R3 terminalization after actual bounded searches and material FCT/CAU/CTRL/ACT results were available; no synthetic attempt/result IDs.')

# Accountability checkpoint requires all AXS terminal.
run(['checkpoint','--state',str(STATE),'--label','INVESTIGATION_ACCOUNTABILITY','--last-completed','17','--next-action','18'])
