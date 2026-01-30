# PROMPT GÉNÉRATION TWEETS — v3.1 UPDATE

**Date:** 2025-11-12
**Base:** [TWEET_GENERATION_PROMPT.md](TWEET_GENERATION_PROMPT.md:1) v3.0
**Nouveautés:** Intégration patterns avancés tweets 250→150 (les plus aboutis)
**Référence:** [TWEET_PATTERNS_ADVANCED.md](TWEET_PATTERNS_ADVANCED.md:1)

---

## I. NOUVEAUX PATTERNS OBLIGATOIRES

### 1. **ContreArgumentLoyal** (Anticipation Objections)

**QUAND:** Type D long avec thèse controversée OU sujets à forte opposition prévisible

**FORMAT:**
```
[Développement thèse]

*ContreArgumentLoyal:* "[Objection prévisible citation]"
**Réponse:** [Réfutation courte argumentée + preuve]

👉 Conséquence: [...]
```

**EXEMPLE RÉEL (234):**
```
*ContreArgumentLoyal:* "Sans limite, le débat devient toxique."
**Réponse:** une limite claire, publiée, contestable protège; une limite floue et déléguée étouffe.
```

**RÈGLE:** Anticiper ≥1 objection avant conclusion section pour tweets Type D ≥2000 mots

---

### 2. **Définitions Inline** (Acronymes/Concepts)

**OBLIGATOIRE:** Première occurrence TOUJOURS définie immédiatement

**FORMAT STANDARD:**
```
**Acronyme** — _Expansion complète italique_ (contexte) : [explication courte]
```

**EXEMPLES:**
- `**DSA** — _Digital Services Act_ (UE) depuis **17/02/2024**`
- `**ARCOM** : _Autorité de régulation de la communication audiovisuelle et numérique_ (régulateur médias/plateformes)`

**ALTERNATIVE FIN TWEET (si ≥5 acronymes):**
```
_Glossaire utile_ — **DSA**: règlement · **ARCOM**: régulateur · **CNIL**: données.
```

**RÈGLE:** Inline prioritaire, glossaire fin si tweet court Type E OU ≥5 acronymes

---

### 3. **Double Conséquence Systématique**

**OBLIGATOIRE:** TOUJOURS dériver implications pour 2 acteurs distincts

**FORMAT:**
```
👉 Conséquence: **[acteur 1]** — [implication spécifique]
👉 Conséquence: **[acteur 2]** — [implication spécifique]
```

**PAIRES RÉCURRENTES:**
- citoyen + gouvernance
- légal + citoyen
- pluralisme + budget public
- industrie + gouvernance
- système + public

**RÈGLE:** JAMAIS une seule conséquence, minimum 2 perspectives différentes

---

### 4. **MYTHES VS FAITS Section**

**QUAND:** Idées reçues/croyances répandues à déconstruire

**FORMAT:**
```
──────────────────────────────
**MYTHES VS FAITS (ANTIDOTE RAPIDE)**

Mythe: "[Croyance répandue]"
Fait: [Correction factuelle avec preuve]

Mythe: "[Autre croyance]"
Fait: [Correction]

[...]
──────────────────────────────
```

**PLACEMENT:** Avant conclusion finale, après développement principal

---

### 5. **Payoff Opérationnel**

**QUAND:** Analyse qui doit déboucher sur action concrète mesurable

**FORMAT:**
```
📊 Payoff: [action précise] + [indicateur mesurable] + [deadline optionnelle]
```

**EXEMPLES:**
- `📊 Payoff: avant le vote du PLF 2026, publier 3 scénarios d'assiette + indicateurs résultat`
- `Payoff: si l'on annonce 'la sortie', on fixe des critères vérifiables + horizon`

**VARIANTES:**
- `🎯 **Objectif réel** :`
- `**Verdict:**`
- `✅ **Exiger/faire** :`

---

### 6. **Règle X–Y–Z Mémorisable**

**QUAND:** Méthode citoyenne simplifiable en formule numérique

