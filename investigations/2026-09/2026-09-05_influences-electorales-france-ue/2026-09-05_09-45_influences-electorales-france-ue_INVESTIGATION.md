ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-0945-influences-electorales-france-ue | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_influences-electorales-france-ue/2026-09-05_09-45_influences-electorales-france-ue_INPUT.txt | SUBJECT_SLUG:influences-electorales-france-ue | SUBJECT_FP:sha256:ed4cb59fee559e421333e8b7337f5860a45b6aa8958fb6e4692ed8bbb400b1a3 | INPUT_SHA256:sha256:f888f576927471d6ea5f77950240912d886b55c6694319f26d56c95a44a3455a
COMPLEXITY:17→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': 'partis, médias et propriétaires, lobbies et registres, think tanks, élus/commissaires, régulateurs (CNCCFP, ARCOM, Commission UE)', 'domains': 'médias/opinion publique, financement politique, lobbying/think tanks, réseaux d’élites, régulation/transparence', 'exclusions': 'ingérence étrangère étatique (run dédié), achat de vote direct (run dédié), corruption/financement occulte (run dédié), triche de scrutin (run dédié)', 'geo': 'France prioritaire, puis UE ; comparaison monde où matérielle', 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': 'corpus web public ; pas d’accès aux documents internes ; ampleur mesurable seulement via études et registres publics', 'object_question': 'Par quels mécanismes, acteurs et canaux documentés l’influence (hors ingérence étrangère étatique, traitée dans un run dédié) s’exerce-t-elle sur les processus électoraux et le fonctionnement démocratique en France et dans l’UE, quelle en est l’ampleur et quelles protections existent ?', 'period': '2017-2026, profondeur historique quand matérielle'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 1. RÉSUMÉ EXÉCUTIF

OBJECT_QUESTION : Par quels mécanismes, acteurs et canaux documentés l'influence s'exerce-t-elle sur les processus électoraux et le fonctionnement démocratique en France et dans l'UE, quelle en est l'ampleur et quelles protections existent ?

Réponse bornée : l'influence sur les élections et la démocratie en France et dans l'UE est un phénomène structurel et documenté, qui s'exerce par quatre mécanismes principaux : (1) la concentration de la propriété des médias d'information entre les mains de groupes industriels (FCT-003, SRC-003) ; (2) des flux financiers massifs de lobbying déclaré auprès des institutions UE, au moins 343 M€/an déclarés par 162 organisations (FCT-001, SRC-005, SRC-008) ; (3) les portes tournantes public-privé, qui offrent un accès privilégié aux décideurs (FCT-005, FCT-006, SRC-006, SRC-007) ; (4) la prolifération des partis et micro-partis dans un système de financement politique sous contrôle public (FCT-004, SRC-004).

Ampleur : des risques significatifs de pluralité du marché médiatique persistent dans tous les États membres de l'UE selon le Media Pluralism Monitor 2025 (FCT-002, SRC-001, SRC-002) ; les contrôles existent (CNCCFP, HATVP, registre de transparence UE, EMFA) mais leur efficacité est partielle et documentée comme limitée (FCT-007, FCT-008, CTRL-001 à CTRL-004).

Verdict distinct sur le lead/source : aucune source n'était fournie (INPUT_KIND=TOPIC) ; LEAD_QUESTION := N/A(NO_INPUT_LEAD) et SOURCE_AUDIT := N/A.

Acteurs : propriétaires de médias (Bolloré/Vivendi, Arnault/UFIPAR, Saadé/CMA CGM, Pinault/Artemis, Bouygues, Dassault — ACT-001 à ACT-006, SRC-003), 162 organisations déclarant un lobbying UE ≥1 M€/an (FCT-001), anciens responsables publics reconvertis (FCT-005, FCT-006), régulateurs (CNCCFP, HATVP, registre UE, EMFA).

Impact : risques pour le pluralisme médiatique (FCT-002), risque reconnu d'influence de l'argent sur le processus électoral (FCT-004, SRC-004), risque de capture réglementaire signalé par les observatoires et la Cour des comptes européenne (SRC-005, SRC-011) ; l'effet direct de ces mécanismes sur les résultats électoraux n'est pas quantifié dans le corpus inspecté (CLM-005, GAP_TYPE=CAUSALITY).

Principaux écarts : lien causal direct propriété des médias → résultats électoraux non établi (GAP_TYPE=CAUSALITY) ; capture réglementaire effective non prouvée (CAU-004, GAP_TYPE=CAUSALITY) ; montants réels de lobbying hors déclarations inconnus (GAP_TYPE=ACCESS) ; aucune étude française quantifiée propriété → vote inspectée (CLM-005).

# 2. MANIPULATION_REPORT

Input : TOPIC (thème « influences sur les démocraties et les élections », France/UE prioritaires), MISSION_MODE=INVESTIGATION, SYMBOL_STAGE=CORPUS_FINAL.

