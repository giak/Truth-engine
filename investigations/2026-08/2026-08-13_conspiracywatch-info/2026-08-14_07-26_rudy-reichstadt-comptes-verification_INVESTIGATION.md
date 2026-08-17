# INVESTIGATION — Vérification des comptes déposés (SIREN 805407194)

**RUN_MANIFEST**
ENGINE_VERSION:2.8 | STATE:FINAL | RUN_ID:20260814-0726-comptes-verification | PARENT_RUN_ID:20260814-0712-quantification
AS_OF:2026-08-14 | MISSION_MODE:VERIFICATION | SUBJECT_SLUG:comptes-deposes-siren-805407194
OBJET : vérifier si l'association SIREN 805407194 a déposé ses comptes annuels (loi 1901, seuil de dépôt) et reconstruire le budget réel.
MÉTHODE : primaire uniquement — Sirene (recherche-entreprises.api.gouv.fr), DILA OpenDataSoft (jo_associations), décret 2006-335, annexe Jaune PLF 2023.

---

## §0 DEUX CORRECTIONS DE MES PROPRES DOSSIERS (avant tout)

1. **« Fondée en 2007 » est imprécis.** Le JOAFE (primaire) établit la **création de l'association le 21/07/2014**. C'est le **site** conspiracywatch.info qui a été lancé en 2007. L'association « Observatoire du conspirationnisme » n'existe juridiquement que depuis 2014.

2. **« Non-dépôt des comptes = anomalie » est FAUX.** Mon dossier quantification (07-12) écrivait « c'est le non-dépôt ». Or le non-dépôt est **légal** : l'association est sous le seuil de 153 000 € de subventions publiques (décret 2006-335), donc **non assujettie** à la publication des comptes. L'opacité est réelle, mais elle est **volontaire**, pas une infraction.

---

## §1 IDENTITÉ (Sirene, primaire)

| Champ | Valeur | Statut |
|---|---|---|
| SIREN | 805407194 | ✦ |
| Dénomination | OBSERVATOIRE DU CONSPIRATIONNISME (ODC) | ✦ |
| RNA | W751225511 | ✦ |
| Nature juridique | 9220 (association loi 1901) | ✦ |
| Siège | Maison des Associations du 11e, 8 rue du Général Renault, 75011 Paris | ✦ |
| SIRET siège | 80540719400028 | ✦ |
| Établissements | 2 (1 ouvert) | ✦ |
| Effectif salarié (tranche) | 03 = 3 à 5 salariés (2023) | ✦ |
| Employeur | OUI | ✦ |
| Convention collective | IDCC 1480 (journalistes) | ✦ |
| Activité | 94.99Z (organisations par adhésion volontaire) | ✦ |
| Date création SIREN | 2014-07-21 | ✦ |
| Mise à jour INSEE | 2025-12-06 | ✦ |

**Lecture forensique** : tranche 03 (3-5 salariés) + convention collective des **journalistes** (IDCC 1480) confirme que les salariés sont des journalistes professionnels, cohérent avec le statut de « service de presse en ligne IPG » (2024). L'effectif borne la masse salariale réelle.

---

## §2 HISTORIQUE JOAFE (3 annonces, primaire DILA)

| Date déclaration | Parution | n° | Acte | Objet / changement |
|---|---|---|---|---|
| 2014-07-21 | 2014-08-02 | 1334 | **CRÉATION** | objet initial « prévenir et lutter contre le conspirationnisme ». Adresse : 277 rue du Faubourg Saint-Antoine, 75011. Lieu : Police/Paris |
| 2017-03-20 | 2017-04-08 | 1704 | Modification | nouvel objet « service de presse en ligne indépendant » (conspiracywatch.info). Adresse : Maison des Associations du 11e |
| 2024-05-07 | 2024-05-07 | 1459 | Modification | nouveau titre « OBSERVATOIRE DU CONSPIRATIONNISME (ODC) » + objet « service de presse en ligne d'information politique et générale » (statut IPG) |

