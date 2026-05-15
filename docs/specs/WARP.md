# Truth Engine - Claude Code Context

**Essential files** :
- **System prompt** : [system.md](system.md:1) - LLM execution protocol (load first)
- **Knowledge base** : [kb/](kb/) - 16 MD files (use MnemoLite semantic search, don't load all)
- **Architecture** : [TAD.md](TAD.md:1) - 289KB (load on-demand only)
- **Philosophy** : [PFD.md](PFD.md:1) - 61KB (load on-demand only)
- **Full doc** : [CLAUDE_FULL.md](CLAUDE_FULL.md:1) - Version complète si besoin

**Core principle** : "One narrative = propaganda. Five narratives = cartography."

## Investigation Commands

**Basic** :
```bash
claude "Analyse: [subject]. Load system.md + kb/. Truth Engine protocol."
```

**With MCP** (recommended) :
```bash
claude "Analyse [subject]. Use MnemoLite semantic search KB. Context7 docs. WebSearch. Truth Engine protocol."
```

**APEX** (complex topics) :
```bash
claude "Investigation APEX: [subject]. Load system.md. MnemoLite KB search. Target: EDI≥0.60, sources≥15."
```

## Key Principles (Résumé)

- **95% symmetric hostility** to ALL narratives (official + dissident)
- **◈ PRIMARY sources arbitrate** (leaks, documents, data)
- **EDI targets** : SIMPLE≥0.30, COMPLEX≥0.70, APEX≥0.80
- **H7 adversary map** for controversy≥6 (political/geopolitical)
- **10 Commandments** non-negotiable (see CLAUDE_FULL.md)
- **Investigation depth** : L0-L9, minimum L6 (counter-narrative)

## Quality Metrics

- **EDI** (Epistemic Diversity Index) : 0.0-1.0, source diversity 6 dimensions
- **ISN** (Information Source Network) : 0.0-10.0, network robustness
- **Source stratification** : ◈ PRIMARY > ◉ SECONDARY > ○ TERTIARY
- **Wolves** : ≥8 individuals (political), ≥5 (corporate)

## MCP Integration

**Required servers** (see [MCP_STATUS.md](MCP_STATUS.md:1)) :
- **MnemoLite** :
  - `search_code` → KB files search (concepts DSL, patterns)
  - `memories://search/{query}` → **Past investigations search** (PHASE 0.5)
  - `write_memory` → Save investigations (PHASE 9)
  - `index_project` → Index KB files
- **Context7** : `resolve-library-id`, `get-library-docs`
- **WebSearch** : Google API (95%+ success) + MCP web-search fallback (DuckDuckGo)

**CRITICAL DISTINCTION** :
- Pour chercher des **concepts DSL** (kb/) → `mcp__mnemolite__search_code`
- Pour chercher des **investigations passées** → `ReadMcpResourceTool(server="mnemolite", uri="memories://search/{query}")`

**Index KB** :
```bash
index_project(project_path="/home/giak/projects/truth-engine/kb", repository="truth-engine-kb")
```

## Output Structure

**Part 1** - French analysis : Tri-perspective (Academic ⟐🎓, Dissident 🔥⟐̅, Arbitrage)
**Part 2** - Diagnostics : IVF/ISN/EDI, patterns, sources, wolves
**Part 3** - WOLF report (if political/corporate)

## Common Pitfalls

1. Missing `system.md` load → Investigation fails
2. Loading all KB files → Use MnemoLite semantic search instead
3. Ignoring EDI targets → Quality insufficient
4. Loading TAD.md/PFD.md automatically → Load on-demand only
5. Violating 10 Commandments → Investigation fails quality gates

## Knowledge Graph Integration (v10.5)

**MnemoLite MCP Flow:**
1. PHASE 0.5: `memories://search/{query}` - Hybrid search (lexical + vector + RRF) for past investigations
2. PHASE 3.5: `HISTORICAL_PRECEDENTS` - WebSearch FR+EN for top 3 patterns ≥5
3. PHASE 8: Generate `## SEARCH_INDEX` section
4. PHASE 9: `write_memory` - Save investigation to MnemoLite

**PHASE 3.5 Details:**
- Trigger: Top 3 patterns with score ≥5 (MEDIUM+ investigations only)
- Searches: 2 per pattern (FR + EN) = 6 max
- Output: `📜 PRÉCÉDENT:` inline under each pattern
- Purpose: Prove technique has historical precedents

**Benefits:**
- Primary sources (◈) accumulate across investigations
- Avoid redundant research on related topics
- EDI improves with reused validated sources
- Historical precedents strengthen textual analysis

## Substack Engine (v2.0)

**Purpose:** Publish investigations to Substack with tweet hooks - **adaptive length + LLM autonomy**

**Files:**
- System prompt: [prompts/systems/substack-engine-v2.0.md](prompts/systems/substack-engine-v2.0.md)
- Design doc: [docs/plans/2025-11-27-substack-engine-v2-design.md](docs/plans/2025-11-27-substack-engine-v2-design.md)
- Legacy v1.0: [prompts/systems/substack-engine-v1.0.md](prompts/systems/substack-engine-v1.0.md)
- API: `~/projects/Substack-API/` (external, not in repo)

**Usage:**
```bash
# 1. Start API server (separate terminal)
cd ~/projects/Substack-API && source venv/bin/activate && python api_server.py

# 2. Generate article + tweet
claude "Mode SUBSTACK: logs/2025-11-26_investigation.md"
```

**v2.0 Key Changes:**
- **Adaptive length**: 800-6000+ words (based on investigation richness)
- **LLM autonomy**: Decides optimal structure, no arbitrary limits
- **Gate 5 replaced**: Content Integrity (was: length check)
- **Gate 6 added**: Coherence check
- **ICEBERG integration**: Deep layers get dedicated sections for APEX

**Workflow:**
1. PHASE 0: Content Analysis + LLM decision on format/length
2. PHASE 1: Generate tweet hook (≤235 chars + URL)
3. PHASE 2: Generate Substack article (adaptive length)
4. PHASE 3: Quality Gates (6 gates including Content Integrity)
5. PHASE 4: Publish via API → Get URL

**Length Guidance:**
| Investigation Type | Source Words | Article Words |
|-------------------|--------------|---------------|
| SIMPLE | ≤2000 | 800-1500 |
| MEDIUM | 2000-4000 | 1500-3000 |
| COMPLEX | 4000-6000 | 3000-5000 |
| APEX | 6000+ | 4000-6000+ |

**Output files:**
- `prompts/outputs/YYYY-MM-DD_sujet-substack.md` - Article backup
- `prompts/outputs/YYYY-MM-DD_sujet-tweet.txt` - Tweet ready to post
- `prompts/outputs/YYYY-MM-DD_sujet-meta.json` - Metadata (extended v2.0)

---

**Version** : Truth Engine v10.5 HISTORICAL_PRECEDENTS (system.md v10.5)
**Full documentation** : [CLAUDE_FULL.md](CLAUDE_FULL.md:1) (582 lines)
