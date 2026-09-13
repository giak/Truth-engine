---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-135-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-135"
---

<!-- DERIVED_FROM: te_run=20260906-1842-hack-and-leak; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW — INV-135

```text
P0 = 0
P1 = 0
P2 = 3
REVIEW = PASS
RENARD = NO
```

## ROBUSTE

1. `CLM-001` casse correctement le label global « hack-and-leak » en chaîne probatoire : compromission/vol, attribution, intégrité, timing, publication, amplification, exposition, persuasion, résultat et contrefactuel ne s'héritent pas mutuellement.
2. `CLM-002/003 / CTRL-001` traite MacronLeaks avec temporalité : l'incertitude publique de 2017-2018 est conservée, tandis que l'attribution officielle française GRU/APT28 de 2025 est intégrée comme information ultérieure sans fabriquer rétroactivement une chaîne technique publique plus détaillée qu'elle ne l'est.
3. `CLM-004` sépare volume/amplification et effet électoral : l'audience MacronLeaks apparaît largement périphérique/étrangère dans le corpus inspecté, tandis que la commission électorale française n'a pas constaté d'atteinte à la sincérité du scrutin.
4. `CLM-005/006 / CTRL-003` ferme beaucoup plus haut la chaîne DNC/Podesta : GRU, vol, canaux de diffusion et timing sont fortement documentés, tout en refusant le saut vers une coordination Trump-Russie non établie ou un déclencheur causal prouvé du dump du 7 octobre.
5. `CLM-007 / CAU-001..002` distingue effet d'agenda médiatique et effet de vote. La présence des emails volés dans l'agenda est soutenue ; le nombre de votes changés et le vainqueur contrefactuel ne le sont pas.
6. `CLM-008/009 / CTRL-004` ajoute un contrôle partisan/symétrique avec Iran 2024 : le mécanisme vise cette fois la campagne républicaine, et la non-publication substantielle par plusieurs grands médias montre que le gate éditorial est une variable indépendante de l'existence du hack.

## P2

1. **MacronLeaks 2017** : l'authentification exhaustive du corpus et la chaîne technique publique détaillée reliant spécifiquement le cas 2017 à l'attribution étatique restent moins complètes que l'attribution officielle française de 2025. Recheck seulement si ANSSI, justice, opérateur ou archives techniques publient une pièce matérielle nouvelle.
2. **DNC/Podesta 2016** : le corpus établit opération et agenda, pas le contrefactuel « assez de votes pour changer le vainqueur ». Une causalité de résultat exigerait un design et des données que la recherche descriptive supplémentaire ne fournira pas.
3. **Iran 2024** : le dossier judiciaire et l'effet politique final restent susceptibles d'évoluer ; recheck à jugement, nouvelles pièces judiciaires ou données robustes d'exposition/effet.

## RENARD

```text
RENARD = NO
```

Les résiduels n'invalident pas le modèle central. Ils exigent soit des pièces techniques/judiciaires nouvelles, soit un véritable design causal. Ajouter d'autres cas de fuite ou d'autres métriques sociales serait surtout cumulatif et violerait la discipline delta-only.
