# INVESTIGATION — Reconnaissance IPG exacte de CW (liste officielle CPPAP, primaire)

Date : 2026-08-14 | Heure : 10:30 CEST | Type : INVESTIGATION | Complexité : MEDIUM
Objet : vérifier en primaire la reconnaissance IPG exacte de Conspiracy Watch auprès de la CPPAP (numéro, date, qualification).
Protocole : KERNEL v2.8 — source primaire unique : liste officielle CPPAP (data.gouv.fr, Ministère de la Culture).
Suite de : `2026-08-14_10-20_cppap-ipg-aides-presse_INVESTIGATION.md` (dont je corrige deux éléments).

---

## §0 RÉSULTAT NET (deux corrections, un fait de fond)

La liste officielle de la CPPAP (data.gouv.fr, mise à jour 26/06/2026, 1 267 services de presse en ligne) contient cette ligne :

```
OBSERVATOIRE DU CONSPIRATIONNISME | Association | 75 | conspiracywatch.info | 39bisA | 0930 Z 93758
```

Deux corrections aux dossiers antérieurs et à la page de CW elle-même :

1. **Numéro CPPAP** : la page « Nos partenaires » de CW affiche « **0925 Z 93758** ». La liste officielle dit « **0930 Z 93758** ». Le numéro exact est **0930 Z 93758**.
2. **Qualification** : CW n'est **pas reconnu « IPG »** au sens plein. Sa qualification officielle est « **39bisA** » — « consacré pour une large part à l'information politique et générale » au sens de l'article 39 bis A du CGI (régime fiscal de provisions sur investissements). C'est un **échelon inférieur** à l'IPG plein (article 2 du décret 2009).

**Conséquence directe** : l'objet associatif de 2024 « service de presse en ligne d'information politique et générale » (statut IPG) **surestime** la réalité administrative. La CPPAP, seule autorité compétente, qualifie CW « 39bisA », pas « IPG ».

---

## §1 LA LISTE OFFICIELLE (primaire)

Source : data.gouv.fr, dataset « Liste des services de presse en ligne reconnus » (Ministère de la Culture / CPPAP), CSV du 26/06/2026, 1 267 services.

**Ligne CW (exacte)** :
| Champ | Valeur |
|---|---|
| Éditeur | OBSERVATOIRE DU CONSPIRATIONNISME |
| Forme juridique | Association |
| Département | 75 |
| Service | conspiracywatch.info |
| Qualification | **39bisA** |
| Numéro CPPAP | **0930 Z 93758** |

**Distribution des qualifications dans la liste** (1 267 services) :
| Qualification | Effectif | Signification |
|---|---|---|
| (vide) | 446 | simple immatriculation SPEL, sans qualification IPG |
| **IPG** | 360 | information politique et générale pleine (art. 2 décret 2009) |
| 39bisB | 278 | (autre régime fiscal) |
| **39bisA** | 180 | « consacré pour une large part à l'IPG » (art. 39 bis A CGI) |

**Position de CW dans cette échelle** :
| Service | Qualification |
|---|---|
| Mediapart | **IPG** |
| Marianne (CMI France) | **IPG** |
| Blast | **IPG** |
| **Conspiracy Watch (ODC)** | **39bisA** |
| Les Surligneurs (fact-checking juridique) | **39bisA** |

CW est donc dans le **même échelon que Les Surligneurs** (39bisA), et **un échelon sous** Mediapart/Marianne/Blast (IPG plein).

---

## §2 CE QUE « 39bisA » SIGNIFIE EXACTEMENT (source CPPAP)

La page officielle de la CPPAP distingue deux qualifications, **toutes deux éligibles au FSDP** :

1. **IPG (art. 2 du décret 2009)** : exige au moins **un journaliste professionnel** (carte de presse ou affiliation IDCC 1480), un contenu IPG « permanent et continu », actualisé au maximum hebdomadairement, dépassant significativement une catégorie restreinte de lecteurs. C'est le statut plein.

2. **39bisA (art. 39 bis A CGI)** : « consacré pour une large part à l'IPG », exigence réduite au **tiers de la surface rédactionnelle**, **pas de critère de journaliste professionnel**, lectorat restreint toléré. C'est le régime **fiscal** (provisions sur investissements), échelon inférieur.

