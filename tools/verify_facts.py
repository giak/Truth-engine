#!/usr/bin/env python3
"""verify_facts.py — Vérificateur déterministe du registre des faits (P1).

Parse le bloc FACT_REGISTRY_V1 d'un dossier d'investigation et applique les gates :
  - ✦ exige EPI=FACT (jamais INFERENCE/HYPOTHESIS/SPECULATION) ;
  - ✦ exige >=2 familles de provenance indépendantes (A/B/C/D/E) ;
  - ✦ exige une URL http(s) sûre (anti-SSRF) qui répond (200-399, ou 403/405 = HEAD bloqué) ;
  - ✧ = source unique (URL requise) ; ⁅ = URL morte ; ❧ = pas d'URL (constat, non bloquant sauf ✦).

Ce script vérifie la STRUCTURE (URL vivante, familles, classe EPI, tier), pas la VÉRITÉ du
contenu. La vérité reste un jugement (fetch + lecture + gate humaine). Cf. AGENTS.md §4.

Sortie : rapport + code retour 0 (tout passe) / 1 (violations) / 2 (aucun registre trouvé).
Usage :
  python3 tools/verify_facts.py <investigation.md> [--timeout N] [--offline]
  --offline : saute les HEAD-check réseau (tests déterministes sans réseau).
"""

import ipaddress
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request

ALLOWED_SCHEMES = {"http", "https"}
DEFAULT_TIMEOUT = 5
MIN_TIMEOUT = 1
MAX_TIMEOUT = 30

FACT_REGISTRY_START = "<!-- FACT_REGISTRY_V1 -->"
FACT_REGISTRY_END = "<!-- /FACT_REGISTRY_V1 -->"

EPI_CLASSES = {"FACT", "EVIDENCE", "INFERENCE", "HYPOTHESIS", "SPECULATION", "UNKNOWN"}
TIERS = {"✦", "✧", "⁅", "❧"}
PROVENANCE_FAMILIES = set("ABCDE")

# Un ✦ avec un de ces statuts est une source morte : violation.
DEAD_STATUS = {404, 410, 451, 500, 502, 503, 504}
# HEAD bloqué mais la page existe probablement : accepté (le LLM fera un GET).
BLOCKED_OK_STATUS = {403, 405, 429}


def _is_safe_ip(ip_str):
    """Bloque loopback, privé, lien-local, multicast, non-spécifié, réservé, CGN."""
    try:
        ip = ipaddress.ip_address(ip_str)
    except ValueError:
        return False
    mapped = getattr(ip, "ipv4_mapped", None)
    if mapped is not None:
        ip = mapped
    if (ip.is_loopback or ip.is_private or ip.is_link_local
            or ip.is_multicast or ip.is_unspecified or ip.is_reserved):
        return False
    if ip.version == 4 and ip in ipaddress.ip_network("100.64.0.0/10"):
        return False
    return True


def _validate_url(url):
    """(safe, reason). Vérifie scheme + hostname + IP (anti-SSRF), sans requête."""
    if not url:
        return False, "empty_url"
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        return False, "parse_error"
    if parsed.scheme.lower() not in ALLOWED_SCHEMES:
        return False, "scheme_not_allowed"
    if not parsed.hostname:
        return False, "no_hostname"
    host = parsed.hostname
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None
    if literal is not None:
        if not _is_safe_ip(str(literal)):
            return False, "unsafe_ip:{0}".format(literal)
        return True, None
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False, "dns_error"
    for info in infos:
        addr = info[4][0]
        if not _is_safe_ip(addr):
            return False, "unsafe_ip:{0}".format(addr)
    return True, None


def head_check(url, timeout=DEFAULT_TIMEOUT):
    """HEAD-req sur une URL publique. Retourne le code HTTP (int) ou None (refus/erreur)."""
    t = MIN_TIMEOUT if (timeout is None or timeout <= 0) else min(timeout, MAX_TIMEOUT)
    safe, _reason = _validate_url(url)
    if not safe:
        return None
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "verify-facts/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=t) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def extract_registry(text):
    """Retourne la liste des lignes du bloc FACT_REGISTRY_V1, ou []."""
    if FACT_REGISTRY_START not in text:
        return []
    start = text.index(FACT_REGISTRY_START) + len(FACT_REGISTRY_START)
    end = text.index(FACT_REGISTRY_END, start) if FACT_REGISTRY_END in text[start:] else len(text)
    return [ln.strip() for ln in text[start:end].splitlines() if ln.strip()]


def parse_line(line):
    """id, epi, tier, url, families, date — None si ligne mal formée."""
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 5:
        return None
    fid, epi, tier, url, families = parts[0], parts[1], parts[2], parts[3], parts[4]
    date = parts[5] if len(parts) > 5 else ""
    return fid, epi, tier, url, families, date


def _families(spec):
    return [f for f in spec.replace("-", "").split(",") if f.strip() in PROVENANCE_FAMILIES]


def verify_record(rec, offline=False):
    """Vérifie un enregistrement. Retourne une liste de violations (str)."""
    issues = []
    fid, epi, tier, url, families, _date = rec
    if not re.fullmatch(r"FCT-\d+", fid):
        issues.append("id invalide : {0}".format(fid))
    if epi not in EPI_CLASSES:
        issues.append("EPI inconnue : {0}".format(epi))
    if tier not in TIERS:
        issues.append("tier inconnu : {0}".format(tier))
        return issues
    fams = _families(families)
    has_url = url and url != "-"

    if tier == "✦":
        if epi != "FACT":
            issues.append("✦ sur EPI={0} (seul FACT peut être ✦)".format(epi))
        if len(fams) < 2:
            issues.append("✦ avec {0} famille(s) (<2 familles indépendantes)".format(len(fams)))
        if not has_url:
            issues.append("✦ sans URL")
        elif not offline:
            code = head_check(url)
            if code is None:
                issues.append("✦ URL unsafe ou injoignable : {0}".format(url))
            elif code in DEAD_STATUS:
                issues.append("✦ URL morte (HTTP {0}) : {1}".format(code, url))
            elif code not in BLOCKED_OK_STATUS and not (200 <= code < 400):
                issues.append("✦ URL statut inattendu (HTTP {0}) : {1}".format(code, url))
    elif tier == "✧" and not has_url:
        issues.append("✧ sans URL")
    return issues


def verify_text(text, offline=False):
    """Retourne (records, results) où results = {fid: [issues]}."""
    lines = extract_registry(text)
    if not lines:
        return [], {}
    results = {}
    for ln in lines:
        rec = parse_line(ln)
        if rec is None:
            results.setdefault("_parse", []).append("ligne mal formée : {0}".format(ln))
            continue
        issues = verify_record(rec, offline=offline)
        if issues:
            results[rec[0]] = issues
    return lines, results


def report(lines, results):
    if not lines:
        print("AUCUN REGISTRE TROUVÉ : bloc {0} absent.".format(FACT_REGISTRY_START))
        return 2
    if not results:
        print("OK : {0} faits, zéro violation.".format(len(lines)))
        return 0
    n_bad = 0
    for fid, issues in results.items():
        for issue in issues:
            n_bad += 1
            print("VIOLATION [{0}] {1}".format(fid, issue))
    print("{0} violation(s) sur {1} faits.".format(n_bad, len(lines)))
    return 1


def main(argv):
    args = [a for a in argv[1:]]
    if not args:
        print(__doc__)
        return 2
    path = args[0]
    offline = "--offline" in args
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as e:
        print("ERREUR lecture {0} : {1}".format(path, e))
        return 2
    lines, results = verify_text(text, offline=offline)
    return report(lines, results)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
