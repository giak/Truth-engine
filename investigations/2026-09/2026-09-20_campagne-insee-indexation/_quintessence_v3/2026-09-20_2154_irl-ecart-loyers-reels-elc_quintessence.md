# QUINTESSENCE : irl-ecart-loyers-reels-elc
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_irl-ecart-loyers-reels-elc/2026-09-20_21-54_irl-ecart-loyers-reels-elc_INVESTIGATION.md (RUN_ID 20260920-2154, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 95 COMPLEX, G0-G10 PASS, certification DELIVERY PASS par UPDATE 20260921-0826)

## 1. Métadonnées & trace source
UPDATE du run 21-10 : chiffrage de l'écart IRL / loyers réels (ELC, OLAP, Clameur) et conversion du transfert locataires-bailleurs en milliards d'euros par an ; recheck matériel de la mécanique IRL (FCT-002 parent). 2 faits, 11 requêtes, 7 checkpoints. Titre de conclusion du run : « le siphon cherché n'existe pas » (sous cette forme simple). [L9] (mesuré)

## 2. Faits atomiques préservés
- F-01 ✦ Mécanique IRL : moyenne 12 mois de l'IPC hors tabac ET hors loyers (loi 89-462 art 17-1) ; IRL T2 2026 = 148,37 (+1,15 % sur un an) ; le loyer des 7 millions de ménages locataires du privé suit les prix HORS leurs loyers : la composante la plus lourde du budget logement est exclue de sa propre indexation. EPI:FACT mem:d3f212f5-4b6e-4859-a07e-f938d4d1c47d [L166] (mesuré)
- F-02 ✧ Écart IRL / loyers réels 2022-2025 : protection puis rattrapage. Écart IRL-IPCHT annuel moyen : 2022 = -1,93 pt ; 2023 = -1,30 pt ; 2024 = +0,76 pt. IRL plafonnée à 3,5 % (loi 2022-1158 art 12) pendant que l'IPC hors tabac faisait +5,2 % (2022) et +4,9 % (2023) : le plafond a TRANSFÉRÉ aux locataires ~1,9 pt/an de croissance réelle non perçue sur 2022-2023, soit de l'ordre de 1,5 à 2 Md€/an sur la masse des loyers réels (95 Md€, SDES 2024). EPI:FACT mem:eb0a687b-43d5-4763-b921-a688df2c2d97 [L167] (mesuré)Traces registre : premier fait à la ligne 166, dernier à la ligne 167 de la source [L166-L167] (mesuré).
Inventaire source : FCT-001→F-01, FCT-002→F-02 (mesuré).

## 3. Acteurs nominaux
Insee ; ANIL ; UNPI/Clameur ; OLAP ; SDES ; Service-Public.gouv.fr ; législateur (loi 89-462, loi 2022-1158) ; ménages locataires (7 millions, privé) ; bailleurs. [L132] (mesuré)

## 4. Sources externes citées
Fiche Insee IRL (8655863) ; tableau ANIL de l'IRL ; dossier de presse Clameur (UNPI, 18-11-2025) ; Rapport du compte du logement 2024 (SDES) ; Service-Public F13723 ; Insee information 1300612 ; Insee IR 8330913. [L17] (mesuré)

## 5. Chronologie datée
1989 : loi 89-462 (art 17-1, formule IRL). 2022 : plafonnement IRL 3,5 % (loi 2022-1158 art 12), applicable T3 2022-T1 2024. 2022-2023 : IPC-HT +5,2/+4,9 %, IRL plafonnée. 2024 : bascule de signe de l'écart (+0,76 pt). 2024 : masse loyers réels 95 Md€ (SDES). T2 2026 : IRL 148,37 (+1,15 %). [L3] (mesuré)

## 6. Mécanismes / chaînes causales
- M1 (L2) : Formule IRL excluant les loyers → l'indice de révision ne mesure pas la variable qu'il indexe → divergence structurelle possible entre loyers en place et loyers de marché. Preuves : F-01. Verrou : législatif. [L166] (mesuré)
- M2 (L2) : Plafond exceptionnel 3,5 % en haute inflation → transfert temporaire vers les locataires en place (~1,5-2 Md€/an 2022-2023) → rattrapage ensuite par les révisions aux baux (bascule de signe 2024). Preuves : F-02. Verrou : législatif, conjoncturel. [L167] (mesuré)

## 7. Verbatim et citations
- « le loyer des 7 millions de ménages locataires du privé suit les prix HORS leurs loyers » (formulation du run, F-01) (mesuré au sens source). [L166] (mesuré)
- « le siphon cherché n'existe pas » (titre du run : le transfert permanent unidirectionnel cherché n'est pas documenté ; le transfert réel est conjoncturel et bidirectionnel) (mesuré au sens source).

## 8. Notes méthodologiques source
Le run réfute la version simple du « siphon » (transfert structurel permanent bailleurs→locataires via la formule IRL) et documente un transfert conjoncturel à double sens. La masse 95 Md€ sert de support de bornage. Les séries ELC fines (2019-2025) sont extraites dans le run cui-bono (closure du gap quantitatif). [L4] (mesuré)

## 9. Limites connues de cette extraction (case-limites)
Écart calculé en moyenne annuelle sur IPC-HT, pas sur la formule exacte IRL glissement T/T-4 pour tous les trimestres ; la distribution du transfert entre types de baux (révision vs loi 48-10) n'est pas documentée ; traces [Lxx] estimées.
