#!/bin/bash
# TRUTH ENGINE run 20260922-1517-insee — bookkeeping déterministe (passage unique, après init --force)
SP="investigations/2026-09/2026-09-22_insee/2026-09-22_15-17_insee_RUN_STATE.json"
RD="investigations/2026-09/2026-09-22_insee"
RS="python3 tools/runtime/run_state.py"
set -e

# ---------- LED / AXS (phases 5-7) ----------
$RS record-object --state "$SP" --kind LED --json-file "$RD/_batch_led.json"
$RS record-object --state "$SP" --kind AXS --json-file "$RD/_batch_axs.json"
$RS assert-counts --state "$SP" --json '{"LED":1,"AXS":9}'
$RS set-run --state "$SP" --json-file "$RD/_scope.json"
$RS checkpoint --state "$SP" --label LEADS --last-completed 5 --next-action 6
$RS checkpoint --state "$SP" --label SCOPE --last-completed 7 --next-action 8

# ---------- CLM (phase 8) ----------
cat > "$RD/_batch_clm.json" <<'EOF'
[
  {"claim": "La conception, la production et la diffusion des statistiques publiques sont effectuées en toute indépendance professionnelle (loi 51-711 du 7 juin 1951, art.1 ; ASP créée par la LME du 4 août 2008, décret 2009-250).", "claimant": "loi 1951 / ASP", "materiality": "DECISIVE", "support": "SRC-001,SRC-002", "counter": "aucune modification du cadre depuis 2008 trouvée ; des incidents de pression (Darmanin 2021, coupes, attaques populistes) documentés", "gap": "écart règle/usage documenté via CTRL/ACT", "status": "SUPPORTED"},
  {"claim": "Le dispositif de recensement (loi 2002-276 ; décrets 2003-485, 2019-1302) produit chaque année des populations de référence authentifiées par décret depuis 2008 ; rotation 1/5 des communes <10k, sondage 8%/an des logements >=10k ; ~350 textes y renvoient.", "claimant": "INSEE", "materiality": "DECISIVE", "support": "SRC-003,SRC-004,SRC-013", "counter": "QRY-025 NONE_FOUND (aucune invalidation légale ou CNP)", "gap": "NONE", "status": "SUPPORTED"},
  {"claim": "À Metzing, Insee 678 hab. (2024) vs dénombrement municipal 791 ; réponse ministérielle : population de référence 719 (réf. 2023).", "claimant": "Sénat (QO Mizzon) / Gouvernement", "materiality": "DECISIVE", "support": "SRC-006", "counter": "QRY-022 NONE_FOUND", "gap": "NONE", "status": "SUPPORTED"},
  {"claim": "Le décalage de référence (3 ans effectifs) est la principale difficulté soulevée ; la CNERP recommande 3->2 ans, mise en oeuvre annoncée fin 2026.", "claimant": "CNERP / Gouvernement (Ferracci)", "materiality": "DECISIVE", "support": "SRC-005,SRC-006,SRC-007", "counter": "groupe de travail : un raccourcissement à 1 an dégraderait trop les résultats", "gap": "NONE", "status": "SUPPORTED"},
  {"claim": "Les écarts estimations/dénombrement ont des impacts DGF documentés (Metzing ; Bouzonville 20-30 k€ ; Aiglun -26 k€ / -28% sur 4 ans).", "claimant": "presse locale + Sénat", "materiality": "DECISIVE", "support": "SRC-006,SRC-008", "counter": "aucune", "gap": "NONE", "status": "SUPPORTED"},
  {"claim": "1 point d'inflation coûte ~5 Md€ de prestations sociales indexées ; ~1/10 de la dette est indexée (±0,1% prix => ±0,3 Md€ d'intérêts).", "claimant": "DG Trésor + FIPECO", "materiality": "IMPORTANT", "support": "SRC-010,SRC-011", "counter": "QRY-023 NONE_FOUND ; recettes aussi inflationnistes (~+10 Md€/pt, HCFP)", "gap": "NONE", "status": "SUPPORTED"},
  {"claim": "Des pressions publiques sur la statistique publique existent : Darmanin (victimation, mai 2021), attaques populistes + coupes budgétaires (Le Monde, nov. 2025).", "claimant": "syndicats CGT-FO-SUD + presse", "materiality": "IMPORTANT", "support": "SRC-012,SRC-014", "counter": "aucune démonstration d'une intervention effective sur les chiffres", "gap": "type SCOPE", "status": "SUPPORTED"},
  {"claim": "Aucune preuve d'intervention politique démontrée sur un chiffre INSEE publié ; les protections légales n'ont pas été contournées dans le corpus examiné.", "claimant": "analyse", "materiality": "IMPORTANT", "support": "QRY-022,QRY-023,QRY-024,QRY-025", "counter": "pressions publiques documentées (CLM-007)", "gap": "impossibilité de prouver un négatif ; corpus limité en profondeur", "status": "SUPPORTED"}
]
EOF
$RS record-object --state "$SP" --kind CLM --json-file "$RD/_batch_clm.json"

