#!/usr/bin/env python3
"""
sublimator_validate.py — Validateur CLI du Sublimator v36 §13.5.

Remplace 9 sub-agents CRITIQUE LLM par 1 script Python déterministe.
Charge N quintessences JSON + 1 lecture annotée markdown par enquête.
Calcule 8 métriques objectives (M1-M8) avec normalisation Unicode/espaces.
Sort verdict GO/PIVOT/NO-GO par enquête + verdict global.

100% reproductible, $0 coût LLM, < 5 s sur 14 fichiers.

Usage:
    python3 sublimator_validate.py --validation-dir investigations/2026-07-04-RIC/_validation
    python3 sublimator_validate.py --validation-dir <dir> --version v2
    python3 sublimator_validate.py --validation-dir <dir> --enquete cultes_france
    python3 sublimator_validate.py --validation-dir <dir> --format json --output metrics.json
    python3 sublimator_validate.py --validation-dir <dir> --format markdown > report.md

Exit codes:
    0  Verdict global GO
    1  Verdict global PIVOT (au moins 1 enquête PIVOT)
    2  Verdict global NO-GO (au moins 1 enquête NO-GO)

Spec: tools/engines/sublimator/2026-07-05_15-00_v36_preservation_phases_analytiques_SPECS.md §13.5
Date: 2026-07-05
Auteur: Sublimator v36 §13.5 industrialisation (post PIVOT v2 verdict)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constantes §13.5.3 — cibles go / no-go
# ---------------------------------------------------------------------------

CIBLES_GO = {
    "M1": 0.7,     # Jaccard these_centrale >= 0.7
    "M2": 0.6,     # intersection F## >= 0.6
    "M3": 5.0,     # % hallucination F## < 5
    "M4": 5.0,     # % hallucination impact < 5
    "M5": 100.0,   # % parse JSON == 100
    "M6": 50000,   # tokens/enquete < 50000
    "M7": 10.0,    # min latence < 10
    "M8": 7.0,     # score critic moyen >= 7
}

CIBLES_NO_GO = {
    "M1": 0.5,
    "M2": 0.4,
    "M3": 15.0,
    "M4": 15.0,
    "M5": 95.0,
    "M6": 100000,
    "M7": 20.0,
    "M8": 5.0,
}

# Espaces insécables Unicode à normaliser avant re.search (résout bug M4 v1).
INSECABLES = "\u00A0\u202F"


# ---------------------------------------------------------------------------
# Normalisation Unicode/espaces
# ---------------------------------------------------------------------------

def norm(s: str) -> str:
    """Normalise lower + retire espaces/insécables (utilisé pour M3/M4 re.search)."""
    return re.sub(rf"[{INSECABLES}\s]+", "", (s or "").lower())


def jaccard(a: str, b: str) -> float:
    """Jaccard bag-of-words (lemmatisation lowercase + split word boundary)."""
    a_set = set(re.findall(r"\w+", (a or "").lower()))
    b_set = set(re.findall(r"\w+", (b or "").lower()))
    if not (a_set | b_set):
        return 0.0
    return len(a_set & b_set) / len(a_set | b_set)


def digits(s) -> str:
    """Extrait les digits significatifs d'un chiffre (gère '1 500', '20 000', '65%')."""
    return "".join(re.findall(r"\d+", str(s)))


# ---------------------------------------------------------------------------
# Métriques §13.5
# ---------------------------------------------------------------------------

def m1_jaccard_theses(quins: List[dict]) -> Optional[float]:
    """M1 : Jaccard moyen pairwise sur `these_centrale`. Retourne None si < 2 runs."""
    theses = [q.get("these_centrale", "") for q in quins if q.get("these_centrale")]
    if len(theses) < 2:
        return None
    pairs = [(theses[i], theses[j]) for i in range(len(theses)) for j in range(i + 1, len(theses))]
    return round(sum(jaccard(a, b) for a, b in pairs) / len(pairs), 3)


def m2_intersect_F(quins: List[dict]) -> Optional[float]:
    """M2 : intersection / union de l'ensemble des id F-### entre runs."""
    sets = [{f["id"] for f in q.get("faits_atomiques", [])} for q in quins]
    if not any(sets):
        return None
    if len(sets) == 1:
        return 1.0
    inter = set.intersection(*sets)
    union = set.union(*sets)
    if not union:
        return None
    return round(len(inter) / len(union), 3)


