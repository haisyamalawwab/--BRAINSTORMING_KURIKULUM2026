#!/usr/bin/env python3
"""Generator RPS Markdown berbasis data; susunan isi merujuk template SWO, bukan renderer DOCX."""
import argparse
import json
from pathlib import Path
import re
import sys


class DataError(ValueError):
    pass


def validate(d):
    def fail(message):
        raise DataError(message)
    def text(obj, key, where):
        if not isinstance(obj, dict) or not isinstance(obj.get(key), str) or not obj[key].strip():
            fail(f'{where}.{key}: wajib berupa teks tidak kosong')
        return obj[key]
    def array(obj, key, where):
        if not isinstance(obj, dict) or not isinstance(obj.get(key), list) or not obj[key]:
            fail(f'{where}.{key}: wajib berupa daftar tidak kosong')
        return obj[key]
    def integer(obj, key, where, lo=0, hi=100):
        x = obj.get(key) if isinstance(obj, dict) else None
        if type(x) is not int or not lo <= x <= hi:
            fail(f'{where}.{key}: wajib bilangan bulat {lo}–{hi}')
        return x
    def ids(items, where):
        result = []
        for i, item in enumerate(items):
            result.append(text(item, 'id', f'{where}[{i}]'))
        if len(result) != len(set(result)):
            fail(f'{where}: id harus unik')
        return set(result)
    def references(values, allowed, where):
        if not isinstance(values, list) or not values or any(not isinstance(x, str) or x not in allowed for x in values):
            fail(f'{where}: daftar id tidak boleh kosong dan harus merujuk data yang ada')
        if len(set(values)) != len(values):
            fail(f'{where}: id duplikat')
    if not isinstance(d, dict):
        fail('data: akar JSON harus objek')
    for k in ('judul','status','sumber','konteks','deskripsi','bahan_kajian','lingkup','catatan_beban','catatan_evaluasi'):
        text(d, k, 'data')
    identity = d.get('identitas')
    for k in ('universitas','fakultas','prodi','no_dokumen','mk','kode','rumpun','tanggal_penyusunan','penyusun','nuptk','pengembang','koordinator','ketua_prodi','pengampu','prasyarat','periode'):
        text(identity,k,'identitas')
    for k in ('sks_teori','sks_praktik'):
        integer(identity,k,'identitas',0,20)
    if identity['sks_teori'] + identity['sks_praktik'] == 0:
        fail('identitas: total SKS harus positif')
    integer(identity,'semester','identitas',1,20)
    cpl = array(d,'cpl','data'); cpmk = array(d,'cpmk','data'); subs = array(d,'subcpmk','data')
    cplids=ids(cpl,'cpl'); cpids=ids(cpmk,'cpmk'); subids=ids(subs,'subcpmk')
    for i,x in enumerate(cpl):
        for k in ('display','rumusan','irm'): text(x,k,f'cpl[{i}]')
    for i,x in enumerate(cpmk):
        for k in ('rumusan','bloom'): text(x,k,f'cpmk[{i}]')
        references(x.get('cpl'),cplids,f'cpmk[{i}].cpl')
    for i,x in enumerate(subs):
        for k in ('rumusan','bloom','cpmk'): text(x,k,f'subcpmk[{i}]')
        if x['cpmk'] not in cpids: fail(f'subcpmk[{i}].cpmk: id tidak dikenal')
    ref = array(d,'referensi','data'); refids=[]
    for i,x in enumerate(ref):
        refids.append(integer(x,'id',f'referensi[{i}]',1,9999))
        text(x,'nama',f'referensi[{i}]'); text(x,'url',f'referensi[{i}]')
        if x.get('jenis') not in ('utama','pendukung'): fail(f'referensi[{i}].jenis harus utama atau pendukung')
    if len(set(refids)) != len(refids): fail('referensi: id duplikat')
    levels=array(d,'level_rubrik','data')
    if len(levels) < 2 or any(not isinstance(x,str) or not x.strip() for x in levels) or len(set(levels)) != len(levels):
        fail('level_rubrik: minimal dua label teks unik')
    ass=array(d,'asesmen','data'); aids=ids(ass,'asesmen')
    if aids != {'tugas1','uts','tugas2','uas'} or len(ass)!=4:
        fail('asesmen: harus tepat empat id tugas1, uts, tugas2, uas')
    if sum(integer(x,'bobot','asesmen',1,100) for x in ass)!=100: fail('asesmen: total bobot MK harus 100%')
    for i,x in enumerate(ass):
        where=f'asesmen[{i}]'
        for k in ('nama','soal'): text(x,k,where)
        week=integer(x,'week',where,1,16)
        if x['id']=='uts' and week!=8 or x['id']=='uas' and week!=16: fail(f'{where}: UTS minggu 8 dan UAS minggu 16 sesuai template')
        references(x.get('cpmk'),cpids,where+'.cpmk')
        rubric=array(x,'rubrik',where)
        for j,r in enumerate(rubric):
            text(r,'kriteria',f'{where}.rubrik[{j}]'); integer(r,'bobot',f'{where}.rubrik[{j}]',1,100)
            desc=array(r,'deskriptor',f'{where}.rubrik[{j}]')
            if len(desc)!=len(levels) or any(not isinstance(z,str) or not z.strip() for z in desc):
                fail(f'{where}.rubrik[{j}]: deskriptor harus sesuai jumlah level')
        if sum(r['bobot'] for r in rubric)!=100: fail(f'{where}.rubrik: total bobot kriteria harus 100%')
    weeks=array(d,'minggu','data')
    if len(weeks)!=16 or [x.get('week') if isinstance(x,dict) else None for x in weeks]!=list(range(1,17)):
        fail('minggu: harus tepat 16 baris berurutan 1–16')
    for i,w in enumerate(weeks):
        where=f'minggu[{i}]'
        integer(w,'week',where,1,16)
        for k in ('indikator','kriteria_teknik','luring','daring','materi'): text(w,k,where)
        references(w.get('subcpmk'),subids,where+'.subcpmk')
        if not isinstance(w.get('referensi'),list) or not w['referensi'] or any(type(x) is not int or x not in refids for x in w['referensi']): fail(where+'.referensi: nomor pustaka tidak dikenal')
        expected=[x['id'] for x in ass if x['week']==w['week']]
        if not isinstance(w.get('asesmen'),list) or len(set(w['asesmen'])) != len(w['asesmen']) or set(w['asesmen']) != set(expected): fail(where+'.asesmen: harus sesuai jadwal asesmen, tanpa duplikat')
        parents={x['cpmk'] for x in subs if x['id'] in w['subcpmk']}
        if any(not set(x['cpmk']).issubset(parents) for x in ass if x['week']==w['week']): fail(where+': CPMK asesmen tidak termasuk induk Sub-CPMK minggu ini')
    v=d.get('validasi')
    for k in ('tempat_tanggal','upm','upm_nuptk','dosen','dosen_nuptk','ketua_prodi','ketua_prodi_nuptk'): text(v,k,'validasi')
    # Placeholder template tidak boleh terbawa ke isi; tautan Markdown dan [1] pustaka diperbolehkan.
    raw=json.dumps(d,ensure_ascii=False)
    if re.search(r'\{\{[^{}]+\}\}|\[(?:nocpl|cpl|nocpmk|cpmk|nosubcpmk|subcpmk|tabelkolerasi|pustakautama|pustakapendukung|mingguke|kemampuan_subcpmk|indikator|kriteriateknik|luring|daring|materi|bobot_nilai|penugasan1|rubriktugas1|soaluts|rubrikuts|tugas2|rubriktugas2|soaluas|rubrikuas)\]',raw,re.I):
        fail('data: placeholder template belum diisi')
    return d


