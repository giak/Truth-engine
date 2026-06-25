"""HEAD-check URLs — seul module Python nécessaire pour Sublimator v34 Léger."""

import urllib.request
import urllib.error
from typing import Literal

Fiabilite = Literal["✦", "✧", "⁅", "❧"]


def head_check(url: str, timeout: int = 5) -> int | None:
    """Retourne le status code HTTP, ou None si la requête échoue."""
    if not url:
        return None
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


def score_fiabilite(url: str = "", tier: int | None = None) -> Fiabilite:
    """Score fiabilité: ✦ tier1+200, ✧ tier2++200, ⁅ cassé/erreur, ❧ pas d'URL."""
    if not url:
        return "❧"
    status = head_check(url)
    if status is None:
        return "⁅"
    if status == 200:
        return "✦" if tier == 1 else "✧"
    return "⁅"
