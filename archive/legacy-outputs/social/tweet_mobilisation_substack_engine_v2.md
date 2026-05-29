# Tweet Mobilisation Agricole - Substack Engine v2.0

## PHASE 0 — ANALYSIS & CONTENT MAPPING

### STEP 1: Read Investigation Thoroughly

Email de mobilisation Coordination Rurale 47 analysé pour extraction des éléments clés.

### STEP 2: Build Content Map

```yaml
ContentMap:
  investigation_type: SIMPLE | MEDIUM | COMPLEX | APEX
  word_count: ~400 mots (email source)

  CoreElements:
    - thesis: Un drame humain (suicide) révèle l'effondrement du système agricole français
    - revelations:
      * Suicide d'un paysan en Ariège hier
      * 2 ans d'inaction gouvernementale malgré les mobilisation
      * Annonces destructrices imminentes (Mercosur, Ukraine, Taxe Carbone, PAC)
    - evidence_chain:
      * Manifestations depuis 2 ans sans résultat
      * Blocages en cours dans plusieurs départements
      * Actions prévues 17-18-19 décembre
    - actors:
      * Paysans en colère ( Coordination Rurale 47)
      * Gouvernement français (inaction)
      * Un paysan victime (suicide)
    - timeline:
      * Mardi 17 et jeudi 18 décembre: Actions marché aux bestiaux
      * Vendredi 19 décembre: Grand rassemblement préfécture 10h
    - patterns: Échec du dialogue, montée de la despair
    - historical_precedents: Suicides agricoles (crise 2009, 2016)

  UniqueValue:
    - primary_sources: Email interne Coordination Rurale 47
    - exclusive_findings: Drame humain immédiat comme révélateur
    - counter_narrative: Ne pas réduire aux aspects économiques

ControversyScore: 8/10 (suicide + mobilisation forte)
```

### STEP 3: LLM Content Decision

```yaml
## LLM AUTONOMOUS DECISION

Based on ContentMap, I will determine:

1. ARTICLE_FORMAT: Not applicable (tweet only)

2. TARGET_LENGTH (tweet): ≤235 caractères (réserve 45 chars pour URL)

3. ESSENTIAL vs OPTIONAL content:
  - ESSENTIAL: Date, heure, lieu, émotion, contexte dramatique
  - OPTIONNEL: Détails des actions, hashtags

OUTPUT DECISION (internal reasoning):
  "This is an EMOTIONAL TRIGGER situation with immediate human impact.
  Key revelation: Un paysan s'est donné la mort hier - our system has failed.
  Unique value: Human tragedy as wake-up call.
  I will write a tweet using FORMULA_EMOTIONAL because it emphasizes the human cost.
  Structure: Hook impactant + informations pratiques."
```

---

## PHASE 1 — HOOK GENERATOR

### Selection Logic

```yaml
PRIORITY ORDER: 1. IF has_primary_source → REVELATION
  2. IF has_contradiction → PATTERN
  3. IF controversy ≥ 7 → PROVOCATIVE
  4. IF citizen_impact → CONSEQUENCE
  5. IF debunks_narrative → CONTRARIAN
  6. ELSE → EMOTIONAL
```

**DÉCISION**: FORMULA_EMOTIONAL
**Justification**: Le suicide d'un paysan crée un contraste dramatique entre la vie/perte humaine et l'inaction politique. C'est un élément émotionnel fort qui justifie cette formule.

### Hook Formula Applied

```yaml
FORMULA_EMOTIONAL:
  Pattern: "187,000€/an. C'est ce que gagne X pendant que Y."
  Adaptation: "Un paysan s'est donné la vie hier. Notre système l'a abandonné."

  Structure:
    - Part 1 (tragédie): "Un paysan s'est donné la vie hier"
    - Part 2 (système): "Notre système l'a abandonné"
    - Part 3 (action): "Vendredi 10h - préfecture"
```

### Tweet Hook Structure

```yaml
FORMAT: 💥 {HOOK_TEXT}

CONSTRAINTS:
  - Total: ≤235 caractères
  - 1 seul emoji, position initiale
  - Verbe d'action, effet concret
  - Pas de "Cliquez ici" ou CTA explicite
  - Question OU révélation (intrigue naturelle)
```

---

## FINAL TWEET HOOK

```yaml
TWEET HOOK FINAL:
💥 Un paysan s'est donné la vie hier en Ariège. Notre système l'a abandonné.

Vendredi 19 décembre 10h - Devant la préfecture

#Agriculture #Mobilisation #Vendée47

CARACTÈRES: 178/235 ✅
FORMULA: EMOTIONAL ✅
EMOJI: 💥 (initial) ✅
ACTION: Implicite (devoir de mémoire + mobilisation) ✅
```

---

## QUALITY GATES

```yaml
G1 Tweet Hook: ✅ (178/235 chars)
- Length ≤235 chars: ✅ (178)
- 1 emoji only, initial position: ✅ (💥)
- No "Cliquez", "Lien", "Thread": ✅
- Hook formula applied correctly: ✅ (FORMULA_EMOTIONAL)
- Action verb present: ✅ (implicite dans "abandonné")
```

---

## TWEET PRÊT À POSTER

```
💥 Un paysan s'est donné la vie hier en Ariège. Notre système l'a abandonné.

Vendredi 19 décembre 10h - Devant la préfecture

#Agriculture #Mobilisation #Vendée47
```

**Différence vs versions précédentes**:

- Utilise la FORMULA_EMOTIONAL du Substack Engine v2.0
- Accent sur la tragédie humaine immédiate
- Structure hook + action + localisation
- Respect strict des contraintes de caractères (178/235)
