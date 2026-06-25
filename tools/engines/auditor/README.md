# Audit Adversarial — Orchestrateur v3

Audit adversarial multi-modèles d'articles longs. 10 phases dispatchées sur 5 modèles locaux (Ollama Vulkan), sortie JSON native, rendu markdown unique dans le rapport final.

## Usage

```bash
python3 audit.py [--dry-run] [--resume] [--phase PHASE_ID] [--benchmark] <article.md>
```

| Flag | Effet |
|------|-------|
| `--dry-run` | Estimation seule (temps, tokens), pas d'appels LLM |
| `--resume` | Reprend un audit interrompu (vérifie `._complete`) |
| `--phase PHASE_ID` | Lance UNE seule phase (ex: --phase phase6_veto). Charge les outputs sauvés des phases précédentes |
| `--benchmark` | Mesure tok/s des modèles (test courte génération) |

## Principe

```
audit.py
  │
  ├─ Lit le prompt v5 (prompt_v5.md)
  │   └─ parse_sections() → découpe en 4 SHARED + 10 BLOCK
  │
  ├─ Pour chaque phase (10 au total) :
  │   ├─ build_messages() → assemble SHARED (routing tiercé) + BLOCK + article + EXTRA
  │   ├─ call_ollama() → envoie au LLM local (format=JSON_SCHEMA pour G1-G3)
  │   └─ save_phase_output() → .json (réponse brute) + ._complete (marqueur)
  │
  └─ Rapport final :
      └─ json_to_table() → JSON → markdown UNIQUEMENT pour le rapport
```

## Architecture des phases

10 phases, 5 modèles :

| # | Phase | Rôle | Modèle | Format sortie |
|---|-------|------|--------|---------------|
| 0 | Ph0 | Métatexte | phi4-mini 3.8B | Texte structuré (PAS de tableau) |
| 1 | Ph1 | Cold Read | qwen3:8b | 5 réponses brutes (Q1_RALENTI...) |
| 2 | G1 | Greffier (factuel) | granite3.2:8b | **JSON** (schema contraint) |
| 3 | G2 | Logicien (structurel) | qwen3:8b | **JSON** |
| 4 | G3 | Cartographe (représentationnel) | granite3.2:8b | **JSON** |
| 5 | G4 | Contrebandier (pragmatique) | granite3.2:8b | Prose structurée |
| 6 | Ph3 | Deep Dive | qwen3:8b | Tableau + verdict |
| 7 | Ph4 | Synthèse (convergence) | qwen3:8b [KV warm] | Format synthèse |
| 8 | Ph5 | CANNOT_ASSESS Final | qwen3:8b [KV warm] | Verdict structuré |
| 9 | Ph6 | Critical Flaw Veto | qwen3:8b | OUI/NON + justification |

**Pourquoi 10 phases** : 4 Regards indépendants (G1-G4) + Deep Dive (Ph3) + Synthèse (Ph4) + CANNOT_ASSESS (Ph5) + Veto final (Ph6).

## Routing SHARED

Les SHARED blocks du prompt sont distribués de façon **tiercée** — toutes les phases ne reçoivent pas tout :

| SHARED block | Phases destinataires |
|-------------|---------------------|
| `taxonomy` (codes FACT/LACUNA/etc.) | G1, G2, G3, G4, Ph3, Ph4, Ph5, Ph6 |
| `rules` (déontologie) | G1, G2, G3, G4 |
| `format_table` (template JSON) | G1, G2, G3 |
| `format_prose` (template prose) | G4 |

**Ph0 et Ph1 ne reçoivent AUCUN SHARED** — leurs prompts sont auto-suffisants.

## JSON natif (G1, G2, G3)

Les phases tableau utilisent le `format` parameter d'Ollama avec un JSON Schema. Le LLM produit du JSON valide, **pas** un tableau markdown.

```json
{
  "problemes": [
    {"ligne": "10", "citation": "...", "code": "FACT", "gravite": 4, "confiance": 4, "correction": "..."}
  ],
  "fatalites": [...],
  "solide": ["Ligne 5 : « passage fort »"],
  "cannot_assess": ["Aspect X : raison"]
}
```

