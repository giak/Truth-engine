# Architecture de la boucle de vérification

> Spécification de besoin et d'architecture de la boucle de vérification implémentée dans Truth Engine.
> Complémentaire au cahier des charges (`docs/boucle_de_verification.md`) et au tableau de bord (`docs/suivi_verification.md`).
> Ce document décrit l'état **réel** du système au 2026-08-18, pas un état projeté.
> Exception déclarée : le mode `verify.py gate` (review-local Ollama) est **spécifié mais non implémenté** à cette date (seuls `check`, `state-id`, `report`, `certify` existent dans le code). Toute mention de `gate` ci-dessous est une spécification, pas un état de code. Voir EX2, EX11, §2.2, §2.3.

---

## 1. Besoin

### 1.1 Le problème

Truth Engine produit des livrables (investigations, articles, matrices) par des agents LLM. Historiquement, la vérification reposait sur l'obéissance conversationnelle : des consignes (« double check », « tu es sûr ? ») dans les prompts. Quatre faiblesses structurelles :

1. **Probabiliste** : l'agent peut omettre de vérifier, ou mentir par omission.
2. **Auto-évaluation** : l'auteur vérifie son propre travail, sans séparation des rôles.
3. **Sans preuve** : aucun état technique ne bloque la livraison d'un travail modifié après vérification.
4. **Non reproductible** : deux sessions peuvent produire deux verdicts différents sur le même état.

### 1.2 Le principe

Transformer la consigne rhétorique (« l'agent *devrait* vérifier ») en propriété du workflow (« l'agent **ne peut pas** livrer un travail non vérifié »).

```
UNVERIFIED ──► VERIFY ──► PASS ──► DELIVERABLE
                │
                └── FAIL/BLOCKED ──► correction ou blocage déclaré
```

### 1.3 Les deux invariants

| Invariant | Formulation | Mécanisme |
|---|---|---|
| I1 | `NO VERIFIED STATE => NO FINAL DELIVERY` | Gate obligatoire avant livraison, verdict PASS requis |
| I2 | `CHANGE AFTER PASS => PASS INVALID` | STATE_ID : toute modification de l'état (HEAD, diff, fichiers non suivis) change le hash et invalide le certificat |

### 1.4 Exigences

| ID | Exigence | Vérifié par |
|---|---|---|
| EX1 | Le verdict est déterministe pour tout ce qui est mécanique | `verify.py check` (branche, tests, nommage, contenu interdit) |
| EX2 | Le jugement sémantique est confié à un reviewer en contexte neuf | spawn : `.agents/truth-reviewer.ts` (`includeMessageHistory: false`) ; local : review-local Ollama stateless (`verify.py gate`, **spécifié non implémenté**) |
| EX3 | Trois verdicts seulement : PASS, FAIL, BLOCKED. Jamais de score | grammaire des verdicts dans `verify.py` |
| EX4 | La certification exige un verdict de reviewer explicite | `certify --review` ; défaut `BLOCKED` (fail-safe) |
| EX5 | Le chantier est isolé de `main` | worktree + branches protégées |
| EX6 | Toute modification après PASS invalide le PASS | STATE_ID recomputé à chaque `check` et `certify` |
| EX7 | Le périmètre des checks est déclaratif et configurable | `.verify/config.json` (dirs, dir_pattern, only_types, since, exclude) |
| EX8 | Les périmètres vides sont détectables, pas confondus avec la conformité | chaque PASS émet son nombre de fichiers scannés |
| EX9 | Une erreur de configuration bloque, elle ne verdit pas | escalade FAIL > BLOCKED > PASS dans `run_checks` |
| EX10 | Le pipeline KERNEL intègre la gate avant toute livraison | KERNEL 19a GATE_VERIFY, 19b FACT_WRITEBACK conditionnel |
| EX11 | La revue locale est stateless (clean-room par construction) | `verify.py gate` (**spécifié non implémenté**) : prompt complet à chaque appel Ollama, aucun historique ; Ollama down ou sortie non conforme → BLOCKED, jamais PASS |

---

## 2. Architecture

### 2.1 Vue d'ensemble

