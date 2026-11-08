# 070_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-416 — PENGEMBANGAN WEB BACK END (*Web Back End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.4.RPS-STI416` · **Bobot:** 3 SKS `+P` (`TM 100'`, `Prak 170'`, `PT 120'`, `BM 120'`) · **Semester:** 4  
**Prasyarat:** `FST-207` Basis Data, `STI-311` Pengembangan Web Front End · **CPL:** `CPL-08` (`P4` = 35%) & `CPL-13` (`KK5` = 65%) [Level `R`]  
**Klaster Rubrik:** `K-2` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu & Asisten Laboratorium `STI-416` |
|---|---|
| **Struktur Waktu per Sesi** | **Sesi Teori (`100'`):** Bedah Arsitektur & Standar Protokol `15'` · Inti Rekayasa Back-End `70'` · Rangkuman `15'`<br>**Sesi Praktikum Lab (`170'`):** *Setup* Lingkungan `15'` · Koding & Pengujian API Terbimbing `135'` · Uji Koleksi Request & *Git Push* `20'`, diikuti `PT 120'` & `BM 120'`. |
| **Tumpukan Teknologi Lab** | Node.js LTS + Express/TypeScript + Prisma ORM + Zod + Jest/Supertest *(atau jalur setara Python 3.12 + FastAPI + SQLAlchemy 2.0 + Pydantic + Pytest)*, PostgreSQL 16, MongoDB, Redis 7, Swagger/OpenAPI 3.1, Docker. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** menghabiskan waktu kelas untuk styling CSS/komponen UI (`STI-311`), orkestrasi klaster Kubernetes/Terraform (`STB-601`), maupun *event streaming* Apache Kafka skala besar (`STI-625 Rekayasa Platform Digital`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Teori (`100'`) & Modul Praktikum (`170'`) | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Teori: Arsitektur Server, *Async I/O*, & Semantik **HTTP/REST** · Lab 1: API Pertama & Inspeksi HTTP | 270' | Formatif Lab |
| **2** | `Sub-CPMK-1.1` | Teori: Arsitektur Berlapis (*Router–Controller–Service*) · Lab 2: Struktur **RESTful API Modular** | 270' | Formatif Lab |
| **3** | `Sub-CPMK-1.2` | Teori: Siklus **Middleware** & *Centralized Error Handler* · Lab 3: Logging & RFC 7807 Error JSON | 270' | Formatif Lab |
| **4** | `Sub-CPMK-1.2` | Teori: **Validasi & Sanitasi Input** (*Zod/Pydantic*) · Lab 4: Validasi DTO & Uji **Tugas 1** | 270' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Teori: Pemetaan Relasional **ORM** & *Schema Migrations* · Lab 5: Integrasi PostgreSQL via ORM | 270' | Formatif Lab |
| **6** | `Sub-CPMK-2.1, 2.2` | Teori: **NoSQL ODM** & **Transaksi ACID (`Rollback`)** · Lab 6: MongoDB + Transaksi Atomik | 270' | Formatif Lab |
| **7** | `Sub-CPMK-2.2` | Teori: Eliminasi **N+1 Query** & *Pagination* · Lab 7: Optimasi Kueri ORM & Klinik UTS | 270' | Formatif Lab |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** *Live Coding* API + ORM/ODM + Transaksi ACID + Paginasi | 150' | **UTS (25%)** |
| **9** | `Sub-CPMK-3.1` | Teori: **Bcrypt/Argon2** & Autentikasi **JWT** · Lab 8: *Access/Refresh Token* Flow | 270' | Formatif Lab |
| **10** | `Sub-CPMK-3.1` | Teori: Otorisasi **RBAC** & Mitigasi **OWASP API1 (BOLA)** · Lab 9: *Role & Ownership Guards* | 270' | Formatif Lab |
| **11** | `Sub-CPMK-3.2` | Teori: Arsitektur *In-Memory* **Redis** (*Cache-Aside*) · Lab 10: Akselerasi API & *Invalidation* | 270' | Formatif Lab |
| **12** | `Sub-CPMK-3.2` | Teori: **Rate Limiting**, **CORS**, & *Helmet* · Lab 11: Perisai API & Verifikasi **Tugas 2** | 270' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-4.1` | Teori: Spesifikasi **OpenAPI 3.1 / Swagger UI** · Lab 12: Dokumentasi Kontrak API Otomatis | 270' | Formatif Lab |
| **14** | `Sub-CPMK-4.1, 4.2` | Teori: *Integration Testing* & **Docker** untuk Back-End · Lab 13: Tes Otomatis & `docker compose` | 270' | Formatif Lab |
| **15** | `Sub-CPMK-4.2` | Teori: **Cloud Deployment**, *Secrets*, & `/health` · Lab 14: Deploy HTTPS Publik & Klinik UAS | 270' | Formatif Lab |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang *Live Cloud API*, Kontrak OpenAPI, & Uji Individu | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (TEORI + PRAKTIKUM)

### PERTEMUAN 1 — Arsitektur Sisi Server, *Async I/O*, & Semantik Protokol **HTTP / REST**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C2→C3] · **Alat:** Node.js/Express atau Python FastAPI, Bruno/Postman, `curl -v`.
* **Sesi Teori (`100'`):** Memperkenalkan perjalanan permintaan HTTP dari klien menuju server (HTTP/REST tidak diasumsikan telah dikuasai dari `STI-311`): DNS, TCP/TLS, *Event Loop & Non-Blocking Async I/O*, anatomi *Request/Response*, metode HTTP & sifat idempotensi, keluarga kode status (`2xx, 3xx, 4xx, 5xx`), serta *Richardson Maturity Model*.
* **Sesi Praktikum Lab 1 (`170'`):** Menginisialisasi proyek *back-end*, membangun 5 *endpoint* dasar sesuai konvensi REST, dan menginspeksi *raw HTTP headers* menggunakan `curl -v` serta Bruno/Postman.
* **PT (`120'`) & BM (`120'`):** Merancang tabel kontrak URI RESTful untuk 4 entitas sistem perpustakaan/klinik.

### PERTEMUAN 2 — Konstruksi **RESTful API Modular** (*Router – Controller – Service*)
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Alat:** Express Router / FastAPI `APIRouter`, `dotenv`.
* **Sesi Teori (`100'`):** Mengapa menumpuk 1.500 baris kode di dalam satu berkas `app.js` / `main.py` menghancurkan kolaborasi tim? Membedah pola **Layered Architecture**: *Router* (pemetaan URI), *Controller* (adaptasi HTTP Req/Res), *Service* (aturan bisnis murni), dan *Repository/DAO* (akses data), serta manajemen konfigurasi `.env` (*12-Factor App*).
* **Sesi Praktikum Lab 2 (`170'`):** Memfaktorkan ulang aplikasi tunggal menjadi struktur folder modular bersih lengkap standar amplop JSON (`data`, `meta`, `error`).
* **PT (`120'`) & BM (`120'`):** Menambahkan modul *resource* kedua dengan pemisahan lapisan *Service* yang konsisten.

### PERTEMUAN 3 — Siklus Hidup **Middleware**, *Structured Logging*, & *Centralized Error Handling*
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] · **Alat:** Middleware kustom, `pino`/`winston` atau `structlog`.
* **Sesi Teori (`100'`):** Menguraikan pola pipa berantai (*pipeline*) **Middleware**: bagaimana eksekusi mengalir masuk dan keluar, penyuntikan `X-Request-ID`, pencatatan log JSON terstruktur, serta perancangan kelas `AppError` dan *Global Error-Handling Middleware* (RFC 7807 *Problem Details*) agar server tidak pernah mati mendadak atau membocorkan detail tabel internal ke publik. Merilis resmi **Tugas 1 (RTM-1)**.
* **Sesi Praktikum Lab 3 (`170'`):** Membangun rantai *middleware* pencatat durasi permintaan dan pengendali galat terpusat yang memetakan galat bisnis ke status HTTP presisi.
* **PT (`120'`) & BM (`120'`):** Mengimplementasikan arsitektur modular dan *error handling* pada **Tugas 1**.

