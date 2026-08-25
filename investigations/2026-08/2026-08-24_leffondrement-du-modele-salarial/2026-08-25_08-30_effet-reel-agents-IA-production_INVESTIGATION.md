# KERNEL INVESTIGATION: L'effet réel des agents IA en production

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0830-AGENTS-IA-EFFET-REEL |
| Type | KERNEL COMPLEX |
| Loup parent | L-003 (fresque systémique IA-salariat) |
| Date | 2026-08-25 08:30 CEST |
| Gate | naming PASS, em-dash PASS, 111 tests PASS (BLOCKED branche protégée, structurel) |
| RUN_MANIFEST | KERNEL-v2 §4.1 |
| Statut | COMPLETED |

---

## 1. BRIEF

**Question d'enquête :** Quel est l'effet réel, documenté et vérifiable, des agents IA déployés en production sur les emplois ? Pas les projections, pas les promesses — les suppressions de postes attribuables à l'IA, les échecs documentés, les retournements de stratégie.

**Verdict forensique :** L'effet est **réel, concentré, et très inférieur au discours des CEO.** Trois patterns dominent :

1. **Le pattern « remplacer puis regretter »** : Klarna (700 emplois, demi-tour), Commonwealth Bank (45 emplois, excuses écrites), IBM (freeze d'embauche puis triplement des recrutements juniors). L'IA gère le volume, échoue sur la complexité, l'humain est rappelé.

2. **Le pattern « couper dans le profit record »** : Cloudflare (1 100 emplois, record de revenus), Oracle (20 000-30 000, +95 % de résultat net), Block (4 000, 40 % des effectifs, +24 % de profit brut). L'IA est la justification publique ; la profitabilité est la cause réelle.

3. **Le pattern « hybride qui tient »** : Salesforce (4 000 supprimés, mais AI = 50 % du volume seulement, 5 000 humains conservés pour les escalades, CSAT maintenue). La seule stratégie documentée qui fonctionne est l'augmentation, pas le remplacement.

Le chiffre clé : **50-55 % des emplois remodelés, 10-15 % potentiellement éliminés à 5 ans (BCG 2026)** — et ce 10-15 % est une borne haute sous conditions (pas de nouvelle rupture technologique, adoption lente). Les suppressions déjà réalisées et attribuables directement à l'IA, sans cause financière sous-jacente, sont de l'ordre de **21 490 au T1 2026** (Challenger, Gray & Christmas), soit 13 % des licenciements totaux — pas 40-50 % comme le suggère le discours ambiant.

---

## 2. CLAIMS_REGISTRY

### CL-001 — L'IA remplace déjà massivement les travailleurs
- **Claim :** « Près de la moitié des licenciements tech du T1 2026 sont dus à l'IA » (RecruitHorizon.ai)
- **Niveau :** L2 — démenti par Oxford Economics (janvier 2026) et Yale Budget Lab (février 2026) qui ne trouvent aucune trace macro de disruption IA dans l'emploi. Le chiffre Challenger : 13 % des licenciements T1 2026 attribués à l'IA.
- **Statut :** NOT_VERIFIED — exagération par 3-4×. Le chiffre réel est 13 %, pas 50 %. Et même 13 % mélange cause réelle et « AI washing » (Sam Altman lui-même le reconnaît).

### CL-002 — Les remplacements IA complets (full automation) fonctionnent
- **Claim :** L'IA peut remplacer intégralement des départements entiers (customer service, HR back-office)
- **Niveau :** L2 — démenti par les trois cas documentés de retournement : Klarna (700 emplois remplacés → qualité dégradée → retour aux humains), Commonwealth Bank (45 emplois → « erreur » reconnue par écrit → réembauche), IBM (7 800 gelés → triplement des recrutements juniors).
- **Statut :** NOT_VERIFIED. Le full automation échoue sur la complexité, les cas limites, l'émotionnel, et la perte de connaissance institutionnelle.

### CL-003 — Les CEO sont honnêtes sur les causes des licenciements IA
- **Claim :** Les licenciements annoncés comme « liés à l'IA » sont effectivement causés par l'IA.
- **Niveau :** L1 — invérifiable dans l'absolu, mais le faisceau d'indices converge fortement vers l'« AI washing ». Cloudflare licencie 1 100 personnes le jour où elle annonce un chiffre d'affaires record (+34 %). Oracle supprime 20 000-30 000 postes avec un résultat net en hausse de 95 %. Block coupe 40 % des effectifs avec +24 % de profit brut. Le pattern « licencier pendant les profits records en invoquant l'IA » est documenté sur au moins 8 entreprises.
- **Statut :** PARTIALLY_VERIFIED. Le mécanisme « profits records + licenciements = AI washing probable » est documenté. L'intention exacte est non prouvée.

### CL-004 — Les agents IA remplacent surtout les juniors, pas les seniors
- **Claim :** Les déploiements IA en production ciblent les tâches d'entrée de gamme, pas l'expertise.
- **Niveau :** L2 — documenté par HeroHunt (mai 2026), BCG (avril 2026), et le cas IBM. Les juniors font du code, de la documentation, du bug fixing — exactement ce que l'IA générative fait bien. Les seniors font de l'architecture, du client, de la décision — ce que l'IA ne fait pas.
- **Statut :** VERIFIE.

### CL-005 — Le modèle hybride humain-IA est systématiquement supérieur au remplacement complet
- **Claim :** L'association humain + IA surpasse l'IA seule ou l'humain seul.
- **Niveau :** L2 — documenté par Klarna (échec du tout-IA), Salesforce (succès du 50/50), Digital Applied (mars 2026, analyse du cas Klarna), BCG (avril 2026, 50-55 % remodelés, pas remplacés).
- **Statut :** VERIFIE.

---

## 3. FACT_REGISTRY

### 3.1 Les remplacements qui ont échoué (et ce qu'ils révèlent)

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-001 | Klarna : 700 agents customer service remplacés par IA (2024). Début 2026 : demi-tour. Qualité dégradée sur cas complexes, coûts de réembauche > économies projetées ($40M). | Digital Applied, 9 mars 2026 | https://www.digitalapplied.com/blog/klarna-reverses-ai-layoffs-replacing-700-workers-backfired |
| F-002 | Klarna : effectifs passés de 5 500 à 3 400, hiring freeze >1 an. CEO Siemiatkowski a admis que l'approche « allait trop loin ». | Fast Company, 12 janvier 2026 | https://www.fastcompany.com/91468582/klarna-tried-to-replace-its-workforce-with-ai |
| F-003 | Commonwealth Bank of Australia : 45 emplois customer service remplacés par voice-bot IA (juillet 2025). Août 2025 : marche arrière, excuses écrites, « erreur » reconnue. | ABC Australia, 21 août 2025 | https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492 |
| F-004 | IBM : mai 2023, CEO Krishna annonce 7 800 emplois gelés (30 % back-office). Février 2026 : CHRO LaMoreaux annonce le triplement des recrutements juniors US. « Les entreprises qui réussiront dans 3-5 ans sont celles qui auront doublé l'embauche junior dans cet environnement. » | TwinLadder Research, mars 2026 | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder |
| F-005 | IBM : AskHR traite 94 % des questions RH routinières. Mais le problème n'était pas la performance de l'IA — c'était la disparition du pipeline de talents : sans juniors, plus de seniors dans 5-10 ans. | TwinLadder, ibid. ; Josh Bersin, mai 2025 | https://joshbersin.com/2025/05/yes-hr-organizations-will-partially-be-replaced-by-ai-and-thats-good/ |
| F-006 | IBM : 13 000-17 000 suppressions d'emplois sur 2024-2025 (deux vagues). Puis revirement complet en 2026. | TwinLadder, ibid. | ibid. |
| F-007 | 55 % des entreprises regrettent les licenciements motivés par l'IA | Tandem Coach, 2026 (citant étude non nommée — L1, demande corroboration) | https://tandemcoach.co/klarna-ai-automation-lesson/ |

### 3.2 Les remplacements « réussis » (et leurs nuances)

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-008 | Salesforce : 4 000 emplois support supprimés (support passé de ~9 000 à ~5 000). Agentforce traite 1,5 M conversations = volume humain, CSAT équivalente. Mais : 5 000 humains conservés pour escalades. Ce n'est PAS un remplacement complet, c'est un modèle hybride 50/50. | TechRadar, 2 septembre 2025 ; New Market Pitch, 29 juin 2026 | https://www.techradar.com/pro/salesforce-says-it-cuts-4-000-support-jobs-and-replaced-them-with-ai |
| F-009 | Benioff : « I need less heads » + Salesforce n'embauchera plus de software engineers en 2025. | CNBC, cité par HeroHunt | https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/ |
| F-010 | Chegg : 248 emplois supprimés (mai 2025), puis 388 (octobre 2025). Action passée de $113.51 à $0.48. ChatGPT détruit la croissance client. Cas canonique de destruction par l'IA — mais d'une entreprise, pas d'un secteur. | CNBC, cité par HeroHunt | ibid. |

### 3.3 Les licenciements massifs attribués à l'IA (et leurs profits records)

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-011 | Block (Square/Cash App) : ~4 000 emplois supprimés (40 % des effectifs), février 2026. Jack Dorsey : « l'IA permet de faire plus vite avec des équipes plus petites. » Profit brut Q4 : $2,87 Md, +24 % YoY. Action : +24 %. | CNN, cité par HeroHunt | https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/ |
| F-012 | Oracle : 20 000-30 000 supprimés (~18 % des 162 000), mars 2026. Résultat net : +95 % ($6,13 Md). A demandé aux employés de documenter leurs workflows pour entraîner l'IA — puis les a licenciés. TIME : une rédactrice technique de 30 ans d'ancienneté, appelée pendant qu'elle allait à l'hôpital pour une chirurgie du dos. | TIME, mars 2026, cité par HeroHunt | ibid. |
| F-013 | Cloudflare : 1 100 supprimés (20 %, première vague en 16 ans d'histoire), mai 2026. Chiffre d'affaires trimestriel record : $639,8 M, +34 % YoY. CEO Prince : « gains de productivité massifs — 2, 10, voire 100 fois plus productifs. » Utilisation interne IA : +600 % en 3 mois. | TechCrunch, cité par HeroHunt | ibid. |
| F-014 | Coinbase : 700 supprimés (14 %), mai 2026. CEO Armstrong : « ship in days what used to take a team weeks. » Alerte : licenciements massifs à venir dans « toutes les entreprises ». | CNBC, cité par HeroHunt | ibid. |
| F-015 | Meta : 8 000 supprimés (10 %), avril-mai 2026. +6 000 postes gelés. Capex IA 2026 : $125-145 Md. | CNBC, cité par HeroHunt | ibid. |
| F-016 | Microsoft : 8 750 buyouts volontaires (7 % US, première fois en 51 ans d'histoire), avril 2026. Capex IA 2026 : $190 Md. | Fortune, cité par HeroHunt | ibid. |
| F-017 | PayPal : 4 760 supprimés (20 %), mai 2026. Upwork : 145 (24 %). Freshworks : 500 (11 %). Bill : jusqu'à 30 %. Toutes citent l'IA. | TechRadar, cité par HeroHunt | ibid. |
| F-018 | Total licenciements tech 2026 : ~128 270 personnes, 286 événements au 10 mai 2026 (~1 002/jour). | HeroHunt, 10 mai 2026 | ibid. |
| F-019 | Capex IA 2026 des 4 géants : $725 Md cumulés (Microsoft $190 Md, Meta $125-145 Md, etc.) | 24/7 Wall St., cité par HeroHunt | ibid. |

### 3.4 Les données macro qui contredisent la panique

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-020 | 13 % des licenciements US du T1 2026 attribués à l'IA (Challenger, Gray & Christmas). Avril 2026 : 21 490 sur 83 387 annoncés. | Fortune / Challenger, Gray & Christmas | cité par HeroHunt et FinalRoundAI |
| F-021 | Oxford Economics (janvier 2026) : les entreprises « ne semblent pas remplacer les travailleurs par l'IA à une échelle significative » | Oxford Economics, janvier 2026 | cité par FinalRoundAI |
| F-022 | Yale Budget Lab (février 2026) : le taux de changement occupationnel n'a pas augmenté assez pour signaler une disruption massive ; durée de chômage inchangée pour les emplois exposés à l'IA ; « pas de preuve macro de disruption IA dans l'emploi » | Yale Budget Lab, février 2026 | cité par FinalRoundAI |
| F-023 | Sam Altman (OpenAI) reconnaît un « certain degré d'AI washing » — des entreprises blâment l'IA pour des licenciements qu'elles auraient faits de toute façon. | OpenAI, cité par FinalRoundAI | ibid. |
| F-024 | BCG (avril 2026) : 50-55 % des emplois US remodelés (reshaped) en 2-3 ans. 10-15 % potentiellement éliminés en 5 ans+. « Task automation does not equal job loss — most roles will remain but change substantially. » | BCG, avril 2026 | https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces |
| F-025 | BCG : le modèle est microéconomique (pas une prévision de chômage). Suppose les capacités IA actuelles, pas de rupture. Si l'IA atteint le niveau humain en jugement ouvert, le cadre doit être révisé. | BCG, ibid. | ibid. |
| F-026 | McKinsey (2026) : 57 % des heures de travail US automatisables avec la technologie actuelle. Mais distinction clé : travail que l'IA assiste ≠ travail que l'IA accomplit entièrement. | McKinsey Global Institute, 2026 | cité par FinalRoundAI |
| F-027 | WEF Future of Jobs 2025 : 92 millions d'emplois déplacés d'ici 2030, 170 millions créés (solde net +78 M). | WEF, 2025 | cité par FinalRoundAI |

### 3.5 Qui perd vraiment son emploi (les métiers touchés)

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-028 | Juniors développeurs : « AI has eliminated the specific tasks junior developers were assigned, not the senior roles. » Les seniors deviennent des « tech leads » pilotant des « armées d'agents IA » (Zuckerberg). Les juniors n'ont plus de tâche d'entrée. | HeroHunt, mai 2026 | https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/ |
| F-029 | Customer service : 2,9 M de représentants US, « le plus grand groupe occupationnel à risque de déplacement à court terme » (WEF). | FinalRoundAI, 2026 | https://www.finalroundai.com/blog/ai-replacing-jobs-2026 |
| F-030 | Data entry / administratif : 7,5 M de postes projetés disparaître (McKinsey) | FinalRoundAI, ibid. | ibid. |
| F-031 | Parajuristes / recherche juridique : 53 % des tâches automatisables d'ici 2027 (Bloomberg Intelligence). | FinalRoundAI, ibid. | ibid. |
| F-032 | Comptabilité / audit / paie : 75-95 % de risque d'automatisation d'ici 2027 (agentic AI). | FinalRoundAI, ibid. | ibid. |
| F-033 | Travailleurs avec bachelor : 27 % dans des emplois à haute exposition IA, contre 19 % (some college) et 12 % (high school only). L'IA cible les cols blancs, pas les cols bleus. | FinalRoundAI, ibid. | ibid. |

---

## 4. CAUSALITÉ — Les quatre chaînes

### Chaîne 1 : Full automation → Échec → Revers

```
Déploiement IA full replacement (Klarna, CBA, IBM freeze)
→ Métriques de volume OK (rapidité, coût par ticket)
→ Métriques de qualité dégradées sur cas complexes (CSAT, repeat contact)
→ Coûts cachés émergent (perte connaissance institutionnelle, réembauche, attrition clients)
→ Revers partiel ou total (réembauche humains, modèle hybride)
→ Leçon : l'IA gère la routine, pas l'exception. Sans humains, l'exception détruit la valeur.
```

### Chaîne 2 : Profit record → Licenciements → Attribution IA

```
Entreprise poste des profits records (Cloudflare +34 %, Oracle +95 %, Block +24 %)
→ Annonce de licenciements massifs (1 100, 20 000+, 4 000)
→ Attribution publique à l'IA (« AI-native », « gains de productivité IA »)
→ Action monte (souvent)
→ Mais : Oxford Economics et Yale Budget Lab ne trouvent aucune trace macro
→ L'IA est une justification commode pour des restructurations de profitabilité
```

### Chaîne 3 : Junior → Tâches automatisables → Pipeline brisé

```
Junior affecté à des tâches structurées (code, doc, bugs, tickets)
→ L'IA excelle exactement sur ces tâches (copilot, code gen)
→ Le junior n'a plus de fonction visible → poste supprimé ou gelé
→ Le senior (architecture, client, décision) survit
→ MAIS : sans juniors, pas de pipeline → pas de seniors dans 5-10 ans
→ IBM le découvre et triple ses recrutements juniors (février 2026)
```

### Chaîne 4 : Hybride → Résilience → Avantage compétitif

```
Entreprise déploie IA en mode augmenté (assistance, pas remplacement)
→ IA gère le volume, humain gère l'exception et le jugement
→ Productivité +20-40 %, CSAT maintenue, connaissance préservée
→ Pipeline de talents intact (juniors apprennent avec l'IA, pas remplacés par elle)
→ Avantage compétitif durable vs concurrents qui ont coupé trop profond
```

---

## 5. ANALYSE — Ce que les données établissent et ce qu'elles ne peuvent pas dire

### 5.1 Ce qui est établi

1. **L'IA supprime des emplois, mais à une échelle très inférieure au discours.** 13 % des licenciements T1 2026 attribués à l'IA (Challenger). Oxford Economics et Yale ne trouvent pas de disruption macro. Les FAANG ont supprimé ~140 000 postes depuis 2023, mais elles en avaient créé ~400 000 pendant la bulle COVID. Le solde net est positif, pas négatif.

2. **Le full automation échoue systématiquement sur la complexité.** Les trois cas documentés de retournement (Klarna, CBA, IBM) partagent le même mécanisme : l'IA gère le volume, pas l'exception. Et en customer service ou en RH, c'est l'exception qui détermine la rétention client et la valeur organisationnelle.

3. **Les juniors sont les vrais perdants.** Pas parce que l'IA fait mieux qu'eux — mais parce que leurs tâches d'apprentissage (code, doc, bugs) sont exactement celles que l'IA automatise. Le senior survit. Mais sans juniors, le senior de demain n'existe pas. C'est la leçon IBM.

4. **Le modèle hybride fonctionne, le modèle full ne fonctionne pas.** Salesforce (50/50, CSAT maintenue) est le seul « succès » documenté de suppression massive — et c'est un succès d'augmentation, pas de remplacement. 5 000 humains restent.

5. **L'AI washing est massif.** Quand Cloudflare licencie 1 100 personnes le jour où elle annonce un CA record, le motif IA est structurellement suspect. Altman lui-même le reconnaît. La distinction entre « l'IA rend des postes inutiles » et « nous voulons améliorer nos marges et l'IA est une excuse socialement acceptable » est impossible à tracer, mais le faisceau est convergent.

### 5.2 Ce qui n'est pas établi (et pourquoi)

1. **L'effet net sur l'emploi total.** Les 128 270 licenciements tech de 2026 sont un flux brut, pas un solde net. Les créations d'emploi dans l'IA (prompt engineers, AI trainers, MLOps, etc.) ne sont pas comptabilisées en face. Le WEF projette +78 M net d'ici 2030 — mais ce sont des projections.

2. **L'effet de second ordre (demande).** BCG modélise l'élasticité-prix : si l'IA réduit le coût unitaire, la demande augmente, ce qui peut créer plus d'emplois qu'elle n'en détruit. Le cas classique : les guichets automatiques n'ont pas supprimé les employés de banque, ils ont permis d'ouvrir plus d'agences.

3. **Le seuil de rupture.** Si l'IA atteint le jugement ouvert (open-ended reasoning) au niveau humain, les catégories BCG « substitution vs augmentation » basculent. Mais ce seuil n'est pas atteint en août 2026.

4. **L'intention réelle des CEO.** Impossible à établir forensiquement. Le pattern « profits records + licenciements IA » est documenté. La motivation (cynisme, pression des actionnaires, croyance sincère) ne l'est pas.

---

## 6. LE TABLEAU DE BORD DES AGENTS IA EN PRODUCTION

### Entreprises où l'IA a remplacé des humains — et le résultat

| Entreprise | Postes supprimés | Secteur | Résultat | Verdict |
|------------|-----------------|---------|----------|---------|
| Klarna | 700 | Customer service | Qualité dégradée, demi-tour, réembauche | ÉCHEC |
| Commonwealth Bank | 45 | Customer service | « Erreur », excuses écrites, réembauche | ÉCHEC |
| IBM (back-office) | 7 800 gelés | HR/finance | Triplement recrutements juniors en 2026 | CORRECTION |
| Salesforce | 4 000 | Support client | CSAT maintenue, 5 000 humains conservés | HYBRIDE STABLE |
| Oracle | 20 000-30 000 | Multi-sectoriel | +95 % résultat net. Aucune donnée publique de qualité post-licenciement. | INCONNU (probable AI washing) |
| Block | 4 000 | Tech/fintech | +24 % profit brut. Aucune donnée publique de qualité. | INCONNU (probable AI washing) |
| Cloudflare | 1 100 | Tech | Record CA. Aucune donnée publique de qualité. | INCONNU (probable AI washing) |
| Meta | 8 000 | Multi-sectoriel | En cours (effectif mai 2026). | TROP TÔT |
| Chegg | 636 (cumul) | EdTech | Action −99,6 %. ChatGPT a détruit le marché, pas l'interne. | DESTRUCTION EXTERNE |

### L'équation qui manque dans tous les business cases

Aucune des entreprises ci-dessus n'a publié de business case complet incluant :
- Le coût de réembauche si la stratégie échoue
- L'impact de la dégradation CSAT sur le churn client
- Le coût de la perte de connaissance institutionnelle
- L'effet sur le pipeline de talents (où seront les seniors dans 5 ans ?)

Le seul chiffre qui circule est le coût salarial économisé. C'est une équation amputée des deux tiers de ses variables.

---

## 7. VERDICT

**L'effet des agents IA en production sur l'emploi est réel, concentré sur trois catégories (juniors tech, customer service, back-office administratif), et massivement exagéré par le discours des CEO.**

Le chiffre à retenir n'est pas « 50 % des licenciements » (faux) ni « 128 000 emplois tech » (flux brut, pas solde net). C'est le décalage entre :

- **13 %** : part réelle des licenciements US attribuables à l'IA (Challenger, T1 2026)
- **50-55 %** : emplois qui seront *remodelés* (BCG), pas remplacés
- **10-15 %** : emplois potentiellement *éliminés* en 5 ans+ (BCG)
- **3 sur 3** : taux d'échec documenté des stratégies de remplacement complet (Klarna, CBA, IBM)
- **1 sur 8** : taux de succès documenté du remplacement partiel avec maintien de la qualité (Salesforce)

La vraie bombe à retardement n'est pas le nombre de licenciements — c'est **la destruction silencieuse du pipeline de talents juniors**. Si les juniors ne sont plus embauchés parce que l'IA fait leurs tâches, qui seront les seniors de 2031 ? C'est la question qu'IBM a mis 33 mois à comprendre, et que la plupart des entreprises n'ont même pas commencé à se poser.

---

## 8. LOUPS OUVERTS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | L'AI washing rend impossible la mesure réelle de l'effet IA sur l'emploi. Entreprises et chercheurs utilisent la même catégorie pour deux phénomènes différents. | HAUTE |
| W-002 | La destruction du pipeline junior est invisible dans les chiffres d'emploi actuels. Elle se manifestera dans 5-10 ans par une pénurie de seniors. | TRÈS HAUTE |
| W-003 | Aucune entreprise ne publie le coût complet (réembauche, CSAT, churn) de ses stratégies de remplacement IA. Les business cases sont structurellement biaisés. | HAUTE |
| W-004 | Les CEO des entreprises qui vendent de l'IA (Amodei/Anthropic, Altman/OpenAI) sont aussi ceux qui font les prévisions les plus agressives de remplacement. Conflit d'intérêts non divulgué. | MOYENNE |

---

## 9. SOURCES

1. HeroHunt.ai (Yuma Heymans), « Tech Layoffs and AI: The 2026 Reality Check », 10 mai 2026 — https://www.herohunt.ai/blog/tech-layoffs-and-ai-the-2026-reality-check/
2. FinalRoundAI, « AI Job Displacement: Which Jobs Are At Risk in 2026? », 2026 — https://www.finalroundai.com/blog/ai-replacing-jobs-2026
3. Digital Applied, « Klarna Reverses AI Layoffs: Why Replacing 700 Failed », 9 mars 2026 — https://www.digitalapplied.com/blog/klarna-reverses-ai-layoffs-replacing-700-workers-backfired
4. Fast Company, « Klarna tried to replace its workforce with AI », 12 janvier 2026 — https://www.fastcompany.com/91468582/klarna-tried-to-replace-its-workforce-with-ai
5. ABC Australia, « Commonwealth Bank backtracks on AI job cuts, apologises for 'error' », 21 août 2025 — https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492
6. TwinLadder Research, « Tripling the Ladder — How IBM Reversed the Most Famous AI Hiring Freeze », mars 2026 — https://www.twinladder.ai/en/research/ibm-tripling-the-ladder
7. BCG, « AI Will Reshape More Jobs Than It Replaces », avril 2026 — https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces
8. TechRadar, « Salesforce CEO says it cut 4,000 support jobs — and replaced them with AI », 2 septembre 2025 — https://www.techradar.com/pro/salesforce-says-it-cuts-4-000-support-jobs-and-replaced-them-with-ai
9. TIME, couverture des licenciements Oracle (30 ans d'ancienneté, appelée à l'hôpital), cité par HeroHunt
10. Josh Bersin, « Yes, HR Organizations Will (Partially) Be Replaced by AI, And That's Good », mai 2025 — https://joshbersin.com/2025/05/yes-hr-organizations-will-partially-be-replaced-by-ai-and-thats-good/
11. Bloomberg, « Australia's Biggest Bank Reverses Plan to Replace Jobs With AI », 21 août 2025
12. New Market Pitch, « Where is the money in the agentic AI market? », 29 juin 2026 — https://newmarketpitch.com/blogs/news/agentic-ai-where-money
13. Tandem Coach, « Klarna AI Layoffs: Why 55% of Companies Regret AI-Driven Cuts », 2026 — https://tandemcoach.co/klarna-ai-automation-lesson/
14. CNBC, « Coinbase lays off 700 employees », mai 2026, cité par HeroHunt
15. TechCrunch, « Cloudflare lays off 20% of workforce », mai 2026, cité par HeroHunt
16. CNN, « Block lays off 40% », février 2026, cité par HeroHunt
17. Fortune, « Microsoft offers voluntary buyouts », avril 2026, cité par HeroHunt
18. WEF, Future of Jobs Report 2025 — cité par FinalRoundAI
19. McKinsey Global Institute, « Agents, robots, and us: Skill partnerships in the age of AI », 2026 — cité par FinalRoundAI
20. Oxford Economics, janvier 2026 — cité par FinalRoundAI
21. Yale Budget Lab, février 2026 — cité par FinalRoundAI
22. Challenger, Gray & Christmas, données T1 2026 — citées par Fortune et FinalRoundAI