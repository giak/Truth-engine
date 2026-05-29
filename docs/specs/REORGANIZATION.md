# REORGANIZATION — Spécification de réorganisation du monorepo

**But :** Passer de 30 entrées illisibles à la racine à une arborescence navigable, sans casser le pipeline d'investigation/rédaction/publication.

**Version :** 1.0  
**Date :** 2026-05-29  
**Statut :** Spécification — aucune modification appliquée  
**Complète :** docs/specs/PIPELINE_ARTICLE.md (guide de navigation)

---

> **🔰 PAR OÙ COMMENCER**
> 
> | Tu veux… | Lis… |
> |---|---|
> | Comprendre le problème | §0 — Diagnostic |
> | Voir l'état cible | §1 — Cibles |
> | Appliquer le nettoyage minimal | §2 — Plan SAFE |
> | Appliquer la réorganisation complète | §3 — Plan B (breaks refs) |
> | Utiliser les scripts d'automatisation | §4 — Superpowers |
> | Vérifier que tout marche | §5 — Validation |
> | Annuler en cas de problème | §6 — Rollback |

---

## §0 — DIAGNOSTIC

### 0.1 État actuel de la racine

```
truth-engine/                              # ← toi, ici, maintenant
├── FICHIERS (11)
│   ├── AGENTS.md                 ✅ ACTIF — Règles projet IA
│   ├── README.md                 ✅ ACTIF — Mais cite kb/ (inexistant)
│   ├── LICENSE                   📄 Neutre
│   ├── DISCLAIMER.md             ❌ OBSOLÈTE — Projet v1, plus pertinent
│   ├── package.json              📄 Métadonnées (MCP server deps)
│   ├── package-lock.json         📄 Généré
│   ├── KERNEL_v1_DEPRECATED.md   ❌ OBSOLÈTE — Marqué déprécié mais à la racine
│   ├── novlang.md                🤷 ORPHELIN — Non référencé dans AGENTS.md ni PIPELINE
│   ├── CONVENTIONS_NOMMAGE.md    🤷 DOUBLON — Contenu absorbé par AGENTS.md §4.1
│   ├── knowledge.md              🤷 ORPHELIN — Non référencé nulle part
│   └── kilo.json                 ⚙️ Config IDE (kilo)
│
├── DOSSIERS (18)
│   ├── .vscode/                  ⚙️ Config IDE
│   ├── .claude/                  ⚙️ Config IDE
│   ├── .opencode/                ⚙️ Config IDE
│   ├── .agents/                  ⚙️ Config IDE
│   ├── .kilocode/                ⚙️ Config IDE
│   ├── .kilo/                    ⚙️ Config IDE
│   ├── .codebuff/                ⚙️ Config IDE
│   ├── truth-engine-v2/          ✅ ACTIF — KERNEL v2 engine
│   ├── investigations/           ✅ ACTIF — 100+ fichiers
│   ├── articles/                 ✅ ACTIF — ~10 articles finaux
│   ├── audits/                   ✅ ACTIF — ~15 audits
│   ├── tools/                    ✅ ACTIF — SUBLIMATOR, lint, tests
│   ├── substack-online/          ✅ ACTIF — 86 posts exportés
│   ├── docs/                     ✅ ACTIF — Documentation
│   ├── prompts/                  ✅ ACTIF — Prompts spécifiques
│   ├── sources/                  ✅ ACTIF — Documents sources
│   ├── twitter_export/           🤷 INACTIF — Export Twitter unique
│   └── archive/                  ✅ Archive — Anciennes versions
└── node_modules/                 (ignoré)
```

### 0.2 Problèmes identifiés

