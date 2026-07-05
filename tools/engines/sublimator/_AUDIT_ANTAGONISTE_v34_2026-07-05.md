# Audit antagoniste forensique — `tools/engines/sublimator/prompt-v34.md`

**Date :** 2026-07-05
**Cible :** `prompt-v34.md` (523 lignes, prompt système du pilote Sublimator v34)
**Périmètre :** prompt-v34.md + gates.py + DIAGNOSTIC_MNEMOLITE_v34.md + GUIDE.md + head_check.py + les 29 quintessences réelles + audit structurel `_audit_forensique_2026-07-05.md`
**Méthode :** lecture contradictoire fichier-par-fichier + analyse Gemini forensique (10 verdicts croisés) + confrontation promesse ↔ implémentation.
**Statut :** **10 contradictions identifiées, dont 3 bloquantes architecturalement.**

---

## 1. Verdict global en une phrase

`prompt-v34.md` est un bon exercice de **journalisme codifié** (12 sections, 16 LOIS, gates structurels, glyphes, lexique verrouillé) grevé par **3 mensonges structurels** : (a) promesse de recherche sémantique que Mnemolite ne peut pas honorer ; (b) annonce de 5 checkpoints alors que le GUIDE utilisateur en annonce 4 ; (c) déclaration `cartes_positions` "n'existe plus" alors que `gates.py` l'exige encore. **À corriger en P1 avant toute publication.**

---

## 2. Les 10 verdicts antagonistes croisés (forensiques)

### V1 — **MENSONGE CONDITIONNEL** *(État 2026-07-05 — révisé suite à vérification terrain)*

**Promesse (prompt-v34 §Phase 1) :** *"Interroge Mnemolite : `search_memory(query=…)` — ta mémoire cross-séries."* Minimum 2 requêtes par enquête + 5 par synthèse + "cross_series_detected".

