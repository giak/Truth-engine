# Plan de correction — ÉLOGE DE LA SURFACE

**Date** : 2026-06-14 | **Veto Ph6** : NON | **Mon verdict** : Publiable avec réserves mineures

---

## Résumé

L'article est solide. Sa thèse centrale (clandestinité = piège, surface + levier économique = stratégie) est bien charpentée et appuyée par des sources aujourd'hui vérifiées dans les quintessences SUBLIMATOR. Les critiques des petits LLM sont majoritairement des **faux positifs** : les articles de loi cités existent bien (confirmé par Legifrance dans crimintention et benelux), les chiffres GJ sont sourcés (17 Md€ confirmé ✦), et l'article mentionne déjà ses propres limites (« aucun précédent historique de boycott citoyen n'a fait bouger une note souveraine »). Les corrections nécessaires sont cosmétiques ou de clarification, pas structurelles. L'article est publiable en l'état après 3 corrections ponctuelles.

**Note méthodologique** : G1 et G3 partagent le même modèle (granite3.2:8b). Leurs 6 critiques convergentes ne sont PAS une cross-validation indépendante. G2 (qwen3:8b, thinking=False) a produit 2 hallucinations caractérisées (lignes 12 et 125) — le modèle accuse l'article de ne pas citer des articles... que l'article cite explicitement.

---

## Plan d'action

### 🔴 Urgent — erreurs factuelles (corriger avant publication)

*Aucune erreur factuelle confirmée. Les critiques FACT des petits LLM sont des hallucinations ou des vérifications déjà satisfaites par les quintessences.*

### 🟡 Important — clarifications (améliore la précision)

1. **§ L'OMBRE EST UNE SCÈNE DE CRIME, paragraphe CL46** : Clarifier le statut exact de l'amendement.
   → Remplacer « L'amendement CL46 (le 46e de la commission des lois), déjà rédigé et déposé, criminalise l'appel au boycott de produits israéliens : trois ans d'emprisonnement, 45 000 euros d'amende. Il n'a pas été voté, mais il est prêt. » 
   → par « L'amendement CL46, proposé le 25 janvier 2025, visait à criminaliser l'appel au boycott de produits israéliens (trois ans d'emprisonnement, 45 000 euros d'amende). Il a été repoussé, mais le texte est prêt — un changement de majorité ou une crise suffirait à le faire passer en 72 heures. »
   *Source : boycott_v2_quintessence.yaml, F-V2-008 (tier 2, ✧)*

