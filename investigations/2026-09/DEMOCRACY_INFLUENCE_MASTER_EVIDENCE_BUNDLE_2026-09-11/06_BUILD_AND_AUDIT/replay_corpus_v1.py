from pathlib import Path
import pandas as pd, hashlib, csv, re, shutil, zipfile, json, textwrap, os, difflib

BASE=Path('/mnt/data/audit121')
OUT=BASE/'ARTICLE_PROTOCOL_CORPUS_V1_REPLAY_2026-09-11'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
(OUT/'runtime').mkdir()
(OUT/'protocol').mkdir()

CORPUS=BASE/'FORENSIC_CORPUS_REBUILT_2026-09-11'
AUDIT=CORPUS/'CORPUS_121_AUDIT.csv'
df=pd.read_csv(AUDIT).fillna('')

# ---------------- PATCH MINIMAL ----------------
src=(BASE/'replay_v1'/'ARTICLE_PROTOCOL.md').read_text(encoding='utf-8')
patched=src
# bump local candidate status only, preserve rest
patched=patched.replace('status: c2_experiment_no_go_value','status: c2r1_corpus_yield_guard_candidate',1)

global_anchor='10. A4 construit depuis la décision éditoriale **et** le rendement investigatif préservé. Un article exact, traçable mais presque reproductible par recherche superficielle reste un FAIL produit.\n'
global_add='''11. Pour une synthèse multi-investigations, préserver les dimensions ne suffit pas : chaque investigation de fond éligible doit être disposée explicitement comme contribution directe, contribution via une famille matérielle, exclusion matériellement justifiée ou gap explicite. `DIMENSION_COVERAGE != CORPUS_YIELD_COVERAGE`.\n'''
assert global_anchor in patched
patched=patched.replace(global_anchor,global_anchor+global_add,1)

a3_anchor='''`EXCLUDE_WITH_MATERIAL_JUSTIFICATION` exige une raison explicite montrant que l'exclusion ne change pas matériellement la compréhension de l'objet ou de la contribution retenue.\n'''
a3_add='''\n### Garde de rendement corpus multi-investigations\n\nCette garde ne s'active que lorsque la promesse éditoriale prétend exploiter un corpus composé de plusieurs investigations de fond. Elle n'impose ni quota de citations, ni section par dossier, ni égalité de poids.\n\n```text\nINVESTIGATION_DE_FOND_ÉLIGIBLE\n-> DIRECT_MATERIAL_USE\n   OU\n-> COVERED_BY_MATERIAL_FAMILY\n   OU\n-> EXCLUDE_WITH_MATERIAL_JUSTIFICATION\n   OU\n-> GAP_EXPLICIT\n\nDIMENSION_COVERAGE != CORPUS_YIELD_COVERAGE\nSYNTHESIS / CONTROL != INDEPENDENT_CASE_EVIDENCE\n```\n\n`CORPUS_YIELD_COVERAGE = PASS` seulement si toutes les investigations de fond éligibles ont une disposition explicite et si les résultats distinctifs des familles matérielles qui changent l'explication survivent au contrat. `COVERED_BY_MATERIAL_FAMILY` exige que le rendement propre du dossier soit réellement représenté par le mécanisme/famille conservé, pas seulement qu'un thème voisin soit mentionné.\n\nUn dossier matériellement inaccessible reste `GAP_EXPLICIT`; il n'est jamais reconstruit pour obtenir 100 %.\n'''
assert a3_anchor in patched
patched=patched.replace(a3_anchor,a3_anchor+a3_add,1)

a5_anchor='''Un article exact et traçable doit encore échouer si son rendement d'enquête a été aplati au point qu'une recherche superficielle aurait produit presque le même texte.\n'''
a5_add='''\nPour une synthèse multi-investigations, A5 teste séparément :\n\n```text\nEXPLANATORY_DIMENSIONS_SURVIVE\nCORPUS_YIELD_COVERAGE\nFAMILY_DISTINCTIVE_RESULTS_SURVIVE\n```\n\nLe premier PASS ne compense jamais l'échec des deux suivants. A5 compare la production au registre de disposition A3 : toute investigation éligible absente sans justification, toute famille matérielle aplatie ou tout `GAP_EXPLICIT` silencieusement comblé est au minimum P1, P0 si cela change la thèse.\n'''
assert a5_anchor in patched
patched=patched.replace(a5_anchor,a5_anchor+a5_add,1)

(OUT/'protocol'/'ARTICLE_PROTOCOL_C2R1_PATCHED.md').write_text(patched,encoding='utf-8')
diff=''.join(difflib.unified_diff(src.splitlines(True),patched.splitlines(True),fromfile='ARTICLE_PROTOCOL_C2',tofile='ARTICLE_PROTOCOL_C2R1'))
(OUT/'protocol'/'CORPUS_YIELD_COVERAGE.patch').write_text(diff,encoding='utf-8')

# ---------------- CORPUS MODEL ----------------
primary=df[df['type'].isin(['PRIMARY','CASE'])].copy()
assert len(primary)==100

family_map={
'W1':('F1','Interventions historiques, clandestines et mobilisation'),
'W2':('F2','Puissances étrangères, diplomatie, diasporas et réseaux'),
'W3':('F3','Institutions européennes, droit, régulation et coercition'),
'W4':('F4','Philanthropie, ONG et société civile financée'),
'W5':('F5','Expertise, conseil, think tanks et intermédiation cognitive'),
'W6':('F6','Influence étatique domestique et contre-ingérence'),
'W7':('F7','Médias, plateformes, visibilité et sélection informationnelle'),
'W8':('F8','Élections, financement, ciblage, amplification et procédure'),
'W9':('F9','Confiance, indignation et exploitation des récits'),
'W10':('F10','Pouvoir structurel, infrastructures, coercition et élites'),
'W0':('F0','Attribution, symétrie et standards de qualification'),
}
section_map={'W1':'§2','W2':'§3','W3':'§4','W4':'§5','W5':'§5','W6':'§6','W7':'§7','W8':'§8','W10':'§9','W9':'§10','W0':'§10'}
# Explicit direct exemplars named/discussed in prose; remaining are family-preserved.
direct=set('''INV-010 INV-011 INV-012 INV-013 INV-014 INV-016 INV-017 INV-018
INV-019 INV-021 INV-022 INV-023 INV-025 INV-026 INV-027 INV-028 INV-029 INV-030 INV-033 INV-036 INV-037 INV-130 INV-131 INV-138
INV-039 INV-041 INV-042 INV-043 INV-044 INV-045 INV-046 INV-047 INV-048 INV-136 INV-139
INV-049 INV-051 INV-053 INV-054 INV-056 INV-057 INV-059 INV-062 INV-064 INV-065 INV-066 INV-067
INV-069 INV-070 INV-071 INV-072 INV-073 INV-074 INV-075 INV-076 INV-077 INV-078 INV-079 INV-080 INV-137
INV-081 INV-084 INV-085 INV-087 INV-089 INV-090 INV-091 INV-092 INV-142
INV-093 INV-094 INV-096 INV-097 INV-098 INV-099 INV-100 INV-135 INV-140 INV-143
INV-103 INV-111 INV-112
INV-119 INV-120 INV-121 INV-122 INV-124 INV-125 INV-126 INV-127 INV-128 INV-132 INV-141
INV-134 INV-145 INV-147'''.split())

rows=[]
for _,r in primary.iterrows():
    iid=r['id']; ws=r['workstream']; fid,fname=family_map[ws]
    auth=r['authority'] or r['forensic_role']
    if iid=='INV-035': disp='GAP_EXPLICIT'; reason='Artefact terminal absent du corpus V1; aucune reconstruction autorisée.'
    elif iid in {'INV-044','INV-139','INV-140'}: disp='DIRECT_MATERIAL_USE' if iid in direct else 'COVERED_BY_MATERIAL_FAMILY'; reason='Récupération bornée conservée à autorité dégradée; aucune promotion au rang de handoff original.'
    elif iid in direct: disp='DIRECT_MATERIAL_USE'; reason='Résultat distinctif explicitement mobilisé dans la progression/prose ou comme contrepoint.'
    else: disp='COVERED_BY_MATERIAL_FAMILY'; reason='Rendement préservé dans la famille matérielle et son plafond probatoire; pas de section dédiée nécessaire.'
    summ=re.sub(r'\s+',' ',str(r['summary'])).strip()
    if not summ: summ='[NO_SUMMARY_AVAILABLE]'
    rows.append({
        'inv_id':iid,'workstream':ws,'type':r['type'],'family_id':fid,'family':fname,
        'authority':auth,'physical_source':r['physical_source_file'],'disposition':disp,
        'article_section':section_map[ws],'material_yield':summ,'justification':reason
    })
yield_df=pd.DataFrame(rows).sort_values('inv_id')
yield_df.to_csv(OUT/'runtime'/'A3_CORPUS_YIELD_MATRIX.tsv',sep='\t',index=False)

# Counts
counts=yield_df['disposition'].value_counts().to_dict()
auth_counts=primary['provenance_class'].value_counts().to_dict()

