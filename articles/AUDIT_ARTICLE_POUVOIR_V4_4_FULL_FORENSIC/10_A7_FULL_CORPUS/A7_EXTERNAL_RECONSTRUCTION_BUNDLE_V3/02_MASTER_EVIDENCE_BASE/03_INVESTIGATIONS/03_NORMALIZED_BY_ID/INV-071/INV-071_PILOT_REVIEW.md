---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "pilot_review"
artifact_id: "INV-071-PILOT-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-071"
---

<!-- DERIVED_FROM: INV-071_INVESTIGATION.md; INV-071_CERTIFICATION.json -->
<!-- DECISION: pilot=PASS; renard=NO -->

# INV-071 — revue du pilote

## Verdict

```text
P0 = 0
P1 = 0
P2 = 2
PILOT = PASS
RENARD = NO
```

## ROBUSTE

1. **Mandat borné, capacité réelle.** Le cadre public exige un lien avec des intérêts étrangers et des comportements inauthentiques/manipulatoires ; il ne supporte pas la thèse d'un mandat général de fact-checking du débat intérieur. En parallèle, les capacités de collecte, d'automatisation, de R&D, d'alerte et de coordination sont réelles et se sont élargies en 2026.
2. **Mesure d'impact correctement bornée.** VIGISCORE estime un risque d'impact et VIGINUM mesure visibilité/propagation ; ses propres documents distinguent cela des effets réels sur opinions, intentions de vote ou résultat électoral.
3. **Attribution graduée.** Rokh Solis réfute l'absolu « jamais d'acteurs liés à un pays allié » : des marqueurs israéliens/Blackcore sont documentés, sans promotion abusive vers un commanditaire étatique ou final.
4. **Accountability stratifiée.** CES, CNIL, Parlement et commission électorale indépendante existent mais n'ont ni le même statut ni le même pouvoir. Le CES est auprès du SGDSN ; la CNIL apporte un contrôle externe données ; la commission de juillet 2026 est institutionnellement distincte.
5. **I0-I4 ≠ I5-I7.** Les capacités, actions et certaines expositions sont bien mieux établies que la persuasion, le changement électoral ou le contrefactuel.

## P2

- Les résultats de mitigation (comptes/pages rendus inaccessibles, coopération plateformes) sont principalement rapportés par VIGINUM. Ils établissent une conséquence opérationnelle, pas une efficacité causale indépendante sur la menace ou le vote.
- Les réformes de février/juillet 2026 sont récentes. Toute réutilisation future doit conserver un `AS_OF` visible et recontrôler la pratique réelle de la nouvelle commission, les suites CNIL et les avis CES.

## Gate RENARD

```text
RENARD = NO
```

Les gaps restants ont déjà un discriminant explicite mais ne sont pas résolubles par une recherche générique supplémentaire :

```text
I5/I6 électoral -> design exposition/survey/comportement ou preuve juridictionnelle
commanditaire final -> trace technique/financière/tasking upstream
accountability 2026 -> pratique future + suivis CNIL/CES
```

Sans pièce concrète déclenchante, poursuivre serait du fishing et violerait le gate delta-only.

## Certification

```text
TE_DELIVERY = PASS
CERT_DELIVERABLE_SHA_MATCH = PASS
INVESTIGATION_SHA256 = cc0063eb57f6b95f1589cb9d50f81a603bec0415b5069109c4855bdb76f5e810
RUN_STATE_SHA256 = 0accdfae5db03a5a718dae89ea8143e9e8abf4d112469e515e209f4aa1de16b6
SNAPSHOT_SHA256 = ed8b8f00d0d622fe1d487ba97718a061ed65e551d1b75b7d4831da958a1282ec
CERTIFICATION_SHA256 = fbe1ad101bb2dd2b1b0b5776a2809d62946267501a0f7efd4bedc66b7a4265bb
RENARD = NO
INV-071 = CLOSED
NEXT_PILOT = INV-103 READY_NOT_LAUNCHED
```

Aucun redesign de `METHOD_PACK` ou de Truth Engine n'est requis.
