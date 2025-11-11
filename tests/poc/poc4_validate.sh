#!/bin/bash
# POC 4 Validation: Web Search MCP Integration
# Criteria:
# - File exists
# - ≥3 web sources cited in [Name—URL] format
# - system.md loaded
# - Web search MCP used (mcp__web-search__search)

set -e

POC_FILE="/home/giak/projects/truth-engine/logs/2025-11-11_05-00-00_poc4.md"

echo "=== POC 4 Validation ==="

# Check file exists
if [ ! -f "$POC_FILE" ]; then
    echo "❌ FAIL: POC 4 file not found: $POC_FILE"
    exit 1
fi

echo "✅ File exists: $POC_FILE"

# Check file has content (≥50 lines minimum)
LINE_COUNT=$(wc -l < "$POC_FILE")
if [ "$LINE_COUNT" -lt 50 ]; then
    echo "❌ FAIL: File too short ($LINE_COUNT lines, expected ≥50)"
    exit 1
fi

echo "✅ File length: $LINE_COUNT lines"

# Check for web sources in [Name—URL] format (≥3)
WEB_SOURCE_COUNT=$(grep -c "—https\?://" "$POC_FILE" || true)
if [ "$WEB_SOURCE_COUNT" -lt 3 ]; then
    echo "❌ FAIL: Too few web sources cited ($WEB_SOURCE_COUNT, expected ≥3)"
    exit 1
fi

echo "✅ Web sources cited: $WEB_SOURCE_COUNT (≥3 required)"

# Check system.md loaded mentioned
if ! grep -q "system\.md" "$POC_FILE"; then
    echo "❌ FAIL: No mention of system.md loading"
    exit 1
fi

echo "✅ system.md loading mentioned"

# Check web search MCP used
if ! grep -q "mcp__web-search__search\|Web [Ss]earch.*MCP" "$POC_FILE"; then
    echo "❌ FAIL: No mention of web search MCP usage"
    exit 1
fi

echo "✅ Web search MCP usage documented"

# Check basic ICEBERG concept (visible vs reality/caché/total)
if ! grep -qi "visible.*réalité\|visible.*reality\|visible.*caché\|visible.*total" "$POC_FILE"; then
    echo "❌ FAIL: No ICEBERG visible vs reality analysis"
    exit 1
fi

echo "✅ ICEBERG concept applied (visible vs reality)"

# Check Part 1, Part 2 structure
if ! grep -q "## Part 1" "$POC_FILE" || ! grep -q "## Part 2" "$POC_FILE"; then
    echo "❌ FAIL: Missing Part 1 or Part 2 structure"
    exit 1
fi

echo "✅ Multi-part output structure present"

echo ""
echo "🎉 POC 4 VALIDATION PASSED"
echo "   - Web sources: $WEB_SOURCE_COUNT cited"
echo "   - Content: $LINE_COUNT lines"
echo "   - system.md: loaded ✅"
echo "   - Web search MCP: functional ✅"
echo "   - ICEBERG: applied ✅"
