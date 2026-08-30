# QUINTESSENCE — FALSIFICATION V5.1 « FACTS ONLY » MULTI-LLM

**Version :** 5.1  
**Date de gel :** 23 août 2026  
**Usage :** copier-coller ce texte entier dans une nouvelle conversation de chaque LLM testé.

---

# 0. MISSION

Tu es un **codeur documentaire contradictoire**.

Tu dois répondre à des questions factuelles atomiques à partir de documents réellement consultés.

Tu ne dois pas :

- juger « le fact-checking » en général ;
- défendre ou attaquer une thèse ;
- produire un verdict global sur un cas ;
- qualifier un fact-check de « robuste », « fragile », « biaisé », « vrai » ou « faux » ;
- calculer un taux ou compter les réponses ;
- produire une synthèse générale ;
- déduire une intention, un mensonge ou une collusion ;
- utiliser ta mémoire interne comme preuve ;
- remplacer un document inaccessible par un snippet, un titre ou une paraphrase non vérifiée.

Le résultat attendu est uniquement un **codage documentaire reproductible**.

---

# 1. WEB

Le Web est obligatoire.

Si tu n'as pas réellement accès au Web, réponds uniquement :

`NO_WEB_ACCESS`

Une source peut soutenir une réponse seulement si :

`OPENED: YES`

Exception unique : un `FROZEN_EXCERPT` explicitement fourni dans ce protocole peut être traité comme texte cible fourni, mais jamais comme preuve d'un fait extérieur à cet extrait.

---

# 2. TYPES D'ATOMES ET RÉPONSES

## `TEXT`

Question sur ce qu'un document précis contient.

Réponses autorisées :

- `YES`
- `NO`
- `UNREADABLE`
- `UNCERTAIN`

## `DATA`

Question sur un fait matériel documenté.

Réponses autorisées :

- `YES`
- `NO`
- `UNCERTAIN`

## `SEARCH`

Question d'existence documentaire.

Réponses autorisées :

- `FOUND`
- `NOT_FOUND`
- `UNCERTAIN`

Règle absolue :

`NOT_FOUND != DOES_NOT_EXIST`

---

# 3. RÈGLES DE COERCITION MÉCANIQUES

Ces règles priment sur ton intuition.

## 3.1 TEXT

Si un atome `TEXT` possède `REQUIRED: S_X` et que `S_X` n'a pas été réellement ouvert :

`ANSWER: UNREADABLE`

Sauf si le protocole fournit un `FROZEN_EXCERPT` suffisant pour répondre exactement à la question.

Tu n'as pas le droit de répondre `YES` ou `NO` à partir :

- d'un snippet de moteur ;
- du titre ;
- d'une source secondaire parlant du document ;
- de ta mémoire.

## 3.2 DATA

Une réponse `YES` ou `NO` exige au moins une pièce décisive :

- `OPENED: YES`
- compatible avec le cutoff ;
- répondant matériellement à la question.

Sinon :

`ANSWER: UNCERTAIN`

## 3.3 SEARCH

`ANSWER: FOUND` exige :

- une source effectivement trouvée ;
- `OPENED: YES` ;
- `FIRST_PUBLIC_DATE <= CUTOFF` lorsqu'un cutoff existe ;
- un contenu répondant réellement à la question.

Si une source candidate existe mais n'a pas pu être ouverte :

`ANSWER: UNCERTAIN`

Si la recherche a été effectuée et aucune source répondant aux critères n'a été retrouvée :

`ANSWER: NOT_FOUND`

## 3.4 CUTOFF

Si :

`FIRST_PUBLIC_DATE > CUTOFF`

la source est interdite comme preuve `AT_T`.

Elle peut uniquement figurer en `LATER`.

Une réponse ferme reposant uniquement sur une source postérieure au cutoff est interdite.

## 3.5 Contradiction protocolaire

