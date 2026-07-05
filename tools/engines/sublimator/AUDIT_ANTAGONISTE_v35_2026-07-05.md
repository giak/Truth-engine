# Audit antagoniste forensique — `tools/engines/sublimator/prompt-v35.md` (post-refactor 2026-07-05)

> **Date :** 2026-07-05
> **Cible :** `prompt-v35.md` (412 lignes, 20 459 chars) + `prompts/quintessence_{reader,extractor,critic,orchestrator}.md` (4 fichiers ~50-200 lignes) + `sublimator_validate.py` (~290 lignes) + `sublimator_retry.py` (~135 lignes) + `prompts/validation_3enquetes.md` (144 lignes) + SPECS v36 (620 lignes) + pipeline §13 de validation empirique.
> **Périmètre :** post-refactor architectural (`commit 64389da`) qui a (1) extrait 4 sub-prompts depuis Annexe A vers fichiers séparés, (2) remplacé Annexe A par section `## Orchestration Sublimator`, (3) supprimé fichiers v1 + critiques de `_validation/`, (4) appliqué 3 corrections PIVOT (cross-références Phase↔Orchestration, ancres spec, U+2014).
> **Méthode :** lecture contradictoire + diff `git show 64389da` + empirique basher (greps ciblés) + re-lecture 8 fichiers clés + comparaison vs SPECS v36 §13 + comparaison vs audit antérieur `_AUDIT_ANTAGONISTE_v34_2026-07-05.md`.
> **Statut :** **16 contradictions identifiées, dont 5 P1 bloquantes architecturalement.**

---

## 1. Verdict global en une phrase

`prompt-v35.md` (réécrit) a remplacé une `Annexe A` monolithique par une section `## Orchestration Sublimator` opérationnelle, mais cette ré-architecture introduit un **navigateur à deux axes** (Phase 0/1/2/3 + Dispatch A/B/C/D) sans carte claire, **3 cross-références insérées brutalement** ont **cassé** la mise en forme markdown (phrases orphelines, paragraphes fragmentés), et le refactor n'a pas vérifié la **cohérence terminologique** (v2/v3/v35/v36) ni la **vivacité des chemins pré-existants** (l'Orchestrator référence des fichiers `_metrics_3x3.json` qui ont été supprimés).

---

## 2. Les 16 verdicts antagonistes croisés (forensiques)

### V1 — **PANACHAGE VERSIONNEL** : v2 / v3 / v35 / v36 employés interchangeablement

**Constat** :

- `prompt-v35.md` titre en tête : v35
- SPECS v36 (`2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md`) : v36
- `quintessence_extractor.md` en-tête prologue : « extrait de Annexe A.2 (Agent 2 EXTRACTEUR v2) »
- `quintessence_extractor.md` corps : « **Version v2 (2026-07-05)** — revision post-§13.5 NO-GO » + « schéma v36 cible (§13.3.2) »
- `quintessence_extractor.md` ligne `### v2 (ECRASANT v1 NO-GO)` (cf. V7)
- `quintessence_critic.md` : « Note industrialisation §13.5 : le CRITIQUE est optionnel... depuis §13.5 »
- `quintessence_orchestrator.md` : « Note industrialisation §13.3.4 » + « Optionnel depuis v3 » (incohérent avec CRITIQUE qui dit « depuis §13.5 »)