**FORMAT:**
```
**Règle [X]–[Y]–[Z]** : [X description], [Y description], [Z description]
```

**EXEMPLES:**
- `**Règle 3D — Date • Document • Droit**`
- `**Règle 3–2–1** → 3 sources, 2 min vérif, 1 signalement`

**PLACEMENT:** Fin tweet Type E court, outil mnémotechnique

---

### 7. **Séparateurs — Variantes par Longueur**

**Type D très long (≥2000 mots):**
```
──────────────────────────────
```

**Type D/C moyen (1000-2000 mots):**
```
–––
```

**Subdivisions internes (rare):**
```
···
```

**Markdown (≥3 sections H3):**
```
---
```

---

## II. PATTERNS NARRATIFS AVANCÉS

### **Structure Tripartite Standard**

**QUAND:** Analyse politique/économique nécessitant contexte + mécanisme + cui bono

**FORMAT:**
```
**Les faits**
• [Fait 1 chiffré/daté]
• [Fait 2 chiffré/daté]
• [Fait 3 chiffré/daté]

**Comment ça marche**
On [mécanisme manipulation 1].
On [mécanisme manipulation 2].
On [mécanisme manipulation 3].

**Qui profite / qui paie**
Gagnants : [acteurs bénéficiaires]
Perdants : [acteurs impactés]
```

**PLACEMENT:** Début tweet Type C/D après hook

---

### **Duo Conclusion Actionnable**

**FORMAT:**
```
**Gardez le sang-froid**
[Identification manipulation + antidote cognitif]

**Concrètement, maintenant**
[Actions spécifiques avec délais/indicateurs]
```

---

### **Faisceaux d'indices (Liste)**

**FORMAT:**
```
**Faisceaux d'indices sur [sujet]** :
• [Indice 1 observable]
• [Indice 2 observable]
• [Indice 3 observable]
```

**DIFFÉRENCE:** "Faisceaux" (pluriel) = liste signes // "Faisceau ICEBERG" = structure 3 niveaux

---

### **Diagnostic Temporel**

**FORMAT:**
```
**Diagnostic ([année]→[année])** : [résumé pattern échec].
[Année 1] ([événement]) → [Année 2] ([événement]) : [conclusion].
```

---

### **Ce qui coince / Ce qui marche**

**FORMAT:**
```
**Ce qui coince** : [liste problèmes]

**Ce qui marche** (🧩 [principe]) :
• [Solution 1 concrète]
• [Solution 2]
```

---

### **Traduction pédagogique:**

**FORMAT:**
```
Traduction pédagogique :
– [Implication 1 technique expliquée simplement]
– [Implication 2]
```

---

### **Rappel factuel:**

**FORMAT:**
```
**Rappel factuel :** [Liste contradictions/échecs historiques acteur] → [ironie conclusion]
```

---

### **Bilan:** Intro

**FORMAT:**
```
⚖️ **Bilan** : [indicateur 1] **valeur**, [indicateur 2] **valeur**
📊 **[Catégorie]** : [indicateur] valeur
```

---

## III. TYPE F — RAPPORT JURIDIQUE ULTRA-LONG

**NOUVEAU TYPE IDENTIFIÉ**

