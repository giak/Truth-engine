#!/usr/bin/env bash
# lint-article.sh — Lint les articles contre les LOIS SUBLIMATOR
#
# Usage:
#   lint-article.sh <article.md> [article.md ...]
#   lint-article.sh articles/*.md
#
# Exit: 0 si tout OK, 1 si violations
#
# Checks:
#   LOI 8 — Aucun ID interne (F###, D###) dans le corps
#   LOI 8 — Aucun [LIEN_A_INSERER] résiduel
#   LOI 3 — H1 commence par un émoji (warning)
#   LOI 4 — Transitions faibles : pas de « Mais »/« Cependant » en début de phrase
#   LOI 5 — Calibration sections (pas de section > 800 mots)
#   LOI 6 — Gras stratégique : 3-5/section
#   LOI 1 — Section Sources présente avec URLs
#
# Changelog:
#   2026-05-29 — v1.0 création
#   2026-05-29 — v1.1 ajout LOI 6 (gras) + LOI 4 (transitions)

set -o pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

PASS=0
FAIL=0
WARN=0

check_name=""
current_file=""

begin_check() {
  check_name="$1"
}

pass() {
  local msg="${1:-}"
  PASS=$((PASS + 1))
  echo -e "  ${GREEN}✅${NC} $check_name${msg:+ — $msg}"
}

fail() {
  local msg="$1"
  FAIL=$((FAIL + 1))
  echo -e "  ${RED}❌${NC} $check_name — $msg"
}

warn() {
  local msg="$1"
  WARN=$((WARN + 1))
  echo -e "  ${YELLOW}⚠️${NC} $check_name — $msg"
}

# ── LOI 3 : H1 commence par un émoji ──────────────────────────
check_loi3_emoji() {
  local file="$1"
  begin_check "LOI 3 : Émoji en H1"

  local h1
  h1=$(grep -m1 '^# ' "$file" 2>/dev/null || echo "")
  if [ -z "$h1" ]; then
    warn "Pas de H1 trouvé"
    return
  fi

  # Extract first char after "# " — should be an emoji
  local h1_text
  h1_text=$(echo "$h1" | sed 's/^# //')

  # Use Python for reliable Unicode emoji detection
  if python3 -c "
import sys
h = sys.argv[1] if len(sys.argv) > 1 else ''
if not h:
    sys.exit(2)
cp = ord(h[0])
# Emoticons, Misc Symbols, Dingbats, Enclosed, Transport, etc.
if (0x1F000 <= cp <= 0x1FFFF) or (0x2600 <= cp <= 0x27BF) or (0x2300 <= cp <= 0x23FF) or (0x2700 <= cp <= 0x27BF) or (0xFE00 <= cp <= 0xFE0F):
    sys.exit(0)
else:
    sys.exit(1)
" "$h1_text" 2>/dev/null; then
    pass
  else
    # Check if python3 is available — if not, do basic check
    local first_bytes
    first_bytes=$(echo "$h1_text" | head -c 2 | xxd -p 2>/dev/null || echo "")
    # Common emoji byte prefixes: f0 9f (1F...), e2 9c/e2 9d (checkmark/heart), e2 99/e2 98
    if [ -n "$first_bytes" ] && echo "$first_bytes" | grep -qE '^(f09f|e29c|e29d|e299|e298|e28f|e29a|e296|e297|e280|e281|e282|e283|e284|e285|e286|e287|e288|e289|e28a|e28b|e2ad)'; then
      pass
    else
      warn "H1 ne commence pas par un émoji confirmé : « ${h1:0:50}… »"
    fi
  fi
}

# ── LOI 8 : Aucun ID interne F### ou D### dans le texte ───────
check_loi8_ids() {
  local file="$1"
  begin_check "LOI 8 : Aucun ID factice (F###, D###) dans le texte"

  local tmpfile
  tmpfile=$(mktemp)

  # Strip code blocks with awk, then search remaining lines for F###/D###
  # (awk tracks code block state across lines; grep then filters URLs, comments, etc.)
  awk 'BEGIN{c=0} /^```/{c=1-c;next} c{next} 1' "$file" | \
    grep -nP '\b(F|D)[0-9]{2,3}\b' | \
    grep -viP '(https?://|\[.*\]\(https?://|<!--|^    )' > "$tmpfile" || true

  if [ -s "$tmpfile" ]; then
    local violations
    violations=$(cat "$tmpfile")
    fail "IDs factices trouves :
$violations"
  else
    pass
  fi

  rm -f "$tmpfile"
}

