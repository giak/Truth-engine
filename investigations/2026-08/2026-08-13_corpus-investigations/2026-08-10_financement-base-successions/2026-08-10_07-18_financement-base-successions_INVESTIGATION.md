# INVESTIGATION — Financement de la base de données successions DGFiP (rec. Sénat 760 n° 6) : la commission Mattei/de Courson ou le PLF 2027 la financent-ils ? Calendrier d'interrogeabilité publique

```
STATE          : FINAL
DATE           : 2026-08-10 07:18 CEST
TYPE           : INVESTIGATION
KERNEL         : v2.8
SUJET          : Base de données successions DGFiP (plateforme e-enregistrement, rec. Sénat 760 n° 6,
                 module statistique non financé) — vérification du financement par la commission
                 Mattei/de Courson (rapport n° 3056) ou le PLF 2027, et calendrier d'interrogeabilité
                 publique
PARENT         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/2026-08-09_23-25_base-donnees-successions-eenregistrement_INVESTIGATION.md
                 (GAP-003b : corps du rapport Sénat 760 non lu ; GAP-004 : perspective DGFiP absente)
                 investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_rec-10-12-plf-2027/2026-08-10_07-12_rec-10-12-plf-2027_INVESTIGATION.md
METHODE        : texte intégral Tome 1 rapport 3056 (ce_t1.txt : rec. n° 7 l. 4545, calendrier CSN
                 3 lots l. 4040-4110, DESF l. 4041-4057, LF 2026 conservation l. 4129) + Tome 2
                 (ce_t2.txt : audition DGFiP p. 206-208, Giannesini, Coquerel) + Google News RSS
                 (financement e-enregistrement = 0 résultat ; réponse gouv Sénat 760 = 0 résultat)
NOMBRE FAITS   : 13 (FCT-001..FCT-013)
GAP_SEVERITY   : 0.15 (question du financement PLF 2027 INDÉTERMINÉE — PLF non déposé)
CONTRADICTIONS : CONTR-001 (CORRIGÉ 07:26 : lot 3 = 2033 au moins Sénat 760 vs 2030 T1-3056 — divergence réelle, source la plus récente retenue ; cf. dossier 07-26), CONTR-002 (rec. 7 « prioriser »
                 vs absence de moyens fléchés dans le rapport 3056), CONTR-003 (module statistique : e-enregistrement vs Pilat — deux entités)
BIAS TEST      : 15 symboles scorés (§0) — PASS
FICHIERS       : /tmp/ce_t1.txt (T1 327 p.), /tmp/ce_t2.txt (T2 751 p.), g5.xml/g6.xml (RSS)
```

## 1. CONTEXTE — pourquoi cette investigation

Le dossier 23-25 a identifié la « base de données en cours de constitution » (Sénat 760, rec. n° 6) comme la **plateforme e-enregistrement de la DGFiP**, avec un **module statistique non financé** (CPO, ✧) et une **interrogeabilité publique : NON**. Restaient deux trous (GAP-003b, GAP-004) et une question nouvelle posée par l'utilisateur : **est-ce que la commission Mattei/de Courson (rapport n° 3056, déposé 08/07/2026, lu intégralement) ou le PLF 2027 la finance, et quel est le calendrier d'interrogeabilité publique ?**

**Verdict d'entrée vérifié** : la commission d'enquête ne dispose d'AUCUN pouvoir de financement (ce n'est pas un organe budgétaire) ; le PLF 2027 n'est pas déposé au 10/08/2026 (dossier 07-12). La question se reformule donc : (1) le rapport 3056 recommande-t-il un financement ? (2) y a-t-il une trace de crédits PLF 2026/2027 pour le module statistique ? (3) quel calendrier réaliste pour que les données soient exploitées et publiées ?

## 2. CE QUE DIT LE RAPPORT 3056 (Tome 1, lu intégralement)

