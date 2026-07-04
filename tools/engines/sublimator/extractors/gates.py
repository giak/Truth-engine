"""Gates H0-H6 — validation structurelle minimale (Sublimator v34 Léger).

Pas de GATE_G (complétude): le LLM hôte compte ses F## lui-même.
Les 7 checks H0-H6 valident la structure de quintessence/synthese uniquement.

Format supporté (auto-détection par extension depuis 2026-07-05) :
- JSON (.json) : format par défaut, promu pour éviter les bugs LLM sur YAML block-mapping
- YAML (.yaml) : legacy, lecture seule pour rétrocompatibilité investigations pré-2026-07
"""

import json
import yaml
from typing import Any

VALID_GLYPHS: set[str] = {"✦", "✧", "⁅", "❧"}


def _load_data(path: str) -> tuple[Any, str | None]:
    """Charge quintessence ou synthese depuis JSON ou YAML (auto-détection par extension).

    Returns:
        (data, status): data est le dict parsé. status est 'json', 'yaml', 'parse_error: ...'
        ou 'file_not_found' en cas d'échec.
    """
    try:
        if path.endswith(".json"):
            with open(path) as f:
                return json.load(f), "json"
        # Fallback YAML pour rétrocompatibilité legacy
        with open(path) as f:
            return yaml.safe_load(f), "yaml"
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        return None, f"parse_error: {e}"
    except FileNotFoundError:
        return None, "file_not_found"


def validate(
    path: str | None = None,
    struct_type: str = "quintessence",
    *,
    yaml_path: str | None = None,
    yaml_type: str | None = None,
) -> tuple[bool, list[str]]:
    """Valide un fichier (quintessence ou synthese) contre H0-H6.

    Format auto-détecté par extension: `.json` (prioritaire depuis 2026-07-05) ou `.yaml` (legacy).
    Migration v33→v34: les anciens kwargs `yaml_path` / `yaml_type` restent acceptés comme
    alias dépréciés pour rétrocompatibilité (positionnel également supporté).

    Args:
        path: Chemin vers le fichier (JSON ou YAML, auto-détecté).
        struct_type: "quintessence" (12 clés) ou "synthese" (8 clés).
        yaml_path: [DEPRECATED depuis 2026-07-05] ancien nom positionnel/v34-compatible.
        yaml_type: [DEPRECATED depuis 2026-07-05] ancien nom du second paramètre.

    Returns:
        (passed, messages): passed est False si au moins un check échoue.
    """
    # Backward-compat aliases (v33 API: validate(yaml_path, yaml_type))
    if yaml_path is not None:
        path = yaml_path
    if yaml_type is not None:
        struct_type = yaml_type
    if path is None:
        return False, ["H0: Aucun chemin fourni (utilisez `path` ou l'ancien alias `yaml_path`)"]

    messages: list[str] = []

    # H0: fichier parsable
    data, status = _load_data(path)
    if status == "file_not_found":
        return False, [f"H0: Fichier introuvable — {path}"]
    if status and status.startswith("parse_error"):
        fmt = "JSON" if path.endswith(".json") else "YAML"
        return False, [f"H0: {fmt} invalide — {status[len('parse_error: '):]}"]
    if data is None:
        fmt = "JSON" if path.endswith(".json") else "YAML"
        return False, [f"H0: {fmt} invalide (data=None)"]

    if not isinstance(data, dict):
        return False, ["H0: Le fichier est parsable mais ne contient pas un dictionnaire racine"]

    # H1: clés obligatoires
    required_keys = QUINTESSENCE_KEYS if struct_type == "quintessence" else SYNTHESE_KEYS
    missing = [k for k in required_keys if k not in data]
    if missing:
        messages.append(f"H1: Clé(s) manquante(s) — {missing}")

    # H2: types valides
    type_checks = _type_checks(struct_type)
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
                messages.append(f"H4: F## dupliqué — '{fid}' x{count}")

    # H5: chaque thèse a >= 3 F## justificatifs
    if "theses_cardinales" in data and isinstance(data["theses_cardinales"], list):
        for these in data["theses_cardinales"]:
            titre = these.get("titre", these.get("enonce", "?"))
            justifs = these.get("f_atomiques_justificatifs", [])
            if len(justifs) < 3:
                messages.append(f"H5: Thèse '{titre}' a {len(justifs)} F## justificatifs (min 3)")

    # H6: cohérence inter-sections (F## référencés existent dans faits_atomiques).
    # Note: la synthese ne contient pas faits_atomiques -> H6 n'est applicable qu'à la quintessence.
    if struct_type == "quintessence" and "faits_atomiques" in data and isinstance(data["faits_atomiques"], list):
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


# --- Clés requises par type de structure ---

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


def _type_checks(struct_type: str) -> dict[str, type]:
    """Retourne les checks de type attendus selon le type de structure."""
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
    if struct_type == "synthese":
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
