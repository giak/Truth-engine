ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-0927-dechetteries-france-histoire | PARENT_RUN_ID:20260830-0904-dechetteries-france | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france-histoire/2026-08-30_09-27_dechetteries-france-histoire_INPUT.txt | SUBJECT_SLUG:dechetteries-france-histoire | SUBJECT_FP:sha256:c31e341014724072b4c79c03c04adba31b61e7ad97c949ebf74c12fcc869226b | INPUT_SHA256:sha256:c31e341014724072b4c79c03c04adba31b61e7ad97c949ebf74c12fcc869226b
COMPLEXITY:7→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['ANRED', 'ADEME', 'collectivites-EPCI', 'eco-organismes-REP', 'FEDEREC', 'Archives-Bordeaux-Metropole'], 'domains': ['dechets', 'histoire-environnement', 'reglementation', 'rep'], 'exclusions': [], 'geo': 'France', 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': ['Légifrance/Archives-Bordeaux-metropole anti-bot (discovery seule)', 'corroboration indépendante 1ere-dechetterie non trouvée'], 'object_question': 'UPDATE : d où vient l idée et comment le réseau français des déchetteries s est-il construit ? Origine du concept et du mot, situation avant (décharges/dépôts), lois clés (1975/1992/2012), généalogie ADEME/ANRED, éco-organismes REP greffés, et ancrage chiffré du maillage (SINOE) et de la première déchetterie.', 'period': '1970-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# UPDATE — Déchèteries en France : d'où vient l'idée, comment le réseau s'est construit

## RÉSUMÉ EXÉCUTIF

Cette passe **UPDATE** (INPUT_KIND=UPDATE, MISSION_MODE=INVESTIGATION, PARENT `20260830-0904-dechetteries-france`) complète l'investigation initiale (état : tonnages, financement, ICPE) par la **genèse et les acteurs** du réseau. L'OBJECT_QUESTION prioritaire : « d'où vient l'idée des déchèteries et comment le réseau français s'est-il construit ? ».

**Verdicts (tous ✧ PROBABLE, familles le plus souvent uniques) :**

