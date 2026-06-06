import urllib.request
import urllib.error
from typing import Literal

Fiabilite = Literal["✦", "✧", "⁅", "❧"]


def score_fiabilite(url: str = "", tier: int = None) -> Fiabilite:
    """Score fiabilité selon URL et tier. Tier 1 = primaire (✦), Tier 2+ = secondaire (✧)."""
    if not url:
        return "❧"
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as r:
            if r.status == 200:
                return "✦" if tier == 1 else "✧"
            return "⁅"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return "⁅"


def jaccard(s1: str, s2: str) -> float:
    """Jaccard sur mots (lowercase)."""
    w1 = set(s1.lower().split())
    w2 = set(s2.lower().split())
    if not w1 and not w2:
        return 1.0
    return len(w1 & w2) / max(len(w1 | w2), 1)


def curator_fusion(candidats_a: list, ajouts_b: list, civ_prefix: str) -> list:
    """Fusionne candidats A + ajouts B, dédoublonne (Jaccard < 0.7), scoring."""
    result = []

    for cand in candidats_a:
        result.append({
            "id_target": cand.get("id_target", f"F-{civ_prefix}???"),
            "fait": cand.get("fait") or cand.get("contexte_brut", ""),
            "input_format": cand.get("input_format", "?"),
            "source_section": cand.get("source_section", "?"),
            "url": cand.get("url", ""),
            "tier": cand.get("tier"),
        })

    for ajout in ajouts_b:
        is_dup = any(
            jaccard(r["fait"], ajout.get("fait", "")) > 0.7 for r in result
        )
        if not is_dup:
            result.append({
                "id_target": ajout.get("id_target", f"F-{civ_prefix}???"),
                "fait": ajout.get("fait", ""),
                "input_format": "LLM-extracted",
                "source_section": ajout.get("source_section", "?"),
                "url": ajout.get("url", ""),
                "tier": ajout.get("tier"),
            })

    for r in result:
        r["fiabilite"] = score_fiabilite(url=r.get("url", ""), tier=r.get("tier"))

    return result
