# Cartographie Campagne 2026-09 — Plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produire, dans `investigations/2026-09/`, un script Python offline qui agrège les données des 39 dossiers de la campagne (RUN_STATE + MNEMO_SNAPSHOT + INVESTIGATION) et génère `campagne_cartographie.json` + `campagne_cartographie.md` (inventaire des sujets, atlas des faits, matrice 7 classes, gaps, topologie).

**Architecture:** Script unique stdlib (lecture seule, déterministe), tests TDD sur fixtures temporaires, surcharge manuelle de mapping via `campagne_classes.json`.

**Tech Stack:** Python 3.12, pytest (disponible : `~/.local/bin/pytest`), stdlib uniquement.

## Global Constraints

- Périmètre : seulement `investigations/2026-09/` (sous-dossiers ; les `.md` de racine et les sorties propres du script sont exclus du scan).
- Stdlib Python 3 uniquement — aucun appel réseau, aucune dépendance MCP/MnemoLite, aucune écriture dans les dossiers d'investigation existants.
- Déterministe : même entrée → même sortie (tri stable ; seul `generated_at` varie).
- Mapping 7 classes : heuristique `auto` + primauté de la table manuelle `override` ; jamais présenté comme certifié.
- Les chiffres réels du dossier sont des **bornes de validation** à recouper (39 dossiers, ~25 RUN_STATE, 167 faits : ✦119/✧48, tous avec URL) — le script compte, il ne suppose pas.
- Commits : les étapes `git commit` du format skill sont listées mais **exécutées uniquement sur demande explicite de l'utilisateur** (règle projet).

## File Structure

| Fichier | Rôle |
|---|---|
| `investigations/2026-09/mapper_cartographie.py` | Script principal (scan, extraction, mapping, gaps, rendu) |
| `investigations/2026-09/campagne_classes.json` | Table de surcharge manuelle (seed initial honnête) |
| `investigations/2026-09/campagne_cartographie.json` | Sortie agrégée (générée par le script) |
| `investigations/2026-09/campagne_cartographie.md` | Rapport lisible (généré) |
| `investigations/2026-09/test_mapper_cartographie.py` | Tests (import via `sys.path`) |

---

### Task 0 : Scaffolding du test + helper de fixture

**Files:**
- Create: `investigations/2026-09/test_mapper_cartographie.py`
- Create: `investigations/2026-09/mapper_cartographie.py` (squelette minimal, fonctions vides)

**Interfaces:**
- Produces: `build_fixture(tmp_path: pathlib.Path) -> pathlib.Path` — construit 4-5 faux dossiers d'investigation réutilisés par tous les tests.

- [ ] **Step 1: Créer le squelette du script**

`mapper_cartographie.py` :

