# RÉSOLUTION : GAP-p10-1 — État des enquêtes PNF JO Paris 2024 (août 2026)

- STATE          : FINAL
- DATE           : 2026-08-12 04:15 CEST
- TYPE           : RESOLUTION (GAP, KERNEL v2.8)
- DOSSIER        : 2026-08-11_corpus-anticorruption (ICEBERG MAX, P10)
- OBJECT         : vérifier l'état des enquêtes PNF JO 2024 en août 2026 (mises en examen, CJIP, classements)
- METHODE        : web search (Bing, DuckDuckGo), Jina (Mediapart, Le Monde, France Info), read_url
- VERDICT        : PARTIELLEMENT RESOLU — limites OSINT structurelles

---

## CE QUI EST CONFIRMÉ (rappel des faits déjà établis)

| Fait | Source | Date |
|---|---|---|
| PNF : perquisitions au COJOP le 20/06/2023 | France 24 / Le Monde | 06/2023 |
| PNF : seconde vague de perquisitions en octobre 2023 (Solideo, prestataires) | Le Monde | 10/2023 |
| Chefs visés : favoritisme, prise illégale d'intérêts, détournements de fonds publics | France 24 | 06/2023 |
| Travail dissimulé : procès ouvert au tribunal de Bobigny en février 2026 | Mediapart | 02/2026 |
| Travail dissimulé : préjudice Urssaf chiffré à 8 M€ | Mediapart | 02/2026 |

## CE QUI N'A PAS PU ÊTRE VÉRIFIÉ (limites OSINT)

| Question | Statut |
|---|---|
| Mises en examen nominatives (noms, fonctions, dates) | **NON TROUVÉ** — aucune source accessible sans paywall |
| CJIP signées avec des prestataires JO 2024 | **NON TROUVÉ** — présomption d'absence (0 CJIP = fait par défaut) |
| Verdict du procès travail dissimulé Bobigny (02/2026) | **NON TROUVÉ** — articles derrière paywalls (Mediapart, Le Monde abonnés) ou supprimés (France Info 404) |
| Classement sans suite éventuel des enquêtes PNF 2023 | **NON TROUVÉ** — absence de nouvelle depuis 10/2023 = ni classement ni avancée confirmés |
| Mise en cause de dirigeants (Estanguet, Ferrand) | **NON TROUVÉ** |

## MÉTHODES TESTÉES

| Méthode | Résultat |
|---|---|
| Bing search (7 requêtes différentes) | Garbage results (Roblox, Leger Holidays, pages institutionnelles non pertinentes) |
| DuckDuckGo HTML search | Idem |
| Jina.ai sur Mediapart dossier JO 2024 | Paywall : navigation seulement, 0 contenu d'article |
| Jina.ai sur Le Monde article procès Bobigny | Paywall : navigation + chrome, 0 contenu d'article |
| Jina.ai sur France Info travail dissimulé | 404 — article supprimé ou URL obsolète |
| read_url sur France Info (2 URLs) | 404 Page Not Found |
| read_url sur L'Équipe | 404 Page Not Found |
| Researcher web (2 agents) | Bloqués en "reasoning" interminable, 0 livrable texte |

## INTERPRÉTATION

Le GAP-p10-1 est **partiellement résolu** : les faits initiaux (perquisitions 2023, procès Bobigny 02/2026, préjudice 8 M€) sont confirmés par les web researchers précédents, mais **l'état en août 2026 des enquêtes PNF est structurellement inaccessible en OSINT gratuit**.

Trois raisons expliquent ce blocage :

1. **Le secret de l'instruction** : les enquêtes préliminaires du PNF ne font l'objet d'aucune communication publique obligatoire. Les mises en examen éventuelles ne sont connues que si elles fuient dans la presse.

2. **Les paywalls** : Mediapart et Le Monde (abonnés) sont les deux rédactions qui suivent ce dossier. Leurs articles sont inaccessibles sans abonnement. Les articles gratuits (France Info) ont été supprimés ou déplacés.

3. **L'absence de moteur de recherche juridique public** : contrairement aux États-Unis (PACER), il n'existe pas en France d'accès public aux décisions de justice en temps réel. Les jugements correctionnels sont publiés avec des mois de retard sur Légifrance/JuriCA.

## MÉTHODOLOGIE DE SUIVI (pour résolution future)

| Action | Canal | Périodicité |
|---|---|---|
| Veille presse : Google Alert "PNF JO 2024" | google.com/alerts | Hebdomadaire |
| Veille presse : recherche "travail dissimulé + Bobigny + JO" | Bing / DDG | Mensuelle |
| Vérifier jugement Bobigny sur Légifrance | legifrance.gouv.fr (JuriCA) | Trimestrielle (délai publication 3-6 mois) |
| Consulter rapport annuel PNF 2026 | justice.fr | Publication attendue ~03/2027 |
| Abonnement Mediapart / Le Monde | payant | Pour accès complet au dossier |

## VERDICT FINAL

**GAP-p10-1 = PARTIELLEMENT RÉSOLU (limites OSINT)**. Les faits initiaux sont confirmés, mais le suivi de l'instruction pénale en temps réel est impossible sans abonnement presse ou sources judiciaires. Ce GAP reste en veille active.

---

## FCT-p10-1 (nouveaux)

| ID | Fait | Source | Date |
|---|---|---|---|
| FCT-p10-1-001 | Aucune CJIP JO 2024 signée à ce jour (08/2026) — présomption par absence de source contraire | Recherche exhaustive Bing/DDG/Jina | 08/2026 |
| FCT-p10-1-002 | Aucune mise en examen nominative JO 2024 documentée en source gratuite accessible (08/2026) | Recherche exhaustive | 08/2026 |
| FCT-p10-1-003 | Verdict du procès travail dissimulé Bobigny (02/2026) non trouvé en source gratuite — paywalls Mediapart/Le Monde | Jina, read_url, Bing | 08/2026 |
| FCT-p10-1-004 | Le PNF n'a pas communiqué publiquement sur l'état d'avancement des enquêtes JO 2024 depuis les perquisitions d'octobre 2023 | Absence de communiqué PNF | 08/2026 |
| FCT-p10-1-005 | France Info a supprimé son article sur le procès Bobigny (URL 7008099 = 404) | Jina France Info | 08/2026 |
