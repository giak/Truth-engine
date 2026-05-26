# Audit APEX — S15 : Le Verrou

**Article** : `investigations/2026-05-23_macron-systeme-complet/articles/S15_le_verrou.md`
**Protocole** : CONTROLEUR APEX v2.1
**Score** : **8,7/10 — RÉVISION MINEURE**

---

## RADAR — Scores détaillés

| Critère | Poids | Score | Note |
|---------|-------|-------|------|
| **S1 Structure** | 8% | **9,0** | Sections présentes, §6 excellent. Pas de métadonnées en tête |
| **S2 Sourcing** | 12% | **8,0** | Sources présentes pour tous les faits. Sources 5 et 20 partagent URL |
| **S3 URLs** | 12% | **8,5** | 18/20 spécifiques. Sources 5 et 20 pointent page générique Arcom |
| **S4 Ton** | 8% | **8,0** | Ton analytique correct. Quelques formulations qui présupposent |
| **S5 §6** | 12% | **10** | §6 substantiel (15+ lignes), contre-exemples concrets, nuance réelle |
| **S6 Fidélité** | 16% | **7,5** | M12 : 62% vs 44% — divergence Kantar/Reuters non documentée |
| **S7 Profondeur causale** | 7% | **9,0** | Trois verrous montrés comme mécanismes imbriqués, cercle vicieux explicite |
| **S8 Cohérence série** | 5% | **10** | S13→S14→S15→S16 confirmé, article cite explicitement la chaîne |
| **S9 Écriture** | 20% | **9,3** | Système protagoniste, démonstration traçable, catégories distinctes |
| **TOTAL** | **100%** | **8,7** | **RÉVISION MINEURE** |

---

## Findings

### F001 (Moyen) — M12 : divergence Kantar vs Reuters

**Problème** : L'article affirme « 62 % des 18-24 ans s'informent principalement par les réseaux sociaux, selon le baromètre Kantar (2024) » (ligne 61, source 20). Le FACTCHECK M12 (Reuters Institute 2025) donne 44 % pour la même assertion.

**Analyze** : Kantar 2024 (« Baromètre info jeunes » via Arcom) et Reuters Institute 2025 (Digital News Report) utilisent des méthodologies différentes :
- Kantar : mesure l'ensemble des canaux d'information utilisés par les 18-24 ans (tous les réseaux confondus)
- Reuters : mesure la *source principale* d'information (« main source of news ») tous âges confondus, avec breakdown par âge

Les 62 % (Kantar, focalisé jeunes) et 44 % (Reuters, général + 18-24 breakdown différent) ne sont pas nécessairement contradictoires mais la divergence n'est pas documentée.

**Correction M059-01** : Ajouter en note ou en incise la mention du chiffre Reuters pour clarifier : *« selon le baromètre Kantar (2024), contre 44 % selon Reuters Institute (2025). »*

---

### F002 (Moyen) — Sources 5 et 20 : URL générique Arcom

**Problème** : Sources 5 (Arcom Baromètre pluralisme) et 20 (Kantar/Arcom info jeunes) pointent toutes deux vers la même URL générique : `https://www.arcom.fr/se-documenter/etudes-et-donnees/etudes-bilans-et-rapports-de-larcom`

**Correction M059-02** : Remplacer source 5 par URL spécifique du Baromètre pluralisme 2024 si disponible. Remplacer source 20 par URL spécifique du Baromètre info jeunes Kantar 2024 si disponible. Sinon, ajouter le titre exact du document pour permettre la recherche.

---

### F003 (Basse) — HTML comments sur même ligne (×4)

**Problème** : Quatre lignes (53, 85, 132, 148) portent plusieurs commentaires HTML sur la même ligne. Règle absolue : un commentaire par ligne.

