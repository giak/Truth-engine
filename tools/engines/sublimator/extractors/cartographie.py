"""Cartographie v1.0 — extraction legere des INVESTIGATION.md vers cartographie.json.

Sublimator v35 Phase 0 : produit une carte 1 ligne/enquete (~50 lignes pour 44) qui tient
en contexte. Le script Python gere la partie deterministe (regex sur headers), le LLM
prend le relais sur les champs semantiques manquants (these_candidate, complexite, keywords).

**Mode de fonctionnement** (CLI --mode) :
- `python` : extraction regex uniquement. Fichiers incomplets = status="needs_llm".
- `hybrid` : extraction regex, puis 1 appel LLM par fichier needs_llm pour completer.
- `llm` : skip regex, tout passe par LLM (le plus lent, le plus robuste).

**Camps extraits** (cartographie.json) :
- prefix : derive du filename (ex: "ric_def" de "ric_def_INVESTIGATION.md")
- sujet : 1ere ligne non-vide du fichier (titre)
- these_candidate : 1ere phrase trouvee dans §0 (Python) ou generee par LLM (LLM fallback)
- complexite : "APEX" | "STANDARD" | "LIGHT" | "unknown" (degrade)
- keywords : top 5 mots-cles extraits (Python: TF-IDF simple, LLM: generation)
- urls_count : nombre d'URLs dans le fichier (regex)
- f_count_estime : nombre de F## (regex F-XXX)
- n_lines : longueur du fichier
- status : "ok" | "needs_llm" | "llm_filled"
- llm_notes : trace du fallback LLM (vide si status="ok")

**Fallback LLM** (mode hybrid) :
- Declenche si : these_candidate vide, complexite=="unknown", ou keywords<3.
- Cout : 1 appel LLM par fichier degrade (~0.01€/fichier).
- Pilotage : `cartographie.py <dir> --mode hybrid --output cartographie.json`.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


# Regex compilees (evite recompilation a chaque fichier)
RE_SECTION0 = re.compile(r"^## §0\b", re.MULTILINE)
RE_SECTION5 = re.compile(r"^## §5\b", re.MULTILINE)
# Regex Complexite tolerante au bold markdown ** avant et apres le ":"
# Matche : "**Complexit\u00e9 :** APEX (14/18)" ou "Complexit\u00e9: APEX" ou "complexit\u00e9 : LIGHT"
RE_COMPLEXITE = re.compile(
    r"Complexit[ée]\s*:\s*\**\s*(APEX|STANDARD|LIGHT)",
    re.IGNORECASE,
)
# URL regex avec strip de la ponctuation finale (.,;:) et bracket fermant
RE_URL = re.compile(r"https?://[^\s\)\]<>\u00bb]+", re.IGNORECASE)
# Ces deux patterns permettent de detecter les bold headers FR standards :
#   **Date :** 2026-07-04 (meta, pas contenu)
#   **Th\u00e8se :** Le RIC est verrouill\u00e9... (valeur = these candidate)
RE_BOLD_META_HEADER = re.compile(r"^\*\*[^*]+\*\*\s*$")  # ligne entiere en bold = meta
RE_FAIT = re.compile(r"\bF-\d{2,4}\b")
RE_KEYWORDS_STOP = re.compile(
    r"\b(le|la|les|de|du|des|un|une|et|ou|dans|sur|par|pour|avec|sans|"
    r"ce|cette|cettes|ces|son|sa|ses|leur|leurs|qui|que|quoi|"
    r"est|sont|ete|etre|a|ont|fait|faire|plus|meme|tout|tous|"
    r"the|of|to|in|is|are|and|or|as|at|by|for|with|without|"
    r"§\d|investigation|complexit|complexite|analyse|fait|faits|"
    r"enquete|enquetes|document|section|chapitre|partie|etape)\b",
    re.IGNORECASE,
)


def _extract_prefix(filename: str) -> str:
    """Derive prefix du filename. Ex: 'ric_def_INVESTIGATION.md' -> 'ric_def'."""
    stem = filename.replace(".md", "").replace(".yaml", "").replace(".json", "")
    for suffix in ("_INVESTIGATION", "_investigation", "_quintessence", "_synthese"):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
    return stem


def _extract_sujet(content: str) -> str:
    """Sujet = titre H1 (ligne commencant par '# ' mais pas '##').

    Si pas de H1, fallback sur la 1ere ligne non-meta de taille suffisante.
    """
    # Strategie 1 : H1 (ligne "# Titre" mais pas "##" ou plus)
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("##") and len(line) > 5:
            return line[2:].strip()[:200]
    # Strategie 2 : 1ere ligne non-meta de taille >= 10 chars
    for line in content.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and len(line) > 10:
            return line[:200]
    return ""


def _extract_these_candidate_python(content: str) -> str:
    """Tente d'extraire la these depuis §0 (1ere phrase non-meta du §0).

    Strategie :
    1. Si une ligne bold **Th\u00e8se :** VALEUR existe -> extraire VALEUR directement.
    2. Sinon, 1ere ligne >= 30 chars et <= 500 chars qui n'est pas meta.
    Filtre les lignes markdown meta (':', '|', '**' pur, '##', '|---', '---') qui ne
    sont pas du contenu these.
    """
    m = RE_SECTION0.search(content)
    if not m:
        return ""
    after = content[m.end():]
    next_section = re.search(r"^## §\d", after, re.MULTILINE)
    section = after[: next_section.start()] if next_section else after[:3000]
    # Strategie 1 : bold header **Th\u00e8se :** VALEUR
    m_bold = re.search(r"\*\*Th[èe]se\s*:\*\*\s*(.+?)$", section, re.MULTILINE)
    if m_bold:
        val = m_bold.group(1).strip()
        if 30 <= len(val) <= 500:
            return val
    # Strategie 2 : 1ere ligne de contenu non-meta
    for line in section.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if RE_BOLD_META_HEADER.match(line):  # bold header pur (ex: **Date :** 2026-07-04)
            continue
        if line.startswith(("|", ":")) or line.startswith("---"):
            continue
        if "|" in line and line.count("|") >= 2:  # tableau markdown
            continue
        if line.startswith("\u2014") or line.startswith("--"):  # em-dash heading
            continue
        if len(line) > 30 and len(line) < 500:
            return line
    return ""


def _extract_complexite(content: str) -> str:
    """Cherche 'Complexite: APEX|STANDARD|LIGHT' dans le header (50 premieres lignes)."""
    header = "\n".join(content.split("\n")[:50])
    m = RE_COMPLEXITE.search(header)
    return m.group(1).upper() if m else "unknown"


def _extract_keywords_python(content: str, n: int = 5) -> list[str]:
    """Extraction TF-IDF simplifiee : top N mots par frequence (hors stopwords)."""
    # Tokenize sur les mots de 4+ chars
    words = re.findall(r"\b[A-Za-zÀ-ÿ]{4,}\b", content[:50000])  # limite aux 50K premiers chars
    # Filtre stopwords
    words = [w for w in words if not RE_KEYWORDS_STOP.match(w)]
    if not words:
        return []
    # Top N par frequence
    return [w.lower() for w, _ in Counter(words).most_common(n)]


def _extract_urls_count(content: str) -> int:
    """Nombre d'URLs uniques dans le fichier (strip ponctuation finale)."""
    urls = set()
    for u in RE_URL.findall(content):
        # Strip trailing punctuation qui peut etre capturee
        u_clean = u.rstrip(".,;:!?\u3002\uff0c\uff1a\uff1b")
        urls.add(u_clean)
    return len(urls)


