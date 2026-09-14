# SEMANTIC_DIFF, insertion du seuil français à la l. 89

Date : 13 septembre 2026. Article : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`.

| | |
| --- | --- |
| Empreinte avant | `c89be2cd239168b8097bb83fc5541211d8199fd2529ae24b42fe5ac3421d8e82` |
| Empreinte après | `42f5b3745046beb797f8246c3f60fa43d26f085bca112a6d870b7d02e7d13c09` |
| Sauvegarde avant | `/tmp/ARTICLE_V4_4_AVANT_P6.md` |
| Lignes modifiées | 1 dans le corps (l. 89), 2 ajoutées au registre ([63], [64]) |
| Mots du corps | 10 106 → **10 184** (+78) |
| Numéros de ligne | inchangés, l’insertion se fait en fin de ligne existante |

---

## D1. l. 89, phrase ajoutée en fin de paragraphe

**Avant, dernière phrase du paragraphe** : « Le cadre qui organise ce filtrage ne présume pas ce lien : le règlement européen énonce, dans ses motifs, que le contrôle d’un investisseur par un gouvernement de pays tiers, direct ou indirect, s’établit par examen, et il énumère ce qui sert à l’établir : la structure de propriété, le financement public, des montages de gouvernance comme les actions de préférence, ou d’autres dispositifs visant à influencer les décisions de gestion (règlement européen 2026/1386, considérant 30). »

**Après, phrase ajoutée** : « Le droit français chiffre l’entrée dans ce contrôle sans y mêler la qualité de l’actionnaire : l’autorisation est requise au franchissement de 25 % des droits de vote d’une entité de droit français, seuil abaissé à 10 % pour une société dont les actions sont admises aux négociations sur un marché réglementé, y compris hors de l’Union depuis le 17 août 2026 (article R. 151-2 du code monétaire et financier ; décret n° 2026-718 du 30 juillet 2026). »

## D2. Contrôle champ par champ

| Champ | État | Justification |
| --- | --- | --- |
| ACTEUR | inchangé | Aucun acteur nommé n’est ajouté. Les sujets introduits sont des textes : « le droit français », « l’autorisation », « une société ». |
| ACTION / RELATION | ajoutée, sans lien avec un acteur nommé | « le franchissement de 25 % » et « l’autorisation est requise » décrivent un seuil réglementaire, pas une conduite d’acteur. |
| QUANTITÉ | ajoutée, sourcée | 25 %, 10 %. Chiffres repris mot pour mot de l’article R. 151-2, 3° et 4°. |
| TEMPORALITÉ | ajoutée, sourcée | « depuis le 17 août 2026 », date d’entrée en vigueur portée par le décret n° 2026-718 et reproduite dans la note de Légifrance. |
| MODALITÉ | inchangée | Aucun « peut » devenu « va », aucun « suggère » devenu « démontre ». La phrase descriptive est à l’indicatif présent, comme le reste du paragraphe. |
| NÉGATION | conservée | Une négation portée : « sans y mêler la qualité de l’actionnaire ». Comptages avant et après : `\bpas\b` 108 → 108 ; négations nues (`n’est`, `n’a`, `ne sont`, `ne peut`, `ne permet`) 49 → 49. Aucune négation disparue. |
| CONDITION | aucune ajoutée | Le seuil n’est pas présenté comme une condition causale d’un effet. |
| EXCEPTION | aucune retirée | La phrase dit « y compris hors de l’Union », qui est une extension, non une exception nouvelle. L’exception de l’article 18-11 disparue en R4 n’est pas concernée. |
| CAUSALITÉ | aucune ajoutée | La phrase dit qu’une autorisation est **requise** à un seuil, ce qui est une règle de compétence, non une chaîne causale. Aucun des huit raccourcis de l. 167 à 169 n’est touché. |
| DEGRÉ DE CERTITUDE | nouveau degré, explicite et borné | Le fait est présenté comme du droit positif en vigueur à une date nommée. Il n’est pas présenté comme un effet observé. |
| ORDRE DE L’ARGUMENT | renforcé, non déplacé | La phrase suit la citation du considérant 30 et vient après « Le lien avec un État est un élément à examiner. Il ne remplace ni la preuve d’un contrôle effectif ni celle de l’usage politique de ce contrôle. » Elle illustre ce qui précède au lieu de le contredire. |

Verdict : **SAFE**, avec une précision de portée (voir D4).

## D3. Entrées de registre ajoutées

- **[63]** Article R. 151-2 du code monétaire et financier, version en vigueur depuis le 17 août 2026. Lecture sur Légifrance le 13 septembre 2026 : « 3° De franchir, directement ou indirectement, seul ou de concert, le seuil de 25 % de détention des droits de vote d’une entité de droit français ; 4° De franchir, directement ou indirectement, seul ou de concert, le seuil de 10 % de détention des droits de vote d’une société de droit français dont les actions sont admises aux négociations sur un marché réglementé. » L’entrée mentionne l’inapplicabilité aux investisseurs de l’Union et de l’Espace économique européen, portée par le dernier alinéa de l’article.
- **[64]** Décret n° 2026-718 du 30 juillet 2026, article 1, 1° : le 4° de l’article R. 151-2 est complété par la définition du marché réglementé, ce qui étend la prise en compte aux marchés situés dans un pays tiers. Entrée en vigueur au 17 août 2026.

## D4. Réserve de portée, à ne pas confondre avec une régression

La phrase ajoutée **ne restaure pas** le seuil perdu en R4. Elle ne quantifie pas un lien à un État, elle quantifie une participation. La recherche l’établit et le documente : `RECHERCHE_SEUIL_DROIT_FRANCAIS_FILTRAGE_2026-09-13.md`, section 1, résultat négatif écrit en mémoire sous `6fcac913`.

Ce qui est gagné : un chiffre daté, sourcé sur texte en vigueur, qui **montre** que le déclencheur juridique du filtrage est indifférent à la qualité étatique de l’actionnaire. C’est un appui direct pour la thèse du paragraphe, et de même objet que lui.

Ce qui reste perdu : la mention « financée pour plus de moitié ». Elle n’est pas dans l’article et il n’y a pas de pièce honnête pour la remettre à cet endroit.

## D5. HARD_GATE après insertion

Tiret cadratin U+2014 : 0. Tiret demi-cadratin U+2013 : 0. Apostrophes ASCII : 0. Guillemets : 51 ouvrants, 51 fermants. Doubles espaces : 0. `[n]` dans le corps : 0. Tableaux dans le corps : 0. Puces dans le corps : 0. Séparateurs : 7. Figures : 4, inchangées. Registre : 64 entrées, séquence continue de 1 à 64, aucun numéro ni URL en double.
