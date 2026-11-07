# OUTLINE MODUL — STI-726 INTEGRASI LAYANAN CERDAS BERBASIS AI

**Kode:** STI-726 | **Nama (EN):** AI-Based Smart Service Integration | **SKS:** 3 (+P) | **Semester:** 7  
**Prasyarat:** STI-413 Machine Learning, STI-416 Web Back-End | **Rumpun:** Sistem Cerdas & Sains Data — Core STI  
**Koordinator:** Tim Dosen Sistem Cerdas | **Revisi:** 07112026 | **Rujukan:** 005, 007 §38, 043

---

## 1. Peta Modul & Alur PjBL

```
Mg1 AIaaS ─► Mg2 ONNX ─► Mg3 TensorRT ─► [Mg4 FASTAPI MILESTONE1 20%]
   │
   └─► Mg5 Pipeline ─► Mg6 Docker GPU ─► Mg7 VectorDB ─► [Mg8 UTS LIVE CODING 25%]
                              │
                              ▼
Mg9 Chroma/Milvus ─► Mg10 RAG ─► Mg11 LangChain ─► [Mg12 CELERY/REDIS MILESTONE2 25%]
                                                    │
                                       Mg13 Locust ─► Mg14 Guardrails ─► Mg15 FE Integration ─► [Mg16 DEMO DAY 30%]
```

**Produk bertahap:** Repo milestone1 (model serving) → milestone2 (RAG+queue) → produk akhir E2E (FE+AI+security+scalability).

---

## 2. Tujuan Pembelajaran per Modul

| Modul | Nama Modul | CPMK | Tujuan Akhir (ABCD) | Estimasi Beban |
|---|---|---|---|---|
| **M1** | Pengantar AIaaS | CPMK-1 | Menguraikan trade-off latensi/throughput/biaya AIaaS untuk 3 pola deployment | 4.5 jam (100T+170P+180M) |
| **M2** | ONNX Export | CPMK-1 | Mengekspor 2 model PyTorch/TF ke ONNX dengan verifikasi numerik <1e-4 error | 4.5 jam |
| **M3** | TensorRT Acceleration | CPMK-1 | Mengoptimasi ONNX ke TensorRT FP16/INT8 dengan latensi turun ≥30% | 4.5 jam |
| **M4** | FastAPI Inference API | CPMK-2 | Membangun async FastAPI /predict + /health dengan OpenAPI & test RPS | 4.5 jam — **TUGAS1** |
| **M5** | Inference Pipeline | CPMK-2 | Merancang pre/post-processing & dynamic batching (batch 1/8/32 benchmark) | 4.5 jam |
| **M6** | Docker GPU | CPMK-2 | Mengemas service ke Docker GPU multi-stage, image <800MB | 4.5 jam |
| **M7** | VectorDB Fundamentals | CPMK-3 | Menguraikan embedding, cosine, HNSW & memilih Chroma/Milvus | 4.5 jam |
| **M8** | UTS Live Coding | CPMK-1,2 | Ujian praktik ONNX+TensorRT+FastAPI | 2.8 jam — **UTS** |
| **M9** | VectorDB Setup | CPMK-3 | Ingestion 2K dokumen ke Chroma/Milvus dengan partition & recall@5 ≥80% | 4.5 jam |
| **M10** | RAG Pipeline | CPMK-3 | Membangun chunk→embed→retrieve dengan MRR evaluasi | 4.5 jam |
| **M11** | LLM Orchestration | CPMK-3 | Integrasi RAG+LLM via LangChain dengan sitasi & streaming | 4.5 jam |
| **M12** | Scalable Queue | CPMK-2,3 | Implement Celery/Redis queue untuk async batching | 4.5 jam — **TUGAS2** |
| **M13** | Load Testing | CPMK-4 | Menjalankan Locust 100 users & analisis P95/P99 bottleneck | 4.5 jam |
| **M14** | AI Security | CPMK-4 | Menerapkan rate limit & guardrails terhadap prompt injection | 4.5 jam |
| **M15** | FE Integration | CPMK-2,3 | E2E FE→AI backend dengan CORS/SSE & auth | 4.5 jam |
| **M16** | Demo Day | CPMK-1-4 | Sidang produk terpadu & portofolio | 2.8 jam — **UAS** |

---

## 3. Rincian Materi per Modul

