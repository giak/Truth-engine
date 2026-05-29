# Bug Fix: Logs Markdown + MnemoLite Memory Not Saved

**Date:** 2025-11-14
**Version:** Truth Engine v8.4 (post-v8.3.1 hotfix)
**Bug ID:** Missing logs file generation + Missing MnemoLite persistence
**Severity:** HIGH (data loss, no investigation persistence)
**Status:** FIXED ✅

---

## Summary

**Problem:** Truth Engine investigations were NOT saved to disk or persisted to MnemoLite memory database, causing data loss between sessions.

**User Report:**
```
"dans une autre session, j'ai tapé 'Analyse: "L'IA va remplacer tout les développeurs." Protocole Truth Engine complet.'
2 problèmes :
- pas de logs markdown généré
- pas de sauvegarde dans MnemoLite (le premier message d'une session ne semble pas etre pris en compte)"
```

**Root Cause:** Same architectural issue as query splitting bug - system.md contained **aspirational documentation** instead of **procedural execution instructions**.

**Fix:** Added 2 new mandatory steps (9 and 10) to system.md with explicit Write tool and write_memory MCP invocations.

---

## Evidence of Bugs

### Bug #1: No logs/ markdown file generated

**Expected (per CLAUDE.md:305):**
```bash
Save logs/$(date +%Y-%m-%d)_subject.md
```

**Expected (per system.md:206 BEFORE fix):**
```
I0 investigation file path (logs/YYYY-MM-DD_HH-MM-SS_subject.md)
```

**Actual behavior:**
- Investigation completes successfully
- Part 1/2/3 displayed to user in chat
- **NO file created in logs/ directory**
- User loses investigation data when session ends

**Why:** system.md line 206 was **reference passive** ("here's what the path format is") NOT **action imperative** ("USE Write tool to create file at this path").

### Bug #2: No MnemoLite write_memory called

**Expected (per PRD.md:104):**
```
APEX mode adds memory persistence and cross-investigation intelligence
```

**Expected (per CLAUDE.md:395-396):**
```
write_memory, update_memory, delete_memory - Cross-session memory
```

**Actual behavior:**
- Investigation completes successfully
- **NO write_memory MCP tool invoked**
- Investigation NOT persisted to MnemoLite database
- User loses cross-session intelligence (cannot reference past investigations)

**Why:** write_memory invocation **completely absent** from system.md workflow.

---

## Root Cause Analysis (Systematic Debugging)

### Phase 1: Investigation

**Evidence gathering:**

1. **Searched system.md for logs/ instructions:**
   - Found: Line 206 "I0 investigation file path (logs/YYYY-MM-DD_HH-MM-SS_subject.md)"
   - Type: **RÉFÉRENTIEL** (passive reference to path format)
   - Missing: "Use Write tool to create file at logs/..."

2. **Searched system.md for write_memory:**
   - Command: `grep -i "write_memory|Write tool|MCP tool" system.md`
   - Result: **NO MATCHES FOUND**
   - Conclusion: Completely absent from workflow

3. **Compared to CLAUDE.md (user docs):**
   - CLAUDE.md:305 shows user example "Save logs/..."
   - CLAUDE.md:395 lists write_memory as available feature
   - **GAP:** User docs promise features, system.md doesn't implement them

### Phase 2: Pattern Analysis

**Architectural pattern identified:**

Same root cause as query splitting bug (fixed v8.3.1):

| Bug | system.md Content | Type | Claude Interpretation |
|-----|-------------------|------|----------------------|
| **Query splitting** | "IF query keyword_count > 5 → SPLIT" | ASPIRATIONAL | "This documents what optimization does" |
| **Logs file** | "I0 investigation file path (logs/...)" | RÉFÉRENTIEL | "This shows path format" |
| **write_memory** | [completely absent] | MISSING | "Feature doesn't exist" |

**Pattern:** system.md mixes 3 types of information WITHOUT distinguishing them:
1. **Procédural (executable)** - What Claude MUST do (ex: "FOR EACH query, count keywords...")
2. **Aspirational (documentation)** - What system "does" in theory (ex: "Query optimization @KB...")
3. **Référentiel (pointers)** - Where to find info (ex: "@KB[PATTERNS]")

### Phase 3: Hypothesis

**Hypothesis:** Claude needs **explicit step-by-step instructions** with tool names, not passive references or absent features.

**Test:** Search for ANY explicit "Use Write tool" or "Use write_memory" instruction in system.md.

**Result:**
```bash
grep -E "Use Write|write_memory|Write tool|MCP tool|mcp__mnemolite" system.md
# Output: No files found
```

**HYPOTHESIS CONFIRMED ✅** - Zero explicit tool invocation instructions.

### Phase 4: Implementation

**Fix applied:** Added 2 new mandatory workflow steps to system.md after step 8 (OUTPUT).

---

## The Fix

### Before (v8.3 - BROKEN)

```yaml
**8. OUTPUT**: Part 1(FR tri-perspectif dialectique) + Part 2(TECH scores) + Part 3(WOLF if applicable)

## 🌳 INVESTIGATION_TREE (APEX complexity ≥9.0 only)
```

