---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis"
artifact_id: "INV-146-SYNTHESIS"
version: "1.0"
status: "final"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-146"
input_gate: "INV-146_SYNTHESIS_INPUT_GATE.md"
---

<!-- TRACE: synthesized_from=INV-019,INV-022,INV-026,INV-033,INV-128,INV-134,INV-138,INV-139,INV-140,INV-145 -->
<!-- EXECUTION: truth_engine_search=false; generic_collection=false; dependency_delta_only=true -->
<!-- GUARD: geopolitical_alignment!=mechanism; legal_design!=enforcement; vocabulary!=evidence; operation!=effect -->

# INV-146 — Asymétrie alliés/adversaires : mêmes mécanismes, mêmes standards de preuve, mêmes mots ?

## 1. Verdict

La thèse forte — **« les mêmes mécanismes sont systématiquement qualifiés, prouvés et sanctionnés différemment selon qu’ils viennent d’un allié ou d’un adversaire »** — n’est **pas démontrée** par le corpus disponible.

En revanche, une asymétrie plus précise est établie : **les cadres juridiques ne construisent pas tous le même objet d’“influence étrangère” et certains comportent des différences explicites de périmètre géographique ou de relation au mandant**. L’exemple le plus net est le contraste documenté par INV-145 entre FARA, le dispositif français et le cadre européen en construction. Cette asymétrie de design juridique ne prouve ni une application sélective, ni un standard probatoire plus faible contre les adversaires, ni une immunité de fait des alliés.

Le résultat central est donc :

```text
LEGAL_DESIGN_ASYMMETRY                = ESTABLISHED
MECHANISM-LEVEL ALLY/ADVERSARY BIAS   = NOT_ESTABLISHED
EVIDENTIARY_THRESHOLD_ASYMMETRY       = NOT_ESTABLISHED
SYSTEMATIC_VOCABULARY_ASYMMETRY       = NOT_ESTABLISHED
ENFORCEMENT_ASYMMETRY                 = NOT_ESTABLISHED
COMMON_FORENSIC_STANDARD              = SUPPORTED / OPERATIONAL
COUNTERFACTUAL_EFFECT_CEILING         = GENERALLY NOT_ESTABLISHED ACROSS CAMPS
```

Ce verdict n’est pas une conclusion d’égalité parfaite. Il signifie que **l’asymétrie démontrable à ce stade est surtout normative/juridique et de périmètre ; l’asymétrie d’application et de preuve reste une hypothèse à tester avec des cas appariés et des dénominateurs communs**.

## 2. Règle de comparaison

Une comparaison n’est admise que si les objets sont suffisamment isomorphes sur les dimensions suivantes :

```text
mécanisme
visibilité / clandestinité
consentement
base juridique
identité du financeur / client / mandant
relation à l'État
affectation des ressources
coordination / tasking / contrôle
cible
exposition
réception / persuasion
effet comportemental ou institutionnel
résultat contrefactuel
```

Conséquences :

```text
foreign != interference
ally != legitimate
adversary != hostile_operation_proven
legal != legitimate
funding != command
access != control
client_relation != state_tasking
operation_exists != result_changed
public_label != evidentiary_chain
legal_design_difference != selective_enforcement
```

Cette règle dérive directement des contrôles convergents d’INV-128, INV-134, INV-140 et INV-145.

## 3. Contrôle isomorphe n°1 — opérations clandestines / influence-for-hire

### Russie — INV-022

Plusieurs opérations liées à la Russie et visant la France ferment matériellement des arêtes `acteur/infrastructure -> action -> ciblage`; certaines branches disposent aussi d’une base de coordination ou d’attribution élevée. Mais l’exposition est hétérogène, parfois faible, et la persuasion, le changement de comportement et l’effet électoral restent non établis. Le corpus refuse donc de transformer une opération documentée en efficacité politique démontrée.

### Israël / opérateurs privés — INV-026 et INV-128

Le corpus ferme l’existence de mécanismes d’influence israéliens ouverts et de certaines relations financières précises. Il documente également Rokh Solis et Zero Zeno comme opérations liées à des opérateurs israéliens, avec portée faible dans les métriques disponibles, tandis que le commanditaire ultime reste non établi dans certains cas. Le financement ponctuel d’un événement ne devient pas un commandement général, et un acteur pro-israélien n’est pas automatiquement un proxy étatique.

### Émirats arabes unis / Alp Services — INV-033 et INV-128

