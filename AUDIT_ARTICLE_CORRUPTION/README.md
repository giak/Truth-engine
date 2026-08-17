# AUDIT DE L'ARTICLE : « La corruption legale : quand respecter la loi ne suffit plus a garantir l'integrite »

- **DATE DE L'ARCHIVE** : 2026-08-12, 22:15 CEST
- **ARTICLE A AUDITER** : `ARTICLE_A_AUDITER.md` (v4, ~3 900 mots, 26 sources avec URLs)
- **OBJECTIF** : Permettre a un LLM externe independant de verifier chaque affirmation de l'article, de reconstruire la chaine de preuve, et de detecter les erreurs, exagerations ou biais.

---

## 1. Ce que contient cette archive

```
AUDIT_ARTICLE_CORRUPTION/
├── README.md                          # Ce document
├── ARTICLE_A_AUDITER.md               # L'article v4 (objet de l'audit)
├── CORRUPTION_DEFINITION.md           # Definition de la corruption utilisee comme cadre
├── METHODOLOGIE/
│   ├── KERNEL.md                      # Protocole KERNEL v2.8 (methode d'investigation)
│   ├── APEX.md                        # Protocole APEX (specification executive)
│   └── SYMBOLS.md                     # Definitions des symboles et classification EPI
├── CHAINE_DE_FABRICATION/             # Documents montrant comment l'article a ete construit
│   ├── 01_point-consolide-final-definitif.md   # Bilan final : 242 docs, 1 663 FCT, 20 secteurs
│   ├── 02_synthese-massive-finale.md           # Synthese de tous les dossiers agreges
│   ├── 03_iceberg-max-v4_REGISTRE.md           # Registre ICEBERG MAX (pistes P1-P15)
│   ├── 04_cloture-7-gaps.md                    # Resolution des 7 GAPs restants
│   └── 05_run3-enrichissement_REGISTRE.md      # Registre du run3 (dossiers 08-09)
├── DOSSIERS_SECTORIELS/               # Investigations par secteur (documents-sources)
│   ├── ENR/                           # Run2-ENR : energie, Valeco, pantouflage (89 docs)
│   ├── BUZYN/                         # Vaccination obligatoire, Buzyn (5 docs)
│   ├── ALSTOM-AREVA/                  # Cessions Alstom/Areva, BlackRock (5 docs)
│   ├── AUTOROUTES-ADP-FLAMANVILLE/    # Run4 : autoroutes, ADP, EPR (1 doc)
│   └── FONCIER/                       # Run5 : speculation fonciere, DVF (1 doc)
└── ICEBERG_MAX/                       # Corpus anticorruption (35 docs, pistes transversales)
    ├── iceberg-max_REGISTRE.md
    └── synthese-finale_SYNTHESE.md
```

