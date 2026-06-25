"""Gates H0-H6 — validation structurelle minimale (Sublimator v34 Léger).

Pas de GATE_G (complétude): le LLM hôte compte ses F## lui-même.
Les 7 checks H0-H6 valident la structure YAML uniquement.
"""

import yaml
from typing import Any

VALID_GLYPHS: set[str] = {"✦", "✧", "⁅", "❧"}


def validate(yaml_path: str, yaml_type: str = "quintessence") -> tuple[bool, list[str]]:
    """Valide un fichier YAML (quintessence ou synthese) contre H0-H6.

    Args:
        yaml_path: Chemin vers le YAML.
        yaml_type: "quintessence" (12 clés) ou "synthese" (8 clés).

    Returns:
        (passed, messages): passed est False si au moins un check échoue.
    """
    messages: list[str] = []

    # H0: fichier parsable
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return False, [f"H0: YAML invalide — {e}"]
    except FileNotFoundError:
        return False, [f"H0: Fichier introuvable — {yaml_path}"]

    if not isinstance(data, dict):
        return False, ["H0: Le YAML est parsable mais ne contient pas un dictionnaire racine"]

    # H1: clés obligatoires
    required_keys = QUINTESSENCE_KEYS if yaml_type == "quintessence" else SYNTHESE_KEYS
    missing = [k for k in required_keys if k not in data]
    if missing:
        messages.append(f"H1: Clé(s) manquante(s) — {missing}")

    # H2: types valides
    type_checks = _type_checks(yaml_type)
    for key, expected_type in type_checks.items():
        if key in data and not isinstance(data[key], expected_type):
            messages.append(f"H2: Type invalide pour '{key}' — attendu {expected_type.__name__}, reçu {type(data[key]).__name__}")

    # H3: glyphes valides (seulement si faits_atomiques présent)
    if "faits_atomiques" in data and isinstance(data["faits_atomiques"], list):
        for fait in data["faits_atomiques"]:
            gid = fait.get("id", "?")
            glyphe = fait.get("glyphe", "")
            if glyphe not in VALID_GLYPHS:
                messages.append(f"H3: Glyphe invalide pour '{gid}' — '{glyphe}' (attendu ✦/✧/⁅/❧)")

    # H4: IDs uniques
    if "faits_atomiques" in data and isinstance(data["faits_atomiques"], list):
        seen: dict[str, int] = {}
        for fait in data["faits_atomiques"]:
            fid = fait.get("id", "")
            if fid:
                seen[fid] = seen.get(fid, 0) + 1
        for fid, count in seen.items():
            if count > 1:
                messages.append(f"H4: F## dupliqué — '{fid}' ×{count}")

    # H5: chaque thèse a ≥ 3 F## justificatifs
    if "theses_cardinales" in data and isinstance(data["theses_cardinales"], list):
        for these in data["theses_cardinales"]:
            titre = these.get("titre", these.get("enonce", "?"))
            justifs = these.get("f_atomiques_justificatifs", [])
            if len(justifs) < 3:
                messages.append(f"H5: Thèse '{titre}' a {len(justifs)} F## justificatifs (min 3)")

    # H6: cohérence inter-sections (F## référencés existent dans faits_atomiques).
    # Note: la synthese ne contient pas faits_atomiques → H6 n'est applicable qu'à la quintessence.
    if yaml_type == "quintessence" and "faits_atomiques" in data and isinstance(data["faits_atomiques"], list):
        fait_ids = {f["id"] for f in data["faits_atomiques"] if "id" in f}
        for section_name in ("theses_cardinales", "transversalites"):
            if section_name in data and isinstance(data[section_name], list):
                for item in data[section_name]:
                    refs = item.get("f_atomiques_justificatifs", item.get("faits_communs", []))
                    if not isinstance(refs, list):
                        continue
                    for ref in refs:
                        if ref not in fait_ids:
                            messages.append(f"H6: F## '{ref}' référencé dans '{section_name}' mais absent de faits_atomiques")

    passed = len(messages) == 0
    return passed, messages


# --- Clés requises par type YAML ---

QUINTESSENCE_KEYS = [
    "these_centrale",
    "theses_implicites",
    "faits_atomiques",
    "acteurs",
    "causalites",
    "perspectives_dialectiques",
    "limites",
    "wolves",
    "iceberg",
    "chronologie",
    "domaines",
    "urls_prioritaires",
]

SYNTHESE_KEYS = [
    "sujet_majoritaire",
    "theses_cardinales",
    "meta_observations",
    "transversalites",
    "cartes_positions",
    "gaps",
    "shadow_factor_global",
    "mnemo_context",
]


def _type_checks(yaml_type: str) -> dict[str, type]:
    """Retourne les checks de type attendus selon le type de YAML."""
    base = {
        "these_centrale": str,
        "theses_implicites": list,
        "faits_atomiques": list,
        "acteurs": list,
        "causalites": list,
        "perspectives_dialectiques": list,
        "limites": list,
        "wolves": list,
        "iceberg": list,
        "chronologie": list,
        "domaines": list,
        "urls_prioritaires": list,
    }
    if yaml_type == "synthese":
        return {
            "sujet_majoritaire": str,
            "theses_cardinales": list,
            "meta_observations": list,
            "transversalites": list,
            "cartes_positions": list,
            "gaps": list,
            "shadow_factor_global": (int, float),
            "mnemo_context": dict,
        }
    return base
