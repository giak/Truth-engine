# Truth Engine — Project Knowledge

> Système d'analyse cognitive (LLM-driven) pour détecter la manipulation dans les discours.
> Version 11.0. Production-ready. Langue de travail : **français**.

Ce dépôt n'est **pas un projet logiciel classique** : il n'y a quasi aucun code exécutable. C'est un **système opérationnel de prompts, protocoles et knowledge base** chargé dans une session LLM (Claude/GPT) pour mener des investigations forensiques sur la manipulation médiatique, politique et économique.

## Quoi / Où

⚠️ Le `README.md` et `docs/STRUCTURE.md` décrivent une arborescence (`KERNEL.md` racine, dossier `kb/`) qui ne correspond plus à la réalité du dépôt. La structure actuelle est centrée sur `truth-engine-v2/`.

| Élément | Emplacement | Rôle |
|---|---|---|
| **Cœur opérationnel (à charger en premier)** | `truth-engine-v2/KERNEL.md` | Phases 0-9, formules, DSL, gates |
| Architecture moteur | `truth-engine-v2/ARCHITECTURE.md` | Vue système |
| DSL & macros | `truth-engine-v2/tools/DSL.md`, `tools/MACROS.md` | Primitives et raccourcis |
| Définitions | `truth-engine-v2/definitions/` (`PATTERNS.md`, `THREATS.md`, `SYMBOLS.md`) | Vocabulaire |
| 15 clusters de manipulation | `truth-engine-v2/clusters/` (`ICEBERG.md`, `MONEY.md`, `INVERSION.md`, `GASLIGHTING.md`, `FRAMING.md`, `SPECTACLE.md`, `OVERLOAD.md`, `FRAGMENTATION.md`, `NETWORK.md`, `POWER.md`, `WAR.md`, `TEMPORAL.md`, `BIO.md`, `RESISTANCE.md`, `CONFIRMATION.md`, plus `_TEMPLATE.md` / `_INDEX.md`) | Patterns détectables |
| Protocoles | `truth-engine-v2/protocol/` (`INVESTIGATION.md`, `PERSO_FRESQUE.md`) | Flow d'enquête |
| Forensic | `truth-engine-v2/forensic/` (`GATES.md`, `REASONING.md`, `REQUEST_LOG.md`) | Gates qualité, logs |
| Recherche | `truth-engine-v2/search/` (`OPTIMIZATION.md`, `TEMPLATES.md`, `EPISTEMIC.md`) | Templates de queries |
| Output | `truth-engine-v2/output/TEMPLATE.md` | Format du rapport final |
| Philosophie | `docs/VISION.md` | Pourquoi & comment voir la manipulation |
| Specs | `docs/specs/PRD.md`, `docs/specs/SCL_NOTATION.md` | Requirements + notation compressée |
| Guide utilisateur | `docs/user/USER_GUIDE.md`, `docs/user/PHILOSOPHY.md` | Pour aller plus loin |
| Productions | `investigations/`, `articles/`, `sources/`, `audits/` | Contenu généré |
| Substack | `substack-online/` (`posts.csv`, `posts/*.html`, `email_list.giak.csv`) | Export plateforme |
| Config MCP | `.kilocode/mcp.json`, `.claude/settings.local.json`, `.agents/` | Serveurs MCP, agents |
| Archives | `archive/` | Anciennes versions, backups |

Investigations actives importantes : `investigations/2026-05-21_etat-reel-france/` (pipeline en plusieurs phases : `00B_CENSUS.md` → `01_DIGEST.md` → `02_DIALECTIQUE.md` → `03_ARCHITECTURE.md` → `04_FACTCHECK.md` → `_assemblage/draft_article.md` → `_assemblage/quality_gate.md`) et `investigations/2026-05-23_macron-systeme-complet/`.

## Workflow type

```
1. Coller truth-engine-v2/KERNEL.md dans une session LLM vierge
2. Donner un sujet : "Analyse: [sujet]" ou "Investigation APEX: [sujet]. Target EDI≥0.80."
3. Le LLM exécute Phase 0 → 9 (mémoire MnemoLite, complexité, herméneutique,
   recherche web, patterns, métriques EDI/ISN/Wolves/H7, output, sauvegarde)
4. Récupérer un rapport structuré dans investigations/ ou articles/
```

Pas de `npm test`, pas de build. `package.json` ne contient que deux dépendances MCP (`@modelcontextprotocol/server-sequential-thinking`, `tavily-mcp`) — aucun script. Toute l'« exécution » se passe dans le LLM.

