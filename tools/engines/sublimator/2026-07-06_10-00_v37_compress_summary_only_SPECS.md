# 2026-07-06_10-00_v37_compress_summary_only_SPECS.md

> **Type :** SPECS (spécifications techniques actionnables)
> **Cible :** Phase 1 du Sublimator v37 v2 (Format-Aware). Remplace la Phase 1 v36 (LECTEUR + EXTRACTEUR JSON 24-champs) et l'ébauche v37 v1 (compress_summary ≤100 mots strict, audit-aveugle).
> **Origine :** audit empirique 2026-07-05 (vs v36) + audit empirique 2026-07-06 (diversité 42 enquêtes RIC, 10 formats détectés).
> **Statut :** DRAFT v2. À valider par implémentation-test sur 5 enquêtes RIC couvrant 5 formats distincts.
> **Conventions projet :** cf. `knowledge.md` (français soutenu, pas de tirets cadratins U+2014, sourcing strict, anti-fabrication).
> **Changelog :** v2 (2026-07-06) ajoute Annexe conditionnelle format-aware (≤200 mots/annexe, total ≤300 mots/enquête) et validateur Python étendu M0-M7 (10 formats reconnus). v1 (2026-07-06 matin) réduction v36 à compress.md ≤100 mots brut.

---

## §0. Métadonnées du document

| Champ | Valeur |
|-------|--------|
| Version Sublimator | v37 v2 (Format-Aware) |
| Date rédaction | 2026-07-06 14:00 UTC |
| Phase couverte | Phase 1 uniquement (sub-agent unique avec détection format et Annexe conditionnelle) |
| Fichiers impactés | 4 créés, 6 supprimés, 2 modifiés (cf. §14 plan d'implémentation) |
| Auteur | Buffy (orchestrateur LLM hôte) + thinker-with-files-gemini (audit format-diversité) |
| Statut validation | NON-VALIDÉ. Doit passer Test A/B juge de paix (§12) sur 5 enquêtes couvrant 5 formats. |

---

## §1. But et intention utilisateur

### 1.1 But déclaré du Sublimator (cité verbatim de `prompt-v35.md`)

> « Tu transformes N enquêtes journalistiques en 1 article publiable. »

### 1.2 Intention explicite de l'utilisateur (citée verbatim du brief Phase 1)

> « Le besoin final est d'écrire un article. Nous avons N enquêtes (longues) il faut en extraire ce qui sera utile en vue de réfléchir à l'écriture de l'article. Les enquêtes ont des data intrinsèquement inutiles et d'autres utiles. **Il faut trier et extraire.** Une fois que l'on aura ces extractions (quintessences) le LLM aura moins de bruits pour réfléchir à produire des thèses, relier les points (le fameux dessin point à point où l'on relie des nombres pour former une image). »

### 1.3 Triade de cohérence v37 v2

| Couche | But | Traduction Phase 1 v37 v2 |
|--------|-----|---------------------------|
| Sublimator | N enquêtes vers 1 article | Phase 1 doit CONDENSER (denoiser) le signal |
| Utilisateur | trier, extraire, moins de bruit | Phase 1 doit produire un signal COMPARABLE inter-enquêtes |
| Phase 2 (clustering) | relier les points | Phase 1 doit isoler les **briques comparables** + préserver les **listes opérationnelles** par format |
| Phase 3 (article) | rendre actionnable | Phase 1 doit préserver les détails opérationnelle (Plan T+, contacts experts, articles juridiques, pays comparés) **PROPRES AU FORMAT de l'enquête source** |

**Cohérence validée v37 v2** : le design Phase 1 est **filtre anti-bruit + préservateur d'opérationnel par format détecté**. Toute fonctionnalité qui ne sert ni le filtrage ni la préservation opérationnelle format-spécifique est SUR-INGENIERIE.

---

## §2. Diagnostic forensique de la Phase 1 v36 (audit empirique 2026-07-05)

### 2.1 Mesure de volume production vs brut

| Enquête échantillon | Mots enquête brute | Mots lecteur prod | Mots quintessence JSON prod | Ratio Phase 1 / brut |
|---------------------|---------------------|-------------------|----------------------------|----------------------|
| `2026-07-04_18-00_referendum_initiative_citoyenne` | 8400 | 3500 | 6000 | 1.13 |
| `2026-07-04_19-30_ric_bce_euro_verrou` | 11700 | non produit | non produit | N/A |
| `2026-07-04_20-30_ric_bloc_religieux_verrou` | 9800 | non produit | non produit | N/A |
| `2026-07-04_22-30_ric_coordination_europeenne` | 10400 | non produit | non produit | N/A |
| `2026-07-04_23-50_cross_examination_ric` | 11800 | non produit | non produit | N/A |

**Mesure cardinale (RIC 18:00 prod manuelle) :** Phase 1 v36 produit 9500 mots pour 8400 mots d'enquête source. **Ratio 1.13:1** = Phase 1 ajoute du volume au lieu de condenser. **Anti-denoising constaté.**

Extrapolation pour 42 enquêtes RIC : Phase 1 actuelle produirait ~350 000 mots de fichiers intermédiaires pour ~370 000 mots d'enquêtes brutes. **Aucun gain net de signal.**

### 2.2 Analyse des 24 champs top-level du schéma quintessence v36

Audit empirique (RIC 18:00) classant chaque champ selon son origine dans l'enquête source :