# ── LOI 8 : Aucun [LIEN_A_INSERER] résiduel ──────────────────
check_loi8_lien() {
  local file="$1"
  begin_check "LOI 8 : Aucun [LIEN_A_INSERER] résiduel"

  local count
  count=$(grep -c '\[LIEN_A_INSERER\]' "$file" 2>/dev/null || true)
  count=${count:-0}

  if [ "$count" -gt 0 ] 2>/dev/null; then
    local lines
    lines=$(grep -n '\[LIEN_A_INSERER\]' "$file" | head -5)
    fail "$count occurences (montre max 5) :
$lines"
  else
    pass
  fi
}

# ── LOI 5 : Calibration sections ──────────────────────────────
check_loi5_calibration() {
  local file="$1"
  begin_check "LOI 5 : Calibration sections (max 800 mots/section)"

  # Use awk for reliable section word counting — avoids bash subshell/local issues
  local result
  result=$(awk '
    BEGIN { violations = 0; section = "(avant première section)"; words = 0; limit = 800; }
    /^## / {
      if (words > limit) {
        printf "      Section « %s » : %d mots (> %d)\n", section, words, limit;
        violations++;
      }
      section = substr($0, 4);
      if (length(section) > 60) section = substr(section, 1, 60);
      words = 0;
      next;
    }
    /^```/ || /^<!--/ || /^-->/ || /^$/ { next; }
    { words += NF; }
    END {
      if (words > limit) {
        printf "      Section « %s » : %d mots (> %d)\n", section, words, limit;
        violations++;
      }
      print "VIOLATIONS=" violations;
    }
  ' "$file")

  local vcount
  vcount=$(printf '%s\n' "$result" | grep '^VIOLATIONS=' | sed 's/^VIOLATIONS=//' | tr -d '[:space:]')
  vcount=${vcount:-0}

  # Print section warnings
  printf '%s\n' "$result" | grep -v '^VIOLATIONS=' || true

  if [ "$vcount" -gt 0 ] 2>/dev/null; then
    fail "$vcount section(s) dépassent $limit mots"
  else
    pass
  fi
}

# ── LOI 6 : Gras stratégique (3-5/section) ──────────────────────
check_loi6_gras() {
  local file="$1"
  begin_check "LOI 6 : Gras stratégique — 3-5/section"

  local result
  result=$(awk '
    BEGIN {
      violations = 0;
      section = "";
      bold_count = 0;
      limit_low = 3; limit_high = 5;
      in_code = 0;
      in_sources = 0;
      started = 0;
    }
    /^```/ { in_code = 1 - in_code; next }
    in_code { next }
    /^## / {
      if (in_sources) {
        in_sources = 0;
        next;
      }
      # Verifier section precedente seulement si on a commence
      if (started && (bold_count < limit_low || bold_count > limit_high)) {
        printf "      Section « %s » : %d gras (attendu: %d-%d)\n", section, bold_count, limit_low, limit_high;
        violations++;
      }
      section = substr($0, 4);
      if (length(section) > 60) section = substr(section, 1, 60);
      if (tolower(section) ~ /^sources/) {
        in_sources = 1;
        next;
      }
      started = 1;
      bold_count = 0;
      next;
    }
    in_sources { next }
    {
      line = $0;
      count = 0;
      while (match(line, /\*\*[^*]+\*\*/)) {
        count++;
        line = substr(line, RSTART + RLENGTH);
      }
      bold_count += count;
    }
    END {
      if (started && !in_sources && (bold_count < limit_low || bold_count > limit_high)) {
        printf "      Section « %s » : %d gras (attendu: %d-%d)\n", section, bold_count, limit_low, limit_high;
        violations++;
      }
      print "VIOLATIONS=" violations;
    }
  ' "$file")

  local vcount
  vcount=$(printf '%s\n' "$result" | grep '^VIOLATIONS=' | sed 's/^VIOLATIONS=//' | tr -d '[:space:]')
  vcount=${vcount:-0}

  printf '%s\n' "$result" | grep -v '^VIOLATIONS=' || true

  if [ "$vcount" -gt 0 ] 2>/dev/null; then
    fail "$vcount section(s) hors limites (attendu: 3-5 gras/section)"
  else
    pass
  fi
}

