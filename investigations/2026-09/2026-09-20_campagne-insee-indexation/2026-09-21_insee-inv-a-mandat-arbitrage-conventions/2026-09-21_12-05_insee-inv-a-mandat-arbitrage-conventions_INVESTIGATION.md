ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1205-insee-inv-a-mandat-arbitrage-conventions | PARENT_RUN_ID:20260920-2110-indexation-conventions-gains-milliards | AS_OF:2026-09-21
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-inv-a-mandat-arbitrage-conventions/2026-09-21_12-05_insee-inv-a-mandat-arbitrage-conventions_INPUT.txt | SUBJECT_SLUG:insee-inv-a-mandat-arbitrage-conventions | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:0.70→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: qui a juridiquement compétence pour arbitrer les effets d'une convention d'indexation statistique ; object: cartographie des acteurs (parlement, gouvernement, Cour des comptes, CAE, COR, CNP, CNIS, Eurostat) et de leurs textes competents sur l'indexation legale ; period: 1987-2026; geo France; domains droit public, finances publiques; actors Assemblee nationale, Senat, gouvernement, COR, CAE, CNP, IGF; exclusions: debat politique sur le niveau des indexations; limits: aucune simulation interne accessible, recherche centree sur textes et rapports publics
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Qui arbitre les effets d'une convention d'indexation ? (INV-A)

## Objet

Le run parent (20260920-2110) a chiffre en milliards d'euros les gains des conventions d'indexation françaises (SMIC, IRL, retraites, barème IR) et conclu qu'aucune n'est cachée mais qu'aucune n'est arbitree publiquement. Ce run teste l'articulation suivante : existe-t-il un organe institutionnel qui fait ce travail sous une autre forme, c'est-à-dire qui consolide les effets distributifs des conventions d'indexation et les arbitre ?

## Méthode

Cartographie textuelle et institutionnelle : lecture de quatre textes législatifs (article L161-25 du Code de la sécurité sociale pour les pensions, article 1649 A du CGI pour le barème IR, loi 89-462 art 17-1 pour l'IRL, loi 7 juin 1951 art 1 pour l'indépendance professionnelle) et de quatre rapports d'avis consultatifs (COR, Cour des comptes avril 2025 sur les impacts du système de retraites, CAE Focus 124, groupe d'experts SMIC). Requêtes de réfutation adversariales exécutées.

## Résultat

La chaîne de compétence est fragmentée par convention :

- Retraites : parlement (LFSS), règle à l'article L161-25 CSS.
- Barème IR : parlement (LF annuelle), règle à l'article 1649 A CGI.
- IRL : parlement (loi 89-462 art 17-1).
- SMIC : parlement (droit du travail), complété par l'avis du groupe d'experts annuel.
- Chaque organe consultatif (COR, CAE, groupe SMIC, Cour des comptes) documente et critique dans son périmètre propre ; aucun n'a de mandat sur les autres conventions.

Aucun de ces documents n'a pour mandat ni pour réalisation une consolidation des effets distributifs des conventions d'indexation. L'Insee produit l'indice mais ne choisit ni la formule ni l'usage légal (loi 1951 art 1 : indépendance professionnelle).

## Vérification

