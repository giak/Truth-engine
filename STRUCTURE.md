# 📁 Structure du Projet Truth Engine

## Organisation

Ce projet est organisé selon 3 piliers distincts :

```
truth-engine/
├── 📦 core/              # SYSTÈME - Le DSL et les patterns
├── 📤 outputs/           # PRODUCTIONS - Résultats des investigations
├── 🛠️ tools/             # INFRASTRUCTURE - Docs, tests, scripts
├── 🗄️ archive/           # ARCHIVES - Historique et backups
└── 📄 Fichiers racine    # Essentiels uniquement
```

---

## 🔧 CORE/ - Le Système

Le cœur du Truth Engine - **ne doit jamais contenir de contenu généré**.

| Dossier | Contenu |
|---------|---------|
| `core/KERNEL.md` | Cœur du DSL v11.0 - point d'entrée |
| `core/patterns/` | 19 clusters de patterns cognitifs (CLUSTER_*.md) |
| `core/protocols/` | Protocoles d'investigation (INVESTIGATION.md, OUTPUT_TEMPLATE.md...) |
| `core/dsl/` | Fichiers DSL (COGNITIVE_DSL.md, MACROS.md, PATTERNS.md...) |

---

## 📤 OUTPUTS/ - Les Productions

Tout ce qui est **généré par l'utilisation du KERNEL**.

| Dossier | Contenu |
|---------|---------|
| `outputs/investigations/` | Rapports d'investigation par date/sujet |
| `outputs/articles/` | Articles Substack publiés |
| `outputs/social/` | Tweets, threads, contenu réseaux sociaux |
| `outputs/logs/` | Logs historiques des investigations |
| `outputs/results/` | Résultats de tests et simulations |
| `outputs/simulations/` | Simulations APEX et autres |

---

## 🛠️ TOOLS/ - Infrastructure

Documentation, tests et scripts.

| Dossier | Contenu |
|---------|---------|
| `tools/docs/user/` | Documentation utilisateur (USER_GUIDE.md, PHILOSOPHY.md) |
| `tools/docs/dev/` | Documentation technique (MCP, MnemoLite...) |
| `tools/docs/specs/` | Spécifications (TAD.md, PRD.md, VISION.md) |
| `tools/docs/audits/` | Audits et analyses du système |
| `tools/docs/article-plans/` | Plans et stratégies d'articles |
| `tools/docs/plans/` | Roadmap et designs futurs |
| `tools/tests/` | Tests unitaires et d'intégration |
| `tools/scripts/` | Scripts utilitaires |
| `tools/prompts/` | Prompts et templates |

---

## 🗄️ ARCHIVE/ - Historique

Contenu historique et backups.

| Dossier | Contenu |
|---------|---------|
| `archive/backups/` | Sauvegardes anciennes |
| `archive/investigations/` | Vieilles investigations |
| `archive/projects/` | Projets ponctuels terminés |
| `archive/version-docs/` | Historique des versions |

---

## 📄 Racine - Fichiers Essentiels

Uniquement 5 fichiers (+ symlinks) :

| Fichier | Description |
|---------|-------------|
| `README.md` | Documentation principale |
| `DISCLAIMER.md` | Avertissements légaux |
| `KERNEL.md` | → symlink vers `core/KERNEL.md` |
| `package.json` | Dépendances Node.js |
| `package-lock.json` | Lock des dépendances |

---

## 🎯 Règles d'Or

1. **Racine** : Max 5 fichiers essentiels
2. **core/** : Système uniquement - jamais de contenu généré
3. **outputs/** : Tout contenu produit par le KERNEL
4. **tools/** : Infrastructure uniquement
5. **archive/** : Contenu historique, pas de références actives

---

*Structure créée le 30 janvier 2026*
