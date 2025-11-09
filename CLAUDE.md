# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is Truth Engine?

**NOT a traditional codebase.** Truth Engine is a cognitive framework for hostile epistemic analysis, implemented as:
- **LLM prompt system** ([system.md](system.md:1)) - Core execution protocol
- **Knowledge base** ([kb/](kb/)) - 16 markdown files defining formulas, patterns, and investigation protocols
- **MCP integration** - Uses MnemoLite (semantic search/memory), Context7 (docs), and web-search for information gathering

**Core principle:** "One narrative = propaganda. Five narratives = cartography." Analyze claims through adversarial multi-perspective investigation.

## Architecture

```
truth-engine/
├── system.md          # LLM instruction protocol (v7.17)
├── kb/                # Knowledge base (core intelligence)
│   ├── COGNITIVE_DSL.md      # Formulas, symbols, 148 concepts (80KB)
│   ├── PATTERNS.md           # 20+ manipulation patterns (108KB)
│   ├── SEARCH_EPISTEMIC.md   # Source stratification, EDI formula (73KB)
│   ├── QUERY_TEMPLATES.md    # Domain-adaptive search templates, H7 map (18KB)
│   ├── INVESTIGATION.md      # Investigation depth protocols L0-L9 (41KB)
│   ├── VALIDATION.md         # Post-search validation loop (9KB)
│   └── HANDOFF_MEMO.md       # Multi-conversation iteration workflow (15KB)
├── PRD.md             # Product Requirements v7.15.1 (20KB)
├── TAD.md             # Technical Architecture (289KB)
├── PFD.md             # Philosophical Foundation (61KB)
├── MCP_STATUS.md      # MCP server configuration status
└── logs/              # Investigation outputs (auto-created)
```

## Running Investigations

### Basic Investigation

```bash
claude-code "Analyse: [subject]. Load system.md + kb/. Truth Engine protocol."
```

**Example:**
```bash
claude-code "Analyse: 'Unemployment 7.4% France'. Load system.md + kb/. Full Truth Engine protocol."
```

### Investigation with MCP (Recommended)

**Prerequisites:** MCP configured (see [MCP_STATUS.md](MCP_STATUS.md:1))

```bash
claude-code "Analyse [subject]. Use MnemoLite MCP semantic search KB. Context7 web search. Truth Engine protocol."
```

**What happens:**
1. **Complexity assessment** (0-10 scale, 6 dimensions) → determines SIMPLE/MEDIUM/COMPLEX/APEX
2. **Query allocation** (primary ◈, adversary H7, context ⟐, diversity, opportunistic)
3. **Web searches** via domain-adaptive templates ([kb/QUERY_TEMPLATES.md](kb/QUERY_TEMPLATES.md:1))
4. **Validation** - checks coverage gaps, retries if budget remaining
5. **Pattern detection** - 20+ patterns (ICEBERG, MONEY, BIO, NET, WAR, TEMP, etc.)
6. **Output** - 3-part structure:
   - Part 1: French tri-perspective analysis (Academic ⟐🎓, Dissident 🔥⟐̅, Arbitrage)
   - Part 2: Technical diagnostics (IVF/ISN/IVS/EDI, patterns, sources)
   - Part 3: WOLF report (if political/geopolitical/corporate)

### APEX Investigation (Complex Topics)

For high-complexity subjects (politics, geopolitics, corporate scandals):

```bash
claude-code "Investigation APEX: [complex subject].
Load system.md + kb/ via MnemoLite semantic search.
Target: EDI≥0.60, sources≥15, wolves≥8 if political.
Save logs/$(date +%Y-%m-%d)_subject.md"
```

## Key Concepts

### Quality Metrics

- **EDI (Epistemic Diversity Index)**: 0.0-1.0, measures source diversity across 6 dimensions (see [kb/SEARCH_EPISTEMIC.md](kb/SEARCH_EPISTEMIC.md:1))
  - SIMPLE≥0.30, MEDIUM≥0.50, COMPLEX≥0.70, APEX≥0.80
- **ISN (Information Source Network)**: 0.0-10.0, network robustness score
  - Political≥9.0, Tech/Corp≥9.0, Financial≥7.0, Geo≥8.5
