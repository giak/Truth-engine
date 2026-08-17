# INVESTIGATION VP-P1 : TEST DU PATTERN « ELU PROPRIETAIRE FONCIER VOTANT DES PARCS » DANS LE TARN (FONTRIEU, BARRE, LACAUNE)

- STATE          : FINAL
- DATE           : 2026-08-11 12:48 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format allégé axe piste, piste VP-P1 de la veille 11-42)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, veille presse du 11-42)
- OBJECT         : tester le pattern alerté par le SCPC (2014) et documenté par Reporterre : des élus propriétaires fonciers (ou leurs proches) votant des parcs éoliens installés sur leurs terrains (baux 1-10 K€/an/éolienne), sur les 3 communes du Tarn à parcs Valeco/3D ENERGIES : Fontrieu (Puech Cornet), Barre (Combaynart/Couffrau), Lacaune (Puech del Vert)
- METHODE        : route cadastre OSINT validée (Apicarto IGN, geom GeoJSON), tests des routes alternatives (data.cadastre.gouv.fr, WFS, SCPC), croisement avec les baux, délibérations et élus déjà documentés (06-24, 06-44, 18-30, 18-51, 05-40, 05-54), vérification GAP-1c (Folliot) via presse
- VERDICT        : le pattern est CONFIRMÉ une fois dans le Tarn (cas Cabrol/Lacaune : maire propriétaire du terrain d'implantation, condamné 17/10/2023, prise illégale d'intérêts art. 432-12 ; le député-sénateur Folliot, intermédiaire auprès du ministère des Armées, a été auditionné comme témoin et JAMAIS poursuivi) ; le cas de Fontrieu est une variante STRUCTURELLEMENT DIFFÉRENTE (terrains COMMUNAUX, la commune elle-même est propriétaire et bénéficiaire, pas un élu individuel) ; le cas de Barre reste un GAP (propriétaires privés non identifiés, matrice cadastrale nominative inaccessible en OSINT sans déclaration d'identité SCPC)
- NOMENCLATURE   : FCT-vp1-001 à 018
- HASH           : voir tableau §8

---

## 1. Résumé exécutif

La piste VP-P1 de la veille presse (11-42) demandait de tester le pattern « élu propriétaire foncier votant des parcs » (SCPC 2014, Reporterre : baux emphytéotiques 20-30 ans, ~1 000 à plus de 10 000 €/an/éolienne) sur les 3 communes tarnaises à parcs du corpus : Fontrieu (Puech Cornet), Barre (Combaynart/Couffrau), Lacaune (Puech del Vert).

**Résultat du test, parc par parc :**

1. **Lacaune / Puech del Vert : pattern CONFIRMÉ et PÉNALISÉ.** André Cabrol, maire de Lacaune à l'époque du permis (2011), était **propriétaire du terrain d'implantation** des éoliennes. Il a été condamné le **17/10/2023** par le tribunal correctionnel de Castres pour **prise illégale d'intérêts** (art. 432-12 CP) : 2 500 € d'amende + 800 € de dommages-intérêts aux associations ARVIEE et CALELH. Le promoteur (SARL) a été relaxé du chef de recel. C'est le **seul cas pénalisé** du corpus Tarn et l'exacte configuration décrite par le SCPC. Le **GAP-1c est résolu** : Philippe Folliot, ancien député puis sénateur, qui a accompagné Cabrol auprès du ministère des Armées en 2010 pour obtenir un avis favorable malgré le réseau de vol militaire à très basse altitude, a été **auditionné comme témoin**, a affirmé avoir cru que le terrain appartenait à la commune, et **n'a jamais été poursuivi** (aucune source d'enquête, mise en examen ou signalement). Aucun appel de Cabrol n'est documenté : la condamnation est présumée définitive.

2. **Fontrieu / Puech Cornet : variante STRUCTURELLEMENT DIFFÉRENTE.** Le journal municipal de janvier 2026 documente que le parc « contribue au budget communal » via la **location des TERRAINS COMMUNAUX** sur lesquels sont installées les éoliennes (+ 50 % IFER + 10 000 €/an de participation). Ici, c'est la **commune elle-même qui est propriétaire foncier et bénéficiaire**, pas un élu individuel : le pattern SCPC « élu propriétaire privé » ne s'applique pas. Le maire Didier Gavalda (élu 03/2020, réélu 03/2026) est **délégué au SDET** (syndicat départemental d'énergie du Tarn, homologue tarnais du SIEDS qui contrôle 3D ENERGIES) et la commune a délibéré le 12/10/2018 pour **entrer au capital** du projet d'extension « Fontrieu Energie » (avec le SDET) : c'est un autre pattern, documenté (commune associée à la gouvernance de l'exploitant), pas la prise illégale d'intérêts classique. Aucun bail sur terrain privé d'un élu de Fontrieu n'est documenté.

