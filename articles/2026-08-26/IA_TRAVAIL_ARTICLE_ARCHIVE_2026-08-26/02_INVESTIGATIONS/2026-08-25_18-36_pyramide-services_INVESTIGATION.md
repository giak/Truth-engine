# INVESTIGATION — La pyramide des services sous IA

**Date :** 2026-08-25  
**Investigation ID :** `INV-SERVICEPYR-001`  
**Protocole :** RENARD CORE V3  
**Périmètre :** conseil/ESN, Big Four audit-conseil, cabinets d'avocats.  
**Objet :** tester si l'IA creuse déjà la base des organisations de services professionnels ou si elle recompose plutôt la pyramide, l'apprentissage, les prix et les rôles.

## [DECOMPOSE]

| Atom | Sous-affirmation | Source tier requis | Verdict initial |
|---|---|---:|---|
| P1 | Les recrutements juniors se contractent plus vite que l'effectif total | T1-T2 | OPEN |
| P2 | Cette contraction est principalement causée par l'IA | T1-T2 | OPEN |
| P3 | Les tâches juniors routinières sont automatisées | T1-T2 | OPEN |
| P4 | Les firmes reconstruisent volontairement la formation des juniors | T1-T2 | OPEN |
| P5 | La pyramide tend vers un cylindre, davantage de mid/seniors et moins d'entrants | T1-T2 | OPEN |
| P6 | L'IA augmente déjà utilisation, taux journaliers et marge | T1 | OPEN |
| P7 | Le modèle de facturation bascule du temps vers le résultat | T1-T2 | OPEN |
| P8 | De nouveaux rôles IA créent une couche intermédiaire de spécialistes | T1-T2 | OPEN |

## [SHADOW]

| Atom | Trace si H vraie | Trace si H fausse | Discriminant |
|---|---|---|---|
| P1 | intake junior ↓ beaucoup plus vite que headcount | cohortes stables/↑ | Y |
| P2 | baisse post-déploiement plus forte dans firmes/métiers IA, autres causes contrôlées | marché/conjoncture explique mieux | Y |
| P3 | research/draft/review/test/documentation automatisés | juniors gardent les mêmes tâches | Y |
| P4 | formation, apprentissage et tâches conservées/reconstruites explicitement | aucune compensation institutionnelle | Y |
| P5 | ratio junior/mid ↓ et seniority ↑ | pyramide stable | Y |
| P6 | AI share ↑ avec utilisation/rates/marge ↑ | aucune amélioration agrégée | Y |
| P7 | contrats outcome/value/subscription ↑ | hour/day billing reste dominant | Y |
| P8 | AI lawyer/legal engineer/AI delivery ↑ | suppression nette sans nouvelle couche | Y |

## Résultat exécutif

> **La pyramide ne s'effondre pas encore uniformément. Elle commence à devenir plus sélective à sa base, plus technologique au milieu et plus consciente que ses tâches de formation sont menacées.**

Le signal le plus robuste n'est pas « plus de juniors ». Il est :
`moins de tâches routinières par junior + recrutement plus sélectif + formation plus explicite + nouveaux rôles IA + pression progressive sur le temps facturable`.

Le droit fournit le signal structurel le plus clair : l'étude Citi/Hildebrandt rapportée par Reuters indique que 86% des grands cabinets interrogés prévoient encore d'augmenter leur nombre d'associates d'ici 2027, mais seulement environ un tiers prévoit de faire croître les cohortes d'entrée ou de summer associates. Le modèle envisagé ressemble davantage à un **cylindre** qu'à la pyramide historique.

## 1. Le mécanisme économique de la pyramide

### Modèle traditionnel

```text
PARTNERS
    ▲
SENIORS / MANAGERS
    ▲
JUNIORS nombreux
    ▲
travail répétitif facturable
```

