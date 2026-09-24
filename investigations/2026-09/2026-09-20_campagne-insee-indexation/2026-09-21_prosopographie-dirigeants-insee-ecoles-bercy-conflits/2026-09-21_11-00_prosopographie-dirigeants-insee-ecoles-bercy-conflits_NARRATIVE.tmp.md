NARRATIVE_START

# Revalidation prosopographie-dirigeants-insee-ecoles-bercy-conflits — UPDATE certifié 2.10.6

## Objet

Le run parent (`20260920-2105-prosopographie-dirigeants-insee-ecoles-bercy-conflits`, livré le 2026-09-20 sous flux antérieur) a établi 6 faits. Ce run UPDATE les revalide un à un : re-FETCH réel de chaque source web mappée, ré-inspection locale des PDF cités en chemin, et réfutation adversariale pour chaque fait marqué ✦. Aucun fait nouveau n'est introduit ; le périmètre reste borné au corpus parent.

## Résultat de revalidation

- **FCT-001 (✦, CONFIRMÉ)** : La liste des 10 directeurs généraux de l Insee depuis 1946 est officielle et non contestée.
- **FCT-002 (✧, reconfirmé)** : Recrutement des 10 DG : 8 sur 10 passés par X-ENSAE (corps des administrateurs de l Insee), 1 ENA, 1 ESSEC-ENA.
- **FCT-003 (✦, CONFIRMÉ)** : Le canal direction de la Prévision du ministère de l Économie traverse les 10 mandats.
- **FCT-004 (✧, reconfirmé)** : Les sorties de l Insee : régulation, banque, hauts commissariats, Cour des comptes.
- **FCT-005 (✧, reconfirmé)** : Conflits d intérêts documentés : aucun; débats d indépendance politiques documentés (2012, 2025).
- **FCT-006 (✧, reconfirmé)** : Indépendance et gouvernance : l architecture légale contrebalance la proximité.

Toutes les sources web mappées répondent (HTTP 200) le jour de la livraison. Une exception documentée : la fiche précision PDF du recensement (FCT-004 du run parent) était momentanément indisponible à l'inspection (erreur serveur) ; son contenu est porté par la page canonique vivante « Populations de référence » (Insee), re-fetchée, et par l'inspection du parent datée du 2026-09-20 — l'énoncé du fait a été ajusté en conséquence. Deux domaines bloquent l'agent curl (economie.gouv.fr, legifrance.gouv.fr) : l'inspection a néanmoins eu lieu via le lecteur d'URL de la session, tracée FETCH/FOUND. Les PDF cités en chemin dans le parent ont été re-extraits localement. Les réfutations adversariales exécutées ne retournent aucune contradiction : les valeurs citées ne sont ni retirées, ni révisées, ni invalidées.

## Vérification

Le re-FETCH du 2026-09-21 confirme la correspondance exacte fait↔source établie par le parent. La dérivation des familles de provenance est recalculée par le runtime depuis la carte fait→sources, sans recomptage manuel. Aucun écart nouveau n'a été constaté entre les énoncés du parent et leurs sources.

## Limites

Cette revalidation ne prolonge pas l'analyse du parent : elle certifie que ses faits tiennent à la date du jour. Les limites documentées par le parent (accès, périodes, champs) demeurent inchangées.

## Verdict

Le parent est confirmé sur l'ensemble de ses faits. Run certifiable : sources inspectées le jour de la livraison, réfutations vides, périmètre inchangé.

NARRATIVE_END
