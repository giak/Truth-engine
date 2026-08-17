# Quintessence : SPV et bénéficiaires effectifs des parcs ENR

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-10_17-52_spv-beneficiaires-effectifs_INVESTIGATION.md` (81 lignes, 12 FCT-spv)
Date extraction : 2026-08-13 02:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé axe de piste, axe B de la PISTE ENR 07-29
- **Date source** : 2026-08-10 17:52 CEST, STATE FINAL
- **Complexité** : méthode testée sur 1 cas (Parc éolien de Moulins Holdings), GAP_SEVERITY 0.30
- **Identifiants source** : 12 FCT-spv-001 à 012, 6 SRC
- **Object** : cartographier la propriété réelle des parcs ENR via SPV et registres de bénéficiaires effectifs (RBE) [L8 (mesuré)]

## 2. Faits atomiques préservés

- FCT-spv-001 : PARC EOLIEN DE MOULINS HOLDINGS : SAS, SIREN 821 148 830, capital 10 €, RCS Strasbourg, immatriculée 29/06/2016 [L27 (mesuré)]
- FCT-spv-002 : activité déclarée 64.20Z (holdings), forme « gestion de biens » [L28 (mesuré)]
- FCT-spv-003 : dirigeants déclarés (2026) : Bhogal Joginder, Zhou Feng, Beaumont Didier [L29 (mesuré)]
- FCT-spv-004 : résultats 2024 : CA nul, EBITDA -9,2 K€, résultat net -18,4 K€ ; délai de paiement fournisseurs 298 jours [L30 (mesuré)]
- FCT-spv-005 : le RBE français est tenu par l'INPI (data.inpi.fr, navigation web, pas d'API publique agrégée) [L31 (mesuré)]
- FCT-spv-006 : accès public au RBE luxembourgeois RESTREINT depuis l'arrêt CJUE 22/11/2022 (C-37/20, C-601/20, RGPD) [L32 (mesuré)]
- FCT-spv-007 : BORIS = point d'entrée européen reliant les registres centraux [L33 (mesuré)]
- FCT-spv-008 : le cas Moulins apparaît aussi sur societe.com (holding Strasbourg, CA 0 €) [L34 (mesuré)]
- FCT-spv-009 : aucune donnée agrégée publique ne relie les SPV ENR à leurs propriétaires finaux (constat d'absence) [L35 (mesuré)]
- FCT-spv-010 : l'API RNE INPI a renvoyé une réponse minimale (139 octets) sans champ RBE : à re-tester (constat technique) [L36 (mesuré)]
- FCT-spv-011 : data.inpi.fr bloque les requêtes scriptées (Cloudflare) [L37 (mesuré)]
- FCT-spv-012 : usage de structures luxembourgeoises (S.à.r.l.) dans les parcs français : « EIH S.à.r.l. (Enbridge et CPP Investments) » [L38 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : INPI, Luxembourg Business Registers, CJUE, BORIS (Commission européenne).
**Entreprises** : Parc éolien de Moulins Holdings (dirigeants Bhogal, Zhou, Beaumont), Enbridge, CPP Investments (via EIH S.à.r.l.), Valorem, Neoen, Engie, EDF, Boralex (contexte promoteurs).

## 4. Sources externes citées

SRC-1 : Pappers (fiche Moulins, lue) + societe.com ; SRC-2 : data.inpi.fr (RBE) ; SRC-3 : ire.lu (LBR, BORIS) ; SRC-4 : inpi.fr ; SRC-5 : tests API INPI ; SRC-6 : eoliennesenmer.fr (consortiums en mer).

## 5. Chronologie datée

2016 : création Moulins Holdings (03/06) ; 2019 : LBR actif (01/03) ; 2022 : arrêt CJUE (22/11) restreint l'accès public aux RBE ; 2026 : consultation des données.

## 6. Mécanismes / chaînes causales

**M1 — La résistance par friction administrative** : la donnée de propriété réelle existe (RBE) mais sa collecte est nominative (1-3 consultations par société), le RBE INPI bloque le scraping (Cloudflare), le RBE luxembourgeois est restreint : ce n'est pas un trou noir, c'est une friction. Niveau : L2. [L31-L37 (mesuré)]
**M2 — Le signal faible de structure de portage** : capital 10 €, CA nul, résultats négatifs 4 ans, dirigeants absents des promoteurs connus : holding de portage typique, deux lectures (familiale banale vs chaîne vers acteur non identifié). Niveau : L1-L2. [L27-L30 (mesuré)]
M3 : non identifié dans la source.

## 7. Verbatim et citations

- Le RBE « est juridiquement accessible, mais son exploitation passe par des recherches nominatives société par société » [L18 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : SRC-1 à SRC-6 consultées directement (Pappers, INPI, LBR, tests API).
- **F-##** : 12/12 identifiants FCT-spv-001 à 012 préservés verbatim.
- **Méthode** : chaîne d'accès en 4 étapes (SPV → RBE INPI → RBE étranger → personne physique), levier systémique = carte « SPV × contrats de soutien CRE × RBE » (GAP-3).

## 9. Limites connues (case-limites)

- Le bénéficiaire effectif final du cas test n'est pas identifié (GAP-1) : le cas est un signal faible, pas une preuve.
- FCT-spv-006 partiel (statut d'accès à vérifier au cas par cas) ; FCT-spv-010 constat technique à re-tester.
- La rentabilité est dans la carte agrégée (GAP-3), pas dans le cas isolé.
