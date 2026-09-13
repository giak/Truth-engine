ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-1330-infiltration-medias-politiques-france-ue | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_infiltration-medias-politiques-france-ue/2026-09-05_13-30_infiltration-medias-politiques-france-ue_INPUT.txt | SUBJECT_SLUG:infiltration-medias-politiques-france-ue | SUBJECT_FP:sha256:724d3759ac70ce73e882cb5b0666d94f4ad05a58b9c57ed6cc006c621545ec75 | INPUT_SHA256:sha256:f6cb3073770a6c18f211853d7b23c998b7c710e930ae979536d4dc6f243e0ab3
COMPLEXITY:16→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France et UE: infiltration des medias et de la sphere politique (cellules d influence etatiques, faux dissidents, think tanks, nominations audiovisuel public, ELNET/Israel, Twitter Files France, revolving doors, lobbies); focus sur les faits documentes vs accusations
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/EPISTEMIC.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAGMENTATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INFILTRATION DES MÉDIAS ET DE LA SPHÈRE POLITIQUE (FRANCE/UE)

## Objet
Enquête sur les canaux documentés par lesquels l'État français et des acteurs étrangers exercent une influence/infiltration sur les médias et la sphère politique en France et dans l'UE, et sur ce qui relève de l'accusation non prouvée.

## Faits établis (tiers et sources)

**1. Le Quai d'Orsay briefe un réseau d'influenceurs (CONFIRME, ✦, FCT-001).** Selon l'enquête de franceinfo (18 juin 2026, SRC-001), le ministère des Affaires étrangères s'appuie sur un réseau de comptes influents sur X (dont Louis Duclos, ~74 000 abonnés) pour diffuser la position officielle de la France contre les ingérences. Une source diplomatique confirme les briefings ; le ministère affirme qu'il n'y a « ni recrutement, ni contrat », pas de rémunération et pas de « réseau occulte ». Le corpus publié (post #110, 26 nov. 2025, SRC-008) cite Intelligence Online (31 juillet 2025) : Duclos « collabore avec la cellule depuis plus d'un an » et reçoit des documents sensibles avant publication officielle (18e paquet de sanctions). Contre-argument enregistré (réfutation FCT-001) : le Quai conteste la qualification, pas les briefings.

**2. ELNET, lobby pro-israélien, a financé 101 voyages parlementaires (CONFIRME, ✦, FCT-002).** Entre 2017 et 2024, ELNET a financé 101 voyages de parlementaires français (99 en Israël, 2 en Allemagne), selon Mediapart (relayé par Wikipédia SRC-002 et Blast SRC-004). Le cabinet de Benyamin Netanyahou a versé 37 664 € (139 454 shekels) à ELNET en 2020. L'association ne s'est enregistrée comme représentant d'intérêts (HATVP) qu'en novembre 2024, huit ans après l'obligation de la loi Sapin 2 (2016). La proposition de résolution n° 1000 (commission d'enquête sur ELNET, 19 fév. 2025) n'a jamais été examinée. Contre-argument enregistré (réfutation FCT-002) : ELNET se dit « organisation non partisane », l'HATVP a ouvert en 2026 un répertoire des activités d'influence étrangère (instruction en cours).

**3. Twitter Files France : une « censure par procuration » alléguée (VERIFIÉ, ✦, FCT-003).** Le 3 septembre 2025, Pascal Clérotte et Thomas Fazi (Civilization Works, 57 pages, SRC-005) publient des documents internes de X montrant une coordination entre Emmanuel Macron, des législateurs et des ONG (SOS Racisme, UEJF) pour pousser la plateforme à censurer des contenus légaux. Le rapport Atlantico (Épelboin, SRC-003) et le corpus (SRC-009) décrivent un « complexe industriel de censure ». Fiabilité contestée : la publication émane d'un canal proche de Musk, sans vérification indépendante (NPR 2022, The Atlantic, CNN, Le Monde) — d'où le tiers VERIFIÉ et non CONFIRME (contre-argument enregistré, réfutation FCT-003).

