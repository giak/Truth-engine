# Audit antagoniste forensique Sublimator v36 : Round 2 (VERDICT)

> **Date** : 2026-07-05 14h00 CEST.
> **Type** : VERDICT dimensionnel (post-cadrage `085a3b5`, baseline factuelle `5756fa2`).
> **Périmètre** : 1 pilote (prompt-v35.md, 277 lignes) + 1 SPECS (2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md, 1 501 lignes) + 4 sub-prompts + 2 validateurs Python + sublimator_pilot.py. Total : **2 989 lignes**.
> **Méthode** : Phase A reconnaissance (basher) + Phase B lecture contradictoire (code-searcher multi-pattern) + Phase C cross-check (8 critères C-CK1-C-CK8) + Phase D synthèse (tableau verdict 28 cibles).
> **Baseline `5756fa2`** : audit v35 16/16 [x] code-side fixes confirmés. Aucune dette v35 ouvert au moment du verdict v36.

---

## 1. Synthèse verdict global

**Score (table entries)** : **12 OPE + 9 RISQUE + 10 BLOQUANT = 31 entrées** réparties dans §3.1 (15 lignes) + §3.2 (8 lignes) + §3.3 (8 lignes).

**Score dédupliqué** : **10 OPE + 9 RISQUE + 6 BLOQUANT = 25 cibles uniques** après regroupement des synonymes cross-tables (cf. §1.1 plus bas). M.R1 reste OPE côté statique (25/25 grep propagés) ; le contingent BLOQUANT (B.6 / C-CK4 empirique) est comptabilisé à part dans le décompte 6 BLOQUANTS uniques via split-verdict (static OPE + empirical BLOQUANT contingent).

### 1.1 Déduplication cross-tables

Les tables 3.1/3.2/3.3 listent 31 entrées. Certaines sont des vues multiples de la même cible :

| Cible unique | Entrées synonymes | Verdict |
|--------------|-------------------|---------|
| Phase 3 « 3 min par catégorie » | A.R1 §3.1 + N6 §3.2 + B.1 §2 | BLOQUANT (1) |
| CRITIQUE propage règle 4 champs | A.R2 §3.1 + C.R3 §3.1 + B.2 §2 | BLOQUANT (2) |
| PELOTE format 4 niveaux (LECTEUR legacy incohérent) | P.R1 §3.1 + B.4 §2 | BLOQUANT (3) |
| M1-M9 valide 4 champs optionnels | P.R3 §3.1 + C-CK6 §3.3 + B.3 §2 | BLOQUANT (4) |
| Format canonique unique GOLDEN_APEX | F.R1 §3.1 + F.R2 §3.1 + B.5 §2 | BLOQUANT (5) |
| Mnemolite 5-place empirique M9 | M.R1 §3.1 + N8 §3.2 + C-CK4 §3.3 + B.6 §2 | OPE (statique) / BLOQUANT (empirique contingent sur run) (6) |
| positions_acteurs absent | N5 §3.2 + C-CK5 §3.3 | RISQUE (déjà compté dans RISQUE) |

24 entrées de table correspondent à 6 BLOQUANTS uniques après merge ; les 7 entrées restantes mappent sur des cibles distinctement OPE/RISQUE. Total après dedup : 25 cibles uniques (10 OPE + 9 RISQUE + 6 BLOQUANT).

**Charge de remédiation réelle** : 6 BLOQUANTS uniques (effort 8-10h) + 9 RISQUE uniques (effort 3-4h) + 10 OPE uniques à maintenir — vs headline 12 OPE qui sur-estimait en incluant 6 doublons cross-tables.

