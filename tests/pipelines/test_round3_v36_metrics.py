#!/usr/bin/env python3
"""
test_round3_v36_metrics.py — Tests unitaires ROUND 3 corrections P0 verdict v36.

Couvre les 4 BLOQUANTS P0 fermes par `AUDIT_ANTAGONISTE_v36_ROUND2_VERDICT_2026-07-05.md` :

- B.3 (M1-M9 → M1-M12) : M10 profondeur PELOTE / M11 positions_acteurs source / M12 recommandations acteur_cible+horizon.
- Integration : verdict_from_metrics utilise 12 metriques (GO >= 8/12, NO-GO declenche si M10 absent).

100% stdlib, 0 token LLM, pytest compatible.
Convention runner : `rtk pytest tests/pipelines/test_round3_v36_metrics.py -v`.

Note 2026-07-05 : tests `test_classify_*` et `test_classify_integration_extract_python` (qui
dependaient de `extractors/cartographie.py` Phase 0) SUPPRIMES — Phase 0 eliminee du Sublimator
(overengineering pour le besoin « 1 article publiable depuis N enquetes »). cf. git log.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Permettre import relatif au package sublimator via sys.path
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
# M10 : profondeur PELOTE
# ---------------------------------------------------------------------------

def test_m10_pelote_depth_empty():
    """Quintessence sans causalites_pelote : score 0, depth 0."""
    d, n, s = m10_pelote_depth({})
    assert d == 0 and n == 0 and s == 0.0


def test_m10_pelote_depth_niveau4():
    """Arborecence complete 4 niveaux : score 10/10, max_depth 4."""
    q = {
        "causalites_pelote": [
            {"niveau": 1, "type": "mecanisme", "enonce": "M1"},
            {"niveau": 2, "type": "sous-mecanisme", "enonce": "M1.1"},
            {"niveau": 3, "type": "fait", "enonce": "Fait 1.1.1"},
            {"niveau": 4, "type": "source", "enonce": "F-001", "parent": "fait"},
        ]
    }
    d, n, s = m10_pelote_depth(q)
    assert d == 4 and n == 4 and s == 10.0


def test_m10_pelote_depth_niveau2():
    """Arborecence partielle (2 niveaux) : score 5/10 (cible >= 7.5 NO-GO)."""
    q = {
        "causalites_pelote": [
            {"niveau": 1, "type": "mecanisme", "enonce": "M1"},
            {"niveau": 2, "type": "sous-mecanisme", "enonce": "M1.1"},
        ]
    }
    d, n, s = m10_pelote_depth(q)
    assert d == 2 and n == 2 and s == 5.0


def test_m10_pelote_depth_mixed():
    """Mix avec nodes sans niveau = 0 (defaut). max_depth = 4."""
    q = {
        "causalites_pelote": [
            {"type": "mecanisme"},  # niveau absent -> defaut 0
            {"niveau": 4, "type": "source", "enonce": "F-001"},
        ]
    }
    d, n, s = m10_pelote_depth(q)
    assert d == 4 and n == 2 and s == 10.0  # min(4,4)/4 = 1.0 * 10


# ---------------------------------------------------------------------------
# M11 : positions_acteurs source §
# ---------------------------------------------------------------------------

def test_m11_positions_acteurs_all_ok():
    """3 positions_acteurs toutes avec source §X.Y : 100% OK."""
    q = {
        "positions_acteurs": [
            {"acteur": "A", "source": "§1.1"},
            {"acteur": "B", "source": "§X.Y"},
            {"acteur": "C", "source": "§3.2"},
        ]
    }
    h, n, pct = m11_positions_acteurs_source(q)
    assert h == 0 and n == 3 and pct == 100.0


def test_m11_positions_acteurs_partial():
    """2 OK sur 3 : pct ~33.3% NO-GO (< 50%)."""
    q = {
        "positions_acteurs": [
            {"acteur": "A", "source": "§1.1"},
            {"acteur": "B", "source": "http://url"},  # invalide
            {"acteur": "C", "source": "§3.2"},
        ]
    }
    h, n, pct = m11_positions_acteurs_source(q)
    assert h == 1 and n == 3 and pct == 66.7


def test_m11_positions_acteurs_empty():
    """Pas de positions_acteurs : pct 0 (degradation visible)."""
    h, n, pct = m11_positions_acteurs_source({})
    assert h == 0 and n == 0 and pct == 0.0


# ---------------------------------------------------------------------------
# M12 : recommandations acteur_cible + horizon
# ---------------------------------------------------------------------------

def test_m12_recommandations_all_ok():
    """3 recommandations toutes avec acteur_cible + horizon valide."""
    q = {
        "recommandations": [
            {"action": "A1", "acteur_cible": "Parlement", "horizon": "court"},
            {"action": "A2", "acteur_cible": "Prefecture", "horizon": "moyen"},
            {"action": "A3", "acteur_cible": "CESE", "horizon": "long"},
        ]
    }
    h, n, pct = m12_recommandations_acteur_horizon(q)
    assert h == 0 and n == 3 and pct == 100.0


def test_m12_recommandations_invalid_horizon():
    """horizon invalide (non dans {court, moyen, long}) compte comme violation."""
    q = {
        "recommandations": [
            {"action": "A1", "acteur_cible": "X", "horizon": "immediat"},  # invalide
            {"action": "A2", "acteur_cible": "Y", "horizon": "long"},
        ]
    }
    h, n, pct = m12_recommandations_acteur_horizon(q)
    assert h == 1 and n == 2 and pct == 50.0


def test_m12_recommandations_actor_empty():
    """acteur_cible vide compte comme violation."""
    q = {
        "recommandations": [
            {"action": "A1", "acteur_cible": "", "horizon": "court"},  # vide
            {"action": "A2", "acteur_cible": "X", "horizon": "court"},
        ]
    }
    h, n, pct = m12_recommandations_acteur_horizon(q)
    assert h == 1 and n == 2 and pct == 50.0


# ---------------------------------------------------------------------------
# Verdict integration : 12 metriques
# ---------------------------------------------------------------------------

def test_verdict_go_with_12_metrics():
    """Tous GO : 12/12 metriques dans cible GO."""
    metrics = {
        "M1": 0.85, "M2": 0.75, "M3": 2.0, "M4": 2.0, "M5": 100.0, "M6": 40000,
        "M7": 5.0, "M8": 9.0, "M9": 1.0,
        "M10": 10.0, "M11": 100.0, "M12": 100.0,
    }
    v, _ = verdict_from_metrics(metrics)
    assert v == "GO"


def test_verdict_no_go_wo_pelote():
    """PELOTE absent (M10=0) declenche NO-GO meme si reste OK."""
    metrics = {
        "M1": 0.85, "M2": 0.75, "M3": 2.0, "M4": 2.0, "M5": 100.0, "M6": 40000,
        "M7": 5.0, "M8": 9.0, "M9": 1.0,
        "M10": 0.0,  # PELOTE absent -> NO-GO
        "M11": 100.0, "M12": 100.0,
    }
    v, _ = verdict_from_metrics(metrics)
    assert v == "NO-GO"


def test_verdict_pivot_intermediate():
    """Mix : quelques OK, quelques NO-GO -> PIVOT."""
    metrics = {
        "M1": 0.65,  # NOT >= 0.7 GO, mais >= 0.5 NO-GO (intermediate)
        "M2": 0.55, "M3": 8.0, "M4": 8.0, "M5": 98.0, "M6": 60000,
        "M7": 12.0, "M8": 7.5, "M9": 3.0,
        "M10": 5.0,  # NOT >= 7.5 mais >= 2.5 NO-GO
        "M11": 75.0,  # < 100 mais >= 50 NO-GO
        "M12": 75.0,
    }
    v, _ = verdict_from_metrics(metrics)
    assert v == "PIVOT"


# ---------------------------------------------------------------------------
# Cibles spec v36 §13.3.2
# ---------------------------------------------------------------------------

def test_cibles_go_no_go_keys_present():
    """Les 12 cles (M1-M12) sont dans CIBLES_GO et CIBLES_NO_GO."""
    for k in range(1, 13):
        key = f"M{k}"
        assert key in CIBLES_GO, f"{key} missing from CIBLES_GO"
        assert key in CIBLES_NO_GO, f"{key} missing from CIBLES_NO_GO"


def test_m10_targets():
    """M10 cible GO >= 7.5 / 10 (75% profondeur arborescente 4 niveaux)."""
    assert CIBLES_GO["M10"] >= 7.5
    assert CIBLES_NO_GO["M10"] < 5.0  # seuil NO-GO permissif


def test_m11_targets():
    """M11 cible GO == 100% positions_acteurs sourcees."""
    assert CIBLES_GO["M11"] == 100.0
    assert CIBLES_NO_GO["M11"] < 100.0


def test_m12_targets():
    """M12 cible GO == 100% recommandations valides."""
    assert CIBLES_GO["M12"] == 100.0
    assert CIBLES_NO_GO["M12"] < 100.0
