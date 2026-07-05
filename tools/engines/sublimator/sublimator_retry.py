#!/usr/bin/env python3
"""
sublimator_retry.py — Validateur retry N=2 pour EXTRACTEUR Sublimator v36 §13.3.4.

Ce script est un **validateur post-sub-agent** (PAS un lanceur). Il est appelé
par l'orchestrateur (Buffy parent agent, ou Sublimator local) entre chaque
tentative de sub-agent EXTRACTEUR (thinker-with-files-gemini).

Entrée (stdin JSON OU argument --input):
    {
      "enquete_id": "cultes_france",
      "attempt_number": 1,                 # 1-indexed (1 = initial, 2+ = retries)
      "max_retries": 2,                    # budget total de retries
      "timeout_s": 30,                     # silence au-dela = KO
      "response_text": "<raw sub-agent output>",
      "duration_s": 25.3                   # mesuree par l'orchestrateur
    }

Sortie (stdout JSON):
    {
      "verdict": "success | retry_needed | giveup",
      "attempt_number": 1,
      "json_valid": true|false,
      "silence_detected": true|false,
      "duration_ok": true|false,
      "fields_present": ["enquete_id", ...],
      "fields_missing": ["faits_atomiques", ...],
      "fait_count": 0,                     # >= 10 pour OK
      "reason": "...",
      "recommendation": "continue_next_attempt | stop_with_success | stop_with_failure"
    }

Cible : remplace la phrase du ORCHESTRATEUR §13.3.4 etape B :
    > "Lance le prompt EXTRACTEUR ... Stocke quintessence_v1. Valide que c'est du
    > JSON valide. Si non, reessaie 1 fois."
Devient :
    > "python3 sublimator_retry.py --input quint_v1_attempt.json"
    > "lit verdict.recommendation ; si != stop_with_success : reessaie jusqu'a max_retries"

100% deterministe, stdlib only (argparse, json, sys, re, pathlib), $0 cout LLM.

Usage:
    echo '{"enquete_id":"x","attempt_number":1,"max_retries":2,"timeout_s":30,
          "response_text":"...","duration_s":25}' | python3 sublimator_retry.py
    python3 sublimator_retry.py --input attempt.json --max-retries 2 --timeout 30
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

CHAMPS_REQUIS = ["enquete_id", "complexity", "date_extraction", "these_centrale", "faits_atomiques"]
FAIT_MIN = 10  # SPECS §13.3.2 cardinalite minimale


def extract_json(text: str) -> str:
    """Tente d'extraire le premier bloc JSON equilibre depuis une reponse LLM.
    Utilise un parser balanced-brackets qui gere strings echappees (anti-false-negative
    sur reponses avec markdown embarque ou plusieurs {...}).
    """
    if not text:
        return ""
    t = text.strip()
    start = t.find("{")
    if start == -1:
        return ""
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(t)):
        c = t[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return t[start:i + 1]
    return ""  # Pas de bloc equilibre trouve


def validate_attempt(record: Dict) -> Dict:
    """Valide un attempt_record et retourne verdict JSON."""
    resp = str(record.get("response_text") or "")
    duration = float(record.get("duration_s", 0) or 0)
    timeout = float(record.get("timeout_s", 30) or 30)
    attempt_n = int(record.get("attempt_number", 1) or 1)
    max_ret = int(record.get("max_retries", 2) or 2)
    silence = duration > timeout or duration <= 0
    json_block = extract_json(resp)
    parsed: Dict = {}
    json_valid = False
    parse_error = ""
    if json_block:
        try:
            parsed = json.loads(json_block)
            json_valid = True
        except json.JSONDecodeError as e:
            parse_error = str(e)
    fields_present = [c for c in CHAMPS_REQUIS if c in parsed] if json_valid else []
    fields_missing = [c for c in CHAMPS_REQUIS if c not in parsed] if json_valid else list(CHAMPS_REQUIS)
    fait_count = len(parsed.get("faits_atomiques", [])) if json_valid else 0
    fait_ok = fait_count >= FAIT_MIN
    if not json_valid:
        verdict = "giveup" if attempt_n >= max_ret + 1 else "retry_needed"
        reason = f"JSON malforme : {parse_error[:80] if parse_error else 'aucun bloc JSON detecte'}"
        recommendation = "continue_next_attempt" if verdict == "retry_needed" else "stop_with_failure"
    elif silence:
        verdict = "giveup" if attempt_n >= max_ret + 1 else "retry_needed"
        reason = f"silence detecte : {duration:.1f}s > timeout {timeout:.0f}s"
        recommendation = "continue_next_attempt" if verdict == "retry_needed" else "stop_with_failure"
    elif fields_missing:
        verdict = "giveup" if attempt_n >= max_ret + 1 else "retry_needed"
        reason = f"champs manquants : {fields_missing}"
        recommendation = "continue_next_attempt" if verdict == "retry_needed" else "stop_with_failure"
    elif not fait_ok:
        verdict = "giveup" if attempt_n >= max_ret + 1 else "retry_needed"
        reason = f"cardinalite insuffisante : {fait_count} F-### (cible >= {FAIT_MIN})"
        recommendation = "continue_next_attempt" if verdict == "retry_needed" else "stop_with_failure"
    else:
        verdict = "success"
        reason = "ok : JSON valide, champs requis presents, cardinalite >= 10, pas de silence"
        recommendation = "stop_with_success"
    return {
        "verdict": verdict,
        "attempt_number": attempt_n,
        "max_retries": max_ret,
        "json_valid": json_valid,
        "silence_detected": silence,
        "duration_ok": not silence,
        "duration_s": duration,
        "fields_present": fields_present,
        "fields_missing": fields_missing,
        "fait_count": fait_count,
        "reason": reason,
        "recommendation": recommendation,
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", type=Path, default=None, help="Fichier JSON attempt_record (sinon stdin)")
    p.add_argument("--max-retries", type=int, default=2, help="Budget total retries (defaut 2)")
    p.add_argument("--timeout", type=int, default=30, help="Seuil silence en s (defaut 30)")
    p.add_argument("--attempt", type=int, default=1, help="Numero tentative (defaut 1 = initial)")
    return p


def main() -> int:
    args = build_parser().parse_args()
    if args.input:
        try:
            record = json.loads(args.input.read_text())
        except (json.JSONDecodeError, OSError) as e:
            sys.stderr.write(f"FATAL input: {e}\n")
            return 2
    else:
        raw = sys.stdin.read().strip()
        if not raw:
            sys.stderr.write("FATAL: stdin vide et --input absent\n")
            return 2
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"FATAL JSON stdin: {e}\n")
            return 2
    # override depuis args CLI si presents
    record.setdefault("max_retries", args.max_retries)
    record.setdefault("timeout_s", args.timeout)
    record.setdefault("attempt_number", args.attempt)
    verdict = validate_attempt(record)
    sys.stdout.write(json.dumps(verdict, indent=2, ensure_ascii=False) + "\n")
    # exit code : 0=success, 1=retry_needed, 2=giveup
    return {"success": 0, "retry_needed": 1, "giveup": 2}[verdict["verdict"]]


if __name__ == "__main__":
    sys.exit(main())
