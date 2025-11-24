# Notes d'Analyse — Génération Tweets Truth Engine

**Date:** 2025-11-12
**Corpus analysé:** 26 tweets (103→77) de `/home/giak/projects/twitter-dashboars-api/docs/twitter_post/`
**Objectif:** Extraire patterns pour générer tweets "panache" en CLI (vs "âpre")

---

## 🎯 Découvertes Clés

### 1. **5 Types de Tweets Distincts** (au lieu de 3 initiaux)

**✅ À GARDER — Typologie claire:**

| Type | Usage | Longueur | Structure | Exemples |
|------|-------|----------|-----------|----------|
| **A - Révélation choc** | Fact-check, règlement introuvable, conflit intérêt | Moyen | Titres gras inline, pas H2/H3 | 103 (Knafo), 102 (Arras) |
| **B - Anatomie système** | Entre-soi, lobby, réseau, reproduction élitaire | Moyen | Sections émojis (📌⚖️💰🧩) | 97 (Ernotte CNEWS) |
| **C - Déconstruction spectacle** | Meeting, pétition, polémique | Court-Moyen | Questions sections (💰🧩⚖️) | 100-101 (Villiers) |
| **D - Note stratégique** | Investigation État/système très complexe | Très long | H2 markdown ACCEPTÉ + séparateurs | 93 (Hidalgo), 91 (État efficace), 87 (numérique) |
| **E - Pamphlet compact** | Réaction rapide, fact-check ponctuel | Très court | Punch direct, minimal structure | 92 (Darmanin), 85 (LFI-RN), 82 (manif) |

**💡 Insight:** Le CLI produit du "Type D académique froid" alors qu'on veut Types A/B/C/E selon contexte. Type D acceptable SEULEMENT si investigation très complexe + séparateurs visuels.

---

### 2. **Patterns Structurels qui Fonctionnent**

**✅ À GARDER:**

- **Séparateurs visuels** `──────────────────────────────` entre sections (Type D uniquement)
- **Titres gras inline** `**Les faits :**` au lieu de `## Les faits` (Types A/B/C)
- **Listes avec → ou –** jamais `•`
- **Émojis fonctionnels** 📌⚖️💸🧩🎭🧨 (pas décoratifs ✨🔥💯)
- **Questions rhétoriques** intégrées narrativement: "Qui pousse vraiment cet accord?"
- **Facts ultra-précis** avec gras stratégique: `**187 000 €**`, `**13 fév. 2024**`
- **Citations françaises** `« texte »` jamais `" text "`

**❌ À ZAPPER (erreurs CLI récurrentes):**

- Intro méthodologique ("J'ai appliqué Truth Engine...")
- Numérotation plate sans émojis ("Premier problème:", "Deuxième problème:")
- Méthodologie pompante fin ("Investigation: 20 recherches, 40 sources...")
- Ton analytique démonstratif au lieu de révélatoire percutant
- Gras sur phrases entières
- H2/H3 markdown SAUF Type D avec séparateurs

---

### 3. **Vocabulaire Marqueur Étendu**

**✅ NOUVEAUX concepts identifiés (tweets 93→77):**

**Économie/État:**
- "Compteurs/totems"
- "Théâtre budgétaire"
- "Guillotine d'inactivité"
- "Racket institutionnalisé"

**Manipulation cognitive:**
- "Cadrage qui déforme"
- "Décor fait scénario"
- "Safety valve" (soupape sécurité)
- "Gatekeeper"
- "Lawfare" (judiciarisation stratégique)

**Mobilisation/Résistance:**
- "Protest paradigm" (médias cadrent sur casse, pas revendications)
- "OSINT citoyen"
- "SOP-72h" (Standard Operating Procedure)
- "État-major civil"

**💡 Insight:** Vocabulaire devient plus opérationnel (SOP, OSINT, lawfare) = passage du diagnostic à l'action citoyenne.

---

### 4. **Sections Optionnelles Découvertes**

**✅ À GARDER — 3 sections réutilisables:**

#### **A) Faisceau d'indices** (analyse pattern systémique)
```
🔎 **Faisceau d'indices**

1. **[Pattern name]**
   _Symptôme._ [Observable]
   _Signal._ [Interprétation]
   _Trace à suivre._ [Action vérifiable]

[...patterns 2-10...]

**Lecture d'ensemble.** [Diagnostic convergent]
```
**Usage:** Tweets Type D (rapports analytiques longs)
**Exemple:** 91 (État efficace — 10 patterns identifiés)

#### **B) Contre-arguments démontés** (anticipation objections)
```
💬 **Contre-arguments démontés**

_« [Objection citation] »_
**[Réponse argumentée].** [Preuves/faits]
```
**Usage:** Tous types quand investigation anticipe critiques
**Exemple:** 91 (État efficace — 8 objections démontées)