## Conventions (OBLIGATOIRES — voir `AGENTS.md` et `CONVENTIONS_NOMMAGE.md`)

### Nommage des fichiers générés
Format : `YYYY-MM-DD_HH-MM_<sujet-kebab>_<TYPE>.md` dans `investigations/`, `articles/`, `outputs/`.

Types valides : `INVESTIGATION`, `ARTICLE`, `HYPER_MATRICE`, `ARCHITECTURE`, `SATURATION_AUDIT`, `REGISTRE`, `CONCLUSION`. Le suffixe `SOURCES` est aussi observé dans `sources/`.

Règles : pas d'espaces, pas d'accents, sujet en kebab-case, type en MAJUSCULES.

### RTK — Optimisation token (OBLIGATOIRE pour shell commands)
Préfixer **toutes** les commandes shell avec `rtk` lors de l'exécution via un agent : `rtk ls`, `rtk grep`, `rtk git status`, `rtk read fichier`, `rtk find`, `rtk pnpm`, `rtk vitest`, `rtk tsc`. Économie typique 60-90 %. Détails et tableau complet dans `AGENTS.md` § RTK.

**Exceptions (jamais de `rtk`)** : commandes à effets de bord (`git add`, `git commit`, `git push`, `npm install`, `mkdir`, `cp`, `mv`, `rm`) et interactives (`vim`, `htop`, `less`).

### Éthique éditoriale (axiomes du projet)
- **Honnêteté absolue, zéro flagornerie** : pas de fioritures sociales, vérité brute > politesse.
- **Anti-hallucination** : double-check systématique des dates/chiffres/noms ; sources primaires citées ; aveu d'ignorance plutôt qu'invention.
- **Style direct** : résultats standalone, prêts à publier, précision forensique.
- **Français soutenu** : pas d'anglicismes, typographie française (espaces insécables avant `:` `;` `?` `!`, guillemets `« »`), syntaxe idiomatique. Voir section "Rôle d'Écriture en Français" dans `AGENTS.md`.

### DSL cognitif (primitives)
`Ξ` iceberg · `€` cui bono · `Λ` cadrage · `Ω` inversion (DARVO) · `Ψ` surcharge · `↕` verticale haut/bas. Détails : `truth-engine-v2/tools/DSL.md` et `truth-engine-v2/definitions/SYMBOLS.md`.

### Hiérarchie des sources
`◈` PRIMARY (90-95 %) > `◉` SECONDARY (75-85 %) > `○` TERTIARY (40-70 %). Sources officielles plafonnées à 0.20 sauf corroboration ◈.

### Métriques cibles (APEX)
EDI ≥ 0.80 · Sources ≥ 20 · Wolves ≥ 8 · 15 clusters chargés (le `README.md` cite 19, chiffre obsolète).

## Gotchas

- **Ne pas modifier `truth-engine-v2/`** avec du contenu généré — c'est le système, pas une production.
- **`README.md` et `docs/STRUCTURE.md` sont partiellement obsolètes** : ils référencent un dossier `kb/` et un `KERNEL.md` à la racine qui n'existent plus. Source de vérité actuelle : `truth-engine-v2/`.
- **Bug `write()` LLM > 5000 chars** : segmenter en `write()` initial (≤ 3000 chars) puis `edit()` successifs. Procédure complète dans `AGENTS.md` § "BUG DOCUMENTÉ".
- **Pas de roadmap formelle** : boucle Investigation → Métriques → Feedback → Amélioration.
- **`.claudeignore`** filtre ce que voient les agents Claude — vérifier avant d'attendre qu'un fichier soit lu.
- **`substack-online/email_list.giak.csv`** contient des données personnelles : ne pas committer / partager sans précaution.
- Le pipeline `investigations/2026-05-21_etat-reel-france/sections/` a été massivement nettoyé (cf. `git status`) — réorganisation en cours.

## Pour démarrer

1. Lire `docs/VISION.md` (philosophie) puis `truth-engine-v2/KERNEL.md` (exécution) et `truth-engine-v2/ARCHITECTURE.md`.
2. Explorer une investigation récente complète, ex. `investigations/2026-05-23_macron-systeme-complet/` ou `investigations/2026-05-21_etat-reel-france/`.
3. Pour un nouveau sujet : `"Analyse: [sujet]. Truth Engine protocol."` dans une session LLM avec `truth-engine-v2/KERNEL.md` chargé.
