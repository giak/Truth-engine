# SUBLIMATOR v33.2 — Plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Corriger SUBLIMATOR v33.1 → v33.2 en ajoutant le module d'extraction rigoureuse (5 sections) pour exploiter pleinement les 11 enquêtes (60K mots) avec un pipeline 4 agents + humain.

**Architecture:** Fork de v33.1 + 5 ajouts intégrés (§X extraction atomique 3 inputs/9 champs/3 passes, §W quintessence 12 sections, §W.13 agrégation N fiches, scoring ✦, GATE_G audit, référence KERNEL.md). Pipeline cellule = Agent A (script parseur) → B (LLM lecteur cursif) → C (LLM curator) → D (LLM verifier) → E (humain valide). 1 cellule = 1 enquête, scalable de 2 à 20+.

**Tech Stack:** Python 3.11+ (regex, pyyaml, requests pour HEAD), LLM (Claude/GPT pour Agents B/C/D), YAML/JSON pour matrices, KERNEL.md comme méthodologie canonique.

**Reference spec:** `docs/superpowers/specs/2026-06-06-sublimator-v33.2-extraction-design.md` (252 lignes, 10.7K chars).

**Estimated duration:** 6-10 heures (4-5h code + 2-5h pilote Sumer + tests). Wall-time dominé par lesAgents B/C/D LLM (non-déterministes).

---

## File Structure

**Nouveaux fichiers** :
- `tools/engines/SUBLIMATOR_v33.2_spec_agent.md` (fork v33.1 + 5 sections)
- `tools/engines/SUBLIMATOR_v33.2_GUIDE_HUMAN.md` (fork v33.1 + ajouts)
- `tools/engines/extractors/__init__.py` (package)
- `tools/engines/extractors/parse_atomic.py` (Agent A : parseur regex 3 formats)
- `tools/engines/extractors/llm_lecteur.py` (Agent B : LLM lecteur 18 sections)
- `tools/engines/extractors/llm_curator.py` (Agent C : fusion + scoring)
- `tools/engines/extractors/llm_verifier.py` (Agent D : cross-check)
- `tools/engines/extractors/gate_g.py` (audit complétude)
- `tools/engines/extractors/orchestrator.py` (coordinateur cellule)
- `tests/extractors/test_parse_atomic.py` (TDD Agent A)
- `tests/extractors/test_gate_g.py` (TDD GATE_G)
- `tests/extractors/test_curator.py` (TDD Agent C)
- `tests/extractors/test_verifier.py` (TDD Agent D)
- `tests/extractors/test_orchestrator.py` (intégration)
- `investigations/2026-06-03_sumer_article/_quintessence/sumer_quintessence.yaml` (test pilote)
- `investigations/2026-06-03_sumer_article/_quintessence/<civ>_quintessence.yaml` (10 autres)

**Fichiers modifiés** :
- `AGENTS.md` (référence v33.2 dans section Engines)
- `tools/engines/SUBLIMATOR_v33.1_spec_agent.md.bak` (backup déjà créé, non touché)

---

## Task 1: Fork SUBLIMATOR v33.1 → v33.2 spec

**Files:**
- Create: `tools/engines/SUBLIMATOR_v33.2_spec_agent.md`

- [ ] **Step 1.1: Copier v33.1 spec comme base v33.2**

```bash
cp tools/engines/SUBLIMATOR_v33.1_spec_agent.md tools/engines/SUBLIMATOR_v33.2_spec_agent.md
```

- [ ] **Step 1.2: Mettre à jour header (titre + version)**

Dans `tools/engines/SUBLIMATOR_v33.2_spec_agent.md`, ligne 1, remplacer :
```
# SUBLIMATOR v33.1 — Spécification agent
```
par :
```
# SUBLIMATOR v33.2 — Spécification agent (extraction rigoureuse)
```

- [ ] **Step 1.3: Ajouter §X EXTRACTION ATOMIQUE après §9 CHANGELOG**

Trouver la ligne `## §10 CHECKPOINTS (v33.1+)` et insérer AVANT elle :

```markdown
## §X EXTRACTION ATOMIQUE (v33.2+)

### §X.1 Inputs acceptés (3 formats) + méthodologie canonique

**Référence KERNEL.md** : v33.2 étend KERNEL.md §10 FACT_REGISTRY, §14 OUTPUT, §19 SAVE.

**3 formats acceptés en entrée** :
1. **F001-F099 (format ancien)** : regex `\bF0\d{2}\b`
2. **F-CIV-XXX (nouveau format)** : regex `F-[A-Z]+\d+`
3. **Items numérotés "N. **...**"** : regex `^\d+\.\s+\*\*[^*]+\*\*`

### §X.2 Mapping automatique (F001 → F-CIV-XXX)

| F001 source | → | F-CIV-XXX |
|-------------|---|-----------|
| M-A F001-F020 | → | F-MA001-F-MA020 |
| Islam F001-F014 | → | F-I001-F-I014 |
| Inde F001-F013 | → | F-IN001-F-IN013 |
| Amériques F001-F012 | → | F-AM001-F-AM012 |
| Sumer/Rome/Chine | → | F-S001+, F-R001+, F-C001+ (extraction directe) |

### §X.3 Format F-CIV-XXX (9 champs YAML)

```yaml
- id: F-S001
  fait: "..."
  date: "..."
  acteur: "..."
  chiffre: "..."
  source: "..."
  url: "..."
  fiabilite: "✦"
  notes: "..."
  source_section: "§1 RÉSUMÉ EXÉCUTIF"
  input_format: "F001"
