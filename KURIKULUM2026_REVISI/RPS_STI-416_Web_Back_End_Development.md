# RENCANA PEMBELAJARAN SEMESTER (RPS)
# STI-416 — PENGEMBANGAN WEB BACK END
## *Web Back End Development*

---

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI)  
**Universitas:** Universitas Widyagama Malang  
**Semester:** Genap 2026/2027  
**Tanggal Penyusunan:** 28 September 2026  

---

## IDENTITAS MATA KULIAH

| Atribut | Keterangan |
|---|---|
| **Nama Mata Kuliah** | Pengembangan Web Back End (*Web Back End Development*) |
| **Kode Mata Kuliah** | STI-416 |
| **Rumpun Mata Kuliah** | Core Sistem dan Teknologi Informasi |
| **Bobot SKS** | 3 SKS (Teori: 2 SKS, Praktikum: 1 SKS) |
| **Semester** | Semester 4 (Genap) |
| **Mata Kuliah Prasyarat** | FST-207 (Manajemen Basis Data), STI-311 (Pengembangan Web Front End) |
| **Status Mata Kuliah** | Wajib |
| **Nomor Dokumen SPMI** | 071030.B4.5.2.RPS-STI416 |

---

## DOSEN PENGAMPU

**Tim Pengampu:**
- [Nama Dosen Koordinator MK], [Gelar]
- [Nama Dosen Pengampu 2], [Gelar]

**Koordinator Rumpun Mata Kuliah:** [Nama Koordinator RMK], [Gelar]  
**Ketua Program Studi:** [Nama Kaprodi SISTEKIN], [Gelar]

---

## CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN

### CPL Program Studi yang Terkait

| Kode CPL | Rumusan Capaian Pembelajaran Lulusan |
|:---:|---|
| **P4** | Lulusan mampu menguasai konsep dan prinsip arsitektur aplikasi web modern, teknologi RESTful API, autentikasi dan otorisasi berbasis token, serta mekanisme keamanan aplikasi server-side. |
| **KK5** | Lulusan mampu merancang, mengembangkan, dan mendeploy layanan backend yang scalable dan secure menggunakan framework modern (Node.js/Express, Python FastAPI), Object-Relational Mapping (ORM), serta praktik DevOps containerization. |

---

## CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)

| Kode | Rumusan CPMK | Taksonomi Bloom | CPL Terkait |
|:---:|---|:---:|:---:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membangun** RESTful API modular (*B*) menggunakan Node.js/Express atau Python FastAPI (*C*) dengan penanganan rute, middleware, dan sanitasi input yang aman (*D*). | **C3** (Menerapkan) | P4 |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengintegrasikan** backend API dengan database relasional/NoSQL (*B*) menggunakan Object-Relational Mapping (ORM/ODM) (*C*) dengan operasi CRUD transaksional (*D*). | **C3** (Menerapkan) | KK5 |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** sistem autentikasi dan otorisasi (*B*) berbasis JSON Web Token (JWT) dan Role-Based Access Control (RBAC) (*C*) dengan enkripsi password Bcrypt (*D*). | **C4** (Menganalisis) | P4, KK5 |
| **CPMK-4** | Mahasiswa (*A*) mampu **mendokumentasikan** API menggunakan Swagger/OpenAPI serta **mendeploy** backend (*B*) ke server cloud dengan kontainer Docker (*C*) secara andal (*D*). | **C6** (Mencipta) | KK5 |

---

## SUB-CPMK (SUB CAPAIAN PEMBELAJARAN MATA KULIAH)

| Kode | Kompetensi Spesifik | CPMK Induk | Taksonomi |
|:---:|---|:---:|:---:|
| **Sub-CPMK-1.1** | Membangun RESTful API modular menggunakan Node.js/Express atau Python FastAPI. | CPMK-1 | C3 |
| **Sub-CPMK-1.2** | Menerapkan penanganan rute, middleware, dan sanitasi input pada layanan backend. | CPMK-1 | C3 |
| **Sub-CPMK-2.1** | Mengintegrasikan backend dengan database relasional/NoSQL menggunakan ORM/ODM. | CPMK-2 | C3 |
| **Sub-CPMK-2.2** | Mengimplementasikan operasi CRUD transaksional dan query optimization. | CPMK-2 | C3 |
| **Sub-CPMK-3.1** | Mengimplementasikan autentikasi dan otorisasi JWT plus RBAC dengan enkripsi Bcrypt. | CPMK-3 | C4 |
| **Sub-CPMK-3.2** | Menerapkan session dan caching dasar (Redis) pada layanan backend. | CPMK-3 | C4 |
| **Sub-CPMK-4.1** | Mendokumentasikan API menggunakan Swagger/OpenAPI. | CPMK-4 | C6 |
| **Sub-CPMK-4.2** | Mendeploy backend ke server cloud menggunakan kontainer Docker. | CPMK-4 | C6 |

