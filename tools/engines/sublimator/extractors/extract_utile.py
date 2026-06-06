"""Extraction article-utile : patterns que SUBLIMATOR doit capturer pour
qu'un article Substack soit solide.

Tous extractibles par regex Python pur, sans appel API externe. Le LLM
hôte (Agent B) agrège ensuite ces éléments en prose.

Référence spec : §X.8 EXTRACTION ATOMIQUE.
"""
import re
from typing import List, Dict


def extract_dates(text: str) -> List[Dict]:
    """Capture dates ISO, françaises, historiques, relatives."""
    results = []
    patterns = [
        (r"\b(\d{4}-\d{2}-\d{2})\b", "ISO"),
        (r"\b(\d{1,2}\s+(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+\d{4})\b", "FR"),
        (r"\b(\d{1,2}/\d{1,2}/\d{2,4})\b", "slash"),
        (r"\b((?:\d+\s+)?(?:av\.\s*J\.-?C\.|apr\.\s*J\.-?C\.))\b", "REL"),
        (r"\b([IVX]+\w*\s+siècle(?:\s+(?:av\.\s*J\.-?C\.|apr\.\s*J\.-?C\.))?)\b", "SIECLE"),
        (r"\b(il y a\s+\d+\s+ans?)\b", "REL-ANS"),
        (r"\b(?:en|vers|autour de)\s+(-?\d{3,4})\b", "AN"),
    ]
    for pattern, fmt in patterns:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            line_no = text[: m.start()].count("\n") + 1
            ctx_start = max(0, m.start() - 30)
            ctx_end = min(len(text), m.end() + 30)
            results.append({
                "date": m.group(1),
                "format": fmt,
                "line_no": line_no,
                "contexte_brut": text[ctx_start:ctx_end].strip(),
            })
    return results


def extract_sommes(text: str) -> List[Dict]:
    """Capture €, $, Mds, M, k, %, ratios."""
    results = []
    patterns = [
        (r"\b(\d[\d\s,.]*)\s*(milliards?|Mds?)\b", "Mds"),
        (r"\b(\d[\d\s,.]*)\s*(millions?|M)\b", "M"),
        (r"\b(\d[\d\s,.]*)\s*mille\b", "k"),
        (r"\b(\d[\d\s,.]*)\s*%", "pct"),
        (r"(\d[\d\s,.]*)\s*[€$£¥]", "devise"),
        (r"[€$£¥]\s*(\d[\d\s,.]*)", "devise-prefix"),
    ]
    for pattern, fmt in patterns:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            line_no = text[: m.start()].count("\n") + 1
            ctx_start = max(0, m.start() - 30)
            ctx_end = min(len(text), m.end() + 30)
            results.append({
                "montant": m.group(1).strip(),
                "format": fmt,
                "line_no": line_no,
                "contexte_brut": text[ctx_start:ctx_end].strip(),
            })
    return results


def extract_citations(text: str) -> List[Dict]:
    """Capture citations directes guillemets français « ... »."""
    results = []
    for m in re.finditer(r"«\s*([^»]{20,300})\s*»", text):
        line_no = text[: m.start()].count("\n") + 1
        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 30)
        results.append({
            "citation": m.group(1).strip(),
            "line_no": line_no,
            "contexte_brut": text[ctx_start:ctx_end].strip(),
        })
    return results


def extract_urls(text: str) -> List[Dict]:
    """Capture URLs dans le texte."""
    results = []
    for m in re.finditer(r"https?://[^\s)>\]«»\"']+", text):
        line_no = text[: m.start()].count("\n") + 1
        url = m.group(0).rstrip(".,;:")
        results.append({
            "url": url,
            "line_no": line_no,
        })
    return results


def extract_acteurs_nommes(text: str) -> List[Dict]:
    """Heuristique NOMS PROPRES : 2-4 mots capitalisés séparés par 0-3 mots.

    Limitation : faux positifs possibles. Le LLM hôte (Agent B) valide.
    """
    results = []
    word_cap = r"[A-ZÉÀÂÎÔÛÄËÏÖÜÇ][a-zà-ÿ'\-]+"
    pattern = re.compile(rf"\b({word_cap}(?:\s+\w{{1,20}}\s+{word_cap}){{1,3}})\b")
    seen = set()
    for m in pattern.finditer(text):
        nom = m.group(1).strip()
        if nom in seen or len(nom) < 5:
            continue
        seen.add(nom)
        line_no = text[: m.start()].count("\n") + 1
        results.append({
            "nom": nom,
            "line_no": line_no,
        })
    return results


def extract_marqueurs_causalite(text: str) -> List[Dict]:
    """Capture marqueurs de causalité."""
    results = []
    mots = [
        r"\bparce que\b", r"\bpar conséquent\b", r"\bdonc\b",
        r"\bcar\b", r"\bainsi\b", r"\bce qui implique\b",
        r"\bce qui permet de\b", r"\bd'où\b", r"\bc'est pourquoi\b",
    ]
    pattern = re.compile("|".join(mots), re.IGNORECASE)
    for m in pattern.finditer(text):
        line_no = text[: m.start()].count("\n") + 1
        ctx_start = max(0, m.start() - 50)
        ctx_end = min(len(text), m.end() + 100)
        results.append({
            "marqueur": m.group(0),
            "line_no": line_no,
            "contexte_brut": text[ctx_start:ctx_end].strip(),
        })
    return results


def extract_marqueurs_rhetorique(text: str) -> List[Dict]:
    """Capture marqueurs rhétoriques du registre SUBLIMATOR."""
    results = []
    marqueurs = ["DEM", "BF", "NUM", "AUTH", "FAC", "EM", "ANA"]
    for marqueur in marqueurs:
        pattern = re.compile(rf"\b{marqueur}(?:[A-Z_0-9]+)?\b")
        for m in pattern.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            results.append({
                "marqueur": m.group(0),
                "type": marqueur,
                "line_no": line_no,
            })
    return results


def extract_sections_plan(text: str) -> List[Dict]:
    """Capture les 18 sections du plan SUBLIMATOR (§1 à §18)."""
    results = []
    pattern = re.compile(r"^##?\s*§(\d+)\s+([A-ZÀÂÉÈÊËÏÎÔÙÛÇ][^\n]{3,80})", re.MULTILINE)
    for m in pattern.finditer(text):
        results.append({
            "section_num": int(m.group(1)),
            "section_titre": m.group(2).strip(),
            "line_no": text[: m.start()].count("\n") + 1,
        })
    return results


def extract_utile_all(text: str) -> Dict[str, List]:
    """Agrège toutes les extractions article-utile."""
    return {
        "dates": extract_dates(text),
        "sommes": extract_sommes(text),
        "citations": extract_citations(text),
        "urls": extract_urls(text),
        "acteurs_nommes": extract_acteurs_nommes(text),
        "marqueurs_causalite": extract_marqueurs_causalite(text),
        "marqueurs_rhetorique": extract_marqueurs_rhetorique(text),
        "sections_plan": extract_sections_plan(text),
    }
