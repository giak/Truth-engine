# Fresque Systemique — France 1975-2026

## Pourquoi

Ce dossier est le produit d'une enquête systémique sur les défaillances silencieuses de la société française. Le constat de départ : la France produit des tragédies évitables (sang contaminé, canicule 2003, amiante, Mediator, etc.) sans que le système génère de contre-réaction citoyenne proportionnée. Pourquoi ?

**Thèse centrale :** ces défaillances ne sont pas des accidents. Elles sont le produit d'une architecture systémique construite sur 200+ ans, maintenue par un ensemble de mécanismes homéostatiques qui transforment la colère en carburant, la résistance en maintenance, et la lucidité en fonction du système.

---

## Histoire du projet

### Phase 0 : Les enquêtes 68tars (24 juin 2026)

10 investigations sur la génération 68tars (boomers), explorant le verrouillage du pays, les occasions perdues de souveraineté, l'iceberg des 7 faisceaux de confiscation. Ces fichiers sont dans `00_enquetes_68tars/`.

**Enseignement :** accuser une génération est insuffisant. Les boomers ne sont pas la cause — ils sont eux-mêmes le produit d'un système qui les précède et les dépasse.

### Phase 1 : Hyper-matrice 1975-2026

5 matrices couvrant 2 500+ événements de 1975 à 2026, classés en 20 dimensions (POL, ÉCO, SOC, JUR, SANT, etc.). Fichiers dans `01_donnees/`.

### Phase 2 : Analyse systémique et 8 fils (v1.0)

L'enquête sur le **sang contaminé** révèle 8 fils causaux remontant jusqu'en 1791. Chaque fil est un verrou systémique qui neutralise un contre-pouvoir :

| Fil | Contre-pouvoir neutralisé |
|-----|---------------------------|
| A — Mandarinat médical/scientifique | Autorité scientifique incontestable |
| B — Monopole d'État | Initiative citoyenne |
| C — Société civile atrophiée | Solidarité collective |
| D — Justice domestiquée | Recours juridique |
| E — Presse sans contre-pouvoir | Information indépendante |
| F — École-moule | Esprit critique |
| G — Laïcité religion civile | Contre-pouvoir moral |
| H — Exceptionnalisme français | Solutions étrangères |

### Phase 3 : 42 mécanismes actifs (v1.1 → v1.3)

33 mécanismes (M01-M33) + 9 (M34-M42) issus de l'article *L'Empire du Mensonge* + 10 stratégies de résistance (R01-R10). Séparation du protocole et du prompt (v1.3).

### Phase 4 : Standard NREF v2.0 (26 juin 2026)

Refonte du format d'enquête. Standard de preuve **Non Réfutable** : 6 nouveaux chapitres YAML obligatoires (PREUVES, CONTRE-VERSION, ACTIVATION, INCERTITUDES, BIAIS, REPLICATION), barème de conformité à 8 exigences, workflow avec étape de vérification NREF.

### Phase 5 : Renforcement v2.1 (26 juin 2026)

Post-audit de l'enquête sang contaminé v2.0 : les sources n'étaient pas vérifiées (5 glyphes ✦ abusifs, 0 URL, 0 HEAD check). Corrections :
- Instructions opérationnelles de recherche web et HEAD check
- `source_url`, `citation_directe`, `head_check_date` obligatoires dans le schéma YAML
- Glyphes ✦ soumis à HEAD check réel
- Barème NREF passe à 10 exigences (NREF-9, NREF-10)
- Échelle de robustesse A/B/C/D/E
- Étape 0 (recherche documentaire) ajoutée au workflow
- Format ADDENDUM pour l'Ultrathinking (obligatoire degré 4-5)
- Étape 5 bis (vérification par second agent)

---

## Structure du dossier

```
2026-06-25_fresque_systemique/
├── README.md                        ← vous êtes ici
│
├── 00_enquetes_68tars/              ← point de départ (10 enquêtes génération boomer)
│
├── 01_donnees/                      ← hyper-matrices (2 500+ événements)
│   └── (matrices 1975-1982 à 2007-2026, fichier unifié)
│
├── 02_enquetes/                     ← investigations produites
│   ├── 2026-06-26_sang_contamine_v2.1_INVESTIGATION.md   ← ★ enquête de référence v2.1
│   ├── 2026-06-25_17-00_france_1975-2026_ANALYSE_SYSTEMIQUE.md
│   ├── 2026-06-25_02-00_responsability_gaps_RAPPORT.md
│   └── archive/                     ← anciennes investigations
│       ├── 2026-06-26_sang_contamine_INVESTIGATION.md (v1.3)
│       ├── 2026-06-26_sang_contamine_NREF_INVESTIGATION.md (v2.0)
│       └── 2026-06-25_18-00_anatomie_impuissance_civique_ARCHITECTURE.md (essai fondateur)
│
├── 03_framework/                    ← protocole v2.4, prompt v2.4, tableau de bord
│   ├── 2026-06-26_18-30_protocole_investigation_FRAMEWORK_v2.0.md   ← ★ protocole v2.4 (Pelote de Laine)
│   ├── 2026-06-26_21-00_prompt_investigation_v2_PROMPT.md           ← ★ prompt v2.4 (Pelote)
│   ├── TABLEAU_DE_BORD.md                                            ← ★ tableau de bord v2.4
│   ├── 2026-06-25_20-00_empire_mensonge_concepts_extraits_HYPER_MATRICE.md
│   ├── 2026-06-26_18-30_consolidation_5_enquetes_ANALYSE.md        ← analyse transverse
│   ├── 2026-06-26_21-00_synthese_7_enquetes_FRESQUE.md            ← synthèse cumulative
│   ├── 2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md     ← référentiel archéologique
│   ├── 03_framework/README.md       ← documentation détaillée du framework
│   └── archive/                     ← protocoles v1.x
```

