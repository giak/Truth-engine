# Substack Engine v2.0 - Design Document

**Date**: 2025-11-27
**Version**: 2.0
**Status**: IMPLEMENTED

## Problem Statement

### Observed Issue

Investigation `logs/2025-11-27_17-49_macron-ukraine-paix-russie.md`:
- Source: **5,530 words** + ICEBERG MAX appendix
- Substack article: **838 words**
- Ratio: Only **15%** of content preserved

### Root Cause

Gate 5 in v1.0 imposed a rigid **800-2000 word limit**:

```yaml
### Gate 5: Length
CHECK:
  - Article: 800-2000 words
FAIL_ACTION:
  IF over → Compress (merge redundancy)
```

This arbitrary limit forced compression of rich APEX investigations, losing:
- Historical precedents (PHASE 3.5)
- ICEBERG MAX deep analysis
- Actor networks (Wolves)
- Pattern documentation
- Primary source details

### User Feedback

> "la longueur de l'article est souvent (je trouve) trop court. nous avons souvent au moins 2 enquetes, et j'ai l'impression que l'écriture passe à coté ou omet de choses."

> "C mais il faut laisser le LLM décider aussi, il sait mieux écrire et résumer les enquetes que moi"

## Solution Design

### Core Principles

1. **Content Over Format**: Article serves investigation, not arbitrary limits
2. **LLM Autonomy**: LLM decides optimal structure based on content richness
3. **Essential First**: Critical findings must never be omitted
4. **ICEBERG Integration**: Deep layers deserve space in output

### Key Changes

| Aspect | v1.0 | v2.0 |
|--------|------|------|
| Length limit | 800-2000 words (rigid) | 800-6000+ words (adaptive) |
| Decision maker | Rules | LLM autonomous |
| Gate 5 | Length check | Content Integrity |
| Gate 6 | N/A | Coherence |
| ICEBERG MAX | Ignored | Integrated section |
| Content mapping | FactLedger (flat) | ContentMap (structured) |

### Adaptive Length Formula

```yaml
SIMPLE (≤2000 words source):
  → Article: 800-1500 words

MEDIUM (2000-4000 words source):
  → Article: 1500-3000 words

COMPLEX (4000-6000 words source):
  → Article: 3000-5000 words

APEX (6000+ words source):
  → Article: 4000-6000+ words
```

### New Gate 5: Content Integrity

Replaces arbitrary length check with semantic validation:

```yaml
CHECK:
  [ ] All ESSENTIAL elements included
  [ ] No critical revelations omitted
  [ ] Primary sources cited
  [ ] Evidence chain complete
  [ ] Historical precedents included (if found)
  [ ] ICEBERG layers covered (if APEX)
```

### New Gate 6: Coherence

```yaml
CHECK:
  [ ] Article stands alone
  [ ] Narrative flows logically
  [ ] Each section justified
  [ ] Conclusion resonates with intro
```

## Implementation

### Files Created/Modified

1. **NEW**: `prompts/systems/substack-engine-v2.0.md` - Full v2.0 system prompt
2. **UPDATE**: `CLAUDE.md` - Reference v2.0
3. **NEW**: `docs/plans/2025-11-27-substack-engine-v2-design.md` - This document

### Preserved Elements

- All hook formulas (PROVOCATIVE, CONTRARIAN, etc.)
- Markup format for API
- Anti-LLM banned phrases
- Accessibility gates
- API workflow
- Output file structure

### Migration Path

v1.0 commands work unchanged. Same triggers:
- `Mode SUBSTACK: logs/file.md`
- `Mode SUBSTACK DRAFT: logs/file.md`
- `Mode SUBSTACK TWEET: logs/file.md`

## Expected Impact

### For APEX Investigation Example

| Metric | v1.0 | v2.0 Expected |
|--------|------|---------------|
| Source words | 5,530 | 5,530 |
| Article words | 838 | 4,000-5,000 |
| Content ratio | 15% | 70-90% |
| Primary sources | Partial | Complete |
| ICEBERG layers | None | All 4 |
| Precedents | Omitted | Included |

### Quality Improvement

- Readers get the full investigation value
- Primary sources properly documented
- Historical context preserved
- Deep analysis (ICEBERG) accessible
- LLM editorial judgment applied

## Validation Criteria

1. APEX investigations produce 4000+ word articles
2. All ESSENTIAL elements from ContentMap appear in output
3. ICEBERG MAX sections integrated when present
4. Historical precedents from PHASE 3.5 included
5. User checkpoint shows content coverage stats

---

**Approved by**: User (2025-11-27)
**Implemented**: Yes