**Note importante** : Cette archive contient les **documents-sources** les plus importants (points consolidés, synthèses, registres, documents d'investigation clés). Elle ne contient pas l'intégralité des 242 documents. Si l'auditeur a besoin d'un document supplementaire pour verifier un claim specifique, il doit le signaler. Les documents manquants sont disponibles dans les repertoires d'investigation originaux.

---

## 2. Comment auditer cet article

### 2.1 Verifier la chaine de preuve

Pour chaque affirmation factuelle de l'article, l'auditeur doit pouvoir remonter la chaine :

```
Claim dans l'article → Document d'investigation → FCT (fait certifie) → Source primaire (URL)
```

**Exemple** : L'article affirme que « la Cour des comptes recommande depuis 2008 de collecter les couts reels, recommandation reiteree en 2013, 2018 et 2023. En 2026, elle n'est toujours pas appliquee. »

- **Source primaire** : Cour des comptes, rapport ENR mars 2026 (URL dans la section Sources de l'article)
- **FCT correspondant** : Verifier dans les documents ENR/ le FCT qui documente cette recommandation et sa non-application
- **Verification** : L'URL du rapport CdC confirme-t-elle que la recommandation existe et n'est pas appliquee ?

### 2.2 Points critiques a verifier (ordre de priorite)

#### P0 -- Verifications bloquantes

1. **Les 26 URLs de la section Sources sont-elles toutes accessibles ?** Verifier chaque URL. Une URL morte ou pointant vers un mauvais contenu invalide la source correspondante.

2. **Les chiffres agreges sont-ils coherents ?** 
   - 242 documents : le point consolide final les decompose-t-il correctement ?
   - 1 663 FCT cross-dossier uniques : le decompte est-il verifiable ?
   - 20 secteurs : la liste est-elle complete et chaque secteur est-il documente ?

3. **Les 5 mecanismes sont-ils vraiment confirmes sur les 20 secteurs, ou seulement sur certains ?** L'article affirme que les 5 mecanismes sont « transversaux a 20 secteurs ». Verifier pour chaque mecanisme combien de secteurs le confirment reellement.

#### P1 -- Verifications importantes

4. **Le cas HATVP (2 incompatibilites sur ~600 avis)** : L'article affirme que seuls 2 regulateurs/agents d'AAI ont ete formellement bloques (avis 2024-294 et 2025-103). Les URLs HATVP confirment-elles ce decompte ? Le scan des 598 avis de compatibilite avec reserves (document GAP P2) est-il exhaustif ?

5. **Le cas Valeco/ENR (31,3 M EUR dividendes, 100 % allemand)** : Les comptes RCS et Pappers confirment-ils ces chiffres ? La chaine de propriete (MIROVA → EnBW/Commerzbank) est-elle documentee ?

6. **Le cas Dutreil (5,5 Md EUR, 110 donataires)** : Le rapport CdC + IPP confirme-t-il ces chiffres exacts ? La concentration sur 110 beneficiaires est-elle explicitement dans le rapport ?

7. **Le cas Buzyn** : La chronologie (arret CE 08/02/2017 → creation CTV 22/03/2017 → nomination 17/05/2017 → annonce 05/07/2017) est-elle exacte ? Chaque date est-elle sourcee ?

8. **Le cas autoroutes (14,8 Md vente, 34-40 Md dividendes)** : Le rapport CdC 2019 confirme-t-il ces chiffres ? Sont-ils actualises ?

#### P2 -- Verifications de coherence

9. **L'article franchit-il des seuils que les investigations avaient laisses ouverts ?** Comparer chaque claim de l'article avec le document d'investigation correspondant. L'article ajoute-t-il des affirmations non presentes dans les sources ?

10. **Les 6 hypotheses falsifiees** : Sont-elles listees quelque part ? Leur falsification est-elle documentee ou simplement affirmee ?

11. **Le ton est-il coherent avec les sources ?** L'article utilise des formulations comme « gravemenent conteste » ou « massif ». Ces qualificatifs sont-ils justifies par les donnees ?

### 2.3 Methode d'audit recommandee

1. **Premiere passe** : Lire l'article integralement. Noter TOUTES les affirmations factuelles (chiffres, dates, noms, attributions causales).
2. **Deuxieme passe** : Pour chaque affirmation, identifier la source dans la section Sources de l'article.
3. **Troisieme passe** : Verifier chaque URL. L'URL est-elle accessible ? Le contenu correspond-il a l'affirmation ?
4. **Quatrieme passe** : Pour les affirmations sans URL directe (ex. « 31,3 M EUR dividendes Valeco »), chercher le document d'investigation correspondant dans les dossiers sectoriels.
5. **Cinquieme passe** : Verifier la coherence d'ensemble. Les chiffres agreges (242, 1 663, 20, 23) sont-ils coherents entre les differents documents de synthese ?
6. **Rapport final** : Produire un verdict structure :
   - Claims confirmes (source verificable, contenu correspondant)
   - Claims partiellement confirmes (source accessible mais interpretation discutable)
   - Claims non verifiables (source inaccessible, secret des affaires, etc.)
   - Claims infirmes (source contredit l'affirmation)
   - Claims non sources (aucune source identifiable)

---

## 3. Contexte de fabrication

### 3.1 Chronologie

- **8-9 aout 2026** : Investigation preliminaire (29 dossiers : Dutreil, CumCum, EDF, banques, revolving doors)
- **10 aout 2026** : Run2-ENR (89 documents, focus Valeco/ENR + pantouflage HATVP)
- **11 aout 2026** : ICEBERG MAX (35 documents, 15 pistes transversales : McKinsey, pharma, armes, offshore, etc.) + Buzyn (5 documents) + Alstom-Areva (5 documents)
- **12 aout 2026, matin** : Run4 (autoroutes, ADP, Flamanville) + Run5 (speculation fonciere, DVF) + cloture des 7 GAPs restants
- **12 aout 2026, 13:30** : Synthese massive finale (tous dossiers agreges)
- **12 aout 2026, 14:00** : Article Phase 3 v1
- **12 aout 2026, 21:15** : Point consolide final definitif
- **12 aout 2026, 21:30** : Article v3 (corrections HATVP, run4, run5)
- **12 aout 2026, 22:00** : Article v4 (26 sources avec URLs precises)

### 3.2 Methode

- **Protocole KERNEL v2.8** : voir `METHODOLOGIE/KERNEL.md`
- **Classification EPI** : Fait (FACT), Preuve (EVIDENCE), Inference (INFERENCE), Hypothese (HYPOTHESIS), Speculation (SPECULATION), Inconnu (UNKNOWN)
- **Grille 3 axes** : Penal (violation de la loi ?), Integrite (garde-fous fonctionnent-ils ?), Legitimite (conditions du controle citoyen ?)
- **Revue contradictoire** : Chaque document a ete soumis a un code-reviewer (DeepSeek) avec correction des erreurs P0/P1 identifiees
- **Regles strictes** : Zero tiret cadratin (em-dash), guillemets francais, espaces inseccables avant « : », sources verificables, pas de fabrication

### 3.3 Limites assumees

- **Aucune corruption penale documentee** : L'article le dit explicitement (section 5, « Ce qui n'est pas documente »)
- **Secret des affaires, secret fiscal, secret-defense** : Rendent certaines hypotheses inverifiables
- **OSINT uniquement** : Pas d'acces a des sources confidentielles, judiciaires ou internes
- **Periode courte** : 4 jours d'investigation, pas une enquete de plusieurs mois

---

## 4. Instructions pour l'auditeur LLM

### 4.1 Ce que tu dois faire

1. **Lire tous les documents de cette archive** dans l'ordre recommande ci-dessous.
2. **Verifier chaque affirmation factuelle de l'article** en remontant la chaine de preuve.
3. **Signaler toute erreur, exageration, biais ou angle mort**.
4. **Produire un rapport d'audit structure** (verdict par claim).
5. **Ne RIEN inventer** : si une verification est impossible, le dire explicitement.

### 4.2 Ordre de lecture recommande

1. `CORRUPTION_DEFINITION.md` -- le cadre conceptuel
2. `METHODOLOGIE/KERNEL.md` -- la methode
3. `METHODOLOGIE/SYMBOLS.md` -- les definitions (FCT, EPI, etc.)
4. `ARTICLE_A_AUDITER.md` -- l'objet de l'audit (premiere lecture)
5. `CHAINE_DE_FABRICATION/01_point-consolide-final-definitif.md` -- le bilan global
6. `CHAINE_DE_FABRICATION/02_synthese-massive-finale.md` -- la synthese
7. Les dossiers sectoriels pertinents pour les claims que tu souhaites verifier
8. `ARTICLE_A_AUDITER.md` -- relecture avec les sources en main
9. Redaction du rapport d'audit

### 4.3 Format du rapport d'audit attendu

```markdown
# RAPPORT D'AUDIT -- Article « La corruption legale »

## 1. Verdict global
[CONFIRME / PARTIELLEMENT CONFIRME / NON CONFIRME] -- justification en 3 phrases

## 2. Verification des sources (26 URLs)
| # | URL | Accessible ? | Contenu correspond ? | Note |
|---|---|---|---|---|
| 1 | ... | OUI/NON | OUI/PARTIEL/NON | ... |

## 3. Verification des claims principaux
| Claim | Verdict | Source | Preuve |
|---|---|---|---|
| « 934 infractions probite 2024 » | CONFIRME | URL SSMSI | ... |
| « 2 incompatibilites HATVP » | A VERIFIER | ... | ... |

## 4. Erreurs factuelles identifiees
[Liste avec correction proposee]

## 5. Exagerations ou biais
[Liste]

## 6. Angles morts
[Ce que l'article ne dit pas mais qui serait pertinent]

## 7. Conclusion et recommandations
```

---

## 5. Fichiers NON inclus (disponibles sur demande)

L'archive ne contient pas :
- Les 242 documents d'investigation complets (seuls les plus importants sont inclus)
- Les donnees brutes (CSV, JSON, PDF telecharges)
- Les logs et fichiers temporaires
- Les documents des 29 dossiers 08-09 non consolides

Si l'auditeur a besoin d'un document supplementaire, le demander avec le chemin precis. Les repertoires originaux sont dans :
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/`
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_corpus-anticorruption/`
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-12_*/`

---

*Archive preparee le 12 aout 2026, 22:15 CEST. Protocole KERNEL v2.8. Zero em-dash.*
