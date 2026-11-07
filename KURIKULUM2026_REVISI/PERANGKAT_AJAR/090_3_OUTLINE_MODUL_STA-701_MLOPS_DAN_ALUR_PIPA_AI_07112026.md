# OUTLINE MODUL — STA-701 MLOPS DAN ALUR PIPA AI

**Kode:** STA-701 | **3 SKS / +P** — 100T+170P+180M/minggu | **Semester:** 7 | **Prasyarat:** STI-413 Machine Learning & STI-726 Integrasi AI | **CPL:** P4, KK1, KK2 (MLOps & Data Pipeline) | **Revisi:** 07112026

---

## 1. Peta Modul & Alur PjBL

```
Mg1 Pengantar ─► Mg2 Fondasi1 ─► Mg3 Fondasi2 ─► [Mg4 PRAKTIK AWAL TUGAS1 20%]
                                                      │
Mg5 Lanjutan1 ─► Mg6 Lanjutan2 ─► Mg7 Case Study ─► [Mg8 UTS PRAKTIK]
                                                                  │
Mg9 Scalability ─► Mg10 Integration ─► Mg11 Governance ─► [Mg12 INTEGRASI TUGAS2 25%]
                                                                  │
Mg13 Monitoring ─► Mg14 Testing ─► Mg15 Finalisasi ─► [Mg16 UAS DEMO DAY/PRESENTASI 30%]
```

Produk: Service prototype → integrasi → deployable + monitoring — gate Milestone1 & 2.

---

## 2. Tujuan per Modul (16 Modul)

| Modul | Nama | CPMK | Tujuan Akhir | Beban |
|---|---|---|---|---|
| M1 | Pengantar MLOps | CPMK-1 | Menguraikan use cases & roadmap MK | 4.5 jam (100T+170P+180M) |
| M2 | Fondasi Teori 1 | CPMK-1 | Menguasai konsep inti STA-701 | 4.5 jam (100T+170P+180M) |
| M3 | Fondasi Teori 2 | CPMK-1 | Menguasai arsitektur & tools | 4.5 jam (100T+170P+180M) |
| M4 | Praktik Awal | CPMK-2 | Implementasi awal milestone1 — **TUGAS1** | 4.5 jam (100T+170P+180M) |
| M5 | Lanjutan 1 | CPMK-2 | Integrasi & optimasi | 4.5 jam (100T+170P+180M) |
| M6 | Lanjutan 2 | CPMK-2 | Patterns & best practices | 4.5 jam (100T+170P+180M) |
| M7 | Case Study | CPMK-3 | Bedah kasus industri | 4.5 jam (100T+170P+180M) |
| M8 | UTS | CPMK-1,2 | Evaluasi tengah semester | 2.8 jam |
| M9 | Scalability | CPMK-3 | Scalability & performance | 4.5 jam (100T+170P+180M) |
| M10 | Integration | CPMK-3 | Integrasi & deployment | 4.5 jam (100T+170P+180M) |
| M11 | Governance | CPMK-3 | Keamanan/etika/governance | 4.5 jam (100T+170P+180M) |
| M12 | Integrasi Proyek | CPMK-3 | Proyek integrasi — **TUGAS2** | 4.5 jam (100T+170P+180M) |
| M13 | Monitoring | CPMK-4 | Observability & monitoring | 4.5 jam (100T+170P+180M) |
| M14 | Testing | CPMK-4 | UAT & evaluasi | 4.5 jam (100T+170P+180M) |
| M15 | Finalisasi | CPMK-4 | Finalisasi E2E & docs | 4.5 jam (100T+170P+180M) |
| M16 | Demo Day / Presentasi | CPMK-1-4 | Sidang akhir — **UAS** | 2.8 jam |

---

## 3. Rincian Materi per Modul (Ringkasan — Detail SAP 086_2)

### M1 — Pengantar (Mg1)
**Topik:** Motivasi MLOps and AI Pipeline, use cases industri (PL-1 MLOps Engineer), setup tools (GitHub Classroom, Docker/GPU), expectation  
**Aktivitas:** Intro + setup check + quiz  
**Sumber:** Handbook Ch.1

### M2 — Fondasi Teori 1 (Mg2)
**Topik:** Konsep inti — definisi, taksonomi, standar terkait STA-701  
**Hands-on/Diskusi:** Notebook + case  

### M3 — Fondasi Teori 2 (Mg3)
**Topik:** Arsitektur & tools — framework/platform/standar (mis. untuk STA-701: FastAPI/MLOps/LLM/IoT)  
**Aktivitas:** Hands-on  

### M4 — Praktik Awal — TUGAS1 (Mg4)
**Topik:** Build service/endpoint awal (FastAPI/Model serving/Agent)  
**Output TUGAS1:** Repo + benchmark  

### M5 — Lanjutan 1 (Mg5)
**Topik:** Integrasi & optimasi performa/keamanan  
**Hands-on:** Lab  

### M6 — Lanjutan 2 (Mg6)
**Topik:** Patterns & best practices (design patterns, governance patterns)  
**Hands-on:** Workshop  

### M7 — Case Study (Mg7)
**Topik:** Bedah 3 kasus industri — gap & rekomendasi  
**Output:** Case analysis 2 hal  

### M8 — UTS (Mg8)
**Kisi:** Mg1-7 — fondasi + praktik awal — praktik  

### M9 — Scalability (Mg9)
**Topik:** Scalability, performance tuning, observability  

### M10 — Integration & Deployment (Mg10)
**Topik:** E2E integration, Docker/cloud/CI/CD  

### M11 — Governance (Mg11)
**Topik:** Keamanan/etika/governance — OWASP/Guardrails  

### M12 — Integrasi Proyek — TUGAS2 (Mg12)
**Topik:** Proyek integrasi komprehensif — deployable + queue/monitoring  
**Output TUGAS2:** Repo + compose + laporan  

### M13 — Monitoring (Mg13)
**Topik:** Monitoring, logging, dashboard — Grafana/Prometheus  

### M14 — Testing (Mg14)
**Topik:** UAT, evaluasi metrik — RPS/latensi/faithfulness  

### M15 — Finalisasi (Mg15)
**Topik:** Bug bash, docs portofolio, geladi bersih Demo Day  

### M16 — Demo Day / Presentasi (Mg16 — UAS)
**Agenda:** 12m presentasi + 8m demo + 5m Q&A — panel dosen+industri  
**Output:** Repo final + PORTFOLIO.pdf + video 3m  

---

## 4. Bahan Ajar

| Jenis | Judul | Akses |
|---|---|---|
| Buku | Textbook utama MLOps and AI Pipeline (lihat 007 §51. STA-701 refs) | Perpus |
| Docs | Docs resmi tools/framework/standar | Online |
| Paper | IEEE/ACM/vendor whitepapers terkait STA-701 | Scholar |
| Case | Studi kasus industri (Tokopedia, Gojek, Kemenkes, KemenPAN, dll.) | Web |
| Dataset | Dummy kampus privacy-safe | Lab |

---

## 5. Alat & Lingkungan

- Lab GPU/Cloud + GitHub Classroom + Docker + MLflow — sesuai MK
- LMS + Turnitin/MOSS

---

## 6. Skill Ladder

```
Level1 (Mg1-3): Fondasi teori & tools
Level2 (Mg4-7): Praktik awal → case study → UTS
Level3 (Mg9-12): Scalability → integrasi → TUGAS2
Level4 (Mg13-16): Monitoring → testing → finalisasi → Demo Day (UAS)
```

