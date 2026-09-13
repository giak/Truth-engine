---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-147"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-009;INV-015;INV-016;INV-024;INV-029;INV-031;INV-032;INV-034;INV-037;INV-046;INV-051;INV-053;INV-058;INV-075;INV-105;INV-106;INV-107;INV-108;INV-109;INV-111;INV-112;INV-120;INV-121;INV-122;INV-123"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-147

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-2042-double-standard-matched`
- Deliverable: `INV-147_INVESTIGATION.md`
- Deliverable SHA-256: `791ecce8ecccc4e9b37aad3b58ccf2bacb5861de60fefeb116f9a01e053ae96a`
- Corpus runtime: `QRY=20 / SRC=10 / FCT=22 / provenance_families=7`
- Persistence: `PASS / eligible=22 / blocked=22 / success=0 / failure=0 / fabricated_memory_ids=0 / reason=MNEMO_UNAVAILABLE`

## Delta central

Le corpus n’établit pas la thèse forte d’un double standard géopolitique systématique à mécanisme et niveau de preuve comparables. Il établit en revanche une asymétrie située en amont : certains mandats et régimes juridiques construisent explicitement une population de cas étrangers ou non-UE. Le dispositif français de transparence exclut les mandants des États membres de l’UE et VIGINUM a un mandat d’ingérence numérique étrangère. Cela peut produire une distribution asymétrique des cas observés sans démontrer un seuil probatoire ou une sanction discrétionnairement plus sévères contre les adversaires.

La commission d’enquête française de 2023 fournit un signal partiel d’asymétrie d’attention : Russie et Chine sont présentées comme les deux principales menaces, tandis que le traitement américain à la « lisière » du champ est contesté au sein même de la commission. Les confondeurs de menace, périmètre, temps et disponibilité des preuves empêchent toutefois d’identifier le camp comme cause marginale.

## Highest supported influence/effect edge

- `origine du mandant -> périmètre juridique -> obligation/exclusion déclarative` = **SUPPORTED**.
- `comportement technique -> caractérisation MOI -> critère d’attribution étrangère -> label INE` = **SUPPORTED** ; la couche MOI peut fonctionner avant attribution.
- `priorité de menace/camp -> attention parlementaire -> fréquence de qualification` = **PARTIAL / CAUSALITY GAP**.
- `contrôle étatique + manipulation + guerre -> suspension RT/Sputnik` = **SUPPORTED pour le cas** ; `-> enforcement bias par camp` = **NOT ESTABLISHED**.
- `camp -> seuil probatoire/enforcement différent à conduite identique` = **UNRESOLVED / DENOMINATOR GAP**.

## Material gaps / contradictions

- `LEGAL_DESIGN_ASYMMETRY` est établie, mais `LEGAL_DESIGN_ASYMMETRY != ENFORCEMENT_BIAS`.
- Le registre HATVP, lancé le 1er octobre 2025, n’offre pas encore un historique mature permettant des taux comparables.
- Aucun dénominateur public commun ne permet de mesurer par camp les probabilités de détection, qualification, enquête, poursuite ou sanction à conduite isomorphe.
- Les sanctions RT/Sputnik sont confondues par guerre active, contrôle étatique et rôle opérationnel allégué dans la manipulation de l’information.
- Le vocabulaire DGSE/VIGINUM/SEAE/droit de transparence n’est pas une métrique homogène : les mandats et objets diffèrent.

## Contradictory review / causal ceiling

Le meilleur modèle courant est hybride : `design institutionnel/juridique -> population observable`, puis `propriétés du mécanisme + preuve + contexte -> qualification/procédure/conséquence`. Une asymétrie d’attention existe dans un corpus parlementaire borné, mais la thèse `camp géopolitique -> standard probatoire ou enforcement systématiquement différent` n’est pas fermée. Le fait que VIGINUM puisse caractériser un MOI avant l’identité/origine de l’acteur constitue un contrôle important contre une théorie purement camp-first.

## RENARD

`RENARD = NO`.

Raison : les upgrades matériels exigent des données longitudinales et des dénominateurs qui n’existent pas encore, ou un corpus de labels pré-enregistré et reproductible. Une collecte générique supplémentaire aujourd’hui serait surtout cumulative et augmenterait le risque de cherry-picking.

## New ideas triaged

- Revoir longitudinalement la HATVP lorsque l’historique d’application sera matériellement mûr.
- Si un test lexical est relancé, pré-enregistrer avant collecte les champs de matching, sources, codebook et règles de codage.
- Injecter dans les synthèses finales la distinction `mandate/design asymmetry` versus `case-level evidentiary/enforcement asymmetry`.

## Mechanical transition expected

`INV-147 TE_ACTIVE -> CLOSED` uniquement après `control.py apply` avec reclassification post-run valide. `reclass_impact` énumère exhaustivement les 25 PRIMARY|CASE BACKLOG courants : le résultat est transversal et impose REVIEW 25/25, REUSE 0, équivalent sémantique d’un full-pool sans impact inconnu.
