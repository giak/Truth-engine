ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2030-audit-refondation-pmcb-2027 | PARENT_RUN_ID:20260830-2015-audit-exclusion-pros-decheteries-2026 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-refondation-pmcb-2027/2026-08-30_20-30_audit-refondation-pmcb-2027_INPUT.txt | SUBJECT_SLUG:audit-refondation-pmcb-2027 | SUBJECT_FP:sha256:548a8f58785475e03ac03afc689210e5f56215b1031581e49a184a49f2d75ff2 | INPUT_SHA256:sha256:13765261b5be3771c33a134b2472ad237bdb08bae841c02455b2f93f3d1d050b
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Ecomaison', 'Valdelia', 'Valobat', 'Ecominero', 'OCAB', 'Capeb', 'FFB', 'AMF', 'Intercommunalites de France', 'Regions de France', 'ministere Transition ecologique (Lefevre)', 'deputes (rapport AN 2521)'], 'domains': ['REP', 'PMCB', 'dechets batiment', 'eco-organismes', 'agrements', 'politique publique', 'finances'], 'geo': 'France', 'lead_question': 'Qui gagne et qui perd dans la refondation de la REP PMCB 2027 ? Quels sont les textes, les scenarios en conflit et le sort exact des materiaux matures ?', 'limits': 'textes 2027 non publies au 28/08/2026 (memo 1740) ; agrements futurs non decides', 'object_question': '(1) documenter les textes de la refondation (decret/arrete, agrements 2027) ; (2) cartographier les scenarios (gouvernement vs deputes AN n 2521) ; (3) identifier perdants/gagnants (collectivites, artisans, eco-orgs, OCAB) ; (4) preciser la sortie des matures (calendrier, volumes, compensation)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Axe B — « La bataille de la refondation REP PMCB 2027 » : agréments, scénarios, perdants/gagnants, sortie des matériaux matures

**Run `20260830-2030-audit-refondation-pmcb-2027`** — investigation sur la refondation de la filière REP PMCB au 01/01/2027. Objet : documenter les textes (décret/arrêté, agréments), cartographier les scénarios en conflit (gouvernement vs députés vs Sénat), identifier les perdants/gagnants et préciser le sort exact des matériaux matures.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **Le cadre réglementaire de la refondation est en consultation au printemps 2026** : projet de décret (13 articles) + arrêté cahiers des charges soumis du 23/04 au 19/05/2026 (1 469 contributions), entrée en vigueur prévue **01/09/2026**, nouveaux agréments à déposer sous 1 mois pour le **01/01/2027** — matures (minéraux, métal, bois + plâtre) sortis de la reprise sans frais au 01/01/2027, soutien forfaitaire 2 €/t | ✦ (A+B, réfutation NONE) |
| **FCT-002** | **PPL 2723 (28/04/2026, Delautrette/Riotton/Violland) : contre-scénario parlementaire** — la distinction matures/non matures du gouvernement pourrait exonérer **>85 % des matériaux** et reporter la charge aux collectivités et contribuables ; modèle alternatif en 3 agréments (gravats, bois, second œuvre) ; visible fee | ✦ (C+D, réfutation NONE) |
| **FCT-003** | **Le coût de la REP PMCB serait divisé par 2 à l'horizon 2028 (900 → 450 M€)** ; soutiens limitables aux déchèteries publiques **à compter de 2028 si la collectivité accepte encore les professionnels** — l'exclusion des pros devient un conditionnement financier des soutiens | ✦ (B+D, réfutation NONE) |
| **FCT-004** | **Les artisans se mobilisent contre la fin de la reprise sans frais** : CAPEB 26/05/2026, +1 000 entreprises artisanales répondent à la consultation pour défendre la reprise sans frais des petits volumes triés — suppression prévue au 31/12/2026 ; FFB salue « une victoire » (Salleron), Valobat soutient le scénario gouvernemental | ✦ (E+presse, réfutation NONE) |
| **FCT-005** | **Premier front parlementaire du conflit matures/bois** : PPL Sénat 1436 (rééquilibrer la REP PMCB au profit du bois), rapport AN 2521 du 24/02/2026, examinée puis **rejetée en commission** du développement durable | ✧ (C) |

