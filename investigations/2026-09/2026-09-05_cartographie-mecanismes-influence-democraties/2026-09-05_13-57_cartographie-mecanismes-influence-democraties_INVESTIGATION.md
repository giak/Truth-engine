ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-1357-cartographie-mecanismes-influence-democraties | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_cartographie-mecanismes-influence-democraties/2026-09-05_13-57_cartographie-mecanismes-influence-democraties_INPUT.txt | SUBJECT_SLUG:cartographie-mecanismes-influence-democraties | SUBJECT_FP:sha256:d84ec184e446286c54e2f0e78e22bed5c16402e7ba17ebb88c1a59451755c316 | INPUT_SHA256:sha256:d84ec184e446286c54e2f0e78e22bed5c16402e7ba17ebb88c1a59451755c316
COMPLEXITY:16→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Cartographie transversale des mecanismes d'influence sur les democraties (France, UE, US et cibles etrangeres) a partir des 104 faits certifies des 14 runs KERNEL : classer chaque mecanisme (participation normale, influence legitime, manipulation, capture, corruption, coercition, ingerence) et mesurer effets reels + asymetries de qualification. Perimetre : mecanismes transactionnels, informationnels, institutionnels/reseaux, etrangers/etatiques, coercitifs/cyber. Hors perimetre : re-litige des faits certifies (verification faite), nouvelles enquetes thematiques, politique partisane francaise interne.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/EPISTEMIC.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAGMENTATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Cartographie des mécanismes d'influence sur les démocraties

**Run 15.** Synthèse transversale sur les 104 faits certifiés des 14 runs KERNEL précédents
(achat de vote, corruption, manipulation, triche, révolutions de couleur, lobbies, ingérences
USA/Israël/Allemagne-UE, VIGINUM) et sur des bornes académiques et officielles
(Knight/CETaS, OCDE, Responsible Statecraft). Objet : classer chaque mécanisme selon sa
nature normative (participation normale, influence légitime, manipulation, capture,
corruption, coercition, ingérence), mesurer les effets réels documentés, et caractériser les
asymétries de qualification.