### FCT-001 — Rec. n° 7 du rapport 3056 : PRIORISER, pas financer (l. 4545)
**SOURCE** : ce_t1.txt, l. 4545-4550 (texte intégral)
**TEXTE EXACT** : « Recommandation n° 7 : Prioriser parmi les projets de la DGFiP la numérisation des déclarations de succession et leur centralisation en vue notamment de leur exploitation statistique. »
**LECTURE** : la formulation est une **priorisation interne** (« parmi les projets de la DGFiP »), pas un fléchage de crédits ni un montant. Le rapport 3056 ne comporte **aucun chiffre de financement** pour le module statistique (grep « financement » : aucune occurrence liée à la base ; grep « module statistique » : zéro occurrence dans le T1).

### FCT-002 — Le calendrier CSN des 3 lots (l. 4040-4110)
**SOURCE** : ce_t1.txt, l. 4040-4110 (auditions CSN 28/04/2026, compte-rendu n° 15)
**FAITS** : le CSN décrit le déploiement de la numérisation en **3 lots** :
- **Lot 1** : déclarations de succession **ne générant pas de droits** (« en principe les plus simples ») — « devrait démarrer d'ici la fin de l'année » (fin 2026) ;
- **Lot 2** : « certaines déclarations payantes sans grande complexité » — « d'ici deux ans à deux ans et demi » (2028-2029) ; prérequis techniques en cours depuis mars 2026 ;
- **Lot 3** : cas les plus complexes — « paiements différés ou fractionnés, et assurances vie qui posent une difficulté technique à la DGFIP » — **horizon de déploiement fixé à 2030** (T1-3056, audition CSN 28/04/2026). ⚠️ **MAJ 07:26 (corps Sénat 760 lu, dossier 07-26)** : le rapport Sénat 760 (17/06/2026, source plus récente) dit « serait repoussé à **2033 au moins** » — divergence réelle entre deux sources officielles, lecture retenue 2033 (CONTR-001 corrigé).
**ÉCHÉANCE GLOBALE** : le CSN estime le déploiement complet « pour 2032 au plus tôt » tout en prévenant : « en 2019, nous visions 2027 », il ne peut « garantir que l'échéance de 2032 sera tenue ».

### FCT-003 — L'accélération possible : 2029-2030 « en y mettant les moyens » (l. 4542)
**SOURCE** : ce_t1.txt, l. 4542-4544
**FAITS** : le rapport note : « Un investissement humain et financier supplémentaire permettrait de procéder à l'accélération de ce projet. Le CSN a d'ailleurs admis qu'il était possible d'envisager une échéance plus précoce que 2032 pour l'exploitation des données de succession "en y mettant les moyens" et a évoqué la cible de "2029-2030". » — **C'est le passage qui fait le lien entre la rec. n° 7 et le financement : le rapport constate explicitement que l'accélération dépend d'un investissement, mais ne le vote pas.**

### FCT-004 — La LF 2026 a introduit l'obligation de conservation par les notaires (l. 4129)
**SOURCE** : ce_t1.txt, l. 4129-4130
**FAITS** : « la loi de finances pour 2026 a introduit une obligation de conservation par les notaires de la déclaration de succession » — seule avancée législative liée au chantier ; c'est une exigence de forme (gestion), pas un financement du module statistique.

### FCT-005 — Le projet DESF : l'OCR comme palliatif (l. 4041-4057)
**SOURCE** : ce_t1.txt, l. 4041-4057
**FAITS** : le DESF (département des études et statistiques fiscales de la DGFiP) a un troisième projet : l'exploitation des déclarations de succession « par des méthodes de reconnaissance optique de caractères sur des fichiers PDF numérisés ». La DGFiP reçoit « 300 000 actes par an depuis 2018 ». Le rapport note que ce projet DESF « semble en effet être un **palliatif** à la lenteur du projet pourtant essentiel de numérisation des déclarations de succession » (transmission notariale encore en format papier). La complexité croît « plus que proportionnellement avec les montants de patrimoine transmis » — les successions à forts enjeux sont « les plus singuliers et les plus difficiles à traiter par des méthodes algorithmiques ».

## 3. CE QUE DIT LE TOME 2 (audition CPO/Cour des comptes du 14/04/2026, p. 195-208) — la pièce la plus lourde (FCT-006 à FCT-008)

