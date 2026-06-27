# DSL COMPRESSION: PROMPT FAIT-MINEUR v1.1
## Pipeline de découverte, vérification et injection de faits atomiques dans les Chroniques 1789-2026

**Date :** 2026-06-27 (v1.0) / 2026-06-27 (v1.1)
**Type :** PROMPT
**Héritage :** Truth Engine KERNEL v2.0 + protocole investigation v2.4 NREF + PROTOCOLE_ENRICHISSEMENT.md
**Périmètre :** 20 dimensions × 237 années (1789-2026) × 5 989 événements existants
**Révision v1.1 :** simulation sur REL (Rapport `simulation_fait_mineur_REL_RAPPORT.md`) — 5 gaps critiques corrigés

---

## GLOSSAIRE

| Symbole | Concept | Description |
|---------|---------|-------------|
| ◉ | IMPERATIVE | Règle absolue, commande, obligation |
| → | CAUSAL | Chaîne causale, workflow, séquence |
| ◆ | CONSTRAINT | Condition, limite, borne |
| ⊙ | METRIC | Métrique, checklist, mesure |
| △ | PATTERN | En-tête de section, pattern |
| ⟐ | SCOPE | Périmètre, référence documentaire |
| ◈ | PRIMARY | Source primaire (rapport officiel, loi, procès) |
| ◉ | SECONDARY | Source secondaire (presse, enquête, analyse) |
| ○ | ADVERSARY | Source adversaire (contre-version, critique) |

---

## △ MISSION — FAIT-MINEUR

### ◉ Objectif

Trouver, vérifier et injecter des faits atomiques dans les Chroniques de la fresque systémique (1789-2026). Chaque fait est un événement daté, sourcé, classé par dimension.

### ◆ Différence avec une investigation NREF

| Investigation NREF | FAIT-MINEUR |
|-------------------|-------------|
| 1 événement → 14 chapitres YAML | 1 dimension × N années → N lignes dans chroniques |
| Profondeur : 200+ lignes, contre-version, Pelote | Largeur : scan systématique, sourcing rapide |
| NREF-A/B obligatoire | ✦/✧ minimum, ❧ acceptable pour faits secondaires |
| Ultrathinking, second agent | GATES 6 vérifications |
| 3-6h de travail | 15-45 min par session |

### ◉ Périmètre couvert

- **Années :** 1789-2026 (237 ans)
- **Dimensions :** AGR, CUL, DEMO, DIP, ECO, EDU, ENV, IMM, JUR, MED, MIL, POL, REL, SANT, SCI, SOC, SPO, TEC, TER, TRA
- **Sources :** MNEMO_Q → @WEB → @FETCH (KERNEL priority)
- **Format sortie :** lignes dans `chroniques/AAAA/AAAA_DIM.md`

### ⊙ Règles cardinales

◉ Chaque fait DOIT avoir une année (ou plage) et une dimension
◉ Chaque fait DOIT avoir au moins 1 source URL (✦/✧/⁅/❧)
◉ Pas de doublon sémantique avec les chroniques existantes (lire le fichier cible avant)
◉ AFP-compliant : le LLM écrit directement, pas de script intermédiaire
◉ Pas de déduction non sourcée — un fait sans source est une hypothèse, pas un fait
◆ Si un fait est incertain → l'inclure quand même avec ❧ mais le marquer [HYPOTHÈSE]
◆ Si une dimension est totalement absente d'une année → créer le fichier

### ◉ Règle de vérification finale
◉ Après la dernière phase, vérifier que les **7 phases** ont été exécutées :
```
□ PHASE 0: LOAD      — fichiers chargés ?
□ PHASE 1: GAP        — gaps identifiés ?
□ PHASE 2: CREDO      — questions générées ?
□ PHASE 3: SEARCH     — @MNEMO_Q + @WEB + @FETCH exécutés ?
□ PHASE 4: REGISTRY   — registre construit avec URLs ?
□ PHASE 5: GATES      — 6 vérifications passées ?
□ PHASE 6: INJECT     — fichiers écrits, compteurs à jour ?
□ PHASE 7: MEMORY     — @write_memory exécuté ?
```
◉ SI une phase est manquante → [PHASE {N} NON EXÉCUTÉE] → la compléter avant de terminer