1. **Institution** (FCT-001) : les déchèteries sont une **invention de l'État**. L'ANRED, ancêtre de l'ADEME, créée en 1976 (loi du 15/07/1975), « **invente les déchetteries** » et les développe ; l'ADEME naît en 1990/91 (loi du 19/12/1990) par fusion (AQA + AFME + ANRED) et fonctionne depuis le 01/01/1992 (ADEME, source SRC-001).
2. **Le mot** (FCT-002) : « Déchetterie » est un **néologisme-marque ANRED de 1987** (concept d'« apport volontaire », licence vendue aux sociétés de collecte) ; l'orthographe **« déchèterie »** à un « t » fut validée par l'**Académie française** après le panneau d'**Escolives (Yonne), 1990** ; passage de marque à nom commun = **antonomase** (SRC-002, SRC-003 ; convergence avec SRC-001).
3. **Avant** (FCT-005) : avant les déchèteries, pas de maillage de dépôt ménager : décharges et dépôts, frontière poreuse légal/illégal jusqu'aux lois de 1975 puis 2016 ; les dépôts illégaux (déchets ménagers et BTP) persistent, et les frais de déchetterie sont cités comme facteur (Géoconfluences, ENS Lyon, SRC-007).
4. **Le déclencheur** (FCT-003) : la **loi n°92-646 du 13/07/1992** (dès le 01/07/2002, seuls les déchets ultimes admis en décharge — Légifrance, découverte) contraint les collectivités à **divertir** encombrants et recyclables → **essor des déchèteries** (SRC-004).
5. **Les acteurs greffés** (FCT-007) : premiers **éco-organismes** (Éco-Emballages, Adelphe) début des années 1990, dans le cadre de la REP, pour recycler emballages/papiers (Cy-Clope, SRC-008).
6. **Le maillage, chiffré** (FCT-006) : l'annuaire **SINOE/ADEME** recense **4 630 déchèteries** dans la saisie 2026 ; par date d'ouverture (D_OUV) : 2 avant 1970, 7 (années 70), 127 (années 80), 2 058 (années 90), 2 371 (2000-09, pic), 478 (2010-19), 170 (2020-26) ; **~90 % du réseau courant ouvert entre 1990 et 2009** (dataset ADEME, SRC-009).

**Gap majeur (CLM-003, AXS-006)** : la « **première déchetterie de France** » revendiquée — **Gradignan, 17/11/1980** (exposition des Archives Bordeaux Métropole) — reste une **provenance unique**, page amont anti-bot non inspectée, sans corroboration indépendante ni date antérieure (années 70) trouvée. Origin « années 1970 » **WEAKEN** : prototype-seulement (7 sites), la vague est 1990-2009.

**Conclusion bornée** : le réseau des déchèteries est une **construction étatique et réglementaire française (~1980-2000)** — mot inventé en 1987 par l'ANRED, équipements pionniers dès 1980 (Gradignan, non confirmé indépendamment), essor piloté par la loi de 1992 et l'interdiction de mise en décharge (2002), éco-organismes REP greffés dès les années 90, maillage massif 1990-2009 (~4 630 sites répertoriés en 2026).

## CHRONOLOGIE (source : history)

- **1975** : loi n°75-633 (15/07/1975) — élimination des déchets + récupération des matériaux ; pose la prévention (SRC-001).
- **1976** : création de l'**ANRED** (décret d'application) pour accompagner la loi (SRC-001).
- **17/11/1980** : ouverture revendiquée de la « première déchetterie (de France) » à **Gradignan** (Gironde, agglomération CUB) — données de l'exposition des Archives Bordeaux Métropole (SRC-005, SRC-006 ; amont anti-bot).
- **1987** : néologisme et marque **« Déchetterie »** par l'ANRED ; concept d'apport volontaire (SRC-002, SRC-003).
- **1990** : panneau d'**Escolives** ; l'**Académie française** valide l'orthographe « déchèterie » (1 t) (SRC-002, SRC-003).
- **1990-1992** : loi du 19/12/1990 créant l'**ADEME** (fusion AQA+AFME+ANRED), active le 01/01/1992 (SRC-001).
- **13/07/1992** : loi n°92-646 — dès le 01/07/2002, seuls les déchets ultimes en décharge (Légifrance, découverte ; SRC-004). Début des **éco-organismes** Éco-Emballages et Adelphe (SRC-008).
- **1990-2009** : **vague de création** du maillage — 2 058 sites (90s) + 2 371 (2000-09) (dataset SINOE, SRC-009).
- **2007** : Grenelle de l'environnement (fonds déchets confié à l'ADEME — rapporté dans la passe antérieure).
- **2012** : décret n°2012-384 — cadre ICPE de la rubrique 2710 des déchèteries (passe antérieure, FCT état).
- **2026** : saisie SINOE ramenée à **4 630 déchèteries** répertoriées (SRC-009).

## DOMAINES

### D1. Origine de l'idée (AXS-001, SATURATED)
L'idée est **étatique** : c'est l'ANRED (ancêtre ADEME) qui invente le concept (apport volontaire) et y accole une **marque en 1987** ; l'orthographe est fixée par l'Académie française en 1990 (FCT-001, FCT-002). Pas une initiative privée spontanée.

### D2. Situation avant (AXS-005, SATURATED)
Avant ~1980 : quasi aucun site (2 avant 1970, 7 dans les années 70, 127 dans les années 80 — dataset SINOE, FCT-006). Les flux échappaient aux décharges, dépôts illicites et enlèvements (FCT-005). La déchèterie comblait un **vide de dépôt contrôlé**.

### D3. Cadre légal (AXS-003, SATURATED)
Continuité 1975 (prévention) → 1992 (déchets ultimes 2002 → détourner) → 2012 (ICPE 2710). La loi de 1992 est le **catalyseur** documenté de l'essor (FCT-003).

### D4. Acteurs greffés (AXS-002, SATURATED)
ADEME (ex-ANRED) ; collectivités/EPCI (compétence) ; **éco-organismes REP** dès les années 90 (FCT-007) puis CITEO/Valdelia/Ecosystem (montée en charge rapportée) ; inspection ICPE ; ressourceries.

### D5. Maillage chiffré (AXS-005, SATURATED)
4 630 sites répertoriés (2026) ; profil d'ouverture très concentré 1990-2009 (FCT-006).

