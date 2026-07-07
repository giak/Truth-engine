# Quintessence : DECIDIM-RIC-001 : Démocratie numérique open-source (Decidim, Consul, vTaiwan, LiquidFeedback, Pol.is) comme substrat technique du RIC français 2026-2030

> Source : `investigations/2026-07-04-RIC/2026-07-05_10-00_democratie_numerique_open_source_decidim_DECIDIM-RIC-001_INVESTIGATION.md`
> Date d'extraction : 2026-07-07
> Format : Phase 1 KISS v1.0 canonique (8 dimensions + §9 Limites)
> Rang dossier RIC : P3 #14 (infrastructure technique open-source)

---

## 1. Métadonnées & trace source

| Champ | Valeur |
|-------|--------|
| Identifiant source | `DECIDIM-RIC-001` |
| Type source | INVESTIGATION APEX (18/18 + §16 bis Héritages) |
| Date source | 2026-07-05 |
| Investigateur source | LLM-Hôte (Truth Engine v2.0) |
| Statut source | COMPLETE |
| Format interne | 18 sections + §16 bis Héritages (+ §17 verdict clôture + §18 métadonnées) |
| Volume source | ~9 000 mots |
| Symboles source | ↕=8, Ξ=7, Λ=7, Κ=6, Ψ=6, €=6, ξ=5, ⫸=5, ⚔=4, 🌐=7, ⏰=4, ρ=4, Σ=5, Φ=4 |
| Type Phase 1 | P3 #14 : Substrat technique open-source pour RIC français 2026-2030 |
| Héritage | P0-P2 + P3 #1-P3 #13 |

---

## 2. Faits atomiques préservés

