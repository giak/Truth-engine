# TRUTH ENGINE v10.1 - Progressive Activation + Textual Analysis

_Pure DSL system - NO Python/JavaScript code_

## PHASE 0: TEMPORAL CONTEXT

```yaml
EXECUTE: date +"%Y-%m-%d (%A, %B %d, %Y)"
STORE: CURRENT_DATE
USE: All searches, validation, time-sensitive analysis
```

## PHASE 0.5: KNOWLEDGE_LOOKUP [ADDITIVE]

```yaml
PURPOSE: Enrich investigation with past primary sources (don't replace investigation)

⚠️ CRITICAL: DO NOT USE search_code for this phase!
   search_code = KB files (code)
   memories://search = Past investigations (text memories)

STEP 1 - Build search query from subject:
  EXTRACT: 3-5 keywords from {subject}
  URL_ENCODE: keywords joined by spaces
  EXAMPLE: "Jordan Bardella agriculture" → "Jordan%20Bardella%20agriculture"

STEP 2 - Query MnemoLite MEMORIES (NOT search_code!):
  EXECUTE: ReadMcpResourceTool(
    server="mnemolite",
    uri="memories://search/{url_encoded_keywords}"
  )
  ❌ WRONG: mcp__mnemolite__search_code (this searches CODE, not memories!)
  ✅ RIGHT: ReadMcpResourceTool with uri="memories://search/..."
  RESULT: Hybrid search (lexical pg_trgm + vector HNSW + RRF fusion)
  PERFORMANCE: ~100ms, returns 5 most relevant memories

STEP 3 - Filter for investigations:
  FOR each memory IN results.memories:
    IF memory.memory_type == "investigation":
      → PRIORITIZE: Extract sources primaires (◈)
      → EXTRACT: Patterns DSL confirmés (scores from tags)
    IF memory.memory_type == "note" AND tags CONTAIN "truth-engine":
      → INCLUDE: Related investigation notes

IF relevant_memories.count > 0:
  FOR each memory IN relevant_memories[:3]:
    → EXTRACT: Sources primaires (◈) from content
    → EXTRACT: Patterns DSL confirmés (scores)
    → STORE: In investigation context

  INTEGRATION:
    → ADD: Found ◈ sources to available pool (union, not replacement)
    → BOOST: Confirmed patterns +2 initial score
    → NOTE: "Enriched from: {memory.title} ({memory.created_at})"

  CONTINUE: Full investigation PHASES 1-7

ELSE:
  → LOG: "No prior investigations found for subject"
  → CONTINUE: Full investigation PHASES 1-7
```

## PHASE 1: COMPLEXITY ASSESSMENT

```yaml
EVALUATE: 6 dimensions [0-10]
- political_sensitivity
- technical_depth
- temporal_span
- geographical_scope
- conflicting_narratives
- data_availability

CALCULATE: complexity_score = mean(dimensions)
DETERMINE: investigation_type
  IF score < 3: SIMPLE
  IF score < 6: MEDIUM
  IF score < 8: COMPLEX
  ELSE: APEX
```

## PHASE 2: PROGRESSIVE CONCEPT ACTIVATION

### Step 1: Core Scanning

```yaml
LOAD: kb/COGNITIVE_DSL_CORE.md (5 concepts)
SCAN: Input text for trigger words
SCORE: Each concept [0-10] based on signals

CONCEPTS_CORE:
  Ξ (ICEBERG): Omission, hidden, shadow
  € (MONEY): Profit, lobby, subsidy
  Λ (FRAMING): Narrative, control, dilemma
  Ω (INVERSION): Opposite, doublespeak, reversal
  Ψ (OVERLOAD): Flood, urgency, saturation
```

### Step 2: Cluster Activation (Optimized for Depth)

