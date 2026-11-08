# 097_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STC-602 — Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech)

**Identitas:** `STC-602` Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) · Semester 7 · 3 SKS (+P) · Prasyarat `STI-416` · PL PL-3 · PEO PEO-1, PEO-2 · IRM M.

## Identitas dan pengesahan

Prodi S1 SISTEKIN FSTI UWG. Koordinator, dosen dan tanggal pengesahan diisi oleh program studi. Beban mingguan: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. PT = tugas terstruktur; BM = belajar mandiri.

## CPL dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| CPL-08 (P4) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | M |
| CPL-13 (KK5) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | M |

## CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD Dok 043 | Bloom | CPL |
| --- | --- | --- | --- |
| CPMK-1 | Mahasiswa (*A*) mampu **menerapkan** arsitektur sistem pembayaran digital (*B*) dengan integrasi Payment Gateway API (Midtrans/Xendit) dan buku besar akuntansi ganda (*Double-Entry Ledger*) (*C*) secara aman dan konsisten (*D*). | C4 | `CPL-08` (`P4`), `CPL-13` (`KK5`) |
| CPMK-2 | Mahasiswa (*A*) mampu **mengimplementasikan** standar interoperabilitas pembelajaran digital (SCORM 1.2/2004 dan xAPI Tin-Can) (*B*) pada Learning Management System (LMS) (*C*) dengan pelacakan aktivitas belajar yang presisi (*D*). | C4 | `CPL-08` (`P4`), `CPL-13` (`KK5`) |
| CPMK-3 | Mahasiswa (*A*) mampu **membangun** platform aplikasi industri vertikal terpadu (*B*) dengan penanganan transaksi idempotensi (*Idempotency Key*) dan kepatuhan regulasi industri (*C*) secara andal (*D*). | C6 | `CPL-13` (`KK5`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Menganalisis kebutuhan dan alur transaksi aplikasi FinTech (e-wallet, AML/risk rule). | CPMK-1 | C4 |
| Sub-CPMK-1.2 | Menganalisis kebutuhan aplikasi EdTech (LMS, SIS, proctoring). | CPMK-1 | C4 |
| Sub-CPMK-2.1 | Mengintegrasikan payment gateway pada aplikasi FinTech. | CPMK-2 | C4 |
| Sub-CPMK-2.2 | Merancang alur pembayaran dan pencatatan transaksi yang aman. | CPMK-2 | C4 |
| Sub-CPMK-3.1 | Membangun aplikasi industri vertikal (FinTech/EdTech) yang siap pakai. | CPMK-3 | C6 |
| Sub-CPMK-3.2 | Mengevaluasi kepatuhan dan keamanan aplikasi industri vertikal. | CPMK-3 | C6 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-08` (`P4`), `CPL-13` (`KK5`) | 20% | 25% | — | — | 45% |
| CPMK-2 | `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | — | 25% | — | 25% |
| CPMK-3 | `CPL-13` (`KK5`) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan karakteristik aplikasi vertikal dan Domain-Driven Design (C2) | Pengantar Vertical Industry Apps, Karakteristik Spesifik Domain, DDD | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 2 | Mampu menganalisis ekosistem pembayaran digital dan regulasi Bank Indonesia (C4) | Domain FinTech: Payment Gateway, E-Wallet, Regulasi SNAP Open Banking | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 3 | Mampu mengintegrasikan Payment Gateway API (Midtrans/Xendit Sandbox) (C3) | Payment Integration: Snap Checkout, Webhook Notification, Status Inquiry | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 4 | Mampu menerapkan mekanisme Idempotency Key dan distributed locking (C4) | Keamanan Transaksi: Idempotency Keys, Mencegah Double-Spending, Race Conditions | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 20% |
| 5 | Mampu merancang arsitektur Buku Besar Digital (Double-Entry Bookkeeping) (C4) | Financial Ledger Engine: Akun Debet/Kredit, Immutability, Audit Trail | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 6 | Mampu menganalisis kepatuhan standar keamanan data kartu PCI-DSS (C4) | FinTech Security: Tokenisasi Kartu Kredit, Enkripsi Payload, Standar PCI-DSS | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 7 | Mampu merancang deteksi dini anomali transaksi mencurigakan (Fraud) (C4) | Fraud Detection Dasar: Rule-Based Velocity Checks & Geolocation Mismatch | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Integrasi Payment Gateway API & Double-Entry Ledger | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS 25% |
| 9 | Mampu menguraikan ekosistem teknologi pendidikan (EdTech) dan LMS (C2) | Domain EdTech: Arsitektur LMS Modern, Kursus Daring, Gamifikasi Pembelajaran | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 10 | Mampu menganalisis standar paket pembelajaran SCORM 1.2 / 2004 (C4) | Standar Interoperabilitas EdTech: Paket SCORM, Manifest XML, CMI Data Model | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 11 | Mampu mengimplementasikan protokol xAPI (Experience API / Tin Can) (C4) | Standar xAPI: Desain Statement (Actor, Verb, Object), Learning Record Store (LRS) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 12 | Mampu merancang arsitektur Computer-Based Testing (CBT) anti-curang (C4) | Arsitektur CBT: Timer Sinkronisasi, Randomisasi Soal, Anti-Cheating Guard | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 25% |
| 13 | Mampu menganalisis metrik keterlibatan siswa via Learning Analytics (C4) | Learning Analytics: Retention Rate, Completion Rate, Quiz Heatmaps | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 14 | Mampu mengintegrasikan streaming video adaptif HLS untuk materi belajar (C4) | Media Streaming: HLS Video Segmentation, DRM Protection, Progress Tracking | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 15 | Mampu membangun platform industri vertikal terpadu (FinTech Billing / EdTech) (C6) | PjBL Vertical Apps Studio: Pembangunan Solusi Terpadu Spesifik Domain | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Platform Aplikasi Industri Vertikal (FinTech/EdTech) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Rancang alur payment gateway sandbox dengan pengamanan transaksi. Bukti: diagram transaksi, request dan threat notes |
| UTS | 8 | 25% | CPMK-1 | Implementasikan payment sandbox dan double-entry ledger serta uji idempotensi. Bukti: kode individual, log transaksi dan hasil uji |
| Tugas 2 | 12 | 25% | CPMK-2 | Implementasikan SCORM/xAPI pada lingkungan LMS contoh. Bukti: paket pembelajaran, statement xAPI dan log uji |
| UAS | 16 | 30% | CPMK-3 | Bangun solusi vertikal dengan transaksi idempotent dan evaluasi keamanan. Bukti: repo, demo, hasil uji dan batas kepatuhan |

## Pustaka utama dan pendukung

[Stripe API](https://docs.stripe.com/api), [ADL xAPI](https://adlnet.gov/projects/xapi/), dan ketentuan BI/OJK terkini untuk domain kasus (verifikasi dosen).

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS12` *Web & Mobile*, `BK-IT04` *Platform Technologies*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Sistem Industri Vertikal, Layanan FinTech (Sistem Pembayaran, Payment Gateway, Fraud Detection Dasar, Regulasi BI/OJK), Layanan EdTech (LMS, Learning Analytics), Keamanan Transaksi Finansial.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang audit kepatuhan perbankan legal murni, pembuatan game edukasi 3D mendalam, setup hardware server fisik data center.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun sistem aplikasi industri bernilai ekonomi tinggi yang patuh pada standar regulasi sektoral.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
