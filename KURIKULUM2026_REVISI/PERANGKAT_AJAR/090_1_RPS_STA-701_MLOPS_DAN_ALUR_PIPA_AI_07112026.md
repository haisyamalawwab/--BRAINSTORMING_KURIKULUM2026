# RPS — STA-701 MLOPS DAN ALUR PIPA AI 

**Program Studi:** S1 SISTEKIN | **Semester:** 7 | **Kode:** STA-701 | **Nama EN:** MLOps and AI Pipeline
**SKS/Tipe:** 3 SKS / +P — 100m Teori + 170m Lab + 180m Mandiri | **Rumpun:** MLOps — P1 Integrated Smart Systems
**Prasyarat:** STI-413 Machine Learning & STI-726 Integrasi AI | **Dosen:** Tim Dosen MLOps | **Revisi:** 07112026
**CPL:** P4, KK1, KK2 (MLOps & Data Pipeline) | **PL:** PL-1 MLOps Engineer | **PEO:** PEO-1 | **Rujukan:** 005, 007 §51. STA-701, 008, 043

---

## 1. Identitas & Pemetaan Makro

| Atribut | Spesifikasi |
|---|---|
| **Kode & Nama MK** | STA-701 MLOPS DAN ALUR PIPA AI |
| **Semester/Rumpun** | Semester 7 / MLOps — P1 Integrated Smart Systems |
| **Prasyarat** | STI-413 Machine Learning & STI-726 Integrasi AI |
| **CPL Dibebankan** | P4, KK1, KK2 (MLOps & Data Pipeline) — sesuai 003 & 004 Matriks Ketertelusuran OBE |
| **Profil Lulusan** | PL-1 MLOps Engineer |
| **PEO** | PEO-1 |
| **BoK APTIKOM** | Lihat 003 — BK terkait P4, |
| **Level KKNI** | Level 6 — Mampu merancang & mengevaluasi solusi sesuai CPMK |

MK ini adalah bagian dari Semester 7 Peminatan P1 Integrated Smart Systems — prasyarat berjenjang dari Semester 5-6.

---

## 2. Deskripsi Mata Kuliah

Mata kuliah **STA-701 — Mlops Dan Alur Pipa Ai** membekali mahasiswa kompetensi inti jalur peminatan sesuai CPL **P4, KK1, KK2 (MLOps & Data Pipeline)**. Pembelajaran berbasis **Case Method + Project-Based Learning (PjBL) + Lab Hands-on** (untuk +P) atau **Case Method + Studio** (untuk Teori) dengan produk akhir berupa **proyek terpadu/kajian komprehensif** yang dipresentasikan pada **Demo Day / Sidang Presentasi** pada Minggu 16. Materi selaras dengan BoK APTIKOM dan kebutuhan industri (PL-1 MLOps Engineer).

Relevansi karir: PL-1 MLOps Engineer — roles: MLOps and AI Pipeline Specialist, PL-1 MLOps Engineer Engineer.

---

## 3. CPL Dibebankan

| CPL | Indikator Pencapaian MK |
|---|---|
| **P4** | Mahasiswa mampu mendemonstrasikan kompetensi sesuai deskripsi CPL dalam konteks MLOps and AI Pipeline (lihat 003) |

Pemetaan BoK: lihat Dok 003 & 004 — MK ini mendukung PL PL-1 MLOps Engineer.

---

## 4. CPMK (Format ABCD & Level Bloom) — Sumber 007 §51. STA-701

