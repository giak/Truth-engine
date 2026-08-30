# Écrire un article à partir de données

> Méthode de base, avant tout chantier complexe. Tirée d'une enquête réelle (70 057 enregistrements, article forensique). v4 : ajout du contexte (besoin, problèmes, pistes) et de la fusion v38→Writer (voir `tools/engines/writer/FUSION_V38.md`).

## Contexte : besoin, problèmes, pistes

**Le besoin.** Produire, à partir d'une masse de données d'investigation (70 057 records, 57 quintessences KERNEL), un article forensique « à son apex » : conforme, traçable, démontratif, publiable.

**Les problèmes rencontrés.**

1. **Le pipeline produisait les données, pas l'article.** KERNEL (enquêtes) et Sublimator v36 (quintessences) fonctionnaient, mais l'étape article (Sublimator v38) ne produisait pas un texte assez bon.
2. **Le recours à ChatGPT a contourné le problème en en créant un autre.** L'article V4/V5/V6 est meilleur, mais à trois prix : vocabulaire épistémique dégradé (~40 statuts au lieu du canonique KERNEL), traçabilité refaite à la main (58 footnotes), entropie procédurale (33 cycles d'itération).
3. **Deux moteurs de prose coexistaient sans réconciliation.** v38 (16 LOIs négatives) et Writer (9 principes positifs) se chevauchaient ; Writer n'a jamais été utilisé.
4. **Un conflit de spécification central.** « Sourcing organique, zéro footnote » (v38 LOI 1) contredisait « toute phrase doit remonter à ses pièces » (invariant #6). Résolu par le sourcing hybride.

**Les pistes de solution retenues.**

1. **Division du travail** : Sublimator condense, Writer écrit, la checklist v38 valide (voir `tools/engines/writer/FUSION_V38.md`).
2. **Sourcing hybride** : source nommée en phrase + renvoi discret (URL + date). LOI 1 amendée.
3. **Le claim comme unité de pilotage** (§3), avec statut daté et vocabulaire canonique KERNEL (§4).
4. **L'audit inverse** (§10) : exploiter la donnée présente dans la base mais absente de l'article.
5. **La pyramide des données** (§2) : ne pas confondre les 89,5 % d'evidence brute avec les 61 claims pilotants.

## Principe directeur

Une enquête robuste n'est pas une recherche documentaire suivie d'une rédaction. C'est un **système de transformation contrôlée** :

```text
corpus brut
→ données structurées
→ hypothèses concurrentes
→ tests discriminants
→ preuves et contre-preuves
→ claims bornés
→ architecture démonstrative
→ article
```

Le danger principal est de **sauter un maillon**. Sauter du corpus à l'article produit un catalogue de faits sans démonstration. Sauter de l'hypothèse à la rédaction produit un plaidoyer, pas une enquête.

Règle de placement : **l'article arrive en dernier**. La thèse initiale existe, mais elle sert de *générateur d'hypothèses*, pas de conclusion présupposée. Une matière sélectionnée pour servir le récit est une matière morte.

---

## 1. Les cinq objets que l'on confond constamment

Presque toutes les erreurs viennent de la fusion de catégories différentes :

```text
SOURCE
≠ AFFIRMATION DE LA SOURCE
≠ FAIT ÉTABLI
≠ INFÉRENCE
≠ CONCLUSION ÉDITORIALE
```

Et, transversalement :

```text
CORRÉLATION        != CAUSALITÉ
DÉPENDANCE         != COMMANDE
FINANCEMENT        != INFLUENCE ÉDITORIALE
SIGNAL             != SANCTION
ERREUR             != INTENTION
INTERFACE          != COORDINATION
RÉSEAU             != COMPLOT
ASYMÉTRIE          != BIAIS
ABSENCE DE PREUVE  != PREUVE D'ABSENCE
CONNECTED          != COORDINATED
NETWORK            != HIERARCHY
STRUCTURE          != INTENT
```

Avec 50 sources, un humain tient ces distinctions de tête. Avec 70 000 enregistrements, c'est impossible : **la structure de données doit imposer elle-même la discipline épistémique**. Chaque champ de la base doit forcer la séparation que l'esprit ne sait plus maintenir.

---

## 2. L'architecture des données : sept couches, pas une grosse base

Accumuler tout dans un SQLite ou un CSV géant ne suffit pas. Il faut des couches séparées, chacune avec un rôle :

| Couche | Contenu | Règle |
|---|---|---|
| **RAW** | sources, documents, captures, textes bruts | jamais modifié |
| **CORPUS** | extraction normalisée, dédupliquée | provenance conservée |
| **EVIDENCE** | faits, citations, chiffres, relations, événements | peut soutenir OU contredire |
| **CLAIMS** | ce que l'on envisage d'affirmer | l'unité de pilotage |
| **GAPS** | ce qu'il faudrait encore pour trancher | résultat négatif = donnée |
| **DECISIONS** | pourquoi un claim est gardé, réduit, rejeté, ouvert | traçabilité du raisonnement |
| **ARTICLE** | architecture éditoriale + correspondance claim → preuve → passage | la sortie |

Le reste (registres multiples, graphes, dashboards, fichiers dérivés) est secondaire. **Un outil supplémentaire ne se justifie que s'il répond à une question que les couches existantes ne traitent pas.** Sinon : YAGNI.

### Diagnostic concret (chiffres re-vérifiés contre la base)

Sur 70 057 records :

- **62 684 (89,5 %)** sont des mentions mécaniques : 25 260 nombres, 17 208 blocs de texte, 11 335 dates, 4 188 URLs, 2 965 pourcentages, 1 728 monnaies. Ce ne sont **pas du bruit** : c'est **l'evidence brute**, le substrat de preuves (chiffres, citations, sources) avant promotion en claim.
- **66 854 (95,4 %)** ont un `EPISTEMIC_STATUS` vide : ils n'ont pas encore été qualifiés.
- **3 203** records ont un `EPISTEMIC_STATUS` non vide, **2 695** un `CONFIDENCE`, **3 027** un `PUBLICATION_SAFE`. C'est la matière qualifiée.
- Au sommet de l'enquête en cours : **36 `FROZEN_CORE_CLAIM` + 25 `CANONICAL_ARGUMENT_CLAIM` = 61 claims** portant chacun un statut. S'y ajoutent **197 `CANONICAL_CLAIM`** de provenance mélangée (dont des faits financiers directement pertinents, et des claims d'une autre enquête), plus 265 `FACT`, 63 `FINDING`.

La leçon n'est pas « 95 % est à ignorer ». C'est l'inverse : **les 62 684 mentions sont le bassin de preuves que l'on interroge quand un claim a besoin de soutien.** La pyramide : 89,5 % d'evidence brute → ~4 % de matière qualifiée → 61 claims pilotants.

### La lignée réelle : KERNEL → Sublimator → LLM externe

Les sept couches ci-dessus ne sont pas une abstraction libre : elles recouvrent le pipeline réel du projet.

```text
KERNEL v2.8 (investigation forensique)
  → INVESTIGATION.md : FCT-### (faits, EPI + tier), CLM-### (claims),
    CAU-### (causalité PELOTE), GAP, TRACE, BIAS_TEST (15 symboles), ÉDI
  → Sublimator (extraction atomique)
  → _quintessence/*.md : F### + scoring ✦/✧/⁅/❧ + 11 sections
  → zip
  → deux branches :
      (a) LLM externe (recherches web + itérations Q/R)
          → SQLite master (70 057 records, non vérifié)
      (b) Freebuff : protocole de vérification (fact-checker)
          → Mnemolite (status CONFIRME/VERIFIE + memory_id + source + citation)
  → article (préférentiellement alimenté par Mnemolite CONFIRME)
```

Correspondance couche conceptuelle ↔ artefact réel :

| Couche | Artefact réel |
|---|---|
| RAW | sources fetchées pendant la recherche KERNEL |
| CORPUS | corpus maître (Conspipédia) + documents |
| EVIDENCE | FACT_REGISTRY (FCT-###) + quintessence F### |
| CLAIMS | CLAIM_REGISTRY (CLM-###) + claims de l'article |
| GAPS | registre GAP (GAP_TYPE, SATURATION) |
| DECISIONS | STATUS_DELTA + décisions de mapping |
| ARTICLE | l'article final |

Conséquence majeure : **la base SQLite est la sortie du LLM externe, pas l'entrée du pipeline.** Elle est alimentée par deux flux : (1) la quintessence structurée KERNEL→Sublimator (les faits typés), et (2) les recherches web et itérations questions/réponses du LLM externe lui-même (l'essentiel des 62 684 mentions mécaniques). Le vocabulaire épistémique canonique est défini en amont, dans KERNEL (voir §4) ; le SQLite en est une re-saisie partiellement dégradée, aggravée par le volume d'itérations.

**La couche de vérité vérifiée est Mnemolite**, alimentée par le protocole de vérification Freebuff (fact-checker) : les faits `status:CONFIRME`/`VERIFIE` y portent `memory_id`, source, URL et citation. L'article se construit préférentiellement sur ces faits vérifiés, selon le protocole mémoire-d'abord : `search_memory` avant le web, `write-back` obligatoire après toute recherche web aboutie, et zéro appel web pour un fait déjà `status:CONFIRME`. Le SQLite fournit le bassin de preuves ; Mnemolite fournit ce qui a été vérifié.

---

## 3. Le claim, unité centrale de pilotage

L'article ne publie finalement qu'un petit nombre d'affirmations importantes. C'est donc le **claim**, pas le document, qui pilote le système. Chaque claim doit répondre immédiatement à :

```text
CLAIM_ID
texte exact
statut épistémique
date de validité du statut
importance éditoriale
preuve principale
corroborations indépendantes
contre-preuves
alternative explicative
niveau de confiance
risque juridique
risque causal
ce qui falsifierait le claim
superseded_by (claim qui le remplace, le cas échéant)
utilisé dans l'article ? où ?
```

Et surtout, la question de pilotage unique :

> **Quelle formulation maximale les preuves m'autorisent-elles à écrire sans franchir la frontière probatoire ?**

Pas « que puis-je raisonnablement raconter ? », mais « quelle phrase précise est autorisée ? ». C'est la règle qui sépare une enquête d'un essai.

### Le statut est daté, pas absolu

Un claim n'est pas `OPEN` dans l'absolu : il est `OPEN` **à une date**, révisable. La base porte des statuts temporellement bornés (`ESTABLISHED_INTENT_WITH_TEMPORAL_LIMIT`, « au 18 août 2026 »). Conséquence : toute phrase de l'article qui affirme un `OPEN` ou un `ESTABLISHED` porte implicitement une date de validité. Un claim révisé doit pointer vers son remplaçant (`superseded_by`), jamais disparaître silencieusement.

---

## 4. Le vocabulaire épistémique est déjà défini en amont (KERNEL)

La base SQLite porte ~40 valeurs de statut hétérogènes. Ce désordre n'est pas un manque de méthode : c'est un **artefact de handoff**. Le vocabulaire canonique existe en amont, dans KERNEL v2.8, et la re-saisie par le LLM externe l'a partiellement dégradé.

Vocabulaire canonique (KERNEL v2.8) :

| Axe | Valeurs | Signification |
|---|---|---|
| **EPI** (nature de la proposition) | FACT / EVIDENCE / INFERENCE / HYPOTHESIS / SPECULATION / UNKNOWN | ce que la proposition EST |
| **Tier** (disponibilité de la source) | ✦ / ✧ / ⁅ / ❧ | ✦ = ≥2 familles indépendantes fetchées ; ✧ = 1 famille ; ⁅ = URL non fetchée ; ❧ = pas d'URL |
| **Glyphe** (statut épistémique) | ⁕ CLAIMED / ⁂ SPECULATED / ⊗ CONTRADICTED / ⊙ PARTIAL | ce que la source ATTRIBUE vs DÉMONTRE |
| **Statut** (après vérification) | CONFIRME (✦ L4) / VERIFIE (✧ L1-L3) | le write-back mémoire |

Écriture autorisée, dérivée de ce vocabulaire (et non d'un vocabulaire inventé) :

| Statut | Écriture autorisée | Interdit |
|---|---|---|
| ✦ FACT (CONFIRME) | affirmer | noyer dans le conditionnel |
| ✧ FACT (VERIFIE) | affirmer avec attribution | transformer en certitude multi-source |
| ⁅ / ❧ | ne pas affirmer (source non ancrée) | affirmer sans source |
| ⁕ CLAIMED | « X affirme / autodéclare » | présenter comme fait établi |
| ⁂ SPECULATED | « hypothèse, non démontré » | présenter comme mécanisme établi |
| ⊗ CONTRADICTED | « contesté » | présenter comme acquis |
| GAP (OPEN) | « cherché, non trouvé » (méthode documentée) | « n'existe pas » sans méthode |

Règle : **toute valeur de la base SQLite doit être mappée vers ce vocabulaire canonique avant rédaction.** Un statut SQLite non mappable est un chantier de re-tracage vers la quintessence KERNEL d'origine, pas un statut à inventer.

---

## 5. Le registre de gaps : le résultat négatif est une donnée

« Information non trouvée » ne suffit pas. Un gap doit être enregistré comme une conclusion méthodologique reproductible :

```text
question
ce qui a été cherché
avec quelles variantes
où
ce qui a été trouvé
ce qui manque
pourquoi cela empêche de conclure
quelle source pourrait théoriquement fermer le gap
public / probablement non public
```

Ainsi :

```text
RiPOST telemetry
→ OPEN
→ impressions / clics / CTR / conversions / spend réels absents
→ ROI informationnel non calculable
```

devient un verdict, pas un trou. Cela évite qu'un agent (humain ou LLM) relance quinze fois la même recherche.

**Accepter `OPEN` tôt.** Certaines questions sont impossibles à fermer publiquement. `OPEN` n'est pas un échec : c'est parfois le seul verdict honnête. Exemple réel :

```text
mécanisme général de conflit d'intérêts inconscient   → SUPPORTED (littérature)
application à la population étudiée                    → OPEN (pas d'expérience discriminante)
```

Un `OPEN` correctement démontré vaut mieux qu'une conclusion forcée.

---

## 6. Chercher n'est pas enquêter

La recherche classique :

```text
question → recherche → source → réponse
```

L'enquête :

```text
question → hypothèses concurrentes → prédictions observables
→ données discriminantes → recherche ciblée → résultat
→ révision des hypothèses → nouvelle question
```

La bonne question n'est pas « trouve-moi des infos sur le financement des fact-checkers », mais :

> **Quelle observation permettrait de distinguer un financement de capacité d'un financement qui modifie le comportement éditorial ?**

### Privilégier le discriminant, pas l'horizontal

```text
10 sources → incertitude
30 sources → plus de contexte
100 sources → la même incertitude
```

Continuer n'est plus de l'investigation, c'est de l'accumulation. Règle :

> **Priorité informationnelle = capacité d'une donnée à modifier le verdict, pas quantité de contexte ajoutée.**

Une dixième page de politique de financement apporte peu. Un `contrat / rate card / SOW / critère KPI / série avant-après / comparaison financeur-non-financeur` peut être discriminant.

### L'heuristique de priorité

```text
PRIORITÉ =
  importance_du_claim
  × incertitude_actuelle
  × pouvoir_discriminant_de_la_donnée
  × probabilité_de_l'obtenir
  ÷ coût
```

Une piste fascinante mais sans importance pour l'article → priorité faible. Une petite pièce qui fait basculer une conclusion centrale → priorité maximale.

---

## 7. La discipline épistémique, partout

### Le dénominateur avant le chiffre

Les chiffres impressionnants sont les plus dangereux. `51 contre 24` ne signifie rien sans :

```text
numérateur / dénominateur / unité / périmètre
période / population / méthode / source
```

Sans cela, un chiffre précis fabrique une fausse rigueur. Le réflexe doit être systématique, y compris sur ses propres chiffres.

### Explorer ≠ confirmer

L'exploration regarde partout (patterns, corrélations, outliers, réseaux, anomalies). Mais une anomalie découverte **dans les données qui ont servi à la découvrir** n'est pas une preuve. Il faut ensuite une phase confirmatoire : hypothèse gelée, population définie, variables et règles de codage définies, contre-hypothèses définies, puis test. Uniquement quand le problème le justifie : ne pas transformer chaque article en publication académique.

### Les graphes posent des questions, ils ne concluent pas

```text
A finance B → B travaille avec C → C certifie D → D fournit un signal à E
```

ne démontre pas `A contrôle E`. Un graphe transforme des arêtes vraies en impression de système cohérent. Règle : **le graphe génère des questions, il ne fournit pas la conclusion.**

### Les contre-hypothèses dès la création du claim

La red team en fin de processus est utile mais tardive. Les alternatives doivent être inscrites **dès la naissance du claim**. Exemple :

```text
Observation : Le Pen davantage vérifiée que Macron sur un événement donné.
H1 : biais idéologique
H2 : nombre différent d'affirmations vérifiables
H3 : nombre différent d'affirmations erronées
H4 : stratégie de communication différente
H5 : choix de saillance éditoriale
H6 : hasard / petit échantillon
```

Sans le dénominateur qui départage H1-H6, il est interdit de convertir l'observation en « preuve d'un biais ». Cette démarche doit être native, pas corrective.

---

## 8. La boucle d'investigation, avec sa sortie

```text
OBSERVE → QUESTION → HYPOTHÈSES → DISCRIMINANT → SEARCH
→ EVIDENCE → COUNTEREVIDENCE → VERDICT → GAP → NEXT
```

Règle de sortie :

```text
STOP si :
- claim suffisamment fermé ;
- un nouveau search n'ajoute plus de pouvoir discriminant ;
- la donnée nécessaire n'est pas publique ;
- coût marginal > valeur informationnelle ;
- la question n'est pas indispensable à l'article.
```

`STOP` est aussi important que `SEARCH`. Un système sans condition de sortie devient une machine à accumuler.

---

## 9. L'article comme démonstration, pas comme rapport

Une fois l'enquête mûre, ne pas commencer par « écrire joliment ». Construire d'abord :

```text
QUESTION → FAIT ÉTONNANT → MÉCANISME → PREUVE
→ CONTRE-EXPLICATION → TEST → CE QUI RÉSISTE → LIMITE → CONSÉQUENCE
```

Un bon article forensique n'est pas un rapport de base de données. Il **cache la complexité du laboratoire sans cacher les limites de la preuve**. Le lecteur n'a pas besoin de voir les 70 000 lignes : il doit comprendre *pourquoi* la conclusion découle des pièces.

### Séparer le laboratoire et la publication

- **Laboratoire** : sale, exhaustif, contradictoire (notes, hypothèses absurdes, leads, doublons, résultats négatifs, graphes, scripts, versions abandonnées).
- **Article** : net (question, faits nécessaires, démonstrations, contre-arguments loyaux, limites, conclusion, sources).

Le lecteur ne subit pas l'historique de l'enquête. Mais le laboratoire doit permettre à quiconque de **reconstruire et attaquer l'article**. C'est là que le RAG prend sa valeur : il est la preuve que l'article a un laboratoire.

### La provenance doit survivre à toutes les transformations

```text
SOURCE → EXTRACTION → NORMALISATION → RECORD → CLAIM → ARTICLE
```

doit rester traversable dans les deux sens :

```text
phrase article → claim → evidence → extrait → document → URL source
```

et, en sens inverse :

```text
pièce → tous les claims et passages qui l'utilisent
```

C'est le critère de qualité opérationnel, parce qu'il teste la réversibilité de la chaîne : « pourquoi cette phrase existe-t-elle ? » doit répondre en quelques secondes. Sans cette réversibilité, une phrase devient inattaquable dans les deux sens et la base cesse de servir de laboratoire.

---

## 10. L'audit inverse : la donnée présente mais non utilisée

« Exploiter la donnée » ne veut pas dire lire la base. Cela veut dire **auditer l'écart entre ce que la base contient et ce que l'article utilise**, dans deux sens :

1. **Claim → evidence** : pour chaque claim de l'article, la base contient-elle une preuve plus forte ou plus précise que celle citée ?
2. **Evidence → claim** : pour chaque cluster d'evidence de la base, est-il absent de l'article, et pourquoi (périmètre, redondance, oubli) ?

Exemple réel : l'article cite « Full Fact a reçu 342 712 £ de Meta en 2025 » (une seule ligne). La base contient en plus :

```text
C13-FIN-001 : Full Fact 2025, revenu total £3 054 478 ;
              flux directs Meta/Facebook/Google £766 988 (~25,1 %).
C13-FIN-002 : £259 726 de l'EFCSN pour « Prebunking at Scale »,
              projet financé par Google.org ; après réattribution,
              plancher Big Tech 2025 ≈ £1,03 M.
```

Le chiffre publié est donc un fragment d'une image plus complète **déjà présente dans la base**. L'audit inverse est ce qui transforme « masse de data » en « data exploitable » : il localise les preuves que l'article oublie, et interdit qu'une conclusion reste plus faible que les pièces disponibles ne l'autorisent.

---

## 11. Trois moteurs, pas quinze sous-systèmes

Le système tient en trois moteurs + une fonction transversale :

```text
DISCOVERY        → corpus + leads
      ↓
PROOF            → claims + tests + evidence + gaps
      ↓
EDITORIAL        → démonstration + article
```

Transversal : `RED TEAM / FACT CHECK / JURIDIQUE`.

Les reviewers interviennent à des moments différents, pas tous partout :

```text
Exploration        → contradicteur épistémologique
Données            → auditeur provenance / data
Claims             → fact-checker forensique
Causalité          → contradicteur causal / statisticien
Architecture       → rédacteur en chef
Texte presque final → juriste
Final              → hostile reviewer + non-régression
```

Point subtil : **le contradicteur doit intervenir avant que la formulation ne se cristallise**. Après, il ne fait que corriger ; avant, il modifie l'enquête.

---

## 12. Le risque spécifique du LLM : fabriquer de la cohérence

Avec un humain seul, le goulot est « pouvons-nous lire 5 000 documents ? ». Avec un LLM, il se déplace :

> **« Pouvons-nous empêcher le système de fabriquer de la cohérence artificielle avec 5 000 documents ? »**

Le LLM excelle à relier, résumer, catégoriser, généraliser, raconter : précisément les opérations qui créent de faux systèmes. Il faut donc l'utiliser pour **extraire, chercher, contraster, falsifier, normaliser, dédupliquer, retrouver, tester** *avant* de lui demander de **synthétiser, interpréter, raconter**.

### Le RAG ne doit pas devenir une machine à confirmation

Une requête « montre-moi comment les financeurs influencent le fact-checking » récupère les morceaux compatibles avec cette formulation. Il faut pouvoir demander en parallèle :

```text
preuves POUR / preuves CONTRE / contre-exemples / résultats négatifs
claims réfutés / gaps / sources primaires / sources dépendantes
hypothèses alternatives
```

D'où des métadonnées épistémiques sur chaque chunk : `source_type`, `claim_id`, `supports`, `contradicts`, `status`, `confidence`, `primary/secondary`, `independence_group`, `superseded_by`. Le champ `contradicts` est aussi important que `supports`.

### Conserver les erreurs, pas seulement les corrections

Ne jamais transformer silencieusement `CLAIM V1 faux` en `CLAIM V2 correct` en supprimant V1. Conserver :

```text
V1 → ERREUR DÉTECTÉE → CAUSE → CORRECTION → IMPACT → V2
```

L'erreur révèle souvent une faiblesse méthodologique : c'est du **knowledge négatif**, précieux pour le prochain LLM.

---

## 13. Les sept invariants

1. **Ne jamais confondre corpus et preuve.**
2. **Ne jamais confondre observation et explication.**
3. **Toute hypothèse sérieuse a au moins une hypothèse rivale.**
4. **Chercher d'abord la donnée qui pourrait changer le verdict.**
5. **Un `OPEN` correctement démontré vaut mieux qu'une conclusion forcée.**
6. **Toute phrase importante de l'article doit remonter jusqu'aux pièces qui l'autorisent.**
7. **L'enquête doit pouvoir produire une conclusion différente de celle espérée au départ.**

Le septième est le plus discriminant, parce qu'il teste la seule propriété qui sépare un moteur d'investigation d'un moteur de confirmation : la capacité à produire une conclusion contraire à l'hypothèse de départ. Si le pipeline ne peut pas répondre « Non, cette intuition était fausse », il confirme, il n'enquête pas.

---

## 14. Les modes d'échec à connaître

Chaque invariant existe parce qu'un mode d'échec l'a rendu nécessaire. Table de correspondance :

| Mode d'échec | Symptôme observé | Garde-fou |
|---|---|---|
| Entropie procédurale | 30+ cycles, versions de bases et dashboards successives | §11 trois moteurs, condition de sortie §8 |
| Overengineering | registres, graphes, POC multipliés sans question nouvelle | un outil = une question non traitée (§2) |
| Recherche horizontale | 100 sources, incertitude inchangée | discriminant (§6), STOP (§8) |
| Red team tardive | la correction remplace la modification de l'enquête | contre-hypothèses natives (§7) |
| Suppression silencieuse des erreurs | V1 disparaît, V2 reste | conserver les erreurs (§12) |
| RAG à confirmation | requête orientée → morceaux compatibles | champ `contradicts` (§12) |
| Dégradation au handoff | le vocabulaire canonique KERNEL (EPI + tier + glyphes) devient ~40 valeurs SQLite hétérogènes | mapper vers KERNEL (§4), jamais ré-inventer |
| Evidence oubliée | conclusion plus faible que les pièces disponibles | audit inverse (§10) |
| Corpus confondu avec preuve | un document présent = un fait établi | §1 les cinq objets |

---

## 15. Cas d'application : le fact-checking

Ce que la méthode a produit sur l'enquête de référence :

- **Corpus** : 70 057 records, 89,5 % d'evidence brute (mentions mécaniques), 95,4 % sans qualification épistémique.
- **Sommet** : 61 claims pilotants (36 faits figés + 25 thèses argumentatives), chacun portant un statut daté.
- **Résultat emblématique** : l'intuition « on ne mord pas la main qui nourrit » est morte en tant que loi générale (contre-exemples trouvés), puis raffinée en :

> L'argent exerce au minimum un pouvoir de cadrage, de capacité et de sortie. Son influence sur le verdict lui-même doit être démontrée séparément.

Le produit visé par une enquête réussie est là : **raffiner une intuition jusqu'à son noyau démontrable**, moins spectaculaire mais plus difficile à réfuter. C'est la définition même du progrès probatoire : la thèse finale est plus étroite et plus solide que l'intuition initiale.

- **Audit inverse** : a révélé que l'article publiait un fragment (342 712 £ Meta) là où la base contenait l'image complète (3,05 M£ total, ~25 % Big Tech, subvention Google.org). La donnée existait ; elle n'était pas remontée dans l'article.

La prochaine étape n'est pas d'écrire une grosse spécification, mais un **workflow minimal V1** : 6 à 8 objets, les sept invariants, une boucle d'investigation discriminante, et un test sur une enquête entièrement différente pour vérifier qu'il tient.
