# ENRICHISSEMENT SUBSTACK : Suivi des modifications S1-S15
> **Date de création :** 2026-05-26
> **Objet :** Enrichissement des articles « Le Changement de Régime » par le corpus Substack existant
> **Périmètre :** 14 articles S (S1-S15 sans S12) + 84 posts Substack publiés
> **État global :** 🟡 Phase 1 (liens) terminée : Phase 2 (contenu) en cours

---

## §0 : Pourquoi enrichir les articles S avec les posts Substack ?

### Le problème

Les **articles S** (format enquête synthétique, ~8-20K signes) constituent la colonne vertébrale de la série « Le Changement de Régime ». Ils sont denses, causaux, chiffrés. Mais ils sont écrits dans un **vide relatif** : le corpus Substack existant (84 posts, certains de 120K+ signes) n'est pas exploité dans leur rédaction.

Conséquence : les articles S répètent parfois des démonstrations déjà faites, sans les approfondir ; ils manquent d'exemples concrets, d'ancrages théoriques, de chair narrative.

### La solution

**Enrichir avec parcimonie** : ne pas réécrire les articles S, mais y injecter des éléments choisis des posts Substack là où ils apportent une plus-value démontrable :

| Type d'enrichissement | Description | Exemple (S15 + post) |
|----------------------|-------------|----------------------|
| 🔬 **Démonstration** | Chiffre ou mécanisme du post qui remplace une abstraction | Boucle colère-impuissance (post « Paradoxe français ») → §1 |
| 📖 **Narration** | Anecdote ou cas concret qui illustre | Exemples de ré-enracinement (post « Constellation d'avril ») → §5 |
| 🧠 **Explication** | Concept ou causalité mieux développée | Référence à Lorenz sur l'empreinte (post « Ingénierie de l'enclos ») → §4 |

### Principe directeur

**Parcimonie** : chaque injection doit pouvoir se justifier par « cet article S est meilleur AVEC qu'il ne l'était SANS ». Maximum 2-3 phrases par injection. L'article S doit rester reconnaissable. L'enrichissement ne doit pas changer sa structure.

---

## §1 : Procédure & Conventions

### 1.1 Convention de marquage

Chaque injection dans un article S porte les marqueurs suivants :

| Marqueur | Usage | Exemple |
|----------|-------|--------|
| `<!-- ENRICHIE: post-slug -->` | Injection de contenu issu d'un post Substack | `<!-- ENRICHIE: le-paradoxe-francais-66-de-colere -->` |
| `<!-- CROSS-REF: S{num} -->` | Référence inter-article | `<!-- CROSS-REF: S10 -->` |
| `<!-- THEME: {slug} -->` | Renforcement d'un fil thématique global | `<!-- THEME: impotence-apprise -->` |

**Slugs des 5 fils thématiques :**

| Fil | Slug |
|-----|------|
| Impuissance apprise | `impotence-apprise` |
| Double peine | `double-peine` |
| Prédation invisible | `predation-invisible` |
| Verrouillage systémique | `verrouillage-systemique` |
| Résilience locale | `resilience-locale` |

Chaque injection porte AU MOINS `<!-- ENRICHIE: ... -->`. Elle peut porter `<!-- THEME: ... -->` et/ou `<!-- CROSS-REF: S{num} -->` si elle sert un fil ou une connexion inter-article.

### 1.2 Lexique des 🔗 marqueurs (section « À voir aussi »)

| Marqueur | Signification |
|----------|---------------|
| 🔗 **Lien direct** | Le post traite EXACTEMENT du sujet de l'article S |
| 🔗 **Lien indirect** | Le post aborde un thème connexe mais pas le sujet central |
| 🔗 **Le plus connexe** | Parmi les posts liés, celui-ci est le plus proche du sujet |

### 1.3 Workflow : enrichissement réticulaire

