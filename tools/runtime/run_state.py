#!/usr/bin/env python3
"""Truth Engine 2.10 lightweight deterministic run-state helper.

Owns only mechanics: atomic JSON state, ID allocation, request/source/fact bookkeeping,
checkpoint accounting, warm snapshot import/export and deterministic machine-block rendering.
It does not search the web, judge evidence, assign epistemic meaning, or replace KERNEL.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

SCHEMA = 1
ENGINE = "2.10.6"
BUNDLE_REVISION = "R2A.1"
ID_KINDS = ("SYS", "QRY", "SRC", "FCT", "LED", "CLM", "AXS", "CAU", "CTRL", "ACT", "CP")
DELTA_CLASSES = {"REUSE", "RECHECK", "NEW", "GAP"}
CHECKPOINT_RANK = {"LEADS":5,"SCOPE":7,"SEARCH":9,"SEARCH_PARTIAL":9,"FACTS":10,"CAUSAL":11,"CAUSAL_GAP":11,"VERIFY":13,"INVESTIGATION_ACCOUNTABILITY":17,"CORRECTION":18,"FINALIZATION_BLOCKED":18}
QRY_MODES = {"WEB", "FETCH", "EXA"}
VALID_EPI = {"FACT", "EVIDENCE", "INFERENCE", "HYPOTHESIS", "SPECULATION", "UNKNOWN"}
VALID_TIER = {"✦", "✧", "⁅", "❧"}
SOURCE_ROLES = {"◈", "◉", "○"}
OBJECT_KINDS = ("LED","CLM","AXS","CAU","CTRL","ACT")
OBJECT_BUCKETS = {"LED":"leads","CLM":"claims","AXS":"axes","CAU":"causal","CTRL":"controls","ACT":"actions"}

FAMILY_RE = re.compile(r"^(?:[A-E]|other:[a-z0-9][a-z0-9_-]{0,47})$")
REQUIRED_ALWAYS_LOAD = {
    "definitions/SYMBOLS.md", "definitions/PATTERNS.md", "definitions/THREATS.md",
    "forensic/GATES.md", "forensic/REQUEST_LOG.md",
}

CANONICAL_SECTIONS = (
    "TEMPORAL_STATE", "MANIPULATION_REPORT", "SCOPING_REPORT", "CREDO",
    "LEAD_REGISTRY", "INVESTIGATION_MAP", "COGNITIVE_MAP", "DIALECTICAL_MAP",
    "CLAIM_REGISTRY", "RESOURCE_FLOW_MAP", "ACTOR_NETWORK_MAP", "CONTROL_MAP",
    "CAUSALITY_REGISTRY", "IMPACT_MAP", "STATUS_DELTA", "CONTRADICTION_LEDGER",
    "VERIFICATION_REPORT", "TRACE_MATRIX", "EDI_REPORT", "RESPONSIBILITY_MAP",
    "OPEN_GAPS", "NEXT_QUERIES", "GATE_STATUS_V1",
)

# These sections are exact projections of runtime-owned registries. Keeping a
# second mutable copy would create two authorities for the same information.
DERIVED_SECTIONS = {
    "LEAD_REGISTRY", "INVESTIGATION_MAP", "CLAIM_REGISTRY", "CONTROL_MAP",
    "CAUSALITY_REGISTRY", "STATUS_DELTA", "TRACE_MATRIX", "OPEN_GAPS",
}
REQUIRED_REPORT_SECTIONS = tuple(
    x for x in CANONICAL_SECTIONS if x not in DERIVED_SECTIONS and x != "GATE_STATUS_V1"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def die(msg: str, code: int = 2) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def load(path: str | Path) -> dict:
    p = Path(path)
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError:
        die(f"state not found: {p}")
    except json.JSONDecodeError as e:
        die(f"invalid state JSON: {e}")
    if obj.get("schema") != SCHEMA:
        die(f"unsupported state schema: {obj.get('schema')}")
    return obj


def atomic_write(path: str | Path, obj: dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    fd, tmp = tempfile.mkstemp(prefix=p.name + ".", suffix=".tmp", dir=str(p.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)



def atomic_write_text(path: str | Path, text: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=p.name + ".", suffix=".tmp", dir=str(p.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def archive_replayed_artifacts(paths: dict) -> str | None:
    """Move an overwritten run generation aside before `init --force`.

    Canonical derived paths must become absent so a replay cannot silently
    reuse a narrative, snapshot, delivery or certification with reallocated
    IDs. The previous generation remains recoverable in `_replay_backups`.
    """
    candidates = []
    state_path = Path(paths["state_path"])
    if state_path.is_file():
        candidates.append(state_path)
        try:
            previous = json.loads(state_path.read_text(encoding="utf-8"))
            prior_input = Path(previous.get("run", {}).get("input_path", ""))
            if prior_input.is_file():
                candidates.append(prior_input)
        except Exception:
            pass
    for key in ("narrative_path", "snapshot_path", "investigation_path", "certification_path"):
        p = Path(paths[key])
        if p.is_file():
            candidates.append(p)
    unique = []
    seen = set()
    for p in candidates:
        rp = str(p.resolve())
        if rp not in seen:
            unique.append(p)
            seen.add(rp)
    if not unique:
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    backup = Path(paths["run_dir"]) / "_replay_backups" / stamp
    backup.mkdir(parents=True, exist_ok=False)
    for src in unique:
        os.replace(src, backup / src.name)
    return str(backup)

def mutate(path: str | Path, fn):
    state = load(path)
    fn(state)
    state["meta"]["updated_at"] = now_iso()
    atomic_write(path, state)
    return state


def next_id(state: dict, kind: str) -> str:
    if kind not in ID_KINDS:
        die(f"unsupported ID kind: {kind}")
    state["counters"][kind] = int(state["counters"].get(kind, 0)) + 1
    return f"{kind}-{state['counters'][kind]:03d}"


def parse_json_value(raw: str):
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        die(f"invalid --json payload: {e}")

def read_json_input(a):
    modes = [getattr(a, "json", None) is not None, getattr(a, "json_file", None) is not None, bool(getattr(a, "stdin", False))]
    if sum(modes) != 1:
        die("provide exactly one of --json, --json-file, --stdin")
    if getattr(a, "json", None) is not None:
        return parse_json_value(a.json)
    if getattr(a, "json_file", None) is not None:
        try:
            return json.loads(Path(a.json_file).read_text(encoding="utf-8"))
        except Exception as e:
            die(f"cannot read --json-file: {e}")
    try:
        return json.load(sys.stdin)
    except Exception as e:
        die(f"cannot read JSON from stdin: {e}")

def canonical_run_paths(root: str, as_of: str, run_id: str, slug: str, input_suffix: str = ".txt") -> dict:
    m = re.match(r"^\d{8}-(\d{2})(\d{2})-", run_id)
    if not m:
        die("run_id must start YYYYMMDD-HHMM-")
    hh, mm = m.groups()
    ym = as_of[:7]
    run_dir = Path(root) / "investigations" / ym / f"{as_of}_{slug}"
    prefix = f"{as_of}_{hh}-{mm}_{slug}"
    suffix = input_suffix if input_suffix.startswith(".") else "." + input_suffix
    return {
        "run_dir": str(run_dir),
        "state_path": str(run_dir / f"{prefix}_RUN_STATE.json"),
        "narrative_path": str(run_dir / f"{prefix}_NARRATIVE.tmp.md"),
        "snapshot_path": str(run_dir / f"{prefix}_MNEMO_SNAPSHOT.json"),
        "investigation_path": str(run_dir / f"{prefix}_INVESTIGATION.md"),
        "certification_path": str(run_dir / f"{prefix}_CERTIFICATION.json"),
        "input_path": str(run_dir / f"{prefix}_INPUT{suffix}"),
    }

def canonical_inv_path(root: str, as_of: str, run_id: str, slug: str) -> str:
    return canonical_run_paths(root, as_of, run_id, slug)["investigation_path"]

def _fingerprint_v1_text(text: str) -> bytes:
    text = unicodedata.normalize("NFKC", text).replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\s+", " ", text).strip().encode("utf-8")


def _fingerprint_v2_text(text: str) -> bytes:
    # Bound typographic normalization only. Do not lowercase, strip accents,
    # remove emoji or otherwise merge semantically distinct documents.
    text = unicodedata.normalize("NFKC", text).replace("\r\n", "\n").replace("\r", "\n")
    table = str.maketrans({
        "\u2018": "'", "\u2019": "'", "\u201b": "'", "\u2032": "'", "\u02bc": "'",
        "\u201c": '"', "\u201d": '"', "\u201f": '"', "\u2033": '"', "\u00ab": '"', "\u00bb": '"',
        "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-", "\u2014": "-", "\u2212": "-",
        "\u00a0": " ", "\u202f": " ",
        "\u2026": "...",
    })
    text = text.translate(table)
    return re.sub(r"\s+", " ", text).strip().encode("utf-8")


def canonical_text_fingerprint(raw: bytes) -> tuple[str,str,str]:
    raw_h = hashlib.sha256(raw).hexdigest()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        # Binary inputs remain byte-identity only; V2 and legacy V1 coincide.
        fp = "sha256:" + raw_h
        return fp, raw_h, fp
    v1 = "sha256:" + hashlib.sha256(_fingerprint_v1_text(text)).hexdigest()
    v2 = "sha256:" + hashlib.sha256(_fingerprint_v2_text(text)).hexdigest()
    return v2, raw_h, v1

def validate_family_token(value: str) -> None:
    machine_field("family", value)
    if value.startswith("fam:") or not FAMILY_RE.fullmatch(value):
        die("family must be bare A|B|C|D|E or other:stable-token (never fam:A)")

def url_specific_enough(url: str) -> bool:
    if not url.startswith(("http://","https://")):
        return True
    u=urlparse(url)
    path=(u.path or "").rstrip("/")
    if not path:
        return False
    generic={"/news/en/press-room", "/news", "/", "/en", "/fr"}
    return path.lower() not in generic

def trivial_url_inconsistency(url: str, subject: str, value: str) -> str | None:
    m=re.search(r"CELEX:(\d{5})([LDR])(\d+)", url, re.I)
    text=(subject+" "+value).lower()
    if m and m.group(2).upper()=="L" and any(x in text for x in ("regl", "regulation", "règlement")):
        return "CELEX type L (directive) conflicts with fact text claiming regulation/règlement"
    return None



def machine_field(name: str, value: str, allow_empty: bool = False) -> str:
    if value is None:
        value = ""
    if not allow_empty and value == "":
        die(f"{name} must be non-empty")
    if "|" in value or "\n" in value or "\r" in value:
        die(f"{name} contains forbidden machine-row delimiter/newline")
    return value

def source_by_id(state: dict, sid: str) -> dict | None:
    return next((x for x in state["sources"] if x["id"] == sid), None)


def fact_by_id(state: dict, fid: str) -> dict | None:
    return next((x for x in state["facts"] if x["id"] == fid), None)


def object_by_id(state: dict, oid: str) -> tuple[str, dict] | tuple[None, None]:
    m = re.match(r"^(LED|CLM|AXS|CAU|CTRL|ACT)-\d{3}$", oid or "")
    if not m:
        return None, None
    kind = m.group(1)
    row = next((x for x in state.get(OBJECT_BUCKETS[kind], []) if x.get("id") == oid), None)
    return kind, row


def hydrated_fact_by_key(state: dict, key: str) -> dict | None:
    h = state.get("hydrated") or {}
    return next((x for x in h.get("facts", []) if x.get("key") == key), None)


def delta_by_key(state: dict, key: str) -> dict | None:
    return next((x for x in state.get("delta_plan", []) if x.get("key") == key), None)


def query_by_id(state: dict, qid: str) -> dict | None:
    return next((x for x in state["requests"] if x["id"] == qid), None)


def _semantic_tokens(value: str) -> list[str]:
    """Return stable, accent-insensitive tokens for a bounded identity check."""
    raw = unicodedata.normalize("NFKD", value or "")
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch)).lower()
    return re.findall(r"[a-z0-9]+", raw)


def refutation_alignment_error(fact: dict, query: dict) -> str | None:
    """Check that a refutation query visibly targets the selected fact.

    This is deliberately a narrow lexical contract, not a semantic judgement:
    the query must declare itself as a refutation and carry a stable subject
    anchor (including every numeric discriminator such as CONTROL-1 vs -2).
    """
    result = str(query.get("result", "")).strip().upper()
    if result.startswith(("FAIL", "ERROR", "BLOCKED", "UNEXECUTED")):
        return f"query result {result or 'EMPTY'} is not an executed refutation"
    query_text = str(query.get("query", "")).strip()
    if not re.match(r"(?i)^REFUTATION(?:\b|[_:-])", query_text):
        return "query text must start with REFUTATION"
    subject_tokens = _semantic_tokens(str(fact.get("subject", "")))
    query_tokens = set(_semantic_tokens(query_text))
    numeric = {t for t in subject_tokens if t.isdigit()}
    if not numeric.issubset(query_tokens):
        return "query is missing a numeric discriminator from the fact subject"
    stop = {
        "a", "an", "and", "control", "controle", "d", "de", "des", "du", "et",
        "fact", "fait", "la", "le", "les", "l", "of", "ou", "the", "un", "une",
    }
    anchors = {t for t in subject_tokens if not t.isdigit() and len(t) >= 3 and t not in stop}
    # Generic test/legacy subjects named simply "fact" still need an explicit
    # subject echo; only discard generic tokens when a better anchor exists.
    if not anchors:
        anchors = {t for t in subject_tokens if not t.isdigit() and len(t) >= 3}
    if not anchors or not (anchors & query_tokens):
        return "query does not carry a stable lexical anchor from the fact subject"
    return None


def gap_is_typed(row: dict) -> bool:
    gap_type = row.get("gap_type") or row.get("GAP_TYPE")
    gap_text = row.get("gap") or row.get("reason") or row.get("question")
    return (
        str(gap_type or "").strip().upper() not in {"", "-", "NONE", "NULL", "UNSPECIFIED"}
        and bool(str(gap_text or "").strip())
    )


def section_statuses(state: dict) -> dict:
    out = {}
    sections = state.get("sections", {})
    for name in CANONICAL_SECTIONS:
        value = sections.get(name, "NOT_INITIALIZED")
        if name in DERIVED_SECTIONS:
            out[name] = "DERIVED" if value == "RUNTIME_DERIVED" else "INVALID"
        elif value == "NOT_INITIALIZED":
            out[name] = "NOT_INITIALIZED"
        elif value in ([], {}):
            out[name] = "EMPTY"
        else:
            out[name] = "SET"
    return out


def archive_repair_outputs(state: dict) -> str | None:
    """Invalidate materialized FINAL outputs before a controlled repair."""
    candidates = []
    for key in ("investigation_path", "snapshot_path", "certification_path"):
        p = Path(state.get("run", {}).get(key, ""))
        if p.is_file():
            candidates.append(p)
    if not candidates:
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    backup = Path(state["run"]["run_dir"]) / "_repair_backups" / stamp
    backup.mkdir(parents=True, exist_ok=False)
    for src in candidates:
        os.replace(src, backup / src.name)
    return str(backup)


def reopen_for_repair(state: dict, reason: str) -> None:
    if state.get("run", {}).get("state") != "FINAL":
        return
    p = state.get("persistence", {})
    pending = (
        p.get("mnemo_row") == "PENDING_PRE_GATE"
        and p.get("writeback_row") == "PENDING_PRE_GATE"
        and not p.get("writeback_execution")
        and not p.get("attempt_history")
    )
    if not pending:
        die("controlled repair is allowed only before persistence; start an UPDATE run after writeback")
    backup = archive_repair_outputs(state)
    state["run"]["state"] = "OPEN"
    state["run"]["last_completed"] = "18a"
    state["run"]["next_action"] = f"REVALIDATE_AFTER_{reason}"
    state["sections"]["GATE_STATUS_V1"] = "NOT_INITIALIZED"
    state.get("stamps", {}).pop("FINAL_RENDERED", None)
    state.get("stamps", {}).pop("DELIVERY_PASS", None)
    if backup:
        state["run"]["repair_backup"] = backup


def cmd_paths(a):
    print(json.dumps(canonical_run_paths(a.truth_engine_root, a.as_of, a.run_id, a.subject_slug), ensure_ascii=False, indent=2))

def cmd_init(a):
    paths = canonical_run_paths(a.truth_engine_root, a.as_of, a.run_id, a.subject_slug)
    p = Path(a.state)
    if p.resolve() != Path(paths["state_path"]).resolve():
        die(f"state path must be canonical: {paths['state_path']}")
    if p.exists() and not a.force:
        die(f"state already exists: {p}; use --force only for deliberate replacement")
    replay_backup = archive_replayed_artifacts(paths) if a.force else None
    Path(paths["run_dir"]).mkdir(parents=True, exist_ok=True)
    sections = {k: ("RUNTIME_DERIVED" if k in DERIVED_SECTIONS else "NOT_INITIALIZED") for k in CANONICAL_SECTIONS}
    state = {
        "schema": SCHEMA,
        "engine": ENGINE,
        "run": {
            "run_id": a.run_id,
            "parent_run_id": a.parent_run_id,
            "as_of": a.as_of,
            "input_kind": a.input_kind,
            "mission_mode": a.mission_mode,
            "input_ref": a.input_ref,
            "original_input_ref": a.input_ref,
            "subject_slug": a.subject_slug,
            "subject_fingerprint": "PENDING",
            "subject_fingerprint_legacy_v1": "PENDING",
            "input_sha256": "PENDING",
            "input_path": "PENDING",
            "run_dir": paths["run_dir"],
            "state_path": paths["state_path"],
            "narrative_path": paths["narrative_path"],
            "snapshot_path": paths["snapshot_path"],
            "investigation_path": paths["investigation_path"],
            "certification_path": paths["certification_path"],
            "state": "OPEN",
            "checkpoint_seq": 0,
            "last_completed": "NONE",
            "next_action": a.next_action,
            "resume_count": 0,
            "complexity": a.complexity,
            "complexity_score": a.complexity_score,
            "scope": "PENDING",
            "route_overrides": [],
            "loaded_modules": [],
            "degraded_flags": [],
        },
        "counters": {k: 0 for k in ID_KINDS},
        "sections": sections,
        "requests": [],
        "sys_log": [],
        "sources": [],
        "facts": [],
        "leads": [], "claims": [], "axes": [], "causal": [], "controls": [], "actions": [],
        "refutations": [],
        "checkpoints": [],
        "delta_plan": [],
        "hydrated": None,
        "memory_probe": {"status":"PENDING","memory_id":"-","run_id":"-"},
        "stamps": {"START": now_iso()},
        "persistence": {
            "mnemo_row": "PENDING_PRE_GATE",
            "self_write_row": "PENDING_AT_SERIALIZATION",
            "writeback_row": "PENDING_PRE_GATE",
            "writeback_execution": [],
            "attempt_history": [],
        },
        "meta": {"created_at": now_iso(), "updated_at": now_iso()},
    }
    atomic_write(p, state)
    print(str(p) + (f" replay_backup={replay_backup}" if replay_backup else ""))


def cmd_archive_input(a):
    modes = [bool(a.source_file), a.text is not None, bool(a.stdin)]
    if sum(modes) != 1:
        die("provide exactly one of --source-file, --text, --stdin")
    if a.source_file:
        src=Path(a.source_file)
        if not src.is_file(): die(f"input source not readable: {src}")
        raw=src.read_bytes(); suffix=src.suffix or ".bin"
    elif a.text is not None:
        raw=a.text.encode("utf-8"); suffix=".txt"
    else:
        raw=sys.stdin.buffer.read(); suffix=".txt"
    fp, raw_sha, legacy_v1 = canonical_text_fingerprint(raw)
    def fn(st):
        r=st["run"]
        paths=canonical_run_paths(Path(r["run_dir"]).parents[2], r["as_of"], r["run_id"], r["subject_slug"], suffix)
        out=Path(paths["input_path"]); out.parent.mkdir(parents=True,exist_ok=True)
        fd,tmp=tempfile.mkstemp(prefix=out.name+".",suffix=".tmp",dir=str(out.parent))
        try:
            with os.fdopen(fd,"wb") as fh:
                fh.write(raw); fh.flush(); os.fsync(fh.fileno())
            os.replace(tmp,out)
        finally:
            if os.path.exists(tmp): os.unlink(tmp)
        r["input_path"]=str(out); r["input_sha256"]="sha256:"+raw_sha; r["subject_fingerprint"]=fp; r["subject_fingerprint_legacy_v1"]=legacy_v1; r["input_ref"]="PATH:"+str(out)
        if r.get("original_input_ref") in {None, "", "PENDING"}:
            if a.source_file:
                r["original_input_ref"]="PATH:"+str(Path(a.source_file).resolve())
            else:
                r["original_input_ref"]="INLINE_UNSTABLE"
    mutate(a.state, fn)
    st=load(a.state); print(f"{st['run']['input_path']} {st['run']['subject_fingerprint']}")

def cmd_memory_probe(a):
    status=a.status.upper()
    if status not in {"NONE","FOUND"}: die("status must be NONE or FOUND")
    def fn(st):
        if st["run"].get("subject_fingerprint") in {None,"","PENDING"}: die("archive input before memory probe")
        if status=="FOUND" and not a.memory_id: die("FOUND requires --memory-id")
        st["memory_probe"]={"status":status,"memory_id":a.memory_id or "-","run_id":a.run_id or "-"}
        sid = next_id(st, "SYS")
        st["sys_log"].append({"id":sid,"mode":"SYS","result":status,"tool":"runtime","ref":a.memory_id or "-","call":"MEMORY_PROBE"})
    mutate(a.state, fn); print(status)

def cmd_alloc(a):
    out = {}
    def fn(s):
        out["id"] = next_id(s, a.kind)
    mutate(a.state, fn)
    print(out["id"])


def cmd_set_run(a):
    payload = read_json_input(a)
    if not isinstance(payload, dict):
        die("set-run payload must be an object")
    allowed = {"parent_run_id","complexity","complexity_score","scope","resume_count","route_overrides","loaded_modules","degraded_flags"}
    unknown = set(payload) - allowed
    if unknown:
        die("immutable/unknown run fields: " + ",".join(sorted(unknown)))
    if "route_overrides" in payload and not isinstance(payload["route_overrides"], list): die("route_overrides must be list")
    if "loaded_modules" in payload and not isinstance(payload["loaded_modules"], list): die("loaded_modules must be list")
    if "degraded_flags" in payload and not isinstance(payload["degraded_flags"], list): die("degraded_flags must be list")
    if "resume_count" in payload and (not isinstance(payload["resume_count"], int) or payload["resume_count"] < 0): die("resume_count must be non-negative int")
    def fn(s):
        s["run"].update(payload)
    mutate(a.state, fn)
    print("RUN")


def cmd_set_section(a):
    value = read_json_input(a)
    if a.name not in CANONICAL_SECTIONS:
        die(f"unknown canonical section: {a.name}")
    if a.name in DERIVED_SECTIONS:
        die(f"section {a.name} is runtime-derived and cannot be set manually")
    def fn(s):
        s["sections"][a.name] = value
    mutate(a.state, fn)
    print(a.name)


def cmd_append_section(a):
    value = read_json_input(a)
    if a.name not in CANONICAL_SECTIONS:
        die(f"unknown canonical section: {a.name}")
    if a.name in DERIVED_SECTIONS:
        die(f"section {a.name} is runtime-derived and cannot be appended manually")
    def fn(s):
        cur = s["sections"].get(a.name, "NOT_INITIALIZED")
        if cur == "NOT_INITIALIZED":
            cur = []
        if not isinstance(cur, list):
            die(f"section {a.name} is not a list")
        cur.append(value)
        s["sections"][a.name] = cur
    mutate(a.state, fn)
    print(a.name)


def cmd_record_sys(a):
    machine_field("result", a.result); machine_field("call", a.call)
    if a.tool: machine_field("tool", a.tool)
    if a.ref: machine_field("ref", a.ref)
    out = {}
    def fn(s):
        sid = next_id(s, "SYS")
        row = {"id": sid, "mode": "SYS", "result": a.result, "tool": a.tool or "-", "ref": a.ref or "-", "call": a.call}
        s["sys_log"].append(row)
        out.update(row)
    mutate(a.state, fn)
    print(out["id"])


def cmd_record_query(a):
    mode = a.mode.upper()
    if mode not in QRY_MODES:
        die(f"mode must be one of {sorted(QRY_MODES)}")
    machine_field("result", a.result)
    if a.url: machine_field("url", a.url)
    if a.query: machine_field("query", a.query)
    if a.accept_source:
        if not a.url or not a.role or not a.family:
            die("--accept-source requires --url --role --family")
        if a.role not in SOURCE_ROLES:
            die("invalid source role")
        validate_family_token(a.family)
    out = {}
    def fn(s):
        src_id = "-"
        if a.accept_source:
            src_id = next_id(s, "SRC")
            src = {"id": src_id, "role": a.role, "family": a.family, "url": a.url, "title": a.title or ""}
            s["sources"].append(src)
        qid = next_id(s, "QRY")
        row = {"id": qid, "mode": mode, "result": a.result, "source": src_id, "url": a.url or "-", "query": a.query or "-"}
        s["requests"].append(row)
        out["qid"], out["sid"] = qid, src_id
    mutate(a.state, fn)
    print(out["qid"] + (f" {out['sid']}" if out["sid"] != "-" else ""))


def cmd_record_source(a):
    if a.role not in SOURCE_ROLES:
        die("invalid source role")
    validate_family_token(a.family); machine_field("url", a.url)
    out = {}
    def fn(s):
        sid = next_id(s, "SRC")
        row = {"id": sid, "role": a.role, "family": a.family, "url": a.url, "title": a.title or ""}
        s["sources"].append(row)
        out.update(row)
    mutate(a.state, fn)
    print(out["id"])

def cmd_link_query_source(a):
    """Repair one truthful FETCH→SRC linkage through the runtime, never by editing RUN_STATE directly."""
    def fn(s):
        q = next((x for x in s.get("requests", []) if x.get("id") == a.qry), None)
        src = source_by_id(s, a.src)
        if not q:
            die(f"unknown query: {a.qry}")
        if not src:
            die(f"unknown source: {a.src}")
        if q.get("mode") != "FETCH":
            die("link-query-source requires QRY mode FETCH")
        if q.get("result") != "FOUND":
            die("link-query-source requires successful FETCH result FOUND")
        if q.get("source") not in {None, "", "-"}:
            die(f"query already linked to {q.get('source')}")
        if q.get("url") != src.get("url"):
            die("link-query-source requires exact QRY.url == SRC.url")
        q["source"] = src["id"]
    mutate(a.state, fn)
    print(f"{a.qry} -> {a.src}")


def cmd_record_fact(a):
    if a.epi not in VALID_EPI:
        die(f"invalid EPI: {a.epi}")
    if a.tier not in VALID_TIER:
        die(f"invalid tier: {a.tier}")
    src_ids = [x.strip() for x in a.sources.split(",") if x.strip() and x.strip() != "-"]
    for name, value in (("url",a.url),("date",a.date),("subject",a.subject),("value",a.value)):
        machine_field(name, value)
    out = {}
    def fn(s):
        rows = []
        for sid in src_ids:
            src = source_by_id(s, sid)
            if not src:
                die(f"unknown source: {sid}")
            rows.append(src)
        families = sorted({x["family"] for x in rows if x.get("family")})
        urls = {x["url"] for x in rows if x.get("url")}
        if a.tier in {"✦", "✧"} and not rows:
            die(f"tier {a.tier} requires mapped source(s)")
        if a.tier == "✦" and len(families) < 2:
            die("tier ✦ requires at least 2 derived source families")
        if a.url.startswith(("http://", "https://")) and a.tier in {"✦", "✧"} and a.url not in urls:
            die("canonical fact URL must be one of mapped support source URLs")
        fid = next_id(s, "FCT")
        bad = trivial_url_inconsistency(a.url, a.subject, a.value)
        if bad:
            die(bad)
        hf = hydrated_fact_by_key(s, a.subject) or {}
        drow = delta_by_key(s, a.subject) or {}
        origin_memory_id = a.origin_memory_id or hf.get("memory_id") or drow.get("memory_id") or "-"
        origin_run_id = a.origin_run_id or hf.get("origin_run_id") or (s.get("hydrated") or {}).get("run_id") or "-"
        origin_verified_at = a.origin_verified_at or hf.get("verified_at") or drow.get("prior_verified_at") or "-"
        snapshot_memory_id = (s.get("memory_probe") or {}).get("memory_id")
        if origin_memory_id not in {None, "", "-"} and origin_memory_id == snapshot_memory_id:
            die("origin_memory_id must identify the prior fact, not the enclosing snapshot memory")
        row = {
            "id": fid, "epi": a.epi, "tier": a.tier, "url": a.url,
            "families": families, "date": a.date, "subject": a.subject,
            "value": a.value, "mem": a.mem, "sources": src_ids,
            "origin_memory_id": origin_memory_id,
            "origin_run_id": origin_run_id,
            "origin_verified_at": origin_verified_at,
        }
        s["facts"].append(row)
        out.update(row)
    mutate(a.state, fn)
    print(out["id"])


def cmd_record_refutation(a):
    if a.status not in {"NONE", "FOUND_RESOLVED"}:
        die("status must be NONE or FOUND_RESOLVED")
    def fn(s):
        fact = fact_by_id(s, a.fct)
        if not fact:
            die(f"unknown fact: {a.fct}")
        query = query_by_id(s, a.qry)
        if not query:
            die(f"unknown query: {a.qry}")
        alignment = refutation_alignment_error(fact, query)
        if alignment:
            die(f"semantic refutation mismatch {a.fct}->{a.qry}: {alignment}")
        s["refutations"] = [x for x in s["refutations"] if x["fct"] != a.fct]
        s["refutations"].append({"fct": a.fct, "qry": a.qry, "status": a.status})
    mutate(a.state, fn)
    print(a.fct)


def cmd_record_object(a):
    kind=a.kind.upper()
    if kind not in OBJECT_KINDS:
        die(f"kind must be one of {OBJECT_KINDS}")
    payload=read_json_input(a)
    rows = payload if isinstance(payload, list) else [payload]
    if not rows or any(not isinstance(x, dict) for x in rows):
        die("object payload must be a JSON object or non-empty array of objects")
    if any("id" in x for x in rows):
        die("semantic object id is runtime-owned; payload must not contain id")
    ids=[]
    def fn(s):
        for item in rows:
            oid=next_id(s, kind)
            row={"id":oid, **item}
            s[OBJECT_BUCKETS[kind]].append(row)
            ids.append(oid)
    mutate(a.state, fn)
    print(f"{kind} count={len(ids)} ids={','.join(ids)}")

def cmd_update_object(a):
    payload=read_json_input(a)
    if not isinstance(payload, dict):
        die("update payload must be JSON object")
    if "id" in payload:
        die("object id is immutable")
    def fn(s):
        kind,row=object_by_id(s,a.id)
        if not row:
            die(f"unknown semantic object: {a.id}")
        row.update(payload)
    mutate(a.state, fn)
    print(a.id)


def cmd_update_fact(a):
    payload = read_json_input(a)
    if not isinstance(payload, dict) or not payload:
        die("update-fact payload must be a non-empty JSON object")
    allowed = {
        "epi", "tier", "url", "sources", "date", "subject", "value",
        "origin_memory_id", "origin_run_id", "origin_verified_at",
    }
    unknown = set(payload) - allowed
    if unknown:
        die("update-fact immutable/unknown field(s): " + ",".join(sorted(unknown)))
    if "epi" in payload and payload["epi"] not in VALID_EPI: die("invalid EPI")
    if "tier" in payload and payload["tier"] not in VALID_TIER: die("invalid tier")
    if "sources" in payload and (not isinstance(payload["sources"], list) or any(not isinstance(x, str) for x in payload["sources"])):
        die("sources must be a JSON array of SRC IDs")
    for key in ("url", "date", "subject", "value", "origin_memory_id", "origin_run_id", "origin_verified_at"):
        if key in payload:
            if not isinstance(payload[key], str): die(f"{key} must be a string")
            machine_field(key, payload[key], allow_empty=key.startswith("origin_"))
    def fn(s):
        fact = fact_by_id(s, a.id)
        if not fact:
            die(f"unknown fact: {a.id}")
        candidate = {**fact, **payload}
        rows = []
        for sid in candidate.get("sources", []):
            src = source_by_id(s, sid)
            if not src: die(f"unknown source: {sid}")
            rows.append(src)
        families = sorted({x["family"] for x in rows if x.get("family")})
        if candidate["tier"] in {"✦", "✧"} and not rows:
            die(f"tier {candidate['tier']} requires mapped source(s)")
        if candidate["tier"] == "✦" and len(families) < 2:
            die("tier ✦ requires at least 2 derived source families")
        urls = {x.get("url") for x in rows}
        if candidate["url"].startswith(("http://", "https://")) and candidate["tier"] in {"✦", "✧"} and candidate["url"] not in urls:
            die("canonical fact URL must be one of mapped support source URLs")
        bad = trivial_url_inconsistency(candidate["url"], candidate["subject"], candidate["value"])
        if bad: die(bad)
        snapshot_memory_id = (s.get("memory_probe") or {}).get("memory_id")
        origin = candidate.get("origin_memory_id")
        if origin not in {None, "", "-"} and origin == snapshot_memory_id:
            die("origin_memory_id must identify the prior fact, not the enclosing snapshot memory")
        reopen_for_repair(s, "FACT_REPAIR")
        fact.update(payload)
        fact["families"] = families
        sid = next_id(s, "SYS")
        s["sys_log"].append({"id":sid,"mode":"SYS","result":"PASS","tool":"runtime","ref":a.id,"call":"REPAIR_FACT"})
    mutate(a.state, fn)
    print(a.id)


def cmd_update_sys(a):
    payload = read_json_input(a)
    if not isinstance(payload, dict) or not payload:
        die("update-sys payload must be a non-empty JSON object")
    allowed = {"result", "tool", "ref", "call"}
    unknown = set(payload) - allowed
    if unknown:
        die("update-sys immutable/unknown field(s): " + ",".join(sorted(unknown)))
    for key, value in payload.items():
        if not isinstance(value, str): die(f"{key} must be a string")
        machine_field(key, value)
    def fn(s):
        row = next((x for x in s.get("sys_log", []) if x.get("id") == a.id), None)
        if not row: die(f"unknown SYS row: {a.id}")
        if row.get("call") in {"MEMORY_PROBE", "HYDRATE", "PERSIST_REBIND"}:
            die(f"runtime-owned {row.get('call')} row cannot be repaired")
        reopen_for_repair(s, "SYS_REPAIR")
        row.update(payload)
        sid = next_id(s, "SYS")
        s["sys_log"].append({"id":sid,"mode":"SYS","result":"PASS","tool":"runtime","ref":a.id,"call":"REPAIR_SYS"})
    mutate(a.state, fn)
    print(a.id)

def cmd_assert_counts(a):
    expected=parse_json_value(a.json)
    if not isinstance(expected, dict):
        die("--json must be an object of semantic counts")
    bad=[]
    s=load(a.state)
    for kind,want in expected.items():
        k=kind.upper()
        if k not in OBJECT_KINDS or not isinstance(want,int) or want < 0:
            die(f"invalid semantic count expectation: {kind}={want}")
        got=len(s.get(OBJECT_BUCKETS[k],[]))
        if got != want:
            bad.append(f"{k}:{got}!={want}")
    if bad:
        die("semantic count postcondition failed: "+", ".join(bad),1)
    print("PASS "+" ".join(f"{k.upper()}={v}" for k,v in expected.items()))

def cmd_delta(a):
    klass = a.class_.upper()
    if klass not in DELTA_CLASSES:
        die(f"delta class must be one of {sorted(DELTA_CLASSES)}")
    def fn(s):
        if s.get("hydrated") and klass == "REUSE":
            if a.key in set((s["hydrated"] or {}).get("conflict_keys", [])):
                die("REUSE forbidden for contradictory hydrated memories; use RECHECK")
            if a.url and not url_specific_enough(a.url):
                die("REUSE requires a specific canonical URL; use RECHECK")
            bad=trivial_url_inconsistency(a.url or "", a.key, a.reason)
            if bad:
                die("REUSE rejected: "+bad+"; use RECHECK")
        hf = hydrated_fact_by_key(s, a.key) or {}
        row = {"key": a.key, "class": klass, "reason": a.reason,
               "memory_id": a.memory_id or hf.get("memory_id") or "-",
               "url": a.url or hf.get("url") or "-",
               "prior_verified_at": a.prior_verified_at or hf.get("verified_at") or "-"}
        s["delta_plan"] = [x for x in s["delta_plan"] if x["key"] != a.key]
        s["delta_plan"].append(row)
    mutate(a.state, fn)
    print(a.key)


def cmd_hydrate(a):
    sp = Path(a.snapshot)
    if sp.stat().st_size > 65536:
        die("snapshot exceeds 64 KiB routing-state bound")
    try:
        snap = json.loads(sp.read_text(encoding="utf-8"))
    except Exception as e:
        die(f"cannot read snapshot: {e}")
    if snap.get("snapshot_schema") != 1:
        die("unsupported snapshot schema")
    def fn(s):
        current_fp=s["run"].get("subject_fingerprint")
        legacy_v1=s["run"].get("subject_fingerprint_legacy_v1")
        snap_fp=snap.get("subject_fingerprint")
        if current_fp in {None,"","PENDING"}: die("archive input before hydrate")
        if not snap_fp: die("snapshot lacks subject_fingerprint; legacy snapshot is warm-route only, not exact HYDRATE")
        exact_v2 = snap_fp == current_fp
        compatible_2104_v1 = snap.get("engine") == "2.10.4" and legacy_v1 not in {None,"","PENDING"} and snap_fp == legacy_v1
        if not (exact_v2 or compatible_2104_v1): die("snapshot subject_fingerprint does not match current input")
        snap["fingerprint_match"] = "V2" if exact_v2 else "LEGACY_V1_2.10.4"
        vals = {}
        conflicts = []
        for f in snap.get("facts", []):
            key=f.get("key")
            val=f.get("value")
            if key in vals and vals[key] != val:
                conflicts.append(key)
            vals[key]=val
        snap["conflict_keys"] = sorted(set(conflicts))
        s["hydrated"] = snap
        s["memory_probe"]={"status":"FOUND","memory_id":a.memory_id or "-","run_id":snap.get("run_id","-")}
        s["stamps"]["HYDRATED"] = now_iso()
        sid = next_id(s, "SYS")
        s["sys_log"].append({"id":sid,"mode":"SYS","result":"FOUND","tool":"runtime","ref":a.memory_id or "-","call":"HYDRATE"})
    mutate(a.state, fn)
    print(f"HYDRATED:{snap.get('run_id','UNKNOWN')} facts={len(snap.get('facts',[]))}")


def cmd_stamp(a):
    allowed = {"START","HYDRATED","RESEARCH_DONE","FINAL_RENDERED","DELIVERY_PASS"}
    if a.name not in allowed:
        die(f"stamp must be one of {sorted(allowed)}")
    def fn(s):
        if a.name == "START" and "START" in s["stamps"]:
            die("START already set by init")
        s["stamps"][a.name] = now_iso()
    mutate(a.state, fn)
    print(a.name)


def checkpoint_rank(label: str):
    base = label.split(":", 1)[0]
    return CHECKPOINT_RANK.get(base)


def _terminal(row):
    return str(row.get("status","")).upper() in {"PASS","DONE","SATURATED","GAP","CLOSED","RESOLVED","TERMINAL"}

def semantic_terminal(kind: str, row: dict) -> bool:
    st=str(row.get("status","")).strip().upper()
    if kind=="LED": return st in {"SATURATED","EXCLUDED"} or (st=="GAP" and gap_is_typed(row))
    if kind=="AXS": return st in {"SATURATED","N/A","NA"} or (st=="GAP" and gap_is_typed(row))
    if kind=="CLM": return st in {"SATURATED","PARTIAL","SUPPORTED","REFUTED","CONTRADICTED"} or (st=="GAP" and gap_is_typed(row))
    if kind=="CAU":
        if st in {"SUPPORTED","SATURATED","REFUTED"}: return True
        if st in {"GAP","UNKNOWN","UNRESOLVED"} and gap_is_typed(row): return True
        return False
    return _terminal(row)

def checkpoint_preconditions(s: dict, label: str) -> list[str]:
    base=label.split(":",1)[0]
    e=[]
    r=s["run"]
    if base == "LEADS" and (r.get("input_kind") == "DOCUMENT" or r.get("complexity") in {"COMPLEX","APEX"}) and not s.get("leads"):
        e.append("LEADS checkpoint requires runtime-owned LED objects")
    if base in {"SCOPE","SEARCH","SEARCH_PARTIAL","FACTS","CAUSAL","CAUSAL_GAP","VERIFY","INVESTIGATION_ACCOUNTABILITY"}:
        if str(r.get("complexity","PENDING"))=="PENDING" or str(r.get("complexity_score","PENDING"))=="PENDING": e.append("complexity still PENDING")
    if base == "SCOPE" and not s.get("axes"):
        e.append("SCOPE checkpoint requires runtime-owned AXS objects")
    if base in {"SEARCH","SEARCH_PARTIAL","FACTS","CAUSAL","CAUSAL_GAP","VERIFY","INVESTIGATION_ACCOUNTABILITY"} and r.get("scope")=="PENDING": e.append("scope still PENDING")
    if base in {"FACTS","CAUSAL","CAUSAL_GAP","VERIFY","INVESTIGATION_ACCOUNTABILITY"}:
        if not any(checkpoint_rank(x["label"])==9 for x in s["checkpoints"]): e.append("SEARCH checkpoint missing")
        if any(not semantic_terminal("LED",x) for x in s.get("leads",[])): e.append("non-terminal LED objects remain")
    if base in {"CAUSAL","CAUSAL_GAP"} and not s.get("causal"):
        e.append("CAUSAL checkpoint requires runtime-owned CAU object(s)")
    if base in {"VERIFY","INVESTIGATION_ACCOUNTABILITY"}:
        if not any(checkpoint_rank(x["label"])==10 for x in s["checkpoints"]): e.append("FACTS checkpoint missing")
        if not any(checkpoint_rank(x["label"])==11 for x in s["checkpoints"]): e.append("CAUSAL/CAUSAL_GAP checkpoint missing")
    if base=="INVESTIGATION_ACCOUNTABILITY":
        if any(not semantic_terminal("AXS",x) for x in s.get("axes",[])): e.append("non-terminal AXS objects remain")
    return e

def cmd_checkpoint(a):
    out = {}
    def fn(s):
        rank = checkpoint_rank(a.label)
        if rank is None:
            die(f"unknown checkpoint label: {a.label}")
        prereq = checkpoint_preconditions(s, a.label)
        if prereq:
            die("checkpoint preconditions failed: " + "; ".join(prereq))
        if s["checkpoints"]:
            prev = checkpoint_rank(s["checkpoints"][-1]["label"])
            if prev is not None and rank < prev:
                die(f"retroactive checkpoint order: {a.label} after {s['checkpoints'][-1]['label']}")
        lm = re.match(r"\s*(\d+)", a.last_completed)
        if lm and rank != 18 and int(lm.group(1)) != rank:
            die(f"LAST_COMPLETED {a.last_completed} does not match checkpoint phase {rank}")
        cp = next_id(s, "CP")
        seq = int(cp.split("-")[1])
        row = {"id": cp, "seq": seq, "label": a.label, "status": "PASS", "last_completed": a.last_completed, "next_action": a.next_action, "created_at": now_iso()}
        s["checkpoints"].append(row)
        s["run"]["checkpoint_seq"] = seq
        s["run"]["last_completed"] = a.last_completed
        s["run"]["next_action"] = a.next_action
        if rank == 10 and "RESEARCH_DONE" not in s["stamps"]:
            s["stamps"]["RESEARCH_DONE"] = now_iso()
        out.update(row)
    mutate(a.state, fn)
    print(out["id"])


def cmd_set_gates(a):
    value = parse_json_value(a.json)
    expected = {f"G{i}" for i in range(11)}
    if not isinstance(value, dict) or set(value) != expected:
        die("gate JSON must contain exactly G0..G10")
    if any(v not in {"PASS", "FAIL", "BLOCKED", "PENDING", "UNEXECUTED"} for v in value.values()):
        die("invalid gate status")
    def fn(s):
        s["sections"]["GATE_STATUS_V1"] = value
    mutate(a.state, fn)
    print("GATES")


def cmd_mark_final(a):
    def fn(s):
        if s["run"].get("mission_mode") == "INVESTIGATION" and "MEMOIRE_SEULE_NO_REFETCH" in s["run"].get("degraded_flags", []):
            die("memory-only/no-refetch run cannot be certified as INVESTIGATION FINAL; render a memory reconstruction outside certified investigation mode")
        if s.get("hydrated") is not None and not s.get("delta_plan"):
            die("hydrated run requires non-empty DELTA_PLAN before finalization")
        required_semantic=[]
        r=s["run"]
        if r.get("input_kind") == "DOCUMENT" or r.get("complexity") in {"COMPLEX","APEX"}: required_semantic.append("LED")
        if r.get("mission_mode") == "INVESTIGATION": required_semantic.extend(["AXS","CLM"])
        if any(checkpoint_rank(x.get("label","")) == 11 for x in s.get("checkpoints",[])): required_semantic.append("CAU")
        empty=[k for k in dict.fromkeys(required_semantic) if not s.get(OBJECT_BUCKETS[k],[])]
        if empty:
            die("mark-final requires runtime-owned semantic registries: "+",".join(empty))
        nonterminal=[]
        for k in ("LED","AXS","CLM","CAU"):
            for row in s.get(OBJECT_BUCKETS[k],[]):
                if not semantic_terminal(k,row): nonterminal.append(row.get("id",k))
        if nonterminal:
            die("mark-final blocked by non-terminal semantic objects: "+",".join(nonterminal))
        incomplete = [name for name in REQUIRED_REPORT_SECTIONS if s.get("sections", {}).get(name) == "NOT_INITIALIZED"]
        if incomplete:
            die("mark-final requires every report section set to content or []: " + ",".join(incomplete))
        structural = state_errors(s, None)
        if structural:
            die("mark-final blocked by state integrity: " + "; ".join(structural))
        gates = s["sections"].get("GATE_STATUS_V1")
        if not isinstance(gates, dict) or any(gates.get(f"G{i}") != "PASS" for i in range(11)):
            die("mark-final requires explicit G0..G10=PASS already stored; helper never invents gate results")
        s["run"]["state"] = "FINAL"
        s["run"]["last_completed"] = "18b"
        s["run"]["next_action"] = "NONE"
    mutate(a.state, fn)
    print("FINAL")


def persistence_attempt_snapshot(s: dict, result: str, created_at: str) -> dict:
    p = s["persistence"]
    return {
        "seq": len(p.get("attempt_history", [])) + 1,
        "created_at": created_at,
        "result": result,
        "mnemo_row": copy.deepcopy(p.get("mnemo_row")),
        "writeback_row": copy.deepcopy(p.get("writeback_row")),
        "writeback_execution": copy.deepcopy(p.get("writeback_execution", [])),
        "fact_mem": {
            f["id"]: f.get("mem", "-") for f in s.get("facts", [])
            if f.get("mem", "-") not in {None, "", "-"}
        },
    }


def persistence_attempt_result(s: dict) -> str:
    p = s["persistence"]
    wr = p.get("writeback_row")
    rows = p.get("writeback_execution") or []
    eligible = {f["id"]: f for f in s.get("facts", []) if eligible_fact(f)}
    if isinstance(wr, dict) and int(wr.get("failure", 0)) > 0:
        return "FAIL"
    if any(int(row.get("failure", 0)) > 0 for row in rows if isinstance(row, dict)):
        return "FAIL"
    if p.get("mnemo_row") in {None, "", "PENDING_PRE_GATE"}:
        return "PARTIAL"
    keys = {"eligible", "attempted", "success", "failure", "blocked"}
    if not isinstance(wr, dict) or set(wr) != keys:
        return "PARTIAL"
    by_fct = {row.get("fct"): row for row in rows if isinstance(row, dict)}
    if set(by_fct) != set(eligible):
        return "PARTIAL"
    attempted = success = failure = blocked = 0
    for fid, fact in eligible.items():
        row = by_fct[fid]
        a, ok, fail, block = (int(row.get(k, 0)) for k in ("attempted", "success", "failure", "blocked"))
        if a + block != 1 or a != ok + fail:
            return "PARTIAL"
        if ok != 1 or fact.get("mem") in {None, "", "-"}:
            return "PARTIAL"
        attempted += a; success += ok; failure += fail; blocked += block
    observed = {
        "eligible": len(eligible), "attempted": attempted, "success": success,
        "failure": failure, "blocked": blocked,
    }
    return "PASS" if wr == observed else "PARTIAL"


def cmd_set_persistence(a):
    payload = read_json_input(a)
    if not isinstance(payload, dict):
        die("set-persistence payload must be a JSON object")
    allowed={"mnemo_row","self_write_row","writeback_row","writeback_execution","fact_mem"}
    unknown=set(payload)-allowed
    if unknown:
        die("set-persistence unknown field(s): " + ",".join(sorted(unknown)))
    if "self_write_row" in payload and payload["self_write_row"] != "PENDING_AT_SERIALIZATION":
        die("self_write_row is fixed to PENDING_AT_SERIALIZATION")
    if "mnemo_row" in payload and not isinstance(payload["mnemo_row"], str):
        die("mnemo_row must be a string")
    if "writeback_row" in payload and payload["writeback_row"] != "PENDING_PRE_GATE":
        wr=payload["writeback_row"]
        required={"eligible","attempted","success","failure","blocked"}
        if not isinstance(wr,dict) or set(wr) != required or any(not isinstance(wr[k],int) or isinstance(wr[k],bool) or wr[k] < 0 for k in required):
            die("writeback_row must be structured object {eligible,attempted,success,failure,blocked}")
    if "writeback_execution" in payload:
        rows=payload["writeback_execution"]
        if not isinstance(rows,list):
            die("writeback_execution must be a list")
        required={"fct","action","attempted","success","failure","blocked","reason"}
        for i,row in enumerate(rows):
            if not isinstance(row,dict) or set(row)!=required:
                die(f"writeback_execution[{i}] must contain exactly {sorted(required)}")
            if not isinstance(row["fct"],str) or not row["fct"].startswith("FCT-"):
                die(f"writeback_execution[{i}].fct invalid")
            if not isinstance(row["action"],str) or not isinstance(row["reason"],str):
                die(f"writeback_execution[{i}] action/reason must be strings")
            for k in ("attempted","success","failure","blocked"):
                if not isinstance(row[k],int) or isinstance(row[k],bool) or row[k] < 0:
                    die(f"writeback_execution[{i}].{k} must be non-negative int")
    if "fact_mem" in payload and not isinstance(payload["fact_mem"],dict):
        die("fact_mem must be an object mapping FCT-ID to memory id")
    def fn(s):
        if s.get("run", {}).get("state") != "FINAL":
            die("set-persistence requires a PRE-verified FINAL state")
        p = s["persistence"]
        p.setdefault("attempt_history", [])
        for key in ("mnemo_row", "self_write_row", "writeback_row", "writeback_execution"):
            if key in payload:
                p[key] = payload[key]
        mem_map = payload.get("fact_mem", {})
        for fid, mem in mem_map.items():
            if not isinstance(fid,str) or not isinstance(mem,str) or mem in {"","-"}:
                die("fact_mem entries require FCT-ID -> non-empty memory id")
            f = fact_by_id(s, fid)
            if not f:
                die(f"unknown fact in fact_mem: {fid}")
            if not eligible_fact(f):
                die(f"fact_mem cannot bind ineligible fact: {fid}")
            f["mem"] = mem
        result = persistence_attempt_result(s)
        created_at = now_iso()
        attempt = persistence_attempt_snapshot(s, result, created_at)
        p["attempt_history"].append(attempt)
        sid = next_id(s, "SYS")
        s["sys_log"].append({"id":sid,"mode":"SYS","result":result,"tool":"runtime","ref":f"ATTEMPT-{attempt['seq']:03d}","call":"PERSIST_REBIND"})
    mutate(a.state, fn)
    print("PERSISTENCE")

def writeback_action(f):
    if f["epi"] == "FACT" and f["tier"] == "✦":
        return "ELIGIBLE:CONFIRME"
    if f["epi"] == "FACT" and f["tier"] == "✧":
        return "ELIGIBLE:VERIFIE"
    return "SKIP:NOT_ELIGIBLE"


def activity(state):
    out = {"WEB": 0, "FETCH": 0, "EXA": 0}
    for q in state["requests"]:
        if q["mode"] in out:
            out[q["mode"]] += 1
    return out


def format_writeback_row(value) -> str:
    if value == "PENDING_PRE_GATE":
        return value
    if not isinstance(value, dict):
        die("writeback_row must remain structured in RUN_STATE")
    return "{" + ";".join(f"{k}:{int(value[k])}" for k in ("eligible","attempted","success","failure","blocked")) + "}"


def eligible_fact(f: dict) -> bool:
    return f.get("epi") == "FACT" and f.get("tier") in {"✦", "✧"}

def snapshot_alignment_errors(s: dict) -> list[str]:
    path = Path(s.get("run", {}).get("snapshot_path", ""))
    if not path.is_file():
        return ["delivery snapshot missing"]
    try:
        snap = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"delivery snapshot unreadable: {e}"]
    if snap.get("snapshot_schema") != 1:
        return ["delivery snapshot schema invalid"]
    if snap.get("subject_fingerprint") != s.get("run", {}).get("subject_fingerprint"):
        return ["delivery snapshot subject_fingerprint mismatch"]
    rows = snap.get("facts")
    if not isinstance(rows, list):
        return ["delivery snapshot facts missing"]
    by_key = {x.get("key"): x for x in rows if isinstance(x, dict) and x.get("key")}
    errors = []
    for f in s.get("facts", []):
        row = by_key.get(f.get("subject"))
        if row is None:
            errors.append(f"delivery snapshot missing fact key {f.get('subject')}")
            continue
        expected = f.get("mem", "-")
        observed = row.get("memory_id", "-")
        if eligible_fact(f) and expected in {None, "", "-"}:
            errors.append(f"{f.get('id')} eligible fact missing memory id before delivery")
        if observed != expected:
            errors.append(f"delivery snapshot memory_id mismatch for {f.get('id')}: {observed} != {expected}")
    extra = sorted(set(by_key) - {f.get("subject") for f in s.get("facts", [])})
    if extra:
        errors.append("delivery snapshot contains unknown fact key(s): " + ",".join(extra))
    return errors

def memory_write_mode(f: dict) -> tuple[str,str]:
    mid=f.get("origin_memory_id") or "-"
    return ("UPDATE", mid) if mid not in {"-","",None} else ("WRITE", "-")


def semantic_counts(state: dict) -> dict:
    return {k: len(state.get(OBJECT_BUCKETS[k],[])) for k in OBJECT_KINDS}


def semantic_blocks(state: dict) -> str:
    c=semantic_counts(state)
    lines=["SEMANTIC_COUNTS_V1:"+"|".join(f"{k}:{c[k]}" for k in OBJECT_KINDS), "", "## SEMANTIC_REGISTRIES_V1"]
    titles={"LED":"LEAD_REGISTRY_V1","CLM":"CLAIM_REGISTRY_V1","AXS":"AXIS_REGISTRY_V1","CAU":"CAUSALITY_REGISTRY_V1","CTRL":"CONTROL_REGISTRY_V1","ACT":"ACTION_REGISTRY_V1"}
    for kind in OBJECT_KINDS:
        lines += ["", f"### {titles[kind]}"]
        for row in state.get(OBJECT_BUCKETS[kind],[]):
            payload={k:v for k,v in row.items() if k != "id"}
            lines.append(f"{row['id']} | "+json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":")))
    return "\n".join(lines).rstrip()+"\n"


def machine_blocks(state: dict, phase: str) -> str:
    lines = []
    a = activity(state)
    lines.append(f"SEARCH_ACTIVITY_V1:WEB:{a['WEB']}|FETCH:{a['FETCH']}|EXA:{a['EXA']}")
    lines.append("SECTION_STATUS_V1:" + json.dumps(section_statuses(state), ensure_ascii=False, sort_keys=True, separators=(",",":")))
    lines += ["", "## REQUEST_LOG"]
    for x in state["sys_log"]:
        lines.append(f"{x['id']} | SYS | {x['result']} | {x['tool']} | {x['ref']} | {x['call']}")
    for q in state["requests"]:
        lines.append(f"{q['id']} | {q['mode']} | {q['result']} | {q['source']} | {q['url']} | {q.get('query','-')}")
    lines += ["", "## EVIDENCE_REGISTRY"]
    for s in state["sources"]:
        lines.append(f"{s['id']} | {s['role']} | fam:{s['family']} | {s['url']}")
    lines += ["", "<!-- FACT_REGISTRY_V1 -->"]
    for f in state["facts"]:
        fam = ",".join(f["families"]) if f["families"] else "-"
        mem = f["mem"] if phase == "delivery" else "-"
        lines.append(f"{f['id']} | {f['epi']} | {f['tier']} | {f['url']} | {fam} | {f['date']} | {f['subject']} | {f['value']} | {mem}")
    lines.append("<!-- /FACT_REGISTRY_V1 -->")
    lines += ["", "## FCT_SOURCE_MAP_V1"]
    for f in state["facts"]:
        lines.append(f"{f['id']} | {','.join(f['sources']) if f['sources'] else '-'}")
    lines += ["", "## REFUTATION_REGISTRY_V1"]
    ref = {x["fct"]: x for x in state["refutations"]}
    for f in state["facts"]:
        if f["id"] in ref:
            r = ref[f["id"]]
            lines.append(f"{f['id']} | {r['qry']} | {r['status']}")
    lines += ["", "## WRITEBACK_PLAN_V1"]
    for f in state["facts"]:
        lines.append(f"{f['id']} | {writeback_action(f)}")
    lines += ["", "## MEMORY_WRITE_MODE_V1"]
    for f in state["facts"]:
        if writeback_action(f).startswith("ELIGIBLE:"):
            mode,mid=memory_write_mode(f)
            lines.append(f"{f['id']} | {mode} | {mid}")
    lines += ["", "## CHECKPOINT_LOG_V1"]
    for cp in state["checkpoints"]:
        lines.append(f"{cp['id']} | {cp['label']} | PASS | LAST_COMPLETED:{cp['last_completed']} | NEXT_ACTION:{cp['next_action']}")

    p = state["persistence"]
    lines += ["", "## WRITEBACK_ATTEMPT_LOG_V1"]
    if phase == "delivery":
        for attempt in p.get("attempt_history", []):
            payload = {k:v for k,v in attempt.items() if k != "seq"}
            lines.append(f"ATTEMPT-{attempt['seq']:03d} | " + json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",",":")))
    if phase == "pre":
        lines += ["", "PERSISTENCE_META: MNEMO_ROW:PENDING_PRE_GATE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:PENDING_PRE_GATE | WRITEBACK_EXECUTION_V1:[]"]
    else:
        lines += ["", f"PERSISTENCE_META: MNEMO_ROW:{p['mnemo_row']} | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{format_writeback_row(p['writeback_row'])} | WRITEBACK_EXECUTION_V1:[{len(p['writeback_execution'])} rows, see section]"]
        lines += ["", "## WRITEBACK_EXECUTION_V1"]
        for r in p["writeback_execution"]:
            lines.append(
                f"{r['fct']} | {r['action']} | attempted:{r['attempted']} | success:{r['success']} | "
                f"failure:{r['failure']} | blocked:{r['blocked']} | reason:{r['reason']}"
            )
    return "\n".join(lines).rstrip() + "\n"


def manifest_lines(state: dict) -> str:
    r = state["run"]
    modules = ",".join(r.get("loaded_modules", [])) or "NONE"
    degraded = ",".join(r.get("degraded_flags", [])) or "NONE"
    overrides = ",".join(r.get("route_overrides", [])) or "NONE"
    gate = state["sections"].get("GATE_STATUS_V1")
    if not isinstance(gate, dict) or set(gate) != {f"G{i}" for i in range(11)}:
        die("GATE_STATUS_V1 missing/invalid in state")
    gate_row = "GATE_STATUS_V1 | " + "|".join(f"G{i}:{gate[f'G{i}']}" for i in range(11))
    return (
        f"ENGINE:{ENGINE} | BUNDLE_REVISION:{BUNDLE_REVISION} | STATE:FINAL | RUN_ID:{r['run_id']} | PARENT_RUN_ID:{r['parent_run_id']} | AS_OF:{r['as_of']}\n"
        f"INPUT_KIND:{r['input_kind']} | MISSION_MODE:{r['mission_mode']} | INPUT_REF:{r['input_ref']} | SUBJECT_SLUG:{r['subject_slug']} | SUBJECT_FP:{r.get('subject_fingerprint','PENDING')} | INPUT_SHA256:{r.get('input_sha256','PENDING')}\n"
        f"COMPLEXITY:{r['complexity_score']}→{r['complexity']} | CHECKPOINT_SEQ:{r['checkpoint_seq']} | LAST_COMPLETED:18b | NEXT_ACTION:NONE\n"
        f"scope:{r.get('scope','PENDING')}\n"
        f"RESUME_COUNT:{r['resume_count']} | ROUTE_OVERRIDES:[{overrides}] | modules:{modules} | degraded:{degraded}\n"
        f"{gate_row}\n"
    )


def cmd_write_narrative(a):
    modes=[bool(a.source_file), bool(a.stdin)]
    if sum(modes)!=1: die("provide exactly one of --source-file or --stdin")
    st=load(a.state); out=Path(st["run"]["narrative_path"])
    text=Path(a.source_file).read_text(encoding="utf-8") if a.source_file else sys.stdin.read()
    if re.search(r"\bQRY-\d{3}\b", text):
        die("narrative must not contain volatile QRY IDs; cite stable FCT/SRC IDs instead")
    if "<!-- NARRATIVE_START -->" in text or "<!-- NARRATIVE_END -->" in text:
        die("narrative boundary markers are renderer-owned")
    atomic_write_text(out, text)
    print(out)

def cmd_render(a):
    state = load(a.state)
    if state["run"]["state"] != "FINAL":
        die("render requires state marked FINAL")
    phase = a.phase
    if phase not in {"pre", "delivery"}:
        die("phase must be pre or delivery")
    errs = state_errors(state, phase)
    if errs:
        die("state invalid for render: " + "; ".join(errs))
    narrative_path=Path(a.narrative or state["run"]["narrative_path"])
    output_path=Path(a.output or state["run"]["investigation_path"])
    if narrative_path.resolve()!=Path(state["run"]["narrative_path"]).resolve(): die("narrative path must be canonical")
    if output_path.resolve()!=Path(state["run"]["investigation_path"]).resolve(): die("investigation output path must be canonical")
    narrative = narrative_path.read_text(encoding="utf-8").strip()
    if re.search(r"\bQRY-\d{3}\b", narrative):
        die("narrative must not contain volatile QRY IDs; cite stable FCT/SRC IDs instead")
    if re.search(r"(?m)^\s*(?:ENGINE|GATE_STATUS_V1|PERSISTENCE_META)\s*[:|]", narrative):
        die("narrative contains machine-owned header/persistence fields")
    if re.search(r"(?mi)^#{1,6}\s+(?:REQUEST_LOG|EVIDENCE_REGISTRY|FCT_SOURCE_MAP_V1|REFUTATION_REGISTRY_V1|WRITEBACK_PLAN_V1|MEMORY_WRITE_MODE_V1|CHECKPOINT_LOG_V1|WRITEBACK_EXECUTION_V1|WRITEBACK_ATTEMPT_LOG_V1)\s*$", narrative) or "FACT_REGISTRY_V1" in narrative or "SECTION_STATUS_V1" in narrative:
        die("narrative contains machine-owned registry section")
    if re.search(r"(?mi)^#{1,6}\s+(?:LEAD_REGISTRY(?:_V1)?|CLAIM_REGISTRY(?:_V1)?|AXIS_REGISTRY(?:_V1)?|CAUSALITY_REGISTRY(?:_V1)?|CONTROL_REGISTRY(?:_V1)?|ACTION_REGISTRY(?:_V1)?|SEMANTIC_REGISTRIES_V1)\s*", narrative):
        die("narrative duplicates runtime-owned semantic registry; store objects in RUN_STATE")
    text = (
        manifest_lines(state) + "\n<!-- NARRATIVE_START -->\n" + narrative
        + "\n<!-- NARRATIVE_END -->\n\n" + semantic_blocks(state) + "\n" + machine_blocks(state, phase)
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(output_path, text)
    if phase == "pre":
        def _stamp(st): st["stamps"]["FINAL_RENDERED"] = now_iso()
        mutate(a.state, _stamp)
    print(output_path)


def derive_snapshot_gaps(s: dict):
    out=[]
    for kind,bucket in (("AXS","axes"),("CLM","claims"),("CAU","causal")):
        for row in s.get(bucket,[]):
            st=str(row.get("status","")).upper(); gt=row.get("gap_type") or row.get("GAP_TYPE")
            if st=="GAP" or (gt and str(gt).upper() not in {"NONE","NULL","-","UNSPECIFIED"}):
                if not gap_is_typed(row):
                    die(f"{row.get('id',kind)} GAP must have a specific gap_type and description")
                out.append({"id":row.get("id"),"kind":kind,"status":row.get("status"),"gap_type":gt,"gap":row.get("gap") or row.get("reason") or row.get("question")})
    sec=s.get("sections",{}).get("OPEN_GAPS")
    if sec not in (None,"NOT_INITIALIZED","RUNTIME_DERIVED",[]) and sec:
        out.append({"id":"OPEN_GAPS","kind":"SECTION","status":"GAP","gap_type":"SECTION","gap":sec})
    return out

def cmd_export_snapshot(a):
    s = load(a.state)
    missing = [f["id"] for f in s.get("facts", []) if eligible_fact(f) and f.get("mem", "-") in {None, "", "-"}]
    if missing:
        die("export-snapshot requires persisted memory ids for all eligible facts: " + ",".join(missing))
    snap = {
        "snapshot_schema": 1,
        "engine": ENGINE,
        "run_id": s["run"]["run_id"],
        "as_of": s["run"]["as_of"],
        "subject_slug": s["run"]["subject_slug"],
        "subject_fingerprint": s["run"].get("subject_fingerprint"),
        "input_sha256": s["run"].get("input_sha256"),
        "facts": [
            {
                "key": f["subject"], "value": f["value"][:140], "epi": f["epi"], "tier": f["tier"],
                "url": f["url"], "families": f["families"], "memory_id": f.get("mem", "-"),
                "verified_at": s["run"]["as_of"],
                "origin_run_id": s["run"]["run_id"],
            }
            for f in s["facts"]
        ],
        "gaps": derive_snapshot_gaps(s),
        "contradictions": [] if s["sections"].get("CONTRADICTION_LEDGER", "NOT_INITIALIZED") == "NOT_INITIALIZED" else s["sections"].get("CONTRADICTION_LEDGER", []),
        "created_at": now_iso(),
    }
    def contains_not_initialized(x):
        if x == "NOT_INITIALIZED": return True
        if isinstance(x, dict): return any(contains_not_initialized(v) for v in x.values())
        if isinstance(x, list): return any(contains_not_initialized(v) for v in x)
        return False
    if contains_not_initialized(snap):
        die("FINAL snapshot cannot contain NOT_INITIALIZED")
    raw = json.dumps(snap, ensure_ascii=False, separators=(",", ":"))
    out=Path(a.output or s["run"]["snapshot_path"])
    if out.resolve()!=Path(s["run"]["snapshot_path"]).resolve(): die("snapshot output path must be canonical")
    atomic_write_text(out, raw + "\n")
    print(f"{out} bytes={len(raw.encode('utf-8'))}")


def cmd_archive_certification(a):
    s=load(a.state); src=Path(a.result); out=Path(s["run"]["certification_path"]); inv=Path(s["run"]["investigation_path"])
    try: result=json.loads(src.read_text(encoding="utf-8"))
    except Exception as e: die(f"cannot read certification result: {e}")
    if result.get("verdict")!="PASS" or result.get("deterministic")!="PASS" or result.get("kernel_contract")!="delivery": die("certification must be deterministic delivery PASS")
    if not inv.is_file(): die("canonical investigation file missing")
    root=Path(s["run"]["run_dir"]).parents[2]
    declared=result.get("deliverable")
    if not declared: die("certification missing deliverable")
    declared_path=Path(declared) if Path(declared).is_absolute() else root/declared
    if declared_path.resolve()!=inv.resolve(): die("certification deliverable path mismatch")
    sha=hashlib.sha256(inv.read_bytes()).hexdigest()
    if result.get("deliverable_sha256") != sha: die("certification deliverable_sha256 mismatch")
    if not str(result.get("state_id","")).startswith("sha256:"): die("certification state_id missing")
    out.parent.mkdir(parents=True,exist_ok=True); atomic_write_text(out, json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(out)

def state_errors(s: dict, phase: str | None = None):
    errors = []
    r=s.get("run",{})
    sections = s.get("sections", {})
    missing_sections = sorted(set(CANONICAL_SECTIONS) - set(sections))
    unknown_sections = sorted(set(sections) - set(CANONICAL_SECTIONS))
    if missing_sections: errors.append("canonical sections missing: " + ",".join(missing_sections))
    if unknown_sections: errors.append("unknown canonical sections: " + ",".join(unknown_sections))
    bad_derived = sorted(name for name in DERIVED_SECTIONS if sections.get(name) != "RUNTIME_DERIVED")
    if bad_derived: errors.append("runtime-derived section authority drift: " + ",".join(bad_derived))
    try:
        root=str(Path(r.get("run_dir","")).parents[2])
        expected=canonical_run_paths(root,r.get("as_of",""),r.get("run_id",""),r.get("subject_slug",""))
        for k in ("run_dir","state_path","narrative_path","snapshot_path","investigation_path","certification_path"):
            if r.get(k)!=expected.get(k): errors.append(f"canonical path mismatch: {k}")
    except Exception:
        errors.append("cannot derive canonical run paths")
    input_meta_missing = r.get("subject_fingerprint") in {None,"","PENDING"} or r.get("subject_fingerprint_legacy_v1") in {None,"","PENDING"} or r.get("input_sha256") in {None,"","PENDING"} or r.get("input_path") in {None,"","PENDING"}
    if input_meta_missing: errors.append("input archive/fingerprint missing")
    if phase in {"pre", "delivery"} and r.get("original_input_ref") in {None, "", "PENDING"}: errors.append("final original_input_ref unresolved")
    if not input_meta_missing and not Path(r.get("input_path")).is_file(): errors.append("archived input file missing")
    mp=s.get("memory_probe") or {}
    if mp.get("status") not in {"NONE","FOUND"}: errors.append("memory probe not resolved")
    if mp.get("status")=="FOUND" and s.get("hydrated") is None: errors.append("memory probe FOUND requires HYDRATE")
    legacy_keys=set(s.get("sections",{})) & {"leads","claims","axes","causal","controls","actions"}
    if legacy_keys:
        errors.append("semantic object registries embedded in sections instead of runtime-owned buckets: " + ",".join(sorted(legacy_keys)))
    if s.get("checkpoints") and max((checkpoint_rank(x["label"]) or 0) for x in s["checkpoints"]) >= 7:
        r=s["run"]
        if str(r.get("complexity","PENDING"))=="PENDING" or str(r.get("complexity_score","PENDING"))=="PENDING": errors.append("advanced state with PENDING complexity")
        if r.get("scope")=="PENDING": errors.append("advanced state with PENDING scope")
    for kind, bucket in (("SYS", s["sys_log"]), ("QRY", s["requests"]), ("SRC", s["sources"]), ("FCT", s["facts"]), ("CP", s["checkpoints"])):
        ids = [int(x["id"].split("-")[1]) for x in bucket]
        if ids != list(range(1, len(ids) + 1)):
            errors.append(f"{kind} IDs not contiguous")
        if s["counters"].get(kind, 0) != len(ids):
            errors.append(f"{kind} counter mismatch")
    for kind in OBJECT_KINDS:
        bucket=s.get(OBJECT_BUCKETS[kind], [])
        ids=[int(x["id"].split("-")[1]) for x in bucket]
        if ids != list(range(1,len(ids)+1)): errors.append(f"{kind} IDs not contiguous")
        if s["counters"].get(kind,0) != len(ids): errors.append(f"{kind} counter mismatch")
        for row in bucket:
            if str(row.get("status", "")).strip().upper() in {"GAP", "UNKNOWN", "UNRESOLVED"} and not gap_is_typed(row):
                errors.append(f"{row.get('id', kind)} untyped GAP")
    for src in s.get("sources",[]):
        if src.get("family","").startswith("fam:") or not FAMILY_RE.fullmatch(src.get("family", "")):
            errors.append(f"invalid source family token {src.get('id')}")
    for q in s.get("requests",[]):
        sid=q.get("source")
        if sid not in {None,"","-"}:
            src=source_by_id(s,sid)
            if not src:
                errors.append(f"{q.get('id')} references unknown {sid}")
            elif q.get("mode") != "FETCH" or q.get("url") != src.get("url"):
                errors.append(f"{q.get('id')} source linkage invalid for {sid}")
    ref = {}
    for row in s.get("refutations", []):
        fid, qid = row.get("fct"), row.get("qry")
        if fid in ref:
            errors.append(f"duplicate refutation row for {fid}")
        ref[fid] = row
        fact = fact_by_id(s, fid)
        query = query_by_id(s, qid)
        if not fact:
            errors.append(f"refutation references unknown fact {fid}")
        if not query:
            errors.append(f"refutation references unknown query {qid}")
        if fact and query:
            alignment = refutation_alignment_error(fact, query)
            if alignment:
                errors.append(f"semantic refutation mismatch {fid}->{qid}: {alignment}")
    for f in s["facts"]:
        snapshot_memory_id = (s.get("memory_probe") or {}).get("memory_id")
        if f.get("origin_memory_id") not in {None, "", "-"} and f.get("origin_memory_id") == snapshot_memory_id:
            errors.append(f"{f['id']} origin_memory_id points to enclosing snapshot memory")
        for sid in f["sources"]:
            src = source_by_id(s, sid)
            if not src:
                errors.append(f"{f['id']} references unknown {sid}")
                continue
            if f["tier"] in {"✦", "✧"} and src["url"].startswith(("http://", "https://")):
                if not any(q["mode"] == "FETCH" and q["source"] == sid and q["url"] == src["url"] for q in s["requests"]):
                    errors.append(f"{f['id']} mapped {sid} lacks current FETCH trace")
        derived_families = sorted({source_by_id(s, sid)["family"] for sid in f.get("sources", []) if source_by_id(s, sid)})
        if sorted(f.get("families", [])) != derived_families:
            errors.append(f"{f['id']} families drift from runtime source map: {sorted(f.get('families', []))} != {derived_families}")
        if f["tier"] == "✦":
            if len(set(f["families"])) < 2:
                errors.append(f"{f['id']} ✦ lacks two families")
            if f["id"] not in ref:
                errors.append(f"{f['id']} ✦ lacks refutation row")
        if f["tier"] in {"✦", "✧"} and f["url"].startswith(("http://", "https://")):
            if not any(q["mode"] == "FETCH" and q["url"] == f["url"] for q in s["requests"]):
                errors.append(f"{f['id']} lacks current exact FETCH")
    if s["run"]["checkpoint_seq"] != len(s["checkpoints"]):
        errors.append("checkpoint_seq mismatch")
    prev = -1
    for cp in s["checkpoints"]:
        rank = checkpoint_rank(cp["label"])
        if rank is None or rank < prev:
            errors.append(f"checkpoint order invalid at {cp['id']}")
        if rank is not None:
            prev = rank
    if s["checkpoints"]:
        ranks=[checkpoint_rank(x["label"]) for x in s["checkpoints"]]
        required=[7,9,10,11,13,17]
        if s["run"].get("input_kind")=="DOCUMENT" or s["run"].get("complexity") in {"COMPLEX","APEX"}: required=[5]+required
        missing=[x for x in required if x not in ranks]
        if missing: errors.append("CP_COVER missing phases " + ",".join(map(str,missing)))
    if s.get("hydrated") is not None and not s.get("delta_plan"):
        errors.append("hydrated state requires DELTA_PLAN")
    if phase in {"pre", "delivery"}:
        r=s["run"]
        incomplete = [name for name in REQUIRED_REPORT_SECTIONS if sections.get(name) == "NOT_INITIALIZED"]
        if incomplete:
            errors.append(f"{phase}: report sections NOT_INITIALIZED: " + ",".join(incomplete))
        sys_calls=[str(x.get("call","")) for x in s.get("sys_log",[])]
        if sys_calls.count("MNEMO_Q") != 1: errors.append(f"{phase}: exactly one SYS MNEMO_Q required")
        route_calls=sum(1 for x in sys_calls if x in {"MEMORY_PROBE","HYDRATE"})
        if route_calls < 1: errors.append(f"{phase}: at least one SYS memory route required")
        if phase == "delivery" and "PERSIST_REBIND" not in sys_calls: errors.append("delivery: SYS PERSIST_REBIND required")
        if not REQUIRED_ALWAYS_LOAD.issubset(set(r.get("loaded_modules",[]))): errors.append(f"{phase}: ALWAYS LOAD modules not fully recorded")
        req=[]
        if r.get("input_kind")=="DOCUMENT" or r.get("complexity") in {"COMPLEX","APEX"}: req.append("LED")
        if r.get("mission_mode")=="INVESTIGATION": req.extend(["AXS","CLM"])
        if any(checkpoint_rank(x.get("label",""))==11 for x in s.get("checkpoints",[])): req.append("CAU")
        for k in dict.fromkeys(req):
            if not s.get(OBJECT_BUCKETS[k],[]): errors.append(f"{phase}: required semantic registry {k} empty")
            elif any(not semantic_terminal(k,x) for x in s.get(OBJECT_BUCKETS[k],[])): errors.append(f"{phase}: non-terminal {k} object(s)")
        r = s["run"]
        if str(r.get("complexity", "PENDING")) == "PENDING" or str(r.get("complexity_score", "PENDING")) == "PENDING" or str(r.get("scope", "PENDING")) == "PENDING":
            errors.append("final run manifest still has PENDING complexity/scope")
        if r.get("input_kind") == "UPDATE":
            if r.get("parent_run_id") in {None,"","NONE","PENDING"}: errors.append("UPDATE requires resolved parent_run_id")
        elif r.get("parent_run_id") != "NONE":
            errors.append("non-UPDATE requires parent_run_id=NONE")
        if any(str(x).startswith("RESUME_MIGRATION_") for x in r.get("route_overrides", [])) and int(r.get("resume_count",0)) == 0:
            errors.append("RESUME_MIGRATION override with resume_count=0")
        if phase == "delivery":
            errors.extend(snapshot_alignment_errors(s))
        gates = s["sections"].get("GATE_STATUS_V1")
        if s["run"]["state"] != "FINAL" or not isinstance(gates, dict) or any(gates.get(f"G{i}") != "PASS" for i in range(11)):
            errors.append(f"{phase}: FINAL with explicit G0..G10 PASS required")
        p = s["persistence"]
        if p.get("self_write_row") != "PENDING_AT_SERIALIZATION":
            errors.append("SELF_WRITE_ROW must remain PENDING_AT_SERIALIZATION")
        eligible = [f for f in s["facts"] if writeback_action(f).startswith("ELIGIBLE:")]
        if phase == "pre":
            if p.get("mnemo_row") != "PENDING_PRE_GATE" or p.get("writeback_row") != "PENDING_PRE_GATE" or p.get("writeback_execution") or p.get("attempt_history"):
                errors.append("pre persistence boundary invalid")
            if any(f.get("mem") not in {"-", ""} for f in s["facts"]):
                errors.append("pre fact mem already rebound")
        else:
            if p.get("mnemo_row") == "PENDING_PRE_GATE" or p.get("writeback_row") == "PENDING_PRE_GATE":
                errors.append("delivery persistence still pending")
            wr=p.get("writeback_row")
            if wr != "PENDING_PRE_GATE":
                keys={"eligible","attempted","success","failure","blocked"}
                if not isinstance(wr,dict) or set(wr) != keys:
                    errors.append("delivery writeback_row not structured")
            rows = p.get("writeback_execution") or []
            by_fct = {r.get("fct"): r for r in rows}
            for f in eligible:
                r = by_fct.get(f["id"])
                if not r:
                    errors.append(f"delivery missing writeback row {f['id']}")
                    continue
                if r.get("attempted",0) + r.get("blocked",0) != 1 or r.get("attempted",0) != r.get("success",0) + r.get("failure",0):
                    errors.append(f"delivery invalid writeback accounting {f['id']}")
                if r.get("success") == 1 and f.get("mem") in {"-", "", None}:
                    errors.append(f"delivery successful {f['id']} missing mem id")
            history = p.get("attempt_history") or []
            seqs = [x.get("seq") for x in history if isinstance(x, dict)]
            if not history:
                errors.append("delivery persistence attempt history missing")
            elif seqs != list(range(1, len(history) + 1)):
                errors.append("delivery persistence attempt history not contiguous")
            else:
                last = history[-1]
                if last.get("result") != "PASS":
                    errors.append("delivery last persistence attempt is not PASS")
                current = persistence_attempt_snapshot(s, last.get("result", "PARTIAL"), last.get("created_at", ""))
                current["seq"] = last.get("seq")
                if current != last:
                    errors.append("delivery persistence attempt history drifts from current state")
            persist_rows = [x for x in s.get("sys_log", []) if x.get("call") == "PERSIST_REBIND"]
            if len(persist_rows) != len(history):
                errors.append("delivery PERSIST_REBIND SYS/history count mismatch")
            elif persist_rows and persist_rows[-1].get("result") != "PASS":
                errors.append("delivery last SYS PERSIST_REBIND is not PASS")
    return errors


def cmd_validate(a):
    s = load(a.state)
    errors = state_errors(s, a.phase)
    if errors:
        for e in errors:
            print("FAIL", e)
        raise SystemExit(1)
    print("PASS")


def cmd_summary(a):
    s = load(a.state)
    ac = activity(s)
    print(json.dumps({
        "engine": s["engine"], "run_id": s["run"]["run_id"], "state": s["run"]["state"],
        "checkpoint_seq": s["run"]["checkpoint_seq"], "next_action": s["run"]["next_action"],
        "subject_fingerprint": s["run"].get("subject_fingerprint"),
        "subject_fingerprint_legacy_v1": s["run"].get("subject_fingerprint_legacy_v1"),
        "queries": len(s["requests"]), "sources": len(s["sources"]), "facts": len(s["facts"]),
        "activity": ac, "delta": {k: sum(1 for x in s["delta_plan"] if x["class"] == k) for k in sorted(DELTA_CLASSES)},
        "semantic_counts": semantic_counts(s),
        "hydrated_from": (s.get("hydrated") or {}).get("run_id"),
        "stamps": s.get("stamps", {}),
    }, ensure_ascii=False, indent=2))


def build_parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    x = sub.add_parser("paths"); x.add_argument("--run-id", required=True); x.add_argument("--as-of", required=True); x.add_argument("--subject-slug", required=True); x.add_argument("--truth-engine-root", default=os.environ.get("TRUTH_ENGINE_ROOT","/home/giak/projects/truth-engine")); x.set_defaults(func=cmd_paths)

    x = sub.add_parser("init")
    x.add_argument("--state", required=True); x.add_argument("--run-id", required=True); x.add_argument("--parent-run-id", default="NONE")
    x.add_argument("--as-of", required=True); x.add_argument("--input-kind", required=True); x.add_argument("--mission-mode", required=True)
    x.add_argument("--input-ref", required=True); x.add_argument("--subject-slug", required=True); x.add_argument("--truth-engine-root", default=os.environ.get("TRUTH_ENGINE_ROOT","/home/giak/projects/truth-engine"))
    x.add_argument("--next-action", default="1"); x.add_argument("--complexity", default="PENDING"); x.add_argument("--complexity-score", default="PENDING")
    x.add_argument("--force", action="store_true"); x.set_defaults(func=cmd_init)
    x = sub.add_parser("archive-input"); x.add_argument("--state", required=True); x.add_argument("--source-file"); x.add_argument("--text"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_archive_input)
    x = sub.add_parser("memory-probe"); x.add_argument("--state", required=True); x.add_argument("--status", required=True); x.add_argument("--memory-id"); x.add_argument("--run-id"); x.set_defaults(func=cmd_memory_probe)

    x = sub.add_parser("alloc"); x.add_argument("--state", required=True); x.add_argument("--kind", choices=ID_KINDS, required=True); x.set_defaults(func=cmd_alloc)
    x = sub.add_parser("set-run"); x.add_argument("--state", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_set_run)
    x = sub.add_parser("set-section"); x.add_argument("--state", required=True); x.add_argument("--name", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_set_section)
    x = sub.add_parser("append-section"); x.add_argument("--state", required=True); x.add_argument("--name", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_append_section)

    x = sub.add_parser("record-sys"); x.add_argument("--state", required=True); x.add_argument("--result", required=True); x.add_argument("--tool"); x.add_argument("--ref"); x.add_argument("--call", required=True); x.set_defaults(func=cmd_record_sys)
    x = sub.add_parser("record-query"); x.add_argument("--state", required=True); x.add_argument("--mode", required=True); x.add_argument("--result", required=True); x.add_argument("--url"); x.add_argument("--query")
    x.add_argument("--accept-source", action="store_true"); x.add_argument("--role"); x.add_argument("--family"); x.add_argument("--title"); x.set_defaults(func=cmd_record_query)
    x = sub.add_parser("record-source"); x.add_argument("--state", required=True); x.add_argument("--role", required=True); x.add_argument("--family", required=True); x.add_argument("--url", required=True); x.add_argument("--title"); x.set_defaults(func=cmd_record_source)
    x = sub.add_parser("link-query-source"); x.add_argument("--state", required=True); x.add_argument("--qry", required=True); x.add_argument("--src", required=True); x.set_defaults(func=cmd_link_query_source)
    x = sub.add_parser("record-fact"); x.add_argument("--state", required=True); x.add_argument("--epi", required=True); x.add_argument("--tier", required=True); x.add_argument("--url", required=True); x.add_argument("--sources", required=True); x.add_argument("--date", required=True); x.add_argument("--subject", required=True); x.add_argument("--value", required=True); x.add_argument("--mem", default="-"); x.add_argument("--origin-memory-id"); x.add_argument("--origin-run-id"); x.add_argument("--origin-verified-at"); x.set_defaults(func=cmd_record_fact)
    x = sub.add_parser("record-refutation"); x.add_argument("--state", required=True); x.add_argument("--fct", required=True); x.add_argument("--qry", required=True); x.add_argument("--status", required=True); x.set_defaults(func=cmd_record_refutation)

    x = sub.add_parser("record-object"); x.add_argument("--state", required=True); x.add_argument("--kind", choices=OBJECT_KINDS, required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_record_object)
    x = sub.add_parser("update-object"); x.add_argument("--state", required=True); x.add_argument("--id", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_update_object)
    x = sub.add_parser("update-fact"); x.add_argument("--state", required=True); x.add_argument("--id", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_update_fact)
    x = sub.add_parser("update-sys"); x.add_argument("--state", required=True); x.add_argument("--id", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_update_sys)
    x = sub.add_parser("assert-counts"); x.add_argument("--state", required=True); x.add_argument("--json", required=True); x.set_defaults(func=cmd_assert_counts)
    x = sub.add_parser("delta"); x.add_argument("--state", required=True); x.add_argument("--key", required=True); x.add_argument("--class", dest="class_", required=True); x.add_argument("--reason", required=True); x.add_argument("--memory-id"); x.add_argument("--url"); x.add_argument("--prior-verified-at"); x.set_defaults(func=cmd_delta)
    x = sub.add_parser("hydrate"); x.add_argument("--state", required=True); x.add_argument("--snapshot", required=True); x.add_argument("--memory-id"); x.set_defaults(func=cmd_hydrate)
    x = sub.add_parser("stamp"); x.add_argument("--state", required=True); x.add_argument("--name", required=True); x.set_defaults(func=cmd_stamp)
    x = sub.add_parser("checkpoint"); x.add_argument("--state", required=True); x.add_argument("--label", required=True); x.add_argument("--last-completed", required=True); x.add_argument("--next-action", required=True); x.set_defaults(func=cmd_checkpoint)
    x = sub.add_parser("set-gates"); x.add_argument("--state", required=True); x.add_argument("--json", required=True); x.set_defaults(func=cmd_set_gates)
    x = sub.add_parser("mark-final"); x.add_argument("--state", required=True); x.set_defaults(func=cmd_mark_final)
    x = sub.add_parser("set-persistence"); x.add_argument("--state", required=True); x.add_argument("--json"); x.add_argument("--json-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_set_persistence)
    x = sub.add_parser("write-narrative"); x.add_argument("--state", required=True); x.add_argument("--source-file"); x.add_argument("--stdin", action="store_true"); x.set_defaults(func=cmd_write_narrative)
    x = sub.add_parser("render"); x.add_argument("--state", required=True); x.add_argument("--narrative"); x.add_argument("--output"); x.add_argument("--phase", choices=("pre", "delivery"), required=True); x.set_defaults(func=cmd_render)
    x = sub.add_parser("export-snapshot"); x.add_argument("--state", required=True); x.add_argument("--output"); x.set_defaults(func=cmd_export_snapshot)
    x = sub.add_parser("archive-certification"); x.add_argument("--state", required=True); x.add_argument("--result", default=".verify/result.json"); x.set_defaults(func=cmd_archive_certification)
    x = sub.add_parser("validate"); x.add_argument("--state", required=True); x.add_argument("--phase", choices=("pre","delivery")); x.set_defaults(func=cmd_validate)
    x = sub.add_parser("summary"); x.add_argument("--state", required=True); x.set_defaults(func=cmd_summary)
    return p


def main(argv=None):
    a = build_parser().parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
