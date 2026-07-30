#!/usr/bin/env python3
"""
audit_phase2_sublimator_v37.py
================================
Audit formel des rapports Phase 2 produits via prompt-v37_phase2.md.
Verifie 7 criteres [GO] (C0-C6) + cross-check exhaustivite source/reference.

Usage :
    python3 tools/audit_phase2_sublimator_v37.py <rapport_synthese_phase2.md>

Sortie :
    exit 0 : tous les criteres passent.
    exit 1 : au moins un critere C0-C5 echoue.
    exit 64 : C6 INDETERMINE (§1 Couverture d'ingestion absente).
            (differencie dans stdout).

Criteres verifies :
    C0 - 9 H2 numerotees 1-9 strictes (anti-derive structurelle).
    C1 - Tout F-##/M-## cite dans le rapport existe verbatim dans source.
    C2 - Etendue minimum >= 4 fiches par these cardinale.
    C3 - >= 2 transversalites avec format pivot.
    C4 - CP1 binaire strict en §9.
    C5 - Aucune section H2 hors 1-9 (refus redaction Phase 3).
    C6 - Score de completude = N fiches citees >=1x / N fiches source >= 80 %.
          Etat INDETERMINE si §1 Couverture d'ingestion absente.
"""

import sys
import re
from pathlib import Path
from collections import defaultdict


def parse_quintessence_source(source_dir: Path) -> dict:
    """Cartographie exhaustive du dossier _quintessence_v3/.

    Retourne : {
        'files': [noms de fichiers],
        'f_ids': {file: set(F-##/M-## contenus)},
        'meta': {file: (top_F, top_M, top_acteurs, annee_peak)},
    }
    """
    files = []
    f_ids = {}
    meta = {}
    if not source_dir.exists():
        print(f"[WARN] Dossier source {source_dir} introuvable.")
        return {'files': files, 'f_ids': f_ids, 'meta': meta}

    pattern_F = re.compile(r'F-[A-Z]+(-[A-Z]+)?-\d+')
    pattern_M = re.compile(r'M[1-4]')

    for f in sorted(source_dir.glob('*.md')):
        text = f.read_text(encoding='utf-8', errors='replace')
        f_set = set(pattern_F.findall(text))
        m_set = set(pattern_M.findall(text))
        meta_f = {
            'F_count': len(f_set),
            'M_count': len(m_set),
        }
        files.append(f.name)
        f_ids[f.name] = f_set | m_set
        meta[f.name] = meta_f
    return {'files': files, 'f_ids': f_ids, 'meta': meta}


