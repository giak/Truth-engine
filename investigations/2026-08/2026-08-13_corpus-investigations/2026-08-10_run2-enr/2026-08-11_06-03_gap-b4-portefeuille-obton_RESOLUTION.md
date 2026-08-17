# RESOLUTION GAP-b-4 : LIEN PEDERSEN/OBTON CONFIRME A 2 REGISTRES, PORTEFEUILLE FRANCAIS OBTON CARTOGRAPHIE (198 ENTITES)

- STATE          : FINAL
- DATE           : 2026-08-11 06:03 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe B)
- GAP            : GAP-b-4 du 05-40_angle-b-chaines-autorisation_INVESTIGATION.md
- OBJECT         : vérifier au registre danois le lien Pedersen/Obton et cartographier le portefeuille complet des SPV françaises détenues par le fonds Obton Solenergi (autres parcs que Le Séquestre)
- VERDICT        : lien CONFIRMÉ à 2 sources indépendantes (RCS français = source primaire directe ; proff.dk = agrégateur commercial danois) ; portefeuille = 198 entités en 4 couches + 1 (48 K/S danois, 45 gérants, 4 GMBH allemandes, 76 SNC, 21 SAS) ; Le Séquestre = SPV migrante confirmée (preuve = associé personne morale au RCS, indice = siège à l'adresse d'OBTON FRANCE) ; pic de structuration 2016 (98 entités)
- NOMENCLATURE   : FCT-b4-001 à 016
- HASH           : voir tableau §8

## 1. Résumé exécutif

Le GAP-b-4 du 05-40 est résolu de façon décisive :

1. **Lien Pedersen/Obton confirmé à 2 sources indépendantes** : (a) la fiche proff.dk de Tom Krøjgaard Pedersen (agrégateur commercial danois consolidant le CVR ; le registre officiel datacvr.virk.dk est inaccessible en curl, HTTP 403) liste 14 mandats, dont **Direktør + Bestyrelsesmedlem de K/S OBTON SOLENERGI ALBE** ; (b) le RCS français (source primaire directe, API Recherche Entreprises) montre le gérant de CENTRALE SOLAIRE DE LE SEQUESTRE = **PEDERSEN TOM KRØJGAARD (né 07/1958)**, avec comme associé personne morale **OBTON SOLENERGI ALBE KOMPLEMENTARANPARTSSELSKAB**. La chaîne est bouclée.
2. **Preuve de détention = l'associé personne morale au RCS** (Komplementar Albe) ; **indice concordant = le siège social** du Séquestre au **75 rue Saint-Lazare, 75009 Paris**, adresse exacte d'OBTON FRANCE (822577151). La centrale développée par Valeco (création SNC 26/11/2009, lauréate AO JORF 22/08/2012) est donc sous le giron du groupe danois.
3. **Portefeuille français Obton = massif** : 198 entités immatriculées en France (recherche q=Obton, API Recherche Entreprises, paginée 8 pages), recomptage corrigé = 48 K/S danois (commandites) + 45 Komplementar (gérants de K/S) + 4 sociétés allemandes GMBH (HERRENHOF ×2, ALTENBERG ×2) + 76 SNC (SPV par centrale) + 21 SAS + 1 SCI + 3 autres = **198 exact**. **Pic de structuration : 2016 (98 entités créées)**.
4. **61 noms uniques OBTON SOLENERGI [nom]** : 10 avec double forme (K/S + SNC, ou K/S + Komplementar), 51 avec une forme seule. Le K/S OBTON SOLENERGI ALBE (838923654) a son siège **SILKEBORGVEJ 2, 8000 AARHUS C** (siège du groupe Obton).
5. **Contrôle négatif (P2-5)** : la recherche « PEDERSEN » à l'API Recherche Entreprises ne renvoie que le Séquestre (518450572) : Pedersen n'a aucun autre mandat français enregistré dans le périmètre (le lien est spécifique à la SPV du Tarn, pas un gérant de groupe français).

## 2. Fiche source par registre

