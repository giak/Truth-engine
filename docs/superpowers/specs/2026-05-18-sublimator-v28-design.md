# SUBLIMATOR v28.0 — Design Spec

**Date** : 2026-05-18
**Auteur** : Session brainstorming
**Statut** : En attente de validation utilisateur
**Version cible** : SUBLIMATOR_v28.0.md

---

## 0. RÉSUMÉ EXÉCUTIF

SUBLIMATOR v28.0 est une refonte architecturale majeure de v27.0. Elle résout 5 défaillances systémiques identifiées lors d'audits forensiques sur des articles de sujets variés :

1. **Illusion de l'agent unique** → Cycle multi-agent à 4 rôles distincts
2. **LOI 4 abstraite** → Doctrine complète + glossaire anti-anglicismes + scoring mesurable
3. **PHASE C sans challenge** → Pipeline Écrivain → Critique → Correcteur → Arbitre
4. **Sourcing primaire non enforceé** → DOI/brevets/titres obligatoires pour chaque claim
5. **Nomenclature fichiers non appliquée** → Auto-renommage + migration vers `/articles/`

---

## 1. ARCHITECTURE DU CYCLE MULTI-AGENT (§5.1 révisé)

### 1.1 Pipeline à 4 rôles

Le cycle sectionnel remplace la PHASE A→B→C→D linéaire de v27.0 :

```
┌─────────────────────────────────────────────────────────┐
│                  CYCLE SECTIONNEL v28.0                  │
│                                                         │
│  ÉCRIVAIN ──→ CRITIQUE ──→ CORRECTEUR ──→ ARBITRE       │
│  (PHASE W)    (PHASE R)     (PHASE C)     (PHASE A)      │
│                                                         │
│  Si score ≥4/5 sur tous critères → CHECKPOINT #4        │
│  Si score <4 → retour ÉCRIVAIN (max 3 itérations)        │
│  Si échec après 3 tours → rapport utilisateur           │
└─────────────────────────────────────────────────────────┘
```

### 1.2 PHASE W — ÉCRIVAIN

