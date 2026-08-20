#!/usr/bin/env python3
"""Prepare a deterministic local manifest for one unverified queue candidate.

The script copies upstream identity and provenance from the queue. It never reads
web pages, calls Mnemolite, or promotes a candidate's epistemic status.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("queue", type=Path)
    parser.add_argument("record_id")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with args.queue.open(newline="", encoding="utf-8-sig") as stream:
        matches = [
            row for row in csv.DictReader(stream)
            if row.get("RECORD_ID") == args.record_id
        ]

    if not matches:
        raise SystemExit(f"record not found: {args.record_id}")
    if len(matches) != 1:
        raise SystemExit(f"record is not unique: {args.record_id}")

    row = matches[0]
    source_url = row.get("SOURCE_URL", "")
    if not source_url.startswith(("http://", "https://")):
        raise SystemExit(f"candidate has no HTTP source URL: {args.record_id}")

    manifest = {
        "upstream_id": row["RECORD_ID"],
        "upstream_key": row["CANONICAL_KEY"],
        "candidate_content": row["CONTENT"],
        "source_ref_original": source_url,
        "source_ref_used": source_url,
        "source_replacement_reason": None,
        "source_document": row["SOURCE_DOCUMENT"],
        "source_ref": row["SOURCE_REF"],
        "raw_epistemic_status": row["SQLITE_EPISTEMIC_STATUS_RAW"],
        "verification_status": "NOT_VERIFIED",
        "verification_level": "L0",
        "excerpt_ok": False,
        "locator": None,
        "memory_id": None,
        "writeback_allowed": False,
        "policy": "LOCAL_ONLY; source must be read and classified L0-L4 before any write-back.",
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(args.output),
        "upstream_id": manifest["upstream_id"],
        "upstream_key": manifest["upstream_key"],
        "verification_status": manifest["verification_status"],
        "writeback_allowed": manifest["writeback_allowed"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