### PERTEMUAN 4 — **Validasi Skema & Sanitasi Input** (*Zod / Pydantic*) + Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alat:** `Zod` / `Pydantic v2`, `multer` / `UploadFile`.
* **Sesi Teori (`100'`):** *"Never trust client input!"* — membuktikan bahwa validasi di Front-End bisa dilewati dalam 2 detik menggunakan `curl`; menerapkan validasi skema deklaratif (*body, query, params*), pemangkasan *unknown fields* penangkal *Mass Assignment* (*OWASP API3*), sanitasi string, serta validasi ukuran & *magic bytes/MIME* unggahan berkas.
* **Sesi Praktikum Lab 4 (`170'`):** Mengintegrasikan *validation middleware* otomatis dan melaksanakan pengujian koleksi *endpoint* serta verifikasi langsung **Tugas 1 (`CPMK-1`)**.
* **PT (`120'`) & BM (`120'`):** Menyiapkan basis data PostgreSQL lokal untuk modul ORM pekan depan.

### PERTEMUAN 5 — Integrasi Basis Data Relasional (**PostgreSQL**) via **ORM** & *Schema Migrations*
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Alat:** PostgreSQL 16 + `Prisma ORM` / `SQLAlchemy 2.0 + Alembic`.
* **Sesi Teori (`100'`):** Menghubungkan fondasi `FST-207 Basis Data` ke aplikasi modern: cara kerja **ORM**, pengelolaan siklus **Versioned Database Migrations** yang aman bagi tim, konfigurasi *Connection Pool* (mengapa membuka koneksi DB baru di setiap request akan menumbangkan PostgreSQL!), dan jaminan *Parameterized Queries* anti-*SQL Injection*.
* **Sesi Praktikum Lab 5 (`170'`):** Mendefinisikan skema berelasi `1:N` dan `M:N`, menjalankan *migration* & *seed script*, dan menggantikan penyimpanan memori sementara dengan persistensi PostgreSQL nyata.
* **PT (`120'`) & BM (`120'`):** Menambahkan relasi tabel perantara beserta *constraint* keunikan komposit di ORM.

