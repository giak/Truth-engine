#!/usr/bin/env bash
# adversarial_gate_v4.sh — Patch 1 V3.1 du gate adversarial (rev 3, sécurisé)
# JSON few-shot 1-shot + greedy decoding (temp=0, top_k=1, top_p=0) + format:"json" natif Ollama
#
# Bugs éliminés vs rev 2 :
#   #1 Injection Python heredoc — éliminée : passage par fichiers temp lus/crits
#      par Python via open().read(), AUCUNE interpolation bash dans Python.
#   #2 sed+THESE caractères spéciaux — éliminée : THESE vient d'un fichier,
#      lu par Python. Aucun sed avec interpolation variable bash.
#   #4 ${VAR//$\n/\n} cassait le newline — éliminée : printf '%s\n' vers fichier,
#      Python lit le fichier tel quel.
#   #5 exit 0 silencieux sur 11/11 malformés — fixé : exit 1 si JSON_VALID < TOTAL_BATCHES.
#   #8 /tmp collisions runs parallèles — fixé : tous les paths préfixés par $$.
#
# Usage :
#   ./adversarial_gate_v4.sh <facts_file> <these_file> [batch_size] [output_file]
#
# Args :
#   facts_file   : chemin vers le .md contenant les faits (1 fait par ligne)
#   these_file   : chemin vers un fichier texte contenant la thèse du chapitre
#                  (le fichier, pas la string, pour éviter quotes/backticks/bash sigils)
#   batch_size   : taille des batchs (défaut 5, max recommandé 6)
#   output_file  : fichier de sortie markdown pour rapport adversarial
#
# Sécurité :
#   - THESE lu depuis fichier (aucune interpolation)
#   - Facts écrits dans fichier temp via printf (safe multi-lignes)
#   - Template prompt écrit via cat << 'EOF' (pas d'interpolation)
#   - Python lit fichiers, fait str.replace, écrit prompt
#   - Aucune interpolation bash → Python

set -euo pipefail

FACTS_FILE="${1:?Usage: $0 <facts_file> <these_file> [batch_size] [output_file]}"
THESE_FILE="${2:?Fichier these requis (évite quotes/bash injection)}"
BATCH_SIZE="${3:-5}"
OUTPUT_FILE="${4:-/tmp/v31_adversarial_output_$$.md}"

OLLAMA_HOST="${OLLAMA_HOST:-http://localhost:11434}"
MODEL="${OLLAMA_ADVERSARIAL_MODEL:-qwen25-coder-7b-opt:latest}"
TIMEOUT="${OLLAMA_TIMEOUT:-180}"

# --- Paramètres Ollama V3.1 (Patch 1) — DOIVENT matcher spec §2.5 ---
TEMPERATURE="0.0"
TOP_K="1"
TOP_P="0.0"
NUM_PREDICT="600"
NUM_CTX="4096"

RED=$'\033[0;31m'; GREEN=$'\033[0;32m'; YELLOW=$'\033[1;33m'; NC=$'\033[0m'

PID_TAG="$$_$(date +%s)"  # PID + timestamp → 0 collision runs parallèles

echo "=== adversarial_gate_v4.sh — Patch 1 V3.1 (rev 3, sécurisé) ==="
echo "Facts file: $FACTS_FILE"
echo "These file: $THESE_FILE"
echo "Batch size: $BATCH_SIZE"
echo "Model: $MODEL"
echo "Output: $OUTPUT_FILE"
echo "PID tag: $PID_TAG"
echo ""

# --- Vérification Ollama UP ---
if ! curl -sf --max-time 5 "$OLLAMA_HOST/api/tags" >/dev/null 2>&1; then
    echo "${RED}ERREUR: Ollama non reachable sur $OLLAMA_HOST${NC}" >&2
    exit 2
fi

# --- Vérification fichiers d'entrée ---
if [[ ! -r "$FACTS_FILE" ]]; then
    echo "${RED}ERREUR: facts_file illisible: $FACTS_FILE${NC}" >&2
    exit 2
fi
if [[ ! -r "$THESE_FILE" ]]; then
    echo "${RED}ERREUR: these_file illisible: $THESE_FILE${NC}" >&2
    exit 2
fi

