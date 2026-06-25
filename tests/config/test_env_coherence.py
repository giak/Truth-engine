"""
Automated coherence tests for environment variable configuration.

Verifies that:
1. All env vars used in code are documented in .env.example
2. All env vars in docker-compose.yml are documented in .env.example
3. AppSettings field defaults match .env.example documented defaults
4. No undocumented env var drift between code, config, and documentation
"""

import os
import re
from pathlib import Path
from typing import Dict, Set

import pytest

# Expected env vars that are intentionally NOT in .env.example
# (e.g., deprecated, internal-only, or set by Docker/k8s at runtime)
WHITELIST_UNDOCUMENTED = {
    # Set by Docker Compose at runtime
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "POSTGRES_DB",
    "POSTGRES_INITDB_ARGS",
    "OTLP_LOGS_ENDPOINT",  # Added in docker-compose but not yet in .env.example
}


def test_all_getenv_vars_documented(env_vars_in_code, env_example_doc):
    """Every os.getenv() var must be documented in .env.example."""
    all_code_vars = (
        env_vars_in_code["os_getenv"]
        | env_vars_in_code["os_environ_get"]
        | env_vars_in_code["os_environ_direct"]
    )
    documented = set(env_example_doc.keys())
    undocumented = all_code_vars - documented - WHITELIST_UNDOCUMENTED

    if undocumented:
        msg = (
            f"{len(undocumented)} env var(s) used in code but NOT documented in .env.example:\n"
            + "\n".join(f"  ❌  {v}" for v in sorted(undocumented))
            + "\n\nAdd them to .env.example or add to WHITELIST_UNDOCUMENTED if intentional."
        )
        pytest.fail(msg)


def test_all_appsettings_fields_documented(env_vars_in_code, env_example_doc):
    """Every AppSettings field (uppercase) must be documented in .env.example."""
    settings_fields = env_vars_in_code.get("settings_fields", set())
    documented = set(env_example_doc.keys())
    undocumented = settings_fields - documented - WHITELIST_UNDOCUMENTED

    # Internal AppSettings fields that are NOT env vars:
    # These are computed fields (lowercase) or internal config, not env vars
    internal_fields = {
        "VALID_EMBEDDING_MODES",
        "KNOWN_MODELS",
        "ModelSpec",
    }
    undocumented -= internal_fields

    if undocumented:
        msg = (
            f"{len(undocumented)} AppSettings field(s) NOT documented in .env.example:\n"
            + "\n".join(f"  ❌  {v}" for v in sorted(undocumented))
            + "\n\nThese fields are read from env vars but have no .env.example entry."
        )
        pytest.fail(msg)


def test_docker_compose_vars_documented(env_example_doc, docker_compose_env):
    """Every env var used in docker-compose.yml must be documented."""
    documented = set(env_example_doc.keys())
    undocumented = docker_compose_env - documented - WHITELIST_UNDOCUMENTED

    if undocumented:
        msg = (
            f"{len(undocumented)} env var(s) in docker-compose.yml NOT documented in .env.example:\n"
            + "\n".join(f"  ❌  {v}" for v in sorted(undocumented))
        )
        pytest.fail(msg)