---

## MATRIKS KORELASI CPL TERHADAP CPMK

| CPL ↓ / CPMK → | CPMK-1 | CPMK-2 | CPMK-3 | CPMK-4 |
|:---:|:---:|:---:|:---:|:---:|
| **P4** | ✓ | — | ✓ | — |
| **KK5** | — | ✓ | ✓ | ✓ |

---

## DESKRIPSI SINGKAT MATA KULIAH

Mata kuliah **Pengembangan Web Back End** memberikan pemahaman dan keterampilan komprehensif dalam merancang, membangun, dan mendeploy layanan backend (server-side) yang robust, scalable, dan secure untuk mendukung aplikasi web dan mobile modern. Mahasiswa akan mempelajari arsitektur RESTful API, framework backend populer (Node.js/Express atau Python FastAPI), integrasi database menggunakan ORM/ODM (Sequelize, Prisma, SQLAlchemy, MongoDB), sistem autentikasi dan otorisasi berbasis JSON Web Token (JWT) dan Role-Based Access Control (RBAC), enkripsi password dengan Bcrypt, session management dan caching menggunakan Redis, serta dokumentasi API standar industri menggunakan Swagger/OpenAPI. 

Mahasiswa juga akan menguasai containerization menggunakan Docker untuk deployment di cloud environment. Pembelajaran berfokus pada pendekatan praktis berbasis proyek (*Project-Based Learning*), di mana mahasiswa akan membangun sistem backend lengkap yang terintegrasi dengan database, menerapkan best practices keamanan aplikasi, dan mendeploy ke server cloud. Mata kuliah ini menjadi fondasi krusial bagi mahasiswa yang ingin menjadi **Backend Engineer**, **Full Stack Developer**, atau **API Developer** profesional di industri teknologi.

---

## BAHAN KAJIAN (BODY OF KNOWLEDGE)

Mata kuliah ini mengacu pada standar Body of Knowledge (BoK) APTIKOM:

1. **BK-IS12** — *Web and Mobile Application Development*
   - RESTful API Design & Implementation
   - Server-Side Programming & Business Logic
   - Authentication & Authorization Mechanisms
   - API Security & Input Validation
   
2. **BK-IT04** — *Platform Technologies*
   - Backend Framework (Node.js/Express, Python FastAPI)
   - Database Integration & ORM/ODM
   - Containerization & Cloud Deployment
   - Middleware & Request Processing Pipeline

**Pokok Bahasan:**
1. Arsitektur Server-Side dan Request-Response Cycle
2. RESTful API Design Principles (Resource-Based URL, HTTP Methods)
3. Framework Backend: Node.js/Express atau Python FastAPI
4. Middleware, Routing, dan Error Handling
5. Integrasi Database Relasional (PostgreSQL/MySQL) dan NoSQL (MongoDB)
6. Object-Relational Mapping (ORM): Sequelize, Prisma, SQLAlchemy
7. Operasi CRUD dan Query Optimization
8. Autentikasi Berbasis JSON Web Token (JWT)
9. Role-Based Access Control (RBAC) dan Authorization
10. Password Hashing dengan Bcrypt
11. Session Management dan Caching dengan Redis
12. Input Validation dan Sanitization
13. API Documentation dengan Swagger/OpenAPI
14. Containerization dengan Docker
15. Deployment ke Cloud (AWS, Google Cloud, Heroku, Railway)

---

## PUSTAKA

### Pustaka Utama

