# 113_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## FST-714 — SKRIPSI / TUGAS AKHIR (*Undergraduate Thesis / Final Project*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-FST714` · **Bobot:** 6 SKS (`Mandiri`) · **Semester:** 8 — Tahap *Mastery*  
**Klaster Asesmen MK (Dok 018):** Klaster 4 (`K-4`) — Tugas Akhir, Proyek Inovasi & Publikasi Ilmiah  
**CPL Dibebankan:** `CPL-01`–`CPL-14` (14 CPL menyeluruh, Level `M`) · **Jalur:** 4 Opsi Setara (Dok 009)  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN PPEPP

Selaras **Dokumen 008 (Sistem Asesmen OBE), 009 (Pedoman TA Non-Skripsi), 018 (Klaster Rubrik), 043 (Guardrails), dan RPS `FST-714`**, mata kuliah `FST-714 Skripsi / Tugas Akhir` (6 SKS `Mandiri`) menerapkan skema bobot baku Klaster `K-4` dengan pemetaan presisi ke keempat CPMK:

* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-05`–`CPL-08` & `CPL-09`–`CPL-14`)** — *Laporan Kemajuan Riset 25% + Kode Baseline/Novelty + Log Eksperimen Batch-1*.
* **UTS-Monev (Pekan 8 — 25%) → `CPMK-2` (`CPL-02` & `CPL-09`–`CPL-14`)** — *Monev Kemajuan Riset 50% (Presentasi 10' + QA 15') oleh Tim Pembimbing*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-01` & `CPL-03`)** — *Naskah Lengkap Bab 1–5 + Artikel IMRAD + Bukti HKI + Lembar Turnitin <20%*.
* **UAS-Sidang (Pekan 16 — 30%) → `CPMK-4` (`CPL-01`, `CPL-03`, `CPL-04`)** — *Sidang Pendadaran Sarjana: Presentasi & Live Demo 20' (50% UAS) + Tanya Jawab 40' (50% UAS)*.
* **Kepatuhan PPEPP & IKU 7:** Seluruh asesmen bersifat *Project-Based & Performance Assessment* (100%). Nilai FST-714 menjadi penentu utama yudisium & agregasi CPL *Mastery* (ambang cohort ≥ 75% lulus tepat waktu, Dok 010 Tracer Study).