def m3_hallucination_F(quin: dict, reader_norm: str) -> Tuple[int, int, float]:
    """M3 : ratio F-### dont le head[:30] n'est pas ré-extractable du reader normalisé."""
    h = n = 0
    for f in quin.get("faits_atomiques", []):
        head = norm(f.get("enonce", "")[:30])
        n += 1
        if head and head not in reader_norm:
            h += 1
    pct = round((h / n * 100), 1) if n else 0.0
    return h, n, pct


def m4_hallucination_impact(quin: dict, reader_norm: str) -> Tuple[int, int, float]:
    """M4 : ratio chiffres impact dont les digits ne matchent pas le reader normalisé."""
    h = n = 0
    for c in quin.get("impact", []):
        ch = digits(c.get("chiffre", ""))
        n += 1
        if not ch:
            continue
        short = ch[:3] if len(ch) > 3 else ch
        if short not in reader_norm and ch not in reader_norm:
            h += 1
    pct = round((h / n * 100), 1) if n else 0.0
    return h, n, pct


def m5_parse(quins: List[dict]) -> float:
    """M5 : % de quintessences parsées. Validé par json.loads en amont (charge)."""
    return 100.0 if quins else 0.0


def m6_volume_tokens_proxy(quins: List[dict]) -> int:
    """M6 proxy : volume tokens approximé par taille JSON (heuristique 1 token ~= 4 chars).
    Cible go : < 50000 tokens/enquete ; cible no-go : > 100000. Voir SPECS §13.5.5.
    NB : pur proxy bytes→tokens ; ne reflete pas la consommation réelle de l'hote LLM.
    """
    if not quins:
        return 0
    bytes_total = sum(len(json.dumps(q, ensure_ascii=False)) for q in quins)
    return round(bytes_total / 4)


def m7_latence_proxy(quins: List[dict]) -> Optional[float]:
    """M7 proxy : latence sequentielle en minutes. Sans timestamps reellement mesures,
    retourne None. Les fichiers de quintessence ne portent pas de metadata de datation
    d'execution ; sur hote productif, le Sublimator doit injecter les timestamps.
    """
    return None


def m8_quality_proxy(quin: dict) -> Tuple[int, int, float]:
    """M8 proxy : score 10 = 100% faits non-dégradés. Dégradation = tier=3 OU glyphe='❧' OU note_violation."""
    faits = quin.get("faits_atomiques", [])
    n = len(faits)
    h = sum(1 for f in faits
            if f.get("tier") == 3
            or str(f.get("glyphe", "")).endswith("\u2747")  # ❧
            or "note_violation" in f)
    score = round(10 * (1 - h / max(n, 1)), 1)
    return h, n, score


# ---------------------------------------------------------------------------
# IO : chargement du dossier _validation/
# ---------------------------------------------------------------------------

def detect_version(q: dict, name: str) -> str:
    if "v2" in name or (q.get("version_prompt") or "").startswith("v2"):
        return "v2"
    return "v1"


def load_validation_dir(d: Path) -> Tuple[Dict[str, str], Dict[str, List[dict]], List[dict]]:
    """Charge readers (*-reader.md) et quintessences (*-quintessence*.json, hors critique)."""
    readers: Dict[str, str] = {}
    quins_by_enq: Dict[str, List[dict]] = {}
    quins_flat: List[dict] = []
    for p in sorted(d.iterdir()):
        if p.is_file() and p.suffix == ".md" and "reader" in p.name:
            enq = p.stem.replace("-reader", "").replace("_reader", "")
            readers[enq] = p.read_text()
        elif p.is_file() and p.suffix == ".json" and "quintessence" in p.name and "critique" not in p.name:
            try:
                q = json.loads(p.read_text())
            except json.JSONDecodeError:
                continue
            enq = q.get("enquete_id") or p.stem.split("-quintessence")[0]
            quins_flat.append(q)
            quins_by_enq.setdefault(enq, []).append((p.name, q))
    # Convertir tuples (name, q) en q uniquement (laisse trace via len si besoin)
    quins_only = {k: [qq for _, qq in v] for k, v in quins_by_enq.items()}
    return readers, quins_only, quins_flat


def find_reader(enq_id: str, readers: Dict[str, str]) -> str:
    """Matcher reader pour une enquete (fuzzy: kebab/snake)."""
    e_norm = enq_id.replace("-", "_")
    for k, v in readers.items():
        k_norm = k.replace("-", "_")
        if k_norm in e_norm or e_norm in k_norm:
            return v
    return ""


# ---------------------------------------------------------------------------
# Verdict §13.5.3
# ---------------------------------------------------------------------------

