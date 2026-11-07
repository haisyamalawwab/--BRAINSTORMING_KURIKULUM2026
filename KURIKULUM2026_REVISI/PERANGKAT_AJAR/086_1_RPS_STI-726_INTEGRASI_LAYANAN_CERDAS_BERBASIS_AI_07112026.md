# RPS — STI-726 INTEGRASI LAYANAN CERDAS BERBASIS AI

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI  
**Semester:** 7 | **Kode:** STI-726 | **Nama MK (EN):** AI-Based Smart Service Integration  
**SKS / Tipe:** 3 SKS / +P — 100 menit Teori + 170 menit Praktikum Lab + 180 menit Mandiri / minggu  
**Rumpun MK:** Sistem Cerdas & Sains Data (Core STI — Wajib Prodi)  
**Prasyarat:** STI-413 Machine Learning, STI-416 Web Back-End Development (Lulus ≥ C)  
**Dosen Pengampu:** Tim Dosen Sistem Cerdas | **Koordinator MK:** Kaprodi SISTEKIN  
**Kelas / Kuota:** A-B / 40 mhs/kelas | **Bahasa Pengantar:** Indonesia / Inggris (istilah teknis)  
**Revisi:** 07112026 | **Dokumen:** 005, 007 §38, 008, 043 | **Status:** WAJIB — CPL P2 & KK1

---

## 1. Identitas & Pemetaan Makro Kurikulum

| Atribut | Spesifikasi OBE |
|---|---|
| **Kode & Nama MK** | STI-726 Integrasi Layanan Cerdas Berbasis AI |
| **Semester / Rumpun** | Semester 7 / Sistem Cerdas & Sains Data — Core STI (28 MK Core, 79 SKS total) |
| **Prasyarat** | STI-413 (ML) & STI-416 (Web Back-End) — mahasiswa wajib menguasai Python, PyTorch/TensorFlow, REST API, Docker dasar |
| **CPL Dibebankan** | **P2** — Arsitektur AI-as-a-Service & SI Enterprise; **KK1** — Rekayasa Sistem Cerdas & Model AI (IS2020 BK-AI01, BK-IS18; IT2017 KK1) |
| **Profil Lulusan (PL)** | PL-1 Intelligent Information Systems Developer & AI Engineer (Peminatan P1: Integrated Smart Systems) |
| **PEO Terkait** | PEO-1 Professional Practice, PEO-3 Research & Lifelong Learning |
| **BoK APTIKOM** | BK-AI03 Model Serving & Deployment, BK-IS02 Pipeline Data, BK-IS18 Machine Learning & AI Engineering |
| **Level KKNI** | Level 6 — Mampu merancang & mengintegrasikan layanan AI produksi dengan latensi rendah & throughput tinggi |

**Kontribusi ke Kurikulum:** MK puncak (capstone-teknis) jalur P1 sebelum STA-701 MLOps. Menjembatani STI-413/624 (pemodelan) ke layanan produksi (STI-728 inovasi). Menjadi prasyarat STA-701.

---

## 2. Deskripsi Mata Kuliah

Mata kuliah ini membekali mahasiswa kemampuan **end-to-end AI Service Integration**: dari optimasi model (ONNX, TensorRT FP16/INT8), pembangunan **Inference Service** asinkron berkinerja tinggi (FastAPI + Docker GPU), hingga **Retrieval-Augmented Generation (RAG)** dengan Vector Database (Milvus/Chroma) dan orkestrasi LLM (LangChain/LlamaIndex). Mahasiswa juga mempelajari **scalability** (Celery/Redis queue, batching), **observability** (load testing Locust/k6, P95/P99 latency), serta **security** (rate limiting, prompt-injection defense, guardrails). Pembelajaran berbasis **PjBL + Case Method** dengan produk akhir: **AI Smart Service terintegrasi ke aplikasi web/mobile tim** yang dideploy sebagai container dan dievaluasi via Demo Day.

**Relevansi Industri:** AI Engineer, ML Engineer, AI Platform Engineer, RAG Engineer — mengisi kebutuhan AIaaS di perbankan, kesehatan, e-commerce, dan pemerintahan.

---

## 3. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan

| Kode CPL | Deskripsi CPL SISTEKIN 2026 | Indikator Pencapaian MK |
|---|---|---|
| **P2** | Menguasai konsep teoretis SI, analisis & perancangan sistem, arsitektur enterprise, metodologi SDLC & proses bisnis untuk transformasi digital | Mahasiswa mampu merancang arsitektur AI-as-a-Service yang selaras dengan arsitektur enterprise & SDLC |
| **KK1** | Mampu menganalisis, merancang, mengembangkan sistem informasi cerdas terintegrasi AI (ML, NLP, Vision, DSS) | Mahasiswa mampu membangun layanan inferensi AI produksi: ONNX/TensorRT, FastAPI, RAG+VectorDB, dengan evaluasi performa & keamanan |

**Pemetaan BoK:** BK-AI03 (Model Serving), BK-IS18 (ML Engineering), BK-IS02 (Data Pipeline), IT2017 KK1.

---

## 4. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Bloom

| Kode CPMK | Rumusan CPMK (A-B-C-D) | Bloom | CPL | Indikator Kinerja |
|---|---|---|---|---|
| **CPMK-1** | Mahasiswa (A) mampu **mengoptimalkan & mengonversi** model DL terlatih (B) ke ONNX & TensorRT (C) untuk inferensi latensi rendah (D) | C4 Analyze | KK1 | Konversi berhasil, latensi turun ≥30% vs baseline PyTorch, laporan benchmark P95 |
| **CPMK-2** | Mahasiswa (A) mampu **membangun** REST/gRPC Inference Service asinkron (B) via FastAPI + Docker (C) dengan throughput tinggi (D) | C6 Create | P2, KK1 | FastAPI async endpoint, Docker GPU passthrough, RPS ≥50 req/s, OpenAPI docs |
| **CPMK-3** | Mahasiswa (A) mampu **merancang & mengintegrasikan** sistem RAG (B) via VectorDB Milvus/Chroma + LLM API (C) akurat minim halusinasi (D) | C6 Create | KK1 | Pipeline chunk→embed→retrieve→generate, evaluasi faithfulness ≥80%, sitasi sumber |
| **CPMK-4** | Mahasiswa (A) mampu **mengevaluasi** performa layanan AI (B) via Load Testing Locust, monitoring latensi & pertahanan prompt-injection (C) secara kritis (D) | C5 Evaluate | KK1 | Laporan Locust (P95/P99), dashboard latensi, uji guardrails & rate limiter |

**Keterkaitan CPMK-CPL:** CPMK-1→KK1, CPMK-2→P2+KK1, CPMK-3→KK1, CPMK-4→KK1. Semua bermuara pada PL-1.

---

## 5. Prasyarat Pengetahuan & Keterampilan Awal

- Python lanjut (async/await, typing), PyTorch/TensorFlow, REST API & JSON, SQL/NoSQL dasar
- Linux & Docker dasar (Dockerfile, volume, port mapping)
- Statistik ML (train/val/test, metrik akurasi, confusion matrix) dari STI-413
- Web Back-End (routing, middleware, autentikasi JWT) dari STI-416
- **Diagnostic Test Minggu 1:** Quiz 30 menit ONNX concept + coding FastAPI hello-world

---

## 6. Matriks Pembelajaran 16 Minggu (Sub-CPMK, Kajian, Metode, Asesmen)