| # | Problème | Impact | Détail |
|---|----------|--------|--------|
| P1 | **11 fichiers à la racine** dont 5 inutiles | Navigation : 50% de bruit | DISCLAIMER.md, novlang.md, CONVENTIONS_NOMMAGE.md, knowledge.md, KERNEL_v1_DEPRECATED.md sont morts ou doublons |
| P2 | **7 dossiers de config IDE** à la racine | Navigation : 7 entrées parasites | .vscode, .claude, .opencode, .agents, .kilocode, .kilo, .codebuff |
| P3 | **1 dossier inactif** à la racine | Navigation : bruit | twitter_export/ — export unique, jamais référencé |
| P4 | **3 docs obsolètes** qui référencent des fichiers inexistants | Confusion | STRUCTURE.md (parle de kb/), USER_GUIDE.md (v8.0), README.md (cite kb/) |
| P5 | **100+ investigations à plat** sans filtre chronologique | Perte de vue d'ensemble | Les dossiers projet (2026-05-23_macron-systeme-complet/) sont bien organisés, mais les fichiers seuls (2026-05-27_*.md) sont 80+ à la racine |
| P6 | **Pas de Makefile** ni d'orchestration | Friction : chaque action est manuelle | Lancer investigation, linter, publier — tout est commande ad-hoc |
| P7 | **Pas de validation d'intégrité** | Risque de corruption silencieuse | Aucun script ne vérifie que les cross-refs entre fichiers sont valides |

### 0.3 Métriques de charge cognitive

| Métrique | Actuel | Cible |
|----------|--------|-------|
| Entrées racine visibles | 29 (11 fichiers + 18 dossiers) | ≤12 |
| Fichiers orphelins à la racine | 5 | 0 |
| Dossiers config IDE visibles | 7 | 1 (`config/`) |
| Dossiers inactifs visibles | 1 | 0 |
| Temps pour trouver un fichier | 15-30s | <5s |
| Temps pour comprendre la structure | 5-10 min | <1 min (PIPELINE_ARTICLE.md) |

---

## §1 — CIBLES

### 1.1 Cible A : Réorganisation minimale (recommandée)

**Principe :** Ne PAS renommer les dossiers actifs. Ne PAS casser les chemins relatifs. Seulement : déplacer les morts, cacher les configs, ajouter des raccourcis.

```
truth-engine/
│
├── ACTIF (7 entrées)
│   ├── engine/               ← truth-engine-v2/ (RENOMMÉ)
│   ├── content/              ← NOUVEAU dossier parent
│   │   ├── investigations/   ← (inchangé)
│   │   ├── articles/         ← (inchangé)
│   │   └── audits/           ← (inchangé)
│   ├── tools/                ← (inchangé)
│   ├── publish/              ← substack-online/ (RENOMMÉ)
│   ├── docs/                 ← (inchangé)
│   ├── sources/              ← (inchangé)
│   └── prompts/              ← (inchangé)
│
├── CONFIG (1 entrée)
│   ├── config/               ← NOUVEAU — rassemble .vscode, .claude, .opencode, .agents,
│   │                             .kilocode, .kilo, .codebuff, twitter_export
│   │   ├── vscode/
│   │   ├── claude/
│   │   ├── opencode/
│   │   ├── agents/
│   │   ├── kilocode/
│   │   ├── kilo/
│   │   ├── codebuff/
│   │   └── twitter_export/
│   └── kilo.json             ← déplacé ici
│
├── ARCHIVE (1 entrée)
│   ├── archive/              ← (inchangé) + nouveaux ajouts :
│   │   ├── v1/               ← KERNEL_v1_DEPRECATED.md + dépendances
│   │   ├── orphans/          ← novlang.md, knowledge.md, CONVENTIONS_NOMMAGE.md,
│   │   │                        DISCLAIMER.md
│   │   └── audit-vieux/      ← audits mars 2026
│
├── RACINE (4 entrées)
│   ├── AGENTS.md             ← (inchangé)
│   ├── README.md             ← MIS À JOUR — reflets structure réelle
│   ├── LICENSE               ← (inchangé)
│   └── Makefile              ← NOUVEAU — commandes d'orchestration
│
├── SCRIPTS (inclus dans tools/scripts/)
│   └── tools/scripts/reorganize.sh  ← NOUVEAU — script de migration
```

#### Qu'est-ce qui change vraiment ?

