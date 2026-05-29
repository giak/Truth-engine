#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validation Phase 2 — Multi-Branch Synthesis Operations"
echo ""

# Files to validate
KB_TREE="kb/INVESTIGATION_TREE.md"
TEST_SPEC="tests/tree/test_phase2_multi_branch.md"
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
echo "1. SYNTHÈSE FINALE — §5 Section Present"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "## §5 — SYNTHÈSE FINALE" \
    "Section §5 SYNTHÈSE FINALE exists"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "2. CONCORDANCES — ⊕ Detection"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "DETECT_CONCORDANCES" \
    "DETECT_CONCORDANCES operation defined"

# Check concordances logic (≥2 branches)
if grep -q "count.*≥ 2\|count >= 2" "${KB_TREE}"; then
    echo "  ✅ Concordances threshold (≥2 branches)"
else
    echo "  ❌ MISSING: Concordances threshold ≥2 branches"
    ((ERRORS++))
fi

# Check ⊕ symbol usage
if grep -q "⊕" "${KB_TREE}"; then
    echo "  ✅ ⊕ symbol (confirmed facts)"
else
    echo "  ⚠️  WARNING: ⊕ symbol not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "3. CONTRADICTIONS — ⊗ Detection"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "DETECT_CONTRADICTIONS" \
    "DETECT_CONTRADICTIONS operation defined"

# Check dialectical presentation
if grep -q "dialectique\|Dialectique" "${KB_TREE}"; then
    echo "  ✅ Dialectical presentation referenced"
else
    echo "  ⚠️  WARNING: Dialectical presentation not explicit"
fi

# Check ⊗ symbol usage
if grep -q "⊗" "${KB_TREE}"; then
    echo "  ✅ ⊗ symbol (contradicted facts)"
else
    echo "  ⚠️  WARNING: ⊗ symbol not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "4. GAPS UNRESOLVED — △ Identification"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "IDENTIFY_GAPS_UNRESOLVED" \
    "IDENTIFY_GAPS_UNRESOLVED operation defined"

# Check EXHAUSTED status filter
if grep -q "status = EXHAUSTED" "${KB_TREE}"; then
    echo "  ✅ EXHAUSTED status filtering"
else
    echo "  ❌ MISSING: EXHAUSTED status check"
    ((ERRORS++))
fi

# Check critical gap detection
if grep -q "critical.*GAP_CRITICAL\|GAP_CRITICAL.*critical" "${KB_TREE}"; then
    echo "  ✅ Critical gap classification (GAP_CRITICAL type)"
else
    echo "  ⚠️  WARNING: Critical gap classification unclear"
fi

# Check △ symbol usage
if grep -q "△" "${KB_TREE}"; then
    echo "  ✅ △ symbol (gaps unresolved)"
else
    echo "  ⚠️  WARNING: △ symbol not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "5. EDI GLOBAL — Aggregation Calculation"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "CALCULATE_EDI_GLOBAL" \
    "CALCULATE_EDI_GLOBAL operation defined"

# Check source aggregation
if grep -q "aggregate.*sources\|all_sources" "${KB_TREE}"; then
    echo "  ✅ Source aggregation from all branches"
else
    echo "  ❌ MISSING: Source aggregation logic"
    ((ERRORS++))
fi

# Check EDI improvement calculation
if grep -q "improvement.*edi_i1 - edi_i0\|edi_i1 - edi_i0" "${KB_TREE}"; then
    echo "  ✅ EDI improvement calculation (edi_i1 - edi_i0)"
else
    echo "  ❌ MISSING: EDI improvement formula"
    ((ERRORS++))
fi

# Check target APEX reference (0.80)
if grep -q "target.*0\.80\|0\.80.*target" "${KB_TREE}"; then
    echo "  ✅ EDI target APEX (0.80) referenced"
else
    echo "  ⚠️  WARNING: EDI target 0.80 not explicit"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "6. I2 DECISION — Trigger Logic"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "DECIDE_I2" \
    "DECIDE_I2 operation defined"

# Check critical gaps condition
if grep -q "count.*critical_gaps.*> 0\|critical_gaps.*> 0" "${KB_TREE}"; then
    echo "  ✅ Critical gaps condition (count > 0)"
else
    echo "  ❌ MISSING: Critical gaps > 0 condition"
    ((ERRORS++))
fi