---

## △ PHASE 0: LOAD — Chargement des références

### ◆ Fichiers à charger AVANT toute recherche

```
⟐ Chroniques existantes de la période ciblée
   → rtk ls chroniques/AAAA/    (repérer les fichiers existants)
   → read_files chroniques/AAAA/AAAA_DIM.md  (pour chaque DIM ciblée)
   → read_files chroniques/README.md        (métriques globales)

⟐ KERNEL Truth Engine (axiomes, priorité source, symboles)
   → truth-engine-v2/KERNEL.md

⟐ PROTOCOLE_ENRICHISSEMENT.md (format AFP, compteurs, pièges)
   → investigations/.../01_donnees/chroniques/PROTOCOLE_ENRICHISSEMENT.md

⟐ Si la session cible une enquête spécifique :
   → Lire l'INVESTIGATION.md ou APEX.md correspondant
```

### ◆ Sous-phase AUDIT [v1.1] — Détection des anomalies avant injection

◉ AVANT toute injection, scanner les fichiers existants pour détecter :
- Codes non standard (ni ✅⚠❌💀) → [ANOMALIE: CODE] — les corriger
- Lignes vides parasites → [ANOMALIE: FORMAT] — les supprimer
- Headers manquants (`> N événement(s)`) → [ANOMALIE: HEADER] — les ajouter
- Lignes orphelines hors tableau → [ANOMALIE: STRUCTURE] — les intégrer

◉ Noter le nombre d'anomalies : `0 anomalie(s) détectée(s)` ou `N anomalie(s) → corriger avant PHASE 6`

### ◉ À l'issue du chargement, le LLM doit pouvoir répondre :

1. Quels fichiers chroniques existent pour la période ciblée ?
2. Quels sont les compteurs actuels ?
3. Quels sont les faits déjà présents (pour éviter les doublons) ?
4. Quelles anomalies de format existent (codes, lignes, headers) ?
4. Quels KERNEL axiomes s'appliquent ?

---

## △ PHASE 1: GAP — Analyse des angles morts

### ◆ Pour chaque dimension ciblée, calculer :

| Métrique | Formule | Seuil d'alerte |
|----------|---------|----------------|
| Densité | nb_événements / nb_années_couvertes | < 3 → SOUS-COUVERT |
| Saturation | nb_événements / max_dimension | < 10% → ANGLE MORT |
| Couverture temporelle | années_couvertes / 237 | < 25% → TROU TEMPOREL |
| Équilibre code | %✅ vs %❌ vs %⚠ vs %💀 | Déséquilibre > 80% → BIAIS |

### ◆ Types de gaps à identifier

1. **Gap dimensionnel** : une dimension entièrement sous-couverte (ex: SCI=43, REL=36, DEMO=70)
2. **Gap temporel** : une décennie vide pour une dimension donnée
3. **Gap thématique** : un sujet majeur absent (ex: pas de faits sur les scandales pharmaceutiques dans SANT)
4. **Gap de sourcing** : des faits existants sans URL vérifiée (❧ sans tentative HEAD)
5. **Gap dialectique** : une dimension avec uniquement des ❌ (pas de ✅, pas de ⚠ nuancé)

### ◉ Générer une liste de cibles prioritaires (3-5 max par session)

Format : `[PRIORITÉ] Dimension Période — raison du gap — estimation du potentiel`

**Exemple :**
```
[P1] SCI 1975-1995 — 8 événements seulement pour 20 ans de recherche française — potentiel : 15-25 faits (prix Nobel, CNRS, grands programmes)
[P2] REL 1905-2005 — 12 événements, focale uniquement catholique — potentiel : 10-15 faits (laïcité, autres cultes, sécularisation)
```

---

## △ PHASE 2: CREDO — Questions de recherche

