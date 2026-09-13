ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-1442-filiere-antidrones-europe-qui-vend-qui-gagne | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_filiere-antidrones-europe-qui-vend-qui-gagne/2026-09-05_14-42_filiere-antidrones-europe-qui-vend-qui-gagne_INPUT.txt | SUBJECT_SLUG:filiere-antidrones-europe-qui-vend-qui-gagne | SUBJECT_FP:sha256:aa25c50098a1b60f55b148bb5451497cfc839b80b9ebe4ab7394841d08df14a4 | INPUT_SHA256:sha256:c2e64c5bbdba676214e63ca5e5ae2ed47f42394b48720b30de3ba038d8fa7b9a
COMPLEXITY:16→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Examen ADVERSARIAL de la filiere anti-drones (C-UAS) en Europe 2025-2026: QUI VEND, QUI GAGNE. Distinguer (a) cas BELGE panique 2025 sans preuve -> 50 M EUR sans appel d'offres (Senhive 10,4 M EUR 84 antennes RF; Cobbs/Origin Robotics 300 BLAZE 7,8 M EUR; avis defavorable Inspection Finances octobre 2025; enquete parquet Bruxelles 17/04/2026); (b) marche FRANCE structurel post-Orly 2016 (Hologarde 2017, Thales, appels d'offres, 2000+ incidents/an; France 4e operateur BLAZE via DSV juin 2026); (c) marche UE C-UAS croissant (rapports marche 1,2->4,2 Md USD 2025-2030; plan action Commission 11/02/2026); (d) effet reel: 558 signalements BE 0 preuve, Leipzig 04/08/2026 = preuve materielle.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/EPISTEMIC.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,tools/MACROS.md,definitions/CONTROLS.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Run 18 — Filière anti-drones Europe : qui vend, qui gagne ?

**Run KERNEL (APEX, RENARD CORE V3, charge inversée).** Examen adversarial de la filière C-UAS (counter-drone) européenne : les vagues de signalements de drones (dont la vague 2025 sans preuve, Run 17) alimentent-elles un marché anti-drones — et qui en profite ?

## Verdicts (6 faits ✦ CONFIRME, 2 familles indépendantes + réfutation chacun)

1. **Procédure Belgique (FCT-001).** Le plan anti-drones de 50 M EUR a été lancé en urgence **SANS appel d'offres** malgré l'avis **DÉFAVORABLE** de l'Inspection des Finances (10/2025), qui avertissait d'une contradiction avec la loi sur les marchés publics et d'un risque de prix élevés. La commission Armée a approuvé (1 abstention sur 11) ; le parquet de Bruxelles a ouvert une enquête le 17/04/2026 (corruption, obstruction d'enchères publiques). **Réfutation intégrée :** la procédure d'urgence était légale (loi respectée), le budget était déjà approuvé depuis 5 mois, l'avis de l'Inspection est consultatif.

2. **Prix Senhive (FCT-002).** 84 antennes RF SENID payées 10,4 M EUR (~84.000 EUR/antenne) ; l'étude marché de Pano les trouve à ~1/4 du prix. **LITIGE (CAU-002 GAP-DISPUTED) :** Senhive répond que la Défense a acheté le **SENIDPRO** (version militaire pro, double bande passante, AoA/TDOA, clients défense avant 11/2025, prix déjà pratiqué) et que comparer un prix par antenne en configuration de base est incorrect ; la Défense invoque la version SEN PRO du projet **CAMO** belgo-français, prix vérifié via le pays partenaire.

3. **Prix BLAZE (FCT-003).** 300 drones kamikazes lettons BLAZE (Origin Robotics) achetés 7,8 M EUR via l'intermédiaire belge Cobbs ; l'expert (ex-colonel Housen) et le producteur estiment chaque drone à ~6.000 EUR, soit un surcoût allégué de plusieurs millions. **Réfutation intégrée :** la Défense a contrôlé le prix fin 2025 (support Ukraine) et le prix unitaire de 26.000 EUR inclut consoles, munitions, formation et système de commandement — package complet, non comparable à un prix « drone seul ».

4. **La menace qui justifie l'achat (FCT-004).** 558 signalements (09/2025–01/2026) présentés par Francken comme une « crise militaire » de guerre hybride russe ; la contre-enquête Pano (15/04/2026) n'a trouvé **AUCUNE preuve** de drones hostiles d'État — le « gros drone » de Zaventem était un hélicoptère de police. La Défense maintient l'hypothèse russe « la plus plausible » (Euroclear, Kleine-Brogel) **sans preuve formelle**.

