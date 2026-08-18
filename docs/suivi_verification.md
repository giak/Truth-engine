# Suivi de la boucle de vérification

> Tableau de bord du chantier. Cahier des charges : `docs/boucle_de_verification.md`.
> Le « verdict courant » est régénérable à tout moment : `python3 tools/verify/verify.py report`.

## 1. État d'avancement (roadmap §52)

| # | Étape | Statut | Preuve / reste |
|---|---|---|---|
| 0 | Assainissement minimal | ✅ | `knowledge.md` consolidé (canonique), `AGENTS.md` pointeur, nommage tranché : kebab-case |
| 1 | `truth-reviewer.ts` | ✅ écrit | `.agents/truth-reviewer.ts`, `node --check` OK. Runtime non validé |
| 2 | Gate déterministe | ✅ | `tools/verify/verify.py` : `check` / `state-id` / `certify` / `report` |
| 3 | STATE_ID | ✅ testé | invalidation post-modif vérifiée (fichier non suivi + worktree) |
| 4 | `truth-verifier.ts` | ✅ écrit | `.agents/truth-verifier.ts`, `node --check` OK. Runtime non validé |
| 5 | DELIVERY GATE | ✅ | section ajoutée dans `knowledge.md` |
| 6 | Worktrees | ✅ | `tools/verify/worktree-new.sh`, démo `.worktrees/te-verification-gate` |
| 7 | Enforcement orchestrateur | ✅ | runtime Codebuff validé (2026-08-18) : spawn verifier → reviewer → `result.json` écrit. Le reviewer a attrapé un vrai bug du moteur (escalade BLOCKED) et une fausse assurance (périmètre em-dash vide). Voir §2 |

## 2. Décisions ouvertes

- ~~kebab-case vs snake_case~~ : résolu (2026-08-17) → kebab-case, **majuscules tolérées dans le sujet** (marqueur `KERNEL-*`).
- ~~Périmètre du check naming~~ : résolu (2026-08-17). Le check ne couvre que les **livrables** (types officiels `ARTICLE|HYPER_MATRICE|ARCHITECTURE|SATURATION_AUDIT|REGISTRE|INVESTIGATION`) dans les **dossiers de chantier datés** `YYYY-MM-DD_<sujet>/`, **produits après** `since=2026-08-17`. Le legacy (snake_case, non datés, types internes `MEMO`/`SYNTHESE`/`RESOLUTION`, métadonnées) est hors scope : flagger 2772 fichiers historiques serait du bruit, pas de la vérification.
- ~~Périmètre du check em-dash~~ : résolu (2026-08-17/18). Le check shell `grep articles/` flaggait 107 fichiers / 9 601 occurrences dont 87 hors scope. Remplacé par un **content check** (`forbidden: "—"`, `only_types: [ARTICLE]`, dossiers datés, **sans `since`** : le contrat Phase 3 couvre tout article publié, y compris antérieur). **13 articles corrigés : 612 em-dash reformulés** (séparateurs de sources → `:` ; incises → parenthèses/virgules/deux-points). Vérifié : 0 URL modifiée, 0 lien cassé.
- **Verdict du reviewer (2026-08-18)** : le premier run du verifier en runtime réel a rendu FAIL avec 5 constats, dont 3 réels corrigés : (1) un `BLOCKED` de naming/content n'escaladait pas le verdict global (une regex invalide verdissait le gate) ; (2) les checks passants étaient muets, un périmètre vide était indistinguable d'une vraie conformité ; (3) le check em-dash protégeait un périmètre **vide** (0 fichier) : `since` excluait les articles publiés et `dir_pattern` exigeait un underscore alors que les dossiers articles utilisent des tirets. Le PASS venait de la vacuité du scope, pas de la conformité. Tout est corrigé dans `verify.py` + `.verify/config.json`.
- **Runtime des `.agents/*.ts`** : à valider en orchestrant un premier chantier dans Codebuff. Le câblage verdict reviewer → certify est fail-safe (retombe sur `BLOCKED`, jamais `PASS`).

## 3. Verdict courant

Régénérer : `python3 tools/verify/verify.py report`

Dernière exécution :

- Branche : `main`
- Verdict déterministe : **BLOCKED**
- STATE_ID : `c3f7b1a95d726e9e5ddf0fcbf103fab851935294ec52e7f0b9bcd85fbe0f0ade`
- HEAD : `f16acc29ecf8`

| Check | Verdict |
|---|---|
| protected_branch | BLOCKED |
| test: python3 -m pytest tests/extractors/ -q | PASS |
| naming | PASS |
| no-em-dash-in-published-articles | PASS (67 fichiers scannés, 0 occurrence) |

Interprétation : sur `main`, le gate bloque (branche protégée). Dans le worktree `te-verification-gate`, le verdict déterministe est **PASS complet** : naming conforme, em-dash conforme sur les **67 livrables ARTICLE** du périmètre (13 articles corrigés, 612 occurrences reformulées). Les artefacts hors scope (05_ARTICLE, PLAN-CORRECTION, audits, copies) restent exclus du contrat.

**Certificat émis (2026-08-18 06:42 CEST)** dans `.worktrees/te-verification-gate/.verify/result.json` : `verdict: PASS`, `deterministic: PASS`, `review: PASS`, `state_changed: false`, HEAD `b3211bfd`. Première certification complète de la boucle en runtime réel.

## 4. Limites connues

- Agents `.ts` : le chargement et l'exécution réels par Codebuff sont **validés** (2026-08-18, run CLI non-interactif dans le worktree). Reste à automatiser la chaîne dans un vrai chantier complet (commit → gate → certify).
- `.git` ≈ 72 Mo : blobs des gros fichiers présents dans l'historique (réécriture `git filter-repo` nécessaire pour purger, non faite).