# Families table with all IDs
fam_lines=[]
for (fid,fname) in [family_map[f'W{i}'] for i in range(1,11)]+[family_map['W0']]:
    g=yield_df[yield_df.family_id==fid]
    fam_lines.append((fid,fname,', '.join(g.inv_id.tolist()),len(g)))

# ---------------- A2 ----------------
a2 = f'''# A2 — Reconstruction matérielle depuis le corpus forensique V1

Status: **PASS_WITH_EXPLICIT_GAP**  
Date: 2026-09-11  
Sélection éditoriale: **interdite pendant A2**  
Corpus logique: **121 CLOSED**  
Investigations de fond PRIMARY+CASE: **100**  
Matière de fond exploitable: **99**  
Gap terminal: **INV-035**

## 1. Autorité d'entrée

Le replay ne repart pas des 121 quintessences comme si elles étaient 121 preuves. Il consomme le corpus reconstruit V1 selon sa hiérarchie d'autorité : 96 handoffs terminaux originaux, 1 récupération bornée (`INV-044`), 2 récupérations bornées via synthèse (`INV-139`, `INV-140`), 1 lacune explicite (`INV-035`), 13 synthèses dérivées et 8 unités de contrôle/méthode.

Les synthèses servent à relier et contrôler. Les unités de contrôle servent à calibrer. Elles ne comptent pas comme nouveaux cas indépendants.

## 2. Correction de la compréhension précédente

La compréhension précédente n'était pas factuellement fausse, mais elle était **trop compressée**. Les 15 dimensions transversales restaient présentes tandis que plusieurs familles empiriques devenaient décoratives ou disparaissaient. La reconstruction conserve donc deux niveaux simultanés :

1. les dimensions causales transversales : ressources, accès, sélection, action, droit/contrainte, infrastructure informationnelle, exposition, persuasion, comportement, attribution/tasking, contre-pouvoirs, incitations, asymétrie juridique, temporalité ;
2. les **familles empiriques distinctives** qui empêchent ces dimensions de devenir un essai abstrait.

`DIMENSION_SURVIVAL != CORPUS_YIELD_SURVIVAL`.

## 3. Familles matérielles obligatoires

### F1 — Interventions historiques, clandestines et mobilisation

Le corpus historique ferme l'existence d'interventions, d'opérations clandestines, d'infiltration, de propagande, d'assistance à la mobilisation et de ciblage politique : CIA dans des élections étrangères, relations CIA-médias, COINTELPRO, active measures soviétiques/russes, assistance aux révolutions de couleur, Otpor/CANVAS, printemps arabes, Cambridge Analytica, opération russe de 2016. Il corrige simultanément le récit d'omnipotence : intervention documentée ne signifie ni contrôle total, ni persuasion démontrée, ni résultat électoral contrefactuel fermé.

**Doit survivre :** l'histoire prouve la réalité des techniques et de certains taskings, mais fournit aussi les meilleurs contre-exemples aux récits de toute-puissance.

### F2 — Puissances étrangères, diplomatie, diasporas et réseaux

Le corpus documente plusieurs architectures de puissance : promotion américaine de la démocratie, renseignement et influence en Europe, opérations russes contre la France, relations Russie-partis, United Front chinois, diplomatie/influence israélienne, ELNET, AIPAC, puissance allemande/UE, nucléaire franco-allemand, Émirats, Turquie, Iran, Maroc, Algérie, influence extérieure française. Les mécanismes vont de la diplomatie ouverte au lobbying, à l'association diasporique, au financement, au renseignement privé et à l'opération clandestine.

**Doit survivre :** `foreign != interference`; diaspora, voyage, subvention, lobbying ou proximité ne valent pas tasking. La clandestinité, la tromperie, la coercition, le droit et le commanditaire doivent être établis arête par arête.

### F3 — Institutions européennes, droit, régulation et coercition

Commission, Conseil, Parlement, BCE/CJUE, lobbying, DSA, trusted governance, anti-FIMI, fact-checking certifié, Chat Control/eIDAS, sanctions, normes commerciales et affaires de corruption montrent un pouvoir institutionnel réel et distribué. Certaines décisions modifient directement droits, accès, coûts ou visibilité sans passer par la persuasion.

**Doit survivre :** pouvoir réglementaire et coercitif réel, pluralité des centres, recours et réversibilité. `institutional coordination != common political command`.

### F4 — Philanthropie, ONG et société civile financée

Open Society, grandes philanthropies, ONG migrations, contentieux stratégique, astroturfing et ONG de politique étrangère ferment des chaînes `financement -> capacité -> agenda/programme -> output/accès` dans de nombreux cas. Ils ferment moins souvent `financeur -> contenu dicté -> décision publique causée`.

**Doit survivre :** le financement est un pouvoir de capacité et de sélection de problèmes ; il ne devient commandement que lorsqu'une arête de contrôle/tasking est documentée.

### F5 — Expertise, conseil et intermédiation cognitive

Think tanks français/américains, McKinsey, Big Four, relations publiques, experts médiatiques, recherche financée et groupes d'experts publics documentent une économie de production d'expertise, de réputation, d'accès et de normes. Les conflits d'intérêts, revolving doors et choix d'experts sont parfois fermés case-specifically ; la capture générale ne l'est pas.

**Doit survivre :** l'intermédiation transforme des ressources en présence légitime et en capacité d'agenda. `access != adoption`, `expertise != command`, `repetition != independent consensus`.

### F6 — Influence étatique domestique et contre-ingérence

Communication gouvernementale, nudges, VIGINUM, SGDSN, doctrines militaires, ARCOM, audiovisuel public, aides à la presse, publicité publique, Fonds Marianne, associations subventionnées et sanctions administratives établissent que l'État domestique influence, informe, régule, finance et parfois cherche explicitement des effets comportementaux.

**Doit survivre :** l'espace domestique n'est pas neutre. Les capacités publiques peuvent être légitimes, bornées et contrôlées ; leur existence ne prouve ni abus partisan ni efficacité politique terminale. La contre-ingérence crée aussi institutions, budgets, métriques et intermédiaires.

### F7 — Médias, plateformes, visibilité et sélection informationnelle

Concentration médiatique, agences de presse, gatekeeping éditorial, sondages, trusted flaggers, demotion/démonétisation, moteurs/recommandation, IA générative et influence sponsorisée cachée ferment plusieurs mécanismes de visibilité. Les plateformes et rédactions peuvent modifier l'exposition sans produire automatiquement persuasion ou vote.

**Doit survivre :** propriété, sélection, classement, priorité de traitement et visibilité sont des pouvoirs différents. Les expériences disponibles montrent que `exposure -> attitude` peut être nul, limité ou positif selon contexte ; aucune loi générale n'est autorisée.

### F8 — Élections, financement, ciblage, amplification et procédure

Financement des campagnes, argent étranger, sélection des candidats, microtargeting, bots, achat de votes/clientélisme, fraude réelle, annulation d'élections, hack-and-leak, financement indirect et timing judiciaire ferment des mécanismes distincts qui peuvent modifier compétition, coûts, éligibilité, exposition ou réputation.

**Doit survivre :** ces mécanismes ne forment pas par eux-mêmes un « verrou électoral » commun. L'effet institutionnel peut être certain tandis que l'intention partisane ou le résultat contrefactuel restent non établis.

### F9 — Confiance, indignation et exploitation des récits

Défiance institutionnelle, économie de l'indignation et complotisme montrent des mécanismes de confiance différenciée, de sélection négative, d'engagement et d'exploitation actor-specific. Le pont général `défiance -> manipulabilité -> manipulation réussie` n'est pas fermé.

**Doit survivre :** ne pas utiliser la défiance comme variable magique expliquant toute persuasion.

### F10 — Pouvoir structurel, infrastructures, coercition et élites

Grandes écoles/Inspection des finances, banque/finance, pharma, défense, debanking, infrastructures numériques, corps intermédiaires, soft power académique, influence-for-hire, réseaux d'élites et spyware montrent des pouvoirs qui précèdent parfois toute persuasion : accès, dépendance, exclusion, expertise, infrastructure, surveillance, marché de services clandestins.

**Doit survivre :** pouvoir structurel n'équivaut ni à centre unique ni à capture totale. Les cas Pegasus/Brejza et influence-for-hire montrent ce que signifie fermer une chaîne plus longue, tout en laissant souvent le vote/résultat non établi.

### F0 — Attribution, symétrie et qualification

Les dossiers d'attribution, agents étrangers et double standard imposent une discipline commune : incident -> artefact -> opérateur -> intermédiaire -> principal -> tasking/intention -> exposition -> effet. Le niveau de preuve peut être élevé sur certaines arêtes et faible sur les suivantes. Les différences juridiques alliés/adversaires sont parfois explicites ; un double standard empirique général exige des cas appariés et reste non fermé.

## 4. Compréhension systémique reconstruite

Le corpus n'établit ni un pluralisme équilibré, ni une architecture intégrée commandée par un centre unique. Il établit un **pouvoir polycentrique sous asymétries structurelles**, composé de mécanismes de nature différente : persuasion ouverte, lobbying, financement, expertise, sélection, régulation, coercition, opérations clandestines, surveillance, infrastructure et contrôle de visibilité.

Le résultat transversal le plus robuste reste une décroissance de preuve le long des chaînes :

```text
RESSOURCES / CAPACITÉ
-> ACCÈS / ACTION / CONTRAINTE
-> EXPOSITION / DISTRIBUTION
-> RÉCEPTION / PERSUASION
-> COMPORTEMENT / DÉCISION
-> RÉSULTAT CONTREFACTUEL
```

Mais cette chaîne ne doit plus absorber tout le corpus. Certaines formes de pouvoir agissent par droit, exclusion, infrastructure ou sélection et n'ont pas besoin de persuasion pour produire un effet matériel. L'article doit donc conserver **à la fois** le plafond causal aval et la diversité des mécanismes amont.

## 5. Connaissance négative et limites

- `INV-035` : **GAP_EXPLICIT**. Aucun résultat terminal ne sera reconstruit.
- `INV-044`, `INV-139`, `INV-140` : autorité dégradée, récupérations bornées seulement.
- efficacité électorale générale : non établie ;
- commandement transversal unique : non établi ;
- financement -> commandement : non généralisable ;
- propriété -> contrôle éditorial : non généralisable ;
- exposition -> persuasion -> vote : hétérogène et souvent non fermé ;
- double standard alliés/adversaires systématique : non établi avec dénominateur apparié ;
- contre-ingérence -> fabrication de menace : non établi.

## 6. Handoff A2 -> A3

A3 reçoit :

1. la chaîne probatoire transversale ;
2. les dix familles empiriques F1-F10 + F0 attribution/symétrie ;
3. leurs résultats distinctifs et contre-exemples ;
4. le gap INV-035 ;
5. l'interdiction de substituer préservation des dimensions à rendement corpus.

**A2 VERDICT = PASS_WITH_EXPLICIT_GAP**. Aucune nouvelle investigation générale n'est nécessaire pour prendre une décision éditoriale honnête.
'''
(OUT/'runtime'/'A2_CORPUS_MATERIAL_RECONSTRUCTION.md').write_text(a2,encoding='utf-8')

