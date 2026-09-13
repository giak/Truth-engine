#!/usr/bin/env python3
"""Minimal control plane.

Commands: validate | preflight | dashboard | run-card | synthesis-card |
          cycle | batch | state | reclass-bootstrap | reclass-plan | apply
"""
from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import io
import json
import os
import pathlib
import re
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent
REGISTRY = ROOT / "INVESTIGATION_REGISTRY.csv"
DASHBOARD = ROOT / "DASHBOARD.md"
ORCHESTRATOR = ROOT / "INVESTIGATION_ORCHESTRATOR.md"
METHOD_PACK = ROOT / "METHOD_PACK.md"
CONTROL_STATE = ROOT / "CONTROL_STATE.json"
TRACELOG = ROOT / "TRACELOG.md"
PRIMARY_SELECTION_PREFIX = "CORE_MISSION_V2_SELECTED_"
SYNTHESIS_SELECTION_PREFIX = "CORE_MISSION_V2_SYNTHESIS_SELECTED_"
RECLASS_POLICY_VERSION = "CORE_MISSION_V2/ranking-7/v1"
RUNTIME_BUNDLE_SHA256 = "d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30"
RUNTIME_PACK_NAME = "TRUTH_ENGINE_2.10.6_R3P1_CANONICAL.zip"
RUNTIME_KERNEL_SHA256 = "0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974"
CORPUS_BASELINE_SHA256 = "6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052"
PROJECT_TZ = ZoneInfo("Europe/Paris")
PROGRAM_EXPORT = "DEMOCRACY_INFLUENCE_ALL_INVESTIGATIONS_2026-09-07.zip"
PROGRAM_EXPORT_SHA256 = "b2fec50e9cdd5e18806a96cdc7682b3fa23a917af6abe939ecafa1d0a590779f"
PROGRAM_SNAPSHOT = "PROGRAM_SNAPSHOT_2026-09-07.json"
PROGRAM_ANALYTIC_POINT = "ANALYTIC_POINT_2026-09-07.md"
REQUIRED = ['id', 'workstream', 'title', 'status', 'priority', 'type', 'mode', 'coverage', 'utility', 'dependencies', 'parent', 'merged_into', 'gate', 'object_question', 'scope', 'corpus_refs', 'truth_engine', 'renard', 'result_path', 'next_action']
VALID_STATUS = {
    "BACKLOG", "READY", "TE_ACTIVE", "TE_DONE", "PILOT_REVIEW", "CLOSED",
    "BLOCKED", "CONDITIONAL", "DEFERRED", "MERGED", "DROPPED",
}
RUNNABLE = {"PRIMARY", "CASE"}
SCORE_FIELDS = (
    "model_change", "discrimination", "effect_closure", "symmetry_value",
    "dependency_unlock", "coverage_gap", "utility",
)
SCORE_VALUE = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "VERY_HIGH": 3}
CLASSIFICATION_FIELDS = (
    "id", "workstream", "title", "status", "type", "mode", "coverage", "utility",
    "dependencies", "parent", "merged_into", "object_question", "scope", "corpus_refs",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    return sha256_bytes(path.read_bytes())


def stable_json(payload) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def gate_date(value: str) -> str | None:
    m = re.search(r"(?<!\d)(20\d{2}-\d{2}-\d{2})(?!\d)", value or "")
    return m.group(1) if m else None


def state_date(rows) -> str:
    selected = selected_rows(rows)
    if len(selected) == 1:
        d = gate_date(selected[0].get("gate", ""))
        if d:
            return d
    dates = [d for r in rows if (d := gate_date(r.get("gate", "")))]
    return max(dates) if dates else datetime.date.today().isoformat()


def atomic_write_text(path: pathlib.Path, text: str) -> str:
    """Write atomically and only when bytes differ. Returns WRITTEN|UNCHANGED."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    if path.exists() and path.read_bytes() == data:
        return "UNCHANGED"
    tmp = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    tmp.write_bytes(data)
    os.replace(tmp, path)
    return "WRITTEN"


def load():
    with REGISTRY.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def registry_bytes(rows) -> bytes:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=REQUIRED, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode("utf-8")


def split_ids(value: str | None):
    if not value:
        return []
    return [x.strip() for x in value.split(";") if x.strip()]


def selected_rows(rows):
    active = [r for r in rows if r["status"] in {"READY", "TE_ACTIVE"}]
    synth = [
        r for r in rows
        if r["type"] == "SYNTHESIS"
        and r["status"] == "BACKLOG"
        and r["gate"].startswith(SYNTHESIS_SELECTION_PREFIX)
    ]
    return active + synth


def validate(rows=None):
    if rows is None:
        rows = load()
    errors = []
    if not rows:
        return ["registry empty"]
    if list(rows[0].keys()) != REQUIRED:
        errors.append("registry schema drift")
    ids = [r["id"] for r in rows]
    known = set(ids)
    if len(ids) != len(known):
        errors.append("duplicate id")
    if not ORCHESTRATOR.exists():
        errors.append("missing INVESTIGATION_ORCHESTRATOR.md")
    if not METHOD_PACK.exists():
        errors.append("missing METHOD_PACK.md")
    for r in rows:
        rid = r["id"]
        if r["status"] not in VALID_STATUS:
            errors.append(f"{rid} invalid status={r['status']}")
        if r["status"] in {"READY", "TE_ACTIVE"}:
            if r["type"] not in RUNNABLE:
                errors.append(f"{rid} runnable status with type={r['type']}")
            if not r["gate"].startswith(PRIMARY_SELECTION_PREFIX):
                errors.append(f"{rid} runnable without current CORE_MISSION_V2 selection gate")
            if not r["object_question"].strip():
                errors.append(f"{rid} object_question missing")
            if not r["scope"].strip():
                errors.append(f"{rid} scope missing")
        if r["type"] == "SYNTHESIS" and r["status"] == "BACKLOG" and r["gate"].startswith(SYNTHESIS_SELECTION_PREFIX):
            if not r["object_question"].strip():
                errors.append(f"{rid} synthesis object_question missing")
            if not r["scope"].strip():
                errors.append(f"{rid} synthesis scope missing")
        for dep in [x for x in r["dependencies"].split(";") if x]:
            if dep not in known:
                errors.append(f"{rid} unknown dependency {dep}")
        if r["parent"] and r["parent"] not in known:
            errors.append(f"{rid} unknown parent {r['parent']}")
        if r["merged_into"] and r["merged_into"] not in known:
            errors.append(f"{rid} unknown merged_into {r['merged_into']}")
        if r["status"] == "MERGED" and not r["merged_into"]:
            errors.append(f"{rid} MERGED without merged_into")
    selected = selected_rows(rows)
    if len(selected) > 1:
        errors.append("more than one selected READY/TE_ACTIVE/SYNTHESIS item: " + ",".join(r["id"] for r in selected))
    return errors


def resolve_selected(rows, inv_id=None):
    byid = {r["id"]: r for r in rows}
    if inv_id:
        r = byid.get(inv_id)
        if not r:
            raise SystemExit(f"unknown INV_ID: {inv_id}")
        return r
    selected = selected_rows(rows)
    if not selected:
        raise SystemExit("no selected READY/TE_ACTIVE/SYNTHESIS item")
    if len(selected) != 1:
        raise SystemExit("selection invariant failed")
    return selected[0]


def preflight(inv_id=None, rows=None):
    if rows is None:
        rows = load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    byid = {r["id"]: r for r in rows}
    r = resolve_selected(rows, inv_id)
    selected = selected_rows(rows)
    if len(selected) != 1 or selected[0]["id"] != r["id"]:
        raise SystemExit(f"{r['id']} is not the unique current selection")

    if r["type"] in RUNNABLE:
        if r["status"] != "READY":
            raise SystemExit(f"not launch-preflightable: status={r['status']}")
        if not r["gate"].startswith(PRIMARY_SELECTION_PREFIX):
            raise SystemExit(f"stale selection gate: {r['gate']}")
        if r["truth_engine"] != "NOT_RUN":
            raise SystemExit(f"stale runnable state: truth_engine={r['truth_engine']}")
        kind = "RUN_CARD"
    elif r["type"] == "SYNTHESIS":
        if r["status"] != "BACKLOG":
            raise SystemExit(f"synthesis not selectable: status={r['status']}")
        if not r["gate"].startswith(SYNTHESIS_SELECTION_PREFIX):
            raise SystemExit(f"stale synthesis gate: {r['gate']}")
        deps = [x for x in r["dependencies"].split(";") if x]
        if not deps:
            raise SystemExit(f"{r['id']} synthesis has no dependencies")
        open_deps = [d for d in deps if byid.get(d, {}).get("status") != "CLOSED"]
        if open_deps:
            raise SystemExit("synthesis dependencies not CLOSED: " + ",".join(open_deps))
        kind = "SYNTHESIS_CARD"
    else:
        raise SystemExit(f"not executable by control plane: type={r['type']}")

    state = read_control_state()
    baseline = state.get("reclassification") or {}
    if baseline.get("policy_version") != RECLASS_POLICY_VERSION:
        raise SystemExit("no current reclassification baseline for active policy")
    if baseline.get("selected") != r["id"]:
        raise SystemExit(
            f"stale selection: baseline_selected={baseline.get('selected') or 'NONE'} current={r['id']}"
        )
    entry = (baseline.get("entries") or {}).get(r["id"])
    if not entry or entry.get("fp") != row_fingerprint(r):
        raise SystemExit(f"stale selection contract: {r['id']} differs from reclassification baseline")

    return {
        "status": "PASS",
        "inv_id": r["id"],
        "type": r["type"],
        "artifact": kind,
        "gate": r["gate"],
        "registry_sha256": sha256_file(REGISTRY),
    }


def dashboard_text(rows):
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    byid = {r["id"]: r for r in rows}
    pilots = ["INV-010", "INV-019", "INV-049", "INV-071", "INV-103"]
    current = next((r for r in rows if r["status"] in {"READY", "TE_ACTIVE", "PILOT_REVIEW"}), None)
    if not current:
        current = next((r for r in rows if r["type"] == "SYNTHESIS" and r["status"] == "BACKLOG" and r["gate"].startswith(SYNTHESIS_SELECTION_PREFIX)), None)
    status_order = ["CLOSED", "BACKLOG", "BLOCKED", "CONDITIONAL", "MERGED", "DEFERRED", "READY", "TE_ACTIVE"]
    counts = {st: sum(1 for r in rows if r["status"] == st) for st in status_order}
    delivery_r3p1 = sum(1 for r in rows if r["status"] == "CLOSED" and r["truth_engine"] == "DELIVERY_PASS_R3P1")
    synth_watch = [r["id"] for r in rows if r["type"] == "SYNTHESIS" and r["status"] != "CLOSED"]

    def plan_ids(prefix):
        return [r["id"] for r in rows if (r.get("next_action") or "").startswith(prefix)]

    def open_deps(r):
        deps = [x for x in r["dependencies"].split(";") if x]
        return [d for d in deps if byid.get(d, {}).get("status") != "CLOSED"]

    lines = [
        "---",
        'trace_schema: "forensic-md/v1"',
        'project: "democracy-influence-investigations"',
        'artifact_type: "dashboard"',
        'artifact_id: "DASHBOARD"',
        'version: "2.5-kiss"',
        'status: "generated"',
        f'updated: "{state_date(rows)}"',
        'canonical_ref: "INVESTIGATION_REGISTRY.csv"',
        "---", "",
        "<!-- TRACE: generated_by=control.py; source=INVESTIGATION_REGISTRY.csv; do_not_edit_state_here=true -->",
        "<!-- TRACE: supplemental_snapshots_and_CONTROL_STATE_are_noncanonical=true -->",
        "", "# Dashboard", "",
        f"Current: **{current['id'] + ' / ' + current['status'] if current else 'no active item'}**",
        f"Next gate: **{'synthesis-card' if current and current['type'] == 'SYNTHESIS' else ('continue current item' if current else 'reclassification required before any launch')}**",
        "", "## Program state", "",
        "| Metric | Value |", "|---|---:|",
        f"| TOTAL | {len(rows)} |",
        f"| CLOSED | {counts['CLOSED']} |",
        f"| BACKLOG | {counts['BACKLOG']} |",
        f"| BLOCKED | {counts['BLOCKED']} |",
        f"| CONDITIONAL | {counts['CONDITIONAL']} |",
        f"| MERGED | {counts['MERGED']} |",
        f"| DEFERRED | {counts['DEFERRED']} |",
        f"| READY | {counts['READY']} |",
        f"| TE_ACTIVE | {counts['TE_ACTIVE']} |",
        f"| CLOSED / DELIVERY_PASS_R3P1 | {delivery_r3p1} |",
        "", "## Pilot baseline", "",
        "| Pilot | Status | Truth Engine | Next |", "|---|---|---|---|",
    ]
    for pid in pilots:
        r = byid.get(pid)
        if r:
            lines.append(f"| {pid} | {r['status']} | {r['truth_engine']} | {r['next_action']} |")

    lanes = [
        ("TE active", [r["id"] for r in rows if r["status"] == "TE_ACTIVE"]),
        ("TE next (advisory)", plan_ids("PLAN_TE_NEXT")),
        ("TE later (advisory)", plan_ids("PLAN_TE_LATER")),
        ("New TE candidate / needs reclass", plan_ids("PLAN_TE_CANDIDATE_NEW")),
        ("Reframe / HOLD", plan_ids("PLAN_REFRAME_HOLD")),
        ("Synthesis ready", plan_ids("PLAN_SYNTHESIS_READY")),
        ("Synthesis blocked", plan_ids("PLAN_SYNTHESIS_BLOCKED")),
        ("Conditional", plan_ids("PLAN_CONDITIONAL")),
    ]
    lines += ["", "## Execution portfolio", "",
              "Advisory planning only. Fresh `CORE_MISSION_V2` reclassification remains the selection authority.", "",
              "| Lane | Count | IDs |", "|---|---:|---|"]
    for label, ids_ in lanes:
        lines.append(f"| {label} | {len(ids_)} | {', '.join(ids_) if ids_ else 'NONE'} |")

    if current and current["id"] in pilots:
        critical = [f"{current['id']} {current['status']}", "-> pilot review", "-> targeted RENARD only if still material"]
    elif current and current["type"] == "SYNTHESIS":
        critical = [f"{current['id']} SYNTHESIS_SELECTED", "-> synthesis-card", "-> dependency-only synthesis/review"]
    elif current:
        critical = [f"{current['id']} {current['status']}", "-> run Truth Engine R3P1", "-> terminal RUN_HANDOFF + incremental reclassification/apply"]
    else:
        critical = ["no active item", "-> read INVESTIGATION_ORCHESTRATOR.md", "-> guarded incremental reclassification", "-> full-pool fallback if impact cannot be bounded", "-> select at most one item"]

    lines += ["", "## Critical path", "", "```text", *critical, "```", ""]
    lines += ["## Synthesis dependency watch", "", "| Synthesis | Status | Open direct dependencies |", "|---|---|---|"]
    for sid in synth_watch:
        r = byid.get(sid)
        if r:
            deps = open_deps(r)
            lines.append(f"| {sid} | {r['status']} | {', '.join(deps) if deps else 'NONE'} |")

    lines += [
        "", "## Forensic snapshot / export", "",
        f"- Program snapshot: `{PROGRAM_SNAPSHOT}` (derived, non-canonical).",
        f"- Analytic point: `{PROGRAM_ANALYTIC_POINT}` (derived, non-canonical).",
        f"- Consolidated export: `{PROGRAM_EXPORT}`.",
        f"- Export SHA-256: `{PROGRAM_EXPORT_SHA256}`.",
        "- Runtime locked: `Truth Engine 2.10.6 / R3P1`.",
        f"- Runtime bundle SHA-256: `{RUNTIME_BUNDLE_SHA256}`.",
        f"- Corpus SHA-256: `{CORPUS_BASELINE_SHA256}`.",
        "",
        "Selection authority: `INVESTIGATION_ORCHESTRATOR.md`.",
        "Hard gate: `CORE_MISSION_V2`.",
        "Ranking: `model_change > discrimination > effect_closure > symmetry_value > dependency_unlock > coverage_gap > utility`.",
        f"Reclassification policy: `{RECLASS_POLICY_VERSION}`; unchanged rows may be reused only with a bounded impact frontier; otherwise full-pool fallback.",
        "", "<!-- GATE: one_selected_READY_or_TE_ACTIVE_or_SYNTHESIS_max=true -->",
        "<!-- INVARIANT: dashboard_and_CONTROL_STATE_are_derived; registry_is_state_source -->", "",
    ]
    return "\n".join(lines)


def write_dashboard(rows=None):
    if rows is None:
        rows = load()
    status = atomic_write_text(DASHBOARD, dashboard_text(rows))
    return DASHBOARD, status


def run_card_text(r):
    d = gate_date(r.get("gate", "")) or datetime.date.today().isoformat()
    return f'''---
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

TRUTH_ENGINE_PACK = {RUNTIME_PACK_NAME}
TRUTH_ENGINE_BUNDLE_SHA256 = {RUNTIME_BUNDLE_SHA256}
TRUTH_ENGINE_KERNEL_SHA256 = {RUNTIME_KERNEL_SHA256}
CORPUS_BASELINE_SHA256 = {CORPUS_BASELINE_SHA256}
METHOD_PACK = METHOD_PACK.md
ORCHESTRATOR = INVESTIGATION_ORCHESTRATOR.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md. Preserve the selected contract from INVESTIGATION_ORCHESTRATOR.md; do not broaden the run to adjacent context.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
'''


def synthesis_card_text(r, byid):
    deps = [x for x in r["dependencies"].split(";") if x]
    dep_rows = [byid[d] for d in deps]
    dep_manifest = "\n".join(
        f"{d['id']} | status={d['status']} | truth_engine={d['truth_engine']} | result={d['result_path'] or 'MISSING'}"
        for d in dep_rows
    )
    d = gate_date(r.get("gate", "")) or datetime.date.today().isoformat()
    return f"""---
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
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
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


def card_target(r, output=None):
    if output:
        p = pathlib.Path(output)
        return p if p.is_absolute() else ROOT / p
    suffix = "SYNTHESIS_CARD" if r["type"] == "SYNTHESIS" else "RUN_CARD"
    return ROOT / f"{r['id']}_{suffix}.md"


def write_card(inv_id=None, output=None, rows=None):
    if rows is None:
        rows = load()
    pf = preflight(inv_id, rows)
    byid = {r["id"]: r for r in rows}
    r = byid[pf["inv_id"]]
    p = card_target(r, output)
    text = synthesis_card_text(r, byid) if r["type"] == "SYNTHESIS" else run_card_text(r)
    status = atomic_write_text(p, text)
    return p, status


def run_card(inv_id, output=None):
    rows = load()
    r = next((x for x in rows if x["id"] == inv_id), None)
    if not r:
        raise SystemExit(f"unknown INV_ID: {inv_id}")
    if r["type"] not in RUNNABLE:
        raise SystemExit(f"not directly runnable: type={r['type']}")
    p, _ = write_card(inv_id, output, rows)
    print(p)


def synthesis_card(inv_id, output=None):
    rows = load()
    r = next((x for x in rows if x["id"] == inv_id), None)
    if not r:
        raise SystemExit(f"unknown INV_ID: {inv_id}")
    if r["type"] != "SYNTHESIS":
        raise SystemExit(f"not a synthesis: type={r['type']}")
    p, _ = write_card(inv_id, output, rows)
    print(p)


def read_control_state():
    if not CONTROL_STATE.exists():
        return {}
    try:
        return json.loads(CONTROL_STATE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        raise SystemExit("invalid CONTROL_STATE.json")


def compact_state_payload(rows, previous=None):
    previous = previous or {}
    selected = selected_rows(rows)
    chosen = selected[0] if len(selected) == 1 else None
    counts = {st: sum(1 for r in rows if r["status"] == st) for st in sorted(VALID_STATUS)}
    payload = {
        "schema": "investigation-control-state/v1",
        "registry_is_state_source": True,
        "registry_sha256": sha256_file(REGISTRY),
        "rows": len(rows),
        "selected": None if not chosen else {
            "id": chosen["id"], "status": chosen["status"], "type": chosen["type"], "gate": chosen["gate"],
        },
        "counts": {k: v for k, v in counts.items() if v},
        "dashboard_sha256": sha256_file(DASHBOARD) if DASHBOARD.exists() else None,
        "reclassification": previous.get("reclassification"),
    }
    return payload


def persist_compact_state(rows=None):
    if rows is None:
        rows = load()
    payload = compact_state_payload(rows, read_control_state())
    status = atomic_write_text(CONTROL_STATE, stable_json(payload))
    return payload, status


def row_fingerprint(r):
    payload = {k: r.get(k, "") for k in CLASSIFICATION_FIELDS}
    return sha256_bytes(stable_json(payload).encode("utf-8"))


def row_state_fingerprint(r):
    payload = {k: r.get(k, "") for k in REQUIRED}
    return sha256_bytes(stable_json(payload).encode("utf-8"))


def classification_candidates(rows):
    return [r for r in rows if r["type"] in RUNNABLE and r["status"] in {"BACKLOG", "READY"}]


def parse_reclassification_artifact(path: pathlib.Path, required=True):
    """Parse legacy/full Gate intégral tables."""
    entries = {}
    in_gate = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("## Gate intégral"):
            in_gate = True
            continue
        if in_gate and raw.startswith("## "):
            break
        if not in_gate or not raw.startswith("|"):
            continue
        parts = [p.strip() for p in raw.strip().strip("|").split("|", 9)]
        if len(parts) < 10 or not parts[0].startswith("INV-") or parts[1] not in {"PASS", "HOLD"}:
            continue
        score_values = parts[2:9]
        entries[parts[0]] = {
            "gate": parts[1],
            **dict(zip(SCORE_FIELDS, score_values)),
            "motif": parts[9],
        }
    if required and not entries:
        raise SystemExit(f"no Gate intégral entries parsed from {path}")
    return entries


def parse_review_delta(path: pathlib.Path):
    """Parse only the semantically re-evaluated rows of a delta artifact."""
    entries = {}
    in_review = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("## REVIEW"):
            in_review = True
            continue
        if in_review and raw.startswith("## "):
            break
        if not in_review or not raw.startswith("|"):
            continue
        parts = [p.strip() for p in raw.strip().strip("|").split("|", 9)]
        if len(parts) < 10 or not parts[0].startswith("INV-") or parts[1] not in {"PASS", "HOLD"}:
            continue
        entries[parts[0]] = {
            "gate": parts[1],
            **dict(zip(SCORE_FIELDS, parts[2:9])),
            "motif": parts[9],
        }
    return entries


def validate_eval(rid, entry):
    gate = entry.get("gate")
    scores = [entry.get(f, "") for f in SCORE_FIELDS]
    if gate == "PASS":
        bad = [x for x in scores if x not in SCORE_VALUE]
        if bad:
            raise SystemExit(f"{rid} invalid PASS score(s): {','.join(bad)}")
    elif gate == "HOLD":
        if any(x not in {"—", "-"} for x in scores):
            raise SystemExit(f"{rid} HOLD must not carry ranking scores")
    else:
        raise SystemExit(f"{rid} invalid gate={gate}")
    if not str(entry.get("motif", "")).strip():
        raise SystemExit(f"{rid} missing reclassification motif")


def resolve_reclassification_evals(path: pathlib.Path, seen=None):
    """Resolve full semantics from a legacy full table or a chained delta artifact."""
    path = path.resolve()
    seen = set() if seen is None else set(seen)
    if path in seen:
        raise SystemExit(f"reclassification baseline cycle at {path.name}")
    seen.add(path)
    full = parse_reclassification_artifact(path, required=False)
    if full:
        return full
    if frontmatter_scalar(path, "artifact_type") != "routing_reclassification_delta":
        raise SystemExit(f"unsupported reclassification artifact without Gate intégral: {path.name}")
    if frontmatter_scalar(path, "policy_version") != RECLASS_POLICY_VERSION:
        raise SystemExit(f"reclassification policy mismatch in {path.name}")
    base_name = frontmatter_scalar(path, "baseline_artifact")
    base_sha = frontmatter_scalar(path, "baseline_sha256")
    closed = frontmatter_scalar(path, "closed")
    if not base_name or not base_sha or not closed:
        raise SystemExit(f"delta artifact missing baseline/closed metadata: {path.name}")
    base = resolve_path(base_name)
    if not base.exists():
        raise SystemExit(f"missing delta baseline artifact: {base}")
    if sha256_file(base) != base_sha:
        raise SystemExit(f"delta baseline SHA mismatch: {base.name}")
    merged = resolve_reclassification_evals(base, seen)
    merged.pop(closed, None)
    for rid, entry in parse_review_delta(path).items():
        validate_eval(rid, entry)
        merged[rid] = entry
    return merged

def resolve_path(value):
    p = pathlib.Path(value)
    return p if p.is_absolute() else ROOT / p


def frontmatter_scalar(path: pathlib.Path, key: str) -> str | None:
    text = path.read_text(encoding="utf-8")
    m = re.search(rf'^\s*{re.escape(key)}:\s*["\']?([^"\'\n]+)["\']?\s*$', text, re.MULTILINE)
    return m.group(1).strip() if m else None


def reclass_bootstrap(artifact):
    rows = load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    p = resolve_path(artifact)
    if not p.exists():
        raise SystemExit(f"missing reclassification artifact: {p}")
    parsed = resolve_reclassification_evals(p)
    candidates = classification_candidates(rows)
    expected = {r["id"] for r in candidates}
    found = set(parsed)
    if expected != found:
        missing = sorted(expected - found)
        extra = sorted(found - expected)
        raise SystemExit(f"reclassification baseline mismatch: missing={','.join(missing) or 'NONE'} extra={','.join(extra) or 'NONE'}")
    byid = {r["id"]: r for r in rows}
    artifact_selected = frontmatter_scalar(p, "selected")
    current_selected = selected_rows(rows)
    if len(current_selected) == 1 and artifact_selected != current_selected[0]["id"]:
        raise SystemExit(
            f"reclassification selected mismatch: artifact={artifact_selected or 'NONE'} registry={current_selected[0]['id']}"
        )
    if len(current_selected) == 0 and artifact_selected:
        raise SystemExit(f"reclassification artifact selects {artifact_selected} but registry has no current selection")
    reclass = {
        "policy_version": RECLASS_POLICY_VERSION,
        "artifact": p.name,
        "artifact_sha256": sha256_file(p),
        "registry_sha256": sha256_file(REGISTRY),
        "selected": artifact_selected,
        "row_order": [r["id"] for r in rows],
        "row_state_fp": {r["id"]: row_state_fingerprint(r) for r in rows},
        "entries": {
            rid: {
                "fp": row_fingerprint(byid[rid]),
                "eval": [parsed[rid]["gate"], *[parsed[rid][field] for field in SCORE_FIELDS]],
            }
            for rid in sorted(parsed)
        },
    }
    previous = read_control_state()
    previous["reclassification"] = reclass
    payload = compact_state_payload(rows, previous)
    status = atomic_write_text(CONTROL_STATE, stable_json(payload))
    return {"status": "PASS", "mode": "BASELINE", "candidates": len(expected), "artifact": p.name, "write": status}


def reverse_dependency_closure(rows, seeds):
    reverse = {}
    for r in rows:
        for dep in [x for x in r["dependencies"].split(";") if x]:
            reverse.setdefault(dep, set()).add(r["id"])
    seen = set(seeds)
    frontier = list(seeds)
    while frontier:
        cur = frontier.pop()
        for child in reverse.get(cur, ()):
            if child not in seen:
                seen.add(child)
                frontier.append(child)
    return seen


def reclass_plan(changed, impacts, closing=None):
    rows = load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    state = read_control_state()
    baseline = state.get("reclassification")
    current = classification_candidates(rows)
    current_ids = [r["id"] for r in current]
    current_set = set(current_ids)
    known = {r["id"] for r in rows}
    changed = list(dict.fromkeys(changed or []))
    impacts = list(dict.fromkeys(impacts or []))
    if closing:
        if closing not in known:
            raise SystemExit(f"unknown closing INV_ID: {closing}")
        closing_row = next(r for r in rows if r["id"] == closing)
        if closing_row["status"] != "TE_ACTIVE":
            raise SystemExit(f"closing item must be TE_ACTIVE: {closing} status={closing_row['status']}")
        changed = list(dict.fromkeys([closing, *changed]))
    invalid_changed = [x for x in changed if x not in known]
    if invalid_changed:
        raise SystemExit("unknown changed INV_ID: " + ",".join(invalid_changed))

    reasons = []
    if not baseline:
        reasons.append("missing_baseline")
    elif baseline.get("policy_version") != RECLASS_POLICY_VERSION:
        reasons.append("policy_version_changed")
    elif not baseline.get("row_state_fp") or not baseline.get("row_order"):
        reasons.append("baseline_missing_registry_snapshot")
    elif baseline.get("row_order") != [r["id"] for r in rows]:
        reasons.append("registry_order_changed")
    if not impacts:
        reasons.append("impact_frontier_not_declared")
    if "GLOBAL" in impacts:
        reasons.append("global_impact_declared")
    if reasons:
        return {
            "status": "FULL_POOL_REQUIRED",
            "reasons": reasons,
            "current_candidates": len(current_ids),
            "changed": changed,
        }

    if "NONE" in impacts and len(impacts) != 1:
        raise SystemExit("impact NONE cannot be combined with other impact IDs")
    explicit = set() if impacts == ["NONE"] else set(impacts)
    unknown_impact = sorted(x for x in explicit if x not in known)
    if unknown_impact:
        raise SystemExit("unknown impact INV_ID: " + ",".join(unknown_impact))

    entries = baseline.get("entries") or {}
    baseline_set = set(entries)
    byid = {r["id"]: r for r in rows}
    baseline_row_fp = baseline.get("row_state_fp") or {}
    current_row_fp = {r["id"]: row_state_fingerprint(r) for r in rows}
    detected_changed = {
        rid for rid in set(baseline_row_fp) & set(current_row_fp)
        if baseline_row_fp[rid] != current_row_fp[rid]
    }
    detected_changed |= set(current_row_fp) - set(baseline_row_fp)
    detected_changed |= set(baseline_row_fp) - set(current_row_fp)
    effective_changed = set(changed) | (detected_changed & known)
    added = current_set - baseline_set
    removed = baseline_set - current_set
    fingerprint_changed = {
        rid for rid in current_set & baseline_set
        if entries[rid].get("fp") != row_fingerprint(byid[rid])
    }
    dependency_impact = reverse_dependency_closure(rows, effective_changed) & current_set
    review = (added | fingerprint_changed | dependency_impact | explicit) & current_set
    reusable = current_set - review
    order = {rid: i for i, rid in enumerate(r["id"] for r in rows)}
    key = lambda rid: order.get(rid, 10**9)
    return {
        "status": "INCREMENTAL_PLAN",
        "policy_version": RECLASS_POLICY_VERSION,
        "closing": closing,
        "baseline_artifact": baseline.get("artifact"),
        "baseline_artifact_sha256": baseline.get("artifact_sha256"),
        "current_candidates": len(current_ids),
        "changed_declared": changed,
        "changed_detected": sorted(detected_changed & known, key=key),
        "changed_effective": sorted(effective_changed, key=key),
        "explicit_impact": [] if impacts == ["NONE"] else sorted(explicit, key=key),
        "review": sorted(review, key=key),
        "reuse": sorted(reusable, key=key),
        "removed": sorted(removed, key=key),
        "added": sorted(added, key=key),
        "fingerprint_changed": sorted(fingerprint_changed, key=key),
        "dependency_impact": sorted(dependency_impact, key=key),
        "invariant": "reuse means prior evaluation unchanged, not inherited cohort; final ranking still covers the entire current pool",
    }


def cycle(inv_id=None, output=None):
    """Prepare only. Derived dashboard/state are written on real mutations, not preflight."""
    rows = load()
    pf = preflight(inv_id, rows)
    card, card_status = write_card(pf["inv_id"], output, rows)
    return {
        "status": "PASS",
        "inv_id": pf["inv_id"],
        "preflight": "PASS",
        "card": str(card.relative_to(ROOT) if card.is_relative_to(ROOT) else card),
        "card_write": card_status,
        "launch": False,
    }


def handoff_meta(path: pathlib.Path):
    if not path.exists():
        raise SystemExit(f"missing RUN_HANDOFF: {path}")
    if frontmatter_scalar(path, "artifact_type") != "run_handoff":
        raise SystemExit(f"not a RUN_HANDOFF artifact: {path.name}")
    meta = {k: frontmatter_scalar(path, k) for k in (
        "inv_id", "truth_engine", "renard", "reclass_impact", "status"
    )}
    if not meta["inv_id"]:
        raise SystemExit(f"RUN_HANDOFF missing inv_id: {path.name}")
    if meta["truth_engine"] != "DELIVERY_PASS_R3P1":
        raise SystemExit(f"RUN_HANDOFF is not certified DELIVERY_PASS_R3P1: {path.name}")
    if meta["renard"] not in {"NO", "DONE"}:
        raise SystemExit(f"RUN_HANDOFF not closure-authorized: renard={meta['renard'] or 'MISSING'}")
    impacts = split_ids(meta["reclass_impact"] or "")
    if not impacts:
        raise SystemExit(f"RUN_HANDOFF missing reclass_impact: {path.name}")
    if "NONE" in impacts and len(impacts) != 1:
        raise SystemExit("reclass_impact NONE cannot be combined")
    if "GLOBAL" in impacts and len(impacts) != 1:
        raise SystemExit("reclass_impact GLOBAL cannot be combined")
    meta["impacts"] = impacts
    return meta



def winner_from_evals(rows, evals):
    order = {r["id"]: i for i, r in enumerate(rows)}
    candidates = classification_candidates(rows)
    ranked = []
    for r in candidates:
        ev = evals.get(r["id"])
        if not ev:
            raise SystemExit(f"missing merged evaluation for {r['id']}")
        if ev[0] != "PASS":
            continue
        scores = ev[1:]
        if len(scores) != len(SCORE_FIELDS) or any(x not in SCORE_VALUE for x in scores):
            raise SystemExit(f"invalid merged PASS evaluation for {r['id']}")
        ranked.append((tuple(SCORE_VALUE[x] for x in scores), -order[r["id"]], r["id"]))
    if not ranked:
        raise SystemExit("no PASS candidate after reclassification")
    return max(ranked)[2]


def selection_gate(artifact: pathlib.Path, closed: str):
    d = frontmatter_scalar(artifact, "updated")
    if not d or not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", d):
        raise SystemExit(f"delta artifact missing valid updated date: {artifact.name}")
    return f"{PRIMARY_SELECTION_PREFIX}{d}_POST_{closed.replace('-', '')}-R1"


def trace_stamp():
    return datetime.datetime.now(PROJECT_TZ).strftime("%Y-%m-%d %H:%M")


def append_trace_once(token: str, line: str):
    old = TRACELOG.read_text(encoding="utf-8") if TRACELOG.exists() else ""
    if token in old:
        return "UNCHANGED"
    if old and not old.endswith("\n"):
        old += "\n"
    return atomic_write_text(TRACELOG, old + line.rstrip() + "\n")


def apply_post_run(handoff, reclassification):
    rows = load()
    errors = validate(rows)
    if errors:
        raise SystemExit("registry invalid: " + "; ".join(errors))
    hp = resolve_path(handoff)
    rp = resolve_path(reclassification)
    hm = handoff_meta(hp)
    if not rp.exists():
        raise SystemExit(f"missing reclassification delta: {rp}")
    if frontmatter_scalar(rp, "artifact_type") != "routing_reclassification_delta":
        raise SystemExit(f"apply requires routing_reclassification_delta: {rp.name}")
    if frontmatter_scalar(rp, "policy_version") != RECLASS_POLICY_VERSION:
        raise SystemExit("delta artifact policy mismatch")
    closed = hm["inv_id"]
    if frontmatter_scalar(rp, "closed") != closed:
        raise SystemExit("handoff/delta closed INV mismatch")
    selected = frontmatter_scalar(rp, "selected")
    if not selected:
        raise SystemExit("delta artifact missing selected")
    gate = selection_gate(rp, closed)
    byid = {r["id"]: r for r in rows}
    if closed not in byid or selected not in byid:
        raise SystemExit("handoff/delta references unknown INV_ID")

    # Recovery/idempotence path after the canonical registry mutation already landed.
    cr = byid[closed]
    sr = byid[selected]
    if (cr["status"] == "CLOSED" and cr["truth_engine"] == "DELIVERY_PASS_R3P1"
            and cr["result_path"] == hp.name and sr["status"] == "READY" and sr["gate"] == gate):
        resolved = resolve_reclassification_evals(rp)
        current_ids = {r["id"] for r in classification_candidates(rows)}
        if set(resolved) != current_ids:
            raise SystemExit("applied registry and delta artifact candidate sets diverge")
        if winner_from_evals(rows, {rid: [e["gate"], *[e[f] for f in SCORE_FIELDS]] for rid, e in resolved.items()}) != selected:
            raise SystemExit("applied selected item is not delta winner")
        write_dashboard(rows)
        previous = read_control_state()
        previous["reclassification"] = {
            "policy_version": RECLASS_POLICY_VERSION,
            "artifact": rp.name,
            "artifact_sha256": sha256_file(rp),
            "registry_sha256": sha256_file(REGISTRY),
            "selected": selected,
            "row_order": [r["id"] for r in rows],
            "row_state_fp": {r["id"]: row_state_fingerprint(r) for r in rows},
            "entries": {rid: {"fp": row_fingerprint(byid[rid]), "eval": [e["gate"], *[e[f] for f in SCORE_FIELDS]]} for rid, e in sorted(resolved.items())},
        }
        atomic_write_text(CONTROL_STATE, stable_json(compact_state_payload(rows, previous)))
        card, card_write = write_card(selected, rows=rows)
        token = f"| CONTROL_APPLY | {closed} |"
        stamp = trace_stamp()
        append_trace_once(token, f"{stamp} | CONTROL_APPLY | {closed} | recovered/idempotent; next={selected} READY; artifact={rp.name}; mechanical-only.")
        return {"status": "ALREADY_APPLIED", "closed": closed, "selected": selected, "card": card.name, "card_write": card_write}

    if cr["status"] != "TE_ACTIVE":
        raise SystemExit(f"apply requires {closed} TE_ACTIVE or an exactly applied transition; status={cr['status']}")
    active = selected_rows(rows)
    if len(active) != 1 or active[0]["id"] != closed:
        raise SystemExit(f"{closed} is not the unique TE_ACTIVE selection")
    state = read_control_state()
    baseline = state.get("reclassification") or {}
    if baseline.get("policy_version") != RECLASS_POLICY_VERSION:
        raise SystemExit("missing current reclassification baseline")
    if frontmatter_scalar(rp, "baseline_artifact") != baseline.get("artifact"):
        raise SystemExit("delta baseline artifact is not current")
    if frontmatter_scalar(rp, "baseline_sha256") != baseline.get("artifact_sha256"):
        raise SystemExit("delta baseline SHA is not current")

    plan = reclass_plan([], hm["impacts"], closing=closed)
    if plan.get("status") != "INCREMENTAL_PLAN":
        raise SystemExit("delta apply refused: " + ",".join(plan.get("reasons", [])))
    review = parse_review_delta(rp)
    if set(review) != set(plan["review"]):
        raise SystemExit(f"delta REVIEW mismatch: expected={','.join(plan['review']) or 'NONE'} got={','.join(sorted(review)) or 'NONE'}")
    for rid, entry in review.items():
        validate_eval(rid, entry)

    evals = {}
    for rid in plan["reuse"]:
        prior = (baseline.get("entries") or {}).get(rid)
        if not prior:
            raise SystemExit(f"missing reusable baseline evaluation: {rid}")
        evals[rid] = list(prior["eval"])
    for rid, entry in review.items():
        evals[rid] = [entry["gate"], *[entry[f] for f in SCORE_FIELDS]]
    candidate_ids = {r["id"] for r in classification_candidates(rows)}
    if set(evals) != candidate_ids:
        raise SystemExit("merged delta does not cover the entire current candidate pool")
    computed = winner_from_evals(rows, evals)
    if selected != computed:
        raise SystemExit(f"selected mismatch: artifact={selected} computed={computed}")
    if sr["status"] != "BACKLOG" or sr["type"] not in RUNNABLE:
        raise SystemExit(f"winner is not selectable BACKLOG PRIMARY|CASE: {selected}")
    if not sr["object_question"].strip() or not sr["scope"].strip():
        raise SystemExit(f"winner contract incomplete; repair semantically before apply: {selected}")

    newrows = [dict(r) for r in rows]
    nb = {r["id"]: r for r in newrows}
    c = nb[closed]
    c["status"] = "CLOSED"
    c["truth_engine"] = "DELIVERY_PASS_R3P1"
    c["renard"] = hm["renard"]
    c["result_path"] = hp.name
    c["next_action"] = "NONE - CLOSED; see RUN_HANDOFF."
    w = nb[selected]
    w["status"] = "READY"
    w["gate"] = gate
    w["truth_engine"] = "NOT_RUN"
    w["renard"] = ""
    w["result_path"] = ""
    w["next_action"] = "Run-card gate, then launch only if PASS."
    errors = validate(newrows)
    if errors:
        raise SystemExit("post-apply registry invalid: " + "; ".join(errors))

    new_registry_bytes = registry_bytes(newrows)
    new_registry_sha = sha256_bytes(new_registry_bytes)
    new_candidates = classification_candidates(newrows)
    new_ids = {r["id"] for r in new_candidates}
    if new_ids != set(evals):
        raise SystemExit("post-apply candidate set changed unexpectedly")
    new_byid = {r["id"]: r for r in newrows}
    new_reclass = {
        "policy_version": RECLASS_POLICY_VERSION,
        "artifact": rp.name,
        "artifact_sha256": sha256_file(rp),
        "registry_sha256": new_registry_sha,
        "selected": selected,
        "row_order": [r["id"] for r in newrows],
        "row_state_fp": {r["id"]: row_state_fingerprint(r) for r in newrows},
        "entries": {rid: {"fp": row_fingerprint(new_byid[rid]), "eval": evals[rid]} for rid in sorted(new_ids)},
    }

    # Registry is canonical: land it first. Any later partial write is recoverable by rerunning apply.
    if REGISTRY.read_bytes() != new_registry_bytes:
        tmp = REGISTRY.with_name(f".{REGISTRY.name}.tmp-{os.getpid()}")
        tmp.write_bytes(new_registry_bytes)
        os.replace(tmp, REGISTRY)
    write_dashboard(newrows)
    previous = read_control_state()
    previous["reclassification"] = new_reclass
    atomic_write_text(CONTROL_STATE, stable_json(compact_state_payload(newrows, previous)))
    card, card_write = write_card(selected, rows=newrows)
    token = f"| CONTROL_APPLY | {closed} |"
    stamp = trace_stamp()
    trace_write = append_trace_once(
        token,
        f"{stamp} | CONTROL_APPLY | {closed} | DELIVERY_PASS_R3P1 -> CLOSED; REVIEW={len(plan['review'])}; REUSE={len(plan['reuse'])}; next={selected} READY; artifact={rp.name}; mechanical-only."
    )
    return {
        "status": "PASS", "closed": closed, "selected": selected, "gate": gate,
        "review": plan["review"], "reuse_count": len(plan["reuse"]),
        "registry_sha256": sha256_file(REGISTRY), "card": card.name,
        "card_write": card_write, "trace_write": trace_write,
    }

def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("validate")
    pf = sp.add_parser("preflight")
    pf.add_argument("inv_id", nargs="?")
    sp.add_parser("dashboard")
    rc = sp.add_parser("run-card")
    rc.add_argument("inv_id")
    rc.add_argument("--output")
    sc = sp.add_parser("synthesis-card")
    sc.add_argument("inv_id")
    sc.add_argument("--output")
    for name in ("cycle", "batch"):
        cp = sp.add_parser(name)
        cp.add_argument("inv_id", nargs="?")
        cp.add_argument("--output")
    sp.add_parser("state")
    rb = sp.add_parser("reclass-bootstrap")
    rb.add_argument("--artifact", required=True)
    rp = sp.add_parser("reclass-plan")
    rp.add_argument("--changed", action="append", default=[])
    rp.add_argument("--impact", action="append", default=[])
    rp.add_argument("--closing")
    rp.add_argument("--handoff")
    ap = sp.add_parser("apply")
    ap.add_argument("--handoff", required=True)
    ap.add_argument("--reclassification", required=True)
    a = p.parse_args()

    if a.cmd == "validate":
        errors = validate()
        if errors:
            for e in errors:
                print("FAIL", e)
            raise SystemExit(1)
        print("PASS")
    elif a.cmd == "preflight":
        print(stable_json(preflight(a.inv_id)).strip())
    elif a.cmd == "dashboard":
        path, status = write_dashboard()
        print(f"{status} {path}")
    elif a.cmd == "run-card":
        run_card(a.inv_id, a.output)
    elif a.cmd == "synthesis-card":
        synthesis_card(a.inv_id, a.output)
    elif a.cmd in {"cycle", "batch"}:
        print(stable_json(cycle(a.inv_id, a.output)).strip())
    elif a.cmd == "state":
        payload, status = persist_compact_state()
        print(f"{status} {CONTROL_STATE}")
        print(stable_json(payload).strip())
    elif a.cmd == "reclass-bootstrap":
        print(stable_json(reclass_bootstrap(a.artifact)).strip())
    elif a.cmd == "reclass-plan":
        changed, impacts, closing = a.changed, a.impact, a.closing
        if a.handoff:
            hm = handoff_meta(resolve_path(a.handoff))
            if closing and closing != hm["inv_id"]:
                raise SystemExit("--closing conflicts with RUN_HANDOFF inv_id")
            if impacts:
                raise SystemExit("use either --handoff or --impact, not both")
            closing, impacts = hm["inv_id"], hm["impacts"]
        print(stable_json(reclass_plan(changed, impacts, closing=closing)).strip())
    else:
        print(stable_json(apply_post_run(a.handoff, a.reclassification)).strip())


if __name__ == "__main__":
    main()