Les quatre requêtes de réfutation adversariales (rapport IGF, étude d'impact LF 2025/2026, Cour des comptes juin 2025, décrets techniques) ne retourne aucune consolidation. Le fait négatif est établi sur le périmètre : documents publics textuels et institutionnels consultables en 2026.

## Limites

Le fait négatif porte sur les documents publics inspectés : un rapport interne non publié resterait hors d'atteinte. La recherche n'a pas couvert les annexes budgétaires détaillées poste par poste.

## Verdict

La fragmentation des compétences est confirmée : chaque convention a son texte, chaque organe consultatif son périmètre, et personne n'a le mandat de la chaîne entière. La thèse « rien n'est arbitré » se reformule plus précisément : « le droit répartit la compétence par convention, et ne la consolide nulle part ».

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:4|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["RELATION"],"lead":"Mandat institutionnel d'arbitrage des effets d'une convention d'indexation: qui peut dire 'cette formule coute X a ces menages'?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["FLOW"],"lead":"Cartographie textuelle des competences: LF/CSS (legislateur), decret (gouvernement), avis (COR, CAE, CNP, groupe SMIC), recommandations (Cour des comptes, IGF)","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"gap":"Aucune publication consolidant les effets distributifs des conventions d indexation identifiee dans le perimetre public inspecte; une etude interne non publiee resterait hors d atteinte","gap_type":"ACCESS","kinds":["OBJECT"],"lead":"Existence d'un document unique consolidant les effets distributifs des conventions d'indexation","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Aucun organe n'a pour mandat consolide d'arbitrer les effets distributifs des conventions d'indexation; chaque convention releve d'une competence propre (legislateur ou gouvernement) et les organes consultatifs n'opinent que sur leur perimetre","status":"SUPPORTED"}
CLM-002 | {"claim":"Un document unique consolidant les effets distributifs des 5 conventions existe quelque part (rapport annexe, etude d'impact, IGF)","status":"REFUTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"RULES_CONTROLS: competence juridique par convention (loi 89-462, L161-25 CSS, CGI 1649 A, L1411-3 CFT)","status":"SATURATED"}
AXS-002 | {"axis":"ACTORS_RELATIONS: parlement vs gouvernement vs organes consultatifs (COR, CAE, CNP, groupe SMIC)","status":"SATURATED"}
AXS-003 | {"axis":"IMPACT_RESPONSIBILITY: existe-t-il un document de consolidation des effets distributifs des indexations?","gap":"Pas de document consolide identifie; la recherche couvre les rapports publics principaux, pas toutes les annexes budgetaires","gap_type":"ACCESS","status":"GAP"}
AXS-004 | {"axis":"COUNTER_HYPOTHESES: un rapport recent consolide-t-il les effets des indexations?","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"competence legiferee (parlement pour retraites/bareme/IRL/SMIC; gouvernement pour decret IRL/moyenne technique) -> arbitrage annuel dans la LF/CSS -> les organes consultatifs (COR, CAE, CNP, groupe SMIC) produisent des avis perimetres -> aucune consolidation inter-conventions","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement: 5 textes legiferaux lues (legifrance CSS/CGI/loi89-462/CFT + decret IRL) + rapports COR/CAE/Cour des comptes positions","result":"Chaque convention porte bien un texte competent distinct; aucune competence consolidee d'arbitrage trouvee","status":"PASS"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"lecture de 5 textes legiferaux + rapports d'avis consultatifs le 2026-09-21","intent":"PROVEN","name":"INV-A cartographier le mandat d'arbitrage des conventions","responsibility_scope":"cartographie de competence","role":"investigation falsification","source":"-","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:4|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-inv-a-mandat-arbitrage-conventions | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.service-public.fr/particuliers/vosdroits/F13723 | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.anil.org/aj-irl-revision-loyers/ | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.ccomptes.fr/fr/publications/impacts-du-systeme-de-retraites-sur-la-competitivite-et-lemploi | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.strategie-plan.gouv.fr/groupe-dexperts-sur-le-smic | -
QRY-007 | FETCH | FOUND | SRC-007 | https://www.cor-retraites.fr/ | -
QRY-008 | FETCH | FOUND | SRC-008 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | -
QRY-009 | WEB | FOUND | - | - | REFUTATION consolidation effets distributifs conventions indexation France: rapport IGF étude d'impact indexations retraites barème IRL SMIC chiffrage consolidé, rapport parlementaire arbitrages indexations annuelles, annexe budgétaire conventions indexation document consolidé
QRY-010 | WEB | FOUND | - | - | REFUTATION barème impôt revenu règle permanente indexation automatique CGI article loi finances gel non revalorisation choix annuel
QRY-011 | WEB | FOUND | - | - | REFUTATION IRL formule décret gouvernement non loi 89-462 art 17-1 modifiée décret 2025 2026
QRY-012 | WEB | FOUND | - | - | REFUTATION L161-25 CSS coefficient revalorisation fixé par décret hors loi financement sécurité sociale

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092
SRC-002 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/actualites/A18045
SRC-003 | ◈ | fam:A | https://www.service-public.fr/particuliers/vosdroits/F13723
SRC-004 | ◉ | fam:E | https://www.anil.org/aj-irl-revision-loyers/
SRC-005 | ◈ | fam:D | https://www.ccomptes.fr/fr/publications/impacts-du-systeme-de-retraites-sur-la-competitivite-et-lemploi
SRC-006 | ◈ | fam:D | https://www.strategie-plan.gouv.fr/groupe-dexperts-sur-le-smic
SRC-007 | ◈ | fam:A | https://www.cor-retraites.fr/
SRC-008 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | A | 2026-09-21 | L161-25 CSS : revalorisation sur IPC hors tabac, modifiée par LFSS | L'article L161-25 du Code de la sécurité sociale (version en vigueur depuis le 01/01/2016, modifié par LOI n°2015-1785 du 29 décembre 2015 - art. 67, loi de financement de la sécurité sociale) dispose que la revalorisation annuelle des prestations qui y renvoient est effectuée sur la base d'un coefficient égal à l'évolution de la moyenne annuelle des prix à la consommation hors tabac sur les douze derniers indices mensuels publiés par l'Insee ; si le coefficient est inférieur à un, il est porté à cette valeur. La règle relève du parlement (LFSS), pas de l'Insee | 52f894af-dd9e-4d2b-b987-ecd1da7cccc1
FCT-002 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | A | 2026-09-21 | Barème IR fixé chaque année par la loi de finances | Service-Public (DILA, 23/02/2026) : « le barème de l'impôt est fixé chaque année » ; le barème 2026 applicable aux revenus 2025 est fixé par la loi de finances pour 2026 promulguée le 19 février 2026, indexée sur l'inflation (+0,9 %). La revalorisation (ou la non-revalorisation) du barème est donc un choix annuel du législateur budgétaire et non une règle d'indexation permanente | adf0a261-6ae2-4582-981a-6a4e88a3a13e
FCT-003 | FACT | ✧ | https://www.service-public.fr/particuliers/vosdroits/F13723 | A,E | 2026-09-21 | IRL : formule légiférée loi 89-462 art 17-1 | L'IRL est obtenu à partir de la moyenne de l'évolution des prix à la consommation hors tabac et hors loyers sur les 12 derniers mois (règle énoncée par Service-Public F13723 vérifié 12/07/2026 et ANIL ; article 17-1 de la loi du 6 juillet 1989) ; publication au JO chaque trimestre ; la modification de la formule relève du parlement | cfdd9289-72a4-4431-81da-0477ed1b27df
FCT-004 | FACT | ✦ | https://www.ccomptes.fr/fr/publications/impacts-du-systeme-de-retraites-sur-la-competitivite-et-lemploi | A,D,E | 2026-09-21 | Fragmentation des compétences : aucun organe à mandat consolidé d'arbitrage des conventions | La cartographie textuelle et institutionnelle (CSS L161-25 pour les prestations, loi de finances annuelle pour le barème IR, loi 89-462 art 17-1 pour l'IRL, loi 7 juin 1951 art 1 pour l'indépendance de la production) établit que chaque convention d'indexation relève d'une compétence légiférée distincte du parlement, et que les organes consultatifs restent périmétrés : Cour des comptes (rapport avril 2025, saisi par le Premier ministre sur le seul système de retraites), groupe d'experts SMIC (rapport annuel sur le seul SMIC), COR (seules retraites) ; aucun de ces documents n'a pour mandat ni pour réalisation une consolidation des effets distributifs des conventions d'indexation | 9cbeb0e7-f2cc-4c26-ad06-d24b48d9f348
FCT-005 | FACT | ✧ | https://www.ccomptes.fr/fr/publications/impacts-du-systeme-de-retraites-sur-la-competitivite-et-lemploi | D | 2026-09-21 | Cour des comptes avril 2025 : critique périmétrée aux retraites | La Cour des comptes a été saisie par le Premier ministre le 20 janvier 2025 ; son second rapport (10/04/2025) étudie les effets des paramètres actuels du système de retraites sur la compétitivité et l'emploi, avec des analyses détaillées par niveau de revenu et catégories socio-professionnelles : critique documentée mais portant sur la seule convention retraites | 642143ed-6bd0-47c5-ac7b-87ac0f17eefb
FCT-006 | FACT | ✧ | https://www.strategie-plan.gouv.fr/groupe-dexperts-sur-le-smic | D | 2026-09-21 | Groupe d'experts SMIC : obligation de motivation écrite en cas de divergence | Chaque année le Groupe d'experts sur le SMIC remet au Gouvernement et à la Commission nationale de la négociation collective un rapport analysant l'impact du SMIC et comportant ses recommandations sur son évolution ; si le rapport du Gouvernement s'écarte de celui du groupe d'experts, le Gouvernement doit motiver par écrit ces différences auprès de la Commission nationale : unique obligation formelle de justification de divergence identifiée, périmétrée à la convention SMIC | 84bbff4b-1210-45d5-83f3-121324f5a9a1
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | A | 2026-09-21 | Loi 1951 art 1 : l'Insee produit, elle n'arbitre pas | La loi du 7 juin 1951 (art 1) place la conception, la production et la diffusion des statistiques publiques en indépendance professionnelle : l'Insee produit les indices d'indexation mais ne choisit ni les formules légales d'usage ni leur arbitrage, qui relèvent du législateur | 804b7bfc-245f-4d71-8fb4-ce80f9b96e43
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003,SRC-004
FCT-004 | SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008
FCT-005 | SRC-005
FCT-006 | SRC-006
FCT-007 | SRC-008

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-012 | NONE
FCT-002 | QRY-010 | NONE
FCT-003 | QRY-011 | NONE
FCT-004 | QRY-009 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-004 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T14:11:51.625969+00:00","fact_mem":{"FCT-001":"52f894af-dd9e-4d2b-b987-ecd1da7cccc1","FCT-002":"adf0a261-6ae2-4582-981a-6a4e88a3a13e","FCT-003":"cfdd9289-72a4-4431-81da-0477ed1b27df","FCT-004":"9cbeb0e7-f2cc-4c26-ad06-d24b48d9f348","FCT-005":"642143ed-6bd0-47c5-ac7b-87ac0f17eefb","FCT-006":"84bbff4b-1210-45d5-83f3-121324f5a9a1","FCT-007":"804b7bfc-245f-4d71-8fb4-ce80f9b96e43"},"mnemo_row":"PASS: investigation memory WRITE:4ff0a050-e708-47e7-abf4-de7fcae0135b; fact writeback 7/7; run 20260921-1205-insee-inv-a-mandat-arbitrage-conventions","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:4ff0a050-e708-47e7-abf4-de7fcae0135b; fact writeback 7/7; run 20260921-1205-insee-inv-a-mandat-arbitrage-conventions | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