**Caractéristiques:**
- **Longueur:** 5000-15000 mots (jusqu'à 609 lignes)
- **Structure:** Sections I-XX numérotation romaine
- **Séparateurs:** Longs (30 tirets) systématiques entre CHAQUE section
- **Glossaire:** Section dédiée obligatoire (pas inline)
- **Checklists:** Procédurales multiples (≥3)
- **Tableaux:** Métriques, KPI, seuils chiffrés nombreux
- **Tone:** Mélange académique rigoureux + pamphlétaire percutant

**EXEMPLE:** Tweet 239 (Cyberharcèlement, 609 lignes, structure I-XX complète)

**FORMAT TYPE:**
```
⚠️ **[TITRE MAJUSCULES]**

[Intro contextuelle 2-3 phrases]

──────────────────────────────
**I - [SECTION MAJUSCULES]**

[Développement avec définitions, worked examples]

👉 Conséquence: **[acteur 1]** — [...]
👉 Conséquence: **[acteur 2]** — [...]

──────────────────────────────
**II - [SECTION]**
[...]

──────────────────────────────
[...sections III-XIX...]

──────────────────────────────
**XX - CONCLUSION (PROPRE, CARRÉE, PAMPHLÉTAIRE)**

[Synthèse 3-5 phrases]
Prochain pas clair : [action + deadline]
[Formule finale citoyenne]
```

**SECTIONS RÉCURRENTES TYPE F:**
- **DÉFINITIONS UTILES** (glossaire académique)
- **MÉTRIQUES INDISPENSABLES**
- **CHECKLIST EN X POINTS (15 JOURS MAX)**
- **QUESTIONS CLAIRES (À CHAQUE ACTEUR)**
- **CE QUE PEUVENT FAIRE LES CITOYENS**
- **CONCLUSION (PROPRE, CARRÉE, PAMPHLÉTAIRE)**

**USAGE:** Dossiers juridiques/techniques exigeant exhaustivité procédurale

---

## IV. ÉMOJIS FONCTIONNELS NOUVEAUX

**Intégrer à palette existante:**

| Émoji | Usage | Contexte |
|-------|-------|----------|
| 🧮 | Arithmétique/comparaison | Chiffres, abstention |
| 🛡️ | Protection/garde-fous | Libertés, sécurité |
| 🪧 | Manifestation/mobilisation | Guerre, débat |
| 📕 | Liste méthodes/tactiques | Manipulation systémique |
| 🧩 | Procédure/ingénierie | Solutions techniques |
| 🕊️ | Paix | Diplomatie |
| 🧭 | Navigation/cap | Orientation stratégique |
| ✅ | Action validée | Checklist citoyenne |
| 💣 | Impact/explosion | Conséquence majeure |

---

## V. TAG APEX

**NOUVEAU:** Signale tweets "ultra-aboutis" analyses de pointe

**FORMAT:**
```
**APEX — [Titre accrocheur]**
[Contenu analyse fine]
```

**CARACTÉRISTIQUES:**
- Analyse comportement politique fin
- Décryptage manipulation narrative précis
- Méthodologie citoyenne actionnable
- Ton pamphlétaire + rigueur académique maximale

**EXEMPLES:**
- `**APEX — Quand l'aveu devient stratégie.**`
- `**APEX — Une phrase domestique ne lave pas le soupçon.**`

---

## VI. CHECKLIST INTÉGRÉE v3.1

**Avant génération tweet Type D long abouti, vérifier:**

### Checklist Contenu (v3.0 existante)
- [x] Hook choc ≤2 phrases
- [x] ≥3 facts ultra-précis (noms + montants + dates)
- [x] Citations « guillemets français »
- [x] Acronymes traduits première occurrence
- [x] Gaps documentés
- [x] Chiffres précis (JAMAIS vague)

### **Checklist Patterns Avancés v3.1 (NOUVEAUX)**
- [ ] **ContreArgumentLoyal** anticipé si thèse controversée (Type D ≥2000 mots)
- [ ] **Définitions inline** acronymes première occurrence OU glossaire fin
- [ ] **Double conséquence** systématique (citoyen + gouvernance/légal)
- [ ] **MYTHES VS FAITS** si idées reçues à déconstruire
- [ ] **Payoff/Verdict** actionnable mesurable
- [ ] **Règle X–Y–Z** si méthode simplifiable
- [ ] **Séparateurs adaptés** longueur (long 30 tirets si ≥2000 mots, court 3 tirets sinon)
- [ ] **Structure tripartite** (Les faits + Comment ça marche + Qui profite) si applicable
- [ ] **Tag APEX** si analyse ultra-fine comportement/manipulation
- [ ] **Type F** si dossier juridique/technique nécessitant exhaustivité (≥5000 mots)

### Checklist Style (v3.0 existante)
- [x] Formules percutantes/métaphores (≥2)
- [x] Verbes actifs pamphlétaires
- [x] Zéro sycophancy
- [x] Pédagogique citoyen
- [x] Formule finale mémorable
- [x] Concepts académiques explicités

### Checklist Structure (v3.0 existante)
- [x] 1 émoji titre unique
- [x] Titres gras inline (PAS H2) SAUF Type D/F long
- [x] Si Type D/F: H2 markdown + séparateurs obligatoires
- [x] Listes → ou –
- [x] Émojis sections fonctionnels
- [x] Fin 💣/🧨/🎯 + appel action

---

## VII. PROMPT EXÉCUTION MISE À JOUR

**INPUT:** Investigation Truth Engine I0/I1 (markdown, 3 parties)

**TASK v3.1:**
1. **Extrait révélations** (règlement introuvable, timing, omissions, bénéficiaires)
2. **Identifie pattern** dominant (ICEBERG, FRAMING, MONEY, TEMPORAL, spectacle)
3. **Choisis type** approprié:
   - **Type A** (révélation choc) — 400-800 mots
   - **Type B** (anatomie système) — 600-1200 mots
   - **Type C** (déconstruction spectacle) — 500-1000 mots
   - **Type D** (note stratégique) — 1500-5000 mots, H2 + séparateurs longs
   - **Type E** (pamphlet compact) — 150-500 mots, ultra-compact, NO H2
   - **🆕 Type F** (rapport juridique) — 5000-15000 mots, I-XX, checklists, tableaux, glossaire dédié

4. **🆕 Applique patterns avancés v3.1:**
   - ContreArgumentLoyal si thèse controversée
   - Définitions inline acronymes
   - Double conséquence systématique
   - MYTHES VS FAITS si idées reçues
   - Payoff actionnable mesurable
   - Structure tripartite si analyse politique
   - Tag APEX si analyse ultra-fine

5. **Vérifie checklist qualité v3.1** (contenu + patterns avancés + style + structure)

6. **Vérifie anti-patterns** (intro méthodologique, vague, sycophancy, H2 dans Type A/B/C/E)

**OUTPUT FORMAT:**
```
[EMOJI] **TITRE PERCUTANT**

[Hook ≤2 phrases]

[Développement sections avec patterns v3.1]

💣 **Conclusion/Verdict/Payoff** : [Synthèse]
👉 [Action]. [Action]. [Action].

[Formule mémorable finale]
```

**RENDU:** Version finale prête poster, sans préambule, sans meta-commentaires.

---

## VIII. CHANGELOG v3.1

**Ajouts majeurs:**
1. **7 nouveaux patterns obligatoires** (ContreArgumentLoyal, Définitions inline, Double conséquence, MYTHES VS FAITS, Payoff, Règle X-Y-Z, Séparateurs variantes)
2. **10 patterns narratifs avancés** (Structure tripartite, Duo conclusion, Faisceaux indices, Diagnostic temporel, etc.)
3. **Type F** documenté (rapport juridique ultra-long 5000-15000 mots)
4. **9 émojis fonctionnels nouveaux**
5. **Tag APEX** pour tweets aboutis
6. **Checklist v3.1** étendue (patterns avancés obligatoires)
7. **Glossaire inline vs fin** règles clarifiées
8. **Prompt exécution** mis à jour avec Type F + patterns v3.1

**Base conservée:**
- Tous patterns v3.0 (5 types A-E, vocabulaire 185 concepts, formules choc 40+, structures variantes Type D)
- Anti-patterns complets
- Checklist qualité originale

**Référence complète:** [TWEET_PATTERNS_ADVANCED.md](TWEET_PATTERNS_ADVANCED.md:1) — 47KB, 700+ lignes documentation exhaustive

---

**Version:** 3.1
**Date:** 2025-11-12
**Source:** Analyse tweets 250→104 (focus 250→150 aboutis) + base v3.0 (tweets 103→2)
**Corpus total:** ~150 tweets analysés (102 exhaustifs 103→2, 48 échantillon stratégique 250→150)
**Statut:** Patterns ultra-matures intégrés ✅
