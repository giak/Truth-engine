#!/usr/bin/env python3
"""
Génère des graphes Mermaid de saturation du corpus Truth Engine.
- Graphe 1 : cooccurrence des symboles (quels symboles apparaissent ensemble)
- Graphe 2 : clusters dominants et leur hiérarchie
- Graphe 3 : architecture du corpus (secteurs → clusters → symboles)
"""

import json
import os
from pathlib import Path
from collections import defaultdict, Counter

INVESTIGATIONS_DIR = Path("investigations")
OUTPUT_DIR = Path("outputs")

def parse_all_investigations():
    """Parse all investigation files to extract symbole and cluster cooccurrence"""
    # Symbol cooccurrence: for each file, record which symbols appear together
    symbol_pairs = Counter()
    file_symbols = {}  # filename -> set of symbols
    
    # Cluster cooccurrence  
    cluster_pairs = Counter()
    file_clusters = {}  # filename -> set of clusters
    
    for root, dirs, files in os.walk(INVESTIGATIONS_DIR):
        for f in files:
            if not f.endswith('.md') or f == 'README.md':
                continue
            filepath = Path(root) / f
            try:
                content = filepath.read_text()
            except:
                continue
            
            # Extract symbols
            symbols = set()
            in_sym = False
            for line in content.split('\n'):
                if '### Symbol Scores' in line:
                    in_sym = True
                    continue
                if in_sym and line.startswith('|') and '**' in line:
                    parts = line.split('|')
                    if len(parts) >= 2:
                        sym = parts[1].strip().replace('**', '')
                        if len(sym) <= 3 and sym:
                            symbols.add(sym)
                elif in_sym and (line.startswith('## ') or line.startswith('### ') and 'Pattern' in line):
                    break
            
            # Extract clusters from LOADED line
            clusters = set()
            for line in content.split('\n'):
                if '**LOADED:**' in line:
                    import re
                    matches = re.findall(r'([A-Z_]+)\(', line)
                    clusters = set(matches)
                    break
            
            if symbols:
                file_symbols[str(filepath)] = symbols
                # Count pairs
                syms = sorted(symbols)
                for i in range(len(syms)):
                    for j in range(i+1, len(syms)):
                        pair = tuple(sorted([syms[i], syms[j]]))
                        symbol_pairs[pair] += 1
            
            if clusters:
                file_clusters[str(filepath)] = clusters
                cls = sorted(clusters)
                for i in range(len(cls)):
                    for j in range(i+1, len(cls)):
                        pair = tuple(sorted([cls[i], cls[j]]))
                        cluster_pairs[pair] += 1
    
    return symbol_pairs, file_symbols, cluster_pairs, file_clusters


def generate_mermaid_symbols(symbol_pairs, file_symbols):
    """Mermaid graph: symbol cooccurrence network"""
    
    # Count single symbol occurrences
    sym_counts = Counter()
    for syms in file_symbols.values():
        sym_counts.update(syms)
    
    # Use top 8 symbols
    top_syms = [s[0] for s in sym_counts.most_common(8)]
    sym_names = {
        'Ξ': 'Iceberg', '↕': 'Power', '€': 'Money', 'Λ': 'Framing',
        'Ω': 'Inversion', '🌐': 'Network', 'Κ': 'Cynical', '⏰': 'Temporal',
    }
    
    # Build edges for top symbols
    edges = []
    for (a, b), count in symbol_pairs.items():
        if a in top_syms and b in top_syms:
            if count >= 10:
                edges.append((a, b, count))
    
    edges.sort(key=lambda x: -x[2])
    
    lines = []
    lines.append("```mermaid")
    lines.append("graph TD")
    lines.append("    %% Cooccurrence des symboles — corpus Truth Engine (100 dossiers)")
    lines.append("")
    
    for sym in top_syms:
        name = sym_names.get(sym, sym)
        cnt = sym_counts.get(sym, 0)
        lines.append(f"    {sym}[{sym}<br/>{name}<br/>{cnt} fichiers]")
    
    lines.append("")
    max_c = max(c for _, _, c in edges) if edges else 1
    for a, b, count in edges[:20]:
        thickness = max(1, int(count / max_c * 5))
        label = f"{count}"
        lines.append(f"    {a} -->|{label}| {b}")
    
    lines.append("```")
    return "\n".join(lines)


