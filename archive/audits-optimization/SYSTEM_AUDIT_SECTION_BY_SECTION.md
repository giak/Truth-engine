# SYSTEM.MD — AUDIT COMPLET SECTION PAR SECTION

**Date**: 2025-11-20
**Version analysée**: system.md v8.3 (1069 lignes, 48KB)
**Objectif**: Identifier TOUTES répétitions + examples déplaçables pour optimisation DSL
**Méthodologie**: Analyse ligne par ligne appliquant principes DSL_METAGUIDE.md

---

## MÉTRIQUES GLOBALES (Baseline)

```yaml
Total lignes: 1069
Taille: 48KB
Densité actuelle: 0.45 (target: 0.75)
Clarté actuelle: 0.85 (target: 0.95)

Enforcement logic: ~756 lignes (71%) — CRITIQUE, non compressible sans perte
Examples inline: ~120 lignes (11%) — déplaçables vers kb/SYSTEM_EXAMPLES.md
Répétitions: ~180 lignes (17%) — factorisables via macros DSL
```

---

## SECTION 1 — HEADER
**Lignes**: 1-5
**Purpose**: Version, KB loading, JSON metadata
**Densité**: **HIGH** (5 lignes, 0 verbosité)

### Analyse
```yaml
L1: # TRUTH ENGINE v8.3 — Cognitive Engine
L3: LOAD: @KB[COGNITIVE_DSL,PATTERNS,SEARCH_EPISTEMIC,QUERY_TEMPLATES,QUERY_OPTIMIZATION,VALIDATION,HANDOFF_MEMO] | if missing → ERROR:KB_MISSING STOP
L4: {"truth_engine_active":true,"v":"8.3","parts":3,"p1":"FR"}
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Aucune nécessaire (optimal)
**Lazy-loading**: Non applicable (CORE runtime)

**Verdict**: ✅ **OPTIMAL — Ne pas modifier**

---

## SECTION 2 — ROUTING
**Lignes**: 6-8
**Purpose**: Command routing (tweet, thread, I1 AUTO, default)
**Densité**: **HIGH** (3 lignes, notation compacte)

### Analyse
```yaml
L6: ## ⚡ ROUTING
L8: Command: `tweet`|`thread` → @KB[PAT§11.1] | `---` separator → main/context split | `I1 AUTO` → AUTONOMOUS_ITERATION | Default: PREPROCESSING
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Aucune nécessaire
**Lazy-loading**: Non applicable (CORE runtime)

**Verdict**: ✅ **OPTIMAL — Ne pas modifier**

---

## SECTION 3 — WEB SEARCHES MANDATORY
**Lignes**: 10-199 (190 lignes = **18% du fichier**)
**Purpose**: Enforcement web searches obligatoires, query minimums, MCP checks, quality enforcement
**Densité**: **LOW** (verbosité élevée, examples inline, enforcement répété)

### Analyse Détaillée

#### 3.1 CRITICAL_AWARENESS (L12-45)
```yaml
Contenu: IF conditions pour trigger v8.1 enforcement
Lignes: 34 lignes
Densité: MEDIUM (structured YAML, clear conditions)
```

**Répétitions identifiées**:
- Aucune dans cette sous-section

**Examples identifiés**:
- L14-18: Liste exemples trigger (5 lignes)
- L20-24: Liste exemples exclusions (5 lignes)
- L28-33: Liste "You MUST NOT" (6 lignes)
- L35-39: Liste "You MUST" (5 lignes)

**Total examples**: 21 lignes

**Factorisation possible**:
```yaml
# ACTUEL (21 lignes verbose):
**IF user invokes ANY of:**
- "Protocole Truth Engine"
- "Truth Engine protocol"
- [... 3 autres lignes ...]

**EXCLUSIONS (DO NOT trigger v8.1 enforcement):**
- "Investigate [technical]" where technical ∈ {bug, code, ...}
- [... 3 autres lignes ...]

**You MUST NOT:**
- Proceed with KB-only analysis
- [... 4 autres lignes ...]

**You MUST:**
- Execute web searches IMMEDIATELY after complexity assessment
- [... 3 autres lignes ...]

# OPTIMISÉ (5 lignes + macro):
@MACRO[WEB_MANDATORY_TRIGGERS] = [list from kb/SYSTEM_MACROS.md]
@MACRO[WEB_MANDATORY_EXCLUSIONS] = [list from kb/SYSTEM_MACROS.md]
@MACRO[WEB_MANDATORY_RULES] = {MUST_NOT: [...], MUST: [...]}

IF @MACRO[WEB_MANDATORY_TRIGGERS] AND NOT @MACRO[WEB_MANDATORY_EXCLUSIONS]:
  → ENFORCE: @MACRO[WEB_MANDATORY_RULES]

Gain: 21 → 5 lignes = 76% compression
```

#### 3.2 QUERY_MINIMUM (L47-53)
```yaml
Densité: HIGH (7 lignes, notation compacte YAML)
```

**Répétitions**: Pattern réutilisé dans QUERY_ENFORCEMENT (L79-100)
**Examples**: Aucun inline (YAML compact optimal)
**Factorisation**: Non nécessaire (déjà optimal)

#### 3.3 MCP_AVAILABILITY_CHECK (L55-77)
```yaml
Densité: MEDIUM (23 lignes, enforcement logic structurée)
```

**Répétitions identifiées**:
- **PATTERN A**: Enforcement checkpoint structure
  ```yaml
  IF condition:
    → STATUS: **[ÉTAT]** [emoji]
    → ERROR/WARNING: "Message"
    → ACTION: "1. Step 1\n 2. Step 2\n 3. Step 3"
    → [STOP/PROCEED]: Action
  ```
  - **Occurrences**: L55-77 (ici), L79-100 (QUERY_ENFORCEMENT), L102-187 (QUALITY_ENFORCEMENT), L455-475 (MANDATORY_CHECKPOINT), L506-533 (MCP_HEALTH_CHECK), L597-600 (VALIDATION)
  - **Total répétitions**: 6 fois dans system.md
  - **Factorisation**: Macro @ENFORCEMENT[TYPE, conditions, actions]

**Examples inline**: Aucun
**Factorisation prioritaire**: ✅ **HIGH** (pattern répété 6×)

#### 3.4 QUERY_ENFORCEMENT (L79-100)
```yaml
Densité: MEDIUM (22 lignes, enforcement + I2 cap logic)
```

**Répétitions identifiées**:
- **PATTERN A** (enforcement checkpoint) — 2ème occurrence
  - L84-91: IF queries < min AND iteration < I2
  - L93-99: ELIF iteration ≥ I2

**Examples inline**: Aucun
**Factorisation**: @MACRO[ENFORCEMENT_CHECKPOINT]