### PERTEMUAN 6 — Integrasi **NoSQL (MongoDB ODM)** & Penerapan **Transaksi ACID**
* **Sub-CPMK:** `Sub-CPMK-2.1` & `2.2` [C3] · **Alat:** MongoDB + `Mongoose`/`Motor` & PostgreSQL Interactive Transactions.
* **Sesi Teori (`100'`):** Membandingkan model relasional kaku vs dokumen fleksibel **NoSQL** (*Polyglot Persistence*: PostgreSQL untuk transaksi keuangan/pesanan + MongoDB untuk jejak audit/spesifikasi produk variatif), dilanjutkan bedah kritis **Transaksi ACID** dan penanganan *race condition* ketika dua pembeli memesan 1 barang terakhir di detik yang sama!
* **Sesi Praktikum Lab 6 (`170'`):** Mengintegrasikan ODM MongoDB untuk pencatatan aktivitas serta membangun *endpoint* `POST /orders` transaksional di PostgreSQL yang diuji gagal di tengah jalan untuk membuktikan kesempurnaan `ROLLBACK`.
* **PT (`120'`) & BM (`120'`):** Menguji skenario permintaan paralel serentak terhadap *endpoint* pemotongan stok.

### PERTEMUAN 7 — *Query Optimization*: Eliminasi **N+1 Query**, Indeks, & **Pagination** + Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` [C3] · **Alat:** ORM *Query Logging*, PostgreSQL `EXPLAIN`.
* **Sesi Teori (`100'`):** Membongkar pembunuh performa nomor satu pada aplikasi berbasis ORM: **N+1 Query Problem** (memuat 100 artikel lalu tanpa sadar menembakkan 100 kueri tambahan untuk mengambil nama penulisnya!), cara mengatasinya dengan *eager loading / select projection*, penambahan indeks pada kolom filter/urut, serta perbandingan **Offset Pagination** vs **Cursor-Based Pagination**.
* **Sesi Praktikum Lab 7 (`170'`):** Mengaktifkan log SQL ORM untuk menangkap dan menyembuhkan *N+1 query*, mengimplementasikan pencarian + penyortiran + paginasi aman, dan simulasi ujian praktik **UTS Pekan 8**.
* **PT (`120'`) & BM (`120'`):** Persiapan mandiri menghadapi ujian praktik *live coding* pada UTS.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3]) · **Bobot:** **25%** · **Durasi:** `150 menit` (*Live Coding* di Lab).
* **Pelaksanaan:** Mahasiswa membangun layanan *back-end* terintegrasi basis data relasional & NoSQL via **ORM/ODM**, menjalankan migrasi skema, mengimplementasikan **CRUD transaksional ACID** yang tahan gagal, paginasi dinamis, serta optimasi kueri bebas *N+1* dan injeksi.