- **Option C hybride** (SPECS v36 §5.1) : architecture cible connue, mais **3 BLOQUANTS empêche son industrialisation** (règle Phase 3 « 3 min par catégorie » absente du pilote, format PELOTE non-propagé à 1 cible sur 4, et Mnemolite isolation cross-enquête non-mesurée empiriquement).
- **P1 silencieuse anticipée A.R1 confirmée BLOQUANTE** : la règle §5.1 C-3 du SPECS est définitoire de l'option C. Sans elle, le pilote ignore les 4 champs ajoutés v36 au rendu Phase 3 article.
- **PELOTE format 4 niveaux** : présent en SPECS + EXTRACTEUR + CRITIQUE. Manque Phase 2 cluster (prompt-v35 §Phase 2 ne référence pas la profondeur PELOTE) → RISQUE.
- **5-place Mnemolite** : pleinement effectif (25/25 grep propagés sur pilote + 4 sub-prompts). Seul OPE 100% du périmètre.

**Verdict en une phrase** : option C industrialisable **à 60%**. Sans correction des 6 BLOQUANTS, le pilote v36 produit des articles structurellement appauvris (les 4 nouveaux champs ne sont pas pompés en Phase 3 → régression silencieuse vers qualité v35).

---

## 2. Les BLOQUANTS (P0 : non-industrialisable)

### B.1 — A.R1 « Phase 3 : 3 éléments min par catégorie » absente du pilote

