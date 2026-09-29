# RPS STI-416 — PENGEMBANGAN WEB BACK END (VERSI 2 — SIMPLIFIED PYTHON FOCUS)
## *Web Back End Development — Python Web API Development with Flask*

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI)  
**Universitas:** Universitas Widyagama Malang  
**Nomor Dokumen SPMI:** 071030.B4.5.2.RPS-STI416-V2  
**Versi:** 2.0 — Simplified Python Focus  
**Tanggal Penyusunan:** 28 September 2026  
**Status:** ✅ **FINAL & READY FOR APPROVAL**

---

## 🔖 TENTANG VERSI 2 (DOWNGRADE)

### Rasionale Penyederhanaan

Versi 2 RPS ini dirancang khusus dengan pertimbangan:

1. **Keterbatasan Kemampuan Teknis Dosen**
   - Tidak semua dosen memiliki keahlian mendalam dalam Node.js/TypeScript
   - Python lebih familiar bagi dosen dengan latar belakang data science/ML
   - Flask memiliki learning curve yang lebih landai dibanding Express.js

2. **Profil Mahasiswa dengan Motivasi Menengah**
   - Mahasiswa semester 4 dengan IPK 2.75-3.25
   - Kemampuan pemrograman Python sudah diajarkan di Semester 1-2
   - Fokus pada **practical skills** bukan kompleksitas arsitektur

3. **Sustainability & Maintainability**
   - Mengurangi dependency library yang kompleks
   - Fokus pada konsep fundamental backend yang transferable
   - Dokumentasi lebih sederhana dan terstruktur

### Perbedaan dengan Versi 1 (Original)

| Aspek | Versi 1 (Original) | Versi 2 (Simplified) |
|-------|-------------------|----------------------|
| **Bahasa** | Node.js/Express atau FastAPI | **Python Flask (wajib)** |
| **ORM** | Sequelize/Prisma (kompleks) | **Flask-SQLAlchemy (simple)** |
| **Auth** | JWT + OAuth2 + RBAC | **JWT + Basic RBAC (2 role saja)** |
| **Caching** | Redis (setup kompleks) | **Flask-Caching (in-memory)** |
| **Documentation** | Swagger/OpenAPI (kompleks) | **Flask-RESTX (auto-swagger)** |
| **Deployment** | Docker + Cloud (Railway/GCP) | **Heroku (one-click deploy)** |
| **Complexity Level** | Advanced (C4-C6) | **Intermediate (C3-C4)** |
| **Project Scope** | E-Commerce full-stack | **Library Management System API** |
| **Learning Curve** | Steep (70% fail rate) | **Gentle (target 85% pass rate)** |

### Target Capaian Pembelajaran

- ✅ Mahasiswa dapat **membangun RESTful API sederhana dengan Python Flask**
- ✅ Mahasiswa dapat **mengintegrasikan database SQLite/MySQL menggunakan SQLAlchemy ORM**
- ✅ Mahasiswa dapat **mengimplementasikan autentikasi JWT dasar dan otorisasi 2 role**
- ✅ Mahasiswa dapat **men-deploy aplikasi Flask ke Heroku atau PythonAnywhere**
- ✅ Mahasiswa **memahami konsep fundamental backend** yang transferable ke framework lain

---

## BAGIAN I: IDENTITAS & CAPAIAN PEMBELAJARAN

### 1.1 IDENTITAS MATA KULIAH

| Atribut | Detail |
|---------|--------|
| **Kode MK** | STI-416 |
| **Nama MK (ID)** | Pengembangan Web Back End |
| **Nama MK (EN)** | *Web Back End Development* |
| **SKS** | **3 SKS** (Teori: 2 SKS, Praktikum: 1 SKS) |
| **Tipe** | **+P** (Teori dengan Praktikum) |
| **Semester** | **Semester 4** (Genap) |
| **Prasyarat** | `FST-207` Sistem Basis Data (Database Systems)<br>`STI-311` Pengembangan Web Front End (Web Front End Development) |
| **Status** | **Wajib** (Core STI) |
| **Rumpun** | Platform & Pengembangan Web/Mobile |
| **Kelompok** | Mata Kuliah Keahlian Berkarya (MKB) |

---

### 1.2 CAPAIAN PEMBELAJARAN LULUSAN (CPL) PROGRAM STUDI

Mata kuliah ini berkontribusi langsung terhadap 2 CPL Program Studi SISTEKIN:

#### CPL-P4: Arsitektur RESTful API & Keamanan Server
> Mahasiswa menguasai arsitektur RESTful API, protokol HTTP/HTTPS, mekanisme autentikasi-autorisasi (Basic Auth, Token-Based, OAuth), desain endpoint resource-oriented, dan prinsip keamanan backend (OWASP Top 10, injection prevention, secure session management).

**Indikator Kinerja CPL-P4:**
- Merancang endpoint RESTful API sesuai prinsip resource-oriented design
- Mengimplementasikan autentikasi JWT dan otorisasi role-based
- Menerapkan teknik keamanan backend (input sanitization, SQL injection prevention, secure password hashing)

#### CPL-KK5: Backend Engineering & ORM
> Mahasiswa terampil membangun backend application logic menggunakan kerangka kerja server-side (Node.js, Python, PHP), mengintegrasikan database relasional/non-relasional melalui ORM/ODM, mengimplementasikan middleware pipeline, dan men-deploy aplikasi backend ke cloud platform production-ready.

**Indikator Kinerja CPL-KK5:**
- Membangun backend API menggunakan Python Flask dengan arsitektur modular
- Mengintegrasikan database menggunakan SQLAlchemy ORM
- Men-deploy aplikasi backend ke platform cloud (Heroku/PythonAnywhere)

---

### 1.3 CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)

Mata kuliah ini memiliki **4 CPMK** yang dirancang dengan format **ABCD** (Audience, Behavior, Condition, Degree) dan level **Taksonomi Bloom C3-C4** (disesuaikan untuk kemampuan mahasiswa menengah):

| Kode | Rumusan CPMK | Bloom | CPL |
|:---:|---|:---:|:---:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membangun** RESTful API modular dengan routing, middleware, dan error handling (*B*) menggunakan Python Flask (*C*) secara terstruktur dan fungsional (*D*). | **C3** | `P4`, `KK5` |
| **CPMK-2** | Mahasiswa (*A*) mampu **mengintegrasikan** database relasional dengan ORM (*B*) menggunakan Flask-SQLAlchemy pada aplikasi Flask (*C*) secara efisien dan bebas SQL injection (*D*). | **C3** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** autentikasi JWT dan otorisasi role-based (Admin-User) (*B*) pada endpoint yang dilindungi (*C*) secara aman sesuai standar OWASP (*D*). | **C4** | `P4`, `KK5` |
| **CPMK-4** | Mahasiswa (*A*) mampu **men-deploy** aplikasi Flask dengan dokumentasi API sederhana (*B*) ke platform cloud production-ready (*C*) secara fungsional dan dapat diakses publik (*D*). | **C3** | `KK5` |

**Catatan Penyederhanaan:**
- CPMK-1 fokus pada **Flask fundamental** (bukan Express/FastAPI yang lebih kompleks)
- CPMK-2 menggunakan **Flask-SQLAlchemy** (built-in, mudah dipelajari) bukan Sequelize/Prisma
- CPMK-3 hanya **2 role** (Admin-User), bukan sistem RBAC kompleks multi-level
- CPMK-4 deployment ke **Heroku** (one-click), bukan Docker/Kubernetes

---

### 1.4 SUB-CAPAIAN PEMBELAJARAN MATA KULIAH (SUB-CPMK)

Penjabaran operasional CPMK menjadi **8 Sub-CPMK** yang akan dipelajari secara bertahap:

| Kode | Kompetensi Spesifik | CPMK | Bloom | Pekan |
|:---:|---|:--:|:--:|:---:|
| **Sub-CPMK-1.1** | Membangun RESTful API sederhana dengan Flask routing (GET, POST, PUT, DELETE) | CPMK-1 | **C3** | 2 |
| **Sub-CPMK-1.2** | Mengimplementasikan middleware (request logging, CORS) dan error handling global | CPMK-1 | **C3** | 3 |
| **Sub-CPMK-2.1** | Menghubungkan Flask dengan database SQLite/MySQL menggunakan Flask-SQLAlchemy | CPMK-2 | **C3** | 4 |
| **Sub-CPMK-2.2** | Melakukan operasi CRUD pada model database dengan relationship (One-to-Many) | CPMK-2 | **C3** | 5 |
| **Sub-CPMK-3.1** | Mengimplementasikan autentikasi JWT (register, login, token generation) | CPMK-3 | **C4** | 6 |
| **Sub-CPMK-3.2** | Mengimplementasikan otorisasi role-based (Admin & User) pada protected endpoint | CPMK-3 | **C4** | 7 |
| **Sub-CPMK-4.1** | Membuat dokumentasi API sederhana dengan Flask-RESTX (Swagger auto-generate) | CPMK-4 | **C3** | 9-10 |
| **Sub-CPMK-4.2** | Men-deploy aplikasi Flask ke Heroku dengan environment variable configuration | CPMK-4 | **C3** | 11 |

---

### 1.5 MATRIKS KORELASI CPL ↔ CPMK

| CPL | CPMK-1 | CPMK-2 | CPMK-3 | CPMK-4 |
|:---:|:---:|:---:|:---:|:---:|
| **P4** — Arsitektur RESTful API & Keamanan Server | ✅ | | ✅ | |
| **KK5** — Backend Engineering & ORM | ✅ | ✅ | ✅ | ✅ |

---

### 1.6 DESKRIPSI SINGKAT MATA KULIAH

**Pengembangan Web Back End (STI-416)** adalah mata kuliah wajib pada Semester 4 yang membekali mahasiswa dengan keterampilan fundamental dalam membangun backend application logic menggunakan **Python Flask framework**. 

Mata kuliah ini berfokus pada konsep dan praktik esensial backend engineering: **RESTful API design** dengan routing modular, **database integration** menggunakan SQLAlchemy ORM, **autentikasi JWT** dan otorisasi role-based sederhana, serta **deployment** ke platform cloud production-ready.

Berbeda dengan pendekatan yang memerlukan penguasaan JavaScript/Node.js atau framework kompleks seperti FastAPI, versi RPS ini dirancang khusus untuk **mahasiswa dengan motivasi menengah** yang sudah familiar dengan Python dari semester awal. Dengan menggunakan **Flask** (micro-framework yang minimalis), mahasiswa dapat fokus pada **konsep fundamental backend** tanpa terbebani kompleksitas tooling dan dependency management.

