# XQ182 — Règles d’adjudication finale

**Projet :** QUINTESSENCE / Covid fact-checking  
**Date :** 23 août 2026  
**Statut :** FROZEN pour la couche d’adjudication issue de V5.1-FROZEN  
**Entrées :** 41 atomes, 4 runs LLM validés mécaniquement, sources gelées, contrôle manuel des trous résiduels.

## 1. Principe

Les LLM ne décident pas la conclusion éditoriale. Ils servent de **codeurs documentaires reproductibles**. La couche finale est dérivée des atomes après validation de protocole et, si nécessaire, contrôle primaire manuel.

`SOURCE != OBSERVATION != ATOME != VERDICT_DE_CAS != THÈSE_GÉNÉRALE`

Aucun niveau ne doit hériter automatiquement de la certitude du niveau précédent.

## 2. États atomiques finaux

- **ESTABLISHED** : la question atomique reçoit `YES` ou `FOUND` sur preuve admissible.
- **NEGATED** : la question atomique reçoit `NO` sur preuve admissible.
- **BOUNDED_NOT_FOUND** : recherche documentée sans source répondant aux critères. Ne signifie jamais inexistence.
- **UNRESOLVED** : preuve insuffisante, inaccessible ou contradictoire.
- **PROTOCOL_INVALID** : état d’un run individuel seulement ; il ne devient pas une conclusion factuelle.

## 3. Consensus inter-LLM

Le consensus sert de test de **reproductibilité**, jamais de preuve par autorité.

- **Tier A** : 4/4 réponses déterminées valides identiques.
- **Tier B** : 3/4 réponses déterminées valides identiques ; le quatrième est non déterminé ou inaccessible.
- **Tier C** : 2/4 seulement ; adjudication manuelle obligatoire.
- **Tier D** : une seule réponse déterminée valide ; contrôle primaire manuel recommandé avant usage éditorial fort.
- **Tier E** : aucune réponse déterminée valide ; contrôle primaire manuel obligatoire.

Un conflit substantiel existe uniquement lorsque deux réponses **déterminées et valides** s’opposent (`YES` vs `NO`, `FOUND` vs `NOT_FOUND`). `UNREADABLE` ou `UNCERTAIN` ne sont pas des désaccords factuels.

## 4. Adjudication manuelle

Une adjudication manuelle peut remplacer un Tier E/C/D seulement si :

1. la source primaire ou version historique pertinente est réellement consultée ;
2. le cutoff est respecté ;
3. la conclusion reste atomique ;
4. le motif est tracé dans la matrice ;
5. aucune conclusion éditoriale plus large n’est injectée dans l’atome.

**Application XQ182 :** C03-A est résolu manuellement `NO` à partir de l’article NEJM et de son correctif : le dénominateur utilisé pour le calcul « 82 % » ne couvrait pas correctement l’ensemble des grossesses pertinentes ; le correctif précise qu’aucun dénominateur approprié n’était alors disponible.

## 5. Verdicts de cas autorisés

Les fiches de cas peuvent utiliser uniquement des qualifications bornées :

- `ACCURATE_AT_T`
- `TOO_CATEGORICAL_AT_T`
- `MIXED_COMPONENTS`
- `LATER_CONFIRMED`
- `LATER_CONTRADICTED_ABSOLUTE`
- `EXPLICIT_REPAIR`
- `LATER_CONTEXT_ONLY`
- `NO_SELF_REPAIR_FOUND`
- `TEMPORAL_FLATTENING`
- `MODEL_TO_SLOGAN_COMPRESSION`
- `BOUNDED_SELECTION_GAP`
- `REGULATORY_EXCLUSION_SUPPORTED`

Les combinaisons sont permises si les dimensions sont différentes.

## 6. Les cinq axes

### Selection
Question : **qu’est-ce qui a été choisi ou non choisi pour vérification ?**  
Ne peut pas être inféré des 14 cas comme taux de prévalence. Un négatif doit rester borné à un sous-ensemble, une période et une stratégie de recherche.

### Fidelity
Question : **le fact-check répond-il exactement à la proposition qui était réellement formulée ?**  
Un claim composite doit être séparé : détection biologique != toxicité != causalité clinique != intention de dissimulation.

### Calibration
Question : **le degré de certitude éditoriale correspond-il au degré de certitude des preuves à T ?**  
`non détecté != impossible` ; `non démontré != faux` ; `modèle != mesure observationnelle`.

### Temporality
Question : **la conclusion respecte-t-elle ce qui était disponible à T, les dates online-first et les versions historiques ?**  
Une page actuelle ne prouve jamais seule une formulation ancienne.

### Repair
Question : **une correction ultérieure est-elle explicitement reliée au contenu antérieur ?**  
`correction != contextualisation ultérieure != réparation`.

## 7. Passage atomes -> cas

Un verdict de cas doit :

1. citer les atomes qui le soutiennent ;
2. préserver les résultats contraires ou limitatifs ;
3. expliciter ce qui reste hors scope ;
4. ne jamais convertir une erreur locale en taux global de fiabilité.

Exemple C06 :

`S1/Spike détectée = OUI` + `toxicité systémique démontrée par Ogata = NON`  
=> conclusion autorisée : **l’absolu « ne circule pas » est trop fort ; la détection ne démontre pas la toxicité alléguée.**

Conclusion interdite : **« Spike toxique partout »** ou **« le fact-check est entièrement faux »**.

## 8. Passage cas -> article

Toute phrase d’article doit être classée avant publication :

- `DIRECT_FACT`
- `BOUNDED_INFERENCE`
- `EDITORIAL_INTERPRETATION`
- `OPEN_QUESTION`

Les formulations suivantes restent interdites sans nouvelle preuve :

- « le fact-checking est inutile » ;
- « tous les fact-checkers mentent » ;
- « collusion générale démontrée » ;
- un taux sectoriel dérivé de ces 14 cas ;
- « quatre IA sont d’accord donc c’est vrai ».

## 9. Règle de publication

Le résultat multi-LLM peut être décrit ainsi :

> Quatre systèmes différents, contraints par le même protocole documentaire et soumis à un validateur mécanique, n’ont produit aucun conflit substantiel validé sur les atomes comparables. Cet accord mesure la reproductibilité du codage, pas la vérité par vote.

## 10. Patch P0 découvert pendant XQ182

La narration actuelle du dossier **C07 / lait maternel** doit être corrigée : le preprint Golan était public le **8 mars 2021**, avant le fact-check AFP du **18 juin 2021**. Il rapportait une non-détection dans une petite série et une fenêtre limitée ; cela ne démontrait pas une impossibilité absolue. La publication ultérieure de Hanna détecte des traces dans certains échantillons mais ne démontre pas de danger clinique.
