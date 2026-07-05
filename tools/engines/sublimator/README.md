# Sublimator — README

> Pipeline d'orchestration qui transforme N enquêtes journalistiques en 1 article
> publiable, avec traçabilité forensique.
>
> **Versions** : prompt v35 (top-level) / schéma quintessence v36 (§13.3.2) /
> protocoles §13.x. Voir `AUDIT_ANTAGONISTE_v35_2026-07-05.md` pour la dette
> technique résiduelle et les commits de fix.

## Quickstart

```bash
# 2. (Validation algorithmique Python retirée 2026-07-06 — voir prompt-v35.md
#     Note d'architecture. La validation est désormais portée par le sub-agent
#     CRITIQUE invoqué via filePaths, cf. SPECS v36 §13.5.2.)
```

> **Note CLI** : le pipeline `python` (sans `3`) ne fonctionne PAS sur les systemes Linux recents (Debian 12+, Ubuntu 24.04+) qui ne fournissent que `python3`. Utilisez systematiquement `python3`.

## Architecture

```
                  [Phase 1 Extraction LLM par-enquete] (cartographie.json SUPPRIMÉE 2026-07-05 — overengineering)
                              |
                              v
            [Phase 1 Extraction LLM par-enquete]
              |                       |
              v                       v
  [Sub-agent 1 LECTEUR §13.3.1]   reader.md
  [Sub-agent 2 EXTRACTEUR §13.3.2]  quintessence.json
  [Sub-agent 3 CRITIQUE §13.3.3*]   critique.json     (* optionnel §13.5)
              |
              v
  [Sub-agent 4 ORCHESTRATEUR §13.3.4]  coordonne A->B->C->D, max 3 iter,
                                        materialise iteration_count (V16)
                              |
                              v
              [Phase 1.5 Compression 100 mots]
                              |
                              v
              [Phase 2 Synthese Map-Reduce]
                    |              |
                    v              v
          synthese_clusters.json  synthese.json (3-5 theses cardinales)
                              |
                              v
              [Phase 2.5 rapport_synthese.md]
              [Phase 2.6 plan_article.md]
                              |
                              v
              [Phase 3 Article 3000-5000 mots (CP2 humain)]
```