- **IVF (Information Volume Factor)**: Source count relative to complexity
- **Conf (Confidence)**: <5% uncertainty in final claims

### Source Stratification

- **◈ PRIMARY**: Independent investigative journalism, specialized academic sources
- **◉ SECONDARY**: Mainstream media (fact-checked, transparent)
- **○ TERTIARY**: Institutional, corporate, state-affiliated sources

### H7 Adversary Map

When controversy≥6 (political/geopolitical topics), automatically query adversarial sources (RT, TASS, TeleSUR, PressTV, CGTN, etc.) to prevent Western-centric bias. See [kb/QUERY_TEMPLATES.md](kb/QUERY_TEMPLATES.md:1) §3 for full H7 map.

### Investigation Depth Levels

- **L0 (5min)**: Surface analysis
- **L1 (10min)**: Actor identification + qui_paie (who pays)?
- **L2 (15min)**: Cui bono - 3 levels (visible×1, shadow×10, black×100)
- **L3 (20min)**: Pattern detection + omissions analysis
- **L4 (25min)**: Timing analysis (prob<0.01% coincidences?)
- **L5 (30min)**: Power archaeology (historical context)
- **L6 (ALWAYS)**: Counter-narrative (assume official=lie)
- **L7 (⚔≥2)**: Warfare patterns
- **L8 (🌐≥2)**: Network analysis
- **L9 (⏰≥2)**: Temporal/historical patterns

## Working with the Knowledge Base

### Loading KB Files

**Always load system.md first:**
```bash
# In investigation prompt:
"Load /home/giak/projects/truth-engine/system.md + kb/"
```

**With MnemoLite MCP (semantic search):**
```bash
# MCP automatically indexes and retrieves relevant KB sections
"Use MnemoLite semantic search for KB concepts (COGNITIVE_DSL, PATTERNS, etc.)"
```

### KB File Reference

| File | Purpose | Size | Key Sections |
|------|---------|------|--------------|
| [COGNITIVE_DSL.md](kb/COGNITIVE_DSL.md:1) | Formulas (IVF/ISN/EDI), 148 concepts, symbolic language | 80KB | §0 Philosophy, §1 Atoms, §2 Formulas |
| [SEARCH_EPISTEMIC.md](kb/SEARCH_EPISTEMIC.md:1) | Source stratification (◈◉○), EDI formula | 73KB | §1.3 Stratification, §11 EDI |
| [PATTERNS.md](kb/PATTERNS.md:1) | 20+ manipulation patterns | 108KB | ICEBERG, MONEY, BIO, NET, WAR, TEMP |
| [QUERY_TEMPLATES.md](kb/QUERY_TEMPLATES.md:1) | Domain-adaptive search templates, H7 map | 18KB | §1-3 Templates, §3.1 H7_OVERRIDE |
| [INVESTIGATION.md](kb/INVESTIGATION.md:1) | Investigation protocols L0-L9, CASCADE | 41KB | §7 APEX Protocol |
| [VALIDATION.md](kb/VALIDATION.md:1) | Post-search validation loop | 9KB | §1-5 Validation, §6 Penalties |
| [HANDOFF_MEMO.md](kb/HANDOFF_MEMO.md:1) | Multi-conversation iteration | 15KB | I0→I1→I2 workflow |

### Improving the KB

**KISS principle:** Problem detected → fix KB file directly, no complex process.

**Common improvements:**
- Pattern missing → Add to [kb/PATTERNS.md](kb/PATTERNS.md:1)
- Formula imprecise → Adjust [kb/COGNITIVE_DSL.md](kb/COGNITIVE_DSL.md:1)
- Low EDI → Extend [kb/QUERY_TEMPLATES.md](kb/QUERY_TEMPLATES.md:1) H7 map
- Validation gaps → Update [kb/VALIDATION.md](kb/VALIDATION.md:1)

**Workflow:**
1. Run investigation
2. Note gaps/issues (EDI low, pattern missed, H7 coverage insufficient)
3. Edit relevant KB file
4. Reindex if using MnemoLite: `curl -X POST http://localhost:8001/api/v1/index/reindex -d '{"repository": "truth-engine-kb"}'`
5. Re-run investigation to validate improvement

## MCP Integration