1. **Bitnami** (2023). *RESTful Web API Design with Node.js 12*. Packt Publishing. ISBN: 978-1-83898-303-9.
2. **Sebastián Ramírez** (2023). *FastAPI: Modern Python Web Development*. O'Reilly Media. (Official FastAPI Documentation).
3. **Morgan, Nick** (2022). *Node.js Design Patterns*, 3rd Edition. Packt Publishing. ISBN: 978-1-83921-411-0.
4. **Fielding, Roy T.** (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, University of California, Irvine. (RESTful API founding paper).
5. **Tilkov, Stefan & Vinoski, Steve** (2010). *Node.js: Using JavaScript to Build High-Performance Network Programs*. IEEE Internet Computing, 14(6), 80–83.

### Pustaka Pendukung

1. **OWASP** (2024). *OWASP Top 10 Web Application Security Risks*. Retrieved from https://owasp.org/www-project-top-ten/
2. **JWT.io** (2024). *Introduction to JSON Web Tokens*. https://jwt.io/introduction
3. **Docker Inc.** (2024). *Docker Documentation: Containerize Your Applications*. https://docs.docker.com/
4. **Swagger/OpenAPI** (2024). *OpenAPI Specification v3.1*. https://swagger.io/specification/
5. **Prisma Documentation** (2024). *Prisma ORM for Node.js & TypeScript*. https://www.prisma.io/docs
6. **Sequelize Documentation** (2024). *Sequelize ORM for Node.js*. https://sequelize.org/
7. **Redis Documentation** (2024). *Redis Caching and Data Store*. https://redis.io/documentation

---

## RENCANA PEMBELAJARAN 16 PERTEMUAN

### Catatan Waktu Pembelajaran:
- **TM (Tatap Muka):** 1 SKS = 50 menit/pekan (Teori)
- **Praktikum:** 1 SKS = 170 menit/pekan
- **Total per Pertemuan:** 3 SKS = 150 menit (2.5 jam)

---

| **Pekan** | **Sub-CPMK** | **Topik Pembelajaran** | **Kemampuan Akhir yang Diharapkan (ABCD)** | **Metode Pembelajaran** | **Waktu (Menit)** | **Materi Pembelajaran** | **Kriteria & Teknik Penilaian** | **Bobot (%)** |
|:---:|:---:|---|---|:---:|:---:|---|---|:---:|
| **1** | — | **Pengantar MK, Kontrak Belajar & Orientasi** | Mahasiswa (*A*) memahami ruang lingkup mata kuliah, capaian pembelajaran, skema asesmen, dan persiapan environment development (*B*) melalui penjelasan dosen dan instalasi tools (*C*) secara jelas dan terstruktur (*D*). | Kuliah Interaktif, Instalasi Environment | 150' | • Silabus dan RPS<br>• Pengenalan Backend Engineering<br>• Setup Node.js/Python, npm/pip, VSCode<br>• Postman, Database Client | Observasi Partisipasi | — |
| **2** | Sub-1.1 | **Membangun RESTful API Modular (Node.js/Express atau Python FastAPI)** | Mahasiswa (*A*) mampu membangun RESTful API modular menggunakan Node.js/Express atau Python FastAPI (*B*) melalui hands-on praktikum pembuatan server dan routing dasar (*C*) secara tepat dan terukur (*D*). Selaras CPMK-1. | Praktikum / PjBL | 150' | • Arsitektur Client-Server<br>• HTTP Methods (GET, POST, PUT, DELETE)<br>• REST Principles<br>• Inisialisasi Project Express/FastAPI<br>• Basic Routing & JSON Response | Unjuk Kerja Praktikum: Ketepatan routing dan JSON response | — |
| **3** | Sub-1.2 | **Menerapkan Penanganan Rute, Middleware, dan Sanitasi Input** | Mahasiswa (*A*) mampu menerapkan penanganan rute dinamis, middleware (logging, CORS, body-parser), dan sanitasi input pada layanan backend (*B*) melalui praktikum terstruktur (*C*) secara tepat dan aman (*D*). Selaras CPMK-1. | Praktikum / PjBL | 150' | • Dynamic Routing & Route Parameters<br>• Middleware Chain<br>• Error Handling Middleware<br>• Input Validation (express-validator, Pydantic)<br>• Security Middleware (Helmet, CORS) | Unjuk Kerja Praktikum: Implementasi middleware dan validasi input | — |
| **4** | Sub-2.1 | **Mengintegrasikan Backend dengan Database menggunakan ORM/ODM** | Mahasiswa (*A*) mampu mengintegrasikan backend dengan database relasional (PostgreSQL/MySQL) atau NoSQL (MongoDB) menggunakan ORM/ODM (Sequelize/Prisma/SQLAlchemy/Mongoose) (*B*) melalui praktikum konfigurasi dan koneksi database (*C*) secara tepat dan terukur (*D*). Selaras CPMK-2. | Praktikum / PjBL | 150' | • Pengenalan ORM vs ODM<br>• Setup Database Connection<br>• Schema Definition & Model Creation<br>• Sequelize/Prisma/SQLAlchemy Basics<br>• Migration & Seeding | Penugasan: **Tugas 1** (20%)<br>Bangun API dengan routing dan middleware lengkap | **20%** |
| **5** | Sub-2.2 | **Mengimplementasikan Operasi CRUD Transaksional dan Query Optimization** | Mahasiswa (*A*) mampu mengimplementasikan operasi CRUD (Create, Read, Update, Delete) transaksional dan query optimization (*B*) melalui praktikum pembuatan endpoint CRUD lengkap (*C*) secara tepat, efisien, dan transaksional (*D*). Selaras CPMK-2. | Praktikum / PjBL | 150' | • CRUD Operations Implementation<br>• Transactional Queries<br>• Query Optimization (Indexing, Eager Loading)<br>• Error Handling pada Database Operations<br>• HTTP Status Codes Best Practices | Unjuk Kerja Praktikum: Implementasi CRUD lengkap dan efisien | — |
| **6** | Sub-3.1 | **Mengimplementasikan Autentikasi JWT dan RBAC dengan Bcrypt** | Mahasiswa (*A*) mampu mengimplementasikan sistem autentikasi berbasis JSON Web Token (JWT) dan Role-Based Access Control (RBAC) dengan enkripsi password menggunakan Bcrypt (*B*) melalui praktikum endpoint login/register dan middleware auth (*C*) secara aman dan terukur (*D*). Selaras CPMK-3. | Praktikum / PjBL | 150' | • Authentication vs Authorization<br>• Password Hashing dengan Bcrypt<br>• JSON Web Token (JWT) Structure<br>• Endpoint Register & Login<br>• Token Generation & Verification<br>• Protected Routes Middleware | Unjuk Kerja Praktikum: Implementasi autentikasi JWT | — |
| **7** | Sub-3.2 | **Menerapkan Session Management dan Caching dengan Redis** | Mahasiswa (*A*) mampu menerapkan session management dan caching dasar menggunakan Redis pada layanan backend (*B*) melalui praktikum integrasi Redis untuk session storage dan caching response (*C*) secara tepat dan efisien (*D*). Selaras CPMK-3. | Praktikum / PjBL | 150' | • Pengenalan Redis & In-Memory Database<br>• Session Management dengan express-session + Redis<br>• Caching Strategy<br>• Cache Invalidation<br>• Role-Based Access Control (RBAC) Implementation | Unjuk Kerja Praktikum: Implementasi Redis caching dan RBAC | — |
| **8** | CPMK-1, 2, 3 | **UJIAN TENGAH SEMESTER (UTS)** | Mahasiswa (*A*) mendemonstrasikan penguasaan CPMK-1 sampai CPMK-3 (*B*) melalui ujian praktikum pembuatan RESTful API dengan database, autentikasi, dan RBAC (*C*) dengan kriteria ketuntasan minimal (*D*). | Ujian Praktikum | 150' | • **Evaluasi Komprehensif:**<br>  - RESTful API Design<br>  - Database Integration (ORM)<br>  - CRUD Operations<br>  - JWT Authentication<br>  - RBAC Implementation<br>  - Error Handling | Ujian Praktikum: **UTS** (25%)<br>Studi kasus pembuatan API backend sistem tertentu (misal: Sistem Manajemen Perpustakaan) | **25%** |
| **9** | Sub-4.1 | **Mendokumentasikan API Menggunakan Swagger/OpenAPI** | Mahasiswa (*A*) mampu mendokumentasikan API menggunakan standar Swagger/OpenAPI (*B*) melalui praktikum implementasi swagger-ui-express atau FastAPI automatic documentation (*C*) secara profesional dan terstruktur (*D*). Selaras CPMK-4. | Praktikum / PjBL | 150' | • Pentingnya API Documentation<br>• OpenAPI Specification (OAS) 3.0<br>• Swagger UI Setup<br>• Anotasi Swagger (JSDoc/Decorators)<br>• Auto-Generated API Docs (FastAPI)<br>• Best Practices API Documentation | Unjuk Kerja Praktikum: Dokumentasi API lengkap dengan Swagger | — |
| **10** | Sub-4.2 | **Mendeploy Backend ke Server Cloud dengan Docker** | Mahasiswa (*A*) mampu mendeploy backend ke server cloud menggunakan kontainer Docker (*B*) melalui praktikum pembuatan Dockerfile, docker-compose, dan deployment ke platform cloud (Heroku/Railway/GCP) (*C*) secara andal dan reproducible (*D*). Selaras CPMK-4. | Praktikum / PjBL | 150' | • Pengenalan Containerization<br>• Docker Architecture<br>• Dockerfile Best Practices<br>• Docker Compose untuk Multi-Container<br>• Environment Variables Management<br>• Deployment ke Cloud (Railway/Heroku/GCP) | Unjuk Kerja Praktikum: Deploy backend ke cloud dengan Docker | — |
| **11** | CPMK-3, 4 | **Studi Kasus: Integrasi Frontend-Backend & Best Practices Security** | Mahasiswa (*A*) menerapkan CPMK-3 dan CPMK-4 (*B*) pada studi kasus integrasi frontend-backend, CORS configuration, API rate limiting, dan security headers (*C*) secara kolaboratif dan terukur (*D*). | PjBL / Case Method | 150' | • CORS Configuration<br>• API Rate Limiting (express-rate-limit)<br>• Security Headers (Helmet)<br>• HTTPS & SSL Certificates<br>• Environment-Based Configuration<br>• Testing dengan Postman/Thunder Client | Unjuk Kerja Praktikum: Implementasi security best practices | — |
| **12** | CPMK-4 | **Proyek Terapan: Pengembangan Sistem Backend Kompleks** | Mahasiswa (*A*) menyajikan progres proyek backend kompleks (misal: RESTful API E-Commerce, Task Management System, atau Blog Platform) (*B*) dalam forum kelas dengan presentasi fitur, arsitektur, dan tantangan teknis (*C*) dengan argumen yang valid dan solusi terukur (*D*). | PjBL / Presentasi | 150' | • Proyek Mandiri:<br>  - Desain Database Schema<br>  - Implementasi CRUD Lengkap<br>  - Autentikasi Multi-Role<br>  - File Upload & Storage<br>  - Pagination & Filtering<br>  - Search Functionality | Penugasan: **Tugas 2** (25%)<br>Presentasi progres proyek backend + dokumentasi API | **25%** |
| **13** | Seluruh CPMK | **Penyempurnaan Proyek Backend & Code Review** | Mahasiswa (*A*) menyempurnakan hasil proyek backend (*B*) berdasarkan feedback dosen dan peer review, melakukan refactoring code, dan optimasi performa (*C*) secara mandiri dan berkualitas tinggi (*D*). | PjBL / Konsultasi | 150' | • Code Refactoring<br>• Performance Optimization<br>• Error Handling Enhancement<br>• Unit Testing (Jest/Pytest)<br>• Code Review Best Practices<br>• Git Workflow & Version Control | Unjuk Kerja: Kualitas kode dan dokumentasi proyek | — |
| **14** | Seluruh CPMK | **Review Komprehensif & Konsultasi Persiapan UAS** | Mahasiswa (*A*) mengonsolidasikan seluruh capaian pembelajaran (*B*) melalui review materi, tanya jawab intensif, dan simulasi studi kasus UAS (*C*) secara komprehensif (*D*). | Diskusi / Konsultasi | 150' | • Review RESTful API Design<br>• Review Database Integration & ORM<br>• Review Authentication & Authorization<br>• Review Docker & Deployment<br>• Tips & Tricks Troubleshooting<br>• Q&A Session | Observasi Partisipasi | — |
| **15** | Seluruh CPMK | **Presentasi Final Proyek Backend** | Mahasiswa (*A*) mempresentasikan hasil akhir proyek backend secara live demonstration (*B*) di hadapan dosen dan rekan mahasiswa dengan menunjukkan fitur lengkap, API documentation, dan deployment cloud (*C*) secara profesional (*D*). | Presentasi | 150' | • Live Demo Proyek<br>• Penjelasan Arsitektur Sistem<br>• Demonstrasi API Endpoints<br>• Showcase Swagger Documentation<br>• Q&A Session | Unjuk Kerja Presentasi: Kualitas demo dan penguasaan materi | — |
| **16** | Seluruh CPMK | **UJIAN AKHIR SEMESTER (UAS)** | Mahasiswa (*A*) mendemonstrasikan penguasaan seluruh CPMK (CPMK-1 sampai CPMK-4) (*B*) melalui ujian praktikum pembuatan sistem backend lengkap dari nol (authentication, CRUD, deployment) (*C*) dengan kriteria ketuntasan minimal dan batasan waktu tertentu (*D*). | Ujian / Proyek Akhir | 150' | • **Evaluasi Akhir Komprehensif:**<br>  - Build Backend System from Scratch<br>  - RESTful API + Database Integration<br>  - JWT Authentication & RBAC<br>  - API Documentation (Swagger)<br>  - Dockerization & Deployment<br>  - Code Quality & Best Practices | Ujian Praktikum: **UAS** (30%)<br>Studi kasus sistem backend real-world | **30%** |

---

## KOMPONEN PENILAIAN & BOBOT

| No | Komponen Penilaian | Waktu Pelaksanaan | Bentuk Asesmen | Bobot (%) |
|:---:|---|:---:|---|:---:|
| 1 | **Tugas 1** | Pekan 4 | Penugasan Praktikum: Membangun RESTful API dengan routing, middleware, dan validasi input | **20%** |
| 2 | **Ujian Tengah Semester (UTS)** | Pekan 8 | Ujian Praktikum: Studi kasus pembuatan backend API dengan database, autentikasi JWT, dan RBAC | **25%** |
| 3 | **Tugas 2** | Pekan 12 | Penugasan Proyek: Presentasi progres proyek backend kompleks + dokumentasi Swagger/OpenAPI | **25%** |
| 4 | **Ujian Akhir Semester (UAS)** | Pekan 16 | Ujian Praktikum: Build backend system lengkap dari nol dengan deployment ke cloud | **30%** |
| **TOTAL** | | | | **100%** |

---

## KRITERIA PENILAIAN (GRADING RUBRIC)

### Kriteria Umum Penilaian Praktikum & Proyek

| Aspek Penilaian | Sangat Kurang (0-55) | Kurang (56-65) | Cukup (66-75) | Baik (76-85) | Sangat Baik (86-100) |
|---|---|---|---|---|---|
| **Fungsionalitas** | Sistem tidak berfungsi atau error critical | Sebagian fitur berfungsi, banyak bug | Fitur utama berfungsi, beberapa bug minor | Seluruh fitur berfungsi dengan baik | Seluruh fitur sempurna + fitur tambahan |
| **Arsitektur & Clean Code** | Kode tidak terstruktur, tidak ada modularisasi | Struktur kurang jelas, duplikasi kode tinggi | Struktur cukup baik, beberapa modularisasi | Arsitektur modular, kode bersih | Arsitektur sangat baik, best practices diterapkan |
| **Keamanan** | Tidak ada implementasi keamanan | Keamanan minimal, banyak vulnerability | Autentikasi basic, beberapa proteksi | JWT + validasi input lengkap | JWT + RBAC + sanitasi + security headers |
| **Database Integration** | Tidak ada integrasi database | Koneksi database ada, query tidak efisien | ORM digunakan, CRUD dasar berfungsi | ORM optimal, transaksional, relasi lengkap | ORM sempurna + query optimization + migration |
| **Dokumentasi API** | Tidak ada dokumentasi | Dokumentasi minimal, tidak terstruktur | Dokumentasi cukup, beberapa endpoint terdokumentasi | Dokumentasi lengkap dengan Swagger | Swagger sempurna + contoh request/response |
| **Deployment** | Tidak berhasil deploy | Deploy berhasil tapi sering error | Deploy stabil di environment development | Deploy ke cloud, accessible publicly | Deploy production-ready + CI/CD pipeline |

---

## BOUNDARY GUARDRAILS (BATASAN KEWENANGAN MATA KULIAH)

Sesuai dengan Dokumen 037 dan 043 Kurikulum SISTEKIN 2026, mata kuliah ini memiliki batasan kewenangan (*scope*) yang jelas:

### 🟢 **IN-SCOPE (Wajib Diajarkan)**
- Arsitektur Server-Side dan Request-Response Cycle
- Node.js/Express atau Python FastAPI
- RESTful API Design Principles
- Middleware Chain dan Error Handling
- JSON Web Token (JWT) dan OAuth2 Basics
- ORM/ODM (Sequelize, Prisma, SQLAlchemy, Mongoose)
- Query Optimization dan Database Transactions
- Role-Based Access Control (RBAC)
- Session Management dan Caching dengan Redis
- Input Validation dan Sanitization
- API Documentation (Swagger/OpenAPI)
- Containerization dengan Docker
- Deployment ke Cloud Platform (Heroku, Railway, GCP)

### ❌ **OUT-OF-SCOPE (Dilarang Diajarkan)**
- ❌ **Desain Visual Antarmuka Pengguna (HTML/CSS/UI Design)** → Diserahkan ke `STI-311` (Web Front End Development)
- ❌ **Orkestrasi Microservices Multi-Container dengan Kubernetes** → Diserahkan ke `STI-727` (Smart City & Digital Governance)
- ❌ **Event Streaming Kafka Skala Besar dan Message Broker RabbitMQ** → Diserahkan ke `STI-727` (Smart City & Digital Governance)
- ❌ **Mobile App Development (Flutter/React Native)** → Diserahkan ke `STI-522` (Pemrograman Aplikasi Mobile)
- ❌ **Advanced DevOps (CI/CD Pipeline Lengkap, Infrastructure as Code Terraform)** → Diserahkan ke `STB-601` (DevOps & Otomasi Infrastruktur)

### 🔄 **HANDOFF ANCHOR (Titik Serah Terima)**
Mata kuliah ini menghasilkan **layanan backend API yang andal, secure, dan terdokumentasi**. Mahasiswa kemudian akan:
- Melanjutkan ke `STI-522` untuk mengonsumsi API backend ini dari aplikasi mobile.
- Melanjutkan ke `STI-625` (Rekayasa Platform Digital) untuk membangun arsitektur platform yang lebih kompleks.
- Melanjutkan ke `STI-727` (Smart City & Digital Governance) untuk mempelajari orkestrasi layanan terdistribusi skala besar.

---

## LAMPIRAN: INSTRUMEN ASESMEN & RUBRIK PENILAIAN

### LAMPIRAN A: TUGAS 1 — Membangun RESTful API dengan Middleware (Pekan 4)

**Deskripsi Tugas:**  
Mahasiswa diminta membangun RESTful API sederhana untuk sistem **Manajemen Buku Perpustakaan** dengan spesifikasi berikut:

**Spesifikasi Fungsional:**
1. Endpoint `GET /api/books` — Menampilkan semua buku
2. Endpoint `GET /api/books/:id` — Menampilkan detail buku berdasarkan ID
3. Endpoint `POST /api/books` — Menambahkan buku baru (validasi: title, author, year wajib diisi)
4. Endpoint `PUT /api/books/:id` — Mengupdate data buku
5. Endpoint `DELETE /api/books/:id` — Menghapus buku

**Spesifikasi Teknis:**
- Framework: Node.js/Express atau Python FastAPI
- Middleware: CORS, Body Parser, Logger, Error Handler
- Validasi Input: express-validator atau Pydantic
- Data Storage: Boleh menggunakan array in-memory atau file JSON (database belum wajib)
- Format Response: JSON dengan struktur `{ status, message, data }`
- HTTP Status Codes: 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Internal Server Error)