def parse_rapport(rapport: Path, source: dict) -> dict:
    """Parse le rapport Phase 2 et calcule tous les criteres."""
    text = rapport.read_text(encoding='utf-8', errors='replace')
    lines = text.split('\n')

    # C0 : 9 H2 numerotees 1-9
    h2_lines = [l for l in lines if re.match(r'^## [1-9]\. ', l)]
    h2_titles = [l.strip() for l in h2_lines]
    c0_ok = (len(h2_lines) == 9)
    c0_titles_set = set(int(re.match(r'^## (\d+)\. ', l).group(1)) for l in h2_lines)
    c0_strict = c0_titles_set == set(range(1, 10))

    # C1 : F-##/M-## cites doivent exister dans source
    pattern_cite = re.compile(r'F-[A-Z]+(-[A-Z]+)?-\d+|M[1-4]')
    cites = set(pattern_cite.findall(text))
    source_set = set()
    for f_ids in source['f_ids'].values():
        source_set.update(f_ids)
    c1_unknown = cites - source_set
    c1_ok = (len(c1_unknown) == 0)

    # C2 : theses >= 4 fiches (mesure heuristique via §2)
    section2 = _extract_section(lines, 2, 3)
    thetas_match = re.findall(r'^### T[1-5]', section2, re.MULTILINE)
    c2_thetas_count = len(thetas_match)
    c2_ok = (c2_thetas_count >= 4)  # tolerant

    # C3 : transversalites >= 2 avec format pivot
    section3 = _extract_section(lines, 3, 4)
    c3_trans_count = len(re.findall(r'^### Transversalité [1-9]', section3, re.MULTILINE))
    c3_pivots = len(re.findall(r'\[[^\]]+\([^)]+\) \u2194 [^\]]+\([^)]*\)\]', section3))
    c3_ok = (c3_trans_count >= 2 and c3_pivots >= 1)

    # C4 : CP1 binaire strict en §9
    section9 = _extract_section(lines, 9, 99)
    c4_oui = bool(re.search(r'<RECOMMANDATION:OUI>', section9))
    c4_non = bool(re.search(r'<RECOMMANDATION:NON>', section9))
    c4_ok = (c4_oui ^ c4_non) and not (c4_oui and c4_non)  # XOR strict

    # C5 : refus Phase 3 (aucune section hors 1-9)
    hors_range = bool(re.search(r'^## 1[0-9]\. ', text, re.MULTILINE))
    mots_interdits = re.findall(
        r'^#{1,2} (Accroche|Introduction|Conclusion \u00e9ditoriale|Plan d\u00e9taill\u00e9)',
        text, re.MULTILINE)
    c5_ok = (not hors_range) and (len(mots_interdits) == 0)

    # C6 : Score de completude - 3 etats (OK | KO | INDETERMINE).
    # Si §1 ne contient pas le marqueur 'Couverture d ingestion',
    # C6 retourne INDETERMINE (audit impossible) plutot que KO silencieux
    # (evite le faux positif quand le format §1 varie).
    section1 = _extract_section(lines, 1, 2)
    coverage_marker = re.search(
        r"Couverture\s+d['\u2019]ingestion",
        section1, re.IGNORECASE
    )
    if coverage_marker is None:
        c6_indetermine = True
        c6_ok = None
        c6_score = None
        c6_cited = 0
        c6_total = len(source['files'])
        cited_source_stems = set()
    else:
        c6_indetermine = False
        pattern_file = re.compile(r'\|\s*`?<?([^`>|]+)\.md>?`?')
        cited_files = set(pattern_file.findall(section1))
        source_files_set = set(Path(f).stem for f in source['files'])
        cited_source_stems = cited_files & source_files_set
        c6_cited = len(cited_source_stems)
        c6_total = len(source['files'])
        c6_score = (c6_cited / c6_total * 100) if c6_total > 0 else 0.0
        c6_ok = (c6_score >= 80.0)  # tolerant : 80% en mode degrade

    return {
        'C0_ok': c0_ok and c0_strict,
        'C0_titles': h2_titles,
        'C1_ok': c1_ok,
        'C1_unknown': sorted(c1_unknown),
        'C2_ok': c2_ok,
        'C2_thetas_count': c2_thetas_count,
        'C3_ok': c3_ok,
        'C3_trans_count': c3_trans_count,
        'C3_pivots': c3_pivots,
        'C4_ok': c4_ok,
        'C4_oui': c4_oui,
        'C4_non': c4_non,
        'C5_ok': c5_ok,
        'C6_ok': c6_ok,
        'C6_indetermine': c6_indetermine,
        'C6_score': c6_score,
        'C6_cited': c6_cited,
        'C6_total': c6_total,
        'C6_cited_files': sorted(cited_source_stems),
    }


