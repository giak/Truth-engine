# Implementation Plan: Google Search MCP Integration [ABANDONED]

**Date:** 2025-11-16
**Status:** ❌ ABANDONED after load testing (0% success rate on 25 queries)
**Complexity:** MEDIUM
**Estimated time:** 60-90 minutes (NOT executed)
**Reason:** Google anti-bot detection blocks 100% of Playwright-based searches
**Post-mortem:** [docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md](../postmortems/2025-11-16-google-search-mcp-ABANDONED.md)

---

## ⚠️ PLAN ABANDONNÉ - NE PAS EXÉCUTER

Ce plan a été abandonné après tests de charge démontrant une viabilité nulle :
- 25 requêtes testées (burst, modéré 5s, conservateur 30s)
- 0 succès, 25 échecs (0% taux de succès)
- Cause : Google overlay anti-bot bloque tous clics Playwright
- Architecture actuelle Truth Engine (WebSearch + MCP web-search) supérieure

Voir post-mortem pour analyse complète.

---

## Goal

Integrate Google Search MCP server alongside existing DuckDuckGo (web-search) to maximize EDI (Epistemic Diversity Index) for Truth Engine investigations through parallel search execution and result fusion.

## Architecture

```
Truth Engine Investigation
    ↓
[Complexity Assessment] → Query Allocation
    ↓
┌─────────────────────────────────────┐
│  PARALLEL SEARCH ORCHESTRATION      │
├─────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐ │
│  │ DuckDuckGo   │  │ Google       │ │
│  │ (web-search) │  │ (google-srch)│ │
│  │ MCP          │  │ MCP          │ │
│  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────┘
    ↓
[Result Fusion + Deduplication]
    ↓
[EDI Calculation] (2 sources → +0.15-0.25 boost)
    ↓
[Validation Loop] → Investigation Output
```

**Key Design Decisions:**
- **Parallel systematic execution**: Both engines ALWAYS queried (maximize diversity)
- **Graceful degradation**: If Google fails, DuckDuckGo results still valid
- **Result fusion**: URL-based deduplication, preserve source attribution
- **EDI boost**: source_diversity dimension benefits from dual search engines

## Tech Stack

- **Package:** `google-search-mcp` (npm package, no API key required)
- **Technology:** Playwright + Chromium headless browser
- **Installation:** npx (no global install needed)
- **Integration:** `.mcp.json` configuration + Claude Code permissions
- **Orchestration:** Parallel async calls in investigation protocol
- **Fallback:** DuckDuckGo if Google unavailable (graceful degradation)

## Prerequisites

- Truth Engine v8.0+ with MCP support
- Node.js/npm installed (for npx execution)
- Claude Code with MCP permissions system
- Existing web-search MCP server (DuckDuckGo) functional

## Implementation Tasks

### Task 1: Install and Test google-search-mcp Package (5 min)

**Objective:** Verify google-search-mcp works standalone via npx

**Commands:**
```bash
# Test npx installation (will download on first run)
npx google-search-mcp --version

# Verify Playwright dependencies (installs Chromium if needed)
npx playwright install chromium

# Test basic search (should return JSON results)
echo '{"query": "test search anthropic claude"}' | npx google-search-mcp
```

**Expected output:**
- Version output (e.g., `google-search-mcp v1.0.0` or similar)
- Playwright installation success
- JSON array with search results (title, url, snippet fields)

**Validation:**
```bash
# Verify results structure
echo '{"query": "github anthropic"}' | npx google-search-mcp | jq '.[0] | keys'
# Expected: ["title", "url", "snippet"] or similar
```

**Troubleshooting:**
- If Playwright fails: `npx playwright install --with-deps chromium`
- If rate limited: Wait 60s between tests (anti-scraping detection)

---

### Task 2: Configure .mcp.json for google-search Server (3 min)

**Objective:** Add google-search MCP server to Truth Engine configuration

**File:** `/home/giak/projects/truth-engine/.mcp.json`

**Current state:**
```json
{
  "mcpServers": {
    "mnemolite": {
      "command": "bash",
      "args": ["/home/giak/Work/MnemoLite/scripts/mcp_server.sh"],
      "env": {
        "DOCKER_COMPOSE_PROJECT": "mnemolite"
      }
    }
  }
}
```