**Avantage** : zéro corruption de format, validable automatiquement, exploitable par les phases suivantes.

La conversion markdown n'arrive qu'**une fois** : dans le rapport final (`json_to_table()`).

## Stockage

Chaque phase produit :
- `{phase_id}.json` — réponse brute du LLM (JSON ou texte)
- `{phase_id}._complete` — marqueur vide (présent = phase terminée avec succès)

Répertoire de sortie : `articles/_audit_v3_{nom_article}/`

## Garde-fous

| Mécanisme | Cible |
|-----------|-------|
| `format=JSON_SCHEMA` (G1-G3) | Corruption de tableau markdown |
| `temperature=0` | Sortie déterministe |
| `repeat_penalty=1.1` | Boucles de répétition |
| `stop=["\n\n\n\n"]` | Prévention du rabâchage |
| `num_predict` plafonné par phase | Anti-truncation, anti-boucle |
| `num_ctx=16384` | Contexte suffisant pour article long (~8K tok) + prompt (~6K tok) |
| `enable_thinking=False` (g2_logicien uniquement) | Anti-persévération sur qwen3:8b avec JSON schema — ⚠️ PAS sur les phases thinking (ph1, ph6) |
| `validate_output()` après chaque phase | Détection JSON invalide, sortie vide |
| 2 phases défaillantes consécutives → HALTE | Détection panne Ollama/modèle |

## Calibration par phase

Valeurs de `num_predict` et `num_ctx` déterminées expérimentalement (test réel sur article 26K chars, juin 2026) :

| Phase | Modèle | num_predict | Contexte nécessaire | Notes |
|-------|--------|-------------|-------------------|-------|
| Ph0 Métatexte | phi4-mini 3.8B | 200 | 16K | Sortie courte (~50 tok) ; pas de SHARED |
| Ph1 Cold Read | qwen3:8b | 600 | 16K | 5 réponses × 2-3 phrases ≈ 400-600 tok ; thinking model ; pas de SHARED |
| G1 Greffier | granite3.2:8b | 1500 | 16K | JSON 3-7 problèmes ; `maxLength:150` sur citations ; 668 tok mesuré |
| G2 Logicien | qwen3:8b | 1500 | 16K | JSON ; enable_thinking=False (schema compense) ; `maxLength:150` ; 1364 tok mesuré |
| G3 Cartographe | granite3.2:8b | 1500 | 16K | JSON ; `maxLength:150` sur citations ; remplace phi4-mini (gravités timides) |
| G4 Contrebandier | granite3.2:8b | 800 | 16K | Prose 7 sections (5×3-5 phrases + solide + cannot_assess) ; 700 tok mesuré |
| Ph3 Deep Dive | qwen3:8b | 2000 | 16K | Reçoit EXTRA de Ph0 (domaines critiques) ; 1102 tok mesuré, 3 domaines analysés |
| Ph4 Synthèse | qwen3:8b | 2000 | 16K | Reçoit EXTRA compressé de toutes les phases, pas l'article ; 1285 tok mesuré (après retrait article), np 2000 validé |
| Ph5 CANNOT_ASSESS | qwen3:8b | 800 | 16K | Reçoit zones CANNOT_ASSESS extraites, pas l'article ; 216 tok mesuré, 3 zones |
| Ph6 Veto | qwen3:8b | 1500 | 16K | Binaire OUI/NON ; thinking model ; 122 tok mesuré (réel), np 800→1500 (thinking ~400 tok interne) |

## Leçons du test Phase 1 (juin 2026)

La Phase 1 (Cold Read, qwen3:8b) a nécessité 4 corrections avant de fonctionner :

