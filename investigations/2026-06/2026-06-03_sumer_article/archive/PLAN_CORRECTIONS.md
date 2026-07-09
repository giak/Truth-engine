# PLAN DE CORRECTIONS — Article Sumer (post-audit)

**Date :** 2026-06-04
**Source :** Audits `2026-06-04_19-35` et `2026-06-04_19-37`
**Cible :** `sections/1_introduction.md` à `sections/7_verdict.md`
**Statut :** ✅ EXÉCUTÉ — Toutes les corrections appliquées le 2026-06-04.

---

## 🔴 CRITIQUE 1 — Confusion transmission : philosophie islamique ≠ droit romain ✅

**Fichiers :** `3_rome_chine.md`, `4_islam_inde_ameriques.md`, `5_synthese_5000_ans.md`, `7_verdict.md`

**Problème :** L'article juxtaposait deux chaînes de transmission distinctes sans les différencier :
- Chaîne A (philosophie/science) : Aristote, Galien → Bagdad (Bayt al-Hikma, 830) → Cordoue → Tolède → Paris. L'Islam a transmis la science grecque.
- Chaîne B (droit) : *Corpus Juris Civilis* → Byzance (application continue) + *Littera Florentina* → Bologne (Irnerius, ~1070). Le droit romain n'a jamais transité par le monde islamique. La charia est un système autonome, non dérivé du droit romain.

**Correction appliquée :** Les 4 fichiers dissocient désormais explicitement les deux canaux. §3 : suppression de « Rome islamique », ajout de « Deux canaux, deux contenus : la philosophie par l'Islam, le droit par Byzance et les manuscrits italiens ». §4 : « droit romain » → « science grecque » dans la phrase sur l'Islam. §5 : paragraphe « Deux canaux distincts ont ramené le savoir antique en Europe ». §7 : même dissociation.

---

## 🔴 CRITIQUE 2 — Opposition Charpin/Hudson fabriquée ✅

**Fichiers :** `2_sumer.md`, `4_islam_inde_ameriques.md`

**Problème :** L'article affirmait que Charpin « contredit » Hudson en opposant « restauration conservatrice » à « réforme sociale progressiste ». Or Hudson lui-même qualifie l'andurarum de « conservative tradition ». Les deux historiens convergent sur la nature conservatrice. La divergence réelle porte sur la *finalité* : Hudson y voit une stratégie économique de préservation du pouvoir royal ; Charpin l'inscrit dans un rituel cosmologique de légitimation.

**Correction appliquée :** §2 : « Charpin précise la lecture de l'historien Michael Hudson. Tous deux qualifient l'andurarum de restauration conservatrice de l'ordre originel. Mais là où Hudson y voit une stratégie de préservation du pouvoir royal face aux crises d'endettement, Charpin l'inscrit dans une logique rituelle et cosmologique [...] La divergence porte sur la finalité du geste, pas sur sa nature. » §4 : aligné.

---

## 🔴 CRITIQUE 3 — Absence de David Graeber ✅

**Fichiers :** `1_introduction.md`, `4_islam_inde_ameriques.md`

**Correction appliquée :** Graeber cité avec référence bibliographique complète — *Dette : 5000 ans d'histoire* (2011) — dans §1 et §4. §1 : « David Graeber [...] avait déjà documenté les sociétés sans monnaie ni dette : les Incas, l'Inde du dharma, l'Islam du riba étaient connus de l'anthropologie. L'enquête ne partait pas de zéro : elle testait systématiquement, sur six civilisations, ce que Graeber avait esquissé, et elle y ajoutait la question qu'il n'avait pas posée : que deviennent ces mécanismes d'intégration quand une élite les capture ? »

---

## 🟠 HAUTE 4 — « Caste » comme catégorie universelle ✅

**Fichiers :** `1_introduction.md`, `5_synthese_5000_ans.md`, `6_miroir_francais.md`, `7_verdict.md`

**Décision :** « Caste » réservé à deux cas : les brahmanes (seule véritable caste au sens anthropologique : endogamie, transmission par le sang, pureté rituelle) et la France contemporaine (terme établi de la série Substack *La Caste Parasite*). Pour Sumer, Rome, Chine, Islam, Incas : « corps de spécialistes » ou « élite administrante ».