| Kode CPMK | Rumusan CPMK (A-B-C-D) | Bloom | CPL |
|---|---|---|---|
| **CPMK-1** | Mahasiswa (*A*) mampu **mengelola** pelacakan versi data dan eksperimen model (*B*) menggunakan Data Version Control (DV… | **C4** | `KK2` |
| **CPMK-2** | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Training (CT) otomatis (*B*) menggunakan Kubeflow Pipelines / Ap… | **C6** | `P4, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **mendeploy dan memantau** model AI produksi (*B*) dengan strategi Canary/Shadow Deployment serta … | **C5** | `KK1` |
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** teknik Prompt Engineering tingkat lanjut (Few-Shot, Chain-of-Thought, ReAct) (*B*) … | **C3** | `KK1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **merancang dan mengoptimalkan** sistem RAG multi-dokumen (*B*) menggunakan teknik Contextual Comp… | **C6** | `P2, KK1` |
| **CPMK-3** | Mahasiswa (*A*) mampu **melakukan** Fine-Tuning model LLM open-source (*B*) menggunakan teknik Parameter-Efficient Fine-… | **C4** | `KK1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **membangun** asisten virtual cerdas berbasis agen otonom (Tool Calling) (*B*) dengan integrasi mu… | **C6** | `KK1` |

*Detail CPMK lengkap lihat 007 §51. STA-701. Tabel di atas ringkasan; rumusan lengkap ABCD ada di Dok 007.*

---

## 5. Matriks Pembelajaran 16 Minggu (Sub-CPMK, Kajian, Metode, Asesmen)

| Mg | Sub-CPMK & Bahan Kajian | Metode | Asesmen & Bobot | Sumber |
|---|---|---|---|---|
| 1 | Pengantar & motivasi MK — use cases industri MLOps and AI Pipeline (C2) | Kuliah interaktif 100m + Lab setup 170m / Diskusi 120m | Formatif quiz | [A1] Handbook, industri whitepapers |
| 2 | Fondasi teori 1 — konsep inti STA-701 (C2-C3) | Case Method + Lab/Diskusi | Formatif — latihan | [A2] Textbook Ch.1-2 |
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

**Bobot:** 20%+25%+25%+30% =100%. Minimal C (55), UAS ≥50, hadir ≥80%.

---

## 6. Pengalaman Belajar Mahasiswa

- **Case Method 30%:** Bedah kasus industri relevan MLOps and AI Pipeline (3-4 kasus semester)
- **PjBL 50% (+P) / 40% (Teori):** Proyek tim 4-5 org bertahap Milestone1→Milestone2→UAS — role: Engineer, Analyst, QA, PM
- **Team-Based:** Kolaborasi lintas peran, peer evaluation 20% dari nilai UAS
- **Industry Guest:** 1-2 sesi praktisi (PL-1 MLOps Engineer) — Mg6 & Mg14
- **Open Source/Portfolio:** Hasil proyek menjadi portofolio karir

---

## 7. Asesmen Ringkas (Detail di Dokumen 090_4)

| Komponen | Bentuk | CPMK | Bobot | Kriteria |
|---|---|---|---|---|
| Tugas1 Mg4 | Milestone 1 / Case Analysis 1 | CPMK-1,2 | 20% | Fungsionalitas & docs |
| UTS Mg8 | Live Coding Lab Test | CPMK-1,2 | 25% | Kebenaran & analisis |
| Tugas2 Mg12 | Milestone 2 / Proyek Integrasi | CPMK-3 | 25% | Integrasi & evaluasi |
| UAS Mg16 | Demo Day / Presentasi Akhir | CPMK-1-4 | 30% | E2E + Q&A |

Remedial 1× untuk Tugas, susulan UTS/UAS terjadwal. Plagiarisme Turnitin ≤20% (laporan), MOSS ≤30% (code).

---

## 8. Sumber Belajar Utama

1. Textbook utama sesuai MLOps and AI Pipeline (lihat 007 §51. STA-701 refs)
2. Dokumentasi resmi tools/framework terkait (online)
3. Paper/whitepaper industri (IEEE, ACM, vendor whitepapers)
4. Case studies industri (Tokopedia, Gojek, Jakarta Smart City, dll. sesuai konteks)
5. Dokumen kurikulum FSTI: 003, 005, 007, 008, 043

---

## 9. Media & Fasilitas

- Lab MLOps (GPU/Cloud/GIS sesuai MK) + GitHub Classroom
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

*Disahkan Kaprodi SISTEKIN — perubahan via rapat kurikulum. Referensi CPMK lengkap di 007 §51. STA-701.*

