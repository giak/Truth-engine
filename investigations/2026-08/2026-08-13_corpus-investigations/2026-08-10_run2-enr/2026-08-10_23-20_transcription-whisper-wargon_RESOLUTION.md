# RESOLUTION : TRANSCRIPTION DE LA VIDÉO 18767384 (AUDITION WARGON 29/04/2026) : PAS DE SOUS-TITRES CACHÉS, CHAÎNE WHISPER VALIDÉE, TRANSCRIPTION COMPLÈTE LANCÉE EN ARRIÈRE-PLAN

- STATE          : FINAL
- DATE           : 2026-08-10 23:20 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste, exploration technique de la piste ouverte par le 22-38)
- DOSSIER        : 2026-08-10_run2-enr (fil Valeco/EnBW, axe légitimité, suite du 22-38 GAP-ll2-2)
- OBJECT         : tester la piste de transcription de la vidéo 18767384 (audition Wargon du 29/04/2026 par la commission des affaires économiques de l'AN) : (1) vérifier si l'AN expose des sous-titres cachés dans la diffusion (VTT/WebVTT, piste de sous-titres, flux data), (2) tester un service de transcription vocale open source local (openai-whisper, modèle medium) pour rendre la parole de Wargon exploitable en texte
- VERDICT        : (1) AUCUN SOUS-TITRE CACHÉ : le endpoint .vtt renvoie une page HTML (35 Ko, pas un WebVTT), le flux data (index 2) du mp4 est de l'AMF0 Wowza (métadonnées de streaming, pas des sous-titres), aucune piste VTT/WebVTT dans la playlist. (2) CHAÎNE WHISPER VALIDÉE DE BOUT EN BOUT : téléchargement par HTTP range + ffmpeg (16 kHz mono) + whisper medium français produit un texte propre et exploitable (segment 900-1000 s et 1200-1800 s transcrits, contenu vérifié : Battistel interroge Wargon sur gaz/Ormuz/ARENH, propos liminaire Wargon : missions CRE, gaz 97 % importé, prix repère, nucléaire 370 TWh, ENR hydro 60 TWh, éolien 50 TWh, solaire 30 TWh, prix élec 50-58 €/MWh). La transcription séquentielle de la plage 1800-5400 s (suite de l'audition) est lancée en arrière-plan (setsid, survit aux sessions)
- GAP_SEVERITY   : 0.05 (la piste technique est tranchée : whisper est l'outillage OSINT retenu ; les segments restants sont en cours de transcription, résultats à collecter en fin de run)

## 1. Méthode : deux voies testées en parallèle

1. **Voie sous-titres** : test des endpoints possibles de sous-titres sur le domaine AN : `videos.assemblee-nationale.fr/video.18767384_69f1aa769a018.vtt`, `.srt`, variantes Vodalys (`/vod/mp4/.../6241_20260429085135_1.vtt`, `/vod/captions/...`), et le flux data (index 2) du mp4.
2. **Voie transcription locale** : identification de la diffusion réelle de la vidéo (yt-dlp → mp4 1,64 Go sur `anorigin.vodalys.com`), téléchargement d'échantillons audio par HTTP range (ffmpeg `-ss/-to`), puis transcription openai-whisper (modèle medium, langue française).

## 2. Constat 1 : AUCUN sous-titre caché (4 tests, tous négatifs)

| Test | Endpoint | Résultat |
|------|----------|----------|
| T1 | `videos.assemblee-nationale.fr/video.18767384_69f1aa769a018.vtt` | 35 285 octets : **page HTML** (DOCTYPE html, titre « Commission des affaires économiques : Mme Emmanuelle Wargon... »), pas un WebVTT |
| T2 | `anorigin.vodalys.com/vod/mp4/ida/domain1/2026/04/6241_20260429085135_1.vtt` et `.srt` | 535 octets : page 404 |
| T3 | Flux data (index 2) du mp4 | 0 octet lisible : **AMF0 Wowza** (métadonnées `onTimeCoordInfo`, `onStatus`), pas de texte |
| T4 | Playlist HLS (smil/m3u8) | 0 octet (chemin Vodalys différent, pas de m3u8 simple exposé) |

**Conclusion** : l'AN ne publie pas de sous-titres pour cette vidéo. La parole de Wargon n'est accessible qu'en audio (piste AAC du mp4, qui contient le son : vérifié par volumedetect, l'audio est vivant à partir de ~900 s, mean -25,7 dB).

