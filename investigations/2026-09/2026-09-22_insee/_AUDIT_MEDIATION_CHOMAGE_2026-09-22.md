# AUDIT DE MÉDIATION — Le chômage dans la presse : IC et alternatives au test
**Date** : 2026-09-22 · **Protocole** : KERNEL v2.10.6 + RENARD CORE V3 · **Question** : combien de titres/articles médiatisent le chômage avec son intervalle de confiance (±0,3 pt) et ses alternatives (halo, cat A) ?

---

## 1. Protocole

- **Corpus nominal** : 20 articles de presse francophones, 2025-2026, évoquant le chômage France (BIT ou inscrits France Travail), tous **réellement fetchés** (HTTP 200 + texte lu). Un même titre limité à 5 occurrences (poids AFP). Salves de recherche neutres (« chômage France Insee/France Travail 2025 2026 ») + 1 salve à ancrages méthodologiques (BIT/halo) dont l'effet de sélection est suivi séparément.
- **Unité de mesure** : article. Le titre seul ne suffit jamais à scorer un critère ; seuls les articles lisibles en corps sont scorés pleins. 2 articles partiels (extraction tronquée) sont scorés sur titre+description et comptés avec flag.
- **Grille binaire (0/1) par article** :
  - **C1 — IC** : marge d'échantillonnage / intervalle de confiance / « ±0,3 pt » / fourchette explicitement associée au taux BIT.
  - **C2 — Étalon BIT** : « au sens du BIT » / « Bureau international du travail » nommé (définition BIT = la convention, pas une évidence).
  - **C3 — Alternatives nommées+chiffrées** : catégorie A France Travail OU halo du chômage, nommés et chiffrés pour la même période.
  - **C4 — Sensibilité conventionnelle** : effets de réforme quantifiés, données « corrigées », alerte Dares/ASP (labellisation suspendue), chiffrage contrefactuel (« si on enlevait… »).
- **Score composite** = moyenne des 4 critères. La médiatisation « complète » attendue d'un chiffre d'estimation = 4/4.

## 2. Corpus et déroulé de collecte

**33 URLs tentées** → 19 articles de presse pleins lisibles + 2 partiels = **corpus nominal de 20** ; 9 substitués/inaccessibles ; 3 sources pédagogiques hors presse (indicatives).

| Statut | Médias | Détail |
|---|---|---|
| Pleins (19) | Le Figaro ×5, Le Parisien, 20 Minutes ×2, Capital, TF1 Info, franceinfo, l'Opinion, France 24 (AFP), Mémento (AFP), RMC/BFM, Sud Ouest, La Dépêche ×2, Alternatives Éco | 2025-11 → 2026-09 |
| Partiels (2) | La Tribune, Public Sénat | extraction tronquée, score plancher |
| Inaccessibles (9) | Libération ×2, Ouest-France ×3, Le Monde ×2, Les Échos ×2 | 403 / anti-bot — **non testés**, biais assumé |
| Hors presse (3) | Observatoire des inégalités, La finance pour tous, Club Patrimoine | indicatifs, non comptés |

Fenêtre couverte : T3 2025 (7,7 %), T4 2025 (7,9 %), T1 2026 (8,1 %), T2 2026 (8,3 %) + prévision 8,6 % + quatre publications Dares (cat A).

## 3. Résultats — grille complète (19 articles pleins)

