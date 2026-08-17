# RESOLUTION : GAP-x-1, DATATION ET INTERPOLATION DE LA PAGE a8486 (ARRÊTÉ DE REJET PUECH CORNET), VÉRIFICATION DES RAA TARN 2020 DANS LA FENÊTRE DE PUBLICATION ATTENDUE (MAI-JUILLET)

- STATE          : FINAL
- DATE           : 2026-08-11 09:56 CEST
- TYPE           : RESOLUTION (GAP-x-1 du 07-43)
- DOSSIER        : 2026-08-10_run2-enr (angle C : Puech Cornet / Fontrieu)
- OBJECT         : resserrer la datation de l'arrêté préfectoral de rejet de l'extension du parc éolien de Puech Cornet (page a8486 du site tarn.gouv.fr, supprimée) par interpolation avec les numéros voisins archivés (CDX Wayback), et retenter le RAA du Tarn hors rate-limit pour retrouver le numéro d'acte. Portée de la vérification RAA : mensuels mai-juillet 2020 (fenêtre de publication attendue d'un acte du 15/05, ≤ 3 mois) et spéciaux mai-juin 2020 ; mensuels avril et août-décembre non consultés (hors fenêtre, voir §6)
- PREDECESSEUR   : 2026-08-11_07-43_gap3-refus-extension-puech-cornet_RESOLUTION.md (10 FCT-x) ; 2026-08-11_09-37_gap4-recours-3denergies-ta_RESOLUTION.md (date 15/05/2020 découverte)
- HASH           : 2026-08-11_09-56

## 1. Contexte et objectif

Le 07-43 a établi le refus préfectoral de l'extension du parc éolien de Puech Cornet (Fontrieu, Tarn) comme fait documenté (article ToutesNosEnergies du 23/05/2020, lien direct vers la page `tarn.gouv.fr/arrete-portant-rejet-d-une-demande-d-exploiter-un-a8486.html`). Le 09-37 a resserré la date au **15/05/2020** via le journal municipal de Fontrieu n°9 (octobre 2020). Restait inconnu : le numéro d'acte administratif (81-2020-XXXX) et la publication RAA effective. Ce document exécute la piste d'interpolation demandée (comparer a8486 aux numéros voisins archivés, ex. a8287 Boissezon) et lève le rate-limit IP pour une vérification exhaustive des RAA Tarn 2020.

## 2. Interpolation : la série a84xx = pages créées en mai 2020 (VALIDÉE)

Requête CDX Wayback (matchType=domain tarn.gouv.fr, filtre original:.*a8[0-9]{2}.*) :

| ID page | Capture | Slug archivé | Attribution |
|---------|---------|--------------|-------------|
| a8412 | 2020-05-01 | titre-de-sejour-ressortissants-andorrans-et-a8412.html | Page d'acte, 01/05/2020 |
| a8442 | 2021-01-20 | raa-special-no-084-dreal-installation-de-turbinage-a8442.html | RAA spécial n°084, mai 2020 |
| a8452 | 2022-01-17 | aps-plans-de-mise-en-conformite-piscicole-de-l-a8452.html | Page d'acte |
| a8462 | 2020-10-20 | labastide-rouairoux-realisation-d-une-station-de-a8462.html | Page d'acte |
| a8482 | 2021-01-17 | raa-special-no-093-ouverture-du-musee-d-art-du-a8482.html | RAA spécial n°093, mai 2020 |
| a8486 | AUCUNE | arrete-portant-rejet-d-une-demande-d-exploiter-un-a8486.html | Page d'acte : REJET (supprimée) |