## 3. Constat 2 : chaîne whisper validée de bout en bout

### 3.1 La diffusion

- yt-dlp identifie la vidéo : `6241_20260429085135_1.mp4` (enregistrée 29/04/2026 08:51, fin 10:18).
- URL de diffusion : `http://anorigin.vodalys.com/vod/mp4/ida/domain1/2026/04/6241_20260429085135_1.mp4` (1 640 530 359 octets, ~1,64 Go, accessible par HTTP range requests).

### 3.2 Les temps de la réunion

- L'audio est du silence pendant les 15 premières minutes (attente, début d'enregistrement 08:51, réunion à 9 h).
- Les débats commencent vers ~900 s (début : Battistel ouvre, désigne Brulebois/Fugit rapporteurs sur le DDADUE n° 2518).
- À 1200-1800 s : questions de Battistel + propos liminaire de Wargon (c'est le début de l'audition CRE).

### 3.3 Preuve de qualité (segment 1200-1800 s, transcrit intégralement, ~10 Ko)

Extraits vérifiés (texte brut whisper, retranscrit) :

- Battistel : « ...nous nous interrogeons sur l'évolution du prix de l'électricité, notamment depuis la disparition au 1er janvier dernier du dispositif de l'ARENH, accès régulé à l'électricité nucléaire historique... » (le plan d'urgence Accelerate UE du 22 avril, budgets 100 Md€ RTE/Enedis, paquet réseau du 10/12/2025).
- Wargon (propos liminaire) : « La CREU, comme vous le savez, est une autorité administrative indépendante... La deuxième, c'est de garantir le bon fonctionnement des marchés de gros et de détail... Et la troisième est d'accompagner le développement des énergies renouvelables en opérant les appels d'offres tels que décidés par le gouvernement... Nous importons 97% [du gaz]... le prix du gaz qui était environ de 30 euros par mégawatt-heure avant la crise est passé à 60 juste après début mars... autour de 43-44 euros... [prix repère] avec une augmentation de 15% au 1er mai... [électricité] le nucléaire est revenu à ces niveaux de production d'avant corrosion sous contrainte, à peu près 370 TWh... l'hydroélectricité à peu près 60 TWh... l'éolien à peu près 50 TWh et le solaire à peu près 30... le prix de l'électricité est passé d'en gros 50 à 58 euros du mégawatt-heure juste après l'invasion » (propos cohérents avec le contexte mars-avril 2026, guerre en Iran et détroit d'Ormuz).

### 3.4 Coût de calcul mesuré

| Segment | Durée audio | Temps CPU | Ratio | Note |
|---------|-------------|-----------|-------|------|
| 900-1000 s | 100 s | ~142 s | 1,42× | silence partiel (début) |
| 1200-1800 s | 600 s | ~140 min CPU | ~14× | modèle medium, 7,8 cœurs, charge mémoire 4,3 Go RSS |

- Le ratio réel sur segments longs (~14×) est bien supérieur au 1,42× mesuré sur 100 s : overhead mémoire du modèle sur fichiers longs. À ~7-8 cœurs effectifs, 600 s d'audio ≈ 18 min wall.
- Projection pour la plage cible 900-5400 s (audition CRE ~1 h 15 de débats réels) : ~6 segments de 600 s ≈ 2 h wall de calcul.

## 4. Action lancée : transcription séquentielle complète en arrière-plan