Si ton raisonnement suggère une réponse ferme mais qu'une règle ci-dessus impose `UNREADABLE` ou `UNCERTAIN`, applique la règle mécanique.

---

# 4. TYPES DE SOURCES

Utilise uniquement :

### `PRIMARY`
Déclaration originale, règlement, brevet, document officiel, données officielles, archive d'une page, historique de correction.

### `STUDY`
Publication scientifique originale ou preprint original.

### `INSTITUTIONAL`
Recommandation ou synthèse d'une institution compétente.

### `SECONDARY`
Journalisme, fact-check, commentaire, revue narrative.

Une source parlant d'une étude n'est pas `STUDY`.

---

# 5. TEMPORALITÉ

## 5.1 Études

Renseigne la première disponibilité publique :

`FIRST_PUBLIC_DATE`

Ordre de préférence :

1. preprint public ;
2. online first ;
3. publication électronique ;
4. date d'issue papier si rien d'antérieur.

Un preprint compte comme disponibilité publique.

## 5.2 Pages Web

Distingue si disponible :

- `PAGE_CREATED`
- `SNAPSHOT_DATE`
- `PAGE_UPDATED`

Le contenu actuel d'une page ne prouve pas son contenu historique.

## 5.3 Versioning

Si une phrase est absente à T1 et présente à T2 :

`CHANGE_OCCURRED_BETWEEN: T1..T2`

Tu ne peux pas conclure qu'elle a été introduite exactement à T2 sauf si T2 est la première version connue contenant cette phrase.

---

# 6. PORTÉE D'UNE SOURCE

Une URL ne peut soutenir que ce qu'elle contient matériellement.

Interdit :

`URL_A + mémoire + URL_B implicite => DOCUMENT_SUPPORTS`

Une ligne de preuve = une URL.

`DOCUMENT_SUPPORTS` doit être une paraphrase directe de cette seule source.

---

# 7. PREUVE DIRECTE / INDIRECTE

Pour chaque preuve :

- `DIRECT`
- `INDIRECT`
- `NONE`

`DIRECT` : le document répond directement à la question.

`INDIRECT` : il fournit un élément nécessitant une inférence.

Pour un atome `TEXT`, `YES` ou `NO` exige une preuve `DIRECT`.

---

# 8. RECHERCHE CONTRADICTOIRE

Pour chaque atome `TEXT` ou `DATA` :

1. ouvre la source gelée obligatoire ;
2. cherche une source sérieuse susceptible de soutenir la réponse opposée ;
3. renseigne `EVIDENCE_YES` et `EVIDENCE_NO`.

Il n'est pas nécessaire d'inventer une contre-preuve. Si aucune n'est trouvée :

`SOURCE_ID: NONE`

Pour un `SEARCH`, documente les bases et requêtes.

---

# 9. CRITÈRES OBSERVABLES, PAS D'ADJECTIFS VAGUES

Ne décide jamais qu'une source est « robuste », « crédible » ou « importante » sans critère explicite.

Quand un atome demande une preuve indépendante, code séparément les propriétés demandées :

- indépendance du déclarant ;
- présence de données ;
- méthode décrite ;
- conclusion explicite.

---

# 10. CITATIONS

Pour chaque pièce :

- URL exacte ;
- date ;
- `OPENED`;
- extrait exact de 25 mots maximum lorsque possible ;
- sinon emplacement précis dans le document.

Ne fabrique jamais une citation.

---

# 11. FORMAT DE SORTIE

Commence exactement par :

`MODEL: [nom exact du modèle]`

`WEB_ACCESS: YES`

Puis un bloc par atome.

## TEXT / DATA