Pembelajaran dilakukan melalui metode **praktikum intensif** dengan studi kasus **Library Management System API** — sebuah domain sederhana namun cukup representatif untuk melatih seluruh kompetensi backend dasar. Mahasiswa akan membangun API yang dapat melakukan manajemen buku, anggota perpustakaan, peminjaman, dan pengembalian dengan autentikasi Admin-User.

Di akhir semester, mahasiswa mampu **men-deploy aplikasi Flask mereka ke Heroku** dan memiliki portofolio backend project yang fungsional dan dapat diakses publik — sebuah modal penting untuk magang industri di Semester 6.

**Prasyarat:** 
- `FST-207` Sistem Basis Data (untuk memahami konsep RDBMS, SQL, dan normalisasi)
- `STI-311` Pengembangan Web Front End (untuk memahami komunikasi client-server dan konsumsi API)

**Kata Kunci:** Python Flask, RESTful API, SQLAlchemy ORM, JWT Authentication, Role-Based Access Control (RBAC), Heroku Deployment, Backend Engineering

---

### 1.7 BAHAN KAJIAN (BODY OF KNOWLEDGE)

Mata kuliah ini mencakup bahan kajian dari **2 BoK APTIKOM**:

#### BK-IS12: Web and Mobile Application Development
- Server-side web programming dengan Python Flask
- RESTful API design dan resource-oriented architecture
- HTTP methods (GET, POST, PUT, DELETE) dan status codes
- Request-response cycle dan middleware pipeline

#### BK-IT04: Platform Technologies
- Web framework fundamentals (Flask micro-framework)
- Database integration dengan ORM (Flask-SQLAlchemy)
- Authentication dan authorization mechanisms (JWT, role-based)
- Cloud platform deployment (Platform-as-a-Service / PaaS)

#### Pokok Bahasan (17 Topik Utama):

1. **Flask Fundamentals** — Setup environment, Flask app structure, routing, request handling
2. **RESTful API Design** — Resource-oriented endpoints, HTTP methods, status codes, JSON response
3. **Middleware & Error Handling** — Request logging, CORS configuration, global error handler
4. **Database Integration** — Flask-SQLAlchemy setup, model definition, migration dengan Flask-Migrate
5. **CRUD Operations** — Create, Read, Update, Delete data dengan ORM
6. **CRUDLFIX Extended** — **List with Pagination**, **Filter/Search**, **Import CSV/Excel**, **Export CSV/JSON** ⭐ **NEW**
7. **Database Relationships** — One-to-Many relationships (Books ↔ Authors, Loans ↔ Users)
8. **Input Validation** — Request body validation dengan marshmallow atau Flask-Inputs
9. **Authentication (JWT)** — User registration, login, password hashing (bcrypt), token generation
10. **Authorization (RBAC)** — Role-based access control (Admin vs User), protected endpoints decorator
11. **Security Best Practices** — Password hashing, SQL injection prevention, CORS, input sanitization
12. **API Documentation** — Flask-RESTX untuk auto-generate Swagger UI
13. **Environment Configuration** — .env file, environment variables, config management
14. **Deployment** — Heroku deployment, Procfile, Gunicorn WSGI server
15. **Testing (Optional)** — Unit testing dengan pytest-flask (jika waktu memungkinkan)
16. **Performance Optimization** — Query optimization, N+1 problem, eager loading ⭐ **NEW**
17. **Capstone Project** — Library Management System API (full implementation dengan CRUDLFIX)

---

### 1.8 PUSTAKA

#### A. Pustaka Utama (Textbooks & Core References)

1. **Grinberg, M.** (2018). *Flask Web Development: Developing Web Applications with Python* (2nd Edition). O'Reilly Media. ISBN: 978-1491991732.
   
2. **Burke, B.** (2020). *Flask Framework Cookbook* (2nd Edition). Packt Publishing. ISBN: 978-1789951295.

3. **Aggarwal, S.** (2021). *Building REST APIs with Flask: Create Python Web Services with MySQL*. Apress. ISBN: 978-1484266656.