La base remplit quatre fonctions en même temps :
1. produire à coût salarial inférieur ;
2. fournir du levier économique aux seniors/partners ;
3. absorber les gros volumes de recherche, revue, test, documentation ;
4. fabriquer les professionnels expérimentés de demain.

L'IA attaque précisément les tâches qui réalisaient simultanément ces quatre fonctions.

### Modèle émergent, encore hypothétique

```text
PARTNERS / EXPERTS
        ▲
MIDS / SENIORS + AI SPECIALISTS
        ▲
JUNIORS plus sélectifs
        ▲
IA / agents / knowledge systems
```

Le risque principal n'est donc pas simplement un étage en moins. C'est la **désynchronisation entre production et apprentissage**.

## 2. Conseil et ESN : pas de disparition de la base, mais une économie du levier sous tension

### Wavestone, notre meilleur thermomètre français

2025/26 :
- chiffre d'affaires : 954,3 M€ ;
- IA : 17% du chiffre d'affaires, contre 8% un an plus tôt ;
- taux d'utilisation : 72%, contre 73% ;
- taux journalier moyen : 938 €, contre 939 € ;
- 6 111 salariés, contre 6 076 ;
- environ 900 recrutements bruts ;
- turnover 12%.

Au T1 2026/27, le taux d'activité tombe à 71% et le taux journalier moyen à 926 €, soit -1.3% par rapport aux 938 € de l'exercice précédent.

**DELTA :** la part de revenu liée à l'IA a plus que doublé, sans produire dans les agrégats une hausse visible de l'utilisation ni du prix journalier. Wavestone dit même que le taux d'utilisation a été insuffisant et que le ratio prix de vente/salaire s'est légèrement dégradé.

Cela ne prouve pas que l'IA dégrade les taux. Cela réfute simplement :
> « plus de business IA = gain de productivité immédiatement capturé par le cabinet ».

### Sopra Steria, contre-exemple frontal

En 2026, Sopra Steria annonce plus de 8 500 recrutements mondiaux pour industrialiser notamment l'IA. En France :
- 3 400 CDI ;
- 500 stages ;
- 500 alternances.

En Inde, environ 250 diplômés sont prévus.

La base de la pyramide n'est donc pas universellement supprimée. Certaines ESN **augmentent ou maintiennent volontairement leurs pipelines d'entrée pour construire les compétences nécessaires à l'industrialisation**.

### Capgemini et Accenture : repondération plutôt qu'effondrement démontré

Capgemini baisse organiquement de 5 800 personnes entre fin 2025 et juin 2026 malgré la hausse consolidée liée à WNS. Onshore et offshore baissent tous deux. La restructuration est réelle, l'IA est un axe stratégique fort, mais les données publiques ne donnent pas encore la distribution junior/mid/senior.

Accenture affiche au contraire 779 000 employés contre 774 000 et un taux d'utilisation stable à 92%. L'entreprise ajuste explicitement ses embauches et son attrition selon la demande, tout en portant sa population AI/data à ~77 000 et en réalisant ~97 000 promotions.

**Verdict conseil/ESN :** la pyramide se recompose par compétence et demande, mais le dossier ne permet pas encore de parler de « disparition des juniors ».

## 3. Big Four : l'endroit où le paradoxe de formation devient visible

### Deloitte UK : le signal quantitatif le plus inquiétant

Entre FY23 et FY25 :
- recrutements d'entrée : 2 767 → 1 908, soit **-31.0%** ;
- FTE salariés : 26 503 → 25 205, soit **-4.9%** ;
- dépenses de formation par FTE : £1 980 → £2 473, soit **+24.9%** ;
- heures de formation/FTE : 27 → 35, soit **+29.6%** ;
- promotions partner/director : 501 → 341, soit **-31.9%**.

La base d'entrée se contracte donc beaucoup plus vite que l'effectif salarié.

**Mais la pièce primaire interdit d'en conclure « IA ».** Deloitte attribue explicitement le fort recul FY24 aux conditions de marché et dit que FY25 connaît des conditions similaires. La baisse des promotions partner/director montre en outre une compression plus large de la carrière.

