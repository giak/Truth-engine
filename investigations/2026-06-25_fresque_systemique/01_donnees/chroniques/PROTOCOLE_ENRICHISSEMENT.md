# Enrichir les chroniques

Chroniques = fichiers `chroniques/AAAA/AAAA_DIM.md` qui listent les événements factuels année par année, dimension par dimension.

L'idée : quand on lit une investigation, on peut en extraire des faits qui ne sont pas encore dans les chroniques, ou corriger des faits qui y sont mais avec des chiffres erronés.

**AFP (Anti-Fausse-Précision) :** ce protocole suit la règle AFP — pas de script déterministe qui parse du texte LLM. Le LLM fait l'extraction ET l'écriture directement.

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
- **Année** : l'année du fait (extraite du contexte), pas celle du document.
  - Si le fait couvre plusieurs années (ex: sous-financement 2020-2024) → utiliser la plage dans la colonne Année (`2020-2024`) et ranger le fichier dans le dossier de l'année de fin (`2024/2024_SANT.md`).
  - Si le fait est révélé par un rapport (ex: rapport IGAS 2026 qui révèle un sous-financement 2020-2024) → **deux lignes** : une pour le fait historique avec la plage d'années, une pour la révélation (année du rapport). Les deux événements sont distincts, les deux méritent une entrée.
- **Dimension** : POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL, SCI, DIP, MED, TER. Si ambigu → contexte.
- **Code** : ❌ = fait documenté (source primaire), ⚠ = tendance ou source secondaire, ✅ = progrès (rare), 💀 = catastrophe

### 4. Qu'est-ce que ça apporte ?

- Un fait nouveau ? → ajout
- Une correction ? → remplacement
- Une confirmation ? → déjà présent, rien à faire

---

## Ajouter dans les chroniques (AFP-compliant)

Ne pas utiliser de script. Le LLM ajoute les faits **directement** dans les fichiers, en respectant scrupuleusement le format.

### Ou trouver le fichier

Les chroniques sont dans `chroniques/AAAA/AAAA_DIM.md`. Exemple : `chroniques/2024/2024_SOC.md`.

### Format attendu d'une ligne

```
| Année | Dimension | Description | Code |
```

Règles :
- La description commence par une majuscule, pas de point final
- Pas de pipe `|` dans la description (échapper ou reformuler)
- Année dans la 1ʳᵉ colonne = année du fichier (sauf plage)
- Code : ❌ ⚠ ✅ 💀

### Procédure

Pour ajouter un fait :

1. **Lire** le fichier cible (`chroniques/AAAA/AAAA_DIM.md`) — ou le créer s'il n'existe pas
2. **Vérifier** que le fait n'est pas déjà présent (déduplication sémantique, pas regex)
3. **Ajouter** la ligne à la fin du tableau, AVANT la ligne vide finale
4. **Mettre à jour** le compteur dans l'en-tête : remplacer `> N événement(s)` par le nouveau total

### Template si le fichier n'existe pas

```markdown
# Chronique AAAA — Dimension DIM

> Fait atomique extrait de l'HYPER-MATRICE FRANCE 1975-2026.
> 0 événement(s) classé(s) dans la dimension DIM pour l'année AAAA.

| Année | Dimension | Description | Code |
|---|---|---|---|
```

Puis ajouter la 1ʳᵉ ligne et changer `0 événement(s)` en `1 événement(s)`.

### Piège : le sens des lignes

- L'en-tête est une ligne de commentaire (`> ...`)
- La ligne de séparation est `|---|---|---|---|`
- Les données commencent après
- Ne pas compter l'en-tête ni le séparateur comme des données

### Cas plage d'années

Si le fait couvre plusieurs années (ex: 2020-2024) :
- Ranger le fichier dans le dossier de l'année de fin : `2024/2024_SANT.md`
- Mettre la plage dans la colonne Année : `| 2020-2024 | SANT | ...`
- Si c'est une révélation (ex: rapport 2026 qui révèle un fait 2020-2024) → deux entrées séparées

### Vérification

Après chaque enrichissement, relire le fichier modifié et compter mentalement les lignes de données pour confirmer que le compteur est correct.

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

**Q3 — Opération :** Le LLM écrit directement chaque fait dans le fichier chronique correspondant, en vérifiant le format, le compteur et les doublons.

**Q4 — Apport :** 31 nouveaux faits sur la communication d'État (budgets, effectifs, pantouflage) qui n'étaient pas couverts.

---

## Exemple 2 — Correction d'erreur factuelle

**Document :** investigations GJ

**Q1 — Type :** Les chroniques existaient déjà, l'enquête GJ a révélé une erreur.

**Q2 — Extraction :** Pas de nouveau fait, mais une incohérence : les chroniques disaient « 89 morts, 2 500 blessés, 15 000 gardes à vue ».

**Q3 — Opération :** Le LLM lit le fichier chronique, repère la ligne erronée, la remplace par la ligne corrigée. Vérifie que le compteur reste inchangé (même nombre de lignes).

**Q4 — Apport :** Correction d'une erreur factuelle propagée (89 → 11 morts).

---

## Exemple 3 — APEX structuré : déjà couvert

**Document :** `medias_concentration_milliardaires_APEX.md`

**Q1 — Type :** APEX. Registry structuré avec 45 faits F-CIV-XXX, années, descriptions, URLs.

**Q2 — Extraction :** 45 faits extraits du registry.

**Q3 — Opération :** Le LLM vérifie chaque fait contre les chroniques MED/POL/ECO 2024-2026 existantes. 0 ajout — tous déjà présents.

**Q4 — Apport :** Validation : les chroniques sont exhaustives sur ce périmètre.

---

## Pièges fréquents

| Situation | À faire |
|-----------|---------|
| Scanner de vérification trop agressif | Vérifier ligne par ligne, pas par mots-clés |
| Dimensions oubliées | Scanner les 20 dimensions |
| Année du document au lieu de l'année du fait | Lire le paragraphe, extraire l'année du contexte |
| Chiffre non vérifié | Croiser les sources avant d'ajouter |
| Compteur non mis à jour | Relire le fichier après ajout, compter les lignes |
| Doublon non détecté | Lire le fichier avant d'ajouter, vérifier sémantiquement |

---

## Ce qu'il faut retenir

3 étapes séparées : **extraire → décider → appliquer**.

4 questions dans l'ordre : **type ? → faits ? → opération ? → apport ?**

Le LLM fait l'écriture directement, sans script intermédiaire. C'est plus simple, plus fiable, et conforme AFP.

**Règle d'or sur l'année :** l'année du fait, pas du document.

**Règle d'or sur la granularité :** un sous-fait = une ligne. Ne pas agréger.
