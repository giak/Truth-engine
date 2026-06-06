"""Pilote Sumer 50K — intégration end-to-end.

Sans LLM API, valide uniquement Agent A (parse_all). Agent B lève
NotImplementedError — comportement attendu et documenté.
"""
import json
from pathlib import Path
from tools.engines.sublimator.extractors.parse_atomic import parse_all
from tools.engines.sublimator.extractors.gate_g import compute_completude, gate_g_pass

INPUT = "investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md"
OUTPUT = "/tmp/sumer_agent_a_output.json"


def main():
    text = Path(INPUT).read_text()
    candidats = parse_all(text, civ_prefix="S")
    score = compute_completude(text, candidats)
    gate_ok = gate_g_pass(score, "APEX")

    result = {
        "input": INPUT,
        "n_candidats": len(candidats),
        "completude_pct": score,
        "gate_g_apex_pass": gate_ok,
        "first_5": candidats[:5],
    }
    Path(OUTPUT).write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"OK: {len(candidats)} candidats, complétude={score}%, GATE_G(APEX)={gate_ok}")
    print(f"→ {OUTPUT}")


if __name__ == "__main__":
    main()
