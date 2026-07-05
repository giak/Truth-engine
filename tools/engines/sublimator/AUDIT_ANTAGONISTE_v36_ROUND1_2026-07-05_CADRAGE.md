# Audit antagoniste forensique Sublimator v36 : Round 1 (CADRAGE)

> **Date** : 2026-07-05 13h36 CEST
> **Type** : Cadrage méthodologique (pré-audit, pas de verdict).
> **État de l'art v35** : 16 contradictions identifiées (9 P1 + 7 P2). P1 closes via commits `a7adbd7` / `64389da` / `405e00b` / `0e29c8f` / `5108ff1`. P2 : V6, V7, V10, V14, V15 closes, V16 reste ouvert. Total : 15/16 contradictions v35 théoriquement closes, 1 ouverte (V16 tracking).
> **Déclencheur v36** : `2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` (matrice A/B/C). Option C (hybride) retenue implicitement comme cible par les fixes post-refactor `ce550c9`. Architecture multi-agent §13 esquissée (4 prompts LLM en chaîne). Validation empirique §13.5 non encore exécutée.
> **Périmètre** : prompt-v35.md (277 lignes post-ce550c9) + SPECS v36 + 4 sub-prompts (`quintessence_{reader,extractor,critic,orchestrator}.md`) + 2 validateurs Python + sublimator_pilot.py + Mnemolite contrat (5-place redundancy).

---

## 1. Cible

**Inclus dans l'audit** :

- `tools/engines/sublimator/prompt-v35.md` (pilote top-level, 277 lignes).
- `tools/engines/sublimator/2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md` (SPECS v36, 1250 lignes).
- `tools/engines/sublimator/prompts/quintessence_reader.md` (Agent 1 LECTEUR).
- `tools/engines/sublimator/prompts/quintessence_extractor.md` (Agent 2 EXTRACTEUR v2).
- `tools/engines/sublimator/prompts/quintessence_critic.md` (Agent 3 CRITIQUE).
- `tools/engines/sublimator/prompts/quintessence_orchestrator.md` (Agent 4 ORCHESTRATEUR).
- `tools/engines/sublimator/sublimator_validate.py` (~290 lignes).
- `tools/engines/sublimator/sublimator_retry.py` (~135 lignes).
- `tools/engines/sublimator/sublimator_pilot.py` (~330 lignes).
- `tools/engines/sublimator/AUDIT_ANTAGONISTE_v35_2026-07-05.md` (audit précédent, pour cross-ref).

**Exclus du périmètre** :

- `tools/engines/sublimator/extractors/cartographie.py` (audit précédent OK sur la signature Python).
- `tools/engines/sublimator/extractors/gates.py` (idem).
- 42 enquêtes `investigations/2026-07-04-RIC/*_INVESTIGATION.md` (sondage fait en v36 §10-§12).
- `_validation/RIC/` (déjà couvert par v35 RAPPORT_MULTI_AGENT).

---

## 2. Méthode

1. **Relecture contradictoire** : chaque section du prompt-v35 confrontée à SPECS v36 §équivalent. Si divergence, marquer P-candidat.
2. **Cross-ref croisés** : pour chaque référence §13.x dans prompt-v35 ou sub-prompts, vérifier existence et contenu dans SPECS v36 §13.x.
3. **Empirique basher** : grep des 24 top-level fields (6 requises + 6 optionnelles legacy + 4 v36) dans les 4 sub-prompts. Compter les occurrences, vérifier la cohérence.
4. **Rejeu RAPPORT_MULTI_AGENT v35** : 7 questions de Q1 à Q7 + Preuves 1-7 + Estimations 2-3-4-6. Vérifier si les bloquants sont clos ou persistent.
5. **Lecture KERNEL + PELOTE** : sur enquête religieuse (§3 SPECS v36, GOLDEN_APEX cible), vérifier que la chaîne 4 niveaux est documentée de manière identique partout (SPECS + EXTRACTEUR + CRITIQUE).
6. **Comparaison v35/v36 vs audit antagoniste v34** : ce qui a régressé vs progressé, en miroir de la table §9 AUDIT v35.

