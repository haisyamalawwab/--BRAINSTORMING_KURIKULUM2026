#!/usr/bin/env python3
"""Bangun inventaris kandidat pemetaan dari 004 dan pembacaan APTIKOM. --check tanpa menulis."""
from collections import Counter
from pathlib import Path
import argparse
import hashlib
import re
import sys

BASE = Path(__file__).resolve().parent
SRC = BASE / '004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md'
PDF = BASE.parent / 'BUKU_OBE/839193049-Buku-Kurikulum-Prodi-S1-Informatika-atau-Ilmu-Komputer-Versi-2-0-aptikom.pdf'
OUT = BASE / '005_PEMETAAN_APTIKOM_MK_INFORMATIKA_07112026_0910.md'
SRC_HASH = 'dec913954063d25cdaa3583a9567c4ca6f2508bb61cedb38eb5931a5174e9e65'
PDF_HASH = '30f91073c242faf4fc397fef3992d6f1f11241f911ea2cda32d7539fbe344701'

# A01–A22 = BK01–BK22 APTIKOM Tabel 4, bukan kode BK lokal. Kandidat
# dikurasi berdasarkan judul MK, bukan pemetaan resmi atau bukti RPS.
CATEGORIES = {
'A01': ('Society, Ethics and Professionalism', 'BK07, BK09', 'FST-206 KOM-317'),
'A02': ('Security', 'BK07', 'KOM-631 KFC-602'),
'A03': ('Project Management', 'BK10', 'KOM-317 FST-610'),
'A04': ('User Experience Design', 'BK04', 'KOM-419 KFC-707'),
'A05': ('Software Development Fundamentals', 'BK02', 'FST-102 FST-203 KOM-311 KOM-312 KOM-418 KOM-524 KOM-526 KFC-506 KFC-601 KOM-627 KFC-710'),
'A06': ('Data Management', 'BK03', 'FST-207 KFD-601 KFD-603'),
'A07': ('Parallel and Distributed Computing', 'BK06', 'KOM-315 KFC-711'),
'A08': ('Network and Communication', 'BK06', 'KOM-314 KFC-603'),
'A09': ('Human-Computer Interaction', 'BK04', 'KOM-419 KFC-707'),
'A10': ('Software Engineering', 'BK02', 'KOM-313 KOM-417 KOM-418 FST-610'),
'A11': ('Operating Systems', 'BK06', 'KOM-420'),
'A12': ('Algorithmic Foundations', 'BK01, BK02', 'FST-102 FST-203 KOM-201 KOM-630'),
'A13': ('Foundations of Programming Languages', 'BK01, BK02', 'KOM-311 KOM-418 KOM-630'),
'A14': ('Programming Fundamentals', 'BK02', 'FST-102 KOM-311 KOM-312 KOM-524'),
'A15': ('Systems Fundamentals', 'BK06', 'KOM-102 FST-101 KOM-310 KOM-315 KOM-420'),
'A16': ('Architecture and Organization', 'BK06', 'KOM-102 FST-101 KOM-310'),
'A17': ('Graphics and Interactive Techniques', 'BK04', 'KOM-525 KFM-506 KFM-601 KFM-707 KFM-708 KFM-709 KFM-710 KOM-729 KOM-627 KFC-710'),
'A18': ('Artificial Intelligence', 'BK03, BK05', 'FST-204 KOM-527 KOM-629 KOM-625 KOM-626 KOM-730 KFM-602 KFD-711 KFC-604 KFC-709'),
'A19': ('Specialized Platform Development', 'BK02, BK06', 'KOM-312 KOM-524 KOM-526 KFC-506 KFC-601 KFC-708 KFC-710'),
'A20': ('Mathematical and Statistical Foundations', 'BK01', 'KOM-103 KOM-201 KOM-202 KOM-316 FST-408 KFD-506 KFD-604'),
'A21': ('Pengembangan Diri', 'BK09, BK10', 'MKU-204 MKU-507 MKU-508 FST-612'),
'A22': ('Metodologi', 'BK08', 'FST-611 FST-613 FST-713 KFD-707'),
}
CPLBK = {
'CPL01': {'BK07','BK09'}, 'CPL02': {'BK09'}, 'CPL03': {'BK01'},
'CPL04': {'BK02'}, 'CPL05': {'BK03'}, 'CPL06': {'BK04','BK05'},
'CPL07': {'BK06'}, 'CPL08': {'BK07'}, 'CPL09': {'BK08'}, 'CPL10': {'BK09','BK10'},
}


