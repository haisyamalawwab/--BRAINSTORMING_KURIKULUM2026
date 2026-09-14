---
name: buku-kpt-layouter
description: Use when menyusun buku, laporan, dokumen DOCX, PDF, atau HTML 045 mengikuti Template Master KPT FSTI UWG (cover, pengesahan, BAB I-XIV, tabel navy, header/footer, TOC).
---

# Buku KPT Layouter — Template Master FSTI UWG

Penyusun layout buku/laporan/dokumen resmi agar **persis Template Master KPT FSTI** (contoh: `KURIKULUM2026_REVISI/Template_KPT_2024.docx` / `.pdf`, 24 halaman: Sampul, Pengesahan, Kata Pengantar, Daftar Isi, Daftar Singkatan, BAB I–XIV, Lampiran 1–38).

## When to use

- User menyebut: susun buku, layout buku, rapikan laporan, buat DOCX/PDF resmi, ikuti template, template master, KPT FSTI, atau file `045*`.
- Membuat dokumen baru yang harus siap cetak/arsip (skripsi-like formal), BUKAN portal web modern.
- Khusus `045_DRAFT_BUKU_KPT*` (.md/.html/.docx/.pdf): WAJIB gaya Template Master, BUKAN gaya portal (`assets/css/style.css`, navbar, hero badges, card, dark-mode).

## Ground truth (jangan dikarang)

- Master DOCX: `KURIKULUM2026_REVISI/Template_KPT_2024.docx` — sumber tunggal style DOCX.
- Master PDF visual: `KURIKULUM2026_REVISI/Template_KPT_2024.pdf` — acuan tampilan (24 hlm).
- Isi definitif SISTEKIN: `KURIKULUM2026_REVISI/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md` + Dok 001–005, `AGENTS.md` (146 SKS/55 MK ditempuh, 182/67 portofolio, 14 CPL, 4 PL, 3 PEO).
- Placeholder yang belum ada data resmi tulis verbatim `[Nama Program Studi]`, `[Isi]`, `[SKS]`, atau `[PERLU DATA UPPS]` — jangan mengarang nama pejabat/NIDN/SK.

## Spesifikasi visual Template Master (wajib ditiru)

1. **Kertas & margin:** A4 portrait (21 × 29.7 cm), margin Normal 2.54 cm (1 inch) semua sisi. Body font `Calibri / Arial 11pt`, warna teks `#262626`, spasi 1.15, rata kiri-kanan (justify) untuk paragraf isi.
2. **Header berjalan (tiap halaman kecuali sampul):** rata kanan, `Calibri 9pt italic abu-abu #808080`, teks `Template Master KPT FSTI - Universitas Widya Gama Malang`.
3. **Footer:** tengah bawah, `Calibri 10pt regular #000000`, format `Halaman X` (angka saja, tanpa total).
4. **Sampul (Hlm 1):** semua tengah (center). Judul baris 1 `TEMPLATE MASTER` + baris 2 `DOKUMEN KURIKULUM PENDIDIKAN TINGGI` — `Calibri 16pt bold #1F4E79` (navy template; toleransi `#1F3864`/`#244061`). Baris 3–4 fakultas/universitas — `Calibri 13pt bold #000000`. Tabel identitas 4 baris di tengah halaman: kolom-1 `fill #D9E1F2 bold`, kolom-2 putih; border single 0.5pt hitam. Blok bawah fakultas/tahun tengah bold.
5. **Judul BAB:** `Calibri 13pt bold #1F4E79 UPPERCASE`, contoh `BAB I` + baris kedua nama bab. Spasi atas 14pt, bawah 6pt, keep-with-next.
6. **Sub-bab (1.1, 2.3):** `Calibri 12pt bold #1F4E79`, Title Case. Sub-sub (jika ada): `11pt bold #2E75B6`.
7. **Heading khusus:** `LEMBAR PENGESAHAN`, `KATA PENGANTAR`, `DAFTAR ISI`, `DAFTAR SINGKATAN`, `LAMPIRAN` — format sama seperti Judul BAB (navy, uppercase, 13pt bold).
8. **Tabel:** header `fill #1F4E79 (atau #244061), teks putih bold 10pt kiri`; isi `9.5–10pt`, baris ganjil putih `#FFFFFF`, genap `#F2F5F9`; padding cell 80–120 dxa; border tipis `#D3D3D3`/`#000000` single 4–6pt; header repeat di tiap halaman (`tblHeader`); judul tabel di atas, sumber di bawah bila ada. Tanda centang matriks: `√` (U+221A).
9. **Daftar isi (Template hlm 4):** teks uppercase tanpa nomor halaman di template (catatan: di Word final aktifkan TOC otomatis). Untuk HTML: daftar polos uppercase, tanpa dot-leader.
10. **Bullet/numbering:** bullet `•` indent 0.63 cm; numbering `1.` hierarki bertingkat. Quote italic abu untuk catatan (contoh Bab 2.6 tracer study).
11. **Urutan wajib dokumen:** Sampul → Pengesahan → Kata Pengantar → Daftar Isi → Daftar Tabel → Daftar Gambar → Daftar Singkatan → BAB I–XIV → Lampiran (38 item) → (opsional) Daftar Pustaka. Jangan ubah urutan.

## Workflow DOCX (buku/laporan resmi)

