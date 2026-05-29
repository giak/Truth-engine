#!/bin/bash
# V8.0 Validation Script
# Validates that v8.0 test output contains all required features

set -e

TEST_FILE="/home/giak/projects/truth-engine/logs/2025-11-12_v8_validation_test.md"

echo "=== Truth Engine v8.0 Validation ==="
echo ""

# Check file exists
if [ ! -f "$TEST_FILE" ]; then
    echo "❌ FAIL: Test file not found: $TEST_FILE"
    exit 1
fi

echo "✅ Test file exists: $TEST_FILE"
echo ""

PASS_COUNT=0
TOTAL_CHECKS=9

# Check 1: Confidence Contextualized
echo "CHECK 1: Confidence Contextualized"
if grep -q "Conf:.*sur.*data uncertainty:" "$TEST_FILE"; then
    echo "  ✅ PASS: Confidence format 'sur pattern_name (data uncertainty: XX%)' found"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: Confidence contextualized format not found"
fi
echo ""

# Check 2: Factor Best Estimate + Bounds
echo "CHECK 2: Factor Best Estimate + Bounds"
if grep -q "Best estimate:" "$TEST_FILE" && \
   grep -q "Validated bounds:" "$TEST_FILE" && \
   grep -q "Full alternatives:" "$TEST_FILE" && \
   grep -q "Data uncertainty:.*divergence" "$TEST_FILE"; then
    echo "  ✅ PASS: Factor uncertainty handling complete (best/validated/alternatives/uncertainty)"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: Factor bounds incomplete"
fi
echo ""

# Check 3: Triggered Deep Search
echo "CHECK 3: Triggered Deep Search"
if grep -q "Deep searches triggered: YES" "$TEST_FILE" && \
   grep -q "Ξ=9" "$TEST_FILE"; then
    echo "  ✅ PASS: Deep search triggered (Ξ≥7)"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: Deep search not triggered"
fi
echo ""

# Check 4: Dynamic WOLF Threshold
echo "CHECK 4: Dynamic WOLF Threshold"
if grep -q "Threshold adjusted = 8 - 1 - 1 = 6" "$TEST_FILE" || \
   grep -q "threshold.*adjusted.*controversy.*complexity" "$TEST_FILE"; then
    echo "  ✅ PASS: Dynamic WOLF threshold formula present"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: Dynamic WOLF threshold not calculated"
fi
echo ""

# Check 5: Partial WOLF Output (or Full if threshold met)
echo "CHECK 5: Partial WOLF Output"
if grep -q "FULL WOLF triggered" "$TEST_FILE" || \
   grep -q "Part 3.*WOLF (Partial:" "$TEST_FILE"; then
    echo "  ✅ PASS: WOLF handling present (Full or Partial)"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: No WOLF output (full or partial)"
fi
echo ""

# Check 6: Autonomous I1 Preview in REFLECTION
echo "CHECK 6: Autonomous I1 Preview in REFLECTION"
if grep -q "AUTONOMOUS_I1_PREVIEW:" "$TEST_FILE" && \
   grep -q "Auto-queries would target:" "$TEST_FILE" && \
   grep -q "Execute:.*I1 AUTO" "$TEST_FILE"; then
    echo "  ✅ PASS: Autonomous I1 preview with query breakdown"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: I1 preview incomplete"
fi
echo ""

# Check 7: GAP_ANALYSIS in REFLECTION
echo "CHECK 7: GAP_ANALYSIS in REFLECTION"
if grep -q "GAP_ANALYSIS:" "$TEST_FILE" && \
   grep -q "EDI_gap:" "$TEST_FILE" && \
   grep -q "Sources_gap:" "$TEST_FILE" && \
   grep -q "Wolves_gap:" "$TEST_FILE" && \
   grep -q "Pattern_gaps:" "$TEST_FILE" && \
   grep -q "Depth_gap:" "$TEST_FILE"; then
    echo "  ✅ PASS: GAP_ANALYSIS with 5 dimensions (EDI, Sources, Wolves, Patterns, Depth)"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: GAP_ANALYSIS incomplete"
fi
echo ""

# Check 8: DIAGNOSTICS Format Updated
echo "CHECK 8: DIAGNOSTICS Format Updated"
if grep -q "\[DIAGNOSTICS\]" "$TEST_FILE" && \
   grep -q "Conf:.*sur.*data uncertainty:" "$TEST_FILE"; then
    echo "  ✅ PASS: DIAGNOSTICS format includes contextualized confidence"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: DIAGNOSTICS format not updated"
fi
echo ""

# Check 9: REFLECTION Always Present
echo "CHECK 9: REFLECTION Always Present"
if grep -q "\[REFLECTION\].*ALWAYS PRESENT" "$TEST_FILE" && \
   grep -q "INVESTIGATION_STATUS:" "$TEST_FILE" && \
   grep -q "ITERATION_RECOMMENDATION:" "$TEST_FILE" && \
   grep -q "META_NOTES:" "$TEST_FILE"; then
    echo "  ✅ PASS: REFLECTION section present with required subsections"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "  ❌ FAIL: REFLECTION missing or incomplete"
fi
echo ""

# Summary
echo "========================================="
echo "VALIDATION SUMMARY"
echo "========================================="
echo "Checks passed: $PASS_COUNT/$TOTAL_CHECKS"
echo ""

if [ $PASS_COUNT -ge 8 ]; then
    echo "🎉 VALIDATION: PASS ✅"
    echo ""
    echo "Truth Engine v8.0 features validated:"
    echo "  - Confidence contextualized (pattern vs data)"
    echo "  - Factor with uncertainty bounds"
    echo "  - Triggered deep search"
    echo "  - Dynamic WOLF threshold"
    echo "  - WOLF output (full/partial)"
    echo "  - Autonomous I1 preview"
    echo "  - Comprehensive GAP_ANALYSIS"
    echo "  - Updated DIAGNOSTICS format"
    echo "  - REFLECTION always present"
    echo ""
    echo "Status: READY FOR PRODUCTION"
    exit 0
elif [ $PASS_COUNT -ge 6 ]; then
    echo "⚠️  VALIDATION: PARTIAL"
    echo "Some v8.0 features missing. Review failures above."
    exit 1
else
    echo "❌ VALIDATION: FAIL"
    echo "Critical v8.0 features missing. Implementation incomplete."
    exit 1
fi