#### 3.5 QUALITY_ENFORCEMENT (L102-187)
```yaml
Densité: LOW (86 lignes = 8% du fichier total)
Problème: Sur-ingénierie (DSL_METAGUIDE §7 Piège 1)
```

**Répétitions identifiées**:
- **PATTERN A** (enforcement checkpoint) — 3ème occurrence
  - L117-122: severity = MINOR
  - L124-129: severity = MODERATE
  - L131-137: severity = SEVERE

**Examples inline** (verbeux):
- L146-180: Gap root cause examples (35 lignes)
  ```yaml
  L146-157: IF PRIMARY_actual < PRIMARY_target (12 lignes)
    # Explications + examples templates queries

  L150-157: IF geo_diversity < target (8 lignes)
    # Explications + examples templates

  L154-157: IF L6_counter_narrative == MISSING (4 lignes)

  L162-180: Generate I{n+1} queries section (19 lignes)
    # 3 blocs examples:
    # - ◈_PRIMARY gap (6 lignes)
    # - geo_diversity gap (6 lignes)
    # - L6_counter_narrative gap (6 lignes)
  ```

**Total examples**: 35 lignes déplaçables vers kb/SYSTEM_EXAMPLES.md

**Factorisation possible**:
```yaml
# ACTUEL (86 lignes verbose):
IF queries_total ≥ minimum_for_complexity AND current_iteration < I2:
  # Step 1: Calculate gaps (4 lignes OK)
  # Step 2: Severity analysis (22 lignes enforcement pattern × 3)
  # Step 3: Root cause analysis (35 lignes examples verbose)

# OPTIMISÉ (18 lignes + macros):
IF queries_total ≥ minimum_for_complexity AND current_iteration < I2:

  gaps = @FUNCTION[CALCULATE_GAPS](EDI, PRIMARY, geo, L6)

  severity = @FUNCTION[ANALYZE_SEVERITY](gaps)
  # Returns: MINOR | MODERATE | SEVERE (avec thresholds prédéfinis)

  IF severity IN [MODERATE, SEVERE]:
    → @MACRO[ENFORCEMENT_I1_AUTO](severity, gaps)
    → queries_I{n+1} = {8 if MODERATE else 10}
    → root_causes = @FUNCTION[IDENTIFY_ROOT_CAUSES](gaps)
    → generated_queries = @KB[QUERY_TEMPLATES§gap_types] with root_causes
    → OUTPUT: @TEMPLATE[I1_AUTO_PREVIEW] with gaps, queries, expected_gains

Gain: 86 → 18 lignes = 79% compression
```

#### 3.6 OVERRIDE (L189-199)
```yaml
Densité: HIGH (11 lignes, use cases clairs)
```

**Répétitions**: Aucune
**Examples**: 3 lignes (L191-197) — justifiés (use cases nécessaires)
**Factorisation**: Non nécessaire

### RÉSUMÉ SECTION 3

```yaml
Total lignes: 190 (18% du fichier)
Densité globale: LOW (verbosité, examples, répétitions)

RÉPÉTITIONS:
  - PATTERN A (enforcement checkpoint): 3 occurrences (L55-77, L79-100, L102-187)
    Gain factorisation: ~60 lignes → 20 lignes macro

EXAMPLES INLINE:
  - L14-18: Trigger examples (5 lignes)
  - L20-24: Exclusion examples (5 lignes)
  - L28-33: MUST NOT list (6 lignes)
  - L35-39: MUST list (5 lignes)
  - L146-180: Gap root cause examples (35 lignes)
  Total: 56 lignes déplaçables

FACTORISATION PRIORITAIRE:
  ✅ @MACRO[WEB_MANDATORY_RULES] (21 lignes → 5)
  ✅ @MACRO[ENFORCEMENT_CHECKPOINT] (60 lignes → 20)
  ✅ @KB[SYSTEM_EXAMPLES§web_mandatory] (35 lignes externalisés)

GAIN TOTAL SECTION 3:
  Actuel: 190 lignes
  Optimisé: 190 - 116 (compression) = 74 lignes
  Compression: 61%
```

---

## SECTION 4 — AUTONOMOUS_ITERATION_I1
**Lignes**: 201-269 (69 lignes)
**Purpose**: I1 AUTO mode, gap analysis, query auto-generation
**Densité**: **MEDIUM** (structured YAML, 1 example inline)

### Analyse

#### 4.1 Core Logic (L201-250)
```yaml
Densité: MEDIUM (50 lignes, YAML structuré)
Contenu:
  - Gap analysis (5 types gaps)
  - Query auto-generation (5 priorities)
  - Execution + output
```

**Répétitions**: Aucune
**Examples**: Aucun dans cette partie
**Factorisation**: Non nécessaire (déjà optimal)

#### 4.2 Example Block (L252-269)
```yaml
Densité: LOW (18 lignes example verbose)
```

**Example identifié**:
```
L253-269: I1 AUTO execution example
User: "I1 AUTO logs/2025-11-11_10-00-00_tweet_clandestins.md"

Auto-generated queries:
1. [EDI geo] "clandestins France + EU Eurostat comparison irregular migration"
2. [EDI geo] "immigration clandestine + Spain Italy Germany regional analysis"
[... 8 autres queries listées ...]

Executing I1... (merging with I0 findings)
```

**Factorisation**:
```yaml
# ACTUEL (18 lignes example):
L252-269: Full example avec 10 queries listées

# OPTIMISÉ (2 lignes + pointer):
**Example**: @KB[SYSTEM_EXAMPLES§I1_AUTO_execution]
See full example with 10 auto-generated queries in kb/SYSTEM_EXAMPLES.md

Gain: 18 → 2 lignes = 89% compression
```

### RÉSUMÉ SECTION 4

```yaml
Total lignes: 69
Densité: MEDIUM (example inline pénalise densité globale)

EXAMPLES INLINE:
  - L252-269: I1 AUTO example (18 lignes)
  Déplaçable: ✅ kb/SYSTEM_EXAMPLES.md

GAIN SECTION 4:
  Actuel: 69 lignes
  Optimisé: 69 - 16 = 53 lignes
  Compression: 23%
```

---

## SECTION 5 — USER POSITION DETECTION
**Lignes**: 271-314 (44 lignes)
**Purpose**: Anti-sycophancy, dialectical challenge, contre-hypothèse
**Densité**: **HIGH** (contenu opérationnel compact)

### Analyse

#### 5.1 Core Logic (L271-302)
```yaml
Densité: HIGH (32 lignes, YAML structuré, enforcement clair)
```

**Répétitions**: Aucune
**Examples**: Aucun (logique pure)
**Factorisation**: Non nécessaire

