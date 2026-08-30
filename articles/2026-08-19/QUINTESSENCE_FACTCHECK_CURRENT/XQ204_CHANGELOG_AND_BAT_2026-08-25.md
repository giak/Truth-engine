# XQ204 — changelog des passes A-E, rollback figures et BAT final

## État

- Candidat : `QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ204_2026-08-25.md`
- SHA-256 : `0ddd1ab44ff314d10b49be90036c360374727a2b5f6f1bb64f7e26ad6e051b4e`
- Cible : **Substack**
- Gate : `PASS_WITH_BOUNDS / READY_FOR_HUMAN_SUBSTACK_PUBLICATION_REVIEW`

## A — probatoire — VALIDÉE

- Yahoo 23/07/2021 : contenu récupéré et analysé ; contre-exemple contemporain au raccourci « ×12 ».
- *Conspiracy Watch* : contextualisation accessible datée du 16/04/2020 ; le jalon Premium du 20/04 reste borné à ce qui est vérifiable.
- Audit : `annexes/XQ204_PASS_A_PROBATIVE_PATCH_AUDIT_2026-08-25.md`.

## B — langue / terminologie — VALIDÉE

- `— = 0` ; `– = 0` dans le candidat.
- Acronymes et paramètres techniques ciblés explicités.
- Audit : `annexes/XQ204_PASS_B_LANGUAGE_TERMINOLOGY_AUDIT_2026-08-25.md`.

## C — lisibilité cognitive — VALIDÉE

- Segmentation ciblée des tunnels conceptuels.
- Ajout limité de transitions et consolidations.
- Aucun nouveau schéma ; aucun fait retiré pour simplifier.
- Audit : `annexes/XQ204_PASS_C_COGNITIVE_READABILITY_AUDIT_2026-08-25.md`.

## D — tentative figures mobile — REJETÉE

- La contrainte mobile-first n’avait pas été demandée et ne devait pas piloter le design Substack.
- Le résultat dégradait les figures canoniques : `REJECTED_VISUAL_REGRESSION / YAGNI / NO_REGRESSION_FAIL`.
- Les fichiers rejetés sont archivés sous `annexes/rejected/XQ204_PASS_D_VISUAL_REGRESSION/` pour traçabilité uniquement.

## Rollback figures — VALIDÉ

- 5 SVG + 5 PNG restaurés depuis XQ203.
- 10/10 SHA-256 identiques octet pour octet aux figures XQ203.
- L’article ne référence que les cinq PNG canoniques `figures/FIG_*.png`.
- Audit : `annexes/XQ204_FIGURE_ROLLBACK_AUDIT_2026-08-25.md`.

## E — BAT final post-rollback — PASS_WITH_BOUNDS

- 113 sources définies et 113 utilisées.
- 187 appels de citation.
- 0 citation orpheline ; 0 cible relative manquante.
- 5 références de figures canoniques ; aucune référence mobile/rejected.
- Synchronisation : registre de réparation 6 cas ; fresque 45 événements.
- SQLite : `PRAGMA integrity_check = ok`.
- Spot-check ciblé reconfirmé : Yahoo, *Conspiracy Watch*, AFP Bridle, EPI-PHARE.
- BAT : `annexes/XQ204_PASS_E_FINAL_FORENSIC_BAT_2026-08-25.md`.
- JSON BAT : `annexes/XQ204_FINAL_BAT_POST_ROLLBACK_2026-08-25.json`.

## Bornes documentaires ouvertes

1. état exact AFP Bridle avant le 29/06/2021 ;
2. original complet et historique *Fact & Furious* pharmacovigilance.

Elles restent explicitement déclarées et ne sont jamais transformées en preuves négatives.


## F — audit de conformité au brief éditorial initial — PARTIAL_FAIL

- Relecture de XQ204 contre la demande initiale de confort de lecture, typographie, définitions, archéologie et pédagogie.
- Typographie mécanique / acronymes : largement réalisés.
- Archéologie : partielle ; deux gaps importants restent ouverts et aucun inventaire exhaustif de toutes les sources bloquées n'a encore été fermé.
- Lisibilité : passe C trop minimale par rapport au brief ; 1 « Point de lecture », 1 « À retenir », 1 analogie explicite ; aucun mini-schéma nouveau.
- Gate réouverte : `HOLD_FOR_EDITORIAL_COMPLETION`.
- Audit : `annexes/XQ204F_EDITORIAL_BRIEF_FULFILLMENT_AUDIT_2026-08-25.md`.
