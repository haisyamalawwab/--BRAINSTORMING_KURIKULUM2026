# 090_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STA-701 — MLOps dan Alur Pipa AI

**Identitas:** `STA-701` MLOps dan Alur Pipa AI · Semester 7 · 3 SKS (+P) · Prasyarat `STI-413`, `STI-726` · PL PL-1 · PEO PEO-1, PEO-3 · IRM M.

## Identitas dan pengesahan

Prodi S1 SISTEKIN FSTI UWG. Koordinator, dosen dan tanggal pengesahan diisi oleh program studi. Beban mingguan: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. PT = tugas terstruktur; BM = belajar mandiri.

## CPL dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| CPL-10 (KK2) | Mampu merekayasa pipeline data skala besar (*Data Engineering*), membangun model machine learning/deep learning, serta menerapkan MLOps untuk solusi analitik dan visualisasi data bisnis. | M |
| CPL-08 (P4) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | M |
| CPL-09 (KK1) | Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri. | M |

## CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD Dok 043 | Bloom | CPL |
| --- | --- | --- | --- |
| CPMK-1 | Mahasiswa (*A*) mampu **mengelola** pelacakan versi data dan eksperimen model (*B*) menggunakan Data Version Control (DVC) dan MLflow Tracking (*C*) secara terstruktur (*D*). | C4 | `CPL-10` (`KK2`) |
| CPMK-2 | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Training (CT) otomatis (*B*) menggunakan Kubeflow Pipelines / Apache Airflow (*C*) dengan trigger retraining teruji (*D*). | C6 | `CPL-08` (`P4`), `CPL-09` (`KK1`) |
| CPMK-3 | Mahasiswa (*A*) mampu **mendeploy dan memantau** model AI produksi (*B*) dengan strategi Canary/Shadow Deployment serta deteksi Data/Concept Drift (*C*) menggunakan Evidently AI dan Prometheus (*D*). | C5 | `CPL-09` (`KK1`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Menganalisis siklus hidup MLOps (CI/CD/CT) untuk model Machine Learning. | CPMK-1 | C4 |
| Sub-CPMK-1.2 | Mengelola eksperimen dan registry model menggunakan MLflow. | CPMK-1 | C4 |
| Sub-CPMK-2.1 | Mengotomasi retraining model dan monitoring data drift. | CPMK-2 | C6 |
| Sub-CPMK-2.2 | Menerapkan feature store untuk konsistensi data model. | CPMK-2 | C6 |
| Sub-CPMK-3.1 | Mendeploy model dengan strategi canary dan blue-green. | CPMK-3 | C5 |
| Sub-CPMK-3.2 | Mengevaluasi performa dan stabilitas pipeline AI di produksi. | CPMK-3 | C5 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-10` (`KK2`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-08` (`P4`), `CPL-09` (`KK1`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-09` (`KK1`) | — | — | 25% | 30% | 55% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan filosofi MLOps, DevOps vs MLOps, dan siklus hidup ML (C2) | Pengantar MLOps, Tingkat Kematangan MLOps, Tantangan Deployment AI | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 2 | Mampu mengonfigurasi pelacakan versi dataset via Data Version Control (DVC) (C3) | Data & Model Versioning: Setup DVC, Integrasi Remote Storage S3/GCS | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 3 | Mampu menerapkan validasi skema data otomatis via Great Expectations (C4) | Automated Data Validation: Great Expectations Skema Ingestion Data | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 4 | Mampu mengonfigurasi MLflow Tracking Server untuk logging eksperimen (C3) | Experiment Tracking: MLflow Server, Parameter Logging, Metrics Artifacts | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 20% |
| 5 | Mampu mengelola siklus hidup model di MLflow Model Registry (C4) | Model Governance: Model Registry Stages (Staging, Production, Archive) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 6 | Mampu merancang graf pipeline data science DAG menggunakan Apache Airflow (C4) | Workflow Orchestration: DAG Airflow, Python Operators, Task Scheduling | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 7 | Mampu membangun Continuous Training (CT) pipeline otomatis (C6) | Continuous Training Pipeline: Automated Model Retraining & Evaluation | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Setup DVC, MLflow Registry, & Airflow Pipeline | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS 25% |
| 9 | Mampu mengemas model terstandarisasi menggunakan BentoML / TorchServe (C4) | Model Packaging & Containerization: BentoML Service & REST Endpoint | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 10 | Mampu mendeploy inference service pada klaster Kubernetes via KServe (C4) | Cloud Native AI Serving: KServe / Seldon Core on Kubernetes | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 11 | Mampu mengonfigurasi strategi Canary Deployment & A/B Testing model (C4) | Advanced Rollout: Canary Releases, Blue-Green, Shadow Deployment Model | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 12 | Mampu mendeteksi Data Drift dan Concept Drift via Evidently AI (C5) | Model Monitoring: Deteksi Drift Statistik (Kolmogorov-Smirnov, PSI) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 25% |
| 13 | Mampu mengintegrasikan metrik observabilitas AI ke Prometheus & Grafana (C4) | AI Observability: Custom Inference Latency Metrics, GPU Utilization | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 14 | Mampu menerapkan Explainable AI (XAI) via SHAP dan LIME (C4) | Model Explainability & AI Fairness: Nilai Shapley & Interpretasi Fitur | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 15 | Mampu membangun pipeline end-to-end MLOps enterprise terpadu (C6) | PjBL MLOps Studio: Integrasi Penuh dari Commit Git ke Production Serving | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Pipeline MLOps Terpadu & Simulasi Drift Handling | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Versikan data dan lacak eksperimen MLflow; jelaskan sumber data dan model. Bukti: repositori DVC, eksperimen dan model card |
| UTS | 8 | 25% | CPMK-2 | Susun DAG continuous training, validasi data dan uji trigger retraining. Bukti: DAG, bukti eksekusi dan hasil validasi |
| Tugas 2 | 12 | 25% | CPMK-3 | Simulasikan canary/shadow dan deteksi drift dengan data yang terkendali. Bukti: konfigurasi serving, metrik dan hasil uji drift |
| UAS | 16 | 30% | CPMK-3 | Integrasikan registry, serving dan monitoring; jelaskan prosedur rollback. Bukti: pipeline, log, laporan dan demonstrasi |

## Pustaka utama dan pendukung

Dokumentasi [MLflow](https://mlflow.org/docs/latest/), [DVC](https://dvc.org/doc) dan [Airflow](https://airflow.apache.org/docs/).

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS18` *Machine Learning*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Lifecycle MLOps, Experiment Tracking (MLflow), Data Versioning (DVC), Containerization Model (Docker), Model Serving (FastAPI/Triton), CI/CD Pipeline for ML, Monitoring Data & Concept Drift.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang merancang arsitektur jaringan saraf tiruan CNN baru dari nol, pengembangan antarmuka grafis UI/UX bisnis.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menjamin model kecerdasan buatan dapat dideploy, dipantau, dan di-retrain secara otomatis di lingkungan produksi.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
