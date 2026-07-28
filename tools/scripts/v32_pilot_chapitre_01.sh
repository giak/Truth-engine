#!/usr/bin/env bash
# v32_pilot_chapitre_01.sh — Pilote V3.2 circuit-breaker sur chapitre 01.
# Materiau: /tmp/v30_facts_full.txt (66 items IT Etat francais, valide V3.1).
# Stoppe AVANT §2.5 Biblio (phi4-mini absent runtime, voir spec §6 fin Data-Drift).
# Cf spec §4 Boucles d'echec V3.2 Patch 2 (PRIORITAIRE sur V3.0 prose).

set -euo pipefail

CHAP_ID="01"
CHAP_TITLE="Oligopole ESN IT Etat francais"
MAT_FACTS="/tmp/v30_facts_full.txt"
THESE="/tmp/v32_pilot_these.txt"
GATE="/home/giak/projects/truth-engine/tools/scripts/adversarial_gate_v4.sh"
COUNTER="/home/giak/projects/truth-engine/book/_catalogue/state/fail_hard_${CHAP_ID}.json"
GATES="/home/giak/projects/truth-engine/book/gates"
LOG="/tmp/v32_pilot_run.log"

mkdir -p "$(dirname "$COUNTER")" "$GATES"

# These (parametres fichier, pas string, cf adversarial_gate_v4.sh spec)
cat > "$THESE" << 'THESE_EOF'
Le systeme IT de l'Etat francais est capte par un oligopole d'ESN privees
(Capgemini, Sopra Steria, Atos, Accenture) sur les marches strategiques.
THESE_EOF

# Init/reset compteur (etape V3.2 step 1 : validation JSON stricte)
if [ ! -f "$COUNTER" ] || ! python3 -c "import json; d=json.load(open('$COUNTER')); assert isinstance(d.get('count'),int); assert d.get('status') in {'RUNNING','PASS','BLOQUE'}" 2>/dev/null; then
  if [ -f "$COUNTER" ]; then
    echo "[$(date -Iseconds)] WARN: compteur corrompu, reset" >> "$LOG"
  fi
  python3 - << 'PYEOF'
import json
from datetime import datetime, timezone
data = {
  "chap_id": "01",
  "chap_title": "Oligopole ESN IT Etat francais (pilote V3.2)",
  "count": 0,
  "history": [],
  "first_fail_at": None,
  "last_attempt_at": None,
  "status": "RUNNING"
}
with open("/home/giak/projects/truth-engine/book/_catalogue/state/fail_hard_01.json", "w") as f:
  json.dump(data, f, indent=2, ensure_ascii=False)
PYEOF
  echo "[$(date -Iseconds)] Compteur initialise" >> "$LOG"
fi

echo "[$(date -Iseconds)] === PILOTE V3.2 CHAPITRE 01 START ===" | tee -a "$LOG"

MAX_ITER=3
for i in $(seq 1 $MAX_ITER); do
  echo "" | tee -a "$LOG"
  echo "=== ITERATION $i/$MAX_ITER ===" | tee -a "$LOG"

  OUT_MD="${GATES}/adversarial-pilote-iter${i}.md"
  echo "[$(date -Iseconds)] Appel adversarial_gate_v4.sh iter=$i" >> "$LOG"

  set +e
  bash "$GATE" "$MAT_FACTS" "$THESE" 6 "$OUT_MD" 2>>"$LOG"
  EXIT_CODE=$?
  set -e

  echo "[$(date -Iseconds)] Exit code adversarial: $EXIT_CODE" >> "$LOG"

  # Parse : compte verdict et total FAIL_HARD cette iteration
  JSON_VALID=$(grep -c '### Batch.*JSON VALID' "$OUT_MD" || echo 0)
  VERDICT_FAIL_HARD=$(grep -c '### Batch.*verdict=FAIL_HARD' "$OUT_MD" || echo 0)
  VERDICT_PASS=$(grep -c '### Batch.*verdict=PASS' "$OUT_MD" || echo 0)
  echo "  JSON_VALIDE=$JSON_VALID  FAIL_HARD=$VERDICT_FAIL_HARD  PASS=$VERDICT_PASS" | tee -a "$LOG"

  # Precompute verdict en bash (évite ternaire Python fragile post-bash substitution)
  if [ "$VERDICT_FAIL_HARD" -gt 0 ]; then
    VERDICT_GLOBAL="FAIL_HARD"
  elif [ "$VERDICT_PASS" -gt 0 ]; then
    VERDICT_GLOBAL="PASS"
  else
    VERDICT_GLOBAL="UNKNOWN"
  fi
  echo "  VERDICT_GLOBAL=$VERDICT_GLOBAL" | tee -a "$LOG"

  # Update compteur
  python3 - << PYEOF