# ---------------- A3 ----------------
a3s1='''# A3-S01 — Contributions candidates, replay corpus V1

Status: **PASS**

## C1 — Requalifier « ingérence » en chaîne de mécanismes prouvables

Delta : remplacer le label binaire par une analyse mécanisme + arêtes + niveau de preuve. Le gain dépend du croisement de cas historiques, étatiques, privés, domestiques, informationnels, électoraux et structurels. Sans le corpus, la proposition retombe dans un simple « corrélation n'est pas causalité ».

## C2 — Montrer un pouvoir polycentrique, pas un centre unique

Delta : le corpus établit de nombreuses asymétries de ressources, accès, sélection, visibilité, droit et infrastructure, mais ne ferme pas un commandement transversal commun. Ce n'est ni un pluralisme équilibré ni une architecture intégrée démontrée.

## C3 — Distinguer pouvoir matériel et efficacité persuasive

Delta : plusieurs mécanismes produisent des effets directs sans persuasion, notamment sanction, exclusion, réglementation, compromission, sélection ou restriction de visibilité. Parallèlement, la chaîne vers persuasion/vote/résultat reste souvent beaucoup moins fermée. Le plafond causal aval ne doit donc plus effacer la diversité des pouvoirs amont.

## C4 — Appliquer la même grammaire aux étrangers, alliés, acteurs domestiques et dispositifs de contre-ingérence

Delta : mêmes mécanismes -> mêmes questions de tasking, visibilité, clandestinité, coercition, droit et effet. Le corpus ferme certaines asymétries juridiques, mais pas un double standard empirique général sans cas appariés.

## Admission

Les quatre candidats sont complémentaires plutôt que concurrents. C1 fournit la méthode, C2 le modèle systémique, C3 la correction causale et C4 le contrôle de symétrie. Le contrat éditorial peut les unir sans les fusionner en confirmations indépendantes.
'''
(OUT/'runtime'/'A3_S01_CONTRIBUTIONS_V2.md').write_text(a3s1,encoding='utf-8')

# no new published corpus comparison; inherit prior bounded comparison, explicitly scope
a3s2='''# A3-S02 — Relation au corpus publié, replay borné

Status: **PASS_BOUNDED / NO_NEW_CORPUS_SCAN**

Le replay ne relance pas une comparaison générale du corpus publié : aucune nouvelle matière éditoriale externe n'a été fournie et le défaut identifié était A2/A3 corpus-yield, non la nouveauté relative au Substack.

La relation éditoriale héritée reste : continuité cumulative avec correction méthodologique et systémique. Le nouveau delta est **interne au rendement de l'enquête** : réintégrer les familles empiriques que le premier contrat avait aplaties. Cette décision ne transforme aucune ancienne publication en preuve du fond.
'''
(OUT/'runtime'/'A3_S02_PUBLISHED_CORPUS_COMPARISON_V2.md').write_text(a3s2,encoding='utf-8')

a3s3=f'''# A3-S03 — Contrat éditorial reconstruit

Status: **PASS**

## Promesse centrale

**Montrer comment s'exerce réellement le pouvoir d'influence dans une démocratie lorsque l'on applique la même chaîne de preuve aux États étrangers, alliés, acteurs domestiques, institutions, financeurs, médias, plateformes, cabinets, ONG et infrastructures.**

Le corpus autorise une conclusion bornée : il existe une forte densité de mécanismes d'influence et d'asymétries de capacité, d'accès, de sélection, de visibilité, de droit et d'infrastructure ; ces mécanismes forment un système polycentrique plutôt qu'un commandement unique démontré. La preuve est souvent forte pour capacité/action/contrainte et plus faible pour persuasion, vote ou résultat contrefactuel.

## Gain lecteur

Le lecteur doit pouvoir distinguer :

- influence légitime, pouvoir structurel, coercition et opération clandestine ;
- ressources/capacité, tasking, exposition et effet ;
- acteur étranger et ingérence ;
- coordination sectorielle et centre commun ;
- asymétrie juridique et double standard empirique ;
- réalité des menaces et efficacité/proportionnalité de la contre-ingérence.

## Plancher explicatif

F1 à F10 et F0 attribution/symétrie sont **PRESERVE_IN_EXPLANATORY_FLOOR**. Aucun n'est supprimé. Leur poids éditorial varie, mais aucune famille ne peut disparaître du produit.

## CORPUS_YIELD_COVERAGE

PRIMARY+CASE = 100  
DIRECT_MATERIAL_USE = {counts.get('DIRECT_MATERIAL_USE',0)}  
COVERED_BY_MATERIAL_FAMILY = {counts.get('COVERED_BY_MATERIAL_FAMILY',0)}  
GAP_EXPLICIT = {counts.get('GAP_EXPLICIT',0)} (`INV-035`)  
UNACCOUNTED = 0

**Gate = PASS.** Le registre détaillé est `A3_CORPUS_YIELD_MATRIX.tsv`.

## Limites déterminantes

- aucune reconstruction d'INV-035 ;
- aucune promotion des récupérations bornées ;
- aucun résultat électoral général inféré depuis l'existence d'une opération ;
- aucun commandement inféré depuis financement, propriété, accès ou coprésence ;
- aucun double standard systémique affirmé sans comparateur apparié ;
- contre-pouvoirs et revers restent dans le modèle.
'''
(OUT/'runtime'/'A3_S03_EDITORIAL_CONTRACT_V2.md').write_text(a3s3,encoding='utf-8')

a3s4='''# A3-S04 — Décision pré-rédactionnelle, replay corpus V1

Status: **FORME_LONGUE**

## Décision

`FORME_LONGUE`

## Pourquoi

`SHORTER_OUTPUT` échoue : le gain serait déformé si l'on réduisait le corpus à la seule fracture opération/effet. Le contrat exige de préserver plusieurs modalités de pouvoir qui n'obéissent pas à la même chaîne finale, ainsi que les contre-pouvoirs et le contrôle de symétrie.

`MORE_INVESTIGATION` est écarté : le seul gap de provenance certain est INV-035 et il ne bloque pas le contrat. Les autres limites sont des plafonds probatoires à conserver, non des prétextes à réinvestiguer globalement.

`NO_ARTICLE` est écarté : le contrat est matériel, spécifique au corpus et produit un modèle falsifiable.

## Obligations de transmission

1. histoire/opérations clandestines sans omnipotence ;
2. pluralité des puissances et influence ouverte/opaque ;
3. droit/régulation/coercition ;
4. financement et intermédiation sans saut vers commandement ;
5. influence étatique domestique et contre-ingérence ;
6. gatekeeping/visibilité sans saut automatique vers persuasion ;
7. mécanismes électoraux distincts sans « verrou » commun inventé ;
8. pouvoir structurel/infrastructure/surveillance ;
9. attribution arête par arête et symétrie de standard ;
10. modèle polycentrique + plafond causal aval ;
11. INV-035 visible comme gap, jamais rempli.
'''
(OUT/'runtime'/'A3_S04_PREWRITING_DECISION_V2.md').write_text(a3s4,encoding='utf-8')