3. **Barre / Combaynart-Couffrau : GAP non résolu.** La Dépêche (01/02/2025) documente des « **terres de particuliers louées par Valeco** » : les propriétaires sont des personnes privées non nommées dans la presse. Le maire Vincent Vidal affiche sa satisfaction (« 30 ans qu'on n'avait pas eu la visite d'un préfet », 12/07/2023) et aucun conflit d'intérêts n'est documenté. La matrice cadastrale nominative (qui seule permettrait de vérifier si un élu de Barre ou Murat-sur-Vèbre figure parmi les propriétaires) n'est **pas accessible en OSINT** : la consultation libre SCPC pour communes < 2 000 habitants exige une déclaration d'identité interactive (flux Struts, bloqué en automatisation : erreur de redirection documentée).

**Découverte de méthode (à conserver dans le protocole)** : la route cadastre OSINT sans clé fonctionnelle est **Apicarto IGN** (`https://apicarto.ign.fr/api/cadastre/parcelle?geom={Point GeoJSON}`), qui renvoie commune, section, numéro et contenance des parcelles à une coordonnée donnée. Les routes `data.cadastre.gouv.fr` (API ODS vide), `cadastre.data.gouv.fr/wfs` (404) et le SCPC automatisé (déclaration d'identité) ne sont pas exploitables en automatisation.

**Correction de localisation à signaler** : les coordonnées GPS de la fiche Valeco 2014 pour « Puech Cornet » (43.73520, 2.84794, reprises en FCT-pc-001) tombent sur la commune de **Barre (81023)** section AO, pas sur Le Margnès/Fontrieu (81062). Le pôle « Monts de Lacaune » de The Wind Power (43°44'20.9"N, 2°50'52.6"E = 43.73914, 2.84794) tombe aussi à Barre (AO 0030). Les coordonnées de la fiche Valeco semblent donc pointer vers la zone du complexe de Couffrau (Barre/Murat-sur-Vèbre) plutôt que le site réel du Puech Cornet (Fontrieu, sections 0F/0I). Caveat : les coordonnées cadastrales exactes des éoliennes individuelles devraient être recoupées sur les arrêtés préfectoraux (références cadastrales) avant toute conclusion de localisation.

---

## 2. Table de faits (FCT-vp1)

| # | Fait | Source | Statut |
|---|------|--------|--------|
| FCT-vp1-001 | La route cadastre OSINT sans clé fonctionnelle est Apicarto IGN `/api/cadastre/parcelle?geom=<Point GeoJSON>` : renvoie code INSEE, commune, section, numéro et contenance de la parcelle à une coordonnée (format WGS84, lon/lat) | Tests 11/08/2026 : 22 requêtes réussies (Barre, Fontrieu, Murat-sur-Vèbre, Lacaune, voisinages ; 1 point vide sur 23) | CONFIRMÉ (route validée) |
| FCT-vp1-002 | Les routes alternatives ne sont pas exploitables en automatisation : `data.cadastre.gouv.fr/api/explore` (réponse vide), `cadastre.data.gouv.fr/wfs` (404 Next.js), `cadastre.data.gouv.fr/api/parcelles/*` (404), WMS SCPC `afficherServiceWMS.do` (GetCapabilities = page HTML sans couches) | Tests 11/08/2026 (HTTP 404 / réponse vide / HTML non WMS) | CONSTAT D'ABSENCE (routes inopérantes) |
| FCT-vp1-003 | Le SCPC (cadastre.gouv.fr) expose les formulaires de recherche par commune et par référence cadastrale (champs `prefixeParcelle`, `sectionLibelle`, `numeroParcelle`, CSRF) ; le flux automatisé vers la matrice échoue (« impossible de rediriger la requete », erreur Struts sur `listerFeuillesParcommune.do`). L'accès à la matrice nominative pour communes < 2 000 habitants est réputé nécessiter une déclaration d'identité interactive (comportement documenté du SCPC, non vérifié en session) | Tests 11/08/2026 (session SCPC complète, 6 scripts) | CONSTAT D'ACCÈS PARTIEL (humain requis) |
| FCT-vp1-004 | Les coordonnées GPS de la fiche Valeco 2014 pour « Puech Cornet » (43.73520, 2.84794, reprises FCT-pc-001) tombent sur la commune de BARRE (81023), section AO : parcelles 0030 (9 460 m²), 0036 (21 025 m²), 0039 (14 280 m²), 0054 (11 741 m²) ; le voisinage couvre aussi Murat-sur-Vèbre (81192) section 0D (parcelles 1824 = 33 577 m², 0249 = 40 671 m², 0296 = 22 129 m²) | Apicarto IGN, requêtes 11/08/2026 (6 points autour de 43.7352, 2.84794) | CONFIRMÉ (coordonnées → Barre/Murat) |
| FCT-vp1-005 | Le pôle « Monts de Lacaune » de The Wind Power (ID 10375) : centre à 43°44'20.9"N / 2°50'52.6"E (= 43.73914, 2.84794), 15 Enercon E70/2300, villes « La Bessière - Monts de Lacaune - Plo de la Rouquette - Puech de l'Homme » : la requête cadastre à ce point tombe sur Barre (81023) AO 0030 | thewindpower.net/windfarm_en_10375 + Apicarto 11/08/2026 | CONFIRMÉ |
| FCT-vp1-006 | Le site réel du Puech Cornet (Le Margnès, Fontrieu 81062) est dans la zone ~43.655, 2.555 : sections cadastrales 0F (parcelles 0080 = 23 173 m², 0103, 0115 = 219 000 m², 0048, 0276 = 998 190 m², 0026 = 172 180 m²), 0I (0058 = 78 900 m²), 0P (0919), ZD (0027) | Apicarto IGN, balayage 7 points 11/08/2026 | CONFIRMÉ (localisation Fontrieu) |
| FCT-vp1-007 | CAVEAT LOCALISATION : les coordonnées de la fiche Valeco pour « Puech Cornet » (FCT-pc-001) pointent vers la zone Couffrau de Barre, PAS vers le site documenté par les APC (lieu-dit Puech Cornet, commune Fontrieu/Le Margnès) : écart de localisation à signaler, les références cadastrales exactes des éoliennes doivent être recoupées sur les arrêtés préfectoraux | Comparaison FCT-pc-001 vs APC 06/10/2022 (06-24) + RNIP série 81062 (07-18/11-26) | INFÉRENCE étayée (écart documenté) |
| FCT-vp1-008 | CAS CABROL (Lacaune) : André Cabrol, maire de Lacaune à l'époque du permis (2011), était propriétaire du terrain d'implantation du parc éolien de Puech del Vert ; condamné le 17/10/2023 par le TC de Castres pour prise illégale d'intérêts (art. 432-12 CP) : 2 500 € amende + 800 € dommages-intérêts aux associations ARVIEE et CALELH ; promoteur/SARL relaxés du chef de recel | La Dépêche 17/10/2023 (déjà documenté 18-30, FCT-axeD-012 à 016) | CONFIRMÉ |
| FCT-vp1-009 | GAP-1c RÉSOLU : Philippe Folliot, ancien député puis sénateur (intermédiaire en 2010 auprès du ministère de la Défense, avec Cabrol, pour court-circuiter un avis militaire défavorable sur le réseau de vol à très basse altitude) a été auditionné comme témoin dans la procédure, a indiqué avoir cru que le terrain appartenait à la commune, et n'a JAMAIS été poursuivi, mis en examen ou signalé (ni PNF, ni procureur, ni HATVP) pour cette affaire | La Dépêche 11/12/2015 (mise en examen de Cabrol, intervention 2010 de Folliot) ; 29/08/2023 et 05/09/2023 (audience : témoignage de bonne foi de Folliot) | CONFIRMÉ (recherche web dédiée) |
| FCT-vp1-010 | Aucun appel d'André Cabrol n'est documenté dans les sources publiques consultées (La Dépêche, bases judiciaires, observatoire Anticor) : la condamnation du 17/10/2023 est présumée définitive | Recherche web (La Dépêche, bases) 11/08/2026 | CONSTAT D'ABSENCE (aucune source d'appel trouvée) |
| FCT-vp1-011 | CAS FONTRIEU : le journal municipal de janvier 2026 documente que le parc de Puech Cornet contribue au budget communal par la location des TERRAINS COMMUNAUX (sur lesquels sont installées les éoliennes) + 50 % de l'IFER + participation annuelle 10 000 € : le propriétaire foncier est la COMMUNE, pas un élu individuel | Journal municipal Fontrieu n°15, janvier 2026 (déjà documenté 06-44, FCT-fo-001/002) | CONFIRMÉ |
| FCT-vp1-012 | Aucun bail individuel sur terrain privé d'un élu de Fontrieu (ou proche) n'est documenté dans les 7 journaux municipaux (2018-2026) ni le site communal ; le bail initial 2004-2005 n'est pas publié (GAP-fo-3 ouvert) | Fontrieu.fr + journaux municipaux (06-44) | CONSTAT D'ABSENCE (documenté) |
| FCT-vp1-013 | Le maire de Fontrieu Didier Gavalda (élu 03/2020, réélu 03/2026) est délégué au SDET (Syndicat Départemental d'Énergie du Tarn) et aux Communes Forestières ; la commune a délibéré le 12/10/2018 pour entrer au capital du projet d'extension « Fontrieu Energie » (avec le SDET) : pattern « commune associée à la gouvernance de l'exploitant », distinct de la prise illégale d'intérêts classique | La Dépêche 11/03/2020 + 06-24 (FCT-pc-016) + 06-44 (FCT-fo-004/006/012) | CONFIRMÉ (pattern documenté, sans signal pénal) |
| FCT-vp1-014 | CAS BARRE : la presse documente des « terres de particuliers louées par Valeco » pour le parc de Combaynart/Puech de Cambert (renouvellement 2024-2026) : les propriétaires sont des personnes privées non nommées publiquement | La Dépêche 01/02/2025 (déjà documenté 05-54, FCT-b1-010) | CONFIRMÉ (existence) + GAP (identité) |
| FCT-vp1-015 | Le maire de Barre Vincent Vidal affiche sa satisfaction vis-à-vis du projet (« 30 ans qu'on n'avait pas eu la visite d'un préfet », 12/07/2023) et aucun conflit d'intérêts ne le concerne dans les sources publiques | La Dépêche 19/07/2023 (déjà documenté 05-54, FCT-b1-015) | CONSTAT D'ABSENCE (aucun signal) |
| FCT-vp1-016 | Les parcelles d'emprise possible du parc de Barre/Combaynart : section AO (0030, 0036, 0039, 0054) côté Barre et section 0D (1824, 0249, 0296) côté Murat-sur-Vèbre : l'identité des propriétaires exige la matrice nominative (non accessible en OSINT) | Apicarto IGN 11/08/2026 + dénominations couffrau/COUFFE (RNIP archive) | CONSTAT D'ACCÈS PARTIEL |
| FCT-vp1-017 | Le pattern national est une alerte institutionnelle : le SCPC (rapport 2014) a alerté sur la multiplication des dossiers de prise illégale d'intérêts d'élus dans l'éolien terrestre (baux sur terrains propres, 1 000 à plus de 10 000 €/an/éolienne ; ex. 54 000 €/an pour 5 éoliennes, 108 000 €/an pour 10, chiffres rapportés par Reporterre) | Rapport SCPC 2014, relayé par Reporterre (veille 11-42, VPB-02/VPC-04) | FACT institutionnel (alerte) |
| FCT-vp1-018 | Verdict consolidé du test : sur 3 communes testées, 1 pattern CONFIRMÉ et pénalisé (Cabrol/Lacaune, le seul cas du corpus Tarn), 1 variante différente (Fontrieu : commune propriétaire, pas élu), 1 GAP (Barre : propriétaires privés non identifiés) ; aucun autre cas de prise illégale d'intérêts éolienne documenté dans le Tarn | Synthèse croisée 11/08/2026 (dossier + recherche) | VERDICT |

---

## 3. Le test parc par parc

### 3.1 Lacaune / Puech del Vert : le pattern CONFIRMÉ (le seul cas pénalisé du corpus)

Le cas Cabrol est l'exacte configuration décrite par le SCPC : un maire **propriétaire du terrain d'implantation** d'un parc éolien. La chaîne complète est documentée :

- **2008** : projet lancé par la SARL Puech del Vert (devenue FERME EOLIENNE DE PUECH DEL VERT, SIREN 495300600, adresse Valeco Montpellier) ;
- **2010** : intervention de Cabrol (maire de Lacaune) accompagné du député **Philippe Folliot** auprès du ministère de la Défense pour obtenir un avis favorable, malgré l'avis défavorable initial (éoliennes sur un « réseau de vol à très basse altitude » des avions de chasse) ;
- **2011** : permis de construire délivré en septembre (municipalité Cabrol) ;
- **17/10/2023** : condamnation du TC de Castres pour prise illégale d'intérêts (432-12) : 2 500 € d'amende + 800 € de dommages ; promoteur relaxé.

**Enseignement** : le pattern SCPC est réel et a été pénalisé dans le Tarn, mais la sanction est faible (3 300 € au total) et le promoteur (Valeco via la SARL) a été relaxé. Le bénéficiaire de la rente (EnBW depuis 2019, groupe public allemand) n'est pas impliqué dans l'infraction.

**GAP-1c (Folliot) résolu** : auditionné comme témoin, il a plaidé sa bonne foi (croyance que le terrain était communal), jamais poursuivi. Aucun signalement HATVP. La condamnation de Cabrol est présumée définitive (aucun appel documenté).

### 3.2 Fontrieu / Puech Cornet : une variante structurellement différente (commune propriétaire)

Le test à Fontrieu produit un résultat inattendu mais net : **les éoliennes de Puech Cornet sont installées sur des terrains appartenant à la commune** (journal municipal janvier 2026 : « location des terrains communaux »). Le propriétaire foncier est donc la **personne morale communale**, pas un élu individuel. Le pattern SCPC (élu propriétaire privé) ne s'applique pas.

En revanche, un pattern connexe est documenté (et n'est pas une infraction) :
- le maire Gavalda est **délégué au SDET**, syndicat départemental d'énergie du Tarn, homologue du SIEDS des Deux-Sèvres qui contrôle 3D ENERGIES (exploitant du parc depuis 2015) ;
- la commune a délibéré le **12/10/2018** pour **entrer au capital** du projet d'extension « Fontrieu Energie » (avec le SDET et 3D ENERGIES) ;
- le refus communal du repowering (journal 2026) montre une capacité de contrôle, pas une complaisance.

**Enseignement** : dans ce cas, l'imbrication est élu ↔ syndicat d'énergie ↔ SEM exploitante, pas élu ↔ bail personnel. C'est un signal de gouvernance à suivre (GAP-fo-1/2/3 sur les montants), pas un signal pénal.

### 3.3 Barre / Combaynart-Couffrau : GAP non résolu (propriétaires privés non identifiés)

À Barre, la presse documente des « terres de particuliers louées par Valeco » (La Dépêche 01/02/2025) : ce sont des personnes privées, non nommées. La question « un élu de Barre ou de Murat-sur-Vèbre (ou proche) est-il propriétaire d'une parcelle louée au parc ? » ne peut pas être tranchée en OSINT :

- les parcelles d'emprise possible sont identifiées (Barre AO 0030/0036/0039/0054 ; Murat 0D 1824/0249/0296) ;
- mais la **matrice cadastrale nominative** (seule source de l'identité des propriétaires) n'est consultable librement qu'au SCPC pour les communes < 2 000 habitants, avec une **déclaration d'identité interactive** que nous ne pouvons pas exécuter en automatisation (flux Struts : erreur de redirection documentée).

Le maire Vincent Vidal ne présente aucun signal documenté de conflit. Le repowering a été inauguré le 11/06/2026 avec sous-préfet, président de CdC et propriétaires terriens présents (La Dépêche 27/06/2026) : la transparence affichée ne préjuge pas de l'identité de tous les bailleurs.

---

## 4. Méthode : la route cadastre OSINT validée (à conserver dans le protocole)

Le test a permis de valider la **seule route cadastre OSINT sans clé** :

- **Apicarto IGN** : `GET https://apicarto.ign.fr/api/cadastre/parcelle?geom={"type":"Point","coordinates":[lon,lat]}` (GeoJSON URL-encodé, WGS84) renvoie `code_insee`, `nom_com`, `section`, `numero`, `feuille`, `contenance`. 12 requêtes réussies.
- **Routes écartées** : `data.cadastre.gouv.fr` (API explore : réponse vide), `cadastre.data.gouv.fr/wfs` (404), `cadastre.data.gouv.fr/api/parcelles/*` (404), WMS SCPC (GetCapabilities = HTML sans couches), SCPC automatisé (déclaration d'identité requise pour la matrice).
- **Limite** : Apicarto donne la **géométrie** (commune/section/numéro/contenance), PAS l'identité des propriétaires. L'identité exige la matrice (SCPC humain, CADA, ou sources locales).

**Leçon protocole** : pour tester « élu propriétaire foncier », la géométrie cadastrale (OSINT) identifie les parcelles d'emprise ; l'identité des propriétaires se croise ensuite par les baux publics, les délibérations, la presse et (en dernier recours) la matrice/le CADA.

---

## 5. Verdict

| Question | Réponse | Confiance |
|----------|---------|-----------|
| Pattern SCPC « élu propriétaire foncier » présent dans le Tarn ? | OUI, 1 cas documenté et pénalisé : Cabrol/Lacaune (maire propriétaire du terrain, condamné 17/10/2023) | TRÈS HAUTE (presse + condamnation) |
| Le député Folliot a-t-il été poursuivi ? | NON : témoin auditionné, bonne foi plaidée, aucun signalement | HAUTE (3 articles La Dépêche 2015-2023) |
| Fontrieu : élu propriétaire ? | NON : terrains communaux, la commune est propriétaire ; élu Gavalda délégué au SDET + commune au capital de l'extension (pattern gouvernance, sans signal pénal) | HAUTE (journaux municipaux 2018-2026) |
| Barre : élu propriétaire ? | INDÉTERMINÉ : terres de particuliers non nommés, matrice nominative inaccessible en OSINT | GAP (accès partiel) |
| Autres cas de prise illégale d'intérêts éolienne dans le Tarn ? | NON documentés (le cas Cabrol est unique dans le corpus) | MOYENNE (constat d'absence, couverture presse limitée) |

**Conclusion graduée** : la piste VP-P1 confirme que le pattern « élu propriétaire foncier votant des parcs » existe dans le Tarn (1 cas pénalisé : Cabrol), mais il n'est ni généralisé ni récurrent dans le corpus : Fontrieu relève d'une configuration différente (commune propriétaire), Barre reste indéterminé faute d'accès à la matrice. Le test ne produit donc **aucun nouveau signal pénal**, mais **une leçon de méthode** (route cadastre OSINT validée, limite de la matrice) et **une correction de localisation** (coordonnées « Puech Cornet » de la fiche Valeco pointant vers Barre/Couffrau).

---

## 6. GAP résiduels (actionnables)

| GAP | Description | Voie |
|-----|-------------|------|
| GAP-vp1-1 | Identité des propriétaires des parcelles d'emprise de Barre/Combaynart (AO 0030/0036/0039/0054 ; Murat 0D 1824/0249/0296) : y a-t-il un élu ou proche parmi les bailleurs ? | Matrice cadastrale via SCPC (déclaration d'identité manuelle) ou CADA DGFiP ; presse locale (Journal d'Ici, La Dépêche) ; associations (Nostra Montanha) |
| GAP-vp1-2 | Références cadastrales exactes des éoliennes de Puech Cornet (Fontrieu) et de Puech del Vert (Lacaune) : recouper sur les arrêtés préfectoraux (PC 2005, APC 2021/2022) | Textes des arrêtés (pages tarn.gouv verrouillées : CADA préfecture, GAP-b1-2 du 05-54) |
| GAP-vp1-3 | Bail initial 2004-2005 de Fontrieu (GAP-fo-3) : qui a signé, sur quelles parcelles, quel loyer ? | Archives communales, CADA commune, comptes administratifs |
| GAP-vp1-4 | Délibérations de Barre et Murat-sur-Vèbre sur le repowering (GAP-b-3 du 05-40) : votes, cessions foncières | Registres en mairie, presse |
| GAP-vp1-5 | Vérifier si le pattern Cabrol a des équivalents dans les autres parcs EnBW/Valeco de la région (Aveyron : Plo de la Rouquette/Murasson, Brusque) | Presse + cadastre + matrice (même méthode) |

---

## 7. Conformité

- Em-dash : 0 (grep du tiret cadratin = 0)
- Nomenclature : FCT-vp1-001 à 018 (18 faits)
- STATE : FINAL
- RUN_MANIFEST : entrée 61
- Write-back mémoire : obligatoire après recherche aboutie (fait)
- Revue critique : code-reviewer-deepseek-flash (appliquée 12:50 : compteur requêtes corrigé à 22, FCT-vp1-010 en CONSTAT D'ABSENCE, confiance du verdict sur les autres cas ramenée à MOYENNE, « ancien député puis sénateur », attribution des sources 2015/2023 précisée, explication SCPC adoucie)
