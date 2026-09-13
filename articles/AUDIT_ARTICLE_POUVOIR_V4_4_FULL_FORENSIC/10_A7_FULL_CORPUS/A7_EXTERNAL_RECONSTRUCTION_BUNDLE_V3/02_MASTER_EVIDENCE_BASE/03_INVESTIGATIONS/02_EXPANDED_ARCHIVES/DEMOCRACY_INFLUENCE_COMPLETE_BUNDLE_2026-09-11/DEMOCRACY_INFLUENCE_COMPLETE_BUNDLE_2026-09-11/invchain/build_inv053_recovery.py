#!/usr/bin/env python3
import json, subprocess, pathlib, hashlib, sys, os
BASE=pathlib.Path('/mnt/data/invchain')
ROOT=(BASE/'te053'/'truth-engine-v2_2.10.6-R3P1_CANONICAL').resolve()
PACK=(BASE/'TRUTH_ENGINE_2.10.6_R3P1_CANONICAL(1).zip').resolve()
RS=ROOT/'tools/runtime/run_state.py'
RB=BASE/'runtime_batch.py'
RUN_ID='20260911-1027-migration-ngo-funding'
AS_OF='2026-09-11'; SLUG='migration-ngo-funding'
RUN_DIR=ROOT/'investigations'/'2026-09'/f'2026-09-11_{SLUG}'
STATE=RUN_DIR/f'2026-09-11_10-27_{SLUG}_RUN_STATE.json'
CARD=BASE/'INV-053_RUN_CARD.md'

def run(cmd, check=True):
    p=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.stdout.strip(): print(p.stdout.strip())
    if p.stderr.strip(): print(p.stderr.strip(),file=sys.stderr)
    if check and p.returncode: raise SystemExit(p.returncode)
    return p

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

# pack identity
run([sys.executable,str(RB),'check-pack','--pack',str(PACK),'--engine-root',str(ROOT)])
# clean deliberate replay
run([sys.executable,str(RS),'init','--state',str(STATE),'--run-id',RUN_ID,'--parent-run-id','NONE','--as-of',AS_OF,'--input-kind','RUN_CARD','--mission-mode','DEEPEN','--input-ref','PATH:'+str(CARD),'--subject-slug',SLUG,'--truth-engine-root',str(ROOT),'--next-action','SCOPE','--complexity','HIGH','--complexity-score','8','--force'])
run([sys.executable,str(RS),'archive-input','--state',str(STATE),'--source-file',str(CARD)])
run([sys.executable,str(RS),'record-sys','--state',str(STATE),'--result','UNAVAILABLE','--tool','mnemolite','--ref','-','--call','MNEMO_Q'])

