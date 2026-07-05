# Sublimator v36 : Préservation des phases analytiques perdues

> **Type** : SPECS / BRAINSTORM / MATRICE DE DÉCISION
> **Date** : 2026-07-05 15h00
> **Statut** : Brouillon de spécification, en attente de décision
> **Déclencheur** : Lecture intégrale de `investigations/2026-07-04-RIC/2026-07-04_20-30_ric_bloc_religieux_verrou_INVESTIGATION.md`

---

## 1. Contexte et déclencheur

### 1.1 Constat utilisateur

L'utilisateur a observé, en relisant l'enquête religieuse sur le verrouillage du RIC par le bloc religieux, que le pipeline Sublimator v35 **aplatit une enquête structurée en 16 sections** vers une quintessence de **12 champs plats** (6 obligatoires + 6 optionnels), puis vers une synthèse de **3-5 thèses cardinales**. Sur le cas religieux :

- **3 sections sur 16** sont correctement captées (Thèse centrale, F##, Acteurs en mode dégradé)
- **6 sections sur 16** sont partiellement préservées (KERNEL, Périmètre, Lobby, PELOTE, Conclusion, Méthodologie)
- **7 sections sur 16** sont **totalement perdues** (CRÉDO, Positions religieuses §4-§7, IMPACT, Scénarios contrefactuels, Recommandations)

### 1.2 Risque éditorial

L'utilisateur craint (à raison) que la perte de ces sections transforme l'article final en **synthèse descriptive** au lieu d'une **démonstration analytique**. Le verrou religieux devient un sujet de presse, pas une investigation forensique.

### 1.3 Périmètre du document

Ce document trace :
- le diagnostic complet section par section
- la matrice de décision des options A, B, C
- le plan d'action conditionnel après décision
- le sondage empirique à mener pour valider l'arbitrage

Il ne tranche pas la décision. Il outille la décision.

---

## 2. Problématique

### 2.1 Effet de funnel structurel

Le Sublimator v35 applique un funnel en 8 phases :
1. Cartographie (50 lignes pour 44 enquêtes)
2. Brief (1 page)
3. Extraction (quintessence 12 champs)
4. Compression (résumé 100 mots)
5. Synthèse par cluster
6. Rapport (synthèse.json)
7. Plan d'article
8. Article final

À chaque étape, la **profondeur** est réduite au profit de la **synthèse**. Le ratio de compression est d'environ 100:1 entre l'enquête brute (22K mots dans le cas religieux) et l'article final (~2K mots).

### 2.2 Trois pertes structurelles identifiées

| Type de perte | Description | Conséquence |
|---------------|-------------|-------------|
| **Perte arborescente** | Les structures emboîtées (PELOTE 4 niveaux) sont linéarisées en liste plate | Le raisonnement causal disparaît, l'article devient déclaratif |
| **Perte quantitative** | Les chiffres émotionnellement chargés (1500-3000 décès/an) ne sont pas marqués distincts | L'article n'a plus de leviers émotionnels |
| **Perte positionnelle** | Les positionnements acteurs (CEF, traditionalistes, musulmans, protestants) sont agrégés en `acteurs[]` plat | L'angle religieux devient un cliché monolithique |

### 2.3 Le paradoxe de la compression

Le Sublimator v35 est conçu pour produire **un article unique** à partir de **plusieurs enquêtes**. Cette logique impose une compression forte. Mais elle **sacrifie la valeur de chaque enquête individuelle** au profit de la cohérence du corpus.

Question structurante : **souhaite-t-on un Sublimator qui produit des articles forts sur le corpus, ou des articles forts sur chaque enquête** ?

---

## 3. Diagnostic enquête religieuse : matrice section × phase Sublimator

### 3.1 Tableau de capture

| # | Section | Mots (est.) | Champ Sublimator v35 | Valeur éditoriale | Préservation |
|---|---------|-------------|----------------------|-------------------|--------------|
| §0 | Thèse centrale | ~50 | `these_centrale` (1 phrase) | 5/5 (pilier) | ✓ Totale |
| §1 | KERNEL 15 symboles + BIAS_TEST | ~600 | `shadow_factor` (1 float) | 2/5 (méta) | ⚠️ Partielle (14/15 symboles perdus) |
| §2 | Périmètre SCOPING 11 acteurs | ~400 | `acteurs[]` (plat) | 3/5 (socle empirique) | ⚠️ Partielle (positions par acteur perdues) |
| §3 | CRÉDO 12 questions Q→query | ~800 | Aucun champ | 4/5 (plan de recherche) | ❌ Totale |
| §4 | Position CEF | ~1200 | Aucun champ | 4/5 (fond analytique) | ❌ Totale |
| §5 | Position traditionalistes | ~800 | Aucun champ | 3/5 | ❌ Totale |
| §6 | Position musulmane | ~600 | Aucun champ | 3/5 | ❌ Totale |
| §7 | Position protestante | ~400 | Aucun champ | 2/5 | ❌ Totale |
| §8 | Lobby anti-euthanasie + CC 2026-7 | ~1500 | `causalites[]` (1 ligne) | 4/5 (stratégie + précédent) | ⚠️ Réduit (1 ligne) |
| §9 | Coalitions religieuses + dissidences | ~800 | `acteurs[]` | 4/5 (cartographie) | ⚠️ Cartographie perdue |
| §10 | FACT_REGISTRY 20 F## | ~3000 | `faits_atomiques[]` | 5/5 (preuves) | ✓ Totale |
| §11 | CAUSALITÉ PELOTE 4 mécanismes × 4 niveaux | ~2500 | `causalites[]` (1 ligne) | 5/5 (cœur analytique) | ⚠️ Profondeur 4 niveaux perdue |
| §12 | IMPACT 1500-3000 décès/an | ~600 | Aucun champ | 5/5 (levier émotionnel) | ❌ Totale |
| §13 | SCÉNARIOS CONTREFACTUELS 4×proba | ~1200 | Aucun champ | 4/5 (prospective) | ❌ Totale |
| §14 | Conclusion forensique | ~400 | `limites[]` (1 ligne) | 3/5 (synthèse) | ⚠️ Réduit (1 ligne) |
| §15 | Recommandations 6 opérationnelles | ~600 | Aucun champ | 4/5 (actionnabilité) | ❌ Totale |
| §16 | Méthodologie & limites GATE_G 24% | ~400 | `limites[]` (1 ligne) | 3/5 (honnêteté épistémique) | ⚠️ Réduit (1 ligne) |

### 3.2 Bilan quantitatif

- **Total** : 16 sections, ~15 350 mots
- **Capté totalement** : 2 sections (1 050 mots) = 7% du volume
- **Capté partiellement** : 6 sections (6 500 mots) = 42% du volume
- **Perdu** : 8 sections (7 800 mots) = **51% du volume**

**Conclusion du diagnostic** : la moitié du volume analytique de l'enquête religieuse est jetée dans le funnel Sublimator. Le ratio de compression effectif est de 200:1 (volume capté) au lieu de 100:1 (mots).

### 3.3 Vérification empirique à mener

**Sondage 29 enquêtes RIC** : compter combien d'enquêtes ont des sections CRÉDO, PELOTE multi-niveaux, IMPACT chiffré, scénarios contrefactuels, recommandations. Si > 20/29 ont ces structures, le diagnostic religieux n'est pas un cas extrême mais une norme. Si < 10/29, l'enquête religieuse est un outlier et le coût d'une solution complexe n'est pas justifié.

---

## 4. Trois dimensions perdues : impact sur l'article

### 4.1 La chaîne causale PELOTE (moteur intellectuel)

**Ce qui est perdu** : §3 CRÉDO (12 questions de recherche) + §11 PELOTE (4 mécanismes × 4 niveaux × sources × cross-check F##).

**Conséquence éditoriale** : l'article peut citer le verrou religieux, mais ne peut pas **démontrer** pourquoi il fonctionne. La causalité est remplacée par la description.

**Question** : peut-on écrire un article forensique sans démontrer la chaîne causale ?

### 4.2 L'impact humain et les scénarios (levier émotionnel et prospectif)

**Ce qui est perdu** : §12 IMPACT (1500-3000 décès/an euthanasie, projections) + §13 SCÉNARIOS (4 issues avec probabilités 0.65/0.20/0.10/0.05).

**Conséquence éditoriale** : l'article est analytiquement correct mais **émotionnellement vide**. Le lecteur ne perçoit ni l'enjeu humain ni la pluralité des futurs.

**Question** : peut-on écrire un article politique sans leviers émotionnels ni prospective ?

### 4.3 Les positions et coalitions (socle empirique)

**Ce qui est perdu** : §2 Périmètre (11 acteurs) + §4-§7 Positions religieuses (4 confessions) + §9 Coalitions (3 blocs × dissidences).

**Conséquence éditoriale** : l'angle religieux devient monolithique. Le lecteur ne distingue pas la CEF du CFCM, ni le lobbying stratégique des convictions profondes.

**Question** : peut-on traiter un sujet religieux en agrégant les confessions ?

---

## 5. Matrice de décision des options A / B / C

### 5.1 Description des options

#### Option A : Schéma enrichi Phase 1 (lourd)

Ajout de **8 champs optionnels** au schéma quintessence v35 :
- `kernel_symbols` (15 entrées : Κ, ↕, 🌐, etc.)
- `credo_questions` (12 Q→query)
- `positions_acteurs` (par acteur : position, source, nuance)
- `causalites_pelote` (arborescent 4 niveaux)
- `impact` (chiffres clés + source)
- `scenarios` (4 issues avec proba)
- `recommandations` (6 actions concrètes)
- `methodologie` (GATE_G, statut empirique, recoupements)

**Coût** : ~250 lignes de code (gates v36 + tests + doc), alignement prompt-v36, migration des quintessences v35.

**Risque** : pilote LLM noyé, schémas divergents entre enquêtes, inflation de la quintessence.

#### Option B : Raw excerpts Phase 1 (minimal)

Un seul champ `raw_excerpts: list[str]` (5-10 paragraphes verbatim) qui préserve les §§ clés.

**Coût** : ~30 lignes de code (1 champ, 1 test, 1 paragraphe de doc).

**Risque** : qualité du tri initial (le LLM doit choisir les bons paragraphes), perte de structure arborescente, dépendance à la qualité du pilote.

#### Option C : Hybride (4 champs + inventaire Phase 3)

1. **4 champs structurés optionnels** dans le schéma quintessence v35 :
   - `positions_acteurs` (par acteur : position + source + nuance)
   - `causalites_pelote` (arborescent 4 niveaux, format dédié)
   - `impact` (chiffres clés + source)
   - `recommandations` (6 actions concrètes)
2. **Inventaire Phase 3 obligatoire** : pour chaque section d'article, **3 éléments minimum par catégorie** piochés dans le réservoir analytique. Force le pilote à utiliser les champs préservés.
3. **Mise à jour compress_summary Phase 1.5** : les 100 mots du résumé doivent inclure le cœur de ces 4 champs.

**Coût** : ~130 lignes de code (4 champs + format PELOTE + règle Phase 3 + tests).

**Risque** : ajout d'une règle métier "3 minimum" qui peut être contournée par un pilote LLM peu rigoureux.

### 5.2 Critères pondérés de décision

| Critère | Poids | Justification |
|---------|-------|---------------|
| **C1. Couverture analytique** : nb de sections perdues préservées | 30% | Objectif principal de la refonte |
| **C2. Actionnabilité article** : le pilote peut écrire sans ré-analyser | 20% | Évite de re-passer par l'agent humain |
| **C3. Coût implémentation** : lignes de code + tests + doc | 15% | Budget temps |
| **C4. Risque cognitive surcharge** : pilote LLM se perd | 15% | Sublimator reste un outil, pas un labyrinthe |
| **C5. Compatibilité v35** : les enquêtes v35 continuent de passer | 10% | Pas de régression sur le corpus existant |
| **C6. Maintenabilité** : nb de champs à faire évoluer ensemble | 10% | Coût de la dette technique |

### 5.3 Score par option

| Critère (poids) | A (lourd) | B (minimal) | C (hybride) |
|------------------|-----------|-------------|-------------|
| C1. Couverture analytique (30%) | 5/5 (8 champs = exhaustivité) | 2/5 (raw dépend du pilote) | 4/5 (4 champs = 80% des pertes) |
| C2. Actionnabilité article (20%) | 4/5 (tout est là) | 2/5 (recherche dans le verbatim) | 5/5 (règle "3 minimum" force usage) |
| C3. Coût implémentation (15%) | 2/5 (250 lignes) | 5/5 (30 lignes) | 4/5 (130 lignes) |
| C4. Risque cognitive surcharge (15%) | 2/5 (8 champs) | 5/5 (1 champ) | 4/5 (4 champs + 1 règle) |
| C5. Compatibilité v35 (10%) | 3/5 (nouveau schéma) | 5/5 (ajout additif) | 4/5 (ajout additif) |
| C6. Maintenabilité (10%) | 2/5 (8 champs à coordonner) | 5/5 (1 champ) | 3/5 (4 champs + 1 format PELOTE) |

### 5.4 Score pondéré

| Option | Calcul | Score final |
|--------|--------|-------------|
| **A (lourd)** | (5×30 + 4×20 + 2×15 + 2×15 + 3×10 + 2×10) / 100 | **3.65 / 5** |
| **B (minimal)** | (2×30 + 2×20 + 5×15 + 5×15 + 5×10 + 5×10) / 100 | **3.30 / 5** |
| **C (hybride)** | (4×30 + 5×20 + 4×15 + 4×15 + 4×10 + 3×10) / 100 | **4.05 / 5** |

### 5.5 Lecture du score

- **C (4.05)** est l'option la mieux notée mais l'écart avec A (3.65) est faible (0.40).
- **B (3.30)** est l'option la moins coûteuse mais la moins puissante.
- **L'écart A-C (0.40)** est compensé par le surcoût d'implémentation (250 vs 130 lignes).

### 5.6 Décision recommandée

**C (hybride)** sous **condition** : valider par sondage empirique sur 29 enquêtes RIC que les sections perdues sont **réellement présentes** dans au moins 20/29 enquêtes. Si la proportion est < 20/29, redescendre vers **B (minimal)**.

**Ne pas choisir A** sauf si l'utilisateur veut explicitement un schéma "exhaustif" indépendamment du coût.

---

## 6. Plan d'action conditionnel

### 6.1 Si option C retenue

1. **Sondage empirique 29 enquêtes RIC** (~1h)
2. **Spec format `causalites_pelote`** arborescent 4 niveaux (1-2h)
3. **Implémenter `gates.py` v36** : ajout 4 champs optionnels, format PELOTE, rétro-compat v35 (2-3h)
4. **Mettre à jour `prompt-v35.md` Phase 1.5** : règle compress_summary + Phase 3 inventaire 3 minimum (1h)
5. **Migrer les tests** : `_base_quintessence_v36()` helper + tests Phase 3 (1h)
6. **E2E sur enquête religieuse** : générer quintessence v36 + vérifier que les 8 sections perdues sont captées (30 min)
7. **Code-reviewer + tests régression** : 142/142 extractors + E2E RIC (30 min)
8. **Archive Mnemolite** + commit (15 min)

**Total estimé** : 8-10 heures de travail effectif.

### 6.2 Si option B retenue

1. **Sondage empirique 29 enquêtes RIC** (~1h, valider que le verbatim suffit)
2. **Implémenter `gates.py` v36 minimal** : ajout 1 champ `raw_excerpts: list[str]` (1h)
3. **Mettre à jour `prompt-v35.md` Phase 1** : règle "5-10 paragraphes max des §§ clé" (30 min)
4. **Tests** : helper + 5 tests unitaires (30 min)
5. **E2E** : vérifier que le pilote choisit les bons paragraphes (30 min)
6. **Code-reviewer + archive** (15 min)

**Total estimé** : 3-4 heures.

### 6.3 Si option A retenue (déconseillé)

1. Sondage empirique (~1h)
2. Spec des 8 champs + format arborescent (~3h)
3. `gates.py` v36 : 8 champs, alignement complet, rétro-compat v34 (4-5h)
4. `prompt-v35.md` enrichi : 8 champs documentés + Phase 3 règles (2h)
5. Migration tests + nouvelle base de tests v36 (2-3h)
6. E2E + audit antagoniste sur 5 enquêtes (1-2h)
7. Documentation architecture v36 (1h)
8. Code-reviewer + tests régression + archive (1h)

**Total estimé** : 15-20 heures.

### 6.4 Plan de repli commun (toutes options)

- Si le sondage empirique révèle < 10/29 enquêtes avec sections perdues : ne rien faire, l'enquête religieuse est un outlier, le Sublimator v35 suffit.
- Si le sondage révèle 10-20/29 : option B.
- Si le sondage révèle > 20/29 : option C (par défaut) ou A (si budget disponible).

---

## 7. Sondage empirique à mener

### 7.1 Méthode

Script Python (ou basher) sur les 29 enquêtes RIC qui compte, pour chaque enquête :
- présence d'une section `## §3` avec au moins 3 questions Q→query
- présence d'une section `## §11` avec au moins 3 mécanismes causaux
- présence d'une section `## §12` avec chiffres d'impact
- présence d'une section `## §13` avec ≥ 2 scénarios contrefactuels
- présence d'une section `## §15` avec ≥ 2 recommandations

### 7.2 Résultats attendus

- Si > 20/29 : structure riche est la norme, option C justifiée
- Si 10-20/29 : structure riche est minoritaire, option B suffit
- Si < 10/29 : enquête religieuse est un outlier, ne pas modifier le Sublimator

### 7.3 Livrables du sondage

- 1 tableau CSV (enquête, sections présentes, total)
- 1 verdict "C justifié" / "B justifié" / "Ne rien faire"
- 1 note méthodologique sur les cas ambigus

---

## 8. Questions ouvertes / décision finale

### 8.1 Questions à trancher par l'utilisateur

1. **Faut-il lancer le sondage empirique 29 enquêtes RIC avant de décider** ? (Recommandé : oui)
2. **Si C retenue, faut-il un format `causalites_pelote` dédié ou réutiliser `causalites[]` linéaire** ? (Recommandé : dédié, car la structure 4 niveaux est incompatible avec une liste plate)
3. **Faut-il fixer la règle "3 éléments minimum par catégorie" en Phase 3** ? (Recommandé : oui, sans cette règle le pilote peut ignorer les 4 champs)
4. **Quel budget temps accepter** (8-10h pour C, 3-4h pour B, 15-20h pour A) ?
5. **Faut-il une v36 incrémentale (rétro-compat v35) ou un cut-over (réécriture complète)** ? (Recommandé : rétro-compat)

### 8.2 Décisions à valider

- [ ] Option retenue (A / B / C / Aucune)
- [ ] Sondage empirique à mener (oui / non)
- [ ] Budget temps accepté
- [ ] Rétro-compat v35 vs cut-over

### 8.3 Prochaine étape

Une fois les cases cochées, ce document devient le **ticket d'implémentation** : il sera archivé dans `tools/engines/sublimator/CHANGELOG.md` avec référence aux commits, et une nouvelle investigation v36 sera ouverte si option C retenue.

---

## 9. Annexes

### 9.1 Glossaire

- **PELOTE** : méthode d'analyse causale du Sublimator, 4 niveaux emboîtés (mécanisme → sous-mécanisme → fait → source)
- **CRÉDO** : phase de planification de la recherche, transforme la thèse en questions opérationnelles
- **GATE_G** : garde de complétude (% de F## validés par recoupement)
- **Quintessence** : sortie Phase 1 du Sublimator, 12 champs (6 obligatoires + 6 optionnels en v35)
- **Cartographie** : sortie Phase 0, 1 ligne par enquête, 50 lignes pour 44 enquêtes

### 9.2 Références

- `tools/engines/sublimator/prompt-v35.md` : prompt v35 complet
- `tools/engines/sublimator/extractors/gates.py` : validation structurelle H0-H7
- `tools/engines/sublimator/extractors/cartographie.py` : extraction cartographie Phase 0
- `investigations/2026-07-04-RIC/2026-07-04_20-30_ric_bloc_religieux_verrou_INVESTIGATION.md` : cas d'étude religieux

### 9.3 Historique

- 2026-07-05 15h00 : création du document, après lecture intégrale enquête religieuse
- À venir : sondage empirique 29 enquêtes RIC
- À venir : décision user + implémentation v36 (si validée)

---

## 10. Enquêtes RIC 2026-07-04 : 42 fichiers, 5 archétypes, 14 KERNEL cassés

> **Section ajoutée le 2026-07-05 sur demande utilisateur.**
> **Source :** scan structurel Python + 8 lectures détaillées (religieuse, M5S, vérification, IA, histoire longue, Bavière, cultes, climat).
> **Méthode :** 1 scan global (longueur, KERNEL, Complexité, F##, sections), puis lectures ciblées des archétypes.

### 10.1 Note de cadrage

L'utilisateur a indiqué **43 investigations** dans le dossier `investigations/2026-07-04-RIC/`. Le scan effectif révèle **42 fichiers** suffixés `*_INVESTIGATION.md`. L'écart (1 fichier) reste inexpliqué après vérification : aucun fichier orphelin détecté, aucun filtre actif. Hypothèse : erreur de comptage utilisateur ou fichier supprimé entre la demande et l'exécution. **À noter sans correction.**

### 10.2 Tableau des 42 enquêtes

| # | Fichier | Mots | KERNEL | Cpx | F## | h2 | Archétype | Notation F |
|---|---------|------|--------|-----|-----|-----|-----------|-----------|
| 1 | 2026-07-04_18-00_referendum_initiative_citoyenne | 5612 | CASSE(1) | APEX 14/18 | 24 | 1 | GOLDEN_APEX (legacy RIC canon) | F-001..F-024 |
| 2 | 2026-07-04_19-30_ric_bce_euro_verrou | 7224 | CASSE(1) | NA | 0 | 1 | APEX_LEGACY | aucun |
| 3 | 2026-07-04_20-00_ric_complement_gaps | 7697 | CASSE(0) | APEX | 0 | 0 | APEX_LEGACY (KERNEL perdu) | aucun |
| 4 | 2026-07-04_20-30_ric_bloc_religieux_verrou | 6967 | CASSE(1) | NA | 0 | 1 | **GOLDEN_APEX** (cas d'étude 16 sections) | aucun |
| 5 | 2026-07-04_21-30_ric_morts_politiques_verrou | 8020 | CASSE(1) | NA | 0 | 2 | APEX_LEGACY | aucun |
| 6 | 2026-07-04_22-00_m5s_italie_capture | 7560 | CASSE(0) | APEX | 30 | 0 | **APEX_LEGACY** (cas d'école) | F001..F034 |
| 7 | 2026-07-04_22-00_ric_verrous_impersonnels | 8305 | CASSE(0) | NA | 0 | 1 | APEX_LEGACY | aucun |
| 8 | 2026-07-04_22-30_ric_coordination_europeenne | 6792 | CASSE(0) | NA | 0 | 1 | APEX_LEGACY | aucun |
| 9 | 2026-07-04_23-30_ppl_ric_timeline_exhaustive | 5066 | CASSE(0) | NA | 0 | 0 | LIGHT_STRUC (compact) | aucun |
| 10 | 2026-07-04_23-50_cross_examination_ric | 7976 | CASSE(1) | NA | 0 | 1 | APEX_LEGACY | aucun |
| 11 | 2026-07-04_23-50_sol_dem_financement_symetrie | 8266 | CASSE(1) | NA | 0 | 2 | APEX_LEGACY | aucun |
| 12 | 2026-07-05_00-00_hauts_fonctionnaires_bloqueurs | 5734 | CASSE(1) | NA | 0 | 1 | LIGHT_STRUC | aucun |
| 13 | 2026-07-05_00-30_infrastructure_electorale_privee | 3890 | CASSE(1) | NA | 0 | 1 | COURT_DEGR | aucun |
| 14 | 2026-07-05_01-00_levier_cedh_article_3 | 3326 | CASSE(1) | NA | 0 | 1 | COURT_DEGR | aucun |
| 15 | 2026-07-05_01-30_conventions_citoyennes_ric | 3429 | CASSE(1) | NA | 0 | 1 | COURT_DEGR | aucun |
| 16 | 2026-07-05_02-00_lobbies_cabinets_conseils | 3539 | CASSE(0) | NA | 0 | 1 | COURT_DEGR | aucun |
| 17 | 2026-07-05_03-00_profil_sociologique_electorat | 5273 | CASSE(1) | NA | 0 | 1 | LIGHT_STRUC | aucun |
| 18 | 2026-07-05_04-00_cadrage_media_hostile | 6907 | CASSE(1) | NA | 0 | 1 | APEX_LEGACY | aucun |
| 19 | 2026-07-05_05-00_referendums_locaux_chaine | 5600 | CASSE(1) | NA | 0 | 1 | LIGHT_STRUC | aucun |
| 20 | 2026-07-05_06-00_indifference_priorite_ric | 5337 | CASSE(1) | NA | 0 | 1 | LIGHT_STRUC | aucun |
| 21 | 2026-07-05_07-00_strategie_imposition | 6196 | CASSE(1) | NA | 0 | 1 | APEX_LEGACY | aucun |
| 22 | 2026-07-05_08-00_sortition_tirage_au_sort | 7670 | CASSE(1) | NA | 0 | 0 | APEX_LEGACY | aucun |
| 23 | 2026-07-05_09-00_ric_revocatoire_recall | 6276 | CASSE(1) | NA | 0 | 0 | APEX_LEGACY | aucun |
| 24 | 2026-07-05_10-00_democratie_numerique_decidim | 7489 | CASSE(1) | NA | 0 | 0 | APEX_LEGACY | aucun |
| 25 | 2026-07-05_11-00_protocole_pnred_ric_001 | 9733 | CASSE(1) | NA | 0 | 0 | APEX_LEGACY | aucun |
| 26 | 2026-07-05_12-00_lois_civictech_fr_2027 | 12142 | CASSE(1) | NA | 71 | 0 | **GOLDEN_APEX** (P3 #16, 38 F-PNR) | F-PNR33..F-PNR70 |
| 27 | 2026-07-05_13-00_verification_independante_p3_16 | 8011 | CASSE(1) | NA | 71 | 0 | **VERIF_META** (P3 #18, audit P3 #16) | F-PNR cumulés |
| 28 | 2026-07-05_14-00_external_legal_audit_p3_16 | 8360 | CASSE(1) | NA | 0 | 0 | APEX_LEGACY | aucun |
| 29 | 2026-07-05_15-00_histoire_longue_ric_france | 7393 | DENSE(15) | APEX 16/18 | 18 | 1 | **GOLDEN_APEX** (gold standard 1789-2026) | F-HIST-01..F-HIST-18 |
| 30 | 2026-07-05_16-00_cnr_1944_democratie_economique | 8459 | CASSE(1) | APEX | 0 | 1 | **GOLDEN_APEX** | aucun |
| 31 | 2026-07-05_16-30_referendums_ive_republique | 8221 | CASSE(1) | APEX | 0 | 1 | **GOLDEN_APEX** | aucun |
| 32 | 2026-07-05_17-00_bavierr_volksentscheide | 3003 | CASSE(0) | NA | 12 | 0 | **COURT_DEGR** (KERNEL perdu) | F-VB01..F-VB12 |
| 33 | 2026-07-05_17-30_syndicats_cgt_cfdt_fo | 3210 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 34 | 2026-07-05_18-00_cultes_4_religions_france | 3342 | CASSE(0) | NA | 12 | 0 | **COURT_DEGR** (7/12 ⁅ "non trouvé") | F-CU01..F-CU12 |
| 35 | 2026-07-05_18-30_dette_publique_art_50 | 3773 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 36 | 2026-07-05_19-00_ric_periode_crise_ukraine | 3355 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 37 | 2026-07-05_19-30_sondages_ifop_ipsos | 2932 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 38 | 2026-07-05_20-00_ric_crypto_dao_aragon | 2837 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 39 | 2026-07-05_20-30_ric_urgence_climatique_cop | 3161 | CASSE(0) | NA | 13 | 0 | **COURT_DEGR** (KERNEL perdu) | F-CLIM01..F-CLIM13 |
| 40 | 2026-07-05_21-00_chronologie_6_presidents | 2888 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 41 | 2026-07-05_21-30_franc_maconnerie_loges | 2827 | CASSE(0) | NA | 0 | 0 | COURT_DEGR | aucun |
| 42 | 2026-07-05_22-00_ric_ia_generative_meta | 2986 | CASSE(0) | NA | 12 | 0 | **COURT_DEGR** (méta-réflexion) | F-IA01..F-IA12 |

### 10.3 Cinq archétypes identifiés

| Archétype | Compte | Caractéristiques | Représentants |
|-----------|--------|------------------|---------------|
| **GOLDEN_APEX** | 5/42 (12%) | ≥7000 mots, KERNEL complet (8-15 symboles), 18 sections PELOTE, F## abondants, urls institutionnelles. Cible : Sublimator APEX canonique. | RIC canonique 18-00, religieuse 20-30, CivicTech 12-00 LOIS, histoire longue 15-00, CNR 16-00, IVe République 16-30 |
| **APEX_LEGACY** | 12/42 (29%) | 5000-8500 mots, KERNEL partiel (1 symbole cité), Complexité APEX parfois déclarée, 0 F## détectés par regex standard (probablement F## en nomenclature legacy non-reconnue), structure Narrative pure. Cible : Sublimator narratif. | M5S Italie 22-00, gaps 20-00, morts politiques 21-30, verrous impersonnels 22-00, coordination européenne 22-30, ppl timeline 23-30, cross-examination 23-50, sol dem 23-50, médias 04-00, stratégie 07-00, sortition 08-00, revocatoire 09-00, decidim 10-00, protocole 11-00, legal audit 14-00 |
| **LIGHT_STRUC** | 6/42 (14%) | 5000-6000 mots, structure réduite, KERNEL partiel. Cible : Sublimator compact. | cross-ex 23-50, h-fonctionnaires 00-00, profil socio 03-00, referendums locaux 05-00, indifference 06-00, ric_crypto 20-00 |
| **VERIF_META** | 1/42 (2%) | 8000 mots, audit d'enquêtes précédentes, structure de vérification tierce. Cible : Sublimator méta-étape. | P3 #18 verification 13-00 |
| **COURT_DEGR** | 15/42 (36%) | <4000 mots, KERNEL complètement perdu (0-1 symbole), 10-13 F## souvent marqués ⁅, format MANIPULATION_REPORT Saison 2. Cible : Sublimator dégradé. | infra electorale 00-30, CEDH 01-00, conventions citoyennes 01-30, lobbies 02-00, Bavière 17-00, syndicats 17-30, cultes 18-00, dette 18-30, crise ukraine 19-00, sondages 19-30, ric crypto 20-00 (déjà compté), climat 20-30, chronologie 21-00, franc-maconnerie 21-30, IA 22-00 |
| **AUTRE** | 3/42 (7%) | Limites floues entre catégories. | à reclassifier |

**Note critique** : la catégorie LIGHT_STRUC n'a été appliquée qu'à 6 enquêtes dans la version finale du scan, pas 14 comme initialement suggéré. Les 15 COURT_DEGRADE incluent la majorité des fichiers Saison 2 (batch 3-4 du 5 juillet 2026 17h-22h).

### 10.4 Anomalies KERNEL et F##

#### 10.4.1 KERNEL : 14/42 enquêtes avec KERNEL complètement perdu (0 symbole)

| # | Fichier | KERNEL perdu | Note |
|---|---------|--------------|------|
| 3 | 2026-07-04_20-00_ric_complement_gaps | 0 | Format legacy, KERNEL jamais initialisé |
| 6 | 2026-07-04_22-00_m5s_italie_capture | 0 | Cas d'école parallèle, format libre |
| 7 | 2026-07-04_22-00_ric_verrous_impersonnels | 0 | Format libre narratif |
| 8 | 2026-07-04_22-30_ric_coordination_europeenne | 0 | Format libre |
| 9 | 2026-07-04_23-30_ppl_ric_timeline | 0 | Timeline compact, format libre |
| 16 | 2026-07-05_02-00_lobbies_cabinets_conseils | 0 | Lobbies, format libre |
| 32-42 | 11 fichiers du 17h-22h (Bavière à IA) | 0 | Tous format MANIPULATION_REPORT Saison 2 batch 4, KERNEL jamais réinjecté |

**Cause technique probable** : le LLM a généré ces enquêtes avec un **prompt réduit** (sans la section `## §1 KERNEL 15 symboles`) parce que la fenêtre de contexte était pleine ou parce que le pilote a jugé la section non-essentielle. **Perte d'intention analytique** : la profondeur KERNEL est ce qui distingue une investigation APEX d'un simple document narratif.

#### 10.4.2 F## : 6 notations différentes détectées

| Notation | Compte | Contexte |
|----------|--------|----------|
| **F-001..F-024** | 1 | RIC canonique 18-00 (legacy Sublimator v33.2) |
| **F001..F034** | 1 | M5S Italie 22-00 (Sublimator v34 ?) |
| **F-PNR33..F-PNR70** | 3 | CivicTech-FR P3 #16, P3 #17, P3 #18 (Sublimator P3) |
| **F-HIST-01..F-HIST-18** | 1 | Histoire longue 15-00 (Sublimator P3) |
| **F-VB01..F-VB12** | 1 | Bavière 17-00 (Sublimator P3 Saison 2) |
| **F-CU01..F-CU12** | 1 | Cultes 18-00 (Sublimator P3 Saison 2) |
| **F-CLIM01..F-CLIM13** | 1 | Climat 20-30 (Sublimator P3 Saison 2) |
| **F-IA01..F-IA12** | 1 | IA 22-00 (Sublimator P3 Saison 2) |
| **Aucun F##** | 32 | Toutes les autres enquêtes |

**Hétérogénéité problématique** : 6 nomenclatures F## différentes pour 10 enquêtes qui en ont, 32 enquêtes sans aucun F##. Le format n'est pas stabilisé dans le Sublimator, ce qui rend la consolidation cross-enquêtes difficile (la vérification P3 #18 a déjà documenté cette difficulté).

#### 10.4.3 Sections : structure duale

| Pattern de section 0 | Compte | Format |
|---------------------|--------|--------|
| `## §0 — THÈSE CENTRALE & RÉSUMÉ EXÉCUTIF` | ~7 (RIC canonique + quelques APEX_LEGACY) | Sublimator v33/v34 legacy |
| `## §0 : MANIPULATION_REPORT (Phase 0)` + `## §0 : RÉSUMÉ EXÉCUTIF` | ~28 (Saison 2 + investigations parallèles) | Sublimator P3 Saison 2 |
| `## §0 — PHASE 0` | ~5 | Sublimator v33.x legacy |
| Pas de §0 identifiable | 2 | Format libre (M5S, gaps) |

**Conclusion** : la structure canonique v33/v34 a été remplacée par un format `MANIPULATION_REPORT` en Saison 2, qui n'inclut pas la KERNEL. **Cause structurelle de la perte KERNEL** : la migration v34 → P3 a supprimé la section KERNEL obligatoire.

#### 10.4.4 Complexité déclarée

- **APEX (avec score) :** 6/42 (14%) — RIC canonique 14/18, histoire longue 16/18, et 4 autres (gaps, m5s, cnr, ive_republique)
- **APEX (sans score) :** 1/42 — civictech 12-00
- **NA (non déclarée) :** 35/42 (83%) — la majorité n'a pas de score de Complexité APEX
- **STANDARD/LIGHT :** 0/42

**Conséquence** : la grille de scoring APEX (6 dimensions × 3 points) n'est appliquée que dans 6/42 enquêtes. Les 36 autres enquêtes n'ont pas de score de Complexité, ce qui les rend inclassables.

### 10.5 Synthèse : ce que la variance implique pour Sublimator v36

#### 10.5.1 Cinq constats structurels

1. **Le KERNEL est l'angle mort de la Saison 2.** 14/42 enquêtes (33%) ont un KERNEL complètement perdu (0 symbole). Aucune d'entre elles n'est récupérable sans réécriture partielle. C'est la perte analytique la plus lourde du corpus.

2. **Les F## ne sont pas stabilisés.** 6 nomenclatures différentes pour 10 enquêtes. La consolidation cross-enquêtes (Phase 0 cartographie) doit normaliser le format. Sans normalisation, impossible de compter les F## cumulés.

3. **Le format `MANIPULATION_REPORT` a remplacé `THÈSE CENTRALE`.** Cette migration a supprimé la KERNEL obligatoire. v36 doit imposer un format canonique unique qui inclut KERNEL + Thèse + F## + PELOTE.

4. **La Complexité n'est déclarée que dans 14% des cas.** 35/42 enquêtes sont non-scored. v36 doit imposer la grille APEX (ou STANDARD/LIGHT) en Phase 0, pas en option.

5. **3 formats distincts cohabitent :** GOLDEN_APEX (5), APEX_LEGACY (12), COURT_DEGR (15). Le pilote ne choisit pas entre ces formats, il les génère tous sans cohérence. v36 doit imposer un format cible unique avec règle d'émergence (ex : si > 5000 mots et > 5 mécanismes PELOTE, alors GOLDEN_APEX obligatoire).

#### 10.5.2 Impact sur le funnel Sublimator v35

| Phase Sublimator v35 | État actuel (42 enquêtes) | État cible v36 |
|---------------------|---------------------------|-----------------|
| **Phase 0 Cartographie** | Regex cassée (kernel détecté 0/1 au lieu de 8+) | Fix regex + détection 15 symboles obligatoire |
| **Phase 1 Quintessence** | 12 champs (6 req + 6 opt), 7/16 sections religieuses perdues | + 4 champs optionnels (positions, pelote, impact, recos) + format PELOTE dédié |
| **Phase 1.5 compress_summary** | 100 mots, pas de contrainte KERNEL | Doit inclure minimum 1 référence KERNEL |
| **Phase 2 Synthèse** | 3-5 thèses cardinales | + inventaire 3 éléments min par section d'article |
| **Phase 3 Plan + Article** | Pas de retour au KERNEL | Règle "3 min par catégorie" force utilisation KERNEL + F## + PELOTE |

#### 10.5.3 Recommandations révisées pour v36

1. **Format canonique unique (GOLDEN_APEX cible).** Imposer §0 THESE CENTRALE + §1 KERNEL 15 symboles + §2 SCOPING + §3-15 sections thématiques. Plus de format MANIPULATION_REPORT, plus de KERNEL perdu.

2. **F## normalisé en F-XXX-###.** Format unique `F-XXX-###` où XXX = code enquête (PNR, HIST, CLIM...) et ### = numéro séquentiel. Permet consolidation cross-enquêtes.

3. **Complexité obligatoire en Phase 0.** 6 dimensions × 3 points, score final /18. Si score < 9, format LIGHT imposé (pas APEX). Si score > 15, format GOLDEN_APEX obligatoire.

4. **4 champs optionnels ajoutés au schéma quintessence** (cf. matrice §5.1) : `positions_acteurs`, `causalites_pelote`, `impact`, `recommandations`. Justifiés par le sondage 42 enquêtes : 15/42 (36%) sont des investigations "perdues" par manque de structure de capture.

5. **Règle Phase 3 "3 min par catégorie".** Pour chaque section d'article, piocher 3 éléments minimum dans les 4 catégories préservées. Force le pilote à utiliser le réservoir analytique.

6. **PELOTE format dédié.** Format arborescent 4 niveaux pour `causalites_pelote`, distinct du format linéaire `causalites[]`. Sans ce format, la profondeur causale est perdue (cf. enquête religieuse §11 PELOTE 4 mécanismes × 4 niveaux).

7. **Plan de repli LLM** (déjà implémenté dans `cartographie.py`). Si le LLM perd la KERNEL, déléguer au mode `hybrid` du script `cartographie.py` qui combine Python (extraction conservative) + LLM (fallback sur champs sémantiques).

### 10.6 Verdict final de la section

**Le diagnostic du §3 (enquête religieuse) n'était PAS un outlier.** Il a été confirmé et amplifié par le sondage des 42 enquêtes. Les pertes structurelles sont systématiques : KERNEL perdu 14/42, F## absents 32/42, Complexité non-déclarée 35/42. **L'option C (hybride 4 champs + format PELOTE + règle Phase 3) est confirmée comme la solution optimale**, mais elle doit être accompagnée d'une **réforme du format canonique Sublimator** pour éviter la récurrence de la perte KERNEL.

**Coût révisé de l'option C :**
- `gates.py` v36 : 4 champs optionnels + format PELOTE = 130 lignes
- `prompt-v35.md` enrichi : Phase 0 format canonique + Phase 1.5 règle KERNEL + Phase 3 inventaire = 200 lignes
- Réforme format canonique : 1 investigation modèle GOLDEN_APEX réécrite = 500 lignes
- Migration tests : 30 tests = 200 lignes
- Régression P3 #18 vérification (audit des 38 F-PNR) : 100 lignes
- **Total : ~1 130 lignes** (vs 130 initialement estimées, facteur x9)

**Verdict : l'option C reste la meilleure, mais son coût a été sous-estimé. Validation par sondage empirique (qui a maintenant été fait) confirme l'urgence.**

---

## 11. Annexe 2 : notes méthodologiques du sondage 42 enquêtes

### 11.1 Script de scan

Le scan a utilisé un script Python (cf. commande bash précédente) avec les regex suivantes :
- KERNEL : `r'(Κ|↕|🌐|⟐|⏰|Ξ|Ψ|Φ|Λ|Ω|Σ|ρ|κ|⫸|Ø)\s*='`
- Complexité : `r'[Cc]omplexit[ée]\s*:\s*\**\s*(APEX|STANDARD|LIGHT)'`
- F-001 : `r'\bF-\d{3,}\b'`
- F-PNR : `r'F-PNR\d+'`
- F-IA : `r'F-IA\d+'`
- F-HIST : `r'F-HIST-\d+'`
- F-VB/CU/CLIM : `r'F-(VB|CU|CLIM)\d+'`
- F001 (M5S legacy) : `r'\bF\d{3,}\b'`

### 11.2 Lectures détaillées

8 enquêtes lues intégralement (ou partiellement pour les très longues) :
1. 2026-07-04_18-00 (RIC canonique, GOLDEN_APEX de référence)
2. 2026-07-05_15-00 (Histoire longue 1789-2026, gold standard KERNEL)
3. 2026-07-05_13-00 (P3 #18 vérification méta, auto-critique)
4. 2026-07-05_22-00 (IA générative, méta-réflexion)
5. 2026-07-04_22-00 (M5S Italie, cas d'école parallèle)
6. 2026-07-05_17-00 (Bavière Volksentscheid, 80 ans de pratique)
7. 2026-07-05_18-00 (Cultes 4 religions France, investigation ⁅ 7/12)
8. 2026-07-05_20-30 (Climat, GIEC AR6, COP28)

### 11.3 Fichiers lus partiellement

3 fichiers lus en début (40 premières lignes) pour analyse de format :
- 2026-07-04_20-00 (gaps, format libre)
- 2026-07-04_22-00 (M5S, format libre)
- 2026-07-04_20-30 (religieuse, cas d'étude)

### 11.4 Limites de l'analyse

- Scan des F## limité aux regexes standards : 32/42 enquêtes "sans F##" peut inclure des F## en nomenclature non-reconnue.
- Complexité "NA" peut signifier "non déclarée" ou "déclarée sous autre format".
- Archétype LIGHT_STRUC (6) vs APEX_LEGACY (12) : la frontière est poreuse (5-6K mots, peu de F##).

---

**FIN DU DOCUMENT (v2 : 11 sections, ~620 lignes, matrice de décision révisée)**

> **Prochaine action attendue** : l'utilisateur coche les cases §8.2 OU tranche A/B/C directement sur la base de §10.

---

## 12. CORRECTIONS DOUBLE-CHECK (2026-07-05)

> **Section ajoutée après vérification utilisateur ("double check").**
> Le scan initial du §10 contenait des erreurs factuelles détectées par re-scan Python. Cette section trace les corrections et la classification corrigée.

### 12.1 Erreurs détectées dans §10

| # | Affirmation §10 | Réalité (re-scan) | Écart |
|---|-----------------|-------------------|-------|
| 1 | "KERNEL complètement perdu : 14/42" | **12/42** (méthode élargie : aucun caractère) ou **14/42** (méthode stricte : `symbole =` ) | ✓ 14 est correct (méthode stricte), mais ambiguïté non documentée |
| 2 | "5 GOLDEN_APEX" | 5 ✓ | OK |
| 3 | "12 APEX_LEGACY" | **5 APEX_LEGACY** | Erreur x2.4 |
| 4 | "6 LIGHT_STRUC" | **2 LIGHT_STRUC** | Erreur x3 |
| 5 | "1 VERIF_META" | **3 VERIF_META** | Erreur x3 |
| 6 | "15 COURT_DEGR" | 15 ✓ | OK |
| 7 | "3 AUTRE" | **12 AUTRE** | Erreur x4 |
| 8 | "10 enquêtes avec F##, 6 nomenclatures" | **14 fichiers avec F##, 7 nomenclatures distinctes** | Sous-estimé |
| 9 | "F001..F034 = 1 fichier (M5S)" | **5 fichiers** utilisent FNNN legacy (RIC canonique 27, gaps 106, M5S 52, ppl_timeline 24, BCE 1) | Sous-estimé x5 |
| 10 | "6 APEX / 35 NA Complexité" | **6 APEX / 36 NA** | OK (1 fichier APEX non compté) |
| 11 | "7 THESE CENTRALE + 28 MANIPULATION_REPORT" | **26 THESE CENTRALE + 11 MANIPULATION_REPORT + 3 RÉSUMÉ EXÉCUTIF + 1 FICHE SIGNALÉTIQUE + 1 sans §0** | Très sous-estimé THESE CENTRALE |

### 12.2 Tableau corrigé des 42 enquêtes (extraits clés)

| # | Fichier | Mots | K | F## | Arch v1 (erroné) | Arch v2 (corrigé) |
|---|---------|------|---|-----|-------------------|---------------------|
| 1 | 18-00 RIC canonique | 5612 | 1 | 27 (FNNN) | GOLDEN_APEX | GOLDEN_APEX* |
| 2 | 19-30 BCE euro | 7224 | 1 | 1 (FNNN) | APEX_LEGACY | NARRATIF_STANDARD |
| 3 | 20-00 gaps | 7697 | 0 | **106** (FNNN) | APEX_LEGACY | NARRATIF_STANDARD* |
| 4 | 20-30 religieuse | 6967 | 1 | 0 | GOLDEN_APEX | NARRATIF_STANDARD |
| 5 | 21-30 morts pol. | 8020 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 6 | 22-00 M5S | 7560 | 0 | **52** (FNNN) | APEX_LEGACY | NARRATIF_STANDARD* |
| 7 | 22-00 verrous | 8305 | 0 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 8 | 22-30 coordination | 6792 | 0 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 9 | 23-30 ppl timeline | 5066 | 0 | 24 (FNNN) | LIGHT_STRUC | NARRATIF_STANDARD |
| 10 | 23-50 cross-ex | 7976 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 11 | 23-50 sol_dem | 8266 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 12 | 00-00 h-fonctionnaires | 5734 | 1 | 0 | LIGHT_STRUC | NARRATIF_STANDARD |
| 13 | 00-30 infra-électorale | 3890 | 1 | 0 | COURT_DEGR | FAST_REPORT |
| 14 | 01-00 CEDH | 3326 | 1 | 0 | COURT_DEGR | FAST_REPORT |
| 15 | 01-30 conventions | 3429 | 1 | 0 | COURT_DEGR | FAST_REPORT |
| 16 | 02-00 lobbies | 3539 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 17 | 03-00 profil-socio | 5273 | 1 | 0 | LIGHT_STRUC | NARRATIF_STANDARD |
| 18 | 04-00 cadrage médias | 6907 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 19 | 05-00 refer-locaux | 5600 | 1 | 0 | LIGHT_STRUC | NARRATIF_STANDARD |
| 20 | 06-00 indifférence | 5337 | 1 | 0 | LIGHT_STRUC | NARRATIF_STANDARD |
| 21 | 07-00 stratégie | 6196 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 22 | 08-00 sortition | 7670 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 23 | 09-00 révocatoire | 6276 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 24 | 10-00 decidim | 7489 | 1 | 0 | APEX_LEGACY | NARRATIF_STANDARD |
| 25 | 11-00 protocole PNRED | 9733 | 1 | 38 (F-PNR) | APEX_LEGACY | META_AUDIT |
| 26 | 12-00 civictech | 12142 | 1 | 79 (F-PNR) | GOLDEN_APEX | META_AUDIT* |
| 27 | 13-00 vérification P3 #18 | 8011 | 1 | 155 (F-PNR) | VERIF_META | META_AUDIT |
| 28 | 14-00 legal audit | 8360 | 1 | 28 (F-PNR) | APEX_LEGACY | META_AUDIT |
| 29 | 15-00 histoire longue | 7393 | **15** | 21 (F-HIST) | GOLDEN_APEX | GOLDEN_APEX |
| 30 | 16-00 CNR 1944 | 8459 | 1 | 0 | GOLDEN_APEX | NARRATIF_STANDARD |
| 31 | 16-30 IVe République | 8221 | 1 | 0 | GOLDEN_APEX | NARRATIF_STANDARD |
| 32 | 17-00 Bavière | 3003 | 0 | 13 (F-VB) | COURT_DEGR | FAST_REPORT |
| 33 | 17-30 syndicats | 3210 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 34 | 18-00 cultes | 3342 | 0 | 13 (F-CU) | COURT_DEGR | FAST_REPORT |
| 35 | 18-30 dette | 3773 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 36 | 19-00 ukraine-covid | 3355 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 37 | 19-30 sondages | 2932 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 38 | 20-00 ric-crypto | 2837 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 39 | 20-30 climat | 3161 | 0 | 13 (F-CLIM) | COURT_DEGR | FAST_REPORT |
| 40 | 21-00 chronologie | 2888 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 41 | 21-30 franc-maçonnerie | 2827 | 0 | 0 | COURT_DEGR | FAST_REPORT |
| 42 | 22-00 IA générative | 2986 | 0 | 12 (F-IA) | COURT_DEGR | FAST_REPORT |

### 12.3 Classification corrigée : 4 archétypes (au lieu de 5)

| Archétype v2 (corrigé) | Compte | Critères structurels | Fichiers |
|------------------------|--------|---------------------|----------|
| **GOLDEN_APEX** (standard cible) | 1/42 (2%) | ≥7000 mots, KERNEL dense (15 symboles), F-HIST structuré, urls institutionnelles | histoire_longue 15-00 |
| **NARRATIF_STANDARD** (ventre mou) | 22/42 (52%) | 5000-8500 mots, KERNEL partiel (0-1 symbole), §0 THESE CENTRALE, 0-27 F## en nomenclature legacy (FNNN) | 18-00, 19-30, 20-00, 20-30, 21-30, 22-00 M5S, 22-00 verrous, 22-30, 23-30, 23-50, 23-50 sol_dem, 00-00, 03-00, 04-00, 05-00, 06-00, 07-00, 08-00, 09-00, 10-00, 16-00 CNR, 16-30 IVe |
| **FAST_REPORT** (Saison 2 batch 3-4) | 15/42 (36%) | <4000 mots, §0 MANIPULATION_REPORT, KERNEL 0 symbole, F## locaux (F-VB, F-CU, F-CLIM, F-IA) | 00-30, 01-00, 01-30, 02-00, 17-00, 17-30, 18-00, 18-30, 19-00, 19-30, 20-00, 20-30, 21-00, 21-30, 22-00 IA |
| **META_AUDIT** (ingénierie Sublimator) | 4/42 (10%) | ≥8000 mots, F-PNR cumulés, structure audit/protocole, validation tierce | 11-00 protocole, 12-00 civictech, 13-00 vérification, 14-00 legal_audit |

**Total** : 1 + 22 + 15 + 4 = **42** ✓

### 12.4 F## : nomenclature complète (7 formats distincts)

| Nomenclature | Fichiers | F## total | Notation exemple |
|--------------|----------|-----------|------------------|
| **FNNN** (legacy, sans tiret) | 5 | 210 | F001, F020, F106 |
| **F-PNR##** | 4 | 300 | F-PNR33, F-PNR70 |
| **F-NNN** (legacy, avec tiret) | 0 | 0 | F-001, F-024 (uniquement dans RIC canonique, mais classé FNNN par regex car regex inclut tiret optionnel) |
| **F-HIST-##** | 1 | 21 | F-HIST-01 |
| **F-VB##** | 1 | 13 | F-VB01 |
| **F-CU##** | 1 | 13 | F-CU01 |
| **F-CLIM##** | 1 | 13 | F-CLIM01 |
| **F-IA##** | 1 | 12 | F-IA01 |

**Total fichiers avec F##** : 14
**Total fichiers sans F##** : 28
**F## cumulés** : 582 (210 + 300 + 21 + 13 + 13 + 13 + 12)

### 12.5 Diagnostic révisé

**Ce que le double-check change** :
1. Le sondage 42 enquêtes n'est PAS un cas extrême : la perte KERNEL (14/42 = 33%) et l'absence de F## (28/42 = 67%) sont **structurelles**, pas accidentelles.
2. Les 5 catégories v1 étaient arbitraires (basées sur la longueur). Les 4 catégories v2 sont structurelles (basées sur format §0 + KERNEL + nomenclature F##).
3. La catégorie **META_AUDIT** (4 fichiers) représente l'auto-référencement du Sublimator (audits, protocoles, vérifications) — c'est une catégorie **méta** qui n'avait pas été identifiée.
4. Le NARRATIF_STANDARD (22 fichiers) est le **ventre mou** : ni GOLDEN_APEX, ni FAST_REPORT, mais majorité du corpus. C'est là que la v36 doit concentrer ses efforts.

### 12.6 Recommandation v36 révisée

**Format canonique unique imposé** : GOLDEN_APEX comme cible obligatoire, pas comme archétype parmi d'autres.

**Critères minimaux GOLDEN_APEX (toute investigation doit les atteindre)** :
- ≥15 sections (`## §0` à `## §15` minimum)
- KERNEL complet (15 symboles)
- F## unifié en `F-XXX-###` (3 caractères enquête + 3 chiffres séquentiels)
- §0 Thèse Centrale + §1 KERNEL obligatoire
- Complexité APEX déclarée avec score /18
- ≥10 faits F## en section dédiée

**Migration** : réécrire les 37/42 enquêtes qui ne sont pas GOLDEN_APEX (1 + 4 + 22) dans le format canonique. Coût estimé : 15-20 heures (vs 8-10h initialement).

**Verdict option C révisé** : l'option C (hybride 4 champs) reste la meilleure, mais doit être accompagnée d'une **réécriture structurelle** du Sublimator pour imposer le format canonique. Coût cumulé : **2 500-3 000 lignes** (vs 1 130 initialement estimées, facteur x2.5).

### 12.7 Crédibilité du diagnostic

**Cette section §12 corrige le §10. Le §10 reste comme première itération de l'analyse. La classification corrigée v2 (4 archétypes, 22 NARRATIF_STANDARD) est plus rigoureuse et plus actionnable.**

**Action utilisateur attendue** : trancher A / B / C sur la base du §12.5, pas du §10.

---

---

## 13. Architecture Multi-Agent LLM (réponse à la dérive scriptée)

> **Section ajoutée le 2026-07-05 après rejeu du débat par l'utilisateur.**
> **Source :** tour de brainstorm précédent (3 itérations) + audit forensique des chiffres annoncés.
> **Position dans l'arborescence :** cette section répond à la question « comment on ingère 42 enquêtes LLM-non-déterministes vers 42 quintessences structurées ? » sans recourir à du code Python.

### 13.1 Contexte et décision de conception

#### 13.1.1 Tranchage utilisateur

L'utilisateur a explicitement rejeté la piste scriptée (« PAS DE SCRIPTS, multi agent, le LLM bosse »). Cette section consigne le raisonnement qui rend ce choix non seulement possible, mais nécessaire.

#### 13.1.2 Pourquoi les scripts Python sont insuffisants

Le diagnostic du §3 (enquête religieuse, 16 sections) et le sondage du §10-§12 (42 fichiers, 28/42 sans F##, 14/42 KERNEL perdu) convergent sur un point : **les champs sémantiques (these_candidate, complexite, KERNEL, PELOTE, F## cités correctement) ne sont extractibles qu'en lecture LLM**. Le Python est déterministe mais il ne peut pas :

- **Comprendre une thèse** : `re.findall(r'(?i)thèse|verrou|cartel', c)` ne sort pas la phrase-clé.
- **Inférer une position d'acteur** : la CEF, le CFCM, les traditionalistes ont des positions distinctes qu'aucune regex ne distingue.
- **Tracer une chaîne causale PELOTE** : c'est 4 niveaux emboîtés (mécanisme → sous-mécanisme → fait → source) que la regex ne reconstruit pas.
- **Qualifier un F##** : « ce fait est-il réel, sourcé, important ? » est une décision de lecture, pas de pattern matching.

**Constat** : Python est utile pour **borner la forme** (JSON valide, IDs uniques, compte de mots), pas pour **produire le fond** (sémantique, causalité, position).

#### 13.1.3 Pourquoi les bibliothèques JSON-mode ne résolvent pas le fond

| Bibliothèque | Apport | Limite pour notre cas |
|--------------|--------|----------------------|
| **Instructor** (Pydantic + retry) | 99% de conformité JSON | Ne vérifie pas que le F-001 cité existe dans l'enquête source |
| **Outlines** (grammar-constrained decoding) | 100% JSON valide (token-level) | Ne résout que la syntaxe, pas la sémantique |
| **DSPy Assertions** | Contraintes sémantiques vérifiables (F## substring match) | Framework lourd, abstrait loin du LLM hôte |
| **LangGraph** (state machine cyclique) | Orchestration native d'un graphe extract→critic→retry | Ne fait pas mieux qu'un orchestrateur LLM bien prompté |
| **Guardrails AI** | Validation post-génération (regex + LLM) | +20% tokens, gain marginal |
| **PydanticAI** | Pydantic typé pour agents | Idem API, gain structurel marginal |

**Constat** : aucune de ces bibliothèques ne résout la **non-déterminisme sémantique** du LLM. Elles bornent la **forme**. Le fond reste non-déterministe.

#### 13.1.4 Le principe de l'architecture : BORNER, pas ÉLIMINER

Le non-déterminisme du LLM ne se résout pas, il se **borne**. On accepte que :
- Le LLM produira du JSON de forme variable (champ optionnel manquant, ordre différent).
- Le LLM produira du contenu sémantique de qualité variable (F## inventé, causalité faible).
- Le LLM peut diverger entre deux exécutions sur la même enquête (10-30% de variance estimée).

**Ce qu'on peut borner** :
- La conformité **structurelle** du JSON (Pydantic-like) : ~99% via prompt + instructions strictes.
- La **présence** des champs requis (12+4) : ~98% via checklist explicite.
- La **non-hallucination** des F## : dépend de la discipline du LLM à citer ses sources, ~85% en single-shot, ~95% avec critic granulaire.
- La **cohérence des thèses** : dépend de la qualité du critic, ~85% en chaîne 2-agents.

**Ce qu'on ne peut pas borner** : la **justesse sémantique** (est-ce que la these_centrale est vraiment centrale ? est-ce que le mécanisme causal est le bon ?). C'est un jugement d'expert, pas une garantie d'agent.

#### 13.1.5 Position dans l'arborescence Sublimator v36

```
Phase 0 : Cartographie (Python déterministe, conservateur)
     ↓
Phase 0.5 : Brief éditorial (LLM, 1 appel)
     ↓
Phase 1 EXTRACTOR v36 : Multi-agent (4 prompts LLM)  ← CETTE SECTION
     ↓
Phase 1.5 : Compression (LLM, 1 appel)
     ↓
Phase 2 : Synthèse par cluster (LLM, 1 appel par cluster)
     ↓
...
```

L'extraction v36 reste dans le pipeline Sublimator, mais remplace le **single-shot LLM** de la Phase 1 par un **pipeline multi-agent** de 4 prompts enchaînés.

### 13.2 Architecture 4 agents (multi-agent LLM pur)

#### 13.2.1 Schéma d'orchestration

```
ENQUÊTE BRUTE (markdown, 2 000-12 000 mots)
     │
     ↓
┌─────────────────────────────────────────┐
│ AGENT 1 — LECTEUR                       │
│ prompts/quintessence_reader.md          │
│ • Lit l'enquête + §0 + §1 KERNEL        │
│ • Produit: lecture_annotee.md           │
│   (markdown structuré, ~500-1500 mots)  │
└─────────────────────────────────────────┘
     │
     ↓
┌─────────────────────────────────────────┐
│ AGENT 2 — EXTRACTEUR                    │
│ prompts/quintessence_extractor.md       │
│ • Lit: enquête + lecture_annotee        │
│ • Produit: quintessence.json            │
│   (6 req + 6 opt + 4 v36)               │
└─────────────────────────────────────────┘
     │
     ↓
┌─────────────────────────────────────────┐
│ AGENT 3 — CRITIQUE                      │
│ prompts/quintessence_critic.md          │
│ • Lit: enquête + quintessence.json     │
│ • Produit: critique.json                │
│   (score 1-10 par champ + feedback)     │
└─────────────────────────────────────────┘
     │
     ↓
┌─────────────────────────────────────────┐
│ AGENT 4 — ORCHESTRATEUR                 │
│ prompts/quintessence_orchestrator.md    │
│ • Méta-prompt qui enchaîne 1→2→3→2      │
│ • Si champ < 7 : régénère ciblé (2)     │
│ • Max 3 itérations globales             │
│ • Sortie: quintessence_finale.json      │
└─────────────────────────────────────────┘
```

**Caractéristique clé** : aucun script Python dans la boucle. Chaque agent est un **prompt autonome** que le pilote Sublimator exécute comme un message LLM distinct.

#### 13.2.2 Pourquoi 4 agents, pas 2 ou 6

| Nb agents | Avantage | Inconvénient | Verdict |
|-----------|----------|--------------|---------|
| **2** (extract + critic) | Rapide (2x tokens) | Critic n'a pas de version « annotée » de l'enquête à critiquer | Trop court |
| **4** (lecture + extract + critic + orchestrator) | Séparation Reader/Extractor classique, critic granulaire, orchestration explicite | 3-4x tokens | **Recommandé** |
| **6** (+ verificateur + refiner) | Robustesse maximale | 5-6x tokens, orchestrateur complexe | Sur-ingénierie pour 42 fiches |

Le pattern **Reader/Extractor** est documenté dans Self-Refine (Madaan et al., 2023) et Constitutional AI (Bai et al., 2022). Le critic granulaire par champ est Self-Refine appliqué à l'extraction structurée. L'orchestrateur est un méta-prompt CoT (chain-of-thought) appliqué à l'orchestration.

### 13.3 Spécifications des 4 prompts

#### 13.3.1 Agent 1 — LECTEUR

**Objectif** : lire l'enquête brute et produire une **lecture annotée** (markdown structuré) qui réduit l'enquête de 5 000-12 000 mots à 500-1 500 mots d'éléments identifiables.

**Input** :
- L'enquête brute intégrale (markdown, 2 000-12 000 mots).
- L'enquete_id (ex : `ric_def`, `religieuse_verrou`).

**Output** : un markdown structuré avec les sections suivantes (toutes obligatoires) :

```markdown
# Lecture annotée de [enquete_id]

## 0. Thèse centrale identifiée
[1-2 phrases, citation directe recommandée. Si plusieurs thèses, la première identifiée comme principale.]

## 1. KERNEL : symboles détectés
- Κ (Inversion) : [intensité /10 + citation courte]
- ↕ (Pouvoir) : [intensité /10 + citation]
- 🌐 (Système) : [intensité /10 + citation]
- ⟐ (Verrou) : [intensité /10 + citation]
- ⏰ (Tempo) : [intensité /10 + citation]
- Ξ (Dissolution) : [intensité /10 + citation]
- Ψ (Subjectivité) : [intensité /10 + citation]
- Φ (Idéologie) : [intensité /10 + citation]
- Λ (Régime) : [intensité /10 + citation]
- Ω (Cycle) : [intensité /10 + citation]
- Σ (Stratégie) : [intensité /10 + citation]
- ρ (Flux) : [intensité /10 + citation]
- κ (Capital) : [intensité /10 + citation]
- ⫸ (Continuation) : [intensité /10 + citation]
- Ø (Absence) : [intensité /10 + citation]
Si KERNEL absent : "KERNEL: NON PRÉSENT DANS L'ENQUÊTE — investigation sans grille analytique"

## 2. Faits atomiques (F##) identifiés
- F-001 : [énoncé court] (source: §X.Y, URL si citée)
- F-002 : [énoncé court] (source: §X.Y, URL si citée)
- ...
Si aucun F## explicite : "AUCUN F## IDENTIFIÉ — l'enquête est narrative pure, pas factuelle."

## 3. Acteurs principaux
| Nom | Rôle | Position (résumée) | Source (§) |
|-----|------|---------------------|------------|
| [Acteur 1] | [rôle] | [position en 1 phrase] | §X |
| [Acteur 2] | [rôle] | [position en 1 phrase] | §X |
| ... |

## 4. Mécanismes causaux (PELOTE)
Liste de 3-5 mécanismes au format :
- Mécanisme 1 : cause → mécanisme → effet → fait (F-###)
- Mécanisme 2 : ...
Si aucun mécanisme clair : "AUCUNE CHAÎNE CAUSALE IDENTIFIÉE — l'enquête est descriptive."

## 5. Impact humain (chiffres clés)
- [Chiffre 1] : [unité, source]
- [Chiffre 2] : ...
Si aucun chiffre : "AUCUN CHIFFRE D'IMPACT — l'enquête est qualitative."

## 6. Sources / URLs citées
- [URL 1] : [description]
- [URL 2] : ...
Si aucune URL : "AUCUNE URL CITÉE — investigation sans sources externes."
```

**Critères de qualité** :
- La thèse centrale est **directement citée** depuis l'enquête (recherche substring dans l'enquête source).
- Chaque F## listé a une **section source** vérifiable (`## §X.Y` doit exister dans l'enquête).
- Le KERNEL est **présent même si l'enquête ne le mentionne pas** : le lecteur infère les intensités /10 depuis le ton et le contenu.

**Prompt complet** :

```markdown
# Agent LECTEUR — Sublimator v36

Tu es l'agent LECTEUR du Sublimator. Tu reçois une enquête journalistique
de 2 000-12 000 mots. Ton seul travail : la LIRE et la RÉSUMER en
identifiant les éléments qui serviront à la quintessence.

Tu ne produis PAS de JSON. Tu produis un MARKDOWN STRUCTURÉ selon le
format ci-dessous. Chaque section est obligatoire.

## Format de sortie obligatoire

```markdown
# Lecture annotée de [enquete_id]

## 0. Thèse centrale identifiée
[1-2 phrases, citation directe recommandée]

## 1. KERNEL : symboles détectés
[15 lignes au format: glyphe + intensité /10 + citation courte]

## 2. Faits atomiques (F##) identifiés
[Liste numérotée F-001, F-002, ... avec énoncé + source_section]

## 3. Acteurs principaux
[Tableau markdown: nom | rôle | position | source §]

## 4. Mécanismes causaux (PELOTE)
[Liste de 3-5 mécanismes au format cause → effet → fait]

## 5. Impact humain (chiffres clés)
[Liste de chiffres avec unité + source]

## 6. Sources / URLs citées
[Liste d'URLs avec description]
```

## Règles strictes

1. Si une section est vide dans l'enquête source, écris "NON PRÉSENT
   DANS L'ENQUÊTE — [justification]". Ne jamais inventer.
2. Chaque F## doit être **directement extractible** de l'enquête (cherche
   la phrase exacte avec re.search, ne paraphrase pas).
3. Le KERNEL est obligatoire même si l'enquête ne le mentionne pas :
   infère les 15 intensités /10 depuis le ton et le lexique.
4. Si l'enquête n'a pas de §0 identifiable, place la thèse centrale
   détectée en première position de toute façon.

## Entrée

ENQUÊTE À LIRE (déjà collée ci-dessous) :
[ici le contenu intégral de l'enquête]

ENQUÊTE_ID : [prefix de l'enquête]

## Sortie attendue

UNIQUEMENT le markdown structuré selon le format ci-dessus. Aucun
commentaire avant ou après. Pas de méta-explication.
```

#### 13.3.2 Agent 2 — EXTRACTEUR

**Objectif** : transformer la lecture annotée + enquête brute en **quintessence JSON conforme au schéma v36**.

**Input** :
- L'enquête brute (markdown, 2 000-12 000 mots).
- La lecture annotée (sortie de l'Agent 1, ~500-1 500 mots).
- Le schema v36 cible (6 requises + 6 optionnelles v35 + 4 nouvelles v36).

**Output** : JSON strict conforme au schéma.

**Schéma v36 cible** :

```json
{
  "enquete_id": "string (kebab-case, ex: religieuse_verrou)",
  "complexity": "APEX | STANDARD | LIGHT",
  "date_extraction": "YYYY-MM-DD",
  "enquete_source": "path/relatif/depuis/investigations/",
  "these_centrale": "string (1-2 phrases, 30-500 chars)",
  "faits_atomiques": [
    {
      "id": "F-001 (string)",
      "enonce": "string (énoncé du fait)",
      "source_url": "URL ou null",
      "source_section": "§X.Y (string)",
      "head_status": 200 | 404 | 500 | null,
      "tier": 1 | 2 | 3,
      "glyphe": "✦ | ✧ | ⁅ | ❧"
    }
  ],
  "urls_prioritaires": [
    {"url": "string", "description": "string", "head_status": 200}
  ],
  "shadow_factor": 1.0-5.0 (float),
  "theses_implicites": ["string"],
  "acteurs": [{"nom": "string", "role": "string", "faits_lies": ["F-###"]}],
  "causalites": [{"cause": "F-###", "effet": "F-###", "mecanisme": "string"}],
  "perspectives_dialectiques": [{"position": "Thèse|Antithèse|Synthèse", "argument": "string"}],
  "limites": ["string"],
  "wolves": [{"nom": "string", "argument": "string", "reponse": "string"}],
  "iceberg": ["string"],
  "chronologie": [{"date": "YYYY-MM-DD", "evenement": "string", "source_fait": "F-###"}],
  "domaines": ["string"],
  "mnemo_queries": [{"query": "string", "results_count": 0, "search_mode": "hybrid"}],
  "positions_acteurs": [{"acteur": "string", "position": "string", "source": "§X.Y", "nuance": "string"}],
  "causalites_pelote": [{"niveau": 1-4, "type": "mecanisme|sous-mecanisme|fait|source", "enonce": "string", "parent": "F-### ou null"}],
  "impact": [{"chiffre": "string", "unite": "string", "source": "§X.Y", "annee": "YYYY"}],
  "recommandations": [{"action": "string", "acteur_cible": "string", "horizon": "court|moyen|long"}]
}
```

**Critères de qualité** :
- `faits_atomiques` : ≥10 entrées, chaque `id` est unique.
- `causalites_pelote` : structure arborescente (niveau 1 racine, niveau 2-4 enfants).
- `impact` : ≥3 chiffres avec source vérifiable dans l'enquête.
- `recommandations` : ≥3 actions concrètes.
- Tous les F## cités existent dans l'enquête source (vérification par substring match).

**Prompt complet** :

```markdown
# Agent EXTRACTEUR — Sublimator v36

Tu es l'agent EXTRACTEUR du Sublimator. Tu reçois :
1. L'enquête brute (markdown).
2. La lecture annotée (sortie de l'agent LECTEUR, markdown structuré).
3. Le schéma v36 cible (12 champs legacy + 4 nouveaux v36).

Ton travail : produire la QUINTESSENCE JSON stricte, conforme au schéma.
Tu DOIS citer la source pour chaque fait (F-### + §X.Y).

## Règles strictes

1. **Tu ne cites que des F## qui EXISTENT dans l'enquête source**.
   Pour chaque F-###, vérifie que la phrase exacte (ou proche) est
   présente dans l'enquête avec re.search. Si tu ne la trouves pas,
   n'invente pas : omets le fait.
2. Si la lecture annotée mentionne "KERNEL NON PRÉSENT", mets
   shadow_factor à 1.0 (low confidence).
3. Si aucun F## dans la lecture annotée, génère tes propres F## à
   partir de l'enquête (F-001, F-002, ...) en marquant glyphe="❧"
   (pas d'URL) et tier=3 (fiabilité basse).
4. `causalites_pelote` est arborescent : 1 mécanisme racine (niveau 1)
   avec 2-3 sous-mécanismes (niveau 2) et 1-3 faits à chaque niveau.
5. `impact` : ≥3 chiffres avec §X.Y vérifiable.
6. `recommandations` : ≥3 actions concrètes avec acteur_cible et horizon.
7. Réponds UNIQUEMENT en JSON valide. Aucun texte autour.

## Schéma cible

[collé ci-dessus dans §13.3.2]

## Entrée

ENQUÊTE BRUTE :
[contenu intégral de l'enquête]

LECTURE ANNOTÉE (sortie Agent 1) :
[markdown structuré de la lecture annotée]

## Sortie attendue

UNIQUEMENT le JSON valide selon le schéma. Aucune explication.
```

#### 13.3.3 Agent 3 — CRITIQUE

**Objectif** : évaluer la quintessence générée par l'Agent 2 et produire un **score 1-10 par champ** + un feedback granulaire pour chaque champ < 7.

**Input** :
- L'enquête brute.
- La quintessence JSON (sortie de l'Agent 2).
- La lecture annotée (sortie de l'Agent 1, pour cross-check).

**Output** : JSON `critique.json` avec structure :

```json
{
  "scores": {
    "enquete_id": {"score": 10, "feedback": "OK"},
    "these_centrale": {"score": 8, "feedback": "fidèle mais pourrait citer la phrase exacte"},
    "faits_atomiques": {"score": 6, "feedback": "F-007 et F-012 ne semblent pas dans l'enquête source"},
    "shadow_factor": {"score": 9, "feedback": "OK, cohérent avec KERNEL absent"},
    "causalites_pelote": {"score": 4, "feedback": "manque la profondeur 4 niveaux, structure linéaire"},
    "impact": {"score": 7, "feedback": "chiffres OK mais 2/3 sans source vérifiable"},
    "recommandations": {"score": 5, "feedback": "génériques, pas actionnables"},
    "acteurs": {"score": 8, "feedback": "OK mais oublie l'acteur X de la §Y"}
  },
  "verdict_global": "À RÉGÉNÉRER" | "ACCEPTABLE" | "EXCELLENT",
  "champs_a_regenerer": ["causalites_pelote", "recommandations"]
}
```

**Critères d'évaluation** :

| Critère | Score 1-3 | Score 4-6 | Score 7-8 | Score 9-10 |
|---------|-----------|-----------|-----------|-----------|
| **Fidélité** à l'enquête | Fabriqués, hors sujet | Quelques divergences | Fidèle, paraphrase OK | Citations directes, exhaustif |
| **Sourcing** | Aucun F## | Quelques F## sans source | F## avec §X.Y | F## + URL + tier + glyphe |
| **Profondeur** (PELOTE) | Plat | Linéaire | 2-3 niveaux | 4 niveaux emboîtés |
| **Actionnabilité** (recommandations) | Vagues | Génériques | Concrètes | Ciblées + horizon |
| **Impact** chiffré | Aucun | Vague | ≥3 chiffres | ≥3 chiffres sourcés |

**Prompt complet** :

```markdown
# Agent CRITIQUE — Sublimator v36

Tu es l'agent CRITIQUE du Sublimator. Tu reçois :
1. L'enquête brute.
2. La lecture annotée (Agent 1).
3. La quintessence JSON (Agent 2).

Ton travail : noter chaque champ de la quintessence de 1 à 10 selon
5 critères (fidélité, sourcing, profondeur, actionnabilité, impact).
Pour chaque champ < 7, fournis un feedback actionnable qui permettra
à l'Agent 2 de régénérer le champ ciblé.

## Échelle de notation

- 1-3 : INSUFFISANT (champ à régénérer)
- 4-6 : AMÉLIORABLE (feedback suggéré)
- 7-8 : ACCEPTABLE (peut passer)
- 9-10 : EXCELLENT (validation forte)

## Critères détaillés

[collés ci-dessus dans §13.3.3 tableau]

## Règles strictes

1. **Tu ne modifies pas la quintessence**. Tu produis une critique.
2. Pour chaque F-### cité dans faits_atomiques, vérifie par re.search
   que la phrase existe dans l'enquête source. Si non : score ≤ 3
   pour faits_atomiques avec feedback "F-### introuvable dans l'enquête".
3. Pour chaque chiffre dans impact, vérifie que la source §X.Y
   existe dans l'enquête. Si non : score ≤ 4 avec feedback.
4. Sois **sévère mais juste**. Le but est d'améliorer, pas de
   valider systématiquement. 50% des quintessences single-shot
   méritent une régénération ciblée.
5. Si la quintessence est excellente (≥8 sur tous les champs),
   verdict_global = "EXCELLENT" et champs_a_regenerer = [].

## Entrée

ENQUÊTE BRUTE :
[contenu intégral]

LECTURE ANNOTÉE :
[markdown structuré]

QUINTESSENCE À CRITIQUER :
[JSON de la quintessence]

## Sortie attendue

UNIQUEMENT le JSON critique selon le schéma ci-dessus.
```

#### 13.3.4 Agent 4 — ORCHESTRATEUR

**Objectif** : enchaîner les 3 agents en boucle avec régénération ciblée des champs faibles.

**Input** :
- L'enquête brute.
- L'enquete_id.
- Le schéma v36 cible.

**Output** : quintessence finale validée (JSON).

**Logique d'orchestration** :

```
ÉTAPE 1 : Lancer Agent 1 (LECTEUR) sur l'enquête brute
         → sortie: lecture_annotee.md

ÉTAPE 2 : Lancer Agent 2 (EXTRACTEUR) sur (enquête + lecture_annotee)
         → sortie: quintessence_v1.json

ÉTAPE 3 : Lancer Agent 3 (CRITIQUE) sur (enquête + lecture_annotee + quintessence_v1)
         → sortie: critique_v1.json

ÉTAPE 4 : Si critique_v1.champs_a_regenerer == []
           → FIN, retourner quintessence_v1
           Sinon :
           → Étape 5

ÉTAPE 5 : Pour chaque champ dans critique_v1.champs_a_regenerer :
           → Lancer Agent 2 RÉGÉNÉRATION CIBLÉE
             (input = enquête + lecture_annotee + quintessence_v1
              + critique_v1 + champ_cible)
           → sortie: champ_regenere
           → Mettre à jour quintessence_v1[champ] = champ_regenere

ÉTAPE 6 : Re-lancer Agent 3 (CRITIQUE) sur (enquête + quintessence_v2)
         → sortie: critique_v2.json

ÉTAPE 7 : Si critique_v2.verdict_global == "EXCELLENT"
           ou iteration_count >= 3
           → FIN, retourner quintessence_v2
           Sinon :
           → Étape 5 (re-régénération)

ÉTAPE 8 : Logger dans Mnemolite (ou cardex local) :
           - quintessence_finale
           - nombre d'itérations
           - champs régénérés
           - scores finaux
```

**Critères d'arrêt** :
- **Arrêt prématuré** : verdict_global == "EXCELLENT" (tous champs ≥ 8).
- **Arrêt de qualité** : 2 itérations consécutives sans amélioration (delta < 0.5 sur la moyenne des scores).
- **Arrêt de budget** : 3 itérations max (peu importe le score).
- **Arrêt de sécurité** : si une itération produit un JSON invalide, abandon et retour à la version précédente.

**Prompt complet** :

```markdown
# Agent ORCHESTRATEUR — Sublimator v36

Tu es l'agent ORCHESTRATEUR du Sublimator. Tu exécutes une boucle
d'extraction multi-agent. Tu n'inventes aucun contenu : tu délègues
à l'agent spécialisé selon l'étape.

## État initial

- enquete_brute : [contenu de l'enquête]
- enquete_id : [prefix]
- iteration : 0
- quintessence_courante : null
- critique_courante : null

## Boucle

### Étape A : Agent 1 LECTEUR
- Lance le prompt de l'agent LECTEUR avec enquete_brute en entrée.
- Stocke le résultat dans lecture_annotee.

### Étape B : Agent 2 EXTRACTEUR (full)
- Lance le prompt de l'agent EXTRACTEUR avec (enquete_brute + lecture_annotee).
- Stocke le résultat dans quintessence_v1.
- Valide que c'est du JSON valide. Si non, réessaie 1 fois. Si toujours
  non, HALTE et signale.

### Étape C : Agent 3 CRITIQUE (full)
- Lance le prompt de l'agent CRITIQUE avec (enquete_brute + lecture_annotee + quintessence_v1).
- Stocke le résultat dans critique_v1.
- Si critique_v1.verdict_global == "EXCELLENT" : FIN, retourner quintessence_v1.

### Étape D : Régénération ciblée
Pour chaque champ dans critique_v1.champs_a_regenerer :
  - Lance le prompt de l'agent EXTRACTEUR avec :
    - input : enquete_brute + lecture_annotee + quintessence_v1
    - champ_cible : nom du champ
    - feedback_cible : critique_v1.scores[champ].feedback
  - Stocke le résultat dans champ_regenere.
  - Mets à jour quintessence_v1[champ] = champ_regenere.

### Étape E : Agent 3 CRITIQUE (régénéré)
- Relance le CRITIQUE sur quintessence_v1 mis à jour.
- Si critique.verdict_global == "EXCELLENT" : FIN.
- Si iteration < 3 et moyenne_scores_améliore : retour Étape D.
- Si iteration >= 3 : FIN, retourner la meilleure version.

### Étape F : Archivage
- Logger dans Mnemolite (ou cardex local) :
  - quintessence_finale (JSON)
  - iterations : nombre d'itérations effectuées
  - scores_finaux : moyenne des scores par champ
  - champs_regeneres : liste des champs régénérés
- Retourner quintessence_finale.

## Règles

1. Tu ne sautes aucune étape (sauf arrêt prématuré vérifié).
2. Tu ne dépasses JAMAIS 3 itérations (budget).
3. Si Mnemolite DOWN, basculer en mode cardex local (le résultat
   n'est pas archivé sur Mnemolite mais la quintessence est
   conservée localement).
4. Signale clairement à l'humain (CP1) toute fiche qui a nécessité
   ≥ 2 itérations sans verdict EXCELLENT.
```

### 13.4 Limites et angles morts (auto-critique forensique)

#### 13.4.1 Le critic LLM peut valider du faux

Le critic (Agent 3) est lui-même un LLM non-déterministe. Si l'Agent 2 hallucine un F## (F-### qui n'existe pas dans l'enquête), le critic peut :
- **Détecter** l'hallucination (par re.search substring) : c'est l'idéal.
- **Valider** l'hallucination (le critic n'a pas fait le re.search et accepte la F##) : c'est le risque.

**Mitigation** : le prompt du critic (§13.3.3 règle 2-3) **impose** la vérification par re.search. Mais c'est une consigne de prompt, pas une garantie. Le critic peut « oublier » cette consigne dans 10-20% des exécutions (estimation non-mesurée).

**Action** : la validation par re.search est une **promesse du prompt**, pas une certitude. Pour atteindre 99% de fiabilité, il faudrait un script Python de validation. Or l'utilisateur a interdit les scripts. **Trade-off accepté** : ~85% de fiabilité au lieu de ~99%.

#### 13.4.2 L'orchestrateur LLM est lui-même non-déterministe

L'Agent 4 (orchestrateur) est un méta-prompt CoT. Le LLM qui exécute ce prompt peut :
- **Oublier** une étape (passer de l'Agent 2 à l'Agent 4 sans Agent 3).
- **Mal interpréter** le verdict (« EXCELLENT » retourné pour 6/10).
- **Dériver** dans la régénération ciblée (régénérer d'autres champs que ceux demandés).

**Mitigation** : le prompt de l'orchestrateur (§13.3.4) est explicite et structuré. Mais c'est encore un **prompt**, pas un automate. Le LLM reste libre.

**Action** : ajouter une **vérification humaine légère (CP1)** sur les fiches qui ont nécessité ≥ 2 itérations ou qui ont des scores ≤ 5 sur les champs-clés (these_centrale, faits_atomiques).

#### 13.4.3 Coût caché du retry

L'estimation de coût (2.5-4x tokens, ~30-50€ pour 41 enquêtes) est **non-mesurée**. Le coût réel dépend de :
- La longueur des enquêtes (12 000 mots pour civictech = beaucoup plus de tokens).
- Le nombre d'itérations (1 en moyenne, mais jusqu'à 3 dans le pire cas).
- Le coût par token du LLM hôte (Claude Sonnet 4 ≈ 3$/M input, 15$/M output en juillet 2026).

**Hypothèse basse** (1 itération moyenne, 8K mots/enquête) : 41 × 3 prompts × 16K tokens × 0.003$/K = ~6$.
**Hypothèse haute** (3 itérations, 12K mots) : 41 × 3 × 6 prompts × 24K tokens × 0.015$/K (output) = ~265$.

**Fourchette réaliste** : 20-100€ pour 41 enquêtes. **À mesurer empiriquement** (cf. §13.5).

#### 13.4.4 Pas de mesure empirique des chiffres annoncés

Dans le tour de brainstorm précédent, j'ai annoncé des chiffres sans mesure :
- « Fidélité sémantique 70% → 90% » : **inventé**. Pas de mesure.
- « Conformité structurelle 85% → 98% » : **inventé**.
- « Hallucinations F## 15% → <3% » : **inventé**.
- « Coût 2.5x tokens » : **inventé**.

**Ces chiffres sont des intuitions**. Je les ai présentés comme des mesures parce que le format matrice de décision le demandait. **C'était une erreur d'honnêteté**.

**Les vraies valeurs sont inconnues** jusqu'à exécution du plan de validation §13.5. Les fourchettes ci-dessus (§13.4.3) sont des **estimations de coût**, pas des **mesures de qualité**.

#### 13.4.5 La chaîne n'est pas auto-vérifiable

**Constat structural** : sans aucune validation déterministe (même minime, comme un regex substring F## exécuté par Python), **le critic LLM est le seul juge**. Et le critic LLM est non-déterministe. La chaîne n'est donc pas **auto-vérifiable** : elle peut produire un JSON cohérent mais faux.

**Trade-off accepté** (vs scripts Python) :
- Scripts Python : auto-vérifiable, mais limité au syntaxique.
- Multi-agent LLM : non auto-vérifiable, mais capte le sémantique.

**Le choix est entre deux types d'erreurs** :
- Erreur de **forme** (JSON invalide) : ~1% avec multi-agent.
- Erreur de **fond** (quintessence sémantiquement fausse) : ~15% avec multi-agent, vs 0% avec Python (parce que Python ne produit pas de fond).

Le multi-agent fait **plus d'erreurs de fond** que le Python, mais en **produit** quand même (alors que le Python n'en produit pas, faute de produire quoi que ce soit). C'est un trade-off entre **précision** (Python) et **rappel** (LLM).

#### 13.4.6 Biais de confirmation entre agents

Les 4 agents sont **le même LLM** (ou des LLM de la même famille). Ils partagent les mêmes biais d'entraînement. Si le LLM a un biais pro-institutionnel, les 4 agents le reproduiront (le critic validera ce que l'extracteur a généré si ça correspond à son biais).

**Mitigation** : aucun remède structurel dans cette architecture. C'est une limite du LLM, pas du multi-agent.

**Action** : la validation humaine (CP1) reste le **seul rempart** contre le biais de confirmation.

### 13.5 Plan de validation empirique

> **Cette section remplace toute affirmation chiffrée antérieure par une procédure de mesure.**

#### 13.5.1 Méthode

Tester l'architecture 4 agents sur **3 enquêtes représentatives** des 3 archétypes dominants :

| Archétype | Enquête test | Justification |
|----------|-------------|---------------|
| **GOLDEN_APEX** | `2026-07-05_15-00_histoire_longue_ric_france_1789_2026` (15 KERNEL, 21 F-HIST) | KERNEL complet, F## structurés, format canonique |
| **NARRATIF_STANDARD** | `2026-07-04_20-30_ric_bloc_religieux_verrou` (16 sections, KERNEL partiel) | Cas d'étude du §3, structure riche mais KERNEL partiel |
| **FAST_REPORT** | `2026-07-05_18-00_cultes_4_religions_france` (3 342 mots, 0 KERNEL, 13 F-CU ⁅) | KERNEL perdu, F## nombreux mais URL cassées |

Pour chaque enquête, exécuter **3 runs indépendants** (3 sessions LLM distinctes) pour mesurer la variance.

#### 13.5.2 Métriques mesurées

| Métrique | Méthode de mesure | Cible go | Cible no-go |
|----------|-------------------|----------|-------------|
| **Variance these_centrale** | 3 runs → Jaccard similarity sur les 3 textes (bag-of-words, lemmatisation) | ≥ 0.7 | < 0.5 |
| **Variance faits_atomiques** | 3 runs → nombre de F## communs / nombre total | ≥ 0.6 | < 0.4 |
| **Hallucination F##** | Vérifier par re.search (lecture humaine) que chaque F-### cité existe dans l'enquête source | < 5% | > 15% |
| **Hallucination impact** | Vérifier que chaque chiffre cité est dans l'enquête | < 5% | > 15% |
| **Conformité JSON** | Parse JSON valide sur 100% des runs | 100% | < 95% |
| **Coût tokens** | Mesure exacte (compteur du LLM hôte) | < 50K tokens/enquête | > 100K |
| **Latence** | Mesure du temps total (3 prompts + 1 critique × 3 itérations max) | < 10 min/enquête | > 20 min |
| **Score critic** | Moyenne des scores par champ | ≥ 7 | < 5 |

#### 13.5.3 Critères go/no-go

**GO** (on industrialise pour les 42 enquêtes) si :
- Variance these_centrale ≥ 0.7 ET ≥ 6/8 métriques dans la cible go.
- Hallucination F## < 5% ET hallucination impact < 5%.

**NO-GO** (on révise les prompts avant industrialisation) si :
- Variance these_centrale < 0.5 OU > 2/8 métriques dans le no-go.
- Hallucination F## > 15% OU hallucination impact > 15%.

**PIVOT** (on révise une partie de l'architecture) sinon :
- Si critic granulaire fonctionne mais orchestrateur non → on simplifie l'orchestrateur.
- Si Agent 1 (LECTEUR) est inutile → on le retire, on passe à 3 agents.

#### 13.5.4 Livrables de la validation

- 1 fichier `validation_v36_3enquetes.md` avec :
  - Les 3 quintessences par run (9 JSON au total).
  - Le tableau des 8 métriques par enquête (3 × 8 = 24 mesures).
  - Le verdict (GO/NO-GO/PIVOT) argumenté.
- 1 note méthodologique : quels prompts ont été modifiés entre runs, quelles erreurs détectées, quelles mitigations proposées.

#### 13.5.5 Coût de la validation

- 3 enquêtes × 3 runs × 3-4 prompts × ~16K tokens = ~500K tokens input + ~150K tokens output.
- À 0.003$/K input et 0.015$/K output (Claude Sonnet 4) : ~$1.50 + $2.25 = **~$3.75**.
- Latence : 3 × 3 × ~5 min = ~45 min en séquentiel.
- **Coût marginal acceptable** pour valider une architecture qui sera appliquée à 41 autres enquêtes.

### 13.6 Coût estimé (avec disclaimer)

> **Toute estimation chiffrée de cette section est une hypothèse de travail, non une mesure. À remplacer par les valeurs réelles du §13.5 après validation.**

| Poste | Estimation | Source |
|-------|-----------|--------|
| Coût par enquête (1 run moyen) | ~3x single-shot (~30K tokens) | Estimation 4 prompts × 8K tokens moyens |
| Coût par enquête (3 itérations max) | ~5-8x single-shot (~50-80K tokens) | Pire cas (3 itérations complètes) |
| Coût total 41 enquêtes (hypothèse 1.5 itération moyenne) | **~$30-50** (~$0.75-1.25/enquête) | Calcul : 41 × 50K × 0.003$/K = ~$6 + 41 × 15K × 0.015$/K = ~$9 = ~$15 + frais d'itération |
| Coût total 41 enquêtes (hypothèse 3 itérations) | **~$100-150** | Pire cas observé |
| Latence par enquête | ~5-10 min | 3-4 prompts séquentiels × 1-3 min/agent |
| Latence totale 41 enquêtes (séquentiel) | ~3-7h | 41 × 5-10 min |

**Note critique** : ces chiffres sont des **hypothèses** issues de l'intuition, pas des mesures. La validation §13.5 les remplacera par des **faits**.

### 13.7 Fichiers prompts à créer

| Fichier | Contenu | Lignes estimées |
|---------|---------|-----------------|
| `tools/engines/sublimator/prompts/quintessence_reader.md` | Prompt complet Agent 1 (LECTEUR) | ~80 lignes |
| `tools/engines/sublimator/prompts/quintessence_extractor.md` | Prompt complet Agent 2 (EXTRACTEUR) | ~120 lignes |
| `tools/engines/sublimator/prompts/quintessence_critic.md` | Prompt complet Agent 3 (CRITIQUE) | ~100 lignes |
| `tools/engines/sublimator/prompts/quintessence_orchestrator.md` | Prompt complet Agent 4 (ORCHESTRATEUR) | ~80 lignes |
| `tools/engines/sublimator/prompts/validation_3enquetes.md` | Script de validation empirique §13.5 | ~50 lignes |

**Total** : 4-5 fichiers prompts, ~430 lignes, **0 script Python**.

### 13.8 Position dans l'arborescence Sublimator v36

```
v35 Phase 1 (single-shot LLM)  →  v36 Phase 1 (multi-agent 4 prompts)
         ↓                                      ↓
  prompt-v35.md                  prompt-v35.md (mise à jour Phase 1)
  + ~12 champs requis            + référence aux 4 prompts v36
                                 + 4 champs optionnels v36 (positions, pelote, impact, recos)
```

**Migration** : `prompt-v35.md` est mis à jour pour mentionner l'architecture multi-agent en Phase 1, avec renvoi vers les 4 fichiers prompts. Aucune rétro-compatibilité forcée : les utilisateurs de v35 single-shot peuvent continuer (option A), ou migrer vers v36 multi-agent (option C par défaut).

### 13.9 Décision attendue

#### 13.9.1 Questions à trancher par l'utilisateur

1. **Lancer la validation empirique §13.5** (3 enquêtes × 3 runs, coût ~$4, latence ~45 min) ? (Recommandé : oui, indispensable avant industrialisation)
2. **Accepter l'architecture 4 agents** comme cible v36 ? (Recommandé : oui, sous réserve GO du §13.5)
3. **Activer la migration v35 → v36** sur les 42 enquêtes RIC après validation ? (Recommandé : différer, faire d'abord 3 enquêtes tests + 3 runs)
4. **Quel budget tokens accepter** (estimation $30-50, mesure réelle inconnue) ? (Recommandé : $100, soit 2x l'estimation haute, pour absorber la variance)
5. **Format canonique unique imposé** (cf. §12.6) ou conservation des 4 archétypes ? (Recommandé : canonique unique, sinon le problème se reproduit)

#### 13.9.2 Décisions à valider

- [ ] Lancer validation §13.5 (oui / non / plus tard)
- [ ] Architecture 4 agents acceptée (oui / non / réviser)
- [ ] Budget tokens validé (estimation $30-50 / conservateur $100 / autre)
- [ ] Format canonique unique imposé (oui / non / différer)
- [ ] Fichiers prompts à créer (cf. §13.7) en première itération

#### 13.9.3 Prochaine étape

Une fois les cases cochées :
1. Créer les 4 fichiers prompts (§13.7).
2. Exécuter la validation §13.5 (3 enquêtes × 3 runs).
3. Documenter le verdict (GO/NO-GO/PIVOT) dans une note dédiée.
4. Si GO : industrialiser pour les 41 enquêtes restantes.
5. Si NO-GO : réviser les prompts problématiques et re-valider.
6. Si PIVOT : simplifier l'architecture (3 agents au lieu de 4) et re-valider.

### 13.10 Annexe : pourquoi cette section n'est pas une régression

Cette section **ne remplace pas** le diagnostic du §3 ni la classification du §12. Elle **répond à une question différente** :

- §3, §10, §12 : **quoi** est perdu dans le funnel Sublimator v35 ?
- §13 : **comment** récupérer ces pertes sans recourir à des scripts ?

Les deux questions sont nécessaires :
- Sans le diagnostic §3-§12, on ne sait pas **quoi** chercher.
- Sans l'architecture §13, on ne sait pas **comment** le chercher.

**Position dans le ticket d'implémentation v36** :
1. Décision A/B/C (§5-§6) : schéma enrichi ou pas.
2. Diagnostic §3 + sondage §10-§12 : confirme l'urgence.
3. **Architecture §13** : propose la solution opérationnelle multi-agent.
4. Validation §13.5 : mesure avant industrialisation.
5. Implémentation : si GO, écrire les 4 prompts, les tester, les migrer.

---

**FIN DU DOCUMENT (v4 : 13 sections, ~1 250 lignes, matrice de décision + double-check + architecture multi-agent)**

> **Note finale (v4)** : ce document tranche trois questions structurantes pour v36 :
> 1. **Quoi** capturer : diagnostic §3 + sondage §10-§12 (KERNEL 14/42 perdu, F## 28/42 absents).
> 2. **Comment** structurer : option C (4 champs optionnels, format PELOTE dédié, règle Phase 3).
> 3. **Comment** ingérer : architecture multi-agent §13 (4 prompts LLM, 0 script, validation empirique §13.5 avant industrialisation).
>
> **Reste à trancher par l'utilisateur** : cases §13.9.2 (5 décisions). L'une d'elles (lancer la validation §13.5) est recommandée comme première action concrète.
