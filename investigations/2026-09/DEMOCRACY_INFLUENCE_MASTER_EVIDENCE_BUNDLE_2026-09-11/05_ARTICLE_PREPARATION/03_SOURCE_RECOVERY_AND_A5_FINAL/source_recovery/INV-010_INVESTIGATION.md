---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "investigation_report"
artifact_id: "INV-010-INVESTIGATION"
version: "1.0"
status: "forensic_final_runtime_degraded"
updated: "2026-09-05"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-010"
runtime_certification: "unavailable_missing_truth_engine_helpers"
method_pack: "0.3"
---

<!-- TRACE: generated_from=INV-010_RUN_CARD.md; execution=actual_web+files; truth_engine_runtime_helpers=missing -->
<!-- GATE: scope=Italy_1948+Chile_1964+Chile_1970; no_other_INV_launched=true -->

# INV-010 — CIA et élections étrangères : Italie 1948, Chili 1964/1970

## Statut

**Forensic final utilisable / runtime Truth Engine non certifiable.**

Le `KERNEL.md` v2.10.6 a été utilisé comme doctrine d'enquête avec `METHOD_PACK v0.3`. Le ZIP Truth Engine fourni ne contient cependant pas les helpers runtime nommés par le KERNEL (state manager, renderer/verifier, persistance MnemoLite). Ce dossier ne prétend donc pas avoir passé mécaniquement G0–G10 ni reproduire les registres canoniques `QRY/SRC/FCT/CAU/ACT`.

<!-- DECISION: certification=DEGRADED_RUNTIME; reason=missing_helpers; evidence_work=real_not_simulated -->

# 1. RÉSUMÉ EXÉCUTIF

La question se sépare en deux problèmes :

1. **Les États-Unis ont-ils matériellement tenté d'influencer des élections étrangères, parfois clandestinement ?**
2. **Ces interventions ont-elles changé le vainqueur ou le résultat politique final ?**

Sur le premier point, les trois cas étudiés apportent une réponse nette : **oui**. Les archives américaines établissent des interventions politiques et électorales explicites en Italie en 1948 et au Chili en 1964 et 1970 : financement, soutien organisationnel, propagande, pression politique, opérations clandestines et, après le scrutin chilien de 1970, soutien à une stratégie visant à empêcher l'accession d'Allende par un coup.

Sur le second point, le niveau de preuve chute fortement.

**Italie 1948.** L'intervention américaine, ouverte et clandestine, est établie. La DC obtient 48,5 % des voix. Mais les travaux historiques consultés ne permettent pas de réduire sa victoire au financement clandestin américain : Église catholique, aide économique/Marshall Plan, climat anticommuniste et stratégie de De Gasperi constituent des causes concurrentes substantielles. Le contrefactuel « sans Washington, le Front populaire gagnait » reste non démontré.

**Chili 1964.** C'est le cas le plus fort pour une influence électorale directe. L'aide financière et organisationnelle, la propagande massive et le financement américain de la campagne Frei sont documentés. Les propres évaluations américaines disent que l'aide fut un ingrédient important et qu'en son absence Frei aurait au mieux obtenu une faible pluralité. Cela soutient fortement un effet sur **la marge et la majorité absolue** ; cela ne démontre toujours pas que l'intervention a changé **l'identité du vainqueur**.

**Chili 1970.** La CIA mène une opération de « spoiling » anti-Allende. Allende arrive pourtant premier avec 36,3 % contre 34,9 % pour Alessandri : l'objectif électoral immédiat d'empêcher sa pluralité échoue. Après le vote, les documents Track II établissent un niveau qualitativement différent : politique clandestine visant explicitement à provoquer un coup, contacts avec des comploteurs, encouragement à coordonner des groupes et livraison de matériel/armes. Allende est néanmoins confirmé et investi.

**Conclusion centrale :**

```text
INTERVENTION_EXISTED = fortement démontré
INTERVENTION_CHANGED_MARGIN = soutenu dans certains cas, surtout Chili 1964
INTERVENTION_CHANGED_WINNER = non établi pour les trois cas étudiés
COVERT_OPERATION != ELECTORAL_DETERMINISM
```

Cette séparation doit devenir une règle de la fresque générale : `action / coordination / portée / persuasion / effet / contrefactuel` ne sont pas interchangeables.