```
ÉTAPE 0 : PRÉ-REQUIS GLOBAL
    ├── Lire la DIALECTIQUE (5 tensions, piège causal)
    ├── Comprendre la fonction de l'acte dans lequel se situe l'article
    └── Consulter la carte inter-articles (§4.3) et les fils thématiques (§4.1)

ÉTAPE 1 : ANALYSE INDIVIDUELLE
    ├── Confronter l'article S à ses posts Substack associés
    ├── Identifier les opportunités : 🔬 Démonstration, 📖 Narration, 🧠 Explication
    └── Prioriser selon la parcimonie (max 2-3 phrases, 5 % de signes max)

ÉTAPE 2 : ANALYSE RÉTICULAIRE
    ├── Identifier les cross-links possibles avec d'autres articles S (carte §4.3)
    ├── Vérifier que l'enrichissement ne duplique pas une démonstration déjà faite
    ├── S'assurer qu'il renforce AU MOINS UN fil thématique global (§4.1)
    └── Vérifier la progression narrative (Acte 1 → Acte 2 → Acte 3 → Acte 4)

ÉTAPE 3 : INTÉGRATION S0 (conditionnelle)
    ├── Vérifier si S0 (numérique → promu S16) éclaire l'article en cours
    └── Si oui, intégrer via cross-ref ou enrichissement ponctuel

ÉTAPE 4 : INJECTION + MARQUAGE
    ├── Injecter avec `<!-- ENRICHIE: post-slug -->`
    ├── Ajouter `<!-- THEME: slug -->` si renforcement d'un fil
    └── Ajouter `<!-- CROSS-REF: S{num} -->` si connexion inter-article

ÉTAPE 5 : VÉRIFICATION DE COHÉRENCE GLOBALE
    ├── Vérifier que l'enrichissement n'introduit pas de contradiction
    ├── Vérifier la cohérence terminologique avec le reste de la série
    ├── Vérifier que le ton forensique est respecté
    └── Vérifier la lisibilité sans dépendance aux posts ou autres articles S
```

### 1.4 Principes généraux

**Pourquoi enrichir le contenu (et pas seulement mettre des liens) :**
1. **Crédibilité journalistique** : l'article S s'appuie sur un corpus existant, il ne part pas de zéro
2. **Épaisseur** : les posts Substack densifient l'article sans le faire dévier de sa structure
3. **Effet réseau** : le lecteur voit qu'il peut creuser sur Substack → appel à l'abonnement implicite
4. **Non-redondance** : l'article S résume une démonstration déjà faite et renvoie au post pour l'approfondissement

**Limites :**
- ❌ Ne pas réécrire l'article S : sa structure et son ton restent intacts
- ❌ Ne pas ajouter plus de 5 % de signes par article
- ❌ Ne pas citer un post qui contredit la thèse de l'article S
- ❌ Ne pas créer de dépendance : l'article S doit être lisible sans les posts ni les autres articles S
- ✅ Privilégier les injections qui ajoutent un **exemple concret**, un **ancrage théorique**, ou un **chiffre qui fait mouche**

---

## §2 : Phase 1 : Sections « À voir aussi » injectées ✅

### 2.1 Récapitulatif

| Article | Posts injectés | 🔗 Gradation | Statut | Date |
|---------|---------------|-------------|--------|------|
| **S1** : Caste | 4 : Ils ont quitté l'humanité, Féodalité financiarisée, Empire du mensonge, Richesse verrouille | Fort | ✅ | 2026-05-25 |
| **S2/S3** : Argent/Dette | 4 : Emprunt forcé, Vampire de la croissance, Budget 2026, Crédit social | Fort | ✅ | 2026-05-25 |
| **S4** : Santé | 2 : UE-Mercosur, DNC | Moyen | ✅ | 2026-05-25 |
| **S5** : Pauvreté | 2 : Grand manège, Empire des miettes | Moyen | ✅ | 2026-05-25 |
| **S6** : Industrie | 1 : ArcelorMittal | Faible | ✅ | 2026-05-25 |
| **S7** : École | 1 : Effondrement éducatif | Moyen | ✅ | 2026-05-25 |
| **S8** : Immigration | 3 : État qui contrôle, Machine à silence, Démocratie en cage | Faible→Moyen | ✅ | 2026-05-25 |
| **S9** : Logement | 3 : Architecture à l'œuvre, Grand manège, Richesse verrouille | Moyen→Fort | ✅ | 2026-05-25 |
| **S10** : Énergie/Climat | 3 : Sabotage énergétique, Deux escroqueries, Ciel pas gratuit | Très fort | ✅ | 2026-05-25 |
| **S11** : Agriculture | 3 : Grande arnaque, Agriculture au scanner, UE-Mercosur | Très fort | ✅ | 2026-05-25 |
| **S13** : Europe | 3 : Crédit social doux, Censure européenne, UE-Mercosur | Très fort | ✅ | 2026-05-25 |
| **S14** : Défense | 2 : Armée Potemkine, Guerre des autres | Très fort | ✅ | 2026-05-25 |
| **S15** : Verrou | 6 : Démocratie en cage, Paradoxe français, Opposition contrôlée, Audiovisuel public, Ingénierie de l'enclos, Télégraphistes | Très fort | ✅ | 2026-05-25 |
| **Total (uniques)** | **32 posts** | : | ✅ **14/14** | |

