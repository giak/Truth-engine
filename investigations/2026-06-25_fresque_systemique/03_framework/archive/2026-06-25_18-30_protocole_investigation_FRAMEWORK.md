# PROTOCOLE D'INVESTIGATION SYSTEMIQUE
## Framework d'enquete sur les defaillances francaises
### Prompt agentique : version 1.0

---

## PREAMBULE

Ce document decrit un protocole d'investigation systematique pour analyser les defaillances de la societe francaise. Il a ete construit inductivement a partir d'une matrice de 2 519 evenements (1975-2026), dont l'analyse a revele des patterns recurrants de blocage.

**Constats fondateurs :**
- Le systeme francais produit des defaillances silencieuses (catastrophes sanitaires, scandales, effondrements) sans generer de contre-reaction citoyenne proportionnee
- Ces defaillances ne sont pas des accidents : elles sont le produit d'une architecture systemique construite sur 200+ ans
- L'analyse du "sang contamine" (1984) a revele 8 fils causaux remontant jusqu'en 1791
- Chaque fil est un verrou systemique qui neutralise un contre-pouvoir

**Objectif du protocole :**
A partir d'une matrice d'evenements annee par annee, detecter les faits qui signalent une defaillance systemique, lancer une enquete pour remonter chaque fil jusqu'a sa racine, et accumuler les resultats pour construire une architecture systemique complete de la societe francaise.

---

## METHODOLOGIE GENERALE

### Principe

```
Evenement dans la matrice
    |
    v
Code X ou XX ? > Non > Ignorer
    | Oui
    v
Lancer enquete "tirer la pelote"
    |
    v
Identifier le(s) verrou(x) systemique(s) active(s)
    |
    v
Remonter chaque fil jusqu'a sa racine historique
    |
    v
Documenter dans une fiche d'enquete
    |
    v
Mettre a jour le tableau de bord
```

### Les 8 fils systemiques (checklist)

Chaque enquete doit verifier systematiquement les 8 fils suivants :

| # | Fil | Question pivot | Racine | Verrou |
|---|-----|---------------|--------|--------|
| A | Mandarinat medical/scientifique | Un expert a-t-il impose une decision sans contestation ? | 1803 | Le savoir est un monopole d'Etat |
| B | Monopole d'Etat | Y avait-il un monopole public empechant une alternative ? | 1791 | Pas de Plan B si l'Etat faillit |
| C | Societe civile atrophiee | Les victimes avaient-elles une organisation pour se defendre ? | 1791 | Pas de corps intermediaire |
| D | Justice domestiquee | La justice a-t-elle protege l'Etat plutot que les victimes ? | 1804 | L'Etat ne se juge pas |
| E | Presse sans contre-pouvoir | L'information a-t-elle ete filtree ou retardee ? | 1811 | Pas de journalisme d'investigation |
| F | Ecole-moule | Le systeme educatif a-t-il forme a l'obeissance plutot qu'au doute ? | 1808 | L'obeissance civique est un reflexe |
| G | Laicite religion civile | Y avait-il un contre-pouvoir moral independant de l'Etat ? | 1905 | L'Etat est seul maitre moral |
| H | Exceptionnalisme francais | Une solution etrangere a-t-elle ete refusee par nationalisme ? | 1660 | La souverainete tue |

---

## DECLENCHEMENT D'UNE ENQUETE

Un evenement dans la matrice annuelle declare une enquete si :

1. **Code X (echec)** : reforme retiree, crise, scandale, defaite electorale, effondrement d'une institution
2. **Code XX (tragedie)** : attentat, catastrophe, deces evitables, emeute, effondrement meurtrier
3. **Code +/- avec dimension critique** : evenement neutre qui revele un dysfonctionnement structurel (rapport accablant, commission d'enquete, temoignage, aveu d'impuissance)

**Cas particulier :** Un evenement code + (succes) peut occasionnellement etre investigue s'il revele un "contre-exemple" : un moment ou un contre-pouvoir a fonctionne. Utile pour comprendre ce qui aurait pu exister ailleurs.

---

## FORMAT DE LA FICHE D'ENQUETE

Chaque enquete produit une fiche au format suivant :

