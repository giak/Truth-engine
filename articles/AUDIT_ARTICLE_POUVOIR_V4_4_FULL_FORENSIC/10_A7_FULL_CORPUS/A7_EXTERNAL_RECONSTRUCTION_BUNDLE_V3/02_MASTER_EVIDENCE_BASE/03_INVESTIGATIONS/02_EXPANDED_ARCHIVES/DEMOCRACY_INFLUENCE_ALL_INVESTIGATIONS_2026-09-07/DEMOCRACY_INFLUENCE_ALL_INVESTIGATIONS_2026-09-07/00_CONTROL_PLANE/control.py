#!/usr/bin/env python3
"""Minimal control plane. Commands: validate | dashboard | run-card | synthesis-card."""
from __future__ import annotations
import argparse
import csv
import datetime
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
REGISTRY = ROOT / "INVESTIGATION_REGISTRY.csv"
DASHBOARD = ROOT / "DASHBOARD.md"
RUNTIME_BUNDLE_SHA256 = "d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30"
RUNTIME_KERNEL_SHA256 = "0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974"
CORPUS_BASELINE_SHA256 = "6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052"
REQUIRED = ['id', 'workstream', 'title', 'status', 'priority', 'type', 'mode', 'coverage', 'utility', 'dependencies', 'parent', 'merged_into', 'gate', 'object_question', 'scope', 'corpus_refs', 'truth_engine', 'renard', 'result_path', 'next_action']
VALID_STATUS = {
    "BACKLOG", "READY", "TE_ACTIVE", "TE_DONE", "PILOT_REVIEW", "CLOSED",
    "BLOCKED", "CONDITIONAL", "DEFERRED", "MERGED", "DROPPED",
}
RUNNABLE = {"PRIMARY", "CASE"}


def load():
    with REGISTRY.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate(rows=None):
    rows = rows or load()
    errors = []
    if not rows:
        return ["registry empty"]
    if list(rows[0].keys()) != REQUIRED:
        errors.append("registry schema drift")
    ids = [r["id"] for r in rows]
    known = set(ids)
    if len(ids) != len(known):
        errors.append("duplicate id")
    active = []
    for r in rows:
        rid = r["id"]
        if r["status"] not in VALID_STATUS:
            errors.append(f"{rid} invalid status={r['status']}")
        if r["status"] in {"READY", "TE_ACTIVE"}:
            active.append(rid)
            if r["type"] not in RUNNABLE:
                errors.append(f"{rid} runnable status with type={r['type']}")
            if not r["object_question"].strip():
                errors.append(f"{rid} object_question missing")
            if not r["scope"].strip():
                errors.append(f"{rid} scope missing")
        for dep in [x for x in r["dependencies"].split(";") if x]:
            if dep not in known:
                errors.append(f"{rid} unknown dependency {dep}")
        if r["parent"] and r["parent"] not in known:
            errors.append(f"{rid} unknown parent {r['parent']}")
        if r["merged_into"] and r["merged_into"] not in known:
            errors.append(f"{rid} unknown merged_into {r['merged_into']}")
        if r["status"] == "MERGED" and not r["merged_into"]:
            errors.append(f"{rid} MERGED without merged_into")
    if len(active) > 1:
        errors.append("more than one READY/TE_ACTIVE item: " + ",".join(active))
    return errors


def write_dashboard(rows=None):
    rows = rows or load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    byid = {r["id"]: r for r in rows}
    pilots = ["INV-010", "INV-019", "INV-049", "INV-071", "INV-103"]
    current = next((r for r in rows if r["status"] in {"READY", "TE_ACTIVE", "PILOT_REVIEW"}), None)
    lines = [
        "---",
        'trace_schema: "forensic-md/v1"',
        'project: "democracy-influence-investigations"',
        'artifact_type: "dashboard"',
        'artifact_id: "DASHBOARD"',
        'version: "2.0-kiss"',
        'status: "generated"',
        f'updated: "{datetime.date.today().isoformat()}"',
        'canonical_ref: "INVESTIGATION_REGISTRY.csv"',
        "---", "",
        "<!-- TRACE: generated_by=control.py; source=INVESTIGATION_REGISTRY.csv; do_not_edit_state_here=true -->",
        "", "# Dashboard", "",
        f"Current: **{current['id'] + ' / ' + current['status'] if current else 'no active item'}**",
        "", "| Pilot | Status | Truth Engine | Next |", "|---|---|---|---|",
    ]
    for pid in pilots:
        r = byid.get(pid)
        if r:
            lines.append(f"| {pid} | {r['status']} | {r['truth_engine']} | {r['next_action']} |")
    current_pilot = current if current and current["id"] in pilots else None
    next_pilot = None
    if current_pilot:
        i = pilots.index(current_pilot["id"])
        next_pilot = next((pid for pid in pilots[i + 1:] if byid.get(pid, {}).get("status") != "CLOSED"), None)
    if current_pilot:
        critical = [f"{current_pilot['id']} {current_pilot['status']}", "-> pilot review", "-> targeted RENARD only if still material"]
        if next_pilot:
            critical.append(f"-> {next_pilot}")
    elif current:
        critical = [f"{current['id']} {current['status']}", "-> run Truth Engine R3P1", "-> post-run review / RENARD delta-only"]
    else:
        critical = ["no active item"]
    lines += [
        "", "## Critical path", "", "```text", *critical, "```", "",
        "Selection after pilots: `CORE_MISSION_GATE -> model_change > discrimination > dependency_unlock > coverage_gap > utility`.",
        "", "<!-- GATE: one_READY_or_TE_ACTIVE_max=true -->", "",
    ]
    DASHBOARD.write_text("\n".join(lines), encoding="utf-8")
    return DASHBOARD


