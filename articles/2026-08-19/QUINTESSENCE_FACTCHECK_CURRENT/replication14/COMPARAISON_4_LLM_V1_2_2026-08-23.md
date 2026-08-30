# Comparaison inter-LLM — 4 modèles — V5.1-FROZEN + validateur v1.2

## Résumé

| Modèle | VALID | PROTOCOL_INVALID | Warnings |
|---|---:|---:|---:|
| Kilo | 39/41 | 2 | 12 |
| GLM-5.2 | 40/41 | 1 | 13 |
| GPT-5.6 Luna | 40/41 | 1 | 2 |
| DeepSeek V4 Flash | 40/41 | 1 | 4 |

- Atomes VALID dans les quatre runs : **39/41**.
- Réponse brute identique sur ces atomes : **24/39**.
- Atomes disposant d’au moins une réponse valide et déterminée : **40/41**.
- **Conflits substantiels entre réponses valides et déterminées : 0.**

## Niveaux de consensus

- **Tier A — 4/4 déterminés et concordants : 24 atomes.**
- **Tier B — 3/4 déterminés et concordants : 15 atomes.**
- Tier C — 2/4 : 0.
- Tier D — 1/4 : 1.
- Sans réponse valide déterminée : 1.
- Conflit substantiel : 0.

### Tier A — 4/4

C01-A, C01-B, C03-C, C04-A, C04-B, C05-B, C05-C, C06-C, C07-C, C08-A, C08-B, C08-C, C08-D, C09-D, C10-B, C11-A, C11-B, C12-A, C12-B, C12-C, C12-D, C13-A, C13-B, C13-C

### Tier B — 3/4

C02-A, C02-B, C05-A, C06-A, C06-B, C07-A, C07-B, C09-A, C09-B, C09-C, C10-A, C14-A, C14-B, C14-C, C14-D

Dans ces 15 atomes, **Kilo + GLM + DeepSeek convergent**, tandis que GPT-5.6 Luna renvoie `UNREADABLE` ou `UNCERTAIN` pour des raisons d’accès documentaire.

### Tier D — 1/4

C03-B

- `C03-B` : DeepSeek ouvre la correction NEJM via archive et répond `YES`; GLM et GPT la déclarent `UNREADABLE`; la réponse `YES` de Kilo est invalidée par le protocole.

### Sans réponse valide déterminée

C03-A

- `C03-A` : les quatre runs sont `PROTOCOL_INVALID` car la source gelée `S_C03_NEJM` n’a pas été ouverte conformément au `REQUIRED`.

## DeepSeek V4 Flash

- **40/41 VALID**, 1 `PROTOCOL_INVALID`, 4 warnings.
- Seul `C03-A` est invalide : `S_C03_NEJM` n’est pas ouverte alors qu’elle est `REQUIRED`.
- DeepSeek emploie des accès alternatifs au **même document** (`web.archive.org`, `r.jina.ai`) lorsque l’URL canonique bloque. Cela améliore la couverture documentaire mais doit être distingué du contenu source lui-même.
- Sur les 39 atomes valides en commun avec Kilo : **39/39 réponses identiques**.
- Sur les 40 atomes valides en commun avec GLM : **39/40 identiques**; l’unique écart est `C03-B`, résolu par DeepSeek via archive et `UNREADABLE` chez GLM.
- Sur les 40 atomes valides en commun avec GPT : **24/40 réponses brutes identiques**; les écarts sont des `UNREADABLE/UNCERTAIN` GPT, pas des réponses factuelles opposées.

## Point de vigilance documentaire

- `C03-B` : DeepSeek renseigne `FIRST_PUBLIC_DATE: 2021-10-14` pour la correction NEJM. Le protocole exige la **première disponibilité publique** ; cette métadonnée doit être revue séparément, car elle n’affecte pas ici le verdict TEXT mais compte pour la qualité temporelle.
- Les proxies/archives ne doivent jamais changer l’identité de la source : il faut distinguer à l’avenir **source canonique** et **URL d’accès** dans l’analyse externe, sans modifier `V5.1-FROZEN`.

## Conclusion méthodologique

- `V5.1-FROZEN` reste inchangé.
- Le validateur v1.2 reste inchangé.
- **Aucune contradiction substantielle entre réponses valides et déterminées sur les quatre runs.**
- Les différences restantes sont principalement des différences d’accès documentaire ou de conformité au protocole.

