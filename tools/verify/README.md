# tools/verify — Vérificateur générique

Moteur de vérification déterministe, **indépendant de tout projet**. Il ne connaît aucune règle métier : toutes les règles sont déclarées dans `.verify/config.json`.

## Principe

```
UNVERIFIED → VERIFY → PASS → DELIVERABLE
```

- `NO PASS => NO DELIVERY`
- `CHANGE AFTER PASS => PASS INVALID`

Trois verdicts, et seulement trois : `PASS`, `FAIL`, `BLOCKED`. Pas de score.

## Fichiers

| Fichier | Rôle |
|---|---|
| `tools/verify/verify.py` | Moteur déterministe (stdlib Python 3 uniquement, aucune dépendance) |
| `.verify/config.json` | Règles du projet (branches protégées, tests, contrôles, nommage) |
| `.verify/pending.json` | État + verdict déterministe enregistrés par `check` (transitoire, gitignoré) |
| `.verify/result.json` | Certificat final (transitoire, gitignoré) |
| `.agents/truth-verifier.ts` | Agent Codebuff : orchestre check → review → certify |
| `.agents/truth-reviewer.ts` | Agent Codebuff : revue indépendante en contexte neuf, lecture seule |

## Modes

```bash
python3 tools/verify/verify.py check                       # déterministe + STATE_ID (exit 0/1/2)
python3 tools/verify/verify.py state-id                    # STATE_ID courant
python3 tools/verify/verify.py certify --review PASS|FAIL|BLOCKED|N/A
python3 tools/verify/verify.py gate --file <livrable>      # check + certify, déterministe seul
```

`check` et `certify` écrivent un rapport JSON sur stdout. Codes retour : `0` = PASS, `1` = FAIL, `2` = BLOCKED.

### Gate unifié (`gate`)

`gate` exécute `check` + `certify` en une commande, sans revue LLM :

```
gate
  1. check (déterministe)      FAIL/BLOCKED → le certificat porte ce verdict, jamais PASS
  2. horodatage (déterministe) le nom de fichier ne doit pas être dans le futur
  3. certify (result.json au format officiel, review=N/A)
```

- Pas de reviewer local : Ollama a été supprimé (2026-08-18), un LLM sans outils ne peut pas fact-checker. Le verdict est le déterministe seul.
- La revue sémantique premium, si le runtime Codebuff l'expose, est le sous-agent `truth-reviewer` (chemin spawn, `.agents/truth-verifier.ts`), jamais requis.
- `--file` est optionnel : sans lui, le contrôle d'horodatage est sauté (noté dans `review_note`). stdout porte le certificat final, le rapport de check va sur stderr.

## Adapter à n'importe quel projet

1. Copier `tools/verify/verify.py` dans le projet cible.
2. Créer `.verify/config.json` avec les règles du projet.
3. (Optionnel, Codebuff) copier `.agents/truth-verifier.ts` et `.agents/truth-reviewer.ts`.

Le moteur reste identique. Seul le config change.

## Schéma de configuration

```json
{
  "version": 1,
  "task": "identifiant-du-chantier",
  "protected_branches": ["main", "master"],
  "tests": ["pytest -q"],
  "checks": [
    {
      "name": "no-todo",
      "cmd": "grep -rn 'TODO' src/ && exit 1 || exit 0",
      "fail_message": "TODO restants dans src/"
    }
  ],
  "naming": {
    "enabled": true,
    "dirs": ["docs/"],
    "pattern": "^\\d{4}-\\d{2}-\\d{2}_[A-Za-z0-9]+(-[A-Za-z0-9]+)*_(REPORT|NOTE)\\.md$",
    "dir_pattern": "^\\d{4}-\\d{2}-\\d{2}_[A-Za-z0-9]+(-[A-Za-z0-9]+)*$",
    "only_types": ["REPORT", "NOTE"],
    "since": "2026-01-01",
    "exclude": []
  },
  "content": [
    {
      "name": "no-em-dash-in-published-articles",
      "forbidden": "—",
      "dirs": ["articles/"],
      "dir_pattern": "^\\d{4}-\\d{2}-\\d{2}_[A-Za-z0-9]+(-[A-Za-z0-9]+)*$",
      "only_types": ["ARTICLE"],
      "since": "2026-01-01",
      "exclude": []
    }
  ]
}
```

