#!/usr/bin/env python3
"""Uji generator, CLI, dan kesesuaian data STI-311 dengan paket revisi."""
import copy
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

import generate_rps_md as gen

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'PERANGKAT_AJAR'
DATA=P/'_data/065_STI-311_RPS.json'
RPS=P/'065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md'
SCRIPT=Path(gen.__file__)


def fixture():
    # Data fiktif berbeda dengan jumlah CPMK, pemetaan, skala dan bobot berbeda.
    i={k:'Belum ditetapkan' for k in ('no_dokumen','tanggal_penyusunan','penyusun','nuptk','pengembang','koordinator','ketua_prodi','pengampu','periode')}
    i.update(universitas='Universitas Contoh',fakultas='Fakultas Contoh',prodi='S1 Contoh',mk='Metode Penelitian',kode='TES-001',rumpun='Riset',sks_teori=3,sks_praktik=0,semester=2,prasyarat='Tidak ada')
    v={k:'Belum ditetapkan' for k in ('tempat_tanggal','upm','upm_nuptk','dosen','dosen_nuptk','ketua_prodi','ketua_prodi_nuptk')}
    cp=[dict(id=f'CP-{n}',rumusan=f'Kompetensi riset {n}',bloom='C3',cpl=['PL-A' if n%2 else 'PL-B']) for n in range(1,6)]
    subs=[dict(id=f'SUB-{n}',rumusan=f'Tahapan riset {n}',cpmk=f'CP-{n}',bloom='C3') for n in range(1,6)]
    specs=[('tugas1','Tugas riset',3,10,['CP-1']),('uts','UTS riset',8,30,['CP-2']),('tugas2','Tugas analisis',11,20,['CP-3']),('uas','UAS riset',16,40,['CP-4','CP-5'])]
    ass=[dict(id=id,nama=nm,week=w,bobot=weight,cpmk=c,soal=f'Soal metode {nm}',rubrik=[dict(kriteria='Kesesuaian metode',bobot=60,deskriptor=['Unggul','Memadai','Perlu perbaikan']),dict(kriteria='Bukti',bobot=40,deskriptor=['Lengkap','Sebagian','Tidak ada'])]) for id,nm,w,weight,c in specs]
    weeks=[]
    for n in range(1,17):
        ids=['SUB-1'] if n<8 else ['SUB-2'] if n<11 else ['SUB-3'] if n<16 else ['SUB-4','SUB-5']
        weeks.append(dict(week=n,subcpmk=ids,indikator=f'Indikator riset {n}',kriteria_teknik='Uji argumentasi',luring='Diskusi 100 menit',daring='Diskusi daring 100 menit',materi=f'Metode observasi {n}',referensi=[7],asesmen=[a['id'] for a in ass if a['week']==n]))
    return dict(judul='RPS Contoh',status='Fiktif',sumber='Contoh uji',identitas=i,konteks='Uji',cpl=[dict(id='PL-A',display='PL-A',rumusan='Rumusan A',irm='R'),dict(id='PL-B',display='PL-B',rumusan='Rumusan B',irm='I')],cpmk=cp,subcpmk=subs,deskripsi='Penelitian',bahan_kajian='Observasi',lingkup='Riset',referensi=[dict(id=7,nama='Buku Contoh',url='https://example.org',jenis='utama')],catatan_beban='Alokasi contoh',minggu=weeks,level_rubrik=['Baik','Cukup','Kurang'],asesmen=ass,catatan_evaluasi='Bobot instrumen tidak diduplikasi.',validasi=v)


class RpsTest(unittest.TestCase):
    def setUp(self): self.data=json.loads(DATA.read_text(encoding='utf-8'))
    def test_actual_output_and_sources(self):
        out=gen.render(self.data)
        self.assertEqual(out,RPS.read_text(encoding='utf-8'))
        self.assertEqual(len(re.findall(r'^\| \d+ \|',out,re.M)),16)
        self.assertNotRegex(out,r'\{\{[^{}]+\}\}|\[(?:mingguke|rubriktugas1)\]')
        sap=next(P.glob('065_2_*STI-311*.md')).read_text(encoding='utf-8')
        for w in self.data['minggu']:
            block=re.search(rf'^### Pertemuan {w["week"]}\b.*?\n(.*?)(?=\n### Pertemuan \d+\b|\n## |\Z)',sap,re.M|re.S).group(1)
            self.assertIn(w['materi'],block)
        rub=next(P.glob('065_5_*STI-311*.md')).read_text(encoding='utf-8')
        for a in self.data['asesmen']:
            block=re.search(rf'^### {re.escape(a["nama"])} — minggu .*?\n(.*?)(?=\n### |\n## |\Z)',rub,re.M|re.S).group(1)
            rows=[line.strip(' |').split(' | ') for line in block.splitlines() if re.match(r'^\| [^|]+ \| \d+% \|',line)]
            self.assertEqual([(r['kriteria'],str(r['bobot'])+'%',r['deskriptor']) for r in a['rubrik']],[(r[0],r[1],r[2:]) for r in rows])
        self.assertEqual([(a['week'],a['bobot'],a['cpmk']) for a in self.data['asesmen']],[(4,20,['CPMK-1']),(8,25,['CPMK-2']),(12,25,['CPMK-3']),(16,30,['CPMK-4'])])
        self.assertEqual(len(self.data['level_rubrik']),4)
    def test_different_course_multimap(self):
        s=gen.render(fixture())
        for x in ('TES-001','Metode Penelitian','Metode observasi 16','CP-5','✓','Kesesuaian metode','UAS riset'):
            self.assertIn(x,s)
        for x in ('STI-311','landing page','Bootstrap','CPL-08'):
            self.assertNotIn(x,s)
        self.assertIn('**10%** | **30%** | **20%** | **40%** | **100%**',s)
        self.assertIn('CP-4, CP-5',s)
    def test_invalid(self):
        for change in ('week','weight','rubric','cpl','sub','bibliography','assessment_week','placeholder'):
            d=copy.deepcopy(self.data)
            if change=='week': d['minggu'][1]['week']=1
            if change=='weight': d['asesmen'][0]['bobot']=19
            if change=='rubric': d['asesmen'][0]['rubrik'][0]['bobot']=34
            if change=='cpl': d['cpmk'][0]['cpl']=['missing']
            if change=='sub': d['minggu'][0]['subcpmk']=['missing']
            if change=='bibliography': d['minggu'][0]['referensi']=[999]
            if change=='assessment_week': d['asesmen'][0]['week']=5
            if change=='placeholder': d['identitas']['mk']='{{namamk}}'
            with self.subTest(change=change),self.assertRaises(gen.DataError): gen.render(d)
    def test_cli_overwrite_and_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            inp=Path(tmp)/'course.json'; out=Path(tmp)/'rps.md'
            inp.write_text(json.dumps(fixture()),encoding='utf-8')
            def run(*args): return subprocess.run([sys.executable,'-B',str(SCRIPT),str(inp),*map(str,args)],capture_output=True,text=True)
            self.assertEqual(run('-o',out).returncode,0)
            original=out.read_text()
            self.assertNotEqual(run('-o',out).returncode,0)
            self.assertEqual(out.read_text(),original)
            self.assertEqual(run('--check','-o',out).returncode,0)
            out.write_text('changed')
            self.assertNotEqual(run('--check','-o',out).returncode,0)
            self.assertEqual(run('--force','-o',out).returncode,0)
            self.assertEqual(out.read_text(),original)
            self.assertNotEqual(run('-o',Path(tmp)/'out.docx').returncode,0)
            self.assertEqual(run('--check').returncode,0)

if __name__=='__main__': unittest.main()
