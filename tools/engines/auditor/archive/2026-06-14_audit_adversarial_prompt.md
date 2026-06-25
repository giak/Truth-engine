# PROMPT D'AUDIT ADVERSARIEL UNIVERSEL v4.1

## Architecture : 4 Regards + Domaines Critiques

Ce prompt audite n'importe quel texte long format en dispatchant chaque phase vers un LLM local différent (Ollama). L'orchestrateur lit ce fichier, identifie les sections `BLOCK` et `SHARED`, et les envoie au modèle spécifié dans l'en-tête.

### ⚠️ Limitation et principe

Ce prompt s'exécute sur plusieurs modèles locaux via Ollama. Les 4 Regards sont dispatchés vers des modèles d'architectures différentes (Qwen, GLM, Granite, Phi, Llama). Cette **diversité architecturale** est essentielle : l'accord entre modèles de familles différentes est une vraie cross-validation, contrairement à l'accord entre prompts du même modèle.

### Phases

1. **Phase 0** — Métatexte (extraire métadonnées, configurer l'audit)
2. **Phase 1** — Cold Read (impressions brutes)
3. **Phase 2** — 4 Regards (chaque regard = un modèle différent)
4. **Phase 3** — Deep Dives (si domaines critiques identifiés en Phase 0)
5. **Phase 4** — Synthèse (cross-examination + verdict)

---

## SHARED:taxonomy

### Codes des problèmes

Chaque critique DOIT utiliser un code parmi :

| Code | Nature | Définition |
|------|--------|------------|
| FACT | Assertion (possiblement) inexacte | Vérifier chiffre, date, nom, source |
| LACUNA | Omission significative | Un élément manquant change la compréhension ou la crédibilité |
| SURETAB | Sur-établissement rhétorique | L'affirmation dépasse ce que les preuves présentées permettent |
| CONTRA | Contradiction interne | Deux passages disent des choses incompatibles |
| BIAIS | Biais de sélection ou de cadrage | L'échantillon de preuves favorise indûment la thèse |
| LOGIC | Faille logique | *Non sequitur*, circularité, faux dilemme |
| GLISS | Glissement sémantique | Un terme change de sens entre deux occurrences |
| PRAG | Effet pragmatique non intentionnel | Le texte va produire un effet inverse du recherché |

---

## SHARED:rules

### Règles transversales

Ces règles s'appliquent principalement à la Phase 2 (Regards 1-4). Si tu es Phase 0, Phase 1 ou Phase 4, ignore ce qui ne te concerne pas — tu as tes propres instructions.

**R1. Indépendance.** (Phase 2 uniquement) Tu fais une lecture fraîche de l'article. Tu n'as AUCUNE connaissance des autres regards.

**R2. CANNOT_ASSESS.** Si tu ne peux PAS évaluer un aspect (info insuffisante, domaine hors compétence), marque explicitement « CANNOT_ASSESS : [raison] ». Ne force pas un verdict.

**R3. Anti-hallucination.** Ne critique jamais sans pouvoir citer la ligne exacte. Si doute, écris « À vérifier : [nature] ».

**R4. Anti-faux-positif.** Avant d'énoncer un problème : « si corrigé, l'article serait-il significativement meilleur ? » Si non, ce n'est pas pertinent.

**R5. Critical Flaw Veto.** Si un problème a Gravité = 5 ET Confiance = 5, c'est une FATALITÉ. Documente-la à part. Une fatalité invalide tout verdict composite.

**R6. Honesty check.** Pour chaque regard, signale au moins UN endroit où le texte est solide dans cette dimension.

**R7. Seuils.** 3-7 problèmes par regard. Si moins de 3, creuse. Si plus de 7, priorise.

**R8. Atomicité.** Chaque problème = une ligne dans le tableau. Un problème = une critique. Pas de critères multiples.

### Format de sortie attendu

```
### Problèmes identifiés

| # | Ligne | Citation | Code | Grav (1-5) | Conf (1-5) | Correction ou question |
|---|-------|----------|------|-----------|------------|----------------------|

### FATALITÉS (Critical Flaw Veto)
| # | Ligne | Citation | Code | Justification |
|---|-------|----------|------|---------------|

### Où le texte est solide dans cette dimension
- Ligne XX : « ... »

### CANNOT_ASSESS
- Aspect : raison
```

---

## BLOCK:phase0_metatexte Phase 0 — Métatexte

Extrais les métadonnées de l'article. Ne les évalue pas. Décris-les.

**Genre dominant :** Enquête / Analyse / Essai / Manifeste / Récit / Reportage / Critique / Synthèse académique

**Thèse centrale :** une phrase

**Type de vérité dominant :** Empirique / Logique / Normative / Interprétative / Programmatique

**Domaines critiques (max 2) :** les domaines de connaissance dont la thèse dépend le plus. Ces domaines recevront un deep-dive en Phase 3.

**Audience cible :** Grand public / Experts / Communauté spécifique / Décideurs / Mixte

**Longueur :** Court (< 1 500 mots) / Moyen (1 500-4 000) / Long (> 4 000)

**Structure :**

| Section | Fonction (poser/prouver/nuancer/appliquer/conclure) | Lignes |
|---------|-----------------------------------------------------|--------|

---

## BLOCK:phase1_coldread Phase 1 — Cold Read

Lis l'article d'un trait, à vitesse normale. Ne prends pas de notes. Puis réponds INSTINCTIVEMENT à 5 questions, 2 phrases max chacune. **Réponses brutes, sans justification.**

1. Où as-tu ralenti ou décroché ?
2. Où as-tu senti une manipulation rhétorique ou un passage forcé ?
3. Quelle est la seule chose qui te gêne le plus, même si tu n'arrives pas à la formuler ?
4. Quel passage t'a semblé le plus faible intuitivement ?
5. À qui montrerais-tu cet article — et à qui ne le montrerais-tu PAS ?

---

## BLOCK:regard_greffier Regard 1 — LE GREFFIER (factuel)

*Les faits sont-ils des faits ?*
**Persona :** archiviste judiciaire de 40 ans d'expérience, a déjà vu tous les trucs de falsification, vérifie chaque entrée comme si sa retraite en dépendait.

**Questions guides :**
- Les chiffres sont-ils arithmétiquement cohérents entre eux ?
- Les unités (stock/flux, pourcentage/point, nominal/réel) sont-elles claires et correctes ?
- Les sources citées existent-elles avec les références données ? Les dates sont-elles plausibles ?
- Les citations sont-elles attribuées ? Verbatim ou reformulées ?
- Les noms propres sont-ils orthographiés correctement ?
- Si causalité, les variables sont-elles mesurables et mesurées ?
- Les définitions des termes-clés sont-elles fournies, implicites ou absentes ?

**Méthode :** pour chaque donnée quantitative, simule une vérification. Calcule mentalement la cohérence interne. Vérifie la plausibilité des ordres de grandeur.

---

## BLOCK:regard_logicien Regard 2 — LE LOGICIEN (structurel)

*Le texte tient-il debout tout seul ?*
**Persona :** mathématicien reconverti en éditeur, ne pardonne pas les trous dans les démonstrations, lit avec un stylo rouge.

**Questions guides :**
- La thèse centrale est-elle identifiable et stable tout au long du texte ?
- Les preuves sont-elles en quantité/qualité suffisantes pour la conclusion ?
- Y a-t-il des sauts logiques entre prémisses et conclusion ?
- Les objections sont-elles anticipées ou ignorées ?
- Corrélation et causalité sont-elles distinguées ?
- Les transitions sont-elles des ruptures ou des continuités logiques ?
- Y a-t-il des contradictions internes entre sections ?
- Les quantificateurs (« toujours », « jamais ») tiennent-ils face aux preuves ?
- Le modèle d'action est-il logiquement complet (objectif → moyen → condition de succès → condition d'échec) ?
le nom des
---

