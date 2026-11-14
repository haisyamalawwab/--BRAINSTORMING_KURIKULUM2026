# 052 — ANALISIS DAN INVENTARISASI TEMPLATE RPS OBE SISTEKIN 2026

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Status Dokumen:** Laporan Inventarisasi, Audit Desain, Kamus Tag, dan Panduan Ekosistem Template RPS OBE  
**Tanggal & Waktu:** 09 November 2026, 15:20 WIB (`09112026_1520`)  
**Penyusun:** Tim Pengembang Kurikulum SISTEKIN & Asesor Internal Mutu Akademik OBE  

---

## 1. Eksekutif Ringkasan

Penyusunan Rencana Pembelajaran Semester (RPS) berbasis *Outcome-Based Education* (OBE) pada Program Studi S1 Sistem dan Teknologi Informasi (SISTEKIN) FSTI Universitas Widyagama Malang mengacu pada standar baku akreditasi nasional (LAM INFOKOM, BAN-PT, Permendikbudristek No. 53 Tahun 2023, dan Panduan Kurikulum OBE APTIKOM SI/TI 2024).

Dokumen ini mendokumentasikan inventarisasi komprehensif atas seluruh artefak template RPS OBE yang tersedia di repositori, membedah karakteristik arsitektur tata letak (*layout geometry*), memetakan kamus tag *placeholder* otomasi generator, serta menyajikan ekosistem perangkat pendukung dan implementasi yang telah aktif digunakan untuk portofolio 46 mata kuliah Kurikulum 2026.

---

## 2. Inventarisasi Berkas Template RPS OBE yang Tersedia

Berikut adalah tabel status seluruh berkas template dan sampel acuan yang tersimpan di dalam repositori:

| No | Nama Berkas | Jalur Relatif / Folder | Format | Ukuran | Status & Peruntukan |
|:---:|---|---|:---:|:---:|---|
| **1** | `Template_RPS_GEN_2026_20092026-SWO.docx` | `KURIKULUM2026_REVISI/` | Word DOCX | 123 KB | **Template Master Generator Utama**. Menggunakan format *hybrid* (Landscape + Portrait), memuat 12 tabel baku, 18 tag scalar `{{...}}`, dan 25 tag blok konten `[...]`. |
| **2** | `Template_RPS_GEN_2026_20092026-SWI.pdf` | `KURIKULUM2026_REVISI/` | PDF | 226 KB | **Template Master Visual Resmi (9 Halaman)**. Representasi visual PDF dari template master ber-tag placeholder untuk verifikasi layout cetak. |
| **3** | `0001_Template_RPS_OBE.pdf` | `KURIKULUM2026_REVISI/` | PDF | 508 KB | **Sampel Riil Terisi (11 Halaman)**. Contoh implementasi penuh RPS OBE UWG pada mata kuliah acuan *Dasar Pemrograman Komputer* (`MSN-315`) sebagai benchmark format dan rubrik. |
| **4** | `052_ANALISIS_FORMAT_DAN_LAYOUT_TEMPLATE_RPS_OBE.md` | `KURIKULUM2026_REVISI/` | Markdown | 24 KB | **Spesifikasi Arsitektur Layout & Kamus Tag**. Audit forensik desain, pembagian seksi, orientasi halaman, dan daftar lengkap tag generator. |
| **5** | `053_MASTER_PROMPT_GENERATOR_RPS_OBE.md` | `KURIKULUM2026_REVISI/` | Markdown | 6 KB | **Master Prompt SOP Generator**. Prosedur operasi baku berjenjang T0–T6 untuk pengisian otomatis template RPS satu per satu mata kuliah. |
| **6** | `generate_rps_docx.py` & `generate_rps_md.py` | `KURIKULUM2026_REVISI/_tools/` | Python | ~12 KB | **Mesin Automasi Pengisi Template**. Skrip engine Python untuk membangkitkan dokumen RPS berformat `.docx` dan `.md` dari kontrak data JSON. |
| **7** | `065_STI-311_RPS.json` | `KURIKULUM2026_REVISI/PERANGKAT_AJAR/_data/` | JSON | ~25 KB | **Kontrak Data JSON Baku**. Skema data referensi lengkap untuk pengisian template RPS (CPMK, Sub-CPMK, 16 pekan, 4 asesmen, 4 rubrik). |

---

## 3. Arsitektur Desain & Tata Letak Template Master

Template resmi `Template_RPS_GEN_2026_20092026-SWO.docx` dirancang dengan arsitektur **Tata Letak Campuran (*Hybrid Orientation Architecture*)** 9 halaman:

```
┌────────────────────────────────────────────────────────────────────────┐
│               ARSITEKTUR DOKUMEN RPS OBE FSTI UWG (9 HALAMAN)          │
├───────────────────────────────────┬────────────────────────────────────┤
│   BAGIAN 1: MATRIKS KURIKULER     │    BAGIAN 2: INSTRUMEN ASESMEN     │
│       (Halaman Landscape)         │        (Halaman Portrait)          │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Hal 1: Cover Judul RPS          │ • Hal 5: Lampiran Tugas 1 + Rubrik │
│ • Hal 2: Identitas, Otorisasi,    │ • Hal 6: Lampiran UTS + Rubrik     │
│          CPL, CPMK, Korelasi CPL- │ • Hal 7: Lampiran Tugas 2 + Rubrik │
│          CPMK, Deskripsi MK       │ • Hal 8: Lampiran UAS + Rubrik     │
│ • Hal 3-4: Bahan Kajian, Pustaka, │ • Hal 9: Lembar Validasi UPM,      │
│            Dosen, Prasyarat, &    │          Dosen, dan Pengesahan     │
│            Tabel 16 Pertemuan     │          Ketua Program Studi       │
│            (8 Kolom Baku)         │                                    │
└───────────────────────────────────┴────────────────────────────────────┘
```

### Parameter Geometri Halaman:
1. **Bagian I (Halaman 1 s.d. 4 — Landscape A4):**
   * Ukuran Kertas: A4 Landscape ($297\text{ mm} \times 210\text{ mm}$).
   * Margin: Kiri $25\text{ mm}$, Kanan $20\text{ mm}$, Atas $20\text{ mm}$, Bawah $20\text{ mm}$.
   * Tujuan: Memberikan ruang lebar horizontal untuk tabel matriks 16 pertemuan (8 kolom operasional).
2. **Bagian II & III (Halaman 5 s.d. 9 — Portrait A4):**
   * Ukuran Kertas: A4 Portrait ($210\text{ mm} \times 297\text{ mm}$).
   * Margin: Kiri $25\text{ mm}$, Kanan $20\text{ mm}$, Atas $25\text{ mm}$, Bawah $25\text{ mm}$.
   * Tujuan: Format vertikal optimal untuk lembar naskah penugasan/ujian, kisi-kisi rubrik penilaian bertingkat, dan tanda tangan pengesahan tripartit.

---

## 4. Struktur 12 Tabel Baku dalam Template Master

Template master terdiri atas 12 struktur tabel berkesinambungan:

1. **Tabel 1 — Cover / Sampul Depan (Hal 1):** Judul RPS, nama pengampu, NUPTK, nama prodi/fakultas/universitas, tahun akademik.
2. **Tabel 2 — Header Penjaminan Mutu & Identitas MK (Hal 2):** Logo UWG, nomor dokumen SPMI (`071030.{{kodeprodi}}`), nama MK, kode MK, rumpun keilmuan, bobot SKS Teori & Praktikum, semester, dan tanggal penyusunan.
3. **Tabel 3 — Otorisasi Dokumen (Hal 2):** Tiga kolom sejajar: Pengembang RPS, Koordinator RMK, dan Ketua Program Studi.
4. **Tabel 4 — Capaian Pembelajaran (Hal 2):** Pemetaan CPL Prodi yang dibebankan, Capaian Pembelajaran Mata Kuliah (CPMK ABCD + Bloom), dan Sub-CPMK.
5. **Tabel 5 — Matriks Korelasi CPL terhadap CPMK & Bobot (Hal 2):** Pemetaan silang ketercapaian CPL vs CPMK beserta persentase kontribusi asesmen sumatif.
6. **Tabel 6 — Deskripsi Singkat MK & Bahan Kajian (Hal 3):** Ringkasan ruang lingkup mata kuliah dan pokok materi keilmuan.
7. **Tabel 7 — Pustaka, Pengampu, & Prasyarat (Hal 3):** Referensi utama, referensi pendukung, dosen pengampu, dan mata kuliah prasyarat akademik.
8. **Tabel 8 — Matriks 16 Pertemuan Mingguan (Hal 3–4):** Tabel 8 kolom baku SN-Dikti:
   - Kolom 1: Minggu Ke (`[mingguke]`)
   - Kolom 2: Kemampuan Akhir Tahapan Belajar / Sub-CPMK (`[kemampuan_subcpmk]`)
   - Kolom 3: Penilaian Indikator (`[indikator]`)
   - Kolom 4: Penilaian Kriteria & Teknik (`[kriteriateknik]`)
   - Kolom 5: Bentuk, Metode & Penugasan Luring [Estimasi Waktu: TM, PT, BM] (`[luring]`)
   - Kolom 6: Bentuk, Metode & Penugasan Daring (`[daring]`)
   - Kolom 7: Materi Pembelajaran [Pustaka] (`[materi]`)
   - Kolom 8: Bobot Penilaian % (`[bobot_nilai]`) — total akumulasi 100%.
