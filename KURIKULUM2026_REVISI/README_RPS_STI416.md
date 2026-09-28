# 📘 RPS STI-416 — Web Back End Development

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI)  
**Universitas:** Universitas Widyagama Malang  
**Status:** ✅ **FINAL & READY FOR APPROVAL**  
**Tanggal Penyusunan:** 28 September 2026

---

## 📋 Daftar Isi

1. [Informasi Mata Kuliah](#informasi-mata-kuliah)
2. [File Tersedia](#file-tersedia)
3. [Cara Generate DOCX](#cara-generate-docx)
4. [Struktur Dokumen RPS](#struktur-dokumen-rps)
5. [Keselarasan Kurikulum](#keselarasan-kurikulum)
6. [Checklist Review](#checklist-review)
7. [Kontak & Approval](#kontak--approval)

---

## 📚 Informasi Mata Kuliah

| Atribut | Detail |
|---------|--------|
| **Kode MK** | STI-416 |
| **Nama MK** | Pengembangan Web Back End (*Web Back End Development*) |
| **SKS** | 3 SKS (Teori: 2 SKS, Praktikum: 1 SKS) |
| **Tipe** | +P (Teori dengan Praktikum) |
| **Semester** | Semester 4 (Genap) |
| **Prasyarat** | FST-207 (Manajemen Basis Data), STI-311 (Pengembangan Web Front End) |
| **Status** | Wajib (Core STI) |
| **Rumpun** | Platform & Pengembangan Web/Mobile |

### CPL yang Dibebankan
- **P4:** Arsitektur RESTful API & Keamanan Server
- **KK5:** Backend Engineering & ORM

### Body of Knowledge (BoK)
- **BK-IS12:** Web and Mobile Application Development
- **BK-IT04:** Platform Technologies & Web/Mobile

---

## 📁 File Tersedia

### 1. File Sumber (Markdown)
```
RPS_STI-416_Web_Back_End_Development.md
```
- Format: Markdown (.md)
- Ukuran: ~45 KB
- Konten: RPS lengkap dengan 16 pertemuan, 4 CPMK, 8 Sub-CPMK, 4 lampiran asesmen
- Status: ✅ Final & Verified

### 2. File Output (DOCX)
```
DOCX/RPS_STI-416_Web_Back_End_Development.docx
```
- Format: Microsoft Word (.docx)
- Ukuran: ~56 KB
- Layout: A4 Portrait (standar Template RPS OBE FSTI UWG)
- Status: ✅ Ready for Print & Approval

### 3. Generator Script
```
_tools/generate_rps_sti416_docx.py
```
- Bahasa: Python 3
- Dependencies: python-docx
- Fungsi: Convert MD → DOCX dengan format standar

### 4. Batch File (Windows)
```
GENERATE_RPS_STI416_DOCX.bat
```
- Platform: Windows
- Fungsi: One-click generator DOCX
- Output: Otomatis membuka folder DOCX setelah selesai

---

## 🚀 Cara Generate DOCX

### Metode 1: Menggunakan Batch File (Termudah)

**Windows:**
```batch
# Double-click file batch
GENERATE_RPS_STI416_DOCX.bat

# Atau via Command Prompt
cd KURIKULUM2026_REVISI
GENERATE_RPS_STI416_DOCX.bat
```

File DOCX akan otomatis di-generate di folder `DOCX/` dan folder akan terbuka otomatis.

---

### Metode 2: Menggunakan Python Langsung

```bash
# Pastikan berada di folder KURIKULUM2026_REVISI
cd KURIKULUM2026_REVISI

# Jalankan generator
python _tools/generate_rps_sti416_docx.py
```

**Output:**
```
================================================================================
🚀 GENERATOR RPS DOCX — STI-416 Web Back End Development
================================================================================
📄 Input  : RPS_STI-416_Web_Back_End_Development.md
📁 Output : DOCX\RPS_STI-416_Web_Back_End_Development.docx
--------------------------------------------------------------------------------
⚙️  Memproses konversi Markdown → DOCX...
================================================================================
✅ SUKSES! RPS DOCX berhasil di-generate
================================================================================
📍 Lokasi file: DOCX\RPS_STI-416_Web_Back_End_Development.docx
📊 Ukuran    : 56.41 KB
================================================================================
```

---

### Metode 3: Re-generate Semua Dokumen Kurikulum

Jika ingin generate ulang seluruh dokumen kurikulum (termasuk RPS ini):

```bash
# Windows
GENERATE_DOCX.bat

# Atau manual
python _tools/convert_md_to_docx.py
```

---

## 📖 Struktur Dokumen RPS

### Bagian I: Identitas & Capaian Pembelajaran (Hal 1-3)

- ✅ **Cover & Header**
  - Logo UWG
  - Nomor Dokumen SPMI: `071030.B4.5.2.RPS-STI416`
  - Identitas MK lengkap

- ✅ **CPL Program Studi** (2 CPL)
  - P4: Arsitektur RESTful API & Keamanan Server
  - KK5: Backend Engineering & ORM

- ✅ **CPMK** (4 Capaian)
  - CPMK-1: Membangun RESTful API Modular (C3)
  - CPMK-2: Integrasi Database dengan ORM (C3)
  - CPMK-3: Autentikasi JWT & RBAC (C4)
  - CPMK-4: Dokumentasi API & Deployment Docker (C6)

- ✅ **Sub-CPMK** (8 Sub-Capaian)
  - Penjabaran operasional CPMK per minggu pembelajaran

- ✅ **Matriks Korelasi CPL ↔ CPMK**

- ✅ **Deskripsi Singkat MK**
  - Naratif 200+ kata
  - Ruang lingkup, tujuan, dan posisi strategis

- ✅ **Bahan Kajian (Body of Knowledge)**
  - BK-IS12: Web and Mobile App Development
  - BK-IT04: Platform Technologies
  - 15 pokok bahasan detail

- ✅ **Pustaka**
  - 5 Pustaka Utama (buku teks)
  - 7 Pustaka Pendukung (dokumentasi resmi, OWASP, JWT, Docker, Swagger)

---

### Bagian II: Rencana Pembelajaran 16 Pertemuan (Hal 4-8)

**Tabel 16 Pertemuan Lengkap** dengan 8 kolom standar SN-DIKTI:

| Pekan | Sub-CPMK | Topik | Kemampuan Akhir (ABCD) | Metode | Waktu | Materi | Bobot Asesmen |
|:---:|:---:|---|---|:---:|:---:|---|:---:|
| 1 | — | Pengantar & Kontrak Belajar | ... | Kuliah | 150' | Setup Environment | — |
| 2 | Sub-1.1 | RESTful API Modular | ... | Praktikum | 150' | Node.js/Express | — |
| 3 | Sub-1.2 | Middleware & Validasi | ... | Praktikum | 150' | Input Sanitization | — |
| 4 | Sub-2.1 | Database & ORM | ... | Praktikum | 150' | Sequelize/Prisma | **Tugas 1 (20%)** |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 8 | CPMK-1,2,3 | **UTS** | ... | Ujian Praktikum | 150' | Evaluasi Komprehensif | **UTS (25%)** |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 12 | CPMK-4 | Proyek Kompleks | ... | Presentasi | 150' | Swagger + Deployment | **Tugas 2 (25%)** |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 16 | Seluruh CPMK | **UAS** | ... | Ujian/Proyek | 150' | Backend from Scratch | **UAS (30%)** |

**Total Waktu:** 16 pekan × 150 menit = 2,400 menit = 40 jam tatap muka

---

### Bagian III: Komponen Penilaian & Rubrik (Hal 9-10)

**Skema Asesmen 4 Titik (Total 100%):**

| Komponen | Pekan | Bentuk | Bobot |
|----------|:-----:|--------|:-----:|
| **Tugas 1** | 4 | Penugasan Praktikum (RESTful API + Middleware) | **20%** |
| **UTS** | 8 | Ujian Praktikum (Task Management System API) | **25%** |
| **Tugas 2** | 12 | Proyek Backend Kompleks + Dokumentasi Swagger | **25%** |
| **UAS** | 16 | Ujian Praktikum (Build Backend from Scratch) | **30%** |

**Kriteria Penilaian (6 Aspek):**
1. Fungsionalitas (40%)
2. Arsitektur & Clean Code (25%)
3. Keamanan (15%)
4. Database Integration (10%)
5. Dokumentasi API (5%)
6. Deployment (5%)

**Gradasi:** Sangat Kurang (0-55) | Kurang (56-65) | Cukup (66-75) | Baik (76-85) | Sangat Baik (86-100)

---

### Bagian IV: Boundary Guardrails (Hal 11)

**🟢 IN-SCOPE (Wajib Diajarkan):**
- ✅ Node.js/Express atau Python FastAPI
- ✅ RESTful API Design
- ✅ Middleware & Error Handling
- ✅ JWT Authentication & OAuth2
- ✅ ORM/ODM (Sequelize, Prisma, SQLAlchemy, Mongoose)
- ✅ RBAC (Role-Based Access Control)
- ✅ Redis Caching & Session Management
- ✅ Swagger/OpenAPI Documentation
- ✅ Docker Containerization
- ✅ Cloud Deployment (Heroku, Railway, GCP)

**❌ OUT-OF-SCOPE (Dilarang Diajarkan):**
- ❌ HTML/CSS/UI Design → STI-311 (Web Front End)
- ❌ Kubernetes Multi-Container → STI-727 (Smart City)
- ❌ Kafka Event Streaming → STI-727
- ❌ Mobile App Development → STI-522
- ❌ Advanced DevOps CI/CD → STB-601

**🔄 HANDOFF ANCHOR (Titik Serah Terima):**
- Backend API andal & terdokumentasi
- → STI-522: Konsumsi API dari mobile app
- → STI-625: Arsitektur platform kompleks
- → STI-727: Orkestrasi layanan terdistribusi

---

### Bagian V: Lampiran Instrumen Asesmen (Hal 12-20)

**Lampiran A: Tugas 1 — RESTful API Perpustakaan**
- Spesifikasi: 5 endpoint CRUD Buku
- Framework: Node.js/Express atau FastAPI
- Validasi: express-validator/Pydantic
- Deliverables: Source code + README + Screenshot + Laporan
- Rubrik: 5 kriteria × 5 level

**Lampiran B: UTS — Task Management System API**
- Waktu: 150 menit
- Spesifikasi: User Management + Task Management
- Database: PostgreSQL/MySQL/MongoDB (wajib ORM)
- Autentikasi: JWT + Bcrypt
- Rubrik: 5 kriteria (30% auth, 25% ORM, 20% middleware, 15% CRUD, 10% code quality)

**Lampiran C: Tugas 2 — Proyek Backend Kompleks**
- Pilihan domain: E-Commerce, Social Media, LMS
- Minimum: 4 resource, JWT + 2 role, RBAC, Swagger, Redis, File Upload, Deployment
- Deliverables: GitHub repo + Live URL + Swagger URL + Video 15' + Laporan 10 hal
- Rubrik: 6 kriteria (30% kompleksitas, 20% RBAC, 15% Swagger, 15% deployment, 10% code, 10% presentasi)

**Lampiran D: UAS — Backend from Scratch**
- Waktu: 150 menit
- Studi kasus: Hotel Reservation / Event Ticketing / Online Clinic
- Minimum: 3 resource, JWT, Protected routes, CRUD, Validasi, Swagger 5 endpoint, Docker, Deploy
- Ketentuan: Open Internet, Closed Collaboration, No AI Code Generator
- Rubrik: 7 kriteria (20% auth, 25% ORM, 15% validasi, 10% Swagger, 15% Docker, 10% deploy, 5% code quality)

---

### Bagian VI: Lembar Validasi & Pengesahan (Hal 21)

**Tripartit Approval:**

1. ✅ **Unit Penjaminan Mutu (UPM)**
   - Fakultas Sains dan Teknologi Informasi
   - [Nama Pejabat UPM]
   - NUPTK. __________________

2. ✅ **Dosen Pengampu**
   - Malang, 28 September 2026
   - [Nama Dosen Koordinator MK]
   - NUPTK. __________________

3. ✅ **Ketua Program Studi**
   - S1 Sistem dan Teknologi Informasi
   - [Nama Ketua Prodi SISTEKIN]
   - NUPTK. __________________

---

## ✅ Keselarasan Kurikulum

### Verifikasi terhadap Dokumen Kurikulum SISTEKIN 2026

| Dokumen | Aspek Verifikasi | Status |
|---------|------------------|:------:|
| **Dok 003** | CPL P4 & KK5 | ✅ Selaras 100% |
| **Dok 005** | Kode MK, SKS, Prasyarat, Semester | ✅ Selaras 100% |
| **Dok 007** | CPMK, Sub-CPMK, 16 Pertemuan | ✅ Selaras 100% |
| **Dok 037** | Boundary Guardrails (In/Out/Handoff) | ✅ Selaras 100% |
| **Dok 043** | CPL, CPMK, Sub-CPMK, BoK, 16 Pertemuan | ✅ Selaras 100% |
| **Dok 052** | Template RPS OBE Format & Layout | ✅ Selaras 100% |
| **Dok 008** | Skema 4× Asesmen (20-25-25-30%) | ✅ Selaras 100% |

### Standar Rujukan

- ✅ **Panduan Kurikulum OBE APTIKOM SI v2.0** (IS2020)
- ✅ **Panduan Kurikulum OBE TI 2023** (IT2017/CC2020)
- ✅ **Permendikbudristek No. 53 Tahun 2023** (MBKM & Penjaminan Mutu)
- ✅ **Template RPS OBE FSTI UWG** (Dokumen 052)

---

## 📋 Checklist Review

### ☑️ Kelengkapan Dokumen

- [x] Identitas Mata Kuliah lengkap
- [x] CPL Program Studi (2 CPL: P4, KK5)
- [x] CPMK (4 capaian dengan format ABCD & Bloom)
- [x] Sub-CPMK (8 sub-capaian operasional)
- [x] Matriks Korelasi CPL ↔ CPMK
- [x] Deskripsi Singkat MK (200+ kata)
- [x] Bahan Kajian BoK (BK-IS12, BK-IT04)
- [x] Pustaka (5 utama + 7 pendukung)
- [x] Tabel 16 Pertemuan (8 kolom standar)
- [x] Komponen Penilaian (4 asesmen = 100%)
- [x] Kriteria Penilaian & Rubrik
- [x] Boundary Guardrails (In/Out/Handoff)
- [x] Lampiran Instrumen Asesmen (4 lampiran)
- [x] Lembar Validasi & Pengesahan

### ☑️ Kesesuaian Konten

- [x] CPMK selaras dengan CPL Program Studi
- [x] Sub-CPMK selaras dengan CPMK
- [x] 16 Pertemuan mencakup seluruh Sub-CPMK
- [x] Asesmen terdistribusi merata (Pekan 4, 8, 12, 16)
- [x] Bobot asesmen = 100% (20+25+25+30)
- [x] Metode pembelajaran sesuai tipe MK (+P = Praktikum dominan)
- [x] Waktu pembelajaran = 3 SKS × 50' = 150' per pekan
- [x] Pustaka mutakhir (max 10 tahun terakhir)
- [x] Boundary Guardrails jelas & tidak tumpang tindih

### ☑️ Format & Standar

- [x] Format ABCD pada CPMK & Sub-CPMK
- [x] Taksonomi Bloom (C3-C6) pada CPMK
- [x] Kata Kerja Operasional (KKO) sesuai level Bloom
- [x] Tabel 8 kolom standar SN-DIKTI
- [x] Layout A4 Portrait (DOCX)
- [x] Font Arial 10-11 pt (body text)
- [x] Font Arial 12-14 pt Bold (heading)
- [x] Margin 25mm (kiri-kanan-atas-bawah)

---

## 📞 Kontak & Approval

### Tim Penyusun RPS

**Koordinator Penyusunan:**
- [Nama Dosen Koordinator]
- Email: [email@uwg.ac.id]
- Telp: [+62-xxx-xxxx-xxxx]

### Approval Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW APPROVAL RPS                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ✅ Penyusunan RPS oleh Dosen Koordinator MK            │
│     Status: COMPLETED (28 Sept 2026)                       │
│                                                             │
│  2. ⏳ Review oleh Tim Kurikulum Prodi                     │
│     PIC: Ketua Tim Kurikulum SISTEKIN                      │
│     Target: 30 Sept 2026                                   │
│                                                             │
│  3. ⏳ Validasi oleh Unit Penjaminan Mutu (UPM)            │
│     PIC: Kepala UPM FSTI                                   │
│     Target: 5 Okt 2026                                     │
│                                                             │
│  4. ⏳ Pengesahan oleh Ketua Program Studi                 │
│     PIC: Ketua Prodi SISTEKIN                              │
│     Target: 7 Okt 2026                                     │
│                                                             │
│  5. ⏳ Upload ke SIAKAD & Distribusi ke Dosen              │
│     PIC: Sekretaris Prodi                                  │
│     Target: 10 Okt 2026                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Feedback & Revisi

Jika ada feedback atau permintaan revisi:

1. **Edit file sumber** (Markdown):
   ```
   RPS_STI-416_Web_Back_End_Development.md
   ```

2. **Re-generate DOCX**:
   ```batch
   GENERATE_RPS_STI416_DOCX.bat
   ```

3. **Submit ulang** untuk approval

---

## 📝 Catatan Penting

### Revisi Berkala

RPS ini akan dievaluasi dan direvisi **setiap tahun akademik** sesuai dengan:
- Perkembangan teknologi backend terkini
- Kebutuhan industri
- Feedback dari dosen pengampu
- Feedback dari mahasiswa (tracer study)
- Perubahan standar APTIKOM

### Version History

| Versi | Tanggal | Perubahan | PIC |
|:---:|---------|-----------|-----|
| 1.0 | 28 Sept 2026 | Initial draft lengkap | Tim Kurikulum SISTEKIN |

---

## 🎓 Lampiran Tambahan

### A. Tools & Environment Setup

**Backend Development Stack:**
- Node.js v18 LTS atau Python 3.10+
- VSCode dengan extension: REST Client, Thunder Client, Docker
- Postman atau Insomnia (API testing)
- PostgreSQL 14+ atau MongoDB 6+
- Redis 7+
- Docker Desktop
- Git & GitHub

**Cloud Platform:**
- Railway (recommended untuk deployment cepat)
- Heroku (free tier)
- Google Cloud Platform (GCP)
- AWS (untuk mahasiswa advanced)

---

### B. Referensi Tambahan

**Online Resources:**
- Node.js Official Docs: https://nodejs.org/docs
- FastAPI Docs: https://fastapi.tiangolo.com
- Express.js Guide: https://expressjs.com
- Prisma Docs: https://www.prisma.io/docs
- JWT.io: https://jwt.io
- OWASP Top 10: https://owasp.org/www-project-top-ten
- Docker Docs: https://docs.docker.com

**Video Tutorials:**
- YouTube Channel: Traversy Media (Backend Development)
- YouTube Channel: Codevolution (Node.js & Express)
- YouTube Channel: TechWorld with Nana (Docker & Deployment)

---

**END OF DOCUMENT**

---

*Dokumen ini disusun berdasarkan Kurikulum SISTEKIN 2026 dan Template RPS OBE FSTI Universitas Widyagama Malang. Untuk informasi lebih lanjut, hubungi Program Studi S1 Sistem dan Teknologi Informasi.*
