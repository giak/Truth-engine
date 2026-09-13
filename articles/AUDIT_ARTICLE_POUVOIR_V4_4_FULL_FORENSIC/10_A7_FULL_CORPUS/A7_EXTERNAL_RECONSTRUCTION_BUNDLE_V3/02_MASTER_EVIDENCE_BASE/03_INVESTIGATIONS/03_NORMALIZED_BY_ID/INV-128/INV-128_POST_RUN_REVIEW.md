---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-128-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-128"
---

<!-- DERIVED_FROM: te_run=20260906-1732-influence-for-hire; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW — INV-128

```text
P0 = 0
P1 = 0
P2 = 3
REVIEW = PASS
RENARD = NO
```

## ROBUSTE

1. `CLM-001/002/007` établit un marché commercial réel sans confondre influence-for-hire et seule influence étrangère : Archimedes, Rally Forge, STOIC, Team Jorge et Alp Services fournissent des familles distinctes de mécanismes.
2. `CLM-003 / CTRL-001` empêche de certifier le marketing de Team Jorge : capacité démontrée et actions observées sont séparées du chiffre commercial de 30 000 profils et du palmarès électoral revendiqué.
3. `CLM-004/005` sépare correctement trois étages STOIC : opérateur/action fortement attribués ; portée authentique faible ; client ministériel rapporté mais explicitement contesté.
4. `CLM-006 / CTRL-004` donne à Alp Services la chaîne client-paiement-tasking la plus dense tout en conservant le démenti du prestataire et le statut non jugé de certaines allégations.
5. `CLM-008 / CAU-001..002` refuse le saut opération -> résultat : followers, dépenses publicitaires, faux comptes ou hacking ne constituent pas une mesure de persuasion ni un contrefactuel électoral.
6. La circularité de provenance est explicitement comptée : Meta/Reuters, Story Killers Guardian/Le Monde et Abu Dhabi Secrets Mediapart/EIC ne deviennent pas plusieurs corroborations indépendantes par simple multiplication éditoriale.

## P2

1. `CLM-005` : le lien public direct ministère israélien -> STOIC reste `PARTIAL/ATTRIBUTION`. Une pièce contractuelle, comptable, administrative ou judiciaire publique pourrait le requalifier.
2. Team Jorge : les clients et les succès revendiqués doivent être fermés dossier par dossier ; la démonstration commerciale ne suffit pas.
3. `CAU-001..002` : l'effet causal sur persuasion, vote ou politique reste non identifié. Il faut des données d'exposition et un design contrefactuel, pas davantage de métriques de bots.

## RENARD

```text
RENARD = NO
```

Les résiduels ne menacent pas le modèle central et ne sont pas des trous génériques de recherche. Ils demandent soit de nouvelles pièces de client/tasking, soit des décisions judiciaires, soit des designs causaux. Continuer à chercher des exemples d'officines ou des métriques de réseaux ajouterait surtout de la redondance. Les branches matérielles sont déjà routées vers `INV-134` (attribution), `INV-140` (financement étranger indirect) et `INV-146` (symétrie alliés/adversaires).
