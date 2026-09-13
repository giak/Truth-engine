# INV-022 — Opérations d’influence russes visant la France

## Objet et résultat borné

L’objet est la chaîne **opération → infrastructure/acteurs → exposition → effet**, pour les opérations visant matériellement la France entre 2022 et le 6 septembre 2026. Le corpus établit solidement l’existence et la persistance de plusieurs dispositifs visant la France, mais pas un effet causal démontré sur l’opinion, le comportement ou un résultat électoral. Cette frontière est portée notamment par `CLM-001`, `CLM-004`, `CLM-006`, `CAU-001` et `CAU-005`.

## Systèmes opérationnels observés

**RRN / Doppelganger.** Des clones de médias et des actifs coordonnés ciblant la France sont directement documentés (`FCT-001`, `FCT-002`, `FCT-019`). Les liens avec SDA/Structura et des autorités russes sont soutenus par plusieurs familles institutionnelles et plateforme (`FCT-003`), tout en conservant l’incertitude historique d’attribution plus forte au début de l’opération (`FCT-025`).

**Portal Kombat.** Le dispositif combine automatisation, forte volumétrie et techniques de découvrabilité (`FCT-004`, `FCT-006`). La mesure française disponible va toutefois dans le sens inverse d’une assimilation volume = audience : environ 10 700 visites pour `pravda-fr` sur le mois documenté (`FCT-005`). `CLM-002` reste donc `PARTIAL` avec un gap temporel : cette mesure n’est pas une série longitudinale 2022-2026.

**Matriochka / Operation Overload.** La cible comprend les médias, les fact-checkers et le débat français (`FCT-007`). Un effet direct est mesurable sur les intermédiaires : volume de sollicitations et travail de vérification induit (`FCT-008`, `CAU-003`). En revanche, l’effet de persuasion du public reste non établi (`FCT-009`, `CLM-003`).

**Storm-1516 / CopyCop / Storm-1679.** Le corpus documente des opérations persistantes visant élections, candidats et grands événements français (`FCT-010`, `FCT-012`, `FCT-015`, `FCT-021`, `FCT-024`, `FCT-026`). Les cas municipaux 2026 et les opérations pré-2027 observées fournissent toutefois plusieurs indicateurs de portée faible ou limitée (`FCT-013`, `FCT-014`, `FCT-026`).

## Attribution et réseau

La branche Doppelganger/SDA/Structura dispose de la convergence la plus forte : sources françaises, européennes, américaines et plateforme (`FCT-001`, `FCT-003`). Elle autorise une conclusion bornée sur cette branche, pas une généralisation à tous les modes opératoires russes étudiés.

L’attribution directe de Storm-1516 à l’unité 29155 du GRU reste plus délicate. Le rapport 2026 formule cette attribution (`FCT-016`), tandis que le rapport technique 2025 indiquait ne pas pouvoir confirmer l’implication directe de cette unité (`FCT-017`). `CLM-007` et `CAU-006` conservent donc un gap `INDEPENDENCE` : l’évolution de l’évaluation officielle est observée, mais le pont probatoire public n’est pas reproduit indépendamment.

## Exposition, audience et impact

Le corpus ne permet pas de traiter comme synonymes : nombre de contenus, actifs détectés, vues, audience, persuasion et effet politique. Plusieurs résultats vont même contre une lecture automatique de l’efficacité : faible audience Portal Kombat (`FCT-005`), capacité limitée de Matriochka à façonner l’opinion selon VIGINUM (`FCT-009`), absence d’engagement authentique positif substantiel observé par OpenAI pour les activités Doppelganger détectées (`FCT-018`), portée globalement limitée dans la synthèse VIGINUM (`FCT-022`) et faible retentissement de plusieurs opérations pré-2027 (`FCT-026`).

Le résultat le plus robuste est donc négatif : **aucun design causal ou contrefactuel public inspecté n’établit qu’une opération du corpus a causé un changement d’opinion, de comportement ou de résultat électoral en France** (`CLM-006`, `CAU-005`). Cela ne prouve pas l’absence d’effet ; cela borne ce qui peut être affirmé avec les preuves disponibles.

## Contre-mesures et effets observables

Des effets locaux de mitigation sont documentés : suspension de domaines par l’AFNIC (`FCT-013`), suppressions d’actifs par Meta (`FCT-019`) et blocages/suppressions par Google (`FCT-020`). `CAU-004` autorise une causalité locale entre action de retrait et indisponibilité des actifs concernés. `CLM-008` conserve cependant un gap causal sur l’effet dissuasif agrégé : le corpus ne permet pas d’isoler l’impact de ces mesures sur la capacité globale, la persistance ou l’audience de l’écosystème.

## Contradictions et limites actives

La contradiction matérielle principale concerne l’attribution Storm-1516 → GRU 29155 (`FCT-016` versus `FCT-017`). Elle n’est pas moyennée ni effacée. Les autres limites structurantes sont : absence de série longitudinale d’audience française pour Portal Kombat, absence de mesure causale de persuasion/comportement, topologie publique incomplète de certains réseaux et impossibilité de calculer une centralité ou un facteur d’exposition total à partir du corpus disponible.

## Conclusion technique

Le corpus permet d’établir avec des niveaux de preuve différenciés :

- des opérations répétées et adaptatives visant la France ;
- des infrastructures et relations d’acteurs documentées pour plusieurs branches ;
- des effets observables sur la disponibilité des contenus, les intermédiaires informationnels et certains actifs supprimés ;
- une exposition hétérogène, souvent faible dans les cas où elle est mesurée ;
- aucune preuve publique inspectée suffisante pour convertir cette activité en affirmation causale de persuasion ou de résultat électoral.

Les gaps conservés dans `CLM-002`, `CLM-003`, `CLM-005`, `CLM-006`, `CLM-007`, `CLM-008`, `CAU-005` et `CAU-006` constituent les points de reprise prioritaires d’une future mise à jour.
