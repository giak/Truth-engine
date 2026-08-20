# GAP 1 du 10-54 — Le critère de rattachement des publications aux fiches sources du CASD : la publication hérite des sources de son projet, pas de son usage réel

- **Date** : 2026-08-10 | **Heure** : 11:20 CEST | **Type** : INVESTIGATION | **KERNEL** : v2.8
- **État** : `STATE          : FINAL`
- **Dossier** : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_criteres-rattachement-casd/
- **Fait suite à** : 2026-08-10_11-13_verif-3-publications-fiche-dmtg (GAP 1) ; 10-54, 10-48, 09-15 (dossiers CASD/DMTG)

## 1. CONTEXTE

Les dossiers 10-48, 10-54 et 11-13 ont établi que la fiche source DMTG du CASD liste 5 publications dont 4 n'utilisent pas l'enquête dans leur texte (WID WP 2017/4, AER 2023, notes FS 120/121). Le critère de rattachement des publications aux fiches sources n'était pas documenté — c'était le GAP 1 du 10-54, avec une hypothèse « thème vs usage réel ».

## 2. OBJECT

Identifier le mécanisme réel par lequel une publication se retrouve listée sur une fiche source du CASD : vérification d'usage dans le texte, rattachement par projet d'habilitation, ou déclaration volontaire. Sources : site CASD (casd.eu), portail CDAP (cdap.casd.eu), pages publi.php/prj.php/src.php.

## 3. SOURCES LUES

- `SRC-001` : casd.eu/declaration-publications/ — page « Indiquer vos publications » (lue) : le CASD **demande aux chercheurs de déclarer leurs publications** (« Le CASD a besoin de vos publications ! ») et leur rappelle de citer les DOI et la formule de référence (10.34724/CASD).
- `SRC-002` : casd.eu/remontees-des-publications/ — formulaire de remontée (lu) : champs = **auteurs, titre, lien, « Code projet CASD »** — le chercheur rattache sa publication à un projet, pas à des sources.
- `SRC-003` : casd.eu/publi.php?id=108 — fiche de la publication « Accounting for Wealth Inequality Dynamics » (lue) : rubrique « **Données mises à disposition via le CASD (19)** » = exactement les 19 sources du projet 254 ; rubrique « Projet » = TAXOPTI (id=254) ; URL = dt-633.pdf (morte).
- `SRC-004` : casd.eu/publi.php?id=457 — fiche du commentaire AER 2023 (lue) : « **Données mises à disposition via le CASD (68)** » = les 68 sources du projet 1107 (EVREFIS) ; le libellé est « mises à disposition », **pas** « utilisées ».
- `SRC-005` : casd.eu/prj.php?id=254 (TAXOPTI, 19 sources, lu) ; casd.eu/prj.php?id=1107 (EVREFIS/IPP, 68 sources, lu) ; casd.eu/prj.php?id=1041 (« Travaux de France Stratégie »/CGSP, **97 sources**, lu).
- `SRC-006` : casd.eu/src.php?id=106 — fiche source DMTG (lue) : échantillon MOOREA « exhaustives mais incomplètes », produits 2010/2006/1994, DOI persistants (2010 : 10.34724/CASD.106.881.V1).

## 4. FACT_REGISTRY