```yaml
ENQUETE: [ID unique: SYSTEME_AAAA_Sujet]
DATE: AAAA-MM-DD

EVENEMENT:
  annee: [AAAA]
  description: "[30-50 mots]"
  dimension: [POL/ECO/SOC/JUR/SANT/EDU/AGR/ENV/TEC/CUL/IMM/SPO/REL/DEMO/TRA/MIL/SCI]
  code: [X/XX/+/-]

VICTIMES:
  type: [directes/indirectes/systemiques]
  nombre: [chiffre ou estimation]
  profil: [qui etaient-elles ?]

CONTEXTE:
  gouvernement: [Premier ministre, President]
  contexte_eco: [crise, croissance, stagflation...]
  contexte_social: [mouvements en cours, tension, apathie...]

RESUME:
  [3 a 8 lignes : ce qui s'est passe, la chronologie, le denouement]

# --- ANALYSE DES 8 FILS ---

FIL_A_MANDARINAT:
  active: [oui/non/partiel]
  manifestation: "[comment l'autorite incontestee s'est exercee]"
  acteurs_concernez: "[qui avait l'autorite, qui l'a conteste]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[moment ou ca aurait pu etre different]"

FIL_B_MONOPOLE_ETAT:
  active: [oui/non/partiel]
  manifestation: "[quel monopole etait en cause, comment il a bloque]"
  alternative_existante: "[oui/non : decrire l'alternative]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

FIL_C_SOCIETE_CIVILE:
  active: [oui/non/partiel]
  manifestation: "[comment les victimes etaient isolees ou non-representees]"
  organisations_existantes: "[associations, syndicats, partis presents ou absents]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

FIL_D_JUSTICE:
  active: [oui/non/partiel]
  manifestation: "[comment la justice a traite ou ignore l'affaire]"
  verdict: "[sanction / acquittement / prescription / non-lieu]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

FIL_E_PRESSE:
  active: [oui/non/partiel]
  manifestation: "[comment l'info a circule ou ete bloquee]"
  delai_revelation: "[delai entre evenement et publication]"
  media_competent: "[journal, journaliste, type d'enquete]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

FIL_F_ECOLE:
  active: [oui/non/partiel]
  manifestation: "[comment la formation a joue un role dans l'obeissance]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

FIL_G_LAICITE:
  active: [oui/non/partiel]
  manifestation: "[contre-pouvoir moral aurait du reagir, ne l'a pas fait]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

FIL_H_EXCEPTIONNALISME:
  active: [oui/non/partiel]
  manifestation: "[solution etrangere refusee par orgueil national]"
  solution_refusee: "[quoi, par qui, pourquoi]"
  racine_historique: "[date : mecanisme]"
  bifurcation_perdue: "[...]"

# --- SYNTHESE ---

VERROU_PRINCIPAL: [A-H]
VERROUS_SECONDAIRES: [A-H, tries par importance]
DEGRE_SYSTEMICITE: [1 a 5]

ENSEIGNEMENT:
  "[3 a 5 lignes : ce que cette enquete revele sur le systeme]"

CITATION_CLE:
  "[citation la plus revelatrice de l'affaire, avec source]"

LIENS:
  - vers architecture systemique
  - vers autres enquetes liees
  - vers matrice d'evenements
```

---

## EXIGENCES DE QUALITE

Chaque enquete doit respecter les regles suivantes :

1. **Precision factuelle** : chaque affirmation doit etre verifiable. Citer les sources (dates, noms, decideurs, institutions).

2. **Remontee jusqu'a la racine** : ne pas s'arreter au premier niveau de cause. Chaque fil doit etre remonte jusqu'a son moment de creation : une loi, une institution, une decision fondatrice.

3. **Bifurcation perdue** : chaque fil doit identifier un moment ou ca aurait pu etre different. C'est le point le plus important : il revele la contingency du systeme.

4. **Citation cle** : trouver la phrase qui resume l'affaire. Celle que les historiens retiendront. ("Responsable mais pas coupable", "La France a peur", etc.)