# Check EDI threshold condition
if grep -q "edi.*<.*target\|edi_i1.*<.*0\.80" "${KB_TREE}"; then
    echo "  ✅ EDI < target threshold condition"
else
    echo "  ❌ MISSING: EDI threshold condition"
    ((ERRORS++))
fi

# Check OR logic (critical gaps OR edi insufficient)
if grep -q "OR" "${KB_TREE}"; then
    echo "  ✅ OR logic present (critical gaps OR edi < target)"
else
    echo "  ⚠️  WARNING: OR logic not explicit"
fi

# Check I2 launch vs finalize outcomes
if grep -q "LAUNCH_I2\|launch_i2.*true" "${KB_TREE}" && grep -q "FINALIZE\|finalize.*true" "${KB_TREE}"; then
    echo "  ✅ I2 launch vs finalize outcomes defined"
else
    echo "  ❌ MISSING: I2 launch/finalize outcomes"
    ((ERRORS++))
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "7. FORMATS OUTPUT — §6 Section Present"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "## §6 — FORMATS OUTPUT" \
    "Section §6 FORMATS OUTPUT exists"

echo ""
echo "═══════════════════════════════════════════════════════"
echo "8. MERMAID DIAGRAM — Generation"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "GENERATE_MERMAID" \
    "GENERATE_MERMAID operation defined"

# Check graph TD (Mermaid syntax)
if grep -q "graph TD" "${KB_TREE}"; then
    echo "  ✅ Mermaid graph TD syntax"
else
    echo "  ❌ MISSING: Mermaid graph TD"
    ((ERRORS++))
fi

# Check I0 node generation
if grep -q "I0\[.*EDI\|I0 node" "${KB_TREE}"; then
    echo "  ✅ I0 root node generation"
else
    echo "  ⚠️  WARNING: I0 node generation unclear"
fi

# Check branch nodes loop
if grep -q "FOR branch IN branches" "${KB_TREE}"; then
    echo "  ✅ Branch nodes iteration (FOR loop)"
else
    echo "  ⚠️  WARNING: Branch nodes loop not found"
fi

# Check status icons (✅ ❌)
if grep -q "✅.*❌\|CONVERGED.*EXHAUSTED" "${KB_TREE}"; then
    echo "  ✅ Status icons (✅ CONVERGED, ❌ EXHAUSTED)"
else
    echo "  ⚠️  WARNING: Status icons not referenced"
fi

# Check concordance/contradiction edges
if grep -q "concordance\|contradiction.*edge\|dotted" "${KB_TREE}"; then
    echo "  ✅ Concordance/contradiction edges referenced"
else
    echo "  ⚠️  WARNING: ⊕⊗ edges not explicit"
fi

# Check SYNTH node
if grep -q "SYNTH\|synthesis.*node" "${KB_TREE}"; then
    echo "  ✅ SYNTH synthesis node"
else
    echo "  ⚠️  WARNING: SYNTH node not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "9. JSON STATE — Export Format"
echo "═══════════════════════════════════════════════════════"

check_contains "${KB_TREE}" \
    "GENERATE_JSON_STATE" \
    "GENERATE_JSON_STATE operation defined"

# Check JSON structure keys
JSON_KEYS=(
    "investigation_id"
    "complexity"
    "iterations"
    "synthesis"
    "decision"
)

for key in "${JSON_KEYS[@]}"; do
    if grep -q "${key}" "${KB_TREE}"; then
        echo "  ✅ JSON key: ${key}"
    else
        echo "  ⚠️  WARNING: JSON key '${key}' not found"
    fi
done

# Check branches array in JSON
if grep -q "branches:.*\[" "${KB_TREE}"; then
    echo "  ✅ Branches array in JSON structure"
else
    echo "  ⚠️  WARNING: Branches array unclear"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "10. INTEGRATION VERIFICATION"
echo "═══════════════════════════════════════════════════════"

# Check system.md references synthesis
if grep -q "synthesis\|SYNTHÈSE" "${SYSTEM_MD}"; then
    echo "  ✅ system.md references synthesis operations"
else
    echo "  ⚠️  WARNING: system.md synthesis integration unclear"
fi

# Check system.md references output formats
if grep -q "Mermaid\|JSON.*state" "${SYSTEM_MD}"; then
    echo "  ✅ system.md references Mermaid/JSON outputs"
else
    echo "  ⚠️  WARNING: system.md output formats integration unclear"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "11. TEST CASE COMPLETENESS"
