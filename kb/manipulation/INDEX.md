# MANIPULATION TECHNIQUES INDEX
# ==============================
# Reference index for Phase 0 - TEXT ANALYSIS
# Used by KERNEL.md §0bis

---

## CATÉGORIES

### 1. LOGICAL FALLACIES → kb/dsl/COGNITIVE_DSL.md

| Technique | Description |
|-----------|-------------|
| motte_and_bailey | Changement de position défensive |
| goalpost_shifting | Déplacer les critères |
| gish_gallop |Nombre d'arguments pour noyer le débat |
| whataboutism | "Et X alors ?" |
| tu_quoque | "Vous aussi !" |
| sea_lioning | Demande insistante de preuves |
| false_balance | Faux équilibre médiatique |
| loaded_question | Question piégée |
| concern_trolling | Fausse préoccupation |
| strawman | Argument falsifié |
| quote_mining | Citation hors contexte |

---

### 2. DEMAGOGY → kb/dsl/COGNITIVE_DSL.md

| Technique | Description |
|-----------|-------------|
| populist_framing | Cadrage populiste |
| us_vs_elites | Nous vs eux |
| miracle_solution | Solution miracle |
| free_lunch_promise | Promesse sans coût |
| scapegoating | Bouc émissaire |
| strategic_ambiguity | Ambigüité stratégique |

---

### 3. NUMERIC/LINGUISTIC → kb/dsl/COGNITIVE_DSL.md

| Technique | Description |
|-----------|-------------|
| weasel_words | Mots flous |
| percentage_without_base | Pourcentage sans base |
| card_stacking | Sélection de données |
| technobabble | Langage technique vide |

---

### 4. COERCION → kb/dsl/THREATS.md

| Technique | Description |
|-----------|-------------|
| BIDERMAN_1_isolation | Isolement |
| BIDERMAN_2_monopoly | Monopole perceptuel |
| BIDERMAN_3_exhaustion | Épuisement |
| BIDERMAN_4_threats | Menaces |
| BIDERMAN_5_indulgences | Indults |
| BIDERMAN_6_omnipotence | Omnipotence |
| BIDERMAN_7_degradation | Dégradation |
| BIDERMAN_8_absurd | Absurdité |
| SHOCK | Doctrine du choc |
| GASLIGHTING | Manipulation de la réalité |
| INFODEMIC | Saturation informationnelle |
| LAWFARE | Usage juridique comme arme |
| FALSE_FLAGS | Fausses opérations |

---

### 5. PSYCHOLOGICAL → kb/dsl/THREATS.md

| Technique | Description |
|-----------|-------------|
| NUDGING | Incitation douce |
| CIALDINI_reciprocity | Reciprocité |
| CIALDINI_commitment | Engagement |
| CIALDINI_social_proof | Preuve sociale |
| CIALDINI_authority | Autorité |
| CIALDINI_liking | Sympathie |
| CIALDINI_scarcity | Rareté |
| CIALDINI_unity | Unité |
| NLP | Programmation neuro-linguistique |
| EMOTIONAL | Manipulation émotionnelle |
| DIGITAL_DARK | Dark patterns UX |

---

### 6. RHETORICAL → kb/dsl/PATTERNS.md

| Technique | Description |
|-----------|-------------|
| tone_policing | Attaquer le ton |
| infantilization | Traitement infantillant |
| false_equivalence | Équivalence fausse |
| virtue_signaling | Signaux de vertu |
| ad_hominem | Attaque personnelle |
| false_authority | Fausse autorité |
| DARVO | Deny, Attack, Reverse Victim & Offender |

---

### 7. INFORMATION → kb/patterns/CLUSTER_ICEBERG.md

| Technique | Description |
|-----------|-------------|
| cherry_picking | Sélection de données |
| selective_evidence | Preuve sélective |
| memory_hole | Trou de mémoire |
| context_stripping | Stripping du contexte |
| inconvenient_truth_burial | Enfouissement vérité gênante |

---

### 8. SEMANTIC → kb/patterns/CLUSTER_FRAMING.md

| Technique | Description |
|-----------|-------------|
| euphemisms | Euphémismes |
| loaded_language | Langage chargé |
| redefinition | Redéfinition |
| inversion | Inversion victim/perpétrateur |

---

### 9. WAR PROPAGANDA → kb/patterns/CLUSTER_WAR.md

| Technique | Description |
|-----------|-------------|
| threat_inflation | Inflation des menaces |
| dehumanization | Déshumanisation |
| enemy_morphing | L'ennemi change |
| convenient_timing | Timing arrangeant |
| emotion_over_evidence | Émotion plutôt que preuve |

---

### 10. GASLIGHTING → kb/patterns/CLUSTER_GASLIGHTING.md

| Technique | Description |
|-----------|-------------|
| denial | Négation |
| contradiction | Contradiction |
| pathologizing | Pathologisation |
| memory_erasure | Effacement de mémoire |

---

## MAPPING POUR PHASE 0

```
MANDATORY_CHECKS:
  - logical_fallacies: kb/dsl/COGNITIVE_DSL.md
  - demagogy: kb/dsl/COGNITIVE_DSL.md
  - numeric: kb/dsl/COGNITIVE_DSL.md
  - coercion: kb/dsl/THREATS.md
  - psychological: kb/dsl/THREATS.md
  - rhetorical: kb/dsl/PATTERNS.md
  - information: kb/patterns/CLUSTER_ICEBERG.md
  - semantic: kb/patterns/CLUSTER_FRAMING.md
  - war: kb/patterns/CLUSTER_WAR.md
  - gaslighting: kb/patterns/CLUSTER_GASLIGHTING.md
```

---

## OUTPUT FORMAT

```
MANIPULATION_REPORT:
├── TECHNIQUES_DETECTED: [technique:confiance]
├── SEMANTIC_FIELDS: {champ: [mots]}
├── CLAIMS_IMPLICITES: [3-5]
├── SPEAKER_PROFILE: {ton, cible, but}
├── VERIFICATION_PRIORITIES: [quoi vérifier]
└── QUERY_GUIDANCE: [comment techniques guident recherches]
```