# 2. MANIPULATION_REPORT

## Italie 1948

Mécanismes établis : soutien aux forces anticommunistes, usage de l'aide et de signaux diplomatiques, communication officielle, campagne d'information et opérations clandestines contemporaines reconnues par le NSC.

```text
ORIGIN = FOREIGN / STATE
VISIBILITY = OPEN + COVERT
METHOD = FUNDING | PERSUASION | INFORMATION | POLITICAL_SUPPORT
RELATION = COORDINATED_AT_US_POLICY_LEVEL
TARGET = ELECTORATE | PARTIES | GOVERNMENT
LEVEL = I2-I4 strong ; I5-I7 open/partial
```

## Chili 1964

Mécanismes établis : soutien financier direct via intermédiaires, soutien organisationnel, financement d'autres acteurs de l'offre électorale, mobilisation/ciblage, propagande multicanale et black propaganda documentée dans l'enquête sénatoriale.

```text
ORIGIN = FOREIGN / STATE
VISIBILITY = COVERT / DECEPTIVE
METHOD = FUNDING | ORGANIZATION | PROPAGANDA | TARGETING
RELATION = COORDINATED/TASKED
TARGET = CANDIDATE | ELECTORATE | PARTY_SYSTEM
LEVEL = I2-I4 verified ; I5 supported ; I6 supported on margin/majority ; I7 open
```

## Chili 1970

Avant le vote :

```text
METHOD = SPOILING | PROPAGANDA | POLITICAL_ACTION
LEVEL = I2-I4 verified
I6 immediate objective = failed
```

Après le vote :

```text
METHOD = CLANDESTINE_ACTION | COUP_PROMOTION | CONTACTS | MATERIAL_SUPPORT
RELATION = TASKED/COORDINATED
TARGET = CONGRESSIONAL_CONFIRMATION | MILITARY | SUCCESSION
LEVEL = I3 verified
```

La proposition de payer des votes parlementaires apparaît dans des plans. **Planifier un achat de voix n'est pas prouver son exécution.**

# 3. CLUSTERS

Trois clusters suffisent.

### C-A — Influence électorale ouverte + clandestine
Italie 1948 : diplomatie, économie, information, soutien politique et clandestin sont imbriqués.

### C-B — Intervention électorale clandestine de haute intensité
Chili 1964 : le soutien finance et équipe une capacité électorale domestique tout en masquant son origine.

### C-C — De l'élection à l'empêchement institutionnel
Chili 1970 : échec du spoiling électoral, puis déplacement vers la confirmation parlementaire et l'option militaire. Influencer le vote et empêcher l'accession après le vote ne sont pas le même mécanisme.

# 4. HERMÉNEUTIQUE

Le récit « la CIA choisit les gouvernements » est trop fort. Le récit inverse « les accusations d'ingérence américaine sont fantasmées » est faux pour les cas étudiés.

La documentation montre un État américain qui, dans le contexte de guerre froide, considère explicitement la politique intérieure d'autres États comme un champ de compétition stratégique et mobilise des moyens publics et clandestins pour modifier leur trajectoire.

Le point difficile est le **contrôle du résultat**. Une opération peut être massive, opaque, coordonnée au plus haut niveau et néanmoins ne pas permettre de prouver que le vainqueur aurait été différent sans elle.

# 5. FORENSIC REASONING

## H1 — Washington a conduit des opérations matérielles d'influence électorale clandestine
**STRENGTHEN / VERIFIED** pour les cas étudiés.

## H2 — Ces opérations ont déterminé les vainqueurs
**UNRESOLVED / trop forte.**

- Italie 1948 : fortes causes domestiques et structurelles concurrentes.
- Chili 1964 : effet sur l'ampleur du succès soutenu ; winner counterfactual ouvert.
- Chili 1970 : opération anti-Allende n'empêche pas sa pluralité.

## H3 — Après échec électoral, l'action clandestine peut se déplacer vers l'étape institutionnelle suivante
**STRENGTHEN** sur Chili 1970.

## H4 — Clé clandestine = causalité électorale forte
**KILL.**

La clandestinité renseigne sur le mode d'action et la responsabilité, pas sur l'efficacité.

# 6. PRISME DIALECTIQUE

### Thèse forte
Les États-Unis ont historiquement pratiqué des interventions électorales/politiques clandestines documentées.