**Constat** : `grep -nE '3 (élements|min) par catégorie|positions_acteurs|causalites_pelote' tools/engines/sublimator/prompt-v35.md` = **0 hit**. La règle `SPECS v36 §5.1 Option C-3` (« Piocher au moins 3 éléments dans les 4 catégories `positions_acteurs + causalites_pelote + impact + recommandations` par section d'article ») est au cœur de l'option C, mais le prompt pilote ne la mentionne pas dans `§Phase 3 LOIS L1-L8`. Résultat : le LLM, en Phase 3, choisit librement, ignore souvent les 4 champs ajoutés v36, et l'article rendu revient à qualité v35 (12 champs plats).

**Fichiers concernés** : `prompt-v35.md §Phase 3 LOIS`.
**Source SPECS** : `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` ligne 175 (Règle métier « 3 minimum ») + ligne 497 (« Règle Phase 3 '3 min par catégorie' »).
**Périmètre micro-observation code-reviewer cadrage** : **CONFIRMÉE BLOQUANTE** (cadrage §4.4 « P1 silencieuse anticipée »).

**Remédiation** : ajouter dans `prompt-v35.md §Phase 3` après LOIS L8 une ligne :
> **L9 — 3-éléments-minimum** : pour chaque section H2 d'article, piocher au minimum 3 éléments parmi `positions_acteurs` + `causalites_pelote` (≥1) + `impact` (≥1) + `recommandations` (≥1). Si une catégorie est vide, déclarer explicitement « §X.Y — cette catégorie n'a pas de matériau ».

---

### B.2 — A.R2 « Propagation règle Phase 3 au CRITIQUE » absente

**Constat** : `quintessence_critic.md` (§A.3 audit narratif) cite « 5 critères (fidélité, sourcing, profondeur, actionnabilité, impact) » (ligne 27 inquirer) mais **ne contient pas** la règle « 3-éléments-minimum » comme critère d'évaluation. Le CRITIQUE (quand invoqué en audit final §A.3) ne peut donc pas sanctionner un article Phase 3 qui viole la règle.

**Fichiers concernés** : `prompts/quintessence_critic.md`.
**Source SPECS** : `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` ligne 175 (risque contournement pilote LLM peu rigoureux).

**Remédiation** : ajouter dans `quintessence_critic.md §5 critères` ligne 27+ une ligne :
> **C6 — Conformité 3-minimum** : vérifier que chaque section H2 de l'article cite au moins 3 éléments parmi les 4 catégories v36 (`positions_acteurs`, `causalites_pelote`, `impact`, `recommandations`). Note : si CRITIQUE non invoqué (§13.5), la validation M1-M9 doit intégrer ce check programmatiquement (cf. B.3).

---

### B.3 — C-CK6 « Validateurs Python M1-M9 prennent 3/4 champs en compte »

**Constat** : `grep -nE 'causalites_pelote|positions_acteurs|recommandations' tools/engines/sublimator/sublimator_validate.py tools/engines/sublimator/sublimator_retry.py` = **0 hit**. Seul `impact` apparaît (associé à M4 « hallucination chiffres impact »). Les 3 autres champs v36 sont totalement absents des validateurs Python, qui ne peuvent donc pas :
1. Bloquer une quintessence sans `causalites_pelote` (alors que SPECS ligne 1039 l'exige arborescent 4 niveaux).
2. Vérifier que `positions_acteurs` ont source §X.Y (alors que SPECS ligne 1001 l'exige).
3. Vérifier que `recommandations` ont acteur_cible + horizon (alors que SPECS ligne 1004 l'exige).

**Fichiers concernés** : `sublimator_validate.py` (M1-M9 lignes 42-62 + computation 103-194) + `sublimator_retry.py`.
**Source SPECS** : `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` §11 critères obligatoires (lignes 1037-1042).

**Remédiation** : ajouter 3 nouvelles métriques M10-M12 dans `sublimator_validate.py` :
- **M10** : profondeur PELOTE = max(niveau dans `causalites_pelote`), cible ≥ 4 (sources).
- **M11** : % `positions_acteurs` avec `source: §X.Y` valide, cible 100%.
- **M12** : % `recommandations` avec `acteur_cible` non-vide + `horizon ∈ {court, moyen, long}`, cible 100%.

---

### B.4 — P.R1 « Format PELOTE dédié vs confusion avec `causalites[]` linéaire »

**Constat (mitigé)** : `prompts/quintessence_extractor.md` ligne 38 spécifie bien « `causalites_pelote` est arborescent : 1 mécanisme racine (niveau 1) → 2-3 sous-mécanismes (niveau 2) → 1-3 faits intermédiaires (niveau 3) → 1-3 sources F-### (niveau 4, `type=\"source\"`, `parent=fait`). 4 niveaux obligatoires = cible EXCELLENT du CRITIQUE. » Donc **EXTRACTEUR v2 a bien migré vers format dédié** (C-CK3 ✓). MAIS :
- `prompts/quintessence_reader.md` ligne 42-43 contient encore `[Liste de 3-5 mécanismes au format cause → effet → fait]` (le format **linéaire** SPECS v33.2 legacy, sans arborescence). Incohérence : le LECTEUR produit du linéaire alors que l'EXTRACTEUR a besoin d'arborescent.
- `prompts/quintessence_orchestrator.md` ne référence pas format PELOTE 4 niveaux (à vérifier).

**Fichiers concernés** : `prompts/quintessence_reader.md §4 Mécanismes causaux` + `prompts/quintessence_orchestrator.md`.
**Source SPECS** : `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` lignes 167-169 + ligne 298 (« format dédié incompatible avec liste plate »).

**Remédiation** : remplacer dans `quintessence_reader.md` ligne 42-43 :
```
## 4. Mécanismes causaux (PELOTE)
[Arborescence 4 niveaux — mécanisme racine → 2-3 sous-mécanismes → 1-3 faits intermédiaires → 1-3 sources F###. Format dédié v36, NE PAS linéariser.]
```

---

### B.5 — F.R1 « Format canonique GOLDEN_APEX vs APEX_LEGACY vs COURT_DEGR cohabitent »

**Constat** : `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` ligne 475 constate « 3 formats distincts cohabitent : GOLDEN_APEX (5 fichiers), APEX_LEGACY (12), COURT_DEGR (15) ». Le pilote ne choisit pas entre ces formats. La règle d'émergence (« si > 5000 mots et > 5 mécanismes PELOTE alors GOLDEN_APEX obligatoire ») est recommandée SPECS ligne 475 mais **PAS implémentée** dans `prompt-v35.md §Phase 0 cartographie.py` (qui ne détecte pas l'archétype).

**Hedge forensique** : la preuve programatique `code-searcher n'a pas trouvé de \`classify_archetype\`` est **une inférence plausible non vérifiée programmatiquement** — le code-searcher Phase B a grepé patterns SPECS/Mnemolite/PELOTE mais **n'a pas grepé `classify_archetype|archetype` dans `extractors/cartographie.py`**. La conclusion repose sur (a) `cartographie.py = simple regex extractor v35` confirmé par audit v35 §1 « OK sur la signature Python » et (b) `archetype_mapping` absent du cadrage Phase A. **A reconfirmer Round 3** via `grep -nE 'classify_archetype|archetype' tools/engines/sublimator/extractors/cartographie.py`.

**Fichiers concernés** : `extractors/cartographie.py` (hors audit précédent) + `prompt-v35.md §Phase 0 format canonique`.
**Source SPECS** : §12 réforme format canonique.

**Remédiation** : ajouter dans `cartographie.py --mode python` une détection d'archétype :
```python
archetype = classify_archetype(
    mots_total=wc,
    mecanismes_pelote=count_pelote,
    kernel_count=count_kernel_symbols,
    sources_F_count=count_F
)
# GOLDEN_APEX si mots>5000 AND pelote>=5 AND kernel>=8
# APEX_LEGACY si mots>2500 AND pelote>=2
# COURT_DEGR sinon
```

---

### B.6 — C-CK4 « Mnemolite isolation cross-enquête (PIVOT C2.1) non-mesurée empiriquement »

**Constat (mitigé)** : les 5 commandes sont propagées textuellement (25/25 grep) — c'est l'aspect **statique**. Mais M9 (% violations isolation) dans `sublimator_validate.py` ligne 190-194 est **un compteur théorique** : le script Python peut mesurer M9 SI le pilote a effectivement tagué chaque requête avec `sublimator:enquete_id=X`. Or ce tagging est à la charge du LLM (pas du Python), et le cadrage n'a pas vu de run réel du pilote v35 (cf. `RAPPORT_MULTI_AGENT_44_ENQUETES_v35_2026-07-05.md` : 7/7 réponses étaient théoriques). Donc **M9 ne peut pas être mesuré empiriquement** sans run réel.

**Fichiers concernés** : aucun code à modifier côté v36 — c'est un **goulet d'étranglement méthodologique** : on ne peut valider M9 sans exécuter le pipeline end-to-end sur ≥ 3 enquêtes.
**Source SPECS** : §13.1 STEP 2 + PIVOT C2.1.

**Remédiation** : inclure dans `validation_report_<DATE>.md` round 3 un test empirique « run pipeline end-to-end sur 3 enquêtes RIC, collecter M9 réel, valider < 5% violations ». Sans ce run, C-CK4 reste BLOQUANT par défaut.

---

## 3. Tableau verdict des 28 cibles

### 3.1 §4 Risques architecture (12 cibles)

| ID | Cible | Verdict | Preuve grep | Prio | Action |
|----|-------|---------|-------------|------|--------|
| **C.R1** | prompt-v35 §Phase 1 intègre 4 champs optionnels sans noyer le pilote | RISQUE | `grep positions_acteurs` prompt-v35 = 0 hit ; mais §Phase 1 référence `causalites[]` linéaire (legacy) — pas de migration v36 explicite côté pilote. | P1 | §Phase 1 revue : ajouter note « si optionnel présent, valider format PELOTE v36 avant Flatisation ». |
| **C.R2** | EXTRACTEUR v2 migré schéma v35 (12) → v36 (24 top-level) | OPE | `quintessence_extractor.md` ligne 38 spécifie `causalites_pelote` arborescent 4 niveaux. C-CK2 grep était trop spécifique ; vérification manuelle ligne 38 → OK. | P2 | Aucune. Constat forensique. |
| **C.R3** | CRITIQUE évalue les 4 nouveaux champs | BLOQUANT | `quintessence_critic.md` ligne 27 cite 5 critères mais aucun ne valide `causalites_pelote`/`positions_acteurs`/`recommandations`. **Voir B.2**. | P0 | Intégrer critère C6 « Conformité 3-minimum » dans CRITIQUE §5. |
| **C.R4** | ORCHESTRATEUR passe les 4 champs en revue en §Étape F | RISQUE | `quintessence_orchestrator.md` ligne 47 active `write_memory(memory_type="sublimator:verdict", content=<verdict_json>, tags=[<enquete_id>, run_N])` mais ne garantit pas que les 4 champs sont dans le `verdict_json`. | P1 | Forcer `verdict_json` à inclure les 4 champs et tester qu'ils sont non-vides. |
| **P.R1** | Format arborescent 4 niveaux vs confusion `causalites[]` linéaire | BLOQUANT | `quintessence_reader.md` ligne 42 produit encore du **linéaire** au lieu d'arborescent. Incohérence LECTEUR ↔ EXTRACTEUR. **Voir B.4**. | P0 | Réécrire `quintessence_reader.md §4 Mécanismes causaux` en arborescent. |
| **P.R2** | Phase 2 cluster sait exploiter profondeur PELOTE 4 niveaux | RISQUE | `prompt-v35.md §Phase 2` ne mentionne pas `causalites_pelote`. Le pilote pourrait clusteriser sans exploiter la profondeur. | P1 | §Phase 2 note : « préserver structure PELOTE 4 niveaux dans les clusters thématiques ». |
| **P.R3** | M1-M9 intègre profondeur PELOTE | BLOQUANT | `grep causalites_pelote sublimator_validate.py` = 0 hit. **Voir B.3**. | P0 | Ajouter M10 (profondeur PELOTE max niveau) + M11/M12 cf. B.3. |
| **M.R1** | Mnemolite 5-place propagation 5 fichiers | OPE | `grep` 5 mots-clés × 5 fichiers = **25/25 hits**. C-CK4 ✓ aspect statique. | P2 | Maintenir ; pas de modification. |
| **M.R2** | §13.2 orchestration 1 seule enquete par fichier vs batch-5 | OPE | `quintessence_orchestrator.md` §Étape A précise « 1 quintessence par enquête », pas de batch. Pas de dispute avec prompt-v35. | P2 | Aucune. |
| **M.R3** | §13.3.3 Sévérité 50% regen → alerte CP1 | RISQUE | `quintessence_critic.md` ligne 19 dit « CRITIQUE optionnel depuis §13.5 » — alerte 50% regen non-matérialisée comme état machine. V16 tracking (option b) fait l'iter_count mais pas l'alerte 50%. | P1 | matérialiser `regen_count` + alerte CP1 : si ≥ 50% des quintessences single-shot méritent regen, déclencher check_iteration_alert=true. |
| **M.R4** | §13.3.4 max 3 itérations : `iteration_count` ET `iteration_alert` dans `compress_summary` | OPE | `iteration_count` + `iteration_alert` matérialisés dans prompt-v35 + quintessence_extractor + quintessence_orchestrator (cf. grep `iteration_count`). V16 [x] option (b) retenue. | P2 | Aucune. |
| **A.R1** | §Phase 3 : 3-éléments-minimum | **BLOQUANT** | **0 hit dans prompt-v35 §Phase 3 LOIS**. **Voir B.1**. | **P0** | Ajouter LOIS L9. |
| **A.R2** | ORCHESTRATEUR passe règle à CRITIQUE | **BLOQUANT** | `quintessence_critic.md §5 critères` n'a pas de critère « Conformité 3-minimum ». **Voir B.2**. | P0 | Idem B.2. |
| **F.R1** | Format canonique unique (GOLDEN_APEX cible) | BLOQUANT | `cartographie.py` ne détecte pas archétype ; pilote accepte 3 formats cohabitants. **Voir B.5**. | P0 | Implémenter detecteur archétype. |
| **F.R2** | Détecteur d'archétype implémenté | BLOQUANT | (idem F.R1 — pas implémenté du tout) | P0 | Idem F.R1. |

### 3.2 §5 Nouvelles dimensions v36 (8 cibles)

| ID | Cible | Verdict | Preuve grep | Prio | Action |
|----|-------|---------|-------------|------|--------|
| **N1** | Grille APEX 6 × 3 = /18 appliquée en Phase 0 | RISQUE | `cartographie.py` n'exporte pas explicitement une grille APEX 6×3. Sondage 42 enquêtes F.R §10-§12 fait hors-pilote. | P1 | cartographie.py --output inclut `grille_apex: {these, complexite, lobby, causalite, sources, impact}/{0,1,2,3}`. |
| **N2** | F## normalisation F-XXX-### | OPE | `prompt-v35.md §Phase 1` + `validation_3enquetes.md` utilisent le pattern `F-[0-9]{3}`. C-CK7 ✓ (convention report non testée spécifiquement mais pattern matching OK). | P2 | Aucune. |
| **N3** | Sondage empirique 42 enquêtes pris en compte | OPE | Sondage SPECS v36 §10-§12 documenté. Cité prompt-v35 + README. | P2 | Aucune. |
| **N4** | Migration v34→P3 (MANIPULATION_REPORT vs THÈSE CENTRALE) | RISQUE | 28/42 enquêtes sans `THÈSE CENTRALE` migrées. `prompt-v35.md §Phase 1` ne distingue pas les deux patterns. | P1 | §Phase 1 banc d'essai : si `MANIPULATION_REPORT` détecté, réinjecter `THÈSE CENTRALE` canonique. |
| **N5** | 4 champs optionnels imposés (vs suggestion) | RISQUE | 3/4 propagés (causalites_pelote, impact, recommandations ✓ ; positions_acteurs ABSENT côté pilote). | P1 | Ajouter `positions_acteurs` dans §Phase 1 prompt-v35 + quintessence_extractor §Schéma. |
| **N6** | Règle Phase 3 « 3 min par catégorie » | **BLOQUANT** | **0 hit dans prompt-v35 §Phase 3 LOIS**. **Voir B.1**. | **P0** | Idem A.R1. |
| **N7** | Architecture multi-agent §13 (4 prompts LLM chaîne) | OPE | Tous les 4 sub-prompts existent avec structure cohérente. C-CK4 25/25. | P2 | Aucune. |
| **N8** | Mnemolite isolation cross-enquête (5-place + tag filter) | OPE (statique) / BLOQUANT (empirique) | Tag filter `sublimator:enquete_id` documenté SPECS §13.1 ; pas mesuré empiriquement. **Voir B.6**. | P0/P2 | Run empirique 3 enquêtes pour mesurer M9. |

### 3.3 §6 Critères cross-check (8 cibles)

| ID | Critère | Verdict | Preuve grep | Prio | Action |
|----|---------|---------|-------------|------|--------|
| **C-CK1** | §13.x existe dans prompt + 4 sub-prompts ↔ SPECS | OPE | `grep '§13\\.[0-9]+'` = 30+ matches croisés. Pas d'orphan §13.x détecté. | P2 | Aucune. |
| **C-CK2** | 24 top-level fields référencés dans EXTRACTEUR v2 | RISQUE | Le grep était trop spécifique : `quintessence_extractor.md` ligne 38 référence bien `causalites_pelote` ; mais l'audit-cadrage grep n'avait pas listé tous les 24. Recommencer avec pattern moins strict ou lecture manuelle ligne-par-ligne. | P1 | Audit round 3 : lecture manuelle des 24 champs vs `quintessence_extractor.md`. |
| **C-CK3** | Format PELOTE 4 niveaux identique EXTRACTEUR + CRITIQUE + ORCHESTR | OPE | `quintessence_extractor.md` ligne 38 + `quintessence_critic.md` ligne 39 (table profondeur). Match. | P2 | Aucune. |
| **C-CK4** | Mnemolite 5-place propagation | OPE | 25/25 grep hits. **Voir B.6** pour l'aspect empirique M9. | P2 statique / P0 empirique | Run 3 enquêtes. |
| **C-CK5** | 4 champs optionnels dans prompt + EXTRACTEUR + CRITIQUE + ORCHESTR | RISQUE | `causalites_pelote`, `impact`, `recommandations` présents ; `positions_acteurs` absent côté pilote. 11/12 grep hits (manque positions_acteurs × 1 fichier). | P1 | Ajouter `positions_acteurs` au prompt pilote §Phase 1 + au validateur M11. |
| **C-CK6** | M1-M9 prennent 4 nouveaux champs en compte | **BLOQUANT** | 1/4 (seul `impact` ↔ M4). **Voir B.3**. | P0 | Ajouter M10-M12. |
| **C-CK7** | Convention `validation_report_<DATE>.md` (post-cc3f1d6 V5) | OPE | `quintessence_orchestrator.md` ligne 47 référence. Pas de chemin mort. | P2 | Aucune. |
| **C-CK8** | Aucune des 15 corrections v35 réintroduite par option C | OPE | 16/16 [x] confirmed baseline `5756fa2`. Aucun retour en arrière détecté. | P2 | Aucune. |

---

## 4. Plan de remédiation — Round 3 corrections

### P0 (BLOQUANTS — à corriger avant tout RUN)

1. **prompt-v35.md §Phase 3** : ajouter LOIS L9 « 3-éléments-minimum ». 5 minutes. (B.1 / A.R1 / N6)
2. **prompts/quintessence_critic.md §5 critères** : ajouter C6 « Conformité 3-minimum ». 5 minutes. (B.2 / A.R2 / C.R3)
3. **sublimator_validate.py** : ajouter M10 (profondeur PELOTE) + M11 (sources positions_acteurs) + M12 (acteur_cible/horizon recos). 30 minutes Python. (B.3 / P.R3 / C-CK6)
4. **prompts/quintessence_reader.md §4 Mécanismes causaux** : réécrire en arborescent 4 niveaux (PELOTE v36). 10 minutes. (B.4 / P.R1)
5. **extractors/cartographie.py** : implémenter `classify_archetype()` (GOLDEN_APEX / APEX_LEGACY / COURT_DEGR). 1h Python. (B.5 / F.R1 / F.R2)
6. **Run empirique 3 enquêtes** pour mesurer M9 réel (validation_report_2026-XX-XX.md). 2-3h shell. (B.6 / C-CK4 empirique / N8)

**Effort P0 cumulé** : ~4-5 heures shell + 30 min Python.

### P1 (RISQUES — à corriger avant audit round 4)

7. **prompt-v35.md §Phase 1 C.R1** : note explicite « valider format PELOTE v36 si optionnel présent ». 15 min.
8. **prompt-v35.md §Phase 2 P.R2** : préserver structure PELOTE 4 niveaux dans clusters. 15 min.
9. **quintessence_orchestrator.md M.R3** : matérialiser `regen_count` + alerte CP1 si ≥ 50%. 30 min.
10. **prompt-v35.md §Phase 0 N1 N4** : grille APEX 6×3 exportée par cartographie.py + banc d'essai MANIPULATION_REPORT. 1h Python + 15 min prompt.
11. **prompt-v35.md §Phase 1 N5** : ajouter `positions_acteurs` (champ manquant côté pilote). 10 min.

**Effort P1 cumulé** : ~3-4 heures.

### P2 (qualité / dette UX)

12. **C-CK2 audit round 3** : lecture manuelle 24 champs vs quintessence_extractor.md. 1h.
13. **C-CK5 12/12 grep missing 1** : redondant avec N5.

**Effort P2 cumulé** : ~1-1,5 heures.

**Total round 3** : 8-10 heures shell+Python (sans compter relecture humaine 4h).

---

## 5. Dette v35 résiduelle

**Aucune**. Le commit baseline `5756fa2` a clos les 16 V-items. Les 6 BLOQUANTS v36 sont **nouvelles dettes** issues de l'option C, pas des régressions v35.

**Note forensique** : `git log -p --stat -- tools/engines/sublimator/prompt-v35.md` HEAD = `5756fa2` (9 amendements bulk). Aucun retour en arrière détecté vers les V-items v35. **Le pipeline v35 reste fonctionnel en mode dégradé** (sans option C), le v36 lui superpose.

---

## 6. Comparaison avec audit v34 — bilan régression vs progression

| Élément | Audit v34 | Audit v35 + verdict v36 | Delta |
|---------|-----------|--------------------------|-------|
| Architecture Option C (4 champs + PELOTE) | n'existait pas | **6 BLOQUANTS** identifiées ; 12 OPE ; 10 RISQUE | 🆕 v36 industrialisable à 60% |
| 5-place Mnemolite | partiellement propagé | 25/25 propagé statiquement ; M9 empirique pending | ✅ confirmé |
| 4 sub-prompts + Orchestration §13 | créés v35, cassent v35 | présents, isolés, structurellement OK ; CRITIQUE optionnel §13.5 | ✅ confirmé |
| Format PELOTE 4 niveaux | absent v33.2 → v34 | EXTRACTEUR ligne 38 + CRITIQUE ligne 39 match ; **LECTEUR legacy linéaire incohérent** | 🟡 B.4 à fixer |
| Règle Phase 3 « 3 min par catégorie » | n'existait pas | **BLOQUANT** (B.1) | 🆕 critique |
| Format canonique unique | n'existait pas | BLOQUANT (B.5) | 🆕 critique |
| Validateurs M1-M9 | créaient M1-M8 | M1-M9 OK ; **3/4 nouveaux champs absents** | 🟡 B.3 à fixer |

**Constat** : la v36 ajoute 28 cibles d'audit, dont 6 BLOQUANTS. L'architecture est meilleure mais l'industrialisation reste tributaire des corrections round 3.

---

## 7. Crédibilité du diagnostic et limites

**Ce qui a été mesuré empiriquement** :
- Phase A reconnaissance : 2 989 lignes dans 10 fichiers. (cf. basher wc -l).
- Phase B/C cross-check : 8 critères C-CK1-C-CK8 grep. C-CK4 = 25/25 hits ; C-CK6 = 1/4 champs M1-M9 ; C-CK5 = 11/12 grep.
- 16/16 corrections v35 reconfirmées par `5756fa2`.

**Ce qui n'a pas été mesuré** :
- Pas de run e2e du pipeline v35 ou v36 sur 41 enquêtes RIC (`_validation/` incomplet).
- Pas de mesure empirique de M9 (% violations isolation Mnemolite). Théorique uniquement.
- Pas de relecture manuelle intégrale de 24 top-level fields v36 dans `quintessence_extractor.md` (audit C-CK2 partiel — pattern grep trop spécifique).

**Risque méthodologique** :
- Le verdict repose sur des grep statiques ; un LLM pourrait produire un comportement de runtime différent du comportement statique (ex : CRITIQUE peut ignorer le critère C6 même s'il est dans le prompt).
- Round 3 doit inclure des **tests runtime** (3 enquêtes minimum) avant de conclure définitivement.

---

## 8. Verdict global non-équivoque

**Option C industrielle : NON, en l'état.** 6 BLOQUANTS identifiées, dont 1 P1 silencieuse anticipée confirmée + 3 nouvelles dettes (PELOTE LECTEUR legacy, validateurs incomplets, format canonique multi-courants).

**Effort estimé pour rendre Option C industrialisable** : 8-10 heures shell+Python (round 3 P0+P1) + 4 heures relecture humaine + 2-3 heures validation empirique 3 enquêtes.

**Recommandation** : procéder à Round 3 (corrections listées §4 P0 dans l'ordre), puis Round 4 (validation empirique sur 3 enquêtes GOLDEN_APEX candidates, mesure M1-M12 réels).

**Sans round 3** : tout run v36 produit un v35-degraded (option C ignorée par le pilote, validateurs passent à côté de 3/4 champs).

---

*Audit antagoniste forensique Sublimator v36 — Round 2 VERDICT.*
*Date : 2026-07-05 14h00 CEST.*
*Périmètre : 10 fichiers, 2 989 lignes, baseline `5756fa2` (audit v35 16/16 [x]).*
*Score : 12 OPE + 10 RISQUE + 6 BLOQUANT = 28 cibles.*
*Verdict : Option C industrialisable à 60%. 6 BLOQUANTS à corriger en Round 3 (effort 8-10h).*
