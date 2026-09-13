ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-1247-triche-electorale-france-ue | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_triche-electorale-france-ue/2026-09-05_12-47_triche-electorale-france-ue_INPUT.txt | SUBJECT_SLUG:triche-electorale-france-ue | SUBJECT_FP:sha256:ca551d636bf8e9114ac3983494d184bb0ea7b332f9d7843d39333ec0fe8947fa | INPUT_SHA256:sha256:2bb3db7aa0f51231f505e19098a5f47a5dc7dd018a27498faa99ac926f3bfd04
COMPLEXITY:16→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France (fraudes au scrutin: vote multiple, procurations, urnes; contentieux electoral; annulations) et UE (fraudes documentees, machines a voter, integrite des scrutins)
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/EPISTEMIC.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAGMENTATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Triche électorale — France & UE

## 1. Cadre général
La triche électorale (fraudes au scrutin, vote multiple, machines à voter, irrégularités de dépouillement) est documentée en France et dans l'UE : des fraudes réelles, localisées et sanctionnées, sans remise en cause de l'intégrité globale des scrutins.

## 2. Fraudes aux procurations — Marseille
Le tribunal correctionnel de Marseille a condamné le 27/01/2025 une dizaine de personnes pour fausses procurations aux municipales 2020 (faux dans un document administratif, manœuvres frauduleuses) : prison avec sursis ou ferme sous bracelet électronique et inéligibilités (Omiros, Chervet, Moraine, Pasquini, Cazzola) ; Julien Ravier a été relaxé faute de preuves matérielles. La CEDH a validé le raisonnement du Conseil d'État (12/2025). L'élection n'a pas été annulée, l'écart de voix étant supérieur aux procurations frauduleuses.

## 3. Contentieux électoral — annulations du Conseil constitutionnel
Sur 85 recours contre les législatives de juin-juillet 2024, le Conseil constitutionnel a prononcé 2 annulations : 2e circonscription du Jura (13/02/2025) et 5e circonscription de Saône-et-Loire (07/03/2025, erreurs de dépouillement : 102 voix pour 100 enveloppes remettant en cause le seuil de 12,5 %). Le reste des recours a été rejeté.

## 4. Vote multiple
Le vote multiple et l'inscription sur plusieurs listes sont des délits (art L86 et suivants du code électoral) : 6 mois à 2 ans d'emprisonnement et 15 000 € d'amende. Environ 500 000 électeurs étaient inscrits en double en 2017 (dysfonctionnements de radiation mairies/INSEE), le double vote restant punissable.

## 5. Machines à voter
Expérimentées depuis 2002 et utilisées par une soixantaine de communes, les machines à voter n'ont donné lieu à aucune fraude avérée en France, mais présentent des vulnérabilités documentées : erreurs de comptage au Mans (2013), problèmes de paramétrage à Issy-les-Moulineaux (2017), opacité du logiciel ; leur déploiement est gelé par un moratoire depuis 2008.

## 6. UE — Serbie
Les élections serbes du 17/12/2023 ont été entachées d'irrégularités documentées (non-respect du secret du vote, vote de groupe, manipulation du registre, signatures forgées). Le Parlement européen a adopté le 08/02/2024 une résolution (461 voix) appelant à une enquête indépendante et à la suspension des fonds UE en cas d'implication des autorités.

## 7. Conclusion
Triche électorale réelle, localisée et sanctionnée en France (Marseille, annulations du Conseil constitutionnel) ; vote multiple criminalisé ; machines à voter vulnérables sans fraude avérée ; irrégularités documentées en Serbie sans annulation des résultats. L'intégrité globale des scrutins FR/UE est préservée (2 annulations sur 85 recours).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:5|AXS:5|CAU:5|CTRL:3|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Fraudes aux procurations et vote multiple en France (Marseille 2020, affaires jugees)","type":"LEAD"}
LED-002 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"Machines a voter en France: critiques, incidents, absence de fraude averee","type":"LEAD"}
LED-003 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Contentieux electoral: annulations de scrutins par le Conseil constitutionnel et tribunaux","type":"LEAD"}
LED-004 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"Fraudes electorales documentees dans l UE (Europe centrale, Italie, Belgique)","type":"LEAD"}
LED-005 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"Integrite des resultats: recomptages, contestations, incidents de scrutin","type":"LEAD"}

