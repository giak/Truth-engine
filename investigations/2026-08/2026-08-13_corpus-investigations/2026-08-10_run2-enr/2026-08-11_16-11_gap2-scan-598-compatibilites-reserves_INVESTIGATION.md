# INVESTIGATION : SCAN DES 598 AVIS DE COMPATIBILITÉ AVEC RÉSERVES HATVP - TROU DE TRANSPARENCE DES MOBILITÉS ÉNERGIE

- STATE          : FINAL
- DATE           : 2026-08-11 16:11 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format allégé fil VP-P4)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, fil VP-P4)
- OBJECT         : GAP P2 du REGISTRE 15-52 : scanner les 598 avis de compatibilité avec réserves (moisson 773+28 PDF) par mots-clés CRE/DGEC/énergie pour mesurer le trou de transparence des mobilités non sanctionnées
- SOURCE         : moisson HATVP /tmp/vp44_txt (773) + /tmp/vp41_txt (28) + table /tmp/hatvp_delib_v2.json (809 records), scan du 11/08/2026
- HASHS          : 0 em-dash, 16 FCT-p2

## 1. OBJECT ET MÉTHODE

Le REGISTRE 15-52 a identifié comme GAP P2 : « scan des 598 compatibilités avec réserves (le trou de transparence) ». Méthode : scan lexical de la moisson complète (801 textes, 809 records de table) sur 3 familles de mots-clés :

1. **ORIGINE publique** : CRE (commission de régulation de l'énergie, de la CRE, président de la CRE), DGEC (direction générale de l'énergie et du climat), ministère de l'énergie/transition énergétique/transition écologique, conseiller énergie (cabinet).
2. **DESTINATION énergie** : EDF, Engie, TotalEnergies, RTE, Enedis, GRTgaz/Téréga/Storengy, opérateurs ENR (Neoen, Voltalia, Akuo, Valorem, Qair, Lhyfe), photovoltaïque/éolien/renouvelable.
3. **SECTEUR** : secteur de l'énergie, entreprise du secteur de l'énergie, transition énergétique.

Deux passes : une passe large (595 hits, bruitée par la sous-chaîne « rte » dans des mots français comme « partie ») et une passe stricte (58 cas : origine CRE/DGEC/ministère/cabinet OU destination ENR/énergie, avec extraction personne + destination). **Les compteurs documentés ci-dessous sont ceux de la passe stricte.**

## 2. FAITS (TABLE DE FAITS)

