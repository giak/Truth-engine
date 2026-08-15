# Truth Engine

Système d'analyse cognitive et de production éditoriale : enquêtes forensiques sourcées → articles publiables, avec registre de faits vérifiés et traçabilité des sources.

## Pipeline

1. **Investigation** : `truth-engine-v2/KERNEL.md` (v2.8) produit une enquête avec faits atomiques classés (FACT / EVIDENCE / INFERENCE) et sources ancrées.
2. **Vérification des faits** : `truth-engine-v2/protocol/FACT_VERIFICATION.md` (échelle L0→L4, gate EPI) + `tools/verify_facts.py` (HEAD-check anti-SSRF, exigence de ≥ 2 familles de provenance indépendantes).
3. **Rédaction** : SUBLIMATOR transforme N enquêtes en 1 article (Phase 1 → 2 → 2.5 → 3).
4. **Lint** : `tools/scripts/lint-article.sh`.
5. **Publication** : Substack (`substack-online/`).

## SUBLIMATOR (v36-v38)

| Phase | Prompt | Rôle |
|-------|--------|------|
| 1 | `tools/engines/sublimator/prompt-v36.md` | Extraction quintessence par enquête (4 sous-agents) |
| 2 | `tools/engines/sublimator/prompt-v37_phase2.md` | Synthèse par cluster (3-5 thèses cardinales) |
| 2.5 | `tools/engines/sublimator/prompt-phase2_5_raisonnement_narratif.md` | Raisonnement narratif |
| 3 | `tools/engines/sublimator/prompt-v38_phase3.md` | Rédaction d'article Substack publiable |

`prompt-v35.md` est obsolète (remplacé par v36).

## Mnemolite

Base de connaissance vectorielle (RAG) servie via MCP (voir `docs/MNEMOLITE_STATUS.md` et `~/.agents/skills/mnemolite-mem-first/`). Le registre des faits utilise `status:CONFIRME` + `verifie-YYYY-MM-DD` + `source:<hash>`. Recherche sémantique : `search_memory(..., search_mode="hybrid")`. Synchronisation : `tools/scripts/sync-mnemolite.sh`.

## Dossiers actifs

| Dossier | Contenu |
|---------|---------|
| `truth-engine-v2/` | KERNEL v2.8 + protocoles (FACT_VERIFICATION, INVESTIGATION, UPDATE, PERSO_FRESQUE) + clusters/définitions/forensic/search |
| `investigations/` | Enquêtes, rapports, corpus |
| `articles/` | Articles finaux |
| `tools/` | SUBLIMATOR (`engines/sublimator/`), scripts (lint, sync-mnemolite, verify_facts), audits |
| `substack-online/` | Posts exportés et index |
| `outputs/` | Sorties intermédiaires (audits, JSON, synthèses) |
| `docs/` | `AGENT.md`, `MNEMOLITE_STATUS.md` |
| `config/` | Configurations IDE |
| `archive/` | Anciennes versions |

## Quick Start

```bash
# Investigation
→ truth-engine-v2/KERNEL.md

# Vérifier le registre de faits
python3 tools/verify_facts.py --help

# Surveiller les URLs mortes du registre
python3 tools/monitor_urls.py --help

# Rédaction (Phase 1 → 2 → 2.5 → 3)
→ tools/engines/sublimator/prompt-v36.md
→ tools/engines/sublimator/prompt-v37_phase2.md
→ tools/engines/sublimator/prompt-phase2_5_raisonnement_narratif.md
→ tools/engines/sublimator/prompt-v38_phase3.md

# Lint d'un article
./tools/scripts/lint-article.sh articles/xxx.md

# Tests
pytest tests/
```

## Licence

À définir.