```python
#!/usr/bin/env python3
"""Cartographie de la campagne 2026-09 - aggregation offline des investigations."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR_DEFAULT = Path(__file__).resolve().parent
OUT_JSON = "campagne_cartographie.json"
OUT_MD = "campagne_cartographie.md"
OVERRIDES_FILE = "campagne_classes.json"

TIERS = ("✦", "✧", "⁅", "❧")

CLASSES = (
    "transactionnelle",
    "informationnelle",
    "lobbying",
    "reseau",
    "etrangere_etatique",
    "coercitive",
    "effet_asymetrie",
)


def scan_dirs(base: Path) -> list[str]:
    raise NotImplementedError


def classify_dir(base: Path, name: str) -> dict:
    raise NotImplementedError


def load_json(path: Path | None) -> dict | None:
    raise NotImplementedError


def extract_title(base: Path, info: dict) -> str:
    raise NotImplementedError


def extract_facts(run_state: dict | None, origin_run: str, subject_dir: str) -> list[dict]:
    raise NotImplementedError


def extract_actions_pending(run_state: dict | None) -> list[dict]:
    raise NotImplementedError


def extract_causal_gaps(run_state: dict | None) -> list[dict]:
    raise NotImplementedError


def extract_leads_non_saturated(run_state: dict | None) -> list[dict]:
    raise NotImplementedError


def extract_run_id(run_state: dict | None) -> str:
    raise NotImplementedError


def map_classes(info: dict, title: str, run_state: dict | None, overrides: dict) -> list[dict]:
    raise NotImplementedError


def derive_gaps(subjects: list[dict], facts: list[dict]) -> dict:
    raise NotImplementedError


def build_data(base: Path, overrides: dict) -> dict:
    raise NotImplementedError


def render_markdown(data: dict) -> str:
    raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Créer le fichier de tests avec la fixture**

`test_mapper_cartographie.py` :

```python
"""Tests du mapper de campagne 2026-09 (fixtures temporaires, jamais les données réelles)."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mapper_cartographie as mc


def build_fixture(tmp_path: Path) -> Path:
    base = tmp_path / "campagne"
    base.mkdir()

    kernel = base / "2026-09-05_achat-de-vote-france-ue"
    kernel.mkdir()
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_INVESTIGATION.md").write_text(
        "# Achat de vote - France et UE\n\nCorps du rapport.\n", encoding="utf-8"
    )
    run_state = {
        "schema": 1,
        "engine": "2.10.6",
        "run": {"id": "20260905-1100-achat-de-vote-france-ue"},
        "facts": [
            {
                "key": "achat de vote documenté",
                "value": "Affaire X : paiement constaté.",
                "epi": "FACT",
                "tier": "✦",
                "families": ["A", "B"],
                "url": "https://example.org/achat",
                "memory_id": "mem-0001",
            },
            {
                "key": "corruption locale hypothétique",
                "value": "Cas Y non tranché.",
                "epi": "FACT",
                "tier": "✧",
                "families": ["D"],
                "url": "https://example.org/corruption",
                "memory_id": "mem-0002",
            },
        ],
        "actions": [
            {"id": "ACT-001", "status": "PENDING", "text": "Saisir les juridictions."},
            {"id": "ACT-002", "status": "DONE", "text": "Déjà fait."},
        ],
        "causal": [
            {
                "id": "CAU-001",
                "status": "GAP",
                "gap_type": "EVIDENCE_GAP",
                "text": "Causalité non quantifiable.",
            }
        ],
        "leads": [
            {"id": "LED-001", "status": "OPEN", "priority": "HIGH", "subject": "Vérifier le cas Y."}
        ],
    }
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_RUN_STATE.json").write_text(
        json.dumps(run_state, ensure_ascii=False), encoding="utf-8"
    )
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_CERTIFICATION.json").write_text(
        json.dumps({"verdict": "PASS", "kernel_contract": "delivery"}), encoding="utf-8"
    )
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_INPUT.txt").write_text("input", encoding="utf-8")
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_NARRATIVE.tmp.md").write_text("n", encoding="utf-8")
    (kernel / "2026-09-05_11-00_achat-de-vote-france-ue_MNEMO_SNAPSHOT.json").write_text(
        json.dumps({"snapshot_schema": 1}), encoding="utf-8"
    )

    partial = base / "2026-09-05_uk-brexit-v2"
    partial.mkdir()
    (partial / "2026-09-05_12-00_uk-brexit-v2_RUN_STATE.json").write_text(
        json.dumps({"facts": []}), encoding="utf-8"
    )

    bare = base / "2026-09-05_justice-deux-vitesses-weaponisation-judiciaire"
    bare.mkdir()
    (bare / "2026-09-05_justice-deux-vitesses_INVESTIGATION.md").write_text(
        "# Justice à deux vitesses\n", encoding="utf-8"
    )

    empty = base / "2026-09-05_uk-brexit-dark-money-flux-financiers"
    empty.mkdir()

    # Fichiers de sortie que le script doit ignorer (fichiers, pas dossiers)
    (base / mc.OUT_JSON).write_text("{}", encoding="utf-8")
    (base / mc.OUT_MD).write_text("x", encoding="utf-8")

    return base
```

- [ ] **Step 3: Lancer la suite — l'import du squelette passe (pas encore de tests actifs)**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`
Expected: l'import réussit (squelette présent), pas encore de tests actifs. Le squelette n'est pas exécuté.

- [ ] **Step 4: Commit** (uniquement à la demande explicite de l'utilisateur)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/test_mapper_cartographie.py
git commit -m "chore: scaffold mapper campagne 2026-09"
```

---

### Task 1 : Scan et classification des dossiers

**Files:**
- Modify: `investigations/2026-09/mapper_cartographie.py`
- Test: `investigations/2026-09/test_mapper_cartographie.py`

**Interfaces:**
- Consumes: `build_fixture` (Task 0).
- Produces:
  - `scan_dirs(base: Path) -> list[str]`
  - `classify_dir(base: Path, name: str) -> dict` avec clés `name`, `kind` ∈ {`kernel`, `partial`, `bare`, `empty`}, `files` (int), `inv_file`, `run_file`, `cert_file` (str|None).

- [ ] **Step 1: Écrire les tests qui échouent**

```python
def test_scan_dirs_retourne_dossiers_tries(tmp_path):
    base = build_fixture(tmp_path)
    dirs = mc.scan_dirs(base)
    assert dirs == sorted(dirs)
    assert len(dirs) == 4
    assert "2026-09-05_achat-de-vote-france-ue" in dirs


def test_classify_dir_kinds(tmp_path):
    base = build_fixture(tmp_path)
    assert mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")["kind"] == "kernel"
    assert mc.classify_dir(base, "2026-09-05_uk-brexit-v2")["kind"] == "partial"
    assert mc.classify_dir(base, "2026-09-05_justice-deux-vitesses-weaponisation-judiciaire")["kind"] == "bare"
    assert mc.classify_dir(base, "2026-09-05_uk-brexit-dark-money-flux-financiers")["kind"] == "empty"
```

- [ ] **Step 2: Lancer — attendu FAIL (NotImplementedError)**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 3: Implémenter**

```python
def scan_dirs(base: Path) -> list[str]:
    return sorted(p.name for p in base.iterdir() if p.is_dir())


def classify_dir(base: Path, name: str) -> dict:
    d = base / name
    files = [p.name for p in d.iterdir() if p.is_file()]
    inv = next((f for f in files if f.endswith("_INVESTIGATION.md")), None)
    run = next((f for f in files if f.endswith("_RUN_STATE.json")), None)
    cert = next((f for f in files if f.endswith("_CERTIFICATION.json")), None)
    if run and inv and cert:
        kind = "kernel"
    elif run:
        kind = "partial"
    elif files:
        kind = "bare"
    else:
        kind = "empty"
    return {
        "name": name,
        "kind": kind,
        "files": len(files),
        "inv_file": inv,
        "run_file": run,
        "cert_file": cert,
    }
```

- [ ] **Step 4: Lancer — attendu PASS**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 5: Commit** (sur demande)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/test_mapper_cartographie.py
git commit -m "feat: scan et classification des dossiers campagne"
```

---

### Task 2 : Extraction des faits, tiers, actions, gaps, leads, run_id

**Files:**
- Modify: `investigations/2026-09/mapper_cartographie.py`
- Test: `investigations/2026-09/test_mapper_cartographie.py`

**Interfaces:**
- Consumes: `classify_dir`, `load_json`.
- Produces:
  - `load_json(path: Path | None) -> dict | None` (None si chemin absent/invalide)
  - `extract_title(base, info) -> str`
  - `extract_facts(run_state, origin_run, subject_dir) -> list[dict]` — chaque dict : `{key, value, tier, families:list, url, memory_id, origin_run, subject_dir}`
  - `extract_actions_pending(run_state) -> list[dict]` — `{id, text}` status == PENDING
  - `extract_causal_gaps(run_state) -> list[dict]` — `{id, text, gap_type}` status GAP ou gap_type EVIDENCE_GAP
  - `extract_leads_non_saturated(run_state) -> list[dict]` — `{id, subject, priority}` status != SATURATED
  - `extract_run_id(run_state) -> str`

- [ ] **Step 1: Écrire les tests qui échouent**

```python
def test_extract_facts_normalise(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    facts = mc.extract_facts(rs, "run-1", "2026-09-05_achat-de-vote-france-ue")
    assert len(facts) == 2
    assert facts[0]["tier"] == "✦"
    assert facts[0]["url"] == "https://example.org/achat"
    assert facts[0]["memory_id"] == "mem-0001"
    assert facts[0]["families"] == ["A", "B"]
    assert facts[0]["origin_run"] == "run-1"
    assert facts[1]["tier"] == "✧"


def test_extract_actions_causal_leads(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    assert mc.extract_actions_pending(rs) == [
        {"id": "ACT-001", "text": "Saisir les juridictions."}
    ]
    gaps = mc.extract_causal_gaps(rs)
    assert len(gaps) == 1 and gaps[0]["id"] == "CAU-001" and gaps[0]["gap_type"] == "EVIDENCE_GAP"
    leads = mc.extract_leads_non_saturated(rs)
    assert len(leads) == 1 and leads[0]["id"] == "LED-001" and leads[0]["subject"] == "Vérifier le cas Y."


def test_extract_run_id(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    assert mc.extract_run_id(rs) == "20260905-1100-achat-de-vote-france-ue"


def test_extract_title(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    assert mc.extract_title(base, info) == "Achat de vote - France et UE"


def test_load_json_absent():
    assert mc.load_json(None) is None
    assert mc.load_json(Path("/nonexistent/path.json")) is None
```

- [ ] **Step 2: Lancer — attendu FAIL**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 3: Implémenter**

```python
def load_json(path: Path | None) -> dict | None:
    if path is None or not Path(path).exists():
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else None
    except (json.JSONDecodeError, OSError):
        return None


def extract_title(base: Path, info: dict) -> str:
    inv_path = info.get("inv_file")
    if not inv_path:
        return ""
    try:
        text = (base / info["name"] / inv_path).read_text(encoding="utf-8")
    except OSError:
        return ""
    m = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return m.group(1).strip()[:200] if m else ""


def extract_facts(run_state: dict | None, origin_run: str, subject_dir: str) -> list[dict]:
    if not run_state:
        return []
    out = []
    for f in run_state.get("facts", []) or []:
        if not isinstance(f, dict):
            continue
        out.append(
            {
                "key": str(f.get("key", "")),
                "value": str(f.get("value", "")),
                "tier": str(f.get("tier", "?")),
                "families": [str(x) for x in f.get("families", []) or []],
                "url": str(f.get("url", "")),
                "memory_id": str(f.get("memory_id", "")),
                "origin_run": origin_run,
                "subject_dir": subject_dir,
            }
        )
    return out


def extract_actions_pending(run_state: dict | None) -> list[dict]:
    if not run_state:
        return []
    out = []
    for a in run_state.get("actions", []) or []:
        if isinstance(a, dict) and str(a.get("status", "")).upper() == "PENDING":
            out.append({"id": str(a.get("id", "")), "text": str(a.get("text", ""))[:200]})
    return out


def extract_causal_gaps(run_state: dict | None) -> list[dict]:
    if not run_state:
        return []
    out = []
    for c in run_state.get("causal", []) or []:
        if not isinstance(c, dict):
            continue
        if c.get("status") == "GAP" or c.get("gap_type") == "EVIDENCE_GAP":
            out.append(
                {
                    "id": str(c.get("id", "")),
                    "text": str(c.get("text", ""))[:300],
                    "gap_type": str(c.get("gap_type", "")),
                }
            )
    return out


def extract_leads_non_saturated(run_state: dict | None) -> list[dict]:
    if not run_state:
        return []
    out = []
    for l in run_state.get("leads", []) or []:
        if isinstance(l, dict) and str(l.get("status", "")).upper() != "SATURATED":
            out.append(
                {
                    "id": str(l.get("id", "")),
                    "subject": str(l.get("subject") or l.get("text") or "")[:200],
                    "priority": str(l.get("priority", "")),
                }
            )
    return out


def extract_run_id(run_state: dict | None) -> str:
    if not run_state:
        return ""
    for key in ("run", "meta"):
        v = run_state.get(key)
        if isinstance(v, dict):
            for k2 in ("id", "run_id"):
                if isinstance(v.get(k2), str) and v[k2]:
                    return v[k2]
    for k3 in ("id", "run_id"):
        v = run_state.get(k3)
        if isinstance(v, str) and v:
            return v
    return ""
```

- [ ] **Step 4: Lancer — attendu PASS**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 5: Commit** (sur demande)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/test_mapper_cartographie.py
git commit -m "feat: extraction faits, tiers, actions, causal, leads, run_id"
```

---

### Task 3 : Mapping aux 7 classes (heuristique + override)

**Files:**
- Modify: `investigations/2026-09/mapper_cartographie.py`
- Test: `investigations/2026-09/test_mapper_cartographie.py`
- Create: `investigations/2026-09/campagne_classes.json`

**Interfaces:**
- Produces:
  - `CLASS_KEYWORDS: dict[str, tuple[str, ...]]` (7 classes)
  - `_norm(s: str) -> str` (minuscules, ponctuation → espace, espaces simples)
  - `map_classes(info: dict, title: str, run_state: dict | None, overrides: dict) -> list[dict]`
    → liste `{"class": str, "source": "auto"|"override", "confidence": "high"|"medium"|"low"}`,
    triée par confiance décroissante (conf auto = high si ≥2 mots-clés distincts, medium si 1, low si 0).
    Si le nom de dossier est dans `overrides`, retourne exactement les classes listées (source override).

- [ ] **Step 1: Écrire les tests qui échouent**

```python
def test_map_classes_auto_multi(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    classes = mc.map_classes(info, "Achat de vote - France et UE", rs, {})
    cls = {c["class"]: c for c in classes}
    assert "transactionnelle" in cls
    assert cls["transactionnelle"]["source"] == "auto"
    assert cls["transactionnelle"]["confidence"] == "high"


def test_map_classes_aucun_mot_cle(tmp_path):
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_uk-brexit-dark-money-flux-financiers")
    classes = mc.map_classes(info, "", None, {})
    assert classes == []


def test_map_classes_override_prime(tmp_path):
    overrides = {"2026-09-05_achat-de-vote-france-ue": ["coercitive"]}
    base = build_fixture(tmp_path)
    info = mc.classify_dir(base, "2026-09-05_achat-de-vote-france-ue")
    rs = mc.load_json(base / info["name"] / info["run_file"])
    classes = mc.map_classes(info, "Achat de vote - France et UE", rs, overrides)
    assert classes == [{"class": "coercitive", "source": "override", "confidence": "high"}]


def test_campagne_classes_json_seed_valide(tmp_path):
    seed = json.loads(Path(__file__).resolve().parent.joinpath("campagne_classes.json").read_text(encoding="utf-8"))
    assert isinstance(seed, dict)
    for cls_list in seed.values():
        for c in cls_list:
            assert c in mc.CLASSES
```

- [ ] **Step 2: Lancer — attendu FAIL**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 3: Créer le seed `campagne_classes.json`**

```json
{
  "2026-09-05_cartographie-mecanismes-influence-democraties": ["transactionnelle", "informationnelle", "lobbying", "reseau", "etrangere_etatique", "coercitive", "effet_asymetrie"],
  "2026-09-05_paradis-data-armes-electorales": ["informationnelle"],
  "2026-09-05_uk-brexit-v2": [],
  "2026-09-05_seconde-vague-elevation-faits-non-confirmes": [],
  "2026-09-05_vague3-elevation-faits-non-confirmes-restants": []
}
```

- [ ] **Step 4: Implémenter**

```python
CLASS_KEYWORDS: dict[str, tuple[str, ...]] = {
    "transactionnelle": ("achat", "corruption", "clientélisme", "clientelisme", "triche", "vote"),
    "informationnelle": ("désinformation", "desinformation", "manipulation", "infiltration", "factcheck", "propagande", "microciblage", "deepfake"),
    "lobbying": ("lobby", "thinktank", "think tank", "capture"),
    "reseau": ("club", "siècle", "siecle", "francmacon", "franc-macon", "pantouflage", "réseau", "reseau"),
    "etrangere_etatique": ("ned", "usaid", "cia", "elnet", "aipac", "soros", "israel", "ingérence", "ingerence", "couleur", "nordstream", "nord-stream"),
    "coercitive": ("gps", "pegasus", "nso", "doppelganger", "brouillage", "cyber", "drone", "coercition", "caviardage"),
    "effet_asymetrie": ("effet", "asymétrie", "asymetrie", "narratif", "impact"),
}


def _norm(s: str) -> str:
    return " ".join(re.sub(r"[^a-zà-ÿœæ0-9]", " ", s.lower()).split())


def map_classes(info: dict, title: str, run_state: dict | None, overrides: dict) -> list[dict]:
    name = info["name"]
    if name in overrides:
        cls_list = overrides[name]
        if not isinstance(cls_list, list):
            cls_list = [cls_list]
        return [
            {"class": c, "source": "override", "confidence": "high"}
            for c in cls_list
            if c in CLASSES
        ]

    texts = [_norm(name), _norm(title)]
    if run_state:
        for bucket in ("leads", "claims", "axes"):
            for o in run_state.get(bucket, []) or []:
                if isinstance(o, dict):
                    texts.append(_norm(str(o.get("subject") or o.get("text") or "")))
        for f in run_state.get("facts", []) or []:
            if isinstance(f, dict):
                texts.append(_norm(str(f.get("key") or "")))
    blob = " ".join(texts)

    scores: dict[str, int] = {}
    for cls, kws in CLASS_KEYWORDS.items():
        hits = {kw for kw in kws if kw in blob}
        if hits:
            scores[cls] = len(hits)

    result = []
    for cls, n in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])):
        confidence = "high" if n >= 2 else "medium"
        result.append({"class": cls, "source": "auto", "confidence": confidence})
    return result
```

- [ ] **Step 5: Lancer — attendu PASS**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 6: Commit** (sur demande)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/campagne_classes.json investigations/2026-09/test_mapper_cartographie.py
git commit -m "feat: mapping 7 classes par mots-clés + surcharge manuelle"
```

---

### Task 4 : Dérivation des gaps (G1-G7)

**Files:**
- Modify: `investigations/2026-09/mapper_cartographie.py`
- Test: `investigations/2026-09/test_mapper_cartographie.py`

**Interfaces:**
- Consumes: `classify_dir`, `extract_actions_pending`, `extract_causal_gaps`,
  `extract_leads_non_saturated`, `CLASSES`.
- Produces: `derive_gaps(subjects: list[dict], facts: list[dict]) -> dict` avec clés :
  `planifie_non_execute` (diroirs dossiers empties), `hors_protocole` (bare),
  `partiel` (partial), `candidats_elevation` (liste de faits ✧),
  `actions_pending`, `questions_ouvertes`, `leads_a_traiter`,
  `angles_morts_classes` (dict class → count ≤ 1 sur les 7 classes).

- [ ] **Step 1: Écrire les tests qui échouent**

```python
def test_derive_gaps(tmp_path):
    base = build_fixture(tmp_path)
    subjects = []
    facts = []
    for name in mc.scan_dirs(base):
        info = mc.classify_dir(base, name)
        rs = mc.load_json(base / name / info["run_file"]) if info["run_file"] else None
        title = mc.extract_title(base, info)
        fcts = mc.extract_facts(rs, mc.extract_run_id(rs), name)
        facts += fcts
        subjects.append(
            {
                "name": name,
                "kind": info["kind"],
                "title": title,
                "actions_pending": mc.extract_actions_pending(rs),
                "causal_gaps": mc.extract_causal_gaps(rs),
                "leads_non_saturated": mc.extract_leads_non_saturated(rs),
            }
        )
    gaps = mc.derive_gaps(subjects, facts)
    assert gaps["planifie_non_execute"] == ["2026-09-05_uk-brexit-dark-money-flux-financiers"]
    assert gaps["hors_protocole"] == ["2026-09-05_justice-deux-vitesses-weaponisation-judiciaire"]
    assert gaps["partiel"] == ["2026-09-05_uk-brexit-v2"]
    assert len(gaps["candidats_elevation"]) == 1
    assert gaps["candidats_elevation"][0]["tier"] == "✧"
    assert len(gaps["actions_pending"]) == 1
    assert len(gaps["questions_ouvertes"]) == 1
    assert len(gaps["leads_a_traiter"]) == 1
    assert isinstance(gaps["angles_morts_classes"], dict)
    assert all(c in mc.CLASSES for c in gaps["angles_morts_classes"])
```

- [ ] **Step 2: Lancer — attendu FAIL**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 3: Implémenter**

```python
def derive_gaps(subjects: list[dict], facts: list[dict]) -> dict:
    empty_dirs = sorted(s["name"] for s in subjects if s["kind"] == "empty")
    bare_md = sorted(s["name"] for s in subjects if s["kind"] == "bare")
    partial = sorted(s["name"] for s in subjects if s["kind"] == "partial")

    candidates = []
    for f in facts:
        if f["tier"] == "✧":
            candidates.append(
                {
                    "key": f["key"],
                    "tier": "✧",
                    "url": f["url"],
                    "subject_dir": f["subject_dir"],
                }
            )

    actions_pending = []
    questions_ouvertes = []
    leads_a_traiter = []
    class_counts: dict[str, int] = {}
    for s in subjects:
        for a in s.get("actions_pending", []):
            actions_pending.append({"dir": s["name"], "id": a["id"], "text": a["text"]})
        for g in s.get("causal_gaps", []):
            questions_ouvertes.append(
                {"dir": s["name"], "id": g["id"], "text": g["text"], "gap_type": g["gap_type"]}
            )
        for l in s.get("leads_non_saturated", []):
            leads_a_traiter.append({"dir": s["name"], "id": l["id"], "subject": l["subject"]})
        for cm in s.get("classes", []):
            class_counts[cm["class"]] = class_counts.get(cm["class"], 0) + 1

    angles_morts = {c: class_counts.get(c, 0) for c in CLASSES if class_counts.get(c, 0) <= 1}

    return {
        "planifie_non_execute": empty_dirs,
        "hors_protocole": bare_md,
        "partiel": partial,
        "candidats_elevation": candidates,
        "actions_pending": actions_pending,
        "questions_ouvertes": questions_ouvertes,
        "leads_a_traiter": leads_a_traiter,
        "angles_morts_classes": angles_morts,
    }
```

- [ ] **Step 4: Lancer — attendu PASS**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 5: Commit** (sur demande)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/test_mapper_cartographie.py
git commit -m "feat: dérivation des gaps G1-G7"
```

---

### Task 5 : Agrégation `build_data` → JSON

**Files:**
- Modify: `investigations/2026-09/mapper_cartographie.py`
- Test: `investigations/2026-09/test_mapper_cartographie.py`

**Interfaces:**
- Consumes: toutes les fonctions d'extraction.
- Produces:
  - `build_data(base: Path, overrides: dict) -> dict` — clés `generated_at`, `source_dir`,
    `counts` ({dirs, with_run_state, with_full_kernel, empty_dirs}), `facts_total`
    ({n, tiers, with_url, with_memory_id}), `subjects` (list enrichie : `n_facts`, `tiers`,
    `n_leads`, `classes`, `actions_pending`, `causal_gaps`, `leads_non_saturated`, `run_id`),
    `facts`, `matrix_classes`, `gaps`, `runs_topology`.

- [ ] **Step 1: Écrire les tests qui échouent**

```python
def test_build_data_structure(tmp_path):
    base = build_fixture(tmp_path)
    data = mc.build_data(base, {})
    assert data["counts"]["dirs"] == 4
    assert data["counts"]["with_full_kernel"] == 1
    assert data["counts"]["with_run_state"] == 2
    assert data["counts"]["empty_dirs"] == 1
    assert data["facts_total"]["n"] == 2
    assert data["facts_total"]["tiers"]["✦"] == 1
    assert data["facts_total"]["tiers"]["✧"] == 1
    assert data["facts_total"]["with_url"] == 2
    assert data["facts_total"]["with_memory_id"] == 2
    assert len(data["subjects"]) == 4
    assert data["runs_topology"][0]["run_id"] == "20260905-1100-achat-de-vote-france-ue"
    assert "transactionnelle" in data["matrix_classes"]

```

- [ ] **Step 2: Lancer — attendu FAIL**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 3: Implémenter**

```python
def build_data(base: Path, overrides: dict) -> dict:
    subjects: list[dict] = []
    facts: list[dict] = []
    for name in scan_dirs(base):
        info = classify_dir(base, name)
        run_state = load_json(base / name / info["run_file"]) if info["run_file"] else None
        run_id = extract_run_id(run_state)
        title = extract_title(base, info)
        fcts = extract_facts(run_state, run_id, name)
        facts += fcts
        subjects.append(
            {
                "name": name,
                "kind": info["kind"],
                "files": info["files"],
                "title": title,
                "run_id": run_id,
                "n_facts": len(fcts),
                "tiers": {t: sum(1 for f in fcts if f["tier"] == t) for t in TIERS},
                "n_leads": len(run_state.get("leads", []) or []) if run_state else 0,
                "actions_pending": extract_actions_pending(run_state),
                "causal_gaps": extract_causal_gaps(run_state),
                "leads_non_saturated": extract_leads_non_saturated(run_state),
                "classes": map_classes(info, title, run_state, overrides),
            }
        )

    facts_total = {
        "n": len(facts),
        "tiers": {t: sum(1 for f in facts if f["tier"] == t) for t in TIERS},
        "with_url": sum(1 for f in facts if f.get("url")),
        "with_memory_id": sum(1 for f in facts if f.get("memory_id")),
    }

    matrix_classes: dict[str, list[str]] = {}
    for s in subjects:
        for cm in s["classes"]:
            matrix_classes.setdefault(cm["class"], []).append(s["name"])
    for cls in CLASSES:
        matrix_classes.setdefault(cls, [])

    counts = {
        "dirs": len(subjects),
        "with_run_state": sum(1 for s in subjects if s["kind"] in ("kernel", "partial")),
        "with_full_kernel": sum(1 for s in subjects if s["kind"] == "kernel"),
        "empty_dirs": sum(1 for s in subjects if s["kind"] == "empty"),
    }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_dir": str(base),
        "counts": counts,
        "facts_total": facts_total,
        "subjects": subjects,
        "facts": facts,
        "matrix_classes": matrix_classes,
        "gaps": derive_gaps(subjects, facts),
        "runs_topology": [
            {"run_id": s["run_id"], "subject_dir": s["name"], "facts_n": s["n_facts"], "n_leads": s["n_leads"]}
            for s in subjects
            if s["run_id"]
        ],
    }
```

- [ ] **Step 4: Lancer — attendu PASS**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 5: Commit** (sur demande)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/test_mapper_cartographie.py
git commit -m "feat: agrégation build_data"
```

---

### Task 6 : Rendu markdown + écriture des sorties + CLI

**Files:**
- Modify: `investigations/2026-09/mapper_cartographie.py`
- Test: `investigations/2026-09/test_mapper_cartographie.py`

**Interfaces:**
- Consumes: `build_data`, `render_markdown`.
- Produces:
  - `render_markdown(data: dict) -> str` — 6 sections `## §1 …` à `## §6 …`.
  - `main(argv: list[str] | None = None) -> int` — args `--base`, `--overrides`, `--out-json`,
    `--out-md` ; défauts : base = dossier du script, out = base/nom par défaut ; écrit les deux
    fichiers ; affiche un récap `OK — … N faits` ; retour 0.

- [ ] **Step 1: Écrire les tests qui échouent**

```python
def test_render_markdown_sections(tmp_path):
    base = build_fixture(tmp_path)
    data = mc.build_data(base, {})
    md = mc.render_markdown(data)
    for section in (
        "## §1 Vue d'ensemble",
        "## §2 Inventaire des sujets",
        "## §3 Atlas des faits",
        "## §4 Matrice 7 classes x dossiers",
        "## §5 Gaps & leads",
        "## §6 Topographie des runs",
    ):
        assert section in md
    assert "achat de vote documenté" in md


def test_main_ecrit_les_sorties(tmp_path):
    base = build_fixture(tmp_path)
    out_json = tmp_path / "sortie.json"
    out_md = tmp_path / "sortie.md"
    rc = mc.main(
        [
            "--base", str(base),
            "--overrides", str(tmp_path / "campagne_classes.json"),
            "--out-json", str(out_json),
            "--out-md", str(out_md),
        ]
    )
    assert rc == 0
    assert out_json.exists() and out_md.exists()
    data = json.loads(out_json.read_text(encoding="utf-8"))
    assert "facts" in data and "gaps" in data
```

Note : `--overrides` pointe ici vers un fichier absent → `load_json` retourne `None` →
`main` doit le traiter comme `{}` (pas de crash).

- [ ] **Step 2: Lancer — attendu FAIL**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 3: Implémenter**

```python
def render_markdown(data: dict) -> str:
    lines: list[str] = []
    A = lines.append
    A("# CAMPAGNE 2026-09 — Cartographie des investigations")
    A("")
    A(f"> Rapport généré automatiquement · {data['generated_at']}")
    A(f"> Périmètre : `{data['source_dir']}`")
    A("> **Règle d'honnêteté** : aucune donnée n'est inventée ; les lacunes sont étiquetées "
      "(hors-protocole, vide, non certifié). Mapping de classes : `auto` (heuristique) ou `override` (manuel).")
    A("")

    A("## §1 Vue d'ensemble")
    A("")
    c = data["counts"]
    ft = data["facts_total"]
    A("| Métrique | Valeur |")
    A("|---|---|")
    A(f"| Dossiers | {c['dirs']} |")
    A(f"| Runs KERNEL complets | {c['with_full_kernel']} |")
    A(f"| Avec RUN_STATE (kernel + partiel) | {c['with_run_state']} |")
    A(f"| Dossiers vides | {c['empty_dirs']} |")
    tiers = ft["tiers"]
    A(f"| Faits agrégés | {ft['n']} (✦ {tiers['✦']} · ✧ {tiers['✧']} · ⁅ {tiers['⁅']} · ❧ {tiers['❧']}) |")
    A(f"| Faits avec URL | {ft['with_url']} |")
    A(f"| Faits avec memory_id | {ft['with_memory_id']} |")
    A("")

    A("## §2 Inventaire des sujets")
    A("")
    A("| Dossier | Type | Sujet | Faits | Tiers | Run | Classes |")
    A("|---|---|---|---|---|---|---|")
    for s in data["subjects"]:
        tier_cell = " ".join(f"{t}:{s['tiers'][t]}" for t in TIERS)
        classes_cell = ", ".join(cm["class"] for cm in s["classes"]) or "—"
        subject_cell = s["title"][:60] or "(sans titre)"
        A(f"| `{s['name']}` | {s['kind']} | {subject_cell} | {s['n_facts']} | {tier_cell} | `{s['run_id'] or '—'}` | {classes_cell} |")
    A("")

    A("## §3 Atlas des faits")
    A("")
    A("| Fait | Tier | Familles | URL | memory_id | Run |")
    A("|---|---|---|---|---|---|")
    for f in data["facts"]:
        fams = ",".join(f["families"]) or "—"
        url = f["url"] or "—"
        A(f"| {f['key'][:80]} | {f['tier']} | {fams} | {url} | `{f['memory_id'] or '—'}` | `{f['origin_run'] or f['subject_dir']}` |")
    A("")

    A("## §4 Matrice 7 classes x dossiers")
    A("")
    A("| Classe | Dossiers |")
    A("|---|---|")
    for cls in CLASSES:
        ds = data["matrix_classes"].get(cls, [])
        cell = ", ".join(f"`{d}`" for d in ds) or "—"
        A(f"| {cls} | {cell} |")
    A("")

    A("## §5 Gaps & leads")
    A("")
    g = data["gaps"]

    def sub(title: str, items) -> None:
        A("")
        A(f"### {title} ({len(items)})")
        if not items:
            A("_Aucun_")
            return
        for it in items:
            if isinstance(it, dict):
                prefix = f"{it.get('dir')} · " if it.get("dir") else ""
                ident = f"`{it.get('id')}` " if it.get("id") else ""
                detail = it.get("text") or it.get("key") or it.get("subject") or ""
                A(f"- {prefix}{ident}{detail}")
            else:
                A(f"- `{it}`")

    sub("Dossiers planifiés non exécutés", g["planifie_non_execute"])
    sub("Hors protocole (sujet connu, faits non certifiés)", g["hors_protocole"])
    sub("Runs partiels", g["partiel"])
    sub("Faits candidats à l'élévation (✧)", g["candidats_elevation"])
    sub("Actions en attente (PENDING)", g["actions_pending"])
    sub("Questions ouvertes (EVIDENCE_GAP)", g["questions_ouvertes"])
    sub("Leads non saturés", g["leads_a_traiter"])
    A("")
    A("### Angles morts de classe (≤ 1 dossier)")
    if g["angles_morts_classes"]:
        for cls, n in sorted(g["angles_morts_classes"].items()):
            A(f"- `{cls}` : {n} dossier(s)")
    else:
        A("_Aucun_")
    A("")

    A("## §6 Topographie des runs")
    A("")
    A("| Run | Dossier | Faits | Leads |")
    A("|---|---|---|---|")
    for r in data["runs_topology"]:
        A(f"| `{r['run_id']}` | {r['subject_dir']} | {r['facts_n']} | {r['n_leads']} |")
    A("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Cartographie de la campagne 2026-09")
    ap.add_argument("--base", type=str, default=None, help="Dossier campagne (défaut : dossier du script)")
    ap.add_argument("--overrides", type=str, default=None, help="Table de surcharge JSON")
    ap.add_argument("--out-json", type=str, default=None, help="Sortie JSON")
    ap.add_argument("--out-md", type=str, default=None, help="Sortie markdown")
    args = ap.parse_args(argv)

    base = Path(args.base) if args.base else BASE_DIR_DEFAULT
    overrides_path = Path(args.overrides) if args.overrides else base / OVERRIDES_FILE
    out_json = Path(args.out_json) if args.out_json else base / OUT_JSON
    out_md = Path(args.out_md) if args.out_md else base / OUT_MD

    overrides = load_json(overrides_path) or {}
    data = build_data(base, overrides)
    out_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(render_markdown(data), encoding="utf-8")
    print(f"OK — {out_json.name} ({len(data['facts'])} faits) + {out_md.name}")
    return 0
```

Note : `overrides = load_json(...) or {}` rend `--overrides` absent/invalide non bloquant
(cf. test `test_main_ecrit_les_sorties`).

- [ ] **Step 4: Lancer — attendu PASS**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`

- [ ] **Step 5: Commit** (sur demande)

```bash
git add investigations/2026-09/mapper_cartographie.py investigations/2026-09/test_mapper_cartographie.py
git commit -m "feat: rendu markdown + CLI + écriture sorties"
```

---

### Task 7 : Exécution sur les données réelles + validation des bornes

**Files:**
- Run: `investigations/2026-09/mapper_cartographie.py`
- Create: `investigations/2026-09/campagne_cartographie.json` (généré)
- Create: `investigations/2026-09/campagne_cartographie.md` (généré)

**Interfaces:**
- Consumes: `main` (Task 6).

- [ ] **Step 1: Exécuter sur les données réelles**

Run: `python3 investigations/2026-09/mapper_cartographie.py --base investigations/2026-09`
Expected: `OK — campagne_cartographie.json (N faits) + campagne_cartographie.md`

- [ ] **Step 2: Valider les bornes contre l'inventaire connu**

Run: `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v` (toujours vert)

Vérification manuelle (le script compte — il faut que ses comptes collent à l'inventaire
préalablement vérifié du dossier) :

- `counts.dirs` = **39** dossiers (40 entrées − 1 fichier racine `2026-09-05_seconde-vague-faits-non-confirmes.md`) ;
- `counts.with_full_kernel` ~ 17 (bornes d'observation : compter réellement, pas recopier) ;
- `facts_total.n` ≈ **167**, ✦ ≈ 119, ✧ ≈ 48, `with_url` = 167 ;
- la liste des `planifie_non_execute` doit contenir les **8** dossiers `uk-brexit-*` ;
- `gaps.hors_protocole` doit contenir les 6 dossiers .md isolés.

Si un comptage diverge de l'observation, **corriger le script AVANT de valider** — jamais
l'inverse : ne pas forcer le résultat.

- [ ] **Step 3: Afficher l'angle-mort de classe et la matrice §4 pour validation humaine**

Run: `python3 -c "import json; d=json.load(open('investigations/2026-09/campagne_cartographie.json')); print(json.dumps(d['gaps']['angles_morts_classes'], ensure_ascii=False, indent=2))"`
Expected : les classes à ≤ 1 dossier, à confronter au §4 du markdown généré.

- [ ] **Step 4: Commit** (sur demande)

```bash
git add investigations/2026-09/campagne_cartographie.json investigations/2026-09/campagne_cartographie.md
git commit -m "feat: première cartographie générée de la campagne 2026-09"
```

---

### Task 8 : Calibration du surcharge manuel sur les données réelles

**Files:**
- Modify: `investigations/2026-09/campagne_classes.json`

**Interfaces:**
- Consumes: `campagne_cartographie.md` (§2 Classes) et `campagne_cartographie.json`
  (`subjects[*].classes`).

- [ ] **Step 1: Reconnaître les cas ambigus**

Run: `python3 -c "
import json
d = json.load(open('investigations/2026-09/campagne_cartographie.json'))
for s in d['subjects']:
    auto = [c['class'] for c in s['classes'] if c['source'] == 'auto']
    if s['kind'] != 'empty':
        print(f\"{s['name']} -> {auto}\")
"`

Identifier : dossiers à 0 classe ou classes douteuses (ex. `etat-profond-*`,
`convergences-systemiques-*`, `justice-2-vitesses-*`, `influences-electorales-*`).

- [ ] **Step 2: Ajouter les entrées validées dans `campagne_classes.json`**

Exemple (à confirmer par validation humaine, ne pas deviner) :

```json
{
  "2026-09-05_etat-profond-interferences-interieures-france": ["reseau"],
  "2026-09-05_paradis-data-armes-electorales": ["informationnelle"],
  "2026-09-05_justice-deux-vitesses-weaponisation-judiciaire": ["effet_asymetrie"],
  "2026-09-05_convergences-systemiques-architecture-controle": ["reseau", "coercitive"]
}
```

Ne **jamais** mettre de classe par défaut pour lever un doute : si le doute persiste
après lecture du dossier, laisser `[]` et le signaler comme `angle_mort`.

- [ ] **Step 3: Re-générer et re-valider**

Run: `python3 investigations/2026-09/mapper_cartographie.py --base investigations/2026-09`
Puis : `~/.local/bin/pytest investigations/2026-09/test_mapper_cartographie.py -v`
Expected : PASS, comptages inchangés, `subjects[*].classes` avec les `source: override` attendues.

- [ ] **Step 4: Commit** (sur demande)

```bash
git add investigations/2026-09/campagne_classes.json investigations/2026-09/campagne_cartographie.json investigations/2026-09/campagne_cartographie.md
git commit -m "feat: calibration du mapping manuel sur données réelles"
```

---

## Self-Review

**Couverture spec :**
- §2 inventaire des sujets → Task 1 (scan/classify) + §2 du rendu ✅
- §3 atlas des faits → Task 2 (extraction) + §3 ✅
- §4 matrice 7 classes → Task 3 (mapping) + §4 ✅
- §5 gaps → Task 4 (G1-G7) + §5 ✅
- §6 topographie runs → Task 2 (run_id) + §6 ✅
- JSON sortie → Task 5 ✅ · markdown + CLI → Task 6 ✅ · validation réelle → Tasks 7-8 ✅
- Contrainte « ignorer ses propres sorties » : le script ne scanne que les **sous-dossiers**
  (`p.is_dir()`), or `campagne_cartographie.*` sont des fichiers → exclus nativement ✅

**Placeholders:** aucun TBD/TODO ; tout le code est fourni.

**Cohérence des types/names :** `map_classes` retourne `{"class","source","confidence"}` ;
`build_data` stocke ces dicts dans `subjects[].classes` et `matrix_classes` — cohérent.
`derive_gaps` consomme `subjects[].classes` (pour `angles_morts_classes`) même si les first
tests de Task 4 ne le remplissent pas — vérifié : `s.get("classes", [])` est défensif ✅.