# 099_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STC-702 — Arsitektur SaaS & Multi-Tenansi

**Identitas:** `STC-702` Arsitektur SaaS & Multi-Tenansi · Semester 7 · 3 SKS (+P) · Prasyarat `STI-416` · PL PL-3 · PEO PEO-1, PEO-2 · IRM M.

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
| CPMK-1 | Mahasiswa (*A*) mampu **merancang** strategi isolasi data multi-tenant (Shared Database with Row-Level Security vs Database-per-Tenant) (*B*) pada PostgreSQL (*C*) dengan jaminan isolasi data mutlak (*D*). | C4 | `CPL-08` (`P4`) |
| CPMK-2 | Mahasiswa (*A*) mampu **membangun** mesin penagihan berlangganan (*Subscription Engine*) otomatis (*B*) dengan integrasi Stripe API dan webhook (*C*) secara transaksional (*D*). | C6 | `CPL-13` (`KK5`) |
| CPMK-3 | Mahasiswa (*A*) mampu **mengimplementasikan** arsitektur Micro-Frontends dan *Feature Toggling* (*B*) pada platform SaaS (*C*) untuk aktivasi fitur dinamis per paket langganan (*D*). | C4 | `CPL-08` (`P4`), `CPL-13` (`KK5`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Merancang arsitektur SaaS multi-tenant dengan isolasi antar tenant. | CPMK-1 | C4 |
| Sub-CPMK-1.2 | Menganalisis skema sharing database pada arsitektur multi-tenant. | CPMK-1 | C4 |
| Sub-CPMK-2.1 | Mengimplementasikan proses on-boarding tenant dan manajemen kuota. | CPMK-2 | C6 |
| Sub-CPMK-2.2 | Menerapkan mekanisme monetisasi dan metering (plan, quota) pada SaaS. | CPMK-2 | C6 |
| Sub-CPMK-3.1 | Membangun aplikasi SaaS dengan arsitektur multi-tenant yang andal. | CPMK-3 | C4 |
| Sub-CPMK-3.2 | Mengevaluasi skalabilitas dan keamanan isolasi antar tenant. | CPMK-3 | C4 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | — | 25% | 30% | 55% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan model bisnis SaaS dan tantangan arsitektur Multi-Tenancy (C2) | Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 2 | Mampu membandingkan 3 pola isolasi data multi-tenant (C4) | Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 3 | Mampu mengimplementasikan Row-Level Security (RLS) pada PostgreSQL (C4) | Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 4 | Mampu mengonfigurasi resolusi tenant via Subdomain (*tenant.app.com*) (C3) | Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 20% |
| 5 | Mampu merancang otentikasi multi-tenant dan Single Sign-On (SSO / SAML) (C4) | Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 6 | Mampu merancang skema paket langganan SaaS (Free, Pro, Enterprise) (C4) | Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 7 | Mampu mengintegrasikan Subscription Engine via Stripe Billing API (C3) | Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Multi-Tenant RLS Database & Integrasi Stripe Billing | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS 25% |
| 9 | Mampu menangani Stripe Webhooks untuk aktivasi/pembatalan akun otomatis (C4) | Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 10 | Mampu mengimplementasikan Metered Billing berbasis konsumsi sumber daya (C4) | Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 11 | Mampu mengonfigurasi Feature Toggling berbasis paket langganan (C3) | Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 12 | Mampu merancang arsitektur Micro-Frontends via Module Federation (C4) | Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 25% |
| 13 | Mampu mencegah Noisy Neighbor Problem via Rate Limiting per tenant (C4) | Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 14 | Mampu merancang wizard onboarding mandiri instan tenant baru (C4) | Self-Service Onboarding: Automated Tenant Database Provisioning Wizard | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 15 | Mampu membangun platform SaaS multi-tenant terpadu siap produksi (C6) | PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Platform SaaS Multi-Tenant Live & Ujian Portofolio | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Rancang isolasi tenant dan uji akses lintas tenant pada data dummy. Bukti: skema, kebijakan RLS dan hasil negative test |
| UTS | 8 | 25% | CPMK-2 | Bangun langganan dengan Stripe test mode dan penanganan webhook. Bukti: kode, event sandbox dan bukti transaksi |
| Tugas 2 | 12 | 25% | CPMK-3 | Implementasikan feature flag per plan dan micro-frontends. Bukti: kode, konfigurasi dan hasil uji akses |
| UAS | 16 | 30% | CPMK-3 | Integrasikan SaaS dan lakukan uji isolasi, akses plan, billing dan pemulihan. Bukti: repo, demo, hasil uji keamanan dan dokumentasi |

## Pustaka utama dan pendukung

[PostgreSQL Row Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [Stripe Subscriptions](https://docs.stripe.com/billing/subscriptions/overview), dan dokumentasi stack yang digunakan.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS12` *Web & Mobile*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Software-as-a-Service (SaaS), Pola Multi-Tenancy (Database per Tenant, Shared Database Shared Schema), Tenant Isolation, Sistem Penagihan Berlangganan (Stripe API), Skalabilitas Horisontal Layanan SaaS.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding driver perangkat keras, audit pajak korporat, perancangan sensor IoT fisik.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan platform SaaS multi-penyewa yang siap dipasarkan secara komersial dan skalabel.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Gunakan akun pembayaran sandbox, dan uji negatif antar-tenant; hasil uji tidak membuktikan isolasi mutlak. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