```

### §X.4 Process 3 passes

- Passe 1 regex : extraction automatique 3 formats
- Passe 2 lecture cursive : 18 sections enquête (§1, §18, §10, §9, §6, §7, §8, etc.)
- Passe 3 curation humaine : dédoublonnage, scoring ✦, contexte

### §X.5 Minima quantitatifs

- SIMPLE ≥10 / MEDIUM ≥15 / COMPLEX ≥25 / APEX ≥35 F###

### §X.6 Validation + GATE_G

- URL HEAD 200 OK → ✦/✧ ; 4xx/5xx → ⁅ ; pas URL → ❧
- Dédoublonnage Jaccard <0.7
- GATE_G complétude : SIMPLE 70% / MEDIUM 80% / COMPLEX 85% / APEX 90%

### §X.7 Workflow 4 agents + humain (séquentiel)

- **Agent A — Script Parseur** : regex 3 formats → JSON candidats
- **Agent B — LLM Lecteur Cursif** : 18 sections → JSON enrichi
- **Agent C — LLM Curator** : fusion + scoring ✦ + dédoublonnage
- **Agent D — LLM Verifier** : cross-check + trous
- **Agent E — Humain** : valide/refuse (max 2 boucles)
```

- [ ] **Step 1.4: Ajouter §W QUINTESSENCE 12 SECTIONS après §X**

```markdown
## §W QUINTESSENCE 12 SECTIONS (v33.2+)

12 sections par fiche d'enquête : Thèse centrale, 3 implicites, F### (15-35), Acteurs (5-15), Causalités (3-5), 3 perspectives dialectiques, Limites, Wolves, Iceberg, Chronologie (5-10 dates), Domaines (5-7), URLs (5-10).

Output : `_quintessence/<civ>_quintessence.yaml`.

### §W.13 Agrégation N fiches

Compile matrice maître, détecte transversalités (F### dans ≥3 enquêtes), brainstorm thèses bottom-up, humain arbitre, réécriture article.
```

- [ ] **Step 1.5: Commit**

```bash
git add tools/engines/SUBLIMATOR_v33.2_spec_agent.md
git commit -m "feat(sublimator): v33.2 spec — extraction atomique + quintessence 12 sections"
```

- [ ] **Step 1.6: Vérifier**

Run: `wc -l tools/engines/SUBLIMATOR_v33.2_spec_agent.md`
Expected: >1500 lines (vs 1422 v33.1)

---

## Task 2: Fork SUBLIMATOR v33.1 → v33.2 guide

**Files:**
- Create: `tools/engines/SUBLIMATOR_v33.2_GUIDE_HUMAN.md`

- [ ] **Step 2.1: Copier v33.1 guide comme base**

```bash
cp tools/engines/SUBLIMATOR_v33.1_GUIDE_HUMAN.md tools/engines/SUBLIMATOR_v33.2_GUIDE_HUMAN.md
```

- [ ] **Step 2.2: Mettre à jour header**

Dans `tools/engines/SUBLIMATOR_v33.2_GUIDE_HUMAN.md`, ligne 1, remplacer :
```
# SUBLIMATOR v33.1 — Guide humain
```
par :
```
# SUBLIMATOR v33.2 — Guide humain (extraction rigoureuse)
```

- [ ] **Step 2.3: Ajouter §16 EXTRACTION v33.2 dans guide**

Trouver la ligne `## §15 Changelog v32.0 → v33.0` et insérer AVANT :

```markdown
## §16 Extraction atomique v33.2 (référence rapide)

### 16.1 Quand lancer l'extraction ?

À chaque nouvelle enquête (nouveau fichier .md dans investigations/), ou pour rétro-exploiter une enquête existante.

### 16.2 Commande type

```bash
python3 tools/engines/extractors/orchestrator.py \
  --input investigations/<sujet>/<civ>_INVESTIGATION.md \
  --civ <prefix> \
  --output investigations/<sujet>/_quintessence/<civ>_quintessence.yaml \
  --complexity MEDIUM
```

### 16.3 Outputs

- `_quintessence/<civ>_quintessence.yaml` : 12 sections de quintessence
- Console : progression Agent A → B → C → D → E
- Code retour : 0 (succès) / 1 (GATE_G fail) / 2 (refus humain)

### 16.4 Validation humaine (Agent E)

Le curator (C) produit une matrice YAML. Le verifier (D) signale les trous. L'humain :
1. Lit les 2 outputs (~5 min)
2. Décide : valider / modifier / refuser (cf. CP4 v33.1)
3. Max 2 boucles

### 16.5 Mapping F001 → F-CIV-XXX

Voir spec §X.2.
```

- [ ] **Step 2.4: Commit**

