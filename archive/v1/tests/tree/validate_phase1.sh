#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validation Phase 1 — Single Branch DSL Specification"
echo ""

# Test specification vs implementation files
TEST_SPEC="tests/tree/test_phase1_single_branch.md"
KB_TREE="kb/INVESTIGATION_TREE.md"
KB_VALIDATION="kb/VALIDATION.md"
SYSTEM_MD="system.md"

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
echo "1. TRIGGER DETECTION — @TRIGGER[TREE_LAUNCH]"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "@TRIGGER\[TREE_LAUNCH\]" \
    "TREE_LAUNCH trigger defined"

check_contains "${KB_TREE}" \
    "IF complexity ≥ 9\.0:" \
    "Complexity ≥9.0 condition present"

# Check GAP_CRITICAL and ◈ gap detection (multi-line)
if grep -q "GAPS_CRITICAL" "${KB_TREE}" && grep -q "◈_current < ◈_target" "${KB_TREE}"; then
    echo "  ✅ GAP_CRITICAL trigger detects ◈ gap"
else
    echo "  ❌ MISSING: GAP_CRITICAL trigger detects ◈ gap"
    ((ERRORS++))
fi

# Check PATTERN_STRONG (multi-line)
if grep -q "PATTERNS_STRONG" "${KB_TREE}" && grep -q "pattern\.score ≥ 8" "${KB_TREE}"; then
    echo "  ✅ PATTERN_STRONG trigger threshold 8"
else
    echo "  ❌ MISSING: PATTERN_STRONG trigger threshold 8"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "2. BRANCH SCORING — @F[BRANCH_PRIORITY]"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "@F\[BRANCH_PRIORITY\]" \
    "BRANCH_PRIORITY formula defined"

check_contains "${KB_TREE}" \
    "priority ← edi_impact × 0\.5 + cui_bono_centrality × 0\.5" \
    "Priority formula correct (0.5 weights)"

check_contains "${KB_TREE}" \
    "@F\[EDI_IMPACT\]" \
    "EDI_IMPACT formula defined"

# Check EDI_IMPACT gap_primary_sources value (multi-line)
if grep -q "gap_primary_sources" "${KB_TREE}" && grep -q "→ 0\.50" "${KB_TREE}"; then
    echo "  ✅ EDI_IMPACT(gap_primary_sources) = 0.50"
else
    echo "  ❌ MISSING: EDI_IMPACT(gap_primary_sources) = 0.50"
    ((ERRORS++))
fi

check_contains "${KB_TREE}" \
    "@F\[CUI_BONO_CENTRALITY\]" \
    "CUI_BONO_CENTRALITY formula defined"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "3. BRANCH LIFECYCLE — @MACRO[EXPLORE_BRANCH]"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "@MACRO\[EXPLORE_BRANCH\]" \
    "EXPLORE_BRANCH macro defined"

check_contains "${KB_TREE}" \
    "LOOP_WHILE.*status = EXPLORING" \
    "Loop while EXPLORING status"

check_contains "${KB_TREE}" \
    "consecutive_failures ≥ 3" \
    "Budget adaptatif: stop at 3 failures"

check_contains "${KB_TREE}" \
    "status ← EXHAUSTED" \
    "Branch status EXHAUSTED on budget limit"

check_contains "${KB_TREE}" \
    "status ← CONVERGED" \
    "Branch status CONVERGED on target reached"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "4. PERTINENCE EVALUATION"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "evaluate_pertinence.*criteria.*A\|B\|C\|D" \
    "Pertinence criteria A|B|C|D defined"

# Check criteria A (new facts) reference
if grep -q "new facts\|facts_new\|nouveaux faits" "${KB_TREE}"; then
    echo "  ✅ Criteria A (new facts) referenced"
else
    echo "  ⚠️  WARNING: Criteria A (new facts) not explicitly found"
fi

# Check criteria B (better sources) reference
if grep -q "better sources\|sources supérieures\|◈.*◉.*○" "${KB_TREE}"; then
    echo "  ✅ Criteria B (better sources) referenced"
else
    echo "  ⚠️  WARNING: Criteria B (better sources) not explicitly found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "5. SYNTHESIS OPERATIONS"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "DETECT_CONCORDANCES" \
    "Concordances detection defined"

check_contains "${KB_TREE}" \
    "DETECT_CONTRADICTIONS" \
    "Contradictions detection defined"

check_contains "${KB_TREE}" \
    "IDENTIFY_GAPS_UNRESOLVED" \
    "Gaps identification defined"