Scores des 15 symboles évalués sur le corpus borné et inspecté (aucun DEFERRED) : Ξ Omission 6 (opacité des chaînes de propriété, dépenses publiques non publiées, sous-déclaration du lobbying — FCT-003, SRC-003 ; FCT-001, SRC-012) ; € Money 7 (343 M€/an lobbying déclaré, 64 M€ aide publique aux partis, concentration financière — FCT-004, FCT-001) ; Λ Framing 4 (effets de cadrage médiatique documentés — FCT-009, SRC-010) ; Ω Inversion 1 (aucune inversion documentée dans le corpus) ; Ψ Sideration 2 (transformation de l'espace public par les réseaux sociaux signalée par la CNCCFP — SRC-004) ; ↕ Vertical power 6 (asymétries structurelles d'accès : badges, réunions, portes tournantes — FCT-001, FCT-005, FCT-006) ; Φ Spectacle 2 ; Σ Semiotics 2 ; Κ Cynicism 3 (écart entre dispositifs de transparence et limites documentées — FCT-008, CTRL-003) ; ρ Resistance 4 (régulateurs, EMFA, presse indépendante — CTRL-001 à CTRL-004) ; κ Subtle influence 4 (architecture d'accès, accréditations PE — FCT-001, FCT-008) ; ⫸ Convergence 5 (indices indépendants convergents : concentration + lobbying + portes tournantes) ; ⚔ Cognitive warfare 1 (aucune évidence d'activité coordonnée organisée dans ce corpus — hors périmètre du run ingérences) ; 🌐 Network 6 (réseaux d'entre-soi et portes tournantes — FCT-005, FCT-006) ; ⏰ Temporal 4 (concentration croissante, cycle électoral 2026-2027 en préparation).

Clusters chargés conformément à SYMBOLS §4 : ICEBERG (Ξ≥5), MONEY (€≥7), POWER (↕≥5), FRAGMENTATION (⫸≥5), NETWORK (🌐≥5). Hypothèse d'analyse : la transparence partielle (registres, comptes) coexiste avec des flux et accès non entièrement traçables ; les scores orientent l'inspection, ils ne prouvent ni intention ni coordination.

# 3. CLUSTERS

ICEBERG (Ξ=6) : omissions documentées — chaînes de propriété complexes et non totalement identifiables (SRC-003), dépenses publiques et fiscales en faveur des médias non toutes publiées (SRC-003), sous-déclaration et sur-déclaration dans le registre de transparence UE (FCT-001, SRC-012). Facteur ICEBERG non calculable (pas de total de référence). Explication innocente testée : complexité des holdings familiaux et absence d'obligation de publication complète. Statut : omissions documentées, pas de dissimulation prouvée.

MONEY (€=7) : flux tracés — payer → véhicule → bénéficiaire pour le lobbying UE (entreprises/associations → registre → institutions UE, ≥343 M€/an déclarés, FCT-001) ; aide publique aux partis (État → partis, 64 M€, FCT-004) ; collecte de dons via micro-partis (non quantifiée, FCT-004). Capture réglementaire : risque signalé (SRC-005, SRC-011), preuve directe absente (CAU-004, GAP_TYPE=CAUSALITY).

POWER (↕=6) : asymétries d'accès documentées — accréditations PE (CEFIC 323 badges, BusinessEurope 295, Insurance Europe 268, ensemble supérieur au nombre de députés — FCT-001, SRC-008), réunions privilégiées (BusinessEurope 467 réunions depuis 2014 — SRC-008), portes tournantes (FCT-005, FCT-006). Alternatives testées : transparence partielle des réunions (élargissement de la publication à ~1 500 responsables — SRC-008).

FRAGMENTATION (⫸=5) : indices indépendants convergents sur l'existence d'une influence structurelle : concentration médiatique (famille E, SRC-003), dépenses de lobbying (familles B et D, SRC-005, SRC-008), portes tournantes (famille B, SRC-006, SRC-007), contrôles imparfaits (famille A, SRC-004, SRC-011). Ratio de convergence : 4 indices indépendants sur 4 applicables (sans compter les sources syndiquées). La convergence oriente l'inspection ; elle n'établit pas de coordination.

NETWORK (🌐=6) : graphe typé partiel — 8 arêtes documentées (carte réseau d'acteurs) ; métriques non calculées (graphe incomplet) ; points de contrôle identifiés : propriété des médias, accès parlementaire, répertoires de lobbying. Endogamie : allers-retours public-privé documentés (FCT-005, FCT-006). Alternatives : liens d'affiliation seule ≠ coordination.

# 4. HERMÉNEUTIQUE

L1 Explicite : les sources affirment une concentration significative des médias d'information français (FCT-003), des dépenses déclarées de lobbying UE d'au moins 343 M€/an (FCT-001), des portes tournantes massives (FCT-005, FCT-006), des contrôles publics étendus mais imparfaits (FCT-004, FCT-007, FCT-008).

L2 Implicite : le discours institutionnel présuppose que la transparence protège le processus électoral de l'influence de l'argent (mission CNCCFP, SRC-004) ; les observatoires présupposent que ressources et accès inégaux produisent une influence disproportionnée (SRC-005, SRC-006).

L3 Structurel : le cadre oppose démocratie délibérative (égalité des voix) et marché de l'information (visibilité financée) ; la concentration médiatique et le lobbying sont traités comme des risques de marché et de gouvernance, pas comme des délits.

L4 Symbolique : les chiffres (343 M€, 3 617 inscrits, 747 partis) portent une charge symbolique de démonstration ; ils restent bornés par leurs définitions (déclarations, registres).

L5 Présupposé : l'information pluraliste et le contrôle public sont supposés être des conditions de la qualité démocratique (SRC-001, SRC-004).

L6 Épistémique : qui produit la preuve — régulateurs (A), observatoires (B), médias (D), universitaires (E) ; les acteurs influents contrôlent les données de propriété (SRC-003) ; le corpus ne contient aucune source locale/dissidente inspectée (limite déclarée).

# 5. FORENSIC REASONING

NOT APPLICABLE : aucune omission de « population cachée » reconstruite ; les omissions documentées (opacité de propriété, sous-déclaration) sont qualitatives et restent des GAP_TYPE=ACCESS/INDEPENDENCE, sans reconstruction quantitative comparable (pas de total de référence inspecté).

# 6. PRISME DIALECTIQUE

P1 (dominant/officiel) : les institutions reconnaissent des risques — MPM 2025 : risques significatifs de pluralité du marché pour tous les États membres (FCT-002) ; CNCCFP : risque accru d'influence de l'argent, coopération Viginum/Tracfin/Arcom (FCT-004, SRC-004) ; HATVP et registre UE : dispositifs de transparence étendus (FCT-007, FCT-008) ; EMFA applicable depuis le 08/08/2025 (FCT-002).

P2 (critique/adversarial) : les observatoires documentent une influence structurelle des intérêts privés — dépenses de lobbying massives et croissantes (FCT-001), portes tournantes comme « arme fatale » d'influence (FCT-005, FCT-006), failles des registres (inscription volontaire, 76 % des inscriptions du haut du registre UE entachées d'erreurs — FCT-008, SRC-012), risque de capture réglementaire (SRC-005).

P3 (arbitrage par les preuves) : les faits des deux côtés coexistent et se limitent mutuellement : mécanismes d'influence réels et documentés (FCT-003, FCT-001, FCT-005, FCT-006) ; contrôles réels mais d'efficacité limitée (FCT-004, FCT-007, FCT-008) ; effet direct sur le vote non quantifié (FCT-009, CLM-005 GAP). Égale force argumentative ≠ poids probatoire égal.

# 7. CHRONOLOGIE

2017 : ouverture du répertoire HATVP des représentants d'intérêts (1er juillet) — base du contrôle du lobbying français (SRC-009). 2017 : constat académique des effets indirects des médias sur le vote (Gerstlé, SRC-010). 2021 : réforme du registre de transparence UE (accord juillet 2021, intégration du Conseil ; >12 000 entités — FCT-008, SRC-011). 2022 : rapport Sénat n° 593 sur la concentration des médias (repéré en découverte, non inspecté). 2023-2024 : prise de contrôle de Lagardère par Vivendi/Bolloré, renforcement de la concentration (FCT-003, SRC-003). 2024 : 3 140 comptes de campagne des législatives anticipées contrôlés par la CNCCFP (FCT-004) ; Cour des comptes européenne : rapport spécial 05/2024 sur le registre de transparence UE (utile mais limité — repéré en découverte, SRC-011 en synthèse). 2024-2025 : 162 organisations déclarent ≥343 M€/an de lobbying UE (février 2025, FCT-001) ; retrait d'Altice du secteur, montée de CMA CGM (FCT-003, SRC-003). 2025 : EMFA applicable le 08/08/2025 (FCT-002) ; MPM 2025 publié (27/06, FCT-002) ; 747 partis soumis au contrôle CNCCFP, aide publique 64 M€ (FCT-004) ; enquête Ombudsman UE sur le pantouflage des agences (repérée en découverte). 2026 : MPM 2026 publié (29/06) avec passage à un système de risque à six niveaux (FCT-002, SRC-002) ; 4 879 comptes de campagne des municipales 2026 à contrôler (FCT-004) ; 3 617 représentants d'intérêts inscrits au répertoire HATVP (septembre, FCT-007) ; préparation de la présidentielle 2027 par la CNCCFP (FCT-004).

# 8. DOMAINES

Médias/opinion (AXS-001, AXS-004, AXS-005) : concentration significative du marché français de l'information, portée par des groupes industriels extérieurs aux médias (FCT-003, SRC-003) ; risques de pluralité du marché dans tous les États membres UE (FCT-002) ; effets indirects des médias sur les électeurs documentés, effets directs limités (FCT-009).

Financement politique (AXS-003) : 747 partis soumis au contrôle CNCCFP en 2025, dont une prolifération de micro-partis ; 64 M€ d'aide publique ; 4 879 comptes municipales 2026 à contrôler (FCT-004, SRC-004).

Lobbying UE et France (AXS-003, AXS-004, AXS-006) : ≥343 M€/an de dépenses déclarées par 162 organisations (FCT-001) ; >12 000 entités au registre UE, inscription volontaire mais avantageuse, contrôles et sanctions existants (FCT-008) ; 3 617 inscrits au répertoire HATVP (FCT-007).

Réseaux d'élites (AXS-005) : portes tournantes documentées en France (33/96 ministres issus de grandes entreprises ; 27/53 ex-ministres retournés au privé — FCT-005) et à Bruxelles (~50 % des effectifs des grands cabinets de lobbying issus des institutions UE ; 6/13 commissaires sortants 2009-2010 vers le privé — FCT-006).

Régulation/transparence (AXS-006, AXS-008) : CNCCFP, HATVP, registre UE, EMFA (CTRL-001 à CTRL-004) ; limites documentées : inscription volontaire, qualité des déclarations critiquée, ressources des autorités souvent inadéquates (FCT-008, SRC-002, SRC-012).

Frontières : la frontière entre influence légale (lobbying déclaré, propriété médiatique) et influence indue (capture, opacité) n'est pas nette ; l'influence étrangère étatique, l'achat de vote, la corruption et la triche de scrutin sont exclus de ce run (runs dédiés).

# 9. RÉSEAU D'ACTEURS

Nœuds et arêtes typés documentés (carte réseau d'acteurs) : propriétaires de médias → contrôle de titres et chaînes (Bolloré/Vivendi → CNews, Europe 1, JDD, Paris Match, Canal+ ; Arnault/UFIPAR → Le Parisien, Les Echos ; Saadé/CMA CGM → présence forte dans les médias d'information ; Pinault/Artemis → Le Point ; Bouygues → TF1 ; Dassault → Le Figaro — FCT-003, SRC-003, ACT-001 à ACT-006) ; anciens responsables publics → grands groupes et lobbies (portes tournantes — FCT-005, FCT-006) ; 162 organisations → institutions UE (lobbying déclaré — FCT-001).

Carte de contrôle (CTRL-001 à CTRL-004) : CNCCFP (comptes de campagne et partis), HATVP (répertoire des représentants d'intérêts), registre de transparence UE (code de conduite, contrôles, sanctions), EMFA (pluralisme, indépendance éditoriale, transparence de propriété). Centralité : non calculée (graphe partiel, définition de graphe explicite requise).

# 10. CHAÎNES / PELOTE

CAUSAL_ROUTE=REQUIRED (la question porte sur des mécanismes affectant un rapport de pouvoir et le fonctionnement démocratique). Quatre arbres, chaîne courte vérifiée > chaîne longue inventée :

CAU-001 (SUPPORTED, ENABLER) : concentration des médias (FCT-003) → les propriétaires nomment les rédacteurs en chef et influencent les lignes éditoriales (SRC-003) → effets indirects sur les électeurs (agenda, cadrage, visibilité — FCT-009). Contre-explication testée : garde-fous éditoriaux (clauses de conscience, chartes) et effets directs limités (Lazarsfeld 1944, FCT-009) — la chaîne reste un ENABLER, pas une causalité directe propriété → vote.

CAU-002 (GAP, GAP_TYPE=CAUSALITY) : financement privé et prolifération des micro-partis (747 en 2025 — FCT-004) → vecteurs de collecte de dons ; le régulateur reconnaît le risque d'influence de l'argent (SRC-004) ; le lien causal direct financement → décision électorale n'est pas prouvé.

CAU-003 (SUPPORTED, ENABLER) : portes tournantes public-privé (FCT-005, FCT-006) → accès privilégié, information, culture d'entre-soi → influence réglementaire et politique des grands groupes (SRC-006 : « l'arme fatale »). Contre-explication testée : règles de refroidissement (2-3 ans commissaires UE, 18 mois président du Conseil européen — FCT-008, SRC-011).

CAU-004 (GAP, GAP_TYPE=CAUSALITY) : lobbying UE (≥343 M€/an déclarés, accréditations, réunions — FCT-001) → accès structurellement inégal → risque de capture réglementaire signalé (SRC-005, SRC-011) ; aucune décision UE liée à une dépense n'est prouvée dans le corpus.

TIMELINE : voir section 7. COUVERTURE : 4 chaînes sur 4 applicables ; 2 soutenues, 2 en GAP de causalité. La provenance des sources n'est pas substituée à la causalité de l'objet.

# 11. CARTE DES PREUVES

Registres machine : les registres complets (registres sémantiques, registre des preuves, registre des faits, carte des sources, registre des réfutations, plan de write-back, matrice de traçabilité, journal des requêtes) sont émis par le rendu déterministe ci-dessous ; cette section ne les duplique pas.

Faits : 9 faits construits (FCT-001 à FCT-009), tous issus de FETCH inspectés (extraits exacts). Deux faits atteignent le tier ✦ (L4) : FCT-001 (lobbying UE déclaré, familles B et D, réfutation sans contradiction — caveat qualité documenté en registre des contradictions CON-001) et FCT-008 (registre de transparence UE, familles A et D, réfutation sans contradiction). Sept faits sont ✧ (L1-L3) : FCT-002 (famille A), FCT-003 (famille E), FCT-004 (famille A), FCT-005 (famille B), FCT-006 (famille B), FCT-007 (famille A), FCT-009 (famille E).

Contradiction : CON-001 — fiabilité des montants déclarés de lobbying UE (12 déclarants suspectés de sur-déclaration sur 175 ; 76 % des inscriptions du haut du registre entachées d'erreurs — SRC-005, SRC-012) ; résolue par re-scope des FCT-001/FCT-008 à « dépenses déclarées » et « inscription volontaire » ; caveat conservé.

Traçabilité : 4 LEDs SATURATED (LED-001 à LED-004) ; 9 axes terminaux (8 SATURATED, 1 N/A sans source) ; 5 claims (4 SATURATED, 1 GAP de causalité) ; 4 chaînes (2 SUPPORTED, 2 GAP) ; 4 contrôles ; 6 actions. Toute référence requête/source résout vers une ligne exécutée (journal des requêtes).

EDI : 0,93 BROAD (cible APEX 0,80) ; dimensions geo 1,0, lang 1,0, strat 0,8, owner 1,0, persp 0,8, temp 1,0 ; perspectives 4/5 (pas de source dissidente inspectée) ; COV 1,0 ; IND 1,0 ; CC N/A ; EDI* 0,98 ; sévérité d'écart 0,0. DIAGNOSTIC, PAS VÉRITÉ.

# 12. CARTE DIALECTIQUE

SCENARIO_A (influence structurelle significative) : concentration + lobbying massif + portes tournantes convergent vers une influence matérielle des intérêts privés sur les processus électoraux et la décision (FCT-003, FCT-001, FCT-005, FCT-006). SCENARIO_B (démocratie résiliente / influence maîtrisée) : les contrôles publics encadrent le financement et la représentation d'intérêts (FCT-004, FCT-007, FCT-008), et l'effet direct des médias sur le vote est limité (FCT-009).

CONVERGENCES : les deux scénarios reconnaissent l'existence de mécanismes d'influence et de risques documentés. DIVERGENCES : l'ampleur et l'effectivité des protections. ARBITRAGE : les mécanismes sont établis (faits ✦/✧) ; l'ampleur nette et l'effet causal sur les résultats électoraux restent non quantifiés (CLM-005, CAU-002, CAU-004 — GAP_TYPE=CAUSALITY).

IMPACT : bénéficiaires documentés : acteurs disposant d'accès et de ressources (ACT-001 à ACT-006, FCT-001) ; coûts/harmes : risques de pluralisme (FCT-002), risque d'influence de l'argent (FCT-004), capture réglementaire potentielle (SRC-005) ; affectés : citoyens-électeurs, journalistes (pression éditoriale — SRC-003), candidats ; réponses : EMFA, registres, contrôle CNCCFP (CTRL-001 à CTRL-004).

Responsabilité : ACT-001 à ACT-006 — actions documentées (propriété, acquisitions), INTENT=UNKNOWN, responsabilité bornée à la propriété ; ROLE ≠ RESPONSIBILITY ; BENEFIT ≠ INTENT.

# 13. PÉRIMÈTRE & LIMITES

Inclusions : mécanismes d'influence en France et dans l'UE (médias, financement politique, lobbying, portes tournantes, régulation), période 2017-2026.

Exclusions (runs dédiés) : ingérence étrangère étatique ; achat de vote direct ; corruption et financement occulte ; triche de scrutin.

Limites d'accès/méthode : corpus web public uniquement ; pas d'accès aux documents internes (registres bruts, déclarations individuelles) — GAP_TYPE=ACCESS ; chaînes de propriété complètes non identifiables — GAP_TYPE=ACCESS/INDEPENDENCE ; aucun registre public exhaustif des cas d'influence ; aucune étude française quantifiée propriété → vote inspectée — GAP_TYPE=CAUSALITY ; source locale/dissidente absente du corpus (EDI persp 4/5) ; dates de certaines sources anciennes (ALTER-EU 2009-2013, Gerstlé 2017) bornées au moment de leur publication.

# 14. ÉTAT DES CONNAISSANCES

Établi (✦) : dépenses déclarées de lobbying UE ≥343 M€/an (162 organisations, février 2025 — FCT-001) ; registre de transparence UE >12 000 entités, inscription volontaire, contrôles et sanctions existants, qualité des déclarations critiquée (FCT-008).

Probable (✧) : risque de pluralité du marché dans tous les États membres UE (FCT-002) ; concentration significative des médias français par des groupes industriels (FCT-003) ; 747 partis sous contrôle CNCCFP, 64 M€ d'aide publique (FCT-004) ; portes tournantes France (33/96 ; 27/53 — FCT-005) et UE (~50 % ; 6/13 — FCT-006) ; 3 617 inscrits au répertoire HATVP (FCT-007) ; effets indirects des médias sur le vote documentés, effets directs limités (FCT-009).

Hypothèses : influence structurelle proportionnelle aux ressources et à l'accès (non prouvée comme causalité — ⁂).

Contesté/partiel : efficacité des contrôles de transparence (dispositifs réels, limites documentées — CLM-004, CON-001).

Inconnu (⁅) : effet net de l'influence sur les résultats électoraux (GAP_TYPE=CAUSALITY) ; montants réels de lobbying hors déclarations (GAP_TYPE=ACCESS) ; capture réglementaire effective (GAP_TYPE=CAUSALITY).

# 15. SUSPICION / VÉRIFICATION

Audit de la source : aucune source fournie (INPUT_KIND=TOPIC) ; SOURCE_AUDIT := N/A.

Vérification : 9 faits réouverts ; 2 faits ✦ avec contre-requête de réfutation exécutée (FCT-001 : requête de réfutation → aucune contradiction sur le montant déclaré, caveat qualité documenté ; FCT-008 : requête de réfutation → corroboration, aucune contradiction) ; aucun fait déclassé ni reclassé en cours de run ; contradiction CON-001 documentée et résolue par re-scope.

Vérifications restantes : fiabilité des déclarations individuelles du registre UE (sans accès au registre brut) ; effet causal propriété → vote (étude française quantifiée manquante) ; capture réglementaire (décision liée à une dépense).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:5|AXS:9|CAU:4|CTRL:4|ACT:6

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kind":"CLAIM","led":"le thème posé affirme l’existence d’influences pesant sur les élections et la démocratie en France et dans l’UE","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005"],"locator":"sujet fourni par l’utilisateur","materiality":"DECISIVE","routes":["EXPAND","LINK"],"source_id":"INPUT","status":"SATURATED"}
LED-002 | {"kind":"CLAIM","led":"les démocraties et élections sont exposées à des mécanismes d’influence structurels","linked_ids":["CLM-001","CLM-005"],"locator":"sujet fourni","materiality":"IMPORTANT","routes":["EXPAND"],"source_id":"INPUT","status":"SATURATED"}
LED-003 | {"kind":"CLAIM","led":"l’influence s’exerce notamment via médias, financement politique, lobbying et réseaux d’élites","linked_ids":["CLM-002","CLM-003","CLM-004"],"locator":"sujet fourni","materiality":"IMPORTANT","routes":["EXPAND","LINK"],"source_id":"INPUT","status":"SATURATED"}
LED-004 | {"kind":"CONTEXT","led":"périmètre géographique : France prioritaire, UE ensuite, reste du monde en comparaison","linked_ids":[],"locator":"sujet fourni","materiality":"CONTEXT","routes":["CONTEXT"],"source_id":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"la concentration de la propriété des médias en France/UE crée une influence matérielle sur l’opinion et les élections","claimant":"thème d’investigation","counter":"effets directs limites sur le vote (Lazarsfeld 1944, Gerstle) ; garde-fous editoriaux","gap":"lien causal direct propriete->resultats electoraux non quantifie dans le corpus inspecte","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SATURATED","support":"FCT-002,FCT-003,FCT-009"}
CLM-002 | {"claim":"le financement privé des partis et campagnes (légal et occulte) influence les décisions électorales et post-électorales","claimant":"thème d’investigation","counter":"controles CNCCFP (4879 comptes municipales 2026 + 3140 legislatives 2024) ; aide publique 64 Me","gap":"influence directe de l’argent sur des decisions electorales non prouvee ; risque documente par le regulateur","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SATURATED","support":"FCT-004"}
CLM-003 | {"claim":"think tanks, lobbies et revolving doors sont des canaux d’influence documentés en FR/UE","claimant":"thème d’investigation","counter":"NONE_FOUND : canaux documentes par toutes les sources inspectees","gap":"-","gap_type":"NONE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-001,FCT-005,FCT-006,FCT-007,FCT-008"}
CLM-004 | {"claim":"les règles de transparence et les régulateurs limitent efficacement l’influence indue","claimant":"thème d’investigation","counter":"caveat qualite declarative (LobbyFacts 76% inscriptions du haut du registre entachees d’erreurs) ; sous-declaration ; inscription volontaire","gap":"efficacite reelle des controles non etablie ; dispositifs existent mais limites documentees","gap_type":"INDEPENDENCE","materiality":"IMPORTANT","status":"SATURATED","support":"FCT-007,FCT-008,CTRL-001,CTRL-002,CTRL-003,CTRL-004"}
CLM-005 | {"claim":"l’influence a un effet mesurable sur les résultats électoraux et la qualité démocratique","claimant":"thème d’investigation","counter":"effets directs limites ; ancrage social des electeurs","gap":"aucune etude francaise quantifiee propriete->vote inspectee dans ce run","gap_type":"CAUSALITY","materiality":"IMPORTANT","status":"GAP","support":"FCT-009"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-017"],"axis":"SCOPE_HISTORY","gap":"evolution documentee 2017-2026 ; inventaire historique non exhaustif","led_clm_links":["LED-001","LED-003"],"question":"Comment les mécanismes d’influence électorale en FR/UE ont-ils évolué (2017-2026) ?","result_ids":["FCT-002","FCT-003","FCT-004","FCT-001"],"sought_objects":"définitions, chronologie, comparaisons, études de cadrage","status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-005","QRY-006","QRY-018"],"axis":"EVIDENCE_CASES","gap":"aucun registre public exhaustif des cas d’influence ; cas documentes via mecanismes et acteurs","led_clm_links":["LED-001"],"question":"Quels cas documentés d’influence sur les élections/démocratie en FR/UE ?","result_ids":["FCT-003","FCT-005","FCT-006"],"sought_objects":"rapports d’enquête, commissions, audits, jugements","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-004","QRY-007","QRY-013","QRY-016","QRY-017","QRY-020"],"axis":"RESOURCES_FLOWS","gap":"montants reels (hors declarations) et depenses publiques medias non toutes publiees","led_clm_links":["LED-003"],"question":"Quels flux financiers d’influence (médias, partis, think tanks) sont documentés ?","result_ids":["FCT-004","FCT-001","FCT-007"],"sought_objects":"déclarations, comptes, registres de transparence","status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-005","QRY-006","QRY-018","QRY-019"],"axis":"MECHANISMS","gap":"mecanismes documentes ; preuve directe de capture reglementaire absente","led_clm_links":["LED-002","LED-003"],"question":"Quels mécanismes (concentration médias, revolving doors, lobbying) produisent l’influence ?","result_ids":["FCT-002","FCT-003","FCT-005","FCT-006","FCT-009","CAU-001","CAU-002","CAU-003","CAU-004"],"sought_objects":"analyses, enquêtes, études de mécanismes","status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-005","QRY-006"],"axis":"ACTORS_RELATIONS","gap":"graphe complet des liens documentes non etabli (sources partielles)","led_clm_links":["LED-003"],"question":"Quels acteurs/réseaux d’influence sont documentés en FR/UE ?","result_ids":["FCT-003","FCT-005","FCT-006","ACT-001","ACT-002","ACT-003","ACT-004","ACT-005","ACT-006"],"sought_objects":"registres, liens documentés, profils","status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-003","QRY-004","QRY-017","QRY-019","QRY-022","QRY-026"],"axis":"RULES_CONTROLS","gap":"efficacite des controles partiellement mesuree ; qualite des declarations critiquee","led_clm_links":["LED-001"],"question":"Quelles règles et contrôles limitent l’influence indue (régulateurs, transparence) ?","result_ids":["FCT-004","FCT-007","FCT-008","CTRL-001","CTRL-002","CTRL-003","CTRL-004"],"sought_objects":"textes, bilans de contrôle, sanctions","status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-002","QRY-018","QRY-023"],"axis":"IMPACT_RESPONSIBILITY","gap":"impact direct sur les resultats electoraux non quantifie (GAP_TYPE=CAUSALITY)","led_clm_links":["LED-001","LED-002"],"question":"Quels effets mesurables de l’influence sur les élections et la qualité démocratique ?","result_ids":["FCT-002","FCT-009","CAU-001","CAU-002","CAU-003","CAU-004"],"sought_objects":"études d’impact, évaluations, indicateurs","status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-019","QRY-023","QRY-024","QRY-026"],"axis":"COUNTER_HYPOTHESES","gap":"contre-hypotheses examinees : controles existent, effets directs limites ; mais limites des controles documentees","led_clm_links":["LED-002"],"question":"L’influence est-elle surestimée ou effectivement maîtrisée ?","result_ids":["FCT-007","FCT-008","FCT-009","CTRL-001","CTRL-002","CTRL-003","CTRL-004"],"sought_objects":"évaluations indépendantes, cas de contrôle efficace, contre-arguments","status":"SATURATED"}
AXS-009 | {"axis":"SOURCE_AUDIT","gap":"AUCUNE_SOURCE_FOURNIE (INPUT_KIND=TOPIC) : audit de source non applicable","led_clm_links":[],"question":"Audit de la source fournie","sought_objects":"aucune source fournie","status":"N/A"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"garde-fous editoriaux (clauses de conscience, chartes), effets directs limites (Lazarsfeld)","from":"concentration des medias d’info (proprietaires industriels)","gap_type":"NONE","link_type":"ENABLER","mechanism":"les proprietaires nomment les redacteurs en chef et influencent les lignes editoriales ; la concentration accroit ce pouvoir","source":"SRC-003,SRC-010","status":"SUPPORTED","to":"influence editoriale puis effets indirects sur les electeurs (agenda, cadrage, visibilite)"}
CAU-002 | {"counter":"controle de 4879 comptes municipales 2026 et 3140 legislatives 2024 par la CNCCFP","from":"financement prive et proliferation des micro-partis","gap":"chaine partiellement etayee : le risque d’influence de l’argent est documente (CNCCFP) mais le lien causal direct financement->decision electorale n’est pas prouve","gap_type":"CAUSALITY","link_type":"ENABLER","mechanism":"la multiplication des partis/micro-partis (747 en 2025) cree des vecteurs de collecte de dons ; l’aide publique (64 M€) et le controle (CNCCFP) encadrent mais le risque d’influence de l’argent est reconnu par le regulateur","source":"SRC-004","status":"GAP","to":"risque d’influence de l’argent sur le processus electoral"}
CAU-003 | {"counter":"regles de refroidissement (2-3 ans commissaires UE, 18 mois president Conseil europeen)","from":"portes tournantes public-prive","gap_type":"NONE","link_type":"ENABLER","mechanism":"les allers-retours ministres/commissaires/hauts fonctionnaires vers le prive offrent acces privilegie, informations et culture d’entre-soi ; arme d’influence documentee","source":"SRC-006,SRC-007","status":"SUPPORTED","to":"influence reglementaire et politique des grands groupes"}
CAU-004 | {"counter":"registre de transparence (>12 000 entites), controles (4973 en 2020), sanctions possibles ; pas de preuve directe de decision capturee","from":"lobbying aupres des institutions UE (depenses declarees, accreditations, reunions)","gap":"acces et depenses documentes ; la capture reglementaire effective (decision liee a une depense) n’est pas prouvee dans le corpus inspecte","gap_type":"CAUSALITY","link_type":"ENABLER","mechanism":"des depenses declarees >=343 M€/an, des milliers de badges PE et de reunions donnent un acces structurellement inegal ; risque de capture reglementaire alerte par les observatoires et la Cour des comptes europeenne","source":"SRC-005,SRC-008,SRC-011,SRC-012","status":"GAP","to":"risque de capture reglementaire de la decision UE"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"controller":"CNCCFP (France)","documented_action":"747 partis soumis au controle ; 4879 comptes municipales 2026 a controler ; 3140 comptes legislatives 2024 controles","fct_src_ids":"FCT-004 (SRC-004)","gap":"efficacite mesuree sur les micro-partis et les flux en ligne non quantifiee","information_input":"depots de comptes, declarations, cooperation Viginum/Tracfin/Arcom","oversight_outcome":"processus electoral protege de l’influence de l’argent (mission declaree) ; proliferation des micro-partis a surveiller","rule_duty_authority":"controle des comptes de campagne et des partis (loi 88-227 et suivantes)"}
CTRL-002 | {"controller":"HATVP (France)","documented_action":"3617 representants inscrits, 127174 activites declarees (09/2026)","fct_src_ids":"FCT-007 (SRC-009)","gap":"exhaustivite des declarations non verifiee ; montants des budgets non tous publies","information_input":"inscriptions et declarations des representants d’interets","oversight_outcome":"transparence des activites de representation d’interets ; perimetre plus restreint que la definition UE (campagnes medias exclues)","rule_duty_authority":"repertoire des representants d’interets (loi Sapin 2, depuis 01/07/2017) ; encadrement du lobbying"}
CTRL-003 | {"controller":"Registre de transparence UE (PE, Conseil, Commission)","documented_action":">12 000 entites inscrites ; 4973 entites controlees en 2020 ; premier retrait de 2 ans (sanction maximale) prononce","fct_src_ids":"FCT-008 (SRC-011,SRC-012)","gap":"inscription non obligatoire ; sanctions rares ; sous-declaration documentee","information_input":"declarations annuelles des entites inscrites","oversight_outcome":"transparence partielle ; qualite des declarations critiquee (LobbyFacts : 76% des inscriptions du haut du registre entachees d’erreurs)","rule_duty_authority":"code de conduite commun, declaration annuelle ; inscription volontaire mais avantageuse"}
CTRL-004 | {"controller":"EMFA - reglement europeen sur la liberte des medias","documented_action":"applicable depuis le 08/08/2025 ; cité par la Commission comme reponse aux risques MPM","fct_src_ids":"FCT-002 (SRC-001,SRC-002)","gap":"effets de la mise en oeuvre non encore mesurables","information_input":"transposition/application par les Etats membres et autorites nationales","oversight_outcome":"mise en oeuvre a evaluer ; EPRA 2026 : ressources financieres et humaines des autorites nationales souvent inadequates","rule_duty_authority":"regles de pluralisme, independance editoriale, transparence de propriete, concentrations, publicite d’Etat"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"prise de controle de Lagardere (2023-2024) ; controle de CNews, Europe 1, JDD ; entites ciblees par les analyses de concentration","intent":"UNKNOWN","name":"Vincent Bollore / groupe Bollore (Vivendi)","responsibility_scope":"propriete de medias ; pas de decision electorale documentee","role":"proprietaire de medias d’information francais via Vivendi (Canal+, Hachette)","source":"SRC-003"}
ACT-002 | {"documented_action":"detention de titres de presse via UFIPAR ; structures de propriete complexes signalees par EurOMo","intent":"UNKNOWN","name":"Bernard Arnault / LVMH (UFIPAR)","responsibility_scope":"propriete de medias","role":"proprietaire de medias via UFIPAR (Le Parisien, Les Echos)","source":"SRC-003"}
ACT-003 | {"documented_action":"presence forte et croissante dans le secteur des medias d’information francais (EurOMo 2025) ; groupe de transport maritime controle par la famille Saade","intent":"UNKNOWN","name":"Rodolphe Saade / CMA CGM","responsibility_scope":"propriete de medias","role":"proprietaire de medias (presence forte et croissante dans les medias d’information)","source":"SRC-003"}
ACT-004 | {"documented_action":"detention de titres de presse via Artemis","intent":"UNKNOWN","name":"Francois Pinault / Artemis","responsibility_scope":"propriete de medias","role":"proprietaire de medias (Le Point)","source":"SRC-003"}
ACT-005 | {"documented_action":"detention de TF1, principale chaine financee par la publicite","intent":"UNKNOWN","name":"Groupe Bouygues","responsibility_scope":"propriete audiovisuelle","role":"proprietaire audiovisuel (TF1)","source":"SRC-003"}
ACT-006 | {"documented_action":"detention du Figaro, fleuron de la presse politique quotidienne nationale","intent":"UNKNOWN","name":"Groupe Dassault","responsibility_scope":"propriete de presse","role":"proprietaire de presse (Le Figaro)","source":"SRC-003"}

SEARCH_ACTIVITY_V1:WEB:14|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND:NO_RELEVANT | mnemolite-mcp | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | SYS-001 | REPAIR_SYS
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-005 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | concentration propriété médias France presse télévision rapport concentration 2024 2025 — découverte : carte PPA Monde Diplomatique, rapport Sénat n°593 (2021-2022), media-ownership.eu France 2025, vie-publique
QRY-002 | WEB | FOUND | - | - | Media Pluralism Monitor 2025 France results risk media concentration — découverte : cmpf.eui.eu France 2026 (risque 46%, marché 71%), communiqué CE MPM 2025
QRY-003 | WEB | FOUND | - | - | CNCCFP rapport 2024 financement vie politique France comptes partis — découverte : cnccfp.fr, rapport activité 2025 (635 partis recensés exercice 2024), data.gouv.fr comptes
QRY-004 | WEB | FOUND | - | - | EU Transparency Register 2024 top lobby spending organisations annual report — découverte : Cour des comptes européenne SR 05/2024, transparency-register rapports annuels, Corporate Europe Observatory
QRY-005 | WEB | FOUND | - | - | revolving doors France UE commissaires hauts fonctionnaires lobbying pantouflage — découverte : TI EU rapport 2017, ALTER-EU, Corporate Europe, multinationales.org, médiateur européen 2025, Cour des comptes UE agences
QRY-006 | WEB | FOUND | - | - | think tanks France financement fondations influence — découverte : multinationales.org (think tanks laboratoires d'influence), vie-publique (influence UE), Cairn sources financement
QRY-007 | WEB | FOUND | - | - | LobbyFacts EU lobbying expenditure top companies — découverte : Corporate Europe (162 sociétés >1M€, ≥343M€ total ; big tech 151M€/an), euronews (CEFIC+Meta plus gros 2024-2025)
QRY-008 | WEB | FOUND | - | - | France influence réseaux élites élections — découverte : Mediapart enquête municipales 2026 ingérence (reportage ultérieurement utile au run ingérences)
QRY-009 | FETCH | FOUND | SRC-001 | https://digital-strategy.ec.europa.eu/en/news/publication-2025-media-pluralism-monitor | FETCH communiqué CE publication MPM 2025 : plupart des États membres en risque moyen ; risques significatifs de pluralité du marché pour tous ; EMFA applicable 08/08/2025
QRY-010 | FETCH | FOUND | SRC-002 | https://www.epra.org/news_items/monitoring-media-pluralism-in-the-eu-highlights-from-the-mpm-2026 | FETCH EPRA MPM 2026 : publié 29/06/2026, système à 6 niveaux de risque, focus indépendance/efficacité des autorités de régulation
QRY-011 | FETCH | FOUND | SRC-003 | https://media-ownership.eu/2025-edition/country-reports/france/ | FETCH EurOMo France 2025 : concentration significative des médias d'info FR ; propriétaires industriels (Bolloré/Vivendi, Arnault/UFIPAR, Saadé/CMA CGM, Pinault/Artemis, Bouygues/TF1, Dassault/Le Figaro) ; opacité chaînes de propriété ; influence des propriétaires sur lignes éditoriales ; nomination politique des conseils audiovisuel public
QRY-012 | FETCH | FOUND | SRC-004 | https://cnccfp.fr/rapport-dactivite-2025/ | FETCH CNCCFP rapport activité 2025 : 747 partis soumis contrôle 2025, 64 M€ aide publique partis, 4879 comptes municipales 2026, 3140 comptes législatives 2024 ; mission = protéger le processus électoral de l'influence de l'argent ; coopération Viginum/Tracfin/Arcom
QRY-013 | FETCH | FOUND | SRC-005 | https://corporateeurope.org/en/2025/02/eus-lobby-league-table | FETCH Corporate Europe lobby league table 24/02/2025 : 162 sociétés/associations ≥1M€ déclarent ensemble ≥343 M€/an de lobbying UE (+13% vs 2024, +33% depuis 2020) ; risque de capture réglementaire ; registre UE imprécis, sous-déclaration
QRY-014 | FETCH | FOUND | SRC-006 | https://www.multinationales.org/fr/enquetes/les-portes-tournantes/ | FETCH Observatoire des multinationales — portes tournantes : plus d'un tiers des ministres Macron (33/96) issus de grandes entreprises ; ~moitié des ex-ministres (27/53) retournés au privé ; pantouflage = arme d'influence ; ex. Barroso/Goldman, Kroes/Uber, Macron/Rothschild
QRY-015 | FETCH | FOUND | SRC-007 | https://www.alter-eu.org/the-revolving-door-in-detail | FETCH ALTER-EU revolving door in detail : ~50% des effectifs des grands cabinets de lobbying bruxellois issus des institutions UE ; 2009-10 : 6/13 commissaires sortants vers privé/lobbying ; règles : interdiction 18 mois commissaires (2011), 12 mois hauts fonctionnaires (2013), failles subsistent
QRY-016 | FETCH | FOUND | SRC-008 | https://www.euronews.com/my-europe/2025/02/24/big-tech-banking-energy-who-are-the-biggest-spenders-on-eu-lobbying | FETCH Euronews 24/02/2025 : 162 plus grandes sociétés/associations ont dépensé 343 M€/an en lobbying UE (fév 2024-fév 2025, +13%, +~33% depuis 2020) ; Meta 9 M€, Microsoft 7 M€ ; CEFIC 323 badges PE, BusinessEurope 295, Insurance Europe 268 (ensemble > nombre de députés) ; BusinessEurope 467 réunions depuis 2014
QRY-017 | WEB | FOUND | - | - | HATVP répertoire représentants d'intérêts France — découverte : vie-publique bilan 2024 (~3 500 inscrits au 01/07/2025, +9%), bilan 2023 (3 215 au 01/07/2024, +12%), budget lobbying ~215 M€ (Cairn RFAP)
QRY-018 | WEB | FOUND | - | - | effet propriété médias sur vote étude académique — découverte : J-PAL (USA), Chapitre 1 Les effets des médias sur le vote (Presses des Mines), The Conversation (les médias font-ils l'élection)
QRY-019 | WEB | FOUND | - | - | régulation lobbying UE évaluation critique registre — découverte : ECA rapport spécial 05/2024 (infos utiles mais limitées), vie-publique synthèse mai 2024, Qatargate renforcement règles PE
QRY-020 | FETCH | FOUND | SRC-009 | https://www.hatvp.fr/le-repertoire/ | FETCH HATVP répertoire : 3 617 représentants d'intérêts inscrits, 3 439 ayant déclaré des activités, 127 174 activités déclarées (sept. 2026)
QRY-021 | FETCH | FOUND | SRC-010 | https://theconversation.com/les-medias-font-ils-lelection-74576 | FETCH The Conversation (Gerstlé, Paris 1) : effets directs limités des médias sur le vote (Lazarsfeld 1944) ; effets indirects puissants : agenda-setting, cadrage, amorçage, visibilité différentielle ; une campagne électorale se joue principalement dans les médias
QRY-022 | FETCH | FOUND | SRC-011 | https://www.hatvp.fr/lobbying/actualites/la-regulation-du-lobbying-au-niveau-de-lunion-europeenne/ | FETCH HATVP — régulation du lobbying UE : registre >12 000 entités, inscription facultative mais avantageuse ; définition large (inclut campagnes médias) ; 2020 : 4 973 entités contrôlées, 1er retrait 2 ans ; règles portes tournantes : 2 ans commissaires, 3 ans présidents Commission, 18 mois président Conseil européen, 1 an cadres supérieurs
QRY-023 | WEB | FOUND:NO_CONTRADICTION | - | - | REFUTATION Media Pluralism Monitor 2025 market plurality risk : aucune critique matérielle trouvée ; corroboration CMPF (pluralité de marché = zone la plus fragile de l'UE, concentration et domination plateformes à très haut risque) ; discussion méthodologique académique (ResearchGate)
QRY-024 | WEB | FOUND:CAVEAT | - | - | REFUTATION EU lobbying 343 M€ : pas de contradiction sur le montant déclaré ; caveat qualité : LobbyFacts identifie 12 déclarants suspectés de sur-déclaration parmi 175 ; étude Parliament Magazine : 76% des inscriptions du haut du registre entachées d'erreurs ; sous-déclaration par ailleurs documentée
QRY-025 | FETCH | FOUND | SRC-012 | https://www.theparliamentmagazine.eu/news/article/eu-transparency-register-inaccurate-say-campaigners | FETCH Parliament Magazine (LobbyFacts) : 76% des inscriptions au sommet du registre de transparence UE entachées d'erreurs — caveat qualité des chiffres déclarés
QRY-026 | WEB | FOUND:NO_CONTRADICTION | - | - | REFUTATION registre transparence UE 12000 entités inscription volontaire : corroboré (Toute l'Europe : >12 600 entités mai 2024 ; révision des règles post-Qatargate) ; aucune contradiction

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://digital-strategy.ec.europa.eu/en/news/publication-2025-media-pluralism-monitor
SRC-002 | ◉ | fam:A | https://www.epra.org/news_items/monitoring-media-pluralism-in-the-eu-highlights-from-the-mpm-2026
SRC-003 | ◉ | fam:E | https://media-ownership.eu/2025-edition/country-reports/france/
SRC-004 | ◈ | fam:A | https://cnccfp.fr/rapport-dactivite-2025/
SRC-005 | ◉ | fam:B | https://corporateeurope.org/en/2025/02/eus-lobby-league-table
SRC-006 | ◉ | fam:B | https://www.multinationales.org/fr/enquetes/les-portes-tournantes/
SRC-007 | ◉ | fam:B | https://www.alter-eu.org/the-revolving-door-in-detail
SRC-008 | ◉ | fam:D | https://www.euronews.com/my-europe/2025/02/24/big-tech-banking-energy-who-are-the-biggest-spenders-on-eu-lobbying
SRC-009 | ◈ | fam:A | https://www.hatvp.fr/le-repertoire/
SRC-010 | ◉ | fam:E | https://theconversation.com/les-medias-font-ils-lelection-74576
SRC-011 | ◈ | fam:A | https://www.hatvp.fr/lobbying/actualites/la-regulation-du-lobbying-au-niveau-de-lunion-europeenne/
SRC-012 | ○ | fam:D | https://www.theparliamentmagazine.eu/news/article/eu-transparency-register-inaccurate-say-campaigners

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://corporateeurope.org/en/2025/02/eus-lobby-league-table | B,D | 2025-02-24 | lobbying-ue-depenses-declarees | 162 organisations declarant >=1Me declarant ensemble >=343Me/an; +13% vs 2024; +33% depuis 2020 | 5f213c75-29c1-4889-990d-f68ee0d8b082
FCT-002 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/publication-2025-media-pluralism-monitor | A | 2026-06-27 | mpm-2025-pluralite-marche-ue | risque moyen UE; risques significatifs pluralite marche tous EM; EMFA applicable 08/08/2025 | 7c2109b9-3d44-416c-8952-fed31fc5655f
FCT-003 | FACT | ✧ | https://media-ownership.eu/2025-edition/country-reports/france/ | E | 2025-12 | concentration-medias-france | concentration significative; groupes industriels controles Le Figaro, Liberation, Le Parisien, BFMTV, CNews, Europe 1, RMC, Les Echos, Le Point, Paris Match | bf1b2218-20cb-4c93-b10f-899086425bb9
FCT-004 | FACT | ✧ | https://cnccfp.fr/rapport-dactivite-2025/ | A | 2026-06 | cnccfp-2025-partis-controle | 747 partis soumis controle; 64Me aide publique; 4879 comptes municipales 2026; 3140 comptes legislatives 2024 | 5f8a3dcf-dcc9-41ba-a1de-177a5f4e4e70
FCT-005 | FACT | ✧ | https://www.multinationales.org/fr/enquetes/les-portes-tournantes/ | B | - | portes-tournantes-france | 33/96 ministres Macron issus de grandes entreprises; 27/53 ex-ministres retournes au prive | 70708d81-2600-425d-b6bd-f8ab610ffed4
FCT-006 | FACT | ✧ | https://www.alter-eu.org/the-revolving-door-in-detail | B | - | revolving-doors-ue | ~50% effectifs grands cabinets lobbying bruxellois issus institutions UE; 6/13 commissaires sortants 2009-10 vers prive | b912f09e-cf5e-47b7-88e7-114fd6641dad
FCT-007 | FACT | ✧ | https://www.hatvp.fr/le-repertoire/ | A | 2026-09-05 | hatvp-repertoire | 3617 inscrits; 3439 avec activites declarees; 127174 activites declarees | 73c00e68-fe95-45b8-8f74-b547c2b66992
FCT-008 | FACT | ✦ | https://www.hatvp.fr/lobbying/actualites/la-regulation-du-lobbying-au-niveau-de-lunion-europeenne/ | A,D | 2021-09-27 | registre-transparence-ue | >12000 entites; inscription volontaire avec avantages; 4973 entites controlees 2020; 1er retrait 2 ans; qualite declarations critiquee | 28f2efac-bec7-48b4-98ea-d452a0821b41
FCT-009 | FACT | ✧ | https://theconversation.com/les-medias-font-ils-lelection-74576 | E | 2017-03-16 | effets-medias-vote | effets directs limites; effets indirects (agenda, cadrage, amorcage, visibilite) puissants; campagne se joue dans les medias | 6c9dab77-ff1b-4d58-aed5-179999aec5a0
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-005,SRC-008
FCT-002 | SRC-001,SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-006
FCT-006 | SRC-007
FCT-007 | SRC-009
FCT-008 | SRC-011,SRC-012
FCT-009 | SRC-010

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-024 | NONE
FCT-008 | QRY-026 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:CONFIRME
FCT-009 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8b
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T08:10:23.183941+00:00","fact_mem":{"FCT-001":"7c2109b9-3d44-416c-8952-fed31fc5655f","FCT-002":"bf1b2218-20cb-4c93-b10f-899086425bb9","FCT-003":"5f8a3dcf-dcc9-41ba-a1de-177a5f4e4e70","FCT-004":"5f213c75-29c1-4889-990d-f68ee0d8b082","FCT-005":"70708d81-2600-425d-b6bd-f8ab610ffed4","FCT-006":"b912f09e-cf5e-47b7-88e7-114fd6641dad","FCT-007":"73c00e68-fe95-45b8-8f74-b547c2b66992","FCT-008":"28f2efac-bec7-48b4-98ea-d452a0821b41","FCT-009":"6c9dab77-ff1b-4d58-aed5-179999aec5a0"},"mnemo_row":"2d714543-896b-4ef8-87d5-11b4eb96604c","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}
ATTEMPT-002 | {"created_at":"2026-09-05T08:31:06.100961+00:00","fact_mem":{"FCT-001":"5f213c75-29c1-4889-990d-f68ee0d8b082","FCT-002":"7c2109b9-3d44-416c-8952-fed31fc5655f","FCT-003":"bf1b2218-20cb-4c93-b10f-899086425bb9","FCT-004":"5f8a3dcf-dcc9-41ba-a1de-177a5f4e4e70","FCT-005":"70708d81-2600-425d-b6bd-f8ab610ffed4","FCT-006":"b912f09e-cf5e-47b7-88e7-114fd6641dad","FCT-007":"73c00e68-fe95-45b8-8f74-b547c2b66992","FCT-008":"28f2efac-bec7-48b4-98ea-d452a0821b41","FCT-009":"6c9dab77-ff1b-4d58-aed5-179999aec5a0"},"mnemo_row":"2d714543-896b-4ef8-87d5-11b4eb96604c","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:2d714543-896b-4ef8-87d5-11b4eb96604c | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