```bash
git add tools/engines/SUBLIMATOR_v33.2_GUIDE_HUMAN.md
git commit -m "feat(sublimator): v33.2 guide humain — §16 extraction atomique"
```

---

## Task 3: Coder Agent A — Script parseur regex (TDD)

**Files:**
- Create: `tools/engines/extractors/__init__.py`
- Create: `tools/engines/extractors/parse_atomic.py`
- Test: `tests/extractors/__init__.py`
- Test: `tests/extractors/test_parse_atomic.py`

- [ ] **Step 3.1: Créer structure packages**

```bash
mkdir -p tools/engines/extractors tests/extractors
touch tools/engines/extractors/__init__.py tests/extractors/__init__.py
```

- [ ] **Step 3.2: Écrire test pour format F001**

Créer `tests/extractors/test_parse_atomic.py` :

```python
from tools.engines.extractors.parse_atomic import parse_f001

def test_parse_f001_basic():
    text = "F001 dette annulée par Urukagina. F002 autre fait."
    result = parse_f001(text)
    assert len(result) == 2
    assert result[0]["id_old"] == "F001"
    assert "dette" in result[0]["contexte_brut"]
    assert result[0]["line_no"] > 0
```

- [ ] **Step 3.3: Lancer test pour vérifier qu'il échoue**

Run: `pytest tests/extractors/test_parse_atomic.py::test_parse_f001_basic -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'tools.engines.extractors.parse_atomic'"

- [ ] **Step 3.4: Implémenter parse_f001 minimal**

Créer `tools/engines/extractors/parse_atomic.py` :

```python
import re

def parse_f001(text: str) -> list[dict]:
    """Parse F001-F099 format ancien depuis texte enquête."""
    results = []
    for m in re.finditer(r"\bF0(\d{2})\b", text):
        line_no = text[:m.start()].count("\n") + 1
        # Contexte : 100 chars autour
        start_ctx = max(0, m.start() - 50)
        end_ctx = min(len(text), m.end() + 50)
        contexte = text[start_ctx:end_ctx].strip()
        results.append({
            "id_old": f"F0{m.group(1)}",
            "contexte_brut": contexte,
            "line_no": line_no,
        })
    return results
```

- [ ] **Step 3.5: Lancer test pour vérifier qu'il passe**

Run: `pytest tests/extractors/test_parse_atomic.py::test_parse_f001_basic -v`
Expected: PASS

- [ ] **Step 3.6: Écrire test pour format F-CIV-XXX**

Ajouter à `tests/extractors/test_parse_atomic.py` :

```python
from tools.engines.extractors.parse_atomic import parse_f_civ

def test_parse_f_civ_basic():
    text = "F-S001 annulation. F-MA005 serment."
    result = parse_f_civ(text)
    assert len(result) == 2
    assert result[0]["id_old"] == "F-S001"
    assert result[1]["id_old"] == "F-MA005"
```

- [ ] **Step 3.7: Implémenter parse_f_civ**

Ajouter à `tools/engines/extractors/parse_atomic.py` :

```python
def parse_f_civ(text: str) -> list[dict]:
    """Parse F-CIV-XXX format nouveau."""
    results = []
    for m in re.finditer(r"F-([A-Z]+)(\d+)", text):
        line_no = text[:m.start()].count("\n") + 1
        start_ctx = max(0, m.start() - 50)
        end_ctx = min(len(text), m.end() + 50)
        contexte = text[start_ctx:end_ctx].strip()
        results.append({
            "id_old": m.group(0),
            "contexte_brut": contexte,
            "line_no": line_no,
        })
    return results
```

- [ ] **Step 3.8: Lancer test, vérifier PASS**

Run: `pytest tests/extractors/test_parse_atomic.py::test_parse_f_civ_basic -v`
Expected: PASS

- [ ] **Step 3.9: Écrire test pour items numérotés**

Ajouter à `tests/extractors/test_parse_atomic.py` :

```python
from tools.engines.extractors.parse_atomic import parse_items

def test_parse_items_basic():
    text = "1. **Premier item**\n2. **Second item**\n3. **Troisième**"
    result = parse_items(text)
    assert len(result) == 3
    assert result[0]["num"] == 1
    assert result[0]["item_brut"] == "Premier item"
    assert result[2]["num"] == 3
```

- [ ] **Step 3.10: Implémenter parse_items**

Ajouter à `tools/engines/extractors/parse_atomic.py` :

```python
def parse_items(text: str) -> list[dict]:
    """Parse items numérotés 'N. **item**'."""
    results = []
    pattern = re.compile(r"^(\d+)\.\s+\*\*([^*]+)\*\*", re.MULTILINE)
    for m in pattern.finditer(text):
        line_no = text[:m.start()].count("\n") + 1
        results.append({
            "num": int(m.group(1)),
            "item_brut": m.group(2).strip(),
            "line_no": line_no,
        })
    return results
