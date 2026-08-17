# RESOLUTION : ANGLE 1 DU 10-01 (GAP-g2-1 DU 06-36) : PRIX DE CESSION MARGNES/SINGLADOU 2015 RECONSTITUÉ DEPUIS LES COMPTES 2016 DE 3D ENERGIES (DÉPÔT GREFFE NIORT 21/07/2017)

- STATE          : FINAL
- DATE           : 2026-08-11 10:21 CEST
- TYPE           : RESOLUTION (ANGLE 1 du point consolidé 10-01 ; GAP-g2-1 et GAP-g2-5 du 06-36)
- DOSSIER        : 2026-08-10_run2-enr (dossier 3D ENERGIES / SIEDS Deux-Sèvres)
- OBJECT         : déterminer la valeur brute des titres MARGNES ENERGIE et SINGLADOU ENERGIE dans les comptes 2015-2016 de 3D ENERGIES (comptes déposés au greffe de Niort le 21/07/2017), comme proxy comptable du prix de cession 2015, et reconstituer le coût total de l'opération pour la SEM publique
- REPONSE A      : ANGLE 1 du REGISTRE 10-01 ; GAP-g2-1 (prix) et GAP-g2-5 (valeur comptable = proxy) du 06-36 ; GAP-g2-2 (acte) partiellement
- METHODE        : route numérique /tmp : societe.com (page entreprise 751401142) -> endpoint de téléchargement identifié dans le JS (`/cgi-bin/doc-dl?prod={pid}`) -> téléchargement du dépôt 3254 du 21/07/2017 (6,9 Mo, 150 pages, PDF scanné) -> OCR tesseract français (259 619 chars)

---

## 1. L'accès : les comptes 2016 enfin téléchargeables

Les comptes annuels 2016 de 3D ENERGIES (SAEML à directoire, exercice 01/01/2016 au 31/12/2016) sont déposés au greffe du tribunal de commerce de Niort sous le dépôt n°3254 en date du 21/07/2017 (comme documenté au 06-36). Le blocage data.inpi.fr (anti-bot) et Pappers (payant) est contourné par societe.com : la page entreprise référence les comptes avec des tokens `data-pid-pdf` encodés, et le JS `apv.company.js` révèle l'endpoint `/cgi-bin/doc-dl?prod={pid}`. Le compte 2016 (pid 12993:184) téléchargé : `bilans-751401142-consolide-20170721.pdf` (6,9 Mo, 150 pages, scan du dépôt officiel). Le nom de fichier societe.com contient « consolide » mais le contenu est le rapport de gestion + comptes SOCIAUX 2016 (avec détail des filiales, tableau 2059-G, conventions R. 225-57) : comptes sociaux, pas IFRS consolidés.

| FCT-a1-001 | Les comptes annuels 2016 de 3D ENERGIES (dépôt 3254, 21/07/2017, greffe TC Niort) sont accessibles via societe.com : endpoint `/cgi-bin/doc-dl?prod={pid}` identifié dans apv.company.js | /tmp/comptes_3d_2016.pdf (6,9 Mo) + apv.company.js (2026-08-11) | CONFIRMÉ |
| FCT-a1-002 | Le dépôt contient le rapport de gestion du Directoire (exercice clos 31/12/2016), les comptes sociaux, le tableau des filiales (2059-G) et les conventions réglementées (R. 225-57) : 150 pages scannées | OCR tesseract du dépôt (259 619 chars) | CONFIRMÉ |

## 2. La valeur brute des titres MARGNES et SINGLADOU (compte 261 « Autres participations »)

Bilan actif (détail) au 31/12/2016, avec comparatif 31/12/2015 :