## Découvertes clés

1. **Une bataille d'argent, pas technique** : le conflit central n'est pas la logistique mais **qui paie les matériaux matures** (minéraux, métal, bois, plâtre) après 2027. Le gouvernement exfiltre ~85 % du gisement (selon la PPL 2723) de la reprise sans frais ; la charge se déplace vers les collectivités (déchèteries) et les contribuables.
2. **Le levier caché : la fermeture aux pros devient un conditionnement financier** (FCT-003) — les soutiens REP aux déchèteries publiques pourraient être conditionnés, à compter de 2028, au refus d'accueillir les professionnels. La décision de service public (accès) se transforme en variable de financement REP. C'est le lien direct avec l'axe A (exclusion des pros).
3. **Les perdants documentés** : artisans TPE (fin de la reprise sans frais des petits volumes au 31/12/2026), collectivités (charge des matures), contribuables (fonds dépôts sauvages réclamé jusqu'à 10 m³ par AMF/Intercommunalités/Régions). Les gagnants restent à établir (recomposition du marché des éco-orgs, 4 candidats potentiels).

## Sources INSPECTED (FETCH direct)

- Consultation publique 23/04-19/05/2026 : projet de décret (13 articles) + arrêté cahiers des charges (1469 contributions)
- Communiqué ministère 19/02/2026 (Lefèvre : scénario officiel, maillage par Conseils régionaux, matures vs non matures, fonds dépôts sauvages)
- PPL 2723 (28/04/2026) PDF intégral (Delautrette/Riotton/Violland)
- Localtis/Banque des Territoires 27/04/2026 (cadre réglementaire en consultation, coût divisé par 2, soutiens conditionnés 2028)
- CAPEB 26/05/2026 (plus d'un millier d'artisans, défense de la reprise sans frais)
- Verre & Protections (réactions Valobat/FFB/CAPEB)
- Rapport AN 2521 (24/02/2026, PPL Sénat 1436 bois rejetée en commission)

## Réfutations (4 NONE + 1 ✧)

- FCT-001 : aucune preuve d'un report de l'entrée en vigueur au-delà du 01/09/2026 ni d'un maintien de l'agrément 2022 sans redépôt ; calendrier cohérent
- FCT-002 : aucune source contredisant le chiffre de 85 % d'exonération potentielle ; la charge reportée aux collectivités est confirmée par Localtis et le communiqué ministériel
- FCT-003 : aucune source documentant un maintien des soutiens REP aux déchèteries publiques accueillant des pros après 2028 ; le cahier des charges conditionne explicitement
- FCT-004 : aucune source documentant une position CAPEB favorable à la fin de la reprise sans frais ; au contraire, +1 000 artisans y sont opposés (26/05/2026)
- FCT-005 (✧) : aucun texte examiné en commission ; la PPL Sénat 1436 a été rejetée en commission du développement durable (rapport AN 2521)

## Gaps ouverts

1. Texte final du décret/arrêté après publication (post-consultation, non publié au 28/08/2026)
2. Liste des candidats aux agréments 2027 et résultat (recomposition du marché : OCAB, Valobat, Ecominero, Valdélia, Ecomaison)
3. Répartition exacte des volumes matures par flux (le chiffre de 85 % de la PPL 2723 reste à confronter aux données ADEME)
4. Sort du fonds dépôts sauvages (montant, abondement, gouvernance)
5. Positions de Ecominero/OCAB/Valdélia/Ecomaison sur le scénario gouvernemental

## Conséquence sur la fresque

L'axe A avait documenté l'exclusion des pros (2025-2026) ; cette passe ajoute la **bataille d'argent qui la sous-tend** : la refondation REP PMCB 2027 exfiltre les matériaux matures de la reprise sans frais, conditionne les soutiens des déchèteries publiques à la fermeture aux pros (2028) et déplace la charge vers les collectivités et les contribuables — pendant que députés (PPL 2723), Sénat (PPL 1436) et artisans (CAPEB/FFB) portent des contre-scénarios. La déchèterie reste le guichet central où se joue la captation.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Le gouvernement veut supprimer la reprise gratuite des dechets matures (metal, bois, platre, inertes) au 01/01/2027","kind":"EVENT","lead":"Refondation REP PMCB au 01/01/2027 : nouveaux agrements eco-orgs, sortie des materiaux matures de la reprise sans frais, fonds depots sauvages 10 m3 demande par AMF/Intercommunalites/Regions + Capeb","linked_ids":["AXS-001"],"locator":"france3 21/04/2026 (Lefevre) ; consultations-publiques.developpement-durable.gouv.fr (projets decret/arrete) ; rapports parlementaires","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (textes 2027 non publies, agrements futurs)","linked_ids":["LED-001","AXS-001"],"proposition":"La refondation PMCB 2027 tranfere la charge des materiaux matures vers les collectivites et les contribuables, au benefice des eco-organismes qui reduisent leurs obligations de reprise — a tester avec textes et chiffres","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":[],"gap_type":"NONE","led_links":["LED-001"],"question":"Quels textes/scenarios gouvernent la refondation PMCB 2027, qui sont les perdants/gagnants et quel est le sort exact des materiaux matures ?","result_ids":[],"sought_objects":["projets decret/arrete refondation PMCB","consultation publique 2026","rapport AN 2521 + scenario 3 deputes","agrements eco-orgs 2027","sortie matures (calendrier, volumes, 2 EUR/t)","positions Capeb/FFB/AMF"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Refondation REP PMCB 2027 (sortie des matures de la reprise sans frais, nouveaux agrements)","effect":"Report de la charge des dechets matures vers les collectivites (decheteries) et risque de depots sauvages ; recomposition du marche des eco-orgs","source":"FCT-002","status":"SUPPORTED","type":"MECHANISM"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:7|EXA:4
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND: warm-route mems b6dea4f9 (FCT-004 axe A : suppression reprise matures 01/01/2027, fonds depots sauvages 10 m3 demande AMF/Capeb) + 749c6591 (bareme Valobat 2026 recalibrage 01/07/2026, refondation 2027, soutien forfaitaire 2 EUR/t) + 20b2f3fe (Valobat agre 2023) ; GAP: textes 2027, scenarios, perdants/gagnants OPEN | mnemolite:search_memory | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-008 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.consultations-publiques.developpement-durable.gouv.fr/projets-de-decret-et-d-arrete-ministeriel-a3340.html | FETCH consultation publique refondation PMCB : decret 13 articles, matures (mineraux/metal/bois + platre 01/01/2027), soutien forfaitaire 2 EUR/t matures, agrements a redeposer sous 1 mois, entree vigueur 01/09/2026, 1469 contributions
QRY-002 | FETCH | FOUND | SRC-002 | https://www.ecologie.gouv.fr/presse/refondation-rep-pmcb-filiere-plus-efficace-plus-lisible-economiquement-soutenable | FETCH communique Lefevre 19/02/2026 : maillage par Conseils regionaux (dechetteries pro > distributeurs > dechetteries publiques), matures vs non matures, fonds depots sauvages alimente par eco-contributions, delai 9 mois baremes, suppression enveloppes comm/R&D, sanctions DDADUE
QRY-003 | FETCH | FOUND | SRC-003 | https://www.assemblee-nationale.fr/dyn/17/textes/l17b2723_proposition-loi.pdf | FETCH PPL 2723 : trie deputes, distinction matures/non matures du gouvernement pourrait exonerer >85% des materiaux, charge aux collectivites/contribuables ; 3 categories d'agrements (gravats, bois, second oeuvre) ; visible fee ; prise en charge integrale depots sauvages (80% des depots illegaux = materiaux) ; contractualisation obligatoire 01/01/2027
QRY-004 | FETCH | FOUND | SRC-004 | https://www.banquedesterritoires.fr/refonte-de-la-rep-produits-et-materiaux-de-construction-du-secteur-du-batiment-le-cadre | FETCH Localtis : cout REP divise par 2 a l'horizon 2028 (900 a 450 MEUR) ; soutiens limitables aux dechetteries publiques a compter de 2028 si la collectivite accepte encore les pros ; contrats signes sous 3 mois ; temps de parcours 15 min ; prise en charge au premier point de massification ; transport chantiers exclu
QRY-005 | FETCH | FOUND | SRC-005 | https://www.capeb.fr/actualites/dechets-du-batiment-les-artisans-disent-non-a-la-fin-de-la-reprise-sans-frais | FETCH CAPEB 26/05/2026 : plus d'un millier d'entreprises artisanales ont repondu a la consultation ; defense de la reprise sans frais des petits volumes de dechets tries ; suppression au 31/12/2026 inquiete fortement les TPE ; Jean-Christophe Repon
QRY-006 | FETCH | FOUND | SRC-006 | https://www.verreetprotections.com/refondation-de-la-rep-reactions-valobat-capeb-ffb/ | FETCH reactions : Valobat (Herve de Maistre) salue une orientation « viable et perenne » ; FFB (Olivier Salleron) « une belle et grande victoire », « REP de la derniere chance » ; CAPEB obtient de premieres avancees pour les artisans ; maillage, budget revu a la baisse, visibilite 9 mois
QRY-007 | FETCH | FOUND | SRC-007 | https://www.assemblee-nationale.fr/dyn/17/rapports/cion-dvp/l17b2521_rapport-fond | FETCH rapport AN 2521 : proposition de loi adoptee par le Senat visant a reequilibrer la filiere REP PMCB au profit des produits du bois (n 1436), deposee 24/02/2026, examinee puis rejetee en commission du developpement durable
QRY-008 | EXA | NONE trouve : aucune source ne documente un report de l'entree en vigueur de la refondation au-dela du 01/09/2026 ni un maintien de l'agrement 2022 sans redepot ; le calendrier decret/arrete/agrements 01/01/2027 est coherent | - | - | REFUTATION refondation PMCB 01 09 2026 01 01 2027 13 articles : une preuve que la refondation ne serait pas entree en vigueur au 01/09/2026 ou que les eco-organismes n'auraient pas a redeposer leur agrement pour 2027
QRY-009 | EXA | NONE trouve : aucune source ne contredit le chiffre de 85 % d'exoneration potentielle avance par la PPL 2723 ; la charge reportee aux collectivites est au contraire confirmee par Localtis (soutiens conditionnes a la fermeture aux pros) et le communique ministeriel (dechets pros uniquement en dechetteries pro) | - | - | REFUTATION PPL 2723 85 pourcent exonerations materiaux : une preuve chiffree que la distinction matures/non matures n'exonererait pas la majorite des materiaux ni ne reporterait la charge sur les collectivites
QRY-010 | EXA | NONE trouve : aucune source ne documente un maintien des soutiens REP aux dechetteries publiques accueillant des professionnels apres 2028 ; le cahier des charges conditionne explicitement les soutiens a la fermeture de l'acces pros | - | - | REFUTATION soutiens dechetteries publiques 2028 professionnels : une preuve que les eco-organismes maintiendraient leurs soutiens aux dechetteries publiques accueillant des professionnels apres 2028
QRY-011 | EXA | NONE trouve : aucune source ne documente une position favorable de la CAPEB a la fin de la reprise sans frais des petits volumes ; au contraire, la CAPEB et plus de 1000 artisans y sont opposes (26/05/2026) | - | - | REFUTATION CAPEB reprise sans frais 31 12 2026 : une preuve que la CAPEB soutiendrait la fin de la reprise sans frais des petits volumes de dechets tries au 31/12/2026

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.consultations-publiques.developpement-durable.gouv.fr/projets-de-decret-et-d-arrete-ministeriel-a3340.html
SRC-002 | ◈ | fam:B | https://www.ecologie.gouv.fr/presse/refondation-rep-pmcb-filiere-plus-efficace-plus-lisible-economiquement-soutenable
SRC-003 | ◈ | fam:C | https://www.assemblee-nationale.fr/dyn/17/textes/l17b2723_proposition-loi.pdf
SRC-004 | ◈ | fam:D | https://www.banquedesterritoires.fr/refonte-de-la-rep-produits-et-materiaux-de-construction-du-secteur-du-batiment-le-cadre
SRC-005 | ◈ | fam:E | https://www.capeb.fr/actualites/dechets-du-batiment-les-artisans-disent-non-a-la-fin-de-la-reprise-sans-frais
SRC-006 | ◈ | fam:other:presse-acteurs | https://www.verreetprotections.com/refondation-de-la-rep-reactions-valobat-capeb-ffb/
SRC-007 | ◈ | fam:C | https://www.assemblee-nationale.fr/dyn/17/rapports/cion-dvp/l17b2521_rapport-fond

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.consultations-publiques.developpement-durable.gouv.fr/projets-de-decret-et-d-arrete-ministeriel-a3340.html | A,B | 2026-08-30 | Refondation REP PMCB : projet de decret (13 articles) + arrete cahiers des charges mis en consultation au printemps 2026 — entree en vigueur 01/09/2026, nouveaux agrements a deposer pour 01/01/2027 | Textes INSPECTED : (1) decret : reprise distributeurs limitee au maillage, maillage defini par Conseils regionaux a l'echelle departementale (objectif 15 min), prise en charge au premier point de massification (transport chantiers exclu), distinction materiaux matures/non matures (art. 6, matures definis au cahier des charges), entree en vigueur 01/09/2026 ; (2) arrete : remplace les cahiers des charges, matures = mineraux/inertes, metal, bois + platre a compter du 01/01/2027 ; soutien forfaitaire 2 EUR/t pour le tri/tracabilite des matures ; depots d'agrement sous 1 mois apres publication pour poursuivre au 01/01/2027. Communique Lefevre 19/02/2026 : scenario officiel apres 12 mois de concertation (maillage dechetteries pro > distributeurs > dechetteries publiques). | 54577e4d-3aec-4d3b-b621-e2b2e059cbe4
FCT-002 | FACT | ✦ | https://www.assemblee-nationale.fr/dyn/17/textes/l17b2723_proposition-loi.pdf | C,D | 2026-08-30 | PPL 2723 Delautrette/Riotton/Violland : la distinction matures/non matures du gouvernement pourrait exonerer plus de 85 pourcent des materiaux et reporter la charge aux collectivites et contribuables — modele alternatif en trois agrements separes (gravats, bois, second oeuvre) | PPL 2723 INSPECTED (PDF integral) : expose des motifs — les conclusions du moratoire gouvernemental 2025 n'apportent pas de reponse satisfaisante ; la distinction matures/non matures sans definitions claires « pourrait conduire a l'exoneration a plus de 85 % des materiaux de construction aujourd'hui compris dans le dispositif (bois mais aussi platre, beton et autres materiaux inertes) » avec suppression de tout financement de collecte/recyclage, charge « entierement aux collectivites, et donc aux contribuables et petites entreprises du batiment » ; creation de 3 categories d'agrements (gravats, bois, second oeuvre) avec contributions differenciees ; visible fee ; prise en charge operationnelle ou financiere integrale des depots sauvages de materiaux (80 % des depots illegaux) ; contractualisation eco-orgs/collectivites obligatoire au 01/01/2027. | 86bf69c7-397b-4688-9fd9-24c10f1745a5
FCT-003 | FACT | ✦ | https://www.banquedesterritoires.fr/refonte-de-la-rep-produits-et-materiaux-de-construction-du-secteur-du-batiment-le-cadre | B,D | 2026-08-30 | Cout de la REP PMCB divise par deux a l horizon 2028 ; soutiens limitables aux dechetteries publiques a compter de 2028 si la collectivite accepte encore les professionnels — le levier de l exclusion pros devient un conditionnement financier | Localtis 27/04/2026 (INSPECTED) : cout de la REP divise par deux a l'horizon 2028 (900 a 450 MEUR) ; cahier des charges : objectifs de collecte opposables cibles sur les non matures ; les eco-organismes peuvent limiter les soutiens aux dechets des menages pris en charge au niveau des dechetteries publiques a compter de 2028 en l'absence de mesures de la collectivite visant a ne plus accepter les dechets des professionnels — i.e. la refondation CONDITIONNE le soutien des dechetteries publiques a la fermeture de l'acces pros (axe A) ; contrats collectivites signes sous 3 mois ; maillage 15 min ; enveloppe a la performance en cas de non atteinte des objectifs. | f0597a42-2ffb-4967-951e-7a743d6410ad
FCT-004 | FACT | ✦ | https://www.capeb.fr/actualites/dechets-du-batiment-les-artisans-disent-non-a-la-fin-de-la-reprise-sans-frais | E,other:presse-acteurs | 2026-08-30 | CAPEB : plus d un millier d entreprises artisanales repondent a la consultation pour defendre la reprise sans frais des petits volumes de dechets tries — suppression prevue au 31/12/2026 ; FFB salue une victoire (Salleron), Valobat soutient le scenario gouvernemental | Positions INSPECTED : (1) CAPEB (26/05/2026) : >1000 entreprises artisanales ont repondu a la consultation ; la reprise sans frais des petits volumes « n'est pas un avantage, c'est une necessite » ; suppression au 31/12/2026 « inquiete fortement les TPE » ; (2) FFB (Salleron) : « une belle et grande victoire » pour les artisans, « la REP de la derniere chance doit absolument tenir ses promesses » ; (3) Valobat (Herve de Maistre) : salue une orientation « claire, coherente, economiquement viable et perenne » ; (4) Verre&protections 20/02/2026 : CAPEB « obtient de premieres avancees » (reprise sans frais petits volumes jusqu'a fin 2026). — Divergence CAPEB/FFB sur la reprise sans frais. | 155dfaa7-79b8-40b3-a567-65ee3f830bea
FCT-005 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/17/rapports/cion-dvp/l17b2521_rapport-fond | C | 2026-08-30 | PPL Senat 1436 (reequilibrer la REP PMCB au profit du bois) : rapport AN 2521 du 24/02/2026, examinee puis rejetee en commission du developpement durable — premier front parlementaire du conflit matures/bois | Rapport AN 2521 INSPECTED : proposition de loi adoptee par le Senat visant a reequilibrer la filiere REP PMCB au profit des produits du bois (n 1436), rapport depose le 24/02/2026, examinee puis rejetee en commission du developpement durable et de l'amenagement du territoire — le bois, classe mature par le gouvernement (avec metal et inertes, puis platre 2027), fait l'objet d'un front parlementaire (Senat : sortir le bois de la REP ; PPL 2723 : 3e categorie dediee avec contribution tenant compte de l'ecologique ; 30 % des dechets du bois de construction non recycles selon PPL 2723). | 87f18ff9-1b64-4580-b7bc-e4f4bc8519c3
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-003,SRC-004
FCT-003 | SRC-004,SRC-002
FCT-004 | SRC-005,SRC-006
FCT-005 | SRC-007,SRC-003

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-008 | NONE
FCT-002 | QRY-009 | NONE
FCT-003 | QRY-010 | NONE
FCT-004 | QRY-011 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7:AXS-001:QRY-001
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:FCT-001
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:CAU-001
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18:FINALIZATION_BLOCKED

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T18:35:24.774234+00:00","fact_mem":{"FCT-001":"54577e4d-3aec-4d3b-b621-e2b2e059cbe4","FCT-002":"86bf69c7-397b-4688-9fd9-24c10f1745a5","FCT-003":"f0597a42-2ffb-4967-951e-7a743d6410ad","FCT-004":"155dfaa7-79b8-40b3-a567-65ee3f830bea","FCT-005":"87f18ff9-1b64-4580-b7bc-e4f4bc8519c3"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory note MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
