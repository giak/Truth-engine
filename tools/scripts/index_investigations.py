#!/usr/bin/env python3
"""Index all investigation markdown files from truth-engine into MnemoLite via MCP API."""
import os, json, subprocess, sys, time

BASE = "/home/giak/projects/truth-engine"
DIRS = [
    "investigations/2026-06/2026-06-10_action_acephalique_manquante",
    "investigations/2026-06/2026-06-10_analyse_defaite_guerilla",
    "investigations/2026-06/2026-06-10_audit_general_senior",
    "investigations/2026-06/2026-06-10_droit_compare_benelux_coordination",
    "investigations/2026-06/2026-06-10_financement_coordination",
    "investigations/2026-06/2026-06-10_fresque_systemique_oligarchie",
    "investigations/2026-06/2026-06-10_leadership_acephalique",
    "investigations/2026-06/2026-06-10_modele_non_escalade_france",
    "investigations/2026-06/2026-06-10_puits_de_droit_concret",
    "investigations/2026-06/2026-06-10_risque_juridique_coordination",
    "investigations/2026-06/2026-06-10_solutions_financement_invisible",
    "investigations/2026-06/2026-06-10_solutions_succession",
    "investigations/2026-06/2026-06-10_verrou_coordination_guerilla",
]

MCP_URL = "http://localhost:8002/mcp"
HEADERS_TEMPLATE = 'Accept: application/json, text/event-stream\nContent-Type: application/json'

def call_mcp(method, arguments, msg_id):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": method, "arguments": arguments},
        "id": msg_id,
    })
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "120", "-X", "POST", MCP_URL,
             "-H", "Accept: application/json, text/event-stream",
             "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True, timeout=130
        )
        for line in result.stdout.split("\n"):
            if line.startswith("data:"):
                data = json.loads(line[5:])
                r = data.get("result", {})
                text = r.get("content", [{}])[0].get("text", "")
                inner = json.loads(text) if isinstance(text, str) else {}
                return inner
        return {"error": "no data line", "raw": result.stdout[:300]}
    except Exception as e:
        return {"error": str(e)}

def extract_title(content):
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            title = line[2:].strip()
            return title[:200]
    return "Untitled"

def extract_tags(dirname):
    parts = dirname.replace("2026-06-10_", "").split("_")
    tag_map = {
        "action": "action_collective", "acephalique": "coordination_acephalique",
        "manquante": "gap", "analyse": "analyse", "defaite": "defaite",
        "guerilla": "guerilla", "audit": "audit", "general": "audit",
        "senior": "audit", "droit": "droit", "compare": "droit_compare",
        "benelux": "benelux", "coordination": "coordination",
        "financement": "financement", "fresque": "fresque",
        "systemique": "systemique", "oligarchie": "oligarchie",
        "leadership": "leadership", "modele": "modele",
        "non": "non_violence", "escalade": "non_escalade", "france": "france",
        "puits": "droit", "concret": "solutions", "risque": "risque",
        "juridique": "droit", "solutions": "solutions",
        "invisible": "clandestinite", "succession": "succession",
        "verrou": "verrouillage",
    }
    tags = set()
    for p in parts:
        if p in tag_map:
            tags.add(tag_map[p])
    tags.add("2026-06-10")
    tags.add("investigation")
    return list(tags)

def main():
    total = 0
    success = 0
    errors = []
    
    for d in DIRS:
        dirpath = os.path.join(BASE, d)
        dirname = os.path.basename(d)
        if not os.path.isdir(dirpath):
            print(f"SKIP (not found): {d}")
            continue
        
        for fname in sorted(os.listdir(dirpath)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            total += 1
            
            with open(fpath, "r") as f:
                content = f.read()
            
            if not content.strip():
                print(f"SKIP (empty): {fname}")
                continue
            
            title = extract_title(content)
            tags = extract_tags(dirname)
            fname_lower = fname.lower()
            for kw in ["apex", "investigation", "solutions", "audit", "wolves",
                        "hyper_matrice", "manipulation", "sources", "kernel"]:
                if kw in fname_lower:
                    tags.append(kw if kw != "kernel" else "kernel_synthesis")
            
            msg_id = 1000 + total
            print(f"[{total}] {title[:80]}... ", end="", flush=True)
            
            result = call_mcp("write_memory", {
                "title": title,
                "content": content,
                "memory_type": "investigation",
                "tags": tags,
            }, msg_id)
            
            if "error" in result:
                print(f"ERROR: {result['error'][:100]}")
                errors.append({"file": fpath, "error": str(result)})
            else:
                mem_id = result.get("id", result.get("memory_id", result.get("success", "")))
                if mem_id:
                    print(f"OK")
                    success += 1
                else:
                    print(f"UNEXPECTED: {str(result)[:200]}")
                    errors.append({"file": fpath, "response": str(result)})
            
            time.sleep(0.3)
    
    print(f"\n=== RESULTS ===")
    print(f"Total: {total} | Success: {success} | Errors: {len(errors)}")
    for e in errors[:5]:
        print(f"  ERR: {e['file']}")

if __name__ == "__main__":
    main()
