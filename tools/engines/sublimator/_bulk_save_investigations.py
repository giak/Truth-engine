#!/usr/bin/env python3
"""
Sauvegarde TOUTES les enquêtes INVESTIGATION.md dans Mnemolite.
Strategie: POST direct vers l'API REST memoire (pas de CLI, pas de stdin, pas de truncation).
Verification post-import via search vectoriel.
"""

import os
import sys
import json
import time
import subprocess
import urllib.request
import urllib.error
import urllib.parse

# ── Configuration ──────────────────────────────────────────────

API_MEMORIES = "http://localhost:8001/api/v1/memories"
API_SEARCH = "http://localhost:8001/v1/search/"
INVESTIGATIONS_DIR = "/home/giak/projects/truth-engine/investigations"
LOG_FILE = os.path.join(os.path.dirname(__file__), "_import_log.jsonl")
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "_import_progress.json")
SENDMAIL_BIN = "/usr/sbin/sendmail"
REPORT_EMAIL = "christophe.giacomel@proton.me"
DELAY_SECONDS = 0.5  # entre chaque POST (ne pas surcharger l'embedding)
MAX_RETRIES = 3
REQUEST_TIMEOUT = 120  # secondes pour POST + embedding

EXCLUDE_DIRS = {
    "_quintessence", "_synthese", "_assemblage", "_draft",
    "archive", "sections", "articles", "audits", "sessions",
    "sublimation", "02_articles", "03_fichiers_connexes",
}

EXCLUDE_PATTERNS = [
    "INDEX.md", "README.md", "00B_CENSUS.md", "00_DIGEST.md", "01_DIGEST.md",
    "01_MATRICE.md", "02_CLUSTERING.md", "02_DIALECTIQUE.md", "03_THESES.md",
    "03_ARCHITECTURE.md", "04_ARCHITECTURE.md", "04_FACTCHECK.md",
    "05_ARTICLE.md", "06_SATURATION", "tweet.md", "CP1A.md",
    "CHANGELOG", "PROMPT", "REGISTRE_URLS", "liste_articles",
    "_MASTER_", "ENRICHISSEMENT", "APEX_status", "changelog_session",
]


# ── Helpers ────────────────────────────────────────────────────