5. **Contraste France (FCT-005).** La France montre qu'une filière C-UAS peut être structurelle et procédurale : Hologarde (ADP/Thales/DSNA) créée en 2017 après un incident réel (Orly 2016), marchés avec appels d'offres, milliers d'incidents/an mesurés ; la France sélectionne BLAZE/DSV en 06/2026 après **évaluation competitive** (4e opérateur européen). **Réfutation intégrée :** la France a aussi accéléré et industrialisé (plan 350 M EUR dès 2022, déploiement JO 2024 de 42 M EUR), et Hologarde dépend d'un opérateur privé (ADP) ayant un intérêt commercial direct.

6. **Qui vend, qui gagne (FCT-006).** Senhive (startup de Hasselt fondée en 2019, sans lien politique documenté) reçoit 10,4 M EUR publics ; Origin Robotics (Riga) étend BLAZE à 4 pays européens via des intermédiaires (Cobbs en BE, DSV en FR) ; le marché UE C-UAS croît de ~1,2 Md USD (2025) à ~4,2 Md (2030, 27,5 % CAGR) pour des causes à la fois matérielles (Ukraine, Leipzig 2026) et liées au cas belge. **GAP (CAU-003) :** la part de la croissance attribuable aux vagues de signalements non confirmés n'est pas quantifiable.

## L'asymétrie documentée

Le cas belge est le seul où la chaîne **panique → dépense** est démontrée par une contre-enquête indépendante : amplification d'une menace sans preuve, fuite d'une vidéo trompeuse, avis technique écarté, 50 M EUR sans appel d'offres, enquête judiciaire ouverte. La France est le contre-exemple procédural. La menace réelle existe ailleurs (Leipzig 04/08/2026 : drone avec explosif) — le discriminateur entre les deux régimes n'est pas la menace mais **la procédure** (appel d'offres + évaluation vs urgence sans appel d'offres).

## Limites d'évidence (GAP typés)

- **CAU-002 (DISPUTED) :** l'écart de prix x4 est contesté par les vendeurs (version pro / package) — litige non tranché publiquement ; l'enquête parquet et l'audit interne sont en cours.
- **CAU-003 (CORRELATION_VS_CAUSATION) :** impossible de quantifier la part de la croissance du marché C-UAS UE attribuable aux vagues de signalements vs aux menaces matérielles.
- **CAU-005 (INTENT) :** aucun lien politique direct entre vendeurs et décideurs n'est documenté ; l'enquête doit trancher entre corruption, conflit d'intérêts et procédure d'urgence maladroite.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:6|CLM:2|AXS:3|CAU:5|CTRL:3|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"priority":"HIGH","status":"SATURATED","subject":"Achats C-UAS Belgique 2025-2026 sans appel d'offres: Senhive 10,4 M EUR (84 antennes RF) + Cobbs 300 BLAZE 7,8 M EUR - prix vs marche (Pano: ~1/4 pour Senhive; ~6.000 EUR/unite BLAZE soit ~1,8 M EUR)","type":"LEAD"}
LED-002 | {"priority":"HIGH","status":"SATURATED","subject":"Enquete judiciaire: parquet de Bruxelles ouvre enquete 17/04/2026 (corruption, obstruction encheres publiques) suite reportage Pano; avis defavorable Inspection des Finances oct 2025 outre","type":"LEAD"}
LED-003 | {"priority":"HIGH","status":"SATURATED","subject":"Contre-enquete Pano VRT 15/04/2026: 0 preuve de drones hostiles sur vague 2025 BE (558 signalements 09/2025-01/2026); 'gros drone' Zaventem = helicoptere police","type":"LEAD"}
LED-004 | {"priority":"MEDIUM","status":"SATURATED","subject":"Marche FRANCE: structurel depuis Orly 2016 (Hologarde 2017 + Thales + appels d'offres, 2000+ incidents/an) CONTRASTE procedures BE; France 4e operateur BLAZE via DSV 06/2026","type":"LEAD"}
LED-005 | {"priority":"MEDIUM","status":"SATURATED","subject":"Qui vend: Senhive (Hasselt 2019, Petracca/Paesen/Burm, CEO Krekels, startup seed), Origin Robotics (Riga, fabricant BLAZE), Cobbs (Bonheiden, intermediaire, CEO Rummens), DSV (FR), Hologarde (ADP/Thales)","type":"LEAD"}
LED-006 | {"priority":"MEDIUM","status":"SATURATED","subject":"Marche UE C-UAS croissant (rapports: 1,2 -> 4,2 Md USD 2025-2030 UE 27,5% CAGR); plan action Commission 11/02/2026; reponse Defense a Pano: SENIDPRO version pro (CAMO FR-BE) prix verifie, BLAZE inclut consoles+munitions+formation","type":"LEAD"}

