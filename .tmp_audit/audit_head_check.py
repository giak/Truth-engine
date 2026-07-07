"""Audit antagoniste head_check.py — 6 scenarios SSRF/security."""
import sys, time, socket
sys.path.insert(0, 'tools/engines/sublimator/extractors')
from head_check import head_check, score_fiabilite

print("="*70)
print("AUDIT ANTAGONISTE head_check.py (avant hardening)")
print("="*70)
print()

results = []

# --- F1 : schemes exotiques ---
print("="*70); print("F1 : schemes exotiques (file://, ftp://, data:)"); print("="*70)
for url in [
    "file:///etc/passwd",
    "file:///etc/hostname",
    "file:///proc/self/environ",
    "ftp://anonymous@example.com/test",
    "data:text/plain,hello",
    "javascript:alert(1)",
    "gopher://example.com/_",
]:
    try:
        status = head_check(url, timeout=3)
        leaked = "LEAK!" if status is not None else "none"
        print(f"  {leaked:>5} {url} -> status={status}")
        results.append((url, status, "F1"))
    except Exception as e:
        print(f"  EXC   {url} -> {type(e).__name__}: {e}")
        results.append((url, f"EXC:{e}", "F1"))

# --- F2 : SSRF localhost / IP privees ---
print(); print("="*70); print("F2 : SSRF localhost / IP privees (sans serveur reel)"); print("="*70)
for url in [
    "http://localhost/",
    "http://127.0.0.1/",
    "http://0.0.0.0/",
    "http://[::1]/",
    "http://10.0.0.1/",
    "http://192.168.1.1/",
    "http://172.16.0.1/",
    "http://169.254.169.254/latest/meta-data/",  # AWS metadata
    "http://100.100.100.200/latest/meta-data/",  # GCP metadata
]:
    t0 = time.time()
    try:
        status = head_check(url, timeout=2)
        dt = time.time() - t0
        # None = refuse, int = reached
        reached = "REACH" if status is not None else "REFUSE"
        print(f"  {reached:>6} {url} -> status={status} ({dt:.2f}s)")
        results.append((url, status, "F2"))
    except Exception as e:
        dt = time.time() - t0
        print(f"  EXC    {url} -> {type(e).__name__} ({dt:.2f}s)")
        results.append((url, f"EXC:{e}", "F2"))

# --- F3 : redirects vers IP privees (mock via local server) ---
print(); print("="*70); print("F3 : redirect 301 vers 127.0.0.1 (URL publique qui redirige)"); print("="*70)
import threading, http.server
class RedirHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(302)
        self.send_header('Location', 'http://127.0.0.1:9999/secret')
        self.end_headers()
    def do_GET(self):
        self.do_HEAD()
    def log_message(self, *a): pass

server = http.server.HTTPServer(('127.0.0.1', 0), RedirHandler)
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()
try:
    url = f'http://localhost:{port}/redir'
    print(f"  Server redirigeur lance sur port {port} : {url} -> http://127.0.0.1:9999/secret")
    t0 = time.time()
    status = head_check(url, timeout=3)
    dt = time.time() - t0
    reached = "REACH" if status is not None else "REFUSE"
    print(f"  {reached:>6} {url} -> status={status} ({dt:.2f}s)")
    if status is not None:
        print(f"  ** REDIRECTION SUIVIE MALGRE destination privee ! **")
    results.append((url, status, "F3"))
finally:
    server.shutdown()

# --- F4 : IPv6 brackets (loopback, link-local, ULA) ---
print(); print("="*70); print("F4 : IPv6 brackets (loopback/link-local)"); print("="*70)
for url in [
    "http://[::1]/",
    "http://[::ffff:127.0.0.1]/",  # IPv4-mapped IPv6
    "http://[fe80::1]/",
    "http://[fc00::1]/",  # ULA
    "http://[2001:db8::1]/",  # documentation, devrait passer
]:
    t0 = time.time()
    try:
        status = head_check(url, timeout=2)
        dt = time.time() - t0
        reached = "REACH" if status is not None else "REFUSE"
        print(f"  {reached:>6} {url} -> status={status} ({dt:.2f}s)")
        results.append((url, status, "F4"))
    except Exception as e:
        dt = time.time() - t0
        print(f"  EXC    {url} -> {type(e).__name__} ({dt:.2f}s)")
        results.append((url, f"EXC:{e}", "F4"))

# --- F5 : timeout ---
print(); print("="*70); print("F5 : timeout"); print("="*70)
for t in [0, 1, None, 999999, -5]:
    try:
        t0 = time.time()
        # URL publique reelle, on veut voir si timeout=0 hang ou pas
        status = head_check("http://example.com", timeout=t)
        dt = time.time() - t0
        print(f"  timeout={t!r:>10} -> status={status} ({dt:.2f}s)")
        results.append((f"timeout={t}", status, "F5"))
    except Exception as e:
        dt = time.time() - t0
        print(f"  EXC timeout={t!r:>10} -> {type(e).__name__} ({dt:.2f}s)")

# --- F6 : DNS rebinding ---
print(); print("="*70); print("F6 : DNS rebinding (resolve public, puis private)"); print("="*70)
# Implementation : on utilise un hostname qui repond 127.0.0.1 (loopback) ou 1.1.1.1 (public)
# On ne peut pas facilement simuler DNS rebinding en local, mais on peut tester :
# - Le hostname est-il resolvable ? (getaddrinfo)
# - L'IP resultante est-elle checkee avant urlopen ?
import socket
for host in ["localhost", "127.0.0.1", "1.1.1.1", "example.com", "10.0.0.1"]:
    try:
        infos = socket.getaddrinfo(host, 80)
        for f, t, p, c, sa in infos[:2]:
            print(f"  {host:>20} -> {sa[0]}")
    except Exception as e:
        print(f"  {host:>20} -> EXC {e}")
print("  NB : head_check ne fait PAS de check IP pre-connection, donc DNS rebinding exploitable si le hostname repond une IP privee.")

print(); print("="*70)
print("RESUME PAR FINDING")
print("="*70)
for f in ["F1","F2","F3","F4","F5","F6"]:
    fr = [r for r in results if r[2] == f]
    if not fr: continue
    leaks = sum(1 for _, s, _ in fr if s is not None and not str(s).startswith('EXC'))
    print(f"  {f}: {len(fr)} scenarios testes, {leaks} ont reussi a atteindre la cible")