#### 5.2 Example Block (L304-311)
```yaml
Densité: LOW (8 lignes example inline)
```

**Example identifié**:
```
L305-311:
User: "Le chômage 7.4% cache la réalité des DEFM B-E"
→ OUTPUT:
"❗ POSITION USER: Stats officielles = manipulation (DEFM B-E cachés)
⚔️ CONTRE-HYPOTHÈSE: Stats officielles = méthodologie rigoureuse (DEFM B-E = choix statistique légitime)
Investigation: ◈ evidence arbitrera."
```

**Factorisation**:
```yaml
# OPTIMISÉ:
L304: **Example**: @KB[SYSTEM_EXAMPLES§user_position_challenge]

Gain: 8 → 1 ligne = 87% compression
```

#### 5.3 Enforcement Note (L313-314)
```yaml
Densité: HIGH (2 lignes, critique)
```

**Contenu**: Enforcement failure handling
**Factorisation**: Non nécessaire (CORE)

### RÉSUMÉ SECTION 5

```yaml
Total lignes: 44
Densité: HIGH (example inline = seule verbosité)

EXAMPLES INLINE:
  - L304-311: User position challenge example (8 lignes)
  Déplaçable: ✅ kb/SYSTEM_EXAMPLES.md

GAIN SECTION 5:
  Actuel: 44 lignes
  Optimisé: 44 - 7 = 37 lignes
  Compression: 16%
```

---

## SECTION 6 — PREPROCESSING
**Lignes**: 317-476 (160 lignes = **15% du fichier**)
**Purpose**: Complexity, hermeneutic planning, DSL macros, enforcement checkpoint, routing
**Densité**: **MIXED** (0.4 verbose examples, 0.5-0.6 compact YAML)

### Analyse Détaillée

#### 6.1 COMPLEXITY (L319-323)
```yaml
Densité: HIGH (5 lignes compactes)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

#### 6.2 HERMENEUTIC-DRIVEN PLANNING (L325-416)
```yaml
Densité: LOW (92 lignes = 57% de la section)
Problème: Verbosité élevée, examples inline multiples
```

**Examples inline identifiés**:
```yaml
L332-337: Pattern triggers keywords (6 lignes)
  Keywords: "médian", "statistiques", "officiel", "taux" → @PAT[ICEBERG]
  Keywords: "réforme", "annonce", "gouvernement" → @PAT[GAS], @PAT[CYN]
  [... 4 lignes similaires]

L342-346: Work hypotheses examples (5 lignes)
  @PAT[ICEBERG] → H1: "Stats officielles cachent population (temps partiel, DEFM B-E, halo)"
  @PAT[FRAMING] → H2: "Débat cadré occulte vraie question (cui bono?)"
  [... 3 autres lignes]

L350-373: Dissident identification maps (24 lignes)
  ICEBERG (stats manipulation) + LABOR:
    → syndicats: CGT, CFDT, FO, Solidaires (France)
    → ONG inégalités: Observatoire des inégalités, Oxfam, ATTAC
    [... 18 lignes mappings par pattern + domain]

L377-395: Query contextualization examples (19 lignes)
  Examples transformation:
    Generic (FAILS): "CGT CFDT salaires France"
    Contextualized (SUCCEEDS): "CGT CFDT critique EQTP exclusion temps partiel statistiques salaires France"
    [... 15 lignes autres exemples + templates]

L398-403: Output example (6 lignes)
  "[HERMENEUTIC PLANNING]
   Patterns detected: Ξ:7 (ICEBERG), Λ:6 (FRAMING)
   [... 4 lignes example output]"
```

**Total examples**: 60 lignes

**Factorisation possible**:
```yaml
# ACTUEL (92 lignes verbose):
STEP 1 - PATTERN TRIGGERS (reuse @PAT[] from kb/PATTERNS.md):
  Analyze subject keywords to detect PROBABLE patterns:
    [6 lignes keywords mapping]

STEP 2 - WORK HYPOTHESES (dialectical reasoning):
  For each pattern detected, generate hypothesis about hidden tensions:
    [5 lignes hypothèses examples]

STEP 3 - DISSIDENT IDENTIFICATION (counter-power mapping):
  Map probable dissident actors based on pattern + domain:
    [24 lignes domain mappings]

STEP 4 - QUERY CONTEXTUALIZATION (dialectical injection):
  [19 lignes query examples + templates]

# OPTIMISÉ (22 lignes + KB pointers):
**0.4 HERMENEUTIC-DRIVEN PLANNING** (v8.7):
   ```yaml
   PURPOSE: Predictive dissident mapping via pattern detection BEFORE searches.

   WORKFLOW:
     1. PATTERN TRIGGERS: Analyze keywords → @PAT[] probable (see @KB[PATTERNS§triggers])
     2. WORK HYPOTHESES: Generate dialectical hypotheses per pattern (see @KB[HERMENEUTIC§hypotheses])
     3. DISSIDENT ID: Map counter-power actors (see @KB[HERMENEUTIC§dissidents_map])
     4. QUERY CONTEXT: Generate contextualized queries (see @KB[QUERY_TEMPLATES§4])

   ADAPTIVE:
     SIMPLE (0-3): 1-2 hypotheses, 2-3 dissidents
     MEDIUM (4-6): 2-3 hypotheses, 3-5 dissidents
     COMPLEX (7-8): 3-4 hypotheses, 5-7 dissidents
     APEX (9-10): 4+ hypotheses, 7+ dissidents

   OUTPUT: [HERMENEUTIC PLANNING] block (see @KB[SYSTEM_EXAMPLES§hermeneutic_output])

   INTEGRATION:
     - Patterns: @KB[PATTERNS§triggers]
     - Dissidents: @KB[HERMENEUTIC§dissidents_map]
     - Queries: @KB[QUERY_TEMPLATES§4]
     - Examples: @KB[SYSTEM_EXAMPLES§hermeneutic]
   ```

Gain: 92 → 22 lignes = 76% compression
```

#### 6.3 DSL MACRO EXPANSION (L418-453)
```yaml
Densité: MEDIUM (36 lignes, YAML structuré + enforcement)
```

**Répétitions**: Aucune (logique unique)
**Examples inline**: 1 block (L442-453, 12 lignes)

**Example identifié**:
```
L442-453: [DSL MACROS INITIALIZED] output example
```

**Factorisation**:
```yaml
# OPTIMISÉ:
L442: OUTPUT: @TEMPLATE[DSL_MACROS_INITIALIZED] (see @KB[SYSTEM_EXAMPLES§dsl_macros])