5. **Degre de systemicite** :
   - 1 : defaillance individuelle, le systeme a bien fonctionne par ailleurs
   - 2 : defaillance locale, quelques verrous actives
   - 3 : defaillance structurelle, plusieurs verrous, pattern connu
   - 4 : defaillance systemique, la plupart des verrous actives
   - 5 : effondrement inscrit dans le code genetique du systeme (ex: sang contamine, 13 novembre, Outreau)

6. **Taille** : chaque enquete doit etre substantielle (minimum 200 lignes). Ne pas survoler. Un evenement simple peut reveler des racines profondes.

---

## TRAITEMENT DES RESULTATS

### Mise a jour du tableau de bord

Apres chaque enquete, mettre a jour le fichier `TABLEAU_DE_BORD.md` :

```markdown
# TABLEAU DE BORD : INVESTIGATIONS SYSTEMIQUES

## Metriques globales
| Annees couvertes | Evts dans matrice | Enquetes realisees | Enquetes en cours |
|---|---|---|---|
| 1975-2026 | 2519 | [N] | [N] |

## Distribution par code
| Code | Total | Enquete | % enquete |
|---|---|---|---|
| + | 821 | 0 | 0% |
| +/- | 1028 | ... | ... |
| X | 394 | ... | ... |
| XX | 276 | ... | ... |

## Activation par fil
| Fil | # enquetes | Verrou principal | Verrou secondaire |
|---|---|---|---|
| A | 0 | 0 | 0 |
| B | 0 | 0 | 0 |
| C | 0 | 0 | 0 |
| D | 0 | 0 | 0 |
| E | 0 | 0 | 0 |
| F | 0 | 0 | 0 |
| G | 0 | 0 | 0 |
| H | 0 | 0 | 0 |

## Bifurcations identifiees
| Date | Bifurcation | Verrou | Enquete |
|---|---|---|---|

## Enquetes recentes
| Date | ID | Evenement | Fils | Degre |
|---|---|---|---|---|

## Enquetes a faire (file d'attente)
| Priorite | Annee | Evenement | Code | Raison |
|---|---|---|---|---|
```

### Consolidation periodique

Toutes les 10 enquetes (ou sur demande) :
1. Analyser les fils les plus actives (pattern detection)
2. Verifier si un 9e fil emerge (fil systemique non couvert par A-H)
3. Mettre a jour l'architecture systemique globale
4. Rediger un rapport de synthese

---

## WORKFLOW D'EXECUTION

### Pour lancer une enquete

```
PROMPT AGENT :

Enquete systemique sur : [ANNEE] : [EVENEMENT]

Tu dois investiguer cet evenement en utilisant le protocole des 8 fils systemiques
(disponible dans PROTOCOLE_INVESTIGATION_FRAMEWORK.md).

Pour chaque fil (A a H), reponds :
1. Est-il active ? Oui/Non/Partiel
2. Comment s'est-il manifeste ?
3. Quelle est la racine historique ?
4. Quelle est la bifurcation perdue ?

Produis une fiche d'enquete complete au format YAML (spec dans le protocole).
Sauvegarde-la dans : enquetes/AAAA-MM-JJ_HH-MM_Sujet_ENQUETE.md
Ajoute-la au tableau de bord.
```

### Ordre de priorite

1. **XX** (tragedie avec morts evitables)
2. **X** (echec systemique : scandale, effondrement institutionnel)
3. **+/-** avec revelateur structurel (rapport accablant, commission)
4. **+** excepcionnel (reussite d'un contre-pouvoir, contre-exemple)

---

## EXEMPLE D'ENQUETE REALISEE

Le fichier suivant est l'enquete fondatrice qui a revele les 8 fils :

```
archives/2026-06-25_18-00_anatomie_impuissance_civique_ARCHITECTURE.md
Evenement : Sang contamine (1984-1991)
Degre de systemicite : 5
Verrous actives : A, B, C, D, E, F, G, H (les 8)
```

Cet exemple sert de reference pour la profondeur attendue.

---

## NOTES DE VERSION

- **v1.0** (2026-06-25) : Version fondatrice. 8 fils identifies a partir de l'enquete sur le sang contamine. Protocole valide sur un cas. A enrichir par l'usage.