**Doctrine** : "Journaliste Français d'Enquête" (prompt fourni par l'utilisateur).

**Principes** :
- Toute phrase justifie son existence (information, distinction, raisonnement)
- Tension narrative = faits réels, pas d'emphase artificielle
- Qualifier explicitement le statut de chaque affirmation (fait/interprétation/hypothèse)
- Anti-complaisance : ne pas confirmer une thèse implicite
- Interdits structurels : langue de bois, généralités, vocabulaire incantatoire

**Output** : `draft_v{N}` de la section (400-600 mots)

### 1.3 PHASE R — CRITIQUE

**Doctrine** : Modules cognitifs Ω Ξ Φ Λ M Ψ.

**Modules activés** :
- **Ω** — Analyse de fond : thèses, logique interne, contradictions
- **Ξ** — Diagnostic stylistique : densité, précision lexicale, rythme
- **Φ** — Structure & narration : progression, articulation, tension factuelle
- **Λ** — Contexte & lectorat : niveau de connaissance, seuil de compréhension
- **M** — Mémoire longue : continuité conceptuelle, cohérence globale
- **Ψ** — Métacognition éditoriale : intention réelle vs effet produit

**Scoring (0-5 par critère)** :

| Critère | Question | Seuil |
|---------|----------|-------|
| Pureté lexicale | Zéro anglicisme ? Terminologie FR exacte ? | ≥4 |
| Rigueur factuelle | DOI/patent/titre pour chaque claim substantiel ? | ≥4 |
| Cohérence thèse | Répond à la sous-question ? Pas de dérive ? | ≥4 |
| Style forensic | Pas de théâtralité, ironie, anthropomorphisme ? | ≥4 |
| Structure cognitive | Chaque phrase porte une information ? | ≥4 |

**Règle** : Le Critique NE RÉÉCRIT PAS. Il diagnostique et score. Décision : ACCEPTER ou REJETER.

### 1.4 PHASE C — CORRECTEUR

**Doctrine** : "Rédacteur Français Intraitable" + glossaire anti-anglicismes.

**Actions** :
1. Appliquer les corrections linguistiques du glossaire
2. Remplacer les formulations théâtrales par des formulations cliniques
3. Vérifier la typographie française (guillemets « », espaces insécables, tirets)
4. Corriger les phrases vides ou creuses
5. Produire `corrected_v{N}`

**Règle** : Le Correcteur NE CHANGE PAS le sens. Il corrige la forme et la pureté de langue.

### 1.5 PHASE A — ARBITRE

**Logique de décision** :

```
SI tous scores ≥4 ET Critique = "ACCEPTER"
  → CHECKPOINT #4 (validation utilisateur)

SI score <4 sur ≥1 critère OU Critique = "REJETER"
  → Retour ÉCRIVAIN avec scores + feedback + corrections
  → Itération N+1

SI itération = 3 ET score <4
  → RAPPORT D'ÉCHEC utilisateur
```

**Max itérations** : 3

---

## 2. LOI 4 : PURETÉ DE LA LANGUE + GLOSSAIRE

### 2.1 Nouvelle LOI 4

Remplace les 5 lignes actuelles par une doctrine complète :

**PRINCIPE CARDINAL** : Toute phrase justifie son existence par une information, une distinction conceptuelle ou un raisonnement.

**REGISTRE** : Français soutenu, syntaxe complète, stable, lisible à voix haute.

**INTERDITS STRUCTURELS** (8 items) :
1. Langue de bois ou institutionnelle
2. Formules creuses ("Cependant", "Il convient de noter")
3. Vocabulaire incantatoire
4. Jargon non défini
5. Emphase émotionnelle non justifiée
6. Tournures pompeuses
7. Pseudo-neutralité masquant un flou
8. Généralités non étayées

### 2.2 Glossaire Anti-Anglicismes

| Anglicisme | Remplacement |
|---|---|
| patents | brevets |
| peer-reviewed | évalué par les pairs |
| cloud seeding | ensemencement de nuages |
| grants | subventions |
| supply | approvisionnement |
| grid patterns | quadrillages |
| deep learning | apprentissage profond |
| survey | relevé / cartographie |
| gap | lacune / faille |
| portrayals | représentations |
| town hall | réunion publique |
| principal investigator | directeur de recherche |
| test flight | vol d'essai |
| debunking | réfutation |
| fact-check | vérification des faits |
| feedback | retour |
| draft | brouillon |
| score | note |

**Règle** : Glossaire vivant. Tout anglicisme non listé détecté est ajouté avec sa traduction.

**MÉCANISME DE PERSISTANCE** : Le glossaire est stocké dans un fichier maître :
`tools/prompts/systems/glossaire-anglicismes.md`

Le Correcteur DOIT :
1. Détecter tout anglicisme non listé dans le texte
2. Déterminer la traduction française appropriée
3. **Écrire immédiatement** dans le fichier maître via l'outil `edit` :
   - Ajouter la ligne `| {anglicisme} | {traduction} |` au tableau existant
4. Appliquer la correction dans le texte courant

**Format du fichier maître** :
```markdown
# GLOSSAIRE ANTI-ANGLICISMES — SUBLIMATOR v28.0

| Anglicisme | Remplacement | Contexte d'usage |
|---|---|---|
| patents | brevets | propriété intellectuelle |
| ... | ... | ... |
```

**Règle de session** : Le fichier maître persiste entre les sessions. Si le fichier n'existe pas au démarrage, le Correcteur le crée avec le glossaire de base (Section 2.2).

### 2.3 Détection Syntaxique

- Anglicismes syntaxiques : "faire face à" → "confronter", "prendre une décision" → "décider"
- Néologismes : "solutionner" → "résoudre", "impacter" → "affecter"
- Formules théâtrales : "La physique ne se voit pas" → "Les processus physiques sont invisibles"

---

## 3. ENFORCEMENT DES SOURCES PRIMAIRES

### 3.1 LOI 1 révisée

**OBLIGATION D'IDENTIFIANT PRIMAIRE** : Tout fait substantiel DOIT avoir son identifiant vérifiable :

| Type | Identifiant requis |
|---|---|
| Article scientifique | DOI obligatoire |
| Brevet | Numéro de brevet + office |
| Rapport institutionnel | Numéro de rapport + institution |
| Étude universitaire | Auteurs + titre exact + année |
| Donnée statistique | Source + date de collecte |
| Citation directe | Contexte exact + source |

**Interdictions** :
- ❌ "Des études montrent" → ✅ "L'étude de X (DOI: ..., année)"
- ❌ "Un brevet récent" → ✅ "Le brevet US11260974B2 (déposant, année)"

### 3.2 Vérification pré-rédaction (PURGE PRÉVENTIVE)

Avant d'écrire, l'Écrivain DOIT :
1. Lister chaque fait F### de la matrice
2. Identifier le type de source requis pour chaque fait
3. Collecter l'identifiant primaire (DOI, brevet, titre d'étude, etc.)
4. **SI identifiant introuvable** → purger le fait de la matrice sectionnelle AVANT rédaction
5. Noter les faits purgés dans un registre `faits_purges_v{N}` avec raison de la purge
6. **Ne pas utiliser un fait sans identifiant dans le texte final**