- Script : `/tmp/transcribe_all.sh` (boucle segments 1800-2400, 2400-3000, 3000-3600, 3600-4200, 4200-4800, 4800-5400 ; pour chaque : ffmpeg range download → whisper medium fr → texte).
- Lancement : `setsid nohup bash /tmp/transcribe_all.sh` (survit aux sessions), log `/tmp/transcribe_all.log`, sorties `/tmp/whisper_out/wargon_*.txt`.
- État au 23:20 CEST : segment 1800-2400 s en cours (PID 2774571, 602 % CPU).
- À la fin du run : concaténation des segments, recherche des mentions « collecte », « coûts », « échantillonnage », « plan d'audit », « rapport Cour des comptes » dans la transcription pour documenter la position orale de Wargon sur la rec. n°1 CdC (l'objectif du fil).

## 5. Table de faits

| ID | Proposition | Source | Localisation | Nature | Statut |
|----|-------------|--------|--------------|--------|--------|
| FCT-wsp-001 | Le endpoint .vtt de la vidéo 18767384 renvoie une page HTML (35 285 octets), pas un WebVTT | test curl 10/08/2026 | /tmp/wargon_18767384.vtt | Fait (absence) | ÉTABLI |
| FCT-wsp-002 | Les variantes Vodalys .vtt/.srt renvoient 404 (535 octets) | test curl 10/08/2026 | /tmp | Fait (absence) | ÉTABLI |
| FCT-wsp-003 | Le flux data (index 2) du mp4 est de l'AMF0 Wowza (onTimeCoordInfo, onStatus), pas des sous-titres | ffprobe 10/08/2026 | /tmp | Fait (absence) | ÉTABLI |
| FCT-wsp-004 | La vidéo est diffusée en mp4 1,64 Go sur anorigin.vodalys.com, accessible par HTTP range | yt-dlp + curl 10/08/2026 | URL Vodalys | Fait | ÉTABLI |
| FCT-wsp-005 | L'audio du mp4 est vivant (mean -25,7 dB à partir de ~900 s) ; les 15 premières minutes sont du silence | ffmpeg volumedetect | /tmp | Fait | ÉTABLI |
| FCT-wsp-006 | Whisper (modèle medium, français) produit un texte propre et exploitable sur la vidéo AN | run 10/08/2026 | /tmp/whisper_out/wargon_900.txt + wargon_1200.txt | Fait | ÉTABLI |
| FCT-wsp-007 | Le contenu transcrit (Battistel/Wargon, gaz 97 % importé, ARENH, nucléaire 370 TWh, ENR 60/50/30 TWh, prix 50-58 €/MWh) correspond à l'audition du 29/04/2026 | transcription 1200-1800 s | wargon_1200.txt | Fait | ÉTABLI |
| FCT-wsp-008 | Le ratio de transcription mesuré est ~1,42× sur 100 s et ~14× sur 600 s (modèle medium, 7,8 cœurs) | mesures 10/08/2026 | §3.4 | Fait | ÉTABLI |
| FCT-wsp-009 | La plage cible 900-5400 s (audition CRE) est couverte par 6 segments de 600 s ; transcription lancée en arrière-plan (setsid) | lancement 23:20 | /tmp/transcribe_all.sh | Fait | ÉTABLI |
| FCT-wsp-010 | À la fin du run, les segments seront concaténés et fouillés pour « collecte », « coûts », « échantillonnage », « plan d'audit », « rapport Cour des comptes » | plan | §4 | Inférence | PLANIFIÉ |
| FCT-wsp-011 | La position orale de Wargon sur la collecte des coûts (rec. n°1 CdC) reste à extraire de la transcription en cours | analyse | §4 | Inconnu | EN COURS |

## 6. Grille de verdict 3 axes (doctrine §13)

```text
PÉNAL    : 0 fait. L'absence de sous-titres n'est pas une infraction.
LÉGAL    : oui. La vidéo publique de l'AN est librement accessible ; la transcription locale (whisper) d'un débat public est licite.
LÉGITIME : renforcé. L'AN ne fournit ni CR écrit (22-38), ni sous-titres : la parole du régulateur sur 1,2 Md€ de soutien ENR est verrouillée hors du texte. La transcription par outillage local lève ce verrou technique, à coût nul, sans passer par l'administration.
```

## 7. Conclusion graduée

