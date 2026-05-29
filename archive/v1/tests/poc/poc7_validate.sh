#!/bin/bash
# POC 7 Validation: EDI Targeting - Source Diversification
# Criteria:
# - File exists
# - EDI improvement demonstrated (POC 6 → POC 7)
# - ≥9 sources (diversification from POC 6's 5)
# - Geographic diversity increased (France + EU/OECD)
# - Perspectives diversity (⟐🎓🌍⟐̅)
# - Comparative analysis present

set -e

POC_FILE="/home/giak/projects/truth-engine/logs/2025-11-11_09-00-00_poc7.md"

echo "=== POC 7 Validation ==="

# Check file exists
if [ ! -f "$POC_FILE" ]; then
    echo "❌ FAIL: POC 7 file not found: $POC_FILE"
    exit 1
fi

echo "✅ File exists: $POC_FILE"

# Check file has substantial content (≥250 lines)
LINE_COUNT=$(wc -l < "$POC_FILE")
if [ "$LINE_COUNT" -lt 250 ]; then
    echo "❌ FAIL: File too short ($LINE_COUNT lines, expected ≥250)"
    exit 1
fi

echo "✅ File length: $LINE_COUNT lines"

# Check EDI mentioned and improvement demonstrated
if ! grep -q "EDI.*:" "$POC_FILE"; then
    echo "❌ FAIL: EDI not calculated"
    exit 1
fi

if ! grep -qi "amélioration\|improvement\|POC 6.*POC 7\|vs POC 6" "$POC_FILE"; then
    echo "❌ FAIL: No improvement comparison with POC 6"
    exit 1
fi

echo "✅ EDI improvement demonstrated"

# Check source count (≥9 for diversification)
SOURCE_COUNT=$(grep -c "^[0-9]\+\.\s\+\*\*[A-Z].*—http" "$POC_FILE" || true)
if [ "$SOURCE_COUNT" -lt 9 ]; then
    echo "❌ FAIL: Too few sources ($SOURCE_COUNT, expected ≥9)"
    exit 1
fi

echo "✅ Sources cited: $SOURCE_COUNT (≥9 diversification)"

# Check international sources present
if ! grep -qi "OECD\|ILO\|Eurostat\|World Bank" "$POC_FILE"; then
    echo "❌ FAIL: No international sources (OECD/ILO/Eurostat/World Bank)"
    exit 1
fi

echo "✅ International sources present (OECD/ILO/Eurostat/World Bank)"

# Check geographic diversity (France + EU countries)
if ! grep -qi "Allemagne\|Germany\|Espagne\|Spain\|UK\|United Kingdom" "$POC_FILE"; then
    echo "❌ FAIL: No EU country comparisons"
    exit 1
fi

echo "✅ Geographic diversity: EU comparisons present"

# Check perspectives diversity (⟐🎓🌍⟐̅)
PERSPECTIVES_COUNT=0

if grep -q "⟐🎓\|Académique.*🎓\|Academic.*🎓" "$POC_FILE"; then
    PERSPECTIVES_COUNT=$((PERSPECTIVES_COUNT + 1))
    echo "✅ Academic perspective ⟐🎓 present"
fi

if grep -q "🌍\|Regional\|Régional" "$POC_FILE"; then
    PERSPECTIVES_COUNT=$((PERSPECTIVES_COUNT + 1))
    echo "✅ Regional perspective 🌍 present"
fi

if grep -q "⟐̅\|Dissident.*🔥" "$POC_FILE"; then
    PERSPECTIVES_COUNT=$((PERSPECTIVES_COUNT + 1))
    echo "✅ Dissident perspective ⟐̅ present"
fi

if [ "$PERSPECTIVES_COUNT" -lt 3 ]; then
    echo "❌ FAIL: Too few perspectives ($PERSPECTIVES_COUNT, expected ≥3)"
    exit 1
fi

# Check comparative analysis (benchmarking)
if ! grep -qi "compar\|benchmark\|vs\|versus" "$POC_FILE"; then
    echo "⚠️  WARNING: No explicit comparative analysis"
else
    echo "✅ Comparative analysis present"
fi

# Check EDI breakdown by dimensions
if ! grep -q "geo.*:\|Geographic\|lang.*:\|Language\|strat.*:\|Stratification\|own.*:\|Ownership\|persp.*:\|Perspectives\|temp.*:\|Temporal" "$POC_FILE"; then
    echo "⚠️  WARNING: EDI breakdown not detailed"
else
    echo "✅ EDI breakdown by dimensions present"
fi

# Check improvement metrics
if grep -q "+[0-9]\+%\|amélioration.*%" "$POC_FILE"; then
    echo "✅ Improvement percentages calculated"
fi

echo ""
echo "🎉 POC 7 VALIDATION PASSED"
echo "   - Sources: $SOURCE_COUNT (diversified) ✅"
echo "   - Perspectives: $PERSPECTIVES_COUNT (⟐🎓🌍⟐̅) ✅"
echo "   - Geographic: EU comparisons ✅"
echo "   - International: OECD/ILO/Eurostat ✅"
echo "   - EDI: improvement demonstrated ✅"
echo "   - Content: $LINE_COUNT lines"