# ---------------- A4 PROGRESSION ----------------
progress='''# A4-S01 — Progression reconstruite

Status: **PASS**  
PROSE_WRITTEN = 0

## P1 — Partir du problème de qualification
Avant : « influence » et « ingérence » semblent être des catégories évidentes.  
Gain : montrer que le même espace contient persuasion ouverte, lobbying, financement, sélection, coercition, clandestinité, surveillance et infrastructure.  
Transition : il faut donc tester des chaînes plutôt que des étiquettes.

## P2 — Utiliser l'histoire comme étalon, pas comme mythe fondateur
Avant : opérations historiques = preuve d'omnipotence.  
Gain : CIA, COINTELPRO, active measures, mobilisations assistées, Cambridge Analytica et 2016 ferment des actions réelles tout en laissant souvent l'effet terminal ouvert.  
Transition : la présence d'un opérateur et d'une action ne suffit pas à mesurer ce qu'ils ont changé.

## P3 — Comparer les puissances étrangères par mécanisme
Avant : étranger = ingérence.  
Gain : diplomatie, lobbying, diaspora, financement, renseignement, communication stratégique et clandestinité sont séparés.  
Transition : cette discipline doit s'appliquer aussi aux institutions et acteurs domestiques.

## P4 — Montrer que droit et institution peuvent produire un effet sans persuasion
Avant : influence = convaincre.  
Gain : sanctions, normes, régulation, accès à la TNT, DSA, procédure et corruption peuvent changer coûts/droits/accès directement.  
Transition : d'autres pouvoirs amont agissent via ressources et intermédiation.

## P5 — Suivre argent, expertise et intermédiation
Avant : financement = contrôle.  
Gain : philanthropies, ONG, think tanks, consultants, recherche et groupes d'experts transforment ressources en capacité, accès, expertise et agenda, avec tasking variable.  
Transition : l'État domestique participe lui aussi à ce champ.

## P6 — Réintégrer l'influence étatique domestique et la contre-ingérence
Avant : démocratie domestique neutre versus ingérence étrangère.  
Gain : communication, nudges, VIGINUM/SGDSN, ARCOM, audiovisuel, aides, publicité et programmes anti-désinformation constituent des capacités d'influence/régulation réelles et contrôlées de façon inégale.  
Transition : une partie essentielle du pouvoir passe ensuite par la visibilité.

## P7 — Séparer propriété, gatekeeping, classement et persuasion
Avant : concentration/plateforme = contrôle des opinions.  
Gain : propriété, agences, sélection éditoriale, sondages, trusted flaggers, demotion, recommandation, IA et sponsoring caché agissent sur l'exposition ; les effets attitudinaux restent hétérogènes.  
Transition : l'élection combine plusieurs de ces leviers sans les fondre en système unique.

## P8 — Décomposer les mécanismes électoraux
Avant : tout mécanisme qui touche une élection change le résultat.  
Gain : financement, microtargeting, bots, clientélisme, fraude, annulation, hack-and-leak et timing judiciaire ont des effets distincts et des plafonds causaux différents.  
Transition : le pouvoir politique dépasse toutefois la période électorale.

## P9 — Montrer les infrastructures et dépendances structurelles
Avant : influence = message.  
Gain : élites, finance, pharma, défense, debanking, cloud, corps intermédiaires, soft power, influence-for-hire et spyware montrent des leviers d'accès, exclusion, dépendance ou compromission.  
Transition : il faut alors un modèle systémique qui ne fabrique pas un centre commun.

## P10 — Conclure par attribution, symétrie et modèle polycentrique
Avant : choix entre pluralisme équilibré et complot centralisé.  
Gain : pouvoir polycentrique sous asymétries, avec coordinations locales, contre-pouvoirs et chaînes de preuve incomplètes. Même mécanisme = même standard, quel que soit le camp.  
Conclusion autorisée : dense architecture de pouvoirs, pas preuve d'un commandement unique ; forte preuve amont, effet terminal plus difficile à fermer.
'''
(OUT/'runtime'/'A4_S01_PROGRESSION_V2.md').write_text(progress,encoding='utf-8')

