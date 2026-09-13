---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-097-RUN-HANDOFF"
version: "1.0"
status: "terminal"
updated: "2026-09-09"
inv_id: "INV-097"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
---

<!-- TRACE: source=certified_INV-097_R3P1; no_new_web=true -->

# INV-097 — RUN_HANDOFF

- **INV_ID:** INV-097
- **TE:** `DELIVERY_PASS_R3P1`
- **Deliverable SHA-256:** `59780a267b3e30f4a5f1bf7df6af8cfb2d559978fda1bd0ab9ad30b0d8f6f763`
- **Counts:** 30 QRY / 15 SRC / 30 FCT / 5 provenance families / 140 passed / 2 skipped
- **Persistence:** 20 eligible FACT rows, 20 blocked `MNEMO_UNAVAILABLE`, 0 fabricated memory IDs

## Central delta

L’amplification artificielle est un mécanisme réel et mesurable : réseaux coordonnés ou inauthentiques, bots, faux engagement, répétition automatisée et infrastructures de distribution peuvent augmenter la visibilité de contenus politiques ; la retransmission humaine est documentée case-specifically. En revanche, `bot != faux compte`, `réseau != coordination`, `coordination != tasking`, `amplification != persuasion` et `amplification != vote_change`.

## Evidence-chain ceiling

- **I0–I2:** établis case-specifically pour plusieurs opérations.
- **I3:** coordination opérationnelle souvent établie ; tasking/commanditaire ultime incomplet selon les cas.
- **I4:** amplification/exposition structurelle établie ; dénominateur humain incrémental incomplet.
- **I5:** retransmission humaine établie dans un comparateur ; persuasion générale non établie.
- **I6:** non établi de façon générale France/UE.
- **I7:** non établi.

## Material gaps

1. tasking/client authentifié ;
2. dénominateur reproductible amplification artificielle vs baseline organique et exposition humaine ;
3. design causal France/UE sur persuasion, participation, vote ou résultat.

## RENARD

**NO** — les upgrades matériels exigent de nouvelles traces discriminantes, pas davantage de cas isomorphes.

## New ideas triaged

- IA générative/deepfakes (INV-092) reste distincte : création/transformation de contenu et changement d’échelle, pas simple amplification.
- Les contrôles négatifs doivent rester obligatoires dans toute synthèse sur l’« influence numérique » afin d’éviter `détection -> prévalence -> effet`.