Gain: 12 → 1 ligne = 92% compression
```

#### 6.4 MANDATORY ENFORCEMENT CHECKPOINT (L455-475)
```yaml
Densité: MEDIUM (21 lignes)
```

**Répétitions identifiées**:
- **PATTERN A** (enforcement checkpoint) — 4ème occurrence
  - L456-468: IF NO → STOP enforcement
  - L469-470: IF YES → PROCEED

**Examples**: Aucun
**Factorisation**: @MACRO[ENFORCEMENT_CHECKPOINT]

#### 6.5 WORKFLOW_ROUTING (L477-487)
```yaml
Densité: HIGH (11 lignes compactes)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

### RÉSUMÉ SECTION 6

```yaml
Total lignes: 160 (15% du fichier)
Densité globale: MIXED (LOW dans 0.4, MEDIUM ailleurs)

RÉPÉTITIONS:
  - PATTERN A (enforcement checkpoint): 1 occurrence (L455-475)
    Gain factorisation: ~20 lignes → 8 lignes macro

EXAMPLES INLINE:
  - L332-337: Pattern triggers (6 lignes)
  - L342-346: Work hypotheses (5 lignes)
  - L350-373: Dissident maps (24 lignes)
  - L377-395: Query contextualization (19 lignes)
  - L398-403: Output example (6 lignes)
  - L442-453: DSL macros output (12 lignes)
  Total: 72 lignes déplaçables

FACTORISATION PRIORITAIRE:
  ✅ Externaliser hermeneutic examples → kb/HERMENEUTIC.md + kb/SYSTEM_EXAMPLES.md (60 lignes)
  ✅ @MACRO[ENFORCEMENT_CHECKPOINT] (20 lignes → 8)
  ✅ @TEMPLATE[DSL_MACROS_INITIALIZED] (12 lignes → 1)

GAIN TOTAL SECTION 6:
  Actuel: 160 lignes
  Optimisé: 160 - 84 = 76 lignes
  Compression: 52%
```

---

## SECTION 7 — ALLOCATION/EXECUTION/VALIDATION
**Lignes**: 489-610 (122 lignes)
**Purpose**: Query allocation, TRIGGERED_DEEP_SEARCH, MCP health check, execution, running metrics, validation
**Densité**: **MEDIUM** (structured enforcement, 1 long enforcement block)

### Analyse Détaillée

#### 7.1 ALLOCATION (L489-495)
```yaml
Densité: HIGH (7 lignes, formulas compactes)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

#### 7.2 TRIGGERED_DEEP_SEARCH (L497-504)
```yaml
Densité: HIGH (8 lignes, conditional logic)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

#### 7.3 MCP HEALTH CHECK (L506-533)
```yaml
Densité: MEDIUM (28 lignes)
```

**Répétitions identifiées**:
- **PATTERN A** (enforcement checkpoint) — 5ème occurrence
  - L514-517: IF canary returns []
  - L519-521: IF canary returns results
  - L523-525: IF canary timeout

**Examples**: Aucun
**Factorisation**: @MACRO[ENFORCEMENT_CHECKPOINT]

#### 7.4 EXECUTION (L535-565)
```yaml
Densité: HIGH (31 lignes, algorithmic logic)
```

**Répétitions**: Aucune (algorithme query optimization unique)
**Examples**: Aucun
**Factorisation**: Non nécessaire

#### 7.5 RUNNING METRICS TRACKING (L567-595)
```yaml
Densité: LOW (29 lignes, output verbose)
```

**Examples inline identifiés**:
```yaml
L571-588: Running metrics output example (18 lignes)
  "Running metrics (search {N}/{budget}):
   - ◈ PRIMARY: {count} (target: {◈_min})
   [... 16 lignes output example]"
```

**Factorisation**:
```yaml
# OPTIMISÉ:
L571: OUTPUT: @TEMPLATE[RUNNING_METRICS] (see @KB[SYSTEM_EXAMPLES§running_metrics])

Gain: 18 → 1 ligne = 94% compression
```

#### 7.6 VALIDATION (L597-600)
```yaml
Densité: HIGH (4 lignes compactes)
```

**Répétitions**: PATTERN A (enforcement) — 6ème occurrence (mais ultra-compact ici, 4 lignes)
**Examples**: Aucun
**Factorisation**: Déjà optimal (4 lignes = gain marginal si macro)

### RÉSUMÉ SECTION 7

```yaml
Total lignes: 122
Densité: MEDIUM (running metrics verbose, reste compact)

RÉPÉTITIONS:
  - PATTERN A (enforcement checkpoint): 2 occurrences (L506-533 MCP health, L597-600 validation)
    Gain factorisation: ~28 lignes → 12 lignes macro (validation déjà optimal 4L)

EXAMPLES INLINE:
  - L571-588: Running metrics output (18 lignes)
  Déplaçable: ✅ kb/SYSTEM_EXAMPLES.md

GAIN SECTION 7:
  Actuel: 122 lignes
  Optimisé: 122 - 33 = 89 lignes
  Compression: 27%
```

---

## SECTION 8 — PROCESSING/SAVE/PERSIST
**Lignes**: 602-636 (35 lignes)
**Purpose**: Herméneutique, scoring, patterns, wolves, output, save, persist
**Densité**: **HIGH** (KB pointers compacts)

### Analyse

#### 8.1 Steps 4-8 (L602-610)
```yaml
Densité: HIGH (9 lignes, KB pointers)
```

**Contenu**:
- L602: HERMÉNEUTIQUE → @KB[COGNITIVE_DSL§3]
- L604: SCORING → formulas + KB pointer
- L606: PATTERNS → @KB[PATTERNS]
- L608: WOLVES → @KB[WOLF§8]
- L610: OUTPUT → Parts 1-3

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire (optimal)

#### 8.2 SAVE INVESTIGATION (L612-622)
```yaml
Densité: MEDIUM (11 lignes, instructions détaillées)
```

**Répétitions**: Aucune
**Examples**: Inline (L614-616, 3 lignes filename format) — justifiés (clarté nécessaire)
**Factorisation**: Non nécessaire

#### 8.3 PERSIST TO MEMORY (L624-636)
```yaml
Densité: MEDIUM (13 lignes, MCP integration)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

### RÉSUMÉ SECTION 8

```yaml
Total lignes: 35
Densité: HIGH

RÉPÉTITIONS: Aucune
EXAMPLES: 3 lignes filename (justifiés, ne pas externaliser)
FACTORISATION: Non nécessaire

GAIN SECTION 8:
  Verdict: ✅ OPTIMAL — Ne pas modifier