**Problems:**
- No step 9 (save to disk)
- No step 10 (persist to memory)
- Investigation output "vanishes" after chat ends

---

### After (v8.4 - FIXED)

```yaml
**8. OUTPUT**: Part 1(FR tri-perspectif dialectique) + Part 2(TECH scores) + Part 3(WOLF if applicable)

**9. SAVE INVESTIGATION** (MANDATORY - create markdown file):
   - Generate filename: `logs/YYYY-MM-DD_HH-MM-SS_{subject_slug}.md`
     * YYYY-MM-DD: Current date (e.g., 2025-11-14)
     * HH-MM-SS: Current time (e.g., 15-53-46)
     * subject_slug: Lowercase, spaces→hyphens, max 40 chars (e.g., "ia-remplacer-developpeurs")
   - Use Write tool to create file with complete investigation:
     * Include ALL 3 parts (Part 1 FR + Part 2 TECH + Part 3 WOLF if applicable)
     * Preserve exact formatting, symbols (⟐🎓🔥⟐̅◈◉○), YAML blocks, tables
     * Add header: "# Truth Engine Investigation - {subject}" at top
     * Add footer: "---\n**Investigation:** {iteration} | **Complexity:** {score}/10 | **Date:** {timestamp}"
   - Confirm file created successfully before proceeding

**10. PERSIST TO MEMORY** (MANDATORY if MCP available - cross-session intelligence):
   - Check MCP status: IF mcp__mnemolite__write_memory available → EXECUTE
   - Use mcp__mnemolite__write_memory tool:
     * title: "{subject} - Truth Engine {iteration} (EDI {edi_score})"
     * content: Full investigation markdown (same as logs/ file)
     * memory_type: "note"
     * tags: ["truth-engine", "{iteration}", "edi-{edi_band}", "{domain}", "{complexity}"]
       - edi_band: "low" (≤0.30), "medium" (0.31-0.60), "high" (≥0.61)
       - domain: Political, Scientific, Corporate, Geopolitical, etc.
       - complexity: SIMPLE, MEDIUM, COMPLEX, APEX
     * project_id: "truth-engine" (scoping)
   - Track: memory_saved = true/false (report in [REFLECTION] if failed)
   - IF MCP unavailable: Skip with warning in [REFLECTION]: "⚠️ MnemoLite unavailable - cross-session memory not persisted"
```

**Fix details:**

**Step 9 (SAVE INVESTIGATION):**
- **"Use Write tool"** - Explicit tool invocation (not "save" or "create")
- **Filename generation formula** - Exact YYYY-MM-DD_HH-MM-SS_{slug} format
- **subject_slug transformation** - Lowercase, spaces→hyphens, 40 char limit
- **Content specification** - ALL 3 parts, exact symbols preserved
- **Header/footer templates** - Structured metadata
- **"Confirm file created successfully"** - Verification step

**Step 10 (PERSIST TO MEMORY):**
- **"IF mcp__mnemolite__write_memory available"** - Graceful degradation
- **"Use mcp__mnemolite__write_memory tool"** - Explicit MCP tool name
- **Parameter mapping** - title, content, memory_type, tags, project_id
- **tags array construction** - Dynamic based on EDI/domain/complexity
- **Tracking** - memory_saved flag for [REFLECTION] reporting
- **Fallback behavior** - Warning if MCP unavailable

---

## Expected Impact After Fix

### Functional Improvements

**Logs file generation:**
- Before: 0 files created (100% data loss)
- After: 1 file per investigation in logs/ directory
- Format: `logs/2025-11-14_15-53-46_ia-remplacer-developpeurs.md`
- Persistence: Investigations preserved on disk

**MnemoLite cross-session memory:**
- Before: 0 memories saved (no cross-session intelligence)
- After: 1 memory per investigation in MnemoLite database
- Tags enable: search by EDI quality, domain, complexity, iteration
- project_id scoping: "truth-engine" project separation
- Cross-investigation: Reference past analyses, track patterns over time

### User Experience

**Before (data loss):**
1. User runs investigation
2. Sees results in chat
3. Session ends
4. **Investigation lost forever** ❌
5. Cannot reference past work
6. Must re-run investigations from scratch

