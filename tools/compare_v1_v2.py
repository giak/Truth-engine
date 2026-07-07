#!/usr/bin/env python3
"""Compare v1 (n=42 originaux) vs v2 (5 pilotes post-refonte P1)."""

import json
import subprocess
import statistics

# Audit v1 (dossier _quintessence/ original)
v1 = subprocess.run(
    ['python3', 'tools/audit_phase1_sublimator_v35.py', 'json',
     '-d', 'investigations/2026-07-04-RIC/_quintessence'],
    capture_output=True, text=True,
    cwd='/home/giak/projects/truth-engine',
)
d1 = json.loads(v1.stdout)

# Audit v2 (dossier _quintessence_v2/)
v2 = subprocess.run(
    ['python3', 'tools/audit_phase1_sublimator_v35.py', 'json',
     '-d', 'investigations/2026-07-04-RIC/_quintessence_v2'],
    capture_output=True, text=True,
    cwd='/home/giak/projects/truth-engine',
)
d2 = json.loads(v2.stdout)

# 5 fichiers pilotes
mapping = [
    ('cultes_4_religions_france_position_ric', 'cultes_4_religions'),
    ('ric_bce_euro_verrou', 'bce_euro_verrou'),
    ('chronologie_6_presidents_ric_effectif', 'chronologie_6_presidents'),
    ('ric_crypto_dao_aragon_snapshot_blockchain', 'crypto_dao_aragon'),
    ('infrastructure_electorale_privee_INFRA-ELEC-001', 'infrastructure_electorale_privee'),
]


def to_score(v):
    return 1 if v == '\u2705' else (0.5 if v == '\u26a0\ufe0f' else 0)


v1_dict = {a['file']: a for a in d1['canoniques']}
v2_dict = {a['file']: a for a in d2['canoniques']}

print('=' * 110)
print('COMPARAISON V1 (originaux) vs V2 (post-refonte P1 - 5 pilotes)')
print('=' * 110)
print()
header = f'{"SUJET":35} | {"V1 score":10} | {"V2 score":10} | {"DELTA":8} | {"C10 V1":8} | {"C10 V2":8} | {"C7 V1":6} | {"C7 V2":6}'
print(header)
print('-' * 110)

c10_gains = []
c7_gains = []
score_gains = []

for pattern, label in mapping:
    v1_file = next((f for f in v1_dict if pattern in f), None)
    v2_file = next((f for f in v2_dict if pattern in f), None)
    if v1_file and v2_file:
        a1 = v1_dict[v1_file]
        a2 = v2_dict[v2_file]
        delta = a2['score_strict'] - a1['score_strict']
        c10g = to_score(a2['C10_strict']) - to_score(a1['C10_strict'])
        c7g = to_score(a2['C7']) - to_score(a1['C7'])
        c10_gains.append(c10g)
        c7_gains.append(c7g)
        score_gains.append(delta)
        print(f'{label:35} | {a1["score_strict"]:>5.1f}/7 | {a2["score_strict"]:>5.1f}/7 | {delta:+5.2f} | {a1["C10_strict"]:8} | {a2["C10_strict"]:8} | {a1["C7"]:6} | {a2["C7"]:6}')

print()
print('=' * 110)
print('STATISTIQUES GLOBALES')
print('=' * 110)
print()
print(f'V1 n={len(d1["canoniques"])} fichiers | Score strict moyen: {d1["stats"]["canoniques"]["score_strict_moyen"]}/7')
print(f'V2 n={len(d2["canoniques"])} fichiers | Score strict moyen: {d2["stats"]["canoniques"]["score_strict_moyen"]}/7')
print()
print('Sur les 5 fichiers pilotes :')
print(f'  - Gain C10 moyen: {statistics.mean(c10_gains):+.2f} (objectif utilisateur: >=+0.5)')
print(f'  - Gain C7 moyen: {statistics.mean(c7_gains):+.2f} (objectif utilisateur: >=+0.3)')
print(f'  - Gain score strict moyen: {statistics.mean(score_gains):+.2f}/7')
print()
print('Detail par fichier :')
for pattern, label in mapping:
    v1_file = next((f for f in v1_dict if pattern in f), None)
    v2_file = next((f for f in v2_dict if pattern in f), None)
    if v1_file and v2_file:
        a1 = v1_dict[v1_file]
        a2 = v2_dict[v2_file]
        c10g = to_score(a2['C10_strict']) - to_score(a1['C10_strict'])
        c7g = to_score(a2['C7']) - to_score(a1['C7'])
        ok10 = 'OK' if c10g >= 0.5 else 'KO'
        ok7 = 'OK' if c7g >= 0.3 else 'KO'
        print(f'  {label:35} C10: {c10g:+.2f} [{ok10}] | C7: {c7g:+.2f} [{ok7}]')

print()
print('=' * 110)
print('VERDICT FINAL')
print('=' * 110)
c10_moy = statistics.mean(c10_gains)
c7_moy = statistics.mean(c7_gains)
c10_ok = c10_moy >= 0.5
c7_ok = c7_moy >= 0.3
print(f'C10 >=+0.5: {c10_ok} (mesure: {c10_moy:+.2f})')
print(f'C7 >=+0.3: {c7_ok} (mesure: {c7_moy:+.2f})')
if c10_ok and c7_ok:
    print('CONCLUSION : Objectifs atteints. Pas d\'iteration prompt necessaire.')
else:
    print('CONCLUSION : Objectifs non atteints. Iterer le prompt (cf. P1, P2).')