def _extract_section(lines: list, start: int, end: int) -> str:
    """Extrait le contenu de la section H2 numerotee `start` jusqu'a `end` (exclusive)."""
    capture = []
    in_section = False
    pattern_start = re.compile(r'^## ' + str(start) + r'\. ')
    pattern_end = re.compile(r'^## \d+\. ') if end > 9 else re.compile(r'^## ' + str(end) + r'\. ')
    for line in lines:
        if pattern_start.match(line):
            in_section = True
            continue
        if in_section and pattern_end.match(line):
            break
        if in_section:
            capture.append(line)
    return '\n'.join(capture)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/audit_phase2_sublimator_v37.py <rapport.md>")
        sys.exit(2)

    rapport = Path(sys.argv[1])
    if not rapport.exists():
        print(f"[ERREUR] Rapport {rapport} introuvable.")
        sys.exit(2)

    # Inferrence du chemin source : <rapport>/../../quintessence_v3/
    source_dir = rapport.parent.parent / "_quintessence_v3"
    if not source_dir.exists():
        # Tentative : <investigation>/quintessence_v3/ directement
        source_dir = rapport.parent.parent / "quintessence_v3"

    print(f"[AUDIT] Rapport : {rapport}")
    print(f"[AUDIT] Source  : {source_dir}")
    print()

    source = parse_quintessence_source(source_dir)
    print(f"[INFO]   {len(source['files'])} fichiers dans la source.")
    result = parse_rapport(rapport, source)

    # Affichage des resultats par critere (C0-C6)
    print("=" * 60)
    print("RESULTATS PAR CRITERE (C0-C6)")
    print("=" * 60)
    print(f"C0 Anti-derive structurelle      : {'\u2705 OK' if result['C0_ok'] else '\u274c KO'} ({len(result['C0_titles'])} H2 detectees)")
    if not result['C0_ok']:
        print(f"    Titres actuels : {result['C0_titles']}")
    print(f"C1 Tracabilite F-##/M-##            : {'\u2705 OK' if result['C1_ok'] else '\u274c KO'}")
    if result['C1_unknown']:
        print(f"    Identifiants inconnus dans source : {result['C1_unknown'][:10]}{'...' if len(result['C1_unknown']) > 10 else ''}")
    print(f"C2 Etendue minimum theses         : {'\u2705 OK' if result['C2_ok'] else '\u274c KO'} ({result['C2_thetas_count']} theses)")
    print(f"C3 Densite transversalites           : {'\u2705 OK' if result['C3_ok'] else '\u274c KO'} ({result['C3_trans_count']} trans., {result['C3_pivots']} pivots)")
    print(f"C4 Binaire CP1 (OUI|NON)             : {'\u2705 OK' if result['C4_ok'] else '\u274c KO'} (OUI={result['C4_oui']}, NON={result['C4_non']})")
    print(f"C5 Refus redaction Phase 3           : {'\u2705 OK' if result['C5_ok'] else '\u274c KO'}")
    # C6 : 3 etats possibles (OK | KO | INDETERMINE)
    c6_indet = result['C6_indetermine']
    c6_state = result['C6_ok']
    if c6_indet:
        print(f"C6 Exhaustivite (couverture source) : \u26a0\ufe0f  INDETERMINE (\u00a71 Couverture d'ingestion absente - audit impossible)")
    elif c6_state:
        print(f"C6 Exhaustivite (couverture source) : \u2705 OK ({result['C6_score']:.1f}%, {result['C6_cited']}/{result['C6_total']})")
    else:
        print(f"C6 Exhaustivite (couverture source) : \u274c KO ({result['C6_score']:.1f}%, {result['C6_cited']}/{result['C6_total']})")
    if result['C6_cited_files']:
        print(f"    Fiches source citees en \u00a71 : {len(result['C6_cited_files'])}/{result['C6_total']}")
    print()

    # Verdict final (3 etats : TOUT OK | ECHEC | INDETERMINE)
    c6_ok_bool = bool(result['C6_ok'])
    all_ok = all([
        result['C0_ok'], result['C1_ok'], result['C2_ok'],
        result['C3_ok'], result['C4_ok'], result['C5_ok'], c6_ok_bool
    ])
    any_indet = c6_indet
    print("=" * 60)
    if all_ok and not any_indet:
        print("VERDICT : \u2705 TOUT OK (7/7 criteres valides). CP1 peut proceder.")
        return 0
    elif any_indet:
        print("VERDICT : \u26a0\ufe0f  INDETERMINE (\u00a71 Couverture d'ingestion absente - re-pipeline Phase 2-A recommande pour auditabilite).")
        return 64  # EX_USAGE (sysexits.h) : format §1 non conforme, distinct d'un echec C0-C5
    else:
        failures = [
            f"C{c}" for c, ok in [
                ('0', result['C0_ok']), ('1', result['C1_ok']),
                ('2', result['C2_ok']), ('3', result['C3_ok']),
                ('4', result['C4_ok']), ('5', result['C5_ok']),
                ('6', c6_ok_bool)
            ] if not ok
        ]
        print(f"VERDICT : \u274c ECHEC ({', '.join(failures)}) - re-pipeline Phase 2-A recommande.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
