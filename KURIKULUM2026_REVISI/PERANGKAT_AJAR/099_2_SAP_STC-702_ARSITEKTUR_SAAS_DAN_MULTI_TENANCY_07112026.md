# SAP — STC-702 ARSITEKTUR SAAS DAN MULTI TENANCY

**Kode:** STC-702 | **Nama:** Arsitektur Saas Dan Multi Tenancy / *SaaS Architecture & Multi-Tenancy*
**SKS:** 3 SKS / +P | **Semester:** 7 | **Rumpun:** SaaS — P3
**Prasyarat:** STI-625 Platform Engineering | **Dosen:** Tim Dosen SaaS  | **Revisi:** 07112026

---

## A. Deskripsi & Posisi MK

SAP 16 minggu PjBL + Lab Hands-on — **Bobot:** 20/25/25/30 =100%. Lulus minimal **C (55)**, hadir ≥80%, UAS ≥50. MK Peminatan Semester 7 — prasyarat Semester 5-6. Produk akhir deployable service + Demo Day.

---

## B. CPMK & CPL Terkait

| CPMK | Rumusan (ABCD) | Bloom | CPL |
|---|---|---|---|
| CPMK-1 | Mahasiswa (*A*) mampu **merancang** strategi isolasi data multi-tenant (Shared Database with Row-Lev… | C4 | P4 |
| CPMK-2 | Mahasiswa (*A*) mampu **membangun** mesin penagihan berlangganan (*Subscription Engine*) otomatis (*… | C6 | KK5 |
| CPMK-3 | Mahasiswa (*A*) mampu **mengimplementasikan** arsitektur Micro-Frontends dan *Feature Toggling* (*B*… | C4 | P4, KK5 |
| CPMK-1 | Mahasiswa (*A*) mampu **merumuskan** Visi Produk, Strategi Produk, dan Objectives and Key Results (O… | C4 | P2, KK6 |
| CPMK-2 | Mahasiswa (*A*) mampu **melakukan** Product Discovery dan prioritisasi backlog (*B*) menggunakan ker… | C4 | KK6 |
| CPMK-3 | Mahasiswa (*A*) mampu **menyusun** dokumen Product Requirement Document (PRD) berstandar industri (*… | C6 | KK6 |

*Detail lengkap 007 §64. STC-702.*

---

## C. Rencana Mingguan Detail (16 Minggu)

### MINGGU 1 — Pengantar SaaS Architecture & Multi-Tenancy (C2)
**Bahan:** Motivasi, use cases industri, roadmap 16 minggu, tools setup  
**Metode:** Kuliah 100m + Lab setup 170m + Mandiri 180m/120m  
**Tugas:** Setup check — install tools, clone template repo, quiz konsep (non-graded)  
**Sumber:** Handbook Ch.1, industri whitepaper

### MINGGU 2 — Fondasi Teori 1 (C2-C3)
**Bahan:** Konsep inti — definisi, prinsip, taksonomi STC-702  
**Metode:** Case Method + Lab Coding 270m/220m  
**Asesmen:** Formatif — latihan notebook  
**Sumber:** Textbook Ch.2

### MINGGU 3 — Fondasi Teori 2 (C3-C4)
**Bahan:** Arsitektur & tools utama (framework, platform, standar)  
**Metode:** Case Method + Hands-on 270m/220m  
**Asesmen:** Formatif — code review  

### MINGGU 4 — Praktik Awal — TUGAS1 (20%)
**Bahan:** Implementasi awal — build service/endpoint  
**Metode:** Kuliah 50m + Lab Hands-on 170m + Studio 50m  
**Asesmen:** **TUGAS1 (20%)** — Milestone 1: repo + README + benchmark — **Rubrik:** Fungsionalitas 30%, kebenaran 30%, docs 20%, runnable 20%. **Deadline:** Mg4 Jumat 23:59  

### MINGGU 5 — Lanjutan 1 — Integrasi & Optimasi (C4)
**Bahan:** Integrasi komponen, optimasi performa/keamanan  
**Metode:** Case Method + Lab 270m/220m  
**Asesmen:** Formatif — lab report  

### MINGGU 6 — Lanjutan 2 — Patterns & Best Practices (C4)
**Bahan:** Design patterns, best practices industri  
**Metode:** Workshop + Hands-on 270m/220m  
**Asesmen:** Formatif — code review  

### MINGGU 7 — Studi Kasus Industri (C4-C5)
**Bahan:** Bedah kasus nyata (3 kasus) — analisis gap & rekomendasi  
**Metode:** Case Method 220m  
**Asesmen:** Formatif — case analysis 2 hal  

### MINGGU 8 — UTS Evaluasi Tengah Semester
**Format:** Live Coding Lab Test 120m + wawancara 50m  
**Materi:** Mg1-7 — fondasi & praktik awal  
**Rubrik:** Fungsionalitas/Kebenaran 40%, analisis 30%, penjelasan 20%, docs 10% — Minimal 50. Susulan H+7.  
**Bobot:** 25%  

### MINGGU 9 — Lanjutan 3 — Scalability & Performance (C4)
**Bahan:** Scalability, performance tuning, observability  
**Metode:** Kuliah+Lab 270m/220m  
**Asesmen:** Formatif — benchmark report  

### MINGGU 10 — Lanjutan 4 — Integration & Deployment (C6)
**Bahan:** Integrasi E2E, deployment (Docker/cloud), CI/CD dasar  
**Metode:** Lab Hands-on 270m/220m  
**Asesmen:** Formatif — integration test  

### MINGGU 11 — Keamanan/Etika & Governance (C4-C5)
**Bahan:** Keamanan, etika, governance sesuai STC-702 (mis. OWASP, COBIT, ITIL, TOGAF)  
**Metode:** Case Workshop 270m/220m  
**Asesmen:** Formatif — risk matrix / governance gap  

### MINGGU 12 — Proyek Integrasi — TUGAS2 (25%)
**Bahan:** Proyek integrasi komprehensif — deployable service + queue/monitoring  
**Metode:** PjBL Studio 270m/220m  
**Asesmen:** **TUGAS2 (25%)** — Milestone 2: repo + compose + laporan evaluasi — **Rubrik:** Integrasi 35%, evaluasi 30%, runnable/docs 20%, analisis 15%. **Deadline:** Mg12 Jumat  

### MINGGU 13 — Optimasi & Monitoring (C4)
**Bahan:** Monitoring, logging, alerting — dashboard observability  
**Metode:** Lab Session 270m/220m  
**Asesmen:** Formatif — dashboard  

### MINGGU 14 — Validasi & Testing — UAT (C5)
**Bahan:** UAT bersama pengguna, evaluasi metrik  
**Metode:** Workshop Testing 270m/220m  
**Asesmen:** Formatif — UAT report  

### MINGGU 15 — Finalisasi Proyek — E2E & Docs (C6)
**Bahan:** Finalisasi E2E, bug bash, dokumentasi portofolio  
**Metode:** PjBL Studio 270m/220m  
**Asesmen:** Formatif — E2E demo screen record  

### MINGGU 16 — UAS Demo Day / Presentasi Komprehensif (30%)
**Format:** Demo Day panel industri+dosen 170m (12m presentasi + 8m demo + 5m Q&A)  
**Deliverables:** Repo final + PORTFOLIO.pdf + video 3m + Laporan Turnitin ≤20%  
**Rubrik UAS:** Fungsionalitas/Evaluasi 30%, performa/audit 20%, analisis 20%, docs 15%, presentasi 15% — Minimal UAS 50, demo live wajib.  

---

## D. Tugas Terstruktur

| Tugas | Output | Bobot | Deadline |
|---|---|---|---|
| Tugas1 Mg4 | Milestone 1 / Analisis 1 |20%|Mg4|
| UTS Mg8 | Live Coding |25%|Mg8|
| Tugas2 Mg12 | Milestone 2 / Integrasi |25%|Mg12|
| UAS Mg16 | Demo Day + Portofolio |30%|Mg16|

Keterlambatan -10%/hari, MOSS>30% atau Turnitin>20% → revisi/batal.