**Livrables par section** : verdict (OPE / RISQUE / BLOQUANT) + source citation + ligne/P + recommandation actionnable.

---

## 3. État de l'art post-v35 (à reconfirmer)

| # | V35 | Statut actuel | Source vérif | À reconfirmer ROUND 1 |
|---|-----|---------------|--------------|------------------------|
| V1 | Panachage versions v2/v3/v35/v36 | Clos via Note terminologique §R1 prompt-v35.md | `0e29c8f` | OUI (terminologie propagée partout ?) |
| V2/V3 | Phrases orphelines Phase 1-2 | Clos via correctif markdown | `0e29c8f` (présumé) | OUI |
| V4 | `spanw` typo | Clos via sed | `a7adbd7` (audit) | NON (regexp grep OK) |
| V5 | §Étape F chemins morts | Clos via Mnemolite archivage | À reconfirmer via `grep -nE 'write_memory|memory_type' quintessence_orchestrator.md` | OUI (convention active ?) |
| V6 | Note migration dupliquée | Clos par retrait | À reconfirmer via `grep -nE 'migration|Note migration v1' prompt-v35.md promts/quintessence_extractor.md` | OUI (note purgée grep ?) |
| V7 | `### v2` hiérarchie | Clos via sed | À reconfirmer via `grep -nE '^## Version v2 de EXTRACTEUR' quintessence_extractor.md` | NON (grep OK) |
| V8 | `défini défini` ×4 | Clos via sed | `a7adbd7` (audit) | NON (grep OK) |
| V9 | Naming _validation/ regression | Clos via fuzzy match `sublimator_validate.py` | À reconfirmer via `grep -nE 'fuzzy|normalize|underscore|hyphen' sublimator_validate.py` | OUI (test fonctionne?) |
| V11 | Statut Phase 0 cardex | Clos via section dédiée | `0e29c8f` | OUI (énum error ?) |
| V12 | `search_mode="hybrid"` sub-prompts | Clos via ajout ×4 | `a7adbd7` (audit) | OUI (propagé correctement ?) |
| V13 | `get_system_snapshot` sub-prompts | Clos via ajout ×4 | `a7adbd7` (audit) | OUI (idem V12) |
| V14 | Test E2E dispatch | Clos via `test_e2e_dispatch_v35.py` | À reconfirmer via `pytest tests/pipelines/test_e2e_dispatch_v35.py -v` | OUI (toujours OK ?) |
| V15 | README Sublimator | Clos via `README.md` complet | À reconfirmer via `wc -l tools/engines/sublimator/README.md` | NON (132 lignes présentes) |
| V10 | Claim « 3 arrêts » non-mesuré | Clos par retrait §Diff v34 + note forensique AUDIT §6 | `5108ff1` | NON (audit V10 étendu) |
| V16 | Tracking Mnemolite itérations | OUVERT | n/a | OUI (clé `sublimator:iterations:` matérialisée ?) |

**Action** : pour chaque ligne « OUI » dans la dernière colonne, vérification grep + lecture ciblée dans ROUND 2.

---

## 4. Inventaire des zones de risque v36

### 4.1 Architecture (option C hybride)

