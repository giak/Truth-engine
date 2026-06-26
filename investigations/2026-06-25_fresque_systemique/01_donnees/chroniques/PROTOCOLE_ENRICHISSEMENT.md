# Protocole d'Enrichissement des Chroniques depuis une Investigation

**Version** : 1.1 — **Statut** : validé manuellement avant exécution

**Principe** : Lire une investigation, en extraire les faits atomiques vérifiés, les croiser avec les chroniques existantes, et produire un rapport exécutable d'enrichissement. RIEN n'est modifié sans validation humaine.

---

## Étape 1 — Extraction atomique des faits

### 1.1 Parcours systématique

Lire l'intégralité de l'investigation section par section. Pour CHAQUE paragraphe, extraire tous les faits atomiques.

**Un fait atomique est valide s'il satisfait TOUS ces critères :**
1. **Daté** : année précise (2018), date complète (17 novembre 2018), ou plage (1980-2000). Un mois seul = incomplet, à signaler.
2. **Dimensionnable** : rattachable à UNE des 20 dimensions (POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL, SCI, DIP, MED, TER).
3. **Chiffré ou nommable** : au moins un nombre (282 000 manifestants, 10 Md€) ou un nom propre (loi, personne, lieu).
4. **Sourcé** : une URL, une source nommée (Le Monde, INSEE), ou une référence explicite dans le texte.

### 1.2 Formats à capturer

La table d'extraction brute :

```
Date précise | Année | Dimension (une) | Description (≤200 car.) | Code (✅⚠❌💀) | URL source | Titre section | Contexte libre
```