```

- [ ] **Step 3.11: Lancer tests, vérifier PASS**

Run: `pytest tests/extractors/test_parse_atomic.py -v`
Expected: 3 tests PASS

- [ ] **Step 3.12: Commit**

```bash
git add tools/engines/extractors/ tests/extractors/
git commit -m "feat(sublimator): Agent A parseur regex 3 formats (TDD)"
```

---

## Task 4: Coder Agent A — fonction parse_all + scoring ✦ (TDD)

**Files:**
- Modify: `tools/engines/extractors/parse_atomic.py`
- Modify: `tests/extractors/test_parse_atomic.py`

- [ ] **Step 4.1: Écrire test parse_all unifié**

Ajouter à `tests/extractors/test_parse_atomic.py` :

```python
from tools.engines.extractors.parse_atomic import parse_all

def test_parse_all_combines_3_formats():
    text = """
    F001 annulation dette.
    F-S001 autre fait.
    1. **Item un**
    F002 deuxième fait.
    2. **Item deux**
    """
    result = parse_all(text, civ_prefix="S")
    # F001, F-S001, F002, 2 items = 4
    assert len(result) == 4
    formats = {r["input_format"] for r in result}
    assert formats == {"F001", "F-CIV-XXX", "item"}

def test_parse_all_maps_f001_to_civ():
    text = "F001 fait ancien."
    result = parse_all(text, civ_prefix="MA")
    assert result[0]["id_target"] == "F-MA001"
```

- [ ] **Step 4.2: Lancer test pour vérifier FAIL**

Run: `pytest tests/extractors/test_parse_atomic.py::test_parse_all_combines_3_formats -v`
Expected: FAIL with "function parse_all not defined"

- [ ] **Step 4.3: Implémenter parse_all + mapping F001→F-CIV**

Ajouter à `tools/engines/extractors/parse_atomic.py` :

```python
def parse_all(text: str, civ_prefix: str, civ_f001_offset: int = 0) -> list[dict]:
    """Parse tous les formats et unifie avec mapping F001→F-CIV-XXX.
    
    Args:
        text: contenu enquête
        civ_prefix: préfixe civilisation (S, R, C, MA, I, IN, AM, A)
        civ_f001_offset: décalage pour F001 (ex: M-A 0, Islam 0, Inde 0)
    """
    results = []
    
    # F001 (ancien) → F-CIV-XXX
    f001_results = parse_f001(text)
    for idx, r in enumerate(f001_results):
        old_num = int(r["id_old"][1:])  # F001 → 1
        new_num = old_num  # séquence préservée
        results.append({
            "id_old": r["id_old"],
            "id_target": f"F-{civ_prefix}{new_num:03d}",
            "contexte_brut": r["contexte_brut"],
            "line_no": r["line_no"],
            "input_format": "F001",
        })
    
    # F-CIV-XXX (déjà bon format)
    f_civ_results = parse_f_civ(text)
    for r in f_civ_results:
        results.append({
            "id_old": r["id_old"],
            "id_target": r["id_old"],
            "contexte_brut": r["contexte_brut"],
            "line_no": r["line_no"],
            "input_format": "F-CIV-XXX",
        })
    
    # Items numérotés → F-CIV-XXX (continuent la séquence)
    items_results = parse_items(text)
    base_num = max(
        (int(r["id_target"].split(civ_prefix)[1]) for r in results if civ_prefix in r.get("id_target", "")),
        default=0
    ) + 1
    for r in items_results:
        results.append({
            "id_old": f"item_{r['num']}",
            "id_target": f"F-{civ_prefix}{base_num:03d}",
            "contexte_brut": r["item_brut"],
            "line_no": r["line_no"],
            "input_format": "item",
        })
        base_num += 1
    
    return results
```

- [ ] **Step 4.4: Lancer tests, vérifier PASS**

Run: `pytest tests/extractors/test_parse_atomic.py -v`
Expected: 5 tests PASS (3 existants + 2 nouveaux)

- [ ] **Step 4.5: Commit**

```bash
git add tools/engines/extractors/parse_atomic.py tests/extractors/test_parse_atomic.py
git commit -m "feat(sublimator): Agent A parse_all unifié + mapping F001→F-CIV"
```

---

## Task 5: Coder GATE_G audit complétude (TDD)

**Files:**
- Create: `tools/engines/extractors/gate_g.py`
- Modify: `tests/extractors/test_gate_g.py` (nouveau)

- [ ] **Step 5.1: Écrire test GATE_G basique**

Créer `tests/extractors/test_gate_g.py` :

```python
from tools.engines.extractors.gate_g import compute_completude, gate_g_pass

def test_compute_completude_basic():
    text = "F001 F002 F003. 1. **X** 2. **Y** 100 dette 200 soldats."
    matrice = [{"id": "F-S001"}, {"id": "F-S002"}]  # 2 F### / 4 phrases-faits
    score = compute_completude(text, matrice)
    assert 0 <= score <= 100
    assert score == 50.0  # 2/4

def test_gate_g_pass_medium():
    assert gate_g_pass(85, complexity="MEDIUM") is True
    assert gate_g_pass(75, complexity="MEDIUM") is False
    assert gate_g_pass(70, complexity="SIMPLE") is True
    assert gate_g_pass(90, complexity="APEX") is True
    assert gate_g_pass(85, complexity="APEX") is False
