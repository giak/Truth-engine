import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("run_state", ROOT / "tools/runtime/run_state.py")
rs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rs)


def _fact(mem="-"):
    return {
        "id": "FCT-001",
        "epi": "FACT",
        "tier": "✧",
        "mem": mem,
        "subject": "fact-key",
        "value": "fact-value",
        "url": "https://example.org/a",
        "families": ["A"],
    }


def _state(tmp_path, *, degraded=True, blocked=True, mem="-", reason="MNEMO_UNAVAILABLE"):
    fact = _fact(mem)
    action = rs.writeback_action(fact)
    row = {
        "fct": "FCT-001",
        "action": action,
        "attempted": 0 if blocked else 1,
        "success": 0 if blocked else 1,
        "failure": 0,
        "blocked": 1 if blocked else 0,
        "reason": reason if blocked else "NONE",
    }
    wr = {
        "eligible": 1,
        "attempted": row["attempted"],
        "success": row["success"],
        "failure": 0,
        "blocked": row["blocked"],
    }
    return {
        "schema": 1,
        "engine": "2.10.6",
        "run": {
            "run_id": "20260905-1600-test",
            "as_of": "2026-09-05",
            "subject_slug": "test",
            "subject_fingerprint": "sha256:test",
            "input_sha256": "sha256:input",
            "snapshot_path": str(tmp_path / "snapshot.json"),
            "degraded_flags": ["MNEMO_UNAVAILABLE"] if degraded else [],
        },
        "facts": [fact],
        "axes": [],
        "claims": [],
        "causal": [],
        "sections": {"OPEN_GAPS": []},
        "persistence": {
            "mnemo_row": "FAIL:MNEMO_UNAVAILABLE" if blocked else "PASS",
            "self_write_row": "PENDING_AT_SERIALIZATION",
            "writeback_row": wr,
            "writeback_execution": [row],
            "attempt_history": [],
        },
    }


def _seal_attempt(s):
    result = rs.persistence_attempt_result(s)
    attempt = rs.persistence_attempt_snapshot(s, result, "2026-09-05T16:00:00+00:00")
    s["persistence"]["attempt_history"] = [attempt]
    return result


def test_mnemo_unavailable_is_terminal_pass_when_observed(tmp_path):
    s = _state(tmp_path, degraded=True, blocked=True)
    assert _seal_attempt(s) == "PASS"
    assert rs._fact_persistence_terminal(s, s["facts"][0]) is True


def test_mnemo_block_without_degraded_flag_is_partial(tmp_path):
    s = _state(tmp_path, degraded=False, blocked=True)
    assert rs.persistence_attempt_result(s) == "PARTIAL"


def test_successful_write_still_requires_memory_id(tmp_path):
    s = _state(tmp_path, degraded=False, blocked=False, mem="-")
    assert rs.persistence_attempt_result(s) == "PARTIAL"


def test_successful_write_with_memory_id_passes(tmp_path):
    s = _state(tmp_path, degraded=False, blocked=False, mem="mem-123")
    assert _seal_attempt(s) == "PASS"


def test_snapshot_allows_terminal_blocked_fact_without_fake_memory_id(tmp_path):
    s = _state(tmp_path, degraded=True, blocked=True)
    assert _seal_attempt(s) == "PASS"
    state_path = tmp_path / "state.json"
    state_path.write_text(json.dumps(s), encoding="utf-8")
    rs.cmd_export_snapshot(SimpleNamespace(state=str(state_path), output=None))
    snap = json.loads(Path(s["run"]["snapshot_path"]).read_text(encoding="utf-8"))
    assert snap["facts"][0]["memory_id"] == "-"
    assert rs.snapshot_alignment_errors(s) == []


def test_snapshot_rejects_unresolved_eligible_fact(tmp_path):
    s = _state(tmp_path, degraded=False, blocked=False, mem="-")
    # Force an apparently PASS attempt to ensure export rechecks actual terminal state.
    attempt = rs.persistence_attempt_snapshot(s, "PASS", "2026-09-05T16:00:00+00:00")
    s["persistence"]["attempt_history"] = [attempt]
    state_path = tmp_path / "state.json"
    state_path.write_text(json.dumps(s), encoding="utf-8")
    try:
        rs.cmd_export_snapshot(SimpleNamespace(state=str(state_path), output=None))
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("snapshot export should have rejected unresolved fact")


def test_illegal_block_reason_is_partial(tmp_path):
    s = _state(tmp_path, degraded=True, blocked=True, reason="MADE_UP_REASON")
    assert rs.persistence_attempt_result(s) == "PARTIAL"


def test_blocked_fact_cannot_carry_fake_memory_id(tmp_path):
    s = _state(tmp_path, degraded=True, blocked=True, mem="fake-mem")
    assert rs.persistence_attempt_result(s) == "PARTIAL"
