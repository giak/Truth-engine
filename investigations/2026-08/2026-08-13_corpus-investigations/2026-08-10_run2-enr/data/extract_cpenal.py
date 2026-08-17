import re
raw = open('/tmp/payload_cpenal.xml', encoding='utf-8', errors='ignore').read()

def extract(num, maxc=3500):
    m = re.search(r'<article[^>]*\snum="' + re.escape(num) + r'"[^>]*>(.*?)</article>', raw, re.S)
    if not m:
        print('====', num, ': NON TROUVÉ ====')
        return
    bloc = m.group(0)
    # capturer etat et date
    etat = re.search(r'etat="([^"]+)"', bloc)
    date = re.search(r'date="([^"]+)"', bloc)
    mod = re.search(r'modTitle="([^"]+)"', bloc)
    txt = re.sub(r'<[^>]+>', ' ', bloc)
    txt = re.sub(r'\s+', ' ', txt).strip()
    print('====', num, '====')
    print('etat:', etat.group(1) if etat else '?', '| date:', date.group(1) if date else '?', '| mod:', mod.group(1) if mod else '?')
    print(txt[:maxc])
    print()

for num in ['432-11', '432-12', '432-13', '432-14', '433-1', '433-2', '321-1']:
    extract(num)
