"""Démonstration end-to-end sur Sumer/France."""
import yaml
from pathlib import Path
from tools.engines.sublimator.extractors.orchestrator import run_cellule


if __name__ == "__main__":
    output = "/tmp/sumer_demo.yaml"
    result = run_cellule(
        input_path="investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md",
        civ_prefix="S",
        output_path=output,
        complexity="MEDIUM",
    )

    print("=" * 70)
    print("SUBLIMATOR v33.2 — Démonstration Sumer/France (end-to-end)")
    print("=" * 70)
    print(f"Exit code : {result['exit_code']}")
    print(f"Score GATE_G : {result['score']}% (MEDIUM cible 80%)")
    print(f"Gate pass : {result['gate_pass']}")
    print(f"F### matrice : {len(result['matrice'])}")
    print()
    print("=" * 70)
    print("EXTRACTIONS ARTICLE-UTILE")
    print("=" * 70)
    u = result["utile"]
    print(f"  Dates            : {len(u['dates']):3d}")
    print(f"  Sommes           : {len(u['sommes']):3d}")
    print(f"  Citations        : {len(u['citations']):3d}")
    print(f"  URLs             : {len(u['urls']):3d}")
    print(f"  Acteurs nommés   : {len(u['acteurs_nommes']):3d}")
    print(f"  Causalités       : {len(u['marqueurs_causalite']):3d}")
    print(f"  Rhétorique       : {len(u['marqueurs_rhetorique']):3d}")
    print(f"  Sections plan    : {len(u['sections_plan']):3d}/18")
    print()

    print("=" * 70)
    print("SECTIONS DU PLAN SUBLIMATOR DÉTECTÉES")
    print("=" * 70)
    for s in u["sections_plan"]:
        print(f"  §{s['section_num']:2d} {s['section_titre'][:60]:60s} L{s['line_no']}")
    print()

    print("=" * 70)
    print("PROMPT HÔTE (1ère ligne + nb sections)")
    print("=" * 70)
    prompt = result["prompt_hote"]
    print(f"  Longueur : {len(prompt):,} chars")
    print(f"  Première ligne : {prompt.splitlines()[0]}")
    n_sections_12 = sum(
        1 for s in [
            "these_centrale", "theses_implicites", "f_atomiques",
            "acteurs_network", "causalites", "perspectives_dialectiques",
            "limites", "wolves", "iceberg", "chronologie",
            "domaines", "urls_prioritaires",
        ] if s in prompt
    )
    print(f"  Sections 12 sections présentes dans le prompt : {n_sections_12}/12")
    print()

    print(f"YAML sérialisé : {output}")
    print(f"Taille YAML    : {Path(output).stat().st_size:,} octets")
