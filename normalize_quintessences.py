#!/usr/bin/env python3
"""Normalize all quintessence YAMLs to the 'ace' canonical format.

Backs up each file to <original>.backup before overwriting.

Note migration YAML→JSON (2026-07-05) :
    Ce script reste un lecteur pur YAML (utility legacy pour investigations pré-2026-07).
    Pour les nouvelles fiches au format JSON (.json), utiliser plutôt :
    - `tools/scripts/yaml_to_json.py` pour convertir legacy vers JSON
    - directement le pipeline Sublimator v34 (prompt-v34.md format par défaut = JSON)

Compatibilité forward : ce script ignore volontairement les fichiers `.json` (skip) car
la normalization ace format est désormais redondante avec le schema JSON strict imposé par
`tools/engines/sublimator/extractors/gates.py`.

V34.1 cleanup (2026-07-05, coherent avec V4 cleanup de gates.py) :
    Ce script opère uniquement sur des fichiers YAML quintessence. Les champs
    `cartes_positions` ne concernent QUE les synthese (Phase 2), donc ce script
    n'a aucune clé à retirer côté quintessence. La cohérence V4 est respectée par
    absence : aucune référence legacy n'apparaît dans le normalize.
"""
import yaml
import os
import glob
import shutil
import sys

PROJECT_ROOT = "/home/giak/projects/truth-engine"

def find_yamls():
    """Find all _quintessence/*.yaml files."""
    pattern = os.path.join(PROJECT_ROOT, "investigations", "*", "_quintessence", "*_quintessence.yaml")
    return sorted(glob.glob(pattern))

def is_ace_format(d):
    """Check if YAML is already in ace canonical format."""
    faits = d.get("faits_atomiques", [])
    if not faits:
        return False
    f0 = faits[0]
    # ace format has 'glyphe' field
    if "glyphe" in f0:
        return True
    # classe format has 'fiabilite' field
    if "fiabilite" in f0:
        return False
    # projetpol format has 'fait' field
    if "fait" in f0:
        return False
    # Default: assume not ace
    return False

def normalize_faits(faits):
    """Normalize faits_atomiques to ace format: {id, enonce, source_url, source_section, head_status, tier, glyphe}."""
    result = []
    for f in faits:
        entry = {}

        # id
        entry["id"] = f.get("id", "F-UNKNOWN")

        # enonce: may be 'enonce', 'fait', or missing
        entry["enonce"] = f.get("enonce") or f.get("fait") or ""

        # source_url
        entry["source_url"] = f.get("source_url") or f.get("source") or None

        # source_section
        entry["source_section"] = f.get("source_section", "")

        # fiabilite → glyphe, head_status, tier
        fiabilite = f.get("fiabilite")
        glyphe = f.get("glyphe")
        if glyphe and not fiabilite:
            entry["glyphe"] = glyphe
            entry["head_status"] = f.get("head_status", 0)
            entry["tier"] = f.get("tier", 2)
        elif fiabilite:
            entry["glyphe"] = fiabilite
            if fiabilite == "✦":
                entry["head_status"] = 200
                entry["tier"] = 1
            elif fiabilite == "✧":
                entry["head_status"] = 200
                entry["tier"] = 2
            else: # ❧
                entry["head_status"] = 0
                entry["tier"] = 2
        else:
            entry["glyphe"] = "❧"
            entry["head_status"] = 0
            entry["tier"] = 2

        # Preserve note if present
        if "note" in f and f["note"]:
            entry["note"] = f["note"]

        result.append(entry)
    return result

def normalize_acteurs(acteurs):
    """Normalize acteurs to ace format: {nom, role, faits_lies: [...]}."""
    result = []
    for a in acteurs:
        entry = {
            "nom": a.get("nom", "UNKNOWN"),
            "role": a.get("role", ""),
            "faits_lies": a.get("faits_lies", [])
        }
        result.append(entry)
    return result

def normalize_causalites(causalites):
    """Normalize causalites to ace format: {cause, effet, mecanisme} or {chaine} preserved."""
    result = []
    for c in causalites:
        if "cause" in c and "effet" in c and "mecanisme" in c:
            # Already ace format
            result.append({
                "cause": c["cause"],
                "effet": c["effet"],
                "mecanisme": c.get("mecanisme", "")
            })
        elif "causalite" in c:
            # projetpol format: has chaine label + causalite text
            causalite = c.get("causalite", c.get("chaine", ""))
            result.append({
                "cause": None,
                "effet": None,
                "mecanisme": causalite
            })
        elif "chaine" in c:
            # classe format: single chaine string
            chaine = c["chaine"]
            result.append({
                "cause": None,
                "effet": None,
                "mecanisme": chaine
            })
        else:
            # Unknown, preserve as is
            result.append(c)
    return result

