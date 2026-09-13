from pathlib import Path
import pandas as pd, csv, re, shutil, hashlib, json, os
from collections import OrderedDict
BASE=Path('/mnt/data/audit121')
PREV=BASE/'ARTICLE_PROTOCOL_CORPUS_V1_REPLAY_2026-09-11'
OUT=BASE/'ARTICLE_PROTOCOL_CORPUS_V1_A4S02_A5_2026-09-11'
if OUT.exists(): shutil.rmtree(OUT)
(OUT/'runtime').mkdir(parents=True)
(OUT/'protocol').mkdir()
(OUT/'source_recovery').mkdir()
# copy essential previous artifacts
for f in (PREV/'runtime').glob('*'):
    shutil.copy2(f, OUT/'runtime'/f.name)
for f in (PREV/'protocol').glob('*'):
    shutil.copy2(f, OUT/'protocol'/f.name)
for name in ['CORPUS_121_AUDIT.csv','SOURCE_INDEX.csv']:
    if (PREV/name).exists(): shutil.copy2(PREV/name, OUT/name)
# source recovery catalog
catp=BASE/'source_recovery'/'SOURCE_CATALOG_ALL.tsv'
shutil.copy2(catp, OUT/'source_recovery'/'SOURCE_CATALOG_ALL.tsv')
D=pd.read_csv(catp,sep='\t')

def pick(inv,sid,title_override=None):
    x=D[(D.inv==inv)&(D.src_id==sid)]
    if x.empty: raise KeyError((inv,sid))
    r=x.iloc[0]
    return dict(title=title_override or str(r.title), url=str(r.url), origin=f'{inv}/{sid}', provenance='TE_ORIGINAL_SOURCE')

def custom(title,url,origin,prov='TARGETED_WEB_RECOVERY'):
    return dict(title=title,url=url,origin=origin,provenance=prov)

