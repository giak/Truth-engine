# INSEE : architecture d'indépendance, pressions documentées et limites matérielles des chiffres publics (2024-2026)

## RÉSUMÉ EXÉCUTIF

L'INSEE est une direction générale du ministère de l'Économie (MTEFR) qui produit, dans un cadre légal d'indépendance professionnelle inscrit à l'article 1er de la loi n° 51-711 du 7 juin 1951 et contrôlé par l'Autorité de la statistique publique depuis 2008, des chiffres aux effets matériels massifs : populations de référence authentifiées par décret annuel qui conditionnent la DGF et ~350 textes (FCT-002, FCT-003), et indices d'inflation (IPC) qui indexent ~500 Md€ de prestations sociales (~5 Md€ par point d'inflation) et ~1/10 d'une dette publique elle-même indexée (FCT-008, FCT-009). L'enquête n'a trouvé aucune preuve d'intervention politique démontrée sur un chiffre publié ; elle documente en revanche des pressions publiques réelles (Darmanin sur l'enquête de victimation en 2021 ; attaques populistes et coupes budgétaires, Le Monde, novembre 2025) et un contrôle demeurant essentiellement consultatif (CTRL-001, ACT-003). Les controverses les plus concrètes portent sur la production des populations : méthode (rotation 1/5 des communes de moins de 10 000 habitants, sondage annuel de 8 % des logements au-delà) et décalage de référence de trois ans, qui produisent des écarts estimation/dénombrement aux conséquences DGF documentées — Metzing 678 (Insee) contre 791 (dénombrement municipal) en 2024, réponse ministérielle à 719 (réf. 2023) ; Bouzonville, ~100 habitants perdus et 20 000-30 000 € de dotations en moins (FCT-002, FCT-004, FCT-006). La réponse institutionnelle est en cours : la CNERP a recommandé de ramener ce décalage de trois à deux ans, mise en œuvre annoncée par l'Insee pour fin 2026 (FCT-005). Le verdict sur le lead (« investigation sur l'INSEE ») : un input minimal mais exploitable, qui a été élargi vers un objet propre (fonctionnement effectif, pressions, limites des chiffres) ; le lead est SATURATED (LED-001).

SUJET: investigation sur l'INSEE (TOPIC)
OBJET: cadre d'indépendance légal réel, pressions publiques documentées sans preuve d'intervention sur les chiffres, limites matérielles des populations de référence et de l'IPC ; LED-001, AXS-001..009, FCT-001..011
SOURCE: lead utilisateur exploité comme porte d'entrée ; verdict distinct : input TOPIC valide, aucun document source à auditer (LED-001 SATURATED)
MANIPULATION/STRUCTURE: non applicable en tant que verdict ; diagnostic ↕=6 (asymétrie de contrôle des chiffres) et ⏰=5 (décalage N-2/N-3) (MANIPULATION_REPORT)
LIMITE: GAP de profondeur institutionnelle (budget/effectifs, archives des avis ASP) — GAP_TYPE=SCOPE/ACCESS

## MANIPULATION_REPORT

