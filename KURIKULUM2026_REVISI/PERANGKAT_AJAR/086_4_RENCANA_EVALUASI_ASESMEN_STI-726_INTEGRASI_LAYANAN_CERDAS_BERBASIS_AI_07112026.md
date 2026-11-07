# RENCANA EVALUASI & ASESMEN — STI-726 INTEGRASI LAYANAN CERDAS BERBASIS AI

**Kode:** STI-726 | **Nama:** Integrasi Layanan Cerdas Berbasis AI | **SKS:** 3 (+P) — 100T+170P+180M  
**Semester:** 7 | **Rumpun:** Sistem Cerdas & Sains Data — Core STI (Prasyarat STI-413, STI-416)  
**CPL:** P2, KK1 | **CPMK:** 1 (C4 ONNX/TRT), 2 (C6 FastAPI+Docker), 3 (C6 RAG), 4 (C5 evaluasi & security)  
**Revisi:** 07112026 | **Rujukan:** 007 §38.B-C, 008 (Sistem Asesmen OBE), 043 (Guardrails)

---

## 1. Prinsip Asesmen OBE (008)

- **Authentic Assessment:** Produk layanan AI yang dideploy (Docker) & dievaluasi performa nyata (latensi, RPS, faithfulness), bukan hanya teori
- **Proportional:** Tugas1 20% (milestone awal) + UTS 25% (ujian praktik individu) + Tugas2 25% (integrasi RAG+queue) + UAS 30% (Demo Day tim) = 100%
- **Transparan:** Rubrik terpublikasi di 086_5, MOSS & Turnitin untuk integritas code & laporan
- **Formative + Summative:** 12 sesi formatif (pass/fail) untuk scaffolding, 4 summative untuk yudisium

---

## 2. Pemetaan CPMK → Asesmen

| CPMK | Bloom | Asesmen Utama | Bobot Total | Teknik |
|---|---|---|---|---|
| CPMK-1 (ONNX/TensorRT) | C4 | Tugas1 (50% CPMK1) + UTS (50%) | 22.5% efektif | Benchmark latensi, verifikasi numerik, live coding |
| CPMK-2 (FastAPI+Docker) | C6 | Tugas1 (40%) + UTS (30%) + Tugas2 (15%) + UAS (15%) | 27.5% efektif | Repo review, RPS test, compose runnable |
| CPMK-3 (RAG+VectorDB) | C6 | Tugas2 (60%) + UAS (40%) | 27% efektif | Faithfulness, recall@k, sitasi |
| CPMK-4 (Evaluasi & Security) | C5 | UAS (60%) + Tugas2 (20%) + UTS (20% wawancara) | 23% efektif | Locust report, guardrails test |

*Bobot efektif = kontribusi CPMK terhadap nilai akhir via komponen asesmen.*

---

## 3. Rincian Komponen Asesmen Summative

### A. TUGAS 1 — Milestone Proyek 1: ONNX + FastAPI Inference Service (20% — Mg4)

**Tujuan:** Menguji CPMK-1 & CPMK-2 tahap awal (konversi & serving dasar)  
**Bentuk:** Kelompok 4-5 org, repo GitHub + README benchmark + Docker image  
**Deliverables (wajib):**
1. `models/` — `model.onnx` + `model.trt` (engine) + script `export.py` & `build_trt.py`
2. `app/` — `main.py` (FastAPI async), `schemas.py` (Pydantic), `requirements.txt`, `tests/test_api.py`
3. `Dockerfile` + `docker-compose.yml` (api service) + `.dockerignore`
4. `README.md` — tabel benchmark: PyTorch FP32 vs ONNX vs TensorRT FP16 vs INT8 (latensi P50/P95, throughput), screenshot Swagger UI, instruksi `docker run --gpus all`
5. Video demo 2 menit (opsional, nilai tambah)

**Kriteria Penilaian (Rubrik 086_5 §A):**
- Konversi valid & verifikasi numerik (30%): ONNX checker pass, output diff <1e-4, engine load sukses
- Endpoint async & OpenAPI (30%): /predict berfungsi, async def, Pydantic validasi, Swagger docs lengkap
- Docker GPU runnable (20%): Build sukses, image <1GB, cold-start <5s, --gpus passthrough
- Benchmark & dokumentasi (20%): Tabel lengkap, analisis trade-off, instruksi runnable

**Deadline:** Mg4 Jumat 23:59 WIB, tag `milestone1`. Keterlambatan -10%/hari. Plagiarisme code >30% MOSS = 0.

### B. UTS — Live Coding Lab Test: ONNX & FastAPI (25% — Mg8)