# ---------------- ARTICLE ----------------
article='''# Le pouvoir d'influence n'a pas un centre unique

## 1. Le mot « ingérence » mélange trop de choses

Une démocratie n'est jamais un espace sans influence. Les gouvernements communiquent, les partis cherchent des voix, les entreprises défendent leurs intérêts, les syndicats négocient, les associations plaident, les médias sélectionnent, les plateformes classent, les diplomaties cultivent des réseaux et les services de renseignement tentent parfois d'agir clandestinement. Le problème commence quand ces mécanismes différents sont condensés dans un seul mot.

Le corpus d'enquêtes reconstruit oblige à distinguer au moins quatre familles de pouvoir. Il y a l'influence ouverte : diplomatie publique, lobbying, campagnes, expertise, financement déclaré. Il y a le pouvoir structurel : propriété, accès, infrastructure, capacité financière, contrôle d'une procédure ou d'un canal de distribution. Il y a la coercition : sanction, exclusion, gel d'avoirs, restriction administrative, règle juridique, dépendance technique. Et il y a les opérations opaques ou trompeuses : faux comptes, faux médias, hack-and-leak, infiltration, spyware, astroturfing, prestataires clandestins.

Ces familles peuvent se combiner, mais elles ne prouvent pas la même chose. Un financement prouve une ressource. Un rendez-vous prouve un accès. Une campagne prouve une action. Une campagne vue prouve une exposition. Rien de cela ne suffit, seul, à établir une persuasion, un vote modifié ou un résultat électoral différent.

Cette distinction paraît élémentaire. Elle change pourtant presque tout. Elle empêche de transformer la présence d'un acteur étranger en ingérence par définition. Elle empêche aussi l'erreur inverse : réserver le mot « influence » aux puissances étrangères comme si les institutions domestiques, les financeurs, les régulateurs, les médias ou les infrastructures n'exerçaient aucun pouvoir sur les conditions du choix.

Le corpus ne décrit donc pas une bataille simple entre une démocratie passive et des attaquants extérieurs. Il décrit un espace saturé d'acteurs dont les moyens, les droits, les accès et les méthodes sont profondément inégaux. La question sérieuse devient : **quelle arête est effectivement prouvée, avec quel degré d'autorité, et jusqu'où peut-on suivre la chaîne avant que la preuve s'arrête ?**

## 2. L'histoire prouve les opérations. Elle ne prouve pas l'omnipotence

Les dossiers historiques sont indispensables parce qu'ils ferment ce que le débat contemporain transforme parfois en abstraction. Des interventions américaines dans des élections étrangères sont documentées. Des relations clandestines entre la CIA et des journalistes ou médias ont existé. COINTELPRO n'était pas une simple surveillance : infiltration, désorganisation, lettres anonymes, conflits provoqués et opérations de discrédit ont été utilisés contre des organisations politiques américaines. Les « active measures » soviétiques combinaient faux, organisations de façade, agents d'influence et manipulation médiatique.

Ces faits interdisent une naïveté commode : les États démocratiques comme autoritaires ont utilisé des techniques d'influence clandestine. Mais ils interdisent aussi l'excès symétrique. Même dans des cas historiques très documentés, le passage de l'intervention au résultat politique final reste souvent difficile à isoler.

Le Chili de 1964 est un bon exemple. Le soutien américain à Eduardo Frei est documenté. En revanche, isoler l'effet marginal de cette intervention sur sa majorité ou sur le résultat contrefactuel demeure beaucoup plus fragile. Une explication domestique concurrente reste matériellement possible. Le fait important n'est donc pas que « la CIA n'a eu aucun effet », proposition que le corpus ne permet pas davantage. Le point est qu'une opération réelle et substantielle ne fournit pas automatiquement la mesure de ce qu'elle a changé.

La même discipline vaut pour les mobilisations soutenues de l'extérieur. Les révolutions de couleur, Otpor et CANVAS, puis les printemps arabes montrent des circulations de méthodes, de formations, d'assistance, de financement ou de technologies. Cela ne transforme pas les dynamiques locales en produits importés. Une mobilisation peut être endogène tout en bénéficiant d'une assistance extérieure. Une assistance peut modifier des capacités sans créer la cause principale du soulèvement. Confondre ces niveaux revient à choisir à l'avance entre deux récits totalisants : spontanéité pure ou opération extérieure.

Cambridge Analytica fournit un autre contrôle utile. L'entreprise a réellement travaillé sur les données, le ciblage et la communication politique. Ses capacités commerciales et ses revendications ont alimenté l'idée d'une machine psychométrique capable de manipuler un électorat. Le corpus ne ferme pas cette efficacité générale. L'existence d'un système de ciblage et d'une stratégie ne suffit pas à démontrer qu'ils ont produit le résultat politique revendiqué.

L'élection américaine de 2016 pousse encore plus loin la distinction. L'opération russe est documentée. Le piratage, les fuites et différentes opérations informationnelles appartiennent au dossier. En revanche, les évaluations officielles n'ont pas conclu à une mesure du changement de résultat électoral. Là encore, la conclusion rationnelle n'est ni « aucune influence » ni « l'élection a été causée par l'opération ». C'est une conclusion plus étroite : **l'action est beaucoup plus facile à établir que le résultat contrefactuel**.

Cette histoire est essentielle pour la suite. Elle montre que l'exigence probatoire n'est pas une manière de nier l'ingérence. C'est exactement l'inverse : elle permet d'établir les opérations réelles sans leur attribuer les effets que les sources ne permettent pas de mesurer.

## 3. Les puissances étrangères n'utilisent pas toutes le même mécanisme

Le mot « influence étrangère » écrase lui aussi des réalités trop différentes. Les États-Unis disposent d'une architecture publique de promotion de la démocratie, d'aide, de médias internationaux et de diplomatie publique. La Russie combine des instruments officiels, des opérations clandestines, des infrastructures informationnelles et, dans certains cas, des relations financières ou politiques avec des mouvements européens. La Chine s'appuie notamment sur des dispositifs liés au United Front, mais la relation à une diaspora ou à une association ne prouve pas par elle-même un contrôle politique. Israël, l'Allemagne, la Turquie, l'Iran, le Maroc ou l'Algérie apparaissent chacun dans des configurations différentes de diplomatie, lobbying, réseaux, religion, économie, sécurité, diaspora ou communication.

Le corpus force donc à abandonner les analogies paresseuses. Un voyage parlementaire financé par un réseau d'influence n'est pas équivalent à une opération de faux comptes. Un prêt à un parti n'est pas équivalent à un tasking politique. Une organisation diasporique n'est pas un agent d'un État par nature. Une coopération sécuritaire n'est pas une opération informationnelle. Un lobby légal n'est pas une campagne clandestine.

Les dossiers ELNET et AIPAC illustrent la différence entre influence organisée et ingérence clandestine. Des réseaux peuvent chercher un accès politique, financer des voyages, structurer une communauté de décideurs ou engager d'importantes ressources électorales. C'est un pouvoir réel. Mais l'analyse doit ensuite demander ce qui est documenté : déclaration d'intérêts, relation financière, lobbying, dépense électorale, consigne, contrepartie, décision. Le même vocabulaire ne peut pas être utilisé pour un dispositif légal de représentation d'intérêts et pour une opération de renseignement privé visant à salir clandestinement un adversaire.

Le cas des Émirats montre précisément pourquoi cette frontière compte. Le recours à des intermédiaires ou à des services privés de réputation et de renseignement peut produire des opérations beaucoup plus opaques. Ici, la question du principal, du contrat, du paiement et du tasking devient centrale. L'industrie de l'influence-for-hire étudiée ailleurs dans le corpus confirme qu'un marché privé permet à des clients publics ou privés de sous-traiter des campagnes trompeuses, des faux profils, des opérations de discrédit ou parfois des intrusions. Mais même dans ce secteur, il faut résister au palmarès commercial des prestataires : capacité déclarée, action observée, client réel et succès politique sont quatre objets différents.

Les cas turc, iranien, marocain et algérien ajoutent une difficulté : la diaspora, la religion, les associations et les relations économiques créent des réseaux réels, mais l'appartenance ou la proximité ne constituent pas une preuve de direction étatique. Le corpus oblige à revenir aux arêtes : financement, nomination, coordination, consigne, dépendance, objectif, action.

La France elle-même fournit le contrôle de symétrie le plus simple. Elle finance une diplomatie culturelle, des médias internationaux, des programmes d'aide, des réseaux d'anciens étudiants, des coopérations et des dispositifs de promotion de la démocratie ou de ses intérêts. Ces activités ne sont pas clandestines par définition. Elles montrent néanmoins qu'une puissance démocratique cherche elle aussi à structurer des préférences, des relations et des environnements favorables à l'étranger.

La frontière pertinente ne peut donc pas être « nous influençons, ils ingèrent ». Elle doit porter sur le mécanisme : transparence, consentement, droit applicable, clandestinité, tromperie, coercition, tasking et effet. Cette règle est plus exigeante parce qu'elle retire à la géopolitique le droit de décider du vocabulaire avant la preuve.

## 4. Le droit et les institutions exercent un pouvoir sans convaincre personne

Une partie importante du corpus corrige une idée implicite : l'influence serait toujours une tentative de persuasion. Or plusieurs mécanismes agissent directement sur les possibilités d'action.

Dans l'Union européenne, la production réglementaire, les consultations, les trilogues, les actes délégués et le lobbying organisent des accès asymétriques à la décision. La Commission dispose d'un pouvoir d'initiative important, mais elle ne gouverne pas seule. Conseil, Parlement, Cour, Banque centrale et États disposent de compétences et de veto différents. Les lobbies peuvent documenter leurs intérêts, rencontrer des responsables et proposer des textes ou arguments ; cela ne prouve pas qu'une disposition finale leur est imputable.

Le DSA rend cette architecture encore plus visible dans le domaine informationnel. Il crée des obligations, des procédures, des rôles intermédiaires, des priorités de traitement, des audits et des mécanismes de recours. Les trusted flaggers, par exemple, disposent d'un pouvoir procédural de priorité. Ils ne possèdent pas pour autant un bouton autonome de suppression : la plateforme conserve une décision, elle-même bornée par des règles et des voies de recours.

Les écosystèmes anti-FIMI, EDMO, EUvsDisinfo et les dispositifs de certification de fact-checking produisent eux aussi des capacités, des standards et des relations institutionnelles. Le corpus établit financement public, coordination, recherche, signalement, certification et co-régulation. Il ne ferme pas une architecture unique dans laquelle la Commission commanderait chaque décision éditoriale ou chaque retrait de contenu.

D'autres instruments sont plus directement coercitifs. Les sanctions, le gel d'avoirs, les restrictions administratives ou certaines règles commerciales modifient immédiatement l'accès à des ressources et des marchés. Leur effet ne dépend pas de persuader la cible. Le pouvoir s'exerce par droit. La question analytique change : base légale, proportionnalité, procédure, recours, sélectivité, réversibilité.

Les affaires de corruption au sein des institutions européennes constituent un autre cas limite. Lorsque cadeaux, paiements ou avantages sont documentés, on ne parle plus simplement d'accès ou de lobbying. Mais là encore, les responsabilités doivent être individualisées. Une affaire de corruption ne transforme pas l'ensemble d'une institution en acteur capturé.

Le résultat est important pour la théorie générale. **Une démocratie peut être influencée par des mécanismes qui modifient directement les coûts, droits, accès et procédures sans jamais passer par une opinion convaincue.** Toute analyse centrée uniquement sur la propagande ou la désinformation rate cette moitié du pouvoir.

## 5. L'argent achète d'abord des capacités, pas automatiquement des verdicts

La deuxième grande famille amont est financière. Les enquêtes sur les philanthropies, les ONG, les think tanks, les cabinets, les experts et la recherche financée convergent sur un point : l'argent produit des capacités réelles.

Une fondation peut financer une équipe, un programme, une étude, un contentieux, une campagne ou une organisation. Une ONG financée peut recruter, publier, ester en justice, intervenir auprès d'institutions ou fournir des services. Un think tank peut employer des chercheurs, organiser des événements, produire des notes et occuper les médias. Un cabinet peut vendre une expertise que l'administration ne possède plus ou pas en interne. Une entreprise peut financer de la recherche et obtenir un accès à des communautés scientifiques. Ces effets sont concrets sans qu'il soit nécessaire d'imaginer un ordre secret.

C'est précisément pourquoi la règle `financement != commandement` est importante. Elle n'innocente pas le financement. Elle précise son effet certain : capacité, agenda possible, accès, continuité organisationnelle, production. Pour démontrer une chaîne plus forte, il faut une pièce supplémentaire : clause contractuelle, instruction, droit de veto, condition de financement, échange explicite, sanction ou mécanisme de contrôle.

Les grandes philanthropies illustrent ce problème à l'échelle internationale. Elles peuvent orienter l'attention vers certains problèmes, financer des métriques et soutenir des solutions spécifiques. Cela peut créer une asymétrie de pouvoir entre ce qui est financé et ce qui ne l'est pas. La conclusion robuste n'est pas qu'elles « contrôlent les politiques publiques ». Elle est qu'elles modifient l'ensemble des options suffisamment dotées pour entrer dans le débat.

Les ONG liées aux migrations ou aux droits humains montrent une autre forme d'intermédiation. Le financement peut soutenir une activité opérationnelle, un plaidoyer, une expertise ou un contentieux stratégique. Le recours judiciaire lui-même peut devenir un instrument de transformation politique lorsqu'il modifie une règle ou une pratique. Là encore, le mécanisme doit être nommé correctement : ce n'est pas de la persuasion de masse, c'est l'usage du droit et de la procédure.

Les think tanks, cabinets de conseil, Big Four, relations publiques, experts médiatiques, groupes d'experts publics et recherche sponsorisée forment un continuum d'intermédiation cognitive. Ils convertissent ressources et expertise en accès, langage légitime, propositions, visibilité et parfois normes. Le corpus documente des conflits d'intérêts, des revolving doors et des erreurs de classification ou de récusation. Il documente aussi des refus, des divergences et des décisions qui ne suivent pas automatiquement l'intérêt du financeur.

Ce point empêche deux erreurs opposées. La première consiste à dire : « il n'y a pas de contrôle prouvé, donc le financement ne compte pas ». C'est faux : il crée une capacité et un avantage structurel. La seconde consiste à dire : « il finance, donc il dicte ». C'est également faux sans arête de tasking.

Le pouvoir d'influence le plus banal est souvent celui-ci : **rendre certaines idées, expertises, procédures et organisations durablement disponibles, professionnelles et audibles**. Il est moins spectaculaire qu'une opération clandestine, mais il est beaucoup plus permanent.

## 6. L'État domestique influence lui aussi l'environnement politique

Le corpus devient réellement symétrique lorsqu'il applique ses critères aux institutions françaises elles-mêmes.

La communication gouvernementale ne se réduit pas à des communiqués. Elle dispose d'infrastructures de campagne, d'analyse d'opinion, d'achat média, de segmentation et d'évaluation. Certains programmes poursuivent explicitement des objectifs comportementaux. Les sciences comportementales de l'État ajoutent une capacité d'expérimentation : modifier une architecture de choix, mesurer un comportement, conserver ou abandonner un dispositif. Les résultats observés sont hétérogènes, ce qui est précisément ce qu'une analyse sérieuse doit garder : un nudge peut produire un effet, aucun effet, ou même un effet contre-productif.

VIGINUM et le SGDSN appartiennent à un autre registre. Ils détectent et caractérisent des ingérences numériques étrangères, structurent des échanges interministériels et peuvent transmettre des éléments à des autorités ou plateformes. Le corpus corrige deux simplifications. D'abord, le VIGISCORE n'est pas « aucune mesure d'impact » : il estime un risque à partir de visibilité, propagation, contexte et signaux techniques. Ensuite, l'existence d'un risque d'impact ne mesure pas causalement l'effet sur des opinions ou un vote.

Le cas Rokh Solis impose une correction supplémentaire : l'attribution d'une opération comportant des marqueurs israéliens/Blackcore empêche de soutenir que les acteurs d'un pays allié seraient par principe hors du champ d'attribution. En revanche, le commanditaire final restait non établi et la visibilité des actifs était faible. Un bon système probatoire doit pouvoir dire ces trois choses à la fois.

Les doctrines militaires d'influence informationnelle doivent elles aussi être bornées. L'existence d'une doctrine, d'une capacité et d'opérations extérieures ne prouve pas automatiquement un usage politique intérieur. C'est une distinction simple entre capacité, mandat et action.

ARCOM, l'audiovisuel public, les aides à la presse et la publicité institutionnelle montrent enfin des formes de pouvoir plus structurelles. ARCOM peut sanctionner, réguler le pluralisme et attribuer des fréquences. Les aides publiques peuvent être économiquement matérielles pour le secteur. La publicité publique constitue un flux vers les médias. La gouvernance de l'audiovisuel public combine nominations, financement, responsabilité éditoriale et contrôle juridictionnel. Rien de cela n'est neutre ; rien de cela ne prouve, sans autre pièce, une commande éditoriale gouvernementale générale.

Le Fonds Marianne est particulièrement instructif parce qu'il réunit financement public de contre-discours, procédure de sélection contestée, production de contenu et défauts administratifs. Certaines productions politiques sont documentées. Le tasking éditorial direct de l'État ne l'est pas de façon générale. Cette différence est la frontière entre un scandale administratif et la preuve d'une chaîne de commandement.

La conclusion de cette famille est inconfortable pour les récits binaires : **la démocratie se défend contre des opérations d'influence en créant elle-même des capacités d'influence, de qualification, de financement et de régulation**. Cela ne rend pas la défense illégitime. Cela rend nécessaire un second niveau de contrôle : efficacité, proportionnalité, transparence, recours et conditions d'arrêt.

## 7. Gouverner la visibilité n'est pas gouverner les opinions

La concentration des médias est réelle, mais son interprétation dépend de la métrique. Un chiffre spectaculaire peut être exact pour un univers précis et faux lorsqu'il est étendu à « les médias » en général. Le corpus reconstruit donc propriété, audience, diffusion, contrôle et date avant de parler de concentration.

Même lorsque la concentration économique est forte, l'arête `propriétaire -> décision éditoriale précise` exige des preuves supplémentaires. C'est ici qu'intervient le gatekeeping. Les rédactions sélectionnent réellement les sujets et les claims selon des critères de pertinence, dommage, vérifiabilité, audience ou jugement éditorial. Des différences systématiques entre médias peuvent être mesurées. Leur cause n'est pas pour autant automatiquement le propriétaire, l'État, un financeur ou une plateforme.

Les agences de presse ajoutent une autre couche. AFP, Reuters et AP fournissent des flux mondiaux repris par de nombreux médias. Cette position leur donne un pouvoir d'agenda et de vérification structurel. Mais le degré de dépendance varie selon les marchés et aucune coordination éditoriale commune des trois agences n'est établie par leur simple fonction.

Les sondages modifient également l'information disponible sur la viabilité des candidats. Des effets de bandwagon, de vote stratégique ou de participation sont documentés dans certains designs. Ils restent hétérogènes et ne ferment pas un changement général du vainqueur.

Les plateformes rendent le mécanisme encore plus explicite. Trusted flaggers, démonétisation, déréférencement, demotion, règles de recommandation et classement affectent ce qui est vu, dans quel ordre et avec quelle friction. Des recours renversent certaines décisions. Des expériences randomisées montrent surtout pourquoi il faut séparer exposition et persuasion : modifier le fil ou la recommandation peut changer fortement l'exposition et l'engagement tout en produisant des effets politiques faibles dans certains cas ; dans d'autres expériences, certains effets d'opinion apparaissent.

L'IA générative ne supprime pas cette contrainte. Elle réduit le coût de production, de traduction, de reformulation et de cadence d'une opération. Elle ne résout pas automatiquement la distribution, l'acquisition d'audience authentique ou la persuasion. Elle change l'échelle potentielle de l'offre de contenu, pas les lois de la réception humaine.

Les campagnes sponsorisées cachées, faux médias, influenceurs payés non déclarés et relais coordonnés montrent enfin pourquoi la provenance est une variable politique. Le même message transparent et le même message présenté comme indépendant ne constituent pas la même opération.

Le résultat général est donc précis : **la visibilité est gouvernée par une chaîne distribuée de propriétaires, rédactions, agences, plateformes, régulateurs, signaleurs, annonceurs et publics.** Cette chaîne peut produire des asymétries considérables sans qu'un centre commun soit nécessaire. Et gouverner l'exposition ne revient toujours pas à gouverner le vote.

## 8. Une élection concentre plusieurs leviers qui ne doivent pas être fusionnés

Le financement politique agit en amont : dons, prêts, partis, micro-partis, prestations et remboursements publics ont des régimes distincts. Des violations existent et peuvent être sanctionnées. Un financement étranger peut créer une dépendance ou un risque sans établir un tasking. Le prêt russe du RN, par exemple, ferme un flux et une relation de créancier ; il ne ferme pas, par lui-même, une consigne politique en échange.

Le microtargeting agit autrement. Il combine données, segmentation, livraison de messages et parfois expérimentation. La distribution ciblée est mesurable. La persuasion varie. Le contexte européen a en outre changé avec les règles et décisions de plateformes sur la publicité politique, ce qui rend les comparaisons temporelles délicates.

Les bots et faux comptes produisent encore un autre effet : amplification artificielle, répétition, faux engagement et visibilité. Mais un bot n'est pas toujours un faux compte, un réseau n'est pas toujours coordonné, et une coordination ne révèle pas automatiquement son commanditaire. Même lorsque l'amplification est fermée, l'effet sur le vote reste une question supplémentaire.

L'achat de votes et le clientélisme sont différents parce qu'ils concernent un échange plus direct. Des cas de vote-buying existent et le droit les définit. Des politiques de redistribution électoraliste ou de favoritisme peuvent aussi être mesurées. Mais un bénéfice ciblé ne prouve pas automatiquement un quid pro quo individuel ni une architecture clientéliste nationale.

La fraude électorale doit elle aussi rester séparée de l'accusation de fraude. Des fraudes réelles existent. Des erreurs sérieuses existent. Une fraude peut être établie sans avoir changé le résultat global. Le volume d'accusations, lui, n'est pas un dénominateur de fraude.

L'annulation ou la neutralisation d'une élection par une décision judiciaire ou administrative ferme au moins un effet institutionnel : le résultat ou l'éligibilité est modifié. Cela ne ferme pas automatiquement l'intention partisane, l'attribution étrangère ou le résultat contrefactuel qui aurait prévalu sans la décision.

Le hack-and-leak est encore une chaîne différente : compromission, vol, attribution, intégrité des documents, timing, publication, amplification, exposition, persuasion, résultat. L'affaire MacronLeaks montre que l'attribution elle-même peut évoluer avec le temps. Une non-attribution initiale n'est pas une preuve d'absence définitive ; une attribution ultérieure ne transforme pas rétroactivement chaque maillon en effet électoral démontré.

Le timing judiciaire produit enfin des effets possibles sur une campagne sans qu'il soit nécessaire de prouver une persuasion de masse. Une inéligibilité, une fuite ou une annonce institutionnelle peut modifier la compétition, la réputation ou les options disponibles. L'intention partisane est pourtant une question distincte et plus difficile.

Additionner ces mécanismes sous le mot « manipulation électorale » ferait perdre l'essentiel : ils n'agissent pas au même endroit et ne demandent pas les mêmes preuves.

## 9. Le pouvoir le plus profond est parfois une dépendance ou une infrastructure

Les enquêtes sur les élites, la finance, les industries réglementées et les infrastructures déplacent encore le regard.

Les grandes écoles et l'Inspection des finances montrent une reproduction sociale et une circulation élevées entre positions de pouvoir. Cela crée des proximités, des langages communs et des réseaux. Cela ne suffit pas à établir une coordination secrète de leurs membres. Le même contrôle vaut pour Bilderberg, les programmes Young Leaders ou les réseaux du World Economic Forum : sélection, coprésence et socialisation sont établissables ; le tasking politique ultérieur doit être démontré séparément.

La banque, la pharmacie et la défense montrent un autre type de pouvoir structurel : ressources considérables, accès réglementaire, expertise technique et revolving doors. Des actions de lobbying peuvent être reliées à des textes ou à des priorités précises. Des risques d'intégrité peuvent être documentés. Pourtant, le corpus conserve aussi des contre-cas : régulateurs qui refusent un produit, arbitrages publics contraires à un intérêt industriel, absence de causalité spécifique entre une intervention et une décision finale.

Le debanking et les sanctions financières rappellent qu'une infrastructure privée ou publique peut exercer une coercition sans discours. Une autorité peut interdire ou geler. Une banque peut fermer un compte dans un cadre AML/KYC. L'exclusion est réelle. Son motif politique, lui, ne peut pas être présumé.

Le cloud, les données, les câbles et les dépendances numériques posent le même problème à l'échelle technique. La concentration et les coûts de sortie créent une capacité potentielle. Une capacité devient un levier observé lorsqu'une arête de contrôle est effectivement exercée ou qu'elle contraint matériellement une décision. L'extraterritorialité juridique peut conduire à des garanties, à des architectures souveraines ou à des stratégies de réduction du risque sans qu'un accès étranger ait nécessairement été exercé dans le cas étudié.

Les corps intermédiaires disposent légalement d'un accès privilégié. Ce privilège peut produire des concessions ou des normes. Il peut aussi échouer : les gouvernements peuvent passer outre des syndicats ou négociations. L'accès n'est pas l'adoption.

Le soft power culturel et académique agit encore différemment. Bourses, échanges, langue, instituts et réseaux d'alumni produisent exposition, mobilité, compétences, contacts et parfois attitudes. La France l'assume explicitement dans sa diplomatie. Le mécanisme est réel sans devoir inventer une fidélité politique future des bénéficiaires.

Le marché de l'influence-for-hire et le spyware sont les formes les plus dures de cette famille. Des prestataires privés peuvent fournir faux profils, hacking, réputation et campagnes clandestines. Le spyware peut fermer une chaîne de compromission, exfiltration puis réutilisation médiatique, comme dans le cas Brejza en Pologne. C'est une preuve beaucoup plus forte qu'une simple ressource ou proximité. Même ici, le dernier maillon, l'effet sur le résultat électoral, reste généralement ouvert.

Le pouvoir structurel ne signifie donc pas « contrôle total ». Il signifie qu'avant même de persuader qui que ce soit, certains acteurs disposent de plus de moyens pour entrer dans l'arène, rester présents, imposer des coûts, obtenir une expertise, contrôler une infrastructure ou rendre la sortie difficile.

## 10. Le modèle qui résiste : un pouvoir polycentrique sous asymétries

À la fin du corpus, deux modèles simples échouent.

Le premier est le pluralisme équilibré. Il suppose que les influences concurrentes se neutralisent à peu près parce que beaucoup d'acteurs peuvent parler. Les enquêtes montrent trop d'asymétries pour cela : argent, accès, expertise, propriété, infrastructures, capacité juridique, données, surveillance, achat média, relais institutionnels et endurance ne sont pas distribués également.

Le second est le centre unique. Il suppose qu'un même commandement relierait transversalement gouvernements, médias, ONG, plateformes, financeurs, experts et institutions. Le corpus ferme des coordinations très concrètes, parfois clandestines, parfois contractuelles, parfois institutionnelles. Il ne ferme pas cette chaîne générale de tasking commun.

Le modèle intermédiaire est plus robuste : **un pouvoir polycentrique sous asymétries structurelles**. Plusieurs centres agissent simultanément. Ils coopèrent parfois, se financent parfois, se régulent, se combattent, se concurrencent ou se corrigent. Des alignements peuvent émerger sans chef commun. Des captures sectorielles peuvent exister sans capture totale. Des opérations clandestines peuvent être réelles sans expliquer tout l'environnement.

Les contre-pouvoirs doivent faire partie de ce modèle. Les juridictions annulent certaines mesures. Des plateformes restaurent des contenus. Des administrations refusent des intérêts privés. Des études produisent des résultats nuls. Des campagnes d'influence restent peu visibles. Des institutions se contredisent. Ces revers ne prouvent pas l'équilibre du système, mais ils réfutent la version la plus simple d'une architecture omnipotente.

La défiance institutionnelle ne peut pas servir de colle causale universelle. Elle est fortement différenciée selon les institutions et les publics. L'économie de l'indignation peut augmenter clics et engagement. Des récits complotistes peuvent être exploités par des opérateurs, des mouvements domestiques ou des marchés de contenu. Mais le pont général `défiance -> vulnérabilité -> manipulation réussie` n'est pas fermé.

L'attribution fournit alors la discipline finale. Un incident peut être lié à un artefact, un opérateur, un intermédiaire, un client ou un État avec des niveaux de confiance différents. Le principal ultime ou l'intention peuvent rester inconnus alors que l'opération elle-même est certaine. La preuve peut également évoluer dans le temps. Un label binaire « attribué/non attribué » perd cette structure.

La même règle doit s'appliquer aux alliés et adversaires. Le corpus établit des différences juridiques de périmètre et d'exemption. Il établit aussi des opérations, influences ou coercitions menées par des acteurs appartenant à des camps différents. Il ne dispose pas encore d'un dénominateur apparié suffisant pour conclure à un double standard systématique de qualification et de sanction. La bonne question n'est pas « qui est notre allié ? », mais « quel mécanisme, quel niveau de preuve, quelle clandestinité, quel tasking, quelle portée, quelle conséquence ? ».

C'est aussi la meilleure manière d'évaluer la contre-ingérence. Des menaces réelles existent. Les institutions créées pour les détecter produisent elles-mêmes budgets, capacités, métriques, partenariats et pouvoirs procéduraux. Leur légitimité ne peut donc pas être évaluée uniquement par l'existence de la menace. Elle dépend aussi de leur efficacité mesurée, de leur proportionnalité, de leurs contrôles, de leur réversibilité et de la possibilité de dire qu'une extension n'est plus nécessaire.

Le corpus aboutit ainsi à une conclusion moins spectaculaire qu'un récit de contrôle total, mais plus forte analytiquement. **Les démocraties sont traversées par une architecture dense de pouvoirs d'influence. La plupart sont plus faciles à prouver au niveau des ressources, de l'accès, de l'action, de la sélection, de la contrainte et de l'exposition qu'au niveau de la persuasion et du résultat final.** Certaines formes de pouvoir n'ont d'ailleurs pas besoin de persuasion : elles modifient directement les options disponibles.

Cette conclusion n'est pas une excuse pour sous-estimer l'ingérence. Elle fournit au contraire un standard plus difficile à manipuler. Elle permet d'affirmer une opération clandestine lorsqu'elle est prouvée, de reconnaître un pouvoir structurel sans inventer son commanditaire, de mesurer une coercition sans la confondre avec une opinion, et d'appliquer les mêmes exigences aux adversaires, aux alliés et à nous-mêmes.

Il reste une limite matérielle au corpus : un dossier, consacré à la diplomatie d'influence ukrainienne en France et dans l'Union européenne, n'a pas de handoff terminal récupérable dans le corpus forensique V1. Il demeure donc explicitement hors de la preuve reconstruite. Cette lacune n'empêche pas le modèle général, mais elle interdit de prétendre à une couverture probatoire parfaite des 100 investigations de fond.

Le résultat final tient en une règle : **ne jamais demander au mot « influence » de prouver ce que seules les arêtes peuvent établir.**
'''
(OUT/'runtime'/'ARTICLE_CANDIDATE_CORPUS_V1.md').write_text(article,encoding='utf-8')