### PERTEMUAN 9 — Keamanan Kata Sandi (**Bcrypt / Argon2**) & Siklus Autentikasi **JWT**
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Alat:** `bcrypt` / `argon2`, `jsonwebtoken` / `PyJWT`.
* **Sesi Teori (`100'`):** Evaluasi UTS lalu bersinergi dengan `STI-418 Dasar Keamanan Informasi`: mengapa MD5/SHA-256 polos berbahaya untuk kata sandi dan mengapa **Bcrypt / Argon2** memakai *per-user salt* + *work factor* lambat sengaja; perbandingan *Stateful Session* vs *Stateless JWT*, struktur `Header.Payload.Signature` (peringatan keras: jangan pernah menaruh data rahasia di *payload* JWT!), serta pola pasangan *Short-Lived Access Token* (15 menit) + *HttpOnly Refresh Token*.
* **Sesi Praktikum Lab 8 (`170'`):** Membangun *endpoint* `/auth/register`, `/auth/login`, `/auth/refresh`, `/auth/logout` serta *Authentication Guard Middleware*.
* **PT (`120'`) & BM (`120'`):** Menguji skenario kedaluwarsa token (`TokenExpiredError`) dan pemalsuan tanda tangan token.

### PERTEMUAN 10 — Otorisasi **RBAC** & Mitigasi Kerentanan Nomor Satu API: **BOLA / IDOR**
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Alat:** *Role & Ownership Middleware*, Bruno/Postman Multi-User Test.
* **Sesi Teori (`100'`):** Membedah perbedaan **Authentication (`401 Unauthorized` — siapa Anda?)** vs **Authorization (`403 Forbidden` — bolehkah Anda melakukan ini?)**; merancang matriks **Role-Based Access Control (RBAC)** dan membedah celah paling fatal pada **OWASP API Security Top 10**: `API1:2023 Broken Object Level Authorization (BOLA / IDOR)` di mana pengguna terautentikasi sah berhasil mengintip faktur orang lain hanya dengan menaikkan angka ID di URL! Merilis resmi **Tugas 2 (RTM-2)**.
* **Sesi Praktikum Lab 9 (`170'`):** Mengimplementasikan *Role Guard* sekaligus pemeriksaan kepemilikan baris di tingkat kueri (`WHERE id = $1 AND user_id = $2`), lalu saling menguji celah BOLA dengan rekan sebelah meja.
* **PT (`120'`) & BM (`120'`):** Mengimplementasikan skema RBAC dan proteksi objek pada **Tugas 2**.

