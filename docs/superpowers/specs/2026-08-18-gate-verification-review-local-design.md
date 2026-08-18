# Design — Gate de vérification unifié : `verify.py gate` (check + review-local + certify)

> Date : 2026-08-18. Statut : validé en brainstorm. Version 2.
> Remplace la V1 « spawn spécialistes (thinker/researcher) » (hors cible : l'utilisateur a tranché pour la chaîne reviewer+verifier, pas de thinker).
> Contexte : `docs/boucle_de_verification.md` (§11-13, AC-07/08, §55, §57.1-57.8), `docs/architecture_verification.md`, `docs/suivi_verification.md` (rapport benchmark §5).

## 1. Problème

Le cahier des charges impose une revue finale indépendante : reviewer en contexte neuf, sans historique, sans droit d'écriture (knowledge.md DELIVERY GATE). L'état réel :

1. **Spawn verrouillé en free tier** : sous Freebuff base3-free, le main-agent n'expose pas `spawn_agents` (preuve forensique §57.8 : session 07-55, zéro appel spawn_agents ; le run POC 08:02:30 était une auto-review du main-agent, pas une revue indépendante). La chaîne verifier→reviewer ne tourne que sur Codebuff payant / base2-free / base-chat.
2. **Pas de commande unique scriptable** : `verify.py check` existe (déterministe), mais la revue indépendante dépend d'un runtime avec spawn.
3. **Le POC gemma2:9b a échoué** : 1/6 findings sur le livrable de test (pourtant 6 violations réelles) → le modèle par défaut du §57.7 est disqualifié.

La réponse : une commande unique `verify.py gate` = check déterministe + revue locale Ollama (stateless, clean-room par construction) + certification, avec la chaîne spawn conservée en voie premium. Le benchmark 5 modèles (§5 de suivi) a désigné **qwen3.6:35b**.

## 2. Décisions de design (validées en brainstorm, 2026-08-18)

| # | Décision | Valeur |
|---|---|---|
| D1 | Commande unique | `python3 tools/verify/verify.py gate` : check → review-local → certify. 100 % scriptable, exécutable sans runtime Codebuff |
| D2 | Reviewer local | Ollama **`qwen3.6:35b`** (MoE 35B-A3B, ~3B actifs), appel stateless (prompt complet à chaque requête, aucun historique) = clean-room par construction |
| D3 | Options LLM | mapping modèle→options porté par `verify.py` : `{"think": false, "format": "json"}` pour qwen3.6:35b (`think:false` obligatoire, réponse vide sinon) |
| D4 | Hybride | vérifs mécaniques (STATE, KERNEL, structure SIMPLE, FACT_REGISTRY/URL, horodatage) → déterministe dans `check` ; le LLM ne juge que le sémantique (fabrication L4, locators, assertions indémontrables) |
| D5 | Verdicts | PASS/FAIL/BLOCKED uniquement chez `verify.py` ; la sortie LLM est advisory, sa non-conformité → BLOCKED |
| D6 | Fail-safe | Ollama down, réponse illisible, JSON invalide ou points manquants → BLOCKED, jamais PASS |
| D7 | Spawn premium | chaîne verifier→reviewer conservée pour Codebuff payant / base2-free / base-chat ; dégradation « reviewer juge seul » sinon, sans BLOCKED automatique (les spécialistes sont optionnels) |
| D8 | Fixtures | paire BAD + témoin versionnée sous `tools/verify/fixtures/` comme test de non-régression : un reviewer correct doit FAILER les deux |

## 3. Architecture

```
verify.py gate
  ├─ 1. check (déterministe)
  │      naming / no-em-dash / tests / protected_branch
  │      FAIL ──► arrêt : verdict FAIL (jamais de revue sur livrable non conforme)
  ├─ 2. review-local (Ollama qwen3.6:35b, think:false, format:json)
  │      prompt = ROLE + CONTRACT + ENUM(C1..C7) + nom du fichier + livrable
  │      Ollama down / JSON invalide ──► BLOCKED (jamais PASS)
  ├─ 3. mapping verdict advisory → verdict gate
  │      verdict == "PASS" et check PASS ──► PASS
  │      verdict == "FAIL" ──► FAIL (findings du LLM enregistrés)
  │      verdict inconnu / points incomplets ──► BLOCKED
  └─ 4. certify (.verify/findings.json + .verify/result.json au format officiel)
```

- Un livrable par revue, séquentiel. Le livrable = périmètre du `check` (config `.verify/config.json`).
- Le LLM ne rend jamais de verdict de gate : sa sortie est convertie par des règles déterministes.

## 4. Détails de `verify.py gate`

1. **check** : réutilisation intégrale du check existant (naming, em-dash, tests, branches). Échec → verdict FAIL, aucune étape LLM (pas de revue d'un livrable non conforme).
2. **review-local** : pour chaque livrable du périmètre, appel `/api/generate` Ollama avec le mapping modèle→options (D3). Timeout 300 s, `num_predict` 4096, temp 0.3.
3. **Conversion** : parser JSON strict. Points C1..C7 attendus en `points` (valeurs `OK`/`VIOLATION`), `verdict` advisory, `findings` (location/problem/evidence). Toute anomalie (champ manquant, valeur inconnue, extrait JSON non parsable, sortie tronquée) → BLOCKED avec le motif dans le certificat. **Anti-fausse-précision (knowledge.md §3.5) : le parser est tolérant sur la forme (stripping fences), strict sur la grammaire close des valeurs.**
4. **certify** : écrit `.verify/findings.json` (liste JSON libre, champ `source` toléré) et `.verify/result.json` (format officiel : `deterministic`, `review`, `state_changed`, state_id). Sans `--review` valide, jamais PASS (fail-safe existant conservé).

## 5. Prompt du reviewer local

Trois blocs fixes + le livrable. Le nom de fichier est passé dans le prompt (C6 horodatage non vérifiable sinon).

```
ROLE : reviewer indépendant et hostile, lecture seule, ne répare rien. Verdict PASS/FAIL/BLOCKED.
Interdits : scores, pourcentages, flatterie. Style direct. Uniquement les défauts qui
empêchent rationnellement la livraison dans findings.

CONTRACT : extraits canoniques de knowledge.md et truth-engine-v2/KERNEL.md
- Livrable final : STATE=FINAL, NEXT_ACTION=NONE (« NEVER persist OPEN/PENDING as final »)
- Pipeline KERNEL : ANALYZE §0 (15 symboles narratifs scorés), BIAS_TEST, CRÉDO/SCOPING,
  LEAD_REGISTRY, CLAIM_REGISTRY, EVIDENCE_REGISTRY
- COMPLEXITY=SIMPLE : 5 sections core (RÉSUMÉ EXÉCUTIF, CHRONOLOGIE, DOMAINES, CARTE DES
  PREUVES, PÉRIMÈTRE & LIMITES) + appendices SOURCES et REQUEST_LOG
- Traçabilité : FACT_REGISTRY_V1 (id|epi|tier|url|families|date), FCT-###, source = URL de
  page spécifique cliquable / SRC-ID / locator exact
- L4 (CONFIRMÉ) : L3 + gate EPI=FACT + recherche de contre-exemples + preuves matérielles
  (sources fetchées, recoupement ≥2 familles, FACT_REGISTRY_V1, REQUEST_LOG)
- Horodatage du nom de fichier = date/heure réelle de création (CEST), jamais inventé
- Toute affirmation sans source vérifiable = violation grave

ENUM : procédure obligatoire dans l'ordre
1. Trancher C1..C7 (une ligne par point : C1:OK ou C1:VIOLATION)
   C1 STATE=FINAL ? C2 Pipeline KERNEL ? C3 Structure SIMPLE ? C4 Traçabilité
   (FACT_REGISTRY_V1, FCT-###, URL/locator) ? C5 Preuve matérielle L4 ? C6 Horodatage
   fichier ? C7 Autre fabrication ?
2. Findings UNIQUEMENT pour les VIOLATION (location + problem + evidence)
3. Verdict : FAIL si ≥1 VIOLATION, sinon PASS, BLOCKED si illisible
RÉPONDS UNIQUEMENT EN JSON : {"points": {...}, "verdict": "...", "findings": [...]}
```

## 6. Mapping modèle → options

| Modèle | Options | Statut |
|---|---|---|
| `qwen3.6:35b` | `{"think": false, "format": "json"}` | **Défaut** (benchmark §5, 20.4 tok/s) |
| `qwen3:8b`, `gemma3:12b` | `{"format": "json"}` | Possible mais laxiste (faux PASS sur livrable imparfait) : à n'utiliser qu'en secours, jamais seul |
| `phi4-mini` | `{"format": "json"}` | Éliminé (3/6 findings, faux FAIL incohérent) |
| `gemma4:26b` | — | Éliminé (dégénérescence, JSON cassé) |
| `gemma2:9b` | `{"format": "json"}` | Éliminé (1/6 findings, §57.7) |

> Preuve versionnée (2026-08-18) : `tools/verify/fixtures/benchmark_results.json` + `benchmark.log` (rejouable via `benchmark_review_local.py`). Le re-run donne qwen3.6:35b = 6/6 points sur BAD et **3/4 sur le témoin** (C2 manqué), avec une finding hallucinée sur BAD (date 2011 → 2021). Le « 4/4 » antérieur n'était pas persisté. Le modèle reste retenu (seul à ne pas faux-PASS le témoin), mais sa sortie est advisory (D5/D6) : chaque finding doit être recoupé.

Le mapping vit dans une table de `verify.py` (model → options). Tout modèle inconnu : options par défaut `{"format": "json"}` et avertissement dans le certificat.

## 7. Réalité runtime et dégradation

Prouvé au §57.8 : sous Freebuff base3-free, le verrou spawn est côté binaire client. Conséquences :

- **`verify.py gate`** : fonctionne partout (Ollama + Python), c'est le chemin par défaut.
- **Spawn disponible** (Codebuff payant, base2-free, base-chat) : la chaîne `truth-verifier` → `truth-reviewer` reste opérationnelle, avec les agents `.agents/*.ts` existants. Le verifier peut invoquer le gate après la revue, ou certifier la revue spawnée.
- **Spawn indisponible** (Freebuff base3-free) : dégradation « reviewer juge seul » via review-local. Pas de BLOCKED automatique (les spécialistes sont optionnels par design).
- **Ne rien casser** : si Freebuff rouvre le spawn, la boucle spawnée fonctionne sans modification.

## 8. Mises à jour des 3 docs

- `docs/architecture_verification.md` : composant review-local ajouté au tableau 2.2 ; schéma 2.5 enrichi (couche gate unifié) ; note de dégradation runtime dans les limites (§5).
- `docs/boucle_de_verification.md` : §57.7 passe de « prévu » à « spécifié » (référence à cette spec + rapport benchmark §5) ; nouveau §57.9 documentant la commande `gate`, le mapping modèle→options et la dégradation.
- `docs/suivi_verification.md` : §5 (rapport benchmark) déjà rédigé ; roadmap ligne 8 ajoutée ; étape 9 (implémentation gate) à suivre.

## 9. Tests et critères d'acceptation

1. `verify.py gate` sur le livrable BAD des fixtures → verdict FAIL, findings ≥ 5, certificat au format officiel.
2. `verify.py gate` sur le livrable témoin → verdict FAIL (le témoin est imparfait par construction : 4 défauts réels à détecter par le LLM).
3. `verify.py gate` sur un livrable réellement conforme → PASS. **Résultat réel (2026-08-18) : FAIL, voir `docs/suivi_verification.md` §5.8** : le reviewer `qwen3.6:35b` false-FAIL systématiquement (hallucination d'éditeur, erreur de comptage des symboles, rejet des dates 2026). Le chemin PASS n'est pas opérationnel avec ce reviewer ; l'horodatage (C6) a été déplacé en contrôle déterministe (`check_deliverable_timestamp`) et les points LLM ramenés de C1-C7 à C1-C6.
4. Ollama down simulé → BLOCKED, jamais PASS.
5. Sortie LLM non JSON / points incomplets → BLOCKED, motif dans le certificat.
6. `think:false` manquant sur qwen3.6:35b → BLOCKED détecté par le parseur (réponse vide), test unitaire du mapping.
7. `node --check` inchangé : les `.agents/*.ts` ne sont pas modifiés par cette spec (la chaîne spawnée reste identique).
8. Fixtures versionnées sous `tools/verify/fixtures/` et intégrées à la suite de tests.

## 10. Hors périmètre (YAGNI)

- Pas de deuxième LLM en « double revue » (deux modèles) en V1 : le benchmark a montré que les petits modèles sont laxistes, pas complémentaires.
- Pas de journal des consultations persisté (`.verify/consultations.json`) : la trace vit dans `findings.json` et `result.json`.
- Pas de modification des `.agents/truth-verifier.ts` / `truth-reviewer.ts` ni de la chaîne spawnée.
- Pas de changement du KERNEL : le gate reste dans la couche de vérification, au-dessus du pipeline.
- Pas de reviewers spécialisés par domaine (le 35B-A3B couvre le sourcing et le sémantique).
