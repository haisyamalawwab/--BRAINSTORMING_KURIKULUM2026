# LAPORAN PENGEMBANGAN RPS STI-311 — PENGEMBANGAN WEB FRONT END

Unit pilot ke-2 RPS Batch Generator FSTI UWG (isi penuh template) — mengikuti Master Prompt Generator RPS OBE (Dok 053) tahap T0–T6. Tanggal: 30 September 2026.

## 1. Tabel Keluaran

| Keluaran | Path | Status |
|---|---|---|
| DOCX RPS (isi penuh 12 tabel) | `DOCX/RPS_STI-311_Web_Front_End_Development.docx` | Terisi, zero residual |
| Markdown companion | `RPS_STI-311_Web_Front_End_Development.md` | Satu sumber kebenaran dengan DOCX |
| Skrip generator (idempoten) | `_tools/generate_rps_sti311_docx.py` | Selalu mulai dari template bersih |
| Verifikator T5 independen | `_tools/verify_rps_sti311_t5.py` | 4 kelompok cek, lulus penuh |
| Ekstraksi T1 Dok 043 | `043_STI-311_WEB_FRONT_END_DEVELOPMENT_30092026.md` | Verbatim baris 633–686 |

## 2. Mapping 43 Tag (18 `{{...}}` + 25 `[...]`)