9. **Tabel 9 — Lampiran Tugas 1 & Rubrik (Hal 5, Portrait):** Naskah soal Tugas 1 (Pekan 4–5, bobot 20%) + matriks rubrik analitik 4 level.
10. **Tabel 10 — Lampiran UTS & Rubrik (Hal 6, Portrait):** Naskah soal UTS (Pekan 8, bobot 25%–30%) + matriks rubrik evaluasi tengah semester.
11. **Tabel 11 — Lampiran Tugas 2 & Rubrik (Hal 7, Portrait):** Naskah soal Tugas 2 (Pekan 12, bobot 20%–25%) + matriks rubrik analitik 4 level.
12. **Tabel 12 — Lampiran UAS, Rubrik, & Lembar Pengesahan (Hal 8–9, Portrait):** Naskah soal UAS (Pekan 16, bobot 30%) + matriks rubrik ujian akhir + Lembar Otorisasi Validasi Tripartit (UPM FSTI, Dosen Pengampu, Kaprodi SISTEKIN).

---

## 5. Kamus Tag Placeholder Template Generator (43 Tag)

Sesuai konsensus arsitektur RPS FSTI UWG, terdapat dua jenis *placeholder* di dalam template:

### A. Tag Scalar / Nilai Tunggal (`{{...}}` — 18 Tag)
Digunakan untuk atribut berformat teks pendek, angka, atau tanggal:

| Tag | Deskripsi Atribut | Contoh Isi di SISTEKIN 2026 |
|---|---|---|
| `{{namamk}}` | Nama Mata Kuliah | Arsitektur dan Organisasi Sistem Teknologi Informasi |
| `{{kodemk}}` | Kode Baku Mata Kuliah | `STI-103` |
| `{{rumpunmk}}` | Rumpun Keilmuan MK | Core Sistem dan Teknologi Informasi |
| `{{skst}}` | SKS Teori | `3` |
| `{{sksp}}` | SKS Praktikum | `0` |
| `{{sms}}` | Semester Pelaksanaan | `1` |
| `{{tglsusun}}` | Tanggal Penyusunan RPS | `30 September 2026` |
| `{{kodeprodi}}` | Kode Dokumen SPMI Prodi | `B4.5.2.RPS-STI103` |
| `{{pengembangrps}}`| Nama Dosen Pengembang | Dosen Pengembang Kurikulum SISTEKIN |
| `{{koordinatormk}}`| Koordinator RMK | Koordinator Rumpun Keilmuan |
| `{{ketuaprodi}}` | Nama Ketua Program Studi | Ketua Program Studi S1 SISTEKIN |
| `{{deskripsimk}}` | Deskripsi Singkat MK | Paragraf deskriptif 150–200 kata |
| `{{bahankajian}}` | Pokok Bahan Kajian | Daftar pokok keilmuan BoK |
| `{{dosenpengampu}}`| Dosen Pengampu MK | Nama Dosen, Gelar Akademik |
| `{{mkprasyarat}}` | Mata Kuliah Prasyarat | `-` (atau kode & nama MK prasyarat) |
| `{{namadosen}}` | Nama Dosen (Cover & Validasi)| Nama Dosen Pengampu Utama |
| `{{nuptk}}` | NUPTK/NIDN Dosen | Nomor Pokok Tenaga Kependidikan |
| `{{prodi}}` | Nama Program Studi | S1 Sistem dan Teknologi Informasi |

### B. Tag Blok Konten Dinamis (`[...]` — 25 Tag)
Digunakan untuk konten berulang (*looping*), tabel multi-baris, daftar butir, dan matriks rubrik:

| Tag | Deskripsi Konten Dinamis |
|---|---|
| `[nocpl]`, `[cpl]` | Nomor dan deskripsi rumusan Capaian Pembelajaran Lulusan (`CPL-01` s.d. `CPL-14`). |
| `[nocpmk]`, `[cpmk]` | Nomor dan deskripsi Capaian Pembelajaran Mata Kuliah (CPMK 1 s.d. CPMK 4). |
| `[nosubcpmk]`, `[subcpmk]` | Nomor dan deskripsi Sub-CPMK tiap tahapan belajar. |
| `[tabelkolerasi]` | Matriks silang CPL vs CPMK lengkap dengan persentase bobot asesmen. |
| `[pustakautama]`, `[pustakapendukung]` | Daftar referensi buku teks primer ber-ISBN dan artikel jurnal/standar industri. |
| `[mingguke]` s.d. `[bobot_nilai]` | Baris data matriks 16 pertemuan mingguan (8 kolom SN-Dikti). |
| `[soaltugas1]`, `[rubriktugas1]` | Naskah instruksi soal dan tabel kriteria rubrik Tugas 1 (Pekan 4). |
| `[soaluts]`, `[rubrikuts]` | Naskah soal ujian dan rubrik penilaian UTS (Pekan 8). |
| `[soaltugas2]`, `[rubriktugas2]` | Naskah instruksi soal dan tabel kriteria rubrik Tugas 2 (Pekan 12). |
| `[soaluas]`, `[rubrikuas]` | Naskah soal komprehensif dan rubrik penilaian UAS (Pekan 16). |

