import re
raw = open('/tmp/payload_cpat.xml', encoding='utf-8', errors='ignore').read()

def extract(num, maxc=2800):
    # balise article avec attribut num exact
    m = re.search(r'<article[^>]*\snum="' + re.escape(num) + r'"[^>]*>(.*?)</article>', raw, re.S)
    if not m:
        print('====', num, ': NON TROUVÉ ====')
        print()
        return
    bloc = m.group(0)
    txt = re.sub(r'<[^>]+>', ' ', bloc)
    txt = re.sub(r'\s+', ' ', txt).strip()
    print('====', num, '====')
    print(txt[:maxc])
    print()

for num in ['L523-1', 'L523-4', 'L523-6', 'L523-7', 'L523-8', 'L523-9', 'L523-10', 'L523-11']:
    extract(num)
