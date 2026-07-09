#!/usr/bin/env python3
"""
Replace all [LIEN_A_INSERER] navigation placeholders with real Substack URLs.
"""

import os
import re

ARTICLES_DIR = os.path.dirname(os.path.abspath(__file__))

URLS = {
    "S1": "https://giak.substack.com/p/la-caste-parasite-qui-gouverne-la",
    "S2": "https://giak.substack.com/p/largent-qui-disparait-80-a-100-milliards",
    "S3": "https://giak.substack.com/p/la-dette-instrumentalisee-3-200-milliards",
    "S4": "https://giak.substack.com/p/le-systeme-de-sante-demantele-8-millions",
    "S5": "https://giak.substack.com/p/les-visages-de-la-pauvrete-98-millions",
    "S6": "https://giak.substack.com/p/la-france-desindustrialisee-81-milliards",
    "S7": "https://giak.substack.com/p/lecole-sans-transmission-43-points",
    "S8": "https://giak.substack.com/p/limmigration-sans-cap-340-000-titres",
    "S9": "https://giak.substack.com/p/le-logement-la-machine-a-creer-de",
    "S10": "https://giak.substack.com/p/lenergie-sacrifiee-923-twh-exportes",
    "S11": "https://giak.substack.com/p/lagriculture-qui-meurt-100-000-fermes",
    "S12": "https://giak.substack.com/p/medias-censure-et-desinformation",
    "S13": "https://giak.substack.com/p/leurope-piege-francais-12-contentieux",
    "S14": "https://giak.substack.com/p/la-defense-rongee-449-md-sans-munitions",
    "S15": "https://giak.substack.com/p/le-verrou-28-recours-au-493-57-dabstention",
    "S16": "https://giak.substack.com/p/le-numerique-colonise-70-des-donnees",
    "S17": "https://giak.substack.com/p/la-justice-fantome-020-du-pib-86",
    "HUB": "https://giak.substack.com/p/le-changement-de-regime-pourquoi",
}

NAV_MAP = {
    "S1_la_caste_parasite.md": [("L'Argent qui dispara", "S2")],
    "S2_l_argent_qui_disparait.md": [("La Dette instrumentalis", "S3")],
    "S3_la_dette_instrumentalisee.md": [
        ("Le Verrou", "S15"),
        ("L'Argent qui dispara", "S2"),
    ],
    "S4_le_systeme_de_sante_demantele.md": [("Les Visages de la Pauvr", "S5")],
    "S5_les_visages_de_la_pauvrete.md": [("Le Syst\xe8me de sant\xe9 d", "S4")],
    "S6_la_france_desindustrialisee.md": [("Les Visages de la Pauvr", "S5")],
    "S8_limmigration_sans_cap.md": [("Le Logement, la Machin", "S9")],
    "S9_le_logement_la_machine_a_creer_de_la_rarete.md": [
        ("L'\xc9nergie sacrifi\xe9e", "S10"),
        ("L'Immigration sans Ca", "S8"),
    ],
    "S10_lenergie_sacrifiee.md": [
        ("L'Agriculture qui meur", "S11"),
        ("Le Logement, la Machin", "S9"),
    ],
    "S11_lagriculture_qui_meurt.md": [
        ("L'Europe : cadre ou car", "S13"),
        ("L'Agriculture qui meur", "S11"),  # precedent
        ("L'\xc9nergie sacrifi\xe9e", "S10"),
    ],
    "S12_medias_censure_desinformation.md": [
        ("L'Immigration sans ca", "S8"),
        ("L'\xc9cole et l'\xc9duc", "S7"),
    ],
    "S13_leurope_cadre_ou_carcan.md": [
        ("La D\xe9fense en ber", "S14"),
        ("L'Agriculture qui meur", "S11"),
    ],
    "S14_la_defense_en_berne.md": [
        ("Le Num\xe9rique colonis", "S16"),
        ("L'Europe : cadre ou ca", "S13"),
    ],
    "S15_le_verrou.md": [("La Dette instrumentalis", "S3")],
}