**Règles de description :**
- Commencer par une majuscule, pas de point final
- Pas de pipe `|` dans la description (reformuler si nécessaire)
- Précision max : chiffre + unité + verbe (`Hausse TICPE 7,6 cts/L gazole`)
- Pas de jugement dans la description (le code d'impact porte le jugement)

### 1.3 Détection des faits par type de structure

**Tableaux markdown** : chaque ligne = un fait. Extraire année, dimension, description, code.

**Listes à puces** : chaque item `- **Date** : Description` = probablement un fait. Vérifier que la date est explicite.

**Notes de bas de page** : contiennent souvent des sources ou des chiffres-clés.

**Paragraphes narratifs** : contiennent parfois des dates implicites. Chercher les patrons :
- `\d{1,2}\s+\w+\s+\d{4}` : "17 novembre 2018"
- `\d{4}` seul : présumer l'année du contexte
- `\d+%\s+\w+` :  "40% des condamnés"

### 1.4 Cas particuliers

| Cas | Règle |
|-----|-------|
| Date implicite (ex: « L'année suivante ») | Remonter la référence dans le texte, dater explicitement |
| Plage d'années (1980-2000) | Rediriger vers `plages_annees.md` |
| Année seule sans mois | Suffisant si la description est précise |
| Pas de source explicite | Marquer `Source: à vérifier` — ne pas l'exclure mais abaisser sa priorité |
| Fait déjà présent textuellement dans les chroniques | Ignorer (pas de duplicata) |

---

## Étape 2 — Vérification des chroniques existantes

### 2.1 Lecture ciblée

Pour chaque année identifiée dans l'extraction :

```bash
cat chroniques/AAAA/*.md
# ou cibler une dimension spécifique :
cat chroniques/AAAA/AAAA_DIM.md
```

### 2.2 Matrice de comparaison

Construire une matrice :

```
Fait extrait → Fichier cible → Ligne existante ? → Statut
```

Avec 3 statuts possibles :

| Statut | Définition | Action |
|--------|-----------|--------|
| ✅ Nouveau | Aucune ligne ne correspond | Ajouter |
| 🔁 Doublon exact | Même texte, même code | Ignorer (ne pas ajouter) |
| 🔀 Near-duplicate | Similitude > 70% mais pas identique | Signaler pour fusion |

**Détection des near-duplicates** (prévenir les doublons comme les 5 lignes GJ) :

Pour chaque candidat, comparer sa description normalisée avec toutes les lignes du fichier cible :
```python
def normalize(s):
    s = s.lower().strip()
    s = re.sub(r'[,\\(\\)\\[\\]"\'\\-–—:;!?€]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s
```

Calculer la similarité Jaccard sur les mots (token unigrams) :
```
J(A, B) = |A ∩ B| / |A ∪ B|
```
- J ≥ 0,7 : **near-duplicate** à fusionner
- J < 0,7 : **fait distinct** à ajouter

**Signaler les doublons existants** : Si les chroniques contiennent déjà plusieurs lignes quasi-identiques (comme les 5 lignes GJ dans 2018_SOC), les inventorier pour un futur nettoyage.

---

## Étape 3 — Fact-checking forensique

### 3.1 Quand déclencher

Le fact-checking est **obligatoire** dans TOUS ces cas :

1. **Conflit investigation vs chroniques** : un même événement a des chiffres différents (ex: GJ 89 morts vs 11 morts)
2. **Chiffre suspect** : nombre anormalement élevé ou bas par rapport au contexte connu
3. **Source unique** : l'investigation s'appuie sur une seule source pour un chiffre important
4. **Date improbable** : événement daté un jour férié, un week-end historique, ou en conflit avec d'autres sources
5. **Pas de source** : fait important sans aucune URL ni référence

### 3.2 Pipeline de vérification

**Niveau 1 — Test URL** (pour chaque URL citée) :

```bash
# Vérifier que l'URL est accessible (HEAD request)
curl -sI "URL" | head -5
# ou utiliser rtk curl
rtk curl -sI "URL"
```

Résultats :
- `200 OK` : source accessible → confiance renforcée
- `4xx` : page supprimée → confiance réduite, chercher archive.org
- `5xx` : site temporairement indisponible → réessayer plus tard
- `timeout` ou `connection refused` : domaine peut-être mort

**Niveau 2 — Recoupement** (obligatoire pour les cas 1, 2, 3) :

Pour chaque chiffre contesté, chercher **au moins 2 sources indépendantes** :

```python
# Prompts de recherche web :
- "[événement] [date] chiffres bilan"
- "[événement] [chiffre] morts blessés"
- "[nom source] [événement] [chiffre]"
```

Exemple concret (GJ) :
```
Search 1: "gilets jaunes bilan morts 2018 2019 chiffres"
Search 2: "gilets jaunes 11 morts"
Search 3: "nombre de morts gilets jaunes Décembre 2018"
```

**Niveau 3 — Source primaire** (quand les recoupements divergent) :

Identifier et lire la source la plus autoritaire :
- Données ministérielles (Intérieur, Justice)
- Rapports parlementaires
- Enquêtes journalistiques long format
- Statistiques officielles (INSEE, DARES, etc.)

### 3.3 Grille de décision pour conflits

| Contexte | Décision |
|----------|----------|
| Investigation sourcée (URL OK) + Chroniques non sourcées | **Corriger les chroniques** |
| Investigation sourcée (URL OK) + Chroniques sourcées (URL OK aussi) | **Signaler le conflit**, ne pas trancher sans l'humain |
| Investigation non sourcée + Chroniques sourcées | **Garder les chroniques** |
| Ni l'un ni l'autre n'est sourcé | **Exclure le fait**, marquer `Source manquante` |
| Les deux citent la même source | **Vérifier la source directement** pour trancher |

### 3.4 Glyphe de fiabilité

Marquer chaque fait extrait avec un niveau de confiance :

| Glyphe | Signification | Condition |
|--------|---------------|-----------|
| ✦ | Fiable | Source primaire (URL → 200 OK) + chiffre confirmé par ≥1 recoupement |
| ✧ | Probable | Source secondaire (média, article) + chiffre plausible |
| ⁅ | Fragile | Source cassée (URL 4xx/5xx) ou unique |
| ❧ | Non sourcé | Aucune URL, pas de recoupement possible |

---

## Étape 4 — Catégorisation et décision de dimension

### 4.1 Arbre de décision pour la dimension

Un fait peut relever de plusieurs dimensions. Choisir la **plus spécifique** :

```
Événement politique / institutionnel ?
  ├─ Loi, élection, nomination → POL
  ├─ Justice, procès, droit → JUR
  ├─ Terrorisme, attentat → TER
  └─ Diplomatie, relations internationales → DIP

Événement économique / social ?
  ├─ Économie, fiscalité, budget → ECO
  ├─ Social, logement, pauvreté → SOC
  ├─ Santé, hôpital → SANT
  ├─ Éducation → EDU
  └─ Agriculture → AGR

Événement culturel / sociétal ?
  ├─ Culture, médias → CUL
  ├─ Sport → SPO
  ├─ Religion → REL
  └─ Immigration → IMM

Événement technique / scientifique ?
  ├─ Technologie, industrie → TEC
  ├─ Environnement, climat → ENV
  ├─ Transport → TRA
  ├─ Science, recherche → SCI
  └─ Militaire → MIL

Autre ?
  ├─ Démographie → DEMO
  └─ Média → MED
```

**Règle** : En cas de doute, privilégier la dimension qui rend le fait le plus **visible** dans le contexte de l'investigation. Un même événement peut nécessiter plusieurs lignes dans des dimensions différentes (ex: loi = POL + ses conséquences budgétaires = ECO).

### 4.2 Arbre de décision pour le code d'impact

```
Le fait décrit-il ?
  ├─ Un progrès, une réussite, une amélioration → ✅
  │   Ex: Loi votée, innovation, victoire électorale
  ├─ Une situation préoccupante, une alerte, un risque → ⚠
  │   Ex: Tensions, réforme avortée, transition incertaine
  ├─ Un échec, une régression, une crise → ❌
  │   Ex: Répression, blocage, austérité, échec politique
  └─ Une catastrophe, un crime, la mort → 💀
      Ex: Attentat, assassinat, scandale majeur, effondrement
```

**Règle de la dimension :** Le code dépend de la dimension choisie. Un même événement peut être ❌ en POL et 💀 en SOC (ex: loi anti-casseurs = répression en POL, blessés graves en SOC/💀).

---

## Étape 5 — Rapport final

### 5.1 Structure du rapport

```
## RAPPORT : [sujet] — [période] — [date]

### Résumé exécutif (3 lignes max)
- Investigation : [titre]
- Faits extraits : [N] | Nouveaux : [N] | À enrichir : [N] | Doublons : [N]
- Dimensions concernées : [liste]

### 1. État existant
- [N] lignes dans les chroniques pour ce sujet
- Répartition : [fichier] = [N], [fichier] = [N]...
- Codes : [répartition]

### 2. Problèmes identifiés
- [N] doublons (détail)
- [N] erreurs factuelles (détail + correction)
- [N] codes non-standards
- [N] ambigüités de dimension

### 3. Nouveaux faits à ajouter (N)
| Date | Dim | Description | Code | Fiabilité | URL | Fichier cible |
|------|-----|-------------|------|-----------|-----|---------------|

### 4. Faits existants à enrichir (N)
| Fichier | Ligne actuelle | Enrichissement | Raison |
|---------|---------------|----------------|--------|

### 5. Nettoyage des doublons (N)
| Fichier | Lignes à supprimer | Ligne à garder | Raison |
|---------|-------------------|----------------|--------|

### 6. Faits écartés (N)
| Raison | Faits concernés |
|--------|-----------------|
| Non sourcé | ... |
| Déjà présent | ... |
| Hors période | ... |
| Dimension non déterminable | ... |

### 7. Note de fact-checking
- [N] conflits résolus (détail)
- [N] vérifications web effectuées
- Sources consultées : [liste URLs]
```

### 5.2 Règles de priorité pour l'implémentation

| Priorité | Catégorie | Exemple |
|:--------:|-----------|---------|
| 1 | **Nettoyage** : supprimer les doublons, corriger les erreurs | Fusionner 5 lignes GJ en 1, corriger 89→11 |
| 2 | **Ajout** : faits nouveaux, bien sourcés (✦ ou ✧) | Acte II, Acte III GJ |
| 3 | **Enrichissement** : améliorer des lignes existantes | Ajouter chiffres Acte I à la ligne existante |
| 4 | **Faits ambigus** : sans dimension claire ou code discutable | À valider avec l'humain |

---

## Checklist de validation (avant envoi du rapport)

- [ ] Chaque fait extrait a une date explicite ou implicite résolue
- [ ] Chaque fait a une dimension assignée (une seule)
- [ ] Chaque fait a un code d'impact (✅⚠❌💀)
- [ ] Les doublons avec les chroniques existantes ont été détectés (Jaccard ≥ 0,7)
- [ ] Les conflits investigation vs chroniques ont été fact-checkés (web)
- [ ] Les sources URLs ont été testées (HEAD request ou read_url)
- [ ] Les faits hors période (avant 1975 ou après 2026) sont signalés comme tels
- [ ] Les faits sans année précise (plages) sont redirigés vers plages_annees.md
- [ ] Le rapport est prêt à être exécuté par un agent sans relecture de l'investigation source

---

## Annexe A — Cas d'école : Gilets Jaunes

Ce qu'a donné l'application du protocole sur l'investigation GJ (2018-2020) :

| Métrique | Valeur |
|----------|--------|
| Faits extraits de l'investigation | 34 |
| Nouveaux faits (absents des chroniques) | ~18 |
| Doublons trouvés dans les chroniques | 5 (dans 2018_SOC) |
| Erreurs factuelles corrigées | 1 (89 morts → 11 morts, vérifié web) |
| Codes non-standards dans les chroniques | 4 |
| Dimensions les plus impactées | SOC (+10), ECO (+3), POL (+2), MIL (+1) |

**Erreur détectée :** Les chroniques disaient « 89 morts, 2500 blessés, 15000 gardes à vue ». Vérification web (Figaro, Le Point, JDD) : **11 morts** (dont 9 accidents de la route), **2 448 blessés manifestants**, 1 797 blessés forces de l'ordre, **12 107 interpellations**. L'erreur « 89 morts » est probablement un artefact de fusion entre GJ et un autre événement.

---

## Annexe B — Outils utilisables

| Outil | Usage |
|-------|-------|
| `grep` / `rtk grep` | Chercher des mots-clés dans les chroniques existantes |
| `read_url` | Lire le contenu textuel d'une URL source |
| `researcher-web` | Chercher des recoupements pour le fact-checking |
| `str_replace` | Modifier une ligne précise dans un fichier chronique |
| `write_file` | Créer un nouveau fichier chronique (si la dimension manque) |
| `read_files` | Lire les chroniques existantes |
| Python (inline) | Calcul de similarité Jaccard, normalisation de texte |
