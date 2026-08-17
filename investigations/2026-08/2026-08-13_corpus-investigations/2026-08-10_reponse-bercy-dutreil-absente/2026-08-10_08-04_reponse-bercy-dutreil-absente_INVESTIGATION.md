# INVESTIGATION — GAP-003 RÉSOLU : la « réponse de Bercy » au rapport CdC Dutreil n'existe pas — « Destinataire n'ayant pas répondu » (Lecornu)

```
STATE          : FINAL
DATE           : 2026-08-10 08:04 CEST
TYPE           : INVESTIGATION
KERNEL         : v2.8
SUJET          : GAP-003 du dossier 07-46 (BNDP accès exceptionnel) — retéléchargement de la
                 réponse écrite de Bercy (ministre de l'économie) au rapport CdC « Le Pacte
                 Dutreil » (18/11/2025) et vérification de son contenu sur le régime d'accès
                 à la BNDP.
OBJECT_QUESTION : « La réponse du Gouvernement (Lecornu/Bercy) au rapport CdC Dutreil précise-
                 t-elle le régime d'accès à la BNDP ? »
METHODE         : (1) Téléchargement direct du PDF « 20251118-reponse-Pacte Dutreil.pdf »
                 depuis ccomptes.fr (le site répond directement — le 504 précédent était un
                 timeout Wayback) : 254 313 octets, PDF valide, 3 pages, lu intégralement via
                 pdftotext ; (2) vérification Wayback CDX des snapshots alternatifs du même
                 fichier (20251120095126, HTTP 200) pour confirmer qu'il n'existe qu'une
                 version ; (3) grep ciblé (BNDP, patrimoniales, habilitation, secret fiscal,
                 module statistique, DMTG).
CONTEXTE        : Le dossier 07-46 avait documenté l'Annexe n° 4 du rapport CdC Dutreil
                 (communication de la BNDP + habilitation des rapporteurs) et posé le GAP-003 :
                 « la réponse du Gouvernement (Lecornu/Bercy) au rapport CdC (PDF archivé
                 20251118-reponse-Pacte Dutreil.pdf) n'a pas pu être téléchargée (timeout
                 Wayback en session) — elle pourrait contenir des précisions sur l'accès aux
                 données ». Ce dossier exécute le GAP-003 et tranche la question.
```

## 1. LE RÉSULTAT — LA RÉPONSE N'EXISTE PAS

Le PDF officiel « **Réponses des administrations, organismes et personnes concernés** » du rapport « Le Pacte Dutreil » (novembre 2025, 3 pages, **texte intégral extrait = 921 octets**) contient exactement une mention :

> **« Destinataire n'ayant pas répondu : Monsieur le ministre de l'économie, des finances et de la souveraineté industrielle et énergétique »** *(ponctuation normalisée : dans le PDF, les deux lignes se suivent sans deux-points)*

→ **Le ministre de l'économie, des finances et de la souveraineté industrielle et énergétique** (la fonction désignée « Bercy » dans le corpus) **n'a PAS répondu** au rapport de la Cour des comptes. Le fascicule de réponses du rapport Dutreil ne contient **aucune réponse, aucun texte de Bercy** : il se limite à constater que le destinataire principal n'a pas répondu. *(L'identité de la personne physique titulaire du portefeuille au 18/11/2025 n'est pas vérifiée en session — cf. LIMITE 1.)*

**Conséquence directe sur la question posée :** la réponse Bercy ne précise pas le régime d'accès à la BNDP **pour la simple raison qu'elle n'existe pas**. La question se résout par un **constat d'absence documenté à la source primaire** — le silence de Bercy est lui-même un fait, et un fait significatif pour le corpus.

## 2. DÉTAILS DE LA VÉRIFICATION

### 2.1 Le téléchargement (la route qui a fonctionné)

- **Échec Wayback initial** (dossier 07-46) : le snapshot `20251118102524` renvoyait un **504 Gateway Time-out** (nginx) — 562 octets HTML d'erreur. Le problème venait du serveur Wayback, pas du fichier.
- **Route directe ccomptes.fr** (10/08 08:00) : `https://www.ccomptes.fr/sites/default/files/2025-11/20251118-reponse-Pacte%20Dutreil.pdf` → **HTTP 200, 254 313 octets, PDF valide** (version 1.6, 3 pages, creation 10/11/2025, modifié 18/11/2025). Le site de la Cour répond sans blocage.
- **Confirmation CDX** : le fichier possède un snapshot Wayback distinct (20251120095126, HTTP 200) — la version publiée est unique.

### 2.2 Le contenu (grep exhaustif)

