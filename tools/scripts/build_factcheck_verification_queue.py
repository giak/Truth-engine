#!/usr/bin/env python3
"""Build a local fact-verification queue from the current factcheck SQLite.

This script is deliberately local-only. It never calls Mnemolite and never changes
an epistemic status. SQLite labels are copied as raw labels and remain untrusted.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
from pathlib import Path

MECHANICAL_TYPES = {
    "NUMBER_MENTION", "TEXT_BLOCK", "DATE_MENTION", "URL",
    "PERCENTAGE_MENTION", "CURRENCY_MENTION",
}
FACT_LIKE_TYPES = {
    "FACT", "EVIDENCE", "FINDING", "METRIC", "STRUCTURED_OBSERVATION",
    "VERIFIED_RELATION", "REMEDIATION_EVENT", "EVENT",
}
CLAIM_LIKE_TYPES = {
    "CANONICAL_CLAIM", "FROZEN_CORE_CLAIM", "CANONICAL_ARGUMENT_CLAIM",
    "ATLAS_REDTEAM_THESIS", "ARTICLE_PROBATIVE_FREEZE",
}
OPEN_LIKE = {"OPEN", "OPEN_CRITICAL", "AUDIT_GAP", "UNKNOWN", "SEARCH_NEGATIVE", "COUNTEREVIDENCE"}

COLUMNS = [
    "RECORD_ID", "CANONICAL_KEY", "RECORD_TYPE", "DATA_CLASS",
    "EPISTEMIC_STATUS", "CONFIDENCE", "PUBLICATION_SAFE", "SUBJECT",
    "PREDICATE", "OBJECT", "VALUE_RAW", "CONTENT", "SOURCE_DOCUMENT",
    "SOURCE_REF", "SOURCE_URL", "SOURCE_TYPE", "PROVENANCE_STATUS",
    "DERIVATION_LEVEL", "PARENT_KEY", "TAGS", "NOTES",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def bucket(row: sqlite3.Row) -> str:
    record_type = (row["RECORD_TYPE"] or "").strip()
    status = (row["EPISTEMIC_STATUS"] or "").strip()
    if status in OPEN_LIKE or record_type in {"SEARCH_NEGATIVE", "COUNTEREVIDENCE"}:
        return "OPEN_OR_COUNTEREVIDENCE"
    if record_type in FACT_LIKE_TYPES:
        return "FACT_LIKE_CANDIDATE"
    if record_type in CLAIM_LIKE_TYPES:
        return "CLAIM_LIKE_CANDIDATE"
    if "INFERENCE" in status or "HYPOTHESIS" in status or record_type in {"INFERENCE", "SYNTHESIS", "CAUSAL_TRACE", "RELATION_CANDIDATE"}:
        return "INFERENCE_OR_RELATION_CANDIDATE"
    return "STRUCTURED_CANDIDATE"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("sqlite", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(args.sqlite)
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT * FROM records ORDER BY RECORD_ID").fetchall()
    candidates = []
    excluded = {"mechanical": 0, "structured_without_http_url": 0}
    buckets: dict[str, int] = {}
    for row in rows:
        record_type = (row["RECORD_TYPE"] or "").strip()
        content = (row["CONTENT"] or "").strip()
        source_url = (row["SOURCE_URL"] or "").strip()
        if record_type in MECHANICAL_TYPES:
            excluded["mechanical"] += 1
            continue
        if not content or not source_url.lower().startswith(("http://", "https://")):
            excluded["structured_without_http_url"] += 1
            continue
        item = {column: row[column] for column in COLUMNS}
        item["QUEUE_CLASS"] = bucket(row)
        item["SQLITE_EPISTEMIC_STATUS_RAW"] = row["EPISTEMIC_STATUS"]
        item["VERIFICATION_STATUS"] = "NOT_VERIFIED"
        candidates.append(item)
        buckets[item["QUEUE_CLASS"]] = buckets.get(item["QUEUE_CLASS"], 0) + 1

    queue_columns = COLUMNS + ["QUEUE_CLASS", "SQLITE_EPISTEMIC_STATUS_RAW", "VERIFICATION_STATUS"]
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=queue_columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(candidates)

    report = {
        "input": str(args.sqlite),
        "input_sha256": sha256(args.sqlite),
        "total_records": len(rows),
        "queue_records": len(candidates),
        "excluded": excluded,
        "queue_buckets": buckets,
        "policy": "LOCAL_ONLY; no Mnemolite write; every candidate remains NOT_VERIFIED until L0-L4.",
        "output": str(args.output),
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
