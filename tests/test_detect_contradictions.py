"""Tests de detect_contradictions.py (P5 : contradictions entre faits du registre)."""

from tools.detect_contradictions import (
    detect,
    normalize,
    report_json,
    report_text,
    scan,
)


# --- normalize ---

def test_normalize():
    assert normalize("DGSI effectif") == "dgsi-effectif"
    assert normalize("  dgsi_effectif  ") == "dgsi-effectif"
    assert normalize("-") == ""
    assert normalize("") == ""


# --- detect : contradictions ---

def _rec(fid, sujet, valeur, f="x.md"):
    return {"file": f, "fid": fid, "sujet": sujet, "valeur": valeur}


def test_detect_contradiction():
    records = [
        _rec("FCT-001", "dgsi-effectif", "5000"),
        _rec("FCT-002", "dgsi-effectif", "5500"),
    ]
    contradictions, collisions = detect(records)
    assert len(contradictions) == 1
    assert contradictions[0]["sujet"] == "dgsi-effectif"
    assert contradictions[0]["valeurs"] == ["5000", "5500"]
    assert collisions == []


def test_detect_meme_sujet_normalise_et_meme_valeur():
    # Même sujet (slug vs texte) + même valeur → pas de contradiction.
    records = [
        _rec("FCT-001", "dgsi-effectif", "5000"),
        _rec("FCT-002", "DGSI effectif", "5000"),
    ]
    contradictions, _ = detect(records)
    assert contradictions == []


def test_detect_valeur_vide_ignoree():
    records = [
        _rec("FCT-001", "dgsi-effectif", "5000"),
        _rec("FCT-002", "dgsi-effectif", "-"),
    ]
    contradictions, _ = detect(records)
    assert contradictions == []


def test_detect_sujet_placeholder_ignore():
    records = [_rec("FCT-001", "-", "x"), _rec("FCT-002", "-", "y")]
    contradictions, _ = detect(records)
    assert contradictions == []


def test_detect_collision_id():
    records = [
        _rec("FCT-001", "dgsi-effectif", "5000"),
        _rec("FCT-001", "dgsi-effectif", "5500"),
    ]
    contradictions, collisions = detect(records)
    assert len(contradictions) == 1
    assert len(collisions) == 1
    assert collisions[0]["fid"] == "FCT-001"


# --- scan + rapports ---

def _registry(facts):
    return "\n".join(["<!-- FACT_REGISTRY_V1 -->"] + facts + ["<!-- /FACT_REGISTRY_V1 -->"])


def test_scan_et_report(tmp_path, capsys):
    (tmp_path / "x.md").write_text(_registry([
        "FCT-001 | FACT | ✦ | https://a.fr/x | A,E | 2024-03-07 | dgsi-effectif | 5000",
        "FCT-002 | FACT | ✦ | https://b.fr/x | A,E | 2024-03-07 | dgsi-effectif | 5500",
    ]))
    files, records = scan([str(tmp_path)])
    assert len(files) == 1 and len(records) == 2
    contradictions, collisions = detect(records)
    assert report_text(files, records, contradictions, collisions) == 1
    out = capsys.readouterr().out
    assert "dgsi-effectif" in out and "5000" in out and "5500" in out


def test_report_json_contradiction(tmp_path, capsys):
    (tmp_path / "x.md").write_text(_registry([
        "FCT-001 | FACT | ✦ | https://a.fr/x | A,E | | dgsi-effectif | 5000",
        "FCT-002 | FACT | ✦ | https://b.fr/x | A,E | | dgsi-effectif | 5500",
    ]))
    files, records = scan([str(tmp_path)])
    contradictions, collisions = detect(records)
    assert report_json(files, records, contradictions, collisions) == 1
    out = capsys.readouterr().out
    assert '"contradictions": 1' in out


def test_report_sans_contradiction_retourne_0(tmp_path, capsys):
    (tmp_path / "x.md").write_text(_registry([
        "FCT-001 | FACT | ✦ | https://a.fr/x | A,E | | dgsi-effectif | 5000",
        "FCT-002 | FACT | ✦ | https://b.fr/x | B,C | | dgsi-effectif | 5000",
    ]))
    files, records = scan([str(tmp_path)])
    contradictions, collisions = detect(records)
    assert report_text(files, records, contradictions, collisions) == 0


def test_report_sans_registre_retourne_2(tmp_path, capsys):
    (tmp_path / "x.md").write_text("# pas de registre")
    files, records = scan([str(tmp_path)])
    contradictions, collisions = detect(records)
    assert report_text(files, records, contradictions, collisions) == 2