Le texte intégral extrait (3 pages, 921 octets) ne contient que : page de garde du rapport, puis la mention du destinataire n'ayant pas répondu. **Aucune occurrence** de : BNDP, base nationale, patrimoniales, habilitation, secret fiscal, secret professionnel, CJF, L. 141, L. 140, module statistique, DMTG, numérisation. **Il n'y a littéralement rien d'autre à lire.**

### 2.3 La précision honnête sur l'identité du destinataire

Le rapport est adressé au **« ministre de l'économie, des finances et de la souveraineté industrielle et énergétique »**. Dans le corpus, ce ministère a été désigné « Bercy/Lecornu ». **Précision forensique** : le titulaire du portefeuille économique au moment du rapport (novembre 2025) est une question d'identité ministérielle **distincte de la désignation du ministère**, et **non vérifiée en session**. Le dossier 07-46 a écrit « Lecornu/Bercy » en raccourci — cette désignation est impropre pour la personne (cf. LIMITE 1) mais correcte pour la fonction. **Ce qui est certain et suffisant pour le fait : le ministère de l'économie, destinataire nommé par la Cour, n'a pas répondu** — quelle que soit la personne physique le dirigeant à cette date.

## 3. CE QUE CE SILENCE CHANGE POUR LE CORPUS

### 3.1 Le faisceau BNDP s'enrichit d'un maillon de silence

Le corpus documente désormais, sur le rapport Dutreil :
1. La CdC a exploité intégralement la BNDP (Annexe 4 — dossier 07-46) ;
2. La BNDP n'est jamais nommée par la commission AN (dossier 07-51) ;
3. **Bercy, destinataire officiel du rapport, n'a pas répondu** (ce dossier).

Le **triple silence sur le sujet le plus documenté du corpus fiscal 2025** : le Sénat 760 nomme la BNDP (p. 14), la CdC la nomme (Annexe 4), la commission AN ne la nomme jamais (07-51), et le ministère qui gère la BNDP ne répond pas au rapport qui la décrit. C'est un **constat d'absence cumulatif**, pas une preuve d'intention — mais la convergence des absences est elle-même un fait du dossier.

### 3.2 La comparaison avec la pratique des réponses de la Cour

La pratique des rapports publics thématiques de la CdC veut que les destinataires reçoivent le rapport pour observations et que leurs réponses soient publiées en annexe. **Le non-réponse du ministère de l'économie est un événement dans cette pratique** — un destinataire sollicité répond habituellement (constat de pratique, non quantifié). Le fait est objectif : pour l'évaluation la plus complète jamais produite sur une niche fiscale de 5,5 Md€, le ministère qui gère la dépense et la base de données est resté silencieux.

### 3.3 Limite d'interprétation (anti-sur-affirmation)

Le silence de Bercy **ne prouve pas** : (a) une volonté de dissimuler le régime d'accès ; (b) un mépris de la Cour ; (c) une position sur la BNDP. Le non-réponse peut avoir des causes banales (agenda, choix de communication). **Le fait documenté est le silence lui-même**, et son absence de contenu sur la BNDP — rien de plus.

## 4. CONTRADICTIONS

| ID | Contradiction | Résolution |
|----|---------------|------------|
| CONTR-001 | Le GAP-003 supposait que la réponse « pourrait contenir des précisions sur l'accès aux données » (07-46) vs le fascicule est vide de toute réponse | **Le fascicule officiel confirme : le destinataire principal (ministre de l'économie) n'a pas répondu** — le GAP se résout par absence, l'hypothèse de contenu est invalidée. |
| CONTR-002 | L'échec Wayback (504) pouvait suggérer que le fichier était indisponible → la route directe ccomptes.fr fonctionne (HTTP 200) | Le fichier est bien publié et téléchargeable ; c'est son contenu qui est minimal (constat de non-réponse). L'absence est de contenu, pas d'accès. |
| CONTR-003 | Désignation « Lecornu/Bercy » dans le corpus (07-46) | La fonction ministérielle (économie/finances) est confirmée par le PDF ; la personne physique titulaire au 18/11/2025 n'est pas vérifiée en session → le fait se formule sur le ministère, pas sur la personne (cf. §2.3). |

## 5. FACT_REGISTRY

