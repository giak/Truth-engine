# Rapport d'attaque systématique — V0.1

Date : 2026-08-16  
Scope : résumé professionnel fourni, portfolio/CV publics, page Substack, dépôts GitHub accessibles et README clés.

## Résultat court

La base actuelle montre une **preuve de fabrication technique substantielle**, mais une **preuve commerciale asymétrique** :
- historique professionnel : chronologie détaillée, essentiellement auto-documentée dans la V0.1 ;
- projets IA récents : existence et contenu technique largement inspectables ;
- utilisation client/production des projets IA récents : peu documentée dans le corpus actuel ;
- ROI/gains historiques : nombreux chiffres, mais non corroborés dans le corpus collecté ;
- production éditoriale : publiquement observable, volumes exacts encore à recompter.

Aucun claim n'est « sauvé » parce qu'il est favorable. Aucun claim n'est rejeté parce qu'il est auto-déclaré : il est simplement classé au niveau de preuve disponible.

## Batterie d'attaques

### A1 — Atomicité
Question : le claim contient-il plusieurs affirmations ?
Action : scinder rôle, période, technologie, résultat, métrique.

### A2 — Origine
Question : plusieurs sources sont-elles réellement indépendantes ?
Risque observé : CV, portfolio, README et Substack ont le même originator.

### A3 — Portée
Question : la pièce prouve-t-elle le dépôt, le sous-système, le produit ou la production client ?
Cas : « Truth Engine 0 .py » ne peut pas être appliqué à la racine du dépôt, où des scripts Python sont présents.

### A4 — Temporalité
Question : la valeur est-elle un snapshot ou un invariant ?
Cas : MnemoLite 199 → 1570 → 1893 tests ; 29 → 31 outils MCP ; ~37k → ~39.7k mémoires.

### A5 — Définition de métrique
Question : « test » signifie-t-il fonction, cas collecté, fichier ou suite ?
Gate : exécuter/collecter avant de publier la valeur comme mesure observée.

### A6 — Fabrication ≠ production
Question : un dépôt public prouve-t-il un système client ?
Réponse : non. Il prouve au minimum un artefact/repository dans la portée inspectée.

### A7 — Auteur ≠ mainteneur
Question : un compte GitHub unique prouve-t-il l'auteur exclusif ?
Réponse : non. LLM, bibliothèques, contributions externes ou travaux hors Git peuvent intervenir.

### A8 — Résultat commercial
Question : le gain/ROI est-il mesuré, attribuable et documenté ?
Résultat V0.1 : claims HydroDam/Accès/DFacto/BBOI/BBOIHeures/VDGI bloqués.

### A9 — Inflation terminologique
Question : « expert », « OS cognitif », « zéro perte » ajoutent-ils une conclusion non mesurée ?
Action : décrire les artefacts et laisser les capacités être dérivées.

### A10 — Contradiction
Question : valeurs incompatibles à date/définition identiques ?
Résultat : beaucoup de divergences sont probablement temporelles; ne pas créer de faux conflit.

### A11 — Fraîcheur
Question : quelle date de capture ?
Règle : toute donnée actuelle externe reçoit `captured_at`.

### A12 — Confidentialité
Question : une preuve peut-elle être stockée sans être publiée ?
Règle : oui. Preuve privée ≠ pièce à exposer.

### A13 — Reproductibilité
Question : une métrique technique peut-elle être recalculée ?
Priorité : tests, outils MCP, routes/pages, corpus publications, nombre de mots.

### A14 — Falsification
Question : qu'est-ce qui ferait tomber le claim ?
Chaque claim HIGH doit avoir une future gate explicite si non corroboré.

## Claims P0 à réparer

1. **Expériences à forte valeur** : SolarStack, Accès Industrie, Breizh Company.
   - Rechercher contrat/attestation/recommandation/archives contemporaines.
2. **SolarStack** : 1000+ events/s, 99.99 %, <100 ms, <50 MB.
   - Rechercher bench/logs/monitoring/document technique ou reformuler sans chiffre.
3. **ROI/gains historiques** : tout bloquer jusqu'à pièce de calcul ou attestation.
4. **MnemoLite** : mesurer directement tests, outils MCP, routes/pages.
5. **Truth Engine** : définir « investigation », « enquête », « rapport », « article » puis recompter.
6. **Substack** : exporter la liste, dédoublonner, compter articles et mots.
7. **« solo »** : définir « piloté/développé individuellement » et vérifier historique de contributions.
8. **MCO « zéro perte »** : créer benchmark ou retirer l'absolu.

## Claims déjà assez solides pour une future communication prudente

- existence de plusieurs dépôts publics actifs : MnemoLite, Truth Engine, Expanse, CV Generator, RéseauRacine ;
- MnemoLite documente une architecture PostgreSQL/pgvector, recherche hybride et intégration MCP ;
- Truth Engine documente un pipeline d'analyse/production éditoriale ;
- CV Generator documente une architecture Vue/TypeScript/Clean Architecture/JSON Resume/i18n ;
- RéseauRacine documente un travail Rust/Nostr/crypto appliquée ;
- la page Substack publique documente une activité d'écriture/recherche utilisant des LLM ;
- le CV public contient une chronologie professionnelle longue et détaillée, à qualifier comme auto-documentée tant que non corroborée.

## Conclusion hostile

Le risque principal n'est pas un manque de matière. C'est **l'inflation de certitude** :
- transformer un README en benchmark ;
- transformer un dépôt en preuve de production ;
- transformer une auto-description en expertise certifiée ;
- transformer un ancien chiffre en vérité actuelle ;
- transformer une amélioration ressentie en ROI mesuré.

La V0.1 bloque précisément ces passages.
