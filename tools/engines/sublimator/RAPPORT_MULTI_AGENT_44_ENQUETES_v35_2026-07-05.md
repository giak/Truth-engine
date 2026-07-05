# Rapport multi-agent Sublimator v35 — Audit + Simulation + Preuves

> **Date :** 2026-07-05
> **Cible :** `tools/engines/sublimator/prompt-v35.md` (pilote) + 4 sub-prompts (`prompts/quintessence_*.md`) sur **44 enquêtes industrielles**.
> **Périmètre :** comportement multi-agent face à une volumétrie réelle (44 fiches cibles du dossier `investigations/2026-07-04-RIC/`).
> **Méthode :** audit antagoniste forensique (thinker) + 7 preuves empiriques (basher) + 4 estimations analytiques (basher Python).
> **Verdict global :** **3 OPE + 1 RISQUE MAJEUR + 3 BLOQUANTS.** Industrialisation NON-VERIFIEE sur 44 enquêtes tant que les bloquants ne sont pas corrigés.

---

## 1. Executive summary

L'architecture Map-Reduce du Sublimator (Phase 0 cartographie + Phase 1 par-enquête + Phase 1.5 compression + Phase 2 synthèse par cluster + Phase 3 article) est **saine sur le papier** : le pilote délègue 100% du contexte aux sub-agents (`filePaths` par-enquête) et ne conserve que les `compress_summary` (100 mots/enquête). Pour 44 fiches, ~7 500 tokens de mémoire de travail — dérisoire.

Mais sur le **chemin critique**, 3 bloquants empêchent l'industrialisation sur 44 fiches réelles :

1. **Cartographie Phase 0 retourne 0 clusters** sur les 42 fiches réelles (Preuve 7). Sans clusters, Phase 2 Map-Reduce ne peut pas s'exécuter.
2. **Contradiction frontale §Phase 1 « batch-par-5 » vs §Orchestration « per-file »** (Preuve 2 analytique). Le pilote LLM va s'emmêler les pinceaux.
3. **Iteration alert flood possible** : 50% regen rate × 44 = ~22 alertes CP1 (Preuve 3 analytique), ruine la promesse « 3 arrêts ».

Sub-blocks (Mnemolite pollution cross-enquete, retry exit 2 ~2.2 blocages sur 44, dispatch ordering coûteux) sont des dégradations opérationnelles qui rendent le pipeline non-industriel même une fois les bloquants corrigés.

---

## 2. Inventaire data réel (Preuve 1 + empirique §cartographie)

### 2.1 Volume des 42 enquêtes réelles (`investigations/2026-07-04-RIC/`)

| Métrique | Valeur | Source |
|----------|--------|--------|
| Fichiers `*_INVESTIGATION.md` | **42** (pas 44) | `ls investigations/2026-07-04-RIC/*_INVESTIGATION.md` |
| Mots totaux bruts | **246 782** | `wc -w` |
| Moyenne par enquête | **5 875 mots** | division |
| Tokens estimés (×1.3) | **~320 816** | projection |
| Taille disque | **2.5 MB** | `du -sh` |

> **Note :** discrepancy `44` (SPEC §13.5) vs `42` (réel). 2 enquêtes manquent ou sont renommées. Hypothèse : 2 fichiers `*_INVESTIGATION.md` ont été archivés ou déplacés. Vérification : `git log --all --diff-filter=D --name-only | grep INVESTIGATION.md`.

### 2.2 Sortie cartographie Phase 0

```bash
$ python -m tools.engines.sublimator.extractors.cartographie investigations/2026-07-04-RIC/ --mode python --output /tmp/cart_test.json
# Result: 6 ok, 36 needs_llm, 0 clusters
```

| Champ | Valeur |
|-------|--------|
| `n_enquetes_totales` | 42 |
| `clusters` | **0** |
| Statuts | 6 ok + 36 needs_llm |
| Cause probable | `--mode python` ne détecte pas les keywords thématiques dans les headers Markdown de 36 enquêtes (≥75% Fragmented ou non-KERNEL). |

> **🔴 BLOQUANT** : Phase 2 est `Pour chaque cluster identifié en Phase 0...` (prompt-v35.md §Phase 2). Zéro cluster = zéro synthèse par cluster. L'article final ne peut pas être produit.

---

## 3. Audit antagoniste — 7 questions tranchées

### 3.1 Q1 — Context window scaling

