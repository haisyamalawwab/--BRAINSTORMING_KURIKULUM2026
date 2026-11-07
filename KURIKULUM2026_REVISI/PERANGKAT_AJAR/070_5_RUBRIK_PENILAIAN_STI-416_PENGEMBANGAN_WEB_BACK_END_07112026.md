# 070_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-416 — PENGEMBANGAN WEB BACK END (*Web Back End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.4.RPS-STI416` · **Klaster Rubrik Master (Dok 018):** Klaster 2 (`K-2`)  
**CPL:** `CPL-08` (`P4` = 35%) & `CPL-13` (`KK5` = 65%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN REKAYASA LAYANAN WEB BACK END (`K-2`)

Mengacu **Dokumen 018 §3 (Klaster `K-2`)**, penilaian pada `STI-416` mengedepankan kepatuhan kontrak protokol HTTP/REST, kebersihan arsitektur berlapis (*Separation of Concerns*), integritas transaksi basis data ACID dan efisiensi kueri ORM, ketangguhan keamanan autentikasi/otorisasi (**JWT, RBAC, Bcrypt, Anti-BOLA**) dan *caching* **Redis**, serta kesiapan operasional layanan terkontainerisasi **Docker** di *cloud* lengkap dokumentasi **Swagger/OpenAPI**.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-08` [C3])
**Objek Penilaian:** Proyek **RESTful API Modular**, *Middleware*, *Error Handling*, & Validasi Input (*Express / FastAPI*).

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Desain Kontrak HTTP/REST & Arsitektur Modular**<br>(`Sub-CPMK-1.1`) | **45%** | Penamaan URI kata benda jamak, metode HTTP, & kode status (`200/201/204/400/404/422`) 100% tepat; arsitektur *Router–Controller–Service* terpisah sangat bersih. | Mengikuti konvensi RESTful dengan baik dan memisahkan rute dari pengendali/layanan secara rapi. | *Endpoint* CRUD dasar berjalan, namun terdapat sedikit ketidaktepatan kode status (mis. semua dikembalikan `200 OK`). | URL penuh kata kerja RPC (`/createBarang`, `/hapusBarang`) dan seluruh kode menumpuk di satu berkas. | Server API gagal dijalankan. |
| **2. *Middleware*, *Centralized Error Handler*, & Sanitasi Input**<br>(`Sub-CPMK-1.2`) | **40%** | *Custom middleware*, pengendali galat global terpusat (tanpa kebocoran *stack trace*), dan skema validasi *Zod/Pydantic* menangani seluruh input cacat secara elegan. | Validasi skema input dan *global error handler* berfungsi baik pada seluruh *endpoint* mutasi. | Validasi dasar tersedia, namun beberapa kasus input kosong/salah tipe masih memicu galat `500` mentah. | Tidak ada validasi skema input di sisi server sama sekali. | Aplikasi langsung *crash* saat menerima JSON tidak lengkap. |
| **3. Kerapian Kode, Konfigurasi `.env`, & Verifikasi Lab** | **15%** | Struktur kode sangat konsisten, `.env.example` terdokumentasi tanpa rahasia di Git, dan mahasiswa fasih menjawab verifikasi kode di lab. | Kode rapi, konfigurasi `.env` benar, dan lulus verifikasi laboratorium. | Kode cukup terbaca dengan sedikit duplikasi dan mampu dijelaskan secara dasar. | Penamaan variabel acak dan konfigurasi port/*secret* di-*hardcode*. | Menyalin repositori rekan atau gagal saat verifikasi lab. |

$$\text{Skor Tugas 1} = 0,45(K_1) + 0,40(K_2) + 0,15(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-13` [C3])
**Objek Penilaian:** Ujian Praktik 150 Menit: Integrasi **PostgreSQL ORM + MongoDB ODM**, **Transaksi ACID**, & *Query Optimization*.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Integrasi **ORM/ODM** & *Versioned Migrations***<br>(`Sub-CPMK-2.1`) | **35%** | Skema relasional PostgreSQL (via migrasi ORM) dan dokumen MongoDB (ODM) terintegrasi mulus dengan relasi, *constraint*, serta *connection pool* yang tepat. | Integrasi ORM PostgreSQL dan ODM MongoDB berjalan benar untuk seluruh operasi baca/tulis yang diminta. | Integrasi basis data relasional utama berjalan penuh, namun integrasi pencatatan NoSQL masih parsial. | Skema dibuat manual tanpa *migration* atau gagal menghubungkan aplikasi ke basis data. | Koneksi basis data gagal total. |
| **2. Operasi **CRUD Transaksional (ACID)****<br>(`Sub-CPMK-2.2`) | **35%** | Operasi bisnis multi-tabel dibungkus transaksi atomik yang terbukti 100% me-*rollback* seluruh perubahan parsial saat kondisi gagal/stok habis dipicu. | Mekanisme transaksi `COMMIT/ROLLBACK` berjalan benar menjaga konsistensi data antar-tabel. | Operasi CRUD berjalan untuk alur normal, namun batas transaksi belum melindungi seluruh cabang eksepsi. | Tidak memakai transaksi (stok sudah terpotong padahal pembuatan pesanan gagal di langkah berikutnya!). | Operasi tulis merusak integritas data atau gagal berjalan. |
| **3. Paginasi, Keamanan Kueri, & Eliminasi **N+1 Query****<br>(`Sub-CPMK-2.2`) | **30%** | Paginasi + filter/sortir berjalan aman dari *SQL/NoSQL Injection*, dan inspeksi log SQL membuktikan **nol masalah N+1 Query** (*eager loading* optimal). | Fitur paginasi/filter berfungsi akurat dan kueri bebas penggabungan string SQL mentah. | Paginasi dasar berjalan, namun pemuatan relasi masih memicu *N+1 query* di dalam perulangan. | Menyambung input pengguna langsung ke string SQL mentah (*rentan SQL Injection!*). | Tidak mengimplementasikan paginasi maupun pemuatan relasi. |

