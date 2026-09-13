ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-1002-quotas-controle-acces-vs-flux-decheteries | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_quotas-controle-acces-vs-flux-decheteries/2026-08-31_10-02_quotas-controle-acces-vs-flux-decheteries_INPUT.txt | SUBJECT_SLUG:quotas-controle-acces-vs-flux-decheteries | SUBJECT_FP:sha256:28144c5a7eba0f0101116f9fb6e825cb953ca033ebfff7e8c3b7927518dccd44 | INPUT_SHA256:sha256:3a69cab19c210e25cb7b21c34bab36593297309927cee6576d63739bb3e0d39b
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['EPCI', 'syndicats', 'ADEME', 'AMORCE', 'menages', 'professionnels'], 'domains': ['dechets', 'decheterie', 'controle-acces', 'quotas', 'flux'], 'geo': 'France (EPCI documentes: AMP, Point Fort, SYDED 87, Loire Forez, Troyes)', 'lead_question': 'Quel quota de controle d acces frappe quel flux (encombrants vs gravats vs verts, DDS, pneus) par EPCI ?', 'limits': 'effets mesures agregees (DT138 21 CL); aucun EPCI ne publie tonnages x flux avant/apres quota isole', 'object_question': '(1) grilles de quota par EPCI ; (2) effets par flux ; (3) confondants climat/perimetre/pros'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Croiser les quotas de contrôle d'accès avec la structure des flux : quel quota frappe quel flux ?

**Run `20260831-1002-quotas-controle-acces-vs-flux-decheteries`** — croisement de la grille des quotas (passes 2103/2123) avec la structure des flux par EPCI, pour répondre : quel quota frappe quel flux (encombrants vs gravats vs verts, DDS, pneus) ?

## Ce que l'enquête établit

### 1. Deux mécanismes de quota, deux flux frappés (FCT-001, FCT-002, FCT-010)