Le noyau `client lié au renseignement émirati -> paiements/tasking -> Alp Services -> opérations/cibles` ferme I0-I3 beaucoup plus fortement que de simples indices de proximité. C’est un cas important car il montre qu’un partenaire étroit de plusieurs États européens peut présenter une chaîne clandestine matériellement comparable à des opérations attribuées à des adversaires. Mais la connaissance du client ultime par chaque intermédiaire, la portée et surtout l’effet politique restent variables ou non établis.

### France comme émetteur — INV-138

La France fournit un contrôle supplémentaire : influence ouverte, conditionnalité, moyens militaires informationnels, interventions directes et au moins un réseau trompeur lié à des individus associés à l’armée apparaissent dans le corpus. L’affiliation individuelle ne ferme cependant pas automatiquement le tasking institutionnel du réseau trompeur, et I5-I7 restent généralement ouverts.

### Résultat du contrôle

Sur les opérations clandestines ou trompeuses réellement comparables, le corpus **ne justifie pas deux standards de preuve**. Dans tous les camps, les mêmes plafonds réapparaissent : attribution du commanditaire, tasking précis, portée réelle, persuasion et effet contrefactuel.

Le cas UAE/Alp invalide en outre une règle simpliste du type `allié/partenaire -> absence d’opération clandestine`. À l’inverse, INV-022 invalide `adversaire + opération -> effet politique démontré`.

Ce que ce contrôle **ne démontre pas** : que les institutions, médias ou juridictions appliquent effectivement ces mêmes exigences avec la même fréquence et la même sévérité. Pour cela, il faudrait un corpus apparié de décisions/qualifications, pas seulement des enquêtes de mécanisme.

## 4. Contrôle isomorphe n°2 — promotion démocratique, médias, société civile, conditionnalité

### États-Unis — INV-019

L’architecture américaine de promotion de la démocratie est un écosystème public-financé et juridiquement structuré : State Department, NED, USAGM et partenaires financent ou soutiennent institutions, société civile, médias et processus électoraux. L’architecture, les ressources et les actions sont documentées ; un contrôle CIA actuel de l’ensemble n’est pas établi ; la persuasion et l’effet systémique ne peuvent pas être inférés des subventions, outputs ou audiences.

### Union européenne — INV-139, récupération bornée

Les faits persistés documentent des programmes de démocratie, société civile et médias, l’observation électorale et son suivi, le soutien à des acteurs politiques, la conditionnalité budgétaire/d’adhésion et des sanctions explicitement conçues pour provoquer un changement de politique ou d’activité. Certains dispositifs sont invités ; certains financements thématiques peuvent fonctionner sans approbation du gouvernement tiers ; la conditionnalité et les sanctions sont ouvertement coercitives.

### France — INV-138

La France combine elle aussi diplomatie publique, aide, médias internationaux, coopération institutionnelle, conditionnalité et, dans d’autres classes de cas, instruments plus coercitifs ou clandestins.

### Résultat du contrôle

Ces mécanismes démontrent que les démocraties occidentales **cherchent explicitement à modifier des institutions, capacités civiques, politiques ou environnements informationnels étrangers**. Mais cette propriété commune n’est pas suffisante pour les rendre isomorphes à une opération clandestine de faux comptes, hacking, infiltration ou renseignement privé.

La distinction pertinente est :

```text
OPEN + ATTRIBUTABLE + LEGALLY BASED + OFTEN CONSENTED
    !=
COVERT + DECEPTIVE + HIDDEN TASKING
```

Le premier ensemble est bien de l’influence. Il peut être coercitif lorsqu’il passe par sanctions ou conditionnalité. Il ne devient pas automatiquement « ingérence clandestine » parce qu’il vient d’un État étranger. Inversement, son caractère occidental, légal ou déclaré ne suffit pas à établir sa légitimité normative ni l’absence d’effet politique.

Cette distinction réduit un faux positif majeur dans le débat d’asymétrie : comparer une subvention publique déclarée à une ferme de faux comptes clandestine ne teste pas un double standard ; cela compare deux mécanismes différents.

## 5. Contrôle isomorphe n°3 — financement étranger de l’espace électoral

INV-140 impose la chaîne :

```text
origine ultime
-> véhicule
-> affectation électorale
-> coordination/tasking
-> exposition
-> réception/comportement
-> résultat contrefactuel
```

Best for Britain illustre une chaîne où le financement amont et l’activité électorale sont tous deux documentés sans que l’affectation comptable précise du premier vers la seconde soit fermée. Voice of Europe présente une chaîne plus forte de ressources désignées et de soutien clandestin rapporté à des acteurs politiques. Avaaz fournit au contraire un contrôle d’intervention électorale transnationale ouverte sans tasking étatique démontré.

