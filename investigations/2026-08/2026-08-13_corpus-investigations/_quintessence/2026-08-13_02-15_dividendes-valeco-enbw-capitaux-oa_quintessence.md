# Quintessence : dividendes VALECO REN vers EnBW et valeur capitalisée des OA

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-10_21-50_dividendes-valeco-enbw-capitaux-oa_INVESTIGATION.md` (97 lignes, 15 FCT-dv)
Date extraction : 2026-08-13 02:15 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé axe de piste, axe A suite 20-26/20-36/21-30
- **Date source** : 2026-08-10 21:50 CEST, STATE FINAL
- **Complexité** : quantification + manipulation report (15 symboles, score +7/30)
- **Identifiants source** : 15 FCT-dv-001 à 015, 5 GAP-dv
- **Object** : quantifier les dividendes VALECO REN vers EnBW (2023-2025) et la valeur capitalisée des contrats OA rachetés en 2019 [L11 (mesuré)]

## 2. Faits atomiques préservés

- FCT-dv-001 : VALECO REN : résultat net 75,3 M€ (2022), 3,11 M€ (2023), 2,33 M€ (2024), 2,08 M€ (2025) ; CAF = RN à 100 % [L21 (mesuré)]
- FCT-dv-002 : VALECO REN = holding pure de dividendes : CA 1,51 K€, EBITDA -58,9 K€ [L22 (mesuré)]
- FCT-dv-003 : actionnariat 03/06/2019 : VALECO SAS 51 % / FPCI Mirova Eurofideme 3 49 % ; sortie du FPCI postérieure (2021-2022) [L23 (mesuré)]
- FCT-dv-004 : réorganisation 2021-2022 : DAHLIA HOLDING (100 % VALECO REN), apport Bois de Merdelou, PV « Reconstitution de l'actif net » 07/07/2022 [L24 (mesuré)]
- FCT-dv-005 : portefeuille : 20+ filiales (Puech del Vert, Bois de Merdelou, L'Ensinet, Fenouilledes, La Bruyère, La Chaussée, Tuchanais, centrales solaires, etc.) [L25 (mesuré)]
- FCT-dv-006 : EnBW a racheté 100 % de Valeco en 2019 : prix officiel ~229 M€ (earnings call Q1-2019) ; 300-400 M€ (Figaro, dette/pipeline inclus) ; clôture 03/06/2019 [L26 (mesuré)]
- FCT-dv-007 : Valeco 2019 : 332 MW en exploitation (276 éolien + 56 solaire), pipeline 1 700 MW, ~300 ETP, CA ~30-50 M€/an [L27 (mesuré)]
- FCT-dv-008 : EnBW groupe : EBITDA renouvelables 1,31 Md€ (2023), ~1,2 Md€ (2024) ; capacité ~8 100 MW [L28 (mesuré)]
- FCT-dv-009 : les dividendes Valeco vers EnBW ne sont pas ventilés publiquement (constat) [L29 (mesuré)]
- FCT-dv-010 : flux OA brut portefeuille Valeco : 620 GWh/an × 82 €/MWh = ~50,8 M€/an ; écart au marché ~35 €/MWh = ~21,7 M€/an de subvention nette [L30 (mesuré)]
- FCT-dv-011 : capitalisation de l'écart au marché : ~168 M€ (10 ans, 5 %) à ~225 M€ (15 ans, 5 %) [L31 (mesuré)]
- FCT-dv-012 : le prix de 229 M€ (2019) est cohérent avec la capitalisation (168-225 M€) + pipeline + valeur hors OA [L32 (mesuré)]
- FCT-dv-013 : dividendes potentiels 2023-2025 : 7,52 M€ cumulés (3,11 + 2,33 + 2,08) si distribution à 100 % [L33 (mesuré)]
- FCT-dv-014 : part vers EnBW : ≥ 51 % (VALECO SAS), potentiellement 100 % après sortie du FPCI Mirova [L34 (mesuré)]
- FCT-dv-015 : la part Valeco dans EnBW est minoritaire : < 0,3 % de l'EBITDA renouvelables EnBW [L35 (mesuré)]

## 3. Acteurs nominaux

**Entreprises** : VALECO REN (434054318), VALECO SAS (421377946), EnBW AG (Land de Bade-Wurtemberg, ~99 % public), FPCI Mirova Eurofideme 3, DAHLIA HOLDING, famille Gay, CDC/Banque des Territoires, EDF OA.

## 4. Sources externes citées

Pappers (fiche financière VALECO REN, téléchargée), verif.com, rapport EnBW 2023-2024, earnings call EnBW Q1-2019, Figaro (20-36), calculs /tmp/calc_valeco_flux.py.

## 5. Chronologie datée

2019 : rachat EnBW (clôture 03/06), actionnariat VALECO REN 51/49 ; 2021-2022 : sortie FPCI Mirova, réorganisation DAHLIA ; 2022 : pic 75,3 M€ ; 2023-2025 : 3,11 / 2,33 / 2,08 M€.

## 6. Mécanismes / chaînes causales

**M1 — La capitalisation de la subvention publique** : EnBW a acheté en 2019 un portefeuille dont 168-225 M€ correspondent à la capitalisation de l'écart de soutien public restant ; le contribuable finance des flux capitalisés au profit du cédant (famille Gay + CDC, TRI 28 %) puis d'un actionnaire public allemand jusqu'à l'échéance des OA (2032 pour PDV). Niveau : L2. [L30-L32 (mesuré)]
**M2 — La pompe à dividendes comme mécanisme, pas comme volume** : holding pure (CA 1,51 K€, 20+ filiales parcs), flux récurrent réel 2-3 M€/an (7,52 M€ cumulés), pic 2022 = événement unique de réorganisation. Niveau : L2. [L21-L25 (mesuré)]
M3 : non identifié dans la source.

## 7. Verbatim et citations

- « Le vrai trou de contrôle reste le GAP du 21-10 (CRIM non captée, bouclier non recapté), pas les dividendes Valeco » [L86 (mesuré)]
- Charge correcte : « transfert de souveraineté légal et quantifié », 0 élément pénal [L85 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : Pappers + earnings call EnBW ; calculs documentés (script) ; manipulation report 15 symboles, score net +7/30 (faisceau faible à modéré).
- **F-##** : 15/15 identifiants FCT-dv-001 à 015 préservés verbatim.
- **INCONNU** : politique de distribution (PV d'AG non lues, GAP-dv-1).

## 9. Limites connues (case-limites)

- GAP-dv-1 à 5 : affectations 2023-2025, sortie du FPCI Mirova, dividendes des filiales, valeur du pipeline, part exacte de la subvention dans le prix (DCF non public).
- Le flux de dividendes est modeste (2-3 M€/an) : la « pompe » est un mécanisme documenté, pas un détournement massif.
- Les « 87 Md€ d'engagements » sont l'ensemble du parc français, pas la part Valeco (332 MW sur ~30 GW) : ne pas attribuer.
