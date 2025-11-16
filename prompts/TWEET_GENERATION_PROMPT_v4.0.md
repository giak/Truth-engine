# PROMPT GÉNÉRATION TWEET — Truth Engine v4.0 CLI

**Date:** 2025-11-13
**Philosophie:** Guider sans contraindre
**Source:** Analyse 161 tweets (103→2 + 250→104) + distillation patterns v3.1
**Évolution:** Prompt Web 10 lignes → v4.0 30 lignes (vs v3.0 693 lignes)

---

## I. LE PROMPT

```markdown
Brainstorm deeper et ultrathink.

Écris une analyse à charge, pamphlétaire, pédagogique et avec panache.
Transforme l'investigation Truth Engine en tweet long format (compte premium, sans thread).
Double-check : honnêteté absolue, vérité, fact-check tout.
On s'adresse aux citoyens, pas aux experts.

──────────────────────────────
PRINCIPES TRUTH ENGINE (non-négociables)

1. Chiffres exacts > adjectifs vagues
   Noms complets, montants précis, dates. JAMAIS "beaucoup" → "187 000 €", "13 fév. 2024"

2. Honnêteté brutale > consensus confortable
   Zéro sycophancy, gaps documentés ("règlement introuvable après 6 recherches"), incertitude assumée

3. Pédagogie citoyenne > jargon technique
   Acronymes traduits première occurrence (EDI → Indice Diversité Épistémique), concepts explicités

4. Frappe fort dès l'intro, formule finale mémorable
   Hook immédiat qui accroche, conclusion qui claque et reste en tête

5. Qui profite ? Toujours chercher
   Bénéficiaires visibles, shadow, cachés. Qui gagne réellement derrière le discours ?

6. Impact double : citoyen + gouvernance
   Conséquences pour les deux. Jamais une seule perspective.

7. Ton mordant, verbes d'action
   Métaphores percutantes ("théâtre d'ombres", "pipeline marketing"), verbes qui frappent

──────────────────────────────
FORMAT DE RENDU

Structure naturelle : frappe dès l'intro, développe avec rigueur, conclus avec impact.
Mise en page : émoji titre unique, gras pour souligner (pas décorer), formule finale mémorable.
Citations : « guillemets français ». Listes : → ou –

RENDU — Version finale prête à poster, sans préambule, sans meta-commentaires.
```

---

## II. GENÈSE & MÉTHODOLOGIE

### Contexte

**Problème initial:**
- Prompt Web (10 lignes) fonctionne bien sur interfaces web Claude
- Prompt technique v3.0 (693 lignes) trop détaillé, contraint le LLM
- Besoin : distiller l'essence de 161 tweets analysés en prompt **guidant sans contraindre**

**Corpus analysé:**
- Session 1 (v1.0→v3.0) : Tweets 103→2 (102 tweets exhaustifs)
- Session 2 (v3.1) : Tweets 250→104 (~59 échantillons stratégiques, focus "les plus aboutis")
- **Total : ~161 tweets sur 7 ans d'évolution**

**Documentation référence:**
- [TWEET_PATTERNS_ADVANCED.md](TWEET_PATTERNS_ADVANCED.md) (47KB, patterns ultra-matures)
- [TWEET_GENERATION_PROMPT_v3.1_UPDATE.md](TWEET_GENERATION_PROMPT_v3.1_UPDATE.md) (479 lignes, intégration patterns avancés)
- [TWEET_GENERATION_PROMPT.md](TWEET_GENERATION_PROMPT.md) (693 lignes, prompt technique v3.0)

### Processus de Conception (Brainstorming Socratique)

**Phase 1 - Clarification philosophie:**
- **Q:** Guider vs contraindre - quelle approche ?
- **R:** Prompt court (style Web) avec principes clés, pas contraintes rigides
- **Choix:** Option A "prompt court" enrichi légèrement

**Phase 2 - Identification besoins:**
- **Q:** Qu'est-ce qui manque dans sorties CLI vs Web ?
- **R:** Guidance structurelle légère
- **Choix:** Option A "guidance structurelle" (pas patterns spécifiques, pas exemples, pas critères mesurables)