**Deliverables:**
1. Source code lengkap (zip/GitHub repository)
2. File README.md berisi instruksi instalasi dan cara menjalankan
3. Screenshot Postman testing semua endpoint
4. Laporan singkat (max 3 halaman) menjelaskan arsitektur dan middleware yang digunakan

**Rubrik Penilaian Tugas 1:**

| Kriteria | Bobot | 0-55 (Sangat Kurang) | 56-65 (Kurang) | 66-75 (Cukup) | 76-85 (Baik) | 86-100 (Sangat Baik) |
|---|:---:|---|---|---|---|---|
| Fungsionalitas API (5 Endpoint) | 40% | 0-2 endpoint berfungsi | 3 endpoint berfungsi | 4 endpoint berfungsi | 5 endpoint berfungsi | 5 endpoint + edge case handling |
| Implementasi Middleware | 25% | Tidak ada middleware | 1-2 middleware basic | 3 middleware | 4 middleware lengkap | 4+ middleware + custom middleware |
| Validasi Input | 15% | Tidak ada validasi | Validasi sederhana manual | Validasi dengan library, kurang lengkap | Validasi lengkap semua field | Validasi lengkap + error message jelas |
| Struktur Kode & Clean Code | 10% | Kode tidak terstruktur | Struktur kurang jelas | Struktur cukup, ada modularisasi | Struktur baik, modular | Struktur sempurna, best practices |
| Dokumentasi & README | 10% | Tidak ada dokumentasi | Dokumentasi minimal | README cukup lengkap | README lengkap + screenshot | README sempurna + video demo |

