# DIREKTORI PERANGKAT AJAR OBE — PRODI S1 SISTEKIN FSTI UWG (KURIKULUM 2026)

[Indeks lengkap dan tautan lima dokumen per MK](../INDEX.md#perangkat-ajar-core-sti-dan-peminatan) · [README repositori](../../README.md)

> **INSTRUKSI WAJIB BAGI SELURUH GENERATOR BAHAN AJAR & AGENT AI (OpenCode, Arena, Claude Code, Cursor, Skrip Python, maupun Kontributor Manual):**
>
> 1. **Satu-satunya Lokasi Keluaran Perangkat Ajar:** Seluruh paket perangkat ajar mata kuliah (**RPS, SAP, Outline Modul, Rencana Evaluasi & Asesmen, Rubrik Penilaian**, maupun ekspansi **Modul Ajar Utuh, Bank Soal, Jobsheet Praktikum, dan Slide Perkuliahan**) **WAJIB langsung dibuat, diperkaya, dan disimpan di dalam folder `KURIKULUM2026_REVISI/PERANGKAT_AJAR/` ini**.
> 2. **Larangan Menulis di Root `KURIKULUM2026_REVISI/`:** **JANGAN** lagi menaruh berkas `055_*` s.d. `100_*` (atau perangkat ajar lanjutan lainnya) di root `KURIKULUM2026_REVISI/`. Root folder dikhususkan hanya untuk dokumen induk Buku Kurikulum KPT-OBE (`000`–`054`, `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md`, dan template master).
> 3. **Status Saat Ini (7 November 2026):** Paket `055_*`–`100_*` telah tersedia: **46 MK × 5 = 230 berkas Markdown** untuk Core STI dan peminatan STA/STB/STC. Keberadaan berkas bukan pengesahan akademik. Paket `089`–`100` diperbaiki terhadap sumber dan perlu pendalaman serta validasi pengampu; `086`–`088` dan paket sebelumnya juga perlu audit substantif.
>    - **Generator pengayaan:** edit paket yang sudah ada langsung di folder ini; jangan membuat ulang `086`–`100` sebagai antrean kosong.
>    - **Pemeriksaan:** cek CPMK/sub-CPMK, hubungan asesmen, rubrik, rincian kegiatan dan sumber, selain verifikasi identitas otomatis. Selisih isi antardokumen induk harus dicatat dan divalidasi oleh koordinator.

---

## 1. Konvensi Penamaan Berkas Baku (5 Dokumen Utama per Mata Kuliah)

Setiap mata kuliah dibangkitkan dalam **1 paket utuh berisi 5 berkas Markdown (`.md`)** dengan pola:

```text
KURIKULUM2026_REVISI/PERANGKAT_AJAR/<NNN>_<SUB>_<JENIS>_<KODE-MK>_<NAMA_MK_KAPITAL>_<DDMMYYYY>.md
```

| Kode `<SUB>` | Jenis Dokumen (`<JENIS>`) | Cakupan Isi Wajib |
|:---:|---|---|
| `1` | `RPS` | Identitas resmi MK (Dok 005), Otorisasi, Pemetaan CPL (`CPL-01`..`CPL-14` Dok 003/004) — CPMK ABCD+Bloom — Sub-CPMK (Dok 007 & 043), Matriks Korelasi CPL×CPMK & Bobot 100%, Rencana 16 Pertemuan lengkap estimasi waktu SN-Dikti, Pustaka Utama/Pendukung, dan Boundary Guardrails (*In-Scope / Out-of-Scope / Handoff*). |
| `2` | `SAP` | Satuan Acara Perkuliahan mikro 16 pekan: kegiatan Pendahuluan — Inti — Penutup per pertemuan, metode aktif (*Case Method* / *Team-Based Project* IKU 7 $\ge 50\%$), media/perangkat lunak spesifik, tugas terstruktur & mandiri, serta aktivitas laboratorium (khusus MK `+P`). |
| `3` | `OUTLINE_MODUL` | Kerangka buku ajar/modul 14 bab materi (Pekan 1–7 & 9–15), sub-topik mendalam, studi kasus kontekstual *AI/Smart Systems Integrator*, latihan per bab, spesifikasi *prompt* ilustrasi diagram teknis (aset disimpan di `../assets/ilustrasi_modul/`), dan *hands-on lab* (khusus MK `+P`). |
| `4` | `RENCANA_EVALUASI_ASESMEN` | Arsitektur 4 titik evaluasi baku = **100%** (Tugas 1 Pekan 4, UTS Pekan 8, Tugas 2 Pekan 12, UAS Pekan 16), pemetaan instrumen terhadap CPMK (beberapa instrumen dapat mengukur CPMK yang sama), kisi-kisi (*blueprint*) soal/proyek, formula ketercapaian CPMK & kontribusi CPL (Dok 008), serta mekanisme remedial & CQI/PPEPP. |
| `5` | `RUBRIK_PENILAIAN` | Instrumen rubrik analitik 4 level kinerja (**Sangat Baik $\ge 81$, Baik $66\text{–}80$, Cukup $56\text{–}65$, Kurang $< 56$**) selaras klaster rubrik `K-1` s.d. `K-4` (Dok 018) untuk keempat instrumen asesmen + skala persepsi holistik (Dok 033). |

> **Catatan Ekstensi untuk Generator Bahan Ajar Turunan Lainnya:**
> Apabila terdapat generator terpisah untuk **Modul Ajar Penuh**, **Jobsheet Praktikum**, **Slide Presentasi**, atau **Bank Soal**, gunakan nomor urut mata kuliah `<NNN>` yang sama dengan sufiks lanjutan (`<NNN>_6_MODUL_AJAR_...`, `<NNN>_7_JOBSHEET_PRAKTIKUM_...`, `<NNN>_8_BANK_SOAL_...`) di dalam `KURIKULUM2026_REVISI/PERANGKAT_AJAR/` agar seluruh artefak satu mata kuliah mengelompok secara leksikografis.

---

> **Revisi STI-311:** Paket `065_1`–`065_5` diselaraskan ke HTML/CSS dasar–menengah, Flexbox lanjutan, Bootstrap/Tailwind dasar dan JavaScript dasar; tidak mencakup React/API. Buka [rancangan 043 STI-311](../043_STI-311_WEB_FRONT_END_DEVELOPMENT_DASAR_USULAN_07112026.md), [audit dampak dan status validasi](../LAPORAN_AUDIT_DAMPAK_STI-311.md), atau [tautan paket STI-311](../INDEX.md#semester-3). Revisi menunggu tinjauan/pengesahan RMK dan prodi. Ekspor non-Markdown dan pilot lama dapat belum selaras.
>
> **Paket di luar cakupan:** `113_1`–`113_5` untuk FST-714 Skripsi / Tugas Akhir tersedia terpisah, bukan bagian dari 46 MK Core STI/peminatan. [Buka kelima dokumen FST-714](../INDEX.md#paket-di-luar-cakupan-46-mk).

## 2. Daftar Nomor Urut Baku `<NNN>` (`055` s.d. `100` — 46 MK Core STI & Peminatan)

Seluruh atribut di bawah ini ditarik langsung dari **Single Source of Truth `../005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md`** (termasuk hasil restrukturisasi kode Semester 6–7 pada Dokumen 050 & 051). **Jangan mengubah nomor urut `<NNN>`, kode MK, SKS, tipe, atau semester.**

### A. Tahap 1–4: Semester 1 s.d. Semester 4 (`055`–`072` — 18 MK / 90 Berkas) — AKTIF DI FOLDER INI

| `<NNN>` | Sem | Kode MK | Nama Mata Kuliah Resmi (Dok 005) | SKS | Tipe | Prasyarat Resmi | Status Berkas |
|:---:|:---:|:---:|---|:---:|:---:|---|---|
| `055` | 1 | `STI-101` | Pengantar Sistem dan Teknologi Informasi | 2 | Teori | — | Tersedia (5 file, diperkaya) |
| `056` | 1 | `STI-102` | Kalkulus | 3 | Teori | — | Tersedia (5 file, diperkaya) |
| `057` | 1 | `STI-103` | Arsitektur dan Organisasi Sistem Teknologi Informasi | 3 | Teori | — | Tersedia (5 file, diperkaya) |
| `058` | 2 | `STI-204` | Matematika Diskrit dan Logika | 3 | Teori | `STI-103` | Tersedia (5 file, diperkaya) |
| `059` | 2 | `STI-205` | Aljabar Linear dan Matriks | 3 | Teori | `STI-102` | Tersedia (5 file, diperkaya) |
| `060` | 3 | `STI-306` | Analisis dan Perancangan Sistem Informasi | 3 | Teori | `STI-101`, `FST-207` | Tersedia (5 file) |
| `061` | 3 | `STI-307` | Sistem Cerdas | 2 | Teori | `STI-204`, `FST-204` | Tersedia (5 file) |
| `062` | 3 | `STI-308` | Desain & Prototyping UI/UX | 3 | +P | `FST-101` | Tersedia (5 file) |
| `063` | 3 | `STI-309` | Rekayasa Perangkat Lunak | 3 | Teori | `FST-203` | Tersedia (5 file) |
| `064` | 3 | `STI-310` | Sistem Operasi | 3 | Teori | `STI-103` | Tersedia (5 file) |
| `065` | 3 | `STI-311` | Pengembangan Web Front End | 3 | +P | `FST-102` | Tersedia (5 file) |
| `066` | 3 | `STI-312` | Jaringan Komputer | 3 | +P | `STI-103` | Tersedia (5 file) |
| `067` | 4 | `STI-413` | Pembelajaran Mesin | 3 | +P | `STI-205`, `STI-307` | Tersedia (5 file) |
| `068` | 4 | `STI-414` | Pengantar NLP & Temu Balik Informasi | 2 | +P | `STI-307` | Tersedia (5 file) |
| `069` | 4 | `STI-415` | Gudang Data & Kecerdasan Bisnis | 3 | +P | `FST-207` | Tersedia (5 file) |
| `070` | 4 | `STI-416` | Pengembangan Web Back End | 3 | +P | `FST-207`, `STI-311` | Tersedia (5 file) |
| `071` | 4 | `STI-417` | Komputasi Awan | 3 | Teori | `STI-312`, `STI-310` | Tersedia (5 file) |
| `072` | 4 | `STI-418` | Dasar Keamanan Informasi | 2 | Teori | `STI-312` | Tersedia (5 file) |

### B. Tahap 5: Semester 5 (`073`–`080` — 8 MK / 40 Berkas) — TERSEDIA

| `<NNN>` | Sem | Kode MK | Nama Mata Kuliah Resmi (Dok 005) | SKS | Tipe | Prasyarat Resmi | Rumpun / Jalur |
|:---:|:---:|:---:|---|:---:|:---:|---|---|
| `073` | 5 | `STI-519` | Keamanan Informasi Lanjut | 3 | Teori | `STI-418` | Core STI |
| `074` | 5 | `STI-520` | Penambangan Data & Visualisasi Data | 3 | +P | `STI-413`, `STI-415` | Core STI |
| `075` | 5 | `STI-521` | Internet untuk Segala (IoT) | 3 | +P | `STI-312`, `STI-310` | Core STI |
| `076` | 5 | `STI-522` | Pemrograman Aplikasi Mobile | 3 | +P | `STI-311`, `STI-416` | Core STI |
| `077` | 5 | `STI-523` | Manajemen Proyek TI | 3 | Teori | `STI-306`, `STI-309` | Core STI |
| `078` | 5 | `STA-501` | Sistem Pendukung Keputusan | 3 | +P | `STI-307` | P1: Integrated Smart Systems |
| `079` | 5 | `STB-501` | Keamanan Jaringan dan Forensik Digital | 3 | +P | `STI-312`, `STI-418` | P2: Cloud Infra & Cybersecurity |
| `080` | 5 | `STC-501` | Riset & Desain Pengalaman Pengguna (UX) | 3 | +P | `STI-308` | P3: Digital Platform Engineering |

### C. Tahap 6: Semester 6 (`081`–`085` — 5 MK / 25 Berkas) — TERSEDIA

| `<NNN>` | Sem | Kode MK | Nama Mata Kuliah Resmi (Dok 005) | SKS | Tipe | Prasyarat Resmi | Rumpun / Jalur |
|:---:|:---:|:---:|---|:---:|:---:|---|---|
| `081` | 6 | `STI-624` | Pembelajaran Mendalam & Jaringan Saraf | 3 | +P | `STI-413` | Core STI |
| `082` | 6 | `STI-625` | Rekayasa Platform Digital | 3 | +P | `STI-416` | Core STI |
| `083` | 6 | `STA-601` | Rekayasa Big Data dan Komputasi Terdistribusi | 3 | +P | `FST-207`, `STI-415` | P1: Integrated Smart Systems |
| `084` | 6 | `STB-601` | Arsitektur Cloud & DevOps | 3 | +P | `STI-417` | P2: Cloud Infra & Cybersecurity |
| `085` | 6 | `STC-601` | Rekayasa & Otomasi Proses Bisnis (BPA) | 3 | +P | `STI-306` | P3: Digital Platform Engineering |

### D. Tahap 7: Semester 7 (`086`–`100` — 15 MK / 75 Berkas) — TERSEDIA (PERLU VALIDASI SUBSTANTIF)

**Catatan QA:** Paket peminatan `089`–`100` telah direkonstruksi: CPMK penuh dari Dok 043, topik dari Dok 007, empat asesmen dan rubrik per MK. Dokumen tersebut masih berupa rancangan dan perlu pendalaman SAP, modul, kriteria rubrik dan validasi dosen; beberapa relasi Sub-CPMK di sumber 043 tidak sejalan dengan rumusan CPMK dan dipertahankan sambil menunggu rekonsiliasi. Core `086`–`088` belum diaudit menyeluruh; contohnya `087_4` memuat bobot efektif CPMK dan pembagian instrumen yang perlu diperiksa ulang, dan `086`/`088` masih menggunakan notasi 180M yang berbeda dari acuan 120 PT + 120 BM untuk 3 SKS +P. Lakukan audit juga pada paket semester terdahulu sebelum menganggapnya siap disahkan.

| `<NNN>` | Sem | Kode MK | Nama Mata Kuliah Resmi (Dok 005) | SKS | Tipe | Prasyarat Resmi | Rumpun / Jalur |
|:---:|:---:|:---:|---|:---:|:---:|---|---|
| `086` | 7 | `STI-726` | Integrasi Layanan Cerdas Berbasis AI | 3 | +P | `STI-413`, `STI-416` | Core STI |
| `087` | 7 | `STI-727` | Smart City & Pemerintahan Digital | 2 | Teori | `STI-521` | Core STI |
| `088` | 7 | `STI-728` | Inovasi Teknologi dan Startup Digital | 3 | +P | `STI-625`, `MKU-204` | Core STI |
| `089` | 7 | `STA-602` | Sistem Agen Cerdas | 3 | +P | `STI-307` | P1: Integrated Smart Systems |
| `090` | 7 | `STA-701` | MLOps dan Alur Pipa AI | 3 | +P | `STI-413`, `STI-726` | P1: Integrated Smart Systems |
| `091` | 7 | `STA-702` | AI Percakapan dan Asisten Cerdas | 3 | +P | `STI-413`, `STI-416` | P1: Integrated Smart Systems |
| `092` | 7 | `STA-703` | Pengawasan Cerdas dan Analitika IoT | 3 | +P | `STI-624`, `STI-521` | P1: Integrated Smart Systems |
| `093` | 7 | `STB-602` | Manajemen Risiko Keamanan Siber | 3 | Teori | `STI-418` | P2: Cloud Infra & Cybersecurity |
| `094` | 7 | `STB-701` | Tata Kelola & Kepatuhan TI (COBIT 2019) | 3 | Teori | `STI-101` | P2: Cloud Infra & Cybersecurity |
| `095` | 7 | `STB-702` | Manajemen Layanan TI (ITIL 4) | 3 | Teori | `STI-101` | P2: Cloud Infra & Cybersecurity |
| `096` | 7 | `STB-703` | Arsitektur Enterprise (TOGAF) | 3 | Teori | `STI-306` | P2: Cloud Infra & Cybersecurity |
| `097` | 7 | `STC-602` | Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) | 3 | +P | `STI-416` | P3: Digital Platform Engineering |
| `098` | 7 | `STC-701` | Media Imersif & Pengembangan XR | 3 | +P | `STI-311` | P3: Digital Platform Engineering |
| `099` | 7 | `STC-702` | Arsitektur SaaS & Multi-Tenansi | 3 | +P | `STI-416` | P3: Digital Platform Engineering |
| `100` | 7 | `STC-703` | Manajemen Produk Digital & Praktik Agile | 3 | Teori | `STI-523` | P3: Digital Platform Engineering |

> **Cadangan Penomoran `101+` (MK Wajib Fakultas `FST-*` & MKWU `MKU-*`):**
> Jika di tahap berikutnya diperlukan pembangkitan perangkat ajar untuk 13 MK FSTI (`FST-101` s.d. `FST-714`) atau 8 MKWU (`MKU-101` s.d. `MKU-508`) sebagaimana tercantum di Dokumen 007, gunakan nomor urut mulai **`101` ke atas** tetap di dalam folder `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`.

---

## 3. Aturan Kepatuhan Ground Truth & Anti-Discrepancy (Wajib Dipatuhi Generator)

1. **Hierarki Sumber Kebenaran:**
   - **Identitas MK (Kode, Nama ID/EN, SKS, Tipe, Semester, Prasyarat):** `../005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md` adalah **rujukan tertinggi**. Apabila terdapat perbedaan kode/semester pada teks naratif lama di Dok 043 akibat pertukaran Semester 6–7 (Dok 050 & 051), **ikuti Dok 005** secara mutlak.
   - **Kode Baku 14 CPL:** Gunakan `CPL-01` s.d. `CPL-14` (padanan alias kategori lama `S1`, `KU1–KU3`, `P1–P4`, `KK1–KK6` merujuk `../004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md` Bagian 0 & `../003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md`).
   - **Silabus 16 Pekan, CPMK ABCD, Sub-CPMK, & Guardrails:** Rujuk `../007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md`, `../037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md`, dan `../043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md`.
2. **Standar Estimasi Waktu Belajar per Minggu & Bobot 4x Asesmen (= 100%):**
   - **2 SKS Teori:** `TM 100', PT 120', BM 120'` | Bobot: **Tugas 1 (20%) · UTS (30%) · Tugas 2 (20%) · UAS (30%)**
   - **3 SKS Teori:** `TM 150', PT 180', BM 180'` | Bobot: **Tugas 1 (20%) · UTS (30%) · Tugas 2 (20%) · UAS (30%)**
   - **2 SKS +P (1T + 1P):** `TM 50', Prak 170', PT 60', BM 60'` | Bobot: **Tugas 1 (20%) · UTS (25%) · Tugas 2 (25%) · UAS (30%)**
   - **3 SKS +P (2T + 1P):** `TM 100', Prak 170', PT 120', BM 120'` | Bobot: **Tugas 1 (20%) · UTS (25%) · Tugas 2 (25%) · UAS (30%)**
3. **Pencegahan Error Nomenklatur yang Diaudit Otomatis oleh `_tools/`:**
   - Selalu tulis lengkap **`STI-204 Matematika Diskrit dan Logika`** (jangan memotong kata `dan Logika`).
   - Selalu tulis **`STI-103 Arsitektur dan Organisasi Sistem Teknologi Informasi`** untuk K2026.
   - Pastikan **`STI-519` adalah `Keamanan Informasi Lanjut` (Sem 5, 3 SKS Teori)** dan **`STI-624` adalah `Pembelajaran Mendalam & Jaringan Saraf` (Sem 6, 3 SKS +P)**; **`STI-625` adalah `Rekayasa Platform Digital` (Sem 6, 3 SKS +P)**; **`STI-726` adalah `Integrasi Layanan Cerdas Berbasis AI` (Sem 7, 3 SKS +P)**; **`STI-727` adalah `Smart City & Pemerintahan Digital` (Sem 7, 2 SKS Teori)**.
   - Path relatif ke aset gambar/diagram dari berkas di folder ini wajib memakai awalan `../assets/ilustrasi_modul/<nama_berkas>.png`.
4. **Gerbang Verifikasi Wajib Sebelum Commit / PR:**
   Setiap kali selesai menambah atau memperkaya berkas di `PERANGKAT_AJAR/`, jalankan ketiga skrip audit dari folder `KURIKULUM2026_REVISI/`:
   ```bash
   python3 -B _tools/verify_all_mk_aligned_with_005.py
   python3 -B _tools/verify_zero_discrepancy.py
   python3 -B _tools/check_all_md_alignment_with_005.py
   ```
   Ketiga skrip memeriksa keselarasan tertentu dengan Dok 005; hasil lulus tidak membuktikan kelengkapan atau mutu akademik. Periksa juga rumusan CPMK lengkap, pemetaan asesmen dan total bobot, referensi silang, substansi dan validasi pengampu.
