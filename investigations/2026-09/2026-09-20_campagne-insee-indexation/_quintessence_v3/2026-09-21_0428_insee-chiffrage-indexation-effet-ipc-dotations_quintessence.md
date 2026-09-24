# QUINTESSENCE : insee-chiffrage-indexation-effet-ipc-dotations
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-21_insee-chiffrage-indexation-effet-ipc-dotations/2026-09-21_04-28_insee-chiffrage-indexation-effet-ipc-dotations_INVESTIGATION.md (RUN_ID 20260921-0428, ENGINE 2.10.6, INPUT_KIND UPDATE, COMPLEXITY 9 APEX, G0-G10 PASS, DELIVERY PASS)

## 1. Métadonnées & trace source
UPDATE du run 19-21 et du run 17-04 : que fait un dixième de point d'IPC sur les montants indexés, et que vaut un écart d'estimation de population légale sur une dotation réelle ? Période 1946-2027. 9 faits, 19 requêtes, 8 checkpoints. L'objet n'est pas de dénoncer l'indexation mais de mesurer ce qui est mesurable : la chaîne est documentée à ses deux bouts (formule légale ↔ montant publié).

## 2. Faits atomiques préservés
- F-01 ✧ IRL (métropole continentale) : 148,37 au T2 2026 (+1,15 %) ; 146,60 T1 2026 (+0,78 %), 145,78 T4 2025 (+0,79 %), 145,77 T3 2025 (+0,87 %), 146,68 T2 2025 (+1,04 %) ; formule de révision = loyer actuel hors charges × IRL trimestre de référence / IRL même trimestre année précédente. EPI:FACT mem:823fd1be-29b5-4b48-baf3-449415b10ce4 [L302] (mesuré)
- F-02 ✦ L'indice qui indexe les loyers exclut les loyers : IRL = moyenne 12 mois de l'évolution des prix hors tabac et hors loyers ; règle énoncée à l'identique par l'administration (Service-Public, page vérifiée le 12 juillet 2026) et par l'ANIL. EPI:FACT mem:20845282-f990-4095-8311-6b2f8f1904d5 [L303] (mesuré)
- F-03 ✧ SMIC relevé au 1er juin 2026 par arrêté du 22 mai 2026 : 12,31 EUR/h en métropole et outre-mer listé, 9,56 EUR/h à Mayotte ; hausse de 2,41 % par déclenchement du mécanisme automatique lié à l'indice des prix des ménages modestes. EPI:FACT mem:4228e724-4f2b-4682-8a63-8f280c7470bb [L304] (mesuré)
- F-04 ✧ Metzing : recensement 2020 = 665 ; au 1er janvier 2024, Insee 678 vs services municipaux 791, écart >15 % ; la DGF est calculée sur la base du niveau de population ; réponse ministérielle du 24 juin 2025. EPI:FACT mem:f9b89c63-8291-465a-a5d6-d3eb08aa7bf8 [L305] (mesuré)
- F-05 ✧ Méthode des populations de référence (<10 000 hab) : 1 an sur 5 résultats directs de terrain, 2 ans sur 5 évolution constatée, 2 ans sur 5 données fiscales ; population en vigueur depuis le 1er janvier 2025. EPI:FACT mem:1d16b90d-44d1-4ead-af82-db093f26f71c [L306] (mesuré)
- F-06 ✧ CNERP : réduction du décalage entre date de référence et date d'entrée en vigueur de 3 ans à 2 ans, recommandée et datée fin 2026. EPI:FACT mem:c938affe-393f-491e-b1c1-6a4cf57278bb [L307] (mesuré)
- F-07 ✧ Loi du 7 juin 1951 article 1 (version 2010) : le SSP comprend l'Insee et les SSM ; la liste annuelle des enquêtes est arrêtée par un arrêté du ministre chargé de l'économie ; indépendance professionnelle. EPI:FACT mem:65a43fee-3a97-4f44-b203-f5a7be625f89 [L308] (mesuré)
- F-08 ✧ Règlement (UE) 2019/1700 : cadre commun des statistiques européennes sur personnes et ménages ; considérant 5 : primordial que les indicateurs sociaux soient précis et comparables. EPI:FACT mem:713fca91-9332-4e2e-a2a8-e2b4dfd5a75e [L309] (mesuré)
- F-09 ✧ Coût par dixième de point d'inflation : base ~500 Md€ de prestations sociales indexées (pensions de base pour l'essentiel, prestations familiales, allocations logement, minima sociaux) ; coût d'indexation ~5 Md€ par POINT (presque 0,2 pt de PIB) ; ~0,3 Md€ de charge d'intérêts par dixième de point (division arithmétique signalée comme telle, pas un chiffre publié). EPI:FACT mem:a6b13073-b4e5-4a1a-bed1-877904424517 [L310] (mesuré)Traces registre : premier fait à la ligne 302, dernier à la ligne 310 de la source [L302-L310] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-009→F-09 (mesuré).

