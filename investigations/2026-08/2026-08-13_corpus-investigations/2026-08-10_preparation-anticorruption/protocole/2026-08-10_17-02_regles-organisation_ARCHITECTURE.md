# RÈGLES D'ORGANISATION DES FICHIERS (ANTICORRUPTION) : CONTRAINTES ABSOLUES

> Type : ARCHITECTURE. Version : 1.0 (2026-08-10). Statut : EN VIGUEUR immédiate.
> Motif de création : erreurs d'organisation répétées le 10/08/2026 (création d'un dossier parallèle `2026-08-10_iceberg-max-v2/`, puis d'un sous-dossier `run2-enr/iceberg-max-v2/`, au lieu d'intégrer les fichiers à la racine du dossier de travail dédié `run2-enr/`). L'utilisateur : « tu fous des fichiers partout, c'est le BORDEL ». Ces règles sont des INTERDITS, pas des recommandations.
> Hiérarchie : ce fichier complète AGENTS.md (convention de nommage) et le README du dossier commun. En cas de conflit, ce fichier gagne sur l'organisation des fichiers.

## R1. UN TRAVAIL = UN DOSSIER, PAS PLUS

- Toute investigation, tout complément, toute synthèse relevant d'un sujet existant vit dans **le dossier de travail DÉDIÉ de ce sujet** (le dossier RUN le plus récent, ou celui désigné par l'utilisateur).
- **INTERDIT** de créer un dossier parallèle pour un travail qui relève d'un dossier existant.
- Exemple vécu : les documents ICEBERG MAX v2 (faisceaux, doctrine, matrices juridiques) relèvent du run ENR → ils doivent vivre dans `2026-08-10_run2-enr/`, PAS dans un dossier `2026-08-10_iceberg-max-v2/`.

## R2. LA RACINE, PAS LES SOUS-DOSSIERS

- Les documents finaux (INVESTIGATION, HYPER_MATRICE, APPLICATION, REGISTRE, SYNTHESE) se posent **à la racine du dossier de travail**.
- **INTERDIT** de créer un sous-dossier intermédiaire du type `dossier-de-travail/sous-dossier/` pour loger un document. Le sous-dossier est une couche inutile.
- Seuls deux sous-dossiers sont autorisés, et uniquement à la racine du dossier de travail :
  - `data/` : artefacts bruts (PDF, CSV, XML, scripts, hashes).
  - `cada_lettres/` (ou `droit_reponse/`) : lettres de demande d'accès et questionnaires.
