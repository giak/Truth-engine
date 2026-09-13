# INV-111 — Économie de l’indignation : attention, ranking et effets politiques

## Objet
Tester si les systèmes médiatiques et plateformes récompensent structurellement les contenus négatifs ou conflictuels, puis distinguer quatre arêtes qui sont souvent confondues : `contenu -> attention`, `feedback -> production/expression`, `ranking -> exposition/engagement`, et `exposition -> attitude/comportement politique`.

## Résultat central
**FACT.** Des essais randomisés sur les titres Upworthy établissent qu’une formulation plus négative augmente causalement le clic : pour un titre de longueur moyenne, un mot négatif supplémentaire accroît le CTR d’environ 2,3 % (FCT-001). Le dispositif même d’A/B testing montre qu’un éditeur peut sélectionner les formulations maximisant la consommation (FCT-002).

**FACT.** Sur Twitter, des travaux combinant données longitudinales et expériences preregistrées montrent que le feedback social positif reçu après une expression d’indignation augmente la probabilité d’expressions d’indignation futures ; les normes du réseau modulent également cette expression (FCT-003, FCT-004).

**INFERENCE.** Ces deux blocs ferment un mécanisme d’**incitation à l’attention et d’apprentissage expressif**. Ils ne ferment pas une manipulation politique : clic, engagement et expression ne sont ni croyance, ni persuasion, ni mobilisation.

## Ranking, exposition et engagement
**FACT.** Dans l’expérience Facebook/Instagram 2020, remplacer les fils algorithmiques par un ordre chronologique réduit substantiellement le temps passé et l’activité, et modifie le contenu exposé (FCT-005). Cela ferme une arête `ranking -> exposition/engagement`.

**FACT.** Pourtant, malgré ces changements de consommation, les principaux indicateurs d’attitudes politiques et de polarisation restent sans effet significatif détectable pendant l’expérience (FCT-006). La désactivation de Facebook/Instagram réduit surtout la participation politique en ligne, sans effet significatif sur le turnout validé (FCT-007).

**FACT.** Le contrôle YouTube va dans le même sens : des recommandations expérimentalement plus partisanes changent les contenus consommés, mais ne produisent pas d’effet cohérent substantiel sur les attitudes à court terme dans quatre expériences naturalistes (FCT-010).

## Contre-exemple positif : X
**FACT.** Une expérience de terrain publiée en 2026 sur X observe qu’un fil algorithmique, comparé à un fil chronologique, augmente l’engagement et déplace plusieurs opinions politiques vers des positions plus conservatrices (FCT-008). L’analyse du mécanisme montre davantage de contenu conservateur, moins de médias traditionnels et davantage de follows vers des comptes militants conservateurs (FCT-009).

**INFERENCE.** L’arête `ranking -> exposition -> certains changements d’attitudes` peut donc être causalement fermée dans au moins un contexte contemporain. Le contraste avec Meta et YouTube interdit toutefois de l’universaliser : l’effet est **platform-specific, intervention-specific et horizon-specific**.

## Asymétries de recommandation, intention et manipulation
**FACT.** Les audits TikTok trouvent des asymétries partisanes systématiques de recommandation dans la campagne américaine 2024, même après ajustement sur certaines métriques d’engagement (FCT-012). Les audits YouTube trouvent de la congruence idéologique dans les recommandations, mais pas une montée générale de l’extrémisme le long des parcours, même si certaines chaînes problématiques deviennent plus fréquentes dans certains parcours (FCT-013).

**FACT.** La Commission européenne a demandé à X des documents internes et informations techniques sur son système de recommandation dans le cadre du DSA (FCT-011). Cette intervention montre que le ranking est traité comme un objet de risque systémique auditable ; elle ne constitue pas une preuve de manipulation politique intentionnelle.

**INFERENCE.** Une asymétrie de sortie ne suffit pas pour inférer un objectif politique. Il faut encore fermer `intention/tasking -> paramétrage -> exposition -> effet`.

## Verdict
1. `négativité -> attention/clic` : **établi causalement**.
2. `feedback/normes -> expression future d’indignation` : **établi**.
3. `ranking -> exposition/engagement` : **établi**.
4. `ranking -> attitude politique` : **établi dans certains cas, non universel** ; X fournit un résultat positif, Meta et YouTube des contrôles nuls ou limités.
5. `économie de l’indignation -> manipulation politique intentionnelle` : **non démontré comme modèle général**.
6. `viralité/engagement -> mobilisation électorale` : **non fermé**.

Le modèle le plus robuste n’est donc ni « les algorithmes ne font rien » ni « l’indignation est mécaniquement une arme politique ». Il est à étages : les systèmes d’attention récompensent certains contenus et expressions ; le ranking modifie effectivement l’exposition ; mais la conversion en opinion ou comportement politique dépend fortement de la plateforme, du mécanisme, du public et de l’horizon temporel.