```
                        ┌────────────────────────────────────────────────┐
                        │                 .verify/config.json           │
                        │  protected_branches │ tests │ naming │ content│
                        └───────────────────────┬────────────────────────┘
                                                │
        ┌───────────────────────┐               ▼
        │   truth-verifier.ts   │     ┌──────────────────────────┐
        │  (agent orchestrateur)│────►│   verify.py              │
        │  check → review → cert│     │  check · gate · state-id │
        └──────────┬────────────┘     │  certify · report        │
                   │                  └──────────┬───────────────┘
                   │                             │
                   ▼                             │
        ┌───────────────────────┐      ┌─────────▼──────────────┐
        │  truth-reviewer.ts    │      │  gate = check +        │
        │  (spawn, clean-room,  │      │  review-local (Ollama  │
        │   lecture seule)      │      │  qwen3.6:35b stateless)│
        └───────────────────────┘      │  + certify             │
                                       └────────────────────────┘
                                                │
                        ┌───────────────────────▼───────────────────────┐
                        │              worktree (1 chantier)            │
                        │  .worktrees/<chantier>  · branche non protégée │
                        │  livrable : investigations/, articles/, ...    │
                        └────────────────────────────────────────────────┘
```

### 2.2 Composants

| Composant | Fichier | Rôle |
|---|---|---|
| Moteur déterministe | `tools/verify/verify.py` | checks, STATE_ID, certification, rapport ; `gate` = check + review-local + certify (**spécifié non implémenté** : seuls `check`/`state-id`/`report`/`certify` existent) |
| Configuration | `.verify/config.json` | déclaration des checks et périmètres |
| Agent verifier | `.agents/truth-verifier.ts` | orchestre la chaîne complète dans Codebuff (chemin spawn) |
| Agent reviewer | `.agents/truth-reviewer.ts` | revue LLM indépendante spawnée, sans historique d'auteur |
| Reviewer local | Ollama `qwen3.6:35b` | revue stateless (prompt complet à chaque appel, aucun historique) = clean-room par construction ; options `{think: false, format: json}` (**spécifié non implémenté** : dépend du mode `gate`) |
| Isolateur de chantier | `tools/verify/worktree-new.sh` | 1 chantier = 1 worktree = 1 branche |
| Contrat | `knowledge.md` (DELIVERY GATE) | obligation contractuelle de passer la gate |
| Pipeline | `truth-engine-v2/KERNEL.md` (19a/19b) | intégration de la gate au protocole d'investigation |

### 2.3 Le moteur déterministe (`verify.py`)

```
   check ──► exécute chaque check déclaré ──► aggrège les verdicts
     │                                          FAIL > BLOCKED > PASS
     │                                                │
     │                                                ▼
     │                                   calcule STATE_ID (sha256)
     │                                   head + diff HEAD + untracked
     │                                                │
     │                                                ▼
     │                                   écrit .verify/pending.json
     │                                   exit 0 (PASS) / 1 (FAIL) / 2 (BLOCKED)
     │
   certify --review <V> ──► recompute STATE_ID
     │                        │
     │                        ├── changé  → verdict FAIL (PASS invalidé)
     │                        ├── inchangé + deterministic ≠ PASS → deterministic
     │                        └── inchangé + deterministic = PASS → review
     │                                                │
     │                                                ▼
     │                                   écrit .verify/result.json (certificat)
     │                                   exit 0 / 1 / 2
```

Fail-safe : `certify` sans `--review` émet `BLOCKED`. `NO REVIEW => NO PASS`.

Le bloc `gate` ci-dessous est **spécifié mais non implémenté** au 2026-08-18
(les fixtures et le benchmark sont prêts : `tools/verify/fixtures/`).

   gate ───► check (déterministe) ── FAIL ──► arrêt : verdict FAIL, jamais de revue
             │
             ▼
        review-local (Ollama qwen3.6:35b, think:false, format:json)
             │
             ├── Ollama down / JSON invalide / points manquants → BLOCKED
             ├── verdict advisory FAIL → FAIL (findings enregistrés)
             └── verdict advisory PASS + check PASS → PASS
             │
             ▼
        certify (.verify/findings.json + .verify/result.json au format officiel)

Le verdict LLM est advisory : converti par des règles déterministes dans `verify.py`.
La sortie LLM n'est jamais parsée en confiance (anti-fausse-précision, knowledge.md §3.5) :
forme tolérante (fences), grammaire close stricte (OK/VIOLATION, PASS/FAIL/BLOCKED).

### 2.4 Le STATE_ID (invariant I2)

```
STATE_ID = sha256(
    head=<SHA du commit courant>
    diff=<sha256 du diff non commité>
    untracked=<liste des fichiers non suivis>
)
```

Propriété : toute modification de l'état (commit, édition, ajout de fichier, suppression) change le STATE_ID. Le certificat ne vaut que pour l'état exact au moment du `check`.

### 2.5 Les agents

```
AUTEUR (session courante)          VERIFIER (truth-verifier.ts)      REVIEWER (truth-reviewer.ts)
┌────────────────────┐             ┌──────────────────────┐          ┌──────────────────────┐
│ produit le livrable│             │ 1. verify.py check   │          │ contexte neuf         │
│                    │             │ 2. spawn reviewer    │◄────────►│ includeMessageHistory │
│                    │             │ 3. lit verdict       │          │ : false               │
│                    │             │ 4. certify --review  │          │ lecture seule         │
└────────────────────┘             └──────────────────────┘          │ pas d'écriture        │
                                                                     └──────────────────────┘
```