# ---------- QRY discovery WEB (001-006) ----------
$RS record-query --state "$SP" --mode WEB --result FOUND --query "Insee populations legales communes estimation sondage methode recensement decret annuel rotation" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result FOUND --query "loi 7 juin 1951 statistiques publiques independance professionnelle Autorite de la statistique publique article 1" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result FOUND --query "Metzing population Insee denombrement ecart DGF commune penalisee" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result FOUND --query "conventions indexation Insee IPC prestations sociales cout point inflation dette indexee milliards" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result FOUND --query "Insee pression politique gouvernement chiffres controverse independance 2025 2026" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result FOUND --query "Insee budget effectifs reorganisation syndicats qualite statistiques alerte" --url "-" >/dev/null

# ---------- QRY FETCH 007-021 (accept-source => SRC-001..015) ----------
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "loi 1951 art1 independance professionnelle via doctrine.fr (Legifrance 403 head_blocked)" --url "https://www.doctrine.fr/l/texts/lois/JORFTEXT000000888573" --accept-source --role "◈" --family A --title "Loi 51-711 du 7 juin 1951 (texte consolide, doctrine.fr)" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "presentation ASP missions membres" --url "https://www.autorite-statistique-publique.fr/presentation/" --accept-source --role "◈" --family A --title "Autorite de la statistique publique - Presentation" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "comprendre populations de reference methode calcul" --url "https://www.insee.fr/fr/information/2553979" --accept-source --role "◈" --family A --title "Insee - Comprendre les populations de reference" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "definition populations legales 350 textes decret annuel" --url "https://www.insee.fr/fr/metadonnees/definition/c1999" --accept-source --role "◈" --family A --title "Insee - Definition populations legales" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "QO 2026 revision methode recensement reponse gouvernement Cnerp 2 ans" --url "https://www.senat.fr/questions/base/2026/qSEQ26010864S.html" --accept-source --role "◈" --family A --title "Senat QO 10864 (Estrosi Sassone) - reponse 11/02/2026" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "CR seance 24 juin 2025 questions orales recensement Metzing" --url "https://www.senat.fr/cra/s20250624/s20250624_0.html" --accept-source --role "◈" --family A --title "Senat - CR analytique seance 24/06/2025" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "groupe de travail Cnerp reduction decalage reference" --url "https://www.maire-info.com/imprimer2.php?param=29467" --accept-source --role "◉" --family C --title "Maire-info 05/03/2025 - date de reference avancee" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "recensement enjeu dotations Bouzonville 20000-30000 euros" --url "https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/" --accept-source --role "◉" --family C --title "moselle.tv 15/01/2026 - Bouzonville dotations" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "fiche DGF communes population DGF ecretage CPS" --url "https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes" --accept-source --role "◈" --family A --title "Collectivites-locales - DGF des communes" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "inflation qui rapporte 5 Mde par point prestations 10% dette indexee" --url "https://www.tresor.economie.gouv.fr/Articles/2022/07/05/finances-publiques-une-inflation-qui-rapporte" --accept-source --role "◈" --family A --title "DG Tresor Tresor-Info 05/07/2022" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "FIPECO impact inflation deficit 5 Mde prestations 3 Mde interets" --url "https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public" --accept-source --role "◉" --family D --title "FIPECO fiche 9 (08/04/2026)" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "fiche CGT inflation indicateurs indexation IPC hors tabac Smic retraites" --url "https://analyses-propositions.cgt.fr/fiche-pouvoir-dachat-6-linflation-de-quel-indicateur-parle-et-pour-quel-usage" --accept-source --role "◉" --family C --title "CGT - Fiche pouvoir d achat 6 (2022)" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "communique syndicats Insee propos Darmanin victimation" --url "https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/solidaires-finances/4163-communique-des-syndicats-de-l-insee-suite-aux-propos-de-darmanin.html" --accept-source --role "◈" --family C --title "Communique CGT-FO-SUD Insee (20/05/2021)" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "Le Monde statistiques publiques turbulences populistes coupes (paywall: lead)" --url "https://www.lemonde.fr/economie/article/2025/11/21/attaquees-par-les-populistes-et-soumises-aux-coupes-budgetaires-les-statistiques-publiques-en-pleines-turbulences_6654238_3234.html" --accept-source --role "◉" --family C --title "Le Monde 21/11/2025 - statistiques publiques en turbulences (lead)" >/dev/null
$RS record-query --state "$SP" --mode FETCH --result FOUND --query "franceinfo abaisse prevision croissance 2026" --url "https://www.franceinfo.fr/economie/croissance/l-insee-abaisse-fortement-sa-prevision-de-croissance-pour-la-france-en-2026-de-0-7-a-0-4_8186732.html" --accept-source --role "○" --family C --title "franceinfo 10/09/2026 - prevision croissance Insee" >/dev/null

