# Enrichir les chroniques

Chroniques = fichiers `chroniques/AAAA/AAAA_DIM.md` qui listent les événements factuels année par année, dimension par dimension.

L'idée : quand on lit une investigation, on peut en extraire des faits qui ne sont pas encore dans les chroniques, ou corriger des faits qui y sont mais avec des chiffres erronés.

---

## La démarche en 4 questions

Quel que soit le type d'enquête, on se pose ces 4 questions dans l'ordre :

### 1. Qu'est-ce que j'ai devant moi ?

Identifier le type de document :

| Type | À quoi ça ressemble | Ce qu'il contient |
|------|---------------------|-------------------|
| **APEX** | Nom se termine par `_APEX.md` | Registry structuré `F-CIV-XXX` avec faits, années, URLs |
| **INVESTIGATION** | Nom se termine par `_INVESTIGATION.md` ou `_SUPPLEMENT.md` | Texte narratif avec faits dispersés dans les paragraphes |
| **HYPER_MATRICE** | Nom se termine par `_HYPER_MATRICE.md` | Matrice de données déjà formatées |
| **Analyse / ARCHITECTURE** | Nom se termine par `_ARCHITECTURE.md` | Structure narrative, thèse, pas de faits bruts |

Si c'est une analyse sans faits datés → ne rien extraire.

### 2. Qu'est-ce que j'en extrais ?

Selon le type :

- **APEX** : lire le registry `F-CIV-XXX`. Chaque entrée a déjà une année, une description, parfois une URL. Extraire les lignes.
- **INVESTIGATION / SUPPLEMENT** : lire le texte. Repérer les faits dans les paragraphes — budgets, dates, citations, événements. Lister TOUS les faits sans filtrer. L'année est dans le contexte du paragraphe, pas dans le nom du fichier.
- **Les deux** : noter aussi les erreurs possibles — chiffres qui semblent aberrants, sources qui se contredisent.

Ne pas décider à cette étape où iront les faits. Juste les lister.

### 3. Qu'est-ce que j'en fais ?

Une fois la liste complète :

- **Ajouter** : le fait n'est pas dans les chroniques → créer ou enrichir le fichier `chroniques/AAAA/AAAA_DIM.md`
- **Corriger** : le fait existe avec un chiffre erroné → remplacer la ligne dans le fichier existant
- **Ignorer** : le fait est trop vieux, trop granulaire, ou déjà présent → ne rien faire

Pour chaque fait, décider :
- **Année** : l'année du fait (extraite du contexte), pas celle du document. Fourchette → `plages_annees.md`.
- **Dimension** : POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL, SCI, DIP, MED, TER. Si ambigu → contexte.
- **Code** : ❌ = fait documenté (source primaire), ⚠ = tendance ou source secondaire, ✅ = progrès (rare), 💀 = catastrophe

### 4. Qu'est-ce que ça apporte ?

- Un fait nouveau ? → ajout
- Une correction ? → remplacement
- Une confirmation ? → déjà présent, rien à faire

---

## Exemple 1 — INVESTIGATION narrative : ajout de faits

**Document :** `1500_communicants_etat_caste_INVESTIGATION.md`

**Q1 — Type :** INVESTIGATION narrative. Faits dispersés dans le texte : budgets (14,1M€, 1 Md€), nominations (Kohler, Ndiaye), citations, chronologie réforme 2025-2026.

**Q2 — Extraction :** 37 faits listés, dont :
```
2023 | Budget SIG : 14,1M€ | source dans le texte
2025 | Budget réel SIG : 23,4M€ | L'Humanité
2024 | Budget total comm. État : 1 Md€ | JDD
2017 | Ndiaye : « assume de mentir pour protéger le président » | citation directe
2025 | Kohler : SG Élysée → Société générale | pantouflage
2025 | 500+ portes tournantes documentées (2022-2025) | ?
```

**Q3 — Opération :** 31 faits nouveaux → ajout dans `chroniques/AAAA/AAAA_DIM.md` (14 fichiers, de 2017 à 2026). 4 exclus (DICOM 2010 obsolètes, création SIG 1963 non datable).

**Q4 — Apport :** 31 nouveaux faits sur la communication d'État (budgets, effectifs, pantouflage) qui n'étaient pas couverts.

---

## Exemple 2 — Correction d'erreur factuelle

**Document :** investigations GJ (lors de l'enrichissement des chroniques GJ)

**Q1 — Type :** Les chroniques existaient déjà, l'enquête GJ a révélé une erreur.

**Q2 — Extraction :** Pas de nouveau fait, mais une incohérence : les chroniques disaient « 89 morts, 2 500 blessés, 15 000 gardes à vue ».

**Q3 — Opération :** Vérification → le vrai bilan GJ 2018-2019 est « 11 morts, 2 448 blessés, 12 107 interpellations ». **Remplacer** la ligne erronée par la ligne corrigée.

**Q4 — Apport :** Correction d'une erreur factuelle propagée (89 → 11 morts). Le chiffre « 89 » était une rumeur non vérifiée passée dans les chroniques.

---

## Exemple 3 — APEX structuré : déjà couvert

**Document :** `medias_concentration_milliardaires_APEX.md`

**Q1 — Type :** APEX. Registry structuré avec 45 faits F-CIV-XXX, années, descriptions, URLs.

**Q2 — Extraction :** 45 faits extraits du registry (structuré, facile).

**Q3 — Opération :** Vérification contre les chroniques MED/POL/ECO 2024-2026 → tous les faits sont déjà présents. 0 ajout.

**Q4 — Apport :** Validation : les chroniques MED sont exhaustives pour 2024-2026. Pas d'ajout nécessaire.

---

## Pièges fréquents (tirés des tests réels)

| Situation | Ce qui s'est passé | À faire |
|-----------|-------------------|---------|
| Scanner de vérification trop agressif | Tous les faits déclarés « déjà présents » à cause d'une normalisation trop forte | Vérifier ligne par ligne, pas par mots-clés |
| Dimensions oubliées | Faits classés absents… dans la mauvaise dimension | Scanner les 20 dimensions |
| Année du document au lieu de l'année du fait | Fait de 2017 assigné à 2026 | Lire le paragraphe, extraire l'année du contexte |
| plages_annees.md ignoré | Faits sur 4 ans sans dossier | Vérifier plages_annees.md en parallèle |
| Chiffre non vérifié | « 89 morts GJ » reproduit sans fact-check | Croiser les sources avant d'ajouter ou corriger |
| **Accent mismatch dans les fichiers créés** | Template `Annee` (sans accent) ≠ compteur cherche `Année` (avec) → ligne d'en-tête comptée comme donnée → compteur gonflé de 1 | Quand tu crées un fichier, utilise EXACTEMENT le même format que les fichiers existants : accents, em dash (—), majuscules. Le moindre écart casse le compteur. |
| **update_header regex incompatible** | Regex cherche `événement` (accentué) mais le template écrit `evenement` (sans) → la mise à jour du compteur échoue silencieusement | Le pattern dans le template et la regex de mise à jour doivent être identiques caractère pour caractère. |

---

## Ce qu'il faut retenir

3 étapes séparées : **extraire → décider → appliquer**.

4 questions dans l'ordre : **type ? → faits ? → opération ? → apport ?**

Quand tu hésites, regarde le contexte dans l'investigation, pas dans le protocole.