**4. Think tanks : un entre-soi public-privé documenté (CONFIRME, ✦, FCT-004).** L'Observatoire des multinationales (SRC-007) documente : Institut Jacques Delors financé 562 136 € par la Commission européenne (2021), EuropaNova 50 000 € du Premier ministre (2020), Fondation Robert Schuman 615 000 € de l'État (2020) ; Pascal Lamy, président émérite de l'Institut Delors, est lobbyiste en chef chez Brunswick (clients dont Nord Stream 2). Le corpus (SRC-010) relève les liens Terra Nova→macronisme et Fondation Jean-Jaurès→PS. Contre-argument enregistré (réfutation FCT-004) : littérature nuancée (Fondapol : think tanks français trop faibles), sans contradiction des montants.

**5. Commission d'enquête sur l'audiovisuel public (✧, FCT-005, documenté).** Lancée à l'initiative d'Éric Ciotti (nov. 2025–avril 2026), présidée par Jérémie Patrier-Leitus, rapporteur Charles Alloncle, elle a auditionné l'ensemble de l'audiovisuel public (Ernotte, Niel, Lucet, Salamé…) avec tensions (affaire Mediawan, « cirque » selon Niel) et un risque de non-publication du rapport voté le 27 avril 2026 (LCP, 9 avril 2026, SRC-006).

**6. ELNET au Sénat (✧, FCT-006).** Le Sénat a hébergé le 10 novembre 2025 un sommet financé par ELNET (189 000 € déboursés), en contradiction avec le code de conduite du Sénat (Wikipédia/Mediapart, SRC-002).

**7. Résolution n° 1000 jamais examinée (✧, FCT-007).** La proposition de commission d'enquête sur les ingérences d'ELNET France (19 fév. 2025) n'a jamais été mise à l'ordre du jour (corpus SRC-009).

## Réfutations
Quatre contre-requêtes exécutées sur les faits ✦ (FCT-001 à 004) : défenses ministérielles, enregistrements HATVP et répertoire 2026, critique de fiabilité des Twitter Files, littérature académique nuancée sur les think tanks. Statut : FOUND_RESOLVED — aucune contradiction matérielle, plusieurs limites de preuve enregistrées.

## Analyse causale
L'influence se diffuse par des canaux multiples et largement non coordonnés : briefings informels (État), voyages tout frais payés (ELNET), documents contestés (Twitter Files), financement public-privé (think tanks). Aucun de ces canaux ne démontre un impact électoral direct ; aucun scrutin FR/UE n'a été annulé ou inversé par ces mécanismes. L'asymétrie institutionnelle est frappante : VIGINUM documente abondamment les ingérences russes mais ne nomme jamais les alliés (Israël, EAU, Qatar) — point approfondi dans le run dédié.

## Verdict
L'infiltration/influence des médias et de la sphère politique française et européenne est réelle et documentée par des faits précis (briefings d'État vers des influenceurs, lobbying par voyages, coordination de modération alléguée, financement des think tanks). En revanche, l'accusation d'un contrôle global, coordonné et invisible n'est pas établie : chaque canal documenté fait l'objet de défenses et de limites de preuve, et la transparence réglementaire (HATVP, répertoire des influences étrangères) est en construction. « Où sont les preuves ? » : elles sont publiques, inspectables, et pour partie contestées — c'est précisément leur statut probatoire qui doit rester au premier plan.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:4|AXS:4|CAU:3|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Cellule d influence du Quai d Orsay et faux dissidents (Louis Duclos, Intelligence Online juillet 2025)","type":"LEAD"}
LED-002 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Twitter Files France: censure orchestree par l Etat via ONG et plateformes (sept. 2025)","type":"LEAD"}
LED-003 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"Think tanks et revolving doors politiques (Terra Nova, Fondation Jean-Jaures, Institut Thomas More)","type":"LEAD"}
LED-004 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"ELNET: voyages parlementaires en Israel sans enregistrement HATVP (101 voyages 2017-2024)","type":"LEAD"}
LED-005 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"Audiovisuel public et ARCOM: nominations, politisation, orientation editoriale","type":"LEAD"}