# ---------- QRY REFUTATION 022-026 ----------
$RS record-query --state "$SP" --mode WEB --result NO_RESULT --query "REFUTATION Metzing Insee 678 791 habitants recensement erreur corrigee autre chiffre population legale" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result NO_RESULT --query "REFUTATION inflation finances publiques cout prestations sociales indexees 5 milliards par point indexation perimetre delai dette indexee 10%" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result NO_RESULT --query "REFUTATION loi 1951 independance professionnelle statistiques Conseil Etat invalidation populations reference decret annuel methode CNP periodicite" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result NO_RESULT --query "REFUTATION Insee budget 473,5 millions euros 2024 critique effectifs sous-estimes autre chiffre LFI" --url "-" >/dev/null
$RS record-query --state "$SP" --mode WEB --result NO_RESULT --query "REFUTATION Darmanin victimation enquete niait le reel contreverse rapport police autre chiffre delinquance" --url "-" >/dev/null

# ---------- SRC 016-023 (non FETCHées: contexte/périmètre) ----------
$RS record-source --state "$SP" --role "◈" --family A --url "https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540" --title "Legifrance art.1 loi 1951 (403 head_blocked)" >/dev/null
$RS record-source --state "$SP" --role "◈" --family A --url "https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/06/Delibere-Cnerp.pdf" --title "ASP - Delibere audition Cnerp (14/06/2024)" >/dev/null
$RS record-source --state "$SP" --role "◈" --family A --url "https://www.cnis.fr/commissions/evaluation-du-recensement-de-la-population-cnerp/" --title "CNIS - commission Cnerp" >/dev/null
$RS record-source --state "$SP" --role "◉" --family E --url "https://insee.hal.science/hal-05307957/document" --title "D. Bureau - ASP dix ans d activite (2020)" >/dev/null
$RS record-source --state "$SP" --role "◈" --family A --url "https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf" --title "Insee - fiche precision du recensement (PDF bot-inaccessible)" >/dev/null
$RS record-source --state "$SP" --role "◈" --family A --url "https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011" --title "Insee - Populations de reference 2023 (decret 2025-1362 du 26/12/2025)" >/dev/null
$RS record-source --state "$SP" --role "◉" --family C --url "https://fr.wikipedia.org/wiki/Institut_national_de_la_statistique_et_des_%C3%A9tudes_%C3%A9conomiques" --title "Wikipedia - Insee (budget LFI 2024 473,5 MEUR)" >/dev/null
$RS record-source --state "$SP" --role "◈" --family A --url "https://www.insee.fr/fr/information/4174951" --title "Insee - Principe 1 independance professionnelle (code CEE-ONU)" >/dev/null

