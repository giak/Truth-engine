#!/usr/bin/env python3
"""web_search_ddg.py — Recherche web via le serveur MCP DuckDuckGo docker.

Wrapper du serveur MCP `ghcr.io/mudler/mcps/duckduckgo` (configuré dans
`~/.lmstudio/mcp.json`). Sert de moteur de recherche de secours quand
`web_search` (Serper) tombe en panne, et de source de découverte d'URLs
pour `read_url`. Pas de clé API, pas de scraping maison : le docker fait
la recherche DuckDuckGo et renvoie titres, descriptions et URLs.

Protocole : MCP stdio (JSON-RPC ligne à ligne sur stdin/stdout).
  initialize → notifications/initialized → tools/call search {query}
L'outil `search` ne prend qu'un paramètre `query` (≈5 résultats, ou
`MAX_RESULTS` via env docker).

Usage :
  python3 tools/web_search_ddg.py "requête de recherche" [--limit N] [--json]
  --limit N : nombre max de résultats (env MAX_RESULTS, défaut 10, plafond 10)
  --json     : sortie JSON machine-readable

Sortie texte : titres + URLs décodées (les URLs DDG `//duckduckgo.com/l/?uddg=`
sont déredirectionnées vers la cible réelle). Code retour :
  0 = résultats trouvés (ou recherche OK même si vide)
  1 = erreur (docker indisponible, handshake MCP échoué, timeout)
"""

import argparse
import json
import subprocess
import sys
import time
import urllib.parse

DOCKER_IMAGE = "ghcr.io/mudler/mcps/duckduckgo:latest"
HANDSHAKE_TIMEOUT = 8.0   # démarrage docker + initialize
CALL_TIMEOUT = 25.0       # la recherche DDG peut prendre 10-15 s


class MCPError(Exception):
    pass


def _send(proc, payload):
    """Envoie un message JSON-RPC au serveur MCP (stdio)."""
    proc.stdin.write(json.dumps(payload) + "\n")
    proc.stdin.flush()


def _read_responses(proc, wanted_id, timeout):
    """Lit stdout jusqu'à la réponse JSON-RPC voulue (ou timeout)."""
    deadline = time.time() + timeout
    for line in proc.stdout:
        if time.time() > deadline:
            raise MCPError(f"timeout après {timeout:.0f}s (id {wanted_id} absent)")
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        if msg.get("id") == wanted_id:
            return msg
    raise MCPError("stdout fermé avant la réponse attendue")


def search(query, limit=10):
    """Recherche DuckDuckGo via le MCP docker. Retourne une liste de dicts
    {title, url, description} (URLs DDG déredirectionnées)."""
    proc = subprocess.Popen(
        ["docker", "run", "--rm", "-i", "-e", "MAX_RESULTS=" + str(max(1, min(int(limit), 10))), DOCKER_IMAGE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        _send(proc, {
            "jsonrpc": "2.0", "id": 1, "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "truth-engine-web-search", "version": "0.1"},
            },
        })
        _read_responses(proc, 1, HANDSHAKE_TIMEOUT)
        _send(proc, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
        _send(proc, {
            "jsonrpc": "2.0", "id": 2, "method": "tools/call",
            "params": {"name": "search", "arguments": {"query": query}},
        })
        resp = _read_responses(proc, 2, CALL_TIMEOUT)
    except Exception as exc:
        proc.kill()
        proc.wait()
        raise MCPError(str(exc))

    proc.stdin.close()
    proc.wait(timeout=10)

    if resp.get("error"):
        raise MCPError(f"erreur serveur : {resp['error']}")
    content = resp.get("result", {}).get("content", [])
    text = "".join(c.get("text", "") for c in content if c.get("type") == "text")

    # Le serveur emballe la réponse dans un JSON stringifié : {"result": "..."}
    text = _unwrap(text)

    results = []
    for block in text.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        title = desc = url = None
        for line in block.splitlines():
            if line.startswith("Title:"):
                title = line[len("Title:"):].strip()
            elif line.startswith("Description:"):
                desc = line[len("Description:"):].strip()
            elif line.startswith("URL:"):
                url = line[len("URL:"):].strip()
        if title and url:
            results.append({
                "title": title,
                "url": decode_ddg_url(url),
                "description": desc or "",
            })
    return results


def _unwrap(text):
    """Désemballe un JSON stringifié ({"result": "..."}) si présent."""
    if not text.startswith("{"):
        return text
    try:
        payload = json.loads(text)
        if isinstance(payload, dict) and isinstance(payload.get("result"), str):
            return payload["result"]
    except ValueError:
        pass
    return text


def decode_ddg_url(url):
    """Déredirectionne une URL DuckDuckGo `//duckduckgo.com/l/?uddg=<cible>`."""
    if url.startswith("//"):
        url = "https:" + url
    parsed = urllib.parse.urlparse(url)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        qs = urllib.parse.parse_qs(parsed.query)
        if "uddg" in qs and qs["uddg"]:
            return qs["uddg"][0]
    return url


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("query", help="requête de recherche")
    parser.add_argument("--limit", type=int, default=5,
                        help="nombre max de résultats (1-10, défaut 5)")
    parser.add_argument("--json", action="store_true",
                        help="sortie JSON machine-readable")
    args = parser.parse_args()

    try:
        results = search(args.query, args.limit)
    except MCPError as exc:
        print(f"web_search_ddg: erreur — {exc}", file=sys.stderr)
        return 1
    except FileNotFoundError:
        print("web_search_ddg: docker introuvable (installé ? démarré ?)",
              file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print("Aucun résultat.")
            return 0
        for i, r in enumerate(results, 1):
            print(f"[{i}] {r['title']}")
            print(f"    {r['url']}")
            if r["description"]:
                print(f"    {r['description'][:220]}")
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