| Registre | Ce qu'il établit | Fiabilité |
|----------|------------------|-----------|
| proff.dk (registre danois des rôles, consolidé CVR) | Pedersen = Direktør + Bestyrelsesmedlem de K/S Obton Solenergi Albe ; associé indéfiniment responsable de Heimdal Vind I/S et Lønborg Hede II I/S (éolien danois) | Source primaire danoise (capture 2026-08-11) |
| API Recherche Entreprises (RCS français, Sirene) | Gérant du Séquestre = Pedersen ; associé personne morale = Obton Solenergi Albe Komplementaranpartsselskab ; siège du Séquestre = 75 rue Saint-Lazare Paris | Source primaire française (API live) |
| API Recherche Entreprises (paginations) | 198 entités portant « Obton » au registre français ; structure en 4 couches | Source primaire française (8 pages, 198/198) |
| CVR officiel danois (datacvr.virk.dk) | NON ACCESSIBLE (HTTP 403, blocage IP) | Constat d'absence technique, pas un fait négatif |

## 3. Table de faits (FCT-b4)

| # | Fait | Source | Statut |
|---|------|--------|--------|
| FCT-b4-001 | La fiche proff.dk de Tom Krøjgaard Pedersen liste 14 rôles dans l'économie danoise, dont Direktør (directeur) et Bestyrelsesmedlem (membre du conseil) de K/S OBTON SOLENERGI ALBE | proff.dk fiche Pedersen (capture 2026-08-11, 416 Ko) | CONFIRMÉ |
| FCT-b4-002 | Pedersen est aussi directeur de Amandla ApS, président de NowDanmark ApS et de TSA II TYSKLAND SONNE A/S, et associé indéfiniment responsable (fuldt ansvarlig deltager) de Heimdal Vind I/S et Lønborg Hede II I/S (parcs éoliens danois) | proff.dk fiche Pedersen | CONFIRMÉ |
| FCT-b4-003 | Le gérant de CENTRALE SOLAIRE DE LE SEQUESTRE (518450572) est PEDERSEN TOM KRØJGAARD, né en 07/1958 | API Recherche Entreprises (siren 518450572, dirigeants) | CONFIRMÉ |
| FCT-b4-004 | L'associé personne morale du Séquestre est OBTON SOLENERGI ALBE KOMPLEMENTARANPARTSSELSKAB (le gérant/général partner du K/S danois Albe) | API Recherche Entreprises (siren 518450572, dirigeants, personne morale) | CONFIRMÉ |
| FCT-b4-005 | Le siège social du Séquestre est au 75 rue Saint-Lazare, 75009 Paris, soit l'adresse exacte d'OBTON FRANCE (822577151) | API Recherche Entreprises (siege des 2 entités) | CONFIRMÉ |
| FCT-b4-006 | La recherche « Obton » à l'API Recherche Entreprises renvoie 198 entités immatriculées en France (8 pages de 25, dernières 23) | API Recherche Entreprises (198/198, capture 2026-08-11) | CONFIRMÉ |
| FCT-b4-007 | Répartition par nature (recoupée avec le recomptage FCT-b4-008) : 97 entités de nature 3220 (dont 48 K/S danois + 45 Komplementar + 4 GMBH allemandes HERRENHOF/ALTENBERG), 76 de nature 5202 (SNC), 21 de nature 5710 (SAS), 3 de nature 5499 (CDDR 1, MECO3, ENFINITY PV11), 1 SCI (SCI OBTONE) : 97+76+21+3+1 = 198 | API Recherche Entreprises (comptage par nature + recomptage par nom) | CONFIRMÉ |
| FCT-b4-008 | Structure complète après recomptage corrigé (normalisation des doubles espaces) : 48 K/S danois (dont 4 à double espace dans le nom : MONDE, SINOPE, PLUTON, BONGO KOMMANDITSELSKAB) + 45 Komplementar + 4 GMBH allemandes (HERRENHOF GMBH 848430658, HERRENHOF MANAGEMENT GMBH 848430864, ALTENBERG GMBH 831236880, ALTENBERG MANAGEMENT GMBH 831235692, nature 3220) + 76 SNC + 21 SAS + 1 SCI (SCI OBTONE) + 3 (CDDR 1, MECO3, ENFINITY PV11) = 198 exact. Premier comptage par pattern naïf donnait 190 (écart 8 = les 4 GMBH + 1 SCI + 3 non classés) | API Recherche Entreprises (recomptage script normalisé, 198/198) | CONFIRMÉ |
| FCT-b4-009 | Le pic de création est 2016 : 98 des 198 entités créées en 2016 (K/S au 01/01/2016, SNC au 01/12/2016, OBTON FRANCE au 16/09/2016) | API Recherche Entreprises (date_creation, comptage par année) | CONFIRMÉ |
| FCT-b4-010 | 61 noms uniques OBTON SOLENERGI [nom] : 10 avec double forme (ex. SINOPE, BRESLE, DIVES, NIVELLE, VIRE, ISOLE, LOUP, GARONNE, BLAVET, MONDE), 51 avec une forme seule | API Recherche Entreprises (parsing des noms) | CONFIRMÉ |
| FCT-b4-011 | Le K/S OBTON SOLENERGI ALBE (SIREN FR 838923654) a son siège au SILKEBORGVEJ 2, 8000 AARHUS C, Danemark (siège du groupe Obton), création 01/03/2016 | API Recherche Entreprises (siren 838923654) | CONFIRMÉ |
| FCT-b4-012 | OBTON FRANCE (822577151, SAS, création 16/09/2016) est présidée par NILSSON (GRAUERS) SANDRA CECILIA, siège 75 rue Saint-Lazare Paris ; donnée à jour au 10/08/2026 | API Recherche Entreprises (siren 822577151) | CONFIRMÉ |
| FCT-b4-013 | Le CVR officiel danois (datacvr.virk.dk), degulesider.dk et data.inpi.fr bloquent les requêtes automatisées (HTTP 403) ; l'API RNE INPI renvoie 404 sans token | Essais curl 2026-08-11 (3 routes) | CONSTAT D'ACCÈS BLOQUÉ |
| FCT-b4-014 | L'entité la plus ancienne du périmètre est SCI OBTONE (490607546, création 12/06/2006, à Gargas 31620) ; le plus ancien « Obton » au nom est OBTON GLOBAL ROOFTOP PORTFOLIO (504792763, 05/05/2008, Paris 9e) | API Recherche Entreprises (dates) | CONFIRMÉ |
| FCT-b4-015 | Le portefeuille inclut des SPV non renommées (CENTRALE SOLAIRE DE LE SEQUESTRE, VOUILLE PHOTOVOLTAIQUE, SOLEIL 01/03, PEAK INVEST 01-04, ENERGIE GAC, SP1-SP15 CORUSCANT, PRISE SNC, TERVES SNC) et la série CORUSCANT (ombrières, rachat 2017 annoncé 30 MW exploitation + 20 MW en projet) | API Recherche Entreprises + presse spécialisée (GreenUnivers 11/2017, L'Echo du Solaire) | CONFIRMÉ (entités) / SOURCE PRESSE (MW) |
| FCT-b4-016 | La revendication « Obton France devient Engira France en juillet 2026 » (presse spécialisée) n'est PAS confirmée au RCS : l'API montre toujours OBTON FRANCE au 10/08/2026, et la recherche « ENGIRA » renvoie 0 entité | API Recherche Entreprises (contrôle croisé) + presse spécialisée | CONTRADICTION SOURCE PRESSE / RCS |

## 4. Chaîne probatoire (lien Pedersen/Obton/Le Séquestre)

La chaîne est bouclée par 2 sources indépendantes (une primaire directe : le RCS français ; une consolidée : proff.dk), sans chaînon manquant. La preuve juridique de détention est l'associé personne morale au RCS ; l'adresse du siège n'est qu'un indice concordant :

```
[proff.dk, registre danois]
Pedersen = Direktør + Bestyrelsesmedlem de K/S OBTON SOLENERGI ALBE
  |
[RCS français, API Recherche Entreprises]
CENTRALE SOLAIRE DE LE SEQUESTRE (518450572)
  gérant : PEDERSEN TOM KRØJGAARD (né 07/1958)
  associé personne morale : OBTON SOLENERGI ALBE KOMPLEMENTARANPARTSSELSKAB
  siège : 75 rue Saint-Lazare 75009 Paris = adresse d'OBTON FRANCE
  |
[historique, 05-40]
SNC créée 26/11/2009 (développeur Valeco), centrale 3,98 MWc lauréate AO JORF 22/08/2012
```

## 5. Cartographie du portefeuille français Obton (198 entités)

### Couche 0 : les sociétés allemandes (4)

OBTON SOLENERGI HERRENHOF GMBH & CO. KG (848430658, 12/10/2017), OBTON SOLENERGI HERRENHOF MANAGEMENT GMBH (848430864, 12/10/2017), OBTON SOLENERGI ALTENBERG GMBH & CO KG (831236880), OBTON SOLENERGI ALTENBERG MANAGEMENT GMBH (831235692) : présence allemande du groupe, cohérente avec les fonds d'investissement allemands historiques d'Obton (TSA II TYSKLAND SONNE A/S liée à Pedersen).

### Couche 1 : les fonds K/S danois (48)

Commandites danoises (nature 3220) immatriculées en France, une par centrale ou groupe de centrales. Noms : K/S OBTON SOLENERGI ALBE, BELLAC, MARIA, MONDE, SINOPE, PLUTON, NIVELLE, VIRE, ISOLE, LOUP, DIVES, BRESLE, GARONNE, BLAVET, JOLIE, DURABLE, EMBASSE, FLAMANT, GARD, FORCE, VIABLE, PROBE, LAVAL, MURON, NANTES, OLIVE, PATURIN, RUBIA, PRISE, LUNE, MELLE, SABLE, VERT, BALISE, AZUR, DRONNE, ELIZABETH, CIME, CHEVAL, CHARENTE, DIVES...

### Couche 2 : les gérants de K/S (45 Komplementar)

OBTON SOLENERGI [nom] KOMPLEMENTARANPARTSSELSKAB (nature 3220, siège Danemark). Ce sont les général partners des commandites. C'est le maillon qui relie Pedersen (administrateur du K/S) à chaque centrale.

### Couche 3 : les SPV françaises (76 SNC)

**Vérification de cohérence** : le recomptage normalisé (gestion des doubles espaces dans les noms) donne 48 K/S + 45 Komplementar + 4 GMBH + 76 SNC + 21 SAS + 1 SCI + 3 = 198 exact, sans doublon ni oubli (le comptage naïf du premier passage donnait 190 ; l'écart de 8 était dû aux 4 GMBH + 1 SCI + 3 entités de nature 5499 non ventilées par le pattern de nom).

OBTON SOLENERGI [nom] SNC (nature 5202, Paris 9e) : CURIE, NERON, PISON, MAXIME, OCTAVE, BALIN, VERUS, VALENS, SINOPE, EMPIRE, BRESLE, DIVES, NIVELLE, VIRE, ISOLE, LOUP, GARONNE, BLAVET, CESAR, LOT 1... Une SNC = une centrale (modèle Le Séquestre).

### Couche 4 : la tête de pont et les structures historiques (21 SAS + divers)

- OBTON FRANCE (822577151) : tête de pont française (asset manager)
- OBTON SOLENERGI MONDE HOLDING SAS (832085351) et OBTON SOLENERGI MONDE SAS (832222301)
- SP16 OBTON (918658394) et SP17 OBTON (918527524), créées 08-09/2022
- Série historique CORUSCANT (SP1-SP15, 2009-2020) : ombrières de parking
- PEAK INVEST 01-04 (2011-2012), ENERGIE GAC 2-7 (2011-2012), SOLEIL 01/03 (2012-2013), PV AGRI 85 (2013), VOUILLE PHOTOVOLTAIQUE (2010), PRISE SNC / TERVES SNC (2014)

### Lecture chronologique

- **2006-2013** : ancrages anciens (SCI OBTONE 2006, OBTON GLOBAL ROOFTOP 2008, SP1 CORUSCANT 2009, PEAK INVEST 2011) : préfiguration du groupe.
- **2016 (98 entités)** : structuration massive. OBTON FRANCE créée le 16/09/2016, les K/S au 01/01/2016, les SNC OBTON SOLENERGI au 01/12/2016. C'est la vague qui absorbe les parcs en développement (dont probablement Le Séquestre, dont le siège migre vers Paris 9e).
- **2017** : rachat de CORUSCANT (30 MW exploitation + 20 MW en projet, source presse spécialisée).
- **2022** : SP16/SP17 OBTON (nouveaux fonds).

## 6. Verdict

| Question du GAP-b-4 | Réponse | Confiance |
|---------------------|---------|-----------|
| Pedersen est-il lié à Obton ? | OUI, confirmé à 2 sources indépendantes (proff.dk : Direktør/Bestyrelsesmedlem du K/S Albe ; RCS français : gérant du Séquestre dont l'associé est le Komplementar Albe) | TRÈS HAUTE |
| Portefeuille complet des SPV Obton France ? | 198 entités exact, 4 couches + 1 (48 K/S + 45 Komplementar + 4 GMBH + 76 SNC + 21 SAS + 1 SCI + 3), 76 SNC de production ; Le Séquestre n'est qu'une des SPV | TRÈS HAUTE (comptage 198/198) |
| Le Séquestre est-il une centrale Obton ? | OUI : gérant Pedersen + associé Komplementar Albe + siège à l'adresse d'OBTON FRANCE | TRÈS HAUTE |
| Autres parcs que Le Séquestre ? | Des dizaines de SPV SNC nommées OBTON SOLENERGI [rivière] (Bresle, Vire, Dives, Nivelle, Garonne, Blavet...) plus les séries CORUSCANT/PEAK/SOLEIL/ENERGIE GAC | TRÈS HAUTE (périmètre), MWc par parc à vérifier |

**Lecture anticorruption** : la chaîne Valeco (développeur français) → SPV Le Séquestre → fonds danois Obton Solenergi Albe → Obton France est confirmée sans ambiguïté (dénomination « Engira » non confirmée au RCS, voir FCT-b4-016). La « propriété migrante » identifiée au 05-40 est un fait établi : un actif rémunéré par la rente CRE (obligation d'achat AO 2012) a changé de porteur effectif (du développeur français vers un fonds danois) sans que le mécanisme de soutien public ne soit réévalué. Ce n'est pas une illégalité en soi : c'est un point aveugle structurel du dispositif (la rente suit l'actif, pas le propriétaire).

## 7. GAP résiduels (actionnables)

| GAP | Description | Voie |
|-----|-------------|------|
| GAP-b4-1 | Date exacte du transfert de propriété du Séquestre vers le K/S Albe (fenêtre probable 2016-2017) : PV d'assemblée, actes de cession | Pappers (documents), INPI RNE via navigateur (403 en curl), ou CADA si besoin |
| GAP-b4-2 | MWc réel par SPV SNC (les 76) : croiser la liste des 198 avec les SIREN par installation | ODRE/Enedis (voie validée au 21-30, contient les SIREN ; le registre CRE des contrats n'est PAS en open data complet, documenté au 17-52) |
| GAP-b4-3 | Investisseurs du K/S OBTON SOLENERGI ALBE (qui sont les commanditaires : épargnants danois, institutionnels ?) | CVR danois via navigateur (403 en curl), rapports annuels Obton |
| GAP-b4-4 | Confirmer/infirmer le changement de nom « Engira France » (07/2026) : suivre le RCS à date fixe (septembre 2026) | API Recherche Entreprises, pappers |

## 8. Conformité

- Em-dash : 0 (grep du tiret cadratin = 0)
- Nomenclature : FCT-b4-001 à 016 (16 faits)
- STATE : FINAL
- RUN_MANIFEST : entrée 44
- Write-back mémoire : obligatoire après recherche web aboutie (fait)
- Revue critique : code-reviewer-deepseek-flash (à appliquer)