# --- Découpage en batches (hôte) ---
mapfile -t ALL_FACTS < <(grep -E '^[FD]-?[0-9]+' "$FACTS_FILE" || true)
if [[ ${#ALL_FACTS[@]} -eq 0 ]]; then
    echo "${RED}ERREUR: aucun fait trouvé dans $FACTS_FILE${NC}" >&2
    exit 2
fi
echo "Faits chargés: ${#ALL_FACTS[@]}"

# Calcule le nombre total de batches d'abord (pour les placeholders)
TOTAL_BATCHES_AT_END=$(( (${#ALL_FACTS[@]} + BATCH_SIZE - 1) / BATCH_SIZE ))
echo "Batches: $TOTAL_BATCHES_AT_END"
echo ""

# --- Prompt adversarial V3.1 — Few-shot 1-shot (avec 2 exemples, INVENTE + CHERRY_PICKING) ---
# Schéma JSON STRICT : contient_fait_invente, contient_cherry_picking, verdict, vulnerabilites[{id, type, description}]
# type ∈ {INVENTE|CHERRY_PICKING|CONTRADICTION|OMISSION} (aligné sur spec §2.5)
PROMPT_TEMPLATE_PATH="/tmp/v31_template_${PID_TAG}.txt"
cat > "$PROMPT_TEMPLATE_PATH" << 'TEMPLATE_EOF'
Tu es un auditeur adversarial. Tu DOIS trouver des failles dans le batch de faits ci-dessous.

⚠️ Les sources ont déjà été vérifiées (par l hôte). Concentre-toi UNIQUEMENT sur le contenu sémantique.

Cherche : hallucinations de contenu, cherry-picking narratif, biais narratif, incohérences entre CES faits, contradictions avec la thèse, omissions d acteurs ou chiffres essentiels.

=== EXEMPLE 1 (CHERRY_PICKING) — NE PAS COPIER CES DONNÉES ===
[Brief]: La privatisation du SI étatique est pilotée par un oligopole ESN.
[Faits batch 1/1]:
  F-12 | Capgemini a obtenu 1.1 Md€ de contrats État 2017-2022 mais aucun chiffre d évaluation d efficacité n est publié | Le Monde
  F-13 | Sopra Steria gère les radars (82M€ 2017-2026) mais aucun audit indépendant | Sénat
[JSON PARFAIT]:
{
  "contient_fait_invente": false,
  "contient_cherry_picking": true,
  "verdict": "FAIL_HARD",
  "vulnerabilites": [
    {"id": "F-12", "type": "CHERRY_PICKING", "description": "Sélection des montants financiers sans les contre-performances documentées (Cour des Comptes 2024)."}
  ]
}

=== EXEMPLE 2 (INVENTE) — NE PAS COPIER CES DONNÉES ===
[Brief]: Le marché français du cloud est dominé par AWS et Azure.
[Faits batch 1/1]:
  F-01 | AWS détient 73% du marché cloud français en 2026 (source inventée) | Rapport_Inconnu_2026
[JSON PARFAIT]:
{
  "contient_fait_invente": true,
  "contient_cherry_picking": false,
  "verdict": "FAIL_HARD",
  "vulnerabilites": [
    {"id": "F-01", "type": "INVENTE", "description": "Aucune source identifiable. Le chiffre 73% ne correspond à aucune étude publique (Gartner, IDC, Syndex)."}
  ]
}

=== FIN EXEMPLES ===

Brief : __THESE_PLACEHOLDER__
Faits (batch __BATCH_PLACEHOLDER__) : __FACTS_PLACEHOLDER__

⚠️ RÈGLE DE VERDICT IMPÉRATIVE (ne pas pondérer) :
- Si ≥ 1 fait est INVENTÉ (ou HALLUCINÉ) → verdict = FAIL_HARD, type = INVENTE
- Si ≥ 1 fait est CHERRY_PICKING (sélection orientée) → verdict = FAIL_HARD, type = CHERRY_PICKING
- Si ≥ 1 fait est CONTRADICTION (auto-contradiction entre faits du batch) → verdict = FAIL_HARD
- Si ≥ 1 fait est OMISSION (acteur ou chiffre essentiel à la thèse absent) → verdict = FAIL_HARD
- Si formulation ambiguë SANS invention → verdict = FAIL_SOFT
- Aucun défaut détecté → verdict = PASS

⚠️ FORMAT DE SORTIE STRICT (V3.1) :
- Réponds UNIQUEMENT avec le JSON.
- Pas de markdown, pas de ``` fences, pas de commentaire avant ou après.
- JSON parsable par json.loads Python SANS ERREUR.
- Toutes les clés obligatoires : contient_fait_invente, contient_cherry_picking, verdict, vulnerabilites.
- Type enum STRICT : INVENTE, CHERRY_PICKING, CONTRADICTION, OMISSION (vocabulaire exact).
TEMPLATE_EOF

# --- Entête du rapport ---
{
    echo "# Rapport adversarial V3.1 — $(date +%Y-%m-%d_%H-%M-%S)"
    echo ""
    echo "**Modèle** : $MODEL"
    echo "**Paramètres** : temperature=$TEMPERATURE, top_k=$TOP_K, top_p=$TOP_P, num_predict=$NUM_PREDICT, num_ctx=$NUM_CTX, format=json"
    echo "**Faits analysés** : ${#ALL_FACTS[@]}"
    echo "**Batch size** : $BATCH_SIZE"
    echo "**PID tag** : $PID_TAG (anti-collision runs parallèles)"
    echo ""
    echo "## Résultats par batch"
    echo ""
} > "$OUTPUT_FILE"

# --- Helper Python (fixe, écrit une fois) — Runner Ollama + Builder Prompt ---
# Runner Ollama : args = model, temp, top_k, top_p, num_predict, num_ctx, prompt_path
# Retourne JSON sur stdout : {ok, raw_text, verdict, vulnerabilites_count, error, duration_s}
RUNNER_PATH="/tmp/v31_runner_${PID_TAG}.py"
cat > "$RUNNER_PATH" << 'RUNNER_EOF'
#!/usr/bin/env python3
"""Runner adversarial V3.1 — invoque Ollama et valide JSON.

Args (sys.argv) :
  1. model
  2. temp (float)
  3. top_k (int)
  4. top_p (float)
  5. num_predict (int)
  6. num_ctx (int)
  7. prompt_path (str)

Returns : JSON sur stdout (pour faciliter parsing bash).
"""
import json, sys, urllib.request, urllib.error, time, os

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
TIMEOUT = int(os.environ.get("OLLAMA_TIMEOUT", "180"))

model = sys.argv[1]
temperature = float(sys.argv[2])
top_k = int(sys.argv[3])
top_p = float(sys.argv[4])
num_predict = int(sys.argv[5])
num_ctx = int(sys.argv[6])
prompt_path = sys.argv[7]

with open(prompt_path, "r", encoding="utf-8") as f:
    prompt = f.read()

request_body = {
    "model": model,
    "prompt": prompt,
    "format": "json",
    "stream": False,
    "options": {
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p,
        "num_predict": num_predict,
        "num_ctx": num_ctx,
    },
}

start = time.time()
try:
    data = json.dumps(request_body).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_HOST}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        result = json.loads(r.read().decode("utf-8"))
    duration = time.time() - start
    raw_text = result.get("response", "")
    ok, payload = False, None
    err_msg = ""
    try:
        payload = json.loads(raw_text)
        req_keys = ["contient_fait_invente", "contient_cherry_picking", "verdict", "vulnerabilites"]
        missing = [k for k in req_keys if k not in payload]
        if missing:
            err_msg = f"KEYS_MISSING:{missing}"
        else:
            # Validation stricte du type enum
            valid_types = {"INVENTE", "CHERRY_PICKING", "CONTRADICTION", "OMISSION"}
            for v in payload.get("vulnerabilites", []):
                vtype = v.get("type", "")
                if vtype not in valid_types:
                    err_msg = f"INVALID_TYPE:{vtype} (attendu ∈ {valid_types})"
                    break
            if not err_msg:
                # Validation stricte du verdict top-level (V3.1 rev 4)
                valid_verdicts = {"PASS", "FAIL_SOFT", "FAIL_HARD"}
                verdict = payload.get("verdict", "")
                if verdict not in valid_verdicts:
                    err_msg = f"INVALID_VERDICT:{verdict} (attendu ∈ {valid_verdicts})"
                else:
                    ok = True
    except json.JSONDecodeError as e:
        err_msg = f"INVALID_JSON:{e}"
    print(json.dumps({
        "ok": ok,
        "raw_text": raw_text,
        "verdict": payload.get("verdict") if ok else None,
        "vulnerabilites_count": len(payload.get("vulnerabilites", [])) if ok else 0,
        "error": err_msg,
        "duration_s": round(duration, 2),
    }, ensure_ascii=False))
except urllib.error.URLError as e:
    print(json.dumps({"ok": False, "raw_text": "", "error": f"CURL_ERR:{e}", "duration_s": round(time.time()-start, 2)}))
except Exception as e:
    print(json.dumps({"ok": False, "raw_text": "", "error": f"EXCEPTION:{type(e).__name__}:{e}", "duration_s": round(time.time()-start, 2)}))
RUNNER_EOF

# --- Helper Python — Build prompt from template (lit fichiers, AUCUNE interpolation bash) ---
# Args : template_path, these_file, batch_num, total_batches, facts_lines_via_stdin
BUILDER_PATH="/tmp/v31_builder_${PID_TAG}.py"
cat > "$BUILDER_PATH" << 'BUILDER_EOF'
#!/usr/bin/env python3
"""Builder prompt V3.1 — lit template + these + facts depuis fichiers.

Args (sys.argv) :
  1. template_path
  2. these_file
  3. batch_num (str)
  4. total_batches (str)
  5. output_path

Lit les facts depuis stdin (ligne par ligne).
"""
import sys

template_path = sys.argv[1]
these_file = sys.argv[2]
batch_num = sys.argv[3]
total_batches = sys.argv[4]
output_path = sys.argv[5]

with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

with open(these_file, "r", encoding="utf-8") as f:
    these = f.read().strip()

facts = sys.stdin.read().rstrip("\n")

prompt = template.replace("__THESE_PLACEHOLDER__", these)
prompt = prompt.replace("__BATCH_PLACEHOLDER__", f"{batch_num}/{total_batches}")
prompt = prompt.replace("__FACTS_PLACEHOLDER__", facts)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(prompt)
BUILDER_EOF

JSON_VALID=0
JSON_MALFORMED=0
TOTAL_BATCHES=0

# --- Boucle sur chaque batch ---
for ((i=0; i<"${#ALL_FACTS[@]}"; i+=BATCH_SIZE)); do
    BATCH=("${ALL_FACTS[@]:i:BATCH_SIZE}")
    BATCH_NUM=$(( (i / BATCH_SIZE) + 1 ))
    TOTAL_BATCHES=$((TOTAL_BATCHES + 1))

    PROMPT_PATH="/tmp/v31_prompt_${PID_TAG}_${BATCH_NUM}.txt"

    # Construit le prompt via Python BUILDER (sécurisé, lit fichiers)
    # Passe les facts via stdin (printf '%s\n')
    printf '%s\n' "${BATCH[@]}" | python3 "$BUILDER_PATH" \
        "$PROMPT_TEMPLATE_PATH" \
        "$THESE_FILE" \
        "$BATCH_NUM" \
        "$TOTAL_BATCHES_AT_END" \
        "$PROMPT_PATH"

    echo -n "Batch ${BATCH_NUM}/${TOTAL_BATCHES_AT_END} (${#BATCH[@]} faits)… "

    # Invoque Ollama via Python RUNNER
    RESULT_JSON=$(python3 "$RUNNER_PATH" \
        "$MODEL" "$TEMPERATURE" "$TOP_K" "$TOP_P" \
        "$NUM_PREDICT" "$NUM_CTX" \
        "$PROMPT_PATH")

    # Extraction sécurisée des champs JSON via Python (pas d'injection bash)
    OK=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; print('1' if json.loads(sys.stdin.read())['ok'] else '0')")
    VERDICT=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); print(d.get('verdict') or '?')")
    NB_VULN=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); print(d.get('vulnerabilites_count', 0))")
    ERROR=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); print(d.get('error') or '')")
    RAW=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; print(json.loads(sys.stdin.read())['raw_text'])")
    DURATION=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); print(d.get('duration_s', 0))")

    # --- Circuit-breaker V3.1 rev 4 : warn si batch lent >60s (suggère model swap/reload) ---
    BATCH_LENT=$(printf '%s' "$RESULT_JSON" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); print('1' if float(d.get('duration_s', 0)) > 60.0 else '0')" 2>/dev/null || echo 0)
    if [[ "$BATCH_LENT" == "1" ]]; then
        echo "${YELLOW}[BATCH-LENT] ${BATCH_NUM}/${TOTAL_BATCHES_AT_END} = ${DURATION}s > 60s (swap/reload probable — surveiller)${NC}" >&2
    fi

    # Échappe ``` dans RAW (anti-casse fences markdown)
    SAFE_RAW="${RAW//\`\`\`/<BACKTICK_FENCE>}"

    if [[ "$OK" == "1" ]]; then
        JSON_VALID=$((JSON_VALID + 1))
        echo "${GREEN}OK (${DURATION}s) verdict=${VERDICT} vulns=${NB_VULN}${NC}"
        {
            echo "### Batch ${BATCH_NUM}/${TOTAL_BATCHES_AT_END} — ✅ JSON VALID — verdict=${VERDICT} — ${NB_VULN} vulnérabilités — ${DURATION}s"
            echo ""
            echo '```json'
            echo "$SAFE_RAW"
            echo '```'
            echo ""
        } >> "$OUTPUT_FILE"
    else
        JSON_MALFORMED=$((JSON_MALFORMED + 1))
        echo "${RED}MALFORMED (${DURATION}s) — ${ERROR}${NC}"
        {
            echo "### Batch ${BATCH_NUM}/${TOTAL_BATCHES_AT_END} — ❌ ${ERROR} — ${DURATION}s"
            echo ""
            echo '```'
            echo "$SAFE_RAW"
            echo '```'
            echo ""
        } >> "$OUTPUT_FILE"
    fi

    # Cleanup prompt-batch (réduit risque de pollution /tmp)
    rm -f "$PROMPT_PATH" 2>/dev/null || true
done

# --- Synthèse finale ---
{
    echo ""
    echo "## Synthèse"
    echo ""
    echo "- **Batches totaux** : $TOTAL_BATCHES"
    echo "- **JSON valides** : $JSON_VALID"
    echo "- **JSON malformés** : $JSON_MALFORMED"
    if [[ $TOTAL_BATCHES -gt 0 ]]; then
        SUCCESS_RATE=$(python3 -c "print(f'{100*$JSON_VALID/$TOTAL_BATCHES:.1f}%')")
        echo "- **Taux de réussite JSON** : $SUCCESS_RATE"
        if [[ $JSON_MALFORMED -eq 0 ]]; then
            echo ""
            echo "✅ **PATCH 1 V3.1 CONFIRMÉ** : 100% JSON valides sur $TOTAL_BATCHES batchs."
            echo "Rappel V3.0 (sans Patch 1) : 0/$TOTAL_BATCHES JSON valides (11/11 malformés sur le stress test IT)."
        else
            echo ""
            echo "⚠️ **PATCH 1 V3.1 PARTIELLEMENT OPÉRANT** : $JSON_VALID/$TOTAL_BATCHES JSON valides."
            echo "Cause possible : type enum invalide, greedy decoding insuffisant, ou prompt mal calibré."
        fi
    fi
} >> "$OUTPUT_FILE"

echo ""
echo "=== Synthèse ==="
echo "Batches traités: $TOTAL_BATCHES"
echo "${GREEN}JSON valides: $JSON_VALID${NC}"
echo "${RED}JSON malformés: $JSON_MALFORMED${NC}"
if [[ $TOTAL_BATCHES -gt 0 ]]; then
    SUCCESS_RATE=$(python3 -c "print(f'{100*$JSON_VALID/$TOTAL_BATCHES:.1f}%')")
    echo "Taux de réussite: $SUCCESS_RATE"
fi
echo "Rapport complet: $OUTPUT_FILE"

# Cleanup final
rm -f "$PROMPT_TEMPLATE_PATH" "$RUNNER_PATH" "$BUILDER_PATH" 2>/dev/null || true

# --- Bug #5 fixé : exit 1 si Patch 1 inopérant ---
if [[ $JSON_VALID -lt $TOTAL_BATCHES ]]; then
    echo ""
    echo "${RED}[ÉCHEC-PATCH-1-V3.1-INOPÉRANT] $JSON_VALID/$TOTAL_BATCHES JSON valides — escalation hôte requise${NC}" >&2
    exit 1
fi

exit 0