1. JANGAN buat dari `Document()` kosong untuk buku final. Clone dari master:
   `Copy-Item Template_KPT_2024.docx <output>.docx`, lalu isi via `_tools/fill_template_kpt*.py` atau python-docx (replace placeholder, fill baris tabel, duplicate row).
2. Pertahankan styles master (Heading 1/2, Normal, Header/Footer, Table Grid). Jika bangun tabel baru: tiru `convert_md_to_docx.py` — header navy `#1F3864`, zebra `#FFFFFF`/`#F2F5F9`, border `#D3D3D3`, font Calibri.
3. Page setup: A4 + margin 1 inch via `section.page_width/height/margins`. Header kanan italic abu, footer tengah `Halaman X` (field PAGE, bukan teks statis bila via Word).
4. Verifikasi: buka di Word → tiap tabel tidak terpotong, header tabel repeat, tidak ada placeholder tersisa selain `[PERLU DATA UPPS]`.

## Workflow HTML khusus 045* (pengecualian portal)

Aturan keras: file `045*.html` TIDAK BOLEH memakai `assets/css/style.css`, navbar, hero, badge, portal-card, theme-toggle, search-box, atau footer portal.

1. Generate sebagai dokumen mandiri `045_*.html` dengan `<style>` inline mandiri (atau `045-template-master-kpt.css` berdampingan). Struktur:
   `<div class="kpt-page">` per bab, `<header class="kpt-running">` + `<footer class="kpt-pagenum">Halaman X</footer>`.
2. CSS acuan (tempel langsung, jangan modifikasi portal):
```css
:root{--navy:#1F4E79;--ink:#262626;--grey:#808080;-- hdr:#1F4E79;--zebra:#F2F5F9;--line:#000;}
body{font-family:Calibri,Arial,sans-serif;color:var(--ink);background:#fff;margin:0;}
.kpt-page{max-width:170mm;margin:0 auto;padding:25.4mm 0;}
.kpt-running{text-align:right;font-size:9pt;font-style:italic;color:var(--grey);margin-bottom:12pt;}
h1.bab{font-size:13pt;color:var(--navy);text-transform:uppercase;margin:18pt 0 6pt;line-height:1.3;}
h2.sub{font-size:12pt;color:var(--navy);margin:14pt 0 4pt;}
p,li{font-size:11pt;line-height:1.5;text-align:justify;}
.kpt-cover{text-align:center;} .kpt-cover h1{font-size:16pt;color:var(--navy);line-height:1.4;}
table{width:100%;border-collapse:collapse;margin:8pt 0 12pt;font-size:10pt;}
th{background:var(--navy);color:#fff;text-align:left;padding:6px 8px;border:1px solid #000;}
td{padding:5px 8px;border:1px solid #000;vertical-align:top;}
tr:nth-child(even) td{background:var(--zebra);}
.kpt-pagenum{text-align:center;font-size:10pt;margin-top:18pt;}
@media print{@page{size:A4;margin:25.4mm;} .kpt-page{max-width:none;padding:0;} }
```
3. Sampul: replika hlm 1 PDF (judul navy tengah + tabel 4 baris kolom-1 `#D9E1F2` + blok fakultas/tahun). Pengesahan: 2 kolom tanda tangan + 1 tengah (Rektor), tanpa foto/logo.
4. Tabel identitas sampul/pengesahan: kolom-1 bold; border hitam single — jangan pakai style badge portal (`.cat-badge`, `.badge-type`).
5. Navigasi antar-dokumen dilarang di body 045. Cukup satu link kecil `← Kembali ke Portal` di paling atas dengan class `no-print`.

## Workflow PDF

- Dari DOCX master: Save As PDF / Export (Word) — hasil utama untuk arsip.
- Dari HTML 045: Chrome/Edge headless dengan `--no-pdf-header-footer` (lihat `_tools/convert_html_to_pdf.py`), agar header/footer datang dari HTML (`kpt-running`/`kpt-pagenum`), bukan bawaan browser. Cek: tiap halaman ada `Template Master...` kanan-atas dan `Halaman X` tengah-bawah, tabel tidak terbelah sembarangan (`thead{repeat}`, `tr{page-break-inside:avoid}`).

## Constraints

- Sumber kebenaran isi = `.md` + Dok 001–005 + AGENTS.md. Skill ini hanya mengatur layout — jangan ubah angka konsensus (146/55, 182/67, 14 CPL, 4 PL, 3 PEO, 3 peminatan STA/STB/STC-501,601-602,701-703, 4x asesmen).
- Jangan campur gaya portal modern (Inter/Plus-Jakarta, card, badge warna-warni, dark mode) ke dokumen 045/buku resmi.
- Jangan hapus placeholder `[PERLU DATA UPPS]` tanpa data resmi. Jangan commit biner besar tanpa diminta.
- Setelah generate: laporkan file output + ukuran bytes + ketidakcocokan vs Template (halaman, tabel, header/footer).

## Verifikasi akhir (checklist sebelum selesai)

- [ ] Urutan Sampul→Lampiran sesuai Template; BAB I–XIV judul navy uppercase.
- [ ] Header kanan italic abu + footer `Halaman X` di semua halaman isi.
- [ ] Semua tabel header navy/putih, border single, zebra benar, tidak overflow A4.
- [ ] Cover 045 identik hlm 1 PDF (judul navy, tabel 4 baris, blok fakultas).
- [ ] DOCX dibuka di Word tanpa style rusak; PDF dicetak A4 terbaca; HTML 045 tanpa navbar/hero portal.