3 checkpoints humains : CP1 (Phase 1.5 thèse / Phase 2 thèse fil rouge),
CP2 (Phase 3 article fini). Entre les CP, les validateurs Python valident H0-H7
automatiquement. *(L'ancien CP0 cartographie a été supprimé 2026-07-05 ; il reste 2 checkpoints actifs.)*

## Workflow (8 phases)

  optionnel (`search_mode="hybrid"` obligatoire depuis V11). Les fiches LLM par-enquête sont stockées dans `_quintessence/`.
- **Phase 1.5** : Compression en 100 mots (champ `compress_summary` dans la quintessence).
- **Phase 1** : Extraction LLM par-enquête, 4 sub-agents orchestrés via
  `filePaths` (voir ## Orchestration §prompt-v35).
- **Phase 1.5** : Compression en 100 mots (`compress_summary` dans la
  quintessence, inclut `iteration_count` V16).
- **Phase 2** : Map-Reduce par cluster puis synthèse globale (3-5 thèses
  cardinales max, vs 15 en v34). CP1.
- **Phase 2.5** : Rapport de synthèse (5 sections).
- **Phase 2.6** : Plan d'article (3-5 sections).
- **Phase 3** : Article 3000-5000 mots selon 8 LOIS. CP2.

## Auto-Audit (sub-agent CRITIQUE)

> **Note 2026-07-06** : les validateurs déterministes Python ont été retirés (cf. prompt-v35.md Note d'architecture). La conformité est désormais validée par :
>
> 1. Sub-agent LLM **CRITIQUE** (cf. `prompts/quintessence_critic.md`) invoqué via `filePaths = [<quint>.json, <enquete>.md]` après chaque production de quintessence.
> 2. Sub-agent LLM **CRITIQUE** Format-Aware (cf. SPECS v37 v2 §6) pour les compress.md.
> 3. Auto-audit antagoniste du pilote (Phase 3 L8).
> 4. Checklist manuelle du pilote aux checkpoints CP1/CP2.


## Prompts (source unique de vérité)

| Fichier | Rôle | Chargeable via |
|---------|------|----------------|
| `prompt-v35.md` | Pilote Sublimator top-level | standalone, premier message |
| `prompts/quintessence_reader.md` | Sub-agent 1 LECTEUR §13.3.1 | `filePaths` au dispatch |
| `prompts/quintessence_extractor.md` | Sub-agent 2 EXTRACTEUR §13.3.2 | `filePaths` (charte v2 VERBATIM) |
| `prompts/quintessence_critic.md` | Sub-agent 3 CRITIQUE §13.3.3 | `filePaths` (optionnel §13.5) |
| `prompts/quintessence_orchestrator.md` | Sub-agent 4 ORCHESTRATEUR §13.3.4 | `filePaths` (boucle max 3 iter) |
| `prompts/validation_3enquetes.md` | Protocole §13.5 ré-exécution | rejouable tout hôte LLM |

**Contrat Mnemolite (5-place redundancy propage V12/V13)** :
`get_system_snapshot` au démarrage (HALTE si DOWN, sans cardex fallback depuis suppression Phase 0 2026-07-05) + `search_memory(..., search_mode="hybrid", ...)` TOUJOURS (jamais sans le paramètre). Présent dans `prompt-v35.md` + les 4 sub-prompts.

## Métriques (SPECS §13.5.2)

| # | Métrique | Cible GO | Cible NO-GO |
|---|----------|----------|-------------|
| M1 | Jaccard `these_centrale` | ≥ 0.7 | < 0.5 |
| M2 | Intersection F## | ≥ 0.6 | < 0.4 |
| M3 | Hallucination F## (re.search strict) | < 5 % | > 15 % |
| M4 | Hallucination impact (chiffres sourcés) | < 5 % | > 15 % |
| M5 | JSON parse | 100 % | < 95 % |
| M6 | Volume tokens | ≤ 50 K/enquête | > 100 K |
| M7 | Latence | < 10 min/enquête | > 20 min |
| M8 | Score critic | ≥ 7 | < 5 |

Critères globales : M1 ≥ 0.7 ET ≥ 6/8 cibles GO + M3 < 5 % + M4 < 5 % = **GO**.
M1 < 0.5 OU > 2/8 cibles NO-GO OU M3 > 15 % OU M4 > 15 % = **NO-GO**.

## Dépannage

### Mnemolite DOWN

1. Vérifier `get_system_snapshot` : si `status: DOWN`, **HALTE et signaler**.
2. Si `cartographie.json` Phase 0 existe → mode dégradé cardex local, les
   quintessences sont conservées localement.
3. Si pas de cardex → arrêt explicite, ne produire aucun fichier.

### Naming `_validation/` inconsistent

Convention unifiée : underscore (pas hyphen), drop suffix.
`sublimator_validate.py` matche par préfixe exact.

### Hallucination M3/M4 (> 15 %)

1. Vérifier règle VERBATIM côté `quintessence_extractor.md` §A.0.
2. Forcer `iteration_count` ↑ (max 3) via `quintessence_orchestrator.md` §D.
3. À `iteration_count >= 2`, `iteration_alert: true` notifié à CP1.

### Typos connus (déjà corrigés)

- `spanw` → `spawn` (commit `a7adbd7`).
- `défini défini` (×4) → `défini` (commit `a7adbd7`).
- `## Version v2 de EXTRACTEUR` (intact dans extracteur, label historique).

## Tests

- *(Section `tests/extractors/` supprimée 2026-07-05 : extractors/cartographie.py retiré comme overengineering.)*
  `test_gates_json.py`, `test_gates_hardening.py`,
  `test_head_check_hardening.py`.
- `tests/pipelines/test_e2e_dispatch_v35.py` : cohérence statique du dispatch
  Sublimator v35 (résout audit V14).

## Audit / dette technique

- `AUDIT_ANTAGONISTE_v35_2026-07-05.md` : 16 contradictions initiales (9 P1,
  7 P2). État courant : P1 résolues en commits `a7adbd7` / `64389da` /
  `405e00b`. P2 résolues en commit `bbcb71b`. 16/16.
- `RAPPORT_MULTI_AGENT_44_ENQUETES_v35_2026-07-05.md` : audit multi-agent
  44 enquetes industrielles. 7 questions + 7 preuves (3 empiriques + 4
  analytiques). Verdict : 2 BLOQUANTS (Q2 dispatch contradiction + Q7
  extractors 0 clusters) + 3 RISQUES (Q3 alert flood, Q4 Mnemolite
  pollution, Q6 friction). Industrialisation NON-VALIDABLE en l'état.
  Effort corrections : 5-6h shell+Python.

## Crédits

Conception initiale : `prompt-v34.md`. Refonte v35 : introduction validateurs
Python + extraction 4 sub-prompts séparés + section ## Orchestration Sublimator.
Diff vs v34 : tableau §Diff de `prompt-v35.md`.