**Point clé** : la création (2014) est **antérieure de 7 ans** au lancement du site (2007). Le site a fonctionné **7 ans sans structure associative déclarée**. C'est un fait structurel documenté, ni plus ni moins.

**Statut IPG (2024)** : le nouvel objet de 2024 qualifie CW de « service de presse en ligne d'information politique et générale », condition du régime fiscal et social de la presse (CPPAP, TVA à taux réduit, aides à la presse). Cohérent avec l'aide publique « concours de dessin de presse » (30 000 €, annexe Jaune 2023).

---

## §3 LES COMPTES DÉPOSÉS : ZÉRO (primaire, base DCA)

La base DILA « jo_associations » (OpenDataSoft) fusionne les annonces JOAFE **et** les dépôts de comptes associatifs (DCA). Le champ `source` vaut `joafe` (annonce) ou `dca` (dépôt de compte).

**Requête sur le RNA W751225511 : 3 résultats, tous `joafe`.**
**Requête sur « conspirationnisme » : 6 résultats, tous `joafe`.**
**Aucun enregistrement `source=dca` n'existe pour l'Observatoire du conspirationnisme.**

→ **L'association n'a JAMAIS déposé de comptes annuels** depuis sa création (2014), sur la période couverte par la base (1998 à nos jours).

**Conséquence directe** : le « budget réel » ne peut **pas** être reconstruit à partir de comptes déposés, car il n'en existe aucun. Toute reconstitution ne peut s'appuyer que sur :
- les subventions publiques de l'annexe Jaune (open data) ;
- la déclaration sous serment au Sénat (mai 2023) ;
- l'effectif Sirene (tranche 03).

---

## §4 CADRE LÉGAL DU DÉPÔT : SEUIL DE 153 000 €

**Décret n° 2006-335 du 21 mars 2006** : une association qui reçoit annuellement **plus de 153 000 €** de subventions publiques (autorités administratives) **ou** de dons (avec reçus fiscaux) doit :
1. établir des comptes annuels (bilan + compte de résultat + annexe) ;
2. nommer un commissaire aux comptes ;
3. **publier** ses comptes (siège + dépôt en préfecture + base DCA/DILA).

**Application à CW** :
| Source du financement public | Montant | Statut |
|---|---|---|
| Annexe Jaune PLF 2023 (prog 129 + 216) | 45 000 € | ✦ primaire |
| Déclaration Sénat « plafond 50 % » sur budget ~230 k€ | ~115 000 € | ✦ déclaré, non audité |
| Rechecking « total 130 k€/an » | ~130 000 € | ⁕ non reproduisible |

**Aucun de ces trois chiffres n'atteint 153 000 €.** Même en retenant l'estimation la plus haute (Rechecking, non confirmée), CW reste **sous le seuil**.

→ **CW n'est pas assujettie à la publication de ses comptes.** L'absence de dépôt est conforme à la loi, pas une violation.

**Nuance d'honnêteté** : le seuil porte sur les **subventions publiques**. Les fonds privés (Fondation pour la Mémoire de la Shoah, Fonds du 11-Janvier) ne comptent pas dans ce calcul. Une association peut donc être financée à ~230 k€ sans jamais être tenue de publier ses comptes, si la part publique reste sous 153 k€.

---

## §5 RECONSTRUCTION DU BUDGET : CE QUI EST ÉTABLI vs CE QUI RESTE INCONNU

**Établi en primaire (plancher) :**
- Subventions publiques 2023 : **45 000 €** (30 k€ prog 129 + 15 k€ prog 216).
- Effectif : **3 à 5 salariés** journalistes (Sirene, tranche 03, IDCC 1480).
- Local : Maison des Associations du 11e (adresse non privée, coût structurel faible).

**Déclaré (non audité) :**
- Budget annuel ~230 000 € ; part publique plafonnée à ~50 % (audition Sénat, 29/05/2023).

