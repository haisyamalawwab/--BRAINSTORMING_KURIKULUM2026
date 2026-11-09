#!/usr/bin/env python3
"""Isi template SWO dari JSON kurasi yang sama dengan generator Markdown."""
import argparse
from copy import deepcopy
from pathlib import Path
import re
import sys
import json

try:
    from docx import Document
    from docx.oxml.ns import qn
    from docx.shared import Pt, Cm
except ImportError:
    print('Pasang dependensi: python3 -m pip install -r KURIKULUM2026_REVISI/_tools/requirements-rps-docx.txt',file=sys.stderr)
    sys.exit(1)
from generate_rps_md import validate, DataError

TEMPLATE=Path(__file__).resolve().parents[1]/'Template_RPS_GEN_2026_20092026-SWO.docx'
TAGS=re.compile(r'\{\{[^{}]+\}\}|\[(?:nocpl|cpl|nocpmk|cpmk|nosubcpmk|subcpmk|tabelkolerasi|pustakautama|pustakapendukung|mingguke|kemampuan_subcpmk|indikator|kriteriateknik|luring|daring|materi|bobot_nilai|penugasan1|rubriktugas1|soaluts|rubrikuts|tugas2|rubriktugas2|soaluas|rubrikuas)\]',re.I)


def plain(s):
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',str(s))
    s=s.replace('**','').replace('`','')
    return re.sub(r'(?<!\w)\*([^*\n]+)\*(?!\w)',r'\1',s)


def unique(row):
    found=[]; seen=set()
    for cell in row.cells:
        if cell._tc not in seen:
            found.append(cell); seen.add(cell._tc)
    return found


def text(cell,value):
    cell.text=plain(value)
    for p in cell.paragraphs:
        p.paragraph_format.space_after=Pt(0)
        for r in p.runs: r.font.size=Pt(8)


def paragraphs(doc):
    def walk(t):
        seen=set()
        for row in t.rows:
            for cell in row.cells:
                if cell._tc in seen: continue
                seen.add(cell._tc)
                yield from cell.paragraphs
                for inner in cell.tables: yield from walk(inner)
    yield from doc.paragraphs
    for t in doc.tables: yield from walk(t)
    for section in doc.sections:
        for area in (section.header,section.footer):
            yield from area.paragraphs
            for t in area.tables: yield from walk(t)


def replace_paragraph(p, mapping):
    original=p.text; s=original
    for a,b in mapping.items(): s=s.replace(a,plain(b))
    if s!=original:
        if p.runs:
            p.runs[0].text=s
            for r in p.runs[1:]: r.text=''
        else: p.add_run(s)


def tagcell(t,tag):
    cells=[];seen=set()
    for row in t.rows:
        for c in row.cells:
            if c._tc not in seen and tag in c.text:
                cells.append(c);seen.add(c._tc)
    return cells


def expand(t,idtag,bodytag,items):
    # Template's three fixed row groups contain merged first-column cells.
    rows=[r for r in t.rows if any(idtag in c.text for c in unique(r))]
    if not rows: raise DataError('template tidak memiliki baris '+idtag)
    while len(rows)<len(items):
        new=deepcopy(rows[-1]._tr); rows[-1]._tr.addnext(new)
        rows=[r for r in t.rows if any(idtag in c.text for c in unique(r))]
    for idx,row in enumerate(rows):
        cells=unique(row)
        idcell=next((c for c in cells if idtag in c.text),None)
        bodycell=next((c for c in cells if bodytag in c.text),None)
        if not idcell or not bodycell: raise DataError('struktur baris template tidak sesuai '+idtag)
        code,body=items[idx] if idx<len(items) else ('','')
        text(idcell,code);text(bodycell,body)


def setblock(table,tag,value):
    cells=tagcell(table,tag)
    if len(cells)!=1: raise DataError(f'template: {tag} seharusnya muncul satu kali, ditemukan {len(cells)}')
    text(cells[0],value)
    return cells[0]


def nested(cell, header, rows):
    t=cell.add_table(rows=1,cols=len(header));t.style='Table Grid';t.autofit=True
    for c,v in zip(t.rows[0].cells,header): text(c,v)
    for row in rows:
        for c,v in zip(t.add_row().cells,row): text(c,v)
    return t