def process_file(filepath):
    filename = os.path.basename(filepath)
    if filename not in NAV_MAP:
        return False, []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    modified = False
    changes = []

    for i, line in enumerate(lines):
        if "[LIEN_A_INSERER]" not in line:
            continue

        # Try each entry in NAV_MAP to find a keyword match
        matched = False
        for keyword, target_article in NAV_MAP[filename]:
            if keyword not in line:
                continue

            url = URLS.get(target_article)
            if not url:
                print(f"  \u26a0\ufe0f  {filename}:{i+1} \u2014 Pas d'URL pour {target_article}")
                continue

            # Parse the line to extract the title text and build a proper markdown link.
            # The line looks like:
            # *... **Article suivant :** EMOJI Titre de l'article [LIEN_A_INSERER]*
            # or
            # *... **\u00c0 lire ensuite :** EMOJI Titre [LIEN_A_INSERER]*

            # Strategy: find the position of :** then skip emoji/separator chars to find title
            # Then wrap title in [title](url) and remove [LIEN_A_INSERER]

            # Find the ":**" marker
            colon_pos = line.find(":**")
            if colon_pos == -1:
                print(f"  \u26a0\ufe0f  {filename}:{i+1} \u2014 Pas de ':**' dans la ligne")
                continue

            # Everything after ":** " up to " [LIEN_A_INSERER]" is the "separator + title"
            after_colon = line[colon_pos + 3:]  # skip ":**"

            # The first part (before the first word character) is the emoji separator
            # Find first actual word character
            title_start_in_after = 0
            for ch_idx, ch in enumerate(after_colon):
                if ch.isalpha() or ch in "'\"":
                    title_start_in_after = ch_idx
                    break

            # The title text goes until we hit " [LIEN_A_INSERER]"
            lien_pos = line.find("[LIEN_A_INSERER]")
            if lien_pos == -1:
                continue

            # title is from after_colon offset to the [LIEN_A_INSERER]
            title_relative_end = lien_pos - (colon_pos + 3)
            title_text = after_colon[title_start_in_after:title_relative_end].strip()

            # Build the new line
            before_title = line[:colon_pos + 3 + title_start_in_after]
            after_lien = line[lien_pos + len("[LIEN_A_INSERER]"):]

            # Remove trailing "*" if it was after [LIEN_A_INSERER]
            if after_lien.startswith("*"):
                after_lien = after_lien[1:]

            new_line = before_title + "[" + title_text + "](" + url + ")" + after_lien

            lines[i] = new_line
            modified = True
            changes.append((i + 1, target_article, url))
            matched = True
            break

        if not matched:
            print(f"  \u26a0\ufe0f  {filename}:{i+1} \u2014 [LIEN_A_INSERER] non reconnu")
            print(f"      Ligne: {line[:120]}")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    return modified, changes


def main():
    print("=" * 60)
    print("Remplacement des [LIEN_A_INSERER] dans les articles")
    print("=" * 60)
    print()

    article_files = sorted([
        f for f in os.listdir(ARTICLES_DIR)
        if f.endswith(".md") and not f.startswith("2026-")
        and not f.startswith("replace_") and not f.startswith("liste_")
    ])

    total_modified = 0
    total_changes = 0

    for filename in article_files:
        filepath = os.path.join(ARTICLES_DIR, filename)
        if not os.path.isfile(filepath):
            continue
        if filename not in NAV_MAP:
            continue

        modified, changes = process_file(filepath)
        if modified:
            total_modified += 1
            total_changes += len(changes)
            for lineno, target, url in changes:
                print(f"  \u2705 {filename}:{lineno} \u2192 {target} ({url})")

    # Verify remaining
    remaining = []
    skip_files = {"PROMPT_ARTICLE_MASTER.md"}
    for filename in article_files:
        if filename in skip_files:
            continue
        filepath = os.path.join(ARTICLES_DIR, filename)
        if not os.path.isfile(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if "[LIEN_A_INSERER]" in line:
                    remaining.append(f"  {filename}:{i}")

    print()
    print("=" * 60)
    print(f"Fichiers modifi\xe9s : {total_modified}")
    print(f"Remplacements effectu\xe9s : {total_changes}")

    if remaining:
        print(f"[LIEN_A_INSERER] restants dans les articles S/HUB : {len(remaining)}")
        for r in remaining:
            print(f"  \u26a0\ufe0f  {r}")
    else:
        print("[LIEN_A_INSERER] restants dans les articles S/HUB : 0 \u2705")

    # Note about PROMPT_ARTICLE_MASTER.md
    prompt_file = os.path.join(ARTICLES_DIR, "PROMPT_ARTICLE_MASTER.md")
    if os.path.isfile(prompt_file):
        count = 0
        with open(prompt_file, "r") as f:
            for line in f:
                if "[LIEN_A_INSERER]" in line:
                    count += 1
        if count > 0:
            print(f"PROMPT_ARTICLE_MASTER.md : {count} [LIEN_A_INSERER] (template — volontaire)")

    print("=" * 60)


if __name__ == "__main__":
    main()
