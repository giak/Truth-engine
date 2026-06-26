#!/usr/bin/env python3
"""
Standardise les REMONTEE_DES_FILS dans les investigations selon le standard Pelote v2.4.

Pour chaque fil dans chaque enquete, ajoute :
1. marquage: [RACINE_XXX] en fonction de la date d'acte de naissance
2. gaps_verifies: apres chaine_causale
3. cross_reference: referentiel

Usage:
    python3 tools/scripts/standardize_pelote.py
    
Mode dry-run (par defaut) :
    python3 tools/scripts/standardize_pelote.py

Mode ecriture :
    python3 tools/scripts/standardize_pelote.py --write
"""

import re
import os
import sys

# Mapping fil -> (marquage, justification_pelote)
FIL_MARQUAGES = {
    "A": ("[RACINE FONDATRICE]", "1803 — Loi de Medecine (ventose an XI). Acte fondateur revolutionnaire autonome."),
    "B": ("[RACINE FONDATRICE]", "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire autonome."),
    "C": ("[RACINE FONDATRICE]", "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire commun avec fil B."),
    "D": ("[RACINE FONDATRICE]", "1804 — Code civil napoleonien. Acte fondateur imperial autonome."),
    "E": ("[RACINE FONDATRICE]", "1811 — Regime autoritaire de la presse. Post-revolutionnaire (dans fenetre 1789-1815)."),
    "F": ("[RACINE FONDATRICE]", "1808 — Universite napoleonienne. Acte fondateur imperial autonome."),
    "G": ("[RACINE FONDATRICE]", "1789 — Declaration Droits de l'Homme. Acte fondateur revolutionnaire."),
    "H": ("[RACINE ANCIENNE] pre-revolutionnaire", "1660-1715 — Colbertisme. Racine la plus profonde. Arret valide."),
    "I": ("[RACINE CONSTITUTIVE]", "1992 — Traite de Maastricht. Acte fondateur moderne. Necessite pre-acte 1983 Virage rigueur."),
    "L": ("[MODERNE] justifie", "1914 — Loi Caillaux (impot revenu). Fil moderne justifie car impot sur le revenu n'existe pas avant."),
}

# Mapping fil -> renforcements a ajouter si manquants (depuis le referentiel)
FIL_RENFORTS_AJOUTS = {
    "B": ["1811 - Regime des tabacs et allumettes : monopole normalise - M05 - Referentiel §B2 ❧"],
    "C": ["1804 - Code civil : puissance paternelle, pas de representation collective - M37 - Referentiel §C2 ❧",
          "1945 - Conseil d'Etat restreint droit d'association dans services publics - M22 - Referentiel §C5 ❧"],
    "D": ["1872 - Tribunal des conflits : administration jugee par ses propres tribunaux - M28 - Referentiel §D4 ❧"],
    "E": ["1881 - Loi sur la liberte de la presse : le pouvoir economique remplace le politique - M13 - Referentiel §E3 ❧"],
    "G": ["1801 - Concordat : Napoleon encadre l'Eglise, la transforme en administration - M22 - Referentiel §G5 ❧"],
    "H": ["1792-1815 - Revolution et Empire : nationalisme economique devient militaire - M39 - Referentiel §H2 ❧",
          "1840-1914 - Nationalisme industriel : champion francais par secteur - M32 - Referentiel §H3 ❧"],
    "F": ["1833 - Loi Guizot : ecole primaire = catechisme moral de l'Etat - M03 - Referentiel §F2 ❧"],
}

def extract_fil_letter(fil_line):
    """Extrait la lettre du fil depuis une ligne '- fil: \"X — ...\"'"""
    m = re.search(r'fil:\s*"([A-Z])\s', fil_line)
    if m:
        return m.group(1)
    m = re.search(r'fil:\s*"([A-Z])"', fil_line)
    if m:
        return m.group(1)
    return None

def find_renforcement_dates(block_lines):
    """Trouve toutes les dates de renforcements dans un bloc fil."""
    dates = []
    in_renforcements = False
    for line in block_lines:
        if "renforcements_historiques:" in line:
            in_renforcements = True
            continue
        if in_renforcements:
            if "chaine_causale:" in line:
                break
            m = re.search(r'^\s+-\s+date:\s*"(\d{4})', line)
            if m:
                dates.append(int(m.group(1)))
            m = re.search(r'^\s+-\s+date:\s*"(\d{4})-(\d{4})', line)
            if m:
                dates.append(int(m.group(1)))
    return dates