def _extract_f_count(content: str) -> int:
    """Nombre de F## (id de faits atomiques) trouves."""
    return len(set(RE_FAIT.findall(content)))


def _needs_llm(entry: dict[str, Any]) -> bool:
    """Determine si l'entree necessite un fallback LLM."""
    if not entry.get("these_candidate"):
        return True
    if entry.get("complexite") == "unknown":
        return True
    if len(entry.get("keywords", [])) < 3:
        return True
    return False


def extract_python(path: Path) -> dict[str, Any]:
    """Extraction 100% Python (mode 'python' ou etape 1 du mode 'hybrid')."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError) as e:
        return {
            "filename": path.name,
            "prefix": _extract_prefix(path.name),
            "status": "error",
            "error": f"Lecture impossible: {type(e).__name__}: {e}",
        }
    entry: dict[str, Any] = {
        "filename": path.name,
        "prefix": _extract_prefix(path.name),
        "sujet": _extract_sujet(content),
        "these_candidate": _extract_these_candidate_python(content),
        "complexite": _extract_complexite(content),
        "keywords": _extract_keywords_python(content, n=10),  # PIVOT C2.2 : 10 mots pour overlap
        "urls_count": _extract_urls_count(content),
        "f_count_estime": _extract_f_count(content),
        "n_lines": content.count("\n"),
        "status": "ok",  # sera revu ci-dessous
    }
    entry["status"] = "needs_llm" if _needs_llm(entry) else "ok"
    return entry


def extract_llm_fallback(entries_needing_llm: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Fallback LLM pour les fichiers degrades.

    Note : implementation reelle necessiterait un client LLM. Cette fonction est
    un stub qui :
    1. Log les fichiers a traiter
    2. Marque `status: 'llm_filled'` (placeholder, le pilote LLM re-remplit)
    3. NE MODIFIE PAS les champs (le vrai client LLM le fera)

    Pour activer le vrai LLM : remplacer le corps par un appel a anthropic/openai/etc.
    avec un prompt structure demandant these_candidate + complexite + keywords.

    **Cout estime** : ~0.01 EUR/fichier (Claude Haiku) pour ~150 tokens input + 100 output.
    Pour 44 fichiers : 0.44 EUR max.
    **Prompt suggere** (a envoyer par fichier) :
        Extrait de : {filename} (n_lines={n_lines}, complexite_initiale={complexite})
        Sujet : {sujet}
        Premiere section (1000 chars) : {content[:1000]}
        Reponds en JSON strict : {"these_candidate": "...", "complexite": "APEX|STANDARD|LIGHT", "keywords": ["k1", "k2", "k3", "k4", "k5"]}
    Args:
        entries_needing_llm: liste des entries avec status="needs_llm"
    Returns:
        Les memes entries avec status="llm_filled" et un placeholder llm_notes.
    """
    for entry in entries_needing_llm:
        missing = []
        if not entry.get("these_candidate"):
            missing.append("these_candidate")
        if entry.get("complexite") == "unknown":
            missing.append("complexite")
        if len(entry.get("keywords", [])) < 3:
            missing.append("keywords")
        # v1.0 STUB : on marque llm_filled SANS remplir les champs. Le vrai client LLM
        # doit remplacer ce stub par un appel API + update entry["these_candidate"],
        # entry["complexite"], entry["keywords"] avant de retourner.
        entry["status"] = "llm_filled"
        entry["llm_notes"] = (
            f"LLM fallback necessaire pour : {', '.join(missing)} "
            f"(stub - implementer client LLM dans extract_llm_fallback)"
        )
    return entries_needing_llm