# ── LOI 4 : Transitions faibles « Mais »/« Cependant » ────────
check_loi4_transitions() {
  local file="$1"
  begin_check "LOI 4 : Transitions faibles — « Mais »/« Cependant »"

  # Extraire le corps (hors blocs de code) avec awk
  local body
  body=$(awk 'BEGIN{in_code=0} /^```/{in_code=1-in_code;next} in_code{next} 1' "$file")

  # Compter les occurrences en debut de phrase : debut de ligne, ou apres . ! ?
  local count
  count=$(printf '%s\n' "$body" | grep -cP '(^|[.!?]\s+)(Mais|Cependant)\b' || true)
  count=${count:-0}

  if [ "$count" -gt 3 ] 2>/dev/null; then
    local lines
    lines=$(printf '%s\n' "$body" | grep -nP '(^|[.!?]\s+)(Mais|Cependant)\b' | head -10)
    fail "$count occurrences comme transition faibles (§3.3 interdit) :\n$lines"
  elif [ "$count" -gt 0 ] 2>/dev/null; then
    warn "$count occurrences detectees"
  else
    pass
  fi
}

# ── LOI 1 : Sources présentes avec URLs ──────────────────────
check_loi1_sources() {
  local file="$1"
  begin_check "LOI 1 : Section Sources avec URLs"

  # Chercher ## Sources
  if grep -qP '^##\s+Sources' "$file" 2>/dev/null; then
    # Compter les URLs dans la section Sources
    local in_sources=0
    local url_count=0

    while IFS= read -r line; do
      if echo "$line" | grep -qP '^##\s+Sources'; then
        in_sources=1
        continue
      fi
      if [ "$in_sources" -eq 1 ]; then
        # Fin de section si nouvelle H1/H2
        if echo "$line" | grep -qP '^#{1,2}\s'; then
          break
        fi
        if echo "$line" | grep -qP 'https?://'; then
          url_count=$((url_count + 1))
        fi
      fi
    done < "$file"

    if [ "$url_count" -eq 0 ]; then
      fail "Section Sources trouvée mais aucune URL"
    else
      pass "($url_count URLs)"
    fi
  else
    fail "Section « ## Sources » non trouvée"
  fi
}

# ── Main ──────────────────────────────────────────────────────
main() {
  local files=("$@")

  if [ ${#files[@]} -eq 0 ]; then
    echo "Usage: lint-article.sh <article.md> [article.md ...]"
    echo "       lint-article.sh articles/*.md"
    exit 1
  fi

  local global_fail=0
  local global_warn=0

  for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
      echo -e "${RED}Erreur : fichier introuvable : $file${NC}"
      global_fail=1
      continue
    fi

    # Skip non-markdown et templates
    if [[ ! "$file" =~ \.md$ ]]; then
      continue
    fi
    if [[ "$file" == *"PROMPT_"* ]]; then
      echo -e "\n${YELLOW}⏭️  $file — template ignoré${NC}"
      continue
    fi

    echo -e "\n${BOLD}━━━ $file ━━━${NC}"
    PASS=0
    FAIL=0
    WARN=0

    check_loi3_emoji "$file"
    check_loi4_transitions "$file"
    check_loi5_calibration "$file"
    check_loi6_gras "$file"
    check_loi8_ids "$file"
    check_loi8_lien "$file"
    check_loi1_sources "$file"

    echo -e "\n  ${BOLD}Résumé :${NC} ${GREEN}$PASS OK${NC} / ${RED}$FAIL violations${NC} / ${YELLOW}$WARN warnings${NC}"

    if [ "$FAIL" -gt 0 ]; then
      global_fail=1
    fi
    if [ "$WARN" -gt 0 ]; then
      global_warn=1
    fi
  done

  # Bilan global
  echo ""
  if [ "$global_fail" -gt 0 ]; then
    echo -e "${RED}❌ VIOLATIONS DÉTECTÉES — corriger avant CP#5${NC}"
    exit 1
  elif [ "$global_warn" -gt 0 ]; then
    echo -e "${YELLOW}⚠️  OK avec warnings — vérifier manuellement${NC}"
    exit 0
  else
    echo -e "${GREEN}✅ TOUT OK${NC}"
    exit 0
  fi
}

main "$@"
