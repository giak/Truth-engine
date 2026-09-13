import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("run_state_r3", ROOT / "tools/runtime/run_state.py")
rs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rs)


def test_axs_saturated_requires_attempt_and_result_ids():
    row = {
        "id":"AXS-001", "axis":"MECHANISMS", "question":"q", "sought_objects":["record"],
        "links":["CLM-001"], "attempt_ids":[], "result_ids":[], "status":"SATURATED",
    }
    errors = rs.semantic_contract_errors("AXS", row)
    assert any("attempt_ids" in x for x in errors)
    assert any("result_ids" in x for x in errors)
    assert rs.semantic_terminal("AXS", row) is False


def test_claim_requires_counter_and_explicit_gap_state():
    row = {
        "id":"CLM-001", "claim":"x", "claimant":"source", "materiality":"DECISIVE",
        "support":["FCT-001"], "counter":"", "gap_type":"", "gap":"", "status":"SUPPORTED",
    }
    errors = rs.semantic_contract_errors("CLM", row)
    assert any("counter" in x for x in errors)
    assert any("gap_type" in x for x in errors)


def test_source_contract_requires_forensic_provenance():
    src={"id":"SRC-001","role":"◈","family":"A","url":"https://example.org","title":"t"}
    errors=rs.source_contract_errors(src)
    assert any("canonical_id" in x for x in errors)
    assert any("locator" in x for x in errors)
    assert any("checked_at" in x for x in errors)


def test_loaded_module_alias_and_duplicates_rejected():
    errors=rs.canonical_module_errors({"loaded_modules":["definitions/SYMBOLS.md","truth-engine-v2/definitions/SYMBOLS.md","definitions/SYMBOLS.md"]})
    assert any("duplicates" in x for x in errors)
    assert any("non-canonical" in x for x in errors)


def test_forensic_sections_are_markdown_not_json():
    state={
        "sections": {name: [] for name in rs.CANONICAL_SECTIONS},
    }
    for name in rs.DERIVED_SECTIONS:
        state["sections"][name]="RUNTIME_DERIVED"
    state["sections"]["GATE_STATUS_V1"]={f"G{i}":"PASS" for i in range(11)}
    state["sections"]["SCOPING_REPORT"]={"object_question":"What?","period":"2026"}
    text=rs.forensic_sections(state)
    assert "## FORENSIC_SECTIONS_V1" in text
    assert "### SCOPING_REPORT" in text
    assert "**object_question:** What?" in text
    assert '{"object_question"' not in text
