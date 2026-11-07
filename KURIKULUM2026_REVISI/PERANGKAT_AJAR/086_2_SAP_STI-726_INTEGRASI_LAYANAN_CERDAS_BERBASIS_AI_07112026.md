# SAP — STI-726 INTEGRASI LAYANAN CERDAS BERBASIS AI

**Kode MK:** STI-726 | **Nama:** Integrasi Layanan Cerdas Berbasis AI / *AI-Based Smart Service Integration*  
**SKS:** 3 SKS (+P) | **Semester:** 7 | **Rumpun:** Sistem Cerdas & Sains Data — Core STI  
**Prasyarat:** STI-413 (ML), STI-416 (Web Back End) | **Dosen:** Tim Dosen Sistem Cerdas  
**Waktu:** 100 menit Teori + 170 menit Lab/Studio + 180 menit Mandiri per minggu (total 450 menit/minggu)  
**Revisi:** 07112026 | **Rujukan OBE:** Dok 005 (Struktur 8 Semester), 007 §38, 008 (Asesmen OBE), 043 (Guardrails)

---

## A. Deskripsi & Posisi MK

SAP ini merinci pelaksanaan 16 pertemuan berbasis **Case Method + PjBL + Lab Hands-on**. Bobot nilai: **Tugas1 20% (Mg4) + UTS 25% (Mg8) + Tugas2 25% (Mg12) + UAS 30% (Mg16)**. Kelulusan minimal **C (55)**. MK puncak jalur P1 - prasyarat STA-701 MLOps. Produk akhir berupa **AI Smart Service** (ONNX/TensorRT + FastAPI + RAG+VectorDB + Queue) yang terintegrasi ke FE/mobile dan dideploy via Docker — dievaluasi melalui **Demo Day**.

---

## B. CPMK & CPL Terkait

| CPMK | Rumusan (ABCD) | Bloom | CPL | Indikator |
|---|---|---|---|---|
| CPMK-1 | Mengoptimalkan & mengonversi model DL ke ONNX/TensorRT untuk latensi rendah | C4 | KK1 | Latensi turun ≥30%, engine valid |
| CPMK-2 | Membangun REST/gRPC Inference Service async via FastAPI+Docker throughput tinggi | C6 | P2,KK1 | RPS≥50, async endpoint, Docker GPU |
| CPMK-3 | Merancang & mengintegrasikan RAG via VectorDB+Milvus/Chroma+LLM minim halusinasi | C6 | KK1 | Faithfulness ≥80%, sitasi sumber |
| CPMK-4 | Mengevaluasi performa via Load Testing & pertahanan prompt injection | C5 | KK1 | Laporan P95/P99, guardrails aktif |

---

## C. Rencana Mingguan Detail (16 Minggu)

### MINGGU 1 — Pengantar AI-as-a-Service (AIaaS)
**Sub-CPMK:** Menguraikan arsitektur AIaaS & tantangan inferensi (C2)  
**Bahan Kajian:** Model serving patterns (embedded vs service), latensi vs throughput vs biaya, batching real-time  
**Media:** Slide AIaaS, arsitektur Tokopedia/Gojek (studi kasus), GPU lab  
**Metode:** Kuliah interaktif 100m + Lab setup ONNX Runtime & Docker GPU toolkit 170m + Mandiri instalasi env 180m  
**Tugas:** Setup check: `onnxruntime-gpu`, `docker --gpus`, FastAPI hello-world push ke GitHub Classroom  
**Asesmen:** Formatif — quiz 10 soal AIaaS (non-graded)  
**Sumber:** [A1] Ch.1, NVIDIA AIaaS whitepaper, ONNXRuntime docs

