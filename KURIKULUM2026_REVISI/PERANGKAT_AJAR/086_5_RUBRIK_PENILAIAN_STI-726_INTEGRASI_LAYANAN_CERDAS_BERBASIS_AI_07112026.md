# RUBRIK PENILAIAN — STI-726 INTEGRASI LAYANAN CERDAS BERBASIS AI

**Kode:** STI-726 | **Nama:** Integrasi Layanan Cerdas Berbasis AI | **SKS:** 3 (+P)  
**Semester:** 7 | **Prasyarat:** STI-413, STI-416 | **CPL:** P2, KK1 | **CPMK:** 1 (C4), 2 (C6), 3 (C6), 4 (C5)  
**Komponen Nilai:** Tugas1 20% + UTS 25% + Tugas2 25% + UAS 30% = 100% | **Revisi:** 07112026 | **Rujukan:** 007 §38, 008, 043

---

## A. RUBRIK TUGAS 1 — Milestone Proyek 1: ONNX + FastAPI (20% — Mg4) — CPMK-1,2

| Aspek (Bobot) | Skor 4 — Sangat Baik (85-100) | Skor 3 — Baik (70-84) | Skor 2 — Cukup (55-69) | Skor 1 — Kurang (0-54) |
|---|---|---|---|---|
| **Konversi ONNX & TensorRT Valid (30%)** | ONNX checker pass, diff <1e-4, trtexec FP16 & INT8 sukses, engine load <1s, benchmark 4 presisi lengkap dengan grafik | ONNX pass, diff <1e-3, hanya FP16, benchmark 2 presisi | ONNX pass tetapi diff 1e-2, benchmark tidak lengkap | ONNX export gagal / checker fail, tidak ada benchmark |
| **Endpoint FastAPI Async & OpenAPI (30%)** | Async def benar, Pydantic validasi lengkap, /predict & /health & /metrics, Swagger docs lengkap dengan example, error handler 422/500, pytest 100% pass | Async sebagian sync, Pydantic ada, Swagger ada tetapi contoh kurang, error handler ada | Endpoint sync (blocking), Swagger minimal, tidak ada validasi | Endpoint tidak merespons 200, tidak ada OpenAPI |
| **Docker GPU Runnable (20%)** | Dockerfile multi-stage, image <800MB, --gpus passthrough, build <2m, cold-start <3s, logs JSON, .dockerignore lengkap | Image <1GB, --gpus ok, build <5m, cold-start <5s | Image >1.5GB, --gpus gagal fallback CPU, build >10m | Docker build gagal, tidak ada --gpus |
| **Benchmark & Dokumentasi (20%)** | README tabel latensi P50/P95 per presisi (PyTorch/ONNX/TRT FP16/INT8), analisis trade-off 200 kata, instruksi runnable copy-paste, screenshot Swagger, repo tag milestone1 | Tabel latensi ada tetapi tanpa P95, analisis singkat 100 kata, instruksi runnable | Tabel tidak lengkap (hanya 1 presisi), instruksi tidak lengkap | Tidak ada README benchmark, instruksi tidak runnable |

**Skor Tugas1 = Σ (skor_aspek × bobot) → konversi 0-100. Minimal 55 untuk lanjut ke UTS (remedial 7 hari jika <55).**

---

## B. RUBRIK UTS — Live Coding Lab Test: ONNX & FastAPI (25% — Mg8) — CPMK-1,2

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Fungsionalitas Endpoint Baru /classify (40%)** | Endpoint 200, JSON {label, score, latency_ms} valid, async, validasi input (max file size, mime), handle corrupted file 400, test curl sukses | 200 tetapi validasi kurang (tidak cek mime), handle error generik | 200 tetapi sync blocking, tidak ada handle error | Tidak 200 atau crash saat test |
| **Kebenaran Konversi ONNX→TRT (30%)** | ONNX opset 17 benar, dynamic axes batch, checker pass, trtexec INT8 sukses dengan calibration cache, engine load sukses, diff <1e-3 | ONNX pass tetapi tanpa dynamic axes, INT8 sukses tanpa calib cache, diff <1e-2 | ONNX export sukses tetapi checker fail (ops unsupported), INT8 gagal fallback FP16 | Export gagal, checker fail |
| **Latensi Benchmark (20%)** | trtexec log P95 <80% baseline FP32, melaporkan throughput (qps), grafik perbandingan | P95 < baseline tetapi tanpa throughput | P95 ≈ baseline (tidak ada optimasi) | Tidak melakukan benchmark |
| **Wawancara Lisan Trade-off (10%)** | Jelaskan FP16 vs INT8 (accuracy drop, calib), async vs sync (event loop, GIL), batching trade-off dengan jelas & contoh angka | Jelaskan 2 trade-off dengan benar tanpa angka | Jelaskan 1 trade-off benar, lainnya ragu | Tidak mampu menjelaskan |

