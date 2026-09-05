#!/usr/bin/env python3
"""Cartographie de la campagne 2026-09 - aggregation offline des investigations."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR_DEFAULT = Path(__file__).resolve().parent
OUT_JSON = "campagne_cartographie.json"
OUT_MD = "campagne_cartographie.md"
OVERRIDES_FILE = "campagne_classes.json"

TIERS = ("✦", "✧", "⁅", "❧")

CLASSES = (
    "transactionnelle",
    "informationnelle",
    "lobbying",
    "reseau",
    "etrangere_etatique",
    "coercitive",
    "effet_asymetrie",
)

CLASS_KEYWORDS: dict[str, tuple[str, ...]] = {
    "transactionnelle": ("achat", "corruption", "clientélisme", "clientelisme", "triche", "vote"),
    "informationnelle": ("désinformation", "desinformation", "manipulation", "infiltration", "factcheck", "propagande", "microciblage", "deepfake"),
    "lobbying": ("lobby", "thinktank", "think tank", "capture"),
    "reseau": ("club", "siècle", "siecle", "francmacon", "franc-macon", "pantouflage", "réseau", "reseau"),
    "etrangere_etatique": ("ned", "usaid", "cia", "elnet", "aipac", "soros", "israel", "ingérence", "ingerence", "couleur", "nordstream", "nord-stream"),
    "coercitive": ("gps", "pegasus", "nso", "doppelganger", "brouillage", "cyber", "drone", "coercition", "caviardage"),
    "effet_asymetrie": ("effet", "asymétrie", "asymetrie", "narratif", "impact"),
}


def _norm(s: str) -> str:
    return " ".join(re.sub(r"[^a-zà-ÿœæ0-9]", " ", s.lower()).split())


def scan_dirs(base: Path) -> list[str]:
    return sorted(p.name for p in base.iterdir() if p.is_dir() and not p.name.startswith("__"))


def classify_dir(base: Path, name: str) -> dict:
    d = base / name
    files = [p.name for p in d.iterdir() if p.is_file()]
    inv = next((f for f in files if f.endswith("_INVESTIGATION.md")), None)
    run = next((f for f in files if f.endswith("_RUN_STATE.json")), None)
    cert = next((f for f in files if f.endswith("_CERTIFICATION.json")), None)
    if run and inv and cert:
        kind = "kernel"
    elif run:
        kind = "partial"
    elif files:
        kind = "bare"
    else:
        kind = "empty"
    return {
        "name": name,
        "kind": kind,
        "files": len(files),
        "inv_file": inv,
        "run_file": run,
        "cert_file": cert,
    }


def load_json(path: Path | None) -> dict | None:
    if path is None:
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def extract_title(base: Path, info: dict) -> str:
    inv_path = info.get("inv_file")
    if not inv_path:
        return ""
    try:
        text = (base / info["name"] / inv_path).read_text(encoding="utf-8")
    except OSError:
        return ""
    m = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return m.group(1).strip()[:200] if m else ""


def extract_facts(run_state: dict | None, origin_run: str, subject_dir: str) -> list[dict]:
    if not run_state:
        return []
    out = []
    for f in run_state.get("facts", []) or []:
        if not isinstance(f, dict):
            continue
        out.append(
            {
                "key": str(f.get("key", "")),
                "value": str(f.get("value", "")),
                "tier": str(f.get("tier", "?")),
                "families": [str(x) for x in f.get("families", []) or []],
                "url": str(f.get("url", "")),
                "memory_id": str(f.get("memory_id", "")),
                "origin_run": origin_run,
                "subject_dir": subject_dir,
            }
        )
    return out


def extract_actions_pending(run_state: dict | None) -> list[dict]:
    if not run_state:
        return []
    out = []
    for a in run_state.get("actions", []) or []:
        if isinstance(a, dict) and str(a.get("status", "")).upper() == "PENDING":
            out.append({"id": str(a.get("id", "")), "text": str(a.get("text", ""))[:200]})
    return out


def extract_causal_gaps(run_state: dict | None) -> list[dict]:
    if not run_state:
        return []
    out = []
    for c in run_state.get("causal", []) or []:
        if not isinstance(c, dict):
            continue
        if c.get("status") == "GAP" or c.get("gap_type") == "EVIDENCE_GAP":
            out.append(
                {
                    "id": str(c.get("id", "")),
                    "text": str(c.get("text", ""))[:300],
                    "gap_type": str(c.get("gap_type", "")),
                }
            )
    return out


def extract_leads_non_saturated(run_state: dict | None) -> list[dict]:
    if not run_state:
        return []
    out = []
    for l in run_state.get("leads", []) or []:
        if isinstance(l, dict) and str(l.get("status", "")).upper() != "SATURATED":
            out.append(
                {
                    "id": str(l.get("id", "")),
                    "subject": str(l.get("subject") or l.get("text") or "")[:200],
                    "priority": str(l.get("priority", "")),
                }
            )
    return out


def extract_run_id(run_state: dict | None) -> str:
    if not run_state:
        return ""
    for key in ("run", "meta"):
        v = run_state.get(key)
        if isinstance(v, dict):
            for k2 in ("id", "run_id"):
                if isinstance(v.get(k2), str) and v[k2]:
                    return v[k2]
    for k3 in ("id", "run_id"):
        v = run_state.get(k3)
        if isinstance(v, str) and v:
            return v
    return ""


def map_classes(info: dict, title: str, run_state: dict | None, overrides: dict) -> list[dict]:
    name = info["name"]
    if name in overrides:
        cls_list = overrides[name]
        if not isinstance(cls_list, list):
            cls_list = [cls_list]
        return [
            {"class": c, "source": "override", "confidence": "high"}
            for c in cls_list
            if c in CLASSES
        ]

    texts = [_norm(name), _norm(title)]
    if run_state:
        for bucket in ("leads", "claims", "axes"):
            for o in run_state.get(bucket, []) or []:
                if isinstance(o, dict):
                    texts.append(_norm(str(o.get("subject") or o.get("text") or "")))
        for f in run_state.get("facts", []) or []:
            if isinstance(f, dict):
                texts.append(_norm(str(f.get("key") or "")))
    blob = " ".join(texts)

    scores: dict[str, int] = {}
    for cls, kws in CLASS_KEYWORDS.items():
        hits = {kw for kw in kws if kw in blob}
        if hits:
            scores[cls] = len(hits)

    result = []
    for cls, n in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])):
        confidence = "high" if n >= 2 else "medium"
        result.append({"class": cls, "source": "auto", "confidence": confidence})
    return result


def derive_gaps(subjects: list[dict], facts: list[dict]) -> dict:
    empty_dirs = sorted(s["name"] for s in subjects if s["kind"] == "empty")
    bare_md = sorted(s["name"] for s in subjects if s["kind"] == "bare")
    partial = sorted(s["name"] for s in subjects if s["kind"] == "partial")

    candidates = []
    for f in facts:
        if f["tier"] == "✧":
            candidates.append(
                {
                    "key": f["key"],
                    "tier": "✧",
                    "url": f["url"],
                    "subject_dir": f["subject_dir"],
                }
            )

    actions_pending = []
    questions_ouvertes = []
    leads_a_traiter = []
    class_counts: dict[str, int] = {}
    for s in subjects:
        for a in s.get("actions_pending", []):
            actions_pending.append({"dir": s["name"], "id": a["id"], "text": a["text"]})
        for g in s.get("causal_gaps", []):
            questions_ouvertes.append(
                {"dir": s["name"], "id": g["id"], "text": g["text"], "gap_type": g["gap_type"]}
            )
        for l in s.get("leads_non_saturated", []):
            leads_a_traiter.append({"dir": s["name"], "id": l["id"], "subject": l["subject"]})
        for cm in s.get("classes", []):
            class_counts[cm["class"]] = class_counts.get(cm["class"], 0) + 1

    angles_morts = {c: class_counts.get(c, 0) for c in CLASSES if class_counts.get(c, 0) <= 1}

    return {
        "planifie_non_execute": empty_dirs,
        "hors_protocole": bare_md,
        "partiel": partial,
        "candidats_elevation": candidates,
        "actions_pending": actions_pending,
        "questions_ouvertes": questions_ouvertes,
        "leads_a_traiter": leads_a_traiter,
        "angles_morts_classes": angles_morts,
    }


def build_data(base: Path, overrides: dict) -> dict:
    subjects: list[dict] = []
    facts: list[dict] = []
    for name in scan_dirs(base):
        info = classify_dir(base, name)
        run_state = load_json(base / name / info["run_file"]) if info["run_file"] else None
        run_id = extract_run_id(run_state)
        title = extract_title(base, info)
        fcts = extract_facts(run_state, run_id, name)
        facts += fcts
        subjects.append(
            {
                "name": name,
                "kind": info["kind"],
                "files": info["files"],
                "title": title,
                "run_id": run_id,
                "n_facts": len(fcts),
                "tiers": {t: sum(1 for f in fcts if f["tier"] == t) for t in TIERS},
                "n_leads": len(run_state.get("leads", []) or []) if run_state else 0,
                "actions_pending": extract_actions_pending(run_state),
                "causal_gaps": extract_causal_gaps(run_state),
                "leads_non_saturated": extract_leads_non_saturated(run_state),
                "classes": map_classes(info, title, run_state, overrides),
            }
        )

    facts_total = {
        "n": len(facts),
        "tiers": {t: sum(1 for f in facts if f["tier"] == t) for t in TIERS},
        "with_url": sum(1 for f in facts if f.get("url")),
        "with_memory_id": sum(1 for f in facts if f.get("memory_id")),
    }

    matrix_classes: dict[str, list[str]] = {}
    for s in subjects:
        for cm in s["classes"]:
            matrix_classes.setdefault(cm["class"], []).append(s["name"])
    for cls in CLASSES:
        matrix_classes.setdefault(cls, [])

    counts = {
        "dirs": len(subjects),
        "with_run_state": sum(1 for s in subjects if s["kind"] in ("kernel", "partial")),
        "with_full_kernel": sum(1 for s in subjects if s["kind"] == "kernel"),
        "empty_dirs": sum(1 for s in subjects if s["kind"] == "empty"),
    }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_dir": str(base),
        "counts": counts,
        "facts_total": facts_total,
        "subjects": subjects,
        "facts": facts,
        "matrix_classes": matrix_classes,
        "gaps": derive_gaps(subjects, facts),
        "runs_topology": [
            {"run_id": s["run_id"], "subject_dir": s["name"], "facts_n": s["n_facts"], "n_leads": s["n_leads"]}
            for s in subjects
            if s["run_id"]
        ],
    }


def render_markdown(data: dict) -> str:
    lines: list[str] = []
    A = lines.append
    A("# CAMPAGNE 2026-09 — Cartographie des investigations")
    A("")
    A(f"> Rapport généré automatiquement · {data['generated_at']}")
    A(f"> Périmètre : `{data['source_dir']}`")
    A("> **Règle d'honnêteté** : aucune donnée n'est inventée ; les lacunes sont étiquetées "
      "(hors-protocole, vide, non certifié). Mapping de classes : `auto` (heuristique) ou `override` (manuel).")
    A("")

    A("## §1 Vue d'ensemble")
    A("")
    c = data["counts"]
    ft = data["facts_total"]
    A("| Métrique | Valeur |")
    A("|---|---|")
    A(f"| Dossiers | {c['dirs']} |")
    A(f"| Runs KERNEL complets | {c['with_full_kernel']} |")
    A(f"| Avec RUN_STATE (kernel + partiel) | {c['with_run_state']} |")
    A(f"| Dossiers vides | {c['empty_dirs']} |")
    tiers = ft["tiers"]
    A(f"| Faits agrégés | {ft['n']} (✦ {tiers['✦']} · ✧ {tiers['✧']} · ⁅ {tiers['⁅']} · ❧ {tiers['❧']}) |")
    A(f"| Faits avec URL | {ft['with_url']} |")
    A(f"| Faits avec memory_id | {ft['with_memory_id']} |")
    A("")

    A("## §2 Inventaire des sujets")
    A("")
    A("| Dossier | Type | Sujet | Faits | Tiers | Run | Classes |")
    A("|---|---|---|---|---|---|---|")
    for s in data["subjects"]:
        tier_cell = " ".join(f"{t}:{s['tiers'][t]}" for t in TIERS)
        classes_cell = ", ".join(cm["class"] for cm in s["classes"]) or "—"
        subject_cell = s["title"][:60] or "(sans titre)"
        A(f"| `{s['name']}` | {s['kind']} | {subject_cell} | {s['n_facts']} | {tier_cell} | `{s['run_id'] or '—'}` | {classes_cell} |")
    A("")

    A("## §3 Atlas des faits")
    A("")
    A("| Fait | Tier | Familles | URL | memory_id | Run |")
    A("|---|---|---|---|---|---|")
    for f in data["facts"]:
        fams = ",".join(f["families"]) or "—"
        url = f["url"] or "—"
        A(f"| {f['key'][:80]} | {f['tier']} | {fams} | {url} | `{f['memory_id'] or '—'}` | `{f['origin_run'] or f['subject_dir']}` |")
    A("")

    A("## §4 Matrice 7 classes x dossiers")
    A("")
    A("| Classe | Dossiers |")
    A("|---|---|")
    for cls in CLASSES:
        ds = data["matrix_classes"].get(cls, [])
        cell = ", ".join(f"`{d}`" for d in ds) or "—"
        A(f"| {cls} | {cell} |")
    A("")

    A("## §5 Gaps & leads")
    A("")
    g = data["gaps"]

    def sub(title: str, items) -> None:
        A("")
        A(f"### {title} ({len(items)})")
        if not items:
            A("_Aucun_")
            return
        for it in items:
            if isinstance(it, dict):
                prefix = f"{it.get('dir')} · " if it.get("dir") else ""
                ident = f"`{it.get('id')}` " if it.get("id") else ""
                detail = it.get("text") or it.get("key") or it.get("subject") or ""
                A(f"- {prefix}{ident}{detail}")
            else:
                A(f"- `{it}`")

    sub("Dossiers planifiés non exécutés", g["planifie_non_execute"])
    sub("Hors protocole (sujet connu, faits non certifiés)", g["hors_protocole"])
    sub("Runs partiels", g["partiel"])
    sub("Faits candidats à l'élévation (✧)", g["candidats_elevation"])
    sub("Actions en attente (PENDING)", g["actions_pending"])
    sub("Questions ouvertes (EVIDENCE_GAP)", g["questions_ouvertes"])
    sub("Leads non saturés", g["leads_a_traiter"])
    A("")
    A("### Angles morts de classe (≤ 1 dossier)")
    if g["angles_morts_classes"]:
        for cls, n in sorted(g["angles_morts_classes"].items()):
            A(f"- `{cls}` : {n} dossier(s)")
    else:
        A("_Aucun_")
    A("")

    A("## §6 Topographie des runs")
    A("")
    A("| Run | Dossier | Faits | Leads |")
    A("|---|---|---|---|")
    for r in data["runs_topology"]:
        A(f"| `{r['run_id']}` | {r['subject_dir']} | {r['facts_n']} | {r['n_leads']} |")
    A("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Cartographie de la campagne 2026-09")
    ap.add_argument("--base", type=str, default=None, help="Dossier campagne (défaut : dossier du script)")
    ap.add_argument("--overrides", type=str, default=None, help="Table de surcharge JSON")
    ap.add_argument("--out-json", type=str, default=None, help="Sortie JSON")
    ap.add_argument("--out-md", type=str, default=None, help="Sortie markdown")
    args = ap.parse_args(argv)

    base = Path(args.base) if args.base else BASE_DIR_DEFAULT
    overrides_path = Path(args.overrides) if args.overrides else base / OVERRIDES_FILE
    out_json = Path(args.out_json) if args.out_json else base / OUT_JSON
    out_md = Path(args.out_md) if args.out_md else base / OUT_MD

    overrides = load_json(overrides_path) or {}
    data = build_data(base, overrides)
    out_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(render_markdown(data), encoding="utf-8")
    print(f"OK — {out_json.name} ({len(data['facts'])} faits) + {out_md.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())