⚠️ **CORRECTION D'ATTRIBUTION (revue 10/08/2026)** : le passage p. 195-208 n'est PAS l'audition DGFiP (15/04, p. 239-266, représentants Créange/Pomeranc/Touvenin/Fabre/Perraud/Fénelon) mais l'audition n° 11 « du Conseil des prélèvements obligatoires et de la Cour des comptes (14 avril 2026) » (TDM T2 l. 101-102). Intervenants : **Patrick Lefas (vice-président du CPO)**, **Guilhem Blondy (secrétaire général du CPO)**, **Alexandre Jehan (conseiller référendaire à la CdC)**, **Emmanuel Giannesini (président de section à la première chambre de la Cour des comptes, l. 9221)**. Les constats sur la DGFiP y sont donc des constats EXTERNES (CPO/CdC), pas des aveux de la DGFiP elle-même.

### FCT-006 — La DGFiP n'a PAS de « bibliothèque des pactes Dutreil » (p. 208)
**SOURCE** : ce_t2.txt, audition CPO/CdC du 14/04/2026, Giannesini (président de section, 1re chambre CdC), p. 208
**CITATION VERBATIM** : « l'administration fiscale ne possédait pas de bibliothèque des pactes Dutreil ; ils ne sont pas numérisés sous des formats types ni conservés en routine, et ne sont donc découverts que lorsqu'on les fait jouer, c'est-à-dire au moment où l'on demande le bénéfice de l'avantage fiscal lié à la transmission. »
**PRÉCISION** : c'est la Cour des comptes qui le constate à partir de ses travaux sur la fraude fiscale (rapport « La lutte contre la fraude fiscale », décembre 2025, cité en ouverture de l'audition) — pas une déclaration directe de la DGFiP. **PORTÉE** : au-delà du module statistique, la DGFiP **n'a même pas une base de travail sur les pactes Dutreil** — la rec. Sénat 760 n° 6 (mention notariale) part donc d'un trou de données antérieur, non documenté par le dossier 23-25. La mention notariale devra créer ex nihilo une traçabilité qui n'existe pas en routine.

### FCT-007 — Le « manque de données » : Coquerel interroge la cause (p. 207-208)
**SOURCE** : ce_t2.txt, audition CPO/CdC du 14/04/2026
**CITATION VERBATIM** (Coquerel) : « ce manque de données tient-il au fait que, depuis des années, il n'y a pas eu de donneurs d'ordres pour les chercher ou à une extrême complexité de la tâche ? » — Réponse de Giannesini (CdC) : « depuis la fin de l'impôt de solidarité sur la fortune (ISF), il n'y a plus de données consolidées sur le patrimoine des contribuables. À ma connaissance, il n'existe pas de fichier qui permette de récapituler et de croiser de façon relativement simple l'ensemble du patrimoine et des revenus d'un contribuable. »
**LECTURE** : la suppression de l'ISF (2017) a éteint la seule source consolidée ; rien n'a été reconstruit depuis (cohérent avec la DMTG 2010 du dossier 23-25).

### FCT-008 — L'architecture statistique DGFiP : Iliad et Pilat (p. 207)
**SOURCE** : ce_t2.txt, audition CPO/CdC du 14/04/2026, Giannesini (CdC)
**FAITS** : le système d'information statistique de la DGFiP s'appelle **Iliad** (extraction de données à des fins statistiques) ; le projet **Pilat** vise à unifier les applications de contrôle fiscal ; « on peut imaginer qu'avec Pilat le module statistique fonctionnera et sera capable de croiser les résultats des contrôles fiscaux et la catégorisation des contribuables » (Giannesini).
**⚠️ RÉSERVE (CONTR-003)** : le « module statistique » dont parle Giannesini (T2) répond à la question de de Courson sur les **contrôles fiscaux** (ESFP, pénalités, encaissements) ; la rec. Sénat 760 n° 3 vise le **module statistique de la plateforme e-enregistrement** (données de succession). ✧ **Deux entités plausibles mais non prouvées identiques — l'équation « module = brique de Pilat » est une inférence analytique, pas un fait établi.**