### MODUL 1 — Pengantar AI-as-a-Service (Mg1)
**Topik:** Definisi AIaaS, embedded vs service vs serverless, latensi (P50/P95) vs throughput (RPS) vs cost/GPU-hour  
**Sub-topik:** Studi kasus: AI service Tokopedia (rekomendasi), SatuSehat (NLP), Gojek (routing) — analisis arsitektur  
**Aktivitas Lab:** Setup env: `conda create -n sti726 python=3.11`, install onnxruntime-gpu, docker --gpus check, clone template repo  
**Output:** Setup check screenshot, quiz AIaaS  
**Sumber:** Huyen Ch.1, NVIDIA AIaaS WP, ONNXRuntime intro

### MODUL 2 — ONNX Export (Mg2)
**Topik:** ONNX opset, `torch.onnx.export` (input_names, dynamic_axes, export_params), ONNX checker, simplifier, Netron  
**Hands-on:** Ekspor ResNet18 (vision) + DistilBERT (text) → verifikasi output PyTorch vs ONNXRuntime (allclose atol 1e-4)  
**Latihan mandiri:** Ekspor model custom mahasiswa (dari STI-413)  
**Sumber:** PyTorch ONNX docs, ONNX tutorials

### MODUL 3 — TensorRT (Mg3)
**Topik:** TensorRT builder, FP16, INT8 PTQ calibration (500 samples), engine serialization, trtexec CLI, polygraphy  
**Hands-on:** ONNX→TensorRT FP32/FP16/INT8, benchmark latensi & throughput via trtexec, plot grafik trade-off  
**Sumber:** NVIDIA TensorRT Dev Guide

### MODUL 4 — FastAPI Inference API (Mg4 — TUGAS1)
**Topik:** FastAPI async, Pydantic v2 BaseModel, Uvicorn workers (4), /predict (multipart/file+JSON), /health, /metrics, OpenAPI (Swagger), exception handlers, logging JSON  
**Hands-on:** Scaffold `app/main.py` dengan lifespan, model load once, async inference (run_in_executor untuk TRT), pytest client  
**Tugas 1 (20%):** Milestone1 — ONNX+TRT + FastAPI + Dockerfile + README benchmark (tabel latensi, RPS). Penilaian: konversi valid 25%, endpoint 30%, Docker 20%, docs 25%  
**Sumber:** FastAPI official, Uvicorn

### MODUL 5 — Inference Pipeline (Mg5)
**Topik:** Preprocess (resize 224, normalize ImageNet, tokenizer truncation), postprocess (softmax, NMS), validation (Pydantic), dynamic batching queue  
**Hands-on:** Implement batch aggregator (timeout 50ms, max batch 32), benchmark batch 1 vs 8 vs 32  
**Sumber:** Huyen Ch.5, HuggingFace tokenizers

### MODUL 6 — Docker GPU (Mg6)
**Topik:** Dockerfile multi-stage (nvidia/cuda:11.8-runtime → python:3.11-slim), NVIDIA Container Toolkit, layer caching, .dockerignore, docker-compose (api + redis placeholder)  
**Hands-on:** Build & run `--gpus all`, inspect cold-start (<5s), optimize image size (<800MB via slim)  
**Sumber:** Docker docs, NVIDIA Container Toolkit

### MODUL 7 — VectorDB Fundamentals (Mg7)
**Topik:** Embedding (SBERT all-MiniLM-L6-v2, OpenAI ada-002), cosine vs dot, HNSW (M=16, efConstruction=200), recall vs latency trade-off, Chroma vs Milvus vs pgvector  
**Demo:** Visualisasi 2D t-SNE 500 docs, query live  
**Sumber:** Milvus/Chroma docs, Sentence-Transformers

### MODUL 8 — UTS Live Coding (Mg8)
**Format:** 120m coding (ekspor ONNX opset 17, TensorRT INT8 via trtexec, FastAPI endpoint baru /classify) + 50m wawancara trade-off  
**Kisi:** Mg1-7, tanpa internet kecuali docs offline, template repo disediakan  
**Bobot:** 25%

### MODUL 9 — VectorDB Setup (Mg9)
**Topik:** Chroma persistent (`./chroma_db`), Milvus Lite, collection create, partition by fakultas/tahun, indexing params, hybrid search (BM25+vector)  
**Hands-on:** Ingestion 2K docs kampus dummy, evaluasi recall@5  
**Sumber:** Chroma/Milvus API

### MODUL 10 — RAG Pipeline (Mg10)
**Topik:** Loaders (PyPDF, Markdown), chunking (512 tokens, overlap 50, recursive splitter), embedding ingestion, top-k (k=4) retrieval, reranker cross-encoder (ms-marco-MiniLM)  
**Hands-on:** Notebook RAG E2E, evaluasi MRR & faithfulness manual  
**Sumber:** LangChain RAG tutorial, Lewis et al. 2020

