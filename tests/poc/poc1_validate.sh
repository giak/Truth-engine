#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 1..."

# Find latest POC 1 output
LATEST=$(ls -t logs/*_poc1.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 1 output found"
    exit 1
fi

# Check file exists and not empty
if [ ! -s "${LATEST}" ]; then
    echo "❌ Output file empty"
    exit 1
fi

# Check contains "2+2" or "4"
if grep -qi "2.*2\|quatre\|4" "${LATEST}"; then
    echo "✅ POC 1 validation passed"
    echo "📁 Output: ${LATEST}"
    echo ""
    echo "File size: $(wc -l < "${LATEST}") lines"
else
    echo "❌ Output doesn't mention 2+2 or 4"
    exit 1
fi
