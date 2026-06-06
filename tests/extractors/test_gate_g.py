from tools.engines.sublimator.extractors.gate_g import (
    compute_completude,
    gate_g_pass,
)

def test_compute_completude_basic():
    text = "F001 dette annulée. F002 autre. 100 soldats. 200 chars."
    matrice = [{"id": "F-S001"}, {"id": "F-S002"}]
    score = compute_completude(text, matrice)
    assert 0 <= score <= 100
    assert score == 50.0  # 2 F### / 4 phrases-faits

def test_gate_g_pass_medium():
    assert gate_g_pass(85, complexity="MEDIUM") is True
    assert gate_g_pass(75, complexity="MEDIUM") is False
    assert gate_g_pass(70, complexity="SIMPLE") is True
    assert gate_g_pass(90, complexity="APEX") is True
    assert gate_g_pass(85, complexity="APEX") is False
