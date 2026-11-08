# 099_3 — OUTLINE MODUL PEMBELAJARAN

## STC-702 — Arsitektur SaaS & Multi-Tenansi

**Identitas:** `STC-702` Arsitektur SaaS & Multi-Tenansi · Semester 7 · 3 SKS (+P) · Prasyarat `STI-416` · PL PL-3 · PEO PEO-1, PEO-2 · IRM M.

## Peta 14 bab

Materi pekan 1–7 dan 9–15 menjadi bab; pekan 8 dan 16 untuk evaluasi. Gunakan rujukan dan guardrails di akhir.

### Bab 1 — Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation (pekan 1)

- **Capaian:** Mampu menguraikan model bisnis SaaS dan tantangan arsitektur Multi-Tenancy (C2).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Pengantar SaaS Architecture, Model Bisnis Langganan, Tenant Isolation, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 2 — Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table (pekan 2)

- **Capaian:** Mampu membandingkan 3 pola isolasi data multi-tenant (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Pola Isolasi Data: Database-per-Tenant, Schema-per-Tenant, Shared-Table, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 3 — Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable (pekan 3)

- **Capaian:** Mampu mengimplementasikan Row-Level Security (RLS) pada PostgreSQL (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Multi-Tenant RLS: Kebijakan RLS PostgreSQL, Current Tenant Session Variable, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 4 — Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping (pekan 4)

- **Capaian:** Mampu mengonfigurasi resolusi tenant via Subdomain (*tenant.app.com*) (C3).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Tenant Routing: Subdomain Extraction, Custom Domain CNAME Mapping, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 5 — Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration (pekan 5)

- **Capaian:** Mampu merancang otentikasi multi-tenant dan Single Sign-On (SSO / SAML) (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Tenant Identity: Multi-Tenant JWT Claims, Organization SSO Integration, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 6 — Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing (pekan 6)

- **Capaian:** Mampu merancang skema paket langganan SaaS (Free, Pro, Enterprise) (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Model Langganan: Pricing Tiers, Quota Limits, Per-Seat vs Usage Billing, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 7 — Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle (pekan 7)

- **Capaian:** Mampu mengintegrasikan Subscription Engine via Stripe Billing API (C3).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Stripe API Integration: Customers, Payment Methods, Subscriptions Lifecycle, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 8 — Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers (pekan 9)

- **Capaian:** Mampu menangani Stripe Webhooks untuk aktivasi/pembatalan akun otomatis (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Payment Webhooks: Invoice Payment Succeeded, Subscription Deleted Handlers, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 9 — Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records (pekan 10)

- **Capaian:** Mampu mengimplementasikan Metered Billing berbasis konsumsi sumber daya (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Usage-Based Billing: Event Ingestion, Metering Aggregation, Usage Records, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 10 — Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime (pekan 11)

- **Capaian:** Mampu mengonfigurasi Feature Toggling berbasis paket langganan (C3).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Feature Flags: Dynamic Feature Toggling per Tenant Plan di Runtime, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 11 — Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS (pekan 12)

- **Capaian:** Mampu merancang arsitektur Micro-Frontends via Module Federation (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Micro-Frontends: Webpack/Vite Module Federation untuk Multi-Team SaaS, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 12 — Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling (pekan 13)

- **Capaian:** Mampu mencegah Noisy Neighbor Problem via Rate Limiting per tenant (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Tenant Fair-Use: Redis Rate Limiter per Tenant, Resource Throttling, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 13 — Self-Service Onboarding: Automated Tenant Database Provisioning Wizard (pekan 14)

- **Capaian:** Mampu merancang wizard onboarding mandiri instan tenant baru (C4).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan Self-Service Onboarding: Automated Tenant Database Provisioning Wizard; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait Self-Service Onboarding: Automated Tenant Database Provisioning Wizard, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang Self-Service Onboarding: Automated Tenant Database Provisioning Wizard, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

### Bab 14 — PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu (pekan 15)

- **Capaian:** Mampu membangun platform SaaS multi-tenant terpadu siap produksi (C6).
- **Substansi:** konsep dasar, komponen dan asumsi; tahapan penerapan PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu; cara memverifikasi hasil dan keterbatasannya.
- **Studi kasus & latihan:** pilih kasus sesuai CPMK; identifikasi input dan tujuan, terapkan konsep, lalu bandingkan hasil pada skenario berbeda.
- **Praktikum:** buat artefak atau analisis terkait PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu, tuliskan langkah, hasil dan alasan; terapkan batas dan keamanan pada bagian akhir.
- **Prompt ilustrasi:** diagram edukasi berlabel Indonesia tentang PjBL SaaS Studio: Pembangunan Solusi Platform SaaS Terpadu, menunjukkan input, proses, output dan titik verifikasi; tanpa data pribadi.

## Pustaka utama dan pendukung

[PostgreSQL Row Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [Stripe Subscriptions](https://docs.stripe.com/billing/subscriptions/overview), dan dokumentasi stack yang digunakan.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS12` *Web & Mobile*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Software-as-a-Service (SaaS), Pola Multi-Tenancy (Database per Tenant, Shared Database Shared Schema), Tenant Isolation, Sistem Penagihan Berlangganan (Stripe API), Skalabilitas Horisontal Layanan SaaS.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding driver perangkat keras, audit pajak korporat, perancangan sensor IoT fisik.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan platform SaaS multi-penyewa yang siap dipasarkan secara komersial dan skalabel.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Gunakan akun pembayaran sandbox, dan uji negatif antar-tenant; hasil uji tidak membuktikan isolasi mutlak. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
