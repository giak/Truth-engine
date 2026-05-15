#!/usr/bin/env bash
# char-tool.sh — Character counting and safe truncation for tweets
# Usage:
#   char-tool.sh count "text here"           → print char count
#   char-tool.sh validate "text here"        → print count + PASS/FAIL (280 limit)
#   char-tool.sh truncate "text here"        → truncate to 275 chars at last space + "…"
#   char-tool.sh batch file.txt              → validate each non-empty line
#   char-tool.sh generate "text here"        → validate, if fail auto-truncate + show both

LIMIT=280
SAFE=275  # truncate at 275 to leave room for "…"

cmd="${1:-count}"
shift

case "$cmd" in
  count)
    text="$*"
    # Use printf to avoid echo issues with special chars
    chars=$(printf '%s' "$text" | wc -m | tr -d ' ')
    echo "$chars"
    ;;

  validate)
    text="$*"
    chars=$(printf '%s' "$text" | wc -m | tr -d ' ')
    if [ "$chars" -le "$LIMIT" ]; then
      echo "${chars}/${LIMIT} ✅ PASS"
    else
      echo "${chars}/${LIMIT} ❌ FAIL (+$((chars - LIMIT)) chars over)"
    fi
    ;;

  truncate)
    text="$*"
    chars=$(printf '%s' "$text" | wc -m | tr -d ' ')
    if [ "$chars" -le "$LIMIT" ]; then
      echo "$text"
    else
      # Cut at SAFE chars, find last space before cut point, add "…"
      truncated=$(printf '%s' "$text" | cut -c1-"$SAFE")
      # Find last space in truncated
      last_space=$(echo "$truncated" | grep -bo ' ' | tail -1 | cut -d: -f1)
      if [ -n "$last_space" ] && [ "$last_space" -gt 50 ]; then
        result=$(printf '%s' "$text" | cut -c1-"$last_space")
      else
        result="$truncated"
      fi
      echo "${result}…"
    fi
    ;;

  batch)
    file="$1"
    if [ ! -f "$file" ]; then
      echo "ERROR: File not found: $file"
      exit 1
    fi
    line_num=0
    while IFS= read -r line; do
      line_num=$((line_num + 1))
      [ -z "$line" ] && continue
      chars=$(printf '%s' "$line" | wc -m | tr -d ' ')
      if [ "$chars" -le "$LIMIT" ]; then
        echo "L${line_num}: ${chars}/${LIMIT} ✅"
      else
        echo "L${line_num}: ${chars}/${LIMIT} ❌ (+$((chars - LIMIT)))"
      fi
    done < "$file"
    ;;

  generate)
    text="$*"
    chars=$(printf '%s' "$text" | wc -m | tr -d ' ')
    if [ "$chars" -le "$LIMIT" ]; then
      echo "ORIGINAL (${chars} chars):"
      echo "$text"
    else
      echo "ORIGINAL (${chars} chars — TOO LONG):"
      echo "$text"
      echo ""
      echo "TRUNCATED:"
      truncated=$(printf '%s' "$text" | cut -c1-"$SAFE")
      last_space=$(echo "$truncated" | grep -bo ' ' | tail -1 | cut -d: -f1)
      if [ -n "$last_space" ] && [ "$last_space" -gt 50 ]; then
        result=$(printf '%s' "$text" | cut -c1-"$last_space")
      else
        result="$truncated"
      fi
      echo "${result}…"
      final_chars=$(printf '%s%s' "$result" "…" | wc -m | tr -d ' ')
      echo "(${final_chars} chars)"
    fi
    ;;

  *)
    echo "Usage: char-tool.sh {count|validate|truncate|batch|generate} text"
    exit 1
    ;;
esac
