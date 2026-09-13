# INV-149 — PRE-COLLECTION / lancement

Status: **ACTIVE_PRECOLLECTION**  
Date: 2026-09-11  
Truth Engine FINAL: **NOT_RUN**

## Hypothèse de travail

L’opacité financière n’est pas en elle-même une influence. Elle devient matériellement pertinente lorsqu’elle empêche d’identifier le véritable principal, la contrepartie ou le bénéficiaire d’un flux qui alimente ensuite un actif, un contrat, un intermédiaire ou un accès politique.

## Chaîne candidate

```text
ORIGINE ECONOMIQUE
-> SOCIETE / TRUST / PRETE-NOM / NOMINEE
-> BENEFICIAIRE EFFECTIF / CONTROLE REEL
-> FACILITATEUR PROFESSIONNEL
-> BANQUE / ACTIF / PAIEMENT / CONTRAT / DON
-> INTERMEDIAIRE / BENEFICIAIRE POLITIQUE
-> ACCES / ACTION / DECISION
-> EFFET
```

## Sources initiales vérifiées

### SRC-001 — Règlement (UE) 2024/1624
https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng

Le règlement harmonise la transparence des bénéficiaires effectifs. Il définit le bénéficiaire effectif par propriété ou contrôle, traite les structures multi-couches, les trusts et les nominees, et prévoit des obligations pour certaines entités étrangères entrant dans des relations économiques ou des marchés publics dans l’Union.

### SRC-002 — France, décret n° 2026-310 du 24 avril 2026
https://www.legifrance.gouv.fr/eli/decret/2026/4/24/2026-310/jo/texte

Le décret réforme l’accès au registre des bénéficiaires effectifs et transpose les mécanismes de la directive (UE) 2024/1640. Il fournit un objet français actuel pour tester disponibilité, intérêt légitime et limites d’accès aux données de propriété réelle.

### SRC-003 — FATF, Guidance on Beneficial Ownership of Legal Persons
https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html

Le FATF identifie les sociétés écrans et structures anonymes comme des moyens utilisés notamment par acteurs corrompus, blanchisseurs et personnes cherchant à dissimuler des activités ou patrimoines illicites. Cela établit le risque d’opacité, pas un effet politique.

### SRC-004 — OLAF, schéma de fraude via sociétés écrans, 30 avril 2025
https://anti-fraud.ec.europa.eu/media-corner/news/olaf-and-polish-authorities-uncover-major-vat-import-fraud-scheme-2025-04-30_en

OLAF documente un réseau opérant via sociétés de transport, logisticiens et dizaines de sociétés écrans enregistrées au nom de ressortissants de plusieurs pays. Contrôle positif pour `shell network -> opacity / illicit flow`; aucun effet d’influence politique n’est inféré.

## Claims PRE

| Claim | Statut |
|---|---|
| `beneficial_owner != legal_holder` peut être matériel dans une chaîne multi-couche | SUPPORTED_LEGAL |
| structures multi-couches / nominees peuvent compliquer l’attribution du contrôle réel | SUPPORTED_LEGAL / RISK |
| société écran = blanchiment | REFUTED_AS_AUTOMATIC_EQUIVALENCE |
| blanchiment = influence politique | REFUTED_AS_AUTOMATIC_EQUIVALENCE |
| bénéficiaire effectif = commanditaire politique | REFUTED_AS_AUTOMATIC_EQUIVALENCE |
| opacité peut casser l’arête `fonds -> principal réel` | HYPOTHESIS_TO_TEST |

## Gaps à fermer avant FINAL

1. cas France/UE où l’opacité de propriété ou de paiement est reliée à un intermédiaire/acteur politique identifiable ;
2. au moins un dossier judiciaire fermant plusieurs couches `fonds -> shell/nominee -> bénéficiaire effectif -> paiement/actif -> action` ;
3. contrôles négatifs : structures complexes légitimes sans blanchiment/influence ;
4. rôle différencié des banques, avocats, comptables, fiduciaires et autres facilitateurs ;
5. articulation avec INV-148 : `principal réel -> paiement courtier -> influence`, sans convertir tout blanchiment en trafic d’influence ;
6. audit de l’accès réel aux registres et de ses limites après la réforme française 2026.

## Verdict de lancement

`INV-149 = ACTIVE_PRECOLLECTION`.
