# INVESTIGATOR v2.0 - Améliorations Clés

## Ce qui a changé de v1.0 à v2.0

### 1. Noyau Cognitif (ΩI*)

**v1.0:** Pas de définition du "self"
**v2.0:** 
```
ΩI* = cognitive_kernel ⟶ (
    ontology:    {entity, event, evidence, claim, source, relationship, timeline}
    epistemology: verify ⨁ corroborate ⨁ falsify ⨁ triangulate
    axiology:    truth > speed | accuracy > completeness | source > inference
)
```

**Impact:** Le LLM comprend SON identité et SES valeurs.

---

### 2. Heuristiques d'Investigation (H)

**v1.0:** Aucune
**v2.0:**
```
H = {
    cui_bono, follow_money, triangulate, 
    temporal_co, source_trace, contradiction, 
    pattern_hunt, gap_detect
}
```

**Impact:** Raccourcis cognitifs automatiques - "Qui profite?", "Follow the money", etc.

---

### 3. Méta-cognition (MC)

**v1.0:** Aucune
**v2.0:**
```
MC.monitor = (δΘ, δΦ, δΞ)  // Dérives
MC.adjust = recalibrage automatique
MC.reflect = "Qu'est-ce que je manque?"
```

**Impact:** Auto-évaluation et ajustement pendant l'investigation.

---

### 4. Machine à États

**v1.0:** Pas de transitions définies
**v2.0:**
```
ΩI.states = {dormant, parsing, searching, verifying, synthesizing, reporting, stuck}
ΩI.transitions = {transitions conditionnelles}
```

**Impact:** Comportement adaptatif selon l'état cognitif.

---

### 5. Internalisation des Symboles

**v1.0:** Symboles comme notation
**v2.0:** Symboles comme "cognitive modes"

| Symbol | Internal Thought |
|--------|-----------------|
| Θ | "I track hypotheses" |
| Φ | "I evaluate credibility" |
| Γ | "I map relationships" |
| MC | "I reflect on my process" |

**Impact:** Le LLM "devient" chaque composant.

---

### 6. Compression de Sortie

**v1.0:** Aucune instruction
**v2.0:**
```
compress = {remove_redundancy, abstract_patterns, use_tables, prefer_symbols}
```

**Impact:** Sorties plus denses et efficaces.

---

## Token Economy

| Métrique | v1.0 | v2.0 |
|----------|------|------|
| Taille prompt | ~2000 tokens | ~1800 tokens |
| Richesse cognitive | Basse | Haute |
| Auto-régulation | Non | Oui |
| Heuristiques | 0 | 8 |
| États cognitifs | 0 | 7 |

---

## Test Comparatif

### Simulation d'Input Identique

**Input:** "Tweet: Le PDG de TechCorp achète villa Monaco 15M€ après 200 licenciements"

**v1.0 Response:**
- Parse basique
- Requêtes générées
- Pas de méta-réflexion

**v2.0 Response:**
- Parse herméneutique (littéral/contextuel/implicite)
- Application H.cui_bono ("Qui profite des licenciements?")
- États affichés: [ΩI: parsing] → [ΩI: searching]
- MC.reflect: "Que manque-t-il?"
- Compression de sortie

---

## Recommandations d'Usage

1. **Toujours inclure les state indicators** dans la sortie
2. **Appliquer les heuristiques automatiquement** selon le contexte
3. **Utiliser MC.reflect** quand l'investigation stagne
4. **Afficher le symbole actif** pour montrer le mode cognitif

---

## Prochaines Améliorations Possibles

1. **Ajouter un glossaire symbolique** en fin de prompt
2. **Templates de raisonnement** par type d'enquête
3. **Intégration Chain-of-Thought** dans les hooks
4. **Feedback loop** utilisateur → MC.adjust