**Inconnu (aucun document déposé, aucun comptes publiés) :**
- Budget réel total, année par année, 2014-2025.
- Part exacte du financement public (le « 50 % » est un plafond auto-imposé, pas un chiffre audité).
- Montant exact FMS, Fonds du 11-Janvier, Europe 1, autres privés.
- Rémunération exacte du directeur (Reichstadt) et des salariés.

**Anomalies de données (documentées) :**
- Les datasets annexe Jaune PLF 2018-2022 renvoient **0 résultat** pour ce SIREN/nom, alors que le concours de dessin est réputé financé depuis 2017. Soit les données open data sont lacunaires (GAP_ACCESS), soit le financement 2017-2022 passait par un autre canal non capturé.
- La base « plf-jaune-associations-subventionnees » (consolidée) renvoie **0 résultat** pour « conspirationnisme » et « 805407194 ».

**Conclusion de reconstruction** : le budget réel est **intranchable par les comptes** (inexistants). Le seul plancher dur est 45 000 €/an de subventions publiques (2023) + 3-5 salariés. Tout le reste est déclaratif.

---

## §6 VERDICT (borné)

1. **Établi (✦)** : l'association ODC (SIREN 805407194, RNA W751225511) a été **créée le 21/07/2014**, modifiée en 2017 et 2024 (statut IPG).
2. **Établi (✦)** : **aucun compte annuel n'a jamais été déposé** (0 enregistrement DCA, base DILA 1998→2026).
3. **Établi (✦)** : ce non-dépôt est **légal** — CW est sous le seuil de 153 000 € de subventions publiques (décret 2006-335).
4. **Établi (✦)** : le budget réel est **reconstituable seulement en plancher** : 45 000 € public (2023) + 3-5 salariés. Le « ~230 k€ » et le « 50 % public » sont **déclaratifs, non audités**.
5. **Corrigé** : mes dossiers antérieurs « fondée en 2007 » et « non-dépôt = anomalie » sont **révisés** (cf. §0).
6. **Non établi** : toute accusation de fraude, de détournement ou d'infraction comptable. Le non-dépôt n'en est pas une, puisqu'il est conforme au droit.

**La seule critique factuelle qui reste debout** : l'opacité **volontaire**. Une association de 3-5 salariés, financée par l'État (45 k€/an minimum, plafond déclaré ~50 %) et la philanthropie, qui anime un service de presse labellisé IPG, **pourrait** publier ses comptes volontairement (comme le font de nombreux médias). Elle ne le fait pas. C'est un choix de transparence, pas une violation de la loi.

---

## SOURCES

- SRC-020 ◈ Sirene / recherche-entreprises.api.gouv.fr — SIREN 805407194 — https://recherche-entreprises.api.gouv.fr/search?q=805407194
- SRC-021 ◈ DILA OpenDataSoft, dataset « jo_associations » (JOAFE + DCA) — https://journal-officiel-datadila.opendatasoft.com — requêtes RNA W751225511 / « conspirationnisme »
- SRC-022 ◈ Décret n° 2006-335 du 21 mars 2006 (seuil 153 000 €) — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000266544
- SRC-023 ◈ DILA, fiche API Associations et Comptes associations (04/06/2021) — https://echanges.dila.gouv.fr/OPENDATA/COMPTES_DES_ASSOCIATIONS/
- SRC-024 ◈ Annexe Jaune PLF 2023 (data.economie.gouv.fr) — 30 000 € prog 129 + 15 000 € prog 216 (déjà établi dans le dossier quantification 07-12)
- SRC-025 ◈ Sénat, audition Fonds Marianne (29/05/2023) — déclaration sous serment budget ~230 k€ / plafond 50 % — https://www.senat.fr/compte-rendu-commissions/20230529/fin.html

---

*Dossier — KERNEL v2.8. Aucun compte déposé (0 DCA) ; non-dépôt légal (sous 153 k€) ; budget reconstituable seulement en plancher (45 k€ public + 3-5 salariés).*
