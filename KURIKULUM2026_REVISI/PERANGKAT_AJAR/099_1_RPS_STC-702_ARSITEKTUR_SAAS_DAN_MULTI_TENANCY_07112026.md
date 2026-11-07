# RPS — STC-702 ARSITEKTUR SAAS DAN MULTI TENANCY 

**Program Studi:** S1 SISTEKIN | **Semester:** 7 | **Kode:** STC-702 | **Nama EN:** SaaS Architecture & Multi-Tenancy
**SKS/Tipe:** 3 SKS / +P — 100m Teori + 170m Lab + 180m Mandiri | **Rumpun:** SaaS — P3
**Prasyarat:** STI-625 Platform Engineering | **Dosen:** Tim Dosen SaaS | **Revisi:** 07112026
**CPL:** KK5 (SaaS, Multi-tenant) | **PL:** PL-3 | **PEO:** PEO-1 | **Rujukan:** 005, 007 §64. STC-702, 008, 043

---

## 1. Identitas & Pemetaan Makro

| Atribut | Spesifikasi |
|---|---|
| **Kode & Nama MK** | STC-702 ARSITEKTUR SAAS DAN MULTI TENANCY |
| **Semester/Rumpun** | Semester 7 / SaaS — P3 |
| **Prasyarat** | STI-625 Platform Engineering |
| **CPL Dibebankan** | KK5 (SaaS, Multi-tenant) — sesuai 003 & 004 Matriks Ketertelusuran OBE |
| **Profil Lulusan** | PL-3 |
| **PEO** | PEO-1 |
| **BoK APTIKOM** | Lihat 003 — BK terkait KK5 |
| **Level KKNI** | Level 6 — Mampu merancang & mengevaluasi solusi sesuai CPMK |

MK ini adalah bagian dari Semester 7 Peminatan P3 — prasyarat berjenjang dari Semester 5-6.

---

## 2. Deskripsi Mata Kuliah

Mata kuliah **STC-702 — Arsitektur Saas Dan Multi Tenancy** membekali mahasiswa kompetensi inti jalur peminatan sesuai CPL **KK5 (SaaS, Multi-tenant)**. Pembelajaran berbasis **Case Method + Project-Based Learning (PjBL) + Lab Hands-on** (untuk +P) atau **Case Method + Studio** (untuk Teori) dengan produk akhir berupa **proyek terpadu/kajian komprehensif** yang dipresentasikan pada **Demo Day / Sidang Presentasi** pada Minggu 16. Materi selaras dengan BoK APTIKOM dan kebutuhan industri (PL-3).

Relevansi karir: PL-3 — roles: SaaS Architecture & Multi-Tenancy Specialist, PL-3 Engineer.

---

## 3. CPL Dibebankan

