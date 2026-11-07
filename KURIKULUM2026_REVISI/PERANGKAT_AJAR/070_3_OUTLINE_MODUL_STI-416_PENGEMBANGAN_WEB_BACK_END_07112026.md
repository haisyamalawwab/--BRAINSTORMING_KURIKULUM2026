# 070_3 — OUTLINE BUKU MODUL PEMBELAJARAN & PRAKTIKUM BERBASIS OBE
## STI-416 — PENGEMBANGAN WEB BACK END (*Web Back End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.4.RPS-STI416` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 4  
**CPL:** `CPL-08` (`P4` = 35%) & `CPL-13` (`KK5` = 65%) [Level `R`] · **BoK:** `BK-IS12`, `BK-IT04`, `BK-IT11`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR + PRAKTIKUM

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Layanan Web Back-End Modern: Arsitektur RESTful API, ORM Transaksional, Keamanan JWT & RBAC, Redis Caching, OpenAPI, hingga Deployment Kontainer Docker di Cloud* |
| **Target Tebal Naskah** | 14 Bab Materi + 14 Modul Praktikum Laboratorium + 2 Unit Evaluasi ($\pm 240\text{–}270\text{ halaman}$ A4) |
| **Pagar Pembatas Buku (*Guardrail*)** | Melanjutkan `FST-207` & `STI-311` pada rekayasa sisi server; tidak mencakup UI/CSS (`STI-311`), orkestrasi Kubernetes/Terraform (`STB-601`), maupun *event streaming* Apache Kafka skala besar (`STI-625 Rekayasa Platform Digital`). |

---

## 2. PETA KESELARASAN 14 BAB & 14 MODUL PRAKTIKUM TERHADAP CPMK & SUB-CPMK