---

## Comment utiliser le projet

### Lire la fresque

1. **Commencer par le TABLEAU_DE_BORD.md** (dans `03_framework/`) — il agrège les 10 enquêtes v2.4, leurs synthèses, le statut Pelote, et la file d'attente. C'est le point d'entrée unique.
2. **Plonger dans une enquête** dans `02_enquetes/` — chaque investigation est une fiche YAML autonome avec sources vérifiées, contre-version, REMONTEE_DES_FILS standardisée, et CONTRE_MESURES.
3. **Consulter le protocole** dans `03_framework/` pour comprendre les 10 fils (A-L), les 42 mécanismes (M01-M42), et la Méthode de la Pelote de Laine.

### Lancer une nouvelle enquête (protocole v2.4 — Pelote de Laine)

1. Consulter le **TABLEAU_DE_BORD.md** pour la file d'attente et les priorités
2. Ouvrir `03_framework/2026-06-26_21-00_prompt_investigation_v2_PROMPT.md` (v2.4)
3. Suivre le workflow du protocole v2.4 :
   - **Étape 0** : Recherche documentaire (recherches web, HEAD checks, citations directes)
   - **Étape 0 bis** : **Pelote de Laine** — appliquer l'algorithme 5 questions récursives pour remonter chaque fil jusqu'à son acte fondateur. Format de sortie obligatoire : `[AAAA] — événement — [M##]`
   - **Étape 1** : Lancer l'enquête via le prompt
   - **Étape 2** : Produire la fiche YAML (14 chapitres dont REMONTEE_DES_FILS + CONTRE_MESURES, sources vérifiées)
   - **Étape 3** : Auto-vérification (4 questions système)
   - **Étape 4** : Ultrathinking (obligatoire degré 4-5, format ADDENDUM)
   - **Étape 5** : Vérification NREF (12 exigences dont NREF-11 Pelote et NREF-12 Contre-mesures, niveaux A-E)
   - **Étape 5 bis** : Vérification par second agent (contre-expertise)
   - **Étape 6** : Mettre à jour le TABLEAU_DE_BORD.md
4. Sauvegarder la fiche YAML produite dans `02_enquetes/`

---

## Version du protocole

| Version | Date | Changement |
|---------|------|------------|
| v1.0 | 2026-06-25 | 8 fils fondateurs (sang contaminé) |
| v1.1 | 2026-06-25 | 33 mécanismes actifs (7 articles Resistance Cognitive) |
| v1.2 | 2026-06-25 | +9 mécanismes M34-M42, +10 résistances R01-R10 (Empire du Mensonge) |
| v1.3 | 2026-06-25 | Séparation prompt/protocole, YAML simplifié, autonomie du LLM |
| v2.0 | 2026-06-26 | Refonte NREF : 6 nouveaux chapitres, barème 8 exigences, workflow vérification |
| **v2.1** | **2026-06-26** | **Renforcement post-audit : sources vérifiées, HEAD checks, 10 exigences, Ultrathinking obligatoire, second agent** |
| **v2.4 (Pelote)** | **2026-06-26** | **Pelote de Laine (algorithme 5 questions récursives), REMONTEE_DES_FILS standardisé (marquage, gaps, cross_ref), CONTRE_MESURES, 12 exigences NREF, workflow 14 chapitres** |

---

## Contexte plus large

Ce dossier est un module du projet Truth Engine. Les investigations produites ici alimentent la base Mnemolite (RAG vectoriel). Les articles de la Résistance Cognitive (103 articles, Substack) sont la source conceptuelle des mécanismes.

Voir `AGENTS.md` à la racine du projet pour les règles opératoires.

### Enquête de référence

La première enquête produite avec le protocole v2.1 est **l'affaire du sang contaminé** (1984-2003). Elle sert de démonstrateur et de test du workflow complet (étapes 0 à 6). Résumé :
- **Niveau NREF :** B (vérifiable, sources déclarées honnêtement)
- **Sources :** 1 ✦ (HEAD 200 OK) + 3 ⁅ (Legifrance anti-bot) + 4 ❧ (papier/non trouvé)
- **5 mécanismes dominants :** M14 (Impuissance apprise), M23 (Ingénierie de la possession), M05 (Perfusion publique), M28 (DARVO), M11 (Kayfabe politique)
- **8 fils tous actifs :** verrouillage complet (degré 5/5)
- **Ultrathinking :** ✅ réalisé (6 sections, 2 pistes P1/P2)
- **Second agent :** 🔲 à réaliser

Voir le détail dans `02_enquetes/2026-06-26_sang_contamine_v2.3_INVESTIGATION.md`.
