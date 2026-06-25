# Audit Adversarial — Orchestrateur v2 (Multi-modèles CPU/iGPU)

**Date** : 2026-06-14
**Statut** : Design validé, pré-implantation
**Système cible** : Ryzen 7 7840HS / Radeon 780M iGPU / 54GB DDR5 / Linux Mint 22.2

---

## 1. Contrainte matérielle (dure)

### 1.1 Benchmarks réels (iGPU 780M + Vulkan)

**Configuration** : Radeon 780M (RADV PHOENIX, gfx1103) via Mesa 25.2.8 + Vulkan 1.3.275.
Mémoire iGPU : 34.3 GiB total, 29.6 GiB disponible (shared system memory).
**Optimisations** : OLLAMA_FLASH_ATTENTION=1, OLLAMA_KV_CACHE_TYPE=q8_0, num_ctx=8192, num_batch=2048.

| Modèle | Taille | Génération | Prompt Eval | Note |
|--------|--------|-----------|-------------|------|
| phi4-mini (3.8B) | 2.5 GB | **19.9 tok/s** | **181 tok/s** | PE inchangé, gen -6% |
| qwen3:8b | 5.2 GB | **11.1 tok/s** | **103 tok/s** | Stable |
| granite3.2:8b | 4.9 GB | **10.4 tok/s** | **100 tok/s** | Stable |
| qwen3.5:2b | 2.7 GB | **24.6 tok/s** | **156 tok/s** | Backup |
| Qwen3.6-35b-MoE | 23 GB | **17.8 tok/s** | **252 tok/s** | **PE ×10 avec FA+q8_0** |

**Découverte clé** : le contexte par défaut du modèle (262 144 tokens) forçait
Ollama à pré-allouer un KV cache massif, saturant la bande passante mémoire de
l'iGPU. En réduisant `num_ctx` à 8192 et en activant Flash Attention + KV cache
q8_0, le prompt eval du 35B MoE passe de **25 → 252 tok/s** (×10).

Le KV cache reuse fonctionne parfaitement : la 2e requête vers le même modèle
atteint **10 000+ tok/s** de prompt eval (les tokens du préfixe partagé sont
cachés — SHARED blocks + article).

### 1.2 Règle d'assignation

- **Tous les modèles** passent par Vulkan sur l'iGPU, y compris le 35B MoE
- Le goulot d'étranglement est le **prompt eval** du 35B MoE (25 tok/s) :
  6000 tokens de prompt = 240s par phase 35B
- Optimisation : exécuter les phases 35B en séquence continue (KV cache reuse
  partiel pour les phases suivantes)

### 1.3 Configuration Ollama

```bash
# Variables d'environnement REQUISES :
OLLAMA_VULKAN=1        # activer le backend Vulkan
OLLAMA_IGPU_ENABLE=1   # NE PAS exclure les iGPUs (Ollama les droppe par défaut)

# Vérification :
ollama ps    # PROCESSOR = GPU → backend actif
```

Config systemd : `/etc/systemd/system/ollama.service.d/override.conf`
```
[Service]
Environment="OLLAMA_VULKAN=1"
Environment="OLLAMA_IGPU_ENABLE=1"
SupplementaryGroups=render video
```

L'utilisateur doit être dans les groupes `render` et `video` pour accéder au
périphérique GPU Vulkan via `/dev/dri/renderD128`.

### 1.4 Configuration finale (validée)

| Variable | Valeur | Effet |
|----------|--------|-------|
| `OLLAMA_VULKAN=1` | Activé | Backend GPU Vulkan |
| `OLLAMA_IGPU_ENABLE=1` | Activé | Inclure les iGPU (Ollama les exclut par défaut) |
| `OLLAMA_FLASH_ATTENTION=1` | Activé | Attention mémoire efficace, requis pour KV cache q8_0 |
| `OLLAMA_KV_CACHE_TYPE=q8_0` | Activé | KV cache quantifié sur 8 bits (demi-mémoire) |
| `num_ctx=8192` | Dans API calls | Contexte suffisant pour un article, KV cache gérable |
| `num_batch=2048` | Dans API calls | ×2 à ×4 la vitesse de prompt eval |