def normalize_wolves(wolves):
    """Normalize wolves to ace format: {nom, argument, reponse}."""
    result = []
    for w in wolves:
        if "nom" in w and "argument" in w and "reponse" in w:
            # Already ace format
            result.append(w)
        elif "wolf" in w:
            # classe format: single wolf string
            text = w["wolf"]
            # First sentence as nom, full text as argument
            sentences = text.replace("\n", " ").split(". ")
            nom = sentences[0][:80] + ("..." if len(sentences[0]) > 80 else "")
            result.append({
                "nom": nom.strip(),
                "argument": text,
                "reponse": ""
            })
        else:
            result.append(w)
    return result

def normalize_urls(urls):
    """Normalize urls_prioritaires to ace format: [{url, description, head_status}]."""
    if urls is None:
        return []
    result = []
    for u in urls:
        if isinstance(u, dict):
            if "url" in u:
                result.append({
                    "url": u["url"],
                    "description": u.get("description", u.get("note", "")),
                    "head_status": u.get("head_status", 0)
                })
        elif isinstance(u, str):
            result.append({
                "url": u,
                "description": "",
                "head_status": 0
            })
    return result

def normalize_yaml(d, filepath):
    """Normalize a single YAML dict to ace format."""
    # Normalize faits
    if "faits_atomiques" in d:
        d["faits_atomiques"] = normalize_faits(d["faits_atomiques"])

    # Normalize acteurs
    if "acteurs" in d:
        d["acteurs"] = normalize_acteurs(d["acteurs"])

    # Normalize causalites
    if "causalites" in d:
        d["causalites"] = normalize_causalites(d["causalites"])

    # Normalize wolves
    if "wolves" in d:
        d["wolves"] = normalize_wolves(d["wolves"])

    # Normalize urls_prioritaires
    if "urls_prioritaires" in d or "urls_prioritaires" not in d:
        d["urls_prioritaires"] = normalize_urls(d.get("urls_prioritaires"))

    # Ensure shadow_factor is a number
    if "shadow_factor" in d:
        try:
            d["shadow_factor"] = float(d["shadow_factor"])
        except (ValueError, TypeError):
            d["shadow_factor"] = 2.0

    # Add shadow_justification if missing
    if "shadow_justification" not in d:
        d["shadow_justification"] = ""

    # Ensure mnemo_queries exists
    if "mnemo_queries" not in d:
        d["mnemo_queries"] = [{"note": "Mnemolite DOWN."}]

    # Remove non-ace fields that might confuse
    d.pop("extracteur", None)

    return d

def validate_yaml(d, filepath):
    """Basic validation after normalization."""
    required = [
        "enquete_id", "complexity", "date_extraction", "enquete_source",
        "these_centrale", "theses_implicites", "faits_atomiques",
        "acteurs", "causalites", "perspectives_dialectiques",
        "limites", "wolves", "iceberg", "chronologie", "domaines",
        "urls_prioritaires", "shadow_factor", "mnemo_queries"
    ]
    missing = [k for k in required if k not in d]
    if missing:
        return False, f"MISSING: {missing}"
    return True, "OK"

def write_yaml_preserving_style(filepath, d):
    """Write YAML with block scalar style (>) for long strings."""
    # Use ruamel.yaml if available for better formatting,
    # else fall back to PyYAML
    try:
        from ruamel.yaml import YAML
        ryaml = YAML()
        ryaml.width = 120
        ryaml.default_flow_style = False
        with open(filepath, 'w') as f:
            ryaml.dump(d, f)
    except ImportError:
        # Fallback: PyYAML with custom representer for folded scalars
        with open(filepath, 'w') as f:
            yaml.dump(d, f, allow_unicode=True, default_flow_style=False,
                      sort_keys=False, width=120)

def main():
    yamls = find_yamls()
    print(f"Found {len(yamls)} YAML files")

    already_ace = 0
    normalized = 0
    errors = []

    for fp in yamls:
        rel = os.path.relpath(fp, PROJECT_ROOT)
        try:
            with open(fp, 'r') as f:
                d = yaml.safe_load(f)

            if is_ace_format(d):
                already_ace += 1
                print(f"  ✅ {rel} — already ace format")
                continue

            # Backup
            backup = fp + ".backup"
            shutil.copy2(fp, backup)

            # Normalize
            d = normalize_yaml(d, fp)

            # Validate
            ok, msg = validate_yaml(d, fp)
            if not ok:
                errors.append(f"{rel}: {msg}")
                continue

            # Write
            with open(fp, 'w') as f:
                yaml.dump(d, f, allow_unicode=True, default_flow_style=False,
                          sort_keys=False, width=120)

            normalized += 1
            print(f"  🔄 {rel} — normalized")

        except Exception as e:
            errors.append(f"{rel}: {str(e)}")
            print(f"  ❌ {rel}: {e}")

    print(f"\n=== SUMMARY ===")
    print(f"Already ace format: {already_ace}")
    print(f"Normalized: {normalized}")
    print(f"Errors: {len(errors)}")
    if errors:
        for e in errors:
            print(f"  ❌ {e}")

    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(main())