**RÈGLE DE PURGE** : Tout fait classé "source non vérifiable" est RETIRÉ de la matrice avant la PHASE W (Écrivain). Le Critique ne pénalise PAS un fait absent — il pénalise un fait présent sans identifiant. Cette purge préventive empêche les boucles infinies sur données manquantes.

**Registre des purges** : `faits_purges_v{N}` liste les faits retirés avec :
- F### d'origine
- Affirmation
- Raison de la purge (DOI introuvable, brevet inaccessible, étude non localisée)
- Impact sur la section (mineur/majeur/critique)
- Si impact critique → signaler au Checkpoint #4

### 3.3 Module de vérification des brevets

Avant de citer un brevet, l'Écrivain DOIT :
1. Consulter le texte complet via `webfetch` sur patents.google.com ou USPTO
   - URL format : `https://patents.google.com/patent/{NUMERO}`
   - URL alternative : `https://api.uspto.gov/patents/{NUMERO}`
2. Vérifier que les revendications (claims) correspondent à l'affirmation faite
3. Si le brevet est mal interprété → corriger l'interprétation OU signaler la divergence

**FALLBACK SI ACCÈS IMPOSSIBLE** :
- Si patents.google.com bloque le scraping ou retourne un contenu incomplet :
  1. Tenter `websearch` avec la requête : `"{NUMERO} patent text claims"`
  2. Si un résumé fiable est trouvé (Google Patents snippet, USPTO abstract) → l'utiliser avec mention "résumé uniquement"
  3. Si aucun résumé fiable → purger le fait (Section 3.2) et noter dans le registre des purges
- **Ne jamais citer un brevet sans avoir consulté au minimum son résumé officiel**

**VÉRIFICATION DES CLAIMS** :
- Les claims numérotés (Claim 1, Claim 2...) sont la seule source autorisée pour décrire ce que le brevet "couvre"
- Le titre et l'abstract ne suffisent pas pour affirmer qu'un brevet "décrit X" — il faut citer le claim pertinent
- Si le claim ne correspond pas à l'affirmation → corriger OU purger

### 3.4 LOI 2 révisée

`06_SOURCES.md` DOIT inclure : identifiant primaire + URL active + date de consultation.

---

## 4. CHECKPOINT #4 : TEMPLATE DE SCORING

### 4.1 Structure du checkpoint

Le Checkpoint #4 présente à l'utilisateur :