def load():
    for path, expected in ((SRC,SRC_HASH),(PDF,PDF_HASH)):
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Sumber berubah; pemetaan manual harus ditinjau: {path}')
    sections=SRC.read_text(encoding='utf-8').split('## Tabel 15 — MK dengan bahan kajian')
    if len(sections)!=2: raise ValueError('Tabel 15 tidak ditemukan atau ganda')
    t18=[]; t15=[]
    for line in sections[0].splitlines():
        cols=[c.strip() for c in line.strip('|').split('|')]
        if len(cols)==5 and re.fullmatch('[1-8]',cols[0]): t18.append(cols)
    for line in sections[1].splitlines():
        cols=[c.strip() for c in line.strip('|').split('|')]
        if len(cols)==3 and re.fullmatch(r'[A-Z]+-\d{3}',cols[0]): t15.append(cols)
    if len(t18)!=62 or len(t15)!=83 or len({x[0] for x in t15})!=83:
        raise ValueError('Cakupan sumber berubah; periksa input.')
    course={x[1]:x for x in t18 if x[1]!='—'}
    if len(course)!=58 or any(k not in {r[0] for r in t15} for k in course):
        raise ValueError('Kode MK Tabel 18 berubah atau tidak ada di Tabel 15')
    for cat,(_,_,ids) in CATEGORIES.items():
        codes=ids.split()
        if len(set(codes))!=len(codes) or set(codes)-{r[0] for r in t15}:
            raise ValueError(f'Kode salah/duplikat di {cat}: {ids}')
    return t18,t15,course


def status(row,course):
    if row[0] not in course: return 'P'
    c=course[row[0]]
    match=re.search(r'\[wajib konsentrasi (IM|DS|MC)\]',c[2])
    if match: return match.group(1)
    return 'U'