- INPUT_KIND: TOPIC | MISSION_MODE: INVESTIGATION | SYMBOL_STAGE: CORPUS_FINAL
- SYMBOLS (15, échelle 0-10, observés sur corpus borné) : Ξ omission 5 (dénominateurs de la méthode non médiatisés) ; € money 4 (DGF/indexations dérivées) ; Λ framing 2 ; Ω inversion 3 (contestation municipale inverse la charge de preuve) ; Ψ sideration 1 ; ↕ power 6 (monopole public du chiffre, contrôle consultatif) ; Φ spectacle 1 ; Σ sémiotique 0 ; Κ cynisme 2 ; ρ résistance 3 (syndicats, élus, presse) ; κ nudge 0 ; ⫸ convergence 4 (convergence d'impacts DGF indépendants) ; ⚔ guerre cognitive 1 ; 🌐 réseau 3 ; ⏰ temporel 5 (référence N-2/N-3).
- PATTERNS : @PAT[ICEBERG] — facteur total/visible NON COMPUTABLE, dimensions d'omission documentées (rotation, sondage, décalage) ; @PAT[TEMP] — P_ORCH NON ESTIMÉ (pas de modèle nul défendable).
- THREATS : @THR[MYTHO]-like — contestation municipale sans preuve d'erreur Insee (Metzing : les deux chiffres existent, l'écart est une propriété de la méthode) ; contre-check : CR Sénat + réponse ministérielle (SRC-006). @THR[NUDGE] : N/A.
- RHETORICAL : DEM 1 | BF 3 (contestation « méthode obsolète » sans alternative robuste) | NUM 4 (dénominaturs et délais absents du débat public) | AUTH 3 (appel au « vécu du maire ») | FAC 2.
- COMPLEXITY: 11 → APEX. CLUSTERS chargés : POWER, TEMPORAL, ICEBERG, MONEY, NETWORK, CONFIRMATION (routés via SYMBOLS §4 sur ⏰=5, ↕=6, Ξ=5, ⫸=4+€=4 plafonnés par les seuils : ICEBERG/TEMPORAL/POWER chargés, MONEY/NETWORK/CONFIRMATION en lecture d'affinité).
- IMPLICIT: présupposé dominant « chiffre officiel = neutre » ; présupposé concurrent « chiffre municipal = réel ». ASSUMPTIONS: sujet générique → périmètre arrêté sur les controverses matérielles 2024-2026. PRIORITIES: indépendance effective ; populations de référence ; conventions d'indexation. QUERY_GUIDANCE: objets de preuve (textes, CR, notes méthodo, presse locale), pas d'éditorialisation.

## CLUSTERS

- POWER (↕=6) : entrée = monopole légal de production (loi 1951, décret annuel) ; sortie = l'asymétrie existe (l'usager d'un chiffre ne peut le contester que par des voies politiques, pas techniques) ; explication concurrente = toute statistique officielle concentre ce pouvoir ; gap = pas de décision d'attribution individuelle.
- TEMPORAL (⏰=5) : entrée = référence N-2/N-3 des populations ; sortie = effet matériel documenté sur DGF (FCT-004, FCT-006) ; explication concurrente = le délai garantit l'égalité de traitement entre communes recensées des cinq groupes (SRC-003) ; gap = chiffrage national des écarts NON ESTABLISHED.
- ICEBERG (Ξ=5) : entrée = ~350 textes renvoient aux populations (SRC-003) ; sortie = les dimensions d'omission (rotation, sondage, décalage) sont peu médiatisées ; facteur NON COMPUTABLE ; gap = pas de base d'écarts publiée.
- MONEY (€=4, lecture) : entrée = mécanique DGF et indexations ; sortie = chiffrages ~5 Md€/pt et ±0,3 Md€/0,1 pt (FCT-008, FCT-009) ; explication concurrente = les recettes augmentent aussi avec l'inflation (HCFP, ~+10 Md€/pt, SRC-011) ; gap = effet net non tranché ici.
- NETWORK (🌐=3, lecture) : MTEFR → Insee (tutelle), ASP → service statistique public (veille), CNERP → Insee (évaluation) ; pas de centralité calculée (pas de graphe complet).
- CONFIRMATION (κ=0, exclue) : aucun choix d'architecture de décision relevant du cluster.

## HERMÉNEUTIQUE

- L1 explicite : « investigation sur l'INSEE » ; corpus : loi 1951, pages Insee/ASP, CR Sénat, presse.
- L2 implicite : l'input ne définit ni période ni angle ; le choix des axes (indépendance, populations, indexation) est une inférence du run, assumée dans le scope.
- L3 structurel : le cadre 1951/2008 sépare production (Insee), usage (gouvernement/parlement) et contrôle (ASP/CNERP) ; le débat public mélange ces niveaux.
- L4 symbolique : « l'Insee » fonctionne comme emblème de neutralité publique ; les attaques (populistes) comme de la contestation d'institutions.
- L5 présupposé : l'auditoire suppose l'exactitude des chiffres officiels ; les élus supposent la supériorité du dénombrement local.
- L6 épistémique : la production des preuves (bases, méthodes) est exclusivement publique ; les contre-preuves possibles (dénombrements communaux) ne sont pas consolidées ; les données du litige (écart) n'ont pas d'instance d'arbitrage technique documentée.
- Séparation faits/inférence : FCT-001..011 = faits ; toute reconstruction (ex. prévalence nationale des écarts) = NON COMPUTABLE (pas de dénominateur publié).

## FORENSIC REASONING

Ξ=5 → branche forensic exécutée de façon bornée.
- FOUND : cadre légal et institutionnel (FCT-001) ; mécanique populations/DGF (FCT-002, FCT-007) ; chiffrages d'indexation (FCT-008, FCT-009).
- ESTIMATED : l'ordre de grandeur des pertes DGF locales (20-30 k€ pour ~100 habitants, Bouzonville) est documenté cas par cas (FCT-006) ; extension nationale NON COMPUTABLE.
- UNKNOWN (GAP_TYPE=SCOPE) : prévalence nationale des écarts estimation/dénombrement ; archives des avis ASP sur les méthodes ; aucune reconstruction cachée n'est produite faute d'unités comparables.

## PRISME DIALECTIQUE

- P1 dominant/⟐ : « La méthode garantit l'équité entre communes et la robustesse statistique ; les écarts sont des limites connues, le décalage sera réduit » (Insee, Gouvernement — SRC-003, SRC-005, SRC-006).
- P2 critique/⟐̅ : « La méthode pénalise les petites communes en croissance et la statistique publique est sous pression (coupes, délégitimation) » (élus, syndicats, presse — SRC-007, SRC-008, SRC-012, SRC-014).
- P3 arbitrage ◈◉○ : le cadre légal d'indépendance est réel (FCT-001) ; les impacts DGF sont réels et bornés cas par cas (FCT-004, FCT-006) ; les pressions sont réelles mais aucune n'a débouché sur une altération démontrée d'un chiffre publié (cinq contre-requêtes bornées, toutes NONE_FOUND) ; la réforme du décalage est annoncée, non encore appliquée (FCT-005).
- TENSIONS : robustesse vs fraîcheur ; indépendance juridique vs pression publique ; équité intercommunale vs précision communale. SILENCES : absence d'instance de rectification documentée ; absence de statistique publique des écarts. IMPACT : réforme 3→2 ans fin 2026.

## CHRONOLOGIE

- 07/06/1951 — Loi 51-711 : obligation, coordination et secret ; l'art. 1er (version 2010) pose l'indépendance professionnelle (FCT-001, SRC-001).
- 27/02/2002 — Loi démocratie de proximité : objectif de populations annuelles ; recensement par rotation dès 2004 (SRC-003).
- 04/08/2008 — LME art. 144 : création de l'ASP ; décret 2009-250 (SRC-002).
- Fin 2008 — Premier décret annuel d'authentification des populations (SRC-003, SRC-004).
- 20/05/2021 — Déclarations du ministre de l'Intérieur contre l'enquête de victimation ; communiqué CGT-FO-SUD (FCT-010, SRC-013).
- 14/06/2024 — Délibéré ASP après audition de la CNERP (SRC-017).
- 24/06/2025 — QO Sénat (Mizzon) : cas Metzing 678/791 ; réponse Ferracci (réf. 2023 : 719) (FCT-004, SRC-006).
- 21/11/2025 — Le Monde : statistiques publiques attaquées par les populistes et soumises aux coupes (FCT-011, SRC-014).
- 26/12/2025 — Décret n° 2025-1362 : authentification des populations de référence 2023 (SRC-021).
- 11/02/2026 — Réponse QO 10864 : recommandation CNERP 3→2 ans, application fin 2026 (FCT-005, SRC-005).
- 08/04/2026 — FIPECO actualise l'impact de l'inflation (±0,3 Md€/0,1 pt) (FCT-009, SRC-011).
- 10/09/2026 — Note Insee : croissance 2026 révisée à 0,4 % (contexte de pression sur les prévisions) (SRC-015).

## DOMAINES

- SOURCE_AUDIT (AXS-001, SATURATED) : le lead n'a pas de source documentaire à auditer (TOPIC) ; le cadre légal de l'institution est audité : loi 1951 + ASP (FCT-001). Traces QRY/SRC dans les registres machine.
- SCOPE_HISTORY (AXS-002, SATURATED) : du recensement général aux populations de référence annuelles (2002→2008→2024, terminologie « populations de référence » recommandée par l'ASP, concept « populations légales » clos le 30/12/2024) (FCT-002, FCT-003).
- EVIDENCE_CASES (AXS-003, SATURATED) : Metzing (678/791, réf. 719) ; Bouzonville (−100 hab. → 20-30 k€) ; Aiglun (−28 % de dotation en 4 ans, −26 k€) (FCT-004, FCT-006).
- RESOURCES_FLOWS (AXS-004, SATURATED) : chiffres → dotations et indexations ; ~5 Md€/pt de prestations ; dette indexée ~1/10 (FCT-008, FCT-009).
- MECHANISMS (AXS-005, SATURATED) : mécanique population DGF (Insee + rés. secondaires + caravanes ; écrêtement PF>85 % ; CPS→EPCI LF2024) (FCT-007).
- ACTORS_RELATIONS (AXS-006, SATURATED) : MTEFR (tutelle), ASP (veille, 9 membres), CNERP (évaluation), CNIS (concertation) (FCT-001, FCT-005).
- RULES_CONTROLS (AXS-007, SATURATED) : avis ASP, audition CNERP, recommandations ; pouvoir de sanction non documenté (CTRL-001..003).
- IMPACT_RESPONSIBILITY (AXS-008, SATURATED) : pertes DGF documentées ; pressions publiques documentées ; responsabilité individuelle non établie au-delà des actions (ACT-001..003).
- COUNTER_HYPOTHESES (AXS-009, SATURATED) : imprécision statistique inhérente ≠ pression ; indexation = choix législatif ≠ méthode IPC ; aucune réfutation des faits retenus (registre REFUTATION machine : toutes NONE_FOUND).

## RÉSEAU D'ACTEURS

- ACTOR_NETWORK_MAP (arêtes typées, sources) : MTEFR —tutelle→ Insee (permanent, FCT-001) ; ASP —veille indépendance→ service statistique public (depuis 2008, FCT-001) ; CNERP —évaluation→ Insee/recensement (continu, FCT-005) ; syndicats CGT/FO/SUD —alerte publique→ direction/affaires publiques (2021, FCT-010) ; sénateurs/maires —contestation parlementaire→ Gouvernement/Insee (2025-2026, FCT-004/FCT-005). Pas de métrique de centralité (graphe non exhaustif).
- CONTROL_MAP (CTRL-001..003) : ASP (avis/saisines ; sanction non documentée — gap) ; CNERP/groupe de travail (rapports, recommandation 3→2 ans ; application effective à vérifier 2026-2027) ; Insee (traitement des contestations via directions régionales ; procédure formelle non documentée — gap).

## CHAÎNES / PELOTE

- OBJECT_CAUSALITY — CAU-001 ENABLER : méthode (rotation 1/5, sondage 8 %, référence N-2/N-3) ⇒ écarts estimation/dénombrement (Metzing 678 vs 791) (SRC-003, SRC-006).
- CAU-002 CAUSE : écart de population estimée ⇒ perte de dotations (population DGF = Insee + rés. secondaires + caravanes) (SRC-009, SRC-005 ; FCT-006).
- CAU-003 CAUSE : délai de référence de 3 ans ⇒ chiffres obsolètes pour communes en croissance ⇒ recommandation CNERP 3→2 ans (SRC-005, SRC-007).
- CAU-004 ENABLER : choc inflation 2021-2024 ⇒ indexations automatiques IPC ⇒ sensibilité accrue des comptes publics à la mesure IPC (contre : recettes aussi inflationnistes, ~+10 Md€/pt) (SRC-010, SRC-011).
- Alternatives testées : aucune chaîne alternative défendable n'émerge du corpus ; « méthode obsolète » (élus) reste non démontrée comme erreur (c'est un compromis documenté).
- Couverture : 4/4 arbres supportés ; aucun GAP causal non typé. SOURCE_PROVENANCE (généalogie du lead) : distincte, LED-001 SATURATED.

## CARTE DES PREUVES

- LEAD_COVERAGE : LED-001 SATURATED (routes EXPAND ; tentatives tracées dans REQUEST_LOG machine ; FCT-001/002/004/005/008/010).
- OBJECT_COVERAGE : tous les DECISIVE/IMPORTANT EXPAND/LINK mènent à l'OBJECT_QUESTION ; aucune branche AUDIT-only. INVESTIGATION_MAP : AXS-001..009 SATURATED avec ATTEMPT_IDS (registres machine).
- CLAIM_REGISTRY : CLM-001..008 (support/counter/gap explicites ; CLM-007 gap typé SCOPE ; aucune contradiction matérielle non résolue).
- FACT_REGISTRY : FCT-001..011 serialisés par le runtime (bloc machine) ; 1 seul fait ✦ (FCT-008, familles A+D), 10 faits ✧ appuyés.
- Réfutations : 5 faits appuyés ont fait l'objet d'une contre-requête bornée, toutes NONE_FOUND (registre machine).
- Persistance mémoire : FCT-008 éligible CONFIRME ; les 10 autres faits éligibles VERIFIE (plan writeback machine).
- EDI : EDI=0.49 (raw 0.64 − pénalité POWER_BLOC_CONCENTRATION 0.15) → bande LIMITED (cible APEX .80 non atteinte : corpus dominé par la famille A) ; COV 9/9 axes ; IND 15 SRC/4 familles dérivées ; CC N/A ; EDI* ≈ 0.53. DIAGNOSTIC_NOT_TRUTH.

## CARTE DIALECTIQUE

- SCENARIO_A (institutionnel) : le système fonctionne ; les limites sont connues et corrigées (réforme du décalage). SCENARIO_B (critique) : la méthode blesse des communes et la pression s'accroît ; le contrôle est trop faible. CONVERGENCES : la réforme du décalage est demandée par les deux camps et acceptée par le Gouvernement. DIVERGENCES : caractère « d'erreur » ou de « compromis » des écarts. UNRESOLVED : prévalence nationale des écarts ; archives des avis ASP. SHARED_SILENCES : instance de rectification communale.
- IMPACT (résumé) : communes rurales (DGF), bénéficiaires de prestations, contribuables ; voir IMPACT_MAP. RESPONSIBILITY_MAP : ACT-001 (Ferracci : annonce de mise en œuvre), ACT-002 (CNERP : recommandation, intent PROVEN), ACT-003 (Darmanin : déclarations publiques, intent UNKNOWN) ; BENEFIT≠INTENT, ROLE≠RESPONSIBILITY respectés.

## PÉRIMÈTRE & LIMITES

- Inclus : architecture légale/institutionnelle ; populations de référence et litiges DGF ; indexations IPC ; pressions documentées 2021-2026. Exclus : politique générale de la statistique publique hors INSEE ; conjoncture courante.
- Accès/méthode : Légifrance 403 head_blocked (loi 1951 lue via texte consolidé doctrine.fr) ; Le Monde paywall (lead non inspecté, FCT-011 étiqueté comme tel) ; PDF Insee (fiche précision) bot-inaccessibles ; budget/effectifs et archives ASP non investigués en profondeur → GAP_TYPE=SCOPE/ACCESS.
- Limite majeure : sujet générique ; l'angle (indépendance, populations, indexation) est un choix documenté du run, pas une demande explicite.

## ÉTAT DES CONNAISSANCES

- KNOWN (✦) : coût indexation ~5 Md€/pt et dette indexée ~1/10 (FCT-008).
- PROBABLE (✧) : cadre d'indépendance et mécaniques (FCT-001..007) ; impacts DGF locaux (FCT-006) ; pressions publiques (FCT-010, FCT-011).
- CLAIMED (⁕) : « méthode obsolète » des élus (non prouvée comme erreur) ; « décrédibilisation » par les populistes (paywall non inspecté).
- HYPOTHESES (⁂) : aucune retenue au-delà des alternatives documentées.
- CONTESTED (⊗) : aucun conflit matériel non résolu dans le corpus.
- UNKNOWN (⁅) : prévalence nationale des écarts ; budget/effectifs ; archives ASP (GAP_TYPE=SCOPE/ACCESS).
- REFUTED (❧) : aucune proposition du corpus n'est réfutée dans son périmètre.

## SUSPICION / VÉRIFICATION

- Audits de source : 15 FETCH observés et liés aux sources retenues ; 5 contre-requêtes REFUTATION ciblées → NONE_FOUND pour tous les faits ✦/✧ retenus.
- STATUS_DELTA : FCT-004 et FCT-005 évalués ✧ (famille A unique ; la corroboration interne Sénat ne compte pas comme seconde famille) — honnêteté du tier.
- Contrôles non résolus : application effective de la réforme fin 2026 (FCT-005) ; contenu intégral du Monde (paywall) ; sanctions éventuelles de l'ASP.

## SOURCES

- SRC-001 (◈, fam A) — Loi n° 51-711 du 7 juin 1951, art. 1er (texte consolidé) — https://www.doctrine.fr/l/texts/lois/JORFTEXT000000888573
- SRC-002 (◈, fam A) — Autorité de la statistique publique, présentation — https://www.autorite-statistique-publique.fr/presentation/
- SRC-003 (◈, fam A) — Insee, le recensement de la population (méthode, rotation, sondage) — https://www.insee.fr/fr/information/2553979
- SRC-004 (◈, fam A) — Insee, définition « populations légales » (concept clos 30/12/2024) — https://www.insee.fr/fr/metadonnees/definition/c1999
- SRC-005 (◈, fam A) — Sénat, réponse à la QO 10864 (CNERP, décalage 3→2 ans) — https://www.senat.fr/questions/base/2026/qSEQ26010864S.html
- SRC-006 (◈, fam A) — Sénat, CR séance du 24/06/2025 (cas Metzing) — https://www.senat.fr/cra/s20250624/s20250624_0.html
- SRC-007 (◉, fam C) — maire-info, CNERP et populations de référence — https://www.maire-info.com/imprimer2.php?param=29467
- SRC-008 (◉, fam C) — Moselle.tv, Bouzonville : perte d'une centaine d'habitants, ~30 000 € de dotations — https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/
- SRC-009 (◈, fam A) — collectivites-locales.gouv.fr, DGF des communes (mécanique population) — https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes
- SRC-010 (◈, fam A) — Trésor-Éco, « Finances publiques : une inflation qui rapporte » (2022) — https://www.tresor.economie.gouv.fr/Articles/2022/07/05/finances-publiques-une-inflation-qui-rapporte
- SRC-011 (◉, fam D) — FIPECO, impact de l'inflation sur le déficit public (2026) — https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public
- SRC-012 (◉, fam C) — CGT, fiche pouvoir d'achat : quel indicateur d'inflation, pour quel usage — https://analyses-propositions.cgt.fr/fiche-pouvoir-dachat-6-linflation-de-quel-indicateur-parle-et-pour-quel-usage
- SRC-013 (◈, fam C) — Solidaires Finances Publiques, communiqué des syndicats de l'Insee après les propos de Darmanin (2021) — https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/solidaires-finances/4163-communique-des-syndicats-de-l-insee-suite-aux-propos-de-darmanin.html
- SRC-014 (◉, fam C) — Le Monde, « Attaquées par les populistes et soumises aux coupes budgétaires, les statistiques publiques en pleines turbulences » (21/11/2025, paywall) — https://www.lemonde.fr/economie/article/2025/11/21/attaquees-par-les-populistes-et-soumises-aux-coupes-budgetaires-les-statistiques-publiques-en-pleines-turbulences_6654238_3234.html
- SRC-015 (○, fam C) — franceinfo, l'Insee abaisse sa prévision de croissance 2026 à 0,4 % (10/09/2026) — https://www.franceinfo.fr/economie/croissance/l-insee-abaisse-fortement-sa-prevision-de-croissance-pour-la-france-en-2026-de-0-7-a-0-4_8186732.html
- SRC-016 (◈, fam A) — Légifrance, loi 51-711 art. 1er (403 head_blocked ; trace FETCH) — https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540
- SRC-017 (◈, fam A) — ASP, délibéré du 14/06/2024 après audition CNERP (PDF) — https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/06/Delibere-Cnerp.pdf
- SRC-018 (◈, fam A) — CNIS, commission d'évaluation du recensement (CNERP) — https://www.cnis.fr/commissions/evaluation-du-recensement-de-la-population-cnerp/
- SRC-019 (◉, fam E) — HAL (archive ouverte), document académique sur le recensement — https://insee.hal.science/hal-05307957/document
- SRC-020 (◈, fam A) — Insee, fiche précision du recensement (PDF bot-inaccessible) — https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf
- SRC-021 (◈, fam A) — Insee, populations de référence 2023 (décret n° 2025-1362 du 26/12/2025) — https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011
- SRC-022 (◉, fam C) — Wikipédia, Institut national de la statistique et des études économiques — https://fr.wikipedia.org/wiki/Institut_national_de_la_statistique_et_des_%C3%A9tudes_%C3%A9conomiques
- SRC-023 (◈, fam A) — Insee, page institutionnelle (gouvernance) — https://www.insee.fr/fr/information/4174951
