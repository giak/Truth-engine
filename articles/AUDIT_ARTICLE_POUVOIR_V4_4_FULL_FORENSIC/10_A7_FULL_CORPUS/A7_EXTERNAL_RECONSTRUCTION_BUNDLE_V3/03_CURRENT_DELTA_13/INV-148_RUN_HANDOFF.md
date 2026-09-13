---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-148"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-149"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-148

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-1742-trafic-influence-courtiers-acces`
- PRE deterministic gate: **PASS**
- DELIVERY deterministic gate: **PASS**
- verify tests: **140 passed / 2 skipped**
- Sources: **12**
- Facts: **16**
- Provenance families: **3**
- Mnemo: `MNEMO_UNAVAILABLE`; 16/16 eligible facts terminally blocked, no memory id fabricated
- Deliverable SHA-256: `5507d13278bfa85d5086b2056743c61f21c43ab53f8549188f5028a042087d7d`
- State ID: `sha256:7eb930bffd3b0d96e54b4e23feab2102e8d1f9a014dfcc898054e4cbfa3ba298`

## Delta central

INV-148 établit le **trafic d’influence comme mécanisme triadique autonome** :

```text
BENEFICIAIRE / PAYEUR
-> AVANTAGE INDU
-> INTERMEDIAIRE
-> INFLUENCE REELLE OU SUPPOSEE
-> DETENTEUR DE LA DECISION
-> INTERVENTION
-> DECISION / AVANTAGE RECHERCHE
```

La mécanique ne se confond ni avec la corruption directe, ni avec le lobbying rémunéré. L’intermédiaire est causalement central mais non suffisant : un consultant, lobbyiste, agent commercial ou canal de corruption n’est pas automatiquement un courtier d’influence. Le droit français couvre explicitement les décisions d’agents publics étrangers et d’organisations internationales ; la directive (UE) 2026/1021 confirme que l’influence peut être réelle ou supposée et que la réussite finale n’est pas nécessaire à l’infraction.

Les contrôles positifs incluent l’échantillon AFA, l’affaire Bismuth et le dossier croate EPPO de marché public financé par l’UE. Airbus reste un contrôle négatif utile : `intermediaire + commission + corruption != trafic_d_influence` sans preuve que l’objet de l’échange est l’influence sur un tiers décideur.

## Gap explicite

`NOT_FOUND_IN_BOUNDED_RUN` : aucun jugement français définitif récent sous `435-2/435-4` n’a été identifié dans le run qui ferme proprement `principal étranger -> avantage -> intermédiaire rémunéré -> influence -> décision étrangère/internationale`.

Ce résultat est un **gap d’accès/retrieval**, pas une preuve de non-existence.

## Impact de reclassification

Le maillon devenu prioritaire n’est plus « existe-t-il un courtier ? », mais :

```text
QUI EST LE PRINCIPAL REEL ?
-> D'OU VIENT L'ARGENT ?
-> QUEL VEHICULE / PRETE-NOM / BENEFICIAIRE EFFECTIF ?
-> QUEL PROFESSIONNEL FACILITE ?
-> QUEL PAIEMENT / ACTIF / CONTRAT ?
-> QUEL INTERMEDIAIRE POLITIQUE ?
```

Impact direct : **promouvoir INV-149**.
