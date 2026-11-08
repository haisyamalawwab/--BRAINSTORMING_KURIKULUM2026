# 099_2 — SATUAN ACARA PERKULIAHAN 16 PERTEMUAN

## STC-702 — Arsitektur SaaS & Multi-Tenansi

**Identitas:** `STC-702` Arsitektur SaaS & Multi-Tenansi · Semester 7 · 3 SKS (+P) · Prasyarat `STI-416` · PL PL-3 · PEO PEO-1, PEO-2 · IRM M.

## Panduan

Alokasi minggu: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. Dosen menyiapkan contoh kasus dan bahan uji berizin. Asesmen formatif tidak menambah bobot nilai.

### Pertemuan 1 — Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation

**Kemampuan:** Mampu menguraikan model bisnis SaaS dan tantangan arsitektur Multi-Tenancy (C2).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 2 — Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table

**Kemampuan:** Mampu membandingkan 3 pola isolasi data multi-tenant (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 3 — Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable

**Kemampuan:** Mampu mengimplementasikan Row-Level Security (RLS) pada PostgreSQL (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 4 — Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping

**Kemampuan:** Mampu mengonfigurasi resolusi tenant via Subdomain (*tenant.app.com*) (C3).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Tugas 1 (20%, CPMK-1):** Rancang isolasi tenant dan uji akses lintas tenant pada data dummy. Bukti: skema, kebijakan RLS dan hasil negative test.

### Pertemuan 5 — Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration

**Kemampuan:** Mampu merancang otentikasi multi-tenant dan Single Sign-On (SSO / SAML) (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 6 — Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing

**Kemampuan:** Mampu merancang skema paket langganan SaaS (Free, Pro, Enterprise) (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 7 — Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle

**Kemampuan:** Mampu mengintegrasikan Subscription Engine via Stripe Billing API (C3).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 8 — Ujian Koding Terjadwal Multi-Tenant RLS Database & Integrasi Stripe Billing

**Kemampuan:** EVALUASI TENGAH SEMESTER (UTS).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Ujian Koding Terjadwal Multi-Tenant RLS Database & Integrasi Stripe Billing dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **UTS (25%, CPMK-2):** Bangun langganan dengan Stripe test mode dan penanganan webhook. Bukti: kode, event sandbox dan bukti transaksi.

### Pertemuan 9 — Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers

**Kemampuan:** Mampu menangani Stripe Webhooks untuk aktivasi/pembatalan akun otomatis (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 10 — Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records

**Kemampuan:** Mampu mengimplementasikan Metered Billing berbasis konsumsi sumber daya (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 11 — Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime

**Kemampuan:** Mampu mengonfigurasi Feature Toggling berbasis paket langganan (C3).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 12 — Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS

**Kemampuan:** Mampu merancang arsitektur Micro-Frontends via Module Federation (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Tugas 2 (25%, CPMK-3):** Implementasikan feature flag per plan dan micro-frontends. Bukti: kode, konfigurasi dan hasil uji akses.

### Pertemuan 13 — Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling

**Kemampuan:** Mampu mencegah Noisy Neighbor Problem via Rate Limiting per tenant (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 14 — Self-Service Onboarding: Automated Tenant Database Provisioning Wizard

**Kemampuan:** Mampu merancang wizard onboarding mandiri instan tenant baru (C4).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Self-Service Onboarding: Automated Tenant Database Provisioning Wizard dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 15 — PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu

**Kemampuan:** Mampu membangun platform SaaS multi-tenant terpadu siap produksi (C6).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **Formatif:** catatan analisis dan latihan, tanpa bobot sumatif.

### Pertemuan 16 — Sidang Demonstrasi Produk Platform SaaS Multi-Tenant Live & Ujian Portofolio

**Kemampuan:** EVALUASI AKHIR SEMESTER (UAS).

- **Pendahuluan:** kaitkan topik dengan CPMK dan prasyarat; jelaskan batas etik.
- **Inti:** kaji konsep dan contoh; mahasiswa bekerja pada kasus, menerapkan atau mengevaluasi Sidang Demonstrasi Produk Platform SaaS Multi-Tenant Live & Ujian Portofolio dan memeriksa hasil bersama dosen.
- **Penutup:** jelaskan keputusan, batas asumsi dan terima umpan balik.
- **PT/BM:** dokumentasikan langkah, sumber dan hasil; berikan satu contoh berbeda serta refleksi keterbatasan.
- **UAS (30%, CPMK-3):** Integrasikan SaaS dan lakukan uji isolasi, akses plan, billing dan pemulihan. Bukti: repo, demo, hasil uji keamanan dan dokumentasi.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS12` *Web & Mobile*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Software-as-a-Service (SaaS), Pola Multi-Tenancy (Database per Tenant, Shared Database Shared Schema), Tenant Isolation, Sistem Penagihan Berlangganan (Stripe API), Skalabilitas Horisontal Layanan SaaS.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding driver perangkat keras, audit pajak korporat, perancangan sensor IoT fisik.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan platform SaaS multi-penyewa yang siap dipasarkan secara komersial dan skalabel.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Gunakan akun pembayaran sandbox, dan uji negatif antar-tenant; hasil uji tidak membuktikan isolasi mutlak. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
