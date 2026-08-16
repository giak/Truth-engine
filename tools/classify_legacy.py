#!/usr/bin/env python3
"""classify_legacy.py — Réconcilie le corpus legacy `livre-cst` avec FACT_VERIFICATION §11.

Lit un enregistrement legacy (contenu markdown structuré produit par
`book/book/audit-apex-v8/archive/index_csv_to_mnemolite.py`) et mappe ses champs
`Statut canonique` / `Classe source` vers les termes FACT_VERIFICATION
(verdict, tag status, EPI, famille).

Déterministe : parse les CHAMPS STRUCTURÉS (`**Statut canonique** : ...`,
`**Classe source** : ...`), jamais la prose libre. Ne juge pas la vérité :
il applique la table de mapping §11.2/§11.3 (AGENTS.md §4).

Usage :
  python3 tools/classify_legacy.py [--json] <fichier.md...>
  # contenu via stdin :
  echo "$CONTENT" | python3 tools/classify_legacy.py --stdin [--json]

Sortie : une ligne par enregistrement — « id | verdict | status | epi | famille | action »
(ou JSON si --json). Exit 0 (traité) / 2 (aucun enregistrement lisible).
"""

import json
import re
import sys
from pathlib import Path

# bootstrap sys.path pour exécution directe (tools est un namespace package)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Labels structurés émis par index_csv_to_mnemolite.py
_RE_STATUS = re.compile(r"\*\*Statut canonique\*\*\s*:\s*(.+)")
_RE_SOURCE_CLASS = re.compile(r"\*\*Classe source\*\*\s*:\s*(.+)")
_RE_SOURCE = re.compile(r"\*\*Source\*\*\s*:\s*(.+)")
_RE_CLAIM = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def _clean(value):
    return value.strip().rstrip()


def map_status(canonical):
    """Statut canonique legacy → (verdict, status_tag, epi, action)."""
    c = _clean(canonical or "")
    key = c.split()[0] if c else ""
    if key.startswith("C1"):
        return ("CANDIDAT", None, None, "re-fetch -> L0->L4")
    if key.startswith("C2"):
        return ("CANDIDAT", None, None, "re-fetch + fixer le perimetre")
    if key.startswith("C3"):
        return ("HYPOTHESIS", None, "HYPOTHESIS", "lifecycle_state=doubt")
    if key.startswith("C4"):
        return ("UNKNOWN", None, "UNKNOWN", "pas de write")
    if key.startswith("C5"):
        return ("REFUTE", "REFUTE", "FACT", "citable uniquement comme faux")
    if key.startswith("C6"):
        return ("UNKNOWN", None, "UNKNOWN", "pas de write, log GAP")
    if key.startswith("WEB"):
        return ("CANDIDAT", None, None, "arbitrer -> re-fetch")
    if key.startswith("ENFANCE") or key.startswith("LOOP"):
        return ("CANDIDAT", None, None, "arbitrer -> re-fetch")
    return ("UNKNOWN", None, "UNKNOWN", "statut legacy inconnu")


def map_family(source_class):
    """Classe source legacy → famille FACT_VERIFICATION."""
    sc = _clean(source_class or "")
    key = sc.split()[0] if sc else ""
    if key.startswith("S0"):
        return None          # aucune source
    if key.startswith("S1"):
        return "INTERNE"     # registre interne : non indépendant
    if key.startswith("S2"):
        return "SECONDAIRE"  # C/D/E selon l'émetteur
    if key.startswith("S3"):
        return "A"           # primaire / officiel
    return None


def classify(content):
    """Mappe un contenu legacy markdown en dict FACT_VERIFICATION."""
    status = _RE_STATUS.search(content or "")
    source_class = _RE_SOURCE_CLASS.search(content or "")
    source = _RE_SOURCE.search(content or "")
    claim = _RE_CLAIM.search(content or "")

    verdict, status_tag, epi, action = map_status(status.group(1) if status else "")
    famille = map_family(source_class.group(1) if source_class else "")

    return {
        "claim_id": claim.group(1).strip() if claim else None,
        "legacy_status": _clean(status.group(1)) if status else None,
        "legacy_source_class": _clean(source_class.group(1)) if source_class else None,
        "claimed_source": _clean(source.group(1)) if source else None,
        "verdict": verdict,
        "status_tag": status_tag,
        "epi": epi,
        "famille": famille,
        "action": action,
    }


def render(rec, as_json):
    if as_json:
        return json.dumps(rec, ensure_ascii=False)
    return " | ".join(
        str(rec.get(k) or "-")
        for k in ("claim_id", "verdict", "status_tag", "epi", "famille", "action")
    )


def main(argv):
    as_json = "--json" in argv
    use_stdin = "--stdin" in argv
    files = [a for a in argv if not a.startswith("--")]

    contents = []
    if use_stdin or not files:
        contents.append(("stdin", sys.stdin.read()))
    for path in files:
        contents.append((path, Path(path).read_text(encoding="utf-8")))

    emitted = 0
    for name, text in contents:
        rec = classify(text)
        if rec["legacy_status"] is None and rec["legacy_source_class"] is None:
            continue
        print(render(rec, as_json))
        emitted += 1

    return 0 if emitted else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