echo "═══════════════════════════════════════════════════════"

# Check test specification exists and is complete
if [ ! -f "${TEST_SPEC}" ]; then
    echo "  ❌ MISSING: Test specification file"
    ((ERRORS++))
else
    echo "  ✅ Test specification file exists"

    # Check test has 4 branches
    if grep -q "Branches:.*4\|4 branches\|4 parallel" "${TEST_SPEC}"; then
        echo "  ✅ Test specifies 4 parallel branches"
    else
        echo "  ⚠️  WARNING: Test branch count unclear"
    fi

    # Check test has expected concordances
    if grep -q "concordances.*3\|3 concordances" "${TEST_SPEC}"; then
        echo "  ✅ Test expects 3 concordances"
    else
        echo "  ⚠️  WARNING: Test concordances expectation unclear"
    fi

    # Check test has expected contradictions
    if grep -q "contradictions.*2\|2 contradictions" "${TEST_SPEC}"; then
        echo "  ✅ Test expects 2 contradictions"
    else
        echo "  ⚠️  WARNING: Test contradictions expectation unclear"
    fi

    # Check test has EDI improvement target
    if grep -q "EDI improvement.*40%\|+0\.14" "${TEST_SPEC}"; then
        echo "  ✅ Test expects EDI improvement +40%"
    else
        echo "  ⚠️  WARNING: Test EDI target unclear"
    fi
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "12. CONVERGENCE METRICS"
echo "═══════════════════════════════════════════════════════"

# Check convergence rate calculation
if grep -q "convergence.*rate\|branches.*converged" "${KB_TREE}"; then
    echo "  ✅ Convergence rate concept referenced"
else
    echo "  ⚠️  WARNING: Convergence rate not explicit"
fi

# Check 60% target referenced
if grep -q "60%.*convergence\|convergence.*60" "${KB_TREE}"; then
    echo "  ✅ Convergence rate target (60%) referenced"
else
    echo "  ⚠️  WARNING: 60% convergence target not found"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "SUMMARY"
echo "═══════════════════════════════════════════════════════"

if [ ${ERRORS} -eq 0 ]; then
    echo ""
    echo "✅ Phase 2 Validation PASSED"
    echo ""
    echo "All synthesis operations are properly specified:"
    echo "  • DETECT_CONCORDANCES (⊕ ≥2 branches)"
    echo "  • DETECT_CONTRADICTIONS (⊗ dialectical)"
    echo "  • IDENTIFY_GAPS_UNRESOLVED (△ EXHAUSTED filter)"
    echo "  • CALCULATE_EDI_GLOBAL (aggregation, improvement)"
    echo "  • DECIDE_I2 (critical gaps OR edi < target)"
    echo "  • GENERATE_MERMAID (graph TD, nodes, edges, ⊕⊗)"
    echo "  • GENERATE_JSON_STATE (complete schema)"
    echo ""
    echo "📋 Test specification: ${TEST_SPEC}"
    echo "📁 Implementation: ${KB_TREE}"
    echo ""
    echo "Test case summary:"
    echo "  • Subject: EU AI Act 2024"
    echo "  • Complexity: 9.5 (APEX)"
    echo "  • Branches: 4 parallel (2 ACTOR_CENTRAL, 2 GAP_CRITICAL)"
    echo "  • Expected: 3 concordances, 2 contradictions, 1 gap"
    echo "  • EDI: 0.35 → 0.49 (+40%)"
    echo "  • Convergence: 75% (3/4 branches)"
    echo ""
    echo "Ready for Phase 3 — Full Integration Testing"
    exit 0
else
    echo ""
    echo "❌ Phase 2 Validation FAILED"
    echo ""
    echo "Errors found: ${ERRORS}"
    echo ""
    echo "Review files:"
    echo "  • ${KB_TREE} (§5 SYNTHÈSE, §6 OUTPUT)"
    echo "  • ${SYSTEM_MD} (INVESTIGATION_TREE section)"
    echo "  • ${TEST_SPEC}"
    echo ""
    echo "Common issues:"
    echo "  • Missing synthesis operations (DETECT_*, CALCULATE_*, DECIDE_*)"
    echo "  • Incomplete logic (threshold conditions, OR clauses)"
    echo "  • Output format specifications (Mermaid, JSON schema)"
    echo ""
    exit 1
fi
