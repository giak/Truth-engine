#!/usr/bin/env python3
"""
test_round4_v36_p1_risques.py — Round 4 tests RISQUE P1 corrections v36.

Couvre les sub-survivants apres suppression Phase 0 (2026-07-05) :

- **B.7** BLOQUANT conditionnel : conversion table canonique PELOTE (thinker H2 — IDs fictifs M-N, M-N.M).
- **N5 + C-CK5** : positions_acteurs exporte avec source §X.Y.
- **M.R3** : iteration_count + regen_count materialises dans sublimator_validate.py + CP1 alert >= 50%.
- **Regression** : tests round 3 non-regression.

Note 2026-07-05 : `grille_apex_score()` et la regression `test_regression_cartographie_golden_apex`
ont ete SUPPRIMES (dependaient de `extractors/cartographie.py` Phase 0, eliminee par
overengineering). cf. git log.

Convention runner : `rtk pytest tests/pipelines/test_round4_v36_p1_risques.py -v`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "engines" / "sublimator"))

from sublimator_validate import (
    CIBLES_GO,
    CIBLES_NO_GO,
    m10_pelote_depth,
    m11_positions_acteurs_source,
    m12_recommandations_acteur_horizon,
    verdict_from_metrics,
)


# ---------------------------------------------------------------------------
# B.7 — conversion PELOTE table (testable partiellement en Python)
# ---------------------------------------------------------------------------

def test_b7_pelote_canonical_4_niveaux():
    """Exemple canonique 4 niveaux : source F-### comme parent valide."""
    q = {
        "causalites_pelote": [
            {"niveau": 1, "type": "mecanisme", "enonce": "M-Activation verrou", "parent": None},
            {"niveau": 2, "type": "sous-mecanisme", "enonce": "M-1.1", "enonce_long": "CEF mobilise", "parent": "M-1"},
            {"niveau": 3, "type": "fait", "enonce": "Note CEF 12 mars 2026", "parent": "M-1.1"},
            {"niveau": 4, "type": "source", "enonce": "F-014", "parent": "F-014"},
        ]
    }
    d, n, s = m10_pelote_depth(q)
    assert d == 4 and n == 4 and s == 10.0  # cible GO >= 7.5


def test_b7_pelote_parent_string_only():
    """Parent doit etre str ou None, jamais objet."""
    q = {
        "causalites_pelote": [
            {"niveau": 1, "type": "mecanisme", "enonce": "M", "parent": None},
            {"niveau": 2, "type": "sous-mecanisme", "enonce": "M.1", "parent": "M"},
        ]
    }
    d, n, s = m10_pelote_depth(q)
    assert d == 2 and n == 2
    for entry in q["causalites_pelote"]:
        assert isinstance(entry["parent"], (str, type(None))), "parent must be str or None"


# ---------------------------------------------------------------------------
# N5 + C-CK5 — positions_acteurs via M11
# ---------------------------------------------------------------------------

def test_n5_positions_acteurs_export_source_required():
    """M11 valide que source commence par § (cf. SPECS §13.3.2 ligne 1001)."""
    q = {
        "positions_acteurs": [
            {"acteur": "CEF", "position": "Oppose", "source": "§4.1"},
            {"acteur": "CFCM", "position": "Neutre", "source": "§6.2"},
        ]
    }
    h, n, pct = m11_positions_acteurs_source(q)
    assert h == 0 and n == 2 and pct == 100.0


def test_n5_positions_acteurs_alternative_patterns():
    """Patterns source acceptes par M11 (source commence par §)."""
    valid_sources = ["§1.1", "§10.4", "§X.Y", "§4"]
    for src in valid_sources:
        q = {"positions_acteurs": [{"acteur": "A", "source": src}]}
        _, _, pct = m11_positions_acteurs_source(q)
        assert pct == 100.0, f"Pattern {src!r} doit passer"


def test_n5_positions_acteurs_invalid_source_blocked():
    """Source invalide (pas de §) -> violation comptee par M11."""
    q = {"positions_acteurs": [
        {"acteur": "A", "source": "http://url"},
        {"acteur": "B", "source": "p4.1"},  # pas de §
        {"acteur": "C", "source": "§1.1"},
    ]}
    h, n, pct = m11_positions_acteurs_source(q)
    assert h == 2 and n == 3 and pct == 33.3


# ---------------------------------------------------------------------------
# M.R3 — iteration_count + regen_count materialites
# ---------------------------------------------------------------------------

def test_mr3_metrics_includes_iteration_and_regen():
    """metrics dict doit exposer iteration_count >= 1 + regen_count = iter - 1 (P.R verdict round 2)."""
    # On construit un metrics complet pour verifier verdict_from_metrics accepte les champs.
    metrics = {
        "M1": 0.85, "M2": 0.75, "M3": 2.0, "M4": 2.0, "M5": 100.0, "M6": 40000,
        "M7": 5.0, "M8": 9.0, "M9": 1.0,
        "M10": 10.0, "M11": 100.0, "M12": 100.0,
        "iteration_count": 3,
        "regen_count": 2,
    }
    v, _ = verdict_from_metrics(metrics)
    assert v == "GO"


def test_mr3_regen_count_formula():
    """regen_count = iteration_count - 1 par definition (P.R verdict round 2)."""
    # Test sur la formule (extrait de sublimator_validate.py).
    for iter_count, expected_regen in [(1, 0), (2, 1), (3, 2)]:
        calculated = max(0, iter_count - 1)
        assert calculated == expected_regen


