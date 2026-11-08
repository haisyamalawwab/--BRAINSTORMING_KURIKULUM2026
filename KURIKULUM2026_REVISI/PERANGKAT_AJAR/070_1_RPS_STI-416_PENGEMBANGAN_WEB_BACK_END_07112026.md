# 070_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-416 — PENGEMBANGAN WEB BACK END (*Web Back End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.4.RPS-STI416`  
**Tanggal Penyusunan:** 07 November 2026  

---

> **Audit prasyarat STI-311:** HTML/CSS/Flexbox dan JavaScript dasar tersedia; HTTP/REST, Fetch/Axios, asinkron dan framework JS bukan capaian STI-311 yang baru. Bekali semantik HTTP/REST pada pertemuan 1 STI-416 dan uji endpoint dengan curl/Postman; penempatan pengayaan integrasi klien menunggu keputusan prodi. Lihat `../LAPORAN_AUDIT_DAMPAK_STI-311.md`.

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, 043, & RPS Pilot STI-416) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Pengembangan Web Back End / *Web Back End Development* |
| **Kode Mata Kuliah** | `STI-416` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Rekayasa Perangkat Lunak & Platform Digital (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS (`+P`)** (`T = 2, P = 1`) — Tatap Muka `2×50' = 100'`, Praktikum Terbimbing `1×170' = 170'`, Penugasan Terstruktur `2×60' = 120'`, Belajar Mandiri `2×60' = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 4 (Genap) — Tahap Penguatan Rekayasa Layanan Sisi Server (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `FST-207` Basis Data, `STI-311` Pengembangan Web Front End |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Bersinergi dengan `STI-417` Komputasi Awan & `STI-418` Dasar Keamanan Informasi; menyuplai kontrak API ke `STI-522` Pemrograman Aplikasi Mobile, `STI-625` Rekayasa Platform Digital, `STI-726` Integrasi Layanan Cerdas Berbasis AI, `STC-602` Rekayasa Sistem E-Commerce dan Fintech, & `STC-702` Proyek Konsultansi Transformasi Digital |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-08` (`P4` = **35%**) dan `CPL-13` (`KK5` = **65%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 2 (`K-2`)** — Rekayasa Perangkat Lunak, Data & Sistem Enterprise (Bobot MK `+P`: Tugas 1 `20%` · UTS `25%` · Tugas 2 `25%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Rekayasa Perangkat Lunak & Platform Digital |
| **Koordinator RMK** | Dr. Istiadi, S.T., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-08`** (`P4`) | Pengetahuan | Menguasai metode pengembangan perangkat lunak, rekayasa kebutuhan, pemrograman berorientasi objek, serta teknologi pengembangan aplikasi web dan perangkat bergerak. | **R** (*Reinforce*) | **35%** |
| **`CPL-13`** (`KK5`) | Keterampilan Khusus | Mampu merancang, mengembangkan, menguji, dan memelihara perangkat lunak aplikasi lintas platform (*web, mobile, IoT*) yang fungsional, aman, dan berorientasi pengguna. | **R** (*Reinforce*) | **65%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menerapkan arsitektur sisi server (*Server-Side Architecture*) dan membangun RESTful API modular** (*B*) menggunakan *framework back-end* modern (*Node.js/Express* atau *Python FastAPI*) (*C*) sesuai standar protokol HTTP (*D*). | **C3** (*Apply*) | `CPL-08` (`P4`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **mengintegrasikan aplikasi *back-end* dengan basis data relasional dan NoSQL menggunakan ORM/ODM** (*B*) untuk operasi CRUD transaksional dan *query optimization* (*C*) yang aman (*D*). | **C3** (*Apply*) | `CPL-13` (`KK5`) | **UTS — Pekan 8 (25%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **menganalisis dan mengimplementasikan mekanisme autentikasi serta otorisasi API** (*B*) menggunakan **JWT** (*JSON Web Token*), **RBAC** (*Role-Based Access Control*), *password hashing* (**Bcrypt**), serta pengelolaan *session/caching* dasar (**Redis**) (*C*) secara tangguh (*D*). | **C4** (*Analyze*) | `CPL-08` (`P4`) & `CPL-13` (`KK5`) | **Tugas 2 — Pekan 12 (25%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **membangun layanan *back-end* produksi lengkap dokumentasi API otomatis (*Swagger/OpenAPI*)** serta melakukan ***deployment* aplikasi terkontainerisasi (*Docker*)** (*B*) ke lingkungan *cloud* (*C*) yang terdokumentasi dan siap diakses (*D*). | **C6** (*Create*) | `CPL-13` (`KK5`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Membangun **RESTful API** modular berarsitektur berlapis (*Router–Controller–Service*) dengan *Node.js/Express* atau *Python FastAPI*. | `CPMK-1` | **C3** | Mg 1–2 |
| **`Sub-CPMK-1.2`** | Mengelola rute dinamis, *middleware*, penanganan galat terpusat, dan validasi/sanitasi input (*Zod / Pydantic*). | `CPMK-1` | **C3** | Mg 3–4 |
| **`Sub-CPMK-2.1`** | Mengintegrasikan basis data relasional (PostgreSQL) dan NoSQL (MongoDB) menggunakan **ORM/ODM** (*Prisma / SQLAlchemy / Mongoose*). | `CPMK-2` | **C3** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Menerapkan operasi **CRUD transaksional (ACID)**, paginasi kursor/offset, dan *query optimization* bebas *N+1* & *SQL Injection*. | `CPMK-2` | **C3** | Mg 6–7 |
| **`Sub-CPMK-3.1`** | Mengimplementasikan autentikasi dan otorisasi API dengan **JWT**, **RBAC**, dan *password hashing* **Bcrypt**. | `CPMK-3` | **C4** | Mg 9–10 |
| **`Sub-CPMK-3.2`** | Mengelola *session/refresh token*, *rate limiting*, *CORS/Helmet*, dan *caching* dasar dengan **Redis**. | `CPMK-3` | **C4** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Menyusun dokumentasi API interaktif otomatis (**Swagger / OpenAPI 3.1**) serta pengujian *endpoint* otomatis (*Jest/Supertest* atau *Pytest*). | `CPMK-4` | **C6** | Mg 13–14 |
| **`Sub-CPMK-4.2`** | Melakukan pengemasan kontainer (**Docker**) dan *deployment* aplikasi *back-end* ke lingkungan *cloud* lengkap *health-check*. | `CPMK-4` | **C6** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Layanan Back-End Produksi, Pengujian API, Dokumentasi Swagger/OpenAPI, & Cloud Docker Deployment (C6) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: OpenAPI 3.1 / Swagger UI & Automated API Tests | Sub-CPMK-4.2: Dockerfile, Env Secrets, & Cloud Deploy)
      │
[CPMK-3: Keamanan Layanan API (JWT, RBAC, Bcrypt, Rate Limit) & Caching Dasar Redis (C4) — Mg 9–12 (Tugas 2 25%)]
      ▲  (Sub-CPMK-3.1: Stateless Auth JWT Access/Refresh, RBAC, Bcrypt | Sub-CPMK-3.2: Redis Cache-Aside, CORS, Helmet, Rate Limit)
      │
[CPMK-2: Integrasi Persistensi Relasional & NoSQL via ORM/ODM, Transaksi ACID, & Query Optimization (C3) — Mg 5–8 (UTS 25%)]
      ▲  (Sub-CPMK-2.1: PostgreSQL ORM + MongoDB ODM & Schema Migrations | Sub-CPMK-2.2: ACID Transactions, Pagination, Anti-N+1)
      │
[CPMK-1: Arsitektur Sisi Server, Protokol HTTP, RESTful API Modular, Middleware, & Sanitasi Input (C3) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Express/FastAPI Layered Architecture & HTTP Semantics | Sub-CPMK-1.2: Middleware, Error Handler, Zod/Pydantic)
      ▲
[Fondasi Prasyarat: FST-207 Basis Data + STI-311 Pengembangan Web Front End (HTML/CSS/Flexbox dan JavaScript dasar; konsumsi Fetch/Axios tidak diasumsikan)]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-08`** (`P4`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-08` = 35%** *(20%+15%)* |
| **`CPL-13`** (`KK5`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **25%** | — | — | **25%** | **`CPL-13` = 65%** *(25%+10%+30%)* |
| **`CPL-08`** (`15%`) & **`CPL-13`** (`10%`) | **`CPMK-3`** | `Sub-CPMK-3.1` (`P4`: 15%), `Sub-CPMK-3.2` (`KK5`: 10%) | — | — | **25%** | — | **25%** | *(Terdisagregasi 15% `P4` + 10% `KK5`)* |
| **`CPL-13`** (`KK5`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | *(ke `CPL-13`)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **25%** | **25%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-2` Dok 018; Target Dok 004 `70%`):** `Tugas 1 (20% — Case-Based Modular REST API) + Tugas 2 (25% — Case-Based Secure Auth RBAC & Redis Caching Audit) + UAS (30% — Project-Based Cloud-Deployed Production API)` = **75%** *(melampaui target 70% Dokumen 004)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-416 Pengembangan Web Back End` (3 SKS `+P`) membekali mahasiswa dengan keahlian rekayasa perangkat lunak sisi server berstandar industri untuk melayani aplikasi web dan perangkat bergerak modern. Mahasiswa membangun **RESTful API** berarsitektur berlapis (*Controller–Service–Repository*) menggunakan **Node.js/Express (TypeScript)** atau **Python FastAPI**, menerapkan validasi kontrak input (*Zod/Pydantic*) dan *centralized error middleware*, mengintegrasikan basis data relasional (**PostgreSQL**) serta NoSQL (**MongoDB**) melalui **ORM/ODM** dengan transaksi **ACID** dan optimasi kueri bebas masalah *N+1*, mengamankan *endpoint* dengan **Bcrypt**, **JWT (*Access & Refresh Token*)**, **RBAC**, *rate limiting*, serta akselerasi **Redis Caching**, hingga melengkapi pengujian otomatis, dokumentasi interaktif **Swagger/OpenAPI**, dan *deployment* kontainer **Docker** ke lingkungan *cloud*.

* **🟢 IN-SCOPE (Wajib Diajarkan):** Semantik protokol HTTP, arsitektur berlapis **RESTful API** (*Express / FastAPI*), *middleware* & sanitasi input, **ORM/ODM** (PostgreSQL + MongoDB), transaksi ACID & optimasi kueri, **JWT + RBAC + Bcrypt**, *rate limiting* & **Redis** *cache-aside*, pengujian otomatis *endpoint*, **Swagger/OpenAPI**, serta *deployment* kontainer **Docker** tunggal ke *cloud*.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. Dilarang mengulang desain tata letak visual HTML/CSS yang merupakan lingkup **`STI-311 Pengembangan Web Front End`**; manajemen *state* komponen tidak diasumsikan telah diajarkan pada STI-311.
  2. Dilarang membahas orkestrasi multi-klaster **Kubernetes** & *Infrastructure as Code* Terraform (ranah **`STB-601 Arsitektur Cloud & DevOps`**).
  3. Dilarang membahas arsitektur *Microservices Event-Driven* berskala besar dengan **Apache Kafka** dan *Service Mesh* (ranah **`STI-625 Rekayasa Platform Digital`**).
* **🔄 HANDOFF ANCHOR:** Menyerahkan kemampuan membangun *RESTful API* aman dan terdokumentasi *OpenAPI* untuk dikonsumsi oleh aplikasi seluler pada **`STI-522 Pemrograman Aplikasi Mobile`**, didekomposisi ke layanan terdistribusi pada **`STI-625 Rekayasa Platform Digital`**, dan diintegrasikan dengan model AI pada **`STI-726 Integrasi Layanan Cerdas Berbasis AI`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS12` (*System Design & Implementation*), `BK-IT04` (*Web Systems & Technologies*), & `BK-IT11` (*Platform-Based Development*).

**Pustaka Utama:**
1. Lauret, A. (2019). *The Design of Web APIs*. Manning Publications.
2. Herron, D. (2020). *Node.js Web Development* (5th ed.). Packt Publishing. / Lubanovic, B. (2023). *FastAPI: Modern Python Web Development*. O'Reilly Media.
3. Richardson, L., Amundsen, M., & Ruby, S. (2013). *RESTful Web APIs*. O'Reilly Media.

**Pustaka Pendukung:**
4. OWASP Foundation. (2023). *OWASP API Security Top 10 (2023 Edition)*.
5. Dokumentasi Resmi Express.js / FastAPI, Prisma ORM / SQLAlchemy 2.0, Redis, OpenAPI Specification 3.1, & Docker Engine.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Teori + Praktikum) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Bagian I):** Memahami arsitektur sisi server (*Event Loop / Async I/O*), semantik protokol **HTTP/1.1 & HTTP/2**, serta kematangan **RESTful API** (*Richardson Maturity Model*) [C2→C3] | 1.1.1 Ketepatan merancang penamaan *resource URI* kata benda jamak, pemilihan metode HTTP idempoten (`GET, PUT, DELETE` vs `POST, PATCH`), dan kode status HTTP (`200, 201, 204, 400, 401, 403, 404, 409, 422, 500`). | **Kriteria:** Kontrak URI & kode status HTTP mematuhi kaidah REST murni (tanpa kata kerja di URL seperti `/getUsers`!).<br>**Teknik:** Inspeksi lalu lintas HTTP dengan `curl`/Bruno/Postman di lab. | **Interactive Lecture** `[TM: 100']`<br>**Praktikum Lab 1:** Penyiapan Proyek *Node.js/Express* (atau *Python FastAPI*), *Async/Await*, & Eksperimen Semantik HTTP `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kontrak belajar, panduan instalasi runtime, Git, & Bruno/Postman di LMS Edlink. | Arsitektur Sisi Server, *Non-Blocking Async I/O*, Semantik Protokol **HTTP**, & Prinsip Desain **RESTful API** `[1] Bab 1–3; [2]` | — |
| **2** | **`Sub-CPMK-1.1` (Bagian II):** Membangun struktur proyek **RESTful API Modular** berarsitektur berlapis (*Router – Controller – Service – Data Access*) [C3] | 1.1.2 Ketepatan memisahkan logika rute HTTP, pengendali permintaan/respons, dan aturan bisnis (*Service Layer*) sehingga mudah diuji dan dirawat. | **Kriteria:** Tidak ada logika bisnis bersarang langsung di dalam berkas definisi rute.<br>**Teknik:** Code review struktur direktori modular di laboratorium. | **Live Architecture Lecture** `[TM: 100']`<br>**Praktikum Lab 2:** Konstruksi **RESTful API Modular** (*Layered Architecture*) & Konfigurasi Variabel Lingkungan (`.env`) `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Unduh templat *boilerplate* arsitektur berlapis di LMS Edlink. | Pola *Separation of Concerns* (*Router–Controller–Service*), Konfigurasi Twelve-Factor App (`.env`), & Amplop Respons JSON Konsisten `[1] Bab 4; [2]` | — |
| **3** | **`Sub-CPMK-1.2` (Bagian I):** Mengelola parameter rute (*path, query, headers*), rantai **Middleware**, pencatatan log terstruktur, & *Centralized Error Handling* [C3] | 1.2.1 Ketepatan membangun *custom middleware* (pencatat waktu eksekusi/`request-id`) dan pengendali galat global berformat standar (*Problem Details* tanpa membocorkan *stack trace* internal ke klien!). | **Kriteria:** Seluruh eksepsi tak-terduga tertangkap rapi oleh *global error handler* dengan kode status tepat.<br>**Teknik:** Uji injeksi permintaan rusak pada API di lab. | **Problem-Based Lecture** `[TM: 100']`<br>**Praktikum Lab 3:** Siklus Hidup **Middleware**, *Structured Logging*, & *Global Error Handling* `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi spesifikasi **Tugas 1 (RTM-1)** di LMS Edlink. | Siklus Permintaan **Middleware**, *Request Context*, Penanganan Eksepsi Terpusat (RFC 7807), & *Structured Logging* `[1] Bab 5; [2]` | — |
| **4** | **`Sub-CPMK-1.2` (Bagian II):** Menerapkan **Validasi Skema & Sanitasi Input** (*Zod / Joi* atau *Pydantic*) serta pengelolaan unggah berkas aman (*Multipart/Form-Data*) [C3]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.2 Ketepatan menolak *payload* JSON tidak valid (`422 Unprocessable Entity`), mencegah *Mass Assignment*, dan membatasi tipe MIME serta ukuran unggahan berkas. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-2`)**.<br>**Teknik:** Pengujian Otomatis Koleksi *Endpoint* & Verifikasi Kode **Tugas 1 (`CPMK-1`)** di Lab. | **Validation Lecture & Uji Tugas 1** `[TM: 100']`<br>**Praktikum Lab 4:** Validasi Kontrak Input (*Zod / Pydantic*), Sanitasi, & Verifikasi **Tugas 1 (`CPMK-1`)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan repositori Git **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Validasi Skema Deklaratif (*DTO / Zod / Pydantic*), Pencegahan *Mass Assignment*, & Validasi Unggahan Berkas `[2]; [4] API3` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1` (Bagian I):** Mengintegrasikan basis data relasional (**PostgreSQL**) menggunakan **ORM** (*Prisma / Drizzle* atau *SQLAlchemy 2.0*) beserta *Schema Migrations* & *Connection Pooling* [C3] | 2.1.1 Ketepatan memetakan relasi `1:1`, `1:N`, dan `M:N` pada skema ORM, mengelola riwayat *database migration* terkendali versi, serta melakukan *seeding* data awal. | **Kriteria:** Skema basis data terbangun murni melalui *migration script* reproduksibel (bukan klik manual di GUI!).<br>**Teknik:** Praktikum integrasi ORM PostgreSQL & CRUD relasional. | **Interactive Lecture ORM** `[TM: 100']`<br>**Praktikum Lab 5:** Integrasi **PostgreSQL via ORM**, *Versioned Migrations*, & Relasi Entitas `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis pemetaan relasi & *Connection Pool* di LMS Edlink. | Pola *Object-Relational Mapping* (**ORM**), *Versioned Schema Migrations*, *Connection Pooling*, & Pencegahan *SQL Injection* via *Parameterized Queries* `[2]` | — |
| **6** | **`Sub-CPMK-2.1` (Bagian II) & `2.2` (Bagian I):** Integrasi basis data dokumen **NoSQL (MongoDB via ODM)** & penerapan **Transaksi ACID** multi-tabel [C3] | 2.1.2 Ketepatan memilih kapan data disimpan di PostgreSQL (transaksi finansial/inventori ketat) vs MongoDB (log aktivitas/katalog atribut fleksibel).<br>2.2.1 Ketepatan membungkus operasi pemotongan stok + pembuatan pesanan dalam **Database Transaction (`COMMIT / ROLLBACK`)** yang atomik! | **Kriteria:** Jika langkah ke-2 gagal di tengah jalan, perubahan langkah ke-1 wajib ter-*rollback* 100%.<br>**Teknik:** Uji simulasi kegagalan transaksi konkurensi di laboratorium. | **Case-Based Persistence Lecture** `[TM: 100']`<br>**Praktikum Lab 6:** Integrasi **MongoDB ODM** & Pengujian **Transaksi ACID (`Rollback` Otomatis)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Studi kasus *Polyglot Persistence* di LMS Edlink. | Integrasi **NoSQL (MongoDB ODM)**, *Polyglot Persistence*, **Transaksi ACID**, & Penanganan *Race Condition / Optimistic Locking* `[2]; [5]` | — |
| **7** | **`Sub-CPMK-2.2` (Bagian II):** *Query Optimization* Sisi Aplikasi: Eliminasi Masalah **N+1 Query**, Indeks Komposit, Penyaringan Dinamis, & **Pagination** (*Offset vs Cursor*) + Klinik UTS [C3] | 2.2.2 Ketepatan mendeteksi dan memberantas **N+1 Query Problem** menggunakan *eager loading / batch join*, serta mengimplementasikan paginasi lengkap metadata (`page, limit, total, hasNext`). | **Kriteria:** Pengambilan 50 pesanan beserta itemnya hanya memicu 1–2 kueri SQL (bukan 51 kueri!).<br>**Teknik:** Inspeksi *Query Log* ORM & simulasi ujian praktik **UTS**. | **Performance Tuning & Klinik UTS** `[TM: 100']`<br>**Praktikum Lab 7:** Eliminasi **N+1 Query**, *Cursor/Offset Pagination*, & Simulasi UTS `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Latihan mandiri simulasi *live coding* UTS di LMS Edlink. | Deteksi **N+1 Query Problem**, Indeks Basis Data untuk API, Pencarian/Penyortiran Aman, & **Cursor vs Offset Pagination** `[1] Bab 6; [5]` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C3]** | Keberhasilan membangun secara mandiri layanan **RESTful API Terintegrasi Basis Data via ORM/ODM** lengkap migrasi skema, operasi **CRUD Transaksional ACID**, paginasi/pencarian aman, serta optimasi kueri bebas *N+1* dan *SQL/NoSQL Injection*. | **Kriteria:** **Rubrik Analitik UTS Praktik (`K-2`)**.<br>**Teknik:** Ujian Praktik *Live Coding* Back-End & Basis Data Terawasi di Laboratorium. | **Ujian Praktik Integrasi Layanan Back-End & Persistensi Data di Lab**<br>`[150 menit]` | Pengarsipan kode ujian & nilai `CPMK-2` pada portal OBE. | Materi RESTful API Modular, **ORM/ODM**, **Transaksi ACID**, Paginasi, & *Query Optimization* (Pekan 1–7) | **25%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1` (Bagian I):** Menganalisis keamanan penyimpanan kredensial (**Password Hashing Bcrypt / Argon2**) & mekanisme autentikasi *stateless* **JWT (*JSON Web Token*)** [C4] | 3.1.1 Ketepatan membedakan *encoding* (Base64 pada payload JWT yang **bisa dibaca siapa saja!**), *encryption*, dan *one-way salted hashing* (**Bcrypt/Argon2**).<br>3.1.2 Ketepatan mengimplementasikan alur `/auth/register`, `/auth/login`, *Access Token* berumur pendek, & *Refresh Token* aman (`HttpOnly Cookie`). | **Kriteria:** Kata sandi tidak pernah tersimpan *plaintext*/MD5 dan tanda tangan JWT diverifikasi ketat.<br>**Teknik:** Praktikum implementasi autentikasi Bcrypt + JWT di lab. | **Security-Focused Lecture** `[TM: 100']`<br>**Praktikum Lab 8:** *Password Hashing* (**Bcrypt**) & Siklus Autentikasi **JWT (*Access + Refresh Token*)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis anatomi `Header.Payload.Signature` JWT di LMS Edlink. | Kriptografi Kata Sandi (**Bcrypt/Argon2**), *Session-Based vs Token-Based Auth*, Anatomi **JWT**, & Rotasi *Refresh Token* `[4] API2` | — |
| **10** | **`Sub-CPMK-3.1` (Bagian II):** Mengimplementasikan otorisasi **RBAC (*Role-Based Access Control*)** & pencegahan kerentanan kritis **BOLA / IDOR** (*OWASP API1*) [C4] | 3.1.3 Ketepatan membangun *Auth & Role Guard Middleware* (`admin, staff, customer`) **DAN** pemeriksaan kepemilikan sumber daya (*Object-Level Authorization*: pelanggan A dilarang melihat/mengubah pesanan pelanggan B hanya dengan mengganti `:id` di URL!). | **Kriteria:** Pengujian penetrasi otorisasi membuktikan nol celah *Broken Object Level Authorization (BOLA)*.<br>**Teknik:** Praktikum uji serang-bertahan otorisasi RBAC & BOLA antar-mahasiswa di lab. | **Case-Based API Security** `[TM: 100']`<br>**Praktikum Lab 9:** Middleware Otorisasi **RBAC** & Mitigasi Celah **OWASP API1 (BOLA / IDOR)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi spesifikasi **Tugas 2 (RTM-2)** di LMS Edlink. | Autentikasi vs Otorisasi, **Role-Based Access Control (RBAC)**, & Mitigasi **OWASP API Security Top 10** (*BOLA, Broken Function Level Auth*) `[4] API1 & API5` | — |
| **11** | **`Sub-CPMK-3.2` (Bagian I):** Mengelola penyimpanan *in-memory* **Redis** untuk pola *Cache-Aside*, *TTL Invalidation*, & daftar pencabutan sesi/*token blacklist* [C4] | 3.2.1 Ketepatan mengimplementasikan pola **Cache-Aside** dengan **Redis** pada *endpoint* katalog yang sering dibaca, menetapkan *Time-To-Live (TTL)*, dan menghapus *cache* saat data diperbarui (*cache invalidation*). | **Kriteria:** Waktu respons *endpoint* turun drastis (mis. $80\text{ ms} \rightarrow <5\text{ ms}$ pada *cache hit*) tanpa menyajikan data basi setelah *update*.<br>**Teknik:** Pengukuran tolok ukur latensi sebelum vs sesudah **Redis** di lab. | **Performance & Caching Lecture** `[TM: 100']`<br>**Praktikum Lab 10:** Implementasi **Redis** untuk *API Caching*, *Cache Invalidation*, & *Session/Token Revocation* `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Panduan menjalankan kontainer Redis lokal di LMS Edlink. | Arsitektur Penyimpanan *In-Memory* **Redis**, Pola *Cache-Aside*, Strategi *TTL & Cache Invalidation*, serta Manajemen Sesi `[5]` | — |
| **12** | **`Sub-CPMK-3.2` (Bagian II):** Perisai ketahanan API produksi: **Rate Limiting** berbasis Redis, kebijakan **CORS** ketat, & *Security Headers* (`Helmet`) [C4]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.2 Ketepatan menerapkan pembatas laju permintaan (**Rate Limiting** `429 Too Many Requests` anti-*brute-force* pada `/auth/login`), konfigurasi asal **CORS** terpercaya untuk Front-End, dan header keamanan HTTP. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-2`)**.<br>**Teknik:** Pengujian Keamanan & Performa Langsung atas Pengumpulan **Tugas 2 (`CPMK-3`)** di Lab. | **Hardening & Uji Tugas 2** `[TM: 100']`<br>**Praktikum Lab 11:** **Rate Limiting**, **CORS**, *Helmet*, & Verifikasi Keamanan/Redis **Tugas 2 (`CPMK-3`)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan repositori Git **Tugas 2 (`CPMK-3`)** di LMS Edlink. | Mitigasi *Unrestricted Resource Consumption* (*OWASP API4*): **Rate Limiting**, Kebijakan **CORS**, & *HTTP Security Headers* `[4] API4 & API8` | **25%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1` (Bagian I):** Menyusun **Dokumentasi API Interaktif Otomatis** sesuai spesifikasi **OpenAPI 3.1 / Swagger UI** sebagai kontrak kolaborasi Front-End & Mobile [C5→C6] | 4.1.1 Ketepatan menghasilkan spesifikasi **OpenAPI/Swagger** lengkap skema permintaan/respons, kode galat, dan tombol uji otorisasi `Bearer JWT` sehingga pengembang Front-End/Mobile dapat langsung mengintegrasikannya tanpa menebak-nebak. | **Kriteria:** Halaman `/docs` (**Swagger UI**) akurat 100% mencerminkan perilaku nyata seluruh *endpoint*.<br>**Teknik:** Praktikum pembuatan & pengujian kontrak *Swagger/OpenAPI* di lab. | **Contract-First API Lecture** `[TM: 100']`<br>**Praktikum Lab 12:** Penyusunan Dokumentasi Otomatis **Swagger / OpenAPI 3.1** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Spesifikasi proyek akhir layanan produksi **UAS** dirilis di LMS Edlink. | *API-First Design*, Standar **OpenAPI 3.1**, Dokumentasi Interaktif **Swagger UI / Scalar**, & Tata Kelola Versi API (`/api/v1`) `[1] Bab 9 & 11; [5]` | — |
| **14** | **`Sub-CPMK-4.1` (Bagian II) & `4.2` (Bagian I):** Pengujian *Endpoint* Otomatis (*Integration Testing*: `Jest + Supertest` / `Pytest + HTTPX`) & kontainerisasi aplikasi dengan **Docker** [C6] | 4.1.2 Ketepatan menulis skrip pengujian otomatis skenario sukses & gagal (*happy path & unauthorized/validation error*).<br>4.2.1 Ketepatan menyusun `Dockerfile` ramping (*non-root user*, `.dockerignore`) dan `docker-compose.yml` (App + PostgreSQL + Redis). | **Kriteria:** Seluruh tes otomatis lulus hijau dan seluruh tumpukan layanan menyala dengan satu perintah `docker compose up`.<br>**Teknik:** Praktikum pengujian integrasi & kontainerisasi **Docker** *(selaras ko-semester `STI-417`)*. | **Testing & Container Lecture** `[TM: 100']`<br>**Praktikum Lab 13:** *Automated API Integration Testing* & Pengemasan **Dockerfile + Docker Compose** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Templat `.dockerignore` & pengujian basis data terisolasi di LMS Edlink. | *Unit vs Integration Testing* untuk API, Konstruksi **Dockerfile** Produksi, & Lingkungan Lokal Terpadu **Docker Compose** `[2]; [5]` | — |
| **15** | **`Sub-CPMK-4.2` (Bagian II):** **Deployment** Layanan Back-End Terkontainerisasi ke Lingkungan **Cloud**, Konfigurasi *Environment Secrets*, `/health` *Endpoint*, & Klinik Pra-UAS [C6] | 4.2.2 Ketepatan men-*deploy* kontainer aplikasi *back-end* + basis data terkelola ke *cloud* (mis. Railway / Render / Fly.io / Cloud Run / VPS), mengamankan *secrets* produksi, menyediakan `/health` *readiness check*, serta menguji konsumsi HTTPS dari klien Front-End. | **Kriteria:** URL publik HTTPS aktif, dokumentasi `/docs` dapat diakses, dan nol rahasia kredensial bocor di repositori Git!<br>**Teknik:** *Live Cloud Smoke Test* & klinik kesiapan sidang UAS di lab. | **Cloud Deployment & Klinik UAS** `[TM: 100']`<br>**Praktikum Lab 14:** **Cloud Deployment** Kontainer Docker, *Health Check*, *Graceful Shutdown*, & Klinik UAS `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan tautan URL *cloud* aktif, `/docs` OpenAPI, & repositori Git proyek UAS di LMS Edlink. | Praktik Terbaik **Cloud Deployment** Kontainer, *Secret Management*, *Zero-Downtime Health Checks*, & *Handoff* ke `STI-522` dan `STI-625` `[5]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C6]** | Kualitas rekayasa layanan **Back-End Produksi** yang lengkap dengan pengujian otomatis, dokumentasi interaktif **Swagger/OpenAPI**, kontainerisasi **Docker**, serta keberhasilan **Deployment di Cloud** yang dapat diuji langsung melalui HTTPS. | **Kriteria:** **Rubrik Analitik UAS (`K-2`)**.<br>**Teknik:** Penilaian Repositori, Tes Otomatis, Swagger/OpenAPI, & Deployment Cloud (50% UAS) + Sidang Pengujian *Live Request* & Verifikasi Kode Individu (50% UAS). | **Sidang Demonstrasi *Live Cloud API*, Pengujian Kontrak OpenAPI, & Tanya-Jawab Individu**<br>`[150 menit]` | Pengarsipan artefak proyek & nilai akhir `CPL-08` dan `CPL-13` pada portal OBE. | Integrasi Utuh Arsitektur RESTful API, ORM/ODM, Keamanan JWT/RBAC, Redis, OpenAPI, & Docker Cloud Deployment | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-08` [C3])
* **Bentuk Instrumen:** Proyek Individu **Pembangunan RESTful API Modular & Validasi Kontrak HTTP** (*Express* atau *FastAPI*): mahasiswa membangun layanan API minimal 3 *resource* saling berelasi berarsitektur berlapis (*Router–Controller–Service*), mematuhi kode status HTTP standar, dilengkapi *custom logging middleware*, *centralized error handler*, dan validasi skema input ketat (*Zod/Pydantic*).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kepatuhan desain RESTful URI, metode HTTP, & arsitektur modular (`Sub-CPMK-1.1`) = **45%**; (2) Ketepatan *middleware*, *centralized error handling*, & validasi/sanitasi input (`Sub-CPMK-1.2`) = **40%**; (3) Kerapian kode & verifikasi lab = **15%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 25% · Mengukur `CPMK-2` / `CPL-13` [C3])
* **Bentuk Instrumen:** **Ujian Praktik *Live Coding* Integrasi Basis Data & Transaksi di Laboratorium** (150 menit, individu): diberikan spesifikasi domain (mis. Sistem Pemesanan Tiket / Inventori Gudang), mahasiswa membangun *endpoint* CRUD terintegrasi **PostgreSQL via ORM** (+ pencatatan log dokumen **NoSQL**), mengimplementasikan **transaksi ACID** yang me-*rollback* otomatis saat stok kurang, paginasi + filter aman, serta kueri relasi bebas masalah **N+1**.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Ketepatan skema migrasi & integrasi **ORM/ODM** (`Sub-CPMK-2.1`) = **35%**; (2) Kebenaran **transaksi ACID** (`COMMIT/ROLLBACK`) (`Sub-CPMK-2.2`) = **35%**; (3) Paginasi, keamanan dari injeksi, & bebas **N+1 Query** (`Sub-CPMK-2.2`) = **30%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 25% · Mengukur `CPMK-3` / `CPL-08` [15%] & `CPL-13` [10%] [C4])
* **Bentuk Instrumen:** Proyek Keamanan & Performa **Hardening API dengan JWT, RBAC, Bcrypt, & Redis Caching** (diuji penetrasi & tolok ukur di lab): mahasiswa mengamankan layanan API dengan *Bcrypt*, rotasi *Access/Refresh Token JWT*, *Role-Based & Object-Level Authorization* (anti-BOLA!), *Rate Limiting*, *CORS/Helmet*, serta mengimplementasikan *Redis Cache-Aside* lengkap *cache invalidation* saat mutasi data.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Ketangguhan autentikasi **Bcrypt + JWT** & otorisasi **RBAC + Anti-BOLA** (`Sub-CPMK-3.1` → `CPL-08`) = **60%** *(setara 15% bobot MK)*; (2) Ketepatan implementasi **Redis Caching**, *invalidation*, & *Rate Limiting/CORS* (`Sub-CPMK-3.2` → `CPL-13`) = **40%** *(setara 10% bobot MK)*.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-13` [C6])
* **Bentuk Instrumen:** **Proyek Akhir Layanan Back-End Siap Produksi di Cloud** (50% nilai UAS: proyek tim maks. 3 mahasiswa atau individu terintegrasi yang memiliki arsitektur bersih, DB transaksional, keamanan JWT/RBAC, Redis, minimal 12 *automated integration tests*, dokumentasi interaktif **Swagger/OpenAPI 3.1**, `Dockerfile` + `docker-compose.yml`, dan **URL publik HTTPS aktif di Cloud**) + **Sidang Pengujian *Live Request* & Verifikasi Kode Individu** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kelengkapan & keakuratan dokumentasi **Swagger/OpenAPI** serta cakupan tes otomatis (`Sub-CPMK-4.1`) = **35%**; (2) Kualitas kontainerisasi **Docker**, keamanan *secrets*, & keandalan **Deployment Cloud** aktif (`Sub-CPMK-4.2`) = **35%**; (3) Kualitas rekayasa menyeluruh *endpoint* produksi = **15%**; (4) Penguasaan teknis individu saat sidang tanya-jawab = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK RPL & Platform Digital**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Istiadi, S.T., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