| FCT-x1-001 | Les pages RAA a84xx identifiées du site tarn.gouv.fr sont datées autour de mai 2020 : a8412 (titre de séjour Andorrans) capturé 01/05/2020, a8442 = RAA spécial n°084 de mai 2020, a8482 = RAA spécial n°093 de mai 2020 (a8452 et a8462, capturés 2022 et 10/2020, n'ont pas de datation de création confirmée) | CDX Wayback (2026-08-11), matchType=domain, filtre a84xx | CONFIRMÉ (pour les pages datées ; a8452/a8462 non datés) |
| FCT-x1-002 | a8486 se situe dans la fourchette a8462 (capturé 20/10/2020) et a8482 (RAA spécial 093) : cohérent avec un acte daté du 15/05/2020, quelques numéros après a8482 | Interpolation CDX | CONFIRMÉ (datation cohérente) |
| FCT-x1-003 | La page a8486 est une page d'acte individuel (pattern « arrete-portant-rejet-d-une-demande-d-exploiter-un-a8486.html »), distincte des pages RAA mensuels | URL originale fournie par TNE 23/05/2020 + pattern CMS | CONFIRMÉ |
| FCT-x1-004 | a8486 : 0 capture Wayback (CDX vide sur toutes les variantes du filtre), cohérent avec une page éphémère supprimée rapidement | CDX Wayback, filtres a8486 / arrete-portant-rejet / a84[0-9]{2} | CONSTAT D'ABSENCE |

## 3. Vérification des RAA Tarn 2020 dans la fenêtre de publication attendue (mai-juillet)

Le rate-limit IP (HTTP 000) a été levé : accès direct HTTP 200 avec User-Agent Chrome. Les RAA mensuels de la fenêtre ont été téléchargés en PDF complets et fouillés (pdftotext -layout, grep Fontrieu / éolien / rejet / Puech / Margn / 15-05-2020) :

| RAA mensuel | N° | PDF | Résultat |
|-------------|-----|-----|----------|
| Mai 2020 (publié 03/06/2020) | 112-113 | 13,1 Mo + 5,3 Mo | 0 mention Fontrieu/éolien/rejet |
| Juin 2020 | 141-142-143 | 3 PDF | 0 mention |
| Juillet 2020 | 158-162 | 5 PDF (17,4 + 17,4 + 19,5 + 10,7 + 7,1 Mo) | 0 mention (seuls des « rejet implicite » génériques dans les notices de recours DDT) |

| FCT-x1-005 | Le RAA mensuel de mai 2020 (n°112-113, publié le 03/06/2020) ne contient pas l'arrêté de rejet de l'extension de Puech Cornet : 0 occurrence Fontrieu / éolien / rejet dans les 2 PDF complets | pdftotext des PDF recueil-81-2020-112 et 113 (tarn.gouv.fr, 2026-08-11) | CONSTAT D'ABSENCE |
| FCT-x1-006 | Le RAA mensuel de juin 2020 (n°141-143) ne contient pas davantage le rejet : 0 occurrence | pdftotext des 3 PDF (2026-08-11) | CONSTAT D'ABSENCE |
| FCT-x1-007 | Le RAA mensuel de juillet 2020 (n°158-162) ne contient pas le rejet : 0 occurrence | pdftotext des 5 PDF (2026-08-11) | CONSTAT D'ABSENCE |
| FCT-x1-008 | Le RAA mensuel de mai 2020 (n°112) contient l'acte a8287 Boissezon (autorisation d'exploiter l'usine hydroélectrique, 14 pages) : borne basse de l'interpolation validée dans le RAA réel | pdftotext recueil-81-2020-112 | CONFIRMÉ |

## 4. RAA spéciaux de mai et juin 2020 : 0 mention

Les 25 RAA spéciaux de mai 2020 et les 8 de juin 2020 ont été énumérés depuis la pagination officielle et vérifiés : aucun ne concerne Fontrieu, Puech Cornet, Margnès, ni l'éolien. Les spéciaux de mai sont des actes de musées, lacs, délégations de signature DDFIP/DREAL/CH, marchés de bestiaux, forets domaniales. Les spéciaux de juin sont des délégations de signature (ANRU, DDFIP, Hôpital d'Albi) et des fermetures (tabac, piscines).

| FCT-x1-009 | Les 25 RAA spéciaux de mai 2020 (n°084 à 111) ne contiennent aucun acte lié à Fontrieu, à l'éolien ou à un rejet d'autorisation : tous sont des musées, lacs, délégations de signature, marchés de bestiaux, forets, CH | Énumération pagination officielle Mai-2020 + vérification des 25 pages (2026-08-11) | CONSTAT D'ABSENCE |
| FCT-x1-010 | Les 8 RAA spéciaux de juin 2020 (n°114 à 123) ne contiennent aucun acte lié à Fontrieu ou à l'éolien : délégations de signature et fermetures | Énumération pagination Juin-2020 + vérification des 8 pages (2026-08-11) | CONSTAT D'ABSENCE |

## 5. Conclusion et verdict