**Penilaian:** Dosen + asisten lab (2 penilai), screen record sebagai bukti. Susulan H+7 soal setara.

---

## C. RUBRIK TUGAS 2 — Milestone Proyek 2: RAG + Queue (25% — Mg12) — CPMK-2,3

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **RAG Faithfulness & Sitasi (35%)** | Faithfulness ≥85% (RAGAS manual 10 queries), recall@5 ≥85%, sitasi [1][2] valid (ID dokumen ada), chunk 512/overlap50 rasional + reranker, minim halusinasi (0-1/10) | Faithfulness 75-84%, recall@5 70-84%, sitasi ada tetapi 1-2 invalid | Faithfulness 60-74%, recall@5 50-69%, sitasi tidak valid (hallucinated IDs) | Faithfulness <60%, tidak ada sitasi, recall@5 <50% |
| **Celery/Redis Queue Architecture (30%)** | Task `inference.delay()` asinkron, Redis broker, result polling /result/{id} dengan status PENDING/SUCCESS, timeout 30s, Flower dashboard, retry on failure, throughput ≥10 tasks/sec | Queue berfungsi tetapi polling sync (blocking), tanpa Flower, throughput 5-10/sec | Queue berfungsi tetapi tanpa status polling (hanya fire-and-forget), throughput <5/sec | Queue tidak berfungsi, task tidak dieksekusi worker |
| **Docker Compose Runnable E2E (20%)** | `docker compose up` sukses 4 services (api, worker, redis, chroma) dengan healthchecks, semua service up <30s, E2E curl /rag/query → /rag/result sukses, logs terpisah | Compose up sukses 4 services tetapi tanpa healthcheck, E2E manual (curl 2-step) sukses | Compose up 3 services (missing 1), E2E sebagian gagal | Compose gagal, service crash loop |
| **Laporan & Analisis (15%)** | REPORT_TUGAS2.md 3-5 hal: faithfulness table, queue throughput table, analisis halusinasi (contoh 2 queries), trade-off chunk size & top-k, instruksi runnable lengkap | Laporan 2-3 hal, ada faithfulness & throughput tetapi tanpa analisis halusinasi | Laporan 1-2 hal, hanya faithfulness tanpa throughput | Tidak ada laporan atau sangat tidak lengkap |

---

## D. RUBRIK UAS — Demo Day & Portofolio: E2E AI Service (30% — Mg16) — CPMK-1 s.d. 4

| Aspek (Bobot) | Skor 4 — Excellent (85-100) | Skor 3 — Good (70-84) | Skor 2 — Fair (55-69) | Skor 1 — Poor (0-54) |
|---|---|---|---|---|
| **Fungsionalitas E2E Live (30%)** | FE Next.js → FastAPI → VectorDB → LLM → response streaming sukses live (no mock), semua endpoint up, handle concurrent 2 users demo, error UX (retry) ada | E2E sukses tetapi tanpa streaming (polling saja), 1 endpoint minor gagal tetapi workaround | E2E sebagian gagal (RAG tidak merespons), fallback ke video rekaman | Demo gagal total (video saja tanpa live), service down |
| **Latensi & Load Test (20%)** | P95 <500ms (mock GPU T4, batch 1), RPS ≥50, Locust report HTML lengkap (ramp-up 10→100 users), analisis bottleneck (GPU vs I/O) & rekomendasi scaling (tambah worker) | P95 500ms-1s, RPS 30-49, Locust ada tetapi tanpa analisis bottleneck | P95 1-2s, RPS 15-29, Locust minimal (hanya 1 concurrency) | P95 >2s atau tidak ada Locust report |
| **RAG Faithfulness & Sitasi (20%)** | Faithfulness ≥80% (10 queries manual review), sitasi valid 9-10/10, zero hallucinated IDs, reranker relevan, jawaban grounded di dokumen | Faithfulness 70-79%, sitasi valid 7-8/10, 1 hallucinated | Faithfulness 60-69%, sitasi valid 5-6/10, 2-3 hallucinated | <60% atau sitasi tidak ada |
| **Security & Docs (15%)** | Rate limit 60/min aktif (slowapi), prompt injection blocked ≥90% (uji 20 payloads), input sanitization (max_tokens, regex), PORTFOLIO.pdf lengkap (arsitektur diagram, benchmark, security test, lesson learned, kontribusi individu), repo tag v1.0, video 3m | Rate limit aktif tetapi 100/min, blocked 75-89%, docs lengkap tetapi tanpa lesson learned | Rate limit ada tetapi tidak diuji, blocked 50-74%, docs tidak lengkap (tanpa diagram) | Tidak ada rate limit / guardrails, blocked <50%, docs sangat tidak lengkap |
| **Presentasi & Teamwork (15%)** | Presentasi 12m jelas (problem→arsitektur→benchmark→demo), Q&A menjawab trade-off dengan angka, peer eval seimbang (kontribusi 20-25% per org), time management tepat, handling pertanyaan sulit baik | Presentasi jelas tetapi Q&A ragu-ragu, peer eval 1 org dominan 40% tetapi diakui | Presentasi melebihi waktu 15m, Q&A banyak tidak terjawab, peer eval timpang tanpa penjelasan | Presentasi tidak terstruktur, tidak mampu jawab Q&A dasar, peer eval konflik |