| Bagian | Bab & Lab | Judul Bab Materi & Modul Praktikum | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Arsitektur Sisi Server & RESTful API** | **Bab 1 / Lab 1** | Arsitektur Sisi Server, *Async I/O*, Semantik **HTTP**, & Standar **RESTful API** | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2 / Lab 2** | Konstruksi **RESTful API Modular** Berarsitektur Berlapis (*Router–Controller–Service*) | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3 / Lab 3** | Siklus Hidup **Middleware**, *Structured Logging*, & *Centralized Error Handling* | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | Tugas 1 (20%) |
| | **Bab 4 / Lab 4** | **Validasi Skema & Sanitasi Input** (*Zod/Pydantic*) serta Unggahan Berkas Aman | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Persistensi ORM/ODM & Optimasi Kueri** | **Bab 5 / Lab 5** | Integrasi **PostgreSQL via ORM**, *Versioned Migrations*, & *Connection Pooling* | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 6 / Lab 6** | Integrasi **NoSQL (MongoDB ODM)** & Penerapan **Transaksi ACID (`COMMIT/ROLLBACK`)** | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | UTS (25%) |
| | **Bab 7 / Lab 7** | *Query Optimization*: Eliminasi **N+1 Query**, Indeks API, & **Pagination** | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Simulasi Ujian Praktik Layanan API Terintegrasi ORM, Transaksi ACID, & Paginasi (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (25%)* |
| **Bagian III:<br>Keamanan API & Caching Redis** | **Bab 8 / Lab 8** | Kriptografi Kata Sandi (**Bcrypt/Argon2**) & Siklus Autentikasi **JWT** | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 9 / Lab 9** | Otorisasi **RBAC** & Pencegahan Kerentanan **OWASP API1 (BOLA / IDOR)** | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 10 / Lab 10** | Penyimpanan *In-Memory* **Redis**: Pola *Cache-Aside*, *Invalidation*, & Sesi | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (25%) |
| | **Bab 11 / Lab 11** | Ketahanan API Produksi: **Rate Limiting**, Kebijakan **CORS**, & *Security Headers* | Mg 12 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>OpenAPI, Testing, & Cloud Docker** | **Bab 12 / Lab 12** | Kontrak Kolaborasi & Dokumentasi Interaktif Otomatis **Swagger / OpenAPI 3.1** | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13 / Lab 13** | *Automated API Integration Testing* & Pengemasan Kontainer **Docker / Compose** | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 14 / Lab 14** | **Deployment Cloud** Produksi, *Secret Management*, *Health Check*, & *Handoff* | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Akhir Layanan Back-End Cloud & Protokol Sidang Live API (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB & MODUL PRAKTIKUM

#### BAB 1 & LAB 1: Arsitektur Sisi Server, Async I/O, Semantik HTTP, & Standar RESTful API (Pekan 1)
* **Materi & Praktikum:** *Event Loop*, struktur *HTTP Request/Response*, idempotensi metode HTTP, pemilihan kode status yang presisi, serta konvensi penamaan *resource URI*.

#### BAB 2 & LAB 2: Konstruksi RESTful API Modular Berarsitektur Berlapis (Pekan 2)
* **Materi & Praktikum:** Pemisahan tanggung jawab *Router – Controller – Service – Repository*, konfigurasi variabel lingkungan `.env`, dan amplop respons JSON standar.

#### BAB 3 & LAB 3: Siklus Hidup Middleware, Structured Logging, & Centralized Error Handling (Pekan 3)
* **Materi & Praktikum:** Aliran eksekusi *middleware*, *request correlation ID*, log terstruktur JSON, serta kelas galat kustom dan pengendali galat global berstandar RFC 7807.

#### BAB 4 & LAB 4: Validasi Skema & Sanitasi Input serta Unggahan Berkas Aman (Pekan 4)
* **Materi & Praktikum:** Skema DTO deklaratif (*Zod / Pydantic*), penangkalan *Mass Assignment*, sanitasi karakter berbahaya, dan pembatasan ukuran/MIME unggahan berkas.

#### BAB 5 & LAB 5: Integrasi PostgreSQL via ORM, Versioned Migrations, & Connection Pooling (Pekan 5)
* **Materi & Praktikum:** Pemodelan relasi di *Prisma / SQLAlchemy*, alur kerja *migration* tim, manajemen *Connection Pool*, dan proteksi bawaan *parameterized queries*.

#### BAB 6 & LAB 6: Integrasi NoSQL (MongoDB ODM) & Penerapan Transaksi ACID (Pekan 6)
* **Materi & Praktikum:** Strategi *Polyglot Persistence* (PostgreSQL + MongoDB), pembungkusan operasi multi-langkah dalam transaksi atomik `COMMIT/ROLLBACK`, dan pencegahan *race condition* stok.

#### BAB 7 & LAB 7: Query Optimization — Eliminasi N+1 Query, Indeks API, & Pagination (Pekan 7)
* **Materi & Praktikum:** Diagnosis *N+1 query* dari log SQL, *eager loading & projection*, indeks komposit untuk filter API, serta *Offset vs Cursor Pagination*.

#### BAB 8 & LAB 8: Kriptografi Kata Sandi (Bcrypt/Argon2) & Siklus Autentikasi JWT (Pekan 9)
* **Materi & Praktikum:** *Salted password hashing*, anatomi & verifikasi tanda tangan **JWT**, serta rotasi pasangan *Access Token* dan *HttpOnly Refresh Token*.

#### BAB 9 & LAB 9: Otorisasi RBAC & Pencegahan Kerentanan OWASP API1 (BOLA / IDOR) (Pekan 10)
* **Materi & Praktikum:** Perancangan *Role Guard Middleware* (**RBAC**), validasi kepemilikan baris tingkat objek (**Anti-BOLA**), dan pengujian keamanan multi-peran.

#### BAB 10 & LAB 10: Penyimpanan In-Memory Redis — Pola Cache-Aside, Invalidation, & Sesi (Pekan 11)
* **Materi & Praktikum:** Integrasi klien **Redis**, implementasi *Cache-Aside* ber-TTL, strategi penghapusan *cache* saat mutasi data, dan daftar pencabutan token.

#### BAB 11 & LAB 11: Ketahanan API Produksi — Rate Limiting, CORS, & Security Headers (Pekan 12)
* **Materi & Praktikum:** *Sliding-window Rate Limiting* berbasis Redis (`429 Too Many Requests`), konfigurasi *whitelist* **CORS** dengan Front-End, dan pengamanan header `Helmet`.

#### BAB 12 & LAB 12: Kontrak Kolaborasi & Dokumentasi Otomatis Swagger / OpenAPI 3.1 (Pekan 13)
* **Materi & Praktikum:** Pembangkitan spesifikasi `openapi.json`, anotasi skema permintaan/respons/galat, konfigurasi *Bearer JWT* di **Swagger UI**, dan manajemen versi `/api/v1`.

#### BAB 13 & LAB 13: Automated API Integration Testing & Kontainerisasi Docker (Pekan 14)
* **Materi & Praktikum:** Pengujian *endpoint* otomatis (*Supertest / HTTPX*) terhadap basis data uji terisolasi, penulisan `Dockerfile` produksi *non-root*, dan orkestrasi lokal `docker-compose.yml`.

#### BAB 14 & LAB 14: Deployment Cloud Produksi, Secret Management, Health Check, & Handoff (Pekan 15)
* **Materi & Praktikum:** Penerbitan kontainer ke *cloud* ber-HTTPS, injeksi *environment secrets* aman, *readiness probe* `/health`, *graceful shutdown*, dan kesiapan integrasi menuju `STI-522` serta `STI-625`.
