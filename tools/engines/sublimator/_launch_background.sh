#!/usr/bin/env bash
# Lance l'import Mnemolite en arriere-plan.
# Usage: bash _launch_background.sh
#
# Le script Python:
#   - Reprend automatiquement la ou il s'etait arrete (progress file)
#   - Envoie un email a christophe.giacomel@proton.me a la fin

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/_bulk_save_investigations.py"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
STDOUT_LOG="$SCRIPT_DIR/_import_stdout_${TIMESTAMP}.log"
STDERR_LOG="$SCRIPT_DIR/_import_stderr_${TIMESTAMP}.log"
PID_FILE="$SCRIPT_DIR/_import_pid.txt"

echo "============================================"
echo "Lancement import Mnemolite en arriere-plan"
echo "============================================"
echo ""
echo "Script    : $PY_SCRIPT"
echo "Stdout    : $STDOUT_LOG"
echo "Stderr    : $STDERR_LOG"
echo "PID file  : $PID_FILE"
echo "Email     : christophe.giacomel@proton.me (a la fin)"
echo ""

# Verifier que Mnemolite est UP
if curl -s 'http://localhost:8001/health' > /dev/null 2>&1; then
    echo "✅ Mnemolite UP"
else
    echo "❌ Mnemolite DOWN — abort"
    exit 1
fi

# Verifier que le script Python existe
if [ ! -f "$PY_SCRIPT" ]; then
    echo "❌ Script introuvable: $PY_SCRIPT"
    exit 1
fi

# Lancer en arriere-plan (passe les chemins de log au script Python pour l'email)
nohup env IMPORT_STDOUT_LOG="$STDOUT_LOG" IMPORT_STDERR_LOG="$STDERR_LOG" python3 "$PY_SCRIPT" > "$STDOUT_LOG" 2> "$STDERR_LOG" &
PID=$!
echo "$PID" > "$PID_FILE"

echo "✅ Lance — PID: $PID"
echo ""
echo "Surveiller la progression :"
echo "  tail -f $STDOUT_LOG"
echo ""
echo "Verifier que ca tourne :"
echo "  ps -p $PID"
echo ""
echo "Statut actuel (progress file) :"
python3 -c "
import json, sys
try:
    with open(sys.argv[1]) as f:
        p = json.load(f)
    print(f'  Deja importes : {len(p.get(\"imported\", []))}')
    print(f'  Echecs        : {len(p.get(\"failed\", []))}')
except:
    print('  Pas encore de progress file')
" "$SCRIPT_DIR/_import_progress.json"
echo ""
echo "Pour tuer le processus :"
echo "  kill $PID"
