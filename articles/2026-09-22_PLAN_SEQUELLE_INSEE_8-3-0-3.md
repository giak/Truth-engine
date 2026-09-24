# PLAN DÉTAILLÉ — Séquelle « 8,3 ± 0,3 : nous avons attaqué l'INSEE, voici ce qui a tenu »

Statut : PLAN v1 (22/09/2026) — SUIVI : article rédigé le 22/09/2026 dans articles/2026-09-22_18-00_insee-sequelle-8-3-0-3_ARTICLE.md, audits multi-rôles passés sur le texte réel (fact-check ligne à ligne : 5 défauts corrigés dont un chiffre orphelin et une inversion CNERP ; scan des interdits : conforme ; adhérence : conforme ; deux points ouverts éditoriaux : slug du lien V2 à insérer à la publication, « CV médian 1,16 % » volontairement omis par densité).
Genre : récit de méthode (F3) × anatomie d'un chiffre (angle 1), fin constructive (protocole).
Spine retenue : le taux de chômage (8,3 ± 0,3). Metzing/populations légales = contre-point interne, pas spine (arbitrage documenté séparément).

## Convention de traçabilité

- `[R-1704·F-01]` = fait F-01 du run cité, registre préservé dans `_quintessence_v3` (runs 20-21/09, tous G0-G10 PASS, DELIVERY PASS).
- `[R-1625·FCT-006]` = fait du run 20260922-1625 (blindage 4 axes) ; autres runs du 22/09 : RENARD (process), RECL (reclassifications APU), SURP (surprise déficit), PROT (protocole audit), MEDI (audit médiation presse 20 articles).
- Tout fait non listé ici est HORS ARTICLE, sauf re-sourçage à la rédaction.

## Longueur cible et règle de densité

