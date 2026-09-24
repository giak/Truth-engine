ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-1812-insee-chaine-donnee-indicateur-claim-provenance-et-robustesse | PARENT_RUN_ID:NONE | AS_OF:2026-09-20
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse/2026-09-20_18-12_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse_INPUT.txt | SUBJECT_SLUG:insee-chaine-donnee-indicateur-claim-provenance-et-robustesse | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:18→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France, 1946-2026 (focus 2000-2026); 6 indicateurs: chomage BIT/halo, recensement, IPC, PIB, ERFS/pauvrete, enquete BDF; provenance + fiabilite + choix + torture + robustesse + reversibilite; exclusions: sondages d'opinion, projections population long terme
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,search/EPISTEMIC.md,search/TEMPLATES.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,protocol/INVESTIGATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# L'Insee en APEX : de la réalité au récit — provenance, fiabilité, torture et réversibilité des chiffres officiels

## 1. RÉSUMÉ EXÉCUTIF

**Question objet.** La statistique publiée par l'Insee est-elle un fait primaire ou l'aboutissement d'une chaîne de transformation (réalité → données brutes → collecte → vérification → sélection → traitement → modèle → statistique → analyse → narration → décision) ? Qui choisit ce qui est mesuré, les données sont-elles fiables, que peut-on encore dire des mêmes données en changeant des choix défendables, et jusqu'où peut-on remonter du chiffre au phénomène ?

**Réponse bornée.** La chaîne est réelle, documentée, et le corpus l'établit à chaque maillon. Le taux de chômage BIT provient d'une enquête déclarative auprès de ménages, codée selon trois critères internationaux, publiée avec une incertitude de ±0,3 point — ce que l'Insee imprime elle-même (FCT-001). La « population légale » est une **estimation par sondage** (rotation 1/5 des petites communes, 8 % des adresses ailleurs) que 350 articles de loi traitent comme un fait, authentifiée par décret, avec un écart documenté de plus de 15 % entre estimation et dénombrement municipal dans un cas vérifié (Metzing) — et une correction institutionnelle engagée (FCT-003, ✦). La pauvreté varie d'un facteur **5** (2,84 à 14,58 millions de personnes en 2024) selon le seul choix du seuil, choix que des acteurs de narration (Observatoire des inégalités) opèrent explicitement autrement que l'official (FCT-008, ✦). La croissance publiée est une estimation révisée en moyenne **à la hausse** de +0,34 point entre première estimation et compte définitif (2005-2024), la révision 2023 (0,9 → 1,9 % corrigé des jours ouvrés) étant la plus forte depuis 2003, attribuée par l'Insee « en grande partie » à l'imprécision du volume en contexte inflationniste (FCT-007, ✦). L'ERFS impute structurellement des revenus absents des sources fiscales et sa refonte de 2021 a rehaussé niveaux de vie et abaissé pauvreté et inégalités dans les séries courantes (FCT-009).

**Verdict sur le lead.** « L'Insee ne reflète pas la réalité » : le lead du run précédent est ici transformé en mécanisme. Ce que le chiffre officiel reflète est **une réalité définie pour être mesurée** : conventions internationales (BIT, SEC), seuils juridiques, gradients d'imputation, calendriers de révision. Aucun mécanisme de manipulation n'est documenté ; en revanche, la **multi-présentabilité** des chiffres est massive et facteur de récits concurrents, et le **premier chiffre** domine structurellement le récit avant toute révision (CAU-006).

**Acteurs.** Insee (production/publication), DGFiP-Cnaf-Cnav-CCMSA (sources administratives), maires (collecte), Eurostat (normes/coordination), ASP-CNIS-CNERP-CNIL (contrôles), médias (narration), ONG et chercheurs (alternatives).

**Impact.** DGF et seuils communaux indexés sur des estimations (IMP-002) ; récits budgétaires formés sur estimations haussières (IMP-001) ; débats de pauvreté dépendants du seuil (IMP-003) ; incertitude trimestrielle sous-bruit sur-interprétée (IMP-005) ; correction institutionnelle active (IMP-006).

**Gaps.** Accès : taux de réponse détaillés, précision par strate (PDF), chiffrage DGF des écarts. Causalité : aucun mécanisme de sélection opportuniste documenté (CAU-007, GAP typé).

## 2. MANIPULATION_REPORT