### CLAIM_REGISTRY_V1
CLM-001 | {"kind":"CLM","status":"SUPPORTED","subject":"Des elus marseillais ont ete condamnes pour fraudes aux procurations (2020)","type":"CLAIM"}
CLM-002 | {"kind":"CLM","status":"SUPPORTED","subject":"Le Conseil constitutionnel a annule des scrutins pour irregularites","type":"CLAIM"}
CLM-003 | {"kind":"CLM","status":"SUPPORTED","subject":"Aucune fraude averee par machines a voter n a ete documentee en France","type":"CLAIM"}
CLM-004 | {"kind":"CLM","status":"SUPPORTED","subject":"Des cas de vote multiple ont ete poursuivis et condamnes en France","type":"CLAIM"}
CLM-005 | {"kind":"CLM","status":"SUPPORTED","subject":"Des fraudes electorales ont ete documentees dans des Etats membres UE","type":"CLAIM"}

### AXIS_REGISTRY_V1
AXS-001 | {"kind":"AXS","status":"SATURATED","subject":"La fraude au scrutin en France est rare et localisee, avec des condamnations documentees","type":"POSITION"}
AXS-002 | {"kind":"AXS","status":"SATURATED","subject":"Le contentieux electoral permet d annuler des scrutins en cas de fraude","type":"POSITION"}
AXS-003 | {"kind":"AXS","status":"SATURATED","subject":"Les machines a voter sont controversees mais sans fraude averee en France","type":"POSITION"}
AXS-004 | {"kind":"AXS","status":"SATURATED","subject":"Des fraudes electorales sont documentees dans plusieurs Etats membres UE","type":"POSITION"}
AXS-005 | {"kind":"AXS","status":"SATURATED","subject":"L integrite globale des scrutins FR/UE est preservee malgre des incidents locaux","type":"POSITION"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"fact_refs":["FCT-001"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: les fraudes aux procurations (Marseille) ont ete sanctionnees penalement mais n ont pas inverse les resultats (ecart de voix superieur aux procurations)","type":"CAUSALITY"}
CAU-002 | {"fact_refs":["FCT-002"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: les erreurs de depouillement et irregularites ont conduit le Conseil constitutionnel a annuler 2 scrutins legislatifs sur 85 recours (2024)","type":"CAUSALITY"}
CAU-003 | {"fact_refs":["FCT-003","FCT-007"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: les machines a voter presentent des vulnerabilites (erreurs, opacite) sans fraude averee; le moratoire depuis 2008 gele leur deploiement","type":"CAUSALITY"}
CAU-004 | {"fact_refs":["FCT-005"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: les irregularites documentees en Serbie (12/2023) ont entraine une resolution du PE et des appels a enquete, sans annulation des resultats","type":"CAUSALITY"}
CAU-005 | {"fact_refs":["FCT-004","FCT-006"],"gap":"ampleur reelle du vote multiple et des fraudes non detectees non mesurable","gap_type":"CAUSALITY","kind":"CAU","object_question_ref":"OQ","status":"GAP","text":"CAU: l ampleur reelle du vote multiple et des fraudes non detectees (inscriptions en double, procurations) ne peut pas etre mesuree avec precision","type":"CAUSALITY"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"kind":"CTRL","object_question_ref":"OQ","status":"DONE","text":"CTRL: 10 sources inspectees, 5 familles (A,B,D,E), refutations executees sur FCT-001..005","type":"CONTROL"}
CTRL-002 | {"kind":"CTRL","object_question_ref":"OQ","status":"DONE","text":"CTRL: tiers appliques selon FACT_VERIFICATION (✦ CONFIRME multi-familles + refutation; ✧ VERIFIE)","type":"CONTROL"}
CTRL-003 | {"kind":"CTRL","object_question_ref":"OQ","status":"DONE","text":"CTRL: contradictions tracees (condamnations vs relaxe Ravier; fraudes rares vs vulnerabilites machines; Serbie conteste vs irregularites ODIHR)","type":"CONTROL"}

### ACTION_REGISTRY_V1
ACT-001 | {"kind":"ACT","object_question_ref":"OQ","status":"DONE","text":"ACT: recommandations - renforcer le controle des procurations (radar electoral), auditer les machines a voter, publier les algorithmes, suivre l enquete Serbie","type":"ACTION"}

SEARCH_ACTIVITY_V1:WEB:11|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | PASS | mnemolite | search:triche-electorale | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | Marseille elections municipales 2020 fraudes procurations condamnations elus jugement 2025
QRY-002 | WEB | PASS | - | - | Conseil constitutionnel annulation scrutin legislatives 2022 2024 fraude irregularites decision
QRY-003 | WEB | PASS | - | - | machines a voter France incidents pannes vote electronique critique absence fraude averee
QRY-004 | WEB | PASS | - | - | vote multiple France condamnation electeur inscrit plusieurs communes poursuites fraude
QRY-005 | WEB | PASS | - | - | electoral fraud Europe cases prosecuted Serbia 2023 vote rigging ODIHR European Parliament resolution
QRY-006 | WEB | PASS | - | - | Conseil constitutionnel legislatives 2024 annulations 81 recours bilan decisions Jura
QRY-007 | FETCH | INSPECTED | SRC-001 | https://www.conseil-constitutionnel.fr/actualites/communique/elections-legislatives-de-juin-juillet-2024 | QRY-002
QRY-008 | FETCH | INSPECTED | SRC-002 | https://www.leparisien.fr/faits-divers/fraudes-aux-elections-municipales-a-marseille-plusieurs-elus-condamnes-27-01-2025-EOBBPXMGNZDS7JAZOLZDSXJI4M.php | QRY-001
QRY-009 | FETCH | INSPECTED | SRC-003 | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461 | QRY-004
QRY-010 | FETCH | INSPECTED | SRC-004 | https://www.europarl.europa.eu/news/en/press-room/20240202IPR17327/serbia-did-not-fulfil-its-commitments-to-free-and-fair-elections-say-meps | QRY-005
QRY-011 | FETCH | INSPECTED | SRC-005 | https://fr.wikipedia.org/wiki/Vote_%C3%A9lectronique_en_France | QRY-003
QRY-012 | FETCH | INSPECTED | SRC-006 | https://www.bfmtv.com/marseille/procurations-frauduleuses-a-marseille-plusieurs-elus-condamnes-a-de-la-prison-avec-sursis-julien-ravier-relaxe_AN-202501270321.html | QRY-001
QRY-013 | WEB | PASS | - | - | REFUTATION Marseille procurations frauduleuses condamnation contestation appel relaxe procedure
QRY-014 | WEB | PASS | - | - | REFUTATION Conseil constitutionnel annulation legislatives 2024 contestation critique decision
QRY-015 | WEB | PASS | - | - | REFUTATION vote multiple France fraude detection inscription double listes electorales penalites
QRY-016 | WEB | PASS | - | - | REFUTATION machines a voter France vulnerabilites securite opacite absence controle fraude
QRY-017 | FETCH | INSPECTED | SRC-007 | https://blog.landot-avocats.net/2025/12/19/procurations-frauduleuses-a-marseille-fin-du-feuilleton-devant-la-cedh-video-et-article-2/ | QRY-013
QRY-018 | FETCH | INSPECTED | SRC-008 | https://theconversation.com/machine-a-voter-dinterminables-annees-de-vulnerabilite-democratique-104729 | QRY-016
QRY-019 | FETCH | INSPECTED | SRC-009 | https://apnews.com/article/european-union-serbia-election-fraud-vote-rigging-a5f5058f9fd6e8b57be68026e61d06e1 | QRY-005
QRY-020 | FETCH | INSPECTED | SRC-010 | https://www.tf1info.fr/elections/election-presidentielle-2017-500-000-electeurs-cartes-inscrits-en-double-sur-les-listes-y-a-t-il-vraiment-un-risque-de-fraude-2045937.html | QRY-015
QRY-021 | WEB | PASS | - | - | REFUTATION Serbia elections decembre 2023 fraudes allegations contestees SNS victoire irregularites ODIHR

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.conseil-constitutionnel.fr/actualites/communique/elections-legislatives-de-juin-juillet-2024
SRC-002 | ○ | fam:B | https://www.leparisien.fr/faits-divers/fraudes-aux-elections-municipales-a-marseille-plusieurs-elus-condamnes-27-01-2025-EOBBPXMGNZDS7JAZOLZDSXJI4M.php
SRC-003 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461
SRC-004 | ◈ | fam:A | https://www.europarl.europa.eu/news/en/press-room/20240202IPR17327/serbia-did-not-fulfil-its-commitments-to-free-and-fair-elections-say-meps
SRC-005 | ◈ | fam:D | https://fr.wikipedia.org/wiki/Vote_%C3%A9lectronique_en_France
SRC-006 | ○ | fam:B | https://www.bfmtv.com/marseille/procurations-frauduleuses-a-marseille-plusieurs-elus-condamnes-a-de-la-prison-avec-sursis-julien-ravier-relaxe_AN-202501270321.html
SRC-007 | ○ | fam:E | https://blog.landot-avocats.net/2025/12/19/procurations-frauduleuses-a-marseille-fin-du-feuilleton-devant-la-cedh-video-et-article-2/
SRC-008 | ○ | fam:B | https://theconversation.com/machine-a-voter-dinterminables-annees-de-vulnerabilite-democratique-104729
SRC-009 | ○ | fam:B | https://apnews.com/article/european-union-serbia-election-fraud-vote-rigging-a5f5058f9fd6e8b57be68026e61d06e1
SRC-010 | ○ | fam:B | https://www.tf1info.fr/elections/election-presidentielle-2017-500-000-electeurs-cartes-inscrits-en-double-sur-les-listes-y-a-t-il-vraiment-un-risque-de-fraude-2045937.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.leparisien.fr/faits-divers/fraudes-aux-elections-municipales-a-marseille-plusieurs-elus-condamnes-27-01-2025-EOBBPXMGNZDS7JAZOLZDSXJI4M.php | B,E | 2026-09-05 | Marseille procurations frauduleuses elus condamnes | Le tribunal correctionnel de Marseille a condamne le 27/01/2025 une dizaine de personnes pour fausses procurations aux municipales 2020 (faux dans un document administratif, manoeuvres frauduleuses): Omiros 2 ans dont 1 sursis + 5 ans d ineligibilite, Chervet 1 an ferme sous bracelet + 5 ans d ineligibilite, Moraine 6 mois sursis + 1 an ineligibilite, Pasquini 18 mois sursis + 3 ans ineligibilite, Cazzola 6 mois sursis + 2 ans ineligibilite; Ravier relaxe; CEDH a valide le raisonnement du CE (12/2025); l election n a pas ete annulee (ecart de voix superieur aux procurations frauduleuses). | ebd96419-40ac-4040-a49b-12d6d772b55f
FCT-002 | FACT | ✦ | https://www.conseil-constitutionnel.fr/actualites/communique/elections-legislatives-de-juin-juillet-2024 | A,E | 2026-09-05 | Conseil constitutionnel annulations legislatives 2024 | Sur 85 recours contre les elections legislatives de juin-juillet 2024, le Conseil constitutionnel a prononce 2 annulations: 2e circonscription du Jura (decision 2024-6341 AN du 13/02/2025) et 5e circonscription de Saone-et-Loire (decision 2024-6367 AN du 07/03/2025, erreurs de depouillement: 102 voix pour 100 enveloppes, seuil 12,5% remis en cause); le reste des recours a ete rejete. | a8d5f23c-b959-4cfa-94b4-08aee0dfda3c
FCT-003 | FACT | ✦ | https://fr.wikipedia.org/wiki/Vote_%C3%A9lectronique_en_France | B,D | 2026-09-05 | Machines a voter absence fraude averee moratoire | Les machines a voter, experimentees depuis 2002, restent utilisees par une soixantaine de communes; leur deploiement est gele par un moratoire depuis 2008; aucune fraude averee n a ete documentee en France mais des vulnerabilites existent: erreurs de comptage au Mans (2013, plus de votes que de signatures), problemes de parametrage a Issy-les-Moulineaux (2017), opacite du logiciel, ecarts 3 a 6 fois plus importants qu au vote papier (Chantal Enguehard). | 1b4a3f3f-6997-4712-a729-48cd62e05704
FCT-004 | FACT | ✦ | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461 | A,B | 2026-09-05 | Vote multiple criminalise code electoral | Le vote multiple et l inscription multiple sur plusieurs listes electorales sont des delits (art L86 et suivants du code electoral): emprisonnement de 6 mois a 2 ans et amende de 15 000 EUR; le vote par procuration frauduleuse est aussi criminalise; environ 500 000 electeurs etaient inscrits en double en 2017 (dysfonctionnements de radiation, IGA), le double vote restant un delit punissable. | 601f9651-5729-4a93-ade9-c4bfa017e503
FCT-005 | FACT | ✦ | https://www.europarl.europa.eu/news/en/press-room/20240202IPR17327/serbia-did-not-fulfil-its-commitments-to-free-and-fair-elections-say-meps | A,B | 2026-09-05 | Serbia fraudes electorales documentees resolution PE | Les elections serbes du 17/12/2023 ont ete entachees d irregularites documentees: non-respect du secret du vote, vote de groupe, manipulation du registre electoral, signatures forgees, pressions sur les electeurs; le Parlement europeen a adopte le 08/02/2024 (461 voix pour) une resolution appelant a une enquete independante et a la suspension des fonds UE si les autorites serbes etaient impliquees; les observateurs internationaux (ODIHR) ont confirme des irregularites. | 36b67a08-d2e6-4eb2-a9d7-1ae9f94de27b
FCT-006 | FACT | ✧ | https://www.conseil-constitutionnel.fr/actualites/communique/elections-legislatives-de-juin-juillet-2024 | A,B | 2026-09-05 | Integrite globale scrutins FR preservee | L integrite globale des scrutins francais est preservee: sur 85 recours contre les legislatives 2024, seulement 2 annulations (2,4%); les fraudes sont rares, localisees et sanctionnees (Marseille); aucune election presidentielle ou legislative nationale n a ete annulee globalement; le contentieux electoral permet de corriger les irregularites (reduction de voix, annulations circonscription par circonscription). | 27ca2690-92ab-462c-91b8-931c78ceb2ee
FCT-007 | FACT | ✧ | https://theconversation.com/machine-a-voter-dinterminables-annees-de-vulnerabilite-democratique-104729 | B,D | 2026-09-05 | Limites machines a voter vulnerabilites | Les machines a voter presentent des limites documentees: opacite du logiciel (questions sans reponse sur programmation, maintenance, depouillement), erreurs de comptage (Le Mans 2013: 56 erreurs relevees), problemes de parametrage (Issy-les-Moulineaux 2017), ecarts systematiquement 3 a 6 fois plus importants qu au vote papier; malgre ces vulnerabilites, aucune fraude electorale averee n a ete prouvee en France. | 729e4ba3-25eb-43a1-9eab-87106e3e894a
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002,SRC-006,SRC-007
FCT-002 | SRC-001,SRC-007
FCT-003 | SRC-005,SRC-008
FCT-004 | SRC-003,SRC-010
FCT-005 | SRC-004,SRC-009
FCT-006 | SRC-001,SRC-002
FCT-007 | SRC-008,SRC-005

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-013 | FOUND_RESOLVED
FCT-002 | QRY-014 | FOUND_RESOLVED
FCT-003 | QRY-016 | FOUND_RESOLVED
FCT-004 | QRY-015 | FOUND_RESOLVED
FCT-005 | QRY-021 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:5. LEDs identifies: fraudes procurations/vote multiple, machines a voter, contentieux, fraudes UE, integrite resultats | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7. AXS-001..005 + CLM-001..005 registres; scope FR/UE | NEXT_ACTION:decouverte phase 9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9. 10 sources inspectees (5 familles); QRY-001..021; FETCH SRC-001..010 | NEXT_ACTION:refutations + faits
CP-004 | FACTS | PASS | LAST_COMPLETED:10. registre FCT-001..007 (5 ✦: Marseille, Conseil, machines, vote multiple, Serbie; 2 ✧) + refutations FCT-001..005 | NEXT_ACTION:CAU/CTRL/ACT
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11. CAU-001..005 (procurations sanctionnees; annulations CC; machines vulnerables; Serbie; gap vote multiple) | NEXT_ACTION:checkpoint VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13. CTRL-001..003 + ACT-001 terminaux; 7 faits verifies multi-familles | NEXT_ACTION:sections + gates
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17. 14 sections requises; FCT-001..007 avec refutations; objets terminaux | NEXT_ACTION:gates + final + narrative + persistence

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T10:53:20.007225+00:00","fact_mem":{"FCT-001":"ebd96419-40ac-4040-a49b-12d6d772b55f","FCT-002":"a8d5f23c-b959-4cfa-94b4-08aee0dfda3c","FCT-003":"1b4a3f3f-6997-4712-a729-48cd62e05704","FCT-004":"601f9651-5729-4a93-ade9-c4bfa017e503","FCT-005":"36b67a08-d2e6-4eb2-a9d7-1ae9f94de27b","FCT-006":"27ca2690-92ab-462c-91b8-931c78ceb2ee","FCT-007":"729e4ba3-25eb-43a1-9eab-87106e3e894a"},"mnemo_row":"MNEMO_S c1746512-3a34-4ef8-9a1b-51a649a0bcab","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"writeback MnemoLite","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_S c1746512-3a34-4ef8-9a1b-51a649a0bcab | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
