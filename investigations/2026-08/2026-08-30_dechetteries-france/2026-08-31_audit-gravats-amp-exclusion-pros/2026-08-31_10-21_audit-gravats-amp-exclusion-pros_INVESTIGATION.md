ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-1021-audit-gravats-amp-exclusion-pros | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-gravats-amp-exclusion-pros/2026-08-31_10-21_audit-gravats-amp-exclusion-pros_INPUT.txt | SUBJECT_SLUG:audit-gravats-amp-exclusion-pros | SUBJECT_FP:sha256:6531a2ddedb9bded286eeb4083859ff923227b6c8bdaeebee36590badac3e032 | INPUT_SHA256:sha256:350ca066a6d1c041336828785db2f3e6ef74717686565a280caac9f12833b8f1
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['AMP', 'professionnels', 'communes (Bouc-Bel-Air)', 'Matild', 'OCAB'], 'domains': ['dechets', 'decheterie', 'gravats', 'exclusion-pros', 'quotas'], 'geo': 'Aix-Marseille-Provence', 'lead_question': "Quel est l'effet de l'exclusion des professionnels (01/07/2025) sur le flux gravats des decheteries AMP ?", 'limits': 'tonnage gravats 2025 non publie ; exclusion et quota simultanes', 'object_question': '(1) avant 2024 ; (2) apres 2025 ; (3) signaux qualitatifs'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Tonnages gravats AMP 2024 vs 2025 : l'effet de l'exclusion des professionnels

**Run `20260831-1021-audit-gravats-amp-exclusion-pros`** — recherche des tonnages gravats Aix-Marseille-Provence avant/après l'exclusion des professionnels (01/07/2025), pour mesurer l'effet sur le flux gravats, en isolant le confondant du quota simultané (3 m³ gravats/jour).

## Ce que l'audit établit

### 1. Le chiffre gravats 2024→2025 n'est PAS publié (GAP, FCT-007)

Le tonnage gravats spécifique des déchèteries AMP 2024 vs 2025 n'est pas accessible : le rapport annuel métropolitain 2025 (post-exclusion) n'est pas encore paru au 31/08/2026, et le rapport 2024 ne détaille pas les gravats par déchèterie (Annexe 10 non exploitable en texte brut). La mesure quantitative de l'effet reste donc **impossible aujourd'hui**.

### 2. La baisse précède l'exclusion (FCT-001)

Entre 2023 et 2024, **AVANT** l'exclusion (01/07/2025) et le quota : **OMR +0,10 %, collectes sélectives +4,5 %, DÉCHÈTERIES -2,9 %**, total DMA -0,7 %. Les tonnages déchèterie (et donc, en partie, les gravats) baissent déjà sans exclusion. Confondant supplémentaire à la passe 1002/1012.

### 3. Le confondant irréductible : exclusion pros + quota gravats simultanés (FCT-005)

Au 01/07/2025, l'AMP combine deux mesures frappant le MÊME flux gravats/verts : l'exclusion des professionnels (gravats, DIB, verts de chantiers) ET le quota ménager de 3 m³ gravats/jour + 3 m³ verts/jour. Isoler l'effet « exclusion » de celui du « quota » dans une évolution 2024→2025 est structurellement impossible pour ce flux.

### 4. Les signaux qualitatifs post-exclusion (FCT-003, FCT-004)

