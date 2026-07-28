"""
Fetch Canoniques — Orchestrateur @FETCH multi-clés (Verrou-B Cycle V154-V253).

Périmètre :
  investigations/2026-07/2026-07-10_14-juillet-2026-defile-privatisation/
  (44 V154-V197 INV + 7 SYNTHESE topic-papers consolidés)

Rôle :
  1. Extrait les clés canoniques depuis les fichiers .md (KEY_NAMES + @FETCH
     markers + Anthme-@-FETCH placeholders).
  2. Produit un manifest prioritisable :
       - outputs/fetch_manifest_v154_v253.json (machine-readable)
       - outputs/fetch_manifest_v154_v253.md   (human-readable, exécutable LLM)
  3. Option --resolve : HEAD-req urllib contre URL candidates, marque OK/404/403.

Anti-cascade cleanup (V176-V197-pattern) : applique collapse + itération-3
sur le SCRIPT-LUI-MÊME si modifications manuelles introduisent des répétitions
de tokens (cycle-cycle, distinct-distinct, etc.). Cleanup autonome appliqué
sur chaque fichier-keyword mark à l'affichage du marcheur.

Usage :
    python3 tools/fetch_canoniques.py scan          # extrait clés, dump stdout
    python3 tools/fetch_canoniques.py manifest      # écrit outputs/fetch_manifest_v154_v253.json + .md
    python3 tools/fetch_canoniques.py resolve       # ajoute HEAD-req urllib (peut être long)
    python3 tools/fetch_canoniques.py full          # scan + manifest + resolve
    python3 tools/fetch_canoniques.py cleanup-self  # applique anti-cascade sur le script lui-même

Search priority (cf. truth-engine-v2/KERNEL.md) :
    1. @MNEMO_Q → local DB
    2. @WEB     → DuckDuckGo
    3. @FETCH   → direct URL (ce script orchestre)
    4. @EXA     → LAST RESORT, rate-limited

Verrou-B = programmé ici : ~175 @FETCH multi-clés canoniques à résoudre
                          pour promotion Tier-1 ARTICLE press-FR canonique
                          cycle V154-V253.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path("/home/giak/projects/truth-engine")
DEFAULT_TARGET_DIR = PROJECT_ROOT / "investigations/2026-07/2026-07-10_14-juillet-2026-defile-privatisation"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs"
DEFAULT_OUTPUT_PREFIX = "fetch_manifest_v154_v253"

# Thématiques 12-topic-papers-prévus-V154-V253 + canonical-keys-with-URL-hints
# Format : thematic -> [(canonical-key, url-hint, source-paper-tag, tier-priority 1=haute)]
# url-hint = partial URL (often homepage-part) ; --resolve mode vérifie via HEAD.
CANON_KEYS: list[tuple[str, str, str, int]] = [
    # -- Thématique Forensique terrain (V190-V193) --
    # Muller-Hertz Report : marque fabrication_alert - not_found dans littérature-médico-légale-officielle-Bucha (researcher-web 2026-07-11)
    ("Muller-Hertz-Scientific-Report-2024-Autopsies-458-corps",
     "", "V190-Bucha", 1),
    ("Muller-Hertz-Bellingcat-Investigation-2022-Autopsies-458-corps",
     "https://www.bellingcat.com/news/ukraine-and-russia/", "V190-Bucha", 1),
    ("OSCE-ODIHR-Bucha-Mission-2022",
     "https://www.osce.org/odihr/", "V190-Bucha", 1),
    ("ICC-OTP-Bucha-Warrants-2023",
     "https://www.icc-cpi.int/news/", "V190-V192", 1),
    ("Maxar-Satellites-Yablonska-Street-19-mars-2022",
     "https://www.maxar.com/", "V190-Bucha", 1),
    ("Amnesty-Bucha-Report-2022",
     "https://www.amnesty.org/en/search/?query=bucha", "V190-Bucha", 1),
    ("HRW-Bucha-Report-2022",
     "https://www.hrw.org/search?keyword=bucha", "V190-Bucha", 2),
    ("Bellingcat-Bucha-Evidence-Review",
     "https://www.bellingcat.com/", "V190-Bucha", 2),
    ("Katchanovski-Univ-Ottawa-Peer-Reviewed-2024",
     "https://www.researchgate.net/profile/", "V191-SBU-Botsman", 1),
    ("SBU-Activities-Statement-Anthme-@-FETCH",
     "https://ssu.gov.ua/en/activity", "V191-SBU-Botsman", 2),
    ("Forensic-Architecture-Bucha-SBU",
     "https://forensic-architecture.org/", "V191-SBU-Botsman", 2),
    ("Ukrainian-Ombudsman-Post-Withdrawal-Audit",
     "https://ombudsman.gov.ua/en/", "V191-SBU-Botsman", 2),
    # -- Thématique CPI asymétrie (V192) --
    ("ICC-Rome-Statute-2002",
     "https://www.icc-cpi.int/sites/default/files/RS-Eng.pdf", "V192-CPI", 1),
    ("Karim-Khan-Warrant-Poutine-2023-03-17",
     "https://www.icc-cpi.int/news/statement-prosecutor-karim-khan-kc-issuance-arrest-warrants-against-president-vladimir-putin", "V192-CPI", 1),
    ("ICC-Investigation-UA-2022-04-28",
     "https://www.icc-cpi.int/news/ukraine-investigation", "V192-CPI", 1),
    ("Ukraine-RADA-Declaration-2014-02-21",
     "https://zakon.rada.gov.ua/laws/show/962-18", "V192-CPI", 1),
    ("Ukraine-RADA-Second-Declaration-2015-09-08",
     "https://zakon.rada.gov.ua/laws/show/617-19", "V192-CPI", 2),
    ("Russia-Withdrawal-Rome-Statute-2016-11-30",
     "https://www.icc-cpi.int/rs", "V192-CPI", 2),
    ("Karim-Khan-Personal-Jurisdiction-doctrine-Article-12-2-b",
     "https://www.icc-cpi.int/sites/default/files/RS-Eng.pdf", "V192-CPI", 1),
    # -- Thématique Marioupol-Amnesty (V193) --
    # Amnesty-Twomey (officiellement Amnesty-International-rapport-militarisation-Ukraine) ; URL-vérifié-researcher-web-2026-07-11
    ("Amnesty-Twomey-Rapport-Militarisation-juin-2022",
     "https://www.amnesty.org/en/latest/news/2022/08/ukraine-ukrainian-fighting-tactics-endanger-civilians/", "V193-Marioupol", 1),
    ("Amnesty-Callamard-Apology-juillet-2022-Officiel",
     "https://www.amnesty.org/en/latest/news/2022/08/urging-ukrainian-authorities-investigate-claims/", "V193-Marioupol", 1),
    ("Amnesty-Press-Release-2022-06-30",
     "https://www.amnesty.org/en/latest/news/", "V193-Marioupol", 2),
    ("Amnesty-Callamard-Apology-juillet-2022",
     "https://www.amnesty.org/en/latest/news/", "V193-Marioupol", 1),
    ("BBC-Marioupol-Theatre-Bombing-2022-03-16",
     "https://www.bbc.com/news/world-europe-mar", "V193-Marioupol", 1),
    ("OSCE-ODIHR-Marioupol-Mission-2022",
     "https://www.osce.org/odihr/", "V193-Marioupol", 2),
    ("MFA-UA-Marioupol-Theatre-Anthme-@-FETCH",
     "https://mfa.gov.ua/en", "V193-Marioupol", 2),
    ("Ukraine-Azov-Statement-Anthme-@-FETCH",
     "https://azov.org.ua/en/", "V193-Marioupol", 2),
    ("Russia-MoD-Statement-Anthme-@-FETCH",
     "https://function.mil.ru/news_page/", "V193-Marioupol", 3),
    # -- Thématique Crossfire médiatique NYT-Irpin (V194-V196) --
    ("NYT-Coverage-Retractions-Anthme-@-FETCH",
     "https://www.nytimes.com/", "V194-NYT", 1),
    ("WSJ-Precision-Irpin-Bridge-Anthme-@-FETCH",
     "https://www.wsj.com/", "V195-Irpin", 1),
    ("NYT-Kostiantynivka-Iskander-Anthme-@-FETCH",
     "https://www.nytimes.com/", "V196-Kostiantynivka", 1),
    # -- Thématique Oliver Stone Ukraine on Fire (V197) --
    ("IMDB-Oliver-Stone-Ukraine-on-Fire-Archive",
     "https://www.imdb.com/title/tt5769416/", "V197-Documentaire-Stone", 1),
    ("NYT-Critique-Oliver-Stone-Ukraine",
     "https://www.nytimes.com/", "V197-Documentaire-Stone", 1),
    ("Hollywood-Reporter-Critique-Oliver-Stone",
     "https://www.hollywoodreporter.com/", "V197-Documentaire-Stone", 1),
    ("Variety-Review-Oliver-Stone-Ukraine",
     "https://variety.com/", "V197-Documentaire-Stone", 1),
    ("Alcr-Monitor-2024-Oliver-Stone-Omerta",
     "https://www.acrimed.org/", "V197-Documentaire-Stone", 1),
    ("Russia-Today-RT-Oliver-Stone-Promotion-Anthme-@-FETCH",
     "https://www.rt.com/", "V197-Documentaire-Stone", 3),
    ("Igor-Lopatonok-Interview-Defense-Anthme-@-FETCH",
     "https://www.youtube.com/", "V197-Documentaire-Stone", 2),
    # -- Thématique 14 juillet 2026 (V154-V166) --
    ("LeMonde-Bucha-2022",
     "https://www.lemonde.fr/", "V190-Bucha", 2),
    ("RFI-Bucha-2022",
     "https://www.rfi.fr/fr/", "V190-Bucha", 2),
    ("Alcr-Monitor-2024-Bucha-Omission-A8",
     "https://www.acrimed.org/", "V190-Bucha", 2),
    ("Le-Monde-Diplomatique-Asymetrie-CPI-A8-A7",
     "https://www.monde-diplomatique.fr/", "V192-CPI", 2),
    ("Press-FR-Blackout-1958-Cycle-A8",
     "https://www.acrimed.org/", "V190-V193-A8", 2),
]

# Patterns extraction : @FETCH-markers in investigation files
F_FETCH_LINE = re.compile(r"^.*@FETCH", flags=re.MULTILINE)
F_FETCH_KEY = re.compile(r"@FETCH[\(\[][^\)\]]+[\)\]]")
F_KEY_NAME = re.compile(r"\b([A-Z][A-Za-z0-9-]{4,})-(?:Anthme-)?@ ?FETCH\b")
F_F_NUMBER = re.compile(r"\bF-\d+\b")
F_M_NUMBER = re.compile(r"\bM[1-9]\b")


@dataclass
class CanonKey:
    """Une clé canonique @FETCH à résoudre pour Verrou-B.

    Conformité KERNEL §1 step 10 : URL précise (page spécifique).
    Les clés sans URL-spécifique sont marquées needs_llm_resolve=True
    et bloquées pour publication Tier-1 (cf. §10 VALIDATION :
    IF URL points to domain root → mark ⁅ (gap)).
    """

    key: str
    url_hint: str
    source_paper: str
    tier_priority: int  # 1=haute, 2=moyenne, 3=basse
    thematic: str = ""
    presence: list[str] = field(default_factory=list)  # files containing this key
    url_resolved: str = ""  # URL after --resolve HEAD-req
    http_status: int = 0
    fetch_status: str = "PENDING"  # PENDING | OK | 403 | 404 | ERROR | SKIPPED
    needs_llm_resolve: bool = False  # True = URL-hint trop-generique OU absente
    resolve_strategy: str = "@WEB-search-priority-1-2-3-4-BY-LLM-AGENT"
    a4_warning: str = ""  # Anti-conspiration advisory (optional)
    fabrication_alert: bool = False  # True = source not_found-in-official-literature
    fabrication_status: str = ""  # "CLAIMED" | "δ-GAP" | "fabrication-suspected" | "fabrication-prouvé"


def classify_thematic(source_paper: str) -> str:
    """Déduit la thématique depuis le tag source-paper via split -V1xx-boundary.

    Fix code-reviewer 2026-07-11 : l'ancien startswith classait V190-V192
    comme Forensique-terrain-Bucha alors qu'il vise CPI. Nouveau : split
    sur première borne -V1\\d+ pour match exact du paper principal.
    """
    m = re.match(r"^V1(\d{2})", source_paper)
    if m:
        vnum = int(m.group(1))
        _DISPATCH = {
            90: "Forensique-terrain-Bucha-V190",
            91: "Repr\u00e9sailles-UA-V191",
            92: "CPI-Asym\u00e9trie-V192",
            93: "Marioupol-Amnesty-V193",
            94: "Crossfire-NYT-V194",
            95: "Irpin-Bridge-V195",
            96: "Kostiantynivka-Iskander-V196",
            97: "Documentaire-Stone-V197",
        }
        return _DISPATCH.get(vnum, "Cross-th\u00e9matique")
    return "Cross-th\u00e9matique"


def needs_llm_resolve(url_hint: str) -> bool:
    """Détermine si une URL-hint viole KERNEL §1 step 10 (page-spécifique).

    Page-racine (homepage, search-page-API, news-index) est marque ⁅(gap).
    URL-précise (chemin-spécifique, publication, document-path) est OK.
    Fix code-reviewer 2026-07-11 : identifie homepage-racines + domains-génériques.
    """
    if not url_hint:
        return True
    homepage_indicators = [
        "https://www.nytimes.com/",
        "https://www.hollywoodreporter.com/",
        "https://variety.com/",
        "https://www.acrimed.org/",
        "https://www.lemonde.fr/",
        "https://www.rfi.fr/",
        "https://azov.org.ua/en/",
        "https://mfa.gov.ua/en",
        "https://www.rt.com/",
        "https://www.youtube.com/",
        "?query=",  # search-pages-Bing/DDG
    ]
    if any(ind in url_hint for ind in homepage_indicators):
        return True
    # Trop court (longueur < 40 caractères) sans chemin spécifique
    if len(url_hint) < 40 and "/" not in url_hint.split("?")[0][8:]:
        return True
    return False


def crawl_target(target_dir: Path, key_lookup: dict[str, list[CanonKey]]) -> None:
    """Crawl les fichiers V154-V253 et les SYNTHESE pour remplir key.lookup."""
    if not target_dir.is_dir():
        print(f"ERREUR : dossier introuvable : {target_dir}", file=sys.stderr)
        sys.exit(1)
    files = sorted(target_dir.glob("*.md"))
    inv_files = [f for f in files if "_V" in f.name if "SYNTHESE" not in f.name.upper()]
    synt_files = [f for f in files if "SYNTHESE" in f.name.upper()]
    file_list = inv_files + synt_files
    print(f"--- CRAWL : {len(inv_files)} INV + {len(synt_files)} SYNTHESE = {len(file_list)} ---", file=sys.stderr)
    for fp in file_list:
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            print(f"WARN : lecture impossible : {fp.name} : {exc}", file=sys.stderr)
            continue
        for k in key_lookup:
            # normalized match
            key_norm = k.replace("-Anthme-@-FETCH", "-Anthme").replace("-@-FETCH", "")
            if key_norm in text:
                key_lookup[k].append(fp.name)


def build_manifest_keys() -> list[CanonKey]:
    """Construit la liste CanonKey depuis CANON_KEYS canonique.

    Fix code-reviewer 2026-07-11 : marque needs_llm_resolve=True pour les
    URL-hints homepage-root qui violent KERNEL §1 step 10.
    """
    A4_WARNING_TIER3 = (
        "Tier-3 = sources à utiliser SEULEMENT avec cross-check A4-anti-conspiration. "
        "Russia-MoD + RT biaisés par doctrine Kremlin."
    )
    # Clés-marquées-fabrication-suspected-par-researcher-web-2026-07-11
    FABRICATION_ALERT_KEYS = {
        "Muller-Hertz-Scientific-Report-2024-Autopsies-458-corps": "δ-définitif-prouvé-fabrication-suspected-3-sources-concordant-2026-07-11",
        "Muller-Hertz-Bellingcat-Investigation-2022-Autopsies-458-corps": "δ-définitif-prouvé-fabrication-suspected-3-sources-concordant-2026-07-11",
    }
    manifest: list[CanonKey] = []
    for (key, url, paper, priority) in CANON_KEYS:
        ck = CanonKey(
            key=key,
            url_hint=url,
            source_paper=paper,
            tier_priority=priority,
            thematic=classify_thematic(paper),
            needs_llm_resolve=needs_llm_resolve(url),
        )
        if priority == 3:
            ck.a4_warning = A4_WARNING_TIER3
        if key in FABRICATION_ALERT_KEYS:
            ck.fabrication_alert = True
            ck.fabrication_status = FABRICATION_ALERT_KEYS[key]
        manifest.append(ck)
    return manifest


def resolve_url(ck: CanonKey, timeout: float = 4.0, exc_429_count: int = 0) -> tuple[CanonKey, int]:
    """Tente un HEAD-req urllib sur url_hint de la CanonKey.

    KERNEL-compliance :
      - 200-399 → OK
      - 403/405 → HEAD parfois bloqué : OK partiel (laissera LLM GET)
      - 429 → stop immédiat (KERNEL rule "NEVER retry after 429")
      - 404 / autres → enregistrée pour révision
      - URL absente ou homepage-root → skip, needs_llm_resolve

    Returns (CanonKey, exc_429_count) — compteur cumulé sur batch.
    """
    if not ck.url_hint or ck.needs_llm_resolve:
        ck.fetch_status = "SKIPPED-LLM-RESOLVE"
        return ck, exc_429_count
    req = urllib.request.Request(ck.url_hint, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ck.http_status = resp.status
            ck.fetch_status = "OK" if 200 <= resp.status < 400 else f"HTTP {resp.status}"
    except urllib.error.HTTPError as e:
        ck.http_status = e.code
        if e.code == 429:
            ck.fetch_status = "429-RATE-LIMITED"
            exc_429_count += 1
        elif e.code in (403, 405):
            ck.fetch_status = "OK-HEAD-BLOCKED"
        elif e.code == 404:
            ck.fetch_status = "404-NOT-FOUND"
        else:
            ck.fetch_status = f"HTTP {e.code}"
    except urllib.error.URLError:
        ck.fetch_status = "ERROR-URL"
    except Exception:
        ck.fetch_status = "ERROR-UNKNOWN"
    return ck, exc_429_count


def cleanup_cascade_text(text: str, runs: int = 10) -> str:
    """Anti-cascade cleanup : collapse 3+ repeats du meme token (cycle-cycle, etc).

    Pattern type V176-V197 :
        - run Anti collapse `(TOKEN-?){3,}` -> TOKEN
        - run `\bTOKEN\b + whitespace + TOKEN\b` -> TOKEN
    Returns cleaned text + iteration stats.
    """
    cascade_tokens = [
        "Anti", "distinct", "cross", "pure", "canon", "cycle",
        "Official", "Officiel", "Cross", "Cycle", "FIN",
        "canonical", "topic", "pivot", "Bipartisan", "Section",
        "Maidan", "Marioupol", "Irpin", "Kostiantynivka", "Oliver",
        "Stone", "coherent", "coh\u00e9rent", "Cycle",
    ]
    prev = None
    total_iter = 0
    while prev != text and total_iter < runs:
        prev = text
        total_iter += 1
        for tok in cascade_tokens:
            # Triple repeat with optional hyphen
            text = re.sub(rf"({re.escape(tok)}-?){{3,}}", tok, text)
            # Token + whitespace + same Token
            text = re.sub(rf"\b({re.escape(tok)})\s+(?=\1)", "", text)
        # Iteration-3 fallback on stubborn short repeats (ws/hyphen)
        text = re.sub(r"\b(\w+)(?:[-\s]\s*\1){2,}", r"\1", text)
    return text


def render_json(manifest: list[CanonKey]) -> str:
    """Sérialise la manifest en JSON."""
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "cycle": "V154-V253",
        "manifest_version": "v1",
        "n_keys_total": len(manifest),
        "n_by_tier": {
            "1-haute": sum(1 for k in manifest if k.tier_priority == 1),
            "2-moyenne": sum(1 for k in manifest if k.tier_priority == 2),
            "3-basse": sum(1 for k in manifest if k.tier_priority == 3),
        },
        "keys": [asdict(k) for k in manifest],
    }
    return json.dumps(out, ensure_ascii=False, indent=2)


def render_markdown(manifest: list[CanonKey]) -> str:
    """Sérialise la manifest en Markdown human-readable prioritisable."""
    lines: list[str] = []
    lines.append("# @FETCH Manifest — Verrou-B Cycle V154-V253")
    lines.append("")
    lines.append(f"**G\u00e9n\u00e9r\u00e9 le** : {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"**Cycle** : V154-V253 (12-topic-papers-pr\u00e9vus)")
    lines.append(f"**Cl\u00e9s totales** : {len(manifest)}")
    lines.append("")
    lines.append("## Strat\u00e9gie d'orchestration (cf. KERNEL.md search priority)")
    lines.append("")
    lines.append(
        "1. `@MNEMO_Q` \u2192 local DB (rapide)\n"
        "2. `@WEB`     \u2192 DuckDuckGo (souple)\n"
        "3. `@FETCH`   \u2192 URL directe (ce script orchestre via --resolve)\n"
        "4. `@EXA`     \u2192 LAST RESORT (rate-limited 429)"
    )
    lines.append("")
    lines.append("**Tier-priority** :")
    lines.append("- **Tier 1 (haute)** : ex\u00e9cuter AVANT tous (ex. Muller-Hertz, Karim-Khan)")
    lines.append("- **Tier 2 (moyenne)** : ex\u00e9cuter en parall\u00e8le")
    lines.append("- **Tier 3 (basse)** : ex\u00e9cuter apr\u00e8s (ex. Russia-MoD, RT)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Manifest prioritis\u00e9 (Tier 1 \u2192 Tier 3)")
    lines.append("")
    by_thematic: dict[str, list[CanonKey]] = {}
    for k in sorted(manifest, key=lambda c: (c.tier_priority, c.thematic, c.key)):
        by_thematic.setdefault(k.thematic, []).append(k)
    for them in sorted(by_thematic.keys()):
        lines.append(f"### Th\u00e9matique : {them}")
        lines.append("")
        for ck in by_thematic[them]:
            tier_span = ""
            tier_span = "1 (haute)" if ck.tier_priority == 1 else (
                "2 (moyenne)" if ck.tier_priority == 2 else "3 (basse)"
            )
            status = ck.fetch_status
            status_str = f"HTTP {ck.http_status}" if ck.http_status else status
            presence_count = len(ck.presence)
            mini_presence = ", ".join(set(p[:30] for p in sorted(set(ck.presence))[:3]))
            lines.append(f"- **Tier {tier_span}** | `{ck.key}`")
            lines.append(f"  - URL hint: {ck.url_hint or '(none)'}")
            lines.append(f"  - Source-paper: {ck.source_paper}")
            lines.append(f"  - Fetch status: `{status_str}`")
            lines.append(f"  - Presence ({presence_count} files): {mini_presence}")
            lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Action manuelle requise par le pilote LLM (Codebuff)")
    lines.append("")
    lines.append(
        "Pour chaque cl\u00e9 Tier 1 (priorit\u00e9 haute) :\n"
        "1. V\u00e9rifier URL hint via `--resolve`\n"
        "2. Si OK : appeler `@webfetch(url=URL_RESOLVED, format='markdown')`\n"
        "3. Sauvegarder le r\u00e9sultat dans outputs/fetch_cache/<key>.md\n"
        "4. Lancer Tier 2 en parall\u00e8le (multi-basher subagents)\n"
        "5. Apr\u00e8s tous Tier 1+2 : tester Tier 3 (sources \u00e9ventuellement biaisees)\n"
    )
    lines.append("**Stop-condition** : 429 sur Tier 3 \u2192 STOP Tier 3, continuer Tier 1+2.")
    lines.append("")
    return "\n".join(lines)


def scan_mode(target_dir: Path) -> list[CanonKey]:
    """Mode scan : extrait + crawl + stdout (lisible humain)."""
    manifest = build_manifest_keys()
    key_lookup: dict[str, list[CanonKey]] = {
        ck.key: ck for ck in manifest
    }
    # Crawl fill .presence
    files = sorted(target_dir.glob("*.md"))
    for fp in files:
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
            key_norm = lambda k: k.replace("-Anthme-@-FETCH", "-Anthme").replace("-@-FETCH", "")
            for ck in manifest:
                if key_norm(ck.key) in text:
                    ck.presence.append(fp.name)
        except Exception as exc:
            print(f"WARN : {fp.name} : {exc}", file=sys.stderr)
    # Standout : TOP-15 prioritaire
    print(f"--- CANON_KEYS-CRAWL : {len(manifest)} cl\u00e9s ---", file=sys.stderr)
    for ck in sorted(manifest, key=lambda c: (c.tier_priority, c.key)):
        print(f"T{ck.tier_priority} | {len(ck.presence):3d} presence | {ck.key[:60]:60s} | paper={ck.source_paper}")
    return manifest


def manifest_mode(
    target_dir: Path,
    output_dir: Path,
) -> int:
    """Mode manifest : scan + write JSON + Markdown."""
    manifest = scan_mode(target_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{DEFAULT_OUTPUT_PREFIX}.json"
    md_path = output_dir / f"{DEFAULT_OUTPUT_PREFIX}.md"
    json_path.write_text(render_json(manifest), encoding="utf-8")
    md_path.write_text(render_markdown(manifest), encoding="utf-8")
    write_fabrication_log(manifest)
    print(f"JSON \u00e9crit : {json_path}", file=sys.stderr)
    print(f"Markdown \u00e9crit : {md_path}", file=sys.stderr)
    return 0


def resolve_mode(target_dir: Path, output_dir: Path, limit: int | None = None) -> int:
    """Mode resolve : scan + manifest + HEAD-req urllib (Tier 1 prioritaires).

    KERNEL-429-rule : compteur cumulé ; STOP-PROC après 3+ hits 429
    (cf. KERNEL.md "RULE: NEVER retry same query on Exa after 429" +
    "IF @EXA returns 429 → STOP using Exa, continue with @WEB/@FETCH only").
    """
    manifest = scan_mode(target_dir)
    tier1 = [k for k in manifest if k.tier_priority == 1 and not k.needs_llm_resolve]
    print(f"--- RESOLVE : {len(tier1)} Tier-1 HEAD-req (skip homepage-root markées) ---", file=sys.stderr)
    if limit:
        tier1 = tier1[:limit]
    exc_429_count = 0
    for ck in tier1:
        ck, exc_429_count = resolve_url(ck, exc_429_count=exc_429_count)
        print(f"  T1 | HTTP {ck.http_status} | {ck.fetch_status:20s} | {ck.key[:55]}")
        if exc_429_count >= 3:
            print(f"--- STOP : 3+ cumuls 429 — respecting KERNEL-rule-429-STOP ---", file=sys.stderr)
            for ck_left in tier1[tier1.index(ck) + 1:]:
                ck_left.fetch_status = "429-STOPPED-RATE-LIMIT"
            break
    # Re-render outputs
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{DEFAULT_OUTPUT_PREFIX}.json"
    md_path = output_dir / f"{DEFAULT_OUTPUT_PREFIX}.md"
    json_path.write_text(render_json(manifest), encoding="utf-8")
    md_path.write_text(render_markdown(manifest), encoding="utf-8")
    print(f"--- JSON + Markdown mis \u00e0 jour ; 429 hits total : {exc_429_count} ---", file=sys.stderr)
    return 0


def full_mode(target_dir: Path, output_dir: Path) -> int:
    """Mode full : scan + manifest + resolve Tier 1."""
    return resolve_mode(target_dir, output_dir, limit=None)


FABRICATION_LOG_PATH = PROJECT_ROOT / "outputs" / "fabrication_log.md"


def write_fabrication_log(manifest):
    """Cree/ecrit outputs/fabrication_log.md avec alertes fabrication-prouvees V154-V253."""
    FAB_LOG = FABRICATION_LOG_PATH
    FAB_LOG.parent.mkdir(parents=True, exist_ok=True)
    alert_keys = [k for k in manifest if k.fabrication_alert]
    lines = []
    lines.append("# Fabrication Log Verrou-B V154-V253")
    lines.append("")
    lines.append("Genere le: " + datetime.now(timezone.utc).isoformat())
    lines.append("")
    lines.append("## Alerte fabrication-prouvee delta (3-researcher-web-concordant 2026-07-11)")
    lines.append("")
    if not alert_keys:
        lines.append("(aucune alerte-fabrication)")
    else:
        for ak in alert_keys:
            lines.append("### ALERT: " + ak.key)
            lines.append("")
            lines.append("- Status: " + str(ak.fabrication_status))
            lines.append("- Source-paper: " + str(ak.source_paper))
            url_hint = ak.url_hint if ak.url_hint else "(empty)"
            lines.append("- URL-hint-dans-CANON_KEYS: " + url_hint)
            lines.append("")
            lines.append("Contexte-recherche-web (3-researcher-web-concordant 2026-07-11):")
            lines.append("- UN-OHCHR / HRW / ICC-OTP / Council of Europe / MSF / ICRC / OSCE-ODIHR / Amnesty / NYT / Reuters / Guardian / BBC / Bellingcat : aucune mention d'un rapport-nominal-Muller-Hertz-dans-lit-medicale-legale-officielle-Bucha.")
            lines.append("- 458-corps-quantity : official (Ukrainian municipal authorities 2022).")
            lines.append("- flechettes/darts-usage-par-artillerie-russe : official (Reuters/Guardian 2022).")
            lines.append("- Cat-A-mixed-60-70%-russes + Cat-B-flechettes-UA-30-40% : delta-definitif-prouve (aucune nomenclature-officielle-supportant-cette-mixed-distribution).")
            lines.append("")
            lines.append("Indications-Action-prealable-publication-Tier-1:")
            lines.append("1. delta-MARQUAGE-definitif : la cle NE-peut-pas-utilisee-comme-preuve-V190-prealable-Tier-1-publication-press-FR-canonique.")
            lines.append("2. Action-cycle-V190-regeneration : regenerer-V190-préalable-Tier-1-publication-cycle-uniform-V154-V253 (remplacer-mixed-60-70%-Cat-A-russes+30-40%-Cat-B-flechettes par-PELOTE-3-facteurs-prouvés : 458-corps-official + usage-flechettes-officiel + absence-classification-officielle).")
            lines.append("3. Synchronisation-V190-regeneration : propager-remplacement-V191-V192-V193-V194-V195-V196-V197-SYNTHESE-V190-V193-SYNTHESE-V194-V196-SYNTHESE-V197-prealable-publication-press-FR-canonique.")
            lines.append("")
    FAB_LOG.write_text("\n".join(lines), encoding="utf-8")
    print("FABRICATION-LOG ecrit : " + str(FAB_LOG), file=sys.stderr)


def cleanup_self_mode(script_path: Path) -> int:
    """Mode cleanup-self : applique anti-cascade cleanup sur le script."""
    text = script_path.read_text(encoding="utf-8")
    before = len(text)
    cleaned = cleanup_cascade_text(text)
    after = len(cleaned)
    delta = before - after
    if delta > 0:
        script_path.write_text(cleaned, encoding="utf-8")
        print(f"CLEANUP appliqu\u00e9 : {delta} octets r\u00e9duits ({before} \u2192 {after})", file=sys.stderr)
    else:
        print(f"CLEANUP n\u00e9gligeable : 0 octets (d\u00e9j\u00e0 propre)", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch Canoniques - orchestrateur @FETCH multi-cl\u00e9s (Verrou-B V154-V253)",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan", help="extrait cl\u00e9s, dump stdout")
    p_scan.add_argument("-d", "--dir", type=Path, default=DEFAULT_TARGET_DIR)

    p_man = sub.add_parser("manifest", help="scan + outputs/fetch_manifest_v154_v253.{json,md}")
    p_man.add_argument("-d", "--dir", type=Path, default=DEFAULT_TARGET_DIR)
    p_man.add_argument("-o", "--out", type=Path, default=DEFAULT_OUTPUT_DIR)

    p_res = sub.add_parser("resolve", help="scan + manifest + HEAD-req urllib Tier 1")
    p_res.add_argument("-d", "--dir", type=Path, default=DEFAULT_TARGET_DIR)
    p_res.add_argument("-o", "--out", type=Path, default=DEFAULT_OUTPUT_DIR)
    p_res.add_argument("-l", "--limit", type=int, default=None, help="limiter N HEAD-req")

    p_full = sub.add_parser("full", help="scan + manifest + resolve (sans limit)")
    p_full.add_argument("-d", "--dir", type=Path, default=DEFAULT_TARGET_DIR)
    p_full.add_argument("-o", "--out", type=Path, default=DEFAULT_OUTPUT_DIR)

    p_clean = sub.add_parser("cleanup-self", help="anti-cascade cleanup sur le script lui-meme")
    p_clean.add_argument(
        "-s", "--script", type=Path,
        default=Path(__file__).resolve(),
        help=f"chemin du script (default: {__file__})",
    )

    args = parser.parse_args()

    if args.cmd == "scan":
        scan_mode(args.dir)
        return 0
    if args.cmd == "manifest":
        return manifest_mode(args.dir, args.out)
    if args.cmd == "resolve":
        return resolve_mode(args.dir, args.out, args.limit)
    if args.cmd == "full":
        return full_mode(args.dir, args.out)
    if args.cmd == "cleanup-self":
        return cleanup_self_mode(args.script)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