#### **C) Recommandations stratégiques** (opérationnel citoyen)
```
🔑 **Recommandations stratégiques**

**État** : [Actions concrètes]
**Citoyens** : [Actions concrètes]
**Société** : [Actions concrètes]

**Calendrier 30/90/180 jours** :
- **J+30** : [Jalons précis]
- **J+90** : [Jalons précis]
- **J+180** : [Jalons précis]
```
**Usage:** Tweets opérationnels (réforme, mobilisation)
**Exemples:** 91 (État efficace), 87 (numérique), 90 (manif)

**💡 Insight:** Ces sections transforment diagnostic en action = valeur ajoutée vs analyse pure.

---

### 5. **Formules Clôture Variées**

**✅ À GARDER — 5 variantes identifiées:**

| Émoji | Label | Usage | Exemple |
|-------|-------|-------|---------|
| 💣 | **Conclusion** | Standard | "Le peuple clique, le système engrange" |
| 🎯 | **Verdict** | Analyses factuelles/juridiques | 97 (Ernotte CNEWS) |
| ⚡ | **L'État...** | Formules choc État | 87 (numérique), 86 (manif) |
| 📌 | **Moralité** | Leçons systémiques | 91 (État efficace) |
| 🧨 | **Conclusion** | Révélations explosives | 90 (manif Rodrigues) |

**💡 Insight:** Variation émoji clôture = adaptation ton selon gravité/type investigation.

---

## 🧩 Patterns par Sujet Dominant

**Observation:** Certains sujets appellent structures spécifiques.

### **Politique/État (93, 91, 80)**
- **Type D** (note stratégique long)
- Sections multiples (I-XIII)
- Faisceau d'indices obligatoire
- Contre-arguments démontés
- Recommandations État/Citoyens/Société

### **Mobilisation/Manif (90, 89, 86, 82, 79)**
- **Type E** (pamphlet compact) OU **Type C** (déconstruction spectacle)
- Vocabulaire opérationnel: SOP-72h, État-major civil, OSINT
- Formule finale impérative courte: "La foule impressionne. L'organisation gagne."
- Focus sur lawfare + protest paradigm

### **Fact-check rapide (92, 85, 77)**
- **Type E** (pamphlet compact)
- Ultra-court (quelques paragraphes)
- Punch direct sans développement
- 1-2 émojis max

### **Système/Réseau (97, 93)**
- **Type B** (anatomie système) OU **Type D** si très complexe
- Vocabulaire: entre-soi, reproduction élitaire, pantouflage
- ICEBERG pattern systématique

### **Tech/Sécurité/Données (87, 81)**
- **Type D** (note stratégique)
- Facts techniques précis (montants, dates, volumes données)
- Recommandations stratégiques État/Citoyens
- Ton pédagogique (traduire acronymes)

---

## 🚨 Erreurs CLI vs Web

**❌ CE QUE LE CLI PRODUIT (à corriger):**

1. **Intro méthodologique** — "J'ai appliqué Truth Engine avec analyse hostile..."
2. **Numérotation académique** — "1. Premier problème" / "2. Deuxième problème"
3. **H2/H3 markdown partout** — Même pour tweets courts (Types A/B/C)
4. **Ton démonstratif** — "Il apparaît que..." / "On peut constater..."
5. **Méthodologie fin** — "Investigation: 20 recherches, 40 sources, EDI 0.65"
6. **Pas de formules choc** — Conclusions fades, pas de "claque" finale

**✅ CE QUE LE WEB PRODUIT (à reproduire):**

1. **Hook immédiat** — Citation choc OU révélation dans 2 premières phrases
2. **Titres gras inline** — `**Les faits :**` intégré dans narratif
3. **Questions rhétoriques** — "Qui pousse vraiment cet accord?"
4. **Verbes actifs** — assène, martèle, exhibe, orchestre, engrange
5. **Formules mémorables** — "Le peuple clique, le système engrange"
6. **Facts ultra-précis** — Noms complets, montants exacts, dates précises

**💡 Root Cause:** CLI applique template "rapport analytique Type D" par défaut. Il faut classifier investigation PUIS choisir type adapté.

---

## 📊 Statistiques Corpus

**26 tweets analysés (103→77):**

- **Type A** (révélation choc): 2 tweets (~8%)
- **Type B** (anatomie système): 3 tweets (~12%)
- **Type C** (déconstruction spectacle): 6 tweets (~23%)
- **Type D** (note stratégique): 9 tweets (~35%) ← **dominant**
- **Type E** (pamphlet compact): 6 tweets (~23%)

**💡 Insight:** Type D domine = sujets complexes État/système. Mais CLI abuse du Type D même pour sujets simples → erreur classification.