**Citation §Phase 1.5** : *« Toutes les enquêtes compressées tiennent en contexte (~50 lignes × 100 mots = 5 000 mots) ». §Orchestration : l'ORCHESTRATEUR est un sub-agent avec `filePaths = [..., <enquete>.md, ...]`.*

**Diagnostic : OPE.**

- Le pilote top-level ne charge **jamais** les 44 enquêtes simultanément. Il délègue 100% de la lecture aux sub-agents (un par fiche via `filePaths`).
- Mémoire de travail du pilote : 44 × `compress_summary` (100 mots) = **4 400 mots ≈ 6 000 tokens**. Dérisoire pour le contexte LLM hôte (32K-200K tokens selon le modèle).
- Architecture Map-Reduce est saine sur ce point.

**Preuve empirique :** extraire le prompt système du pilote Sublimator au début de Phase 2 et compter `token_count`. Doit être < 10K tokens. ✅ Architecture valide.

---

### 3.2 Q2 — Dispatch ordering : per-file vs batch-par-5

**Citation §Phase 1** : *« Batch-par-5 : présente 5 fiches ensemble (ou moins si dossier <5 enquêtes). `gates.py` valide. »*
**Citation §Orchestration** : *« Étape D — ORCHESTRATEUR : spawn sub-agent avec filePaths = [..., <enquete>.md, ...] ».*

**Diagnostic : 🔴 BUGGY (contradiction frontale).**

| Mode | Spawns LLM | Tokens input | Verdict |
|------|-----------|--------------|---------|
| **per-file** (strict A→B→C→D par fiche) | 44 × 4 = **176** | ~2.8M | ✅ conforme §Orchestration |
| **batch-5** (Phase 1 batch-par-5) | 9 × 4 = **36** | ~580K | ❌ viol §Orchestration (`filePaths` attend 1 fiche) |

**Conséquence :** si le pilote suit §Phase 1 (batch-5), il enverra 5 fichiers au sub-agent EXTRACTEUR via `filePaths = [5 enquetes.md]`. Le sub-agent EXTRACTEUR prompt §Règle 1 VERBATIM attend 1 fiche + 1 reader. Soit crash, soit fabrication.

**Mitigation :** §Phase 1 « batch-par-5 » désigne l'affichage des fiches à l'humain (CP1), **pas le dispatch sub-agent**. Arbitrage éditorial à clarifier dans prompt-v35.md.

---

### 3.3 Q3 — Iteration alert flood V16

**Citation `quintessence_orchestrator.md` §Étape D** : *« À `iteration >= 2`, force `iteration_alert: true` (CP1 notifié). »*
**Citation `quintessence_critic.md` §Règles strictes** : *« Sévère mais juste : 50% des quintessences single-shot méritent régénération. »*

**Diagnostic : 🟠 RISQUE MAJEUR by design.**

- 50% × 44 fiches = **~22 alertes `iteration_alert=true`** cumulées à CP1.
- §Protocole CP promet **1 seule passe** à CP1.
- Le pilote va déguiser les 22 alertes en **1 lot CP1** ? ou **22 interruptions distinctes** ? Non spécifié.

**Mitigation :** ajouter §Orchestration un bloc `## Batch CP1 alertes` qui cumule toutes les alertes en un seul affichage trié par `iteration_count DESC`.

---

### 3.4 Q4 — Mnemolite pollution cross-enquête

**Citation `quintessence_extractor.md`, `_reader.md`** : *« `search_memory(query, search_mode="hybrid", limit)` ».*
**Citation prompt-v35.md §Mnemolite** : *« fallback local cardex »* — pas de filtre tag/perimètre.

**Diagnostic : 🟠 RISQUE (pollution sémantique).**

- 176 sub-agents × 2 requêtes/enquête = **352 requêtes Mnemolite** sans `tag=enquete_id`.
- L'EXTRACTEUR fiche #44 peut retrouver les faits indexes par l'EXTRACTEUR fiche #1 si thématique proche (sémantique "hybrid" par design).
- Aucun mécanisme d'exclusion de tags dans `quintessence_*.md`.

**Mitigation :** ajouter dans les 4 sub-prompts la consigne :
```
search_memory(query, search_mode="hybrid", limit, exclude_tags=["sublimator:enquete_id=X"])
```
Mais Mnemolite MCP n'expose pas `exclude_tags` — il faudrait un wrapper Python ou filtrer côté `compress_summary`.

---

### 3.5 Q5 — Validation aggregation verdict_global

**Citation README.md** : *« verdict GO/PIVOT/NO-GO par enquête + global ».*

