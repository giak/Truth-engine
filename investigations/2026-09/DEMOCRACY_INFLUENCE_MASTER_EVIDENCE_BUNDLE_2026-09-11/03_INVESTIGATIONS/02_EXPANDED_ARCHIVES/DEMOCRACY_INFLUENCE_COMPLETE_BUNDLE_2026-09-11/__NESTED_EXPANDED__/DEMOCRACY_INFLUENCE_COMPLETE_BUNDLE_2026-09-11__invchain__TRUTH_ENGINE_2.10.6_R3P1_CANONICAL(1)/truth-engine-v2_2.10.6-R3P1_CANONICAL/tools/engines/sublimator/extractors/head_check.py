"""head_check.py — HEAD-check durci anti-SSRF (Sublimator v2.0).

Vérifie la vivacité d'une URL sans s'exposer au SSRF :
- F1 : scheme whitelist {http, https} uniquement ;
- F2 : blocklist IP (loopback, private, link-local, metadata, CGN, unspecified,
  multicast, IPv4-mapped, IPv6 loopback/ULA/link-local/documentation) ;
- F3 : redirects validés (blocage des redirects vers IP non-safe) ;
- F4 : IPv6 brackets refusés quand l'IP sous-jacente est non-safe ;
- F5 : clamp de timeout (MIN_TIMEOUT..MAX_TIMEOUT) ;
- F6 : résolution DNS pré-connexion (getaddrinfo) ; limitation rebinding documentée.
"""

import ipaddress
import socket
import urllib.error
import urllib.parse
import urllib.request

# F1 : seuls http/https sont autorisés.
ALLOWED_SCHEMES = {"http", "https"}

# F5 : clamp de timeout.
MIN_TIMEOUT = 1
DEFAULT_TIMEOUT = 5
MAX_TIMEOUT = 30


def _is_safe_ip(ip: str) -> bool:
    """F2 : True si l'IP est publique et non-réservée, False sinon."""
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False

    # Normaliser les IPv6 "IPv4-mapped" (::ffff:a.b.c.d) vers IPv4.
    if isinstance(addr, ipaddress.IPv6Address) and addr.ipv4_mapped is not None:
        addr = addr.ipv4_mapped

    if (
        addr.is_unspecified      # 0.0.0.0, ::
        or addr.is_loopback      # 127/8, ::1
        or addr.is_link_local    # 169.254/16, fe80::/10
        or addr.is_multicast     # 224/4, ff00::/8
        or addr.is_private       # 10/8, 172.16/12, 192.168/16, fc00::/7
        or addr.is_reserved      # 240/4, TEST-NET, benchmark
    ):
        return False

    if isinstance(addr, ipaddress.IPv4Address):
        # 0.0.0.0/8 ("this network") et CGN 100.64/10 (Carrier-Grade NAT).
        if addr in ipaddress.ip_network("0.0.0.0/8"):
            return False
        if addr in ipaddress.ip_network("100.64.0.0/10"):
            return False
    else:
        # IPv6 documentation (2001:db8::/32) et discard-only (100::/64).
        if addr in ipaddress.ip_network("2001:db8::/32"):
            return False
        if addr in ipaddress.ip_network("100::/64"):
            return False

    return True


def _validate_url(url):
    """Retourne (safe: bool, reason: str|None).

    F2 : empty_url / scheme_not_allowed / no_hostname / unsafe_ip / dns_error.
    F6 : résolution pré-connexion via getaddrinfo (chaque IP résolue est contrôlée).
    """
    if not url:
        return (False, "empty_url")

    try:
        parsed = urllib.parse.urlparse(url)
    except (ValueError, TypeError):
        return (False, "invalid_url")

    if parsed.scheme.lower() not in ALLOWED_SCHEMES:
        return (False, f"scheme_not_allowed:{parsed.scheme}")

    hostname = parsed.hostname
    if not hostname:
        return (False, "no_hostname")

    try:
        infos = socket.getaddrinfo(hostname, None)
    except socket.gaierror:
        return (False, "dns_error")

    for info in infos:
        ip = info[4][0]
        if not _is_safe_ip(ip):
            return (False, f"unsafe_ip:{ip}")

    return (True, None)


class _SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    """F3 : bloque les redirects vers une URL non-safe."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        is_safe, reason = _validate_url(newurl)
        if not is_safe:
            raise urllib.error.URLError(
                f"redirect_blocked: {reason} ({newurl})"
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _clamp_timeout(timeout):
    """F5 : clamp le timeout dans [MIN_TIMEOUT, MAX_TIMEOUT]."""
    try:
        t = int(timeout)
    except (TypeError, ValueError):
        return DEFAULT_TIMEOUT
    if t < MIN_TIMEOUT:
        return DEFAULT_TIMEOUT
    if t > MAX_TIMEOUT:
        return MAX_TIMEOUT
    return t


def head_check(url, timeout=DEFAULT_TIMEOUT):
    """HEAD-check d'une URL safe. Retourne le status int, ou None si refusé/erreur.

    Ne lève jamais : toute URL non-safe ou tout échec réseau retourne None.
    """
    is_safe, _reason = _validate_url(url)
    if not is_safe:
        return None

    t = _clamp_timeout(timeout)
    opener = urllib.request.build_opener(_SafeRedirectHandler())
    req = urllib.request.Request(url, method="HEAD")
    try:
        with opener.open(req, timeout=t) as resp:
            return int(resp.status)
    except Exception:
        return None


def score_fiabilite(url):
    """Glyphe de fiabilité selon la vivacité/URL.

    ❧ (U+2767) : pas d'URL ; ⁅ (U+2045) : URL unsafe/cassée ; ✦ (U+2726) : vivante.
    """
    if not url:
        return "\u2767"  # ❧
    is_safe, _reason = _validate_url(url)
    if not is_safe:
        return "\u2045"  # ⁅
    status = head_check(url)
    if status is None or status >= 400:
        return "\u2045"  # ⁅
    return "\u2726"  # ✦