### 2.2 Renommage

| Date | Action | Détail |
|------|--------|--------|
| 2026-05-26 | Renommage S1-S7 | `### Lectures complémentaires` → `### À voir aussi` |
| 2026-05-26 | Renommage S8-S15 | `### Lectures complémentaires` → `### À voir aussi` |
| 2026-05-26 | Vérification | 0 occurrence restante de « Lectures complémentaires » ; 14/14 articles avec « ### À voir aussi » ✅ |

---

## §3 : Phase 2 : Enrichissement contenu (en cours) 🟡

### 3.1 Article pilote : S15 : Le Verrouillage démocratique

**Statut :** 5 enrichissements injectés ✅

**Posts Substack associés (6) :**
1. « La démocratie en cage » : verrouillage institutionnel
2. « Le paradoxe français : 66 % de colère, zéro résultat » : défiance citoyenne
3. « Opposition contrôlée : anatomie d'un siphonnage » : verrou médiatique
4. « Audiovisuel public : anatomie d'une asphyxie » : concentration médias
5. « L'ingénierie de l'enclos » : enfermement mental
6. « La constellation d'avril : la révolution silencieuse qui vient » : ré-enracinement

**Opportunités identifiées :**

| Section | Post source | Injection proposée | Parcimonie | Effet attendu |
|---------|-------------|-------------------|------------|---------------|
| **§1** : Paradoxe | « Paradoxe français » | Boucle colère-impuissance : la colère mesurée par enquêtes → confinée dans les urnes → jamais traduite politiquement | 2-3 phrases | Rend le paradoxe *vécu* |
| **§2** : Opposition contrôlée | « Opposition contrôlée » | Chiffre précis de subventions : tel syndicat a reçu X euros sans appeler à une seule grève | 1-2 phrases | Ancre la démo dans un fait |
| **§3** : Audiovisuel public | « Audiovisuel public » | Jalons chronologiques : nomination X → départ Y → purge Z | 2-3 dates | Montre le *processus* |
| **§4** : Ingénierie | « Ingénierie de l'enclos » | Référence Lorenz (empreinte) + Bourdieu (violence symbolique) | 1 phrase | Épaissit théoriquement |
| **§5** : Constellation | « Constellation d'avril » | Exemples concrets d'initiatives de ré-enracinement (nommer, situer) | 3-4 lignes | Rend l'alternative tangible |

