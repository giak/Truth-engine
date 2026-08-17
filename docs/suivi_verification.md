# Suivi de la boucle de vérification

> Tableau de bord du chantier. Cahier des charges : `docs/boucle_de_verification.md`.
> Le « verdict courant » est régénérable à tout moment : `python3 tools/verify/verify.py report`.

## 1. État d'avancement (roadmap §52)

| # | Étape | Statut | Preuve / reste |
|---|---|---|---|
| 0 | Assainissement minimal | 🔶 partiel | `knowledge.md` consolidé (canonique), `AGENTS.md` pointeur. Reste : trancher kebab-case vs snake_case |
| 1 | `truth-reviewer.ts` | ✅ écrit | `.agents/truth-reviewer.ts`, `node --check` OK. Runtime non validé |
| 2 | Gate déterministe | ✅ | `tools/verify/verify.py` : `check` / `state-id` / `certify` / `report` |
| 3 | STATE_ID | ✅ testé | invalidation post-modif vérifiée (fichier non suivi + worktree) |
| 4 | `truth-verifier.ts` | ✅ écrit | `.agents/truth-verifier.ts`, `node --check` OK. Runtime non validé |
| 5 | DELIVERY GATE | ✅ | section ajoutée dans `knowledge.md` |
| 6 | Worktrees | ✅ | `tools/verify/worktree-new.sh`, démo `.worktrees/te-verification-gate` |
| 7 | Enforcement orchestrateur | ❌ | le spawn Codebuff des agents n'est pas validé depuis une session agent |

## 2. Décisions ouvertes

- **kebab-case vs snake_case** : bloquant pour activer le check de nommage (§20.1). Documenté `enabled: false` dans `.verify/config.json`.
- **Runtime des `.agents/*.ts`** : à valider en orchestrant un premier chantier dans Codebuff. Le câblage verdict reviewer → certify est fail-safe (retombe sur `BLOCKED`, jamais `PASS`).

## 3. Verdict courant

Régénérer : `python3 tools/verify/verify.py report`

Dernière exécution :

- Branche : `main`
- Verdict déterministe : **FAIL**
- STATE_ID : `f7ca2770f00a92896a680ecf2eb81012baefae9935b80afc44eb6d98da4b2958`
- HEAD : `9aab3e9ec2c0`

| Check | Verdict |
|---|---|
| protected_branch | BLOCKED |
| test: python3 -m pytest tests/extractors/ -q | PASS |
| no-em-dash-in-articles | FAIL |

Interprétation : sur `main`, le gate bloque (branche protégée). Dans le worktree `te-verification-gate`, seul `no-em-dash-in-articles` reste `FAIL`. Corriger les em-dash de `articles/` est le prérequis d'un `PASS` déterministe.

## 4. Limites connues

- Agents `.ts` : chargement réel par Codebuff non validé depuis une session agent.
- `.git` ≈ 72 Mo : blobs des gros fichiers présents dans l'historique (réécriture `git filter-repo` nécessaire pour purger, non faite).