| # | Symptôme | Cause racine | Correction |
|---|----------|-------------|------------|
| 1 | `done_reason=length`, 0 token | `num_predict=150` insuffisant pour 5 réponses | → 400 |
| 2 | Une seule réponse sur 5 | `enable_thinking=False` sur un *thinking model* (qwen3:8b) → modèle amnésique | → retiré pour phase1 (gardé pour g2/ph6) |
| 3 | 0 token, 70s PE | `num_ctx=8192` < article (~8K tok) + prompt (~6K tok) = ~14K | → 16384 |
| 4 | Q5 manquante malgré 3 correctifs | Prompt ambigu (« Maximum 2 phrases par question » sans ordre explicite) | → « Réponds aux 5 questions ci-dessous. Réponds à TOUTES » |

**Règle générale** : un thinking model (qwen3:8b) avec `enable_thinking=False` + contexte saturé = 0 token. Ne jamais désactiver le thinking sur un modèle qui en a besoin, sauf si le `format=JSON_SCHEMA` compense (cas de G2).

## Leçons du test G1-G3 (juin 2026)

Les phases tableau (G1 Greffier, G2 Logicien, G3 Cartographe) produisent du JSON contraint par schéma.
La calibration a nécessité 3 itérations :

| # | Symptôme | Cause racine | Correction |
|---|----------|-------------|------------|
| 1 | JSON tronqué à 300 tok (2.5 problèmes, chaîne coupée) | Budget insuffisant pour 3-7 problèmes structurés | `num_predict` : 300 → 500 |
| 2 | JSON tronqué à 500 tok (citations copient des paragraphes entiers, ~125 tok/problème) | Modèle recopie des blocs de 300+ caractères au lieu d'extraire une phrase | `num_predict` : 500 → 1000 + `maxLength:150` sur les champs `citation` du JSON schema + instruction prompt « citation : max 150 caractères. Ne recopie PAS des paragraphes entiers. » |
| 3 | 7 problèmes OK mais `solide`/`cannot_assess`/`fatalites` tronqués à 1000 tok | 7 × 120 tok = 840 minimum, insuffisant pour le reste du JSON | `num_predict` : 1000 → 1500 (`gen_tok_est` aligné dans PHASE_CONFIG) |

**Règle générale** : un problème JSON complet (citation courte + code + gravité + confiance + correction) consomme ~120 tokens avec granite3.2:8b. Pour 7 problèmes + fatalités + solide + cannot_assess, compter **~1500 tokens minimum**. Le `maxLength:150` sur les citations + l'instruction prompt sont indispensables pour éviter l'explosion du budget tokens par des citations trop longues.

## Leçon du test G4 (juin 2026)

La Phase G4 (Contrebandier, granite3.2:8b, prose structurée) était tronquée à 485/500 tokens, coupée en pleine phrase dans la 5ᵉ section (RISQUES DE RÉCUPÉRATION).

| # | Symptôme | Cause racine | Correction |
|---|----------|-------------|------------|
| 1 | Troncature mi-phrase dans la 5ᵉ section, sections solide/cannot_assess absentes | 5 sections × 4 phrases × ~27 tok + headers + 2 sections bonus ≈ 738 tok > 500 | `num_predict` : 500 → 800 (`gen_tok_est` aligné dans PHASE_CONFIG) |

**Règle générale** : pour la prose G4 (5 sections × 3-5 phrases + solide + cannot_assess), compter **~800 tokens**. Le modèle suit correctement le format `SHARED:format_prose` — le seul problème était le budget tokens.

## Résultats des tests réels (juin 2026)

Tests unitaires sur l'article « Éloge de la surface comme levier » (26K chars, ~5000 mots).

