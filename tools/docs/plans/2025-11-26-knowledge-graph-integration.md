# Knowledge Graph d'Investigations - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Integrate MnemoLite semantic search into Truth Engine to create a Knowledge Graph of investigations that accumulates and reuses primary sources across investigations.

**Architecture:** Add 3 new phases to system.md: PHASE 0.5 (search past investigations via MCP), PHASE 8 (generate SEARCH_INDEX section), PHASE 9 (save to MnemoLite via write_memory MCP). The system uses MnemoLite's hybrid search (lexical + vector + RRF) with E5-base embeddings for French content.

**Tech Stack:** Truth Engine DSL (system.md), MnemoLite MCP (memories://search, write_memory), E5-base embeddings (768D)

---

## Task 1: Add PHASE 0.5 - KNOWLEDGE_LOOKUP

**Files:**
- Modify: `/home/giak/projects/truth-engine/system.md:9-27` (insert after PHASE 0)

**Step 1: Read current PHASE 0 section**

Verify current structure ends at line ~9 with PHASE 0: TEMPORAL CONTEXT.

**Step 2: Insert PHASE 0.5 after PHASE 0**

Add the following block after line 9 (after PHASE 0 closing ```):

```yaml
## PHASE 0.5: KNOWLEDGE_LOOKUP [ADDITIVE]
```yaml
PURPOSE: Enrich investigation with past primary sources (don't replace investigation)

EXECUTE: ReadMcpResourceTool(
  server="mnemolite",
  uri="memories://search/{sujet_url_encoded}?limit=5&memory_type=investigation"
)

IF results.memories.count > 0:
  FOR each memory IN results.memories[:3]:
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
```

**Step 3: Verify edit preserves PHASE 1 structure**

Ensure PHASE 1: COMPLEXITY ASSESSMENT remains intact starting around line 30.

**Step 4: Commit**

```bash
cd /home/giak/projects/truth-engine
git add system.md
git commit -m "feat(system.md): add PHASE 0.5 KNOWLEDGE_LOOKUP for MnemoLite integration"
```

---

## Task 2: Add PHASE 8 - SEARCH_INDEX GENERATION

**Files:**
- Modify: `/home/giak/projects/truth-engine/system.md` (insert after PHASE 7 OUTPUT STRUCTURE)

**Step 1: Locate PHASE 7 end**

Find the end of PHASE 7: OUTPUT STRUCTURE section (around line 240).

**Step 2: Insert PHASE 8 before ENFORCEMENT RULES**

Add the following block:

```yaml
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

RULES:
  → NO opinion, NO analysis - Pure factual extraction
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
```

**Step 3: Commit**

```bash
cd /home/giak/projects/truth-engine
git add system.md
git commit -m "feat(system.md): add PHASE 8 SEARCH_INDEX generation for optimal embeddings"
```

---

## Task 3: Add PHASE 9 - KNOWLEDGE_SAVE

**Files:**
- Modify: `/home/giak/projects/truth-engine/system.md` (insert after PHASE 8)

**Step 1: Insert PHASE 9 after PHASE 8**

Add the following block:

```yaml
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
```

**Step 2: Commit**

```bash
cd /home/giak/projects/truth-engine
git add system.md
git commit -m "feat(system.md): add PHASE 9 KNOWLEDGE_SAVE to persist investigations"
```

---

## Task 4: Update ENFORCEMENT RULES

**Files:**
- Modify: `/home/giak/projects/truth-engine/system.md` (ENFORCEMENT RULES section)

**Step 1: Add new mandatory outputs**

Update the MANDATORY_OUTPUT block to include:

```yaml
MANDATORY_OUTPUT:
  ✅ Analyse Textuelle DSL (concepts, techniques)
  ✅ Déconstruction Sémantique (sous-entendus)
  ✅ Cartographie Dialectique (tensions)
  ✅ Tri-perspective (95% symmetric hostility)
  ✅ Technical diagnostics (EDI, ISN, patterns)
  ✅ SEARCH_INDEX section (200-400 words) [NEW]
  ✅ MnemoLite save attempted [NEW]
```

**Step 2: Add to CHECK_BEFORE_OUTPUT**

Add items 9 and 10:

```yaml
CHECK_BEFORE_OUTPUT:
1. Textual analysis present? (10+ concepts)
2. Techniques named explicitly? (DSL terms)
3. Sous-entendus revealed? (numbered list)
4. Dialectic mapped? (thèse/antithèse)
5. EDI meets target? (≥0.30/0.50/0.70/0.80)
6. Sources stratified? (◈◉○)
7. Patterns quantified? (scores)
8. Pure DSL? (no code)
9. SEARCH_INDEX present? (all 8 fields) [NEW]
10. write_memory called? (investigation saved) [NEW]
```

**Step 3: Commit**

```bash
cd /home/giak/projects/truth-engine
git add system.md
git commit -m "feat(system.md): update ENFORCEMENT RULES for Knowledge Graph phases"
```

---

## Task 5: Update Version and Footer

**Files:**
- Modify: `/home/giak/projects/truth-engine/system.md` (footer section, last 10 lines)

**Step 1: Update version to v10.2**

Change:

```yaml
**Version**: v10.1 TEXTUAL
```

To:

```yaml
**Version**: v10.2 KNOWLEDGE_GRAPH
**Innovation**: Progressive loading + MANDATORY textual analysis + MnemoLite integration
**Memory**: -94% (22KB vs 370KB baseline)
**Precision**: Specific terms replace "hermeneutic" catch-all
**Output**: 4-part structure with enforced sections + SEARCH_INDEX
**Pure DSL**: No Python/JavaScript code
**Knowledge Graph**: Investigations persist and accumulate in MnemoLite
```

**Step 2: Commit**

```bash
cd /home/giak/projects/truth-engine
git add system.md
git commit -m "feat(system.md): bump to v10.2 KNOWLEDGE_GRAPH"
```

---

## Task 6: Update CLAUDE.md Documentation

**Files:**
- Modify: `/home/giak/projects/truth-engine/CLAUDE.md`

**Step 1: Update version reference**

Change version to v10.2 and add Knowledge Graph section:

```markdown
## Knowledge Graph Integration (v10.2)

**MnemoLite MCP Flow:**
1. PHASE 0.5: `memories://search/{subject}` - Find past investigations
2. PHASE 8: Generate `## SEARCH_INDEX` section
3. PHASE 9: `write_memory` - Save investigation to MnemoLite

**Benefits:**
- Primary sources (◈) accumulate across investigations
- Avoid redundant research on related topics
- EDI improves with reused validated sources
```

**Step 2: Commit**

```bash
cd /home/giak/projects/truth-engine
git add CLAUDE.md
git commit -m "docs(CLAUDE.md): document Knowledge Graph integration v10.2"
```

---

## Task 7: Manual E2E Test

**Files:**
- None (manual test)

**Step 1: Start investigation with Knowledge Lookup**

Run a test investigation:

```bash
claude "Analyse: Accord UE-Mercosur agriculture. Load system.md + kb/. Truth Engine protocol v10.2."
```

**Step 2: Verify PHASE 0.5 executed**

Check output for:
- "memories://search/..." MCP call attempted
- Either "Enriched from: ..." or "No prior investigations found"

**Step 3: Verify SEARCH_INDEX generated**

Check output contains:
```
## SEARCH_INDEX

SUBJECT: ...
THEMES: ...
ENTITIES: ...
PRIMARY_SOURCES: ...
PATTERNS_DSL: ...
TEMPORAL: ...
KEYWORDS_FR: ...
KEYWORDS_EN: ...
```

**Step 4: Verify write_memory called**

Check output for:
- `write_memory` MCP tool invocation
- "Investigation saved to MnemoLite: {uuid}"

**Step 5: Verify persistence**

Search MnemoLite for the saved investigation:
```
memories://search/Mercosur?memory_type=investigation
```

Should return the investigation just saved.

---

## Summary

| Task | Description | Commit |
|------|-------------|--------|
| 1 | Add PHASE 0.5 KNOWLEDGE_LOOKUP | `feat(system.md): add PHASE 0.5` |
| 2 | Add PHASE 8 SEARCH_INDEX | `feat(system.md): add PHASE 8` |
| 3 | Add PHASE 9 KNOWLEDGE_SAVE | `feat(system.md): add PHASE 9` |
| 4 | Update ENFORCEMENT RULES | `feat(system.md): update ENFORCEMENT RULES` |
| 5 | Update version to v10.2 | `feat(system.md): bump to v10.2` |
| 6 | Update CLAUDE.md | `docs(CLAUDE.md): document v10.2` |
| 7 | Manual E2E test | (no commit) |

**Total estimated time:** 20-30 minutes
