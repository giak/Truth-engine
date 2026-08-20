# Lot de dix candidats : résultats de vérification

## Périmètre

Les quatre candidats déjà traités précédemment sont exclus du lot :

```text
FC17_0033BA3236A3D267
FC17_00B86A60F5128FFD
FC17_00DC29532E08B562
FC17_026DD557FDAD5442
```

Le lot contient dix nouveaux candidats. Les recherches Mnemolite ont été faites avant les lectures Web. Les URLs identiques ont été lues une seule fois puis évaluées candidat par candidat.

## Résultats

| # | UPSTREAM_ID | Claim résumé | Niveau | Verdict | Memory ID |
|---:|---|---|---|---|---|
| 1 | `FC17_00C616D7AA540782` | XWiki participe à ADMO | L2 | `VERIFIE` | `e7872268-1a1d-4da7-a0c0-0195ed85189d` |
| 2 | `FC17_00D4550C931427FA` | Lie Detectors : organisation du consortium | L1 au mieux | `NOT_VERIFIED` : assertion structurée insuffisamment établie | - |
| 3 | `FC17_01BD29DC772F85E4` | ATC est partenaire de BROD | L0 | `NOT_VERIFIED` : la page BROD lue ne mentionne pas ATC | - |
| 4 | `FC17_01DBCAD2422C8831` | Internews Kosova - KALLXO, membre EFCSN | L2 | `VERIFIE` | `5b3ccf27-a0b0-45d7-bc63-0d343c2d259d` |
| 5 | `FC17_0217F5CA13303655` | EDMO : type infrastructure réseau | L0 au regard du claim exact | `NOT_VERIFIED` : classification non énoncée directement | - |
| 6 | `FC17_02361B7DEBE4E306` | Verificat, membre EFCSN | L2 | `VERIFIE` | `f31f3bc7-648a-4109-af80-7c7d1377c61e` |
| 7 | `FC17_0248637C7AE2D3EE` | EFCSN dirige FACTEUR | PARTIAL / mismatch | `NOT_VERIFIED` : URL redirigée vers l'accueil, claim non établi | - |
| 8 | `FC17_027DB8021A989A3F` | University of Dubrovnik : type université | L1 au mieux | `NOT_VERIFIED` : la page établit la coordination d'ADMO, pas exactement cette classification | - |
| 9 | `FC17_0340EBD9966A1377` | France Médias Monde : société médiatique publique | L1 au mieux | `NOT_VERIFIED` : la page décrit le groupe, mais le type du registre est une classification | - |
| 10 | `FC17_040A2D35079DA036` | Myth Detector, membre EFCSN | L2 | `VERIFIE` | `7e2dd385-baa2-4ea7-9917-a715cecc6835` |

## Taux

```text
Candidats examinés                 : 10
L2 / VERIFIE écrit                 : 4 (40 %)
L1 au mieux, non écrit             : 3 (30 %)
L0 / aucune assertion exacte       : 2 (20 %)
PARTIAL / SOURCE_MISMATCH          : 1 (10 %)
CONFIRME                            : 0 (0 %)
Write-back non vérifié              : 0
```

Accès :

```text
403 automatisés récupérés par Chrome : 2
Source finalement illisible          : 0
URL redirigée                        : 2
```

Les deux `403` ne sont donc pas des verdicts. Dans un cas, le navigateur a néanmoins fourni une page insuffisante ; dans l'autre, la page EDMO reste sans assertion exploitable pour le claim exact.

## Doublons et provenance

- Aucun `duplicate_warning` Mnemolite n'a été retourné pour les quatre écritures.
- Les recherches sémantiques ont souvent renvoyé des mémoires voisines, pas le `UPSTREAM_ID` exact. Elles ne peuvent donc pas servir de dédoublonnage déterministe.
- Trois candidats utilisent la page EFCSN et un quatrième candidat déjà traité utilise la même page. Les entités sont distinctes : les mémoires similaires ne sont pas des doublons.
- La page ADMO couvre deux candidats différents ; cette réutilisation de source est valide, avec un locator propre à chaque claim.
- Une erreur de provenance a été détectée sur le premier candidat ADMO : la redirection `/` → `/en/` n'était pas conservée séparément. La mémoire a été corrigée avant clôture du lot.
- Les dix manifestes locaux copient les clés exactes du CSV. Les six candidats non écrits restent `NOT_VERIFIED`, `memory_id=null`, `writeback_allowed=false` ; les quatre candidats écrits ont été rebouclés vers leur `memory_id`, niveau `L2` et locator.

## Conclusion opérationnelle

Le lot confirme que l'automatisation utile est limitée à :

```text
copie exacte de l'identité amont
→ préparation du manifeste
→ regroupement des URLs identiques
→ contrôle de la clé et du locator
→ rebouclage du memory_id après écriture
```

Le classement EPI, la portée du claim et la décision d'écriture restent manuels. Le taux d'écriture L2 de 40 % ne justifie pas encore un traitement massif : il faut d'abord vérifier le comportement sur un deuxième lot de même taille et contrôler les mémoires similaires avant d'augmenter le volume.