- **Bouc-Bel-Air (mairie officielle, 01/08/2025)** : depuis le 01/07/2025, pros (paysagistes/jardiniers) exclus ; la commune déclare que la restriction « risque d'amplifier » le phénomène des dépôts sauvages, renforce les rondes et caméras mobiles dans les collines, et a évacué « plusieurs tonnes » dans la zone des Chabauds (près de l'usine Lafarge). La seule déchèterie pro de la commune (Matild) est « déjà sous-dimensionnée » et objet de plaintes riveraines (déchets sur la voie publique, bruit, trafic).
- **ici.fr / Radio France (10/06/2025)** : un entrepreneur en travaux d'extérieurs (Mallemort) produit 1 à 2 t de déchets verts/jour, pas prévenu, prédit dépôts sauvages et risque d'incendie (résineux), contraint d'aller à Gardanne (~1h) car les déchèteries privées le refusent. Il affirme que des entreprises contourneront (dépôt en déchèteries publiques ou sauvage).
- **Rapport MIE (Sophie Camard, 2024)** : « L'accès des déchèteries aux professionnels est interdit quelque soit le gabarit », et les gravats/inertes ne sont « pas considérés comme encombrants » — le service déchèterie exclut structurellement les flux pros de gravats.

### 5. Le faisceau pour le flux gravats

