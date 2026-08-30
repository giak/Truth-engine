# XQ203A — Audit post-XQ203 : traçabilité, archéologie documentaire et lisibilité

**Date :** 25 août 2026  
**Nature :** patch de données et de traçabilité uniquement  
**Article XQ203 modifié :** NON  
**SHA-256 article :** `26d902f33a5fcc83a72ae698b879fb41b29fb159c300189b5148757c7af6b456`

## Résultats nouveaux ou corrigés

1. **Yahoo / ×12, 23 juillet 2021** : le texte intégral est récupérable via l’index web. Il explicite que le « ×12 » provient d’une modélisation Pasteur et recommande de ne pas le lire comme une mesure directe de l’efficacité vaccinale sur la transmission. Les deux passages de XQ203 qui disent le corps « non rejouable » sont désormais obsolètes.
2. **Conspiracy Watch, 9 avril 2020** : la compression « fabrication + propagation accidentelle/intentionnelle depuis un laboratoire » reste un cas de périmètre amalgamé.
3. **Conspiracy Watch, 16 avril 2020** : une mise à jour d’un article de mars distingue déjà fuite accidentelle d’un virus naturel et fabrication/arme biologique. C’est l’état le plus précoce actuellement confirmé dans ce corpus, soit 7 jours après le texte du 9 avril.
4. **Conspiracy News #16.2020** : date source corrigée au **20 avril 2020**. L’ancienne valeur du dataset, 18 avril, était erronée.
5. **AFP / Byram Bridle** : la page actuelle confirme une reformulation le 29 juin 2021 de l’avant-dernier paragraphe sur l’ARN messager dans le lait maternel. La formulation antérieure reste non récupérée.
6. **Fact & Furious** : original complet et historique de correction toujours manquants ; adjudication globale interdite.

## Contrôles mécaniques de lecture

- tirets cadratins `—` : **4** -> FAIL par rapport à la contrainte éditoriale ;
- blocs de prose avant les Sources : **235** ;
- médiane : **46 mots** ;
- blocs > 100 mots : **14** ;
- maximum : **290 mots** ;
- figures existantes : **5** ;
- ajout de nouvelles figures par défaut : **REJETÉ** comme overengineering.

## QA mobile des figures

Les cinq SVG ont une largeur de référence de 2 400 px. Les plus petits corps typographiques sont de 22 à 23 px dans le repère SVG. Si la figure entière est affichée à 390 px de large, ces textes tombent mécaniquement à environ **3,58 à 3,74 px CSS**.

Conclusion : le fond graphique n’est pas à multiplier ; les cinq figures existantes doivent être adaptées en mobile-first, typiquement par empilement, réduction du texte secondaire ou variantes dédiées.

## Acronymes / termes à corriger à la première occurrence

P0/P1 identifiés : `CLEMI`, `OMS`, `FDA`, `EMA`, `SEAE`, `HAS`, `OR`, `IC`, `ARNm`, `PCR`.

Règle : définir uniquement ce qui aide réellement un lecteur cultivé non spécialiste ; ne pas transformer l’article en glossaire.

## Cascade d’archéologie documentaire verrouillée

`WEB VIVANT / INDEX -> WAYBACK -> COMMON CRAWL -> BnF -> TRACES INDIRECTES`

Règles négatives :
- `NO_WAYBACK_CAPTURE != PAGE_NEVER_EXISTED`
- `PAYWALL != DONNÉE PERDUE`
- `TRACE_INDIRECTE != SOURCE_PRIMAIRE`
- `ABSENCE_DE_CORRECTION_RETROUVÉE != PREUVE_QU_IL_N_Y_EN_A_JAMAIS_EU`

## Données mises à jour

- `data/XQ200_COVID_ECOSYSTEM_FRESQUE.csv` : F200-004 corrigé au 20/04/2020 ; F200-045 ajouté pour le 16/04/2020.
- `data/XQ200_COVID_CLAIM_AUDIT.csv` : C200-001 contextualisation précoce intégrée.
- `data/QUINTESSENCE_REPAIR_STRENGTH_CASES_2026-08-24.csv` : RS06 ajouté, réparation/contextualisation acteur-level à J+7, audience overlap inconnue.
- `data/XQ203A_EDITORIAL_FORENSIC_AUDIT_2026-08-25.csv` : registre structuré des nouveaux findings.
- `data/XQ203A_RESEARCH_SOURCE_REGISTRY_2026-08-25.csv` : registre des sources de l’audit post-XQ203.
- `XQ203A_POSTAUDIT_TRACE_2026-08-25.json` : état machine-readable.

## Artefacts de preuve conservés

- `annexes/XQ203A_MOBILE_FIGURE_QA_390PX.png` : montage reproductible des cinq figures ramenées à 390 px de large pour le contrôle mobile.
- `data/XQ203A_EDITORIAL_FORENSIC_AUDIT_2026-08-25.csv` : findings structurés, statuts, confiance, source et action.
- `data/XQ203A_RESEARCH_SOURCE_REGISTRY_2026-08-25.csv` : sources nouvelles de l’archéologie documentaire avec état d’accès.
- `XQ203A_POSTAUDIT_TRACE_2026-08-25.json` : état machine-readable, règles négatives, files d’attente P0/P1 et gaps.
- `data/QUINTESSENCE_XQ196_INV_FC65.sqlite` : base XQ196 d’origine préservée puis enrichie de façon additive avec XQ203A ; source Library et SHA de base consignés dans `metadata`; intégrité SQLite vérifiée.

Principe : conserver également les résultats négatifs et les données non récupérées. `NOT_RECOVERED` reste un état de preuve, jamais un synonyme de `N’EXISTE PAS`.

## Gate

`XQ203_ARTICLE_TEXT = FROZEN_UNCHANGED`  
`XQ203A_TRACEABILITY = UPDATED`  
`ARTICLE_PATCH = REQUIRED_BEFORE_PUBLICATION_PROMOTION`  
`P0_DOCUMENTARY = OPEN`  
`P0_TYPO_TERMINOLOGY = OPEN`  
`P1_MOBILE_QA = OPEN`