Lignes concernées :
- L53 : `<!-- ENRICHIE: ... --> <!-- THEME: ... --> <!-- CROSS-REF: ... -->`
- L85 : `<!-- ENRICHIE: ... --> <!-- THEME: ... --> <!-- CROSS-REF: ... -->`
- L132 : `<!-- ENRICHIE: ... --> <!-- THEME: ... --> <!-- CROSS-REF: ... -->`
- L148 : `<!-- ENRICHIE: ... --> <!-- THEME: ... --> <!-- CROSS-REF: ... -->`

**Correction M059-03** : Séparer chaque commentaire sur sa propre ligne.

---

### F004 (Basse) — Pas de métadonnées en tête

**Problème** : Absence de bloc métadonnées (titre formaté, date, auteur) en tête de fichier, contrairement au format attendu.

**Correction M059-04** : Ajouter un bloc de métadonnées en tête.

---

## Détail des scores

### Couche 1 — Structure (poids 8%)

| Sous-critère | Note | Commentaire |
|-------------|------|-------------|
| 1.1 Sections §0-§5 | 10/10 | §0-§5 tous présents avec ancres |
| 1.2 §6 présent et substantiel | 10/10 | 15+ lignes, contre-exemples concrets, §6 authentique |
| 1.3 Métadonnées | 6/10 | Pas de bloc métadonnées en tête |
| 1.4 Ancres inter-sections | 10/10 | Ancres H2 propres, format cohérent |

### Couche 2 — Sourcing (poids 12%)

18/20 sources ont des URLs spécifiques (sauf sources 5 et 20 → même URL générique). Chaque fait dans le texte a une source listée en §Sources.

### Couche 3 — URLs (poids 12%)

20 sources listées. 2 URLs génériques. 18 URLs spécifiques pointant vers des documents identifiés.

### Couche 4 — Fidélité (poids 16%)

| Sous-critère | Poids | Note |
|-------------|-------|------|
| 4.1 Chiffres vs FACTCHECK | 35% | 8/10 — M12 divergence |
| 4.2 Texte vs sources | 15% | 7/10 — M12 non documenté |
| 4.3 URLs valides | 30% | 8/10 — 2 URLs génériques |
| 4.4 Vérif web faits contestés | 20% | 6/10 — M12 vérifié, divergence documentable |
| 4.5 Cohérence projet | 10% | 10/10 — s'inscrit parfaitement dans la série |

### Couche 5 — Écriture (poids 20%)

| Sous-critère | Poids | Note |
|-------------|-------|------|
| 5.1 Système protagoniste | 35% | 10/10 — « génie du système est son invisibilité » |
| 5.2 Démonstration traçable | 25% | 9/10 — §1→§2→§3→§4→§5 enchaînement causal clair |
| 5.3 Respiration | 25% | 8/10 — blockquotes bien placés, paragraphes parfois denses |
| 5.4 Cohérence catégorielle | 15% | 10/10 — trois verrous distincts, pas de fausses équivalences |

---

## Vérifications

- 23 recours 49.3 → D1 ✅
- 57 % abstention → D2 ✅
- 22 % confiance politique → D4 ✅
- 90 % lois sans vote → D21 ✅
- 90 % pays en déclin → D23 ✅
- 43 % colère → D24 ✅
- 60 % théories complot → M18 ✅
- 29 % confiance médias → M10 ✅
- 9 propriétaires 90 % → M1 ✅
- Stratégie Bolloré → M2 ✅
- 35 % homme fort → Source 11 IPSOS ✅ (hors FACTCHECK mais sourcé)
- 200 journalistes → Source 18 ✅
- Budget police +50 % → Source 13 ✅
- Budget justice 0,34 % vs 0,67 % → Source 14 ✅
- 60 associations dissoutes → Source 16 ✅
- 23 éborgnés LBD → Source 12 ✅
- Convention citoyenne → D11/D12 ✅
- 120 ordonnances → Source 17 Légifrance ✅
- Baisse temps débat 40 % → Source 15 Fondapol ✅
- Chaîne série : S13→S14→S15→S16 → ✅ confirmé

---

**Score final : 8,7/10 — Quatre corrections (M059-01 à M059-04).**
