NARRATIVE_START

# Révalidation IRL et écarts loyers 2022-2025 — UPDATE certifié 2.10.6

## Objet

Le run parent (`20260920-2154`) avait établi la mécanique de l'indice de référence des loyers — moyenne sur douze mois consécutifs de l'évolution de l'IPC hors tabac et hors loyers (loi 2008-111 art. 9, création par la loi 2005-841 art. 35) — et chiffré l'écart entre l'IRL et les loyers réels sur 2022-2024, avec un transfert de l'ordre de 1,5-2 Md€/an vers les locataires en place pendant le choc, puis ~0,7 Md€ en 2024. Ce run UPDATE revalide ces résultats sous le flux certifié 2.10.6, un jour après leur production, par re-FETCH des sources primaires le jour même.

## Résultat de revalidation

Toutes les valeurs du parent survivent au re-FETCH :

- **Mécanique IRL (CONFIRMÉ)** : la fiche Insee (T3 2025, inspectée) redonne la formule exacte, documente elle-même le plafonnement de 3,5 % (loi 2022-1158 art. 12, T3 2022-T1 2024) et publie IRL T3 2025 = 145,77 (+0,87 %) ; le tableau ANIL est identique à l'arrondi près (recoupement concluant sur T3 et T4 2025).
- **Écarts 2022-2024 (CONFIRMÉ)** : IPC hors tabac +5,2 % (2022) et +4,8 % (2023) et +1,8 % (2024) réaffichés par l'IR n°6 du 15/01/2025 ; combiné aux glissements IRL (+3,27 %/+3,49 %/+2,75 % en moyenne annuelle), le différentiel IRL-IPC-HT de -1,93/-1,31/+0,95 point tient.
- **Complément 2025 (NOUVEAU)** : IPC hors tabac +0,9 % (IR n°8 du 15/01/2026, inspecté) ; IRL T/T-4 2025 en moyenne +1,02 % ; différentiel résiduel +0,12 point, la protection étant pratiquement terminée.
- **Conversion en milliards (RAFRAÎCHIE)** : sur la masse SDES de 95 Md€ de loyers réels des locataires (compte du logement 2024), la protection 2022-2023 vaut environ 1,8 puis 1,2 Md€/an pour les locataires en place ; le rattrapage 2024 environ 0,9 Md€/an.

## Continuité avec l'UPDATE frère

Le gap routé par le parent (extraire le sous-indice « loyers effectifs ») a été clos le même jour par l'UPDATE certifié `20260921-0824 cui-bono-quantification-gap-closure` : série BDM 001763530 extraite, bascule 2025 documentée (ELC +2,32 % > IRL +1,02 %). Le présent run maintient le verdict d'ensemble : ni neutralité ni avantage structurel unidirectionnel ; le transfert est conjoncturel et le rattrapage passe par les révisions annuelles.

## Hygiène mémoire et traçabilité

Les mémoires de faits du parent ont été retrouvées en mémoire (recherche MCP) : la revalidation est enregistrée en mode UPDATE avec référence à la mémoire d'origine, conformément au protocole. Les trois requêtes de réfutation formelles (formule remplacée ? cumuls falsifiés ? série IPC révisée ?) ne retournent aucune contradiction : la fiche Insee en vigueur redit la formule de 2008, les IR n°6 et n°8 convergent, aucune révision incompatible n'est documentée.

## Limites

L'IRL hexagone exclut par dérogation Outre-mer et Corse depuis T3 2022 (IRL spécifiques) ; le périmètre est déclaré à la scoping. L'ELC n'est pas extraite dans ce run — la closure est celle de l'UPDATE frère, citée comme livery liée, pas refaite ici. Les transferts en milliards restent des ordres de grandeur sensibles au périmètre de masse (95 Md€ tous locataires, dont ~60 % privé).

## Verdict

Le parent est confirmé sur toutes ses valeurs ; le complément 2025 renforce la lecture bidirectionnelle (protection 2022-2023, rattrapage 2024-2025). Le run est certifiable : sources primaires inspectées le jour de la livraison, recoupement ANIL/Insee concluant, réfutations vides, routage maintenu.

NARRATIVE_END