Le fichier `/etc/systemd/system/ollama.service.d/override.conf` final :

```
[Service]
Environment="OLLAMA_VULKAN=1"
Environment="OLLAMA_IGPU_ENABLE=1"
Environment="OLLAMA_FLASH_ATTENTION=1"
Environment="OLLAMA_KV_CACHE_TYPE=q8_0"
SupplementaryGroups=render video
```

---

## 2. Architecture modèles

### 2.1 Tableau d'assignation

Chaque phase reçoit un modèle de famille architecturale différente pour maximiser la diversité des blind spots.

| Phase | Rôle | Modèle | Famille | Taille | Gen | PE | Estimation |
|-------|------|--------|---------|--------|-----|----|------------|
| Ph0 | Regards U+V | `phi4-mini:latest` | Microsoft Phi | 3.8B | 19.9 | 181 | ~45s |
| Ph1 | Single-Model Warning | `qwen3:8b` | Qwen dense | 8B | 11.1 | 103 | ~76s |
| G1 | Domaine Verification | `granite3.2:8b` | IBM Granite | 8B | 10.4 | 100 | ~118s |
| G2 | CANNOT_ASSESS | `qwen3:8b` (think) | Qwen dense | 8B | 11.1 | 103 | ~115s |
| G3 | Deep Dive | `Qwen3.6-35b-MoE` | Qwen MoE | 35B | 17.8 | 252 | **~66s** |
| G4 | Critical Flaw Cross-Check | `granite3.2:8b` | IBM Granite | 8B | 10.4 | 100 | ~118s |
| Ph3 | Synthèse | `Qwen3.6-35b-MoE` (KV chaud) | Qwen MoE | 35B | 17.8 | 252 | **~53s** |
| Ph4 | CANNOT_ASSESS Final | `Qwen3.6-35b-MoE` (KV chaud) | Qwen MoE | 35B | 17.8 | 252 | **~26s** |