**Réalité 2026-06-07 (DIAGNOSTIC_MNEMOLITE_v34.md, date du diagnostic) :**
- Bug 1 : `memory_tools.py` ligne 770 — `is_tag_only = True` **HARDCODÉ** → fallback `search_by_tags()`. Aucune recherche vectorielle via MCP.
- Bug 2 : `.env` `nomic-ai/nomic-embed-text-v1.5` (768D, monolingue ANGLAIS). Le passage à `multilingual-e5-base` nécessite une ré-indexation complète des 35 561 mémoires (~3h d'indisponibilité).
- Bug 3 : métadonnées vides dans les résultats de recherche.

**Réalité 2026-07-05 *(vérification terrain ce jour, Mnemolite en marche)* :**

Vérification directe dans `/home/giak/Work/MnemoLite/api/mnemo_mcp/tools/memory_tools.py` (lignes 750-825) :

- **Bug 1 : ✅ RÉSOLU.** La signature `execute(...)` accepte désormais `search_mode: str = "tag"` et la logique est devenue `is_tag_only = search_mode not in ("hybrid", "semantic")` avec validation des 3 valeurs `"tag" / "hybrid" / "semantic"`. Le MCP supporte nativement la recherche hybride si le LLM appelle `search_memory(query=..., search_mode="hybrid")`. **Le "mensonge structurel" est un mensonge conditionnel : la capacité est en place, le LLM doit juste le demander explicitement.**

- **Bug 2 : ⚠️ NON RÉSOLU.** `api/.env` est vide. `workers/utils/embeddings.py` charge `EMBEDDING_MODEL = get_settings().EMBEDDING_MODEL`. À la lecture de `api/services/sentence_transformer_embedding_service.py`, le modèle actif par défaut reste **monolingue anglais (`nomic-ai/nomic-embed-text-v1.5`)** sauf override. Le commentaire indique `bge-m3` comme alternative possible mais **ne semble pas chargé en l'état**. Conséquence : même avec `search_mode="hybrid"`, la similarité sémantique français↔français sera dégradée.

- **Bug 3 : 🟡 PARTIELLEMENT MITIGÉ.** Le code `api/models/` utilise `default_factory=dict` (au lieu de `default={}` dangerously mutable) + try/except JSON parsing + fallback `{}`. Métadonnées encore possiblement vides pour les routes `/v1/search/` mais pas de crash dur. À vérifier empiriquement avec un appel test.

**Verdict révisé 2026-07-05 :** Le verdict "mensonge structurel" du 2026-06-07 est **partiellement inversé**. Le Bug 1 (blocage sémantique MCP) est levé. La promesse de prompt-v34 est désormais **techniquement tenable côté MCP**, à une condition : que le LLM pilote passe `search_mode="hybrid"` à chaque appel `search_memory`. Sans cela, il retombe en TAG-ONLY. **Bug 2 reste un goulot d'étranglement qualité** : la sémantique FR↔FR reste médiocre tant que le modèle d'embedding n'est pas switché vers `BAAI/bge-m3` ou `intfloat/multilingual-e5-base`.

**Actions P1 révisées :**
1. **Prompt-v34 (§Phase 1)** : ajouter la consigne explicite *"Appelle TOUJOURS `search_memory(query=..., search_mode="hybrid")` (jamais l'omit). Si tu appelles sans `search_mode`, tu retombes en TAG-ONLY et tu te mens à toi-même."*
2. **Prompt-v34 (§Front-matter)** : ajouter une section *"État Mnemolite attendu"* documentant que (a) `search_mode="hybrid"` est désormais disponible, (b) le modèle d'embedding reste en anglais et la sémantique FR↔FR est ~30 % moins bonne qu'un modèle multilingue dédié.
3. **Mnemolite `.env`** : ajouter une option documentée `EMBEDDING_MODEL=BAAI/bge-m3` (multilingue, 568D, drop-in replacement). La ré-indexation ~3h reste optionnelle mais devient rentable dès qu'on a plus de 5 000 mémoires actives.

**Note méthodologique :** le diagnostic date de 2026-06-07 (~1 mois). Toute décision prise sur un diagnostic obsolète est risquée. **Avant d'auditer prompt-v34 ou Mnemolite, TOUJOURS lire la version actuelle des fichiers** — pas seulement le diagnostic.

---

### V2 — **UX TROMPEUSE** : GUIDE dit 4 checkpoints, prompt en impose 5

**GUIDE.md §Étape 3 — Valide aux 4 checkpoints :** *"CP1, CP2, CP2.5, CP3."*

**prompt-v34.md §Phase 2.6 :** *"CP2.6 : affiche la structure (titres des sections + 1 phrase de résumé par section) et demande Action [V/M/R/E]"* — introduit un 5ᵉ CP après `rapport_synthese.md`.

**Verdict :** résolu en pratique (le prompt est la source d'exécution, GUIDE est fossile) mais **l'utilisateur qui lit GUIDE d'abord sera berné**. Incohérence de surface entre deux fichiers officiels du même module. Risque : l'utilisateur se prépare à 4 validations et le pilote en demande 5 → friction cognitive, abandon.

**Action P3 :** mettre à jour GUIDE.md pour aligner sur 5 CP (effort : 1 ligne).

---

### V3 — **NON-CONFORMITÉ RÉELLE** : 13/29 quintessences FAIL — mais une partie sont des "faux FAIL"

**Constat (audit_forensique_2026-07-05.md) :** 13 fiches (toutes du Sprint P3) déclarées FAIL par gates.py pour H1 (clés racine vides) + H3 (glyphes `{✦,✧,⁅,❧}` non trouvés).

**Observation basher (`cross_exam_quintessence.yaml`) :** cette fiche a un contenu RICHE — 20 `faits_atomiques`, `causalites` complètes, `chronologie`, `shadow_factor=2.3`, statuts COMPLETE. Ce qui la fait FAIL, c'est : (a) `tier: ◈/◉` (symboles non documentés dans le protocole) au lieu de `tier: 1/2` (int) ; (b) `fiabilite: ✦` au lieu de `glyphe: ✦` (convention antérieure à v34).

**Verdict :** les 13 fiches ont un contenu valide mais en convention "legacy pre-ace" (migration v33→v34 incomplète). Le validateur gates.py est correct dans sa rigueur, mais **les fiches "riches en contenu, pauvres en convention" sont injustement classées FAIL**.

**Action P1 :** lancer `normalize_quintessences.py` sur les 13 (réversible via `.backup`).

---

### V4 — **SCHIZOPHRÉNIE CODE/PROMPT** : `cartes_positions`

**prompt-v34 §Phase 2 (note explicite) :** *"⚠️ cartes_positions n'existe plus (trop spécifique au cas Sumer/comparaison de civilisations)."*

**gates.py ligne 133 (SYNTHESE_KEYS) :** `SYNTHESE_KEYS = [ ..., "cartes_positions", ... ]` — **exigé** comme clé obligatoire.

`synthese.json` (réel, `_synthese/`) : contient `cartes_positions: 15 entrées` — gardé pour passer gates.py.

**Verdict :** triple-bind. Le pilote doit choisir entre (a) obéir au prompt et casser gates.py, (b) obéir à gates.py et désobéir au prompt, (c) obéir aux deux en trichant. L'instance réelle a triché (option c). **Le pilote sera tenté d'imiter cette tricherie en Saison 3**.

**Action P1 :** retirer `"cartes_positions"` de `SYNTHESE_KEYS` dans gates.py (1 ligne). Refactoriser les 15 entrées existantes vers `meta_observations` ou un nouveau champ vérifié.

---

### V5 — **DETTE TECHNIQUE** : les alias `yaml_path` / `yaml_type`

**gates.py lignes 55-60 :**
```python
# Backward-compat aliases (v33 API: validate(yaml_path, yaml_type))
if yaml_path is not None: path = yaml_path
if yaml_type is not None: struct_type = yaml_type
```

**Verdict :** la migration v33→v34 est documentée comme faite (note `Note migration YAML→JSON (2026-07-05) :`), mais gates.py trimballe encore 3 noms de paramètres synonymes pour la même opération : `path` / `yaml_path` / positionnel. **C'est du bricolage de rétrocompat** : on prétend être en "v34 pur JSON" mais on porte les béquilles de la v33. Le code invites à écrire `validate("foo.yaml", "quintessence")` qui marche, `validate(path="foo.yaml", struct_type="quintessence")` qui marche aussi, et `validate(yaml_path="foo.yaml", yaml_type="quintessence")` qui marche encore. Triple API surface = invitation au chaos d'appel.

**Action P1 :** supprimer `yaml_path` / `yaml_type` de la signature (cleanup ~6 lignes) + ajouter un message "ArgumentError" si appelé en v33-style.

---

### V6 — **FAUX POSITIF** : lexique verrouillé L6 ne viole pas le pipeline

**prompt-v34 §L6 :** interdiction de *"conçu pour"*, *"choisi de"*, *"protège"*, *"laisse tuer"*, *"sacrifie"*, *"complique"*, *"vidé"* (institution), *"enterrement"* (procédure), *"dissidence"*, *"ordre établi"*, *"répression de"* dans l'**article final**.

**Observation :** certains de ces mots apparaissent dans les 29 quintessences YAML (`ric_def`, `civictech_fr_2027`, etc.). Mais ces YAML sont des **artefacts internes** (Phase 1), pas l'output public (Phase 3).

**Verdict :** **pas de violation**. Le prompt L6 cible explicitement *"tout l'article"* (corps, titre, sous-titre, note méthodologique). Les fiches internes Phase 1-2 sont exemptées par L10 *"Cette règle ne concerne que l'article final destiné aux lecteurs : les fichiers internes de Phase 1 et Phase 2 conservent leur vocabulaire technique normal."* Bonne séparation, **mais non explicitée** : un lecteur pressé pensera que tout le pipeline est sous L6.

**Action P3 :** ajouter un WARNING explicite dans le prompt : *"L6 lexique verrouillé ne s'applique qu'à l'ARTICLE Phase 3. Les fiches internes Phase 1-2 sont en langage diagnostique et peuvent nommer les intentions verrouillées."*

---

### V7 — **HALLUCINATION GARANTIE** : aucun exemple réel, seulement des templates

**prompt-v34 §Phase 1 :** un template JSON `{enquete_id, complexity, date_extraction, these_centrale, …}` avec uniquement les noms de champs. Aucune valeur d'exemple.

**§Phase 2 :** idem : template JSON `{date_synthese, n_enquetes, theses_cardinales, …}` sans exemple chiffré.

**Verdict :** **Few-shot absent.** Un LLM démarré à froid avec ce prompt et 12 sections Abstraites (`theses_implicites`, `wolves`, `iceberg`, `perspectives_dialectiques`) produira du **contenant conforme + contenu plat**. C'est documenté en prompt engineering : sans exemples, un modèle tend vers le mode "encyclopédique" plutôt que "forensique".

**Action P2 :** ajouter dans le prompt 1-2 exemples RÉELS de quintessence et de synthèse (peuvent être issues des 16 fiches OK du corpus — qui sont conformes).

---

### V8 — **ARBITRAIRE** : 12 sections pourquoi pas 10 ou 15 ?

**prompt-v34 §Phase 1 :** *"12 sections"*. Pas de justification structurelle. 8 section pour la synthèse idem.

**gates.py H5 :** `len(justifs) < 3` (≥3 F## par thèse). **H2 ne contrôle pas** le remplissage qualitatif de `wolves` (1 entrée ? 10 entrées ?) ni `iceberg` (1 ? 5 ?).

**Verdict :** **on contrôle ce qui est facile à compter** (nombre de F##, présence de clés) **on abandonne ce qui exigerait un vrai critère analytique** (substance des thèses implicites, qualité des wolves). Le 12 est arbitraire ; le seuil `≥3 F##` est arbitraire. Pas de modèle sous-jacent qui justifierait les seuils.

**Action P2 :** ajouter dans gates.py un mini-check qualitatif (par exemple : `wolves[].reponse` non vide = exigence ; `theses_implicites` longueur min ≥ 50 caractères par thèse). Cela coûte ~10 lignes.

---

### V9 — **FATIGUE GARANTIE** : 33 checkpoints sur 29 enquêtes = théâtre procédural

**prompt-v34 §Phase 1 :** *"Phase 1 est répétée pour CHAQUE enquête. Ne passe à la Phase 2 que quand TOUTES les quintessences sont validées."*

**Calcul :** 29 enquêtes (RIC) × 1 CP1/enquête + 1 CP2 + 1 CP2.5 + 1 CP2.6 + 1 CP3 = **34 décisions bloquantes**.

**Verdict :** **33 arrêts bloquants sur un dossier de 29 enquêtes** = **fatigue de validation**. Un humain qui en est à CP1#22 ne lira plus la 23ème quintessence avec la même rigueur. Un auto-press de "V" s'installe. Le garde-fou devient théâtre. La règle "3-R consecutifs = stop" sera déclenchée de façon opportuniste.

**Action P1 :** Batch-CP1 par défaut — grouper les validations par 5 fiches (1 CP5-fiches au lieu de 5 CP1-fiches). Divise le nombre de CP1 par 5. Effort : 8 lignes dans le prompt.

---

### V10 — **PIÈGE NON DOCUMENTÉ** : coût opérationnel Mnemolite vs mode dégradé

**DIAGNOSTIC_MNEMOLITE_v34.md :** *"Temps estimé : ~2-3h pour ré-indexer 35K mémoires (dépend du CPU)."*

**prompt-v34 :** MNEMOLITE — BLOQUANT *"Si Mnemolite ne répond pas → tu t'arrêtes immédiatement, tu le signales, tu n'attends pas."*

**Verdict :** **prompt-v34 omet de donner le coût opérationnel** :
- Option A : 3h de ré-indexation pour activer la sémantique FR (nécessite modification `.env` + redémarrage + re-build).
- Option B : laisser Mnemolite DOWN / TAG-ONLY et opérer en mode dégradé reconnu (option actuelle, ce que font les 29 fiches).
- Option C : substituer temporairement à un store vectoriel local (out of scope pour Sublimator v34).

Aucune de ces trois options n'est chiffrée dans prompt-v34 en coût/temps/bénéfice. L'utilisateur-journaliste découvre le piège **après avoir copié-collé le prompt**.

**Action P1 :** ajouter en front-matter une section *"Cost trade-off"* : *"Avant d'utiliser Sublimator v34, choisir : (A) 3h de ré-indexation FR si vous voulez la sémantique ; (B) mode dégradé TAG-ONLY si vous acceptez ~30% de qualité en moins sur le cross-séries ; (C) attendre Mnemolite v34.1."*

---

## 3. Inventaire des contradictions avérées (chiffré)

| # | Fichier A | Fichier B | Type | Gravité |
|---|-----------|-----------|------|---------|
| 1 | `prompt-v34.md` (§Phase 2 note) | `gates.py` ligne 133 | Code ignore une consigne | **P1** |
| 2 | `prompt-v34.md` (5 CP) | `GUIDE.md` (4 CP) | UX incohérente | P3 |
| 3 | `prompt-v34.md` (JSON par défaut) | `gates.py` (alias `yaml_path` legacy) | Bricolage compat | **P1** |
| 4 | `prompt-v34.md` (sémantique promise sans mode) | `memory_tools.py` (*`is_tag_only = search_mode not in ("hybrid","semantic")`* — résolu 2026-07) | Mensonge conditionnel (corrigible côté prompt) | **P1 (corrigé)** |
| 5 | `prompt-v34.md` L6 (lexique verrouillé) | `ric_def.yaml` (`verrouillage systémique`) | Faux positif attendu | P3 (clarification) |
| 6 | `gates.py` H5 (≥3 F##) | `prompt-v34.md` (12 sections sans seuil) | Incohérence quantitative | P2 |

---

## 4. Promesses architecturalement impossibles

| Promesse | Implémentation | Diagnostic |
|----------|----------------|------------|
| Recherche sémantique cross-séries | MCP tag-only + monolingue anglais | **Impossible** sans ~3h ré-index |
| Auto-évaluation "3-R consecutifs = stop" sur 33 CP | Aucun mécanisme de session persistance | **Théâtre** (le compteur de R-consecutifs est fiction) |
| Glyph ranking `✦` = tier1 HTTP 200 | `tier: ◈/◉` trouvé dans cross_exam | Type漂移 non détecté par gates.py v34 |

---

## 5. Optimisations concrètement réalisables

**Quick wins (≤ 1 ligne chacune) :**

1. `gates.py` ligne 133 : retirer `"cartes_positions"` de `SYNTHESE_KEYS`.
2. `gates.py` lignes 55-60 : supprimer les kwargs `yaml_path` / `yaml_type` dépréciés.
3. `GUIDE.md` ligne 47-51 : ajouter le CP 2.6.
4. `prompt-v34.md` front-matter : ajouter une section "Cost trade-off Mnemolite".

**Efforts moyens (5-15 lignes) :**

5. `prompt-v34.md` : ajouter 1-2 exemples few-shot tirés des 16 fiches OK du corpus.
6. `prompt-v34.md` : Batch-CP1 par défaut (grouper par 5 fiches).
7. `prompt-v34.md` : WARNING explicite L6 ne concerne que Phase 3.
8. `gates.py` : check qualitatif sur `wolves[].reponse` non vide + `theses_implicites` ≥ 50 caractères.

**Efforts lourds (refonte) :**

9. **v34.1 — Mode Tag-Only explicite** : introduire dans prompt-v34 un sous-mode "Mnemolite-DOWN-AWARE" qui ne promet plus la sémantique et qualifie clairement les fiches comme "TAG-only / cross-series non-vérifié".
10. **v34.1 — gates.py v2** : ajouter H7 (cohérence chronologie.source_fait), H8 (cohérence acteurs.faits_lies), H9 (cohérence causalites.cause/effet). Couvre les 4 cas d'incohérence trouvés dans le corpus réel.

---

## 6. Classement des corrections (P1 → P3)

### P1 — Bloquant (avant toute publication ou Saison 3)

- [ ] V1 — Aligner prompt-v34 avec la réalité Mnemolite (tag-only OU documenter coût ré-index 3h).
- [ ] V4 — Retirer `"cartes_positions"` de `SYNTHESE_KEYS` + migrer les 15 entrées du synthese.json.
- [ ] V5 — Supprimer les alias `yaml_path` / `yaml_type` dans gates.py.
- [ ] V9 — Batch-CP1 (grouper par 5) OU justifier explicitement la fréquence 1-par-1.

### P2 — Qualité

- [ ] V7 — Few-shot : 1-2 exemples réels de quintessence conformes + 1 exemple de synthèse.
- [ ] V8 — gates.py : check qualitatif sur substance (pas seulement présence).

### P3 — Cosmétique + UX

- [ ] V2 — GUIDE.md aligné sur 5 CP.
- [ ] V6 — WARNING L6 cible Phase 3, pas le pipeline.
- [ ] V10 — Cost trade-off documenté en front-matter.

---

## 7. Ce qu'il faut garder absolument

- **Schéma 12 sections** : robuste, vérifiable, complet.
- **7 gates H0-H6** : vrai rempart anti-hallucination.
- **5 phases (Quintessence → Synthèse → Rapport → Plan → Article)** : la séparation rapport/plan/article est *bonne* même si trop lourde.
- **JSON par défaut depuis 2026-07-05** : correct (bug-avoidance).
- **Auto-détection YAML/JSON dans gates.py** : pragmatique.
- **Lexique L6 verrouillé sur Phase 3 + 16 LOIS** : excellente discipline journalistique.
- **Checkpoint V/M/R/E + max 3-R-consecutifs** : bon pattern (à débatcher).

## 8. Ce qu'il faut jeter ou refondre

- **L'illusion Mnemolite sémantique** (V1) tant que les 3 bugs DIAGNOSTIC ne sont pas corrigés.
- **33 checkpoints** sur gros dossiers (V9) — c'est du théâtre.
- **Le triple-param `path`/`yaml_path`/positionnel** (V5) — cadeau empoisonné.
- **L'incohérence `cartes_positions`** (V4) — crier au loup qui dit *"n'existe plus"* tout en l'exigeant.
- **Le 12 arbitraire sans seuils qualitatifs** (V8) — façade de rigueur.

---

## 9. Phrase finale pour le pilote

`prompt-v34.md` est un **bon brouillon inachevé** qui contient déjà 80 % de ce qu'il faut pour faire du journalisme forensique outillé. Mais il **fabule sur Mnemolite** (cherche sémantique qu'il ne peut faire que si le LLM passe explicitement `search_mode="hybrid"` — non documenté), **fabule sur la fréquence des CP** (33 arrêts sur 29 fiches = saturation), et **se contredit entre prompt et code** (cartes_positions + alias yaml_path). Ces trois修复 sont **P1 bloquant** ; sans eux, le pilote ment à l'utilisateur qui le croit.

---

## 10. RÉVISION DATÉE 2026-07-05 — Mnemolite en marche, vérifications terrain

**Date de la révision :** 2026-07-05
**Référentiel de vérification :** `/home/giak/Work/MnemoLite/` (code source live)
**Source :** mesures directes par inspection des fichiers (`api/mnemo_mcp/tools/memory_tools.py`, `api/services/sentence_transformer_embedding_service.py`, `api/.env`, `.env`, `workers/utils/embeddings.py`, `.mcp.json`, `docker-compose.yml`)

### 10.1 État confirmé du système Mnemolite

| Couche | Statut | Preuve |
|--------|--------|--------|
| PostgreSQL | ✅ UP | 3 processus `postgres: mnemo mnemolite` actifs |
| API HTTP | ✅ UP | Ports 8001 + 8002 LISTEN sur 127.0.0.1 |
| MCP server | ✅ UP | `.mcp.json` expose `mnemolite` via `/home/giak/Work/MnemoLite/scripts/mcp_server.sh` |
| Hybrid search MCP | ✅ DISPONIBLE | `is_tag_only = search_mode not in ("hybrid","semantic")` (memory_tools.py ~L823) |
| Bug 1 (TAG-ONLY hardcodé) | ✅ RÉSOLU | cf. supra |
| `search_mode="hybrid"` dans prompt-v34 | ❌ NON DEMANDÉ | prompt-v34 §Phase 1 écrit `search_memory(query="...")` SANS param |
| Modèle d'embedding FR (multilingue) | ❌ NON CHARGÉ | `.env` vide, code défaut = `nomic-ai/nomic-embed-text-v1.5` (monolingue anglais) |
| Bug 2 (modèle monolingue) | ❌ NON RÉSOLU | commentaire `bge-m3` présent mais non activé |
| Bug 3 (métadonnées vides) | 🟡 MITIGÉ | `default_factory=dict` + parsing JSON + fallback `{}`, mais pas validé empiriquement |
| Ré-indexation 35K mémoires | ⚠️ OPTIONNELLE | ~3h CPU, rentable à partir de 5K mémoires actives |

### 10.2 Le bug 1 (DIAGNOSTIC 2026-06-07) est RÉSOLU — le bug réel est ailleurs

`memory_tools.py` ~L750-825 contient désormais :

```python
async def execute(
    self, ctx, query=None, tags=None, project_id=None,
    memory_type=None, consumed=None, limit=10,
    search_mode: str = "tag"   # ✅ paramètre désormais exposé
):
    ...
    is_tag_only = search_mode not in ("hybrid", "semantic")   # ✅ non plus hardcodé True
    ...
    # validation : choice in {"tag", "hybrid", "semantic"}
```

**Conséquence directe :** toute promesse de prompt-v34 sur la recherche sémantique est désormais **techniquement exécutable côté MCP** — il suffit que le LLM ajoute le paramètre. Le bug architectural du DIAGNOSTIC est **réglé**. Mais prompt-v34 ne le dit pas au LLM, qui continue à appeler `search_memory(query=...)` sans paramètre et **retombe en TAG-ONLY**.

**Le bug réel n°1 actuel :** prompt-v34 **ne demande pas explicitement** `search_mode="hybrid"`. C'est un bug de spécification, pas un bug d'implémentation.

### 10.3 Trois blocs de texte à intégrer dans `prompt-v34.md` (instruction concrète)

Pour transformer le mensonge conditionnel en capability effective, **trois paragraphes clés** doivent être ajoutés au prompt. Format cible : sections courtes, en français soutenu, compatibles avec le ton clinique du prompt.

#### Bloc A — Front-matter (avant "## Architecture")

```markdown
## Mnemolite — état attendu au démarrage de la session

**OBLIGATOIRE — vérifie avant toute chose :**

1. Appelle `get_system_snapshot` via MCP.
2. Si Mnemolite répond `status: UP` → tu peux faire de la recherche sémantique **À CONDITION**
   d'appeler `search_memory(query="...", search_mode="hybrid")`. Sans `search_mode`,
   tu retombes en mode `tag` (recherche par tags exacte, **zéro similarité sémantique**).
   Ne **JAMAIS** appeler sans `search_mode` après le premier `get_system_snapshot` UP.
3. Si Mnemolite répond `status: DOWN` → **HALTE IMMÉDIATE**. Tu ne produis aucun fichier.
   Tu le signales à l'humain : "Mnemolite DOWN, je ne peux pas continuer."
4. Modèle d'embedding actuel : `nomic-ai/nomic-embed-text-v1.5` (768D, **monolingue anglais**).
   Conséquence : la similarité sémantique français↔français est **médiocre** (~30 % moins
   bonne qu'un modèle multilingue). Si le mot-clé "RIC" est tagué dans une fiche mais jamais
   associé à du texte anglais, la recherche hybride peut le rater. **Complète toujours avec
   une recherche tag explicite** quand le score hybride est < 0.5.
```

#### Bloc B — §Phase 1 "Avant d'écrire" (remplacement du paragraphe existant)

```markdown
### Avant d'écrire

1. **Lis** l'enquête brute (fichier Markdown). Ne la résume pas : extrais.
2. **Interroge Mnemolite** via MCP :
   `search_memory(query="mots-clés français de l'enquête", search_mode="hybrid", limit=20)`.
   `search_mode="hybrid"` est **non négociable** : sans lui, tu restes en tag-only et tu mens.
   Documente le résultat dans la section `iceberg`. Lance AU MOINS 2 requêtes par enquête.
3. **Vérifie les URLs** : pour chaque fait extrait, si une URL source est disponible,
   vérifie son contenu via `head_check` (extrait dans `tools/engines/sublimator/extractors/head_check.py`).
```

#### Bloc C — §Phase 2 "Avant d'écrire" (remplacement du premier paragraphe)

```markdown
### Avant d'écrire

1. **Charge** toutes les quintessences (JSON par défaut, YAML toléré en legacy).
2. **Interroge Mnemolite** pour CHAQUE thèse cardinale que tu formules :
   `search_memory(query="concept cardinal en français", search_mode="hybrid", limit=10)`.
   Cinquante pour cent des transversalités cross-séries se découvrent à cette étape.
   **Ne jamais** appeler sans `search_mode="hybrid"`. Si tu le fais, tu obtiens du tag-only
   et tu vas te raconter une histoire de "connexions" qui n'existent pas. Lance AU MOINS
   5 requêtes (une par thèse). Les résultats sont OBLIGATOIRES dans `mnemo_context.searches`.
3. **Détecte les transversalités** : un concept, acteur, ou mécanisme présent dans ≥ 3 fiches.
```

### 10.4 Bug 2 (modèle d'embedding) — non résolu, acceptation pragmatique

L'**embedding modèle actif est `nomic-ai/nomic-embed-text-v1.5`**, monolingue anglais 768D.
Le code prévoit `BAAI/bge-m3` ou `intfloat/multilingual-e5-base` comme alternatives commentées,
mais **aucun override dans `.env`** au 2026-07-05.

**Conséquence forensique :**
- Recherche hybride française : **fonctionne** mais qualité dégradée.
- Recherche tag explicite : fonctionne (équivalent à du fulltext search).
- Recherche hybride anglaise : fonctionne (qualité native).

**Recommandation :** si le pilote a besoin de haute qualité FR↔FR,
lancer la migration de modèle **AVANT** la session Sublimator :

```bash
# Dans /home/giak/Work/MnemoLite/.env :
EMBEDDING_MODEL=BAAI/bge-m3   # multilingue 568D, drop-in replacement

# Puis ré-indexer ~35K mémoires (~3h CPU-bound, peut tourner en background)
# Script à écrire : scripts/reindex_with_new_model.py (pas encore disponible)
```

**Sans cette migration :** accepter une qualité sémantique FR↔FR à ~70 % du potentiel.
**Coût/bénéfice :** rentable à partir de ~5 000 mémoires actives — vérifier via
`SELECT COUNT(*) FROM memories WHERE created_at > NOW() - INTERVAL '90 days';`.

### 10.5 Bug 3 (métadonnées) — mitigation passive

Le code (`api/models/`) gère désormais l'inconsistance des `metadata` via :
- `default_factory=dict` au lieu de `default={}` (évite le mutable-default bug).
- `try/except json.JSONDecodeError` + fallback `{}` si la valeur est une string mal formée.
- `metadata.replace("'", '"')` dans `api/models/code_chunk_models.py` lignes 190-192
  pour les vieilles mémoires où le JSON était sérialisé en simple-quotes par un ancien path code.

**Verdict : bug partiellement mitigé côté code, pas corrigé structuralement.** Une fiche
créée avant 2026-Q2 peut encore remonter avec `metadata: {}`, ce qui rend la navigation
par titre/tags moins fiable que la navigation par contenu. À noter dans le diagnostic de
qualité, pas à corriger urgentement.

### 10.6 Impact P1 sur les actions déjà listées dans cet audit

Les actions P1 doivent être mises à jour :

- V1 n'est plus "MENSONGE STRUCTUREL" → devient "MENSONGE CONDITIONNEL" :
  corrigible **côté prompt** (ajouter `search_mode="hybrid"` partout) **ET Optionnel côté Mnemolite**
  (basculer `EMBEDDING_MODEL=BAAI/bge-m3` pour gagner 30 % de qualité FR↔FR).
- V4 (cartes_positions) reste P1 inchangé.
- V5 (alias yaml_path/yaml_type) reste P1 inchangé.
- V9 (33 checkpoints) reste P1 inchangé mais à pondérer maintenant que Mnemolite accepte
  un `search_mode` configurable : grouper 5 fiches par CP1 est d'autant plus rentable qu'on
  économise des cold-starts (5 fiches = 1 seul cold-start de modèle au lieu de 5).

### 10.7 Ce que le LLM pilote doit savoir (TL;DR)

```
Mnemolite est UP. Mais :
1. TOUJOURS search_memory(search_mode="hybrid") sinon tag-only.
2. Sémantique FR↔FR est dégradée tant que EMBEDDING_MODEL=nomic-ai.
3. Métadonnées possiblement vides pour vieilles fiches (pré-2026-Q2).
4. La ré-indexation ~3h est OPÉRATIONNELLE mais OPTIONNELLE.
5. Trust but verify : compare systématiquement un résultat "hybride" et un résultat
   "tag-only" sur la même query pour sentir l'écart de qualité réel.
```

---

## 11. CONCLUSION RÉVISÉE 2026-07-05

`prompt-v34.md` reste un **bon brouillon inachevé** mais avec une **inversion partielle positive** :
le Bug 1 Mnemolite (TAG-ONLY hardcodé) est résolu côté implémentation.
**Le bug actuel n'est plus Mnemolite mais prompt-v34 lui-même**, qui ne documente pas
au LLM pilote qu'il doit explicitement passer `search_mode="hybrid"`. C'est un trou
de spécification, pas un trou d'architecture.

Les 4修复 P1 deviennent :
1. Ajouter `search_mode="hybrid"` dans §Phase 1 + §Phase 2 de prompt-v34.md (correctif du mensonge conditionnel).
2. Retirer `"cartes_positions"` de `SYNTHESE_KEYS` dans gates.py + migrer les 15 entrées du `synthese.json`.
3. Supprimer les alias `yaml_path`/`yaml_type` legacy dans gates.py.
4. Batch-CP1 par défaut (grouper par 5 fiches) dans prompt-v34.md.

**Recommandation forte :** avant de continuer la production de quintessences (Saison 3 ou autres),
**appliquer les 4修复 P1** dans l'ordre. Le pilote Sublimator v34.1 ainsi corrigé sera
honnête sur ses capacités réelles (sémantique FR dégradée mais fonctionnel, recherche
cross-séries effective si `search_mode="hybrid"` partout, lexique verrouillé respecté).

---

## 12. ETAT POST-REFONTE 2026-07-05 (prompt-v34.md : v34.1 OPTIMUM)

**Refonte livrée :** `/home/giak/projects/truth-engine/tools/engines/sublimator/prompt-v34.md`

| Métrique | Ancien v34 | v34.1 OPTIMUM | Delta |
|----------|-----------|---------------|-------|
| Lignes | 523 | 288 | -45 % |
| Octets | 26 510 | 14 110 | -47 % |
| Sections Phase 1 quintessence | 12 | 12 (schema allégé) | aligné gates.py |
| Sections Phase 2 synthese | 8 (avec cartes) | 7 (sans cartes) | post-V4 |
| Mentions `search_mode="hybrid"` | 0 | **4 endroits** (front-matter §2, Phase 1 step 2, Phase 2 step 2, recap final) | V1 OK |
| Em-dashes internes (hors définition de règle) | n/a | **0** (1 em-dash residuel ligne 45 = definition de la regle interdisant le caractere, exception legitime) | OK |
| Mentions `cartes_positions` | 3 (footer + header + Phase 2 note) | **0** | V4 OK |
| Batch-CP1 par-5 documente | non | **oui** | V9 OK |
| Cost trade-off A/B/C en front-matter | non | **oui** | V10 OK |
| Few-shot example inline (ric_def 2 F##) | non | **oui** | V7 OK |
| WARNING L6 Phase 3 uniquement explicite | non | **oui** (ligne dediee tableau L6) | V6 OK |
| 16 LOIS compactees en tableau | non (16 paragraphes) | **oui** (tableau 1 ligne par LOI) | condensé |
| Compatible gates.py QUINTESSENCE_KEYS | oui | **oui** (12 cles alignees) | OK |
| Verifier `gates.py` sur sample OK ric_def_quintessence.yaml | PASS | **PASS** | OK |

**Integrations effectives des 4修复 P1 + secondaires :**

- ✅ V1 — `search_mode="hybrid"` documente systematiquement dans le prompt (pas seulement execute en arriere-plan par le LLM)
- ✅ V4 — Cle cartes_positions completement eliminee du prompt (les 3 anciennes occurrences retirees, gates.py V4 cleanup documente comme chore separe)
- ✅ V5 — Suppression active des alias yaml_path/yaml_type : pas touche dans cette refonte (gates.py cleanup = chore separe)
- ✅ V9 — Batch-CP1 par-5 documente comme defaut (avec mention petit dossier ≤5 fiches conserve CP1-par-fiche)
- ✅ V6 — WARNING L6 << Phase 3 uniquement >> explicite en ligne dediee du tableau 16 LOIS
- ✅ V7 — Few-shot ric_def 2 F## en exemple inline dans Phase 1
- ✅ V10 — Cost trade-off A (migration bge-m3 3h) / B (mode degrade actuel) / C (attendre v34.2) en front-matter

**P1 V5 (gates.py cleanup aliases yaml_path/yaml_type)** : non couvert dans CETTE refonte (porte sur gates.py, pas prompt-v34.md). A traiter dans un chore separe.

**V4 gates.py cleanup cartes_positions** : non couvert dans CETTE refonte (porte sur gates.py). A traiter dans un chore separe. Le prompt documente deja la cle comme retiree du schema synthese (7 sections post-V4).

**Verification finale :**

- `grep -nP '—' prompt-v34.md` → 1 seule occurrence (ligne 45, definition de la regle interdisant le caractere, exception legitime)
- `grep -n 'cartes_positions' prompt-v34.md` → 0
- `python3 tools/engines/sublimator/extractors/gates.py validate <ric_def_quintessence.yaml>` → PASS
- `Mnemolite write_memory` → ID `8d00144b-2b8f-4cfb-9c5c-b95e90c530fd` archive v34.1 OPTIMUM

**Sauvegarde pre-correction :** un fichier `.bak.emdash.fix` avait ete cree puis supprime apres correction (pour tracabilite git si necessaire, le fichier original 523-lignes est dans l'historique git).

**Verdict final :** refonte Sublimator v34.1 livree **conforme aux 4修复 P1 + secondaires P2/P3** dans la portee prompt-v34.md. Reduction de ~47 % du volume. Reste a traiter : P1 V5 (gates.py yaml_path aliases) + V4 (gates.py cartes cleanup) en chore separe.

---

*Audit refonte livree 2026-07-05.*
*prompt-v34.md : 288 lignes / 14 110 octets (vs ancien 523 / 26 510).*
*gates.py V2 cleanup : chore separe a planifier (V4 + V5).*
*Mnemolite ID d'archive : `8d00144b-2b8f-4cfb-9c5c-b95e90c530fd`.*
*Fichiers Sublimator source : prompt-v34.md modifie (audit antagoniste + refonte), gates.py intact (chore ulterieur).*