| ID | Fait | Valeur | Source | Statut |
|----|------|--------|--------|--------|
| FCT-001 | Le PDF officiel « Réponses des administrations » du rapport Dutreil (18/11/2025) contient **uniquement** la mention « **Destinataire n'ayant pas répondu : Monsieur le ministre de l'économie, des finances et de la souveraineté industrielle et énergétique** » *(ponctuation normalisée)* | 3 pages, 921 octets de texte | PDF ccomptes.fr (254 313 o, lu intégralement via pdftotext), fichier 20251118-reponse-Pacte Dutreil.pdf | CONFIRMÉ (source primaire) |
| FCT-002 | **Aucune occurrence** de BNDP / base nationale / patrimoniales / habilitation / secret fiscal / module statistique / DMTG dans le fascicule de réponses | 0 occurrence | grep sur reponse_dutreil.txt (texte intégral extrait) | CONFIRMÉ (constat d'absence) |
| FCT-003 | Le téléchargement direct depuis ccomptes.fr fonctionne (HTTP 200) — l'échec du dossier 07-46 était un timeout Wayback (504 nginx), pas une indisponibilité du fichier | 200, 254 313 o | curl ccomptes.fr 10/08/2026 | CONFIRMÉ |
| FCT-004 | Le fichier possède un snapshot Wayback alternatif (20251120095126, HTTP 200) — version unique publiée | 1 snapshot 200 | CDX Wayback | CONFIRMÉ |
| FCT-005 | La question « la réponse Bercy précise-t-elle le régime d'accès à la BNDP ? » se résout par **absence** : il n'y a pas de réponse à analyser | non-réponse | FCT-001 + FCT-002 | CONFIRMÉ (conclusion) |
| FCT-006 | Le ministère de l'économie (destinataire nommé par la Cour) est resté silencieux sur un rapport qui documente l'exploitation de sa propre base de données (BNDP) par la CdC | silence | FCT-001 + dossier 07-46 (Annexe 4) | CONFIRMÉ (faisceau) |
| FCT-007 | **Limite** : le silence ne prouve ni dissimulation ni mépris — les causes banales (agenda, choix de communication) ne sont pas exclues ; le fait documenté est le silence lui-même | non tranchable | analyse | CONSTAT BORNÉ |

## 6. LIMITES

1. **Identité du titulaire du portefeuille** : la fonction ministérielle est confirmée par le PDF, mais la personne physique dirigeant le ministère au 18/11/2025 n'a pas été vérifiée en session (le corpus a écrit « Lecornu » par raccourci — cf. §2.3). Le fait ne dépend pas de cette identité.
2. Le fascicule de réponses ne liste qu'**un** destinataire (« le ministre de l'économie ») ; la pratique de la Cour publie parfois plusieurs réponses (autres ministères, organismes) — le rapport Dutreil semble n'en avoir sollicité qu'un seul ou n'en avoir publié qu'un. La procédure exacte de notification n'a pas été vérifiée (combien de destinataires ont reçu le rapport).
3. Le CP de la Cour (20251118-CP-Le-Pacte-Dutreil-Vdéf.pdf, archivé) n'a pas été lu — il ne contiendrait de toute façon pas une réponse de Bercy, mais il pourrait contextualiser la publication.
4. Le dossier 07-46 a désigné le ministère par « Lecornu/Bercy » : cette désignation est impropre pour la personne (cf. LIMITE 1) mais correcte pour la fonction ; corrigée en §2.3.

## 7. GAPS / ACTIONS

| ID | Action | Priorité |
|----|--------|----------|
| GAP-001 | Vérifier l'identité du titulaire du ministère de l'économie au 18/11/2025 (composition du gouvernement en vigueur) pour corriger la désignation « Lecornu » dans le dossier 07-46 si besoin | 3 |
| GAP-002 | Vérifier si d'autres destinataires ont reçu le rapport Dutreil pour observations (procédure de notification de la CdC, réponses multiples éventuelles) | 3 |
| GAP-003 | Lire le CP de la Cour (20251118-CP-Le-Pacte-Dutreil-Vdéf.pdf) pour contextualiser la publication — ne contiendra pas de réponse Bercy mais précise les annonces | 3 |

## 8. LEÇON

**Le GAP-003 se résout par le plus instructif des résultats : l'absence.** La « réponse de Bercy » au rapport le plus complet jamais produit sur le pacte Dutreil **n'existe pas** : le fascicule officiel publié par la Cour des comptes se borne à constater que « le destinataire n'a pas répondu ». Le ministère qui perçoit les droits de mutation, gère la BNDP, chiffre (ou refuse de chiffrer) la dépense fiscale, et ne finance pas le module statistique DMTG 2.0 — ce même ministère n'a pas jugé utile de répondre, par écrit, à une évaluation publique qui documente l'exploitation de sa propre base de données par la Cour. **Le silence est ici une donnée.** Il rejoint le faisceau des absences du corpus : la BNDP que le Sénat nomme (760), que la CdC nomme (Annexe 4), que la commission AN ne nomme jamais (07-51) — et sur laquelle le gestionnaire ne dit rien. Quatre institutions, quatre régimes de parole : l'une la nomme en annexe technique, l'autre en page 14, la troisième jamais, la dernière pas du tout. La convergence de ces silences ne prouve pas une intention ; elle documente un fait : **sur l'un des sujets les plus sensibles du système fiscal français — l'héritage des plus riches — l'administration choisit de ne pas parler, quand elle ne choisit pas de ne pas répondre.**