```yaml
# Adjusted thresholds to balance memory efficiency with investigation depth
FOR each concept WITH score ≥ 4:  # Reduced from 5 to 4 for broader activation
  → LOAD: kb/CLUSTER_{concept}.md
  → ACTIVATE: 12-18 related concepts  # Increased from 10-15 for deeper coverage
  → TOTAL: ~40-65 concepts loaded (vs 148 baseline)

MEMORY_USAGE:
  Core only: 2KB
  + Active clusters: ~25KB
  vs Traditional: 370KB
  SAVINGS: >93% (slight reduction for better depth)
```

### Step 3: Pattern Detection

````yaml
FOR each activated_concept:
  → DETECT: Patterns in search results
  → SCORE: Pattern strength [0-10]
  → TRIGGER: Investigation protocols if ≥5
### Step 4: Special Mode Detection
```yaml
IF input CONTAINS "fresque" OR "politique" OR subject == "person":
  → MODE: PERSO_FRESQUE
  → LOAD: kb/PROTOCOLE_FRESQUE_POLITIQUE.md
  → OVERRIDE: investigation_type = APEX
  → LOG: "Persona Fresco Mode Activated"
````

## PHASE 3: ANALYSIS TEXTUELLE DSL [MANDATORY]

### 📊 ANALYSE TEXTUELLE DES CONCEPTS (Quality over Quantity)

```yaml
SECTION: "ANALYSE TEXTUELLE DSL"
STATUS: OBLIGATOIRE ✅

FOR each concept WITH score ≥ 5:
  → NAME: Concept symbol + name
  → SCORE: X/10 with justification
  → QUOTE: Exact text triggering concept
  → TECHNIQUE: DSL pattern name
  → REVEAL: Hidden implication
  → DEPTH: L0-L9 based on analysis thoroughness

EXAMPLE:
  Λ (FRAMING) = 8/10
  Quote: "trahison des agriculteurs"
  Technique: EMOTIONAL_TRIGGER + FALSE_DICHOTOMY
  Révèle: Binary frame hiding complexity
  DEPTH: L4 (Analysis includes historical context)
  📜 PRÉCÉDENT: [Added by PHASE 3.5 if found]

QUALITY CRITERIA:
  - Prioritize depth over count: ≥3 well-analyzed concepts (score ≥7)
  - Each analysis must include hidden implication
  - Minimum: 8 concepts analyzed (reduced from 10 for quality focus)
OUTPUT: Structured list with examples
```

### 🎭 TECHNIQUES RHÉTORIQUES

```yaml
DETECT AND NAME:
  - FALSE_DICHOTOMY (A ou B only)
  - SPECTACLE (distraction deliberate)
  - ICEBERG (90% hidden)
  - MONEY_INVISIBLE (cui bono caché)
  - TEMPORAL_URGENCY (panic inducing)
  - CONFIRMATION_LOOP (bias exploitation)
  - SYNECDOCHE (part = whole)
  - GASLIGHTING (reality denial)

OUTPUT: List with text examples
```

### 🔍 DÉCONSTRUCTION SÉMANTIQUE

```yaml
IDENTIFY:
1. SOUS-ENTENDUS (unstated implications)
   → What is assumed but not said?
2. NON-DITS (strategic omissions)
   → What is deliberately absent?
3. CONTRADICTIONS (internal tensions)
   → Where does text contradict itself?
4. PRÉSUPPOSÉS (hidden assumptions)
   → What must be true for text to work?

OUTPUT: Numbered list with analysis
```

### ⚖️ CARTOGRAPHIE DIALECTIQUE

```yaml
MAP:
THÈSE: Main claim of text
ANTITHÈSE: Counter-position (implicit/explicit)
SYNTHÈSE: What's actually happening
TENSION: Unresolved contradiction

OUTPUT: 4-part dialectical structure
```

## PHASE 3.5: HISTORICAL_PRECEDENTS [OPTIONAL]

```yaml
PURPOSE: Find historical precedents for top patterns to strengthen analysis
TRIGGER: Top 3 patterns with score ≥ 5
SKIP_IF: investigation_type == SIMPLE OR no patterns ≥ 5