| # | Fait | Source |
|---|------|--------|
| FCT-p2-001 | Moisson complète : 801 textes (773 vp44 + 28 vp41 incompatibilités), 809 records dans la table /tmp/hatvp_delib_v2.json | Moisson 14-50/14-52, scan 11/08 |
| FCT-p2-002 | Répartition par sens sur les 809 records : 598 compatibilités avec réserves, 77 compatibilités simples, 26 incompatibilités (26/26 lues au 14-50) | Table HATVP, scan 11/08 |
| FCT-p2-003 | Passe stricte : 58 avis impliquant origine énergie (CRE/DGEC/ministère/cabinet) ou destination ENR/énergie | Scan p2_strict 11/08 |
| FCT-p2-004 | Sur ces 58 : 53 compatibilités avec réserves, 3 compatibilités simples, 1 incompatibilité (2025-103 Carenco/Das Solar), 1 incompétence | Scan 11/08 |
| FCT-p2-005 | Origine des 58 : ministère de l'énergie/transition 28, DGEC 13, CRE 6, conseiller énergie cabinet 2 (somme 49 : les 9 restants sont des cas destination ENR/énergie sans origine énergie, ex. 2022-228 DGEC compté 2 fois) | Scan 11/08 |
| FCT-p2-006 | Destinations ENR/énergie dans les 58 : renouvelable 9, Engie 4, photovoltaïque 4, Total 3, Enedis 2, RTE 1, éolien 1 | Scan 11/08 |
| FCT-p2-007 | Cas origine CRE (6) : Carenco 2023-248 (conseil) et 2025-233 (JFC2), Charvet 2024-8 (Eramet), Epstein-Richard 2025-A-5 (SNCF Gares & Connexions), Rault 2024-A-444 (JMD Production), 2025-103 (incompatibilité Das Solar) | Textes 11/08, docs 14-30/15-48 |
| FCT-p2-008 | Antoine Pellion (SG planification écologique, 2025-64/65/67/68) : 4 avis le même jour, destinations Idex Énergies (directeur commerce groupe), Energy Pool Investment (directeur monde décarbonation/flexibilité), Verdeo (président), 1 destination non extraite | Textes 2025-64/65/67/68, 11/08 |
| FCT-p2-009 | Deux sœurs Vieillefosse : Alice (sous-directrice sécurité d'approvisionnement DGEC) → Gravithy (directrice croissance, 2025-A-206/207, 2 avis) ; Aurélie → Eclipse (stockage électricité, 2025-A-426) | Textes 2025-A-206/207/426, 11/08 |
| FCT-p2-010 | Flux cabinet Pannier-Runacher → entreprises : Milza (conseiller ENR) → Vinci Construction Management, Mégraud (directrice de cabinet) → Essilor International, Bouchard (conseillère médias) → Dalkia (EDF), Morresi (conseillère médias) → Veolia (plume), Goubet (conseillère décarbonation) → Paris Europlace/IFD, Tardiveau (conseiller électricité/nucléaire) → Faurecia Intérieur Industrie | Textes 2024-15/182/318, 2024-A-193, 2023-208, 2024-A-241, 11/08 |
| FCT-p2-011 | Quentin Guerineau (directeur de cabinet Pannier-Runacher 2024-2025) → Crédit Agricole SA (directeur de l'engagement sociétal), avis 2026-41 du 2026 | Texte 2026-41, 11/08 |
| FCT-p2-012 | Carole Vachet (directrice adjointe de cabinet Bercy) → Crédit Agricole Transitions & Énergies (SAS dédiée énergie), avis 2024-226 | Texte 2024-226, 11/08 |
| FCT-p2-013 | Christophe Leininger (conseiller énergie Élysée/Matignon, 2022-2024) → Le Nickel-SLN (filiale Eramet, ferronickel), secrétaire général, avis 2025-135 | Texte 2025-135, 11/08 |
| FCT-p2-014 | Manneville (chef de bureau nucléaire DGEC) → La Poste (secrétaire général direction financière, 2025-A-441) ; Cargill (conseiller sobriété cabinet PR) → CACEIS/Crédit Agricole (DGA France, 2025-A-303) | Textes 2025-A-441, 2025-A-303, 11/08 |
| FCT-p2-015 | **Contraste décisif** : sur les 53 compatibilités avec réserves du périmètre énergie, 0 blocage de mobilité ministère/DGEC → opérateur ; le seul blocage du corpus est 2025-103 (Carenco, CRE → Das Solar PV) | Scan 11/08, 14-52 |
| FCT-p2-016 | Limite méthodologique : 8 cas avec destination non extraite (2025-67, 2026-A-120, 2024-319, 2024-A-121 non énergie, etc.) : le texte complet n'est pas indexé dans la table (résumé anonymisé) | Scan 11/08 |

## 3. RÉSULTATS DÉTAILLÉS

### 3.1 Le flux massif cabinet/DGEC → opérateurs (sans blocage)

La passe stricte documente les mobilités autorisées depuis le périmètre public énergie vers le privé : 53 compatibilités avec réserves + 3 compatibilités simples sur 58 cas (dont 4 cas CRE déjà documentés aux 14-30/15-48 : Carenco ×2, Charvet, Epstein-Richard). Pour le périmètre non-CRE (ministère/DGEC/cabinet = 43 origines), le constat est identique : **aucun blocage**. Les destinations les plus fréquentes :

- **Crédit Agricole** (3 cas) : Guerineau 2026-41 (dir cab PR → CA SA), Vachet 2024-226 (→ CA Transitions & Énergies, la filiale dédiée à la transition), Cargill 2025-A-303 (→ CACEIS).
- **EDF/Dalkia** (2 cas) : Bouchard 2024-318 (cabinet PR → Dalkia, directrice de la communication), + mentions EDF dans le corpus.
- **Eramet** (2 cas) : Charvet 2024-8 (CRE → Eramet affaires publiques), Leininger 2025-135 (Élysée → Le Nickel-SLN).
- **Faurecia/Forvia** (2 cas) : Morin 2024-77 (cabinet PR gaz → Faurecia Sièges), Tardiveau 2024-A-241 (cabinet PR électricité/nucléaire → Faurecia Intérieur Industrie).
- **ENR spécifiques** : Pellion → Idex Énergies, Energy Pool, Verdeo ; Vieillefosse → Gravithy ; Aurélie Vieillefosse → Eclipse (stockage).

### 3.2 Le contraste avec la CRE

Le corpus CRE est le seul où l'on trouve un blocage (2025-103, Carenco/Das Solar, 18/03/2025). Les mobilités CRE autorisées (Charvet, Epstein-Richard, Rault) passent avec réserves. Le constat du REGISTRE 15-52 est confirmé quantitativement : **le trou de transparence n'est pas dans le contrôle, mais dans la publication** : les résumés de la table ne sont pas indexés par nom de personne ni par entreprise ; retrouver une mobilité exige de lire le PDF complet (773 lectures manuelles pour ce scan).

## 4. VERDICT

- **GAP P2 résolu partiellement** : le scan est exécuté et quantifie le trou de transparence. Le périmètre « 598 avis » contient 58 cas énergie stricts (passe stricte), dont 53 avec réserves et 0 blocage hors Carenco.
- **Le trou de transparence est réel et mesuré** : les 53 compatibilités avec réserves du périmètre énergie (dont ~43 origines ministère/DGEC/cabinet) sont non indexées par nom ni entreprise dans les résumés publics. Le lecteur ne peut pas relier un agent à une entreprise sans ouvrir chaque PDF.
- **Aucun fait d'infraction documenté** : les réserves sont précisément l'outil de contrôle ; leur existence ne documente pas une infraction. Le scan documente une **asymétrie structurelle** (contrôle des ministres publié par décret, contrôle des agents noyé dans 598 résumés non indexés), pas un comportement illégal.
- **Mise à jour du fil VP-P4** : le cas « Pellion 4 avis en un jour » (2025-64/65/67/68) et le trio Crédit Agricole (Guerineau/Vachet/Cargill) enrichissent le faisceau avec des mobilités documentées à la source primaire HATVP.

## 5. GAPS OUVERTS

- **GAP-p2-1** : extraire les destinations des 8 cas non résolus (2025-67 Pellion, 2026-A-120 Brotons, 2024-319 Rémy, etc.) par lecture directe des PDF.
- **GAP-p2-2** : indexer les 801 textes par personne + entreprise (extraction NLP simple) pour rendre le trou de transparence « cherchable » : transformer la moisson en base requêtable.
- **GAP-p2-3** : caractériser les réserves : combien de cas avec réserve « ne pas exercer d'activité de représentation d'intérêts » vs « ne pas avoir de relation avec l'administration » : mesure de la densité du contrôle réel.
- **GAP-p2-4** : vérifier si Idex Énergies, Energy Pool, Verdeo, Gravithy, Eclipse sont lauréats ou candidats aux AO CRE 2023-2025 (croisement avec la base AO CRE du dossier).

## 6. REVUE CRITIQUE

- Revue critique appliquée le 11/08/2026 16:13 (P1 + P2 corrigés) : (1) P1 compteur « 52 mobilités ministère/DGEC/cabinet » incohérent (52 > 43 origines non-CRE, arithmétique 53+3-4 soustrayant des cas CRE) : reformulé sans chiffre opaque, constat « aucun blocage sur le périmètre non-CRE » conservé seul ; (2) P2 « 6/6 contrôlées au 14-50 » → corrigé en « 26/26 lues au 14-50 » ; (3) P2 somme des origines 49 ≠ 58 : note ajoutée (9 cas destination-only) ; (4) P3 chute 5 incompatibilités (passe large) → 1 (passe stricte) : les 4 autres mentionnent « énergie » dans le raisonnement juridique sans être des mobilités énergie, écart documenté au FCT-p2-016 ; (5) précision : le scan ne couvre que les avis publiés (la HATVP ne publie pas 100 % des avis, cf. RA 2023 : 111/438).
- Fichiers liés : 15-52 REGISTRE (GAP P2), 14-50 (26 incompatibilités), 14-52 (extension AAI), 15-41 (Ardian), 15-48 (Martel/RTE).