4. **Fielding, R. T.** (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, University of California, Irvine. [REST Architecture Seminal Work]

5. **Flask Official Documentation** (2024). https://flask.palletsprojects.com — Referensi resmi dan tutorial terstruktur.

#### B. Pustaka Pendukung (Supporting Materials)

6. **SQLAlchemy Official Documentation** (2024). https://www.sqlalchemy.org — ORM library documentation.

7. **JWT.io** (2024). https://jwt.io — JSON Web Token introduction dan debugger.

8. **OWASP Top 10** (2021). https://owasp.org/www-project-top-ten — Web application security risks.

9. **Flask-RESTX Documentation** (2024). https://flask-restx.readthedocs.io — Auto-documentation dengan Swagger.

10. **Heroku Python Support** (2024). https://devcenter.heroku.com/categories/python-support — Deployment guide.

11. **PythonAnywhere** (2024). https://help.pythonanywhere.com — Alternative cloud platform untuk Flask.

12. **Miguelgrinberg.com Blog** (2024). https://blog.miguelgrinberg.com — Artikel tutorial Flask oleh author buku referensi.

---

## BAGIAN II: RENCANA PEMBELAJARAN SEMESTER (16 PERTEMUAN)

### 2.1 TABEL RENCANA PEMBELAJARAN

| Pekan | Sub-CPMK | Topik Pembelajaran | Kemampuan Akhir yang Diharapkan (ABCD) | Metode | Waktu | Materi Pembelajaran | Bobot Asesmen |
|:---:|:---:|---|---|:---:|:---:|---|:---:|
| **1** | — | **Pengantar MK & Setup Environment** | Mahasiswa (*A*) memahami silabus, CPL, CPMK, dan aturan perkuliahan (*B*) melalui penjelasan dosen (*C*) secara jelas (*D*). Setup Python, Flask, dan VSCode. | Kuliah Interaktif + Demo | **150'** | • Kontrak Belajar<br>• RPS Overview<br>• Python 3.9+ Setup<br>• Flask Installation<br>• VSCode + Extensions<br>• Postman Setup | — |
| **2** | Sub-1.1 | **Flask Routing & RESTful API Dasar** | Mahasiswa (*A*) mampu membangun RESTful API sederhana dengan Flask routing (GET, POST, PUT, DELETE) (*B*) menggunakan Flask framework (*C*) secara terstruktur dan fungsional (*D*). | Kuliah + Praktikum | **150'** | • Flask App Structure<br>• Routing `@app.route()`<br>• HTTP Methods (GET, POST, PUT, DELETE)<br>• JSON Response `jsonify()`<br>• Request Handling `request.get_json()`<br>• Status Codes (200, 201, 404, 500) | — |
| **3** | Sub-1.2 | **Middleware, CORS & Error Handling** | Mahasiswa (*A*) mampu mengimplementasikan middleware (request logging, CORS) dan error handling global (*B*) pada aplikasi Flask (*C*) secara robust (*D*). | Kuliah + Praktikum | **150'** | • Flask Middleware Concept<br>• Request Logging<br>• CORS Configuration `flask-cors`<br>• Global Error Handler `@app.errorhandler()`<br>• Custom Exception Classes<br>• Error Response Format | — |
| **4** | Sub-2.1 | **Database Integration dengan SQLAlchemy** | Mahasiswa (*A*) mampu menghubungkan Flask dengan database SQLite/MySQL menggunakan Flask-SQLAlchemy (*B*) pada aplikasi Flask (*C*) secara efisien (*D*). | Kuliah + Praktikum | **150'** | • Flask-SQLAlchemy Setup<br>• Database URI Configuration<br>• Model Definition `db.Model`<br>• Column Types & Constraints<br>• `db.create_all()` Migration<br>• SQLite vs MySQL | **📋 Tugas 1**<br>**(20%)**<br><br>*RESTful API Dasar*<br>(Sub-CPMK 1.1–1.2)<br><br>Deadline:<br>Pekan 5 |
| **5** | Sub-2.2 | **CRUD Operations & Database Relationships** | Mahasiswa (*A*) mampu melakukan operasi CRUD pada model database dengan relationship (One-to-Many) (*B*) menggunakan SQLAlchemy ORM (*C*) secara efisien dan bebas SQL injection (*D*). | Kuliah + Praktikum | **150'** | • CRUD dengan SQLAlchemy (`.query`, `.filter`, `.all()`, `.first()`)<br>• Create: `db.session.add()`, `.commit()`<br>• Update: modifikasi object + `.commit()`<br>• Delete: `db.session.delete()`<br>• Relationship (One-to-Many)<br>• Foreign Key & `db.relationship()` | — |
| **6** | Sub-2.2 (Extended) | **CRUDLFIX: List, Filter & Pagination** ⭐ | Mahasiswa (*A*) mampu mengimplementasikan **List with Pagination**, **Filter/Search**, dan **Sorting** (*B*) pada endpoint RESTful API (*C*) secara efisien dengan query parameter (*D*). | Kuliah + Praktikum | **150'** | • **List**: `GET /api/books?page=1&limit=10`<br>• **Pagination**: Offset-based (`page`, `limit`, `total`, `pages`)<br>• **Filter**: `?category=Fiction&year=2023`<br>• **Search**: `?search=Harry Potter`<br>• **Sorting**: `?sort_by=title&order=asc`<br>• Query Builder Pattern<br>• Response Meta (pagination info) | — |
| **6** | Sub-3.1 | **Autentikasi JWT (Register & Login)** | Mahasiswa (*A*) mampu mengimplementasikan autentikasi JWT (register, login, token generation) (*B*) pada endpoint auth (*C*) secara aman sesuai standar bcrypt hashing (*D*). | Kuliah + Praktikum | **150'** | • User Model (username, password_hash, role)<br>• Password Hashing `bcrypt.hashpw()`<br>• User Registration Endpoint `/api/auth/register`<br>• Login Endpoint `/api/auth/login`<br>• JWT Token Generation `PyJWT`<br>• Token Response Format | — |
| **7** | Sub-3.2 | **Otorisasi RBAC (Admin & User)** | Mahasiswa (*A*) mampu mengimplementasikan otorisasi role-based (Admin & User) pada protected endpoint (*B*) menggunakan decorator `@require_role()` (*C*) secara aman dan fungsional (*D*). | Kuliah + Praktikum | **150'** | • JWT Token Verification `jwt.decode()`<br>• Decorator `@token_required`<br>• Role-Based Decorator `@require_role('admin')`<br>• Protected Endpoint (Admin-only, User-only)<br>• Authorization Header `Bearer <token>`<br>• Error Handling (401 Unauthorized, 403 Forbidden) | — |
| **8** | CPMK-1, 2, 3 | **📝 UJIAN TENGAH SEMESTER (UTS)** | Mahasiswa (*A*) mendemonstrasikan penguasaan CPMK-1, CPMK-2, dan CPMK-3 (*B*) melalui ujian praktikum (*C*) dengan kriteria ketuntasan minimal 70% (*D*). | **Ujian Praktikum** | **150'** | **Soal UTS:**<br>• Membangun API Task Management<br>• Database: Users, Tasks (relationship)<br>• Auth: Register, Login, JWT<br>• CRUD Tasks dengan authorization<br>• **CRUDLFIX**: List + Pagination + Filter by status<br>• Admin dapat delete semua tasks<br>• User hanya dapat CRUD tasks miliknya | **📝 UTS**<br>**(25%)**<br><br>*Praktikum Closed-Book* |
| **9** | Sub-4.1 | **API Documentation dengan Flask-RESTX** | Mahasiswa (*A*) mampu membuat dokumentasi API sederhana dengan Flask-RESTX (Swagger auto-generate) (*B*) pada aplikasi Flask (*C*) secara otomatis dan interaktif (*D*). | Kuliah + Praktikum | **150'** | • Flask-RESTX Setup<br>• API Namespace Definition<br>• Model Serialization `api.model()`<br>• Swagger Decorators `@api.doc()`, `@api.expect()`<br>• Swagger UI `/api/docs`<br>• Request/Response Schema | — |
| **10** | Sub-4.1 (Extended) | **CRUDLFIX: Import & Export Data** ⭐ | Mahasiswa (*A*) mampu mengimplementasikan **Import CSV/Excel** dan **Export CSV/JSON** (*B*) pada endpoint API (*C*) secara aman dengan validasi data (*D*). | Kuliah + Praktikum | **150'** | • **Import CSV**: `POST /api/books/import` (multipart/form-data)<br>• Parse CSV dengan `pandas` atau `csv` module<br>• Bulk Insert dengan SQLAlchemy `db.session.bulk_insert_mappings()`<br>• Validasi data import (schema validation)<br>• **Export CSV**: `GET /api/books/export?format=csv`<br>• **Export JSON**: `GET /api/books/export?format=json`<br>• Response Header `Content-Disposition: attachment`<br>• Streaming large data | — |
| **11** | Sub-4.2 | **Deployment ke Heroku** | Mahasiswa (*A*) mampu men-deploy aplikasi Flask ke Heroku dengan environment variable configuration (*B*) secara fungsional dan dapat diakses publik (*C*) dengan URL live (*D*). | Kuliah + Demo + Praktikum | **150'** | • Heroku Account Setup<br>• Heroku CLI Installation<br>• `Procfile` Configuration<br>• `requirements.txt` Generation<br>• Gunicorn WSGI Server<br>• Environment Variables Config<br>• `heroku create` & `git push heroku main`<br>• Database: Heroku Postgres Add-on | — |
| **12** | Seluruh CPMK | **Capstone Project: Library Management System API (Part 1)** | Mahasiswa (*A*) mampu membangun Capstone Project Library Management System API (Part 1: Planning & Database Design) (*B*) secara kolaboratif dalam tim (*C*) dengan spesifikasi yang jelas (*D*). | **Project-Based Learning** | **150'** | **Capstone Project Kickoff:**<br>• Domain Analysis (Library System)<br>• Database Design (ERD)<br>• API Endpoint Planning (13 endpoints)<br>• User Stories & Acceptance Criteria<br>• GitHub Repository Setup<br>• Sprint Planning (2 minggu) | **📋 Tugas 2**<br>**(25%)**<br><br>*Library Management System API*<br>(Capstone Project)<br><br>Deadline:<br>Pekan 15<br><br>Presentasi:<br>Pekan 15 |
| **13** | Seluruh CPMK | **Capstone Project: Library Management System API (Part 2)** | Mahasiswa (*A*) mampu mengimplementasikan backend logic dan database integration (*B*) sesuai rancangan database dan API endpoint (*C*) secara fungsional (*D*). | **Project-Based Learning + Konsultasi** | **150'** | **Development Sprint:**<br>• Model Definition (4 models)<br>• CRUD Operations (Books, Members, Authors, Loans)<br>• Relationship Implementation<br>• Authentication & Authorization<br>• Testing dengan Postman<br>• Bug Fixing & Code Review | — |
| **14** | Seluruh CPMK | **Capstone Project: Library Management System API (Part 3)** | Mahasiswa (*A*) mampu menyelesaikan dokumentasi API dan deployment ke Heroku (*B*) sesuai acceptance criteria (*C*) dengan URL live yang fungsional (*D*). | **Project-Based Learning + Konsultasi** | **150'** | **Finalisasi Project:**<br>• Flask-RESTX Documentation<br>• Input Validation Implementation<br>• Security Checklist Review<br>• Heroku Deployment<br>• Testing Live API<br>• README.md Documentation | — |
| **15** | Seluruh CPMK | **Presentasi & Demo Capstone Project** | Mahasiswa (*A*) mempresentasikan hasil Capstone Project (*B*) di hadapan dosen dan rekan (*C*) secara profesional dengan live demo (*D*). | **Presentasi + Demo** | **150'** | **Presentation Day:**<br>• Live Demo API (15 menit per tim)<br>• Penjelasan Arsitektur<br>• Demo Authentication Flow<br>• Demo CRUD Operations<br>• Q&A Session<br>• Peer Review | — |
| **16** | Seluruh CPMK | **📝 UJIAN AKHIR SEMESTER (UAS)** | Mahasiswa (*A*) mendemonstrasikan penguasaan seluruh CPMK (*B*) melalui ujian praktikum komprehensif (*C*) dengan kriteria ketuntasan minimal 70% (*D*). | **Ujian Praktikum Komprehensif** | **150'** | **Soal UAS:**<br>• Membangun API E-Book Store<br>• Auth + RBAC (Admin, Customer)<br>• CRUD Books, Orders, Reviews<br>• Relationship (Books ↔ Categories, Orders ↔ Books)<br>• Flask-RESTX Documentation<br>• Deploy ke Heroku<br>• Submit: GitHub Repo + Live URL | **📝 UAS**<br>**(30%)**<br><br>*Praktikum Komprehensif* |

**Total Waktu Pembelajaran:** 16 pekan × 150 menit = **2,400 menit** = **40 jam tatap muka**

---

### 2.2 METODE PEMBELAJARAN

Mata kuliah ini menggunakan kombinasi metode:

1. **Kuliah Interaktif (20%)** — Penjelasan konsep fundamental backend, REST API, ORM, security
2. **Praktikum Terbimbing (50%)** — Live coding bersama dosen, hands-on implementation
3. **Project-Based Learning (20%)** — Capstone Project Library Management System API
4. **Diskusi & Konsultasi (10%)** — Problem-solving session, code review, debugging

**Pendekatan:**
- **Learning by Doing** — Setiap konsep langsung dipraktikkan
- **Incremental Complexity** — Dimulai dari Flask sederhana, bertahap menambah fitur
- **Guided Tutorial** — Dosen menyediakan starter code dan step-by-step guide
- **Peer Learning** — Capstone project dikerjakan berpasangan (2 orang)

---

### 2.3 SUMBER BELAJAR

#### A. Wajib
- Flask Official Documentation: https://flask.palletsprojects.com
- SQLAlchemy Tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
- JWT.io Introduction: https://jwt.io/introduction

#### B. Pendukung
- Video Tutorial: Corey Schafer — Flask Tutorials (YouTube)
- Video Tutorial: Tech With Tim — Flask REST API (YouTube)
- Buku: *Flask Web Development* oleh Miguel Grinberg (Chapter 1-8)

---

## BAGIAN III: KOMPONEN PENILAIAN & RUBRIK

### 3.1 SKEMA ASESMEN (TOTAL 100%)

| Komponen | Pekan | Bentuk Asesmen | Cakupan CPMK | Bobot |
|----------|:-----:|----------------|:------------:|:-----:|
| **Tugas 1** | 4 | Penugasan Praktikum | CPMK-1 (Sub 1.1, 1.2) | **20%** |
| **UTS** | 8 | Ujian Praktikum | CPMK-1, CPMK-2, CPMK-3 | **25%** |
| **Tugas 2** | 12-15 | Capstone Project + Presentasi | Seluruh CPMK (1, 2, 3, 4) | **25%** |
| **UAS** | 16 | Ujian Praktikum Komprehensif | Seluruh CPMK (1, 2, 3, 4) | **30%** |
| **TOTAL** | — | — | — | **100%** |

**Catatan:**
- Seluruh asesmen berbentuk **praktikum coding** (tidak ada ujian teori tertulis)
- Mahasiswa wajib submit **source code** dan **live URL** untuk setiap asesmen
- Keterlambatan submit: **-10% per hari** (maksimal 3 hari)

---

### 3.2 KRITERIA PENILAIAN

Setiap asesmen dinilai berdasarkan **6 kriteria** dengan bobot berbeda:

| No | Kriteria Penilaian | Bobot | Deskripsi |
|:--:|-------------------|:-----:|-----------|
| 1 | **Fungsionalitas** | **40%** | API endpoint berfungsi sesuai spesifikasi, tidak ada bug kritis |
| 2 | **Kualitas Kode** | **20%** | Kode terstruktur, readable, mengikuti PEP 8, ada komentar |
| 3 | **Database & ORM** | **15%** | Model database benar, relationship tepat, CRUD efisien |
| 4 | **Keamanan** | **15%** | Password hashing, JWT valid, input validation, RBAC benar |
| 5 | **Dokumentasi** | **5%** | README jelas, Flask-RESTX (untuk Tugas 2 & UAS) |
| 6 | **Deployment** | **5%** | Live URL accessible, environment config benar (untuk Tugas 2 & UAS) |

---

### 3.3 RUBRIK PENILAIAN

#### Rubrik Fungsionalitas (40%)

| Level | Skor | Deskripsi |
|:-----:|:----:|-----------|
| **Sangat Baik** | **86-100** | Semua endpoint berfungsi sempurna, tidak ada bug, response format konsisten |
| **Baik** | **76-85** | Semua endpoint berfungsi, ada bug minor yang tidak mengganggu fungsi utama |
| **Cukup** | **66-75** | Sebagian besar endpoint (≥70%) berfungsi, ada bug yang cukup mengganggu |
| **Kurang** | **56-65** | Hanya sebagian endpoint (<70%) yang berfungsi, banyak bug |
| **Sangat Kurang** | **0-55** | Aplikasi tidak berjalan sama sekali atau error fatal |

#### Rubrik Kualitas Kode (20%)

| Level | Skor | Deskripsi |
|:-----:|:----:|-----------|
| **Sangat Baik** | **86-100** | Kode modular (Blueprint), PEP 8 compliant, komentar jelas, no code smell |
| **Baik** | **76-85** | Kode terstruktur dengan baik, sebagian besar mengikuti PEP 8, ada komentar |
| **Cukup** | **66-75** | Kode dapat dipahami, ada struktur dasar, komentar minimal |
| **Kurang** | **56-65** | Kode berantakan, sulit dibaca, tidak ada komentar |
| **Sangat Kurang** | **0-55** | Kode tidak terstruktur, copy-paste tanpa pemahaman |

#### Rubrik Database & ORM (15%)

| Level | Skor | Deskripsi |
|:-----:|:----:|-----------|
| **Sangat Baik** | **86-100** | Model database optimal, relationship benar, query efisien, normalisasi tepat |
| **Baik** | **76-85** | Model database benar, relationship tepat, query cukup efisien |
| **Cukup** | **66-75** | Model database dasar benar, relationship sederhana berfungsi |
| **Kurang** | **56-65** | Model database ada error, relationship tidak tepat |
| **Sangat Kurang** | **0-55** | Model database salah total atau tidak ada database sama sekali |

#### Rubrik Keamanan (15%)

| Level | Skor | Deskripsi |
|:-----:|:----:|-----------|
| **Sangat Baik** | **86-100** | Password hashing bcrypt, JWT secure, input validation lengkap, RBAC robust, CORS configured |
| **Baik** | **76-85** | Password hashing ada, JWT benar, input validation dasar, RBAC berfungsi |
| **Cukup** | **66-75** | Password hashing ada, JWT basic, RBAC sederhana berfungsi |
| **Kurang** | **56-65** | Password plaintext (FATAL), JWT tidak aman, RBAC broken |
| **Sangat Kurang** | **0-55** | Tidak ada security mechanism sama sekali |

#### Rubrik Dokumentasi (5%)

| Level | Skor | Deskripsi |
|:-----:|:----:|-----------|
| **Sangat Baik** | **86-100** | README lengkap (setup, endpoint, Swagger), Flask-RESTX auto-doc sempurna |
| **Baik** | **76-85** | README ada (setup, endpoint), Flask-RESTX basic |
| **Cukup** | **66-75** | README minimal (setup saja) |
| **Kurang** | **56-65** | README sangat minim |
| **Sangat Kurang** | **0-55** | Tidak ada dokumentasi sama sekali |

#### Rubrik Deployment (5%)

| Level | Skor | Deskripsi |
|:-----:|:----:|-----------|
| **Sangat Baik** | **86-100** | Deployed ke Heroku, URL accessible, database production berfungsi, env config aman |
| **Baik** | **76-85** | Deployed ke Heroku, URL accessible, ada minor issue |
| **Cukup** | **66-75** | Deployed tapi sering down atau ada issue signifikan |
| **Kurang** | **56-65** | Deployed tapi tidak berfungsi dengan baik |
| **Sangat Kurang** | **0-55** | Tidak di-deploy sama sekali |

---

### 3.4 KONVERSI NILAI AKHIR

| Nilai Angka | Nilai Huruf | Bobot | Predikat |
|:-----------:|:-----------:|:-----:|----------|
| **86 – 100** | **A** | 4.00 | Sangat Baik (Excellent) |
| **76 – 85** | **B+** | 3.50 | Baik Sekali (Very Good) |
| **70 – 75** | **B** | 3.00 | Baik (Good) |
| **66 – 69** | **C+** | 2.50 | Cukup Baik (Fairly Good) |
| **60 – 65** | **C** | 2.00 | Cukup (Fair) — **Batas Lulus** |
| **56 – 59** | **D** | 1.00 | Kurang (Poor) — **Tidak Lulus** |
| **0 – 55** | **E** | 0.00 | Sangat Kurang (Fail) |

**Syarat Kelulusan:**
- Nilai minimal **C (60)** untuk dapat lulus mata kuliah
- Kehadiran minimal **75%** dari total pertemuan (12 dari 16 pertemuan)

---

## BAGIAN III.B: PEMBAHASAN KHUSUS — CRUDLFIX (CRUD EXTENDED)

### 3B.1 APA ITU CRUDLFIX?

**CRUDLFIX** adalah ekstensi dari operasi CRUD standar yang mencakup fitur-fitur enterprise-ready untuk aplikasi backend modern:

| Operasi | Keterangan | HTTP Method | Contoh Endpoint |
|:-------:|-----------|:-----------:|-----------------|
| **C** | **Create** — Membuat data baru | `POST` | `POST /api/books` |
| **R** | **Read** — Membaca data tunggal | `GET` | `GET /api/books/1` |
| **U** | **Update** — Memperbarui data | `PUT/PATCH` | `PUT /api/books/1` |
| **D** | **Delete** — Menghapus data | `DELETE` | `DELETE /api/books/1` |
| **L** | **List** — Daftar data dengan pagination | `GET` | `GET /api/books?page=1&limit=10` |
| **F** | **Filter** — Filter & search data | `GET` | `GET /api/books?category=Fiction&search=Harry` |
| **I** | **Import** — Import data bulk (CSV/Excel) | `POST` | `POST /api/books/import` (multipart) |
| **X** | **eXport** — Export data (CSV/JSON/Excel) | `GET` | `GET /api/books/export?format=csv` |

### 3B.2 MENGAPA CRUDLFIX PENTING?

**Aplikasi backend enterprise memerlukan:**
1. ✅ **Pagination** — Menampilkan data besar secara bertahap (tidak load semua sekaligus)
2. ✅ **Filter & Search** — User bisa mencari data spesifik (filter by category, search by keyword)
3. ✅ **Sorting** — Urutkan data (by name ASC, by date DESC)
4. ✅ **Import Bulk** — Admin bisa upload data massal via CSV/Excel (efisiensi)
5. ✅ **Export Data** — User/Admin bisa download data untuk analisis/reporting

**Tanpa CRUDLFIX:**
- ❌ API hanya bisa CRUD basic → tidak production-ready
- ❌ Load semua data sekaligus → performance issue
- ❌ Tidak ada search → user experience buruk
- ❌ Input data manual satu-satu → tidak efisien

**Dengan CRUDLFIX:**
- ✅ API production-ready & scalable
- ✅ Performance optimal (pagination)
- ✅ User experience excellent (search & filter)
- ✅ Data management efisien (import/export)

---

### 3B.3 IMPLEMENTASI LIST WITH PAGINATION

#### Konsep Pagination

**Offset-based Pagination:**
- Parameter: `page` (halaman ke-berapa) & `limit` (jumlah data per halaman)
- Formula: `offset = (page - 1) * limit`
- Response: data + metadata (total records, total pages, current page)

**Contoh Request:**
```http
GET /api/books?page=2&limit=10
```

**Contoh Implementation (Flask):**
```python
from flask import request, jsonify

@app.route('/api/books', methods=['GET'])
def get_books_paginated():
    # Get query parameters
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    # Calculate offset
    offset = (page - 1) * limit
    
    # Query with pagination
    books = Book.query.offset(offset).limit(limit).all()
    total = Book.query.count()
    
    # Calculate total pages
    total_pages = (total + limit - 1) // limit
    
    # Response with metadata
    return jsonify({
        'data': [book.to_dict() for book in books],
        'meta': {
            'page': page,
            'limit': limit,
            'total': total,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1
        }
    }), 200
```

**Contoh Response:**
```json
{
  "data": [
    {"id": 11, "title": "Book 11", "author": "Author A"},
    {"id": 12, "title": "Book 12", "author": "Author B"},
    ...
  ],
  "meta": {
    "page": 2,
    "limit": 10,
    "total": 45,
    "total_pages": 5,
    "has_next": true,
    "has_prev": true
  }
}
```

---

### 3B.4 IMPLEMENTASI FILTER & SEARCH

#### Konsep Filter

**Dynamic Query Building:**
- Filter by field: `?category=Fiction`
- Filter multiple: `?category=Fiction&year=2023`
- Search keyword: `?search=Harry Potter`
- Sorting: `?sort_by=title&order=asc`

**Contoh Request:**
```http
GET /api/books?category=Fiction&year=2023&search=Harry&sort_by=title&order=asc&page=1&limit=10
```

**Contoh Implementation (Flask):**
```python
@app.route('/api/books', methods=['GET'])
def get_books_filtered():
    # Start with base query
    query = Book.query
    
    # Filter by category
    category = request.args.get('category')
    if category:
        query = query.filter(Book.category == category)
    
    # Filter by year
    year = request.args.get('year', type=int)
    if year:
        query = query.filter(Book.year == year)
    
    # Search by title or author (LIKE)
    search = request.args.get('search')
    if search:
        search_pattern = f'%{search}%'
        query = query.filter(
            (Book.title.like(search_pattern)) | 
            (Book.author.like(search_pattern))
        )
    
    # Sorting
    sort_by = request.args.get('sort_by', 'id')
    order = request.args.get('order', 'asc')
    
    if order == 'desc':
        query = query.order_by(getattr(Book, sort_by).desc())
    else:
        query = query.order_by(getattr(Book, sort_by).asc())
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    offset = (page - 1) * limit
    
    books = query.offset(offset).limit(limit).all()
    total = query.count()
    total_pages = (total + limit - 1) // limit
    
    return jsonify({
        'data': [book.to_dict() for book in books],
        'meta': {
            'page': page,
            'limit': limit,
            'total': total,
            'total_pages': total_pages,
            'filters_applied': {
                'category': category,
                'year': year,
                'search': search,
                'sort_by': sort_by,
                'order': order
            }
        }
    }), 200
```

---

### 3B.5 IMPLEMENTASI IMPORT DATA (CSV/EXCEL)

#### Konsep Import Bulk

**Use Case:**
- Admin perlu upload 1000 buku dari file Excel/CSV
- Manual input satu-satu tidak efisien
- Import bulk: upload file → parse → validate → insert ke database

**Contoh Request:**
```http
POST /api/books/import
Content-Type: multipart/form-data

file: books.csv
```

**Format CSV (books.csv):**
```csv
title,author,isbn,year,category
"Harry Potter","J.K. Rowling","978-0439708180",1997,"Fantasy"
"The Hobbit","J.R.R. Tolkien","978-0547928227",1937,"Fantasy"
"1984","George Orwell","978-0451524935",1949,"Dystopian"
```

**Contoh Implementation (Flask):**
```python
import csv
import io
from flask import request, jsonify

@app.route('/api/books/import', methods=['POST'])
@require_role('admin')  # Only admin can import
def import_books():
    # Check if file exists
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'Only CSV files allowed'}), 400
    
    try:
        # Read CSV file
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_reader = csv.DictReader(stream)
        
        books_to_insert = []
        errors = []
        
        for row_num, row in enumerate(csv_reader, start=2):
            # Validate each row
            try:
                book_data = {
                    'title': row['title'],
                    'author': row['author'],
                    'isbn': row['isbn'],
                    'year': int(row['year']),
                    'category': row['category']
                }
                
                # Check if ISBN already exists
                if Book.query.filter_by(isbn=book_data['isbn']).first():
                    errors.append({
                        'row': row_num,
                        'error': f"ISBN {book_data['isbn']} already exists"
                    })
                    continue
                
                books_to_insert.append(book_data)
                
            except (KeyError, ValueError) as e:
                errors.append({
                    'row': row_num,
                    'error': str(e)
                })
        
        # Bulk insert using SQLAlchemy
        if books_to_insert:
            db.session.bulk_insert_mappings(Book, books_to_insert)
            db.session.commit()
        
        return jsonify({
            'message': f'Successfully imported {len(books_to_insert)} books',
            'imported': len(books_to_insert),
            'errors': errors
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
```

**Response Success:**
```json
{
  "message": "Successfully imported 2 books",
  "imported": 2,
  "errors": [
    {
      "row": 4,
      "error": "ISBN 978-0451524935 already exists"
    }
  ]
}
```

---

### 3B.6 IMPLEMENTASI EXPORT DATA (CSV/JSON)

#### Konsep Export

**Use Case:**
- User/Admin perlu download semua data buku untuk reporting
- Export format: CSV (untuk Excel) atau JSON (untuk analisis)

**Contoh Request:**
```http
GET /api/books/export?format=csv
GET /api/books/export?format=json
```

**Contoh Implementation (Flask):**
```python
import csv
from io import StringIO, BytesIO
from flask import Response

@app.route('/api/books/export', methods=['GET'])
@token_required
def export_books():
    format_type = request.args.get('format', 'csv')
    
    # Get all books (or apply filters)
    books = Book.query.all()
    
    if format_type == 'csv':
        # Create CSV in memory
        si = StringIO()
        csv_writer = csv.writer(si)
        
        # Write header
        csv_writer.writerow(['ID', 'Title', 'Author', 'ISBN', 'Year', 'Category'])
        
        # Write data
        for book in books:
            csv_writer.writerow([
                book.id,
                book.title,
                book.author,
                book.isbn,
                book.year,
                book.category
            ])
        
        # Create response
        output = si.getvalue()
        si.close()
        
        return Response(
            output,
            mimetype='text/csv',
            headers={
                'Content-Disposition': 'attachment; filename=books_export.csv'
            }
        )
    
    elif format_type == 'json':
        # Export as JSON
        books_data = [book.to_dict() for book in books]
        
        return Response(
            jsonify(books_data).data,
            mimetype='application/json',
            headers={
                'Content-Disposition': 'attachment; filename=books_export.json'
            }
        )
    
    else:
        return jsonify({'error': 'Invalid format. Use csv or json'}), 400
```

**Response CSV:**
```csv
ID,Title,Author,ISBN,Year,Category
1,"Harry Potter","J.K. Rowling","978-0439708180",1997,"Fantasy"
2,"The Hobbit","J.R.R. Tolkien","978-0547928227",1937,"Fantasy"
```

**Response JSON:**
```json
[
  {
    "id": 1,
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "isbn": "978-0439708180",
    "year": 1997,
    "category": "Fantasy"
  },
  {
    "id": 2,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "isbn": "978-0547928227",
    "year": 1937,
    "category": "Fantasy"
  }
]
```

---

### 3B.7 BEST PRACTICES CRUDLFIX

#### 1. Pagination Best Practices
✅ **DO:**
- Selalu sediakan pagination untuk endpoint list
- Default limit: 10-50 (tidak terlalu besar)
- Maksimal limit: 100 (cegah overload)
- Sertakan metadata (total, pages, has_next, has_prev)

❌ **DON'T:**
- Return semua data tanpa pagination (performance issue)
- Allow unlimited limit (security risk)

#### 2. Filter & Search Best Practices
✅ **DO:**
- Gunakan query parameter (`?filter=value`)
- Support multiple filters (AND logic)
- Escape special characters (prevent SQL injection)
- Use ORM `.filter()` (auto-escape)

❌ **DON'T:**
- Filter menggunakan raw SQL (SQL injection risk)
- Ignore case sensitivity untuk search (gunakan `.ilike()` di PostgreSQL)

#### 3. Import Best Practices
✅ **DO:**
- Validate setiap row sebelum insert
- Gunakan bulk insert (efisien)
- Return error detail per row
- Rollback jika ada error critical
- Limit file size (max 10MB)

❌ **DON'T:**
- Insert tanpa validasi (data corruption)
- Allow file size unlimited (DoS attack)
- Insert satu-satu dalam loop (slow)

#### 4. Export Best Practices
✅ **DO:**
- Support multiple format (CSV, JSON, Excel)
- Set proper headers (`Content-Disposition: attachment`)
- Stream large data (tidak load semua ke memory)
- Apply same authorization (user bisa export data miliknya)

❌ **DON'T:**
- Load semua data ke memory (out of memory)
- Allow export tanpa authentication (data leak)

---

### 3B.8 PERFORMA OPTIMIZATION

#### Problem: N+1 Query

**Bad Practice (N+1 Query):**
```python
# 1 query untuk get all books
books = Book.query.all()

# N queries untuk get author tiap book (N+1 problem!)
for book in books:
    print(book.author.name)  # Trigger separate query per book
```

**Total Queries:** 1 + N = 1 + 100 = **101 queries** (SLOW!)

**Good Practice (Eager Loading):**
```python
# 1 query dengan JOIN (eager loading)
books = Book.query.options(db.joinedload(Book.author)).all()

# No additional queries!
for book in books:
    print(book.author.name)  # Already loaded
```

**Total Queries:** **1 query** (FAST!)

**SQLAlchemy Eager Loading:**
```python
# Option 1: joinedload (LEFT OUTER JOIN)
books = Book.query.options(db.joinedload(Book.author)).all()

# Option 2: subqueryload (subquery)
books = Book.query.options(db.subqueryload(Book.author)).all()

# Option 3: selectinload (IN query) - recommended
books = Book.query.options(db.selectinload(Book.author)).all()
```

---

### 3B.9 SECURITY CONSIDERATIONS

#### 1. Import Security
✅ **Validate file type** (only CSV/Excel)
✅ **Limit file size** (max 10MB)
✅ **Validate data schema** (marshmallow)
✅ **Sanitize input** (escape special characters)
✅ **Check for duplicate** (ISBN, email, etc.)

#### 2. Export Security
✅ **Authentication required** (JWT token)
✅ **Authorization check** (user can only export own data, admin can export all)
✅ **Rate limiting** (prevent abuse)
✅ **Audit log** (track who export what data)

#### 3. Filter Security
✅ **Use ORM filter** (prevent SQL injection)
✅ **Whitelist allowed fields** (prevent arbitrary field access)
✅ **Sanitize search input** (prevent XSS)

---

### 3B.10 SUMMARY CRUDLFIX

| Operasi | Tujuan | HTTP | Contoh Endpoint | Complexity |
|:-------:|--------|:----:|-----------------|:----------:|
| **C** | Create single record | POST | `/api/books` | ⭐ Easy |
| **R** | Read single record | GET | `/api/books/1` | ⭐ Easy |
| **U** | Update single record | PUT | `/api/books/1` | ⭐ Easy |
| **D** | Delete single record | DELETE | `/api/books/1` | ⭐ Easy |
| **L** | List with pagination | GET | `/api/books?page=1&limit=10` | ⭐⭐ Medium |
| **F** | Filter & search | GET | `/api/books?category=Fiction&search=Harry` | ⭐⭐ Medium |
| **I** | Import bulk (CSV) | POST | `/api/books/import` | ⭐⭐⭐ Hard |
| **X** | Export (CSV/JSON) | GET | `/api/books/export?format=csv` | ⭐⭐ Medium |

**Learning Path:**
1. **Pekan 2-5:** Master CRUD basic (C, R, U, D)
2. **Pekan 6:** Learn List with Pagination (L)
3. **Pekan 6:** Learn Filter & Search (F)
4. **Pekan 10:** Learn Import & Export (I, X)
5. **Pekan 12-15:** Apply CRUDLFIX on Capstone Project

**By End of Semester:**
- ✅ Mahasiswa dapat build **production-ready API** dengan CRUDLFIX complete
- ✅ Mahasiswa paham **performance optimization** (pagination, eager loading)
- ✅ Mahasiswa paham **security best practices** (validation, sanitization)
- ✅ Mahasiswa punya **portofolio backend** yang impressive

---

## BAGIAN IV: BOUNDARY GUARDRAILS (DEMARKASI SILABUS)

### 4.1 IN-SCOPE (WAJIB DIAJARKAN) ✅

Topik-topik berikut adalah **kewenangan mata kuliah STI-416** dan **WAJIB** diajarkan oleh dosen pengampu:

#### A. Flask Fundamental
✅ Flask application structure (`app = Flask(__name__)`)  
✅ Routing dengan `@app.route()` decorator  
✅ HTTP methods (GET, POST, PUT, DELETE)  
✅ Request handling (`request.get_json()`, `request.args`, `request.form`)  
✅ Response handling (`jsonify()`, status codes)  

#### B. RESTful API Design
✅ Resource-oriented endpoint design (`/api/books`, `/api/books/<id>`)  
✅ HTTP status codes (200, 201, 400, 401, 403, 404, 500)  
✅ JSON request dan response format  
✅ Error handling dan error response standardization  

#### C. Database Integration (SQLAlchemy ORM)
✅ Flask-SQLAlchemy setup dan configuration  
✅ Database URI (SQLite untuk development, MySQL/Postgres untuk production)  
✅ Model definition (`db.Model`, `db.Column`, `db.String`, `db.Integer`, etc.)  
✅ Database migration dengan Flask-Migrate  
✅ CRUD operations (`db.session.add()`, `.commit()`, `.query.all()`, `.filter()`, `.delete()`)  
✅ Relationship (One-to-Many, Many-to-One, Foreign Key)  

#### D. Authentication & Authorization
✅ User model (username, password_hash, role)  
✅ Password hashing dengan `bcrypt`  
✅ User registration (`/api/auth/register`)  
✅ User login (`/api/auth/login`)  
✅ JWT token generation (`PyJWT`)  
✅ JWT token verification (`jwt.decode()`)  
✅ Token-based authentication decorator (`@token_required`)  
✅ Role-based authorization (Admin & User) decorator (`@require_role('admin')`)  
✅ Protected endpoint (hanya bisa diakses dengan valid token)  

#### E. Security Best Practices
✅ Password hashing (NEVER store plaintext password)  
✅ SQL injection prevention (ORM auto-escape)  
✅ Input validation (marshmallow atau Flask-Inputs)  
✅ CORS configuration (`flask-cors`)  
✅ Environment variable management (`.env` + `python-decouple`)  

#### F. API Documentation
✅ Flask-RESTX setup dan namespace  
✅ Swagger UI auto-generation (`/api/docs`)  
✅ API model definition (`api.model()`)  
✅ Swagger decorators (`@api.doc()`, `@api.expect()`, `@api.marshal_with()`)  

#### G. Deployment
✅ Heroku account setup dan Heroku CLI  
✅ `Procfile` configuration  
✅ `requirements.txt` generation  
✅ Gunicorn WSGI server  
✅ Environment variables di Heroku  
✅ Heroku Postgres add-on  
✅ Deploy dengan `git push heroku main`  

---

### 4.2 OUT-OF-SCOPE (DILARANG DIAJARKAN) ❌

Topik-topik berikut **TIDAK BOLEH** diajarkan di STI-416 karena menjadi kewenangan mata kuliah lain atau terlalu kompleks untuk mahasiswa semester 4:

#### A. Front-End Development (Kewenangan STI-311)
❌ HTML, CSS, JavaScript front-end development  
❌ React, Vue, Angular framework  
❌ UI/UX design dan prototyping  
❌ Client-side routing dan state management  

#### B. Advanced Backend Architecture (Terlalu Kompleks)
❌ Microservices architecture  
❌ Message queue (RabbitMQ, Kafka)  
❌ Event-driven architecture  
❌ CQRS pattern  
❌ GraphQL API (bukan RESTful)  

#### C. Container Orchestration (Kewenangan STI-727 / STB-601)
❌ Docker Compose multi-container  
❌ Kubernetes orchestration  
❌ Service mesh (Istio, Linkerd)  
❌ CI/CD pipeline automation (Jenkins, GitLab CI)  

#### D. Advanced Database (Kewenangan FST-207 / STI-415)
❌ Database normalisasi theory (sudah di FST-207)  
❌ Complex query optimization  
❌ Database sharding dan replication  
❌ NoSQL database (MongoDB, Cassandra)  
❌ Data warehouse design (sudah di STI-415)  

#### E. Advanced Security (Kewenangan STI-418 / STI-519)
❌ OAuth2 authorization server implementation (terlalu kompleks)  
❌ Cryptography algorithms detail  
❌ Penetration testing dan vulnerability assessment  
❌ Network security dan firewall configuration  

#### F. Mobile App Development (Kewenangan STI-522)
❌ Flutter, React Native development  
❌ Mobile-specific API design  
❌ Push notification implementation  

---

### 4.3 HANDOFF ANCHOR (TITIK SERAH TERIMA KOMPETENSI) 🔄

Mata kuliah STI-416 menjadi **fondasi** untuk mata kuliah berikutnya dengan serah terima kompetensi sebagai berikut:

#### A. Dari STI-416 → STI-522 (Pemrograman Aplikasi Mobile)
🔄 **Serah Terima:** Backend API andal dan terdokumentasi (Flask API)  
✅ **Yang Diterima STI-522:** Mahasiswa datang dengan kemampuan membangun RESTful API  
✅ **Fokus STI-522:** Konsumsi API dari mobile app (Flutter/React Native), HTTP client, state management  

#### B. Dari STI-416 → STI-625 (Rekayasa Platform Digital)
🔄 **Serah Terima:** Pemahaman backend single-service sederhana  
✅ **Yang Diterima STI-625:** Mahasiswa paham routing, database, auth dasar  
✅ **Fokus STI-625:** Arsitektur platform kompleks multi-service, API Gateway, service communication  

#### C. Dari STI-416 → STI-727 (Integrasi Layanan Cerdas Berbasis AI)
🔄 **Serah Terima:** Backend API deployment ke cloud production  
✅ **Yang Diterima STI-727:** Mahasiswa bisa deploy Flask app ke Heroku  
✅ **Fokus STI-727:** Orkestrasi layanan terdistribusi, microservices, Docker Compose, Kubernetes  

#### D. Dari STI-416 → STB-601 (Arsitektur Cloud & DevOps)
🔄 **Serah Terima:** Deployment manual ke Heroku (PaaS)  
✅ **Yang Diterima STB-601:** Mahasiswa pernah deploy ke cloud  
✅ **Fokus STB-601:** Infrastructure as Code (IaC), Docker container, Kubernetes, CI/CD pipeline  

#### E. Dari FST-207 → STI-416 (Prasyarat Database)
🔄 **Yang Diterima STI-416:** Mahasiswa sudah paham SQL, RDBMS, normalisasi  
✅ **Fokus STI-416:** Abstraksi database ke ORM (SQLAlchemy), tidak lagi menulis raw SQL  

#### F. Dari STI-311 → STI-416 (Prasyarat Web Front End)
🔄 **Yang Diterima STI-416:** Mahasiswa sudah paham HTTP protocol, REST API consumption (fetch/axios)  
✅ **Fokus STI-416:** Backend API provider, bukan consumer  

---

### 4.4 RATIONALE PENYEDERHANAAN (V2 vs V1)

| Aspek | V1 (Original) | V2 (Simplified) | Alasan Penyederhanaan |
|-------|---------------|-----------------|------------------------|
| **Framework** | Node.js/Express **ATAU** FastAPI | **Flask ONLY** | ✅ Python lebih familiar bagi mahasiswa semester 4<br>✅ Flask lebih sederhana dan minimalis<br>✅ Dokumentasi Flask lebih ramah pemula |
| **ORM** | Sequelize (Node) / Prisma (Node) / SQLAlchemy (Python) | **Flask-SQLAlchemy ONLY** | ✅ Flask-SQLAlchemy built-in dan terintegrasi sempurna<br>✅ Dokumentasi lengkap dan contoh banyak<br>✅ Tidak perlu belajar ORM lain di luar ekosistem Flask |
| **Auth** | JWT + OAuth2 + Multi-level RBAC | **JWT + 2-Role RBAC** | ✅ OAuth2 terlalu kompleks untuk semester 4<br>✅ 2 role (Admin-User) cukup untuk memahami konsep RBAC<br>✅ Fokus pada fundamental, bukan complexity |
| **Caching** | Redis (external service) | **Flask-Caching (in-memory)** | ✅ Redis memerlukan setup service eksternal (kompleks)<br>✅ Flask-Caching built-in, zero external dependency<br>✅ In-memory cukup untuk pembelajaran |
| **Documentation** | Swagger/OpenAPI manual | **Flask-RESTX (auto-generate)** | ✅ Flask-RESTX otomatis generate Swagger dari code<br>✅ Tidak perlu menulis YAML/JSON OpenAPI spec manual |
| **Deployment** | Docker + Cloud (Railway/GCP/AWS) | **Heroku (one-click)** | ✅ Docker memerlukan pemahaman container yang belum diajarkan<br>✅ Heroku one-click deploy, fokus pada aplikasi bukan infrastruktur<br>✅ Free tier Heroku cukup untuk pembelajaran |
| **Validation** | express-validator (Node) / Pydantic (FastAPI) | **marshmallow (Flask)** | ✅ marshmallow ekosistem Flask, terintegrasi baik<br>✅ Learning curve gentle, dokumentasi jelas |
| **Complexity** | C4-C6 (Advanced) | **C3-C4 (Intermediate)** | ✅ Target mahasiswa motivasi menengah (IPK 2.75-3.25)<br>✅ Fokus pada **konsep fundamental** yang transferable<br>✅ Success rate ditargetkan 85% (vs 50% di V1) |

---

## BAGIAN V: LAMPIRAN INSTRUMEN ASESMEN

### LAMPIRAN A: TUGAS 1 — RESTful API PERPUSTAKAAN SEDERHANA

#### A.1 Deskripsi Tugas

Mahasiswa diminta membangun **RESTful API Perpustakaan Sederhana** dengan Flask yang memiliki fitur manajemen buku (CRUD) tanpa autentikasi.

#### A.2 Spesifikasi Teknis

**Framework:** Python Flask 2.3+  
**Database:** SQLite (tidak perlu setup eksternal)  
**ORM:** Flask-SQLAlchemy  

**Fitur Wajib:**
1. **Model Book** dengan kolom:
   - `id` (Integer, Primary Key, Auto-Increment)
   - `title` (String 200, Not Null)
   - `author` (String 100, Not Null)
   - `year` (Integer, Not Null)
   - `isbn` (String 20, Unique, Not Null)

2. **5 Endpoint CRUD:**
   - `POST /api/books` — Create new book
   - `GET /api/books` — Get all books
   - `GET /api/books/<id>` — Get book by ID
   - `PUT /api/books/<id>` — Update book by ID
   - `DELETE /api/books/<id>` — Delete book by ID

3. **Middleware:**
   - Request logging (print setiap request ke console)
   - CORS enabled untuk semua origin

4. **Error Handling:**
   - 404 Not Found (jika book ID tidak ditemukan)
   - 400 Bad Request (jika input tidak valid)
   - 500 Internal Server Error (jika ada exception)

#### A.3 Deliverables

1. **Source Code** (submit ke GitHub repository):
   - `app.py` (main Flask application)
   - `models.py` (Book model definition)
   - `requirements.txt` (list semua dependency)
   - `README.md` (cara menjalankan aplikasi)

2. **Screenshot Postman** (minimal 5 screenshot):
   - Create Book (POST)
   - Get All Books (GET)
   - Get Book by ID (GET)
   - Update Book (PUT)
   - Delete Book (DELETE)

3. **Laporan Singkat** (1-2 halaman PDF):
   - Penjelasan struktur kode
   - Penjelasan setiap endpoint
   - Tantangan yang dihadapi dan solusinya

#### A.4 Rubrik Penilaian (Total 100 poin)

| Kriteria | Bobot | Sangat Baik (86-100) | Baik (76-85) | Cukup (66-75) | Kurang (56-65) | Sangat Kurang (0-55) |
|----------|:-----:|---------------------|--------------|---------------|----------------|----------------------|
| **Fungsionalitas** | 40% | Semua 5 endpoint berfungsi sempurna | 4 endpoint berfungsi | 3 endpoint berfungsi | 2 endpoint berfungsi | ≤1 endpoint berfungsi |
| **Database & ORM** | 20% | Model Book benar, CRUD efisien | Model benar, CRUD cukup efisien | Model benar, CRUD basic | Model ada error minor | Model salah total |
| **Error Handling** | 15% | 404, 400, 500 semua handled | 2 dari 3 handled | 1 dari 3 handled | Error handling minimal | Tidak ada error handling |
| **Middleware & CORS** | 10% | Logging + CORS configured | Hanya CORS atau logging | Minimal middleware | Tidak ada middleware | — |
| **Kualitas Kode** | 10% | Kode clean, PEP 8, komentar | Kode terstruktur, cukup clean | Kode dapat dipahami | Kode berantakan | Kode tidak terstruktur |
| **Dokumentasi** | 5% | README lengkap + laporan | README lengkap | README minimal | README sangat minim | Tidak ada dokumentasi |

---

### LAMPIRAN B: UTS — TASK MANAGEMENT SYSTEM API

#### B.1 Deskripsi Ujian

Ujian Tengah Semester berbentuk **praktikum coding selama 150 menit** (2,5 jam). Mahasiswa diminta membangun **Task Management System API** dengan autentikasi JWT dan otorisasi role-based.

#### B.2 Spesifikasi Soal UTS

**Framework:** Python Flask 2.3+  
**Database:** SQLite (database file akan di-generate otomatis)  
**ORM:** Flask-SQLAlchemy  
**Auth:** JWT dengan PyJWT library  

**Fitur Wajib:**

1. **Model User** dengan kolom:
   - `id` (Integer, Primary Key)
   - `username` (String 50, Unique, Not Null)
   - `password_hash` (String 255, Not Null)
   - `role` (String 20, Not Null) — nilai: "admin" atau "user"

2. **Model Task** dengan kolom:
   - `id` (Integer, Primary Key)
   - `title` (String 200, Not Null)
   - `description` (Text, Nullable)
   - `status` (String 20, Not Null) — nilai: "pending", "in_progress", "completed"
   - `user_id` (Integer, Foreign Key ke User, Not Null)
   - `created_at` (DateTime, Default: now)

3. **Relationship:**
   - User ↔ Task: One-to-Many (satu user bisa punya banyak task)

4. **Endpoint Auth (3 endpoint):**
   - `POST /api/auth/register` — Register new user
     - Input: `username`, `password`, `role`
     - Output: User object (tanpa password_hash)
   
   - `POST /api/auth/login` — Login dan dapatkan JWT token
     - Input: `username`, `password`
     - Output: `{"token": "eyJ..."}`
   
   - `GET /api/auth/profile` — Get current user profile (protected)
     - Header: `Authorization: Bearer <token>`
     - Output: User object

5. **Endpoint Tasks (5 endpoint):**
   - `POST /api/tasks` — Create new task (protected, any authenticated user)
     - Input: `title`, `description`, `status`
     - Task akan ter-assign ke user yang sedang login
   
   - `GET /api/tasks` — Get all tasks
     - **Admin**: dapat melihat semua tasks dari semua user
     - **User**: hanya dapat melihat tasks miliknya sendiri
   
   - `GET /api/tasks/<id>` — Get task by ID
     - **Admin**: dapat melihat task siapa saja
     - **User**: hanya dapat melihat task miliknya sendiri
   
   - `PUT /api/tasks/<id>` — Update task by ID
     - **Admin**: dapat update task siapa saja
     - **User**: hanya dapat update task miliknya sendiri
   
   - `DELETE /api/tasks/<id>` — Delete task by ID (admin only)
     - Hanya **Admin** yang boleh delete task (mana saja)

#### B.3 Acceptance Criteria

✅ Password harus di-hash dengan `bcrypt.hashpw()` (TIDAK BOLEH plaintext)  
✅ JWT token harus valid dan bisa di-decode  
✅ Endpoint protected harus return 401 jika tidak ada token  
✅ Endpoint protected harus return 403 jika role tidak sesuai  
✅ User tidak boleh akses task milik user lain  
✅ Admin dapat akses semua task  

#### B.4 Ketentuan Ujian

- ⏰ **Waktu:** 150 menit (2,5 jam)
- 📖 **Open Internet:** Boleh akses dokumentasi Flask, SQLAlchemy, PyJWT
- 🚫 **Closed Collaboration:** DILARANG diskusi dengan mahasiswa lain
- 🚫 **No AI Code Generator:** DILARANG pakai ChatGPT, GitHub Copilot, atau AI lainnya
- 📁 **Submit:** GitHub private repository + invite dosen sebagai collaborator

#### B.5 Rubrik Penilaian UTS (Total 100 poin)

| Kriteria | Bobot | Poin Penuh | Poin Sebagian | Poin Minimal | Tidak Ada |
|----------|:-----:|:----------:|:-------------:|:------------:|:---------:|
| **Autentikasi (Register, Login, JWT)** | 30% | 30 | 20 | 10 | 0 |
| **Database & ORM (Model, Relationship)** | 25% | 25 | 17 | 9 | 0 |
| **Otorisasi (RBAC Admin-User)** | 20% | 20 | 13 | 7 | 0 |
| **CRUD Tasks (5 endpoint berfungsi)** | 15% | 15 | 10 | 5 | 0 |
| **Kualitas Kode (Clean, PEP 8)** | 10% | 10 | 7 | 4 | 0 |

**Catatan:**
- Aplikasi tidak berjalan sama sekali = **Nilai 0**
- Password plaintext (tidak di-hash) = **Maksimal nilai 60** (tidak lulus)

---

### LAMPIRAN C: TUGAS 2 — CAPSTONE PROJECT: LIBRARY MANAGEMENT SYSTEM API

#### C.1 Deskripsi Project

**Capstone Project** adalah proyek besar (bobot 25%) yang dikerjakan secara **berpasangan (2 orang)** selama **3 minggu** (Pekan 12-15). Mahasiswa diminta membangun **Library Management System API** yang lengkap dengan autentikasi, otorisasi, dan deployment.

#### C.2 Domain Analysis

**Library Management System** adalah sistem backend untuk mengelola perpustakaan dengan fitur:
- 📚 **Manajemen Buku** (CRUD)
- 👥 **Manajemen Anggota** (CRUD)
- ✍️ **Manajemen Penulis** (CRUD)
- 📖 **Manajemen Peminjaman** (Create, Return)
- 🔐 **Autentikasi & Otorisasi** (Admin & Member)

#### C.3 Database Schema (ERD)

**4 Model Utama:**

1. **User**
   - `id` (PK)
   - `username` (Unique, Not Null)
   - `password_hash` (Not Null)
   - `role` (Not Null) — "admin" atau "member"
   - `created_at` (Default: now)

2. **Author**
   - `id` (PK)
   - `name` (Not Null)
   - `bio` (Nullable)
   - `created_at` (Default: now)

3. **Book**
   - `id` (PK)
   - `title` (Not Null)
   - `isbn` (Unique, Not Null)
   - `year` (Not Null)
   - `stock` (Integer, Default: 1)
   - `author_id` (FK ke Author, Not Null)
   - `created_at` (Default: now)

4. **Loan** (Peminjaman)
   - `id` (PK)
   - `book_id` (FK ke Book, Not Null)
   - `user_id` (FK ke User, Not Null)
   - `borrow_date` (Default: now)
   - `return_date` (Nullable) — diisi saat buku dikembalikan
   - `status` (Not Null) — "borrowed" atau "returned"

**Relationships:**
- Author ↔ Book: **One-to-Many** (satu author bisa punya banyak buku)
- User ↔ Loan: **One-to-Many** (satu user bisa punya banyak peminjaman)
- Book ↔ Loan: **One-to-Many** (satu buku bisa dipinjam berkali-kali)

#### C.4 API Endpoint Specification (13 Endpoints)

**A. Auth Endpoints (3)**
1. `POST /api/auth/register` — Register new user
2. `POST /api/auth/login` — Login dan dapatkan JWT
3. `GET /api/auth/profile` — Get profile (protected)

**B. Author Endpoints (4)**
4. `POST /api/authors` — Create author (admin only)
5. `GET /api/authors` — Get all authors (public)
6. `PUT /api/authors/<id>` — Update author (admin only)
7. `DELETE /api/authors/<id>` — Delete author (admin only)

**C. Book Endpoints (8) — CRUDLFIX Complete**
8. `POST /api/books` — **Create** book (admin only)
9. `GET /api/books` — **List** all books with **pagination & filter** (public)
   - Query params: `?page=1&limit=10&search=title&author_id=1&sort_by=year&order=desc`
10. `GET /api/books/<id>` — **Read** book by ID (public)
11. `PUT /api/books/<id>` — **Update** book (admin only)
12. `DELETE /api/books/<id>` — **Delete** book (admin only)
13. `POST /api/books/import` — **Import** books from CSV (admin only)
   - Upload CSV dengan kolom: `title`, `isbn`, `year`, `author_id`, `stock`
14. `GET /api/books/export` — **eXport** books to CSV/JSON (admin only)
   - Query params: `?format=csv` atau `?format=json`
15. `GET /api/books/search` — **Filter** books by multiple criteria (public)
   - Query params: `?title=keyword&min_year=2020&max_year=2024&in_stock=true`

**D. Loan Endpoints (2)**
16. `POST /api/loans` — Borrow book (member & admin)
17. `PUT /api/loans/<id>/return` — Return book (member & admin)

**Total Endpoints: 17** (3 Auth + 4 Author + 8 Book CRUDLFIX + 2 Loan)

#### C.5 Business Rules

1. **Stok Buku:**
   - Saat buku dipinjam, `stock` di-decrement (-1)
   - Saat buku dikembalikan, `stock` di-increment (+1)
   - Buku tidak bisa dipinjam jika `stock` = 0

2. **Otorisasi:**
   - **Admin**: dapat CRUD semua resource (authors, books, loans)
   - **Member**: hanya dapat borrow & return book milik sendiri
   - **Public** (tanpa login): hanya dapat GET books & authors

3. **Validasi Loan:**
   - Member tidak boleh pinjam buku yang sama jika masih dipinjam (status "borrowed")
   - Return loan harus mengubah status menjadi "returned" dan mengisi `return_date`

4. **CRUDLFIX Operations:**
   - **List**: Endpoint `/api/books` harus mendukung pagination (`?page=1&limit=10`)
   - **Filter**: Endpoint `/api/books/search` harus mendukung filter multiple criteria
   - **Import**: Endpoint `/api/books/import` harus validasi CSV sebelum bulk insert
   - **eXport**: Endpoint `/api/books/export` harus generate CSV dengan header yang benar
   - **Performance**: Gunakan eager loading untuk Author relationship (hindari N+1 query)

#### C.6 Technical Requirements

**Framework & Library:**
- Python Flask 2.3+
- Flask-SQLAlchemy
- Flask-Migrate (untuk database migration)
- Flask-RESTX (untuk dokumentasi Swagger)
- PyJWT (untuk JWT token)
- bcrypt (untuk password hashing)
- marshmallow (untuk input validation)
- python-decouple (untuk environment variables)

**Database:**
- Development: SQLite
- Production (Heroku): PostgreSQL (Heroku Postgres add-on)

**Deployment:**
- Platform: Heroku
- WSGI Server: Gunicorn
- Live URL harus accessible (tidak 404)

**Dokumentasi:**
- Flask-RESTX Swagger UI di `/api/docs`
- README.md lengkap (setup, endpoint, demo)

#### C.7 Deliverables

1. **GitHub Repository (Public):**
   - Source code lengkap dengan struktur yang rapi
   - `.gitignore` yang benar (tidak commit `.env`, `__pycache__`, `*.db`)
   - `requirements.txt` complete
   - `Procfile` untuk Heroku
   - `README.md` lengkap (minimal 500 kata)

2. **Live Deployment:**
   - URL Heroku app yang accessible: `https://nama-app.herokuapp.com`
   - Swagger documentation: `https://nama-app.herokuapp.com/api/docs`

3. **Video Demo (15 menit):**
   - Penjelasan arsitektur aplikasi
   - Demo live API menggunakan Postman/Thunder Client
   - Demo autentikasi & otorisasi (Admin vs Member)
   - **Demo CRUDLFIX operations:**
     - List books dengan pagination (`?page=1&limit=5`)
     - Filter books by author & search (`?author_id=1&search=Python`)
     - Import books dari CSV file
     - eXport books ke CSV/JSON format
   - Demo borrow & return book
   - Penjelasan business logic (stock management)
   - Demo Swagger UI documentation

4. **Laporan Teknis (10 halaman PDF):**
   - Pendahuluan & domain analysis
   - Database schema (ERD diagram)
   - API endpoint specification (tabel 17 endpoint CRUDLFIX)
   - Business rules documentation
   - Security implementation (hashing, JWT, RBAC)
   - CRUDLFIX implementation explanation (pagination, filter, import/export)
   - Deployment process (step-by-step)
   - Screenshot aplikasi (Swagger UI, Postman, CSV import/export demo)
   - Tantangan & solusi
   - Kesimpulan & pembelajaran

#### C.8 Presentasi (Pekan 15)

**Format:**
- Durasi: **15 menit per tim** (10 menit presentasi + 5 menit Q&A)
- Slide: Maksimal 10 slide
- Live Demo: Wajib (akses URL Heroku langsung)

**Penilaian Presentasi:**
- Kejelasan penjelasan arsitektur (30%)
- Live demo fungsionalitas (40%)
- Menjawab pertanyaan dosen (20%)
- Slide & komunikasi (10%)

#### C.9 Rubrik Penilaian Capstone (Total 100 poin)

| Kriteria | Bobot | 86-100 (A) | 76-85 (B) | 66-75 (C) | <66 (Tidak Lulus) |
|----------|:-----:|-----------|-----------|-----------|-------------------|
| **Kompleksitas & Fitur** | 25% | Semua 17 endpoint + CRUDLFIX | 13-16 endpoint | 10-12 endpoint | <10 endpoint |
| **CRUDLFIX Operations** | 15% | List + Filter + Import + eXport perfect | 3 dari 4 fitur | 2 dari 4 fitur | 0-1 fitur |
| **Autentikasi & RBAC** | 20% | JWT + 2 role flawless | JWT + RBAC basic | JWT saja | Tidak ada auth |
| **Database & ORM** | 10% | 4 model + relationship perfect | 4 model + relationship basic | 3 model | <3 model |
| **Swagger Documentation** | 10% | Flask-RESTX complete 17 endpoint | Flask-RESTX partial | Swagger minimal | Tidak ada Swagger |
| **Deployment** | 10% | Heroku + Postgres working | Heroku working | Heroku tapi issue | Tidak deploy |
| **Kualitas Kode** | 5% | Clean, modular, PEP 8 | Terstruktur | Basic structure | Berantakan |
| **Presentasi & Demo** | 5% | Sangat jelas + demo CRUDLFIX flawless | Cukup jelas + demo working | Demo minimal | Tidak presentasi |

**Catatan Penting:**
- Tim yang tidak deploy ke Heroku: **Maksimal nilai 75** (C)
- Tim yang tidak presentasi: **Nilai 0** untuk project

---

### LAMPIRAN D: UAS — E-BOOK STORE API (BUILD FROM SCRATCH)

#### D.1 Deskripsi Ujian

Ujian Akhir Semester adalah **ujian praktikum komprehensif** selama **150 menit** (2,5 jam). Mahasiswa diminta membangun **E-Book Store API** dari nol (*from scratch*) dengan semua fitur backend yang telah dipelajari.

#### D.2 Studi Kasus: E-Book Store

**Domain:** Online E-Book Store dengan fitur:
- 📚 Manajemen E-Book (CRUD)
- 🗂️ Kategori E-Book (CRUD)
- 👤 User Authentication (Admin & Customer)
- 🛒 Order Management (Create Order)
- ⭐ Review & Rating (Create Review)

#### D.3 Spesifikasi Soal UAS

**3 Model Wajib:**

1. **User**
   - `id`, `username`, `password_hash`, `role` ("admin" / "customer")

2. **Book**
   - `id`, `title`, `author`, `price` (Float), `category_id` (FK)

3. **Category**
   - `id`, `name`

**Bonus Model (Opsional, +10 poin):**

4. **Order**
   - `id`, `user_id` (FK), `book_id` (FK), `order_date`

5. **Review**
   - `id`, `book_id` (FK), `user_id` (FK), `rating` (1-5), `comment`

**Endpoint Minimum (10 endpoint wajib):**

**Auth (2):**
1. `POST /api/auth/register`
2. `POST /api/auth/login`

**Category (3):**
3. `POST /api/categories` (admin only)
4. `GET /api/categories` (public)
5. `DELETE /api/categories/<id>` (admin only)

**Book (5 — CRUDLFIX):**
6. `POST /api/books` (admin only) — **Create** book
7. `GET /api/books` (public) — **List** books with pagination & filter
   - Query params: `?page=1&limit=10&category_id=1&search=keyword`
8. `GET /api/books/<id>` (public) — **Read** book by ID
9. `PUT /api/books/<id>` (admin only) — **Update** book
10. `GET /api/books/export` (admin only) — **eXport** books to CSV/JSON
   - Query params: `?format=csv` atau `?format=json`

**Order (1):**
11. `POST /api/orders` (customer & admin) — buat pesanan

**Review (1):**
12. `POST /api/reviews` (customer & admin) — buat review untuk buku

**Total Endpoint Minimum: 12 endpoint** (2 Auth + 3 Category + 5 Book CRUDLFIX + 1 Order + 1 Review)

**Bonus Endpoint (+5 poin per endpoint):**
- `GET /api/books/<id>/reviews` — get all reviews for a book
- `GET /api/orders/my-orders` — get orders milik user yang login
- `POST /api/books/import` — import books from CSV (admin only)

#### D.4 Technical Requirements (Wajib)

✅ **Password hashing** dengan bcrypt  
✅ **JWT authentication** pada protected endpoint  
✅ **RBAC**: Admin dapat CRUD semua, Customer hanya bisa order & review  
✅ **Input validation** (minimal untuk auth & create book)  
✅ **CRUDLFIX**: Minimal List dengan pagination + Filter by category + eXport CSV  
✅ **Swagger documentation** minimal 5 endpoint dengan Flask-RESTX  
✅ **Deploy ke Heroku** (URL accessible, tidak 404)  
✅ **Database production**: Heroku Postgres  

#### D.5 Ketentuan Ujian

- ⏰ **Waktu:** 150 menit (2,5 jam)
- 📖 **Open Internet:** Boleh akses dokumentasi resmi
- 🚫 **Closed Collaboration:** DILARANG diskusi dengan mahasiswa lain
- 🚫 **No AI Code Generator:** DILARANG pakai ChatGPT, GitHub Copilot
- 📁 **Submit:**
  - GitHub private repository + invite dosen
  - URL Heroku live deployment
  - Screenshot Swagger UI

#### D.6 Rubrik Penilaian UAS (Total 100 poin)

| Kriteria | Bobot | Poin |
|----------|:-----:|------|
| **Autentikasi (Register, Login, JWT)** | 15% | 15 |
| **Database & ORM (3 model + relationship)** | 20% | 20 |
| **CRUD Operations (12 endpoint berfungsi)** | 20% | 20 |
| **CRUDLFIX (List Pagination + Filter + eXport)** | 10% | 10 |
| **Otorisasi RBAC (Admin vs Customer)** | 10% | 10 |
| **Swagger Documentation (Flask-RESTX)** | 10% | 10 |
| **Deployment (Heroku + Postgres)** | 10% | 10 |
| **Kualitas Kode (Clean, PEP 8)** | 5% | 5 |
| **TOTAL** | **100%** | **100** |

**Bonus Poin (Maksimal +20):**
- Model Order + Review implementasi sempurna: **+10 poin**
- 3 bonus endpoint berfungsi: **+15 poin** (+5 per endpoint)

**Konsekuensi:**
- Aplikasi tidak berjalan: **Nilai 0**
- Password plaintext (tidak hashing): **Maksimal 55** (E)
- Tidak deploy ke Heroku: **Maksimal 65** (C)
- Tidak ada CRUDLFIX sama sekali: **Maksimal 70** (C+)

---

## BAGIAN VI: LEMBAR VALIDASI & PENGESAHAN

### MATRIKS APPROVAL RPS

RPS ini telah disusun, direview, dan divalidasi oleh:

| No | Pihak | Nama | Jabatan | Tanda Tangan | Tanggal |
|:--:|-------|------|---------|:------------:|:-------:|
| 1 | **Dosen Pengampu** | [Nama Dosen Koordinator MK] | Dosen Koordinator STI-416 | ________________ | _______ |
| 2 | **Tim Kurikulum** | [Nama Ketua Tim Kurikulum] | Ketua Tim Kurikulum SISTEKIN | ________________ | _______ |
| 3 | **Unit Penjaminan Mutu (UPM)** | [Nama Kepala UPM FSTI] | Kepala UPM FSTI | ________________ | _______ |
| 4 | **Ketua Program Studi** | [Nama Ketua Prodi] | Ketua Prodi S1 SISTEKIN | ________________ | _______ |

---

**Kota, Tanggal:**  
Malang, 28 September 2026

---

**Catatan Perubahan dari Versi 1 ke Versi 2:**

1. Framework: Node.js/Express/FastAPI → **Python Flask ONLY**
2. ORM: Sequelize/Prisma/SQLAlchemy → **Flask-SQLAlchemy ONLY**
3. Auth: JWT + OAuth2 + Multi-RBAC → **JWT + 2-Role RBAC (Admin-User)**
4. Caching: Redis eksternal → **Flask-Caching (in-memory)**
5. Documentation: Swagger manual → **Flask-RESTX (auto-generate)**
6. Deployment: Docker + Cloud → **Heroku (one-click)**
7. Complexity: C4-C6 Advanced → **C3-C4 Intermediate**
8. Target Pass Rate: 50-60% → **85%+ (gentle learning curve)**

---

**END OF DOCUMENT — RPS STI-416 VERSI 2 (SIMPLIFIED PYTHON FOCUS)**

*Dokumen ini disusun khusus untuk dosen dengan keterbatasan kemampuan teknis dan mahasiswa dengan motivasi belajar menengah, dengan fokus pada konsep fundamental backend yang transferable dan practical skills yang langsung applicable di industri.*

