# INVESTIGATION — IA déclarée vs IA réelle

**Date :** 2026-08-25  
**Protocole :** RENARD CORE V3  
**Investigation ID :** `INV-DECLREAL-001`  
**Objet :** mesurer l'écart entre discours/adoption déclarée et intégration productive réellement documentée.

## Hypothèse de travail

La diffusion de l'IA peut être simultanément :
- très large comme **usage individuel ou outil générique** ;
- beaucoup plus faible comme **automatisation intégrée au cœur de l'entreprise** ;
- encore plus rare comme **transformation structurelle mesurable de coûts, prix, recrutement ou organisation**.

L'enquête ne cherche pas à prouver un « AI-washing » général. Elle teste où la communication précède les preuves, où elle leur correspond, et où l'adoption réelle est au contraire plus avancée que le discours.

## Méthode

### Échelle de maturité réelle
0 aucune → 1 ad hoc → 2 assistance/pilote → 3 workflow intégré → 4 production avec KPI → 5 effet structurel.

### Intensité narrative
0 silence/rejet → 1 prudent → 2 important → 3 stratégique → 4 central → 5 AI-first/AI-powered/récit existentiel.

`gap_communication = intensité narrative - maturité documentée`.

**Important :** un gap positif n'est pas une preuve de tromperie. C'est un indicateur de **distance entre le récit public et les preuves opérationnelles disponibles**.

## Échantillon

30 cas **délibérément stratifiés et non représentatifs** :
- 10 grands groupes à communication IA forte ou transformation visible ;
- 10 PME/ETI françaises avec cas d'usage concrets sélectionnés comme mécanismes ;
- 10 témoins à usage faible ou nul tirés de l'enquête qualitative France Num.

Les témoignages France Num sont des cas sélectionnés et auto-déclarés : ils ne permettent pas d'estimer une prévalence nationale.

## Résultats du panel

| Groupe | N | Narrative moyen /5 | Maturité moyenne /5 | Gap moyen | Maturité ≥3 | Maturité ≥4 |
|---|---:|---:|---:|---:|---:|---:|
| Grands groupes | 10 | 3.9 | 3.5 | +0.4 | 9/10 | 5/10 |
| PME/ETI cas concrets | 10 | 1.5 | 2.9 | -1.4 | 7/10 | 2/10 |
| Témoins faibles | 10 | 0.7 | 0.6 | +0.1 | 0/10 | 0/10 |

### Lecture

1. **Le marketing n'explique pas tout.** Chez les grands groupes sélectionnés, le récit est légèrement en avance sur les preuves publiques, mais plusieurs entreprises ont de vrais systèmes en production.
2. **Il existe aussi une IA silencieuse.** Dans les PME sélectionnées pour leurs cas concrets, la maturité opérationnelle dépasse largement l'intensité narrative : EIST et Ixarys fournissent des KPI plus concrets que nombre de grands groupes.
3. **Le tissu réel reste très hétérogène.** Les dix témoins faibles ne montrent aucune intégration productive.
4. **Le résultat national ne peut pas être déduit du panel** : les statistiques publiques restent la base pour la prévalence.

## La vraie fracture statistique

Trois enquêtes différentes aboutissent à la même structure générale, sans former un même entonnoir :
- Bpifrance : 55% des TPE-PME disent recourir à l'IAG, mais 17% régulièrement.
- France Num : 26% disent utiliser une solution IA, mais 5% automatiser des tâches.
- BCE : environ 70% des entreprises de zone euro déclarent un usage quelconque, mais 7% seulement un usage significatif.

Ces chiffres ne sont pas directement divisibles entre eux, car questions, échantillons et définitions diffèrent. Leur convergence suggère néanmoins une distinction robuste entre **diffusion** et **profondeur**.

## Cas forensiques

### Publicis : performance réelle, causalité marketing non isolée
Publicis affiche +5,6% de croissance organique en 2025, une marge de 18,2% et qualifie son modèle de « AI-powered ». Les résultats sont réels. L'affirmation que l'IA *cause* la surperformance est une attribution managériale, pas une identification causale indépendante.

