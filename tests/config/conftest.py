"""
Shared fixtures for configuration tests.

Provides:
- env_var_scan: Scans api/ and workers/ for all os.getenv / os.environ calls
- env_example_doc: Parses .env.example to extract documented env vars
- settings_defaults: Extracts all default values from AppSettings
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, Set, Tuple

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Return the absolute project root path."""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def env_vars_in_code(project_root: Path) -> Dict[str, Set[str]]:
    """
    Scan api/ and workers/ for ALL env var accesses.

    Returns a dict:
        "os_getenv": set of env var names from os.getenv("VAR", ...)
        "os_environ_get": set of env var names from os.environ.get("VAR", ...)
        "os_environ_direct": set of env var names from os.environ["VAR"]
        "settings_fields": set of env var names from AppSettings fields
    """
    result = {
        "os_getenv": set(),
        "os_environ_get": set(),
        "os_environ_direct": set(),
        "settings_fields": set(),
    }

    source_dirs = [
        project_root / "api",
        project_root / "workers",
    ]

    # Patterns for finding env var names in string literals
    getenv_pattern = re.compile(r'os\.getenv\s*\(\s*["\']([A-Z_]+)["\']')
    environ_get_pattern = re.compile(r'os\.environ\.get\s*\(\s*["\']([A-Z_]+)["\']')
    environ_direct_pattern = re.compile(r'os\.environ\s*\[\s*["\']([A-Z_]+)["\']')

    for src_dir in source_dirs:
        if not src_dir.exists():
            continue
        for pyfile in src_dir.rglob("*.py"):
            if "node_modules" in str(pyfile) or "__pycache__" in str(pyfile):
                continue
            try:
                text = pyfile.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            for match in getenv_pattern.finditer(text):
                result["os_getenv"].add(match.group(1))
            for match in environ_get_pattern.finditer(text):
                result["os_environ_get"].add(match.group(1))
            for match in environ_direct_pattern.finditer(text):
                result["os_environ_direct"].add(match.group(1))

    # Also scan AppSettings fields (they're env vars even if read via Pydantic)
    settings_file = project_root / "api" / "core" / "settings.py"
    if settings_file.exists():
        try:
            tree = ast.parse(settings_file.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == "AppSettings":
                    for item in node.body:
                        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                            name = item.target.id
                            if name.isupper():  # Only uppercase = env var
                                result["settings_fields"].add(name)
        except Exception:
            pass

    return result


@pytest.fixture(scope="session")
def env_example_doc(project_root: Path) -> Dict[str, str]:
    """
    Parse .env.example to extract documented env vars and their defaults.

    Returns dict mapping VAR_NAME -> default_value (or "" if just documented).
    """
    env_path = project_root / ".env.example"
    documented = {}
    if not env_path.exists():
        return documented

    text = env_path.read_text()
    var_pattern = re.compile(r"^#?\s*([A-Z][A-Z_0-9]+)\s*=\s*(.*?)(?:\s+#.*)?$", re.MULTILINE)

    for match in var_pattern.finditer(text):
        name = match.group(1)
        # Exclude Makefile-like vars
        if not name.startswith("VITE_"):
            documented[name] = match.group(2).strip()

    return documented


@pytest.fixture(scope="session")
def docker_compose_env(project_root: Path) -> Set[str]:
    """
    Parse docker-compose.yml to extract env vars passed to containers.
    """
    dc_path = project_root / "docker-compose.yml"
    env_vars = set()
    if not dc_path.exists():
        return env_vars

    text = dc_path.read_text()
    var_pattern = re.compile(r"\$\{?([A-Z][A-Z_0-9]+)\}?", re.MULTILINE)

    for match in var_pattern.finditer(text):
        name = match.group(1)
        # Filter out non-env-var patterns
        if name not in ("HOME", "PWD", "UID", "GID", "PATH", "SHELL", "USER"):
            env_vars.add(name)

    return env_vars