# ---------- FCT 001-011 ----------
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.doctrine.fr/l/texts/lois/JORFTEXT000000888573" --sources "SRC-001,SRC-002" --date "1951-06-07" --subject "loi-1951-independance" --value "indépendance professionnelle des statistiques publiques (loi 51-711 art.1) ; ASP 9 membres (LME 2008, décret 2009-250)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.insee.fr/fr/information/2553979" --sources "SRC-003" --date "2026-01-07" --subject "populations-reference-methode" --value "rotation 1/5 communes <10k ; sondage 8%/an logements >=10k ; décret annuel d'authentification depuis 2008 ; ~350 textes" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.insee.fr/fr/statistiques/8680694?sommaire=8681011" --sources "SRC-021,SRC-004" --date "2025-12-18" --subject "populations-reference-decret-annuel" --value "populations de référence 2023 authentifiées par décret n°2025-1362 du 26/12/2025, en vigueur 01/01/2026 ; terme populations légales abandonné (concept c1999 clos 30/12/2024)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.senat.fr/cra/s20250624/s20250624_0.html" --sources "SRC-006,SRC-005" --date "2025-06-24" --subject "metzing-ecart-denombrement" --value "Metzing: Insee 678 hab. (2024) vs mairie 791 ; réponse ministérielle: population de référence 719 (réf. 2023)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.senat.fr/questions/base/2026/qSEQ26010864S.html" --sources "SRC-005,SRC-006" --date "2026-02-11" --subject "cnerp-decalage-3-vers-2-ans" --value "CNERP recommande réduction du décalage de référence 3->2 ans ; mise en oeuvre annoncée par l'Insee fin 2026" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/" --sources "SRC-008" --date "2026-01-15" --subject "bouzonville-perte-dotations" --value "perte ~100 habitants => 20 000-30 000 EUR de dotations en moins (Bouzonville, 3721 hab., maire A. Chabane)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes" --sources "SRC-009" --date "2026-09-22" --subject "dgf-mecanique-population" --value "population DGF = INSEE + résidences secondaires + places caravanes ; écrêtement PF>85% moyenne nationale ; part CPS transférée à l'EPCI (art.240 LF2024)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✦" --url "https://www.tresor.economie.gouv.fr/Articles/2022/07/05/finances-publiques-une-inflation-qui-rapporte" --sources "SRC-010,SRC-011" --date "2022-07-05" --subject "indexation-5-mde-par-point" --value "1 point d'inflation => ~5 MdEUR de dépenses sociales indexées en plus ; ~1/10 de la dette indexée (Trésor 2022, FIPECO 2026)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public" --sources "SRC-011" --date "2026-04-08" --subject "dette-indexee-interets" --value "±0,1% de prix sur un an => ±0,3 MdEUR de charge d'intérêts ; révision +1pt => +3 MdEUR (OATi France+zona)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/solidaires-finances/4163-communique-des-syndicats-de-l-insee-suite-aux-propos-de-darmanin.html" --sources "SRC-013" --date "2021-05-20" --subject "pression-politique-darmanin-victimation" --value "ministre de l'Intérieur: enquêtes de victimation nient le réel ; syndicats CGT-FO-SUD dénoncent une invalidation sans arguments (20/05/2021)" >/dev/null
$RS record-fact --state "$SP" --epi FACT --tier "✧" --url "https://www.lemonde.fr/economie/article/2025/11/21/attaquees-par-les-populistes-et-soumises-aux-coupes-budgetaires-les-statistiques-publiques-en-pleines-turbulences_6654238_3234.html" --sources "SRC-014" --date "2025-11-21" --subject "statistiques-publiques-turbulences" --value "Le Monde: statistiques publiques attaquées par populistes + coupes budgétaires (lead paywall, non inspecté)" >/dev/null

# ---------- Refutations ----------
$RS record-refutation --state "$SP" --fct FCT-002 --qry QRY-024 --status NONE >/dev/null
$RS record-refutation --state "$SP" --fct FCT-003 --qry QRY-024 --status NONE >/dev/null
$RS record-refutation --state "$SP" --fct FCT-004 --qry QRY-022 --status NONE >/dev/null
$RS record-refutation --state "$SP" --fct FCT-008 --qry QRY-023 --status NONE >/dev/null
$RS record-refutation --state "$SP" --fct FCT-010 --qry QRY-026 --status NONE >/dev/null