**Correction appliquée :**
- §1 sous-titre : « et que la caste a capturé » → « et que l'élite a capturé »
- §5 H3 : « Six castes de spécialistes » → « Six corps de spécialistes »
- §5 corps : ajout d'une phrase différenciant les mécanismes de reproduction (endogamie, examen biaisé, monopole cognitif, cooptation)
- §6 : « caste » pour France et brahmanes, « élite » pour les civilisations antiques
- §7 : « corps de spécialistes » pour le phénomène général, « caste » seulement pour la France

---

## 🟠 HAUTE 5 — Arthashastra « antérieure de mille ans à Rome » ✅

**Fichier :** `4_islam_inde_ameriques.md`

**Correction appliquée :** « antérieure de mille ans à Rome » → « dont la sophistication administrative n'a pas d'équivalent contemporain en Europe »

---

## 🟡 MOYENNE 6 — Redondances structurelles ✅

**Fichiers :** `2_sumer.md`, `5_synthese_5000_ans.md`, `6_miroir_francais.md`, `7_verdict.md`

**Correction appliquée :**
- Chronologie dette (andurarum → Tibère → jiaozi → QE → 3 200 Md€) : version complète conservée dans §5 uniquement. §6 : dispersée par tension. §7 : réduite à une allusion brève.
- Formule « La France a conservé le problème, elle a perdu l'intégration » : conservée dans §2 (place naturelle). §6 : variantes par tension. §5, §7 : supprimée.
- Opposition « fragmenté/intégré » : réduite de ~7 occurrences à ~4.

---

## 🟡 MOYENNE 7 — « Aucun texte sumérien n'a circulé » ✅

**Fichiers :** `1_introduction.md`, `2_sumer.md`

**Correction appliquée :** « Aucun texte sumérien n'a circulé » → « Aucun texte juridique ou administratif sumérien n'a circulé »

---

## 🟢 BASSE 8 — 43 tirets cadratins (—) ✅

**Fichiers :** Les 7 fichiers.

**Correction appliquée :** Remplacement systématique par virgules, deux-points, parenthèses ou reformulation.

**Vérification post-exécution :** `grep -c '—'` sur les 7 fichiers → **0 em-dash résiduel**.

---

## EXÉCUTION

| Étape | Fichier | Corrections | Statut |
|:-----:|---------|-------------|:------:|
| 1 | `2_sumer.md` | Charpin/Hudson + em-dashes + nuance sumérien + réduction redondance | ✅ |
| 2 | `3_rome_chine.md` | Transmission dissociée + em-dashes | ✅ |
| 3 | `4_islam_inde_ameriques.md` | Transmission + Graeber + Arthashastra + Charpin/Hudson + em-dashes | ✅ |
| 4 | `5_synthese_5000_ans.md` | Transmission dissociée + caste→corps de spécialistes + réduction chronologie + em-dashes | ✅ |
| 5 | `6_miroir_francais.md` | Caste différenciée + réduction redondance + em-dashes | ✅ |
| 6 | `7_verdict.md` | Transmission + caste + réduction redondance + em-dashes | ✅ |
| 7 | `1_introduction.md` | Graeber+biblio + sous-titre + nuance sumérien + em-dashes | ✅ |
| 8 | Revue finale | `code-reviewer-deepseek` + `grep em-dash` | ✅ |

---

## DÉCISIONS PRISES

1. **Terme « caste » :** Réservé aux brahmanes (sens anthropologique) et à la France (terme de la série Substack). Remplacé par « corps de spécialistes » ou « élite administrante » pour Sumer, Rome, Chine, Islam, Incas.
2. **Graeber :** Citation avec référence bibliographique complète intégrée dans le flux narratif (*Dette : 5000 ans d'histoire*, 2011).

## LIMITES NON TRAITÉES

- **Sources en langue originale :** 0 source en arabe, sanskrit, chinois, quechua, sumérien/akkadien. Non déclaré dans l'article (audit §3.1).
- **Biais de sélection résiduel :** Sociétés nomades (Mongols, Vikings), Afrique subsaharienne, Océanie absentes. Non déclaré (audit §3.2).
- **Répétition du chiffre 3 200 Md€ :** Apparaît encore 4 fois (§1, §2, §5, §6). Accepté comme rappel nécessaire à la lisibilité.
