# XQ181 — G04C — Pré-enregistrement intra-document exhaustif

**Gel :** 2026-08-22
**Statut :** `PREREGISTERED / EXTRACTION_NOT_YET_ADJUDICATED`
**Parent :** XQ181-G04B / INV-FC-62

## Question
Tester l'hypothèse post hoc issue de G04B : la surcertitude matérielle pourrait ne pas être plus fréquente dans les documents à forte contrainte en général, mais se concentrer au moment rhétorique où le diagnostic devient justification, nécessité/absence d'alternative ou efficacité attendue.

## Corpus gelé
Exactement les 15 documents de G04B, sans ajout ni remplacement :
- Président : 16-03-2020 ; 28-10-2020 ; 31-03-2021 ; 12-07-2021 ; 09-11-2021.
- Premier ministre : 11-09-2020 ; 22-10-2020 ; 14-01-2021 ; 25-02-2021 ; 18-03-2021.
- Ministre de la Santé : 13-10-2020 ; 24-10-2020 ; 20-01-2021 ; 20-07-2021 ; 11-01-2022.

## Extraction exhaustive
Pour chaque document, extraire dans l'ordre **toutes** les affirmations matérielles qui remplissent au moins un critère :
1. décrivent l'état épidémique ou sanitaire invoqué pour justifier la mesure ;
2. attribuent une cause ou un effet à une mesure, un variant, un comportement ou la vaccination ;
3. prédisent une conséquence sanitaire ou institutionnelle pertinente pour la mesure ;
4. affirment une nécessité, une absence d'alternative, une impossibilité ou une suffisance ;
5. donnent une magnitude quantitative utilisée comme justification de la mesure.

Exclure : prescriptions normatives pures, valeurs, rhétorique sans contenu falsifiable, description administrative sans justification, chiffres logistiques sans rôle justificatif, répétitions littérales.

Une proposition composite doit être divisée en unités falsifiables quand le texte le permet. Si la division change artificiellement la modalité, conserver `COMPOSITE/OPEN`.

## Position intra-document
Après extraction exhaustive de N claims éligibles dans un document :
- `norm_pos = (rang - 1) / max(N - 1, 1)`.
- `EARLY` si norm_pos < 1/3.
- `MIDDLE` si 1/3 <= norm_pos < 2/3.
- `LATE` si norm_pos >= 2/3.

Cette position est calculée **avant adjudication C0/C1/C2**.

## Fonction rhétorique primaire
Chaque claim reçoit une fonction primaire gelée avant adjudication :
- `D_DIAGNOSTIC` : état descriptif / risque / incidence / capacité.
- `J_JUSTIFICATION` : causalité expliquant pourquoi une mesure est nécessaire ou pertinente.
- `N_NECESSITY` : nécessité, absence d'alternative, impossibilité, universalité justificative.
- `E_EXPECTED_EFFECT` : efficacité attendue, prédiction ou conséquence future d'une mesure/comportement.
- `Q_QUANT_MAGNITUDE` : chiffre/magnitude servant de levier justificatif sans causalité propre.
- `M_MIXED` : deux fonctions inséparables ; exclu du test principal par fonction mais conservé descriptivement.

## Codage épistémique
- `C0 CALIBRÉ` : force publique <= meilleure preuve contemporaine accessible.
- `C1 COMPRESSION_MINEURE` : modalité/spécificité plus forte, sans inversion substantielle de causalité, universalité, nécessité ou magnitude.
- `C2 SURCERTITUDE_MATÉRIELLE` : causalité, universalité, nécessité, impossibilité, précision ou magnitude substantiellement plus fortes que les preuves disponibles à T.
- `U OPEN` : preuve contemporaine insuffisante/inaccessible ou claim composite non adjudicable.

Évolution ultérieure != erreur à T. C2 != mensonge intentionnel.

## Hypothèses gelées
- H2a : `C2_RATE_{J+N+E} > C2_RATE_{D+Q}`.
- H2b : `C2_RATE_LATE > C2_RATE_EARLY`.
- H2c : les C2 ne dépendent pas d'un seul acteur/document/cas connu.

## Rivaux
- R1 vulgarisation : simplification légère C1, pas C2, augmente près des décisions.
- R2 sélection rhétorique : les absolus célèbres sont rares et notre mémoire les surpondère.
- R3 urgence : formulations fortes reflètent une décision sous incertitude, mais restent compatibles avec les preuves à T.

## Tests
Principal : différence descriptive C2 entre fonctions `J+N+E` et `D+Q`, puis LATE vs EARLY.
Secondaires : C1+C2 ; acteur ; période ; exclusion des cas pilotes connus (×12, « seule façon », « quoi que nous fassions » si présents).

Pas de p-value interprétée comme populationnelle : corpus déterministe non aléatoire. Des intervalles descriptifs peuvent être calculés seulement comme repères de fragilité.

## Gates
- Si C2 n'augmente pas dans J/N/E ni en LATE : `H2_AFFAIBLIE/REFUTEE`.
- Si hausse modeste dépendant d'un seul document/cas connu : `H2_NON_ROBUSTE`.
- Si hausse répétée sur plusieurs acteurs/documents et survit à l'exclusion des pilotes : `H2_RENFORCEE_BORNEE`.

## Réparation
Pour chaque C2 et C1 de forte conséquence : correction explicite, mise à jour du même support, contextualisation ultérieure, contre-discours contemporain, portée comparable si métrique homogène.

## Discipline
Aucun claim n'est ajouté/retiré en fonction de son futur code. Toute exclusion est motivée par la règle d'éligibilité ci-dessus avant adjudication.
