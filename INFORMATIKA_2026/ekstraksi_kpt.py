#!/usr/bin/env python3
"""Ekstraksi tabel KPT Teknik Informatika UWG 2026 dari DOCX sumber terverifikasi.

Install python-docx, lalu jalankan: python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/sumber.docx
Tambahkan --check untuk memeriksa hasil tanpa menulis ulang.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

OUT = Path(__file__).resolve().parent
SHA = 'a54a570150d0f7d38d633e72104b326062981818599101017dd3a7b4dfb2601d'
URL = ('https://github.com/rozanhaisyam/--BRAINSTORMING_KURIKULUM2026/blob/'
       '91b793377cd4b051f7bdcb89d3c19427ff344f9d/KPT_FIX_3PRODI/KPT%20Program%20Studi/'
       'Buku%20KPT%20OBE%20Teknik%20Informatika%20UWG%202026%20%5BUpdate%2011%20September%202026%5D.docx')
SOURCE = f'[Buku KPT OBE Teknik Informatika UWG 2026 (11 September 2026)]({URL})'


def clean(value):
    return re.sub(r'\s+', ' ', value).strip().replace('|', r'\|')


def table_to_md(rows):
    rows = [[clean(c) for c in row] for row in rows]
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('Tabel kosong atau jumlah kolom tidak konsisten')
    fmt = lambda row: '| ' + ' | '.join(row) + ' |'
    return '\n'.join([fmt(rows[0]), fmt(['---'] * len(rows[0])), *map(fmt, rows[1:])])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path, help='DOCX sumber (unduh dari tautan pada README)')
    p.add_argument('--check', action='store_true', help='Bandingkan dengan hasil tersimpan tanpa mengubah berkas')
    args = p.parse_args()
    if hashlib.sha256(args.input.read_bytes()).hexdigest() != SHA:
        sys.exit('SHA-256 tidak cocok dengan versi sumber yang terdokumentasi; hentikan ekstraksi.')
    doc = Document(args.input)
    body = list(doc.element.body)

    def find_table(caption):
        hits = [i for i, e in enumerate(body) if e.tag == qn('w:p') and Paragraph(e, doc).text.strip().startswith(caption)]
        if len(hits) != 1:
            raise ValueError(f'Caption {caption!r} ditemukan {len(hits)} kali')
        for e in body[hits[0] + 1:]:
            if e.tag == qn('w:tbl'):
                return Table(e, doc)
        raise ValueError(f'Tabel {caption!r} tidak ditemukan')

    def rows(table):
        return [[c.text for c in r.cells] for r in table.rows]

    def paragraph(prefix):
        values = [Paragraph(e, doc).text.strip() for e in body if e.tag == qn('w:p') and Paragraph(e, doc).text.strip().startswith(prefix)]
        if len(values) != 1:
            raise ValueError(f'Paragraf {prefix!r} ditemukan {len(values)} kali')
        return values[0]

    t11 = rows(find_table('Tabel 11. Pemetaan Capaian Pembelajaran Lulusan'))
    t13 = rows(find_table('Tabel 13. Body of Knowledge'))
    t14 = rows(find_table('Tabel 14. Matriks CPL'))
    t15 = rows(find_table('Tabel 15. Pemetaan Mata Kuliah'))
    t16 = rows(find_table('Tabel 16. Pemetaan Terpadu'))
    t18 = rows(find_table('Tabel 18. Distribusi Mata Kuliah'))
    t29 = rows(find_table('Tabel 29. Pengukuran CPMK'))
    t35 = rows(find_table('Tabel 35. Deskripsi Kode CPL'))
    # Kodifikasi is a heading rather than a caption; locate by its unique header.
    tables = [Table(e, doc) for e in body if e.tag == qn('w:tbl')]
    coding_matches = [rows(t) for t in tables if rows(t) and rows(t)[0] == ['Kategori', 'Format', 'Contoh']]
    if len(coding_matches) != 1:
        raise ValueError('Tabel kodifikasi tidak unik')
    coding = coding_matches[0]
    assert len(t11) == len(t13) == len(t14) == len(t16) == len(t35) == 11
    assert [(r[1], clean(r[2])) for r in t11[1:]] == [(r[0], clean(r[1])) for r in t35[1:]], 'CPL Bab V dan Lampiran A berbeda'
    assert len(t15) == 252 and t15[:84] == t15[84:168] == t15[168:252], 'Perulangan tabel 15 berbeda dari yang diharapkan'
    t15_unique = t15[:84]
    assert len({r[0] for r in t15_unique[1:]}) == 83
    assert len(t29) == 10 and len(t29[0]) == 9
    semester = None
    mk18 = [['Semester', 'Kode MK', 'Mata Kuliah', 'SKS', 'CPL yang Dibebankan']]
    for row in t18:
        cells = [clean(c) for c in row]
        if re.fullmatch(r'Semester [1-8]', cells[0]):
            semester = cells[0].replace('Semester ', '')
        elif cells[0] == 'Kode MK':
            continue
        else:
            if semester is None or len(cells) != 4:
                raise ValueError('Struktur Tabel 18 berubah')
            mk18.append([semester, *row])

    cpmk_desc = paragraph('CPMK adalah kemampuan spesifik')
    cpmk_map = paragraph('Pemetaan dilakukan dengan memastikan setiap CPMK')
    sub_desc = paragraph('Setiap CPMK dijabarkan menjadi satu atau lebih Sub-CPMK')
    example_desc = paragraph('Workbook OBE 2026 telah menyediakan template pengukuran CPMK')
    bk_note = paragraph('Pemetaan BK–MK berikut diturunkan')
    common = f'> Sumber: {SOURCE}. Identifikasi versi dan batas ekstraksi ada di [README](README.md).\n'

    output = {}
    output['001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md'] = f'''# CPL Teknik Informatika UWG 2026

{common}
## Rumusan CPL dan profil lulusan terkait

Transkripsi Tabel 11 Bab V; isi rumusan juga cocok dengan Tabel 35 Lampiran A. Kode CPL adalah kode **Teknik Informatika** dalam dokumen sumber, bukan kode CPL SISTEKIN.

{table_to_md(t11)}

## CPL–bahan kajian

Transkripsi Tabel 14 Bab VI; lihat uraian BK dan relasi BK–MK pada [BoK](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md).

{table_to_md(t14)}

Pemetaan mata kuliah dan CPL sebagaimana Tabel 18 dapat dilihat pada [pemetaan MK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md). Tabel 12 (matriks CPL–PL) dan Tabel 19 (matriks CPL–MK) memiliki sel relasi kosong pada teks DOCX; daftar relasi di sini berasal dari Tabel 11 dan 18, bukan mengisi matriks yang kosong.
'''
    output['003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md'] = f'''# Body of Knowledge dan bahan kajian — Teknik Informatika UWG 2026

{common}
## Kerangka BoK

{paragraph('Bahan kajian ditetapkan berdasarkan CPL, body of knowledge')}

{paragraph('Bahan kajian ditetapkan dengan mengelompokkan pengetahuan')}

### Tabel 13 — BoK dan ruang lingkup bahan kajian

{table_to_md(t13)}

### Tabel 14 — CPL dengan bahan kajian utama

{table_to_md(t14)}

### Tabel 16 — Pemetaan terpadu CPL–BK–contoh MK

{table_to_md(t16)}

## Pemetaan BK–MK

{bk_note}

Seluruh baris Tabel 15 tersedia pada [pemetaan MK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md#tabel-15--mk-dengan-bahan-kajian); tabel sumber mengulang 84 baris yang sama tiga kali, sehingga untuk navigasi tiap baris identik ditampilkan sekali. Ini **bukan** bukti bahwa suatu topik sudah diajarkan atau telah disahkan. Nama BK dan kode di sini tidak disamakan secara otomatis dengan BoK APTIKOM atau SISTEKIN.
'''
    output['002_CPMK_TEKNIK_INFORMATIKA_07112026_0859.md'] = f'''# CPMK dan Sub-CPMK — Teknik Informatika UWG 2026

{common}
## Status hasil ekstraksi

Dokumen sumber menjelaskan prinsip, format, kodifikasi, dan contoh pembobotan CPMK/Sub-CPMK, tetapi **tidak ditemukan daftar rumusan CPMK/Sub-CPMK per mata kuliah dalam teks dan tabel utama DOCX**. Jangan menganggap contoh angka atau kode di bawah sebagai CPMK resmi suatu MK. RPS/workbook terpisah diperlukan untuk ekstraksi rumusan per MK; dokumen sumber menyebut workbook, tetapi workbook itu tidak diperiksa di sini.

## Kodifikasi

Tabel kodifikasi pada bagian awal dokumen:

{table_to_md(coding)}

`CPMK05.1` dan `Sub-CPMK05.1.1` merupakan contoh format kode, bukan rumusan CPMK.

## Prinsip di Bab IX

> {cpmk_desc}

> {cpmk_map}

> {sub_desc}

## Contoh matriks asesmen — bukan CPMK per MK

Bab XI, Tabel 29. {example_desc}

{table_to_md(t29)}

Tabel ini mencantumkan label CPMK dan Sub-CPMK serta bobot, bukan deskripsi kemampuan atau kode MK. Bobot di atas hanyalah contoh dalam dokumen, bukan ketentuan otomatis bagi setiap mata kuliah.

## Sumber relasi yang sudah tersedia

- CPL dan profil lulusan: [CPL](001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md).
- CPL–BK dan uraian BK: [BoK dan bahan kajian](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md).
- CPL yang dibebankan per MK menurut Tabel 18: [pemetaan MK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md).

Matriks CPL–CPMK–MK dan MK–CPMK–Sub-CPMK yang berisi deskripsi spesifik **tidak dibuat atau direka** pada hasil ini.
'''
    output['004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md'] = f'''# Pemetaan MK–CPL–BK — Teknik Informatika UWG 2026

{common}
## Tabel 18 — mata kuliah dan CPL per semester

Tabel berikut mempertahankan alternatif wajib konsentrasi dan baris pilihan tanpa menggabungkannya sebagai paket yang semuanya diambil mahasiswa. Tabel 18 memberikan CPL yang dibebankan, **bukan CPMK**. Teks, kode, SKS, dan semester dipertahankan dari sumber.

{table_to_md(mk18)}

## Tabel 15 — MK dengan bahan kajian

{bk_note}

Tabel sumber memuat 252 baris, berupa tiga blok identik masing-masing satu header dan 83 baris MK. Di sini satu blok ditampilkan, tanpa mengubah pasangan MK–BK. Tabel 15 juga memuat alternatif MK konsentrasi yang tidak seluruhnya tercantum pada Tabel 18. **Jangan menyimpulkan total MK ditempuh dari jumlah baris ini.**

{table_to_md(t15_unique)}

## Batas interpretasi

Tabel 15 dan 18 adalah transkripsi masing-masing, bukan hasil rekonsiliasi. Sebagai contoh, Tabel 18 membebankan CPL03, CPL04, dan CPL07 pada KOM-101; melalui Tabel 14 ketiganya terkait BK01, BK02, dan BK06. Tabel 15 juga mencantumkan BK09 dan BK10 untuk KOM-101. Tambahan ini perlu diklarifikasi oleh prodi, bukan otomatis dianggap salah atau dihapus. Jangan menyimpulkan relasi CPMK dari kesamaan kode atau nama.
'''
    output['README.md'] = f'''# Ekstraksi KPT Teknik Informatika UWG 2026

Ekstraksi dari {SOURCE}, bukan panduan Informatika APTIKOM umum dan bukan kurikulum SISTEKIN.

| Hasil | Isi |
|---|---|
| [CPL](001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md) | 10 CPL, profil lulusan terkait, dan matriks CPL–BK sumber. |
| [CPMK dan Sub-CPMK](002_CPMK_TEKNIK_INFORMATIKA_07112026_0859.md) | Kodifikasi, prinsip, dan contoh asesmen; batas ketersediaan rumusan per MK. |
| [BoK dan bahan kajian](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md) | 10 BK, ruang lingkup, matriks CPL–BK dan contoh MK pengampu. |
| [Pemetaan MK–CPL–BK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md) | Tabel 18 per semester serta 83 baris unik Tabel 15. |
| [005 — pemetaan APTIKOM](005_PEMETAAN_APTIKOM_MK_INFORMATIKA_07112026_0910.md) | Kandidat 22 BK APTIKOM untuk 83 MK berdasarkan judul; bukan validasi isi. |
| [006 — analisis dan survei pustaka](006_ANALISIS_DAN_SURVEI_PUSTAKA_INFORMATIKA_07112026_0910.md) | Analisis hubungan tabel, perbedaan rujukan dan tindak lanjut. |
| [007 — instrumen survei](007_INSTRUMEN_SURVEI_VALIDASI_INFORMATIKA_07112026_0910.md) | Rancangan survei dan validasi; belum ada respons. |

## Identitas dan keterlacakan sumber

- Berkas: `KPT_FIX_3PRODI/KPT Program Studi/Buku KPT OBE Teknik Informatika UWG 2026 [Update 11 September 2026].docx`.
- Commit sumber: `91b793377cd4b051f7bdcb89d3c19427ff344f9d` pada `main` saat pengambilan. Tautan di atas dipatok ke commit ini; file sumber tidak disalin ke folder hasil.
- SHA-256 DOCX: `{SHA}`.
- Ekstraksi dilakukan dari teks dan tabel tubuh DOCX menggunakan `python-docx`; spasi dan pemisah baris dalam sel dirapikan, kode dan isi dipertahankan. Nomor tabel/bab lebih stabil daripada nomor halaman DOCX yang dapat berubah saat dirender. Gambar tidak di-OCR; isi visual dan workbook/RPS eksternal tidak diperiksa.

## Temuan dan batasan

1. Bab V Tabel 11 dan Lampiran A Tabel 35 sama-sama memuat 10 rumusan CPL; teksnya sesuai setelah perapian spasi.
2. Bab VI Tabel 13 memuat 10 kelompok BK. Tabel 14 memetakan CPL–BK; Tabel 15 memuat tiga salinan identik dari 83 baris MK, ditampilkan satu kali dalam hasil. Dokumen sendiri menyatakan pemetaan rinci BK–MK masih perlu validasi kelompok bidang keahlian.
3. Bab IX memberi prinsip pemetaan CPMK, tetapi tidak ditemukan rumusan per MK dalam teks dan tabel utama. Tabel 29 Bab XI hanya memuat **contoh** label dan bobot; tidak digunakan untuk menciptakan CPMK per MK.
4. Sel relasi pada Tabel 12 (CPL–PL) dan Tabel 19 (CPL–MK) kosong dalam teks DOCX. Tabel 11 dan Tabel 18 diekstrak apa adanya sebagai sumber relasi yang eksplisit; ketidaksesuaian antartabel belum direkonsiliasi.
5. Hasil ini merupakan transkripsi rujukan dan **tidak membuktikan validasi atau pengesahan akademik**. Dokumen sumber menyebut 146 SKS dalam Bab VII; angka tersebut untuk Teknik Informatika dan tidak otomatis menggantikan statistik prodi lain.

## Penamaan

Berkas hasil ekstraksi menggunakan format `00x_NAMA_DDMMYYYY_HHMM.md`. Nomor, tanggal, dan waktu pada nama ditetapkan untuk versi hasil ini agar regenerasi tidak membuat duplikat; `README.md` tetap sebagai indeks folder.

## Reproduksi

Unduh DOCX pada tautan sumber, lalu (setelah memasang `python-docx`):

```bash
python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/to/sumber.docx
python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/to/sumber.docx --check
```

Skrip menolak sumber dengan SHA-256 berbeda agar perubahan versi tidak secara diam-diam mengganti hasil. Pemeriksaan ini tidak menggantikan pembandingan visual terhadap DOCX.
'''
    failed = []
    for name, content in output.items():
        path = OUT / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                failed.append(name)
        else:
            path.write_text(content, encoding='utf-8')
            print('Ditulis:', path)
    if failed:
        sys.exit('Hasil berbeda atau hilang: ' + ', '.join(failed))
    if args.check:
        print(f'Lulus: {len(output)} berkas sesuai; 10 CPL, 10 BK, {len(t15_unique)-1} MK–BK, {len(mk18)-1} baris distribusi MK.')


if __name__ == '__main__':
    main()