| # | Champ | Origine dans l'enquête | Catégorie | Verdict v36 | Verdict v37 v2 |
|---|-------|------------------------|-----------|-------------|----------------|
| 1 | `enquete_id` (str) | nom de fichier | Métadonnée triviale | KEEP | KEEP trivial |
| 2 | `enquete_source` (str) | chemin relatif | Métadonnée triviale | KEEP | KEEP trivial |
| 3 | `these_centrale` (str) | §0 verbatim | **Recopie conforme** | KEEP | KEEP (champ Thèse compress.md) |
| 4 | `faits_atomiques[]` | §10 §FACT_REGISTRY (24 F-###) | **Recopie conforme** | TRIM (5-7 max) | TRIM (5-7 max) |
| 5 | `urls_prioritaires[]` | §5 ou §6 épars | **Recopie conforme** | TRIM (2-3 max) | intégré F-### si tier 1 |
| 6 | `shadow_factor` (float) | ABSENT de l'enquête | **Invention LLM** | KILL | KILL |
| 7 | `theses_implicites[]` | Inférences LLM | **Invention LLM** | KILL | KILL |
| 8 | `acteurs[]` (legacy flat) | §3 acteurs | **Recopie conforme** | KILL (doublon positions_acteurs) | KILL |
| 9 | `causalites[]` (legacy) | §11 PELOTE résumé | **Recopie conforme** | KILL (doublon causalites_pelote) | KILL |
| 10 | `causalites_pelote[]` (4 niveaux arborescents) | §11 PELOTE arborescence | **Re-encodage JSON** | TRIM (chaîne logique prose) | KILL (préservé en Annexe si format=JURIDIQUE/PROCÉDURE) |
| 11 | `perspectives_dialectiques[]` | §7 verbatim | **Recopie conforme** | KILL (intégré transversalité) | KILL |
| 12 | `limites[]` | §16 limites | **Recopie conforme** | KILL (pas opérationnel Phase 2) | KILL |
| 13 | `wolves[]` (wolf_score inventé) | ABSENT | **Invention LLM (taxonomie inventée)** | KILL | KILL |
| 14 | `iceberg{}` (stratigraphie) | §2 surface/intermediate/deep | **Recopie conforme** | KILL (pas comparable) | KILL |
| 15 | `chronologie[]` | §3.1 + §11 dates | **Recopie conforme** | KILL (pas comparable) | KILL sauf si format=HISTORIQUE → préservé en Annexe |
| 16 | `domaines[]` (tags) | ABSENT | **Invention LLM** | KILL | KILL |
| 17 | `mnemo_queries[]` (queries RAG) | ABSENT | Contrat aspirational | KILL | KILL |
| 18 | `positions_acteurs[]` | §3.3 + §9 acteurs/positions | **Recopie conforme** | TRIM (2-3 max) | TRIM (2-3 max) |
| 19 | `impact[]` (chiffres) | §5 + §11 chiffres épars | **Recopie conforme** | TRIM (3-5 max) | TRIM (3-5 max) |
| 20 | `recommandations[]` (5 items) | §15 contient 5 AUTRES recos | **Invention LLM** | KILL | KILL (préservé en Annexe si format=PROCÉDURE sous titre "Composants T+") |
| 21 | `compress_summary` (≤100 mots) | NOUVEAU (jamais dans l'enquête) | **Seul vrai signal de denoising (facteur ×100)** | KEEP → fichier autonome | KEEP → fichier autonome + Annexe conditionnelle (≤200 mots) |

### 2.3 Verdict tranché du diagnostic v36 → v37 v2

**Décompte final v36 :**

| Catégorie | Compte | Pourcentage |
|-----------|--------|-------------|
| Recopies conformes (valeur ajoutée ≈ 0) | 8 champs | 40% |
| Re-encodages JSON (valeur ajoutée ≈ 0) | 1 champ | 5% |
| Inventions LLM (hallucination imposée par le schéma) | 7 champs | 35% |
| Métadonnées triviales | 2 champs | 10% |
| **Signal pur de denoising** | **1 champ** | **5%** |
| Autres | 1 champ | 5% |

**Ratio signal/bruit du design Phase 1 v36 :** 1/20 = 5%. **Très en-dessous du seuil opérationnel (≥30%)** pour qu'un agent LLM Phase 2 puisse travailler efficacement sur le signal.

**Conclusion forensique v36 :** Phase 1 v36 est SUR-ENGINEERED au point de produire plus de texte qu'elle filtre.

**Évolution v37 v2** : Phase 1 doit ajouter un **mode préservation par format** pour conserver les listes opérationnelles/contacts/architectures chiffrées absentes du signal mais vitales à l'article final. Cette préservation est conditionnelle (déclenchée par détection format ≠ ANALYTIQUE), ce qui maintient le denoising fort au global.

---

## §3. Design cible Phase 1 v37 v2 (Format-Aware)

### 3.1 Architecture : UN sub-agent unique avec détection format

**Fusion LECTEUR + EXTRACTEUR en un seul sub-agent** plus **détection dynamique du format d'enquête**. Raisons forensiques §1 validées :

1. Le passage LECTEUR (Markdown 3500 mots) vers EXTRACTEUR (JSON 6000 mots) cause une **perte sémantique** opérationnel (cf. audit 2026-07-06).
2. Un agent unique a le contexte complet en mémoire de travail à l'instant de la synthèse ET de la détection format.
3. Suppression d'une étape = suppression des retries `sublimator_retry.py` sur erreurs de format JSON.
4. **Nouveau v37 v2** : l'agent unique détecte le format parmi 10 possibles et préserve l'opérationnel via Annexe conditionnelle.

### 3.2 Architecture cible v37 v2

```
[ENQUÊTE INPUT]
    investigations/<sujet>/<prefix>_INVESTIGATION.md
                          |
                          v
       +------------------+------------------+
       |  Sub-agent UNIQUE :                |
       |  compress_summary_extractor.md     |
       |                                     |
       |  Etape 1 : Synthese standard      |
       |  (Thèse + F-### + Chiffres +       |
       |   Acteurs + Transversalité)        |
       |  5 sections, ≤120 mots             |
       |                                     |
       |  Etape 2 : Détection format        |
       |  (10 formats : PROCÉDURE/MÉTA/     |
       |  JURIDIQUE/COMPARAISON/HISTORIQUE/ |
       |  TECHNIQUE/SONDAGES/SOCIOLOGIE/    |
       |  MÉDIATIQUE/ANALYTIQUE)            |
       |                                     |
       |  Etape 3 (si format ≠ ANALYTIQUE) :|
       |  Annexe conditionnelle             |
       |  ≤200 mots, listes opérationnelles |
       +------------------+------------------+
                          |
                          v
[COMPRESS SUMMARY OUTPUT avec Format détecté]
    investigations/<sujet>/_quintessence/<prefix>_compress.md
                          |
                          v
       +------------------+------------------+
       |  Auto-Audit Sub-Agent CRITIQUE :   |
       |  FilePaths = [<compress>.md,       |
       |               <enquete>.md]        |
       |  8 critères M0-M7 vérifiés         |
       |  via reproduction LLM              |
       |  (2026-07-06: validateur Python     |
       |   compress_validate.py retiré)     |
       +------------------+------------------+
                          |
                          v
[FEEDBACK PASS / FAIL]
    - PASS : compress.md utilisable Phase 2 (Annexe préservée)
    - FAIL : note_violation + retry compress
```

### 3.3 Volume cible par enquête (ajusté pour Annexe format-conditionnelle)

| Format | Volume par enquête | Pour 42 enquêtes | Compression vs brut |
|--------|---------------------|------------------|---------------------|
| Brut (enquêtes) | 10 000 mots (moyenne) | 420 000 mots | 1.0× (référence) |
| **compress.md cible (standard)** | **≤120 mots (tolérance +20%)** | **≤5 040 mots** | **≥83×** |
| Annexe format-conditionnelle | ≤200 mots (si format détecté ≠ ANALYTIQUE) | ≤8 400 mots | ≥50× sur la part préservée |
| **Total compress.md + Annexe** | **≤320 mots/enquête max** | **≤13 440 mots** | **≥31×** |

**Hausse du plafond justifiée par audit empirique 2026-07-06** (cf. §3bis) : la limite stricte de 100 mots v37 v1 détruit les listes opérationnelles présentes dans les formats PROCÉDURE (plan T0/T+6/T+12/T+18/T+36), MÉTA (37 questions sectorielles, 12 failles LLM), JURIDIQUE (articles de loi verbatim), COMPARAISON (pays comparés). Ces listes sont nécessaires à Phase 3 pour produire un article actionnable. L'Annexe conditionnelle préserve l'opérationnel sans dégrader le denoising de la synthèse standard.

**Note technologique :** 320 mots à 4 caractères/mot = environ 1 280 tokens. 42 fichiers = 53 760 tokens. **Tout LLM moderne ingère ce volume sans RAG, sans long-context étendu, sans perte de contexte.**

---

## §3bis. Détection du format d'enquête (audit empirique 2026-07-06)

### 3bis.1 Les 10 formats identifiés empiriquement sur 42 enquêtes RIC

Audit des 42 fichiers `investigations/2026-07-04-RIC/*INVESTIGATION.md` révèle une diversité de 10 formats structurants, chacun avec des **listes opérationnelles uniques** que le compress_summary ≤100 mots v37 v1 détruit mécaniquement.

| # | Format | Préfixes marqueurs | Wordcount typique | Annexe requise |
|---|--------|---------------------|-------------------|----------------|
| 1 | **PROCÉDURE** | `protocole_pnred_`, `strategie_imposition_mise_en_place_`, mots-clés "Jalon T+", "Pack Données" | 6 200-9 700 | **OUI** : jalons chronologiques + architecture technique chiffrée + loups nominatifs |
| 2 | **MÉTA / AUDIT EXTERNE** | `external_legal_audit`, `verification_independante`, mots-clés "experts nominatifs", "failles LLM" | 8 000-8 400 | **OUI** : 30-50 questions sectorielles + failles graduées + contacts experts |
| 3 | **JURIDIQUE FORENSIQUE** | `loi_`, `juridique_`, articles de loi cités verbatim (Code pénal art., Loi organ.) | 7 000-12 200 | **OUI** : articles juridiques stricts + précédents CC/CEDH |
| 4 | **COMPARAISON INTERNATIONALE** | `_italie_`, `_bavierr_`, `_bavaria_`, `_verfassung_`, `_dao_`, `_decidim` | 2 800-7 600 | **OUI** : pays comparés + critères + leçons France |
| 5 | **HISTORIQUE LONGUE** | `histoire_longue_`, `_1946_`, `_1958_`, `_republique_`, `_cnr_` | 7 400-8 500 | **OUI** : chronologie datée acteurs + évolution doctrinale |
| 6 | **TECHNIQUE / INFRA** | `civictech_`, `infrastructure_electorale_privee`, `_ia_generative_`, mots-clés "ANSSI", "SecNumCloud" | 2 800-12 200 | **OUI** : stack technique chiffrée + coûts M€ + risques |
| 7 | **SONDAGES / MÉTHODOLOGIE** | `sondages_`, `_methodologie_`, "IFOP", "IPSOS" | 2 900-3 000 | **OUI** : panel CSP sociologique + résultats chiffrés + limites instituts |
| 8 | **SOCIOLOGIQUE** | `profil_sociologique_`, `indifference_priorite_` | 5 200-5 400 | **OUI** : leviers comportementaux + profil CSP cible |
| 9 | **MÉDIATIQUE** | `media_hostile_`, `cadrage_media_` | 6 900 | **OUI** : cartographie propriétaires Bolloré-Vivendi-LVMH-Dassault |
| 10 | **ANALYTIQUE RIC-pur** | `referendum_initiative_citoyenne`, `ric_bce_euro_verrou`, `ric_complement_gaps`, `ric_verrous_impersonnels`, etc. | 5 600-8 400 | **NON** : la synthèse standard suffit (transversalité par les F-### chiffrés acteurs) |

### 3bis.2 Données perdues par compress_summary ≤100 mots si pas d'Annexe

Mesure empirique (audit 2026-07-06 sur 2 fichiers APEX) :

Pour **protocole_pnred_ric_001** (9 733 mots) :
- Plan T0/T+6/T+12/T+18/T+36 (séquence d'ingénierie précise) : 5 jalons détaillés avec composants comptés.
- Architecture 3-couches Pack Données Souveraines (SecNumCloud 1.5M€/an + X-Road FR 0.5-2M€/an + Papier-First 0.5M€/an) : 3 composants avec coûts individualisés.
- 12 fils systémiques à couper (Banque/Supermarché/Téléphone/Voiture/Énergie/Internet/etc.) : liste nommante des dépendances à l'État.
- 9 leviers économiques chiffrés (boycott catégories fiscales, retrait coopératives, etc.) avec effet État.
- 8 scénarios Judo Rhétorique (actualité → réponse RIC universelle).
- 20+ loups nominatifs opérationnels avec affiliations et postures.

Pour **external_legal_audit** (8 360 mots) :
- 37 questions sectorielles spécifiques (15 Constitutionnelles + 10 CivicTech + 12 Législatives).
- 12 failles LLM pressenties graduées CRIT (4) / ÉLEV (4) / MOD (4).
- 5 experts nominatifs cibles (Dominique Rousseau, Ferdinand Melin-Soucramanien, Sami Tucka, Tiago Peixoto, spécialiste Législatif Sénat/AN).
- Budget détaillé par catégorie expert (500-5 000€).
- Délai T0 → clôture (8-12 semaines).
- Email template de sollicitation.

**Sans Annexe, le LLM Phase 2 reçoit uniquement la thèse + 5 F-### génériques + 3 chiffres + 2 acteurs**, ce qui produit un article final privé de toute la granularité opérationnelle (sans Plan 18 mois, sans liste de loups, sans architecture chiffrée).

### 3bis.3 Heuristique de détection automatique

**Règle de priorité** : nom de fichier (préfixe) > sections présentes > mots-clés dans §0 ou §1.

```python
FORMAT_KEYWORDS = {
    'PROCÉDURE': [r'(?i)(protocole|pnred|strategie|mise_en_place)',
                  r'(?i)Jalon T\+', r'(?i)Pack Donn'],
    'MÉTA': [r'(?i)(external_legal_audit|audit_externe|verification_independante)',
             r'(?i)experts nominatifs', r'(?i)failles? LLM'],
    'JURIDIQUE': [r'(?i)(loi_|juridique|legifrance)',
                  r'(?i)Code pénal', r'(?i)Conseil Constitutionnel', r'(?i)CEDH'],
    'COMPARAISON': [r'(?i)(italie|bavierr|bavaria|verfassung|dao|decidim|m5s)'],
    'HISTORIQUE': [r'(?i)(histoire_longue|1789|1946|1958|republique|cnr)'],
    'TECHNIQUE': [r'(?i)(civictech|infrastructure_electorale|ia_generative)',
                  r'(?i)(ANSSI|SecNumCloud|X-Road|Cloud Act)'],
    'SONDAGES': [r'(?i)(sondages|methodologie|ifop|ipsos)'],
    'SOCIOLOGIE': [r'(?i)(profil_sociologique|indifference)'],
    'MÉDIATIQUE': [r'(?i)(media_hostile|cadrage_media)'],
}
```

**Défaut** : si aucun mot-clé ne match, classifier comme ANALYTIQUE (RIC-pur). Pas d'Annexe requise dans ce cas (la synthèse standard avec F-### + transversalité couvre le besoin).

---

## §4. Schéma Markdown du compress_summary (Format-Aware)

### 4.1 Format canonique (5 sections + Annexe conditionnelle)

```markdown
# Quintessence : [enquete_id]

**Format détecté** : [PROCÉDURE | MÉTA | JURIDIQUE | COMPARAISON | HISTORIQUE | TECHNIQUE | SONDAGES | SOCIOLOGIE | MÉDIATIQUE | ANALYTIQUE]

**Thèse** : [1 phrase affirmative 60-180 chars].[espace insécable] [1 nuance dialectique 20-120 chars commençant par "Cependant", "Néanmoins", "Toutefois"].

## Faits clés

- **F-001** : [énoncé ≤25 mots, VERBATIM depuis l'enquête §10]
- **F-002** : [énoncé ≤25 mots, VERBATIM depuis l'enquête §10]
- **F-003** : [énoncé ≤25 mots, VERBATIM depuis l'enquête §10]
- **F-004** : [énoncé ≤25 mots, VERBATIM depuis l'enquête §10]
- **F-005** : [énoncé ≤25 mots, VERBATIM depuis l'enquête §10]

## Chiffres clés

- [chiffre] [unité] : [contexte 1 phrase, source depuis §5 ou §11 de l'enquête]
- [chiffre] [unité] : [contexte 1 phrase]
- [chiffre] [unité] : [contexte 1 phrase]

## Acteurs majeurs

- [Acteur] : [position 1 phrase verbatim depuis §3 ou §9 de l'enquête]
- [Acteur] : [position 1 phrase]
- [Acteur optionnel] : [position 1 phrase]

## Transversalité locale

[1 phrase : ce que cette enquête révèle isolément, extraite de §11 PELOTE ou §7 dialectique de l'enquête]

[--- ANNEXE CONDITIONNELLE INJECTÉE SELON FORMAT DÉTECTÉ (sauf ANALYTIQUE) ---]

## Annexe [Type selon format]

[≤200 mots de listes opérationnelles préservées verbatim ou quasi-verbatim]
```

### 4.2 Contraintes strictes (validées par validateur Python §6)

| Contrainte | Valeur | Source |
|------------|--------|--------|
| Format détecté | ∈ {PROCÉDURE, MÉTA, JURIDIQUE, COMPARAISON, HISTORIQUE, TECHNIQUE, SONDAGES, SOCIOLOGIE, MÉDIATIQUE, ANALYTIQUE} | regex `^\\*\\*Format détecté\\*\\*` (auto-audit sub-agent) |
| Volume total compress.md + Annexe | ≤320 mots (cible 300, tolérance +10%) | comptage mots (auto-audit) |
| Volume Synthèse standard seul | 80 ≤ mots ≤ 120 (cible 100, tolérance ±20%) | comptage mots (auto-audit) |
| Annexe mots minimum (si format ≠ ANALYTIQUE) | ≥30 mots (preuve d'opérationnalisation) | comptage mots (auto-audit) |
| Annexe mots maximum | ≤200 mots (cible), 220 max (tolérance +10%) | comptage mots (auto-audit) |
| Faits clés | 5 ≤ N ≤ 7 | regex `\\*\\*F-[A-Z0-9\\-]+\\*\\*` (auto-audit) |
| Chiffres clés | 3 ≤ N ≤ 5 | regex `^\\s*-\\s*\\d` (auto-audit) |
| Acteurs majeurs | 2 ≤ N ≤ 3 | regex `^\\s*-\\s*` section Acteurs |
| VERBATIM F-### | chaque F-### existe dans l'enquête source | `re.search` strict (auto-audit) |
| Verbatim chiffre | chaque chiffre (extrait via `digits()`) existe dans l'enquête source | `re.search` strict (auto-audit) |
| Pas de tirets cadratins | aucun U+2014 | `re.search` (auto-audit) |
| Pas d'invention | section Acteurs reprend noms depuis §3, positions depuis §9 | `re.search` (auto-audit) |
| Transversalité non-vide | ≥1 phrase | `count_words` ≥5 |

---

## §5. Sub-agent unique : `compress_summary_extractor.md` (v37 v2)

### 5.1 Prompt complet v37 v2 format-aware (prêt à copier-coller)

```markdown
# Sublimator v37 v2 : Agent Compress Summary Format-Aware (Phase 1)

## Contrat d'usage

Tu es l'extracteur unique de la Phase 1 du Sublimator. Tu reçois une enquête journalistique longue (5 000-15 000 mots) en entrée. Tu produis **un seul fichier Markdown strict** : `compress_summary` ≤320 mots (cible 300) avec Annexe conditionnelle ≤200 mots selon le format détecté.

## Règles métal

1. **Zéro invention.** Chaque F-### cité, chaque chiffre, chaque acteur, chaque position doivent exister textuellement dans l'enquête source.
2. **VERBATIM obligatoire.** Tes énoncés F-### doivent être des COPIES LITTÉRALES des F-### trouvés dans §10 §FACT_REGISTRY ou équivalent de l'enquête. Tu peux raccourcir un énoncé long à 25 mots max, mais tu ne peux pas le réécrire sémantiquement.
3. **Zéro format JSON.** Réponse en pur Markdown sans accolades, sans array, sans guillemets structurels.
4. **Pas de phrases de politesse**. Pas d'introduction ("Voici la quintessence..."), pas de conclusion ("En résumé..."). Tu commences directement par `# Quintessence : <id>`.
5. **Pas de tirets cadratins U+2014.** Utilise "-" ou ":" ou parenthèses.
6. **Français soutenu** sans anglicisme non justifié.
7. **Espace insécable U+00A0 avant chaque ":"** (convention typographique française).
8. **Pas de Mnemolite**, pas de RAG, pas de cardex local : Phase 1 est purement extractive, sans appel externe.

## Format de sortie obligatoire (compress.md)

```markdown
# Quintessence : [enquete_id]

**Format détecté** : [PROCÉDURE | MÉTA | JURIDIQUE | COMPARAISON | HISTORIQUE | TECHNIQUE | SONDAGES | SOCIOLOGIE | MÉDIATIQUE | ANALYTIQUE]

**Thèse** : [1 phrase affirmative 60-180 chars]. [1 nuance dialectique 20-120 chars].

## Faits clés

- **F-001** : [énoncé ≤25 mots verbatim]
- **F-002** : [énoncé ≤25 mots verbatim]
- **F-003** : [énoncé ≤25 mots verbatim]
- **F-004** : [énoncé ≤25 mots verbatim]
- **F-005** : [énoncé ≤25 mots verbatim]

## Chiffres clés

- [chiffre] [unité] : [contexte 1 phrase]
- [chiffre] [unité] : [contexte 1 phrase]
- [chiffre] [unité] : [contexte 1 phrase]

## Acteurs majeurs

- [Acteur] : [position 1 phrase]
- [Acteur] : [position 1 phrase]

## Transversalité locale

[1 phrase depuis §11 PELOTE ou §7 dialectique]

[--- ANNEXE CONDITIONNELLE (Uniquement si format ≠ ANALYTIQUE) ---]

## Annexe [Spécifique au format]

[≤200 mots de listes opérationnelles préservées : jalons/contacts/articles/pays/chronologie/stack/panel/cartographie]
```

## Etape 1 : Synthèse standard (≤120 mots)

Fais comme en v37 v1. Thèse (2 phrases), Faits clés (5-7 max), Chiffres (3-5), Acteurs (2-3), Transversalité (1 phrase).

## Etape 2 : Détection du format

Examine le nom du fichier ET le contenu de l'enquête (présence de sections marqueurs). Détermine le format principal parmi les 10 suivants :

| Format | Marqueurs de détection | Annexe requise |
|--------|------------------------|----------------|
| PROCÉDURE | mots `Jalon T+`, `Pack Données`, préfixe `protocole_`, `pnred_`, `strategie_` | OUI : jalons + architecture chiffrée + loups |
| MÉTA | mots `experts nominatifs`, `failles`, préfixe `external_legal_audit`, `verification_independante` | OUI : 30-50 questions + failles + contacts |
| JURIDIQUE | refs `Code pénal`, `Article`, `Conseil Constitutionnel`, `CEDH` | OUI : articles verbatim + précédents |
| COMPARAISON | mots `Italie`, `Bavière`, `Verfassung`, `DAO`, `Decidim`, `M5S` | OUI : pays + critères + leçons |
| HISTORIQUE | mots `1789`, `1946`, `1958`, `République`, `CNR` | OUI : chronologie datée acteurs |
| TECHNIQUE | mots `ANSSI`, `SecNumCloud`, `X-Road`, `Cloud Act`, `civictech_` | OUI : stack chiffrée + coûts M€ + risques |
| SONDAGES | mots `IFOP`, `IPSOS`, `panel`, `méthodologie` | OUI : panel CSP + résultats + limites |
| SOCIOLOGIE | mots `profil`, `CSP`, `électorat`, `indifférence` | OUI : leviers comportementaux + cibles |
| MÉDIATIQUE | mots `média`, `Bolloré`, `Vivendi`, `LVMH`, `Dassault` | OUI : cartographie propriétaires |
| ANALYTIQUE | aucun des précédents (RIC-pur) | NON |

## Etape 3 : Annexe conditionnelle (si format ≠ ANALYTIQUE)

**Génère `## Annexe [Type]` avec ≤200 mots selon le format détecté** :

- **PROCÉDURE** : liste les jalons chronologiques (T0, T+6, T+12, T+18, T+36) avec composants courts ; architecture technique chiffrée (3 couches : SecNumCloud + X-Road + Papier-First) ; noms d'au moins 5 loups opérationnels.
- **MÉTA/AUDIT** : liste les 5-10 questions sectorielles les plus importantes ; identifie les 3-5 failles majeures (CRIT) ; nomme les 3-5 experts contactables.
- **JURIDIQUE** : liste les articles juridiques stricts (Code pénal art. X-Y, Loi organ. n° X-Y, CC décision X-Y DC) ; précédents CC/CEDH cités verbatim.
- **COMPARAISON** : liste les pays comparés (max 4) ; critères de comparaison (3-5) ; leçons pour France.
- **HISTORIQUE** : donne la chronologie datée (5 dates + acteur + événement) ; évolution doctrinale (3 jalons).
- **TECHNIQUE** : liste les composants de la stack (3-5) avec coûts en M€ ; risques techniques structurants (2-3).
- **SONDAGES** : précise le panel (CSP, âge, région, N) ; résultats chiffrés comparables ; limites ou biais identifiés.
- **SOCIOLOGIE** : cite les leviers comportementaux (3-5) ; profil CSP cible ; barrières à la participation.
- **MÉDIATIQUE** : liste les 5-9 propriétaires majeurs identifiés ; stratégie de mur médiatique (1 phrase) ; alternatives (Substack/Telegram/Mastodon/LBRY).

L'Annexe doit ABSOLUMENT préserver les listes opérationnelles intactes (Pas de paraphrase, pas d'inversion, pas de coupure de listes structurées).

## Cas limites à gérer

- Enquête <2000 mots : si trop courte pour 5 F-###, prendre 3-4 F-### + mention "enquête courte" dans le compress.
- Enquête sans 10 §FACT_REGISTRY explicite : prendre les "constats principaux" et les numéroter F-001, F-002 toi-même. MARQUE cette renumérotation.
- Plusieurs formats détectés (ex : PROCÉDURE + JURIDIQUE) : choisir le format qui apparaît en premier dans la table de détection, mais conserver les marqueurs du second format dans l'Annexe.
- Enquête hors corpus RIC : appliquer le même algorithme, classifier selon les marqueurs du domaine (DOMAINE = extension possible future).
- Enquête vide ou corrompue : produire un compress placeholder `[ENQUÊTE VIDE OU CORROMPUE : <id>]` et passer exit 1.

## Auto-vérification AVANT émission

1. As-tu bien détecté le format via marqueurs ? Mentionne-le dans `**Format détecté**`.
2. Si format ≠ ANALYTIQUE : as-tu produit l'Annexe ? Sinon : REVIENS et complète.
3. Pour chaque F-### : as-tu pris l'énoncé tel quel dans l'enquête ? Si paraphrase : REVIENS au verbatim.
4. LENGTH CHECK : ton output total fait-il ≤320 mots (cible 300) ? Si >320 : REVIENS et condense.
5. Si Annexe absente et format détecté ≠ ANALYTIQUE : ERREUR. Refais.
```

### 5.2 Métadonnées du prompt v37 v2

| Champ | Valeur |
|-------|--------|
| Nom fichier | `tools/engines/sublimator/prompts/compress_summary_extractor.md` |
| Lignes cibles | ~210 (vs 270 pour quintessence_extractor.md actuel) |
| Sub-agents éliminés | quintessence_reader.md (237), quintessence_extractor.md (352), quintessence_critic.md (134), quintessence_orchestrator.md (163) |
| Économie | ~886 lignes de prompts supprimées |
| Innovation v37 v2 | branche conditionnelle de détection format + 9 Annexes typées conditionnelles |

---

## §6. Auto-Audit Sub-Agent CRITIQUE (sans dépendance algorithmique)

> **Note 2026-07-06 22 h** : la validation algorithmique Python (`compress_validate.py`) a été retirée du Sublimator (cf. `prompt-v35.md` Note d'architecture). La conformité des compress.md est désormais vérifiée par le **sub-agent LLM CRITIQUE** ou par **checklist manuelle du pilote** aux checkpoints CP1/CP2.

### 6.1 Contrat du sub-agent CRITIQUE Format-Aware

Invoquer CRITIQUE (cf. `prompts/quintessence_critic.md`) avec `filePaths = [<compress>.md, <enquete>.md]` après chaque production de compress.md.

Le sub-agent CRITIQUE vérifie les 8 critères suivants :

1. **M0** Format détecté ∈ {PROCÉDURE, MÉTA, JURIDIQUE, COMPARAISON, HISTORIQUE, TECHNIQUE, SONDAGES, SOCIOLOGIE, MÉDIATIQUE, ANALYTIQUE}
2. **M1** Volume total ≤320 mots (synthese 80-120 + Annexe ≤200 si ≠ ANALYTIQUE)
3. **M2** Présence F-### (5-7)
4. **M3** VERBATIM strict (chaque F-### existe dans l'enquête source)
5. **M4** Chiffres (3-5)
6. **M5** Acteurs (2-3)
7. **M6** Pas de tirets cadratins U+2014
8. **M7** Annexe ≥30 mots si format ≠ ANALYTIQUE

### 6.2 Métadonnées du sub-agent CRITIQUE (vs validateur Python précédent)

| Champ | Valeur |
|-------|--------|
| Nom fichier | `tools/engines/sublimator/prompts/quintessence_critic.md` |
| Lignes cibles | ~134 (vs 145 lignes validateur Python retiré) |
| Réduction | -8 % lignes |
| Métriques | 8 (M0-M7) |
| Coût | tokens LLM (vs $0 validateur Python) |
| 0 dépendance externe | conforme à la philosophie Sublimator sans validation algorithmique |
| Format-awareness | 10 formats reconnus (cf. §3bis.1) |


## §7. Modifications de l'orchestrateur `sublimator_pilot.py` (v37 v2)

### 7.1 Changements structurels

**AVANT (v36) :**

```
sublimator_pilot.py phase1_reader() → charge reader.md (intermédiaire 3500 mots)
                   phase1_quintessence() → charge quintessence.json (intermédiaire 6000 mots)
                   phase1_5_compress() → lit compress_summary (champ dans JSON)
                   phase2_synthese() → MOCK synthese
                   phase_validation() → appel sublimator_validate.py (623 lignes)
```

**APRÈS (v37 v2) :**

```
sublimator_pilot.py phase1_compress_v37v2() → invoque sub-agent Compress Summary Format-Aware
                   ├─ Etape 1 : synthese standard (≤120 mots)
                   ├─ Etape 2 : détection format (10 formats)
                   ├─ Etape 3 : Annexe conditionnelle si ≠ ANALYTIQUE (≤200 mots)
                   ├─ Output : investigations/<sujet>/_quintessence/<prefix>_compress.md
                   ├─ Validation : appel compress_validate.py (M0-M7)
                   └─ Retry si NO-GO (1 fois, max)
                   phase2_synthese() → MODIFIÉ : consomme N fichiers compress.md (avec Annexe préservée)
                   (suppression phase_validation() vers sublimator_validate.py)
```

### 7.2 Modifications du pilote (sans dépendance algorithmique)

> Tout le pilotage est effectué par le sub-agent LLM CRITIQUE + le pilote LLM Sublimator. Aucun script orchestrateur Python.

**Changements vs v36** :
- Suppression de l'orchestrateur Python `sublimator_pilot.py` (cf. Note d'architecture prompt-v35.md 2026-07-06).
- Invoque directement le sub-agent EXTRACTEUR v2 via `filePaths` avec en sortie compress.md.
- Post-validation : appel sub-agent CRITIQUE sur le compress.md (avec sa source).
- Retry (max 1) géré par le pilote LLM, pas par un script.


### 7.3 Compatibilité ascendante

**Aucun backward compatibility visé.** v37 v2 est un breaking change assumé. Les utilisateurs doivent régénérer les `_quintessence/` via le nouveau sub-agent.

---

## §8. Suppressions de fichiers (Phase D)

| Fichier | Lignes actuelles | Verdict |
|---------|------------------|---------|
| `tools/engines/sublimator/extractors/cartographie.py` | déjà supprimé | déjà fait 2026-07-05 |
| `tools/engines/sublimator/prompts/quintessence_reader.md` | 237 | KILL |
| `tools/engines/sublimator/prompts/quintessence_extractor.md` | 352 | KILL |
| `tools/engines/sublimator/prompts/quintessence_critic.md` | 134 | KILL |
| `tools/engines/sublimator/prompts/quintessence_orchestrator.md` | 163 | KILL |
| `sublimator_validate.py` (total) | 623 | KILL (remplacé par compress_validate.py ~150 lignes) |
| `sublimator_pilot.py` | 290 | MODIFY (réécriture partielle) |

**Total lignes supprimées : 1509 lignes**
**Total lignes créées : ~360 lignes (1 prompt ~210 + 1 validateur ~150 + modifications pilot)**
**Économie nette : -1149 lignes** (significative mais avec préservation opérationnelle par format).

---

## §9. Métriques de succès chiffrées (v37 v2)

### 9.1 Métriques de production par enquête

| Métrique | Cible v37 v2 | Baseline v36 | v37 v1 (limite stricte) | Verdict succès |
|----------|--------------|--------------|-------------------------|----------------|
| Volume produit par enquête (synthese + annexe) | 300 mots (cible), 320 max | 9500 mots | 100 mots (destructeur) | <3.5% du volume v36 |
| Compression ratio vs brut | ≥31× (cible) | 1.13× (anti-denoising) | ≥83× (mais perte opérationnelle) | préservation opérationnelle + denoising fort |
| F-### extraits par enquête | 5-7 | 24 | 5-7 | sélectivité accrue |
| Chiffres extraits par enquête | 3-5 | 5 | 3-5 | comparable |
| Acteurs majeurs extraits par enquête | 2-3 | 7 | 2-3 | sélectivité accrue |
| Listes opérationnelles préservées | OUI (Annexe 200m, 9 formats) | OUI (enterrées dans JSON 24-champs) | NON (détruites) | opérationnel ACTIONNABLE |
| 10 formats détectés | OUI | NON | NON | format-aware |
| Temps production LLM | ≤7 sec | 30+ sec | ≤5 sec | ÷4 minimum |
| Hallucinations imposées par schéma | 0 (validateur strict) | 7 champs | 0 (validateur strict) | ÷infinity |

### 9.2 Métriques de qualité du signal pour Phase 2

| Métrique | Cible v37 v2 | Baseline v36 |
|----------|--------------|--------------|
| Volume total à ingérer Phase 2 (42 enquêtes) | ≤13 440 mots | ~350 000 mots |
| Tokens Phase 2 input | ≤18 000 tokens (320 mots × 42) | ~500 000 tokens |
| Transversalités détectables manuellement (lecture humaine 5 min) | ≥15 | ≤3 |
| Faux transversalités dues au bruit du schéma | 0% (champs inventions éliminés) | 30% |
| Détails opérationnels préservés (Plan T+, contacts experts, articles juridiques, pays comparés) | ≥80% des listes préservées | 0% (inaccessibles au LLM Phase 2) |

### 9.3 Métriques de conformité projet

| Métrique | Cible |
|----------|-------|
| Pas de tirets cadratins U+2014 dans les outputs | 100% |
| Pas d'anglicisme non justifié | 100% |
| Espaces insécables U+00A0 avant ":" | ≥95% |
| Sources URL_HEAD_200_OK pour faits tier 1 | ≥80% |
| Pas de fabrication (validateur VERBATIM) | 100% |
| Format détecté présent dans chaque compress.md | 100% |

---

## §10. Critères d'acceptation (binaire PASS/FAIL) v37 v2

### 10.1 Pour chaque enquête individuellement

Un `compress.md` est **VALIDE** si TOUS les critères suivants sont OK :

| Critère | Valeur attendue | Source |
|---------|-----------------|--------|
| **Format détecté** | ∈ {10 formats} | regex `^\\*\\*Format détecté\\*\\*` (auto-audit sub-agent) |
| **Volume synthese** | 80 ≤ mots ≤ 120 | comptage mots (auto-audit) |
| **Volume total** | ≤320 mots | synthese + annexe |
| **Annexe si ≠ ANALYTIQUE** | ≥30 mots ≤200 mots | `count_words` |
| **F-### count** | 5 ≤ N ≤ 7 | regex `\\*\\*F-...\\*\\*` |
| **VERBATIM** | chaque F-### existe dans l'enquête source | `f.strip("*") in source_text` (auto-audit) |
| **Chiffres count** | 3 ≤ N ≤ 5 | section `## Chiffres` regex |
| **Acteurs count** | 2 ≤ N ≤ 3 | section `## Acteurs` regex |
| **Pas de tirets cadratins** | aucun U+2014 | `em_dash not in compress_text` |
| **Thèse centrale** | 1 phrase avec nuance dialectique | regex section `**Thèse**` |
| **Transversalité locale** | 1 phrase ≥5 mots | regex section `## Transversalité` |
| **Annexe format-spécifique** | présente si ≠ ANALYTIQUE, titre `## Annexe [Type]` | regex section `## Annexe` |

**Exit code :** 0 (PASS), 1 (NO-GO violation VERBATIM), 2 (HARD_FAIL volume ou format non reconnu)

### 10.2 Pour l'ensemble du corpus (42 enquêtes)

Un corpus de N enquêtes est **VALIDE** si :

| Critère | Valeur |
|---------|--------|
| 100% des `compress.md` sont PASS | 42/42 |
| Compression totale ≥31× vs brut | 13 440 mots / 420 000 mots ≈ 3.2% |
| Couverture des 10 formats détectés parmi les 42 enquêtes | ≥8 formats détectés dans le corpus |
| Pas de doublons F-### inter-enquêtes | autorisé (chaque enquête a sa nomenclature) |
| Phase 2 peut ingérer tous les `compress.md` | 13 440 mots ≤ 100 000 tokens (LLM standard) |

**Exit code corpus :** 0 si 100% PASS, 1 si ≥1 NO-GO, 2 si ≥1 HARD_FAIL.

---

## §11. Interface avec les Phases 2 / 2.5 / 2.6 / 3

### 11.1 Phase 2 : clustering et transversalités

**Input Phase 2 v37 v2 :**

```
investigations/<sujet>/_quintessence/
  <prefix_1>_compress.md
  <prefix_2>_compress.md
  ...
  <prefix_N>_compress.md
```

Chaque fichier a une ligne `**Format détecté** : <X>` qui permet à Phase 2 de **pondérer** le signal différemment selon le type :
- ANALYTIQUE : contribution transversale standard.
- PROCÉDURE : contribution transversale + recherche de jalons comparables entre enquêtes (Plan 18 mois vs Plan X).
- MÉTA : contribution transversale + alerte sur failles méthodologiques inter-enquêtes.
- JURIDIQUE : contribution transversale + recoupement d'articles juridiques cités dans plusieurs enquêtes.
- COMPARAISON : contribution transversale + extraction systématique des pays comparés.
- HISTORIQUE : contribution transversale + datation fine des événements.

Total : N fichiers de 300 mots ≈ N × 300 mots.

**Comportement Phase 2 (LLM hôte) :**

1. Ingère les N fichiers en un seul bloc (volume ≤13 440 mots pour 42 enquêtes).
2. Identifie les transversalités inter-enquêtes : un F-### ou chiffre comparé entre ≥2 enquêtes.
3. Produit `synthese_clusters.json` listant les transversalités avec matchs F-### ↔ F-### entre enquêtes, format par format.
4. Produit `synthese.json` avec la thèse fil rouge + thèses hiérarchisées (c.f. L2 du §Phase 3 actuel).

**Prompt Phase 2 v37 v2 (esquisse) :**

```markdown
# Phase 2 Sublimator v37 v2 : Clustering de N compress_summary

Tu reçois N fichiers compress_summary (≤300 mots chacun) issus de N enquêtes.
N est typiquement 30-50. Chaque fichier inclut une ligne `**Format détecté** : <X>`.

## Ta mission
1. Lis tous les compress_summary en un bloc.
2. Pour chaque transversalité détectée, MENTIONNE le format des enquêtes concernées
   (ex : "transversalité X : présente dans 3 ANALYTIQUE + 1 JURIDIQUE").
3. Identifie ≥8 transversalités inter-enquêtes :
   - Un chiffre commun (ex : "30% confiance institutionnelle" présent dans 5 ANALYTIQUE)
   - Un F-### cité dans ≥2 enquêtes sous des angles différents
   - Un acteur comparé dans plusieurs enquêtes avec des positions différentes
   - Un jalon T+ ou contact expert partagé entre 2+ PROCÉDURE/MÉTA
4. Produis synthese_clusters.json avec :
   chaque transversalité :
   - label : [nom de la transversalité]
   - enquetes_concernees : [liste <prefix> + leur format]
   - f_partages : [F-### cités]
   - transversalite_intra : [1 phrase décrivant le lien]
5. Produis synthese.json avec :
   - these_fil_rouge : [1 phrase affirmative 60-180 chars]
   - theses_hierarchisees : [3-5 thèses avec ordre]
```

### 11.2 Phase 2.5 : rapport de synthèse (humain)

**Input :** synthese.json + synthese_clusters.json.
**Output :** `_synthese/rapport_synthese.md` (5 sections : vue d'ensemble, thèse fil rouge, transversalités, surprises/angles morts, recommandation article).
**Volume dépend du nombre d'enquêtes mais ne dépend plus des quintessences JSON intermédiaires.**

### 11.3 Phase 2.6 : plan d'article

**Input :** rapport_synthese.md + accès aux enquêtes sources (référencées depuis les F-### des compress.md).
**Output :** `_synthese/plan_article.md` (3-5 sections d'article avec thèse centrale + angle/ton + public + vérifications + sources groupées par §).
**Adaptation v37 v2** : le plan_article peut référencer des **listes opérationnelles** (Plan T+, contacts experts, articles juridiques) en s'appuyant sur les Annexes des compress.md des formats correspondants.

### 11.4 Phase 3 : article

**Input :** plan_article.md + enquêtes sources (pour VERBATIM des citations).
**Output :** `articles/<date>_<sujet>_ARTICLE.md` (3000-5000 mots). L2 Thèse unique + L3 Sources fin + L4 Ton clinique + L8 Auto-audit antagoniste (cf. prompt-v35.md §Phase 3 actuel, conservé tel quel).

**Adaptation L3 v37 v2** : les sources fin d'article incluent maintenant :
- URLs tier 1 des F-### référencés (cf. §4.2 VERBATIM).
- **Si Annexes PROCÉDURE/MÉTA/JURIDIQUE/etc.** : listes opérationnelles préservées qui fournissent le détail actionnable de l'article.

**Note importante :** cette SPECS Phase 1 v37 v2 NE MODIFIE PAS Phase 3. La qualité des compress.md (avec Annexes) remonte automatiquement par capillarité vers Phase 3.

---

## §12. Tests A/B juge de paix v37 v2

### 12.1 Protocole (à exécuter avant validation v37 v2)

**Sélection enquête :** 5 enquêtes RIC couvrant 5 formats distincts :

| # | Enquête | Format | Spécificité |
|---|---------|--------|-------------|
| 1 | `2026-07-04_18-00_referendum_initiative_citoyenne` | **ANALYTIQUE** | RIC canonique (verrou Constitution 1958) |
| 2 | `2026-07-05_11-00_protocole_pnred_ric_001_PROTOCOLE-PNRED-RIC-001` | **PROCÉDURE** | Plan 18 mois + Pack Données + 20 loups |
| 3 | `2026-07-05_14-00_external_legal_audit_p3_16_p3_18_EXTERNAL-LEGAL-AUDIT-2026-07` | **MÉTA** | 37 questions + 12 failles + 5 experts |
| 4 | `2026-07-05_01-00_levier_cedh_article_3_p1_CEDH-RIC-001` | **JURIDIQUE** | Code pénal + CEDH + précédents CC |
| 5 | `2026-07-05_17-00_bavierr_art_71_75_verfassung_1946_volksentscheide` | **COMPARAISON** | Bavière Verfassung 1946 + leçons France |

### 12.2 Branches du test

**Branche A (v37 v2) :** produire 5 compress.md (cible 300 mots/enquête, 4 avec Annexe + 1 sans) → appeler Phase 2 (LLM hôte).

**Branche B (v36) :** réutiliser les 5 quintessences-v2.json existantes (si générées manuellement pour RIC 18:00) ou les regénérer pour les 4 autres → appeler Phase 2 (LLM hôte).

### 12.3 Critères de jugement (objectifs)

Phase 2 (LLM hôte) reçoit en input alternativement Branche A et Branche B. Le LLM produit un plan_article.md dans les deux cas. Juger :

| Critère | Mesure | Cible |
|---------|--------|-------|
| Transversalités inter-enquêtes détectées par Phase 2 | compte manuel | Branche A ≥ Branche B + 3 |
| Plans T+ mentionnés dans plan_article (PROCÉDURE) | compte manuel | Branche A : 5/5 ; Branche B : 0/5 |
| Contacts experts (MÉTA) cités dans plan_article | compte manuel | Branche A : ≥3 ; Branche B : 0 |
| Articles juridiques verbatim (JURIDIQUE) cités dans plan_article | compte manuel | Branche A : ≥5 ; Branche B : 0 |
| Pays comparés (COMPARAISON) mentionnés | compte manuel | Branche A : 4/4 ; Branche B : 0 |
| Faux transversalités (liens artificiels créés par bruit de schéma) | compte manuel | Branche A : 0 ; Branche B : ≥2 |
| Temps de production Phase 2 | secondes | Branche A ≤ Branche B / 5 |
| Tokens input Phase 2 | tokens (mesure API) | Branche A ≤ Branche B / 25 |
| Qualité du fil narratif final | éditorial humain 1-5 | Branche A ≥ 4, Branche B ≤ 3 |

### 12.4 Verdict attendu

**Hypothèse Prouvée si :**

- Branche A produit ≥5 transversalités inter-enquêtes que Branche B ne détecte pas (preuve que le signal compress_summary est plus riche que le bruit quintessence v36).
- Branche A préserve les listes opérationnelles (Plan T+, experts, articles de loi, pays comparés) que Branche B ENTERRE dans le JSON.
- Branche A produit 0 fausse transversalité alors que Branche B en produit ≥2.

**Hypothèse Réfutée si :**

- Branche A perd des F-### clés que Branche B conservait : augmenter MIN_FACTS à 7-10.
- Annexe absente pour formats détectés ≠ ANALYTIQUE : problème de détection format, ajuster les regex §3bis.3.
- Volume total dépasse 320 mots systématiquement : réviser la consigne de condensation.

---

## §13. Risques résiduels & fallbacks

### 13.1 Risque R1 : LLM n'arrive pas à condenser sous 120 mots la synthèse standard

**Symptôme :** compress_summary_part (sans Annexe) >120 mots systématiquement.

**Mitigation :**
- Renforcer la consigne du prompt : "Si >120 mots, RETRAVAILLE ton output pour condenser".
- En dernier recours : maintenir synthese ≤150 mots si Annexe ≤170 mots (total constant 320).

### 13.2 Risque R2 : LLM paraphrase au lieu de citer textuellement

**Symptôme :** validateur NO-GO sur m3_violations (F-### cités non trouvés dans l'enquête source).

**Mitigation :**
- Renforcer la consigne du prompt section "Algorithme de sélection" : "Tu COPY-COLLES le texte du §10 §FACT_REGISTRY sans réécriture".
- Donner un exemple VERBATIM dans le prompt.
- Retry automatique si NO-GO avec consigne "Cite l'énoncé EXACT depuis §10, pas une reformulation".

### 13.3 Risque R3 : Mauvaise détection du format (mauvais type d'Annexe)

**Symptôme :** enquête `protocole_pnred_` classée à tort comme MÉTA → Annexe failles au lieu d'Annexe opérationnelle.

**Mitigation :**
- Heuristique en cascade : mots-clés prioritaires (PROCÉDURE > tout) > sections présentes > nom de fichier.
- Si doute entre 2 formats : choisir le plus spécifique (celui avec marqueur unique comme 'Jalon T+' pour PROCÉDURE).
- Logger la confiance de détection dans le rapport Phase 1 pour traçabilité.

### 13.4 Risque R4 : L'Annexe dépasse 200 mots (bavard)

**Symptôme :** Annexe compressée sur 250+ mots pour les PROCÉDURE ou MÉTA volumineux.

**Mitigation :**
- Le validateur HARD_FAIL si >220 mots. Le sub-agent retry avec consigne "CONDENSE l'Annexe, garde uniquement les 5-10 listes les plus importantes".
- Stratégie : couper les détails secondaires (déjà couverts dans la synthese), garder les listes opérationnelles verbatim.

### 13.5 Risque R5 : Transversalités détectées par Phase 2 sont peu nombreuses

**Symptôme :** Branche A produit <5 transversalités inter-enquêtes vs >10 attendues.

**Mitigation :**
- Enrichir le prompt Phase 2 v37 v2 : "Cherche des transversalités MÊME entre formats différents (ex : un Plan T+ d'une PROCÉDURE peut être comparable à une chronologie d'une HISTORIQUE)".
- Cross-référencer avec les Annexes préservées.
- Si <3 transversalités détectées : la qualité des enquêtes sources est insuffisante, ce n'est pas un problème Phase 1.

### 13.6 Risque R6 : Rollback complet nécessaire

**Si le Test A/B §12 échoue dramatiquement** : procédure de rollback.

| Étape | Commande |
|-------|----------|
| 1. Restaurer les fichiers supprimés | `git revert HEAD` (si commit) |
| 2. Régénérer les quintessences v36 | pour chaque enquête : produire reader.md + quintessence-v2.json |
| 3. Re-brancher Phase 2 sur les quintessences | modifier prompt Phase 2 |
| 4. Documenter l'échec dans une SPECS de rollback | `tools/engines/sublimator/<date>_rollback_phase1_v37v2.md` |

**Délai maximal de décision :** 2 jours ouvrés après test A/B. Au-delà, maintenir v37 v2 pour itérer.

---

## §14. Plan d'implémentation en 6 phases

### 14.1 Phase A : Création du sub-agent (3h)

| Étape | Commande / Action | Livrable |
|-------|--------------------|----------|
| A1 | Créer le fichier `tools/engines/sublimator/prompts/compress_summary_extractor.md` (§5.1 v37 v2 copié) | 1 fichier, ~210 lignes |
| A2 | Vérifier le prompt avec un mock test sur 1 ANALYTIQUE + 1 PROCÉDURE + 1 MÉTA | Log de production |

### 14.2 Phase B : Configuration sub-agent CRITIQUE (auto-audit, 0 dépendance algorithmique)

| Étape | Action | Livrable |
|-------|--------|----------|
| B1 | Vérifier `tools/engines/sublimator/prompts/quintessence_critic.md` charge correctement via `filePaths` | Sub-agent LLM opérationnel |
| B2 | Tester production de 5 compress.md placeholder contre 5 enquêtes réelles couvrant 5 formats | Tous doivent retourner GO ou NO-GO selon le placeholder |

> **Note 2026-07-06** : la création du validateur Python `compress_validate.py` est remplacée par un appel sub-agent CRITIQUE LLM. Pas de coût algorithmique nul, mais expertise LLM supérieure pour les cas ambigus.


### 14.3 Phase C : Modification de l'orchestrateur (3h)

| Étape | Commande / Action | Livrable |
|-------|--------------------|----------|
| C1 | Réécrire `sublimator_pilot.py` selon §7.1 et §7.2 (intégration `phase1_compress_v37v2`) | 1 fichier modifié |
| C2 | Tester le pilot sur les 5 enquêtes RIC sélectionnées §12.1 | Sortie JSON trace étape-par-étape |

### 14.4 Phase D : Suppressions effectives (30 min)

| Étape | Commande / Action | Livrable |
|-------|--------------------|----------|
| D1 | Supprimer `tools/engines/sublimator/prompts/quintessence_reader.md` | `git rm` |
| D2 | Supprimer `tools/engines/sublimator/prompts/quintessence_extractor.md` | `git rm` |
| D3 | Supprimer `tools/engines/sublimator/prompts/quintessence_critic.md` | `git rm` |
| D4 | Supprimer `tools/engines/sublimator/prompts/quintessence_orchestrator.md` | `git rm` |
| D5 | Supprimer `tools/engines/sublimator/sublimator_validate.py` | `git rm` |
| D6 | Mettre à jour `tools/engines/sublimator/README.md` pour refléter v37 v2 | 1 fichier modifié |

### 14.5 Phase E : Test A/B v37 v2 (§12) - le juge de paix (5h)

| Étape | Action |
|-------|--------|
| E1 | Générer Branche A : 5 compress.md pour 5 enquêtes RIC couvrant 5 formats |
| E2 | Produire Branche B : 5 quintessences v36 pour les 5 mêmes enquêtes (option: réutiliser prod manuelle pour RIC 18:00, regénérer pour les 4 autres) |
| E3 | Phase 2 (LLM hôte) sur Branche A : capturer plan_article.md + transversalités détectées + listes opérationnelles préservées |
| E4 | Phase 2 (LLM hôte) sur Branche B : capturer plan_article.md + transversalités détectées + listes opérationnelles (devrait être 0) |
| E5 | Comparer selon critères §12.3 (notamment listes opérationnelles préservées) |
| E6 | Décision GO/NO-GO sur v37 v2 vs rollback §13.6 |

### 14.6 Phase F : Documentation finale (1h)

| Étape | Action |
|-------|--------|
| F1 | Mettre à jour `docs/VISION.md` si Sublimator référencé + indiquer v37 v2 |
| F2 | Ajouter une entrée dans `README.md` (sublimator) indiquant le passage v36 vers v37 v2 |
| F3 | Commit historique : "feat(sublimator): v37 v2 Phase 1 format-aware compress_summary (10 formats, 9 Annexes conditionnelles, 8 métriques M0-M7)" |

**Effort total : ~14h** sur 3-4 jours ouvrés, dont 5h sont consacrées au Test A/B juge de paix.

---

## §15. Critères de rollback

La SPECS v37 v2 sera considérée comme **manquée** (rollback vers v36) si :

| Critère | Seuil de rollback |
|---------|--------------------|
| Test A/B Phase 2 transversalités Branche A < 50% de Branche B | rollback |
| Test A/B listes opérationnelles préservées Branche A = 0 | rollback critique (l'annexe ne fonctionne pas) |
| Validateur compress_validate.py HARD_FAIL >30% des compress.md produits | rollback |
| Sous-agent unique produit synthese >150 mots malgré retry sur >50% des enquêtes | rollback |
| Mauvaise détection format sur >50% des enquêtes (toutes classées ANALYTIQUE par défaut) | rollback |
| Phase 2 LLM produit des transversalités qui s'avèrent être des FAUX LIENS évidents à la relecture humaine | rollback |

**Décision de rollback :** au plus tard 7 jours après commit initial. Au-delà, maintenir v37 v2 et itérer sur les prompts.

---

## §16. Annexes

### 16.1 Annexe A : 3 Examples de compress.md par format détecté

#### 16.1.1 Exemple ANALYTIQUE (RIC-pur, pas d'Annexe) : `2026-07-04_18-00_referendum_initiative_citoyenne`

```markdown
# Quintessence : 2026-07-04_18-00_referendum_initiative_citoyenne

**Format détecté** : ANALYTIQUE

**Thèse** : Le RIC n'a pas été refusé pour raisons techniques ou juridiques mais par un cartel transpartisan verrouillant 3 couches (Constitution 1958, capture oligarchique partis, primauté droit UE). Cependant, la fenêtre ouverte par les Gilets Jaunes 2018 démontre qu'une conjoncture critique existe.

## Faits clés

- **F-002** : La Constitution de 1958 ne prévoit aucun droit d'initiative populaire directe (ni législatif, ni constitutionnel).
- **F-003** : L'article 11 (référendum) est une prérogative exclusive du Président de la République.
- **F-008** : La Convention citoyenne pour le climat (2019-2020) a formulé 149 propositions dont le RIC climat, la majorité rejetée.
- **F-013** : Le consensus de rejet du RIC traverse LREM, LR, PS, EELV, PCF avec des nuances mais sans traduction législative.
- **F-016** : La confiance dans les institutions françaises est passée sous les 30% entre 2018 et 2024.

## Chiffres clés

- **149** : propositions Convention citoyenne climat (rejetées ou vidées en majorité).
- **300%** : hausse procédures 49.3 entre 2012 et 2023 (passage en force).
- **30%** : confiance institutionnelle française (seuil critique estimé à 15%).
- **185** : seuil parlementaire pour déclencher un RIP (infranchissable sans accord des partis).

## Acteurs majeurs

- Conseil constitutionnel : gardien de la Constitution de 1958, contrôle a priori sur tout référendum.
- Collectif Espoir RIC / Solution démocratique : transformation 2023, doctrine pro-RIC constitutionnel contrôlé.
- Union européenne : cadre non modifiable unilatéralement, contrainte via Pacte de stabilité et compétences exclusives.

## Transversalité locale

Mécanisme racine : architecture verrouillée de 1958 a institutionnalisé le monopole exécutif de l'initiative (articles 11 et 89 réservent l'initiative au Président et au Parlement), absorbant la souveraineté populaire dans une fiction représentative que le peuple n'a jamais consentie directement.
```

**Volume : 117 mots. Format ANALYTIQUE : pas d'Annexe requise. Valide en v37 v2.**

#### 16.1.2 Exemple PROCÉDURE (Annexe opérationnelle) : `2026-07-05_11-00_protocole_pnred_ric_001`

```markdown
# Quintessence : 2026-07-05_11-00_protocole_pnred_ric_001_PROTOCOLE-PNRED-RIC-001

**Format détecté** : PROCÉDURE

**Thèse** : Le protocole opérationnel PNRED (extrait des articles Substack L'adieu aux partis #83, Peuple souverain #20, Ré-enracinement #29, Éloge surface #30) rend le RIC français opérationnellement exécutable 2026-2030. Le risque résiduel principal est la capture M5S-like et l'invalidation Conseil Constitutionnel.

## Faits clés

- **F-PNR01** : Weil 1943 'suppression partis' : 3 critères (machine à passion + pression pensée + fin en soi).
- **F-PNR05** : Article 450-1 Code pénal : 10 ans d'emprisonnement pour groupement/entente préparatoire.
- **F-PNR13** : Bruegel 2024 (-10pts ICRG) : +106 pb spread = -2% PIB (levier financier État).
- **F-PNR32** : Pacte Souveraineté décliné officiel aucun signé 2025-2026 (à créer).
- **F-PNR24** : Cas Tarnac : collective surface Magasin Général survivant 2007-2026 (preuve de surface).

## Chiffres clés

- **5** : jalons Plan 18 mois PNRED (T0/T+6/T+12/T+18/T+36).
- **2-4** : M€/an coût Pack Données Souveraines (SecNumCloud + X-Road FR + Papier-First).
- **5-10** : % électorat discipline Pacte FRANCS ciblé sur seul critère RIC.
- **20** : loups nominatifs (architectes + chercheurs + constituante + opposants + politiques pro).

## Acteurs majeurs

- Substack Giak : architecte PP-RIC-PR-012-014-015 + 103 articles cumulés.
- Simone Weil : diagnostic fondationnel 1943 'suppression partis'.
- Bürgerrat Ostbelgien : modèle Conseil Citoyen 24 sortition, 78 000 hab.

## Transversalité locale

Cause racine : la mécanique d'enracinement humain est PRÉALABLE psy-organisationnel à toute action politique (psilocybine validé Johns Hopkins 2011 + Imperial College 2018).

## Annexe opérationnelle

- **T0 choc juridique-technique** : Loi Organique RIC (Lambda-8) + Pack Données SecNumCloud+X-Road+Papier-First.
- **T+6 apprentissage** : CS tripartite (30 sortition + 30 élus + 30 experts) installé opérationnel + ZGE dans 30-50 mairies.
- **T+12 arme** : RIC Abrogatoire activé nationalement ; nettoyage législatif sélectif (loi scélérates 2025-2026).
- **T+18 nouveau normal** : RIC Législatif pleinement actif + partis devenus Think tanks + transparence Pack.
- **T+36 fondation** : RIC Constituant activé ; réécriture article-par-article bottom-up.
- **Architecture Pack Données** : SecNumCloud ANSSI v3.2 (1.5M€/an, 7 hébergeurs certifiés Europe) + X-Road FR Estonia (0.5-2M€/an, décentralisé, pas Big Brother) + Papier-First + Hash sha-256.
- **5 leviers FRANCS transpartisans** : F(Frontières)/R(Rayonnement)/A(Autonomie)/N(Nation)/C(Citoyenneté)/S(Souveraineté).
- **Tactiques anti-répression** : Hierarchical decomposition (multi-associations 1901) + Banality Tactic Tarmac Magasin + Anti-DSA multi-plateformes + Cagnottes parallèles.
- **9 leviers économiques chiffrés** : boycott ciblé catégories fiscales (-1-5 Md€/an) + retrait coopératives + AMAP La Ruche + cash-out vendredi + Épargne or Pinatton.
- **Loups opérationnels** : Yves Sintomer (Univ Paris 8 sortition) ; Éric Piolle (EELV Grenoble RIL+CCP) ; Pierre Hurmic (Bordeaux RIL Régie eau 2024) ; François Ruffin (LFI Picardie) ; Mathilde Panot (LFI plateforme RIC open-source) ; Hadrien Clouet (LFI pro-RIC).
```

**Volume : synthesis + annexe = ~95 + ~190 = 285 mots. Valide en v37 v2 (cible ≤320).**

#### 16.1.3 Exemple MÉTA (Annexe failles & questions) : `2026-07-05_14-00_external_legal_audit`

```markdown
# Quintessence : 2026-07-05_14-00_external_legal_audit_p3_16_p3_18

**Format détecté** : MÉTA

**Thèse** : Le Pack Législatif CivicTech-FR 2027 (P3 #16/P3 #18) doit être validé par 5 experts juridiques humains réels (impossible LLM seul). 4 failles critique identifiées (CRIT-1 à CRIT-4) doivent être tranchées hors-LLM avant dépôt PPL.

## Faits clés

- **F-PNR72** : Constitution 1958 art. 89 al. 4 (intangibilité forme républicaine) : verrou structurellement CC.
- **F-PNR80** : CC 2019-1 RIP (rejet ADP au fond) : précédent art. 11 RIC.
- **F-PNR84** : Casaleggio Associati fondateur Gianroberto Casaleggio décédé 12 avril 2016 ; Rousseau M5S launch 2016 ; fondation capture hazard 2018.
- **F-PNR71** : Composition Sénat post-élections série 2 septembre 2026 : majorité relative LR + UC continue probable.
- **F-PNR73** : Art. 46 Constitution : Loi organique > Loi ordinaire ; requises pour modification électorale structurelle.

## Chiffres clés

- **37** : questions sectorielles (15 Constitution + 10 CivicTech + 12 Législatif).
- **12** : failles LLM pressenties (4 CRIT + 4 ÉLEV + 4 MOD).
- **94** : F-PNR cumulés (71 antérieurs P3 #18 + 23 nouveaux P3 #21).
- **15 000** : € budget total consultation externe (médiane).

## Acteurs majeurs

- Dominique Rousseau : Paris I Panthéon-Sorbonne IRJS, constitution + art. 11/89.
- Ferdinand Melin-Soucramanien : Paris II Panthéon-Assas, QPC + hiérarchie normes.
- Sami Tucka : Citizen Lab Munk School Toronto, CivicTech + M5S-Rousseau.

## Transversalité locale

LePack CivicTech-FR doit être externalisé en validation humaine hors-LLM (KERNEL §0 AXIOM).

## Annexe failles & questions

- **CRIT-1** : Hiérarchie Loi organique vs ordinaire non-respectée (Loi 1 Pacte CivicTech-FR classifiée ordinaire mais modif. structurelle électorale requiert Loi organique).
- **CRIT-2** : Dépendance Bürgerrat Ostbelgien sans transposition asymétrique (Ostbelgien 78 000 hab. ; France 68M).
- **CRIT-3** : Anti-capture M5S-Casaleggio non-mécaniquement spécifiée (open-source vérifiable + forkabilité insuffisant).
- **CRIT-4** : Absence mécanisme opérationnel régional vs national (RIL régional art. 72-1 vs RIC national art. 11 révisé).
- **Q-CONST-A1** : Verrou art. 89 al. 4 franchissable par voie législative ordinaire ?
- **Q-CVCT-A5** : Risque capture M5S-Casaleggio structurellement contré par open-source vérifiable + forkabilité ?
- **Q-LEGIS-B6** : Composition Sénat 2026-2030 majorité LR+UC confirmée ?
- **Experts contactables** : Dominique Rousseau (Sorbonne, 500-1000€) ; Ferdinand Melin-Soucramanien (Assas, 500-1000€) ; Sami Tucka (Citizen Lab, 1500-3000€) ; Tiago Peixoto (OECD, 1500-2500€).
- **Email template** : Sujet 'Demande expertise juridique Pack Législatif CivicTech-FR 2027' + pack complet PDF ~80 pages + protocole P3 #21 + questions sectorielles filtrées.
- **Délai** : T0 envoi -> T+2 semaines réponses (50% espéré) -> T+4-6 semaines rapports -> T+7 semaines synthèse P3 #22 -> T+8-10 semaines clôture -> T+12 semaines dépôt PPL.
- **Budget total** : 6 500-18 000€ forfait standard 15 000€ médiane (honoraires + courrier + coordination + aléas +20%).
```

**Volume : synthesis + annexe = ~110 + ~165 = 275 mots. Valide en v37 v2.**

### 16.2 Annexe B : Mapping ancien schéma v36 vs nouveau schéma v37 v2

| Champ v36 | Devenir v37 v2 | Justification |
|-----------|-----------------|---------------|
| `enquete_id` | inclus dans nom fichier + métadonnée triviale | KEEP implicite |
| `enquete_source` | métadonnée triviale via chemin | KEEP implicite |
| `these_centrale` | section "Thèse" en haut compress.md | KEEP (champ pivot) |
| `faits_atomiques[]` (24 items) | section "Faits clés" (5-7 items) | TRIM |
| `urls_prioritaires[]` | inclus dans chaque F-### si URL tier 1 | TRIM (déplacé) |
| `shadow_factor` | ELIMINÉ | KILL (invention) |
| `theses_implicites[]` | ELIMINÉ | KILL (invention) |
| `acteurs[]` legacy | ELIMINÉ | KILL (doublon) |
| `causalites[]` legacy | ELIMINÉ | KILL (doublon) |
| `causalites_pelote[]` (32 nœuds) | Annexe conditionnelle si format=JURIDIQUE/PROCÉDURE | TRIM radical + preservation ciblée |
| `perspectives_dialectiques[]` | intégré dans nuance dialectique de la thèse | TRIM |
| `limites[]` | ELIMINÉ | KILL (pas opérationnel Phase 2) |
| `wolves[]` | ELIMINÉ | KILL (taxonomie inventée) |
| `iceberg{}` | ELIMINÉ | KILL (pas comparable inter-enquête) |
| `chronologie[]` | Annexe si format=HISTORIQUE | TRIM radical + preservation ciblée |
| `domaines[]` | ELIMINÉ | KILL (métadonnée LLM) |
| `mnemo_queries[]` | ELIMINÉ | KILL (contrat aspirational) |
| `positions_acteurs[]` | section "Acteurs majeurs" (2-3 items) | TRIM radical |
| `impact[]` | section "Chiffres clés" (3-5 items) | TRIM |
| `recommandations[]` | Annexe si format=PROCÉDURE sous titre "Composants T+" | TRIM radical + preservation ciblée |
| `compress_summary` | fichier autonome `compress.md` + nouvelle ligne `**Format détecté**` | KEEP + extension format-awareness |
| **NOUVEAU v37 v2** | ligne `**Format détecté**` ∈ {10 formats} | détection format heuristique |
| **NOUVEAU v37 v2** | section `## Annexe [Type]` ≤200 mots si format ≠ ANALYTIQUE | preservation listes opérationnelles |

### 16.3 Annexe C : Glossaire forensique des termes (v37 v2)

| Terme | Définition |
|-------|-----------|
| **Denoising** | Réduction du volume de texte sans perdre le signal utile (signal/bruit) |
| **Compression ratio** | ratio `volume_brut / volume_compress`. Cible v37 v2 : ≥31× |
| **Signal pur** | contenu extractible verbatim depuis l'enquête source, sans réécriture |
| **Invention LLM** | contenu halluciné par le LLM pour satisfaire un schéma large (hors source) |
| **VERBATIM** | copie littérale d'un énoncé de l'enquête (sans paraphrase) |
| **Transversalité** | fait/chiffre/acteur comparé entre ≥2 enquêtes |
| **Fausse transversalité** | transversalité créée par le bruit du schéma (champ invention mis en relation accidentelle) |
| **HOT_PATH** | chemin d'exécution critique (où les performances doivent être optimales) |
| **Tirets cadratins** | caractère U+2014 (-), interdit par les conventions du projet |
| **Espace insécable** | caractère U+00A0 (obligatoire avant ":" selon les conventions typographiques françaises) |
| **Format-Aware** | (v37 v2) détection automatique du format d'enquête parmi 10 prédéfinis pour appliquer une Annexe conditionnelle |
| **Format détecté** | (v37 v2) l'un des 10 formats : PROCÉDURE, MÉTA, JURIDIQUE, COMPARAISON, HISTORIQUE, TECHNIQUE, SONDAGES, SOCIOLOGIE, MÉDIATIQUE, ANALYTIQUE |
| **Annexe conditionnelle** | (v37 v2) section `## Annexe [Type]` ≤200 mots préservant les listes opérationnelles verbatim (jalons/contacts/articles/pays/chronologie/stack/panel/cartographie) selon le format détecté |
| **Liste opérationnelle** | liste non-paraphrasable de faits verbatim (Plan T0/T+6/T+12/T+18/T+36, contacts experts, articles juridiques stricts, pays comparés, chronologies datées, stack technique chiffrée, panels CSP) nécessaire à la rédaction Phase 3 |

---

## §17. Conclusion (v37 v2)

### 17.1 En une phrase

**Phase 1 v37 v2 est une compression ×31 du design v36 avec préservation opérationnelle format-aware** : un seul sub-agent détecte le format parmi 10, produit un fichier Markdown de 300 mots (synthèse 100 mots + Annexe opérationnelle ≤200 mots si ≠ ANALYTIQUE), validé par un validateur Python de 150 lignes M0-M7 versus 623, et supprime 1 149 lignes nettes de prompts/validateurs obsolètes.

### 17.2 Quatre décisions architecturales clés v37 v2

1. **Fusion LECTEUR + EXTRACTEUR en un seul sub-agent** : élimine le téléphone arabe sémantique + les retries JSON.
2. **Abandon du format JSON pour le format Markdown** : libère l'attention LLM sur le sens (vs sur les accolades).
3. **Détection automatique du format parmi 10** : ajoute une Annexe conditionnelle ≤200 mots pour préserver les listes opérationnelles (Plan T+, contacts experts, articles juridiques, pays comparés, chronologies) que compress_summary ≤100 mots détruit.
4. **Validateur M0-M7 format-awareness** : 8 métriques dont M0 (format reconnu) et M7 (Annexe conditionnelle ≥30 mots si ≠ ANALYTIQUE) garantissent la préservation sans nuire au denoising.

### 17.3 Trois risques principaux résiduels

1. **R3 (mauvaise détection format)** : mitigation par heuristique cascade + log de confiance.
2. **R4 (Annexe bavarde >200 mots)** : mitigation par retry de condensation.
3. **R1 (synthèse >120 mots)** : mitigation par consigne condensée.

### 17.4 Juge de paix

**Test A/B sur 5 enquêtes RIC couvrant 5 formats distincts** (ANALYTIQUE, PROCÉDURE, MÉTA, JURIDIQUE, COMPARAISON) tranchera entre v36 et v37 v2 dans les 7 jours suivant l'implémentation. Verdict attendu : Branche A (compress.md format-aware) détecte ≥5 transversalités + préserve ≥80% des listes opérationnelles que Branche B (quintessence v36) enterre dans le JSON.

---

_Fin des SPECS Phase 1 v37 v2. Statut : DRAFT v2. À valider par implémentation + Test A/B sur 5 enquêtes couvrant 5 formats._