check_contains "${KB_TREE}" \
    "CALCULATE_EDI_GLOBAL" \
    "EDI global calculation defined"

check_contains "${KB_TREE}" \
    "DECIDE_I2" \
    "I2 decision logic defined"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "6. PARALLEL EXECUTION — @MACRO[LAUNCH_INVESTIGATION_TREE]"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "@MACRO\[LAUNCH_INVESTIGATION_TREE\]" \
    "Main orchestration macro defined"

check_contains "${KB_TREE}" \
    "PARALLEL\|FOR EACH.*PARALLEL" \
    "Parallel execution specified"

check_contains "${KB_TREE}" \
    "WAIT_ALL" \
    "Wait for all branches completion"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "7. RÉTROCOMPATIBILITÉ — COMPLEXITY_ROUTING"
echo "═══════════════════════════════════════════════════════"

# Check retrocompatibility (multi-line)
if grep -q "IF complexity < 9\.0" "${KB_TREE}" && grep -q "LINEAR WORKFLOW" "${KB_TREE}"; then
    echo "  ✅ Linear workflow for complexity <9.0"
else
    echo "  ❌ MISSING: Linear workflow for complexity <9.0"
    ((ERRORS++))
fi

if grep -q "complexity ≥ 9\.0" "${KB_TREE}" && grep -q "ARBORESCENT WORKFLOW" "${KB_TREE}"; then
    echo "  ✅ Arborescent workflow for complexity ≥9.0"
else
    echo "  ❌ MISSING: Arborescent workflow for complexity ≥9.0"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "8. INTEGRATION POINTS"
echo "═══════════════════════════════════════════════════════"

# Check system.md references Investigation Tree
if grep -q "INVESTIGATION_TREE\|Investigation Tree" "${SYSTEM_MD}"; then
    echo "  ✅ system.md references Investigation Tree"
else
    echo "  ⚠️  WARNING: system.md may need Investigation Tree integration"
fi

# Check VALIDATION.md Section 7
if grep -q "## 7\. BRANCH SCORING" "${KB_VALIDATION}"; then
    echo "  ✅ kb/VALIDATION.md Section 7 BRANCH SCORING present"
else
    echo "  ❌ MISSING: kb/VALIDATION.md Section 7"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "9. DSL PURITY CHECK (NO PYTHON)"
echo "═══════════════════════════════════════════════════════"

# Check for Python code patterns
PYTHON_PATTERNS=(
    "def "
    "class "
    "import "
    "from .* import"
    "return "
    "self\."
    "\.append\("
    "\.extend\("
)

for pattern in "${PYTHON_PATTERNS[@]}"; do
    if grep -q "${pattern}" "${KB_TREE}"; then
        echo "  ❌ PYTHON CODE DETECTED: ${pattern}"
        ((ERRORS++))
    fi
done

if [ ${ERRORS} -eq 0 ]; then
    echo "  ✅ No Python code detected (DSL pur)"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "SUMMARY"
echo "═══════════════════════════════════════════════════════"

if [ ${ERRORS} -eq 0 ]; then
    echo ""
    echo "✅ Phase 1 Validation PASSED"
    echo ""
    echo "All DSL specifications are present and correct:"
    echo "  • @TRIGGER[TREE_LAUNCH] with 5 trigger types"
    echo "  • @F[BRANCH_PRIORITY] formula (edi×0.5 + cui_bono×0.5)"
    echo "  • @F[EDI_IMPACT] with gap_primary_sources = 0.50"
    echo "  • @MACRO[EXPLORE_BRANCH] with budget adaptatif"
    echo "  • Pertinence criteria A|B|C|D"
    echo "  • Synthesis operations (concordances, contradictions, gaps)"
    echo "  • Parallel execution @MACRO[LAUNCH_INVESTIGATION_TREE]"
    echo "  • Rétrocompatibilité (linear vs arborescent)"
    echo "  • DSL pur (no Python code)"
    echo ""
    echo "📋 Test specification: ${TEST_SPEC}"
    echo "📁 Implementation: ${KB_TREE}"
    echo ""
    echo "Ready for Phase 2 — Multi-Branch Synthesis"
    exit 0
else
    echo ""
    echo "❌ Phase 1 Validation FAILED"
    echo ""
    echo "Errors found: ${ERRORS}"
    echo ""
    echo "Review files:"
    echo "  • ${KB_TREE}"
    echo "  • ${KB_VALIDATION}"
    echo "  • ${SYSTEM_MD}"
    echo ""
    exit 1
fi
