# AUDIT MULTIRÔLE — Article V1 « Quand le travail ne vaut plus son temps »

**Date :** 2026-08-25  
**Gate :** `HOLD_P0`

## Verdict exécutif

Le fond **survit à la contradiction**, mais la V1 n'est pas publiable en l'état.

La thèse la plus robuste est :

> **L'IA peut accroître l'écart entre le temps humain mobilisé et le résultat produit, alors qu'une partie de nos contrats, prix, carrières et droits reste organisée autour du temps de travail.**

Cinq réparations P0 bloquent la publication :
1. citation erronée pour Autor, Levy et Murnane ;
2. citation erronée pour l'étude française sur les robots ;
3. cas Salesforce confondu par l'acquisition d'Informatica ;
4. thèse temps-production-prix-salaire trop équivalente ;
5. contre-preuve BEI 2026 absente.

## Revues indépendantes

| Rôle | Verdict | Finding cardinal | Priorité |
|---|---|---|---|
| Contradicteur épistémologique | **HOLD** | La thèse « temps humain = production = prix = salaire » est historiquement trop forte. | P0 |
| Historien du travail | **REPAIR** | Le fil historique fonctionne mais devient parfois téléologique ; plusieurs régimes de travail coexistent. | P1 |
| Économiste du travail / causalité | **HOLD** | Salesforce est confondu par l'acquisition d'Informatica ; le headcount consolidé ne mesure pas l'embauche organique. | P0 |
| Expert IA / automatisation | **REPAIR** | Le contraste « informatique traditionnelle = règles explicites » efface le machine learning statistique antérieur. | P1 |
| Fact-checker forensique | **HOLD** | Deux citations sont mal branchées : Autor-Levy-Murnane et robots France pointent vers l'OIT 1919. | P0 |
| Juriste travail / protection sociale | **REPAIR** | « Qui possède le temps économisé ? » est une métaphore, pas une notion de propriété juridique. | P1 |
| Statisticien / data reviewer | **REPAIR** | Insee, France Num, BCE et panels ont des populations et définitions différentes. | P1 |
| Rédacteur en chef | **REPAIR** | L'article répète quatre idées structurantes et peut perdre 15 à 20 % sans perdre de preuve. | P1 |
| Avocat du diable pro-IA | **REPAIR** | La thèse adverse de complémentarité durable est forte et doit être exposée loyalement. | P0 |
| Expert communication / AI-washing | **PASS_WITH_GUARDRAILS** | Le risque principal est l'instrumentalisation de formulations sorties de leur calibration. | P1 |
| Sociologue / anthropologue du travail | **PASS_WITH_GAPS** | Le paradoxe junior est solide ; identité et sens du travail peuvent rester hors de cette V2. | P2 |
| Auditeur KISS / exécution | **HOLD** | Toute nouvelle grande enquête avant refactor serait du scope creep. | P0 |
| Gardien de la charte éditoriale | **PASS_WITH_MINOR** | Français et pédagogie solides ; quelques absolus sont à réduire. | P1 |

## P0-1. Autor, Levy, Murnane : régression de source-lineage

Le passage sur les tâches routinières et non routinières est substantiellement correct, mais la V1 pointe vers la Convention n°1 de l'OIT.

**Source correcte :** https://www.nber.org/papers/w8337

## P0-2. Robots français : régression de source-lineage

Même défaut pour Acemoglu, LeLarge et Restrepo.

**Source :** https://www.nber.org/papers/w26738

Le résultat utile reste : les adopteurs peuvent augmenter productivité et emploi propre tout en imposant des pertes d'emploi à d'autres firmes par la concurrence.

## P0-3. Salesforce : le headcount consolidé ne prouve pas l'embauche organique

Salesforce déclare :
- 76 453 salariés au 31 janvier 2025 ;
- 83 334 salariés au 31 janvier 2026.

Mais Salesforce a finalisé l'acquisition d'Informatica le 18 novembre 2025. Informatica déclarait plus de 5 200 salariés à temps plein fin 2024.

Donc :

`+6 881 salariés consolidés != +6 881 embauches organiques`

Ce qui reste défendable :
- contraction importante de la fonction support décrite publiquement ;
- centaines de redéploiements et non-backfill documentés ;
- headcount consolidé en hausse, mais comparaison affectée par M&A.

Sources :
- https://www.sec.gov/Archives/edgar/data/1108524/000110852425000006/crm-20250131.htm
- https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm
- https://www.sec.gov/Archives/edgar/data/1108524/000110852425000207/crm-20251118.htm
- https://www.sec.gov/Archives/edgar/data/1868778/000186877825000007/infa-20241231.htm

## P0-4. Thèse centrale à recalibrer

L'article suggère parfois une équivalence historique :

`temps humain ≈ production ≈ prix ≈ salaire`

Elle n'a jamais été stricte. Capital, productivité, salaire mensuel, forfait, commission, rente et propriété intellectuelle ont toujours produit du découplage.

Formulation recommandée :

> **L'IA étend à certaines tâches cognitives une compression du temps humain déjà ancienne, mais elle peut accélérer le décalage entre temps mobilisé et résultat dans des secteurs dont les prix, contrats et carrières restent fortement indexés sur le temps.**

## P0-5. Contre-évidence BEI à intégrer

Le Working Paper BEI 2026/02 étudie plus de 12 000 firmes UE/États-Unis et estime environ **+4 % de productivité du travail** chez les adopteurs, sans baisse d'emploi détectée à court terme. Les effets de long terme restent ouverts.

**Source :** https://www.eib.org/en/publications/20250383-economics-working-paper-2026-02

Ce résultat ne réfute pas l'article recalibré. Il interdit une lecture catastrophiste.

## Red team de la thèse inverse

La meilleure thèse adverse est :

> **Nous sommes peut-être au début d'une longue phase de complémentarité plus que d'une crise du travail : adoption profonde encore rare, frictions de données, compétences et ROI, temps facturable encore dominant, et premières études de firmes observant surtout de la productivité sans perte nette d'emploi.**

Cette thèse est forte.

L'article lui résiste mieux s'il parle de **décalage institutionnel** et de **distribution du surplus**, pas de « crise imminente ».

## KISS / DRY / YAGNI

Quatre idées sont répétées :
1. emploi != tâche ;
2. technologie != organisation ;
3. temps humain != résultat ;
4. gain de productivité != destination du gain.

Objectif V2 : **-15 à -20 %** sans retirer de preuve.

### Architecture V2

**Acte I. Comment le temps est devenu une unité du travail**  
Thompson → Taylor/Ford → droit du temps → salaire/protection sociale → heure facturable.

**Acte II. Ce que l'IA change réellement en 2026**  
Adoption réelle vs déclarée → tâche vs emploi → cas cardinaux → licenciements IA → temps facturable.

**Acte III. Qui capte la valeur du temps économisé ?**  
Distribution → concurrence → apprentissage junior → modèle social → conclusion.

## Gardes anti-régression

- `EXPOSITION != AUTOMATISATION`
- `ANNONCE IA != CAUSALITÉ IA`
- `SOURCE PRIMAIRE CORPORATE != VÉRIFICATION INDÉPENDANTE`
- `HEADCOUNT CONSOLIDÉ != HEADCOUNT ORGANIQUE`
- `CORRÉLATION != CAUSALITÉ`
- `INTÉRÊT != INTENTION`
- `ABSENCE DE PREUVE != PREUVE D'ABSENCE`

## Gate final

`HOLD_P0`

**Pas de nouvelle grande enquête.**  
Corriger P0/P1, refactorer, puis refaire une passe finale Fact-checker + Économiste du travail + Rédacteur en chef.