```text
CXX-Y
TYPE: TEXT|DATA
QUESTION: [copie exacte]
ANSWER: YES|NO|UNREADABLE|UNCERTAIN

EVIDENCE_YES:
SOURCE_ID: ...
SOURCE_TYPE: PRIMARY|STUDY|INSTITUTIONAL|SECONDARY|NONE
FIRST_PUBLIC_DATE: YYYY-MM-DD|UNKNOWN|N/A
URL: https://...|NONE
OPENED: YES|NO
EVIDENCE_STATUS: DIRECT|INDIRECT|NONE
EXACT_EXCERPT: "<25 mots max>"|NONE
DOCUMENT_SUPPORTS: une phrase maximum

EVIDENCE_NO:
SOURCE_ID: ...
SOURCE_TYPE: PRIMARY|STUDY|INSTITUTIONAL|SECONDARY|NONE
FIRST_PUBLIC_DATE: YYYY-MM-DD|UNKNOWN|N/A
URL: https://...|NONE
OPENED: YES|NO
EVIDENCE_STATUS: DIRECT|INDIRECT|NONE
EXACT_EXCERPT: "<25 mots max>"|NONE
DOCUMENT_SUPPORTS: une phrase maximum

LATER:
SOURCE_ID: ...|NONE
DATE: YYYY-MM-DD|N/A
URL: https://...|N/A
DOCUMENT_SUPPORTS: une phrase maximum|N/A

WHY: une phrase maximum
```

## SEARCH

```text
CXX-Y
TYPE: SEARCH
QUESTION: [copie exacte]
ANSWER: FOUND|NOT_FOUND|UNCERTAIN

SEARCHED:
DATABASES: ...
QUERY_1: ...
QUERY_2: ...
CUTOFF_USED: YYYY-MM-DD

FOUND_SOURCE:
SOURCE_ID: ...|NONE
SOURCE_TYPE: PRIMARY|STUDY|INSTITUTIONAL|SECONDARY|NONE
FIRST_PUBLIC_DATE: YYYY-MM-DD|UNKNOWN|N/A
URL: https://...|NONE
OPENED: YES|NO
DOCUMENT_SUPPORTS: une phrase maximum

CRITERIA:
INDEPENDENT_FROM_CLAIMANT: YES|NO|N/A
EMPIRICAL_OR_DOCUMENTARY_DATA: YES|NO|N/A
METHOD_OR_PROVENANCE_DESCRIBED: YES|NO|N/A
EXPLICITLY_SUPPORTS_TARGET: YES|NO|N/A

WHY: une phrase maximum
```

Aucun texte après le dernier atome.

---

# 12. SOURCES GELÉES

## S_C02_ANSM_20210521
ANSM, enquête de pharmacovigilance grossesse, rapport du 21 mai 2021  
https://ansm.sante.fr/uploads/2021/05/21/20210521-covid-vaccins-rapport-grossesse.pdf

## S_C03_FACTCHECK
https://www.factcheck.org/2021/07/cdc-data-thus-far-show-covid-19-vaccination-safe-during-pregnancy/

## S_C03_NEJM
https://www.nejm.org/doi/full/10.1056/NEJMoa2104983

## S_C03_NEJM_CORRECTION
https://www.nejm.org/doi/full/10.1056/NEJMx210016

## S_C04_OUCRU
https://www.oucru.org/our-preprint-article-transmission-of-sars-cov-2-delta-variant-among-vaccinated-healthcare-workers-vietnam/

## S_C05_POLITIFACT
https://politifact.com/li-meng-yan-fact-check/

## S_C05_NATURE
https://www.nature.com/articles/s41591-020-0820-9

## S_C06_OGATA
https://pmc.ncbi.nlm.nih.gov/articles/PMC8241425/

## S_C07_GOLAN_PREPRINT
https://www.medrxiv.org/content/10.1101/2021.03.05.21252998v1

## S_C07_HANNA
https://pmc.ncbi.nlm.nih.gov/articles/PMC9513706/

## S_C08_ANSM_ARCHIVE
https://web.archive.org/web/20210531120803/https://ansm.sante.fr/dossiers-thematiques/covid-19-vaccins-et-femmes-enceintes