**Tujuan:** Evaluasi individu (mencegah free-rider) untuk CPMK-1 & CPMK-2  
**Format:** 170 menit total — 120m coding + 50m wawancara lisan per mahasiswa (bergilir)  
**Soal (3 tugas dalam 120m):**
1. Ekspor model PyTorch (disediakan) ke ONNX opset 17 dengan dynamic axes (batch) — 30 poin
2. Konversi ONNX→TensorRT INT8 via `trtexec --int8 --calib=...` & verifikasi engine — 30 poin
3. Bangun endpoint FastAPI baru `/classify` async dengan validasi & error handler — 40 poin

**Lingkungan:** Lab offline, template repo kosong, docs offline diizinkan, AI assistant dilarang. Proctoring via screen record.  
**Rubrik:**
- Fungsionalitas: endpoint merespons 200 dengan JSON valid (40%)
- Kebenaran konversi: ONNX checker pass + output diff <1e-3 (30%)
- Latensi benchmark: trtexec log P95 < baseline FP32 (20%)
- Wawancara lisan: jelaskan trade-off FP16 vs INT8, async vs sync (10%)

**Susulan:** H+7 dengan surat sakit resmi, soal setara.

### C. TUGAS 2 — Milestone Proyek 2: RAG + Scalable Queue (25% — Mg12)

**Tujuan:** Menguji CPMK-3 & CPMK-2 lanjutan (RAG + scalability)  
**Bentuk:** Kelompok (lanjut dari Tugas1), repo + docker-compose 4 services + laporan faithfulness  
**Deliverables:**
1. `vectordb/` — Chroma/Milvus persistent (`./chroma_db`), script ingestion `ingest.py` (chunk 512/overlap50), koleksi 2K docs
2. `rag/` — `rag_pipeline.py` (LangChain RetrievalQA), `prompts.py`, evaluasi `eval_faithfulness.py` (faithfulness, answer relevancy via RAGAS manual)
3. `queue/` — `tasks.py` (Celery), `celery_app.py`, Redis broker, endpoint `/rag/query` async → enqueue → poll `/rag/result/{id}`
4. `docker-compose.yml` — services: api, worker, redis, chroma (atau milvus), healthchecks
5. `REPORT_TUGAS2.md` — faithfulness ≥75%, recall@5, queue throughput (tasks/sec), analisis halusinasi

**Rubrik:**
- RAG faithfulness & sitasi (35%): faithfulness ≥75%, sitasi sumber [1][2] valid, top-k=4 relevan
- Queue architecture (30%): Celery task berfungsi, Redis broker, polling, Flower (opsional)
- Compose runnable (20%): `docker compose up` sukses E2E, semua healthcheck pass
- Laporan & docs (15%): Analisis halusinasi, trade-off chunk size, instruksi lengkap

**Deadline:** Mg12 Jumat 23:59, tag `milestone2`.

### D. UAS — Demo Day & Portofolio: E2E AI Service (30% — Mg16)

**Tujuan:** Evaluasi komprehensif CPMK-1 s.d. 4 — produk terpadu + performa + security + presentasi  
**Format:** Tim, Demo Day panel (dosen + industri opsional) 170 menit sesi penuh (5-6 tim/hari)  
**Alur per tim (25 menit):**
- 12m presentasi: problem, arsitektur (diagram), benchmark latensi/TRT, RAG faithfulness, security
- 8m Q&A panel: trade-off, scalability, guardrails, etika AI
- 5m live demo: FE (Next.js) → AI backend (FastAPI) → inference + RAG query streaming, via projector

**Deliverables UAS:**
1. Repo final tag `v1.0` — semua milestone + FE client (`/frontend` atau repo terpisah link)
2. `PORTFOLIO.pdf` — arsitektur, benchmark P95/P99 (Locust), faithfulness, security test, lesson learned, kontribusi individu (bagian wajib)
3. Video demo 3 menit (YouTube unlisted) + README final
4. Laporan Locust HTML + Guardrails test report (blocked prompt injections)

**Rubrik UAS (detail 086_5 §D):**
- Fungsionalitas E2E (30%): FE→AI→DB→RAG→response sukses live, semua endpoint up
- Latensi & Load Test (20%): P95 <1s (mock GPU T4), RPS ≥30, failure <2%
- RAG faithfulness & sitasi (20%): faithfulness ≥75%, sitasi valid, minim halusinasi (manual review 10 queries)
- Security & docs (15%): rate limit aktif, prompt injection blocked ≥85%, docs lengkap
- Presentasi & teamwork (15%): kejelasan, Q&A, kontribusi individu seimbang (peer eval 10% dari 15%)