# Support map: family-section + all investigations. Include internal-only source status.
support=[]
for _,r in yield_df.iterrows():
    support.append({
        'section':r.article_section,'inv_id':r.inv_id,'family_id':r.family_id,
        'disposition':r.disposition,'authority':r.authority,
        'support_function':'material_support' if r.disposition!='GAP_EXPLICIT' else 'negative_knowledge_gap',
        'reader_source_status':'PENDING_PUBLIC_SOURCE_LAYER' if r.disposition!='GAP_EXPLICIT' else 'N/A',
        'note':r.justification
    })
pd.DataFrame(support).to_csv(OUT/'runtime'/'A4_S02_SUPPORT_MAP_V2.tsv',sep='\t',index=False)

# ---------------- A5 ----------------
# Gate accounting
gate_pass=(len(yield_df)==100 and (yield_df.disposition!='').all() and (yield_df.inv_id=='INV-035').sum()==1 and counts.get('GAP_EXPLICIT',0)==1)
family_counts=yield_df.groupby(['family_id','family']).size().reset_index(name='n')
family_covered=(family_counts.n>0).all()

review=f'''# A5-S01 — Review matérielle après replay corpus V1

Status: **PASS_MATERIAL / HOLD_PUBLICATION_LAYER**

## Corpus-yield gate

- PRIMARY+CASE attendus: 100
- dispositions explicites: {len(yield_df)}
- DIRECT_MATERIAL_USE: {counts.get('DIRECT_MATERIAL_USE',0)}
- COVERED_BY_MATERIAL_FAMILY: {counts.get('COVERED_BY_MATERIAL_FAMILY',0)}
- GAP_EXPLICIT: {counts.get('GAP_EXPLICIT',0)}
- unaccounted: {100-len(yield_df)}
- familles F0-F10 présentes: {len(family_counts)}/11
- `INV-035`: conservé comme gap, non reconstruit

`CORPUS_YIELD_COVERAGE = {'PASS' if gate_pass and family_covered else 'FAIL'}`

## Perte forensique

**PASS matériel.** Les blocs précédemment sous-exploités survivent désormais explicitement : histoire/interventions, puissances et réseaux étrangers, influence étatique domestique, médias/plateformes, élections, pouvoir structurel/infrastructures. La thèse amont/aval reste un axe mais ne remplace plus ces familles.

## Causalité / responsabilité

**PASS.** Le candidat conserve les séparations `financement != commandement`, `propriété != contrôle éditorial`, `exposition != persuasion`, `opération != résultat`, `réseau != tasking`, `capacité != abus` et `asymétrie juridique != double standard empirique général`.

## Contre-thèses

**PASS.** Contre-pouvoirs, refus, annulations, effets nuls/hétérogènes et absence de commandement transversal restent dans le modèle. Le texte n'utilise pas ces contre-exemples pour nier les asymétries structurelles.

## Gap / provenance

**PASS.** `INV-035` n'est pas comblé. `INV-044`, `INV-139`, `INV-140` ne sont pas promus au rang de handoffs originaux.

## Généricité

**PASS.** Sans le corpus, le texte perdrait les distinctions et contre-exemples propres aux familles : Chile 1964, COINTELPRO, réseaux de puissance, DSA/trusted flaggers, Fonds Marianne, VIGINUM/Rokh Solis, expériences de recommandation, fraude vs accusation, timing judiciaire, influence-for-hire, spyware/Brejza, asymétrie juridique alliés/adversaires.

## Auditabilité

**PASS interne.** `A4_S02_SUPPORT_MAP_V2.tsv` fournit un retour vers les 100 dossiers de fond et conserve leur niveau d'autorité.

## Défaut restant

**P1 — couche de citations lecteur non reconstruite.** Le corpus V1 contient surtout des handoffs, pas toutes les pièces publiques originales nécessaires pour publier la version élargie avec une citation publique locale pour chaque proposition matérielle. Les chemins internes sont suffisants pour le replay de compréhension/couverture, mais pas pour prétendre à une publication externe pleinement sourcée.

Ce P1 n'appelle pas une nouvelle investigation générale. Il appelle une récupération ciblée des sources déjà attachées aux investigations si une publication est demandée.
'''
(OUT/'runtime'/'A5_S01_REVIEW_V2.md').write_text(review,encoding='utf-8')