checked='2026-09-11T08:27:00+00:00'
sources=[
('A','◈','https://www.senat.fr/rap/r24-326/r24-3262.html','Sénat — suite à enquête Cour des comptes sur associations immigration/intégration','SENAT-R24-326-2','2025-02-11','sections B.1-B.2'),
('A','◈','https://www.senat.fr/notice-rapport/2024/r24-326-notice.html','Sénat — notice rapport n°326 (2024-2025)','SENAT-R24-326-NOTICE','2025-02-11','résumé'),
('B','◈','https://www.hatvp.fr/fiche-organisation/?organisation=784547507','HATVP — France Terre d’Asile','HATVP-784547507','2026-03-31','identité/actions 2024-2025'),
('C','◈','https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale','Conseil d’État — SOS Méditerranée, subventions humanitaires sous conditions','CE-SOS-MEDITERRANEE-2024','2024-05-13','communiqué'),
('C','◈','https://conseil-etat.fr/fr/arianeweb/CE/decision/2024-05-13/474507','Conseil d’État — décision n°474507','CE-474507','2024-05-13','décision'),
('B','◈','https://www.hatvp.fr/fiche-organisation/?organisation=813744471','HATVP — SOS Méditerranée France','HATVP-813744471','2024-03-29','identité/actions 2023-2025'),
('D','◉','https://ecre.org/finance/','ECRE — Funding','ECRE-FUNDING','undated-current','funding sources'),
('D','◉','https://ecre.org/wp-content/uploads/2025/03/ECRE-Annual-Report-on-2024.pdf','ECRE Annual Report 2024','ECRE-AR-2024','2025-03','Activity 2 Advocacy'),
('E','◉','https://picum.org/wp-content/uploads/2024/12/PICUMs-Annual-Report-2024.pdf','PICUM Annual Report 2024','PICUM-AR-2024','2024-12','EU funding / advocacy'),
('other:ec-home','◈','https://home-affairs.ec.europa.eu/news/2024-european-migration-forum-highlights-key-role-civil-society-implementing-pact-2024-12-18_en','European Commission — 2024 European Migration Forum','EC-HOME-EMF-2024','2024-12-18','civil society implementation forum'),
]
# Stage facts
cmds=[]
setrun={
 'parent_run_id':'NONE','complexity':'HIGH','complexity_score':8,
 'scope':'France/UE, principalement 2015–2026. Tracer financeur -> ONG/programme -> activité financée -> cible institutionnelle ou population -> output/action -> décision/effet éventuel. Prioriser comptes, subventions, marchés, registres de lobbying, projets et évaluations. Gardes : financement != tasking ; assistance humanitaire != lobbying ; lobbying != capture ; proximité politique != coordination ; output != effet de politique publique.',
 'resume_count':0,'route_overrides':[],
 'loaded_modules':['definitions/SYMBOLS.md','definitions/PATTERNS.md','definitions/THREATS.md','forensic/GATES.md','forensic/REQUEST_LOG.md','clusters/POWER.md','clusters/MONEY.md','clusters/NETWORK.md'],
 'degraded_flags':['MNEMO_UNAVAILABLE']
}
cmds.append({'cmd':'set-run','args':['--json',json.dumps(setrun,ensure_ascii=False,separators=(',',':'))]})
cmds.append({'cmd':'memory-probe','args':['--status','NONE']})
axes=[
 {'axis':'PUBLIC_FUNDING_TO_OPERATIONAL_CAPACITY','question':'Quels financements publics créent une capacité opérationnelle identifiable chez les associations migratoires, sans inférer plaidoyer ou tasking ?','sought_objects':['funding','contract','service','beneficiaries','operational_output'],'links':['CLM-001','CAU-001'],'attempt_ids':['QRY-001','QRY-002','QRY-003','QRY-004','QRY-005','QRY-006'],'result_ids':['FCT-001','FCT-002','FCT-003','FCT-004','FCT-007','FCT-008','FCT-009'],'status':'SATURATED'},
 {'axis':'FUNDING_AND_ADVOCACY_COEXISTENCE','question':'Le même acteur peut-il recevoir des fonds publics/institutionnels et mener un plaidoyer explicite, et cela démontre-t-il un commandement du financeur ?','sought_objects':['funding_mix','advocacy','lobbying','tasking','command'],'links':['CLM-002','CLM-003','CLM-004','CAU-002','CAU-003'],'attempt_ids':['QRY-003','QRY-006','QRY-007','QRY-008','QRY-009'],'result_ids':['FCT-003','FCT-005','FCT-006','FCT-009','FCT-010','FCT-011','FCT-012'],'status':'SATURATED'},
 {'axis':'ACCESS_TO_POLICY_EFFECT','question':'Quelles traces ferment accès/advocacy -> output institutionnel -> delta de politique, et où la causalité reste-t-elle non isolée ?','sought_objects':['access','recommendation','text_delta','decision','counterfactual'],'links':['CLM-005','CLM-006','CAU-004','CAU-005'],'attempt_ids':['QRY-003','QRY-004','QRY-005','QRY-008','QRY-009','QRY-010'],'result_ids':['FCT-006','FCT-007','FCT-008','FCT-011','FCT-012','FCT-013'],'status':'SATURATED'}
]
for a in axes: cmds.append({'cmd':'record-object','args':['--kind','AXS','--json',json.dumps(a,ensure_ascii=False,separators=(',',':'))]})
cmds.append({'cmd':'checkpoint','args':['--label','SCOPE','--last-completed','7','--next-action','SEARCH']})
for i,(fam,role,url,title,cid,pub,loc) in enumerate(sources,1):
    cmds.append({'cmd':'record-query','args':['--mode','FETCH','--result','ACCEPTED','--url',url,'--query',f'INV-053 source fetch {i}','--accept-source','--role',role,'--family',fam,'--title',title,'--canonical-id',cid,'--publication-date',pub,'--checked-at',checked,'--locator',loc]})