3 500-4 500 mots, une phrase = une claim bornée, chaque chiffre porte sa source au moins en fin d'acte. Zéro em-dash dans les titres publiés (règle maison `no-em-dash`). L'article V2 du 21/09 (formules d'indexation, chiffre→formule) est CITÉ, jamais répété : cette séquelle couvre l'institution (fabrique→confiance).

---

## CHAPÔ — le hook

**Fonction** : installer la tension entre le chiffre qu'on nous donne et le chiffre qui existe.

**Faits disponibles** :
- Le chiffre du matin : 8,3 % T2 2026 [R-1812·F-01]. Sa vraie valeur publiée : 8,3 ± 0,3 pt, en niveau comme en évolution, publiée par le producteur et restituée indépendamment par la commission d'enquête du Sénat [R-0347·F-04 ✦].
- Hook alternatif (tension perception) : l'inflation perçue est en moyenne ~6 points au-dessus de l'IPC depuis 2004 (enquêtes de perception OPI/CAMME ; le fait source dit « OPI, CAMME, ~2 000 ménages » — l'appartenance du chiffre à l'OPI seule est à trancher à la rédaction), écart reconnu et expliqué (surpondération des prix en hausse et à forte fréquence d'achat) par l'Insee et la Banque de France [R-1704·F-01].

**Caveats** : le +6 pts est une moyenne de glissements perçus/mesurés sur longue période, pas un écart actuel ; le ±0,3 est un intervalle d'échantillonnage (enquête), pas une erreur administrée.

**Interdits** : ne pas écrire « le chiffre officiel est faux » ; ne pas présenter le ±0,3 comme découverte (il est publié) — c'est sa disparition médiatique qui est notre mesure.

---

## 1. Le chiffre du matin

**Fonction** : anatomie de la médiation — comment un nombre sans incertitude devient une réalité publique.

**Faits sourcés** (audit MEDI, 20 articles fetchés, fenêtre T3 2025 → 09/2026) :
- **0/19** articles mentionnent l'intervalle de confiance.
- « Au sens du BIT » : 13/19 ; alternative (cat A ou halo) nommée et chiffrée : 10/19 — dont 4 articles qui reproduisent quasi verbatim la même dépêche AFP (sans AFP : ~32 %).
- **0 titre sur 21** ne porte une mention d'incertitude ou de convention ; les corrections Dares sont documentées en corps, jamais en une. (Incohérence de décompte à trancher en relisant l'artefact MEDI : 20 articles fetchés mais 21 titres scorés — un article à double titre ou un partiel ; ne pas publier le décompte titres sans l'avoir résolu.)
- La seule décomposition chiffrée « 8,3 → 7,9 sans les nouveaux publics » est prononcée par le ministre (Farandou), pas construite par un journaliste.
- Contre-point méritant : Sud Ouest signale la suspension de labellisation ASP des séries demandeurs d'emploi [voir §6].
- Biais de mesure assumés : 9 grands titres inaccessibles (403/anti-bot : Le Monde, Libération, Les Échos, Ouest-France) ; sélection SEO autour des jours de communiqué ; contre-factuel extrême (les 9 remplacants tous à 4/4) ne ferait monter le composite qu'à 57 %.

**Caveats** : résultat CERTAIN sur le corpus lisible, généralisation à toute la presse SUPPORTED, pas VERIFIED ; extraction ~6 000 caractères ; le scoring porte sur le texte lu, jamais le titre seul.

**Interdits** : « la presse cache » (elle recycle) ; « l'INSEE ne communique pas » (l'IC est publié) ; généraliser 0/19 à toute la presse.

---

## 2. Ce que vaut un dixième de point

**Fonction** : démontrer que les conventions ne sont pas de la cosmétique — chaque dixième devient de l'argent, et chaque convention a un gagnant (mais pas le même).

**Faits sourcés** :
- Prestations sociales indexées ~500 Md€ : ~**5 Md€ par point** d'inflation (presque 0,2 pt de PIB) ; ~**0,3 Md€ par dixième de point** sur la charge d'intérêts (division arithmétique signalée comme telle, pas un chiffre publié) [R-0428·F-09].
- Barème IR indexé sur l'estimation de septembre n-1 sans régularisation : 8 années sur 13 en défaveur du contribuable, cumul -4,1 pts (2010-2022) ; trop-payé estimé 6 Md€ (2019-2023), 2,8-3,4 Md€ incl. 2024 ; gel 2026 = +2 Md€ pour l'État et +200 000 foyers imposables [R-2110·F-04].
- IRL = moyenne 12 mois de l'IPC **hors tabac et hors loyers** (loi 89-462 art 17-1) : l'indice qui indexe les loyers exclut les loyers ; 7 millions de ménages locataires du privé [R-2110·F-02 ; R-0428·F-02 ✦ énoncé identique administration + ANIL].
- Le plafond IRL 3,5 % (T3 2022-T1 2024, loi 2022-1158 art 12) a transféré ~1,5-2 Md€/an **aux locataires** ; cumul 2022-2025 : IRL +10,9 % vs loyers observés +7,7 % ; bascule de signe 2025 (ELC +2,32 % > IRL +1,02 %, première fois de la série) [R-2154·F-02 ; R-2155·F-01, F-03, F-04 — extraction primaire SDMX BDM 001763530].
- Retraites indexées sur les prix depuis 1987/2003 : bascule ≈ 4 Md€/an, ~107 Md€ de niveau à horizon ; sous Destinie, la législation pré-1993 (indexation salaires) donnerait +19,5 % de dépenses [R-2110·F-03].
- Populations légales : 113 habitants d'écart à Metzing ≈ **9 800 €/an** de dotation forfaitaire (élasticité médiane mesurée 86,9 €/hab ; plage bornée 7 300-14 600 €/an ; majorant ~18 000) ; rattrapage réel documenté : 678 → 699 → 715 (2024-2026), DGF totale +7,6 % [R-2008·F-03, F-04, F-05 ; confirmé R-2050·F-04].

**Caveats** : 9 800 € est une borne (élasticité médiane, corrélée par Bouzonville), pas une perte subie — le rattrapage existe ; le 0,3 Md€/dixième est une division signalée ; les cumuls IRL/ELC dépendent du référentiel choisi (le signe du transfert change avec lui — c'est le résultat, pas un bug).

**Interdits** : « Metzing a perdu 9 800 €/an » ; « l'IRL est un siphon » (réfuté : transfert conjoncturel bidirectionnel, « le siphon cherché n'existe pas ») ; « un bénéficiaire caché » (les quatre conventions ont des gagnants différents et publiés).

---

## 3. La fabrique, en quatre machines

**Fonction** : montrer le process réel — estimation, sondage, convention, révision — avant d'attaquer. Le lecteur doit pouvoir dire : « je sais maintenant d'où sort ce nombre ».

**Machine 1 — L'emploi (EEC)** :
- Enquête Emploi en continu, ~110 000 personnes de 15 ans ou plus répondantes par trimestre, panel rotatif [SOURCÉ 22/09 audit : Insee, Emploi-chômage-revenus du travail, « Sources et méthodes », insee.fr/fr/statistiques/fichier/4501170/ECRT2020_Sources-methodes.pdf — même formulation dans ECRT2022] ; 3 critères BIT ; ±0,3 pt en niveau comme en évolution, publié (producteur + Sénat) [R-1812·F-01 ; R-0347·F-04 ✦].
- Trois définitions coexistent : BIT (3 critères), catégorie A (administratif), chômeur au sens du recensement (auto-déclaration, plus élevé) [R-1812·F-04] ; divergence structurelle BIT vs cat A attribuée aux réformes « indépendamment de la situation réelle » du marché [R-1812·F-02].
- Taux de réponse publiés : 77 % (2021), collecte 60,5 %/64,3 % (T2 2023), T3 2025 : 60,6 % ; internet 46,4 % des réinterrogations [R-0255·F-01, F-02 ; R-0347·F-01, F-03] ; non-réponse différentielle documentée (résidences non principales, Paris, locataires, QPV) [R-0255·F-08].
- Correction RSA : sous-estimation jusqu'au T2 2024, puis couverture ~90 % via appariement Pasrau, série passée corrigée sans rupture [R-0347·F-06].

**Machine 2 — Les populations (recensement)** :
- Rotation 1/5 des communes <10 000 (1 an sur 5 en direct, 2/5 évolution, 2/5 données fiscales), 8 % des adresses pour les grandes ; officialisées par décret annuel depuis 2008 ; référencées par ~350 articles législatifs (DGF, seuils, conseillers) [R-1812·F-03 ; R-0428·F-05].
- Précision publiée : exemple réel — commune de 4 900 hab, écart-type 140, intervalle 95 % [4 620 ; 5 180] [R-0255·F-03] ; à l'échelle nationale, la fiche Insee énonce verbatim : « l'erreur aléatoire introduite par le sondage dans les grandes communes conduit à un coefficient de variation de 0,01 %, soit une imprécision de + ou - 17 500 personnes » [SOURCÉ 22/09 audit : fiche-precision.pdf, insee.fr/fr/statistiques/fichier/2383177 — texte confirmé par extrait du domaine insee.fr ; PDF non extractible par nos outils, citation verbatim obligatoire, RECALCUL DU RATIO INTERDIT dans l'article : l'agrégat « grandes communes » n'est pas chiffré dans l'extrait, la cohérence arithmétique interne ne peut être vérifiée de l'extérieur] ; CV médian < 1,16 % pour les communes 10-20 k [R-0255·F-05].
- Erreur → argent : la mécanique DGF (§2) et le contentieux (§6).

**Machine 3 — Les prix (IPC)** :
- ~200 000 relevés/mois, ~27 000 points de vente, panier COICOP pondéré N-1, corrections qualité (hédonique, shrinkflation) documentées [run RENARD, A2 VERIFIED].
- Champ : loyers imputés exclus (comme l'HICP) ; santé remboursée incluse (indice hybride) ; l'Insee publie lui-même les indices alternatifs [R-1704·F-05 ; R-1625·FCT-003].
- Le chiffre « l'inflation des 10 % les plus modestes a été +2,9 pt supérieure à celle des 10 % les plus aisés sur 20 ans » est publié par l'Insee lui-même [RENARD].

**Machine 4 — Les comptes (PIB, dette)** :
- Sources administratives (ESANE/DGFiP, douanes), révision ordinaire 3 ans, rebasing base 2020 révisant 1949-2023 [R-1812·F-06] ; révisions 2023-2025 chiffrées par l'Insee : 2023 +0,2 pt, 2024 +0,3 pt, **2025 inchangé** (note du 3 juin 2026) [R-1921·F-05].
- Biais moyen des révisions 2005-2024 : +0,34 pt haussier (Rexecode) ; cas 2023 : 0,9 % → 1,9 % (corrigé des jours ouvrés ; 1,6 % brut) ; **erratum Insee Première 2105 publié le jour même** [R-1812·F-07 ✦ ; R-1921·F-06].
- Dette Maastricht : non consolidée, à valeur de marché (varie avec les taux), retraites hors dette en Europe (contrairement aux USA) ; Cour des comptes 2019 : le périmètre « reflète correctement la réalité » [RENARD].

**Caveats transverses** : tout ceci est documenté par le producteur ou le contrôle — c'est un acte de description, pas d'exonération ; la précision existe dans les fiches méthodo mais n'est pas attachée au chiffre diffusé (le verrou éditorial, cf. §1).

**Interdits** : « les comptes sont inventés » ; « les révisions sont cachées » (causes publiées, erratum jour même) ; « la population française est fausse » (erreur de sondage relative marginale ; et le chiffre ±17 500 n'est pas publié sans son re-sourçage, cf. sanity check ci-dessus) ; confondre correction des jours ouvrés et révision.

---

## 4. Nous avons attaqué — les six hypothèses

**Fonction** : poser honnêtement nos hypothèses d'assassins avec leurs priors, avant les verdicts. C'est le pacte de lisibilité du genre.

Les six hypothèses (issues des runs, reformulées pour le lecteur) :
- **H1** « Ça ment » — falsification de type INDEC, pression politique effective. Prior faible (base rate : rares dans les démocraties développées ; exceptions : Argentine, Grèce 2004-2010).
- **H2** « Les conventions cachent un bénéficiaire » — la mesure sert des intérêts d'indexation de manière systémique et directionnelle.
- **H3** « L'opacité cache des choses » — le défaut de transparence protège des zones d'ombre matérielles.
- **H4** « La bonne surprise 2025 est maquillée » — le 5,4 % → 5,1 % vient d'une révision de dénominateur (PIB), pas de recettes réelles.
- **H5** « Les reclassifications dissimulent des dettes » — le périmètre APU bouge stratégiquement, dans un seul sens.
- **H6** « Les loyers imputés cachent l'inflation » — l'IPC sous-estime le coût du logement réel.

**Caveats** : chaque H est une hypothèse de travail, jamais une conclusion à défendre (discipline RENARD) ; les priors sont des choix argumentés, pas des mesures.

**Interdits** : cariaturer les hypothèses pour mieux les tuer (pas d'homme de paille) ; les présenter comme « nos accusations » (ce sont des tests).

---

## 5. Ce qui a tenu — les verdicts

**Fonction** : le cœur. Chaque verdict avec sa preuve et son reste.

**H1 — KILLÉE telle que formulée.** Aucune trace discriminante de falsification : méthodos complètes publiées, révisions documentées avec causes, erratum le jour même [R-1921], indices alternatifs publiés par l'Insee lui-même [R-1625·FCT-003]. Structures adversariales réelles **à enjeux** : Eurostat vérifie le GNI français (la cotisation UE en dépend), peer review du Code de bonnes pratiques (visite 28/06-02/07/2021, rapport publié) [R-0446·F-01], ASP, Cour des comptes. La pression politique la plus dure documentée (Darmanin contre l'enquête de victimation, 2021) a rencontré une résistance institutionnelle visible [RENARD]. **Caveat non négociable** : c'est une absence de contre-preuve, pas une preuve d'intégrité — aucun audit forensique de type INDEC n'a jamais été mené sur l'Insee (gap par design, cf. §7).

**H2 — RÉFUTÉE comme théorie du bénéficiaire unique, SURVIVANTE comme espace conventionnel.** Les signes varient : plafond IRL → locataires (~1,5-2 Md€/an), barème IR → État (2,8-6 Md€), retraites 1987 → cotisants/État, SMIC → salariés modestes ; « aucune de ces conventions n'est cachée » (mesuré) [R-2110·F-06]. Survit : chaque convention a un gagnant identifiable et non rémunéré par le hasard — l'espace de manœuvre est réel, documenté, et médiatiquement invisible (§1).

**H3 — REFORMULÉE : opacité d'expertise, pas dissimulation.** Tout est publié, presque rien n'est communiqué. Trois convergences : IC 0/19 dans la presse (§1) ; la revue par les pairs elle-même relève que les rapports de qualité produits pour Eurostat « ne sont pas toujours publiés » [R-0446·F-03] ; le baromètre de réponse existe pour les entreprises (70,2 %) et pas pour les ménages — déficit de centralisation, pas d'accès [R-0255·M2].

**H4 — RÉFUTÉE pour 2025, datée pour 2023-2024.** Décomposition : 5,4 % → 5,1 % = 0,3 pt dont **~95 % numérateur** (161 → 152,5 Md€), dénominateur ~5 % ; à PIB prévu constant, 152,5/2 981 = 5,11 % (la surprise tient sans révision) ; PIB 2025 non révisé (note du 3/06/2026) [SURP]. **CAVEAT OBLIGATOIRE** : le PIB prévu 2 981 Md€ est DÉRIVÉ (161/0,054), non sourcé en direct — robuste à ±50 Md€, à l'écrire tel quel. La « chance fiscale » est décomposée par la Cour des comptes : +30,7 Md€ = 14,4 votées + 3,3 transferts + **13,0 spontané** ; élasticité ~1,05 vs 0,9 prévu [R-1625·FCT-006, FCT-007]. Mais les erreurs 2023-2024 étaient dans l'autre sens — SOURCÉ 22/09 audit : Trésor-Éco n°356 (20/01/2025, actualisé 16/07/2025) : déficit 2023 établi à -5,5 % du PIB contre -4,9 % prévu, écart portant **principalement sur les prélèvements obligatoires** (élasticité historiquement basse, +2,6 % spontané contre +6,3 % de PIB nominal) — l'ancien chiffre « dérives de dépenses 27-32 Md€ » était orphelin ET mal attribué, il est RETIRÉ ; déficit 2024 : -4,4 % en LFI → -5,8 % réalisé (juillet 2025), dérive de 1,4 pt en un an, révisions finales +9,5 Md€ d'amélioration dont collectivités +6,5 et État +3,4 ; FIPECO 18/05/2026 : en 2023 l'inflation plus forte que prévue a permis de tenir l'objectif en volume des dépenses [Trésor-Éco 356 ; FIPECO fiche prévision des dépenses]. → le problème est de neutralité institutionnelle, pas de fraude démontrée ; les erreurs de prévision ne sont pas toujours dans le même sens (2023-2024 : dégradation ; 2025 : amélioration). Contradiction non moyennée : 610 Md€ (Vie-publique) vs 356,4 Md€ (Cour des comptes) = périmètres fiscaux différents, à fixer à chaque citation [R-1625·FCT-008, tier ⁅].

**H5 — CLOSE comptablement, trou matériel maintenu.** Privatisations FDJ/ADP/Engie = cessions de titres (FDJ 2019 : ~50 % cédés pour ~1,9 Md€, État restant actionnaire), aucune sortie d'entité du périmètre documentée 2010-2025 ; l'asymétrie directionnelle des reclassifications (entrées seulement : EPL 2012 ~34 Md€, SFIL 2019 ~40 Md€ ancre basse, SNCF 2020-22 : 35 Md€, Unédic non désagrégée) s'explique par le contrôle public persistant [R-1625·FCT-001, FCT-002 ; RECL]. **Le trou** : aucun tableau public consolidé des effets de périmètre sur la série de dette (marches statistiques ≥100 Md€ — borne, pas mesure).

**H6 — RETOURNÉE.** La série alternative incluant les loyers imputés est **publiée par l'Insee** (Focus 152) et est légèrement **plus basse** que l'IPC sur 1999-2018 (1,6 % vs 1,8 % en 2018) : l'inférence naïve est morte [R-1625·FCT-003]. La critique valide porte sur le **champ** : Eurostat juge « trop étroite » la méthode excluant le logement des propriétaires [R-1704·F-05], le manuel FMI ne recommande aucune méthode, le coût du logement des propriétaires est absent de l'IPCH (Banque de France, billet 253) [R-1625·FCT-005] ; le chantier d'inclusion est européen, lent et daté (inaptitude 2018, recommandation BCE 2021, règlements 2016/792, 2023/1470, 2025/1182) [R-0446·F-04, F-05]. Contrefactuel 2021-2024 : incalculable en sources ouvertes (série publique arrêtée à 2018) — gap typé [R-1625·CLM-002 PARTIAL].

**La normalité européenne (verdict bonus)** : Royaume-Uni LFS 19,6 % de réponse et publications suspendues depuis 2024 ; Allemagne ~65 % ; France 60-77 % [R-0446·F-06, F-07, F-08, F-09]. La revue par les pairs a formulé 16 recommandations, **aucune** sur le champ IPC [R-0446·F-02]. Les griefs « défaillance française » et « les pairs contestent le champ » ne résistent pas à la comparaison.

**Caveats** : le verdict H1 repose sur une fondation inductive (à énoncer comme tel) ; le 34/40 Md€ EPL/SFIL sont des ordres de grandeur ; Unédic non désagrégée (reclassification vs Covid) ; les 2 partenaires de comparaison ne généralisent pas l'Europe.

**Interdits** : « l'Insee a été blanchi » (pas de procès) ; « tout est transparent » ; « la chance fiscale est un vent maquillé » (décomposée par le contrôleur) ; « 100 Md€ cachés » (bornes publiées cas par cas, jamais consolidées — c'est ça le grief) ; « les loyers imputés auraient plus fait monter l'inflation » (réfuté sur la période publiée).

---

## 6. Ce qui reste troué — les résidus typés GAP

**Fonction** : honnêteté asymétrique — ce qui tient n'excuse pas ce qui manque. Chaque trou est un GAP, pas un soupçon.

1. **Le tableau consolidé manquant** : ≥100 Md€ de marches statistiques de périmètre (entrées documentées cas par cas), aucun pont public annuel « dette : effets de périmètre » [RECL]. Le grief le plus concret du dossier.
2. **Les quality reports non publics** : produits pour Eurostat, pas toujours publiés — relevé par le contrôle lui-même [R-0446·F-03].
3. **La prévalence indéterminée des écarts de population** : Metzing + 8 communes des Alpes-Maritimes nommées (Peillon, Cantaron, Spéracèdes, Villeneuve-Loubet, Castellar, Saint-Martin-Vésubie, Cipières, Le Mas), refus de recomptage officiel, CNERP 3→2 ans fin 2026 ; **pas de dénominateur national** [R-1625·FCT-009 ; R-0428·F-06].
4. **La labellisation suspendue** : séries demandeurs d'emploi non labellisées du 01/01/2025 au 20/05/2026 (ASP : stabilité garantie « qu'à l'issue de la transition ») ; le chiffre fait la une, la suspension fait un paragraphe [R-0347·F-07]. Incident de publication T1 2013 documenté en 3 facteurs [R-0347·F-10].
5. **L'effet du contrôle non identifiable** : le cycle 2020-2025 ne formulait aucune exigence sur les taux de réponse → impossible d'attribuer les variations ; le contrôle agit sur le statut (labellisation), pas mesurablement sur les valeurs [R-0347·M1, M2].
6. **Les ruptures assumées** : ERFS 2021 (-0,3 pt pauvreté, Gini -0,007, niveaux rehaussés) ; imputations « fragilités » reconnues (2020) ; pauvreté facteur 5 selon le seuil (2,84 M à 40 % → 14,58 M à 70 %) [R-1921·F-03 ; R-1812·F-08, F-09].

**Caveats** : 9 communes = indicateur qualitatif, jamais un taux ; les ruptures sont chiffrées par le producteur (transparence a posteriori) ; l'absence de baromètre ménages est constatée dans le corpus, pas établie comme absence générale.

**Interdits** : « 9 communes = le recensement est cassé partout » ; « l'ASP a suspendu l'INSEE » (elle a suspendu la labellisation des séries, motif transition) ; « facteur 5 = mensonge » (conventions de seuil, publiées).

---

## 7. Le test final — la confiance conditionnelle

**Fonction** : la fin constructive. Le verdict falsifiable + la proposition.

**Faits/contenus** :
- Le verdict en trois phrases (mémoire consolidée 91b208a9) : confiance aux données comme mesures ; pas aux chiffres comme récits (convention choisie, médiation aveugle à l'incertitude) ; surtout pas sans vérification — la confiance n'est légitime que checkable.
- Les **quatre conditions de révocation** (falsifiables, écrites) : une réservation Eurostat publiée ; un échec de réplication du BIT dans le CASD ; un résidu > 0,3 % du PIB non tracé dans l'identité de la dette ; une asymétrie démontrée dans les vintages de révisions [PROT].
- Le protocole M1-M4 en 6 lignes : étalons indépendants (scanner, panier figé, réplication CASD, identité comptable) ; base de vintages (asymétrie signée, prédictibilité, benchmark UE) ; transparence des frontières (registre des périmètres, pont dette annuel, versionning méthodos, séries alternatives à égalité de visibilité) ; red team institutionnalisé au CASD, mandat « chercher la divergence, pas la confirmation ».
- La phrase de clôture : un institut honnête n'a rien à craindre d'un adversaire public, prévisible et journalisé — c'est le test final, et il reste à faire.

**Caveats** : le protocole automatise la détection et oblige à expliquer ; il ne détectera jamais des intentions ; les étalons ont leurs propres biais ; proposition = concurrencer Eurostat, pas s'y substituer.

**Interdits** : « il faut se méfier de l'INSEE » (bilan : confiance conditionnelle) ; présenter le protocole comme réquisitoire (il est le pendant constructive) ; conclure « au vu de tout cela, l'INSEE ment quand même » (aucun élément ne le soutient).

---

## RÈGLES MAÎTRESSES (à re-vérifier à l'audit multi-rôles)

1. **BORNES ≠ MESURES** : 9 800 €/an, ~34 Md€, ~40 Md€, ≥100 Md€, 5 Md€/pt, 0,3 Md€/dixième — toujours « de l'ordre de », jamais l'article défini de la précision.
2. **TIERS AFFICHÉS** : FCT-008 (610 Md€) cité uniquement avec périmètre et statut ⁅ ; 2,8-6 Md€ IR = thinktank corrodé ; 0,3 Md€/dixième = division arithmétique signalée.
3. **RATTRAPAGE TOUJOURS CO-PUBLIÉ** avec l'erreur (Metzing, RSA, révisions) : le système corrige lentement mais documente.
3 bis. **CITATIONS VERBATIM POUR LES CHIFFRES NON RECALCULABLES** (fiche précision ±17 500) : citer exactement, jamais reconstruire l'arithmétique derrière ; signaler l'agrégat non chiffré (« grandes communes ») si le texte le mentionne.
4. **LE GRIEF VRAI EST MATÉRIEL** (tableaux consolidés, reports publics, prévalence) — jamais intentionnel. ABSENCE ≠ CONCEALMENT.
5. **LA NORMALITÉ EUROPÉENNE GUERIT DEUX GRIEFS** (taux de réponse, champ IPC) mais n'excuse pas les défauts propres (agrégation, publication des rapports).
6. **TOUT CHIFFRE DE PAUVRETÉ PORTE SON SEUIL** ; tout écart de chômage porte sa définition (BIT/cat A/halo).
7. **LIAISON V2** : citer l'article du 21/09 pour formules et montants d'indexation ; zéro répétition.
8. **DUALITÉ DE SPINE ASSUMÉE** : 8,3 ± 0,3 en titre, Metzing en corps (§2, §3, §6) — l'arbitrage complet est dans le document séparé si besoin.
9. **ZÉRO CHIFFRE ORPHELIN** : tout chiffre emprunté au verdict consolidé ou aux audits du 22/09 et non couvert par une quintessence v3 est marqué « à re-sourcer » dans le plan — la séquelle ne publie aucun chiffre sans son run porteur.
10. **ATTRIBUTIONS EXACTES** : les refs entre crochets portent exactement les énoncés cités (audit du 22/09 : deux attributions de ce plan étaient fausses avant correction) — re-vérifier à chaque réécriture.

## APPENDICES prévus dans l'article

- A. Méthodo : 23 runs certifiés cités (14 campagne + 6 audits 22/09 + verdict), tiers et réfutations ; texte du audit MEDI et ses biais.
- B. Cartographie : un schéma « fabrique → conventions → argent → médiation → contrôle → trous ».
- C. Sources maîtresses : Focus 152 ; note révisions 3/06/2026 ; Cour des comptes 22/04/2026 ; FIPECO 04/2026 ; revue par les pairs 2021 + plan d'action mars 2022 ; rapport ASP 2024 ; QE Sénat 07446 ; réponse ministérielle Metzing ; Banque de France billet 253 ; BDM 001763530 ; OFGL Metzing ; **Trésor-Éco n°356 (prévisions 2023-2024, actualisé 16/07/2025)** ; **Insee ECRT « Sources et méthodes » (110 000 répondants/trimestre)** ; **fiche précision recensement (citation verbatim ±17 500)** ; **FIPECO « La prévision des dépenses publiques » (18/05/2026)**.
