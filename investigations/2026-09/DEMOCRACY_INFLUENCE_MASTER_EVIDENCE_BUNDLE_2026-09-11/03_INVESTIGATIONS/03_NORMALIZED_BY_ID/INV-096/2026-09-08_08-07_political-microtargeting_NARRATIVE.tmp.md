# INV-096 — Microtargeting électoral et données personnelles en France/UE

## Résultat central

Le microtargeting politique est un mécanisme réel, mais son effet est beaucoup plus borné que son imaginaire public. Les régulateurs documentent l’usage de données et de techniques de ciblage par des partis et campagnes ; la publicité politique numérique française de 2022 fournit un terrain observable ; et les plateformes ont historiquement fourni des outils de ciblage et de transparence. Cela suffit à établir capacité et usage. Cela ne ferme pas la chaîne jusqu’au vote.

La frontière décisive est : **données != ciblage != delivery != exposition != persuasion != comportement/vote != résultat électoral**. Le corpus ferme bien les premières arêtes dans certains contextes, fournit des résultats expérimentaux mixtes sur la persuasion, et ne ferme pas de manière générale les deux dernières.

## Capacité et pratique

L’ICO décrit explicitement le microtargeting comme l’usage de méthodes d’analyse de données par des partis et groupes de campagne pour adresser des messages spécifiques à de petits groupes ou individus (FCT-030/FCT-031). La CNIL constate parallèlement l’importance croissante des données personnelles dans la prospection politique française (FCT-005). Ces éléments établissent l’existence opérationnelle du mécanisme, pas son efficacité.

La présidentielle française de 2022 offre un cas numérique observable : l’étude Sosnovik et al. analyse un corpus de publicités politiques sur Meta (FCT-018/FCT-019). Mais une distribution démographique d’impressions ne permet pas, seule, de reconstituer les paramètres choisis par l’annonceur, car l’optimisation de delivery peut contribuer à cette distribution (FCT-020).

## Rupture de régime en octobre 2025

Il serait incorrect d’extrapoler directement l’écosystème 2022 à 2026. La CNIL indique que le règlement européen sur la transparence de la publicité politique s’applique depuis octobre 2025 et renforce consentement, collecte et transparence (FCT-001 à FCT-004). Meta a fermé les publicités politiques, électorales et sociales payantes dans l’UE à partir d’octobre 2025 tout en maintenant les contenus organiques (FCT-013/FCT-014). Google a lui aussi annoncé l’arrêt de la publicité politique dans l’UE avant l’entrée en vigueur du nouveau cadre (FCT-016/FCT-017).

Les municipales 2026 se déroulent donc dans un environnement différent. La CNIL recense 739 signalements et 81 plaintes, principalement autour de canaux directs de prospection (FCT-008 à FCT-010). Ces chiffres prouvent une activité de prospection et de contrôle ; ils ne sont ni un taux de microtargeting ni une mesure de fraude.

## Persuasion : effets hétérogènes

Les expériences rapportées par MIT/PNAS fournissent un contrôle positif : sélectionner un message selon un attribut de l’audience peut, dans certains contextes, améliorer substantiellement la persuasion par rapport au meilleur message unique (FCT-025). Mais l’ajout de plusieurs attributs n’apporte pas de gain supplémentaire et l’avantage varie selon les sujets et les designs (FCT-026/FCT-027).

Le comparateur Oxford 2024 va dans l’autre sens pour le microtargeting par LLM : les messages GPT-4 sont persuasifs en moyenne, mais le microciblage individuel n’est pas statistiquement supérieur aux messages non microciblés en agrégé (FCT-028/FCT-029). La conclusion est donc contextuelle : sophistication du profil != puissance persuasive générale.

## De la publicité au vote : chaîne non fermée

Le contrôle causal le plus massif du corpus est l’expérience de retrait de publicités politiques avant l’élection américaine de 2020 : 36 906 utilisateurs Facebook et 25 925 utilisateurs Instagram sont randomisés (FCT-021). La plupart des publicités présidentielles visaient les propres soutiens des partis (FCT-022), mais aucun effet détectable du retrait n’apparaît sur connaissance, polarisation, légitimité perçue, participation, faveur envers les candidats ou turnout (FCT-023).

Cette expérience ne teste pas un contraste pur microciblage versus message générique (FCT-024). Elle interdit néanmoins de convertir automatiquement l’existence d’un marché de publicité ciblée en effet électoral massif. La House of Lords souligne aussi la difficulté à mesurer un effet sur le vote (FCT-032/FCT-033).

## Qualification démocratique

Le microtargeting est une technique d’influence et de persuasion. Il peut devenir problématique lorsque les données sont obtenues ou réutilisées illicitement, lorsque le ciblage est opaque, lorsque des messages contradictoires sont distribués selon les segments ou lorsqu’un sponsor est dissimulé. Mais personnalisation != manipulation et usage de campagne != ingérence étrangère. La sanction CNIL liée à la campagne 2022 illustre cette gradation : un manquement d’information dans la prospection est établi (FCT-011/FCT-012), sans établir persuasion, fraude ou changement de vote.

## Plafond I0–I7

- I0 VERIFIED : acteurs, règles, plateformes et techniques identifiés.
- I1 VERIFIED : capacité de collecter/segmenter/cibler et infrastructure de diffusion établies.
- I2 VERIFIED : usage de techniques de ciblage/prospection et publicité politique numérique documenté.
- I3 PARTIAL : paramètres exacts choisis par l’annonceur pas toujours séparables du delivery algorithmique.
- I4 VERIFIED/PARTIAL case-specifically : exposition/delivery observable dans certains datasets/expériences.
- I5 PARTIAL : persuasion causale dans certains designs, absente ou non supérieure dans d’autres.
- I6 NOT_ESTABLISHED generally : changement de comportement ou de vote non généralisable.
- I7 NOT_ESTABLISHED : aucun effet causal général sur le résultat électoral établi.

## Résidu matériel

Un nouvel effort ne changerait le modèle que s’il apporte des exports de campagnes/prestataires montrant les paramètres réels de ciblage, des données séparant choix annonceur et optimisation plateforme, ou un design causal France/UE reliant assignation de ciblage, exposition réelle, persuasion, vote et résultat. Une recherche générique supplémentaire sur Cambridge Analytica ou la puissance supposée des données serait cumulative.