**Phase 3 - Style de guidance:**
- **Q:** Comment formuler guidance ?
- **R:** Style principes généraux (philosophie > recette)
- **Choix:** Option C "principes généraux"

**Phase 4 - Architecture:**
- **Q:** Comment organiser principes ?
- **R:** Liste courte lois universelles (3-5 max)
- **Choix:** Option D "principes fondamentaux"

**Phase 5 - Hiérarchie principes:**
- **Q:** Quels sont les 3-5 principes VRAIMENT non-négociables ?
- **R:** Classement utilisateur : 1.Précision factuelle → 4.Honnêteté brutale → 3.Pédagogie → 2.Percutance → 6.Qui profite → 7.Double conséquence → 5.Ton pamphlétaire
- **Choix:** Garder les 7 (tous utiles malgré hiérarchie)

**Phase 6 - Périmètre:**
- **Q:** Top 3, Top 5, ou tous les 7 ?
- **R:** Tous les 7 restent légers comme principes
- **Choix:** Option C "Tous les 7"

**Phase 7 - Formulation:**
- **Q:** Style télégraphique, philosophique, maximes, ou mix ?
- **R:** Mix A (télégraphique) + C (maximes percutantes)
- **Choix:** Concision + mémorabilité maximales

**Phase 8 - Architecture globale:**
- **Q:** Fusion, enrichissement structuré, addendum, ou deux versions ?
- **R:** Enrichissement structuré (Intro → Principes → Output)
- **Choix:** Option B "structure tripartite"

**Phase 9 - Densité principes:**
- **Q:** Ultra-compact, compact avec exemples, ou formule+détail ?
- **R:** Compact avec exemples courts (2 lignes)
- **Choix:** Option B (équilibre guidance/liberté)

**Phase 10 - Section Output:**
- **Q:** Garder formulation actuelle, ajouter guidance, mentionner archétypes, ou ultra-minimaliste ?
- **R:** Ajouter guidance structurelle légère (3-4 lignes max)
- **Choix:** Option B

---

## III. ARCHITECTURE & RATIONALE

### Structure Tripartite

```
┌───────────────────────────────────────────┐
│ [INTRO] Contexte & Intention             │
│ • Ton (pamphlétaire, pédagogique, panache)│
│ • Public cible (citoyens, pas experts)   │
│ • Honnêteté absolue, fact-check          │
├───────────────────────────────────────────┤
│ [CŒUR] 7 Principes Truth Engine          │
│ 1. Précision factuelle (RIGUEUR)         │
│ 4. Honnêteté brutale (INTÉGRITÉ)         │
│ 3. Pédagogie citoyenne (ACCESSIBILITÉ)   │
│ 2. Percutance narrative (IMPACT)         │
│ 6. Qui profite ? (ANALYSE)               │
│ 7. Double conséquence (DIALECTIQUE)      │
│ 5. Ton mordant (STYLE)                   │
├───────────────────────────────────────────┤
│ [OUTPUT] Format de rendu                 │
│ • Structure naturelle suggérée           │
│ • Mise en page guidée (émoji, gras)      │
│ • Rendu final sans meta-commentaires     │
└───────────────────────────────────────────┘
```

### Hiérarchie des Principes

**Ordre utilisateur (importance décroissante):**
1. **Précision factuelle** — Base de la crédibilité
4. **Honnêteté brutale** — Intégrité épistémique
3. **Pédagogie citoyenne** — Accessibilité du propos
2. **Percutance narrative** — Impact mémoriel
6. **Qui profite ?** — Analyse structurelle
7. **Double conséquence** — Dialectique complète
5. **Ton pamphlétaire** — Style distinctif

**Rationale ordre dans prompt:**
Suit la hiérarchie utilisateur = signale au LLM les priorités relatives tout en gardant les 7.

### Choix de Formulation

**Style retenu : Mix télégraphique + maximes**

**Avantages:**
- **Mémorabilité** : Formules courtes type "Chiffres > adjectifs" restent en tête
- **Actionnabilité** : Exemples concrets ("187 000 €", "13 fév. 2024") donnent repères
- **Non-contraignant** : 2 lignes par principe = guidance légère, pas recette rigide
- **Concision** : 14 lignes pour 7 principes = densité maximale