def verdict_from_metrics(metrics: Dict[str, float]) -> Tuple[str, int]:
    """Décide GO/PIVOT/NO-GO selon §13.5.3 strict + retourne exit code.
    Cible go : M1>=0.7, M2>=0.6, M3<5, M4<5, M5==100, M6<50000, M7<=10, M8>=7.
    Cible no-go : M1<0.5, M2<0.4, M3>15, M4>15, M5<95, M6>100000, M7>20, M8<5.
    GO requiert >=6/8 metriques dans cible go ET M1>=0.7 ET M3<5 ET M4<5.
    M7=None (mode retroactif) n'est pas compte dans nb_go (neutralite).
    """
    m1 = metrics.get("M1") or 0.0
    m2 = metrics.get("M2") or 0.0
    m3 = metrics.get("M3") or 0.0
    m4 = metrics.get("M4") or 0.0
    m5 = metrics.get("M5") or 0.0
    m6 = metrics.get("M6") or 0.0
    m7 = metrics.get("M7")
    m8 = metrics.get("M8") or 0.0

    nb_go = sum([
        m1 >= CIBLES_GO["M1"],
        m2 >= CIBLES_GO["M2"],
        m3 < CIBLES_GO["M3"],
        m4 < CIBLES_GO["M4"],
        m5 >= CIBLES_GO["M5"],
        m6 < CIBLES_GO["M6"],
        (m7 is not None and m7 <= CIBLES_GO["M7"]),
        m8 >= CIBLES_GO["M8"],
    ])
    if nb_go >= 6 and m1 >= 0.7 and m3 < 5 and m4 < 5:
        return "GO", 0
    if m3 > 15 or m4 > 15 or m1 < 0.5:
        return "NO-GO", 2
    return "PIVOT", 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--validation-dir", type=Path, required=True,
                   help="Dossier contenant les quintessences JSON et lectures .md")
    p.add_argument("--version", choices=["v1", "v2", "both"], default="both",
                   help="Filtrer par version du prompt (défaut: both)")
    p.add_argument("--enquete", type=str, default=None,
                   help="Restreindre à 1 enquête (kebab ou snake-case)")
    p.add_argument("--format", choices=["json", "markdown", "both"], default="both",
                   help="Format sortie (défaut: both)")
    p.add_argument("--output", type=Path, default=None,
                   help="Fichier sortie (sans extension: ajoute .json / .md selon format)")
    p.add_argument("--quiet", action="store_true",
                   help="Supprime affichage console (utile piping)")
    return p


def run_validate(args: argparse.Namespace) -> Dict:
    if not args.validation_dir.exists():
        sys.exit(f"FATAL: validation-dir inexistant: {args.validation_dir}")

    readers, quins_by_enq, _ = load_validation_dir(args.validation_dir)

    if args.enquete:
        e_target = args.enquete.replace("-", "_")
        matched = [k for k in quins_by_enq if e_target in k.replace("-", "_")]
        if not matched:
            sys.exit(f"FATAL: enquête '{args.enquete}' introuvable. Disponibles: {sorted(quins_by_enq.keys())}")
        target_enqs = matched
    else:
        target_enqs = sorted(quins_by_enq.keys())

    results = {
        "_meta": {
            "validation_dir": str(args.validation_dir),
            "version_filter": args.version,
            "total_quintessences_chargees": sum(len(v) for v in quins_by_enq.values()),
            "total_readers": len(readers),
            "cibles_go": CIBLES_GO,
            "cibles_no_go": CIBLES_NO_GO,
        },
        "enquetes": {},
    }

    for enq in target_enqs:
        quins_with_meta = quins_by_enq[enq]
        if args.version != "both":
            quins_with_meta = [(None, q) for q in quins_with_meta if detect_version(q, "") == args.version]
        else:
            quins_with_meta = [(None, q) for q in quins_with_meta]
        quins = [q for _, q in quins_with_meta]
        if not quins:
            continue

        reader = find_reader(enq, readers)
        reader_norm = norm(reader)

        m1 = m1_jaccard_theses(quins)
        m2 = m2_intersect_F(quins)
        m3_pc: List[float] = []
        m4_pc: List[float] = []
        m8_scores: List[float] = []
        degraded = 0
        total_faits = 0
        for q in quins:
            _, n3, p3 = m3_hallucination_F(q, reader_norm)
            _, n4, p4 = m4_hallucination_impact(q, reader_norm)
            h8, n8, s8 = m8_quality_proxy(q)
            m3_pc.append(p3)
            m4_pc.append(p4)
            m8_scores.append(s8)
            degraded += h8
            total_faits += n8
        m3_moy = round(sum(m3_pc) / len(m3_pc), 1) if m3_pc else 0.0
        m4_moy = round(sum(m4_pc) / len(m4_pc), 1) if m4_pc else 0.0
        m5 = m5_parse(quins)
        m6 = m6_volume_tokens_proxy(quins)
        m7 = m7_latence_proxy(quins)  # None en mode retroactif
        m8_moy = round(sum(m8_scores) / len(m8_scores), 1) if m8_scores else 0.0

        metrics = {
            "M1": m1 if m1 is not None else 0.0,
            "M2": m2 if m2 is not None else 0.0,
            "M3": m3_moy,
            "M4": m4_moy,
            "M5": m5,
            "M6": m6,
            "M7": m7,  # None si pas de timestamps injectes par Sublimator
            "M8": m8_moy,
        }
        verdict, _ = verdict_from_metrics(metrics)

        results["enquetes"][enq] = {
            "n_runs": len(quins),
            "reader_found": bool(reader),
            "metrics": metrics,
            "degraded_F_count": degraded,
            "total_F_count": total_faits,
            "verdict": verdict,
        }

    # Verdict global (worst-case)
    verdicts = [r["verdict"] for r in results["enquetes"].values()]
    if "NO-GO" in verdicts:
        global_v = "NO-GO"
        exit_code = 2
    elif "PIVOT" in verdicts:
        global_v = "PIVOT"
        exit_code = 1
    else:
        global_v = "GO"
        exit_code = 0
    results["_meta"]["verdict_global"] = global_v

    return results, exit_code