**Le quota générique de passages** (18 à 36/an selon l'EPCI : AMP 36, Gard 36, Cyclad 24, Point Fort 18, Pays sabolien 18) compte les visites, indépendamment du flux. Son unité de compte est la fréquence : il frappe d'abord le flux des petits apports fréquents, la benne tout-venant résiduelle. C'est le flux le plus touché de tout le dispositif : **-35 % en médiane** (DT138, 8 collectivités), et **-34,7 % pour les encombrants traités** au centre de Point Fort l'année du pass QR (5 574 t contre 8 541 t).

**Le quota de volume ou par flux** (m³ par jour ou par visite, kg, unités) plafonne un flux précis : **verts** (AMP 3 m³/jour, SYDED 87 : 20 passages + 10 m³/an/foyer depuis 2019), **gravats** (AMP 3 m³/jour, un cas à 500 kg/jour), **DDS** (AMP 75 kg/jour), **pneus** (AMP 4/jour). Les recyclables sous REP (cartons, ferraille, piles) sont généralement exempts. Les baisses mesurées : verts -20 %, gravats -20,4 %.

**AMP est le seul EPCI documenté avec une grille par flux complète** (verts + gravats + pneus + DDS en plus des passages). Partout ailleurs, la grille est générique (passages + volume/visite) ou ne vise qu'un flux isolé (SYDED verts, gravats 500 kg/jour). La granularité de la grille est un choix local, sans cadre national.

### 2. Le cas clinique Point Fort (Manche) : le quota passages frappe l'encombrant (FCT-005, FCT-006)

Point Fort Environnement (11 déchèteries, ~117 000 hab) instaure le pass déchèterie au 01/01/2023 : 18 passages/foyer/an. Bilan 2023 : **fréquentation -28 %** (250 482 véhicules vs 349 587), **tonnages -29 %** (36 035 t vs 50 910 t), **340 kg/hab vs 397**. Le RPQS constate « une baisse des flux collectés, par habitant, notamment concernant les gravats et les encombrants ». Structure du territoire : verts 46 % des apports (16 335 t), gravats 17 % (6 115 t), encombrants 15 % (5 503 t) — profil rural, très différent de la moyenne nationale (verts 27-29 %). Confondants nommés par le RPQS lui-même : retrait de 2 déchèteries (St-Sauveur Villages, Périers) et fin des double comptes à Saint-Lô. Les pros restent admis payants (237 038 € de recettes 2023).

### 3. Le témoin sans quota : la baisse n'est pas qu'une affaire de quota (FCT-007, FCT-008)

Loire Forez (aucun contrôle d'accès documenté) : tonnages stables +0,6 % en 2024, mais **encombrants -13 % et gravats -5 %** quand même, et **verts +21 %** (climat pluvieux). Troyes (sans quota) : **verts +15 % = premier flux déchèterie** (6 045 t), gravats -7 %. Le climat fait varier les verts de +15 à +30 % selon les années.

**Conséquence épistémologique** : le -35 % tout-venant sous quota est un signal net (écart avec le -13 % sans quota), mais le partage quota/climat n'est isolé par aucune source. DT138 le reconnaît explicitement : « Il est difficile d'isoler l'effet des quotas d'accès » (modification des tarifs pros, interdictions, COVID, déstockage avant mise en service).

### 4. Le croisement quota × flux par EPCI documenté

| EPCI | Grille | Flux frappé en premier |
|---|---|---|
| AMP (Aix-Marseille) | 3 pass/j, 36/an + 3 m³ verts/j + 3 m³ gravats/j + 4 pneus + 75 kg DDS | verts, gravats, DDS (par flux) + tout-venant (passages) |
| Point Fort (Manche) | 18 passages/an | encombrants (-34,7 % au traitement), gravats par habitant |
| SYDED 87 (Haute-Vienne) | 20 passages + 10 m³/an de verts (2019), envisage 5 m³/an | verts (seul flux visé) |
| Gard rhodanien | 36/an, 3 dépôts/j, 2 m³/visite | verts/gravats via m³ + fréquents |
| Cyclad / Pays sabolien / Rochefort / La Rochelle / Niort | 24 / 18 / 18 / 20 / 24 passages | tout-venant (fréquence) |
| Loire Forez / Troyes | aucun quota | — (témoins) |

## Le mécanisme causal (CAU-001, CAU-002)

1. **Quota passages → baisse disproportionnée du tout-venant** : le passage est l'unité de compte ; les usagers regroupent leurs apports, les plus fréquents (tout-venant) sont dépassés en premier. DT138 documente même l'optimisation : fréquentation -50 % pour des tonnages -28 %.
2. **Quota volume/par flux → contrainte directe des flux volumineux** : verts et gravats sont plafonnés indépendamment du nombre de passages ; ce sont les deux flux « hors bac » (81 % de l'apport déchèterie, passe 0942) les plus massifs.

## L'articulation avec la fresque

Le contrôle d'accès n'est pas un simple compteur : **sa grille détermine quel flux est exclu selon l'EPCI**. Un rural (verts dominants) subit le quota passages sur ses encombrants ; une métropole (AMP) plaque une grille par flux qui cible verts, gravats et DDS ; l'exclusion des pros 2025-2026 (AMP, Nice, Lyon…) frappe gravats et DIB en premier. Le « même » contrôle d'accès produit des exclusions de flux différentes selon le territoire et la granularité choisie — c'est la fragmentation du verrou (passe 2123) portée au niveau du flux.

## GAPs restants

- **Aucun EPCI ne publie sa ventilation tonnages × flux avant/après quota isolée** des autres causes (climat, périmètre, pros, COVID). Point Fort est le seul cas exploitable (RPQS 2022 vs 2023).
- Pas de recensement national des grilles de quota par flux.
- Effet de l'exclusion pros 2025 sur les tonnages gravats AMP (2024 vs 2025) non encore publié.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:3|AXS:3|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"AMP (grille par flux) vs Point Fort (passages) vs Loire Forez/Troyes (sans quota)","note":"la grille (passages vs m3 vs par flux) n'est jamais publiee par rapport a la structure des flux de l'EPCI","routes":["reglements EPCI","RPQS","DT138","presse locale"],"status":"SATURATED","title":"Quel quota frappe quel flux : la grille de controle d'acces determine le flux exclu selon l'EPCI"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le quota de PASSAGES frappe d'abord le tout-venant/encombrants (flux des petits apports frequents : -35% mediane DT138, -34,7% a Point Fort), tandis que les quotas VOLUME ou par flux ciblent verts et gravats (SYDED verts, gravats 500 kg/jour, AMP m3/jour)","counter":"Les baisses d'encombrants (-13%) et gravats (-5%) existent aussi SANS quota (Loire Forez) et le climat fait varier les verts de +15 a +30% : le partage quota/climat n'est pas isole par les sources","gap":"Aucun EPCI ne publie sa ventilation tonnages x flux avant/apres quota isolee des autres causes","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-006","FCT-007","FCT-008"]}
CLM-002 | {"claim":"AMP est le seul EPCI documente avec une grille de quota PAR FLUX complete (3 m3 verts, 3 m3 gravats, 4 pneus, 75 kg DDS par jour) ; les autres EPCI a quota documentes (Point Fort 18, Gard 36, Cyclad 24, Pays sabolien 18) n'ont que passages et volume/visite - la granularite de la grille est un choix local, pas une norme","counter":"DT138 documente d'autres limites flux isolees (SYDED verts, gravats 500 kg/jour, huiles L, pneus) : la grille par flux existe hors AMP, mais fragmentaire","gap":"Pas de recensement national des reglements decheteries par flux","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-005"]}
CLM-003 | {"claim":"La structure des flux determine l'impact du quota : un EPCI rural a flux verts dominants (Point Fort : verts 46%) subit le quota passages sur ses encombrants (-34,7%), alors que les villes a tout-venant dominant subissent le -35% sur la benne residuelle - le meme quota frappe des flux differents selon le territoire","counter":"DT138 agrege 21 collectivites sans decomposition territoriale ; Point Fort a des confondants (2 sites retires, double comptes)","gap":"Pas de croisement public quota x structure des flux par EPCI","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-006","FCT-009"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Quels quotas de controle d'acces existent par EPCI et quel flux frappent-ils (encombrants vs gravats vs verts, DDS, pneus) ?","routes":["AUDIT","EXPAND"],"sought_objects":["quotas passages vs volume par flux","grilles AMP","SYDED verts","gravats 500 kg","effets par flux DT138"],"status":"SATURATED"}
AXS-002 | {"question":"Quel est l'effet mesure des quotas par flux (tout-venant -35%, verts -20%, gravats -20,4%) et quels sont les confondants (climat, perimetre, pros, COVID) ?","routes":["AUDIT"],"sought_objects":["baisse par flux DT138","Point Fort encombrants -34,7%","Loire Forez sans quota","Troyes verts +15%"],"status":"SATURATED"}
AXS-003 | {"question":"Y a-t-il des EPCI avec quota qui publient leur ventilation tonnages x flux avant/apres mise en place ?","routes":["EXPAND"],"sought_objects":["RPQS quota avant apres","Point Fort 2022-2023","SYDED 87 tonnages verts"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Quota generique de passages (18-36/an) calibre a ~2x la moyenne reelle","effect":"Baisse disproportionnee du tout-venant/encombrants (-35% mediane DT138, -34,7% a Point Fort) - le flux des petits apports frequents est le premier depasse","mechanism":"Le passage est l'unite de compte : les usagers regroupent leurs apports, les plus frequents (tout-venant) trinquent d'abord ; DT138 : frequentation -50%/tonnages -28% = optimisation des deplacements","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-010"]}
CAU-002 | {"cause":"Quota de volume (m3/jour ou par visite) ou par flux (verts, gravats, DDS, pneus)","effect":"Contrainte directe des flux volumineux : verts (SYDED 20 passages + 10 m3/an, AMP 3 m3/jour), gravats (AMP 3 m3/jour, 500 kg/jour), DDS (75 kg/jour) - les baisses mesurees verts -20% et gravats -20,4%","mechanism":"L'unite de compte est le volume ou l'unite : le flux volumineux est plafonne independamment du nombre de passages ; les recyclables sous REP (cartons, ferraille, piles) sont generalement exempts","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-002"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-1ca3694a-dt138-quotas | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | Aix-Marseille métropole déchèterie règlement 2025 quota mètres cubes déchets verts gravats pneus professionnels exclusion
QRY-002 | FETCH | INSPECTED | SRC-001 | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | AMP reglement decheteries 2025 quotas par flux
QRY-003 | WEB | OK | - | - | contrôle accès déchèterie quota effet tonnages par flux tout-venant encombrants verts gravats baisse pourcentage ADEME AMORCE DT138
QRY-004 | FETCH | INSPECTED | SRC-002 | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | DT138 PDF inspecte pdftotext effets quotas par flux verts gravats tout-venant SYDED 87
QRY-005 | WEB | OK | - | - | déchèterie tonnages par flux encombrants déchets verts gravats EPCI rapport annuel 2024 collectivité répartition
QRY-006 | FETCH | INSPECTED | SRC-003 | https://www.pointfortenvironnement.fr/wp-content/uploads/2024/06/DEL2024-14-Rapport_annuel_2023.pdf | Point Fort Environnement RPQS 2023 pass decheterie 18 passages flux gravats encombrants
QRY-007 | FETCH | INSPECTED | SRC-004 | https://www.loireforez.fr/wp-content/uploads/2025/07/Rapport-annuel-2024.pdf | Loire Forez RPQS 2024 flux encombrants gravats verts sans quota
QRY-008 | FETCH | INSPECTED | SRC-005 | https://troyes-champagne-metropole.fr/wp-content/uploads/2026/04/Rapport_Annuel_Collecte_TCM_2024.pdf | Troyes Champagne Metropole 2024 verts premier flux decheterie gravats -7%

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/
SRC-002 | ◈ | fam:A | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download
SRC-003 | ◈ | fam:A | https://www.pointfortenvironnement.fr/wp-content/uploads/2024/06/DEL2024-14-Rapport_annuel_2023.pdf
SRC-004 | ◈ | fam:A | https://www.loireforez.fr/wp-content/uploads/2025/07/Rapport-annuel-2024.pdf
SRC-005 | ◈ | fam:A | https://troyes-champagne-metropole.fr/wp-content/uploads/2026/04/Rapport_Annuel_Collecte_TCM_2024.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | A | 2025-07-01 | AMP : grille de quota par flux (seul EPCI documente avec grille complete) | Metropole Aix-Marseille-Provence, reglement decheteries adopte 27/02/2025, en vigueur 01/07/2025 (page officielle INSPECTEE): acces reserve aux habitants; 3 passages max/jour, limite de 36 visites/an; quantites limitees PAR TYPE DE DECHETS: 3 m3 dechets verts/jour, 3 m3 gravats/jour, 4 pneus/jour, 75 kg dechets diffus specifiques (DDS)/jour. Professionnels exclus a compter du 01/07/2025. Alternatives pros: points OCAB pour le batiment, reprise pneus en garages. C'est la seule grille documentee combinant quota passages ET quotas par flux (verts+gravats+pneus+DDS). | 5ecfd657-8f14-4a47-aa9e-3057f7b41275
FCT-002 | FACT | ✧ | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | A | 2025-11-07 | DT138 : baisse mediane -24% a 12 mois, par flux : verts -20%, gravats -20,4%, tout-venant -35% | AMORCE/ADEME DT138 (enquete modalites d'acces en decheterie publique, 21 collectivites, PDF INSPECTE cette session) : baisse mediane des tonnages -24% a 12 mois de mise en place des quotas (8 valeurs); par flux : dechets verts -20% (mediane), gravats -20,4%, benne tout-venant residuel en melange -35% (le plus fort). Un cas : frequentation -50% avec baisse moyenne des tonnages -28% (optimisation des deplacements par les usagers). | 3d493220-c9c3-46cc-b1bc-f7d58b455155
FCT-003 | FACT | ✧ | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | A | 2025-11-07 | DT138 : quotas visant UN SEUL flux (verts SYDED 87, gravats 500 kg/jour) | DT138 INSPECTE : 2 collectivites limitent UNIQUEMENT les dechets verts (principal flux decheterie, saisonnier) ; Focus SYDED 87 (Haute-Vienne) : depuis 01/07/2019 apports verts limites a 20 passages et 10 m3/an/foyer ; 2023 : 11 700 t de vegetaux (+5% vs 2022), 149 kg/foyer/an ; le SYDED envisage 5 m3/an ou 10 passages. Autres limites flux : huiles alimentaires 10 L (1 cas), huiles de vidange 15 L (1 cas), pneus en unites ; un cas rehausse la limite UNIQUEMENT pour les gravats a 500 kg/jour. Les recyclables sous REP (cartons, ferraille, piles) ne sont generalement pas vises. | c6302ed1-964a-4cdf-be28-c09b52ab79e6
FCT-004 | FACT | ✧ | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | A | 2025-11-07 | DT138 : confondants explicites - il est difficile d'isoler l'effet des quotas | DT138 INSPECTE : 38% des collectivites signalent des effets l'annee de mise en place et la suivante; confondants nommes : modification des tarifs professionnels, interdictions sur certaines decheteries, COVID, effet de destockage dans les mois precedant la mise en service. Citation : 'Il est difficile d'isoler l'effet des quotas d'acces dans ces cas de figure.' La baisse par flux (-20/-20,4/-35%) n'est donc PAS entierement attribuable au quota. | a1a489ad-d3f6-426c-ac1b-95947cdd6df6
FCT-005 | FACT | ✧ | https://www.pointfortenvironnement.fr/wp-content/uploads/2024/06/DEL2024-14-Rapport_annuel_2023.pdf | A | 2024-06-30 | Point Fort (Manche) : pass 18 passages/an des 01/01/2023, frequentation -28%, tonnages -29% | Point Fort Environnement (syndicat Manche, 11 decheteries en 2023, RPQS 2023 PDF INSPECTE) : pass decheterie obligatoire depuis 01/01/2023 = 18 passages/foyer/an gratuit ; frequentation 250 482 vehicules 2023 vs 349 587 en 2022 = -28% ; tonnages 36 035 t vs 50 910 t = -29% ; 340 kg/hab vs 397 kg/hab ; 'On constate une baisse des flux collectes, par habitant, notamment concernant les gravats et les encombrants'. Confondants nommes par le RPQS : retrait de 2 decheteries (St-Sauveur Villages, Periers) et fin des double comptes a Saint-Lo. Recette acces pros payants 2023 : 237 038 EUR (les pros sont encore admis payants en 2023). | 646c04b7-36e6-4f97-a2e4-637ab5a49207
FCT-006 | FACT | ✧ | https://www.pointfortenvironnement.fr/wp-content/uploads/2024/06/DEL2024-14-Rapport_annuel_2023.pdf | A | 2024-06-30 | Point Fort structure des flux 2023 : verts 46%, gravats 17%, encombrants 15% ; encombrants traites -34,7% | Point Fort RPQS 2023 INSPECTE : flux collectes en decheterie 2023 (total 36 035 t) : branchages/pelouse (verts) 16 335 t = 46%, gravats inertes 6 115 t = 17%, encombrants 5 503 t = 15%, mobilier 3 223 t (9%), ferraille 1 114 t (3%), DEEE 925 t (3%). Donnees centre de traitement Beauchene : encombrants 5 574 t en 2023 vs 8 541 t en 2022 = -34,7% l'annee du pass QR. Structure rurale (verts dominants) tres differente de la moyenne nationale (verts 27-29%). | 627a2e06-539a-4ecb-8bc8-3e52fd324a4f
FCT-007 | FACT | ✧ | https://www.loireforez.fr/wp-content/uploads/2025/07/Rapport-annuel-2024.pdf | A | 2025-07-19 | Loire Forez SANS quota : tonnages +0,6%, encombrants -13%, gravats -5%, verts +21% (climat) | Loire Forez (RPQS 2024 PDF INSPECTE, pas de controle d'acces ni quota documente) : tonnages globaux decheterie stables +0,6% (2023->2024) ; site de Sury le Comtal : encombrants -13%, gravats -5%, dechets verts +21% (climat pluvieux 2024, cite par le rapport) ; autres sites : verts +25% (Arthun), +30% (Savigneux), gravats +22% (Estivareilles), encombrants +36% sur decheterie mobile (Noiretable). Les baisses d'encombrants (-13%) et gravats (-5%) existent AUSSI sans quota. | d8bf4379-5078-4c2b-afdd-27abfbb77e29
FCT-008 | FACT | ✧ | https://troyes-champagne-metropole.fr/wp-content/uploads/2026/04/Rapport_Annuel_Collecte_TCM_2024.pdf | A | 2026-04-30 | Troyes sans quota : verts 6 045 t = premier flux decheterie 2024 (+15%), gravats 2e flux -7% | Troyes Champagne Metropole (rapport annuel collecte 2024 PDF INSPECTE, pas de quota documente) : en 2024 le flux dechets verts devient le PREMIER flux collecte en decheterie (6 045 t, +15% vs 2023) - le rapport lie la hausse aux conditions meteorologiques ('annee propice a la pousse des vegetaux') ; gravats = 2e flux en baisse de 7% vs 2023. Objectif affiche : -5 a -10% du tonnage verts via broyage/compostage/jardinage au naturel (experimentations 2023-2024). | 244a89f6-ef23-4a3e-8e61-03695e2c37f2
FCT-009 | FACT | ✧ | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | A | 2025-11-07 | DT138 : ratio decheterie 247 kg/hab, verts = principal flux | DT138 INSPECTE : le ratio de collecte en decheterie tous flux confondus (deblais et gravats compris) atteint 247 kg par habitant ; les dechets verts sont qualifies de 'principal flux de dechets collecte en decheterie' - c'est le flux le plus saisonnier et le plus volumineux, d'ou sa cible privilegiee par les limites d'apport dediees. | d35b7153-c1b8-4be4-9ed3-9f7f17416fc2
FCT-010 | FACT | ✧ | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | A | 2026-08-31 | Deux mecanismes de quota documentes : passages (tout-venant) vs volume/par flux (verts, gravats) | Croisement AMP + DT138 (INSPECTES cette session) : les quotas GENERIQUES de passages (AMP 3/jour-36/an, Point Fort 18/an, Gard 36/an, Cyclad 24/an) frappent la frequence d'apport independamment du flux - la benne tout-venant residuel (encombrants) est la plus touchee (-35% mediane DT138, -34,7% a Point Fort) car c'est le flux des petits apports frequents. Les quotas VOLUME (m3 par jour ou par visite) ou par flux (verts SYDED, gravats 500 kg/jour, DDS 75 kg, pneus) ciblent directement verts et gravats. AMP est le seul EPCI documente avec grille par flux complete. | 828193dd-fbc6-40f3-9f9d-04fc49489d1d
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-002
FCT-010 | SRC-001,SRC-002

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -
FCT-010 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T08:09:14.144378+00:00","fact_mem":{"FCT-001":"5ecfd657-8f14-4a47-aa9e-3057f7b41275","FCT-002":"3d493220-c9c3-46cc-b1bc-f7d58b455155","FCT-003":"c6302ed1-964a-4cdf-be28-c09b52ab79e6","FCT-004":"a1a489ad-d3f6-426c-ac1b-95947cdd6df6","FCT-005":"646c04b7-36e6-4f97-a2e4-637ab5a49207","FCT-006":"627a2e06-539a-4ecb-8bc8-3e52fd324a4f","FCT-007":"d8bf4379-5078-4c2b-afdd-27abfbb77e29","FCT-008":"244a89f6-ef23-4a3e-8e61-03695e2c37f2","FCT-009":"d35b7153-c1b8-4be4-9ed3-9f7f17416fc2","FCT-010":"828193dd-fbc6-40f3-9f9d-04fc49489d1d"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-010","reason":"NONE","success":1}],"writeback_row":{"attempted":10,"blocked":0,"eligible":10,"failure":0,"success":10}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:10;attempted:10;success:10;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[10 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-010 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
