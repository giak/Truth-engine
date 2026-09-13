# RUN_HANDOFF — INV-150

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-1828-investissements-strategiques-controle`
- Deliverable: `2026-09-11_18-28_investissements-strategiques-controle_INVESTIGATION.md`
- Deliverable SHA-256: `68b135fcc7ee06e05dcd538fb57a10b7fe83f5f7ecf2cbe6a384de118a53b17c`
- Corpus runtime: `QRY=13 / SRC=13 / FCT=18 / provenance_families=3`
- Tests: `140 passed / 2 skipped`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Persistence: `PASS / eligible=18 / blocked=18 / success=0 / failure=0`

## Delta central

INV-150 établit que l'investissement stratégique devient un objet de pouvoir lorsque le capital confère des droits effectifs de contrôle, de gouvernance, d'information, de veto ou de continuité sur un actif stratégique. Le corpus ferme plusieurs chaînes `acquisition -> contrôle/gouvernance -> intervention publique ou coordination opérationnelle`, sans promouvoir automatiquement cette capacité en coercition politique.

- **Photonis/Teledyne** : `acquisition envisagée -> contrôle IEF -> non-autorisation -> solution nationale` = **SUPPORTED**. Le refus protège un actif stratégique ; il ne démontre pas une intention hostile de Teledyne.
- **STX/Chantiers de l'Atlantique** : `structure de propriété -> droits de gouvernance -> sauvegardes workload/technologie` = **SUPPORTED** comme architecture préventive ; coercition hostile = **NOT_ESTABLISHED**.
- **e&/PPF Telecom** : investisseur contrôlé par un fonds souverain + subventions étrangères -> remèdes FSR = **SUPPORTED** ; la Commission n'a pas constaté que ces subventions avaient faussé le processus d'acquisition lui-même. `STATE_LINK != POLITICAL_TASKING`.
- **GPFG** : contrôle négatif : propriété publique + mandat général ne ferme pas un tasking politique de chaque participation.
- **Piraeus/COSCO** : `majorité de vote -> contrôle corporate -> coordination opérationnelle intra-groupe` = **SUPPORTED** ; `Beijing tasking -> décision politique grecque/UE` = **GAP_CAUSALITY** dans le corpus borné.
- **Newport Wafer Fab/Nexperia** : comparateur UK : acquisition à 100 % -> ordre de céder au moins 86 % = **SUPPORTED** comme matérialité du screening, pas comme preuve d'usage politique hostile antérieur.

## Règles probatoires conservées

```text
ownership != control
control != operational exercise
operational exercise != political coercion
state-linked investor != state tasking
foreign subsidy != foreign command
screening concern != hostile intent
mitigation/refusal != wrongdoing
dependency != exercised leverage
```

## Gap matériel

`DENOMINATOR_GAP`: aucune base représentative ne permet d'estimer la fréquence à laquelle un investissement stratégique étranger devient effectivement un instrument de coercition politique en France/UE.

Le résultat déplace donc le test discriminant vers les **dépendances de flux difficilement substituables**, où une restriction ou menace peut être observée sans passer par des droits actionnariaux.

## Reclassification

Impact direct : `INV-151` promu gagnant suivant. `INV-152` reste sous overlap guard avec INV-124 ; `INV-153` reste P1 ; `INV-154` reste P2.
