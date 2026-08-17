#!/usr/bin/env bash
# worktree-new.sh <chantier> — créer un worktree isolé pour un chantier.
#
# Invariant : 1 chantier = 1 branche = 1 worktree = 1 cycle de vérification.
# Le chantier ne doit PAS être une branche protégée (source de vérité :
# .verify/config.json -> protected_branches).
#
# Usage :
#   tools/verify/worktree-new.sh te-verification-gate
set -euo pipefail

CHANTIER="${1:-}"
if [[ -z "$CHANTIER" ]]; then
  echo "usage: worktree-new.sh <chantier>" >&2
  echo "exemple: worktree-new.sh te-verification-gate" >&2
  exit 2
fi

# Depuis le dépôt principal uniquement (pas depuis un autre worktree).
if [[ "$(git rev-parse --git-dir)" != ".git" ]]; then
  echo "ERREUR: lancer depuis la racine du dépôt principal, pas depuis un worktree." >&2
  exit 2
fi

# Branches protégées : source de vérité = .verify/config.json, sinon défaut.
PROTECTED="main master"
if [[ -f .verify/config.json ]]; then
  PROTECTED=$(python3 -c 'import json;c=json.load(open(".verify/config.json"));print(" ".join(c.get("protected_branches",["main","master"])))' 2>/dev/null || echo "main master")
fi

for b in $PROTECTED; do
  if [[ "$CHANTIER" == "$b" ]]; then
    echo "ERREUR: '$CHANTIER' est une branche protégée ($PROTECTED)." >&2
    exit 2
  fi
done

if ! git check-ref-format "refs/heads/$CHANTIER" >/dev/null 2>&1; then
  echo "ERREUR: '$CHANTIER' n'est pas un nom de branche valide." >&2
  exit 2
fi

if git rev-parse --verify --quiet "refs/heads/$CHANTIER" >/dev/null 2>&1; then
  echo "ERREUR: la branche '$CHANTIER' existe déjà." >&2
  exit 2
fi

git worktree add -b "$CHANTIER" ".worktrees/$CHANTIER"
echo
echo "Worktree créé : .worktrees/$CHANTIER  (branche $CHANTIER, non protégée)"
echo "Suite :"
echo "  cd .worktrees/$CHANTIER"
echo "  python3 tools/verify/verify.py check   # ou spawn truth-verifier"