**Estimation par phase (article 4260 mots ≈ 6400 tokens d'entrée, config optimisée)** :

- Le goulot du 35B MoE (25 tok/s) est résolu par `num_ctx=8192` + FA + q8_0 : **252 tok/s**
- Le KV cache reuse entre phases 35B séquentielles sauve ~80% du prompt eval pour Ph3 et Ph4
- **Total estimé : ~10-11 min** (contre ~22 min sans optimisation)
- Répartition : ~7 min phases 8B + ~3-4 min phases 35B

### 2.2 Justification par regard

- **Ph0 Regards U+V** → phi4-mini 3.8B : le plus rapide (21.3 tok/s), suffisant pour l'extraction structurée de métadonnées. Phi optimisé pour l'inférence légère.
- **Ph1 Single-Model Warning** → Qwen3:8b (dense) : premier jugement généraliste. Meilleur ratio qualité/vitesse pour un 8B. Fixe l'alerte initiale.
- **G1 Domain Verification** → granite3.2:8b (IBM) : famille architecturale ≠ Qwen/Phi. Entraîné sur données régulées enterprise, bonne précision factuelle. Tire le meilleur parti des 11.3 tok/s.
- **G2 CANNOT_ASSESS** → Qwen3:8b (think) : mode think activé via `"enable_thinking": true` dans le payload Ollama `/api/chat`. Systématique, décompose la plausibilité pas-à-pas. Paramètre unique à Qwen3.
- **G3 Deep Dive** → Qwen3.6-35b-MoE : l'étape la plus coûteuse (~5 min) mais critique. Détection de contradictions, biais profonds, propagande. Le 35B excelle ici où les 8B échouent.
- **G4 Critical Flaw Cross-Check** → granite3.2:8b : perspective IBM ≠ Qwen. Cross-validation des vulnérabilités critiques. Entraînement équité IBM utile pour ce jugement.
- **Ph3 Synthèse** → Qwen3.6-35b-MoE : agrégation de tous les regards en grille d'évaluation. Justifie le temps (5 min) par le caractère définitif de cette étape.
- **Ph4 CANNOT_ASSESS Final** → Qwen3.6-35b-MoE : verdict final. Exécuté immédiatement après Ph3 pour bénéficier du KV cache chaud (le système prompt est identique, seuls les résultats changent).

---

## 3. Construction du prompt (clarification définitive)

### 3.1 Ce que reçoit chaque phase

```
SYSTEM:
  ┌─ SHARED:taxonomy     (matrice d'audit — identique pour tous)
  ├─ SHARED:rules        (déontologie — identique pour tous)
  └─ BLOCK:<phase_id>    (instructions spécifiques — UNIQUE à cette phase)
       + EXTRA si applicable (métatexte pour Ph3, résultats précédents pour Synthèse)

USER:
  └─ [ARTICLE À AUDITER] (le texte complet)
```

**Ce qui n'est PAS envoyé :** les autres BLOCKs, le prompt entier, aucun contenu superflu.

### 3.2 Règle EXTRA

| Phase | Contenu EXTRA | Source |
|-------|---------------|--------|
| Ph0 Métatexte | — | — |
| Ph1 Single-Model Warning | résultats de Ph0 | `phase0_metatexte.txt` |
| G1-G4 | — | — |
| Ph3 Deep Dive | domaines critiques de Ph0 | `phase0_metatexte.txt` |
| Ph4 Synthèse | TOUS les résultats précédents | tous les fichiers phase_*.txt |

### 3.3 Taille typique d'un appel et impact prompt eval

- SHARED blocks : ~500 mots (~650 tok)
- BLOCK phase : ~150-300 mots (~200-400 tok)
- Article : ~4260 mots (~5500 tok)
- EXTRA : 0-2000 mots selon la phase (résultats phases précédentes)
- **Total entrée phase** : ~6000-7000 tokens
- **Total sortie** : 150-800 tokens selon la phase

**Impact prompt eval sur le temps réel :**

| Modèle | PE (optimisé) | 6000 tok → temps |
|--------|-------------|-----------------|
| phi4-mini | 181 tok/s | 33s |
| qwen3:8b | 103 tok/s | 58s |
| granite3.2:8b | 100 tok/s | 60s |
| Qwen3.6-35b-MoE (cold) | **252 tok/s** | **24s** |
| Qwen3.6-35b-MoE (KV warm) | **10 000+ tok/s** | **<1s** |

L'optimisation `num_ctx=8192` + Flash Attention + q8_0 a résolu le goulot du
35B MoE. Le prompt eval n'est plus le facteur dominant — la génération et le
changement de modèle entre phases le sont désormais.

---

## 4. Orchestrateur Python

### 4.1 Fichier unique : `tools/engines/auditor/audit.py`

```python
# Structure
main()
├── parse_prompt()       → dict[str, dict]  # clés: shared_taxonomy, shared_rules, phase0_metatexte, ...
│                          chaque dict: {label, content}
├── load_config()        → MODEL_MAP + calibration tok/s
├── estimate_total()     → affiche le tableau de pré-estimation
├── run_pipeline()       → séquence 8 phases
│   ├── for phase in ORDER:
│   │   ├── build_message(shared, block, article, extra)
│   │   ├── call_ollama(messages, model, expected_tokens)
│   │   │   → streaming + flush + progression live
│   │   ├── save_result(phase, output, timing)
│   │   └── if resume: verify_integrity() avant chaque phase
│   └── generate_report() → fusion markdown
└── print_summary()      → tableau récapitulatif tok/temps/modèle
```

### 4.2 Calibration embarquée (`--benchmark`)

```bash
python3 audit.py --benchmark
# → pour chaque modèle, envoie un prompt test de ~500 tokens
# → mesure tok/s (generation), tok/s (prompt eval), TTFT
# → sauvegarde dans ~/.cache/truth-engine/benchmark.json
# → ajuste les estimations de temps
```

Évite les estimations à l'aveugle. Prend ~2 min à exécuter une fois, puis les temps sont précis.

**Benchmarks de référence enregistrés (2026-06-14, config optimisée FA + q8_0) :**

```json
{
  "phi4-mini:latest":         {"gen": 19.9, "prompt_eval": 181},
  "qwen3:8b":                 {"gen": 11.1, "prompt_eval": 103},
  "granite3.2:8b":            {"gen": 10.4, "prompt_eval": 100},
  "huihui_ai/Qwen3.6-abliterated:35b-Claude-4.7": {"gen": 17.8, "prompt_eval": 252}
}
```

**Optimisations appliquées (validées expérimentalement, voir §1.4)** :

| Action | PE 35B avant | PE 35B après | Gain |
|--------|-------------|-------------|------|
| `num_ctx=8192` + `num_batch=2048` | 25 tok/s | 171 tok/s | ×6.8 |
| + `OLLAMA_FLASH_ATTENTION=1` | 171 tok/s | 252 tok/s | +47% |
| + `OLLAMA_KV_CACHE_TYPE=q8_0` | 252 tok/s | 252 tok/s (stable) | Mémoire -50% |
| KV cache reuse (2e requête) | 252 tok/s | **10 000+ tok/s** | ×40 |

Le KV cache à 262K du modèle d'origine forçait Ollama à pré-allouer un cache
massif sur l'iGPU, consommant toute la bande passante mémoire. La réduction à
8192 + Flash Attention libère cette bande passante pour la computation réelle.

### 4.3 Streaming progression (flush résolu)

```python
# Chaque chunk Ollama → flush immédiat
# Progression toutes les ~10s ou tous les ~10%
# Format:
#   ┌─ qwen3:8b — Phase 1 Single-Model Warning
#   │  [████████░░░░░░░░░░░░]  42% — 63/150 tok — 8.1 tok/s — 11s
#   │  [████████████████░░░░]  85% — 128/150 tok — 7.5 tok/s — 22s
#   └─ ✓ Terminé — 150 tok — 24s — 6.3 tok/s
```

`sys.stdout.flush()` ou `PYTHONUNBUFFERED=1` en shebang.

### 4.4 Mécanisme de reprise (Option B — robuste)

```
Reprise à chaud :
  1. Vérifier que `_audit_<article>/` existe
  2. Pour chaque phase dans ORDER :
     a. phase_<id>.txt existe ?
     b. Fichier non-vide (>0 bytes)
     c. ~/tmp/phase_<id>.lock existe ? (verrou d'écriture)
     d. Dernière ligne contient "✓" ou marqueur de complétion
     e. Si tout OK → marquer comme complété, ignorer la phase
     f. Si échec → relancer la phase
  3. Rapport : regénéré à partir des fichiers existants
```

Critères d'intégrité :
- Fichier présent ET taille >0 bytes
- Pas de `.lock` file actif (pid vivant dans `/proc/` ou lock vieux de >30 min = orphelin → supprimer et ignorer)
- Le fichier se termine par `__AUDIT_COMPLETE__\n` (marqueur spécifique écrit APRÈS le streaming réussi, ne peut pas apparaître dans l'output du LLM)
- Si 2 phases échouent consécutivement → HALTE (probable problème modèle/Ollama)

### 4.5 Gestion d'erreurs

| Erreur | Comportement | Code retour |
|--------|-------------|-------------|
| Ollama inaccessible (connection refused) | HALTE immédiate, message "Ollama ne répond pas" | 1 |
| Modèle introuvable (404) | HALTE immédiate, propose `ollama pull <nom>` | 1 |
| Timeout phase légère (>60s dépassé) | Sauvegarde partielle, passe à la phase suivante | 2 |
| Timeout phase lourde (>300s dépassé) | Sauvegarde partielle, passe à la phase suivante | 2 |
| Erreur LLM (garbage output) | Sauvegarde + warning, continue | 0 (warning) |
| Lock file existant | Attend 5s, si bloqué → avertit et propose `--force` | 3 |

---

## 5. Format de sortie

### 5.1 Fichiers de phase (`_audit_<article>/`)

```
_audit_<article>/
├── phase0_metatexte.txt         # Ph0 — Regards U+V (phi4-mini)
├── phase1_single_model_warn.txt # Ph1 — Single-Model Warning (qwen3:8b)
├── gate1_domaine_verify.txt     # G1 — Domain Verification (granite3.2:8b)
├── gate2_cannot_assess.txt      # G2 — CANNOT_ASSESS (qwen3:8b think)
├── gate3_deep_dive.txt          # G3 — Deep Dive (35b-MoE)
├── gate4_flaw_crosscheck.txt    # G4 — Critical Flaw Cross-Check (granite3.2:8b)
├── phase3_synthesis.txt         # Ph3 — Synthèse (35b-MoE)
├── phase4_cannot_assess_fin.txt # Ph4 — CANNOT_ASSESS Final (35b-MoE)
├── meta.json                    # timing, modèle, token count par phase
└── audit_<article>.md           # rapport final fusionné
```

### 5.2 Rapport final

Structure :

```markdown
# Audit Adversarial — <article>
**Date** : ... | **Modèles** : ...
**Temps total** : ... | **Tokens** : ...

## Phase 0 — Regards U+V (phi4-mini:latest)
...

## Phase 1 — Single-Model Warning (qwen3:8b)
...

## Gate 1 — Domain Verification (granite3.2:8b)
...

## Gate 2 — CANNOT_ASSESS (qwen3:8b think)
...

## Gate 3 — Deep Dive (Qwen3.6-35b-MoE)
...

## Gate 4 — Critical Flaw Cross-Check (granite3.2:8b)
...

## Phase 3 — Synthèse (Qwen3.6-35b-MoE)
...

## Phase 4 — CANNOT_ASSESS Final (Qwen3.6-35b-MoE)
...
```

---

## 6. Interface utilisateur

```bash
# Usage
python3 audit.py [--benchmark] [--resume] <article.md>

# Exemples
python3 audit.py --benchmark                                          # calibrer les tok/s
python3 audit.py articles/2026-06-13_11-16_eloge_surface_levier_V2_ARTICLE.md
python3 audit.py --resume articles/2026-06-13_11-16_eloge_surface_levier_V2_ARTICLE.md  # reprendre
```

### Sortie console type

```
============================================================
  AUDIT ADVERSARIAL — v2 (KV cache optimisé + FA + q8_0)
  Article : 2026-06-13_11-16_eloge_surface_levier_V2_ARTICLE
  Mots    : ~4260 | Tokens entrée : ~6000
  Étapes  : 8 (3× 35B MoE en continu)
  Benchmarks 2026-06-14 (Radeon 780M, FA + q8_0, ctx=8192) :
    phi4-mini  gen=19.9 t/s  pe=181 t/s
    qwen3:8b   gen=11.1 t/s  pe=103 t/s
    gr3.2:8b   gen=10.4 t/s  pe=100 t/s
    35b-MoE    gen=17.8 t/s  pe=252 t/s  (×10 avec FA+q8_0)
============================================================
  1/8  Ph0 Métatexte           phi4-mini     pe=33s+gen=9s=42s
  2/8  Ph1 Single-Model Warn   qwen3:8b      pe=58s+gen=14s=72s
  3/8  G1 Domaine Verify       granite3.2    pe=60s+gen=56s=116s
  4/8  G2 CANNOT_ASSESS        qwen3:8b      pe=58s+gen=54s=112s
  5/8  G3 Deep Dive            35b-MoE       pe=24s+gen=34s=58s ◄ cold
  6/8  Ph3 Synthèse            35b-MoE (KV)  pe=8s+gen=45s=53s ◄ chaud
  7/8  Ph4 CANNOT_ASSESS Fin   35b-MoE (KV)  pe=4s+gen=23s=27s ◄ chaud
  8/8  G4 Flaw Cross-Check     granite3.2    pe=60s+gen=56s=116s
  ⏱   Total estimé : ~10 min (FA+q8_0 + KV cache reuse)
============================================================

  ┌─ phi4-mini — Ph0 Métatexte
  │  ⌛ Prompt eval: ~6000 tok @ 181 t/s ≈ 33s
  │  [████████████████████] 100% — 200 tok — 19.9 t/s — 10s
  └─ ✓ Terminé — 43s — 200 tok — 19.9 t/s
  💾 Meta : "domaines=[politique, économie]"

  ┌─ qwen3:8b — Ph1 Single-Model Warning
  │  ⌛ Prompt eval: ~6000 tok @ 103 t/s ≈ 58s
  │  [███████████████░░░░░]  80% — 120/150 tok — 11.1 t/s — 11s
  │  [████████████████████] 100% — 150 tok — 11.1 t/s — 14s
  └─ ✓ Terminé — 72s — 150 tok — 11.1 t/s

  ...

  ┌─ Qwen3.6-35b-MoE — G3 Deep Dive
  │  ⌛ Prompt eval: ~6000 tok @ 252 t/s ≈ 24s
  │  [████████████████████] 100% — PE done — 24s
  │  [█████████████░░░░░░░]  55% — 330/600 tok — 17.8 t/s — 19s
  │  [████████████████████] 100% — 600 tok — 17.8 t/s — 34s
  └─ ✓ Terminé — 58s — 600 tok — 17.8 t/s (cold)

  ┌─ Qwen3.6-35b-MoE — Ph3 Synthèse (KV cache reused ✓)
  │  ⌛ Prompt eval: ~2000 new tok @ 252 t/s ≈ 8s (4200 tok cached)
  │  [████████████░░░░░░░░]  50% — 400/800 tok — 17.8 t/s — 22s
  │  [████████████████████] 100% — 800 tok — 17.8 t/s — 45s
  └─ ✓ Terminé — 53s — 800 tok — 17.8 t/s (KV warm)

  ┌─ Qwen3.6-35b-MoE — Ph4 CANNOT_ASSESS Final (KV cache reused ✓)
  │  ⌛ Prompt eval: ~1000 new tok @ 252 t/s ≈ 4s (6200 tok cached)
  │  [████████████████████] 100% — 400 tok — 17.8 t/s — 23s
  └─ ✓ Terminé — 27s — 400 tok — 17.8 t/s (KV hottest)

  ...

============================================================
  RÉSUMÉ
============================================================
  Ph0 Métatexte              200 tok   43s  19.9 t/s  (phi4-mini)
  Ph1 Single-Model Warn      150 tok   72s  11.1 t/s  (qwen3:8b)
  G1 Domaine Verify          600 tok  116s  10.4 t/s  (granite3.2:8b)
  G2 CANNOT_ASSESS           600 tok  112s  11.1 t/s  (qwen3:8b think)
  G3 Deep Dive               600 tok   58s  17.8 t/s  (35b-MoE, cold)
  G4 Flaw Cross-Check        600 tok  116s  10.4 t/s  (granite3.2:8b)
  Ph3 Synthèse               800 tok   53s  17.8 t/s  (35b-MoE, KV warm)
  Ph4 CANNOT_ASSESS Fin      400 tok   27s  17.8 t/s  (35b-MoE, KV warm)
  ───────────────────────────────────────────────────────────
  TOTAL                     3950 tok  597s  (9 min 57s)
✅ Rapport : _audit_2026-06-13/audit_2026-06-13_11-16_eloge_surface_levier_V2_ARTICLE.md
```