**Injections réalisées :**
- §2 : Jalons chronologiques audiovisuel public (post « Audiovisuel public ») `<!-- ENRICHIE: audiovisuel-public-anatomie-dune -->` `<!-- THEME: verrouillage-systemique -->` `<!-- CROSS-REF: S3, S7 -->`
- §3 : Boucle colère-impuissance (post « Paradoxe français ») `<!-- ENRICHIE: le-paradoxe-francais-66-de-colere -->` `<!-- THEME: impotence-apprise -->` `<!-- CROSS-REF: S5, S7 -->`
- §4 : Subventions comme outil de contrôle (post « Opposition contrôlée ») `<!-- ENRICHIE: opposition-controlee-anatomie-dun -->` `<!-- THEME: double-peine -->` `<!-- CROSS-REF: S8, S10 -->`
- §5 : Référence Lorenz + Bourdieu (posts « Ingénierie de l'enclos », « Démocratie en cage ») `<!-- ENRICHIE: lingenierie-de-lenclos -->` `<!-- ENRICHIE: la-democratie-en-cage -->` `<!-- THEME: impotence-apprise -->` `<!-- CROSS-REF: S1 -->`
- §6 : Exemples concrets alternatives (post « Constellation d'avril ») `<!-- ENRICHIE: la-constellation-davril -->` `<!-- THEME: resilience-locale -->` `<!-- CROSS-REF: S6, S10, S11 -->`

**Review :** ✅ Validé par code-reviewer : injections concises, bien placées, respect du principe de parcimonie

**Marqueurs THEME + CROSS-REF :** ✅ Appliqués et vérifiés (5/5 slugs conformes)

### 3.2 Articles suivants (à analyser)

| Article | Posts Substack | État |
| **S1** : Caste | 4 posts | ✅ 2 enrichissements |
| **S2** : Argent | 4 posts | ✅ 2 enrichissements |
| **S3** : Dette | partagés avec S2 | ✅ 2 enrichissements |
| **S4** : Santé | 2 posts | ✅ 1 enrichissement |
| **S5** : Pauvreté | 2 posts | ✅ 2 enrichissements |
| **S6** : Industrie | 1 post | ✅ 3 enrichissements |
| **S0** : Numérique | 4 posts | ✅ 2 enrichissements |
| **S7** : École | 1 post | ✅ 2 enrichissements |
| **S8** : Immigration | 3 posts | ✅ 2 enrichissements |
| **S9** : Logement | 3 posts | ✅ 2 enrichissements |
| **S10** : Énergie/Climat | 3 posts | ✅ 2 enrichissements |
| **S11** : Agriculture | 3 posts | ✅ 2 enrichissements |
| **S13** : Europe | 3 posts | ✅ 2 enrichissements |
| **S14** : Défense | 2 posts | ✅ 2 enrichissements |

---

## §4 : Références transverses

> **Objet :** Passer d'un enrichissement linéaire (post→article) à un enrichissement réticulaire (post↔article↔article)
> pour que les articles forment un tout cohérent et complémentaire.

### 4.1 Les 5 fils thématiques globaux

Ces fils traversent TOUS les articles S. Chaque enrichissement doit les renforcer pour créer des motifs récurrents.

| Fil | Définition | Apparaît dans | Posts sources |
|-----|-----------|--------------|---------------|
| 🧵 **Impuissance apprise** | Certitude que toute action citoyenne est absorbée sans effet | S1, S3, S5, S8, S15 | « Paradoxe français », « Démocratie en cage », « Ingénierie de l'enclos » |
| 🧵 **Double peine** | Les victimes paient deux fois : extraction + privatisation des solutions | S2, S4, S5, S10 | « Grand manège », « Empire des miettes », « Deux escroqueries » |
| 🧵 **Prédation invisible** | L'extraction masquée par un discours technique | S1, S2, S3, S9 | « Emprunt forcé », « Budget 2026 », « Architecture à l'œuvre » |
| 🧵 **Verrouillage systémique** | Institutions conçues pour résister au changement | S13, S14, S15 | « Crédit social », « Censure européenne », « Télégraphistes » |
| 🧵 **Résilience locale** | Alternatives fragmentaires qui préfigurent l'avenir | S6, S10, S11, §6 de chaque article | « Constellation d'avril », « Agriculture au scanner » |

### 4.2 Stratégie par acte narratif

| Acte | Articles | Fonction | Type prioritaire | Fil dominant |
|------|----------|----------|-----------------|--------------|
| **1** : Accusation | S1, S2, S3, S15 | Poser les faits, nommer les criminels | 🔬 Démonstration (chiffres, mécanismes) | Prédation invisible + Verrouillage |
| **2** : Scènes de crime | S4, S5, S7, S8, S9 | Montrer le coût humain | 📖 Narration (anecdotes, cas concrets) | Double peine + Impuissance apprise |
| **3** : Échelle du crime | S10, S11, S6, S13, S14 | Monter en abstraction | 🧠 Explication (concepts, causalités) | Verrouillage + Résilience |
| **4** : Verdict | HUB, S16 (ex-S0) | Synthèse, irréformabilité, ouverture | 🧠 + 🔬 convergence | Les 5 fils convergent |

### 4.3 Carte inter-articles (cross-links)

| Source | Démonstration | Peut enrichir |
|--------|--------------|---------------|
| S2 (évasion 80-100 Md€/an) | L'extraction qui vide les caisses | S3 (dette), S5 (pauvreté), S10 (climat) |
| S3 (dette instrumentalisée) | L'austérité comme prétexte | S4, S7, S9, S14 (tous les démantèlements) |
| S15 (verrouillage) | 49.3, médias, abstention | S1 (la caste verrouille), S13 (UE verrou), S6 (industrie sacrifiée) |
| S10 (double peine énergétique) | Pauvres paient la transition ET la non-transition | S5 (pauvreté), S2 (argent manquant) |
| S11 (agriculture) | PAC, libre-échange, suicide paysan | S13 (UE verrouille PAC), S5 (pauvreté rurale) |
| S6 (désindustrialisation) | 81 Md€ déficit commercial | S3 (perte valeur ajoutée), S14 (défense sans base) |
| S4 (santé) | 8M sans médecin traitant | S5 (renoncement aux soins), S9 (logement insalubre) |
| S13 (Europe carcan) | 12 contentieux, perte souveraineté | S3, S6, S11 (multiplicateur des tensions) |

**Principe :** L'enrichissement d'un article S peut inclure une référence à un autre article S (`<!-- CROSS-REF: S{num} -->`), pas seulement à un post Substack. Cela crée de la continuité, pas de la redondance.

### 4.4 Intégration de S0 (Le Numérique colonisé → S16)

**Constat :** S0 est complet (7 sections, 15 sources), formaté selon le PROMPT, mais classé comme « hors-série ». Il couvre un angle mort (souveraineté numérique) absent des 14 articles S.

**Proposition :** Promouvoir S0 en **S16** dans l'Acte 3, entre S13 (Europe : cadre numérique) et S14 (Défense : cybersécurité).
- Logique : S13 → montre comment l'UE verrouille la souveraineté → S16 montre comment le numérique la confisque → S14 montre comment la défense la perd
- Modifier le footer : `*📖 Cet article est un hors-série...*` → `*📖 Cet article fait partie de l'enquête **Le Changement de Régime**...*`
- Mettre à jour le compteur de la série (14 → 15 articles actifs)
- Ajouter S0 dans la section « À voir aussi » des articles S13 (Europe) et S14 (Défense)

**Posts Substack pertinents pour S16 :** « L'Europe construit-elle un crédit social doux ? », « L'Architecture de la censure Européenne », « La démocratie en cage », « Les télégraphistes de la terreur »

### 4.5 Les 52 posts Substack restants

Sur 84 posts, 32 sont référencés dans les articles S. Les 52 restants peuvent servir à :

| Usage | Description | Priorité |
|-------|-------------|----------|
| **HUB (Acte 4)** | Citer les posts non utilisés comme preuve de continuité journalistique : le HUB ne reçoit pas d'injections `<!-- ENRICHIE -->` mais une section de références globales listant les 5-10 posts les plus importants pour la thèse centrale | Haute |
| **Angles morts** | 5 angles identifiés par l'AUDIT (justice, transports, genre, culture, police) : scanner les 52 posts pour inventorier ceux qui les couvrent. Si assez de matière, créer des hors-séries post-série | Moyenne |
| **Épaississement** | Les posts les plus longs contiennent des détails que les articles S ne peuvent absorber : disponibles comme « lecture approfondie » via la section « À voir aussi » | Faible (déjà fait) |

---

## §5 : Changelog

### 2026-05-26

| Action | Fichier | Détail |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S5 §2 | Mécanisme du vol de salaire structurel : monopsonie 10-25%, productivité +250% vs salaire médian stagné, écart 43 points, <2% salaires volés recouvrés (post « Grand manège de la dépossession ») |
| ➕ **Injection contenu #2** | S5 §5 | Coût physiologique du transfert : OMS burnout, 47% détresse, 14% sévère, 764 décès professionnels 2024, 62% quiet quitting (post « Grand manège de la dépossession ») |
| ✅ **Review** | S5 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S7 §0 | Dictée CM2 DEPP : 10,7 erreurs (1987) → 19,4 (2021), +81% en 34 ans, mesure scientifique répétée par l'institution (post « Effondrement éducatif français ») |
| ➕ **Injection contenu #2** | S7 §3 | Fuite des élites : écoles hors contrat ×10 (260→2614), 130K élèves, EdTech 1,6 Md€, 5 ministres en 2024 (post « Effondrement éducatif français ») |
| ✅ **Review** | S7 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S8 §4 | Concept de kayfabe (Weinstein) : les 15 lois sur l'immigration comme spectacle, fiction collective du contrôle migratoire (post « La machine à silence ») |
| ➕ **Injection contenu #2** | S8 §5 | Contraste contrôle virtuel vs réel : loi 48h réseaux sociaux vs ASE 396 900, 110 morts narcotrafic, OQTF <10 % (post « L'État qui veut tout contrôler ») |
| ✅ **Review** | S8 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S9 §2 | Fixité des rangs : six générations (~150 ans) pour sortir de la pauvreté, logement comme verrou générationnel (post « Grand manège de la dépossession ») |
| ➕ **Injection contenu #2** | S9 §5 | Esclavage locatif : valeur immobilière ×6,5 plus vite que salaires en 30 ans, sans apport = esclave locatif du rentier (post « Grand manège de la dépossession ») |
| ✅ **Review** | S9 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S4 §2 | Parallèle Mercosur : audit DG Santé oct 2024, œstradiol 17β, 5 000 kg consommés NL, 20 t rappelées (post « UE-Mercosur : le mensonge sanitaire ») |
| ✅ **Review** | S4 | Validé par code-reviewer-deepseek-flash : 1 injection, marqueurs corrects |
| ➕ **Injection contenu #1** | S3 §3 | 95% fiction budgétaire : HCFP : 3/60 Md€ d'économies réelles en 2025, pas d'avis pour 2026 (post « Budget 2026 ») |
| ➕ **Injection contenu #2** | S3 §5 | Fiscal drag : salaires +2%, barème indexé à 0.9%, hausse d'impôt sans vote (post « Budget 2026 ») |
| ✅ **Review** | S3 | Validé par code-reviewer-deepseek-flash |
| ➕ **Injection contenu #1** | S10 §3 | Traînées aviation = 57% impact > CO₂ 32%, CORSIA ne régule que CO₂, 2% des vols = −80% forçage radiatif (Teoh 2020), 100 Md€/an externalités non internalisées, 4 000 morts prématurés/an Europe (Stettler 2013) (post « Le ciel n'est pas gratuit ») |
| ➕ **Injection contenu #2** | S10 §3→§4 | 9M morts/an pollution (Lancet Commission 2022) : un décès sur six, quinze fois plus que toutes les guerres. PFAS, 80% substances jamais évaluées. Le climat a tout (COP, traités, milliards), la pollution n'a rien (post « Climat : les deux escroqueries ») |
| ✅ **Review** | S10 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S11 §1 | Plan Mansholt 1968 : élimination programmée 75% en 58 ans, 1,5M→380K exploitations, Debatisse « deux tiers n'ont pas raison d'exister » (post « Agriculture au scanner ») |
| ➕ **Injection contenu #2** | S11 §2 | Opacité 92% PAC : 55 Md€ dont 50,5 cachés, FNSEA 18 réunions/an, 6 ex-ministres lobbyistes, 14,7 Md€ fraudes documentées (post « La grande arnaque agricole ») |
| ✅ **Review** | S11 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S13 §2 | Capture régulatoire : Thorn/Safer, 600K€ lobbying, Oak Foundation 24 M$, 6% CA mondial (post « Crédit social doux ») |
| ➕ **Injection contenu #2** | S13 §3 | Simulacre Mercosur : Macron « positif » nov 2024 → vote contre jan 2026, Coreper, Italie change vote (post « UE-Mercosur : le mensonge sanitaire ») |
| ✅ **Review** | S13 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S14 §1 | 4 jours de capacité (vs « quelques semaines »), syndrome du village Potemkine, démissions, échec plan Fidélisation 360 (post « Armée Potemkine ») |
| ➕ **Injection contenu #2** | S14 §4 | Stocks MICA épuisés guerre Iran 2026, 400K citoyens exposés Golfe, Araghchi humilie Macron (post « La guerre des autres ») |
| ✅ **Review** | S14 | Validé par code-reviewer-deepseek-flash : 2 injections, marqueurs corrects |
|--------|---------|--------|
| ➕ **Injection contenu #1** | S2 §2 | 400 millionnaires Tax Us Davos 2026 : preuve que l'obstacle est politique (post « Comment la richesse verrouille le système ») |
| ➕ **Injection contenu #2** | S2 §3 | Abandon PPF 15 Oct 2024 : État renonce à son outil public de collecte fiscale (post « Le réseau qui nous facture ») |
| ✅ **Review** | S2 | Validé par code-reviewer-deepseek-flash |
| 🧠 **Brainstorm** | S0 | Analyse 6 posts numériques vs structure S0 → 2 opportunités d'enrichissement |
| ➕ **Injection contenu #1** | S0 §6 | Fuites massives (HubEE 160K, FICOBA 1,2M, IDMerit 52M) + business model Sopra Steria (post « Goulag digital ») |
| ➕ **Injection contenu #2** | S0 §7 | Mise en garde eIDAS Article 45 + Chat Control (post « Crédit social européen ») |
| ✅ **Review** | S0 | Validé par code-reviewer-deepseek-flash |
|--------|---------|--------|
| 🆕 **Création** | `ENRICHISSEMENT_SUBSTACK_CHANGELOG.md` | Document de suivi de l'enrichissement |
| 🧠 **Brainstorm** | S1 | 2 opportunités identifiées : §3 (Bourdieu + dark triad / post pathologie caste) + §6 (affaire Auch / post schisme) |
| ➕ **Injection contenu #1** | S1 §3 | Cadre théorique Bourdieu (machine capital hérité → mérite) + Dark Triad (3-12% chez PDG) + thèse pathologie de caste (post « Ce n'est pas du satanisme ») |
| ➕ **Injection contenu #2** | S1 §6 | Affaire Auch 27 déc. 2025 : DDPN braque agriculteur, coalition du silence (post « Le schisme ») |
| ✅ **Review** | S1 | Validé par code-reviewer-deepseek-flash |
| 🔄 **Renommage** | S8 → S15 | `### Lectures complémentaires` → `### À voir aussi` |
| 🔍 **Vérification** | Tous les articles S | 0 occurrence « Lectures complémentaires », 14/14 « À voir aussi » ✅ |
| 🧠 **Brainstorm** | S15 | Analyse 6 posts vs structure S15 → 5 opportunités d'enrichissement |
| ➕ **Injection contenu #1** | S15 §2 | Jalons chronologiques audiovisuel public (post « Audiovisuel public ») |
| ➕ **Injection contenu #2** | S15 §3 | Boucle colère-impuissance (post « Paradoxe français ») |
| ➕ **Injection contenu #3** | S15 §4 | Subventions comme contrôle de l'opposition (post « Opposition contrôlée ») |
| ➕ **Injection contenu #4** | S15 §5 | Référence Lorenz + Bourdieu (posts « Ingénierie de l'enclos », « Démocratie en cage ») |
| ➕ **Injection contenu #5** | S15 §6 | Exemples concrets alternatives (post « Constellation d'avril ») |
| ✅ **Review** | S15 | Validé par code-reviewer-deepseek-flash |
| 🧠 **Brainstorm v2** | Global | Protocole v2 : enrichissement réticulaire : 5 limitations, 5 fils thématiques, stratégie par acte, intégration S0, carte inter-articles |
| 🏷️ **Marqueurs THEME** | S15 §2 | `<!-- THEME: verrouillage-systemique -->` + `<!-- CROSS-REF: S3, S7 -->` |
| 🏷️ **Marqueurs THEME** | S15 §3 | `<!-- THEME: impotence-apprise -->` + `<!-- CROSS-REF: S5, S7 -->` |
| 🏷️ **Marqueurs THEME** | S15 §4 | `<!-- THEME: double-peine -->` + `<!-- CROSS-REF: S8, S10 -->` |
| 🏷️ **Marqueurs THEME** | S15 §5 | `<!-- THEME: impotence-apprise -->` + `<!-- CROSS-REF: S1 -->` |
| 🏷️ **Marqueurs THEME** | S15 §6 | `<!-- THEME: resilience-locale -->` + `<!-- CROSS-REF: S6, S10, S11 -->` |
| ✅ **Review** | S15 marqueurs | Validé par code-reviewer-deepseek-flash : cohérence et slugs conformes |

### 2026-05-25

| Action | Fichier | Détail |
|--------|---------|--------|
| ➕ **Injection** | S1 (Caste) | Section « À voir aussi » : 4 posts |
| ➕ **Injection** | S2 (Argent) | Section « À voir aussi » : 4 posts |
| ➕ **Injection** | S3 (Dette) | Section « À voir aussi » : 4 posts |
| ➕ **Injection** | S4 (Santé) | Section « À voir aussi » : 2 posts |
| ➕ **Injection** | S5 (Pauvreté) | Section « À voir aussi » : 2 posts |
| ➕ **Injection** | S6 (Industrie) | Section « À voir aussi » : 1 post |
| ➕ **Injection** | S7 (École) | Section « À voir aussi » : 1 post |
| ➕ **Injection** | S8 (Immigration) | Section « À voir aussi » : 3 posts |
| ➕ **Injection** | S9 (Logement) | Section « À voir aussi » : 3 posts |
| ➕ **Injection** | S10 (Énergie) | Section « À voir aussi » : 3 posts |
| ➕ **Injection** | S11 (Agriculture) | Section « À voir aussi » : 3 posts |
| ➕ **Injection** | S13 (Europe) | Section « À voir aussi » : 3 posts |
| ➕ **Injection** | S14 (Défense) | Section « À voir aussi » : 2 posts |
| ➕ **Injection** | S15 (Verrou) | Section « À voir aussi » : 6 posts |
| 🔄 **Renommage** | S1 → S7 | `### Lectures complémentaires` → `### À voir aussi` |
| 📝 **Mise à jour** | AUDIT_RAPPORT.md | 29 → 32 posts uniques ; tableau §4.4 clarifié ; S8/S9 posts injectés |

---

## §6 : Prochaines actions (protocole v2)

### Phase 0 : Finalisation du protocole

- [x] ~~Injecter les 5 enrichissements S15 dans `S15_le_verrou.md`~~
- [x] ~~Faire review du résultat S15~~
- [x] ~~Brainstorm protocole v2 : enrichissement réticulaire~~
- [ ] **Promouvoir S0 en S16** : intégrer S0 dans la série officielle (avant S14 dans l'ordre forensique)
- [x] ~~Appliquer marqueurs thématiques et cross-ref aux 5 injections S15~~ ✅ (voir §4)
- [x] ~~Vérifier la cohérence et conformité des slugs~~ ✅ par code-reviewer

### Phase 1 : Enrichissement par acte (protocole v2)

**Acte 3 d'abord (S10, S11, S6, S13, S14) : prioritaire car les posts sont les plus forts :**

- [ ] Analyser S10 + 3 posts (sabotage énergétique, climat, ciel) + cross-ref S2, S5
- [ ] Analyser S11 + 3 posts (arnaque agricole, scanner, Mercosur) + cross-ref S13, S10, S5
- [ ] Analyser S13 + 3 posts (crédit social, censure, Mercosur) + cross-ref S3, S6, S11
- [ ] Analyser S14 + 2 posts (Armée Potemkine, guerre des autres) + cross-ref S6, S13
- [x] Analyser S6 + 1 post (ArcelorMittal) + cross-ref S3, S10, S14

**Acte 2 ensuite (S4, S5, S7, S8, S9) :**

- [ ] Analyser S4 + 2 posts (Mercosur sanitaire, DNC) + cross-ref S5, S9
- [ ] Analyser S5 + 2 posts (grand manège, empire des miettes) + cross-ref S4, S10, S11
- [ ] Analyser S7 + 1 post (effondrement éducatif) + cross-ref S5
- [ ] Analyser S8 + 3 posts (contrôle, silence, cage) + cross-ref S15, S13
- [ ] Analyser S9 + 3 posts (architecture, dépossession, verrouillage) + cross-ref S4, S5

**Acte 1 en dernier (S1, S2, S3) : les plus denses, à enrichir avec parcimonie :**

- [ ] Analyser S1 + 4 posts (caste, féodalité, mensonge, richesse) + cross-ref S15
- [ ] Analyser S2 + 4 posts (emprunt, vampire, budget, crédit social) + cross-ref S3, S5, S10
- [ ] Analyser S3 + posts partagés avec S2 + cross-ref S4, S7, S9, S14

### Phase 2 : Cohérence globale

- [ ] Vérifier la cohérence terminologique entre tous les articles S
- [ ] S'assurer qu'aucun enrichissement ne duplique une démonstration déjà faite ailleurs
- [ ] Vérifier la progression des 5 fils thématiques à travers la série
- [ ] Produire un rapport de cohérence finale avant enrichissement du HUB

---

## §7 : Métriques de suivi

| Indicateur | Valeur | Objectif |
|------------|--------|----------|
| Articles S | 14 | 14 |
| Posts Substack publiés | 84 | : |
| Posts référencés (liens) | 32 | 32 |
| Articles avec section « À voir aussi » | 14/14 (100 %) | 14/14 ✅ |
| Articles enrichis (contenu) | 14/14 (100 %) | 14/14 |
| Articles analysés (brainstorm) | 1/14 (7 %) | 14/14 |
| Injections contenu réalisées | 30 | ~2-5 par article |
| Posts Substack lus et confrontés | 15/32 (47 %) | 32/32 |

| Fils thématiques globaux | 5 définis | 5/5 ✅ |
| Carte inter-articles | 8 cross-links identifiés | : |
| S0 intégré comme S16 | Proposé (en attente validation) | : |

---

