ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-0957-dechetteries-france-chaine | PARENT_RUN_ID:20260830-0927-dechetteries-france-histoire | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_dechetteries-france-chaine/2026-08-30_09-57_dechetteries-france-chaine_INPUT.txt | SUBJECT_SLUG:dechetteries-france-chaine | SUBJECT_FP:sha256:32a5a1c994f9fde479f540888f00a186cbcf1e90dc2deeb03071ce7e9504ee28 | INPUT_SHA256:sha256:0a92b969623bef4efcecc415cdc0a1ed52643c9c28238aec7bdb81a583c6d83b
COMPLEXITY:7→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'domains': ['histoire des dechets', 'reglementation', 'maillage territorial', 'acteurs institutionnels', 'archives'], 'geo': 'France', 'period': '1880-2026', 'question': 'Quelle est la genese et la construction du reseau des dechetteries en France?'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Passe KERNEL UPDATE certifiée — La chaîne consolidée des déchetteries en France

RUN_ID : 20260830-0957-dechetteries-france-chaine · PARENT_RUN_ID : 20260830-0927-dechetteries-france-histoire
AS_OF : 2026-08-30 · INPUT_KIND : UPDATE (revalidation différentielle) · MISSION_MODE : INVESTIGATION

## 1. La chaîne consolidée

La genèse du réseau des déchetteries en France se décompose en trois maillons vérifiés, chacun ancré dans une famille de preuve distincte :

1. **Gradignan, 17/11/1980 — le dépôt fixe pionnier** (FCT-001). La source amont — le service d'archives de Bordeaux Métropole, panneau de l'exposition « La gestion des déchets dans la Cub » — déclare textuellement : « ouverture de la première déchetterie en France à Gradignan le 17 novembre 1980 ». Cette page a été **inspectée** via le snapshot Wayback du 24/05/2024 (site live bloqué par anti-bot Anubis). Nature : document officiel du dépositaire (tier T2). La revue professionnelle TSM (juillet 1985) présente « l'expérience de la Communauté Urbaine de Bordeaux, celle d'une déchetterie » comme référence nationale (SRC-005) : corroboration indirecte de famille (AGHTM ≠ Archives BM).