| # | Article (média, date) | Chiffre-titre | C1 IC | C2 BIT | C3 alt. | C4 conv. | Score |
|---|---|---|---|---|---|---|---|
| 1 | Figaro 10/02/2026 | 7,9 % T4 | 0 | 1 | 0 | 1 | 2/4 |
| 2 | Figaro 07/08/2026 | 8,3 % T2 | 0 | 1 | 1 (halo 1,9 M) | 1 | 3/4 |
| 3 | Figaro infographie 13/05 | 8,3 % T2 | 0 | 1 | 0 | 0 | 1/4 |
| 4 | Figaro 13/11/2025 | 7,7 % T3 | 0 | 1 | 0 | 0 | 1/4 |
| 5 | Figaro 10/09/2026 (prévision) | 8,6 % fin 2026 | 0 | 0 | 0 | 0 | 0/4 |
| 6 | Parisien 10/02/2026 | 7,9 % T4 | 0 | 1 | 0 | 1 | 2/4 |
| 7 | 20 Minutes 07/08/2026 | 8,3 % T2 | 0 | 1 | 1 (halo 1,9 M) | 1 | 3/4 |
| 8 | 20 Minutes 10/02/2026 | 7,9 % T4 | 0 | 1 | 0 | 1 | 2/4 |
| 9 | Capital 28/04/2026 | cat A −1,2 % | 0 | 0 | 1 (cat A 3,29 M) | 1 | 2/4 |
| 10 | TF1 Info 07/08/2026 | 8,3 % T2 | 0 | 1 | 1 (halo 1,9 M **et** cat A 3,32 M) | 0 | 2/4 |
| 11 | l'Opinion 09/08/2026 | 8,3 % T2 | 0 | 1 | 0 | 0 | 1/4 |
| 12 | franceinfo 07/08/2026 | 8,3 % T2 | 0 | 0 | 0 | 1 (contrefactuel ministre −0,4 pt) | 1/4 |
| 13 | France 24/AFP 28/04/2026 | cat A −1,2 % | 0 | 1 | 1 (cat A 3,29 M) | 1 | 3/4 |
| 14 | Mémento/AFP 07/08/2026 | 8,3 % T2 | 0 | 1 | 1 (halo 1,9 M) | 1 | 3/4 |
| 15 | RMC/BFM 29/04/2026 | cat A −2,4 % | 0 | 0 | 1 (cat A) | 1 | 2/4 |
| 16 | Sud Ouest 28/07/2026 | cat A +0,8 % | 0 | 1 | 1 (cat A 3,32 M) | 1 (**ASP : labellisation suspendue**) | 3/4 |
| 17 | La Dépêche 28/07/2026 | cat A +0,8 % | 0 | 0 | 1 (cat A 3,32 M) | 1 | 2/4 |
| 18 | La Dépêche 29/01/2026 | cat A +6,8 %/an | 0 | 0 | 1 (cat A 3,35 M) | 1 | 2/4 |
| 19 | Alternatives Éco 20/05/2026 | 8,1 % T1 | 0 | 1 | 0 | 0 | 1/4 |

**Partiels (flag plancher)** : La Tribune 29/01 (cat A au titre+DFS : 1/4) · Public Sénat 29/01 (« changements de règles » en DFS : 1/4).

## 4. Agrégats

| Critère | Corpus plein (n=19) | + partiels (n=21) |
|---|---|---|
| **C1 — IC / marge d'échantillonnage** | **0/19 — 0 %** | 0/21 — 0 % |
| C2 — BIT nommé | 13/19 — 68,4 % | 13/21 — 61,9 % |
| C3 — cat A ou halo nommés+chiffrés | 10/19 — 52,6 % | 11/21 — 52,4 % |
| C4 — sensibilité conventionnelle | 13/19 — 68,4 % | 14/21 — 66,7 % |
| **Composite** | **36/76 = 47,4 %** | 38/84 = 45,2 % |

Distribution des scores : 3/4 → 5 articles ; 2/4 → 8 ; 1/4 → 5 ; 0/4 → 1. **Aucun article à 4/4.**

Hors presse (indicatif, 3) : Observatoire des inégalités 3/4 (halo 1,95 M + « ce chiffre reflète mal l'état du marché du travail »), Club Patrimoine 3/4 (BIT + halo + corrections), La finance pour tous 2/4 (contraste BIT/Dares pédagogique). Le secteur pédagogique/advocacy fait mieux que l'info sur C3-C4.

## 5. Analyse — cinq résultats

**R1. L'IC est à 0 % du corpus.** Aucun des 19 articles — y compris les 5 meilleurs — ne mentionne la marge d'échantillonnage du taux BIT (±0,3 pt, Sénat 2016) ni une quelconque fourchette. Un chiffre présenté en général au dixième de point (« +0,1 pt », « 7,7 % ») sans son incertitude, alors que la moitié des mouvements publiés (0,1-0,2 pt) sont inférieurs ou de l'ordre de la marge. Caveat : extractions tronquées à ~6 000 caractères ; mais l'IC n'apparaît pas davantage dans les communiqués Insee que relaie la presse, donc le risque de faux négatif est faible.

**R2. L'effet AFP : la diversité apparente est une source unique.** Les 4 articles « halo » (Figaro, 20 Minutes, Mémento, TF1) reproduisent quasi verbatim le même paragraphe (« Aux 2,7 millions… s'ajoutent 1,9 million… C'est ce que l'on appelle « le halo autour du chômage » ») — une dépêche AFP adossée au communiqué Insee d'août 2026. Le 10/19 de C3 se décompose en ~5-6 rédactions effectivement productrices (récits Dares du ministère : Capital, RMC, Sud Ouest, La Dépêche ×2) et un recyclage à 4 exemplaires. La couverture des « alternatives » n'est pas un choix rédactionnel distributed : c'est l'agenda des communiqués (Insee en février/août, Dares en janvier/avril/juillet) mécaniquement suivi. Seul TF1 met BIT+halo+cat A dans le même article.

