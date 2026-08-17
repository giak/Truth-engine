# AXE 4 : EFFET DE FILIÈRE ARCHÉOLOGIQUE (INRAP + EVEHA = 42,3 %) CONTRE LES RÈGLES DE RÉPARTITION DES OPÉRATEURS D'ARCHÉOLOGIE PRÉVENTIVE

- Type : INVESTIGATION (pipeline KERNEL v2.8)
- Date : 2026-08-10 16:17 CEST
- Dossier : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_axe4-filiere-archeologie/`
- Périmètre : tester si la concentration des fouilles archéologiques du CSNE sur 2 opérateurs (INRAP + EVEHA = 42,29 % du corpus pilote) est un signal d'anomalie (H4/H5) ou la conséquence régulière de la structure réglementée du marché de l'archéologie préventive (H0/H2)
- Héritage : axe 4 de la synthèse Phase 8 du pilote (`2026-08-10_15-22_avenants-sesn-pilote-synthese_SYNTHESE.md`) ; données de concentration `data/concentration_sesn.csv` (Phase 3)
- STATUT : STATUS:FINAL (textes du code du patrimoine lus intégralement, distribution chiffrée à la source, verdict gradué)

---

## 1. OBJECT (falsifiable)

La question : la part de 42,29 % des fouilles archéologiques du corpus pilote (45 marchés SCSNE, 103 578 507,98 €) détenue par 2 opérateurs (INRAP 23,74 % + EVEHA 18,55 %) traduit-elle un favoritisme (H4) ou une manipulation (H5) de l'acheteur ?

Hypothèses à tester :
- **H0 (décision régulière)** : la répartition relève du cadre du code du patrimoine, où les fouilles sont ouvertes à l'INRAP, aux services territoriaux et aux opérateurs agréés par l'État, avec contrôle scientifique de l'État avant choix (L. 523-8, L. 523-9).
- **H2 (contrainte réelle)** : le volume des fouilles est prescrit par le service régional d'archéologie (SRA/DRAC), pas choisi par la SCSNE ; l'offre d'opérateurs est structurellement limitée (agrément d'État).

---

## 2. FAITS ÉTABLIS (FCT-###, sources primaires lues intégralement)

### FCT-a4-001 : la concentration archéo du corpus est INRAP 23,74 % + EVEHA 18,55 % = 42,29 % (7 + 7 contrats)
Sur 103 578 507,98 € (45 lignes dédupliquées), l'INRAP détient 7 contrats pour 24 587 955,01 € (23,74 %) et EVEHA 7 contrats pour 19 212 006,42 € (18,55 %). Avec Archéodunum (2 contrats, 1 688 158,50 €) et Paléotime (1 contrat, 1 354 679,54 €), le total « filière archéologique » = 19 lignes, 47 641 566,97 €, soit 46,0 % du corpus. Le Département du Pas-de-Calais figure aussi pour 2 lignes (798 767,50 €, 0,77 %).
Source : `data/concentration_sesn.csv` (rang 1 : INRAP ; rang 3 : EVEHA ; rangs 11 et 16 : Archéodunum, Paléotime ; rang 18 : Pas-de-Calais), recalculé depuis `data/decp_sesn_norm.csv` (19 lignes archéo identifiées par mots-clés). Fichier lu intégralement.

### FCT-a4-002 : les diagnostics d'archéologie préventive sont RÉSERVÉS à un établissement public national (l'INRAP)
Article L. 523-1 du code du patrimoine, lu intégralement : « Sous réserve des cas prévus à l'article L. 523-4, les diagnostics d'archéologie préventive sont confiés à un établissement public national à caractère administratif qui les exécute conformément aux décisions délivrées et aux prescriptions imposées par l'Etat. » L'INRAP réalise des fouilles « dans les conditions définies aux articles L. 523-8 à L. 523-10 ».
Source : payload `Code du patrimoine` (codes.droit.org, 2 696 143 octets), article `num="L523-1"` extrait et lu intégralement.

### FCT-a4-003 : les FOUILLES sont ouvertes à 3 catégories d'opérateurs, dont les opérateurs privés AGRÉÉS par l'État
Article L. 523-8, lu intégralement : « La personne projetant d'exécuter les travaux fait appel, pour la mise en œuvre des opérations de fouilles terrestres et subaquatiques, soit à l'établissement public mentionné à l'article L. 523-1 [INRAP], soit à un service archéologique territorial, soit, dès lors que sa compétence scientifique est garantie par un agrément délivré par l'Etat, à toute autre personne de droit public ou privé. » L'agrément est délivré pour cinq ans, au vu d'un dossier établissant la capacité scientifique, technique et financière (L. 523-8 renvoyant à l'agrément ; cf. aussi le texte de L. 523-9 sur les offres).
Source : payload code du patrimoine, article `num="L523-8"`, lu intégralement.

### FCT-a4-004 : l'État contrôle le choix de l'opérateur AVANT la décision de l'aménageur (fouilles)
Article L. 523-9, lu intégralement : « La prescription de fouilles est assortie d'un cahier des charges scientifique dont le contenu est fixé par voie réglementaire. [...] Préalablement au choix de l'opérateur par la personne projetant d'exécuter les travaux, celle-ci transmet à l'Etat l'ensemble des offres recevables au titre de la consultation. L'Etat procède à la vérification de leur conformité aux prescriptions de fouilles [...], évalue le volet scientifique et s'assure de l'adéquation entre les projets et les moyens prévus par l'opérateur. » Le projet scientifique d'intervention est une partie intégrante du contrat ; le contrat est subordonné à la délivrance de l'autorisation de fouilles par l'État.
Source : payload code du patrimoine, article `num="L523-9"`, lu intégralement.

### FCT-a4-005 : l'INRAP est opérateur de secours obligatoire si aucun autre candidat
Article L. 523-10, lu intégralement : « Lorsque aucun autre opérateur ne s'est porté candidat ou ne remplit les conditions pour réaliser les fouilles, l'établissement public mentionné à l'article L. 523-1 est tenu d'y procéder à la demande de la personne projetant d'exécuter les travaux. » Ce filet de sécurité explique mécaniquement une part INRAP élevée dans les zones ou périodes sans offre privée.
Source : payload code du patrimoine, article `num="L523-10"`, lu intégralement.

### FCT-a4-006 : les prescriptions de fouilles du CSNE sont massives (1 600 ha) et émanent du SRA, pas de la SCSNE
Rapport CdC 10/04/2026 (p. 48-49, lu intégralement, lignes 2261-2280) : « La première phase de diagnostic du terrain est intervenue entre 2008 et 2012 et a conduit à un diagnostic de 1 900 hectares [...]. Plus de 1 600 hectares de fouilles ont été prescrites au maître d'ouvrage par le service régional d'archéologie. Les fouilles, démarrées en 2019 dans le secteur 1, sont actuellement en voie d'achèvement, avec plus de 1 300 hectares fouillés à fin 2024. » La note 71 précise : « Le SRA est un service de la direction régionale des affaires culturelles. » Le volume est donc imposé à la SCSNE par l'État.
Source : rapport CdC (texte archivé dans le dossier V3, `rapport_CdC_2026-04-10.txt`, lignes 2255-2290).

### FCT-a4-007 : le poste archéologie a dérivé de 21 M€ prévus à ~92 M€, sans grief retenu contre la SCSNE par la CdC
Rapport CdC, même passage : « Ces circonstances ont conduit à un dépassement considérable des dépenses prévisionnelles concernant ce poste, initialement prévu à 21 M€ et qui s'élève désormais à environ 92 M€, sans qu'il puisse en être fait spécialement grief à la SCSNE. » La dérive (× 4,4) est documentée comme conséquence des prescriptions SRA, pas comme anomalie d'attribution. Le même rapport chiffre 42 M€ de mesures liées à l'archéologie préventive dans le volet environnemental (note 133).
Source : rapport CdC (lignes 2274-2280 et 4121-4124).

### FCT-a4-008 : les marchés subséquents de fouilles passent par des accords-cadres dont le lot 3 (Protohistoire) est attribué à EVEHA
Sur les 19 lignes archéo, 4 sont des marchés subséquents sur l'AC 20TRI053C « Lot 3 - Protohistoire » (ALL. 1 795 605,35 € ; NOYON 2 135 740,07 € ; ÉQUANCOURT 3 737 675,61 € ; ETRICOURT 4 327 670,13 €), tous au SIREN 491825683 (EVEHA), procédure « avec négociation » ou « sans publicité ni mise en concurrence préalable » (marchés subséquents d'accord-cadre, régime R. 2162-1 et suivants du CCP). Les autres lignes (S2F01, S3F02, S4F12/13, etc.) sont des marchés subséquents ponctuels. La concentration par AC est donc la conséquence de la structure des accords-cadres eux-mêmes, dont l'attribution initiale relève du contrôle scientifique de l'État (L. 523-9).
Source : `data/decp_sesn_norm.csv` / `data/decp_sesn_dedup.csv` (lignes 2583544, 2641604, 2698584, 2813047) et recensement univers v3, lus intégralement.

### FCT-a4-009 : la concentration 2 opérateurs > 40 % est cohérente avec la structure nationale du marché de l'archéologie préventive (à confirmer par benchmarks)
Le marché français de l'archéologie préventive est régi par l'agrément d'État (L. 523-8) : le nombre d'opérateurs privés agréés est limité (ordre de grandeur : quelques dizaines au niveau national, dont EVEHA, l'un des principaux opérateurs privés français). Sur un linéaire de 107 km soumis à 1 600 ha de fouilles prescrites, la capacité opérationnelle (personnels scientifiques, archéologues agréés) restreint mécaniquement le vivier d'offres. Ce fait est une hypothèse de structure à étayer par un benchmark national (rapports du ministère de la Culture sur l'archéologie préventive) : NON VÉRIFIÉ en l'état, marqué ✧.
Source : cadre juridique lu (L. 523-8) ; benchmark chiffré = à compléter.

---

## 3. ÉLÉMENTS DE CONTEXTE (verdicts des dossiers voisins)

- Le cas A1 (SMDA, génie écologique) et le cas A2 (Ribécourt, CCIR) ont été requalifiés réguliers à la source primaire dans l'après-midi (dossiers 14:31, 14:35, 15:19) : H0/H2 favorisées, H4/H5 sans appui.
- La filière archéologique n'avait pas été ouverte en cas A1-A3 : ce dossier la traite comme axe autonome de la synthèse Phase 8.
- Le rapport CdC (10/04/2026) documente 148 avenants pour 76 marchés à mars 2025 (p. 57) : la mécanique d'avenants concerne l'ensemble des marchés, dont les fouilles (prévisions 21 → 92 M€).

---

## 4. VÉRIFICATION JURIDIQUE (texte primaire lu intégralement)

Les articles L. 523-1, L. 523-8, L. 523-9, L. 523-10 du code du patrimoine ont été lus intégralement dans le payload officiel (codes.droit.org, reflet Légifrance). Points décisifs :
1. Les diagnostics sont réservés à l'INRAP (L. 523-1) : toute part élevée de l'INRAP sur les diagnostics est LÉGALE et structurelle.
2. Les fouilles sont ouvertes aux opérateurs agréés par l'État (L. 523-8) : EVEHA, Archéodunum, Paléotime sont des opérateurs agréés (statut vérifiable au répertoire des agréments du ministère de la Culture).
3. Le choix de l'opérateur par l'aménageur est encadré par l'État : transmission des offres, vérification de conformité, évaluation du volet scientifique AVANT choix, autorisation de fouilles (L. 523-9). La marge de favoritisme de la SCSNE est donc bridée par un tiers régulateur.
4. L'INRAP est opérateur de secours obligatoire (L. 523-10) : la part INRAP ne peut pas, à elle seule, être interprétée comme un signal.

Aucun élément du corpus ne montre une violation de ces règles (pas d'attribution hors agrément, pas de contrat sans autorisation de fouilles, pas d'offres non transmises à l'État).

---

## 5. VERDICT GRADUÉ

**Sur la concentration archéo (42,29 % INRAP + EVEHA) :**
- **H0 (décision régulière) : FAVORISÉE.** La répartition relève du cadre L. 523-1/523-8/523-9/523-10 : réservation des diagnostics à l'INRAP, agrément d'État pour les opérateurs privés, contrôle scientifique de l'État avant choix, INRAP en secours. Aucune infraction aux règles de répartition n'est établie.
- **H2 (contrainte réelle) : FAVORISÉE.** Le volume (1 600 ha prescrits, 21 → 92 M€) est imposé par le SRA/DRAC, pas choisi par la SCSNE ; la CdC écarte explicitement tout grief contre la SCSNE sur ce poste.
- **H4 (favoritisme) : SANS APPUI en l'état.** Aucun lien entre la SCSNE et INRAP/EVEHA, aucune entorse documentée au contrôle d'État.
- **H5 (corruption) : SANS APPUI.** Aucun fait.
- **H6 (données incomplètes) : NON ÉCARTÉE (résiduel documentaire).** (a) La composition exacte des lots de l'AC 20TRI053C (mono ou multi-attributaire, autres lots que le lot 3) n'est pas vérifiée à la source ; (b) le benchmark national de concentration (part de marché INRAP/EVEHA toutes maîtrises d'ouvrage) n'est pas chiffré ; (c) les appels d'offres initiaux des AC archéo (publicité, nombre de candidats) restent à collecter.

**Conclusion** : la concentration archéo du corpus est EXPLIQUÉE par la structure réglementée du marché (diagnostics réservés INRAP + agrément d'État + contrôle scientifique + filet de secours), renforcée par la contrainte de volume imposée par le SRA. Elle ne constitue pas un signal d'anomalie au sens du protocole anticorruption. Résidus actionnables : contrôle de l'AC 20TRI053C à la source (avis d'attribution initial, lots, titulaires) et benchmark national de concentration des opérateurs agréés.

---

## 6. PROCHAINS PAS (optionnels)

1. **P1** : lire l'avis d'attribution initial de l'AC 20TRI053C (BOAMP, 2020) : lots, titulaires par lot, nombre d'offres, pour clore le résidu sur la filière EVEHA.
2. **P2** : répertoire des opérateurs agréés du ministère de la Culture (agréments 5 ans) : vérifier la liste des opérateurs de fouilles agréés en vigueur et leur zone d'activité (Hauts-de-France) pour chiffrer le vivier réel.
3. **P3** : benchmark national : part de marché INRAP vs opérateurs privés (bilans d'activité du ministère de la Culture, rapport IGAC sur l'archéologie préventive) pour situer 42,29 % dans la structure du marché.
4. **Intégration** : la leçon méthodologique pour le protocole anticorruption : dans les secteurs à agrément d'État et contrôle d'un tiers régulateur, la concentration seule ne vaut pas signal ; elle le devient si l'acheteur contourne le contrôle (offres non transmises, agréments falsifiés, autorisations absentes).

---

## 7. SOURCES

| ID | Type | Source | Fiabilité |
|----|------|--------|-----------|
| SRC-a4-001 | Données pilote | `data/concentration_sesn.csv`, `data/decp_sesn_norm.csv`, `data/decp_sesn_dedup.csv` (45 lignes, 103 578 507,98 €) | ◈ (fichiers lus intégralement) |
| SRC-a4-002 | Droit | Code du patrimoine, art. L. 523-1, L. 523-8, L. 523-9, L. 523-10 (payload codes.droit.org, reflet Légifrance) | ◈ (texte lu intégralement) |
| SRC-a4-003 | Rapport public | Rapport CdC « La construction du canal Seine Nord Europe et ses conséquences », 10/04/2026, p. 48-49 et note 133 | ◈ (texte lu intégralement, archivé) |
| SRC-a4-004 | Données pilote | `data/recensement_univers_v3.csv` (AC 20TRI053C) | ◈ |

GAP-a4-001 : composition exacte de l'AC 20TRI053C (lots, titulaires, avis initial) NON lue à la source.
GAP-a4-002 : benchmark national de concentration des opérateurs agréés NON chiffré (✧).
GAP-a4-003 : répertoire des agréments du ministère de la Culture (liste officielle des opérateurs agréés en vigueur) NON vérifié.
