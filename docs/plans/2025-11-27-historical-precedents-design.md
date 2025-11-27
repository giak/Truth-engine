# Historical Precedents Module - Design Document

> **For Claude:** Use superpowers:executing-plans to implement this design.

**Date**: 2025-11-27
**Version**: Truth Engine v10.5
**Status**: APPROVED

## Overview

Add a module that automatically finds historical precedents for detected rhetorical patterns, strengthening textual analysis by proving techniques have been used before in other contexts.

**Core insight**: If a pattern (e.g., "accusation miroir") has documented historical precedents, it validates the analysis and shows the technique is deliberate, not coincidental.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Source | WebSearch | Simple, no new infrastructure |
| Trigger | Top 3 patterns ≥5 | Focused, avoids query flood |
| Query format | FR + EN combined | Maximizes result coverage |
| Output | Inline under pattern | Direct connection to analysis |
| Query generation | Dynamic/adaptive | Context-aware, not hardcoded |

## Architecture

### Position in Workflow

```
PHASE 3: ANALYSE_TEXTUELLE_DSL
    ↓
PHASE 3.5: HISTORICAL_PRECEDENTS [NEW]
    ↓
PHASE 4: TRI_PERSPECTIVE
```

### Execution Flow

```yaml
## PHASE 3.5: HISTORICAL_PRECEDENTS [OPTIONAL]

TRIGGER: Top 3 patterns avec score ≥ 5
SKIP_IF: No patterns ≥ 5 OR investigation_type == SIMPLE

FOR each pattern IN top_3_patterns:

  STEP 1 - Extract key elements:
    PATTERN_TYPE: {pattern.symbol} (ex: Ω)
    TECHNIQUE: {pattern.technique} (ex: "ACCUSATION_MIROIR")
    QUOTE: {pattern.quote} (ex: "accuse de collaboration")
    DOMAIN: {investigation.domain} (ex: "politique", "corporate", "média")

  STEP 2 - Build adaptive queries:
    QUERY_FR: "{technique_fr}" "{domain}" histoire exemples précédents
    QUERY_EN: "{technique_en}" "{domain}" history examples precedents

    WHERE:
      technique_fr = LLM translates TECHNIQUE to French search terms
      technique_en = LLM translates TECHNIQUE to English search terms
      domain = Detected domain OR "propagande" as fallback

  STEP 3 - Execute WebSearch (parallel):
    results_fr = WebSearch(QUERY_FR, limit=3)
    results_en = WebSearch(QUERY_EN, limit=3)

  STEP 4 - Select best precedent:
    CRITERIA (priority order):
      1. Technique similarity (same rhetorical mechanism)
      2. Temporal distance (older = more probative)
      3. Source quality (academic > journalistic > blog)

    OUTPUT: 1 precedent per pattern (maximum)

TOTAL_SEARCHES: 6 max (2 per pattern × 3 patterns)
```

## Output Format

### Inline Integration

Precedents appear directly under each pattern in the "ANALYSE TEXTUELLE DSL" section:

```markdown
### ANALYSE TEXTUELLE DSL

Ω (INVERSION) = 8/10
Quote: "accuse de collaboration"
Technique: ACCUSATION_MIROIR
Révèle: Projection de ses propres pratiques sur l'adversaire
📜 PRÉCÉDENT: Goebbels (1934) - "Accuser l'adversaire de ce que l'on fait soi-même"
   Source: https://example.com/propaganda-techniques
   Similarité: Même mécanisme de projection accusatoire en contexte politique

Λ (FRAMING) = 7/10
Quote: "trahison des agriculteurs"
Technique: EMOTIONAL_TRIGGER + FALSE_DICHOTOMY
Révèle: Cadrage binaire masquant la complexité
📜 PRÉCÉDENT: Bush (2001) - "You're either with us or against us"
   Source: https://example.com/false-dichotomy-politics
   Similarité: Faux dilemme forçant un choix binaire
```

### When No Precedent Found

```markdown
Ψ (OVERLOAD) = 6/10
Quote: "..."
Technique: INFORMATION_FLOODING
Révèle: ...
📜 PRÉCÉDENT: Aucun précédent historique documenté trouvé
```

## Error Handling

```yaml
FALLBACK:
  IF WebSearch returns 0 relevant results:
    → SKIP precedent for this pattern
    → NOTE: "Aucun précédent historique documenté trouvé"

  IF WebSearch timeout/error:
    → CONTINUE investigation without precedents
    → LOG in output: "⚠️ Historical search unavailable"

  IF all 3 patterns have no precedents:
    → SKIP entire PHASE 3.5 section
    → No error, just omit from output
```

## Implementation Tasks

### Task 1: Add PHASE 3.5 to system.md

**File**: `/home/giak/projects/truth-engine/system.md`
**Location**: After PHASE 3 (ANALYSE_TEXTUELLE_DSL), before PHASE 4 (TRI_PERSPECTIVE)

Insert the PHASE 3.5 block as defined above.

### Task 2: Update output format in PHASE 3

**File**: `/home/giak/projects/truth-engine/system.md`
**Location**: PHASE 3 output format section

Add the `📜 PRÉCÉDENT:` line format to the pattern output template.

### Task 3: Update ENFORCEMENT RULES

**File**: `/home/giak/projects/truth-engine/system.md`
**Location**: CHECK_BEFORE_OUTPUT section

Add optional check: "Historical precedents searched? (if patterns ≥5)"

### Task 4: Update version

**File**: `/home/giak/projects/truth-engine/system.md`
**Location**: Footer

Update to v10.5 HISTORICAL_PRECEDENTS

### Task 5: Update CLAUDE.md

**File**: `/home/giak/projects/truth-engine/CLAUDE.md`

Document the new PHASE 3.5 in the workflow section.

## Performance Impact

| Metric | Value |
|--------|-------|
| Additional searches | 6 max per investigation |
| Latency added | ~2-5 seconds |
| Applies to | MEDIUM, COMPLEX, APEX only |
| Skip condition | SIMPLE investigations |

## Success Criteria

1. Top 3 patterns with score ≥5 trigger historical search
2. Relevant precedents appear inline under patterns
3. No precedent = graceful skip (no error)
4. WebSearch failure = continue without precedents
5. Output clearly links precedent to detected technique

---

**Approved by**: User (2025-11-27)
**Ready for implementation**: Yes