**Catatan UAS:**
- **Peer Evaluation:** Setiap anggota menilai kontribusi rekan (20% per org ideal untuk tim 5). Jika 1 org <10% → investigasi, nilai individu bisa -30%.
- **Syarat lulus UAS:** Minimal skor 2 di semua aspek (tidak boleh ada skor 1). Jika ada skor 1 → remedial UAS (perbaikan 14 hari, nilai maks B).
- **Panel:** 2 dosen + 1 industri (opsional). Skor rata-rata panel.

---

## E. RUBRIK FORMATIF & KEHADIRAN (Non-Graded tetapi Gate UAS)

| Kriteria | Lulus | Tidak Lulus | Tindak Lanjut |
|---|---|---|---|
| **Kehadiran Teori+Lab** | ≥80% (13/16 pertemuan) | <80% | Tugas pengganti (paper review) atau tidak boleh UAS |
| **Formatif terkumpul** | ≥8/12 formatif (pass) | <8 | Remedial formatif 7 hari, jika tetap <8 tidak boleh UAS |
| **Etika AI** | Disclosure AI-assistance, guardrails aktif, tidak plagiasi | Plagiarisme MOSS>30% atau Turnitin>20% tanpa revisi | Nilai 0 komponen, sidang etik |

---

## F. KONVERSI NILAI AKHIR (NA) & YUDISIUM

```
NA = 0.20×Tugas1 + 0.25×UTS + 0.25×Tugas2 + 0.30×UAS + bonus (max +3)
Bonus: video demo berkualitas +2, kontribusi open-source model zoo (PR merged) +1
```

| NA | Huruf | Predikat | CPL Tercapai | Tindak Lanjut |
|---|---|---|---|---|
| 85-100 | A | Sangat Memuaskan — Lulus | Semua CPL ≥85% | Rekomendasi asisten lab / publikasi |
| 70-84 | B | Memuaskan — Lulus | CPL ≥70% | — |
| 60-69 | C | Cukup — Lulus Bersyarat | CPL minimal | Wajib bimbingan karir AI Engineer |
| 55-59 | D | Kurang — Tidak Lulus | CPL tidak tercapai | Remedial (maks 1×) |
| <55 | E | Gagal — Tidak Lulus | CPL tidak tercapai | Mengulang MK |

**Aturan yudisium tambahan:**
- Jika NA ≥60 tetapi UAS <50 → nilai akhir maksimal C (mencegah lulus tanpa produk)
- Jika UTS terindikasi free-rider (UTS <40 tetapi tugas tim tinggi) → wawancara validasi, bisa penyesuaian nilai tugas -20%
- Remedial tugas: perbaikan 7 hari, nilai maks 70 (B). Remedial UAS: 14 hari, nilai maks 70.

---

## G. LEMBAR PENILAIAN INDIVIDU (Contoh untuk 1 Mahasiswa — untuk Panel)

| Komponen | Skor 0-100 | Bobot | Nilai Terbobot | Catatan Penilai |
|---|---|---|---|---|
| Tugas1 (kelompok → individu via peer eval) |  | 20% |  | Peer eval factor: ... |
| UTS (individu) |  | 25% |  | — |
| Tugas2 (kelompok → individu) |  | 25% |  | Peer eval factor |
| UAS (kelompok→individu + Q&A individu) |  | 30% |  | Q&A individu: ... |
| **NA** |  | 100% |  | Huruf: ... |

**Tanda tangan penilai:** _________________ **Tanggal:** _______

---

## H. UMPAN BALIK & PERBAIKAN BERKELANJUTAN

- Feedback Tugas1 diberikan dalam 7 hari via GitHub Classroom inline comments
- Feedback UTS via lisan langsung + written summary 3 hari pasca UTS
- Feedback Tugas2 via PR review (requested changes)
- Feedback UAS via panel sheet + rekaman video (untuk refleksi)
- **Evaluasi rubrik tahunan:** Analisis distribusi skor (ideal kurva normal), revisi jika >70% mahasiswa skor 4 (terlalu mudah) atau >40% skor 1 (terlalu sulit)

---

*Rubrik ini mengikat. Perubahan rubrik pasca Mg1 memerlukan persetujuan rapat prodi & sosialisasi ulang.*

