# QUINTESSENCE : dgf-impact-ecart-population-metzing
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_dgf-impact-ecart-population-metzing/2026-09-20_20-08_dgf-impact-ecart-population-metzing_INVESTIGATION.md (RUN_ID 20260920-2008, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 105 COMPLEX, G0-G10 PASS, certification DELIVERY PASS par UPDATE 20260921-0830)

## 1. Métadonnées & trace source
UPDATE du run 19-21 : chiffrage DGF de l'écart de population type Metzing (678 vs 791 = 113 habitants) via barèmes et données DGCL/OFGL. 5 faits, 12 requêtes, 7 checkpoints. Réponse : chiffrable, borné, inférieur à ce que la narration publique suggère. [L9] (mesuré)

## 2. Faits atomiques préservés
- F-01 ✧ Mécanique DGF : la dotation forfaitaire évolue selon la population DGF (population authentifiée INSEE + résidences secondaires + places de caravanes) ; depuis la LF 2024 (art 240), la part CPS est transférée aux EPCI. EPI:FACT mem:a4d80cd4-f50d-4475-a1ea-44599568fa3d [L180] (mesuré)
- F-02 ✧ Série réelle Metzing 2018-2026 (OFGL) : population INSEE 631/647/656/662/669/674/678/699/715 ; population DGF 679 (2024), 700 (2025), 716 (2026) ; DGF 105 906 (2024), 109 808 (2025), 114 005 (2026) EUR ; DSR 37 919 → 43 396 EUR. EPI:FACT mem:d8dc1852-47d2-428a-a230-515e589c141f [L181] (mesuré)
- F-03 ✧ Élasticités forfait/population DGF de Metzing : 94,6 (2022-23), 84,5 (2023-24), 12,9 (2024-25, année de rattrapage), 89,4 (2025-26) EUR/hab ; médiane 86,9 EUR/hab, cohérente avec la plage DGCL 2015 (64,46-128,93). EPI:FACT mem:a56355d3-84c3-4622-84e4-1439ab5348a0 [L182] (mesuré)
- F-04 ✦ Chiffrage central : 113 habitants d'écart ≈ 9 800 EUR/an sur la dotation forfaitaire (élasticité médiane 86,9 EUR/hab) ; plage 7 300-14 600 EUR/an (plage DGCL) ; majorant ~18 000 EUR/an rapporté à la DGF totale par habitant (159,22 EUR/hab 2026) ; corroboration régionale Bouzonville. EPI:FACT mem:db3dbddc-8baa-4ce0-8236-5dc16959beec [L183] (mesuré)
- F-05 ✧ Rattrapage réel : population INSEE de Metzing 678 (2024) → 699 (2025) → 715 (2026), +37 hab en deux ans (+5,5 %) ; la population DGF suit (679 → 700 → 716) et la DGF totale progresse de +7,6 %. EPI:FACT mem:69edb1f7-8251-4e9f-9072-e985b9c618ec [L184] (mesuré)Traces registre : premier fait à la ligne 180, dernier à la ligne 184 de la source [L180-L184] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-005→F-05 (mesuré).

## 3. Acteurs nominaux
Insee ; DGCL ; OFGL ; commune de Metzing (Moselle) ; Sénat (question Mizzon) ; AMF ; maire-info ; moselle.tv ; mairie de Metzing (dénombrement 791).

## 4. Sources externes citées
Page canonique DGCL (collectivites-locales.gouv.fr) ; API OFGL dotations-communes (séries réelles) ; note DGCL relayée par maire-info (modes de calcul) ; question sénatoriale Mizzon (qSEQ24100104S) et réponse ministérielle ; communiqué préfectoral des Landes (DGF 2026) ; AMF (montants DGF 2025) ; moselle.tv (Bouzonville) ; Wikipédia (recensement). [L25] (mesuré)

## 5. Chronologie datée
2018-2026 : série OFGL Metzing. 2020 : recensement terrain 665. 2024 : écart documenté 678 vs 791 ; question sénatoriale ; réponse ministérielle (24 juin 2025). 2024 : LF art 240 (CPS aux EPCI). 2025-2026 : rattrapage (+37 hab) et hausse de dotation.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Écart d'estimation → population DGF inférieure → dotation forfaitaire inférieure, au taux ~86,9 EUR/hab dans la strate. Preuves : F-01, F-03, F-04. Verrou : mécanique légalisée. [L180, L182, L183] (mesuré)
- M2 (L2) : Rotation 1/5 du recensement → retard de collecte → sous-estimation transitoire → rattrapage au fil des vagues (+37 hab). Preuves : F-05, F-02. Verrou : méthodologique, auto-correctif lent. [L184, L181] (mesuré)
- M3 (L2) : Écrêtement et règles de partage (PF > 85 % de la moyenne nationale ; CPS aux EPCI depuis 2024) modulent l'effet brut par commune. Preuves : F-01 (et dgcl FCT-005). Verrou : législatif. [L180] (mesuré)

## 7. Verbatim et citations
- « le montant de la dotation globale de fonctionnement est calculé sur la base du niveau de sa population » (réponse ministérielle, question Metzing) (estimé).
- « une centaine d'habitants en moins prive la commune de près de » (moselle.tv, Bouzonville, corroboration régionale) (estimé).

## 8. Notes méthodologiques source
Le chiffrage 9 800 EUR/an est un produit d'élasticités mesurées sur séries réelles OFGL, borné par la plage DGCL, corroboré par un cas régional famille D. Il est présenté comme borne, pas comme perte subie : le rattrapage réel (F-05) est documenté en parallèle. Écart 2024-25 atypique (12,9 EUR/hab, année de rattrapage) signalé. [L59] (mesuré)

## 9. Limites connues de cette extraction (case-limites)
Un seul cas communal complet (Metzing) : illustration, pas prévalence ; l'élasticité varie par strate et par année ; la question du contentieux juridique des populations légales reste ouverte ; traces [Lxx] estimées.
