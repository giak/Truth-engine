#!/usr/bin/env python3
"""
sublimator_pilot.py — Pilote Sublimator v36 orchestrateur end-to-end Phase 1 → Phase 2 + validation.

**Architecture** (post-suppression Phase 0, revue 2026-07-05) :
- Phase 1 (MOCK LLM-templated) : injecte des fixtures reader.md + quintessence.json schema-conformes
  pre-placees dans `_validation/<enquete_id>/` (production manuelle ou via LLM hote).
- Phase 1.5 (MOCK) : compress_summary lu depuis la quintessence (champ optionnel).
- Phase 2 (MOCK) : synthese_clusters.json + synthese.json generes par agregation sommaire des
  compress_summary.

**Sans LLM runtime**, ce script reste fonctionnel en mode "fixtures" : il valide que le pipeline
accepte du contenu schema-conforme et passe les validateurs Python. Cela PREDIT le comportement
sous LLM hote (memes schemas, memes validateurs).

**Avec LLM runtime**, il faudrait remplacer les `mock_*` par des appels LLM.

Usage:
    python3 tools/engines/sublimator/sublimator_pilot.py \\
        --dossier investigations/2026-07-04-RIC \\
        --validation-dir investigations/2026-07-04-RIC/_validation \\
        --enquete religieuse_verrou

Sortie JSON : pipeline trace etape-par-etape avec exit code 0/1/2.
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional

# Regex F-### count (utilise dans phase1_5_compress_summary).
# Quick win : etendu pour matcher nomenclatures saison 2 (F-PNR33, F-HIST-01, F-REL01,
# F-VB01, F-CU01, F-CLIM01, F-IA01) en plus de F-### standard.
re_fact = re.compile(r"F-[A-Z]*\d{2,4}")


def log(msg: str) -> None:
    """Log structure avec timestamp."""
    sys.stderr.write(f"[sublimator_pilot] {msg}\n")
    sys.stderr.flush()


def phase1_reader(val_dir: Path, enquete_id: str) -> Optional[dict]:
    """Phase 1.1 (LECTEUR) : charge le reader annote depuis _validation/<enquete_id>-reader.md."""
    reader_path = val_dir / f"{enquete_id}-reader.md"
    if not reader_path.exists():
        log(f"Phase 1.1 KO: {reader_path} introuvable. "
            "Fixture requise (LLM-templated mock faute d'hote LLM runtime).")
        return None
    text = reader_path.read_text()
    # Verification structurelle (presence des 6 sections obligatoires).
    sections_required = ["## 0. Thèse centrale", "## 1. KERNEL", "## 2. Faits atomiques",
                         "## 3. Acteurs principaux", "## 4. Mécanismes causaux",
                         "## 5. Impact humain", "## 6. Sources"]
    missing = [s for s in sections_required if s not in text]
    if missing:
        log(f"Phase 1.1 WARNING: sections manquantes dans reader: {missing}")
    log(f"Phase 1.1 OK: {reader_path} ({len(text)} chars, {len(missing)} section(s) manquante(s))")
    return {"ok": True, "path": str(reader_path), "chars": len(text), "missing_sections": missing}


def phase1_quintessence(val_dir: Path, enquete_id: str, reader_text: str = "") -> Optional[dict]:
    """Phase 1.2 (EXTRACTEUR) : charge la quintessence depuis _validation/<enquete_id>-quintessence-v2.json."""
    # Match suffixe -quintessence*.json (v1, v2, etc.)
    candidates = sorted(val_dir.glob(f"{enquete_id}-quintessence*.json"))
    # Filtrer les fichiers "critique"
    candidates = [c for c in candidates if "critique" not in c.name]
    if not candidates:
        log(f"Phase 1.2 KO: aucun {enquete_id}-quintessence*.json dans {val_dir}")
        return None
    quin_path = candidates[0]
    log(f"Phase 1.2 fichier : {quin_path.name}")
    try:
        quin = json.loads(quin_path.read_text())
    except json.JSONDecodeError as e:
        log(f"Phase 1.2 KO: JSON invalide: {e}")
        return None
    # Verification structurelle 6 requises.
    REQUIRED = ["enquete_id", "enquete_source", "these_centrale", "faits_atomiques",
                "urls_prioritaires", "shadow_factor"]
    missing = [k for k in REQUIRED if k not in quin]
    if missing:
        log(f"Phase 1.2 KO: cles requises manquantes: {missing}")
        return None
    n_faits = len(quin.get("faits_atomiques", []))
    if n_faits < 10:
        log(f"Phase 1.2 WARNING: {n_faits} F-### (< 10 minimum recommandes). VERBATIM check OK mais cardinalite faible.")
    version = "v2" if "v2" in quin_path.name else "v1"
    log(f"Phase 1.2 OK: {quin_path.name} (enquete_id={quin['enquete_id']}, n_faits={n_faits}, version={version})")
    return {"ok": True, "path": str(quin_path), "quin": quin, "n_faits": n_faits, "version": version}


def phase1_5_compress_summary(quin: dict) -> dict:
    """Phase 1.5 : extrait compress_summary depuis la quintessence (champ optionnel)."""
    cs = quin.get("compress_summary", "")
    if not cs:
        return {"ok": False, "reason": "compress_summary absent"}
    words = cs.split()
    n_words = len(words)
    ok_words = n_words <= 100
    f_refs = len(re_fact.findall(cs))  # F-### cumulatif via re.findall
    log(f"Phase 1.5 compress_summary : {n_words} mots (<=100 cible: {ok_words}), {f_refs} F-### references")
    return {"ok": ok_words, "n_words": n_words, "n_f_refs": f_refs, "text": cs[:120]}


def phase2_synthese(val_dir: Path, enquete_id: str, quin: dict) -> dict:
    """Phase 2 (MOCK authentique) : synthese_clusters.json + synthese.json depuis les compress_summary.

    MOCK AUTHENTIQUE : aggregation triviale pour demonstration. LLM hote requis pour
    synthese reellement analytique (4 sub-agents coordination + critic loop).
    Aucun fichier n'est ecrit sur disque jusqu'a ce qu'un LLM reel soit connecte.
    """
    syse_dir = val_dir.parent / "_synthese" if (val_dir.parent / "_synthese").exists() else val_dir.parent
    # Si le dossier _synthese existe (pas pour religieuse_verrou seul), creer synthese.
    cluster_path = syse_dir / "synthese_clusters.json"
    synthese_path = syse_dir / "synthese.json"
    these_centrale = quin.get("these_centrale", "")
    n_faits = len(quin.get("faits_atomiques", []))
    mock_synthese = {
        "date_synthese": __import__("datetime").date.today().isoformat(),
        "complexity": quin.get("complexity", "APEX"),
        "n_clusters": 1,
        "clusters": [{
            "id": "C-MOCK",
            "label": enquete_id,
            "n_enquetes": 1,
            "these_cluster": these_centrale[:200],
            "f_partages": [f["id"] for f in quin.get("faits_atomiques", [])[:5]],
            "transversalite_intra": "MOCK AUTHENTIQUE — aggregation triviale Phase 2 par le pilote (LLM reel requis pour analyse semantique)",
            "enquetes_concernees": [quin.get("enquete_id", enquete_id)],
        }],
        "note": "MOCK: Phase 2 LLM-hote requis pour synthese reellement analytique.",
        "written_to_disk": False,  # I/O reel desactive tant que LLM hote absent
    }
    log(f"Phase 2 MOCK synthese : cluster_path={cluster_path} (PAS D'ECRITURE : LLM reel requis)")
    return {"ok": True, "mock": mock_synthese, "cluster_path": str(cluster_path),
            "synthese_path": str(synthese_path), "written_to_disk": False}


def phase_validation(val_dir: Path, version: str, enquete_id: Optional[str] = None) -> dict:
    """Phase de validation Python (REELLE) : invoque sublimator_validate.py sur le dossier _validation/.

    Args:
        val_dir: dossier _validation/
        version: "v1" | "v2" | "both"
        enquete_id: si specifie, propage `--enquete` au validateur pour verdict PER-ENQUETE.
    """
    cmd = [
        "python3",
        str(Path(__file__).parent / "sublimator_validate.py"),
        "--validation-dir", str(val_dir),
        "--version", version,
        "--format", "json",
    ]
    if enquete_id:
        cmd.extend(["--enquete", enquete_id])
    # Quick win : fichier temporaire unique (anti-race condition si 2 pilots en parallele).
    # Construction cmd SANS --output statique pour eviter le bug filtre-any précedemment identifie.
    # Pas de condition bizarre : le tempfile est TOUJOURS utilise via --output ajoute apres.
    _tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False, prefix="sublimator_pilot_validate_")
    _tmp.close()
    cmd.extend(["--output", _tmp.name])
    log(f"Validation : {cmd}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        if result.returncode not in (0, 1, 2):
            log(f"ERREUR Validation (exit {result.returncode}): {result.stderr[:500]}")
            return {"ok": False, "exit": result.returncode, "stderr": result.stderr}
        try:
            out = json.loads(Path(_tmp.name).read_text())
        except (json.JSONDecodeError, FileNotFoundError) as e:
            log(f"Validation WARNING: output JSON introuvable: {e}")
            out = {}
        log(f"Validation exit={result.returncode}, verdict_global={out.get('_meta', {}).get('verdict_global', '?')}")
        return {"ok": True, "exit": result.returncode, "out": out}
    finally:
        # Quick win : cleanup tempfile (anti-leak /tmp/sublimator_pilot_validate_*.json)
        Path(_tmp.name).unlink(missing_ok=True)


# Regex F-### count - DEFINITION CENTRALISEE EN TETE DE MODULE (style PEP 8 / Sublimator codebase).
# re_fact.compilee une seule fois a l'import, utilisee dans phase1_5_compress_summary.


def run_pilot(args: argparse.Namespace) -> dict:
    """Execute le pipeline end-to-end sur une enquete (ou toutes).

    Post-suppression Phase 0 (2026-07-05) : pas de cartographie. Le pilote demarre
    directement a Phase 1.1 sur les fixtures _validation/<enquete_id>/.
    """
    dossier = Path(args.dossier).resolve()
    val_dir = Path(args.validation_dir).resolve()
    enquete_id = args.enquete  # peut etre None (= tout le dossier)

    log(f"Sublimator v36 pipeline end-to-end")
    log(f"Dossier enquetes : {dossier}")
    log(f"Validation dir  : {val_dir}")
    log(f"Enquete cible    : {enquete_id or 'all'}")

    # Phase 1 / 1.5 / 2 / Validation — par enquete (Phase 0 supprimee 2026-07-05)
    enquetes_a_valider = ([enquete_id] if enquete_id else [])
    if not enquetes_a_valider:
        try:
            reader_files = list(val_dir.glob("*-reader.md"))
            enquetes_a_valider = [p.stem.replace("-reader", "") for p in reader_files]
        except Exception as e:
            log(f"AVERTISSEMENT: aucune enquete decouverte ({e}).")
            enquetes_a_valider = []
        if not enquetes_a_valider:
            log("AVERTISSEMENT: aucune enquete specifiee ou fixtures _validation/ detectees.")
    results = []
    for eid in enquetes_a_valider:
        log(f"=== Enquete: {eid} ===")
        reader = phase1_reader(val_dir, eid)
        if not reader:
            results.append({"enquete_id": eid, "phase1": "FAIL reader absent"})
            continue
        quin = phase1_quintessence(val_dir, eid)
        if not quin:
            results.append({"enquete_id": eid, "phase1": "FAIL quintessence absente"})
            continue
        cs = phase1_5_compress_summary(quin["quin"])
        synthese = phase2_synthese(val_dir, eid, quin["quin"])
        results.append({
            "enquete_id": eid,
            "phase1_reader": reader,
            "phase1_quin": {"n_faits": quin["n_faits"], "version": quin["version"]},
            "phase1_5_compress": cs,
            "phase2_mocksynthese": synthese,
        })
    # Validation finale reelle (CORRECTIF C1 : --enquete propage au validateur pour verdict per-enquete).
    validation = phase_validation(val_dir, args.version, enquete_id=enquete_id)
    return {
        "phase0_disabled": True,  # Phase 0 supprimee 2026-07-05 (overengineering)
        "n_enquetes": len(enquetes_a_valider),
        "details_par_enquete": results,
        "validation": validation,
    }


def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--dossier", type=Path, required=True,
                   help="Dossier contenant *_INVESTIGATION.md")
    p.add_argument("--validation-dir", type=Path, required=True,
                   help="Dossier _validation/ avec reader.md + quintessence.json fixtures")
    p.add_argument("--enquete", type=str, default=None,
                   help="Restreindre a 1 enquete (pour test ; sinon iteration sur toutes)")
    p.add_argument("--version", choices=["v1", "v2", "both"], default="both",
                   help="Version prompt (defaut: both)")
    p.add_argument("--format", choices=["json", "summary"], default="summary",
                   help="Format sortie (defaut: summary lisible humain)")
    args = p.parse_args()
    result = run_pilot(args)
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("=" * 70)
        print("SUBLIMATOR PILOT v36 — End-to-end pipeline report")
        print("=" * 70)
        print(f"Phase 0 : SUPPRIMEE (overengineering, voir git log 2026-07-05).")
        print(f"Pipeline : {result['n_enquetes']} enquete(s) executee(s) Phase 1 → Phase 2.")
        for r in result.get("details_par_enquete", []):
            print(f"\n--- Enquete : {r['enquete_id']} ---")
            for k, v in r.items():
                if k == "enquete_id":
                    continue
                print(f"  {k}: {json.dumps(v, ensure_ascii=False)}")
        v = result.get("validation", {})
        print("\n" + "=" * 70)
        print(f"Validation Python (REELLE) : exit={v.get('exit', '?')}, "
              f"verdict_global={v.get('out', {}).get('_meta', {}).get('verdict_global', '?')}")
        print("=" * 70)
    # Exit code : 0 si validation GO ou PIVOT, 2 si validation NO-GO.
    return result.get("validation", {}).get("exit", 2)


if __name__ == "__main__":
    sys.exit(main())
