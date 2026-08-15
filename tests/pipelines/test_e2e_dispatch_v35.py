# -*- coding: utf-8 -*-
"""
test_e2e_dispatch_v35.py

Tests statiques de coherence du dispatch Sublimator v35.

Verifie (sans mock runtime, sans appel LLM) :
- prompt-v35.md §Orchestration reference les 4 sub-prompts (LECTEUR, EXTRACTEUR, CRITIQUE, ORCHESTRATEUR)
- les 4 fichiers sub-prompts existent physiquement
- chaque sub-prompt contient le contrat Mnemolite : get_system_snapshot + search_mode="hybrid" + cardex fallback
- prompt-v35.md contient HALTE/cardex
- quintessence_extractor.md contient la regle VERBATIM (re.search)
- quintessence_orchestrator.md borne la boucle a 3 iterations

Resout AUDIT_ANTAGONISTE_v35 V14 (« aucun test E2E dispatching »).

Coût : 0 token LLM, stdlib only (pathlib + re), execution <100ms.

Note 2026-07-05 : tests `test_cartographie_*` et `test_phase_0_no_duplicate_step_4`
SUPPRIMES (Phase 0 eliminee — voir git log).

Note 2026-08-15 : tests `test_validators_python_exist` et
`test_m9_enforces_isolation_tag_in_quintessence` SUPPRIMES — validateurs Python
(`sublimator_validate.py` / `sublimator_retry.py`) abandonnes (cf. ARCHITECTURE.md,
« Validation algorithmique Python retiree 2026-07-06 »). La section « Validateurs »
du README a ete retiree en consequence.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SUB = ROOT / "tools" / "engines" / "sublimator"
PROMPT_V35 = SUB / "prompt-v35.md"
SUB_PROMPTS = SUB / "prompts"

REQUIRED_SUB_PROMPTS = (
    ("quintessence_reader.md",       "LECTEUR",       "13.3.1"),
    ("quintessence_extractor.md",    "EXTRACTEUR",    "13.3.2"),
    ("quintessence_critic.md",       "CRITIQUE",      "13.3.3"),
    ("quintessence_orchestrator.md", "ORCHESTRATEUR", "13.3.4"),
)

MNEMOLITE_REQUIRED_FRAGMENTS = (
    "get_system_snapshot",
    'search_mode="hybrid"',
    "cardex",
)


def _read(p):
    return p.read_text(encoding="utf-8")


# 1. prompt-v35.md §Orchestration reference les 4 sub-prompts

def test_prompt_v35_dispatch_table_lists_4_sub_agents():
    text = _read(PROMPT_V35)
    m = re.search(r"^## Orchestration Sublimator.+?(?=^## |\Z)", text, re.S | re.M)
    assert m is not None, "Section ## Orchestration Sublimator absente de prompt-v35.md"
    section = m.group(0)
    for fname, label, ref in REQUIRED_SUB_PROMPTS:
        assert fname in section, (
            f"prompt-v35.md Orchestration ne référence pas {fname} "
            f"(label={label}, ref attendu=§{ref})"
        )


# 2. Chaque fichier sub-prompt existe

def test_each_sub_prompt_file_exists():
    for fname, label, ref in REQUIRED_SUB_PROMPTS:
        p = SUB_PROMPTS / fname
        assert p.exists(), f"Fichier sub-prompt manquant : {p} (label={label}, §{ref})"


# 3. Chaque sub-prompt contient le contrat Mnemolite (V12/V13)

def test_each_sub_prompt_has_mnemolite_contract():
    for fname, label, ref in REQUIRED_SUB_PROMPTS:
        text = _read(SUB_PROMPTS / fname)
        for frag in MNEMOLITE_REQUIRED_FRAGMENTS:
            assert frag in text, (
                f"{fname} ne contient pas le fragment '{frag}' "
                f"(label={label}, §{ref}, contrat Mnemolite incomplet)"
            )


# 4. EXTRACTEUR : regle VERBATIM + re.search documente

def test_extractor_has_verbatim_rule():
    text = _read(SUB_PROMPTS / "quintessence_extractor.md")
    assert "VERBATIM" in text, "Extractor : regle VERBATIM absente"
    assert "re.search" in text, "Extractor : re.search non documente"


# 5. ORCHESTRATEUR : boucle max 3 iterations

def test_orchestrator_max_3_iterations():
    text = _read(SUB_PROMPTS / "quintessence_orchestrator.md")
    assert (
        "iteration < 3" in text or "max 3" in text or "3 iterations" in text
    ), "Orchestrator : borne max 3 iterations non explicite"


# 6. V16 tracking iterations materialise

def test_v16_iteration_count_in_orchestrator_and_prompt_v35():
    orch = _read(SUB_PROMPTS / "quintessence_orchestrator.md")
    v35 = _read(PROMPT_V35)
    assert "iteration_count" in orch, (
        "Orchestrator : champ iteration_count absent (V16 non applique)"
    )
    assert "iteration_count" in v35, (
        "prompt-v35.md : champ iteration_count absent (V16 non propage)"
    )


# 7. prompt-v35.md contient HALTE + cardex (V11)

def test_prompt_v35_halte_cardex_contract():
    text = _read(PROMPT_V35)
    assert "cardex local" in text or "cardex" in text, (
        "prompt-v35.md : cardex local non documente"
    )
    assert "HALTE" in text, "prompt-v35.md : pas de HALTE explicite"


# 8. README existe (V15)

def test_sublimator_readme_exists():
    readme = SUB / "README.md"
    assert readme.exists(), "tools/engines/sublimator/README.md manquant (V15)"
    text = _read(readme)
    for section in ("Quickstart", "Architecture", "Workflow", "Prompts", "épanna"):
        assert section in text, f"README.md : section '{section}' absente"