L'auteur ne certifie pas son propre travail : le verdict de revue vient du reviewer, le certificat est émis par le verifier.

**Deux chemins de revue indépendante :**

- **Spawn** (Codebuff payant, base2-free, base-chat) : `truth-verifier.ts` spawn `truth-reviewer.ts` (contexte neuf, lecture seule), lit le verdict, certifie.
- **Review-local** (Freebuff base3-free, ou hors Codebuff) : `verify.py gate` appelle Ollama `qwen3.6:35b` avec le prompt complet (ROLE + CONTRACT + ENUM C1..C7 + nom du fichier + livrable). Stateless : aucun historique, aucun état partagé → clean-room par construction. Le verrou spawn base3-free est prouvé au §57.8 de `docs/boucle_de_verification.md`.

Le gate ne modifie ni les agents `.ts` ni la chaîne spawnée : si le runtime rouvre le spawn, la boucle complète fonctionne sans changement.

### 2.6 Isolation (worktree)

```
  dépôt principal (main, protégé)          worktree du chantier
┌──────────────────────────────┐          ┌─────────────────────────────┐
│ .git/                        │          │ .worktrees/<chantier>/      │
│ .verify/config.json          │          │ .verify/config.json (copie) │
│ tools/verify/verify.py       │          │ .agents/*.ts (copie)        │
│ knowledge.md                 │          │ investigations/...          │
└──────────────────────────────┘          │ branche <chantier>          │
     ▲                                   └─────────────────────────────┘
     └──── verify.py check sur main → BLOCKED (branche protégée)
```

Le gate refuse `main`/`master` : le travail de chantier se fait dans un worktree dédié, créé par `worktree-new.sh <chantier>`, qui refuse lui-même les noms de branches protégées.

### 2.7 Intégration KERNEL (investigations)

```
KERNEL §0 → 18b (GATE_CHECK G0-G10, FREEZE)
        │
        ▼
§19  SAVE              écriture unique STATE:FINAL
        │
        ▼
§19a GATE_VERIFY       python3 tools/verify/verify.py check
        │                PASS → GATE_VERDICT=PASS, STATE_ID enregistré
        │                FAIL → corriger, re-FREEZE, re-SAVE, re-run
        │                BLOCKED → lire le check fautif :
        │                  branche protégée → worktree obligatoire
        │                  config/module invalide → BLOCK_IF, corriger la config
        │
        ▼ (si PASS seulement)
§19b FACT_WRITEBACK     écriture mémoire des faits ✦ (jamais avant PASS)
```

---

## 3. Schémas de flux

### 3.1 Chaîne complète d'un chantier

```
┌──────────┐   ┌───────────────┐   ┌──────────────┐   ┌──────────────┐   ┌─────────────┐
│ création │   │ production    │   │ gate déter-  │   │ revue LLM    │   │ certificat  │
│ worktree │──►│ du livrable   │──►│ ministique   │──►│ indépendante │──►│ result.json │
└──────────┘   └───────────────┘   └──────────────┘   └──────────────┘   └─────────────┘
                                     │ (check)         │ (spawn OU review-local Ollama)
                                     ▼                 ▼
                                FAIL/BLOCKED      FAIL → rework
```

### 3.2 Machine à états du verdict

```
                 ┌────────────┐
                 │  UNKNOWN   │
                 └─────┬──────┘
                       │ verify.py check
                       ▼
              ┌────────────────┐
              │ deterministic  │
              │ PASS/FAIL/BLOCK│
              └───────┬────────┘
                      │ certify --review
                      ▼
              ┌────────────────┐          état modifié ?
              │    CERTIFIED   │─────────► oui ──► FAIL (PASS invalidé)
              │ PASS/FAIL/BLOCK│
              └────────────────┘
                      │
                      ▼
              modification post-PASS
                      │
                      ▼
              ┌────────────────┐
              │  PASS INVALID  │  (STATE_ID recomputé ≠)
              └────────────────┘
```

### 3.3 Escalade des verdicts

```
                    FAIL
                     ▲
        ┌────────────┼────────────┐
        │            │            │
     FAIL          BLOCKED       PASS
     (test,         (branche      (tout vert)
      naming,        protégée,
      content)       config
                     invalide)
```

Règle : un seul FAIL domine tout ; à défaut un BLOCKED domine PASS. Un BLOCKED de naming/content (regex invalide) ne peut pas verdir le gate.