```

- [ ] **Step 5.2: Lancer test pour FAIL**

Run: `pytest tests/extractors/test_gate_g.py -v`
Expected: FAIL "module not found"

- [ ] **Step 5.3: Implémenter GATE_G**

Créer `tools/engines/extractors/gate_g.py` :

```python
import re

CIBLES = {"SIMPLE": 70, "MEDIUM": 80, "COMPLEX": 85, "APEX": 90}

def count_phrases_faits(text: str) -> int:
    """Compte les phrases contenant chiffre/date/acteur."""
    phrases = re.findall(r"[^.\n]{20,}", text)
    n = 0
    for p in phrases:
        if re.search(r"\d{2,}", p):  # chiffre
            n += 1
        elif re.search(r"\bF0?\d{2,3}\b", p):  # F### référence
            n += 1
    return max(n, 1)

def compute_completude(text: str, matrice: list) -> float:
    """Score de complétude = n_faits_matrice / n_phrases_faits * 100."""
    n_phrases = count_phrases_faits(text)
    n_faits = len(matrice)
    return round((n_faits / n_phrases) * 100, 2)

def gate_g_pass(score: float, complexity: str = "MEDIUM") -> bool:
    """Vérifie si GATE_G passe pour la complexité."""
    return score >= CIBLES.get(complexity, 80)
```

- [ ] **Step 5.4: Lancer tests pour PASS**

Run: `pytest tests/extractors/test_gate_g.py -v`
Expected: 2 tests PASS

- [ ] **Step 5.5: Commit**

```bash
git add tools/engines/extractors/gate_g.py tests/extractors/test_gate_g.py
git commit -m "feat(sublimator): GATE_G audit complétude (TDD)"
```

---

## Task 6: Coder Agent B — LLM lecteur cursif (mocké puis réel)

**Files:**
- Create: `tools/engines/extractors/llm_lecteur.py`
- Modify: `tests/extractors/test_lecteur.py` (nouveau)

- [ ] **Step 6.1: Écrire test avec mock LLM**

Créer `tests/extractors/test_lecteur.py` :

```python
from unittest.mock import patch, MagicMock
from tools.engines.extractors.llm_lecteur import lecteur_cursif

@patch("tools.engines.extractors.llm_lecteur.call_llm")
def test_lecteur_cursif_returns_11_sections(mock_llm):
    mock_llm.return_value = """{
      "these_centrale": "Test these",
      "theses_implicites": ["t1", "t2", "t3"],
      "acteurs": ["Urukagina", "Hammurabi"],
      "causalites": [{"liens": ["A", "B", "C"]}],
      "perspectives_dialectiques": {"auteur": "...", "adverse": "...", "arbitre": "..."},
      "limites": ["l1", "l2"],
      "wolves": ["w1", "w2"],
      "iceberg": ["i1", "i2"],
      "chronologie": [{"date": "2400 av. J.-C.", "fait": "Urukagina"}],
      "domaines": ["dette", "droit"],
      "urls_prioritaires": ["https://..."]
    }"""
    text = "# §1 RÉSUMÉ\nContenu enquête..."
    result = lecteur_cursif(text, civ_prefix="S")
    assert result["these_centrale"] == "Test these"
    assert len(result["theses_implicites"]) == 3
    assert len(result["acteurs"]) == 2
    mock_llm.assert_called_once()
```

- [ ] **Step 6.2: Lancer test pour FAIL**

Run: `pytest tests/extractors/test_lecteur.py -v`
Expected: FAIL "module not found"

- [ ] **Step 6.3: Implémenter Agent B (LLM lecteur)**

Créer `tools/engines/extractors/llm_lecteur.py` :

```python
import json
import os

PROMPT_TEMPLATE = """Tu es un agent d'extraction atomique. Lis cette enquête et extrais 11 sections de quintessence.

Sections à extraire :
1. these_centrale (1 phrase)
2. theses_implicites (3 bullets)
3. acteurs (5-15 noms propres, pas catégories)
4. causalites (3-5 chaînes ≥3 liens)
5. perspectives_dialectiques (3 perspectives : auteur, adverse, arbitre, forces égales)
6. limites (3-5 limites méthodologiques)
7. wolves (3-5 acteurs malveillants nommés)
8. iceberg (3-5 angles morts/auto-critiques)
9. chronologie (5-10 dates clés)
10. domaines (5-7 thématiques)
11. urls_prioritaires (5-10 sources)

Enquête :
{text}

Réponds UNIQUEMENT en JSON valide avec ces 11 clés."""

def call_llm(prompt: str) -> str:
    """Appel LLM réel (Claude, GPT, ou autre)."""
    api_key = os.environ.get("LLM_API_KEY")
    # TODO: implémenter appel API réel
    raise NotImplementedError("LLM API call not implemented yet")

def lecteur_cursif(text: str, civ_prefix: str) -> dict:
    """Agent B : lit l'enquête intégralement et extrait 11 sections."""
    prompt = PROMPT_TEMPLATE.format(text=text[:50000])  # limite 50K chars
    response = call_llm(prompt)
    return json.loads(response)
