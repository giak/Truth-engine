ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2156-audit-incendies-securite-decheteries | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:INVESTIGATION | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-incendies-securite-decheteries/2026-08-30_21-56_audit-incendies-securite-decheteries_INPUT.txt | SUBJECT_SLUG:audit-incendies-securite-decheteries | SUBJECT_FP:sha256:cc50f810b84da000b8f30e09c44cfc4ecc808358a5e21ed13f64df50f0964be7 | INPUT_SHA256:sha256:cc50f810b84da000b8f30e09c44cfc4ecc808358a5e21ed13f64df50f0964be7
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:historique incendies decheteries 2020-2026 ; renforcement ICPE incendie 2023/2025 ; cout assurance reparation ; responsabilite exploitants collectivites ; batteries lithium DEEE
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Audit incendies & sécurité des déchèteries (2020-2026)

**Run `20260830-2156-audit-incendies-securite-decheteries`** — axe lièvre 1 demandé par l'utilisateur pour compléter la fresque transdisciplinaire (trou §12 SÉCURITÉ & RISQUE).

## Ce que l'audit établit

### 1. L'accidentologie explose — et la déchèterie est au cœur du flux à risque
La proposition de loi Sénat 24-079 (exposé des motifs, 24/10/2024) documente **plus de 1 400 incendies entre 2010 et 2019 sur les centres de collecte, de tri et de recyclage** ; le BARPI recense **autant d'accidents en 3 ans (2016-2019) que sur les 15 années précédentes**. Son inventaire 2023 : **41 événements liés aux batteries au lithium (presque le double de 2022), dont 60 % dans les filières déchets**. L'étude RECORD 2024 (119 p., SETEC) recense **66 accidents liés aux piles/accumulateurs lithium dans la base ARIA entre octobre 2017 et octobre 2023**, et estime que **~30 % des départs de feu (hors causes indéterminées) sont dus aux P&A lithium**. [FCT-001 ✦]

### 2. La cause dominante est documentée : batteries lithium + bouteilles de gaz
FEDEREC (F. Excoffier, président, 2025) : les centres de tri sont passés de **140-150 à plus de 400 incendies par an** ; **batteries lithium + bouteilles de gaz = 60 % des sinistres** ; **+150 % d'incendies liés aux batteries en 10 ans** (G. Bulot). Cas concrets 2024-2026 documentés : **Toulouse Decoset 07/2026** (emballement thermique 800 °C, benne de déchèterie), **Serqueux 22/06/2026** (emballement thermique dans un container recyclage), **Taulé-Morlaix fermée depuis le 14/09/2024** (incendie aire de déchets verts), Sens Vauguillettes 07/2026, Mercin 08/2026, Wattrelos camion-benne 19/06/2026. [FCT-005 ✦]

### 3. Le renforcement réglementaire arrive en 3 vagues (2023-2025) — y compris pour les déchèteries en déclaration
- **Arrêté du 22/12/2023** (JO 29/12/2023, NOR TREP2330762A) : prescriptions incendie pour les ICPE à autorisation 2710/2712/2718/2790/2791 — détection automatique, rondes, zones, petits îlots (≤ 500 m²), définitions des batteries (SLI, puissance, MTL, industrielle).
- **Arrêté du 8/01/2024** : installations à **déclaration** (2710-1/2710-2 = la majorité des déchèteries) — **plan de défense incendie dès le 01/07/2024**, exercice d'incendie renouvelé au moins tous les 3 ans ; **DEEE susceptibles de contenir des batteries lithium séparés dès le 01/01/2025** (disposition spéciale 670 ADR) ; comptabilité des stocks dès le 01/01/2025 ; dès le **01/01/2026** : petits îlots limités, **batteries en conteneurs/locaux fermés étanches avec rétention R60**, procédure d'identification des batteries mal triées, détection automatique + rondes.
- **Arrêté du 5/05/2025** (JO 31/05/2025) : clarifications (installations nouvelles = dépôt de dossier après le 01/01/2026). [FCT-002 ✦]

