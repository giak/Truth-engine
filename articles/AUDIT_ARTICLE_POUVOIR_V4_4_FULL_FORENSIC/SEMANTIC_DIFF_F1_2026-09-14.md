# SEMANTIC_DIFF, tranche F1, les cinq faits contredits du masterwork

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`.
Empreinte avant : `f1b43a8262536d16be89009daa45b9a2c1bfbaf488c71adc9ed40b99d4e080ce`.
Empreinte après : **`6b0b5af69dc652cbdb7e78157915d7bea04fc494191ebd0ac7bd2b32f13ecfb1`**.
Sauvegarde : `/tmp/ARTICLE_MASTERWORK_AVANT_F1.md` (empreinte identique à l’état avant).

Source de la tranche : `VERIFICATION_MASTERWORK_5_FAITS_2026-09-14.md`, qui avait identifié les cinq faits et **proposé** les corrections sans les appliquer. F1 les applique. Aucune correction n’a été ajoutée qui ne figure dans cette note.

**Huit lignes modifiées, aucune ajoutée ni supprimée** : 3, 9, 11, 19, 20, 67, 101, 113. 308 lignes avant et après. 45 935 → 46 157 octets. 5 204 → 5 244 mots.

---

## 1. Les huit éditions, ligne par ligne

### Fait 1, l. 67, Rokh Solis

> **Avant** : « … en France par des prestataires privés israéliens **agissant pour le compte de commanditaires d’affaires ou d’État**. »
> **Après** : « … en France, **liées à un opérateur privé israélien**. Les marqueurs techniques et la proximité avec Blackcore sont documentés ; **le commanditaire reste non identifié**. »

Motif : INV‑026, INV‑071 et INV‑134 portent tous « sponsor Blackcore/Rokh Solis non identifié », et `EVALUATION_APPORT_BUNDLE_PRO_ISRAEL` §6.5 interdit d’importer cette affaire. L’édition reprend la formulation du corpus. Deux apostrophes ASCII disparaissent avec le membre retiré (« d’affaires », « d’État »).

### Fait 2, l. 101, chronologie Alstom

> **Avant** : « `[3 Mars 2026] Relance de l’information judiciaire pénale par la justice française (Anticor)` »
> **Après** : « `[20 Fév 2026] Anticor se constitue partie civile ; l’information judiciaire ouverte en déc. 2022 reste en cours` »

Motif : `INVESTIGATION_ALSTOM_GE_MACRON_2026-09-12.md` date l’ouverture du volet à **décembre 2022**, la constitution de partie civile au **20 février 2026**, et décrit l’instruction comme « toujours en cours » en mars 2026. Aucune relance n’a eu lieu. Le titre de la source **[57]** disait déjà « Anticor **veut** relancer » ; le jalon transformait le vœu en acte.

Le jalon reste le dernier de la chronologie, l’ordre est donc préservé. **[57] ne devient pas orpheline** : elle reste citée à la l. 108.

### Fait 3, l. 113, Front uni chinois

> **Avant** : « … les révélations de la DGSI et la décision du Conseil d’État confirmant l’existence en France de **neuf stations** de police clandestines **associées au Front Uni chinois et à la province du Fujian**. Ces relais informels ont exercé des pressions, des opérations de contrôle et des **rapatriements forcés**… »
> **Après** : « … les révélations de la DGSI, **qui a identifié neuf relais de stations de police**, et la décision du Conseil d’État **constatant qu’une association du Fujian avait hébergé une station clandestine** servant de relais à des organes du Parti et au ministère chinois de la Sécurité publique. Ces relais informels ont exercé **des pressions et des opérations de contrôle**… »

Motif : INV‑025 écrit « neuf **relais** de stations » et attribue au Conseil d’État **une** station, hébergée par une association du Fujian. « Rapatriement » : **zéro occurrence** dans tout le dossier. Le membre ajouté reprend la qualification du corpus (« organes du PCC chargés du contrôle de la diaspora et ministère chinois de la Sécurité publique »).

### Fait 4, l. 9 et l. 20, rang d’exportateur d’armement

> **l. 9** : « se classe au **3e** rang mondial des exportateurs d’armement » → « se classe au **2e** rang mondial des exportateurs d’armement ».
> **l. 20** (encadré) : « • **3e** exportateur mondial d’armes » → « • **2e** exportateur mondial d’armes ».

Motif : MnemoLite `7ce6073c-501d-4351-8e11-dafd70d261a0`, statut `VERIFIE`, 20 août 2026 : France **2e** exportateur 2021‑2025, 9,8 % mondial, SIPRI, communiqué du 9 mars 2026. Le « 3e » du masterwork recopiait `INV-002_CORPUS_MAP.csv`, ligne `NOT_REVERIFIED` du 30 mai 2026.

**Les deux occurrences ont été corrigées.** N’en corriger qu’une aurait laissé le prologue en contradiction avec son propre encadré.

### Fait 5, l. 3, l. 11 et l. 19, les 70 %

> **l. 3 (sous‑titre)** : « 8,9 milliards de pénalités, **70 % de dépendance cloud** et des mobilités ministérielles » → « 8,9 milliards de pénalités, **un marché du cloud détenu à 70 % par trois acteurs américains** et des mobilités ministérielles ».
> **l. 11 (prologue)** : « **70 % de ses données publiques et de santé ont été transférées sur des serveurs nord‑américains** soustraits à sa juridiction » → « **environ 70 % de son marché du cloud est détenu par trois fournisseurs américains, auxquels sont confiées des données publiques et de santé** soustraites à sa juridiction ».
> **l. 19 (encadré)** : « • **Dépendance cloud 70 % (GAFAM)** » → « • **Marché cloud 70 % (3 acteurs US)** ».

Motif : le chiffre traçable est une **part de marché**, pas un **volume de données**. Le membre retiré affirmait que 70 % des données publiques et de santé *avaient été transférées* ; rien ne l’établit, ni dans le dossier, ni en mémoire, ni dans les sources secondaires retrouvées. La formulation d’arrivée dit ce que le chiffre mesure.

**Ce que F1 ne tranche pas, et qu’il faut décider.** Le chiffre lui‑même **reste non sourcé** : la note de vérification demandait de le sourcer par une source primaire **ou de le retirer**, et F1 n’a fait ni l’un ni l’autre, faute de source primaire. Autrement dit, l’édition rend la phrase **exacte dans son référent**, elle ne rend pas le chiffre **garanti**. Si aucune statistique primaire n’est produite avant publication, le retrait reste disponible : l’emplacement est identifié aux trois mêmes lignes.

---

## 2. Une réparation de forme emportée par la tranche

La l. 19 faisait **76 caractères** là où toute la bordure de l’encadré en fait **75**. Le bord droit de cette ligne dépassait d’une colonne depuis la rédaction initiale. La ligne étant de toute façon modifiée par F1, la largeur a été ramenée à 75 : **les huit lignes du cadre mesurent désormais 75 caractères.**

Ce n’est pas un sixième fait, c’est une réparation de mise en page sur une ligne déjà ouverte, déclarée ici pour qu’aucune modification ne soit portée au crédit d’une tranche qui ne l’aurait pas faite.

---

## 3. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes modifiées | **8**, exactement 3, 9, 11, 19, 20, 67, 101, 113 |
| Lignes ajoutées ou supprimées | **0** (308 avant, 308 après) |
| Chaînes retirées | `rapatriements forcés`, `neuf stations de police`, `Relance de l’information judiciaire`, `commanditaires d’affaires ou d’État`, `3e rang mondial`, `3e exportateur`, `Dépendance cloud 70 %`, `70 % de ses données` : **0 occurrence chacune** |
| Chaînes ajoutées | les neuf formulations d’arrivée : **1 occurrence chacune** |
| Cadre de l’encadré | **8 lignes à 75 caractères** |
| Tiret cadratin | **0** |
| Apostrophes ASCII | **291 → 289** (les deux retirées appartenaient au membre Rokh Solis supprimé) |
| Renvois `[n]` dans le corps | **51**, inchangé |
| Entrées de registre | **64**, inchangé |
| Diff | limité aux huit lignes visées, aucun déplacement |

---

## 4. Ce que F1 ne ferme pas

Rien de tout cela n’est un défaut introduit ou aggravé par F1 : ce sont les points restants de la vérification, inchangés.

1. **Huit nombres non sourçables au dossier** : 4,8 Md$ de South Pars 11 (l. 46), « plus de 40 % d’investisseurs nord‑américains » (l. 55), 67 millions de patients (l. 61), 1 000 emplois et 50 000 € par emploi manquant (l. 108), le membre « intégralité du résultat avant impôt annuel » (l. 38), 57,2 Md€ (l. 9), « sous la pression constante » (l. 61), « des centaines » et « plusieurs centaines » (l. 70, 72). Détail : `VERIFICATION_MASTERWORK_5_FAITS_2026-09-14.md` §6.
2. **La notation `[N]` désignait deux référentiels** : la bibliographie dans le corps et une partie du tableau de synthèse, l’investigation dans trois cellules de ce même tableau ([25], [27], [63]). **F1 ne l’a pas touchée**, pour que la régression reste attribuable : cette réparation a été faite par la tranche **F2** (`SEMANTIC_DIFF_F2_2026-09-14.md`), qui supprime les sept codes d’investigation du corps et des cellules.
3. **29 entrées de registre sur 64 ne servent jamais de source** (compte corrigé en F2, §6 : j’avais écrit 30 en ajoutant [27] à tort), dont [5] [6] [7] qui portent encore leur description d’avant la correction de provenance.
4. **Le défaut de fond, l. 194** : « la souveraineté s’asphyxie dans un système de quatre verrous structurels », « le quatrième verrou ferme la boucle », « le verrouillage cumulatif des quatre dimensions ». Aucune pièce ne mesure une intégration. **Décision d’auteur, non tranchée.** Tant qu’elle ne l’est pas, F1 améliore l’exactitude du texte sans changer son statut probatoire.
5. **La conformité typographique de l’article reste en écart de charte** : 289 apostrophes ASCII contre 10 typographiques. Non traité, parce que la normalisation n’est pas un correctif factuel et qu’elle toucherait tout le fichier.

---

## 5. Renvois

- Vérification et sourçage : `VERIFICATION_MASTERWORK_5_FAITS_2026-09-14.md`.
- Situation de l’objet : `SEMANTIC_DIFF` ci‑présent, et `SUIVI_V4_4_2026-09-13.md` §6.12, qui note que le masterwork est un **objet distinct** de la lignée V4.4 / V4.5 et n’entre donc pas dans `GLOBAL_STATE`, lequel décrit l’autre article.
- Mémoire mobilisée : `7ce6073c-501d-4351-8e11-dafd70d261a0` (rang SIPRI) et `2ba4a5d1-b1d3-4fa5-a0f4-43c9bdd95495` (référent du 70 %).