def table(head,rows):
    def cell(v): return str(v).replace('|',r'\|').replace('\n','<br>')
    return '\n'.join(['| '+' | '.join(map(cell,head))+' |','| '+' | '.join('---' for _ in head)+' |']+['| '+' | '.join(map(cell,r))+' |' for r in rows])


def render(d):
    validate(d)
    I=d['identitas']; V=d['validasi']; ass=d['asesmen']; cpls={x['id']:x for x in d['cpl']}
    parts=[f"# {d['judul']}", f"## {I['kode']} — {I['mk']}", f"> **Status:** {d['status']}",f"**Sumber dan batas:** {d['sumber']}",
           f"## Sampul\n\n**RENCANA PEMBELAJARAN SEMESTER (RPS)**<br>\n{I['universitas']}<br>\nDisusun oleh: {I['penyusun']}<br>\nNUPTK: {I['nuptk']}<br>\nPeriode: {I['periode']}",
           '## Identitas dan otorisasi',table(['Atribut','Isi'],[['Institusi',I['universitas']],['Fakultas',I['fakultas']],['Program studi',I['prodi']],['Nomor dokumen',I['no_dokumen']],['Mata kuliah',I['mk']],['Kode',I['kode']],['Rumpun MK',I['rumpun']],['Bobot SKS',f"{I['sks_teori']+I['sks_praktik']} (T={I['sks_teori']}; P={I['sks_praktik']})"],['Semester',I['semester']],['Tanggal penyusunan',I['tanggal_penyusunan']],['Dosen pengampu',I['pengampu']],['Mata kuliah prasyarat',I['prasyarat']]]),
           table(['Pengembang RPS','Koordinator RMK','Ketua Program Studi'],[[I['pengembang'],I['koordinator'],I['ketua_prodi']]]),d['konteks'],
           '## CPL dibebankan',table(['CPL dibebankan','Rumusan resmi','IRM'],[[x['display'],x['rumusan'],x['irm']] for x in d['cpl']]),
           '## CPMK dan Sub-CPMK',table(['Kode','Rumusan usulan: mahasiswa (A)','Bloom','CPL'],[[f"`{x['id']}`",x['rumusan'],x['bloom'],', '.join(cpls[k]['display'] for k in x['cpl'])] for x in d['cpmk']]),
           table(['Kode','Kemampuan operasional','CPMK','Bloom'],[[f"`{x['id']}`",x['rumusan'],f"`{x['cpmk']}`",x['bloom']] for x in d['subcpmk']]),
           '## Korelasi CPL terhadap CPMK',table(['CPL / CPMK']+[x['id'] for x in d['cpmk']],[[x['display']]+['✓' if x['id'] in c['cpl'] else '—' for c in d['cpmk']] for x in d['cpl']]),
           '## Deskripsi singkat mata kuliah\n\n'+d['deskripsi'],'## Bahan kajian: materi pembelajaran\n\n'+d['bahan_kajian'],'## Lingkup dan fasilitas\n\n'+d['lingkup'],
           '## Pustaka\n\nPengelompokan utama/pendukung adalah usulan untuk mengikuti struktur template; nomor merujuk sumber yang tercantum dalam data MK.',
           '### Utama\n\n'+'\n'.join(f"- [{r['id']}] {r['nama']} {r['url']}" for r in d['referensi'] if r['jenis']=='utama'),
           '### Pendukung\n\n'+'\n'.join(f"- [{r['id']}] {r['nama']} {r['url']}" for r in d['referensi'] if r['jenis']=='pendukung'),
           '## Rencana 16 pertemuan\n\n'+d['catatan_beban']+'\n\nTM = tatap muka; PT = penugasan terstruktur; BM = belajar mandiri.']
    am={x['id']:x for x in ass}
    parts.append(table(['Mg','Kemampuan akhir (Sub-CPMK)','Indikator','Kriteria & teknik','Luring: bentuk, metode, tugas [waktu]','Daring: bentuk, metode, tugas [waktu]','Materi pembelajaran [pustaka]','Bobot penilaian'],[[w['week'],', '.join(f"`{x}`" for x in w['subcpmk']),w['indikator'],w['kriteria_teknik'],w['luring'],w['daring'],w['materi']+' '+', '.join(f'[{x}]' for x in w['referensi']), ' + '.join(str(am[x]['bobot'])+'%' for x in w['asesmen']) if w['asesmen'] else '0%'] for w in d['minggu']]+[['**Total**','','','','','','','**100%**']]))
    parts.append('## Evaluasi dan pemetaan\n\nBobot adalah kontribusi instrumen ke nilai MK, bukan nilai ketercapaian CPL. Tanda ✓ menunjukkan pemetaan tanpa membagi atau menjumlahkan bobot ke CPMK jika ada instrumen yang mengukur lebih dari satu CPMK.')
    matrix=[]
    multimap=any(len(a['cpmk'])>1 for a in ass)
    for cp in d['cpmk']:
        vals=[a['bobot'] if cp['id'] in a['cpmk'] else 0 for a in ass]
        cells=[('✓' if multimap else str(v)+'%') if v else '—' for v in vals]
        matrix.append([f"`{cp['id']}` / "+', '.join(f'`{c}`' for c in cp['cpl'])]+cells+['—' if multimap else str(sum(vals))+'%'])
    matrix.append(['**Total nilai MK**']+[f"**{a['bobot']}%**" for a in ass]+['**100%**'])
    parts.append(table(['CPMK / CPL']+[f"{a['nama']} Mg {a['week']}" for a in ass]+['Total'],matrix)); parts.append(d['catatan_evaluasi'])
    parts.append('## Lampiran soal dan rubrik\n\nSkala dan deskriptor di bawah mengikuti data sumber; bobot kriteria dihitung di dalam masing-masing instrumen, bukan tambahan terhadap bobot MK.')
    for a in ass:
        parts.extend([f"### {a['nama']} — minggu {a['week']}, {a['bobot']}% MK, {', '.join(a['cpmk'])}",'**Soal / penugasan**\n\n'+a['soal'],'**Rubrik penilaian**',table(['Kriteria','Bobot']+d['level_rubrik'],[[r['kriteria'],str(r['bobot'])+'%']+r['deskriptor'] for r in a['rubrik']])])
    parts.extend(['## Validasi dan pengesahan\n\nBelum ditandatangani; nama, NUPTK dan tanggal diisi setelah penetapan.',table(['Memvalidasi: Unit Penjaminan Mutu','Dosen pengampu','Mengesahkan: Ketua Program Studi'],[[f"{V['upm']}<br>NUPTK: {V['upm_nuptk']}",f"{V['dosen']}<br>NUPTK: {V['dosen_nuptk']}",f"{V['ketua_prodi']}<br>NUPTK: {V['ketua_prodi_nuptk']}"]]),f"Tempat/tanggal: {V['tempat_tanggal']}"])
    return '\n\n'.join(parts)+'\n'