### 4. Le coût du sinistre est lourd — et le fonds proposé fait porter la moitié aux producteurs
Le Sénat (PPL 24-079) : les dégâts d'incendie dans les centres de tri/recyclage peuvent atteindre **1,3 M€ par installation** (EuRIC), voire plusieurs dizaines de millions selon la gravité ; protoxyde d'azote : **150 000 € en moyenne d'arrêt pour une UVE** (AMORCE), jusqu'à **500 000 € par explosion** dans les fours. **L'article 2 de la PPL crée un fonds financé par les producteurs (DEEE + piles/batteries) prenant en charge la MOITIÉ des frais d'incendie causés par les batteries mal collectées** — application du principe pollueur-payeur. [FCT-003 ✦]

### 5. Le GAP probatoire : pas de série nationale dédiée aux déchèteries
La donnée BARPI agrège collecte/tri/recyclage ; **RECORD documente que les départs de feu maîtrisés en interne ne remontent pas au BARPI** (sous-estimation structurelle) ; le **taux de collecte des P&A est de 43,5 % en 2021, sous le minimum réglementaire de 45 %** — les batteries mal collectées restent dans le flux. Les cas de déchèteries individuelles sont documentés par la presse locale/Facebook officiels seulement. [FCT-004 ✦]

## Le lien avec le dossier
La déchèterie est le **premier maillon de réception des batteries mal triées** : l'usager y dépose DEEE et P&A, l'emballement thermique y déclenche des incendies. Le renforcement ICPE 2024-2026 impose aux exploitants des coûts de mise en conformité (détection, conteneurs R60, rondes) — **un coût nouveau pour les collectivités**, à rapprocher de la refondation PMCB 2027 (les matériaux « matures » sortent de la reprise) et du contrôle d'accès (axe F). Le PPL 24-079 engage la question « qui paie » : collectivités (exploitant), assureurs, ou producteurs via un fonds REP.

## Gaps ouverts
- **GAP-001 (DATA)** : aucune série nationale officielle dédiée aux incendies de déchèteries ; la donnée BARPI agrège collecte/tri/recyclage et sous-estime (départs maîtrisés en interne non remontés). → test discriminant : le rapport IGEDD « réduction de l'accidentologie » et l'extraction ARIA ciblée rubrique 2710.

