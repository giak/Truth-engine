#!/usr/bin/env python3
"""Minimal post-Truth-Engine helper.

Scope is deliberately narrow:
- handoff: deterministic projection of certified Truth Engine artifacts + 3 semantic inputs
- delta: deterministic routing delta from control.py reclass-plan + explicit REVIEW decisions

It does not modify Truth Engine, the registry, CONTROL_STATE, or any certification artifact.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

PROJECT = "democracy-influence-investigations"
POLICY = "CORE_MISSION_V2/ranking-7/v1"


def die(msg: str) -> "NoReturn":
    raise SystemExit(msg)


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: pathlib.Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        die(f"invalid JSON {path}: {exc}")


def atomic_write(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def scalar_frontmatter(path: pathlib.Path, key: str) -> str | None:
    text = path.read_text(encoding="utf-8")
    m = re.search(rf'^\s*{re.escape(key)}:\s*["\']?([^"\'\n]+)["\']?\s*$', text, re.MULTILINE)
    return m.group(1).strip() if m else None


def load_control(path: pathlib.Path):
    spec = importlib.util.spec_from_file_location("post_run_control", path)
    if spec is None or spec.loader is None:
        die(f"cannot import control.py: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def validate_certified_run(state_path: pathlib.Path, cert_path: pathlib.Path):
    state = load_json(state_path)
    cert = load_json(cert_path)
    run = state.get("run") or {}

    required = {
        "cert.verdict": cert.get("verdict") == "PASS",
        "cert.kernel_contract": cert.get("kernel_contract") == "delivery",
        "cert.deterministic": cert.get("deterministic") == "PASS",
        "cert.state_changed": cert.get("state_changed") is False,
        "cert.deliverable_changed": cert.get("deliverable_changed") is False,
        "run.state": run.get("state") == "FINAL",
        "engine": state.get("engine") == "2.10.6",
    }
    bad = [k for k, ok in required.items() if not ok]
    if bad:
        die("handoff refused: uncertified/nonterminal input: " + ",".join(bad))

    investigation_path = pathlib.Path(run.get("investigation_path") or "")
    if not investigation_path.is_file():
        # Allow standard exported sibling without weakening hash verification.
        inv_guess = state_path.with_name(state_path.name.replace("_RUN_STATE.json", "_INVESTIGATION.md"))
        if inv_guess.is_file():
            investigation_path = inv_guess
        else:
            die(f"handoff refused: deliverable not found: {run.get('investigation_path')}")
    got = sha256_file(investigation_path)
    expected = cert.get("deliverable_sha256")
    if not expected or got != expected:
        die(f"handoff refused: deliverable SHA mismatch expected={expected} got={got}")

    attempts = (state.get("persistence") or {}).get("attempt_history") or []
    if not attempts or attempts[-1].get("result") != "PASS":
        die("handoff refused: terminal persistence is not PASS")
    return state, cert, investigation_path, attempts[-1]


def semantic_text(path: pathlib.Path | None, placeholder: str) -> str:
    if path is None:
        return placeholder
    text = path.read_text(encoding="utf-8").strip()
    return text or placeholder


def cmd_handoff(args):
    state_path = pathlib.Path(args.state).resolve()
    cert_path = pathlib.Path(args.cert).resolve()
    out = pathlib.Path(args.out).resolve()
    state, cert, investigation_path, persistence = validate_certified_run(state_path, cert_path)
    run = state["run"]
    inv = args.inv.strip()
    if not re.fullmatch(r"INV-\d{3}", inv):
        die(f"invalid inv id: {inv}")

    central = semantic_text(pathlib.Path(args.central_delta).resolve() if args.central_delta else None,
                            "{{CENTRAL_DELTA}}")
    renard = args.renard or "PENDING"
    impact = args.impact or "PENDING"
    if renard not in {"NO", "DONE", "PENDING"}:
        die("renard must be NO, DONE or omitted")
    if impact != "PENDING":
        ids = [x for x in impact.split(";") if x]
        if not ids or ("NONE" in ids and len(ids) != 1) or ("GLOBAL" in ids and len(ids) != 1):
            die("invalid impact")
        for x in ids:
            if x not in {"NONE", "GLOBAL"} and not re.fullmatch(r"INV-\d{3}", x):
                die(f"invalid impact id: {x}")

    terminal = central != "{{CENTRAL_DELTA}}" and renard in {"NO", "DONE"} and impact != "PENDING"
    status = "terminal" if terminal else "draft"
    counters = state.get("counters") or {}
    families = sorted({fam for fact in state.get("facts") or [] for fam in fact.get("families") or []})
    wb = persistence.get("writeback_row") or {}
    fake_ids = sum(1 for f in state.get("facts") or [] if f.get("mem") not in {None, "", "-"})

    causal_lines = []
    for row in state.get("causal") or []:
        mech = str(row.get("mechanism") or "").strip()
        st = str(row.get("status") or "").strip()
        limit = str(row.get("limit") or "").strip()
        if mech and st:
            line = f"- `{mech}` = **{st}**"
            if limit:
                line += f" — {limit}"
            causal_lines.append(line)
    if not causal_lines:
        causal_lines = ["- NONE"]

    gaps = []
    for clm in state.get("claims") or []:
        gt = str(clm.get("gap_type") or "").strip()
        gap = str(clm.get("gap") or "").strip()
        if gt and gt != "NONE" and gap and gap != "NONE":
            gaps.append(f"- `{clm.get('id','?')}` / **{gt}** — {gap}")
    if not gaps:
        gaps = ["- NONE"]

    text = f'''---
trace_schema: "forensic-md/v1"
project: "{PROJECT}"
artifact_type: "run_handoff"
status: "{status}"
inv_id: "{inv}"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "{renard}"
reclass_impact: "{impact}"
updated: "{run.get('as_of')}"
---

# RUN_HANDOFF — {inv}

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `{run.get('run_id')}`
- Deliverable: `{inv}_INVESTIGATION.md`
- Deliverable SHA-256: `{cert.get('deliverable_sha256')}`
- Corpus runtime: `QRY={counters.get('QRY',0)} / SRC={counters.get('SRC',0)} / FCT={counters.get('FCT',0)} / provenance_families={len(families)}`
- Persistence: `PASS / eligible={wb.get('eligible',0)} / blocked={wb.get('blocked',0)} / success={wb.get('success',0)} / failure={wb.get('failure',0)} / fabricated_memory_ids={fake_ids}`

## Delta central

{central}

## Registre causal certifié

{chr(10).join(causal_lines)}

## Gaps matériels certifiés

{chr(10).join(gaps)}

## RENARD

`{renard}`

## Reclassification

Impact direct : `{impact}`.

## Transition attendue

`{inv} TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD={renard}`, puis sélection mécanique du gagnant après REVIEW explicite.
'''
    atomic_write(out, text)
    result = {
        "status": "PASS",
        "mode": "terminal" if terminal else "draft",
        "out": str(out),
        "run_id": run.get("run_id"),
        "deliverable_sha256": cert.get("deliverable_sha256"),
        "counts": {k: counters.get(k, 0) for k in ("QRY", "SRC", "FCT", "CLM", "CAU", "CTRL", "ACT")},
        "provenance_families": families,
        "review_semantic_fields_remaining": 0 if terminal else 3,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


def load_registry(path: pathlib.Path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def normalize_review(item, control):
    rid = item.get("inv") or item.get("id")
    gate = item.get("gate")
    motif = str(item.get("motif") or "").strip()
    if not rid or not motif:
        die("each review requires inv/id and motif")
    if gate == "HOLD":
        entry = {"gate": "HOLD", **{f: "—" for f in control.SCORE_FIELDS}, "motif": motif}
    elif gate == "PASS":
        scores = item.get("scores") or {}
        entry = {"gate": "PASS", **{f: scores.get(f, "") for f in control.SCORE_FIELDS}, "motif": motif}
    else:
        die(f"{rid} invalid gate={gate}")
    control.validate_eval(rid, entry)
    return rid, entry


def cmd_delta(args):
    plan_path = pathlib.Path(args.plan).resolve()
    reviews_path = pathlib.Path(args.reviews).resolve()
    registry_path = pathlib.Path(args.registry).resolve()
    state_path = pathlib.Path(args.control_state).resolve()
    control_path = pathlib.Path(args.control).resolve()
    handoff_path = pathlib.Path(args.handoff).resolve()
    out = pathlib.Path(args.out).resolve()

    control = load_control(control_path)
    plan = load_json(plan_path)
    reviews_doc = load_json(reviews_path)
    state = load_json(state_path)
    rows = load_registry(registry_path)

    if plan.get("status") != "INCREMENTAL_PLAN":
        die(f"delta refused: plan status={plan.get('status')}")
    if plan.get("policy_version") != POLICY:
        die("delta refused: policy mismatch")
    closed = plan.get("closing")
    if not closed:
        die("delta refused: plan missing closing")
    if scalar_frontmatter(handoff_path, "inv_id") != closed:
        die("delta refused: handoff/plan closing mismatch")
    if scalar_frontmatter(handoff_path, "truth_engine") != "DELIVERY_PASS_R3P1":
        die("delta refused: handoff not DELIVERY_PASS_R3P1")
    if scalar_frontmatter(handoff_path, "status") != "terminal":
        die("delta refused: handoff not terminal")

    baseline = (state.get("reclassification") or {})
    if baseline.get("policy_version") != POLICY:
        die("delta refused: current baseline policy mismatch")
    if baseline.get("artifact") != plan.get("baseline_artifact"):
        die("delta refused: plan baseline artifact is not current")
    if baseline.get("artifact_sha256") != plan.get("baseline_artifact_sha256"):
        die("delta refused: plan baseline SHA is not current")

    items = reviews_doc.get("reviews")
    if not isinstance(items, list):
        die("reviews JSON must contain a reviews array")
    review_entries = {}
    for item in items:
        rid, entry = normalize_review(item, control)
        if rid in review_entries:
            die(f"duplicate review: {rid}")
        review_entries[rid] = entry
    expected_review = list(plan.get("review") or [])
    if set(review_entries) != set(expected_review):
        die(f"delta refused: REVIEW mismatch expected={','.join(expected_review) or 'NONE'} got={','.join(sorted(review_entries)) or 'NONE'}")

    evals = {}
    base_entries = baseline.get("entries") or {}
    for rid in plan.get("reuse") or []:
        prior = base_entries.get(rid)
        if not prior:
            die(f"delta refused: missing reusable baseline evaluation {rid}")
        evals[rid] = list(prior.get("eval") or [])
    for rid, entry in review_entries.items():
        evals[rid] = [entry["gate"], *[entry[f] for f in control.SCORE_FIELDS]]

    candidate_ids = {r["id"] for r in control.classification_candidates(rows)}
    if set(evals) != candidate_ids:
        die("delta refused: merged evaluations do not cover current candidate pool")
    selected = control.winner_from_evals(rows, evals)
    byid = {r["id"]: r for r in rows}
    winner = byid[selected]
    if not winner.get("object_question", "").strip() or not winner.get("scope", "").strip():
        die(f"delta refused: winner contract incomplete: {selected}")

    updated = scalar_frontmatter(handoff_path, "updated")
    if not updated or not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", updated):
        die("delta refused: invalid handoff updated date")
    artifact_id = f"RECLASSIFICATION-POST-{closed.replace('-', '')}-{updated}-DELTA-R1"
    removed = ",".join(plan.get("removed") or []) or "NONE"
    review_csv = ",".join(expected_review) or "NONE"
    reuse_count = len(plan.get("reuse") or [])
    pool = len(candidate_ids)
    repair_review = bool(plan.get("fingerprint_changed"))

    rows_md = []
    for rid in expected_review:
        e = review_entries[rid]
        vals = [rid, e["gate"], *[e[f] for f in control.SCORE_FIELDS], e["motif"].replace("|", "/")]
        rows_md.append("| " + " | ".join(vals) + " |")

    text = f'''---
trace_schema: "forensic-md/v1"
project: "{PROJECT}"
artifact_type: "routing_reclassification_delta"
artifact_id: "{artifact_id}"
version: "1.0-kiss"
status: "final"
updated: "{updated}"
policy_version: "{POLICY}"
closed: "{closed}"
baseline_artifact: "{plan.get('baseline_artifact')}"
baseline_sha256: "{plan.get('baseline_artifact_sha256')}"
selected: "{selected}"
---

<!-- TRACE: incremental=true; current_pool_after_close={pool}; review={review_csv}; reuse={reuse_count}; removed={removed}; full_pool_ranking=true -->
<!-- DECISION: priority_unused=true; winner={selected}; contract_repair_forced_review={str(repair_review).lower()}; delta_generated=true -->

# Reclassification delta post-{closed} — CORE_MISSION_V2

## Delta matériel

Voir `{handoff_path.name}`. Ce fichier ne répète pas l'analyse certifiée ; seules les lignes REVIEW ci-dessous sont réévaluées sémantiquement.

## REVIEW

| INV | Gate | model_change | discrimination | effect_closure | symmetry_value | dependency_unlock | coverage_gap | utility | Motif |
|---|---|---|---|---|---|---|---|---|---|
{chr(10).join(rows_md)}

## Verdict

`{selected}` est le gagnant lexicographique du full-pool fusionné après retrait de `{closed}` et application exacte des REVIEW. `priority=P1/P2` n'est pas utilisée. Le contrat du gagnant est complet avant `apply`.
'''
    atomic_write(out, text)
    print(json.dumps({
        "status": "PASS",
        "out": str(out),
        "closed": closed,
        "selected": selected,
        "review": expected_review,
        "reuse_count": reuse_count,
        "baseline_artifact": plan.get("baseline_artifact"),
        "baseline_sha256": plan.get("baseline_artifact_sha256"),
    }, ensure_ascii=False, sort_keys=True))


def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)

    h = sp.add_parser("handoff")
    h.add_argument("--inv", required=True)
    h.add_argument("--state", required=True)
    h.add_argument("--cert", required=True)
    h.add_argument("--out", required=True)
    h.add_argument("--central-delta")
    h.add_argument("--renard", choices=["NO", "DONE"])
    h.add_argument("--impact")
    h.set_defaults(func=cmd_handoff)

    d = sp.add_parser("delta")
    d.add_argument("--plan", required=True)
    d.add_argument("--reviews", required=True)
    d.add_argument("--registry", required=True)
    d.add_argument("--control-state", required=True)
    d.add_argument("--control", required=True)
    d.add_argument("--handoff", required=True)
    d.add_argument("--out", required=True)
    d.set_defaults(func=cmd_delta)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