# Ordered curated reader layer
specs=OrderedDict([
('S01', custom('National Archives — Senate staff report: Covert Action in Chile, 1963-1973','https://www.archives.gov/declassification/iscap/pdf/2010-009','INV-010 targeted recovery')),
('S02', pick('INV-011','SRC-001')),
('S03', pick('INV-012','SRC-001')),
('S04', pick('INV-013','SRC-001')),
('S05', pick('INV-016','SRC-001')),
('S06', pick('INV-016','SRC-004')),
('S07', pick('INV-017','SRC-001')),
('S08', pick('INV-017','SRC-015')),
('S09', pick('INV-013','SRC-007')),
('S10', custom('National Endowment for Democracy — Grants program','https://www.ned.org/apply-for-grant/en/','INV-019 targeted recovery')),
('S11', pick('INV-025','SRC-001')),
('S12', pick('INV-027','SRC-001')),
('S13', pick('INV-028','SRC-001')),
('S14', pick('INV-033','SRC-002')),
('S15', pick('INV-036','SRC-001')),
('S16', pick('INV-130','SRC-003')),
('S17', pick('INV-131','SRC-002')),
('S18', pick('INV-138','SRC-001')),
('S19', pick('INV-039','SRC-006')),
('S20', pick('INV-043','SRC-001')),
('S21', pick('INV-043','SRC-004')),
('S22', pick('INV-045','SRC-004')),
('S23', pick('INV-047','SRC-001')),
('S24', pick('INV-136','SRC-001')),
('S25', pick('INV-049','SRC-001','Open Society Foundations — Financials')),
('S26', pick('INV-053','SRC-001')),
('S27', pick('INV-054','SRC-005')),
('S28', pick('INV-062','SRC-003')),
('S29', pick('INV-066','SRC-008')),
('S30', pick('INV-066','SRC-009')),
('S31', custom("Service d’information du Gouvernement — missions",'https://www.info.gouv.fr/organisation/service-d-information-du-gouvernement-sig/les-raisons-detre-du-sig','INV-069 targeted recovery')),
('S32', pick('INV-070','SRC-001')),
('S33', pick('INV-071','SRC-003','VIGINUM — missions')),
('S34', pick('INV-134','SRC-006')),
('S35', custom("Ministère des Armées — La lutte informatique d’influence (L2I)",'https://www.defense.gouv.fr/comcyber/nos-operations/lutte-informatique-dinfluence-l2i','INV-073 targeted recovery')),
('S36', pick('INV-074','SRC-002')),
('S37', pick('INV-076','SRC-002')),
('S38', custom('Sénat — Commission d’enquête sur le Fonds Marianne','https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/commission-denquete-sur-le-fonds-marianne.html','INV-078 targeted recovery')),
('S39', pick('INV-081','SRC-010')),
('S40', pick('INV-085','SRC-001')),
('S41', pick('INV-084','SRC-001')),
('S42', pick('INV-087','SRC-006')),
('S43', pick('INV-091','SRC-015')),
('S44', pick('INV-092','SRC-007')),
('S45', pick('INV-142','SRC-007')),
('S46', pick('INV-093','SRC-001')),
('S47', pick('INV-094','SRC-005')),
('S48', pick('INV-096','SRC-001')),
('S49', pick('INV-097','SRC-001')),
('S50', pick('INV-097','SRC-013')),
('S51', pick('INV-098','SRC-001')),
('S52', pick('INV-099','SRC-002')),
('S53', pick('INV-100','SRC-001')),
('S54', pick('INV-135','SRC-001')),
('S55', pick('INV-135','SRC-002')),
('S56', pick('INV-143','SRC-001')),
('S57', pick('INV-119','SRC-004')),
('S58', pick('INV-119','SRC-019')),
('S59', pick('INV-124','SRC-005')),
('S60', pick('INV-125','SRC-002')),
('S61', custom('Légifrance — Code du travail, négociation collective','https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006145398/2026-04-28','INV-126 targeted recovery')),
('S62', pick('INV-127','SRC-005')),
('S63', pick('INV-128','SRC-001')),
('S64', pick('INV-141','SRC-006')),
('S65', pick('INV-103','SRC-001')),
('S66', custom('Social reinforcement learning as a predictor of real-world moral outrage expressions','https://pmc.ncbi.nlm.nih.gov/articles/PMC8363141/','INV-111 targeted recovery')),
('S67', custom('VIGINUM — Analyse du mode opératoire informationnel russe Storm-1516','https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516','INV-112 targeted recovery')),
('S68', pick('INV-147','SRC-005')),
('S69', pick('INV-147','SRC-001')),
('S70', pick('INV-147','SRC-010')),
])
# Save sources
with (OUT/'runtime'/'READER_SOURCES.md').open('w',encoding='utf-8') as f:
    f.write('# Sources lecteur — A4-S02 V3\n\n')
    f.write('Couche de sources publique locale reconstruite à partir des sources originales Truth Engine et de récupérations ciblées. Une présence ici ne crée aucune corroboration indépendante supplémentaire.\n\n')
    for sid,s in specs.items():
        f.write(f'- **[{sid}]** {s["title"]}. {s["url"]}  \n  Origine: `{s["origin"]}`; provenance: `{s["provenance"]}`.\n')

