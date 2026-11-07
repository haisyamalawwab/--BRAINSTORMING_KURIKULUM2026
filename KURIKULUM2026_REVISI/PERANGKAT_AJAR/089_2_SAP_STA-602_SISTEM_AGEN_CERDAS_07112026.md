# SAP — STA-602 SISTEM AGEN CERDAS

**Kode:** STA-602 | **Nama:** Sistem Agen Cerdas / *Intelligent Agent Systems*
**SKS:** 3 SKS / +P | **Semester:** 7 | **Rumpun:** Sistem Cerdas — P1 Integrated Smart Systems
**Prasyarat:** STI-307 Sistem Cerdas | **Dosen:** Tim Dosen Sistem Cerdas  | **Revisi:** 07112026

---

## A. Deskripsi & Posisi MK

SAP 16 minggu PjBL + Lab Hands-on — **Bobot:** 20% Tugas1 + 25% UTS + 25% Tugas2 + 30% UAS =100%. Lulus minimal **C (55)**, hadir ≥80%, UAS ≥50. MK Peminatan Semester 7 — prasyarat Semester 5-6. Produk akhir deployable service + Demo Day.

---

## B. CPMK & CPL Terkait

| CPMK | Rumusan (ABCD) | Bloom | CPL |
|---|---|---|---|
| CPMK-1 | Mahasiswa (*A*) mampu **merancang** agen otonom berbasis arsitektur Belief-Desire-Intention (BDI) (*… | C4 | P2 |
| CPMK-2 | Mahasiswa (*A*) mampu **membangun** simulasi Multi-Agent Systems (MAS) (*B*) menggunakan protokol ko… | C6 | P2, KK1 |
| CPMK-3 | Mahasiswa (*A*) mampu **mengimplementasikan** algoritma Reinforcement Learning (Q-Learning, Deep Q-N… | C4 | KK1 |
| CPMK-4 | Mahasiswa (*A*) mampu **melatih** agen otonom menggunakan algoritma Policy Gradient (PPO) (*B*) pada… | C5 | KK1 |
| CPMK-1 | Mahasiswa (*A*) mampu **mengelola** pelacakan versi data dan eksperimen model (*B*) menggunakan Data… | C4 | KK2 |
| CPMK-2 | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Training (CT) otomatis (*B*) menggunakan Kub… | C6 | P4, KK1 |
| CPMK-3 | Mahasiswa (*A*) mampu **mendeploy dan memantau** model AI produksi (*B*) dengan strategi Canary/Shad… | C5 | KK1 |

*Detail lengkap 007 §50. STA-602.*

---

## C. Rencana Mingguan Detail (16 Minggu)

### MINGGU 1 — Pengantar Intelligent Agent Systems (C2)
**Bahan:** Motivasi, use cases industri, roadmap 16 minggu, tools setup  
**Metode:** Kuliah 100m + Lab setup 170m + Mandiri 180m/120m  
**Tugas:** Setup check — install tools, clone template repo, quiz konsep (non-graded)  
**Sumber:** Handbook Ch.1, industri whitepaper

### MINGGU 2 — Fondasi Teori 1 (C2-C3)
**Bahan:** Konsep inti — definisi, prinsip, taksonomi STA-602  
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
**Bahan:** Keamanan, etika, governance sesuai STA-602 (mis. OWASP, COBIT, ITIL, TOGAF)  
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

