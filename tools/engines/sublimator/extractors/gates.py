"""Gates H0-H7 — validation structurelle minimale (Sublimator v34 Léger).

Pas de GATE_G (complétude): le LLM hôte compte ses F## lui-même.
Les 8 checks H0-H7 valident la structure de quintessence/synthese uniquement.

Format supporté (auto-détection par extension depuis 2026-07-05) :
- JSON (.json) : format par défaut, promu pour éviter les bugs LLM sur YAML block-mapping
- YAML (.yaml) : legacy, lecture seule pour rétrocompatibilité investigations pré-2026-07

v34.1 (2026-07-05) — cleanup V4 :
- `cartes_positions` retiré de `SYNTHESE_KEYS` et `_type_checks()` pour `synthese`
  (clé legacy trop spécifique au cas Sumer, jamais récurrente).
- Aliases dépréciés `yaml_path` / `yaml_type` retirés de `validate()`.
  Tout ancien appel `validate(yaml_path=..., yaml_type=...)` lève désormais `TypeError`.

v34.1.2 (2026-07-05) — hardening F1+F2 (audit antagoniste) :
- F1 : try/except OSError (IsADirectoryError, PermissionError) dans `_load_data()`.
  Messages H0 explicites (file_not_found, is_a_directory, permission_denied, os_error).
- F2 : H7 string-safety sur `these_centrale` (quintessence) et `sujet_majoritaire` (synthese).
  - Longueur max 10 000 chars (10 KB).
  - Blocklist caractères invisibles : NUL (\\x00), zero-width (\\u200b/\\u200c/\\u200d),
    bidi control (\\u202a-\\u202e), BOM (\\ufeff).
"""

import json
import re
import yaml
from typing import Any

VALID_GLYPHS: set[str] = {"✦", "✧", "⁅", "❧"}

# H7 string-safety constants (F2 hardening)
MAX_STR_LEN: int = 10_000
# Blocklist : caractères invisibles / control dangereux
FORBIDDEN_CHARS = re.compile(r"[\x00\u200b\u200c\u200d\u202a-\u202e\ufeff]")
# Champs string top-level à valider (F2 scope : ces deux-là uniquement)
STRING_FIELDS: dict[str, list[str]] = {
    "quintessence": ["these_centrale"],
    "synthese": ["sujet_majoritaire"],
}


