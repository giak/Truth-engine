# Quintessence : GAP P2, scan des 598 avis de compatibilité avec réserves HATVP, trou de transparence des mobilités énergie

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-11_16-11_gap2-scan-598-compatibilites-reserves_INVESTIGATION.md` (75 lignes, 16 FCT-p2)
Date extraction : 2026-08-13 03:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé fil VP-P4, GAP P2 du REGISTRE 15-52
- **Date source** : 2026-08-11 16:11 CEST, STATE FINAL
- **Identifiants source** : 16 FCT-p2-001 à 016
- **Object** : scanner les 598 avis de compatibilité avec réserves (moisson 773+28 PDF) par mots-clés CRE/DGEC/énergie pour mesurer le trou de transparence des mobilités non sanctionnées
- **Verdict source** : GAP P2 résolu partiellement : 58 cas énergie stricts (passe stricte), dont 53 avec réserves et 0 blocage hors Carenco ; le trou de transparence est réel et mesuré (résumés non indexés par nom ni entreprise)

## 2. Faits atomiques préservés

- FCT-p2-001 : moisson complète : 801 textes (773 vp44 + 28 vp41), 809 records dans la table /tmp/hatvp_delib_v2.json [L25 (mesuré)]
- FCT-p2-002 : répartition par sens : 598 compatibilités avec réserves, 77 compatibilités simples, 26 incompatibilités (26/26 lues au 14-50) [L26 (mesuré)]
- FCT-p2-003 : passe stricte : 58 avis impliquant origine énergie (CRE/DGEC/ministère/cabinet) ou destination ENR/énergie [L27 (mesuré)]
- FCT-p2-004 : sur ces 58 : 53 compatibilités avec réserves, 3 compatibilités simples, 1 incompatibilité (2025-103 Carenco/Das Solar), 1 incompétence [L28 (mesuré)]
- FCT-p2-005 : origine des 58 : ministère de l'énergie/transition 28, DGEC 13, CRE 6, conseiller énergie cabinet 2 (somme 49 ; les 9 restants sont des cas destination ENR/énergie sans origine énergie) [L29 (mesuré)]
- FCT-p2-006 : destinations ENR/énergie dans les 58 : renouvelable 9, Engie 4, photovoltaïque 4, Total 3, Enedis 2, RTE 1, éolien 1 [L30 (mesuré)]
- FCT-p2-007 : cas origine CRE (6) : Carenco 2023-248 (conseil) et 2025-233 (JFC2), Charvet 2024-8 (Eramet), Epstein-Richard 2025-A-5 (SNCF), Rault 2024-A-444 (JMD Production), 2025-103 (incompatibilité Das Solar) [L31 (mesuré)]
- FCT-p2-008 : Antoine Pellion (SG planification écologique, 2025-64/65/67/68) : 4 avis le même jour, destinations Idex Énergies (directeur commerce groupe), Energy Pool Investment (directeur monde décarbonation/flexibilité), Verdeo (président), 1 destination non extraite [L32 (mesuré)]
- FCT-p2-009 : deux sœurs Vieillefosse : Alice (sous-directrice sécurité d'approvisionnement DGEC) → Gravithy (directrice croissance, 2025-A-206/207, 2 avis) ; Aurélie → Eclipse (stockage électricité, 2025-A-426) [L33 (mesuré)]
- FCT-p2-010 : flux cabinet Pannier-Runacher → entreprises : Milza (conseiller ENR) → Vinci Construction Management, Mégraud (directrice de cabinet) → Essilor International, Bouchard (conseillère médias) → Dalkia (EDF), Morresi (conseillère médias) → Veolia (plume), Goubet (conseillère décarbonation) → Paris Europlace/IFD, Tardiveau (conseiller électricité/nucléaire) → Faurecia Intérieur Industrie [L34 (mesuré)]
- FCT-p2-011 : Quentin Guerineau (directeur de cabinet Pannier-Runacher 2024-2025) → Crédit Agricole SA (directeur de l'engagement sociétal), avis 2026-41 [L35 (mesuré)]
- FCT-p2-012 : Carole Vachet (directrice adjointe de cabinet Bercy) → Crédit Agricole Transitions & Énergies (SAS dédiée énergie), avis 2024-226 [L36 (mesuré)]
- FCT-p2-013 : Christophe Leininger (conseiller énergie Élysée/Matignon, 2022-2024) → Le Nickel-SLN (filiale Eramet, ferronickel), secrétaire général, avis 2025-135 [L37 (mesuré)]
- FCT-p2-014 : Manneville (chef de bureau nucléaire DGEC) → La Poste (secrétaire général direction financière, 2025-A-441) ; Cargill (conseiller sobriété cabinet PR) → CACEIS/Crédit Agricole (DGA France, 2025-A-303) [L38 (mesuré)]
- FCT-p2-015 : contraste décisif : sur les 53 compatibilités avec réserves du périmètre énergie, 0 blocage de mobilité ministère/DGEC → opérateur ; le seul blocage du corpus est 2025-103 (Carenco, CRE → Das Solar PV) [L39 (mesuré)]
- FCT-p2-016 : limite méthodologique : 8 cas avec destination non extraite (2025-67, 2026-A-120, 2024-319, etc.) : le texte complet n'est pas indexé dans la table (résumé anonymisé) [L40 (mesuré)]

## 3. Acteurs nominaux

**Cabinet Pannier-Runacher / transition** : Milza, Mégraud, Bouchard, Morresi, Goubet, Tardiveau, Guerineau, Cargill, Pellion (SG planification écologique), Vieillefosse Alice et Aurélie (DGEC).
**Cabinet Bercy / autres** : Vachet, Leininger (Élysée/Matignon), Manneville (DGEC).
**Destinations** : Idex Énergies, Energy Pool Investment, Verdeo, Gravithy, Eclipse, Vinci Construction Management, Essilor, Dalkia (EDF), Veolia, Paris Europlace/IFD, Faurecia, Crédit Agricole (SA, Transitions & Énergies, CACEIS), Le Nickel-SLN (Eramet), La Poste.
**Cas CRE** : Carenco (2), Charvet, Epstein-Richard, Rault, 2025-103.

## 4. Sources externes citées

Moisson HATVP /tmp/vp44_txt (773) + /tmp/vp41_txt (28) + table /tmp/hatvp_delib_v2.json (809 records), scan du 11/08/2026 (passe large 595 hits bruitée par « rte » ; passe stricte 58 cas).

## 5. Chronologie datée

2014-2026 : 809 avis ; 2023-2026 : 58 cas énergie (2023-35 à 2026-41) ; 11/08/2026 : scan des 801 textes.

## 6. Mécanismes / chaînes causales

**M1 — Le flux massif cabinet/DGEC → opérateurs sans blocage** : 53 compatibilités avec réserves + 3 simples sur 58 cas ; pour le périmètre non-CRE (43 origines), aucun blocage ; destinations récurrentes : Crédit Agricole (3), EDF/Dalkia (2), Eramet (2), Faurecia/Forvia (2), ENR spécifiques (Pellion, Vieillefosse). Niveau : L2. [L32-L38 (mesuré)]
**M2 — Le trou de transparence dans la publication, pas dans le contrôle** : les résumés de la table ne sont pas indexés par nom de personne ni par entreprise ; retrouver une mobilité exige de lire le PDF complet (773 lectures manuelles pour ce scan). Niveau : L2. [L40 (mesuré)]
**M3 — Le contraste avec la CRE** : le seul blocage du corpus est 2025-103 (CRE → Das Solar PV) ; les mobilités CRE autorisées passent avec réserves. Niveau : L2. [L39 (mesuré)]

## 7. Verbatim et citations

- « le trou de transparence n'est pas dans le contrôle, mais dans la publication » [L52 (mesuré)]
- « le scan documente une asymétrie structurelle (contrôle des ministres publié par décret, contrôle des agents noyé dans 598 résumés non indexés), pas un comportement illégal » [L58 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : scan exécuté sur la moisson complète, deux passes (large 595 hits / stricte 58 cas) ; les compteurs documentés sont ceux de la passe stricte.
- **F-##** : 16/16 identifiants FCT-p2-001 à 016 préservés verbatim.
- **Méthode** : 3 familles de mots-clés (origine publique, destination énergie, secteur), extraction personne + destination, correction des biais (passe large bruitée).

## 9. Limites connues (case-limites)

- GAP-p2-1 : extraire les destinations des 8 cas non résolus ; GAP-p2-2 : indexer les 801 textes par personne + entreprise (rendre le trou « cherchable ») ; GAP-p2-3 : caractériser les réserves (densité du contrôle réel) ; GAP-p2-4 : vérifier si Idex/Energy Pool/Verdeo/Gravithy/Eclipse sont lauréats des AO CRE 2023-2025.
- Le scan ne couvre que les avis publiés (la HATVP ne publie pas 100 % des avis, cf. RA 2023 : 111/438).