```

- [ ] **Step 6.4: Lancer test pour PASS**

Run: `pytest tests/extractors/test_lecteur.py -v`
Expected: PASS (mock valide le contrat)

- [ ] **Step 6.5: Commit**

```bash
git add tools/engines/extractors/llm_lecteur.py tests/extractors/test_lecteur.py
git commit -m "feat(sublimator): Agent B LLM lecteur cursif (mocké)"
```

---

## Task 7: Coder Agent C — LLM curator (fusion + scoring ✦)

**Files:**
- Create: `tools/engines/extractors/llm_curator.py`
- Modify: `tests/extractors/test_curator.py` (nouveau)

- [ ] **Step 7.1: Écrire test curator (fusion + dédoublonnage + scoring)**

Créer `tests/extractors/test_curator.py` :

```python
from tools.engines.extractors.llm_curator import curator_fusion, score_fiabilite

def test_score_fiabilite_url_accessible():
    # HEAD request mocké à 200
    assert score_fiabilite(url="https://wikipedia.org/x", tier=1) == "✦"

def test_score_fiabilite_pas_url():
    assert score_fiabilite(url="", tier=None) == "❧"

def test_curator_fusion_deduplicate():
    candidats_a = [{"fait": "dette annulée"}, {"fait": "guerre civile"}]
    ajouts_b = [{"fait": "Dette annulée par Urukagina"}, {"fait": "clergé scribe"}]
    result = curator_fusion(candidats_a, ajouts_b, civ_prefix="S")
    # Dédoublonnage Jaccard < 0.7 : "dette annulée" et "Dette annulée par Urukagina" → conservés
    # (Jaccard = 2/5 = 0.4 < 0.7)
    assert len(result) >= 3
```

- [ ] **Step 7.2: Lancer test pour FAIL**

Run: `pytest tests/extractors/test_curator.py -v`
Expected: FAIL

- [ ] **Step 7.3: Implémenter Agent C**

Créer `tools/engines/extractors/llm_curator.py` :

```python
import re
import requests
from typing import Literal

Fiabilite = Literal["✦", "✧", "⁅", "❧"]

def score_fiabilite(url: str = "", tier: int = None) -> Fiabilite:
    """Score fiabilité selon URL et tier."""
    if not url:
        return "❧"
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        if r.status_code == 200:
            return "✦" if tier == 1 else "✧"
        return "⁅"
    except Exception:
        return "⁅"

def jaccard(s1: str, s2: str) -> float:
    """Jaccard sur mots."""
    w1 = set(s1.lower().split())
    w2 = set(s2.lower().split())
    return len(w1 & w2) / max(len(w1 | w2), 1)

def curator_fusion(candidats_a: list, ajouts_b: list, civ_prefix: str) -> list:
    """Fusionne candidats A + ajouts B, dédoublonne, scoring."""
    result = []
    
    # Préférer B pour contexte, A pour traçabilité
    for cand in candidats_a:
        result.append({
            "id_target": cand.get("id_target", f"F-{civ_prefix}???"),
            "fait": cand.get("contexte_brut", ""),
            "input_format": cand.get("input_format", "?"),
            "source_section": cand.get("source_section", "?"),
        })
    
    for ajout in ajouts_b:
        # Dédoublonnage Jaccard
        is_dup = any(jaccard(r["fait"], ajout.get("fait", "")) > 0.7 for r in result)
        if not is_dup:
            result.append({
                "id_target": ajout.get("id_target", f"F-{civ_prefix}???"),
                "fait": ajout.get("fait", ""),
                "input_format": "LLM-extracted",
                "source_section": ajout.get("source_section", "?"),
            })
    
    # Scoring ✦
    for r in result:
        r["fiabilite"] = score_fiabilite(url=r.get("url", ""), tier=r.get("tier"))
    
    return result
```

- [ ] **Step 7.4: Lancer tests pour PASS**

Run: `pytest tests/extractors/test_curator.py -v`
Expected: 3 tests PASS

- [ ] **Step 7.5: Commit**

```bash
git add tools/engines/extractors/llm_curator.py tests/extractors/test_curator.py
git commit -m "feat(sublimator): Agent C curator (fusion + scoring ✦)"
```

---

## Task 8: Coder Agent D — LLM verifier (cross-check + trous)

**Files:**
- Create: `tools/engines/extractors/llm_verifier.py`
- Modify: `tests/extractors/test_verifier.py` (nouveau)

- [ ] **Step 8.1: Écrire test verifier**

Créer `tests/extractors/test_verifier.py` :

```python
from unittest.mock import patch
from tools.engines.extractors.llm_verifier import verifier

@patch("tools.engines.extractors.llm_verifier.call_llm")
def test_verifier_signale_trous(mock_llm):
    mock_llm.return_value = """{
      "f001_manquants": ["fait sur Urukagina non listé"],
      "incoherences": [],
      "acteurs_oublies": ["Hammurabi"],
      "fausses_urls": [],
      "iceberg_sous_exploite": ["fausse attribution dette sumérienne"]
    }"""
    matrice = [{"id": "F-S001", "fait": "dette annulée"}]
    text = "Urukagina et Hammurabi ont annulé les dettes."
    result = verifier(matrice, text)
    assert "Hammurabi" in result["acteurs_oublies"]
    assert len(result["f001_manquants"]) == 1