def main(argv=None):
    ap=argparse.ArgumentParser(description='Susun RPS Markdown dari JSON kurasi, mengikuti struktur template SWO. Tidak menghasilkan DOCX/PDF.')
    ap.add_argument('input',type=Path,help='data JSON mata kuliah')
    ap.add_argument('--output','-o',type=Path,help='file Markdown tujuan')
    ap.add_argument('--force',action='store_true',help='izinkan menimpa file tujuan yang sudah ada')
    ap.add_argument('--check',action='store_true',help='validasi tanpa menulis; dengan --output juga periksa kesamaan hasil')
    args=ap.parse_args(argv)
    try:
        if not args.check and not args.output: ap.error('--output wajib kecuali menggunakan --check')
        if args.force and args.check: ap.error('--force tidak dapat digabung dengan --check')
        if args.output and args.output.suffix.lower() != '.md': raise DataError('output harus berekstensi .md')
        if args.output and args.input.resolve()==args.output.resolve(): raise DataError('input dan output tidak boleh sama')
        data=json.loads(args.input.read_text(encoding='utf-8')); result=render(data)
        if args.check:
            if args.output and args.output.read_text(encoding='utf-8') != result: raise DataError('output tidak sama dengan hasil dari data')
            print('Valid'+(' dan output sesuai data' if args.output else '')+'. Persetujuan akademik tidak diperiksa.')
        else:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            with args.output.open('w' if args.force else 'x',encoding='utf-8',newline='\n') as f: f.write(result)
            print('Ditulis:',args.output)
        return 0
    except (DataError, OSError, json.JSONDecodeError, TypeError, KeyError) as e:
        print('Kesalahan:',e,file=sys.stderr); return 1

if __name__=='__main__': sys.exit(main())