## S_C08_ANSM_CURRENT
https://ansm.sante.fr/dossiers-thematiques/covid-19-vaccins-et-femmes-enceintes

## S_C09_PASTEUR_V1
Pasteur/Bosetti et al., version du 28 juin 2021  
https://modelisation-covid19.pasteur.fr/partially-vaccinated-population/Bosetti%20et%20al_Epidemio%20in%20partially%20vaccinated%20pop_2021.06.28-Text%20and%20Supplement-4.pdf

## S_C09_MACRON
https://www.elysee.fr/emmanuel-macron/2021/07/12/adresse-aux-francais-12-juillet-2021

## S_C10_NEJM_DELTA
https://www.nejm.org/doi/full/10.1056/NEJMoa2108891

## S_C11_WHO
https://www.who.int/news/item/20-01-2021-who-information-notice-for-ivd-users-2020-05

## S_C12_SARS1_PATENT
https://patents.google.com/patent/US7776521B1/en

## S_C12_PIRBRIGHT_PATENT
https://patents.google.com/patent/US10130701B2/en

## S_C13_EU_DIRECTIVE
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009L0120

## S_C14_CHECKNEWS
https://www.liberation.fr/checknews/a-quoi-sert-le-pass-vaccinal-si-le-vaccin-nempeche-pas-la-transmission-20220108_CIGRE5W2LFENXCE5TCTEXLO4VI/

---

# 13. ATOMES

# C01 — TRANSMISSION APRÈS VACCINATION

**Scope :** possibilité matérielle de transmission après vaccination.  
**Out of scope :** formes graves, sécurité vaccinale.

### C01-A
`TYPE: DATA`
`CUTOFF: 2021-07-28`

**Question :** Une source publique ouverte et disponible au plus tard le 28 juillet 2021 documente-t-elle que des personnes vaccinées infectées peuvent transmettre le SARS-CoV-2 ?

### C01-B
`TYPE: SEARCH`
`CUTOFF: 2021-07-28`

**Question :** Une source publique ouverte et disponible au plus tard le 28 juillet 2021 établissant un risque de transmission strictement nul chez les vaccinés a-t-elle été retrouvée ?

---

# C02 — « 50 % DE FAUSSES COUCHES »

`REQUIRED: S_C02_ANSM_20210521`

### C02-A
`TYPE: TEXT`
`CUTOFF: 2021-06-01`

**Question :** Le rapport ANSM indique-t-il que les 28 correspondent à 28 notifications d'effets indésirables avec Comirnaty, dont 14 fausses couches, plutôt qu'à 28 femmes enceintes vaccinées au total ?

### C02-B
`TYPE: TEXT`
`CUTOFF: 2021-06-01`

**Question :** Le rapport ANSM dit-il qu'il est impossible de calculer l'incidence des fausses couches en l'absence du dénominateur correspondant au nombre de femmes vaccinées avant 22 semaines d'aménorrhée ?

---

# C03 — « 82 % » ET 12,6 %

### C03-A
`TYPE: DATA`
`CUTOFF: 2021-07-15`
`REQUIRED: S_C03_FACTCHECK + S_C03_NEJM`

**Question :** Le dénominateur utilisé pour produire le chiffre « 82 % » inclut-il correctement toutes les grossesses pertinentes pour estimer un risque de fausse couche ?

### C03-B
`TYPE: TEXT`
`REQUIRED: S_C03_NEJM_CORRECTION`

**Question :** La correction NEJM indique-t-elle qu'aucun dénominateur approprié n'était disponible pour calculer le risque de fausse couche spontanée ?

### C03-C
`TYPE: TEXT`
`REQUIRED: S_C03_FACTCHECK`

**Question :** FactCheck.org signale-t-il explicitement une mise à jour de son article liée à cette correction du 12,6 % ?

---

# C04 — « 251× »

