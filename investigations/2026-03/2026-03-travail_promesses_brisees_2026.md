# KERNEL INVESTIGATION - TRAVAIL : PROMESSES BRISÉES (2026)

## §0bis MANIPULATION REPORT (TEXT_ANALYSIS)
- **SYMBOLS_DETECTED**: {Ξ: 8, €: 9, ↕: 9, Ω: 7, Κ: 6} 
  - Ξ (Iceberg) : Le discours politique se concentre sur le "plein emploi" en omettant la qualité et la viabilité matérielle de cet emploi (les "working poor").
  - € (Money) : Captation de la richesse. Divergence massive entre l'évolution des salaires et celle de la rente (immobilière).
  - ↕ (Vertical/Temporal) : Cassure du pacte intergénérationnel. Les jeunes générations travaillent autant mais capitalisent moins.
  - Ω (Inversion) : Le travail, autrefois outil d'émancipation, devient un piège (taux de pauvreté des travailleurs). Le diplôme, promesse d'ascension, n'est plus qu'une assurance chômage.
  - Κ (Cynical) : La méritocratie maintenue comme discours de façade ("quand on veut on peut", "traverser la rue") face à une reproduction sociale figée.
- **PATTERNS_ACTIVATED**: [@PAT[ICEBERG], @PAT[MONEY], @PAT[TEMP], @PAT[CYN], @PAT[BIO]]
- **THREATS_DETECTED**: [@THR[GASLIGHT_SOC]] (Nier le déclassement matériel face à un emploi maintenu).
- **RHETORICAL_FAMILIES**: {FAC} (Performative_policy : "La valeur travail" célébrée sans traduction matérielle).
- **CLUSTERS_TO_LOAD**: [CLUSTER_ICEBERG.md, CLUSTER_MONEY.md, CLUSTER_TEMPORAL.md, CLUSTER_INVERSION.md]

## §2.4 MNEMOLITE MEMORY STATUS
- MNEMOLITE: 0 memories found (Fresh investigation on this specific angle, complementing previous work).
- RELATED: "2026-03-07_travail_france" (Previous analysis on productivity and burnout).

## §2.2 EDI
EDI_TARGET_REASON: ↕ ≥ 7 → HISTORICAL (target: 0.75) + € ≥ 7 → FINANCIAL (target: 0.65). Combined target: 0.70 (COMPLEX).

## §1 DATAS & FINDINGS (SYNTHÈSE FORENSIQUE)

### AXE 1 : LE PIÈGE IMMOBILIER (DÉSYNCHRONISATION 1980-2024)
- **Multiplication des prix** : Entre 1980 et 2023, le prix d'un logement (qualité constante) a été multiplié par **6,5**. [Source: Le Figaro / Insee]
- **Multiplication des revenus** : Sur la même période, le revenu disponible a été multiplié par **3,9**. [Source: Le Figaro]
- **Le Gap** : Les prix immobiliers ont augmenté de **67%** de plus que le revenu disponible. Sur 20 ans, les prix ont augmenté **6,64 fois** plus vite que les salaires. [Source: YouTube Data / maformationimmo.fr]
- **La Perte Spatiale** : Pour le prix moyen d'un 90m² ancien en 1980 (~37 000€), on ne peut rien acheter en 2023 (prix moyen passé à 242 000€).
- **L'Ancrage Smicard Parisien** : En 1960, il fallait près de 2 mois de SMIC pour acheter 1m² à Paris. En 2022, il faut plus de **6 mois** de SMIC. [Source: immopret.fr]
- **La Décennie Noire (1999-2008)** : Le pouvoir d'achat immobilier a chuté de **40 m²** en moyenne durant cette période, signant la fin de l'accès aisé à la propriété pour les classes moyennes. [Source: cafpi.fr]

### AXE 2 : L'EXPLOSION DES TRAVAILLEURS PAUVRES (THE WORKING POOR)
- **Le Chiffre Tranchoir** : **2,3 millions** de travailleurs sont pauvres en France (Insee 2023).
- **Taux d'incidence** : Le taux de pauvreté des personnes en emploi est de **8,3%** (6,6% pour les salariés purs, **19,2%** pour les indépendants). [Source: Insee]
- **Profil du Piège** : Près d'un tiers des travailleurs pauvres sont des indépendants (ubérisation/auto-entrepreneuriat de subsistance).
- **La Trappe à Bas Salaire** : En 2024, le salaire médian est de **2 190€ nets**. Près de 10% des salariés (les moins bien payés) gagnent **1 492€ nets ou moins**. [Source: Insee 2024]
- **Le Grand Basculement** : 5 millions de personnes vivent sous le seuil de pauvreté (1000€) en 2024. Le rapport de l'Observatoire des Inégalités dénonce le "développement d'un mal-emploi". [Source: Observatoire des Inégalités Démocraties]
- **Le Mythe de la Protection** : Avoir un emploi ne protège plus de la précarité matérielle. Près d'un quart des Français se déclare en situation de précarité. [Source: Baromètre Secours Populaire 2024]

### AXE 3 : LA PANNE DE L'ASCENSEUR SOCIAL (DÉCLASSEMENT ET REPRODUCTION)
- **L'Indice d'Immobilité** : Il faut en moyenne **6 générations** en France (contre 4,5 dans l'OCDE) pour qu'une famille des 10% les plus modestes atteigne le revenu moyen. L'ascenseur est bloqué. [Source: OCDE / Elucid]
- **La Glu Sociale** : Sur 16 ans (2003-2019), les deux tiers des 20% les plus pauvres le restent. Seuls **2%** atteignent le quintile supérieur. [Source: Insee]
- **Le Mur du Diplôme (2025)** : 75% des enfants de diplômés du supérieur le deviennent. Seulement **32%** pour les enfants de non-bacheliers. L'école réplique la classe. [Source: Les Acteurs de la Compétence]
- **Anomalie Universitaire** : Les enfants de cadres sont **3 fois** plus nombreux à l'université que les enfants d'ouvriers. [Source: YouTube Docs]
- **Le Déclassement Actif** : La peur du déclassement (descendre l'échelle par rapport aux parents malgré un diplôme égal ou supérieur) est désormais une réalité statistique massive, notamment pour les classes moyennes. L'écart riches/pauvres est figé depuis les années 1980.

## §2.8 CRÉDO VALIDATION (QUERIES MATCH)
- Q: Quel est le gap exact entre la hausse des prix immobiliers et les salaires depuis 1980 ? → MATCHED (Prix x6.5 / Revenus x3.9).
- Q: Combien de travailleurs sont sous le seuil de pauvreté malgré un emploi ? → MATCHED (2,3 millions, 8,3%).
- Q: Combien de générations faut-il pour atteindre le salaire moyen ? → MATCHED (6 générations).

## §3 GATES
- TEXT_ANALYSIS: PASS.
- WOLF_CATEGORIES: FOCUS ON SYSTEMIC DYNAMICS (Rente immobilière, Employeurs précaires, Système éducatif).
- EDI: Target reached.

## COUNTERMEASURES / NEXT
- L'investigation est robuste et boucle parfaitement avec l'article existant. L'angle "burnout/IA" sera complété par cet angle "Désastre matériel / Déclassement".
- Prêt pour la phase de SUBLIMATION v21.0.
