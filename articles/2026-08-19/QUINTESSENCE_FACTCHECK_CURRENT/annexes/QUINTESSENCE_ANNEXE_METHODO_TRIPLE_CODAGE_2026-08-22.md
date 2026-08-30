# QUINTESSENCE - Annexe méthodologique du triple codage

**Date :** 22 août 2026
**Objet :** rendre rejouable le test adversarial portant sur 154 propositions issues de 15 interventions publiques françaises.

## 1. Question et discipline

Le test ne cherche pas à mesurer le « mensonge » ni l'intention des locuteurs. Il compare, à la date de chaque déclaration, la force publique de la formulation avec la force des meilleures preuves alors raisonnablement accessibles.

`EVOLUTION_ULTERIEURE != ERREUR_A_T`

`C2 != MENSONGE_INTENTIONNEL`

Le corpus est déterministe et non aléatoire. Aucun pourcentage ne doit être extrapolé à l'ensemble de la communication politique française.

## 2. Corpus gelé avant adjudication

Les 15 interventions ont été fixées avant l'extraction exhaustive et le codage :

- **16/03/2020 - Emmanuel Macron** - confinement - 7 propositions retenues - https://www.elysee.fr/emmanuel-macron/2020/03/16/adresse-aux-francais-covid19
- **11/09/2020 - Jean Castex** - tester-tracer-isoler - 6 propositions retenues - https://www.info.gouv.fr/upload/media/default/0001/01/2020_09_declaration_de_m._jean_castex_premier_ministre_-_11.09.2020.pdf
- **13/10/2020 - Olivier Véran** - régime transitoire - 5 propositions retenues - https://www.vie-publique.fr/discours/276944-olivier-veran-13102020-prorogation-du-regime-transitoire
- **22/10/2020 - Jean Castex** - extension couvre-feu - 8 propositions retenues - https://www.info.gouv.fr/discours/11817-discours-du-premier-ministre-conference-de-presse-sur-l-application-des-mesures-contre-la-covid-19
- **24/10/2020 - Olivier Véran** - état urgence sanitaire - 7 propositions retenues - https://www.assemblee-nationale.fr/dyn/15/comptes-rendus/seance/session-ordinaire-de-2020-2021/premiere-seance-du-samedi-24-octobre-2020.pdf
- **28/10/2020 - Emmanuel Macron** - second confinement - 17 propositions retenues - https://www.elysee.fr/emmanuel-macron/2020/10/28/adresse-aux-francais-28-octobre
- **14/01/2021 - Jean Castex** - couvre-feu 18 h - 8 propositions retenues - https://www.vie-publique.fr/discours/278106-jean-castex-14012021-couvre-feu-18h-virus-covid-mutant
- **20/01/2021 - Olivier Véran** - état urgence sanitaire - 7 propositions retenues - https://www.vie-publique.fr/discours/278705-olivier-veran-20012021-prorogation-de-letat-durgence-sanitaire
- **25/02/2021 - Jean Castex** - restrictions territoriales - 10 propositions retenues - https://www.info.gouv.fr/upload/media/default/0001/01/2021_02_discours_de_m._jean_castex_premier_ministre_-_conference_de_presse_sur_les_mesures_contre_la_covid-19-25.02.2021.pdf
- **18/03/2021 - Jean Castex** - confinements territorialisés - 16 propositions retenues - https://www.vie-publique.fr/discours/279090-jean-castex-18032021-covid-19-confinement-localise-couvre-feu-vaccin
- **31/03/2021 - Emmanuel Macron** - restrictions / écoles - 15 propositions retenues - https://www.elysee.fr/emmanuel-macron/2021/03/31/adresse-aux-francais-31-mars-2021
- **12/07/2021 - Emmanuel Macron** - pass / vaccination / tests payants - 16 propositions retenues - https://www.elysee.fr/emmanuel-macron/2021/07/12/adresse-aux-francais-12-juillet-2021
- **20/07/2021 - Olivier Véran** - pass / obligation - 11 propositions retenues - https://www.vie-publique.fr/discours/281265-olivier-veran-20072021-projet-de-loi-gestion-de-la-crise-sanitaire
- **09/11/2021 - Emmanuel Macron** - rappel / pass - 11 propositions retenues - https://www.elysee.fr/emmanuel-macron/2021/11/09/adresse-aux-francais-9-novembre-2021
- **11/01/2022 - Olivier Véran** - passe vaccinal - 10 propositions retenues - https://www.vie-publique.fr/discours/283737-olivier-veran-11012022-gestion-de-la-crise-sanitaire-senat

Répartition des documents par acteur : cinq interventions d'Emmanuel Macron, cinq de Jean Castex et cinq d'Olivier Véran.

## 3. Unité documentaire

- Allocution ou discours autonome : texte intégral de l'intervention de l'acteur ciblé.
- Conférence de presse à plusieurs intervenants : segment principal continu de l'acteur ciblé avant passage au locuteur suivant.
- Audition ou débat parlementaire : intervention liminaire continue de l'acteur ciblé avant questions, réponses, interruptions ou nouvelle prise de parole.
- Les échanges ultérieurs et les propos des autres acteurs sont exclus de ce corpus.

## 4. Critères d'inclusion des propositions

Une proposition est extraite si elle remplit au moins un de ces critères :