L'exclusion des pros frappe en théorie le premier flux que les pros apportaient : **gravats/DIB** (bâtiment) et **verts** (paysagistes). Le réseau d'alternative (Mat'ild, OCAB) est documenté comme sous-dimensionné (« sous-dimensionnée » Bouc-Bel-Air ; le pros de Mallemort vit Gardanne). Le signal dépôts sauvages (Bouc-Bel-Air) et le risque incendie associé (ici.fr) relient l'exclusion au §7 de la fresque.

## L'articulation avec la fresque

L'AMP est le cas test de l'exclusion des pros de 2025 : la mesure vise les flux que le bac ne prend pas (gravats exclusifs en déchèterie, 81 % hors bac — passe 0942). Privés de l'exutoire public, les pros se reportent sur des réseaux privés sous-dimensionnés ou sur l'abandon sauvage — chaîne déjà documentée par la passe 2135 (dépôts sauvages 900 €/t). Le chiffre gravats manquant reste le maillon quantitatif.

## GAPs restants

- Tonnages gravats AMP 2024 vs 2025 (RP 2025 à venir).
- Effet propre de l'exclusion (confondu avec le quota simultané).
- Tonnages des déchèteries pro (Mat'ild, OCAB) après exclusion (report de flux).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:3|AXS:2|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"Bouc-Bel-Air risque amplification depots sauvages; pros Mallemort 1-2 t verts/jour; Matild sous-dimensionnee","note":"le chiffre gravats 2025 manque; confondant quota simultane","routes":["RP 2025 AMP","presse pros","Matild OCAB","depots sauvages"],"status":"SATURATED","title":"Exclusion pros AMP 01/07/2025 -> report du flux gravats/DIB : chiffrer sur 2024 vs 2025"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le tonnage gravats AMP 2024 vs 2025 n'est pas publie (RP 2025 non paru) : la mesure quantitative de l'effet de l'exclusion est impossible a ce jour","counter":"Le RP 2024 donne -2,9% decheteries (avant exclusion) : la derive naturelle existe","gap":"tonnage gravats par decheterie non detaille; RP 2025 absent","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-007","FCT-001"]}
CLM-002 | {"claim":"L'exclusion pros et le quota gravats (3 m3/jour) simultanes au 01/07/2025 frappent le meme flux gravats/verts : isoler l'effet de l'exclusion de celui du quota sur 2024->2025 est structurellement impossible","counter":"On pourrait comparer par decheterie ou par type d'apport, mais la donnee n'existe pas","gap":"aucune decomposition par cause","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-005"]}
CLM-003 | {"claim":"Le flux gravats/verts exclu se reporte sur des exutoires sous-dimensionnes ou l'abandon : Bouc-Bel-Air constate le risque d'amplification des depots sauvages et nettoie 'plusieurs tonnes'; Matild est 'sous-dimensionnee'; le pros de Mallemort predit contournement et risque d'incendie","counter":"Signaux qualitatifs locaux, pas de serie nationale; intention declaree ne vaut pas comportement mesuré","gap":"pas de tonnage des depots sauvages attribuable a l'exclusion AMP","gap_type":"UNVERIFIED_QUANTITY","status":"SUPPORTED","support":["FCT-003","FCT-004"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Quel est l'effet de l'exclusion des professionnels (01/07/2025) sur les tonnages gravats des decheteries AMP ?","routes":["AUDIT","EXPAND"],"sought_objects":["gravats 2024 vs 2025","exclusion pros","quota 3 m3","depots sauvages"],"status":"SATURATED"}
AXS-002 | {"question":"Y a-t-il une alternative fonctionnelle (décheteries pros, OCAB, Matild) absorbant le flux gravats/dechets verts exclus ?","routes":["EXPAND"],"sought_objects":["Matild sous-dimensionnee","OCAB","décheterie pro","contournement"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Exclusion des professionnels des decheteries publiques AMP (01/07/2025)","effect":"frustration du flux gravats/DIB/verts des pros; report vers decheteries privees sous-dimensionnees ou depots sauvages","mechanism":"les pros apportaient surtout gravats (inertes) et dechets verts de chantiers; sans exutoire public, contournement ou abandon; Bouc-Bel-Air (risque amplification) et ici.fr (contournement/incendie) documentent la chaine","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-005"]}
CAU-002 | {"cause":"Conjoncture, meteo, exclusion (pas tous attribuables)","effect":"-2,9% decheteries AMP en 2024 (avant exclusion)","mechanism":"la derive naturelle des tonnages precede l'exclusion : confondant","status":"SUPPORTED","support":["FCT-001"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | runtime | warm-route-1ca3694a-dt138-1002 | MNEMO_Q
SYS-002 | SYS | FOUND | runtime | 1ca3694a-79e2-4728-8c45-e23b4f5e4411 | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | AMP metropole rapport annuel dechets 2025 decheteries tonnages gravats
QRY-002 | WEB | OK | - | - | AMP RPQS 2024 decheteries gravats encombrants vegetaux tonnages
QRY-003 | WEB | OK | - | - | AMP decheteries 2025 exclusion professionnels effet tonnages gravats bilan
QRY-004 | FETCH | PARTIAL | SRC-001 | https://ampmetropole.fr/missions/environnement/dechets-et-collecte/ | AMP dechets 59 decheteries
QRY-005 | FETCH | INSPECTED | SRC-002 | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf | rapport annuel metropolitain AMP 2024 decheteries -2,9% tonnages hors gravats 616255
QRY-006 | FETCH | INSPECTED | SRC-003 | http://www.sophiecamard.fr/wp-content/uploads/2024/11/Rapport-MIE-Collecte-Dechets-MAMP-2024.pdf | rapport MIE collecte dechets AMP 2024 inertes gravats pros interdits
QRY-007 | FETCH | INSPECTED | SRC-004 | https://www.boucbelair.fr/actualites/depots-sauvages-nouvelles-regles-pour-la-dechetterie-la-municipalite-se-mobilise/ | Bouc-Bel-Air dechets sauves restriction access risque amplifier surveillance Matild
QRY-008 | FETCH | INSPECTED | SRC-005 | https://www.ici.fr/infos/environnement/ca-va-contre-le-bon-sens-pour-les-professionnels-interdiction-au-1er-juillet-d-aller-dans-les-dechetteries-2387857 | ici France pros exclus decheteries AMP 1-2 t verts/jour depots sauvages incendie
QRY-009 | FETCH | INSPECTED | SRC-006 | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | AMP reglement 3m3 gravats 3m3 verts 4 pneus 75kg DDS exclusion pros

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://ampmetropole.fr/missions/environnement/dechets-et-collecte/
SRC-002 | ◈ | fam:A | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf
SRC-003 | ◈ | fam:A | http://www.sophiecamard.fr/wp-content/uploads/2024/11/Rapport-MIE-Collecte-Dechets-MAMP-2024.pdf
SRC-004 | ◈ | fam:B | https://www.boucbelair.fr/actualites/depots-sauvages-nouvelles-regles-pour-la-dechetterie-la-municipalite-se-mobilise/
SRC-005 | ◈ | fam:B | https://www.ici.fr/infos/environnement/ca-va-contre-le-bon-sens-pour-les-professionnels-interdiction-au-1er-juillet-d-aller-dans-les-dechetteries-2387857
SRC-006 | ◈ | fam:A | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf | A | 2025-12-18 | AMP RP 2024 : decheteries -2,9% entre 2023 et 2024 (AVANT exclusion pros 01/07/2025) | Rapport annuel metropolitain AMP dechets 2024 (PDF INSPECTE) : entre 2023 et 2024, OMR +0,10%, collectes selectives +4,5%, DECHETERIES -2,9%; total DMA collectes -0,7%. Tonnages hors gravats (total DMA) = 616 255 t (2024). La baisse des tonnages decheterie PRECEDE l'exclusion des professionnels (01/07/2025) et le quota gravats (3 m3/jour) - un autre confondant qui confirme que les decheteries baissent aussi sans exclusion. | 2d610275-96e5-4515-b6fc-0411e203be55
FCT-002 | FACT | ✧ | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf | A | 2025-12-18 | AMP : 59 decheteries + 3 eco-mobiles = 62 sites, 25 zones de reemploi (42%) | Rapport annuel metropolitain AMP 2024 INSPECTE : 62 sites (59 decheteries et 3 eco-mobiles) sur le territoire ; 25 decheteries equipees d'une zone de reemploi (42% du parc) ; Annexe 10 = 'Decheteries - Tonnages 2024' par site (non exploitable en texte brut, colonnes disjointes). Le tonnage gravats par decheterie n'est pas detaille publiquement dans ce rapport. | 365e3df2-5f86-4b32-b38d-0d0d17c73601
FCT-003 | FACT | ✧ | https://www.boucbelair.fr/actualites/depots-sauvages-nouvelles-regles-pour-la-dechetterie-la-municipalite-se-mobilise/ | B | 2025-08-01 | Bouc-Bel-Air (BdR) : restriction decheteries = risque d'amplifier les depots sauvages, la seule decheterie pro (Matild) sous-dimensionnee | Mairie de Bouc-Bel-Air (page officielle INSPECTEE, 01/08/2025) : depuis le 01/07/2025 les professionnels (paysagistes, jardiniers) n'ont plus le droit de deposer leurs dechets dans les decheteries AMP ; la mairie declare que la restriction 'risque d'amplifier' le phenomene des depots sauvages et renforce la surveillance (rondes week-end, cameras mobiles dans les collines) ; zone des Chabauds (pres usine Lafarge) regulierement ciblee : 'plusieurs tonnes de dechets' evacuees par la commune ; la seule decheterie professionnelle (Matild) est 'deja sous-dimensionnee' et objet de plaintes (dechets sur voie publique, bruit, trafic). | 719fffa4-f9f8-4434-8b4b-21716f8386bd
FCT-004 | FACT | ✧ | https://www.ici.fr/infos/environnement/ca-va-contre-le-bon-sens-pour-les-professionnels-interdiction-au-1er-juillet-d-aller-dans-les-dechetteries-2387857 | B | 2025-06-10 | ici.fr (Radio France) : chantier pros exclu (Mallemort) produit 1-2 t dechets verts/jour, predit depots sauvages et incendies | ici.fr / Radio France (10/06/2025, INSPECTE) : Patrice Theobald, Provence Environnement (Mallemort, BdR), travaux d'exterieurs, produit 'entre une et deux tonnes par jour' de dechets verts en haute saison ; exclu des decheteries AMP au 01/07/2025 ; affirme n'avoir pas ete prevenu et predit 'des depots d'ordures, de dechets sauvages' et risques d'incendie (feuilles de resineux inflammables) ; les decheteries privees le refusent (a ete a Gardanne, ~1h) ; il affirme que des entreprises vont contourner (depot en decheteries publiques ou sauvage). Corroboration : la mairie de Bouc-Bel-Air (SRC-004) confirme le lien restriction -> risque d'augmentation des depots sauvages. Tiers: deux familles B (presse + commune). | e3242fb2-494b-4dad-92a1-764e8d9806c0
FCT-005 | FACT | ✧ | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | A | 2025-07-01 | AMP : exclusion pros et quota gravats/verts simultanes au 01/07/2025 - confondant irreductible | Reglement AMP decheteries (page officielle INSPECTEE, passe 42 et cette session) : au 01/07/2025, (1) les professionnels ne peuvent plus acceder aux decheteries - cible directe des flux gravats, DIB, dechets verts de chantiers ; (2) quota menage simultane 3 m3 dechets verts/jour, 3 m3 gravats/jour, 4 pneus, 75 kg DDS. Quand on mesure l'evolution 2024->2025 des gravats, les deux mesures (exclusion pros + quota menages) frappent le MEME flux gravats/verts la meme annee : il est impossible de separer l'effet de l'exclusion pros de celui du quota. | 79df0b73-8aef-4220-b968-e608ee422c08
FCT-006 | FACT | ✧ | http://www.sophiecamard.fr/wp-content/uploads/2024/11/Rapport-MIE-Collecte-Dechets-MAMP-2024.pdf | A | 2024-11-30 | Rapport MIE AMP (Sophie Camard) : acces des decheteries aux professionnels interdit 'quelque soit le gabarit', gravats = non encombrants | Rapport MIE sur la collecte dechets AMP 2024 (PDF INSPECTE, Sophie Camard) : 'L'acces des decheteries aux professionnels est interdit quelque soit le gabarit de leur vehicule' ; definition : les dechets inertes (gravats, briques, beton, tuiles) 'ne sont pas consideres comme encombrants' et relevent d'une filiere a part ; il confirme que le service decheterie est concu pour les menages et exclut structurellement les flux professionnels de gravats. | 4bf35725-8d2b-4232-9b11-d59a0f374278
FCT-007 | FACT | ✧ | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf | A,B | 2026-08-31 | GAP : tonnages gravats AMP 2024 vs 2025 non publies ; seuls -2,9% pre-exclusion et signaux qualitatifs post-exclusion documentent l'effet | Croisement sources INSPECTEES : le tonnage gravats SPECIFIQUE des decheteries AMP 2024 vs 2025 n'est PAS publie (le rapport annuel 2025, post-exclusion, n'est pas encore paru au 31/08/2026 ; le RP 2024 ne detaille pas les gravats par decheterie - Annexe 10 non exploitable). Ce qui documente l'effet : (1) -2,9% decheteries en 2024 pre-exclusion [SRC-002] ; (2) Bouc-Bel-Air constate le risque d'amplification des depots sauvages et nettoie 'plusieurs tonnes' [SRC-004] ; (3) ici.fr : pros prevoient contournement/depots sauvages sur les verts et inertes [SRC-005]. Le chiffre gravats 2024->2025 reste un GAP de donnee. | d1d72926-40e6-451b-b715-634a5801b1a6
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002
FCT-002 | SRC-002
FCT-003 | SRC-004
FCT-004 | SRC-005,SRC-004
FCT-005 | SRC-006
FCT-006 | SRC-003
FCT-007 | SRC-002,SRC-004,SRC-005

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T08:26:07.643211+00:00","fact_mem":{"FCT-001":"2d610275-96e5-4515-b6fc-0411e203be55","FCT-002":"365e3df2-5f86-4b32-b38d-0d0d17c73601","FCT-003":"719fffa4-f9f8-4434-8b4b-21716f8386bd","FCT-004":"e3242fb2-494b-4dad-92a1-764e8d9806c0","FCT-005":"79df0b73-8aef-4220-b968-e608ee422c08","FCT-006":"4bf35725-8d2b-4232-9b11-d59a0f374278","FCT-007":"d1d72926-40e6-451b-b715-634a5801b1a6"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
