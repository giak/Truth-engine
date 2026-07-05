"""HEAD-check URLs — seul module Python necessaire pour Sublimator v34 Leger.

v2.0 (2026-07-05) - hardening F1+F2 (audit antagoniste 6 scenarios SSRF) :
- F1 : ALLOWED_SCHEMES = {"http", "https"}. Rejette file://, ftp://, data:,
       gopher://, javascript:, etc. (urllib.request.urlopen supporte nativement
       file://, ce qui lisait /etc/passwd, /proc/self/environ avant le patch).
- F2 : _is_safe_url() valide le hostname par resolution DNS + check IP contre
       blocklist (loopback, link-local, private, multicast, reserved, unspecified,
       IPv4-mapped IPv6). Rejette localhost, 127.0.0.1, 10.0.0.0/8, 192.168.0.0/16,
       172.16.0.0/12, 169.254.0.0/16 (metadata AWS/GCP), ::1, fe80::, fc00::.
- F2.1 : _SafeRedirectHandler qui re-valide chaque Location (defense contre
         redirects vers IP privees). Lever URLError si Location unsafe.
- F2.2 : timeout clamp [1, 30]s. Defaut 5s. Rejette timeout=0/None/negatif/huge.
- F6 (limitation documentee) : DNS rebinding partiellement adresse par check
    pre-connection. Pour mitigation stricte, faudrait monkey-patcher
    socket.create_connection (hors scope v2.0).
"""

import ipaddress
import socket
import urllib.request
import urllib.error
from typing import Literal
from urllib.parse import urlparse

Fiabilite = Literal["\u2726", "\u2727", "\u2045", "\u2767"]

# F1 : allowlist schemes (file://, ftp://, data:, gopher://, javascript: refuses)
ALLOWED_SCHEMES: set[str] = {"http", "https"}
# F2.2 : timeout clamp
DEFAULT_TIMEOUT: int = 5
MIN_TIMEOUT: int = 1
MAX_TIMEOUT: int = 30


def _is_safe_ip(ip_str: str) -> bool:
    """Verifie si une IP est 'safe' (globale, non-reservee, non-loopback).

    Rejette: loopback (127.0.0.0/8, ::1), link-local (169.254.0.0/16, fe80::/10),
    private (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, fc00::/7),
    multicast, reserved, unspecified, IPv4-mapped IPv6 (::ffff:127.0.0.1).
    """
    try:
        ip = ipaddress.ip_address(ip_str)
    except ValueError:
        return False
    # IPv4-mapped IPv6 (::ffff:127.0.0.1) : convertir en IPv4 puis re-check
    if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
        ip = ipaddress.ip_address(ip.ipv4_mapped)
    # is_global couvre deja loopback/link-local/private/multicast/reserved/unspecified
    # pour la majorite des cas, mais on double-check explicitement les cas ambigus
    if not ip.is_global:
        return False
    if ip.is_loopback or ip.is_link_local or ip.is_multicast:
        return False
    if ip.is_reserved or ip.is_unspecified:
        return False
    return True


def _validate_url(url: str) -> tuple[bool, str | None]:
    """Valide URL : scheme allowlist + resolution DNS + check IP.

    Returns:
        (is_safe, reason): reason est None si safe, sinon code erreur lisible.
    """
    if not url:
        return False, "empty_url"
    try:
        parsed = urlparse(url)
    except Exception as e:
        return False, f"parse_error: {e}"
    if parsed.scheme not in ALLOWED_SCHEMES:
        return False, f"scheme_not_allowed: {parsed.scheme!r}"
    if not parsed.hostname:
        return False, "no_hostname"
    # Resolution DNS : check TOUTES les IPs resolues
    try:
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        infos = socket.getaddrinfo(parsed.hostname, port, proto=socket.IPPROTO_TCP)
    except socket.gaierror as e:
        return False, f"dns_error: {e}"
    for info in infos:
        ip_str = info[4][0]
        # Strip IPv6 brackets si presents
        if ip_str.startswith("[") and ip_str.endswith("]"):
            ip_str = ip_str[1:-1]
        if not _is_safe_ip(ip_str):
            return False, f"unsafe_ip: {ip_str}"
    return True, None


class _SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    """F2.1 : re-valide chaque Location avant de suivre la redirection.

    Si l'URL de redirection pointe vers une IP non-safe (loopback, privee, etc.),
    leve URLError au lieu de suivre. Casse la chainede SSRF via redirect.
    """

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        is_safe, reason = _validate_url(newurl)
        if not is_safe:
            raise urllib.error.URLError(f"redirect_blocked: {reason}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _build_safe_opener() -> urllib.request.OpenerDirector:
    """Construit un opener avec _SafeRedirectHandler installe."""
    opener = urllib.request.OpenerDirector()
    opener.add_handler(_SafeRedirectHandler())
    opener.add_handler(urllib.request.HTTPHandler())
    opener.add_handler(urllib.request.HTTPSHandler())
    return opener


_SAFE_OPENER: urllib.request.OpenerDirector = _build_safe_opener()


def head_check(url: str, timeout: int = DEFAULT_TIMEOUT) -> int | None:
    """Retourne le status code HTTP, ou None si la requete echoue / URL est unsafe.

    Hardening v2.0 :
    - F1 : rejette schemes exotiques (file://, ftp://, data:, gopher://, javascript:).
    - F2 : rejette URLs dont le hostname resolt vers IP privee/loopback/link-local.
    - F2.1 : rejette les redirections vers IP non-safe.
    - F2.2 : clamp timeout dans [1, 30]s.
    """
    if not url:
        return None
    # F2.2 : clamp timeout
    if timeout is None or timeout < MIN_TIMEOUT:
        timeout = MIN_TIMEOUT
    elif timeout > MAX_TIMEOUT:
        timeout = MAX_TIMEOUT
    # F1+F2 : pre-validation URL
    is_safe, _reason = _validate_url(url)
    if not is_safe:
        return None
    try:
        req = urllib.request.Request(url, method="HEAD")
        with _SAFE_OPENER.open(req, timeout=timeout) as r:
            return r.status
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError):
        return None


def score_fiabilite(url: str = "", tier: int | None = None) -> Fiabilite:
    """Score fiabilite: \u2726 tier1+200, \u2727 tier2+200, \u2045 casse/erreur, \u2767 pas d'URL ou unsafe."""
    if not url:
        return "\u2767"
    status = head_check(url)
    if status is None:
        return "\u2045"
    if status == 200:
        return "\u2726" if tier == 1 else "\u2727"
    return "\u2045"