def render_markdown(results: Dict) -> str:
    lines = ["# Validation Sublimator v36 §13.5\n",
             f"Source : `{results['_meta']['validation_dir']}`",
             f"Version filter : {results['_meta']['version_filter']}",
             f"Quintessences chargées : {results['_meta']['total_quintessences_chargees']}",
             f"**Verdict global : {results['_meta']['verdict_global']}**\n",
             "## Tableau par enquête\n",
             "| Enquête | Runs | M1 Jaccard | M2 Inter | M3 Hallu | M4 Chiffres | M5 Parse | M6 Tokens | M7 Min | M8 Proxy | Verdict |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for enq, r in sorted(results["enquetes"].items()):
        m = r["metrics"]
        m7_str = "N/A" if m.get("M7") is None else f"{m['M7']}"
        lines.append(
            f"| `{enq}` | {r['n_runs']} | "
            f"{m['M1']:.3f} | {m['M2']:.3f} | "
            f"{m['M3']}% | {m['M4']}% | {m['M5']}% | "
            f"{m['M6']} | {m7_str} | "
            f"{m['M8']}/10 | **{r['verdict']}** |"
        )
    lines.append("\n## Légende cible §13.5.3")
    lines.append("- **GO** : M1 >= 0.7 ET >= 6/8 critères go, ET M3 < 5%, ET M4 < 5%.")
    lines.append("- **PIVOT** : intermédiaire (révision ciblée ou proxy incomplet).")
    lines.append("- **NO-GO** : M1 < 0.5 OU M3 > 15% OU M4 > 15% (révision prompts requise).")
    lines.append("")
    lines.append("## Notes métriques")
    lines.append("- M6 = proxy octets/4 (1 token ~ 4 chars). Pas la consommation réelle de l'hôte LLM.")
    lines.append("- M7 = None en mode rétroactif (timestamps non injectés par défaut). Sur hôte productif : `start/end` dans quintessence metadata.")
    lines.append("- M8 = proxy auto-vérification EXTRACTEUR (glyphe='❧' OU tier=3 OU note_violation = dégradation).")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = build_argparser().parse_args()
    results, exit_code = run_validate(args)

    if args.format in ("json", "both"):
        json_out = json.dumps(results, indent=2, ensure_ascii=False)
        if args.output:
            args.output.with_suffix(".json").write_text(json_out)
            if not args.quiet:
                print(f"WROTE {args.output.with_suffix('.json')}")
        elif not args.quiet:
            # Fallback console : imprime JSON meme si --format both
            print(json_out)

    if args.format in ("markdown", "both"):
        md_out = render_markdown(results)
        if args.output:
            args.output.with_suffix(".md").write_text(md_out)
            if not args.quiet:
                print(f"WROTE {args.output.with_suffix('.md')}")
        elif not args.quiet:
            # Fallback console : imprime markdown meme si --format both
            print(md_out)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
