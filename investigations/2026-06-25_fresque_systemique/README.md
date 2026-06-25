# Fresque Systemique — France 1975-2026

## Pourquoi

Ce dossier est le produit d'une enquete systemique sur les defaillances silencieuses de la societe francaise. Le constat de depart : la France produit des tragedies evitables (sang contamine, canicule 2003, amiante, Mediator, etc.) sans que le systeme genere de contre-reaction citoyenne proportionnee. Pourquoi ?

L'hypothese : ces defaillances ne sont pas des accidents. Elles sont le produit d'une architecture systemique construite sur 200+ ans, maintenue par un ensemble de mecanismes homeostatiques qui transforment la colere en carburant, la resistance en maintenance, et la lucidite en fonction du systeme.

## Histoire du projet

### Phase 0 : Les enquêtes 68tars (24 juin 2026)

Le projet n'a pas commence par la theorie systemique, mais par une question tres concrete : **quelle generation est responsable du declin français ?**

10 investigations ont ete menees sur la generation 68tars (boomers), explorant successivement :
- Leur responsabilite dans le verrouillage du pays (10h00)
- Les occasions perdues de souverainete (10h30)
- L'iceberg des 7 faisceaux de confiscation (14h00)
- La contre-enquete dialectique (17h00)
- Le conflit these boomer vs corpus changement de regime (20h00)
- La mecanique du laisser-aller (22h00)
- Le profil du lambda boomer (23h00)
- La chronologie du laisser-aller 1974-2026 (23h30)
- La fresque des mensonges et omissions (00h30)

Ces fichiers se trouvent dans `00_enquetes_68tars/`.

**Ce que cette phase a revele :** accuser une generation est insuffisant. Les boomers ne sont pas la cause — ils sont eux-memes le produit d'un systeme qui les a precedes et qui les depasse. La question est devenue : *quel est le systeme qui produit ces comportements, ces verrouillages, cette impuissance collective ?*

C'est ce constat d'echec de l'approche generationnelle qui a conduit a changer d'echelle.

### Phase 1 : Hyper-matrice 1975-2026

Apres avoir abandonne l'angle generationnel, l'enquete est passee a une echelle macro : 5 agents ont genere une hyper-matrice de 2519 evenements couvrant la France de 1975 a 2026, classes en 20 dimensions (POL, ECO, SOC, JUR, SANT, EDU, etc.). Chaque evenement est code selon son impact systemique (X = echec, XX = tragedie, +/- = revelateur, + = reussite).

Fichiers dans `01_donnees/`, du plus ancien au plus recent :
- `01-00_INTRO_MATRICE` — concept initial de la matrice
- `01-30_matrice_annuelle` — premiere version annuelle
- `03-15_matrice_enrichie` — enrichie a ~300 evenements + fichier maitre
- `12-00_france_2016-2026_HYPER_MATRICE` — hyper-matrice focus 2016-2026
- `12-00_matrice_supplement_700` — supplement de ~700 evenements
- `17-00_france_1975-1982_HYPER_MATRICE` a `17-00_france_2007-2026` — decoupages par decennie
- `17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE` (208K) — version unifiee finale

### Phase 2 : Analyse systemique et 8 fils

L'enquete sur le **sang contamine** (1984-1991) a servi de revelateur. En analysant pourquoi 4000 hemophiles ont ete contamines sans que personne ne reagisse, 8 fils causaux ont ete identifiees, remontant jusqu'en 1791. Chaque fil est un verrou systemique neutralisant un contre-pouvoir :

| Fil | Contre-pouvoir neutralise |
|-----|--------------------------|
| A — Mandarinat medical/scientifique | Autorite scientifique incontestable |
| B — Monopole d'Etat | Initiative citoyenne |
| C — Societe civile atrophiee | Solidarite collective |
| D — Justice domestiquee | Recours juridique |
| E — Presse sans contre-pouvoir | Information independante |
| F — Ecole-moule | Esprit critique |
| G — Laicite religion civile | Contre-pouvoir moral |
| H — Exceptionnalisme francais | Solutions etrangeres |

L'enquete fondatrice qui a revele ces 8 fils est l'analyse du **sang contamine** (1984-1991), dans `02_enquetes/18-00_anatomie_impuissance_civique_ARCHITECTURE.md`.

### Phase 3 : Mecanismes actifs (v1.1)

Les 8 fils expliquent les *structures* du verrouillage, mais pas les *mecanismes* qui stabilisent le systeme. 33 mecanismes actifs (M01-M33) ont ete extraits de 7 articles de la Resistance Cognitive (Substack, 2025-2026), organises en 4 groupes :

- **Capture du Pouvoir** (M01-M07) : comment les elites verrouillent l'Etat
- **Controle de l'Information** (M08-M13) : comment le recit est fabrique
- **Dissuasion/Fragilisation** (M14-M21) : comment la volonte est brisee
- **Neutralisation de la Dissidence** (M22-M33) : comment l'opposition est absorbee

