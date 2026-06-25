# SUBLIMATOR v33.2 — Design : extraction rigoureuse des enquêtes

**Date** : 2026-06-06 (révision 2)
**Statut** : Design révisé, en attente validation user
**Contexte** : v33.1 sous-exploite les 11 enquêtes (60K mots). Bug : §9.4 suppose F### existants. Refonte validée : 12 sections quintessence + 3 inputs (F001/F-CIV-XXX/items N. **).

## §0 PROBLÈME

Audit de v33.1 (spec 1422 lignes, 52K chars) révèle :
- `FACT_REGISTRY` : 5 mentions, pas de process d'extraction
- `extraction` : 5 mentions, aucune méthode
- `F###` : 3 mentions, format non spécifié
- `✦/✧/⁅/❧` : 0 mention (scoring absent)
- `KERNEL.md` : 0 mention
- `quintessence` : 0 mention

**Audit réel des 11 enquêtes** :
- F001-F020 (format ancien) : 59 occurrences dans 4 fichiers (M-A 20, Islam 14, Inde 13, Amériques 12)
- F-CIV-XXX (nouveau) : 0 occurrence
- Items "N. **" : 124 occurrences dans 9 fichiers (Sumer 17, Rome 16, Sumer Iceberg 17, M-A 42, Islam 12, Andurarum 10, Rome Iceberg 4, Inde 3, Amériques 3)
- Sections analytiques (18 par enquête) : §2 MANIPULATION_REPORT, §3 CLUSTERS, §4 HERMÉNEUTIQUE L1-L6, §5 FORENSIC, §7 CHRONOLOGIE, §8 DOMAINES, §11 PREUVES, §14 CONNAISSANCES, §15 SUSPICION SCORES — **non capturées** par le design initial (9 sections)

**Conséquence** : article draft v33.1 a 21 F### (extraits manuels), 5/8 civilisations. Aucune extraction rigoureuse.

## §1 SOLUTION : 5 ajouts à v33.1 → v33.2 (révision 2)

### §X EXTRACTION ATOMIQUE (NOUVELLE)

Module extraction `inputs hétérogènes → F### atomiques unifiés`.

#### §X.1 Inputs acceptés (3 formats) + méthodologie canonique

**Référence KERNEL.md** : v33.2 n'invente pas la roue, il étend KERNEL.md. La méthodologie canonique d'extraction est KERNEL §10 FACT_REGISTRY (process atomique), §14 OUTPUT (structure investigation 15 sections APEX), §19 SAVE (mnemolite + write obligatoires). v33.2 = implémentation sublimator de KERNEL pour agregation multi-enquêtes.

**3 formats acceptés en entrée** :

1. **F001-F099 (format ancien)** : présents dans 4 fichiers (M-A, Islam, Inde, Amériques). Détection : regex `\bF0\d{2}\b`.
2. **F-CIV-XXX (nouveau format)** : cible v33.2, plus rare (0 actuellement). Détection : regex `F-[A-Z]+\d+`.
3. **Items numérotés "N. **...**"** : 124 occurrences dans 9 fichiers. Détection : regex `^\d+\.\s+\*\*[^*]+\*\*`.

#### §X.2 Mapping automatique (F001 → F-CIV-XXX)

| F001 source | → | F-CIV-XXX cible |
|-------------|---|-----------------|
| M-A : F001-F020 | → | F-MA001-F-MA020 |
| Islam : F001-F014 | → | F-I001-F-I014 |
| Inde : F001-F013 | → | F-IN001-F-IN013 |
| Amériques : F001-F012 | → | F-AM001-F-AM012 |
| Sumer/Rome/Chine (sans F001) | → | F-S001+, F-R001+, F-C001+ (extraction directe) |

**Préfixes civilisation** : S=Sumer, R=Rome, C=Chine, MA=M-A, I=Islam, IN=Inde, AM=Amériques, A=Andurarum.

#### §X.3 Format F-CIV-XXX (9 champs YAML)

```yaml
- id: F-S001
  fait: "30 annulations générales de dettes entre 2400 et 1400 av. J.-C."
  date: "2400-1400 av. J.-C."
  acteur: "Rois sumériens (Urukagina, Lipit-Ishtar, etc.)"
  chiffre: "30 annulations"
  source: "tablettes sumériennes, archives BM Londres"
  url: "https://..."
  fiabilite: "✦"  # ✦ ✧ ⁅ ❧
  notes: "inclut 5-8 purement sumériennes, 22 babyloniennes"
  source_section: "§1 RÉSUMÉ EXÉCUTIF"  # traçabilité
  input_format: "F001"  # ou "F-CIV-XXX" ou "item N.**"
```

#### §X.4 Process 3 passes

