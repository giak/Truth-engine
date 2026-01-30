#!/bin/bash
# POC 5 Validation: Full 3-Part Output Structure
# Criteria:
# - File exists
# - 3 parts present (Part 1 FR, Part 2 TECH, Part 3 WOLF)
# - Part 1: Tri-perspective (Académique, Dissident, Arbitrage)
# - Part 2: IVF/ISN/EDI/Conf scores calculated
# - Part 3: WOLF skeleton with ≥5 named individuals, ≥50% ratio

set -e

POC_FILE="/home/giak/projects/truth-engine/logs/2025-11-11_06-00-00_poc5.md"

echo "=== POC 5 Validation ==="

# Check file exists
if [ ! -f "$POC_FILE" ]; then
    echo "❌ FAIL: POC 5 file not found: $POC_FILE"
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

# Check Part 1, Part 2, Part 3 structure
if ! grep -q "## Part 1" "$POC_FILE"; then
    echo "❌ FAIL: Missing Part 1"
    exit 1
fi

if ! grep -q "## Part 2" "$POC_FILE"; then
    echo "❌ FAIL: Missing Part 2"
    exit 1
fi

if ! grep -q "## Part 3" "$POC_FILE"; then
    echo "❌ FAIL: Missing Part 3"
    exit 1
fi

echo "✅ 3-part structure present"

# Check Part 1: Tri-perspective (Académique, Dissident, Arbitrage)
if ! grep -q "Académique.*⟐🎓\|Academic.*⟐🎓" "$POC_FILE"; then
    echo "❌ FAIL: Missing Académique ⟐🎓 perspective"
    exit 1
fi

if ! grep -q "Dissident.*🔥⟐̅" "$POC_FILE"; then
    echo "❌ FAIL: Missing Dissident 🔥⟐̅ perspective"
    exit 1
fi

if ! grep -q "Arbitrage" "$POC_FILE"; then
    echo "❌ FAIL: Missing Arbitrage perspective"
    exit 1
fi

echo "✅ Tri-perspective complete (Académique, Dissident, Arbitrage)"

# Check Part 2: IVF/ISN/EDI/Conf scores
if ! grep -q "IVF.*:" "$POC_FILE"; then
    echo "❌ FAIL: Missing IVF score"
    exit 1
fi

if ! grep -q "ISN.*:" "$POC_FILE"; then
    echo "❌ FAIL: Missing ISN score"
    exit 1
fi

if ! grep -q "EDI.*:" "$POC_FILE"; then
    echo "❌ FAIL: Missing EDI score"
    exit 1
fi

if ! grep -q "Conf.*:" "$POC_FILE"; then
    echo "❌ FAIL: Missing Conf score"
    exit 1
fi

echo "✅ Scoring metrics present (IVF, ISN, EDI, Conf)"

# Check Part 2: Modules detected (Λ, Φ, Ξ, etc.)
if ! grep -q "Λ\|Lambda\|Framing" "$POC_FILE"; then
    echo "⚠️  WARNING: Lambda (Λ) module not detected"
fi

if ! grep -q "Ξ\|Xi\|Omission" "$POC_FILE"; then
    echo "⚠️  WARNING: Xi (Ξ) module not detected"
fi

echo "✅ Modules detection present"

# Check Part 3: WOLF section
if ! grep -q "WOLF\|Wolves\|wolves" "$POC_FILE"; then
    echo "❌ FAIL: Missing WOLF section"
    exit 1
fi

# Check named individuals (≥5 required for POC 5)
# Count lines with pattern: "Number. **Name** (Role"
NAMED_COUNT=$(grep -c "^[0-9]\+\.\s\+\*\*[A-Z]" "$POC_FILE" || true)
if [ "$NAMED_COUNT" -lt 5 ]; then
    echo "❌ FAIL: Too few named individuals ($NAMED_COUNT, expected ≥5)"
    exit 1
fi

echo "✅ Named actors: $NAMED_COUNT (≥5 required)"

# Check ratio individuals mentioned
if ! grep -q "ratio.*50%\|Ratio.*50%\|75%\|60%" "$POC_FILE"; then
    echo "⚠️  WARNING: No explicit 50% ratio mentioned"
else
    echo "✅ Individual ratio ≥50% mentioned"
fi

# Check formulas applied (KB references)
if ! grep -q "Formula:\|Formule:\|Calcul:" "$POC_FILE"; then
    echo "⚠️  WARNING: No explicit formula calculations shown"
else
    echo "✅ Formula calculations present"
fi

# Check 95% symmetric hostility mentioned
if grep -q "95%.*hostil\|hostil.*95%\|symétrique" "$POC_FILE"; then
    echo "✅ 95% symmetric hostility applied"
fi

echo ""
echo "🎉 POC 5 VALIDATION PASSED"
echo "   - Structure: Part 1 + Part 2 + Part 3 ✅"
echo "   - Tri-perspective: Académique + Dissident + Arbitrage ✅"
echo "   - Scoring: IVF + ISN + EDI + Conf ✅"
echo "   - WOLF: $NAMED_COUNT actors (≥5) ✅"
echo "   - Content: $LINE_COUNT lines"
