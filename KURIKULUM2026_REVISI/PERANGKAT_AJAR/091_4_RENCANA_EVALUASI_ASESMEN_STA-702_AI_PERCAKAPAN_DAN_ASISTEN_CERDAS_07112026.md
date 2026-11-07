# RENCANA EVALUASI & ASESMEN — STA-702 AI PERCAKAPAN DAN ASISTEN CERDAS

**Kode:** STA-702 | **3 SKS / +P** — 100T+170P+180M | **Semester:** 7 | **Prasyarat:** STI-413 & STI-416
**CPL:** KK1 (LLM, RAG, Prompt Engineering) | **CPMK:** CPMK-1 C3, CPMK-2 C6, CPMK-3 C4, CPMK-4 C6, CPMK-1 C4, CPMK-2 C4, CPMK-3 C6, CPMK-4 C6 | **Revisi:** 07112026

---

## 1. Prinsip OBE (008)

- **Authentic:** Produk deployable yang di-load test & di-demo live — bukan hafalan
- **Proportional:** Tugas1 20% + UTS 25% + Tugas2 25% + UAS 30% =100%
- **Transparan:** Rubrik 091_5 terpublikasi Mg1, Turnitin/MOSS untuk integritas
- **Formative+Summative:** 10-12 formatif scaffolding, 4 summative yudisium

---

## 2. Pemetaan CPMK→Asesmen

| CPMK | Bloom | Asesmen Utama | Bobot Efektif | Teknik |
|---|---|---|---|---|
| CPMK-1 | C3 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-2 | C6 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-3 | C4 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-4 | C6 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-1 | C4 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-2 | C4 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-3 | C6 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |
| CPMK-4 | C6 | Tugas1/UTS/Tugas2/UAS | 25% | Lab/Repo |

---

## 3. Rincian Summative

### A. TUGAS1 — Milestone 1 / Analisis Awal (20% — Mg4)

**Deliverables:** Repo: service/endpoint/ingestion + README benchmark + Dockerfile/compose  
**Rubrik (091_5 §A):** Fungsionalitas 30%, kebenaran 30%, docs 20%, runnable/analisis 20% — Minimal 55, remedial 7 hari.  
**Deadline:** Mg4 Jumat 23:59 GitHub Classroom.

### B. UTS — Live Coding Lab Test (25% — Mg8)

**Format:** 120m coding (build endpoint/pipeline) + 50m wawancara trade-off  
**Materi:** Mg1-7 — fondasi & praktik awal  
**Rubrik:** Fungsionalitas/kebenaran 40%, analisis 30%, penjelasan 20%, docs 10% — Susulan H+7.  

### C. TUGAS2 — Milestone 2 / Proyek Integrasi (25% — Mg12)

**Deliverables:** Repo integrasi E2E: service+queue/monitoring+compose + laporan evaluasi (latensi/RPS/faithfulness)  
**Rubrik:** Integrasi/kedalaman 35%, evaluasi 30%, runnable/docs 20%, analisis 15% — Minimal 55.  
**Deadline:** Mg12 Jumat 23:59.

### D. UAS — Demo Day / Presentasi Akhir (30% — Mg16)

**Format:** Kelompok 4-5 org, Demo Day 170m (12m presentasi + 8m demo live + 5m Q&A panel industri+dosen)  
**Deliverables:** Repo final + PORTFOLIO.pdf + video 3m unlisted + Turnitin  
**Rubrik (091_5 §D):** Fungsionalitas/kedalaman 30%, performa/audit 20%, analisis 20%, docs 15%, presentasi 15% — Minimal UAS 50, demo live wajib (tidak boleh video saja). Jika demo gagal total → maksimal C.  

---

## 4. Formatif (10-12 sesi — Non-Graded, Gate UAS)

| Mg | Aktivitas | Output | Jika Gagal |
|---|---|---|---|
|1|Quiz konsep 10 soal|Pass ≥60%|Remedial quiz|
|2|Latihan fondasi 1|Pass|Bimbingan|
|3|Arsitektur/tools|Pass|Perbaikan|
|5|Integrasi awal|Pass|Revisi|
|6|Patterns|Pass|Review|
|7|Case study 2 hal|Pass|Revisi|
|9|Benchmark/scalability|Pass|Analisis ulang|
|10|Deployment/integration|Pass|Rebuild|
|11|Governance/risk matrix|Pass|Perbaikan|
|13|Monitoring dashboard|Pass|Revisi|
|14|UAT report|Pass|Perbaikan|
|15|E2E screen record|Pass|Bug fix|

**Aturan:** Tidak kumpul ≥6-8 formatif → tidak boleh UAS (remedial 7 hari). Hadir ≥80%.

---

## 5. Formula Nilai Akhir & Yudisium

```
NA = 0.20×Tugas1 + 0.25×UTS + 0.25×Tugas2 + 0.30×UAS + bonus (max +3)
Bonus: partisipasi aktif >80% +2, video berkualitas/open-source +1
```

| NA | Huruf | Keterangan |
|---|---|---|
|85-100|A|Sangat memuaskan — CPL tercapai sangat baik|
|70-84|B|Memuaskan — CPL tercapai baik|
|60-69|C|Cukup — Lulus bersyarat|
|55-59|D|Tidak lulus — remedial|
|<55|E|Gagal — mengulang|

**Aturan tambahan:** NA ≥55 (C) dengan UAS ≥50 & hadir ≥80%. Jika NA ≥60 tetapi UAS <50 → maksimal C (mencegah lulus tanpa produk). Remedial Tugas 7 hari (maks B), UAS 14 hari (maks B).

---

## 6. Integritas Akademik

- Code plagiarism MOSS >30% → 0, AI-assistance disclosure wajib
- Fabricated data/interview → 0 + sidang etik.

---

## 7. Jadwal Ilustratif

| Milestone | Tanggal | Tempat |
|---|---|---|
|Tugas1|Mg4 Jumat|Classroom|
|UTS|Mg8|Lab GPU|
|Tugas2|Mg12 Jumat|Classroom|
|UAS Demo Day|Mg16 Senin-Selasa 08:00-17:00|Aula FSTI|

---

*Rubrik detail 091_5 terlampir.*

