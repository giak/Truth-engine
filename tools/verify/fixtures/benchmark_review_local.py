#!/usr/bin/env python3
"""Benchmark reviewer local : qwen3.6:35b (think:false) sur BAD + témoin.

Sauvegarde l'ARTEFACT CANONIQUE (benchmark_results.json) et le log
(benchmark.log) dans ce même dossier, afin que les nombres cités dans
docs/suivi_verification.md §5 soient reproductibles et versionnés.

Vérité terrain :
  - BAD : 6 violations réelles (C1 STATE=OPEN, C2 pipeline KERNEL absent,
    C3 structure SIMPLE incomplète, C4 traçabilité absente, C5 preuve L4
    absente, C7 GAP/STOP_OK non étayés). C6 attendu OK.
  - témoin : 4 défauts réels (C2 ANALYZE annonce 15 symboles mais n'en liste
    que 3, C4 URLs = pages de liste, C5 contre-exemple non démontrable et
    recoupement ≥2 familles non prouvé, C7 SRC-003 placeholder irrécupérable).

Usage :
  python3 tools/verify/fixtures/benchmark_review_local.py [--model qwen3.6:35b]
"""
import json
import sys
import time
import urllib.request

HERE = __file__.rsplit("/", 1)[0] + "/"
OLLAMA = "http://localhost:11434/api/generate"

MODEL = "qwen3.6:35b"
DOCS = {
    "BAD": (HERE + "fixture_BAD.md", "2026-08-18_11-45_poc-gate-verification_INVESTIGATION.md"),
    "OK": (HERE + "fixture_OK.md", None),
}

ROLE = """Tu es un reviewer indépendant et hostile au travail présenté. Tu n'as pas produit ce document. Tu es en lecture seule. Tu ne répareras rien.
Rends exactement UN verdict parmi trois : FAIL (défaut démontrable, chaque défaut documenté), BLOCKED (vérification impossible), PASS (aucun défaut matériel).
Interdits : scores, pourcentages, flatterie. Style direct. Seuls les défauts qui empêchent rationnellement la livraison vont dans findings."""

CONTRACT = """CONTRAT DU PROJET (extraits canoniques de knowledge.md et truth-engine-v2/KERNEL.md) :
- Livrable final : STATE=FINAL, NEXT_ACTION=NONE. KERNEL §0 : « NEVER persist OPEN/PENDING as final ».
- Pipeline KERNEL obligatoire : ANALYZE §0 avec 15 symboles narratifs scorés, BIAS_TEST, CRÉDO/SCOPING, LEAD_REGISTRY, CLAIM_REGISTRY, EVIDENCE_REGISTRY.
- COMPLEXITY=SIMPLE : exactement 5 sections core (RÉSUMÉ EXÉCUTIF, CHRONOLOGIE, DOMAINES, CARTE DES PREUVES, PÉRIMÈTRE & LIMITES) + appendices SOURCES et REQUEST_LOG obligatoires.
- Traçabilité : bloc FACT_REGISTRY_V1 (id|epi|tier|url|families|date), identifiant FCT-###, source = URL de page spécifique cliquable / SRC-ID / locator exact.
- L4 (CONFIRMÉ) : L3 + gate EPI=FACT + recherche de contre-exemples + preuves matérielles dans le livrable (sources fetchées, recoupement ≥2 familles, FACT_REGISTRY_V1, REQUEST_LOG).
- Horodatage du nom de fichier = date/heure réelle de création (CEST), jamais inventé.
- Toute affirmation sans source vérifiable = violation grave."""

