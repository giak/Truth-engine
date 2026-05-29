# Truth Engine

**Système d'analyse cognitive et de production éditoriale.**

---

## Navigation

Le point d'entrée unique est **`docs/specs/PIPELINE_ARTICLE.md`** — il décrit tout le pipeline : investigation (Truth Engine v2) → rédaction (SUBLIMATOR) → lint → publication Substack.

### Dossiers actifs

| Dossier | Contenu |
|---------|--------|
| `truth-engine-v2/` | KERNEL v2 — protocole d'investigation (30+ fichiers) |
| `investigations/` | 100+ enquêtes et rapports |
| `articles/` | Articles finaux publiés |
| `investigations/` | Audits déplacés dans investigations/ |
| `tools/` | SUBLIMATOR, lint, scripts |
| `substack-online/` | Posts exportés (86), CSV, emails |
| `docs/` | Spécifications, guides, VISION |
| `docs/specs/` | Spécifications, architecture, audits système |
| `articles/misc/` | Documents sources (PDF) |
| `config/` | Configurations IDE |
| `archive/` | Anciennes versions (KERNEL v1, fichiers morts) |

---

## Quick Start

```bash
# Lancer une investigation
→ truth-engine-v2/KERNEL.md

# Rédiger un article
→ tools/engines/SUBLIMATOR_v28.0.md

# Valider un article
./tools/scripts/lint-article.sh articles/xxx.md

# Comprendre le pipeline complet
→ docs/specs/PIPELINE_ARTICLE.md
```

---

## Licence

À définir.