| Action | Fichiers | Risque |
|--------|----------|--------|
| Renommer `truth-engine-v2/` → `engine/` | ~30 fichiers internes | **ÉLEVÉ** — toutes les refs externes cassées (PIPELINE_ARTICLE.md, AGENTS.md, etc.) |
| Créer `content/` et déplacer `investigations/`, `articles/`, `audits/` dessous | ~200 fichiers | **MOYEN** — chemins relatifs dans les investigations cassés |
| Renommer `substack-online/` → `publish/` | ~90 fichiers | **FAIBLE** — peu de refs externes |
| Déplacer fichiers morts → `archive/` | 5 fichiers | **NUL** — fichiers non référencés |
| Grouper configs → `config/` | 7 dossiers | **NUL** — configs IDE, pas de refs internes |

Le risque principal est le **renommage des dossiers actifs** (engine, content, publish). Toute reférence croisée dans les fichiers devra être mise à jour.

### 1.2 Cible B : Minimal safe (si risque trop élevé)

**Principe :** Ne renommer AUCUN dossier actif. Seulement nettoyer ce qui est mort ou cachable.

```
truth-engine/
│
├── ACTIF (inchangé)
│   ├── truth-engine-v2/      ← (inchangé)
│   ├── investigations/       ← (inchangé)
│   ├── articles/             ← (inchangé)
│   ├── audits/               ← (inchangé)
│   ├── tools/                ← (inchangé)
│   ├── substack-online/      ← (inchangé)
│   ├── docs/                 ← (inchangé)
│   ├── sources/              ← (inchangé)
│   ├── prompts/              ← (inchangé)
│   └── archive/              ← (inchangé)
│
├── CONFIG (nouveau)
│   ├── config/               ← regroupe .vscode, .claude, .opencode, .agents, 
│   │                             .kilocode, .kilo, .codebuff, twitter_export
│   └── kilo.json             ← déplacé ici
│
├── NETTOYAGE (au lieu de archive/)
│   ├── archive/v1/           ← KERNEL_v1_DEPRECATED.md
│   └── archive/orphans/      ← novlang.md, knowledge.md, CONVENTIONS_NOMMAGE.md,
│                                 DISCLAIMER.md
│
├── RACINE (7 entrées)
│   ├── AGENTS.md
│   ├── README.md             ← mis à jour
│   ├── LICENSE
│   ├── truth-engine-v2/      ← (inchangé)
│   ├── investigations/       ← (inchangé)
│   ├── tools/                ← (inchangé)
│   └── Makefile              ← NOUVEAU
│
└── ---
```

**Ce qui change :** Rien dans les dossiers actifs. 5 fichiers morts → archive. 7 dossiers config → config/. Makefile ajouté. README.md mis à jour.

**Risque :** Zéro. Aucune référence cassée. Aucun chemin modifié.

---

## §2 — PLAN SAFE : NETTOYAGE SANS RISQUE

**Correspond à :** Cible B (§1.2). Aucun dossier actif renommé. Aucune référence cassée.

**Durée estimée :** 15 minutes.

### Phase 1 : Nettoyage des fichiers morts

Déplacer dans `archive/` les fichiers qui ne servent plus :

| Fichier | Destination | Raison |
|---------|-------------|--------|
| `KERNEL_v1_DEPRECATED.md` | `archive/v1/` | Déprécié, remplacé par truth-engine-v2/ |
| `DISCLAIMER.md` | `archive/orphans/` | Projet v1, plus pertinent |
| `novlang.md` | `archive/orphans/` | Orphelin, non référencé |
| `CONVENTIONS_NOMMAGE.md` | `archive/orphans/` | Absorbé par AGENTS.md |
| `knowledge.md` | `archive/orphans/` | Orphelin, non référencé |

### Phase 2 : Cacher les configs IDE

Créer un dossier `config/` à la racine et y déplacer les dossiers de configuration :

```bash
mkdir -p config
mv .vscode config/vscode
mv .claude config/claude
mv .opencode config/opencode
mv .agents config/agents
mv .kilocode config/kilocode
mv .kilo config/kilo
mv .codebuff config/codebuff
mv twitter_export config/twitter_export
mv kilo.json config/kilo.json
```

