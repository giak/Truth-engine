ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-0738-frappes-juridiques-veille-reglementaire | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_frappes-juridiques-veille-reglementaire/2026-08-31_07-38_frappes-juridiques-veille-reglementaire_INPUT.txt | SUBJECT_SLUG:frappes-juridiques-veille-reglementaire | SUBJECT_FP:sha256:b38eae0369c68d07550a40c3816f8bb662859db309bd7f9e007c3321f9dff012 | INPUT_SHA256:sha256:b38eae0369c68d07550a40c3816f8bb662859db309bd7f9e007c3321f9dff012
COMPLEXITY:6→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'lead_question': 'Are the three open legal frappes (RGPD badge-data retention, L2224-14 equality vs vehicle quotas, SITREVA procurement legality) valid to raise in the article, and what is the status of the four awaited publications (ADEME wild-dumping study, PMCB 2027 final texts, Senat PPL 24-079, <=10m3 fund)?'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Ce que l'enquête établit

### Frappe 1 — RGPD : les données de passage ont des durées de conservation précises (FCT-001, FCT-002)

Le contrôle d'accès en déchèterie — badge ou lecture automatisée de plaques d'immatriculation (LAPI) — traite des données personnelles identifiantes. La doctrine CNIL fixe des bases claires :

- **Journalisation d'accès** : suppression **3 mois** après enregistrement (doctrine « accès aux locaux », fiche mise à jour le 17/06/2026) ;
- **LAPI** : données sans rapprochement positif conservées **15 jours maximum** à compter de la collecte, effacées automatiquement ensuite ; données avec rapprochement **1 mois** (délibération 2024-042 du 13/06/2024, conforme à l'article L. 233-2 du code de la sécurité intérieure) ;
- **ACVR** (voies réservées) : suppression dès constat de conformité, sinon **8 jours ouvrés** maximum (page CNIL LAPI, 05/06/2025).

**Modalisation obligatoire (LOI 13)** : il n'existe **aucun référentiel CNIL spécifique aux déchèteries**. Ces durées sont transposées des doctrines « accès aux locaux / RH » et « stationnement payant / LAPI ». Un article doit les présenter comme « bases de doctrine applicables par transposition », pas comme un cadre déchèterie dédié. Le SICTIAM (union de collectivités, 04/06/2026) confirme que le LAPI en déchèterie est « autorisé à condition d'être strictement encadré » — plaque référencée en base au préalable, durée définie en rapport avec la finalité.

**GAP nommé (DOCTRINE_TRANSPOSITION)** : aucune enquête publique n'a audité les durées réellement configurées chez les opérateurs de déchèteries.

### Frappe 2 — Quotas par catégorie de véhicule : légalement défendables (FCT-003)

La crainte d'un conflit avec le principe d'égalité de traitement (CGCT L2224-14) ne survit pas à l'examen. La Métropole de Lyon documente publiquement la chaîne juridique : la collectivité n'est compétente que pour les déchets **ménagers et assimilés** — c'est-à-dire produits dans des conditions comparables à un ménage en nature et quantité. Le règlement intérieur peut donc différencier les véhicules : utilitaires ≤ 2 t gratuits mais limités à 4 passages/mois, utilitaires > 2 t payants (4 passages/mois, 10 achats/mois, 50/an par usager), véhicules > 3,5 t interdits pour sécurité. Au-delà du quota, les déchets ne sont plus « assimilés » et ne peuvent plus être pris en charge par un service financé par la TEOM.

**GAP nommé (JURISPRUDENCE_ABSENT)** : aucune décision de juge administratif testant les quotas contre l'égalité de traitement n'a été trouvée. L'article doit dire « juridiquement fondé, jamais contesté avec succès — ni, apparemment, contesté du tout ».

### Frappe 3 — SITREVA / Rennes : le soupçon de marché sans publicité ne tient plus pour la génération actuelle (FCT-004)

L'avis BOAMP n° 25-65097 du 11/06/2025 publie l'attribution du marché « Exploitation du réseau des déchèteries et plateformes de végétaux de Rennes Métropole » (identifiant 2025-2520158). Le contrat d'exploitation actuel est donc **publiquement annoncé**. La frappe SITREVA doit être rescopée : la question de la procédure négociée sans publicité ne vaut, au plus, que pour des générations de contrats antérieures — non revérifiées (**GAP HISTORIC_PROCEDURE_UNVERIFIED**).

### Veille réglementaire — état au 31/08/2026 (FCT-005, FCT-006, FCT-007)

| Publication | État vérifié |
|---|---|
| **Textes finaux refondation REP PMCB 2027** | Décret/arrêté en finalisation, publication attendue **fin août 2026**, premier effet 01/09/2026 ; nouveaux agréments éco-organismes au 01/01/2027 ; les matériaux « matures » sortent de la reprise sans frais au 01/01/2027 (FNTP, 02/07/2026). En parallèle, la FNTP a un recours en cours au Conseil d'État estimant **34 M€** d'écocontributions indûment payées par les TP en 2024. Des fournisseurs annoncent déjà des hausses d'écocontribution pré-refondation pour stabiliser leur trésorerie. |
| **Étude ADEME dépôts sauvages** | Lancée le 20/05/2026 (Ecogeos + Rudologia) ; les collectivités étaient invitées à répondre jusqu'au 13/07/2026 (préfecture de l'Eure, 06/07/2026). **Résultats non publiés au 31/08/2026** — la chaîne causale « contrôle d'accès → dépôts sauvages » reste une corrélation documentée, la causalité attend l'étude. |
| **PPL risque incendie (Sénat l24-367)** | Adoptée à l'unanimité par la commission le 19/02/2025 puis en séance (6 mars) : fonds d'indemnisation des incendies dus aux batteries lithium (article 2), intégration des cartouches de gaz à la REP DDS (article 3), prise en charge du ramassage (article 4). **Toujours en navette parlementaire, pas de loi promulguée au 31/08/2026.** |
| **Fonds dépôts sauvages ≤ 10 m³** | Demande AMF/CAPEB du 27/03/2026 — aucune décision publiée trouvée. |