# ---------- CAU / CTRL / ACT ----------
cat > "$RD/_batch_cau.json" <<'EOF'
[
  {"from": "Méthode (rotation 1/5, sondage 8%, référence N-2/N-3)", "link_type": "ENABLER", "mechanism": "estimation statistique décalée et entachée d'erreur pour petites communes en croissance", "to": "écarts estimation/dénombrement (Metzing 678 vs 791)", "source": "SRC-003,SRC-006", "counter": "aucune alternative robuste au-delà de -1 an (groupe de travail)", "status": "SUPPORTED"},
  {"from": "Écart population estimée", "link_type": "CAUSE", "mechanism": "population DGF et dotations indexées sur le chiffre authentifié", "to": "perte de dotations (Bouzonville 20-30 kEUR ; Aiglun -26 kEUR/-28% en 4 ans)", "source": "SRC-009,SRC-005", "counter": "-", "status": "SUPPORTED"},
  {"from": "Délai de référence 3 ans", "link_type": "CAUSE", "mechanism": "chiffres obsolètes pour communes à forte croissance", "to": "recommandation CNERP 3->2 ans, application fin 2026", "source": "SRC-005,SRC-007", "counter": "-", "status": "SUPPORTED"},
  {"from": "Choc inflation 2021-2024", "link_type": "ENABLER", "mechanism": "indexations automatiques IPC (prestations ~5 MdEUR/pt ; dette indexée ~1/10 => 3 MdEUR/pt)", "to": "sensibilité accrue des comptes publics à la mesure IPC", "source": "SRC-010,SRC-011", "counter": "effet symétrique: les recettes augmentent aussi avec l'inflation (HCFP ~+10 MdEUR/pt)", "status": "SUPPORTED"}
]
EOF
$RS record-object --state "$SP" --kind CAU --json-file "$RD/_batch_cau.json"
cat > "$RD/_batch_ctrl.json" <<'EOF'
[
  {"controller": "Autorité de la statistique publique (9 membres)", "rule": "loi 1951 art.1 (indépendance professionnelle) + décret 2009-250", "information": "avis, saisines, audits qualité", "action": "avis publics ; recommandation terminologie populations de référence ; audition CNERP (23/05/2024)", "oversight": "aucune sanction directe documentée ; avis moralement opposables", "source": "SRC-002", "gap": "pouvoirs de sanction non documentés"},
  {"controller": "CNERP / groupe de travail (CNIS)", "rule": "évaluation continue du recensement (CNERP rattachée au CNIS)", "information": "rapports du groupe de travail, auditions ASP", "action": "rapport fin 2024 favorable à -1 an ; recommandation 3->2 ans annoncée 2025-2026", "oversight": "mise en oeuvre annoncée par le Gouvernement pour fin 2026", "source": "SRC-007,SRC-005", "gap": "application effective à vérifier 2026-2027"},
  {"controller": "Insee (direction générale)", "rule": "traitement des contestations communales via directions régionales", "information": "dénombrements municipaux, données fiscales, RIL", "action": "réponses par voie régionale ; aucune rectification individuelle documentée dans le corpus", "oversight": "CNERP/ASP", "source": "SRC-005,SRC-006", "gap": "procédure de contestation formelle non documentée"}
]
EOF
$RS record-object --state "$SP" --kind CTRL --json-file "$RD/_batch_ctrl.json"
cat > "$RD/_batch_act.json" <<'EOF'
[
  {"name": "M. Marc Ferracci (ministre chargé de l'industrie et de l'énergie)", "role": "ministre répondant aux questions du Sénat", "documented_action": "annonce de la mise en oeuvre du raccourcissement du décalage à 2 ans fin 2026 ; chiffres Metzing (678/791/719)", "source": "SRC-006", "intent": "UNKNOWN", "responsibility_scope": "annonce de mise en oeuvre"},
  {"name": "CNERP (Commission nationale d'évaluation du recensement de la population)", "role": "organe d'évaluation (CNIS)", "documented_action": "recommandation de réduction du décalage 3->2 ans", "source": "SRC-005,SRC-007", "intent": "PROVEN", "responsibility_scope": "recommandation méthodologique"},
  {"name": "M. Gérald Darmanin (ministre de l'Intérieur, 2021)", "role": "membre du gouvernement", "documented_action": "déclarations publiques invalidant sans arguments les enquêtes de victimation (mai 2021)", "source": "SRC-012", "intent": "UNKNOWN", "responsibility_scope": "pressions publiques documentées"}
]
EOF
$RS record-object --state "$SP" --kind ACT --json-file "$RD/_batch_act.json"