**Implication** : CW n'a pas la qualification IPG pleine. Son « 39bisA » l'éligibilise au FSDP (ce qui explique les 6 429 € de 2021), mais n'établit pas la reconnaissance IPG que l'objet associatif de 2024 revendique.

---

## §3 LE NUMÉRO CPPAP : 0925 vs 0930 (discrepancy documentée)

| Source | Numéro | Date |
|---|---|---|
| HelloAsso (ancien) | 0920 W 93758 | antérieur |
| CW « Nos partenaires » | **0925 Z 93758** | 06/05/2026 |
| **CPPAP (liste officielle)** | **0930 Z 93758** | 26/06/2026 |

**Lecture** : trois numéros coexistent dans la trace publique (0920 W → 0925 Z → 0930 Z). La liste officielle CPPAP du 26/06/2026 fait foi : **0930 Z 93758**. La page de CW (06/05/2026) affiche un numéro **dépassé ou erroné** (0925 Z). C'est un écart factuel de plus dans la chaîne de transparence de CW — cohérent avec le pattern documenté (omission du FSDP 2021, omission CIPDR/Fonds Marianne).

**Je ne sur-interprète pas les lettres** (W/Z) : la signification des lettres dans la numérotation CPPAP n'est pas établie en primaire ici. Le fait dur est la **divergence du chiffre** (0925 vs 0930) entre la page de CW et l'état officiel.

---

## §4 CE QUE CELA CHANGE AU DOSSIER GLOBAL

**Établi (✦, primaire)** :
1. Numéro CPPAP officiel : **0930 Z 93758** (pas 0925 Z).
2. Qualification officielle : **39bisA** (pas IPG plein).
3. CW est un **service de presse en ligne reconnu au régime fiscal 39 bis A**, un échelon sous l'IPG plein.

**Corrigé (dossiers antérieurs)** :
- Dossier 07-26 : « statut IPG (2024) » déduit de l'objet JOAFE → la qualification CPPAP réelle est **39bisA**, pas IPG.
- Dossier 10-20 : « CPPAP n° 0925 Z 93758 » (repris de la page CW) → le numéro officiel est **0930 Z 93758**.

**Nuance d'honnêteté (exculpatoire)** : la qualification « 39bisA » est **légale, banale et suffisante** pour le FSDP (6 429 €, 2021) et pour le taux de TVA réduit. Le fait que CW soit « 39bisA » et non « IPG » n'est pas un scandale : c'est le statut normal d'un site spécialisé (le complotisme est une thématique spécialisée, qui ne remplit pas le critère « dépassant significativement une catégorie de lecteurs » requis pour l'IPG plein). La critique tient sur la **précision de l'auto-description** : l'objet associatif dit « information politique et générale » (IPG), la CPPAP dit « 39bisA ». C'est un **écart de formulation**, pas une fraude.

**Le fait le plus solide** : la page « Nos partenaires » de CW affiche un numéro CPPAP (0925 Z) **qui ne correspond pas** à l'état officiel (0930 Z). Même sur un élément aussi aisément vérifiable qu'un numéro d'immatriculation, la trace publique de CW est **inexacte**. C'est un indicateur de la fiabilité générale de ses déclarations de transparence.

---

## §5 SOURCES

1. Ministère de la Culture / data.gouv.fr, « Liste des services de presse en ligne reconnus » (CSV 26/06/2026, 1 267 services) — https://www.data.gouv.fr/fr/datasets/liste-des-services-de-presse-en-ligne-reconnus/
2. CPPAP, « Service de presse en ligne d'information politique et générale » (distinction IPG art. 2 décret 2009 vs 39 bis A CGI) — https://www.cppap.fr/fr/service-de-presse-en-ligne-dinformation-politique-et-generale
3. CPPAP, « FAQ Presse en ligne » — https://www.cppap.fr/fr/services-de-presse-en-ligne/faq-presse-en-ligne
4. CW, « Nos partenaires » (06/05/2026) — https://www.conspiracywatch.info/nos-partenaires
5. HelloAsso, ODC (ancien n° 0920 W 93758) — https://www.helloasso.com/associations/observatoire-du-conspirationnisme
6. JOAFE modification 07/05/2024 (objet « information politique et générale ») — dossier 07-26