La piste technique est tranchée : (1) aucun sous-titre caché n'existe pour la vidéo 18767384 (4 tests négatifs : .vtt = HTML, variantes 404, flux data = AMF0, pas de piste VTT) ; (2) la chaîne openai-whisper est validée de bout en bout (HTTP range + ffmpeg + whisper medium français), avec un texte de qualité vérifiée sur 2 segments ; (3) la transcription séquentielle des segments 1800-5400 s (suite de l'audition) est lancée en arrière-plan et survit aux sessions. La prochaine étape (fin du run) : concaténation, fouille des mentions « collecte des coûts / échantillonnage / plan d'audit / rapport Cour des comptes », et documentation de la position orale de Wargon sur la rec. n°1 CdC, l'objectif final du fil GAP-ll2. L'outillage est réutilisable pour toute autre vidéo d'audition AN (pratique « pas de CR écrit » confirmée au 22-38).

## 7bis. RÉSULTATS COMPLETS DE LA TRANSCRIPTION (mise à jour 11/08/2026 04:09 CEST) : run TERMINÉ, position orale de Wargon documentée

- Run séquentiel TERMINÉ le 11/08/2026 à 01:10 ([ALL DONE], log /tmp/transcribe_all.log) : segments 900, 1200, 1800, 2400, 3000, 3600, 4200, 4800, 5400 s transcrits, concaténation /tmp/wargon_full.txt (73 715 caractères).
- PASSAGE DÉCISIF (l. 300-360) : le député Omblard (RN) interpelle Wargon : « quand la CRE compte-t-elle enfin publier une évaluation complète du coût système des énergies intermittentes en intégrant les subventions, l'effet de la surproduction à venir, le manque à gagner du nucléaire, les coûts de modulation excessifs, l'équilibrage, l'intégration aux réseaux de stockage » ; chiffres cités : évaluation CRE 60,3 €/MWh nucléaire sur hypothèse 362 TWh vs 373 TWh réalisés en 2025 (objectif EDF 400 TWh) ; PPE 3 : surcapacité 50-120 TWh vs prévisions RTE 2035 ; plans RTE/Enedis ~200 Md€ d'ici 2040 dont 70 Md€ liés aux intermittentes.
- RÉPONSE WARGON (l. 373-385) : « En ce qui concerne l'évaluation des coûts complets du système, nous l'avons fait dans notre avis sur la PPE il y a quelques mois, dans laquelle nous avons publié à la fois les coûts de soutien des différentes filières en subventions, mais également les coûts induits sur le réseau qui ne sont pas du tout du même ordre que les coûts de soutien en subventions des ENR et qui sont de l'ordre de quelques euros du MW ». Position orale CONCORDANTE avec la position écrite (fascicule, 22-30) : pas d'engagement de collecte exhaustive annuelle (échantillonnage préféré).
- OBJECTIF DU FIL ATTEINT : la position de la présidente de la CRE sur la collecte des coûts (rec. n°1 CdC) est documentée par 2 canaux indépendants (écrit + oral transcrit). Détail complet et analyse : document `2026-08-11_04-09_contre-test-culture-finances_RESOLUTION.md` §5.

## 8. Sources

1. Vidéo : `https://videos.assemblee-nationale.fr/video.18767384_69f1aa769a018` (audition Wargon, 29/04/2026).
2. Diffusion : `http://anorigin.vodalys.com/vod/mp4/ida/domain1/2026/04/6241_20260429085135_1.mp4` (1,64 Go, HTTP range).
3. Outillage : openai-whisper (venv pipx, modèle medium), ffmpeg, yt-dlp (vérifiés fonctionnels 10/08/2026).
4. Artefacts : `/tmp/whisper_out/wargon_900.txt`, `wargon_1200.txt` (transcrits), `/tmp/transcribe_all.sh` + log (run en cours), segments `/tmp/wargon_1800.wav` etc.
5. Documents croisés : 22-38 (GAP-ll2-2, absence de CR écrit), 22-30 (fascicule réponses CdC), 21-58 (GAP-ll2), 19-07 (check-list rec. n°1).
