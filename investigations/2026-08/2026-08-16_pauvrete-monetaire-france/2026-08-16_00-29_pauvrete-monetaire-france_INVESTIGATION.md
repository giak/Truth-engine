# INVESTIGATION — Pauvreté monétaire en France (2023/2024) : run d'observation de la discipline

Date : 2026-08-16 | Heure : 00:29 CEST | Type : INVESTIGATION | Sujet : pauvrete-monetaire-france
Complexité : MEDIUM (bornée, 1 indicateur + ses millésimes)

## §0 OBJET ET MÉTHODE

Objet unique : observer, sur un sujet réel, si le pipeline force le **fetch primaire** et les
**≥2 familles de provenance** avant d'attribuer `✦`, et comment l'échelle L0→L4 se comporte
face à un indicateur statistique officiel.

Fait central choisi : le taux de pauvreté monétaire en France (seuil à 60 % du niveau de vie
médian). Deux millésimes en circulation (2023 et 2024), trois familles de provenance testées
(A institutionnel, D observatoire, C média). Règle zéro appliquée : chaque FCT-### provient
d'un `@FETCH` effectif produisant un EXCERPT_OK, jamais du rappel paramétrique.

## §1 FAITS VÉRIFIÉS (FCT-###)

Source primaire A : INSEE Première n°2063, « Niveau de vie et pauvreté en 2023 »,
Christelle Rieg, Arnaud Rousset (Insee), paru le 07/07/2025.
URL : https://www.insee.fr/fr/statistiques/8600989 — fetché (HTTP 200).

- **FCT-001** (EPI=FACT, famille A) : taux de pauvreté monétaire 2023 = **15,4 %** en France
  métropolitaine, au plus haut depuis 1996.
  EXCERPT_OK : « Le taux de pauvreté monétaire, c'est-à-dire la part de personnes pauvres dans
  la population, s'établit en 2023 à 15,4 % en France métropolitaine. […] est au plus haut depuis
  1996, date de début de la série. »

- **FCT-002** (EPI=FACT, famille A) : seuil de pauvreté à 60 % = **1 288 €/mois/UC** en 2023.
  EXCERPT_OK : « En 2023, le seuil de pauvreté monétaire, fixé à 60 % du niveau de vie médian,
  s'établit à 1 288 euros par mois et par unité de consommation. »

- **FCT-003** (EPI=FACT, famille A) : **9,8 millions** de personnes pauvres (France métropolitaine,
  logement ordinaire), soit ≈ 650 000 de plus qu'en 2022.
  EXCERPT_OK : « En 2023, 9,8 millions de personnes résidant dans un logement ordinaire en France
  métropolitaine vivent en dessous de ce seuil, soit environ 650 000 personnes de plus qu'en 2022. »

- **FCT-005** (EPI=FACT, famille A) : niveau de vie annuel médian 2023 = **25 760 €/UC**
  (= 2 150 €/mois pour une personne seule).
  EXCERPT_OK : « le niveau de vie annuel médian des personnes vivant dans un logement ordinaire de
  France métropolitaine est de 25 760 euros par unité de consommation. Il correspond à un revenu
  disponible de 2 150 euros mensuels pour une personne seule. »

Source famille D : Observatoire des inégalités, « À quels niveaux se situent les seuils de
pauvreté en France ? », publié le 09/07/2025.
URL : https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France
— fetché (HTTP 200).

