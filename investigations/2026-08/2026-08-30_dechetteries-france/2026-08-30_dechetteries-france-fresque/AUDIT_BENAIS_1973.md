# AUDIT D'ANTÉRIORITÉ — Benais « Vallée de Chanrie » (Indre-et-Loire)

AS_OF : 2026-08-30 · Dossier dechetteries-france-fresque
OBJET : vérifier le `D_OUV 1973-11-26` déclaré SINOE, caractériser le site avant le néologisme « déchèterie » (1987), et trancher la primauté vs Gradignan / Arles.
MÉTHODE : sources primaires et presse locale consultées directement ; statuts V/sn/REFUTÉ/CONTAMINÉ marqués.

**AJOUT PASSÉ 2 (audit renforcé, 2026-08-30)** : corroboration presse locale (La Nouvelle République, Bourgueil 09/10/2021), rapports annuels SMIPE 2016 & 2022, fiche acteur SINOE (date de création 18/02/2004 vs organique 26/11/1973), arrêtés/recueils préfectoraux 2002-2011.

---

## 1. Fiche SINOE du service (dataset brut `/tmp/sinoe_annuaire.csv`)

Fiche C_SERVICE = **4963**, N_SERVICE = `Déchèterie de Benais` (2009→2026 inchangé).

| Champ | Valeur | Statut |
|---|---|---|
| D_OUV | **1973-11-26** | V (constante 2009→2026) |
| D_MODIF | 2025-08-11 | V |
| AD1_SITE | Vallée de Chanrie | V |
| CP / Ville | 37140 / BENAIS | V |
| LOV_MO_GEST | **REGIE** | V |
| C_ACTEUR | 857 — SMIPE (SIVOM) Val Touraine Anjou | V |
| ORIGINE_DECHET_ACC | DMA/PRO | V |

Surface totale déclarée : **1 680 m²**. Le date 1973-11-26 est **stable sur toutes les enquêtes** — valeur interne cohérente, mais cf. §3.

## 2. Corroborations locales (presse + rapports annuels)

- **La Nouvelle République, éd. Bourgueil, 09/10/2021** : « Dans la **vallée Chanrie**, commune de **Benais**, le Smipe Val Touraine Anjou dispose d'**installations de traitements des déchets ménagers : déchetterie et centre de transferts** des ordures ménagères vers l'**usine de valorisation énergétique du Sivert à Lasse (Maine-et-Loire)**. Des cinq déchetteries du Smipe, celle de Benais est la seule accessible aux véhicules > 3,5 t. » → confirme que le site est **d'abord un centre de transfert** du réseau, gravite autour de l'UVE de Lasse. (V, source locale consultée)
- **RA SMIPE 2016** : le site de Benais est décrit comme support des **transferts** vers les filières (refus de tri, papier vers UPM, encombrants vers le Sivert), avec « remise en conformité de la plateforme de déchets verts de Benais » et « étude d'extension de la déchèterie de Benais » (devenant trop exiguë) — **aucune mention d'une antédatation 1973**. (V)
- **RA SMIPE 2022** : « historique SMIPE » ne mentionne aucune déchèterie en 1973 ; vue d'ensemble : 5 déchèteries + **1 quai de transfert + 1 plateforme de stockage** ; matériauthèque de Benais inaugurée **2019**. (V)
- **Recueil des actes administratifs Indre-et-Loire** : plusieurs arrêtés interpréfectoraux (2002, 04/2011, 2020) de **modification des statuts / dénomination** du SMIPE « Val Touraine Anjou » (ex. arrêté 27/02 & 07/03/2002), dénomination à l'origine « Syndicat Mixte Intercommunal pour la Protection de l'Environnement » — le syndicat évolue, sans ouverture 1973 documentée. (V, T1/T2)
- **Fiche acteur SINOE (onglet GEST_DATA)** : « Date de création de l'acteur **dans SINOE : 18/02/2004** » (entrée référentiel). La date **26/11/1973** de la compétence **01A Collecte OMR** correspond à la **création organique du syndicat** (collecte), **pas** à une déchèterie. (V)

## 2-bis. La contradiction probatoire interne SINOE (pièce décisive)