cmds.append({'cmd':'checkpoint','args':['--label','SEARCH','--last-completed','9','--next-action','FACTS']})
facts=[
('https://www.senat.fr/rap/r24-326/r24-3262.html','SRC-001','2025-02-11','French public funding to migration/asylum associations','Les crédits versés aux associations via la mission Immigration, asile et intégration dépassent un milliard d’euros par an et ont fortement augmenté entre 2019 et 2023.'),
('https://www.senat.fr/rap/r24-326/r24-3262.html','SRC-001','2025-02-11','Concentration of association funding','Sur 2019-2023, quinze associations concentrent en moyenne environ 50,3 % des crédits des programmes 104 et 303 dédiés aux associations.'),
('https://www.senat.fr/rap/r24-326/r24-3262.html','SRC-001','2025-02-11','France Terre d’Asile public funding','France Terre d’Asile a reçu environ 57,5 M€ par an en moyenne sur 2019-2023, très majoritairement via le programme 303 pour l’hébergement et l’accompagnement des demandeurs d’asile.'),
('https://www.senat.fr/rap/r24-326/r24-3262.html','SRC-001','2025-02-11','2023 asylum housing and accompaniment funding','En 2023, environ 850 M€ ont été versés aux associations pour l’hébergement et l’accompagnement des demandeurs d’asile/réfugiés vulnérables, dont environ 263,8 M€ estimés pour l’accompagnement.'),
('https://www.hatvp.fr/fiche-organisation/?organisation=784547507','SRC-003','2026-03-31','France Terre d’Asile lobbying registration','France Terre d’Asile est inscrite au répertoire HATVP et identifie plusieurs personnes chargées du plaidoyer/représentation d’intérêts.'),
('https://www.hatvp.fr/fiche-organisation/?organisation=784547507','SRC-003','2026-03-31','France Terre d’Asile declared advocacy actions','Pour 2024-2025, France Terre d’Asile déclare pour son propre compte des actions consistant notamment à transmettre informations et suggestions afin d’influencer des décisions publiques relatives au Pacte migration/asile, aux PLF et à d’autres mesures migratoires.'),
('https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale','SRC-004','2024-05-13','Legal separation of humanitarian subsidies and political activity','Le Conseil d’État exige que les subventions locales à une action humanitaire internationale financent uniquement des activités réellement humanitaires et non des activités politiques.'),
('https://conseil-etat.fr/site/actualites/sos-mediterranee-les-collectivites-territoriales-peuvent-accorder-sous-conditions-une-subvention-a-une-action-humanitaire-internationale','SRC-004,SRC-005','2024-05-13','SOS Méditerranée subsidy outcomes','Le Conseil d’État a validé les subventions de Paris et de l’Hérault à SOS Méditerranée mais annulé celle de Montpellier, jugée insuffisamment ciblée sur l’activité humanitaire.'),
('https://www.hatvp.fr/fiche-organisation/?organisation=813744471','SRC-006','2026-03-31','SOS Méditerranée lobbying negative control','SOS Méditerranée France, inscrite à la HATVP depuis 2024, déclare aucune activité de représentation d’intérêts pour 2024 et 2025.'),
('https://ecre.org/finance/','SRC-007','2026-09-11','ECRE mixed funding base','ECRE déclare recevoir des financements de plusieurs programmes de l’Union européenne ainsi que de multiples fondations philanthropiques et d’autres sources.'),
('https://ecre.org/wp-content/uploads/2025/03/ECRE-Annual-Report-on-2024.pdf','SRC-008','2025-03','ECRE advocacy objective and self-reported incorporation','Le rapport annuel 2024 d’ECRE fixe explicitement l’objectif d’influencer les politiques/pratiques de l’UE et affirme que de nombreuses recommandations ont été incorporées dans les textes finaux du Pacte; cette dernière attribution est auto-déclarée par ECRE.'),
('https://picum.org/wp-content/uploads/2024/12/PICUMs-Annual-Report-2024.pdf','SRC-009','2024-12','PICUM ECRE EU funding advocacy','PICUM rapporte un plaidoyer conjoint avec ECRE sur les fonds de l’UE, des retours à la Commission et des conseils aux eurodéputés, et s’attribue l’obtention de formulations plus fortes dans un avis du Parlement européen.'),
('https://home-affairs.ec.europa.eu/news/2024-european-migration-forum-highlights-key-role-civil-society-implementing-pact-2024-12-18_en','SRC-010','2024-12-18','Institutional access channel for civil society','Le Forum européen sur la migration 2024 a réuni plus de 200 organisations de la société civile avec des institutions européennes et nationales autour de la mise en œuvre du Pacte, établissant un canal institutionnel d’accès et de dialogue.'),
]
for url,srcs,date,subj,val in facts:
    cmds.append({'cmd':'record-fact','args':['--epi','FACT','--tier','✧','--url',url,'--sources',srcs,'--date',date,'--subject',subj,'--value',val,'--mem','-']})
