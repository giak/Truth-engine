# Design — Spawn de spécialistes (thinker/researcher) dans la boucle de vérification

> Date : 2026-08-18. Statut : validé en brainstorm.
> Contexte : `docs/boucle_de_verification.md` (§11-13, AC-07/08, §55), `docs/architecture_verification.md`, `docs/suivi_verification.md`.

## 1. Problème

Le cahier des charges impose `REVIEWER => MAY_SPAWN[THINKER, RESEARCHER]` (§55). L'état réel : `truth-reviewer.ts` déclare `spawnableAgents: []` (commentaire V1 : « les spécialistes seront ajoutés une fois leurs identifiants vérifiés »). Le reviewer juge seul : le raisonnement profond (architecture, causalité, cas limites, arbitrage conceptuel) et la vérification de faits externes (sources, documentation, APIs) se font dans sa propre tête, avec les biais de son propre modèle. Deux défauts :

1. **Erreurs corrélées** : le reviewer juge et raisonne avec le même modèle, sans seconde opinion sur les points difficiles.
2. **Faits externes non sourcés** : le fact-check d'une affirmation dépendante du web repose sur la connaissance interne du reviewer, pas sur une recherche dédiée et traçable.

## 2. Décisions de design (validées en brainstorm, 2026-08-18)

| # | Décision | Valeur |
|---|---|---|
| D1 | Set de spécialistes | Deux agents locaux : `truth-thinker`, `truth-researcher` dans `.agents/` |
| D2 | Déclenchement | On-demand pur : contrat dans le prompt du reviewer, jamais systématique |
| D3 | Fail-safe spawn refusé | Le reviewer juge de la matérialité : secours matériel non résolu → `BLOCKED` ; non matériel → il juge seul |
| D4 | Contrat de sortie | Advisory structuré ; attribution `source` dans les findings du reviewer ; le spécialiste ne rend JAMAIS de verdict de gate |
| D5 | Modèles | thinker = `z-ai/glm-5.2` (diversification), researcher = `deepseek/deepseek-v4-flash` (léger). Catalogue gratuit, zéro crédit |
| D6 | Livrable | Spec puis plan d'implémentation, code dans un chantier worktree séparé |

## 3. Architecture

```
verify.py check ──► PASS ──► truth-reviewer (clean-room, juge unique)
                                  │
                    ┌─────────────┴─────────────┐
                    │ on-demand, 1 à la fois     │
                    ▼                           ▼
            truth-thinker                 truth-researcher
            z-ai/glm-5.2                  deepseek/deepseek-v4-flash
            raisonnement profond          faits externes sourcés
                    │                           │
                    └─────────────┬─────────────┘
                                  ▼
            avis ADVISORY {verdict_advice, analysis, findings|evidence}
                                  │
                                  ▼
            reviewer intègre dans SES findings (attribution source)
                                  │
                                  ▼
            verify.py certify --review <verdict reviewer> --findings-file
```

- Depth maximale : 1. Un spécialiste ne spawn rien (`spawnableAgents: []`).
- Un seul spécialiste à la fois, jamais en parallèle.
- Le verdict de gate (PASS/FAIL/BLOCKED) n'existe que dans la sortie du reviewer et dans `verify.py`.

## 4. truth-thinker.ts (nouveau)

Rôle : second avis cognitif sur les points qui engagent le jugement.

| Propriété | Valeur |
|---|---|
| `id` / `displayName` | `truth-thinker` / `Truth Thinker` |
| `model` | `z-ai/glm-5.2` |
| `includeMessageHistory` | `false` (hérite du contexte clean-room du reviewer) |
| `toolNames` | `read_files`, `code_search`, `find_files`, `read_docs`, `set_output`, `end_turn` (aucune écriture, aucun terminal, aucun web) |
| `spawnableAgents` | `[]` |
| `outputMode` | `structured_output` |

Schéma de sortie (advisory, jamais de verdict de gate) :