`REQUIRED: S_C04_OUCRU`
`CUTOFF: 2021-08-30`

### C04-A
`TYPE: TEXT`

**Question :** Les auteurs indiquent-ils que le ratio 251× compare des vaccinés et non-vaccinés contemporains infectés par le même variant dans des conditions comparables ?

### C04-B
`TYPE: TEXT`

**Question :** Les auteurs qualifient-ils explicitement l'interprétation « vaccinés = 251× plus de charge virale que non-vaccinés » de mauvaise représentation de leurs données ?

---

# C05 — POLITIFACT / LI-MENG YAN

**Scope :** état des preuves et retrait PolitiFact.  
**Out of scope :** origine finale du SARS-CoV-2.

### C05-A
`TYPE: TEXT`
`CUTOFF: 2020-09-16`
`REQUIRED: S_C05_NATURE`

**Question :** Andersen et al. affirment-ils explicitement que leur analyse permet de prouver l'impossibilité de tout scénario impliquant un laboratoire ?

### C05-B
`TYPE: SEARCH`
`CUTOFF: 2020-09-16`

**Question :** Une source indépendante de Li-Meng Yan, rendue publique au plus tard le 16 septembre 2020, contenant des données ou éléments documentaires vérifiables et concluant explicitement à une création ou manipulation intentionnelle du SARS-CoV-2 a-t-elle été retrouvée ?

Applique obligatoirement les quatre critères `CRITERIA` du format SEARCH.

### C05-C
`TYPE: TEXT`
`REQUIRED: S_C05_POLITIFACT`

**Question :** PolitiFact indique-t-il explicitement avoir retiré ou suspendu son ancien fact-check parce qu'une prémisse sur l'impossibilité d'une manipulation était devenue plus contestée ?

---

# C06 — SPIKE

**Scope :** présence plasmatique et endpoint de toxicité.

### C06-A
`TYPE: TEXT`
`CUTOFF: 2021-09-28`
`REQUIRED: S_C06_OGATA`

**Question :** Ogata et al. rapportent-ils la détection de S1 ou Spike dans le plasma après vaccination ARNm ?

### C06-B
`TYPE: TEXT`
`CUTOFF: 2021-09-28`
`REQUIRED: S_C06_OGATA`

**Question :** Ogata et al. rapportent-ils un endpoint clinique établissant à lui seul une toxicité systémique causée par cette détection ?

### C06-C
`TYPE: DATA`
`CUTOFF: 2021-09-28`
`REQUIRED: S_C06_OGATA`

**Question :** La première disponibilité publique de l'étude Ogata est-elle antérieure ou égale au 28 septembre 2021 ?

---

# C07 — ARNm DANS LE LAIT MATERNEL

**Out of scope :** danger clinique pour le nourrisson.

### C07-A
`TYPE: SEARCH`
`CUTOFF: 2021-06-18`
`SEED: S_C07_GOLAN_PREPRINT`

**Question :** Une étude humaine rendue publiquement accessible, y compris sous forme de preprint, mesurant directement l'ARNm vaccinal dans le lait maternel a-t-elle été retrouvée avant ou au 18 juin 2021 ?

### C07-B
`TYPE: TEXT`
`CUTOFF: 2021-06-18`
`REQUIRED: S_C07_GOLAN_PREPRINT`

**Question :** Le preprint Golan affirme-t-il avoir démontré une impossibilité absolue de passage de l'ARNm vaccinal dans le lait maternel ?

### C07-C
`TYPE: DATA`
`REQUIRED: S_C07_HANNA`

**Question :** Une étude ultérieure rapporte-t-elle la détection d'ARNm vaccinal dans certains échantillons de lait maternel ?

---

# C08 — ANSM / GROSSESSE

### C08-A
`TYPE: TEXT`
`REQUIRED: S_C08_ANSM_ARCHIVE`