**Note :** Vérifier que les IDE clients pointent vers les nouveaux chemins. Certains IDE (Claude Code, OpenCode, Codebuff) peuvent avoir des fichiers de config internes qui référencent le chemin racine.

### Phase 3 : Nettoyage des audits anciens

Les audits de mars 2026 (6 fichiers dans `audits/`) sont des artefacts de l'ancien système KERNEL v1. Les déplacer dans `archive/audits/` :

```bash
mkdir -p archive/audits
mv audits/2026-03-0* archive/audits/
mv audits/2026-03-0* archive/audits/  # fichiers commençant par 2026-03-
```

**Ne PAS toucher aux audits de mai 2026.**

### Phase 4 : Mise à jour du README.md

Supprimer les références à :
- `kb/` (inexistant)
- `outputs/` (inexistant)
- `logs/` (inexistant)
- `STRUCTURE.md` (obsolète)

Ajouter une référence vers `docs/specs/PIPELINE_ARTICLE.md` comme point d'entrée principal.

### Phase 5 : Création du Makefile

Créer un Makefile à la racine avec les commandes d'orchestration de base (détaillé en §4).

### Phase 6 : Vérification finale

Exécuter le script de validation (voir §5) et le lint.

---

## §3 — PLAN B : RÉORGANISATION COMPLÈTE (optionnel)

**Risque :** Élevé. Casse les chemins relatifs. Réservé aux moments calmes.

**Durée estimée :** 2-3 heures (dont 1h de vérification).

### Prérequis

- Avoir exécuté le Plan A d'abord.
- Avoir un commit propre (`git commit -m "reorg: plan A"`).
- Avoir identifié toutes les références à `truth-engine-v2/` et `substack-online/`.

### Phase 1 : Renommer truth-engine-v2/ en engine/

```bash
git mv truth-engine-v2 engine
```

**Conséquence :** Tous les fichiers qui référencent `truth-engine-v2/` doivent être mis à jour :

| Fichier | Occurrences |
|---------|-------------|
| `AGENTS.md` | 3+ |
| `docs/specs/PIPELINE_ARTICLE.md` | 8+ |
| `docs/STRUCTURE.md` | 1+ |
| `docs/user/USER_GUIDE.md` | 1+ |
| `README.md` | 2+ |
| `truth-engine-v2/ARCHITECTURE.md` | 2+ (auto-réf.) |

### Phase 2 : Créer content/ et déplacer investigations/ + articles/ + audits/

```bash
mkdir content
git mv investigations content/
git mv articles content/
git mv audits content/
```

**Conséquence :** Les chemins relatifs dans les investigations (`../sources/`, `../../tools/`) doivent être vérifiés. Les fichiers dans `content/investigations/XXX/articles/` référencent `../sources/` qui devient `../../sources/`.

### Phase 3 : Renommer substack-online/ en publish/

```bash
git mv substack-online publish
```

### Phase 4 : Mise à jour massive des références

Utiliser `sed` pour mettre à jour les chemins dans tous les fichiers concernés :

```bash
# truth-engine-v2/ → engine/
find . -name '*.md' -not -path './archive/*' -exec sed -i 's|truth-engine-v2/|engine/|g' {} +

# substack-online/ → publish/
find . -name '*.md' -not -path './archive/*' -exec sed -i 's|substack-online/|publish/|g' {} +
```

**⚠️ Danger :** `sed -i` ne fait pas de backup. Toujours faire un `git stash` ou commit avant.

### Phase 5 : Vérification exhaustive

Exécuter le script de validation (voir §5). Vérifier que `./tools/scripts/lint-article.sh` fonctionne encore sur les articles existants.

---

## §4 — LES SUPERPOWERS (AUTOMATISATION)

### 4.1 Script de réorganisation : `tools/scripts/reorganize.sh`

Script bash exécutant le Plan A avec mode dry-run. Usage :

```bash
# Voir ce qui serait fait (dry-run)
./tools/scripts/reorganize.sh --dry-run

# Exécuter la réorganisation
./tools/scripts/reorganize.sh
```