---

### LAMPIRAN B: UJIAN TENGAH SEMESTER (UTS) — Pekan 8

**Deskripsi Ujian:**  
Ujian praktikum selama 150 menit (2.5 jam). Mahasiswa diminta membangun **RESTful API Sistem Manajemen Tugas (Task Management System)** dengan spesifikasi:

**Spesifikasi Fungsional:**
1. **User Management:**
   - Register: `POST /api/auth/register` (username, email, password)
   - Login: `POST /api/auth/login` (email, password) → return JWT token
   
2. **Task Management (Protected Routes):**
   - `GET /api/tasks` — Menampilkan semua task milik user yang login
   - `POST /api/tasks` — Membuat task baru (title, description, status, due_date)
   - `PUT /api/tasks/:id` — Update task
   - `DELETE /api/tasks/:id` — Hapus task

**Spesifikasi Teknis:**
- Framework: Node.js/Express atau Python FastAPI
- Database: PostgreSQL/MySQL atau MongoDB (wajib menggunakan ORM/ODM)
- Autentikasi: JWT dengan middleware authentication
- Password Hashing: Bcrypt
- Validasi Input: Semua endpoint harus tervalidasi
- Error Handling: Centralized error handler
- HTTP Status Codes: Sesuai standar RESTful

**Kriteria Penilaian UTS:**