```json
{
  "verdict_advice": "SUPPORT | REFUTE | UNRESOLVED",
  "analysis": "raisonnement complet, hypothèses, cas limites",
  "findings": [
    { "location": "fichier:ligne", "problem": "...", "evidence": "..." }
  ]
}
```

Le `findings` du thinker liste les défauts ou les points de vigilance qu'il juge matériels ; le reviewer décide de les retenir, les rejeter ou les reformuler.

## 5. truth-researcher.ts (nouveau)

Rôle : vérification de faits externes (source primaire, documentation, API, chiffre, URL).

| Propriété | Valeur |
|---|---|
| `id` / `displayName` | `truth-researcher` / `Truth Researcher` |
| `model` | `deepseek/deepseek-v4-flash` |
| `includeMessageHistory` | `false` |
| `toolNames` | `read_files`, `code_search`, `find_files`, `read_docs`, `web_search`, `set_output`, `end_turn` (aucune écriture, aucun terminal) |
| `spawnableAgents` | `[]` |
| `outputMode` | `structured_output` |

Schéma de sortie :

```json
{
  "verdict_advice": "SUPPORT | REFUTE | UNRESOLVED",
  "analysis": "synthèse du fact-check",
  "evidence": [
    { "claim": "affirmation vérifiée", "source": "URL ou doc", "status": "CONFIRMED | REFUTED | UNVERIFIABLE" }
  ]
}
```