### 3.4 Périmètres déclaratifs

```
.verify/config.json
├── naming (investigations/)
│   ├── dirs: ["investigations/"]
│   ├── dir_pattern: ^\d{4}-\d{2}-\d{2}_<sujet>$
│   ├── only_types: ARTICLE|HYPER_MATRICE|ARCHITECTURE|SATURATION_AUDIT|REGISTRE|INVESTIGATION
│   ├── since: 2026-08-17          ← legacy hors scope
│   └── exclude: INDEX.md, .zip, _synthese/
│
└── content (articles/)
    ├── name: no-em-dash-in-published-articles
    ├── forbidden: U+2014 (tiret cadratin)  ← interdit dans les livrables ARTICLE
    ├── dir_pattern: date + tiret OU underscore
    ├── only_types: [ARTICLE]
    └── exclude: copies, .bak, audits, PLAN-CORRECTION, 05_ARTICLE
```

Point de vigilance : les périmètres sont déclaratifs, donc vérifiables. Un périmètre vide est visible (`0 fichier(s) scanné(s)`), jamais confondu avec la conformité.

---

## 4. Fichiers d'état

| Fichier | Contenu | Écrit par | Lecture par |
|---|---|---|---|
| `.verify/pending.json` | état déterministe (verdict, STATE_ID, HEAD) | `check` | `certify` |
| `.verify/result.json` | certificat final (verdict, review, state_changed) | `certify` | humain, dashboard |
| `.verify/config.json` | déclaration des checks | éditeur humain | `verify.py` |

---

## 5. Limites connues et honnêteté

1. **Le contrat reste conversationnel** : `knowledge.md` et KERNEL 19a imposent la gate à l'agent, mais l'agent peut en théorie ne pas l'exécuter. La contrainte technique existe (`certify` fail-safe, branches protégées). Le chemin spawné dépend du runtime Codebuff ; le chemin `gate` (review-local) est scriptable et ne dépend que d'Ollama.
2. **Le reviewer LLM est un jugement probabiliste** : la revue sémantique (cohérence, honnêteté, couverture) reste non déterministe par nature. Le déterministe sécurise l'état ; la revue juge le contenu.
3. **Le certificat `review: PASS` n'est valable que si le verdict vient d'un reviewer réel** : depuis le fix fail-safe, `certify` sans `--review` émet BLOCKED. Un certificat antérieur au fix portant `review: PASS` sans verdict explicite est invalide comme preuve de revue.
4. **Les 87 fichiers hors périmètre** (brouillons, audits, JSON) peuvent contenir des em-dash : c'est conforme au contrat Phase 3, qui ne couvre que les articles publiés.
5. **`.git` ≈ 72 Mo** : les gros fichiers retirés du suivi restent dans l'historique ; une purge exigerait `git filter-repo` (destructif, non fait).
6. **Le naming check couvre les livrables produits après `since`** : les fichiers legacy antérieurs ne sont pas flaggés (choix délibéré pour éviter 2772 violations de bruit).
7. **Le choix du modèle de revue locale est un compromis rigueur/performances** : le benchmark du 2026-08-18 (5 modèles, 2 livrables, `docs/suivi_verification.md` §5) a retenu `qwen3.6:35b` (`think: false` obligatoire). Les modèles 8-12B sont laxistes (faux PASS sur livrable imparfait : le pire échec pour un moteur de vérité) ; phi4-mini et gemma4:26b éliminés. Le pairing modèle→options vit dans `verify.py`. Le re-run versionné (`tools/verify/fixtures/benchmark_results.json`, 2026-08-18) donne 6/6 points sur BAD et 3/4 sur le témoin (C2 manqué), avec une finding hallucinée sur BAD (date 2011 → 2021) : la sortie LLM est advisory, chaque finding doit être recoupé avant correction du livrable.

---

## 6. Références

- Cahier des charges : `docs/boucle_de_verification.md`
- Tableau de bord : `docs/suivi_verification.md` (rapport benchmark review-local : §5)
- Spec du gate unifié : `docs/superpowers/specs/2026-08-18-gate-verification-review-local-design.md`
- Moteur : `tools/verify/verify.py` (README : `tools/verify/README.md`)
- Configuration : `.verify/config.json` (exemple : `.verify/config.example.json`)
- Agents : `.agents/truth-verifier.ts`, `.agents/truth-reviewer.ts`
- Isolateur de chantier : `tools/verify/worktree-new.sh`
- Contrat : `knowledge.md` (section DELIVERY GATE)
- Pipeline : `truth-engine-v2/KERNEL.md` (phases 19a GATE_VERIFY, 19b FACT_WRITEBACK)