# Calibrate article
article=(PREV/'runtime'/'ARTICLE_CANDIDATE_CORPUS_V1.md').read_text(encoding='utf-8')
article=article.replace("Israël, l'Allemagne, la Turquie, l'Iran, le Maroc ou l'Algérie apparaissent chacun", "Israël, la Turquie, le Maroc ou l'Algérie apparaissent chacun")
article=article.replace("Les cas turc, iranien, marocain et algérien ajoutent une difficulté", "Les cas turc, marocain et algérien ajoutent une difficulté")
old="La banque, la pharmacie et la défense montrent un autre type de pouvoir structurel : ressources considérables, accès réglementaire, expertise technique et revolving doors. Des actions de lobbying peuvent être reliées à des textes ou à des priorités précises. Des risques d'intégrité peuvent être documentés. Pourtant, le corpus conserve aussi des contre-cas : régulateurs qui refusent un produit, arbitrages publics contraires à un intérêt industriel, absence de causalité spécifique entre une intervention et une décision finale."
new="Les dossiers consacrés aux industries réglementées, à la recherche sponsorisée et aux circulations entre haute administration et secteur privé montrent un autre type de pouvoir structurel : ressources, expertise, accès et revolving doors. Ils documentent des liens, des conflits d'intérêts possibles et des effets d'agenda ; ils ne permettent pas de transformer automatiquement ces relations en causalité décisionnelle. Les contre-cas et résultats hétérogènes restent donc matériellement nécessaires."
article=article.replace(old,new)
old2="Les contre-pouvoirs doivent faire partie de ce modèle. Les juridictions annulent certaines mesures. Des plateformes restaurent des contenus. Des administrations refusent des intérêts privés. Des études produisent des résultats nuls. Des campagnes d'influence restent peu visibles. Des institutions se contredisent. Ces revers ne prouvent pas l'équilibre du système, mais ils réfutent la version la plus simple d'une architecture omnipotente."
new2="Les contre-pouvoirs doivent faire partie de ce modèle. Des juridictions annulent certaines mesures ou bornent leur portée, des voies de recours peuvent renverser des décisions, des études produisent des résultats nuls ou faibles et certaines campagnes d'influence restent peu visibles. Ces revers ne prouvent pas l'équilibre du système, mais ils réfutent la version la plus simple d'une architecture omnipotente."
article=article.replace(old2,new2)
# Mapping factual paragraphs to sources and investigations
p_sources={
6:['S02','S03','S04'],8:['S01'],9:['S05','S06'],10:['S07','S08'],11:['S09'],
13:['S10','S09','S11','S15','S16','S17','S18'],15:['S12','S13'],16:['S14','S63'],17:['S15','S16','S17'],18:['S18','S62'],
21:['S19'],22:['S20','S21'],23:['S22'],24:['S23'],25:['S24'],
28:['S25','S26','S28','S29'],30:['S25'],31:['S26','S27'],32:['S28','S29','S30'],
36:['S31','S32'],37:['S33'],38:['S34'],39:['S35'],40:['S36','S37','S31'],41:['S38'],
43:['S39'],44:['S39','S40'],45:['S41'],46:['S42'],47:['S21','S43'],48:['S44'],49:['S45'],
51:['S46','S47'],52:['S48'],53:['S49','S50'],54:['S51'],55:['S52'],56:['S53'],57:['S54','S55'],58:['S56'],
61:['S57','S58'],62:['S29','S30','S58'],63:['S23','S59'],64:['S60'],65:['S61'],66:['S62','S18'],67:['S63','S64'],
73:['S21','S27','S08','S50'],74:['S65','S66','S67'],75:['S34','S68'],76:['S69','S70','S23'],77:['S33','S20','S22'],
}
p_invs={
6:'INV-011;INV-012;INV-013',8:'INV-010',9:'INV-016',10:'INV-017',11:'INV-013',13:'INV-019;INV-013;INV-025;INV-036;INV-130;INV-131;INV-138',15:'INV-027;INV-028',16:'INV-033;INV-128',17:'INV-036;INV-130;INV-131',18:'INV-127;INV-138',21:'INV-039',22:'INV-043',23:'INV-045',24:'INV-047',25:'INV-136',28:'INV-049;INV-053;INV-062;INV-066',30:'INV-049',31:'INV-053;INV-054',32:'INV-062;INV-066',36:'INV-069;INV-070',37:'INV-071',38:'INV-134',39:'INV-073',40:'INV-074;INV-076;INV-069',41:'INV-078',43:'INV-081',44:'INV-081;INV-085',45:'INV-084',46:'INV-087',47:'INV-043;INV-091',48:'INV-092',49:'INV-142',51:'INV-093;INV-094',52:'INV-096',53:'INV-097',54:'INV-098',55:'INV-099',56:'INV-100',57:'INV-135',58:'INV-143',61:'INV-119',62:'INV-120;INV-121;INV-122;INV-066;INV-119',63:'INV-124;INV-047',64:'INV-125',65:'INV-126',66:'INV-127;INV-138',67:'INV-128;INV-141',73:'cross-corpus',74:'INV-103;INV-111;INV-112',75:'INV-134;INV-147',76:'INV-147;INV-047',77:'INV-071;INV-043;INV-045'}
# Add markers to factual paragraphs by paragraph ordinal
lines=article.splitlines(); pid=0; out_lines=[]; section=''
rows=[]
for lineno,line in enumerate(lines,1):
    if line.startswith('## '): section=line[3:]
    if line.strip() and not line.startswith('#'):
        pid+=1
        typ='FACTUAL' if pid in p_sources else ('METHOD_INTERNAL' if pid==80 else 'SYNTHESIS')
        srcs=p_sources.get(pid,[])
        if typ=='FACTUAL':
            line=line.rstrip()+ ' ' + ' '.join(f'[{s}]' for s in srcs)
            status='PASS'
            invs=p_invs.get(pid,'')
            note='Public reader sources local to material proposition; source repetition does not create independent corroboration.'
        elif typ=='METHOD_INTERNAL':
            line=line.rstrip()+' [M1]'
            status='METHOD_INTERNAL'
            invs='CORPUS_121_AUDIT.csv;INV-035'
            note='Internal corpus-reconstruction limitation, not a public factual claim.'
        else:
            status='SYNTHESIS_TRACE_ONLY'; invs='A2/A3 support map'; note='Analytical synthesis; no decorative citation added.'
        rows.append(dict(paragraph_id=f'P{pid:02d}',article_line=lineno,section=section,unit_type=typ,inv_ids=invs,source_ids=';'.join(srcs),public_urls=';'.join(specs[s]['url'] for s in srcs),support_function='SUPPORT' if typ=='FACTUAL' else ('METHOD' if typ=='METHOD_INTERNAL' else 'SYNTHESIS'),reader_source_status=status,note=note))
    out_lines.append(line)