| Kriteria | Bobot | Indikator Penilaian |
|---|:---:|---|
| Fungsionalitas Autentikasi (Register + Login + JWT) | 30% | Register berhasil, password ter-hash, login return JWT valid |
| Integrasi Database dengan ORM | 25% | Database connection berhasil, model terdefinisi, relasi user-task benar |
| Protected Routes & Middleware Auth | 20% | Middleware JWT verification berfungsi, hanya user logged in bisa akses |
| CRUD Operations Lengkap | 15% | Semua endpoint task management berfungsi dengan benar |
| Code Quality & Error Handling | 10% | Kode terstruktur, error handling centralized, HTTP status codes tepat |

---

### LAMPIRAN C: TUGAS 2 — Proyek Backend Kompleks + Dokumentasi Swagger (Pekan 12)

**Deskripsi Tugas:**  
Mahasiswa diminta mengembangkan **sistem backend kompleks** dengan pilihan domain aplikasi:
- **E-Commerce API** (Product, Cart, Order, Payment)
- **Social Media API** (User, Post, Comment, Like, Follow)
- **Learning Management System API** (Course, Enrollment, Assignment, Submission)

**Spesifikasi Minimum:**
1. Minimal 4 resource/entity dengan relasi database
2. Autentikasi JWT + minimal 2 role (user & admin)
3. Role-Based Access Control (RBAC): admin bisa akses semua endpoint, user terbatas
4. Dokumentasi API lengkap menggunakan Swagger/OpenAPI
5. Redis caching minimal 2 endpoint GET yang sering diakses
6. File upload (misal: profile picture atau product image)
7. Pagination dan filtering pada endpoint list
8. Deployment ke cloud (Heroku/Railway/GCP)