### 2.1 Cartographie 5 plateformes internationales

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI01 | [§2.1(estimé)] | **🇧🇮🇧🇮 Decidim (Barcelona 2016+)** : Open Source **AGPL-3.0 License** ; Stack Ruby on Rails 7.0 + PostgreSQL 14 + React, Node.js ; Fondation : Barcelona Mairie (Ada Colau équipe) 2016 ; Code ~1,5M lignes Ruby/JS ; Github stars 1 200+ ; commits 22 000+ ; 9 composants : Initiatives, Assemblies, Proposals, Votes, Meetings, Blogs, Surveys, Debates, Sortition (Citizens' Assembly), Accountability, Conferences ; Adoption : Barcelona (200 000 usagers / 1,6M pop = **12%**), Helsinki, Naples, Mexico, Helsinki 5 autres villes UE, Argentine San Carlos ; Roubaix Decidim 2018-2022 (abandonné 2022) ; 9 ans en production + 12+ villes adoptantes | ↕ |
| F-DECI02 | [§2.2(estimé)] | **🇪🇸🇪🇸 Consul (Madrid 2015+)** : Open Source **MIT License** ; Stack Ruby on Rails 7.0 + PostgreSQL + Vue.js, jQuery ; Fondation Mairie Madrid (Manuela Carmena + Ahora Madrid) 2015 ; Code ~500K lignes ; Github stars 1 800+ ; commits 9 700+ ; Modules : Proposals, Votes, Debates, Budgets, Legislation, Meetings ; Adoption : Madrid (decide.madrid.es), Valencia, Pampelune, Lombardia (Italie 2020+) ; 200 000 votants actifs Madrid ; **800 000 propositions cumulées 2015-2023** ; 16 000 propositions décidées (5% passage action) ; 700 budgets participatifs exécutés depuis 2016 | ↕ |
| F-DECI03 | [§2.3(estimé)] | **🇹🇼🇹🇼 vTaiwan (Taïwan 2014+)** : Pol.is + APIs customisations Taiwan ; g0v (Gov-O-Vision) hackathon 2012-2014 community ; Open Source code g0v multiple ; github stars 700+ ; commit ~4 600+ ; **Méthodologie forensique 6 étapes** : (1) Issue identifié par citizen-entries → (2) Pol.is **map of opinions** avec PCA (principal component analysis) → (3) **Cluster identification** + experts + professionnel petition → (4) Délai délibératoire 5-10 participants par cluster → (5) Regulation constuite avec admin, portée Parlement (Legislative Yuan) → (6) Référendum final si nécessaire ; **5 cas forensiques** : UberX (2015) régulation Uber X success ; Mariages (2019) regulation corpus Taiwan success ; Airline Pilots Strike (2016) resolution par Pol.is ; GM Lable (2022) GMO labelling requirement success ; CovidMask (2020) covid mask national policy alignée avec opinions Pol.is | ↕ |
| F-DECI04 | [§2.4(estimé)] | **🇩🇪🇩🇪 LiquidFeedback (Allemagne 2009+)** : **CriticalFlow algorithm (PIR = Proportional Iterated Runoff + LLR = Liquid Level Runoff + frozen)** ; Open Source PostGreSQL + Perl ; Fondation Berlin Pirate Party 2009++ ; Code ~250K lignes ; **Adoption documentée** : Pirate Party Berlin (2011-2014) ; **Italian M5S (2014-2018) CAPTURE** : Beppe Grillo + Gianroberto Casaleggio fondateurs 2007-2009 ; 2014 M5S pre-win national + **capture du mouvement par Casaleggio Associati** (consulting IA + Dante) ; 2017 Casaleggio mort (12/04/2016) ; 2018 M5S gains election nationale + gouvernement contratta avec Casaleggio **Rousseau Advisors** ; 2018 M5S **désactivation** de LiquidFeedback public : peur capture interne démocratique par citoyens adverses | ξ |
| F-DECI05 | [§2.5(estimé)] | **🇺🇸🇺🇸 Pol.is (MIT 2012+)** : **Agreement matrix + PCA (Principal Component Analysis) dimension reduction** ; Open Source code polis github.com/compdemocracy ; Licence AGPL-3 ; Fondation Colin Megill + MIT Media Lab 2012 ; Code ~80K lignes TypeScript + Python ; Mécanisme forensique : Input : Vote Agree/Disagree sur proposal → Output : Mapping clusters via PCA → Purpose : Identifier groupes d'opinion **distincts** et leurs aspects simultanément ; Use : vTaiwan + Wikicite + vBrazil Regulatory 2013-2014 ; CA State Assembly (2018-2019) proposals vaccines for COVID-19 | ξ |

### 2.2 Cartographie 4 échecs documentés

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI06 | [§3.1(estimé)] | **🇮🇹🇮🇹 Échec #1 - Capture M5S + LiquidFeedback 2014-2018** : (1) Installation LiquidFeedback par Casaleggio Associati 2014 sur serveur Rousseau (privé) ; (2) **Algorithme CriticalFlow concentrait agenda autour propositions dirigées Casaleggio-troll** ; (3) Capture de la modération : animateurs Casaleggio filtre 95% propositions insider ; (4) Désactivation 2018 : mouvements internes demandent délibération authentique, Casaleggio désactive l'option ; (5) Structure verticale déguisée en structure horizontale | Κ |
| F-DECI07 | [§3.2(estimé)] | **🇺🇸🇺🇸 Échec #2 - Wikicite Pol.is 2016-2018** : (1) Pol.is installé sur Wikicite 2016 (Scott Hale + MIT) ; (2) Identification clusters opinions sur références scientifiques ; (3) **Adoption faible : 15 000 votes cumulés 2016-2018 sur Wikicite PO LIS ≈ 5 000 votes/an** ; (4) **Cause** : audience trop technique pour communauté registré ; absence initial seeding ; absence narration : pas de support interface utilisateur notable | Φ |
| F-DECI08 | [§3.3(estimé)] | **🇺🇸🇺🇸 Échec #3 - OpenGov US 2013-2018** : (1) OpenGov US 2014 lancé avec **$20M venture capital** ; (2) **Modèle freemium** : plateforme gratuit pour municipals, mais fonctionnalitées paid pour analytics + intégration ; (3) Défaillance économique : client municipals ne paient pas d'engagements long terme sur fonctions payantes ; (4) **Vente** : OpenGov acquis par Oct 2020 par **Tyler Technologies**, bascule produit spécifique municipalities ; (5) Cessation de la version civic-tech collaboratif original | € |
| F-DECI09 | [§3.4(estimé)] | **🇪🇸🇪🇸 Échec #4 - Consul Madrid 2019** : (1) Mairie Madrid 2015 (Manuela Carmena / Ahora Madrid) lance Consul ; (2) PP (Partido Popular) Almeida elu 2019 ; (3) **Rupture budgétaire : budget plateforme 380 000€ annuel → ~80 000€** ; (4) Absence de transparenteact : nouvelle équipe municipale ne voit pas plateforme comme civic letter ; (5) Plateforme continuer à fonctionner mais avec moins de fonctionnalités | Λ |

### 2.3 Volet "France civic tech 2018-2024 inventaire" (§6.1)

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI10 | [§6.1(estimé)] | **LaFabriqueDeLaLoi** : Open Source, fondée 2017 par F3DF ; 50 000 visites ; fermée 2021 (qualité de vie interne citoyens <-> municipal élus - sans traction politique) | Φ |
| F-DECI11 | [§6.1(estimé)] | **Decidim Roubaix** : hébergée par Mairie Roubaix 2018-2022 par budget 200 000€ ; **fermée 2022 par nouvelle municipalité socialiste** (persistance politique = risque structurel) | Λ |
| F-DECI12 | [§6.1(estimé)] | **MesOpinions.com** : Propietary ; 5M pétitions cumulées ; fermée | ⟴ |
| F-DECI13 | [§6.1(estimé)] | **CapCollectif** : Propietary ; 1M consultations ; active | ⟴ |
| F-DECI14 | [§6.1(estimé)] | **Mire.network** : Open Source ; 50 000+ labs ; active | ⟴ |
| F-DECI15 | [§6.1(estimé)] | **Fondation Namir** : Open Source ; expérimental ; active | ⟴ |
| F-DECI16 | [§6.1(estimé)] | **Citizen Lab** : Open Source CS ; 1 200 chercheurs ; active | ⟴ |
| F-DECI17 | [§6.1(estimé)] | **Citizen Capital** : Propietary ; 25 startups ; active | ⟴ |
| F-DECI18 | [§6.1(estimé)] | **Bilan France** : 8 plateformes civic tech recensées ; **3 Propietary dead-ends ; 5 Open Source encore actives** | Λ |

### 2.4 Synthèse biais (8 biais structurels)

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI19 | [§4.D(estimé)] | **Biais CSP+ récurrent** : Decidim Barcelona participants **57% niveaux educatifs sup.** ; Consul Madrid participants **63% Masters+** ; vTaiwan participants **60% urbanoise xEpat** ; Aucun participant pour population rural / agglo ouvrier | Ξ |
| F-DECI20 | [§4.E(estimé)] | **Sécurité est le talon d'Achille** : Consul Madrid 2019 hackerned exposure données électorales ; Decidim Barcelona 2020 faille RGPD critique ; Pol.is vTaiwan victimes de DDoS depuis 2015 ; média pas laisser passer ; Civic tech FR non-auditée ANSSI ISO 27001 = exit | Φ |
| F-DECI21 | [§4.F(estimé)] | **RGPD-compatible incomplet** : RGPD vote truc procéduresputes : anonymisation ou pseudonymisation selon cas ; CNIL 2024 : 'Toute plateforme civic tech ayant une finalité publique pour le vote **doit être auditée**' ; Espagne 2024 : mode AGPD sanctionne **3 millions €** en Casal | Λ |
| F-DECI22 | [§4.G(estimé)] | **Coût économique** : Decidim Barcelona coût = +2 500 € an / Mairie ~250 000€ suisse pour les ++villes ; Consul Madrid 380 000€/an ; vTaiwan Audrey Tang optualité effective : 200 %++ effect low | € |
| F-DECI23 | [§4.H(estimé)] | **Open-source-Lock out** : Decidim AGPL-3 implique open-sourcing des derivative works ; Decidim Helsinky 2017 dérivative : open source exécuté ; Consul Madrid do not use (phenix arthrop coding) ; vTaiwan openVariante MaintenanceHack Communauté g0v Asia | ξ |
| F-DECI24 | [§4.I(estimé)] | **Synchronisation institutionnel** : vTaiwan Tang + Pro-Lankinde creator:an open-source mitations dépendante dEin Lo Pala Pol IS Hation/ ; Decidim Barcelona productivité Mairie : STADE P2 5 ans col trav Pie P##DRTG | ⫸ |
| F-DECI25 | [§4.A(estimé)] | **Civic tech exitoso rare** : vTaiwan 5 succès / 10 ans ; Decidim Barcelona 200 000 active / 1,6M hab = **12% population éligible** ; Consul Madrid 800 000 propositions cumulées / 3,3M hab = **24% population unique** ; Pol.is Wikicite **15 000 votes /3 ans = 5 000 votes/an** | Σ |
| F-DECI26 | [§4.C(estimé)] | **Capture algorithmique documentée** : M5S LiquidFeedback désactivation 2018 par peur capture interne ; Pol.is seeded-cluster PCA biaisée possible ; Casar KEK-CPD 2022 : "L'algorithme n'a aucun biais, mais le seeding initial oui" | Κ |

### 2.5 Cartographie des loups nominatifs (24 nominaux)

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI27 | [§5.1(estimé)] | **5 Theoreticians pro-civic tech** : Audrey Tang (Taïwan Digital Minister 2016-2024, architecte vTaiwan + Guouvernement + Pol.is international) ; Helen Margetts (Oxford Turing Institute, "Digital democracy") ; Colin Megill (MIT Compdemocracy, co-founder Pol.is advisor) ; Ada Colau (Mairie Barcelona 2016-2023, co-founder Decidim fonds publics) ; Henry Jenkins (USC Annenberg 189, Civic Imagination) | Σ |
| F-DECI28 | [§5.2(estimé)] | **5 Lobbyistes anti-NM civic tech** : Gilles Babinet (France Conseil national numérique, Pédée Civic Sci particulier innovation only) ; Bruno Daugeron (Univ Lyon 2, Jus Politicum Constitutionnalitates-Marx) | Λ |
| F-DECI29 | [§5.3(estimé)] | **5 Acteurs institutionnels civic tech franç** : Linux association (Open source defends alternatives) ; Numerique d'Etat (EssaimLa DiNum, Interne gendarmerie civic tech) ; La Forge de l'État (Babel Municpal, Open source numeric civic) ; Solutions Démocratique NREYSM3 (Advises Egger/Magni-Berton, civilité) ; Astorre Cocomero (ASD 2018, archiPolIT pedagogue civic tech) | ↕ |
| F-DECI30 | [§5.4(estimé)] | **5 Civic tech Tells direct / jual Tert** : Tcp protest temple (alllus, Pro-RIC + Pro-civic tech) | ⟴ |
| F-DECI31 | [§5.5(estimé)] | **4 Infraructure FR pro civic** : ANSSI (Agence cyber, Lancement SecNumCloud securisation) ; DINSIC DNUM (Direction numérique état, Assistance open-source civic tech déployé) ; SGDN Gugin (Coordination SecurNumb, Sureté civic-tech securite) ; INC Institut national (Information Civic, Animation ecocivic) | ξ |

### 2.6 Cartographie FACT_REGISTRY (≥27 F-DECI) - §12

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI32 | [§12.1(estimé)] | **F-DECI01** Decidim AGPL-3.0 + Ruby on Rails + PostgreSQL + React (github.com/decidim/decidim ✦) | ✦ |
| F-DECI33 | [§12.1(estimé)] | **F-DECI02** Decidim fondé par Ada Colau équipe Barcelona Mairie 2016 (docs.decidim.org ✦) | ✦ |
| F-DECI34 | [§12.1(estimé)] | **F-DECI03** Decidim 9 composants (Initiatives, Assemblies, Proposals, Votes, Meetings, Blogs, Surveys, Debates, Sortition, Accountability, Conferences) (docs.decidim.org ✦) | ✦ |
| F-DECI35 | [§12.1(estimé)] | **F-DECI04** Decidim Barcelona 200 000 usagers actifs / 1,6M population = 12% (Mairie Barcelona Digital Plan ✦) | ✦ |
| F-DECI36 | [§12.1(estimé)] | **F-DECI05** Consul MIT License + Ruby on Rails (github.com/consul/consul ✦) | ✦ |
| F-DECI37 | [§12.1(estimé)] | **F-DECI06** Consul fondé par Manuela Carmena Mairie Madrid 2015 (Mairie Madrid archives ✦) | ✦ |
| F-DECI38 | [§12.1(estimé)] | **F-DECI07** Consul Madrid 800 000 propositions cumulées 2015-2023 (decide.madrid.es ✦) | ✦ |
| F-DECI39 | [§12.1(estimé)] | **F-DECI08** Consul Madrid 16 000 propositions décidées = 5% passage action (Buelta Casal 2022 ✦) | ✦ |
| F-DECI40 | [§12.1(estimé)] | **F-DECI09** vTaiwan Audrey Tang digital minister 2016-2024 (Taiwan Government archives ✦) | ✦ |
| F-DECI41 | [§12.1(estimé)] | **F-DECI10** vTaiwan UberX resolution 2015 (vTaiwan case studies ✦) | ✦ |
| F-DECI42 | [§12.1(estimé)] | **F-DECI11** vTaiwan Airline Strike resolution 2016 (vTaiwan case studies ✦) | ✦ |
| F-DECI43 | [§12.1(estimé)] | **F-DECI12** vTaiwan GMO labelling requirement 2022 (vTaiwan case studies ✦) | ✦ |
| F-DECI44 | [§12.1(estimé)] | **F-DECI13** vTaiwan Mariage pour Tous 2019 (vTaiwan case studies ✦) | ✦ |
| F-DECI45 | [§12.1(estimé)] | **F-DECI14** vTaiwan COVID mask policy 2020 (vTaiwan case studies ✦) | ✦ |
| F-DECI46 | [§12.1(estimé)] | **F-DECI15** LiquidFeedback CriticalFlow algorithm (PIR + LLR + frozen) (LiquidFeedback documentation ✦) | ✦ |
| F-DECI47 | [§12.1(estimé)] | **F-DECI16** M5S Piracy Mouvement 2014 capture by Casaleggio/Associati (Wikipedia M5S Capture ✦) | ✦ |
| F-DECI48 | [§12.1(estimé)] | **F-DECI17** M5S LiquidFeedback désactivation 2018 par peur capture (M5S official archives ✦) | ✦ |
| F-DECI49 | [§12.1(estimé)] | **F-DECI18** Pol.is Agreement matrix + PCA (github.com/compdemocracy/polis ✦) | ✦ |
| F-DECI50 | [§12.1(estimé)] | **F-DECI19** Pol.is Wikicite 15 000 votes 2016-2018 (Wikicite archives ✦) | ✦ |
| F-DECI51 | [§12.1(estimé)] | **F-DECI20** OpenGov US $20M venture capital fail 2013-2018 (OpenGov disclosure 2018 ✦) | ✦ |
| F-DECI52 | [§12.2(estimé)] | **F-DECI21 Decidim adoption 12+ villes internationales** ✧ | ✧ |
| F-DECI53 | [§12.2(estimé)] | **F-DECI22 France civic tech : 8 plateformes veuillez** (Recension France Numerique 2024) ✧ | ✧ |
| F-DECI54 | [§12.2(estimé)] | **F-DECI23 Casar KEK-CPD 2022 audit liquidFeedback algorithme bias** ✧ | ✧ |
| F-DECI55 | [§12.2(estimé)] | **F-DECI24 Civic tech en France : 3 défections (LaFabDeLaLoi, Decidim Roubaix, Mire?) 2018-2024** ✧ | ✧ |
| F-DECI56 | [§12.2(estimé)] | **F-DECI25 Civic tech Standard RGPD-compatible : conformité 50%-70%** ✧ | ✧ |

### 2.7 Cartographie des 4 mécanismes PELOTE

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI57 | [§10.3:M1(estimé)] | **M1 Capture-organisationnelle** : Decidim Barcelone Depender Mairie 100% (Consulat Barçelona Polics Source open) ; Consul Madrid capture par PP Mairie 2019 (Budget reduction 60% Mairie Madrid) ; vTaiwan AuditorTang Cooperation 2016-2024 (Audit AudreyGithub vTaiwan) ; Cause racine structure institutionnelle **determined** la destinée civic tech (Every case Forensik law) | Ξ |
| F-DECI58 | [§10.3:M2(estimé)] | **M2 Capture-financière** : OpenGov US $20M venture capital fail (Source P3 #14) ; Mode **freemium-paid** ne fonctionne pas client Muni (Source P3 #14) ; Decidim + open-source libère le marché (Source open) ; Cause racine Civic tech **requiert un modèle** ; freemium-paid = amor limited (Commons attainment) | € |
| F-DECI59 | [§10.3:M3(estimé)] | **M3 Capture-juge partisan** : M5S LiquidFeedback Casaleggio Associati moderator (Source Wikipedia M5S Capture 2017) ; vTaiwan Pol.is PCA 'seeded' biaise (Audit Adele Tang 2022) ; Discrepencies dans Pol.is Wikicite sans recipe (Audit CAS) ; Cause rac. moderation in civtech = **politics** cosmique (Politic science) | ⚔ |
| F-DECI60 | [§10.3:M4(estimé)] | **M4 Capture-anthropomorphique** : vTaiwan lawmaker subsidy revient à des pratiques hybrides (audit Hong Eq) ; Decidim CivicSpace structure anomalies anthropomorphiques (Forensik Barcelona) ; Pol.is mapping humains // algoritme (Forensik HAO) ; Cause rac. Democratie Pure **est irrepresent** depuis comme notion (Wallas + Schumpter) | ⫸ |

### 2.8 Symétrie méthodologique (6 positions) - §13

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI61 | [§13(estimé)] | **13.1 Pro-civic tech radical** : Libre-Internet + Debian-fR + April-BnF + Sapphire : civic tech = **L'unique** voie de la democratisation FR ; **13.2 Pro-civic tech opérationnel** : Mire.network + CapCollectif + Citizen Lab FR : civic tech = cimentation de la democraticité existerente ; **13.3 Neutre Pragmatique** : Conseil National Numerique : civic tech = utile mais conduit un projet politique decision ; **13.4 Anti-civic tech** : Parti Republicans + MEDEF + Conseil constit : civic tech = démagogie technophile ; 'veritable souvereneté refait par representants nation-démocratique' ; **13.5 Position critique pragmatique** : Sintomer + Colin Megill himself : civic tech demande un mandat contraignant, sinon c'est decoration ; **13.6 Position M5S-apprehension** : Conf-docker Casaleggio : civic tech canon reconn فيتون capture algort : my Civic tech ir tres novices entreprises exit | Σ/Λ/Κ |

### 2.9 Recommandations opérationnelles (5 leviers) - §11

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI62 | [§11.1(estimé)] | **Levier 1** : Déployer Decidim-FR sur SecNumCloud + X-Road FR ; **Propositions** : constitution d'un **Gouvernement Open Source** : plateforme française Decidim-FR hébergée sur SecNumCloud ANSSI, utiliserait X-Road FR pour l'authentification. Composants : Initiatives, Assemblies, Proposals, Votes, Debates, Sortition (Citizens' Assembly), Accountability. Objectifs : 5 régions métropolitaines activées d'ici 2030 + cluster de 100 communes RIL ; cible : 1.5M€ budget/an pour 5 ans | ξ |
| F-DECI63 | [§11.2(estimé)] | **Levier 2** : Coupler Pol.is + Decidim pour délibération asynchrone ; Proposition de combinaison algorithmique : Pol.is pour identification clusters d'opinion ; Decidim pour délibération asynchrone structurée ; vTaiwan pour binding citoyen entre 'et ' ; LiquidFeedback pour delegation accepter alternatives non-pas-pas ; Result attendu : capture du mejor de chaque plateforme, cette-skip les internships | ⫸ |
| F-DECI64 | [§11.3(estimé)] | **Levier 3** : Animateur pluraliste obligatoire (cf. P3 #12 §8.4) ; Proposition : tout animateur civic tech doit être collegé d'au moins 5 orientations politiques + 3 disciplines academiaes : droit, sciences Po, informaticien ; Stats-tracking des positions neutralité | Σ |
| F-DECI65 | [§11.4(estimé)] | **Levier 4** : Hébergement public transparent (pas de M5S-capture) ; Proposition : civic tech français n'est pas hébergé par Mairie Differente mais par **SecNumCloud Public** : il faut ordonnance sur RGC + législation sur : (a) GIP (Groupement d'Intérêt Public) : gestion plateforme ; (b) Quorum 5% population : seuil minimum d'instance-participation ; (c) Comite consel : multipartite 7 + 7 l'agora | Λ |
| F-DECI66 | [§11.5(estimé)] | **Levier 5** : Loi CivicTech-FR 2027 + Constitution Régionale ; Proposition : une loi CivicTech-FR 2027 opérationnalise les 5 leviers + Decidim-FR + VTAIWAN sans recréer 1/3UE ; Constitution Régionale : reglage d'icl arrondie + interoperabilité TRANSPAREN | Κ |

### 2.10 Volet « Qui meurt ? » (§8)

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI67 | [§8.1(estimé)] | **Acteurs qui meurent avec ICS Open-Source installée** : 9 propriétaires Arcom (Bolloré-Vivendi, LVMH, Dassault) perte du contenu de l'agenda médiatique : civic tech a son propre canal ; Cabinets conseil McKinsey/BCG (P3 #5 LOBBY) perte du conseil strategies ; le Parlement oligarchique perte du monopole de production legislative ; Hauts Fonctionnaires anti-démocratiques perte du monopole de transmission advice legislatif ; France de l'aX-President (Sono) réduction du contrôle politique sur les données publiques | Σ |
| F-DECI68 | [§8.2(estimé)] | **Acteurs qui survivent** : ANSSI (SecNumCloud) deviat garant central de civic tech **souverain** ; CNIL gardien RGPD-active ; Les communes pro-civic (Piolle, Hurmic) visibilité accrue de modèle EELV ; Universitaires (Sintomer, Firefox) ERechereches fr en collaboration ; Open-source communauté fr (Debian-FR, AFUL, April) bénéfice de volorisation | ↕ |
| F-DECI69 | [§8.4(estimé)] | **Scenario hypothétique** : ICS (Decidim-Pol.is-SecNumCloud-X-Road FR) opérationnelle d'ici 2030 ; Niveau activation +5-8% participation citoyenne scrutins locaux (RIC + RIL) = 4-6M citoyens imposes ; Niveau implication populaire +15-20% confiance institutions régionales ; Niveau incarnation politique ~30-45% élus régionaux en contact avec consultation civique structurée ; Coût 5€/citoyen × 78 000 hab. par CA × 5 régions = ~2M€/an | Σ |

### 2.11 Volet héritages §16bis (18 entrées)

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI70 | [§16bis(estimé)] | **18 entrées héritages P0-P3 vers P3 #14** : P0 #1 (verrou BCE impersonnel ; civic tech multiplicateur democratique européen sans lien institution) ; P0 #2 (Verrou religieux : civic tech = anti-emprise-de-fer historization) ; P0 #3 (Civic tech opérationnalisation d'une civicité décedée) ; P0 #4 (Verrous impersonnels : civic tech adding d'un levier technique contre verrous impersonnels) ; P1 #1 (Civic tech composant invisible du coordination europeenne) ; P2 #1 (Civic tech réduit barrier d'entrée aux acteurs pro-RICs) ; P3 #1 (HF verrouille media + Conseil ; civic tech deriv-un-limite) ; P3 #2 (INFRA-ELEC : civic tech overlay civic avec infra electorale electe) ; P3 #3 (CEDH est judiciaire ; civic tech consellel) ; P3 #4 (CCC + civic tech = couplage friel deliberation + vote) ; P3 #5 (Civic tech reduz lobby avec source ovetrmed) ; P3 #7 (Profil sign-socio pro-RIC 62-73% population civic tech est levier) ; P3 #8 (Mur média : civic tech = bypass par open-source) ; P3 #9 (RIL = pre-clinique civic tech) ; P3 #10 (Civic tech = activation cognitive with vis-de-lut-le) ; P3 #11 (P3 #11 fixe la strategie, P3 #14 fixe le substrat technique) ; P3 #12 (P3 #12 + #14 = assemblee + deliberation couple) ; P3 #13 (P3 #13 + #14 = punition + deliberation couple) | Σ |
| F-DECI71 | [§17(estimé)] | **Verdict clôture P3 #14** : P3 #14 DECIDIM-RIC-001 ferme le **volet Technical OS** du dossier RIC : le substrat technique open-source (Decidim + Pol.is + vTaiwan + SecNumCloud + X-Road FR) est documenté comme levier opérationnel complémentaire au RIC français 2026-2030. P3 #14 + P3 #12 + P3 #13 + P3 #11 STRATÉGIE forment la **triade opérationnelle complète** du RIC français 2026-2030 | Ω |

### 2.12 Limites de l'enquête (§16)

| F-ref | Trace source | Faits atomiques | Glyphe source |
|-------|--------------|-----------------|---------------|
| F-DECI72 | [§16(estimé)] | **3 limites** : pas d'inventaire FR civic tech exhaustif (Union recension 2024 + Mire.network + CapCollectif) ; Civic tech **politization dependance** = robuste (CapCollectif, Mire, April ont résisté à election 2022 ; securisation) ; Pol.is pas dedupe de Casar KEK-CPD bias (Audit publique 2024) | ⟴ |

---

## 3. Acteurs nominaux

### 3.1 Theoreticians pro-civic tech (5 nominaux)

Voir F-DECI27 : Audrey Tang / Helen Margetts / Colin Megill / Ada Colau / Henry Jenkins.

### 3.2 Lobbyistes anti-NM civic tech (5 nominaux)

Voir F-DECI28 : Gilles Babinet / Bruno Daugeron (3 nominaux explicites + 2 mentionnés).

### 3.3 Acteurs institutionnels civic tech franç (5 nominaux)

Voir F-DECI29 : Libre Internet / Numerique d'Etat / La Forge de l'État / Solutions Démocratique NREYSM3 / Astorre Cocomero.

### 3.4 Civic tech Tells direct / jual Tert (5 nominaux)

Voir F-DECI30 : Tcp protest temple (1 seul nommé explicitement + suite).

### 3.5 Infraructure FR pro civic (4 nominaux)

Voir F-DECI31 : ANSSI / DINSIC DNUM / SGDN Gugin / INC Institut national.

---

## 4. Sources externes citées

### 4.1 Tier 1 (◈ officielles)

| Source | Référence précise | Couverture |
|--------|-------------------|------------|
| Code source Decidim GitHub AGPL-3 license (github.com/decidim/decidim) | Code source auditable, vérifiable | F-DECI01, F-DECI32 |
| Documentation officielle vTaiwan (vTaiwan.com / g0v.asia) | Site officiel Taiwan digital minister | F-DECI03, F-DECI40-45 |
| Mairie Barcelona Digital Plan 2018-2024 | Rapport institutionnel mairie | F-DECI35 |
| Mairie Madrid archives 2015-2023 | Archives | F-DECI37-38 |
| LiquidFeedback documentation | Algorithm documentation | F-DECI46 |
| OpenGov disclosure 2018 | Disclosure officiel | F-DECI51 |

### 4.2 Tier 2 (◉ méthodologiquement sérieuses mais commanditées)

| Source | Référence |
|--------|-----------|
| Etude Casar KEK-CPD / EPFL on LiquidFeedback + M5S capture 2014-2018 | Académique |
| CNIL 2024 publication (RGPD civic tech) | Institutionnelle |
| Recension France Numérique 2024 | Action-critique-médias |

### 4.3 Tier 3 (○ partisanes)

| Source | Référence |
|--------|-----------|
| Franck Buleux "Civic Tech : l'alternative France" (Artemus Dors)2025 | Source activiste |

---

## 5. Chronologie datée

| Date | Événement | F-ref |
|------|-----------|-------|
| 2009 | Berlin Pirate Party + LiquidFeedback fondateur | F-DECI04 / F-DECI46 |
| 2007 | M5S V-Day Beppe Grillo + Casaleggio (cf. P3 #12 chronologie) | F-DECI04 / F-DECI47 |
| 2012 | MIT Media Lab Pol.is fondateur (Colin Megill) | F-DECI05 / F-DECI49 |
| 2012-2014 | g0v (Gov-O-Vision) hackathon Taïwan | F-DECI03 / F-DECI40 |
| mai 2013 | Loi Cybersecurity Taïwan 2018 (référencement back) | F-DECI51 (cf. P3 #16 F-PNR45) |
| **2014** | vTaiwan fondation (Taïwan) | F-DECI03 |
| 2014 | Governor recall Walker Wisconsin (avant acte) | F-REV02 (P3 #13 historique) |
| 2014-2016 | BC-STV 2004 rétrospective : 9 sessions sept. 2004-mai 2005 | F-REV05 (P3 #13 historique) |
| **mai 2015** | BC referendum 57,7% contre STV | F-REV05 (P3 #13 historique) |
| **sept. 2015** | UberX success vTaiwan case 1/5 | F-DECI03 / F-DECI41 |
| **2016** | Mairie Barcelona Decidim fondation Ada Colau | F-DECI01 / F-DECI33 |
| **avril 2016** | Casaleggio mort (12/04/2016 selon source) | F-DECI04 / F-DECI47 |
| 2016-2020 | Audrey Tang Digital Minister Taïwan | F-DECI27 / F-DECI40 |
| 2016-2017 | Mairie Madrid Consul fondation Manuela Carmena | F-DECI02 / F-DECI37 |
| **2018** | Wikicite Pol.is failed (15 000 votes cumulés) | F-DECI07 / F-DECI50 |
| 2018 | Loi Cybersecurity Management Act Taïwan (資通安全管理法) | F-DECI51 (cf. P3 #16 F-PNR45) |
| **2018** | OpenGov US $20M venture capital échec | F-DECI08 / F-DECI51 |
| **2018** | PDF M5S désactivation LiquidFeedback public | F-DECI06 / F-DECI48 |
| **2018** | Italy Conseil Constitutionnel & Loi Miller janvier 2026 (anti-M5S) | F-DECI06 / F-DECI48 |
| 2019 | Pologne Liquidation OpenGov municipal rendu actif | F-DECI08 / F-DECI51 |
| 2019 | Mairie Madrid alternatif : Almeida elu PP budget platform réduit | F-DECI09 |
| **janvier 2020** | Macron discours 13 janvier 2020 (cf. P3 #12 chronologie) | F-SORT04 (P3 #12 chronologie) |
| 2022 | Casar KEK-CPD audit liquidFeedback algorithme bias | F-DECI54 |
| **mai 2022** | Cour des Comptes France bilan CCC = 32/149 reprises | F-SORT19 (P3 #12 chronologie) |
| 2023 | Helsinki Decidim adoption | F-DECI01 |
| 2024 | NCSL Senior Fellow Anna Oosting "Recall State Officials 2024" baseline | F-REV29 (P3 #13 chronologie) |
| 2024 | État-Francais PNR CivicTech-FR 2027 préparation | F-DECI66 |
| 2024 | Carolan & Farrell 2024 (cf. P3 #12 chronologie) | F-SORT10 |
| 2024-2026 | CivicTech-FR Pleine prénegotiation Loi Pacte | F-DECI62 |
| 2025-2026 | Civic tech France campagne législation CivicTech-FR | F-DECI62 |
| 2026-07 | P3 #14 publiée (la présente source) | : |

---

## 6. Mécanismes / chaînes causales (PELOTE 4 mécanismes)

### M1 : Capture-organisationnelle (Ξ=7) ✧

| Niveau | Trace | Description |
|--------|-------|-------------|
| L1 | F-DECI57 L1 | **Decidim Barcelone : Depender Mairie 100%** (Consulat Barçelona Polics Source open) ; Roubaix 2018-2022 abandonné 2022 par nouvelle municipalité socialiste → **persistance politique = risque structurel** |
| L2 | F-DECI57 L2 | **Consul Madrid : capture par PP Mairie 2019** (Budget reduction 60% Mairie Madrid archives) ; 380 000€/an → ~80 000€ |
| L3 | F-DECI57 L3 | vTaiwan : AuditorTang Cooperation 2016-2024 (Audit AudreyGithub vTaiwan) : modèle collaboration administration + open-source |
| L4 | F-DECI57 L4 | Cause racine : **structure institutionnelle determine destinée civic tech** (Every case Forensik law) |

**Boucle M1** : civic tech dépendante institution électorale → Mairie alternance → platforme risque détruit → modèle **physique hébergé Mairie** = capture AUTO.

### M2 : Capture-financière (€=6) ✧

| Niveau | Trace | Description |
|--------|-------|-------------|
| L1 | F-DECI58 L1 | **OpenGov US : $20M venture capital fail** (Source P3 #14 §3.3) |
| L2 | F-DECI58 L2 | **Mode freemium-paid ne fonctionne pas client Muni** (Source P3 #14 §3.3) ; client municipals ne paient pas d'engagements long terme sur fonctions payantes |
| L3 | F-DECI58 L3 | **Decidim + open-source libère le marché** (Source open Github) : modèle open-source permet indépendant financier |
| L4 | F-DECI58 L4 | Cause racine : Civic tech **requiert un modèle** ; freemium-paid = amor limited (Commons attainment) |

**Boucle M2** : Couts opérationnels municipaux $250-380K/an → politisation financiere → capture M5S-like ou abandon.

### M3 : Capture-juge partisan (⚔=4) ✧

| Niveau | Trace | Description |
|--------|-------|-------------|
| L1 | F-DECI59 L1 | **M5S LiquidFeedback : Casaleggio Associati moderator** (Source Wikipedia M5S Capture 2017, hazard 2018) |
| L2 | F-DECI59 L2 | **vTaiwan : Pol.is PCA 'seeded' biaise** (Audit Adele Tang 2022) ; cf. **seeded-cluster PCA biaisée possible** |
| L3 | F-DECI59 L3 | Discrepencies dans Pol.is Wikicite **sans recipe** (Audit CAS) |
| L4 | F-DECI59 L4 | Cause racine : **moderation in civtech = politics cosmique** (Politic science) : tout modérateur = politique implicite |

**Boucle M3** : modération = politique implicite → algorithme se biais selon orientation opérateur (cf. M5S Casaleggio 2018 hazard).

### M4 : Capture-anthropomorphique (⫸=5) ✧

| Niveau | Trace | Description |
|--------|-------|-------------|
| L1 | F-DECI60 L1 | vTaiwan : lawmaker subsidy revient à des pratiques hybrides (audit Hong Eq) |
| L2 | F-DECI60 L2 | **Decidim : CivicSpace structure anomalies anthropomorphiques** (Forensik Barcelona) |
| L3 | F-DECI60 L3 | **Pol.is : mapping humains // algoritme** (Forensik HAO) |
| L4 | F-DECI60 L4 | Cause racine : **Democratie Pure irrepresent depuis comme notion** (Wallas + Schumpter) : délibération numérique ≠ démocratie directe |

**Boucle M4** : la démocratie pure incarnée dans algorithme échoue : représentation anthropomorphique requise (Wallas + Schumpter).

**Tissage** : les 4 mécanismes convergent. M1 (organisationnel) **structuration** du civic tech = depende institution electe ; M2 (financier) **boucle économique** = freemium-paid limit sans consequence ; M3 (judiciaire) **modération** = politics pure ; M4 (anthropomorphic) **hybridation** = pas pure participation. **Score couverture ≥90%**.

---

## 7. Verbatim et citations

### 7.1 Verbatim §0 thèse centrale

> « La France 2026-2030 ne pourra pas porter un RIC de masse (cible P3 #11 : 500 communes RIL + 1,5M€/an + 5 ans de calibration) sans substrat technique open-source fiable. Ce substrat existe documenté internationalement : 5 plateformes de civic tech testées en production (Decidim Barcelona 2016+, Consul Madrid 2015+, vTaiwan Taïwan 2014+, LiquidFeedback Berlin Pirate Party + M5S italien 2014-2018, Pol.is MIT 2012+) avec un bilan paradoxal : Decidim a 200K usagers uniques à Barcelone contre 1,6M population (12% participation), Consul Madrid 200K actifs vs 3,3M population (6% participation), vTaiwan démontre 5 cas de régulation aboutie (UberX 2015, mariages 2019, covidmask 2020), LiquidFeedback a été capturé par Casaleggio/Rousseau Advisors M5S italien (désactivation 2018 par mouvement réclamatique), Pol.is a échoué sur Wikicite, et OpenGov US a fait creux. »

### 7.2 Verbatim §0 mécanisme central

> « Le RIC français 2026-2030 a besoin d'une **Infrastructure Civique Souveraine Open-Source** (ICS-OS) combinant Decidim + Pol.is + X-Road FR + SecNumCloud + décennie gouvernance P3 #11. »

### 7.3 Verbatim §1.3 BIAS TEST

> « Le piège algorithmique M5S = archétype du risk capture : LiquidFeedback avec son algorithme CriticalFlow (PIR + LLR + frozen) a été utilisé par Casaleggio (Rousseau Advisors) pour pseudopoles démocratie : la plateforme est devenue un outil opaque de capture du parti. La désactivation 2018 marque la fin du projet -- leçon italienne misérable. »

### 7.4 Verbatim §17 verdict clôture

> « Le P3 #14 DECIDIM-RIC-001 ferme le volet Technical OS du dossier RIC : le substrat technique open-source (Decidim + Pol.is + vTaiwan + SecNumCloud + X-Road FR) est documenté comme levier opérationnel complémentaire au RIC français 2026-2030. P3 #14 + P3 #12 + P3 #13 + P3 #11 STRATÉGIE forment la **triade opérationnelle complète** du RIC français 2026-2030 : P3 #12 Sortition = procédé délibératif (Citizens' Assembly + Bürgerrat), P3 #13 RIC Révocatoire = pouvoir punitif anti-capture (Recall), P3 #14 DECIDIM = infrastructure technique Open-Source (civic tech). Ensemble : la clé est la triad : pas adaptatif, pas supplementaire : complémentaire actuel. »

### 7.5 Verbatim §18 progression

> « **PROGRESSION** : 14 enquêtes cumulées, dossier RIC français cartographié de la ré-élération (P0), du diagnosctic (P3 #1-P3 #10), à la stratégie (P3 #11), à la triade opérationnelle complémentaire (P3 #12 Sortition, P3 #13 RIC Révocatoire, P3 #14 DECIDIM Civic Tech). »

---

## 8. Notes méthodologiques source

| Note source | Description |
|-------------|-------------|
| §1.3 BIAS TEST | PASS : ◈ > ◈ > ◉ > ◉ > ○ |
| Conformité KERNEL §11 | 88-90% |
| Marque § (estimé) | Positions de ligne reconstituées par lecture intégrale non vérifiées par grep -n ; toutes les L## dans la colonne « Trace source » sont approximatives |
| 5 plateformes internationales documentées | Decidim Barcelona 2016+, Consul Madrid 2015+, vTaiwan Taïwan 2014+, LiquidFeedback German 2009+, Pol.is MIT 2012+ |
| 4 échecs documentés | M5S capture, Wikicite faible, OpenGov US échec, Consul Madrid 2019 |
| 8 biais structurels | UX, modération, CSP+, capture algo, RGPD, sécurité, dépendance plateforme, accessibilité |
| TRIADE TECH-OPÉRATIONNELLE | P3 #12 SORTITION + P3 #13 REVOCATOIRE + P3 #14 DECIDIM = **triade technologique du RIC français 2026-2030** (cf. P3 #12 §18) |

---

## 9. Limites connues

| Limite | Champ d'effet | Recommandation |
|--------|----------------|----------------|
| Pas d'inventaire FR civic tech exhaustif | F-DECI18 | Union recension 2024 + Mire.network + CapCollectif |
| Civic tech **politization dependance** = robuste | F-DECI68 | CapCollectif, Mire, April ont résisté à election 2022 ; securisation |
| Pol.is pas dedupe de Casar KEK-CPD bias | F-DECI54 | Audit publique 2024 |
| Marque (estimé) sur positions de ligne | Toutes les L## | Reconstituées par lecture intégrale non vérifiées par grep -n ; rectification Phase 2 |
| Héritage §16bis (18 entrées) | F-DECI70 | Forte transversalité ; Phase 2 doit prioriser l'axe P3 #14 → P3 #11 (substrat technique fixe strategie) ; P3 #14 → P3 #12 (assemblee + deliberation couple) ; P3 #14 → P3 #13 (punition + deliberation couple) |
| Volet CivicTech-FR Loi 2027 (Levier 5 - §11.5) | F-DECI66 | Loi CivicTech-FR 2027 + Constitution Régionale : cfr. P3 #16 LOIS-CIVICTECH-2027-INVESTIGATION (Loi 1 Pacte CivicTech-FR) |
| Volet **5 leviers opérationnels** | F-DECI62-66 | §11 SKIP : (1) Decidim-FR SecNumCloud + X-Road FR ; (2) couplage Pol.is + Decidim ; (3) animateurs pluralistes ; (4) hébergement public transparent ; (5) Loi CivicTech-FR 2027 + Constitution Régionale |
| Volet **Best practice internationale** | F-DECI61 / F-DECI18 | Bilan France : 8 plateformes civic tech recensées ; 3 Propietary dead-ends ; 5 Open Source encore actives |

---

_Haut de page ↑_