```

---

## SECTION 9 — INVESTIGATION_TREE
**Lignes**: 638-801 (164 lignes = **15% du fichier**)
**Purpose**: APEX complexity ≥9.0, multi-agent parallel branch exploration
**Densité**: **LOW** (examples verbose, Mermaid, JSON, validation criteria)

### Analyse Détaillée

#### 9.1 Header + Workflow (L638-713)
```yaml
Densité: MEDIUM (76 lignes, YAML workflow structuré)
```

**Répétitions**: Aucune (workflow unique)
**Examples**: Aucun dans cette partie
**Factorisation**: Non nécessaire

**NOTE LAZY-LOADING**: ✅ **Candidat PRIORITAIRE**
- Usage: APEX complexity ≥9.0 uniquement
- Fréquence: <5% investigations (estimé)
- Impact: 164 lignes chargées inutilement 95% du temps
- **Solution**: Déplacer vers kb/SYSTEM_ADVANCED.md, lazy load avec @KB[INVESTIGATION_TREE]

#### 9.2 Branch Structure Example (L715-742)
```yaml
Densité: LOW (28 lignes example YAML verbose)
```

**Example identifié**:
```yaml
L717-742: BRANCH structure example
BRANCH:
  id: "b1_sources_primaires"
  parent: "i0_root"
  [... 25 lignes YAML structure example]
```

**Factorisation**:
```yaml
# OPTIMISÉ:
L715: **Branch Structure Example**: @KB[SYSTEM_EXAMPLES§investigation_tree_branch]

Gain: 28 → 1 ligne = 96% compression
```

#### 9.3 Output Formats (L744-776)
```yaml
Densité: LOW (33 lignes, Mermaid + JSON examples)
```

**Examples identifiés**:
```yaml
L746-756: Mermaid diagram example (11 lignes)
L758-776: JSON state example (19 lignes)
```

**Factorisation**:
```yaml
# OPTIMISÉ:
L744: **Output Formats**: @KB[SYSTEM_EXAMPLES§investigation_tree_outputs]

Gain: 33 → 1 ligne = 97% compression
```

#### 9.4 Validation Criteria (L778-789)
```yaml
Densité: MEDIUM (12 lignes, checklist)
```

**Répétitions**: Aucune
**Examples**: Liste success targets (12 lignes) — justifiée (clarté validation)
**Factorisation**: Possible mais gain marginal

#### 9.5 Integration Notes (L791-801)
```yaml
Densité: HIGH (11 lignes compactes)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

### RÉSUMÉ SECTION 9

```yaml
Total lignes: 164 (15% du fichier)
Densité: LOW (examples verbose, lazy-loading candidat)

LAZY-LOADING CANDIDAT: ✅ **PRIORITAIRE**
  - Usage: APEX (complexity ≥9.0) uniquement
  - Fréquence: <5% investigations
  - Gain: 164 lignes non chargées 95% du temps
  - Solution: Déplacer vers kb/SYSTEM_ADVANCED.md

EXAMPLES INLINE:
  - L717-742: Branch structure (28 lignes)
  - L746-756: Mermaid diagram (11 lignes)
  - L758-776: JSON state (19 lignes)
  Total: 58 lignes déplaçables

FACTORISATION:
  ✅ Externaliser section complète → kb/SYSTEM_ADVANCED.md (164 lignes)
  ✅ Examples → kb/SYSTEM_EXAMPLES.md (58 lignes)

GAIN SECTION 9:
  Actuel: 164 lignes chargées TOUJOURS
  Optimisé (lazy): 10 lignes pointer + 164 lignes chargées SI complexity ≥9.0
  Charge moyenne: 10 + (164 × 0.05) = 18 lignes
  Gain cognitif: 164 → 18 lignes = 89% réduction charge LLM
```

---

## SECTION 10 — OUTPUT STRUCTURE
**Lignes**: 803-1044 (242 lignes = **23% du fichier**)
**Purpose**: Part 1 FR, Part 2 TECH, Part 3 WOLF structures + enforcement
**Densité**: **LOW** (examples multiples, forbidden patterns, enforcement répété)

### Analyse Détaillée

#### 10.1 FACT-CHECKING MANDATORY (L807-857)
```yaml
Densité: LOW (51 lignes, enforcement verbose + examples)
```

**Répétitions identifiées**:
- **PATTERN A** (enforcement checkpoint) — 7ème occurrence
  - L812-822: RULE 1 - PRIMARY SOURCE REQUIREMENT
  - L824-831: RULE 2 - CONFIDENCE CEILING
  - L833-843: RULE 3 - "JE NE SAIS PAS" CAPABILITY

**Examples inline identifiés**:
```yaml
L845-849: Forbidden patterns (5 lignes)
L851-856: Example enforcement (6 lignes)
  User asks: "PIB France 2024?"
  [... 5 lignes example IF/ELSE]
```

**Total examples**: 11 lignes

**Factorisation possible**:
```yaml
# ACTUEL (51 lignes verbose):
RULE 1 - PRIMARY SOURCE REQUIREMENT: [10 lignes YAML]
RULE 2 - CONFIDENCE CEILING: [8 lignes YAML]
RULE 3 - "JE NE SAIS PAS" CAPABILITY: [11 lignes YAML]
Forbidden patterns: [5 lignes list]
Example enforcement: [6 lignes]

# OPTIMISÉ (12 lignes + macros):
**FACT-CHECKING MANDATORY** (v8.5 - Honesty Enforcement):

BEFORE outputting factual claims in Part 1:
  → ENFORCE: @MACRO[FACT_CHECK_RULES] (3 rules)
    * RULE 1: ◈ PRIMARY source required for verifiable claims
    * RULE 2: Maximum confidence 95% (NEVER 100%)
    * RULE 3: "Je ne sais pas" capability (explicit uncertainty)

  → FORBIDDEN: @KB[OUTPUT§forbidden_patterns]
  → EXAMPLES: @KB[SYSTEM_EXAMPLES§fact_checking]

Gain: 51 → 12 lignes = 76% compression
```

#### 10.2 Part 1 Standard Structure (L860-868)
```yaml
Densité: HIGH (9 lignes, structured list)
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

#### 10.3 Part 2 TECH (L870-1008)
```yaml
Densité: MIXED (139 lignes = 13% fichier total)
Contenu: [DIAGNOSTICS], [QUERY_OPTIMIZATION], [FORENSIC REASONING], [I0→I1 COMPARISON], [REFLECTION]
```

**Examples inline identifiés**:
```yaml
L874: DIAGNOSTICS format (1 ligne example) — OK compact

L876-884: [QUERY_OPTIMIZATION] format (9 lignes example YAML)

L886-923: [FORENSIC REASONING] (38 lignes instructions détaillées)
  - L895-920: Output format example (26 lignes YAML structure)

L925-953: [I0→I1 COMPARISON] (29 lignes example YAML)