- **EXCEPTION UNIQUE** : le dossier commun anticorruption suit une structure par nature décrite à la règle R12 (la racine plate ne s'applique qu'aux dossiers d'ENQUÊTE).
- Exemple vécu : `run2-enr/iceberg-max-v2/` était une couche interdite → intégration des 3 documents à la racine de `run2-enr/`.

## R3. VÉRIFIER AVANT DE CRÉER (règle du grep)

- **AVANT de créer un dossier ou d'écrire un fichier**, vérifier :
  1. `ls investigations/2026-08/2026-08-13_corpus-investigations/` : un dossier pertinent existe-t-il déjà ?
  2. `grep -rl <sujet> investigations/2026-08/2026-08-13_corpus-investigations/` : un fichier existant couvre-t-il déjà le sujet ?
- Si un dossier pertinent existe → écrire dedans, à sa racine.
- Si aucun n'existe → le nouveau dossier est justifié, MAIS vérifier d'abord avec l'utilisateur quel est le dossier de travail de la session (R5).

## R4. NOM DE FICHIER = SUJET, PAS ARTEFACT D'ORGANISATION

- Convention AGENTS.md : `YYYY-MM-DD_HH-MM_<sujet>_<TYPE>.md`.
- **INTERDIT** que le nom de fichier porte le nom d'un dossier parallèle ou d'une sous-structure. Le chemin EST le dossier ; le nom décrit le sujet et le type.
- Exemple vécu : `2026-08-10_16-44_iceberg-max-v2_faisceaux_HYPER_MATRICE.md` porte « iceberg-max-v2 » dans le nom : toléré en l'état (déjà créé), mais les créations futures ne doivent pas répéter le dossier dans le nom si elles vivent dans le dossier de travail du run.

## R5. EN CAS DE DOUTE SUR L'EMPLACEMENT : DEMANDER

- Si l'emplacement n'est pas évident (plusieurs dossiers possibles, dossier de travail non désigné), **demander à l'utilisateur AVANT de créer un dossier ou d'écrire un fichier**.
- Un fichier au mauvais endroit coûte plus cher (déplacement, mises à jour de références, confusion) qu'une question posée en amont.

## R6. TOUT DÉPLACEMENT = MISE À JOUR DES RÉFÉRENCES

- Si un fichier est déplacé (correction d'erreur) :
  1. vérifier les hashes SHA-256 après déplacement (le contenu ne doit pas changer) ;
  2. mettre à jour TOUTES les références au chemin (dashboard `*_REGISTRE.md`, RUN_MANIFEST, README) : `grep -rn <ancien-chemin> investigations/` doit retourner 0 après correction ;
  3. consigner le déplacement dans le journal du dashboard (date, motif, avant/après).

## R7. CHECK-LIST DE CLÔTURE D'UNE SESSION (obligatoire)

Avant de déclarer un travail terminé, exécuter :
1. `find <dossier-de-travail> -type f | sort` : la structure est plate à la racine (seuls `data/` et `cada_lettres/` en sous-dossiers).
2. Pour le dossier commun : `ls -p <dossier-commun>` ne montre QUE `README.md` et les sous-dossiers de R12 (doctrine/, protocole/, suivi/, pistes/, data/, archive/).
3. `grep -rn '<nom-du-dossier>/\1/' investigations/` : aucune référence à un sous-dossier fantôme.
4. Hashes vérifiés : dossier d'enquête (racine plate) : `sha256sum -c *.sha256` ; dossier commun : `sha256sum -c data/*.sha256` (les hashes sont centralisés dans `data/`).
5. `grep -c $'\u2014' <fichiers-rédigés>` : 0 em-dash (règle projet : le tiret cadratin U+2014 est interdit dans les textes rédigés).
6. `ls -d <dossier-parallèle-suspect>` : aucun dossier parallèle créé par erreur.
7. Mettre à jour le dashboard (sessions, artefacts, journal).

## R8. ARTEFACTS = DANS `data/`, JAMAIS À LA RACINE

- PDF, CSV, XML, scripts, JSON, captures : dans `data/` du dossier de travail.
- **INTERDIT** de déposer un artefact brut à la racine du dossier de travail ou dans un sous-dossier ad hoc.
- Chaque artefact important porte son hash SHA-256 dans `data/`.

## R9. UN SEUL RUN_MANIFEST PAR DOSSIER DE TRAVAIL

- Le dossier de travail contient un seul `RUN_MANIFEST.md` à sa racine, qui recense : l'objectif, les sources, les artefacts, les documents produits (avec chemins relatifs plats et hashes), et les NEXT_ACTION.
- Tout document produit dans le dossier est référencé dans ce RUN_MANIFEST le jour même.

## R11. LES PROTOCOLES TRANSVERSES VIVENT DANS LE DOSSIER COMMUN, JAMAIS DANS UN DOSSIER D'ENQUÊTE

- Les protocoles et registres qui servent TOUTES les enquêtes (accès aux documents, canaux numériques, registre des demandes d'accès, playbook des sources) vivent dans le dossier commun `2026-08-10_preparation-anticorruption/`, PAS dans le dossier d'un run ou d'une enquête spécifique.
- **INTERDIT** de créer un artefact transverse (modèle CADA, registre, inventaire de canaux) dans un dossier d'enquête.
- Seules les pièces SPÉCIFIQUES à une enquête (une lettre de demande ciblée sur les marchés d'un projet, un questionnaire propre à un dossier) vivent dans le dossier de cette enquête, sous `cada_lettres/` ou `data/`.
- Toute demande d'accès, où qu'elle soit rédigée, est référencée le jour même dans le registre central `2026-08-10_17-11_registre-demandes-acces_REGISTRE.md` (sous-dossier `protocole/` du dossier commun).
- Exemple vécu (10/08 17:07) : les modèles email CRE/DGEC ont été créés dans `run2-enr/cada_lettres/` sans registre central : c'est corrigé, le registre central référence désormais les 8 demandes des 3 dossiers.

## R12. STRUCTURE DU DOSSIER COMMUN ANTICORRUPTION (PAR NATURE)

- Le dossier commun `2026-08-10_preparation-anticorruption/` n'est PAS un dossier d'enquête : il suit une structure par nature, PAS la racine plate de R2.
- **Racine : UNIQUEMENT `README.md`.** Aucun autre fichier ne se pose à la racine du dossier commun.
- Sous-dossiers (liste exhaustive, à respecter pour toute création) :
  - `doctrine/` : références stables (corruption_definition.md, corruption_brainstorm.md, corruption_brainstorm_2.md) et capitalisation (16-30 leçons pilote).
  - `protocole/` : les ARCHITECTURE opérationnelles (pilote 07-10, playbook 12-38, règles 17-02, canaux 17-10) et le registre des demandes 17-11.
  - `suivi/` : le dashboard (07-19) et les comptes rendus de session (12-39).
  - `pistes/` : les fiches PISTE d'enquêtes planifiées (07-29).
  - `data/` : artefacts bruts et hashes.
  - `archive/` : éléments de revue ou documents historiques (ex. `tmp3-revue-externe-2026-07-45`).
- Le dossier commun ne contient PAS de `cada_lettres/` : les demandes d'accès vivent dans les dossiers d'enquête (R11) et sont référencées au registre 17-11.
- Toute création dans le dossier commun choisit le sous-dossier selon la NATURE du document ; en cas de doute, R5 (demander à l'utilisateur).
- Exemple vécu (10/08 17:12) : 12 fichiers posés à la racine du dossier commun → restructuration en doctrine/protocole/suivi/pistes/data/archive.

---

## JOURNAL DES VERSIONS

- **v1.0 (2026-08-10 17:02)** : création à la demande de l'utilisateur après erreurs d'organisation répétées (dossier parallèle iceberg-max-v2, sous-dossier run2-enr/iceberg-max-v2). Règles R1-R10.
- **v1.1 (2026-08-10 17:11)** : ajout de la règle R11 (protocoles transverses dans le dossier commun) après l'erreur d'avoir créé des artefacts CADA dans le dossier ENR sans registre central. Règles R1-R11.
- **v1.2 (2026-08-10 17:12)** : ajout de la règle R12 (structure par nature du dossier commun : doctrine/protocole/suivi/pistes/data/archive, racine = README seul, pas de cada_lettres/ dans le dossier commun) et amendement de R2 (la racine plate ne s'applique qu'aux dossiers d'enquête, exception dossier commun) et R7 (check-list : racine du dossier commun propre, R7 renuméroté en 7 points, commande de vérification des hashes précisée par type de dossier). Règles R1-R12.
