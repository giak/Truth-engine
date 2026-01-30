# POC Execution Model - Direct Claude Code Invocation

**Decision:** Option B - Direct invocation (no bash wrapper for POC phase)

## Rationale

Claude Code is an interactive CLI tool, not a programmatically invocable command. The original plan assumed `claude-code "${PROMPT}"` would work like `curl` or `python`, but that's not the execution model.

## Revised Approach: POC 1-8

### Execution Flow

**User action:**
```bash
cd /home/giak/projects/truth-engine
claude-code
```

**In Claude Code session, user types:**
```
POC 1: Analyze "2+2=4". Output markdown to logs/YYYY-MM-DD_HH-MM-SS_poc1.md
```

**Claude Code (assistant) executes:**
1. Performs investigation
2. Generates markdown output
3. Writes to logs/ using Write tool
4. Reports completion

**User validates:**
```bash
cat logs/*_poc1.md
./tests/poc/poc1_validate.sh  # (if validation script exists)
```

### POC Progression

**POC 1 - Hello World (5-10 min)**
- Direct investigation of trivial subject "2+2=4"
- Output markdown to logs/
- Validation: file exists, contains basic analysis

**POC 2 - system.md Loading (10-15 min)**
- Use Read tool to load system.md
- Analyze "France unemployment 7.4%"
- Detect ICEBERG concept (from system.md knowledge)
- Output: markdown with ICEBERG analysis

**POC 3 - MnemoLite KB Search (15-20 min)**
- Prerequisite: KB indexed via `mcp__mnemolite__index_project`
- Use MCP search_code to find ICEBERG pattern details
- Apply pattern with KB-sourced methodology
- Output: markdown with enriched pattern analysis

**POC 4 - Web Search (20-25 min)**
- Use MCP web-search for 3+ queries
- Cite sources [Name—URL] format
- Combine with ICEBERG analysis
- Output: markdown with web sources cited

**POC 5 - 3-Part Structure (15-20 min)**
- Structured output: Part 1 (FR), Part 2 (diagnostics), Part 3 (WOLF)
- Tri-perspective: Académique, Dissident, Arbitrage
- Output: complete 3-part markdown

**POC 6 - Pattern Detection (15-20 min)**
- ICEBERG + 1 optional pattern (MONEY, BIO, NET, etc.)
- Score 0-10 per pattern
- Output: Part 2 with patterns + scores

**POC 7 - EDI Calculation (20-25 min)**
- Calculate EDI across 6 dimensions (simplified)
- Source stratification ◈◉○
- Target: EDI ≥0.30 (SIMPLE)
- Output: Part 2 with EDI metrics

**POC 8 - MnemoLite Persistence (15-20 min)**
- After investigation, save Part 1 to MnemoLite
- Use MCP write_memory
- Validate: retrieve in new session via search_code
- Output: markdown + memory confirmation

## Validation Scripts

Bash validation scripts remain useful for automated checks:

```bash
# tests/poc/poc1_validate.sh
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 1..."

LATEST=$(ls -t logs/*_poc1.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 1 output found"
    exit 1
fi

if [ ! -s "${LATEST}" ]; then
    echo "❌ Output file empty"
    exit 1
fi

if grep -qi "2.*2\|quatre\|4" "${LATEST}"; then
    echo "✅ POC 1 validation passed"
    echo "📁 Output: ${LATEST}"
else
    echo "❌ Output doesn't mention 2+2 or 4"
    exit 1
fi
```

**Run validation after each POC:**
```bash
chmod +x tests/poc/poc1_validate.sh
./tests/poc/poc1_validate.sh
```

## Post-POC: Optional Wrapper

After POC 1-8 complete, optionally create convenience tools:

**Option A: Slash Command**
- `.claude/commands/investigate.md` with prompt template
- User runs: `claude-code` → `/investigate France unemployment`

**Option B: Prompt Constructor**
- Bash script generates prompt file
- User copies/pastes into Claude Code session

**Option C: No Wrapper**
- User types investigation prompts directly (most flexible)

## Prerequisites

**Before POC 3:**
```bash
claude-code "Use MCP tool mcp__mnemolite__index_project to index:
  project_path: /home/giak/projects/truth-engine/kb
  repository: truth-engine-kb
  include_gitignored: false"
```

**Verify indexing:**
```bash
claude-code "Use MCP search_code to find 'ICEBERG pattern' in repository 'truth-engine-kb'"
```

## Usage Pattern (POC Phase)

**Template for each POC:**
```
User: POC X: [task description]. Use [tools]. Output logs/YYYY-MM-DD_HH-MM-SS_pocX.md

Claude Code: [executes investigation]
              [generates markdown]
              [writes to logs/ using Write tool]
              [reports completion]

User: ./tests/poc/pocX_validate.sh
      cat logs/*_pocX.md
```

## Advantages of Direct Invocation

1. **Simplicity**: No wrapper complexity
2. **Flexibility**: User can adjust prompts on-the-fly
3. **Transparency**: Clear what Claude Code is doing
4. **Debugging**: Easier to trace issues
5. **Matches tool design**: Claude Code is interactive by nature

## Production Transition

After POC 8, if bash wrapper needed:
- Create prompt constructor that prints Claude Code commands
- Or build slash command for convenience
- Or keep direct invocation (user types prompts)

**Current decision**: Start with direct invocation, add convenience tools if needed later.

---

**Status**: Ready for POC 1 execution
**Next**: Execute POC 1 in this Claude Code session