> **Prinsip Remedial Berkeadilan:** Mahasiswa yang gagal pada salah satu titik (skor < 50) mendapat **1 kesempatan remedial dalam 2 minggu** dengan plafon nilai 70 (B). Gagal UTS-Monev (<50% kemajuan) → surat peringatan + perpanjangan 2 minggu. Gagal Turnitin (>20%) → revisi parafrasa + uji ulang (maks. 3x). Gagal Sidang (nilai < 65) → mengulang sidang 1x pada periode yudisium berikutnya (maks. 1 bulan).

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-05`–`CPL-08` (P1–P4)**<br>**& `CPL-09`–`CPL-14` (KK1–KK6)**<br>*Level: M* | **`CPMK-1`**<br>(C6) | `1.1` (Dataset etis & preprocessing) | Mg 4 | Laporan kemajuan: kelengkapan dataset card, kebersihan data, kepatuhan UU PDP | **RTM-1 Artefak-1** Dataset card + log preprocessing + surat izin | Sumatif | 5% | **20%** |
| | | `1.2` (Baseline reproduksibel) | Mg 4 | Inspeksi repo: keberfungsian, modularitas, README reproduksibel | **RTM-1 Artefak-2** Repo Git (tag tugas1) + diagram arsitektur | Sumatif | 6% | |
| | | `1.3` (Novelty & tuning) | Mg 4 | Code review: kejelasan kebaruan, kualitas kode, log Batch-1 | **RTM-1 Artefak-3** Kode novelty + log MLflow Batch-1 + draf Bab 4 §1 | Sumatif | 9% | |
| **`CPL-02` (KU1)**<br>**& `CPL-09`–`CPL-14` (KK1–KK6)**<br>*Level: M* | **`CPMK-2`**<br>(C5) | `2.1` (Benchmark SOTA fair) | Mg 8 | Presentasi monev: fairness baseline, pemilihan SOTA mutakhir | **Soal Monev** Tabel komparasi + script evaluasi | Sumatif | 8% | **25%** |
| | | `2.2` (Statistik & visual) | Mg 8 | Analisis notebook: uji signifikansi, IK 95%, kualitas grafik | **Soal Monev** Notebook + 3–5 grafik final | Sumatif | 8% | |
| | | `2.3` (Bab 4 draf) | Mg 8 | Reviu tulisan: kedalaman pembahasan, koherensi, limitasi | **Soal Monev** Draf Bab 4 (≥50%) | Sumatif | 9% | |
| **`CPL-01` (S1)**<br>**& `CPL-03` (KU2)**<br>*Level: M* | **`CPMK-3`**<br>(C6) | `3.1` (Bab 5 sintesis) | Mg 12 | Reviu Bab 5: menjawab rumusan masalah, relevansi saran | **RTM-2 Artefak-1** Draf Bab 5 + matriks keterlacakan | Sumatif | 5% | **25%** |
| | | `3.2` (Artikel IMRAD) | Mg 12 | Reviu artikel: format IMRAD, kontribusi, sitasi IEEE | **RTM-2 Artefak-2** Naskah artikel (PDF) | Sumatif | 7% | |
| | | `3.3` (HKI DJKI) | Mg 12 | Verifikasi bukti EC HKI | **RTM-2 Artefak-3** Bukti permohonan HKI | Sumatif | 4% | |
| | | `3.4` (Turnitin <20%) | Mg 12 | Uji Turnitin <20% + AI <15% + deklarasi orisinalitas | **RTM-2 Artefak-4** Lembar Turnitin + naskah Bab 1–5 | Sumatif | 9% | |
| **`CPL-01` (S1)**<br>**`CPL-03` (KU2)**<br>**`CPL-04` (KU3)**<br>*Level: M* | **`CPMK-4`**<br>(C5) | `4.1` (Administrasi & persetujuan) | Mg 16 | Verifikasi checklist yudisium + lembar persetujuan | **Sidang Artefak** Berkas sidang (SIAKAD) | Sumatif | 5% | **30%** |
| | | `4.2` (Presentasi+Demo 20') | Mg 16 | Penilaian dewan: kejelasan, demo, manajemen waktu | **Sidang Artefak** Slide + live demo (50% UAS) | Sumatif | 12% | |
| | | `4.2` (Tanya jawab 40') | Mg 16 | Penilaian dewan: penguasaan metode, argumen, etika | **Sidang Artefak** QA komprehensif (50% UAS) | Sumatif | 13% | |
| **TOTAL** | **4 CPMK** | **12 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI SIDANG

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Pekan 4: Kemajuan Riset 25% — CPMK-1, 20%)

* **Jadwal & Bobot:** Rilis **Pekan 1** (saat bimbingan-1), Kumpul & Verifikasi **Pekan 4** (Bimbingan-4) · Bobot **20%** (`CPMK-1` → `CPL-05`–`CPL-08` & `CPL-09`–`CPL-14`).
* **Sifat:** *Project-Based — Individual* (satu mahasiswa satu skripsi; kolaborasi diperbolehkan untuk pengumpulan data dengan deklarasi kontribusi).
* **Spesifikasi Artefak Wajib (4 berkas):**
  1. **Dataset Card (2–3 hal):** Sumber, ukuran, distribusi kelas, bias potensial, lisensi, teknik anonimisasi UU PDP, bukti surat izin etik/mitra (scan).
  2. **Repositori Git (tag `tugas1`):** Struktur rapi (`README.md` + env + src + data + experiments), baseline berjalan (`git clone + pip install + python train.py → hasil`), diagram arsitektur (Mermaid/draw.io).
  3. **Kode Novelty + Log Batch-1:** Pseudocode 1 hal + kode terimplementasi + log MLflow/W&B (CSV/URL) berisi ≥ 10 run tuning (param, metric, seed, waktu).
  4. **Draf Bab 4 §Hasil Awal (3–5 hal):** Tabel hasil Batch-1 + 1–2 grafik + interpretasi awal.
* **Teknik Penilaian:** Pembimbing verifikasi artefak di Bimbingan-4 (inspeksi repo + log + dataset card) + rubrik analitik Tugas 1 (K-4).
* **Jalur Diferensiasi:**
  - *J1 Riset:* Dataset benchmark publik + novelty algoritmik.
  - *J2 Industri:* Dataset mitra + surat izin penggunaan data.
  - *J3 Startup:* Dataset pasar + bukti wawancara pengguna (5 responden).
  - *J4 Publikasi:* Dataset + gap literatur dari jurnal target.

### 3.2 Spesifikasi Monev Tengah Semester (UTS-Monev — Pekan 8: Kemajuan 50% — CPMK-2, 25%)

* **Format & Bobot:** **Monev Presentasi 10' + Tanya Jawab 15'** di hadapan Tim Pembimbing (150 menit total termasuk deliberasi) · Bobot **25%** (`CPMK-2` → `CPL-02` & `CPL-09`–`CPL-14`).
* **Jadwal:** Pekan 8 (minggu monev fakultas) — dijadwalkan Panitia TA (bukan pembimbing individu).
* **Spesifikasi Artefak:**
  1. Slide monev 8–10 hal (masalah → metode → hasil 50% → kendala → rencana).
  2. Tabel komparasi SOTA (≥ 2 baseline, metrik identik, mean ± std).
  3. Notebook analisis statistik (Uji-t/Wilcoxon + p-value + IK 95% + 3–5 grafik).
  4. Draf Bab 4 ≥ 50% (Setup + Hasil Utama + Pembahasan Awal + Limitasi).
  5. Logbook harian + kartu bimbingan 4x (Pekan 1–7).
* **Teknik Penilaian:** Dewan monev (pembimbing + koordinator TA) nilai presentasi + artefak via rubrik Monev (K-4). Hasil: **Lulus Monev (≥ 50% kemajuan)** atau **Peringatan + Perpanjangan 2 minggu** (jika <50%).
* **Dampak ke Jalur:**
  - *J2:* Tambahkan bukti deploy awal di mitra (screenshot/log).
  - *J3:* Tambahkan metrik traksi awal (retensi/NPS).
  - *J4:* Tambahkan outline artikel + jurnal target.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Pekan 12: Naskah Lengkap — CPMK-3, 25%)

* **Jadwal & Bobot:** Rilis **Pekan 9** (pasca-monev), Kumpul & Verifikasi **Pekan 12** (Bimbingan-12) · Bobot **25%** (`CPMK-3` → `CPL-01` & `CPL-03`).
* **Sifat:** *Manuscript-Based — Individual* — Penulisan ilmiah sebagai bukti integritas akademik.
* **Spesifikasi Artefak Wajib (5 berkas):**
  1. **Naskah Lengkap Bab 1–5 (80–120 hal, PDF):** Format Panduan Skripsi FSTI (A4, margin 4-3-3-3 cm, TNR 12, spasi 1.5, sitasi IEEE numerik [1], daftar pustaka ≥ 25 sumber, 70% 5 tahun terakhir).
  2. **Naskah Artikel IMRAD (6–10 hal, PDF):** Format IEEE/ACM, siap submit (Title, Abstract 250 kata, Keywords, IMRAD, References ≥ 15).
  3. **Bukti Pendaftaran HKI (PDF):** EC (Electronic Certificate) atau Nomor Permohonan e-HKI DJKI (https://e-hakcipta.dgip.go.id) — judul ciptaan = judul program, jenis = Program Komputer.
  4. **Lembar Hasil Turnitin (PDF):** Similarity <20% (exclude bibliography & quotes), AI-writing <15% (bila tersedia), + surat pernyataan orisinalitas bertanda tangan.
  5. **Repositori Git Final (tag `tugas2`):** Kode lengkap + data (atau link dataset) + script reproduksi + `REPRODUCE.md`.
* **Teknik Penilaian:** Pembimbing verifikasi naskah + artikel + HKI + Turnitin di Bimbingan-12 (cek konsistensi Bab 1–5, format IMRAD, kelengkapan HKI) + rubrik Tugas 2 (K-4).
* **Jalur Diferensiasi:**
  - *J2:* Tambahkan Surat Keterangan Implementasi Mitra (kop surat, cap, tanda tangan) + TRL Assessment Sheet (TRL ≥ 6).
  - *J3:* Tambahkan Lean Canvas 1 hal + Pitch Deck 10 slide + bukti traksi (screenshot dashboard pengguna/MoU).
  - *J4:* Artikel harus sudah *submitted* (bukti submission ID) — jika sudah *accepted*, bobot artikel naik 10% (diambil dari bobot HKI).

### 3.4 Spesifikasi Ujian Akhir Semester (UAS — Pekan 16: Sidang Pendadaran — CPMK-4, 30%)

* **Format & Bobot:** **Sidang Pendadaran Sarjana SISTEKIN** — *Presentasi & Live Demo 20 menit (50% UAS) + Tanya Jawab 40 menit (50% UAS)* = 150 menit total · Bobot **30%** (`CPMK-4` → `CPL-01`, `CPL-03`, `CPL-04`).
* **Jadwal:** Pekan 15–16 (periode sidang fakultas) — dijadwalkan Panitia TA H-7.
* **Dewan Penguji:** 3 dosen (1 Pembimbing Utama + 2 Penguji Independen). Untuk J2/J3, salah satu penguji dapat dari mitra/industri (dosen tamu). Ketua sidang adalah penguji senior (bukan pembimbing).
* **Syarat Maju Sidang (verifikasi Pekan 13):**
  1. Lulus Tugas 1 (≥ 50) & UTS-Monev (≥ 50% kemajuan).
  2. Lulus Tugas 2 (Turnitin <20%, HKI terdaftar, artikel siap).
  3. Kartu bimbingan minimal 8x pertemuan (termasuk monev).
  4. Lembar persetujuan pembimbing (2 tanda tangan, cap prodi).
  5. Transkrip sementara ≥ 120 SKS + bebas pustaka/keuangan.
  6. Untuk J2: Surat mitra + TRL sheet. J3: Bukti traksi. J4: Bukti accepted jurnal (jika ada).
* **Spesifikasi Presentasi 20':**
  - Slide 15–20 hal (16:9): Cover → Problem & Gap (3') → Tujuan & Kontribusi (2') → Metode/Arsitektur (4') → Hasil (5' + demo) → Kesimpulan (3') → Penutup (1') → Demo live (terintegrasi).
  - Demo: *Live* (bukan video saja) — penguji dapat minta input acak. Sediakan video backup 2 menit antisipasi gagal jaringan.
  - Manajemen waktu ketat: bel di 15' & 19', stop di 20'.
* **Spesifikasi Tanya Jawab 40':**
  - Penguji gali: (1) Novelty & kontribusi, (2) Alternatif desain, (3) Limitasi & ancaman validitas, (4) Etika data, (5) Replikasi & generalisasi, (6) Implikasi praktis, (7) Wawasan ke depan. Pembimbing tidak boleh menjawab untuk mahasiswa.
  - Mahasiswa boleh mengakui keterbatasan dengan jujur + tawarkan solusi ("Saya belum coba X, tetapi hipotesis saya X akan...").
* **Teknik Penilaian:** Dewan nilai presentasi + demo (50%) & QA (50%) via rubrik UAS (K-4). Hasil sidang: **Lulus (A/B) / Lulus dengan Revisi Minor (B/C, 1–2 minggu) / Mengulang Sidang (D/E, periode berikut)**. Nilai UAS = rerata 3 penguji (jika selisih > 15 poin, musyawarah).
* **Pasca-Sidang:** Revisi pasca-sidang (maks. 2 minggu) → verifikasi pembimbing → upload naskah final ke SIAKAD + repositori kampus → yudisium fakultas.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{FST-714}$)

$$NA_{FST-714} = 0,20\,S_{Tugas1} + 0,25\,S_{UTSMonev} + 0,25\,S_{Tugas2} + 0,30\,S_{UAS-Sidang}$$

* $S_{Tugas1}$ = Skor Tugas 1 (Pekan 4, CPMK-1, 20%)
* $S_{UTSMonev}$ = Skor UTS-Monev 50% (Pekan 8, CPMK-2, 25%)
* $S_{Tugas2}$ = Skor Tugas 2 (Pekan 12, CPMK-3, 25%)
* $S_{UAS-Sidang}$ = Skor Sidang Pendadaran (Pekan 16, CPMK-4, 30%)

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004, 008)

FST-714 berkontribusi ke 14 CPL pada level *Mastery* (bobot SKS tertimbang 6 SKS per CPL):

1. **Ketercapaian `CPL-05`–`CPL-08` & `CPL-09`–`CPL-14` via `CPMK-1` (20%):**
   $$Score_{CPL_{P/KK},FST714}(i) = \frac{0,20\,S_{Tugas1}(i)}{0,20} = S_{Tugas1}(i)$$
   *(Kontribusi ke agregasi prodi = 6 SKS per CPL)*

2. **Ketercapaian `CPL-02` & `CPL-09`–`CPL-14` via `CPMK-2` (25%):**
   $$Score_{CPL_{02/KK},FST714}(i) = S_{UTSMonev}(i)$$

3. **Ketercapaian `CPL-01` & `CPL-03` via `CPMK-3` (25%):**
   $$Score_{CPL_{01/03},FST714}(i) = S_{Tugas2}(i)$$

4. **Ketercapaian `CPL-01`, `CPL-03`, `CPL-04` via `CPMK-4` (30%):**
   $$Score_{CPL_{01/03/04},FST714}(i) = S_{UAS-Sidang}(i)$$

*Agregasi akhir CPL prodi (Dok 008):* $CPL_{prodi}(i) = \frac{\sum_{MK} (SKS_{MK} \times Bobot_{MK→CPL} \times Score_{MK}(i))}{\sum_{MK} (SKS_{MK} \times Bobot_{MK→CPL})}$ — FST-714 dengan 6 SKS memberikan leverage terbesar.

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial/Yudisium

* **Ambang Lulus MK FST-714:** Skor akhir $NA_{FST-714} \ge 65,0$ (**C+ / 2,50**) — sama dengan ambang CPL *Mastery*. Mahasiswa dengan $NA < 65,0$ **tidak yudisium**.
* **Ambang Revisi Sidang:** Jika Sidang = Lulus dengan Revisi, mahasiswa wajib selesaikan revisi (maks. 2 minggu) & verifikasi pembimbing sebelum yudisium. Gagal revisi → nilai turun 1 huruf.
* **Remedial Tugas 1/2 & Monev:** Maks. 1x remedial per titik dengan plafon 70 (B). Remedial Tugas 1/2: perbaikan artefak 1 minggu. Remedial Monev: perpanjangan 2 minggu + monev ulang.
* **Mengulang Sidang:** Jika UAS < 50 atau gagal sidang, mengulang sidang 1x pada periode yudisium berikutnya (maks. 1 bulan) dengan perbaikan naskah menyeluruh. Gagal 2x → mengulang MK FST-714 semester depan.
* **Integritas Akademik:** Plagiasi >20% similarity atau fabrikasi data yang terbukti → nilai E (gagal) + sidang etik + sanksi skorsing (sesuai Panduan Akademik UWG).

### 4.4 Matriks Konversi Nilai Huruf & Predikat Yudisium (KPT 2024)

| Skor Akhir ($NA_{FST-714}$) | Huruf | Bobot | Predikat Sidang | Status Yudisium |
|:---:|:---:|:---:|---|---|
| 85–100 | A | 4,00 | *Cumlaude* (IPK ≥ 3,51 & masa studi ≤ 8 sem) / Sangat Memuaskan | Lulus |
| 80–84 | A- | 3,75 | Sangat Memuaskan | Lulus |
| 75–79 | B+ | 3,50 | Sangat Memuaskan | Lulus |
| 70–74 | B | 3,00 | Memuaskan | Lulus |
| 65–69 | B- | 2,75 | Memuaskan (Ambang Mastery) | Lulus |
| 60–64 | C+ | 2,50 | Cukup — **Tidak Lulus FST-714 (harus remedial)** | Tidak Yudisium |
| 55–59 | C | 2,00 | Kurang | Tidak Lulus |
| <55 | D/E | 1,00/0 | Gagal | Tidak Lulus |

> **Catatan Cumlaude:** Sesuai Permendikbudristek 53/2023, predikat *Dengan Pujian* mensyaratkan IPK ≥ 3,51, masa studi ≤ 8 semester (4 tahun), tidak pernah mengulang MK, dan nilai FST-714 ≥ A- (≥ 80).

