---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "pilot_review"
artifact_id: "INV-049-PILOT-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-049"
---

<!-- DERIVED_FROM: INV-049_INVESTIGATION.md; INV-049_CERTIFICATION.json; INV-049_RENARD.md -->
<!-- DECISION: pilot=PASS; renard=CLOSED_NO_FURTHER_MATERIAL_DELTA -->

# INV-049 — revue du pilote

## Verdict

```text
P0 = 0
P1 = 0
P2 = 2
PILOT = PASS
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
```

## ROBUSTE

1. **Financement != contrôle.** Le run établit des flux matériels, des objectifs de plaidoyer et des mécanismes d'action, mais refuse de promouvoir automatiquement financement, relation ou accès en commandement.
2. **Neutralité naïve refusée symétriquement.** OSF poursuit explicitement des objectifs de politique publique ; l'absence de commandement démontré ne rend pas l'activité politiquement neutre.
3. **Bridge France/UE renforcé par RENARD.** Le financement de More in Common comporte un objet programmatique explicitement France/UE ; Destin Commun est une branche française d'un réseau à gouvernance mutualisée. Cela établit un bridge de capacité, pas un droit causal.
4. **Correction corpus.** `OSF -> More in Common -> Destin Commun` est défendable comme chaîne réseau/financement ; `OSF -> grant direct Destin Commun` reste non établi.
5. **Causalité bornée.** I0-I2 sont bien mieux établis que I5-I7 ; aucun effet France/UE agrégé n'est inféré depuis les montants ou réunions.

## P2

- `FCT-012` repose sur un miroir fidèle d'une réponse de la Commission. La pièce est utile mais non centrale ; lors d'une réutilisation future, préférer l'URL institutionnelle primaire si elle redevient accessible.
- Les agrégations fiscales sont suffisamment traçables pour le pilote, mais les montants/purposes de grants particulièrement décisifs devraient être remontés au filing IRS/990 original lorsqu'une formulation quantitative finale en dépend.

## Gate

```text
TE_DELIVERY = PASS
CERT_DELIVERABLE_SHA_MATCH = PASS
INVESTIGATION_SHA256 = f731e05757a6b8bcd0fcee1919677256790000e69f9243bb294704f4ca9d14d4
RUN_STATE_SHA256 = 5c4b0c2711af98c141beb0989e5fa4aae94de99ea2073bf9f1b266465183be08
SNAPSHOT_SHA256 = 834d18cb145419d94c19d6ecec51619cb867d2feff328e72d040a55a04907587
CERTIFICATION_SHA256 = 8f549bc737a32acf68e6adce0084ed4efa679cd108283a99d70d0f4271abbad8
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
INV-049 = CLOSED
NEXT_PILOT = INV-071 READY_NOT_LAUNCHED
```

Aucun redesign du METHOD_PACK ou de Truth Engine n'est requis.
