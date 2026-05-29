# Refonte UE-Censor — Suivi de progression

**Date de début** : 5 février 2026
**Article source** : `outputs/articles/2026-02/2026-02-05-ARTICLE_SUBSTACK_UE_CENSOR.md`
**Longueur initiale** : 789 lignes
**Longueur cible** : ~550-600 lignes

---

# MANDAT — Rédaction UE-Censor

## Rôle

Tu es un **rédacteur français rigoureux**, spécialisé dans les enquêtes d'investigation à haute densité informationnelle.

## Objectif

Rendre le texte UE-Censor **plus précis, plus clair, plus sobre** sans perdre d'information.

## 5 RÈGLES D'OR

1. **Préférer la prose aux listes** — Si plus de 3 items, rédiger en paragraphes
2. **Supprimer les jugements moraux** — "hypocrisie", "déni plausible", "machine à censurer" → facts only
3. **Une seule citation par section** — La citer, l'analyser, ne pas l'accumuler
4. **Citer les sources** — "rapport US House, lignes 4343-4378" pas "le rapport"
5. **Pas de superlatifs** — "sans précédent", "le plus efficace" → supprimés

## 3 INTERDICTIONS

- Langue de bois ou institutionnelle
- Formules creuses ou d'amorce vide
- Mots passe-partout ("troublant", "préoccupant", "alarmant")

## Format de travail

1. Lire le contenu original
2. Repérer les passages à améliorer
3. Proposer 2-3 variantes pour chaque passage
4. Justifier chaque choix

---

## État d'avancement

| Section | Statut | Fichier |
|---------|--------|---------|
| I. Introduction | ✅ VALIDÉE | `sections/section_01_intro.md` |
| II. Chronologie | ✅ VALIDÉE | `sections/section_02_chrono.md` |
| III. Architecture | ✅ VALIDÉE | `sections/section_03_archi.md` |
| IV. Preuves | ✅ VALIDÉE | `sections/section_04_preuves.md` |
| V. Comparaison URSS | ✅ VALIDÉE | `sections/section_05_urss.md` |
| VI. Invisibilisation | ✅ VALIDÉE | `sections/section_06_invis.md` |
| VII. Ce qu'on ne sait pas | ✅ VALIDÉE | `sections/section_07_limites.md` |
| VIII. EU Democracy Shield | ✅ VALIDÉE | `sections/section_08_shield.md` |
| IX. Dimension géopolitique | ✅ VALIDÉE | `sections/section_09_geo.md` |
| X. La Matrice | ✅ VALIDÉE | `sections/section_10_matrice.md` |
| XI. Conclusion | ✅ VALIDÉE | `sections/section_11_conclu.md` |
| XII. Méthodologie | ✅ VALIDÉE | `sections/section_12_meth.md` |

---

## Conventions par section

Chaque fichier `section_XX_YYY.md` contient :

```markdown
# SECTION XX — NOM

## Contenu original

[Copier-coller de l'article original]

## Contenu refondu

[Version refondue selon les principes]

## Modifications

| Élément | Avant | Après | Justification |
|---------|-------|-------|---------------|
| ... | ... | ... | ... |

## Statut

**Présentée pour validation le** : [DATE]
**Validation** : ⏳ EN ATTENTE / ✅ VALIDÉE / ❌ À REVOIR
```

---

## Problèmes identifiés — Audit initial

### Sur le plan structurel

| Problème | Exemple |
|----------|---------|
| Citations dupliquées | TikTok (lignes 299 et 464) |
| "Sans précédent" | Lignes 3, 19, 670 |
| Listes excessives | Score, Cui Bono, Vous savez que... |

### Sur le plan stylistique

| Problème | Exemples |
|----------|----------|
| Jugements moraux | "hypocrisie", "déni plausible", "illusion démocratique" |
| Superlatifs | "sans précédent", "sans précédent historique" |
| Apostrophes | "Vous savez que...", "Vous pouvez fermer..." |

### Sur le plan documentaire

| Problème | Conséquence |
|----------|-------------|
| Citations non contextualisées | "After comprehensive review..." citée deux fois |
| Exhibits non exploités | 302 exhibits mentionnés |
| Témoignages absents | 0 voix directe de censorés |

---

## Suppressions validées

| Élément | Emplacement | Justification |
|---------|-------------|--------------|
| Score Truth Engine (74/75) | Lignes 759-778 | Incompatible avec le journalisme |
| Iceberg Factor (128,800) | Ligne 782 | Chiffre arbitraire |
| "Cui Bono" | Lignes 484-497 | Notation non sourcée |
| Scoring URSS | Lignes 320-344 | Réduit la démonstration |
| "Le choix qui nous reste" | Lignes 641-666 | ton militant |
| Liste "Vous savez que..." | Lignes 645-654 | Paternaliste |
| "L'hypocrisie du DSA" | Ligne 388 | Jugement moral |

---

## Déplacements validés

| Élément | De | Vers |
|---------|-----|------|
| "Ce qu'on ne sait pas" | Section VI | Après l'introduction |
| Témoignage type | Section V | Section III (Preuves) |
| Exhibits détaillés | Méthodologie | Annexe |

---

## Notes de l'éditeur

### Sur la Section X "La Matrice"

"La Matrice" fait trois choses essentielles :
1. **Connexion** : Relie l'UE-Censor à l'Empire du mensonge
2. **Acteurs** : Identifie Tristan Mendès France comme architecte
3. **Sélection** : Explique l'hypocrisie (ce qu'on censure vs ce qu'on tolère)

**Décision** : Section conservée, listes condensables.

### Sur le ton

Maintenir le registre sobre dans les sections factuelles. Garder les moments narratifs (cas Slovaquie, Roumanie, "La Matrice").

---

## Procédure de validation

1. Rédiger la section refondue dans `sections/section_XX_YYY.md`
2. Présenter à l'utilisateur avec :
   - Contenu original
   - Contenu refondu
   - Tableau des modifications
3. Attendre validation
4. Si validé : passer à la section suivante
5. Si modifications : itérer jusqu'à validation

---

## Fin de la refonte — Procédure finale

Une fois toutes les sections validées :

1. Assembler toutes les sections validées dans l'ordre
2. Vérifier la cohérence globale (liens, renvois)
3. Nettoyer les doublons
4. Produire la version finale
5. Archiver le dossier `refonte_2026-02`

---

*Document mis à jour le 5 février 2026*