**Add google-search server:**
```json
{
  "mcpServers": {
    "mnemolite": {
      "command": "bash",
      "args": ["/home/giak/Work/MnemoLite/scripts/mcp_server.sh"],
      "env": {
        "DOCKER_COMPOSE_PROJECT": "mnemolite"
      }
    },
    "google-search": {
      "command": "npx",
      "args": ["google-search-mcp"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

**Implementation:**
```bash
# Backup existing config
cp /home/giak/projects/truth-engine/.mcp.json /home/giak/projects/truth-engine/.mcp.json.backup

# Edit with new server configuration
# (Manual edit or use jq to merge)
```

**Validation:**
```bash
# Verify JSON syntax
jq empty /home/giak/projects/truth-engine/.mcp.json
echo $?  # Should be 0 (success)

# Verify servers count
jq '.mcpServers | keys | length' /home/giak/projects/truth-engine/.mcp.json
# Expected: 2
```

**Restart required:** Claude Code session must restart to load new MCP server

---

### Task 3: Add Auto-Approval Permissions for google-search MCP (2 min)

**Objective:** Enable auto-approval for Google Search MCP tools to avoid permission prompts

**File:** `/home/giak/projects/truth-engine/.claude/settings.local.json`

**Current state:** Has web-search, context7, mnemolite permissions (lines 37-48)

**Add google-search permissions:**
```json
{
  "permissions": {
    "allow": [
      // ... existing permissions ...
      "mcp__web-search__search",
      "mcp__context7__resolve-library-id",
      "mcp__context7__get-library-docs",
      "mcp__mnemolite__ping",
      "mcp__mnemolite__search_code",
      "mcp__mnemolite__write_memory",
      "mcp__mnemolite__update_memory",
      "mcp__mnemolite__delete_memory",
      "mcp__mnemolite__index_project",
      "mcp__mnemolite__reindex_file",
      "mcp__mnemolite__clear_cache",
      "mcp__mnemolite__switch_project",
      "mcp__google-search__search"
    ]
  }
}
```

**Note:** Exact tool name may vary. After Task 4, verify actual tool name via:
```bash
# List available MCP tools (in Claude Code session)
# Tool name format: mcp__<server-name>__<tool-name>
```

**Validation:**
- Settings file must validate (Claude Code will show error if syntax wrong)
- No wildcards or parentheses (not supported)

---

### Task 4: Test Google Search MCP Integration in Claude Code (5 min)

**Objective:** Verify Google Search MCP server loads and responds correctly

**Prerequisites:**
- Task 2 completed (.mcp.json configured)
- Claude Code session restarted

**Test steps:**

1. **Verify MCP server loaded:**
```
# In Claude Code session, check available MCP tools
# Should see google-search server listed
```

2. **Test simple search:**
```
# Use google-search MCP tool with basic query
Query: "anthropic claude AI"
Expected: Array of search results (title, url, snippet)
```

3. **Compare with DuckDuckGo:**
```
# Run identical query on web-search (DuckDuckGo)
Query: "anthropic claude AI"
Expected: Different result ordering/sources vs Google
```

**Validation criteria:**
- ✅ Google Search MCP returns ≥5 results
- ✅ Results have title, url, snippet fields
- ✅ URLs are valid and diverse (not all same domain)
- ✅ No errors/timeouts (or graceful error handling if rate limited)

**Troubleshooting:**
- If "MCP server not found": Verify .mcp.json syntax, restart Claude Code
- If Playwright errors: Run `npx playwright install chromium` manually
- If rate limited: Expected on first use, wait 60s and retry

---

### Task 5: Implement Parallel Search Orchestration (15 min)

**Objective:** Modify Truth Engine investigation protocol to query both DuckDuckGo and Google in parallel

**File to modify:** `/home/giak/projects/truth-engine/system.md` (investigation execution section)

**Current behavior (assumed):**
- Sequential web-search (DuckDuckGo) calls
- One search engine per query

**New behavior:**
- Parallel calls to both `mcp__web-search__search` AND `mcp__google-search__search`
- Concurrent execution with Promise.all or equivalent
- Graceful degradation if one fails

**Pseudocode:**
```python
# FOR EACH allocated query in investigation:
async def execute_search_query(query: str, allocated_sources: int):
    # Launch both searches in parallel
    results_ddg = await mcp__web_search__search(query, limit=allocated_sources)
    results_google = await mcp__google_search__search(query, limit=allocated_sources)

    # Await both (parallel execution)
    ddg, google = await asyncio.gather(results_ddg, results_google, return_exceptions=True)

    # Graceful error handling
    if isinstance(ddg, Exception):
        ddg = []  # Fallback to empty
    if isinstance(google, Exception):
        google = []  # Fallback to empty

    # Fuse results (Task 6)
    fused = fuse_search_results(ddg, google)

    return fused
