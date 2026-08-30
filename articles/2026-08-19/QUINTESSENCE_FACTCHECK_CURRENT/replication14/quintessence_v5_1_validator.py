#!/usr/bin/env python3
"""QUINTESSENCE V5.1-FROZEN external protocol validator.

Checks mechanical compliance only. It does NOT fact-check claims or decide whether a source is substantively correct.

Usage:
  python quintessence_v5_1_validator.py RESULT.md \
      --prompt QUINTESSENCE_FALSIFICATION_V5_1_FROZEN_2026-08-23.md \
      --manifest QUINTESSENCE_V5_1_FROZEN_MANIFEST.json \
      --json report.json --markdown report.md

Exit codes: 0 = all atoms valid; 2 = protocol-invalid atom(s); 3 = run-level structural failure.
"""
from __future__ import annotations
import argparse, json, re, hashlib, sys
from pathlib import Path
from datetime import date

ATOM_RE=re.compile(r'(?m)^\s*(?:\*\*)?\s*#{0,6}\s*(C\d{2}-[A-Z])(?:\*\*)?\s*$')
FIELD=lambda name: re.compile(rf'(?mi)^\s*{re.escape(name)}\s*:\s*(.+?)\s*$')

ALLOWED={
    'TEXT':{'YES','NO','UNREADABLE','UNCERTAIN'},
    'DATA':{'YES','NO','UNCERTAIN'},
    'SEARCH':{'FOUND','NOT_FOUND','UNCERTAIN'},
}

def norm(s:str)->str:
    return s.replace('\\_','_').replace('\\: ',': ').replace('\\:',' :').strip()

def get(block,name,default=None):
    m=FIELD(name).search(block)
    return norm(m.group(1)) if m else default

def sections_all(block,label,stop_labels):
    starts=list(re.finditer(rf'(?mi)^\s*{re.escape(label)}\s*:\s*$',block))
    out=[]
    for i,st in enumerate(starts):
        end=len(block)
        # Same label starts the next evidence item.
        if i+1<len(starts): end=min(end,starts[i+1].start())
        for lab in stop_labels:
            for m in re.finditer(rf'(?mi)^\s*{re.escape(lab)}\s*:\s*$',block[st.end():end]):
                end=min(end,st.end()+m.start()); break
        out.append(block[st.end():end])
    return out

def parse_evidence(sec):
    return {
      'source_id':get(sec,'SOURCE_ID','NONE'),
      'source_type':get(sec,'SOURCE_TYPE','NONE'),
      'date':get(sec,'FIRST_PUBLIC_DATE','N/A'),
      'url':get(sec,'URL','NONE'),
      'opened':get(sec,'OPENED','NO'),
      'status':get(sec,'EVIDENCE_STATUS','NONE'),
      'excerpt':get(sec,'EXACT_EXCERPT','NONE'),
      'supports':get(sec,'DOCUMENT_SUPPORTS',''),
    }

def parse_result(text):
    text=text.replace('\\_','_')
    ms=list(ATOM_RE.finditer(text))
    blocks=[]
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(text)
        blocks.append((m.group(1),text[m.end():end]))
    return blocks

def iso(d):
    try:return date.fromisoformat(d)
    except:return None

def words(excerpt):
    if not excerpt or excerpt in {'NONE','N/A'}: return 0
    excerpt=excerpt.strip().strip('"').strip("'")
    return len(re.findall(r"\b[\wÀ-ÿ]+(?:[-’'][\wÀ-ÿ]+)*\b",excerpt))

def issue(code,msg,severity='ERROR'):
    return {'code':code,'severity':severity,'message':msg}

