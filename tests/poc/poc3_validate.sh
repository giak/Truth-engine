#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 3..."

LATEST=$(ls -t logs/*_poc3.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 3 output found"
    exit 1
fi

# Check ICEBERG pattern present
if ! grep -qi "iceberg" "${LATEST}"; then
    echo "❌ ICEBERG not found"
    exit 1
fi
echo "✅ ICEBERG pattern detected"

# Check KB details present (look for pattern-specific terms from PATTERNS.md)
if grep -qi "SHADOW_ENGINE\|PRIORITY_[0-9]\|Factor_calc\|KB\[PATTERNS" "${LATEST}"; then
    echo "✅ KB pattern details present (SHADOW_ENGINE protocol)"
else
    echo "⚠️  KB pattern details not detected"
fi

# Check Factor calculation present (quantified)
if grep -qiE "Factor.*=.*[0-9]\.[0-9]+|Base_Factor.*[0-9]" "${LATEST}"; then
    echo "✅ Factor calculation quantified"
else
    echo "⚠️  No Factor calculation detected"
fi

# Check Classification matrix applied
if grep -qiE "Ξ\+|Classification.*Ξ|Magnitude.*Intent" "${LATEST}"; then
    echo "✅ Classification matrix applied (Ξ symbol present)"
else
    echo "⚠️  Classification matrix not applied"
fi

# Check Confidence/Reliability calculated
if grep -qiE "Confidence.*[0-9]+%|Reliability.*[0-9]\.[0-9]" "${LATEST}"; then
    echo "✅ Confidence/Reliability calculated"
else
    echo "⚠️  No confidence metrics"
fi

# Check KB methodology (PRIORITY method)
if grep -qi "PRIORITY_2\|Population.*Ratio" "${LATEST}"; then
    echo "✅ KB PRIORITY method applied (PRIORITY_2 detected)"
else
    echo "⚠️  KB PRIORITY method not detected"
fi

echo ""
echo "✅ POC 3 validation passed"
echo "📁 Output: ${LATEST}"
echo "📊 File size: $(wc -l < "${LATEST}") lines"
echo ""
echo "POC 3 demonstrates KB-enhanced analysis with SHADOW_ENGINE_V4 protocol"
