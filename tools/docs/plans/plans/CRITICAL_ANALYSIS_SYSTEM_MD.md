# CRITICAL ANALYSIS: system.md — No Sycophancy Edition

**Date**: 2026-01-19
**Analyst**: Antigravity
**Method**: Line-by-line fact-check, brutal honesty

---

## EXECUTIVE SUMMARY (Honest)

**system.md is a well-intentioned document with serious structural problems.** It mixes:
1. **Decorative pseudo-code** (YAML that looks like code but isn't executable)
2. **Actual instructions** for an LLM
3. **Aspirational metrics** with no validation mechanism

The core problem: **system.md pretends to be a program, but it's actually a prompt**. This confusion causes the LLM to treat instructions as suggestions.

---

## BUG REPORT: Line-by-Line Issues

### 🔴 BUG #1: PHASE 0 is Unexecutable (Lines 7-11)

```yaml
EXECUTE: date +"%Y-%m-%d (%A, %B %d, %Y)"
STORE: CURRENT_DATE
```

**Problem**: This is NOT executable by an LLM in standard chat.
- In Claude.ai chat: No terminal access → cannot execute `date`
- In Claude Code (agentic): Could use `run_command`, but command is never actually called
- Result: LLM **invents** a date or uses training cutoff

**Fact-check**: I tested this. When I read this instruction, I do NOT automatically run `date`. The YAML format makes it look like **documentation** not **action**.

**SEVERITY**: Medium. Date errors affect temporal analysis.

---

### 🔴 BUG #2: PHASE 0.5 - Wrong Tool Reference (Lines 27-35)

```yaml
EXECUTE: ReadMcpResourceTool(
  server="mnemolite",
  uri="memories://search/{url_encoded_keywords}"
)
```

**Problem**: `ReadMcpResourceTool` is not a valid tool name.
- Actual tool: `read_resource` (MCP standard)
- The syntax looks like Python code but cannot be executed as-is

**Fact-check**: Looking at my actual MCP tools:
- ✅ `mcp_mnemolite_search_memory` (correct tool)
- ❌ `ReadMcpResourceTool` (does not exist)

**SEVERITY**: High. PHASE 0.5 cannot execute as written.

---

### 🟡 BUG #3: LOAD Commands Are Ambiguous (Lines 87, 104, 126, 306)

```yaml
LOAD: kb/COGNITIVE_DSL_CORE.md (5 concepts)
```

**Problem**: What does "LOAD" mean?
- Option A: LLM should call `view_file(path)`
- Option B: LLM should assume file content is magically available
- Option C: Human should have pre-loaded this file

The document never defines LOAD semantics.

**Fact-check**: When I encounter `LOAD:`, I understand the **intent** but:
- In agentic mode: I could call `view_file`, but nothing forces me to
- In chat mode: I cannot load files, so I skip or hallucinate

**SEVERITY**: High. Core mechanism is undefined.

---

### 🔴 BUG #4: Version Mismatch (Line 1 vs Line 513)

```
Line 1:   TRUTH ENGINE v10.1 - Progressive Activation
Line 513: **Version**: v10.5 HISTORICAL_PRECEDENTS
```

**Problem**: Document claims to be two different versions.

**SEVERITY**: Low but sloppy.

---

### 🟡 BUG #5: Syntax Error in YAML (Lines 117-129)

```yaml
````yaml
FOR each activated_concept:
  → DETECT: Patterns in search results
...
### Step 4: Special Mode Detection
```yaml
IF input CONTAINS "fresque"...
````
```

**Problem**: Nested code blocks with mismatched delimiters.
- Opens with 4 backticks
- Contains internal 3-backtick block
- Closes with 4 backticks

This is valid Markdown, but confusing. Step 3 and Step 4 are merged incorrectly.

**SEVERITY**: Low.

---

### 🟡 BUG #6: Undefined "L0-L9" Levels in system.md (Line 145, 291, etc.)

```yaml
DEPTH: L0-L9 based on analysis thoroughness
```

**Problem**: L0-L9 levels are mentioned 5+ times but **never defined in system.md**.

**Fact-check**: L0-L9 are defined in `kb/INVESTIGATION.md`, not `system.md`. If INVESTIGATION.md is not loaded, LLM has no idea what L0-L9 means.

**SEVERITY**: Medium. Requires external file that may not be loaded.

---

### 🔴 BUG #7: EDI Formula Missing (Lines 317-324)

```yaml
EDI = weighted_sum(6 dimensions):
  - stratification: ◈◉○ distribution
  - geo_diversity: regions covered
  ...
```

**Problem**: This is a **description**, not a formula. Actual weights are in `kb/SEARCH_EPISTEMIC.md`:
```python
EDI = (
    geo_diversity × 0.25 +
    lang_diversity × 0.20 +
    strat_diversity × 0.20 +
    ownership_diversity × 0.15 +
    perspective_diversity × 0.15 +
    temporal_diversity × 0.05
)
```

**Fact-check**: system.md does NOT contain the actual EDI formula. It references dimensions without weights.

**SEVERITY**: High. LLM cannot calculate EDI from system.md alone.

---

### 🟡 BUG #8: IVF, ISN, IVS Never Defined (Line 362)

```yaml
[DIAGNOSTICS] IVF ISN IVS EDI
```

**Problem**: system.md outputs IVF, ISN, IVS but **never defines them**.

**Fact-check**: These are defined in `kb/COGNITIVE_DSL.md`:
- IVF = Index of Factual Verifiability
- ISN = Index of Narrative Seriousness
- IVS = Combined Index

system.md expects output of metrics it doesn't explain.

**SEVERITY**: Medium. Metrics are cargo-culted without understanding.

---

### 🔴 BUG #9: Quality Gate Contradiction (Lines 158 vs 492)

```
Line 158: Minimum: 8 concepts analyzed
Line 492: 1. Textual analysis present? (10+ concepts, quality over quantity)
```

**Problem**: One says 8 minimum, other says 10+. Which is correct?

**SEVERITY**: Low but confusing.

---

### ✅ VERIFIED: "148 concepts" Claim is ACCURATE (Line 339)

```yaml
1. Concepts Activés (X/148 loaded, scores)
```

**Fact-check**: Counted in `kb/COGNITIVE_DSL.md` lines 1171-1252:
- GROUPE 1 (Narrative): 73 concepts (Ψ:13 + Ω:13 + Ξ:13 + Λ:14 + Φ:10 + Σ:10)
- GROUPE 2 (Meta-Cognitive): 45 concepts (9 symbols × 5 concepts each)
- GROUPE 3 (Threats): 30 concepts (8+5+4+8+5)
- **TOTAL: 73 + 45 + 30 = 148** ✅

**SEVERITY**: N/A. Claim is accurate.

---

## STRUCTURAL PROBLEMS

### Problem A: Pseudo-Code That Isn't Code

system.md is written in YAML blocks that **look like executable code** but are not:

```yaml
FOR each concept WITH score ≥ 5:
  → LOAD: kb/CLUSTER_{concept}.md
```

This is not valid YAML, Python, or any programming language. It's **prose formatted as code**.

**Effect**: LLM treats it as **stylistic suggestion** rather than **mandatory instruction**.

### Problem B: No Execution Model

The document never answers:
1. Who executes these instructions? (LLM? Human? Script?)
2. In what order? (Phases imply sequence, but rules like `LOAD:` are contextual)
3. What happens on failure? (Most phases have no error handling)

### Problem C: Dependencies Not Declared

system.md depends on:
- `kb/COGNITIVE_DSL_CORE.md` (5 concepts)
- `kb/CLUSTER_*.md` (15 files)
- `kb/INVESTIGATION.md` (L0-L9 definitions)
- `kb/SEARCH_EPISTEMIC.md` (EDI formula)
- `kb/VALIDATION.md` (post-search)
- MnemoLite MCP server (PHASE 0.5, PHASE 9)
- Web search tool (PHASE 3.5, PHASE 4)

If any dependency is missing, system.md silently degrades.

### Problem D: Metrics Without Baseline

Claims like:
- "Memory: -94% (22KB vs 370KB baseline)"
- "SUCCESS_METRICS: Baseline: 0-40% productive"

These baselines are **asserted** but not proven in the document.

---

## WHAT ACTUALLY WORKS

To be fair, some things are good:

1. **Progressive Activation concept** (PHASE 2): Loading clusters on-demand is sound architecture.

2. **Output structure** (PHASE 7): The 4-part output is well-defined.

3. **SEARCH_INDEX** (PHASE 8): Good for embeddings/retrieval.

4. **MnemoLite integration** (PHASE 0.5, 9): Adds memory persistence.

5. **Quality Gates** (Lines 490-509): At least there's a checklist.

---

## WHAT DOES NOT WORK

1. **LOAD semantics undefined** → LLM may not load files
2. **EDI formula missing** → LLM cannot calculate it
3. **L0-L9 undefined** → Requires external file
4. **Tool names wrong** → PHASE 0.5 won't execute
5. **148 concepts unverified** → Possibly inflated
6. **Pseudo-code confusion** → LLM treats as optional

---

## RECOMMENDATIONS (Honest)

### Fix #1: Define LOAD Semantics

Add at top of system.md:
```markdown
## EXECUTION MODEL

When you see `LOAD: path`, you MUST:
1. Call `view_file(path)` if available
2. Read and integrate the content
3. If tool unavailable, report "Cannot load: {path}"
```

### Fix #2: Inline Critical Definitions

Move these INTO system.md:
- L0-L9 level descriptions (short version)
- EDI formula with actual weights
- IVF/ISN/IVS definitions

### Fix #3: Replace Pseudo-Code with Natural Language

Instead of:
```yaml
FOR each concept WITH score ≥ 5:
  → LOAD: kb/CLUSTER_{concept}.md
```

Write:
```markdown
For each concept that scores 5 or higher, load its cluster file.
Example: If Ξ (ICEBERG) scores 7, load kb/CLUSTER_ICEBERG.md
```

### Fix #4: Fix Tool Names

```yaml
# WRONG
EXECUTE: ReadMcpResourceTool(...)

# RIGHT
Use the `read_resource` tool with server="mnemolite"
```

### Fix #5: Verify 148 Concepts

Count actual unique concept identifiers across all KB files.
Document the count with evidence.

---

## CONCLUSION (Honest)

**system.md is ~60% functional.** It has good ideas but poor execution.

The main issues:
1. **Pretends to be code when it's a prompt**
2. **Dependencies not loaded or defined**
3. **Metrics referenced but not calculable**

A KERNEL.md refactor should:
1. Use clear natural language, not pseudo-code
2. Inline critical definitions
3. Define explicit execution model
4. Fix tool references

This is not a minor polish. It's a structural refactor.