L955-1008: [REFLECTION] (54 lignes example YAML)
  - L958-961: INVESTIGATION_STATUS (4 lignes)
  - L963-969: GAP_ANALYSIS (7 lignes)
  - L971-995: ITERATION_RECOMMENDATION (25 lignes enforcement patterns)
  - L996-1001: AUTONOMOUS_I1_PREVIEW (6 lignes)
  - L1003-1008: META_NOTES (6 lignes)
```

**Total examples Part 2**: 130 lignes

**Factorisation possible**:
```yaml
# ACTUEL (139 lignes Part 2 TECH verbose):
[DIAGNOSTICS] format: "..." (1 ligne OK)

[QUERY_OPTIMIZATION] format: [9 lignes YAML example]

[FORENSIC REASONING]: [38 lignes instructions + example]

[I0→I1 COMPARISON]: [29 lignes example YAML]

[REFLECTION]: [54 lignes example YAML enforcement patterns]

# OPTIMISÉ (20 lignes + templates):
### Part 2 — TECH

**Structure**: @KB[OUTPUT§part2_structure]
  - [DIAGNOSTICS]: IVF ISN IVS Conf format
  - [SOURCES]: ◈◉○ EDI stratification
  - [QUERY_OPTIMIZATION]: IF v8.3+ applied (see @KB[QUERY_OPTIMIZATION§metrics])
  - [FORENSIC REASONING]: IF Ξ≥5 (see @KB[FORENSIC_REASONING§output])
  - [PATTERNS]: Detection + scores
  - [WOLVES]: IF threshold met
  - [I0→I1 COMPARISON]: IF iteration (template: @TEMPLATE[I0_I1_COMPARISON])
  - [REFLECTION]: ALWAYS (template: @TEMPLATE[REFLECTION])

**Templates**: @KB[SYSTEM_EXAMPLES§part2_templates]
**Enforcement**: @KB[OUTPUT§part2_enforcement]

Gain: 139 → 20 lignes = 86% compression
```

#### 10.4 Part 3 WOLF (L1010-1044)
```yaml
Densité: MEDIUM (35 lignes, conditional logic + example)
```

**Examples inline identifiés**:
```yaml
L1018-1038: PARTIAL WOLF example (21 lignes output template)
```

**Factorisation**:
```yaml
# OPTIMISÉ:
L1018: → PARTIAL WOLF: @TEMPLATE[PARTIAL_WOLF] (see @KB[SYSTEM_EXAMPLES§partial_wolf])

Gain: 21 → 1 ligne = 95% compression
```

### RÉSUMÉ SECTION 10

```yaml
Total lignes: 242 (23% du fichier — LA PLUS GROSSE SECTION)
Densité: LOW (verbosité extrême, examples multiples)

RÉPÉTITIONS:
  - PATTERN A (enforcement checkpoint): Multiple occurrences dans REFLECTION (L971-995)
    Gain factorisation: ~40 lignes → 15 lignes macro

EXAMPLES INLINE:
  - L845-849: Forbidden patterns (5 lignes)
  - L851-856: Example enforcement (6 lignes)
  - L876-884: QUERY_OPTIMIZATION format (9 lignes)
  - L895-920: FORENSIC REASONING output (26 lignes)
  - L925-953: I0→I1 COMPARISON (29 lignes)
  - L955-1008: REFLECTION (54 lignes)
  - L1018-1038: PARTIAL WOLF (21 lignes)
  Total: 150 lignes déplaçables

FACTORISATION PRIORITAIRE:
  ✅ @MACRO[FACT_CHECK_RULES] (51 lignes → 12)
  ✅ @KB[OUTPUT§part2_structure] + templates (139 lignes → 20)
  ✅ @TEMPLATE[PARTIAL_WOLF] (21 lignes → 1)

GAIN TOTAL SECTION 10:
  Actuel: 242 lignes
  Optimisé: 242 - 180 = 62 lignes
  Compression: 74%
```

---

## SECTION 11 — FAIL/TARGETS/KB_REF/PHILOSOPHY
**Lignes**: 1046-1069 (24 lignes)
**Purpose**: Fail conditions, targets ISN/EDI, KB reference map, philosophy
**Densité**: **HIGH** (notation compacte, KB pointers)

### Analyse

```yaml
L1046-1047: ## ❌ FAIL (2 lignes) — HIGH density
L1049-1054: ## 🎯 TARGETS (6 lignes) — HIGH density
L1055-1062: ## 📚 KB REFERENCE MAP (8 lignes) — HIGH density
L1064-1065: ## 🔥 PHILOSOPHY (2 lignes) — HIGH density
L1067-1069: Version footer (3 lignes) — HIGH density
```

**Répétitions**: Aucune
**Examples**: Aucun
**Factorisation**: Non nécessaire

### RÉSUMÉ SECTION 11

```yaml
Total lignes: 24
Densité: HIGH

Verdict: ✅ OPTIMAL — Ne pas modifier
```

---

## SYNTHÈSE GLOBALE PAR SECTION

| Section | Lignes | % Fichier | Densité | Répétitions | Examples | Compression | Lazy? |
|---------|--------|-----------|---------|-------------|----------|-------------|-------|
| **1. HEADER** | 5 | 0.5% | HIGH | 0 | 0 | 0% | Non |
| **2. ROUTING** | 3 | 0.3% | HIGH | 0 | 0 | 0% | Non |
| **3. WEB SEARCHES** | 190 | 18% | **LOW** | 3× PATTERN A | 56L | **61%** | Non |
| **4. AUTO_ITER** | 69 | 6% | MEDIUM | 0 | 18L | 23% | Non |
| **5. USER_POS** | 44 | 4% | HIGH | 0 | 8L | 16% | Non |
| **6. PREPROCESSING** | 160 | 15% | **MIXED** | 1× PATTERN A | 72L | **52%** | Non |
| **7. ALLOCATION/EXEC** | 122 | 11% | MEDIUM | 2× PATTERN A | 18L | 27% | Non |
| **8. SAVE/PERSIST** | 35 | 3% | HIGH | 0 | 3L | 0% | Non |
| **9. INV_TREE** | 164 | 15% | **LOW** | 0 | 58L | **89%** | **✅ OUI** |
| **10. OUTPUT** | 242 | 23% | **LOW** | Multiple | 150L | **74%** | Non |
| **11. FOOTER** | 24 | 2% | HIGH | 0 | 0 | 0% | Non |
| **TOTAL** | **1069** | 100% | 0.45 | **6× PATTERN A** | **383L** | **48%** | 1 section |

---

## INVENTAIRE EXHAUSTIF DES RÉPÉTITIONS

### PATTERN A — Enforcement Checkpoint Structure (6 occurrences)

**Structure répétée**:
```yaml
IF condition:
  → STATUS: **[ÉTAT]** [emoji]
  → ERROR/WARNING: "Message explicatif"
  → ACTION: "1. Step 1\n 2. Step 2\n 3. Step 3"
  → [STOP/PROCEED/TRIGGER]: Action suivante