### Capgemini : vendeur et restructurateur IA
Les bookings GenAI/agentic dépassent 10% au T4 2025. Capgemini prévoit environ 700 M€ de coûts de restructuration sur deux ans pour adapter ses compétences à l'évolution technologique principalement portée par l'IA. Cette pièce est importante mais non indépendante : Capgemini vend précisément la transformation IA. Elle ne fournit pas un mapping public tâche automatisée → poste supprimé.

### Société Générale : le meilleur antidote à la causalité simpliste
Le projet de 1 800 postes nets en moins agrège optimisation des achats, simplification, mutualisation, automatisation et IA. Présenter ces 1 800 postes comme « remplacés par l'IA » dépasserait la source.

### Michelin : base rate de restructuration sans causalité IA
Michelin envisage jusqu'à 1 500 postes tertiaires adaptés sur trois ans en invoquant surtout structure de coûts, concurrence, évolution des métiers et simplification. Ce cas montre qu'un plan de réduction d'effectifs peut exister dans le même contexte technologique **sans être attribué principalement à l'IA**.

### Ingérop : 80-85% peut être technologiquement impressionnant et opérationnellement insuffisant
Le pilote d'analyse d'appels d'offres produit des synthèses utiles, mais 80-85% de fiabilité n'est pas jugé suffisant pour automatiser la décision go/no-go. Ce cas est central : la frontière n'est pas « ça marche / ça ne marche pas », mais « assez fiable pour quel risque ? ».

### EIST et Ixarys : la PME peut être plus réelle que le storytelling
EIST ramène un devis de deux heures à dix minutes. Ixarys ramène un traitement documentaire d'environ un mois à quelques heures et attribue deux nouveaux clients en partie à la fonctionnalité. Ces deux cas montrent qu'une TPE/PME peut obtenir un impact profond sur un workflow **sans discours AI-first**.

## Ce que l'enquête soutient

### H1 — « L'adoption déclarée surestime l'intégration productive »
**STRENGTHEN — confiance 0,94.**
La meilleure preuve n'est pas le panel subjectif, mais la convergence France Num / Bpifrance / BCE.

### H2 — « Les PME n'ont pas pris le virage IA »
**WEAKEN sous sa forme absolue.**
Les petites entreprises adoptent moins selon l'Insee, mais certaines intègrent déjà profondément l'IA. Formulation défendable :
> La majorité du tissu PME n'a pas encore reconstruit son système productif autour de l'IA, tandis qu'une minorité de cas concrets obtient déjà des gains importants.

### H3 — « La mouvance IA est largement marketing »
**MAINTAIN, mais seulement comme phénomène partiel.**
Le panel montre de vrais gaps de communication chez certains vendeurs ou grands groupes, mais il montre aussi des déploiements réels et une IA peu médiatisée dans des PME. « Tout est marketing » est réfuté.

### H4 — « L'IA sert parfois de récit de restructuration »
**SUPPORTED, non généralisable.**
Le Sénat reprend explicitement cette hypothèse via Verdugo/Ferguson. Les cas SG, Capgemini et Michelin montrent pourquoi il faut contrôler les causes concurrentes avant toute attribution.

### H5 — « Le vrai obstacle est organisationnel autant que technique »
**STRENGTHEN — confiance 0,95.**
Insee : expertise, compatibilité, droit, coûts. OCDE : ROI, data/privacy, skills, upskilling. Cas Valtus/Acorus/Ingérop/Preventech : qualité des données, organisation, validation et changement sont récurrents.

### H6 — « Le secteur des services basculera en premier »
**SUPPORTED partiel.**
Les services et l'information-communication adoptent davantage. Mais l'usage significatif reste minoritaire. Le vrai seuil est workflow × fiabilité × prix × responsabilité × organisation.

### H7 — « Une minorité d'acteurs peut modifier l'économie d'un secteur avant adoption générale »
**SUPPORTED comme signal émergent.**
Dans les services IT indiens, Reuters documente déjà le passage de facturation au temps vers des contrats davantage liés aux résultats sous pression de clients exigeant plus de productivité et des prix plus bas. Ce mécanisme peut transmettre le choc aux non-adopteurs.