## 4. LE FINANCEMENT : VÉRIFICATION DU PLF 2027 ET DU SÉNAT 760 (FCT-009 à FCT-011)

### FCT-013 — Le projet « IA Enregistrement » : l'opportunité citée par le CPO, avec garde-fou statistique (p. 208-209)
**SOURCE** : ce_t2.txt, audition CPO/CdC du 14/04/2026 — Blondy (secrétaire général du CPO), p. 208-209
**FAITS** : (1) de Courson observe que la reconstitution du patrimoine par les successions est techniquement possible (« quand on connaît le flux des entrées et sorties, on peut évaluer un stock ») et que les données « seront, d'après ce qui nous a été dit, numérisées dans un fichier d'ici deux ans » (cohérent avec le lot 2 du CSN, 2028-2029) ; (2) Blondy confirme : la succession/donation est « le moment où la photo pourrait être la plus complète » (assiette complète incluant les biens professionnels, malgré les régimes dérogatoires) ; (3) **le projet s'appelle « IA Enregistrement »** (« On espère donc beaucoup du projet IA Enregistrement ») ; (4) **garde-fou** : « cette fonction statistique doit être embarquée dès l'origine dans le projet. En effet, de nombreux projets de la DGFIP sont orientés... vers la gestion et le contrôle, mais pas forcément vers la conception de la politique fiscale ou le traitement statistique » — le CPO tire la leçon des projets précédents (cohérent avec le recentrage Moorea→Fidji du 23-25) ; (5) Mattei (président) : « L'administration est donc informée et je suis donc un peu étonné qu'elle ne dispose pas de ces renseignements » (sur l'enregistrement des pactes Dutreil). ✧ « IA Enregistrement » n'apparaît que dans le T2 (2 occurrences) — nom exact du projet non confirmé par le T1 ni par la DGFiP.

### FCT-009 — PLF 2027 : non déposé, aucun crédit visible (constat d'absence)
**SOURCE** : état de l'art au 10/08/2026 + dossier 07-12 (rec. 10/12) + Google News RSS
**FAITS** : le PLF 2027 n'est pas déposé (dépôt octobre 2026). La recherche RSS « e-enregistrement successions financement module statistique » = **zéro résultat** ; aucune trace publique de crédits dédiés à la numérisation successorale ou au module statistique dans la préparation du budget 2027 (chasse aux niches, Figaro 16/07 — cf. dossier 07-12). La réponse écrite du gouvernement au rapport 3056 n'est pas publiée (échéance ~08/09/2026, dossier 07-12 FCT-007).

### FCT-010 — La réponse du gouvernement au Sénat 760 n'existe pas à date
**SOURCE** : RSS Google News « réponse du gouvernement hauts patrimoines Sénat 760 » = 0 résultat ; dossier 23-40 (« réponse Sénat 760 absente, report au PLF 2027 »)
**FAITS** : la rec. Sénat 760 n° 3 demandait de « rendre rapidement opérationnel le module statistique de la plateforme e-enregistrement, le cas échéant par le déploiement de moyens humains ou financiers supplémentaires ». **Aucune réponse gouvernementale publiée** au 10/08/2026. La rec. n° 2 demandait de « redéployer des effectifs au sein des ministères économiques et financiers pour étoffer les moyens du DESF » — sans réponse non plus.

### FCT-011 — Aucun montant de financement public nulle part
**SOURCE** : T1 (grep), T2 (grep), Sénat 760 (23-25), RSS
**FAITS** : le montant exact du financement manquant n'est pas public (23-25 : « dizaines de millions d'euros », CPO, ✧). Le rapport 3056 ne chiffre aucun coût de la numérisation. La seule donnée économique publiée : le coût notarial — « plusieurs milliers d'heures de la part du notariat » depuis 2019 (T1, FCT-002).

## 5. SYNTHÈSE — VERDICT (FCT-012)