| ID | Fait | Statut | Source |
|----|------|--------|--------|
| FCT-001 | **Le rattachement publication→source est INDIRECT** : une publication est rattachée à un **projet** (via le formulaire de remontée, champ « Code projet CASD »), et la fiche de la publication liste **toutes les sources « mises à disposition » de ce projet** — pas les sources effectivement utilisées dans le texte | CONFIRMÉ (mécanisme) | SRC-002, SRC-003, SRC-004 |
| FCT-002 | **Preuve arithmétique (identité ensembliste)** : la fiche publi 108 (BdF WP 636) liste exactement **19 sources** = les 19 identifiants du projet 254 (TAXOPTI) ; la fiche publi 457 (AER 2023) liste exactement **68 sources** = les 68 identifiants du projet 1107 (EVREFIS) ; idem pour les notes FS : publi 454 et 455 listent **97 sources chacune** = les 97 du projet 1041. Égalité des ensembles vérifiée par identifiants src.php?id (ordre d'affichage non vérifié) — 3 projets, 3 identités : 19=19, 68=68, 97=97 | CONFIRMÉ (identité ensembliste) | SRC-003, SRC-004, SRC-005 |
| FCT-003 | **Le libellé de l'interface est explicite** : les fiches publications affichent « Données **mises à disposition** via le CASD (N) » — le mot « utilisées » n'apparaît pas ; le référentiel documente l'accès potentiel, pas l'usage effectif | CONFIRMÉ (libellé) | SRC-003, SRC-004 |
| FCT-004 | **La déclaration est volontaire et auto-déclarée** : la page « Indiquer vos publications » appelle les chercheurs à déclarer (« Le CASD a besoin de vos publications ! ») et précise l'objectif : « faire la preuve de sa pertinence auprès de ses partenaires et bailleurs de fonds » — indicateur de performance du CASD, pas registre d'usage vérifié | CONFIRMÉ | SRC-001 |
| FCT-005 | **Les 5 publications de la fiche DMTG héritent de 3 projets** : TAXOPTI (254, 19 sources) → BdF WP 636 + WID WP 2017/4 ; EVREFIS (1107, 68 sources) → commentaire AER 2023 ; France Stratégie/CGSP (1041, **97 sources**) → notes FS 120/121 | CONFIRMÉ | SRC-003 à SRC-005 + fiche DMTG |
| FCT-006 | **Le projet France Stratégie (1041) a accès à la source DMTG parmi 97 sources** — les notes 120/121 sont listées sur la fiche DMTG parce que LEUR PROJET avait DMTG dans son périmètre, pas parce qu'elles la citent | CONFIRMÉ | SRC-005 (prj1041 contient src.php?id=106) |
| FCT-007 | **La fiche publi 108 pointe vers un PDF mort** : URL `publications.banque-france.fr/.../dt-633.pdf` (HTTP → HTML 404 en session) — le référentiel référence aussi un numéro de WP (dt-633) différent du n° 636 retenu au dossier 11-13 (version de travail GGP2016Wealth.pdf) | CONFIRMÉ (constat) | SRC-003 + test HTTP 11-20 |
| FCT-008 | **La source DMTG (src.php?id=106) documente son périmètre réel** : échantillon de successions ayant payé des DMTG, application MOOREA « exhaustives mais incomplètes » complétée par les dossiers papier des FI (fins de fichier) ; produits 2010 (DOI 10.34724/CASD.106.881.V1), 2006, 1994 | CONFIRMÉ | SRC-006 |
| FCT-009 | **Conséquence pour le faisceau** : la « sur-liste » de la fiche DMTG (3 vérifiées intégralement sans mention + 1 résumé seul non vérifié en texte intégral — AER 2023 — + 1 usage avéré) n'est ni une erreur ni une tromperie — c'est la **conséquence structurelle du critère projet** : toute publication d'un projet habilité DMTG hérite de la mention, indépendamment de son contenu | CONFIRMÉ (analyse) | Croisement FCT-001 à 006 + 11-13 |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-10_11-20_criteres-rattachement-casd | - | -
<!-- /FACT_REGISTRY_V1 -->

## 5. PELOTE

```
Chercheur (formulaire remontees-des-publications)
  └── champ « Code projet CASD » → publication rattachée au PROJET
        └── projet = habilitation : N sources « mises à disposition » (19, 68, 97…)
              └── fiche de la publication : hérite des N sources du projet
                    └── fiche source (ex. DMTG) : liste toutes les publications
                          dont le projet avait la source au périmètre
CONCLUSION : la chaîne ne contient AUCUNE vérification d'usage dans le texte.
La fiche source agrège les héritages de projet, pas les exploitations documentées.
```

## 6. GATE_CHECK

- **GAP 1 du 10-54 : RÉSOLU.** Le critère de rattachement est documenté par le dispositif lui-même (formulaire de remontée + libellé « mises à disposition ») : **publication → projet → toutes les sources du projet**. L'hypothèse « thème vs usage » est dépassée : c'est le périmètre d'habilitation du projet qui détermine la liste.
- **Le constat des 10-48/10-54/11-13 s'explique mécaniquement** : 4/5 publications listées sur la fiche DMTG sans mention dans le texte = elles héritent de la source via leurs projets (TAXOPTI, EVREFIS, France Stratégie). Le seul usage avéré (BdF WP 636) est « coincident » : la DMTG était à la fois dans le périmètre du projet ET dans la méthodologie du papier.
- **Cohérence avec 09-15** : la fiche source DMTG indique 12 projets et 5 publications — les 12 projets avaient DMTG à leur périmètre ; les 5 publications listées en héritent.
- **Fait nouveau (FCT-007)** : le référentiel référence un PDF mort (dt-633) et un numéro divergent du n° 636 — la fiabilité documentaire du référentiel a une seconde faille (URL mortes + numérotation flottante), à joindre au constat d'absence de critère d'usage.

## 7. LIMITES

1. Le formulaire de remontée (SRC-002) est vu dans sa version publique ; le traitement interne (validation par le CASD, mise à jour des fiches) n'est pas documenté publiquement — la chaîne exacte « soumission → fiche publi → fiche source » est déduite de la structure des pages et du formulaire, cohérente sur 3 projets.
2. La page de méthodologie du référentiel CDAP n'a pas été identifiée (cdap.casd.eu/referentiel est une application de recherche, pas une documentation ; la page d'accueil renvoie 1 431 octets de contenu minimal via jina).
3. Le nombre exact de sources du projet 1041 (97) inclut la DMTG (id=106) vérifiée par grep — mais l'exhaustivité des 97 n'a pas été recoupée page à page.

