---
project: article-pouvoir-sans-commande
artifact_type: forensic_investigation
subject: revolving-door-bailey
as_of: 2026-09-13
status: AUDITOR_ADDED_NON_CERTIFIE
provenance: "Produit par l'auditeur pour combler l'absence de dossier INV-### derrière le paragraphe Hugh Bailey de la cible V4.4. N'appartient pas au pipeline certifié du bundle et n'a fait l'objet d'aucun gate."
epistemic_rule: "chronologie != causalité ; soupçon rapporté != fait établi ; nomination ultérieure != récompense ; procédure distincte != procédure de la cession"
zero_em_dash: false
zero_em_dash_note: "Fiche interne : le tiret cadratin est toléré dans les investigations, comme dans le dossier Alstom voisin, et interdit dans les articles publiés."
---

# Investigation forensique — porte tournante Hugh Bailey

## Pourquoi ce dossier existe

L'audit adversarial de la cible `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md` a établi que le paragraphe consacré à Hugh Bailey était la **seule affirmation nominative de l'article sans dossier d'investigation** : vérifié par recherche exhaustive, « Hugh », « Bailey », « GE France », « porte tournante » et « revolving » n'apparaissaient **aucune fois** dans les 113 dossiers du corpus.

Le paragraphe était donc adossé à de la presse, alors que tout le reste de l'article s'appuie sur le corpus. Ce dossier comble cet écart.

**Avertissement de statut.** Ce dossier est produit par l'auditeur, **après** l'audit, à partir de sources publiques. Il ne fait pas partie du pipeline certifié, n'a pas franchi de gate, et son entrée en vigueur comme pièce du corpus est une décision de l'auteur, pas un constat.

## Question

La chronologie professionnelle de Hugh Bailey, ancien conseiller au cabinet du ministre de l'Économie puis dirigeant de General Electric France, permet-elle d'établir une porte tournante, c'est-à-dire un échange entre une décision publique favorable à General Electric et un emploi futur ?

## Verdict exécutif

**La chronologie est établie. L'échange ne l'est pas.**

- `conseiller au cabinet du ministre de l'Économie, 2013-2016` puis `intégration du groupe GE, novembre 2017` = **ÉTABLI**.
- `intégration du groupe GE` puis `direction générale de GE France, avril 2019` = **ÉTABLI**.
- `décision publique favorable à GE prise en échange d'un emploi futur` = **NON ÉTABLI**. Aucune pièce publique identifiée ne ferme cette arête.
- `soupçon d'avoir aidé l'entreprise pendant ses fonctions` = **soupçon rapporté par la presse**, non une qualification.
- `procédure judiciaire distincte de celle portant sur la cession` = **rapportée**, statut actuel non vérifié.

L'article écrit exactement cela, et il a donc raison de refuser le saut causal. Ce que le dossier ajoute, c'est que le paragraphe est **sourcé** et que deux éléments publics ne sont pas repris par l'article (voir section 6).

## 1. Chronologie établie

| Date | Fait | Statut |
|---|---|---|
| 2004-2017 | Fonctions dans l'administration, notamment à la Direction générale de l'armement et à la direction générale du Trésor. | ÉTABLI (AFP) |
| 2013-2016 | Conseiller, au cabinet du ministre de l'Économie, sur les affaires industrielles et le financement à l'export. | ÉTABLI (AFP) |
| Novembre 2017 | Intègre le groupe General Electric comme directeur des affaires publiques de GE France. | ÉTABLI (AFP) |
| 22 avril 2019 | Nommé directeur général de la branche française de GE, succédant à Corinne de Bilbao. | ÉTABLI (AFP) |
| 10 septembre 2019 | Presse : il est visé par une enquête pour « prise illégale d'intérêt » liée à ses fonctions antérieures. | RAPPORTÉ |
| 3 mars 2026 | *Le Monde* : il fait l'objet d'« une autre information judiciaire du parquet de Paris », distincte de celle portant sur la cession, Anticor y étant partie civile. | RAPPORTÉ, selon les recoupements du journal |

**Point de chronologie à ne pas perdre.** Emmanuel Macron est ministre de l'Économie du 26 août 2014 au 30 août 2016. Sur la plage 2013-2016, Bailey n'a donc pas servi sous Macron pendant toute la période. Toute formulation qui attribuerait l'ensemble de la plage à M. Macron serait fausse. La cible écrit « entre 2013 et 2016 [...] au cabinet du ministre de l'Économie », ce qui est correct.