def generate_mermaid_clusters(cluster_pairs, file_clusters):
    """Mermaid graph: cluster hierarchy"""
    cl_counts = Counter()
    for cls in file_clusters.values():
        cl_counts.update(cls)
    
    top_cl = [c[0] for c in cl_counts.most_common(8)]
    
    edges = []
    for (a, b), count in cluster_pairs.items():
        if a in top_cl and b in top_cl:
            if count >= 8:
                edges.append((a, b, count))
    edges.sort(key=lambda x: -x[2])
    
    lines = []
    lines.append("```mermaid")
    lines.append("graph TD")
    lines.append("    %% Hiérarchie des clusters — corpus Truth Engine (100 dossiers)")
    lines.append("")
    
    for cl in top_cl:
        cnt = cl_counts.get(cl, 0)
        lines.append(f"    {cl}[{cl}<br/>{cnt} fichiers]")
    
    lines.append("")
    for a, b, count in edges[:15]:
        lines.append(f"    {a} -->|{count}| {b}")
    
    lines.append("```")
    return "\n".join(lines)


def generate_mermaid_architecture():
    """Mermaid graph: architecture du corpus en 3 strates"""
    lines = []
    lines.append("```mermaid")
    lines.append("graph TB")
    lines.append("    %% Architecture du corpus Truth Engine — 100 dossiers KERNEL APEX")
    lines.append("")
    lines.append("    subgraph STRATE_1[\"Strate 1 : Secteurs couverts (23)\"]")
    lines.append("        A1[Énergie/Nucléaire]")
    lines.append("        A2[Agriculture]")
    lines.append("        A3[Eau/Veolia]")
    lines.append("        A4[Pharma/Santé]")
    lines.append("        A5[Banques]")
    lines.append("        A6[Assurances/Mutuelles]")
    lines.append("        A7[Télécoms]")
    lines.append("        A8[Défense/Armement]")
    lines.append("        A9[Retraites]")
    lines.append("        A10[Immobilier]")
    lines.append("        A11[Luxe]")
    lines.append("        A12[Automobile]")
    lines.append("        A13[Aéronautique]")
    lines.append("        A14[Alimentation]")
    lines.append("        A15[Distribution]")
    lines.append("        A16[Sport/PSG]")
    lines.append("        A17[Narcotrafic]")
    lines.append("        A18[BTP/Concessions]")
    lines.append("        A19[Épargne]")
    lines.append("        A20[Forêts/Biodiversité]")
    lines.append("        A21[Pêche]")
    lines.append("        A22[Protection Sociale]")
    lines.append("        A23[Police]")
    lines.append("    end")
    lines.append("")
    lines.append("    subgraph STRATE_2[\"Strate 2 : Clusters dominants\"]")
    lines.append("        B1[ICEBERG<br/>30 fichiers]")
    lines.append("        B2[MONEY<br/>27 fichiers]")
    lines.append("        B3[POWER<br/>28 fichiers]")
    lines.append("        B4[FRAMING<br/>27 fichiers]")
    lines.append("        B5[INVERSION<br/>26 fichiers]")
    lines.append("        B6[NETWORK<br/>20 fichiers]")
    lines.append("        B7[CYNICAL<br/>17 fichiers]")
    lines.append("        B8[TEMPORAL<br/>17 fichiers]")
    lines.append("    end")
    lines.append("")
    lines.append("    subgraph STRATE_3[\"Strate 3 : Symboles (EDI moyen 0.62)\"]")
    lines.append("        C1[Ξ ICEBERG<br/>57%% couverture]")
    lines.append("        C2[€ MONEY<br/>53%% couverture]")
    lines.append("        C3[↕ POWER<br/>48%% couverture]")
    lines.append("        C4[Λ FRAMING<br/>54%% couverture]")
    lines.append("        C5[Ω INVERSION<br/>52%% couverture]")
    lines.append("    end")
    lines.append("")
    lines.append("    A1 --> B1")
    lines.append("    A2 --> B1")
    lines.append("    A3 --> B1")
    lines.append("    A4 --> B2")
    lines.append("    A5 --> B2")
    lines.append("    A6 --> B2")
    lines.append("    B1 --> C1")
    lines.append("    B2 --> C2")
    lines.append("    B3 --> C3")
    lines.append("    B4 --> C4")
    lines.append("    B5 --> C5")
    lines.append("")
    lines.append("    CORPORA[\"112 posts Substack<br/>+ 100 dossiers KERNEL<br/>= 212 unités\"]")
    lines.append("    CORPORA -.-> STRATE_1")
    lines.append("```")
    return "\n".join(lines)