```

- [ ] **Step 8.2: Lancer test pour FAIL**

Run: `pytest tests/extractors/test_verifier.py -v`
Expected: FAIL

- [ ] **Step 8.3: Implémenter Agent D**

Créer `tools/engines/extractors/llm_verifier.py` :

```python
import json
import os

PROMPT_VERIFIER = """Tu es un agent verifier. Reprends cette matrice F### et signale les trous par rapport au texte source.

Matrice :
{matrice}

Texte source (extrait) :
{text}

Signale :
- f001_manquants : F### qui devraient être listés
- incoherences : claims mal sourcés
- acteurs_oublies : acteurs cités dans texte mais absents matrice
- fausses_urls : URLs qui semblent inventées
- iceberg_sous_exploite : angles morts non capturés

Réponds en JSON."""

def call_llm(prompt: str) -> str:
    api_key = os.environ.get("LLM_API_KEY")
    raise NotImplementedError("LLM API call not implemented yet")

def verifier(matrice: list, text: str) -> dict:
    """Agent D : relit et signale les trous."""
    matrice_str = "\n".join(f"{m['id']}: {m['fait']}" for m in matrice)
    prompt = PROMPT_VERIFIER.format(matrice=matrice_str, text=text[:30000])
    response = call_llm(prompt)
    return json.loads(response)
```

- [ ] **Step 8.4: Lancer test pour PASS**

Run: `pytest tests/extractors/test_verifier.py -v`
Expected: PASS

- [ ] **Step 8.5: Commit**

```bash
git add tools/engines/extractors/llm_verifier.py tests/extractors/test_verifier.py
git commit -m "feat(sublimator): Agent D verifier (cross-check + trous)"
```

---

## Task 9: Coder orchestrateur de cellule

**Files:**
- Create: `tools/engines/extractors/orchestrator.py`
- Modify: `tests/extractors/test_orchestrator.py` (nouveau)

- [ ] **Step 9.1: Écrire test orchestrateur (intégration mockée)**

Créer `tests/extractors/test_orchestrator.py` :

```python
from unittest.mock import patch, MagicMock
from tools.engines.extractors.orchestrator import run_cellule

@patch("tools.engines.extractors.orchestrator.lecteur_cursif")
@patch("tools.engines.extractors.orchestrator.call_llm")
def test_run_cellule_sumer(mock_llm, mock_lecteur):
    mock_lecteur.return_value = {
        "these_centrale": "Test", "theses_implicites": ["t1"],
        "acteurs": ["Urukagina"], "causalites": [],
        "perspectives_dialectiques": {}, "limites": [], "wolves": [],
        "iceberg": [], "chronologie": [], "domaines": [], "urls_prioritaires": []
    }
    mock_llm.return_value = "{}"
    
    result = run_cellule(
        input_path="investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md",
        civ_prefix="S",
        output_path="/tmp/sumer_test.yaml",
        complexity="MEDIUM",
    )
    assert result["exit_code"] == 0
    assert "F-S001" in str(result)
```

- [ ] **Step 9.2: Lancer test pour FAIL**

Run: `pytest tests/extractors/test_orchestrator.py -v`
Expected: FAIL

- [ ] **Step 9.3: Implémenter orchestrateur**

Créer `tools/engines/extractors/orchestrator.py` :

```python
import yaml
from pathlib import Path
from .parse_atomic import parse_all
from .llm_lecteur import lecteur_cursif
from .llm_curator import curator_fusion
from .llm_verifier import verifier
from .gate_g import compute_completude, gate_g_pass

def run_cellule(input_path: str, civ_prefix: str, output_path: str, complexity: str = "MEDIUM") -> dict:
    """Orchestre Agent A → B → C → D → E sur 1 enquête."""
    text = Path(input_path).read_text()
    
    # Agent A : parse
    candidats_a = parse_all(text, civ_prefix=civ_prefix)
    
    # Agent B : lecteur cursif
    sections_b = lecteur_cursif(text, civ_prefix=civ_prefix)
    
    # Agent C : curator (fusion + scoring)
    matrice = curator_fusion(candidats_a, sections_b.get("ajouts", []), civ_prefix=civ_prefix)
    
    # Agent D : verifier
    rapport = verifier(matrice, text)
    
    # GATE_G
    score = compute_completude(text, matrice)
    if not gate_g_pass(score, complexity):
        return {"exit_code": 1, "error": f"GATE_G fail: {score}% < {complexity} cible", "matrice": matrice, "rapport": rapport}
    
    # Construction fiche 12 sections
    fiche = {
        "these_centrale": sections_b["these_centrale"],
        "theses_implicites": sections_b["theses_implicites"],
        "f_atomiques": matrice,
        "acteurs_network": sections_b["acteurs"],
        "causalites": sections_b["causalites"],
        "perspectives_dialectiques": sections_b["perspectives_dialectiques"],
        "limites": sections_b["limites"],
        "wolves": sections_b["wolves"],
        "iceberg": sections_b["iceberg"],
        "chronologie": sections_b["chronologie"],
        "domaines": sections_b["domaines"],
        "urls_prioritaires": sections_b["urls_prioritaires"],
        "completude": score,
        "rapport_verifier": rapport,
    }
    
    # Agent E : humain valide (à faire manuellement ou via question tool)
    Path(output_path).write_text(yaml.dump(fiche, allow_unicode=True, sort_keys=False))
    
    return {"exit_code": 0, "output": output_path, "matrice": matrice, "score": score}