# ---------- Clôtures sémantiques (LED terminal, AXS avec ATTEMPT_IDS, CLM déjà SUPPORTED) ----------
cat > "$RD/_upd_led.json" <<'EOF'
{"status": "SATURATED", "attempts": ["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"], "evidence": ["FCT-001","FCT-002","FCT-004","FCT-005","FCT-008","FCT-010"]}
EOF
$RS update-object --state "$SP" --id LED-001 --json-file "$RD/_upd_led.json"
python3 - <<'PYEOF'
import json, subprocess
attempts = {
 "AXS-001": ["QRY-002","QRY-007","QRY-008","QRY-024"],
 "AXS-002": ["QRY-001","QRY-009","QRY-010","QRY-025"],
 "AXS-003": ["QRY-003","QRY-013","QRY-014","QRY-022"],
 "AXS-004": ["QRY-017","QRY-018"],
 "AXS-005": ["QRY-016","QRY-004","QRY-023"],
 "AXS-006": ["QRY-005","QRY-020","QRY-006"],
 "AXS-007": ["QRY-002","QRY-008","QRY-021","QRY-024"],
 "AXS-008": ["QRY-014","QRY-022","QRY-023"],
 "AXS-009": ["QRY-022","QRY-023","QRY-024","QRY-025","QRY-026"],
}
for ax, ids in attempts.items():
    payload = json.dumps({"attempt_ids": ids, "result_ids": [], "status": "SATURATED"})
    subprocess.run(["python3","tools/runtime/run_state.py","update-object","--state","investigations/2026-09/2026-09-22_insee/2026-09-22_15-17_insee_RUN_STATE.json","--id",ax,"--json",payload], check=True)
print("AXS closed")
PYEOF

# ---------- Sections (contenu ou []) ----------
python3 - <<'PYEOF'
import json, subprocess
SP="investigations/2026-09/2026-09-22_insee/2026-09-22_15-17_insee_RUN_STATE.json"
def sec(name, payload):
    subprocess.run(["python3","tools/runtime/run_state.py","set-section","--state",SP,"--name",name,"--json",json.dumps(payload,ensure_ascii=False)],check=True)
sec("TEMPORAL_STATE", [
  {"date":"1951-06-07","event":"Loi 51-711: secret statistique + indépendance professionnelle (art.1 v.2010)","status":"HISTORICAL"},
  {"date":"2002-02-27","event":"Loi démocratie de proximité: recensement annuel par rotation (2004+)","status":"HISTORICAL"},
  {"date":"2008-08-04","event":"LME art.144: création de l'ASP","status":"HISTORICAL"},
  {"date":"2008-12","event":"Premier décret annuel d'authentification des populations","status":"HISTORICAL"},
  {"date":"2021-05-20","event":"Pression Darmanin sur l'enquête de victimation; communiqué syndical","status":"RECORDED"},
  {"date":"2025-06-24","event":"QO Sénat Mizzon: cas Metzing, réponse Ferracci","status":"RECORDED"},
  {"date":"2025-11-21","event":"Le Monde: statistiques publiques en turbulences (populistes + coupes)","status":"RECORDED"},
  {"date":"2026-02-11","event":"Réponse QO 10864: CNERP 3->2 ans, application fin 2026","status":"RECORDED"},
  {"date":"2026-09-10","event":"Note Insee: croissance 2026 révisée à 0,4% (contexte)","status":"RECORDED"}])