1. elle décrit l'état épidémique ou sanitaire utilisé pour justifier une mesure ;
2. elle attribue une cause ou un effet à une mesure, un variant, un comportement ou la vaccination ;
3. elle prédit une conséquence sanitaire ou institutionnelle pertinente pour la mesure ;
4. elle affirme une nécessité, une absence d'alternative, une impossibilité ou une suffisance ;
5. elle donne une magnitude quantitative utilisée comme justification.

Sont exclus : prescriptions normatives pures, valeurs, rhétorique sans contenu falsifiable, description administrative sans rôle justificatif, chiffres logistiques sans fonction justificative et répétitions littérales.

Une proposition composite est divisée en unités falsifiables uniquement lorsque cette division ne modifie pas artificiellement sa modalité. Sinon elle reste composite et peut être classée non adjudicable.

## 5. Catégories de codage

- **C0 - calibré** : force publique inférieure ou égale à la meilleure preuve contemporaine accessible.
- **C1 - compression mineure** : modalité, précision, causalité ou généralité légèrement plus forte, sans inversion substantielle.
- **C2 - surcertitude matérielle** : causalité, universalité, nécessité, impossibilité, précision ou magnitude substantiellement plus fortes que les preuves disponibles à la date T.
- **U - non adjudicable** : preuve contemporaine insuffisante ou inaccessible, ou proposition composite impossible à trancher proprement.

## 6. Recodage aveugle par modèles de langage

Le premier codage (système A) a été recodé par deux autres modèles de langage (B et C) sur des phrases anonymisées et réordonnées. Les identités d'acteurs, URLs politiques, codes initiaux, rationales initiales et statuts de réparation étaient masqués. L'aveuglement porte donc sur ces métadonnées et sur les labels initiaux. Il ne transforme pas les trois sorties en codages humains indépendants ni en preuves probatoires indépendantes.

Une première tentative Grok a été rejetée comme réplication indépendante après détection d'une similarité textuelle anormale avec le système B. Une nouvelle passe clean room a utilisé un nouvel ordre et de nouveaux identifiants. Elle est conservée pour les labels avec une réserve documentaire, car plusieurs rationales étaient plus courtes et moins sourcées que le protocole demandé.

## 7. Accord inter-systèmes

- Système A vs système B : accord exact **41,6 %**, κ de Cohen **0,078**.
- Système A vs système C clean room : accord exact **50,6 %**, κ **0,190**.
- Système B vs système C clean room : accord exact **75,3 %**, κ **0,228**.

Conclusion : la frontière fine C0/C1 n'est pas suffisamment reproductible pour produire un taux global de surcertitude.

## 8. Partition disjointe des 154 propositions

- **46** : C0 chez les trois systèmes.
- **6** : C1 chez les trois systèmes.
- **1** : C2 chez les trois systèmes.
- **101** : pas d'accord exact des trois systèmes.
  - dont **99** avec majorité 2 contre 1 ;
  - et **2** avec trois codes différents.

Contrôle : 46 + 6 + 1 + 101 = **154**.

## 9. Statistique transversale, non additive

**10 propositions sur 154 ne reçoivent aucun C0 dans les sorties brutes.** Cette statistique recoupe la partition précédente et ne doit donc pas lui être additionnée.

Le seul C2 unanime brut est : « Les vaccins disponibles divisent par 12 le pouvoir de contamination de Delta. » Cette unanimité ne vaut pas adjudication documentaire : deux recodages n'ont pas correctement intégré la prépublication Pasteur contenant déjà le ratio 12,1. Le cas doit être arbitré à partir de la source primaire et de la transformation d'un résultat conditionnel de modèle en formule politique, non par vote des trois labels.

Le cas « quoi que nous fassions, près de 9 000 patients seront en réanimation » est codé C2/C2/C1.

## 10. Fichiers de réplication

- [`QUINTESSENCE_THREE_CODER_CLEANROOM_COMPARISON_154_2026-08-22.csv`](../data/QUINTESSENCE_THREE_CODER_CLEANROOM_COMPARISON_154_2026-08-22.csv) : comparaison ligne à ligne des trois codes.
- [`QUINTESSENCE_THREE_CODER_CRITICAL_CASES_2026-08-22.csv`](../data/QUINTESSENCE_THREE_CODER_CRITICAL_CASES_2026-08-22.csv) : cas non-C0 robustes et cas ayant au moins un C2.
- `QUINTESSENCE_SECOND_CODER_INTERNAL_KEY_154_2026-08-22.csv` : clé interne de remappage, à conserver hors du protocole aveugle.
- `XQ181_G04C_PREREG_INTRADOCUMENT_2026-08-22.md` : pré-enregistrement des critères, fonctions, hypothèses et gates.
- `XQ181_G04C_SCOPE_NOTE_2026-08-22.md` : règle de périmètre documentaire.

## 11. Limites

- corpus ciblé, non représentatif de toute la communication politique ;
- qualité documentaire inégale du troisième système ;
- absence de codage humain indépendant ;
- intégration incomplète d'une source primaire centrale dans deux recodages du « ×12 » ;
- faible reproductibilité de la frontière C0/C1 ;
- la majorité des systèmes n'est jamais traitée comme preuve suffisante ;
- les cas éditorialement centraux doivent être arbitrés par les sources primaires.

## Verdict méthodologique

`GLOBAL_OVERCERTAINTY_RATE = BLOCKED`

`C2_UNANIMOUS_3_OF_3_RAW = 1`

`C2_UNANIMOUS_AS_INDEPENDENT_CONFIRMATION = INVALID`

`ALL_NON_C0_3_OF_3 = 10`

`GENERALIZED_OVERCERTAINTY = NOT_SUPPORTED`