### PwC : une entreprise qui choisit de ne pas automatiser au maximum

PwC UK reçoit environ 60 000 candidatures pour 2 000 places d'entrée, environ **30 candidatures par place**.

Surtout, la direction explique avoir choisi de **conserver certaines tâches routinières** plutôt que de les automatiser ou les externaliser, afin que les juniors apprennent à exercer jugement et esprit critique.

Le reporting de formation renforce ce point :
- associates : 102 heures de formation moyenne ;
- senior associates : 41 heures ;
- managers : 25 heures ;
- partners : 20 heures.

L'organisation traite donc déjà le risque que nous avions identifié : si l'IA retire les tâches d'entrée, il faut reconstruire explicitement l'apprentissage.

### EY et KPMG : le sas d'entrée persiste

EY UK accueille en FY25 :
- 1 124 diplômés et school leavers ;
- plus de 450 stagiaires ;
- 764 des entrants rejoignent l'audit.

KPMG continue d'opérer des routes diplômés/apprentis structurées ; en 2024 le cabinet avait créé environ 1 000 opportunités étudiants. En 2025, l'IA est désormais « dans les mains de chaque auditeur » britannique, sans suppression publique du pipeline d'entrée.

**Verdict Big Four :** signal de compression réelle chez Deloitte, mais contre-exemples et reconstruction institutionnelle suffisamment forts pour tuer une causalité simple IA→juniors.

## 4. Droit : la transition « pyramide → cylindre » est la plus explicite

Reuters rapporte le scénario Citi/Hildebrandt :
- 86% des cabinets prévoient de faire croître les associates d'ici 2027 ;
- seulement environ un tiers prévoit d'augmenter les cohorts entry-level/summer ;
- 63% anticipent une évolution du staffing model à l'horizon 2035.

Ce n'est pas une extinction des associates. C'est un **déplacement du centre de gravité vers les profils intermédiaires et seniors**.

### A&O Shearman : le test causal le plus propre

Harvey documente :
- ~4 000 utilisateurs ;
- 2 à 3 heures économisées par semaine sur tâches routinières ;
- ~2 000 utilisateurs quotidiens de ContractMatrix ;
- temps de revue contractuelle réduit de 30%, jusqu'à environ 7 heures gagnées par revue.

Les tâches visées sont exactement :
- synthèse ;
- analyse ;
- traduction ;
- première rédaction ;
- revue de clauses ;
- recherche de précédents.

Ce sont aussi des tâches traditionnellement formatrices et facturables par les juniors.

A&O transforme en plus cette productivité en produit SaaS, puis en agents tarifés par abonnement ou usage, avec partage de revenus logiciels.

La firme donne donc la chaîne :
`tâche junior automatisable → expertise incorporée → logiciel → nouvelle source de revenu`.

**Ce qui manque :** le ratio trainees/associates/seniors avant/après. Sans lui, il serait abusif d'écrire qu'A&O a déjà détruit sa base junior.

### Clifford Chance : adoption >90% sans preuve de creusement de base

Clifford Chance déclare une adoption IA supérieure à 90% et des gains d'efficacité/rapidité. Parallèlement, FY26 est record :
- revenu +9% ;
- profit partnership +11% ;
- PEP +9%.

Mais deal cycle, expansion régionale et latéraux confondent toute attribution du profit à l'IA. Les contrats de formation continuent.

### Linklaters : naissance d'un nouvel étage

Linklaters déploie Legora firmwide, puis crée :
- une équipe mondiale de 20 **AI Lawyers** ;
- une équipe **Applied Intelligence** réunissant avocats et data scientists.

Cela contredit une représentation purement destructive :

```text
junior supprimé
→ logiciel
```

Le système réel peut devenir :

```text
junior / associate
        +
AI Lawyer
        +
data scientist
        +
senior lawyer
```

La pyramide acquiert une **couche latérale technico-professionnelle**.