import json
from datetime import datetime, timezone
counter_path = "$COUNTER"
out_md_path   = "$OUT_MD"
iteration     = $i

with open(counter_path) as f:
    counter = json.load(f)

if counter.get("status") == "BLOQUE":
    print("BLOQUE deja, skip")
    import sys; sys.exit(0)

now = datetime.now(timezone.utc).isoformat()

# Lit les vulnérabilités de cette iteration (depuis le rapport adversarial)
import re
vulns = []
try:
    with open(out_md_path) as g:
        for m in re.finditer(r'\{"id":\s*"([^"]+)",\s*"type":\s*"([^"]+)"', g.read()):
            vulns.append({"id": m.group(1), "type": m.group(2)})
except Exception as e:
    print(f"warn lecture vulns: {e}")

verdict_global = "$VERDICT_GLOBAL"

if verdict_global == "PASS":
    counter["count"] = 0
    counter["status"] = "PASS"
    counter["history"].append({
        "attempt": iteration,
        "verdict": "PASS",
        "vulns_count": 0,
        "vulns_ids": [],
        "at": now
    })
    counter["last_attempt_at"] = now
    with open(counter_path, "w") as f:
        json.dump(counter, f, indent=2, ensure_ascii=False)
    print("verdict=PASS -> count=0, status=PASS, FIN")
    import sys; sys.exit(0)

# FAIL_HARD ou UNKNOWN -> increment count
counter["count"] += 1
counter["last_attempt_at"] = now
if counter["first_fail_at"] is None:
    counter["first_fail_at"] = now

counter["history"].append({
    "attempt": counter["count"],
    "verdict": verdict_global,
    "vulns_count": len(vulns),
    "vulns_ids": [v["id"] for v in vulns],
    "at": now
})

if counter["count"] >= 3 and verdict_global == "FAIL_HARD":
    # === ESCALADE (V3.2 Patch 2) ===
    import os
    counter["status"] = "BLOQUE"
    with open(counter_path, "w") as f:
        json.dump(counter, f, indent=2, ensure_ascii=False)

    escalade = "${GATES}/escalade-chapitre-${CHAP_ID}.md"
    os.makedirs(os.path.dirname(escalade), exist_ok=True)
    with open(escalade, "w") as f:
        f.write(f"""# ESCALADE -- Chapitre ${CHAP_ID} -- {now}

## 1. Contexte
- Chapitre ID : ${CHAP_ID} -- ${CHAP_TITLE}
- Compteur fail_hard : {counter['count']}/3 (BLOQUE)
- Modele extraction : gemma2-9b-opt
- Modele adversarial : qwen25-coder-7b-opt
- Tentatives : 3

## 2. Cause probable
<!-- Hote analyse : les vulnerabilites detectees sont-elles identiques sur les 3 tentatives ?
     Si oui boucle non-convergente. Pattern? A documenter manuellement. -->

## 3. Rapports adversariaux (3 derniers)
""")
        for hist in counter["history"][-3:]:
            f.write(f"### Tentative {hist['attempt']} ({hist['at']})\n")
            f.write(f"- verdict={hist['verdict']}\n")
            f.write(f"- vulns_count={hist['vulns_count']}\n")
            f.write(f"- vulns_ids={hist['vulns_ids']}\n\n")

        f.write("""## 4. Action humaine requise
- [ ] Inspecter book/_catalogue/faits.md section chapitre XX
- [ ] Inspecter materiau Mnemolite source du chapitre XX
- [ ] Decider : (a) forcer reecriture du prompt d'extraction, (b) pre-traiter manuellement, (c) passer le chapitre (statut BLOQUE permanent)
- [ ] Mettre a jour livre/state/fail_hard_XX.json -> status: BLOQUE ou reset manuel

## 5. Etat pipeline
- Chapitre XX marque BLOQUE
- Prochain chapitre : 02
- Pas d'attente active : pipeline continue
""")
    print(f"count={counter['count']} >= 3 ET verdict=FAIL_HARD -> escalade ecrite, status=BLOQUE, FIN")
    import sys; sys.exit(0)

with open(counter_path, "w") as f:
    json.dump(counter, f, indent=2, ensure_ascii=False)
print(f"verdict={verdict_global} -> count={counter['count']}, pas encore BLOQUE, continuer")
PYEOF

  # Si on a atteint BLOQUE, le python a exit 0 et la suite n'est pas executee
  if [ $? -eq 0 ] && grep -q '"status": "BLOQUE"' "$COUNTER" 2>/dev/null; then
    break
  fi
done

echo "" | tee -a "$LOG"
echo "[$(date -Iseconds)] === PILOTE TERMINE ===" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "Compteur final :" | tee -a "$LOG"
cat "$COUNTER" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "=== STOP NET PRE-§2.5 Biblio (phi4-mini absent runtime) ===" | tee -a "$LOG"