def run(check):
    t18,t15,course=load()
    lines=['# Pemetaan indikatif MK Informatika UWG × APTIKOM 2024','',
           '> **Hipotesis penelusuran, bukan bukti bahwa topik diajarkan, cakupan CS Core, pemenuhan standar atau pengesahan.** Belum ada RPS/CPMK, jam, atau asesmen diverifikasi. Axx di bawah adalah alias untuk BKxx APTIKOM; BKxx adalah kode UWG pada dokumen 004. Jangan menyamakan kedua kode.', '',
           '## Sumber dan metode', '',
           '- Basis 83 baris unik MK–BK UWG: [004](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md), Tabel 15; status/semester dari Tabel 18. KPT dan SHA sumber tercatat pada [README](README.md).',
           '- Daftar A01–A22: [Panduan APTIKOM Informatika v2.0](../BUKU_OBE/839193049-Buku-Kurikulum-Prodi-S1-Informatika-atau-Ilmu-Komputer-Versi-2-0-aptikom.pdf), Tabel 4, **halaman PDF 42**. Daftar 22 BK berbeda dari 17 knowledge area CS2023 (Lampiran 6, halaman PDF 116).',
           '- Tim analisis mengusulkan hubungan melalui nama/rentang BK dan judul MK saja. MK yang judulnya tidak menunjukkan hubungan jelas diberi `—`; bukan berarti MK tersebut tidak terkait. Hubungan 10 BK UWG ↔ 22 BK APTIKOM bersifat banyak-ke-banyak dan tidak otomatis identik.',
           '- Status: **U** = baris MK non-konsentrasi pada Tabel 18 (belum klaim aturan kelulusan); **IM/DS/MC** = wajib konsentrasi tertentu menurut label Tabel 18; **P** = muncul di Tabel 15 tetapi tidak tercantum sebagai MK berkode di Tabel 18. P adalah kelompok yang harus diperiksa pada katalog pilihan, bukan bukti semua mahasiswa mengambilnya.',
           '- Alias dan kandidat tidak memindahkan CPL, mengubah SKS, atau membuat MK baru. Tabel APTIKOM yang berbeda dan sumber CS2023 perlu rekonsiliasi sebelum memakai bobot.', '',
           '## Daftar area APTIKOM dan kandidat MK', '',
           '| Alias | BK APTIKOM | Kode BK UWG yang berkaitan secara konseptual | Kandidat berdasarkan judul (status) |', '|---|---|---|---|']
    lookup={row[0]:row for row in t15}
    for code,(name,local,ids) in CATEGORIES.items():
        candidates=', '.join(f'{k} ({status(lookup[k],course)})' for k in ids.split())
        lines.append(f'| {code} | {name} | {local} | {candidates or "—"} |')
    lines.extend(['','## Inventaris seluruh MK pada Tabel 15','',
                  'Kolom BK UWG dan nama MK disalin dari 004. APTIKOM kandidat diturunkan secara manual berdasarkan judul saja; `—` = **belum diidentifikasi**, bukan gap. Angka frekuensi hanya menghitung baris/relasi kandidat, bukan mutu, kelengkapan, SKS, atau jumlah MK yang ditempuh.', '',
                  '| Kode MK | Nama MK | BK UWG dalam 004 | Status | APTIKOM kandidat |', '|---|---|---|---|---|'])
    for row in t15:
        code,name,bks=row
        cats=', '.join(k for k,(_,_,ids) in CATEGORIES.items() if code in ids.split()) or '—'
        lines.append(f'| {code} | {name} | {bks} | {status(row,course)} | {cats} |')
    count=Counter(status(r,course) for r in t15)
    unassigned=[r[0] for r in t15 if all(r[0] not in ids.split() for _,_,ids in CATEGORIES.values())]
    lines.extend(['','## Catatan pembacaan', '',
                  f'- Inventaris: **{len(t15)} MK berkode** (U {count["U"]}; IM {count["IM"]}; DS {count["DS"]}; MC {count["MC"]}; P {count["P"]}). Tabel 18 juga memuat 4 slot pilihan tanpa kode; slot tersebut tidak dihitung sebagai MK berkode di inventaris ini.',
                  f'- **{len(unassigned)} MK** belum mendapat kandidat APTIKOM berdasarkan metode judul yang konservatif: {", ".join(unassigned)}. Penetapan selanjutnya memerlukan RPS.',
                  '- Kandidat A04 dan A09, A05 dan A14, serta A12 dan A13 dapat bertumpang tindih. Tidak ada alokasi jam yang dihitung. Pemetaan bersifat sementara dan harus divalidasi oleh pengampu/RMK.',
                  '- Hasil kajian rinci dan rancangan survei: [analisis](006_ANALISIS_DAN_SURVEI_PUSTAKA_INFORMATIKA_07112026_0910.md) · [instrumen](007_INSTRUMEN_SURVEI_VALIDASI_INFORMATIKA_07112026_0910.md).',
                  '', '---', '',
                  'Dihasilkan oleh `python3 -B INFORMATIKA_2026/analisis_pemetaan.py`; `--check` memeriksa reproduksi dan hash sumber. Isi kandidat dikurasi manual di skrip, bukan validasi otomatis.', ''])
    text='\n'.join(lines)
    if check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8')!=text: sys.exit('Indeks pemetaan tidak sesuai; jalankan tanpa --check.')
        print(f'Lulus: {len(t15)} baris, {len(CATEGORIES)} area APTIKOM, {len(unassigned)} belum ditautkan; status {dict(count)}.')
    else:
        OUT.write_text(text,encoding='utf-8'); print(f'Ditulis: {OUT}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    run(args.check)