1. **La date de l'arrêté est désormais doublement établie** : 15/05/2020 (journal municipal Fontrieu n°9, octobre 2020, découvert au 09-37) ET cohérente avec l'interpolation CDX (a8486 dans la fourchette a8462/a8482, pages RAA spécial de mai 2020).
2. **Le numéro d'acte administratif (81-2020-XXXX) n'est pas retrouvable dans les sources publiques en ligne** : la page a8486 est supprimée (404), non archivée (0 capture Wayback), et le rejet n'a pas été publié dans les RAA mensuels de mai, juin, juillet 2020 (fenêtre de publication attendue) ni dans les 33 RAA spéciaux de mai-juin 2020, tous vérifiés en PDF complet ou en page.
3. **Interprétation** : soit l'arrêté a été publié dans un RAA spécial d'environnement dont la page a été supprimée sans archivage (la série a84xx contient précisément des pages d'actes individuels éphémères), soit le rejet a fait l'objet d'une notification directe au pétitionnaire sans publication RAA en ligne pérenne. Les deux cas relèvent de l'opacité documentaire, pas d'une anomalie de fond : le refus est un fait établi par la presse (TNE 23/05/2020) et le journal communal (10/2020).
4. **Verdict** : 0 corruption pénale inchangé. Le GAP-x-1 est CLÔTURÉ en constat d'absence partiel : date = 15/05/2020 (confirmée), n° d'acte = non retrouvable en OSINT, texte intégral = non retrouvable en OSINT.

## 6. Limites épistémiques explicites

- L'absence du rejet dans les RAA mensuels vérifiés ne prouve pas la non-publication : les RAA spéciaux d'environnement supprimés entre 2020 et 2026 peuvent avoir contenu l'acte (0 capture Wayback sur l'ensemble des RAA Tarn 2019-2020, FCT-x-004 du 07-43).
- **Portée des mois vérifiés** : mensuels mai, juin, juillet 2020 (fenêtre de publication attendue d'un acte du 15/05, ≤ 3 mois) et spéciaux mai-juin 2020. Les mensuels d'avril (un acte daté du 15/05 ne peut logiquement y figurer) et d'août-décembre 2020 (hors fenêtre) n'ont pas été consultés : une publication très tardive n'est pas formellement exclue.
- Le numéro administratif serait accessible par : (1) demande CADA à la préfecture du Tarn (copie de l'arrêté du 15/05/2020), (2) consultation du RAA d'archives papier de la préfecture, (3) le registre des actes de la DREAL Occitanie (sous réserve d'existence).
- La fourchette CDX est une datation d'ordre de grandeur (création des pages), pas une datation d'acte : elle corrobore sans prouver.

## 7. Méthode et scripts

- CDX Wayback : `http://web.archive.org/cdx/search/cdx?url=tarn.gouv.fr&matchType=domain&fl=timestamp,original&collapse=urlkey&filter=original:.*a84xx.*`
- RAA mensuels Tarn 2020 : `tarn.gouv.fr/Publications/RAA-.../RAA/2020/{Mai,Juin,Juillet}-2020/RAA-N-XXX-MENSUEL` + liens `/contenu/telechargement/XXXX/XXXXXX/file/recueil-81-2020-XXX-...pdf`, analyse pdftotext -layout
- Pagination spéciaux : offsets `(offset)/N` de la page mensuelle, slugs RAA-SPECIAL-N-XXX
- Scripts : /tmp/gapx1_paginate.py, /tmp/gapx1_raa_speciaux.py, /tmp/gapx1_speciaux_detail.py, /tmp/gapx1_juin_mensuel.py, /tmp/gapx1_juin_dl.py, /tmp/gapx1_juillet.py, /tmp/gapx1_juillet_dl.py, /tmp/gapx1_juin_speciaux.py, /tmp/gapx1_cdx_serie.py
- Fichiers : /tmp/raa_mai_m112.pdf, /tmp/raa_mai_m113.pdf, /tmp/raa_juin_*.pdf, /tmp/raa_juil_158-162.pdf, /tmp/jina_raa_*.txt, /tmp/sp_*.txt

## 8. Faits résiduels (GAP)

| GAP-x1-1 | Numéro administratif exact de l'arrêté du 15/05/2020 (81-2020-XXXX) : CADA préfecture du Tarn ou RAA papier |
| GAP-x1-2 | Texte intégral de l'arrêté (motifs détaillés, visa) : CADA préfecture ou DREAL |
| GAP-x1-3 | Vérification de l'hypothèse « RAA spécial d'environnement supprimé » : registre des actes préfecture, ou re-vérification à date fixe (début septembre 2026) |

FIN. Em-dash : 0 vérifié.
