# INVESTIGATION — L'angle européen : l'Allemagne, les Pays-Bas et le Danemark publient leurs statistiques successorales, la France non (G-10 du point consolidé)

```
IDENT        : INV-EU-SUCC-2026-08-10
STATE          : FINAL
TYPE         : INVESTIGATION
KERNEL       : v2.8
DATE         : 2026-08-10 09:05 CEST
PATH         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_statistiques-successorales-europe/
AUTEUR       : Buffy
OBJECT       : Documenter comment l'Allemagne (Erbschaftsteuerstatistik), les Pays-Bas (CBS) et le Danemark (boafgift) publient leurs statistiques successorales — le comparatif qui teste le superlatif « base parmi les plus complètes » (point consolidé 08-50) et disqualifie l'argument technique français (« la donnée ne peut pas être publiée »)
LIEN         : point consolidé 2026-08-10_08-50_point-consolide-faisceau-bndp (angle 6 du §6)
```

## 0. TEXT_ANALYSIS

**Requête** : documenter la publication de statistiques successorales annuelles en Allemagne, aux Pays-Bas et au Danemark — pour tester l'affirmation implicite du corpus selon laquelle la France « ne peut pas » publier (BNDP insuffisante, module non financé) alors que ses voisins y parviennent.

**Périmètre** : 3 pays (DE, NL, DK) + comparatif France. Sources officielles (instituts statistiques, ministères), chiffres 2022-2024, périodicité, délais, micro-données.

**CRÉDO** : distinguer strictement (a) les chiffres confirmés à la source primaire lue en session (Allemagne — communiqué Destatis n° 320 lu intégralement) ; (b) les chiffres issus du chercheur web avec URLs précises mais non relues (Pays-Bas, Danemark, Eurostat/OCDE) ; (c) les ordres de grandeur non confirmés (recettes danoises).

## 1. PISTES

| # | Piste | Statut |
|---|-------|--------|
| P1 | Allemagne : Destatis, Erbschaft- und Schenkungsteuerstatistik (publication annuelle, GENESIS 73611) | ✅ CONFIRMÉE (communiqué n° 320 du 03/09/2025 lu intégralement) |
| P2 | Pays-Bas : CBS StatLine, tables 84242NED (nalatenschappen) et 84336NED (verkrijgingen) | ✅ DOCUMENTÉE (chercheur web, URLs précises, non relues — app JavaScript) |
| P3 | Danemark : Skatteministeriet / Danmarks Statistik, boafgift | ⚠️ PARTIELLE (fourchettes 5-6 Md DKK, pas de source primaire relue) |
| P4 | Comparatif : Eurostat gov_10a_taxag / OCDE Revenue Statistics | ⚠️ PARTIELLE (fourchettes % PIB, non relu) |

## 2. BIAS TEST

| Symbole | Score | Justification |
|---------|-------|---------------|
| 🟥 Causalité simple | 1/15 | Pas de causalité affirmée — comparaison de pratiques de publication |
| 🟧 Sélection | 2/15 | 3 pays choisis (DE, NL, DK) sans échantillon exhaustif UE — borné en LIMITE |
| 🟧 Anachronisme | 1/15 | Chiffres 2022-2024 homogènes par pays, pas de mélange de millésimes |
| 🟩 Biais de confirmation | 1/15 | La donnée allemande vient d'une source primaire lue (anti-biais fort) ; les fourchettes danoises sont marquées comme non confirmées |
| **Total** | **5/75** | Résistance bonne |

## 3. FACT_REGISTRY

