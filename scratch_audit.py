import os
import re

dirs = [
    "2026-06-11_projet_politique_coordination",
    "2026-06-11_biais_classe_corpus",
    "2026-06-11_biais_race_genre_corpus",
    "2026-06-11_police_maintien_ordre_france",
    "2026-06-11_etat_fragile_france",
    "2026-06-11_narratif_opinion_publique",
    "2026-06-11_psychologie_militante_coordination",
    "2026-06-11_addendum_defeat_v2",
    "2026-06-11_design_validation_empirique",
    "2026-06-10_leadership_acephalique",
    "2026-06-10_financement_coordination",
    "2026-06-10_risque_juridique_coordination",
    "2026-06-10_analyse_defaite_guerilla",
    "2026-06-10_verrou_coordination_guerilla",
    "2026-06-10_action_acephalique_manquante",
    "2026-06-10_fresque_systemique_oligarchie",
    "2026-06-10_modele_non_escalade_france",
    "2026-06-10_puits_de_droit_concret",
    "2026-06-10_solutions_succession",
    "2026-06-10_solutions_financement_invisible",
    "2026-06-10_droit_compare_benelux_coordination"
]

base_path = "/home/giak/projects/truth-engine/investigations"

for d in dirs:
    d_path = os.path.join(base_path, d)
    if not os.path.exists(d_path):
        print(f"MISSING DIR: {d}")
        continue
    for f in os.listdir(d_path):
        if f.endswith(".md"):
            f_path = os.path.join(d_path, f)
            with open(f_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Extract score
                score_match = re.search(r'SUSPICION_SCORE\s*:\s*([\d\.]+/\d+)', content)
                score = score_match.group(1) if score_match else "N/A"
                
                # Extract summary (RÉSUMÉ)
                resume_match = re.search(r'## §1 RÉSUMÉ\s*(.*?)(?=\n## |$)', content, re.DOTALL)
                resume = resume_match.group(1).strip()[:500] + "..." if resume_match else "N/A"
                
                print(f"--- FILE: {f} ---")
                print(f"DIR: {d}")
                print(f"SCORE: {score}")
                print(f"RESUME: {resume}")
                print()
