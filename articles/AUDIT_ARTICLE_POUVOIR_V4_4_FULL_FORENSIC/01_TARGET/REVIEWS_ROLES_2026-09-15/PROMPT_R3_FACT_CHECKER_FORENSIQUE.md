# Rôle R3 : Fact-checker forensique

Lis d'abord `00_CONTEXTE_COMMUN.md`, puis le rôle ci-dessous.

Tu disposes du shell et du réseau (`curl`, `python3`). Mission : confronter les affirmations
factuelles de l'article aux **sources du registre final**, en priorité les pièces primaires, et
signaler toute divergence. Tu ne fabriques aucune source : une page inaccessible se déclare
inaccessible, une page qui ne dit pas ce qu'on lui fait dire se déclare divergente.

Faits à recontrôler en priorité (au minimum, dans cet ordre) :

1. BNP Paribas : 8,97 milliards de dollars, plaider-coupable du 30 juin 2014, interdiction
   temporaire d'un an de compensation en dollars (registre [10]).
2. Alstom : enquête FCPA ouverte en 2010, arrestation de Frédéric Pierucci en avril 2013, cession
   signée en 2014, autorisation IEF du 5 novembre 2014, plaider-coupable du 22 décembre 2014,
   772,29 M$ de pénalité (registre [44], [52], [53], [54], [1]).
3. General Electric : engagement de 1 000 emplois nets, pénalité de 50 000 euros par emploi manquant,
   25 emplois nets créés, 50 M€ réclamés (registre [56], [72]).
4. TotalEnergies : annonce du 16 mai 2018, coût du projet South Pars 11 évalué à 4,8 Md$, 40 % du
   capital détenu par des investisseurs nord-américains contre 25,3 % d'actionnaires français
   (registre [11], [71], [74]).
5. Health Data Hub : plus de 66 millions de personnes couvertes par l'assurance maladie, hébergement
   confié à Microsoft Azure (registre [73]).
6. Cloud : « 70 % du marché européen du cloud d'infrastructure détenu par trois fournisseurs
   américains » (registre [80]) : la source porte-t-elle ce périmètre et cette période ?
7. Contrôle des investissements étrangers : 337 décisions rendues en 2024, dont 182 dans le champ,
   54 % des autorisations conditionnées, six refus en trois ans, 392 dossiers en 2024 contre 309 en
   2023 (registre [23], communiqué n° 815 et rapport annuel du Trésor).
8. HATVP : 751 projets soumis pour avis en 2024, 7 % d'avis d'incompatibilité en 2023, moins de dix
   par ministère sur 2020-2023, 77 % de compatibilités avec réserves (registre [84], [85], [40]).
9. VIGINUM 2024 : 259 phénomènes inauthentiques, dont 174 liés à une ingérence numérique étrangère,
   25 manœuvres visant les scrutins français, 43 visant les Jeux de Paris, signalements à sept
   plateformes (registre [3]) : les sept plateformes nommées sont-elles celles du rapport ?
10. Rockhopper c. Italie : 190 M€ en août 2022, annulation le 2 juin 2025 par un comité ad hoc du
    CIRDI (registre [49]).
11. Agences de presse : « jusqu'à 75 % de l'actualité en ligne » aux Pays-Bas (registre [29]) et le
    rôle structurant en Suisse (registre [30]) : les formulations du corps excèdent-elles les sources ?
12. Défense : 57,1 milliards d'euros en 2026 (registre [76]) et « 2e rang mondial des exportateurs
    d'armement » (registre [81]) : périmètres, périodes, unités.
13. Dates réglementaires : eIDAS 2 (règlement 2024/1183) et son article 45a ; dérogation ePrivacy
    rétablie par le règlement 2026/1881 jusqu'au 3 avril 2028 et son caractère volontaire ;
    directive 2026/1021 adoptée le 29 avril 2026, en vigueur le 31 mai 2026 ; sortie du TCE notifiée
    en juin 2024 ; règlement de blocage n° 2271/96 ; arrêt Bank Melli C-124/20 du 21 décembre 2021.
14. Politique : délibérations HATVP 2022-123 et 2022-104 du 17 mai 2022 ; 101 voyages parlementaires
    pris en charge entre 2017 et 2024 ; avis de refus de départ vers CMA CGM ; présidence du conseil
    d'administration d'Hopium effective en juin 2022 (registre [37], [38], [82], [83]).
15. Les deux seules pièces que l'article signale lui-même comme non lues intégralement dans les
    passes précédentes : le communiqué Vattenfall et le document Internet Society sur New IP.

Sortie attendue : tableau `ID | Ligne | Affirmation verbatim | Source invoquée | Statut (CONFIRMÉ / DIVERGENT / NON VÉRIFIABLE / SOURCE INACCESSIBLE) | Preuve (URL consultée + phrase exacte de la source) | Correction`.
Puis une liste courte des affirmations du corps **sans renvoi** ou dont le renvoi ne porte pas la
phrase. Ne développe pas de commentaire juridique (ce n'est pas ton rôle) et n'invente jamais un
chiffre de remplacement : propose seulement la suppression ou la reformulation sur la source vérifiée.

Rapport à écrire : `articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/REVIEWS_ROLES_2026-09-15/R3_FACT_CHECKER_FORENSIQUE.md`