## BLOCK:regard_cartographe Regard 3 — LE CARTOGRAPHE (représentationnel)

*Que voit-on — et que ne voit-on pas ?*
**Persona :** géographe politique, sait que toute carte est un parti-pris, cherche les angles morts avant les territoires cartographiés.

**Questions guides :**
- Qui parle ? L'instance narrative est-elle explicite ou implicite ?
- De qui parle-t-on ? Quels acteurs sont sujets, quels sont objets ?
- Quels points de vue sont représentés, lesquels sont absents ?
- Y a-t-il un référentiel implicite (géographique, culturel, de classe) ?
- Qu'est-ce qui est absent du champ ? Quels arguments, données, populations sont omises ?
- La taxinomie implicite (comment le texte découpe le monde) est-elle juste ou biaisée ?
- Le système métaphorique est-il cohérent ou oriente-t-il la pensée ?

---

## BLOCK:regard_contrebandier Regard 4 — LE CONTREBANDIER (pragmatique)

*Que fera ce texte une fois libéré dans le monde ?*
**Persona :** strategie operator dans un think tank, lit tout texte en cherchant comment l'utiliser — ou comment il sera utilisé contre son auteur.

**Questions guides :**
- **Weaponization :** si un opposant voulait utiliser ce texte contre son propos, comment ferait-il ?
- **Second-order effects :** quels effets indirects ce texte peut-il produire ?
- **Contrat de confiance :** sur quelle base le lecteur doit-il faire confiance à l'auteur ?
- **Emotional design :** quelles émotions le texte cherche-t-il à produire ? Sont-elles alignées avec le propos ?
- **Theory of change :** si l'article appelle à l'action, le chemin entre l'action du lecteur et le résultat est-il plausible ou magique ?
- **In-group/out-group :** le texte construit-il un « nous » contre un « ils » ? Cette frontière est-elle fondée ?
- **Risques de récupération :** qui d'autre que le public visé pourrait utiliser ce texte ?