**Résiste :** financement, propagande, soutien politique clandestin, coup-promotion au Chili.

### Contre-thèse forte
Italie et Chili possèdent des acteurs et causalités domestiques propres. Lire leurs élections comme de simples produits de Washington efface cette agence locale.

**Résiste :** cette objection détruit le déterminisme externe, pas la réalité des opérations.

### Synthèse
Le modèle le moins faux est interactif :

```text
forces domestiques
+ ressources étrangères
+ interventions informationnelles/organisationnelles
+ institutions électorales
+ contexte géopolitique
-> résultat observé
```

La part marginale de chaque cause reste souvent difficile à isoler.

# 7. CHRONOLOGIE

| Date | Événement | Statut |
|---|---|---|
| 8 mars 1948 | NSC 1/3 appelle à empêcher la participation communiste issue du scrutin italien | VERIFIED |
| 18 avril 1948 | DC gagne 48,5 % | VERIFIED |
| 12 mai 1948 | NSC 10 cite les opérations clandestines improvisées des élections italiennes | VERIFIED |
| 14 mai 1964 | Special Group approuve +1,25 M$ pour l'opération chilienne | VERIFIED |
| 4 sept. 1964 | Frei gagne avec 56 % contre 39 % à Allende | VERIFIED |
| mars–sept. 1970 | Opération américaine de spoiling anti-Allende | VERIFIED |
| 4 sept. 1970 | Allende arrive premier avec 36,3 % | VERIFIED |
| 1970 post-vote | Plans envisagent notamment l'achat de votes parlementaires | VERIFIED AS PLAN |
| 16 oct. 1970 | Guidance Track II : politique de renversement d'Allende par coup | VERIFIED |
| 21 oct. 1970 | Armes livrées à des comploteurs selon note FRUS | VERIFIED |
| 4 nov. 1970 | Allende entre en fonction | VERIFIED OUTCOME |

# 8. DOMAINES

Géopolitique, électoral, informationnel, économique, institutionnel, militaire, juridique, psychologique et historique.

# 9. RÉSEAU D'ACTEURS

```text
Présidence / NSC / Special Group / 40 Committee
                    |
                    v
                   CIA
          /          |          \
      financement  propagande   contacts/ops
        |             |             |
        v             v             v
partis/candidats   médias/groupes   acteurs militaires
        \             |             /
         \            v            /
              électorat / institutions
```

Ce graphe n'implique pas le contrôle de tous les acteurs locaux.

# 10. CHAÎNES / PELOTE

## Italie 1948
`menace perçue -> décision US -> aide/signaux/information -> soutien politique + clandestin -> victoire DC -> causalité marginale exacte OPEN`

## Chili 1964
`objectif battre Allende -> autorisation -> intermédiaires -> campagne/propagande/organisation -> Frei 56 % -> effet marge soutenu -> winner counterfactual OPEN`

## Chili 1970
`spoiling -> Allende premier -> échec objectif immédiat -> pression sur confirmation -> Track II/coup-promotion -> Allende confirmé/investi`

# 11. CARTE DES PREUVES

Voir `INV-010_EVIDENCE_MAP.csv`.

| Objet | Niveau atteint | Verdict |
|---|---|---|
| Italie 1948 : existence/action | I2-I3 | VERIFIED |
| Italie : portée/exposition | I4 partiel | SUPPORTED |
| Italie : persuasion | I5 | OPEN |
| Italie : changement du vainqueur | I6-I7 | NOT ESTABLISHED |
| Chili 1964 : action/coordination/reach | I2-I4 | VERIFIED |
| Chili 1964 : marge/majorité | I6 | SUPPORTED |
| Chili 1964 : autre vainqueur sans intervention | I7 | OPEN |
| Chili 1970 : spoiling | I2-I4 | VERIFIED |
| Chili 1970 : empêcher pluralité Allende | I6 | FAILED |
| Chili 1970 : Track II | I3 | VERIFIED |
| Schneider : responsabilité directe CIA | I6-I7 | NOT ESTABLISHED |

# 12. CARTE DIALECTIQUE