| Risque | Zone fichier | Source SPECS v36 | Sévérité attendue |
|--------|--------------|------------------|-------------------|
| **C.R1** | prompt-v35.md Phase 1 | §13.3.2 | 4 champs optionnels (`positions_acteurs`, `causalites_pelote`, `impact`, `recommandations`) bien intégrés sans noyer le pilote |
| **C.R2** | quintessence_extractor.md §Schéma | §13.3.2 | EXTRACTEUR v2 a-t-il migré du schéma v35 (12 champs) vers v36 (24 top-level fields) ? |
| **C.R3** | quintessence_critic.md §Critères | §13.3.3 | CRITIQUE évalue-t-il les 4 nouveaux champs ? (probablement non, c'est un risque) |
| **C.R4** | quintessence_orchestrator.md §Étape F | §13.6 Schéma | ORCHESTRATEUR passe-t-il les 4 champs en revue lors de la boucle de régénération ? |

### 4.2 Format PELOTE dédié

| Risque | Zone fichier | Source SPECS v36 | Sévérité attendue |
|--------|--------------|------------------|-------------------|
| **P.R1** | quintessence_extractor.md § | §13.3.2 | Format arborescent 4 niveaux (mécanisme → sous-mécanisme → fait intermédiaire → source F-###) documenté OU confusion avec `causalites[]` linéaire ? |
| **P.R2** | prompt-v35.md Phase 2 | §Orchestration séquencement | Phase 2 cluster sait-elle exploiter la profondeur 4 niveaux de `causalites_pelote` ? (sinon perte de la causation depth) |
| **P.R3** | Validateurs Python | sublimator_validate.py | Mesure M1-M9 : intègre-t-elle la profondeur PELOTE ? (probablement NON, à ajouter) |

### 4.3 Architecture multi-agent §13

| Risque | Zone fichier | Source SPECS v36 | Sévérité attendue |
|--------|--------------|------------------|-------------------|
| **M.R1** | 4 sub-prompts isolés vs prompt-v35 référent | §13.3.1-§13.3.4 | Mnemolite 5-place redundancy (get_system_snapshot + search_memory + tag + cardex + HALTE) est-elle propagée correctement ? |
| **M.R2** | quintessence_orchestrator.md §Étape A | §13.2 orchestration | « 1 seule enquete.md jamais plusieurs » (cf. Q2 multi-agent, batch-5 vs per-file) : dispute-t-on le §Phase 1 batch-par-5 avec §Orchestration per-file ? |
| **M.R3** | quintessence_critic.md §50% regen | §13.3.3 Sévérité | « 50% des quintessences single-shot méritent régénération ». Confronté à V16 tracking, génère-t-il vraiment l'alerte vers CP1 ? |
| **M.R4** | quintessence_orchestrator.md §Étape D | §13.3.4 | Boucle max 3 itérations : matérialise-t-elle `iteration_count` ET `iteration_alert` dans `compress_summary` ? (résout V16 partiellement) |

### 4.4 Phase 3 règle « 3 min par catégorie »

> **⚠️ P1 silencieuse anticipée (micro-observation code-reviewer)** : la règle « Phase 3 : 3 éléments min par catégorie » listée ci-dessous n'est PAS présente dans `prompt-v35.md` §Phase 3 LOIS L1-L8 (vérifié en session 2026-07-05). Tant que cette règle manque, l'option C est inopérante : le pilote ignore les 4 champs ajoutés en Phase 3 article, brisant la promesse d'actionnabilité de SPECS v36 §5.1. **À traiter en P0 du ROUND 2**.

| Risque | Zone fichier | Source SPECS v36 | Sévérité attendue |
|--------|--------------|------------------|-------------------|
| **A.R1** | prompt-v35.md §Phase 3 LOIS | §6 Option C règle | Pour chaque § d'article, 3 éléments minimum piochés dans `positions_acteurs` + `causalites_pelote` + `impact` + `recommandations`. **Règle absente du prompt au round 1**. |
| **A.R2** | quintessence_orchestrator.md §Étape C → Phase 3 | §13.3.3→§13.6 | L'ORCHESTRATEUR passe-t-il la règle à l'Agent 3 (CRITIQUE) lors de l'évaluation Phase 3 ? |

### 4.5 Réforme format canonique (§12 SPECS v36)

| Risque | Zone fichier | Source SPECS v36 | Sévérité attendue |
|--------|--------------|------------------|-------------------|
| **F.R1** | prompt-v35.md Phase 0 / 1 | §12.6 | Format canonique unique (GOLDEN_APEX cible). Le pilote accepte-t-il des enquêtes 4-archétypes (GOLDEN_APEX 1/42, NARRATIF 22, FAST_REPORT 15, META_AUDIT 4) ? |
| **F.R2** | cartographie.py (extractor) | §10 not in audit scope | Le détecteur d'archétype est-il implémenté ? ou la grille APEX 6×3 = /18 est-elle uniquement déclarative ? |

---

## 5. Nouvelles dimensions v36 (non existantes v35)

Ces zones n'étaient pas dans l'audit v35. Elles sont neuves dans v36 et DOIVENT être auditées en round 1.

| # | Dimension | Source SPECS v36 | Méthode audit |
|---|-----------|------------------|---------------|
| N1 | Grille APEX 6 dimensions × 3 points = /18 | §3.1 + §10 AUDIT | Vérifier que la grille est appliquée en Phase 0 (cartographie.py) |
| N2 | F## normalisation F-XXX-### | §10.4.2 + §12.4 | Constater 7 nomenclatures distinctes sur 14 fichiers, vérifier qu'une unification est imposée |
| N3 | Sondage empirique 42 enquêtes | §3.3 + §10 + §12 | Sondage déjà fait dans SPECS v36 §10-§12. Vérifier prise en compte dans prompt-v35 (ou doc séparée ?) |
| N4 | Format `MANIPULATION_REPORT` vs `THÈSE CENTRALE` | §10.4.3 | Migration v34→P3 a supprimé KERNEL dans 28/42 enquêtes. Règle de réinjection dans prompt ? |
| N5 | 4 champs optionnels schéma quintessence | §5.1 option C | Imposés ou optionnels ? (sinon perte KERNEL/PELOTE se reproduit) |
| N6 | Règle Phase 3 « 3 min par catégorie » | §5.1 C-3 | Documentée dans prompt et validateur ? (sans elle, le pilote ignore les 4 champs) |
| N7 | Architecture multi-agent §13 (4 prompts LLM) | §13.2 schéma | trade-off vs scripts Python : 4 prompts isolés, critique granulaire, orchestration |
| N8 | Mnemolite isolation cross-enquête | §13.1 STEP 2 | Mnemolite 5-place redundancy + tag filter `sublimator:enquete_id=X` |

---

## 6. Critères de cross-check

| Check | Méthode | Source |
|-------|---------|--------|
| **C-CK1** | Pour chaque §13.x référencé dans prompt-v35 ou sub-prompts, existe-t-il dans SPECS v36 ? | grep `§13\.[0-9]+` |
| **C-CK2** | Les 24 top-level fields sont-ils tous référencés dans EXTRACTEUR v2 ? | grep des 24 noms de champs |
| **C-CK3** | Format PELOTE 4 niveaux (mécanisme, sous-mécanisme, fait, source) :定義 identique dans EXTRACTEUR + CRITIQUE + ORCHESTRATEUR ? | grep `niveau.*[1-4]` |
| **C-CK4** | Mnemolite 5-place (get_system_snapshot + search_memory + tag filter + cardex + HALTE) : présent dans les 5 fichiers (prompt + 4 sub-prompts) ? | grep Mnemolite contrat |
| **C-CK5** | 4 champs optionnels v36 (`positions_acteurs`, `causalites_pelote`, `impact`, `recommandations`) : référencés dans prompt-v35 + EXTRACTEUR + CRITIQUE + ORCHESTRATEUR ? | grep des 4 noms |
| **C-CK6** | Validateurs Python (`sublimator_validate.py` + `sublimator_retry.py`) : critères M1-M9 prennent-ils en compte les 4 nouveaux champs ? | lecture code M1-M9 |
| **C-CK7** | Convention `validation_report_<DATE>.md` (post-cc3f1d6 V5) : active et bien formée ? | grep paths |
| **C-CK8** | Vitesse contradictions V35 reopen : aucune des 15 closes n'est réintroduite par l'option C ? | diff prompt-v35 vs commit `0e29c8f` |

---

## 7. Calendrier d'inventaire (suggestion)

**Phase A — Reconnaissance (30 min, basher)** :
1. Vérifier §3 (état de l'art v35) : grps ciblés pour chaque V1-V16 encore à reconfirmer.
2. Vérifier §4 (zones de risque v36) : grep des 4 noms optionnels dans prompt-v35 + 4 sub-prompts.
3. Vérifier §5 (nouvelles dimensions) : grep format canonique, format PELOTE 4-niveaux, règle Phase 3 3-min.

**Phase B — Lecture contradictoire (90 min, parallèle)** :
1. Re-lecture prompt-v35.md (chapitre par chapitre vs SPECS v36).
2. Re-lecture SPECS v36 §13.3.2 (schéma quintessence v36).
3. Re-lecture 4 sub-prompts (focus format PELOTE + Mnemolite + 4 nouveaux champs).
4. Re-lecture 2 validateurs Python (focus M1-M9 vs 24 top-level fields).

**Phase C — Cross-check (60 min)** :
1. Pour chaque item §6 (8 critères C-CK), grep ciblé + lecture code.
2. Pour chaque zone §4 (12 risques R1-R5), confirmer/casser.
3. Pour chaque dimension §5 (8 N), constater présence/absence.

**Phase D — Synthèse (30 min)** :
1. Compter les verdicts par catégorie (OPE / RISQUE / BLOQUANT).
2. Identifier les P0 (non-industrialisable) vs P1 (à corriger avant) vs P2 (qualité).
3. Rédiger le verdict final `AUDIT_ANTAGONISTE_v36_ROUND2_VERDICT_2026-XX.md`.

---

## 8. Livrables attendus

| # | Document | Type | Lignes estimées |
|---|----------|------|----------------|
| 1 | Cette cadrage | Pré-audit | ~150 |
| 2 | AUDIT_ANTAGONISTE_v36_ROUND2_VERDICT_2026-XX.md | Verdict (P0+P1+P2) | ~300-500 |
| 3 | AUDIT_ANTAGONISTE_v36_ROUND3_CORRECTIONS_2026-XX.md | Liste commits idempotents par contradiction | ~100 |
| 4 | RAPPORT_EMPIRIQUE_v36_3ENQUETES_2026-XX.md | Validation §13.5 | ~150 |
| 5 | AUDIT_ANTAGONISTE_v36_ROUND4_VERIF_EMPIRIQUE_2026-XX.md | Re-run post-corrections | ~150 |

**Effort total estimé** : 5-6h shell+Python + 4h relecture humaine + 1-2h validation empirique 3 enquêtes × 3 runs.

---

## 9. Hors-périmètre (out of scope)

- Refonte du schéma v36 lui-même (option C fixé dans SPECS).
- Évaluation des 42 enquêtes RIC en tant que contenu (sondage déjà fait §10-§12).
- Choix du LLM hôte (Gemini vs Claude vs local) : agnosticité gardée dans prompt.
- Mnemolite implémentation côté MCP (aspirational only dans ce dépôt).

---

## 10. Crédibilité du diagnostic et limites

**Ce que cette cadrage présuppose** :

- v35 round 1 a été audité forensiquement (cf. AUDIT_ANTAGONISTE_v35_2026-07-05.md, 16 contradictions).
- SPECS v36 est la spec de référence (matrice A/B/C tranchée vers C implicitement).
- Les 4 sub-prompts existent dans `tools/engines/sublimator/prompts/` mais pas tous validés post-SPECS-v36.
- Le projet utilise des outils gratuits, pas d'API LLM payante (cf. conversation 2026-07-05).

**Ce qui sera mesuré en ROUND 2** :

- Pour chaque zone §4, présence/absence confirmée par grep.
- Pour chaque dimension §5, application effective vs déclaratif.
- Pour chaque critère §6, conformité au schéma canonique.

**Ce qui restera théorique** :

- Volume de tokens réel pour 41 enquêtes (estimation 2.5-27M, mesure à venir round 4).
- Hallucination rate sur 4 nouveaux champs (mesure à venir round 4 via `validation_3enquetes.md`).
- Itération_alert_count CPU réel (mesure à venir round 4 via `iteration_count` matérialisé).

**Risque méthodologique** : risque de régression circulaire si les fixes V1-V15 ont introduit de nouvelles contradictions v36-spécifiques. Le Round 2 doit explicitement tester cette hypothèse.

---

*Audit antagoniste forensique Sublimator v36 - Round 1 (CADRAGE).*
*Date : 2026-07-05 13h36 CEST.*
*Périmètre : 1 pilote + 1 SPECS + 4 sub-prompts + 2 validateurs + 1 orchestrateur side-car (10 fichiers).*
*Verdict : PRÉ-AUDIT. Pas de verdict ici. Round 2 livrera le verdict dimensionnel.*
*Effort Round 2 : 4-5h shell + relecture + cross-check pour passer du CADRAGE au VERDICT.*