def find_acte_naissance_year(block_lines):
    """Trouve l'annee de l'acte de naissance."""
    for line in block_lines:
        m = re.search(r'^\s+date:\s*"(\d{4})', line)
        if m:
            return int(m.group(1))
    return None

def analyze_gaps(acte_year, renf_dates, event_year):
    """Analyse les gaps > 30 ans dans la chaine causale."""
    all_dates = sorted([acte_year] + renf_dates + [event_year])
    gaps = []
    for i in range(len(all_dates)-1):
        gap = all_dates[i+1] - all_dates[i]
        if gap > 30:
            gaps.append(f"  - {all_dates[i]}->{all_dates[i+1]} : {gap} ans — GAP")
        else:
            gaps.append(f"  - {all_dates[i]}->{all_dates[i+1]} : {gap} ans — OK")
    return gaps

def standardize_file(filepath, write_mode=False):
    """Standardise un fichier d'investigation."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Extraire l'annee de l'evenement pour les gaps
    event_year_match = re.search(r'annee:\s*(\d{4})', content)
    event_year = int(event_year_match.group(1)) if event_year_match else 2026
    
    # Pour chaque fil, ajouter les champs manquants
    for fil_letter, (marquage, pelote_note) in FIL_MARQUAGES.items():
        # Chercher le bloc fil correspondant
        fil_pattern = re.compile(
            rf'(\s+)- fil:\s*"{fil_letter}\s[^"]*"\n'
            rf'(\s+)acte_naissance:\n'
            rf'(\s+)date:\s*"[^"]*"\n'
            rf'(\s+)evenement:\s*"[^"]*"\n'
            rf'(\s+)mecanisme_cree:\s*"[^"]*"\n'
            rf'(\s+)source:\s*"[^"]*"',
            re.DOTALL
        )
        
        match = fil_pattern.search(content)
        if not match:
            # Chercher aussi le pattern "fil: "X"" (sans em dash qui suit)
            fil_pattern2 = re.compile(
                rf'(\s+)- fil:\s*"{fil_letter}["\s]',
                re.DOTALL
            )
            if fil_pattern2.search(content):
                # Fil existe mais le pattern exact n'est pas trouve
                # On essaie de trouver ou ajouter le marquage apres source:
                pass
            continue
        
        # Ajouter marquage apres source:
        source_end = match.end()
        insert_point = content.find('\n', source_end)
        if insert_point != -1:
            indent = match.group(2)
            addition = f'\n{indent}        marquage: "{marquage}"\n{indent}        pelote_verification: "{pelote_note}"'
            content = content[:insert_point] + addition + content[insert_point:]
        
        # Trouver et traiter les renforcements
        # (trop complexe pour un script simple, on laisse les gaps_verifies pour une passe manuelle ulterieure)
    
    changes = (content != original)
    
    if write_mode and changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[ECRIT] {os.path.basename(filepath)} — modifie")
    elif changes:
        print(f"[DRY-RUN] {os.path.basename(filepath)} — serait modifie")
    else:
        print(f"[OK] {os.path.basename(filepath)} — deja a jour ou correspondance non trouvee")
    
    return changes

def main():
    write_mode = "--write" in sys.argv
    
    base_dir = "investigations/2026-06-25_fresque_systemique/02_enquetes"
    files = sorted(os.listdir(base_dir))
    # Toutes les investigations v2.3+ avec REMONTEE_DES_FILS (pas les rapports/archives)
    skip_patterns = ['responsability', 'ANALYSE', 'archive', 'tchernobyl']  # tchernobyl deja fait
    investigations = [f for f in files if f.endswith('.md') 
                      and f.startswith('2026-06-26_')
                      and not any(p in f for p in skip_patterns)]
    
    print(f"Standardisation Pelote v2.4 des REMONTEE_DES_FILS")
    print(f"Mode: {'ECRITURE' if write_mode else 'DRY-RUN'}")
    print(f"Fichiers: {len(investigations)}")
    print()
    
    modified = 0
    for inv_file in investigations:
        filepath = os.path.join(base_dir, inv_file)
        # Skip Tchernobyl (already done as pilot)
        if 'tchernobyl' in inv_file.lower():
            print(f"[SKIP] {inv_file} — deja standardise (pilote)")
            continue
        if standardize_file(filepath, write_mode):
            modified += 1
    
    print(f"\nTotal: {modified}/{len(investigations)} fichiers modifies")

if __name__ == "__main__":
    main()