| Claim | Meilleure preuve pour | Meilleure objection | Verdict |
|---|---|---|---|
| USA ont influencé Italie 1948 | NSC 1/3 + NSC 10 | ampleur exacte du covert moins précise | VERIFIED |
| USA ont fait gagner la DC | intervention réelle | Église, Marshall Plan, De Gasperi, pas de contrefactuel | OPEN |
| CIA a puissamment soutenu Frei | autorisations + Church | — | VERIFIED |
| CIA a choisi le président en 1964 | échelle + auto-évaluation CIA | Frei possiblement encore pluralité ; causalités locales | NOT ESTABLISHED |
| Opération 1970 a empêché Allende | campagne réelle | Allende arrive premier | FAILED |
| USA ont tenté de bloquer Allende après le vote | Track II | — | VERIFIED |
| USA ont acheté les votes du Congrès | plan jusqu'à 500k | débats/objections, pas preuve exécution | NOT VERIFIED |
| CIA a directement provoqué coup 1973 | histoire anti-Allende | Church : pas de hard evidence directe | NOT ESTABLISHED HERE |

# 13. PÉRIMÈTRE & LIMITES

1. Trois cas ne suffisent pas à quantifier la fréquence globale.
2. Aucun cas n'offre un contrefactuel expérimental.
3. Les archives déclassifiées sont riches mais incomplètes.
4. Une auto-évaluation CIA prouve mieux ce que l'agence croyait que le monde contrefactuel.
5. 1973 n'est utilisé que pour empêcher une extrapolation abusive.
6. Le runtime Truth Engine canonique n'est pas disponible dans le bundle fourni.
7. Les catégories juridiques contemporaines ne sont pas rétroprojetées mécaniquement.

# 14. ÉTAT DES CONNAISSANCES

## VERIFIED
- intervention active en Italie 1948 ;
- composantes clandestines ;
- soutien clandestin massif au Chili 1964 ;
- objectif de battre Allende ;
- propagande organisée ;
- spoiling 1970 ;
- Allende premier malgré celui-ci ;
- Track II visant explicitement un coup ;
- armes livrées à des comploteurs en octobre 1970.

## SUPPORTED
- aide américaine ayant augmenté la marge de Frei en 1964 ;
- contribution matérielle américaine à l'environnement électoral italien de 1948.

## OPEN / NON ÉTABLI
- nombre de points de vote causés ;
- winner counterfactual Italie 1948 ;
- winner counterfactual Chili 1964 ;
- responsabilité directe CIA dans la mort de Schneider ;
- attribution opérationnelle directe du coup de septembre 1973.

## CORRECTION CORPUS
La formule « 64 tentatives de changement de régime covert par la CIA » est trop forte. O'Rourke décrit **64 tentatives clandestines de changement de régime soutenues par les États-Unis**, contre 6 ouvertes, dans son dataset de guerre froide. Cela ne code pas automatiquement chacune comme « opération CIA », « coup réussi » ou « ingérence électorale ».

# 15. SUSPICION / VÉRIFICATION

### Suspicion
Les puissances dénonçant l'ingérence ont elles-mêmes une histoire documentée d'interventions clandestines.

### Vérification
**Oui**, pour les cas étudiés au sens descriptif d'interventions destinées à modifier une trajectoire politique/électorale étrangère.

### Limite
Cela ne prouve ni que toutes les accusations contemporaines sont hypocrites, ni que les États-Unis déterminaient les résultats électoraux, ni qu'un cas historique permet d'attribuer une opération actuelle.

### Delta méthodologique

```text
QUI a agi ?
PAR QUEL mécanisme ?
QUEL degré de dissimulation ?
QUELLE coordination ?
QUELLE portée ?
QUEL effet observé ?
QUEL contrefactuel ?
```

Le standard doit être symétrique, quel que soit l'acteur.

---

# SOURCES

Registre : `INV-010_SOURCES.csv`.

<!-- SOURCE: registry=INV-010_SOURCES.csv; evidence_map=INV-010_EVIDENCE_MAP.csv -->

# REQUEST / TRACE NOTE

Les recherches web et documents ont été effectivement consultés. Aucun faux `QRY-ID` Truth Engine n'est sérialisé puisque le state manager canonique n'est pas fourni. La reproductibilité repose ici sur les URLs/titres du registre sources, la carte atomique des preuves, la RUN_CARD et les hashes de bundle.

<!-- DECISION: no_fake_TE_registry=true; reason=runtime_helpers_missing -->
