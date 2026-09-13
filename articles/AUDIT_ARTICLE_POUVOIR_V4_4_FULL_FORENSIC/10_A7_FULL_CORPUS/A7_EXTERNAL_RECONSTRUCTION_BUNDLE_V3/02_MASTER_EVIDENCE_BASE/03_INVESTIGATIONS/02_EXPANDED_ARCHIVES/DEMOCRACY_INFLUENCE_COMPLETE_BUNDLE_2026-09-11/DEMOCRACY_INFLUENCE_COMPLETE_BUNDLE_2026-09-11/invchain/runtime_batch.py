#!/usr/bin/env python3
"""Transactional in-process runner for Truth Engine 2.10.6/R3P1 run_state.py.

Purpose: remove per-mutation Python process startup without changing Truth Engine code,
state schema, gates, evidence semantics, or certification. The canonical ZIP remains immutable.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

PACK_SHA256 = "d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30"
ENGINE = "2.10.6"
BUNDLE_REVISION = "R3"
SCHEMA = 1

FACTS_ALLOWED = {
    "set-run", "memory-probe", "record-query", "record-source", "update-source",
    "link-query-source", "record-fact", "record-refutation", "record-object",
    "update-object", "update-fact", "assert-counts", "delta", "hydrate", "stamp",
    "checkpoint", "set-section", "append-section",
}
TAIL_ALLOWED = {
    "record-object", "update-object", "update-fact", "set-section", "append-section",
    "checkpoint", "set-gates", "mark-final", "assert-counts", "stamp",
}
PERSISTENCE_ALLOWED = {"set-persistence"}
ALLOWED_BY_STAGE = {
    "facts": FACTS_ALLOWED,
    "tail": TAIL_ALLOWED,
    "persistence": PERSISTENCE_ALLOWED,
}
SIDE_EFFECT_CMDS = {
    "paths", "init", "archive-input", "write-narrative", "render", "export-snapshot",
    "archive-certification",
}


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_replace_bytes(path: pathlib.Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".runner-", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def verify_pack(pack: pathlib.Path) -> None:
    if not pack.is_file():
        raise SystemExit(f"canonical pack not found: {pack}")
    got = sha256_file(pack)
    if got != PACK_SHA256:
        raise SystemExit(f"canonical pack SHA mismatch: expected={PACK_SHA256} got={got}")


def load_runtime(pack: pathlib.Path, engine_root: pathlib.Path):
    verify_pack(pack)
    runtime_path = engine_root / "tools" / "runtime" / "run_state.py"
    if not runtime_path.is_file():
        raise SystemExit(f"run_state.py not found under engine root: {runtime_path}")
    spec = importlib.util.spec_from_file_location("truth_engine_run_state_locked", runtime_path)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot import canonical run_state.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if getattr(mod, "ENGINE", None) != ENGINE or getattr(mod, "BUNDLE_REVISION", None) != BUNDLE_REVISION:
        raise SystemExit(
            f"runtime identity mismatch: ENGINE={getattr(mod, 'ENGINE', None)} REV={getattr(mod, 'BUNDLE_REVISION', None)}"
        )
    return mod


def read_state(path: pathlib.Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"cannot read state {path}: {exc}") from exc


def load_stage(path: pathlib.Path) -> dict:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"cannot read stage JSON {path}: {exc}") from exc
    if obj.get("schema") != SCHEMA:
        raise SystemExit(f"unsupported stage schema: {obj.get('schema')}")
    stage = str(obj.get("stage", "")).lower()
    if stage not in ALLOWED_BY_STAGE:
        raise SystemExit("stage must be facts|tail|persistence")
    base = obj.get("base_state_sha256")
    if not isinstance(base, str) or len(base) != 64:
        raise SystemExit("stage requires exact base_state_sha256")
    cmds = obj.get("commands")
    if not isinstance(cmds, list) or not cmds or len(cmds) > 500:
        raise SystemExit("stage commands must be a non-empty list with <=500 entries")
    for i, row in enumerate(cmds, 1):
        if not isinstance(row, dict) or set(row) != {"cmd", "args"}:
            raise SystemExit(f"stage command {i} must contain exactly cmd,args")
        cmd = row["cmd"]
        args = row["args"]
        if cmd in SIDE_EFFECT_CMDS or cmd == "record-sys":
            raise SystemExit(f"stage command {i} forbidden in transaction: {cmd}")
        if cmd not in ALLOWED_BY_STAGE[stage]:
            raise SystemExit(f"stage command {i} not allowed for {stage}: {cmd}")
        if not isinstance(args, list) or any(not isinstance(x, str) for x in args):
            raise SystemExit(f"stage command {i} args must be list[str]")
        if "--state" in args or "--stdin" in args:
            raise SystemExit(f"stage command {i} must not supply --state/--stdin")
    if stage == "facts":
        last = cmds[-1]
        if last["cmd"] != "checkpoint" or not _arg_value(last["args"], "--label", "").upper() == "FACTS":
            raise SystemExit("facts stage must end with checkpoint --label FACTS")
    elif stage == "tail":
        if cmds[-1]["cmd"] != "mark-final":
            raise SystemExit("tail stage must end with mark-final")
    else:
        if len(cmds) != 1 or cmds[0]["cmd"] != "set-persistence":
            raise SystemExit("persistence stage must contain exactly one set-persistence command")
    return obj


def _arg_value(args: list[str], key: str, default=None):
    try:
        i = args.index(key)
    except ValueError:
        return default
    return args[i + 1] if i + 1 < len(args) else default


def run_runtime(mod, argv: list[str]) -> tuple[str, str]:
    out = io.StringIO()
    err = io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            mod.main(argv)
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 1
        if code not in (0, None):
            msg = err.getvalue().strip() or out.getvalue().strip() or f"runtime exited {code}"
            raise RuntimeError(msg) from exc
    return out.getvalue(), err.getvalue()


def stage_postconditions(stage: str, before: dict, after: dict) -> None:
    if stage == "facts":
        if after.get("run", {}).get("state") != "OPEN":
            raise RuntimeError("facts stage must leave state OPEN")
        cps = after.get("checkpoints") or []
        if not cps or str(cps[-1].get("label", "")).upper() != "FACTS" or cps[-1].get("status") != "PASS":
            raise RuntimeError("facts stage did not end at FACTS PASS")
    elif stage == "tail":
        if after.get("run", {}).get("state") != "FINAL":
            raise RuntimeError("tail stage must end FINAL")
        if after.get("run", {}).get("last_completed") != "18b":
            raise RuntimeError("tail stage must end last_completed=18b")
    else:
        old_hist = len((before.get("persistence") or {}).get("attempt_history") or [])
        new_hist = (after.get("persistence") or {}).get("attempt_history") or []
        if len(new_hist) != old_hist + 1:
            raise RuntimeError("persistence stage must add exactly one persistence attempt")
        if str(new_hist[-1].get("result", "")).upper() != "PASS":
            raise RuntimeError("persistence attempt is not PASS")
        old_pr = sum(1 for x in before.get("sys_log", []) if x.get("call") == "PERSIST_REBIND")
        new_pr = sum(1 for x in after.get("sys_log", []) if x.get("call") == "PERSIST_REBIND")
        if new_pr != old_pr + 1:
            raise RuntimeError("persistence must create exactly one runtime-owned PERSIST_REBIND")


def cmd_apply(a) -> int:
    started = time.perf_counter()
    pack = pathlib.Path(a.pack).resolve()
    engine_root = pathlib.Path(a.engine_root).resolve()
    state = pathlib.Path(a.state).resolve()
    stage_path = pathlib.Path(a.stage_file).resolve()
    mod = load_runtime(pack, engine_root)
    spec = load_stage(stage_path)
    if not state.is_file():
        raise SystemExit(f"state not found: {state}")
    before_bytes = state.read_bytes()
    before_sha = hashlib.sha256(before_bytes).hexdigest()
    if before_sha != spec["base_state_sha256"]:
        raise SystemExit(f"stage base state SHA mismatch: expected={spec['base_state_sha256']} got={before_sha}")
    before = json.loads(before_bytes)
    if spec["stage"] == "persistence":
        hist = (before.get("persistence") or {}).get("attempt_history") or []
        if hist and str(hist[-1].get("result", "")).upper() == "PASS":
            raise SystemExit("persistence already PASS; do not create a duplicate PERSIST_REBIND")
    fd, tmp_name = tempfile.mkstemp(prefix=state.name + ".stage-", suffix=".json", dir=str(state.parent))
    os.close(fd)
    tmp = pathlib.Path(tmp_name)
    try:
        tmp.write_bytes(before_bytes)
        outputs = []
        for idx, row in enumerate(spec["commands"], 1):
            argv = [row["cmd"], "--state", str(tmp), *row["args"]]
            try:
                stdout, _stderr = run_runtime(mod, argv)
            except RuntimeError as exc:
                raise SystemExit(f"stage command {idx}/{len(spec['commands'])} {row['cmd']} failed: {exc}") from exc
            if stdout.strip():
                outputs.append(stdout.strip().splitlines()[-1])
        # Every command executes the canonical runtime validation on a disposable clone.
        # Full run validation belongs to PRE/DELIVERY; running it at FACTS would wrongly
        # require future checkpoints and would duplicate the gate contract.
        after = read_state(tmp)
        stage_postconditions(spec["stage"], before, after)
        after_bytes = tmp.read_bytes()
        atomic_replace_bytes(state, after_bytes)
        result = {
            "status": "PASS",
            "stage": spec["stage"],
            "commands": len(spec["commands"]),
            "before_sha256": before_sha,
            "after_sha256": hashlib.sha256(after_bytes).hexdigest(),
            "elapsed_seconds": round(time.perf_counter() - started, 3),
            "last_output": outputs[-1] if outputs else None,
        }
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def run_gate(engine_root: pathlib.Path, phase: str, deliverable: pathlib.Path) -> tuple[int, str, str]:
    verify = engine_root / "tools" / "verify" / "verify.py"
    if not verify.is_file():
        raise SystemExit(f"verify.py not found: {verify}")
    p = subprocess.run(
        [sys.executable, str(verify), "gate", "--file", str(deliverable), "--kernel-contract", phase],
        cwd=str(engine_root), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return p.returncode, p.stdout, p.stderr


def state_deliverable(state: pathlib.Path) -> pathlib.Path:
    obj = read_state(state)
    p = obj.get("run", {}).get("investigation_path")
    if not p:
        raise SystemExit("state lacks run.investigation_path")
    return pathlib.Path(p)


def cmd_pre(a) -> int:
    started = time.perf_counter()
    pack = pathlib.Path(a.pack).resolve(); root = pathlib.Path(a.engine_root).resolve(); state = pathlib.Path(a.state).resolve()
    mod = load_runtime(pack, root)
    if read_state(state).get("run", {}).get("state") != "FINAL":
        raise SystemExit("PRE requires FINAL state after mark-final")
    run_runtime(mod, ["render", "--state", str(state), "--phase", "pre"])
    deliverable = state_deliverable(state)
    code, out, err = run_gate(root, "pre", deliverable)
    if code != 0:
        sys.stderr.write(err)
        raise SystemExit(code)
    print(json.dumps({"status":"PASS","phase":"pre","elapsed_seconds":round(time.perf_counter()-started,3),"deliverable":str(deliverable)}, ensure_ascii=False, sort_keys=True))
    return 0


def cmd_delivery(a) -> int:
    started = time.perf_counter()
    pack = pathlib.Path(a.pack).resolve(); root = pathlib.Path(a.engine_root).resolve(); state = pathlib.Path(a.state).resolve()
    mod = load_runtime(pack, root)
    obj = read_state(state)
    hist = (obj.get("persistence") or {}).get("attempt_history") or []
    if not hist or str(hist[-1].get("result", "")).upper() != "PASS":
        raise SystemExit("DELIVERY requires terminal persistence PASS")
    run_runtime(mod, ["render", "--state", str(state), "--phase", "delivery"])
    deliverable = state_deliverable(state)
    code, out, err = run_gate(root, "delivery", deliverable)
    if code != 0:
        sys.stderr.write(err)
        raise SystemExit(code)
    verify_result = root / ".verify" / "result.json"
    run_runtime(mod, ["archive-certification", "--state", str(state), "--result", str(verify_result)])
    run_runtime(mod, ["stamp", "--state", str(state), "--name", "DELIVERY_PASS"])
    # Local state validation only; verify gate already ran the complete test suite exactly once.
    run_runtime(mod, ["validate", "--state", str(state), "--phase", "delivery"])
    print(json.dumps({"status":"PASS","phase":"delivery","elapsed_seconds":round(time.perf_counter()-started,3),"deliverable":str(deliverable),"certification":read_state(state).get("run",{}).get("certification_path")}, ensure_ascii=False, sort_keys=True))
    return 0


def cmd_check_pack(a) -> int:
    pack = pathlib.Path(a.pack).resolve(); root = pathlib.Path(a.engine_root).resolve()
    mod = load_runtime(pack, root)
    print(json.dumps({"status":"PASS","pack_sha256":PACK_SHA256,"engine":mod.ENGINE,"bundle_revision":mod.BUNDLE_REVISION}, sort_keys=True))
    return 0


def build_parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("check-pack", "pre", "delivery"):
        x = sub.add_parser(name)
        x.add_argument("--pack", required=True)
        x.add_argument("--engine-root", required=True)
        if name != "check-pack":
            x.add_argument("--state", required=True)
    x = sub.add_parser("apply")
    x.add_argument("--pack", required=True)
    x.add_argument("--engine-root", required=True)
    x.add_argument("--state", required=True)
    x.add_argument("--stage-file", required=True)
    return p


def main(argv=None):
    a = build_parser().parse_args(argv)
    if a.cmd == "apply": return cmd_apply(a)
    if a.cmd == "pre": return cmd_pre(a)
    if a.cmd == "delivery": return cmd_delivery(a)
    return cmd_check_pack(a)


if __name__ == "__main__":
    raise SystemExit(main())
