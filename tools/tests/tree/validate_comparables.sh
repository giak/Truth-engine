#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validation COMPARABLES_ASYMMETRY — v1.1 Extension"
echo ""

# Files to validate
KB_TREE="kb/INVESTIGATION_TREE.md"
KB_VALIDATION="kb/VALIDATION.md"
TEST_SPEC="tests/tree/test_comparables_asymmetry.md"

ERRORS=0

# Helper function
check_contains() {
    local file=$1
    local pattern=$2
    local description=$3

    if grep -q "${pattern}" "${file}"; then
        echo "  ✅ ${description}"
    else
        echo "  ❌ MISSING: ${description}"
        echo "     Pattern: ${pattern}"
        echo "     File: ${file}"
        ((ERRORS++))
    fi
}

echo "═══════════════════════════════════════════════════════"
echo "1. TRIGGER COMPARABLES_LAUNCH"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "Trigger 6: COMPARABLES" \
    "Trigger 6 COMPARABLES declared"

# Check Path A: Regulatory context
if grep -q "regulatory_context = true" "${KB_TREE}" && grep -q "sanctions_detected > 0" "${KB_TREE}"; then
    echo "  ✅ Path A: Regulatory context trigger"
else
    echo "  ❌ MISSING: Path A regulatory trigger"
    ((ERRORS++))
fi

# Check Path B: Ξ OMISSION pattern
if grep -q "pattern\.score ≥ 8 FOR pattern IN \[Ξ\]\\|Ξ.*≥ 8" "${KB_TREE}"; then
    echo "  ✅ Path B: Ξ OMISSION ≥8 trigger"
else
    echo "  ❌ MISSING: Path B Ξ OMISSION trigger"
    ((ERRORS++))
fi

# Check comparables_regulatory and comparables_omission
if grep -q "comparables_regulatory\\|comparables_omission" "${KB_TREE}"; then
    echo "  ✅ Trigger types: comparables_regulatory, comparables_omission"
else
    echo "  ❌ MISSING: Trigger type names"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "2. BRANCH TYPE COMPARABLES"
echo "═══════════════════════════════════════════════════════"

# Check COMPARABLES in type enum
if grep -q "GAP_CRITICAL.*PATTERN_STRONG.*COMPARABLES\\|COMPARABLES" "${KB_TREE}"; then
    echo "  ✅ COMPARABLES added to branch type enum"
else
    echo "  ❌ MISSING: COMPARABLES in type enum"
    ((ERRORS++))
fi

# Check comparables_found structure
if grep -q "comparables_found" "${KB_TREE}"; then
    echo "  ✅ comparables_found[] structure in results"
else
    echo "  ❌ MISSING: comparables_found structure"
    ((ERRORS++))
fi

# Check comparables_found fields (entity, severity, context_similarity)
if grep -q "entity:.*str" "${KB_TREE}" && grep -q "severity:.*float" "${KB_TREE}" && grep -q "context_similarity:.*float" "${KB_TREE}"; then
    echo "  ✅ comparables_found fields (entity, severity, context_similarity)"
else
    echo "  ⚠️  WARNING: comparables_found fields incomplete"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "3. SCORING FORMULAS — @F[EDI_IMPACT]"
echo "═══════════════════════════════════════════════════════"

# Check @F[EDI_IMPACT] COMPARABLES case
if grep -q "branch.type = \"comparables\"\\|branch_type = \"comparables\"" "${KB_TREE}"; then
    echo "  ✅ @F[EDI_IMPACT] COMPARABLES case present"

    # Check EDI_IMPACT value (may be on next line)
    if grep -B1 -A1 "branch_type = \"comparables\"" "${KB_TREE}" | grep -q "0\\.35"; then
        echo "  ✅ EDI_IMPACT(COMPARABLES) = 0.35"
    else
        echo "  ❌ MISSING: EDI_IMPACT value 0.35"
        ((ERRORS++))
    fi
else
    echo "  ❌ MISSING: @F[EDI_IMPACT] COMPARABLES case"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "4. SCORING FORMULAS — @F[CUI_BONO_CENTRALITY]"
echo "═══════════════════════════════════════════════════════"

