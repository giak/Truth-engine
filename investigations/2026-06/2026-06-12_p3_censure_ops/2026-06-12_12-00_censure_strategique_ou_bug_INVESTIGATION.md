# INVESTIGATION P3 #10 : Censure Stratégique ou Bug  : L'Absence de Prescription dans le KERNEL est-elle Délibérée ?

**Date** : 2026-06-12
**Complexité** : SIMPLE
**Impact** : 6/10
**Symboles KERNEL** : Κ Ξ Ω

---

## §0 RÉSUMÉ

L'enquête P1#1 (Red Teaming) et la synthèse (TC2) identifient un gap : le KERNEL (RESISTANCE.md) a 3/8 concepts chargés, tous négatifs (FAKE_RESISTANCE, OPPOSITION_CONTROLLED, DEPOLITICIZATION). Les 5 concepts d'action positive (SOLIDARITY_NETWORK, CIVIL_DISOBEDIENCE, MUTUAL_AID, COMMONS, COLLECTIVE_EFFICACY) sont VIDES.

Deux hypothèses s'affrontent : (1) BUG  : l'architecture KERNEL a été figée en novembre 2025 avant la production des articles d'action, et personne n'a fait la mise à jour, (2) FEATURE  : l'auteur a DÉLIBÉRÉMENT laissé ces concepts vides parce que les documenter les exposerait à l'adversaire.

Cette investigation teste les deux hypothèses sans pouvoir interroger l'auteur.

**Thèse** : L'absence de prescription est probablement un BUG (architecture figée + négligence), mais elle FONCTIONNE comme un FEATURE (OPSEC par inadvertance). Le résultat est le même : le corpus ne documente pas ses méthodes opérationnelles. La question de l'intention est secondaire  : c'est l'EFFET qui compte.

---

## §1 INDICES DU BUG : ARCHITECTURE FIGÉE

### F001 : Le KERNEL a été figé en novembre 2025 ; les articles d'action ont été publiés entre janvier et mai 2026
**Source** : Analyse du corpus ; TC2
**Fiabilité** : ❧

Le décalage temporel est documenté : l'architecture conceptuelle (clusters KERNEL) précède la production des articles proposant des solutions. C'est un indice fort de BUG : l'architecture n'a simplement pas été mise à jour après la production de nouveau contenu. Les 5 concepts vides ne sont pas des secrets gardés  : ce sont des coquilles vides qui attendent d'être remplies.

### F002 : Les articles d'action (rhizome, résidu, attrition, désorganisation, RIC) existent et sont PUBLIÉS  : ils ne sont pas cachés
**Source** : Articles Substack ; P1#1 (F-ace-003)
**Fiabilité** : ✧

Si l'auteur voulait cacher les méthodes, il n'aurait pas publié 17 articles les décrivant sur Substack. La théorie d'action en 4 couches est PUBLIQUE. L'absence dans le KERNEL n'est pas une censure  : c'est un défaut d'intégration architecture/articles.

---

## §2 INDICES DU FEATURE : OPSEC PAR INADVERTANCE

### F003 : Les mouvements historiques (ANC, FLN, IRA) pratiquaient la stratification de l'information : objectifs publics, méthodes transmises oralement ou en cellules fermées
**Source** : Recherche web : ANC/FLN/IRA OPSEC éditorial
**Fiabilité** : ✧

L'ANC (Afrique du Sud) séparait strictement l'ANC (mouvement public) et Umkhonto we Sizwe (aile armée). Le FLN algérien utilisait une structure pyramidale cloisonnée où l'instruction était largement orale. La rareté de manuels écrits n'était pas une incompétence : tout document écrit constituait une preuve pour les services de renseignement.

### F004 : Le marqueur du FEATURE : le texte JUGE l'espace vide comme dangereux, plutôt que de le laisser vide par omission
**Source** : Analyse
**Fiabilité** : ❧

La distinction clé entre BUG et FEATURE : dans un FEATURE, le texte contient une méta-explication justifiant POURQUOI l'information n'est pas documentée (« la pratique s'apprend sur le terrain », « l'exercice en cellule est la limite de la théorie »). Dans un BUG, l'espace est simplement VIDE. Le KERNEL ne contient PAS ce type de méta-explication  : ce qui penche vers le BUG.

---

## §3 IMPACT SUR LA SYNTHÈSE

Cette investigation **ne tranche pas** entre BUG et FEATURE  : c'est impossible sans interroger l'auteur. Mais elle établit que l'EFFET est le même : le corpus ne documente pas ses méthodes opérationnelles. Si c'est un BUG, il faut le corriger (remplir les 5 concepts vides). Si c'est un FEATURE, il faut le reconnaître comme tel et documenter la STRATÉGIE d'OPSEC éditorial (pour que les futurs contributeurs sachent quels concepts laisser vides et pourquoi).

**Recommandation** : traiter l'absence comme un BUG jusqu'à preuve du contraire. Remplir les 5 concepts vides avec des résumés des articles d'action. Si l'auteur les vide à nouveau, on saura que c'est un FEATURE.

---

## §4 LIMITES

- L'auteur n'a pas été interrogé. Toute conclusion sur l'intention est spéculative.
- La distinction BUG/FEATURE est binaire ; la réalité pourrait être un mélange (certains concepts vides par négligence, d'autres par OPSEC).

---

## §5 WOLVES  : CONTRE-ARGUMENTS DÉVASTATEURS

### L1 : Le rasoir d'Hanlon

« Ne jamais attribuer à la malice ce que l'incompétence suffit à expliquer. » Un fichier .md non mis à jour pendant 7 mois alors que les articles d'action sont publiés en clair sur Substack (5€/mois), c'est de la négligence éditoriale. Prétendre que cette négligence est une « censure stratégique de niveau OPSEC » est du narcissisme intellectuel. Si l'auteur voulait vraiment cacher des méthodes, il ne les vendrait pas sur une plateforme américaine. La thèse du FEATURE est une rationalisation a posteriori qui flatte l'auteur en le présentant comme un stratège clandestin  : alors qu'il a juste oublié de linker ses propres articles.

### L2 : Le paradoxe de la mitose

Une architecture open source dont la survie dépend de la diffusion massive ne peut PAS simultanément cacher « stratégiquement » ses prescriptions. Cacher la recette empêche la mitose. Si le KERNEL doit être dupliqué par d'autres groupes pour que la coordination acéphale scale, alors il doit être COMPLET. Un KERNEL incomplet est un KERNEL mort : personne ne peut l'utiliser, donc personne ne le duplique, donc il reste confiné à son auteur initial. L'OPSEC éditorial est contradictoire avec l'objectif affiché de diffusion.

### Réponse

Le loup 1 est dévastateur et probablement vrai. L'enquête elle-même admet que les indices penchent vers le BUG (§1, F001-F002). La thèse du FEATURE est une hypothèse minoritaire que l'enquête explore par honnêteté intellectuelle, pas par conviction. Le loup 2 est recevable : la contradiction entre « OPSEC » et « diffusion open source » aurait dû être traitée plus frontalement. La seule défense partielle : l'OPSEC éditorial ne porte pas sur les IDÉES (publiées sur Substack) mais sur leur AGRÉGATION SYSTÉMATIQUE en un manuel unique qui deviendrait un mode d'emploi pour l'adversaire. La distinction est subtile et probablement spécieuse  : mais elle existe.

---

## §6 SOURCES

- KERNEL RESISTANCE.md
- Articles Substack (janvier-mai 2026)
- ANC/FLN/IRA : pratiques OPSEC historiques