## 3. Acteurs nominaux
Insee ; Cour des comptes ; Agence France Trésor ; DGFiP ; DGCL ; ministère de l'Économie ; CNERP ; communes ; ANIL ; Service-Public.gouv.fr ; Eurostat.

## 4. Sources externes citées
JORF (arrêté SMIC 22-05-2026) ; question sénatoriale Metzing ; ANIL (révision loyers) ; Service-Public F13723 ; Legifrance (loi 1951 art 1, LEGIARTI000022405540) ; EUR-Lex (2019/1700) ; Fipeco (impact de l'inflation sur le déficit).

## 5. Chronologie datée
1989 : formule IRL. 2008-2025 : décrets de populations de référence. 2022 : plafond IRL. 2025 : populations de référence en vigueur. 24-06-2025 : réponse ministérielle Metzing. Fin 2026 : application du décalage 3→2 ans (CNERP). 22/01-06-2026 : arrêté SMIC (12,31 EUR/h). T2 2026 : IRL 148,37.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Formule légale (IRL hors loyers, SMIC sur les modestes) → indexation de montants de masse (loyers, salaires, pensions) → chaque dixième de point d'écart d'indice devient un montant (5 Md€/pt prestations, 0,3 Md€/0,1 pt dette). Preuves : F-02, F-03, F-09. Verrou : législatif. [L303, L304, L310] (mesuré)
- M2 (L2) : Estimation de population → décret → DGF : l'erreur de mesure d'une commune devient un flux budgétaire annuel (~9 800 EUR/an pour 113 hab, cas Metzing). Preuves : F-04, F-05, F-06. Verrou : légal, délai de correction lent (3→2 ans). [L305, L306, L307] (mesuré)

## 7. Verbatim et citations
- « le coût de l'indexation des prestations sociales est chiffré à environ 5 Md€ par point d'inflation, soit presque 0,2 point de PIB » (Fipeco, reformulation F-09) (estimé). [L310] (mesuré)
- « l'IRL est obtenu à partir de la moyenne, sur les douze derniers mois, de l'évolution des prix à la consommation hors tabac et hors loyers » (Service-Public/ANIL, reformulation F-02) (estimé). [L303] (mesuré)

## 8. Notes méthodologiques source
Aucun dispositif rhétorique de manipulation dans le corpus (DEM 0, BF 0, NUM 3) : la carte dialectique porte sur l'ampleur, pas sur l'intention. Le chiffre 0,3 Md€/0,1 pt est une division arithmétique signalée comme telle, pas une publication officielle. Fait négatif : le coût agrégé consolidé de l'indexation n'est publié nulle part.

## 9. Limites connues de cette extraction (case-limites)
Aucune simulation interne à l'administration accessible ; pas de publication unique consolidant les indexations ; les trois canaux non chiffrés (montants consolidés, effet net par ménage, simulation) restent non établis ; traces [Lxx] estimées.