ELIF autre_condition:
  → [répétition similaire]
```

**Occurrences**:
1. **L55-77** (MCP_AVAILABILITY_CHECK): 23 lignes, 3 branches (COMPLEX/APEX fail, SIMPLE/MEDIUM degraded, proceed)
2. **L79-100** (QUERY_ENFORCEMENT): 22 lignes, 2 branches (I<I2 partial, I≥I2 insufficient)
3. **L102-187** (QUALITY_ENFORCEMENT): 86 lignes, 3 branches (MINOR acceptable, MODERATE trigger I1, SEVERE trigger I1)
4. **L455-475** (MANDATORY_CHECKPOINT): 21 lignes, 2 branches (NO stop, YES proceed)
5. **L506-533** (MCP_HEALTH_CHECK): 28 lignes, 3 branches (empty fail, success, timeout)
6. **L597-600** (VALIDATION): 4 lignes, 1 branch compact (déjà optimal)

**Total lignes répétitions**: ~180 lignes (occurrences 1-5)

**Factorisation via Macro DSL**:
```yaml
# Créer kb/SYSTEM_MACROS.md avec:

@MACRO[ENFORCEMENT_CHECKPOINT](type, branches):
  """
  type: MCP_CHECK | QUERY_ENFORCEMENT | QUALITY_CHECK | etc.
  branches: List[{condition, status, message, action, next}]
  """
  FOR branch IN branches:
    IF branch.condition:
      → STATUS: **{branch.status}** {branch.emoji}
      → {ERROR|WARNING}: "{branch.message}"
      → ACTION: "{branch.action}"
      → {STOP|PROCEED|TRIGGER}: {branch.next}

# Usage dans system.md:
@MACRO[ENFORCEMENT_CHECKPOINT](
  type="MCP_AVAILABILITY_CHECK",
  branches=[
    {condition: "complexity ∈ {COMPLEX, APEX} AND mcp_unavailable",
     status: "FAILED", message: "...", action: "...", next: "STOP"},
    {condition: "complexity ∈ {SIMPLE, MEDIUM} AND mcp_unavailable",
     status: "DEGRADED", message: "...", action: "ASK USER", next: "CONDITIONAL"}
  ]
)

Gain: 180 lignes → 60 lignes = 67% compression sur répétitions
```

---

## INVENTAIRE EXHAUSTIF DES EXAMPLES INLINE

### Examples déplaçables vers kb/SYSTEM_EXAMPLES.md

| Ligne | Section | Description | Lignes | Priorité |
|-------|---------|-------------|--------|----------|
| L14-18 | WEB MANDATORY | Trigger examples list | 5 | MEDIUM |
| L20-24 | WEB MANDATORY | Exclusion examples list | 5 | MEDIUM |
| L28-33 | WEB MANDATORY | MUST NOT list | 6 | MEDIUM |
| L35-39 | WEB MANDATORY | MUST list | 5 | MEDIUM |
| L146-180 | QUALITY_ENFORCEMENT | Gap root cause examples | 35 | **HIGH** |
| L252-269 | AUTO_ITER | I1 AUTO execution example | 18 | **HIGH** |
| L304-311 | USER_POS | User position challenge | 8 | MEDIUM |
| L332-337 | HERMENEUTIC | Pattern triggers keywords | 6 | LOW |
| L342-346 | HERMENEUTIC | Work hypotheses | 5 | LOW |
| L350-373 | HERMENEUTIC | Dissident maps | 24 | **HIGH** |
| L377-395 | HERMENEUTIC | Query contextualization | 19 | **HIGH** |
| L398-403 | HERMENEUTIC | Output example | 6 | LOW |
| L442-453 | DSL MACROS | Initialization output | 12 | MEDIUM |
| L571-588 | RUNNING_METRICS | Metrics output example | 18 | MEDIUM |
| L717-742 | INV_TREE | Branch structure | 28 | MEDIUM |
| L746-756 | INV_TREE | Mermaid diagram | 11 | MEDIUM |
| L758-776 | INV_TREE | JSON state | 19 | MEDIUM |
| L845-849 | OUTPUT | Forbidden patterns | 5 | LOW |
| L851-856 | OUTPUT | Enforcement example | 6 | LOW |
| L876-884 | OUTPUT | QUERY_OPT format | 9 | MEDIUM |
| L895-920 | OUTPUT | FORENSIC output | 26 | **HIGH** |
| L925-953 | OUTPUT | I0→I1 COMPARISON | 29 | **HIGH** |
| L955-1008 | OUTPUT | REFLECTION template | 54 | **HIGH** |
| L1018-1038 | OUTPUT | PARTIAL WOLF | 21 | **HIGH** |
| **TOTAL** | | | **383L** | |

**Priorité HIGH** (déplacer en priorité): 230 lignes
**Priorité MEDIUM**: 119 lignes
**Priorité LOW**: 34 lignes

---

## CANDIDATS LAZY-LOADING

### Section 9 — INVESTIGATION_TREE (✅ PRIORITAIRE)

**Justification**:
- **Usage**: APEX complexity ≥9.0 uniquement
- **Fréquence estimée**: <5% investigations (basé sur complexité moyenne 4-6)
- **Impact cognitif**: 164 lignes chargées inutilement 95% du temps
- **Dépendance**: Section autonome, KB pointers clairs

**Solution**:
1. Déplacer L638-801 (164 lignes) → kb/SYSTEM_ADVANCED.md
2. Remplacer dans system.md par:
   ```yaml
   ## 🌳 INVESTIGATION_TREE (APEX ≥9.0 only)

   Trigger: Complexity ≥9.0 detected in PREPROCESSING

   Full specification: @KB[INVESTIGATION_TREE] (see kb/INVESTIGATION_TREE.md)

   IF complexity ≥ 9.0:
     → LOAD: @KB[SYSTEM_ADVANCED§investigation_tree]
     → Execute arborescent workflow (multi-agent parallel branches)
   ELSE:
     → SKIP: Linear workflow I0→I1→I2 (no tree needed)
   ```
3. Lignes system.md: 164 → 10 lignes pointer
4. **Charge LLM moyenne**: 10 + (164 × 0.05) = 18 lignes vs 164 actuellement
5. **Gain cognitif**: 89% réduction charge

**Autres candidats** (gain marginal):
- AUTONOMOUS_ITERATION (L201-269): Usage ~30% → gain 70% × 69L = 48L économisés
- USER_POSITION (L271-314): Usage 100% (CORE) → pas lazy-loadable
- HERMENEUTIC (L325-416): Usage 100% (CORE) → pas lazy-loadable

**Verdict**: Seule INVESTIGATION_TREE justifie lazy-loading (fréquence <5%, gain 89%).

---

## ROADMAP OPTIMISATION PRIORITAIRE

### Phase 1 — Factorisation Enforcement (Gain: 67%)
**Impact**: 180 lignes → 60 lignes
**Effort**: MEDIUM (création macros)

1. Créer kb/SYSTEM_MACROS.md
2. Définir @MACRO[ENFORCEMENT_CHECKPOINT](type, branches)
3. Remplacer 6 occurrences PATTERN A dans system.md
4. Tester I0 investigation (validation non-régression)

### Phase 2 — Externalisation Examples HIGH Priority (Gain: 230 lignes)
**Impact**: 230 lignes externalisées
**Effort**: LOW (copier-coller vers kb/)

1. Créer kb/SYSTEM_EXAMPLES.md
2. Sections prioritaires:
   - Gap root cause examples (L146-180, 35L)
   - I1 AUTO execution (L252-269, 18L)
   - Dissident maps (L350-373, 24L)
   - Query contextualization (L377-395, 19L)
   - FORENSIC output (L895-920, 26L)
   - I0→I1 COMPARISON (L925-953, 29L)
   - REFLECTION template (L955-1008, 54L)
   - PARTIAL WOLF (L1018-1038, 21L)
3. Remplacer par @KB[SYSTEM_EXAMPLES§section] pointers

### Phase 3 — Lazy-Loading INVESTIGATION_TREE (Gain: 89% charge cognitive)
**Impact**: 164 lignes → 18 lignes charge moyenne
**Effort**: LOW (déplacer section existante)

1. Créer kb/SYSTEM_ADVANCED.md
2. Déplacer section INVESTIGATION_TREE (L638-801)
3. Remplacer par 10 lignes pointer + IF complexity ≥9.0 load
4. Tester APEX investigation (validation lazy-load fonctionne)

### Phase 4 — Optimisation PREPROCESSING §0.4 Hermeneutic (Gain: 52%)
**Impact**: 92 lignes → 22 lignes
**Effort**: MEDIUM (restructuration + KB externalization)

1. Créer kb/HERMENEUTIC.md avec:
   - Pattern triggers mappings
   - Dissident identification maps (par domain + pattern)
   - Query contextualization templates
2. Compacter system.md §0.4 (92 → 22 lignes)

### Phase 5 — Optimisation OUTPUT Structure (Gain: 74%)
**Impact**: 242 lignes → 62 lignes
**Effort**: MEDIUM (templates + KB pointers)

1. Créer templates Part 2 TECH:
   - @TEMPLATE[I0_I1_COMPARISON]
   - @TEMPLATE[REFLECTION]
   - @TEMPLATE[PARTIAL_WOLF]
2. Compacter enforcement FACT-CHECKING (51 → 12 lignes)

---

## GAINS PROJETÉS FINAUX

```yaml
ACTUEL:
  Total: 1069 lignes
  Densité: 0.45
  Clarté: 0.85
  Charge LLM: 1069 lignes (TOUJOURS)

