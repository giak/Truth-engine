# INV-150 — Investissements stratégiques, acquisitions et fonds souverains

## PRE-COLLECTION / lancement

Status: **ACTIVE_PRECOLLECTION**  
Date: 2026-09-11  
Truth Engine FINAL: **NOT_RUN**

## Question

Quand une prise de participation, une acquisition ou un investissement étranger crée-t-il un **levier de contrôle réellement exploitable** sur un actif stratégique français ou européen, et quelles preuves permettent de distinguer propriété économique, contrôle juridique, influence sur la gouvernance, risque de sécurité et coercition effectivement exercée ?

## Chaîne candidate

```text
PRINCIPAL / BÉNÉFICIAIRE EFFECTIF / ÉTAT LIÉ
-> INVESTISSEUR / FONDS / VÉHICULE
-> PARTICIPATION / ACQUISITION
-> DROITS DE VOTE / BOARD / VETO / INFORMATION / CONTRÔLE
-> ACTIF / TECHNOLOGIE / INFRASTRUCTURE / CAPACITÉ STRATÉGIQUE
-> EXERCICE OU MENACE CRÉDIBLE DU LEVIER
-> ADAPTATION / DÉCISION
-> EFFET
```

## Gardes

```text
ownership != control
control != coercion
state-linked investor != state tasking
foreign subsidy != foreign command
screening concern != proven hostile intent
mitigation != proof of wrongdoing
blocked acquisition != interference by itself
```

## Sources publiques initiales

### SRC-001 — Regulation (EU) 2026/1386, foreign investment screening

Le règlement du 17 juin 2026 remplace le cadre 2019/452. Il impose un socle commun de screening, couvre notamment certains investissements indirects/intra-UE sous contrôle tiers et demande de prendre en compte la propriété, le financement public, les droits spéciaux, les administrateurs nommés par un État et le bénéficiaire effectif. Il autorise des mesures de mitigation, l'interdiction ou le démantèlement d'une opération selon le risque.

https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1386

### SRC-002 — Direction générale du Trésor, régime IEF France

Le contrôle français suit la chaîne de contrôle de l'investisseur et peut viser acquisition de contrôle, branche d'activité ou certains seuils de droits de vote dans une cible sensible. L'issue peut être autorisation, autorisation sous conditions ou refus.

https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-conditions-d-une-operation-soumise-a-autorisation-prealable

### SRC-003 — Pouvoirs de police IEF

En cas d'opération non autorisée ou de violation des conditions, le ministre peut exiger régularisation, modification ou rétablissement de la situation antérieure, suspendre des droits de vote ou imposer une cession/mesures conservatoires.

https://www.tresor.economie.gouv.fr/services-aux-entreprises/investissements-etrangers-en-france/les-pouvoirs-de-police-du-ministre-charge-de-l-economie

### SRC-004 — Foreign Subsidies Regulation

Le FSR est un contrôle distinct : il vise les distorsions du marché intérieur causées par des contributions/subventions de pays tiers et peut examiner certaines concentrations. `foreign subsidy != security-control screening` doit rester une séparation explicite.

https://competition-policy.ec.europa.eu/foreign-subsidies-regulation/about_en

## Claims PRE

| Claim | Statut PRE |
|---|---|
| propriété étrangère = ingérence | REFUTED_AS_AUTOMATIC_EQUIVALENCE |
| contrôle juridique peut créer des droits matériels sur un actif stratégique | SUPPORTED_LEGAL |
| contrôle indirect par gouvernement tiers est un facteur explicitement inspecté dans le cadre UE 2026 | SUPPORTED_LEGAL |
| screening / mitigation / prohibition = preuve d'intention hostile | REFUTED_AS_AUTOMATIC_EQUIVALENCE |
| ownership/control peut devenir levier seulement si un droit ou dépendance est exercé ou crédiblement mobilisable | HYPOTHESIS_TO_TEST |
| fonds souverain = commandement étatique de chaque investissement | REFUTED_AS_AUTOMATIC_EQUIVALENCE |

## Gaps à fermer avant FINAL

1. au moins deux cas France/UE où une opération a été conditionnée, refusée ou défaite, avec droits de contrôle et motif documentés ;
2. un contrôle positif où un droit d'ownership/governance a effectivement été exercé comme levier ;
3. un contrôle négatif où propriété étrangère importante n'a pas produit de tasking/coercition ;
4. distinguer FDI screening, merger control et Foreign Subsidies Regulation ;
5. fonds souverains : séparer propriété publique, mandat d'investissement, gouvernance et instruction politique actor-specific ;
6. mesurer l'effet : transfert de technologie, décision de cible, sécurité d'approvisionnement ou décision publique, pas seulement existence du screening.

## Verdict de lancement

`INV-150 = ACTIVE_PRECOLLECTION`.