```bash
#!/usr/bin/env bash
# REORGANIZE.SH — Réorganisation minimale (Plan A)
# Usage: ./tools/scripts/reorganize.sh [--dry-run]
# Options: --dry-run : simuler sans rien déplacer
#          --force   : exécuter sans confirmation

set -euo pipefail

DRY_RUN=false
FORCE=false
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --force) FORCE=true ;;
  esac
done

run() {
  if [ "$DRY_RUN" = true ]; then
    echo "  🔍 DRY-RUN: $*"
  else
    echo "  ⚡ $*"
    eval "$@"
  fi
}

# Couleurs
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

cd "$(git rev-parse --show-toplevel 2>/dev/null || echo '.')"

echo "════════════════════════════════════════"
echo " REORGANIZE — Plan A (minimal)"
echo "════════════════════════════════════════"

# Phase 1: Fichiers morts → archive/
echo ""
echo -e "${YELLOW}Phase 1 : Archivage des fichiers morts${NC}"

run "mkdir -p archive/v1 archive/orphans"

for f in DISCLAIMER.md novlang.md CONVENTIONS_NOMMAGE.md knowledge.md; do
  if [ -f "$f" ]; then
    run "git mv $f archive/orphans/"
  fi
done

if [ -f KERNEL_v1_DEPRECATED.md ]; then
  run "git mv KERNEL_v1_DEPRECATED.md archive/v1/"
fi

# Phase 2: Configs IDE → config/
echo ""
echo -e "${YELLOW}Phase 2 : Regroupement des configs IDE${NC}"

run "mkdir -p config"

for dir in .vscode .claude .opencode .agents .kilocode .kilo .codebuff twitter_export; do
  if [ -d "$dir" ]; then
    # Enlève le point initial pour les dossiers cachés (.vscode → vscode)
    basename="${dir#.}"
    run "git mv $dir config/$basename"
  fi
done

if [ -f kilo.json ]; then
  run "git mv kilo.json config/"
fi

# Phase 3: Audits anciens → archive/audits/
echo ""
echo -e "${YELLOW}Phase 3 : Archivage des audits anciens${NC}"

# Compter les fichiers correspondant au pattern
count=$(find audits/ -maxdepth 1 -name '2026-03-0*.md' 2>/dev/null | wc -l)
if [ "$count" -gt 0 ]; then
  run "mkdir -p archive/audits"
  # find + xargs plus robuste que -exec avec escaping
  run "find audits/ -maxdepth 1 -name '2026-03-0*.md' -print0 | xargs -0 git mv -t archive/audits/"
fi

# Résumé
echo ""
echo "════════════════════════════════════════"
echo -e "${GREEN}Récapitulatif Plan A${NC}"
echo ""
echo "  Fichiers archivés  : DISCLAIMER.md, KERNEL_v1_DEPRECATED.md,"
echo "                        novlang.md, CONVENTIONS_NOMMAGE.md, knowledge.md"
echo "  Dossiers config    : .vscode, .claude, .opencode, .agents,"
echo "                        .kilocode, .kilo, .codebuff, twitter_export"
echo "  Audits archivés    : mars 2026"
echo ""

if [ "$DRY_RUN" = true ]; then
  echo -e "${YELLOW}DRY-RUN terminé. Aucun fichier déplacé.${NC}"
  echo -e "${YELLOW}Passez --force pour exécuter.${NC}"
else
  echo -e "${GREEN}Réorganisation terminée.${NC}"
  echo -e "${YELLOW}Vérifiez avec : git status && git diff --stat${NC}"
  echo -e "${YELLOW}Puis : ./tools/scripts/validate-refs.sh${NC}"
fi
```

### 4.2 Script de validation des références : `tools/scripts/validate-refs.sh`

Vérifie que tous les chemins référencés dans les fichiers `.md` existent réellement. Détecte les dead links.

