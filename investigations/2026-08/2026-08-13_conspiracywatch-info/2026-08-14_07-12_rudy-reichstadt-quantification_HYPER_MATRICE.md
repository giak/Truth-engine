# QUANTIFICATION — Financement public réel de l'Observatoire du conspirationnisme

**RUN_MANIFEST**
ENGINE_VERSION:2.8 | STATE:FINAL | RUN_ID:20260814-0712-rudy-reichstadt-quantification | PARENT_RUN_ID:20260814-0701-rudy-reichstadt-faisceaux
AS_OF:2026-08-14 | MISSION_MODE:INVESTIGATION | SUBJECT_SLUG:rudy-reichstadt-quantification
OBJET : quantifier le financement public réel (2017-2025) via les données primaires, et trancher le % exact.
MÉTHODE : KERNEL v2.8. Sources primaires = data.economie.gouv.fr (annexe Jaune « Effort financier de l'État en faveur des associations ») + rapport DILCRAH 2023.

---

## §1 DONNÉES PRIMAIRES OBTENUES (annexe Jaune, exercice 2023)

Source : data.economie.gouv.fr, dataset `plf25-donnees-de-l-annexe-jaune-effort-financier-de-l-etat-en-faveur-des-associations`, filtre SIREN `805407194`. **✦ (primaire, API interrogée le 14/08/2026).**

| Programme | SIREN | Dénomination | Montant | Objet déclaré |
|---|---|---|---|---|
| 129 | 805407194 | OBSERVATOIRE DU CONSPIRATIONNISME | **30 000 €** | « Accompagner l'organisation d'un concours international de dessin de presse contre le conspirationnisme et le négationnisme » |
| 216 | 805407194 | OBSERVATOIRE DU CONSPIRATIONNISME | **15 000 €** | « Prévention de la Radicalisation » |

**Total visible dans l'annexe Jaune (2023) : 45 000 €.** Établissement : Paris 11e, catégorie juridique 9220 (association loi 1901).

## §2 CE QUE CES DONNÉES ÉTABLISSENT ET CORRIGENT

1. **CONFIRMÉ** : l'association est bien subventionnée par l'État en 2023 (45 000 € visibles en primaire).
2. **RÉFUTATION PARTIELLE du « concours de dessin fantôme »** (allégation Rechecking, FCT-028 ⁕) : l'annexe Jaune 2023 enregistre explicitement **30 000 €** pour le concours de dessin en 2023. L'allégation « plus aucune trace après 2020 » est **fausse pour 2023**. Le concours existe et est financé.
3. **CONFIRMÉ** : le financement « prévention de la radicalisation » (CIPDR/SG-CIPDR) existe en 2023 (15 000 €, programme 216).

## §3 CE QUE CES DONNÉES NE TRANCHENT PAS (GAP honnête)

1. **Les années 2017-2022 sont NON reproductibles en primaire.** Les datasets annexe Jaune PLF 2018-2022 interrogés via l'API renvoient `total_count: 0` (vides) ou sont agrégés (`plf24` = 111 lignes agrégées, sans donnée par association). Les montants « DILCRAH 30 k€/an depuis 2017, CIPDR 30→60 k€, Culture 20 k€, total ≥130 k€/an » avancés par Rechecking (SRC-004) **ne peuvent pas être reproduits** depuis l'open data actuelle pour ces années. Statut : ⁕ non confirmé en primaire, non réfuté.
2. **L'annexe Jaune ne capture pas la totalité du financement public.** Les « co-financements d'actions » (DILCRAH « Les Déconspirateurs », CIPDR « Riposte ») confirmés par le Sénat (SRC-002) et le rapport DILCRAH 2023 (existence, cf. §4) n'apparaissent **pas** en 2023 dans l'annexe Jaune au-delà des 45 k€. Soit ils sont classés en « prestations/conventions » hors annexe Jaune, soit leurs montants 2023 sont inférieurs à 45 k€ au total, soit ils sont sous une autre entité/SIREN.

## §4 RAPPORT DILCRAH 2023 (primaire, PDF officiel)

Le rapport d'activité DILCRAH 2023 liste « Observatoire du conspirationnisme » parmi ses bénéficiaires/partenaires, et décrit « Les Déconspirateurs – l'émission », « co-animée par Rudy Reichstadt et Tristan Mendès-France, présentée par David Medioni », « lancée à l'automne 2021 par Conspiracy Watch ». **Le rapport ne publie pas de montant individuel** pour CW dans le texte accessible. L'enveloppe globale DILCRAH 2023 est de 2,6 M€ (pour l'ensemble de ses actions, pas pour CW seul).

## §5 CONCLUSION QUANTITATIVE (honnête, bornée)

**Le % exact de financement public est INDÉCIDABLE à partir des données primaires publiques actuellement accessibles.** Trois chiffres coexistent, aucun n'est pleinement vérifiable :

| Chiffre | Source | Statut |
|---|---|---|
| ~50 % (plafond auto-imposé) | Reichstadt, Sénat 30/05/2023 | ✦ (déclaration sous serment), non vérifiable (comptes non publiés) |
| 56,5 % (130 k€/230 k€) | Rechecking Media | ⁕ (non reproduisible en primaire 2017-2022) |
| 45 000 € (annexe Jaune 2023) | data.economie.gouv.fr | ✦ (primaire, mais capture incomplète) |

**Ce qui est établi** : financement public confirmé en existence et en montant partiel (45 k€ 2023 + DILCRAH/CIPDR co-financements d'existence confirmée). **Ce qui ne l'est pas** : le total annuel exact et le % réel. Le débat « 50 % vs 56,5 % » est **indécidable en l'état des primaires** : le premier est une déclaration non auditée par des comptes publiés, le second une interprétation critique non reproduisible depuis l'open data.

**La vraie anomalie** (documentée) : une association de 3-5 salariés, au budget déclaré de ~230 k€, **ne publie pas ses comptes**, alors que son financement public est substantiel et contesté. C'est ce défaut de publication — plus que le chiffre exact — qui rend le % invérifiable.

---

## REQUEST_LOG

| # | ACTION | RESULT |
|---|---|---|
| 1 | API catalog data.economie.gouv.fr (annexe Jaune) | FOUND 14 datasets |
| 2 | API records plf25, search « conspirationnisme » | FOUND 2 enregistrements (45 k€) |
| 3 | API records plf18-plf22-plf24, filtre SIREN | EMPTY/AGRÉGÉ (0 ou données agrégées) |
| 4 | DILCRAH rapport 2023 PDF (pdftotext) | FOUND bénéficiaire, montant individuel absent |

---

*Dossier de quantification — KERNEL v2.8. Données primaires distinguées des allégations. Le % exact reste indécidable ; le défaut de publication des comptes est, lui, établi.*
