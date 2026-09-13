from tools.verify import verify


def test_verify_semantic_ir_rejects_saturated_axis_without_attempts():
    text='''SEMANTIC_COUNTS_V1:LED:0|CLM:0|AXS:1|CAU:0|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1
### LEAD_REGISTRY_V1
### CLAIM_REGISTRY_V1
### AXIS_REGISTRY_V1
AXS-001 | {"axis":"MECHANISMS","question":"q","sought_objects":["x"],"links":["CLM-001"],"attempt_ids":[],"result_ids":[],"status":"SATURATED"}
### CAUSALITY_REGISTRY_V1
### CONTROL_REGISTRY_V1
### ACTION_REGISTRY_V1
'''
    _declared,_observed,errors=verify._kernel_semantic_registry(text)
    assert any("attempt_ids" in x for x in errors)
    assert any("result_ids" in x for x in errors)


def test_verify_source_parser_requires_nine_field_provenance():
    text='''## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://example.org

## FCT_SOURCE_MAP_V1
'''
    rows,_dups,errors=verify._kernel_source_rows(text)
    assert not rows
    assert any("9 champs" in x for x in errors)


def test_verify_source_parser_accepts_complete_row():
    text='''## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | cid:example | Example title | 2026-09-01 | 2026-09-06T08:00:00Z | p.3 | https://example.org/a

## FCT_SOURCE_MAP_V1
'''
    rows,_dups,errors=verify._kernel_source_rows(text)
    assert errors == []
    assert rows[1]["locator"] == "p.3"
    assert rows[1]["url"] == "https://example.org/a"


def test_forensic_projection_requires_all_set_sections():
    status={name:("DERIVED" if name in verify.DERIVED_SECTIONS else "EMPTY") for name in verify.CANONICAL_SECTIONS}
    status["GATE_STATUS_V1"]="SET"
    status["SCOPING_REPORT"]="SET"
    text='''FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:0|SRC_COMPLETE:0/0
## FORENSIC_SECTIONS_V1
### SCOPING_REPORT
NONE
## TRACE_MATRIX_V1
'''
    errors=verify._kernel_forensic_projection(text,status)
    assert any("SCOPING_REPORT: SET mais vide" in x for x in errors)
