# Suivi de la boucle de vérification

> ⚠️ **OBSOLÈTE (2026-08-18)** : le reviewer local Ollama a été supprimé (toute la §5 « benchmark des modèles » et les fixtures sont caduques). Canonique : `docs/besoin_factchecking.md`. À archiver.

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
| 8 | Review-local Ollama (POC + benchmark) | ✅ | 5 modèles benchmarkés (2026-08-18), **qwen3.6:35b retenu** (`think: false` obligatoire). Rapport complet §5 |
| 9 | Implémentation `verify.py gate` | ✅ | `verify.py gate --file <livrable>` implémenté et testé (2026-08-18) : BAD → FAIL 7 findings, témoin → FAIL 3 findings, modèle inexistant → BLOCKED, branche protégée → BLOCKED sans revue. Tests §5.7 |

## 2. Décisions ouvertes

- ~~kebab-case vs snake_case~~ : résolu (2026-08-17) → kebab-case, **majuscules tolérées dans le sujet** (marqueur `KERNEL-*`).
- ~~Périmètre du check naming~~ : résolu (2026-08-17). Le check ne couvre que les **livrables** (types officiels `ARTICLE|HYPER_MATRICE|ARCHITECTURE|SATURATION_AUDIT|REGISTRE|INVESTIGATION`) dans les **dossiers de chantier datés** `YYYY-MM-DD_<sujet>/`, **produits après** `since=2026-08-17`. Le legacy (snake_case, non datés, types internes `MEMO`/`SYNTHESE`/`RESOLUTION`, métadonnées) est hors scope : flagger 2772 fichiers historiques serait du bruit, pas de la vérification.
- ~~Périmètre du check em-dash~~ : résolu (2026-08-17/18). Le check shell `grep articles/` flaggait 107 fichiers / 9 601 occurrences dont 87 hors scope. Remplacé par un **content check** (`forbidden: "—"`, `only_types: [ARTICLE]`, dossiers datés, **sans `since`** : le contrat Phase 3 couvre tout article publié, y compris antérieur). **18 fichiers `_ARTICLE.md` corrigés : 613 em-dash reformulés** (comptage git réel : 613 occurrences retirées, 0 restante ; séparateurs de sources → `:` ; incises → parenthèses/virgules/deux-points). Vérifié : 0 URL modifiée (231/231, perdues ∅), 0 lien cassé.
- **Verdict du reviewer (2026-08-18)** : le premier run du verifier en runtime réel a rendu FAIL avec 5 constats, dont 3 réels corrigés : (1) un `BLOCKED` de naming/content n'escaladait pas le verdict global (une regex invalide verdissait le gate) ; (2) les checks passants étaient muets, un périmètre vide était indistinguable d'une vraie conformité ; (3) le check em-dash protégeait un périmètre **vide** (0 fichier) : `since` excluait les articles publiés et `dir_pattern` exigeait un underscore alors que les dossiers articles utilisent des tirets. Le PASS venait de la vacuité du scope, pas de la conformité. Tout est corrigé dans `verify.py` + `.verify/config.json`.
- **Runtime des `.agents/*.ts`** : à valider en orchestrant un premier chantier dans Codebuff. Le câblage verdict reviewer → certify est fail-safe (retombe sur `BLOCKED`, jamais `PASS`).
- **POC round 4 (2026-08-18) : cause racine du findings.json manquant identifiée et corrigée.** Le write_file de `.verify/findings.json` par l'agent était **rejeté par le runtime** : le format `write_file` Codebuff exige `{path, instructions, content}` (les trois champs), et `truth-verifier.ts` ne passait que `{path, content}` → erreur `Invalid parameters for write_file: [instructions: expected string, received undefined]` dans le log du run (ligne 48 du chat `2026-08-18T06-07-35.357Z`). Conséquence : `findings.json` n'a jamais été écrit par l'agent, et l'agent (haiku) a compensé en écrivant lui-même un `result.json` au format custom (worktree/branch/deliverable/conclusion/no_delivery) au lieu de `verify.py certify` : le certificat contenait les 8 findings mais **pas au format officiel** (pas de state_id, review, state_changed). Corrigé : `instructions` ajouté au write_file. L'extraction elle-même fonctionnait (n=8 findings capturés, verdict FAIL extrait).
- **POC round 5 (2026-08-18) : non concluant, crédits épuisés.** `AI_APICallError: Payment Required` au spawn du reviewer → reviewVerdict `BLOCKED`, nFindings 0, certificat `BLOCKED` au format officiel écrit par `verify.py certify` (le fail-safe a fonctionné : reviewer indisponible → jamais PASS). La preuve du write_file corrigé (findings.json écrit par l'agent) reste à produire : il faudra des crédits Codebuff pour relancer un run complet.
- **Modèle du reviewer local (2026-08-18) : qwen3.6:35b retenu par benchmark** (5 modèles, 2 livrables, rapport complet §5). Options obligatoires : `{think: false, format: json}` (`think:false` indispensable : modèle hybrid-thinking, réponse vide sinon). Ollama 0.32.14, Vulkan iGPU 780M : 20.4 tok/s, ~70 s/revue. Le pairing modèle→options est porté par `verify.py gate` (implémenté, tests §5.7). Les petits modèles (8-12B) sont laxistes (faux PASS sur livrable imparfait), phi4-mini et gemma4:26b éliminés.

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

Interprétation : sur `main`, le gate bloque (branche protégée). Dans le worktree `te-verification-gate`, le verdict déterministe est **PASS complet** : naming conforme, em-dash conforme sur les **67 livrables ARTICLE** du périmètre (18 fichiers corrigés, 613 occurrences reformulées). Les artefacts hors scope (05_ARTICLE, PLAN-CORRECTION, audits, copies) restent exclus du contrat.

**Certificat émis (2026-08-18 06:42 CEST)** dans `.worktrees/te-verification-gate/.verify/result.json` : `verdict: PASS`, `deterministic: PASS`, `review: PASS`, `state_changed: false`, HEAD `b3211bfd`. **⚠️ Ce certificat est INVALIDE comme preuve de revue : `review: PASS` était la valeur par défaut du code (`certify` sans `--review`), pas un verdict de reviewer. Le reviewer avait rendu FAIL au run précédent ; aucune revue indépendante n'a eu lieu sur l'état corrigé. Défaut corrigé (fail-safe : sans `--review`, le certificat est BLOCKED, jamais PASS). La certification complète valide reste à produire avec un vrai verdict reviewer.**

**KERNEL câblé à la gate (2026-08-18)** : étape `19b GATE_VERIFY` ajoutée dans `truth-engine-v2/KERNEL.md` (après le SAVE, avant toute déclaration de livraison) : `python3 tools/verify/verify.py check` sur l'état livré → PASS autorise, FAIL oblige à corriger/re-SAVE/re-run, BLOCKED (branche protégée) impose le worktree. `knowledge.md` DELIVERY GATE alignée. Testé : format KERNEL conforme → PASS (1 fichier scanné) ; snake_case → FAIL détecté.

## 4. Limites connues

- Agents `.ts` : le chargement et l'exécution réels par Codebuff sont **validés** (2026-08-18, run CLI non-interactif dans le worktree). Reste à automatiser la chaîne dans un vrai chantier complet (commit → gate → certify).
- `.git` ≈ 72 Mo : blobs des gros fichiers présents dans l'historique (réécriture `git filter-repo` nécessaire pour purger, non faite).

## 5. Rapport POC review-local : benchmark des modèles (2026-08-18)

### 5.1 Contexte

Le spawn de la chaîne verifier→reviewer est verrouillé sous Freebuff base3-free (preuve §57.8 : main-agent sans `spawn_agents`, zéro appel dans la session 07-55 ; le run POC 08:02:30 était une auto-review du main-agent, pas une revue indépendante). Le chemin free tier passe par un reviewer local Ollama (§57.7 ; premier essai gemma2:9b : 1/6 findings seulement). Objectif : choisir le meilleur modèle local au meilleur compromis performances, pour une commande unique `verify.py gate` (check → review-local → certify).

### 5.2 Environnement

- Ollama **0.31.2 → 0.32.14** (mise à jour 2026-08-18, dernière release stable au 15-08 ; série 0.32 = bump llama.cpp en cours, aucun fix Vulkan 780M explicite).
- Réconciliation des répertoires de modèles : le service systemd (user `ollama`) et un serveur temporaire (user `giak`) utilisaient deux `OLLAMA_MODELS` distincts (18 GB vs 70 GB). Résolu : tous les modèles dans `/usr/share/ollama/.ollama/models` (17 modèles), drop-in `override.conf` : `OLLAMA_VULKAN=1`, `OLLAMA_IGPU_ENABLE=1`, `OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`. GPU vérifié : `ollama ps` → 100% GPU.
- Téléchargements limités à 8 MB/s via proxy local throttlé (pas d'option native Ollama), 70 GB de blobs au total.
- Candidats : gemma4:26b (MoE 26B-A4B, ~4B actifs), qwen3.6:35b (MoE 35B-A3B, ~3B actifs), qwen3:8b, gemma3:12b, phi4-mini (installé). Le 780M (RDNA3, ~80 GB/s DDR5) est limité par la bande passante : les MoE sont le sweet spot (19-22 tok/s rapportés vs 4 tok/s pour un dense 28B).

### 5.3 Protocole

- Prompt : ROLE (reviewer hostile et indépendant, verdict PASS/FAIL/BLOCKED) + CONTRACT (extraits canoniques de knowledge.md/KERNEL.md) + ENUM (7 points C1..C7 tranchés OK/VIOLATION, puis findings) + nom du fichier + livrable.
- `format: json`, temp 0.3, num_predict 4096.
- 2 livrables : **BAD** (livrable POC non conforme, 585 B, 6 violations réelles : STATE=OPEN, pipeline KERNEL absent, structure SIMPLE incomplète, FACT_REGISTRY/URL absents, preuve L4 absente, GAP/STOP_OK non étayés) et **témoin** (fixture synthétique censée conforme).
- Mesures : validité JSON, verdict, nombre/couverture des findings, faux positifs, tok/s, latence.

### 5.4 Résultats

| Modèle | Livrable BAD (6 violations) | Livrable témoin (4 défauts réels) | tok/s | Verdict |
|---|---|---|---|---|
| **qwen3.6:35b** (`think:false`) | FAIL, 6/6 points (stable 3/3) | FAIL, 4/4 (stable 3/3) | 21.3 / 18.3 | **RETENU** (seul à ne pas faux-PASS le témoin) |
| qwen3:8b | FAIL, 6/6 findings correctes | PASS (laxiste : 4 défauts manqués) | 11.4 | Risque faux PASS |
| gemma3:12b | FAIL, 6/6 findings correctes | PASS (laxiste) | 7.4 | Risque faux PASS |
| phi4-mini | FAIL, 3 findings seulement | FAIL incohérent (violation C2 sans finding, pipeline pourtant présent) | 22.4 | Éliminé |
| gemma4:26b | Dégénéré (boucle de répétition « section-section… », invente C10, clés dupliquées, JSON sous-terminé) | — | 17.1 | Éliminé |

Les 4 défauts réels du témoin (vérité terrain) :

1. ANALYZE annonce « 15 symboles scorés » mais n'en liste que 3 (HONESTY, VERACITY, UNCERTAINTY) → C2.
2. URLs = pages de liste (`lemonde.fr/archives/...`, `ina.fr/video/...`), pas des locators vers des documents individuels → C4.
3. « aucun contre-exemple trouvé » : assertion non démontrable (aucune méthode de recherche ni liste de tentatives) ; recoupement ≥2 familles non prouvé (dépêches AFP partagées entre Le Monde et INA) → C5.
4. SRC-003 « livre d'histoire de référence, page 45 » : placeholder sans titre, auteur, éditeur → source irrécupérable → C7.

Variance figée (2 séries de 3 runs par livrable, 2026-08-18, temp 0.3 ; artefacts `tools/verify/fixtures/variance_bad_qwen3.6_35b.json` + `variance_temoin_qwen3.6_35b.json`, findings complets versionnés) : qwen3.6:35b rend **FAIL sur les 6 runs versionnés, sans aucun faux PASS**. Les étiquettes sont stables : 6/6 points sur BAD, 4/4 sur le témoin, 3 runs sur 3 chacun. L'audit du texte des findings corrige la première lecture : **le raisonnement sous les étiquettes est instable**. Sur le témoin, la raison de C2 n'est correcte que 1 run sur 3 (run 2 hallucine « registres LEAD/CLAIM/EVIDENCE omis » alors qu'ils sont présents ; run 3 sous-compte « un seul symbole HONESTY » alors que la fixture en liste 3). Sur BAD, run 3 qualifie « FCT-001 » de « format invalide » alors que c'est le format requis (l'invalide est F-001). Le « 3/4 (C2 manqué) » et la finding hallucinée « Blanchard publié en 2021 » du run unique versionné (`benchmark_results.json`, 2026-08-18) étaient des outliers non reproductibles (0/3 chacun). Le faux positif C6 (horodatage) est intermittent : observé 1/3 dans une première série, 0/3 dans la série versionnée. Conséquence : le verdict est stable et sûr, mais **flagger le bon point n'implique pas la bonne raison** ; chaque finding est advisory (D5/D6) et son évidence doit être recoupée avant correction du livrable.

### 5.5 Enseignements

1. **Rigueur = feature, laxisme = faux PASS.** qwen3.6:35b FAIL les deux livrables (jamais de faux PASS), là où les modèles 8-12B passent le témoin imparfait. Un faux PASS est le pire échec pour un moteur de vérité (« jamais faux PASS »). La rigueur du 35B-A3B l'emporte sur la vitesse des petits modèles. Nuance de l'audit des findings : les étiquettes sont stables (4/4 témoin, 6/6 BAD) mais le raisonnement ne l'est pas (C2 expliqué correctement 1 run sur 3, halluciné ou sous-compté sinon) : la sortie est fiable pour le VERDICT, pas pour l'évidence de chaque finding (D5/D6).
2. **`think: false` obligatoire** pour qwen3.6 (hybrid-thinking : sans cette option, réponse vide malgré 695 tokens générés).
3. **gemma4:26b non fiable** sur prompt structuré long malgré `format: json` (dégénérescence en boucle). Ne pas le réutiliser en reviewer.
4. **L'hybride se confirme** : les vérifs mécaniques (STATE, KERNEL, SIMPLE, FACT_REGISTRY, horodatage) sont déterministes et passeront par `verify.py check` ; le LLM (qwen3.6:35b) se concentre sur le sémantique (fabrication L4, locators, assertions indémontrables) — domaine où il est redoutable (findings 3 et 4). L'audit des findings le confirme : C2 (comptage des 15 symboles) est mécanique, et le LLM le sous-compte ou l'hallucine 2 runs sur 3 sur le témoin : C2 est un candidat de plus pour la couche déterministe, pas pour le LLM.
5. **Fixtures de non-régression versionnées** : `tools/verify/fixtures/` (BAD + témoin + `benchmark_review_local.py` + `benchmark_results.json` + `benchmark.log`). Rejouable : `python3 tools/verify/fixtures/benchmark_review_local.py`. Un reviewer correct doit FAILER les deux livrables.
6. **Coût** : ~70 s/revue à 20.4 tok/s (prompt ~1,5K tokens, sortie ~700) → acceptable pour un gate.
7. **Le nom de fichier doit être passé dans le prompt** : C6 (horodatage) n'est pas vérifiable sinon.

### 5.7 Tests d'acceptation du gate (2026-08-18)

`verify.py gate` implémenté (étape 9) et exécuté en worktree propre (branche `te-gate-acceptance`).

| # | Test | Résultat |
|---|---|---|
| AC-01 | gate sur BAD (6 violations) | ✅ verdict FAIL, 7 findings, `state_changed:false` |
| AC-02 | gate sur témoin (4 défauts) | ✅ verdict FAIL, 3 findings |
| AC-04 | Ollama indisponible (`--model nonexistent:999` → 404) | ✅ verdict BLOCKED, `review_note` « Ollama injoignable » |
| AC-04b | check non PASS (branche protégée `main`) | ✅ verdict BLOCKED, aucune revue (`review_note` explicite) |
| AC-06 | `think:false` présent (sinon qwen3.6:35b répond vide → BLOCKED) | ✅ implicite : la revue BAD a rendu du JSON valide |
| AC-07 | `node --check` des `.agents/*.ts` inchangé | ✅ aucune modification des agents |
| AC-08 | fixtures versionnées et rejouables | ✅ `tools/verify/fixtures/benchmark_review_local.py` |

AC-03 exécuté (2026-08-18) : livrable conforme fabriqué (`fixture_CONFORME.md`) → **FAIL** malgré `deterministic: PASS` : le reviewer false-FAIL. Détail et cause racine §5.8.

### 5.8 Chemin PASS : constat décisif (2026-08-18)

Un livrable SIMPLE réellement conforme a été fabriqué (`tools/verify/fixtures/fixture_CONFORME.md`) : STATE=FINAL, 15 symboles scorés, registres LEAD/CLAIM/EVIDENCE, FACT_REGISTRY_V1, deux sources réellement fetchées (éditeur Nouveau Monde + recension La Vie des Idées), recoupement 2 familles, contre-exemple cherché et documenté. Le check déterministe rend **PASS** (naming, em-dash, tests, horodatage non futur).

Le reviewer `qwen3.6:35b` rend **FAIL** sur 7 runs successifs, avec un faux positif DIFFÉRENT à chaque fois :

1. « registres LEAD/CLAIM/EVIDENCE absents de la trace » (faux : présents, ordre canonique).
2. idem (reproductible).
3. idem.
4. « 2026 = date future » (cutoff du modèle antérieur à 2026).
5. « divergence de 9 min entre création 17:09 et revue 17:18 » (confond heure de création et heure de revue).
6. « le sujet ne doit pas contenir de tirets » (méconnaît la convention kebab-case).
7. « l'éditeur est L'Harmattan, pas Nouveau Monde ; La Vie des Idées n'a pas recensé l'ouvrage » (hallucination : l'éditeur est Nouveau Monde et la recension existe, tous deux fetchés en HTTP 200).
8. « 14 symboles au lieu de 15 » (erreur de comptage).

Conséquence : le chemin PASS est inatteignable avec ce reviewer. Le gate est SÛR (jamais de faux PASS, la propriété critique tient) mais le reviewer est un générateur de faux FAIL. Cause racine : il juge contre un contrat résumé, sans accès aux fichiers réels (KERNEL, SYMBOLS, convention de nommage), sans horloge ni outils, avec un cutoff antérieur à 2026, et le rôle « hostile » amplifie les nitpicks hallucinés.

Correctifs appliqués dans `verify.py` (réduisent la surface, ne résolvent pas le fond) :
- horodatage (C6) déplacé en contrôle déterministe `check_deliverable_timestamp` (non-futur), retiré du prompt LLM ; points LLM ramenés de C1-C7 à C1-C6 ;
- date de référence système injectée dans le prompt (le reviewer n'a pas d'horloge) ;
- fixture conforme versionnée (`fixture_CONFORME.md`) pour non-régression.

Le PASS ne sera opérationnel qu'avec un reviewer capable de juger le contenu sans halluciner : modèle plus fort, accès aux fichiers de contrat, ou validation humaine du verdict.

### 5.6 Références

- Write-back Mnemolite : décision `3d93c3c2-5bae-4068-a07b-b1dfabe54199` (tags : verify, ollama, review-local, benchmark, model-selection, qwen3.6-35b).
- Scripts POC historiques (non versionnés, volatils) : `/tmp/opencode/benchmark_review_local.py`, `debug_full.py`, `final_qwen_gemma.py`, `fixture_conforme.md`.
- Artefact canonique versionné : `tools/verify/fixtures/benchmark_results.json` + `benchmark.log` (run unique 2026-08-18 via `benchmark_review_local.py`).
- Variance figée (2 séries de 3 runs/livrable, findings complets) : `tools/verify/fixtures/variance_bad_qwen3.6_35b.json` + `variance_temoin_qwen3.6_35b.json`.
- Spec révisée : `docs/superpowers/specs/2026-08-18-gate-verification-review-local-design.md`.
