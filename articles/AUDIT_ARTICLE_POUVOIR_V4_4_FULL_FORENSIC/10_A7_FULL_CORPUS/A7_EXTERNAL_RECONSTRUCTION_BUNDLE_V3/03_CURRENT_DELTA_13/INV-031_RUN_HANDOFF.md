---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-031"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-12"
---

# RUN_HANDOFF — INV-031

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2359-integrity-initiative-europe`
- Deliverable: `2026-09-11_23-59_integrity-initiative-europe_INVESTIGATION.md`
- Deliverable SHA-256: `2d31bdd966f1100668575019430b411a4163a15c4ec184e343a13eae58df7ba6`
- State ID: `sha256:890ac5576839fe7ce50801c38a7f23ebae35d795255b3fa3a2dfa95014be8570`
- Runtime: `QRY=24 / WEB=8 / FETCH=16 / SRC=16 / FCT=18 / provenance_families=8`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Persistence: `PASS / eligible=18 / attempted=0 / success=0 / failure=0 / blocked=18 / MNEMO_UNAVAILABLE`

## Delta central

INV-031 ferme le résidu britannique sur un mécanisme borné : **financement public de contre-désinformation -> projet intermédiaire -> clusters transnationaux -> journalistes/experts/décideurs -> diffusion, briefing ou mobilisation -> exposition/accès**. Le financement FCO/CSSF et l'architecture déclarée du réseau sont établis. Ce résultat suffit à qualifier une **capacité d'influence transnationale financée par l'État**, sans autoriser le saut vers un commandement clandestin détaillé.

Le cas espagnol `Moncloa` ferme une action rapide et une chronologie d'issue : les artefacts du projet décrivent mobilisation sociale/médiatique et s'attribuent une influence ; une chronologie indépendante confirme que Pedro Baños a été envisagé puis que Miguel Ángel Ballesteros a été choisi. En revanche, aucun objet décisionnel inspecté ne ferme `campagne -> décision` : l'effet causal sur la nomination reste `NOT_ESTABLISHED`.

## Registre causal certifié

- `FCO/CSSF -> financement -> Integrity Initiative` = **SUPPORTED**.
- `financement public -> capacité transnationale de réseau/distribution` = **SUPPORTED_BOUNDED**.
- `clusters -> interfaces journalistes/experts/décideurs` = **SUPPORTED_AS_PROJECT_RECORD**, avec limite de provenance et de participation individuelle.
- `liste France -> membre actif/consentant/taské pour chaque nom` = **REFUTED_AS_AUTOMATIC_INFERENCE**.
- `Moncloa mobilisation -> exposition/pression observable` = **SUPPORTED_BOUNDED**.
- `Moncloa -> changement causal de nomination Baños/Ballesteros` = **NOT_ESTABLISHED / CAUSALITY_GAP**.
- `FCO grant -> attaques partisanes britanniques` = **NOT_ESTABLISHED / FUNDING_ATTRIBUTION_GAP**.
- `Integrity Initiative -> East StratCom cooperation` = **REFUTED_IN_SCOPED_PERIOD** par la réponse Commission 2019.
- `Integrity Initiative -> commandement direct par services britanniques` = **NOT_ESTABLISHED / ATTRIBUTION_GAP**.

## Limites / reopen triggers

Réouvrir uniquement sur un objet primaire nouveau capable de fermer au moins une arête aujourd'hui ouverte :

1. instruction/tasking FCO ou service -> opération précise ;
2. preuve person-specific d'adhésion/tasking pour un contact de cluster ;
3. document décisionnel espagnol reliant la campagne à la nomination ;
4. audit de grant traçant une dépense publique vers une activité partisane domestique ;
5. preuve déclassifiée/judiciaire de commandement par un service.

`Funding != command`, `network != tasking`, `self-attribution != causality` restent les gardes terminales.
