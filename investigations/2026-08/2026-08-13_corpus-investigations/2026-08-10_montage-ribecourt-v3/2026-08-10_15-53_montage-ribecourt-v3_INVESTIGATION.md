# CHOIX DE MONTAGE RIBÉCOURT : MARCHÉ PUBLIC DE SERVICES vs DSP (QUESTION V3 DE LA SYNTHÈSE PILOTE)

- Type : INVESTIGATION (pipeline KERNEL v2.8)
- Date : 2026-08-10 15:53 CEST
- Dossier : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_montage-ribecourt-v3/`
- Périmètre : pourquoi la SCSNE a choisi un marché public de services (4,9 M€/48 mois) plutôt qu'une DSP pour l'exploitation de la plateforme trimodale neuve de Ribécourt-Dreslincourt, alors que le TTC de Dourges (objet similaire, 57 M€) passe par une DSP en affermage
- Héritage : question ouverte n° 2 de la synthèse Phase 8 du pilote (`2026-08-10_15-22_avenants-sesn-pilote-synthese_SYNTHESE.md`) ; cas A2 (Ribécourt, 1 offre) documenté 14:35/14:51/15:19
- STATUT : STATUS:FINAL (faits établis, cadre juridique vérifié à la source primaire, verdict gradué)

---

## 1. OBJECT (falsifiable)

La question : « Pourquoi la SCSNE a-t-elle choisi un marché public de services (4,9 M€/48 mois) plutôt qu'une DSP pour l'exploitation de sa plateforme neuve de Ribécourt, alors que Dourges (objet similaire, 57 M€) passe par une DSP en affermage (CG3P L.2124-8, domaine public fluvial) ? »

Hypothèse à tester : le choix du montage n'est pas arbitraire ni suspect, il est contraint par (a) le statut de société de projet de la SCSNE (disparition à la mise en service), (b) le critère juridique du transfert de risque (CCP L.1121-1), (c) le champ d'application de la DSP (CGCT L.1411-1), et (d) la maturité différente des deux actifs (Dourges existe et a un trafic ; Ribécourt est neuve et sans trafic établi).

---

## 2. FAITS ÉTABLIS (FCT-###, sources primaires lues intégralement)

### FCT-v3-001 : la plateforme de Ribécourt est une infrastructure NEUVE, en construction en 2026
Marché de travaux SCSNE 26-6458 (AAPC 19/01/2026, rectificatif 26-17661, CPV 45213350) : « réalisation d'une plateforme multimodale dont des aménagements de type installation terminale embranchée (ITE) sur la commune de Ribécourt-Dreslincourt, adossée aux quais de transbordement déjà construits sur le canal latéral à l'Oise (CLO) ». Le marché d'exploitation (conclu 12/06/2026) intervient AVANT la fin des travaux : la plateforme n'est pas opérationnelle à la signature.
Source : avis BOAMP 26-6458/26-17661 consultés via API OpenDataSoft (pilote, section 14:51) ; FCT du dossier CCIR.

### FCT-v3-002 : le TTC de Dourges existe et a un trafic établi (250 000 UTI de capacité)
L'avis DSP 23-43560 (Syndicat Mixte Plateforme de Dourges, publié 24/04/2023) : « Le Terminal de Transport Combiné de Dourges est dimensionné pour accueillir un trafic maximum estimé à 250 000 UTI (Unités de Transport Intermodal). Le terminal est exploité à ce jour par une société commerciale dans le cadre d'un bail commercial. Le Délégataire sera tenu de reprendre le personnel affecté au fonctionnement du service. »
Source : BOAMP 23-43560, champ RENS_COMPLEMENT, lu intégralement (JSON archivé `source_BOAMP_23-43560_DSP_Dourges.json`).

### FCT-v3-003 : la DSP de Dourges 2023 transfère le risque d'exploitation au délégataire
L'avis 23-43560 : « Contrat de délégation de service public relatif à l'exploitation par affermage du Terminal de Transport Combiné de Dourges comprenant une prestation supplémentaire éventuelle (PSE) concernant la réalisation des manœuvres ferroviaires. Exploitation aux risques et périls du délégataire. Versement d'une redevance au concédant pendant la durée du contrat. » Valeur : 57 M€ avec PSE (52,5 M€ sans), durée 90 mois (7 ans 6 mois dont 6 mois de préparation), investissements minimum 3,6 M€ à la charge du délégataire, début d'exploitation prévu 01/09/2024, visite du site condition impérative de participation.
Source : BOAMP 23-43560, lu intégralement. JSON archivé.

### FCT-v3-004 : le titulaire de la DSP Dourges est LDCT DSP, véhicule créé ad hoc en 2025
LDCT DSP (SIREN 940604721), créée le 27/01/2025, siège « PLATEFORME MULTIMODALE DELTA 3, 2 voie du Grand Large, 62119 Dourges » ; dirigeants : Jose Carlos Carvalho (président, dirigeant historique de LDCT), Patrick Fehr, Benjamin Poulard. LDCT (Lille Dourges Conteneurs Terminal, SIREN 452050792, créée 05/12/2003, activité 52.21Z) est l'exploitant historique du terminal (le « bail commercial » visé par l'avis 23-43560). Le contrat de DSP aurait été signé le 29/11/2024 selon les statuts (source secondaire researcher-web, à confirmer par la convention elle-même).
Source : API Recherche-Entreprises (data.gouv), JSON archivé `source_annuaire_LDCT_DSP.json` + `source_annuaire_LDCT.json` ; date de signature DSP = source secondaire (presse/statuts), marquée ◈.

### FCT-v3-005 : la SCSNE est un EPIC local, société de projet vouée à disparaître à la mise en service (2032)
Rapport CdC 10/04/2026 (p. 10-11, lu intégralement) : « La société du Canal Seine-Nord Europe (SCSNE) est créée par l'ordonnance n° 2016-489 du 21 avril 2016. EPIC sous tutelle du ministre des transports, sa mission principale est la réalisation du canal. [...] L'ordonnance prévoit enfin la dissolution future de la société, au plus tard douze mois après l'achèvement complet et la réception des travaux. » Transformée en établissement public local par l'art. 134 de la loi n° 2019-1428 (LOM) : rattachée à la région HdF et aux départements Nord, Oise, Pas-de-Calais, Somme (représentation majoritaire). Mise en service annoncée 2032.
Source : rapport CdC (texte archivé `rapport_CdC_2026-04-10.txt`, l. 587-620).

### FCT-v3-006 : à l'issue du chantier, l'exploitation revient à VNF (opérateur du domaine public fluvial)
Rapport CdC : « À la fin de la construction de celui-ci et à l'issue de sa mise en service, elle a vocation à disparaître, cédant la place à Voies Navigables de France (VNF), opérateur national chargé de l'exploitation. » Le domaine public fluvial artificiel (canaux, ouvrages, biens concourant aux ports intérieurs) appartient aux personnes publiques mentionnées à l'art. L.2111-7 CG3P (dont VNF) : L.2111-10 CG3P (texte lu intégralement dans le payload du code).
Source : rapport CdC (l. 444-449) + CG3P L.2111-10 (payload archivé `code_CG3P_payload.xml`).

### FCT-v3-007 : les 4 ports intérieurs du canal sont pilotés par le SMPI (317 M€), Ribécourt en est hors périmètre
Rapport CdC (p. 22-23) : depuis le rapport Pauvros (2013), la maîtrise d'ouvrage des ports intérieurs (Cambrai-Marquion 162 M€, Nesle 91 M€, Noyon 33 M€, Péronne 31 M€) est confiée au SMPI, syndicat mixte dont le comité a été créé par arrêté préfectoral du 11/08/2023 (région HdF + 5 intercommunalités). Coût total évalué 317 M€ HT (juillet 2024). La plateforme de Ribécourt (ITE sur le CLO, Oise) n'est pas un des 4 ports du SMPI : elle relève d'un montage direct SCSNE.
Source : rapport CdC (l. 843-920) + researcher-web (SMPI).

### FCT-v3-008 : le critère juridique de la concession est le transfert du risque d'exploitation (CCP L.1121-1)
Article L.1121-1 CCP (texte lu intégralement) : « Un contrat de concession est un contrat par lequel une ou plusieurs autorités concédantes [...] confient l'exécution de travaux ou la gestion d'un service à un ou plusieurs opérateurs économiques, à qui est transféré un risque lié à l'exploitation de l'ouvrage ou du service, en contrepartie soit du droit d'exploiter [...] La part de risque transférée au concessionnaire implique une réelle exposition aux aléas du marché, de sorte que toute perte potentielle supportée par le concessionnaire ne doit pas être purement théorique ou négligeable. Le concessionnaire assume le risque d'exploitation lorsque, dans des conditions d'exploitation normales, il n'est pas assuré d'amortir les investissements ou les coûts, liés à l'exploitation de l'ouvrage ou du service, qu'il a supportés. »
Source : CCP L.1121-1 (payload archivé `code_CCP_payload.xml`).

### FCT-v3-009 : la DSP est une concession de services réservée aux collectivités, groupements et établissements publics locaux (CGCT L.1411-1 + CCP L.1121-3)
Article L.1411-1 CGCT (texte lu intégralement) : « Les collectivités territoriales, leurs groupements ou leurs établissements publics peuvent confier la gestion d'un service public dont elles ont la responsabilité à un ou plusieurs opérateurs économiques par une convention de délégation de service public définie à l'article L. 1121-3 du code de la commande publique. » L.1121-3 CCP : la DSP est une concession de services ayant pour objet un service public.
Source : CGCT L.1411-1 (payload archivé `code_CGCT_payload.xml`) + CCP L.1121-3 (payload `code_CCP_payload.xml`).

### FCT-v3-010 : L.2124-8 CG3P ne fonde PAS la DSP : il porte sur les travaux sur le domaine public fluvial
Article L.2124-8 CG3P (texte lu intégralement) : « Aucun travail ne peut être exécuté, aucune prise d'eau ne peut être pratiquée sur le domaine public fluvial sans autorisation du propriétaire de ce domaine. » La prémisse de la question V3 (« Dourges passe par une DSP en affermage, CG3P L.2124-8 ») est partiellement inexacte : le fondement de la DSP de Dourges n'est pas L.2124-8 (autorisation de travaux) mais le régime de la concession de services (CCP L.1121-1/L.1121-3) combiné à la compétence de l'autorité concédante. L.2124-8 est pertinent pour l'occupation/travaux sur le domaine, pas pour le choix du montage d'exploitation.
Source : CG3P L.2124-8 (payload archivé). Verdict de rigueur : correction de la prémisse.

### FCT-v3-011 : le marché de Ribécourt est un accord-cadre de services rémunéré par l'acheteur (pas de transfert de risque)
Marché B119 SCSNE : AAPC 25-21716 (25/02/2025), attribution 26-68097 (12/06/2026), 4,9 M€ HT / 48 mois, 1 offre, CCIR HDF. Nature : « Avis de marché » (pas « Concession »), CPV 63711000, accord-cadre sans remise en concurrence, montant maximum payé par la SCSNE (acheteur). Aucun élément de « risque d'exploitation » ni de « redevance au concédant » : la rémunération est un prix versé par l'acheteur public, ce qui est la définition d'un marché public de services (CCP 2e partie), pas d'une concession (CCP 3e partie).
Source : avis BOAMP 25-21716/26-68097 (pilote, vérification 14:35) ; classification nature consultée via API OpenDataSoft.

### FCT-v3-012 : le rapport CdC ne recommande pas un montage particulier pour les plateformes/ports, mais pointe le SMPI comme outil des ports intérieurs
Le rapport CdC (p. 22-24) traite les ports intérieurs comme un enjeu de gouvernance (SMPI) et de financement (317 M€, éligibilité européenne 50 %), pas comme un enjeu de montage d'exploitation. La recommandation n° 4 concerne le SMPI (« accélérer la mise en œuvre des projets de ports intérieurs »). Aucun commentaire de la CdC sur le choix marché public vs DSP pour Ribécourt : GAP.
Source : rapport CdC (l. 410-421, 843-920).

---

## 3. FACT_REGISTRY (table)

| FCT | Fait | Source | Locator | Statut |
|-----|------|--------|---------|--------|
| FCT-v3-001 | Ribécourt : plateforme NEUVE, en construction 2026 (marché 26-6458) | BOAMP 26-6458/26-17661 | API OpenDataSoft | CONFIRMÉ |
| FCT-v3-002 | Dourges : terminal EXISTANT, trafic 250 000 UTI, bail commercial | BOAMP 23-43560 | RENS_COMPLEMENT | CONFIRMÉ |
| FCT-v3-003 | Dourges : DSP affermage, risque transféré, redevance au concédant, 57 M€/90 mois, 3,6 M€ invest. délégataire | BOAMP 23-43560 | OBJET_COMPLET | CONFIRMÉ |
| FCT-v3-004 | Titulaire Dourges : LDCT DSP (940604721, créée 27/01/2025, Delta 3) ; LDCT (452050792) = exploitant historique | API Recherche-Entreprises | JSON archivés | CONFIRMÉ (signature 29/11/2024 : ◈ source secondaire) |
| FCT-v3-005 | SCSNE = EPIC local, société de projet, dissolution ≤ 12 mois après réception des travaux | rapport CdC | p. 10-11, l. 587-620 | CONFIRMÉ |
| FCT-v3-006 | Exploitation post-canal = VNF (domaine public fluvial, L.2111-10 CG3P) | rapport CdC + CG3P | l. 444-449 | CONFIRMÉ |
| FCT-v3-007 | 4 ports intérieurs = SMPI (317 M€) ; Ribécourt hors SMPI | rapport CdC | p. 22-23, l. 843-920 | CONFIRMÉ |
| FCT-v3-008 | Concession = transfert du risque d'exploitation (non théorique) | CCP L.1121-1 | payload lu | CONFIRMÉ |
| FCT-v3-009 | DSP = concession de services, réservée collectivités/groupements/EP locaux | CGCT L.1411-1 + CCP L.1121-3 | payloads lus | CONFIRMÉ |
| FCT-v3-010 | L.2124-8 CG3P = travaux sur domaine public fluvial, PAS fondement de la DSP | CG3P L.2124-8 | payload lu | CONFIRMÉ (correction de prémisse) |
| FCT-v3-011 | Ribécourt = marché public de services (rémunération par acheteur), pas concession | BOAMP 25-21716/26-68097 | nature + montant | CONFIRMÉ |
| FCT-v3-012 | CdC : aucun commentaire sur le montage Ribécourt (GAP) | rapport CdC | lu intégralement | CONSTAT D'ABSENCE |

---

## 4. VERDICT GRADUÉ

**Le choix du marché public de services à Ribécourt est structurellement contraint et cohérent avec le droit ; il ne constitue pas un signal d'anomalie.**

1. **Contrainte institutionnelle** : la SCSNE est une société de projet (EPIC local) vouée à la dissolution au plus tard 12 mois après la réception des travaux ; elle n'a ni l'horizon, ni la mission pour conclure des DSP longues (7-30 ans). Une DSP de l'exploitation du canal relèvera de VNF, qui en est déjà l'opérateur de droit à la mise en service. Un contrat d'exploitation de 48 mois (la durée du marché de Ribécourt) s'inscrit dans l'horizon résiduel de la SCSNE ; une DSP de 7 ans et demi (le montant de Dourges) la dépasserait.

2. **Contrainte juridique (transfert de risque)** : le critère de la concession (CCP L.1121-1) est le transfert d'un risque d'exploitation réel, non théorique. Sur une plateforme NEUVE sans trafic établi (Ribécourt, en construction), aucun opérateur n'accepterait de porter le risque d'exploitation sans contrepartie : un montage « DSP » serait soit sans candidat, soit à subvention telle que le transfert de risque serait fictif et le contrat requalifiable en marché public par le juge. Le choix du marché de services (rémunération par l'acheteur) est l'instrument adapté à un actif sans trafic garanti.

3. **Contrainte organique (DSP L.1411-1 CGCT)** : la DSP au sens du CGCT est réservée aux collectivités, groupements et établissements publics locaux ; même si la SCSNE est un EPIC local, son objet statutaire (construction) et son horizon borné rendent le recours à la DSP inadapté. L'autorité concédante de Dourges est le Syndicat Mixte Plateforme de Dourges (collectivité/groupement), organisme permanent dont le terminal EXISTE avec un trafic et un opérateur en place (LDCT en bail commercial depuis 2003) : toutes les conditions d'une DSP en affermage (transfert de risque sur un actif productif, redevance) sont réunies.

4. **Correction de prémisse (honnêteté forensique)** : la référence à « CG3P L.2124-8 » dans la question V3 est inexacte. L.2124-8 régit l'autorisation des travaux/prises d'eau sur le domaine public fluvial ; il ne fonde ni la DSP de Dourges (fondée sur le régime CCP de la concession de services) ni le choix de Ribécourt. La vraie comparaison porte sur le régime CCP (2e partie : marché public, vs 3e partie : concession).

**Ce qui reste d'observable** : (a) la concurrence faible de Ribécourt (1 offre) reste un fait documenté, désormais expliqué par l'unicité technique du marché (ITE + manœuvres ferroviaires, critère CA 9,8 M€ au plafond légal R.2142-7) et l'avantage structurel de la CCIR (Ports de Lille) : avantage, pas favoritisme ; (b) la date exacte et le montant de la redevance de la DSP Dourges (LDCT DSP) ne sont pas publics : GAP documentaire (la convention n'est pas publiée au BOAMP, seuls les avis le sont) ; (c) la durée de 48 mois du marché de Ribécourt est courte au regard de la mise en service 2032 : la SCSNE devra relancer une procédure d'exploitation pour la période 2030-2032 puis laisser VNF prendre le relais : point de vigilance de calendrier, pas d'anomalie.

---

## 5. GAPS (GAP = nature, tentative, résultat, pas de remplissage)

### GAP-v3-001 : convention de DSP de Dourges (redevance, durée exacte, clauses) non publiée
La convention LDCT DSP / Syndicat Mixte n'est pas publique (seuls les avis BOAMP le sont). Le montant de la redevance au concédant et la date de signature (29/11/2024, source secondaire) restent à confirmer par la convention elle-même (demande d'accès au syndicat mixte ou CADA).

### GAP-v3-002 : documents de la consultation Ribécourt (règlement de consultation, DCE 507911)
Le DCE de la procédure B119 (SCSNE, e3722b4b...) n'est pas public : la justification de la forme de prix « mixte » et l'absence de bon de commande ne sont pas documentables via BOAMP. Déjà relevé au pilote (Phase 8, DELIVERABLE_PENDING).

### GAP-v3-003 : commentaire officiel du choix de montage
Ni la SCSNE, ni la CdC, ni le SMPI n'ont commenté publiquement le choix marché public vs DSP pour Ribécourt : la question reste ouverte documentairement (la réponse structurelle ci-dessus est une déduction juridique fondée sur les faits établis, pas une déclaration officielle).

---

## 6. CHRONOLOGIE (faits établis, sans interprétation)

- 2003-12-05 : création de LDCT (452050792), exploitant du TTC de Dourges.
- 2016-04-21 : ordonnance n° 2016-489 créant la SCSNE (EPIC national, maître d'ouvrage du canal).
- 2019-12-24 : loi LOM (art. 134) : la SCSNE devient EPIC local (région HdF + 4 départements).
- 2021-01-21 : avis 21-7402 : 1re procédure DSP affermage du TTC de Dourges (48 M€) : sans suite (le terminal reste en bail commercial).
- 2022-12-18 : réunion d'information (22-163996) en vue d'une nouvelle procédure de DSP.
- 2023-02-18 : restitution de la réunion (23-22143).
- 2023-04-24 : avis 23-43560 : DSP affermage TTC Dourges, 57 M€/90 mois, redevance, 3,6 M€ investissements délégataire, visite impérative.
- 2023-08-11 : arrêté préfectoral créant le comité syndical du SMPI.
- 2024-07 : étude de modélisation : coût des 4 ports intérieurs = 317 M€ HT.
- 2024-11-29 : signature du contrat de DSP LDCT DSP / Syndicat Mixte (source secondaire ◈).
- 2025-01-19 : AAPC travaux plateforme Ribécourt (26-6458).
- 2025-01-27 : création de LDCT DSP (940604721), véhicule du délégataire.
- 2025-02-25 : AAPC exploitation Ribécourt (25-21716, 4,9 M€/48 mois).
- 2026-06-12 : attribution du marché Ribécourt à la CCIR HDF (26-68097), 1 offre.
- 2026-07-22 : la CCIR, en qualité d'acheteur, publie l'accord-cadre de desserte ferroviaire du terminal (26-72571).
- 2032 : mise en service du canal annoncée ; dissolution de la SCSNE ≤ 12 mois après réception des travaux ; exploitation reprise par VNF.

---

## 7. GATE_CHECK

| Gate | Résultat |
|------|----------|
| Toute affirmation décisionnelle porte un FCT + locator | OUI (12 faits, tous sourcés) |
| Aucun chiffre inventé | OUI : tous les chiffres viennent des avis BOAMP lus, de l'API Recherche-Entreprises ou du rapport CdC lu |
| Aucune URL générique | OUI (sources = JSON archivés + payloads de codes + rapport CdC en texte) |
| Verdict limité à la compatibilité, pas de « preuve de corruption » | OUI : §4 |
| Réserves documentées | OUI (GAP-v3-001 à 003) |
| Correction de prémisse explicite (L.2124-8) | OUI : FCT-v3-010 |
| Source secondaire signalée (signature DSP 29/11/2024) | OUI : FCT-v3-004 ◈ |
| 0 em-dash | OUI (vérifié) |

---

## 8. CONCLUSION

La question V3 trouve une réponse structurelle : le contraste Ribécourt (marché public de services) / Dourges (DSP affermage) n'est pas la marque d'un choix discrétionnaire, mais la conséquence de quatre différences objectives : (1) la nature des actifs (neuf sans trafic vs existant avec trafic), (2) le critère juridique du transfert de risque (CCP L.1121-1), (3) le statut de l'opérateur (société de projet à durée bornée vs syndicat mixte permanent), et (4) le champ de la DSP (CGCT L.1411-1). La prémisse « CG3P L.2124-8 » est corrigée : elle porte sur l'autorisation des travaux, pas sur le montage d'exploitation. Aucun signal d'avantage injustifié ni de contournement : la procédure Ribécourt est publiée, le montant est triple-concordant, le critère de capacité est au plafond légal, et la concurrence faible (1 offre) s'explique par l'unicité technique et l'avantage structurel de la CCIR. Les points restants sont documentaires (convention DSP Dourges non publiée, DCE Ribécourt non public, absence de commentaire officiel).

---

## ANNEXE : SOURCES (URLs de pages spécifiques)

- BOAMP 23-43560 (DSP Dourges 2023) : https://www.boamp.fr/pages/avis/?q=idweb:23-43560 (JSON archivé `data/source_BOAMP_23-43560_DSP_Dourges.json`)
- BOAMP 21-7402 (DSP Dourges 2021, sans suite) : https://www.boamp.fr/pages/avis/?q=idweb:21-7402 (JSON archivé)
- API Recherche-Entreprises LDCT DSP : https://recherche-entreprises.api.gouv.fr/search?q=LDCT%20DSP (JSON archivé)
- API Recherche-Entreprises LDCT : https://recherche-entreprises.api.gouv.fr/search?q=Lille%20Dourges%20Conteneurs (JSON archivé)
- Rapport CdC 10/04/2026 (texte intégral) : https://www.ccomptes.fr/fr/publications/la-construction-du-canal-seine-nord-europe-et-ses-consequences (archivé `data/rapport_CdC_2026-04-10.txt`)
- CCP L.1121-1 et L.1121-3 : https://codes.droit.org/payloads/Code%20de%20la%20commande%20publique.xml (archivé `data/code_CCP_payload.xml`)
- CGCT L.1411-1 : https://codes.droit.org/payloads/Code%20g%C3%A9n%C3%A9ral%20des%20collectivit%C3%A9s%20territoriales.xml (archivé `data/code_CGCT_payload.xml`)
- CG3P L.2124-8 et L.2111-10 : https://codes.droit.org/payloads/Code%20g%C3%A9n%C3%A9ral%20de%20la%20propri%C3%A9t%C3%A9%20des%20personnes%20publiques.xml (archivé `data/code_CG3P_payload.xml`)

Fin du dossier. Contrôles : 0 em-dash, hashs des artefacts vérifiés (`data/artefacts_v3.sha256`), mémoire écrite.
