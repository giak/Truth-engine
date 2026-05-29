# REORGANIZATION — Plan de nettoyage racine

**Date :** 2026-05-29
**Statut :** Spécification — aucune modification appliquée
**Contexte :** Passage de 29 à ~12 entrées à la racine du projet.

---

## §0 — Diagnostic

### État actuel : 29 entrées racine

```
FICHIERS (11)
│   ├── AGENTS.md                 ✅ ACTIF
│   ├── README.md                 ✅ ACTIF (mais cite kb/ inexistant)
│   ├── LICENSE                   📄 Neutre
│   ├── DISCLAIMER.md             ❌ OBSOLÈTE
│   ├── package.json              📄 Métadonnées
│   ├── package-lock.json         📄 Généré
│   ├── KERNEL_v1_DEPRECATED.md   ❌ OBSOLÈTE
│   ├── novlang.md                🤷 ORPHELIN
│   ├── CONVENTIONS_NOMMAGE.md    🤷 DOUBLON (absorbé par AGENTS.md)
│   ├── knowledge.md              🤷 ORPHELIN
│   └── kilo.json                 ⚙️ Config IDE

DOSSIERS (18)
│   ├── .vscode/                  ⚙️ Config IDE
│   ├── .claude/                  ⚙️ Config IDE
│   ├── .opencode/                ⚙️ Config IDE
│   ├── .agents/                  ⚙️ Config IDE
│   ├── .kilocode/                ⚙️ Config IDE
│   ├── .kilo/                    ⚙️ Config IDE
│   ├── .codebuff/                ⚙️ Config IDE
│   ├── truth-engine-v2/          ✅ ACTIF
│   ├── investigations/           ✅ ACTIF (100+ fichiers)
│   ├── articles/                 ✅ ACTIF (~10 articles)
│   ├── audits/                   ✅ ACTIF (~15 audits)
│   ├── tools/                    ✅ ACTIF
│   ├── substack-online/          ✅ ACTIF (86 posts)
│   ├── docs/                     ✅ ACTIF
│   ├── prompts/                  ✅ ACTIF
│   ├── sources/                  ✅ ACTIF
│   ├── twitter_export/           🤷 INACTIF
│   └── archive/                  ✅ Archive
```

### Problèmes

| # | Problème | Impact |
|---|----------|--------|
| P1 | 11 fichiers racine dont 5 morts | 50% de bruit |
| P2 | 7 dossiers config IDE à la racine | 7 entrées parasites |
| P3 | 1 dossier inactif (twitter_export/) | Bruit |
| P4 | README cite kb/ (inexistant) | Confusion |

### Cible : ~12 entrées racine

```
AGENTS.md, README.md, LICENSE, package.json, package-lock.json,
truth-engine-v2/, investigations/, articles/, audits/, tools/,
substack-online/, docs/, prompts/, sources/, archive/
```

---

## §1 — Plan d'exécution : 10 commandes, 5 minutes

```bash
# Phase 1 : fichiers morts → archive/
mkdir -p archive/v1 archive/orphans
git mv KERNEL_v1_DEPRECATED.md archive/v1/
git mv DISCLAIMER.md novlang.md CONVENTIONS_NOMMAGE.md knowledge.md archive/orphans/

# Phase 2 : configs IDE → config/
mkdir config
for dir in .vscode .claude .opencode .agents .kilocode .kilo .codebuff; do
  [ -d "$dir" ] && git mv "$dir" "config/${dir#.}"
done
git mv twitter_export config/
git mv kilo.json config/

# Phase 3 : update README (supprimer références à kb/ outputs/ logs/ STRUCTURE.md)
```

### Résultat attendu

29 entrées → ~12. Aucun dossier actif renommé. Aucune référence cassée.

### Rollback

```bash
git reset --soft HEAD~1   # si commité
# OU
git checkout -- DISCLAIMER.md novlang.md CONVENTIONS_NOMMAGE.md knowledge.md KERNEL_v1_DEPRECATED.md
git checkout -- .vscode .claude .opencode .agents .kilocode .kilo .codebuff twitter_export/
rm -rf archive/v1 archive/orphans config
```

---

*Document de spécification minimal. Voir docs/specs/PIPELINE_ARTICLE.md pour la navigation complète du projet.*