**R3. Les conventions sont documentées en corps, jamais en titre.** C2=68 % et C4=68 % : la presse reprend systématiquement les « données corrigées » Dares (2,6 %→2,0 % ; 6,8 %→1,7 % ; 0,8 %→−0,2 %) et explique sanctions/inscription automatique RSA. Mais l'audit des titres : 0/21 titres mentionne une incertitude ; les titres alternatifs (« inscrits à France Travail ») concernent les seules histoires cat A. La convention fonctionne comme disclaimer d'expert, pas comme information de tête.

**R4. Le chiffrage contrefactuel vient du politique, pas du journaliste.** La seule décomposition « si on enlevait les nouveaux publics : 8,3 %→7,9 % » est prononcée par le ministre Farandou (franceinfo) ; l'Insee donne la version qualitative (« près de la moitié de la hausse ») que la presse recopie. La presse relaie la qualification quand elle est fournie toute faite ; elle n'en produit pas elle-même.

**R5. Perle critique : la labellisation suspendue.** Sud Ouest (28/07/2026) mentionne que l'Autorité de la statistique publique **suspend depuis le 1ᵉʳ janvier 2025 la labellisation des séries demandeurs d'emploi** — information unique du corpus, reléguée en corps d'article, pendant que tous les titres « inscrits » continuent de sortir sans caveat en une. Le chiffre non labellisé fait la une ; sa non-labellisation fait un paragraphe.

## 6. Biais de mesure (honnêteté)

1. **Substitution paywall/anti-bot (9 articles)** : Libération, Ouest-France, Le Monde, Les Échos non testés. Contre-factuel extrême : si les 9 testés remplaçants avaient tous scoré 4/4, le composite monterait à 56,5 % — **le résultat R1 (IC = 0) resterait vrai pour le corpus lisible ; la généralisation à toute la presse reste plausible mais non testée** (aucun cas connu de marge d'erreur au titre du chômage).
2. **Sélection SEO autour des pics de publication** : sous-représentation des dossiers de fond (définitions, halo) hors jours de communiqué — biais contre C3-C4, donc contre le résultat favorable à la presse.
3. **Extraction partielle** (La Tribune, Public Sénat) : scores plancher ; leur réintégration change l'agrégat de <2 pts.
4. **Une salve de recherche à ancrages méthodologiques** (BIT/halo) : son produit (Alternatives Éco, sources pédagogiques) est traçable et n'inflate pas les agrégats presse (1 article/19).
5. **Portion lisible ~6 000 caractères** : un halo très tardif dans l'article peut être coupé — même sens de biais (2).

## 7. Verdict et ledger

**Réponse** : sur 20 articles de presse (2025-2026), **0 médiatise l'intervalle de confiance** du taux de chômage ; 10/19 nomment et chiffrent au moins une alternative (cat A ou halo), mais ~4 sur un recyclage AFP unique ; 13/19 qualifient les conventions en corps d'article, 0 en titre. Score composite moyen 47 %, aucun article « complet » (4/4). La mediation du chômage est **convention-docile** (suit les communiqués, documente les corrections quand la Dares les fournit) et **précision-aveugle** (l'incertitude statistique n'existe pas dans le corpus).

Ledger : verified 4 (grille appliquée sur textes réellement lus ; IC=0/19 ; agrégats arithmétiques ; effet AFP vérifié par recouvrement verbatim) · supported 2 (généralisation presse FR ; agenda communiqués→cadrage) · open 2 (corpus paywalled non testé ; dossiers de fond hors pics) · refuted 0 · CALIBRATION 4/4 = 1,0 sur le corpus, 0,5 sur la généralisation — le seul point fragile est explicitement hors de portée de ce protocole.

Contre-factuel : si les 4 articles AFP n'avaient pas recyclé le paragraphe halo, C3 tomberait à 6/19 (31,6 %) — la « diversité des alternatives » dans la presse française dépend d'une seule dépêche par publication Insee.