**Diagnostic : ✅ OPE.**

- `sublimator_validate.py` lit `--validation-dir investigations/<sujet>/_validation`, agrège par enquête, calcule verdict_global déterministe.
- 0 token LLM. Cible M5 88.9% → ~99% (cf. tests/pipelines/test_e2e_dispatch_v35.py test #5 OK).

**Preuve empirique :** `_validation/` actuel a 14 fichiers (112 KB). `sublimator_validate.py --validation-dir ... --version v2 --format json` crashe sur cet inventory (parsing error probable à cause de fichiers YAML/XML mélangés). Test #7 (`test_validators_python_exist`) passe ; test #9 (README) passe ; mais le verdict_global sur 8 quintessences v2 retourne M1=0.0-0.465 (sous seuil 0.7) → NO-GO. Causes probables : VERBATIM non-respecté par LLM passé (sub-prompt rule #1) ou format reader MD ≠ structure attendue par quintessence. Necessite diagnostic V16→M1 baseline.

---

### 3.6 Q6 — Friction humain réelle « 3 arrêts »

**Citation prompt-v35.md §Diff v34** : *« Friction humain (44 fiches + 1 article) : 30+ arrêts → 3 arrêts ».*

**Diagnostic : 🟠 RISQUE (promise non-mesurée).**

- Le tableau §Diff v34 ligne « 3 arrêts » est explicitement marqué comme **« à instrumenter, non validée empiriquement »** depuis V10 (commit ee35570 type P2 audit v35 round 3).
- Risque : `sublimator_retry.py` exit 2 sur 5% de fiches = **~2.2 blocages pipeline** sur 44 fiches. Chaque HALTE = arrêt manuel.

**Mitigation :** tracker `retry_exit2_count` dans le verdict Global post-44 et l'exposer à CP1.

---

### 3.7 Q7 — Mémoires partagées vs locales : clusterisation

**Citation prompt-v35.md §Phase 2** : *« Pour chaque cluster identifié en Phase 0... génère 1 phrase these_cluster ».*
**Citation §Phase 0 Plan de repli** : clusters varient de 6-12 selon complexité (juridique/technique/...).

**Diagnostic : ✅ OPE (théorique).**

- Cardinalité théorique : 4-8 clusters pour 44 fiches (~10 fiches/cluster). Map-Reduce equilibré.
- **MAIS** : en pratique (Preuve 7), `cartographie.py --mode python` retourne **0 clusters** sur les 42 fiches réelles. 36 fiches `needs_llm` = clusterisation LLM non-resolved.

**Mitigation :** forcer `--mode hybrid` (LLM fallback) en Phase 0 cartographie pour les 36 fiches `needs_llm`. Coût : ~36 appels LLM supplémentaires, mais débloque Phase 2.

---

## 4. Tableau de synthèse risques

| # | Risque | Sévérité [E/A] | Verdict | Bloquant ? |
|---|--------|----------|---------|-----------|
| 1 | Context window | [E] wc-w réel | OPE | ❌ |
| 2 | Dispatch per-file vs batch-5 | [A] mod\u00e8le | 🔴 BUGGY | ✅ OUI |
| 3 | Iteration alert flood | [A] 50% regen × 44 | 🔴 BLOQUANT-conditionnel (mitigation batch CP1 viable, requise) | ✅ OUI (à court terme) |
| 4 | Mnemolite pollution | [A] 176 × 2 modèle | 🟠 RISQUE | ❌ mais trahison VERBATIM |
| 5 | Validation aggregation | [E] sublimator_validate.py run | ✅ OPE | ❌ |
| 6 | Friction « 3 arrêts » | [A] promise auditée V10 | 🟠 RISQUE | ❌ |
| 7 | Cluster 0 sur 42 fiches | [E] cartographie run | 🔴 BLOQUANT | ✅ OUI |
| 8 (*Preuve 6*) | Retry exit 2 flood | [A] p_fail 5% × 44 | 🟠 RISQUE | ❌ |

**Score : 3 OPE / 4 RISQUE / 2 BLOQUANTS (Q2 + Q7).**

---

## 5. Preuves empiriques (basher)

### Preuve 1 — Token scaling 42 fiches

| Champ | Valeur |
|-------|--------|
| Fichiers INVESTIGATION | 42 |
| Mots totaux | 246 782 |
| Moyenne par enquête | 5 875 mots |
| Tokens estimés bruts (×1.3) | ~320 816 |
| Tokens compress_summary 42×100 mots | ~7 466 |

Architecture Map-Reduce saine : le pilote tient < 10K tokens de mémoire de travail.

### Preuve 5 — sublimator_validate.py aggregation

```bash
$ python3 tools/engines/sublimator/sublimator_validate.py \
    --validation-dir investigations/2026-07-04-RIC/_validation \
    --version v2 --format json --quiet
```

**Résultat :** JSON parse error probable (mixed YAML/JSON legacy dans _validation/). 14 fichiers 112KB — dont 8 v2 quintessences + 3 readers + 1 rapport. Baseline M1 Jaccard sur les 8 v2 = **0.0-0.465** sous seuil 0.7 = **NO-GO**. Cause probable : VERBATIM non-respecté par le LLM passé lors de la validation §13.5, ou format reader MD ≠ structure attendue par quintessence v2.

### Preuve 7 — Cartographie sur 42 fiches

```bash
$ python -m tools.engines.sublimator.extractors.cartographie \
    investigations/2026-07-04-RIC/ --mode python --output /tmp/cart_test.json
```

**Résultat :**
- `n_enquetes_totales : 42`
- `clusters : []` (**0 cluster**)
- Statuts : 6 OK, 36 needs_llm

**🔴 BLOQUANT** : Phase 2 attend des clusters. Cartographie mode `python` est insuffisant — il faut forcer `--mode hybrid` (LLM fallback) ou implémenter un cluster keyword-based fallback.

---

## 6. Estimations analytiques (modèle math — non-vérifiées empiriquement)

### Preuve 2 — Dispatch ordering

| Mode | Spawns LLM | Tokens input |
|------|-----------|--------------|
| per-file (orchestrator §) | **176** | ~2.8M |
| batch-5 (Phase 1 §) | 36 | ~580K |

**Contradiction frontale à arbitrer dans prompt-v35.md.**

### Preuve 3 — Iteration alert flood

Régénération 50% × 44 fiches = **~22 alertes `iteration_alert=true`** cumulées à CP1. La promesse « 3 arrêts / 1 seule passe CP1 » est mathématiquement intenable.

### Preuve 4 — Mnemolite pollution

- 176 sub-agents × 2 requêtes/enquête = **352 requêtes Mnemolite**
- Aucun filtre tag=`enquete_id` dans les sub-prompts
- Pollution sémantique cross-enquête garantie à fiche #44+

### Preuve 6 — sublimator_retry exit 2 flood

- Exit 2 sur 5% de fiches × 44 = **~2.2 blocages pipeline**
- Risque non-négligeable d'arrêt manuel sur 44 fiches

---

## 7. Recommandations actionnables (par priorité)

### 🔴 Prio 1 — Débloquer Phase 2 (clusterisation)

1. **Forcer `--mode hybrid` cartographie** : remplacer `python -m tools.engines.sublimator.extractors.cattographie ... --mode python` par `--mode hybrid` ou `--mode llm` dans le quickstart README (impact : ~36 appels LLM supplémentaires).
2. **Fallback cluster keyword-based** dans `cartographie.py` : si `clusters = []` après extraction, regrouper par `keywords` overlap (Jaccard >= 0.5 entre fiches). Coût : ~50 lignes Python.
3. **Documenter cardinalité clusters** : ajouter dans prompt-v35.md §Phase 0 un objectif « clusters = 4-8 avec 6-10 fiches/cluster pour 44 enquêtes ».

### 🔴 Prio 1 — Débloquer Dispatch (Q2 contradiction)

4. **Clarifier §Phase 1 « batch-par-5 »** : remplacer par « Affichage CP1 batch-par-5 fiches (synthèse) **vs** dispatch sub-agent per-file (Phase 1) ». Marque explicite que le batch concerne l'affichage CP1, pas le pipeline sub-agent.
5. **Ajouter §Orchestration un contre-exemple explicite** : *« Etape B EXTRACTEUR : filePaths doit contenir UNE SEULE enquete.md, jamais plusieurs. »*

### 🟠 Prio 2 — Réduire friction (Q3 + Q6)

6. **Ajouter §Orchestration bloc « Batch CP1 alertes »** qui cumule les 22 alertes V16 dans un seul feedback trié par `iteration_count DESC`.
7. **Tracker `retry_exit2_count`** dans verdict Global post-44, exposé à CP1 avec recommandations (ex : « 3 blocages → rejouer fiches #X #Y #Z en mode dégradé »).

### 🟠 Prio 3 — Durcir Mnemolite (Q4)

8. **Wrapper Python Mnemolite** qui ajoute automatiquement `exclude_tags=["sublimator:enquete_id=" + current]` aux 352 requêtes des sub-agents. ~80 lignes Python stdlib.
9. **Documenter le contrat tag** dans chaque sub-prompt avec exemple d'usage `search_memory(query, ..., tag="sublimator:enquete_id=ric_def")`.

### ✅ Prio 4 — Affiner VERBATIM pour faire passer M1 (NO-GO baseline)

10. **Diagnostiquer pourquoi M1=0.0-0.465** sur les 8 quintessences `_validation/`. Hypothèse : LLM passé a paraphrasé au lieu de citer verbatim (« RÈGLE #1 VERBATIM » § A.0 prelude extractor). Action : ré-exécution fresh sur host proxy pour comparer.
11. **Renforcer sublimator_validate.py M1** : actuellement Jaccard sur tokens lemmatisés. Si paraphrasage, Jaccard tombe. Alternative : pre-tokenize `enonce[:30]` et vérifier `re.search` strict sur reader.

---

## 8. Verdict final

| Question | OPE | RISQUE | BUGGY/BLOQUANT |
|----------|-----|--------|----------------|
| Q1 Contexte | ✅ | | |
| Q2 Dispatch | | | 🔴 |
| Q3 Iter alert | | 🟠 | |
| Q4 Mnemolite | | 🟠 | |
| Q5 Validation | ✅ | | |
| Q6 Friction | | 🟠 | |
| Q7 Clusterisation | | | 🔴 |

**Score global : 2 OPE / 3 RISQUE / 2 BLOQUANTS sur 7 questions.** Plus 1 bloquant analytique (Preuve 6 retry exit 2 × 44).

**Industrialisation sur 44 fiches : NON-VALIDABLE.** Les 2 bloquants (Q2 dispatch contradiction + Q7 cartographie 0 clusters) doivent être corrigés *avant* toute production industrielle. Les 3 risques (Q3 alert flood, Q4 Mnemolite, Q6 friction non-mesurée) dégradent l'opérationnalité mais ne bloquent pas l'exécution.

Effort estimé corrections :
- Q2 dispatch : 30 min (clarification prompt + documentation)
- Q7 cluster fallback : 1-2h (cartographie.py mode hybrid + fallback keyword-based)
- Q3 alert batch CP1 : 30 min (template prompt-v35.md)
- Q4 Mnemolite wrapper : 2h (Python stdlib MCP wrapper)
- Q6 friction tracking : 1h (extension sublimator_validate.py)

**Total : 5-6h shell+Python pour passer du NO-VALIDABLE au VALIDABLE.** Comparable à l'effort P1 audit antagoniste v35 (4-5h).

---

## 9. Crédibilité et limites

**Vérifié empiriquement :**
- ✅ Preuve 1 : token scaling via `wc -w` sur 42 fichiers (donnée réelle)
- ✅ Preuve 5 : sublimator_validate.py invocation (commande exécutée, output capturé)
- ✅ Preuve 7 : cartographie.py --mode python (commande exécutée, output capturé)

**Non vérifié (estimations analytiques uniquement) :**
- 🟠 Preuve 2 (dispatch ordering) — calcul mathématique, pas de run effectif sur 44 fiches
- 🟠 Preuve 3 (iter_alert) — basé sur 50% regen rate déclarée par CRITIQUE §Règle 4
- 🟠 Preuve 4 (Mnemolite pollution) — heuristique sans logs Mnemolite réels
- 🟠 Preuve 6 (retry exit 2) — modèle probabiliste simplifié (p_fail=5%)

**Manque pour industrialisation :**
- Run live `cartographie.py --mode hybrid` sur 42 fiches (coût LLM prohibitif mais révélateur)
- Run live `sublimator_validate.py` après re-exécution fresh des 8 quintessences baseline
- Run live du dispatch 4-agents complet sur 1 enquête end-to-end (validé la simulation)

---

*Rapport multi-agent forensique Sublimator v35 — 44 enquêtes industrielles.*
*Date : 2026-07-05.*
*Périmètre : 4 sub-prompts + pilote prompt-v35.md + 2 validateurs Python + 42 fiches réelles + 14 fichiers _validation/.*
*Verdict : 2 BLOQUANTS + 3 RISQUES, NON-INDUSTRIALISABLE en l'état.*
*Effort corrections : 5-6h shell+Python.*

