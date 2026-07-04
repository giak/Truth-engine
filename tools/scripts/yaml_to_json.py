#!/usr/bin/env python3
"""Utility opt-in : convertit un fichier quintessence/synthese YAML en JSON.

Usage :
    python3 tools/scripts/yaml_to_json.py <path>.yaml [output.json]
    python3 tools/scripts/yaml_to_json.py investigations/<sujet>/_quintessence/*.yaml
    python3 tools/scripts/yaml_to_json.py -r investigations/<sujet>/_quintessence/

Note forensique :
    Ce script n'est PAS exécuté automatiquement par le pipeline.
    Il documente le format de conversion depuis la migration YAML→JSON (2026-07-05).
    Il préserve 100% du contenu (les seuls changements : indent=2 + ensure_ascii=False).
    Les commentaires YAML (qui n'ont pas d'équivalent JSON) sont SUPPRIMÉS à dessein :
    JSON ne supporte pas les commentaires, et le pipeline n'en a pas besoin.

Routes de sérialisation :
    - str champ : préservé tel quel (UTF-8)
    - list de dict : préservé
    - shadow_factor (float) : préservé
    - boolean (mode_degrade, cross_series_detected) : préservé

Mnemolite write_memory :
    Le prompt-v34 (depuis 2026-07-05) recommande désormais `content="<JSON sérialisé>"`
    plutôt que `content="<YAML>"`. Utiliser ce script avant indexation Mnemolite pour les
    investigations antérieures.
"""

import json
import os
import sys

import yaml


def convert(yaml_path: str, json_path: str | None = None) -> str:
    """Charge YAML, écrit JSON. Préserve le contenu (UTF-8, indent=2)."""
    if json_path is None:
        if yaml_path.endswith(".yaml"):
            json_path = yaml_path[:-5] + ".json"
        elif yaml_path.endswith(".yml"):
            json_path = yaml_path[:-4] + ".json"
        else:
            json_path = yaml_path + ".json"

    with open(yaml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError(f"{yaml_path}: racine YAML n'est pas un dict (type={type(data).__name__})")

    # Sérialisation UTF-8, indent=2, preserve_unicode (pas d'échappement \uXXXX)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")

    return json_path


def main():
    if len(sys.argv) < 2:
        print("Usage :")
        print("  python3 yaml_to_json.py <path>.yaml [output.json]")
        print("  python3 yaml_to_json.py <path1>.yaml <path2>.yaml ...")
        sys.exit(1)

    inputs = sys.argv[1:]
    converted = []
    errors = []

    for input_path in inputs:
        if not os.path.exists(input_path):
            errors.append(f"introuvable : {input_path}")
            continue
        try:
            out = convert(input_path)
            converted.append((input_path, out))
            print(f"converti : {input_path} -> {out}")
        except Exception as e:
            errors.append(f"{input_path} : {e}")

    print()
    print(f"=== SUMMARY ===")
    print(f"Convertis : {len(converted)}")
    print(f"Erreurs : {len(errors)}")
    for e in errors:
        print(f"  ERREUR : {e}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