| CPL | Indikator Pencapaian MK |
|---|---|
| **KK5 (SaaS** | Mahasiswa mampu mendemonstrasikan kompetensi sesuai deskripsi CPL dalam konteks SaaS Architecture & Multi-Tenancy (lihat 003) |

Pemetaan BoK: lihat Dok 003 & 004 — MK ini mendukung PL PL-3.

---

## 4. CPMK (Format ABCD & Level Bloom) — Sumber 007 §64. STC-702

| Kode CPMK | Rumusan CPMK (A-B-C-D) | Bloom | CPL |
|---|---|---|---|
| **CPMK-1** | Mahasiswa (*A*) mampu **merancang** strategi isolasi data multi-tenant (Shared Database with Row-Level Security vs Datab… | **C4** | `P4` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** mesin penagihan berlangganan (*Subscription Engine*) otomatis (*B*) dengan integrasi… | **C6** | `KK5` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mengimplementasikan** arsitektur Micro-Frontends dan *Feature Toggling* (*B*) pada platform SaaS… | **C4** | `P4, KK5` |
| **CPMK-1** | Mahasiswa (*A*) mampu **merumuskan** Visi Produk, Strategi Produk, dan Objectives and Key Results (OKRs) (*B*) untuk pro… | **C4** | `P2, KK6` |
| **CPMK-2** | Mahasiswa (*A*) mampu **melakukan** Product Discovery dan prioritisasi backlog (*B*) menggunakan kerangka kerja RICE, Ka… | **C4** | `KK6` |
| **CPMK-3** | Mahasiswa (*A*) mampu **menyusun** dokumen Product Requirement Document (PRD) berstandar industri (*B*) dengan User Stor… | **C6** | `KK6` |

*Detail CPMK lengkap lihat 007 §64. STC-702. Tabel di atas ringkasan; rumusan lengkap ABCD ada di Dok 007.*

---

## 5. Matriks Pembelajaran 16 Minggu (Sub-CPMK, Kajian, Metode, Asesmen)

| Mg | Sub-CPMK & Bahan Kajian | Metode | Asesmen & Bobot | Sumber |
|---|---|---|---|---|
| 1 | Pengantar & motivasi MK — use cases industri SaaS Architecture & Multi-Tenancy (C2) | Kuliah interaktif 100m + Lab setup 170m / Diskusi 120m | Formatif quiz | [A1] Handbook, industri whitepapers |
| 2 | Fondasi teori 1 — konsep inti STC-702 (C2-C3) | Case Method + Lab/Diskusi | Formatif — latihan | [A2] Textbook Ch.1-2 |
| 3 | Fondasi teori 2 — arsitektur & tools utama (C3-C4) | Case Method + Hands-on | Formatif — notebook/essay | [B1] Docs resmi |
| **4** | **Topik praktik 1 — implementasi awal (C3-C6)** | Kuliah+Lab/Workshop | **Tugas1 20%** — Milestone 1 | [B2] Tutorial |
| 5 | Topik lanjutan 1 — integrasi & optimasi (C4) | Case Method + Lab | Formatif — lab report | [B3] Advanced guide |
| 6 | Topik lanjutan 2 — patterns & best practices (C4) | Workshop + Hands-on | Formatif — code review | [C1] Pattern ref |
| 7 | Studi kasus industri — bedah kasus nyata (C4-C5) | Case Method | Formatif — case analysis 2 hal | [C2] Case study |
| **8** | **UTS — Evaluasi Tengah Semester** | Ujian Praktik Live Coding 170m/100m | **UTS 25% Live Coding** | Bank soal Mg1-7 |
| 9 | Topik lanjutan 3 — scalability & performance (C4) | Kuliah+Lab | Formatif — benchmark | [D1] Perf guide |
| 10 | Topik lanjutan 4 — integration & deployment (C6) | Lab Hands-on | Formatif — integration test | [D2] Deploy docs |
| 11 | Topik keamanan/etika — governance & risk (C4-C5) | Case Workshop | Formatif — risk matrix | [E1] Governance |
| **12** | **Topik praktik 2 — proyek integrasi (C6)** | PjBL Studio | **Tugas2 25%** — Milestone 2 | [E2] Project template |
| 13 | Optimasi & monitoring — observability (C4) | Lab Session | Formatif — monitoring dashboard | [F1] Observability |
| 14 | Validasi & testing — UAT & evaluation (C5) | Workshop Testing | Formatif — UAT report | [F2] Test guide |
| 15 | Finalisasi proyek — integrasi E2E & docs (C6) | PjBL Studio | Formatif — E2E demo | [G1] Docs template |
| **16** | **UAS — Sidang Demonstrasi Produk / Presentasi Komprehensif** | Demo Day & Defense 170m/100m | **UAS 30% Demo Day** | Rubrik UAS 086_5 style |

**Bobot:** 20/25/25/30 =100%. Minimal C (55), UAS ≥50, hadir ≥80%.

---

## 6. Pengalaman Belajar Mahasiswa

- **Case Method 30%:** Bedah kasus industri relevan SaaS Architecture & Multi-Tenancy (3-4 kasus semester)
- **PjBL 50% (+P) / 40% (Teori):** Proyek tim 4-5 org bertahap Milestone1→Milestone2→UAS — role: Engineer, Analyst, QA, PM
- **Team-Based:** Kolaborasi lintas peran, peer evaluation 20% dari nilai UAS
- **Industry Guest:** 1-2 sesi praktisi (PL-3) — Mg6 & Mg14
- **Open Source/Portfolio:** Hasil proyek menjadi portofolio karir

---

## 7. Asesmen Ringkas (Detail di Dokumen 099_4)

| Komponen | Bentuk | CPMK | Bobot | Kriteria |
|---|---|---|---|---|
| Tugas1 Mg4 | Milestone 1 / Case Analysis 1 | CPMK-1,2 | 20% | Fungsionalitas & docs |
| UTS Mg8 | Live Coding Lab Test | CPMK-1,2 | 25% | Kebenaran & analisis |
| Tugas2 Mg12 | Milestone 2 / Proyek Integrasi | CPMK-3 | 25% | Integrasi & evaluasi |
| UAS Mg16 | Demo Day / Presentasi Akhir | CPMK-1-4 | 30% | E2E + Q&A |

Remedial 1× untuk Tugas, susulan UTS/UAS terjadwal. Plagiarisme Turnitin ≤20% (laporan), MOSS ≤30% (code).

---

## 8. Sumber Belajar Utama

1. Textbook utama sesuai SaaS Architecture & Multi-Tenancy (lihat 007 §64. STC-702 refs)
2. Dokumentasi resmi tools/framework terkait (online)
3. Paper/whitepaper industri (IEEE, ACM, vendor whitepapers)
4. Case studies industri (Tokopedia, Gojek, Jakarta Smart City, dll. sesuai konteks)
5. Dokumen kurikulum FSTI: 003, 005, 007, 008, 043

---

## 9. Media & Fasilitas

- Lab SaaS (GPU/Cloud/GIS sesuai MK) + GitHub Classroom
- Dataset privacy-safe kampus (dummy) + tools edukasi (Figma, Docker, cloud credits)
- LMS FSTI + Turnitin + MOSS

---

## 10. Prinsip 5 Pilar SISTEKIN

- **Academic Excellence:** Evaluasi kuantitatif (metrik performa, audit score)
- **Vocational Excellence:** Produk deployable/portofolio siap kerja
- **Character Building:** Etika (data privacy, AI ethics, governance compliance)
- **Competitive Excellence:** Benchmarking antar-kelompok, leaderboard
- **Community Empowerment:** Proyek untuk mitra desa/UMKM/kampus

---

*Disahkan Kaprodi SISTEKIN — perubahan via rapat kurikulum. Referensi CPMK lengkap di 007 §64. STC-702.*