### ◆ Pour chaque cible prioritaire, générer 6-12 questions selon le CREDO du KERNEL :

```
C ⏰ Ξ (Chronologie)  : Quels événements majeurs jalonnent cette dimension sur la période ?
    Ex: Quelles sont les grandes lois, crises, réformes, scandales ?

R € ♦ 🌐 (Ressources) : Quels budgets, flux financiers, coûts, transferts ?
    Ex: Quel est le budget de l'institution X ? Le coût du scandale Y ?

E ◈ ⊕ ⊗ (Preuves)     : Quels rapports officiels, commissions d'enquête, procès, audits ?
    Ex: Quel rapport parlementaire, IGAS, Cour des comptes documente ce sujet ?

D Ω Ψ Ξ (Doute)       : Quelles versions alternatives, critiques, contre-récits ?
    Ex: Quelle version officielle a été contredite ? Par qui ?

O ⏰ Ξ (Omission)     : Quels sujets passés sous silence, enterrés, oubliés ?
    Ex: Quel scandale a été étouffé ? Quelle alerte ignorée ?

+ Λ Φ Σ (Rhétorique)  : Quels discours, propagande, narratifs dominants ?
    Ex: Quel mot/cliché/narrative masque la réalité ?
```

### ◆ Règles de génération

◉ Au moins 1 question par lettre du CREDO (C, R, E, D, O, +)
◉ Privilégier les questions qui appellent des faits DATÉS et CHIFFRÉS
◉ Éviter les questions trop larges (« qu'est-ce qui s'est passé en France ? »)
◆ Maximum 12 questions par session (contrainte de temps)
◆ Si la dimension est très sous-couverte → + de questions C et R (faits de base)
◆ Si la dimension est bien couverte → + de questions D et O (angles morts)

---

## △ PHASE 3: SEARCH — Recherche multi-source

### ◉ Règle absolue [v1.1] : 3 étapes OBLIGATOIRES

```
ÉTAPE 1 — @MNEMO_Q (recherche mémoire locale)
  ◉ OBLIGATOIRE : exécuter AVANT toute recherche web
  ◉ search_memory(query="{dimension} {période}", limit=5, search_mode="hybrid")
  ◉ Si des mémoires existent → les lire avant d'aller sur le web
  → BLOCK si cette étape est sautée

ÉTAPE 2 — @WEB (recherche DuckDuckGo)
  ◉ researcher_web(prompt="{question contextualisée}")
  ◉ NOTER l'URL de chaque résultat — SANS URL, pas de fait
  ◉ IMPORTANT : le researcher_web produit des synthèses, PAS des URLs
  → Après chaque résultat @WEB, chaîner avec @FETCH sur les sources mentionnées

ÉTAPE 3 — @FETCH (lecture d'URL directe)
  ◉ read_url(url="{url}", max_chars=12000)
  ◉ Pour chaque source mentionnée par le researcher_web, exécuter read_url()
  ◉ Extraire : faits (date, description, chiffres), citations directes
  → Chaque fait DOIT avoir une URL source — sinon ❧

RÈGLE : 1 résultat de recherche = 1 URL minimum. Si pas d'URL → le fait est ❧
RÈGLE : SI read_url() échoue → marquer ⁅ (lien mort), pas ✦
```

### ◆ Pour chaque résultat de recherche, capturer :

```
URL       : l'URL exacte de la source (OBLIGATOIRE)
Type      : ◈ primaire / ◉ secondaire / ○ adversaire
Faits     : liste des faits identifiés (date, description, chiffres)
Fiabilité : ✦ (HEAD 200 OK) / ✧ (source secondaire OK) / ⁅ (lien mort) / ❧ (pas d'URL)
Citation  : citation directe si affirmation clé
```

### ◆ Règles de diversité des sources (KERNEL §1 — adapté)

◉ Au moins 2 types de sources différents par fait majeur (◈ + ◉ ou ◈ + ○)
◉ Si un fait n'est documenté que par une source unique → marquer ❧ avec note [SOURCE UNIQUE]
◆ Si la source est clairement partisane (ex: communiqué gouvernemental) → chercher une source ○ adversaire
◆ Si la source est académique/papier → citer l'URL de la page de recherche @WEB