| Phase | Modèle | Tokens | Temps | Problèmes | Codes | Notes |
|-------|--------|--------|-------|-----------|-------|-------|
| Ph1 Cold Read | qwen3:8b | 125 | 95s | — | — | 5/5 questions (np=600), Q5 présente |
| G1 Greffier | granite3.2:8b | 668 | 66s | 7 | FACT, LACUNA, SURETAB, GLISS, PRAG | 5 codes, bonne diversité |
| G2 Logicien | qwen3:8b | 1364 | 200s | 7 | FACT, LACUNA, SURETAB, LOGIC | 4 codes, enable_thinking=False OK |
| G3 Cartographe | granite3.2:8b | 1214 | 209s | 8 | FACT, SURETAB, LACUNA, CONTRA, BIAIS | 5 codes, grav 3-4 ; ✅ placeholder cannot_assess corrigé dans prompt v5 |
| G4 Contrebandier | granite3.2:8b | 700 | 72s | — | — | 7 sections prose complètes |
| Ph3 Deep Dive | qwen3:8b | 1102 | 242s | — | — | 3 domaines (Droit/Histoire/Sociologie), verdicts Fragile |
| Ph4 Synthèse | qwen3:8b | 1285 | 170s | — | — | ✅ np=2000 — 6 étapes complètes ; 1285 tok après retrait article (NO_ARTICLE_PHASES) |
| Ph5 CANNOT_ASSESS | qwen3:8b | 216 | 68s | — | — | ✅ 3 zones évaluées ; fix NO_ARTICLE_PHASES (article saturait contexte 16K) |
| Ph6 Veto | qwen3:8b | 122 | ~76s | — | — | ✅ VETO: NON + JUSTIFICATION + CONFIANCE:3 ; np 800→1500 (thinking consomme ~400 tok) |

**Pipeline complet** : 10 phases séquentielles avec EXTRA enchaîné — ~27 min (estimation dry-run). 9/10 phases testées sur données réelles, Ph6 testée avec fake data.

**35B MoE abandonné** : le modèle `huihui_ai/Qwen3.6-abliterated:35b-Claude-4.7` (q8_0, ~35 Go) ne génère aucun token sur la Radeon 780M (probablement saturation mémoire). Même avec un prompt minimal (« Bonjour »), `done_reason=length`, 0 token. Les phases Ph3-Ph5 ont été basculées sur qwen3:8b.

**Problèmes résolus (juin 2026) :**
- **G3 (phi4-mini)** → remplacé par granite3.2:8b. Le même modèle que G1 et G4, déjà validé sur le format JSON et la diversité des scores.
- **Ph1 (qwen3:8b)** → `num_predict` 400→600. Q5 n'est plus coupée.
- **Ph4 Synthèse tronquée** → `num_predict` 1500→2000. Les 6 étapes sont complètes (convergence, fatalités, méta-évaluation, Top 5, verdict par lecteur, corrections urgentes) + verdict final. Le thinking model consomme ~900 tok visibles mais a besoin de ~2000 tok de budget pour le raisonnement interne.
- **Ph5 CANNOT_ASSESS tronquée** → `build_messages()` envoyait l'article complet (8K tok) aux phases de synthèse (Ph4/Ph5/Ph6) alors que le README documentait « pas l'article ». Ajout de `NO_ARTICLE_PHASES` : ces phases reçoivent uniquement les EXTRA compressés, plus d'article. Ph5 passe de 0 tok (`done_reason=length`) à 216 tok, 3 zones évaluées.
- **G3 cannot_assess placeholder** → le placeholder `"Aspect X : raison"` dans `SHARED:format_table` était parfois copié tel quel par granite3.2:8b. Remplacé par `"[À REMPLACER — décris l'aspect non évaluable et pourquoi...]"` + règle R9 anti-copie ajoutée dans `SHARED:rules`.
- **Ph6 np 800→1500** → avec np=800 sur données réelles, le thinking model ne produisait que 6 tok visibles (VETO: NON\nJUST). Le thinking consomme ~400 tok en interne pour synthétiser 9 phases. np=1500 donne 122 tok visibles avec verdict complet.

**Problèmes connus non résolus :**
- **G3 dépasse parfois 7 problèmes** : 8 au lieu de 7 max. La règle R7 n'est pas toujours respectée. Le schema `maxItems:10` empêche les dégâts.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `audit.py` | Orchestrateur (10 phases, appel Ollama, stockage JSON, rapport) |
| `2026-06-14_audit_adversarial_prompt_v5.md` | Prompt v5 (SHARED + BLOCK découpés par `parse_sections()`) |
| `2026-06-14_audit_adversarial_prompt.md` | Prompt v4.1 (historique, non utilisé) |
