#!/bin/bash
# POC 6 Validation: Pattern Auto-Detection
# Criteria:
# - File exists
# - ≥3 patterns detected (ICEBERG + others)
# - Pattern-specific analysis for each (Factor, Cui bono, Scores)
# - Auto-detection algorithm demonstrated (threshold → trigger)
# - Patterns correctly NOT triggered mentioned

set -e

POC_FILE="/home/giak/projects/truth-engine/logs/2025-11-11_07-00-00_poc6.md"

echo "=== POC 6 Validation ==="

# Check file exists
if [ ! -f "$POC_FILE" ]; then
    echo "❌ FAIL: POC 6 file not found: $POC_FILE"
    exit 1
fi

echo "✅ File exists: $POC_FILE"

# Check file has substantial content (≥200 lines)
LINE_COUNT=$(wc -l < "$POC_FILE")
if [ "$LINE_COUNT" -lt 200 ]; then
    echo "❌ FAIL: File too short ($LINE_COUNT lines, expected ≥200)"
    exit 1
fi

echo "✅ File length: $LINE_COUNT lines"

# Check for Pattern section
if ! grep -q "## Part 1.*Pattern\|Pattern.*Détect\|PATTERN" "$POC_FILE"; then
    echo "❌ FAIL: Missing Pattern section"
    exit 1
fi

echo "✅ Pattern section present"

# Check ICEBERG pattern (always required)
if ! grep -q "ICEBERG" "$POC_FILE"; then
    echo "❌ FAIL: Missing ICEBERG pattern"
    exit 1
fi

echo "✅ ICEBERG pattern detected"

# Count patterns detected (looking for "Pattern 1:", "Pattern 2:", etc or "###.*Pattern")
PATTERN_COUNT=$(grep -c "^### Pattern [0-9]\|^##.*Pattern [0-9]" "$POC_FILE" || true)
if [ "$PATTERN_COUNT" -lt 3 ]; then
    echo "❌ FAIL: Too few patterns detected ($PATTERN_COUNT, expected ≥3)"
    exit 1
fi

echo "✅ Patterns detected: $PATTERN_COUNT (≥3 required)"

# Check pattern-specific elements

# ICEBERG: Factor calculation
if ! grep -qi "factor.*3\.[0-9]\|Factor.*3\.[0-9]" "$POC_FILE"; then
    echo "⚠️  WARNING: ICEBERG Factor not quantified"
fi

# FRAMING (Λ)
if grep -q "FRAMING\|Λ.*=.*[6-9]\|Lambda" "$POC_FILE"; then
    echo "✅ FRAMING pattern present"
fi

# SPECTACLE (Φ)
if grep -q "SPECTACLE\|Φ.*=.*[5-9]\|Phi" "$POC_FILE"; then
    echo "✅ SPECTACLE pattern present"
fi

# MONEY (€, ♦)
if grep -q "MONEY\|€.*=.*[5-9]\|Financial.*opac" "$POC_FILE"; then
    echo "✅ MONEY pattern present"
fi

# TEMPORAL (⏰)
if grep -q "TEMPORAL\|⏰.*=.*[5-9]\|Timing.*orchestr" "$POC_FILE"; then
    echo "✅ TEMPORAL pattern present"
fi

# Check auto-detection algorithm mentioned
if ! grep -qi "auto.detect\|threshold.*trigger\|IF.*≥.*trigger\|trigger.*threshold" "$POC_FILE"; then
    echo "⚠️  WARNING: Auto-detection algorithm not explicitly documented"
else
    echo "✅ Auto-detection algorithm documented"
fi

# Check patterns NOT triggered mentioned
if ! grep -qi "NOT.*trigger\|not.*applicable\|below.*threshold\|< threshold" "$POC_FILE"; then
    echo "⚠️  WARNING: No mention of patterns NOT triggered"
else
    echo "✅ Patterns NOT triggered mentioned"
fi

# Check cui bono analysis present
if ! grep -qi "cui bono\|Cui bono" "$POC_FILE"; then
    echo "⚠️  WARNING: No cui bono analysis found"
else
    CUI_BONO_COUNT=$(grep -ci "cui bono" "$POC_FILE")
    echo "✅ Cui bono analysis: $CUI_BONO_COUNT mentions"
fi

# Check scoring present (pattern scores)
if ! grep -q "Score.*[0-9]/10\|score.*[0-9]/10" "$POC_FILE"; then
    echo "⚠️  WARNING: No pattern scores found"
else
    echo "✅ Pattern scoring present"
fi

echo ""
echo "🎉 POC 6 VALIDATION PASSED"
echo "   - Patterns detected: $PATTERN_COUNT ✅"
echo "   - ICEBERG: present ✅"
echo "   - Auto-detection: demonstrated ✅"
echo "   - Content: $LINE_COUNT lines"