**Contre-exemples rejetés:**
- ❌ Phrases complètes philosophiques : trop verbeux
- ❌ Maximes seules sans exemples : trop abstrait
- ❌ Format détaillé avec sous-sections : trop contraignant

---

## IV. DIFFÉRENCES AVEC VERSIONS PRÉCÉDENTES

### vs Prompt Web Original (10 lignes)

**Conservé:**
- ✅ Ton (pamphlétaire, pédagogique, panache)
- ✅ Public cible (citoyens, accessibilité)
- ✅ Anti-patterns (pas de sycophancy, honnêteté absolue)
- ✅ Output format (version finale, sans préambule)
- ✅ Mise en page (émojis/gras avec parcimonie)

**Ajouté:**
- ✅ **7 Principes Truth Engine** distillés de 161 tweets
- ✅ **Guidance structurelle légère** (intro, développement, conclusion)
- ✅ **Hiérarchie explicite** (précision > honnêteté > pédagogie...)
- ✅ **Exemples concrets** (formats dates, montants, citations)

**Longueur:** 10 → 30 lignes (+200%, reste léger)

### vs Prompt Technique v3.0 (693 lignes)

**Philosophie inverse:**
- v3.0 : **Prescriptif**, détaille tous les patterns, types A-F, anti-patterns, checklist exhaustive
- v4.0 : **Suggestif**, principes universels, liberté d'exécution

**Contenu:**
- v3.0 : 5 types tweets (A-E), 185 concepts vocabulaire, 40 formules choc, structures variantes Type D, anti-patterns exhaustifs
- v4.0 : 7 principes transversaux + guidance structurelle minimale

**Usage:**
- v3.0 : Référence technique pour comprendre corpus, documentation exhaustive
- v4.0 : Prompt opérationnel quotidien, guider sans contraindre

**Complémentarité:**
- v3.0 = **Documentation** (pour humains analysant tweets)
- v4.0 = **Prompt** (pour LLM générant tweets)

### vs Update v3.1 (479 lignes)

**v3.1 = Intégration patterns avancés:**
- 7 nouveaux patterns obligatoires (ContreArgumentLoyal, Définitions inline, Double conséquence, MYTHES VS FAITS, Payoff, Règle X-Y-Z, Séparateurs variantes)
- 10 patterns narratifs avancés
- Type F (rapport juridique ultra-long)
- Tag APEX
- Checklist étendue

**v4.0 = Distillation essence:**
- Capture **philosophie** des patterns v3.1 sans les détailler
- Ex: "Double conséquence" devient principe #7 "Impact double : citoyen + gouvernance"
- Ex: "Qui profite?" devient principe #6 (synthèse patterns ICEBERG, MONEY, cui bono)

**Relation:**
- v3.1 = Mine de patterns spécifiques
- v4.0 = Principes universels extraits de v3.1

---

## V. PATTERNS v3.1 INTÉGRÉS (Implicites)

Le prompt v4.0 **ne liste pas** les patterns v3.1 explicitement, mais les **implique** via les 7 principes :

### Principe #1 (Précision factuelle) intègre :
- ✅ Définitions inline acronymes
- ✅ Facts ultra-précis (noms, montants, dates)
- ✅ Citations « guillemets français »

### Principe #2 (Honnêteté brutale) intègre :
- ✅ Gaps documentés
- ✅ Zéro sycophancy
- ✅ Incertitude assumée

### Principe #3 (Pédagogie citoyenne) intègre :
- ✅ Acronymes traduits première occurrence
- ✅ Concepts explicités
- ✅ Éviter jargon

### Principe #4 (Percutance narrative) intègre :
- ✅ Hook immédiat
- ✅ Formule finale mémorable
- ✅ Structure naturelle (intro → développement → conclusion)

### Principe #5 (Qui profite ?) intègre :
- ✅ Pattern MONEY (cui bono)
- ✅ Pattern ICEBERG (bénéficiaires cachés ×1, ×10, ×100)
- ✅ Wolves hunting

### Principe #6 (Impact double) intègre :
- ✅ Pattern Double Conséquence v3.1
- ✅ Dialectique citoyen + gouvernance systématique