| Mg | Sub-CPMK & Kemampuan Akhir (Bloom) | Bahan Kajian (BK) | Metode Pembelajaran (100T+170P+180M) | Asesmen & Bobot | Sumber |
|---|---|---|---|---|---|
| 1 | Menguraikan arsitektur AIaaS & trade-off latensi vs throughput (C2) | AI Model Serving, AIaaS pattern, batching vs real-time | Kuliah interaktif 100m + Lab Setup ONNX Runtime, Docker GPU 170m | Formatif: quiz konsep & setup check | [A1] Ch.1, [B1] ONNX docs, NVIDIA AIaaS whitepaper |
| 2 | Mengekspor model PyTorch/TF ke ONNX (C3) | ONNX opset, torch.onnx.export, verifikasi numerik | Case Method + Lab Coding ekspor ResNet/BERT 270m | Formatif: notebook export + onnx checker | [B2] ONNX tutorial, PyTorch export guide |
| 3 | Mengoptimalkan graf komputasi via TensorRT FP16/INT8 (C4) | TensorRT builder, quantization calibration, engine serialization | Case Method + Lab TensorRT 270m | Formatif: benchmark latensi FP32 vs FP16 | [A2] TensorRT Dev Guide, NVIDIA blog |
| **4** | **Membangun Inference API FastAPI async berkinerja tinggi (C6)** | FastAPI async, Pydantic, Uvicorn workers, /predict & /health | Kuliah 100m + Lab Hands-on 170m | **TUGAS 1 (20%)** — Milestone 1: ONNX+FastAPI repo + README benchmark | [B3] FastAPI official, Uvicorn docs |
| 5 | Merancang pipeline pre/post-processing real-time (C4) | Image/text preprocessing, batching, buffer, pydantic validators | Case Method + Lab Coding 270m | Formatif: pipeline unit test | [A1] Ch.5, HuggingFace tokenizer guide |
| 6 | Mengemas inference service ke Docker GPU passthrough (C4) | NVIDIA Container Toolkit, Dockerfile multi-stage, --gpus | Lab Hands-on Docker build & push 270m | Formatif: image size & cold-start log | [B4] Docker docs, NVIDIA Container Toolkit |
| 7 | Menguraikan konsep VectorDB & embedding (C2) | Cosine similarity, HNSW, embeddings (SBERT/OpenAI) | Ceramah & Demo Chroma/Milvus 270m | Formatif: visualisasi embedding 2D | [C1] Milvus docs, Chroma guide, Sentence-Transformers |
| **8** | **UTS — Ujian Koding Terjadwal: Optimasi ONNX & FastAPI Inference Server** | Ujian praktik Live Coding Lab 120m + wawancara 50m | Live Coding Test | **UTS (25%)** — Evaluasi Proyek 50% + Ujian Praktik | Soal UTS terkurasi (OnTime) |
| 9 | Mengonfigurasi VectorDB Chroma/Milvus untuk ingestion (C3) | Collection, partition, indexing, hybrid search | Kuliah 100m + Lab 170m setup Milvus Lite/Chroma | Formatif: CRUD vector & recall@k | [C1] Milvus, [C2] Chroma API |
| 10 | Membangun pipeline RAG: chunking, embedding, retrieval (C6) | Document loaders, chunk overlap, top-k retrieval, reranker | Case Method + PjBL Lab 270m | Formatif: RAG notebook + retrieval eval | [C3] LangChain RAG tutorial, LlamaIndex |
| 11 | Mengintegrasikan RAG+LLM via LangChain/LlamaIndex (C6) | Prompt templates, chains, memory, tool use, citations | Case Method + Lab Coding 270m | Formatif: demo RAG chatbot CLI | [C4] LangChain docs, OpenAI API guide |
| **12** | **Mengimplementasikan scalable serving: Celery/Redis queue & background worker (C4)** | Task queue, Redis broker, Celery worker, async batching | Kuliah 100m + Lab 170m | **TUGAS 2 (25%)** — Milestone 2: RAG + Queue + Docker Compose | [B5] Celery, Redis docs, FastAPI BackgroundTasks |
| 13 | Melakukan Load Testing via Locust/k6 (C4) | RPS, concurrency, P95/P99, ramp-up, failure rate | Lab Testing Session 270m | Formatif: laporan Locust HTML | [D1] Locust docs, k6 guide |
| 14 | Menerapkan pengamanan API AI: rate limit & prompt injection defense (C4) | Rate limiter (slowapi), input sanitization, guardrails, OWASP LLM Top10 | Case Workshop 270m | Formatif: uji serangan prompt injection dataset | [D2] OWASP LLM, Rebuff/Guardrails AI |
| 15 | Mengintegrasikan layanan AI ke front-end/mobile tim (C6) | CORS, WebSocket/SSE streaming, FE client, auth | PjBL Studio 270m — integrasi lintas kelompok | Formatif: E2E demo FE→AI backend | [B3] FastAPI CORS, Next.js/React |
| **16** | **UAS — Sidang Demonstrasi Produk Integrasi AI Terpadu & Portofolio** | Demo Day panel industri + defense portofolio | Demo & Defense 170m | **UAS (30%)** — Demo Day + Portofolio + Laporan Akhir | Rubrik UAS (084_5) |

**Total Beban:** Teori 100m ×16 = 1600m, Lab 170m ×14 = 2380m, Mandiri 180m ×16 = 2880m. **Bobot nilai:** Tugas1 20% + UTS 25% + Tugas2 25% + UAS 30% = 100%.

---

## 7. Pengalaman Belajar Mahasiswa (Student Learning Experience)

