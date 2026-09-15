# Rôle R3 (reprise) : Fact-checker forensique sur sources déjà téléchargées

Lis d'abord `00_CONTEXTE_COMMUN.md`, puis le rôle ci-dessous.

**Contexte de reprise** : la première exécution de ce rôle a téléchargé les sources primaires dans
`/tmp/factcheck_sources/` puis a été interrompue par le délai avant d'écrire son rapport. Les fichiers
sont sur disque : tu n'as pas besoin du réseau. Tu travailles uniquement sur ces fichiers locaux, plus
l'article, plus les deux pages accessibles par `curl` si un point l'exige.

Fichiers disponibles (liste à confirmer par `ls -la /tmp/factcheck_sources/`) :
`bnp_doj_jina.txt`, `bnp_bnpp_jina.txt`, `alstom_doj_jina.txt`, `total_southpars.txt`,
`total_conversation.txt`, `total_cnbc.txt`, `synergy_cloud.txt`, `synergy_cloud2.txt`,
`synergy_cloud3.txt`, `cnil_healthdata.txt`, `cuggia_healthdata.txt`, `hatvp_2024.txt`,
`CComptes` (mobilités), `Tresor IEF` (rapport annuel et communiqué n° 815).

Mission : confronter les affirmations de l'article à ces pièces, et rendre un verdict par affirmation.

Faits à trancher, dans cet ordre :

1. **BNP Paribas** — 8,97 milliards de dollars, plaider-coupable du 30 juin 2014, interdiction
   temporaire d'un an de compensation en dollars pour les activités pétrole et gaz : la pièce
   `bnp_doj_jina.txt` porte-t-elle ces trois éléments, et l'article en donne-t-il une version exacte ?
2. **Alstom** — 772,29 M$ de pénalité, plaider-coupable du 22 décembre 2014 (`alstom_doj_jina.txt`) :
   le montant et la date sont-ils conformes ?
3. **TotalEnergies / South Pars 11** — 4,8 milliards de dollars de coût total, annonce du 16 mai 2018
   (`total_southpars.txt`) ; 40 % d'investisseurs nord-américains contre 25,3 % d'actionnaires français
   (`total_conversation.txt`) ; la question de la dépendance au refinancement en dollars
   (`total_cnbc.txt`). Les trois chiffres du corps sont-ils adossés ?
4. **Cloud européen** — « 70 % du marché européen du cloud d'infrastructure détenu par trois
   fournisseurs américains » : que disent exactement `synergy_cloud.txt`, `synergy_cloud2.txt` et
   `synergy_cloud3.txt` (part des fournisseurs locaux, périmètre, année) ? L'article attribue-t-il à la
   source une mesure qu'elle ne porte pas ?
5. **Health Data Hub** — « plus de 66 millions de personnes » couvertes par l'assurance maladie
   (`cnil_healthdata.txt`, `cuggia_healthdata.txt`) : chiffre exact et périmètre ?
6. **Contrôle des investissements étrangers** — 392 dossiers en 2024 contre 309 en 2023 ; 337 décisions
   dont 182 dans le champ ; 54 % des autorisations conditionnées ; six refus en trois ans : conformité
   avec le rapport annuel et le communiqué du Trésor.
7. **HATVP** — 751 projets soumis pour avis en 2024 ; 7 % d'avis d'incompatibilité en 2023 ; moins de
   dix par ministère sur 2020-2023 ; 77 % de compatibilités avec réserves (`hatvp_2024.txt`, bilan HATVP,
   rapport Cour des comptes) : les quatre chiffres sont-ils exacts, et sur les bonnes périodes ?

N'invente aucun chiffre. Pour chaque point : statut **CONFIRMÉ** (avec la phrase exacte de la source),
**DIVERGENT** (avec l'écart chiffré), **NON VÉRIFIABLE** (fichier absent ou muet). Si un fichier cité
ci-dessus n'existe pas, dis-le au lieu de le présumer.

Puis la liste des affirmations du corps **sans renvoi** ou dont le renvoi ne porte pas la phrase.
Ne propose pas de commentaire juridique ni de réécriture littéraire : uniquement le fait, la source,
l'écart, et la correction factuelle minimale.

Rapport à écrire : `articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/REVIEWS_ROLES_2026-09-15/R3_FACT_CHECKER_FORENSIQUE.md`
