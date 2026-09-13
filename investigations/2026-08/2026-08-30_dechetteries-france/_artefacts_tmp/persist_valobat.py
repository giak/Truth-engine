#!/usr/bin/env python3
import json, urllib.request, re, sys

MCP = "http://localhost:8002/mcp"
HDRS = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}

def call(method, params, reqid):
    body = json.dumps({"jsonrpc": "2.0", "id": reqid, "method": method, "params": params}).encode()
    req = urllib.request.Request(MCP, data=body, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            txt = r.read().decode()
    except Exception as e:
        return {"jsonrpc": "2.0", "error": {"message": str(e)}, "id": reqid}
    # parse SSE data lines
    for m in re.finditer(r'data: ({.*?})\r?\n', txt):
        try:
            return json.loads(m.group(1))
        except Exception:
            continue
    return json.loads(txt)

# initialize
resp = call("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "valobat-pass", "version": "1.0"}}, 1)
print("init:", resp.get("result", {}).get("serverInfo"))

# notifications/initialized
body = json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}).encode()
try:
    urllib.request.urlopen(urllib.request.Request(MCP, data=body, headers=HDRS), timeout=30).read()
except Exception as e:
    print("initialized notification:", e)

facts = [
    ("FCT-001: Barème soutiens REP PMCB - contrat type Valobat CC Dombes delib 24-198 (annexe 2)",
     "Le contrat type REP PMCB (deliberation CC de la Dombes 24-198 du 22/07/2024, annexe 2 aux CG, 71 p.) expose le barème de soutien territorial aux decheteries : forfaits A1 2000 EUR/site, A2 2700 EUR/site, A3 1350/2700 EUR, A5 375 EUR, A6 200 EUR, A7 2700 EUR, A8 400 EUR/an ; soutiens variables tri a la source 20 EUR/t collecte separee, 12 EUR/t transport, bois 50 EUR/t, 30 EUR/t verre-metaux-plastiques-platre-isolants, 75 EUR/t traitement, verre 0 EUR/t en melange ; D1 amiante lie SPGD 500 EUR/t ; E1 communication 5 ctEUR/hab/an ; revalorisation indicielle seuil 90 EUR. Source: https://www.ccdombes.fr/wp-content/uploads/2024/07/DELIB-24-198.pdf (verifie-2026-08-30, T1)"),
    ("FCT-002: Tonnages PMCB SMICTOM des Flandres 2024 - contrat 01/01/2024 475 t materiaux batiment",
     "Le RPQS 2024 du SMICTOM des Flandres (annexe deliberation CC Flandre Lys 2025D195, 14/10/2024) documente le contrat REP PMCB pris d'effet le 01/01/2024 : 475 t de materiaux du batiment collectes sur l'exercice, suivi par flux (platre, menuiseries vitrees, laines minerales) et par site de decheterie. Source: https://www.cc-flandrelys.fr/images/EXTRANET_2020-2026/Conseil_communautaire/2025/20251014/publications/2025D195_-_Annexe_SMICTOM_-_RPQS_2024-tampon.pdf (verifie-2026-08-30, T1)"),
    ("FCT-003: RAA 2024 SICED - Valobat eco-organisme agreé filiere PMCB ouverte decheteries 2023",
     "Le rapport annuel d'activite 2024 du SICED (graphiques officiels) reference Valobat comme eco-organisme agreé de la filiere PMCB, filiere ouverte aux decheteries depuis 2023 (agrement ADEME), soutiens verses sur declaration des tonnages. Source: https://trophees.idealco.fr/wp-content/uploads/2025/06/87868919fcde-Rapport_annuel_SICED_2024_graphiques.pdf (verifie-2026-08-30, T1)"),
    ("FCT-004: Cadre ADEME filiere PMCB - 4 eco-organismes (Ecomaison Ecominero Valdélia Valobat) + OCAB, 22 Mt",
     "Fiche ADEME filieres-REP (filiere PMCB) : 4 eco-organismes agreés (Ecomaison, Ecominero, Valdélia, Valobat) + OCAB organismes coordonnateurs, entree en vigueur progressive depuis 2023, gisement national d'environ 22 Mt de dechets de chantier par an. Source: https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB (verifie-2026-08-30, T2)"),
]

mem_map = {}
rid = 10
for i, (title, content) in enumerate(facts):
    rid += 1
    params = {
        "title": title,
        "content": content + "\n\nstatus:VERIFIE\ntags:project:dechetteries-france-fresque, run:20260830-1558-baremes-valobat-pmcb-2024",
        "memory_type": "reference",
        "tags": ["project:dechetteries-france-fresque", "run:20260830-1558-baremes-valobat-pmcb-2024", f"FCT-{i+1:03d}"],
        "author": "truth-engine",
    }
    resp = call("tools/call", {"name": "write_memory", "arguments": params}, rid)
    mid = None
    res = resp.get("result", {})
    if isinstance(res, dict):
        for c in res.get("content", []):
            t = c.get("text", "")
            try:
                j = json.loads(t)
                mid = j.get("memory_id") or j.get("id") or j.get("data", {}).get("id")
            except Exception:
                mid = None
            sys.stderr.write(f"FCT-{i+1:03d} write resp text: {t[:200]}\n")
    print(f"FCT-{i+1:03d} -> {mid}  ({resp.get('error', '')})")
    mem_map[f"FCT-{i+1:03d}"] = mid or "FAILED"

print("=== MEM_MAP ===")
print(json.dumps(mem_map, ensure_ascii=False))