```bash
#!/usr/bin/env bash
# VALIDATE-REFS.SH — Vérifie l'intégrité des références entre fichiers
# Usage: ./tools/scripts/validate-refs.sh [--strict]

set -euo pipefail

echo "════════════════════════════════════════"
echo " VALIDATE-REFS — Vérification des chemins"
echo "════════════════════════════════════════"

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo '.')
cd "$ROOT"

ERRORS=0
WARNINGS=0

# Vérifier les références à des chemins locaux dans les fichiers .md
# Pattern: `chemin/vers/fichier` dans les fichiers markdown
while IFS= read -r file; do
  # Extraire les chemins entre backticks qui ressemblent à des fichiers
  # (contiennent un / ou finissent par .md, .sh, .json)
  # grep -oE pour compatibilité Linux/macOS (pas de -P)
  refs=$(grep -oE '`[a-zA-Z0-9_/.@-]+/[a-zA-Z0-9_/.@-]+\.[a-z]{2,4}`' "$file" 2>/dev/null || true)
  
  while IFS= read -r ref; do
    # Nettoyer les backticks
    path="${ref#\`}"
    path="${path%\`}"
    
    # Vérifier si le chemin existe
    if [ ! -e "$path" ] && [ ! -e "$(dirname "$file")/$path" ]; then
      echo "  ❌ $file → $path (introuvable)"
      ERRORS=$((ERRORS + 1))
    fi
  done <<< "$refs"
done < <(find . -name '*.md' -not -path './node_modules/*' -not -path './archive/*' -not -path './.git/*')

echo ""
if [ $ERRORS -eq 0 ]; then
  echo "  ✅ Aucune référence cassée."
else
  echo "  ❌ $ERRORS référence(s) cassée(s) trouvée(s)."
  exit 1
fi
```

### 4.3 Makefile

```makefile
# Makefile — Commandes d'orchestration du projet truth-engine
# Usage: make <commande>

.PHONY: help lint nav tree status validate

help:
	@echo "Commandes disponibles :"
	@echo ""
	@echo "  make lint       Linter un article: make lint FILE=articles/xxx.md"
	@echo "  make tree       Afficher l'arborescence du projet"
	@echo "  make nav        Afficher le guide de navigation (PIPELINE_ARTICLE.md)"
	@echo "  make status     Statut git + infos projet"  
	@echo "  make validate   Vérifier l'intégrité des références"
	@echo "  make reorg      Simuler la réorganisation (dry-run)"
	@echo ""

lint:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make lint FILE=articles/xxx.md"; \
		exit 1; \
	fi
	@./tools/scripts/lint-article.sh "$(FILE)"

tree:
	@tree -I 'node_modules|.git|archive' -L 2 --dirsfirst

nav:
	@echo "📖 Guide de navigation : docs/specs/PIPELINE_ARTICLE.md"
	@head -30 docs/specs/PIPELINE_ARTICLE.md

status:
	@echo "=== Git Status ==="
	@git status --short | head -20
	@echo ""
	@echo "=== Fichiers racine ==="
	@ls -la . | grep -v node_modules | grep -v '.git$'

validate:
	@./tools/scripts/validate-refs.sh

reorg:
	@./tools/scripts/reorganize.sh --dry-run
```

### 4.4 Arbre de navigation rapide

Ajouter dans `PIPELINE_ARTICLE.md` un bloc réutilisable. Ou, mieux, créer un lien symbolique vers `docs/specs/PIPELINE_ARTICLE.md` nommé `NAVIGATION.md` à la racine :

```bash
ln -s docs/specs/PIPELINE_ARTICLE.md NAVIGATION.md
```

Ainsi `cat NAVIGATION.md` ou `make nav` donne immédiatement la carte.

---

## §5 — VALIDATION

### 5.1 Tests post-migration

Après avoir exécuté le Plan A (ou B), effectuer ces vérifications dans l'ordre :

| # | Test | Commande | Résultat attendu |
|---|------|----------|------------------|
| 1 | Git status | `git status --short` | Aucun fichier non tracké inattendu |
| 2 | Références | `./tools/scripts/validate-refs.sh` | 0 erreurs |
| 3 | Lint article | `./tools/scripts/lint-article.sh articles/2026-05-28_14-10_peuple-souverain-resistance_ARTICLE.md` | 0 violations |
| 4 | README | Vérifier manuellement | Plus de référence à kb/ |
| 5 | Configs IDE | Lancer Claude/OpenCode/Codebuff | Les outils fonctionnent |

