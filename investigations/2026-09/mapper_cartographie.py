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


def scan_dirs(base: Path) -> list[str]:
    return sorted(p.name for p in base.iterdir() if p.is_dir())


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
    raise NotImplementedError


def derive_gaps(subjects: list[dict], facts: list[dict]) -> dict:
    raise NotImplementedError


def build_data(base: Path, overrides: dict) -> dict:
    raise NotImplementedError


def render_markdown(data: dict) -> str:
    raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())