2. **1987 — le néologisme-marque ANRED** (FCT-002, FCT-006). Le mot « déchetterie » est un néologisme + marque déposée par l'ANRED en 1987 (concept d'apport volontaire, licence) ; l'orthographe à un seul « t » a été validée par l'Académie française (panneau d'Escolives, 1990). L'ANRED (créée 1976, loi 75-633) puis l'ADEME (fusion 1990/91, active 01/01/1992) déclarent avoir inventé les déchetteries : l'invention est **étatique**, antérieure à la diffusion massive du réseau.

3. **1990-2009 — la massification** (FCT-004). L'annuaire SINOE/ADEME (saisie 2026, dataset primaire téléchargé et analysé) recense **4 630 sites**, dont 2 058 ouverts dans les années 1990 et 2 371 dans les années 2000 (pic) : ~90 % du réseau courant a été construit entre 1990 et 2009, après la loi n° 92-646 (13/07/1992) imposant dès le 01/07/2002 l'admission des seuls déchets ultimes en décharge (CAU-001, enabler documenté).

## 2. Ce qui change par rapport au parent

- **FCT-001 passe de revendication relayée à T2 INSPECTED** : la source amont (Archives BM) a été inspectée textuellement ; corroboration indirecte TSM 1985 ajoutée (famille B).
- **Acte primaire localisé** (FCT-003) : la délibération CUB de 1980 se trouve dans le fonds **BXM 511 W** « Délibérations de la communauté urbaine de Bordeaux (1967-2003) », notice « Délibérations de 1980 » (view:8586), registres numérisés **PDF avec OCR** (1 028 registres, 373 275 pages, recherche plein-texte) ; tables index BXM 27 W (1967-1999). Statut : **LOCALIZED, pas encore INSPECTED** (Anubis bloque la lecture automatique ; l'actualité officielle du 15/04/2025 confirme la mise en ligne).
- **Preuve textuelle « comment c'était avant »** (FCT-005) : TSM janvier 1971 (article J. Rougier sur Grenoble) — « le ramassage des déchets encombrants est assuré par deux bennes à ordures traditionnelles qui opèrent chaque jour dans un quartier différent ». En 1971, la collecte était **mobile et tournante**, sans lieu fixe de dépôt : le modèle déchèterie n'existait pas.
- **Les 9 sites SINOE avec D_OUV < 1980 sont neutralisés** (FCT-007) : 2 « Déchèteries Mobiles » du Jura (21/10/1974) correspondent à la création du syndicat SICTOM du Haut-Jura (les fixes datent des années 1990, déclaration officielle du gestionnaire) ; 6 dates rondes au 01/01 sont des valeurs par défaut d'enquête ; 1 date aberrante (Toulouse 1884). Le champ D_OUV est déclaratif depuis 2005 (enquêtes bisannuelles) — non fiable au jour près.

## 3. Test adversaire et limites

- **Test d'antériorité** (réfutation FCT-001) : sur ~300 documents OCR Gallica contenant « dechetterie », aucun daté entre 1937 et 1985 ; les seuls 1885/1937 sont des faux positifs OCR ; le même corpus contient des centaines d'occurrences « encombrants » en 1971-1979 — l'absence du mot n'est pas un artefact de couverture.
- **Limites explicites** : corroboration indépendante datée 1980-85 impossible dans les corpus libres (RetroNews et Sud Ouest payants) → GAP INDEPENDENCE (LED-003) ; acte primaire non lu → GAP ACCESS (LED-001).
- **Verdict** : la chaîne Gradignan 1980 → néologisme 1987 → réseau 1990-2009 est **MAINTAIN** (renforcée), avec deux gaps typés explicites. Rien dans SINOE, Gallica ou les sources locales ne la conteste.

## 4. État du dossier

- 7 faits revalidés (4 ✦, 3 ✧), 10 sources, 3 réfutations exécutées (toutes NONE), 4 LED (2 SATURATED, 2 GAP typés), 7 axes, 6 claims, 1 CAU (GAP CAUSALITY).
- Sections : TEMPORAL_STATE, SCOPING_REPORT, CREDO, COGNITIVE_MAP, DIALECTICAL_MAP, RESOURCE_FLOW_MAP, ACTOR_NETWORK_MAP, IMPACT_MAP, CONTRADICTION_LEDGER, VERIFICATION_REPORT, EDI_REPORT, RESPONSIBILITY_MAP, NEXT_QUERIES, MANIPULATION_REPORT.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:6|AXS:7|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"FCT-003 (acte localisé), FCT-001 (revendication T2 INSPECTED)","gap":"Acte localisé avec précision (fonds BXM 511 W, notice 8586, registres PDF OCR en ligne) mais registre 1980 non lu : Anubis bloque tout le domaine, notice absente du wayback ; lecture requiert accès interactif ou salle de lecture","gap_type":"ACCESS","kind":"LED","lead":"Acte d'ouverture de la déchèterie de Gradignan (délibération CUB 1980)","linked_ids":["AXS-004","CLM-003"],"locator":"fonds BXM 511 W, notice « Délibérations de 1980 » view:8586","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"GAP"}
LED-002 | {"evidence_excerpt":"Aucun document presse/archives nommé « déchetterie » avant 1980 dans les corpus libres (faux positifs OCR 1885/1937 écartés) ; les 9 sites SINOE D_OUV<1980 sont des dates déclaratives (2 mobiles Jura 1974 = création du syndicat, 6 rondes, 1 aberrante) ; le modèle pré-1980 est la collecte mobile (TSM 1971)","gap_type":"-","kind":"LED","lead":"Origine « années 1970 » de la déchèterie (antériorité à Gradignan 1980)","linked_ids":["AXS-005","AXS-006","CLM-004"],"locator":"corpus Gallica OCR + SINOE D_OUV","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"FCT-001 (T2 INSPECTED), SRC-005 (TSM 1985-07, corroboration indirecte)","gap":"Source unique officielle (Archives BM, T2 INSPECTED via Wayback) ; corroboration indirecte par la revue professionnelle TSM 1985 (la déchèterie CUB = référence nationale) mais pas de seconde source datée 1980-85 indépendante : RetroNews et Sud Ouest archives sont payants, non indexables librement","gap_type":"INDEPENDENCE","kind":"LED","lead":"Corroboration indépendante de la revendication « première déchèterie de France » (Gradignan 17/11/1980)","linked_ids":["AXS-006","CLM-003"],"locator":"presse 1980-1985 (Gallica OCR) + revue TSM","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"GAP"}
LED-004 | {"evidence_excerpt":"FCT-004 (4630 sites, chronologie D_OUV 1990-2009 = 2058+2371), FCT-007 (9 sites pré-1980 = déclaratif), SRC-010 (Symetri ~4700, cohérent)","gap_type":"-","kind":"LED","lead":"Construction chiffrée du réseau (SINOE 2026 : 4630 sites, ~90% ouverts 1990-2009)","linked_ids":["AXS-005","CLM-004","CLM-005"],"locator":"annuaire SINOE/ADEME, chronologie D_OUV","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le réseau des déchetteries est une construction récente (aboutissement ≈ 1980-2000), portée par l'État (ANRED/ADEME) puis démultipliée par la loi de 1992 (déchets ultimes 2002).","claimant":"ADEME histoire ; Symetri ; Légifrance (découverte passe précédente)","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-004, FCT-006"}
CLM-002 | {"claim":"Le mot « déchèterie » est un néologisme ANRED de 1987 (marque, concept d'apport volontaire) ; l'orthographe à un « t » a été validée par l'Académie française après le panneau d'Escolives (1990).","claimant":"CC Les Bertranges ; ADEME","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-002, FCT-006"}
CLM-003 | {"claim":"La revendication « première déchetterie de France à Gradignan, ouverte le 17/11/1980 » est une affirmation officielle des Archives de Bordeaux Métropole (T2 INSPECTED via Wayback), corroborée indirectement par la revue TSM 1985 ; l'acte primaire (délibération CUB 1980) est localisé (BXM 511 W) mais non lu.","claimant":"Archives Bordeaux Métropole (panneau d'exposition, INSPECTED) ; TSM 1985","counter":"NONE_FOUND_indep","gap":"Corroboration indépendante datée (presse 1980-85) non établie : source unique officielle ; acte primaire non inspecté (Anubis)","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-001, FCT-003"}
CLM-004 | {"claim":"Avant ~1980, pratiquement pas de déchetteries (2 sites avant 1970, 7 dans les années 70, tous déclaratifs) ; les flux échappaient aux décharges/dépôts et à la collecte mobile au porte-à-porte (bennes tournantes, TSM 1971) ; ~90% du réseau actuel a été ouvert 1990-2009 (2 058 + 2 371 sites).","claimant":"Dataset SINOE/ADEME (D_OUV) ; TSM 1971 ; SICTOM Haut-Jura","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-004, FCT-005, FCT-007"}
CLM-005 | {"claim":"Le nombre courant de déchetteries répertoriées en France est de 4 630 (annuaire SINOE/ADEME, saisie 2026), cohérent avec la fourchette 4 100-4 700.","claimant":"ADEME, dataset SINOE Annuaire","counter":"NONE_FOUND (4 100 ADEME, ~4 700 Symetri)","gap":"Chiffre dérivé du jeu primaire ADEME (famille A) + Symetri (famille C) ; non recoupé par un second institut indépendant","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-004"}
CLM-006 | {"claim":"Des acteurs se sont greffés autour du maillage : ADEME (ex-ANRED), collectivités/EPCI et syndicats (ex. SICTOM du Haut-Jura), éco-organismes REP (Éco-Emballages, Adelphe dès les années 90, puis CITEO/Valdelia/Ecosystem), inspection ICPE et ressourceries/réemploi.","claimant":"ADEME ; SICTOM Haut-Jura ; Cy-Clope (passe précédente)","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-006, FCT-007"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-004","QRY-007","QRY-008","QRY-010"],"axis":"SCOPE_HISTORY","led_clm_links":["LED-001","LED-002","CLM-001","CLM-002"],"question":"D'où vient l'idée des déchetteries (concept, mot, institution) ?","result_ids":["FCT-002","FCT-005","FCT-006"],"sought_objects":"néologisme-marque ANRED 1987, généalogie ADEME/ANRED, TSM 1971 collecte mobile","status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-007"],"axis":"ACTORS_RELATIONS","led_clm_links":["LED-004","CLM-006"],"question":"Quels acteurs se sont greffés sur le maillage (ADEME, éco-organismes, collectivités, syndicats) ?","result_ids":["FCT-006","FCT-007"],"sought_objects":"SICTOM Haut-Jura, généalogie institutionnelle ANRED/ADEME, éco-organismes","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-010"],"axis":"RULES_CONTROLS","led_clm_links":["LED-004","CLM-001"],"question":"Quel cadre légal a cadré/accéléré les déchetteries (lois 1975, 1992, 2012) ?","result_ids":["FCT-004"],"sought_objects":"loi 92-646 déchets ultimes 2002 ; continuité 1975 et ICPE 2710","status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-005","QRY-009","QRY-011"],"axis":"EVIDENCE_CASES","led_clm_links":["LED-001","LED-003","CLM-003"],"question":"Quand et où a ouvert la « première déchetterie » de France ?","result_ids":["FCT-001","FCT-003"],"sought_objects":"revendication Gradignan 17/11/1980 (Archives Bx Métropole, INSPECTED) ; acte primaire délibération CUB 1980 (BXM 511 W)","status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-003","QRY-004","QRY-012"],"axis":"SCOPE_HISTORY","led_clm_links":["LED-002","LED-004","CLM-004","CLM-005"],"question":"Comment le réseau s'est-il construit et quelle était la situation avant ?","result_ids":["FCT-004","FCT-005","FCT-007"],"sought_objects":"annuaire SINOE (sites + D_OUV), TSM 1971 collecte mobile, 9 sites pré-1980","status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-011","QRY-012"],"axis":"COUNTER_HYPOTHESES","gap":"Aucun document nommé « déchetterie » avant 1980 dans les corpus libres (faux positifs OCR 1885/1937) ; revendication « première de France » non corroborée par une source indépendante datée ; acte primaire non lu","gap_type":"INDEPENDENCE","led_clm_links":["LED-002","LED-003","CLM-003","CLM-004"],"question":"L'origine est-elle vraiment « années 1970 » ou la généralisation est-elle postérieure (1980s-2000) ?","result_ids":[],"sought_objects":"date de 1re déchetterie, antériorité indépendante aux années 70, acte primaire","status":"GAP"}
AXS-007 | {"attempt_ids":[],"axis":"SOURCE_AUDIT","gap":"N/A(NO_INPUT_LEAD) : input UPDATE sans source matérielle","gap_type":"NONE","led_clm_links":[],"question":"Audit de la source fournie (lead)","result_ids":[],"sought_objects":"sans objet (aucun lead fourni)","status":"N/A"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"la loi est un catalyseur réglementaire ; le lien causal n'est pas réduit à lui seul (facteurs locaux, fonds ADEME, éco-organismes)","from":"loi n°92-646 (13/07/1992) imposant dès 01/07/2002 seuls déchets ultimes en décharge","gap":"Corrélation temporelle forte (vague 1990-2009 après 1992) mais chaîne causale complète (loi → décisions locales → financement → ouverture) non vérifiée étape par étape ; la loi est un ENABLER documenté, pas une cause unique prouvée","gap_type":"CAUSALITY","link_type":"ENABLER","mechanism":"réduction de la mise en décharge et obligations de tri poussent les collectivités à créer des déchetteries pour divertir encombrants et recyclables","source":"Symetri (T4) ; dataset SINOE chronologie D_OUV (FCT-004)","status":"GAP","to":"essor/massification du réseau des déchetteries (1990-2009 : 4 429 sites ouverts selon SINOE)"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:3|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | OK | mnemolite | memories:9081540d,6ac49063,3308ce33,379d8ecd,29ed45bc,8dbe8b46,bca01348 | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://archives.bordeaux-metropole.fr/expositions/salle-la-gestion-des-dechets-dans-la-cub-56/n:45 | FETCH archives bordeaux metropole salle gestion dechets cub panneau
QRY-002 | FETCH | FOUND | SRC-002 | https://www.sictomhautjura.fr/sictom/historique/ | FETCH sictom haut jura historique page
QRY-003 | FETCH | FOUND | SRC-003 | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | FETCH sinoe annuaire decheteries raw dataset
QRY-004 | FETCH | FOUND | SRC-004 | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k9612214w&query=encombrants | FETCH gallica tsm 1971 encombrants bennes
QRY-005 | FETCH | FOUND | SRC-005 | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k96114163&query=dechetterie | FETCH gallica tsm 1985 dechetterie
QRY-006 | FETCH | FOUND | SRC-006 | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k9608096n&query=dechetterie | FETCH gallica tsm 1985 dechetteries centres accueil
QRY-007 | FETCH | FOUND | SRC-007 | https://www.ademe.fr/lagence/notre-histoire/ | FETCH ademe notre histoire anred dechetteries inventees
QRY-008 | FETCH | FOUND | SRC-008 | https://www.lesbertranges.fr/index.php/2020/02/18/une-histoire-pour-le-mot-decheterie/6689/ | FETCH les bertranges origine mot decheterie anred 1987
QRY-009 | FETCH | FOUND | SRC-009 | https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411 | FETCH archives bordeaux metropole fonds BXM 511 W deliberations cub 1967 2003
QRY-010 | FETCH | FOUND | SRC-010 | https://www.symetri.fr/2024/12/10/les-decheteries-en-france-un-role-essentiel-depuis-leur-creation/ | FETCH symetri les decheteries en france creation 1970s essor 1990s loi 92 646
QRY-011 | WEB | FOUND | - | - | REFUTATION: test antériorité — recherche presse/archives libres : aucun document nommé dechetterie avant 1980 (seuls faux positifs OCR 1885 et 1937), rien ne conteste la 1ere dechetterie de France à Gradignan ouverte le 17 11 1980
QRY-012 | WEB | FOUND | - | - | REFUTATION: test acte primaire — délibération CUB de 1980 non lue en ligne (Anubis) : acte d'ouverture de la dechetterie localisé dans le fonds BXM 511 W mais contenu du registre 1980 non inspecté, statut LOCALIZED et non INSPECTED
QRY-013 | WEB | FOUND | - | - | REFUTATION: test du décompte — annuaire SINOE saisie 2026 : 4630 sites répertoriés ; aucun recensement indépendant contradictoire trouvé, fourchette 4100-4700 (ADEME, Symetri) cohérente avec 4630

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://archives.bordeaux-metropole.fr/expositions/salle-la-gestion-des-dechets-dans-la-cub-56/n:45
SRC-002 | ◈ | fam:B | https://www.sictomhautjura.fr/sictom/historique/
SRC-003 | ◈ | fam:A | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw
SRC-004 | ◈ | fam:B | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k9612214w&query=encombrants
SRC-005 | ◈ | fam:B | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k96114163&query=dechetterie
SRC-006 | ◈ | fam:B | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k9608096n&query=dechetterie
SRC-007 | ◈ | fam:A | https://www.ademe.fr/lagence/notre-histoire/
SRC-008 | ◈ | fam:C | https://www.lesbertranges.fr/index.php/2020/02/18/une-histoire-pour-le-mot-decheterie/6689/
SRC-009 | ◈ | fam:A | https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411
SRC-010 | ◈ | fam:C | https://www.symetri.fr/2024/12/10/les-decheteries-en-france-un-role-essentiel-depuis-leur-creation/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://archives.bordeaux-metropole.fr/expositions/salle-la-gestion-des-dechets-dans-la-cub-56/n:45 | A,B | 1980-11-17 | 1ere-dechetterie-france-gradignan-17-11-1980 | Source amont INSPECTEE (Archives BM, snapshot Wayback 2024-05-24) : « ouverture de la première dechetterie en France à Gradignan le 17 novembre 1980 » ; revendication T2 officielle du dépositaire, corroborée indirectement par la revue TSM 1985-07 (colloqué ASPRODET : l'expérience de la CUB, celle d'une déchetterie, référence nationale) | 8dbe8b46-fac3-49f6-8aa3-0ee07659ef06
FCT-002 | FACT | ✧ | https://www.lesbertranges.fr/index.php/2020/02/18/une-histoire-pour-le-mot-decheterie/6689/ | A,C | 1987 | dechetterie-neologisme-marque-anred-1987 | Mot « dechetterie » = néologisme + marque ANRED 1987 (concept d'apport volontaire, licence) ; orthographe 1-t validée par l'Académie française (Escolives, 1990) ; antonomase | 379d8ecd-3b6b-45a7-a206-8131f44400c6
FCT-003 | FACT | ✧ | https://archives.bordeaux-metropole.fr/archive/fonds/FR-ABM243300316_BXM_0511_W/n:411 | A | 1980 | acte-ouverture-dechetterie-1980-localise | Acte primaire localisé : fonds BXM 511 W « Délibérations de la CUB (1967-2003) », notice « Délibérations de 1980 » (view:8586), registres numérisés PDF avec OCR (recherche plein-texte) ; tables index BXM 27 W (1967-1999) ; délibération d'ouverture de la déchèterie de Gradignan non encore lue (Anubis sur tout le domaine) | 29ed45bc-0e9a-4ece-b772-f4e7055df594
FCT-004 | FACT | ✦ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | A,C | 2026 | decheteries-nombre-sinoe-2026-4630 | Annuaire SINOE/ADEME (saisie 2026) : 4630 sites répertoriés, cumul 5213 ; chronologie D_OUV : <1970:2, 70-79:7, 80-89:127, 90-99:2058, 00-09:2371 (pic), 10-19:478, 20-26:170 ; ~90% du réseau courant ouvert 1990-2009 | fa8a2dc3-71fe-4cce-a107-2c207b3e8af3
FCT-005 | FACT | ✧ | https://gallica.bnf.fr/services/ContentSearch?ark=bpt6k9612214w&query=encombrants | B | 1971 | encombrants-1971-collecte-mobile-bennes | Preuve textuelle « comment c'était avant » : TSM janvier 1971 (article J. Rougier, Grenoble) — « le ramassage des déchets encombrants est assuré par deux bennes à ordures traditionnelles qui opèrent chaque jour dans un quartier différent » : collecte mobile tournante au porte-à-porte, aucun lieu fixe de dépôt type déchèterie | 6ac49063-c3b3-4a81-be10-e81805b596c3
FCT-006 | FACT | ✧ | https://www.ademe.fr/lagence/notre-histoire/ | A | 1976-1992 | dechetterie-invention-etatique-anred-ademe | Invention étatique : ANRED créée 1976 (loi 75-633) pour éliminer/recycler ; ADEME fusion 1990/91 (loi 90-1130), active 01/01/1992 ; ADEME déclare : ANRED a inventé les déchetteries ; le néologisme-marque « Dechetterie » (1987) est antérieur à la diffusion du réseau | bca01348-b259-45ca-b1fe-0c1a78080a9d
FCT-007 | FACT | ✧ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | A,B | 1884-1977 | decheteries-9-sites-avant-1980-realite | Les 9 sites SINOE avec D_OUV < 1980 : 2 « Déchèteries Mobiles » du Jura (21/10/1974) = équipements mobiles datés de la création du syndicat SICTOM Haut-Jura (fixes = années 1990, déclaration officielle du gestionnaire) ; 6 dates rondes au 01/01 (Longwy 1960, St-Aquilin 1973, La Haie-Fouassière 1974, Ivry 1975, Arles 1977, Gradignan 1981) = valeurs par défaut d'enquête ; 1 aberrante (Toulouse 1884) ; D_OUV déclaratif non fiable au jour près | 4d1ea161-6bb8-4070-90c8-7e39bb8dc46e
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-005
FCT-002 | SRC-008,SRC-007
FCT-003 | SRC-009
FCT-004 | SRC-003,SRC-010
FCT-005 | SRC-004
FCT-006 | SRC-007
FCT-007 | SRC-003,SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-011 | NONE
FCT-003 | QRY-012 | NONE
FCT-004 | QRY-013 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | 8dbe8b46-fac3-49f6-8aa3-0ee07659ef06
FCT-002 | UPDATE | 379d8ecd-3b6b-45a7-a206-8131f44400c6
FCT-003 | UPDATE | 29ed45bc-0e9a-4ece-b772-f4e7055df594
FCT-004 | UPDATE | fa8a2dc3-71fe-4cce-a107-2c207b3e8af3
FCT-005 | UPDATE | 6ac49063-c3b3-4a81-be10-e81805b596c3
FCT-006 | UPDATE | bca01348-b259-45ca-b1fe-0c1a78080a9d
FCT-007 | UPDATE | 4d1ea161-6bb8-4070-90c8-7e39bb8dc46e

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18
CP-008 | CORRECTION | PASS | LAST_COMPLETED:18b | NEXT_ACTION:NONE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T08:21:39.141613+00:00","fact_mem":{"FCT-001":"8dbe8b46-fac3-49f6-8aa3-0ee07659ef06","FCT-002":"379d8ecd-3b6b-45a7-a206-8131f44400c6","FCT-003":"29ed45bc-0e9a-4ece-b772-f4e7055df594","FCT-004":"fa8a2dc3-71fe-4cce-a107-2c207b3e8af3","FCT-005":"6ac49063-c3b3-4a81-be10-e81805b596c3","FCT-006":"bca01348-b259-45ca-b1fe-0c1a78080a9d","FCT-007":"4d1ea161-6bb8-4070-90c8-7e39bb8dc46e"},"mnemo_row":"98c854f2-ad0a-4a86-94f1-8b2368df4320","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:98c854f2-ad0a-4a86-94f1-8b2368df4320 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