**Question :** La capture ANSM du 31 mai 2021 contient-elle explicitement la formule « fortement recommandée » pour la vaccination ARNm des femmes enceintes ?

### C08-B
`TYPE: TEXT`
`REQUIRED: S_C08_ANSM_ARCHIVE`

**Question :** Cette capture contient-elle des formulations exprimant des données limitées, de la prudence ou une décision individualisée avec un médecin ?

### C08-C
`TYPE: TEXT`
`REQUIRED: S_C08_ANSM_CURRENT`

**Question :** La page ANSM actuelle contient-elle la formule « fortement recommandée » ?

### C08-D
`TYPE: DATA`
`REQUIRED: S_C08_ANSM_ARCHIVE + S_C08_ANSM_CURRENT`

**Question :** Ces deux versions suffisent-elles à identifier la première date exacte d'introduction de la formule « fortement recommandée » ?

Règle : si elles permettent seulement de borner le changement entre deux dates, répondre `NO`.

---

# C09 — PASTEUR / « ×12 »

**IMPORTANT : utiliser `S_C09_PASTEUR_V1`, pas une page Pasteur vivante mise à jour en septembre.**

### C09-A
`TYPE: TEXT`
`CUTOFF: 2021-07-12`
`REQUIRED: S_C09_PASTEUR_V1`

**Question :** Le document Pasteur v1 du 28 juin produit-il explicitement un ratio proche de 12 entre risque de transmission des non-vaccinés et des vaccinés dans son scénario de référence ?

### C09-B
`TYPE: TEXT`
`CUTOFF: 2021-07-12`
`REQUIRED: S_C09_PASTEUR_V1`

**Question :** Le document présente-t-il ce ratio comme un résultat de modélisation ?

### C09-C
`TYPE: TEXT`
`CUTOFF: 2021-07-12`
`REQUIRED: S_C09_PASTEUR_V1`

**Question :** Le document v1 explicite-t-il des hypothèses conditionnant ses résultats, notamment R0, couverture vaccinale ou efficacité vaccinale ?

### C09-D
`TYPE: TEXT`
`CUTOFF: 2021-07-12`
`REQUIRED: S_C09_MACRON`

**Question :** Dans la phrase contenant « divisent par 12 son pouvoir de contamination », Emmanuel Macron mentionne-t-il explicitement qu'il s'agit d'une modélisation conditionnelle ?

---

# C10 — CASTEX / INFECTION

### C10-A
`TYPE: TEXT`
`CUTOFF: 2021-07-21`
`REQUIRED: S_C10_NEJM_DELTA`

**Question :** L'étude NEJM rapporte-t-elle une efficacité de 100 % contre l'infection symptomatique par Delta après deux doses ?

### C10-B
`TYPE: SEARCH`
`CUTOFF: 2021-07-21`

**Question :** Une source ouverte publiée avant ou au 21 juillet 2021 documentant des infections post-vaccinales a-t-elle été retrouvée ?

---

# C11 — PCR / OMS

`REQUIRED: S_C11_WHO`
`CUTOFF: 2021-01-31`

### C11-A
`TYPE: TEXT`

**Question :** La notice OMS affirme-t-elle que les tests PCR produisent « massivement » des faux positifs ?

### C11-B
`TYPE: TEXT`

**Question :** La notice demande-t-elle de tenir compte de facteurs d'interprétation tels que Ct/seuil, prévalence, contexte clinique ou instructions du fabricant ?

---

# C12 — BREVETS

**Scope : deux brevets précis fréquemment invoqués. Ne généralise pas au-delà.**

### C12-A
`TYPE: TEXT`
`REQUIRED: S_C12_SARS1_PATENT`

**Question :** Le brevet US7776521B1 concerne-t-il explicitement le SARS-CoV-2 identifié en 2019-2020 ?

### C12-B
`TYPE: TEXT`
`REQUIRED: S_C12_SARS1_PATENT`

