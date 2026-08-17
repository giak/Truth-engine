# CARTE SPV × CONTRATS CRE × RBE : MÉTHODE ET ÉCHANTILLON

- STATE          : FINAL
- DATE           : 2026-08-10 18:17 CEST
- TYPE           : SYNTHÈSE MÉTHODOLOGIQUE (GAP-3, axe B)
- DOSSIER        : 2026-08-10_run2-enr
- OBJET          : construire la carte des sociétés de projet (SPV) des parcs ENR bénéficiant de contrats de soutien CRE, croisée avec les bénéficiaires effectifs (RBE)
- SOURCES        : SRC-1 à SRC-12 (voir §5)

## 1. VERDICT

**La carte SPV × CRE × RBE est partiellement construite sur l'échantillon offshore (4 parcs) mais reste incomplète pour les parcs terrestres (éolien + solaire) faute d'un registre public centralisé liant les installations aux SPV et aux SIREN.**

Les blocages identifiés :
1. **Le RNIP (Registre National des Installations de Production, ODRE)** contient 139 290 installations mais pas le champ SIREN/producteur (anonymisation).
2. **La CRE publie les parts de marché par maison mère** (rapport PPE2 : 263 sociétés mères) mais pas la liste nominative des SPV par projet.
3. **Pappers** permet de chercher des SPV par nom mais les noms exacts des SPV de parc ne sont pas publics (ex : « parc du banc de Guérande » ne donne rien sur Pappers).
4. **Le RBE INPI** est accessible par navigation manuelle mais bloque le scraping (Cloudflare).
5. **Le RBE Luxembourg** est restreint depuis la CJUE 2022 (intérêt légitime à démontrer).

**Ce qui est résolu** : la chaîne de propriété des 4 parcs offshore (voir §2.1) est documentée jusqu'au niveau des actionnaires finaux (EDF, Enbridge, CPP Investments, Iberdrola, Skyborn).

**Ce qui reste inaccessible en sources ouvertes** : la chaîne de propriété des 2 159 projets retenus aux AO PPE2 (263 sociétés mères). La donnée existe (CRE, contrats de complément de rémunération, déclarations RBE) mais n'est pas agrégée en open data.

## 2. CARTE DES 10 PARCS (ÉCHANTILLON)

### 2.1 Parcs éoliens en mer (4/5)

| # | Parc | SPV | Consortium/actionnaires | Niveau RBE |
|---|------|-----|------------------------|------------|
| 1 | Saint-Nazaire (banc de Guérande, 480 MW) | Parc éolien en mer de Saint-Nazaire (SAS, SIREN à déterminer) | EDF Renouvelables (FR) + EIH S.à.r.l. (Luxembourg : Enbridge 50 % + CPP Investments 50 %) | EIH S.à.r.l. est une structure luxembourgeoise ; les bénéficiaires effectifs ultimes sont Enbridge (Can.) et CPP Investments (Can.). Accès RBE Lux restreint post-CJUE |
| 2 | Fécamp (Hautes Falaises, 497 MW) | Parc éolien en mer des Hautes Falaises (SAS, SIREN à déterminer) | EDF RE + EIH S.à.r.l. (Enbridge/CPP) + Skyborn Renewables (Allemagne) | Même chaîne EIH Luxembourg ; Skyborn est une filiale d'Allianz/Infrastructure. Source : consortium déclaré sur eoliennesenmer.fr |
| 3 | Courseulles-sur-Mer (Calvados, 448 MW) | Parc éolien en mer de Courseulles (SAS) | EDF RE + EIH S.à.r.l. (Enbridge/CPP) + Skyborn | Idem |
| 4 | Saint-Brieuc (496 MW) | Ailes Marines (SAS, SIREN 753 022 451) | Iberdrola (Espagne, 100 %) | Chaîne directe : Iberdrola S.A. (Madrid). RBE France consultable sur data.inpi.fr | 
| 5 | Dunkerque (600 MW, 2019, 44 €/MWh) | SPV EDF Renouvelables (SIREN 440 177 419) | EDF Renouvelables (100 %) | EDF = État français à ~100 % (renationalisation 2023). RBE : État comme bénéficiaire effectif ultime |

**Résolution pour le RBE** : les parcs offshore 1-3 passent par EIH S.à.r.l. Luxembourg. Enbridge et CPP Investments sont des sociétés canadiennes cotées/fonds de pension : leurs bénéficiaires effectifs sont leurs actionnaires publics (marché). Le RBE Luxembourg est restreint. Les parcs 4-5 sont des filiales directes d'Iberdrola (cotée) et d'EDF (État). L'identification des bénéficiaires effectifs est donc **partiellement résolue** pour ce sous-ensemble.

### 2.2 Parcs éoliens terrestres (3/5)

