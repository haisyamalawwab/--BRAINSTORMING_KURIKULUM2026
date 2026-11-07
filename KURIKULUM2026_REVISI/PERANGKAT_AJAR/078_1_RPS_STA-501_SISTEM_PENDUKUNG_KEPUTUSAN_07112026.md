# 078_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STA-501 — Sistem Pendukung Keputusan

**Identitas:** `STA-501` Sistem Pendukung Keputusan · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-307` · PL-1 · PEO-1, PEO-3 · IRM R · Rubrik K-3.

## 1. Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tanggal dan tanda tangan: **diisi pada pengesahan**. Beban per minggu: **TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit**; PT = penugasan terstruktur, BM = belajar mandiri.

## 2. CPL yang dibebankan

| CPL | Rumusan Dok 003 | IRM |
| --- | --- | --- |
| `CPL-06` (`P2`) | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | R |
| `CPL-09` (`KK1`) | Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri. | R |
| `CPL-10` (`KK2`) | Mampu merekayasa pipeline data skala besar (*Data Engineering*), membangun model machine learning/deep learning, serta menerapkan MLOps untuk solusi analitik dan visualisasi data bisnis. | R |

## 3. CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD (Dok 043) | Bloom | CPL (Dok 004) |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **menerapkan** metode pengambilan keputusan multi-kriteria klasik (SAW, WP, AHP) (*B*) pada kasus pemilihan alternatif bisnis (*C*) dengan uji konsistensi rasio $CR \le 0.1$ (*D*). | C3 | CPL-06 (P2), CPL-09 (KK1) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengimplementasikan** metode perankingan tingkat lanjut (TOPSIS, PROMETHEE, Fuzzy AHP) (*B*) dalam kode program Python (*C*) secara tepat (*D*). | C4 | CPL-09 (KK1), CPL-10 (KK2) |
| `CPMK-3` | Mahasiswa (*A*) mampu **membangun** aplikasi berbasis web Decision Support Systems interaktif (*B*) dengan visualisasi perbandingan alternatif dan analisis sensitivitas (*C*) secara terintegrasi (*D*). | C6 | CPL-09 (KK1), CPL-10 (KK2) |

| Kode | Kompetensi spesifik Dok 043 | CPMK menurut Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Mengimplementasikan metode pengambilan keputusan multikriteria SAW dan WP. | `CPMK-1` | C3 |
| `Sub-CPMK-1.2` | Mengimplementasikan metode AHP dan TOPSIS beserta uji konsistensi (CR). | `CPMK-1` | C3 |
| `Sub-CPMK-2.1` | Menerapkan metode PROMETHEE dan Fuzzy AHP pada perankingan alternatif. | `CPMK-2` | C4 |
| `Sub-CPMK-2.2` | Menganalisis hasil keputusan multikriteria melalui analisis sensitivitas. | `CPMK-2` | C4 |
| `Sub-CPMK-3.1` | Membangun aplikasi web DSS interaktif untuk pengambilan keputusan. | `CPMK-3` | C6 |
| `Sub-CPMK-3.2` | Mengevaluasi keandalan sistem pendukung keputusan yang dibangun. | `CPMK-3` | C6 |

## 4. Analisis pembelajaran dan korelasi penilaian

Alur belajar: pengenalan dan pemodelan → penerapan dan analisis → integrasi serta evaluasi. Penilaian bersifat kumulatif; pengalokasian nilai CPMK berikut merupakan rancangan operasional, bukan bobot resmi CPL prodi.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-06 (P2), CPL-09 (KK1) | 20% | 12.5% | — | — | 32.5% |
| CPMK-2 | CPL-09 (KK1), CPL-10 (KK2) | — | 12.5% | 25% | — | 37.5% |
| CPMK-3 | CPL-09 (KK1), CPL-10 (KK2) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

CPL yang didukung bersama oleh sebuah CPMK menggunakan **bukti yang sama**; nilai tidak dijumlahkan ulang sebagai persentase nilai akhir. Cara menghitung capaian masing-masing CPL dijelaskan di dokumen 4.

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 5. Deskripsi dan rencana 16 pertemuan

Mata kuliah mengembangkan kompetensi sesuai CPMK melalui kasus di atas dengan Python, pandas, NumPy dan Streamlit atau aplikasi setara. Teknik penilaian dan indikator spesifik tiap instrumen ada pada dokumen 4 dan 5.

| Mg | Sub-CPMK terkait | Kemampuan / indikator | Materi | Metode | Alokasi belajar per minggu | Asesmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sub-CPMK-1.1 | Mampu menguraikan konsep dasar DSS, fase Simon, dan arsitektur DSS (C2) | Pengantar Decision Support Systems, Karakteristik Masalah Terstruktur/Semi | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 2 | Sub-CPMK-1.1 | Mampu memodelkan kriteria, bobot, dan normalisasi matriks keputusan (C3) | Multi-Criteria Decision Making (MCDM): Penentuan Kriteria & Skala Likert | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 3 | Sub-CPMK-1.1 | Mampu menerapkan metode Simple Additive Weighting (SAW) & WP (C3) | Metode Klasik: Simple Additive Weighting (SAW) & Weighted Product (WP) | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 4 | Sub-CPMK-1.2 | Menghitung bobot AHP dan CR ≤ 0,1 untuk memvalidasi preferensi. | AHP dan uji consistency ratio | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 (20%) |
| 5 | Sub-CPMK-1.2 | Mampu menguji rasio konsistensi CR pada AHP dan revisi preferensi (C4) | AHP: Consistency Ratio (CR <= 0.1) & Hierarki Keputusan Multi-Level | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 6 | Sub-CPMK-1.2 | Mampu menerapkan metode TOPSIS: Solusi Ideal Positif & Negatif (C4) | Metode TOPSIS: Matriks Ternormalisasi Berbobot & Jarak Euclidean | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 7 | Sub-CPMK-2.1 | Mampu menerapkan metode PROMETHEE dan fungsi preferensi kriteria (C4) | Metode Outranking: PROMETHEE I (Partial) & PROMETHEE II (Complete) | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 8 | Sub-CPMK-1.2, Sub-CPMK-2.1 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Perhitungan Algoritma MCDM (AHP, TOPSIS, PROMETHEE) | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS (25%) |
| 9 | Sub-CPMK-2.1 | Mampu mengintegrasikan logika fuzzy pada pembobotan kriteria (Fuzzy AHP) (C4) | Fuzzy MCDM: Triangular Fuzzy Numbers (TFN), Fuzzy AHP & Fuzzy TOPSIS | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 10 | Sub-CPMK-2.2 | Mampu melakukan Sensitivity Analysis terhadap perubahan bobot kriteria (C4) | Analisis Sensitivitas: Menguji Ketahanan Ranking terhadap Fluktuasi Bobot | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 11 | Sub-CPMK-2.2 | Mampu menerapkan Group Decision Support Systems (GDSS) konsensus Borda (C4) | Group Decision Support Systems (GDSS): Metode Borda & Copeland | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 12 | Sub-CPMK-3.1 | Mampu merancang arsitektur backend REST API mesin kalkulasi DSS (C4) | Backend Engine DSS: API Endpoint Perhitungan & Database Alternatif | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 (25%) |
| 13 | Sub-CPMK-3.1 | Mampu merancang antarmuka visualisasi dashboard DSS interaktif (C6) | Front-End Dashboard DSS: Radar Chart, Bar Chart Komparasi Alternatif | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 14 | Sub-CPMK-3.1 | Mampu mengintegrasikan model prediksi Machine Learning ke dalam DSS (C6) | Hybrid Intelligent DSS: Integrasi Prediksi ML & Rekomendasi Keputusan | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 15 | Sub-CPMK-3.2 | Mampu menguji sistem DSS end-to-end pada studi kasus keputusan industri (C6) | PjBL DSS Studio: Pengujian Sistem Terpadu pada Masalah Nyata Mitra | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 16 | Sub-CPMK-3.1, Sub-CPMK-3.2 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Aplikasi Web Decision Support Systems Terpadu | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS (30%) |

## 6. Ringkasan instrumen

- **Tugas 1 (20%, pekan 4): Pemodelan dan keputusan klasik** — Tetapkan alternatif, benefit/cost, bobot; hitung SAW, WP dan AHP termasuk CR. Bukti: Matriks keputusan, perhitungan manual, kode dan interpretasi. Cek: normalisasi, ketepatan ranking dan CR AHP ≤ 0,1 atau revisi.
- **UTS (25%, pekan 8): Ujian metode multikriteria** — Selesaikan kasus AHP dan TOPSIS/PROMETHEE serta jelaskan perbedaan hasil dan asumsi. Bukti: Jawaban individual, tabel perhitungan dan hasil program. Cek: ketepatan langkah AHP dan metode lanjutan, validasi hasil.
- **Tugas 2 (25%, pekan 12): Sensitivitas dan model lanjut** — Implementasikan PROMETHEE atau Fuzzy AHP dan variasikan bobot untuk mengukur perubahan ranking. Bukti: Notebook, skenario bobot, grafik sensitivitas dan temuan. Cek: metode dapat direproduksi, stabilitas ranking dan keterbatasan.
- **UAS (30%, pekan 16): Purwarupa SPK interaktif** — Bangun aplikasi masukan alternatif, hitung ranking, bandingkan hasil dan tampilkan sensitivitas. Bukti: Kode aplikasi, data contoh, hasil uji dan demo keputusan. Cek: ketepatan algoritma, validasi masukan, transparansi dan uji end-to-end.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS01` *Foundations of IS*, `BK-IS13` *Data Analytics and BI*. Klasifikasi pembina menurut Dok 004: primer BK-IS13, sekunder BK-IS02; BK-IS01 disebut Dok 043 tetapi tidak mencantumkan MK ini pada matriks Dok 004.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur SPK, Metode Multi-Criteria Decision Making (AHP, TOPSIS, SAW, Promethee), Sensitivitas Model, Integrasi DSS dengan Dashboard Eksekutif.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding machine learning neural network, pembuatan pipeline ETL data warehouse dari nol, konfigurasi server database fisik.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menguasai perancangan sistem pendukung keputusan multikriteria; menyerahkan sistem agen otonom ke `STA-602`.

**Catatan rekonsiliasi:** Dok 043 memasukkan TOPSIS dalam Sub-CPMK-1.2 tetapi pada rumusan CPMK-2; disaggregasi UTS dilakukan per butir AHP dan TOPSIS. AHP saja memiliki uji CR, bukan TOPSIS. Integrasi prediksi menggunakan keluaran yang telah tersedia, tanpa melatih neural network. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** Seleksi lokasi layanan masyarakat dengan kriteria biaya, akses dan manfaat; bobot serta data merupakan skenario sintetis.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: Saaty, The Analytic Hierarchy Process (1980); dokumentasi NumPy dan Streamlit.