## [ADVERSARY]

| Axe | H | Rival | Observation | Favorise |
|---|---|---|---|---|
| Adoption déclarée | usage = transformation | usage peut rester superficiel | 55% IAG vs 17% régulier; 26% solution IA vs 5% automatisation; ~70% usage eurozone vs 7% significatif | **H superficiel** |
| PME | PME hors jeu | certains petits acteurs sautent directement sur un workflow rentable | EIST, Ixarys, Cornec | **Rival à l'absolu** |
| Marketing | grands groupes survendent | les systèmes sont réellement en production | Orange/Carrefour forts; Publicis/Capgemini communication plus difficile à causaliser | **Mixte** |
| Licenciements | IA cause directe | coûts/conjoncture/simplification préexistent | SG multifacteur; Michelin restructuration sans causalité IA | **Rival** |
| ROI | modèles trop faibles | organisation/data/intégration limitent davantage | OCDE + cas PME | **Rival technique pur** |
| Services | impact futur lointain | prix et contrats changent déjà | IT services : outcome-based pricing et pression prix | **H impact économique précoce** |

## [EVALUATE]

| Atom | Tier principal | Indépendant ? | Survit BREAK ? | Statut | Confiance |
|---|---:|---|---|---|---:|
| A1 récit > maturité | T1-T2 | Y partiel | Y | SUPPORTED | 0,90 |
| A2 grandes > PME | T1-T2 | Y | partiel | SUPPORTED NUANCÉ | 0,86 |
| A3 usage != automatisation | T1-T2 | Y | Y | VERIFIED/SUPPORTED FORT | 0,96 |
| A4 IA justification restructuration | T1-T3 | partiel | Y | SUPPORTED CAS-LEVEL | 0,82 |
| A5 services plus exposés/adopteurs | T1-T2 | Y | Y | SUPPORTED | 0,90 |
| A6 freins organisation/data/skills/ROI | T1-T2 | Y | Y | SUPPORTED FORT | 0,95 |
| A7 impact par non-création/recrutement | T1-T2 | Y | Y partiel | SUPPORTED, suivi antérieur | 0,88 |
| A8 minorité modifie marché | T2-T3 | partiel | Y partiel | SIGNAL / OPEN LARGE SCALE | 0,72 |

**EPISTEMIC_LEDGER** := verified: 1 | supported: 6 | disputed/open: 1 | refuted: 0

## [REPORT]

| Field | Content |
|---|---|
| what_changed_since_last | Le dossier distingue maintenant diffusion, usage régulier, workflow intégré, production mesurée et transformation structurelle. |
| surviving_H | adoption déclarée surévalue la profondeur; marketing existe; organisation/data/ROI sont des goulots; services subissent déjà pression sur le modèle de facturation |
| killed_H | « les PME n'ont pas pris le virage IA » au sens absolu; « tout est marketing » |
| confidence_before -> confidence_after | hypothèse 'écart récit/réalité' : 0,65 → 0,90; hypothèse 'PME hors jeu' : 0,70 → 0,45 |
| next_priority | Construire le **détecteur de bullshit IA** et auditer 20 annonces de licenciements/restructurations avec chronologie réelle du déploiement |
| CALIBRATION | robuste sur diffusion vs profondeur; non représentatif au niveau du panel 30 |

## Conclusion

La bonne opposition n'est pas **IA réelle contre IA fictive**.

Elle est :

`IA annoncée → IA utilisée → IA intégrée → IA mesurée → IA structurelle`.

Beaucoup d'entreprises sont entre les deux premiers étages. Quelques-unes ont déjà atteint les quatrième et cinquième. Et la communication publique peut être soit très en avance, soit étonnamment en retard sur ce qui se passe réellement.

Le prochain objet discriminant est donc un audit systématique des annonces :
**« dites-moi ce qui a été automatisé, depuis quand, avec quel KPI, quel coût complet, quel contre-factuel et quel effet réel sur l'emploi »**.