## Vérification & réfutation
- 5 FETCH directs INSPECTED (Sénat PPL 24-079, AIDA arrêté 22/12/2023, CNPP arrêté 8/01/2024, RECORD 2024, Les Numériques 29/07/2026).
- 5 réfutations adversariales posées (FOUND_RESOLVED / NONE) : les chiffres FEDEREC (400+) sont des estimations de fédération, mais les 41 événements BARPI et les 66 accidents ARIA (RECORD) corroborent la tendance par deux familles indépendantes ; aucune source ne contredit les dates d'arrêtés (Legifrance/AIDA).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:3|AXS:3|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"desc":"incendies de decheteries 2020-2026 : sinistres documentes par presse/SDIS, couts, causes (batteries lithium, DEEE), suites reglementaires","label":"ledger-incendies","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"desc":"CLAIM: les incendies de decheteries sont frequents et recurrents en France (H a tester, pas de serie nationale officielle)","label":"clm-incendies-recurrents","status":"SUPPORTED"}
CLM-002 | {"desc":"CLAIM: les batteries lithium et DEEE sont la cause dominante des incendies de decheteries (H a tester)","label":"clm-batteries-causes","status":"SUPPORTED"}
CLM-003 | {"desc":"CLAIM: le renforcement ICPE incendie 2023/2025 est une reponse a une vague de sinistres (H a tester)","label":"clm-icpe-reponse","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"desc":"AXIS: catalogue incendies de decheteries 2020-2026 par presse/SDIS - test: nombre, lieu, cause, cout","label":"historique-sinistres","status":"SATURATED"}
AXS-002 | {"desc":"AXIS: renforcement ICPE 2710 incendie 2023/2025 - test: quelles prescriptions nouvelles, origine (sinistres?), impact exploitants","label":"reglementation-icpe","status":"SATURATED"}
AXS-003 | {"desc":"AXIS: qui paie l incendie - test: assurance, collectivite, exploitant, TGAP ; cout moyen par sinistre","label":"cout-assurantiel","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"desc":"GAP: aucune serie nationale officielle dediee aux incendies de decheteries (BARPI agrege collecte/tri/recyclage) ; departs de feu maitrises en interne non remontes (sous-estimation structurelle)","gap":"pas de serie dediee incendies decheteries vs centres de tri ; sous-declaration structurelle des departs maitrises en interne (RECORD)","gap_type":"DATA","label":"cau-gap-serie-decheteries","status":"GAP"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:6|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route ICPE 2710 decret 2012-384 + arretes 27/03/2012 + renforcement incendie 2023/2025 (98be4887, VERIFIE passe 0904) | runtime | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | incendie decheterie France 2024 2025 bilan SDIS cause batterie lithium DEEE benne feu
QRY-002 | WEB | FOUND | - | - | arrete ministeriel ICPE 2710 decheterie incendie 2023 2025 renforcement prescriptions nouvelles
QRY-003 | WEB | FOUND | - | - | decheterie incendie cout degats euros reparation batterie emballement 2025 2026 sinistre benne chiffre
QRY-004 | FETCH | FOUND | SRC-001 | https://www.senat.fr/leg/exposes-des-motifs/ppl24-079-expose.html | -
QRY-005 | FETCH | FOUND | SRC-002 | https://aida.ineris.fr/reglementation/arrete-221223-relatif-a-prevention-risque-dincendie-sein-installations-soumises-a | -
QRY-006 | FETCH | FOUND | SRC-003 | https://www.faceaurisque.com/2024/02/07/installations-de-gestion-des-dechets-l-arrete-du-8-janvier-2024-modifie-plusieurs-arretes-ministeriels/ | -
QRY-007 | FETCH | FOUND | SRC-004 | https://record-net.org/travaux-de-recherche/261-dangerosite-des-batteries-lithium-dans-les-dechets-menagers-et-assimiles.htm | -
QRY-008 | FETCH | FOUND | SRC-005 | https://www.lesnumeriques.com/societe-numerique/il-jette-une-batterie-au-lithium-dans-une-benne-la-dechetterie-prend-feu-pres-de-toulouse-n259852.html | -
QRY-009 | EXA | - | - | - | REFUTATION 1 400 2010 2019 24 079 3 2016 15 2023 41 2022 60 : refutation accidentologie - nombre d incendies centres dechets inferieur ou serie differente ?
QRY-010 | EXA | - | - | - | REFUTATION renforcement reglementaire incendie arrete decheteries 01 1 2 3 05 5 07 8 12 22 29 31 670 2023 2024 2025 2026 2710 2712 2718 2790 2791
QRY-011 | EXA | - | - | - | REFUTATION 1 3 150 000 500 000 24 079 : refutation cout sinistre - montant degats inferieur ou couvert par assurance ?
QRY-012 | EXA | - | - | - | REFUTATION 43 5 2021 45 : refutation gap - taux collecte piles superieur ou serie decheteries existante ?
QRY-013 | EXA | - | - | - | REFUTATION 60 2025 150 10 140 400 07 2026 22 06 14 09 2024 19 : refutation cause dominante - cause autre que batteries ou nombre inferieur ?
QRY-014 | FETCH | FOUND | SRC-006 | https://www.facebook.com/RFfrancebleunord/posts/camion-poubelle-totalement-detruit-deux-voitures-en-feu-des-habitations-endommag/1656278466498568/ | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.senat.fr/leg/exposes-des-motifs/ppl24-079-expose.html
SRC-002 | ◈ | fam:A | https://aida.ineris.fr/reglementation/arrete-221223-relatif-a-prevention-risque-dincendie-sein-installations-soumises-a
SRC-003 | ◈ | fam:B | https://www.faceaurisque.com/2024/02/07/installations-de-gestion-des-dechets-l-arrete-du-8-janvier-2024-modifie-plusieurs-arretes-ministeriels/
SRC-004 | ◈ | fam:E | https://record-net.org/travaux-de-recherche/261-dangerosite-des-batteries-lithium-dans-les-dechets-menagers-et-assimiles.htm
SRC-005 | ◈ | fam:A | https://www.lesnumeriques.com/societe-numerique/il-jette-une-batterie-au-lithium-dans-une-benne-la-dechetterie-prend-feu-pres-de-toulouse-n259852.html
SRC-006 | ◈ | fam:C | https://www.facebook.com/RFfrancebleunord/posts/camion-poubelle-totalement-detruit-deux-voitures-en-feu-des-habitations-endommag/1656278466498568/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.senat.fr/leg/exposes-des-motifs/ppl24-079-expose.html | A,E | 2026-08-30 | ACCIDENTOLOGIE NATIONALE : 1 400+ incendies comptabilises 2010-2019 sur les centres de collecte, tri et recyclage (Senat PPL 24-079) ; BARPI recense autant d'accidents en 3 ans (2016-2019) que sur les 15 annees precedentes ; inventaire 2023 : 41 evenements batteries lithium (presque le double de 2022), 60% dans les filieres dechets | Senat PPL 24-079 expose des motifs INSPECTED : 'Plus de 1 400 incendies ont ete comptabilises entre 2010 et 2019 sur les centres de collecte, de tri et de recyclage. Le BARPI recense autant d'accidents en l'espace de trois ans (2016-2019) que sur les quinze annees precedentes' ; 'inventaire 2023... 41 au total, presque le double de ceux recenses en 2022. 60% des evenements lies aux batteries concernent les filieres dechets' ; RECORD 2024 : 66 accidents P&A Li recenses ARIA oct 2017-oct 2023, ~30% des departs de feu hors indetermines | ad240533-be39-40d8-b831-d89cef367426
FCT-002 | FACT | ✦ | https://www.faceaurisque.com/2024/02/07/installations-de-gestion-des-dechets-l-arrete-du-8-janvier-2024-modifie-plusieurs-arretes-ministeriels/ | A,B | 2026-08-30 | RENFORCEMENT REGLEMENTAIRE EN 3 VAGUES : arrete 22/12/2023 (autorisation 2710/2712/2718/2790/2791, JO 29/12/2023) + arrete 8/01/2024 (declaration 2710-1/2710-2 = la majorite des decheteries) + arrete 5/05/2025 (JO 31/05/2025) : plan defense incendie + exercice 3 ans des 01/07/2024 ; DEEE lithium separes des 01/01/2025 (ADR 670) ; comptabilite stocks 01/01/2025 ; petits ilots, batteries en conteneurs R60, detection auto + rondes des 01/01/2026 | AIDA INERIS INSPECTED (arrete 22/12/2023 NOR TREP2330762A, JO 29/12/2023) : champ 2710/2712/2718/2790/2791, detection automatique, rondes, zones, petits ilots (500 m2 max), definitions batteries (SLI/puissance/MTL/industrielle) ; CNPP/faceaurisque INSPECTED (arrete 8/01/2024) : installations declaration 2710-1/2710-2, plan defense incendie + exercice tous les 3 ans des 01/07/2024, DEEE contenant batteries lithium separes des 01/01/2025 (disposition 670 ADR), comptabilite des stocks 01/01/2025, petits ilots + batteries conteneurs/locaux fermes etanches retention R60 + detection auto + rondes 01/01/2026 | 0ba1a7fa-a8d8-4daa-95f0-7c800a1f3c04
FCT-003 | FACT | ✦ | https://www.senat.fr/leg/exposes-des-motifs/ppl24-079-expose.html | A,E | 2026-08-30 | COUT DU SINISTRE : jusqu'a 1,3 ME par installation pour les degats d'incendie centres de tri/recyclage (EuRIC), plusieurs dizaines de ME selon gravite ; protoxyde d'azote : arret UVE 150 000 EUR en moyenne (AMORCE), explosion jusqu'a 500 000 EUR ; PPL 24-079 : creation d'un fonds finance par les producteurs (DEEE + piles/batteries) prenant en charge la MOITIE des frais d'incendie causes par batteries mal collectees | Senat PPL 24-079 INSPECTED : 'les couts des degats causes par les incendies dans les centres de tri et de recyclage peuvent s'elever jusqu'a 1,3 million d'euros par installation, voire plusieurs dizaines de millions d'euros selon la gravite' ; protoxyde : 'arret des installations - pour un cout de 150 000 euros en moyenne pour une UVE (source AMORCE) ; explosion dans les fours des UVE... jusqu'a 500 000 euros par explosion' ; article 2 : fonds 'prendre en charge la moitie des frais engendres par les incendies causes par l'inflammation des batteries mal collectees' | a255f30f-69b5-4a6a-b537-cc437f71af55
FCT-004 | FACT | ✦ | https://record-net.org/travaux-de-recherche/261-dangerosite-des-batteries-lithium-dans-les-dechets-menagers-et-assimiles.htm | E,C | 2026-08-30 | GAP PROBATOIRE : aucune serie nationale officielle dediee aux decheteries (la donnee BARPI agrege collecte/tri/recyclage) ; RECORD : les departs de feu maitrises en interne ne remontent pas au BARPI (sous-estimation structurelle) ; taux de collecte P&A 43,5% en 2021 < 45% minimum reglementaire - les batteries mal collectees restent dans le flux ; cas decheteries documentes par la presse locale seulement | RECORD 2024 INSPECTED : 'Le nombre d'incendies repertories n'est pas representatif du nombre de departs de feu lies aux P&A lithium... de nombreux departs de feu sont maitrises en interne par l'exploitant et ne sont pas remontes au BARPI' ; 'En 2021, le taux de collecte etait de 43,5%, soit en-dessous du taux minimum de collecte de 45%' ; gap : pas de serie dediee decheteries vs centres de tri ; cas locaux (Taulé, Serqueux, Sens) documentes par presse/FB officiels seulement | 40727e3a-c98e-49b8-a2a7-e19b57918f04
FCT-005 | FACT | ✦ | https://www.lesnumeriques.com/societe-numerique/il-jette-une-batterie-au-lithium-dans-une-benne-la-dechetterie-prend-feu-pres-de-toulouse-n259852.html | A,C | 2026-08-30 | CAUSE DOMINANTE DOCUMENTEE : batteries lithium + bouteilles de gaz = 60% des sinistres des centres de tri (FEDEREC, president Excoffier 2025) ; +150% d'incendies lies aux batteries lithium en 10 ans ; 140-150 -> 400+ incendies/an centres de tri ; cas concrets : Toulouse Decoset 07/2026, Serqueux 22/06/2026, Taulé (Morlaix) fermee 14/09/2024, Sens Vauguillettes 07/2026, Wattrelos camion-benne 19/06/2026 | Les Numeriques 29/07/2026 INSPECTED : FEDEREC 'les centres de tri francais sont passes de 140 a 150 incendies par an a plus de 400' ; 'Les batteries au lithium et les bouteilles de gaz representeraient 60% de ces sinistres' ; 'En dix ans, les incendies lies aux batteries au lithium ont bondi de 150%' (Bulot) ; cas Decoset Toulouse (emballement thermique 800 degres) ; Serqueux 22/06/2026 emballement thermique container recyclage ; Taulé fermee depuis 14/09/2024 (incendie aire dechets verts) | 74bdbddb-5112-4b66-99a6-4cb4536e3e89
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-004
FCT-002 | SRC-002,SRC-003
FCT-003 | SRC-001,SRC-004
FCT-004 | SRC-004,SRC-006
FCT-005 | SRC-005,SRC-006

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-009 | FOUND_RESOLVED
FCT-002 | QRY-010 | FOUND_RESOLVED
FCT-003 | QRY-011 | FOUND_RESOLVED
FCT-004 | QRY-012 | FOUND_RESOLVED
FCT-005 | QRY-013 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7:AXS-001:QRY-001
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:11:AXS-001:QRY-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:AXS-001:QRY-001
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:AXS-001:QRY-001
CP-006 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:CLM-001:QRY-001
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:CAU-001:QRY-001
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b:GATES

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T20:04:14.751314+00:00","fact_mem":{"FCT-001":"ad240533-be39-40d8-b831-d89cef367426","FCT-002":"0ba1a7fa-a8d8-4daa-95f0-7c800a1f3c04","FCT-003":"a255f30f-69b5-4a6a-b537-cc437f71af55","FCT-004":"40727e3a-c98e-49b8-a2a7-e19b57918f04","FCT-005":"74bdbddb-5112-4b66-99a6-4cb4536e3e89"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