def build(d,template=TEMPLATE):
    validate(d);doc=Document(template)
    if len(doc.tables)!=12: raise DataError('template harus memiliki 12 tabel utama SWO')
    cover,identity,weekly=doc.tables[:3];I=d['identitas'];V=d['validasi']
    # Hapus identitas Teknik Mesin hardcoded, bukan nilai MK tujuan.
    header=unique(identity.rows[0])[1]
    ps=[p for p in header.paragraphs if p.text.strip()]
    if len(ps)<3: raise DataError('header template tidak sesuai')
    for p,value in zip(ps[:3],[I['universitas'],I['fakultas'], 'PROGRAM STUDI '+I['prodi']]):
        if p.runs:
            p.runs[0].text=plain(value)
            for r in p.runs[1:]:r.text=''
        else:p.add_run(plain(value))
    cover.rows[0].cells[0].add_paragraph('DRAF: '+plain(d['status']))
    expand(identity,'[nocpl]','[cpl]',[(x['display'],x['rumusan']+' (IRM: '+x['irm']+')') for x in d['cpl']])
    expand(identity,'[nocpmk]','[cpmk]',[(x['id'],x['rumusan']+' ('+x['bloom']+'); CPL: '+', '.join(x['cpl'])) for x in d['cpmk']])
    expand(identity,'[nosubcpmk]','[subcpmk]',[(x['id'],x['rumusan']+' ('+x['bloom']+'); '+x['cpmk']) for x in d['subcpmk']])
    c=setblock(identity,'[tabelkolerasi]','Korelasi CPL terhadap CPMK')
    nested(c,['CPL / CPMK']+[x['id'] for x in d['cpmk']],[[x['id']]+['✓' if x['id'] in y['cpl'] else '—' for y in d['cpmk']] for x in d['cpl']])
    c.add_paragraph('Pemetaan instrumen: bobot adalah kontribusi ke nilai MK, bukan skor CPL.')
    nested(c,['Asesmen','Minggu','Bobot MK','CPMK'],[[a['nama'],a['week'],str(a['bobot'])+'%',', '.join(a['cpmk'])] for a in d['asesmen']])
    c.add_paragraph(plain(d['konteks']))
    for kind,tag in [('utama','[pustakautama]'),('pendukung','[pustakapendukung]')]:
        vals=[f"[{x['id']}] {x['nama']} {x['url']}" for x in d['referensi'] if x['jenis']==kind]
        setblock(identity,tag,'\n'.join(vals) if vals else 'Belum ditetapkan')
    # Ganti seluruh baris data, termasuk sel UTS/UAS yang di-merge, dengan 16 baris 8 kolom.
    trs=weekly._tbl.findall(qn('w:tr'))
    if len(trs)!=17: raise DataError('jumlah baris tabel minggu template tidak sesuai')
    proto=deepcopy(trs[3]); anchor=trs[2]
    for tr in trs[3:-1]:weekly._tbl.remove(tr)
    for w in d['minggu']:
        tr=deepcopy(proto);anchor.addnext(tr);anchor=tr
        pr=tr.get_or_add_trPr();h=pr.find(qn('w:tblHeader'))
        if h is not None:pr.remove(h)
    amap={a['id']:a for a in d['asesmen']}
    for i,w in enumerate(d['minggu']):
        row=weekly.rows[i+3];cells=unique(row)
        if len(cells)!=8:raise DataError('tabel minggu harus memiliki 8 kolom')
        vals=[w['week'],', '.join(w['subcpmk']),w['indikator'],w['kriteria_teknik'],w['luring'],w['daring'],w['materi']+' '+', '.join(f'[{x}]' for x in w['referensi']),' + '.join(str(amap[a]['bobot'])+'%' for a in w['asesmen']) or '0%']
        for c,val in zip(cells,vals):text(c,val)
    total=unique(weekly.rows[-1]);text(total[-1],'100%')
    # Empat soal dan rubrik pada kotak lampiran asli.
    for j,key in enumerate(('tugas1','uts','tugas2','uas')):
        a=amap[key];soal=doc.tables[3+2*j].cell(0,0);rub=doc.tables[4+2*j].cell(0,0)
        text(soal,f"{a['nama']} — minggu {a['week']}; {a['bobot']}% MK; CPMK: {', '.join(a['cpmk'])}\n\n{a['soal']}")
        text(rub,'Bobot kriteria berjumlah 100% dalam instrumen; skala sesuai sumber MK.')
        nested(rub,['Kriteria','Bobot']+d['level_rubrik'],[[r['kriteria'],str(r['bobot'])+'%']+r['deskriptor'] for r in a['rubrik']])
    # Lembar pengesahan harus kosong dari identitas dan tanggal contoh template.
    sign=doc.tables[11]
    text(sign.cell(0,0),f"Memvalidasi,\nUnit Penjaminan Mutu\n{I['fakultas']}\n\n\n{V['upm']}\nNUPTK: {V['upm_nuptk']}")
    text(sign.cell(0,1),f"{V['tempat_tanggal']}\nDosen Pengampu,\n\n\n{V['dosen']}\nNUPTK: {V['dosen_nuptk']}")
    text(sign.cell(1,0),f"Mengesahkan,\nKetua Program Studi {I['prodi']}\n\n\n{V['ketua_prodi']}\nNUPTK: {V['ketua_prodi_nuptk']}")
    # Pertahankan catatan sumber dan pembobotan dalam dokumen Word.
    setblock(identity,'{{bahankajian}}',d['bahan_kajian']+'\n\n'+d['lingkup'])
    setblock(identity,'{{deskripsimk}}',d['deskripsi']+'\n\n'+d['status']+'\nSumber: '+d['sumber'])
    # Tambah catatan waktu dan penilaian sesudah tabel, dalam orientasi lanskap.
    for p in doc.paragraphs:
        if p.text.strip().startswith('Catatan : TM'):
            p.add_run('\n'+plain(d['catatan_beban'])+'\n'+plain(d['catatan_evaluasi']))
            break
    scalars={'{{namamk}}':I['mk'],'{{kodemk}}':I['kode'],'{{rumpunmk}}':I['rumpun'],'{{skst}}':I['sks_teori'],'{{sksp}}':I['sks_praktik'],'{{sms}}':I['semester'],'{{tglsusun}}':I['tanggal_penyusunan'],'071030.{{kodeprodi}}':I['no_dokumen'],'{{pengembangrps}}':I['pengembang'],'{{koordinatormk}}':I['koordinator'],'{{ketuaprodi}}':I['ketua_prodi'],'{{prodi}}':I['prodi'],'{{namadosen}}':I['penyusun'],'{{nuptk}}':I['nuptk'],'{{dosenpengampu}}':I['pengampu'],'{{mkprasyarat}}':I['prasyarat'],'AGUSTUS, 2026':I['periode']}
    for p in paragraphs(doc):replace_paragraph(p,scalars)
    leftovers=TAGS.findall('\n'.join(p.text for p in paragraphs(doc)))
    if leftovers:raise DataError('placeholder template tersisa: '+', '.join(sorted(set(leftovers))))
    return doc


def main():
    ap=argparse.ArgumentParser(description='Isi template DOCX SWO dengan JSON kurasi RPS. Tidak otomatis mengurai Markdown.')
    ap.add_argument('input',type=Path);ap.add_argument('-o','--output',type=Path,required=True);ap.add_argument('--template',type=Path,default=TEMPLATE);ap.add_argument('--force',action='store_true')
    a=ap.parse_args()
    try:
        if a.output.suffix.lower()!='.docx':raise DataError('output harus .docx')
        if a.output.resolve() in (a.input.resolve(),a.template.resolve()):raise DataError('output tidak boleh menimpa input atau template')
        d=json.loads(a.input.read_text(encoding='utf-8'));doc=build(d,a.template)
        a.output.parent.mkdir(parents=True,exist_ok=True)
        with a.output.open('wb' if a.force else 'xb') as f:doc.save(f)
        print('Ditulis:',a.output);return 0
    except (OSError,DataError,TypeError,KeyError,ValueError) as e:
        print('Kesalahan:',e,file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