**Deliverables:**
1. Source code lengkap di GitHub repository (public)
2. Live deployment URL yang bisa diakses public
3. Swagger Documentation URL (misal: `https://yourapp.com/api-docs`)
4. Video presentasi 10-15 menit menjelaskan arsitektur, fitur, dan demo live
5. Laporan teknis (max 10 halaman) berisi:
   - ERD (Entity Relationship Diagram)
   - API Endpoints Documentation
   - Arsitektur Sistem
   - Penjelasan implementasi RBAC dan caching
   - Screenshot testing Postman
   - Refleksi tantangan teknis dan solusi

**Rubrik Penilaian Tugas 2:**

| Kriteria | Bobot | Indikator |
|---|:---:|---|
| Kompleksitas & Fungsionalitas | 30% | Minimal 4 resource, relasi database benar, fitur lengkap |
| Autentikasi & RBAC | 20% | JWT + minimal 2 role, RBAC berfungsi sempurna |
| Dokumentasi API (Swagger) | 15% | Swagger lengkap, semua endpoint terdokumentasi, contoh request/response jelas |
| Deployment & Accessibility | 15% | Deploy berhasil, URL accessible, tidak ada downtime saat demo |
| Code Quality & Best Practices | 10% | Struktur modular, clean code, environment variables, error handling |
| Presentasi & Komunikasi Teknis | 10% | Video presentasi jelas, demo lancar, penjelasan arsitektur tepat |