### Freshfields : adoption très profonde, effet pyramidal encore non observable

Freshfields met Claude à disposition de 5 700 personnes ; plus de 5 000 professionnels utilisent les outils bâtis avec Gemini et plus de 2 100 utilisent régulièrement NotebookLM. La firme a constitué 260 AI Champions.

C'est une adoption profonde.

Mais aucune donnée publique consultée ne permet de relier cette adoption à une chute des trainees ou à un nouveau ratio d'associates.

**ABSENCE DE PREUVE != ABSENCE D'EFFET.**

## 5. Le principal biais causal : le marché junior s'effondre aussi hors IA

Au Royaume-Uni, les vacances graduate recensées par Adzuna tombent à 8 383 en juillet 2026, **-45,6% sur un an**, au plus bas depuis le début de la série en 2016.

Les causes citées incluent :
- ralentissement économique ;
- hausse des coûts salariaux/fiscaux ;
- incertitude ;
- automatisation et IA.

C'est un base rate critique.

Chaque baisse de recrutement junior chez Deloitte, PwC, un cabinet de conseil ou un cabinet d'avocats doit donc être comparée à **ce marché général déjà très dégradé**.

## 6. La vraie bombe : production et apprentissage n'ont plus la même fonction économique

Historiquement, une tâche junior pouvait être simultanément :
- lente ;
- peu rentable ;
- répétitive ;
- mais nécessaire pour apprendre.

L'IA sépare ces deux fonctions.

```text
TÂCHE ROUTINIÈRE
      │
      ├── valeur productive → IA peut la capter
      │
      └── valeur pédagogique → doit être recréée ailleurs
```

Le gain privé immédiat dit :
> automatisons.

Le besoin collectif à cinq ans dit :
> comment fabriquons-nous les experts ?

C'est une **externalité de formation** potentielle.

Une firme peut rationnellement supprimer les tâches formatrices aujourd'hui et bénéficier demain de seniors formés par d'autres. Si toutes les firmes font pareil, le système entier sous-investit dans la fabrication de l'expertise.

Ce mécanisme mérite une enquête économique et juridique autonome.

## 7. La pyramide des services devient peut-être un « cylindre sélectif »

Le modèle le plus compatible avec les preuves actuelles est :

```text
               EXPERTS / PARTNERS
              ───────────────────
                  MIDS / SENIORS
              ───────────────────
        AI LAWYERS / DATA / ENGINEERS
              ───────────────────
           JUNIORS MOINS NOMBREUX ?
            MAIS PLUS SÉLECTIONNÉS
              ───────────────────
          IA / KNOWLEDGE SYSTEMS
```

Le point d'interrogation est volontaire.

Nous avons des signaux sectoriels, pas encore le ratio longitudinal permettant de le transformer en fait général.

## 8. Pricing : le vieux levier du jour facturé ne s'est pas encore effondré

L'enquête précédente montrait déjà que les services IT indiens commencent à déplacer certains contrats du time-and-materials vers l'outcome/performance.

Mais le panel actuel empêche toute généralisation rapide :
- Wavestone : TJM pratiquement stable en FY25/26 malgré le doublement de la part IA, puis -1,3% au T1 suivant ;
- droit : les clients attendent de nouveaux modèles, mais la tarification horaire reste encore résistante ;
- A&O crée un modèle réellement alternatif : **SaaS + abonnement/usage**.

La rupture tarifaire pourrait donc commencer par **une seconde couche de revenus logiciels**, avant de supprimer le jour/horaire historique.

## [ADVERSARY]