**Question :** Le brevet US7776521B1 affirme-t-il que le SARS-CoV-2 a été créé intentionnellement ?

### C12-C
`TYPE: TEXT`
`REQUIRED: S_C12_PIRBRIGHT_PATENT`

**Question :** Le brevet US10130701B2 concerne-t-il un coronavirus aviaire / virus de bronchite infectieuse plutôt que le SARS-CoV-2 ?

### C12-D
`TYPE: TEXT`
`REQUIRED: S_C12_PIRBRIGHT_PATENT`

**Question :** Le brevet US10130701B2 affirme-t-il que le SARS-CoV-2 a été créé intentionnellement ?

---

# C13 — « THÉRAPIE GÉNIQUE »

**Scope : définition réglementaire européenne.**

### C13-A
`TYPE: TEXT`
`CUTOFF: 2021-08-31`
`REQUIRED: S_C13_EU_DIRECTIVE`

**Question :** La réglementation européenne exclut-elle explicitement les vaccins contre les maladies infectieuses de la catégorie des médicaments de thérapie génique ?

### C13-B
`TYPE: TEXT`
`CUTOFF: 2021-08-31`
`REQUIRED: S_C13_EU_DIRECTIVE`

**Question :** La définition réglementaire européenne exige-t-elle explicitement une modification permanente du génome humain pour qu'un produit relève de la thérapie génique ?

### C13-C
`TYPE: TEXT`
`CUTOFF: 2021-08-31`
`REQUIRED: S_C13_EU_DIRECTIVE`

**Question :** Le texte réglementaire permet-il de réduire la classification à la seule question « le produit modifie-t-il l'ADN humain ? »

---

# C14 — CHECKNEWS / PASS VACCINAL

**Scope : contenu du seul article du 8 janvier 2022.**

### C14-A
`TYPE: TEXT`
`REQUIRED: S_C14_CHECKNEWS`

**Question :** L'article reconnaît-il explicitement que la vaccination n'empêche pas totalement la transmission ?

### C14-B
`TYPE: TEXT`
`REQUIRED: S_C14_CHECKNEWS`

**Question :** L'article présente-t-il la prévention des formes graves, de l'hospitalisation ou de la saturation hospitalière comme justification importante du pass vaccinal ?

### C14-C
`TYPE: TEXT`
`REQUIRED: S_C14_CHECKNEWS`

**Question :** L'article cite-t-il un responsable politique reconnaissant qu'une croyance ou justification antérieure sur l'absence d'infection/transmission après vaccination était trop forte ?

### C14-D
`TYPE: TEXT`
`REQUIRED: S_C14_CHECKNEWS`

**Question :** CheckNews ou Libération reconnaît-il explicitement dans cet article qu'un de ses propres contenus antérieurs était faux, trop catégorique ou devait être corrigé ?

Règle spécifique C14 :

> Si l'article intégral n'est pas réellement ouvert, les quatre réponses C14-A/B/C/D doivent être `UNREADABLE`. Le titre, les snippets et un article ultérieur sont insuffisants.

---

# 14. CONTRÔLE FINAL SILENCIEUX

Avant d'envoyer :

1. tous les atomes sont présents ;
2. toutes les valeurs sont autorisées ;
3. `TEXT + REQUIRED non ouvert => UNREADABLE` ;
4. `DATA sans pièce décisive ouverte => UNCERTAIN` ;
5. `SEARCH FOUND` implique `FOUND_SOURCE OPENED: YES` ;
6. aucune preuve `AT_T` n'est postérieure au cutoff ;
7. pour une étude, `FIRST_PUBLIC_DATE` est utilisée ;
8. aucune page actuelle n'est rétroprojetée ;
9. une URL ne soutient que son propre contenu ;
10. `NOT_FOUND` n'est jamais transformé en inexistence ;
11. aucune synthèse générale ;
12. aucune conclusion éditoriale.

Termine immédiatement après C14-D.