**Syarat lulus UAS:** Demo live berhasil (tidak boleh video saja), P95 terukur, guardrails aktif. Jika demo gagal total = maksimal C.

---

## 4. Asesmen Formatif (12 sesi — Non-Graded, Penentu Kelayakan UTS/UAS)

| Mg | Aktivitas Formatif | Output | Tindak Lanjut Jika Gagal |
|---|---|---|---|
| 1 | Quiz AIaaS 10 soal | Pass ≥60% | Remedial quiz online |
| 2 | Notebook ONNX export | Checker pass | Bimbingan lab tambahan |
| 3 | Benchmark TensorRT | Report 1 hal | Revisi benchmark |
| 5 | Unit test pipeline | pytest pass | Perbaikan code |
| 6 | Docker build evidence | Image logs | Rebuild workshop |
| 7 | Quiz VectorDB | Pass ≥60% | Remedial |
| 9 | CRUD vector recall@5 | ≥80% | Tuning params |
| 10 | RAG notebook MRR | Report | Perbaikan chunking |
| 11 | CLI chatbot sitasi | Demo | Perbaikan prompt |
| 13 | Locust report | HTML | Analisis ulang |
| 14 | Security test blocked | ≥80% | Perkuat guardrails |
| 15 | E2E screen record | Video | Bug fix |

**Aturan:** Mahasiswa yang tidak mengumpulkan ≥8 formatif tidak diizinkan ikut UAS (wajib remedial formatif).

---

## 5. Mekanisme Penilaian Akhir & Yudisium

**Formula Nilai Akhir (NA):**
```
NA = 0.20*Tugas1 + 0.25*UTS + 0.25*Tugas2 + 0.30*UAS + bonus (max +3 poin)
Bonus: Video demo berkualitas +2, kontribusi open-source model zoo +1
```

**Konversi Huruf (sesuai 008):**
| NA | Huruf | Keterangan |
|---|---|---|
| 85-100 | A | Lulus — CPL tercapai sangat baik |
| 70-84 | B | Lulus — CPL tercapai baik |
| 60-69 | C | Lulus bersyarat — CPL minimal tercapai |
| 55-59 | D | Tidak lulus — remedial |
| <55 | E | Tidak lulus |

**Kelulusan MK:** NA ≥55 (C) dengan syarat UAS ≥50 (mencegah lulus tanpa produk) dan kehadiran ≥80%. Jika NA ≥60 tetapi UAS <50 → nilai maksimal C.

**Remedial:** 1× kesempatan untuk Tugas1/2 (perbaikan 7 hari, nilai maks B). UTS/UAS susulan terjadwal (soal setara, bukan sama).

---

## 6. Integritas Akademik & Anti-Plagiarisme

- **Code plagiarism:** MOSS (Measure of Software Similarity) threshold 30%. Di atas itu → investigasi, jika terbukti copy-paste antar tim → 0 untuk komponen.
- **Laporan:** Turnitin ≤20% similarity (kecuali code block & sitasi). Wajib sertakan log Turnitin di lampiran.
- **AI-generated code:** Diperbolehkan sebagai assist (Copilot/ChatGPT) dengan disclosure di README (bagian `AI-Assistance Declaration`). Tanpa disclosure & terdeteksi → -20% nilai.
- **Prompt injection dataset:** Penggunaan dataset publik diizinkan, tetapi musti sitasi sumber.

---

## 7. Jadwal Evaluasi & Deadline (Semester Ganjil 2026/2027 — Ilustratif)

| Milestone | Tanggal | Jam | Tempat |
|---|---|---|---|
| Tugas1 deadline | Mg4 Jumat 23:59 | Online (GitHub) | Classroom |
| UTS Live Coding | Mg8 Kamis 08:00-11:00 | Lab GPU A/B | Proctored |
| Tugas2 deadline | Mg12 Jumat 23:59 | Online | Classroom |
| UAS Demo Day | Mg16 Senin-Selasa 08:00-17:00 | Aula FSTI + Zoom | Panel |

*Jadwal final menyesuaikan kalender akademik.*

---

## 8. Evaluasi Mutu & Continuous Improvement

- **Survey kepuasan** Mg8 & Mg16 (kepuasan ≥4.0/5.0 target)
- **Analisis butir soal UTS:** Distraktor analysis, revisi soal jika daya beda <0.3
- **Retrospektif milestone:** Feedback Tugas1→Tugas2, update ONNX opset tiap tahun ajaran
- **Tracer MK:** Tracking alumni ke peran AI Engineer (6 bulan pasca lulus) — target 60% bekerja di bidang AI/MLOps

---

*Rubrik detail & lembar penilaian terlampir di 086_5_RUBRIK_PENILAIAN.*