Le résultat est directement pertinent pour l’asymétrie alliés/adversaires : **la nationalité du financeur ou du véhicule ne permet pas de sauter l’arête d’affectation/tasking**. Le même test doit valoir pour une fondation américaine, un réseau russe, une organisation transnationale ou un véhicule domestique alimenté depuis l’étranger.

Cela ne prouve pas que ce test soit appliqué avec la même intensité à tous les acteurs. Cela définit le standard probatoire minimal qui permettrait de le mesurer.

## 6. Attribution — le label ne remplace jamais la chaîne

INV-134 fournit le contrôle transversal le plus important. L’attribution doit rester un graphe :

```text
incident
-> artefact
-> opérateur
-> intermédiaire
-> commanditaire / État
-> tasking / intention
-> exposition
-> effet
```

Les cas étudiés montrent que certaines attributions publiques ferment seulement les arêtes techniques/opérateurs, d’autres montent plus haut vers le commanditaire, et que la force peut varier au cours du temps. Une déclaration officielle ou un démenti officiel reste un claim dont la valeur dépend des éléments publics disponibles.

Par conséquent, mesurer une asymétrie probatoire exige de comparer **le niveau de chaîne effectivement fermé avant attribution publique**, pas seulement le nombre de fois où le mot « ingérence » apparaît.

## 7. Asymétrie juridique : démontrée, mais bornée

INV-145 établit une différence réelle entre FARA, le dispositif français et le projet européen. Le périmètre du principal/mandant/sponsor, les exemptions et les activités couvertes ne sont pas identiques. Le régime français examiné exclut notamment du mandant étranger certaines relations relevant des États membres/partis de l’Union, ce qui constitue une asymétrie géographique légale réelle.

C’est le résultat le plus fort d’INV-146 : **deux conduites matériellement proches peuvent entrer dans des catégories légales différentes selon le régime et l’origine du mandant**.

Mais trois inférences restent interdites :

```text
différence_de_droit != injustice démontrée
différence_de_périmètre != application sélective
exemption/allègement juridique != absence d'influence réelle
```

L’asymétrie d’enforcement n’est pas mesurable proprement avec les données actuelles : FARA dispose d’un historique long ; le registre français est récent ; le cadre européen n’est pas final/mature. Les dénominateurs de conduites exposées, détectées, poursuivies et sanctionnées ne sont pas comparables.

## 8. Les « mêmes mots » : question encore sous-documentée

Le corpus contient des qualifications institutionnelles et journalistiques multiples, mais il n’a pas été construit comme un échantillon systématique de vocabulaire apparié.

On ne peut donc pas défendre à ce stade :

```text
ALLIES systematically called "influence/lobbying"
ADVERSARIES systematically called "interference/disinformation"
```

comme résultat démontré.

Des cas du corpus vont d’ailleurs contre une version absolue de cette hypothèse au niveau mécanistique : des opérations liées à des acteurs israéliens ou émiratis satisfont analytiquement des critères d’opération clandestine lorsque les arêtes sont documentées ; inversement, les opérations russes ne permettent pas de promouvoir automatiquement leurs effets au niveau I5-I7. Cela ne constitue pas une mesure du vocabulaire public effectivement employé.

Pour mesurer réellement l’asymétrie lexicale, il faut un corpus de sorties comparables `acteur + mécanisme + niveau de preuve + institution/média + label + date`, avec cas alliés, adversaires et domestiques appariés.

## 9. Sanctions et enforcement : non démontrés comme asymétriques par camp

Le corpus établit l’existence de régimes de transparence, sanctions, désignations et mesures restrictives. Il ne fournit pas un dénominateur permettant de calculer, à conduite comparable :

```text
probabilité d'enquête
probabilité de qualification publique
probabilité d'enregistrement obligatoire
probabilité de poursuite
probabilité de sanction
sévérité de sanction
```

selon `allié / adversaire / domestique`.

L’absence de ce dénominateur interdit une conclusion robuste d’enforcement sélectif. Le fait qu’un régime juridique ait un périmètre différent est une donnée ; le fait qu’il sanctionne systématiquement davantage un camp qu’un autre reste une hypothèse.

## 10. Le comparateur domestique reste insuffisant

La question canonique inclut les acteurs domestiques. Les dix dépendances fournissent plusieurs véhicules domestiques, intermédiaires locaux et mécanismes transnationaux, mais **pas un corpus apparié suffisamment riche de conduites purement domestiques réalisées selon les mêmes mécanismes**.

Il est donc possible de contrôler les arêtes `financement -> véhicule -> tasking -> action -> effet`, mais pas de mesurer proprement un ratio `même conduite étrangère vs domestique -> qualification/sanction`.

