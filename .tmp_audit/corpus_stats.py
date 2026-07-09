#!/usr/bin/env python3
"""
Extraction statistique du corpus Truth Engine.
Parse tous les dossiers investigations/ pour extraire SYMBOLS, CLUSTERS, EDI.
Génère un bilan complet : symboles les plus scorés, clusters dominants, EDI moyen,
secteurs couverts vs manquants.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter

INVESTIGATIONS_DIR = Path("investigations")
OUTPUT_DIR = Path(".tmp_audit")

# Mapping des symboles vers leurs noms
SYMBOL_NAMES = {
    "Ξ": "Iceberg",
    "€": "Money",
    "Λ": "Framing",
    "Ω": "Inversion",
    "↕": "Power",
    "🌐": "Network",
    "Κ": "Cynical",
    "⏰": "Temporal",
    "⚔": "Warfare",
    "⚖": "Justice",
    "🏛": "Institution",
    "🌍": "Global",
    "🧠": "Psychology",
    "💀": "Death",
    "🔗": "Chain",
    "📜": "Law",
    "🏭": "Industry",
    "🛡": "Defense",
    "🗳": "Democracy",
    "💧": "Water",
    "🌾": "Agriculture",
    "💊": "Pharma",
    "⚡": "Energy",
    "🔄": "Cycle",
    "📊": "Data",
    "🎭": "Theatre",
    "🔫": "Weapon",
    "🧬": "Biology",
    "🏗": "Construction",
    "📡": "Telecom",
    "🎓": "Education",
    "🏥": "Health",
    "✝": "Religion",
    "👁": "Surveillance",
    "🔐": "Security",
}

# Catégories de l'INDEX.md
CATEGORIES = {
    "1. GÉOPOLITIQUE & CONFLITS": [
        "2026-03-02-iran-epstein", "2026-03-11-mercosur", "2026-03-11-sud-radio-nucleaire",
        "2026-03-12-sabotage-energetique", "2026-04-04-iran-2026", "2026-04-04-iran-guerre",
        "2026-04-21-iran-guerre-deep", "2026-04-03-ingerences-electorales-ue"
    ],
    "2. MÉDIAS, INFLUENCE & CAPTURE": [
        "2026-03-16-reseaux-influence", "2026-04-08-brivael-fr-piege-denonciation",
        "2026-04-09-commission-audiovisuel", "2026-04-09-commission-audiovisuel-public",
        "2026-04-10-capture-audiovisuel-public", "2026-05-20-capture-medias-souverainistes"
    ],
    "3. SYSTÈME FRANCE": [
        "2026-04-01-le-piege-est-boucle", "2026-04-01-pourquoi-le-systeme-va-craquer",
        "2026-04-03-confiance-et-point-de-rupture", "2026-04-05-systeme-france",
        "2026-04-08-etat-francais-inefficacite", "2026-05-21-etat-reel-france",
        "2026-05-23-macron-systeme-complet", "2026-05-27-gaspillage-etat",
        "2026-05-19-opposition-controlee"
    ],
    "3b. SECTORIEL — KERNEL APEX RÉCENT": [
        "2026-07-08_pyromane-pompier", "2026-07-08_depopulation",
        "2026-07-09_narcotrafic", "2026-07-09_eau-veolia-suez",
        "2026-07-09_pharma-capture", "2026-07-09_banques-cartel",
        "2026-07-09_assurances-mutuelles", "2026-07-09_normes-afnor-iso",
        "2026-07-09_cdc-bpifrance", "2026-07-09_conseil-etat",
        "2026-07-09_btp-concessions", "2026-07-09_philanthropie",
        "2026-07-09_gut-veme", "2026-07-09_logistique-ports",
        "2026-07-09_universites-recherche", "2026-07-09_corps-prefectoral",
        "2026-07-09_telecom-oligopole", "2026-07-09_sport-psg",
        "2026-07-09_alimentation", "2026-07-09_grande-distribution",
        "2026-07-09_defense", "2026-07-09_retraites",
        "2026-07-09_francafrique"
    ],
    "4. GÉOPOLITIQUE HISTORIQUE": [
        "2026-07-09_francafrique"
    ],
    "5. CONTRÔLE SOCIAL & RÉSISTANCE": [
        "2026-03-27-facturation-monopoles", "2026-03-28-empire-mensonge",
        "2026-04-17-controle-17avril", "2026-05-17-systeme-controle",
        "2026-05-28-resistance-comme-probleme"
    ],
    "6. ÉLITES, CASTES & POUVOIR": [
        "2026-03-28-satanisme-castes-elites", "2026-04-30-empire-mensonge",
        "2026-04-19-macron-divers"
    ],
    "7. POSSESSION & ENRACINEMENT": [
        "2026-04-12-bignon-possession", "2026-04-12-possession-enracinement",
        "2026-04-13-bignon-possession", "2026-04-13-enracinement",
        "2026-04-13-system-possession"
    ],
    "8. DÉCROISSANCE, TRAVAIL & ÉCONOMIE": [
        "2026-03-29-autoconsommation-effondrement", "2026-04-01-autoconsommation-systeme",
        "2026-03-30-decroissance-opposition", "2026-03-31-travail"
    ],
    "9. IA & ÉPISTÉMOLOGIE": [
        "2026-04-05-ia-epistemologie", "2026-04-05-coupure-epistemologique-ia",
        "2026-04-05-coupure-epistemologique-v2"
    ],
    "10. OAK ISLAND": [
        "2026-04-05-oak-island", "2026-04-05-oak-island-capture-cognitive",
        "2026-04-05-oak-island-super-enquete"
    ],
    "11. ENVIRONNEMENT & CLIMAT": [
        "2026-05-16-gerondeau-tocsin-giec", "2026-05-16-pollution-masking",
        "2026-05-19-chemtrails-v4"
    ],
    "12. SUJETS SPÉCIFIQUES MAI": [
        "2026-05-16-braun-pivet-senegal-homosexualite", "2026-05-16-braun-pivet-senegal-iceberg",
        "2026-05-16-creusot-loire-desindustrialisation", "2026-05-16-tanguy-energie-interview"
    ],
    "13. DIVERS & ORPHELINS": [
        "2026-02-divers", "2026-03-divers", "2026-04-divers", "2026-04-21-misc",
        "2026-06-28_16-03_debat-bfm-ukraine-russie"
    ],
}


def find_dossiers():
    """Trouve tous les dossiers dans investigations/"""
    dossiers = []
    for entry in sorted(os.listdir(INVESTIGATIONS_DIR)):
        path = INVESTIGATIONS_DIR / entry
        if path.is_dir() and entry != "__pycache__":
            dossiers.append(entry)
    return dossiers


def find_investigation_files(dossier_name):
    """Trouve le fichier INVESTIGATION principal dans un dossier"""
    dossier_path = INVESTIGATIONS_DIR / dossier_name
    if not dossier_path.exists():
        return []
    
    files = []
    for f in sorted(os.listdir(dossier_path)):
        if f.endswith(".md") and f != "README.md":
            files.append(dossier_path / f)
    return files


def extract_symbols(content):
    """Extrait la table des symboles du §2 MANIPULATION_REPORT"""
    symbols = []
    in_table = False
    
    for line in content.split("\n"):
        line = line.strip()
        
        if "### Symbol Scores" in line:
            in_table = True
            continue
        
        if in_table:
            if line.startswith("### ") or line.startswith("## "):
                break
            if line.startswith("|") and not line.startswith("| Sym") and not line.startswith("|---"):
                parts = [p.strip() for p in line.split("|")]
                parts = [p for p in parts if p]
                if len(parts) >= 5:
                    sym_raw = parts[0]
                    sym_clean = sym_raw.replace("**", "").strip()
                    name = parts[1].strip()
                    try:
                        raw = int(parts[2])
                        clamp = float(parts[3])
                    except (ValueError, IndexError):
                        raw = 0
                        clamp = 0.0
                    symbols.append({
                        "symbol": sym_clean,
                        "name": name,
                        "raw": raw,
                        "clamp": clamp,
                    })
    
    return symbols


def extract_clusters(content):
    """Extrait la ligne CLUSTERS du §2 MANIPULATION_REPORT"""
    # Pattern: **LOADED:** ICEBERG(Ξ:8) + MONEY(€:9) + FRAMING(Λ:4.8) + ...
    match = re.search(r'\*\*LOADED:\*\*\s*(.+?)(?:\n|$)', content)
    if not match:
        return []
    
    loaded = match.group(1).strip()
    # Parse each cluster: NAME(SYM:VAL)
    clusters = []
    # Split on " + " 
    parts = loaded.split(" + ")
    for part in parts:
        part = part.strip()
        # Extract NAME(SYM:VALUE)
        m = re.match(r'([^(]+)\(([^:]+):([\d.]+)\)', part)
        if m:
            clusters.append({
                "name": m.group(1).strip(),
                "symbol": m.group(2).strip(),
                "value": float(m.group(3)),
            })
    
    return clusters


def extract_edi(content):
    """Extrait le score EDI depuis le FACT_REGISTRY"""
    # Pattern: ✦=8 ✧=2. EDI: 0.80
    match = re.search(r'EDI:\s*([\d.]+)', content)
    if match:
        return float(match.group(1))
    
    # Alternative pattern in newer files
    match = re.search(r'✦=(\d+)\s+✧=(\d+)', content)
    if match:
        stars = int(match.group(1))
        diamonds = int(match.group(2))
        total = stars + diamonds
        if total > 0:
            return round(stars / total, 2)
    
    return None


def extract_complexity(content):
    """Extrait la complexité depuis l'en-tête"""
    match = re.search(r'Complexité\s*\*\s*:\s*(\d+)/(\d+)', content)
    if match:
        return int(match.group(1))
    return None