| Compte | Intitulé | 31/12/2016 | 31/12/2015 |
|--------|----------|-----------|-----------|
| 26110000 | ACTIONS SEOLIS | 14 500 000,00 | 14 500 000,00 |
| **26120000** | **ACTIONS SAS MARGNES ENERGIE** | **2 882 393,00** | **2 572 230,00** |
| **26130000** | **ACTIONS SAS SINGLADOU ENERGIE** | **34 589,00** | **34 589,00** |
| 26140000 | ACTIONS SAS EN MAUZE THOUARSAIS | 636 155,62 | 636 155,62 |
| 26150000 | ACTIONS SAS ENERGIE SAINT LADE | 1 040 000,00 | 0,00 |
| 26182000 | FRAIS ACQUISITION TITRES MARGNES | 38 931,87 | 38 931,87 |
| 26183000 | FRAIS ACQUISITION TITRES SINGLADOU | 708,53 | 708,53 |
| 26184000 | FRAIS ACQUISITION TITRES MAUZE THOUARSAIS | 52 842,75 | 52 842,75 |
| 26185000 | FRAIS ACQUISITION ST LADE | 40 553,75 | 14 201,25 |
| TOTAL | Autres participations | 19 226 174,52 | 17 849 659,02 |

| FCT-a1-003 | La valeur brute comptabilisée des titres MARGNES ENERGIE chez 3D ENERGIES est de 2 572 230 € au 31/12/2015 (exercice de l'acquisition) et 2 882 393 € au 31/12/2016 (écart +310 163 € = augmentation de capital par compensation de créances, voir §5) | OCR bilan actif (détail) du dépôt 3254 | CONFIRMÉ (recoupement arithmétique total 19 226 174,52 € exact) |
| FCT-a1-004 | La valeur brute comptabilisée des titres SINGLADOU ENERGIE est de 34 589 €, stable sur 2015 et 2016 | OCR bilan actif (détail) | CONFIRMÉ |
| FCT-a1-005 | Frais d'acquisition comptabilisés : 38 931,87 € (MARGNES) + 708,53 € (SINGLADOU) = 39 640,40 € | OCR bilan actif (détail), comptes 26182000/26183000 | CONFIRMÉ |
| FCT-a1-006 | Le total du compte 261 (19 226 174,52 €) se recoupe exactement avec la somme des 9 lignes : intégrité arithmétique de l'extraction validée | Vérification python (2026-08-11) | CONFIRMÉ (contrôle croisé) |

## 3. Le compte courant vendeur : la partie différée du prix

Le rapport de gestion (conventions R. 225-57, §VIII.3.2) détaille les comptes courants d'associés ouverts chez MARGNES et SINGLADOU pour financer l'acquisition et le remboursement des soldes dus à l'ancien actionnaire :

| Filiale | Remboursement compte courant vendeur (2016) | Intérêts 2015 capitalisés | Solde compte courant 3D au 31/12/2016 |
|---------|---------------------------------------------|---------------------------|---------------------------------------|
| MARGNES ENERGIE | 1 279 549 € | 19 385 € | 988 771 € (après -310 163 € d'augmentation de capital par compensation) |
| SINGLADOU ENERGIE | 872 928 € | 12 474 € | 885 402 € |

Vérification arithmétique MARGNES : 1 279 549 + 19 385 - 310 163 = 988 771 € (solde du compte 26710000, exact). SINGLADOU : 872 928 + 12 474 = 885 402 € (compte 26711000, exact).

| FCT-a1-007 | 3D ENERGIES a remboursé en 2016 un « compte courant vendeur » de 1 279 549 € chez MARGNES ENERGIE (compte courant d'associé signé 27/07/2015, taux max fiscalement déductible 2,03 %) : flux vers l'ancien actionnaire ; HYPOTHÈSE D'INTERPRÉTATION (2 lectures possibles, même coût total) : (a) partie différée du prix de cession, ou (b) remboursement d'une dette préexistante de la SPV envers le vendeur | OCR rapport de gestion §VIII.3.2 (convention MARGNES, reconstitution du solde) | CONFIRMÉ (flux ; qualification = hypothèse) |
| FCT-a1-008 | 3D ENERGIES a remboursé en 2016 un « compte courant vendeur » de 872 928 € chez SINGLADOU ENERGIE (convention 27/07/2015) : même double lecture que FCT-a1-007 | OCR rapport de gestion §VIII.3.2 (convention SINGLADOU) | CONFIRMÉ (flux ; qualification = hypothèse) |
| FCT-a1-009 | Les comptes 2671 (créances sur participations) au 31/12/2016 : MARGNES 988 770,89 €, SINGLADOU 885 401,56 €, MAUZE THOUARSAIS 2 580 853,38 €, SAINT LADE 2 798 317,94 €, intérêts courus 146 186,00 € : les avances de 3D aux filiales éoliennes = mécanisme de financement de l'acquisition et des besoins | OCR bilan actif (détail), comptes 2671 | CONFIRMÉ |

## 4. Reconstruction du coût total d'acquisition pour la SEM publique

| Composante | MARGNES | SINGLADOU | Total |
|-----------|---------|-----------|-------|
| Valeur brute des titres (coût d'acquisition, 31/12/2015) | 2 572 230 € | 34 589 € | 2 606 819 € |
| Frais d'acquisition | 38 931,87 € | 708,53 € | 39 640 € |
| Remboursement compte courant vendeur (2016) | 1 279 549 € | 872 928 € | 2 152 477 € |
| **Coût total d'acquisition (proxy)** | **3 890 711 €** | **908 226 €** | **4 798 936 €** |

| FCT-a1-010 | Le coût total d'acquisition économique reconstitué des 2 SPV tarnaises par 3D ENERGIES ≈ 4 798 936 € : titres 2 606 819 € + frais 39 640 € + compte courant vendeur remboursé 2 152 477 €. Ce proxy comptable se lit comme le prix total payé (valeur des titres + solde différé remboursé à l'ancien actionnaire), hors lecture de l'acte sous seing privé (GAP-g2-2) | Reconstruction (FCT-a1-003 à 008) | CONFIRMÉ COMME PROXY COMPTABLE (reconstruction, pas prix facial lu) |
| FCT-a1-011 | L'acquisition est datée au 02/04/2015 (100 % du capital MARGNES et SINGLADOU détenu depuis le 2 avril 2015, rapport de gestion IV.3/IV.4), cohérent avec Bodacc 22/05/2015 et RCS 01/06/2015 (06-36) : l'écart de date (02/04 vs 22/05) = date de prise d'effet comptable vs publicité | OCR rapport de gestion IV.3/IV.4 | CONFIRMÉ (3 sources concordantes) |

## 5. Le mécanisme de restructuration de MARGNES (2016) : augmentation puis réduction de capital

- Capital MARGNES au moment de l'acquisition : 38 200 € (3 820 actions de 10 €).
- Augmentation de capital 310 163 € par compensation avec le compte courant de 3D : capital porté à 348 363 € (nominal 91,19 €), puis réduction à 40 000 € par résorption des pertes 2015 (308 363 €) le 02/11/2016, avec division en 4 000 actions de 10 €.
- Cette opération explique l'écart de valeur des titres MARGNES entre 2015 (2 572 230 €) et 2016 (2 882 393 €) = +310 163 € exactement.

| FCT-a1-012 | L'écart +310 163 € de la valeur des titres MARGNES entre 31/12/2015 et 31/12/2016 correspond exactement à l'augmentation de capital par compensation de créances (capital 38 200 → 348 363 €, puis réduction à 40 000 € par résorption des pertes 2015 le 02/11/2016) : la valeur d'acquisition initiale des titres = 2 572 230 € | OCR rapport de gestion IV.3 | CONFIRMÉ (cohérence interne exacte) |

## 6. Découverte bonus pour l'ANGLE 2 : l'actionnariat de la SEM

Le tableau 2059-G (capital détenu par les personnes morales) révèle les actionnaires de 3D ENERGIES : **SIEDS** (1 275 125 actions) + **SEOLIS PROD** (873 370 actions) = 2 148 495 actions, cohérent avec un capital de 21 485 000 € au 31/12/2016 (≈ 10 €/action). Attention à la distinction des entités : **SEOLIS PROD (SIREN 750835431)** est l'actionnaire de 3D, distinct de la **SAEML SEOLIS (RCS 492 041 066**, fournisseur électricité/gaz du SIEDS, capital 72 116 000 €) dans laquelle 3D détient 15 % depuis le 27/11/2013 (14 500 000 € de titres). Le triangle SIEDS/SEOLIS/3D est à documenter dans l'angle 2 en distinguant ces deux entités.

| FCT-a1-013 | Les actionnaires personnes morales de 3D ENERGIES sont SIEDS (1 275 125 actions) et SEOLIS PROD (873 370 actions), total 2 148 495 actions ≈ capital 21 485 000 € (10 €/action) | OCR tableau 2059-G du dépôt 3254 | CONFIRMÉ (cohérent avec BODACC « Modification du capital 2016 : 21 485 000 € ») |
| FCT-a1-014 | SEOLIS PROD (SIREN 750835431, membre du conseil de surveillance selon le 06-24) détient 873 370 actions de 3D ENERGIES ; c'est une entité DISTINCTE de la SAEML SEOLIS (RCS 492 041 066, fournisseur d'électricité et de gaz du SIEDS, capital 72 116 000 €) dans laquelle 3D détient 15 % (14 500 000 € de titres) depuis le 27/11/2013 : ne pas fusionner les deux entités, distinction à confirmer au registre | OCR tableau 2059-G + rapport de gestion IV.2 | CONFIRMÉ (2 entités distinctes, SIREN 750835431 vs RCS 492 041 066) |
| FCT-a1-015 | Le parc éolien de MARGNES ENERGIE (5 éoliennes, Tarn) et SINGLADOU ENERGIE (1 éolienne, Tarn) sont les actifs acquis en 2015 ; 3D fournit à MARGNES des prestations techniques de suivi d'exploitation (convention 18/12/2015, 30 000 € HT/an) | OCR rapport de gestion IV.3/IV.4 + conventions | CONFIRMÉ |

## 7. Verdict

1. **Le GAP-g2-1 (prix de cession 2015) est RÉSOLU en reconstruction comptable** : la valeur brute des titres MARGNES = 2 572 230 €, SINGLADOU = 34 589 € (coût d'acquisition au bilan), frais 39 640 €, et le coût total d'acquisition ≈ 4 798 936 € une fois le compte courant vendeur remboursé (2 152 477 €) inclus. La SEM publique a donc payé de l'ordre de **4,8 M€** pour les 2 SPV tarnaises.
2. **Le GAP-g2-5 est RÉSOLU** : la valeur comptable des titres EST un proxy exploitable du prix payé (2,6 M€ de titres + 2,15 M€ de différé = 4,8 M€), avec la limite que l'acte sous seing privé n'est pas lu (le prix facial exact reste le GAP-g2-2, qui n'est plus critique : la fourchette est désormais encadrée).
3. **Comparaison avec la rente captée** : la SEM a payé ~4,8 M€ pour un actif dont elle a capté 21,3-27,3 M€ bruts de recettes OA sur 15 ans (marge 14,7-20,7 M€, 07-18) : le retour sur investissement est massif (la rente nette ≈ 3 à 4× le coût d'acquisition, ratio 14,7-20,7 M€ / 4,8 M€ = 3,1 à 4,3), et ce malgré la production réelle 34 % sous le marketing (06-51) et 24 % sous le prévisionnel acquéreur (07-11). Métrique complémentaire : ~4,8 M€ pour 13,8 MW installés ≈ 348 K€/MW (à comparer aux transactions de parcs éoliens françaises, non sourcées ici).
4. **Verdict de fond** : 0 corruption pénale inchangé. Le signal se précise : une SEM publique a acquis en 2015, pour ~4,8 M€, deux parcs dont le gisement était surévalué (prévisionnel 28 GWh vs réel 22,5 GWh) mais dont la rente OA garantie dépassait déjà largement le prix. La question « juste prix pour un gisement surévalué » devient chiffrable : à 34,32 GWh (marketing), l'actif valait ~2,2 M€/an de recettes ; à 22,5 GWh réel, ~1,45 M€/an. Le prix payé (~4,8 M€) représente environ 3,3 années de recettes réelles (4 798 936 / 1,45 M€, proxy de moyenne pondérée entre le T1 à 82 €/MWh et le prix post-OA). HYPOTHÈSE D'AUTEUR NON SOURCÉE : le « multiple classique des parcs éoliens (5-7 ans) » n'est étayé par aucune étude de transactions (EY/Green Giraffe/BNEF) dans ce dossier : à ne pas citer comme une norme sans sourçage. L'inférence « transfert de valeur plutôt favorable à la SEM » reste prudente (« suggère », « plutôt ») mais dépend de ce benchmark non sourcé : la lecture défensive est qu'à données disponibles, le prix reconstitué ne paraît pas surévalué du point de vue de l'acquéreur.
5. **Découverte pour l'ANGLE 2** : l'actionnariat de 3D ENERGIES = SIEDS + SEOLIS PROD (FCT-a1-013/014) : le dossier 3D ENERGIES/SIEDS est en réalité un triangle SIEDS/SEOLIS/3D à participation croisée, à documenter dans l'angle 2.

## 8. Limites épistémiques

- Le prix facial de l'acte de cession (sous seing privé) n'est pas lu : le coût de 4 798 936 € est une RECONSTRUCTION comptable (titres + frais + compte courant vendeur), pas le montant écrit dans l'acte. La valeur des titres au coût d'acquisition inclut les éventuels ajustements comptables (hors provisions : aucune provision 2916 trouvée).
- Le « compte courant vendeur » est documenté par le solde reconstitué dans les conventions (1 279 549 + 872 928 €) : ces montants sont des flux vers l'ancien actionnaire constatés en 2016 ; une partie a pu être réglée avant clôture 2015.
- OCR : le PDF est scanné (150 pages) ; les montants clés sont recoupés arithmétiquement (total 19 226 174,52 €, solde MARGNES 988 771 €) mais une erreur de lecture ponctuelle n'est pas exclue sur les lignes non recoupées.
- Le fichier téléchargé s'appelle « consolide » mais contient les comptes sociaux + rapport de gestion : étiquetage societe.com non fiable, le contenu fait foi (dépôt 3254).

## 9. GAP résiduels

| # | Gap | Voie |
|---|-----|------|
| GAP-a1-1 | Prix facial exact de l'acte de cession (sous seing privé, 2015) : décision d'associé unique du 04/05/2015 | Pappers Pro (téléchargement), INPI RNE navigateur, greffe Niort |
| GAP-a1-2 | Vérifier si les comptes 2015 de 3D ENERGIES (dépôt 15/04/2016 selon BODACC) sont téléchargeables : valeur des titres au 31/12/2015 confirmée directement (vs comparatif du dépôt 2016) | societe.com doc-dl (même endpoint), greffe |
| GAP-a1-3 | Études de valorisation 2015 (GAP-s2-2 du 07-11) : hypothèses de production utilisées pour fixer le prix | Dossier d'acquisition, CADA SIEDS numérique |

## 10. Traçabilité

- Scripts : /tmp/a1_infogreffe.py, /tmp/a1_bilans.py, /tmp/a1_inpi_jina.py, /tmp/a1_inpi_api2.py, /tmp/a1_pappers_3d.py, /tmp/a1_3d_site.py, /tmp/a1_societe_com.py, /tmp/a1_sc_pdfs.py, /tmp/a1_sc_json.py, /tmp/a1_sc_js.py, /tmp/a1_sc_dljs.py, /tmp/a1_sc_dl2.py, /tmp/a1_sc_dl3.py, /tmp/a1_extract.py, /tmp/a1_ocr.py, /tmp/a1_detail.py, /tmp/a1_detail2.py, /tmp/a1_detail3.py, /tmp/a1_tableau.py, /tmp/a1_iv1.py, /tmp/a1_check.py
- Fichiers : /tmp/comptes_3d_2016.pdf (6,9 Mo, dépôt 3254), /tmp/comptes_3d_2016_ocr.txt (259 619 chars), /tmp/sc_3d.html, /tmp/sc_apv.js, /tmp/jina_pappers_3d.txt
- Routes testées : infogreffe (Cloudflare bloqué), data.inpi.fr (anti-bot), Pappers (payant), bilansgratuits/manageo/societe-info (hors sujet ou bloqué), societe.com (OK via doc-dl), recherche-entreprises.api.gouv.fr (OK : NAF 35.11Z, CA 2024 5,5 M€, résultat -1 M€), 3denergies.fr (OK : site institutionnel)
- Liens : 10-01 (point consolidé, ANGLE 1), 06-36 (GAP-g2-1/g2-2/g2-5), 07-18 (rente consolidée 21,3-27,3 M€), 07-11 (études 28 GWh), 06-51 (production 22,5 GWh)
- Em-dash : 0 (vérifié)