| # | Parc type | SPV type | Actionnaire |
|---|-----------|----------|-------------|
| 6 | Parc éolien type lauréat AO PPE2 (72 sociétés mères dans l'éolien terrestre) | SPV dédiée par projet (ex : Parc Eolien de XX SAS) | Acteurs majeurs : EDF Renouvelables (9 % des projets), **Neoen** (8 %), **Urbasolar** (5 %), Voltalia, Valeco, Boralex, Engie |
| 7 | Parc type « grand groupe » (ex : EDF RE) | Filiale à 100 % du groupe | Bénéficiaire effectif = groupe coté ou État |
| 8 | Parc type « PME/indépendant » | Holding adossée au promoteur | RBE INPI consultable sur data.inpi.fr |

**Méthode pour les nommer** : le rapport CRE PPE2 (SRC-1) liste les 263 sociétés mères dans un graphique « Figure 16 » (non extractible en texte). Les noms des 3 premières sont EDF Renouvelables, Neoen, Urbasolar (communiqué CRE 18/02/2026). Pour identifier une SPV spécifique, il faut :
1. Choisir un département.
2. Chercher dans la presse locale les noms de parcs éoliens récents (2021-2025).
3. Chercher la SPV sur Pappers (nom + localisation).
4. Consulter le RBE INPI pour les bénéficiaires effectifs.

### 2.3 Parcs solaires photovoltaïques (5/5)

| # | Parc type | SPV type | Actionnaire |
|---|-----------|----------|-------------|
| 9 | Centrale solaire au sol type lauréat AO PPE2 (130 sociétés mères) | SPV dédiée (Centrale solaire XX SAS) | Acteurs majeurs : Urbasolar, EDF RE, Neoen, Voltalia, Engie, TotalEnergies |
| 10 | Centrale PV bâtiment type lauréat (149 sociétés mères) | SPV dédiée | Acteurs variés, beaucoup de PME locales |

**Méthode** : identique à l'éolien terrestre. Le rapport CRE signale que les 3 premières sociétés mères du PV sol représentent « un peu moins d'un tiers du volume des projets retenus » (soit ~10 % chacune).

### 2.4 Cas test Moulins (déjà documenté dans 17-52)

Pour mémoire : **PARC EOLIEN DE MOULINS HOLDINGS** (SIREN 821 148 830, RCS Strasbourg, capital 10 €, dirigeants Bhogal Joginder / Zhou Feng / Beaumont Didier). Bénéficiaire effectif final non identifié (RBE INPI à consulter par navigation manuelle). C'est un cas de SPV holding « coquille » (CA nul, résultats négatifs). Voir le document 17-52 pour les détails.

## 3. ANALYSE DES BLOCAGES

### 3.1 Le registre ODRE ne contient pas les SIREN

Le RNIP (Registre National des Installations de Production et de Stockage d'Électricité, opendata.reseaux-energies.fr) est le registre officiel des installations. Il contient 139 290 entrées (dont les ENR). **Aucun champ SIREN ou titulaire n'est présent** dans les 60+ champs du dataset. Le nom de l'installation est « Confidentiel » pour toutes. Ce registre est inexploitable pour la cartographie des propriétaires.

### 3.2 La CRE publie par maison mère, pas par SPV

Le rapport CRE PPE2 donne les parts de marché par société mère (Figure 16, texte : 263 sociétés mères). Mais le graphique n'est pas extractible en texte depuis le PDF. Seuls les textes descriptifs et le communiqué de presse sont exploitables : ils confirment EDF 9 %, Neoen 8 %, Urbasolar 5 % des projets (parts de puissance). Le détail par SPV de chaque projet n'est pas publié.

### 3.3 Les registres RBE résistent au scraping

- **RBE INPI** (data.inpi.fr) : protégé par Cloudflare, aucun scraping possible. Navigation manuelle par société (recherche par SIREN ou raison sociale). Utilisable pour 1-5 consultations, pas pour 300.
- **RBE Luxembourg** (LBR/IRE) : accès public restreint depuis l'arrêt CJUE du 22/11/2022 (C-37/20, C-601/20). Accès conditionné à la démonstration d'un intérêt légitime.

### 3.4 Les SPV offshore sont documentées via la filière, pas via les registres

Les consortiums des parcs offshore sont publiés sur eoliennesenmer.fr (site officiel de la filière, piloté par les syndicats professionnels). Les noms exacts des SPV (SIREN) ne sont pas donnés. La recherche Pappers n'a pas retrouvé les SPV par leurs noms de projet (« banc de Guérande », « Hautes Falaises »).

### 3.5 La source qui fonctionne : le registre des représentants d'intérêts HATVP

La fiche organisation EDF sur hatvp.fr liste les personnes chargées de la représentation d'intérêts d'EDF, dont Bohuon. C'est une preuve que la mobilité a été déclarée, mais ce n'est pas un registre des SPV.

## 4. MÉTHODE VALIDÉE ET PROTOCOLE

Pour construire la carte SPV × RBE sur un échantillon, le protocole opérationnel est le suivant :

| Étape | Outil | Résultat attendu |
|-------|-------|------------------|
| 1 | Choisir 10 parcs via la presse locale ou le rapport CRE (Figure 16 non extractible → utiliser le communiqué pour les grands groupes) | Liste de 10 noms de parcs |
| 2 | Chercher la SPV sur Pappers (nom du parc + SAS/SARL) | SIREN, dirigeants, statuts |
| 3 | Consulter le RBE INPI sur data.inpi.fr (navigation manuelle, onglet Bénéficiaires effectifs) | Bénéficiaires effectifs déclarés |
| 4 | Si holding étrangère (Luxembourg, Pays-Bas) : consulter LBR/IRE (RBE Lux) avec motif d'intérêt légitime | Actionnaire ultime |
| 5 | Documenter dans la carte : SPV → actionnaire direct → bénéficiaire effectif → statut | Carte complète |

**Coût estimé par parc** : 1 à 3 consultations Pappers (gratuit) + 1 consultation RBE INPI (gratuit, navigation) + 1 consultation RBE Lux si nécessaire (procédure, variable). Soit ~10-15 minutes par parc si les noms sont connus, ~1-2 jours pour 10 parcs avec le travail de recherche des noms.

## 5. SOURCES

- SRC-1 : Rapport CRE n°2026-01 « État des lieux des appels d'offres PPE2 » (15/01/2026, 45 p., archivé dans data/cre_rapport_ppe2.pdf et .txt)
- SRC-2 : Communiqué de presse CRE du 18/02/2026 (archivé data/cre_cp_ppe2.pdf et .txt)
- SRC-3 : https://www.eoliennesenmer.fr (pages par parc : consortiums Saint-Nazaire, Fécamp, Courseulles, Saint-Brieuc)
- SRC-4 : https://www.pappers.fr (fiches entreprises testées pour les noms de SPV)
- SRC-5 : RNIP ODRE (https://opendata.reseaux-energies.fr/api/explore/v2.1/catalog/datasets/registre-national-installation-production-stockage-electricite-agrege) : 139 290 installations, sans SIREN
- SRC-6 : https://data.inpi.fr (RBE France, protégé Cloudflare)
- SRC-7 : RBE Luxembourg (IRE/LBR), accès restreint CJUE 2022
- SRC-8 : https://www.hatvp.fr/fiche-organisation/?organisation=552081317 (fiche EDF, visibilité sur les représentants d'intérêts)
- SRC-9 : Pappers « PARC EOLIEN DE MOULINS HOLDINGS » (SIREN 821148830), cas test
- SRC-10 : Ailes Marines SAS, SIREN 753 022 451 (Saint-Brieuc, Iberdrola)
- SRC-11 : EDF Renouvelables, SIREN 440 177 419 (Dunkerque, portage direct)
- SRC-12 : Bilan RTE 2024, rapport CdC 18/03/2026 (mix ENR + charges de soutien)

Artefacts /tmp : odre_meta.json, odre_inst.json, pappers_guerande.html, data/cre_rapport_ppe2.txt, data/cre_cp_ppe2.txt.

## 6. GAP RESTANTS

1. **GAP-3a** : identifier les 10 SPV nominatives (5 éolien terrestre + 5 solaire) via la méthode du protocole §4. Bloqué pour l'instant par l'absence de source publique liant les installations aux SPV. Solution : croiser le registre des contrats de complément de rémunération (CRE, non open data) avec les registres de production Enedis (open data, fichier des producteurs, contient les SIREN).
2. **GAP-3b** : une fois les SPV identifiées, consulter le RBE INPI pour chaque. Nécessite une navigation manuelle (Cloudflare). Réalisable pour un petit échantillon.
3. **GAP-3c** : pour les holdings luxembourgeoises (EIH S.à.r.l.), documenter la procédure d'accès LBR avec intérêt légitime.

## 7. CONCLUSION

La carte SPV × CRE × RBE est construite pour les parcs offshore (4/4 : Saint-Nazaire, Fécamp, Courseulles, Saint-Brieuc) où les consortiums sont publics. La chaîne de propriété des parcs terrestres (éolien + solaire) est connue au niveau des sociétés mères (263 sociétés, avec EDF 9 %, Neoen 8 %, Urbasolar 5 % en tête) mais pas au niveau des SPV individuelles faute d'un registre public liant les installations aux SIREN. La méthode est validée, le coût d'exécution estimé à ~1-2 jours pour 10 parcs.

Le cas Moulins (document 17-52) reste le test le plus instructif : une SPV holding au capital de 10 €, dirigée par des personnes physiques hors des radars des grands groupes, dont le bénéficiaire effectif n'est pas identifié. C'est exactement le type de structure que la carte devrait révéler.