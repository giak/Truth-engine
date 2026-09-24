# QUINTESSENCE : insee-biais-modes-calcul-fresque-systemique
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_insee-biais-modes-calcul-fresque-systemique/2026-09-20_17-04_insee-biais-modes-calcul-fresque-systemique_INVESTIGATION.md (RUN_ID 20260920-1704, ENGINE 2.10.6, COMPLEXITY 17 APEX, G0-G10 PASS, certification DELIVERY PASS par UPDATE 20260921-1015)

## 1. Métadonnées & trace source
Investigation TOPIC, fresque systémique 1946-2026 (focus 2004-2026), France. 28 sources inspectées, 5 familles. 9 faits, 47 requêtes, 7 checkpoints. Verdict sur le lead « l'Insee ne reflète pas la réalité » : partiellement étayé et partiellement réfuté (L~30-35, estimé). Le sujet réel est une convention de mesure enchâssée dans des intérêts d'indexation, pas un complot de chiffres.

## 2. Faits atomiques préservés
- F-01 ✦ Inflation perçue (OPI, CAMME, ~2000 ménages) : ~6 points au-dessus de l'IPC en moyenne depuis 2004 ; l'Insee et la Banque de France attribuent l'écart à la surpondération des prix en hausse et à forte fréquence d'achat, et reconnaissent que l'OPI possède des bases objectives. EPI:FACT mem:a995399b-01e8-4dc8-bb2f-d0a7ef05cf94 [L380] (mesuré)
- F-02 ✧ Le DG de l'Insee est nommé en Conseil des ministres (art. 13 Constitution) ; Lenglart nommé le 5 juin 2025 sur proposition de Bercy, succède à Tavernier (2012-2025) ; profil X-ENSAE, ex-DREES, France Stratégie, Trésor. EPI:FACT mem:8b6fd4b4-def1-41e9-bbac-dde456f7ee35 [L381] (mesuré)
- F-03 ✦ Croissance 2023 : 0,9 % (janvier 2024) révisée à 1,4 % (mai 2025, base 2020) puis 1,9 % corrigé des jours ouvrés (compte définitif, juin 2026) : révision cumulée ~1 point, la plus forte depuis 2003. EPI:FACT mem:82daeeca-eb22-4adf-859e-0a349c7fb025 [L382] (mesuré)
- F-04 ✧ IRL = moyenne 12 mois de l'IPC hors tabac et hors loyers ; T2 2026 : +1,15 % sur un an. EPI:FACT mem:0c83fb4e-3cc8-485c-9e4b-719f44ad830c [L383] (mesuré)
- F-05 ✦ L'IPC français exclut le coût du logement des propriétaires occupants (loyers imputés), comme l'HICP : méthode qu'Eurostat qualifie elle-même de « trop étroite » ; l'Allemagne (20,7 %), les USA (23,5 % + 7,6 % réels) et le Royaume-Uni (CPIH) l'incluent ; l'IPC français inclut en revanche la santé remboursée (indice hybride). EPI:FACT mem:bb187cdb-bd17-4b57-9f6e-ea949dcc0a11 [L384] (mesuré)
- F-06 ✧ SMIC revalorisé au 1er janvier sur l'inflation des 20 % des ménages les plus modestes ; hausse automatique en cours d'année si IPC +2 % ; adéquation ex post contestée selon les sous-périodes. EPI:FACT mem:ba618622-71eb-4d6e-a818-43bc9bf264f0 [L385] (mesuré)
- F-07 ✧ Loi du 7 juin 1951 (art. 1, version 2010) : indépendance professionnelle, création de l'Autorité de la statistique publique (9 membres). EPI:FACT mem:324d3e38-37f0-405f-9e09-b758eb96ae3f [L386] (mesuré)
- F-08 ✧ Circulation des cadres : biographie Lenglart (X1989, ENSAE 1994) documente Insee-Trésor-Prévision-France Stratégie-DREES-Insee sur trois décennies. EPI:FACT mem:fdee4b44-2d92-4453-84a9-3f7e83212151 [L387] (mesuré)
- F-09 ✧ Pauvreté 2024 : 9 817 000 personnes au seuil 60 % (ERFS) ; taux 15,4 %, plus haut mesuré de la série récente. EPI:FACT mem:16e14263-b2a3-45bf-99f2-4248944c98cf [L388] (mesuré)Traces registre : premier fait à la ligne 380, dernier à la ligne 388 de la source [L380-L388] (mesuré).
Inventaire source : FCT-001→F-01, FCT-002→F-02, FCT-003→F-03, FCT-004→F-04, FCT-005→F-05, FCT-006→F-06, FCT-007→F-07, FCT-008→F-08, FCT-009→F-09 (mesuré).