Ce manque ne renverse pas le verdict alliés/adversaires ; il borne la portée de la troisième branche de la question.

## 11. Modèles concurrents

### M1 — Double standard géopolitique général

Prédiction : à mécanisme et preuve comparables, les adversaires seraient plus facilement qualifiés/sanctionnés et les alliés requalifiés en diplomatie/lobbying.

**Statut : NOT_ESTABLISHED.** Le corpus ne possède ni échantillon apparié suffisant de labels/enforcement ni dénominateurs. Des contre-exemples mécanistiques existent côté partenaires/alliés.

### M2 — Qualification principalement déterminée par les propriétés du mécanisme

Prédiction : clandestinité, tromperie, tasking, coercition, affectation et preuve de l’action expliquent une part importante des différences de qualification.

**Statut : SUPPORTED.** C’est le modèle le plus compatible avec les contrôles transversaux INV-128/134/140 et les cas Russia/Israel/UAE/France/US/EU, sans prétendre expliquer toute pratique institutionnelle réelle.

### M3 — Asymétrie surtout institutionnalisée dans le droit et les périmètres

Prédiction : certaines différences de traitement existent avant même l’enforcement parce que les catégories juridiques ne couvrent pas les mêmes mandants, origines et activités.

**Statut : ESTABLISHED sur le design, pas sur l’enforcement.** INV-145 ferme cette différence de périmètre, mais pas une sélectivité empirique d’application.

### M4 — Modèle mixte

Les propriétés du mécanisme structurent la qualification, tandis que droit, alliances, institutions et contexte politique peuvent modifier les catégories disponibles ou l’attention portée aux cas.

**Statut : PLAUSIBLE / PARTIAL.** Le volet juridique est démontré ; le volet d’attention/enforcement demande des données supplémentaires.

## 12. Conclusion technique

La synthèse ne valide ni « toute influence étrangère est une ingérence », ni « seuls les adversaires font l’objet d’un standard sévère », ni « les alliés sont traités exactement comme les adversaires ».

Elle établit quelque chose de plus précis :

1. **les mêmes propriétés forensiques peuvent et doivent être appliquées à tous les camps** ;
2. **des alliés/partenaires et des démocraties occidentales exercent eux aussi des formes documentées d’influence, parfois coercitives ou clandestines** ;
3. **cela ne rend pas isomorphes des mécanismes ouverts/consentis et des opérations clandestines/trompeuses** ;
4. **l’effet politique ou électoral contrefactuel reste presque partout beaucoup moins démontré que l’existence de l’opération ou de l’instrument** ;
5. **une asymétrie juridique de périmètre est réellement démontrée** ;
6. **une asymétrie systématique de vocabulaire, de seuil de preuve et de sanction selon l’alliance géopolitique reste non établie**.

Le test à retenir pour la suite du programme n’est donc pas `allié/adversaire`, mais :

```text
à mécanisme isomorphe + niveau de preuve comparable,
le label, la charge de preuve et la conséquence institutionnelle changent-ils ?
```

C’est ce test, et non une comparaison de pays ou de mots isolés, qui doit alimenter INV-133.

## 13. Résiduels terminaux

```text
P0 = 0
P1 = 0
P2 = 4
```

1. **VOCABULARY DATASET** — absence de corpus systématique de labels institutionnels/médiatiques appariés par mécanisme et niveau de preuve.
2. **ENFORCEMENT DENOMINATORS** — absence de dénominateurs comparables France/UE/FARA et par camp géopolitique.
3. **DOMESTIC CONTROL** — comparateur domestique pur insuffisamment représenté dans les dix dépendances.
4. **RECOVERY PROVENANCE** — INV-139 et INV-140 reposent pour cette synthèse sur des handoffs de récupération bornés ; aucun détail absent n’a été reconstruit.

Ces résiduels ne justifient pas une collecte générique immédiate. Les trois premiers exigent un design comparatif dédié ; le quatrième est un problème de persistance déjà circonscrit.

## 14. Routing

```text
MERGE -> INV-133 :
  - LEGAL_DESIGN_ASYMMETRY = ESTABLISHED
  - SYSTEMATIC_ALLY_ADVERSARY_EVIDENTIARY_BIAS = NOT_ESTABLISHED
  - ENFORCEMENT_ASYMMETRY = NOT_ESTABLISHED
  - MECHANISM_PROPERTY_MODEL = SUPPORTED
  - EFFECT_CEILING = I5-I7 generally weak/not established

RECHECK -> only if:
  - matched vocabulary/enforcement dataset exists,
  - mature French/EU enforcement denominators become available,
  - materially stronger domestic isomorphic controls are produced.
```
