"""
Audit automatisé Phase 1 Sublimator (prompt-v35.md) sur n=42 quintessences.

Périmètre : investigations/2026-07-04-RIC/_quintessence/
Méthodologie : 6 critères objectifs automatisables (C1, C2, C5, C6, C7, C10) +
  C3 NEUTRALISÉ (cf. note scope ci-dessous) +
  Delta Source-Quintessence (v2026-07-08, contrôle d'intégrité F-##, informatif).
Critères subjectifs C4 (Refus Phase 1), C8 (Fidélité citations), C9 (Pas de jugement)
conservés en audit manuel échantillonné (cf. audit n=6).

Note scope C3 (zéro em-dash) :
- Doctrine originelle (knowledge.md) : « zéro em-dash dans les articles » (Phase 3).
- C3 auditait les QUINTESSENCES (Phase 1) en réalité : sur-application.
- Fiches internes (quintessence Phase 1, INVESTIGATIONS) tolèrent l'em-dash.
- 2026-07-08 : C3 retiré du score final. Le champ `n_em_dash` reste tracké
  dans FileAudit (informatif) mais n'influence plus le verdict.
- Pour audit Phase 3 (articles publiés) : créer audit_phase3_em_dash.py séparé.

Delta Source-Quintessence (v2026-07-08) :
- Compare l'ensemble des F-## source vs quintessence (avec normalisation F-PNR30 ≡ F-PNR-30).
- ❌ si fabrication détectée (F-## dans quintessence absents de la source).
- ⚠️ si manquants (F-## dans source non repris dans quintessence).
- ✅ si delta vide.
- ? si source non trouvée / champ `Source :` absent.
- Informatif (hors score strict/lenient, comme C3).
- Bug latent corrigé : l'ancien C2 = existence check ne détectait pas les fabrications
  (cas sol_dem : 0 F-## source → 16 F-## quintessence, passé 5.5/6 strict).

Sortie : JSON (intégration CI) + Markdown (lecture humaine).

Usage :
    python3 tools/audit_phase1_sublimator_v35.py json
    python3 tools/audit_phase1_sublimator_v35.py markdown
    python3 tools/audit_phase1_sublimator_v35.py full
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

# 9 noms H2 canoniques (extraits verbatim de prompt-v35.md)
CANONICAL_H2 = [
    "1. Métadonnées & trace source",
    "2. Faits atomiques préservés",
    "3. Acteurs nominaux",
    "4. Sources externes citées",
    "5. Chronologie datée",
    "6. Mécanismes / chaînes causales",
    "7. Verbatim et citations",
    "8. Notes méthodologiques source",
    "9. Limites connues (case-limites)",
]

# Variantes acceptées pour §9 (toutes vues dans le corpus)
SECTION_9_VARIANTS = [
    "9. Limites connues (case-limites)",
    "9. Limites (case-limites)",
    "9. Limites (de cette extraction)",
    "9. Limites (de cette extraction (case-limites))",
    "9. Limites connues de cette extraction (case-limites)",
]

EM_DASH_BYTES = b"\xe2\x80\x94"

DEFAULT_QUINTESSENCE_DIR = Path("investigations/2026-07-04-RIC/_quintessence")


@dataclass
class FileAudit:
    """Résultat d'audit d'un fichier quintessence."""

    file: str
    canonical: bool  # False pour LEGACY
    n_h2_numbered: int
    n_em_dash: int
    n_f_ids: int
    n_m_ids: int
    n_source_fields: int
    n_trace_marks: int
    h2_section7_match: bool
    h2_section8_match: bool
    n_canonical_h2_exact: int
    n_canonical_h2_including_s9_variants: int
    h2_found: list = field(default_factory=list)
    C1: str = "?"
    C2: str = "?"
    C3: str = "?"
    C5: str = "?"
    C6: str = "?"
    C7: str = "?"
    C10: str = "?"
    C10_strict: str = "?"  # Avec tolérance variante §9
    score_strict: float = 0.0
    score_lenient: float = 0.0
    # Delta Source-Quintessence (v2026-07-08) : contrôle d'intégrité F-##
    delta_verdict: str = "?"  # ✅ / ⚠️ / ❌ / ?
    delta_fabricated_count: int = 0
    delta_missing_count: int = 0
    delta_source_path: str = ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def is_canonical(path: Path) -> bool:
    """Détecte si un fichier est LEGACY (hors-canonique)."""
    return path.name.endswith("_quintessence.md")


def check_C1(h2_numbered_count: int) -> str:
    """H2 numérotées 1-9 : ✅ = 9, ⚠️ = 7-8, ❌ = <7."""
    if h2_numbered_count == 9:
        return "✅"
    if h2_numbered_count >= 7:
        return "⚠️"
    return "❌"


def check_C2(n_f_ids: int, n_m_ids: int) -> str:
    """IDs préservés (F-##, M1-M4) : ✅ = > 0, ❌ = 0."""
    return "✅" if (n_f_ids + n_m_ids) > 0 else "❌"


def check_C3(n_em_dash: int) -> str:
    """Zéro em-dash (bytes 0xe2 0x80 0x94) : ✅ = 0, ❌ = > 0."""
    return "✅" if n_em_dash == 0 else "❌"


def check_C5(n_source_fields: int) -> str:
    """1 source unique : ✅ = 1, ⚠️ = 2-3 (souvent source + sous-source), ❌ = 0 ou > 3."""
    if n_source_fields == 1:
        return "✅"
    if 2 <= n_source_fields <= 3:
        return "⚠️"
    return "❌"


def check_C6(n_trace_marks: int) -> str:
    """Traçabilité [Lxx] : ✅ = > 10, ⚠️ = 1-10, ❌ = 0."""
    if n_trace_marks > 10:
        return "✅"
    if n_trace_marks >= 1:
        return "⚠️"
    return "❌"


def check_C7(s7: bool, s8: bool) -> str:
    """Sections §7-§8 canoniques (Verbatim + Notes) : ✅ = 2, ⚠️ = 1, ❌ = 0."""
    if s7 and s8:
        return "✅"
    if s7 or s8:
        return "⚠️"
    return "❌"


def check_C10(n_exact: int, n_lenient: int) -> tuple[str, str]:
    """9 noms H2 canoniques : ✅ = 9, ⚠️ = 7-8, ❌ = <7. Strict = match exact, lenient = variantes §9."""
    def verdict(n: int) -> str:
        if n == 9:
            return "✅"
        if n >= 7:
            return "⚠️"
        return "❌"
    return verdict(n_exact), verdict(n_lenient)


def score_from_verdicts(verdicts: list[str]) -> float:
    """Comptage binaire : 1 pour ✅, 0.5 pour ⚠️, 0 pour ❌."""
    score = 0.0
    for v in verdicts:
        if v == "✅":
            score += 1.0
        elif v == "⚠️":
            score += 0.5
    return score


# ==============================================================================
# Contrôle Delta Source-Quintessence (v2026-07-08)
# Bug latent corrigé : C2 = existence check, ne détectait pas les fabrications
# (cas sol_dem : 0 F-## source → 16 F-## quintessence, passé 5.5/6 strict).
# Nouveau contrôle : compare l'ensemble des F-## source vs quintessence,
# signale ❌ si fabrication (quintessence a des F-## absents de la source).
# ==============================================================================

F_ID_REGEX_EXTENDED = r"F-[A-Z]+(?:-[A-Z]+)?-?\d+"


def normalize_f_id(fid: str) -> str:
    """Normalise un F-## : insère un tiret avant le dernier groupe de chiffres.
    Permet de matcher F-PNR30 == F-PNR-30 == F-PNR-30.
    """
    return re.sub(r"([A-Z])(\d)", r"\1-\2", fid, count=1)


def extract_quintessence_source_path(text: str) -> Path | None:
    r"""Extrait le chemin source du champ "Source : `...`" de la quintessence.
    Retourne le Path absolu résolu, ou None si non trouvé.

    Le "source_rel" est déjà un chemin relatif à la racine du projet
    (ex. "investigations/2026-07-04-RIC/.../foo_INVESTIGATION.md").
    On utilise "Path(source_rel).resolve()" pour le résoudre à partir du CWD
    (qui est la racine du projet lors de l'exécution de l'audit).
    """
    m = re.search(r"^Source\s*:\s*`([^`]+)`", text, flags=re.MULTILINE)
    if not m:
        return None
    source_rel = m.group(1).strip()
    return Path(source_rel).resolve()


def extract_source_f_ids(source_path: Path) -> set[str]:
    """Extrait tous les F-## uniques d'un fichier source INVESTIGATION.
    Utilise le regex étendu (tiret optionnel) + normalisation.
    """
    if not source_path.exists():
        return set()
    text = source_path.read_text(encoding="utf-8")
    raw = set(re.findall(F_ID_REGEX_EXTENDED, text))
    return {normalize_f_id(fid) for fid in raw}


def extract_quintessence_f_ids(text: str) -> set[str]:
    """Extrait tous les F-## uniques d'une quintessence.
    Utilise le regex étendu (tiret optionnel) + normalisation.
    """
    raw = set(re.findall(F_ID_REGEX_EXTENDED, text))
    return {normalize_f_id(fid) for fid in raw}


def compute_delta_source_quintessence(quintessence_path: Path, text: str) -> dict:
    """Calcule le delta entre F-## source et F-## quintessence.

    Retourne un dict avec :
    - source_path : str | None (chemin source résolu)
    - source_exists : bool (fichier source trouvé)
    - n_source_f_ids : int
    - n_quintessence_f_ids : int
    - fabricated : list[str] (F-## dans quintessence, absents de la source)
    - missing : list[str] (F-## dans source, absents de la quintessence)
    - delta_verdict : str
        * ❌ si fabrication détectée (F-## dans quintessence non présents source)
        * ⚠️ si manquants (F-## dans source non repris dans quintessence)
        * ✅ si delta vide
        * ? si source non trouvée / champ Source : absent
    """
    source_path = extract_quintessence_source_path(text)
    if source_path is None:
        return {
            "source_path": None,
            "source_exists": False,
            "n_source_f_ids": 0,
            "n_quintessence_f_ids": 0,
            "fabricated": [],
            "missing": [],
            "delta_verdict": "?",
        }
    source_exists = source_path.exists()
    if not source_exists:
        return {
            "source_path": str(source_path),
            "source_exists": False,
            "n_source_f_ids": 0,
            "n_quintessence_f_ids": 0,
            "fabricated": [],
            "missing": [],
            "delta_verdict": "?",
        }
    source_f_ids = extract_source_f_ids(source_path)
    quintessence_f_ids = extract_quintessence_f_ids(text)
    fabricated = sorted(quintessence_f_ids - source_f_ids)
    missing = sorted(source_f_ids - quintessence_f_ids)
    if fabricated:
        delta_verdict = "❌"
    elif missing:
        delta_verdict = "⚠️"
    else:
        delta_verdict = "✅"
    return {
        "source_path": str(source_path),
        "source_exists": True,
        "n_source_f_ids": len(source_f_ids),
        "n_quintessence_f_ids": len(quintessence_f_ids),
        "fabricated": fabricated,
        "missing": missing,
        "delta_verdict": delta_verdict,
    }


def audit_file(path: Path) -> FileAudit:
    """Audite un fichier quintessence et retourne FileAudit."""
    canonical = is_canonical(path)
    text = read_text(path)
    raw = read_bytes(path)

    # C1 : H2 numérotées 1-9
    h2_numbered = re.findall(r"^##\s+(\d+)\.\s+", text, flags=re.MULTILINE)
    n_h2_numbered = len([h for h in h2_numbered if 1 <= int(h) <= 9])

    # C3 : 0 em-dash
    n_em_dash = raw.count(EM_DASH_BYTES)

    # C2 : F-## et M1-M4
    # Regex étendu (v2026-07-08) : dernier tiret optionnel pour matcher F-PNR30 ET F-PNR-30
    f_ids = re.findall(r"F-[A-Z]+(?:-[A-Z]+)?-?\d+", text)
    m_ids = re.findall(r"\bM[1-9](?!\d)", text)

    # C5 : 1 source unique
    source_fields = re.findall(r"(?m)^Source\s*:", text)

    # C6 : traçabilité [Lxx] ou [§X]
    trace_marks = re.findall(r"\[[^\]]*(?:L\d+|§\d)[^\]]*\]", text)

    # Extraction H2 réels (texte complet des lignes H2 numérotées)
    h2_lines = re.findall(r"^##\s+\d+\.\s+.*$", text, flags=re.MULTILINE)
    h2_lines_clean = [h.strip() for h in h2_lines]

    # C7 : §7 + §8 canoniques
    s7_canonical = "## 7. Verbatim et citations" in text
    s8_canonical = "## 8. Notes méthodologiques source" in text
    # Variantes acceptées
    s7_alt = bool(re.search(r"^##\s*7\.\s*Verbatim", text, flags=re.MULTILINE))
    s8_alt = bool(re.search(r"^##\s*8\.\s*Notes\s+m[ée]thodologiques", text, flags=re.MULTILINE))

    # C10 : 9 noms canoniques (match exact)
    n_canonical_exact = sum(1 for h in CANONICAL_H2 if h in text)
    n_canonical_lenient = n_canonical_exact
    # Tolérance §9 : si §9 matche l'une des variantes acceptées, ajouter +1 au compteur (pas forcer un plancher)
    has_s9_variant = any(v in text for v in SECTION_9_VARIANTS)
    if n_canonical_exact < 9 and has_s9_variant:
        n_canonical_lenient = n_canonical_exact + 1

    # Verdicts
    C1 = check_C1(n_h2_numbered)
    C2 = check_C2(len(f_ids), len(m_ids))
    C3 = check_C3(n_em_dash)  # Informatif uniquement, exclu du score (cf. docstring)
    C5 = check_C5(len(source_fields))
    C6 = check_C6(len(trace_marks))
    C7 = check_C7(s7_canonical or s7_alt, s8_canonical or s8_alt)
    C10_strict, C10_lenient = check_C10(n_canonical_exact, n_canonical_lenient)

    # Delta Source-Quintessence (v2026-07-08) : contrôle d'intégrité F-##
    delta = compute_delta_source_quintessence(path, text)
    delta_verdict = delta["delta_verdict"]
    delta_fabricated_count = len(delta["fabricated"])
    delta_missing_count = len(delta["missing"])
    delta_source_path = delta["source_path"] or ""

    # Score (C3 NEUTRALISÉ : hors scope Phase 1, cf. note scope dans docstring)
    verdicts = [C1, C2, C5, C6, C7, C10_lenient]
    score_lenient = score_from_verdicts(verdicts)
    verdicts_strict = [C1, C2, C5, C6, C7, C10_strict]
    score_strict = score_from_verdicts(verdicts_strict)

    return FileAudit(
        file=path.name,
        canonical=canonical,
        n_h2_numbered=n_h2_numbered,
        n_em_dash=n_em_dash,
        n_f_ids=len(f_ids),
        n_m_ids=len(m_ids),
        n_source_fields=len(source_fields),
        n_trace_marks=len(trace_marks),
        h2_section7_match=s7_canonical or s7_alt,
        h2_section8_match=s8_canonical or s8_alt,
        n_canonical_h2_exact=n_canonical_exact,
        n_canonical_h2_including_s9_variants=n_canonical_lenient,
        h2_found=h2_lines_clean,
        C1=C1, C2=C2, C3=C3, C5=C5, C6=C6, C7=C7,
        C10=C10_lenient, C10_strict=C10_strict,
        score_strict=score_strict,
        score_lenient=score_lenient,
        delta_verdict=delta_verdict,
        delta_fabricated_count=delta_fabricated_count,
        delta_missing_count=delta_missing_count,
        delta_source_path=delta_source_path,
    )


def audit_directory(qdir: Path) -> tuple[list[FileAudit], list[FileAudit]]:
    """Audite tout le dossier et retourne (canoniques, legacy)."""
    canoniques: list[FileAudit] = []
    legacy: list[FileAudit] = []
    for path in sorted(qdir.glob("*.md")):
        result = audit_file(path)
        if result.canonical:
            canoniques.append(result)
        else:
            legacy.append(result)
    return canoniques, legacy


def aggregate_stats(audits: list[FileAudit]) -> dict:
    """Agrège les verdicts par critère."""
    if not audits:
        return {}
    criteria = ["C1", "C2", "C3", "C5", "C6", "C7", "C10", "C10_strict"]
    stats: dict = {"total": len(audits), "criteria": {}}
    for crit in criteria:
        verdicts = [getattr(a, crit) for a in audits]
        stats["criteria"][crit] = {
            "✅": verdicts.count("✅"),
            "⚠️": verdicts.count("⚠️"),
            "❌": verdicts.count("❌"),
            "taux_ok_strict": round(verdicts.count("✅") / len(verdicts) * 100, 1),
            "taux_ok_ou_warning": round(
                (verdicts.count("✅") + verdicts.count("⚠️")) / len(verdicts) * 100, 1
            ),
        }
    # Delta Source-Quintessence (v2026-07-08) : agrégation séparée (informatif)
    delta_verdicts = [a.delta_verdict for a in audits]
    stats["criteria"]["delta"] = {
        "✅": delta_verdicts.count("✅"),
        "⚠️": delta_verdicts.count("⚠️"),
        "❌": delta_verdicts.count("❌"),
        "?": delta_verdicts.count("?"),
        "taux_ok_strict": round(delta_verdicts.count("✅") / len(delta_verdicts) * 100, 1),
        "taux_ok_ou_warning": round(
            (delta_verdicts.count("✅") + delta_verdicts.count("⚠️"))
            / len(delta_verdicts) * 100, 1
        ),
    }
    # Scores moyens (score_max = 6, C3 neutralisé)
    stats["score_strict_moyen"] = round(
        sum(a.score_strict for a in audits) / len(audits), 2
    )
    stats["score_lenient_moyen"] = round(
        sum(a.score_lenient for a in audits) / len(audits), 2
    )
    stats["score_max"] = 6.0  # 6 critères post-neutralisation C3 (C1, C2, C5, C6, C7, C10)
    return stats


def render_json(canoniques: list[FileAudit], legacy: list[FileAudit]) -> str:
    return json.dumps(
        {
            "canoniques": [asdict(a) for a in canoniques],
            "legacy": [asdict(a) for a in legacy],
            "stats": {
                "canoniques": aggregate_stats(canoniques),
                "legacy": aggregate_stats(legacy),
            },
        },
        ensure_ascii=False,
        indent=2,
    )


def render_markdown(
    canoniques: list[FileAudit],
    legacy: list[FileAudit],
    stats: dict,
) -> str:
    lines: list[str] = []
    lines.append("# Audit automatisé Phase 1 Sublimator v35 : n=42 + 1 LEGACY")
    lines.append("")
    lines.append("**Date :** 2026-07-08  ")
    lines.append("**Méthodologie :** 6 critères objectifs (C1, C2, C5, C6, C7, C10) + scoring binaire 1/0.5/0 sur 6 points max.  ")
    lines.append("**C3 (zéro em-dash) NEUTRALISÉ 2026-07-08** : scope originel = articles (Phase 3), pas fiches internes (Phase 1 quintessence). Champ `n_em_dash` reste tracké informativement. Cf. docstring pour note scope complète.")
    lines.append("**Critères subjectifs exclus :** C4 (Refus Phase 1), C8 (Fidélité citations), C9 (Pas de jugement) ; réservés à l'audit manuel échantillonné (cf. n=6).  ")
    lines.append("**Critère C10** : strict = match exact des 9 noms canoniques ; lenient = tolérance de la variante §9 « Limites (case-limites) ».")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Synthèse
    lines.append("## 1. Synthèse globale n=42 canoniques")
    lines.append("")
    s = stats["canoniques"]
    lines.append(f"- **Total fichiers canoniques :** {s['total']}")
    lines.append(f"- **Score strict moyen :** {s['score_strict_moyen']} / {s['score_max']}")
    lines.append(f"- **Score lenient moyen :** {s['score_lenient_moyen']} / {s['score_max']}")
    lines.append("")
    lines.append("### 1.1 Taux par critère (canoniques)")
    lines.append("")
    lines.append("| Critère | ✅ | ⚠️ | ❌ | Taux OK strict | Taux OK+Warn |")
    lines.append("|---------|----|----|----|----------------|---------------|")
    # C3 neutralisé : stats C3 affichées pour info mais hors score
    for crit in ["C1", "C2", "C3", "C5", "C6", "C7", "C10", "C10_strict"]:
        c = s["criteria"][crit]
        lines.append(
            f"| **{crit}** | {c['✅']} | {c['⚠️']} | {c['❌']} | {c['taux_ok_strict']}% | {c['taux_ok_ou_warning']}% |"
        )
    # Delta Source-Quintessence (v2026-07-08) : colonne supplémentaire
    d = s["criteria"]["delta"]
    lines.append(
        f"| **Δ Source** | {d['✅']} | {d['⚠️']} | {d['❌']} | {d['taux_ok_strict']}% | {d['taux_ok_ou_warning']}% |"
    )
    lines.append("")

    # Tableau détaillé par fichier
    lines.append("## 2. Tableau détaillé (42 canoniques)")
    lines.append("")
    lines.append("| Fichier | C1 | C2 | C3* | C5 | C6 | C7 | C10 (strict) | C10 (variant §9) | Δ Source | Score strict |")
    lines.append("|---------|----|----|-----|----|----|----|---------------|--------------------|----------|---------------|")
    lines.append("")
    lines.append("*C3 = zéro em-dash, NEUTRALISÉ (informatif uniquement, hors score).*")
    lines.append("")
    lines.append("*Δ Source = contrôle Delta Source-Quintessence (v2026-07-08) : compare les F-## source vs quintessence. ❌ si fabrication détectée.*")
    lines.append("")
    for a in canoniques:
        delta_cell = a.delta_verdict
        if a.delta_fabricated_count > 0:
            delta_cell = f"{a.delta_verdict} ({a.delta_fabricated_count} fab.)"
        lines.append(
            f"| `{a.file}` | {a.C1} | {a.C2} | {a.C3} | {a.C5} | {a.C6} | {a.C7} | {a.C10_strict} | {a.C10} | {delta_cell} | {a.score_strict}/6 |"
        )
    lines.append("")

    # LEGACY
    if legacy:
        lines.append("## 3. Quintessences LEGACY (hors-canonique)")
        lines.append("")
        for a in legacy:
            lines.append(f"- `{a.file}` : H2 numérotées = {a.n_h2_numbered}, F-## = {a.n_f_ids}, em-dash (informatif) = {a.n_em_dash}")
        lines.append("")

    # Patterns identifiés
    lines.append("## 4. Patterns de déviation")
    lines.append("")
    c10_strict_fail = [a for a in canoniques if a.C10_strict == "❌"]
    c10_warn = [a for a in canoniques if a.C10_strict == "⚠️"]
    c7_fail = [a for a in canoniques if a.C7 == "❌"]
    lines.append(f"- **C10 strict = ❌** : {len(c10_strict_fail)}/42 = {round(len(c10_strict_fail)/42*100, 1)}%")
    lines.append(f"- **C10 strict = ⚠️** : {len(c10_warn)}/42 = {round(len(c10_warn)/42*100, 1)}%")
    lines.append(f"- **C7 = ❌** (ni Verbatim ni Notes canoniques) : {len(c7_fail)}/42 = {round(len(c7_fail)/42*100, 1)}%")
    lines.append("")

    # Distribution H2 réels
    h2_patterns: dict[str, int] = {}
    for a in canoniques:
        for h in a.h2_found:
            # Normalise pour grouper les variantes
            key = re.sub(r"^\d+\.\s*", "", h)
            h2_patterns[key] = h2_patterns.get(key, 0) + 1
    lines.append("## 5. Distribution des noms H2 réels (top patterns)")
    lines.append("")
    for pattern, count in sorted(h2_patterns.items(), key=lambda x: -x[1])[:20]:
        lines.append(f"- `{pattern}` : {count} occurrences")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit automatisé Phase 1 Sublimator v35 (n=42 + LEGACY)",
    )
    parser.add_argument(
        "mode",
        choices=["json", "markdown", "full"],
        help="Mode de sortie : json | markdown | full (les deux)",
    )
    parser.add_argument(
        "-d", "--dossier",
        type=Path,
        default=DEFAULT_QUINTESSENCE_DIR,
        help=f"Dossier _quintessence (défaut : {DEFAULT_QUINTESSENCE_DIR})",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Fichier de sortie (optionnel, sinon stdout)",
    )
    args = parser.parse_args()

    if not args.dossier.is_dir():
        print(f"ERREUR : dossier introuvable : {args.dossier}", file=sys.stderr)
        return 1

    canoniques, legacy = audit_directory(args.dossier)
    if not canoniques:
        print(f"ERREUR : aucun fichier quintessence trouvé dans {args.dossier}", file=sys.stderr)
        return 1
    stats = {
        "canoniques": aggregate_stats(canoniques),
        "legacy": aggregate_stats(legacy),
    }

    if args.mode in ("json", "full"):
        output_json = render_json(canoniques, legacy)
        if args.mode == "json":
            print(output_json)
        else:
            json_path = args.output.with_suffix(".json") if args.output else Path("outputs/audit_phase1_v35_n42.json")
            json_path.parent.mkdir(parents=True, exist_ok=True)
            json_path.write_text(output_json, encoding="utf-8")
            print(f"JSON écrit : {json_path}", file=sys.stderr)

    if args.mode in ("markdown", "full"):
        output_md = render_markdown(canoniques, legacy, stats)
        if args.mode == "markdown":
            print(output_md)
        else:
            md_path = args.output if args.output else Path("outputs/audit_phase1_v35_n42.md")
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(output_md, encoding="utf-8")
            print(f"Markdown écrit : {md_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
