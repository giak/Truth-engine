# Quintessence : CONFITE : échéance naturelle de l'habilitation (07/11/2025) non renouvelée : la BPI garde ses 4 autres accès CSS

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_confite-disparition/2026-08-10_09-53_confite-disparition_INVESTIGATION.md` (9 FCT-001..009)
Date extraction : 2026-08-13 06:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc connaissance patrimoniale (CSS)
- **Date source** : 2026-08-10 09:53 CEST, STATE FINAL
- **Identifiants source** : 9 FCT-001..009
- **Object** : pourquoi le projet CSS CONFITE (BPI, transmissions d'entreprises) a disparu de la liste avril 2026 : échéance naturelle, retrait ou refus ?
- **Verdict source** : échéance naturelle non renouvelée (hypothèse la plus probable) : fin d'habilitation 07/11/2025, FAQ prévoit l'expiration sans prolongation ; la BPI conserve ≥ 4 autres habilitations : la disparition est spécifique au projet

## 2. Faits atomiques préservés

- FCT-001 : la colonne date de l'Excel 251106 correspond à la « date fin habilitation » (en-tête de colonne, shared string n° 2), même sémantique que le PDF 260402 [L45 (mesuré)]
- FCT-002 : CONFITE a une date de fin d'habilitation au 07/11/2025 (sérial Excel décodé) ; la liste Excel est datée du 06/11/2025, soit un jour avant l'échéance : CONFITE figurait au dernier jour de validité [L46 (mesuré)]
- FCT-003 : l'habilitation initiale CSS dure 6 ans (depuis décembre 2016 ; avant = 3 ans) : une habilitation finissant le 07/11/2025 a donc été accordée vers novembre 2019 (déduction) [L47 (mesuré)]
- FCT-004 : la FAQ CSS alerte : « si la demande de prolongation n'est pas formulée à temps, vous risquez une interruption de votre accès aux sources. Aucune dérogation ne sera accordée » : l'arrêt à échéance est un scénario explicitement prévu [L48 (mesuré)]
- FCT-005 : CONFITE est absent du PDF d'avril 2026 (grep = 0), 5 mois après sa date de fin [L49 (mesuré)]
- FCT-006 : la BPI a conservé au moins 4 autres habilitations CSS dans le PDF avril 2026 (5 avec PROCRED) : DISPBPI (07/10/2031), EVALBPI (21/12/2027), un projet PIA, FIPENIT (06/07/2027) : la disparition de CONFITE est spécifique au projet [L50 (mesuré)]
- FCT-007 : aucune trace de CONFITE sous une nouvelle dénomination dans le PDF avril 2026 (« contrainte de financement », « transmissions d'entreprises », « CONFITE » = 0) [L51 (mesuré)]
- FCT-008 : la Wayback ne permet pas de retrouver les listes antérieures (CDX timeout/résultat vide) : la chronologie complète reste inaccessible [L52 (mesuré)]
- FCT-009 : le CSS ne publie pas les motifs de fin d'habilitation (retrait, refus, non-renouvellement) : un refus ou un retrait ne serait pas documenté publiquement [L53 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : Comité du secret statistique (CSS, secrétariat), Banque Publique d'Investissement (BPI, CONFITE + DISPBPI + EVALBPI + PIA + FIPENIT + PROCRED), Wayback Machine.

## 4. Sources externes citées

Excel ListeProjets_251106.xlsx (ROW 1097 décodée), PDF ListeProjets260402.pdf, FAQ CSS (l. 31-33, 41), dossier 09-19 (CSS), CDX Wayback (tentée).

## 5. Chronologie datée

~11/2019 : accord d'habilitation CONFITE (déduction 6 ans) ; 06/11/2025 : liste Excel (CONFITE présent, dernier jour) ; 07/11/2025 : fin d'habilitation ; 02/04/2026 : PDF 260402 (CONFITE absent) ; 10/08/2026 : verdict échéance naturelle.

## 6. Mécanismes / chaînes causales

**M1 — L'échéance naturelle documentée** : la sémantique de la colonne (date fin), le décodage du sérial (07/11/2025), l'alerte de la FAQ et la présence au dernier jour de validité convergent vers la non-reconduction à échéance. Force : EXTRÊME. Niveau : L1. [L45-L48 (mesuré)]
**M2 — La spécificité projetuelle** : la BPI conserve 4-5 autres habilitations : la disparition de CONFITE n'est pas une perte générale d'accès BPI, écartant le récit « conflit BPI/CSS ». Force : EXTRÊME. Niveau : L1. [L50 (mesuré)]
**M3 — L'opacité des motifs** : le CSS ne publie ni retrait ni refus : un non-renouvellement délibéré ne serait pas distinguable d'un abandon : la borne reste ouverte (retrait/refus non exclu, non documenté). Force : HAUTE. Niveau : L2. [L53 (mesuré)]

## 7. Verbatim et citations

- « si la demande de prolongation n'est pas formulée à temps, vous risquez une interruption de votre accès aux sources. Aucune dérogation ne sera accordée » (FAQ CSS) [L48 (mesuré)]
- « La disparition de CONFITE est spécifique au projet, pas une perte générale d'accès de la BPI au CSS » [L50 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : en-tête Excel lu, sérial décodé, FAQ lue, grep PDF (0), 5 projets BPI vérifiés (l. 2405, 11762, 12382, 13580, 17106) ; bias test 4/75 ; P6 (documentation publique BPI) clôturé sans livraison (borné).
- **F-##** : 9/9 identifiants FCT-001..009 préservés.
- **Méthode** : sémantique de colonne, décodage sérial, croisement 2 listes + FAQ, constats d'absence (FCT-005, 007, 008), CRÉDO distinguant documenté/probable/non exclu.

## 9. Limites connues (case-limites)

- Le retrait ou le refus de renouvellement n'est pas exclu (motifs non publiés par le CSS) : l'échéance naturelle est l'hypothèse la plus probable, pas une preuve.
- La date d'accord exacte de l'habilitation (≈ nov. 2019) est une déduction de la règle des 6 ans, non documentée dans l'Excel.
- La Wayback indisponible : les listes antérieures à nov. 2025 restent inaccessibles.
- La documentation publique BPI (presse) n'a pas été livrée au moment de la clôture.