### Principe #7 (Ton mordant) intègre :
- ✅ Verbes d'action pamphlétaires
- ✅ Métaphores percutantes
- ✅ Formules choc

### Patterns v3.1 NON intégrés (par choix) :
- ❌ ContreArgumentLoyal (trop spécifique)
- ❌ MYTHES VS FAITS (structure optionnelle)
- ❌ Payoff/Verdict (émerge naturellement de principe #4)
- ❌ Règle X-Y-Z (mnémotechnique optionnel)
- ❌ Tag APEX (méta-classification)
- ❌ Type F structure I-XX (cas ultra-rare 5000-15000 mots)
- ❌ Séparateurs variantes (détail technique)

**Rationale :** Ces patterns avancés sont **optionnels** et émergent naturellement quand pertinent. Les inclure rigidifierait le prompt.

---

## VI. USAGE & INTÉGRATION

### Usage Actuel (CLI)

**Commande type :**
```bash
claude-code "$(cat prompts/TWEET_GENERATION_PROMPT_v4.0.md | grep -A 50 '## I. LE PROMPT' | tail -n +3 | head -n 30)

[Investigation Truth Engine I0/I1 output]"
```

**Ou copier-coller direct** du prompt dans interface Claude Code.

### Intégration Future (Truth Engine)

**Option A - Commande dédiée :**
```bash
truth-engine tweet <investigation-file>
# → Charge automatiquement prompt v4.0 + investigation → génère tweet
```

**Option B - Flag generation :**
```bash
truth-engine investigate "Mercosur" --output-tweet
# → Investigation + génération tweet en une passe
```

**Option C - Post-processing :**
```yaml
# system.md extension
post_processing:
  - type: tweet_generation
    prompt: prompts/TWEET_GENERATION_PROMPT_v4.0.md
    trigger: manual | auto (si requested in query)
```

**Option D - Skill MCP :**
```python
# MCP server mnemolite
@server.call_tool()
async def generate_tweet(investigation_md: str) -> TweetResponse:
    """Generate tweet from Truth Engine investigation using v4.0 prompt."""
    prompt = load_prompt("TWEET_GENERATION_PROMPT_v4.0.md")
    return await llm.generate(prompt + investigation_md)
```

---

## VII. AMÉLIORATION CONTINUE

### Métriques à Suivre

**Qualité output :**
- ✅ Présence ≥3 facts ultra-précis (dates, montants, noms)
- ✅ Zéro sycophancy détectée
- ✅ Acronymes traduits première occurrence
- ✅ Hook immédiat + formule finale mémorable
- ✅ Analyse cui bono présente
- ✅ Double conséquence citoyen + gouvernance

**Feedback utilisateur :**
- Gap entre sorties CLI v4.0 vs Web (prompt original 10 lignes)
- Patterns v3.1 manquants dans outputs (ContreArgumentLoyal, MYTHES VS FAITS, etc.)
- Rigidité perçue ou liberté excessive

### Évolution Possible

**v4.1 - Ajustements mineurs :**
- Reformulation principes si ambiguïté détectée
- Ajout 1-2 exemples si principe mal compris
- Réordonnancement si hiérarchie sous-optimale

**v4.2 - Enrichissement ciblé :**
- Mention suggestive patterns v3.1 optionnels ("Si pertinent : ContreArgumentLoyal, MYTHES VS FAITS...")
- Guidance longueur (compact <500 mots vs long 1500-5000 mots)

**v4.5 - Stratification :**
- Prompt court (v4.0 actuel) pour cas standard
- Prompt étendu (v4.0 + patterns avancés suggérés) pour Type D/F complexes

**v5.0 - Intégration système :**
- Prompt intégré nativement à Truth Engine
- Auto-sélection prompt court/étendu selon complexité investigation (SIMPLE/MEDIUM/COMPLEX/APEX)

---

## VIII. VALIDATION & TESTS

### Test A - Comparaison Web vs CLI

**Protocole :**
1. Prendre 3 investigations Truth Engine récentes (SIMPLE, MEDIUM, COMPLEX)
2. Générer tweet via :
   - Interface Web Claude + prompt original 10 lignes
   - CLI Claude Code + prompt v4.0
3. Comparer qualité (checklist 6 métriques ci-dessus)

**Succès si :** Output CLI v4.0 ≥ 5/6 métriques validées ET comparable qualité Web

### Test B - Patterns v3.1 Émergence

**Protocole :**
1. Générer 10 tweets CLI v4.0 sur investigations variées
2. Identifier patterns v3.1 présents (ContreArgumentLoyal, MYTHES VS FAITS, Double Conséquence, etc.)
3. Calculer taux émergence naturelle vs fréquence corpus (tweets 250→104)

**Succès si :** Patterns fréquents corpus (>30%) émergent spontanément dans ≥50% outputs CLI

### Test C - Liberté vs Qualité

**Protocole :**
1. Générer 5 tweets CLI v4.0 sur même investigation
2. Mesurer diversité outputs (structure, longueur, patterns utilisés)
3. Valider qualité moyenne (checklist 6 métriques)

**Succès si :** Diversité élevée (≥4/5 outputs structurellement différents) ET qualité moyenne ≥ 4/6 métriques

---

## IX. ANNEXES

### Prompt Original Web (Référence)

```markdown
Brainstorm deeper et ultrathink.
Écrit et mature une réponse à charge, pamphlétaire, pédagogique et avec panache.
Écris-moi un tweet reprenant l'ensemble de la conversation (compte premium, sans thread), type note stratégique/journalistique.
Double check, pas de sycophancy/flagornerie, honnêteté absolue, vérité, fact-check tout.
Évitez d'utiliser des termes techniques spécifiques tels que "Truth engine" : les expliquer en langage courant et accessible.
On s'adresse aux citoyens, il faut être pédagogique.
Mise en page lisible (émojis et gras avec parcimonie, ils doivent souligner ce qui est important, améliorer la lecture).
RENDU — Version finale prête à poster, sans préambule, sans meta-commentaires.
```

### Références Corpus

**Tweets analysés (161 total) :**
- Session 1 (v1.0→v3.0) : 103→2 (102 tweets exhaustifs)
- Session 2 (v3.1) : 250→104 (~59 échantillons stratégiques)

**Documentation générée :**
1. [TWEET_ANALYSIS_FINAL.md](TWEET_ANALYSIS_FINAL.md) (682 lignes) — Synthèse première session
2. [TWEET_PATTERNS_ADVANCED.md](TWEET_PATTERNS_ADVANCED.md) (671 lignes, 47KB) — Patterns ultra-matures 250→104
3. [TWEET_GENERATION_PROMPT_v3.1_UPDATE.md](TWEET_GENERATION_PROMPT_v3.1_UPDATE.md) (479 lignes) — Intégration patterns avancés
4. [TWEET_GENERATION_PROMPT.md](TWEET_GENERATION_PROMPT.md) (693 lignes) — Prompt technique v3.0

**Échantillons tweets clés :**
- Tweet 250 : Type E compact abouti (politique économique)
- Tweet 239 : Type F ultra-long 609 lignes (cyberharcèlement juridique)
- Tweet 234 : ContreArgumentLoyal exemplaire
- Tweet 224 : Structure tripartite "Les faits + Comment ça marche + Qui profite"
- Tweet 210 : Diagnostic temporel 1992→2024

---

## X. CHANGELOG

**v4.0 (2025-11-13) — Initial Release**
- ✅ Distillation 161 tweets → 7 principes universels
- ✅ Structure tripartite (Intro → Principes → Output)
- ✅ Philosophie "guider sans contraindre"
- ✅ Format compact avec exemples (30 lignes vs 693 v3.0)
- ✅ Hiérarchie principes selon priorités utilisateur
- ✅ Intégration implicite patterns v3.1 essentiels
- ✅ Documentation complète genèse et rationale

**v4.1 (TBD) — Ajustements post-validation**
- Attente tests A/B/C
- Feedback utilisateur CLI vs Web
- Reformulations si principes ambigus

---

**Statut :** v4.0 DRAFT — En attente validation terrain
**Auteur :** Conception collaborative (brainstorming socratique utilisateur + Claude Code)
**License :** Projet Truth Engine (open development)