## RÉSEAU D'ACTEURS

- ANRED → (ancêtre/absorption) → **ADEME** (1976-1992) (FCT-001).
- État/lois → (cadre) → collectivités créant les déchèteries (1975-2002) (FCT-003).
- Producteurs (REP) → (éco-contributions) → éco-organismes (Éco-Emballages, Adelphe, années 90) (FCT-007).
- Les arêtes mobilier/DEEE/CITEO et le financement TEOM relèvent de la passe antérieure (état) et ne sont pas re-vérifiés dans cette UPDATE.

## CHAÎNES / PELOTE

CAU-001 : la loi 1992 est un **ENABLER** documenté de l'essor (4 429 sites ouverts 1990-2009). Le lien reste une **GAP_TYPE=CAUSALITY** : forte corrélation temporelle, mais chaîne complète (loi → décisions locales → financement → ouverture) non vérifiée étape par étape — le réseau a aussi dépendu de fonds (ADEME/Grenelle) et des éco-organismes (décrits qualitativement). On ne réduit pas l'essor à la seule loi.

## CARTE DIALECTIQUE

- **P1 dominant** (ADEME, archives) : la déchèterie est une invention nationale, outil de progrès du tri.
- **P2 critique** (ADEME/observatoire et associations) : le « première de France » est une revendication locale non recoupée ; le financement REP déplace une partie du coût vers des structures de droit privé.
- **P3 arbitrage** : la généalogie institutionnelle, le mot et le maillage sont bien étayés ; la revendication « première de France » (Gradignan 1980) reste **SUPPORTED, famille unique**, à confirmer.

## CARTE DES PREUVES

Registres machine émis par le runtime (LEAD/CLM/AXS/CAU, registre des preuves, registre des faits, carte source→fait, réfutations, plan de write-back, journal des requêtes, rapport EDI).

- **SOURCE_AUDIT** : N/A(NO_INPUT_LEAD) — input UPDATE, pas de source soumise.
- **Tiers** : tous ✧ (famille unique). Aucun ✦ : les revendications « première de France » et le total du maillage reposent sur une provenance officielle/archives unique ; Légifrance et Archives Bordeaux Métropole sont anti-bot (ACCESS).
- **Refutation** : REFUTATION * menée sur la généalogie ANRED/ADEME, la loi 92-646, la revendication Gradignan et le total SINOE — aucune contradiction ; « première de France » sans corroboration indépendante (INDEPENDENCE).

## PÉRIMÈTRE & LIMITES

- Inclusions : histoire du concept/mot, lois clés, généalogie institutionnelle, acteurs greffés, maillage chiffré.
- Exclusions : pas de ré-établissement de l'état financier/tonnage (passe précédente) ; pas de certification indépendante de la « première de France ».
- Limites d'accès : Légifrance (403) et Archives Bordeaux Métropole (anti-bot Anubis) → découverte seule. Données SINOE = jeu primaire ADEME, famille unique.
- Le chiffre « 4 630 » = déchèteries **répertoriées** dans la saisie 2026, non un « en service aujourd'hui » certifié.

## AUDIT DU LEAD / SOURCE

N/A(NO_INPUT_LEAD). Les sources citées proviennent de la recherche objet ; toutes inspectées (fetch) sauf Légifrance et Archives Bordeaux Métropole (head-blocked, signalés).

## ÉTAT DES CONNAISSANCES