**Question 1 : la commission Mattei/de Courson finance-t-elle la base ?**
**NON — et c'est structurel.** Une commission d'enquête n'a pas de pouvoir budgétaire. Le rapport 3056 fait deux choses : (a) la rec. n° 7 demande à la DGFiP de **prioriser** la numérisation « parmi ses projets » (réallocation interne, pas d'argent neuf) ; (b) il constate explicitement que l'accélération « en y mettant les moyens » vers 2029-2030 est possible (FCT-003) mais ne flèche aucune ligne. La rec. n° 12 (taxation du flux successoral) est conditionnée à la base — elle crée une dépendance, pas un financement.

**Question 2 : le PLF 2027 la finance-t-il ?**
**INDÉTERMINÉ à la date du 10/08/2026.** Le PLF 2027 n'est pas déposé. La réponse du gouvernement au Sénat 760 (qui demandait le financement) est inexistante à date ; la réponse au rapport 3056 n'est pas publiée. Point de contrôle : après dépôt du PLF 2027 (octobre 2026), rechercher dans le bleu budgétaire « Gestion fiscale » / programme 156 les crédits de la numérisation successorale et du projet Pilat. **Le scénario documenté au dossier 23-40 (réponse Sénat 760 « reportée au PLF 2027 ») ne s'est pas concrétisé par un texte à ce jour.**

**Question 3 : quel calendrier d'interrogeabilité publique ?**
**Structurellement limité, et certainement pas nominatif.** Le calendrier CSN (FCT-002) : lot 1 fin 2026, lot 2 2028-2029, lot 3 (assurances vie) **2033 au moins** (Sénat 760, source la plus récente — CONTR-001 corrigé 07:26), complet « 2032 au plus tôt » (T1), accélération possible 2029-2030 « en y mettant les moyens ». La DGFiP a par ailleurs annoncé une diffusion de micro-données « avant 2028 » (Sénat 760 p. 14, FCT-005 du 07-26). Même à cette échéance, deux verrous demeurent : (a) **l'interrogeabilité publique n'est prévue par AUCUN texte** — la rec. Sénat 760 n° 1 prévoit une diffusion **statistique agrégée** par le service statistique public, jamais nominative (secret fiscal) ; (b) la rec. n° 6 (mention Dutreil) part d'un trou documenté par le Tome 2 : la DGFiP n'a pas même de bibliothèque des pactes Dutreil (FCT-006). L'horizon réaliste d'une connaissance publique exploitable sur les successions est **2029-2033, et uniquement sous forme agrégée**.

## 6. FACT_REGISTRY

