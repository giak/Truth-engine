---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "pilot_review"
artifact_id: "INV-103-PILOT-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-103"
---

<!-- DERIVED_FROM: run=20260906-1451-defiance-institutionnelle-francaise; investigation=2026-09-06_14-51_defiance-institutionnelle-francaise_INVESTIGATION.md; certification=2026-09-06_14-51_defiance-institutionnelle-francaise_CERTIFICATION.json -->
<!-- DECISION: pilot=PASS; renard=NO; content_rewrite=NO -->

# INV-103 — revue du pilote

## Verdict

```text
P0 = 0
P1 = 0
P2 = 1
PILOT = PASS
RENARD = NO
```

## ROBUSTE

1. **Pas de défiance institutionnelle uniforme.** `CLM-001` est soutenu : la confiance est très basse pour les institutions politiques nationales et les médias, tandis que les institutions de proximité, de soin et de protection restent nettement plus hautes.
2. **La dynamique longue n'est pas un effondrement général.** `CLM-002/003` séparent la représentation politique nationale des institutions de protection/soin ; les trajectoires diffèrent par institution.
3. **Attachement démocratique ≠ satisfaction démocratique.** `CLM-004` conserve la divergence entre attachement au régime et jugement sur son fonctionnement.
4. **Police et justice ne doivent pas être agrégées.** `CLM-005/006` montrent des niveaux et trajectoires distincts ; la série ne soutient pas un effondrement agrégé de la confiance dans la police.
5. **Causalité correctement bornée.** `CLM-007` et `CAU-001..004` n'élèvent pas des associations observationnelles en causes générales.
6. **Contrôle indépendant de la hiérarchie.** `AXS-006` utilise une famille OCDE distincte pour tester le modèle de défiance généralisée ; le résultat conserve une hiérarchie différenciée.

## P2

- La trajectoire longitudinale française dépend principalement de la famille amont CEVIPOF. L'OCDE apporte un contrôle indépendant sur la hiérarchie récente, mais pas une réplication indépendante complète de la série 2009–2026. C'est une limite à conserver lors d'une réutilisation, pas un défaut invalidant du run.

## Gate

```text
TE_DELIVERY = PASS
CERT_DELIVERABLE_SHA_MATCH = PASS
RUN_ID = 20260906-1451-defiance-institutionnelle-francaise
QRY = 15
SRC = 8
PROVENANCE_FAMILIES = 3
FCT = 15
CHECKPOINTS = 7
INVESTIGATION_SHA256 = 41d0b8d330aae2da557e97437cfc8fd4ba844005c606556571cfae853508a2da
RUN_STATE_SHA256 = 1d18fae4df92884883a198ff51cf1b9681f29cab00dd3116bd669ff0d12fede0
SNAPSHOT_SHA256 = 34c65386beb45b5d886eb83e12d85515137e30494586d5dde1e382d069530a82
CERTIFICATION_SHA256 = 6939bbaa93d43bcec5559dcd7a73618d463b198f883126763c635de2338b20fc
RENARD = NO
INV-103 = CLOSED
```

## RENARD

`NO`. Les résiduels matériels sont soit des limites de design causal (`CAU-001..004`), soit des besoins de nouvelle vague/série indépendante. Une recherche générique supplémentaire ne promet pas de changer le modèle central et risquerait de confondre accumulation de sources et discrimination.