- **Passe 1 regex** : extraction automatique depuis les 3 formats
- **Passe 2 lecture cursive** : §1 résumé, §18 ICEBERG, §10 chaînes, §9 réseau, §6 prisme, §7 chronologie, §8 domaines
- **Passe 3 curation humaine** : dédoublonnage, scoring ✦, ajout contexte

#### §X.5 Minima quantitatifs (par enquête)

- SIMPLE : ≥10 F###
- MEDIUM : ≥15 F###
- COMPLEX : ≥25 F###
- APEX : ≥35 F###

#### §X.6 Validation + GATE_G audit complétude

**Validations unitaires** :
- URL accessible via HEAD request (HEAD 200 OK → ✦/✧ ; 4xx/5xx → ⁅ ; pas d'URL → ❧)
- Dédoublonnage (Jaccard < 0.7 sur champ "fait")
- Format YAML respecté
- Traçabilité : chaque F### référence sa `source_section` enquête

**GATE_G — Audit de complétude** (LOI L16) :

Métrique : `complétude = n_faits_matrice / n_phrases_avec_chiffre_ou_acteur_ou_date * 100`

Cible par niveau de complexité :
- SIMPLE : ≥70%
- MEDIUM : ≥80%
- COMPLEX : ≥85%
- APEX : ≥90%

**Si GATE_G fail** :
- HALTE pipeline de la cellule
- Re-extraction ciblée sur les zones sous-exploitées (sections sans F###)
- Si 2e tentative échoue : signalement à l'humain, enrichissement manuel

**Calcul** : agent E (humain) peut rejouer GATE_G après validation pour traçabilité.

#### §X.7 Workflow 4 agents + humain (séquentiel)

Pipeline de la cellule d'extraction (1 enquête → 1 fiche). 5 étapes, séquentielles.

**Agent A — Script Parseur (mécanique, gratuit, ~1-2 min)**

- Input : fichier .md enquête
- Process : regex sur 3 formats
  - F001 : `r"\bF0\d{2}\b"` → liste `{id_old, contexte_brut, line_no}`
  - F-CIV-XXX : `r"F-[A-Z]+\d+"` → idem
  - Items N. ** : `r"^\d+\.\s+\*\*([^*]+)\*\*"` → `{num, item_brut, line_no}`
- Output : JSON candidats F### bruts
- Garanties : reproductible, exhaustivité mécanique, ne manque aucun F### balisé

**Agent B — LLM Lecteur Cursif (~10-20 min)**

- Input : JSON candidats (A) + texte intégral enquête
- Process séquentiel des 18 sections :
  1. Lit §1 résumé → sort Thèse centrale + 3 thèses implicites
  2. Lit §2 MANIPULATION_REPORT → sort rhétorique (DEM/BF/NUM/AUTH/FAC, ⊕⊗⊙)
  3. Lit §3 CLUSTERS → sort clusters dominants (Ξ€ΛΩΨ↕ΦΣΚρκ⫸⚔🌐⏰)
  4. Lit §4 HERMÉNEUTIQUE → sort L1-L6 (interprétations multi-niveaux)
  5. Lit §5 FORENSIC → sort raisonnements (indices/empreintes)
  6. Lit §6 PRISME + §12 CARTE → sort 3 perspectives dialectiques
  7. Lit §7 CHRONOLOGIE → sort 5-10 dates clés
  8. Lit §8 DOMAINES → sort 5-7 thématiques
  9. Lit §9 RÉSEAU → sort Acteurs (5-15 noms propres)
  10. Lit §10 CHAÎNES → sort 3-5 causalités ≥3 liens
  11. Lit §11 PREUVES → sort sourcing ↔ claims
  12. Lit §13 LIMITES → sort 3-5 limites
  13. Lit §15 SUSPICION → sort 3-5 scores
  14. Lit §16 WOLVES → sort 3-5 acteurs malveillants
  15. Lit §17 REQUEST_LOG → sort URLs classées par tier
  16. Lit §18 ICEBERG → sort 3-5 angles morts
- Pour chaque F### candidat (A), B enrichit avec `source_section` + contexte
- B identifie aussi les F### non-balisés dans le texte (faits implicites)
- Output : JSON enrichi (candidats A + ajouts B) + 11 sections analytiques

**Agent C — LLM Curator (~5-10 min)**

- Input : sortie B (JSON enrichi)
- Process :
  1. Fusion candidats A + ajouts B (préférer B pour contexte, A pour traçabilité)
  2. Dédoublonnage (Jaccard < 0.7 sur champ "fait")
  3. Scoring ✦/✧/⁅/❧ :
    - URL primaire accessible + 2+ sources concordantes → ✦
    - URL accessible + 1 source fiable → ✧
    - URL inactive ou tier 2-3 → ⁅
    - Pas d'URL ou inférence pure → ❧
  4. Mapping F001 → F-CIV-XXX (F-MA001, F-I001, etc.)
  5. Ajout `source_section` pour chaque F### (traçabilité enquête)
- Output : matrice YAML 12 sections de quintessence

**Agent D — LLM Verifier (~5-10 min)**

- Input : matrice curator (C) + JSON enrichi (B) + texte enquête
- Process :
  1. Relit intégralement l'enquête
  2. Compare avec matrice curator
  3. Signale :
    - (a) F### manquants (faits passés sous silence)
    - (b) Incohérences thèses vs F###
    - (c) Acteurs oubliés
    - (d) Causalités non quantifiées
    - (e) Faux URL (typos, sources inventées)
    - (f) ICEBERG/WOLVES sous-exploités
  4. Propose ajouts/rectifications
- Output : rapport de vérification (signalements) + ajouts proposés

**Agent E — Humain valide (5-10 min)**

- Input : matrice curator (C) + rapport verifier (D)
- Process :
  1. Lit les deux
  2. Décide : valider / modifier / refuser / enrichir (4 actions, comme CP)
  3. Si refus : retour à C (curator) ou D (verifier) avec consignes
  4. Max 2 boucles (sinon HALTE)
- Output : fiche quintessence finale

**Total cellule** : ~25-50 min/enquête. Pour 11 enquêtes : 5-9h. Pour 20 : 9-15h.

**Scalabilité** : 1 cellule = 1 enquête, indépendamment. On peut séquentiel (11 en 5-9h) ou batch parallèle (selon ressources workers).

### §W QUINTESSENCE 12 SECTIONS (NOUVELLE — refonte 9→12)

La quintessence d'une enquête = extraction de TOUTE la matière utile, pas seulement les F###. 12 sections :

| # | Section | Source enquête | Format |
|---|---------|----------------|--------|
| 1 | **Thèse centrale** | §1 résumé exécutif | 1 phrase assertive |
| 2 | **3 thèses implicites** | §1 + §18 ICEBERG | 3 bullets |
| 3 | **F### atomiques** | tous §X | 15-35 YAML items |
| 4 | **Acteurs/Network** | §9 Réseau | 5-15 noms propres |
| 5 | **Causalités** | §10 Chaînes | 3-5 chaînes ≥3 liens |
| 6 | **3 perspectives dialectiques** | §6 Prisme + §12 Carte | ⟐/🔥/◈ forces égales |
| 7 | **Limites** | §13 Périmètre | 3-5 limites méthodologiques |
| 8 | **Wolves** | §16 | 3-5 acteurs malveillants nommés |
| 9 | **Iceberg** | §18 | 3-5 angles morts/auto-critiques |
| 10 | **Chronologie** | §7 | 5-10 dates clés |
| 11 | **Domaines** | §8 | 5-7 thématiques couvertes |
| 12 | **URLs prioritaires** | §17 Request log | 5-10 sources |

**Changement vs v1** : Auto-critique (v1) → 3 sections séparées (Limites/Wolves/Iceberg) + ajout Chronologie (§7) + Domaines (§8). Garantit capture des 18 sections analytiques enquête.

**Output** : 1 fichier `_quintessence/<civ>_quintessence.yaml` par enquête (~3-5K chars).

### §W.13 Agrégation N fiches → matrice maître

Pipeline post-extraction, applicable à tout N (2 à 20+).

**Étape 1 : Compile matrice maître**

- Compile les F### de toutes les fiches en 1 table unique
- Déduplique par Jaccard < 0.7 sur `fait` OU par acteurs communs OU par dates communes
- Pour 11 enquêtes MEDIUM : ~200-330 F### uniques
- Pour 20 enquêtes : ~400-600 F###

**Étape 2 : Détection transversalités**

Agent LLM transversaliste :
- Input : matrice maître (200-330 F###)
- Process : identifie les F### qui apparaissent (ou dont le concept est cité) dans ≥3 enquêtes
- Output : liste transversalités (10-30 concepts partagés)

**Étape 3 : Brainstorm thèses bottom-up**

Agent LLM brainstormer :
- Input : matrice maître + transversalités + 11 fiches
- Process : étant donné la matière extraite, quelles thèses cardinales émergent ?
- Output : 3-5 thèses cardinales candidates avec F### justificatifs

**Étape 4 : Choix humain**

- L'humain arbitre entre les thèses candidates
- Valide / modifie / refuse
- Cohérent avec la logique CP1/CP2/CP3 de v33.1

**Étape 5 : Réécriture article**

- Sur la base des thèses validées
- Utilise la matrice complète (vs 21 F### actuels)
- Cible 5500-8000 mots avec sourcing 90%+

**Total agrégation** : ~30-60 min. Wall-time dominé par les 5-9h d'extraction.

**Scalabilité** : N enquêtes → 1 matrice, complexité O(N²) pour dédoublonnage mais N=20 reste gérable.