### ◆ INTERDICTION [v1.1]
❌ Ne pas sauter @MNEMO_Q
❌ Ne pas injecter un fait sans URL source
❌ Ne pas utiliser `researcher_web` seul — TOUJOURS chaîner avec `read_url()`

---

## △ PHASE 4: REGISTRY — Registre des faits atomiques

### ◆ [v1.1] Format simplifié — 5 colonnes obligatoires

◉ Le registre 9-colonnes était trop lourd (simulation : 135-225 champs par session).
◉ Format v1.1 : 5 colonnes obligatoires, 3 optionnelles.

```
Année      : AAAA ou AAAA-AAAA (plage)          ← OBLIGATOIRE
Dimension  : AGR/CUL/.../TRA                    ← OBLIGATOIRE
Description : Texte court, commence par majuscule ← OBLIGATOIRE
Code       : ✅ / ⚠ / ❌ / 💀                    ← OBLIGATOIRE
URL        : URL de la source                   ← OBLIGATOIRE
Fiabilité  : ✦ / ✧ / ⁅ / ❧                     ← OBLIGATOIRE (par défaut ❧)
Acteur     : Acteur principal                   ← OPTIONNEL
Chiffre    : Chiffre clé                        ← OPTIONNEL
Note       : [HYPOTHÈSE], [SOURCE UNIQUE]        ← OPTIONNEL
```

### ◆ Règles du registry