| ID | Fait | Source | Statut |
|----|------|--------|--------|
| FCT-001 | Rec. n° 7 du rapport 3056 : « Prioriser parmi les projets de la DGFiP la numérisation des déclarations de succession et leur centralisation en vue notamment de leur exploitation statistique » — priorisation, PAS de fléchage de crédits | ce_t1.txt l. 4545 | CONFIRMÉ (T1 lu intégralement) |
| FCT-002 | Calendrier CSN des 3 lots : lot 1 (sans droits) fin 2026 ; lot 2 (payantes simples) 2028-2029 ; lot 3 (différés/fractionnés + assurances vie) horizon 2030 (T1) MAIS « repoussé à 2033 au moins » (Sénat 760, 17/06 — source plus récente, CONTR-001 corrigé 07:26) ; complet « 2032 au plus tôt », « en 2019 nous visions 2027 » | ce_t1.txt l. 4040-4110 + jina_760e.txt | CONFIRMÉ (T1 lu + Sénat 760 lu) |
| FCT-003 | Accélération possible 2029-2030 « en y mettant les moyens » (CSN) — le rapport constate la dépendance à un investissement sans le voter | ce_t1.txt l. 4542 | CONFIRMÉ (T1 lu intégralement) |
| FCT-004 | LF 2026 : obligation de conservation de la déclaration de succession par les notaires (avancée de forme, pas de financement) | ce_t1.txt l. 4129 | CONFIRMÉ (T1 lu intégralement) |
| FCT-005 | Projet DESF : OCR sur PDF = « palliatif » à la lenteur de la numérisation ; 300 000 actes/an depuis 2018 ; complexité croissante avec les montants transmis | ce_t1.txt l. 4041-4057 | CONFIRMÉ (T1 lu intégralement) |
| FCT-006 | DGFiP : pas de « bibliothèque des pactes Dutreil », non numérisés, découverts seulement quand on les fait jouer (verbatim Giannesini, CdC) — constat EXTERNE (CPO/CdC), pas un aveu DGFiP | ce_t2.txt p. 208 (audition CPO/CdC 14/04) | CONFIRMÉ (T2 lu) |
| FCT-007 | Coquerel : « pas de donneurs d'ordres » ? ; Giannesini (CdC) : plus de données consolidées sur le patrimoine depuis la fin de l'ISF | ce_t2.txt p. 207-208 | CONFIRMÉ (T2 lu) |
| FCT-008 | Architecture statistique DGFiP : Iliad (extraction statistique) ; projet Pilat (unification contrôle) ; ✧ équation « module statistique = brique de Pilat » = inférence (deux entités plausibles, lien non établi, CONTR-003) | ce_t2.txt p. 207 | CONFIRMÉ (fait Iliad/Pilat) + ✧ (équation) |
| FCT-009 | PLF 2027 non déposé ; aucun crédit visible pour la numérisation successorale/module statistique (RSS = 0 résultat) | RSS + 07-12 | CONFIRMÉ (constat d'absence) |
| FCT-010 | Réponse du gouvernement au Sénat 760 (rec. n° 2/3 : moyens humains/financiers pour le module) : INEXISTANTE à date ; LF 2026 : aucun crédit module identifié (réforme a minima, 23-40) | RSS + 23-40 + 23-40 | CONFIRMÉ (constat d'absence) |
| FCT-011 | Aucun montant de financement public : rapport 3056 ne chiffre rien ; seul coût documenté = « plusieurs milliers d'heures » notariales (CSN) | T1 + 23-25 | CONFIRMÉ (constat) |
| FCT-012 | VERDICT : commission ne peut pas financer (pas de pouvoir budgétaire) ; PLF 2027 indéterminé ; interrogeabilité publique = agrégée au mieux, horizon 2029-2033 (lot 3 = 2033 au moins, Sénat 760), jamais nominative | Synthèse | RÉSOLU EN ÉTAT ZÉRO |
| FCT-013 | Projet « IA Enregistrement » (Blondy, CPO, ✧ 2 occurrences T2 seulement) : la succession = « moment où la photo pourrait être la plus complète » ; garde-fou « la fonction statistique doit être embarquée dès l'origine » (leçon Moorea→Fidji) ; Mattei « un peu étonné » que l'administration ne dispose pas des données Dutreil ; de Courson : reconstitution du patrimoine possible, numérisation « d'ici deux ans » | ce_t2.txt p. 208-209 | CONFIRMÉ (T2 lu) + ✧ (nom exact du projet) |

## 7. CONTRADICTIONS

| ID | Fait A | Fait B | Résolution |
|----|--------|--------|-----------|
| CONTR-001 (CORRIGÉ 10/08/2026 07:26) | Lot 3 (assurances vie) : « horizon de déploiement fixé à 2030 » (T1-3056, audition CSN 28/04/2026) | Lot 3 : « repoussé à 2033 au moins » (Sénat 760, 17/06/2026 — lu intégralement, dossier 2026-08-10_07-26_resolution-gap003b-senat760-corps) | ⚠️ **Divergence réelle entre deux sources officielles, PAS une élimination** : le Sénat 760 (postérieur, actualisé après la réponse ministérielle de mars 2026) dit « 2033 au moins ». Lecture retenue : **2033 au moins**. La résolution antérieure « au profit du T1 » était une erreur — corrigée par la lecture du corps du Sénat 760 (FCT-009 du dossier 07-26) |
| CONTR-002 | Rec. n° 7 « prioriser » (apparence de réponse) | Aucun moyen fléché dans le rapport 3056 | La priorisation interne n'est pas un financement ; le rapport le reconnaît lui-même (« un investissement... supplémentaire permettrait » — conditionnel). DOCUMENTÉE |
| CONTR-003 | « Module statistique » du T2 (Giannesini, réponse à de Courson sur les contrôles ESFP) | « Module statistique de la plateforme e-enregistrement » (Sénat 760 rec. n° 3, données de succession) | ✧ Deux entités plausibles mais non prouvées identiques — l'équation est une inférence analytique (FCT-008). DOCUMENTÉE |

## 8. LIMITES DÉCLARÉES

0. **Correction d'attribution appliquée (revue 10/08/2026)** : les passages p. 195-208 du T2 proviennent de l'audition CPO/CdC du 14/04/2026 (Giannesini = président de section 1re chambre CdC ; Lefas = vice-président CPO ; Blondy = secrétaire général CPO), PAS de l'audition DGFiP du 15/04 (p. 239-266, Créange et al.) — les constats FCT-006/007/008 sont des constats EXTERNES.
1. Le PLF 2027 n'existant pas, le verdict de financement est un état zéro à actualiser après octobre 2026 (recherche dans le bleu budgétaire programme 156 « Gestion fiscale » et le document Pilat).
2. Le montant exact du financement manquant du module statistique n'est pas public (« dizaines de millions d'euros », CPO via 23-25, ✧ non relu dans le corps du Sénat 760 — GAP-003b du 23-25 reste ouvert).
3. Les données sur le budget du projet Pilat (coût, calendrier) ne sont pas publiées à date.
4. La réponse du gouvernement aux deux rapports (Sénat 760, AN 3056) doit être re-vérifiée après le 08/09/2026.
5. Le corps du rapport Sénat 760 (pages 10-15 : chapitre e-enregistrement, citations CPO) n'a toujours pas été lu intégralement — les citations CPO du 23-25 restent ✧.

## 9. LEÇON POUR LE CORPUS

La chaîne de la connaissance successorale est verrouillée à trois étages : (1) **pas de bibliothèque des pactes Dutreil** (Tome 2, constat CPO/CdC, FCT-006) — le trou est en amont de la base elle-même ; (2) **le module statistique n'est pas financé** (rec. Sénat 760 n° 2/3, sans réponse gouvernementale) ; (3) **la commission d'enquête, dernier levier institutionnel, n'a pas de pouvoir budgétaire** — elle ne peut que recommander la priorisation (rec. n° 7). La boucle se referme : chaque institution (Sénat, commission AN, CdC, CPO) constate l'opacité et la recommande à la suivante, sans que personne ne vote l'argent qui la lèverait. Le seul garde-fou émergent : le CPO exige que la « fonction statistique soit embarquée dès l'origine » dans le projet IA Enregistrement (FCT-013) — une exigence de conception, pas un financement. La date de 2032 (« au plus tôt », CSN) n'est pas une échéance technique neutre : le rapport 3056 démontre qu'elle peut être ramenée à 2029-2030 « en y mettant les moyens » — les moyens n'étant mis par personne.

## 10. RÉFÉRENCES COMPLÈTES

- Tome 1 rapport n° 3056 : assemblee-nationale.fr/dyn/17/rapports/cepat/l17b3056_rapport-enquete.pdf (327 p., texte /tmp/ce_t1.txt — rec. n° 7 l. 4545 ; calendrier CSN l. 4040-4110 ; DESF l. 4041-4057 ; LF 2026 l. 4129)
- Tome 2 rapport n° 3056 (auditions) : texte /tmp/ce_t2.txt — audition DGFiP p. 206-208 (Giannesini, Coquerel, Lefas)
- Sénat 760 (17/06/2026) rec. n° 1-6 : senat.fr/rap/r25-760/r25-7601.html (lu intégralement, dossier 23-25)
- Dossier parent 23-25 : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/2026-08-09_23-25_base-donnees-successions-eenregistrement_INVESTIGATION.md
- Google News RSS (g5.xml, g6.xml) : financement e-enregistrement = 0 résultat ; réponse gouv Sénat 760 = 0 résultat
