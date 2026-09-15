#!/usr/bin/env bash
# Harnais de revue multi-rôles du masterwork — 2026-09-15
#
# Fournisseur : NVIDIA NIM (palier gratuit). Le catalogue OpenRouter est épuisé
# (solde 0,034 $ sur 10 $ consommés) et Groq plafonne à 8 000 jetons par minute,
# insuffisant pour un article de 9 099 mots : les deux sont donc écartés, et ce
# choix est tracé ici pour ne pas le rejouer.
#
# Trois modèles seulement répondent encore sur NIM : nemotron-3-ultra-550b-a55b,
# nemotron-3-super-120b-a12b, nemotron-3.5-lightning-30b-a3b. Les autres du
# catalogue renvoient 410 Gone (fin de vie) ou 404.
#
# Chaque agent tourne avec setsid pour survivre à la mort du shell appelant.
set -u
ROOT=/home/giak/projects/truth-engine
DIR="$ROOT/articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/REVIEWS_ROLES_2026-09-15"
cd "$ROOT" || exit 1
mkdir -p "$DIR/_logs"
: > "$DIR/_logs/00_harnais.txt"
echo "demarrage $(date '+%Y-%m-%d %H:%M:%S')" >> "$DIR/_logs/00_harnais.txt"

ULTRA="nvidia/nvidia/nemotron-3-ultra-550b-a55b"
SUPER="nvidia/nvidia/nemotron-3-super-120b-a12b"
LIGHT="nvidia/nvidia/nemotron-3.5-lightning-30b-a3b"

lancer() { # $1 = rôle   $2 = modèle
  local role="$1" model="$2"
  setsid nohup timeout 2700 opencode run --pure --auto -m "$model" \
    "$(cat "$DIR/PROMPT_${role}.md")" \
    > "$DIR/_logs/${role}.log" 2>&1 < /dev/null &
  echo "${role} ${model} pid=$!" >> "$DIR/_logs/00_harnais.txt"
  sleep 5
}

lancer R1_CONTRADICTEUR_EPISTEMOLOGIQUE "$ULTRA"
lancer R4_JURISTE                      "$ULTRA"
lancer R8_AVOCAT_DU_DIABLE             "$ULTRA"
lancer R3_FACT_CHECKER_FORENSIQUE      "$ULTRA"
lancer R2_REDACTEUR_EN_CHEF            "$SUPER"
lancer R5_AUDITEUR_METHODOLOGIQUE      "$SUPER"
lancer R6_PHILOSOPHE_LANGAGE           "$SUPER"
lancer R9_CORRECTEUR_FRANCAIS          "$SUPER"
lancer R7_RISQUE_INSTRUMENTALISATION   "$LIGHT"
lancer R10_LECTEUR_PROFANE             "$LIGHT"

echo "TOUS_LANCES $(date '+%Y-%m-%d %H:%M:%S')" >> "$DIR/_logs/00_harnais.txt"
