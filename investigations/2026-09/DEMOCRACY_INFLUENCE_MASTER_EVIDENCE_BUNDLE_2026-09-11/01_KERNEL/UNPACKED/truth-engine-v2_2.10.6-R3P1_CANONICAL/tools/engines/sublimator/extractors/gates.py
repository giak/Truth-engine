"""gates.py — Validation structurelle H0-H7 des quintessences/synthèses.

Sublimator v34 Léger (2026-07-05). Dual-loader JSON/YAML.
Chaque message d'échec est préfixé par le check (H0..H7).

Checks :
- H0 : fichier lisible (JSON/YAML) + erreurs OS explicites ;
- H1 : clés obligatoires (6 quintessence / 7 synthèse) ;
- H2 : types valides (these_centrale / sujet_majoritaire = string) ;
- H3 : glyphes acceptés (✦ ✧ ⁅ ❧) ;
- H4 : IDs de faits uniques ;
- H5 : thèses avec ≥ 3 justificatifs F## (synthèse) ;
- H6 : cohérence inter-sections, F## référencés existent (quintessence) ;
- H7 : string-safety (longueur max + blocklist invisibles) sur champs top-level.
"""

import json
import os

import yaml

# H3 : les 4 glyphes canoniques de fiabilité.
GLYPHS = {"\u2726", "\u2727", "\u2045", "\u2767"}  # ✦ ✧ ⁅ ❧

# H1 : clés obligatoires (schema v35 allégé).
QUINTESSENCE_KEYS = (
    "enquete_id",
    "enquete_source",
    "these_centrale",
    "faits_atomiques",
    "urls_prioritaires",
    "shadow_factor",
)

SYNTHESE_KEYS = (
    "sujet_majoritaire",
    "theses_cardinales",
    "meta_observations",
    "transversalites",
    "gaps",
    "shadow_factor_global",
    "mnemo_context",
)

# H7 : longueur max et caractères invisibles/contrôle bloqués.
H7_MAX_LEN = 10_000
H7_BLOCKLIST = {
    "\x00",      # NUL
    "\u200b",    # zero-width space
    "\u200c",    # zero-width non-joiner
    "\u200d",    # zero-width joiner
    "\u202e",    # RTL override
    "\ufeff",    # BOM / zero-width no-break space
}


def _load_data(path):
    """Charge un fichier JSON (.json) ou YAML (sinon). Lève en cas d'erreur."""
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _check_h7(text, field, msgs):
    """H7 : string-safety sur un champ top-level. Ignore None/non-str (H2 gère le type)."""
    if not isinstance(text, str):
        return
    if len(text) > H7_MAX_LEN:
        msgs.append(f"H7: {field} trop long ({len(text)} > {H7_MAX_LEN})")
    for ch in H7_BLOCKLIST:
        if ch in text:
            msgs.append(f"H7: {field} contient des caractères interdits")
            break


def validate(path, struct_type="quintessence"):
    """Valide un fichier quintessence/synthèse. Retourne (passed, msgs)."""
    # --- H0 : chargement + erreurs OS explicites ---
    if not path:
        return (False, ["H0: Aucun chemin fourni"])
    if os.path.isdir(path):
        return (False, [f"H0: {path} est un répertoire"])
    if not os.path.exists(path):
        return (False, [f"H0: fichier introuvable: {path}"])

    try:
        data = _load_data(path)
    except PermissionError:
        return (False, [f"H0: Permissions insuffisantes sur {path}"])
    except (json.JSONDecodeError, yaml.YAMLError, ValueError, OSError) as e:
        return (False, [f"H0: fichier illisible: {e}"])

    if data is None:
        return (False, ["H0: fichier vide ou invalide"])
    if not isinstance(data, dict):
        return (False, ["H0: le contenu racine doit être un objet"])

    msgs = []
    is_quint = struct_type == "quintessence"

    # --- H1 : clés obligatoires ---
    required = QUINTESSENCE_KEYS if is_quint else SYNTHESE_KEYS
    missing = [k for k in required if k not in data]
    if missing:
        msgs.append(f"H1: clés manquantes: {missing}")

    # --- H2 : types ---
    if is_quint:
        if "these_centrale" in data and not isinstance(data["these_centrale"], str):
            msgs.append("H2: these_centrale doit être une string")
    else:
        if "sujet_majoritaire" in data and not isinstance(data["sujet_majoritaire"], str):
            msgs.append("H2: sujet_majoritaire doit être une string")

    # --- H3 : glyphes ---
    for f in data.get("faits_atomiques", []) or []:
        if isinstance(f, dict) and "glyphe" in f and f["glyphe"] not in GLYPHS:
            msgs.append(f"H3: glyphe invalide: {f['glyphe']!r} (id={f.get('id')})")
            break

    # --- H4 : IDs uniques ---
    ids = [
        f.get("id")
        for f in (data.get("faits_atomiques", []) or [])
        if isinstance(f, dict) and f.get("id") is not None
    ]
    if len(ids) != len(set(ids)):
        msgs.append("H4: IDs de faits dupliqués")

    # --- H5 : thèses ≥ 3 justificatifs (synthèse) ---
    if not is_quint:
        for t in data.get("theses_cardinales", []) or []:
            if isinstance(t, dict):
                justifs = t.get("f_atomiques_justificatifs", []) or []
                if len(justifs) < 3:
                    msgs.append(
                        f"H5: thèse sous-référencée: {t.get('titre', '?')} "
                        f"({len(justifs)} justificatifs)"
                    )

    # --- H6 : cohérence inter-sections (quintessence) ---
    if is_quint:
        fact_ids = set(ids)
        for t in data.get("transversalites", []) or []:
            if isinstance(t, dict):
                for fc in t.get("faits_communs", []) or []:
                    if fc not in fact_ids:
                        msgs.append(f"H6: référence orpheline: {fc}")

    # --- H7 : string-safety (champs top-level) ---
    if is_quint:
        _check_h7(data.get("these_centrale"), "these_centrale", msgs)
    else:
        _check_h7(data.get("sujet_majoritaire"), "sujet_majoritaire", msgs)

    return (not msgs, msgs)