### CLAIM_REGISTRY_V1
CLM-001 | {"status":"SUPPORTED","subject":"Les vagues de signalements de drones (BE 2025: 558 signalements, 0 preuve) ont ete utilisees pour accelerer des achats anti-drones a prix gonfles (50 M EUR sans appel d'offres)","type":"CLAIM"}
CLM-002 | {"status":"SUPPORTED","subject":"Le marche europeen C-UAS est en croissance structurelle (1,2 -> 4,2 Md USD UE 2025-2030) ET beneficie de l'amplification des menaces: la filiere qui vend est aussi celle qui mesure la menace","type":"CLAIM"}

### AXIS_REGISTRY_V1
AXS-001 | {"status":"SATURATED","subject":"Axe 1 (procedure): la panique drones 2025 a servi de levier pour des achats C-UAS acceleres SANS appel d'offres (urgence invoquee) malgre avis defavorable Inspection des Finances - vs reponse legitime procedure (France Hologarde 2017, appel d'offres)","type":"POSITION"}
AXS-002 | {"status":"SATURATED","subject":"Axe 2 (prix): les prix payes (Senhive 84.000 EUR/antenne, BLAZE ~26.000 EUR/unite via Cobbs) sont 3-4x le prix marche (Pano) - vs Defense/Senhive/Cobbs: version pro SENIDPRO + package complet (consoles, munitions, formation, CAMO)","type":"POSITION"}
AXS-003 | {"status":"SATURATED","subject":"Axe 3 (menace -> marche): la menace qui justifie les achats (vague 2025 BE attribuee a la Russie) n'est pas confirmee par les enquetes (0 preuve Pano) - mais l'incident REEL Leipzig 04/08/2026 (drone explosif) montre qu'une menace materielle existe ailleurs: distinguer panique vs menace vs marche structurel","type":"POSITION"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"confidence":"0.8","evidence":"FCT-001 + FCT-004: avis Inspection Finances negatif 10/2025, commandes sans appel d'offres par haute urgence, 0 preuve de drone hostile (Pano), video 'drone' = helicoptere police","kind":"EFFECT","status":"SUPPORTED","subject":"La vague de signalements (558, 09/2025-01/2026, aucun drone hostile confirme) a declenche un achat accelere de 50 M EUR sans appel d'offres en Belgique: la chronologie (signalements -> crise declaree -> achats sous 2 mois -> avis negatif outre) et l'enquete parquet (04/2026) etayent un lien panique->depense, documente par VRT Pano + sUAS News (2 familles independantes)","type":"CAUSAL"}
CAU-002 | {"confidence":"0.6","evidence":"FCT-002 + FCT-003: reponses ecrites Senhive (Pano 04/2026) et Cobbs (confidentialite), Defense (prix verifies via pays partenaire CAMO et controle Ukraine)","gap":"l'ecart de prix (x4 allege Pano) est conteste par Defense/Senhive/Cobbs (SENIDPRO version pro, package BLAZE complet): le litige porte sur la comparaison (base vs pro), non tranche publiquement - enquete parquet et audit en cours","gap_type":"DISPUTED","kind":"EFFECT","status":"GAP","subject":"Les prix payes (Senhive ~84.000 EUR/antenne, BLAZE ~26.000 EUR/unite) sont 3-4x le prix de marche: l'ecart est documente par l'etude marche de Pano (1/4 du prix Senhive; ~6.000 EUR/unite BLAZE selon expert + producteur) MAIS conteste par Defense/Senhive/Cobbs (SENIDPRO version pro CAMO; package complet consoles+munitions+formation+C2; prix audites et controles fin 2025)","type":"CAUSAL"}
CAU-003 | {"confidence":"0.5","evidence":"FCT-005 + FCT-006: Hologarde 2017 post-Orly 2016 (pre-incident), marche FR structurel, plan Commission 02/2026","gap":"impossible de quantifier la part de la croissance du marche C-UAS attribuable aux vagues de signalements non confirmes vs menaces materielles reelles","gap_type":"CORRELATION_VS_CAUSATION","kind":"GAP","status":"GAP","subject":"Lien causal vague de drones -> croissance du marche europeen C-UAS (1,2 Md -> 4,2 Md USD 2025-2030): la croissance precede et depasse le cas belge (France depuis 2016, Ukraine, Leipzig 2026 = menaces materielles reelles); le cas BE documente UN cas de panique->marche, la generalisation UE reste non demontree","type":"CAUSAL"}
CAU-004 | {"confidence":"0.75","evidence":"FCT-005: evaluation competitive BLAZE (06/2026), partenariat ADP/Thales/DSNA","kind":"EFFECT","status":"SUPPORTED","subject":"La France demontre qu'une reponse anti-drones peut etre structurelle et procedurale SANS panique: Hologarde (2017) cree apres incident reel (Orly 2016), marches avec appels d'offres, 2000+ incidents/an mesures - le contraste BE/FR montre que la procedure (appel d'offres vs urgence) est le discriminant cle, pas la menace","type":"CAUSAL"}
CAU-005 | {"confidence":"0.4","evidence":"FCT-006 (structure Senhive startup seed) + enquete parquet 04/2026 ouverte (FCT-001)","gap":"l'enquete judiciaire (corruption, obstruction encheres) n'a pas rendu de verdict: distinguer corruption etabile, conflit d'interets et simple procedure d'urgence maladroite","gap_type":"INTENT","kind":"GAP","status":"GAP","subject":"Liens entre vendeurs et decideurs (Senhive/fondateurs, Cobbs/intermediaire, Origin Robotics): aucune preuve de lien politique direct documentee - Senhive est une startup sans actionnariat politique public; le flux d'argent public vers des petits acteurs via procedures d'urgence est documente mais l'intention (corruption vs maladresse) est l'objet de l'enquete parquet, non tranchee","type":"CAUSAL"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"evidence":"Run 17 FCT-004 (Leipzig, 2 familles): cas discriminant","status":"SATURATED","subject":"CONTROL-1: le cas Leipzig (04/08/2026, drone avec explosif, preuve materielle, ADN, 2 suspects BKA) montre qu'une menace drone reelle existe et que des achats anti-drones peuvent etre justifies - la panique belge n'invalide pas la menace globale","type":"CONTROL"}
CTRL-002 | {"evidence":"FCT-001 refutation (QRY-015): reponse Defense/Francken 04/2026","status":"SATURATED","subject":"CONTROL-2: la Defense belge defend la legalite de la procedure (loi respectee, commission Armee approuve 1 abstention, budget 2025 approuve 5 mois avant, prix audites) - le cadrage 'corruption' est premature; l'avis Inspection des Finances est consultatif","type":"CONTROL"}
CTRL-003 | {"evidence":"FCT-004 refutation (QRY-018): position Defense 04/2026","status":"SATURATED","subject":"CONTROL-3: l'explication 'menace russe' reste l'hypothese des services belges 'la plus plausible' (Euroclear, Kleine-Brogel) sans preuve formelle - symetrie: le doute sur l'attribution russe ne prouve pas l'absence de drones, seulement l'absence de preuve publiee","type":"CONTROL"}

