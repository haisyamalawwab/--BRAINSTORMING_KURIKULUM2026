#!/usr/bin/env python3
"""Test struktural DOCX; bukan pengganti pemeriksaan tampilan di Word."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from docx import Document
import generate_rps_docx as g
from test_generate_rps_md import fixture, DATA

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'DOCX/RPS_STI-311_TEMPLATE_REVISI_07112026.docx'


def alltext(doc):return '\n'.join(p.text for p in g.paragraphs(doc))


class DocxTest(unittest.TestCase):
    def check_structure(self,doc,data):
        self.assertEqual(len(doc.sections),2)
        self.assertGreater(doc.sections[0].page_width,doc.sections[0].page_height)
        self.assertLess(doc.sections[1].page_width,doc.sections[1].page_height)
        self.assertEqual(len(doc.tables),12)
        t=doc.tables[2]
        self.assertEqual(len(t.rows),20)
        for i,w in enumerate(data['minggu'],3):
            cells=g.unique(t.rows[i]);self.assertEqual(len(cells),8)
            self.assertEqual(cells[0].text,str(w['week']))
            self.assertEqual(cells[1].text,', '.join(w['subcpmk']))
            for c,key in zip(cells[2:7],('indikator','kriteria_teknik','luring','daring','materi')):
                if key=='materi': self.assertTrue(c.text.startswith(g.plain(w[key])))
                else: self.assertEqual(c.text,g.plain(w[key]))
        self.assertEqual(t.rows[-1].cells[-1].text,'100%')
        body=alltext(doc)
        self.assertEqual(g.TAGS.findall(body),[])
        self.assertNotIn('PROGRAM STUDI S1 TEKNIK MESIN',body)
        self.assertNotIn('Nama Pejabat UPM',body)
        self.assertNotIn('xxxxxxxxx',body)
        self.assertIn(data['status'],body)
        for i,slot in enumerate(('tugas1','uts','tugas2','uas')):
            a=next(x for x in data['asesmen'] if x['id']==slot)
            self.assertIn(g.plain(a['soal']),doc.tables[3+2*i].cell(0,0).text)
            nested=doc.tables[4+2*i].cell(0,0).tables
            self.assertEqual(len(nested),1)
            self.assertEqual(len(nested[0].rows),1+len(a['rubrik']))
            self.assertEqual(len(nested[0].columns),2+len(data['level_rubrik']))
            for row,r in zip(nested[0].rows[1:],a['rubrik']):
                self.assertEqual([c.text for c in row.cells],[g.plain(r['kriteria']),str(r['bobot'])+'%']+[g.plain(x) for x in r['deskriptor']])
    def test_sti311_generated_artifact(self):
        data=json.loads(DATA.read_text(encoding='utf-8'))
        self.check_structure(Document(OUTPUT),data)
        rebuilt=g.build(data);self.check_structure(rebuilt,data)
        blob=alltext(Document(OUTPUT))
        self.assertEqual(blob,alltext(rebuilt))
        for sub in data['subcpmk']:self.assertIn(sub['id'],blob)
        for a in data['asesmen']: self.assertIn(a['soal'],blob)
    def test_different_course_and_expanded_rows(self):
        d=fixture()
        for n in range(6,9):
            d['cpl'].append(dict(id=f'PL-{n}',display=f'PL-{n}',rumusan=f'Rumusan {n}',irm='R'))
            d['cpmk'].append(dict(id=f'CP-{n}',rumusan=f'Kompetensi riset {n}',bloom='C3',cpl=[f'PL-{n}']))
            d['subcpmk'].append(dict(id=f'SUB-{n}',rumusan=f'Tahapan riset {n}',cpmk=f'CP-{n}',bloom='C3'))
            d['minggu'][-1]['subcpmk'].append(f'SUB-{n}')
            d['asesmen'][-1]['cpmk'].append(f'CP-{n}')
        doc=g.build(d);self.check_structure(doc,d);blob=alltext(doc)
        for x in ('TES-001','PL-8','CP-8','SUB-8','Metode Penelitian','Fakultas Contoh'):
            self.assertIn(x,blob)
        for x in ('STI-311','Bootstrap','landing page','Teknik Mesin'):
            self.assertNotIn(x,blob)
    def test_cli_safety(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'data.json';out=Path(td)/'result.docx';inp.write_text(json.dumps(fixture()))
            def run(*args):return subprocess.run([sys.executable,'-B',str(g.__file__),str(inp),*map(str,args)],capture_output=True,text=True)
            self.assertEqual(run('-o',out).returncode,0)
            before=out.read_bytes()
            self.assertNotEqual(run('-o',out).returncode,0)
            self.assertEqual(out.read_bytes(),before)
            self.assertNotEqual(run('-o',g.TEMPLATE,'--force').returncode,0)
            self.assertNotEqual(run('-o',Path(td)/'x.md').returncode,0)
            self.assertEqual(run('-o',out,'--force').returncode,0)

if __name__=='__main__':unittest.main()