def validate_atom(aid,block,spec,source_types):
    issues=[]; warnings=[]
    typ=get(block,'TYPE')
    ans=get(block,'ANSWER')
    if typ!=spec['type']:
        issues.append(issue('TYPE_MISMATCH',f"TYPE={typ!r}, attendu {spec['type']!r}"))
    if ans not in ALLOWED.get(spec['type'],set()):
        issues.append(issue('INVALID_ANSWER',f"ANSWER={ans!r} interdit pour {spec['type']}"))

    ey=[parse_evidence(x) for x in sections_all(block,'EVIDENCE_YES',['EVIDENCE_NO','LATER','WHY'])]
    en=[parse_evidence(x) for x in sections_all(block,'EVIDENCE_NO',['EVIDENCE_YES','LATER','WHY'])]
    fs_list=[parse_evidence(x) for x in sections_all(block,'FOUND_SOURCE',['CRITERIA','WHY'])]
    fs=fs_list[0] if fs_list else parse_evidence('')
    all_evs=ey+en+fs_list

    # V5.1 normalization: repeated EVIDENCE_YES/NO blocks are accepted as an evidence list.
    # This resolves atoms with multiple REQUIRED sources without changing the frozen prompt bytes.
    for label,arr in [('EVIDENCE_YES',ey),('EVIDENCE_NO',en)]:
        ids=[e['source_id'] for e in arr if e['source_id']!='NONE']
        if len(ids)!=len(set(ids)):
            issues.append(issue('DUPLICATE_EVIDENCE_SOURCE',f'{label} répète la même SOURCE_ID'))

    reqs=spec.get('required') or []
    if reqs:
        opened_ids={e['source_id'] for e in all_evs if e['opened']=='YES'}
        missing=[r for r in reqs if r not in opened_ids]
        if missing:
            if spec['type']=='TEXT' and ans in {'YES','NO'}:
                issues.append(issue('TEXT_REQUIRED_NOT_OPENED',f"Source(s) REQUIRED non ouverte(s): {', '.join(missing)}; réponse ferme interdite"))
            else:
                issues.append(issue('REQUIRED_NOT_OPENED',f"Source(s) REQUIRED non ouverte(s): {', '.join(missing)}"))

    if spec['type'] in {'TEXT','DATA'}:
        supports=ey if ans=='YES' else (en if ans=='NO' else [])
        if supports:
            opened=[e for e in supports if e['opened']=='YES']
            if not opened:
                issues.append(issue('SUPPORT_NOT_OPENED','Aucune preuve soutenant la réponse ferme n\'est OPENED:YES'))
            if spec['type']=='TEXT' and not any(e['opened']=='YES' and e['status']=='DIRECT' for e in supports):
                issues.append(issue('TEXT_SUPPORT_NOT_DIRECT','Atome TEXT ferme exige au moins une preuve DIRECT et OPENED:YES'))
            cutoff=iso(spec.get('cutoff') or '')
            if cutoff:
                for e in supports:
                    if e['source_id']=='NONE' or e['opened']!='YES': continue
                    sd=iso(e['date'])
                    if sd is None:
                        issues.append(issue('SUPPORT_DATE_UNKNOWN',f"Date de preuve {e['date']!r} incompatible avec contrôle cutoff {cutoff}"))
                    elif sd>cutoff:
                        issues.append(issue('CUTOFF_VIOLATION',f"Preuve {e['source_id']} du {sd} postérieure au cutoff {cutoff}"))
    elif spec['type']=='SEARCH':
        if ans=='FOUND':
            if fs['opened']!='YES': issues.append(issue('SEARCH_FOUND_NOT_OPENED','FOUND exige FOUND_SOURCE OPENED:YES'))
            cutoff=iso(spec.get('cutoff') or '')
            sd=iso(fs['date'])
            if cutoff:
                if sd is None: issues.append(issue('SEARCH_FOUND_DATE_UNKNOWN','FOUND exige une date vérifiable'))
                elif sd>cutoff: issues.append(issue('SEARCH_CUTOFF_VIOLATION',f"FOUND_SOURCE du {sd} postérieure au cutoff {cutoff}"))
        if ans=='NOT_FOUND':
            why=get(block,'WHY','') or ''
            low=why.lower()
            existential=['n’existe pas',"n'existe pas",'does not exist','aucune source n’existe','aucune étude n’existe']
            if any(x in low for x in existential):
                warnings.append(issue('NOT_FOUND_EXISTENTIAL_LANGUAGE','NOT_FOUND est formulé comme inexistence',severity='WARNING'))

    for name,arr in [('EVIDENCE_YES',ey),('EVIDENCE_NO',en),('FOUND_SOURCE',fs_list)]:
        for e in arr:
            if e['source_id']!='NONE':
                wc=words(e['excerpt'])
                if wc>25:
                    warnings.append(issue('EXCERPT_TOO_LONG',f'{name} {e["source_id"]} EXACT_EXCERPT={wc} mots (>25)',severity='WARNING'))
                canon=source_types.get(e['source_id'])
                if canon and e['source_type'] not in {canon,'NONE'}:
                    warnings.append(issue('SOURCE_TYPE_MISMATCH',f"{e['source_id']}: modèle={e['source_type']}, canonique={canon}",severity='WARNING'))

    low=(get(block,'WHY','') or '').lower()
    vague=['robuste','consensuelle','consensuel','crédible','credible']
    if any(v in low for v in vague):
        warnings.append(issue('VAGUE_EVALUATIVE_LANGUAGE','WHY contient un qualificatif évaluatif à éviter',severity='WARNING'))

    return {
      'atom':aid,'type':typ,'answer':ans,
      'status':'VALID' if not issues else 'PROTOCOL_INVALID',
      'errors':issues,'warnings':warnings
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('result')
    ap.add_argument('--prompt',required=True)
    ap.add_argument('--manifest',required=True)
    ap.add_argument('--json',dest='json_out')
    ap.add_argument('--markdown',dest='md_out')
    args=ap.parse_args()
    prompt=Path(args.prompt); manifest=json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    actual=hashlib.sha256(prompt.read_bytes()).hexdigest()
    if actual!=manifest['prompt_sha256']:
        print('RUN_INVALID: prompt hash mismatch',file=sys.stderr); return 3
    specs={x['id']:x for x in manifest['atoms']}
    blocks=parse_result(Path(args.result).read_text(encoding='utf-8'))
    byid={}; duplicates=[]
    for aid,b in blocks:
        if aid in byid: duplicates.append(aid)
        else: byid[aid]=b
    missing=[x for x in specs if x not in byid]
    extra=[x for x in byid if x not in specs]
    atom_reports=[]
    for aid,spec in specs.items():
        if aid in byid: atom_reports.append(validate_atom(aid,byid[aid],spec,manifest.get('canonical_source_types',{})))
    structural=[]
    if missing: structural.append({'code':'MISSING_ATOMS','items':missing})
    if duplicates: structural.append({'code':'DUPLICATE_ATOMS','items':duplicates})
    if extra: structural.append({'code':'UNEXPECTED_ATOMS','items':extra})
    valid=sum(r['status']=='VALID' for r in atom_reports)
    invalid=sum(r['status']!='VALID' for r in atom_reports)
    warn=sum(len(r['warnings']) for r in atom_reports)
    report={
      'protocol':manifest['protocol'],'prompt_sha256':actual,'result_file':str(Path(args.result).name),
      'expected_atoms':len(specs),'parsed_unique_atoms':len(byid),'valid_atoms':valid,'invalid_atoms':invalid,
      'warnings':warn,'structural_errors':structural,'atoms':atom_reports,
      'run_status':'STRUCTURAL_INVALID' if structural else ('PROTOCOL_INVALID' if invalid else 'VALID')
    }
    if args.json_out: Path(args.json_out).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=[f"# Validation {manifest['protocol']}",'',f"- Run: `{report['result_file']}`",f"- Statut: **{report['run_status']}**",f"- Atomes attendus: {report['expected_atoms']}",f"- Atomes valides: {valid}",f"- Atomes `PROTOCOL_INVALID`: {invalid}",f"- Warnings: {warn}",'']
    if structural:
        lines+=['## Erreurs structurelles','']+[f"- `{e['code']}`: {', '.join(e['items'])}" for e in structural]+['']
    if invalid:
        lines+=['## Atomes invalides','']
        for r in atom_reports:
            if r['status']!='VALID':
                lines.append(f"### {r['atom']} — {r['answer']}")
                lines += [f"- `{e['code']}`: {e['message']}" for e in r['errors']]
                lines.append('')
    if warn:
        lines+=['## Warnings','']
        for r in atom_reports:
            for w in r['warnings']:
                lines.append(f"- {r['atom']} `{w['code']}`: {w['message']}")
        lines.append('')
    lines+=['## Matrice','', '| Atome | Réponse | Validation |', '|---|---|---|']
    lines += [f"| {r['atom']} | {r['answer']} | {r['status']} |" for r in atom_reports]
    md='\n'.join(lines)+'\n'
    if args.md_out: Path(args.md_out).write_text(md,encoding='utf-8')
    else: print(md)
    return 3 if structural else (2 if invalid else 0)
if __name__=='__main__': raise SystemExit(main())
