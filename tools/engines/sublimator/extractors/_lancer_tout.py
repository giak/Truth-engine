"""Lance l'orchestrateur Python sur toutes les enquêtes du dossier Sumer.

Génère des YAML squelettes dans _quintessence/. Chaque squelette contient :
  - f_atomiques (candidats)
  - utile (dates, sommes, URLs, acteurs, sections plan)
  - prompt_hote (à compléter par LLM hôte)

Étape suivante : pour chaque squelette, le LLM hôte (moi) lit l'enquête
et complète les 11 sections de quintessence.
"""
from pathlib import Path
from tools.engines.sublimator.extractors.orchestrator import run_cellule


ENQUETES = [
    ("2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md", "S"),
    ("2026-06-03_13-00_rome_vs_france_INVESTIGATION.md", "R"),
    ("2026-06-03_14-00_chine_vs_france_INVESTIGATION.md", "C"),
    ("2026-06-04_09-30_moyen_age_gense_etat_FRANCAIS_INVESTIGATION.md", "MA"),
    ("2026-06-04_10-00_islam_golden_age_CIVILISATION_MANQUANTE.md", "I"),
    ("2026-06-04_10-30_inde_civilisation_manquante_INVESTIGATION.md", "IN"),
    ("2026-06-04_11-00_ameriques_precolombiennes_CIVILISATION_MANQUANTE.md", "AM"),
    ("2026-06-04_14-30_andurarum_autopsy_INVESTIGATION.md", "A"),
    ("2026-06-04_15-00_hub_changement_regime_source_audit_AUDIT.md", "HUB"),
    ("2026-06-04_15-10_shadow_meta_final_RECALCUL.md", "META"),
]

DIR = "investigations/2026-06-03_sumer_article"
QUINT_DIR = f"{DIR}/_quintessence"


def main():
    print("=" * 70)
    print("LANCEMENT ORCHESTRATEUR v33.2 sur 10 enquêtes")
    print("=" * 70)
    for filename, prefix in ENQUETES:
        input_path = f"{DIR}/{filename}"
        output_path = f"{QUINT_DIR}/{prefix}_quintessence_squelette.yaml"
        if not Path(input_path).exists():
            print(f"  SKIP {filename} (fichier introuvable)")
            continue
        result = run_cellule(
            input_path=input_path,
            civ_prefix=prefix,
            output_path=output_path,
            complexity="MEDIUM",
        )
        n_f = len(result["matrice"])
        n_dates = len(result["utile"]["dates"])
        n_sommes = len(result["utile"]["sommes"])
        n_urls = len(result["utile"]["urls"])
        n_sections = len(result["utile"]["sections_plan"])
        print(f"  [{prefix:4s}] {filename[:55]:55s} F###={n_f:3d} dates={n_dates:2d} sommes={n_sommes:3d} urls={n_urls:2d} sections={n_sections:2d}/18 score={result['score']}%")
    print()
    print(f"YAML squelettes dans : {QUINT_DIR}/")


if __name__ == "__main__":
    main()
