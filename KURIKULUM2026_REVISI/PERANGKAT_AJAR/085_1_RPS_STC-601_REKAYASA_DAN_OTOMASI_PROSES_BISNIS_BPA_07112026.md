# 085_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE

## STC-601 — Rekayasa & Otomasi Proses Bisnis (BPA) (*Business Process Engineering & Automation (BPA)*)

**Identitas:** `STC-601` Rekayasa & Otomasi Proses Bisnis (BPA) · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-306` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-4 (adaptasi BPA).

## 1. Identitas, pembelajaran dan otorisasi

Program Studi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tahun akademik, tanggal dan tanda tangan **diisi pada pengesahan**. Beban mingguan: **TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit**; PT adalah tugas terstruktur, BM belajar mandiri. Waktu ujian dan praktik dapat diatur sesuai kalender akademik tanpa mengubah beban semester.

## 2. CPL yang dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| `CPL-06` (`P2`) | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | M |
| `CPL-08` (`P4`) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | M |
| `CPL-13` (`KK5`) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | M |

## 3. Rumusan CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD menurut Dok 043 | Bloom | CPL terkait |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **menganalisis** performa proses bisnis dan mendeteksi kesenjangan (*Conformance Checking*) (*B*) menggunakan teknik Process Mining (*C*) secara empiris (*D*). | C4 | `CPL-06` (`P2`) |
| `CPMK-2` | Mahasiswa (*A*) mampu **merancang dan mengeksekusi** alur kerja otomatis (*B*) menggunakan Workflow Engine (Camunda BPMN 8 / Temporal) dan Decision Model and Notation (DMN) (*C*) secara terstandarisasi (*D*). | C6 | `CPL-06` (`P2`), `CPL-08` (`P4`), `CPL-13` (`KK5`) |
| `CPMK-3` | Mahasiswa (*A*) mampu **mengembangkan** bot Robotic Process Automation (RPA) (*B*) menggunakan Python RPA / UiPath (*C*) untuk otomasi tugas repetitif dan ekstraksi dokumen OCR (*D*). | C6 | `CPL-13` (`KK5`) |

| Sub-CPMK Dok 043 | Kompetensi spesifik | CPMK di Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Memodelkan proses bisnis lanjutan menggunakan BPMN 2.0. | `CPMK-1` | C4 |
| `Sub-CPMK-1.2` | Menganalisis peluang otomasi pada proses bisnis organisasi. | `CPMK-1` | C4 |
| `Sub-CPMK-2.1` | Mengimplementasikan otomasi proses bisnis menggunakan RPA (UiPath). | `CPMK-2` | C6 |
| `Sub-CPMK-2.2` | Memodelkan dan mengeksekusi BPM menggunakan engine Camunda. | `CPMK-2` | C6 |
| `Sub-CPMK-3.1` | Mengintegrasikan sistem melalui ESB/API dan middleware. | `CPMK-3` | C6 |
| `Sub-CPMK-3.2` | Membangun solusi Business Process Automation end-to-end. | `CPMK-3` | C6 |

## 4. Analisis pembelajaran dan matriks korelasi

Alur: fondasi dan analisis → implementasi terarah → integrasi, pengujian dan refleksi. Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UAS sama-sama mengukur CPMK-3.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-06` (`P2`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-06` (`P2`), `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-13` (`KK5`) | — | — | 25% | 30% | 55% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Bobot dalam tabel adalah alokasi terhadap nilai mata kuliah; satu CPMK dapat mendukung beberapa CPL dan tidak boleh dihitung sebagai nilai MK berulang. Lihat dokumen 4 untuk agregasi resmi CPL dan skor diagnostik.

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 5. Deskripsi dan rencana pembelajaran 16 pekan

Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Perangkat: Camunda 8 atau engine BPMN/DMN setara, PM4Py, UiPath/Python RPA dan OCR menggunakan dokumen sintetis. Kegiatan, indikator dan bukti tiap pekan dijabarkan di SAP dan outline modul; asesmen formatif tidak menjadi komponen nilai tambahan.

| Pekan | Sub-CPMK terkait | Topik | Aktivitas / indikator yang dapat diamati | Bukti | Metode | Estimasi belajar | Asesmen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Sub-CPMK-1.1` | BPM lifecycle dan baseline proses | Gambarkan proses as-is, pemangku kepentingan dan titik persetujuan pada kasus kampus. | BPMN as-is dan daftar aktivitas | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 2 | `Sub-CPMK-1.1` | BPMN, log peristiwa dan kualitas data | Buat event log case ID, aktivitas dan timestamp; periksa data hilang dan urutan. | CSV sintetis dan laporan kualitas log | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 3 | `Sub-CPMK-1.2` | Process discovery dan bottleneck | Temukan model proses dari log menggunakan process mining, hitung waktu tunggu dan throughput. | Model hasil discovery dan tabel KPI | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 4 | `Sub-CPMK-1.2` | Conformance checking dan Tugas 1 | Bandingkan model as-is dengan jejak aktual, identifikasi deviasi dan rekomendasi perbaikan. | Laporan kesenjangan, bukti log dan Tugas 1 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 1 (20%) |
| 5 | `Sub-CPMK-2.2` | Workflow engine dan BPMN eksekutabel | Ubah model to-be menjadi BPMN yang dapat dijalankan; atur user/service task. | BPMN dan bukti instans workflow | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 6 | `Sub-CPMK-2.2` | DMN dan aturan keputusan | Rancang tabel keputusan dengan hit policy, batas nilai dan test case konflik. | Tabel DMN dan hasil uji aturan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 7 | `Sub-CPMK-2.2` | Service task dan penanganan error | Integrasikan workflow ke API mock; uji timeout, kesalahan dan jalur manual. | Konfigurasi workflow, payload dan log | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 8 | `Sub-CPMK-2.2` | UTS: workflow dan DMN | Bangun dan jalankan workflow berikut aturan keputusan; uji kasus normal dan gagal. | BPMN, DMN dan bukti uji individual | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UTS (25%) |
| 9 | `Sub-CPMK-2.1` | RPA attended dan unattended | Pilih aktivitas cocok untuk bot, tetapkan batas otomasi dan izin akun latihan. | Matriks kelayakan RPA dan peta exception | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 10 | `Sub-CPMK-2.1` | Bot input formulir | Otomatiskan input pada formulir latihan lokal dengan verifikasi hasil dan timeout. | Script/bot, log dan hasil uji dummy | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 11 | `Sub-CPMK-2.1` | OCR dan kualitas ekstraksi | Ekstrak field dokumen sintetis dengan OCR; bandingkan hasil dengan kebenaran dasar. | Dokumen contoh, hasil OCR dan error report | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 12 | `Sub-CPMK-2.1`, `Sub-CPMK-3.2` | Bot RPA dan Tugas 2 | Gabungkan OCR dengan bot dan mekanisme penanganan kesalahan; serahkan milestone. | Bot, laporan uji dan rekaman Tugas 2 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 2 (25%) |
| 13 | `Sub-CPMK-3.1` | Integrasi workflow, bot dan API | Hubungkan service task pada mock ke bot; korelasikan case ID dengan log. | Diagram integrasi dan hasil uji jalur gagal | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 14 | `Sub-CPMK-3.2` | Pengukuran efisiensi dan akses | Bandingkan baseline dan proses baru menggunakan data simulasi; cek akses berdasarkan peran. | Tabel KPI, asumsi dan pemeriksaan akses | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 15 | `Sub-CPMK-3.2` | Uji end-to-end dan dokumentasi | Uji kasus normal, exception dan pemulihan; siapkan runbook dan demo. | Test matrix, runbook dan catatan batas | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 16 | `Sub-CPMK-2.2`, `Sub-CPMK-3.2` | UAS: solusi BPA terpadu | Demonstrasikan workflow, keputusan dan bot, lalu pertahankan hasil secara individual. | Model, bot, log, laporan dan presentasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UAS (30%) |

## 6. Ringkasan empat instrumen

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Event log, model, perhitungan KPI dan rekomendasi |
| UTS | 8 | 25% | `CPMK-2` | BPMN, DMN, bukti eksekusi dan jawaban individual |
| Tugas 2 | 12 | 25% | `CPMK-3` | Bot, data dummy, hasil OCR dan log pengujian |
| UAS | 16 | 30% | `CPMK-3` | Diagram, workflow, bot, KPI, bukti uji dan demo tim |

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS09` *Business Process Management*, `BK-IS07` *Systems Analysis and Design*. **Pembina Dok 004:** BK-IS09 primer dan BK-IS07 sekunder; Dok 037 juga menyebut BK-IT11.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Rekayasa Proses Bisnis Enterprise, Simulasi Alur Kerja Bisnis (BPMN), Robotic Process Automation (RPA dasar: UiPath / Camunda), Integrasi Alur Kerja Antar-Departemen, Pengukuran Efisiensi Proses.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding antarmuka visual grafis aplikasi dari nol, audit pembukuan keuangan korporat, perancangan firewall jaringan.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Mengotomatisasi proses bisnis organisasi; menyerahkan integrasi platform vertikal ke `STC-602`.

Batas tambahan Dok 037: tidak mengembangkan full-stack aplikasi dari nol atau audit COBIT.

**Catatan sumber:** Dok 037 memberi empat CPMK serta P2/KK4/KK5; Dok 043 memberi tiga CPMK dan P2/P4/KK5, selaras pembebanan Dok 004. Dok 043 menempatkan RPA pada Sub-CPMK-2.1 dan integrasi pada Sub-CPMK-3.1 meski rumusan CPMK-3 berfokus RPA; bukti dinilai menurut rumusan CPMK. OCR menggunakan data sintetis, bukan identitas nyata. Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UAS sama-sama mengukur CPMK-3. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** Dumas et al., *Fundamentals of Business Process Management*, 2nd ed. (2018); OMG BPMN 2.0.2 dan DMN; dokumentasi Camunda dan PM4Py.