### MINGGU 2 — Model Export ke ONNX
**Sub-CPMK:** Mengekspor model PyTorch/TF ke ONNX (C3)  
**Bahan Kajian:** `torch.onnx.export`, opset version, dynamic axes, onnx checker & simplifier  
**Metode:** Case Method — ekspor ResNet18 & Mini-BERT, verifikasi numerik PyTorch vs ONNXRuntime  
**Lab:** Hands-on ekspor, visualisasi graf via Netron, benchmark awal  
**Mandiri:** E-Book ONNX tutorial, latihan ekspor model custom (180m)  
**Asesmen:** Formatif — notebook export terkumpul (pass/fail)  
**Sumber:** [B1][B2], ONNX tutorials

### MINGGU 3 — TensorRT & Hardware Acceleration
**Sub-CPMK:** Mengoptimalkan graf via TensorRT FP16/INT8 (C4)  
**Bahan Kajian:** TensorRT builder, FP16, INT8 calibration (PTQ), engine serialization, trtexec  
**Metode:** Case Method + Lab Coding — konversi ONNX→TensorRT, benchmark latensi 3 presisi  
**Lab:** Ukur latensi baseline vs FP16 vs INT8, catat P95 di spreadsheet  
**Asesmen:** Formatif — laporan mini benchmark 1 halaman  
**Sumber:** [A2] TensorRT Guide, NVIDIA blog

### MINGGU 4 — FastAPI Inference Service (TUGAS 1)
**Sub-CPMK:** Membangun Inference API berkecepatan tinggi via FastAPI async (C6)  
**Bahan Kajian:** FastAPI async def, Pydantic v2, Uvicorn workers, /predict, /health, OpenAPI, streaming response  
**Metode:** Kuliah 50m + Lab Hands-on 170m + Studio integrasi 50m  
**Praktikum:** Scaffold `app/main.py` dengan `/predict` (image/text), async inference, error handling, logging  
**Mandiri:** Finalisasi repo & benchmark report (180m)  
**Asesmen:** **TUGAS 1 (20%)** — Milestone Proyek 1: Repo berisi: (a) Model ONNX + TensorRT engine, (b) FastAPI service + Dockerfile, (c) README benchmark (latensi FP32 vs FP16 vs TRT, RPS), (d) OpenAPI screenshot. **Rubrik:** Konversi valid 25%, endpoint async 30%, Docker GPU 20%, benchmark & docs 25%. **Deadline:** Minggu 4 Jumat 23:59 WIB (GitHub release tag `milestone1`)  
**Sumber:** [B3] FastAPI, Uvicorn tuning

### MINGGU 5 — Inference Pipeline & Batching
**Sub-CPMK:** Merancang pipeline pre/post-processing real-time (C4)  
**Bahan Kajian:** Preprocessing (resize/normalize/tokenize), batching dinamis, buffer management, validation  
**Metode:** Case Method + Lab — implement batch aggregator, tes throughput batch=1 vs 8 vs 32  
**Asesmen:** Formatif — unit test pipeline (pytest)  
**Sumber:** [A1] Ch.5, HuggingFace tokenizers

### MINGGU 6 — Containerizing AI Workloads
**Sub-CPMK:** Mengemas inference service ke Docker GPU passthrough (C4)  
**Bahan Kajian:** Dockerfile multi-stage (python:3.11-slim + CUDA base), NVIDIA Container Toolkit, layer caching, docker-compose  
**Metode:** Lab Hands-on — build, run --gpus, inspect cold-start & image size optimization  
**Asesmen:** Formatif — `docker images` & `docker logs` evidence  
**Sumber:** [B4] Docker, NVIDIA docs

### MINGGU 7 — Vector Database Fundamentals
**Sub-CPMK:** Menguraikan konsep VectorDB & embedding (C2)  
**Bahan Kajian:** Embedding models (SBERT, OpenAI ada-002), cosine/Euclidean, HNSW indexing, recall vs latency  
**Metode:** Ceramah & Demo — visualisasi embedding 2D (t-SNE), query Chroma demo langsung  
**Lab:** Generate embedding untuk 500 dokumen dummy kampus, query top-k  
**Asesmen:** Formatif — quiz VectorDB 10 soal  
**Sumber:** [C1] Milvus/Chroma, Sentence-Transformers