- **Case Method (30%):** Bedah kasus AIaaS Tokopedia, Gojek, Kemenkes SatuSehat — analisis latensi & biaya GPU
- **PjBL (50%):** Proyek bertahap: Milestone1 (ONNX+API) → Milestone2 (RAG+Queue) → Integrasi FE + Demo Day
- **Team-Based (4-5 org):** Role: ML Engineer, Backend Engineer, MLOps/Infra, QA/Security, PM/Docs
- **Industry Guest:** Engineer dari NVIDIA/Nutrix AI (Minggu 6 & 14)
- **Open Source:** Kontribusi dokumentasi ONNX model zoo kampus

---

## 8. Asesmen & Evaluasi (Ringkasan — Detail di Dokumen 086_4)

| Komponen | Bentuk | CPMK | Bobot | Kriteria Kelulusan |
|---|---|---|---|---|
| **Tugas 1 (Mg4)** | Milestone Proyek 1: ONNX conversion + FastAPI + Docker + benchmark report | CPMK-1,2 | 20% | Latensi turun ≥20%, RPS terukur, repo runnable |
| **UTS (Mg8)** | Live Coding: ekspor ONNX, TensorRT INT8, FastAPI async endpoint + lisan | CPMK-1,2 | 25% | Fungsionalitas 60% + kebenaran konversi |
| **Tugas 2 (Mg12)** | Milestone Proyek 2: RAG (Chroma/Milvus) + LangChain + Celery/Redis + Compose | CPMK-3 | 25% | Retrieval faithfulness ≥75%, queue berfungsi |
| **UAS (Mg16)** | Demo Day + Portofolio: E2E AI service + FE + load test + security report | CPMK-1 s.d. 4 | 30% | Demo live, P95 <500ms (mock), guardrails aktif |

**Remedial:** Maksimal 1× untuk Tugas, UTS/UAS susulan terjadwal. **Plagiarisme:** Turnitin ≤20% untuk laporan, code plagiarism via MOSS.

---

## 9. Sumber Belajar Utama

1. [A1] Huyen, C. — *Designing Machine Learning Systems* (O'Reilly, 2022) Ch.7-9 Model Serving
2. [A2] NVIDIA — *TensorRT Developer Guide* & *Triton Inference Server Docs* (2024)
3. [B1] ONNX Runtime Official Documentation — https://onnxruntime.ai
4. [B2] PyTorch ONNX Export — https://pytorch.org/docs/stable/onnx.html
5. [B3] FastAPI Documentation — https://fastapi.tiangolo.com
6. [B4] Docker & NVIDIA Container Toolkit Docs
7. [C1] Milvus & Chroma Documentation (VectorDB)
8. [C2] LangChain & LlamaIndex RAG Tutorials
9. [C3] Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive Tasks* (NeurIPS 2020)
10. [D1] Locust & k6 Load Testing Docs
11. [D2] OWASP Top 10 for LLM Applications (2023)
12. [E1] AWS/GCP AIaaS Architecture Whitepapers

---

## 10. Media & Fasilitas

- Lab GPU (NVIDIA RTX 4060/T4, 32 users) + Cloud credits (GCP/AWS educate)
- Docker Hub kampus, GitHub Classroom, MLflow Model Registry (opsional)
- Dataset: COCO-mini, IMDb-mini, dokumen kampus dummy untuk RAG (privacy-safe)
- Tools: Python 3.11, PyTorch 2.x, ONNX Runtime, TensorRT 8.x, FastAPI, Milvus/Chroma, LangChain, Locust

---

## 11. Prinsip 5 Pilar SISTEKIN (Integrasi di MK)

- **Academic Excellence:** Benchmark kuantitatif (P95/P99), review arsitektur, publikasi model card
- **Vocational Excellence:** Produk deployable (Docker) siap portofolio & magang AI Engineer
- **Character Building:** Etika AI (bias, hallucination disclosure), keamanan prompt, tanggung jawab deployment
- **Competitive Excellence:** Benchmarking kompetitif antar-kelompok, leaderboard RPS & retrieval accuracy
- **Community Empowerment:** AI service untuk mitra desa/kampus (chatbot akademik, layanan aduan cerdas)

---

## 12. Rencana Tindak Lanjut & Evaluasi Mutu

- **Evaluasi Tengah Semester:** Survey kepuasan, analisis drop-rate Lab Mg3-4
- **Continuous Improvement:** Retrospektif Milestone1→2, update ONNX opset tiap tahun
- **Tracer:** Tracking lulusan ke peran AI Engineer/MLOps (6 bulan)

---

*Dokumen RPS ini sah setelah disahkan Kaprodi & Senat FSTI. Perubahan bobot/asesmen wajib melalui rapat kurikulum.*

