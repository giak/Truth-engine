#!/bin/bash
# sync-mnemolite.sh — Indexe tous les fichiers Truth Engine dans MnemoLite
# Usage: ./tools/scripts/sync-mnemolite.sh
# Prérequis: mnemo CLI dans le PATH, MnemoLite UP sur localhost:8001

set -euo pipefail

API="http://localhost:8001"

# Vérifier que MnemoLite est UP
if ! curl -s --connect-timeout 3 -o /dev/null "$API/readiness"; then
    echo "❌ MnemoLite injoignable sur $API"
    exit 1
fi

echo "📡 MnemoLite UP"

# Indexer tous les articles (.md)
echo "📄 Articles..."
for f in articles/*.md; do
    [ -f "$f" ] || continue
    title="$(basename "$f" .md)"
    echo "   → $title"
    mnemo write --title "$title" --content "$(cat "$f")" --type "article" 2>&1 | head -1
done

# Indexer toutes les investigations (.md)
echo "🔍 Investigations..."
for f in investigations/**/*.md; do
    [ -f "$f" ] || continue
    title="$(basename "$f" .md)"
    echo "   → $title"
    mnemo write --title "$title" --content "$(cat "$f")" --type "investigation" 2>&1 | head -1
done

# Indexer toutes les quintessences (.yaml)
echo "📊 Quintessences..."
for f in investigations/**/_quintessence/*.yaml; do
    [ -f "$f" ] || continue
    civ="$(basename "$(dirname "$(dirname "$f")")")"
    title="$(basename "$f" .yaml)"
    echo "   → $civ/$title"
    mnemo write --title "$civ/$title" --content "$(cat "$f")" --type "quintessence" 2>&1 | head -1
done

echo "✅ Sync terminé"