### MINGGU 8 — UTS (Live Coding Lab Test)
**Sub-CPMK:** Evaluasi tengah semester — integrasi ONNX & FastAPI (C4-C6)  
**Materi UTS:** Ekspor PyTorch→ONNX (opset tertentu), konversi TensorRT INT8 (trtexec), bangun FastAPI endpoint baru dalam 120 menit  
**Metode:** Live Coding Lab Test 120m + Wawancara lisan 50m (jelaskan trade-off latensi)  
**Asesmen:** **UTS (25%)** — Rubrik: Fungsionalitas endpoint 40%, kebenaran konversi 30%, latensi benchmark 20%, penjelasan lisan 10%. Susulan H+7 dengan surat.  
**Sumber:** Bank soal Mg1-7

### MINGGU 9 — VectorDB Setup (Chroma/Milvus)
**Sub-CPMK:** Mengonfigurasi VectorDB untuk ingestion (C3)  
**Bahan Kajian:** Chroma persistent vs Milvus Lite, collection, partition, indexing params (M, efConstruction)  
**Metode:** Kuliah 50m + Lab setup Chroma/Milvus, ingestion 2K dokumen, benchmark query  
**Asesmen:** Formatif — CRUD vector & recall@5 ≥80%  
**Sumber:** [C1][C2] docs

### MINGGU 10 — RAG Architecture
**Sub-CPMK:** Membangun pipeline RAG (C6)  
**Bahan Kajian:** Document loaders (PDF/MD), chunking (size 512, overlap 50), embedding ingestion, top-k retrieval, reranker (cross-encoder)  
**Metode:** Case Method + Lab — RAG notebook end-to-end, evaluasi retrieval (MRR)  
**Asesmen:** Formatif — notebook RAG + MRR report  
**Sumber:** [C3] LangChain RAG, Lewis et al.

### MINGGU 11 — LLM Orchestration
**Sub-CPMK:** Mengintegrasikan RAG+LLM via LangChain/LlamaIndex (C6)  
**Bahan Kajian:** LangChain chains, prompt templates, memory, tool use, citation grounding, LlamaIndex query engine  
**Metode:** Lab Coding — chatbot RAG dengan sitasi sumber, streaming SSE  
**Asesmen:** Formatif — demo CLI chatbot dengan sitasi  
**Sumber:** [C4] LangChain, OpenAI API

### MINGGU 12 — Scalable Serving: Celery/Redis (TUGAS 2)
**Sub-CPMK:** Mengimplementasikan async batching via Redis Queue / Celery (C4)  
**Bahan Kajian:** Celery worker, Redis broker, task queue, result backend, flower monitoring, background batching  
**Metode:** Kuliah 50m + Lab Hands-on — FastAPI enqueue → Celery worker inference → polling result  
**Asesmen:** **TUGAS 2 (25%)** — Milestone Proyek 2: (a) RAG service + VectorDB persisten, (b) Celery/Redis queue + worker, (c) docker-compose (api, worker, redis, chroma), (d) Laporan faithfulness & queue throughput. **Rubrik:** RAG faithfulness 35%, queue architecture 30%, compose runnable 20%, docs 15%. **Deadline:** Minggu 12 Jumat 23:59  
**Sumber:** [B5] Celery, Redis, FastAPI BackgroundTasks

### MINGGU 13 — Load Testing (Locust/k6)
**Sub-CPMK:** Melakukan Load Testing layanan inferensi (C4)  
**Bahan Kajian:** Locust locustfile, k6 scripts, RPS, concurrency, P95/P99, failure rate, ramp-up  
**Metode:** Lab Testing Session — run Locust 100 users, analisis bottleneck (GPU vs I/O)  
**Asesmen:** Formatif — laporan HTML Locust + rekomendasi scaling 1 halaman  
**Sumber:** [D1] Locust, k6