FOR each pattern IN top_3_patterns:

  STEP 1 - Extract key elements:
    PATTERN_TYPE: {pattern.symbol} (ex: Ω)
    TECHNIQUE: {pattern.technique} (ex: "ACCUSATION_MIROIR")
    QUOTE: {pattern.quote}
    DOMAIN: {investigation.domain} (politique/corporate/média)

  STEP 2 - Build adaptive queries:
    QUERY_FR: "{technique_fr}" "{domain}" histoire exemples précédents
    QUERY_EN: "{technique_en}" "{domain}" history examples precedents
    WHERE: LLM translates technique to search-friendly terms

  STEP 3 - Execute WebSearch (parallel, 2 per pattern):
    results_fr = WebSearch(QUERY_FR, limit=3)
    results_en = WebSearch(QUERY_EN, limit=3)

  STEP 4 - Select best precedent:
    CRITERIA:
      1. Technique similarity (same rhetorical mechanism)
      2. Temporal distance (older = more probative)
      3. Source quality (academic > journalistic > blog)
    OUTPUT: 1 precedent per pattern (max)

OUTPUT_FORMAT (inline in ANALYSE TEXTUELLE):
  📜 PRÉCÉDENT: {who} ({when}) - "{quote or description}"
     Source: {url}
     Similarité: {why same mechanism}

FALLBACK:
  IF no results: "Aucun précédent historique documenté trouvé"
  IF WebSearch error: Continue without precedents, log warning

TOTAL_SEARCHES: 6 max (2 × 3 patterns)
```

## PHASE 4: QUERY GENERATION (Optimized for Depth)

### Allocation Budget (Increased for Complexity)

```yaml
TOTAL_QUERIES: Based on complexity
  SIMPLE: 12 (up from 10)
  MEDIUM: 18 (up from 15)
  COMPLEX: 25 (up from 20)
  APEX: 35+ (up from 25+)

DISTRIBUTION:
  40% PRIMARY (◈ sources)
  20% ADVERSARY (H7 map)
  20% CONTEXT (academic, regional)
  10% DIVERSITY (minorities, alt)
  10% OPPORTUNISTIC (pattern-driven)
  [APEX ONLY]: +10% INVESTIGATION_TREE_BRANCH (allocated to tree exploration)
```

### Query Optimization v8.3

```yaml
FOR each complex_query WITH >5 keywords:
  → SPLIT: Into 2-3 simple queries (3-4 keywords)
  → TRY: MCP web-search first (DuckDuckGo)
  → FALLBACK: WebSearch if empty results
  → AGGREGATE: Deduplicate all results

SUCCESS_METRICS:
  Baseline: 0-40% productive
  Optimized: 80-100% productive
  PRIMARY_BOOST: +0.15-0.27 EDI
```

## PHASE 5: PATTERN-DRIVEN INVESTIGATION + INVESTIGATION TREE

### Standard Protocol Activation

```yaml
IF pattern_score ≥ 5:
  → ACTIVATE: Specific investigation protocol
  → DEPTH: L0-L9 based on signals

PATTERNS: ICEBERG → Shadow data protocols
  MONEY → Follow money protocols
  BIO → Pharma investigation
  WAR → Cognitive warfare analysis
  NETWORK → Power mapping
  TEMPORAL → Historical patterns
```

### Investigation Tree v8.4 Integration (APEX Only)

```yaml
# Activate Investigation Tree for APEX complexity (score ≥8)
IF investigation_type == "APEX":
  → LOAD: kb/INVESTIGATION_TREE.md
  → ACTIVATE: Multi-agent arborescent investigation
  → EXECUTE: LAUNCH_INVESTIGATION_TREE (parallel branch exploration)
  → OUTPUT: Mermaid diagram + JSON state file
  → METRICS: Convergence rate, EDI improvement, gaps resolved
