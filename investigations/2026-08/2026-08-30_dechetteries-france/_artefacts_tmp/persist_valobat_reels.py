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
        return {"error": str(e)}
    for m in re.finditer(r'data: ({.*?})\r?\n', txt):
        try:
            return json.loads(m.group(1))
        except Exception:
            continue
    return json.loads(txt)

call("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "valobat-reels-pass", "version": "1.0"}}, 1)
body = json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}).encode()
try:
    urllib.request.urlopen(urllib.request.Request(MCP, data=body, headers=HDRS), timeout=30).read()
except Exception:
    pass

facts = [
    ("Montants Valobat reellement percus - SICTOM Nogent-le-Rotrou 2025 : Valobat 14 928 EUR (ventilé par eco-org, Citeo 620 471, Ecomaison 16 508, Refashion 22 685, EcoDDS 8 990, Ecologic 1 950, Cyanide 2 114 ; total soutiens eco-org et aides publiques 687 646 EUR 2025 contre 476 976 EUR 2024)",
     "SICTOM de Nogent-le-Rotrou (Eure-et-Loir, 28) Rapport annuel 2025 (PDF 81p numerique) : tableau des recettes de fonctionnement ventilant les soutiens des eco-organismes par etablissement - VALOBAT = 14 928 EUR en 2025 (Citeo 620 471, Zelavor 0, Ecologic 1 950, EcoDDS 8 990, Refashion 22 685, Corepile 0, Ecomaison 16 508, Cyanide 2 114 ; poste 'Soutien des eco-organismes et aides publiques' total 687 646 EUR 2025 contre 476 976 EUR 2024). Premier montant Valobat annuel reel percus documente (outre Redon 2024). Source: https://www.sictom-nogentlerotrou.fr/wp-content/uploads/2026/07/rapport-2025-SICTOM-NLR_v-num.pdf (verifie-2026-08-30, tier ✧)"),
    ("CC Aspres 2025 : filiere REP PMCB 165 488 EUR d'economies, tonnages platre/laines/menuiseries 31-40 t, bois 267-283 t, melange 182-225 t sur 2 decheteries",
     "Communauté de Communes des Aspres (66) RPQS 2025 : REP PMCB deployees sur les 2 decheteries (Thuir, Trouillas) ; tonnages 2025 platre/laines de verre-roche/menuiseries vitrees Trouillas 31,69 t / Thuir 40,01 t ; REP en melange 182,26 / 224,68 t ; bois 267,55 / 282,64 t ; 165 488 EUR de depenses economisees au 31/12/2025 (coûts traitement et transport pris en charge par les eco-organismes). Soutien en nature, pas verse en euros. Source: https://www.cc-aspres.fr/wp-content/uploads/2024/07/rpqs-2025-1.pdf (verifie-2026-08-30, tier ✧)"),
    ("Rapport annuel metropolitain 2024 : Soutien operationnel Valobat platre + menuiseries vitrees ; budget decheterie 11,85 M EUR TTC (11,1 M soutiens tous eco-org, 0,7 M aides)",
     "Rapport annuel 2024 (PDF 72p) : deploye les REP PMCB en decheterie avec soutien operationnel pour le platre et les menuiseries vitrées (Valobat), soutien financier pour le bois (Ecomaison) et les inertes (Ecominero) ; budget decheterie 2024 = 11,85 M EUR TTC decompose en 11,1 M EUR de soutiens de tous les eco-organismes et 0,7 M EUR d'aides ; pas de montant Valobat separe publie. Source: https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf (verifie-2026-08-30, tier ✧)"),
    ("Sydem Domes Combrailles 2024 : contrat Valobat signe 14/02/2024, recettes valorisation 410 318 EUR ventilees (Citeo 211 867, EcoMaison 11 498, EcoDDS 4 533) mais Valobat absent du tableau (filiere jeune)",
     "Sydem Domes Combrailles (Puy-de-Dome, 63) Rapport annuel 2024 (PDF 47p) : CONTRAT VALOBAT signé le 14/02/2024 (PMCB, VALTOM co-beneficiaire) ; recettes liees a la valorisation 2024 = 410 318 EUR ventilees : CITEO 211 867, ECOSYSTEMES 23 700, ECO MAISON 11 498, Refashion 3 000, EcoDDS 4 533, Cyclevia 900, verre 16 461, ventes ferrailles/batteries 46 257, carton 32 658 ; VALOBAT absent du tableau 2024 (filiere tout juste signee 02/2024, poste non chiffré cette annee). Source: https://www.sydem-domescombrailles.fr/wp-content/uploads/2025/12/rapport-annuel-2024-vise-sous-pref.pdf (verifie-2026-08-30, tier ✧)"),
    ("SICTOMU 2023 : soutiens valorisation/revente 639 452 EUR reverses aux collectivites, mobilier 20 EUR/t, PMCB en structuration",
     "SICTOMU (Gard, 30) Rapport annuel 2023 (PDF 48p) : soutiens a la valorisation et recettes de revente des matériaux = 639 452 EUR en 2023 (vs 638 175 EUR 2022), percus par Sud Rhone Environnement puis integralement reverses aux collectivites membres ; mobilier beneficie d'un soutien de 20 EUR/tonne (EcoMaison) ; flux PMCB/platre en structuration avec consultation Valobat en perspective. Source: https://sictomu.fr/wp-content/uploads/2024/07/N%C2%B0_22_2024_06_26_RAPPORT_ANNUEL_PJ.pdf (verifie-2026-08-30, tier ✧)"),
    ("SMICTOM Zone Sous Vosgienne : convention Valobat signee, recettes annuelles previsionnelles > 100 000 EUR",
     "PV du Comite Syndical du SMICTOM de la Zone Sous Vosgienne (90) du 28/11/2024 (PDF scanne, snippet officiel ccrc70.fr) : approbation de la convention avec Valobat et de sa signature ; les recettes annuelles previsionnelles au benefice du SMICTOM sont estimees a plus de 100 000 EUR par VALOBAT. TIER ⁅ : document scanne, montant lu par snippet non relu integralement. Source: https://www.ccrc70.fr/wp-content/uploads/2025/02/PV-CS-28-11-2024.pdf (verifie-2026-08-30, tier ⁅)"),
]

mem_map = {}
rid = 10
for i, (title, content) in enumerate(facts):
    rid += 1
    params = {
        "title": title,
        "content": content + "\n\nstatus:VERIFIE\ntags:project:dechetteries-france-fresque, run:20260830-1726-montants-valobat-reels-percus-2025",
        "memory_type": "reference",
        "tags": ["project:dechetteries-france-fresque", "run:20260830-1726-montants-valobat-reels-percus-2025", f"FCT-{i+1:03d}"],
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
                mid = j.get("memory_id") or j.get("id") or (j.get("data", {}) or {}).get("id")
            except Exception:
                try:
                    mid = t.strip().strip('"').strip()
                    if len(mid) != 36: mid = None
                except Exception:
                    mid = None
    print(f"FCT-{i+1:03d} -> {mid}  ({resp.get('error', '')})")
    mem_map[f"FCT-{i+1:03d}"] = mid or "FAILED"

print("=== MEM_MAP ===")
print(json.dumps(mem_map, ensure_ascii=False))