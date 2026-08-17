# Quintessence : VP-P1, test du pattern « élu propriétaire foncier votant des parcs » dans le Tarn

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-11_12-48_vp1-elus-proprietaires-fonciers-tarn_INVESTIGATION.md` (140 lignes, 18 FCT-vp1)
Date extraction : 2026-08-13 03:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé axe piste, piste VP-P1 de la veille 11-42
- **Date source** : 2026-08-11 12:48 CEST, STATE FINAL
- **Identifiants source** : 18 FCT-vp1-001 à 018
- **Object** : tester le pattern alerté par le SCPC (2014) et documenté par Reporterre (élus propriétaires fonciers votant des parcs éoliens installés sur leurs terrains, baux 1-10 K€/an/éolienne) sur les 3 communes du Tarn à parcs Valeco/3D ENERGIES : Fontrieu (Puech Cornet), Barre (Combaynart/Couffrau), Lacaune (Puech del Vert)
- **Verdict source** : pattern CONFIRMÉ une fois (cas Cabrol/Lacaune, condamné 17/10/2023, 432-12) ; Fontrieu = variante structurellement différente (terrains communaux) ; Barre = GAP (matrice nominative inaccessible en OSINT)

## 2. Faits atomiques préservés

- FCT-vp1-001 : la route cadastre OSINT sans clé fonctionnelle est Apicarto IGN `/api/cadastre/parcelle?geom=<Point GeoJSON>` : renvoie code INSEE, commune, section, numéro et contenance (22 requêtes réussies sur 23) [L37 (mesuré)]
- FCT-vp1-002 : routes alternatives non exploitables en automatisation : data.cadastre.gouv.fr (réponse vide), cadastre.data.gouv.fr/wfs (404), WMS SCPC (HTML sans couches) [L38 (mesuré)]
- FCT-vp1-003 : le SCPC expose les formulaires de recherche mais le flux automatisé vers la matrice échoue (erreur Struts) ; l'accès à la matrice nominative pour communes < 2 000 habitants réputé nécessiter une déclaration d'identité interactive [L39 (mesuré)]
- FCT-vp1-004 : les coordonnées GPS de la fiche Valeco 2014 pour « Puech Cornet » (43.73520, 2.84794) tombent sur la commune de BARRE (81023), section AO : parcelles 0030 (9 460 m²), 0036 (21 025 m²), 0039 (14 280 m²), 0054 (11 741 m²) ; voisinage Murat-sur-Vèbre (81192) section 0D [L40 (mesuré)]
- FCT-vp1-005 : le pôle « Monts de Lacaune » de The Wind Power (ID 10375) : centre 43.73914, 2.84794, 15 Enercon E70/2300 : la requête cadastre tombe sur Barre (81023) AO 0030 [L41 (mesuré)]
- FCT-vp1-006 : le site réel du Puech Cornet (Le Margnès, Fontrieu 81062) est dans la zone ~43.655, 2.555 : sections 0F, 0I, 0P, ZD (balayage 7 points) [L42 (mesuré)]
- FCT-vp1-007 : CAVEAT LOCALISATION : les coordonnées de la fiche Valeco pointent vers la zone Couffrau de Barre, PAS vers le site documenté par les APC (Fontrieu) : écart à signaler, recouper sur les arrêtés préfectoraux (INFÉRENCE étayée) [L43 (mesuré)]
- FCT-vp1-008 : CAS CABROL (Lacaune) : André Cabrol, maire à l'époque du permis (2011), propriétaire du terrain d'implantation ; condamné 17/10/2023 par le TC de Castres pour prise illégale d'intérêts (432-12 CP) : 2 500 € amende + 800 € dommages ; promoteur/SARL relaxés du chef de recel [L44 (mesuré)]
- FCT-vp1-009 : GAP-1c RÉSOLU : Philippe Folliot, ancien député puis sénateur (intermédiaire en 2010 auprès du ministère de la Défense avec Cabrol), auditionné comme témoin, a indiqué avoir cru que le terrain appartenait à la commune, JAMAIS poursuivi (ni PNF, ni procureur, ni HATVP) [L45 (mesuré)]
- FCT-vp1-010 : aucun appel de Cabrol documenté : la condamnation du 17/10/2023 est présumée définitive [L46 (mesuré)]
- FCT-vp1-011 : CAS FONTRIEU : journal municipal de janvier 2026 : le parc de Puech Cornet contribue au budget communal par la location des TERRAINS COMMUNAUX + 50 % de l'IFER + participation annuelle 10 000 € : le propriétaire foncier est la COMMUNE, pas un élu individuel [L47 (mesuré)]
- FCT-vp1-012 : aucun bail individuel sur terrain privé d'un élu de Fontrieu documenté dans les 7 journaux municipaux (2018-2026) ni le site communal ; bail initial 2004-2005 non publié (GAP-fo-3) [L48 (mesuré)]
- FCT-vp1-013 : le maire de Fontrieu Didier Gavalda (élu 03/2020, réélu 03/2026) est délégué au SDET et aux Communes Forestières ; la commune a délibéré le 12/10/2018 pour entrer au capital du projet d'extension « Fontrieu Energie » (avec le SDET) : pattern « commune associée à la gouvernance de l'exploitant », sans signal pénal [L49 (mesuré)]
- FCT-vp1-014 : CAS BARRE : la presse documente des « terres de particuliers louées par Valeco » (repowering 2024-2026) : propriétaires privés non nommés publiquement [L50 (mesuré)]
- FCT-vp1-015 : le maire de Barre Vincent Vidal affiche sa satisfaction (« 30 ans qu'on n'avait pas eu la visite d'un préfet », 12/07/2023) ; aucun conflit d'intérêts documenté le concernant [L51 (mesuré)]
- FCT-vp1-016 : parcelles d'emprise possible de Barre/Combaynart : section AO (0030, 0036, 0039, 0054) côté Barre et section 0D (1824, 0249, 0296) côté Murat : identité des propriétaires exige la matrice nominative (non accessible en OSINT) [L52 (mesuré)]
- FCT-vp1-017 : le pattern national est une alerte institutionnelle : SCPC (rapport 2014) sur la multiplication des prises illégales d'intérêts d'élus dans l'éolien terrestre (baux sur terrains propres, 1 000 à plus de 10 000 €/an/éolienne ; ex. 54 000 €/an pour 5 éoliennes, 108 000 €/an pour 10, chiffres rapportés par Reporterre) [L53 (mesuré)]
- FCT-vp1-018 : verdict consolidé : sur 3 communes testées, 1 pattern CONFIRMÉ et pénalisé (Cabrol/Lacaune), 1 variante différente (Fontrieu), 1 GAP (Barre) ; aucun autre cas de prise illégale d'intérêts éolienne documenté dans le Tarn [L54 (mesuré)]

## 3. Acteurs nominaux

**Élus** : André Cabrol (maire de Lacaune, condamné 432-12), Didier Gavalda (maire de Fontrieu, délégué SDET), Vincent Vidal (maire de Barre), Philippe Folliot (ancien député puis sénateur, témoin jamais poursuivi).
**Associations** : ARVIEE, CALELH, Reporterre, Nostra Montanha.
**Institutions** : SCPC (rapport 2014), TC Castres, ministère de la Défense, PNF.

## 4. Sources externes citées

Apicarto IGN (API, 22 requêtes), data.cadastre.gouv.fr, cadastre.data.gouv.fr, SCPC (session 6 scripts), The Wind Power (ID 10375), La Dépêche 11/12/2015, 29/08/2023, 05/09/2023, 17/10/2023, 19/07/2023, 01/02/2025, 11/03/2020, journal municipal Fontrieu n°15 (janvier 2026), rapport SCPC 2014.

## 5. Chronologie datée

2014 : rapport SCPC (alerte pattern) ; 2008-2023 : procédure Cabrol (mise en examen 11/12/2015, audiences 08-09/2023, condamnation 17/10/2023) ; 12/10/2018 : délibération Fontrieu entrée au capital Fontrieu Energie ; 03/2020 : élection Gavalda ; 12/07/2023 : déclaration Vidal ; 11/08/2026 : tests cadastre OSINT.

## 6. Mécanismes / chaînes causales

**M1 — Le conflit d'intérêts élu-propriétaire, confirmé et pénalisé une fois** : Cabrol (maire propriétaire du terrain, permis 2011, intervention Folliot/Armée) condamné 432-12 ; le promoteur relaxé du recel. Niveau : L2. [L44-L46 (mesuré)]
**M2 — La variante « commune propriétaire » (Fontrieu)** : terrains communaux, la commune elle-même est propriétaire et bénéficiaire (loyers + IFER + 10 000 €/an) : le pattern SCPC « élu propriétaire privé » ne s'applique pas ; c'est un signal de gouvernance (commune au capital de l'exploitant), pas pénal. Niveau : L2. [L47-L49 (mesuré)]
**M3 — La limite de l'OSINT (Barre)** : les parcelles d'emprise sont identifiées (géométrie Apicarto) mais l'identité des propriétaires exige la matrice cadastrale nominative, inaccessible en automatisation (SCPC : déclaration d'identité). Niveau : L1 (GAP). [L52, L39 (mesuré)]

## 7. Verbatim et citations

- « 30 ans qu'on n'avait pas eu la visite d'un préfet » (Vincent Vidal, 12/07/2023) [L51 (mesuré)]
- Rapport SCPC 2014 : baux sur terrains propres « 1 000 à plus de 10 000 €/an/éolienne » (relayé par Reporterre) [L53 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : route cadastre OSINT validée (Apicarto IGN) ; presse locale recoupée ; FCT-vp1-010 en constat d'absence ; confiance du verdict sur les autres cas ramenée à MOYENNE.
- **F-##** : 18/18 identifiants FCT-vp1-001 à 018 préservés verbatim.
- **Méthode** : géométrie cadastrale OSINT (identification des parcelles d'emprise) puis identité des propriétaires par baux publics, délibérations, presse, matrice/CADA (en dernier recours).

## 9. Limites connues (case-limites)

- GAP-vp1-1 : identité des propriétaires des parcelles de Barre/Combaynart (matrice SCPC manuelle ou CADA DGFiP) ; GAP-vp1-2 : références cadastrales exactes des éoliennes de Puech Cornet et Puech del Vert (arrêtés) ; GAP-vp1-3 : bail initial 2004-2005 de Fontrieu ; GAP-vp1-4 : délibérations de Barre et Murat-sur-Vèbre ; GAP-vp1-5 : équivalents du pattern Cabrol dans les autres parcs EnBW/Valeco (Aveyron).
- Le test ne produit aucun nouveau signal pénal, mais une leçon de méthode (route cadastre validée, limite de la matrice) et une correction de localisation.