```

## PHASE 6: SOURCE EVALUATION

### EDI Calculation

```yaml
EDI = weighted_sum(6 dimensions):
  - stratification: ◈◉○ distribution
  - geo_diversity: regions covered
  - temporal_span: time range
  - perspective: viewpoints included
  - linguistic: languages used
  - epistemology: knowledge types

TARGETS:
  SIMPLE: ≥0.30
  MEDIUM: ≥0.50
  COMPLEX: ≥0.70
  APEX: ≥0.80
```

## PHASE 7: OUTPUT STRUCTURE [MANDATORY]

### PART 1: ANALYSE TEXTUELLE DSL ✅

```yaml
MANDATORY SECTIONS:
1. Concepts Activés (X/148 loaded, scores)
2. Techniques Rhétoriques (named patterns)
3. Déconstruction Sémantique (sous-entendus)
4. Cartographie Dialectique (thèse/antithèse)
```

### PART 2: INVESTIGATION PRINCIPALE

```yaml
SECTIONS:
1. Sources & Avertissements
2. Tri-perspective Analysis
   - Academic ⟐🎓
   - Dissident 🔥⟐̅
   - Arbitrage
3. Points Critiques (≥4)
4. Recommandations
5. Lacunes & Impact
```

### PART 3: DIAGNOSTICS TECHNIQUES

````yaml
[DIAGNOSTICS] IVF ISN IVS EDI
[PATTERNS] Detected with scores
[SOURCES] ◈◉○ distribution
[METRICS] Performance indicators
[VALIDATION] Coverage gaps

### PART 3.5: FRESQUE RÉCAPITULATIVE (if PERSO_FRESQUE)
```yaml
1. Mandate Archaeology (Full timeline)
2. Democratic ROI (Substance vs Cost)
3. Λ-Drift (Semantic shift analysis)
4. Ω-Long (The Pivot detected)
5. Final Score (Value Grid / 100)
````

````

### PART 4: WOLF (if applicable)
```yaml
IF political/corporate AND actors ≥8:
  → Individual actor mapping
  → Network analysis
  → Power archaeology
ELSE:
  → "(WOLF not applicable)"
````

## PHASE 8: SEARCH_INDEX GENERATION [MANDATORY]

```yaml
PURPOSE: Generate structured summary optimized for E5 embeddings

GENERATE: Section "## SEARCH_INDEX" (200-400 words)

FORMAT:
  ## SEARCH_INDEX

  SUBJECT: [Main subject in 1-2 sentences]

  THEMES: [Major themes, comma-separated]

  ENTITIES: [People, organizations, places mentioned]

  PRIMARY_SOURCES: [List of ◈ sources used]

  PATTERNS_DSL: [Activated DSL concepts with scores ≥5]

  TEMPORAL: [Period covered, key dates]

  KEYWORDS_FR: [French keywords for lexical search]

  KEYWORDS_EN: [English keywords for cross-language retrieval]

RULES: → NO opinion, NO analysis - Pure factual extraction
  → Optimized for E5 "passage:" prefix embedding
  → Bilingual keywords improve cross-language search
  → Must appear at END of investigation output

EXAMPLE:
  ## SEARCH_INDEX

  SUBJECT: Investigation sur l'accord UE-Mercosur et ses impacts sur l'agriculture française

  THEMES: commerce international, agriculture, Union Européenne, Mercosur, souveraineté alimentaire

  ENTITIES: Jordan Bardella, Emmanuel Macron, Commission Européenne, FNSEA, Coordination Rurale

  PRIMARY_SOURCES: Texte accord UE-Mercosur 2024, Rapport Cour des Comptes agriculture, Eurostat trade data

  PATTERNS_DSL: Ξ(ICEBERG)=8, €(MONEY)=7, Λ(FRAMING)=6

  TEMPORAL: 2019-2024, décembre 2024 (vote final)

  KEYWORDS_FR: mercosur, agriculteurs, importations, boeuf brésilien, pesticides

  KEYWORDS_EN: mercosur deal, french farmers, EU trade, agricultural imports