## 3. Acteurs nominaux
Insee ; ministère de l'Économie (Bercy) ; Autorité de la statistique publique (ASP) ; Eurostat ; Banque de France ; Fabrice Lenglart ; Jean-Luc Tavernier ; DGFiP ; UFC-Que Choisir ; chercheurs (François Geerolf) ; presse économique.

## 4. Sources externes citées
Loi du 7 juin 1951 ; manuel HICP/Eurostat ; base 2020 des comptes nationaux ; enquête CAMME (Banque de France) ; blog Geerolf (IPC/loyers) ; Que Choisir ; OFCE ; La Vie des idées ; Le Grand truquage (2009, pressions documentées, contexte) ; budget programme 220 (472,5 M€ d'AE 2025, -2,7 %).

## 5. Chronologie datée
1833 : début statistique publique continue. 1946 (27 avril) : création Insee (loi de finances) ; Closon DG 1946-1961. 1951 : loi obligation/secret. 1974-1987 : Malinvaud. 1996 : IPCH européen. 2008 : création ASP (loi LME). 2009 : règlement 223/2009. 2012-2025 : Tavernier. 2020-2022 : épisode inflation, débat ressenti/mesuré. 2023 (janvier) : première estimation 0,9 %. 2025 (juin) : Lenglart DG. 2026 (juin) : compte définitif 1,9 % ; IPC base 2025 ; taux de pauvreté 15,4 % ; fusion des corps ISED (1er décembre 2025).

## 6. Mécanismes / chaînes causales
- M1 (L2) : Convention de champ IPC (exclusion des loyers imputés) → indice phare sous-pondère le poste le plus dynamique du coût de la vie → écart structurel avec la perception. Preuves : F-05, F-01. Verrou : convention légale/statistique. [L384, L380] (mesuré)
- M2 (L2) : IPC = indexeur légal (SMIC, IRL, pensions, contrats) → chaque choix de champ ou de formule se convertit en montants (F-04, F-06) ; formule IRL excluant les loyers de leur propre indexation. Verrou : législatif. [L383] (mesuré)
- M3 (L3) : Enchâssement organisationnel : nomination en Conseil des ministres sur proposition de Bercy (F-02), canal X-ENSAE-Trésor (F-08), budget voté en loi de finances → proximité structurelle sans délit documenté. Verrou : institutionnel. [L381] (mesuré)
- M4 (L2) : Révisions à biais haussier moyen +0,34 pt (2005-2024) → le premier chiffre structure le récit public avant correction (F-03). Verrou : méthodologique/calendaire. [L382] (mesuré)

## 7. Verbatim et citations
- « trop étroite » : qualification par Eurostat de la méthode excluant les loyers imputés (citation rapportée par la source F-05) (estimé). [L384] (mesuré)
- « en trompe-l'œil » : qualification par l'Insee du recul du chômage 2020 (héritée du corpus, FCT-001 chaîne) (estimé).
- « en grande partie » à l'imprécision du volume en contexte inflationniste : attribution Insee de la révision 2023 (F-03) (estimé). [L382] (mesuré)

## 8. Notes méthodologiques source
Statut : investigation TOPIC certifiée (G0-G10 PASS). Familles : A dominante (structurelle pour un objet étatique, pénalité EDI documentée : 0,42 vs cible 0,80, GAP_SEVERITY ≈ 0,045). Contestés ⊙ : ampleur de l'effet logement, caractère exceptionnel des révisions, effectivité de l'indépendance. Hypothèse ⁂ non falsifiable au run : alignement d'intérêts entre conventions de champ et payeurs d'indexations (Scénario B). Réfuté ❧ : la lecture « l'IPC prétend mesurer le coût de la vie » (portée à l'usage médiatique, pas à l'institution). Aucun mécanisme de manipulation micro documenté.

## 9. Limites connues de cette extraction (case-limites)
Traces [Lxx] estimées (digest, pas de re-lecture intégrale). Archives internes Insee inaccessibles ; ampleur budgétaire exacte des indexations non établie au run source (clos ensuite par indexation-conventions) ; rapport ASP intégral et peer review HAL bloqués à l'accès.