def run(dossier: Path, mode: str = "python") -> dict[str, Any]:
    """Execute la cartographie sur un dossier d'investigations.

    Args:
        dossier: chemin du dossier contenant les *_INVESTIGATION.md
        mode: "python" (regex only) | "hybrid" (regex + LLM fallback) | "llm" (LLM only - non implemente)
    Returns:
        dict compatible JSON : {date_cartographie, complexity, n_enquetes_totales, n_enquetes_ok, n_enquetes_needs_llm, n_enquetes_llm_filled, enquetes: [...]}
    """
    if not dossier.is_dir():
        raise FileNotFoundError(f"Dossier introuvable : {dossier}")
    files = sorted(dossier.glob("*_INVESTIGATION.md"))
    if not files:
        raise FileNotFoundError(f"Aucun fichier *_INVESTIGATION.md dans {dossier}")
    entries: list[dict[str, Any]] = []
    for f in files:
        entry = extract_python(f)
        entries.append(entry)
    n_ok = sum(1 for e in entries if e["status"] == "ok")
    n_needs_llm = sum(1 for e in entries if e["status"] == "needs_llm")
    if mode == "hybrid" and n_needs_llm > 0:
        # En mode hybrid, on appelle le fallback LLM sur les besoins
        to_fill = [e for e in entries if e["status"] == "needs_llm"]
        entries = extract_llm_fallback(to_fill)
        # Re-compte apres LLM
        n_llm_filled = sum(1 for e in entries if e["status"] == "llm_filled")
        n_needs_llm_final = sum(1 for e in entries if e["status"] == "needs_llm")
    else:
        n_llm_filled = 0
        n_needs_llm_final = n_needs_llm
    complexity = "APEX"  # 44 enquetes = APEX par defaut (dossier massif)
    # Cluster fallback (Q7 fix audit v35 - PIVOT C1) : group entries by complexite pour Phase 2 Map-Reduce.
    # NOTE DEGRADE : ce grouping est par complexite (operationnel), PAS thematique comme specifie
    # dans prompt-v35.md §Phase 0 §Plan de repli (juridique/technique/psychologique/...).
    # Pour des clusters THEMATIQUES : utiliser `cartographie.py ... --mode hybrid` ou `--mode llm`
    # qui deleguent au LLM la classification thematique des fiches needs_llm.
    complexites = [e.get("complexite", "unknown") for e in entries]
    unique_complexites = sorted(set(complexites))
    clusters = []
    for i, c in enumerate(unique_complexites):
        matching = [e for e in entries if e.get("complexite", "unknown") == c]
        if matching:
            clusters.append({
                "id": f"C{i+1}",
                "label": f"complexite_{c.lower()}",
                "n_enquetes": len(matching),
                "prefixes": [e["prefix"] for e in matching],
                "sufficient": len(matching) >= 2,  # flag cluster trop petit
            })
    # Cluster thematic PIVOT C2.2 - keywords-fallback depth (granularite au-dela complexite)
    # Strategie : union-find sur Jaccard keywords >= 0.15 entre fiches (10 mots extraits
    # par fiche, donc >=2 mots partages sur 10 = overlap thematique). Si produit
    # >= 3 clusters, on prend THEMATIC comme cluster_method (meilleur que complexite_unknown
    # qui collapse 86% du corpus en 1 mega-cluster, perdant l'interet Map-Reduce).
    thematic_clusters = _cluster_keywords_fallback(entries, jaccard_threshold=0.15)
    if len(thematic_clusters) >= 3 and len(thematic_clusters) < len(entries):
        # THEMATIC prime sur COMPLEXITE (granularite superieure), mais seulement si
        # on regroupe reellement (sinon 1 cluster par fiche = inutile)
        clusters = thematic_clusters
        cluster_method = "thematic_keywords_fallback"
    else:
        cluster_method = "complexite_fallback"  # PIVOT C1 fallback preserve
    return {
        "date_cartographie": _today_iso(),
        "complexity": complexity,
        "mode": mode,
        "cluster_method": cluster_method,  # "thematic_keywords_fallback" ou "complexite_fallback"
        "n_enquetes_totales": len(entries),
        "n_enquetes_ok": n_ok,
        "n_enquetes_needs_llm": n_needs_llm_final,
        "n_enquetes_llm_filled": n_llm_filled,
        "n_clusters": len(clusters),
        "clusters": clusters,
        "enquetes": entries,
    }