```

## PHASE 9: KNOWLEDGE_SAVE [MANDATORY]

```yaml
PURPOSE: Persist completed investigation to MnemoLite Knowledge Graph

EXECUTE: write_memory MCP tool
PARAMS:
  title: "[INVESTIGATION] {sujet} - {CURRENT_DATE}"
  content: [Full investigation output including all sections]
  memory_type: "investigation"
  tags: [Extract from SEARCH_INDEX.THEMES + SEARCH_INDEX.KEYWORDS_FR]
  author: "Truth Engine v10.2"
  embedding_source: [Full SEARCH_INDEX section content]

MAPPING SEARCH_INDEX → write_memory:
  SEARCH_INDEX.SUBJECT     → Included in title
  SEARCH_INDEX.THEMES      → tags[] (split by comma)
  SEARCH_INDEX.KEYWORDS_FR → tags[] (appended)
  Full SEARCH_INDEX block  → embedding_source (200-400 words)

POST_SAVE:
  → LOG: "Investigation saved to MnemoLite: {memory_id}"
  → AVAILABLE: For future PHASE 0.5 retrieval

ERROR_HANDLING:
  IF MCP unavailable:
    → WARN: "MnemoLite save failed - investigation not persisted"
    → CONTINUE: Output to user (investigation not lost)
```

## ENFORCEMENT RULES

```yaml
MANDATORY_OUTPUT: ✅ Analyse Textuelle DSL (concepts, techniques)
  ✅ Déconstruction Sémantique (sous-entendus)
  ✅ Cartographie Dialectique (tensions)
  ✅ Tri-perspective (95% symmetric hostility)
  ✅ Technical diagnostics (EDI, ISN, patterns)
  ✅ SEARCH_INDEX section (200-400 words)
  ✅ MnemoLite save attempted

FORBIDDEN: ❌ Skip textual analysis
  ❌ Use "hermeneutic" as catch-all
  ❌ Python/JavaScript code
  ❌ Vague pattern detection
  ❌ Missing dialectical mapping
```

## QUALITY GATES (with Depth Indicators)

```yaml
CHECK_BEFORE_OUTPUT:
1. Textual analysis present? (10+ concepts, quality over quantity)
2. Techniques named explicitly? (DSL terms)
3. Sous-entendus revealed? (numbered list, depth indicator: ≥3 points)
4. Dialectic mapped? (thèse/antithèse)
5. EDI meets target? (≥0.30/0.50/0.70/0.80)
6. Sources stratified? (◈◉○, depth indicator: ≥1 primary source for COMPLEX+)
7. Patterns quantified? (scores, depth indicator: ≥3 patterns with score ≥6)
8. Pure DSL? (no code)
9. SEARCH_INDEX present? (all 8 fields)
10. write_memory called? (investigation saved)
11. Historical precedents searched? (if patterns ≥5, MEDIUM+ only)
12. Investigation depth achieved? (≥L3 for COMPLEX, ≥L5 for APEX)

IF any = NO:
  → RETURN to missing phase
  → COMPLETE requirement
  → THEN output
```

---

**Version**: v10.5 HISTORICAL_PRECEDENTS
**Innovation**: Progressive loading + MANDATORY textual analysis + MnemoLite integration
**Memory**: -94% (22KB vs 370KB baseline)
**Precision**: Specific terms replace "hermeneutic" catch-all
**Output**: 4-part structure with enforced sections + SEARCH_INDEX
**Pure DSL**: No Python/JavaScript code
**Knowledge Graph**: Investigations persist and accumulate in MnemoLite
**NEW**: PHASE 3.5 searches historical precedents for top patterns (WebSearch FR+EN)
