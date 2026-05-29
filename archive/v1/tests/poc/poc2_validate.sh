#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 2..."

LATEST=$(ls -t logs/*_poc2.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 2 output found"
    exit 1
fi

# Check system.md loaded (indirect: file not empty, has substance)
if [ $(wc -l < "${LATEST}") -lt 10 ]; then
    echo "❌ Output too short (<10 lines), system.md may not have been loaded"
    exit 1
fi

# Check ICEBERG concept detected
if grep -qi "iceberg\|caché\|visible.*hidden\|omission" "${LATEST}"; then
    echo "✅ ICEBERG concept detected"
else
    echo "❌ ICEBERG concept not detected in output"
    exit 1
fi

# Check system.md reference
if grep -qi "system\.md\|v7\.17\|truth engine" "${LATEST}"; then
    echo "✅ system.md loaded (referenced in output)"
else
    echo "⚠️  system.md not explicitly referenced"
fi

# Check quantification (ICEBERG should have numbers)
if grep -qE "[0-9]+\.[0-9]+M|[0-9]+%|[0-9]+\.[0-9]+ ?%" "${LATEST}"; then
    echo "✅ Quantification present (ICEBERG with numbers)"
else
    echo "⚠️  No quantification detected"
fi

echo ""
echo "✅ POC 2 validation passed"
echo "📁 Output: ${LATEST}"
echo "📊 File size: $(wc -l < "${LATEST}") lines"