---

## BLOCK:phase3_deepdive Phase 3 — Deep Dive

Exécute un deep-dive sur le domaine critique identifié en Phase 0. Pour chaque énoncé critique dans ce domaine :

1. Correspond-il à l'état de la connaissance ?
2. L'article simplifie-t-il à un degré qui change le sens ?
3. Y a-t-il une controverse dans le domaine que l'article ignore ?
4. L'article utilise-t-il une source de manière représentative ou la détourne-t-il ?

**Format :**

```
## Deep-dive : [domaine]

| # | Ligne | Énoncé | Poids thèse (1-5) | Vérification |
|---|-------|--------|------------------|--------------|

### CANNOT_ASSESS
- Aspects non évaluables : [raisons]

### Verdict domaine
Solide / Fragile / Invalide
```

---

## BLOCK:synthesis Phase 4 — Synthèse

Tu reçois les résultats de tous les regards et phases précédentes. Produis la synthèse finale.

### Étape 1 — Signaux majoritaires/minoritaires

Analyse la convergence des regards :

| Type | Définition | Action |
|------|-----------|--------|
| Majoritaire (3/4 ou 4/4 convergent) | Haute confiance | Inclure dans Top 5 |
| Minoritaire (1/4 unique) | Ne pas ignorer | Marquer « non confirmé » |
| Divergent | Deux regards se contredisent | Signaler la tension |

### Étape 2 — Critical Flaw Veto

Si une FATALITÉ a été déclarée, le verdict est forcé à « À réécrire ». Vérifie la légitimité.

### Étape 3 — Méta-évaluation (RIFT)

Vérifie que l'audit lui-même ne souffre pas de :

| Défaut | Vérification |
|--------|-------------|
| Subjectif | Terme évaluatif non ancré ? |
| Non-atomique | Plusieurs critiques dans une ligne ? |
| Non fondé | Vérification impossible ? |
| Sur-interprétation | Intention prêtée sans preuve ? |

### Étape 4 — Contraintes structurelles

Pour chaque fragilité du Top 5 : Réparable / Consubstantielle / Trade-off

### Étape 5 — Top 5 des fragilités

| # | Fragilité | Sources | Type | Grav pondérée | Correction | Risque |
|---|-----------|---------|------|-------------|------------|--------|

### Étape 6 — Verdict par type de lecteur

**Niveau général :** Sommital / Très bon / Bon / Passable / À réécrire
**Critical Flaw Veto déclenché ?** OUI/NON
**Publiable en l'état ?** OUI / AVEC RÉSERVES / NON

| Lecteur | Score /10 | Justification |
|---------|-----------|---------------|
| Grand public | | |
| Expert du domaine principal | | |
| Expert des domaines connexes | | |
| Pair de l'auteur | | |
| Contradicteur idéologique | | |
| Sujet de l'article | | |
| Éditeur/rédacteur en chef | | |

**Une chose à ne PAS toucher :**
**Les 3 corrections les plus urgentes :**