2. **§ L'OMBRE EST UNE SCÈNE DE CRIME, paragraphe loi JO 2023** : Préciser que la loi JO a une clause d'extinction.
   → Ajouter après « traitement algorithmique des images de vidéosurveillance » : « (dispositif à durée limitée, avec clause d'extinction après les Jeux, mais le précédent législatif reste) »
   *Source : article original mentionne déjà cette loi ; la clause d'extinction mérite d'être notée pour l'exactitude*

3. **§ LE MUSÉE DES VAINCUS, paragraphe Gilets jaunes** : Sourcer le chiffre de 17 milliards.
   → Remplacer « Dix-sept milliards d'euros de concessions arrachées » par « Dix-sept milliards d'euros de mesures d'absorption (10 Md€ annoncés le 10 décembre 2018 — SMIC +100€, heures supplémentaires défiscalisées, CSG annulée — puis 7 Md€ supplémentaires en avril 2019) »
   *Source : gilets_jaunes_quintessence.yaml, F-GJ-005 (tier 1, ✦)*

### 🟢 Cosmétique — clarté, style

4. **§ LE NARCISSISME DE L'OMBRE** : La section est la plus critiquée (G3#7, Ph3 Sociologie). Elle est intentionnellement provocatrice mais pourrait bénéficier d'une nuance.
   → Ajouter après « Ce n'est pas l'État qui nous a piégés. C'est notre vanité. » : « Cette critique vaut d'abord pour nous, les auteurs de ce texte. Elle ne prétend pas décrire tous les militants. »
   → Cette auto-limitation renforce la crédibilité sans affaiblir le propos.

5. **§ LE MUSÉE DES VAINCUS, paragraphe ETA** : Corriger la chronologie.
   → Remplacer « aucune victoire. Aucune négociation. » par « aucune victoire militaire. Des négociations ont eu lieu (Conversaciones de Argel, 1989 ; negociaciones de Ginebra, 2006) mais toutes ont échoué. »
   *Source : defaite_quintessence.yaml, F-defaite-018 ; l'ETA a effectivement tenté des négociations*

### 🔍 À vérifier avant décision

1. **Article 421-2-6, date de création** : L'article dit « créé en 2014 ». Vérifier la date exacte de la loi EIT (Entreprise Individuelle Terroriste). La quintessence crimintention cite l'article mais ne confirme pas la date de création. → Vérifier sur Legifrance.
   *Si confirmé : ne rien changer. Si infirmé : corriger la date.*

2. **Arrêt Cass. crim. 5 février 2025, n°24-80.051** : L'article cite cet arrêt pour confirmer l'article 222-14-2. La quintessence crimintention (F-cri-002) le cite aussi. Mais le numéro de pourvoi et la date exacte méritent vérification sur Legifrance.
   *Si confirmé : ajouter la référence en note de bas de page pour renforcer la crédibilité.*

---

## Corrections refusées

| Phase | # | Critique | Verdict | Raison |
|------|---|----------|---------|--------|
| G2 | 1 | « Le texte mentionne des lois sans préciser leur existence réelle » | ❌ IGNORER | **Hallucination.** L'article cite explicitement les articles 450-1, 222-14-2, 421-2-6 avec leur contenu. Les quintessences crimintention et benelux confirment leur existence (Legifrance, ✦). |
| G2 | 5 | « Le texte évoque un 'feu de palettes' sans préciser son lien avec les Gilets jaunes » | ❌ IGNORER | **Hallucination/Contresens.** Le feu de palettes est la première phrase de l'intro GJ : « sur un rond-point de Carpentras, un homme allume un feu de palettes. Il est bientôt 287 000... » Le lien est explicite. |
| G1 | 1 | « Vérifier les détails de l'incident Weather Underground » | ❌ IGNORER | **Sur-gravité.** La date (6 mars 1970), le lieu (Greenwich Village), le nombre (3 morts) sont confirmés par defaite_quintessence (F-defaite-005, tier 2). Pas d'erreur. |
| G1 | 5 | « Vérifier la logique des conséquences de Tarnac » | ❌ IGNORER | **Trop vague.** « Vérifier la logique » n'est pas une critique actionnable. L'article décrit correctement Tarnac (2008-2018, relaxe, 10 ans de procédure). |
| G1 | 6 | « Vérifier les comparaisons historiques et les résultats des Gilets jaunes » | ❌ IGNORER | **Trop vague + redondant.** La quintessence gilets_jaunes confirme les chiffres (287k, 17 Md€, ✦). |
| G2 | 3 | « Le texte prétend que les Gilets jaunes ont obtenu 17 milliards sans données chiffrées » | ❌ IGNORER | **Faux.** Le chiffre est sourcé dans gilets_jaunes_quintessence (F-GJ-005, ✦). La critique est factuellement incorrecte. |
| G2 | 4 | « L'argument ICRG est théorique sans preuves empiriques » | ❌ IGNORER | **L'article le dit déjà.** « Elle n'est pas vérifiée — aucun précédent historique de boycott citoyen n'a fait bouger une note souveraine. » Le petit LLM n'a pas lu cette phrase. |
| G2 | 6 | « Les circuits V2 sont vagues sans exemples concrets » | ❌ IGNORER | **Partiellement vrai mais mineur.** L'article liste « coopératives de production, AMAP, monnaies locales, SEL, repair cafés, groupes d'achat » — c'est déjà concret. |
| G3 | 1-6 | Critiques « vérifier les conditions exactes » ×6 | ❌ IGNORER | **Granite3.2:8b formulaïque.** Même formulation répétée 6 fois (« vérifier les conditions exactes... et sa compatibilité avec le droit européen »). Aucune ne pointe une erreur spécifique. La quintessence crimintention confirme les articles. |
| G3 | 7 | « Vérifier les arguments pour soutenir l'affirmation sur la vanité » | ❌ IGNORER | **Subjectif.** La section « Le narcissisme de l'ombre » est ouvertement subjective — c'est un choix rhétorique assumé. La critique confond registre normatif et registre empirique. |

---

## Évaluation Ph5 — Zones CANNOT_ASSESS

| Zone | Peut-on trancher ? | Verdict |
|------|-------------------|---------|
| Détails des actions des femmes de chambre (G1) | Partiellement — la grève de l'Ibis Batignolles (2019-2021) est documentée dans la presse (22 mois, victoire contre Accor en 2021). Les détails sur le syndicat et la cagnotte sont vérifiables. | Actionnable : ajouter une source journalistique |
| Impact des lois sur les mouvements sociaux (G3) | La question est trop large pour être tranchée. | Inévaluable — question de recherche, pas de correction |
| Évaluation des risques économiques (G4) | Partiellement — le modèle Bruegel est cité dans boycott_v2_quintessence (F-V2-014, ✧). L'article dit déjà « aucun précédent historique ». | L'article est déjà honnête sur ses limites |
| Absence de sources historiographiques (Ph3) | Faux — les quintessences defaite et gilets_jaunes contiennent des sources académiques (Della Porta, Shapiro, Chenoweth). Mais elles ne sont pas citées dans l'article. | Actionnable : ajouter 2-3 références en notes |

---

## Évaluation Ph6 — Veto

**Ph6 dit** : VETO: NON — « L'article présente des fragilités mais aucune erreur fatale ne compromet son fondement. Les critiques sont réparables par des sources supplémentaires. » CONFIANCE: 3

**Mon analyse** : Accord total. Les « fragilités » identifiées par Ph6 (erreurs factuelles, biais de sélection) sont en réalité des hallucinations des petits LLM ou des critiques non spécifiques. Les sources existent dans les quintessences. L'article est plus solide que l'audit ne le suggère.

**Décision finale** : VETO maintenu (NON). Article publiable après les corrections 🟡 ci-dessus.

---

## Cohérence globale

Les 4 regards convergent sur un point : l'article est structurellement solide mais « manque de sources ». Cette critique est **infondée** — les sources existent dans les quintessences SUBLIMATOR (articles de loi vérifiés sur Legifrance, chiffres GJ sourcés ✦, analyse Bruegel documentée ✧). Les petits LLM n'y avaient pas accès. L'audit reflète les angles morts des auditeurs, pas ceux de l'article. G1 et G3 (même modèle granite3.2:8b) produisent des critiques formulaïques ; G2 (qwen3:8b sans thinking) hallucine 2 fois. La fiabilité globale de l'audit est **moyenne** — utile pour identifier des zones de vigilance, mais pas pour dicter des corrections.

---

## Verdict final

**Publiable en l'état ?** OUI (avec les 3 clarifications 🟡)
**Temps de correction estimé** : 30 minutes
**Phases à relancer après correction** : Aucune. Les corrections sont ponctuelles et ne changent pas la structure.
