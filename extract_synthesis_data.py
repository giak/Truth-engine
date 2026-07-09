#!/usr/bin/env python3
"""
Phase 2 — Extraction agregee des 25 quintessences.
Produit un JSON synthetique pour le thinker agent.

Note migration YAML→JSON (2026-07-05) :
    Ce script reste un lecteur pur YAML (output JSON pour le thinker).
    Pour traiter les nouvelles fiches au format JSON (.json), les convertir au prealable via
    `tools/scripts/yaml_to_json.py`, ou bien adapter `load_yamls()` pour un dual-loader
    JSON+YA ML aligné sur le pattern `_load_data()` de `tools/engines/sublimator/extractors/gates.py`.
"""
import yaml
import json
import glob
import os
from collections import Counter, defaultdict

PROJECT_ROOT = "/home/giak/projects/truth-engine"

def load_yamls():
    patterns = [
        "investigations/2026-06/2026-06-10_*/_quintessence/*_quintessence.yaml",
        "investigations/2026-06/2026-06-11_*/_quintessence/*_quintessence.yaml",
        "investigations/2026-06/2026-06-12_*/_quintessence/*_quintessence.yaml",
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(os.path.join(PROJECT_ROOT, p)))

    yamls = {}
    for fp in sorted(files):
        try:
            with open(fp) as f:
                d = yaml.safe_load(f)
            yamls[d["enquete_id"]] = d
        except Exception as e:
            print(f"SKIP {fp}: {e}", file=__import__('sys').stderr)
    return yamls

def extract_core(yamls):
    """Extract theses centrales, key metrics."""
    theses = {}
    for id_, d in yamls.items():
        theses[id_] = {
            "these": d.get("these_centrale", "")[:300],
            "complexity": d.get("complexity", "?"),
            "shadow": d.get("shadow_factor", 0),
            "n_faits": len(d.get("faits_atomiques", [])),
        }
    return theses

def extract_actors(yamls):
    """Cross-dossier actor analysis."""
    actor_dossiers = defaultdict(list)
    for id_, d in yamls.items():
        for a in d.get("acteurs", []):
            nom = a.get("nom", "")
            if nom:
                actor_dossiers[nom].append(id_)
    # Sort by recurrence
    return {k: v for k, v in sorted(actor_dossiers.items(), key=lambda x: -len(x[1]))}

def extract_causal_chains(yamls):
    """Extract all causal chains and detect shared patterns."""
    chains = []
    for id_, d in yamls.items():
        for c in d.get("causalites", []):
            mecanisme = c.get("mecanisme", "")
            chains.append({
                "dossier": id_,
                "cause": c.get("cause", ""),
                "effet": c.get("effet", ""),
                "mecanisme": mecanisme[:200],
            })
    return chains

def extract_themes(yamls):
    """Aggregate domaines, iceberg, wolves, and implicit theses."""
    all_domaines = Counter()
    all_iceberg = []
    all_wolves = []
    all_theses_impl = []

    for id_, d in yamls.items():
        for dom in d.get("domaines", []):
            all_domaines[dom.strip()] += 1
        for ice in d.get("iceberg", []):
            item = ice.get("item", ice) if isinstance(ice, dict) else ice
            all_iceberg.append({"dossier": id_, "item": str(item)[:200]})
        for w in d.get("wolves", []):
            arg = w.get("argument", w.get("wolf", ""))
            all_wolves.append({"dossier": id_, "argument": str(arg)[:200]})
        for ti in d.get("theses_implicites", []):
            texte = ti.get("texte", "") if isinstance(ti, dict) else str(ti)
            all_theses_impl.append({"dossier": id_, "texte": texte[:200]})

    return {
        "domaines": dict(all_domaines.most_common(30)),
        "iceberg_items": all_iceberg,
        "wolves": all_wolves,
        "theses_implicites": all_theses_impl,
    }

def detect_transversalites(actor_dossiers):
    """Actors cited in >= 3 dossiers."""
    transversal = {}
    for nom, dossiers in actor_dossiers.items():
        if len(dossiers) >= 3:
            transversal[nom] = dossiers
    return transversal

def glyph_stats(yamls):
    """Glyph distribution across all YAMLs."""
    stats = Counter()
    for id_, d in yamls.items():
        for f in d.get("faits_atomiques", []):
            stats[f.get("glyphe", "❧")] += 1
    return dict(stats)

def main():
    yamls = load_yamls()
    print(f"Loaded {len(yamls)} YAMLs", file=__import__('sys').stderr)

    theses = extract_core(yamls)
    actors = extract_actors(yamls)
    chains = extract_causal_chains(yamls)
    themes = extract_themes(yamls)
    transversal = detect_transversalites(actors)

    output = {
        "meta": {
            "n_yamls": len(yamls),
            "n_faits_total": sum(len(d.get("faits_atomiques", [])) for d in yamls.values()),
            "n_acteurs_uniques": len(actors),
            "glyphes": glyph_stats(yamls),
            "complexities": Counter(d.get("complexity", "?") for d in yamls.values()),
            "shadow_moyen": round(sum(d.get("shadow_factor", 0) for d in yamls.values()) / len(yamls), 2),
        },
        "theses_centrales": theses,
        "acteurs_transversaux": transversal,
        "acteurs_top20": {k: v for k, v in list(actors.items())[:20]},
        "domaines_top": themes["domaines"],
        "causal_chains": chains,
        "iceberg_sample": themes["iceberg_items"][:30],
        "wolves_sample": themes["wolves"][:20],
        "theses_implicites_sample": themes["theses_implicites"][:30],
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