### MINGGU 14 — AI Security: Guardrails & Prompt Injection
**Sub-CPMK:** Menerapkan pengamanan API AI: rate limiting & prompt injection defense (C4)  
**Bahan Kajian:** slowapi rate limiter, input sanitization, prompt injection datasets, guardrails (NeMo Guardrails/Rebuff), OWASP LLM Top10  
**Metode:** Case Workshop — uji serangan (jailbreak, data exfiltration) & mitigasi, implement guardrails  
**Asesmen:** Formatif — security test report (blocked vs passed)  
**Sumber:** [D2] OWASP LLM, Guardrails AI

### MINGGU 15 — Full-Stack AI Integration
**Sub-CPMK:** Mengintegrasikan layanan AI ke FE/mobile tim (C6)  
**Bahan Kajian:** CORS, SSE/WebSocket streaming, auth JWT, FE client (Next.js), error UX  
**Metode:** PjBL Studio — integrasi kelompok, E2E test FE→AI backend, bug bash  
**Asesmen:** Formatif — demo E2E live (screen record)  
**Sumber:** [B3] FastAPI CORS, Next.js

### MINGGU 16 — UAS Demo Day & Portofolio
**Sub-CPMK:** Demonstrasi produk integrasi AI terpadu & portofolio (C6)  
**Materi:** Sidang Demo Day panel industri + dosen, presentasi 12 menit + Q&A 8 menit + live demo  
**Metode:** Demo Day & Defense 170m — penilaian panel (teknis, bisnis, etika)  
**Asesmen:** **UAS (30%)** — Rubrik: Fungsionalitas E2E 30%, latensi & load test 20%, RAG faithfulness 20%, security & docs 15%, presentasi 15%. **Syarat lulus:** Demo live berhasil, P95 <1s (mock GPU), guardrails aktif.  
**Sumber:** Rubrik UAS 086_5, template portofolio

---

## D. Tugas & Penugasan Terstruktur

| Tugas | Output Wajib | Bobot | Deadline | Kriteria |
|---|---|---|---|---|
| **Tugas 1 Mg4** | Repo milestone1 + benchmark report + Dockerfile | 20% | Mg4 Jumat | Runnable, latensi terukur, docs lengkap |
| **UTS Mg8** | Live coding ONNX+FastAPI | 25% | Mg8 | Fungsional & lisan |
| **Tugas 2 Mg12** | Repo milestone2 + docker-compose + faithfulness report | 25% | Mg12 Jumat | RAG ≥75%, queue work |
| **UAS Mg16** | Demo Day + portofolio PDF + video 3 menit | 30% | Mg16 | E2E + security |

**Keterlambatan:** -10% per hari, maks 3 hari. **Plagiarisme code:** MOSS check, >30% similarity = 0.

---

## E. Aturan Perkuliahan

- Kehadiran minimal 80% (Teori+Lab). Izin sakit dengan surat H+3.
- Lab GPU booking via sistem; dilarang mining.
- Etika AI: disclosure hallucination, tidak menyalahgunakan LLM untuk plagiarisme, guardrails wajib aktif saat demo.
- Kolaborasi diperbolehkan untuk diskusi, tetapi repo milestone bersifat tim (bukan copy-paste antar tim).

---

## F. Rujukan Mingguan

- Mg1-4: Huyen Ch.1,7-9; ONNXRuntime; FastAPI; NVIDIA TensorRT
- Mg5-6: Docker docs; NVIDIA Container Toolkit
- Mg7-12: Milvus/Chroma; LangChain/LlamaIndex; Celery/Redis; Lewis et al. RAG
- Mg13-14: Locust/k6; OWASP LLM Top10
- Mg15-16: Next.js, SSE/WebSocket, portofolio template