### Required MCP Servers

See [MCP_STATUS.md](MCP_STATUS.md:1) for current configuration status.

**MnemoLite** (code intelligence + semantic memory):
- `search_code` - Hybrid semantic search KB
- `write_memory`, `update_memory`, `delete_memory` - Cross-session memory
- `index_project` - Index KB for semantic search

**Context7** (library documentation):
- `resolve-library-id`, `get-library-docs`

**Web Search** (general search):
- `search` - Google search for investigations

### Indexing KB with MnemoLite

**First time setup:**
```bash
# Via MCP tool (when connected):
index_project(
  project_path="/home/giak/projects/truth-engine/kb",
  repository="truth-engine-kb"
)
```

**Reindex after KB changes:**
```bash
# Via API:
curl -X POST http://localhost:8001/api/v1/index/reindex \
  -H "Content-Type: application/json" \
  -d '{"repository": "truth-engine-kb"}'
```

## Output Structure

Every investigation produces 3 parts:

### Part 1 — French Natural Language
- Sources cited (3-5 web [Name—URL] or KB only)
- Warnings (validation gaps if any)
- Subject + Hermeneutic analysis + Detected concepts
- **Tri-perspective** (Academic ⟐🎓, Dissident 🔥⟐̅, Arbitrage) - 95% symmetric hostility
- Critical points (≥4) + Recommendations
- Gaps & Credibility Impact

### Part 2 — Technical Diagnostics
```
[DIAGNOSTICS] IVF ISN IVS Conf
[MODULES] Λ Φ Ξ Ω Ψ Σ Κ ρ κ € ♦ ⚔ 🌐 ⏰
[SOURCES] ◈◉○ counts, EDI score, diversity metrics
[PATTERNS] Detected patterns with scores
[WOLVES] Individual actors (≥8 political, ≥5 corporate)
[REFLECTION] Meta-analysis
```

### Part 3 — WOLF Report
If political/geopolitical/corporate AND wolves≥threshold:
- Individual actor mapping (≥50% ratio individuals vs institutions)
- Network analysis
- Power archaeology

Otherwise: "(WOLF not applicable)"

## Common Pitfalls

1. **Missing system.md load** → Investigation will fail, KB concepts unknown
2. **Not checking MCP status** → Web searches limited, KB not indexed
3. **Ignoring EDI targets** → Investigation quality insufficient
4. **Skipping validation warnings** → Source gaps unaddressed
5. **Not using H7 adversary sources** → Western-centric bias on political topics
6. **Forgetting complexity assessment** → Wrong resource allocation

## Quality Targets

**Minimums per complexity:**
- **SIMPLE**: EDI≥0.30, ◈≥1, geo_diversity≥0.30
- **MEDIUM**: EDI≥0.50, ◈≥2, geo_diversity≥0.35
- **COMPLEX**: EDI≥0.70, ◈≥3, geo_diversity≥0.40
- **APEX**: EDI≥0.80, ◈≥3, geo_diversity≥0.50

**ISN targets by domain:**
- Political/Geopolitical ≥9.0
- Tech/Corporate ≥9.0
- Financial/Pharma ≥7.0

**Pattern detection:** If signals present (€3, ♦3, ⚔2, etc.), pattern MUST be detected and reported.

## Meta-Development Workflow

Truth Engine is self-improving. After investigations:

1. **Collect feedback** - Note EDI scores, pattern misses, H7 gaps
2. **Analyze patterns** - Weekly review of logs/ (if tracking)
3. **Improve KB** - Add patterns, extend H7 map, adjust formulas
4. **Validate** - Re-run similar investigations, compare metrics
5. **Iterate** - Continuous quality improvement

See [VISION.md](VISION.md:1) for detailed meta-development workflows.

## Philosophy

**95% hostility symmetric:** Assume manipulation in official, dissident, AND user claims. No sacred cows.

**User = sovereign decision-maker, NOT oracle.** Truth Engine provides epistemic cartography, user decides.

**"One narrative = propaganda. Five narratives = cartography."**

See [PFD.md](PFD.md:1) for full philosophical foundation (148 concepts).

---

**Version:** Truth Engine v8.0 (system.md v7.17)
**Last updated:** 2025-11-08
