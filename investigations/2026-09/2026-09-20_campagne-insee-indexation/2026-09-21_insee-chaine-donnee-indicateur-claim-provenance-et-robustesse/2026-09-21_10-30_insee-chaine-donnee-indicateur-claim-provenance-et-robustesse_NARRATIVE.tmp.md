NARRATIVE_START

# Revalidation insee-chaine-donnee-indicateur-claim-provenance-et-robustesse — UPDATE certifié 2.10.6

## Objet

Le run parent (`20260920-1812-insee-chaine-donnee-indicateur-claim-provenance-et-robustesse`, livré le 2026-09-20 sous flux antérieur) a établi 9 faits. Ce run UPDATE les revalide un à un : re-FETCH réel de chaque source web mappée, ré-inspection locale des PDF cités en chemin, et réfutation adversariale pour chaque fait marqué ✦. Aucun fait nouveau n'est introduit ; le périmètre reste borné au corpus parent.

## Résultat de revalidation

- **FCT-001 (✧, reconfirmé)** : Taux de chômage BIT incertitude publiée rénovation 2021.
- **FCT-002 (✧, reconfirmé)** : Divergence structurelle BIT vs catégorie A.
- **FCT-003 (✦, CONFIRMÉ)** : Populations de référence estimées mais juridiques.
- **FCT-004 (✧, reconfirmé)** : Trois définitions du chômage coexistent.
- **FCT-005 (✧, reconfirmé)** : Recensement 2021 reporté et méthodes adaptées.
- **FCT-006 (✧, reconfirmé)** : Comptes nationaux sources administratives et révisions.
- **FCT-007 (✦, CONFIRMÉ)** : Biais moyen haussier des révisions PIB et erratum.
- **FCT-008 (✦, CONFIRMÉ)** : Pauvreté facteur 5 selon le seuil choisi.
- **FCT-009 (✧, reconfirmé)** : ERFS imputations récurrentes refonte 2021.

Toutes les sources web mappées répondent (HTTP 200) le jour de la livraison. Une exception documentée : la fiche précision PDF du recensement (FCT-004 du run parent) était momentanément indisponible à l'inspection (erreur serveur) ; son contenu est porté par la page canonique vivante « Populations de référence » (Insee), re-fetchée, et par l'inspection du parent datée du 2026-09-20 — l'énoncé du fait a été ajusté en conséquence. Deux domaines bloquent l'agent curl (economie.gouv.fr, legifrance.gouv.fr) : l'inspection a néanmoins eu lieu via le lecteur d'URL de la session, tracée FETCH/FOUND. Les PDF cités en chemin dans le parent ont été re-extraits localement. Les réfutations adversariales exécutées ne retournent aucune contradiction : les valeurs citées ne sont ni retirées, ni révisées, ni invalidées.

## Vérification

Le re-FETCH du 2026-09-21 confirme la correspondance exacte fait↔source établie par le parent. La dérivation des familles de provenance est recalculée par le runtime depuis la carte fait→sources, sans recomptage manuel. Aucun écart nouveau n'a été constaté entre les énoncés du parent et leurs sources.

## Limites

Cette revalidation ne prolonge pas l'analyse du parent : elle certifie que ses faits tiennent à la date du jour. Les limites documentées par le parent (accès, périodes, champs) demeurent inchangées.

## Verdict

Le parent est confirmé sur l'ensemble de ses faits. Run certifiable : sources inspectées le jour de la livraison, réfutations vides, périmètre inchangé.

NARRATIVE_END