### Phase 4 : Empire du Mensonge (v1.2)

L'article *L'Empire du Mensonge : Rapport d'autopsie d'une civilisation sous anesthesie* (1987 lignes, Resistance Cognitive, 2026-01-07) a ete systematiquement analyse. Il a livre :
- 9 nouveaux mecanismes (M34-M42) : Firehose, OODA, Controle reflexif, Hypernormalisation, Lawfare, Shifting Baseline, Propagande algorithmique, Complexe de la censure, Schismogenese
- 10 strategies de resistance (R01-R10)
- 32 concepts relais documentes dans l'hypermatrice d'extraction

### Phase 5 : Separation mission/connaissance (v1.3)

Le protocole initial melait 3 choses : la connaissance (mecanismes/fils), la methode, et le prompt d'enquete. v1.3 les separe :

- **`PROMPT_INVESTIGATION_v1.md`** — la mission envoyee au LLM (court, environ 80 lignes)
- **`PROTOCOLE_v1.3.md`** — la reference documentaire (472 lignes, consultable a discretion)

Le principe : le LLM enquete librement. Le protocole est une boite a outils, pas un formulaire.

## Structure du dossier

```
2026-06-25_fresque_systemique/
├── README.md                        ← vous etes ici
│
├── 00_enquetes_68tars/              ← point de depart (10 enquetes generation boomer)
│
├── 01_donnees/                      ← hyper-matrices (2519 evenements)
│   ├── 2026-06-25_01-00_fresque_systemique_INTRO_MATRICE.md
│   ├── 2026-06-25_01-30_matrice_annuelle_1975_2026.md
│   ├── 2026-06-25_03-15_matrice_enrichie_300_et_MAITRE.md
│   ├── 2026-06-25_12-00_france_2016-2026_HYPER_MATRICE.md
│   ├── 2026-06-25_12-00_matrice_supplement_700_et_SUPPL.md
│   ├── 2026-06-25_17-00_france_1975-1982_HYPER_MATRICE.md
│   ├── 2026-06-25_17-00_france_1983-1990_HYPER_MATRICE.md
│   ├── 2026-06-25_17-00_france_1991-1998_HYPER_MATRICE.md
│   ├── 2026-06-25_17-00_france_1999-2006_HYPER_MATRICE.md
│   ├── 2026-06-25_17-00_france_2006-2015_HYPER_MATRICE.md
│   ├── 2026-06-25_17-00_france_2007-2026_HYPER_MATRICE.md
│   └── 2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md
│
├── 02_enquetes/                     ← analyses et investigations
│   ├── 2026-06-25_02-00_responsability_gaps_RAPPORT.md
│   ├── 2026-06-25_17-00_france_1975-2026_ANALYSE_SYSTEMIQUE.md
│   └── 2026-06-25_18-00_anatomie_impuissance_civique_ARCHITECTURE.md
│
└── 03_framework/                    ← protocole, prompt, outils
    ├── 2026-06-25_18-30_protocole_investigation_FRAMEWORK.md      (v1.0)
    ├── 2026-06-25_18-30_protocole_investigation_FRAMEWORK_v1.3.md (latest)
    ├── 2026-06-25_20-00_empire_mensonge_concepts_extraits_HYPER_MATRICE.md
    └── 2026-06-25_21-00_prompt_investigation_v1_PROMPT.md
```

## Comment lancer une enquete

1. Choisir un evenement dans la matrice (`01_donnees/`)
2. Ouvrir `03_framework/2026-06-25_21-00_prompt_investigation_v1_PROMPT.md`
3. Copier le prompt, remplacer `[ANNEE]` et `[TITRE]`
4. Envoyer a l'agent d'enquete
5. Consulter `PROTOCOLE_v1.3.md` si besoin d'approfondir un mecanisme ou pattern
6. Sauvegarder la fiche YAML produite dans `02_enquetes/`

## Version du protocole

| Version | Date | Changement |
|---------|------|------------|
| v1.0 | 2026-06-25 | 8 fils fondateurs (sang contamine) |
| v1.1 | 2026-06-25 | 33 mecanismes actifs (7 articles Resistance Cognitive) |
| v1.2 | 2026-06-25 | +9 mecanismes M34-M42, +10 resistances R01-R10 (Empire du Mensonge) |
| v1.3 | 2026-06-25 | Separation prompt/protocole, YAML simplifie, autonomie du LLM |

## Contexte plus large

Ce dossier est un module du projet Truth Engine. Les investigations produites ici alimentent la base Mnemolite. Les articles de la Resistance Cognitive (103 articles, Substack) sont la source conceptuelle des mecanismes.

### Point de depart

Le dossier `00_enquetes_68tars/` contient les 10 investigations du 24 juin 2026 qui ont amorce le projet. Elles sont conservees comme trace du cheminement intellectuel : on est parti d'une question generationnelle, on a abouti a un protocole d'enquete systemique.

Voir `AGENTS.md` a la racine du projet pour les regles operatoires.