### Ce que l'article doit faire de ces résultats

1. **Citer les durées CNIL avec leur modalisation exacte** : « la doctrine CNIL fixe 3 mois pour les journaux d'accès et 15 jours pour les plaques non rapprochées — par transposition, aucun référentiel déchèterie n'existe ».
2. **Présenter les quotas comme légalement fondés** (régime des déchets assimilés), tout en nommant l'absence de jurisprudence.
3. **Retirer le soupçon SITREVA** pour le contrat rennais actuel (BOAMP publié) et le rescoper sur l'historique.
4. **Citer les quatre publications comme attendues, pas comme résultats** : la phrase « selon l'étude ADEME à paraître » est la forme correcte ; « l'étude ADEME montre » est interdite.

## Ce qui reste ouvert

- **Publication PMCB** (fin août 2026 annoncé) : re-vérifier JORF à la livraison de l'article — si les textes sont sortis entre-temps, la section mutation 2025-2026 doit être mise à jour.
- **Étude ADEME** : tout verdict causal sur dépôts sauvages reste conditionnel.
- **Cote exacte délibération Gradignan** : hors périmètre de ce run (demande Archives BM toujours en attente).
- **Récit ANRED 1987** : toujours OPEN, présenté comme non vérifié.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:4|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Badge/plate data at decheteries are subject to RGPD retention limits (3-month baseline for access logs; 15-day LAPI pattern)","counter":"NONE_FOUND","gap":"No decheterie-specific CNIL referential exists; doctrine is transposed from workplace/parking","gap_type":"DOCTRINE_TRANSPOSITION","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"Vehicle quotas rest on the dechets assimiles legal basis and are defensible under L2224-14","counter":"NONE_FOUND","gap":"No litigation found testing quotas against equal-treatment doctrine","gap_type":"JURISPRUDENCE_ABSENT","status":"SUPPORTED","support":["FCT-003"]}
CLM-003 | {"claim":"SITREVA procurement-legality concern is resolved for the current contract generation","counter":"NONE_FOUND","gap":"Historic 2016-2020 award procedure not re-verified","gap_type":"HISTORIC_PROCEDURE_UNVERIFIED","status":"SUPPORTED","support":["FCT-004"]}
CLM-004 | {"claim":"PMCB refondation texts publish end of August 2026; agrements renew 01/01/2027","counter":"FNTP CE recours may delay arrete listing TP materials","gap":"Final texts not yet published","gap_type":"PUBLICATION_PENDING","status":"SUPPORTED","support":["FCT-005"]}
CLM-005 | {"claim":"ADEME wild-dumping study is in fieldwork; results pending","counter":"NONE_FOUND","gap":"Publication date unknown","gap_type":"PUBLICATION_PENDING","status":"SUPPORTED","support":["FCT-006"]}
CLM-006 | {"claim":"Fire-risk compensation fund PPL adopted by Senat first reading; not yet law","counter":"NONE_FOUND","gap":"Assembly second-reading outcome unknown","gap_type":"NAVETTE_OPEN","status":"SUPPORTED","support":["FCT-007"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"RGPD: what retention periods apply to badge/plate passage data collected by decheterie access-control systems, and is retention documented by vendors/collectivites?","routes":["RULES_CONTROLS"],"sought_objects":["CNIL guidance","vendor privacy policies","RGPD retention notices"],"status":"SATURATED"}
AXS-002 | {"question":"Does conditioning decheterie access on vehicle category quotas conflict with CGCT L2224-14 equal treatment of users?","routes":["RULES_CONTROLS"],"sought_objects":["L2224-14 text","prefecture/DGALN guidance","any litigation"],"status":"SATURATED"}
AXS-003 | {"question":"Was the SITREVA (Rennes Metropole) decheterie contract lawfully awarded as a negotiated procedure without advertising?","routes":["RULES_CONTROLS"],"sought_objects":["BOAMP/TED notice","marche public decision","DAJ guidance"],"status":"SATURATED"}
AXS-004 | {"question":"What is the current status of: ADEME wild-dumping study, PMCB 2027 final texts, Senat PPL 24-079, AMF/CAPEB <=10m3 fund?","routes":["EVIDENCE_CASES"],"sought_objects":["ADEME publication page","JORF/consultation records","Senat dossier 24-079"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Quota enforcement requires per-vehicle identity","effect":"Access-control systems collect identifiable passage data (badge id, plate) at decheteries","mechanism":"Access-control vendor stores badge/plate records; retention set by collectivite RGPD notice","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CAU-002 | {"cause":"Dechets assimiles regime (CGCT L2224-14) limits the TEOM-funded service to household-comparable waste","effect":"Vehicle-category quotas are legally defensible, not arbitrary","mechanism":"Reglement interieur differentiates PTAC categories; Lyon FAQ documents the reasoning","status":"SUPPORTED","support":["FCT-003"]}
CAU-003 | {"cause":"Marche public advertising rules","effect":"Rennes decheterie exploitation contract is publicly advertised","mechanism":"BOAMP avis 25-65097 published 11/06/2025 for the exploitation contract","status":"SUPPORTED","support":["FCT-004"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:19|FETCH:31|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-003 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime | FCT-007 | REPAIR_FACT
SYS-009 | SYS | FOUND | - | warm-route-none | MNEMO_Q
SYS-010 | SYS | PARTIAL | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-011 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | WEB | PARTIAL | - | https://www.sictiam.fr/cameras-a-lecture-automatisee-de-plaques-dimmatriculation-et-acces-a-la-decheterie-un-dispositif-autorise-a-condition-detre-strictement-encadre/ | SICTIAM LAPI decheterie encadrement
QRY-002 | FETCH | OK | - | https://www.cnil.fr/fr/les-dispositifs-de-lecture-automatisee-de-plaque-dimmatriculation-lapi | CNIL LAPI dispositifs durees conservation
QRY-003 | FETCH | OK | - | https://www.cnil.fr/fr/acces-locaux-controle-des-horaires-au-travail | CNIL acces locaux horaires badge journalisation 3 mois
QRY-004 | FETCH | OK | - | https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees | CNIL durees de conservation referentiels
QRY-005 | FETCH | OK | - | https://www.doctrine.fr/d/CNIL/2024/CNILTEXT000050361934 | CNIL 2024-042 STCL LAPI 15 jours
QRY-006 | WEB | OK | - | - | CGCT L2224-14 egalite traitement decheterie quotas
QRY-007 | FETCH | OK | - | https://grandlyon-passdecheterie.horanet.com/faq | Grand Lyon Pass Decheterie FAQ quotas utilitaires
QRY-008 | WEB | OK | - | - | L2224-14 dechets assimiles reglement interieur differentiation vehicules
QRY-009 | WEB | PARTIAL | - | - | Defenseur des droits decheterie refus acces badge quota
QRY-010 | WEB | OK | - | - | SITREVA Rennes Metropole marche exploitation decheteries BOAMP
QRY-011 | FETCH | OK | - | https://www.francemarches.com/files/BOAMP/25-65097.html | BOAMP 25-65097 avis attribution exploitation reseau decheteries Rennes
QRY-012 | WEB | OK | - | - | ADEME etude nationale depots sauvages 2026 Ecogeos Rudologia
QRY-013 | WEB | OK | - | - | PPL Senat incendie dechets batteries lithium fonds indemnisation navette
QRY-014 | FETCH | OK | - | https://www.fntp.fr/rep-pmcb-ou-en-est-on/ | FNTP REP PMCB refondation calendrier
QRY-015 | WEB | OK | - | - | REFUTATION CNIL LAPI retention rules: decheterie plaque conservation autre chiffre 30 jours 8 jours ouvre dementi
QRY-016 | WEB | OK | - | - | REFUTATION CNIL badge access-log retention: badge journalisation autre duree 6 mois 1 an decheterie
QRY-017 | WEB | OK | - | - | REFUTATION Lyon Pass Decheterie quota legal framing: quotas decheterie autre chiffre 6 passages 12 passages illimite
QRY-018 | WEB | OK | - | - | REFUTATION Rennes decheterie contract procedure: SITREVA marche sans publicite recours tribunal rennes decheterie
QRY-019 | WEB | OK | - | - | REFUTATION PMCB refondation calendar: decret PMCB publie JORF aout 2026 reporte
QRY-020 | WEB | OK | - | - | REFUTATION ADEME wild-dumping study status: etude ADEME depots sauvages resultats publies 2026
QRY-021 | WEB | OK | - | - | REFUTATION PPL fire-risk fund status: loi incendie dechets promulguee JORF 2026 fonds
QRY-022 | WEB | OK | - | - | REFUTATION CNIL LAPI retention rules: LAPI decheterie plaque conservation autre chiffre dementi 15 jours
QRY-023 | WEB | OK | - | - | REFUTATION CNIL badge access-log retention: badge journalisation 3 mois autre duree 6 mois 1 an
QRY-024 | WEB | OK | - | - | REFUTATION PMCB refondation calendar: decret PMCB refondation publie reporte calendrier autre date
QRY-025 | WEB | OK | - | - | REFUTATION ADEME wild-dumping study status: etude ADEME depots sauvages resultats publies Ecogeos
QRY-026 | WEB | OK | - | - | REFUTATION PPL fire-risk fund status: loi incendie dechets fonds indemnisation promulguee
QRY-027 | FETCH | OK | - | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | AMORCE ADEME etude depots sauvages
QRY-028 | FETCH | OK | - | https://www.eure.gouv.fr/Actualites/Enquete-nationale-sur-les-dechets-sauvages-les-collectivites-invitees-a-participer | Eure enquete nationale dechets sauvages
QRY-029 | FETCH | OK | - | https://www.senat.fr/rap/l24-367/l24-367_mono.html | Senat PPL incendie lithium fonds indemnisation
QRY-030 | FETCH | PARTIAL | - | https://www.sictiam.fr/cameras-a-lecture-automatisee-de-plaques-dimmatriculation-et-acces-a-la-decheterie-un-dispositif-autorise-a-condition-detre-strictement-encadre/ | SICTIAM LAPI decheterie encadrement
QRY-031 | FETCH | FAIL | - | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023268857 | L2224-14 texte integrale
QRY-032 | FETCH | OK | - | https://www.defenseurdesdroits.fr/la-defenseure-des-droits-publie-son-rapport-annuel-pour-lannee-2025-1108 | Defenseur des droits rapport 2025
QRY-033 | FETCH | OK | - | https://www.sictiam.fr/cameras-a-lecture-automatisee-de-plaques-dimmatriculation-et-acces-a-la-decheterie-un-dispositif-autorise-a-condition-detre-strictement-encadre/ | SICTIAM LAPI decheterie encadrement
QRY-034 | FETCH | OK | - | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | AMORCE ADEME etude depots sauvages
QRY-035 | FETCH | OK | - | https://www.eure.gouv.fr/Actualites/Enquete-nationale-sur-les-dechets-sauvages-les-collectivites-invitees-a-participer | Eure enquete nationale dechets sauvages
QRY-036 | FETCH | OK | - | https://www.senat.fr/rap/l24-367/l24-367_mono.html | Senat PPL incendie lithium fonds
QRY-037 | FETCH | OK | - | https://www.defenseurdesdroits.fr/la-defenseure-des-droits-publie-son-rapport-annuel-pour-lannee-2025-1108 | Defenseur des droits rapport 2025
QRY-038 | FETCH | FAIL | - | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023268857 | L2224-14 Legifrance fetch
QRY-039 | FETCH | INSPECTED | SRC-017 | https://www.cnil.fr/fr/les-dispositifs-de-lecture-automatisee-de-plaque-dimmatriculation-lapi | CNIL LAPI dispositifs durees conservation
QRY-040 | FETCH | INSPECTED | SRC-018 | https://www.cnil.fr/fr/acces-locaux-controle-des-horaires-au-travail | CNIL acces locaux horaires badge journalisation 3 mois
QRY-041 | FETCH | INSPECTED | SRC-019 | https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees | CNIL durees de conservation referentiels
QRY-042 | FETCH | INSPECTED | SRC-020 | https://www.doctrine.fr/d/CNIL/2024/CNILTEXT000050361934 | CNIL 2024-042 STCL LAPI 15 jours
QRY-043 | FETCH | INSPECTED | SRC-021 | https://www.sictiam.fr/cameras-a-lecture-automatisee-de-plaques-dimmatriculation-et-acces-a-la-decheterie-un-dispositif-autorise-a-condition-detre-strictement-encadre/ | SICTIAM LAPI decheterie encadrement
QRY-044 | FETCH | INSPECTED | SRC-022 | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | AMORCE ADEME etude depots sauvages
QRY-045 | FETCH | INSPECTED | SRC-023 | https://www.eure.gouv.fr/Actualites/Enquete-nationale-sur-les-dechets-sauvages-les-collectivites-invitees-a-participer | Eure enquete nationale dechets sauvages
QRY-046 | FETCH | INSPECTED | SRC-024 | https://www.senat.fr/rap/l24-367/l24-367_mono.html | Senat PPL incendie lithium fonds indemnisation
QRY-047 | FETCH | INSPECTED | SRC-025 | https://www.defenseurdesdroits.fr/la-defenseure-des-droits-publie-son-rapport-annuel-pour-lannee-2025-1108 | Defenseur des droits rapport 2025
QRY-048 | FETCH | INSPECTED | SRC-026 | https://www.francemarches.com/files/BOAMP/25-65097.html | BOAMP 25-65097 avis attribution Rennes
QRY-049 | FETCH | INSPECTED | SRC-027 | https://www.fntp.fr/rep-pmcb-ou-en-est-on/ | FNTP REP PMCB refondation calendrier
QRY-050 | FETCH | INSPECTED | SRC-028 | https://grandlyon-passdecheterie.horanet.com/faq | Grand Lyon Pass Decheterie FAQ

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.cnil.fr/fr/les-dispositifs-de-lecture-automatisee-de-plaque-dimmatriculation-lapi
SRC-002 | ◈ | fam:A | https://www.cnil.fr/fr/acces-locaux-controle-des-horaires-au-travail
SRC-003 | ◈ | fam:A | https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees
SRC-004 | ◉ | fam:D | https://www.doctrine.fr/d/CNIL/2024/CNILTEXT000050361934
SRC-005 | ◉ | fam:D | https://www.sictiam.fr/cameras-a-lecture-automatisee-de-plaques-dimmatriculation-et-acces-a-la-decheterie-un-dispositif-autorise-a-condition-detre-strictement-encadre/
SRC-006 | ◈ | fam:A | https://grandlyon-passdecheterie.horanet.com/faq
SRC-007 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023268857
SRC-008 | ◉ | fam:D | https://www.defenseurdesdroits.fr/la-defenseure-des-droits-publie-son-rapport-annuel-pour-lannee-2025-1108
SRC-009 | ◈ | fam:A | https://www.francemarches.com/files/BOAMP/25-65097.html
SRC-010 | ◈ | fam:A | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages
SRC-011 | ◈ | fam:A | https://www.eure.gouv.fr/Actualites/Enquete-nationale-sur-les-dechets-sauvages-les-collectivites-invitees-a-participer
SRC-012 | ◈ | fam:A | https://www.senat.fr/rap/l24-367/l24-367_mono.html
SRC-013 | ◈ | fam:A | https://www.fntp.fr/rep-pmcb-ou-en-est-on/
SRC-014 | ◈ | fam:A | https://grandlyon-passdecheterie.horanet.com/faq
SRC-015 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023268857
SRC-016 | ◉ | fam:D | https://www.defenseurdesdroits.fr/la-defenseure-des-droits-publie-son-rapport-annuel-pour-lannee-2025-1108
SRC-017 | ◈ | fam:A | https://www.cnil.fr/fr/les-dispositifs-de-lecture-automatisee-de-plaque-dimmatriculation-lapi
SRC-018 | ◈ | fam:A | https://www.cnil.fr/fr/acces-locaux-controle-des-horaires-au-travail
SRC-019 | ◈ | fam:A | https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees
SRC-020 | ◉ | fam:D | https://www.doctrine.fr/d/CNIL/2024/CNILTEXT000050361934
SRC-021 | ◉ | fam:D | https://www.sictiam.fr/cameras-a-lecture-automatisee-de-plaques-dimmatriculation-et-acces-a-la-decheterie-un-dispositif-autorise-a-condition-detre-strictement-encadre/
SRC-022 | ◈ | fam:A | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages
SRC-023 | ◈ | fam:A | https://www.eure.gouv.fr/Actualites/Enquete-nationale-sur-les-dechets-sauvages-les-collectivites-invitees-a-participer
SRC-024 | ◈ | fam:A | https://www.senat.fr/rap/l24-367/l24-367_mono.html
SRC-025 | ◉ | fam:D | https://www.defenseurdesdroits.fr/la-defenseure-des-droits-publie-son-rapport-annuel-pour-lannee-2025-1108
SRC-026 | ◈ | fam:A | https://www.francemarches.com/files/BOAMP/25-65097.html
SRC-027 | ◈ | fam:A | https://www.fntp.fr/rep-pmcb-ou-en-est-on/
SRC-028 | ◈ | fam:A | https://grandlyon-passdecheterie.horanet.com/faq

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.cnil.fr/fr/les-dispositifs-de-lecture-automatisee-de-plaque-dimmatriculation-lapi | A,D | 2025-06-05 | CNIL LAPI retention rules | CNIL doctrine: LAPI data without a positive match are kept max 15 days from collection (CSI L.233-2); matched data 1 month; ACVR road-rule LAPI data are deleted once the vehicle is compliant, else max 8 working days. ALPR at decheteries must follow the same pattern. | b79bab08-7fe7-4e9a-90ae-e3bade6d06b9
FCT-002 | FACT | ✧ | https://www.cnil.fr/fr/acces-locaux-controle-des-horaires-au-travail | A | 2026-06-17 | CNIL badge access-log retention | CNIL workplace-access doctrine: access-journalisation data should be deleted 3 months after recording; identification data kept while the habilitation is active, up to 5 years intermediate archive when used for time tracking. | 77d43da6-4a74-4de0-86fc-d0ee850f9a88
FCT-003 | FACT | ✧ | https://grandlyon-passdecheterie.horanet.com/faq | A | 2026-08-31 | Lyon Pass Decheterie quota legal framing | Metropole de Lyon FAQ grounds its vehicle-category quotas in the dechets assimiles regime (CGCT L2224-14): PTAC<=2t vans free but 4 visits/month; PTAC>2t paid, 4 visits/month, 10 purchases/month, 50/year per usager; >3.5t banned. Quotas are justified as limiting the service to household-comparable waste financed by TEOM. | 271c59b2-e9f9-4aad-96a5-7e4e2d05d365
FCT-004 | FACT | ✧ | https://www.francemarches.com/files/BOAMP/25-65097.html | A | 2025-06-11 | Rennes decheterie exploitation contract procedure | BOAMP avis 25-65097 (11/06/2025): Rennes Metropole 'Exploitation du reseau des decheteries et plateformes de vegetaux' was published as a formal attributed contract (identifiant 2025-2520158), contradicting the SITREVA 'negotiated without publicity' concern for the current-generation contract. | c58bae38-771e-4e67-8ff0-63ae2830620e
FCT-005 | FACT | ✧ | https://www.fntp.fr/rep-pmcb-ou-en-est-on/ | A | 2026-07-02 | PMCB refondation calendar | FNTP (02/07/2026): PMCB refondation decrees/arretes in finalisation, publication expected end of August 2026, first effect 01/09/2026; new eco-org agrements 01/01/2027; matures leave free take-back 01/01/2027; FNTP CE recours claims 34 M€ undue 2024 ecocontributions; some suppliers already raising ecocontributions pre-refondation for treasury. | 93ad2b50-9efa-410a-89cf-ae9c28df0f65
FCT-006 | FACT | ✧ | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | A | 2026-05-20 | ADEME wild-dumping study status | ADEME national wild-dumping study launched 20/05/2026 with Ecogeos + Rudologia; collectivites invited to respond (prefecture Eure 06/07/2026); results not yet published as of 31/08/2026 — the article's causal chain (access control -> wild dumping) must cite it as pending. | d6d34d94-24f1-4d0c-9685-55e76cb974b7
FCT-007 | FACT | ✧ | https://www.senat.fr/rap/l24-367/l24-367_mono.html | A | 2026-08-31 | PPL fire-risk fund status | Senat PPL (rapport l24-367) creating a compensation fund for waste-treatment fire damage from lithium battery ignition was adopted by the Senat in first reading (06/03/2026 seance); text still in parliamentary navette as of 31/08/2026, no enacted fund. | de4cf438-0165-42cd-8c53-43f70976477c
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-017,SRC-020
FCT-002 | SRC-018,SRC-019
FCT-003 | SRC-028
FCT-004 | SRC-026
FCT-005 | SRC-027
FCT-006 | SRC-022,SRC-023
FCT-007 | SRC-024

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-022 | NONE
FCT-002 | QRY-023 | NONE
FCT-003 | QRY-015 | NONE
FCT-004 | QRY-016 | NONE
FCT-005 | QRY-024 | NONE
FCT-006 | QRY-025 | NONE
FCT-007 | QRY-026 | NONE

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
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T05:58:31.163996+00:00","fact_mem":{"FCT-001":"b79bab08-7fe7-4e9a-90ae-e3bade6d06b9","FCT-002":"77d43da6-4a74-4de0-86fc-d0ee850f9a88","FCT-003":"271c59b2-e9f9-4aad-96a5-7e4e2d05d365","FCT-004":"c58bae38-771e-4e67-8ff0-63ae2830620e","FCT-005":"93ad2b50-9efa-410a-89cf-ae9c28df0f65","FCT-006":"d6d34d94-24f1-4d0c-9685-55e76cb974b7","FCT-007":"de4cf438-0165-42cd-8c53-43f70976477c"},"mnemo_row":"PENDING_PRE_GATE","result":"PARTIAL","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}
ATTEMPT-002 | {"created_at":"2026-08-31T05:58:56.676352+00:00","fact_mem":{"FCT-001":"b79bab08-7fe7-4e9a-90ae-e3bade6d06b9","FCT-002":"77d43da6-4a74-4de0-86fc-d0ee850f9a88","FCT-003":"271c59b2-e9f9-4aad-96a5-7e4e2d05d365","FCT-004":"c58bae38-771e-4e67-8ff0-63ae2830620e","FCT-005":"93ad2b50-9efa-410a-89cf-ae9c28df0f65","FCT-006":"d6d34d94-24f1-4d0c-9685-55e76cb974b7","FCT-007":"de4cf438-0165-42cd-8c53-43f70976477c"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
