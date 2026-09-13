# A4-S03 — Calibration V3

## Verdict

`PASS_AFTER_LOCAL_REPAIR`

## Réparations locales

1. `P13/P17` : retrait des mentions Allemagne/Iran lorsqu'aucune source lecteur locale n'était remontée avec une autorité suffisante dans la récupération courante. Le mécanisme général et les cas sourcés restent inchangés.
2. `P62` : remplacement de la généralisation sectorielle banque/pharmacie/défense par une formulation bornée sur industries réglementées, recherche sponsorisée et circulations public/privé. Aucun passage `accès -> causalité décisionnelle` n'est autorisé.
3. `P73` : remplacement d'une liste d'exemples hétérogènes par des contre-mécanismes réellement sourçables : annulation/borne juridictionnelle, recours, résultats nuls/faibles, faible visibilité de certaines campagnes.

## Contrôles

- `RELATION != CAUSALITÉ` : PASS
- `BÉNÉFICE != INTENTION` : PASS
- `CAS != PRÉVALENCE` : PASS
- `NON_TROUVÉ != ABSENT` : PASS
- `ANNONCE != ÉTAT_FINAL` : PASS
- promotion des bounded recoveries : NONE
- `INV-035` reconstruit artificiellement : NO
- nouveau BACK : 0