### MODUL 11 — LLM Orchestration (Mg11)
**Topik:** LangChain chains (RetrievalQA), prompt templates (system+context+question), memory (conversation buffer), tool use, citation grounding ([1][2]), LlamaIndex query engine, streaming SSE  
**Hands-on:** CLI chatbot RAG dengan sitasi sumber & streaming token  
**Sumber:** LangChain, LlamaIndex, OpenAI API

### MODUL 12 — Scalable Queue (Mg12 — TUGAS2)
**Topik:** Celery worker (concurrency 4), Redis broker, task `inference.delay()`, result polling, Flower monitoring, FastAPI BackgroundTasks vs Celery trade-off  
**Hands-on:** FastAPI enqueue → worker inference → /result/{task_id}, benchmark queue throughput  
**Tugas2 (25%):** Milestone2 — RAG+VectorDB+Celery/Redis+docker-compose (api, worker, redis, chroma) + laporan faithfulness & queue throughput  
**Sumber:** Celery, Redis

### MODUL 13 — Load Testing (Mg13)
**Topik:** Locust locustfile (HttpUser, wait_time, ramp-up), k6 scripts, RPS, concurrency 10/50/100, P95/P99, failure%, bottleneck (GPU vs I/O)  
**Hands-on:** Run Locust 100 users 5 menit, analisis grafik, rekomendasi scaling (tambah worker vs batch size)  
**Sumber:** Locust, k6

### MODUL 14 — AI Security (Mg14)
**Topik:** Rate limiter (slowapi 60/min), input sanitization (max_tokens, regex), prompt injection (jailbreak, DAN, data exfil), guardrails (NeMo Guardrails, Rebuff), OWASP LLM Top10 (LLM01-LLM10)  
**Workshop:** Uji serangan dari dataset prompt-injection, implement mitigasi, test blocked rate ≥90%  
**Sumber:** OWASP LLM Top10 2023

### MODUL 15 — Full-Stack AI Integration (Mg15)
**Topik:** CORS (allow_origins), SSE/WebSocket streaming, JWT auth, FE client (Next.js fetch + SSE), error UX (retry, fallback), E2E test Playwright  
**Studio:** Integrasi kelompok, bug bash, screen record E2E  
**Sumber:** FastAPI CORS, Next.js

### MODUL 16 — Demo Day (Mg16 — UAS 30%)
**Agenda:** 12m presentasi (problem, arsitektur, benchmark, demo) + 8m Q&A + 5m live demo FE→AI + portofolio review  
**Panel:** Dosen + industri (opsional), rubrik 086_5  
**Syarat lulus:** Demo live berhasil, P95<1s (mock GPU T4), guardrails aktif, faithfulness ≥75%  
**Output:** Portofolio PDF + video 3 menit + repo final tag `v1.0`

---

## 4. Bahan Ajar & Sumber

| Jenis | Judul | Akses |
|---|---|---|
| Buku | Huyen, C. *Designing ML Systems* Ch.7-9 | Perpus FSTI / O'Reilly |
| Docs | ONNXRuntime, PyTorch ONNX, TensorRT, FastAPI, Docker, Milvus/Chroma, LangChain, LlamaIndex, Locust, OWASP LLM | Online |
| Paper | Lewis et al. RAG (2020), HNSW paper (Malkov 2016) | Scholar |
| Dataset | COCO-mini (500 img), IMDb-mini (1K), dokumen kampus dummy (2K MD) — privacy-safe | Lab drive |
| Video | NVIDIA GTC TensorRT, FastAPI tutorial (6 jam) | YouTube LMS |

---

## 5. Alat & Lingkungan

- Python 3.11, PyTorch 2.2, ONNX 1.16, ONNXRuntime-GPU 1.17, TensorRT 8.6, FastAPI 0.110, Uvicorn, Pydantic v2, Docker 24+, NVIDIA Container Toolkit, Chroma 0.4.18 / Milvus Lite 2.4, LangChain 0.1, Celery 5.3, Redis 7, Locust 2.19 |
- Lab GPU T4/RTX4060, GitHub Classroom, Docker Hub kampus, VS Code

---

## 6. Peta Keterampilan Bertahap (Skill Ladder)

```
Level 1 (Mg1-3): Konversi model → ONNX → TensorRT → benchmark
Level 2 (Mg4-6): FastAPI async service → Docker GPU → RPS benchmark
Level 3 (Mg7-11): VectorDB → RAG pipeline → LLM orchestration → faithfulness
Level 4 (Mg12-14): Queue scalability → load test → security guardrails
Level 5 (Mg15-16): FE integration → E2E product → Demo Day portfolio
```

Setiap level menjadi prasyarat level berikutnya; milestone1 & 2 adalah gate.