| Clé | Sens |
|---|---|
| `protected_branches` | Travailler sur ces branches → `BLOCKED` (isolation par chantier) |
| `tests` | Commandes de test. Code retour ≠ 0 → `FAIL` ; commande introuvable (127) → `BLOCKED` |
| `checks` | Contrôles arbitraires. Tout ce qu'une machine peut vérifier doit être un `check`, pas un prompt |
| `naming` | Convention de nommage. **Désactivé par défaut** : ne jamais automatiser une règle contradictoire |
| `naming.dir_pattern` | Regex sur les composants du chemin : le dossier n'est parcouru que si au moins un composant matche (ex : dossiers de chantier datés `YYYY-MM-DD_<sujet>` nichés sous `YYYY-MM/`) |
| `naming.only_types` | Si présent, seuls les livrables `_<TYPE>.md` (types officiels) sont vérifiés. Fichiers de travail internes (`MEMO`, `SYNTHESE`, brouillons) hors scope |
| `naming.since` | Date de coupure `YYYY-MM-DD` : seuls les fichiers datés ≥ `since` sont vérifiés. Applique la convention aux livrables nouveaux sans flagger le legacy |
| `naming.exclude` | Regex sur le chemin relatif complet : fichiers/dossiers exclus du check |
| `content` | Contenu interdit. Chaque entrée : `forbidden` (chaîne ou regex), `name`, et le **même périmètre** que `naming` (`dirs`, `dir_pattern`, `only_types`, `since`, `exclude`). Ex : interdire l'em-dash (U+2014) dans les articles publiés sans flagger les brouillons |

**Règle de séparation** : `DETERMINISTIC POSSIBLE => CODE` ; `SEMANTIC JUDGMENT REQUIRED => REVIEWER`.

## STATE_ID

```
STATE_ID := SHA256( HEAD + diff suivi + fichiers non suivis + hash de leur contenu )
```

Deux états différents peuvent partager le même `HEAD`. `STATE_ID` capture l'état complet. Les artefacts du verifier (`.verify/`) sont exclus du calcul, sinon le verifier se certifierait lui-même faux.

Toute modification après `check` → `certify` détecte `state_changed: true` → verdict `FAIL` (il faut re-vérifier).

## Boucle complète (côté Codebuff)

```
AUTHOR
  → spawn truth-verifier
      → verify.py check          (déterministe + STATE_ID)
      → [si PASS] spawn truth-reviewer   (contexte neuf, lecture seule)
      → verify.py certify --review <verdict>
      → PASS / FAIL / BLOCKED
```

- `FAIL` → réparer puis relancer la vérification **complète**.
- `BLOCKED` → déclarer le blocage ; ne pas prétendre que le travail est validé.
- Toute correction après `PASS` invalide le `PASS`.

## Isolation par worktree

Invariant : `1 chantier = 1 branche = 1 worktree = 1 cycle de vérification`.

```bash
tools/verify/worktree-new.sh <chantier>       # crée .worktrees/<chantier> sur une branche non protégée
cd .worktrees/<chantier>
python3 tools/verify/verify.py check
```

- Le helper refuse de créer un chantier sur une branche protégée (`protected_branches` du config).
- `.worktrees/` est gitignoré : les worktrees ne sont jamais commités.
- Suppression : `git worktree remove .worktrees/<chantier>` puis `git branch -D <chantier>`.

Note : un worktree isole branches, diff et historique ; ce n'est pas une sandbox de sécurité OS. Pour un chantier sensible, utiliser un conteneur (niveau « hardened » du cahier des charges).

## Limite connue (V1)

Les agents `.ts` suivent le contrat `AgentDefinition` de Codebuff, vérifié contre la documentation active (`docs/agents/creating-new-agents`, `docs/agents/agent-reference`) :

- `handleSteps` est un générateur qui reçoit `{ toolResult, toolError }` à chaque `yield` ; `toolResult` est une **chaîne** (JSON ou texte).
- L'extraction du verdict reviewer → certify est défensive : elle retombe sur `BLOCKED` en cas d'illisibilité, jamais sur `PASS`.
- `--review` est **obligatoire** : `certify` sans `--review` émet `BLOCKED` (fail-safe). Un certificat `review: PASS` ne peut venir que d'un `--review PASS` explicite. `NO REVIEW => NO PASS`.
- Ce qui n'a pas pu être validé depuis une session agent : le chargement réel des `.agents/*.ts` par le runtime. À confirmer en orchestrant un premier chantier dans Codebuff.

### Extension V2 : thinker / researcher

Le reviewer est volontairement sans `spawnableAgents` en V1. Pour ajouter les spécialistes :

```ts
spawnableAgents: ['codebuff/thinker@<version>', 'codebuff/researcher@<version>']
```

Les agents built-in exigent `publisher/nom@version` (ex. `codebuff/thinker@0.0.1`). Les agents locaux se référencent par leur seul id (ex. `truth-reviewer`). Vérifier la version réelle avant d'activer.

## Sécurité

Les commandes de `tests` et `checks` sont du code de confiance (écrit par le développeur du projet), au même titre qu'un Makefile ou une config CI. Ne pas exécuter `verify.py` avec un config non audité.