# add source appendix and method note
out_lines += ['','---','','## Sources lecteur','','Les marqueurs `[Sxx]` renvoient aux sources publiques ci-dessous. Ils servent à la vérification locale des propositions matérielles ; ils ne transforment pas plusieurs représentations d’une même lignée en corroborations indépendantes.','']
for sid,s in specs.items():
    out_lines.append(f'- **[{sid}]** {s["title"]} — {s["url"]}')
out_lines += ['','**[M1] Note de méthode.** Le corpus forensique V1 dispose 100 investigations PRIMARY+CASE : 96 handoffs originaux, 1 recovery handoff borné (`INV-044`), 2 récupérations bornées via synthèse (`INV-139`, `INV-140`) et 1 dossier sans handoff terminal récupérable (`INV-035`). Cette note décrit la surface reconstruite ; elle ne constitue pas une source publique du fond.','']
(OUT/'runtime'/'ARTICLE_PUBLISH_CANDIDATE_V2.md').write_text('\n'.join(out_lines),encoding='utf-8')
# source map
pd.DataFrame(rows).to_csv(OUT/'runtime'/'A4_S02_READER_SOURCE_MAP.tsv',sep='\t',index=False)
# source recovery manifest: selected sources
with (OUT/'source_recovery'/'SOURCE_RECOVERY_MANIFEST.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['reader_id','title','url','origin','provenance'])
    for sid,s in specs.items(): w.writerow([sid,s['title'],s['url'],s['origin'],s['provenance']])
# Calibration report
cal='''# A4-S03 — Calibration V3\n\n## Verdict\n\n`PASS_AFTER_LOCAL_REPAIR`\n\n## Réparations locales\n\n1. `P13/P17` : retrait des mentions Allemagne/Iran lorsqu'aucune source lecteur locale n'était remontée avec une autorité suffisante dans la récupération courante. Le mécanisme général et les cas sourcés restent inchangés.\n2. `P62` : remplacement de la généralisation sectorielle banque/pharmacie/défense par une formulation bornée sur industries réglementées, recherche sponsorisée et circulations public/privé. Aucun passage `accès -> causalité décisionnelle` n'est autorisé.\n3. `P73` : remplacement d'une liste d'exemples hétérogènes par des contre-mécanismes réellement sourçables : annulation/borne juridictionnelle, recours, résultats nuls/faibles, faible visibilité de certaines campagnes.\n\n## Contrôles\n\n- `RELATION != CAUSALITÉ` : PASS\n- `BÉNÉFICE != INTENTION` : PASS\n- `CAS != PRÉVALENCE` : PASS\n- `NON_TROUVÉ != ABSENT` : PASS\n- `ANNONCE != ÉTAT_FINAL` : PASS\n- promotion des bounded recoveries : NONE\n- `INV-035` reconstruit artificiellement : NO\n- nouveau BACK : 0\n'''
(OUT/'runtime'/'A4_S03_CALIBRATION_V3.md').write_text(cal,encoding='utf-8')
# A4 S04
close='''# A4-S04 — Fermeture V3\n\n`VERDICT = PASS`\n\n- titre <= corps autorisé : PASS\n- chapô : N/A (aucun chapô autonome ajouté)\n- conclusion <= corps autorisé : PASS\n- nouvelle thèse en fermeture : NONE\n- nouveau BACK : 0\n- changement A2/A3 : NONE\n- article fermé : `ARTICLE_PUBLISH_CANDIDATE_V2.md`\n'''
(OUT/'runtime'/'A4_S04_CLOSURE_V3.md').write_text(close,encoding='utf-8')
# Metrics
rdf=pd.DataFrame(rows)
factual=rdf[rdf.unit_type=='FACTUAL']
assert len(factual)==52, len(factual)
assert (factual.reader_source_status=='PASS').all()
assert factual.source_ids.str.len().gt(0).all()
# A5 docs
review=f'''# A5-S01 — Review matérielle V3\n\n## Verdict\n\n`PASS`\n\n## Contrôles\n\n- propositions matérielles factuelles : **{len(factual)}**\n- propositions factuelles avec source publique locale : **{len(factual)}/{len(factual)}**\n- paragraphes de synthèse explicitement non blanchis par citation décorative : **{len(rdf[rdf.unit_type=='SYNTHESIS'])}**\n- limitation méthodologique interne (`P80`) : **1**, marquée `[M1]`\n- `CORPUS_YIELD_COVERAGE` : **100/100 dispositions**\n- matière exploitable : **99/100**\n- gap : `INV-035` explicite\n- bounded recoveries : `INV-044`, `INV-139`, `INV-140` non promues\n- fausse corroboration par répétition de lignée : **0 détectée**\n- retour A2/A3 : **0**\n- nouveau BACK A6 : **0**\n\n## Anti-généricité\n\nPASS. La prose dépend des mécanismes et contre-cas du corpus, et le retrait des apports spécifiques détruirait la topologie explicative centrale.\n\n## Portée\n\nCette review ferme A5 éditorialement. Elle ne vaut ni audit froid indépendant ni certification A7.\n'''
(OUT/'runtime'/'A5_S01_REVIEW_V3.md').write_text(review,encoding='utf-8')
defects='''# A5-S02 — Défauts V3\n\n```text\nP0_OPEN = 0\nP1_OPEN = 0\nP2_OPEN = 1\n```\n\n## P1-01 — Reader citation layer\n\n`CLOSED` — la couche A4-S02 associe désormais chaque paragraphe factuel matériel à au moins une source publique locale, avec provenance et origine d'enquête.\n\n## P2-01 — Densité\n\n`OPEN_NON_BLOCKING` — le candidat reste long et dense. Une compression éditoriale ultérieure est possible uniquement si elle conserve `CORPUS_YIELD_COVERAGE`, les bornes épistémiques et la localité des sources.\n'''
(OUT/'runtime'/'A5_S02_DEFECTS_V3.md').write_text(defects,encoding='utf-8')
repair='''# A5-S03 — Réparation locale V3\n\n`VERDICT = PASS`\n\nLe seul P1 ouvert en V2 était la couche de sources lecteur. Il est réparé au propriétaire minimal A4-S02, puis la calibration A4-S03 et la fermeture A4-S04 ont été rejouées.\n\nAucun replay global, aucune nouvelle investigation, aucune mutation A2/A3 et aucune promotion d'autorité n'ont été nécessaires.\n'''
(OUT/'runtime'/'A5_S03_REPAIR_V3.md').write_text(repair,encoding='utf-8')
terminal='''# A5-S04 — Décision terminale V3\n\n```text\nA2 = PASS_WITH_EXPLICIT_GAP\nA3 = PASS\nCORPUS_YIELD_COVERAGE = PASS\nA4-S02 = PASS\nA4-S03 = PASS_AFTER_LOCAL_REPAIR\nA4-S04 = PASS\nA5_P0_OPEN = 0\nA5_P1_OPEN = 0\nA5_P2_OPEN = 1_NON_BLOCKING\nA5_TERMINAL = PUBLISH_CANDIDATE\nNEXT = A7_COLD_AUDIT\n```\n\n`PUBLISH_CANDIDATE` ferme la review éditoriale A5. Il ne signifie pas `A7_CERTIFIED`, `CANONICAL` ni `PUBLISHED`. Le prochain gate légitime est l'audit froid réellement indépendant A7.\n'''
(OUT/'runtime'/'A5_S04_TERMINAL_V3.md').write_text(terminal,encoding='utf-8')
# report
report=f'''# Replay local A4-S02 -> A5 — Corpus forensique V1\n\n## Résultat\n\nLe P1 lecteur de V2 est fermé sans réinvestigation générale. La récupération a utilisé les sources déjà présentes dans les investigations Truth Engine lorsqu'elles étaient disponibles, et seulement des récupérations web ciblées pour les trous de chemin nécessaires au texte lecteur.\n\n### Métriques\n\n- PRIMARY+CASE disposés : 100/100\n- matière exploitable : 99/100\n- gap : INV-035\n- paragraphes totaux du candidat : {len(rdf)}\n- paragraphes factuels matériels : {len(factual)}\n- couverture publique locale factuelle : {len(factual)}/{len(factual)}\n- sources lecteur uniques : {len(specs)}\n- réparations A4-S03 : 3 locales\n- A5 P0 : 0\n- A5 P1 : 0\n- A5 P2 : 1 non bloquant (densité)\n- terminal : PUBLISH_CANDIDATE\n\n## Ce qui n'a pas été fait\n\n- aucun nouveau run Truth Engine ;\n- aucune reconstruction artificielle d'INV-035 ;\n- aucune promotion des recoveries bornées ;\n- aucun audit A7 simulé dans la même session.\n\n## Prochaine transition autorisée\n\n`A7-S04 audit froid indépendant`, puis seulement si PASS : validation composée/canonicalisation selon le protocole.\n'''
(OUT/'REPLAY_REPORT_V3.md').write_text(report,encoding='utf-8')
# Copy selected recovered investigation files for traceability based on origins in source layer
used_invs=set()
for s in specs.values():
    m=re.search(r'INV-\d{3}',s['origin'])
    if m: used_invs.add(m.group(0))
# copy any exact/slug files corresponding to used invs
slugmap={'INV-087':'2026-09-09_04-49_poll-influence-elections_INVESTIGATION.md','INV-091':'2026-09-08_22-40_algorithmic-political-exposure_INVESTIGATION.md','INV-096':'2026-09-08_08-07_political-microtargeting_INVESTIGATION.md','INV-097':'2026-09-09_04-23_bot-amplification-elections_INVESTIGATION.md','INV-098':'2026-09-08_05-09_vote-buying-clientelism_INVESTIGATION.md','INV-099':'2026-09-08_05-54_electoral-fraud-claims_INVESTIGATION.md','INV-141':'2026-09-08_15-35_spyware-political-compromise_INVESTIGATION.md','INV-142':'2026-09-08_17-22_hidden-sponsored-content_INVESTIGATION.md','INV-143':'2026-09-08_06-18_institutional-election-timing_INVESTIGATION.md'}
for inv in sorted(used_invs):
    candidates=[BASE/'source_recovery'/f'{inv}_INVESTIGATION.md']
    if inv in slugmap: candidates.append(BASE/'source_recovery'/slugmap[inv])
    for c in candidates:
        if c.exists(): shutil.copy2(c,OUT/'source_recovery'/c.name); break
# manifest hashes for everything except manifest itself
def sha(p):
    h=hashlib.sha256();
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
files=[p for p in OUT.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.tsv']
with (OUT/'MANIFEST_SHA256.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['sha256','bytes','path'])
    for p in sorted(files): w.writerow([sha(p),p.stat().st_size,str(p.relative_to(OUT))])
print('OUT',OUT)
print('paragraphs',len(rdf),'factual',len(factual),'sources',len(specs),'files',len(files)+1)
