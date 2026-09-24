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