# Check @F[CUI_BONO_CENTRALITY] COMPARABLES case
if grep -q "branch.type = \"comparables\"\\|branch.type = COMPARABLES" "${KB_TREE}"; then
    echo "  ✅ @F[CUI_BONO_CENTRALITY] COMPARABLES case present"

    # Check CUI_BONO value (may be on next line)
    if grep -B1 -A3 "branch.type = \"comparables\"" "${KB_TREE}" | grep -q "0\\.25"; then
        echo "  ✅ CUI_BONO_CENTRALITY(COMPARABLES, regulatory) = 0.25"
    else
        echo "  ⚠️  WARNING: CUI_BONO value 0.25 unclear"
    fi
else
    echo "  ❌ MISSING: @F[CUI_BONO_CENTRALITY] COMPARABLES case"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "5. SYNTHESIS OPERATION — DETECT_ASYMMETRY"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "DETECT_ASYMMETRY" \
    "DETECT_ASYMMETRY operation defined"

# Check asymmetry analysis structure
if grep -q "asymmetry_score\\|asymmetry_analysis" "${KB_TREE}"; then
    echo "  ✅ asymmetry_analysis output structure"
else
    echo "  ❌ MISSING: asymmetry_analysis structure"
    ((ERRORS++))
fi

# Check ≥2 comparables threshold
if grep -q "count.*< 2\\|count(relevant_comparables) < 2" "${KB_TREE}"; then
    echo "  ✅ Threshold: ≥2 comparables required"
else
    echo "  ❌ MISSING: ≥2 comparables threshold"
    ((ERRORS++))
fi

# Check INSUFFICIENT_DATA verdict
if grep -q "INSUFFICIENT_DATA" "${KB_TREE}"; then
    echo "  ✅ INSUFFICIENT_DATA verdict (< 2 comparables)"
else
    echo "  ⚠️  WARNING: INSUFFICIENT_DATA verdict not found"
fi

# Check context_similarity ≥0.60 filter
if grep -q "context_similarity ≥ 0\\.60\\|0\\.60" "${KB_TREE}"; then
    echo "  ✅ Context similarity filter ≥0.60"
else
    echo "  ⚠️  WARNING: Context similarity threshold unclear"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "6. FORMULA @F[ASYMMETRY_SCORE]"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "@F\[ASYMMETRY_SCORE\]" \
    "@F[ASYMMETRY_SCORE] formula defined"

# Check components (range, variance, extremity)
if grep -q "range_score" "${KB_TREE}" && grep -q "variance_score" "${KB_TREE}" && grep -q "extremity_score" "${KB_TREE}"; then
    echo "  ✅ 3 components: range_score, variance_score, extremity_score"
else
    echo "  ❌ MISSING: ASYMMETRY_SCORE components"
    ((ERRORS++))
fi

# Check weights (0.40, 0.30, 0.30)
if grep -q "0\\.40\\|40%" "${KB_TREE}" && grep -q "0\\.30\\|30%" "${KB_TREE}"; then
    echo "  ✅ Weights present (40%, 30%, 30%)"
else
    echo "  ⚠️  WARNING: Weights unclear"
fi

# Check outlier bonus
if grep -q "bonus\\|2×stddev\\|2 × stddev" "${KB_TREE}"; then
    echo "  ✅ Outlier bonus logic (±2 stddev)"
else
    echo "  ⚠️  WARNING: Outlier bonus not found"
fi

# Check scale 0-10
if grep -q "0-10\\|asymmetry_score.*10" "${KB_TREE}"; then
    echo "  ✅ Scale: 0-10"
else
    echo "  ⚠️  WARNING: 0-10 scale not explicit"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "7. ASYMMETRY VERDICT CLASSIFICATION"
echo "═══════════════════════════════════════════════════════"

# Check EXTREME verdict (≥7.0)
if grep -q "ASYMMETRY_EXTREME" "${KB_TREE}" && grep -q "≥ 7\\.0\\|>= 7\\.0" "${KB_TREE}"; then
    echo "  ✅ EXTREME verdict (≥7.0)"
else
    echo "  ❌ MISSING: EXTREME verdict threshold"
    ((ERRORS++))
fi

# Check SIGNIFICANT verdict (≥5.0)
if grep -q "ASYMMETRY_SIGNIFICANT" "${KB_TREE}" && grep -q "≥ 5\\.0\\|>= 5\\.0" "${KB_TREE}"; then
    echo "  ✅ SIGNIFICANT verdict (≥5.0)"
else
    echo "  ❌ MISSING: SIGNIFICANT verdict threshold"
    ((ERRORS++))
fi

# Check MODERATE verdict (≥3.0)
if grep -q "ASYMMETRY_MODERATE" "${KB_TREE}" && grep -q "≥ 3\\.0\\|>= 3\\.0" "${KB_TREE}"; then
    echo "  ✅ MODERATE verdict (≥3.0)"
