# Test contrôlé de trois candidats structurés

## Périmètre

- Corpus amont : SQLite local, utilisé ici comme cas exceptionnel de corpus structuré.
- Date : 2026-08-20.
- Règle : le statut SQLite brut ne constitue pas une preuve.
- Aucun candidat n'est écrit à `status:CONFIRME`.

## Résultats

### 1. ATC → MEDDMO

```text
UPSTREAM_ID : FC17_00B86A60F5128FFD
SOURCE      : https://meddmo.eu/
```

- Recherche Mnemolite effectuée en premier ; aucun fait confirmé explicite sur ce couple.
- `read_url` : `403 Forbidden`.
- Chrome headless : page récupérée, mais aucun énoncé visible ne relie Athens Technology Center à MEDDMO.
- Deux recherches ciblées : aucun résultat exploitable.
- La page actuelle contient MEDDMO, mais pas la preuve du lien candidat.

```text
ACCESS_STATE      : HEAD_BLOCKED puis BROWSER_READABLE
EVIDENCE_STATE    : NO_ASSERTION
VERIFICATION     : NOT_VERIFIED
WRITE-BACK       : aucun
GAP_TYPE          : NO_ASSERTION / source insuffisante
```

### 2. Full Fact → EFCSN

```text
UPSTREAM_ID : FC17_00DC29532E08B562
SOURCE      : https://members.efcsn.com/signatories
MEMORY_ID   : 8a33e62d-02fe-460b-83d2-b0163d56a095
```

La page officielle est lisible et contient :

```text
VERIFIED MEMBERS
Full Fact
from United Kingdom
Verified since 15-06-2023
```

Locator enregistré : section `VERIFIED MEMBERS`, entrée `Full Fact`, champs `from United Kingdom` et `Verified since 15-06-2023`.

```text
EPI                : FACT
VERIFICATION_LEVEL : L2
STATUS             : VERIFIE
FAMILY             : A uniquement
CONFIRME           : non
WRITE-BACK         : effectué puis relu
```

Le write-back a d'abord reçu une clé amont abrégée par erreur. La clé exacte du CSV a ensuite été recopiée et la mémoire mise à jour :

```text
CYCLE17|ECOSYSTEM_RELATION|full_fact|verified_member_of|european_fact_checking_standards_network_efcsn|R_fd77586fbed4a5
```

### 3. Vrai ou Fake → franceinfo / IFCN

```text
UPSTREAM_ID : FC17_026DD557FDAD5442
SOURCE      : https://mail.ifcncodeofprinciples.poynter.org/application/public/franceinfofr/827E31C3-0D29-3DBE-9C50-2C8AEF308ADD
```

- Recherche Mnemolite effectuée en premier ; aucun fait confirmé explicite utilisé comme preuve.
- `read_url` : certificat expiré.
- Chrome headless : page d'erreur `ERR_CERT_DATE_INVALID`, certificat affiché comme expiré le 9 novembre 2025.
- Une recherche ciblée : aucun résultat exploitable.
- L'erreur de certificat ne permet pas de conclure que la source historique est fausse ou inexistante.

```text
ACCESS_STATE      : UNKNOWN / certificate_error
EVIDENCE_STATE    : GAP
VERIFICATION     : NOT_VERIFIED
WRITE-BACK       : aucun
GAP_TYPE          : ACCESS
```

## Frictions observées

1. **La clé amont ne doit jamais être retapée.** Elle doit être copiée automatiquement depuis le corpus ; une faute de frappe produit un mapping faux même si le fait est correctement vérifié.
2. **Le locator doit être capturé pendant la lecture.** On ne peut pas déduire un L2 après coup à partir d'une citation seule.
3. **L'échec d'accès et l'état probatoire restent distincts.** `403`, certificat expiré et résultat de recherche vide ne sont pas des réfutations.
4. **Le fallback navigateur est utile mais ne remplace pas l'extrait.** Une page récupérée sans assertion pertinente reste `NO_ASSERTION`.
5. **Le write-back L2 est suffisant pour un fait atomique simple.** Le recoupement L3/L4 doit rester réservé aux faits centraux ou contestables.

## Verdict du test

```text
Candidats examinés       : 3
Write-back VERIFIE       : 1
Candidats NOT_VERIFIED   : 2
Write-back CONFIRME      : 0
Erreur corrigée          : clé amont abrégée puis réalignée
```

Conclusion opérationnelle : automatiser maintenant uniquement l'extraction exacte des identifiants, la génération du manifeste et le rebouclage `UPSTREAM_ID → memory_id`. La décision EPI, la lecture de la source, le locator et le verdict restent sous contrôle factuel.
