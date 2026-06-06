import re

CIBLES = {"SIMPLE": 70, "MEDIUM": 80, "COMPLEX": 85, "APEX": 90}


def count_phrases_faits(text: str) -> int:
    """Compte les phrases contenant F### OU chiffre long (sans double-compte)."""
    phrases = re.split(r"[.\n]+", text)
    n = 0
    for p in phrases:
        p = p.strip()
        if not p:
            continue
        if re.search(r"\bF0?\d{2,3}\b", p) or re.search(r"\d{2,}", p):
            n += 1
    return max(n, 1)


def compute_completude(text: str, matrice: list) -> float:
    """Score de complétude = n_faits_matrice / n_phrases_faits * 100."""
    n_phrases = count_phrases_faits(text)
    n_faits = len(matrice)
    return round((n_faits / n_phrases) * 100, 2)


def gate_g_pass(score: float, complexity: str = "MEDIUM") -> bool:
    """Vérifie si GATE_G passe pour la complexité."""
    return score >= CIBLES.get(complexity, 80)
