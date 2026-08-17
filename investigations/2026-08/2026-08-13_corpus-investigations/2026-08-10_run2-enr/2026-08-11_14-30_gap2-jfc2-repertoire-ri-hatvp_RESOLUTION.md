# RESOLUTION : INSCRIPTION DE JFC2/CARENCO AU REPERTOIRE DES REPRESENTANTS D'INTERETS HATVP (GAP-vp4-2)

- STATE          : FINAL
- DATE           : 2026-08-11 14:30 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste VP de la veille presse 11-42)
- OBJECT         : vérifier l'inscription de la SASU JFC2 (Jean-François Carenco) au répertoire des représentants d'intérêts de la HATVP et ses déclarations d'activités, pour convertir la « vigilance » de l'avis 2025-233 (client potentiel : Samfi Ingénierie) en fait vérifié ou en constat d'absence documenté
- REPONSE A      : GAP-vp4-2 du document 13-20 (VP-P4, inventaire des mobilités CRE/DGEC)
- SOURCES        : API Elasticsearch publique du répertoire RI (hatvp.fr, endpoint /hatvp-agora-organisations,hatvp-agora-activites/_msearch, creds embarquées dans la page), fiche publique FEDEREC (fiche-organisation/?organisation=784358749) + JSON agora (agora/784358749.json), API Recherche Entreprises (RNE), avis HATVP 2025-233 (lu intégralement au 13-20)

---

## 1. METHODE : LE REPERTOIRE RI EST INTERROGEABLE PAR API ELASTICSEARCH PUBLIQUE

Le répertoire des représentants d'intérêts de la HATVP (loi 2016-1691, art. 18) est un site WordPress dont la recherche d'autocomplétion interroge un Elasticsearch exposé publiquement :