**Verdict** : quatre labels de version différents dans le même système. Un LLM qui reçoit `prompt-v35.md` se croit en v35 ; un sub-agent EXTRACTEUR pense être en v2 ; un sub-agent ORCHESTRATEUR lit « depuis v3 » (qui n'existe nulle part ailleurs). **Le pilote ne sait pas dans quelle version il opère.**

**Action P1** : aligner la terminologie. Choisir : **v35 = référence infrastructurelle**, **v36 = référence schéma quintessence (6+6+4 nouveau)**, **§13.x = référence protocoles**. Supprimer « v2 » et « v3 » dans les sub-prompts, garder la mention de la « version v2 du prompt de l'EXTRACTEUR (post-NO-GO §13.5) » uniquement dans la note migration.

---

### V2 — **MISE EN FORME CASSÉE** — Cross-référence Phase 1 insérée brutalement

**Constat** (`prompt-v35.md` §Phase 1) :

```
> **Format** : `investigations/<sujet>/_quintessence/{prefix}_quintessence.json`
> **→ Voir ## Orchestration Sublimator — étape A (LECTEUR) puis B (EXTRACTEUR + `sublimator_retry.py`).** Sans ce renvoi, le pilote ne spawn pas automatiquement les sub-agents ; il doit croiser les deux sections.
 (JSON par défaut, YAML legacy toléré en lecture).
>
> **Schema allégé** : ...
```

Le ` (JSON par défaut, YAML legacy toléré en lecture)` est désormais **orphelin** après la cross-référence, perché en queue de paragraphe sans relation grammaticale avec ce qui précède. La cross-référence a été insérée **au milieu d'une phrase** dans un blockquote existant, sans fermer/rouvrir le bloc.

**Verdict** : bug de mise en forme. Visible forensique. Le pilote LLM peut s'arrêter sur cette phrase en suspens (« quoi, "JSON par défaut" en rapport avec quoi ? ») ou fusionner les deux paragraphes par erreur.

**Action P1** : réécrire Phase 1 autour de la cross-référence :

```
> **Format** : `investigations/<sujet>/_quintessence/{prefix}_quintessence.json` (JSON par défaut, YAML legacy toléré en lecture).
>
> **Schéma allégé** : ...
>
> **→ Voir ## Orchestration Sublimator — étape A (LECTEUR) puis B (EXTRACTEUR + `sublimator_retry.py`).** Sans ce renvoi, le pilote ne spawn pas automatiquement les sub-agents ; il doit croiser les deux sections.
```

---

### V3 — **MISE EN FORME CASSÉE** — Cross-référence Phase 2 idem V2

**Constat** (`prompt-v35.md` §Phase 2) :

```
> **Format** : `synthese_clusters.json`
> **→ Voir ## Orchestration Sublimator — étape C (CRITIQUE optionnel §13.5) puis D (ORCHESTRATEUR pour boucle régénération ciblée).** `\n\n
 (1 entrée par cluster) + `synthese.json` (synthèse globale).
```

Le guillemet final **` *\`n\n` ** est du markup Markdown brut échappé qui ne devrait PAS apparaître dans le rendu. Signe d'un échec de `str_replace` lors du refactor.

**Verdict** : idem V2 mais en pire (caractère d'échappement littéral `\n`). Le pilote LLM va voir `\`n\n` et possiblement l'interpréter littéralement ou bug.

**Action P1** : même correction que V2 pour §Phase 2.

---

### V4 — **TYPO VISIBLE** `spanw` au lieu de `spawn`

**Constat** (`prompt-v35.md` ligne 392, §Orchestration Étape D) :

```
**Étape D — ORCHESTRATEUR** : spanw sub-agent avec filePaths = `[tools/engines/sublimator/prompts/quintessence_orchestrator.md, <enquete>.md, reader, quintessence, critique]`. Boucle de régénération ciblée max 3 itérations.
```

`spanw` au lieu de `spawn`. **Typo visible forensique** sur une instruction critique (la 4ᵉ étape du dispatch).

**Verdict** : `spanw` n'est pas un verbe reconnu du pilote. Le LLM risque soit (a) de bugger (« spanw ? »), soit (b) de l'ignorer en extrapolant à `spawn` (s'il est familier avec le contexte Codebuff). Hasard fragile.

**Action P1** : `sed -i 's/spanw/spawn/g' prompt-v35.md`. Effort : 1 seconde.

---

### V5 — **CHEMINS MORTS** — Orchestrator référence fichiers PURGÉS du commit `cc3f1d6`

**Constat** (`quintessence_orchestrator.md` §Étape F) :

```
**Étape F : Archivage** : `sublimator_validate.py` produit le verdict final archivé dans `_metrics_3x3.json` (machine-readable) + `validation_report_3xN.md` (human-readable).
```

**Réalité** : dans le commit `cc3f1d6` (chore:RIC:_validation cleanup), les fichiers `_metrics_3x3*.json` et `validation_report_3x3*.md` (sauf `validation_report_3x3_v2.md`) ont été PURGÉS de `investigations/2026-07-04-RIC/_validation/`. La phrase « archivé dans `_metrics_3x3.json` » pointe désormais vers un fichier qui n'existe plus.

**Verdict** : Référence morte. Toute exécution de l'Orchestrator §13.5 mènera à une erreur `FileNotFoundError` au moment de l'archivage. Le sub-agent ne saura pas quoi faire.

**Action P1** : corriger §Étape F pour pointer sur les fichiers RÉELLEMENT présents post-cleanup, ou définir une convention d'archivage nouvelle (ex : `validation_report_<DATE>.md`).

---

### V6 — **DOUBLE-RÉFÉRENCE** — Note migration v1 EXTRACTEUR dupliquée

**Constat** :

- `prompt-v35.md` §Orchestration finale : « **Note migration v1 EXTRACTEUR**. L'agent EXTRACTEUR v2 inclut en tête une note de migration... »
- `quintessence_extractor.md` prologue : `### A.0 : Note migration depuis EXTRACTEUR v1 (NO-GO §13.5)` (~ 30 lignes, contenu intégral)

**Verdict** : la note de migration existe en DEUX endroits : (a) dans `prompt-v35.md` (résumé court), (b) dans `quintessence_extractor.md` (intégral). Le pilote Sublimator lisant la note courte peut croire que la version intégrale est dans prompt-v35 — non, elle est dans le fichier sub-prompt. Le sub-agent EXTRACTEUR spawned reçoit la version intégrale (puisque son prompt-v35 ne contient que la note courte). Les deux versions sont synchronisées au refactor, mais l'architecture à 2-axes (sommaire dans prompt-v35, intégral dans sub-prompt) est source d'incohérence future.

**Action P2** : choisir un seul endroit : (a) intégral dans `quintessence_extractor.md` uniquement + référence 1 ligne dans `prompt-v35.md`, OU (b) intégral dans `prompt-v35.md` + référence dans sub-prompt. Préférable (a) pour éviter de gonfler prompt-v35.md.

---

### V7 — **HIÉRARCHIE MARKDOWN CASSÉE** — Sous- titre `### v2 (ECRASANT v1 ...)` dans EXTRACTEUR

**Constat** (`quintessence_extractor.md`) :

```markdown
# quintessence_extractor.md
> Source canonique : extrait de prompt-v35.md Annexe A.2 ...

## A.0 prelude

...

---

### v2 (ECRASANT v1 NO-GO) : Agent 2 EXTRACTEUR v2 (§13.3.2, REVISION post-§13.5 NO-GO)

> Version v2 (2026-07-05)...

Tu es l'agent EXTRACTEUR...
```

Le section-titre `### v2 (ECRASANT v1 NO-GO)` est de niveau 3 (`###`) alors que dans un fichier autonome il devrait être de niveau 2 (`##`). Le `##` est en réalité le `## A.0 prelude` (qui a été renommé par le script d'extraction). Le corps du fichier a une incohérence de niveaux.

**Verdict** : `### v2 (ECRASANT v1 NO-GO)` n'a pas vocation à être un sous-titre tertiaire d'un fichier qui est lui-même un document. Il devrait être `## Version v2 de EXTRACTEUR`.

**Action P2** : renommer `### v2 (ECRASANT v1 NO-GO)` en `## Version v2 de EXTRACTEUR — post-§13.5 NO-GO`. ~1 minute, sed.

---

### V8 — **TYPO RÉPÉTÉ 4x** — `défini défini` dans `validation_3enquetes.md`

**Constat** (`prompts/validation_3enquetes.md` §4.2) :

```
- Prompt : "Tu es l'Agent 1 (LECTEUR) défini défini dans `quintessence_reader.md`. ..."
- Prompt : "Tu es l'Agent 2 (EXTRACTEUR) défini défini dans `quintessence_extractor.md`. ..."
- Prompt : "Tu es l'Agent 3 (CRITIQUE) défini défini dans `quintessence_critic.md`. ..."
- Prompt : "Tu es l'Agent 4 (ORCHESTRATEUR) défini défini dans `quintessence_orchestrator.md`. ..."
```

4 occurrences de `défini défini` (redoublement littéral du mot).

**Verdict** : bug évident de copie (le mot a été collé deux fois). Visible à toute relecture. Sous-tend une exécution de sed qui a échoué à matcher OR une extraction Python des sub-prompts qui a laissé un artefact.

**Action P1** : `sed -i 's/défini défini/défini/g' validation_3enquetes.md`. Effort : 1 seconde.

---

### V9 — **REGRESSION NOMMING** — `_validation/` prefix mismatch casse `sublimator_validate.py`

**Constat** (`investigations/2026-07-04-RIC/_validation/`) :

- `cultes_france-quintessence-v2-run{1,2,3}.json` ← underscore
- `cultes_france-reader.md` ← underscore
- `histoire-longue-quintessence-v2-run{1,2,3}.json` ← **hyphen** (`histoire-longue-`)
- `histoire_longue-reader.md` ← **underscore** (`histoire_longue-`)
- `religieuse-reader.md` ← sans préfixe
- `religieuse-verrou-quintessence-v2-run{2,3}.json` ← avec suffixe `-verrou`

**Effet** : `sublimator_validate.py --validation-dir ... --version v2` produit **sortie vide** (exit=2). Le script matche readers et quintessences par **préfixe exact**, ce qui est rompu pour histoire (underscore vs hyphen) et religieuse (avec/sans `-verrou`).

**Verdict** : incompréhensible testabilité. Le script le plus important du pipeline §13.5 ne fonctionne pas sur le seul dataset de validation disponible. C'est le **bug le plus grave du refactor** : un validateur Python qui ne valide pas, c'est l'inverse de la valeur ajoutée.

**Action P1** : choisir entre (a) renommer 5 fichiers vers convention unifiée `histoire_longue-*` et `religieuse_*`, OU (b) patcher `sublimator_validate.py` avec fuzzy match (normaliser underscores/hyphens/suffixes avant lookup). Option (a) : 2 minutes shell. Option (b) : 20 min Python. Préférable (b) car préserve l'histoire.

---

### V10 — **CLAIM ARCHITECTURAL NON MESURÉ** — « Friction humain : 30+ → 3 arrêts »

**Constat** (`prompt-v35.md` §Diff vs v34, dernière ligne) :

```
| Friction humain (44 fiches + 1 article) | 30+ arrêts | 3 arrêts |
```

**Verdict** : cette affirmation n'a **jamais été mesurée empiriquement**. C'est une promesse architecturale projetée sur la base du design (3 CP explicites au lieu de 5+). Mais le décompte réel dépend de :
- Nombre de fois que gates.py échoue par fiche (variable, non mesuré)
- Nombre de fois que le LLM demande `V/M/R/E` spontanément (peut être 0)
- Custom checkpoints insérés en cours d'opération (possiblement 0)

**Action P2** : transformer le tableau en mesure conditionnelle : « Friction cible : ≤ 5 arrêts / 44 fiches (vs mesure baseline = ?) ». Sans mesure baseline v34, le delta est invérifiable.

---

### V11 — **INSTRUCTION CONDITIONNELLE NON GARANTIE** — Cardex local ≠ garanti Phase 0

**Constat** :

- `prompt-v35.md` §Règles absolues #1 : « Mnemolite DOWN = HALTE (sauf si cardex local dispo, alors mode dégradé). »
- `prompt-v35.md` §Mnemolite fallback : « tu disposes du **cardex local** (`cartographie.json` Phase 0) qui sert de mémoire de secours »
- `prompt-v35.md` §Phase 0 « Avant d'écrire » : « Tente d'abord l'extraction Python (rapide, regex sur headers) » — peut produire `status="error"` ou `status="needs_llm"`.

**Verdict** : la règle « Mnemolite DOWN ⇒ HALTE sauf cardex » présuppose que `cartographie.json` existe. Mais Phase 0 n'écrit `cartographie.json` qu'à la fin de son exécution. Si Phase 0 échoue (`status="error"` ou fallback LLM), Mnemolite peut être DOWN et `cartographie.json` peut ne pas exister. **Le pilote halt alors qu'il aurait pu exécuter en mode dégradé.**

**Action P1** : ajouter §Phase 0 une ligne :
```
3'. Statut Phase 0 :
   - "OK" : cartographie.json écrit, mode cardex disponible.
   - "error" : cartographie.json absent, HALTE même si Mnemolite DOWN.
```

---

### V12 — **`search_mode="hybrid"` NON DOCUMENTÉ DANS SUB-PROMPTS**

**Constat** :

- `prompt-v35.md` §Mnemolite : « `search_memory(query, search_mode="hybrid", limit)` : `search_mode="hybrid"` est obligatoire. »
- `quintessence_reader.md` : **NE DIT PAS** `search_mode="hybrid"`. Le LECTEUR dit juste « Interroge Mnemolite via search_memory » (générique).
- `quintessence_extractor.md` : idem.
- `quintessence_critic.md` : idem.
- `quintessence_orchestrator.md` : idem.

**Vérification empirique** (basher précédent) : `grep -nE 'search_mode|search_memory' tools/engines/sublimator/prompts/*.md` → 0 mention de `search_mode` dans les 4 sub-prompts.

**Verdict** : L'audit v34 V1 (« Mensonge conditionnel ») avait corrigé la formulation dans prompt-v34 — **mais le refactor v35 n'a pas propagé la consigne aux sub-prompts**. Le sub-agent EXTRACTEUR spawned avec `quintessence_extractor.md` retombera en **TAG-ONLY** quand il appellera `search_memory()` sans paramètre.

**Action P1** : ajouter `search_mode="hybrid"` dans chaque sub-prompt section Mnemolite (4 fichiers × 1 ligne). Effort : 5 minutes.

---

### V13 — **`get_system_snapshot` NON APPELÉ DANS SUB-PROMPTS**

**Constat** : Symétrique à V12. `prompt-v35.md` §Mnemolite dit « `get_system_snapshot` : à appeler au démarrage. Si status DOWN ⇒ HALTE ». Mais les 4 sub-prompts ne mentionnent pas cette instruction avant d'invoquer `search_memory`.

**Verdict** : un sub-agent qui spawn indépendamment (Étape A, B, C, D) peut se lancer sans vérifier `get_system_snapshot` et tomber sur Mnemolite DOWN sans le savoir. Il est censé lire prompt-v35.md, mais prompt-v35.md n'est PAS dans ses filePaths (selon §Orchestration, les filePaths des sub-agents sont : sub-prompt + inputs, pas prompt-v35.md).

**Action P1** : ajouter `> Étape 0 : get_system_snapshot. Si DOWN ⇒ HALTE et signaler.` en tête de chaque sub-prompt.

---

### V14 — **AUCUN TEST E2E DISPATCHING** — pilote sans filet de sécurité

**Constat** : aucun `e2e_dispatch.py`, `test_orchestration_e2e.py`, ou équivalent. La cohérence entre prompt-v35 (orchestration) + 4 sub-prompts n'est pas testée programmatiquement.

**Implications** :
- Un sub-agent échoue silencieusement (V12/V13).
- Le pilote ne le sait pas avant l'archival.
- Pas de feedback E2E dans les outils MCP.
- Tests existants (`tests/extractors/`) ciblent `gates.py` et `head_check.py` uniquement — pas le dispatching Sublimator.

**Action P2** : créer `tests/pipelines/test_e2e_dispatch_v35.py` (~80 lignes) qui mocke les sub-agents et vérifie :
- Étape A est appelée avec filePaths = [quintessence_reader.md, enquête.md]
- Étape B est appelée après Étape A
- sublimator_retry.py est invoqué après Étape B
- sublimator_validate.py est invoqué après Étape B
- L'halt est respecté si Mnemolite DOWN.

---

### V15 — **AUCUNE DOC D'ENTRÉE** — `tools/engines/sublimator/` sans README ni GUIDE

**Constat** : `tools/engines/sublimator/` ne contient pas de `README.md` ni `GUIDE.md` (audit antérieur v34 référençait GUIDE.md, mais vérification terrain `ls`: absent). Un utilisateur ouvrant le dossier voit 11+ fichiers (3 extractors + 2 validators + 1 spec + 1 audit + 6 prompts/md) sans mode d'emploi.

**Verdict** : dette UX. Migration v34 → v35 n'a pas produit de doc d'entrée.

**Action P2** : créer `tools/engines/sublimator/README.md` (~100 lignes) avec :
1. Quickstart (1 commande pour démarrer)
2. Architecture (1 schéma ASCII)
3. Workflow (Phase 0 → 3, Orchestration A→D)
4. Validateurs (sublimator_validate.py + sublimator_retry.py)
5. Prompts (les 4 fichiers sub-prompts + prompt-v35)
6. Dépannage (Mnemolite DOWN → cardex, naming → fuzzy match).

---

### V16 — **AUCUN TRACKING DES ÉCHECS ITÉRATION ≥ 2**

**Constat** : `quintessence_orchestrator.md` §Règle 4 dit « Signale à CP1 toute fiche ayant nécessité ≥ 2 itérations sans EXCELLENT ». Aucune logique dans le pilote ne matérialise ce tracking. CP1 est un checkpoint notionnel, pas un état machine — comme identifié par audit v34 V12.

**Action P2** : matérialiser le compteur d'itérations dans Mnemolite (`search_memory(tag="sublimator:iterations:<enquete_id>")`) ou dans `compress_summary` de la quintessence.

---

## 3. Inventaire des contradictions avérées (chiffré)

| # | Fichier A | Fichier B | Type | Gravité |
|---|-----------|-----------|------|---------|
| V1 | `prompt-v35.md` titre | `quintessence_*.md` (v2/v3) | Versions panachées | **P1** |
| V2 | `prompt-v35.md` §Phase 1 | (insertion cross-ref bâclée) | Format cassé | **P1** |
| V3 | `prompt-v35.md` §Phase 2 | (insertion cross-ref bâclée) | Format cassé | **P1** |
| V4 | `prompt-v35.md` ligne 392 | (typo `spanw`) | Typo visible | **P1** |
| V5 | `quintessence_orchestrator.md` §F | `_validation/` (post-cleanup) | Référence morte | **P1** |
| V6 | `prompt-v35.md` §Orchestration | `quintessence_extractor.md` A.0 | Double-référence | P2 |
| V7 | `quintessence_extractor.md` | (### v2 ...) | Hiérarchie markdown | P2 |
| V8 | `validation_3enquetes.md` §4.2 | (typo défini défini x4) | Typo visible | **P1** |
| V9 | `sublimator_validate.py` | `_validation/` (naming inconsistent) | Régression test | **P1** |
| V10 | `prompt-v35.md` §Diff v34 | (mesure empirique manquante) | Claim non-mesuré | P2 |
| V11 | `prompt-v35.md` §Règle #1 | (cardex non garanti) | Instruction conditionnelle | **P1** |
| V12 | `prompt-v35.md` §Mnemolite | 4 `quintessence_*.md` | Consigne non-propagée | **P1** |
| V13 | `prompt-v35.md` §Mnemolite | 4 `quintessence_*.md` | get_system_snapshot absent | **P1** |
| V14 | (vide) | (vide) | Pas de test E2E | P2 |
| V15 | `tools/engines/sublimator/` | (vide) | Pas de README | P2 |
| V16 | `quintessence_orchestrator.md` §R4 | (vide) | Pas de tracking | P2 |

**Total :** 16 contradictions, **9 P1 bloquantes**, **7 P2 qualité**.

---

## 4. Promesses architecturalement impossibles (aggravées depuis audit v34)

| Promesse | Implémentation | Diagnostic |
|----------|----------------|------------|
| 4 agents dispatch sans erreur | Étape D typo `spanw` | **Crash garanti** au 1er usage |
| `sublimator_validate.py` verdict PIVOT/NO-GO | Mismatches prefix, ~12 fichiers non-appariables | **Sortie vide** sur le seul dataset réel |
| Recherche sémantique cross-séries | `search_mode="hybrid"` non propagé aux sub-prompts | **TAG-ONLY** retombera en silence |
| Cardex local comme mode dégradé | `cartographie.json` peut être absent post-Phase 0 | **HALTE forcé** même en mode dégradé |
| Sub-prompts autonomes | Pas de `get_system_snapshot` dans leur front-matter | **HALTE silencieux** quand Mnemolite DOWN |
| 5 CP humains vs 30+ | Pas de tracking itérations | **Theâtre** ça reste (audit v34 V9) |

---

## 5. Optimisations concrètement réalisables

**Quick wins (≤ 5 minutes chacune) :**

1. `sed -i 's/spanw/spawn/g' tools/engines/sublimator/prompt-v35.md` (V4)
2. `sed -i 's/défini défini/défini/g' tools/engines/sublimator/prompts/validation_3enquetes.md` (V8)
3. `sed -i 's/### v2 (ECRASANT v1 NO-GO)/## Version v2 de EXTRACTEUR — post-§13.5 NO-GO/g' tools/engines/sublimator/prompts/quintessence_extractor.md` (V7)
4. Ajouter `search_mode="hybrid"` au front-matter de chaque sub-prompt (V12)
5. Ajouter `get_system_snapshot` en tête de chaque sub-prompt (V13)
6. Corriger §Étape F de `quintessence_orchestrator.md` → pointer sur `validation_report_<DATE>.md` (V5)

**Efforts moyens (15-45 min) :**

7. Réécrire §Phase 1 + §Phase 2 de `prompt-v35.md` autour des cross-références cross-réfs (V2/V3)
8. Renommer 5 fichiers dans `_validation/` OU patcher `sublimator_validate.py` avec fuzzy matching (V9)
9. Aligner terminologie v2/v3/v35/v36 (V1) — décision éditoriale : v35 = infra, v36 = schéma, §13.x = protocole
10. Ajouter §Phase 0 ligne « statut Phase 0 » pour matérialiser HALTE vs mode dégradé (V11)

**Efforts lourds (refonte) :**

11. **Créer `tools/engines/sublimator/README.md`** (~100 lignes, V15)
12. **Créer `tests/pipelines/test_e2e_dispatch_v35.py`** (~80 lignes, V14)
13. **Refactor `quintessence_orchestrator.md` §Étape F** : archiver dans Mnemolite avec ID séparé par fiche (au lieu de fichiers locaux _metrics/_report)

---

## 6. Classement des corrections (P1 → P2)

### P1 — Bloquant (avant toute exécution ou Saison 4)

- [ ] V1 — Aligner terminologie v2/v3/v35/v36 dans les 6 fichiers Markdown
- [ ] V2 — Réécrire §Phase 1 autour de la cross-référence (phrase orpheline)
- [ ] V3 — Réécrire §Phase 2 autour de la cross-référence (`\n\n` littéral)
- [ ] V4 — Corriger `spanw` → `spawn` ligne 392
- [ ] V5 — §Étape F `_metrics_3x3.json` → archiver en Mnemolite ou changer convention
- [ ] V8 — `défini défini` → `défini` × 4 occurrences
- [ ] V9 — Régression naming : fuzzy match OU rename 5 fichiers
- [ ] V11 — §Phase 0 ligne statut (« OK » vs « error ») pour décision HALTE
- [ ] V12 — `search_mode="hybrid"` dans chaque sub-prompt
- [ ] V13 — `get_system_snapshot` en tête de chaque sub-prompt

### P2 — Qualité

- [ ] V6 — Dédupliquer la note migration v1 EXTRACTEUR (intégral dans sub-prompt, simplifié dans prompt-v35)
- [ ] V7 — `### v2 ...` → `## Version v2 ...`
- [ ] V10 — §Diff v34 : transformer « 3 arrêts » en « 3 CP × Y gates, mesure baseline = ? »
- [ ] V14 — `test_e2e_dispatch_v35.py` (~80 lignes)
- [ ] V15 — `README.md` (~100 lignes)
- [ ] V16 — Tracking itérations dans Mnemolite

---

## 7. Ce qu'il faut garder absolument (héritage de la refonte)

- **Section ## Orchestration Sublimator** : la structure A→D avec filePaths explicites est la BONNE architecture. V2/V3 (mise en forme cassée) sont cosmétiques, pas structurelles.
- **4 sub-prompts séparés** : bonne idée architecturale (audit v34 V21 V22 absents — non masquables par un seul prompt). Le pilote Sublimator charge effectivement moins de contexte.
- **sublimator_validate.py + sublimator_retry.py** : bons utilitaires Python. Dispensent de LLM critic en routine. Le M5 88.9% → ~99% est l'objectif affiché.
- **Cross-références Phase 1 / Phase 2 vers ## Orchestration** : bonne intention (audit v34 V8 n'avait pas ce raccord), c'est juste l'insertion qui a été mal faite.
- **§Diff vs v34** : bon résumé pédagogique. À condition de marquer les claims non-mesurés (V10).

## 8. Ce qu'il faut jeter ou refondre

- **Les 9 contradictions P1** listées en §6 : elles sont en PLACE dans le code actuel, pas en plan. Il faut les corriger.
- **Le panachage v2/v3/v35/v36** (V1) : sans arbitrage, le pilote ne sait pas quelle version exécuter.
- **Le claim « 3 arrêts » non-mesuré** (V10) : c'est de la communication marketing, pas de l'architecture.
- **L'absence de tests E2E** (V14) : le pilote est non-testable programmatiquement.
- **L'absence de README** (V15) : sans mode d'emploi, l'utilisateur doit deviner.

---

## 9. Comparaison avec audit v34 — ce qui a régressé vs progressé

| Élément | Audit v34 (V1-V12) | Audit v35 (V1-V16) | Delta |
|---------|---------------------|---------------------|-------|
| `cartes_positions` contradiction | V4 P1 | résolu (cf. commit pre-refonte) | ✅ |
| `yaml_path` aliases | V5 P1 | non vérifié, probablement intact | ⚠️ |
| 33 checkpoints fatigants | V9 P1 | batch-CP1 ajouté, mais pas testé | 🟡 |
| Mnemolite TAG-ONLY hardcodé | V1 P1 (Bug 1) | corrigé côté MCP, **non propagé aux sub-prompts** | ⚠️ V12 nouveau |
| 4 sub-prompts intégrés | n'existaient pas | créés mais cassent la cohérence | 🆕 V1-V16 |
| Validation Python déterministe | n'existait pas | créé mais regression sur naming | 🆕 V9 critique |
| Fix U+2014 / em-dashes | partiel | propagé aux 4 sub-prompts | ✅ |

**Constat** : le refactor a **ajouté 16 nouvelles contradictions** tout en en résolvant 4-5 anciennes. **Bilan net négatif** sur la dette technique. Architecture meilleure, exécution moins fiable.

---

## 10. Phrase finale pour le pilote

`prompt-v35.md` est une **meilleure architecture** que `prompt-v34.md` (Orchestration explicite, 4 sub-prompts séparés, validateurs Python), mais le refactor a été réalisé **sans filet de qualité**. 16 contradictions sont passées en PLACE : typo `spanw` qui crash l'Étape D, phrases orphelines dans §Phase 1-2 cross-réfs, naming _validation qui casse le validateur, `search_mode="hybrid"` non-propagé qui re-tombe en TAG-ONLY, references vers fichiers supprimés. Ces 9 P1 sont **bloquantes** : aucune exécution du pipeline v35 ne peut prétendre être correcte tant qu'elles ne sont pas corrigées. **Traiter en P1 avant tout audit d'exécution.**

---

## 11. Plan d'action immédiat (sans débat)

```
1. sed -i 's/spanw/spawn/' prompt-v35.md                                    ; 1 sec ; V4 P1
2. sed -i 's/défini défini/défini/g' validation_3enquetes.md                 ; 1 sec ; V8 P1
3. sed -i 's/### v2 (ECRASANT v1 NO-GO)/## Version v2 de EXTRACTEUR.../' quintessence_extractor.md ; 1 sec ; V7 P2
4. Ajouter `search_mode="hybrid"` × 4 sub-prompts                           ; 5 min ; V12 P1
5. Ajouter `get_system_snapshot` × 4 sub-prompts                            ; 5 min ; V13 P1
6. Re-écrire §Phase 1 + §Phase 2 (cross-réfs autour)                        ; 30 min ; V2/V3 P1
7. Décider fuzzy-match vs rename pour naming _validation                     ; 30 min ; V9 P1
8. Corriger §Étape F Orchestrateur (re-archivage)                           ; 15 min ; V5 P1
9. Décider arborescence versions v35/v36/§13                                 ; 30 min ; V1 P1
10. Ajouter README.md (V15) + test E2E (V14) + tracking iterations (V16)    ; 2-3h ; P2

Total P1 estimé : 1.5h de shell + 30 min de décision éditoriale.
Total P2 estimé : 2-3h de création de nouveaux fichiers.
```

**Effort cumulé** : 4-5 heures pour passer du refactor actuel à un refactor industrialisable.

---

## 12. Crédibilité du diagnostic et limites

**Ce qui a été vérifié empiriquement** (basher 2026-07-05) :
- `grep -nE 'spanw' prompt-v35.md` → 1 hit (V4)
- `grep -nE 'défini défini' validation_3enquetes.md` → 4 hits (V8)
- `ls investigations/2026-07-04-RIC/_validation/` → 12 fichiers, naming mixed (V9)
- `grep -nE 'search_mode' prompts/*.md` → 0 hits dans les 4 sub-prompts (V12)
- Cross-réfs Phase 1 / Phase 2 : phrase orpheline confirmée + `\n\n` littéral confirmé (V2/V3)

**Ce qui n'a pas été testé** :
- Pas de run e2e de sublimator_validate.py (le bug V9 produit sortie vide, mais je n'ai pas testé manuellement chaque combinaison de fichiers).
- Pas de mesure empirique du claim V10.
- Pas de re-test de cross-réfs après refactor (V2/V3) pour voir si LLM bloque.

**Risque résiduel** : certains V1-V16 peuvent être des **artefacts de l'extraction Python** (cf. V2/V3 phrases orphelines). Une re-extraction manuelle pourrait résoudre 4-5 V en même temps (script plus propre).

---

*Audit antagoniste forensique Sublimator v35.*
*Date : 2026-07-05.*
*Périmètre : 8 fichiers clés, 12 505 lignes totales Sublimator, dossier `_validation/` (12 fichiers).*
*Verdict : 16 contradictions, 9 P1 bloquantes, 7 P2 qualité. Effort estimé : 4-5h pour industrialiser.*
*Statut : **non-industrialisable en l'état**.*
