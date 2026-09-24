NARRATIVE_START

# Revalidation DGF Metzing - UPDATE certifié 2.10.6

## Objet

Le run parent (`20260920-2008`) avait chiffré l'impact d'un écart de population sur la dotation forfaitaire à partir de la commune de Metzing (57) : élasticités mesurées de 12,9 à 94,6 EUR/hab DGF ajouté, chiffrage central de ~9800 EUR/an pour un écart de 113 habitants (question sénatoriale Mizzon), mécanique fondée sur la population DGF (population INSEE authentifiée + résidences secondaires + places de caravanes) avec écrêtement des communes dont le potentiel fiscal dépasse 85 % de la moyenne nationale. Ce run UPDATE revalide l'ensemble sous le flux certifié 2.10.6.

## Résultat de revalidation

Les cinq faits du parent survivent au re-FETCH du 2026-09-21 :

- **Mécanique (CONFIRMÉ)** : la page canonique DGCL re-fetchee redonne la construction de la population DGF, l'écrêtement 85 % et le transfert CPS aux EPCI depuis la LF 2024.
- **Série Metzing (CONFIRMÉE)** : l'API OFGL redonne pop INSEE 631 → 715 (2018-2026), pop DGF 679/700/716 (2024-2026) et DGF 70565 → 114005 EUR.
- **Élasticités (CONFIRMÉES)** : 94,6 (2022-23), 84,5 (2023-24), 12,9 (2024-25, année de rattrapage), 89,4 EUR/hab (2025-26).
- **Chiffrage 113 hab (CONFIRMÉ)** : ~9800 EUR/an (élasticité médiane 86,9 ; plage de barème 7300-14600), corroboré par la question sénatoriale et la presse régionale (Bouzonville ~30 kEUR pour ~une centaine d'habitants).
- **Rattrapage (CONFIRMÉ)** : +37 habitants INSEE en deux ans (678 → 715), symptôme du rattrapage des communes sous-recensées.

Le détail des notes DGCL 2026 (modes de calcul, part population, part CPS) est traité par l'UPDATE frère certifié du même jour (`20260921-0731 dgcl-notes-elasticite-part-population`), qui a également confirmé le chiffrage du présent parent.

## Vérification

Les trois requêtes de réfutation formelles (série OFGL révisée ? formule modifiée ? écrêtement supprimé ?) ne retournent aucune contradiction. Le recoupement croisé Sénat/moselle.tv/OFGL reste convergent avec l'élasticité mesurée.

## Limites

Le chiffrage marginal reste sensible à l'élasticité annuelle (rattrapage 2024-25 à 12,9 EUR/hab). La fiche nominative de calcul n'est pas publique. L'écrêtement ne concerne pas Metzing (PF sous le seuil).

## Verdict

Le parent est confirmé sur toutes ses valeurs. Run certifiable : sources officielles inspectées le jour de la livraison, corroboration croisée maintenue, réfutations vides.

NARRATIVE_END
