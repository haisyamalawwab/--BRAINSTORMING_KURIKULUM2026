# 070_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-416 — PENGEMBANGAN WEB BACK END (*Web Back End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.4.RPS-STI416` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 4  
**Klaster Asesmen MK (Dok 018):** Klaster 2 (`K-2`) — Rekayasa Perangkat Lunak, Data & Sistem Enterprise  
**CPL Dibebankan:** `CPL-08` (`P4` = **35%**) & `CPL-13` (`KK5` = **65%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 008, 018, 043,** dan **RPS Pilot STI-416**, mata kuliah `STI-416 Pengembangan Web Back End` (3 SKS `+P`) menerapkan skema bobot baku Klaster `K-2` (`20% / 25% / 25% / 30%`) dengan pemetaan presisi ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-08` / `P4`)** — *Case-Based Modular RESTful API, Middleware, & Schema Input Validation*.
* **UTS (Pekan 8 — 25%) → `CPMK-2` (`CPL-13` / `KK5`)** — *Live Lab Exam: Relational/NoSQL ORM Integration, ACID Transactions, & Query Optimization*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-08` [15%] & `CPL-13` [10%])** — *Case-Based API Security Hardening (JWT, RBAC, Bcrypt, Anti-BOLA) & Redis Caching*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-13` / `KK5`)** — *Project-Based Production Back-End Service with Swagger/OpenAPI, Automated Tests, & Cloud Docker Deployment*.
* **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-2` Dok 018; Target Dok 004 `70%`):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75%` berbasis studi kasus rekayasa layanan API dan proyek produksi *cloud*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-08`**<br>(`P4` — 35%)<br>*Level: R* | **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus rekayasa API: Pembangunan **RESTful API modular** (*Express / FastAPI*) sesuai HTTP | **RTM-1 (Tugas 1)** Repositori Modular + Rubrik Analitik T1 | Sumatif | 11% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Studi kasus rekayasa API: Pengelolaan rute, **middleware**, *error handler*, & sanitasi input | **RTM-1 (Tugas 1)** Uji Koleksi Request + Verifikasi Lab + Rubrik T1 | Sumatif | 9% | |
| **`CPL-13`**<br>(`KK5` — 65%)<br>*Level: R* | **`CPMK-2`**<br>(C3) | `Sub-CPMK-2.1` | Mg 8 | Ujian praktik lab 150': Integrasi basis data relasional & NoSQL via **ORM/ODM** + migrasi | **Soal Praktik UTS** (Bagian Skema & ORM/ODM) + Rubrik UTS | Sumatif | 12% | **25%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian praktik lab 150': Operasi **CRUD transaksional ACID**, paginasi, & *query optimization* | **Soal Praktik UTS** (Bagian Transaksi & Anti-N+1) + Rubrik UTS | Sumatif | 13% | |
| **`CPL-08` (15%)**<br>& **`CPL-13` (10%)**<br>*Level: R* | **`CPMK-3`**<br>(C4) | `Sub-CPMK-3.1`<br>*(`CPL-08`)* | Mg 12 | Studi kasus keamanan API: Implementasi autentikasi/otorisasi **JWT, RBAC, Bcrypt,** & Anti-BOLA | **RTM-2 (Tugas 2)** Uji Penetrasi Otorisasi Lab + Rubrik T2 | Sumatif | 15% | **25%** |
| | | `Sub-CPMK-3.2`<br>*(`CPL-13`)* | Mg 12 | Studi kasus performa API: Pengelolaan *session*, *rate limiting*, & *caching* dasar **Redis** | **RTM-2 (Tugas 2)** Benchmark Redis & Rate Limit + Rubrik T2 | Sumatif | 10% | |
| **`CPL-13`**<br>(`KK5` — 65%)<br>*Level: R* | **`CPMK-4`**<br>(C6) | `Sub-CPMK-4.1` | Mg 16 | Proyek akhir produksi + sidang: Dokumentasi otomatis **Swagger/OpenAPI** & pengujian API | **Halaman `/docs` OpenAPI & Suite Tes Otomatis** + Rubrik UAS | Sumatif | 14% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek akhir produksi + sidang: Kontainerisasi **Docker** & **deployment aplikasi ke cloud** | **URL Publik HTTPS Cloud, Dockerfile, & Sidang UAS** + Rubrik UAS | Sumatif | 16% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN PRAKTIK

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Konstruksi RESTful API Modular & Validasi Kontrak)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Verifikasi Lab **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-08`).
* **Spesifikasi Pengerjaan Individu:**
  1. Membangun layanan **RESTful API** modular (minimal 3 *resource* bisnis, mis. `departments`, `courses`, `enrollments`) dengan pemisahan bersih *Router – Controller – Service* menggunakan *Node.js/Express* atau *Python FastAPI*.
  2. Mengimplementasikan kode status HTTP presisi, *request logger middleware*, *global error handler* berformat JSON konsisten, serta validasi skema input ketat (*Zod/Pydantic*) yang menolak muatan cacat dengan `422 Unprocessable Entity`.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Integrasi ORM/ODM, Transaksi ACID, & Optimasi Kueri)
* **Format & Bobot:** Ujian Praktik *Live Coding* di Laboratorium (**150 menit**, individu) · Bobot **25%** (`CPMK-2` → `CPL-13`).
* **Spesifikasi Soal Praktik:**
  1. Mengintegrasikan API dengan **PostgreSQL melalui ORM** (lengkap *schema migration* & *seed*) serta **MongoDB melalui ODM** untuk jejak aktivitas.
  2. Mengimplementasikan *endpoint* transaksi bisnis multi-langkah (wajib membuktikan `ROLLBACK` atomik saat salah satu syarat gagal!), fitur pencarian + penyortiran + paginasi aman, serta pemuatan relasi yang **bebas masalah N+1 Query** saat diperiksa pada log SQL.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Pengamanan JWT/RBAC/Bcrypt & Akselerasi Redis Caching)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Uji Lab **Pekan 12** · Bobot **25%** (`CPMK-3` → `CPL-08` [15%] & `CPL-13` [10%]).
* **Spesifikasi Teknis Individu:**
  1. Mengimplementasikan *password hashing* **Bcrypt/Argon2**, autentikasi pasangan *Access & Refresh Token* **JWT**, matriks otorisasi **RBAC** minimal 3 peran, serta proteksi kepemilikan sumber daya (**Anti-BOLA/IDOR**).
  2. Mengintegrasikan **Redis** untuk pola *Cache-Aside* lengkap *cache invalidation* otomatis saat data diubah, pencabutan sesi *logout*, dan **Rate Limiting** pelindung *endpoint* autentikasi.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Layanan Back-End Produksi, OpenAPI, & Cloud Docker)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-13`), memadukan **Proyek Layanan Produksi di Cloud (50% nilai UAS)** + **Sidang Pengujian *Live Request* & Verifikasi Individu (50% nilai UAS, 150 menit)**:
  1. Membangun layanan *back-end* utuh siap produksi yang dilengkapi minimal **12 pengujian integrasi otomatis** (*Jest/Supertest* atau *Pytest*), dokumentasi interaktif lengkap **Swagger / OpenAPI 3.1** pada `/docs`, berkas `Dockerfile` + `docker-compose.yml`, serta **ter-deploy aktif di lingkungan Cloud** dengan HTTPS dan `/health` *endpoint*.
  2. Saat sidang, dosen penguji menembakkan permintaan langsung ke URL *cloud* tim melalui halaman *Swagger UI* / Bruno serta menguji pemahaman kode tiap anggota secara individu.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-416}}$)
$$NA_{\text{STI-416}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004, 008, & RPS Pilot STI-416)
1. **Ketercapaian `CPL-08` (`P4` — bobot 35% MK dari `CPMK-1` [20%] + `Sub-CPMK-3.1` pada Tugas 2 [15%]):**
   $$\text{Score}_{\text{CPL-08, STI-416}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,15\,S_{\text{T2, Sub-3.1}}(i)}{0,35}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,35 = 1,05\text{ SKS}$).*
2. **Ketercapaian `CPL-13` (`KK5` — bobot 65% MK dari `CPMK-2` [25%] + `Sub-CPMK-3.2` pada Tugas 2 [10%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-13, STI-416}}(i) = \frac{0,25\,S_{\text{UTS}}(i) + 0,10\,S_{\text{T2, Sub-3.2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,65}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,65 = 1,95\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**; remedial diberikan maksimal 1 kali bagi mahasiswa dengan skor CPMK $< 65,0$ dengan nilai plafon pasca-remedial **70,0 (B)**.