### PERTEMUAN 11 — Pengelolaan *Session* & Akselerasi Performa dengan **Redis Caching**
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] · **Alat:** Redis 7 (`ioredis` / `redis-py`).
* **Sesi Teori (`100'`):** Mengapa basis data utama tidak boleh dihujani kueri berulang yang hasilnya sama ribuan kali per menit? Membedah struktur penyimpanan *in-memory* **Redis**, pola **Cache-Aside** (*cek Redis $\rightarrow$ jika miss baca DB & simpan ke Redis dengan TTL*), strategi **Cache Invalidation** saat terjadi `POST/PUT/DELETE` agar data tidak basi, serta penyimpanan daftar pencabutan sesi/*Refresh Token* di Redis.
* **Sesi Praktikum Lab 10 (`170'`):** Mengintegrasikan Redis ke *endpoint* katalog/ringkasan berat, mengukur penurunan latensi P95, dan menguji penghapusan *cache* otomatis saat produk diperbarui.
* **PT (`120'`) & BM (`120'`):** Menambahkan *Redis Caching* dan pencabutan sesi *logout* pada **Tugas 2**.

### PERTEMUAN 12 — **Rate Limiting**, Kebijakan **CORS**, *Security Headers*, & Evaluasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alat:** `rate-limiter-flexible` / `slowapi` berbasis Redis, `helmet`, `cors`.
* **Sesi Teori (`100'`):** Melengkapi benteng pertahanan API produksi: pembatasan laju permintaan (**Rate Limiting** bertingkat: ketat pada `/auth/login` anti-*brute-force* vs longgar pada pembacaan katalog), mekanisme *Preflight `OPTIONS`* dan daftar asal diizinkan pada **CORS** (pantang memakai `Access-Control-Allow-Origin: *` bersamaan dengan `credentials: true`!), serta header keamanan HTTP (`Helmet`).
* **Sesi Praktikum Lab 11 (`170'`):** Konfigurasi *Redis Rate Limiter* + *CORS* serta pengujian keamanan dan tolok ukur langsung atas pengumpulan **Tugas 2 (`CPMK-3`)**.
* **PT (`120'`) & BM (`120'`):** Membentuk tim dan menyusun spesifikasi *endpoint* proyek akhir **UAS**.

### PERTEMUAN 13 — Dokumentasi Kontrak API Otomatis dengan **Swagger / OpenAPI 3.1**
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5→C6] · **Alat:** `swagger-jsdoc` / `zod-to-openapi` atau bawaan otomatis `FastAPI OpenAPI`.
* **Sesi Teori (`100'`):** Mengajarkan bagaimana tim industri berkolaborasi lintas peran (*Front-End, Mobile, QA, Mitra B2B*) tanpa salah paham menggunakan kontrak **OpenAPI Specification (OAS 3.1)**: pendefinisian skema komponen, contoh muatan, daftar kode respons, dan skema keamanan `BearerAuth` pada antarmuka interaktif **Swagger UI / Scalar**.
* **Sesi Praktikum Lab 12 (`170'`):** Menghasilkan halaman dokumentasi `/docs` otomatis yang sinkron dengan skema validasi aplikasi dan menguji seluruh alur autentikasi langsung dari peramban Swagger UI.
* **PT (`120'`) & BM (`120'`):** Melengkapi dokumentasi OpenAPI seluruh *endpoint* proyek akhir UAS.

### PERTEMUAN 14 — Pengujian *Endpoint* Otomatis (*Integration Tests*) & Kontainerisasi **Docker**
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C6] · **Alat:** `Jest + Supertest` atau `Pytest + HTTPX`, Docker & Docker Compose.
* **Sesi Teori (`100'`):** Mengajarkan penulisan *Automated API Integration Tests* yang menguji siklus nyata HTTP $\rightarrow$ Basis Data Uji (mencakup skenario `201 Created`, `401 Unauthorized`, `403 Forbidden`, `422 Validation Error`), dilanjutkan pengemasan aplikasi *back-end* ke dalam **Dockerfile** produksi (*multi-stage, non-root user*, `.dockerignore`) dan `docker-compose.yml` lokal terpadu (*bersinergi langsung dengan `STI-417 Komputasi Awan`*).
* **Sesi Praktikum Lab 13 (`170'`):** Menulis minimal 10 tes integrasi otomatis dan menyalakan tumpukan utuh (`API + PostgreSQL + Redis`) melalui `docker compose up --build`.
* **PT (`120'`) & BM (`120'`):** Menuntaskan cakupan tes otomatis dan kontainerisasi proyek UAS.

### PERTEMUAN 15 — **Deployment Cloud** Kontainer Docker, *Health Check*, & Klinik Pra-UAS
* **Sub-CPMK:** `Sub-CPMK-4.2` [C6] · **Alat:** Platform Cloud PaaS/Container (Railway / Render / Fly.io / Cloud Run / VPS), GitHub.
* **Sesi Teori (`100'`):** Menguraikan daftar periksa rilis produksi (*Production Readiness Checklist*): injeksi rahasia produksi (`JWT_SECRET`, `DATABASE_URL`, `REDIS_URL`) tanpa pernah meng-*commit* berkas `.env` ke Git!, penyediaan *endpoint* `GET /health` yang memeriksa konektivitas DB & Redis, *graceful shutdown* (`SIGTERM`), *automated migration on deploy*, serta jembatan *handoff* menuju `STI-522 Pemrograman Aplikasi Mobile` dan `STI-625 Rekayasa Platform Digital`.
* **Sesi Praktikum Lab 14 (`170'`):** Melakukan *deployment* kontainer proyek akhir ke layanan *cloud* hingga memperoleh URL HTTPS publik aktif, menguji koneksi dari klien eksternal, dan klinik akhir kesiapan UAS.
* **PT (`120'`) & BM (`120'`):** Finalisasi `README.md`, koleksi tes otomatis, dokumentasi `/docs`, dan URL produksi UAS.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C6]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Layanan Back-End Produksi di Cloud, Tes Otomatis, Kontainer Docker, & Dokumentasi Swagger/OpenAPI (50% nilai UAS)** dengan **Sidang Pengujian *Live Request* ke URL Cloud & Verifikasi Kode Individu (50% nilai UAS)** di laboratorium.
