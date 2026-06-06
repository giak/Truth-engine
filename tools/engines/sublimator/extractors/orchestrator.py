import yaml
from pathlib import Path
from .parse_atomic import parse_all
from .llm_lecteur import lecteur_cursif
from .llm_curator import curator_fusion
from .llm_verifier import verifier
from .gate_g import compute_completude, gate_g_pass


def run_cellule(
    input_path: str,
    civ_prefix: str,
    output_path: str,
    complexity: str = "MEDIUM",
) -> dict:
    """Orchestre Agent A → B → C → D → E sur 1 enquête."""
    text = Path(input_path).read_text()

    candidats_a = parse_all(text, civ_prefix=civ_prefix)
    sections_b = lecteur_cursif(text, civ_prefix=civ_prefix)
    matrice = curator_fusion(
        candidats_a, sections_b.get("ajouts", []), civ_prefix=civ_prefix
    )
    rapport = verifier(matrice, text)

    score = compute_completude(text, matrice)
    if not gate_g_pass(score, complexity):
        return {
            "exit_code": 1,
            "error": f"GATE_G fail: {score}% < {complexity} cible",
            "matrice": matrice,
            "rapport": rapport,
            "score": score,
        }

    fiche = {
        "these_centrale": sections_b["these_centrale"],
        "theses_implicites": sections_b["theses_implicites"],
        "f_atomiques": matrice,
        "acteurs_network": sections_b["acteurs"],
        "causalites": sections_b["causalites"],
        "perspectives_dialectiques": sections_b["perspectives_dialectiques"],
        "limites": sections_b["limites"],
        "wolves": sections_b["wolves"],
        "iceberg": sections_b["iceberg"],
        "chronologie": sections_b["chronologie"],
        "domaines": sections_b["domaines"],
        "urls_prioritaires": sections_b["urls_prioritaires"],
        "completude": score,
        "rapport_verifier": rapport,
    }

    Path(output_path).write_text(
        yaml.dump(fiche, allow_unicode=True, sort_keys=False)
    )

    return {
        "exit_code": 0,
        "output": output_path,
        "matrice": matrice,
        "score": score,
    }