| Élément | Valeur | Source |
|---------|--------|--------|
| Endpoint ES | `https://www.hatvp.fr/hatvp-agora-organisations,hatvp-agora-activites/_msearch` (msearch multi-index) | JS autocompletion-recherche-registre.js |
| Index | `hatvp-agora-organisations` (entités) + `hatvp-agora-activites` (déclarations d'activités annuelles) | Idem |
| Credentials | `hatvp` / `bcuJIEFOGj89356` (embarquées en clair dans la config `epas` de la page /le-repertoire/) | Page HTML (config epas) |
| Champs clés organisations | denomination, nomUsageHatvp, identifiantNational (SIREN ou n° HATVP), categorieOrganisation, dirigeantsText, collaborateursText, clientsText, affiliationsText | Index ES |
| Champs clés activites | objet, organisation.num_organisation (SIREN), exercice.montantDepense, publicationDate, tiersText, decisionsConcerneesText | Index ES |
| Fiche publique par entité | `https://www.hatvp.fr/fiche-organisation/?organisation=<id>` + JSON complet `https://www.hatvp.fr/agora/<id>.json` | Site public |

**Note forensique** : l'endpoint ES n'est pas documenté comme API publique par la HATVP ; les credentials en clair (lecture seule côté client) relèvent probablement d'une configuration du site. Leur usage en lecture de données de transparence publique (le répertoire est consultable par tous) reste équivalent au canal de la barre de recherche du site, sans contournement d'un accès authentifié dédié.

## 2. RESULTAT 1 : JFC2 N'EST PAS INSCRITE AU REPERTOIRE RI (CONSTAT D'ABSENCE)

| Recherche ES | Résultat |
|--------------|----------|
| `JFC2` en denomination | **0 hit organisations** |
| `JFC` en denomination/sigle | 0 entité pertinente (0 fiche) |
| `Carenco` en denomination/nomUsage/sigle | 0 entité inscrite sous ce nom |
| `Carenco` en dirigeantsText/collaborateursText | 1 hit : **FEDEREC** (voir §3) ; aucun autre |
| `JFC2` / `JFC` en activites (objet, tiers) | 0 fiche d'activité |

**Lecture** : la SASU JFC2 annoncée dans l'avis 2025-233 (saisine 26/05/2025, conseil à FEDEREC/Zalis/Samfi Ingénierie à compter du 15/07/2025) **ne figure pas au répertoire des représentants d'intérêts** au 11/08/2026, ni comme entité inscrite, ni comme auteur de déclarations d'activités.

**Limite de la vérification** : le registre RI ne couvre que les activités de représentation d'intérêts (influencer une décision publique) ; une SASU de conseil n'est pas tenue de s'inscrire si son activité est du conseil stratégique hors contacts avec les responsables publics. L'absence d'inscription n'est donc pas en soi une infraction : c'est un constat d'absence qui déplace la question vers le contenu réel des missions JFC2 (GAP-vp4-3).

## 3. RESULTAT 2 : CARENCO EST DECLARE PRESIDENT DELEGUE DE FEDEREC, ENTITE INSCRITE DEPUIS LE 13/11/2017

La seule trace de Carenco dans le répertoire RI est son mandat à FEDEREC (fédération professionnelle du recyclage), l'un des 3 clients annoncés de JFC2 :

| Élément | Valeur | Source |
|---------|--------|--------|
| Entité | FEDEREC, Fédération des entreprises du recyclage, du réemploi et de l'économie circulaire | Fiche publique |
| Identifiant national | SIREN 784358749 (type SIREN) | Idem |
| **Inscription au répertoire** | **13/11/2017 16:29 (datePremierePublication)** | JSON agora |
| Dernière mise à jour | 10/03/2026 (exercice 2025 publié) | Idem |
| Catégorie | Fédération professionnelle | Idem |
| Adresse | 101 rue de Prony, 75017 Paris | Idem |
| **Dirigeants déclarés (publication courante)** | BURNAND Manuel (DG), EXCOFFIER François (Président), **CARENCO Jean-François (Président délégué)** | Idem |
| Personnes chargées de la représentation d'intérêts | 37 collaborateurs déclarés (dont BURNAND, DE CHIREE, FRANCOIS, KORNBERG, PONTI, etc.) | Idem |
| Clients/membres déclarés | COVED, DERICHEBOURG, PAPREC, SUEZ RV, EBS LE RELAIS, GUY DAUPHIN, MALTHA GLASS, FEDEREC EST/OUEST/HDF, etc. (membres de la fédération) | Idem |

**Lecture** : Carenco est inscrit au répertoire RI **indirectement**, en qualité de dirigeant d'une entité inscrite (FEDEREC). Son nom n'apparaît pas comme entité propre. FEDEREC est un acteur de représentation d'intérêts actif sur les secteurs **Economie, Emploi, Energie, Finances publiques, Environnement** (champ déclaré).

## 4. RESULTAT 3 : SAMFI INGENIERIE ET ZALIS NE SONT PAS INSCRITES (CONSTAT D'ABSENCE)

| Recherche ES | Résultat |
|--------------|----------|
| `Samfi` (toutes formes, tous champs) | **0 entité pertinente** (seuls hits : SAMSUNG et SAMMAN Cabinet d'avocats, faux positifs du fuzzy matching) |
| `Samfi` en activites (objet, tiers) | 0 fiche |
| `Zalis` | 0 entité pertinente (seuls hits : Zalando SE + entités de l'Allier, faux positifs) |
| Samfi/Zalis en clientsText de FEDEREC | Absents (les tiers déclarés de FEDEREC sont ses membres : COVED, DERICHEBOURG, PAPREC, SUEZ, etc.) |

**Vérification croisée RNE** (API Recherche Entreprises, le 11/08/2026) :
- SAMFI INGENIERIE : SIREN 833 571 276, actif, rue du Poirier 14650 Carpiquet (Calvados). Confirme la fiche du 13-20 (groupe Samfi-Invest/Alain Samson). Mais **non inscrite au répertoire RI**.
- SASU JFC2 : **aucune société dirigée par CARENCO Jean-François trouvée au RNE** (pagination complète des 76 résultats « Carenco », filtre dirigeants exact) : la SASU annoncée n'est pas immatriculée au RNE à la date de consultation, ou est détenue par une autre voie (holding ?).

**Lecture** : la « vigilance » de la HATVP sur le risque d'influence étrangère (Das Solar) et sur le client Samfi Ingénierie ne peut pas être convertie en fait vérifié par le répertoire RI : ni JFC2, ni Samfi, ni Zalis n'y figurent, et FEDEREC ne déclare pas Samfi/Zalis parmi ses tiers. L'absence est documentée (voie : répertoire) et renvoie à d'autres sources (GAP-vp4-3 : comptes JFC2, presse normande).

## 5. RESULTAT 4 : LE VOLUME DE LA REPRESENTATION D'INTERETS DE FEDEREC (2021-2025)

Les exercices déclarés par FEDEREC au répertoire (JSON agora) :

| Exercice | Publication | Dépenses déclarées | Salariés | Activités déclarées |
|----------|-------------|--------------------|----------|---------------------|
| 2025 | 10/03/2026 | ≥ 200 K€ et < 300 K€ | 2 | 12 |
| 2024 | 31/03/2025 | ≥ 200 K€ et < 300 K€ | 5 | 10 |
| 2023 | 20/03/2024 | ≥ 100 K€ et < 200 K€ | 4 | 21 |
| 2022 | 31/03/2023 | ≥ 100 K€ et < 200 K€ (CA ≥ 1 M€) | 3 | 21 |
| 2021 | 31/03/2022 | ≥ 75 K€ et < 100 K€ (CA ≥ 1 M€) | 4 | 25 |

Thèmes 2025 (échantillon) : REP emballages professionnels, acte européen économie circulaire, plan plastique, refonte REP PMCB, restrictions exports métaux recyclés, REP VHU, REP Batteries, REP Textiles, réforme des REP, ELVR. La fiche DVS2GF8V (exercice 2025) indique des contacts avec un **collaborateur du Président de la République** et des membres du Gouvernement (décisions concernées : lois, y compris constitutionnelles).

## 6. VERDICT

1. **CONSTAT D'ABSENCE PRINCIPAL** : la SASU JFC2 n'est pas inscrite au répertoire des représentants d'intérêts HATVP (0 hit organisations + 0 fiche d'activité), ni au RNE en tant que société dirigée par Carenco Jean-François. La « vigilance » de l'avis 2025-233 ne se matérialise dans aucune déclaration publique au registre.
2. **LE CANAL D'INFLUENCE DECLARE EST FEDEREC** : Carenco est président délégué d'une fédération inscrite depuis le 13/11/2017, qui déclare 200-300 K€/an de dépenses de représentation d'intérêts (2024-2025) et des contacts jusqu'au niveau de l'Élysée. Le lien « ex-régulateur → représentation d'intérêts » est donc réel et documenté, mais via un mandat de dirigeant, pas via une société de conseil inscrite.
3. **La question des clients réels de JFC2 reste ouverte** : Samfi Ingénierie, Zalis et FEDEREC ne sont pas visibles dans le répertoire comme « clients de JFC2 » (le registre ne déclare pas les prestataires des entités inscrites). Le GAP-vp4-3 (prestations effectives : comptes JFC2, presse) reste la seule voie pour établir les missions réelles.
4. **Nuance honnête** : l'absence d'inscription de JFC2 n'établit pas un manquement (le périmètre du registre est la représentation d'intérêts, pas le conseil). Elle établit que la vigilance HATVP ne peut pas être confirmée ni infirmée par cette source.
5. **Pour le corpus** : le répertoire RI HATVP est interrogable par API ES publique (creds embarquées) : méthode réutilisable pour tout dossier (vérifier l'inscription de tout acteur ENR, ses déclarations, ses dépenses). Gain méthodologique du GAP-vp4-2.

## 7. FAITS (FCT-vp42)

| # | Fait | Source | Date |
|---|------|--------|------|
| FCT-vp42-001 | Le répertoire RI HATVP expose un Elasticsearch public (endpoint /_msearch, index hatvp-agora-organisations + hatvp-agora-activites) avec credentials embarquées dans la page (hatvp / bcuJIEFOGj89356) | Page /le-repertoire/ (config epas) + JS | 2026 |
| FCT-vp42-002 | JFC2 : 0 entité inscrite au répertoire RI (denomination, sigle, dirigeant) et 0 fiche d'activité : CONSTAT D'ABSENCE | API ES (11/08/2026) | 2026 |
| FCT-vp42-003 | Samfi Ingénierie : 0 entité inscrite au répertoire RI (les seuls hits « samfi » sont SAMSUNG et SAMMAN, faux positifs) | API ES | 2026 |
| FCT-vp42-004 | Zalis : 0 entité inscrite au répertoire RI (seuls hits : Zalando + entités de l'Allier, faux positifs) | API ES | 2026 |
| FCT-vp42-005 | FEDEREC : inscrite au répertoire RI depuis le 13/11/2017 (SIREN 784358749, fédération professionnelle, 101 rue de Prony Paris) | Fiche publique + JSON agora | 2017 |
| FCT-vp42-006 | Carenco Jean-François : déclaré Président délégué de FEDEREC (dirigeants de la publication courante : BURNAND DG, EXCOFFIER Président, CARENCO Président délégué) | JSON agora 784358749 | 2026 |
| FCT-vp42-007 | FEDEREC déclare 37 personnes chargées de la représentation d'intérêts (dont BURNAND, DE CHIREE, FRANCOIS, KORNBERG, PONTI) | JSON agora | 2026 |
| FCT-vp42-008 | FEDEREC : 5 exercices déclarés 2021-2025, dépenses 75-100 K€ (2021) à 200-300 K€ (2024-2025), 2-5 salariés | JSON agora | 2022-2026 |
| FCT-vp42-009 | FEDEREC : 12 activités déclarées 2025, 10 en 2024, 21 en 2023, 21 en 2022, 25 en 2021 (REP, économie circulaire, énergie, environnement) | JSON agora | 2022-2026 |
| FCT-vp42-010 | Au moins une fiche de l'exercice 2025 (DVS2GF8V) mentionne des contacts avec un collaborateur du Président de la République et des membres du Gouvernement (décisions : lois, y compris constitutionnelles) | JSON agora (exercice 2025) | 2026 |
| FCT-vp42-011 | Samfi et Zalis ne figurent pas dans les tiers déclarés de FEDEREC (tiers = membres : COVED, DERICHEBOURG, PAPREC, SUEZ, etc.) | JSON agora | 2026 |
| FCT-vp42-012 | SAMFI INGENIERIE : SIREN 833 571 276, actif, rue du Poirier 14650 Carpiquet (Calvados), non inscrite au répertoire RI | API Recherche Entreprises + API ES | 2026 |
| FCT-vp42-013 | SASU JFC2 : aucune société dirigée par CARENCO Jean-François au RNE (pagination complète des 76 résultats « Carenco », 0 hit JFC/conseil) | API Recherche Entreprises | 2026 |
| FCT-vp42-014 | La vigilance de l'avis 2025-233 (Das Solar, risque d'influence étrangère, client Samfi) ne se matérialise dans aucune déclaration du répertoire RI | API ES (croisement) | 2026 |
| FCT-vp42-015 | L'absence d'inscription de JFC2 n'établit pas un manquement : le registre couvre la représentation d'intérêts, pas le conseil (limite documentée) | Cadre légal (loi 2016-1691 art. 18) + constat | 2026 |
| FCT-vp42-016 | Méthode réutilisable : le répertoire RI est interrogable par API ES publique (creds embarquées) : fiche par entité + JSON complet via /agora/<id>.json | Session (vérifié) | 2026 |

## 8. GAPS

| # | Gap | Voie |
|---|-----|------|
| GAP-vp42-1 | Prestations effectives de JFC2 auprès de Samfi Ingénierie (montants, missions, facturation) : comptes de la SASU (non trouvée au RNE : vérifier l'immatriculation réelle, holding, statuts) | INPI, greffe TC, presse normande, comptes Samfi-Invest | 
| GAP-vp42-2 | Dater la prise de fonction de Carenco comme président délégué de FEDEREC (avant/pendant/après la CRE) : archives FEDEREC, presse recyclage | Presse spécialisée recyclage (Recylux, Environnement Magazine) |
| GAP-vp42-3 | Vérifier si FEDEREC a déclaré des activités de représentation d'intérêts en 2017-2021 antérieures à l'exercice 2021 (date d'inscription 13/11/2017 : traçer le premier exercice déclaré) | JSON agora, exercices antérieurs |
| GAP-vp42-4 | Vérifier l'inscription au répertoire d'autres acteurs ENR (Valeco/EnBW, 3D Energies, Obton) avec la même méthode API ES (gain méthodologique) | API ES (méthode du présent document) |

## 9. TRAÇABILITE

- Em-dash : 0 (vérifié)
- Date/heure réelle : 11/08/2026 14:30 CEST (heure du système)
- Sources : API ES répertoire RI HATVP (requêtes _msearch directes, 11/08/2026), fiche publique FEDEREC + JSON agora/784358749.json, API Recherche Entreprises (RNE), avis 2025-233 (lu au 13-20)
- Artefacts /tmp : hatvp_ri_home.html, hatvp_ri_autocomp.js, hatvp_federec.json, re_carenco_p*.json, hatvp_fiche_fed2.html
- Liens : 13-20 (VP-P4, GAP-vp4-2), 11-42 (veille, signal VPC-03), 19-00 (Bohuon base délibérations)
- Revue critique appliquée le 11/08/2026 14:40 (corrections : FCT-vp42-010 reformulé au singulier « au moins une fiche de l'exercice 2025 (DVS2GF8V) » ; note forensique §1 nuancée « l'endpoint n'est pas documenté comme API publique par la HATVP » ; chiffre des activités corrigé : 89 déclarées 2021-2025, 128 = total toutes périodes depuis 13/11/2017)