def list_investigation_files():
    """Trouve tous les fichiers INVESTIGATION.md (pas les quintessences, drafts, etc.)."""
    files = []
    for root, dirs, fnames in os.walk(INVESTIGATIONS_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in fnames:
            if not fn.endswith(".md"):
                continue
            if "INVESTIGATION" not in fn.upper():
                continue
            skip = False
            for pat in EXCLUDE_PATTERNS:
                if pat.lower() in fn.lower():
                    skip = True
                    break
            if skip:
                continue
            files.append(os.path.join(root, fn))
    files.sort()
    return files


def derive_title(filepath):
    """Titre unique lisible depuis le nom de fichier."""
    basename = os.path.basename(filepath).replace(".md", "")
    rel = os.path.relpath(filepath, INVESTIGATIONS_DIR)
    folder = os.path.dirname(rel)
    if folder:
        title = f"[{folder}] {basename}"
    else:
        title = basename
    if len(title) > 200:
        title = title[:197] + "..."
    return title


def derive_tags(filepath):
    """Tags depuis le chemin du dossier."""
    tags = ["truth-engine", "investigation"]
    rel = os.path.relpath(filepath, INVESTIGATIONS_DIR)
    folder = os.path.dirname(rel)
    for segment in folder.split(os.sep):
        # Garde les mots de 3+ caracteres, pas purement numeriques
        cleaned = segment.replace("_", " ").replace("-", " ")
        for word in cleaned.split():
            if len(word) >= 3 and not word.isdigit():
                if word.lower() not in tags:
                    tags.append(word.lower())
    return tags[:10]


def post_memory(title, content, tags):
    """POST /api/v1/memories — retourne (success: bool, message: str, mem_id: str|None)."""
    payload = {
        "title": title,
        "content": content,
        "memory_type": "investigation",
        "tags": tags,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        API_MEMORIES,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            mem_id = body.get("id", body.get("memory_id", None))
            return True, f"HTTP {resp.status}", mem_id
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:300]
        return False, f"HTTP {e.code}: {err_body}", None
    except urllib.error.URLError as e:
        return False, f"URL error: {e.reason}", None
    except Exception as e:
        return False, f"Exception: {str(e)[:200]}", None


def verify_via_search(filepath):
    """Verifie que le fichier est trouvable dans Mnemolite via l'API search vectorielle."""
    basename = os.path.basename(filepath).replace(".md", "").replace("_", " ")
    # Utilise les ~8 premiers mots distinctifs du nom
    keywords = " ".join(basename.split()[:8])
    url = f"{API_SEARCH}?vector_query={urllib.parse.quote(keywords)}&limit=3"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            results = body.get("results", body.get("data", []))
            if results and len(results) > 0:
                top_title = results[0].get("title", "")
                return True, f"found: {top_title[:80]}"
            return False, "no results"
    except Exception as e:
        return False, f"search error: {str(e)[:100]}"


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"imported": [], "failed": [], "skipped": []}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def log_entry(entry):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def send_report_email(imported, failed, skipped, total, elapsed, progress):
    """Envoie le rapport par email via sendmail."""
    minutes = elapsed / 60
    status_icon = "✓" if failed == 0 else "⚠"
    subject = f"[Truth Engine] Import Mnemolite termine — {status_icon} {imported} OK, {failed} KO sur {total}"

    # Logs stdout/stderr (passes par le wrapper bash via env)
    stdout_log = os.environ.get("IMPORT_STDOUT_LOG", "")
    stderr_log = os.environ.get("IMPORT_STDERR_LOG", "")
    full_log_section = f"Log JSONL : {LOG_FILE}"
    if stdout_log:
        full_log_section += f"\nStdout    : {stdout_log}"
    if stderr_log:
        full_log_section += f"\nStderr    : {stderr_log}"

    # Construire la liste des echecs
    failed_list = ""
    if progress.get("failed"):
        failed_list = "\nFichiers en echec:\n"
        for fp in progress["failed"][-20:]:  # 20 derniers max
            failed_list += f"  - {os.path.basename(fp)}\n"
        if len(progress["failed"]) > 20:
            failed_list += f"  ... et {len(progress['failed']) - 20} autres (voir log)\n"

    body = f"""Rapport d'import Mnemolite — {time.strftime('%Y-%m-%d %H:%M:%S')}
{'=' * 50}

Importes : {imported}
Echecs   : {failed}
Ignores  : {skipped}
Total    : {total}
Duree    : {minutes:.1f} min ({elapsed:.0f}s)

{full_log_section}
Progres   : {PROGRESS_FILE}
{failed_list}
---
Script: _bulk_save_investigations.py
Machine: {os.uname().nodename}
"""

    email = f"""To: {REPORT_EMAIL}
From: truth-engine@localhost
Subject: {subject}
Content-Type: text/plain; charset=utf-8

{body}"""

    try:
        proc = subprocess.run(
            [SENDMAIL_BIN, "-t", "-oi"],
            input=email,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if proc.returncode == 0:
            print(f"\n📧 Rapport envoye a {REPORT_EMAIL}")
        else:
            print(f"\n⚠ Email ECHEC (sendmail exit {proc.returncode}): {proc.stderr[:200]}")
    except FileNotFoundError:
        print(f"\n⚠ sendmail introuvable a {SENDMAIL_BIN} — pas d'email envoye")
    except Exception as e:
        print(f"\n⚠ Email erreur: {e}")


# ── Main ───────────────────────────────────────────────────────

def main():
    all_files = list_investigation_files()
    total = len(all_files)
    print(f"Fichiers INVESTIGATION.md : {total}")
    print(f"API : {API_MEMORIES}")
    print(f"Delai : {DELAY_SECONDS}s | Timeout : {REQUEST_TIMEOUT}s | Retries : {MAX_RETRIES}")
    print(f"Log  : {LOG_FILE}")
    print(f"Progres : {PROGRESS_FILE}")
    print()

    progress = load_progress()
    already_imported = set(progress["imported"])
    already_failed = set(progress["failed"])

    imported, failed, skipped = 0, 0, 0
    start_time = time.time()

    for i, fp in enumerate(all_files):
        if fp in already_imported:
            skipped += 1
            continue
        title = derive_title(fp)
        tags = derive_tags(fp)

        # Lecture du contenu INTEGRAL
        try:
            with open(fp, "r", encoding="utf-8") as fh:
                content = fh.read()
        except Exception as e:
            failed += 1
            progress["failed"].append(fp)
            log_entry({"file": fp, "status": "read_error", "error": str(e), "ts": time.time()})
            print(f"  LECTURE ERREUR [{i+1}/{total}] {os.path.basename(fp)[:60]}: {e}")
            continue

        if len(content) < 200:
            skipped += 1
            log_entry({"file": fp, "status": "too_short", "size": len(content), "ts": time.time()})
            continue

        # POST avec retries
        success = False
        last_error = ""
        mem_id = None

        for attempt in range(1, MAX_RETRIES + 1):
            success, msg, mem_id = post_memory(title, content, tags)
            if success:
                break
            last_error = msg
            if attempt < MAX_RETRIES:
                time.sleep(2)

        if success:
            imported += 1
            progress["imported"].append(fp)
            # Nettoyer de la liste des echecs si retente reussie
            if fp in already_failed:
                progress["failed"].remove(fp)
            log_entry({
                "file": fp, "title": title, "status": "ok",
                "size": len(content), "mem_id": str(mem_id),
                "attempt": attempt, "ts": time.time(),
            })

            # Verification: search pour ce fichier (1 sur 10, economie de temps)
            if imported % 10 == 0:
                v_ok, v_msg = verify_via_search(fp)
                v_status = "verified" if v_ok else f"verify_failed: {v_msg}"
                if not v_ok:
                    print(f"  ⚠ VERIF ECHEC [{i+1}/{total}] {os.path.basename(fp)[:60]}: {v_msg}")
        else:
            failed += 1
            progress["failed"].append(fp)
            log_entry({
                "file": fp, "title": title, "status": "error",
                "size": len(content), "error": last_error,
                "attempts": attempt, "ts": time.time(),
            })
            if failed <= 10:
                print(f"  ECHEC [{i+1}/{total}] {os.path.basename(fp)[:60]}: {last_error[:120]}")

        # Delai entre requetes
        time.sleep(DELAY_SECONDS)

        # Rapport periodique + sauvegarde progres
        if (i + 1) % 20 == 0:
            elapsed = time.time() - start_time
            remaining = (elapsed / (imported + failed + skipped)) * (total - i - 1) if (imported + failed + skipped) > 0 else 0
            print(f"  [{i+1}/{total}] ✓{imported} ✗{failed} ↷{skipped} | {elapsed:.0f}s | ~{remaining:.0f}s restants")
            save_progress(progress)

    # ── Sauvegarde finale ──
    save_progress(progress)
    elapsed = time.time() - start_time

    print(f"\n{'='*60}")
    print(f"IMPORT TERMINE")
    print(f"  Importes : {imported}")
    print(f"  Echecs   : {failed}")
    print(f"  Ignores  : {skipped}")
    print(f"  Total    : {total}")
    print(f"  Duree    : {elapsed:.0f}s ({elapsed/60:.1f} min)")
    print(f"  Log      : {LOG_FILE}")
    print(f"  Progres  : {PROGRESS_FILE}")

    if failed > 0:
        print(f"\n⚠ {failed} echecs. Relance le script pour retenter (la progress file evite les doublons).")

    # Email de rapport
    send_report_email(imported, failed, skipped, total, elapsed, progress)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