| Axe | H prediction | Rival prediction | Observation | Favorise |
|---|---|---|---|---|
| Juniors | IA fait chuter partout les cohorts | demande/macro/institutions dominent encore | Sopra, EY, KPMG, PwC maintiennent de gros pipelines | Rival |
| Deloitte | -31% intake prouve IA | marché global faible | Deloitte attribue explicitement la baisse aux conditions de marché | Rival |
| Tâches formatrices | automatisation sans coût pédagogique | firmes doivent reconstruire formation | PwC conserve des tâches; KPMG/EY renforcent formation | H apprentissage |
| Law | base disparaît | pyramide devient cylindre | 86% associates ↑, ~1/3 seulement entry ↑ | H cylindre |
| Prix | IA fait monter utilisation/rates | gain non capturé ou marché faible | Wavestone AI share ↑ mais utilisation/rate non ↑ | Rival |
| Nouveaux rôles | IA remplace | IA crée couche spécialiste | Linklaters AI Lawyers/Applied Intelligence | Rival au remplacement pur |
| Profit law | AI fait exploser PEP | cycle deals/rates/laterals expliquent | profits records, causalité AI non isolée | Neutral |

## [EVALUATE]

| Hypothèse | Statut | Confiance |
|---|---|---:|
| Effondrement uniforme de la base junior causé par l'IA | **WEAKEN** | 0.91 |
| Pyramide plus sélective / tendance au cylindre | **STRENGTHEN** | 0.94 |
| Paradoxe d'apprentissage | **SUPPORTED FORT** | 0.95 |
| Gain IA déjà visible dans rates/utilisation/marges | **WEAKEN** | 0.93 |
| Facturation temps → résultat | **SUPPORTED SECTORAL** | 0.89 |
| Nouvelle couche AI specialists | **STRENGTHEN** | 0.94 |
| Chute actuelle des juniors principalement causée par IA | **WEAKEN** | 0.96 |

**EPISTEMIC_LEDGER** := verified: 4 | supported: 5 | disputed/open: 4 | refuted: 0

## [REPORT]

| Field | Content |
|---|---|
| what_changed_since_last | La « pyramide » devient deux objets : pyramide d'effectifs et pyramide d'apprentissage. Les deux peuvent diverger. |
| surviving_H | tâches juniors comprimées; sélection accrue; nouveaux rôles spécialistes; pression graduelle sur facturation; risque de sous-investissement collectif dans la formation |
| killed_H | « l'IA a déjà détruit uniformément la base des services »; « moins de graduates = preuve IA »; « gains IA apparaissent déjà automatiquement dans rates/marges » |
| confidence_before -> confidence_after | modèle du cylindre sélectif : 0.55 → 0.91 |
| next_priority | reconstruire **ratios par grade 2022-2026**, heures facturables et tâches formatrices dans 8-12 firmes France/Europe |
| CALIBRATION | robuste sur mécanismes; insuffisant pour quantifier une baisse nette des juniors causée par l'IA |

## Gaps P0

1. **SENIORITY_LEDGER** : junior / consultant / manager / senior / partner par année 2022-2026.
2. **FORMATIVE_TASK_LEDGER** : heures de recherche, revue, draft, test, documentation réellement réalisées par juniors avant/après IA.
3. **GRADE_ECONOMICS** : taux d'utilisation, tarif/jour ou taux horaire, coût salarial et marge par grade.
4. **FRANCE_CONTROL** : reproduire les observations Big Four / droit en France, les données UK servant ici de laboratoire mieux documenté.
5. **AI_SPECIALIST_LAYER** : quantifier AI lawyers, legal engineers, data scientists, AI delivery et leur origine de recrutement.
6. **CLIENT_PRICING** : contrats réels time-and-materials vs fixed/outcome/value/SaaS.
7. **TRAINING_EXTERNALITY** : tester économiquement le risque de passager clandestin dans la formation des futurs seniors.

## Verdict

> **L'IA ne fait pas encore disparaître la pyramide des services. Elle commence à retirer certaines briques qui rendaient cette pyramide économiquement rentable et pédagogiquement reproductible.**

Le risque de court terme est une base plus étroite.

Le risque de moyen terme est plus subtil :

> **que les firmes sachent encore produire le travail, mais ne sachent plus produire les experts capables de le contrôler.**