**Longueurs moyennes:**
- Type A/B/C: 500-1500 mots
- Type D: 2000-5000 mots (parfois 8000+)
- Type E: 150-400 mots

**Émojis titre les plus fréquents:**
- 🔴 (5x) — Actualité/urgence
- 🚨 (4x) — Révélation/alerte
- 🔍 (3x) — Enquête/anatomie
- ⚖️ (3x) — Justice/équité
- 🎭 (2x) — Spectacle/théâtre

---

## 🎯 Recommandations Prompt v2.0

**✅ CE QUI FONCTIONNE:**

1. **Typologie 5 types** claire avec critères décision
2. **Vocabulaire étendu** (118→130 concepts marqueurs)
3. **Sections optionnelles** documentées (Faisceau/Contre-arguments/Recommandations)
4. **Checklist qualité** avec anti-patterns explicites
5. **Exemples annotés** (pourquoi ça marche)

**⚠️ CE QUI RESTE À TESTER:**

1. **Classification automatique** investigation → type tweet approprié
2. **Prompt exécution** — Est-ce que v2.0 produit "panache" en CLI?
3. **Seuils longueur** — Quand Type E vs Type C vs Type D?
4. **Adaptation ton** — Pamphlétaire vs pédagogique vs opérationnel

**🔧 AMÉLIORATIONS FUTURES POSSIBLES:**

1. Ajouter **arbres décision** Type A/B/C/D/E selon investigation
2. Créer **templates remplissables** par type
3. Documenter **formules choc** réutilisables (banque de 50+)
4. Extraire **métaphores récurrentes** par domaine (État, tech, mobilisation)

---

## 📝 Points Intéressants à Creuser

**1. Progression narrative Type D (tweets longs):**
- Intro hook → Sections factuelles → Faisceau d'indices → Contre-arguments → Recommandations → Verdict
- Structure "entonnoir inversé": du factuel vers l'opérationnel

**2. Vocabulaire opérationnel mobilisation:**
- SOP-72h, État-major civil, OSINT citoyen, lawfare
- = Passage du diagnostic à l'action concrète
- Pourrait devenir section dédiée prompt (vocabulaire par domaine)

**3. Formules finales courtes ultra-percutantes:**
- "La foule impressionne. L'organisation gagne."
- "Pas des contes, des comptes. Pas des promesses, des référendums."
- "Un État se juge à la façon dont il traite ses foules."
- → Banque de formules réutilisables?

**4. Contre-arguments structure italique + gras:**
- _« Citation objection »_ **Réponse factuelle.**
- Format très efficace visuellement
- Anticipe critiques = renforce crédibilité

**5. Calendrier 30/90/180 jours:**
- Rend recommandations concrètes/vérifiables
- Jalons = accountability
- Pourrait être template réutilisable

---

## 🧪 Prochaines Étapes

**Option A — Continuer analyse tweets:**
- Analyser tweets 76→50 (20-25 tweets supplémentaires)
- Chercher patterns manquants
- Affiner typologie

**Option B — Tester prompt v2.0:**
- Prendre investigation Truth Engine récente
- Générer tweet avec prompt v2.0
- Comparer CLI output vs web output
- Itérer prompt selon résultats

**Option C — Créer templates remplissables:**
- 5 templates (un par type)
- Zones `[À REMPLIR]` clairement identifiées
- Exemples annotations

**Option D — Extraire formules choc:**
- Lire tous tweets (103→2)
- Extraire toutes formules finales mémorables
- Catégoriser par domaine (État, mobilisation, tech, etc.)
- Créer banque réutilisable

---

## ✅ À Garder Absolument

1. **Typologie 5 types** (A/B/C/D/E)
2. **Titres gras inline** (pas H2/H3 sauf Type D)
3. **Émojis fonctionnels** (pas décoratifs)
4. **Facts ultra-précis** (noms + montants + dates)
5. **Formules clôture variées** (💣🎯⚡📌🧨)
6. **Vocabulaire marqueur étendu** (130 concepts)
7. **Sections optionnelles** (Faisceau/Contre-arguments/Recommandations)
8. **Listes → ou –** (jamais •)
9. **Citations françaises** `« »`
10. **Hook immédiat** 2 premières phrases

## ❌ À Zapper Définitivement

1. Intro méthodologique longue
2. Numérotation plate sans émojis (sauf Type D avec séparateurs)
3. Méthodologie pompante fin
4. Jargon non traduit
5. Overload émojis décoratifs
6. Gras phrases entières
7. Ton analytique froid (sauf Type D pédagogique)
8. Citations anglaises `" "`
9. H2/H3 markdown partout (réserver Type D)
10. Conclusions fades sans "claque"

---

**Prêt pour suite analyse ou test prompt?**