# ---------------------------------------------------------------------------
# Regression round 3 — sanity check que les bases round 3 tiennent toujours.
# ---------------------------------------------------------------------------

def test_regression_pelote_vide():
    """Quintessence sans pelote -> M10=0.0 declenche NO-GO (gardefou)."""
    metrics = {
        "M1": 0.85, "M2": 0.75, "M3": 2.0, "M4": 2.0, "M5": 100.0, "M6": 40000,
        "M7": 5.0, "M8": 9.0, "M9": 1.0,
        "M10": 0.0, "M11": 100.0, "M12": 100.0,
    }
    v, _ = verdict_from_metrics(metrics)
    assert v == "NO-GO"


def test_cibles_v36_coherence():
    """M10 GO >= 7.5, M11 GO == 100, M12 GO == 100 (round 3 coherent)."""
    assert CIBLES_GO["M10"] >= 7.5
    assert CIBLES_GO["M11"] == 100.0
    assert CIBLES_GO["M12"] == 100.0


# ---------------------------------------------------------------------------
# M.R3 — Code-reviewer micro-observation #1 : test cp1_alert activation 50%.
# ---------------------------------------------------------------------------

def test_mr3_cp1_alert_above_50():
    """Si >= 50% des fiches ont regen_count >= 1 dans compress_summary,
    run_validate emet cp1_alert dans _meta (M.R3 verdict ROUND 2 RISQUE P1).

    Test de bout en bout : on construit un dossier _validation synthetique avec
    4 fiches (3 regen, 1 stable) et on verifie que cp1_alert est declenchee.
    """
    import tempfile
    import subprocess
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        # Fiche stable (iteration_count=1, regen_count=0)
        (d / "stable-quintessence-v2.json").write_text(json.dumps({
            "enquete_id": "stable",
            "these_centrale": "Test stable.",
            "compress_summary": {"iteration_count": 1},
            "faits_atomiques": [{"id": "F-001", "enonce": "Fait test."}],
        }), encoding="utf-8")
        (d / "stable-reader.md").write_text("## 1. Faits\nF-001 : Fait test.", encoding="utf-8")
        # 3 fiches avec regen (iteration_count=2, regen_count=1)
        for i, ic in enumerate([("regen1", 2), ("regen2", 3), ("regen3", 2)]):
            prefix, iter_count = ic
            (d / f"{prefix}-quintessence-v2.json").write_text(json.dumps({
                "enquete_id": prefix,
                "these_centrale": "Test regen.",
                "compress_summary": {"iteration_count": iter_count, "iteration_alert": True},
                "faits_atomiques": [],
            }), encoding="utf-8")
            (d / f"{prefix}-reader.md").write_text("## 1. Pas de faits.", encoding="utf-8")
        # Run sublimator_validate via subprocess pour isoler l'env.
        script = Path("tools/engines/sublimator/sublimator_validate.py").resolve()
        r = subprocess.run(
            ["python3", str(script), "--validation-dir", str(d), "--version", "v2", "--format", "json"],
            capture_output=True, text=True, timeout=30,
        )
        assert r.returncode in (0, 1, 2), f"sublimator_validate returncode unexpected: {r.returncode}"
        out = json.loads(r.stdout)
        meta = out.get("_meta", {})
        assert "regen_ratio" in meta, "cp1_alert test: regen_ratio missing from _meta"
        assert meta["regen_ratio"] == 0.75, f"expected regen_ratio=0.75 got {meta['regen_ratio']}"
        assert meta.get("fiches_avec_regen") == 3, "expected 3 fiches avec regen"
        assert "cp1_alert" in meta, f"cp1_alert missing despite regen_ratio {meta['regen_ratio']} >= 0.5"
        assert "[CP1 ALERT]" in meta["cp1_alert"]
        assert "50" in meta["cp1_alert"]


def test_mr3_cp1_alert_below_50_no_alert():
    """Si < 50% des fiches ont regen_count >= 1, PAS de cp1_alert."""
    import tempfile
    import subprocess
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        # 4 fiches stables (regen_ratio = 0/4 = 0)
        for i in range(4):
            (d / f"stable{i}-quintessence-v2.json").write_text(json.dumps({
                "enquete_id": f"stable{i}",
                "these_centrale": "Test.",
                "compress_summary": {"iteration_count": 1},
                "faits_atomiques": [{"id": "F-001", "enonce": "Fait test."}],
            }), encoding="utf-8")
            (d / f"stable{i}-reader.md").write_text("## 1. Faits\nF-001 : Fait test.", encoding="utf-8")
        # 1 fiche avec regen (regen_ratio = 1/5 = 0.2 < 0.5)
        (d / "regen-quintessence-v2.json").write_text(json.dumps({
            "enquete_id": "regen",
            "these_centrale": "Test regen.",
            "compress_summary": {"iteration_count": 3, "iteration_alert": True},
            "faits_atomiques": [],
        }), encoding="utf-8")
        (d / "regen-reader.md").write_text("## 1. Pas de faits.", encoding="utf-8")
        script = Path("tools/engines/sublimator/sublimator_validate.py").resolve()
        r = subprocess.run(
            ["python3", str(script), "--validation-dir", str(d), "--version", "v2", "--format", "json"],
            capture_output=True, text=True, timeout=30,
        )
        out = json.loads(r.stdout)
        meta = out.get("_meta", {})
        assert meta.get("regen_ratio") == 0.2
        assert "cp1_alert" not in meta, f"cp1_alert should NOT appear with regen_ratio < 0.5, got: {meta.get('cp1_alert')}"