### CLAIM_REGISTRY_V1
CLM-001 | {"kind":"CLM","status":"SUPPORTED","subject":"Une cellule d influence du ministere des Affaires etrangeres a collabore avec des influenceurs francais (Duclos) - documente par Intelligence Online","type":"CLAIM"}
CLM-002 | {"kind":"CLM","status":"SUPPORTED","subject":"L Etat a orchestre une censure coordonnee des reseaux sociaux via des ONG (Twitter Files France) - accusation documentee et contestee","type":"CLAIM"}
CLM-003 | {"kind":"CLM","status":"SUPPORTED","subject":"Des think tanks francais entretiennent des liens organiques avec des partis politiques (Terra Nova, Fondation Jean-Jaures) - documente","type":"CLAIM"}
CLM-004 | {"kind":"CLM","status":"SUPPORTED","subject":"ELNET a finance des voyages parlementaires en Israel sans enregistrement HATVP (101 voyages 2017-2024) - documente","type":"CLAIM"}

### AXIS_REGISTRY_V1
AXS-001 | {"kind":"AXS","status":"SATURATED","subject":"Des faits documentes etablissent une infiltration/influence des medias par des acteurs etatiques francais (Twitter Files France, cellule Quai d Orsay)","type":"POSITION"}
AXS-002 | {"kind":"AXS","status":"SATURATED","subject":"Les think tanks francais sont lies aux partis politiques sans preuve de controle direct","type":"POSITION"}
AXS-003 | {"kind":"AXS","status":"SATURATED","subject":"ELNET exerce un lobbying etranger documente aupres des parlementaires francais","type":"POSITION"}
AXS-004 | {"kind":"AXS","status":"SATURATED","subject":"La politisation des nominations dans l audiovisuel public est documentee, pas une infiltration etrangere","type":"POSITION"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"fact_refs":["FCT-001","FCT-002","FCT-003"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: l influence sur les medias/politiques passe par des canaux documentes (briefings Etat vers influenceurs, lobbying de voyages ELNET, coordination censure) dont l impact electoral direct reste non mesure; aucun scrutin annule","type":"CAUSALITY"}
CAU-002 | {"fact_refs":["FCT-004"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: le financement public-prive des think tanks cree une dependance structurelle a l egard des decideurs et entreprises, reduisant la capacite de critique independante (entre-soi documente)","type":"CAUSALITY"}
CAU-003 | {"fact_refs":["FCT-005"],"kind":"CAU","object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: la politisation des nominations audiovisuel public est contestee parlementairement (commission d enquete) mais sans preuve de controle editorial direct etablie","type":"CAUSALITY"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"kind":"CTRL","object_question_ref":"OQ","status":"DONE","text":"CTRL: 10 sources inspectees (6 familles: A,B,C,E,other:observatoire-multinationales,other:substack-giak), refutations executees sur FCT-001..004 (FOUND_RESOLVED), aucune contradiction materielle","type":"CONTROL"}

### ACTION_REGISTRY_V1
ACT-001 | {"kind":"ACT","object_question_ref":"OQ","status":"DONE","text":"ACT: recommandations - rendre publics les briefings Etat-influenceurs (registre), appliquer Sapin 2/HATVP a ELNET et publier l instruction du repertoire influence etrangere, verifier independamment les Twitter Files, encadrer le financement public des think tanks","type":"ACTION"}

SEARCH_ACTIVITY_V1:WEB:11|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | PASS | mnemolite | search:infiltration-medias-politiques | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PARTIAL | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-005 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | https://www.atlantico.fr/article/decryptage/ce-que-les-nouveaux-twitter-files-revelent-sur-les-sombres-manoeuvres-de-la-france-pour-restreindre-la-liberte-d-expression-sur-internet | Twitter Files France censure coordonnee Etat ONG plateformes reseaux sociaux documents 2025 revelations
QRY-002 | WEB | PASS | - | https://www.franceinfo.fr/internet/reseaux-sociaux/autour-du-quai-d-orsay-une-galaxie-d-influenceurs-pour-combattre-les-attaques-contre-la-france-sur-les-reseaux-sociaux_8046578.html | Louis Duclos Intelligence Online Quai d Orsay cellule influence veille strategie collaboration documents avant publication
QRY-003 | WEB | PASS | - | https://www.lepoint.fr/politique/comment-les-think-tanks-s-imposent-dans-le-debat-politique-25-12-2022-2502843_20.php | think tanks francais financement influence politique Terra Nova Fondation Jean-Jaures Institut Thomas More liens partis enquete
QRY-004 | WEB | PASS | - | https://www.publicsenat.fr/actualites/politique/elnet-un-reseau-de-lobbying-pro-israelien-au-coeur-du-debat-sur-les-voyages-des-parlementaires | ELNET voyages parlementaires francais Israel HATVP enregistrement retard 101 voyages 2017 2024 financement bureau Netanyahu
QRY-005 | WEB | PASS | - | https://www.mediapart.fr/journal/politique/291224/elnet-un-agent-d-influence-pro-israel-au-coeur-du-parlement | ELNET reseau lobbying pro-israelien voyages parlementaires francais Assemblee nationale enquete Mediapart
QRY-006 | WEB | PASS | - | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L17B2698-t1.html | audiovisuel public France nominations ARCOM politisation presidence France Televisions 2024 2025 critique
QRY-007 | WEB | PASS | - | https://www.vie-publique.fr/rapport/301522-viginum-protection-contre-les-ingerences-numeriques-etrangeres-2024 | VIGINUM VIGISCORE methode critique asymetrie attribution ingerences allies jamais nommes rapport 2025
QRY-008 | FETCH | INSPECTED | SRC-001 | https://www.franceinfo.fr/internet/reseaux-sociaux/autour-du-quai-d-orsay-une-galaxie-d-influenceurs-pour-combattre-les-attaques-contre-la-france-sur-les-reseaux-sociaux_8046578.html | -
QRY-009 | FETCH | INSPECTED | SRC-002 | https://fr.wikipedia.org/wiki/ELNET_(organisation) | -
QRY-010 | FETCH | INSPECTED | SRC-003 | https://atlantico.fr/article/decryptage/ce-que-les-nouveaux-twitter-files-revelent-sur-les-sombres-manoeuvres-de-la-france-pour-restreindre-la-liberte-d-expression-sur-internet | -
QRY-011 | FETCH | INSPECTED | SRC-004 | https://www.blast-info.fr/articles/2025/elnet-le-reseau-dinfluence-au-service-disrael-et-de-netanyahu-qirou80iQxObxdwjyAzd7g | -
QRY-012 | FETCH | INSPECTED | SRC-005 | https://www.public.news/p/twitter-files-france | -
QRY-013 | FETCH | INSPECTED | SRC-006 | https://lcp.fr/actualites/audiovisuel-public-et-maintenant-apres-la-fin-des-auditions-la-suite-du-processus-de-la | -
QRY-014 | FETCH | INSPECTED | SRC-007 | https://multinationales.org/fr/enquetes/think-tanks-laboratoires-d-influence/les-think-tanks-francais-et-l-europe-un-partenariat-public-prive-loin-des | -
QRY-015 | FETCH | INSPECTED | SRC-008 | https://giak.substack.com/p/qui-est-vraiment-louis-duclos | -
QRY-016 | FETCH | INSPECTED | SRC-009 | https://giak.substack.com/p/la-democratie-en-cage | -
QRY-017 | FETCH | INSPECTED | SRC-010 | https://giak.substack.com/p/opposition-controlee-anatomie-dun | -
QRY-018 | WEB | PASS | - | - | REFUTATION Quai d Orsay influenceurs Duclos 74 000 abonnes: defense ministere 'ni recrutement ni contrat', pas de reseau occulte, briefings = marche normale communication; aucun contre-fait materiel trouve
QRY-019 | WEB | PASS | - | - | REFUTATION ELNET 101 voyages 2017 2024 (99 Israel, 2 Allemagne) 37 664 EUR 2020 HATVP 8 ans novembre 2024: defense 'organisation non partisane', voyages declares, repertoire influence etrangere HATVP en instruction fev 2026; aucun contre-fait sur les faits documentes
QRY-020 | WEB | PASS | - | - | REFUTATION Twitter Files France 2025 rapport 57 pages: fiabilite contestee (NPR 2022, The Atlantic 'bait', CNN avocats Twitter refutent Musk, Le Monde 'censurement compromettantes'); publications partisan context, verification independante absente
QRY-021 | WEB | PASS | - | - | REFUTATION think tanks francais entre-soi public prive: litterature nuancee (Fondapol 2022: think tanks trop faibles/finances; Montbrial: 'import/export intellectuel'); pas de contradiction des montants documentes 562 136 EUR 2021, 50 000 EUR 2020, 615 000 EUR 2020, Nord Stream 2

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.franceinfo.fr/internet/reseaux-sociaux/autour-du-quai-d-orsay-une-galaxie-d-influenceurs-pour-combattre-les-attaques-contre-la-france-sur-les-reseaux-sociaux_8046578.html
SRC-002 | ◈ | fam:C | https://fr.wikipedia.org/wiki/ELNET_(organisation)
SRC-003 | ◈ | fam:B | https://atlantico.fr/article/decryptage/ce-que-les-nouveaux-twitter-files-revelent-sur-les-sombres-manoeuvres-de-la-france-pour-restreindre-la-liberte-d-expression-sur-internet
SRC-004 | ◈ | fam:B | https://www.blast-info.fr/articles/2025/elnet-le-reseau-dinfluence-au-service-disrael-et-de-netanyahu-qirou80iQxObxdwjyAzd7g
SRC-005 | ◈ | fam:E | https://www.public.news/p/twitter-files-france
SRC-006 | ◈ | fam:A | https://lcp.fr/actualites/audiovisuel-public-et-maintenant-apres-la-fin-des-auditions-la-suite-du-processus-de-la
SRC-007 | ◈ | fam:other:observatoire-multinationales | https://multinationales.org/fr/enquetes/think-tanks-laboratoires-d-influence/les-think-tanks-francais-et-l-europe-un-partenariat-public-prive-loin-des
SRC-008 | ◈ | fam:other:substack-giak | https://giak.substack.com/p/qui-est-vraiment-louis-duclos
SRC-009 | ◈ | fam:other:substack-giak | https://giak.substack.com/p/la-democratie-en-cage
SRC-010 | ◈ | fam:other:substack-giak | https://giak.substack.com/p/opposition-controlee-anatomie-dun

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.franceinfo.fr/internet/reseaux-sociaux/autour-du-quai-d-orsay-une-galaxie-d-influenceurs-pour-combattre-les-attaques-contre-la-france-sur-les-reseaux-sociaux_8046578.html | A,other:substack-giak | 2026-09-05 | Le ministere des Affaires etrangeres briefe un reseau d analystes-influenceurs sur X (dont Louis Duclos, ~74 000 abonnes) pour diffuser la position officielle de la France; non remuneres, sans contrat, source diplomatique confirme les briefings | CONFIRME | 7d1bc1cb-800b-49be-8e21-1cc89cfc625e
FCT-002 | FACT | ✦ | https://fr.wikipedia.org/wiki/ELNET_(organisation) | B,C | 2026-09-05 | ELNET, lobby pro-israelien, a finance 101 voyages de parlementaires francais 2017-2024 (99 Israel, 2 Allemagne), recu 37 664 EUR du cabinet Netanyahu en 2020, et ne s est enregistre comme representant d interets (HATVP) qu en novembre 2024, 8 ans apres l obligation Sapin 2 | CONFIRME | 0e8face1-88a9-4b81-a560-54374900dbf4
FCT-003 | FACT | ✦ | https://www.public.news/p/twitter-files-france | B,E | 2026-09-05 | Twitter Files France (sept. 2025, Clerotte/Fazi, rapport 57 p.): documents X montrant une coordination Macron/legislateurs/ONG (SOS Racisme, UEJF) pour pousser la plateforme a censurer et modele de censorship-by-proxy; publications contestees car non verifiees independamment | VERIFIE | eff93e59-e78c-4406-bc90-f09ecdcd724f
FCT-004 | FACT | ✦ | https://multinationales.org/fr/enquetes/think-tanks-laboratoires-d-influence/les-think-tanks-francais-et-l-europe-un-partenariat-public-prive-loin-des | other:observatoire-multinationales,other:substack-giak | 2026-09-05 | Les think tanks francais entretiennent un entre-soi public-prive documente: Institut Jacques Delors finance 562 136 EUR par la Commission (2021), EuropaNova 50 000 EUR du PM (2020), Fondation Robert Schuman 615 000 EUR de l Etat (2020), Pascal Lamy lobbyiste Brunswick (Nord Stream 2) president emerite de l Institut Delors | CONFIRME | cdd09667-08af-4a80-8987-91d3f0037f50
FCT-005 | FACT | ✧ | https://lcp.fr/actualites/audiovisuel-public-et-maintenant-apres-la-fin-des-auditions-la-suite-du-processus-de-la | A | 2026-09-05 | Une commission d enquete de l Assemblee nationale sur la neutralite, le fonctionnement et le financement de l audiovisuel public (initiative Ciotti, pres. Patrier-Leitus, rapp. Alloncle) a auditionne de nov. 2025 a avril 2026, avec tensions (Mediawan, Niel) et risque de non-publication du rapport | VERIFIE | 4b302248-ebec-44bd-9822-1142d694cc60
FCT-006 | FACT | ✧ | https://fr.wikipedia.org/wiki/ELNET_(organisation) | C | 2026-09-05 | Le Senat a accueilli le 10 nov. 2025 un sommet finance par ELNET (189 000 EUR debourses), contrairement au code de conduite du Senat interdisant les colloques avec participation financiere des intervenants | VERIFIE | 5bda5944-f24a-4f54-be7e-bf4776a5ef31
FCT-007 | FACT | ✧ | https://giak.substack.com/p/la-democratie-en-cage | other:substack-giak | 2026-09-05 | La proposition de resolution n 1000 (19 fev. 2025) creant une commission d enquete sur les ingerences politiques d ELNET France n a jamais ete examinee par l Assemblee nationale | VERIFIE | 1bdfb8d0-ff04-49d1-8e89-b7eac6c895a0
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-008
FCT-002 | SRC-002,SRC-004
FCT-003 | SRC-005,SRC-003
FCT-004 | SRC-007,SRC-010
FCT-005 | SRC-006
FCT-006 | SRC-002
FCT-007 | SRC-009

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-018 | FOUND_RESOLVED
FCT-002 | QRY-019 | FOUND_RESOLVED
FCT-003 | QRY-020 | FOUND_RESOLVED
FCT-004 | QRY-021 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:LEADS | NEXT_ACTION:SEARCH_DISCOVERY
CP-002 | SCOPE | PASS | LAST_COMPLETED:SCOPE | NEXT_ACTION:SEARCH_DISCOVERY
CP-003 | SEARCH | PASS | LAST_COMPLETED:SEARCH | NEXT_ACTION:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:FACTS | NEXT_ACTION:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:CAUSAL | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:VERIFY | NEXT_ACTION:FINALIZATION
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T11:43:38.805950+00:00","fact_mem":{"FCT-001":"7d1bc1cb-800b-49be-8e21-1cc89cfc625e","FCT-002":"0e8face1-88a9-4b81-a560-54374900dbf4","FCT-003":"eff93e59-e78c-4406-bc90-f09ecdcd724f","FCT-004":"cdd09667-08af-4a80-8987-91d3f0037f50","FCT-005":"4b302248-ebec-44bd-9822-1142d694cc60","FCT-006":"5bda5944-f24a-4f54-be7e-bf4776a5ef31","FCT-007":"1bdfb8d0-ff04-49d1-8e89-b7eac6c895a0"},"mnemo_row":"MNEMO_S 19e1adb3-c3e5-438a-b84b-4929d73be69f","result":"PARTIAL","writeback_execution":[],"writeback_row":"PENDING_PRE_GATE"}
ATTEMPT-002 | {"created_at":"2026-09-05T11:44:26.742000+00:00","fact_mem":{"FCT-001":"7d1bc1cb-800b-49be-8e21-1cc89cfc625e","FCT-002":"0e8face1-88a9-4b81-a560-54374900dbf4","FCT-003":"eff93e59-e78c-4406-bc90-f09ecdcd724f","FCT-004":"cdd09667-08af-4a80-8987-91d3f0037f50","FCT-005":"4b302248-ebec-44bd-9822-1142d694cc60","FCT-006":"5bda5944-f24a-4f54-be7e-bf4776a5ef31","FCT-007":"1bdfb8d0-ff04-49d1-8e89-b7eac6c895a0"},"mnemo_row":"MNEMO_S 19e1adb3-c3e5-438a-b84b-4929d73be69f","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"writeback MnemoLite","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_S 19e1adb3-c3e5-438a-b84b-4929d73be69f | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