| Tag | Nilai (ringkas) | Sumber | Status |
|---|---|---|---|
| `{{namamk}}` | Pengembangan Web Front End (Web Front End Development) | Dok 005 baris 118/226; EN Dok 007 §22 | verbatim |
| `{{kodemk}}` | STI-311 | Dok 005 | verbatim |
| `{{rumpunmk}}` | Rekayasa Perangkat Lunak & Platform (Core STI) | Dok 007 Tabel 22.A | verbatim |
| `{{skst}}` / `{{sksp}}` | 2 / 1 | Dok 007 22.A: 3 SKS +P (100m teori + 170' lab) | turunan |
| `{{sms}}` | 3 (Ganjil) | Dok 005 | verbatim |
| `{{tglsusun}}` | 30 September 2026 | Parameter | parameter |
| `{{kodeprodi}}` | B4.5.2.RPS-STI311 | Parameter (pola master prompt) | parameter |
| `{{pengembangrps}}` | Tim KBK Rekayasa Perangkat Lunak & Platform | Aturan KBK per rumpun (master prompt T3) | turunan |
| `{{koordinatormk}}` | Dr. Roni Wahyu, S.Kom., M.T. | Kamus tag Dok 052 baris 204 | verbatim |
| `{{ketuaprodi}}` | [Nama Ketua Prodi SISTEKIN] | Tanpa sumber | placeholder |
| `{{prodi}}` | Sistem dan Teknologi Informasi | Identitas prodi | verbatim |
| `{{namadosen}}` / `{{nuptk}}` / `{{dosenpengampu}}` | [Nama Dosen Pengampu 1/2/STI-311], [NUPTK Dosen] | Tanpa sumber | placeholder |
| `{{mkprasyarat}}` | FST-102 Algoritma dan Pemrograman | Dok 005 & Dok 007 22.A | verbatim |
| `{{deskripsimk}}` | Deskripsi MK + handoff ke STI-416 | Sintesis Dok 007 22.A/B + guardrail Dok 043 | komposisi |
| `{{bahankajian}}` | BK-IS12, BK-IT04 + 15 pokok bahasan | BoK Dok 043; backbone Dok 007 22.C | turunan |
| `[nocpl]`/`[cpl]` | P4, KK5 + rumusan penuh | Dok 003 tabel CPL | verbatim |
| `[nocpmk]`/`[cpmk]` | CPMK-1..4 (ABCD + Bloom C3/C3/C6/C5) | Dok 043 baris 633–686; Dok 007 22.B | verbatim |
| `[nosubcpmk]`/`[subcpmk]` | Sub-CPMK-1.1..4.2 (8 butir) | Dok 043 (verbatim) | verbatim |
| `[tabelkolerasi]` | P4→CPMK-1,2 (T1 20%+UTS 25%=45%); KK5→CPMK-3,4 (T2 25%+UAS 30%=55%) | Mapping Dok 043 + skema Dok 008 | turunan |
| `[pustakautama]` / `[pustakapendukung]` | 5 + 7 pustaka | Referensi standar bidang | komposisi* |
| `[mingguke]` | Pekan 1–16 | Dok 007 Tabel 22.C | verbatim |
| `[kemampuan_subcpmk]` | Topik Tabel 22.C × kode Sub-CPMK Dok 043 | Dok 007 × Dok 043 | turunan |
| `[indikator]` / `[kriteriateknik]` | Indikator per pekan; rubrik kompilasi/analitik | Diturunkan dari rumusan kemampuan; gaya Dok 018 | turunan |
| `[luring]` / `[daring]` | Distribusi 100'/170'/270'; Edlink + GitHub Classroom | Dok 007 22.C | komposisi* |
| `[materi]` | Pokok bahasan + sitasi pustaka [1]..[10] | Dok 007 22.C | verbatim |
| `[bobot_nilai]` | T1 20% (P4), UTS 25%, T2 25% (P4/KK5), UAS 30%; — untuk non-asesmen | Skema 4x Dok 008 (tipe +P) | verbatim |
| `[penugasan1]`/`[rubriktugas1]` | Tugas 1 Milestone Proyek 1 + rubrik analitik 6 kriteria | Gaya pilot STI-416/018 | komposisi* |
| `[soaluts]`/`[rubrikuts]` | UTS praktik live coding + rubrik 5 kriteria | idem | komposisi* |
| `[tugas2]`/`[rubriktugas2]` | Tugas 2 Milestone Proyek 2 + rubrik 5 kriteria | idem | komposisi* |
| `[soaluas]`/`[rubrikuas]` | UAS Demo Day & defense + rubrik 7 kriteria | idem | komposisi* |

\* komposisi baru yang wajib divalidasi KBK/GPM (lihat Bagian 3).

## 3. Daftar Butir Konfirmasi

1. **Nama pejabat & dosen** (placeholder di keluaran): Ketua Prodi SISTEKIN, Kepala UPM FSTI, 2 dosen pengampu + NUPTK. Blok pengesahan DOCX memakai label bawaan template ("Nama Pejabat UPM / Program Studi", NUPTK `xxxx`).
2. **Kamus Dok 052 baris 208** menawarkan default `{{namadosen}}` = "Dr. Roni Wahyu, S.Kom., M.T." — perlu konfirmasi apakah beliau pengampu STI-311 sebelum diisi.
3. **Pustaka utama & pendukung (12 entri)** = komposisi referensi standar bidang (Duckett, Robbins, Banks & Porcello, MDN, react.dev, dst.) — perlu validasi KBK/GPM.
4. **Seluruh instrumen lampiran** (soal + 4 rubrik) = komposisi baru mengikuti gaya pilot STI-416 & rubrik master Dok 018 — perlu validasi KBK/GPM.
5. **Kolom Daring** menyebut platform "Edlink" dan "GitHub Classroom" — konfirmasi nama LMS/tool resmi prodi.

## 4. Discrepancy T1 (dilaporkan, tidak diubah diam-diam)

| # | Temuan | Penyelesaian (aturan master prompt) |
|---|---|---|
| 1 | Nama MK: Dok 005 = "Pengembangan Web Front End"; heading Dok 007 §22 = "Web Front End Development" (kolom ID terisi EN) | Identitas dari Dok 005; EN dalam tanda kurung |
| 2 | Rencana 16 pekan: Dok 043 menyajikan varian generik, Dok 007 Tabel 22.C varian spesifik (topik per pekan berbeda urutan Sub-CPMK) | Backbone = Dok 007 22.C; kode Sub-CPMK = Dok 043 (master prompt T3) |
| 3 | Dok 007 22.C baris UTS menulis "Evaluasi Proyek Awal 50% / Ujian Praktik" | Bobot mengikuti skema baku Dok 008 untuk tipe +P: UTS 25%, T2 25% |

## 5. Batas Verifikasi

**Terverifikasi terprogram** (`_tools/verify_rps_sti311_t5.py`, exit 0):
- Zero residual: 0 dari 43 tag (18 `{{...}}` + 25 `[...]`, kamus Dok 052).
- Posisi: header institusi FSTI/SISTI, identitas 7 kolom, CPL/CPMK/Sub-CPMK verbatim, tabel kolerasi nested, pustaka, 16 baris pekan, 8 lampiran + 4 nested rubrik.
- Konsistensi: SKS/semester/prasyarat = Dok 005; CPMK/Sub-CPMK = Dok 043; jangkar Pekan 4/8/12/16; bobot total 100%; skema +P (UTS 25/T2 25); CPMK↔CPL = Dok 043; handoff STI-416.
- Sampah: tanpa "TEKNIK MESIN", LaTeX residue, `\n` mentah, tag mentah.

**Terverifikasi visual** (render Word → PDF → PNG, 15 halaman diinspeksi):
- Layout landscape (cover, identitas, 16 pekan, sebagian lampiran) dan portrait (lampiran, pengesahan) terbaca; tidak ada mojibake/overflow.

**Perbaikan yang dilakukan pada keluaran selama verifikasi visual** (template master tidak diubah):
1. **Bug sel merge UTS/UAS**: isi berlabel multiline semula tertulis di kolom bobot sempit (gridcol 7) akibat deskripsi "merge kolom 3–8" pada master prompt yang tidak akurat — dump XML membuktikan sel merge lebar adalah gridcol 1–6 dan kolom bobot terpisah. Diperbaiki: label + isi berlabel di sel merge; kolom bobot = "UTS 25%"/"UAS 30%". Jumlah halaman 17 → 15.
2. **Typo warisan template** "Dosen Pengampuh," → "Dosen Pengampu," di tabel pengesahan.

## 5A. Perapian Layout (skill `documents:docx` — rute Format, 30 September 2026)

Diagnosis akar masalah via dump XML + bisect varian + probe posisi Word COM; semua perbaikan diterapkan di `_tools/generate_rps_sti311_docx.py` agar tetap idempoten.

| # | Masalah | Akar Masalah | Perbaikan | Bukti |
|---|---|---|---|---|
| 1 | Halaman kosong berisi hanya "Catatan : TM/PT/BM" | Warisan template: SEMUA baris data Tabel 2 membawa `w:tblHeader` (ulangi-header) — Word menolak menempatkan paragraf setelah tabel di halaman terakhirnya | `tblHeader` dibersihkan dari 14 baris data; hanya R0–R2 yang diulang (standar skill: `tableHeader` hanya baris header) | Catatan kini menempel di bawah tabel (hal. 7); 15 → 12 halaman |
| 2 | Label "Pustaka — Utama :" yatim di dasar halaman | Pemenggalan halaman alami | `keep_with_next` pada baris label 33 & 35 | Blok Pustaka utuh satu halaman (hal. 4) |
| 3 | Luapor 1 baris rubrik ke halaman berikut (2 tempat) | Nested rubrik lebih tinggi dari tinggi minimum kotak lampiran (4116/4664 twips) | Nested rubrik: layout tetap, lebar 8497 twips, lebar kolom proporsional, margin sel rapat, font 9pt, `cantSplit` per baris | 4 rubrik utuh satu halaman masing-masing (hal. 8–11) |
| 4 | Pemenggalan kata di kolom sempit ("Komponen-n", "Bobo-t") | Lebar kolom autofit terlalu sempit | Lebar kolom proporsional baku per jumlah kolom (7/6/3) | Tidak ada pemenggalan kata |
| 5 | Baris data berpotensi terbelah di tengah saat tabel menyeberang halaman | Tanpa `cantSplit` | `cantSplit` pada semua baris data Tabel 2 & nested rubrik | Tidak ada baris terbelah |
| 6 | Postcheck ❌ "3 paragraf kosong penutup section" | Warisan template | Satu paragraf kosong ekor section dibuang | Postcheck 0 error |

**Hasil verifikasi setelah perapian:** T5 lulus penuh (5 kelompok cek, termasuk CEK 5 LAYOUT anti-regresi: tblHeader hanya 0–2, cantSplit, fixed-layout rubrik 8497 twips, font 9pt, keep-with-next) · postcheck.py **0 error** (6/9 lolos) · render Word 12 halaman diinspeksi seluruhnya — header tabel terulang rapi di tiap halaman, tidak ada halaman kosong, tidak ada mojibake.

**Warning postcheck yang tersisa (warisan template, diverifikasi tak berdampak):**
- `[blank-pages]` 4 paragraf kosong ber-PageBreak = pemisah antar-bagian desain template (render membuktikan 0 halaman kosong).
- `[line-spacing]` campuran default/single = gaya template; single dipilih sadar untuk kompaksi rubrik.
- `[font-fallback]` Cambria & Trebuchet MS = font bawaan Windows/Office, tersedia di lingkungan sasaran institusi.

**Belum diverifikasi / catatan minor:**
- Penempatan halaman (page break) bergantung versi Word/printer — namun setelah perapian, seluruh 12 halaman terinspeksi bersih; tidak ada lagi halaman nyaris kosong maupun luapor baris.
- Review substantif oleh KBK/GPM belum dilakukan (butir komposisi pada Bagian 2–3).

## 6. RPS V2 VANILLA — Downgrade Terarah (2 Oktober 2026)

Keputusan pemilik proyek: turunkan level RPS — tanpa framework React, SPA dibangun dengan Vanilla JavaScript, API hanya DIKONSUMSI dari API publik yang endpoint & dokumentasinya tersedia (tidak membangun API). Jawaban kelayakan: **SPA vanilla mungkin dan dibakukan** — SPA adalah arsitektur (satu halaman, routing client-side, state terpusat), bukan framework; pola: komponen fungsi + template literal, Store & Pub/Sub, Hash Router/History API.

**Keluaran baru (V1 verbatim-043 dipertahankan sebagai baseline pembanding):**

| Keluaran | Path |
|---|---|
| DOCX V2 | `DOCX/RPS_STI-311_Web_Front_End_Development_V2_VANILLA.docx` (12 halaman) |
| MD V2 | `RPS_STI-311_Web_Front_End_Development_V2_VANILLA.md` |
| Generator V2 | `_tools/generate_rps_sti311_v2_vanilla_docx.py` |
| Verifikator V2 | `_tools/verify_rps_sti311_v2_t5.py` |

**Status keselarasan V2 terhadap Dok 043 (uji ulang 3 batasan):**

| Batasan | Status | Bukti |
|---|---|---|
| Tanpa SPA React-based | ⚠️ **Deviasi terarah** dari CPMK-3 043 (React.js) — diganti SPA Vanilla JavaScript [C6]; jangkar CPL `KK5 (SPA)` **tetap terampu** karena vanilla SPA tetap SPA. IN-SCOPE 043 lainnya (HTML5, CSS3, Vanilla JS, DOM, State Management) tetap penuh; satu butir IN-SCOPE ("Front-End Framework (React/Vue)") sengaja tidak diajarkan | Deviasi tercatat di header MD V2 |
| Hanya konsumsi API publik terdokumentasi, bukan membuat API | ✅ **Selaras penuh** dengan OUT-OF-SCOPE 043 ("dilarang perancangan API REST gateway") — dipersempit eksplisit di CPMK-4: "RESTful API publik eksternal yang endpoint dan dokumentasinya tersedia"; contoh diajarkan: REST Countries / TheMealDB / JSONPlaceholder | CPMK-4 V2, Tugas 2, rubrik |
| (Warisan) REST API eksternal = konsumsi, bukan penyediaan | ✅ HANDOFF ke STI-416 tetap tercantum | Deskripsi & guardrails V2 |

**Perubahan konten V1 → V2:**

| Elemen | V1 (verbatim 043/007) | V2 VANILLA |
|---|---|---|
| CPMK-1, CPMK-2, Sub-CPMK 1.1/1.2/2.1/2.2/4.2 | verbatim 043 | **tetap verbatim** |
| CPMK-3 & Sub-CPMK 3.1/3.2 | SPA React (Hooks, Context, Router) | SPA komponen fungsi vanilla (Store & Pub/Sub, Hash Router/History API) |
| CPMK-4 & Sub-CPMK-4.1 | integrasi RESTful API eksternal | konsumsi API publik terdokumentasi (dipersempit) |
| Pekan 7, 9–13 | React.js, Hooks, Context API, React Router, Axios, RHF+Zod | Arsitektur SPA Vanilla, State & Re-render, Store & Pub/Sub, Hash Router/History API, Konsumsi API publik, Constraint Validation API |
| Pekan 1–6, 14–16 + skema asesmen 4x (20/25/25/30) | — | **tidak berubah** |
| Pustaka | Learning React, react.dev, React Router, RHF, Zod | Mikowski & Powell *SPA End-to-End*, Osmani *Design Patterns*, MDN History/Fetch, REST Countries, TheMealDB |
| Kolerasi CPL | P4 = T1+UTS (45%); KK5 = T2+UAS (55%) | **tetap** (peta CPMK↔CPL tak berubah) |

**Verifikasi V2:** zero residual 43 tag · CPMK/Sub-CPMK = ekspektasi V2 · **0 residu framework** (React/useEffect/JSX/Axios/Zod/Context API/Virtual DOM — cek regex baru) · jangkar asesmen Pekan 4/8/12/16 + total 100% · jangkar V2 (SPA Vanilla/Hash Router/API publik) tercantum · CEK 5 layout lulus (pewarisan paket perapian Bagian 5A) · postcheck 0 error · render Word 12 halaman diinspeksi (identitas, CPMK, pekan, Tugas 2, UAS).

**Revisi rebalancing V2 (2 Oktober 2026, arah pemilik proyek):** "too much JS" — porsi pokok bahasan 5–12 semuanya JS/SPA/API. Porsi disusun ulang berdasar BoK (Dok 037 menempatkan "HTML5/CSS modern" & "Responsive Layout (Flexbox, CSS Grid)" di urutan pertama IN-SCOPE STI-311):

| Kelompok | Sebelum | Sesudah |
|---|---|---|
| HTML5 | ~1 pekan | **3 pekan** (W2 Semantic & Metadata/SEO, W3 Media & Gambar Responsif, W4 Forms & Aksesibilitas WCAG/ARIA) |
| CSS3 | ~2 pekan | **3 pekan** (W5 Box Model/Unit/Custom Properties, W6 Flexbox & Media Queries, W7 Grid & Dashboard) |
| JS + SPA + API | 8/15 pokok (53%) | **5 pekan** (W9 JS DOM & Event, W10 Modular & Async/Fetch, W11 SPA Vanilla, W12 Routing & Konsumsi API publik, W13 Form & Constraint Validation API) ≈ 36% |
| W1/W8/W14–16 | — | tidak berubah (Pengantar, UTS, Performance, Deployment, UAS) |

Instrumen turut bergeser: **Tugas 1** = dokumen HTML5 semantik, media & aksesibel (bukan layout CSS); **UTS** = praktik Semantic HTML5 + Responsive CSS Grid (CPMK-1); **Tugas 2** = SPA vanilla + routing + konsumsi API publik (cakupan Sub-CPMK 2.1/2.2/3.1 → CPMK-2 & CPMK-3); UAS tetap. Pustaka: + Marcotte *Responsive Web Design*, W3C WCAG 2.1; − Osmani (JS patterns). Kolerasi CPL & skema 4x (20/25/25/30) tetap. Verifikasi: seluruh cek T5 lulus (nol residu framework, ekspektasi pekan baru), postcheck 0 error, render 12 halaman diinspeksi.

**File:** karena `DOCX/RPS_STI-311_..._V2_VANILLA.docx` terkunci oleh Word saat regenerasi, hasil rebalancing diterbitkan sebagai `DOCX/RPS_STI-311_..._V2_VANILLA_REV2.docx` (+ `.md` REV2). Sinkronisasi: tutup file di Word, lalu jalankan `python _tools/generate_rps_sti311_v2_vanilla_docx.py` — generator kini sudah memuat konten rebalancing dan akan menulis ulang file V2 kanonik.

**Catatan tata kelola:** V2 adalah **deviasi terdokumentasi dari Dok 043/007** (CPMK-3 & CPMK-4 + Sub-CPMK terkait + satu butir IN-SCOPE). Agar tidak menjadi sumber inkonsistensi kurikulum, Tim Kurikulum perlu memilih: (a) meratifikasi V2 dan merevisi Dok 043 (2 varian) + Dok 007 §22 pada siklus revisi berikutnya; atau (b) mempertahankan 043 dan memakai V1. Sampai diputuskan, kedua versi tersimpan dengan status masing-masing.



## 7. Langkah Lanjutan

1. **Isi nama pejabat/dosen** pada Daftar Butir Konfirmasi butir 1–2, lalu regenerate.
2. **Validasi KBK/GPM** atas pustaka dan 8 instrumen lampiran (komposisi baru).
3. **Koreksi Master Prompt Dok 053 T2** dengan dua temuan dump XML: (a) ganti "baris UTS merge kolom 3–8" menjadi "sel merge lebar gridcol 1–6 + kolom bobot (gridcol 7) terpisah"; (b) catat defect warisan template — baris data Tabel 2 membawa `tblHeader` yang wajib dibersihkan ke R0–R2 oleh generator.
4. **Terapkan perbaikan pola yang sama ke `_tools/generate_rps_sti309_docx.py`** — terkonfirmasi memiliki bug identik (isi UTS/UAS di kolom bobot sempit); sekalian terapkan paket perapian layout (tblHeader, cantSplit, nested rubrik fixed-width 9pt, keep-with-next) dan audit `postcheck.py`.
5. Regenerasi dokumen setelah konfirmasi via `python _tools/generate_rps_sti311_docx.py` + audit `python _tools/verify_rps_sti311_t5.py`.