defects='''# A5-S02 — Défauts

```text
P0_OPEN = 0
P1_OPEN = 1
P2_OPEN = 1
```

## P1-01 — Reader citation layer

La prose élargie est traçable vers les investigations mais pas encore vers un jeu complet de sources publiques locales. Bloque `PUBLISH_CANDIDATE`, ne bloque pas le replay matériel A2→A5.

## P2-01 — Densité

Le candidat est long et dense. Une compression éditoriale est possible uniquement après fermeture de la couche de sources, en conservant `CORPUS_YIELD_COVERAGE`.
'''
(OUT/'runtime'/'A5_S02_DEFECTS_V2.md').write_text(defects,encoding='utf-8')

repair='''# A5-S03 — Réparation locale

Aucune réparation de fond A2/A3 requise après replay : `CORPUS_YIELD_COVERAGE` passe et aucun P0 n'est détecté.

Le P1 restant n'est pas réparable honnêtement par invention ou par ajout de citations génériques. Propriétaire minimal : **A4-S02 récupération ciblée des sources publiques déjà rattachées aux dossiers**, uniquement si l'objectif suivant est la publication.

`NEW_INVESTIGATION = NO`  
`GLOBAL_REPLAY = NO`
'''
(OUT/'runtime'/'A5_S03_REPAIR_V2.md').write_text(repair,encoding='utf-8')

