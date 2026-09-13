# INV-148 — Trafic d’influence et courtiers d’accès
## PRE-COLLECTION / lancement

Status: **ACTIVE_PRECOLLECTION**  
Date: 2026-09-11  
Truth Engine FINAL: **NOT_RUN**  
Purpose: établir le discriminant avant collecte exhaustive.

## Question

Quand rémunère-t-on directement un acte du décideur, et quand rémunère-t-on un intermédiaire afin qu'il abuse d'une influence réelle ou supposée sur le décideur ?

## Chaîne candidate

```text
PRINCIPAL / PAYEUR
-> AVANTAGE / PROMESSE
-> INTERMÉDIAIRE
-> INFLUENCE RÉELLE OU SUPPOSÉE
-> AUTORITÉ / ADMINISTRATION / ORGANISATION INTERNATIONALE
-> INTERVENTION
-> DÉCISION / MARCHÉ / EMPLOI / AVANTAGE
-> EFFET
```

Cette chaîne est distincte de :

```text
CORRUPTION DIRECTE:
PAYEUR -> DÉCIDEUR -> ACTE

LOBBYING:
MANDANT -> REPRÉSENTANT DÉCLARÉ -> ARGUMENT/ACCÈS -> DÉCIDEUR

TRAFIC D'INFLUENCE:
PAYEUR -> INTERMÉDIAIRE RÉMUNÉRÉ -> ABUS D'INFLUENCE -> DÉCIDEUR
```

## Sources publiques initiales

### SRC-001 — Code pénal, article 433-2
https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070719/LEGISCTA000006165366/

Le droit français incrimine la sollicitation, l'acceptation ou l'offre d'un avantage afin qu'une personne abuse de son influence réelle ou supposée pour obtenir d'une autorité ou administration publique une décision favorable.

### SRC-002 — Code pénal, articles 435-2 et 435-4
https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070719/LEGISCTA000006181779/
https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070719/LEGISCTA000006181780/

Le même mécanisme existe pour l'influence visant un agent public étranger ou une organisation internationale publique. L'origine étrangère n'est donc pas le mécanisme : le droit isole l'avantage, l'intermédiaire, l'influence et la décision recherchée.

### SRC-003 — Direction des affaires criminelles et des grâces, circulaire Sapin II
https://www.justice.gouv.fr/bo/2018/20180228/JUSD1802971C.pdf

La circulaire décrit le trafic d'influence comme une infraction proche de la corruption, consistant à obtenir d'une personne qu'elle utilise abusivement son influence réelle ou supposée. Elle souligne que l'extension aux agents publics étrangers vise notamment l'intervention frauduleuse d'intermédiaires dans la conclusion de contrats internationaux.

### SRC-004 — Cour de cassation, crim., 18 décembre 2024, n° 23-83.178
https://www.courdecassation.fr/decision/67626d77d9347f6c9aef808c

Contrôle positif domestique. La Cour rejette les pourvois dans l'affaire dite des écoutes. Le raisonnement retient l'usage d'une influence auprès d'acteurs de la Cour de cassation afin d'obtenir une décision favorable, ainsi qu'une contrepartie promise. La Cour précise aussi que le pacte peut être postérieur aux actes d'influence.

### SRC-005 — Agence française anticorruption
https://www.agence-francaise-anticorruption.gouv.fr/fr/recommandations
https://www.agence-francaise-anticorruption.gouv.fr/files/files/Note_Analyse_Decisionsdejustice_ObservatoireAFA_09122024.pdf

L'AFA traite le trafic d'influence comme une atteinte à la probité distincte de la corruption. Son observatoire des décisions de justice fournit un lead empirique sur les profils de prévenus ; les chiffres ne seront pas extrapolés à la prévalence nationale sans audit du périmètre de l'échantillon.

## Claims initiaux

| Claim | Statut PRE |
|---|---|
| `corruption_directe != trafic_influence` | SUPPORTED_LEGAL |
| `lobbying != trafic_influence` | SUPPORTED_CONCEPTUAL / CASE_TEST_NEEDED |
| `influence_réelle_ou_supposée` suffit comme objet de l'abus si les autres éléments sont établis | SUPPORTED_LEGAL |
| le droit français couvre le trafic d'influence visant un agent public étranger / organisation internationale | SUPPORTED_LEGAL |
| l'intermédiaire est un objet causal central et ne doit plus être rangé dans `OTHER` | SUPPORTED_METHOD |
| trafic d'influence = ingérence étrangère | REFUTED_AS_AUTOMATIC_EQUIVALENCE |
| toute rémunération d'un intermédiaire politique = trafic d'influence | REFUTED_AS_AUTOMATIC_EQUIVALENCE |

## Leads corpus à réouvrir seulement comme matériaux

- `INV-136` : Qatargate / Huawei / Azerbaïdjan-PACE — corruption, intermédiaires, cadeaux, actes politiques.
- `INV-128` : influence-for-hire — marché privé d'intermédiation opaque.
- `INV-063` : Big Four — accès/expertise/révolving doors, sans trafic d'influence établi.
- `INV-120` : banques — lobbying/revolving doors, sans capture actor-specific établie.
- `INV-122` : défense — contrats/lobbying/expertise, sans causalité spécifique.
- `INV-027/028` : lobbying déclaré et organisé comme contrôles négatifs nécessaires.

## Gaps à fermer avant FINAL

1. jurisprudence 2016–2026 appliquant `435-2/435-4` à des agents publics étrangers ou organisations internationales ;
2. au moins un cas transnational avec intermédiaire, avantage et décision ciblée suffisamment fermés ;
3. contrôles négatifs : rémunération de consultant/lobbyiste sans trafic d'influence ;
4. relation avec règles HATVP / mandants étrangers : transparence administrative != qualification pénale ;
5. rôle des professionnels intermédiaires dans marchés internationaux ;
6. dénominateur minimal : fréquence et typologie des décisions judiciaires, sans confondre signalements et condamnations.

## Verdict de lancement

`INV-148 = ACTIVE_PRECOLLECTION`.

Aucune conclusion systémique n'est autorisée à ce stade. Le run a déjà produit un changement méthodologique durable : **le trafic d'influence devient une ACTION/QUALIFICATION distincte de `CORRUPTION`, `LOBBYING` et `FUNDING`.**