## 8. VERDICT

**Le GAP 1 est résolu, et la réponse change la lecture du faisceau.** La fiche source CASD n'atteste PAS l'usage d'une donnée : elle documente les héritages de projets habilités. Une publication listée sur la fiche DMTG signifie seulement que son projet avait DMTG à son périmètre — pas que le texte l'exploite. Le dispositif est un **registre d'accès potentiel** (et un outil de preuve de pertinence pour ses bailleurs, comme le dit la page « Indiquer vos publications »), pas un registre d'usage vérifié. Les publications « sans mention » (3 vérifiées intégralement, 1 résumé seul) sont donc la norme du système, non une anomalie : **la donnée DMTG est « rattachée » par périmètre à un grand nombre de publications dont elle n'est pas l'instrument**. Le fil « la donnée existe mais sa traçabilité est confinée » gagne une précision : la traçabilité n'est pas fausse, elle est **projetuelle et non textuelle** — le dispositif sur-atteste l'usage, dans un sens favorable à sa propre démonstration de pertinence (biais de plaidoyer structurel, sans imputation de mauvaise foi).

## 9. RECOMMANDATIONS

1. **Réutiliser le critère dans les dossiers futurs** : pour toute « publication de la fiche DMTG », vérifier (a) le projet d'attache (champ « Projet » de la fiche publi) et (b) la mention dans le texte — le projet seul ne prouve rien.
2. **Documenter la faille FCT-007** : URL morte dt-633.pdf + divergence de numérotation (633 vs 636) — à ajouter au registre des défauts documentaires du référentiel.
3. **Cadrer la demande CADA** (si poursuite) : demander au CASD la procédure interne de validation des remontées de publications (qui contrôle, quels critères, depuis quand) — le seul maillon non public de la chaîne.
4. **Alimenter le point consolidé** : le mécanisme projet → sources élargit la critique aux 12 projets DMTG (09-15) : chaque publication de chaque projet hérite de toutes leurs sources — la carte des « usages » du référentiel est systématiquement sur-approximée.

## 10. LEÇON

**Un registre d'accès n'est pas un registre d'usage.** Le CASD documente ce que ses projets pouvaient toucher, pas ce que leurs papiers ont utilisé — et il le fait par construction (formulaire de remontée par code projet, libellé « mises à disposition »). Pour un corpus d'enquête sur la connaissance patrimoniale, la leçon est double : (1) ne jamais citer une fiche source CASD comme preuve d'exploitation d'une donnée ; (2) le dispositif a un intérêt structurel à sur-attester la pertinence de ses données (preuve auprès des bailleurs), ce qui oriente sa documentation — à lire avec cette clé, sans imputation de mauvaise foi.