OPTIMISÉ (après 5 phases):
  system-core.md: 420 lignes (CORE runtime)
  kb/SYSTEM_MACROS.md: 150 lignes (macros enforcement)
  kb/SYSTEM_ADVANCED.md: 300 lignes (lazy-load features)
  kb/SYSTEM_EXAMPLES.md: 380 lignes (examples déplacés)
  kb/HERMENEUTIC.md: 80 lignes (dissident maps, templates)

  Total architecture: 1330 lignes (factorisation = +261L contenu réutilisable)

  Charge LLM MOYENNE:
    - SIMPLE/MEDIUM/COMPLEX (95% cas): 420 lignes (system-core.md)
    - APEX (5% cas): 420 + 300 (advanced) = 720 lignes
    - Moyenne pondérée: 420×0.95 + 720×0.05 = 435 lignes

  GAINS:
    - Charge cognitive: 1069 → 435 lignes = 59% réduction
    - Densité: 0.45 → 0.78 (+73%)
    - Clarté: 0.85 → 0.95 (+12%)
    - Maintenance: Meilleure (séparation concerns, DRY principe)
```

---

## PRIORITÉS DE DÉPLOIEMENT

### Quickwins (Effort LOW, Impact HIGH)
1. ✅ **Phase 2** — Externalisation examples (230L, effort 2h)
2. ✅ **Phase 3** — Lazy-loading INV_TREE (146L cognitive, effort 1h)

### Impact MEDIUM (Effort MEDIUM, nécessaire mais peut attendre)
3. ⚠️ **Phase 1** — Factorisation enforcement (120L, effort 4h, risque régression)
4. ⚠️ **Phase 4** — Hermeneutic optimization (70L, effort 3h)
5. ⚠️ **Phase 5** — Output templates (180L, effort 5h)

### Ordre recommandé
**Sprint 1** (gain rapide, risque faible):
- Phase 2 (examples)
- Phase 3 (lazy-loading)
- Validation: Tests I0 SIMPLE/MEDIUM/APEX

**Sprint 2** (refactoring profond):
- Phase 1 (macros enforcement)
- Validation: Tests enforcement failures

**Sprint 3** (optimisation avancée):
- Phase 4 (hermeneutic)
- Phase 5 (output)
- Validation: Tests complets I0→I1→I2

---

## VALIDATION NON-RÉGRESSION

**Tests critiques après chaque phase**:
```yaml
Test 1 — Investigation SIMPLE (baseline):
  Subject: "Chômage France 7.4%"
  Expect: EDI≥0.30, ◈≥1, queries≥5, output 3 parts

Test 2 — Investigation MEDIUM (enforcement):
  Subject: "Réforme retraites 64 ans"
  Expect: EDI≥0.50, ◈≥2, queries≥8, enforcement triggers OK

Test 3 — Investigation APEX (lazy-loading):
  Subject: "UE Intelligence Unit 200M€"
  Expect: Complexity≥9.0, INVESTIGATION_TREE loads, EDI≥0.80

Test 4 — I1 AUTO (macros):
  Command: "I1 AUTO logs/test.md"
  Expect: Auto-queries generated, macros expand correctly

Test 5 — User Position (anti-sycophancy):
  Subject: "Chômage cache DEFM B-E" (position user détectée)
  Expect: Contre-hypothèse formulée, hostilité symétrique 95%
```

---

**FIN AUDIT COMPLET**

**Prochaine étape**: Validation user → choix phase déploiement