◉ Chaque fait = UNE ligne de registre (pas de doublon, pas d'agrégat)
◉ Description entre 50 et 250 caractères — précise, factuelle, pas de commentaire
◉ Code impact : ✅ progrès/positif | ⚠ alerte/tension | ❌ négatif/critique | 💀 catastrophe
◉ **URL OBLIGATOIRE** — même pour les faits secondaires. Si pas d'URL directe → URL de la page @WEB
◉ **Si pas d'URL du tout** → marquer ❧ avec `[HYPOTHÈSE]` et continuer (mais tenter 1 recherche supplémentaire)
◆ Si plage d'années > 5 ans → ranger dans le dossier de l'année de fin, NOTER dans `chroniques/plages_annees.md`
◆ Si révélation (rapport qui révèle un fait passé) → DEUX entrées : fait historique + révélation
◆ Si un fait touche 2 dimensions (ex: Charlie Hebdo → REL + TER) → UNE ligne par dimension

### ◆ Format de sortie du registry (avant injection)

```markdown
## Registry — [Dimension] [Période]

| # | Année | Dim | Description | Code | URL | Fiabilité | Acteur | Chiffre |
|---|-------|-----|-------------|------|-----|-----------|--------|---------|
| 1 | 2004 | REL | Loi signes religieux ostensibles écoles publiques | ❌ | https://www.legifrance.gouv.fr/... | ✦ | Raffarin | 15 mars 2004 |
| 2 | 2021 | REL | Rapport CIASE Sauvé : 216 000 victimes abus sexuels clergé | 💀 | https://www.ciase.fr/... | ✦ | Jean-Marc Sauvé | 216 000 |
```

→ Ce registre est une **étape intermédiaire** de vérification avant injection.
→ Les URLs et fiabilités ne sont PAS injectées dans les chroniques (format 4 colonnes).
→ **Conserver le registre comme trace de la session** (dans le rapport de session).

---

## △ PHASE 5: GATES — Vérification qualité

### ◆ 6 vérifications AVANT injection

```
□ GATE-1 : DATATION
   Chaque fait a une année ou plage d'années valide ?
   → Si non → corriger ou exclure

□ GATE-2 : DÉDUPLICATION
   Aucun doublon sémantique avec les chroniques existantes ?
   → Vérifier en chargeant le fichier cible
   → Si doublon → ne pas ajouter (mais noter [CONFIRMÉ])

□ GATE-3 : SOURCAGE [v1.1 renforcé]
   Chaque fait a au moins 1 URL source ?
   → Si ❧ sans URL → marquer [HYPOTHÈSE] et RETOUR PHASE 3 pour 1 tentative supplémentaire
   → Si 2e tentative sans URL → NOTER [HYPOTHÈSE FORTE] et continuer (documenté)

□ GATE-4 : HEAD CHECK (OBLIGATOIRE pour ✦ [v1.1])
   Les URLs ✦ retournent-elles 200 OK ?
   ◉ OBLIGATOIRE pour les faits marqués ✦
   ◉ Si HEAD échoue → rétrograder ✦→⁅ et NOTER la raison
   ◉ Si pas de HEAD check → rétrograder ✦→❧ (par défaut)

□ GATE-5 : COHÉRENCE
   Le code impact (✅⚠❌💀) est-il cohérent avec la description ?
   → Si incohérence → corriger le code

□ GATE-6 : COMPTEUR [v1.1 renforcé]
   Le compteur dans l'en-tête du fichier cible est-il correct après ajout ?
   → COMPTER les lignes de données MANUELLEMENT (pas à la confiance)
   → Remplacer '> N événement(s)' par le nouveau total
   → VÉRIFIER : relire le fichier après édition, compter visuellement
```

### ◆ Seuils d'acceptation

| Résultat GATES | Action |
|----------------|--------|
| 6/6 ✅ | Injection directe |
| 4-5/6 ✅ | Injection avec notes de correction |
| < 4/6 ✅ | HALTE — retour PHASE 3 pour compléter |

### ◆ Vérification finale après injection [v1.1]
◉ Relire le fichier modifié
◉ Compter visuellement les lignes de données
◉ Vérifier qu'aucune ligne vide parasite n'a été créée
◉ Vérifier que tous les codes sont standards

---

## △ PHASE 6: INJECT — Écriture dans les Chroniques

### ◆ Procédure d'injection (AFP-compliant)

```
1. LIRE le fichier cible
   read_file(path="chroniques/AAAA/AAAA_DIM.md")
   → Vérifier le format, le compteur, les lignes existantes

2. VÉRIFIER les doublons
   Pour chaque nouveau fait, scanner les lignes existantes
   → Si description similaire (même événement, même année) → DOUBLON → ne pas ajouter
   → Si fait complémentaire (même événement, chiffre différent) → AJOUTER avec note

3. AJOUTER les lignes
   str_replace(file="chroniques/AAAA/AAAA_DIM.md",
                oldString="| Année | Dimension | Description | Code |\n|---|---|---|---|\n",
                newString="| Année | Dimension | Description | Code |\n|---|---|---|---|\n| AAAA | DIM | Nouveau fait | ❌ |\n")

   → Ajouter AVANT la ligne vide finale du tableau
   → OU utiliser la dernière ligne comme ancre

4. METTRE À JOUR le compteur
   str_replace(file="chroniques/AAAA/AAAA_DIM.md",
                oldString="> {N} événement(s)",
                newString="> {N+Increment} événement(s)")

5. (Optionnel) REPORTER dans HYPER_MATRICE_UNIFIEE
   → Si le fait est significatif → ajouter aussi dans le fichier maître
```

### ◆ Format attendu d'une ligne

```markdown
| AAAA | DIM | Description du fait, commence par majuscule, pas de point final | ❌ |
```

### ◆ Création de fichier si inexistant

```markdown
# Chronique AAAA — Dimension DIM

> Fait atomique extrait de l'HYPER-MATRICE FRANCE 1975-2026.
> 0 événement(s) classé(s) dans la dimension DIM pour l'année AAAA.

| Année | Dimension | Description | Code |
|---|---|---|---|
```

→ Puis ajouter la 1ʳᵉ ligne et changer `0 événement(s)` → `1 événement(s)`

### ◆ Cas plage d'années

- Plage ≤ 5 ans : ranger dans le dossier de l'année de fin
- Plage > 5 ans : ajouter dans `chroniques/plages_annees.md`
- Révélation postérieure : DEUX entrées (fait + révélation)

---

## △ PHASE 7: MEMORY — Sauvegarde Mnemolite [OBLIGATOIRE]

### ◉ Règle : MEMORY est OBLIGATOIRE — ne pas terminer sans cette étape

### ◆ Après chaque session, indexer les découvertes

```python
search_memory(query="{dimension} {période} nouveaux faits", limit=3, search_mode="hybrid")
write_memory(
    title="FAIT-MINEUR: {dimension} {période} — {N} nouveaux faits",
    content="Résumé des faits ajoutés et des sources trouvées",
    memory_type="note",
    tags=["fait_mineur", "{dimension}", "{année}", "chroniques"]
)
```

### ◆ Informations à conserver

- Dimension et période traitée
- Nombre de faits ajoutés (et compteur final)
- Sources clés trouvées (URLs ✦)
- Gaps restants pour la dimension
- Leçons pour les sessions futures

### ◆ VÉRIFICATION FINALE — Les 7 phases

◉ Retourner à la vérification de la section MISSION pour confirmer les 7 phases

---

## △ APPENDICE A: Simulation réelle sur REL (v1.1)

Une simulation a été exécutée sur la dimension REL. Résultats détaillés dans `simulation_fait_mineur_REL_RAPPORT.md`.

### Résumé de la simulation

| Métrique | Valeur |
|----------|:------:|
| Fichiers créés | 7 (2004, 2010, 2012, 2015, 2020, 2022, 2025) |
| Fichiers mis à jour | 2 (2009, 2021) |
| Faits ajoutés | 9 |
| Compteur REL | 38→47 |
| Gaps identifiés | 5 (corrigés en v1.1) |

### Les 5 gaps corrigés en v1.1

| Gap | Correctif v1.1 |
|-----|----------------|
| @MNEMO_Q sauté | ÉTAPE 1 obligatoire avec block si sautée |
| Pas d'URLs dans résultats web | Chaînage obligatoire @WEB → @FETCH |
| Registre 9 colonnes trop lourd | Passage à 5 colonnes obligatoires |
| Sourçage impossible dans chroniques | Colonne URL dans registre, trace externe |
| PHASE 7 oubliée | Vérification finale 7 phases + interdiction de terminer sans |

---

## △ APPENDICE A: Exemple de session FAIT-MINEUR (v1.0)

### Cible : Dimension SCI (Science) — Période 1970-2000

**PHASE 0 — LOAD :** 17 événements SCI pour 30 ans. Fichiers lus : 1970-2000/SCI.md

**PHASE 1 — GAP :** Densité = 0,6 événements/an → SOUS-COUVERT. Manquent : budget CNRS, prix Nobel français, grands programmes (TGV, Ariane, Minitel, nucléaire)

**PHASE 2 — CREDO :** 8 questions dont :
- C : Quels sont les grands programmes scientifiques français 1970-2000 ?
- R : Budget CNRS 1970-2000 : évolution en % PIB ?
- E : Rapports sur la fuite des cerveaux ? Prix Nobel français ?
- D : La science française a-t-elle décliné ? Quand ? Preuves ?

**PHASE 3 — SEARCH :** @MNEMO_Q → 0 résultats. @WEB → 8 résultats dont 3 ◈ (Comptes CNRS, liste prix Nobel, rapports OST). @FETCH → 4 pages extraites.

**PHASE 4 — REGISTRY :** 12 faits extraits, dont :
| 1972 | SCI | Budget CNRS : 1,2 MdF (0,4% PIB) | ❌ | https://... | ✦ | CNRS |
| 1991 | SCI | Prix Nobel médecine : Neher/Sakmann (Allemagne), pas de Français depuis 1965 | ⚠ | https://... | ✧ | Nobel |
| 1998 | SCI | Création AERES (évaluation recherche) | ✅ | https://... | ◈ | |

**PHASE 5 — GATES :** 6/6 ✅

**PHASE 6 — INJECT :** 12 lignes ajoutées dans 6 fichiers chroniques (1970-2000/SCI.md). Compteurs mis à jour.

**PHASE 7 — MEMORY :** Sauvegarde Mnemolite. Tags [fait_mineur, SCI, 1970-2000]

---

## △ APPENDICE B: Dimensions — codes et description

| Code | Dimension | Description | Nb actuel | Priorité |
|------|-----------|-------------|:---------:|:--------:|
| AGR | Agriculture | PAC, filières, crises agricoles | 254 | 🟢 |
| CUL | Culture | Cinéma, livre, patrimoine, CNC | 365 | 🟢 |
| DEMO | Démographie | Natalité, mortalité, pyramide âges | 70 | 🔴 |
| DIP | Diplomatie | Affaires étrangères, UE, alliances | 92 | 🟡 |
| ECO | Économie | Finances, fiscalité, industrie, dette | 1 244 | 🟢 |
| EDU | Éducation | École, université, réformes, PISA | 318 | 🟢 |
| ENV | Environnement | Climat, pollution, nucléaire, biodiversité | 206 | 🟢 |
| IMM | Immigration | Flux, intégration, politiques, asile | 111 | 🟡 |
| JUR | Justice | Procès, lois, jurisprudence, affaires | 494 | 🟢 |
| MED | Médias | Concentration, liberté presse, SIG | 173 | 🟡 |
| MIL | Militaire | Armée, défense, budgets, opérations | 187 | 🟡 |
| POL | Politique | Institutions, élections, gouvernements | 803 | 🟢 |
| REL | Religion | Cultes, laïcité, Églises, sécularisation | 36 | 🔴 |
| SANT | Santé | Hôpital, épidémies, scandales, Sécu | 186 | 🟡 |
| SCI | Science | Recherche, CNRS, prix Nobel, innovation | 43 | 🔴 |
| SOC | Social | Protection sociale, pauvreté, logement | 659 | 🟢 |
| SPO | Sport | JO, football, fédérations, dopage | 243 | 🟢 |
| TEC | Technologie | Industrie, numérique, énergie, transport | 321 | 🟢 |
| TER | Terrorisme | Attentats, antiterrorisme, radicalisation | 69 | 🔴 |
| TRA | Transports | SNCF, RATP, infrastructures, aérien | 115 | 🟡 |

🔴 = urgence (densité < 1 événement/an) — 🟡 = à surveiller — 🟢 = couverture acceptable

---

## △ APPENDICE C: Codes impact

| Code | Signification | Quand l'utiliser |
|------|--------------|------------------|
| ✅ | Positif / constructif | Loi votée, innovation, progrès social, réussite |
| ⚠ | Préoccupant / alerte | Tension, risque, réforme avortée, transition |
| ❌ | Négatif / critique | Répression, échec, crise, blocage, austérité |
| 💀 | Fatal / catastrophique | Crime, attentat, catastrophe, scandale majeur |

---

## △ APPENDICE D: Pièges fréquents [v1.1]

| Situation | À faire |
|-----------|---------|
| Scanner de vérification trop agressif | Vérifier ligne par ligne, pas par mots-clés |
| Dimensions oubliées | Scanner les 20 dimensions, pas seulement la cible |
| Année du document au lieu de l'année du fait | Lire le paragraphe, extraire l'année du contexte |
| Chiffre non vérifié | Croiser les sources avant d'ajouter |
| Compteur non mis à jour | Relire le fichier après ajout, compter les lignes |
| Doublon non détecté | Lire le fichier avant d'ajouter, vérifier sémantiquement |
| Surcharger une session | Maximum 15-25 faits par session (qualité > quantité) |
| Ignorer les dimensions sous-couvertes | Prioriser SCI, REL, DEMO, TER, IMM avant ECO, POL |

---

*FAIT-MINEUR v1.1 — 2026-06-27*
*Héritage : Truth Engine KERNEL v2.0 + Protocole investigation v2.4 NREF + PROTOCOLE_ENRICHISSEMENT.md*
*Périmètre : 20 dimensions × 237 années (1789-2026) × 7 phases pipeline*
*Révision v1.1 : 5 gaps critiques corrigés suite simulation REL — voir `simulation_fait_mineur_REL_RAPPORT.md`*

---

## △ APPENDICE B: Dimensions — codes et description

| Code | Dimension | Description | Nb actuel | Priorité |
|------|-----------|-------------|:---------:|:--------:|
| AGR | Agriculture | PAC, filières, crises agricoles | 254 | 🟢 |
| CUL | Culture | Cinéma, livre, patrimoine, CNC | 365 | 🟢 |
| DEMO | Démographie | Natalité, mortalité, pyramide âges | 70 | 🔴 |
| DIP | Diplomatie | Affaires étrangères, UE, alliances | 92 | 🟡 |
| ECO | Économie | Finances, fiscalité, industrie, dette | 1 244 | 🟢 |
| EDU | Éducation | École, université, réformes, PISA | 318 | 🟢 |
| ENV | Environnement | Climat, pollution, nucléaire, biodiversité | 206 | 🟢 |
| IMM | Immigration | Flux, intégration, politiques, asile | 111 | 🟡 |
| JUR | Justice | Procès, lois, jurisprudence, affaires | 494 | 🟢 |
| MED | Médias | Concentration, liberté presse, SIG | 173 | 🟡 |
| MIL | Militaire | Armée, défense, budgets, opérations | 187 | 🟡 |
| POL | Politique | Institutions, élections, gouvernements | 803 | 🟢 |
| REL | Religion | Cultes, laïcité, Églises, sécularisation | 36 | 🔴 |
| SANT | Santé | Hôpital, épidémies, scandales, Sécu | 186 | 🟡 |
| SCI | Science | Recherche, CNRS, prix Nobel, innovation | 43 | 🔴 |
| SOC | Social | Protection sociale, pauvreté, logement | 659 | 🟢 |
| SPO | Sport | JO, football, fédérations, dopage | 243 | 🟢 |
| TEC | Technologie | Industrie, numérique, énergie, transport | 321 | 🟢 |
| TER | Terrorisme | Attentats, antiterrorisme, radicalisation | 69 | 🔴 |
| TRA | Transports | SNCF, RATP, infrastructures, aérien | 115 | 🟡 |

🔴 = urgence (densité < 1 événement/an) — 🟡 = à surveiller — 🟢 = couverture acceptable

---

## △ APPENDICE C: Codes impact

| Code | Signification | Quand l'utiliser |
|------|--------------|------------------|
| ✅ | Positif / constructif | Loi votée, innovation, progrès social, réussite |
| ⚠ | Préoccupant / alerte | Tension, risque, réforme avortée, transition |
| ❌ | Négatif / critique | Répression, échec, crise, blocage, austérité |
| 💀 | Fatal / catastrophique | Crime, attentat, catastrophe, scandale majeur |

---

## △ APPENDICE D: Pièges fréquents

| Situation | À faire |
|-----------|---------|
| Scanner de vérification trop agressif | Vérifier ligne par ligne, pas par mots-clés |
| Dimensions oubliées | Scanner les 20 dimensions, pas seulement la cible |
| Année du document au lieu de l'année du fait | Lire le paragraphe, extraire l'année du contexte |
| Chiffre non vérifié | Croiser les sources avant d'ajouter |
| Compteur non mis à jour | Relire le fichier après ajout, compter les lignes |
| Doublon non détecté | Lire le fichier avant d'ajouter, vérifier sémantiquement |
| Surcharger une session | Maximum 15-25 faits par session (qualité > quantité) |
| Ignorer les dimensions sous-couvertes | Prioriser SCI, REL, DEMO, TER, IMM avant ECO, POL |

---

*FAIT-MINEUR v1.0 — 2026-06-27*
*Héritage : Truth Engine KERNEL v2.0 + Protocole investigation v2.4 NREF + PROTOCOLE_ENRICHISSEMENT.md*
*Périmètre : 20 dimensions × 237 années (1789-2026) × 7 phases pipeline*