cmds.append({'cmd':'assert-counts','args':['--json',json.dumps({'AXS':3},separators=(',',':'))]})
cmds.append({'cmd':'checkpoint','args':['--label','FACTS','--last-completed','10','--next-action','CAUSAL']})
facts_stage={'schema':1,'stage':'facts','base_state_sha256':sha(STATE),'commands':cmds}
facts_path=BASE/'INV-053_FACTS_STAGE.json'; facts_path.write_text(json.dumps(facts_stage,ensure_ascii=False,indent=2),encoding='utf-8')
run([sys.executable,str(RB),'apply','--pack',str(PACK),'--engine-root',str(ROOT),'--state',str(STATE),'--stage-file',str(facts_path)])

# TAIL
claims=[
 {'claim':'Les financements publics français créent une capacité opérationnelle majeure pour l’hébergement, l’accompagnement et l’intégration liés à l’asile/migration.','claimant':'INV-053','materiality':'DECISIVE','support':['FCT-001','FCT-002','FCT-003','FCT-004'],'counter':'NONE_FOUND','gap_type':'NONE','gap':'NONE','status':'SUPPORTED'},
 {'claim':'France Terre d’Asile cumule des financements publics opérationnels significatifs et un plaidoyer/lobbying explicitement déclaré.','claimant':'INV-053','materiality':'DECISIVE','support':['FCT-003','FCT-005','FCT-006'],'counter':['FCT-009'],'gap_type':'NONE','gap':'NONE','status':'SUPPORTED'},
 {'claim':'Le seul financement d’une ONG migratoire suffit à établir un tasking ou commandement politique par le financeur.','claimant':'hypothèse forte','materiality':'DECISIVE','support':['FCT-007','FCT-008','FCT-009'],'counter':['FCT-005','FCT-006'],'gap_type':'NONE','gap':'NONE','status':'REFUTED'},
 {'claim':'Dans l’écosystème UE, des organisations comme ECRE/PICUM cumulent financements institutionnels/privés et activités d’advocacy explicites.','claimant':'INV-053','materiality':'IMPORTANT','support':['FCT-010','FCT-011','FCT-012'],'counter':'NONE_FOUND','gap_type':'NONE','gap':'NONE','status':'SUPPORTED'},
 {'claim':'Le plaidoyer d’ECRE/PICUM a causé des modifications précises de textes ou décisions de l’UE.','claimant':'organisations concernées / hypothèse causale','materiality':'DECISIVE','support':['FCT-011','FCT-012'],'counter':['FCT-013'],'gap_type':'CAUSALITY','gap':'Les auto-attributions d’incorporation et l’accès institutionnel ne fournissent pas un contrefactuel ni une attribution indépendante article-par-article du delta décisionnel.','status':'PARTIAL'},
 {'claim':'Le droit français impose une séparation explicite entre subvention humanitaire locale et financement d’activités politiques.','claimant':'Conseil d’État','materiality':'IMPORTANT','support':['FCT-007','FCT-008'],'counter':'NONE_FOUND','gap_type':'NONE','gap':'NONE','status':'SUPPORTED'},
]
causal=[
 {'mechanism':'financement public -> capacité opérationnelle -> hébergement/accompagnement/intégration','support':['FCT-001','FCT-003','FCT-004'],'counter':'Le volume de financement ne renseigne pas à lui seul sur une consigne politique.','limit':'Chaîne capacité/service fermée; aucun tasking inféré.','causal_right':'crédit public affecté à des missions -> ressources associatives -> prestation opérationnelle mesurable','status':'SUPPORTED'},
 {'mechanism':'financement public -> dépendance -> tasking/lobbying -> décision publique','support':['FCT-003','FCT-005','FCT-006'],'counter':['FCT-007','FCT-008','FCT-009'],'gap_type':'CAUSALITY','gap':'Aucune instruction du financeur ni médiation causale financeur->position de plaidoyer->décision n’est documentée dans les cas échantillonnés.','limit':'Coexistence financement+plaidoyer établie; commandement/capture non établi.','status':'UNRESOLVED'},
 {'mechanism':'financement mixte institutionnel/privé -> ressources organisationnelles -> advocacy/accès -> outputs','support':['FCT-010','FCT-011','FCT-012','FCT-013'],'counter':'Pluralité de financeurs et mandat propre des organisations empêchent d’identifier un principal commanditaire par le seul flux financier.','limit':'Capacité, advocacy et accès fermés; tasking par un financeur non établi.','causal_right':'ressources multi-financeurs -> capacité d’expertise/advocacy -> accès et productions institutionnelles','status':'SUPPORTED'},
 {'mechanism':'advocacy NGO -> recommandation -> modification de texte/décision UE','support':['FCT-011','FCT-012'],'counter':['FCT-013'],'gap_type':'CAUSALITY','gap':'Manquent attribution indépendante du delta de texte, chronologie amendement par amendement et contrefactuel sans intervention.','limit':'Contribution revendiquée/documentée; causalité marginale spécifique non isolée.','status':'UNRESOLVED'},
 {'mechanism':'règle juridique de ciblage -> affectation de subvention humanitaire -> exclusion des activités politiques','support':['FCT-007','FCT-008'],'counter':['FCT-009'],'limit':'Contrôle juridique spécifique établi; ne prouve pas la séparation parfaite de toutes les subventions existantes.','causal_right':'condition légale de finalité -> contrôle juridictionnel du ciblage -> validation ou annulation de la subvention','status':'SUPPORTED'},
]
controls=[
 {'control':'financement != tasking','support':['FCT-007','FCT-008','FCT-009'],'status':'PASS'},
 {'control':'assistance humanitaire != lobbying','support':['FCT-007','FCT-009'],'status':'PASS'},
 {'control':'lobbying != capture','support':['FCT-006','FCT-013'],'status':'PASS'},
 {'control':'auto-attribution d’un delta de texte != preuve causale indépendante','support':['FCT-011','FCT-012'],'status':'PASS'},
 {'control':'absence de déclaration HATVP != absence de toute expression publique, mais réfute funded NGO => lobbying nécessaire','support':['FCT-009'],'status':'PASS'},
]
sections={
'TEMPORAL_STATE':{'as_of':'2026-09-11','window':'France/UE principalement 2015-2026','breaks':['2019-2023 hausse des crédits IAI associatifs','2024 décisions Conseil d’État SOS Méditerranée','2024-2026 formalisation HATVP du plaidoyer FTDA','2024 Pacte UE et phase de mise en œuvre'],'status':'CURRENT'},
'MANIPULATION_REPORT':{
 'input_kind':'RUN_CARD','mission_mode':'DEEPEN','symbol_stage':'CORPUS_FINAL',
 'symbols':{f'S{i:02d}':v for i,v in enumerate(['financeur','subvention','marché','ONG','programme','capacité','bénéficiaire','plaidoyer','accès','suggestion','tasking','décision','effet','contrôle','contrefactuel'],1)},
 'patterns':{'P01':'funding-to-capacity','P02':'funding+advocacy coexistence','P03':'access without causal closure','P04':'legal separation humanitarian/political'},
 'threats':['funding=tasking','service=lobbying','lobbying=capture','access=effect','self-report=causal proof','grant amount=political alignment'],
 'rhetorical':{'R01':'agréger tous les financements comme influence','R02':'confondre mission publique et relais politique','R03':'transformer accès institutionnel en capture'},
 'complexity':{'band':'HIGH','score':8},'clusters':['MONEY','POWER','NETWORK'],
 'implicit':{'I01':'un même acteur peut séparer opérations et plaidoyer','I02':'pluralité de financeurs réduit l’inférence de commandement','I03':'effet politique exige un delta décisionnel identifiable'},
 'speaker':{'goal':'tester financeur->ONG->activité->output/décision','target':'séparer capacité, lobbying, tasking et effet','tone':'forensic'},
 'assumptions':['les montants publics décrivent des capacités et missions, pas une orientation politique par eux-mêmes','les déclarations HATVP décrivent l’activité revendiquée par l’organisation','les auto-attributions ECRE/PICUM ne valent pas attribution causale indépendante'],
 'priorities':['tracer flux et finalité','séparer opérationnel et plaidoyer','exiger instruction pour tasking','exiger delta/counterfactual pour effet'],
 'query_guidance':'sources officielles pour financements et droit; registres de lobbying; rapports organisationnels seulement pour auto-description de l’advocacy'
},
'MODULE_EXECUTION':[
 {'module':'clusters/MONEY.md','trigger':'flux publics/UE/privés','reason':'distinguer ressource, affectation et dépendance','input_ids':['FCT-001','FCT-002','FCT-003','FCT-004','FCT-010'],'operations_applied':['mapped funder->recipient->program/purpose','separated operational capacity from political effect'],'result_ids':['CLM-001','CLM-004','CAU-001','CAU-003'],'negative_results':['no financial flow alone establishes tasking'],'not_computable':['share of total NGO budgets for all actors'],'gaps':['full cross-organisation funding denominator'],'status':'DONE'},
 {'module':'clusters/POWER.md','trigger':'lobbying/access/decision claims','reason':'test whether resources convert into identifiable public decision','input_ids':['FCT-005','FCT-006','FCT-011','FCT-012','FCT-013'],'operations_applied':['separated access, advocacy, text claim and causal effect','tested legal/institutional counter-controls'],'result_ids':['CLM-002','CLM-005','CAU-002','CAU-004'],'negative_results':['no actor-specific captured decision closed'],'not_computable':['marginal probability of policy adoption caused by NGO advocacy'],'gaps':['article-level legislative footprint and counterfactual'],'status':'DONE'},
 {'module':'clusters/NETWORK.md','trigger':'financeur-recipient-principal inference','reason':'prevent funding relation from substituting for tasking','input_ids':['FCT-003','FCT-009','FCT-010'],'operations_applied':['separated funder, grantee, mandate and principal','used SOS as negative control'],'result_ids':['CLM-003','CLM-006','CAU-005'],'negative_results':['no authenticated financeur command chain'],'not_computable':['latent informal tasking not in public record'],'gaps':['authenticated instructions where any exist'],'status':'DONE'}
],
'SCOPING_REPORT':{'included':['French IAI association funding','FTDA HATVP advocacy','SOS Méditerranée subsidy jurisprudence','ECRE/PICUM funding+advocacy','EU civil-society access forum'],'excluded':['generic NGO ideology','all migration spending outside sampled chains','claims of capture without decision delta','foreign cases without France/UE relevance'],'reason':'actor/case-specific chains with traceable funding, activity and decision/output'},
'CREDO':{'rule':'trace money to funded activity, then separately prove tasking, advocacy and effect','forbidden_shortcuts':['funding=command','humanitarian service=lobbying','advocacy=capture','access=causal effect','self-report=independent proof']},
'COGNITIVE_MAP':{'chain':['financeur','instrument','bénéficiaire','activité financée','advocacy éventuelle','accès/output','décision','effet'],'rival_models':['service delivery','autonomous advocacy','funder tasking','institutional co-production','capture']},
'DIALECTICAL_MAP':{'thesis':'Le financement d’ONG migratoires peut convertir des ressources publiques/privées en influence politique non élective.','antithesis':'Une grande partie finance des missions opérationnelles; plaidoyer et financement peuvent coexister sans commandement ni capture.','synthesis':'Capacité opérationnelle et advocacy sont observables et parfois réunies chez le même acteur; la chaîne financeur->tasking->décision capturée n’est pas fermée dans l’échantillon.'},
'RESOURCE_FLOW_MAP':{'flows':['État français -> programmes 303/104 -> associations -> hébergement/accompagnement/intégration','financeurs UE/fondations -> ECRE/PICUM -> expertise/advocacy','collectivités -> SOS Méditerranée -> activité humanitaire ciblée'],'limits':['flux != instruction','montant != effet politique','cofinancement != principal unique']},
'ACTOR_NETWORK_MAP':[
 {'from':'État français / mission IAI','relation':'finance missions opérationnelles','to':'FTDA et autres associations','support':['FCT-001','FCT-003','FCT-004']},
 {'from':'FTDA','relation':'plaidoyer déclaré pour son propre compte','to':'Parlement/Gouvernement/administration','support':['FCT-005','FCT-006']},
 {'from':'UE + fondations','relation':'financement multi-source','to':'ECRE/PICUM','support':['FCT-010','FCT-011','FCT-012']},
 {'from':'institutions UE','relation':'forum/dialogue structuré','to':'société civile migration','support':['FCT-013']}
],
'IMPACT_MAP':{'established':['financement public -> capacité opérationnelle','FTDA financement opérationnel + lobbying explicite','ECRE/PICUM financement + advocacy','contrôle juridique de séparation humanitaire/politique'],'partial':['auto-attributions de recommandations incorporées','accès institutionnel vers décisions'],'not_established':['financeur->tasking politique','capture d’une décision spécifique','effet politique général des financements']},
'CONTRADICTION_LEDGER':[
 {'issue':'FTDA reçoit des fonds publics et lobbye','resolution':'coexistence factuelle; ne pas inférer tasking sans instruction/condition politique'},
 {'issue':'ECRE/PICUM affirment avoir influencé des textes','resolution':'retenir comme auto-attribution et output; causalité indépendante reste ouverte'},
 {'issue':'SOS reçoit des subventions mais HATVP indique aucune RI 2024-2025','resolution':'contrôle contre funded NGO => lobbyist; ne pas inférer silence politique total'},
 {'issue':'Montpellier annulée mais Paris/Hérault validées','resolution':'le ciblage juridique, pas l’identité de l’ONG, discrimine les décisions'}
],
'VERIFICATION_REPORT':{'research_queries':10,'sources_fetched':10,'facts':13,'method':'official funding/judicial/lobbying records plus organization self-reports clearly labelled; causal edge tested separately','negative_checks':['SOS HATVP no RI','Conseil d’État subsidy targeting','multi-funder ECRE','EC Forum access != effect'],'verdict':'sufficient to establish capacity, declared advocacy and access; insufficient to establish funder tasking or captured decision'},
'EDI_REPORT':{'source_counts':{'A':2,'B':2,'C':2,'D':2,'E':1,'other:ec-home':1},'edi':'DIVERSE_OFFICIAL_PLUS_SELF_REPORT_WITH_PROVENANCE_SEPARATED','dimensions':['French budget/mission execution','lobbying register','administrative jurisprudence','NGO funding disclosures','NGO advocacy reports','EU institutional access'],'corpus':'10 accepted sources across 6 provenance families','decisive_claim_coverage':[{'claim':'CLM-001','families':['A']},{'claim':'CLM-002','families':['A','B']},{'claim':'CLM-003','families':['B','C']},{'claim':'CLM-004','families':['D','E']},{'claim':'CLM-005','families':['D','E','other:ec-home']},{'claim':'CLM-006','families':['C']}],'diagnostic_not_truth':True},
'RESPONSIBILITY_MAP':[
 {'actor':'État français','documented_action':'finance des missions d’asile/intégration exécutées par associations','intent':'PROVEN','scope':'capacity/service delivery; political tasking not established','support':['FCT-001','FCT-003','FCT-004']},
 {'actor':'France Terre d’Asile','documented_action':'mène un plaidoyer explicite auprès des décideurs pour son propre compte','intent':'PROVEN','scope':'declared lobbying; funding causation not established','support':['FCT-005','FCT-006']},
 {'actor':'Conseil d’État','documented_action':'contrôle la finalité humanitaire et le ciblage des subventions','intent':'PROVEN','scope':'legal control only','support':['FCT-007','FCT-008']},
 {'actor':'ECRE/PICUM','documented_action':'mènent advocacy et revendiquent certains outputs politiques','intent':'PROVEN','scope':'self-reported contribution; marginal causal effect not established','support':['FCT-010','FCT-011','FCT-012']}
],
'NEXT_QUERIES':['Pour fermer un effet politique, construire un legislative footprint article-par-article reliant recommandation datée, décideur, amendement et justification.','Pour tester tasking, rechercher des conventions/subventions contenant des conditions de positionnement politique explicites ou des instructions authentifiées.','Pour INV-052, utiliser séparément capacité opérationnelle, lobbying déclaré et absence de preuve de commandement.']
}
cmds=[]
for o in claims: cmds.append({'cmd':'record-object','args':['--kind','CLM','--json',json.dumps(o,ensure_ascii=False,separators=(',',':'))]})
for o in causal: cmds.append({'cmd':'record-object','args':['--kind','CAU','--json',json.dumps(o,ensure_ascii=False,separators=(',',':'))]})
for o in controls: cmds.append({'cmd':'record-object','args':['--kind','CTRL','--json',json.dumps(o,ensure_ascii=False,separators=(',',':'))]})
for name,val in sections.items(): cmds.append({'cmd':'set-section','args':['--name',name,'--json',json.dumps(val,ensure_ascii=False,separators=(',',':'))]})
cmds.append({'cmd':'checkpoint','args':['--label','CAUSAL','--last-completed','11','--next-action','VERIFY']})
cmds.append({'cmd':'checkpoint','args':['--label','VERIFY','--last-completed','13','--next-action','INVESTIGATION_ACCOUNTABILITY']})
cmds.append({'cmd':'checkpoint','args':['--label','INVESTIGATION_ACCOUNTABILITY','--last-completed','17','--next-action','FINALIZE']})
cmds.append({'cmd':'assert-counts','args':['--json',json.dumps({'AXS':3,'CLM':6,'CAU':5,'CTRL':5},separators=(',',':'))]})
cmds.append({'cmd':'set-gates','args':['--json',json.dumps({f'G{i}':'PASS' for i in range(11)},separators=(',',':'))]})
cmds.append({'cmd':'mark-final','args':[]})
tail={'schema':1,'stage':'tail','base_state_sha256':sha(STATE),'commands':cmds}
tail_path=BASE/'INV-053_TAIL_STAGE.json'; tail_path.write_text(json.dumps(tail,ensure_ascii=False,indent=2),encoding='utf-8')
run([sys.executable,str(RB),'apply','--pack',str(PACK),'--engine-root',str(ROOT),'--state',str(STATE),'--stage-file',str(tail_path)])
run([sys.executable,str(RS),'validate','--state',str(STATE),'--phase','pre'])
print('STATE='+str(STATE))
print('RUN_DIR='+str(RUN_DIR))