def _load_data(path: str) -> tuple[Any, str | None]:
    """Charge quintessence ou synthese depuis JSON ou YAML (auto-détection par extension).

    Returns:
        (data, status): data est le dict parsé. status est 'json', 'yaml',
        'parse_error: ...', 'file_not_found', 'is_a_directory',
        'permission_denied', ou 'os_error: ...' en cas d'échec.
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
    except IsADirectoryError:
        return None, "is_a_directory"
    except PermissionError:
        return None, "permission_denied"
    except FileNotFoundError:
        return None, "file_not_found"
    except OSError as e:
        return None, f"os_error: {e}"


def _check_string_safety(data: dict, struct_type: str) -> list[str]:
    """H7 : longueur max 10 KB + blocklist caractères invisibles (F2 hardening)."""
    msgs: list[str] = []
    for field in STRING_FIELDS.get(struct_type, []):
        v = data.get(field)
        if not isinstance(v, str):
            continue  # H2 catch le type
        if len(v) > MAX_STR_LEN:
            msgs.append(
                f"H7: '{field}' trop long : {len(v)} chars (max {MAX_STR_LEN})"
            )
        bad = sorted(set(FORBIDDEN_CHARS.findall(v)))
        if bad:
            uniq = [repr(c) for c in bad]
            msgs.append(
                f"H7: '{field}' contient des caractères interdits : {uniq[:5]}"
            )
    return msgs


def validate(
    path: str | None = None,
    struct_type: str = "quintessence",
) -> tuple[bool, list[str]]:
    """Valide un fichier (quintessence ou synthese) contre H0-H7.

    Format auto-détecté par extension: `.json` (prioritaire depuis 2026-07-05) ou `.yaml` (legacy).
    v34.1 (2026-07-05) : alias `yaml_path`/`yaml_type` retirés. Si ancien code les passe,
    Python lève `TypeError: validate() got an unexpected keyword argument`.

    Args:
        path: Chemin vers le fichier (JSON ou YAML, auto-détecté).
        struct_type: "quintessence" (12 clés) ou "synthese" (7 clés — `cartes_positions` retiré en v34.1).

    Returns:
        (passed, messages): passed est False si au moins un check échoue.
    """
    if path is None or path == "":
        return False, ["H0: Aucun chemin fourni (paramètre `path`)"]

    messages: list[str] = []

    # H0: fichier parsable
    data, status = _load_data(path)
    if status == "file_not_found":
        return False, [f"H0: Fichier introuvable : {path}"]
    if status == "is_a_directory":
        return False, [f"H0: Le chemin pointe vers un répertoire, pas un fichier : {path}"]
    if status == "permission_denied":
        return False, [f"H0: Permissions insuffisantes pour lire : {path}"]
    if status and status.startswith("os_error"):
        return False, [f"H0: Erreur OS : {status}"]
    if status and status.startswith("parse_error"):
        fmt = "JSON" if path.endswith(".json") else "YAML"
        return False, [f"H0: {fmt} invalide : {status[len('parse_error: '):]}"]
    if data is None:
        fmt = "JSON" if path.endswith(".json") else "YAML"
        return False, [f"H0: {fmt} invalide (data=None)"]

    if not isinstance(data, dict):
        return False, ["H0: Le fichier est parsable mais ne contient pas un dictionnaire racine"]

    # H1: cles obligatoires (v35 alignement prompt)
    # REQUIRED_* = 6 (quintessence) / 7 (synthese) - BLOQUANT.
    # QUINTESSENCE_KEYS / SYNTHESE_KEYS conserves pour retro-compat (info).
    if struct_type == "quintessence":
        required_keys = REQUIRED_QUINTESSENCE_KEYS
    else:
        required_keys = REQUIRED_SYNTHESE_KEYS
    missing = [k for k in required_keys if k not in data]
    if missing:
        messages.append(f"H1: Cle(s) requise(s) manquante(s) : {missing}")

    # H2: types valides
    type_checks = _type_checks(struct_type)
    for key, expected_type in type_checks.items():
        if key in data and not isinstance(data[key], expected_type):
            messages.append(f"H2: Type invalide pour '{key}' : attendu {expected_type.__name__}, reçu {type(data[key]).__name__}")

    # H3: glyphes valides (seulement si faits_atomiques présent)
    if "faits_atomiques" in data and isinstance(data["faits_atomiques"], list):
        for fait in data["faits_atomiques"]:
            gid = fait.get("id", "?")
            glyphe = fait.get("glyphe", "")
            if glyphe not in VALID_GLYPHS:
                messages.append(f"H3: Glyphe invalide pour '{gid}' : '{glyphe}' (attendu ✦/✧/⁅/❧)")

    # H4: IDs uniques
    if "faits_atomiques" in data and isinstance(data["faits_atomiques"], list):
        seen: dict[str, int] = {}
        for fait in data["faits_atomiques"]:
            fid = fait.get("id", "")
            if fid:
                seen[fid] = seen.get(fid, 0) + 1
        for fid, count in seen.items():
            if count > 1:
                messages.append(f"H4: F## dupliqué : '{fid}' x{count}")

    # H5: chaque thèse a >= 3 F## justificatifs
    if "theses_cardinales" in data and isinstance(data["theses_cardinales"], list):
        for these in data["theses_cardinales"]:
            titre = these.get("titre", these.get("enonce", "?"))
            justifs = these.get("f_atomiques_justificatifs", [])
            if len(justifs) < 3:
                messages.append(f"H5: Thèse '{titre}' a {len(justifs)} F## justificatifs (min 3)")

    # H6: cohérence inter-sections (F## référencés existent dans faits_atomiques).
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

    # H7: string safety (F2 hardening)
    messages.extend(_check_string_safety(data, struct_type))

    passed = len(messages) == 0
    return passed, messages


# --- Clés requises par type de structure (v35 alignement prompt) ---
# v35.0 (2026-07-05) : schema allege. REQUIRED_* (6 quintessence, 7 synthese) sont les
# cles BLOQUANTES pour H1 (validation stricte). QUINTESSENCE_KEYS / SYNTHESE_KEYS
# conserves comme listes informatives de toutes les cles possibles (12/7).

REQUIRED_QUINTESSENCE_KEYS = [
    "enquete_id",       # str : identifiant unique de l'enquete (ex: "ric_def")
    "enquete_source",   # str : chemin relatif vers le fichier INVESTIGATION.md
    "these_centrale",   # str : these en une phrase
    "faits_atomiques",  # list : >= 10 faits avec id + enonce + glyphe
    "urls_prioritaires",  # list : >= 1 URL avec head_status
    "shadow_factor",    # float : 1.0-5.0
]

REQUIRED_SYNTHESE_KEYS = [
    "sujet_majoritaire",   # str
    "theses_cardinales",   # list : 3-5 theses (v35) ou 15 (v34 legacy)
    "meta_observations",   # list
    "transversalites",     # list
    "gaps",                # list
    "shadow_factor_global",  # float
    "mnemo_context",       # dict
]

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

# v34.1 : SYNTHESE_KEYS passe de 8 a 7 cles. cartes_positions retire (legacy case Sumer).
SYNTHESE_KEYS = [
    "sujet_majoritaire",
    "theses_cardinales",
    "meta_observations",
    "transversalites",
    "gaps",
    "shadow_factor_global",
    "mnemo_context",
]


def _type_checks(struct_type: str) -> dict[str, type]:
    """Retourne les checks de type attendus selon le type de structure (v35).

    Check uniquement les cles PRESENTES dans le data (les 6 requises + les optionnelles
    si le pilote les a fournies). Ne fail pas si une optionnelle est absente.
    """
    base = {
        # Requises (v35) - 6 cles
        "enquete_id": str,
        "enquete_source": str,
        "these_centrale": str,
        "faits_atomiques": list,
        "urls_prioritaires": list,
        "shadow_factor": (int, float),
        # Optionnelles (v35) - 6 cles
        "theses_implicites": list,
        "acteurs": list,
        "causalites": list,
        "perspectives_dialectiques": list,
        "limites": list,
        "wolves": list,
        "iceberg": list,
        "chronologie": list,
        "domaines": list,
        "mnemo_queries": list,
    }
    if struct_type == "synthese":
        return {
            "sujet_majoritaire": str,
            "theses_cardinales": list,
            "meta_observations": list,
            "transversalites": list,
            "gaps": list,
            "shadow_factor_global": (int, float),
            "mnemo_context": dict,
        }
    return base