- **FCT-004** (EPI=FACT, famille D relais de A) : seuil à 60 % = **1 337 €/mois** pour une personne
  seule, **données 2024** selon l'Insee (millésime différent de FCT-002).
  EXCERPT_OK : « Une personne vivant seule est considérée comme pauvre en France quand ses revenus
  mensuels sont inférieurs à 891, 1 114 ou 1 337 euros (données 2024 selon l'Insee), selon que l'on
  utilise le seuil de pauvreté fixé à 40 %, 50 % ou à 60 % du niveau de vie médian. »

Tentative famille C : Le Monde, « La pauvreté et les inégalités au plus haut depuis trente ans »
(07/07/2025) — **fetch échoué** : HTTP 200 mais « Client Challenge » (JS anti-bot), contenu
illisible. Non compté comme source (EXCERPT_OK impossible).

## §2 REGISTRE MACHINE-READABLE FACT_REGISTRY_V1

```
<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8600989 | A | 2025-07-07 | pauvrete-taux-60-2023 | 15.4 | 452c2c9e-0dbd-40bd-9dfa-495f626453c6
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8600989 | A | 2025-07-07 | pauvrete-seuil-60-euros-2023 | 1288 | 452c2c9e-0dbd-40bd-9dfa-495f626453c6
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8600989 | A | 2025-07-07 | pauvrete-nb-pauvres-millions-2023 | 9.8 | 452c2c9e-0dbd-40bd-9dfa-495f626453c6
FCT-004 | FACT | ✧ | https://www.inegalites.fr/A-quels-niveaux-se-situent-les-seuils-de-pauvrete-en-France | D | 2025-07-09 | pauvrete-seuil-60-euros-2024 | 1337 | 452c2c9e-0dbd-40bd-9dfa-495f626453c6
FCT-005 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8600989 | A | 2025-07-07 | niveau-vie-median-euros-2023 | 25760 | 452c2c9e-0dbd-40bd-9dfa-495f626453c6
<!-- /FACT_REGISTRY_V1 -->
```

Note de construction : tous les faits sont `✧` (famille unique fetchée). Aucun n'atteint `✦`.
C'est un résultat de discipline, pas une défaillance : cf. §3.

## §3 FRICTIONS OBSERVÉES (où la discipline tient / peine)

1. **La règle ≥2 familles refuse `✦` sur un fait statistique officiel.** INSEE (A) est le seul
   émetteur primaire. Le Monde (C) = mur anti-bot. L'Observatoire (D) relaie « selon l'Insee ».
   Aucun fait n'a donc 2 familles de provenance réellement indépendantes → tous `✧`. Correct.
2. **Le piège du millésime est capté par le slug.** 1 288 € (2023, FCT-002) vs 1 337 € (2024,
   FCT-004) ont des `sujet` distincts (`…-2023` vs `…-2024`) : `detect_contradictions.py` ne les
   signalera **pas** comme contradiction. C'est exactement la frontière que les erreurs passées
   (DGSI 5 000/5 500, Squarcini) franchissaient faute d'ancrer l'année dans l'identité du fait.
3. **« Relais » ≠ « corroboration ».** L'Observatoire (D) affirme un chiffre dont la source est
   INSEE (A). Deux émetteurs distincts, mais une seule **mesure** sous-jacente. La règle des
   familles ne le compte donc pas comme 2 familles pour un même millésime : c'est une fausse
   corroboration détectée, pas un recoupement. Extension exacte du cas DILA (Légifrance +
   Service-Public = même émetteur).
4. **Mur anti-bot ≠ source morte.** Le Monde renvoie 200 + « Client Challenge » : l'URL est
   vivante mais le contenu est inaccessible au fetch automatisé. Statut distinct du 403 Légifrance
   (§4.6 FACT_VERIFICATION) mais même conséquence : EXCERPT_OK impossible → source non comptée.

## §4 VERDICT DE DISCIPLINE

Le pipeline **force** le fetch primaire et les ≥2 familles au niveau déterministe : aucun `✦`
ne peut être attribué ici sans 2 familles fetchées, et le registre ci-dessus est ce que
`verify_facts.py` valide (structure). La **vérité** du contenu (15,4 %, 1 288 €, 9,8 M) reste un
jugement humain sur extraits verbatim, non scripté (AGENTS.md §4). Le résultat le plus instructif
n'est pas le chiffre : c'est que, pour un indicateur à émetteur unique, la barre `✦` est
structurellement hors d'atteinte et force l'honnête `✧`.
