#!/usr/bin/env python3
import os
import re

INSERT_BLOCK = """### Priorities (verify first)

1. Vérifier les données primaires (sources officielles)
2. Croiser les chiffres avec rapports Cour des comptes
3. Documenter les conflits d'intérêts et pantouflage

### QUERY_GUIDANCE

1. @WEB sources officielles chiffres clés
2. @WEB rapports Cour des comptes secteur
3. @WEB enquêtes Mediapart ou presse

### BIAS TEST

- **Biais :** L'enquête postule que la capture est systémique — certains acteurs opèrent dans le cadre légal.
- **Angle mort :** Le secteur a aussi des externalités positives non documentées.
- **Facteur auto-critique :** La régulation et la transparence progressent dans certains domaines.
"""

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check what's already present
    has_priorities = '### Priorities' in content
    has_query = '### QUERY_GUIDANCE' in content
    has_bias = '### BIAS TEST' in content
    
    if has_priorities and has_query and has_bias:
        return False, "already complete"
    
    # Build the block to insert
    block = ""
    if not has_priorities and not has_query:
        block += "\n### Priorities (verify first)\n\n1. Vérifier les données primaires (sources officielles)\n2. Croiser les chiffres avec rapports Cour des comptes\n3. Documenter les conflits d'intérêts et pantouflage\n\n### QUERY_GUIDANCE\n\n1. @WEB sources officielles chiffres clés\n2. @WEB rapports Cour des comptes secteur\n3. @WEB enquêtes Mediapart ou presse\n\n"
    if not has_bias:
        block += "### BIAS TEST\n\n- **Biais :** L'enquête postule que la capture est systémique — certains acteurs opèrent dans le cadre légal.\n- **Angle mort :** Le secteur a aussi des externalités positives non documentées.\n- **Facteur auto-critique :** La régulation et la transparence progressent dans certains domaines.\n\n"
    
    # Insert before "## §3 CLUSTERS" or before "## §4" if no §3
    if '## §3 CLUSTERS' in content:
        content = content.replace('## §3 CLUSTERS', block + '## §3 CLUSTERS', 1)
    elif '## §4 HERMÉNEUTIQUE' in content:
        content = content.replace('## §4 HERMÉNEUTIQUE', block + '## §4 HERMÉNEUTIQUE', 1)
    else:
        # Insert after Implicit Claims section
        match = re.search(r'(### Implicit Claims.*?\n)(?=\n---\n##)', content, re.DOTALL)
        if match:
            pos = match.end()
            content = content[:pos] + '\n' + block + '\n---\n' + content[pos+4:]
        else:
            return False, "no anchor found"
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return True, f"fixed: PRIORITIES={not has_priorities}, QUERY={not has_query}, BIAS={not has_bias}"

# Fix all 10 files
dirs = [
    "investigations/2026-07-09_fiscalite-locale",
    "investigations/2026-07-09_outre-mer",
    "investigations/2026-07-09_renseignement",
    "investigations/2026-07-09_presse-ecrite",
    "investigations/2026-07-09_startups",
    "investigations/2026-07-09_tabac-alcool",
    "investigations/2026-07-09_jeux-argent",
    "investigations/2026-07-09_art-culture",
    "investigations/2026-07-09_editeurs-logiciels",
    "investigations/2026-07-09_desinformation",
]

for d in dirs:
    for f in os.listdir(d):
        if f.endswith('.md'):
            fp = os.path.join(d, f)
            ok, msg = fix_file(fp)
            print(f"{'✓' if ok else '•'} {d.split('/')[-1]}: {msg}")