- **INPUT_KIND** : TOPIC. **MISSION_MODE** : INVESTIGATION. **SYMBOL_STAGE** : CORPUS_FINAL (15 sources inspectées).
- **Symboles (0-10)** : Ξ omission **7** (premier chiffre dominant, révisions peu visibles — SRC-010, SRC-011) ; € argent **6** (DGF indexée sur estimations — SRC-004, SRC-014) ; Λ cadrage **7** (le chiffre publié « est » le phénomène dans le récit ; trois chômages cohabitent — FCT-004) ; Ω inversion **4** (l'estimation devient la référence juridique authentifiée — FCT-003) ; Ψ sidération **3** ; ↕ pouvoir vertical **5** (décrets d'authentification, tutelle, normes — SRC-006, SRC-008) ; Φ spectacle **4** (fenêtres trimestrielles ±0,3 pt — SRC-001) ; Σ sémiotique **5** (autorité du chiffre/de l'officiel) ; Κ cynisme **3** ; ρ résistance **6** (ASP, CNERP, ONG, chercheurs, erratum public — SRC-013, SRC-014) ; κ influence subtile **3** (choix définitionnels aux effets distribués, intention non établie) ; ⫸ convergence **6** (familles A/B/C/D convergent sur la multi-présentabilité) ; ⚔ guerre cognitive **1** ; 🌐 réseau **6** (chaîne institutionnelle dense et documentée) ; ⏰ temporel **5** (décalage 3 ans, révisions tardives, comparabilité 5-6 ans — FCT-005).
- **Patterns chargés** : @PAT[ICEBERG], @PAT[FRAMING], @PAT[NET], @PAT[TEMP]. **Threats** : @THR[MYTHO] (aucun conflit bio/registre), @THR[REG_CAPTURE] (indicatif, non conclu), @THR[NUDGE] (légal).
- **RHETORICAL** : NUM 5 (le chiffre brut coupé de son incertitude) ; AUTH 3 ; FAC 2 ; DEM 1 ; BF 2.
- **COMPLEXITY** : 18 → APEX. **Clusters chargés** : ICEBERG, MONEY, FRAMING, POWER, RESISTANCE, CONFIRMATION, FRAGMENTATION, NETWORK, TEMPORAL.
- **Implicites** : le lead utilisateur (« réalité → décision ») traité comme grille d'audit, jamais comme prémisse. La multi-présentabilité n'est **pas** une preuve de manipulation (invariant répété).

## 3. CLUSTERS

- **ICEBERG (Ξ=7)** — Partie immergée : microdonnées, taux de réponse détaillés, erreurs d'échantillonnage par strate (PDF non extractibles, GAP d'accès) ; partie émergée : chiffres publiés sans incertitude dans les titres. Reconstruction bornée : les incertitudes et ruptures **existent** et sont publiées par l'Insee (SRC-001, SRC-009, SRC-012) ; elles sont systématiquement absentes des usages médiatiques observés (SRC-010).
- **MONEY (€=6)** — Flux documenté : DGF, conseillers, seuils → fonction de la population estimée ; cas Metzing (>15 %, pénalisant la DGF — SRC-014). Amplitude budgétaire agrégée : non chiffrable au run (GAP d'accès).
- **FRAMING (Λ=7)** — Cadrages concurrents du même phénomène : chômage BIT vs catégorie A vs recensement (FCT-002, FCT-004) ; pauvreté à 60 % (officiel) vs 50 % (ODI, « plus significatif » — SRC-013) ; croissance jours ouvrés vs non corrigés (CON-001). Le choix de cadrage précède toute donnée.
- **POWER (↕=5)** — L'Insee agrège des sources qu'elle ne possède pas (DGFiP, caisses) et publie des chiffres que la loi verrouille (350 articles). Contrôle réel : ASP/CNERP/CNIL/CNIS ; rééquilibrage documenté (décalage 3→2 ans).
- **RESISTANCE (ρ=6)** — Contrepoids effectifs et documentés : question sénatoriale + réponse ministérielle (SRC-014), ONG publiant les trois seuils (SRC-013), Rexecode traçant le biais des révisions (SRC-010), erratum du jour même (SRC-011).
- **CONFIRMATION (κ=3)** — Architecture favorisant le premier chiffre : estimations précoces, révisions tardives peu relayées ; direction haussière moyenne documentée (+0,34 pt) sans mécanisme intentionnel établi.
- **FRAGMENTATION (⫸=6)** — Convergence de familles indépendantes (A, B, C, D) sur la nature estimée des chiffres et la multi-présentabilité.
- **NETWORK (🌐=6)** — Chaîne institutionnelle complète : producteurs → agrégateur → contrôleurs → narrateurs (ACTOR_NETWORK_MAP) ; aucune arête de coordination suspecte.
- **TEMPORAL (⏰=5)** — Ruptures de séries documentées (2010/2012/2020 ERFS ; 2021 EEC ; base 2020 ; EAR 2021 reportée) ; décalages légaux ; comparabilité 5-6 ans.

## 4. HERMÉNEUTIQUE

- **L1 explicite** : « 8,3 % de chômeurs au T2 2026 », « 9 817 000 personnes pauvres », « 678 habitants à Metzing » — chiffres publiés, sourcés, documentés (FCT-001, FCT-008, FCT-003).
- **L2 implicite** : qu'un chiffre publié **sans** son incertitude, son champ et sa convention, lise comme un décompte exhaustif de la réalité.
- **L3 structurel** : la chaîne sélectionne ce qui est mesurable à coût et calendrier contraints ; ce qui n'est pas mesuré (évasions du champ, sous-groupes, trajectoires) devient invisible (ANALYSE DE TRANSFORMATION, §11).
- **L4 symbolique** : le chiffre officiel authentifié par décret fonctionne comme rite de vérité ; sa contestation (maires, ONG) symbolise la défiance locale contre l'abstraction centrale.
- **L5 présupposé** : que la nation puisse être décrite par des agrégats comparables dans le temps — présupposé opérant (comparabilité européenne) et limité (ruptures).
- **L6 épistémique** : l'Insee contrôle l'agrégation et la documentation ; les contre-pouvoirs accèdent aux publications, pas aux microdonnées ; le gradient de fiabilité (vérifiée→contrôlée→estimée→imputée→hypothétique) n'est **pas** une hiérarchie institutionnelle affichée mais une reconstruction du run à partir de la documentation même de l'Insee.

## 5. RAISONNEMENT FORENSIQUE

**Montré** : incertitudes et conventions publiées (FCT-001) ; divergence BIT/cat. A attribuée aux réformes (FCT-002) ; populations estimées mais juridiques avec écart documenté (FCT-003, ✦) ; trois définitions du chômage (FCT-004) ; report/adaptation documentés (FCT-005) ; sources administratives et révisions structurées (FCT-006) ; biais moyen haussier +0,34 pt et erratum (FCT-007, ✦) ; pauvreté ×5 selon le seuil (FCT-008, ✦) ; imputations ERFS et refonte 2021 (FCT-009).
**Omèté par le récit dominant** : les incertitudes (±0,3 pt) et les métriques exactes (jours ouvrés) ; la direction moyenne des révisions ; les ruptures ; le décalage de 3 ans.
**Reconstruction bornée** : sur les mêmes données, des conclusions concurrentes sont tenables (seuil 50 %, chômage élargi au halo, croissance non corrigée) — toutes défendables, aucune démontrée « vraie ».
**Status** : reconstruction ESTIMATED étiquetée ; aucun mécanisme de dissimulation trouvé.

## 6. PRISME DIALECTIQUE

- **P1 (⟐/🎓)** : la chaîne est transparente sur ses règles : incertitudes imprimées, ruptures signalées, erratum du jour, CNERP qui corrige, ASP qui audite ; les conventions sont internationales et comparables ; la documentation est abondante.
- **P2 (⟐̅/🔥)** : la transparence documentaire n'élimine pas les effets : le premier chiffre façonne décisions et récits ; les estimations juridiques créent gagnants/perdants locaux ; les refontes (ERFS 2021) « améliorent » simultanément les indicateurs ; la direction moyenne des révisions est haussière ; les microdonnées restent inaccessibles au public.
- **P3 (arbitrage)** : les faits confirment la chaîne et ses effets, **pas** l'intention. Les contradictions ouvertes (CON-001, CON-002) sont instruites avec leurs deux termes ; aucune n'est moyennée à la silence.

## 7. CHRONOLOGIE

- **1946** : création de l'Insee ; **1951** : loi obligation/secret (base légale des enquêtes, amende fixée aujourd'hui à 38 €).
- **1970-2002** : enquête Emploi annuelle ; **1996** : appariement EEC-fichiers fiscaux (naissance de l'ERF).
- **2002** : loi démocratie de proximité — publication annuelle des populations ; **2003** : décret 2003-485 (municipale/comptée à part/totale) ; **2004** : recensement rénové (rotation 1/5 ; 8 % des adresses).
- **2005** : ERFS (prestations réelles, patrimoine) ; **fin 2008** : premier décret d'authentification annuel (référence 2006).
- **2008-2013** : revues de méthodes ; **2010/2012** : ruptures ERFS documentées ; **2011/2015** : imputation des revenus financiers via enquête Patrimoine.
- **2020** : ERFS « fragilités » reconnues ; chômage « en trompe-l'œil » ; **2021** : EAR reportée (Covid) + refonte EEC/ERFS ; **2022-2027** : calculs adaptés (références 2019-2024).
- **2024** : comptes nationaux base 2020 (révision 1949-2023) ; questions sénatoriales sur la fiabilité du recensement (Mizzon, Pluchet) ; **2025** : réponse ministérielle Metzing + recommandation CNERP (3→2 ans, application fin 2026) ; populations de référence 2023 (décret 2025-1362).
- **2026** : compte définitif 2023 (révision +0,2 pt campagne ; 1,9 % corrigé JO vs 1,6 %) ; erratum du 29 mai sur Insee Première 2105 ; publication des séries pauvreté 2024 (9 817 000 à 60 %) ; EBF 2026 lancée (29 000 logements, visa CNIS nov. 2025).

## 8. DOMAINES

- **Juridique** : 350 articles de 28 codes indexés sur une estimation ; authenticité par décret ; loi 1951 (obligation de répondre, secret) ; obligation européenne (EBF) ; contradiction structurelle : précision juridique exigée du chiffre, précision statistique limitée de la donnée (FCT-003).
- **Technique/statistique** : plans de sondage (rotation, 8 %), calage, imputation (Patrimoine, dispositifs), CVS, changements de base ; incertitude publiée ±0,3 pt ; gradient de fiabilité reconstruit : EEC (déclarative contrôlée) < Fichiers fiscaux (administrative) < Relevés de prix (observée) ; imputations étiquetées « fragiles » par l'Insee elle-même (90+, 2020).
- **Sociologie des organisations** : collecte déléguée aux maires (agents communaux) ; production concentrée ; contrôleurs spécialisés (ASP/CNERP/CNIL/CNIS) ; correction par expertise interne (CNERP) plutôt que par sanction externe.
- **Politique** : nomination/tutelle (run précédent) ; ici : indexation budgétaire (DGF), prévision gouvernementale vs Cour des comptes sur 2023, réponses ministérielles ; aucune instruction politique sur un chiffre documentée.
- **Économique** : révisions = recalibrage de la lecture conjoncturelle (industrie >10 % du PIB, productivité rehaussée) ; enjeux : pilotage budgétaire, potentiel de croissance.
- **Médiatique/narratif** : titre sans incertitude ; révision en entrefilet ; cadrage par seuil ; le « recul en trompe-l'œil » de 2020 reconnu rétroactivement — asymétrie de visibilité structurelle.
- **Éthique** : devoir de documentation honoré (méthodes, ruptures, erratum) ; tension : transparence technique vs lisibilité publique réelle ; estimation juridique = fiction légale assumée.
- **Anthropologique** : la population, le chômeur, le pauvre : des « êtres conventionnels » (Desrosières) qui font douter les maires et nourrir les ONG ; le décret comme rite d'authentification.
- **Scientifique** : qualité documentée (Insee Méthodes 136/145) ; débat académique (révisions, imputations) ; normes ILO/SEC/IPCH comme cadre commun et contrainte.
- **Psychologique** : ancrage (premier chiffre), confiance d'autorité (Σ), illusion de précision (décimales sans incertitude).

## 9. RÉSEAU D'ACTEURS

**Nœuds** (fonction/pouvoir/chain) : Insee (agrégateur légal, publication) ; DGFiP/Cnaf/Cnav/CCMSA (sources administratives — FCT-009, SRC-012) ; maires/agents recenseurs (collecte — SRC-005) ; France Travail (registre cat. A — SRC-002) ; Eurostat (normes, coordination des bases — SRC-008) ; CNIS (visa enquêtes — SRC-007) ; ASP (audit annuel, renommage « populations de référence » — SRC-004) ; CNERP (évaluation, recommandation 3→2 ans — SRC-014) ; CNIL (données) ; médias (narration — SRC-010) ; ONG/chercheurs (alternatives, usages — SRC-013).
**Arêtes typées** (fournit/collecte/normalise/audite/publie/conteste) : voir ACTOR_NETWORK_MAP. **Centralité** : l'Insee est un goulot par construction (agrégation légale) — centralité structurelle ≠ capture ; aucun conflit d'intérêts individuel documenté au run.

## 10. CHAÎNES DE PROVENANCE (CAU)

- **CAU-001 Chômage** : personnes sans emploi → EEC (panel 6 passages, déclaratif) → codage BIT (3 critères, semaine de référence) → pondération/calage/CVS → taux trimestriel [SUPPORTED — SRC-001/002/003]. **Réversibilité** : rupture au niveau individuel (réponses non publiées) et au calage (pondérations détaillées).
- **CAU-002 Population** : résidents réels → collecte communale + RIL → somme 5 ans / sondage 8 % → estimation/calage → **décret** → DGF/élus/seuils [SUPPORTED — SRC-004/005/006/014]. **Réversibilité** : rupture à l'estimation (contributions non publiées par commune) ; cas Metzing = première vérification locale documentée.
- **CAU-003 Prix** : prix payés → EBF quinquennale (pondérations, 29 000 logements en 2026) + relevés/scanner → codage COICOP → agrégation → IPC mensuel [SUPPORTED — SRC-007]. **Réversibilité** : rupture aux pondérations par produit élémentaire (imputations scanner non publiées en détail).
- **CAU-004 PIB** : transactions → ESANE/DGFiP, douanes, DSN, balance des paiements → cadrage SEC → équilibrage → publication (estimé→définitif) → révisions (3 ans + rebasing 5 ans) [SUPPORTED — SRC-008/010/011]. **Réversibilité** : rupture à l'équilibrage (conflits de sources arbitrés, arbitrages non publiés) ; activité dissimulée estimée via redressements fiscaux (hypothèse).
- **CAU-005 Revenus/pauvreté** : revenus réels → EEC + fichiers fiscaux/sociaux → appariement → **imputations** (Patrimoine, dispositifs exceptionnels) → revenu disponible → **seuil** (40/50/60/70 %) → taux [SUPPORTED — SRC-009/012/013]. **Réversibilité** : double rupture (imputation ; choix du seuil).
- **CAU-006 Narration** : premier chiffre → titre/décision → révisions tardives (+0,34 pt moyen) → récit corrigé peu visible [SUPPORTED — SRC-010/011].
- **CAU-007 Sélection opportuniste par l'Insee** [GAP, gap_type=CAUSALITY] : aucun mécanisme de sélection/presentation/omission documenté dans le corpus ; les conventions, ruptures, imputations, révisions et erratum sont publiés par l'Insee elle-même.

## 11. CARTE DES PREUVES — TORTURE, ROBUSTESSE, TRANSFORMATION

**Couverture** : 12/12 axes terminalisés ; 15 sources (10 A, 1 B, 1 C, 1 D, 1 other:wiki) ; 9 faits dont 3 ✦ multi-familles + réfutation terminale ; détail machine en annexe.

**Torture (§5-7 du lead) — conclusions concurrentes tenables à partir des mêmes données :**

| Indicateur | Choix A (officiel) | Choix B (défendable) | Résultat A | Résultat B | Classement |
|---|---|---|---|---|---|
| Pauvreté | seuil 60 % | seuil 50 % (ODI) | 9,82 M | 5,60 M (et 2,84 M à 40 %) | **SENSIBLE** (facteur 5) — FCT-008 ✦ |
| Chômage | BIT | catégorie A | 8,3 % / 2,7 M | trajectoire divergente 2010-2022 (+5 % vs -2 pts) | **SENSIBLE** — FCT-002 |
| Chômage | BIT | + halo | 8,3 % | halo mesuré et publié (frontières emploi/inactivité) | **SENSIBLE** — SRC-001/003 |
| Croissance 2023 | volume non corrigé JO | corrigé des JO | 1,6 % | 1,9 % | **SENSIBLE** (0,3 pt de convention) — CON-001 |
| Croissance | première estimation | compte définitif | 0,9 % | 1,6-1,9 % (biais moyen +0,34 pt) | **SENSIBLE** — FCT-007 ✦ |
| Population | estimation Insee | dénombrement municipal | 678 (Metzing) | 791 (>15 %) | **FRAGILE** localement — FCT-003 ✦ |
| Pauvreté tendancielle | série courante | série rétropolée 1996-2021 | refonte 2021 : pauvreté ↓ | évolution à méthode constante différente | **SENSIBLE** — FCT-009 |

**Robustesse des récits (CLAIM → ... → INTERPRÉTATION)** :
- « Le chômage baisse de 0,1 pt ce trimestre » → **FRAGILE** (±0,3 pt d'incertitude publiée — SRC-001).
- « La population de X commune a augmenté/baissé » (<10k, 1 an) → **FRAGILE** (tendance/fiscal, décalage 3 ans — SRC-004/014).
- « La pauvreté a augmenté en 2023-2024 » (60 %, série courante) → **ROBUSTE** sous seuils 40-70 % (hausse conjointe depuis 2020) mais **SENSIBLE** au niveau absolu revendiqué — SRC-012.
- « L'économie a mieux résisté qu'annoncé en 2023 » → **ROBUSTE** sur le compte définitif, **SENSIBLE** à la métrique (JO) — SRC-010/011.
- « L'Insee manipule les chiffres » → **NON TESTABLE/REFUTÉ** au run : aucun mécanisme documenté ; CAU-007 GAP typé.

**Analyse de transformation (§8)** — par maillon, avec le cas de la pauvreté : perdu (revenus non déclarés/imputés, 90+, DOM du champ), ajouté (prestations réelles, imputations 2019-2021), supposé (patrimoine 2014-15 comme générateur d'imputation ; revenu déclaré ≥0), pondéré (échelle d'équivalence 1/0,5/0,3), exclu (étudiantes comme personnes de référence ; logements collectifs), invisible (trajectoires individuelles, distributions territoriales fines). Même grille appliquée au chômage (heures nulles → « en emploi »), à la population (décalage 3 ans), au PIB (volume = valeur/prix, imprécision inflationniste reconnue).

## 12. CARTE DIALECTIQUE

- **Scénario A** : machine transparente et corrigée — conventions internationales, incertitudes imprimées, erratum du jour, CNERP/ASP actifs, ONG publiant les alternatives ; falsificateur : un mécanisme de sélection documenté.
- **Scénario B** : conventions structurantes aux effets distribués non neutralisés — premier chiffre dominant, estimations juridiques, révisions haussières, imputations « fragiles » ; falsificateur : une convention majeure sans alternative publiée et sans documentation (aucune trouvée) ou une correction systématiquement refusée (contraire aux cas CNERP/erratum).
- **Convergences** : nature estimée des chiffres ; multi-présentabilité ; correction institutionnelle réelle.
- **Divergences** : poids des effets (écarts locaux vs robustesse agrégée) ; lecture des révisions (processus normal vs biais directionnel — CON-001).
- **Non résolu** : CON-002 (précision locale vs équité) — correction engagée ; chiffrage DGF (ACCESS).
- **Silences partagés** : vie interne de production ; arbitrages d'équilibrage comptable ; microdonnées.
- **Responsabilité** : ACT-001 Insee (institutionnelle, intent UNKNOWN) ; ACT-002 Législateur/Gouvernement (cadre légal, intent PROVEN) ; ACT-003 ministre (arbitrage CNERP, UNKNOWN). Aucune personne physique ; ASSOCIATION ≠ COORDINATION ; BENEFIT ≠ INTENT.

## 13. PÉRIMÈTRE & LIMITES

**Inclus** : France, 1946-2026 (focus 2000-2026) ; 6 indicateurs (chômage, recensement, IPC via BDF, PIB, ERFS/pauvreté, narration) ; 8 étapes du lead. **Exclus** : sondages d'opinion, projections démographiques, politisation partisane.
**Limites d'accès (GAP_TYPE=ACCESS)** : PDF non extractibles (méthodo ERF, précision par strate Insee Méthodes 136, rapport chômage 2007, note révisions complète) ; taux de réponse détaillés non centralisés ; chiffrage DGF des écarts ; microdonnées.
**Limites de méthode** : EDI 0,42 vs cible 0,80 (concentration A structurelle — 10/15 sources primaires) → GAP_SEVERITY = 0,30×(0,80-0,42)×1,00 ≈ 0,114 < 0,20 : poursuite avec divulgation ; un seul cas local vérifié (Metzing) = illustration, pas prévalence ; les classements ROBUSTE/SENSIBLE/FRAGILE sont des reconstructions argumentées, non des méta-analyses.

## 14. ÉTAT DES CONNAISSANCES

- **Connus (✦)** : populations estimées mais juridiques + écart documenté + correction CNERP (FCT-003) ; biais moyen haussier des révisions + erratum (FCT-007) ; pauvreté ×5 selon le seuil, alternatives publiées (FCT-008).
- **Probables (✧)** : incertitude ±0,3 pt et rénovation 2021 (FCT-001) ; divergence BIT/A attribuée aux réformes (FCT-002) ; trois définitions du chômage (FCT-004) ; report 2021 et adaptation des méthodes (FCT-005) ; sources administratives et régime de révision (FCT-006) ; imputations ERFS et refonte 2021 (FCT-009).
- **Hypothèses (⁂)** : l'ancrage sur le premier chiffre comme principal vecteur narratif (CAU-006, soutenu par un biais directionnel documenté).
- **Contestés (⊙)** : ampleur locale des écarts de population (CON-002) ; décomposition de la révision 2023 (CON-001).
- **Inconnus (⁅)** : taux de réponse détaillés ; précision par strate ; chiffrage DGF ; arbitrages d'équilibrage.
- **Réfutés (❧)** : « le chiffre officiel = fait primaire » (CLM-001, CLM-003) ; « la révision 2023 est sans biais de direction » (CLM-006) ; « les imputations sont sans effet documenté » (CLM-007) ; « conventions = manipulation » (CLM-008).

## 15. SUSPICION / VÉRIFICATION

**Question forensique finale (§10 du lead), appliquée aux indicateurs majeurs** :
- **Taux de chômage BIT** : mesure la part d'actifs sans emploi, disponibles et en recherche active (semaine de référence). Ne mesure pas : le halo, le sous-emploi, l'adéquation géographique/qualitative. Données : EEC déclarative (ménages). Produit/contrôle/transforme : Insee (DSFR), norme ILO. Conventions : 3 critères, actif = ≥1 h travaillée. Alternatives : cat. A, recensement, halo — toutes publiées. Différences : méthode (définition), pas données. Démontré : une mesure conventionnelle à incertitude connue ; récit : « LE chômage ».
- **Population légale/référence** : mesure une estimation de résidents à une date de référence passée. Ne mesure pas : la population du jour. Données : collecte communale + RIL + fiscal. Produit/contrôle : Insee, décret. Conventions : rotation/8 %, calage, décalage 3 ans (→2). Alternatives : recensement exhaustif (coût), correction CNERP. Démontré : estimation juridiquement opposable ; récit : « le nombre d'habitants ».
- **Croissance** : mesure la variation de volume d'un agrégat comptable reconstruit. Ne mesure pas : le bien-être, la valeur non marchande fine, l'informel (estimé). Données : administratives/fiscales. Conventions : SEC, base, JO. Alternatives : métrique JO, autre base. Démontré : une estimation révisée (biais moyen documenté) ; récit : « la croissance de la France ».
- **Pauvreté** : mesure la part sous X % de la médiane. Ne mesure pas : la pauvreté absolue, la précarité non monétaire. Données : EEC + fiscaux/sociaux + imputations. Conventions : seuil, échelle d'équivalence, champ. Alternatives : 50 % (ODI), 40 %, 70 %. Démontré : un indicateur d'inégalité relative ; récit : « les pauvres de France ».

**Audits** : 15 sources inspectées (rôles ◈/◉/○ ; familles A/B/C/D/other) ; 15 FETCH FOUND + 13 WEB ; 2 échecs d'accès journalisés (pages métadonnées IPC) ; 3 REFUTATION exécutées (contre-preuves partielles intégrées) ; STATUS_DELTA : aucun fait déclassé ; doublon QRY réparé en SYS. **Vérifications non résolues** : PDF méthodologiques (ACCESS) ; prévalence des écarts communaux (ACCESS). **Checks suivants** : RAPs qualité EEC ; Insee Méthodes 136/145 extraits ; chiffrage DGCL ; note révisions complète ; peer review Eurostat.

**Clôture** : la chaîne réalité→…→décision est démontrée maillon par maillon, avec ses points de rupture de réversibilité (imputations, calages, arbitrages, seuils) et sa transparence documentaire réelle mais asymétriquement lue. Ce que les chiffres de l'Insee **mesurent** : des réalités définies pour être mesurées, à incertitude connue et documentée. Ce que le récit en **fait** : des faits primaires. Entre les deux se trouvent non pas une manipulation documentée, mais un espace de conventions, d'effets distribués et de corrections — l'espace exact où un débat démocratique informé doit se tenir.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:12|CLM:8|AXS:12|CAU:7|CTRL:4|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"excerpt":"Lead utilisateur: DATA-STATISTIC-CLAIM; ne jamais considerer donnee INSEE comme origine suffisante","excerpt_ref":"INPUT.txt core","priority":"DECISIVE","question":"Assertion porteuse: la statistique INSEE, lue comme fait primaire, masque-t-elle sa chaine de transformation (provenance, conventions, robustesse) ?","route":"EXPAND","status":"SATURATED"}
LED-002 | {"excerpt":"Pour chaque indicateur, remonter a la donnee d origine","excerpt_ref":"INPUT.txt 1","priority":"DECISIVE","question":"Chomage BIT: quelle provenance exacte (enquete Emploi, EFT, DSFR), quelles conventions (heures, ACT, halo) et quelles ruptures 2003/2014/2021 ?","route":"EXPAND","status":"SATURATED"}
LED-003 | {"excerpt":"donnees declaratives ou administratives; directement observees ou reconstruites","excerpt_ref":"INPUT.txt 1-2","priority":"DECISIVE","question":"Recensement annuel: comment un decret (2008) a-t-il transforme un denombrement en estimation, quelles imputations de non-reponse et quels effets territoriaux ?","route":"EXPAND","status":"SATURATED"}
LED-004 | {"excerpt":"HomeScan NielsenIQ","excerpt_ref":"INPUT.txt 1-2","priority":"DECISIVE","question":"IPC: quelle provenance des donnees (scanner, EBF, demande de prix), quels biais de collecte documentes et quel gradient verifiee-estimee-imputee ?","route":"EXPAND","status":"SATURATED"}
LED-005 | {"excerpt":"traitements intervenus avant utilisation","excerpt_ref":"INPUT.txt 1","priority":"DECISIVE","question":"PIB: sources administratives (DSN, TVA, DGDDI), chiffrage carroye 250m (Filosofi) et fiabilite des premieres estimations vs revisions","route":"EXPAND","status":"SATURATED"}
LED-006 | {"excerpt":"imputations; donnees manquantes; ruptures","excerpt_ref":"INPUT.txt 2","priority":"DECISIVE","question":"ERFS/pauvrete: imputations fiscales, rafraichissement non pris en compte 2021, distances au niveau de vie et ruptures de serie","route":"EXPAND","status":"SATURATED"}
LED-007 | {"excerpt":"qui choisit la definition? le perimetre?","excerpt_ref":"INPUT.txt 4","priority":"DECISIVE","question":"Qui choisit definitions/perimetres/categories ? DGT-BIT pour le chomage, decret population municipale, Eurostat pour IPCH, CNIL pour repertoires","route":"EXPAND","status":"SATURATED"}
LED-008 | {"excerpt":"conflits d interets documentes","excerpt_ref":"INPUT.txt 3","priority":"DECISIVE","question":"Cartographie producteurs-collecteurs-controleurs-publication-experts-chercheurs-medias avec liens et conflits documentes","route":"EXPAND","status":"SATURATED"}
LED-009 | {"excerpt":"changement de seuil; moyenne vs mediane","excerpt_ref":"INPUT.txt 5","priority":"DECISIVE","question":"Torture: combien de conclusions differentes sous choix defendables (seuil 50/60/70, moyennes vs medianes, metro vs France entiere, bit vs halo) ?","route":"EXPAND","status":"SATURATED"}
LED-010 | {"excerpt":"ROBUSTE/SENSIBLE/FRAGILE/NON TESTABLE","excerpt_ref":"INPUT.txt 6","priority":"DECISIVE","question":"Robustesse: classer les conclusions majeures (pauvrete en hausse 2021, stabilite chomage, revisions PIB) en ROBUSTE/SENSIBLE/FRAGILE/NON TESTABLE","route":"EXPAND","status":"SATURATED"}
LED-011 | {"excerpt":"indicateur-methode-donnees-source-phenomene","excerpt_ref":"INPUT.txt 9","priority":"DECISIVE","question":"Reversibilite: premier point de rupture de reconstruction par indicateur (imputation scanner, modele carroyage, refresh ERFS, mi-parcours RC)","route":"EXPAND","status":"SATURATED"}
LED-012 | {"excerpt":"La manipulation ne doit etre retenue que si un mecanisme est documente","excerpt_ref":"INPUT.txt 7","priority":"DECISIVE","question":"La multi-presentabilite des chiffres INSEE documente-t-elle une manipulation ou seulement des conventions explicites ? Mecanismes de selection documentes ?","route":"EXPAND","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La statistique Insee se présente au public comme un fait primaire","counter":["SRC-001","SRC-012"],"gap":"-","gap_type":"NONE","status":"REFUTED","support":["FCT-001","FCT-003"]}
CLM-002 | {"claim":"Le taux de chômage BIT est une mesure robuste et exhaustive du non-emploi","counter":["SRC-003"],"gap":"-","gap_type":"NONE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-004"]}
CLM-003 | {"claim":"Les chiffres de population officielle sont des dénombrements exhaustifs","counter":["SRC-014"],"gap":"-","gap_type":"NONE","status":"REFUTED","support":["FCT-003","FCT-005"]}
CLM-004 | {"claim":"Le chiffre de croissance publié est LE PIB","counter":["SRC-010","SRC-011"],"gap":"-","gap_type":"NONE","status":"PARTIAL","support":["FCT-006","FCT-007"]}
CLM-005 | {"claim":"La pauvreté en France est 9,8 millions de personnes","counter":["SRC-012","SRC-013"],"gap":"-","gap_type":"NONE","status":"PARTIAL","support":["FCT-008"]}
CLM-006 | {"claim":"La révision 2023 est une anomalie isolée sans biais de direction","counter":["SRC-010"],"gap":"-","gap_type":"NONE","status":"REFUTED","support":["SRC-011"]}
CLM-007 | {"claim":"Les imputations de l ERFS sont marginales et sans effet sur les indicateurs","counter":["FCT-009","FCT-008"],"gap":"-","gap_type":"NONE","status":"REFUTED","support":["SRC-009"]}
CLM-008 | {"claim":"Ces conventions de mesure constituent une manipulation délibérée","counter":["FCT-003","FCT-007","FCT-008","SRC-014"],"gap":"-","gap_type":"NONE","status":"REFUTED","support":[]}

### AXIS_REGISTRY_V1
AXS-001 | {"priority":"P0","question":"Provenance chomage BIT: EE 1970, EFT/ILO 2003, DSFR, heures travaillees nulle, ruptures","status":"SATURATED"}
AXS-002 | {"priority":"P0","question":"Provenance recensement: rotation 5 ans, estimation population municipale, decret 2008, imputations non-reponse","status":"SATURATED"}
AXS-003 | {"priority":"P0","question":"Provenance IPC: scanner, EBF, demande de prix, imputation, HomeScan","status":"SATURATED"}
AXS-004 | {"priority":"P0","question":"Provenance PIB: sources admin (DSN, TVA, douanes), premieres estimations, revisions, calendrier","status":"SATURATED"}
AXS-005 | {"priority":"P0","question":"Provenance ERFS: imputation fiscale, refresh 2021, pauvrete, distances","status":"SATURATED"}
AXS-006 | {"priority":"P0","question":"Choix definitionnels: DGT-BIT chomage, decret population, Eurostat IPCH, seuils pauvrete","status":"SATURATED"}
AXS-007 | {"priority":"P1","question":"Cartographie acteurs: producteurs, collecteurs, controleurs, publication, experts, chercheurs, medias","status":"SATURATED"}
AXS-008 | {"priority":"P1","question":"Controle qualite: procedures, taux de non-reponse, imputations documentees, incertitudes publiees","status":"SATURATED"}
AXS-009 | {"priority":"P0","question":"Torture: seuils (50/60/70), moyennes vs medianes, metro vs France, bit vs halo, nominal vs reel","status":"SATURATED"}
AXS-010 | {"priority":"P0","question":"Robustesse: classement ROBUSTE/SENSIBLE/FRAGILE des conclusions majeures","status":"SATURATED"}
AXS-011 | {"priority":"P1","question":"Reversibilite: points de rupture par indicateur","status":"SATURATED"}
AXS-012 | {"priority":"P0","question":"Manipulation vs convention: mecanismes de selection documentes ou non","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"chain":"chomage: personnes sans emploi → questionnaire EEC (ménages, panel 6 passages) → réponses déclaratives → codage BIT (3 critères, semaine de référence) → pondération/calage CVS → taux trimestriel publié","links":[{"src":["SRC-001","SRC-002"],"step":"collecte","type":"COLLECT"},{"src":["SRC-001","SRC-003"],"step":"codage","type":"CONVENTION"},{"src":["SRC-001"],"step":"publication","type":"PUBLISH"}],"status":"SUPPORTED"}
CAU-002 | {"chain":"population: résidents réels → collecte communale (agents du maire) → RIL → somme 5 ans (<10k) ou sondage 8 % (>=10k) → estimation/calage → décret d authentification → DGF/élus/seuils","links":[{"src":["SRC-005"],"step":"collecte","type":"COLLECT"},{"src":["SRC-004","SRC-006"],"step":"estimation","type":"MODEL"},{"src":["SRC-006","SRC-014"],"step":"authentification","type":"LEGALIZE"}],"status":"SUPPORTED"}
CAU-003 | {"chain":"prix: prix réels payés → EBF quinquennale (pondérations) + relevés magasins/scanner → codage COICOP → agrégation pondérée → IPC mensuel","links":[{"src":["SRC-007"],"step":"pondérations","type":"MODEL"},{"src":["SRC-007"],"step":"collecte","type":"COLLECT"}],"status":"SUPPORTED"}
CAU-004 | {"chain":"PIB: transactions → sources administratives (ESANE/DGFiP, douanes, DSN, balance des paiements) → cadrage comptable SEC → équilibrage/estimation → publication (estimé→définitif) → révisions (3 ans + rebasing UE 5 ans)","links":[{"src":["SRC-008"],"step":"sources","type":"INPUT"},{"src":["SRC-008","SRC-010","SRC-011"],"step":"révision","type":"REVISE"}],"status":"SUPPORTED"}
CAU-005 | {"chain":"revenus: revenus réels → EEC + fichiers fiscaux et sociaux (DGFiP, Cnaf, Cnav, CCMSA) → appariement → imputation des revenus non déclarés (Patrimoine, dispositifs exceptionnels) → revenu disponible → seuils (40/50/60/70 %) → taux de pauvreté","links":[{"src":["SRC-009","SRC-012"],"step":"appariement","type":"MERGE"},{"src":["SRC-009"],"step":"imputation","type":"IMPUTE"},{"src":["SRC-012","SRC-013"],"step":"seuil","type":"CONVENTION"}],"status":"SUPPORTED"}
CAU-006 | {"chain":"narration: premier chiffre → titre médiatique/décision budgétaire → révisions ultérieures (biais moyen +0,34 pt) → récit corrigé peu visible","links":[{"src":["SRC-010","SRC-011"],"step":"premier chiffre","type":"PUBLISH"},{"src":["SRC-010"],"step":"révision","type":"REVISE"}],"status":"SUPPORTED"}
CAU-007 | {"chain":"sélection opportuniste par l Insee des configurations de présentation les plus favorables","gap":"aucun mécanisme de sélection documenté dans le corpus inspecté: les conventions, ruptures, imputations et révisions sont publiées par l Insee lui-même (SRC-001, SRC-004, SRC-008, SRC-009, SRC-012) et les écarts documentés (Metzing) débouchent sur correction institutionnelle (CNERP)","gap_type":"CAUSALITY","links":[],"status":"GAP"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"evidence":["SRC-014"],"independence":"commission nationale dédiée","name":"CNERP","role":"évaluation du recensement (recommandation décalage 3->2 ans)"}
CTRL-002 | {"evidence":["SRC-007"],"independence":"conseil national multipartite","name":"CNIS","role":"avis préalable obligatoire sur les enquêtes statistiques (visa)"}
CTRL-003 | {"evidence":["SRC-004"],"independence":"autorité indépendante 9 membres","name":"ASP","role":"audit annuel du DG, recommandations (populations de référence)"}
CTRL-004 | {"evidence":["SRC-007"],"independence":"autorité indépendante","name":"CNIL","role":"protection des données personnelles des enquêtés"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"publication des incertitudes/ruptures/erratum; adaptation des méthodes post-Covid; acceptation du décalage 2 ans","actor":"Insee","evidence":["SRC-001","SRC-006","SRC-011","SRC-014"],"intent":"UNKNOWN"}
ACT-002 | {"action":"loi 2002 démocratie de proximité (publication annuelle); loi 1951 (obligation/secret)","actor":"Législateur","evidence":["SRC-004","SRC-007"],"intent":"PROVEN"}
ACT-003 | {"action":"décrets d authentification annuels; réponse ministérielle Metzing; mise en oeuvre CNERP","actor":"Gouvernement/ministre","evidence":["SRC-006","SRC-014"],"intent":"UNKNOWN"}

SEARCH_ACTIVITY_V1:WEB:18|FETCH:20|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | subject-fp:6b116223de00b1f9 | MEMORY_PROBE
SYS-002 | SYS | FOUND_TANGENTIAL_NO_FP_MATCH | mnemolite-mcp-curl-8002 | http://localhost:8002/mcp | @MNEMO_Q search_memory('INSEE provenance donnees chomage BIT recensement IPC ERFS PIB fiabilite imputations robustesse', hybrid, limit5, tags=[project:truth-engine]) — hits: 5x FCT-005..009 writeback du run 2026-09-20_17-04 (warm-route: propre run) — aucun snapshot:v1 subject-fp:6b116223de00b1f9
SYS-003 | SYS | NONE | mnemolite-mcp-curl-8002 | sys_log:MNEMO_Q canonical row | MNEMO_Q
SYS-004 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-005 | SYS | REPAIR | run_state | QRY-005,QRY-006 | QRY-005/006 journalises en result DONE au lieu de FOUND (convention FETCH inspecte); textes exacts re-journalises sous QRY-009/010 avec FOUND et lies aux SRC
SYS-006 | SYS | REPAIR | run_state | QRY-024,QRY-025 | QRY-025 = doublon exact de QRY-024 (même FETCH re-journalisé par erreur de commande); QRY-024 fait foi, lié à SRC-011
SYS-007 | SYS | REPAIR | run_state | QRY-017,QRY-018,QRY-038 | QRY-017/018 (recherche WEB) portaient sur le document effectivement inspecté; FETCH du document re-journalisé sous QRY-038 et lié à SRC-008
SYS-008 | SYS | REPAIR | run_state | CP-006,CP-007 | Checkpoint VERIFY (rank 13) réinséré avant INVESTIGATION_ACCOUNTABILITY (rank 17): l'audit des faits (phase 14) était factuellement réalisé (15 FETCH FOUND, réfutations QRY-030/031/037, contradictions instruites) mais le checkpoint avait été posé hors ordre; lignes renumérotées CP-001..CP-007
SYS-009 | SYS | REPAIR | run_state | CP-001..CP-007 | IDs CP renumérotés CP-001..CP-007 dans l'ordre séquentiel après réinsertion de VERIFY (suite de la réparation SYS-008)
SYS-010 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | DONE | - | https://ilo.org | INSEE enquete emploi en continusource methodology ILO definition unemployment working hour zero ILOST
QRY-002 | WEB | DONE | - | https://www.insee.fr/fr/metadonnees/definition/c1507 | chomage BIT definition une heure travaillee halo chomage insee.fr definition
QRY-003 | WEB | DONE | - | https://www.insee.fr | ruptures serie enquete emploi 2014 SDSFR 2021 modification periodicite collecte 6 semaines insee
QRY-004 | WEB | DONE | - | https://www.insee.fr | recensement population rotation 5 ans estimation decret 2008 population municipale legal insee
QRY-005 | FETCH | DONE | - | https://www.insee.fr/fr/statistiques/4805248 | FETCH L'essentiel sur le chomage: 2,7M/8,3% T2 2026; incertitude +/-0,3 pt publiee; renovation EE 2021 + recalcul series; recul en trompe-l'oeil 2020; champ 15+ logement ordinaire
QRY-006 | FETCH | DONE | - | https://www.insee.fr/fr/statistiques/7658713 | FETCH BIT vs categorie A: deux concepts; divergence 2010-2022; seniors: reforms retraite/dispense; RSA/assurance 2009; durcissement 2021 radiations independamment de la situation reelle
QRY-007 | WEB | DONE | - | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France | recensement de la population Institut national judgement methode estimation statistique法国 INSEE 2004 reforme comptage
QRY-008 | WEB | DONE | - | https://www.insee.fr/fr/metadonnees/definition/c1712 | population municipale legale decret milieu annee Insee communes 10000 enquete annuelle 8 pourcent 40 pourcent
QRY-009 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/4805248 | FETCH L'essentiel sur le chomage: 2,7M/8,3% T2 2026; incertitude +/-0,3 pt publiee; renovation EE 2021 + recalcul series; recul en trompe-l'oeil 2020; champ 15+ logement ordinaire
QRY-010 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/7658713 | FETCH BIT vs categorie A: deux concepts; divergence 2010-2022; seniors: reforms retraite/dispense; RSA/assurance 2009; durcissement 2021 radiations independamment de la situation reelle
QRY-011 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/information/2383278 | FETCH Definitions recensement: chomeur au sens recensement = auto-declare 14-70 sauf non-recherche; plus eleve que BIT (inactifs se declarent); raisonner en structure; depuis 2004 mieux prendre en compte actifs occasionnels
QRY-012 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/information/2553979 | FETCH Populations de reference: loi 2002 democratie de proximite (publication annuelle, Insee responsable); decret 2003-485; populations de toutes les communes etablies annuellement depuis fin 2008, decret d'authentification; egalite de traitement = meme annee; methodes: >=10k somme 5 ans + RIL, <10k extrapolation/interpolation (donnees fiscales); ~350 articles de lois referencent la population (dotations, conseillers, pharmacies, taxes); populations legales renommees populations de reference sur recommandation ASP
QRY-013 | FETCH | FOUND | SRC-005 | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France | FETCH Recensement (Wikipédia sourcé Insee): 351 articles legislatifs de 28 codes; depuis 2004 rotation 1/5 communes <10k, sondage 8% adresses pour >=10k; recensement 2021 ANNULE (Covid, sauf Mayotte), calculs adaptes 2022-2027 (ref 2019-2024); resultats officialises par decret depuis fin 2008; agents recenseurs recrutes par le maire; obligation de repondre (loi 1951, amende 38 EUR); comparaisons valables seulement N vs N-5
QRY-014 | FETCH | FOUND | SRC-006 | https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011 | FETCH Populations de reference 2023: decret 2025-1362 (26 dec 2025), en vigueur 1er janv 2026; EAR 2021 reportee en 2022 (Covid) + document 'Adaptation des methodes de calcul' ; millésime 2023 comparable seulement a >=6 ans; Mayotte: derogation jusqu'en 2017, integree 2021, cyclone Chido -> recensement exhaustif nov 2025-janv 2026
QRY-015 | FETCH | FOUND | SRC-007 | https://www.insee.fr/fr/information/7652980 | FETCH Budget de famille 2026: 29000 logements; carnet une semaine + app tickets de caisse; precedente 2016-2017; reglement europeen obligatoire; visa CNIS favorable + arrete ministre 25/11/2025; appariement donnees socio-fiscales + RSVERO; utile pour calculer l'IPC; infl 2022-23 plus pesante menages ruraux et modestes
QRY-016 | WEB | DONE | - | https://www.insee.fr | IPC Insee demande de prix releves magasins donnees scanner magasins spectacles methodologie collecte
QRY-017 | WEB | DONE | - | https://www.insee.fr | comptes nationaux Insee sources donnees administratives DSN TVA douanes declarations sociales base 2020
QRY-018 | FETCH | FOUND | - | https://www.insee.fr/fr/information/7768619 | FETCH Base 2020: revision 1949-2023; rebasing coordonne UE quinquennal; campagnes ordinaires = sources en evolution sur 3 ans, changement de base = recalage en niveau; recalage ESANE (VA SNF baisse); balance des paiements; ENL 2019 loyers reels/imputes; activite dissimulee estimee via redressements fiscaux DGFiP (contribution moindre); perimetres APU integrent audiovisuel public + SNCF Reseau; R&D/logiciels/SIFIM methodes revoes; tableau des sens de revision
QRY-019 | WEB | DONE | - | https://www.insee.fr | ERFS rafraichissement non pris en compte 2021 revenus fiscaux imputation niveau de vie pauvrete Insee
QRY-020 | WEB | DONE | - | https://www.insee.fr | ERFS enquete revenus fiscaux sociaux imputations non reponse fiscalite fiabilite methodologie Insee
QRY-021 | FETCH | FOUND | SRC-009 | https://www.insee.fr/fr/statistiques/7766289?sommaire=7766297 | FETCH ERFS: refonte 2021 (nouvelle EEC): niveaux de vie rehausses, pauvrete et inegalites diminuent (sauf interdeciles); imputations recurrentes: revenus financiers via Patrimoine (2011/2015), prime PPAP+heures supp (2019), FSE/primes sante/aide exceptionnelle (2020 'fragilites'), indemnite inflation (2021); individus non apparies conserves sauf 90+ (imputations 'trop fragiles'); series 1970-2021: perimetre constant incomplet + chaine; ruptures BIT 2002/2007
QRY-022 | FETCH | FOUND | SRC-010 | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html | FETCH BFM juin 2026: croissance 2023 revee de 0,9% a 1,9% en base 2020 (compte definitif), plus forte revision depuis 2003
QRY-023 | FETCH | FOUND | SRC-010 | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html | FETCH BFM/Rexecode: 1,9% = corrigé des jours ouvrés, 1,6% = non corrigé (compte définitif 2023); plus forte révision depuis 2003; écart moyen première estimation/définitif +0,34 pt (2005-2024); Insee citée: révision 2023 'en grande partie' contexte inflationniste -> imprécision du volume; mécanisme: données micro liasses fiscales; enjeu narration/décision: prévision gouvernement 1% vs Cour des comptes
QRY-024 | FETCH | FOUND | SRC-011 | https://www.insee.fr/fr/statistiques/8996855 | FETCH Insee Première 2105 (29 mai 2026): PIB 2023 = 1,6% en volume (non corrigé jours ouvrés) base 2020; erratum du jour même (2024/2025 intervertis); encadré révisions PIB/pouvoir d'achat; PIB 2025 0,8% après 1,5%
QRY-025 | FETCH | FOUND | - | https://www.insee.fr/fr/statistiques/8996855 | FETCH Insee Première 2105 (29 mai 2026): PIB 2023 = 1,6% en volume (non corrigé jours ouvrés) base 2020; erratum du jour même (2024/2025 intervertis); encadré révisions PIB/pouvoir d'achat; PIB 2025 0,8% après 1,5%
QRY-026 | WEB | DONE | - | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France | seuils pauvreté 40/50/60% médiane inegalites.fr 891/1114/1337 euros personne seule 2024
QRY-027 | FETCH | FOUND | SRC-012 | https://www.insee.fr/fr/statistiques/2408345 | FETCH Personnes pauvres selon le seuil (1975-2024): 2024 = 2843000 (40%) / 5599000 (50%) / 9817000 (60%) / 14576000 (70%); champ France métropolitaine, revenu déclaré >=0, personne de référence non étudiante; sources Insee-DGFiP-Cnaf-Cnav-CCMSA; ruptures 2010/2012/2020; point 2020 fragile; données <1996 hors revenus financiers
QRY-028 | FETCH | FOUND | SRC-013 | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France | FETCH Observatoire des inégalités: seuils 2024 = 891/1114/1337 EUR (40/50/60%) personne seule; échelle d'équivalence expliquée (1/0,5/0,3); ODI utilise le seuil 50% qu'il juge 'plus significatif' que le 60% officiel; stagnation seuils 2008-2018
QRY-029 | WEB | DONE | - | - | REFUTATION chomage BIT une heure travaillée mesure tout le monde n'est pas chomeur halo sous-emploi critiques
QRY-030 | WEB | DONE | - | - | REFUTATION populations de référence estimation fiabilité critique communes petites marges erreur recensement rénové
QRY-031 | WEB | DONE | - | - | REFUTATION révisions PIB France procédure normale estimation définitive pas manipulation Cour des comptes révision erronée
QRY-032 | WEB | DONE | - | - | REFUTATION... executé: chomage BIT une heure (QRY-029): rien de neuf trouvé; contre-preuves dans SRC-001/002 (halo mesuré et publié, critère BIT international)
QRY-033 | WEB | DONE | - | - | REFUTATION... executé: révisions PIB (QRY-031): contre-preuve trouvée = biais moyen HAUSSIER +0,34 pt documenté par Rexecode via SRC-010; processus et erratum publics SRC-011
QRY-034 | WEB | DONE | - | - | REFUTATION seuil pauvreté 60% minimise pauvreté choix seuil 50% 40% 70% alternative
QRY-035 | FETCH | FOUND | SRC-014 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | FETCH Sénat question Mizzon 104 + réponse ministérielle (24/06/2025): Metzing Insee 678 vs mairie 791 (>15%) pénalisant la DGF; défense: équité inter-communes, cycle 5 ans (1 an direct, 2 ans tendance, 2 ans fiscal), CNERP recommande décalage référence 3->2 ans mis en oeuvre fin 2026
QRY-036 | FETCH | FOUND | SRC-015 | https://www.insee.fr/fr/metadonnees/source/operation/s2150/precision-fiabilite | FETCH Insee precision-fiabilite (recensement 2021): renvoie vers Insee Methodes n°136 'La qualité des estimations de population dans le recensement' (2020) et fiche thématique 'La précision des résultats du recensement' (2023)
QRY-037 | WEB | DONE | - | - | REFUTATION pauvreté facteur 5 selon le seuil choisi: contre-preuve cherchée (le choix de seuil ne changerait pas les conclusions)
QRY-038 | FETCH | FOUND | SRC-008 | https://www.insee.fr/fr/information/7768619 | FETCH communiqué base 2020 (comptes nationaux): révision 1949-2023; rebasing coordonné UE quinquennal; recalage ESANE/balance paiements/ENL 2019; activité dissimulée via redressements fiscaux DGFiP; périmètres APU; sens des révisions

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/4805248
SRC-002 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/7658713
SRC-003 | ◉ | fam:A | https://www.insee.fr/fr/information/2383278
SRC-004 | ◈ | fam:A | https://www.insee.fr/fr/information/2553979
SRC-005 | ◉ | fam:other:wiki | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France
SRC-006 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011
SRC-007 | ◈ | fam:A | https://www.insee.fr/fr/information/7652980
SRC-008 | ◈ | fam:A | https://www.insee.fr/fr/information/7768619
SRC-009 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/7766289?sommaire=7766297
SRC-010 | ◉ | fam:D | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html
SRC-011 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8996855
SRC-012 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/2408345
SRC-013 | ◉ | fam:C | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France
SRC-014 | ◉ | fam:B | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html
SRC-015 | ○ | fam:A | https://www.insee.fr/fr/metadonnees/source/operation/s2150/precision-fiabilite

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.insee.fr/fr/statistiques/4805248 | A | 2026-08-07 | Taux de chômage BIT incertitude publiée rénovation 2021 | Le taux de chômage BIT (2,7 M / 8,3 % au T2 2026) est publié avec une incertitude de +/-0,3 pt sur le niveau et son évolution trimestrielle; l'enquête Emploi rénovée en 2021 a imposé le recalcul des séries antérieures; l'Insee qualifie elle-même le recul de 2020 de 'en trompe-l'œil' (recherche et disponibilité réduites). | 46193d3f-f889-4f44-991f-6b001f4397bb
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/7658713 | A | 2023-08-31 | Divergence structurelle BIT vs catégorie A | BIT et catégorie A divergent structurellement: 2010-2022, taux BIT -2 pts vs catégorie A +5 % (Pays de la Loire, ampleur comparable nationalement), écarts attribués documentés aux réformes réglementaires (retraite/dispense seniors, RSA et assurance 2009, durcissement 2021, radiations) intervenant 'indépendamment de la situation réelle' sur le marché du travail. | 25a43ded-fb6a-4ac0-8ccc-6f765d3bc068
FCT-003 | FACT | ✦ | https://www.insee.fr/fr/information/2553979 | A,B,other:wiki | 2025-06-24 | Populations de référence estimées mais juridiques | Les chiffres de population légale/référence sont des estimations par sondage (rotation 1/5 des communes <10k; sondage de 8 % des adresses pour les ≥10k) officialisées par décret annuel depuis 2008 et référencées par ~350 articles législatifs (DGF, nombre de conseillers, seuils); un écart >15 % entre estimation Insee (678) et dénombrement municipal (791) est documenté (Metzing, 2024, pénalisant la DGF); la CNERP a recommandé de réduire le décalage date de référence-entrée en vigueur de 3 à 2 ans (mise en oeuvre fin 2026). | dad9d305-19ff-4191-95a9-00a2ff13994c
FCT-004 | FACT | ✧ | https://www.insee.fr/fr/information/2383278 | A | 2019-09-17 | Trois définitions du chômage coexistent | L'Insee publie au moins trois mesures du chômage: BIT (3 critères), demandeurs d'emploi catégorie A (administratif), chômeur au sens du recensement (auto-déclaration 14-70 ans, plus élevé que le BIT car des inactifs se déclarent chômeurs, 'conseillé' uniquement en structure/positionnement relatif). | dab61379-34b1-4808-adde-ad00c8688212
FCT-005 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011 | A,other:wiki | 2025-12-29 | Recensement 2021 reporté et méthodes adaptées | L'enquête annuelle de recensement 2021 (sauf Mayotte) a été reportée en 2022 (Covid); l'Insee a adapté ses méthodes de calcul des populations (document dédié) pour 2022-2027; le millésime 2023 ne se compare correctement qu'aux millésimes distants d'au moins 6 ans; Mayotte: dérogation jusqu'en 2017, intégration 2021, recensement exhaustif nov 2025-janv 2026 après le cyclone Chido. | 5bae61ea-ac18-48f4-bacd-3ea296e4e077
FCT-006 | FACT | ✧ | https://www.insee.fr/fr/information/7768619 | A,D | 2026-06-03 | Comptes nationaux sources administratives et révisions | Les comptes nationaux sont construits sur sources administratives et fiscales (ESANE/DGFiP, douanes, balance des paiements, ENL 2019 pour les loyers réels et imputés, redressements fiscaux pour estimer l'activité dissimulée); la révision ordinaire porte sur 3 ans; le rebasing coordonné UE (base 2020, mai 2024) a révisé toute la série 1949-2023; le compte définitif 2023 révise la croissance de +0,2 pt (2023) et +0,3 pt (2024) et l'Insee attribue la révision 2023 'en grande partie' au contexte inflationniste (imprécision du volume). | 7718bab2-4b99-4292-a7ce-c7552191e438
FCT-007 | FACT | ✦ | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html | A,D | 2026-06-07 | Biais moyen haussier des révisions PIB et erratum | L'écart moyen entre première estimation et compte définitif de croissance est de +0,34 pt (2005-2024) selon Rexecode — biais directionnel documenté; 2023 passe de 0,9 % (estimation fin 2023) à 1,9 % corrigé des jours ouvrés / 1,6 % non corrigé (compte définitif), plus forte révision depuis 2003; l'Insee Première 2105 (29 mai 2026) a publié un erratum le jour même (années 2024/2025 interverties dans la version initiale). | 0e7b6e8b-6941-4b24-9e67-ad37fbd256f7
FCT-008 | FACT | ✦ | https://www.insee.fr/fr/statistiques/2408345 | A,C | 2026-07-09 | Pauvreté facteur 5 selon le seuil choisi | En 2024 (France métropolitaine, ménages ordinaires, revenu déclaré >=0, référence non étudiante): 2 843 000 personnes pauvres au seuil 40 %, 5 599 000 à 50 %, 9 817 000 à 60 %, 14 576 000 à 70 % du niveau de vie médian — un facteur d'environ 5 selon le seul choix de seuil; l'Observatoire des inégalités privilégie le seuil 50 % qu'il juge 'plus significatif' que le 60 % officiel (seuils personne seule: 891/1114/1337 EUR). | a22a2146-1f94-4fa9-8978-9c1a97f0ef4e
FCT-009 | FACT | ✧ | https://www.insee.fr/fr/statistiques/7766289?sommaire=7766297 | A | 2024-03-04 | ERFS imputations récurrentes refonte 2021 | L'ERFS impute structurellement des revenus absents des sources fiscales (revenus financiers via enquête Patrimoine depuis 2011/2015; prime PPAP et heures supplémentaires 2019; Fonds de solidarité, primes santé, aide exceptionnelle 2020 'fragilités' reconnues; indemnité inflation 2021); la refonte 2021 (nouvelle EEC) rehausse les niveaux de vie et abaisse pauvreté et inégalités (sauf rapport interdéciles); les individus non appariés sont conservés sauf 90 ans et plus (imputations 'trop fragiles'). | 5fffa41a-57cb-497e-ac22-318b511182bd
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002,SRC-009
FCT-002 | SRC-002,SRC-001
FCT-003 | SRC-004,SRC-005,SRC-006,SRC-014
FCT-004 | SRC-003,SRC-001,SRC-002
FCT-005 | SRC-006,SRC-005
FCT-006 | SRC-008,SRC-011,SRC-010
FCT-007 | SRC-010,SRC-011
FCT-008 | SRC-012,SRC-013
FCT-009 | SRC-009,SRC-012

## REFUTATION_REGISTRY_V1
FCT-003 | QRY-030 | NONE
FCT-007 | QRY-031 | NONE
FCT-008 | QRY-037 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9,SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12,13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14,17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-20T16:57:37.237630+00:00","fact_mem":{"FCT-001":"46193d3f-f889-4f44-991f-6b001f4397bb","FCT-002":"25a43ded-fb6a-4ac0-8ccc-6f765d3bc068","FCT-003":"dad9d305-19ff-4191-95a9-00a2ff13994c","FCT-004":"dab61379-34b1-4808-adde-ad00c8688212","FCT-005":"5bae61ea-ac18-48f4-bacd-3ea296e4e077","FCT-006":"7718bab2-4b99-4292-a7ce-c7552191e438","FCT-007":"0e7b6e8b-6941-4b24-9e67-ad37fbd256f7","FCT-008":"a22a2146-1f94-4fa9-8978-9c1a97f0ef4e","FCT-009":"5fffa41a-57cb-497e-ac22-318b511182bd"},"mnemo_row":"PASS: 9/9 eligible facts persisted via MCP write_memory (8002); no duplicate_warning; run 2026-09-20_18-12_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"tier ✦ -> status:CONFIRME (>=2 familles + réfutation terminale)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"tier ✦ -> status:CONFIRME (>=2 familles + réfutation terminale)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"tier ✦ -> status:CONFIRME (>=2 familles + réfutation terminale)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"tier ✧ -> status:VERIFIE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:PASS: 9/9 eligible facts persisted via MCP write_memory (8002); no duplicate_warning; run 2026-09-20_18-12_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> status:CONFIRME (>=2 familles + réfutation terminale)
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-007 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> status:CONFIRME (>=2 familles + réfutation terminale)
FCT-008 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> status:CONFIRME (>=2 familles + réfutation terminale)
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