### 5.2 Journal de migration

Pour tracer ce qui a été fait, ajouter une entrée dans un fichier `MIGRATION_LOG.md` à la racine :

```markdown
# Migration Log

## 2026-05-29 — Réorganisation Plan A

**Ce qui a été fait :**
- KERNEL_v1_DEPRECATED.md → archive/v1/
- DISCLAIMER.md, novlang.md, CONVENTIONS_NOMMAGE.md, knowledge.md → archive/orphans/
- .vscode, .claude, .opencode, .agents, .kilocode, .kilo, .codebuff → config/
- twitter_export/ → config/twitter_export/
- kilo.json → config/
- Audits mars 2026 → archive/audits/
- README.md mis à jour (suppression références à kb/)
- Makefile créé
- validate-refs.sh créé

**Problèmes rencontrés :** ...

**Validations :**
- validate-refs.sh : ✅ 0 erreurs
- lint-article.sh : ✅ 0 violations
```

---

## §6 — ROLLBACK

### 6.1 Rollback via git

Si la réorganisation a été commitée :

```bash
# Voir le dernier commit
$ git log --oneline -5

# Annuler le dernier commit (garder les changements dans le working directory)
$ git reset --soft HEAD~1

# OU : annuler complètement (perdre les changements)
$ git reset --hard HEAD~1
```

### 6.2 Rollback manuel (si non commité)

```bash
# Restaurer les fichiers déplacés depuis archive/orphans/
git checkout -- DISCLAIMER.md novlang.md CONVENTIONS_NOMMAGE.md knowledge.md

# Restaurer KERNEL v1
git checkout -- KERNEL_v1_DEPRECATED.md

# Restaurer les configs IDE (après avoir vidé config/)
git checkout -- .vscode .claude .opencode .agents .kilocode .kilo .codebuff

# Restaurer twitter_export
git checkout -- twitter_export/

# Restaurer audits
git checkout -- audits/2026-03-*.md

# Supprimer les dossiers créés
rm -rf archive/v1 archive/orphans archive/audits config Makefile tools/scripts/validate-refs.sh
```

### 6.3 Condition de rollback

Le rollback est possible tant qu'aucun nouveau fichier n'a été créé dans les dossiers déplacés. Si tu as lancé une nouvelle investigation après la réorganisation, le rollback est plus complexe.

---

## §7 — MAINTENANCE

### 7.1 Règles pour garder la racine propre

1. **Tout nouveau dossier** de configuration IDE va dans `config/`
2. **Tout fichier racine** doit être justifié dans `PIPELINE_ARTICLE.md`
3. **Tout fichier mort** va dans `archive/` dans les 7 jours
4. **Les audits** de plus de 2 mois vont dans `archive/audits/`
5. **Les investigations** terminées depuis >3 mois vont dans `archive/investigations/`

### 7.2 Rythme de ménage

| Action | Fréquence |
|--------|-----------|
| Déplacer fichiers morts → archive | À chaque fin d'article |
| Nettoyer la racine | Mensuel |
| Mettre à jour PIPELINE_ARTICLE.md | À chaque changement de structure |
| Exécuter validate-refs.sh | Avant chaque commit |

### 7.3 Pre-commit hook (optionnel)

```bash
# .git/hooks/pre-commit — Vérifie les références avant chaque commit
#!/usr/bin/env bash

./tools/scripts/validate-refs.sh
if [ $? -ne 0 ]; then
  echo "❌ Références cassées détectées. Corrigez avant de commit."
  exit 1
fi
```

Pour installer :
```bash
# Créer le fichier .git/hooks/pre-commit avec le contenu ci-dessus
cat > .git/hooks/pre-commit << 'HOOK'
#!/usr/bin/env bash
./tools/scripts/validate-refs.sh
if [ $? -ne 0 ]; then
  echo "❌ Références cassées détectées. Corrigez avant de commit."
  exit 1
fi
HOOK
chmod +x .git/hooks/pre-commit
```

---

*Document de spécification v1.0 — À valider avant exécution.*