def run_card(inv_id, output=None):
    rows = load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    r = next((x for x in rows if x["id"] == inv_id), None)
    if not r:
        raise SystemExit(f"unknown INV_ID: {inv_id}")
    if r["status"] != "READY":
        raise SystemExit(f"not runnable: status={r['status']} gate={r['gate']}")
    if r["type"] not in RUNNABLE:
        raise SystemExit(f"not directly runnable: type={r['type']}")
    d = datetime.date.today().isoformat()
    text = f'''---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "{r['id']}-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "{d}"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "{r['id']}"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#{r['id']} -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — {r['id']}

```text
SUBJECT = {r['title']}
OBJECT_QUESTION = {r['object_question']}
SCOPE = {r['scope']}
MODE = {r['mode']}
COVERAGE = {r['coverage']}
CORPUS_REFS = {r['corpus_refs'] or 'NONE'}
DEPENDENCIES = {r['dependencies'] or 'NONE'}

TRUTH_ENGINE_BUNDLE_SHA256 = {RUNTIME_BUNDLE_SHA256}
TRUTH_ENGINE_KERNEL_SHA256 = {RUNTIME_KERNEL_SHA256}
CORPUS_BASELINE_SHA256 = {CORPUS_BASELINE_SHA256}
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
'''
    if output:
        p = pathlib.Path(output)
        if not p.is_absolute():
            p = ROOT / p
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        print(p)
    else:
        print(text)


def synthesis_card(inv_id, output=None):
    rows = load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    byid = {r["id"]: r for r in rows}
    r = byid.get(inv_id)
    if not r:
        raise SystemExit(f"unknown INV_ID: {inv_id}")
    if r["type"] != "SYNTHESIS":
        raise SystemExit(f"not a synthesis: type={r['type']}")
    if r["status"] != "BACKLOG":
        raise SystemExit(f"synthesis not selectable: status={r['status']} gate={r['gate']}")
    if r["gate"] != "DEPENDENCIES_DONE":
        raise SystemExit(f"synthesis gate not satisfied: gate={r['gate']}")
    if not r["object_question"].strip():
        raise SystemExit(f"{inv_id} object_question missing")
    if not r["scope"].strip():
        raise SystemExit(f"{inv_id} scope missing")
    deps = [x for x in r["dependencies"].split(";") if x]
    if not deps:
        raise SystemExit(f"{inv_id} synthesis has no dependencies")
    open_deps = [d for d in deps if byid.get(d, {}).get("status") != "CLOSED"]
    if open_deps:
        raise SystemExit("synthesis dependencies not CLOSED: " + ",".join(open_deps))
    dep_rows = [byid[d] for d in deps]
    dep_manifest = "\n".join(
        f"{d['id']} | status={d['status']} | truth_engine={d['truth_engine']} | result={d['result_path'] or 'MISSING'}"
        for d in dep_rows
    )
    d = datetime.date.today().isoformat()
    text = f"""---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "{r['id']}-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "{d}"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "{r['id']}"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#{r['id']} -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+gate=DEPENDENCIES_DONE+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — {r['id']}

```text
SUBJECT = {r['title']}
OBJECT_QUESTION = {r['object_question']}
SCOPE = {r['scope']}
MODE = {r['mode']}
COVERAGE = {r['coverage']}
CORPUS_REFS = {r['corpus_refs'] or 'NONE'}
DEPENDENCIES = {';'.join(deps)}
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
{dep_manifest}
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
"""
    if output:
        p = pathlib.Path(output)
        if not p.is_absolute():
            p = ROOT / p
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        print(p)
    else:
        print(text)


def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("validate")
    sp.add_parser("dashboard")
    rc = sp.add_parser("run-card")
    rc.add_argument("inv_id")
    rc.add_argument("--output")
    sc = sp.add_parser("synthesis-card")
    sc.add_argument("inv_id")
    sc.add_argument("--output")
    a = p.parse_args()
    if a.cmd == "validate":
        errors = validate()
        if errors:
            for e in errors:
                print("FAIL", e)
            raise SystemExit(1)
        print("PASS")
    elif a.cmd == "dashboard":
        print(write_dashboard())
    elif a.cmd == "run-card":
        run_card(a.inv_id, a.output)
    else:
        synthesis_card(a.inv_id, a.output)

if __name__ == "__main__":
    main()