- PROBABLE (✧) : invention ANRED/ADEME ; mot 1987 + orthographe Académie 1990 ; lois 1975/1992 (déchets ultimes 2002) ; éco-organismes années 90 ; maillage 4 630 (2026) / profil 1990-2009.
- SUPPORTED, famille unique : « première déchetterie (de France) » Gradignan 17/11/1980 (à corroborer).
- GAP : corroboration indépendante de la première ; origine 1970s non datée indépendamment (WEAKEN).
- CAUSALITY GAP : essor ↔ loi 1992 = ENABLER documenté, cause unique non prouvée.
- Aucun fait refuté ; aucune contradiction matérielle non résolue.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:6|AXS:7|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Thème obtenu dérivé du sujet (histoire) : étayé par FCT-001, FCT-002, FCT-004","kind":"OBJECT","lead":"Origine du concept et du mot déchèterie (ANRED/ADEME 1975-1992 ; néologisme-marque 1987 ; première déchetterie Gradignan 1980)","linked_ids":["AXS-001","AXS-004","CLM-001","CLM-002","CLM-003"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"Thème objet dérivé du sujet : étayé par FCT-005","kind":"OBJECT","lead":"Situation avant les déchetteries : décharges et dépôts, frontière légal/illégal avant 1975 puis 1992/2002","linked_ids":["AXS-005","CLM-004"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"Thème objet dérivé du sujet : étayé par FCT-001, FCT-003, FCT-007","kind":"OBJECT","lead":"Cadre légal (lois 1975/1992/2012) et acteurs qui se greffent (ADEME, collectivités/EPCI, éco-organismes REP)","linked_ids":["AXS-002","AXS-003","CLM-001","CLM-006"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"Thème objet dérivé du sujet : étayé par FCT-006","kind":"OBJECT","lead":"Maillage chiffré du réseau au fil du temps (annuaire SINOE : 4 630 en 2026 ; chronologie d'ouverture)","linked_ids":["AXS-005","CLM-004","CLM-005"],"locator":"-","materiality":"DECISIVE","routes":["EXPAND"],"source_id":"-","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le réseau des déchetteries est une construction récente (about ≃ années 1980-2000), portée par l'État (ANRED/ADEME) puis démultipliée par la loi de 1992 (déchets ultimes 2002).","claimant":"ADEME histoire ; Symetri ; Légifrance (découverte)","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-001, FCT-003"}
CLM-002 | {"claim":"Le mot 'déchèterie' est un néologisme ANRED de 1987 (marque, concept d'apport volontaire) ; l'orthographe à un 't' a été validée par l'Académie française après le panneau d'Escolives (1990).","claimant":"CC Les Bertranges ; La Galerie du Zéro Déchet ; ADEME","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-002"}
CLM-003 | {"claim":"Une revendication (Archives Bordeaux Métropole, exposition) désigne Gradignan, 17/11/1980, comme 'première déchetterie (de France)' ; corroboration indépendante non établie, page amont anti-bot.","claimant":"Archives Bordeaux Métropole (via vieux-bordeaux.fr, go-expo.fr)","counter":"NONE_FOUND_indep","gap":"Le statut de 'première de France' reste une seule famille de provenance ; pas de source indépendante antérieure datée (années 1970) trouvée","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-004"}
CLM-004 | {"claim":"Avant ~1980, pratiquement pas de déchetteries (2 sites avant 1970, 7 dans les années 70) ; les flux échappaient aux décharges/dépôts ; ~90% du réseau actuel a été ouvert 1990-2009 (2 058 + 2 371 sites).","claimant":"Dataset SINOE/ADEME (D_OUV) ; Geoconfluences ENS Lyon ; Symetri","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-005, FCT-006"}
CLM-005 | {"claim":"Le nombre courant de déchetteries répertoriées en France est de 4 630 (annuaire SINOE/ADEME, saisie 2026), cohérent avec la fourchette 4 100-4 700.","claimant":"ADEME, dataset SINOE Annuaire","counter":"NONE_FOUND (4 100 ADEME, ~4 700 Symetri)","gap":"Chiffre dérivé du jeu primaire ADEME (famille unique A) ; non recoupé par un second institut indépendant","gap_type":"INDEPENDENCE","materiality":"DECISIVE","status":"SATURATED","support":"FCT-006"}
CLM-006 | {"claim":"Des acteurs se sont greffés autour du maillage : ADEME (ex-ANRED), collectivités/EPCI, éco-organismes REP (Éco-Emballages et Adelphe dès les années 90, puis CITEO/Valdelia/Ecosystem…), inspection ICPE et ressourceries/réemploi.","claimant":"Cy-Clope ; ADEME ; passe KERNEL précédente","counter":"NONE_FOUND","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-001, FCT-007"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-011"],"axis":"SCOPE_HISTORY","led_clm_links":["LED-001","CLM-001","CLM-002"],"question":"D où vient l idée des déchetteries (concept, mot, institution) ?","result_ids":["FCT-001","FCT-002","FCT-003"],"sought_objects":"néologisme-marque ANRED 1987, généalogie ADEME/ANRED, lois 1975-2012","status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-011"],"axis":"ACTORS_RELATIONS","led_clm_links":["LED-003","CLM-006"],"question":"Quels acteurs se sont greffés sur le maillage (ADEME, éco-organismes, collectivités) ?","result_ids":["FCT-001","FCT-007"],"sought_objects":"éco-organismes REP 90s, généalogie institutionnelle","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-015"],"axis":"RULES_CONTROLS","led_clm_links":["LED-003","CLM-001"],"question":"Quel cadre légal a cadré/accéléré les déchetteries (lois 1975, 1992, 2012) ?","result_ids":["FCT-003"],"sought_objects":"loi 92-646 déchets ultimes 2002 ; continuité 1975 et ICPE 2710 (passe précédente)","status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-006","QRY-007","QRY-008","QRY-009","QRY-013"],"axis":"EVIDENCE_CASES","led_clm_links":["LED-001","CLM-003"],"question":"Quand et où a ouvert la 'première déchetterie' de France ?","result_ids":["FCT-004"],"sought_objects":"revendication Gradignan 17/11/1980 (Archives Bx Métropole)","status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-010","QRY-012","QRY-016"],"axis":"SCOPE_HISTORY","led_clm_links":["LED-002","LED-004","CLM-004","CLM-005"],"question":"Comment le réseau s est-il construit et quelle était la situation avant ?","result_ids":["FCT-005","FCT-006"],"sought_objects":"annuaire SINOE (sites + D_OUV), histoire des décharges","status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-013"],"axis":"COUNTER_HYPOTHESES","gap":"Origine 'années 1970' non étayée par une source indépendante datée ; la revendication 'première de France' (Gradignan 1980) n a pas de corroboration indépendante ; la masse date de 1990-2009","gap_type":"INDEPENDENCE","led_clm_links":["LED-002","CLM-003","CLM-004"],"question":"L origine est-elle vraiment 'années 1970' ou la généralisation est-elle postérieure (1980s-2000) ?","result_ids":[],"sought_objects":"date de 1re déchetterie, antériorité indépendante aux années 70","status":"GAP"}
AXS-007 | {"attempt_ids":[],"axis":"SOURCE_AUDIT","gap":"N/A(NO_INPUT_LEAD) : input UPDATE sans source matérielle","gap_type":"NONE","led_clm_links":[],"question":"Audit de la source fournie (lead)","result_ids":[],"sought_objects":"sans objet (aucun lead fourni)","status":"N/A"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"la loi est un catalyseur réglementaire ; le lien causal n est pas réduit à lui seul (facteurs locaux, fonds ADEME, éco-organismes)","from":"loi n°92-646 (13/07/1992) imposant dès 01/07/2002 seuls déchets ultimes en décharge","gap":"Corrélation temporelle forte (vague 1990-2009 après 1992) mais chaîne causale complète (loi → décisions locales → financement → ouverture) non vérifiée étape par étape ; la loi est un ENABLER documenté, pas une cause unique prouvée","gap_type":"CAUSALITY","link_type":"ENABLER","mechanism":"réduction de la mise en décharge et obligations de tri poussent les collectivités à créer des déchetteries pour divertir encombrants et recyclables","source":"Symetri (T4) ; dataset SINOE chronologie D_OUV (FCT-003, FCT-006)","status":"GAP","to":"essor/massification du réseau des déchetteries (1990-2009 : 4 429 sites ouverts)"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"EMPTY","RESPONSIBILITY_MAP":"EMPTY","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND lineage: parents dechetteries-france (RUN 20260830-0904 FINAL) + memoire RENARD + facts; pas de snapshot subject-fp de l'INPUT UPDATE | MnemoLite-MCP8002 | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | histoire decheterie origine mot ANRED 1987 premiere dechetterie France (decouverte)
QRY-002 | FETCH | FOUND | SRC-001 | https://www.ademe.fr/lagence/notre-histoire/ | -
QRY-003 | FETCH | FOUND | SRC-002 | https://www.lesbertranges.fr/index.php/2020/02/18/une-histoire-pour-le-mot-decheterie/6689/ | -
QRY-004 | FETCH | FOUND | SRC-003 | https://lagalerieduzerodechet.fr/pourquoi-ecrit-on-decheterie-une-histoire-dantonomase/ | -
QRY-005 | FETCH | FOUND | SRC-004 | https://www.symetri.fr/2024/12/10/les-decheteries-en-france-un-role-essentiel-depuis-leur-creation/ | -
QRY-006 | WEB | FOUND | - | - | premiere dechetterie de France Gradignan 1980 archives bordeaux (decouverte)
QRY-007 | FETCH | FOUND | SRC-005 | https://vieux-bordeaux.fr/actualites-historiques/exposition-fabuleux-destin-dechets-menagers/ | -
QRY-008 | FETCH | FOUND | SRC-006 | https://go-expo.fr/expo/le-fabuleux-destin-des-dechets-menagers-archives-de-bordeaux-metropole | -
QRY-009 | FETCH | FAILED:anubis-head-blocked | - | https://archives.bordeaux-metropole.fr/expositions/salle-la-gestion-des-dechets-dans-la-cub-56/n:45 | -
QRY-010 | FETCH | FOUND | SRC-007 | https://geoconfluences.ens-lyon.fr/informations-scientifiques/dossiers-thematiques/geographie-critique-des-ressources/articles/decharges-isdnd-en-france | -
QRY-011 | FETCH | FOUND | SRC-008 | https://www.cy-clope.com/histoire-du-recyclage-en-france-quand-qui-et-comment/ | -
QRY-012 | FETCH | FOUND | SRC-009 | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | -
QRY-013 | WEB | NO_RESULT:no-independent-contradiction | - | - | REFUTATION premiere dechetterie de France Gradignan 1980 : source independante ou date anterieure 1970s non trouvee; seule provenance Archives Bordeaux Metropole
QRY-014 | WEB | NO_RESULT:no-contradiction | - | - | REFUTATION geneologie ANRED creation 1975/1976 nom officiel recuperation et elimination des dechets (ADEME, francearchives) confirmee
QRY-015 | WEB | NO_RESULT:no-contradiction | - | - | REFUTATION loi 92-646 13/07/1992 : a compter 01/07/2002 seuls dechets ultimes en decharge (legifrance, sittomat) confirmee; catalyseur essor dechetteries
QRY-016 | WEB | NO_RESULT:no-contradiction | - | - | REFUTATION nombre decheteries France : 4630 repertoriees saisie 2026 (SINOE ademe) coherent avec fourchette 4100-4700

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.ademe.fr/lagence/notre-histoire/
SRC-002 | ○ | fam:C | https://www.lesbertranges.fr/index.php/2020/02/18/une-histoire-pour-le-mot-decheterie/6689/
SRC-003 | ○ | fam:C | https://lagalerieduzerodechet.fr/pourquoi-ecrit-on-decheterie-une-histoire-dantonomase/
SRC-004 | ○ | fam:C | https://www.symetri.fr/2024/12/10/les-decheteries-en-france-un-role-essentiel-depuis-leur-creation/
SRC-005 | ○ | fam:C | https://vieux-bordeaux.fr/actualites-historiques/exposition-fabuleux-destin-dechets-menagers/
SRC-006 | ○ | fam:C | https://go-expo.fr/expo/le-fabuleux-destin-des-dechets-menagers-archives-de-bordeaux-metropole
SRC-007 | ◉ | fam:E | https://geoconfluences.ens-lyon.fr/informations-scientifiques/dossiers-thematiques/geographie-critique-des-ressources/articles/decharges-isdnd-en-france
SRC-008 | ○ | fam:C | https://www.cy-clope.com/histoire-du-recyclage-en-france-quand-qui-et-comment/
SRC-009 | ◈ | fam:A | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.ademe.fr/lagence/notre-histoire/ | A | 1976-1992 | dechetterie-origine-ademe-anred | ANRED creee 1976 (loi 75-633) pour eliminer/recycler; ADEME fusion 1990/91 (loi 90-1130), active 01/01/1992; ADEME declare: ANRED a invente les dechetteries | bca01348-b259-45ca-b1fe-0c1a78080a9d
FCT-002 | FACT | ✧ | https://www.lesbertranges.fr/index.php/2020/02/18/une-histoire-pour-le-mot-decheterie/6689/ | A,C | 1987-1990 | dechetterie-neologisme-marque | mot 'Dechetterie' = neologisme+marque ANRED 1987 (concept apport volontaire, licence); orthographe 'decheterie' 1-t validee par Acad. francaise (Escolives, 1990); antonomase (marque inindicate) | 379d8ecd-3b6b-45a7-a206-8131f44400c6
FCT-003 | FACT | ✧ | https://www.symetri.fr/2024/12/10/les-decheteries-en-france-un-role-essentiel-depuis-leur-creation/ | C | 1992 | loi-1992-dechets-ultimes-2002 | loi 92-646 (13/07/1992) : a compter 01/07/2002 seuls dechets ultimes admis en decharge (snippet legifrance) ; tournant accelerant les dechetteries (symetri, T4) | 379fb16a-1c3e-4428-9674-ae0dbd018d45
FCT-004 | FACT | ✧ | https://vieux-bordeaux.fr/actualites-historiques/exposition-fabuleux-destin-dechets-menagers/ | C | 1980 | decheterie-premiere-gradignan-1980 | recits d'exposition (Archives Bx Metropole, rapporte par vieux-bordeaux et go-expo) : 1ere dechetterie (de France) a Gradignan ouverte le 17/11/1980 ; page amont archives anti-bot non inspectee | 8dbe8b46-fac3-49f6-8aa3-0ee07659ef06
FCT-005 | FACT | ✧ | https://geoconfluences.ens-lyon.fr/informations-scientifiques/dossiers-thematiques/geographie-critique-des-ressources/articles/decharges-isdnd-en-france | E | 2024 | avant-dechetteries-decharges | avant 1975/2016 frontiere poreuse decharge/ill egal ; depots illegaux dechets menagers+BTP persistent ; frais de dechetterie cites comme facteur de depots sauvages (Geoconfluences ENS Lyon) | 4e8d3aaf-f826-4e6f-8d6f-961d3ea026fc
FCT-006 | FACT | ✧ | https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw | A | 2026 | decheteries-nombre-sinoe-2026 | 4630 sites repertories saisie 2026 ; chronologie D_OUV : <1970:2, 70-79:7, 80-89:127, 90-99:2058, 00-09:2371(pic), 10-19:478, 20-26:170 ; cumul 5213 ; ~90% du reseau courant ouvert 1990-2009 | fa8a2dc3-71fe-4cce-a107-2c207b3e8af3
FCT-007 | FACT | ✧ | https://www.cy-clope.com/histoire-du-recyclage-en-france-quand-qui-et-comment/ | C | 1990 | rep-ecoorganismes-90s | premiers eco-organismes (Eco-Emballages, Adelphe) apparaissent debut annees 1990 dans le cadre de la REP pour recycler emballages/papiers (Cy-Clope) | a963f179-afbf-4ebb-a13c-b70eb6bd0e7c
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002,SRC-003,SRC-001
FCT-003 | SRC-004
FCT-004 | SRC-005,SRC-006
FCT-005 | SRC-007
FCT-006 | SRC-009
FCT-007 | SRC-008

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-014 | NONE
FCT-003 | QRY-015 | NONE
FCT-004 | QRY-013 | NONE
FCT-006 | QRY-016 | NONE

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH:AXS-001 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T07:32:24.100514+00:00","fact_mem":{"FCT-001":"bca01348-b259-45ca-b1fe-0c1a78080a9d","FCT-002":"379d8ecd-3b6b-45a7-a206-8131f44400c6","FCT-003":"379fb16a-1c3e-4428-9674-ae0dbd018d45","FCT-004":"8dbe8b46-fac3-49f6-8aa3-0ee07659ef06","FCT-005":"4e8d3aaf-f826-4e6f-8d6f-961d3ea026fc","FCT-006":"fa8a2dc3-71fe-4cce-a107-2c207b3e8af3","FCT-007":"a963f179-afbf-4ebb-a13c-b70eb6bd0e7c"},"mnemo_row":"33b23208-4e38-425a-9fdc-199bb5798ed8","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:33b23208-4e38-425a-9fdc-199bb5798ed8 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