def main():
    print("Parsing investigations...")
    symbol_pairs, file_symbols, cluster_pairs, file_clusters = parse_all_investigations()
    
    print(f"  Parsed {len(file_symbols)} files with symbols, {len(file_clusters)} files with clusters")
    print(f"  Found {len(symbol_pairs)} symbol pairs, {len(cluster_pairs)} cluster pairs")
    
    # Generate Mermaid graphs
    mermaid_symbols = generate_mermaid_symbols(symbol_pairs, file_symbols)
    mermaid_clusters = generate_mermaid_clusters(cluster_pairs, file_clusters)
    mermaid_arch = generate_mermaid_architecture()
    
    # Assemble final report
    with open(OUTPUT_DIR / "graphe_saturation_corpus.md", 'w') as f:
        f.write("# GRAPHE DE SATURATION — CORPUS TRUTH ENGINE\n\n")
        f.write(f"**Date :** 2026-07-09 | **Méthode :** extraction Python + Mermaid\n\n")
        f.write(f"**100 dossiers KERNEL, 112 posts Substack, 212 unités documentaires.**\n\n")
        f.write("## 1. Cooccurrence des symboles\n\n")
        f.write("Les arêtes montrent quels symboles apparaissent ensemble dans les mêmes fichiers. Épaisseur = fréquence.\n\n")
        f.write(mermaid_symbols)
        f.write("\n\n---\n\n")
        f.write("## 2. Hiérarchie des clusters\n\n")
        f.write("Les arêtes montrent quels clusters cooccurrent. Épaisseur = fréquence.\n\n")
        f.write(mermaid_clusters)
        f.write("\n\n---\n\n")
        f.write("## 3. Architecture du corpus\n\n")
        f.write("Vue en 3 strates : secteurs → clusters → symboles.\n\n")
        f.write(mermaid_arch)
        f.write("\n\n---\n\n")
        f.write("*Graphes générés automatiquement — rendus dans tout visualiseur Mermaid (GitHub, VS Code, mermaid.live).*\n")
    
    print(f"\n✅ Rapport + graphes écrits dans {OUTPUT_DIR / 'graphe_saturation_corpus.md'}")
    top_syms_set = set('Ξ↕€ΛΩ🌐Κ⏰')
    strong_sym = [1 for ((a,b),c) in symbol_pairs.items() if c>=10 and a in top_syms_set and b in top_syms_set]
    print(f"   Graphe 1 : cooccurrence symboles — {len(strong_sym)} arêtes fortes")
    top_cls = set(['ICEBERG', 'MONEY', 'POWER', 'FRAMING', 'INVERSION', 'NETWORK', 'CYNICAL', 'TEMPORAL'])
    strong_cl = [1 for ((a,b),c) in cluster_pairs.items() if c>=8 and a in top_cls and b in top_cls]
    print(f"   Graphe 2 : hiérarchie clusters — {len(strong_cl)} arêtes fortes")
    print(f"   Graphe 3 : architecture 3 strates")


if __name__ == '__main__':
    main()
