# 📁 Structure du Projet Truth Engine

## Organisation Réelle

```
truth-engine/
├── KERNEL.md                    # Point d'entrée — CHARGÉ EN PREMIER
├── README.md                     # Dashboard central
├── DISCLAIMER.md                 # Avertissements légaux
├── kb/                          # KNOWLEDGE BASE
├── docs/                        # DOCUMENTATION
├── outputs/                     # PRODUCTIONS
├── tools/                       # INFRASTRUCTURE
├── investigations/             # Investigations récentes
├── enquetes/                   # Enquêtes
├── logs/                       # Logs
└── archive/                    # Archives
```

---

## 🔧 KB/ - Knowledge Base

Le système — **jamais de contenu généré**.

| Dossier | Contenu |
|---------|---------|
| `kb/dsl/` | DSL definitions (COGNITIVE_DSL.md, COGNITIVE_DSL_CORE.md) |
| `kb/patterns/` | 19 clusters (CLUSTER_*.md) |
| `kb/protocols/` | Protocoles (INVESTIGATION.md, INVESTIGATION_TREE.md...) |

---

## 📄 DOCS/ - Documentation

| Dossier | Contenu |
|---------|---------|
| `docs/VISION.md` | Philosophie et principes |
| `docs/STRUCTURE.md` | Ce fichier |
| `docs/user/` | USER_GUIDE.md, PHILOSOPHY.md |
| `docs/specs/` | PRD.md, SCL_NOTATION.md |
| `docs/audits/` | Rapports d'audit |
| `docs/plans/` | Roadmaps et designs |

---

## 📤 OUTPUTS/ - Productions

Tout ce qui est **généré par Truth Engine**.

| Dossier | Contenu |
|---------|---------|
| `outputs/investigations/` | Rapports complets |
| `outputs/articles/` | Articles Substack |
| `outputs/social/` | Tweets, threads |
| `outputs/simulations/` | Simulations APEX |
| `outputs/logs/` | Logs historiques |
| `outputs/results/` | Résultats de tests |

---

## 🛠️ TOOLS/ - Infrastructure

| Dossier | Contenu |
|---------|---------|
| `tools/docs/` | Documentation technique |
| `tools/tests/` | Tests et validations |
| `tools/prompts/` | Prompts et templates |
| `tools/scripts/` | Scripts utilitaires |

---

## 📁 ROOT - Fichiers

| Fichier | Description |
|---------|-------------|
| `KERNEL.md` | Cœur opérationnel — point d'entrée |
| `README.md` | Dashboard central |
| `DISCLAIMER.md` | Avertissements légaux |
| `kb/` | Knowledge Base |
| `investigations/` | Investigations récentes |
| `enquetes/` | Enquêtes |
| `logs/` | Logs |

---

## 🗄️ ARCHIVE/

| Dossier | Contenu |
|---------|---------|
| `archive/backups/` | Sauvegardes |
| `archive/projects/` | Projets terminés |
| `archive/kb_archive_old/` | Ancienne KB |

---

## 📋 Règles

1. **KERNEL.md** → toujours à la racine, point d'entrée
2. **kb/** → système uniquement — jamais de contenu généré
3. **docs/** → philosophie, specs, audits
4. **outputs/** → productions générées
5. **investigations/** → investigations récentes
6. **tools/** → infrastructure

---

*Structure mise à jour le 25 février 2026*