La fiche **acteur** SINOE du SMIPE (code 857, maître d'ouvrage) liste ses **compétences déchets** :

| Compétence | Code | Date début |
|---|---|---|
| **Collecte OMR** | 01A | **26/11/1973** |
| **Collecte sélective** | 01B | 01/01/1997 |
| **Déchèterie** | 01C | **02/06/1985** |
| Traitement (délégué SIVERT) | 01D | 17/07/1995 |

Or le `D_OUV` de la déchèterie de Benais = **26/11/1973**, **exactement la date de la compétence Collecte OMR** (création du syndicat). Deux autres services du même maître d'ouvrage :
- **Transfert Benais** (service 7037) : ouverture **20/06/1983**, autorisation préfectorale **01/09/1982**.
- **Déchèterie de Benais** (service 4963) : autorisation/déclaration préfectorale **12/01/1995** (onglet « Autorisations administratives », code 01C Déclaration préfectorale).

## 3. Verdict : `D_OUV 1973` = date CONTAMINÉE (REJET de la primauté)

**Analyse de cohérence** :
- Si la déchèterie de Benais avait réellement ouvert le 26/11/1973, elle précéderait **la loi du 15/07/1975 (75-633)** de 2 ans ET **la circulaire 1987 (néologisme)** de 14 ans — un anachronisme d'équipement d'apport-volontaire « moderne » très improbable pour un petit syndicat rural (28 communes, majoritairement rural) créé à cette époque.
- La **compétence déchèterie du SMIPE date de 02/06/1985** (SINOE acteur), et le **premier site d'élimination/transfert de Benais n'ouvre qu'en 20/06/1983**. Le transfert (1983) précède de peu la compétence déchèterie (1985) ; la **déclaration préfectorale de la déchèterie elle-même est datée 12/01/1995**.
- Le `D_OUV 1973-11-26` reproduit **exactement** la date de la compétence collecte OMR (création du SIVOM). C'est le **même patron d'erreur** que l'outlier Longwy (D_OUV 1960) et Toulouse Ribaute (D_OUV **1884**, artefact évident) : une date de service non-déchèterie recopiée dans le champ déchèterie.

→ **Statut : `D_OUV 1973-11-26` très probablement CONTAMINÉ** par la date de création du syndicat / collecte OMR. La **primauté absolue de Benais est REJETÉE** jusqu'à preuve d'un acte d'ouverture 1973 (délibération, arrêté, presse). L'ouverture réelle la plus probable de la déchèterie de Benais se situe **~1985-1995** (compétence 1985 ; déclaration 1995).

## 4. Ce que restait le site avant le néologisme

- Le site de Benais (vallée Chanrie) est **en premier lieu un site de transfert / de traitement** (service 7037, ouverture 20/06/1983) du syndicat, pivot des envois vers l'UVE de Lasse et les filières — pas un apport-volontaire « moderne » isolé datant de 1973.
- **Aucune source presse/archive consultée** (La NR 2021, RA 2016/2022, assemblées préfectorales) **ne confirme une ouverture 1973**, et aucune ne revendique « Benais = première déchèterie de France ».
- La **déclaration préfectorale de la déchèterie de Benais est datée 12/01/1995** et la compétence déchèterie du SMIPE du **02/06/1985** — deux bornes postérieures à la circulaire 87-63 (néologisme), cohérentes avec l'essor des déchèteries après 1987.

## 5. Conséquences sur la fresque de primauté

- **Élimination de Benais comme candidat n°1 de la primauté absolue** (date contaminée).
- Il reste comme sites pré-1980 crédibles : **St-Aquilin-de-Pacy 1973** (Eure, Onyx/Veolia), **Ivry-la-Bataille 1975** (Eure, Veolia/Onyx) — tous deux chez les opérateurs Onyx/Veolia (à noter : Veolia revendique ses « premières déchèteries » en 1986, alors que leurs sites normands portent D_OUV 1973-75 → cohérence douteuse à interroger), **déchèteries mobiles du Haut-Jura 1974**, et **Arles 1977** (voir AUDIT_ARLES).
- La primauté doit être reformulée : **ni Gradignan (1980), ni Benais (1973 contaminé), ni un site unique, mais un faisceau d'apports-volontaires antérieurs à la circulaire 1987** sur d'anciennes décharges/dépôts.
- **Verdict final Benais** : `D_OUV 1973` = contamination par la date de création du syndicat/collecte OMR. La déchèterie de Benais, comme l'ensemble du réseau SMIPE, s'inscrit dans l'essor **post-1985/1987** (compétence 1985, déclaration 1995). **Benais est écarté de la primauté absolue.**

## TRAÇABILITÉ
- Dataset SINOE brut `/tmp/sinoe_annuaire.csv` (fiches 4963, 7037 ; INSEE 37140) — INSPECTED.
- SINOE fiche acteur SMIPE (competences : OMR 26/11/1973, sélective 01/01/1997, déchèterie 02/06/1985, transfert ; GEST_DATA création 18/02/2004) — INSPECTED (pages lues).
- SINOE fiche service 4963 (autorisation préfectorale 12/01/1995) — INSPECTED (page lue).
- SINOE fiche service 7037 (transfert Benais, ouverture 20/06/1983, autorisation 01/09/1982) — INSPECTED.
- Rapport annuel SMIPE 2022 (tourainepropre.fr, PDF 38 p., extrait texté) — INSPECTED (matériauthèque 2019, historique compétences, transfert Benais).
- Rapport annuel SMIPE 2016 (tourainepropre.fr, PDF 32 p., extrait texté) — INSPECTED (site Benais = transfert, extension déchèterie).
- La Nouvelle République, éd. Bourgueil, 09/10/2021 (« Portes ouvertes et découvertes à la déchetterie ») — INSPECTED (texte lu : vallée Chanrie, transfert vers UVE Lasse, matériauthèque).
- Recueils des actes administratifs d'Indre-et-Loire (2002, 04/2011, 2020) via indre-et-loire.gouv.fr — repérés (références d'arrêtés de modification SMIPE) — index consulté.

## GAPS / PROCHAINES FRAPPES
1. **Acte d'ouverture de la déchèterie de Benais** (délibération, arrêté ~1985/1995) — aux Archives départementales d'Indre-et-Loire / fonds SMIPE (périodiques 2001→, cotes 1290PERC/1457PERC) ; déterminant pour certifier la vraie ouverture (probablement post-1983/1985) et clore la primauté Benais.
2. **Auditer les sites Onyx/Veolia (St-Aquilin 1973, Ivry 1975, La Haie-Fouassière 1974)** — leur D_OUV 1973-75 chez un groupe qui revendique un démarrage déchèterie en 1986 est un signal de doute.
3. **Confirmer la cohérence du champ D_OUV SINOE** : distinguer « date d'enquête » vs « date d'ouverture réelle » vs « date de compétence du syndicat » (patron de contamination identifié).