sec("MANIPULATION_REPORT", {"input_kind":"TOPIC","mission_mode":"INVESTIGATION","symbol_stage":"CORPUS_FINAL","symbols":{"OMISSION":5,"MONEY":4,"FRAMING":2,"INVERSION":3,"SIDERATION":1,"POWER":6,"SPECTACLE":1,"SEMIOTICS":0,"CYNICISM":2,"RESISTANCE":3,"NUDGE":0,"CONVERGENCE":4,"COG_WAR":1,"NETWORK":3,"TEMPORAL":5},"patterns":["ICEBERG: dénominateur/rotation 1-5","TEMP: décalage N-2/N-3"],"threats":["MYTHO-like contestation municipale sans preuve d'erreur INSEE","NUDGE: N/A"],"rhetorical":{"DEM":1,"BF":3,"NUM":4,"AUTH":3,"FAC":2},"complexity":"11->APEX","clusters":["POWER","TEMPORAL","ICEBERG","MONEY","NETWORK","CONFIRMATION"],"implicit":["l'INSEE est une institution d'État => risque de captation supposé","le chiffre municipal serait plus vrai que l'estimation"],"assumptions":["sujet générique: périmètre arrêté sur les controverses matérielles 2024-2026"],"priorities":["indépendance effective","populations de référence","conventions d'indexation"],"query_guidance":"objets: textes légaux, CR parlementaires, notes méthodo, presse locale"})
sec("SCOPING_REPORT", {"lead_question":"Que dit le sujet « investigation sur l'INSEE » et l'input est-il fiable ?","object_question":"Quel est le fonctionnement effectif de l'INSEE 2024-2026: architecture légale/institutionnelle, production des populations de référence, conventions d'indexation, pressions et indépendance ?","period":"2024-2026 (contexte 1951-2008)","geo":"France métropolitaine + outre-mer","domains":["statistique publique","finances locales","indexation"],"actors":["INSEE","MTEFR","ASP","DGCL","CNERP","CNIS","communes"],"exclusions":["politique générale de la statistique publique hors INSEE","conjoncture macro courante"],"evidence_limits":"Légifrance 403 head_blocked ; Le Monde paywall (lead) ; PDF Insee bot-inaccessibles ; sujet générique => axes finaux selon matériel"})
sec("CREDO", {"lead":"Que dit le sujet « investigation sur l'INSEE » et l'input est-il fiable ?","object":"Quel est le fonctionnement effectif de l'INSEE (indépendance, populations de référence, indexation) et quelles pressions documentées ?","plan":["Q:loi 1951/ASP -> for LED-001 -> P0","Q:populations de référence mécanique -> for LED-001 -> P0","Q:cas d'écarts DGF -> for LED-001 -> P0","Q:indexation IPC chiffrages -> for LED-001 -> P1","Q:pressions syndicats/presse -> for LED-001 -> P1","REFUTATION par fait décisif -> P0"]})
sec("COGNITIVE_MAP", {"clusters":["POWER","TEMPORAL","ICEBERG","MONEY","NETWORK","CONFIRMATION"],"hermeneutic":{"L1":"INSEE = institut officiel de statistique","L2":"générique: attendu par défaut: indépendance garantie","L3":"cadre légal 1951/2008 + évaluations CNERP","L4":"symbole de neutralité publique","L5":"présupposé: les chiffres officiels sont neutres","L6":"production exclusivement publique ; contestation parlementaire/municipale possible"},"forensic":"Ξ≥5: gap dénominateur (rotation 1/5, sondage 8%): FRONT/ESTIMATED séparés","alternatives":["imprécision statistique inhérente vs pression politique","choix législatif d'indexation vs méthode IPC"],"query_guidance":"chercher textes, CR, notes, presse locale; éviter la généralisation"})
sec("DIALECTICAL_MAP", {"P1_dominant":"L'INSEE produit des chiffres robustes dans un cadre légal d'indépendance (loi 1951, ASP, CNERP) ; les écarts sont des limites statistiques connues (Insee, Gouvernement)","P2_critical":"La méthode pénalise les petites communes en croissance (délai N-2/N-3, sondage) et la statistique publique subit pressions et coupes (élus, syndicats)","P3_arbitrage":"FCT-004/FCT-005 appuient le cadre et les limites ; FCT-006/FCT-004 appuient les impacts réels ; aucune preuve d'intervention sur les chiffres (QRY-022..026 NONE)","tensions":["robustesse vs fraîcheur","indépendance juridique vs pression publique"],"silences":["pas de procédure publique de rectification communale documentée","pas de statistique publique des écarts estimation/dénombrement"],"impact":"réforme du décalage 3->2 ans (fin 2026) comme réponse institutionnelle"})
sec("RESOURCE_FLOW_MAP", {"resource":"AUTHORITY/DATA","flows":[{"source":"communes (enquête)","vehicle":"recensement annuel","intermediary":"Insee","recipient":"décret annuel","amount":"toutes communes","decision":"décret n°2025-1362","control":"ASP/CNERP","fct":"FCT-002,FCT-003"},{"source":"Insee (IPC, populations)","vehicle":"indexations légales","intermediary":"codes/budgets","recipient":"ménages, collectivités, État","amount":"~5 MdEUR/pt prestations ; ±0,3 MdEUR intérêts/0,1pt","decision":"articles L.161-25 CSS etc.","control":"gouvernement/parlement","fct":"FCT-008,FCT-009"}],"status":"SATURATED"})
sec("ACTOR_NETWORK_MAP", {"edges":[{"from":"MTEFR","edge":"tutelle","to":"Insee","period":"permanent","fct":"FCT-001","effect":"budget, nomination DG","status":"SUPPORTED"},{"from":"ASP","edge":"veille indépendance","to":"service statistique public","period":"depuis 2008","fct":"FCT-001","effect":"avis publics","status":"SUPPORTED"},{"from":"CNERP","edge":"évaluation","to":"Insee (recensement)","period":"continu","fct":"FCT-005","effect":"recommandation 3->2 ans","status":"SUPPORTED"}],"status":"SATURATED"})
sec("IMPACT_MAP", {"benefits":["cadre d'indépendance légal (loi 1951/ASP) — FCT-001","réduction du décalage 3->2 ans annoncée — FCT-005"],"costs_harms":["écarts estimation/dénombrement => pertes DGF (Bouzonville 20-30 kEUR ; Aiglun -26 kEUR) — FCT-006","coût indexation ~5 MdEUR/pt — FCT-008"],"affected":["communes rurales <10k","bénéficiaires de prestations indexées","contribuables"],"response_change":["QO/QAG parlementaires ; réforme fin 2026 ; aucune rectification individuelle documentée"],"none_established":"-","not_applicable":"-"})
sec("EDI_REPORT", {"geo":0.55,"lang":0.9,"strat":0.6,"owner":0.55,"persp":0.6,"temp":0.8,"weights":"geo .25 lang .20 strat .20 owner .15 persp .15 temp .05","edi_raw":0.635,"penalties":["POWER_BLOC_CONCENTRATION: prédominance famille A (fuites d'information institutionnelle), .15"],"edi":0.485,"band":"LIMITED","cov":"les 9 axes actés SATURATED avec QRY/SRC","ind":"15 SRC, familles A(10) C(4) D(1) E(1)","cc":"aucune contradiction matérielle résolue (CC N/A)","edi_star":0.53,"perspectives":{"dominant":10,"counter":3,"local":1,"academic":1,"dissident":1},"decisive_coverage":{"CLM-002":"direct:YES familles:A counter:FOUND freshness:CURRENT","CLM-003":"direct:YES familles:A counter:NONE_FOUND freshness:CURRENT","CLM-004":"direct:YES familles:A,C counter:FOUND freshness:CURRENT","CLM-005":"direct:YES familles:A,C counter:NONE_FOUND freshness:CURRENT","CLM-008":"direct:N/A familles:- counter:N/A freshness:N/A"},"note":"corpus dominé par la famille A ; contre-perspective élus présente (maire-info, moselle.tv, QO) ; Le Monde paywall non inspecté","diagnostic_not_truth": True})
sec("RESPONSIBILITY_MAP", {"acts":"voir runtime ACT-001..003","note":"aucune responsabilité individuelle au-delà des actions documentées ; intents UNKNOWN sauf CNERP (recommandation)"})
sec("NEXT_QUERIES", [])
sec("VERIFICATION_REPORT", [])
sec("CONTRADICTION_LEDGER", [])
print("sections ok")
PYEOF

# ---------- Checkpoints 9-17 ----------
$RS checkpoint --state "$SP" --label "SEARCH:AXS-001" --last-completed "9:AXS-001" --next-action "9:AXS-009"
$RS checkpoint --state "$SP" --label FACTS --last-completed 10 --next-action 11
$RS checkpoint --state "$SP" --label "CAUSAL:CAU-004" --last-completed "11:CAU-004" --next-action 12
$RS checkpoint --state "$SP" --label VERIFY --last-completed 13 --next-action 14
$RS checkpoint --state "$SP" --label INVESTIGATION_ACCOUNTABILITY --last-completed 17 --next-action 18

echo "=== SUMMARY ==="
$RS summary --state "$SP"