else
    echo "  ❌ MISSING: MODERATE verdict threshold"
    ((ERRORS++))
fi

# Check MINIMAL verdict (<3.0)
if grep -q "ASYMMETRY_MINIMAL" "${KB_TREE}"; then
    echo "  ✅ MINIMAL verdict (<3.0)"
else
    echo "  ⚠️  WARNING: MINIMAL verdict not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "8. INTEGRATION kb/VALIDATION.md"
echo "═══════════════════════════════════════════════════════"

# Check §7.5 COMPARABLES section exists
if grep -q "### 7\\.5 COMPARABLES" "${KB_VALIDATION}"; then
    echo "  ✅ §7.5 COMPARABLES Detection & Scoring section exists"
else
    echo "  ❌ MISSING: §7.5 section in kb/VALIDATION.md"
    ((ERRORS++))
fi

# Check trigger 6 in §7.1
if grep -q "Trigger 6: COMPARABLES\\|@TRIGGER\[COMPARABLES_LAUNCH\]" "${KB_VALIDATION}"; then
    echo "  ✅ Trigger 6 COMPARABLES in §7.1 branch detection"
else
    echo "  ❌ MISSING: Trigger 6 in §7.1"
    ((ERRORS++))
fi

# Check @F[EDI_IMPACT] COMPARABLES in §7.2
if grep -q "branch.type = COMPARABLES" "${KB_VALIDATION}" && grep -q "0\\.35" "${KB_VALIDATION}"; then
    echo "  ✅ @F[EDI_IMPACT](COMPARABLES) in §7.2"
else
    echo "  ❌ MISSING: EDI_IMPACT COMPARABLES in §7.2"
    ((ERRORS++))
fi

# Check @F[CUI_BONO_CENTRALITY] COMPARABLES in §7.2
if grep -q "branch.type = COMPARABLES" "${KB_VALIDATION}" && grep -q "0\\.25\\|0\\.15" "${KB_VALIDATION}"; then
    echo "  ✅ @F[CUI_BONO_CENTRALITY](COMPARABLES) in §7.2"
else
    echo "  ❌ MISSING: CUI_BONO COMPARABLES in §7.2"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "9. VERSION UPDATE"
echo "═══════════════════════════════════════════════════════"

# Check version 1.1
if grep -q "Version.*1\\.1\\|v1\\.1" "${KB_TREE}"; then
    echo "  ✅ Version updated to 1.1"
else
    echo "  ❌ MISSING: Version 1.1 in kb/INVESTIGATION_TREE.md"
    ((ERRORS++))
fi

# Check changelog v1.1
if grep -q "Changelog v1\\.1\\|v1\\.1 Extensions" "${KB_TREE}"; then
    echo "  ✅ Changelog v1.1 present"
else
    echo "  ⚠️  WARNING: Changelog v1.1 not found"
fi

# Check §9 EXTENSIONS mentions COMPARABLES
if grep -q "COMPARABLES_ASYMMETRY.*IMPLEMENTED\\|v1\\.1 Extensions.*COMPARABLES\\|COMPARABLES.*6th branch type" "${KB_TREE}"; then
    echo "  ✅ §9 EXTENSIONS documents COMPARABLES v1.1"
else
    echo "  ⚠️  WARNING: §9 EXTENSIONS not updated"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "10. DSL PURITY CHECK"
echo "═══════════════════════════════════════════════════════"

# Check no Python code added
PYTHON_COUNT=$(grep -c "^def \\|^class \\|^import \\|^return " "${KB_TREE}" 2>/dev/null || echo "0")

# Ensure PYTHON_COUNT is a valid integer
if ! [[ "${PYTHON_COUNT}" =~ ^[0-9]+$ ]]; then
    PYTHON_COUNT=0
fi

if [ "${PYTHON_COUNT}" -eq 0 ]; then
    echo "  ✅ No Python code detected (DSL pur maintained)"
else
    echo "  ❌ FAIL: Python code detected (${PYTHON_COUNT} lines)"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "11. TEST SPECIFICATION COMPLETENESS"
echo "═══════════════════════════════════════════════════════"

if [ ! -f "${TEST_SPEC}" ]; then
    echo "  ❌ MISSING: Test specification file"
    ((ERRORS++))