---

### LAMPIRAN D: UJIAN AKHIR SEMESTER (UAS) — Pekan 16

**Deskripsi Ujian:**  
Ujian praktikum komprehensif selama 150 menit (2.5 jam). Mahasiswa diminta membangun **sistem backend dari nol** berdasarkan studi kasus yang diberikan saat ujian (misal: **Hotel Reservation System API**, **Event Ticketing System API**, atau **Online Clinic Appointment System API**).

**Spesifikasi Minimum (diberikan saat ujian):**
1. Minimal 3 resource/entity dengan relasi database
2. Autentikasi JWT (register + login)
3. Minimal 1 protected route dengan middleware authentication
4. CRUD lengkap untuk minimal 2 resource
5. Validasi input semua endpoint
6. Dokumentasi Swagger minimal untuk 5 endpoint utama
7. Dockerfile untuk containerization
8. Deploy ke Railway atau Heroku

**Ketentuan Ujian:**
- **Open Internet:** Mahasiswa boleh akses dokumentasi resmi, StackOverflow, dan tutorial
- **Closed Collaboration:** Tidak boleh berkomunikasi dengan mahasiswa lain atau menggunakan AI Code Generator (GitHub Copilot, ChatGPT for coding)
- **Time Limit:** 150 menit ketat
- **Submission:** Source code di-zip + link deployment di-submit via LMS sebelum waktu habis

**Rubrik Penilaian UAS:**

| Kriteria | Bobot | Indikator |
|---|:---:|---|
| Fungsionalitas Autentikasi | 20% | Register & login berfungsi, JWT valid, middleware auth bekerja |
| Database Integration & CRUD | 25% | ORM setup benar, relasi database tepat, CRUD 2 resource berfungsi |
| Validasi Input & Error Handling | 15% | Semua endpoint tervalidasi, error handling centralized |
| Dokumentasi Swagger | 10% | Minimal 5 endpoint terdokumentasi dengan benar |
| Dockerization | 15% | Dockerfile valid, image bisa di-build tanpa error |
| Deployment | 10% | Deploy berhasil, URL accessible dan berfungsi |
| Code Quality | 5% | Struktur kode rapi, tidak ada code smell critical |

---

## LEMBAR VALIDASI & PENGESAHAN

### Memvalidasi:
**Unit Penjaminan Mutu (UPM)**  
Fakultas Sains dan Teknologi Informasi  
Universitas Widyagama Malang

_________________________________  
[Nama Pejabat UPM]  
NUPTK. __________________

---

### Pengampu Mata Kuliah:
Malang, 28 September 2026

Dosen Pengampu,

_________________________________  
[Nama Dosen Koordinator MK]  
NUPTK. __________________

---

### Mengesahkan:
**Ketua Program Studi S1 Sistem dan Teknologi Informasi**  
Fakultas Sains dan Teknologi Informasi  
Universitas Widyagama Malang

_________________________________  
[Nama Ketua Prodi SISTEKIN]  
NUPTK. __________________

---

**Catatan:**  
RPS ini disusun berdasarkan Kurikulum SISTEKIN 2026 (Dokumen 005, 007, 043), Panduan Kurikulum OBE APTIKOM SI v2.0 (IS2020), dan Panduan Kurikulum OBE TI 2023 (IT2017). RPS ini akan dievaluasi dan direvisi setiap tahun akademik sesuai dengan kebutuhan industri dan perkembangan teknologi backend terkini.

---

**END OF DOCUMENT**