---

## 6. Ekosistem Generator & Otomasi yang Telah Dibangun

Untuk menjamin kepatuhan 100% terhadap template tanpa manipulasi manual yang rentan kesalahan (*human error*), telah dibangun ekosistem generator teruji:

1. **`generate_rps_md.py`:**
   - Membangkitkan keluaran Markdown formal yang mempertahankan struktur 12 tabel dan 8 kolom matriks mingguan.
   - Dilengkapi validasi struktur ketat (`--check`), pencegahan penimpaan file tidak disengaja, dan verifikasi konsistensi relasi CPL–CPMK–Sub-CPMK.
2. **`generate_rps_docx.py`:**
   - Membaca data JSON terkurasi dan mengisikannya langsung ke `Template_RPS_GEN_2026_20092026-SWO.docx`.
   - Menghasilkan berkas Word `.docx` siap cetak dengan mempertahankan orientasi campuran (*Hybrid Orientation* Landscape & Portrait) dan *styling* tabel asli.
3. **Unit Uji Otomatis (*Test Suite*):**
   - `test_generate_rps_md.py` & `test_generate_rps_docx.py` menguji integritas parser, keunikan ID, total bobot tepat 100%, dan ketiadaan *leftover placeholder tags*.

---

## 7. Status Portofolio Perangkat Ajar yang Tersedia

Di dalam repositori, implementasi RPS OBE telah tersedia pada dua tingkatan:

1. **Unit Percontohan (*Pilot Units*):**
   - **`STI-416` Pengembangan Web Back End:** Unit percontohan awal versi simplified (`RPS_STI-416_Web_Back_End_Development_V2_SIMPLIFIED.md`).
   - **`STI-311` Pengembangan Web Front End:** Unit implementasi penuh pertama yang mengintegrasikan skema data JSON (`065_STI-311_RPS.json`), Markdown terstruktur template (`065_1_RPS_STI-311_...md`), dan berkas Word terisi (`DOCX/RPS_STI-311_TEMPLATE_REVISI_07112026.docx`).
2. **Paket 230 Berkas Perangkat Ajar (`PERANGKAT_AJAR/`):**
   - Seluruh 46 mata kuliah Core STI dan Peminatan (STA, STB, STC) telah memiliki paket dasar 5 dokumen OBE (`_1_RPS`, `_2_SAP`, `_3_OUTLINE_MODUL`, `_4_RENCANA_EVALUASI_ASESMEN`, `_5_RUBRIK_PENILAIAN`) dari seri `055_*` s.d. `100_*` yang siap diperkaya secara substantif menggunakan engine generator di atas.

---

## 8. Panduan Ringkas bagi Pengembang Mata Kuliah Baru

Bagi dosen pengampu atau pengembang kurikulum yang hendak menyusun RPS untuk mata kuliah berikutnya:

1. **Jangan Mengubah Berkas Master:** Gunakan salinan dari `Template_RPS_GEN_2026_20092026-SWO.docx` atau jalankan via skrip `generate_rps_docx.py`.
2. **Rujuk Dokumen Kebenaran Tunggal (*Single Source of Truth*):**
   - Identitas, SKS, Semester, Prasyarat $\rightarrow$ **Dokumen 005**.
   - Rumusan CPL $\rightarrow$ **Dokumen 003 / Dokumen 004** (`CPL-01` s.d. `CPL-14`).
   - Rumusan CPMK ABCD, Sub-CPMK, & Boundary Guardrails $\rightarrow$ **Dokumen 007 & Dokumen 043**.
   - Skema 4 Titik Asesmen Baku (T1 20%, UTS 25/30%, T2 20/25%, UAS 30%) $\rightarrow$ **Dokumen 008**.
   - Rubrik Analitik Kinerja 4 Level $\rightarrow$ **Dokumen 018 & Dokumen 033**.
3. **Penyimpanan Berkas Hasil:**
   - Seluruh berkas RPS Markdown mata kuliah wajib disimpan di folder `KURIKULUM2026_REVISI/PERANGKAT_AJAR/` sesuai format `<NNN>_1_RPS_<KODE>_<NAMA>_<DDMMYYYY>.md`.
   - Berkas keluaran Microsoft Word disimpan di folder `KURIKULUM2026_REVISI/DOCX/`.

---

*Laporan inventarisasi ini merupakan dokumen resmi pendamping pengembangan kurikulum OBE SISTEKIN FSTI Universitas Widyagama Malang.*