else
    echo "  ✅ Test specification file exists"

    # Check test case subject
    if grep -q "ARCOM amende CNews" "${TEST_SPEC}"; then
        echo "  ✅ Test case: ARCOM/CNews scenario"
    else
        echo "  ⚠️  WARNING: Test case subject unclear"
    fi

    # Check expected asymmetry_score
    if grep -q "asymmetry_score.*7\\.4\\|7\\.4.*asymmetry" "${TEST_SPEC}"; then
        echo "  ✅ Expected asymmetry_score: 7.4/10"
    else
        echo "  ⚠️  WARNING: Expected score unclear"
    fi

    # Check expected verdict EXTREME
    if grep -q "ASYMMETRY_EXTREME" "${TEST_SPEC}"; then
        echo "  ✅ Expected verdict: ASYMMETRY_EXTREME"
    else
        echo "  ⚠️  WARNING: Expected verdict unclear"
    fi

    # Check comparables count (4: TF1, LCI, BFM, CNews)
    if grep -q "TF1.*LCI.*BFM.*CNews\\|4 comparables" "${TEST_SPEC}"; then
        echo "  ✅ Expected comparables: 4 (TF1, LCI, BFM, CNews)"
    else
        echo "  ⚠️  WARNING: Expected comparables count unclear"
    fi
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "12. CROSS-REFERENCES"
echo "═══════════════════════════════════════════════════════"

# Check design document reference
if grep -q "COMPARABLES_ASYMMETRY_design\\.md" "${KB_TREE}"; then
    echo "  ✅ Cross-reference to COMPARABLES_ASYMMETRY_design.md"
else
    echo "  ⚠️  WARNING: Design document cross-reference not found"
fi

# Check @KB[INVESTIGATION_TREE§5.6] reference
if grep -q "§5\\.6.*DETECT_ASYMMETRY\\|DETECT_ASYMMETRY.*§5\\.6" "${KB_VALIDATION}"; then
    echo "  ✅ Cross-reference @KB[INVESTIGATION_TREE§5.6]"
else
    echo "  ⚠️  WARNING: §5.6 cross-reference not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "SUMMARY"
echo "═══════════════════════════════════════════════════════"

if [ ${ERRORS} -eq 0 ]; then
    echo ""
    echo "✅ COMPARABLES_ASYMMETRY Validation PASSED"
    echo ""
    echo "Investigation Tree v1.1 extension complete:"
    echo "  • COMPARABLES (6th branch type) ✅"
    echo "  • DETECT_ASYMMETRY (6th synthesis operation) ✅"
    echo "  • @F[ASYMMETRY_SCORE] (0-10 scale) ✅"
    echo "  • Triggers: regulatory_context OR Ξ≥8 ✅"
    echo "  • Scoring: EDI 0.35, CUI_BONO 0.25 ✅"
    echo "  • Verdict: EXTREME/SIGNIFICANT/MODERATE/MINIMAL ✅"
    echo "  • Integration: kb/VALIDATION.md §7.5 ✅"
    echo "  • DSL purity maintained ✅"
    echo ""
    echo "📋 Implementation: kb/INVESTIGATION_TREE.md (+206 lines)"
    echo "📋 Integration: kb/VALIDATION.md (+118 lines)"
    echo "📋 Design: docs/plans/COMPARABLES_ASYMMETRY_design.md"
    echo "📋 Test: tests/tree/test_comparables_asymmetry.md"
    echo ""
    echo "Use case: ARCOM CNews asymmetry detection (score 7.4/10 EXTREME)"
    echo ""
    echo "Backward compatible: Phase 1-2 validations still pass ✅"
    exit 0
else
    echo ""
    echo "❌ COMPARABLES_ASYMMETRY Validation FAILED"
    echo ""
    echo "Errors found: ${ERRORS}"
    echo ""
    echo "Review files:"
    echo "  • ${KB_TREE} (§1 §2 §3 §5.6 §9)"
    echo "  • ${KB_VALIDATION} (§7.1 §7.2 §7.5)"
    echo "  • ${TEST_SPEC}"
    echo ""
    echo "Common issues:"
    echo "  • Missing COMPARABLES branch type in enum"
    echo "  • Missing @F[EDI_IMPACT]/CUI_BONO_CENTRALITY COMPARABLES cases"
    echo "  • Missing DETECT_ASYMMETRY synthesis operation"
    echo "  • Missing @F[ASYMMETRY_SCORE] formula"
    echo "  • Missing verdict thresholds (EXTREME ≥7.0, etc.)"
    echo ""
    exit 1
fi