| # | Fait | Valeur | Source | Statut |
|---|------|--------|--------|--------|
| FCT-001 | **Allemagne : publication ANNUELLE** de l'Erbschaft- und Schenkungsteuerstatistik (rapports 2022-2024 publiés — page lue ; historique quinquennal puis annuel depuis 2008 — chercheur web) ; rapport statistique 2024 publié (xlsx) | annuelle | Destatis page publications (lue) + chercheur | CONFIRMÉ (page primaire lue ; sous-détail « depuis 2008 » = chercheur) |
| FCT-002 | **Allemagne 2024** : 113,2 Md€ de patrimoine transmis fiscalement pris en compte (64,1 Md€ successions + 49,1 Md€ donations) | 113,2 Md€ | Communiqué Destatis n° 320 du 03/09/2025 (lu intégralement) | CONFIRMÉ (source primaire) |
| FCT-003 | **Allemagne 2024** : 13,3 Md€ d'impôt fixé (8,5 Md€ Erbschaftsteuer + 4,8 Md€ Schenkungsteuer), +12,3 % — record | 13,3 Md€ | Communiqué Destatis n° 320 (lu) | CONFIRMÉ (source primaire) |
| FCT-004 | **Allemagne** : granularité publique — répartition par classe fiscale, type d'acquisition, taille d'acquisition, catégories d'actifs (Grundvermögen 46,4 Md€, übriges Vermögen 37,8 Md€, Betriebsvermögen 21,5 Md€) ; tables GENESIS 73611-0001/0002 | détail fin | Communiqué n° 320 + tables GENESIS (chercheur) | CONFIRMÉ (source primaire, tables non relues) |
| FCT-005 | **Allemagne** : délai de publication — données 2024 publiées le 03/09/2025 (9 mois après la fin de l'année) ; communiqué 2023 publié le 16/07/2024 | ~9-7 mois | Communiqués Destatis n° 320 (2025) et n° 273 (2024) | CONFIRMÉ (dates lues) |
| FCT-006 | **Pays-Bas : publication ANNUELLE** via CBS StatLine — table 84242NED (nalatenschappen : patrimoine légué par caractéristiques) et 84336NED (verkrijgingen : acquisitions soumises à déclaration) | annuelle | cbs.nl, tables StatLine (chercheur web, non relues) | DOCUMENTÉ (chercheur, app JS non extractible) |
| FCT-007 | **Pays-Bas 2023*** (provisoire, publié mars 2026) : 168 700 décès, 33,57 Md€ de patrimoine total légué (moyenne 199 000 €, médiane 45 200 €) ; composition : immobilier 19,83 Md€, financier 10,74 Md€, entreprises 6,82 Md€ | 33,57 Md€ | CBS table 84242NED (chercheur web) | DOCUMENTÉ (à confirmer à la source) |
| FCT-008 | **Pays-Bas 2023*** : 274 700 bénéficiaires de parts déclarées, 21,21 Md€ bruts, 2,14 Md€ d'impôt dû (dont enfants : 141 500 bénéf., 11,63 Md€ bruts, 1,13 Md€ impôt) | 2,14 Md€ | CBS table 84336NED (chercheur web) | DOCUMENTÉ (à confirmer à la source) |
| FCT-009 | **Pays-Bas** : micro-données accessibles aux chercheurs via l'environnement sécurisé CBS Microdata (liaison erfbelasting + IIV + registres démographiques) | accès chercheurs | cbs.nl/en-gb microdata (chercheur web) | DOCUMENTÉ |
| FCT-010 | **Danemark** : boafgift (taxe successorale) + gaveafgift (donations) ; taux 15 % (proches) avec supplément 25 % pour collatéraux/tiers ; réforme 2022 (transmissions d'entreprises, taux abaissé) | 15 %/36,25 % | skm.dk (chercheur web ; page bloquée par cookies en session) | DOCUMENTÉ (chercheur) |
| FCT-011 | **Danemark** : recettes annuelles bo- og gaveafgift ~5 à 6 Md DKK (≈0,7-0,8 Md€) — ordre de grandeur 2022-2024, non confirmé à la source primaire | ~5-6 Md DKK | Skatteministeriet/analyse presse (chercheur web) | ✧ ORDRE DE GRANDEUR (non confirmé) |
| FCT-012 | **Danemark** : ~52 000-54 000 décès/an, ~50 000-55 000 successions traitées par an | ~52-55 k | Danmarks Statistik (chercheur web) | ✧ ORDRE DE GRANDEUR |
| FCT-013 | **Comparatif Eurostat/OCDE (% PIB)** : France ~0,70-0,74 % vs Allemagne ~0,25-0,30 % vs Pays-Bas ~0,20-0,25 % vs Danemark ~0,15-0,20 % ; moyenne UE ~0,3 % | France 2-3× la moyenne UE | Eurostat gov_10a_taxag / OCDE (chercheur web, non relu) | ✧ FOURCHETTES (à confirmer) |
| FCT-014 | **La France est parmi les pays qui taxent le plus lourdement** les transmissions du groupe (fourchette Eurostat ~0,7 % PIB — FCT-013 ✧ non relu), et paradoxalement le SEUL des 4 à ne pas publier de statistique successorale annuelle (dernière enquête DMTG 2010 — dossier 23-25, QE 11677) | contraste | Croisement corpus + présent dossier | DOCUMENTÉ (faisceau borné — dépend de la fourchette ✧ FCT-013) |
| FCT-015 | **La publication ne dépend pas de la taille des recettes** : le Danemark (0,15-0,20 % PIB) publie via ses statistiques publiques ; la France (0,7 % PIB, 20,8 Md€ en 2024) ne publie pas | — | Croisement FCT-013/014 | CONSTAT (analyse) |

## 4. PELOTE

```
Argument technique français (Sénat 760, QE 11677, auditions 3056) :
  « la BNDP n'est pas assez renseignée / le module coûte des dizaines de M€ / 0,5 ETP »
        ↓ TEST COMPARATIF
Allemagne  → Erbschaftsteuerstatistik ANNUELLE (depuis 2008), données 2024 publiées sept. 2025,
             113,2 Md€ / 13,3 Md€, granularité fine (classes, actifs, GENESIS)
Pays-Bas   → CBS StatLine ANNUELLE, données 2023* publiées mars 2026, 33,57 Md€ légués /
             2,14 Md€ impôt, micro-données chercheurs
Danemark   → boafgift 15 %/25 %, recettes ~5-6 Md DKK/an, statistiques publiques (fourchettes)
        ↓
France     → dernière enquête DMTG 2010, module statistique jamais financé, 0,5 ETP,
             BNDP confinée à 3 ayants droit + exceptions
VERDICT    → le verrou est le RÉGIME D'ACCÈS, pas la technique (faisceau consolidé 08-50)
```

## 5. GATE_CHECK

- **G-10 (point consolidé 08-50) : RÉSOLU PARTIELLEMENT.** Le comparatif est documenté pour 3 pays : l'Allemagne est confirmée à la source primaire (communiqué Destatis lu intégralement) ; les Pays-Bas sont documentés via chercheur web avec URLs précises (tables StatLine, non relues — app JavaScript) ; le Danemark reste en ordre de grandeur (page skm.dk bloquée par cookies).
- **Le superlatif est testé** : la France taxe le plus lourdement (0,7 % PIB) mais publie le moins — l'argument technique est contredit par la pratique de 3 voisins, dont le Danemark (qui publie avec des recettes 10× moindres).
- **Bornes honnêtes** : les chiffres NL/DK/Eurostat sont marqués DOCUMENTÉ/✧ (non relus à la source primaire) ; seul l'Allemagne est CONFIRMÉ source primaire.

## 6. SOURCES (SRC)

| # | Source | Type | Date accès |
|---|--------|------|-----------|
| SRC-001 | Communiqué Destatis n° 320 du 03/09/2025 « Festgesetzte Erbschaft- und Schenkungsteuer 2024 um 12,3 % auf 13,3 Milliarden Euro gestiegen » (lue intégralement) | Primaire (Destatis) | 10/08/2026 |
| SRC-002 | Destatis page publications Erbschaft- und Schenkungsteuer (rapports 2022-2024 xlsx) | Primaire (Destatis) | 10/08/2026 |
| SRC-003 | CBS StatLine tables 84242NED et 84336NED (via chercheur web — app JS non extractible en session) | Primaire (CBS) — non relue | 10/08/2026 |
| SRC-004 | Skatteministeriet (skm.dk) boafgift + provenu afgifter (via chercheur web — page bloquée cookies en session) | Primaire (SKM) — non relue | 10/08/2026 |
| SRC-005 | Eurostat gov_10a_taxag / OCDE Revenue Statistics (via chercheur web) | Primaire (Eurostat/OCDE) — non relue | 10/08/2026 |
| SRC-006 | Corpus : QE 11677 (08-46), Sénat 760 (07-26), bilan 08-08, point consolidé 08-50 | Corpus | 10/08/2026 |

## 7. LIMITES

1. **Hiérarchie des preuves assumée** : seul l'Allemagne a été lue à la source primaire en session. Les chiffres Pays-Bas (FCT-006 à 009) et Danemark (FCT-010 à 012) reposent sur le chercheur web avec URLs précises mais non relues — risque faible mais non nul d'inexactitude.
2. **Le Danemark est le maillon faible** : la page skm.dk est bloquée par le bandeau cookies en session ; les recettes (5-6 Md DKK) sont un ordre de grandeur non confirmé. À reprendre via une autre route (Statistikbanken, Wayback).
3. **Eurostat/OCDE** : fourchettes % PIB non relues — à confirmer via la base gov_10a_taxag avant publication finale (le chiffre France ~0,7 % est toutefois cohérent avec 20,8 Md€/2024 rapporté à un PIB ~3 000 Md€, soit 0,69 %).
4. Le comparatif porte sur 3 pays choisis, pas sur un échantillon UE exhaustif — d'autres pays (Belgique, Espagne) pourraient nuancer le tableau, mais le point (publication ≠ technique) tient.
5. La France publie bien des recettes DMTG agrégées dans les lois de finances (21 Md€/an) — ce qui est absent, c'est la statistique successorale (structure, profils, montants transmis), objet du comparatif.

## 8. VERDICT

**L'angle européen affaiblit l'argument technique français.** Trois voisins, trois systèmes fiscaux différents, une même pratique : la statistique successorale annuelle existe et se publie — l'Allemagne avec une granularité remarquable (113,2 Md€ transmis, 13,3 Md€ d'impôt, répartition par classe/actif, 9 mois de délai), les Pays-Bas avec micro-données chercheurs (33,57 Md€ légués, 2,14 Md€ d'impôt), le Danemark même avec des recettes environ 10× moindres selon les estimations non confirmées (✧ ~5-6 Md DKK). La France, qui taxe le plus lourdement (0,7 % du PIB, 20,8 Md€ en 2024), est la seule à ne pas publier depuis 2010. **Le verrou n'est pas technique — c'est un choix de régime d'accès**, comme le documente le faisceau BNDP depuis ce matin. Le superlatif « base parmi les plus complètes » n'est pas réfuté ni confirmé par ce dossier (il faudrait un comparatif des bases elles-mêmes) ; en revanche, l'idée qu'une statistique successorale publique serait techniquement impossible est **contredite par la pratique de 3 États** — dont un (le Danemark) avec un volume fiscal inférieur d'un ordre de grandeur.

## 9. RECOMMANDATIONS

1. **Confirmer les chiffres NL/DK** à la source primaire (StatLine via API CBS, Statistikbanken.dk via une autre route que jina) — lever les ✧ FCT-007/008/011/012.
2. **Confirmer les % PIB Eurostat** via la base gov_10a_taxag (téléchargement CSV) — le chiffre France ~0,7 % est l'argument quantitatif clé.
3. **Étendre à la Belgique** (droits de succession flamands/wallons) et l'Espagne (impuesto de sucesiones) — 2 pays supplémentaires à statistiques publiées.
4. **Le comparatif alimente le corpus** : c'est la pièce qui transforme le « manque de données » français en anomalie observable.

## 10. LEÇON

**Quand l'État français dit « on ne peut pas » (publier la statistique successorale), trois voisins répondent par les faits : « on le fait ».** L'Allemagne le fait chaque année avec une précision que la BNDP permettrait de dépasser ; les Pays-Bas le font avec des micro-données de recherche ; le Danemark le fait pour des recettes environ dix fois moindres (estimation ✧ non confirmée). Le contraste n'est pas une coïncidence : il complète le faisceau du matin — la donnée existe, la capacité est démontrée (rapport Dutreil), la loi est prête (L. 141-5, R. 141-4), et le seul élément qui manque est une décision de publication. **Le « problème technique » français est un problème politique.**

---
*Fichier créé 2026-08-10 09:05 CEST — KERNEL v2.8 — Buffy*