ENUM = """

PROCÉDURE OBLIGATOIRE, À EXÉCUTER DANS CET ORDRE :
1. Examine le livrable ci-dessous.
2. Pour CHACUN des 7 points C1..C7, tranche explicitement : C1:OK ou C1:VIOLATION, etc. (une ligne par point, dans l'ordre).
3. Convertis en findings UNIQUEMENT les points marqués VIOLATION (location + problem + evidence pour chacun).
4. Le verdict est FAIL si au moins un point est VIOLATION, sinon PASS, BLOCKED si le livrable est illisible.

Points à trancher :
C1. STATE du manifeste = FINAL ?
C2. Pipeline KERNEL présent (ANALYZE 15 symboles, BIAS_TEST, CRÉDO/SCOPING, registres) ?
C3. Structure SIMPLE complète (5 sections core + SOURCES + REQUEST_LOG) ?
C4. Traçabilité des faits (FACT_REGISTRY_V1, FCT-###, source URL/locator) ?
C5. Preuve matérielle de « vérifié L4 » ?
C6. Horodatage du nom de fichier cohérent ?
C7. Autre fabrication ou affirmation non étayée ?

RÉPONDS UNIQUEMENT EN JSON :
{"points": {"C1": "OK" ou "VIOLATION", ..., "C7": ...}, "verdict": "PASS" ou "FAIL" ou "BLOCKED", "findings": [{"location": "...", "problem": "...", "evidence": "..."}]}"""


def call(model, prompt, timeout=300):
    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "think": False,
            "options": {"temperature": 0.3, "num_predict": 4096},
        }
    ).encode()
    req = urllib.request.Request(
        OLLAMA, data=payload, headers={"Content-Type": "application/json"}
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode())
    elapsed = time.time() - t0
    raw = body.get("response", "").strip()
    eval_count = body.get("eval_count", 0)
    tok_s = eval_count / elapsed if elapsed > 0 else 0
    return raw, elapsed, eval_count, tok_s


def strip_fences(raw):
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    return raw


def run(model, doc_label):
    path, fname = DOCS[doc_label]
    doc = open(path, encoding="utf-8").read()
    if fname is None:
        fname = doc.splitlines()[1].replace("FICHIER : ", "").strip()
    prompt = ROLE + "\n" + CONTRACT + ENUM + "\n\n" + fname + "\n\nLIVRABLE À EXAMINER :\n\n" + doc
    raw, elapsed, eval_count, tok_s = call(model, prompt)
    cleaned = strip_fences(raw)
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        return {
            "model": model, "doc": doc_label, "parsed": False,
            "parse_error": str(exc), "verdict": None, "points": {},
            "findings": [], "n_findings": 0, "viol_points": 0,
            "elapsed_s": round(elapsed, 1), "tok_s": round(tok_s, 1),
            "eval_count": eval_count, "raw": raw[:2000],
        }
    points = parsed.get("points", {}) or {}
    findings = parsed.get("findings", []) or []
    viol = [k for k, v in points.items() if v == "VIOLATION"]
    return {
        "model": model, "doc": doc_label, "parsed": True,
        "parse_error": None, "verdict": parsed.get("verdict"),
        "points": points, "findings": findings,
        "n_findings": len(findings), "viol_points": len(viol),
        "viol": viol, "elapsed_s": round(elapsed, 1),
        "tok_s": round(tok_s, 1), "eval_count": eval_count, "raw": raw[:2000],
    }


def main():
    if "--model" in sys.argv:
        global MODEL
        MODEL = sys.argv[sys.argv.index("--model") + 1]
    results = []
    lines = []
    for doc_label in ("BAD", "OK"):
        print(f"[{MODEL} {doc_label}] en cours...", file=sys.stderr)
        r = run(MODEL, doc_label)
        results.append(r)
        lines.append(f"[{MODEL} {doc_label}] parsed={r['parsed']} verdict={r['verdict']} "
                     f"findings={r['n_findings']} viol={r.get('viol', [])} "
                     f"tok/s={r['tok_s']} ({r['elapsed_s']}s)")
        if r["parsed"]:
            for f in r["findings"]:
                lines.append(
                    f"  - [{f.get('location', '?')}] {f.get('problem', '?')}\n"
                    f"    evidence: {f.get('evidence', '?')}"
                )
        else:
            lines.append(f"  PARSE FAIL: {r['parse_error']}")
        lines.append("")

    with open(HERE + "benchmark_results.json", "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)

    header = [
        f"# Benchmark reviewer local : {MODEL} (think:false, format:json, temp 0.3)",
        "# Vérité terrain : BAD = 6 violations réelles ; témoin = 4 défauts réels.",
        "",
    ]
    with open(HERE + "benchmark.log", "w", encoding="utf-8") as fh:
        fh.write("\n".join(header + lines) + "\n")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
