ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260922-1517-insee | PARENT_RUN_ID:NONE | AS_OF:2026-09-22
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-22_insee/2026-09-22_15-17_insee_INPUT.txt | SUBJECT_SLUG:insee | SUBJECT_FP:sha256:4c76cc98b3f0d4b0347102de9b8caf7741f3d50d9a0c58d5d4674fe537dc4d9a | INPUT_SHA256:sha256:4c76cc98b3f0d4b0347102de9b8caf7741f3d50d9a0c58d5d4674fe537dc4d9a
COMPLEXITY:11→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['INSEE', 'MTEFR', 'ASP', 'DGCL', 'CNERP', 'CNIS', 'communes'], 'domains': ['statistique publique', 'finances locales', 'indexation'], 'exclusions': ['politique générale de la statistique publique hors INSEE', 'conjoncture macroéconomique courante'], 'geo': 'France métropolitaine + outre-mer', 'lead_question': "Que dit le sujet utilisateur « investigation sur l'INSEE » et l'input est-il fiable ?", 'limits': 'sujet générique: axes finaux selon matériel trouvé', 'object_question': "Quel est le fonctionnement effectif de l'INSEE en 2024-2026 : architecture légale/institutionnelle, production des populations légales, conventions d'indexation, pressions et indépendance ?", 'period': '2024-2026 (contexte 1951-2008)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
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
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:8|AXS:9|CAU:4|CTRL:3|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempts":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"],"evidence":["FCT-001","FCT-002","FCT-004","FCT-005","FCT-008","FCT-010"],"kinds":["ENTITY"],"lead":"investigation sur l'INSEE (TOPIC: l'institution INSEE — fonctionnement, indépendance effective, pressions/intérêts, controverses matérielles 2024-2026: populations légales, conventions d'indexation)","materiality":"DECISIVE","routes":["EXPAND"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La conception, la production et la diffusion des statistiques publiques sont effectuées en toute indépendance professionnelle (loi 51-711 du 7 juin 1951, art.1 ; ASP créée par la LME du 4 août 2008, décret 2009-250).","claimant":"loi 1951 / ASP","counter":"aucune modification du cadre depuis 2008 trouvée ; des incidents de pression (Darmanin 2021, coupes, attaques populistes) documentés","gap":"écart règle/usage documenté via CTRL/ACT","materiality":"DECISIVE","status":"SUPPORTED","support":"SRC-001,SRC-002"}
CLM-002 | {"claim":"Le dispositif de recensement (loi 2002-276 ; décrets 2003-485, 2019-1302) produit chaque année des populations de référence authentifiées par décret depuis 2008 ; rotation 1/5 des communes <10k, sondage 8%/an des logements >=10k ; ~350 textes y renvoient.","claimant":"INSEE","counter":"QRY-025 NONE_FOUND (aucune invalidation légale ou CNP)","gap":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"SRC-003,SRC-004,SRC-013"}
CLM-003 | {"claim":"À Metzing, Insee 678 hab. (2024) vs dénombrement municipal 791 ; réponse ministérielle : population de référence 719 (réf. 2023).","claimant":"Sénat (QO Mizzon) / Gouvernement","counter":"QRY-022 NONE_FOUND","gap":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"SRC-006"}
CLM-004 | {"claim":"Le décalage de référence (3 ans effectifs) est la principale difficulté soulevée ; la CNERP recommande 3->2 ans, mise en oeuvre annoncée fin 2026.","claimant":"CNERP / Gouvernement (Ferracci)","counter":"groupe de travail : un raccourcissement à 1 an dégraderait trop les résultats","gap":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"SRC-005,SRC-006,SRC-007"}
CLM-005 | {"claim":"Les écarts estimations/dénombrement ont des impacts DGF documentés (Metzing ; Bouzonville 20-30 k€ ; Aiglun -26 k€ / -28% sur 4 ans).","claimant":"presse locale + Sénat","counter":"aucune","gap":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":"SRC-006,SRC-008"}
CLM-006 | {"claim":"1 point d'inflation coûte ~5 Md€ de prestations sociales indexées ; ~1/10 de la dette est indexée (±0,1% prix => ±0,3 Md€ d'intérêts).","claimant":"DG Trésor + FIPECO","counter":"QRY-023 NONE_FOUND ; recettes aussi inflationnistes (~+10 Md€/pt, HCFP)","gap":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":"SRC-010,SRC-011"}
CLM-007 | {"claim":"Des pressions publiques sur la statistique publique existent : Darmanin (victimation, mai 2021), attaques populistes + coupes budgétaires (Le Monde, nov. 2025).","claimant":"syndicats CGT-FO-SUD + presse","counter":"aucune démonstration d'une intervention effective sur les chiffres","gap":"type SCOPE","materiality":"IMPORTANT","status":"SUPPORTED","support":"SRC-012,SRC-014"}
CLM-008 | {"claim":"Aucune preuve d'intervention politique démontrée sur un chiffre INSEE publié ; les protections légales n'ont pas été contournées dans le corpus examiné.","claimant":"analyse","counter":"pressions publiques documentées (CLM-007)","gap":"impossibilité de prouver un négatif ; corpus limité en profondeur","materiality":"IMPORTANT","status":"SUPPORTED","support":"QRY-022,QRY-023,QRY-024,QRY-025"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-002","QRY-007","QRY-008","QRY-024"],"axis":"SOURCE_AUDIT","links":"LED-001","question":"Quelle est l'architecture légale et institutionnelle de l'INSEE (loi 1951, décret 2009-918, tutelle, autorité de la statistique publique) et les controverses matérielles 2024-2026 sur les populations légales et les conventions d'indexation ?","result_ids":[],"sought_objects":"texte loi 1951; décret 2009-918; décret annuel populations légales 2026; pages officielles INSEE/DGCL; notes méthodologiques","status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-009","QRY-010","QRY-025"],"axis":"SCOPE_HISTORY","links":"LED-001","question":"Comment la production des populations légales a-t-elle évolué (recensement rénové 2004+, rotation 1/5 communes <10k, sondage 8% adresses >=10k, décret annuel depuis 2008) et quelles critiques de fiabilité (CNERP, cas Metzing) ?","result_ids":[],"sought_objects":"pages méthodo INSEE recensement; rapport CNERP 2024; documentation écart Metzing","status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-003","QRY-013","QRY-014","QRY-022"],"axis":"EVIDENCE_CASES","links":"LED-001","question":"Quels cas documentés d'écarts estimation/dénombrement et d'impacts concrets (Metzing 678 vs 791, DGF) existent 2024-2026 ?","result_ids":[],"sought_objects":"courrier préfet Moselle; série OFGL Metzing; articles presse locale; réponse ministérielle","status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-017","QRY-018"],"axis":"RESOURCES_FLOWS","links":"LED-001","question":"Quels flux financiers/organisationnels dépendent des chiffres INSEE (DGF ~5 MdE part population, prestations indexées ~5 MdE/pt IPC, dette indexée) ?","result_ids":[],"sought_objects":"notes DGCL dotations; PLF/RFF; chiffres indexation prestations","status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-016","QRY-004","QRY-023"],"axis":"MECHANISMS","links":"LED-001","question":"Par quels mécanismes les chiffres INSEE affectent-ils décisions et transferts (DGF écrêtage 85%, CPS EPCI, conventions d'indexation, dette indexée) ?","result_ids":[],"sought_objects":"mécanique DGF; mécanique indexation; dossiers législatifs conventions","status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-005","QRY-020","QRY-006"],"axis":"ACTORS_RELATIONS","links":"LED-001","question":"Qui contrôle/dépend d'INSEE (MTEFR, ASP, CNIS, CNP, autorité statistique publique) et quelles pressions documentées ?","result_ids":[],"sought_objects":"organigramme; textes gouvernance; déclarations dirigeants; articles presse","status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-002","QRY-008","QRY-021","QRY-024"],"axis":"RULES_CONTROLS","links":"LED-001","question":"Quels contrôles protègent l'indépendance et la qualité (ASP 9 membres, CNP, avis méthodologiques, commissions) et comment ont-ils réagi aux controverses ?","result_ids":[],"sought_objects":"loi 1951 art.1; avis ASP/CNP; rapports CNERP/CNIS","status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-014","QRY-022","QRY-023"],"axis":"IMPACT_RESPONSIBILITY","links":"LED-001","question":"Quels impacts mesurés des choix méthodologiques INSEE (DGF communes pénalisées, indexation prestations, dette) et qui en porte responsabilité documentée ?","result_ids":[],"sought_objects":"cas Metzing; chiffrages indexation; débats parlementaires","status":"SATURATED"}
AXS-009 | {"attempt_ids":["QRY-022","QRY-023","QRY-024","QRY-025","QRY-026"],"axis":"COUNTER_HYPOTHESES","links":"LED-001","question":"Quelles explications alternatives aux critiques (imprécision inhérente au sondage vs pression politique ; conventions d'indexation vs choix budgétaire) et quelles réfutations ?","result_ids":[],"sought_objects":"défenses méthodo INSEE; contre-analyses; réfutations des thèses de pression","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"aucune alternative robuste au-delà de -1 an (groupe de travail)","from":"Méthode (rotation 1/5, sondage 8%, référence N-2/N-3)","link_type":"ENABLER","mechanism":"estimation statistique décalée et entachée d'erreur pour petites communes en croissance","source":"SRC-003,SRC-006","status":"SUPPORTED","to":"écarts estimation/dénombrement (Metzing 678 vs 791)"}
CAU-002 | {"counter":"-","from":"Écart population estimée","link_type":"CAUSE","mechanism":"population DGF et dotations indexées sur le chiffre authentifié","source":"SRC-009,SRC-005","status":"SUPPORTED","to":"perte de dotations (Bouzonville 20-30 kEUR ; Aiglun -26 kEUR/-28% en 4 ans)"}
CAU-003 | {"counter":"-","from":"Délai de référence 3 ans","link_type":"CAUSE","mechanism":"chiffres obsolètes pour communes à forte croissance","source":"SRC-005,SRC-007","status":"SUPPORTED","to":"recommandation CNERP 3->2 ans, application fin 2026"}
CAU-004 | {"counter":"effet symétrique: les recettes augmentent aussi avec l'inflation (HCFP ~+10 MdEUR/pt)","from":"Choc inflation 2021-2024","link_type":"ENABLER","mechanism":"indexations automatiques IPC (prestations ~5 MdEUR/pt ; dette indexée ~1/10 => 3 MdEUR/pt)","source":"SRC-010,SRC-011","status":"SUPPORTED","to":"sensibilité accrue des comptes publics à la mesure IPC"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"action":"avis publics ; recommandation terminologie populations de référence ; audition CNERP (23/05/2024)","controller":"Autorité de la statistique publique (9 membres)","gap":"pouvoirs de sanction non documentés","information":"avis, saisines, audits qualité","oversight":"aucune sanction directe documentée ; avis moralement opposables","rule":"loi 1951 art.1 (indépendance professionnelle) + décret 2009-250","source":"SRC-002"}
CTRL-002 | {"action":"rapport fin 2024 favorable à -1 an ; recommandation 3->2 ans annoncée 2025-2026","controller":"CNERP / groupe de travail (CNIS)","gap":"application effective à vérifier 2026-2027","information":"rapports du groupe de travail, auditions ASP","oversight":"mise en oeuvre annoncée par le Gouvernement pour fin 2026","rule":"évaluation continue du recensement (CNERP rattachée au CNIS)","source":"SRC-007,SRC-005"}
CTRL-003 | {"action":"réponses par voie régionale ; aucune rectification individuelle documentée dans le corpus","controller":"Insee (direction générale)","gap":"procédure de contestation formelle non documentée","information":"dénombrements municipaux, données fiscales, RIL","oversight":"CNERP/ASP","rule":"traitement des contestations communales via directions régionales","source":"SRC-005,SRC-006"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"annonce de la mise en oeuvre du raccourcissement du décalage à 2 ans fin 2026 ; chiffres Metzing (678/791/719)","intent":"UNKNOWN","name":"M. Marc Ferracci (ministre chargé de l'industrie et de l'énergie)","responsibility_scope":"annonce de mise en oeuvre","role":"ministre répondant aux questions du Sénat","source":"SRC-006"}
ACT-002 | {"documented_action":"recommandation de réduction du décalage 3->2 ans","intent":"PROVEN","name":"CNERP (Commission nationale d'évaluation du recensement de la population)","responsibility_scope":"recommandation méthodologique","role":"organe d'évaluation (CNIS)","source":"SRC-005,SRC-007"}
ACT-003 | {"documented_action":"déclarations publiques invalidant sans arguments les enquêtes de victimation (mai 2021)","intent":"UNKNOWN","name":"M. Gérald Darmanin (ministre de l'Intérieur, 2021)","responsibility_scope":"pressions publiques documentées","role":"membre du gouvernement","source":"SRC-012"}

SEARCH_ACTIVITY_V1:WEB:11|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"EMPTY","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"EMPTY"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | OK:health-200 | mnemolite/health | http://localhost:8001/health | curl /health pre-check
SYS-003 | SYS | FOUND:5 warm routes; no V2 snapshot by fingerprint | mnemolite/search_memory | http://localhost:8001 | @MNEMO_Q hybrid tags=[project:truth-engine,kernel] limit5 query INSEE/indexation/population/DGCL
SYS-004 | SYS | FOUND | mnemolite | warm-routes:5;snapshot:NONE | MNEMO_Q
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Insee populations legales communes estimation sondage methode recensement decret annuel rotation
QRY-002 | WEB | FOUND | - | - | loi 7 juin 1951 statistiques publiques independance professionnelle Autorite de la statistique publique article 1
QRY-003 | WEB | FOUND | - | - | Metzing population Insee denombrement ecart DGF commune penalisee
QRY-004 | WEB | FOUND | - | - | conventions indexation Insee IPC prestations sociales cout point inflation dette indexee milliards
QRY-005 | WEB | FOUND | - | - | Insee pression politique gouvernement chiffres controverse independance 2025 2026
QRY-006 | WEB | FOUND | - | - | Insee budget effectifs reorganisation syndicats qualite statistiques alerte
QRY-007 | FETCH | FOUND | SRC-001 | https://www.doctrine.fr/l/texts/lois/JORFTEXT000000888573 | loi 1951 art1 independance professionnelle via doctrine.fr (Legifrance 403 head_blocked)
QRY-008 | FETCH | FOUND | SRC-002 | https://www.autorite-statistique-publique.fr/presentation/ | presentation ASP missions membres
QRY-009 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/information/2553979 | comprendre populations de reference methode calcul
QRY-010 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/metadonnees/definition/c1999 | definition populations legales 350 textes decret annuel
QRY-011 | FETCH | FOUND | SRC-005 | https://www.senat.fr/questions/base/2026/qSEQ26010864S.html | QO 2026 revision methode recensement reponse gouvernement Cnerp 2 ans
QRY-012 | FETCH | FOUND | SRC-006 | https://www.senat.fr/cra/s20250624/s20250624_0.html | CR seance 24 juin 2025 questions orales recensement Metzing
QRY-013 | FETCH | FOUND | SRC-007 | https://www.maire-info.com/imprimer2.php?param=29467 | groupe de travail Cnerp reduction decalage reference
QRY-014 | FETCH | FOUND | SRC-008 | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/ | recensement enjeu dotations Bouzonville 20000-30000 euros
QRY-015 | FETCH | FOUND | SRC-009 | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | fiche DGF communes population DGF ecretage CPS
QRY-016 | FETCH | FOUND | SRC-010 | https://www.tresor.economie.gouv.fr/Articles/2022/07/05/finances-publiques-une-inflation-qui-rapporte | inflation qui rapporte 5 Mde par point prestations 10% dette indexee
QRY-017 | FETCH | FOUND | SRC-011 | https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public | FIPECO impact inflation deficit 5 Mde prestations 3 Mde interets
QRY-018 | FETCH | FOUND | SRC-012 | https://analyses-propositions.cgt.fr/fiche-pouvoir-dachat-6-linflation-de-quel-indicateur-parle-et-pour-quel-usage | fiche CGT inflation indicateurs indexation IPC hors tabac Smic retraites
QRY-019 | FETCH | FOUND | SRC-013 | https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/solidaires-finances/4163-communique-des-syndicats-de-l-insee-suite-aux-propos-de-darmanin.html | communique syndicats Insee propos Darmanin victimation
QRY-020 | FETCH | FOUND | SRC-014 | https://www.lemonde.fr/economie/article/2025/11/21/attaquees-par-les-populistes-et-soumises-aux-coupes-budgetaires-les-statistiques-publiques-en-pleines-turbulences_6654238_3234.html | Le Monde statistiques publiques turbulences populistes coupes (paywall: lead)
QRY-021 | FETCH | FOUND | SRC-015 | https://www.franceinfo.fr/economie/croissance/l-insee-abaisse-fortement-sa-prevision-de-croissance-pour-la-france-en-2026-de-0-7-a-0-4_8186732.html | franceinfo abaisse prevision croissance 2026
QRY-022 | WEB | NO_RESULT | - | - | REFUTATION Metzing Insee 678 791 habitants recensement erreur corrigee autre chiffre population legale
QRY-023 | WEB | NO_RESULT | - | - | REFUTATION inflation finances publiques cout prestations sociales indexees 5 milliards par point indexation perimetre delai dette indexee 10%
QRY-024 | WEB | NO_RESULT | - | - | REFUTATION loi 1951 independance professionnelle statistiques Conseil Etat invalidation populations reference decret annuel methode CNP periodicite
QRY-025 | WEB | NO_RESULT | - | - | REFUTATION Insee budget 473,5 millions euros 2024 critique effectifs sous-estimes autre chiffre LFI
QRY-026 | WEB | NO_RESULT | - | - | REFUTATION Darmanin victimation enquete niait le reel contreverse rapport police autre chiffre delinquance
QRY-027 | FETCH | FOUND | SRC-021 | https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011 | populations de reference 2023 decret 2025-1362 en vigueur 1er janvier 2026

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.doctrine.fr/l/texts/lois/JORFTEXT000000888573
SRC-002 | ◈ | fam:A | https://www.autorite-statistique-publique.fr/presentation/
SRC-003 | ◈ | fam:A | https://www.insee.fr/fr/information/2553979
SRC-004 | ◈ | fam:A | https://www.insee.fr/fr/metadonnees/definition/c1999
SRC-005 | ◈ | fam:A | https://www.senat.fr/questions/base/2026/qSEQ26010864S.html
SRC-006 | ◈ | fam:A | https://www.senat.fr/cra/s20250624/s20250624_0.html
SRC-007 | ◉ | fam:C | https://www.maire-info.com/imprimer2.php?param=29467
SRC-008 | ◉ | fam:C | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/
SRC-009 | ◈ | fam:A | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes
SRC-010 | ◈ | fam:A | https://www.tresor.economie.gouv.fr/Articles/2022/07/05/finances-publiques-une-inflation-qui-rapporte
SRC-011 | ◉ | fam:D | https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public
SRC-012 | ◉ | fam:C | https://analyses-propositions.cgt.fr/fiche-pouvoir-dachat-6-linflation-de-quel-indicateur-parle-et-pour-quel-usage
SRC-013 | ◈ | fam:C | https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/solidaires-finances/4163-communique-des-syndicats-de-l-insee-suite-aux-propos-de-darmanin.html
SRC-014 | ◉ | fam:C | https://www.lemonde.fr/economie/article/2025/11/21/attaquees-par-les-populistes-et-soumises-aux-coupes-budgetaires-les-statistiques-publiques-en-pleines-turbulences_6654238_3234.html
SRC-015 | ○ | fam:C | https://www.franceinfo.fr/economie/croissance/l-insee-abaisse-fortement-sa-prevision-de-croissance-pour-la-france-en-2026-de-0-7-a-0-4_8186732.html
SRC-016 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540
SRC-017 | ◈ | fam:A | https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/06/Delibere-Cnerp.pdf
SRC-018 | ◈ | fam:A | https://www.cnis.fr/commissions/evaluation-du-recensement-de-la-population-cnerp/
SRC-019 | ◉ | fam:E | https://insee.hal.science/hal-05307957/document
SRC-020 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf
SRC-021 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011
SRC-022 | ◉ | fam:C | https://fr.wikipedia.org/wiki/Institut_national_de_la_statistique_et_des_%C3%A9tudes_%C3%A9conomiques
SRC-023 | ◈ | fam:A | https://www.insee.fr/fr/information/4174951

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.doctrine.fr/l/texts/lois/JORFTEXT000000888573 | A | 1951-06-07 | loi-1951-independance | indépendance professionnelle des statistiques publiques (loi 51-711 art.1) ; ASP 9 membres (LME 2008, décret 2009-250) | 0753b910-3a89-4a01-a22e-45f642bb1954
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/information/2553979 | A | 2026-01-07 | populations-reference-methode | rotation 1/5 communes <10k ; sondage 8%/an logements >=10k ; décret annuel d'authentification depuis 2008 ; ~350 textes | a9538d85-912c-419d-8e46-42a08aab1655
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011 | A | 2025-12-18 | populations-reference-decret-annuel | populations de référence 2023 authentifiées par décret n°2025-1362 du 26/12/2025, en vigueur 01/01/2026 ; terme populations légales abandonné (concept c1999 clos 30/12/2024) | 72810efe-2752-4e38-bf35-cc2eeda22c95
FCT-004 | FACT | ✧ | https://www.senat.fr/cra/s20250624/s20250624_0.html | A | 2025-06-24 | metzing-ecart-denombrement | Metzing: Insee 678 hab. (2024) vs mairie 791 ; réponse ministérielle: population de référence 719 (réf. 2023) | cdaf21b7-5de4-4c82-8595-b5e15b01fe25
FCT-005 | FACT | ✧ | https://www.senat.fr/questions/base/2026/qSEQ26010864S.html | A | 2026-02-11 | cnerp-decalage-3-vers-2-ans | CNERP recommande réduction du décalage de référence 3->2 ans ; mise en oeuvre annoncée par l'Insee fin 2026 | bc1edb42-79cb-497e-b947-882292a1b8fc
FCT-006 | FACT | ✧ | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/ | C | 2026-01-15 | bouzonville-perte-dotations | perte ~100 habitants => 20 000-30 000 EUR de dotations en moins (Bouzonville, 3721 hab., maire A. Chabane) | a9652b12-d49c-421a-ad5d-b6b65aaa5ee8
FCT-007 | FACT | ✧ | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | A | 2026-09-22 | dgf-mecanique-population | population DGF = INSEE + résidences secondaires + places caravanes ; écrêtement PF>85% moyenne nationale ; part CPS transférée à l'EPCI (art.240 LF2024) | 2c0fec9b-4f5d-497f-a771-9073dc119d7a
FCT-008 | FACT | ✦ | https://www.tresor.economie.gouv.fr/Articles/2022/07/05/finances-publiques-une-inflation-qui-rapporte | A,D | 2022-07-05 | indexation-5-mde-par-point | 1 point d'inflation => ~5 MdEUR de dépenses sociales indexées en plus ; ~1/10 de la dette indexée (Trésor 2022, FIPECO 2026) | 9390b20a-c16c-405d-a7f3-75ee1c4b7549
FCT-009 | FACT | ✧ | https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public | D | 2026-04-08 | dette-indexee-interets | ±0,1% de prix sur un an => ±0,3 MdEUR de charge d'intérêts ; révision +1pt => +3 MdEUR (OATi France+zona) | 591ef480-c5e1-48f3-ad7b-1fcb150ab062
FCT-010 | FACT | ✧ | https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/solidaires-finances/4163-communique-des-syndicats-de-l-insee-suite-aux-propos-de-darmanin.html | C | 2021-05-20 | pression-politique-darmanin-victimation | ministre de l'Intérieur: enquêtes de victimation nient le réel ; syndicats CGT-FO-SUD dénoncent une invalidation sans arguments (20/05/2021) | e937d108-9b7e-477f-86a3-d383e3fd5d5c
FCT-011 | FACT | ✧ | https://www.lemonde.fr/economie/article/2025/11/21/attaquees-par-les-populistes-et-soumises-aux-coupes-budgetaires-les-statistiques-publiques-en-pleines-turbulences_6654238_3234.html | C | 2025-11-21 | statistiques-publiques-turbulences | Le Monde: statistiques publiques attaquées par populistes + coupes budgétaires (lead paywall, non inspecté) | 98c90698-c601-4cda-b2cc-141971c7e9dc
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-003
FCT-003 | SRC-021,SRC-004
FCT-004 | SRC-006,SRC-005
FCT-005 | SRC-005,SRC-006
FCT-006 | SRC-008
FCT-007 | SRC-009
FCT-008 | SRC-010,SRC-011
FCT-009 | SRC-011
FCT-010 | SRC-013
FCT-011 | SRC-014

## REFUTATION_REGISTRY_V1
FCT-002 | QRY-024 | NONE
FCT-003 | QRY-024 | NONE
FCT-004 | QRY-022 | NONE
FCT-008 | QRY-023 | NONE
FCT-010 | QRY-026 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:CONFIRME
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | ELIGIBLE:VERIFIE

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
FCT-010 | WRITE | -
FCT-011 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH:AXS-001 | PASS | LAST_COMPLETED:9:AXS-001 | NEXT_ACTION:9:AXS-009
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL:CAU-004 | PASS | LAST_COMPLETED:11:CAU-004 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-22T15:05:28.617048+00:00","fact_mem":{"FCT-001":"0753b910-3a89-4a01-a22e-45f642bb1954","FCT-002":"a9538d85-912c-419d-8e46-42a08aab1655","FCT-003":"72810efe-2752-4e38-bf35-cc2eeda22c95","FCT-004":"cdaf21b7-5de4-4c82-8595-b5e15b01fe25","FCT-005":"bc1edb42-79cb-497e-b947-882292a1b8fc","FCT-006":"a9652b12-d49c-421a-ad5d-b6b65aaa5ee8","FCT-007":"2c0fec9b-4f5d-497f-a771-9073dc119d7a","FCT-008":"9390b20a-c16c-405d-a7f3-75ee1c4b7549","FCT-009":"591ef480-c5e1-48f3-ad7b-1fcb150ab062","FCT-010":"e937d108-9b7e-477f-86a3-d383e3fd5d5c","FCT-011":"98c90698-c601-4cda-b2cc-141971c7e9dc"},"mnemo_row":"PASS: 11/11 eligible facts persisted via MCP write_memory; run 20260922-1517-insee","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"fait nouveau CONFIRME (2 familles independantes A+D, refutation bornee NONE_FOUND)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-010","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-011","reason":"fait nouveau VERIFIE","success":1}],"writeback_row":{"attempted":11,"blocked":0,"eligible":11,"failure":0,"success":11}}

PERSISTENCE_META: MNEMO_ROW:PASS: 11/11 eligible facts persisted via MCP write_memory; run 20260922-1517-insee | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:11;attempted:11;success:11;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[11 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-008 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME (2 familles independantes A+D, refutation bornee NONE_FOUND)
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-010 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-011 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