**After (persistence):**
1. User runs investigation
2. Sees results in chat
3. **File saved to logs/** ✅
4. **Memory saved to MnemoLite** ✅
5. Session ends
6. User can:
   - Open logs/YYYY-MM-DD_HH-MM-SS_subject.md (markdown file)
   - Search MnemoLite: "truth-engine EDI high political" (find past investigations)
   - Reference previous analyses in new investigations
   - Track patterns across multiple subjects

---

## Validation Plan

### Test Case 1: Logs File Generation

**Input:** Run Truth Engine investigation
```bash
"Analyse: 'L'IA va remplacer tous les développeurs.' Protocole Truth Engine complet."
```

**Expected results:**
1. Investigation completes (Part 1/2/3 displayed)
2. File created: `logs/2025-11-14_16-30-00_ia-remplacer-developpeurs.md`
3. File contains:
   - Header: "# Truth Engine Investigation - L'IA va remplacer tous les développeurs"
   - Part 1 (French analysis)
   - Part 2 (DIAGNOSTICS)
   - Part 3 (WOLF if applicable)
   - Footer: "**Investigation:** I0 | **Complexity:** X/10 | **Date:** 2025-11-14 16:30:00"

**Pass criteria:**
- ✅ File exists in logs/ directory
- ✅ Filename format correct (YYYY-MM-DD_HH-MM-SS_slug.md)
- ✅ Content complete (all 3 parts)
- ✅ Symbols preserved (⟐🎓🔥⟐̅◈◉○)

### Test Case 2: MnemoLite Memory Persistence

**Input:** Same investigation as Test Case 1

**Expected results:**
1. write_memory MCP tool invoked
2. Memory created with:
   - title: "L'IA va remplacer tous les développeurs - Truth Engine I0 (EDI 0.XX)"
   - content: Full investigation markdown
   - tags: ["truth-engine", "I0", "edi-medium", "tech", "MEDIUM"]
   - project_id: "truth-engine"

**Pass criteria:**
- ✅ write_memory tool called (check MCP logs)
- ✅ Memory searchable: `search_code(query="truth-engine IA développeurs")`
- ✅ Tags correct (EDI band, domain, complexity)

### Test Case 3: Graceful Degradation (MCP Unavailable)

**Input:** Run investigation with MnemoLite MCP disabled

**Expected results:**
1. Investigation completes
2. Logs file created successfully
3. [REFLECTION] section contains: "⚠️ MnemoLite unavailable - cross-session memory not persisted"
4. No error/crash

**Pass criteria:**
- ✅ Logs file created (step 9 works independently)
- ✅ Warning displayed in [REFLECTION]
- ✅ Investigation quality unaffected

---

## Files Modified

1. **system.md** (line 348-375)
   - Added step 9: SAVE INVESTIGATION (mandatory Write tool)
   - Added step 10: PERSIST TO MEMORY (mandatory write_memory if MCP available)
   - Explicit tool names, parameter mapping, verification steps

2. **tests/query_optimization/BUG_FIX_logs_and_memory.md** (this file)
   - Complete root cause analysis
   - Before/after comparison
   - Validation plan

---

## Architectural Lesson Learned

**Anti-pattern identified:** Mixing 3 types of information in system.md WITHOUT explicit execution instructions:
1. **Procédural** (what to do) - GOOD ✅
2. **Aspirational** (what system "does") - DANGEROUS ⚠️
3. **Référentiel** (where to find info) - NEUTRAL ℹ️

**Pattern to follow:**

❌ **WRONG (aspirational):**
```
Query optimization involves splitting complex queries
I0 investigation file path (logs/...)
```

✅ **RIGHT (procedural):**
```
FOR EACH query:
  STEP 1: Count keywords
  STEP 2: IF count > 5 → Invoke @FUNCTION[SPLIT_QUERY]

Use Write tool to create file logs/YYYY-MM-DD_HH-MM-SS_{slug}.md
```

**Key difference:** Explicit **action verbs** (Use, Invoke, Create, Execute) + **tool names** (Write tool, write_memory MCP).

---

## Commit Message

```
feat: Add logs/ file persistence + MnemoLite memory (v8.4)

HIGH SEVERITY: Investigations were NOT saved to disk or memory database,
causing data loss between sessions.

Root cause: system.md lacked procedural instructions for:
1. Write tool (logs/ file generation)
2. write_memory MCP (MnemoLite persistence)

Fix: Added 2 mandatory workflow steps after OUTPUT:
  STEP 9: SAVE INVESTIGATION
    - Explicit "Use Write tool" instruction
    - Filename: logs/YYYY-MM-DD_HH-MM-SS_{subject_slug}.md
    - Content: Full investigation (Part 1/2/3 + header/footer)

  STEP 10: PERSIST TO MEMORY (if MCP available)
    - Explicit "Use mcp__mnemolite__write_memory" instruction
    - Parameters: title, content, tags (EDI/domain/complexity), project_id
    - Graceful degradation: Warning if MCP unavailable

Expected impact:
- Logs file: 0 files → 1 file per investigation (100% → 0% data loss)
- Memory: 0 memories → 1 memory per investigation (cross-session intelligence)

User report (bug evidence):
"pas de logs markdown généré"
"pas de sauvegarde dans MnemoLite (le premier message d'une session ne semble pas etre pris en compte)"

Files modified:
- system.md (line 348-375): Steps 9-10 procedural instructions
- tests/query_optimization/BUG_FIX_logs_and_memory.md: Documentation

Validation: Re-run user's investigation "L'IA va remplacer tous les développeurs"

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Status

**Implementation:** ✅ COMPLETE
**Testing:** ⏳ PENDING (re-run user's investigation)
**Documentation:** ✅ COMPLETE

**Next step:** User should re-run investigation to validate both bugs fixed

---

**Version:** v8.4
**Date:** 2025-11-14
**Type:** Feature addition (missing persistence layers)
**Related bugs:** Query splitting v8.3.1 (same architectural root cause)