## 2. Registre causal certifié de ce dossier

- `conseiller au cabinet du ministre de l'Économie -> intégration du groupe GE` = **SUPPORTED** (fait de carrière documenté).
- `intégration du groupe GE -> direction générale de GE France` = **SUPPORTED** (fait de carrière documenté).
- `fonctions publiques -> soupçon d'avoir aidé l'entreprise` = **REPORTED_SUSPICION**, non qualifiée.
- `fonctions publiques -> décision favorable à GE en échange de l'emploi` = **NOT_ESTABLISHED / CAUSALITY_GAP**.
- `nomination chez GE -> récompense d'un service rendu` = **NOT_ESTABLISHED / REWARD_GAP**.
- `procédure du parquet de Paris -> lien avec la cession Énergie` = **NOT_ESTABLISHED / PROCEDURE_SEPARATION** (le journal distingue lui-même les deux procédures).

## 3. Gardes

`chronologie != causalité` ; `soupçon publié != qualification` ; `nomination ultérieure != récompense` ; `procédure distincte != procédure de la cession` ; `recoupements de presse != pièce` ; `reconnaissance du fait de carrière != reconnaissance du conflit`.

## 4. Sources et niveau de vérification

| Source | Contenu | Niveau |
|---|---|---|
| AFP, 11 avril 2019, « Un nouveau directeur général chez General Electric France » (reprise Connaissance des Énergies) | Intégration du groupe en novembre 2017, fonction de directeur des affaires publiques de GE France, nomination à compter du 22 avril 2019, fonctions de conseiller 2013-2016, parcours administratif | **Lu intégralement** |
| *Le Monde*, 3 mars 2026 | Mention explicite de Hugh Bailey ; « soupçonné d'avoir aidé l'entreprise lorsqu'il était encore conseiller à Bercy » ; « une autre information judiciaire du parquet de Paris » | **Extraits indexés et concordants**, article non accessible (anti-robot) |
| *Libération*, 11 avril 2019 | Nomination et passage au cabinet | **Non lu**, titre et extrait indexés |
| *Le Figaro*, 4 juin 2019 | Nomination au 22 avril, fonctions au cabinet | **Non lu**, extrait indexé |
| 20minutes, 10 septembre 2019 | Enquête pour « prise illégale d'intérêt » | **Non lu**, titre et extrait indexés |

## 5. Limites, et ce que ce dossier n'établit pas

1. **Aucune source primaire.** Aucun document judiciaire, aucun procès-verbal, aucune décision. Tout repose sur de la presse.
2. **Le statut actuel des procédures est inconnu.** Ni l'enquête signalée en 2019, ni l'information judiciaire mentionnée en 2026 n'ont pu être vérifiées à la source.
3. **Le fait de carrière repose sur une dépêche AFP lue intégralement**, complétée par des extraits de presse concordants. C'est solide pour de la presse, ce n'est pas du niveau d'un registre.
4. **Rien n'est établi sur le fond.** Ce dossier ne dit ni qu'une décision a été achetée, ni qu'elle ne l'a pas été. Il dit que la chronologie est réelle et que le lien causal est ouvert.
5. **Ce dossier n'a pas été contradictoirement instruit.** Il a été produit par l'auditeur, contre son propre intérêt de démonstration : combler un écart qu'il avait lui-même signalé.

## 6. Deux éléments publics que l'article ne reprend pas

Ces deux points ne sont pas des défauts : ce sont des choix de périmètre sur une personne nommée. Ils sont consignés ici pour que la décision soit documentée.

1. **L'enquête signalée en 2019** pour « prise illégale d'intérêt » visant Hugh Bailey, liée à ses fonctions antérieures. Rapportée par la presse, statut non vérifié depuis.
2. **L'information judiciaire distincte** mentionnée par *Le Monde* en 2026, que l'article cite déjà par ailleurs comme source [57]. Le journal précise lui-même qu'elle est **autre** que celle portant sur la cession. L'article ne mentionne ni l'une ni l'autre.

Intégrer le second point demanderait une phrase, et rendrait l'article **plus** conforme à sa propre méthode, qui est de distinguer les procédures. Ne pas l'intégrer est défendable et reste un choix éditorial.