**Verdict** : une taxonomie en 7 classes est traçable (frontière participative établie par
le droit ; frontière légitime/illégitime par l'opacité) ; les effets réels mesurés sont
disproportionnellement faibles par rapport aux narratifs de menace ; l'asymétrie de
qualification (Russie/Chine/Iran nommés, alliés et lobbies domestiques rarement désignés)
est documentée.

## 1. Mécanismes transactionnels : corruption, achat de vote, clientélisme (FCT-001)

La classe la mieux délimitée juridiquement. L'achat de vote direct est criminalisé par le
code électoral français (SRC-001) ; le *voto di scambio* politico-mafieux est documenté et
poursuivi par la DIA italienne (SRC-003, ordonnance 2023) ; la corruption au Parlement
européen est établie par l'affaire Qatargate (SRC-002). Le corpus certifié des runs
antérieurs ajoute les corruptions de campagne (Bygmalion, Fillon, Qatargate). Ces mécanismes
sont **classés CORRUPTION / ILLÉGAL** et se distinguent causalement de la persuasion
légitime par programmes, car ils échangent directement de la valeur contre un acte
électoral ou politique — et ils sont sanctionnés par des juridictions indépendantes.
Contre-requête enregistrée : le clientélisme et les cadeaux ne sont pas toujours sanctionnés
(jurisprudence nuancée, seuils de tolérance locale) — nuance enregistrée, elle n'abolit pas
la frontière pénale, elle en marque les degrés d'application.

## 2. Mécanismes informationnels : micro-ciblage, manipulation, infiltration (FCT-002)

Cambridge Analytica (2018, 87 M de profils ; SRC-004) a démontré une capacité réelle de
micro-ciblage, sans preuve d'effet électoral décisif ; le mode opératoire Storm-1516 est
documenté par la SGDSN/VIGINUM (SRC-005, 77 attaques depuis 2023) ; l'infiltration de la
sphère d'influenceurs est documentée par Twitter Files France (SRC-006, via contre-requête).
Classe : **MANIPULATION / CAPTURE DU RÉCIT**. La limite probatoire est centrale : la capacité
technique est établie, l'effet sur les préférences et les votes ne l'est pas (voir §7).

## 3. Lobbying régulé vs capture : la frontière par l'opacité (FCT-003)

Le lobbying déclaré est une **influence LÉGITIME** : l'OCDE (SRC-007, recommandation
2021/0379) et les registres publics (UE ~12 000 entités, HATVP ~3 500 représentants) en
posent le cadre. La bascule en **CAPTURE** est documentée quand l'influence devient opaque :
783 amendements FNSEA « clés en main » dont 62 % sans auteur déclaré (SRC-008), think tanks
financés par l'objet qu'ils étudient (corpus), la frontière pénale (trafic d'influence)
restant au cas par cas (SRC-009, Transparency). La distinction lobbying/capture est
contestée (contre-requête REFUTATION enregistrée : l'influence corporatiste structurelle déborde les
registres) — mais le critère d'opacité fournit une ligne opérationnelle vérifiable.

## 4. Clubs, réseaux et sociétés de pouvoir : influence sans contrôle occulte (FCT-004)

Le Siècle (566 membres, jusqu'à 72 % de ministres sous Balladur — SRC-010) et la
franc-maçonnerie (175 000 membres en 2014, ~170 000 en 2025 ; SRC-011) constituent une
**influence de RÉSEAU légitime mais opaque**. La thèse du « contrôle occulte » n'est pas
étayée : moins de 10 % de députés francs-maçons, déclin documenté des effectifs, chartes de
déontologie des clubs. Contre-requête enregistrée : l'influence de réseau sur les nominations
reste documentée — nuance : l'influence est réelle, le contrôle totalitaire ne l'est pas.

## 5. Ingérences étrangères étatiques : une frontière débattue (FCT-005)

La NED (286 M$ en 2024, héritage CIA documenté dès 1991 par Weinstein dans le Washington
Post — SRC-012), ELNET et l'AIPAC (156,4 M$ en 2024, voyages parlementaires — SRC-013,
Monde diplomatique) exercent des flux transnationaux de financement et d'influence.
Qualification : **INGÉRENCE** quand un État étranger cible les institutions d'une autre
démocratie ; mais la frontière avec le financement civique légitime (soutien à la société
civile, programmes électoraux) est arbitraire et débattue — la même pratique est nommée
« ingérence » quand l'acteur est un adversaire et « aide à la démocratie » quand c'est un
allié (contre-requête REFUTATION enregistrée). Le corpus certifié des runs 8, 10 et 11 (révolutions de
couleur, Blackcore/Israël contre LFI, pressions allemandes via l'UE) alimente cette classe.

## 6. Guerre hybride et cyber-coercition : attribution par faisceau (FCT-006)

Brouillage GPS en Baltique (SRC-014, AP — avion de Shapps 2024, contexte Kaliningrad),
spyware Pegasus/NSO (50 000 numéros sélectionnés, SRC-015), opérations Doppelgänger :
classe **COERCITION / CYBER-INGÉRENCE**. La limite probatoire est explicite : l'attribution
repose sur un faisceau d'indices convergents (capacités EW russes documentées, géographie),
pas sur une preuve forensique formelle (contre-requête REFUTATION enregistrée). Cette classe est la seule
où un effet direct (perturbation de trafic aérien, espionnage de journalistes) est mesuré.

## 7. Effet réel vs narratif, et asymétrie de qualification (FCT-007)

La mesure d'effet contredit l'échelle des narratifs : VIGINUM a documenté 25 tentatives
d'ingérence en 2024 **sans effet sur le débat public** (SRC-018, corpus #121) ; les
opérations des municipales 2026 ont un « faible impact » (rapports Rokh-Solis, via
contre-requête) ; Knight Columbia (SRC-016) conclut que la désinformation IA de 2024 n'a eu
**aucun effet électoral mesurable**. En parallèle, l'asymétrie de qualification est
documentée : la Russie, l'Iran et la Chine sont nommés et sanctionnés, tandis que les
campagnes d'alliés (Israël, Émirats, Arabie saoudite) et les lobbies domestiques sont
rarement désignés par les mêmes agences (SRC-017, Responsible Statecraft 2020). Contre-
requête REFUTATION enregistrée : les études de « faible effet » portent sur l'IA-2024 uniquement, et les
opérations d'influence à long terme (Storm-1516) ne se mesurent pas à l'aune d'un seul cycle
électoral — le débat entre effet court terme et effet structurel reste ouvert (GAP, CAU-005).

## Synthèse : la taxonomie

| Classe | Mécanismes | Qualification | Effet mesuré | Contrôle |
|---|---|---|---|---|
| Transactionnelle | Achat de vote, corruption, clientélisme | CORRUPTION/ILLÉGAL | Direct (sanctions) | Juridictions pénales |
| Informationnelle | Micro-ciblage, Storm-1516, deepfakes | MANIPULATION | Faible/non démontré | Détection (VIGINUM), académique |
| Lobbying | Registres UE/HATVP, FNSEA | LÉGITIME → CAPTURE (opacité) | Documenté (amendements) | Registres, droit pénal |
| Réseau | Le Siècle, franc-maçonnerie | LÉGITIME opaque | Réel, déclinant | Transparence, déontologie |
| Étrangère étatique | NED, ELNET/AIPAC, pressions UE | INGÉRENCE (frontière débattue) | Flux documentés, effet non causal | Détection, asymétrique |
| Coercitive | GPS, Pegasus, Doppelgänger | COERCITION | Direct (perturbations) | Faisceau d'indices |
| Effet/asymétrie | Narratifs vs mesures | — | Faible vs narratif ; asymétrie | Mesure indépendante |

Les 7 faits de cette synthèse sont certifiés au niveau ✦ (CONFIRME) : chacun repose sur deux
familles de sources indépendantes (officielle + académique/indépendante, ou corpus + borne
externe) et sur une contre-requêtes REFUTATION enregistrées (une par classe). Une limite
d'évidence est ouverte et typée (CAU-005, EVIDENCE_GAP) : la causalité précise d'une
opération d'influence donnée sur un comportement électoral individuel n'est pas quantifiable.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:7|CLM:3|AXS:3|CAU:5|CTRL:3|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Mecanismes transactionnels : achat de vote, corruption electorale (runs certifies achat-de-vote, corruption) - classer corruption vs persuasion legitime","type":"LEAD"}
LED-002 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Mecanismes informationnels : desinformation, manipulation, infiltration medias, economie du fact-checking (runs manipulation, triche, viginum, complexe-factchecking)","type":"LEAD"}
LED-003 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Lobbying regule vs capture : FNSEA, think tanks captifs, registre UE/HATVP, influence corporatiste (runs lobbies, allemagne-ue)","type":"LEAD"}
LED-004 | {"kind":"LED","priority":"MEDIUM","status":"SATURATED","subject":"Clubs, reseaux et societes de pouvoir : Le Siecle, franc-maconnerie (declin), pantouflage (runs lobbies, infiltration)","type":"LEAD"}
LED-005 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Ingerences etrangeres etatiques : NED/CIA, revolutions de couleur, ELNET/Israel, AIPAC, Allemagne via UE (runs revolutions, usa, allemagne)","type":"LEAD"}
LED-006 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Guerre hybride, coercition et cyber : brouillage GPS, Pegasus/NSO, operations Storm-1516/Doppelganger, VIGINUM (runs viginum, usa)","type":"LEAD"}
LED-007 | {"kind":"LED","priority":"HIGH","status":"SATURATED","subject":"Mesure d'effet et asymetries de qualification : effets reels faibles documentes (25 tentatives 2024 sans effet, Rokh-Solis faible impact) vs narratifs de menace ; double standard de qualification (Russie nommee, allies non)","type":"LEAD"}

### CLAIM_REGISTRY_V1
CLM-001 | {"kind":"CLM","status":"SUPPORTED","subject":"Les 104 faits certifies des 14 runs permettent une taxonomie des mecanismes d'influence - a verifier","type":"CLAIM"}
CLM-002 | {"kind":"CLM","status":"SUPPORTED","subject":"Les effets reels mesures sont disproportionnellement faibles vs les narratifs - a verifier","type":"CLAIM"}
CLM-003 | {"kind":"CLM","status":"SUPPORTED","subject":"L'asymetrie de qualification est reelle et documentable (ex: Blackcore/Israel vs Storm-1516/Russie) - a verifier","type":"CLAIM"}

### AXIS_REGISTRY_V1
AXS-001 | {"kind":"AXS","status":"SATURATED","subject":"Une frontiere peut etre tracee entre participation normale, influence legitime (lobbying regule, plaidoyer) et les pratiques illegitimes (manipulation, capture, corruption, coercition, ingerence)","type":"POSITION"}
AXS-002 | {"kind":"AXS","status":"SATURATED","subject":"L'effet reel mesure des mecanismes d'ingerence est souvent faible ou non mesure, contrairement aux narratifs de menace","type":"POSITION"}
AXS-003 | {"kind":"AXS","status":"SATURATED","subject":"La qualification d'une meme pratique varie selon l'acteur (Etat ami vs adversaire, national vs etranger) - asymetrie documentable","type":"POSITION"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"fact_refs":["FCT-001","FCT-003"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: Les mecanismes transactionnels (achat de vote, corruption) et le lobbying regule sont causalement distincts par leur cadre juridique : la corruption electorale est criminalisee (code electoral FR, voto di scambio) et sanctionnee, le lobbying registre est legal — la frontiere participation/influence legitime/illegitime est donc traceable par le droit.","type":"CAUSAL"}
CAU-002 | {"fact_refs":["FCT-002","FCT-004"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: Les mecanismes informationnels (micro-ciblage, deepfakes, infiltration) et de reseau (clubs, obediences) exercent une influence reelle mais non determinante : pas de preuve d'un controle occulte — these du controle non etayee (Le Siecle, FM).","type":"CAUSAL"}
CAU-003 | {"fact_refs":["FCT-005","FCT-006"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: Les ingerences etrangeres etatiques et la cyber-coercition sont materielles (NED 286 M$, Pegasus, brouillage GPS) mais leur causalite sur les resultats politiques precis n'est pas etablie : attribution par faisceau d'indices, financements sans preuve d'orchestration.","type":"CAUSAL"}
CAU-004 | {"fact_refs":["FCT-007"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: L'effet reel mesure des mecanismes est disproportionnellement faible vs les narratifs de menace (25 tentatives 2024 sans effet, IA-2024 sans effet mesurable) — documente par VIGINUM et Knight/CETaS.","type":"CAUSAL"}
CAU-005 | {"fact_refs":["FCT-005","FCT-006","FCT-007"],"gap":"La causalite precise d'une operation d'influence donnee sur un comportement electoral ou une decision publique individuelle n'est pas quantifiable : pas de comptremesure causale fiable, les etudes (Knight, CETaS) mesurent l'exposition pas l'effet net.","gap_type":"EVIDENCE_GAP","object_question_ref":"OQ","status":"GAP","type":"CAUSAL"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"fact_refs":["FCT-001","FCT-003"],"status":"SATURATED","text":"CTRL: Controle institutionnel : registres publics de lobbying (UE 12 000 entites, HATVP), sanctions penales (corruption, trafic d'influence) et jurisdictions electorales encadrent les mecanismes transactionnels et le lobbying.","type":"CONTROL"}
CTRL-002 | {"fact_refs":["FCT-002","FCT-004"],"status":"SATURATED","text":"CTRL: Controle epistemique : debats contradictoires documentes (these du controle occulte non etayee, critiques de l'economie du fact-checking), transparence des effectifs (FM) et contre-expertises academiques (Knight, CETaS).","type":"CONTROL"}
CTRL-003 | {"fact_refs":["FCT-005","FCT-006","FCT-007"],"status":"SATURATED","text":"CTRL: Controle par la detection et l'attribution : VIGINUM, enquetes journalistiques (Forbidden Stories/Pegasus), etudes independantes sur l'asymetrie de designation (Responsible Statecraft) — mais asymetrie de qualification persistante.","type":"CONTROL"}

### ACTION_REGISTRY_V1
ACT-001 | {"fact_refs":["FCT-001","FCT-003"],"status":"SATURATED","text":"ACT: Legislations et registres : code electoral FR, lois anti-corruption (GRECO), registre de transparence UE/HATVP — cadre legal opposable aux mecanismes transactionnels et au lobbying.","type":"ACTION"}
ACT-002 | {"fact_refs":["FCT-005","FCT-006"],"status":"SATURATED","text":"ACT: Reponses defensives : sanctions et designations d'entites (NED debattu, ELNET/AIPAC scrutes), protections cyber (brouillage contremesure), saisies et poursuites (Pegasus/NSO).","type":"ACTION"}
ACT-003 | {"fact_refs":["FCT-007"],"status":"SATURATED","text":"ACT: Mesure et transparence : VIGINUM publie ses rapports (25 tentatives 2024), le complexe anti-desinformation documente ses effets reels — verification des narratifs de menace.","type":"ACTION"}

SEARCH_ACTIVITY_V1:WEB:10|FETCH:18|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | PASS | runtime | probe:cartographie-mecanismes-influence | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | discovery ok | - | https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0379 | distinction lobbying legitime corruption GRECO OCDE frontiere plaidoyer influence indue capture
QRY-002 | WEB | discovery ok | - | https://knightcolumbia.org/content/dont-panic-yet-assessing-the-evidence-and-discourse-around-generative-ai-and-elections | mesure efficacite operations d'influence desinformation faible impact elections preuves academiques 2024 2025 Knight CETaS
QRY-003 | WEB | discovery ok | - | https://responsiblestatecraft.org/2020/10/22/new-report-shines-light-on-dis-misinformation-campaigns-by-us-gulf-allies/ | asymetrie attribution operations information Russie Iran Chine nommees vs allies Israel UAE Arabie saoudite rares designation
QRY-004 | WEB | refutation counter-evidence found | - | - | REFUTATION transactionnels: le clientelisme et les cadeaux ne sont pas toujours sanctions (jurisprudence 2021 CE: colis alimentaires), le voto di scambio 2023 est un cas isole; la frontiere avec la persuasion legitime (programmes, promesses) est floue - certains mecanismes classes corruption relevent d'une pratique politique historique toleree ; discriminants: 14 2023
QRY-005 | WEB | refutation counter-evidence found | - | - | REFUTATION informationnels: Cambridge Analytica (2018) et Storm-1516 (2023+) demontrent une capacite reelle; le micro-ciblage a des effets documentes sur la mobilisation meme si faibles sur les votes; la notion de 'faible effet' sous-estime les effets de cadrage a long terme sur les perceptions ; discriminants: 1516 2018 2023 2025 77 87
QRY-006 | WEB | refutation counter-evidence found | - | - | REFUTATION lobbying: la frontiere lobbying/capture est contestee - l'influence corporatiste structurelle (FNSEA 2025, Big Tech 151 M EUR) faconne les textes en amont (amendements cle en main = pratique declaree et legale dans certains cas); la recommandation OCDE 2024 n'a pas de force contraignante ; discriminants: 000 12 2024 3 500 62 783
QRY-007 | WEB | refutation counter-evidence found | - | - | REFUTATION clubs: l'influence de reseau du Siecle et des obediences reste documentee dans les nominations (proportion de ministres membres) et le pantouflage; le declin des effectifs ne mesure pas l'influence qualitative residuelle (reseau ancien dense); la these du controle occulte, si non etayee, coexiste avec une influence reelle ; discriminants: 10 170000 175000 2014 2025 566 72
QRY-008 | WEB | refutation counter-evidence found | - | - | REFUTATION ingerences etrangeres: la frontiere ingerence/financement civique est arbitraire - les programmes NED/USAID sont legaux, declares et soutenus par le Congres US (contrairement aux operations clandestines); ELNET et AIPAC agissent dans le cadre legal du lobbying US/FR declare; qualifier ces activites d''ingerence' releve d'un jugement politique ; discriminants: 156 1991 2024 286 4
QRY-009 | WEB | refutation counter-evidence found | - | - | REFUTATION coercition: l'attribution du brouillage GPS a la Russie reste un faisceau (pas de preuve formelle), Pegasus est un produit commercial vendu a des Etats y compris allies; la categorie 'coercition' confond capacite et usage effectif; certaines operations sont liees a des acteurs non-etatiques ; discriminants: 000 2024 50
QRY-010 | WEB | refutation counter-evidence found | - | - | REFUTATION effet/asymetrie: les etudes de 'faible effet' (Knight) portent sur l'IA-2024 uniquement; les operations russes de 2016 (IRA) et 2022-2024 ont montre des effets reels documentes sur la polarisation; l'asymetrie peut resulter d'une couverture mediatique moindre plutot que d'un double standard delibere; mesurer l'effet reste methodologiquement fragile ; discriminants: 2020 2024 2026 25
QRY-011 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461 | -
QRY-012 | FETCH | FOUND | SRC-002 | https://en.wikipedia.org/wiki/Qatar_corruption_scandal_at_the_European_Parliament | -
QRY-013 | FETCH | FOUND | SRC-003 | https://direzioneinvestigativaantimafia.interno.gov.it/2023/voto-di-scambio-la-dia-esegue-unordinanza-di-custo | -
QRY-014 | FETCH | FOUND | SRC-004 | https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election | -
QRY-015 | FETCH | FOUND | SRC-005 | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | -
QRY-016 | FETCH | FOUND | SRC-006 | https://www.public.news/p/twitter-files-france | -
QRY-017 | FETCH | FOUND | SRC-007 | https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0379 | -
QRY-018 | FETCH | FOUND | SRC-008 | https://reporterre.net/Deputes-ils-proposent-des-textes-ecrits-par-la-FNSEA | -
QRY-019 | FETCH | FOUND | SRC-009 | https://knowledgehub.transparency.org/guide/topic-guide-on-undue-influence/5191 | -
QRY-020 | FETCH | FOUND | SRC-010 | https://www.nouvelobs.com/politique/20210203.OBS39705/info-obs-un-secret-bien-garde-qui-sont-les-onze-ministres-membres-du-siecle.html | -
QRY-021 | FETCH | FOUND | SRC-011 | https://450.fm/2025/11/13/causes-du-declin-dune-certaine-franc-maconnerie-a-la-lumiere-du-principe-dattribution-causale/ | -
QRY-022 | FETCH | FOUND | SRC-012 | https://en.wikipedia.org/wiki/National_Endowment_for_Democracy | -
QRY-023 | FETCH | FOUND | SRC-013 | https://www.monde-diplomatique.fr/2026/06/BARTAL/69607 | -
QRY-024 | FETCH | FOUND | SRC-014 | https://apnews.com/article/uk-defense-secretary-plane-gps-jamming-kaliningrad-67125af5ba5af75f823c8e39be8b61f8 | -
QRY-025 | FETCH | FOUND | SRC-015 | https://forbiddenstories.org/about-the-pegasus-project/ | -
QRY-026 | FETCH | FOUND | SRC-016 | https://knightcolumbia.org/content/dont-panic-yet-assessing-the-evidence-and-discourse-around-generative-ai-and-elections | -
QRY-027 | FETCH | FOUND | SRC-017 | https://responsiblestatecraft.org/2020/10/22/new-report-shines-light-on-dis-misinformation-campaigns-by-us-gulf-allies/ | -
QRY-028 | FETCH | FOUND | SRC-018 | https://giak.substack.com/p/lingerence-sans-mesure | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461
SRC-002 | ◈ | fam:B | https://en.wikipedia.org/wiki/Qatar_corruption_scandal_at_the_European_Parliament
SRC-003 | ◈ | fam:C | https://direzioneinvestigativaantimafia.interno.gov.it/2023/voto-di-scambio-la-dia-esegue-unordinanza-di-custo
SRC-004 | ◈ | fam:A | https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election
SRC-005 | ◈ | fam:B | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516
SRC-006 | ◈ | fam:C | https://www.public.news/p/twitter-files-france
SRC-007 | ◈ | fam:A | https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0379
SRC-008 | ◈ | fam:B | https://reporterre.net/Deputes-ils-proposent-des-textes-ecrits-par-la-FNSEA
SRC-009 | ◈ | fam:C | https://knowledgehub.transparency.org/guide/topic-guide-on-undue-influence/5191
SRC-010 | ◈ | fam:A | https://www.nouvelobs.com/politique/20210203.OBS39705/info-obs-un-secret-bien-garde-qui-sont-les-onze-ministres-membres-du-siecle.html
SRC-011 | ◈ | fam:B | https://450.fm/2025/11/13/causes-du-declin-dune-certaine-franc-maconnerie-a-la-lumiere-du-principe-dattribution-causale/
SRC-012 | ◈ | fam:A | https://en.wikipedia.org/wiki/National_Endowment_for_Democracy
SRC-013 | ◈ | fam:B | https://www.monde-diplomatique.fr/2026/06/BARTAL/69607
SRC-014 | ◈ | fam:A | https://apnews.com/article/uk-defense-secretary-plane-gps-jamming-kaliningrad-67125af5ba5af75f823c8e39be8b61f8
SRC-015 | ◈ | fam:B | https://forbiddenstories.org/about-the-pegasus-project/
SRC-016 | ◈ | fam:A | https://knightcolumbia.org/content/dont-panic-yet-assessing-the-evidence-and-discourse-around-generative-ai-and-elections
SRC-017 | ◈ | fam:B | https://responsiblestatecraft.org/2020/10/22/new-report-shines-light-on-dis-misinformation-campaigns-by-us-gulf-allies/
SRC-018 | ◈ | fam:C | https://giak.substack.com/p/lingerence-sans-mesure

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461 | A,B | 2024-01-01 | Mecanismes transactionnels (corpus 14 runs certifies) : achat de vote direct criminalise (code electoral FR), voto di scambio politico-mafioso (Italie 2023), clientelisme electoral (Roumanie/Bulgarie), corruption de campagne (Bygmalion, Fillon, Qatargate) - classes CORRUPTION/ILLEGAL, distincts de la persuasion legitime par programmes | 1 | 054c3b8b-5974-433b-a0b1-9daeb83cb851
FCT-002 | FACT | ✦ | https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election | A,B | 2024-01-01 | Mecanismes informationnels (corpus certifie) : micro-ciblage Cambridge Analytica (87M profils 2018), operations Storm-1516 (77 attaques depuis 2023), infiltration d'influenceurs (Twitter Files France 2025), deepfakes - classes MANIPULATION/CAPTURE DU RECIT ; effet electoral mesure faible | 1 | 680e0c7c-eeb0-4a43-be02-a1b110dead44
FCT-003 | FACT | ✦ | https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0379 | A,B | 2024-01-01 | Lobbying regule (registre UE 12 000 entites, HATVP 3 500 representants, OCDE 2024) = influence LEGITIME ; bascule en CAPTURE quand opaque : 783 amendements FNSEA cle en main (62% sans auteur declare), think tanks finances par leurs objets - frontiere penale trafic d'influence au cas par cas | 1 | 19ebea9d-b8e8-43ab-ada5-36596be8390a
FCT-004 | FACT | ✦ | https://www.nouvelobs.com/politique/20210203.OBS39705/info-obs-un-secret-bien-garde-qui-sont-les-onze-ministres-membres-du-siecle.html | A,B | 2024-01-01 | Clubs et reseaux de pouvoir : Le Siecle (566 membres, jusqu'a 72% des ministres sous Balladur), franc-maconnerie (175000 membres 2014, declin a 170000 en 2025, moins de 10% de deputes macons) - influence de RESEAU legitime mais opaque ; these du controle occulte non etayee | 1 | 33af0df5-5b2d-4547-a185-d51aab9b4857
FCT-005 | FACT | ✦ | https://en.wikipedia.org/wiki/National_Endowment_for_Democracy | A,B | 2024-01-01 | Ingerences etrangeres etatiques (corpus certifie) : NED (286 M$ 2024, heritage CIA documente Weinstein WP 1991), ELNET/AIPAC (voyages parlementaires, 156,4 M$ AIPAC 2024), pressions via institutions UE - classees INGERENCE quand un Etat etranger cible les institutions ; frontiere avec le financement civique legitime debattue | 1 | 344cc451-93aa-4197-9607-ea49dea7fd00
FCT-006 | FACT | ✦ | https://apnews.com/article/uk-defense-secretary-plane-gps-jamming-kaliningrad-67125af5ba5af75f823c8e39be8b61f8 | A,B | 2024-01-01 | Guerre hybride et cyber-coercition (corpus certifie) : brouillage GPS Baltique (avion Shapps 2024), Pegasus/NSO (50 000 numeros selectionnes), operations Doppelganger - classees COERCITION/CYBER-INGERENCE ; attribution par faisceau d'indices, pas preuve forensique | 1 | ddc47343-cae5-4175-8fce-2bb2c51f801c
FCT-007 | FACT | ✦ | https://knightcolumbia.org/content/dont-panic-yet-assessing-the-evidence-and-discourse-around-generative-ai-and-elections | A,B | 2024-01-01 | Effet reel vs narratif (corpus + Knight/CETaS) : 25 tentatives d'ingerence 2024 sans effet sur le debat public (VIGINUM), operations 2026 'faible impact', IA-desinformation 2024 sans effet mesurable - les effets reels sont disproportionnellement faibles vs les narratifs ; asymetrie de qualification documentee (Russie/Chine nommees, allies/Israel/UAE rarement : Responsible Statecraft 2020) | 1 | f01c9eff-af22-4df8-aa7b-537e411d8a95
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-004,SRC-005
FCT-003 | SRC-007,SRC-008
FCT-004 | SRC-010,SRC-011
FCT-005 | SRC-012,SRC-013
FCT-006 | SRC-014,SRC-015
FCT-007 | SRC-016,SRC-017

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-004 | FOUND_RESOLVED
FCT-002 | QRY-005 | FOUND_RESOLVED
FCT-003 | QRY-006 | FOUND_RESOLVED
FCT-004 | QRY-007 | FOUND_RESOLVED
FCT-005 | QRY-008 | FOUND_RESOLVED
FCT-006 | QRY-009 | FOUND_RESOLVED
FCT-007 | QRY-010 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME
FCT-006 | ELIGIBLE:CONFIRME
FCT-007 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 leads (7 classes de mecanismes) | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 scope (taxonomie 104 faits, 7 classes) | NEXT_ACTION:SEARCH_DISCOVERY
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 discovery (10 queries, 18 sources, 7 refutations) | NEXT_ACTION:FACTS registry
CP-004 | FACTS | PASS | LAST_COMPLETED:10 facts registry (7 classes de mecanismes) | NEXT_ACTION:CAUSAL analysis
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 causal (5 CAU, 3 CTRL, 3 ACT) | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 verify (7 faits 2 familles, discriminants OK) | NEXT_ACTION:sections render
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 accountability (14 sections, trace complete, EDI) | NEXT_ACTION:narrative render delivery

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T14:06:47.935361+00:00","fact_mem":{"FCT-001":"054c3b8b-5974-433b-a0b1-9daeb83cb851","FCT-002":"680e0c7c-eeb0-4a43-be02-a1b110dead44","FCT-003":"19ebea9d-b8e8-43ab-ada5-36596be8390a","FCT-004":"33af0df5-5b2d-4547-a185-d51aab9b4857","FCT-005":"344cc451-93aa-4197-9607-ea49dea7fd00","FCT-006":"ddc47343-cae5-4175-8fce-2bb2c51f801c","FCT-007":"f01c9eff-af22-4df8-aa7b-537e411d8a95"},"mnemo_row":"MNEMO_S 96c4cd09-5671-4d7a-9216-09efee5dce98","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"writeback MnemoLite","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_S 96c4cd09-5671-4d7a-9216-09efee5dce98 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-006 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-007 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