Contraintes du prompt : protocole mnemolite-mem-first si les outils MCP sont disponibles au spawn (recherche mémoire d'abord, web seulement après cache miss, write-back après recherche aboutie) ; source obligatoire pour toute affirmation ; `UNVERIFIABLE` si la source est inaccessible, jamais d'estimation de probabilité.

## 6. truth-reviewer.ts (modifications)

| Propriété | Avant | Après |
|---|---|---|
| `spawnableAgents` | `[]` | `['truth-thinker', 'truth-researcher']` |
| `instructionsPrompt` | contrat de verdict seul | + contrat de déclenchement, d'intégration et de matérialité (§7-8) |
| le reste | inchangé | inchangé |

`truth-verifier.ts` : inchangé. Le verifier lit le verdict et les findings du reviewer ; les avis de spécialistes ne sont jamais parsés par le verifier. `findings.json` reste une liste JSON libre : le champ `source` ajouté aux items est toléré par `verify.py certify` (aucun schéma strict).

## 7. Contrat de déclenchement et d'intégration (instructionsPrompt du reviewer)

Règles ajoutées au prompt du reviewer, dans cet ordre :

1. **Déclenchement on-demand** : spawn `truth-thinker` uniquement si le verdict dépend d'un raisonnement architectural, d'une analyse causale, d'un cas limite ou d'un arbitrage conceptuel. Spawn `truth-researcher` uniquement si le verdict dépend d'un fait externe (source, documentation, API, chiffre, URL, affirmation sensible). Jamais de spawn systématique, jamais de spawn « pour améliorer la qualité » sans doute concret.
2. **Un seul spécialiste à la fois** : si les deux questions se posent, traiter la plus matérielle d'abord ; le second spawn n'a lieu que si le premier avis ne lève pas le doute.
3. **Intégration** : le reviewer est seul responsable du verdict final. Il intègre les contributions des spécialistes dans ses propres findings avec attribution : `"source": "thinker"` ou `"source": "researcher"` sur chaque item retenu. Un avis peut être rejeté, contredit ou jugé non matériel ; un rejet motivé n'est pas un finding.
4. **Traçabilité** : quand un avis de spécialiste change ou confirme le verdict, le reviewer le mentionne dans un finding de type note (`problem` préfixé `NOTE:`) avec la source, pour que le certificat garde la trace de la consultation.

## 8. Fail-safe matérialité (spawn refusé ou indisponible)

Un spawn de spécialiste peut échouer : verrou runtime (base3-free), modèle indisponible, erreur d'infrastructure. Règle :

- Le reviewer décide si le secours était **matériel** au verdict : le doute portait sur un point dont la résolution exigeait le spécialiste et il n'est pas résolu autrement.
- **Matériel** → verdict `BLOCKED` (un finding le documente). Jamais de PASS sur un doute matériel non résolu.
- **Non matériel** → le reviewer juge seul, et le mentionne dans un finding de type note (`NOTE: spawn thinker/researcher indisponible, jugé non matériel`).

Cohérence avec la sémantique `BLOCKED` existante : « source indispensable inaccessible → BLOCKED ». Le spécialiste étant optionnel par design, seule sa nécessité matérielle bloque.

## 9. Réalité runtime et dégradation

Prouvé au §57.8 de `docs/boucle_de_verification.md` : sous Freebuff actuel (templates base3-free, depuis le 13 août 2026), le main-agent n'expose pas `spawn_agents` ; le verrou est côté binaire client, pas une capacité retirée du runtime. Nos agents locaux restent déclarés spawnables dans les templates base2-free et base-chat.

Conséquences pour ce design :

- **Spawn disponible** (Codebuff payant, base2-free, base-chat) : la chaîne complète fonctionne, reviewer → spécialiste → intégration.
- **Spawn indisponible** (Freebuff base3-free) : la chaîne dégrade en « reviewer juge seul », **sans BLOCKED automatique** (les spécialistes sont optionnels). La règle de matérialité (§8) s'applique seulement si le reviewer a tenté un spawn et qu'il a échoué.
- **Ne rien casser** : si Freebuff rouvre l'accès au spawn, la boucle fonctionnera sans modification des agents.

## 10. Mises à jour des 3 docs

- `docs/architecture_verification.md` : composants ajoutés au tableau 2.2 ; schéma 2.5 enrichi (couche consultation) ; exigences §1.4 inchangées ; note de dégradation runtime dans les limites (§5).
- `docs/boucle_de_verification.md` : §11-13 et AC-07/08 passent de « prévu » à « spécifié » (référence au design) ; nouveau §57.9 documentant les agents réels, les slugs, la matérialité et la dégradation ; §55 `REVIEWER => MAY_SPAWN[THINKER, RESEARCHER]` passe de « prévu » à « réalisé ».
- `docs/suivi_verification.md` : ligne roadmap (étape 8 : spécialistes) ; décisions D1-D6 en §2 ; verdict courant inchangé.

## 11. Tests et critères d'acceptation

1. `node --check` sur `truth-thinker.ts`, `truth-researcher.ts`, `truth-reviewer.ts` modifié.
2. Les slugs `z-ai/glm-5.2` et `deepseek/deepseek-v4-flash` appartiennent au catalogue gratuit (§57.1) : revalidation au moment de l'implémentation.
3. `findings.json` avec items portant `source` : `verify.py certify` accepte et embarque sans erreur (test unitaire).
4. Test d'intégration en worktree : spawn réel si le runtime le permet ; sinon test du chemin dégradé (reviewer juge seul, matérialité documentée).
5. Scénario AC-07 (doute conceptuel) : thinker spawné, avis intégré avec attribution, verdict du reviewer inchangé dans la grammaire.
6. Scénario AC-08 (fait externe douteux) : researcher spawné, preuve sourcée, verdict du reviewer conforme.
7. Scénario fail-safe : spawn refusé simulé → reviewer rend BLOCKED si matériel, jugement seul si non matériel.

## 12. Hors périmètre (YAGNI)

- Pas de journal des consultations persisté (`.verify/consultations.json`) en V1 : la trace vit dans les findings attribués.
- Pas de reviewers spécialisés par domaine (contrat, typographie, sourcing séparés) : le researcher couvre le sourcing, le thinker le reste.
- Pas de parallélisme de spawn, pas de profondeur > 1.
- Pas de changement de `truth-verifier.ts`, pas de changement de `verify.py` (hors test de tolérance du champ `source`).
- Pas de modification du KERNEL : les spécialistes restent dans la couche de gate, au-dessus du pipeline (§57, verdict V1 inchangé).