def extract_title(content):
    """Extrait le titre depuis le header"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def extract_civ(content):
    """Extrait le CIV"""
    match = re.search(r'CIV:\*\*\s*(\S+)', content)
    if match:
        return match.group(1)
    return None


def get_category(dossier_name):
    """Détermine la catégorie du dossier"""
    for cat, dossiers in CATEGORIES.items():
        if dossier_name in dossiers:
            return cat
    return "NON CLASSÉ"


def count_md_files(dossier_name):
    """Compte les fichiers .md dans un dossier"""
    dossier_path = INVESTIGATIONS_DIR / dossier_name
    if not dossier_path.exists():
        return 0
    return len([f for f in os.listdir(dossier_path) if f.endswith(".md")])


def main():
    dossiers = find_dossiers()
    
    # Accumulateurs
    all_symbols = []  # (sym, name, raw, clamp) per file
    symbol_occurrences = Counter()  # combien de fichiers utilisent ce symbole
    symbol_raw_sums = defaultdict(float)
    symbol_clamp_sums = defaultdict(float)
    
    all_clusters = []  # (name, symbol, value) per file
    cluster_occurrences = Counter()  # combien de fichiers utilisent ce cluster
    cluster_value_sums = defaultdict(float)
    
    edi_scores = []
    complexity_scores = []
    
    dossier_stats = []  # per-dossier summary
    
    files_parsed = 0
    files_with_symbols = 0
    files_with_edi = 0
    
    cat_counts = Counter()
    cat_edi_sums = defaultdict(float)
    cat_edi_counts = defaultdict(int)
    
    for dossier_name in dossiers:
        files = find_investigation_files(dossier_name)
        category = get_category(dossier_name)
        cat_counts[category] += 1
        
        for filepath in files:
            try:
                content = filepath.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            
            title = extract_title(content)
            symbols = extract_symbols(content)
            clusters = extract_clusters(content)
            edi = extract_edi(content)
            complexity = extract_complexity(content)
            civ = extract_civ(content)
            
            if not symbols and not edi:
                continue  # skip non-KERNEL files
            
            files_parsed += 1
            
            if symbols:
                files_with_symbols += 1
            
            if edi is not None:
                files_with_edi += 1
                edi_scores.append(edi)
                cat_edi_sums[category] += edi
                cat_edi_counts[category] += 1
            
            if complexity:
                complexity_scores.append(complexity)
            
            # Aggregate symbols
            file_sym_names = set()
            for s in symbols:
                all_symbols.append(s)
                symbol_occurrences[s["symbol"]] += 1
                symbol_raw_sums[s["symbol"]] += s["raw"]
                symbol_clamp_sums[s["symbol"]] += s["clamp"]
                file_sym_names.add(s["name"])
            
            # Aggregate clusters
            for c in clusters:
                all_clusters.append(c)
                cluster_occurrences[c["name"]] += 1
                cluster_value_sums[c["name"]] += c["value"]
            
            dossier_stats.append({
                "dossier": dossier_name,
                "file": filepath.name,
                "title": title,
                "civ": civ,
                "category": category,
                "symbols_count": len(symbols),
                "clusters_count": len(clusters),
                "edi": edi,
                "complexity": complexity,
                "symbols": [s["symbol"] for s in symbols],
            })
    
    # ==========================================
    # CALCUL DES STATISTIQUES AGRÉGÉES
    # ==========================================
    
    # SYMBOLES : top par fréquence et par score moyen
    sym_stats = []
    for sym, count in symbol_occurrences.items():
        name = SYMBOL_NAMES.get(sym, sym)
        avg_raw = symbol_raw_sums[sym] / count
        avg_clamp = symbol_clamp_sums[sym] / count
        sym_stats.append({
            "symbol": sym,
            "name": name,
            "occurrences": count,
            "avg_raw": round(avg_raw, 1),
            "avg_clamp": round(avg_clamp, 2),
            "coverage_pct": round(count / files_parsed * 100, 1) if files_parsed else 0,
        })
    
    sym_stats.sort(key=lambda x: x["occurrences"], reverse=True)
    
    # CLUSTERS : top par fréquence et par score moyen
    cl_stats = []
    for name, count in cluster_occurrences.items():
        avg_val = cluster_value_sums[name] / count
        cl_stats.append({
            "name": name,
            "occurrences": count,
            "avg_value": round(avg_val, 2),
            "coverage_pct": round(count / files_parsed * 100, 1) if files_parsed else 0,
        })
    
    cl_stats.sort(key=lambda x: x["occurrences"], reverse=True)
    
    # EDI stats
    avg_edi = round(sum(edi_scores) / len(edi_scores), 2) if edi_scores else 0
    edi_distribution = Counter()
    for e in edi_scores:
        bucket = f"{int(e * 10) / 10:.1f}"  # round to 0.1
        edi_distribution[bucket] += 1
    
    # Catégories stats
    cat_stats = []
    for cat, count in cat_counts.items():
        avg_edi_cat = round(cat_edi_sums[cat] / cat_edi_counts[cat], 2) if cat_edi_counts[cat] > 0 else None
        cat_stats.append({
            "category": cat,
            "dossiers": count,
            "files_with_kernel": cat_edi_counts[cat],
            "avg_edi": avg_edi_cat,
        })
    
    cat_stats.sort(key=lambda x: x["dossiers"], reverse=True)
    
    # ==========================================
    # GÉNÉRATION DU RAPPORT
    # ==========================================
    
    report = []
    report.append("# BILAN STATISTIQUE — CORPUS TRUTH ENGINE")
    report.append("")
    report.append(f"**Date :** 2026-07-09 | **Méthode :** extraction automatisée Python")
    report.append("")
    report.append("---")
    report.append("")
    
    # Vue d'ensemble
    report.append("## 1. VUE D'ENSEMBLE")
    report.append("")
    report.append("| Métrique | Valeur |")
    report.append("|----------|--------|")
    report.append(f"| Dossiers totaux | {len(dossiers)} |")
    report.append(f"| Fichiers .md totaux | {sum(count_md_files(d) for d in dossiers)} |")
    report.append(f"| Fichiers KERNEL APEX parsés | {files_parsed} |")
    report.append(f"| Fichiers avec SYMBOLS | {files_with_symbols} |")
    report.append(f"| Fichiers avec EDI | {files_with_edi} |")
    report.append(f"| Posts Substack | 112 |")
    report.append(f"| Période couverte | Février — Juillet 2026 |")
    report.append(f"| Complexité moyenne | {round(sum(complexity_scores) / len(complexity_scores), 1) if complexity_scores else 'N/A'}/18 |")
    report.append(f"| **EDI moyen** | **{avg_edi}** |")
    report.append("")
    
    # EDI distribution
    report.append("### 1.1 Distribution des scores EDI")
    report.append("")
    report.append("| EDI | Nombre de fichiers |")
    report.append("|-----|-------------------|")
    for bucket in sorted(edi_distribution.keys()):
        cnt = edi_distribution[bucket]
        bar = "█" * cnt
        report.append(f"| {bucket} | {cnt} {bar} |")
    report.append("")
    
    # EDI top and bottom
    edi_dossiers = [d for d in dossier_stats if d["edi"] is not None]
    edi_dossiers.sort(key=lambda x: x["edi"], reverse=True)
    
    report.append("### 1.2 Top 5 / Bottom 5 EDI")
    report.append("")
    report.append("| Rang | Dossier | EDI | CIV |")
    report.append("|------|---------|-----|-----|")
    for i, d in enumerate(edi_dossiers[:5]):
        report.append(f"| 🥇{i+1} | {d['title'][:60] if d['title'] else d['file']} | {d['edi']:.2f} | {d['civ'] or '—'} |")
    report.append("| ... | ... | ... | ... |")
    for i, d in enumerate(edi_dossiers[-5:]):
        report.append(f"| {len(edi_dossiers)-4+i} | {d['title'][:60] if d['title'] else d['file']} | {d['edi']:.2f} | {d['civ'] or '—'} |")
    report.append("")
    
    # SYMBOLES
    report.append("---")
    report.append("")
    report.append("## 2. SYMBOLES — TOP 10")
    report.append("")
    report.append("| Sym | Nom | Occurrences | Couverture | Score Raw ∅ | Score Clamp ∅ |")
    report.append("|-----|-----|-------------|------------|-------------|---------------|")
    for s in sym_stats[:12]:
        report.append(f"| **{s['symbol']}** | {s['name']} | {s['occurrences']} | {s['coverage_pct']}% | {s['avg_raw']} | {s['avg_clamp']} |")
    report.append("")
    
    # Tous les symboles
    report.append("### 2.1 Tous les symboles")
    report.append("")
    report.append("| Sym | Nom | Occ. | ∅ Raw | ∅ Clamp |")
    report.append("|-----|-----|------|-------|---------|")
    for s in sym_stats:
        report.append(f"| **{s['symbol']}** | {s['name']} | {s['occurrences']} | {s['avg_raw']} | {s['avg_clamp']} |")
    report.append("")
    
    # CLUSTERS
    report.append("---")
    report.append("")
    report.append("## 3. CLUSTERS DOMINANTS")
    report.append("")
    report.append("| Rang | Cluster | Occurrences | Couverture | Valeur ∅ |")
    report.append("|------|---------|-------------|------------|----------|")
    for i, c in enumerate(cl_stats[:12]):
        bar = "█" * min(c["occurrences"], 20)
        report.append(f"| {i+1} | **{c['name']}** | {c['occurrences']} | {c['coverage_pct']}% | {c['avg_value']} |")
    report.append("")
    
    # CATÉGORIES
    report.append("---")
    report.append("")
    report.append("## 4. SECTEURS COUVERTS")
    report.append("")
    report.append("| Catégorie | Dossiers | Fichiers KERNEL | EDI ∅ |")
    report.append("|-----------|----------|-----------------|-------|")
    for c in cat_stats:
        edi_str = f"{c['avg_edi']:.2f}" if c['avg_edi'] is not None else "N/A"
        report.append(f"| {c['category']} | {c['dossiers']} | {c['files_with_kernel']} | {edi_str} |")
    report.append("")
    
    # SECTEURS MANQUANTS
    report.append("---")
    report.append("")
    report.append("## 5. SECTEURS MANQUANTS (angles morts)")
    report.append("")
    
    sectors_covered = {
        "Assurances/Mutuelles": True,
        "Normes techniques (AFNOR/ISO)": True,
        "CDC/Bpifrance": True,
        "Conseil d'État": True,
        "BTP/Concessions": True,
        "Philanthropie": True,
        "Logistique/Ports": True,
        "Universités/Recherche": True,
        "Corps préfectoral": True,
        "Télécoms": True,
        "Sport/PSG": True,
        "Alimentation/Agroalimentaire": True,
        "Grande distribution": True,
        "Armée/Défense": True,
        "Retraites": True,
        "Eau/Veolia": True,
        "Pharma/Santé": True,
        "Banques": True,
        "Narcotrafic": True,
        "Françafrique": True,
        "Dépopulation": True,
        "Pyromane-pompier": True,
        "Médias/Audiovisuel": True,
        "Justice": True,
        "Dette/Finances": True,
        "Europe/UE": True,
        "Agriculture": True,
        "Énergie/Nucléaire": True,
        "Mercosur": True,
        "Iran/Guerre": True,
        "Ingérences électorales": True,
        "Contrôle social": True,
        "Facturation électronique": True,
        "Élites/Castes": True,
        "Décroissance": True,
        "Travail": True,
        "IA/Épistémologie": True,
        "Climat/Environnement": True,
        "Chemtrails": True,
        "Opposition contrôlée": True,
    }
    
    missing_sectors = [
        "Aéronautique civile (Airbus, Boeing)",
        "Automobile (Stellantis, Renault) — pas d'enquête dédiée",
        "Assurance-vie/Épargne (hors retraites)",
        "Art/Culture/Musées (hors philanthropie)",
        "Forêts/Biodiversité (hors climat)",
        "Pêche/Pêche industrielle",
        "Transports ferroviaires (SNCF, ouverture concurrence)",
        "Éditeurs/Logiciels (SAP, Microsoft, Dassault Systèmes)",
        "Désinformation/Propagande (analyse technique, pas couvert)",
        "Fiscalité locale/Taxe foncière",
        "Immobilier/Logement (crise du logement)",
        "Protection sociale hors retraite (chômage, famille, dépendance)",
        "Outre-mer/DOM-TOM",
        "Police (IGPN, maintien de l'ordre) — couvert partiellement",
        "Renseignement (DGSE, DGSI) — couvert partiellement",
        "Presse écrite hors Le Figaro/Le Monde",
        "Startups/Licorne française (Doctolib, Back Market, Qonto)",
        "Luxe (LVMH, Kering, Hermès) — couvert par philanthropie mais pas dédié",
        "Tabac/Alcool",
        "Jeux d'argent (FDJ, casinos)",
    ]
    
    report.append("| # | Secteur manquant | Priorité |")
    report.append("|---|------------------|----------|")
    for i, s in enumerate(missing_sectors):
        prio = "🔴" if i < 5 else ("🟠" if i < 10 else "🟡")
        report.append(f"| {i+1} | {s} | {prio} |")
    report.append("")
    
    # RÉSUMÉ FINAL
    report.append("---")
    report.append("")
    report.append("## 6. RÉSUMÉ SYNTHÉTIQUE")
    report.append("")
    report.append(f"- **{len(dossiers)} dossiers**, **{files_parsed} fichiers KERNEL APEX** parsés")
    report.append(f"- **EDI moyen : {avg_edi}** (plage : {min(edi_scores):.2f} — {max(edi_scores):.2f})")
    report.append(f"- **{len(sym_stats)} symboles distincts**, {len(cl_stats)} clusters distincts")
    
    top3_sym = sym_stats[:3]
    report.append(f"- **Top 3 symboles :** {top3_sym[0]['name']} ({top3_sym[0]['symbol']}, {top3_sym[0]['coverage_pct']}%), {top3_sym[1]['name']} ({top3_sym[1]['symbol']}, {top3_sym[1]['coverage_pct']}%), {top3_sym[2]['name']} ({top3_sym[2]['symbol']}, {top3_sym[2]['coverage_pct']}%)")
    
    top3_cl = cl_stats[:3]
    report.append(f"- **Top 3 clusters :** {top3_cl[0]['name']} ({top3_cl[0]['coverage_pct']}%), {top3_cl[1]['name']} ({top3_cl[1]['coverage_pct']}%), {top3_cl[2]['name']} ({top3_cl[2]['coverage_pct']}%)")
    
    report.append(f"- **{len(edi_distribution)} paliers EDI** distincts")
    report.append(f"- **{len(missing_sectors)} secteurs manquants** identifiés")
    report.append("")
    report.append("---")
    report.append("")
    report.append("*Rapport généré automatiquement par `corpus_stats.py` — 2026-07-09*")
    
    # Écrire le rapport
    output_path = OUTPUT_DIR / "bilan_statistique_corpus.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(report))
    
    print(f"✅ Rapport écrit dans {output_path}")
    print(f"   {len(dossiers)} dossiers, {files_parsed} fichiers KERNEL parsés")
    print(f"   EDI moyen : {avg_edi}")
    print(f"   {len(sym_stats)} symboles, {len(cl_stats)} clusters")
    
    # JSON export for further processing
    json_path = OUTPUT_DIR / "bilan_statistique_corpus.json"
    json_data = {
        "total_dossiers": len(dossiers),
        "total_md_files": sum(count_md_files(d) for d in dossiers),
        "files_parsed": files_parsed,
        "files_with_symbols": files_with_symbols,
        "files_with_edi": files_with_edi,
        "avg_edi": avg_edi,
        "edi_range": [min(edi_scores) if edi_scores else 0, max(edi_scores) if edi_scores else 0],
        "avg_complexity": round(sum(complexity_scores) / len(complexity_scores), 1) if complexity_scores else None,
        "symbols_stats": sym_stats,
        "clusters_stats": cl_stats,
        "categories": cat_stats,
        "edi_distribution": {k: v for k, v in sorted(edi_distribution.items())},
        "missing_sectors": missing_sectors,
    }
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2))
    print(f"✅ JSON écrit dans {json_path}")


if __name__ == "__main__":
    main()
