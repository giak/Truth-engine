from pathlib import Path
import tempfile
from tools.engines.sublimator.extractors.orchestrator import run_cellule


def test_run_cellule_sumer_creates_yaml():
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as f:
        output_path = f.name
    try:
        result = run_cellule(
            input_path="investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md",
            civ_prefix="S",
            output_path=output_path,
            complexity="MEDIUM",
        )
        assert "exit_code" in result
        assert "matrice" in result
        assert "score" in result
        assert "prompt_hote" in result
        assert "PROMPT STRUCTURÉ" in result["prompt_hote"]
        # Le fichier YAML doit exister et contenir les sections
        assert Path(output_path).exists()
        content = Path(output_path).read_text()
        assert "civ_prefix: S" in content
        assert "f_atomiques" in content
        assert "prompt_hote" in content
    finally:
        Path(output_path).unlink(missing_ok=True)


def test_run_cellule_prompt_contains_12_sections():
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as f:
        output_path = f.name
    try:
        result = run_cellule(
            input_path="investigations/2026-06-03_sumer_article/2026-06-03_12-30_sumer_vs_france_INVESTIGATION.md",
            civ_prefix="S",
            output_path=output_path,
            complexity="MEDIUM",
        )
        prompt = result["prompt_hote"]
        for section in [
            "these_centrale", "theses_implicites", "f_atomiques",
            "acteurs_network", "causalites", "perspectives_dialectiques",
            "limites", "wolves", "iceberg", "chronologie",
            "domaines", "urls_prioritaires",
        ]:
            assert section in prompt, f"Section {section} manquante du prompt"
    finally:
        Path(output_path).unlink(missing_ok=True)