$$\text{Skor UTS} = 0,35(K_1) + 0,35(K_2) + 0,30(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-08` [15%] & `CPL-13` [10%] [C4])
**Objek Penilaian:** Proyek Keamanan **JWT, RBAC, Bcrypt, Anti-BOLA** & Akselerasi **Redis Caching + Rate Limiting**.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Autentikasi (**Bcrypt + JWT**) & Otorisasi (**RBAC + Anti-BOLA**)**<br>(`Sub-CPMK-3.1` → `CPL-08`) | **60%**<br>*(15% MK)* | *Hashing* **Bcrypt/Argon2**, pasangan *Access/Refresh Token* **JWT**, *Role Guard* **RBAC**, serta pemeriksaan kepemilikan baris (**nol celah BOLA/IDOR**) berjalan kedap celah saat diuji serang di lab. | Alur registrasi/login Bcrypt+JWT dan pembatasan peran RBAC serta kepemilikan data berjalan akurat. | Login JWT dan pembatasan peran admin/pengguna dasar berfungsi, namun rotasi *refresh token* masih sederhana. | Menyimpan kata sandi *plaintext*/MD5 **ATAU** membiarkan pengguna A mengakses data milik pengguna B (*celah BOLA fatal!*). | Mekanisme autentikasi/otorisasi gagal berfungsi. |
| **2. **Redis Caching**, *Invalidation*, **Rate Limiting**, & *CORS***<br>(`Sub-CPMK-3.2` → `CPL-13`) | **40%**<br>*(10% MK)* | Pola *Cache-Aside* **Redis** terbukti memangkas latensi secara terukur, *cache invalidation* saat mutasi data akurat (anti-*stale data*), serta *Rate Limiting* (`429`) & *CORS/Helmet* aktif sempurna. | *Redis caching* ber-TTL, penghapusan *cache* dasar, dan *rate limiting* berjalan benar sesuai spesifikasi. | *Caching* bacaan Redis berjalan dengan TTL, namun penghapusan *cache* otomatis saat `PUT/DELETE` belum lengkap. | *Cache* tidak pernah kedaluwarsa/dihapus sehingga klien terus menerima data usang, atau tanpa *rate limiting*. | Tidak mengintegrasikan layanan Redis pada aplikasi. |

$$\text{Skor Tugas 2} = 0,60(K_{3.1}) + 0,40(K_{3.2})$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-13` [C6])
**Objek Penilaian:** Proyek **Layanan Back-End Produksi**, Dokumentasi **Swagger/OpenAPI**, Tes Otomatis, & **Cloud Docker Deployment**.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Dokumentasi **Swagger / OpenAPI 3.1** & Pengujian Otomatis**<br>(`Sub-CPMK-4.1`) | **35%** | Halaman `/docs` **Swagger/OpenAPI** mendokumentasikan 100% *endpoint*, skema DTO, contoh, & `BearerAuth` secara interaktif; $\ge 12$ *integration tests* otomatis lulus hijau. | Dokumentasi Swagger/OpenAPI lengkap dapat diuji langsung dan cakupan tes otomatis memenuhi syarat. | Dokumentasi Swagger tersedia untuk *endpoint* utama dan terdapat beberapa tes otomatis dasar. | Dokumentasi tidak sinkron dengan perilaku API nyata atau tidak menyertakan pengujian otomatis. | Tidak memiliki dokumentasi OpenAPI maupun pengujian. |
| **2. Kontainerisasi **Docker** & Keandalan **Deployment Cloud****<br>(`Sub-CPMK-4.2`) | **35%** | `Dockerfile` ramping (*non-root*), `docker-compose.yml` bersih, **URL publik HTTPS Cloud** aktif stabil lengkap `/health` *check*, dan **nol kebocoran `.env` secret** di repositori Git. | Kontainer Docker terbangun bersih dan aplikasi *back-end* aktif dapat diakses publik di *cloud* via HTTPS. | Aplikasi berhasil dikontainerisasi dengan Docker dan di-*deploy*, namun `/health` *endpoint* atau optimasi image belum lengkap. | Hanya berjalan di `localhost` laptop sendiri (gagal *deploy* ke *cloud*) atau membocorkan kredensial produksi ke Git publik! | Kontainer gagal dibangun dan aplikasi tidak dapat diakses. |
| **3. Kualitas Rekayasa Menyeluruh Layanan Produksi** | **15%** | Mengintegrasikan secara utuh seluruh standar semester (modular, ACID, RBAC, Redis, logging) tanpa *crash* saat diuji kueri batas oleh penguji. | Seluruh fitur bisnis utama layanan *back-end* berfungsi stabil dan konsisten di lingkungan produksi. | Fitur utama berjalan baik namun penanganan kasus tepi tertentu masih perlu dipoles. | Banyak *endpoint* mengembalikan `500 Internal Server Error` saat diuji langsung pada sidang. | Proyek sangat minim dan tidak layak guna. |
| **4. Penguasaan Teknis Individu saat Sidang** | **15%** | Setiap anggota fasih mendemonstrasikan alur kode, memodifikasi tes/*endpoint* kecil jika diminta, dan menjelaskan arsitektur *deployment*-nya. | Anggota tim menguasai modul tanggung jawabnya dan menjawab pertanyaan penguji dengan tepat. | Anggota memahami alur utama *endpoint* yang dikerjakannya dengan sedikit arahan. | Anggota gagal menjelaskan cara kerja kode di dalam repositori timnya sendiri. | Tidak hadir sidang UAS atau melanggar kejujuran akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,15(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF PRAKTIKUM LABORATORIUM MINGGUAN (LAB 1–14)

| Kriteria Formatif Lab | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Fungsionalitas & Pengujian Endpoint** | Seluruh *endpoint* praktikum lulus uji skenario positif dan negatif di Bruno/Postman/tes otomatis. | Seluruh *endpoint* modul praktikum berjalan benar tepat waktu. | Menyelesaikan minimal 75% tahapan praktikum mingguan. | Gagal menjalankan server atau *endpoint* dasar praktikum. |
| **Kebersihan Kode & Disiplin Git/Secrets** | Commit atomik rapi, tipe/validasi bersih, dan tidak pernah meng-*commit* `node_modules`/`.venv`/`.env`. | Repositori bersih memakai `.gitignore` yang benar. | Kode berjalan namun riwayat *commit* atau struktur berkas kurang rapi. | Meng-*commit* berkas rahasia `.env` atau pustaka ratusan megabita. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-416` (`CPL-08` & `CPL-13` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa mampu merekayasa layanan **Web Back-End** kelas produksi yang modular, transaksional (**ORM/ODM ACID**), aman (**JWT, RBAC, Bcrypt, Anti-BOLA**), cepat (**Redis**), teruji otomatis, terdokumentasi **OpenAPI**, dan ter-*deploy* di **Cloud** dengan **Docker**. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa terampil membangun RESTful API berlapis, mengintegrasikan PostgreSQL/MongoDB secara aman, menerapkan JWT/RBAC & Redis, serta men-*deploy* kontainer API lengkap Swagger UI ke *cloud*. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi ambang ketuntasan minimal OBE ($\ge 65,0$) dalam pembangunan REST API, operasi CRUD ORM, autentikasi JWT dasar, dokumentasi Swagger, dan pengemasan Docker dasar. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih membuat API yang rentan celah otorisasi/injeksi, gagal menjaga transaksi basis data, atau belum mampu men-*deploy* layanannya ke luar mesin lokal. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal membangun layanan *back-end* fungsional dasar atau melakukan pelanggaran integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-416` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu membangun **RESTful API** modular menggunakan *Node.js/Express* atau *Python FastAPI* sesuai standar HTTP. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu mengelola rute, *middleware*, penanganan galat terpusat, dan validasi/sanitasi input. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengintegrasikan basis data relasional dan NoSQL menggunakan **ORM/ODM**. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menerapkan operasi **CRUD transaksional (ACID)** dan *query optimization* bebas masalah *N+1*. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengimplementasikan autentikasi dan otorisasi API menggunakan **JWT, RBAC,** dan **Bcrypt**. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu mengelola *session*, *rate limiting*, dan *caching* dasar menggunakan **Redis**. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu menyusun dokumentasi API otomatis (**Swagger / OpenAPI**) dan pengujian *endpoint* otomatis. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu mengemas aplikasi *back-end* dengan **Docker** dan men-*deploy*-nya ke lingkungan **cloud**. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-416`)

```text
==============================================================================================================================
     LEMBAR REKAPITULASI PENILAIAN OBE — STI-416 PENGEMBANGAN WEB BACK END (3 SKS: T=2, P=1)
==============================================================================================================================
Semester / TA  : Semester 4 (Genap) / 2026-2027      CPL Dibebankan : CPL-08 (P4: 35%) & CPL-13 (KK5: 65%) [Level: Reinforce]
Klaster Rubrik : K-2 (RPL, Data & Enterprise)        Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2:3.1(15%) | T2:3.2(10%) | UAS (30%)   | NA    | CPL-08 | CPL-13 | Hrf
   |           |                  | [CPMK-1:C3] | [CPMK-2:C3] | [CPMK-3:P4] | [CPMK-3:KK5]| [CPMK-4:C6] | Akhir | (35%)  | (65%)  | Mtu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 86.0        | 90.0        | 88.0        | 90.0        | 88.40 | 88.86  | 88.15  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 76.0        | 80.0        | 78.0        | 80.0        | 78.40 | 78.86  | 78.15  | B+
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 70.0        | 68.40 | 68.86  | 68.15  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 78.00       | 76.00       | 80.00       | 78.00       | 80.00       | 78.40 | 78.86  | 78.15  | 100%
==============================================================================================================================
```