```

**Implementation locations:**

1. **If system.md contains executable search logic:**
   - Locate search execution section
   - Replace single web-search call with parallel dual-engine pattern
   - Add error handling for each engine

2. **If search is orchestrated externally (likely):**
   - This task may be **protocol documentation only**
   - Update system.md to instruct Claude Code to:
     - "ALWAYS query BOTH web-search (DuckDuckGo) AND google-search (Google) in parallel"
     - "Use Promise.all or concurrent execution pattern"
     - "Fuse results via URL deduplication (Task 6)"
     - "If one engine fails, use other engine results (graceful degradation)"

**Expected system.md change (example):**

```markdown
## Web Search Execution (Query Optimization v8.4)

### Dual-Engine Parallel Search (NEW in v8.4)

For EVERY allocated web search query:

1. **Execute in parallel:**
   - DuckDuckGo via `mcp__web-search__search(query, limit)`
   - Google via `mcp__google-search__search(query, limit)`

2. **Graceful degradation:**
   - If Google fails/timeout → Use DuckDuckGo results only
   - If DuckDuckGo fails → Use Google results only
   - If BOTH fail → Mark query as failed, retry if budget permits

3. **Result fusion:** (See §8.4.2)
   - Deduplicate by URL (keep first occurrence)
   - Preserve source attribution (ddg vs google)
   - Merge into unified result set

4. **EDI calculation:**
   - source_diversity += 0.15 bonus for dual-engine coverage
   - Count unique domains across BOTH result sets
```

**Validation:**
- Check system.md diff shows parallel execution instruction
- No breaking changes to existing investigation protocol
- Backward compatible (if google-search unavailable, DuckDuckGo still works)

---

### Task 6: Add Result Fusion and Deduplication (10 min)

**Objective:** Implement logic to merge DuckDuckGo + Google results, removing duplicates while preserving source attribution

**Location:** Same as Task 5 (system.md protocol or external orchestration)

**Algorithm:**

```python
def fuse_search_results(ddg_results: List[Dict], google_results: List[Dict]) -> List[Dict]:
    """
    Fuse DuckDuckGo and Google search results with URL-based deduplication.

    Priority: DuckDuckGo results first (preserve existing behavior), then Google.
    """
    fused = []
    seen_urls = set()

    # Add DuckDuckGo results first (priority)
    for result in ddg_results:
        url = normalize_url(result.get('url', ''))
        if url and url not in seen_urls:
            result['source_engine'] = 'duckduckgo'  # Attribution
            fused.append(result)
            seen_urls.add(url)

    # Add Google results (only if URL not already seen)
    for result in google_results:
        url = normalize_url(result.get('url', ''))
        if url and url not in seen_urls:
            result['source_engine'] = 'google'  # Attribution
            fused.append(result)
            seen_urls.add(url)

    return fused

def normalize_url(url: str) -> str:
    """
    Normalize URL for deduplication (remove trailing slash, http/https unification).
    """
    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(url.lower())
    # Remove trailing slash, unify scheme
    path = parsed.path.rstrip('/')
    normalized = urlunparse((
        'https',  # Force https for comparison
        parsed.netloc,
        path,
        parsed.params,
        parsed.query,
        ''  # Remove fragment
    ))
    return normalized
```

**Implementation:**

If system.md is pure protocol documentation (likely):
- Document the fusion algorithm in system.md
- Instruct Claude Code to implement this logic when executing searches

**system.md addition (example):**

```markdown
### Result Fusion Algorithm (v8.4)

When merging DuckDuckGo and Google results:

1. **Deduplication key:** Normalized URL
   - Lowercase
   - Remove trailing slash
   - Unify http/https to https
   - Remove URL fragment (#...)

2. **Priority order:**
   - DuckDuckGo results added first (preserve existing priority)
   - Google results added ONLY if URL not seen

3. **Source attribution:**
   - Add `source_engine` field: "duckduckgo" | "google"
   - Preserve in final source list for diagnostics

4. **Edge cases:**
   - If result missing `url` field → Skip (invalid result)
   - If both engines return SAME url → Keep DuckDuckGo version
   - If duplicate detection fails → Allow duplicate (avoid data loss)

**Example:**
```
DDG: [A, B, C]
Google: [B, D, E]
Fused: [A(ddg), B(ddg), C(ddg), D(google), E(google)]
```
```

**Validation:**
- Document fusion algorithm clearly
- Example shows expected behavior
- Handles edge cases (missing URLs, duplicates)

---

### Task 7: Update EDI Calculation for Dual-Source Boost (8 min)

**Objective:** Enhance EDI (Epistemic Diversity Index) calculation to reflect dual search engine usage

**Background:**
- EDI formula includes `source_diversity` dimension (see kb/SEARCH_EPISTEMIC.md)
- Dual engines (DuckDuckGo + Google) increase source diversity
- Expected boost: +0.15 to +0.25 on EDI score

**File:** `/home/giak/projects/truth-engine/kb/SEARCH_EPISTEMIC.md` (or system.md if EDI calculated there)

**Current EDI formula (simplified):**
```
EDI = (primary_weight × primary_ratio) +
      (secondary_weight × secondary_ratio) +
      (geo_diversity × geo_weight) +
      (source_diversity × source_weight) +
      (temporal_diversity × temporal_weight) +
      (lang_diversity × lang_weight)
```

**source_diversity component (current):**
- Counts unique domains across all search results
- Normalized 0.0-1.0 (more domains = higher score)

**Enhancement for dual engines:**

```python
def calculate_source_diversity_v8_4(results: List[Dict], engines_used: List[str]) -> float:
    """
    Calculate source diversity with dual-engine bonus.

    Args:
        results: Fused search results with source_engine attribution
        engines_used: List of search engines used (e.g., ['duckduckgo', 'google'])

    Returns:
        source_diversity score (0.0-1.0)
    """
    # Count unique domains
    unique_domains = set()
    for result in results:
        url = result.get('url', '')
        domain = extract_domain(url)
        if domain:
            unique_domains.add(domain)

    # Base diversity (domain count normalized)
    base_diversity = min(len(unique_domains) / 20.0, 1.0)  # Cap at 20 domains

    # Dual-engine bonus
    engine_bonus = 0.0
    if len(engines_used) >= 2:
        # +0.15 bonus for using 2+ engines
        engine_bonus = 0.15

        # Additional +0.05 if BOTH engines contributed results
        engines_contributed = set(r.get('source_engine') for r in results)
        if len(engines_contributed) >= 2:
            engine_bonus += 0.05

    # Final score (capped at 1.0)
    final_score = min(base_diversity + engine_bonus, 1.0)

    return final_score
```

**Implementation:**

Update system.md or kb/SEARCH_EPISTEMIC.md to document this enhancement:

```markdown
### Source Diversity Calculation (v8.4 Enhancement)

**Formula:**
```
source_diversity = min(base_diversity + engine_bonus, 1.0)

WHERE:
  base_diversity = min(unique_domains / 20, 1.0)
  engine_bonus = 0.15 if engines_used >= 2
               + 0.05 if BOTH engines contributed results
```

**Rationale:**
- Dual search engines (DuckDuckGo + Google) increase algorithmic diversity
- Different ranking algorithms → different result sets → higher epistemic coverage
- Bonus ONLY awarded if BOTH engines actually return results (not just queried)

**Example:**
```
10 unique domains, 1 engine (DuckDuckGo only):
  source_diversity = 10/20 = 0.50

10 unique domains, 2 engines (DuckDuckGo + Google, both contributed):
  source_diversity = 0.50 + 0.15 + 0.05 = 0.70 (+0.20 boost)
```

**Impact on EDI:**
- SIMPLE investigations: +0.15 to +0.20 typical boost
- COMPLEX investigations: +0.10 to +0.15 (already high domain diversity)
- APEX investigations: +0.05 to +0.10 (already near EDI cap)
```

**Validation:**
- Check documentation shows formula enhancement
- Example calculation demonstrates expected boost
- Rationale explains why dual engines improve epistemic diversity

---

### Task 8: Integration Testing - SIMPLE Investigation (10 min)

**Objective:** Verify dual-engine search works end-to-end on a SIMPLE investigation

**Prerequisites:**
- Tasks 1-7 completed
- Claude Code session restarted with new MCP config
- system.md updated with dual-engine protocol

**Test investigation:**

```
Subject: "Anthropic Claude Code release date"
Complexity: SIMPLE (factual, non-political)
Expected:
  - Queries: 3-5 web searches
  - Each query hits BOTH DuckDuckGo AND Google
  - Results fused, deduplicated
  - EDI boost: +0.15 to +0.20 from dual engines
  - Target: EDI ≥ 0.45 (SIMPLE minimum 0.30 + dual-engine boost)
```

**Execution:**
```bash
# In Claude Code session:
claude-code "Analyse: 'Anthropic Claude Code release date'.
Load system.md + kb/.
Truth Engine protocol SIMPLE investigation.
Show [QUERY_OPTIMIZATION] metrics in Part 2."
```

**Validation checklist:**

**Part 1 (French analysis):**
- ✅ Sources include mix of DuckDuckGo and Google results
- ✅ Source citations show diversity (not all same domain)
- ✅ Tri-perspective analysis present (Academic ⟐🎓, Dissident 🔥⟐̅, Arbitrage)

**Part 2 (Diagnostics):**
- ✅ `[SOURCES]` section shows:
  - Total sources ≥ 7 (minimum for SIMPLE)
  - Source attribution includes "duckduckgo" and "google"
- ✅ EDI score ≥ 0.45 (SIMPLE minimum 0.30 + dual-engine boost ~0.15)
- ✅ `source_diversity` component shows dual-engine bonus applied
- ✅ `[QUERY_OPTIMIZATION]` section shows:
  - Queries executed: 3-5
  - Split count: 0 (SIMPLE queries not complex enough to split)
  - MCP success rate: XX%
  - Google success rate: XX%
  - Both engines contributed results

**Part 3 (WOLF):**
- ✅ "(WOLF not applicable)" (SIMPLE factual topic)

**Success criteria:**
- Investigation completes without errors
- Both engines contribute results (seen in source attribution)
- EDI boost visible in diagnostics
- No degradation in investigation quality

**If test fails:**
- Check Claude Code logs for MCP errors
- Verify both MCP servers responding (Task 4)
- Review result fusion logic (Task 6)
- Check EDI calculation (Task 7)

---

### Task 9: Integration Testing - COMPLEX Investigation (15 min)

**Objective:** Verify dual-engine search improves EDI on high-complexity political investigation

**Test investigation:**

```
Subject: "ARCOM composition membres nominations gouvernement Macron"
Complexity: COMPLEX (political, French regulatory authority)
Expected:
  - Queries: 10-15 web searches
  - Query optimization: Complex queries auto-split (v8.3)
  - Both DuckDuckGo AND Google queried per query
  - H7 adversary sources if controversy ≥ 6
  - EDI target: ≥ 0.85 (COMPLEX minimum 0.70 + dual-engine boost ~0.15)
  - ISN target: ≥ 9.0 (political topic)
  - Wolves: ≥ 8 individuals mapped
```

**Execution:**
```bash
# In Claude Code session:
claude-code "Analyse: 'ARCOM composition membres nominations gouvernement Macron'.
Load system.md + kb/.
Truth Engine protocol COMPLEX investigation.
Target: EDI≥0.85, ISN≥9.0, wolves≥8.
Save logs/2025-11-16_arcom_test.md"
```

**Validation checklist:**

**Part 1 (French analysis):**
- ✅ Tri-perspective with 95% symmetric hostility:
  - Academic ⟐🎓 (institutional position on ARCOM independence)
  - Dissident 🔥⟐̅ (criticism of government control, media concentration)
  - Arbitrage (evidence-based conclusion, ◈ primary sources)
- ✅ Sources include:
  - ◈ PRIMARY: Conseil d'État decisions, ARCOM official decisions
  - ◉ SECONDARY: Le Monde, Mediapart, etc.
  - Adversary H7 if applicable (RT, Sputnik on French media)
- ✅ Critical points ≥ 4
- ✅ Recommendations present

**Part 2 (Diagnostics):**
- ✅ EDI ≥ 0.85 (shows dual-engine boost working)
- ✅ ISN ≥ 9.0 (network robustness for political topic)
- ✅ IVF appropriate for COMPLEX (sources ≥ 15)
- ✅ Confidence <5% (precision in final claims)
- ✅ `[MODULES]` show political patterns detected (€, ♦, 🌐)
- ✅ `[SOURCES]` breakdown:
  - ◈ PRIMARY ≥ 3
  - ◉ SECONDARY ≥ 5
  - ○ TERTIARY ≥ 7
  - Source engines: Both DuckDuckGo and Google
  - geo_diversity ≥ 0.40 (COMPLEX minimum)
- ✅ `[PATTERNS]` detected (e.g., MONEY, NET, ICEBERG)
- ✅ `[QUERY_OPTIMIZATION]`:
  - Split count ≥ 2 (complex queries auto-split)
  - Productive query rate ≥ 80%
  - Both engines contributing

**Part 3 (WOLF Report):**
- ✅ Individual actors ≥ 8 (political topic threshold)
- ✅ Ratio individuals/institutions ≥ 50%
- ✅ Network analysis (connections between actors)
- ✅ Cui bono analysis (3 levels: visible ×1, shadow ×10, black ×100)

**Success criteria:**
- EDI ≥ 0.85 achieved (demonstrates dual-engine EDI boost)
- ISN ≥ 9.0 achieved (network robustness)
- Query optimization + dual engines = productive rate ≥ 80%
- PRIMARY SOURCES (◈) discovered (e.g., ARCOM decisions, Conseil d'État)
- WOLF report complete with ≥8 individuals mapped

**Comparison baseline (if available):**
- Run SAME investigation with Google Search MCP disabled
- Compare EDI scores (expect +0.15 to +0.20 improvement with dual engines)
- Compare PRIMARY source discovery rate

**If test fails:**
- Review query optimization metrics (should auto-split complex queries)
- Check H7 adversary sources queried (if controversy ≥ 6)
- Verify PRIMARY sources discovered (◈ count ≥ 3)
- Check WOLF threshold logic (political topic should trigger)

---

### Task 10: Performance and Fallback Testing (8 min)

**Objective:** Verify graceful degradation when Google Search fails or rate-limits

**Test scenarios:**

**Scenario 1: Google rate-limited (simulated)**
```
1. Run 5-10 searches rapidly via Google Search MCP
2. Expect: Anti-scraping detection, rate limit errors
3. Verify: Investigation completes using DuckDuckGo results only
4. Check: EDI score reasonable (no dual-engine bonus, but still passes minimum)
```

**Scenario 2: Google MCP server down (simulated)**
```
1. Stop google-search MCP server (comment out in .mcp.json, restart Claude Code)
2. Run SIMPLE investigation
3. Verify: Investigation completes normally with DuckDuckGo only
4. Check: No errors logged, graceful fallback to single-engine mode
```

**Scenario 3: Both engines fail (extreme edge case)**
```
1. Simulate network failure (disconnect internet briefly during investigation)
2. Verify: Investigation detects search failures
3. Check: Error messages clear ("Web search unavailable, cannot proceed")
4. Verify: No partial/corrupt results presented as valid
```

**Execution (Scenario 1 - Rate limiting):**
```bash
# Rapid-fire searches to trigger Google rate limit
for i in {1..10}; do
  echo "Query $i: test anthropic claude $i"
  # Execute via google-search MCP
done

# Then run investigation
claude-code "Analyse: 'OpenAI GPT-4 capabilities'.
Load system.md + kb/.
Truth Engine SIMPLE protocol."
```

**Validation:**
- ✅ Investigation completes (doesn't crash)
- ✅ Uses DuckDuckGo results if Google fails
- ✅ EDI score meets SIMPLE minimum (≥0.30) even without dual-engine bonus
- ✅ Error handling logs Google failure gracefully (no stack traces to user)

**Success criteria:**
- All 3 scenarios handled gracefully
- No data loss or corruption
- Clear error messages if total search failure
- Fallback to DuckDuckGo always works

---

## Post-Implementation Validation

After completing all tasks:

### Checklist

- [ ] Task 1: google-search-mcp installed and tested standalone
- [ ] Task 2: .mcp.json configured with google-search server
- [ ] Task 3: Auto-approval permissions added for google-search MCP
- [ ] Task 4: Google Search MCP loads in Claude Code session
- [ ] Task 5: system.md updated with parallel search orchestration protocol
- [ ] Task 6: Result fusion algorithm documented/implemented
- [ ] Task 7: EDI calculation enhanced with dual-engine bonus
- [ ] Task 8: SIMPLE investigation test passed (EDI ≥ 0.45)
- [ ] Task 9: COMPLEX investigation test passed (EDI ≥ 0.85, ISN ≥ 9.0, wolves ≥ 8)
- [ ] Task 10: Fallback scenarios tested (graceful degradation verified)

### Metrics Comparison (Before vs After)

**Run identical investigation BEFORE and AFTER integration:**

Example: "France unemployment 7.4% official statistics"

**BEFORE (DuckDuckGo only):**
- EDI: 0.52 (MEDIUM baseline)
- Sources: 8 total (◈2, ◉3, ○3)
- source_diversity: 0.35
- PRIMARY sources: 2 (INSEE, Eurostat)

**AFTER (DuckDuckGo + Google):**
- EDI: 0.68 (+0.16 boost) ← TARGET
- Sources: 12 total (◈3, ◉5, ○4)
- source_diversity: 0.52 (+0.17 boost from dual engines + more domains)
- PRIMARY sources: 3 (INSEE, Eurostat, DARES via Google)

**Expected improvements:**
- EDI boost: +0.15 to +0.25
- PRIMARY source discovery: +20% to +50% (Google surfaces official docs DuckDuckGo misses)
- Productive query rate: 80-100% (query optimization + dual engines)

---

## Rollback Plan

If integration causes issues:

### Immediate Rollback (2 min)

```bash
# 1. Restore .mcp.json backup
cp /home/giak/projects/truth-engine/.mcp.json.backup /home/giak/projects/truth-engine/.mcp.json

# 2. Remove google-search permissions from settings.local.json
# (Edit manually, remove "mcp__google-search__search" line)

# 3. Restart Claude Code session
# Google Search MCP no longer loaded, system reverts to DuckDuckGo only
```

### Partial Rollback (keep config, disable execution)

If Google Search causes rate limiting issues but want to keep it configured:

**Edit system.md:**
```markdown
## Web Search Execution (v8.4 - GOOGLE DISABLED)

**TEMPORARY:** Google Search disabled due to rate limiting.
Use DuckDuckGo (web-search) ONLY until resolved.

# Comment out parallel execution logic
# Revert to single-engine (DuckDuckGo) calls
```

This preserves configuration but prevents Google Search usage until issues resolved.

---

## Success Criteria Summary

1. **Installation:** google-search-mcp works via npx
2. **Configuration:** .mcp.json and permissions correctly set
3. **Integration:** Both engines queried in parallel, results fused
4. **EDI Boost:** +0.15 to +0.25 improvement on identical investigations
5. **PRIMARY Source Discovery:** Improved (Google surfaces official docs)
6. **Graceful Degradation:** System works with DuckDuckGo only if Google fails
7. **No Regressions:** Existing investigations still pass quality gates
8. **Performance:** No significant latency increase (parallel execution offsets dual queries)

---

## Future Enhancements (Out of Scope)

- **Rate limit mitigation:** Proxy rotation, request throttling
- **Additional search engines:** Bing, Brave Search, Yandex (for geo-diversity)
- **Search quality scoring:** Rank fusion algorithms (Reciprocal Rank Fusion)
- **Cache layer:** Deduplicate identical queries across investigations
- **A/B testing:** Quantify EDI improvement across 100+ investigations

---

**END OF PLAN**

This plan is ready for execution via:
1. **Subagent-Driven Development** (recommended): Dispatch fresh subagent per task with code review checkpoints
2. **Parallel Session Execution**: Developer executes tasks manually, reports back for validation

Which execution mode would you prefer?