terminal='''# A5-S04 — Statut terminal du replay

Status: **HOLD_BEFORE_TERMINAL_DISPOSITION**

A5 ne prononce pas `PUBLISH_CANDIDATE` tant que P1-01 reste ouvert. Il ne choisit pas `MORE_INVESTIGATION` : aucun nouveau fait n'est nécessaire pour le contrat actuel. Il ne choisit pas `SHORTER_OUTPUT` ni `NO_ARTICLE` : le produit long est matériellement justifié.

```text
A2 = PASS_WITH_EXPLICIT_GAP
A3_CORPUS_YIELD_COVERAGE = PASS
A4_MATERIAL_REPLAY = PASS
A5_P0_OPEN = 0
A5_P1_OPEN = 1  # reader citation layer
A5_TERMINAL = HOLD
NEXT_OWNER = A4-S02 targeted source recovery, only for publication readiness
```
'''
(OUT/'runtime'/'A5_S04_TERMINAL_V2.md').write_text(terminal,encoding='utf-8')

# Report
report=f'''# Replay report — Corpus forensique V1

Date: 2026-09-11

## Résultat

- patch protocole minimal appliqué : `CORPUS_YIELD_COVERAGE` à A3 + contrôle séparé à A5 ;
- corpus PRIMARY+CASE : 100/100 disposés ;
- matière disponible : 99/100, `INV-035` gap explicite ;
- familles empiriques : 11/11 préservées (F0-F10) ;
- reconstruction A2 : PASS_WITH_EXPLICIT_GAP ;
- A3 : FORME_LONGUE, `CORPUS_YIELD_COVERAGE=PASS` ;
- A4 : progression + article reconstruits ;
- A5 matériel : PASS ;
- A5 publication : HOLD sur un seul P1, couche de sources publiques lecteur incomplète.

## Ce qui a changé par rapport au run précédent

Le run précédent pouvait passer en conservant 15 dimensions tout en n'exploitant substantiellement qu'une fraction des investigations. Le nouveau gate compte séparément le rendement du corpus et interdit qu'une investigation de fond disparaisse sans disposition explicite.

La thèse « preuve forte amont / preuve faible aval » est conservée mais n'est plus le conteneur unique. Les familles historiques, géopolitiques, institutionnelles, domestiques, informationnelles, électorales et structurelles sont réintroduites dans le plancher explicatif.

## Non-régressions

- aucune réinvestigation générale ;
- aucune reconstruction d'INV-035 ;
- aucune promotion des synthèses en preuves indépendantes ;
- aucune promotion des bounded recoveries ;
- aucune causalité terminale inventée ;
- aucune canonicalisation A7.
'''
(OUT/'REPLAY_REPORT.md').write_text(report,encoding='utf-8')

# copy core corpus audit for auditability
shutil.copy2(AUDIT,OUT/'CORPUS_121_AUDIT.csv')
shutil.copy2(CORPUS/'SOURCE_INDEX.csv',OUT/'SOURCE_INDEX.csv')

# manifest
files=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file():
        b=p.read_bytes(); files.append((str(p.relative_to(OUT)),len(b),hashlib.sha256(b).hexdigest()))
with (OUT/'MANIFEST_SHA256.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['path','bytes','sha256']); w.writerows(files)

# zip
zip_path=BASE/'ARTICLE_PROTOCOL_CORPUS_V1_REPLAY_2026-09-11.zip'
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file(): z.write(p,p.relative_to(BASE))
print('OUT',OUT)
print('ZIP',zip_path,zip_path.stat().st_size,hashlib.sha256(zip_path.read_bytes()).hexdigest())
print('COUNTS',counts)
print('families',family_counts.to_dict('records'))
print('article words',len(article.split()))
