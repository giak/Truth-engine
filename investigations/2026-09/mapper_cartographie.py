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
    raise NotImplementedError


def extract_facts(run_state: dict | None, origin_run: str, subject_dir: str) -> list[dict]:
    raise NotImplementedError


def extract_actions_pending(run_state: dict | None) -> list[dict]:
    raise NotImplementedError


def extract_causal_gaps(run_state: dict | None) -> list[dict]:
    raise NotImplementedError


def extract_leads_non_saturated(run_state: dict | None) -> list[dict]:
    raise NotImplementedError


def extract_run_id(run_state: dict | None) -> str:
    raise NotImplementedError


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