def _jaccard_keywords(a: list[str], b: list[str]) -> float:
    """Jaccard sur sets lowercase de keywords. 0.0 si les deux sets sont vides."""
    sa = set(k.lower() for k in (a or []))
    sb = set(k.lower() for k in (b or []))
    if not (sa | sb):
        return 0.0
    return len(sa & sb) / len(sa | sb)


def _cluster_keywords_fallback(entries: list[dict[str, Any]], jaccard_threshold: float = 0.3) -> list[dict[str, Any]]:
    """Union-find clustering par Jaccard keywords >= threshold (PIVOT C2.2).

    Permet de degager des clusters thematiques au-dela du grouping complexite.
    Exemple : 36 fiches "complexite_unknown" peuvent etre reduites a 8-12 clusters
    thematiques (juridique, fiscal, militaire, etc.) selon les keywords partages.

    Args:
        entries: liste complete des entries cartographiees.
        jaccard_threshold: seuil minimum de Jaccard keywords pour considerer 2 fiches liees.
    Returns:
        Liste de clusters [{id, label, n_enquetes, prefixes, sufficient, top_keywords}].
    """
    n = len(entries)
    if n == 0:
        return []
    # Union-Find: parent[i] = parent cluster de i
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    # Comparaison pairwise O(n^2) - acceptable pour n <= 100 (44 enquetes largement OK)
    kws = [set(k.lower() for k in (e.get("keywords") or [])) for e in entries]
    for i in range(n):
        for j in range(i + 1, n):
            # Calcul Jaccard inline pour eviter appel fonction boucle chaude
            sa, sb = kws[i], kws[j]
            if not (sa | sb):
                continue
            if len(sa & sb) / len(sa | sb) >= jaccard_threshold:
                union(i, j)
    # Group entries par racine union-find
    groups: dict[int, list[int]] = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    # Construit les clusters
    clusters = []
    for idx, (root, members) in enumerate(sorted(groups.items())):
        if not members:
            continue
        # Top keywords : intersection des keywords entre membres (coeur du cluster)
        member_sets = [kws[i] for i in members]
        common = set.intersection(*member_sets) if len(member_sets) > 1 else member_sets[0]
        cluster_kws = sorted(common)[:5] if common else sorted(set.union(*member_sets))[:5]
        clusters.append({
            "id": f"T{idx+1}",
            "label": "theme_" + (cluster_kws[0] if cluster_kws else "divers"),
            "n_enquetes": len(members),
            "prefixes": [entries[i]["prefix"] for i in members],
            "sufficient": len(members) >= 2,
            "top_keywords": cluster_kws,
        })
    # Tri : plus gros clusters d'abord (Map-Reduce sequential)
    clusters.sort(key=lambda c: -c["n_enquetes"])
    return clusters


def _today_iso() -> str:
    from datetime import date
    return date.today().isoformat()


def main() -> int:
    parser = argparse.ArgumentParser(description="Cartographie v1.0 - extraction legere des investigations")
    parser.add_argument("dossier", type=Path, help="Dossier contenant les *_INVESTIGATION.md")
    parser.add_argument("--mode", choices=["python", "hybrid", "llm"], default="python", help="Mode d'extraction (defaut: python)")
    parser.add_argument("--output", "-o", type=Path, help="Fichier de sortie JSON (defaut: stdout)")
    args = parser.parse_args()
    try:
        result = run(args.dossier, args.mode)
    except FileNotFoundError as e:
        print(f"ERREUR : {e}", file=sys.stderr)
        return 1
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Cartographie ecrite dans {args.output} ({result['n_enquetes_totales']} enquetes, {result['n_enquetes_ok']} ok, {result['n_enquetes_needs_llm']} needs_llm)", file=sys.stderr)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