1. **Scores du cycle multi-agent** : 5 critères avec seuil ≥4, statut ✓/✗
2. **Diagnostic du Critique** : 6 modules cognitifs avec commentaires
3. **Corrections du Correcteur** : anglicismes, formules théâtrales, typographie
4. **Données sectionnelles** : faits exploités, identifiants primaires, mots, transition
5. **Texte complet** de la section (version corrigée)
6. **Décision utilisateur** : ACCEPTER / RÉSERVES / MODIFICATIONS / REJETER

### 4.2 Logique de décision

| Scénario | Action |
|---|---|
| Moyenne ≥4 + ACCEPTER | Section validée → suivante |
| Moyenne ≥4 + RÉSERVES | Noter → suivante (traitées à l'assemblage) |
| Moyenne ≥4 + MODIFICATIONS | Appliquer → re-soumettre |
| Moyenne <4 (auto-rejet) | Retour Écrivain → itération N+1 |
| Itération 3 + moyenne <4 | RAPPORT D'ÉCHEC |

### 4.3 Rapport d'échec

Si 3 itérations sans succès : scores finaux, violations persistantes, diagnostic cause racine, recommandation (enrichir faits / reformuler / fusionner / abandonner).

---

## 5. NOMENCLATURE FICHIERS + AUTO-RENOMMAGE

### 5.1 Nouvelle structure de dossiers

```
investigations/YYYY-MM-DD_<sujet>/
├── 00A_DIAGNOSTIC.md
├── 00B_CENSUS.md
├── 01_DIGEST.md
├── 02_DIALECTIQUE.md
├── 03_ARCHITECTURE.md
├── 04_FACTCHECK.md
├── sections/
│   ├── 1_<titre>.md
│   └── ...
└── _assemblage/
    ├── draft_article.md
    └── audit_stylistique.md

articles/
└── YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md

sources/
└── YYYY-MM-DD_<sujet>_SOURCES.md
```

### 5.2 Règle d'auto-renommage

Après Checkpoint #5 validé :
1. Renommer `05_ARTICLE.md` → `YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md`
2. Migrer dans `/articles/`
3. Renommer `06_SOURCES.md` → `YYYY-MM-DD_<sujet>_SOURCES.md`
4. Migrer dans `/sources/`
5. Nettoyer le dossier investigations (supprimer les fichiers migrés)

### 5.3 Vérification pré-renommage

- [ ] Checkpoint #5 validé
- [ ] Audit stylistique §6.3 passé
- [ ] Quality Gate §7 complet
- [ ] Nomenclature conforme

---

## 6. CHANGEMENTS MAJEURS v27.1 → v28.0

| Version | Changements |
|---------|-----------|
| **v28.0** | **"The Multi-Agent Pipeline"** : Refonte architecturale complète. <br> - **Cycle multi-agent** : Écrivain → Critique → Correcteur → Arbitre (4 rôles distincts). <br> - **Scoring 5 critères** : Pureté lexicale, rigueur factuelle, cohérence thèse, style forensic, structure cognitive. <br> - **LOI 4 complète** : Doctrine Rédacteur Intraitable + glossaire anti-anglicismes vivant + détection syntaxique. <br> - **DOI enforcement** : Identifiants primaires obligatoires (DOI, brevets, titres d'études). <br> - **Module vérification brevets** : Consultation USPTO/patents.google avant citation. <br> - **Checkpoint #4 scoring** : Template de validation multi-agent avec scores, diagnostics, corrections. <br> - **Auto-renommage** : Migration automatique vers `/articles/` et `/sources/` après validation. <br> - **Rapport d'échec** : Si 3 itérations sans succès, diagnostic détaillé + recommandations. <br> - **Généricité totale** : Pipeline sujet-agnostique, adaptable à tout domaine (science, politique, histoire, économie, technologie). |
| **v27.1** | "Typographie & Qualité Éditoriale" : Correction tiret cadratin, blockquotes, calibrage 400-600 mots. |

---

## 10. FICHIERS À MODIFIER

| Fichier | Modifications |
|---------|---------------|
| `tools/prompts/systems/SUBLIMATOR_v27.0.md` | Renommer en `SUBLIMATOR_v28.0.md`. Réécrire §0.2, §5.1, §5.3 (LOI 1, 2, 4), §6.1, §6.4, §7, §11. |
| `investigations/2026-05-18_chemtrails/05_ARTICLE.md` | Renommer et migrer vers `articles/2026-05-18_HH-MM_chemtrails_ARTICLE.md` après régénération. |

---

## 8. GÉNÉRICITÉ ET ADAPTABILITÉ

### 8.1 Principe de sujet-agnosticisme

SUBLIMATOR v28.0 est conçu pour être **totalement indépendant du sujet**. Aucune règle, aucun seuil, aucun template ne contient de logique spécifique à un domaine.

**Règles de conception générique** :
- Les doctrines (Écrivain, Critique, Correcteur) s'appliquent à tout sujet : politique, science, histoire, économie, technologie
- Le glossaire anti-anglicismes est **universel** — il ne contient pas de termes spécifiques à un domaine
- Les 5 critères de scoring sont **transversaux** — ils évaluent la qualité d'écriture, pas le contenu thématique
- Le template de Checkpoint #4 est **identique** quel que soit le sujet

### 8.2 Adaptation contextuelle automatique

Le pipeline s'adapte au sujet via les mécanismes suivants :

**Type de source requis** : Déterminé dynamiquement par le type de faits dans la matrice :
- Sujet scientifique → DOI, études, rapports institutionnels
- Sujet juridique → numéros de loi, jurisprudences, codes
- Sujet historique → archives, témoignages, documents d'époque
- Sujet économique → données INSEE, rapports financiers, bilans
- Sujet technologique → patents, specs techniques, documentation

**Calibrage des sections** : Ajustable selon la complexité du sujet :
- Sujet technique dense → sections de 500-700 mots (plus de faits par section)
- Sujet narratif/historique → sections de 400-600 mots (équilibre faits/narration)
- Le calibrage par défaut (400-600) est un point de départ, pas une règle absolue

**Glossaire extensible par domaine** :
- Le glossaire de base couvre les anglicismes transversaux
- Si un sujet introduit du jargon technique anglais spécifique, le Correcteur l'ajoute au glossaire maître
- Le glossaire s'enrichit organiquement sans jamais se spécialiser au point d'exclure d'autres sujets

### 8.3 Interdictions de spécialisation

**Le pipeline NE DOIT PAS** :
- Créer de règles spécifiques à un sujet (ex: "pour les chemtrails, vérifier X")
- Modifier les seuils de scoring selon le sujet
- Ajouter des doctrines spécifiques à un domaine
- Hardcoder des URLs, des noms d'entités, ou des références dans le prompt système

**Le pipeline DOIT** :
- Découvrir le sujet via le Census (§1)
- Adapter la collecte de sources au type de faits identifiés
- Appliquer les mêmes LOIS 1-7 quel que soit le sujet
- Produire un article de qualité identique sur tout thème

---

## 9. RISQUES ET MITIGATIONS

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Prompt trop long (4 rôles + doctrines + glossaire) | Dépassement contexte | Utiliser des références modulaires, charger les doctrines via fichiers séparés |
| Scoring subjectif | Incohérence entre sections | Calibration initiale sur 1 section test, ajuster les seuils |
| Boucles infinies si Critique trop strict | Blocage pipeline | Max 3 itérations + rapport d'échec + décision utilisateur |
| Glossaire incomplet | Anglicismes non détectés | Glossaire vivant persisté dans `glossaire-anglicismes.md`, écriture automatique par le Correcteur |
| DOI introuvables pour certaines sources | Faits non vérifiables | **Purge préventive** avant rédaction (Section 3.2) — le fait est retiré AVANT que le Critique ne puisse pénaliser |
| Brevet inaccessible (scraping bloqué) | Claim non vérifié | Fallback websearch → résumé USPTO → si échec, purge du fait |
| Perte du glossaire entre sessions | Réapprentissage nécessaire | Fichier maître persisté dans `tools/prompts/systems/` |