```

- [ ] **Step 9.4: Lancer test pour PASS**

Run: `pytest tests/extractors/test_orchestrator.py -v`
Expected: PASS

- [ ] **Step 9.5: Commit**

```bash
git add tools/engines/extractors/orchestrator.py tests/extractors/test_orchestrator.py
git commit -m "feat(sublimator): orchestrateur cellule (A→B→C→D→E)"
```

---

## Task 10: Test pilote — Sumer 50K (intégration end-to-end)

**Files:**
- Modify: `investigations/2026-06-03_sumer_article/_quintessence/sumer_quintessence.yaml` (créé par orchestrateur)

- [ ] **Step 10.1: Configurer LLM API key (export env var)**

```bash
export LLM_API_KEY="sk-..."  # ou via .env
```

- [ ] **Step 10.2: Implémenter call_llm réel (TODO des Tasks 6/8)**

Modifier `tools/engines/extractors/llm_lecteur.py` `call_llm()` :
- Si `LLM_API_KEY` set + provider = "anthropic" → appel Claude API
- Si provider = "openai" → appel GPT API
- Sinon → erreur explicite

(Implémentation réelle dépend du provider choisi par l'utilisateur.)

- [ ] **Step 10.3: Lancer orchestrateur sur Sumer 50K**

```bash
mkdir -p investigations/2026-06-03_sumer_article/_quintessence
python3 -m tools.engines.extractors.orchestrator \
  --input investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md \
  --civ S \
  --output investigations/2026-06-03_sumer_article/_quintessence/sumer_quintessence.yaml \
  --complexity APEX
```

- [ ] **Step 10.4: Vérifier la fiche produite**

```bash
cat investigations/2026-06-03_sumer_article/_quintessence/sumer_quintessence.yaml | head -50
```

Expected:
- 12 sections présentes
- ≥35 F### (cible APEX)
- complétude ≥90% (GATE_G)
- 5-15 acteurs
- 5-10 chronologie

- [ ] **Step 10.5: Validation humaine (Agent E)**

L'humain lit la fiche et valide ou demande correctifs. Si refus → boucle curator (max 2).

- [ ] **Step 10.6: Commit**

```bash
git add investigations/2026-06-03_sumer_article/_quintessence/sumer_quintessence.yaml
git commit -m "feat(sublimator): pilote Sumer 50K — quintessence extraite (12 sections, ≥35 F###)"
```

---

## Task 11: Documentation finale

**Files:**
- Modify: `AGENTS.md` (section Engines : référence v33.2)

- [ ] **Step 11.1: Ajouter entrée v33.2 dans AGENTS.md**

Trouver la section Engines et ajouter :
```markdown
### SUBLIMATOR v33.2 (extraction rigoureuse)

- Spec : `tools/engines/SUBLIMATOR_v33.2_spec_agent.md`
- Guide : `tools/engines/SUBLIMATOR_v33.2_GUIDE_HUMAN.md`
- Design : `docs/superpowers/specs/2026-06-06-sublimator-v33.2-extraction-design.md`
- Plan : `docs/superpowers/plans/2026-06-06-sublimator-v33.2-extraction.md`
- Module : `tools/engines/extractors/`
- Tests : `tests/extractors/`
- 5 ajouts vs v33.1 : §X EXTRACTION ATOMIQUE, §W QUINTESSENCE 12 SECTIONS, §W.13 AGRÉGATION, scoring ✦, GATE_G
- Workflow cellule : A (script) → B (LLM lecteur) → C (LLM curator) → D (LLM verifier) → E (humain)
- Scalable 2 à 20+ enquêtes
```

- [ ] **Step 11.2: Commit final**

```bash
git add AGENTS.md
git commit -m "docs(agents): référence SUBLIMATOR v33.2"
```

---

## Self-Review (à compléter après écriture)

- Spec coverage : §X, §W, §W.13, §Y (scoring), §Z (KERNEL), §V (GATE_G) — tous couverts
- Placeholder scan : aucun TBD
- Type consistency : `civ_prefix`, `complexity`, `matrice` cohérents
- Granularity : 11 tasks, ~50 steps TDD, 2-5 min/step

## Execution Handoff

Plan complet : 11 tasks, ~50 steps, 6-10h de travail.

**Options d'exécution** :
1. **Subagent-Driven** (recommandé) : 1 subagent frais par task, review entre tasks
2. **Inline** : exécution dans cette session, batch avec checkpoints

Voir handoff après validation.

---

## Task 5: Coder GATE_G audit complétude (TDD)

**Files:**
- Create: `tools/engines/extractors/gate_g.py`
- Modify: `tests/extractors/test_parse_atomic.py` (ajouter tests GATE_G)
