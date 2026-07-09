#!/bin/bash
# replace_url_placeholders.sh
# Remplace les URL_S# par les vraies URLs Substack dans tous les articles S et HUB
# Usage: bash replace_url_placeholders.sh [--dry-run]

set -e

ARTICLES_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ARTICLES_DIR"

DRY_RUN=false
if [ "$1" = "--dry-run" ]; then
    DRY_RUN=true
fi

# Mapping URL_S# → URLs Substack réelles (liste_articles__online.md)
# Ordre : S10-S17 avant S1-S9 pour éviter les collisions de sous-chaînes
declare -A URLS
URLS[URL_S10]="https://giak.substack.com/p/lenergie-sacrifiee-923-twh-exportes"
URLS[URL_S11]="https://giak.substack.com/p/lagriculture-qui-meurt-100-000-fermes"
URLS[URL_S12]="https://giak.substack.com/p/medias-censure-et-desinformation"
URLS[URL_S13]="https://giak.substack.com/p/leurope-piege-francais-12-contentieux"
URLS[URL_S14]="https://giak.substack.com/p/la-defense-rongee-449-md-sans-munitions"
URLS[URL_S15]="https://giak.substack.com/p/le-verrou-28-recours-au-493-57-dabstention"
URLS[URL_S16]="https://giak.substack.com/p/le-numerique-colonise-70-des-donnees"
URLS[URL_S17]="https://giak.substack.com/p/la-justice-fantome-020-du-pib-86"
URLS[URL_S1]="https://giak.substack.com/p/la-caste-parasite-qui-gouverne-la"
URLS[URL_S2]="https://giak.substack.com/p/l-argent-qui-disparait"
URLS[URL_S3]="https://giak.substack.com/p/la-dette-instrumentalisee-3-200-milliards"
URLS[URL_S4]="https://giak.substack.com/p/le-systeme-de-sante-demantele-8-millions"
URLS[URL_S5]="https://giak.substack.com/p/les-visages-de-la-pauvrete-98-millions"
URLS[URL_S6]="https://giak.substack.com/p/la-france-desindustrialisee-81-milliards"
URLS[URL_S7]="https://giak.substack.com/p/lecole-sans-transmission-43-points"
URLS[URL_S8]="https://giak.substack.com/p/limmigration-sans-cap-340-000-titres"
URLS[URL_S9]="https://giak.substack.com/p/le-logement-la-machine-a-creer-de"
URLS[URL_HUB]="https://giak.substack.com/p/le-changement-de-regime-pourquoi"

# Fichiers à traiter
FILES=(HUB_le_changement_de_regime.md S*.md)

count_total=0
count_files=0

for file in "${FILES[@]}"; do
    [ -f "$file" ] || continue
    file_modified=false

    for placeholder in URL_S10 URL_S11 URL_S12 URL_S13 URL_S14 URL_S15 URL_S16 URL_S17 URL_S1 URL_S2 URL_S3 URL_S4 URL_S5 URL_S6 URL_S7 URL_S8 URL_S9 URL_HUB; do
        url="${URLS[$placeholder]}"
        if grep -q "$placeholder" "$file" 2>/dev/null; then
            count=$(grep -o "$placeholder" "$file" | wc -l)
            count_total=$((count_total + count))
            file_modified=true
            if [ "$DRY_RUN" = false ]; then
                sed -i "s|$placeholder|$url|g" "$file"
            fi
        fi
    done

    if [ "$file_modified" = true ]; then
        count_files=$((count_files + 1))
        if [ "$DRY_RUN" = true ]; then
            echo "[DRY-RUN] $file : placeholders présents"
        fi
    fi
done

if [ "$DRY_RUN" = true ]; then
    echo "---"
    echo "Dry-run terminé. $count_total placeholders trouvés dans $count_files fichiers."
    echo "Lancez sans --dry-run pour appliquer les remplacements."
else
    echo "Remplacement terminé. $count_total placeholders remplacés dans $count_files fichiers."
fi