### ACTION_REGISTRY_V1
ACT-001 | {"evidence":"FCT-001 + FCT-002 + FCT-003","status":"SUPPORTED","subject":"ACT-1: suivre l'enquete du parquet de Bruxelles (ouverte 17/04/2026) et l'audit interne federal ordonne par Francken - verdict sur l'ecart de prix et la procedure d'urgence","type":"ACTION"}
ACT-002 | {"evidence":"FCT-002 + FCT-003 contestations","status":"SUPPORTED","subject":"ACT-2: comparer les prix Senhive/BLAZE aux contrats equivalents UE (CAMO belgo-francais, support Ukraine) une fois les donnees publiees - trancher le litige prix 'version pro' vs 'prix marche'","type":"ACTION"}
ACT-003 | {"evidence":"FCT-005 + FCT-006","status":"SUPPORTED","subject":"ACT-3: verifier la chaine Senhive -> JO 2024 (usage reel allege des capteurs aux JO) et le transfert de technologie BLAZE/DSV en France (echeances 06/2026+)","type":"ACTION"}

SEARCH_ACTIVITY_V1:WEB:13|FETCH:7|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-003 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-009 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-010 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-011 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-012 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-013 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-014 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-015 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-016 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-017 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-018 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-019 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-020 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-021 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-022 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-023 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-024 | SYS | PASS | runtime | probe:filiere-antidrones-europe-qui-vend-qui-gagne | MNEMO_Q
SYS-025 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-026 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | discovery ok | - | - | Pano VRT Francken 50 M EUR antidrone sans appel d'offres Senhive Cobbs BLAZE Inspection Finances avis defavorable
QRY-002 | WEB | discovery ok | - | - | France selectionne intercepteur BLAZE Origin Robotics DSV juin 2026 4e operateur europeen transfert technologie
QRY-003 | WEB | discovery ok | - | - | enquete parquet Bruxelles 17/04/2026 ministere defense corruption obstruction encheres publiques achat anti-drones
QRY-004 | WEB | discovery ok | - | - | Senhive Hasselt fondee 2019 Petracca Paesen Burm startup detecteur drones capital actionnaires
QRY-005 | WEB | discovery ok | - | - | aeroports Paris protection anti-drone Hologarde ADP Thales incidents 2016 Orly 2000 par an DJI Aeroscope
QRY-006 | WEB | discovery ok | - | - | marche europeen anti-drone C-UAS croissance 2025 2030 Commission europeenne plan action fevrier 2026
QRY-007 | WEB | discovery ok | - | - | Blaze drone interceptor prix unitaire Origin Robotics Lettonie Cobbs intermediaire Belgique valeur 300 unites
QRY-008 | FETCH | FOUND | SRC-001 | https://www.vrt.be/vrtnws/nl/2026/04/14/counterdroneplan-francken-pano/ | FETCH VRT Pano 15/04/2026 - Defensie geeft versneld 50 miljoen uit
QRY-009 | FETCH | FOUND | SRC-002 | https://www.suasnews.com/2026/04/echoes-of-agusta-how-a-e50m-drone-panic-sparked-belgiums-latest-defence-crisis/ | FETCH sUAS News 17/04/2026 - Echoes of Agusta: how a 50m drone pan
QRY-010 | FETCH | FOUND | SRC-003 | https://www.brusselstimes.com/2081360/francken-under-fire-as-investigation-condemns-his-e50m-anti-drone-plan-as-ineffective-and-costly | FETCH Brussels Times 17/04/2026 - Francken under fire, investigati
QRY-011 | FETCH | FOUND | SRC-004 | https://thedefensepost.com/2026/06/17/france-blaze-interceptor-drone/ | FETCH The Defense Post 17/06/2026 - France selects BLAZE intercept
QRY-012 | FETCH | FOUND | SRC-005 | https://dronexl.co/2025/09/29/paris-airports-anti-drone-defense-system/ | FETCH dronexl 29/09/2025 - Paris airports deploy multi-layered ant
QRY-013 | FETCH | FOUND | SRC-006 | https://tracxn.com/d/companies/senhive/__dLEy5AQM3jplVIt0WIvAxL4kBM9zrEy3p3_I77dQg9o | FETCH tracxn + made-in.be - Senhive company profile (Hasselt 2019,
QRY-014 | FETCH | FOUND | SRC-007 | https://www.vrt.be/vrtnws/fr/2025/11/17/la-defense-va-acheter-des-intercepteurs-de-drones-d-une-societe/ | FETCH VRT 17/11/2025 - La Defense va acheter des intercepteurs de 
QRY-015 | WEB | refutation counter-evidence found | - | - | REFUTATION procedure BE: la Defense repond (04/2026) que la procedure d'urgence etait LEGALE (loi marches publics respectee, commission Armee approuve avec 1 seule abstention sur ~11 membres), que le plan 50 M EUR etait dans le budget 2025 deja approuve depuis 5 mois (pas un budget supplementaire, Francken X 11/2025), que l'avis defavorable de l'Inspection des Finances (10/2025) est consultatif et peut etre ecarte legalement, et que les prix ont ete audites - la loi n'a pas ete contournee (Francken 17/04/2026)
QRY-016 | WEB | refutation counter-evidence found | - | - | REFUTATION prix Senhive: Senhive repond (Pano 04/2026) que la Defense n'a pas achete le SENID+ standard mais son successeur SENIDPRO (double bande passante, spectrumanalyse avancee, Angle of Arrival, Time Difference of Arrival, cablage supplementaire, design robuste) - deux produits differents; comparer un 'prix par antenne' a une configuration de base n'est pas correct (multilateration = plusieurs unites par perimetre); SENIDPRO est sorti d'abord chez des clients defense AVANT 11/2025; Defense: version SEN PRO du projet CAMO belgo-francais, prix verifie via le pays partenaire - prix conforme au marche
QRY-017 | WEB | refutation counter-evidence found | - | - | REFUTATION prix BLAZE: la Defense repond (04/2026) qu'un controle de prix fin 2025 (paquet support Ukraine) a valide le prix; le prix unitaire ~26.000 EUR (7,8 M EUR / 300) inclut au-dela du drone: consoles de controle, munitions, formation, systeme C2 (commandement-controle) - pas comparable a un prix 'drone seul' de ~6.000 EUR; Cobbs (intermediaire, CEO Rummens) invoque la confidentialite contractuelle et securite operationnelle; la Defense souligne que Cobbs est un partenaire de longue date avec d'autres contrats UE
QRY-018 | WEB | refutation counter-evidence found | - | - | REFUTATION menace BE: la Defense repond (04/2026) que ses services de securite considerent l'hypothese d'ingerence russe 'la plus plausible' (sans preuve formelle) en raison du role de la Belgique (avoirs russes Euroclear, base Kleine-Brogel); les signalements incluent des observations RADAR + visuelles par des militaires formes (pas que des civils); des drones ont ete vus sur 5+ sites sensibles (Elsenborn, Doel, Kleine-Brogel, aeroports) de facon coordonnee sur 4 mois (09/2025-01/2026) - coincidence peu probable
QRY-019 | WEB | refutation counter-evidence found | - | - | REFUTATION contraste FR/BE: la France a AUSSI accelere: plan 350 M EUR pour brouillage anti-drone avant JO 2024 (2022) et deploiement exceptionnel JO 2024 (42 M EUR, perimetre Ile-de-France); la France selectionne BLAZE/DSV apres 'evaluation competitive' (06/2026) MAIS Origin Robotics etait deja operationnel LV/BE/EE - interets industriels partages (transfert de technologie); le marche FR civil (Hologarde) est pilote par ADP (operateur prive de CDG/Orly) qui a un INTERET commercial direct a la securisation - pas une pure reponse d'Etat
QRY-020 | WEB | refutation counter-evidence found | - | - | REFUTATION 'marchand de menace': le marche C-UAS est documente comme reponse a des menaces REELLES et croissantes (Ukraine: 7 millions de drones prevus 2026, drones russes a fibre optique non brouillables; incident Leipzig 04/08/2026 avec explosif reel; 2.000+ incidents/an Paris depuis 2016) - la croissance du marche (1,2 -> 4,2 Md USD UE 2025-2030, 27,5% CAGR, sources marche) precede et depasse le cas belge; la plupart des achats europeens (FR, LV, EE, DE) passent par des appels d'offres et des evaluations - le cas BE est l'exception documentee, pas la regle

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.vrt.be/vrtnws/nl/2026/04/14/counterdroneplan-francken-pano/
SRC-002 | ◈ | fam:A | https://www.suasnews.com/2026/04/echoes-of-agusta-how-a-e50m-drone-panic-sparked-belgiums-latest-defence-crisis/
SRC-003 | ◈ | fam:B | https://www.brusselstimes.com/2081360/francken-under-fire-as-investigation-condemns-his-e50m-anti-drone-plan-as-ineffective-and-costly
SRC-004 | ◈ | fam:C | https://thedefensepost.com/2026/06/17/france-blaze-interceptor-drone/
SRC-005 | ◈ | fam:D | https://dronexl.co/2025/09/29/paris-airports-anti-drone-defense-system/
SRC-006 | ○ | fam:E | https://tracxn.com/d/companies/senhive/__dLEy5AQM3jplVIt0WIvAxL4kBM9zrEy3p3_I77dQg9o
SRC-007 | ◈ | fam:other:vrt | https://www.vrt.be/vrtnws/fr/2025/11/17/la-defense-va-acheter-des-intercepteurs-de-drones-d-une-societe/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.vrt.be/vrtnws/nl/2026/04/14/counterdroneplan-francken-pano/ | A,B | 2026-09-05 | Procedure Belgique: plan anti-drones de 50 M EUR lance en urgence SANS appel d'offres public malgre avis DEFAVORABLE de l'Inspection des Finances (octobre 2025: contradiction avec la loi sur les marches publics, risque de prix eleves); le budget etait dans le plan deja approuve (Francken, 11/2025); commission Armee approuve (1 abstention sur 11); parquet de Bruxelles ouvre enquete en 04/2026 (corruption, obstruction encheres publiques) - comparaison scandale Agusta | Procedure acceleree sans appel d'offres malgre avis negatif Inspection Finances + enquete judiciaire | 3d918434-5991-4445-bd57-2e724dddfef5
FCT-002 | FACT | ✦ | https://www.vrt.be/vrtnws/nl/2026/04/14/counterdroneplan-francken-pano/ | A,B | 2026-09-05 | Prix Senhive: la Defense belge paie plus de dix millions EUR (HT) pour des quatre-vingt-quatre antennes RF SENID a Senhive (Hasselt); etude marche Pano: memes antennes disponibles pour environ le quart de ce prix. CONTESTE par Senhive: la Defense a achete SENIDPRO (version militaire pro, clients defense avant 11/2025, prix deja pratique, marque conforme), comparer un prix par antenne en configuration de base n'est pas correct; Defense: version SEN PRO du projet CAMO belgo-francais, prix verifie via le pays partenaire (04/2026) | Ecart de prix allege x4 (Pano) vs reponse Defense/Senhive (version pro SENIDPRO, prix marque) - litige sur la comparaison | 79353ad3-b572-43f8-baa5-850ace2a86f2
FCT-003 | FACT | ✦ | https://www.vrt.be/vrtnws/fr/2025/11/17/la-defense-va-acheter-des-intercepteurs-de-drones-d-une-societe/ | B,other:vrt | 2026-09-05 | Prix BLAZE: la Defense belge achete 300 drones kamikazes lettons BLAZE (Origin Robotics) via l'intermediaire belge Cobbs pour 7,8 M EUR HT; Pano (04/2026): expert + producteur estiment chaque drone a environ 6.000 EUR - surcout allege de plusieurs millions pour les 300 unites. CONTESTE: Cobbs invoque la confidentialite contractuelle; Defense: prix controle fin 2025 (paquet support Ukraine 2025-2026), prix unitaire de 26.000 EUR incluant consoles, munitions, formation et systeme de commandement - package complet, non comparable a un prix 'drone seul' | Surcout allege ~6 M EUR (300 BLAZE 7,8 M EUR vs ~1,8 M EUR valeur estimee) - package complet conteste | ee09e677-319c-48e1-aee0-e0a440888d17
FCT-004 | FACT | ✦ | https://www.suasnews.com/2026/04/echoes-of-agusta-how-a-e50m-drone-panic-sparked-belgiums-latest-defence-crisis/ | A,B | 2026-09-05 | Menace: des centaines de signalements de drones suspects (septembre 2025 - janvier 2026, soit 5 mois) ont ferme Bruxelles/Liege aeroports et vise Doel + Kleine-Brogel (4 sites et plus); Francken: 'crise militaire', guerre hybride, implication russe. CONTRE-ENQUETE Pano (04/2026): AUCUNE preuve de drones hostiles d'Etat; un 'gros drone' Zaventem etait un helicoptere de police (01/2026); Defense: hypothese russe 'la plus plausible' SANS preuve formelle (09/2025-2026) | 558 signalements -> 0 preuve de drone hostile d'Etat (Pano); 'drone' Zaventem = helicoptere police; hypothese russe 'plus plausible' sans preuve | cb3c0173-e2b9-457a-b854-9a755ae76d19
FCT-005 | FACT | ✦ | https://thedefensepost.com/2026/06/17/france-blaze-interceptor-drone/ | C,D | 2026-09-05 | Marche FRANCE: contraste avec la Belgique. Civil: ADP a cree Hologarde apres incident REEL (Orly, deroutement), avec Thales + DSNA; incidents de drones reguliers mesures autour des sites parisiens; detection multicouche. Militaire: France selectionne (06/2026) l'intercepteur BLAZE (Origin Robotics + DSV) apres evaluation COMPETITIVE, transfert technologie 'Made in France'; 4e operateur europeen. Contre-point: la France a AUSSI accelere (plan brouillage 350 M EUR des 2022, deploiement JO 2024 de 42 M EUR) et Hologarde depend d'un operateur prive (ADP) avec interet commercial direct | France = marche structurel post-incident reel (Hologarde 2017, appels d'offres, 2000+ incidents/an) et selection BLAZE par evaluation competitive - vs BE 50 M EUR sans appel d'offres | 853acad3-6e13-4924-a263-2858fbdfc596
FCT-006 | FACT | ✦ | https://tracxn.com/d/companies/senhive/__dLEy5AQM3jplVIt0WIvAxL4kBM9zrEy3p3_I77dQg9o | C,E | 2026-09-05 | Filiere: Senhive = startup (Hasselt), petit acteur recevant plus de dix millions EUR publics, sans lien politique documente; Origin Robotics = fabricant letton du BLAZE operationnel LV/BE/EE (4 operateurs europeens avec la France), etendu via DSV; Cobbs = intermediaire belge. Marche UE C-UAS en croissance structurelle (1,2 Md USD en 2025 -> 4,2 Md en 2030, 27,5% CAGR); incident REEL Leipzig (aout 2026: drone explosif). Lien causal vague->marche demontre au cas BE seulement, pas au niveau UE | Filiere: startup BE (Senhive) + fabricant letton (Origin) + intermediaire BE (Cobbs) + partenariat FR (DSV); marche UE C-UAS en croissance structurelle; lien causal vague->marche demontre au cas BE seulement | b0e9ac49-1442-4b88-a572-21b8ebe4b07d
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-003
FCT-002 | SRC-001,SRC-003
FCT-003 | SRC-007,SRC-003
FCT-004 | SRC-002,SRC-003
FCT-005 | SRC-004,SRC-005
FCT-006 | SRC-004,SRC-006

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-015 | FOUND_RESOLVED
FCT-002 | QRY-016 | FOUND_RESOLVED
FCT-003 | QRY-017 | FOUND_RESOLVED
FCT-004 | QRY-018 | FOUND_RESOLVED
FCT-005 | QRY-019 | FOUND_RESOLVED
FCT-006 | QRY-020 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME
FCT-006 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 leads (achats C-UAS BE, enquete parquet, contre-enquete Pano, marche FR, vendeurs, marche UE) | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 scope (filiere C-UAS Europe 2025-2026, adversaire) | NEXT_ACTION:SEARCH_DISCOVERY
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 discovery (7 requetes WEB + 7 FETCH traces, 7 sources) + 6 facts tier ETOILE 2 familles | NEXT_ACTION:CAUSAL analysis
CP-004 | FACTS | PASS | LAST_COMPLETED:10 facts registry (6 faits ETOILE, 2 familles, 6 refutations alignees) | NEXT_ACTION:CAUSAL analysis
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 causal (5 CAU dont 2 GAP types, 3 CTRL, 3 ACT) | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 verify (6 faits 2 familles + refutation, discriminants numeriques OK, litiges prix enregistres) | NEXT_ACTION:sections render
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 accountability (14 sections dont 9 derivees RUNTIME_DERIVED, trace complete, 6 faits ETOILE, EDI) | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T14:51:52.534309+00:00","fact_mem":{"FCT-001":"3d918434-5991-4445-bd57-2e724dddfef5","FCT-002":"79353ad3-b572-43f8-baa5-850ace2a86f2","FCT-003":"ee09e677-319c-48e1-aee0-e0a440888d17","FCT-004":"cb3c0173-e2b9-457a-b854-9a755ae76d19","FCT-005":"853acad3-6e13-4924-a263-2858fbdfc596","FCT-006":"b0e9ac49-1442-4b88-a572-21b8ebe4b07d"},"mnemo_row":"MNEMO_S 87d34194-93d2-495c-a191-c3f1521e3f3a","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"writeback MnemoLite","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_S 87d34194-93d2-495c-a191-c3f1521e3f3a | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-006 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