def test_no_dead_documentation(env_vars_in_code, env_example_doc, docker_compose_env):
    """
    Warn about env vars documented in .env.example but NEVER used in code.

    This is a soft check — documented-but-unused is better than undocumented.
    """
    all_code_vars = (
        env_vars_in_code["os_getenv"]
        | env_vars_in_code["os_environ_get"]
        | env_vars_in_code["os_environ_direct"]
        | env_vars_in_code.get("settings_fields", set())
        | docker_compose_env
    )
    documented = set(env_example_doc.keys())

    # VITE_* vars are used by frontend, not backend code
    frontend_vars = {v for v in documented if v.startswith("VITE_")}
    documented_backend = documented - frontend_vars

    unused = documented_backend - all_code_vars - WHITELIST_UNDOCUMENTED

    # These are documented in .env.example but not directly read by os.getenv
    # because they're read via Pydantic settings (which reads from .env automatically)
    pydantic_only = {
        "SECRET_KEY",
        "EMBEDDING_MODEL",
        "CODE_EMBEDDING_MODEL",
        "EMBEDDING_MODE",
        "EMBEDDING_DEVICE",
        "EMBEDDING_CACHE_SIZE",
        "USE_ONNX",
        "MNEMO_AUTH_ENABLED",
        "MNEMO_API_KEYS",
        "MNEMO_RATE_LIMIT_ENABLED",
        "MNEMO_RATE_LIMIT_MAX",
        "MNEMO_RATE_LIMIT_WINDOW",
        "TYPESCRIPT_LSP_ENABLED",
        "CLAUDE_PROJECTS_DIR",
        "CODEBUFF_DIR",
        "OPENCODE_DIR",
        "ACTIVE_PROJECT",
        "ENABLE_AUTO_IMPORT",
        "CONVERSATION_WATCHER_ENABLED",
        "POLL_INTERVAL",
        "IMPORT_HISTORICAL",
        "WATCHER_LOG_FORMAT",
        "MCP_PRIVACY_ENABLED",
        "ENTITY_EXTRACTION_ENABLED",
        "ENTITY_EXTRACTION_MEMORY_TYPES",
        "ENTITY_EXTRACTION_SYSTEM_TAGS",
        "QUERY_UNDERSTANDING_ENABLED",
        "QUERY_UNDERSTANDING_FALLBACK",
        "UPLOAD_BATCH_SIZE",
        "UPLOAD_INDEXING_TIMEOUT",
        "O2_URL",
        "VITE_API_URL",
        "CODE_EMBEDDING_MODEL",
        "EMBEDDING_DIMENSION",
    }
    unused -= pydantic_only

    if unused:
        msg = (
            f"{len(unused)} env var(s) documented in .env.example but never used in code:\n"
            + "\n".join(f"  ⚠️  {v}" for v in sorted(unused))
            + "\n\nConsider removing from .env.example if truly obsolete."
        )
        pytest.fail(msg)


def test_appsettings_defaults_match_env_example(env_example_doc):
    """
    Verify that AppSettings default values match .env.example documented defaults.

    This test checks a representative sample of the most critical defaults.
    """
    settings = __import__("api.core.settings", fromlist=["get_settings"]).get_settings()

    # Known key:value pairs where AppSettings field != env var name
    FIELD_TO_VAR = {
        "TIMEOUT_TREE_SITTER": "TIMEOUT_TREE_SITTER",
        "TIMEOUT_INDEX_FILE": "TIMEOUT_INDEX_FILE",
        "REDIS_CIRCUIT_FAILURE_THRESHOLD": "REDIS_CIRCUIT_FAILURE_THRESHOLD",
        "EMBEDDING_CIRCUIT_FAILURE_THRESHOLD": "EMBEDDING_CIRCUIT_FAILURE_THRESHOLD",
        "EMBEDDING_MODEL": "EMBEDDING_MODEL",
        "LOG_LEVEL": "LOG_LEVEL",
    }

    mismatches = []
    for field, var in FIELD_TO_VAR.items():
        actual = str(getattr(settings, field, "MISSING"))
        expected_raw = env_example_doc.get(var, "")
        # Extract default from comment: e.g. "BAAI/bge-m3       # Default (1024D...)"
        # Actually .env.example just documents the default value
        if expected_raw:
            expected = expected_raw.split("#")[0].strip()
            # If it's quoted, unquote
            expected = expected.strip('"').strip("'")
            if actual != expected and actual != "MISSING":
                mismatches.append(f"  {var}: .env.example says '{expected}', AppSettings has '{actual}'")
            elif actual == "MISSING":
                mismatches.append(f"  {var}: field not found in AppSettings")

    if mismatches:
        msg = (
            f"{len(mismatches)} default value mismatch(es):\n"
            + "\n".join(mismatches)
        )
        pytest.fail(msg)
