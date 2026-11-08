# 092_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STA-703 — Pengawasan Cerdas dan Analitika IoT

**Identitas:** `STA-703` Pengawasan Cerdas dan Analitika IoT · Semester 7 · 3 SKS (+P) · Prasyarat `STI-624`, `STI-521` · PL PL-1, PL-2 · PEO PEO-1, PEO-3 · IRM M.

## Identitas dan pengesahan

Prodi S1 SISTEKIN FSTI UWG. Koordinator, dosen dan tanggal pengesahan diisi oleh program studi. Beban mingguan: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. PT = tugas terstruktur; BM = belajar mandiri.

## CPL dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| CPL-09 (KK1) | Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri. | M |
| CPL-07 (P3) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. | M |
| CPL-11 (KK3) | Mampu merancang, mengintegrasikan, dan mengelola infrastruktur komputasi awan (Cloud/DevOps), sistem sensor cerdas (IoT), dan ketahanan siber (*Cybersecurity*) secara andal, terukur, dan aman. | M |

## CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD Dok 043 | Bloom | CPL |
| --- | --- | --- | --- |
| CPMK-1 | Mahasiswa (*A*) mampu **melatih dan mengoptimalkan** model deteksi objek modern (YOLOv8/YOLOv10) (*B*) pada dataset CCTV kustom (*C*) dengan mAP $\ge 0.80$ (*D*). | C4 | `CPL-09` (`KK1`) |
| CPMK-2 | Mahasiswa (*A*) mampu **mengimplementasikan** algoritma pelacakan multi-objek (ByteTrack / DeepSORT) dan pengenalan wajah biometrik (*B*) pada stream video RTSP real-time (*C*) dengan frame rate stabil $\ge 25$ FPS (*D*). | C4 | `CPL-09` (`KK1`) |
| CPMK-3 | Mahasiswa (*A*) mampu **mengonversi dan mendeploy** model vision cerdas (*B*) pada perangkat komputasi tepi (*Edge AI: NVIDIA Jetson / Raspberry Pi 5*) menggunakan TensorRT/OpenVINO (*C*) secara optimal (*D*). | C6 | `CPL-07` (`P3`), `CPL-11` (`KK3`) |
| CPMK-4 | Mahasiswa (*A*) mampu **membangun** sistem pengawasan cerdas terpadu (*B*) dengan trigger alarm otomatis ke broker MQTT dan dasbor monitoring (*C*) secara andal (*D*). | C6 | `CPL-07` (`P3`), `CPL-09` (`KK1`), `CPL-11` (`KK3`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Menerapkan video analytics dan deteksi objek real-time (YOLO) pada edge device. | CPMK-1 | C4 |
| Sub-CPMK-1.2 | Menganalisis alur pengolahan citra dan pelacakan objek/re-identification. | CPMK-1 | C4 |
| Sub-CPMK-2.1 | Mengintegrasikan kamera dan sensor untuk akuisisi data pengawasan. | CPMK-2 | C4 |
| Sub-CPMK-2.2 | Mengirim data telemetri dari edge ke platform secara real-time. | CPMK-2 | C4 |
| Sub-CPMK-3.1 | Membangun dashboard monitoring IoT untuk visualisasi analitik. | CPMK-3 | C6 |
| Sub-CPMK-3.2 | Mengembangkan pipeline analitik smart surveillance end-to-end. | CPMK-3 | C6 |
| Sub-CPMK-4.1 | Mengevaluasi keandalan dan latensi sistem smart surveillance. | CPMK-4 | C6 |
| Sub-CPMK-4.2 | Menyempurnakan sistem pengawasan berdasarkan metrik akurasi deteksi. | CPMK-4 | C6 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-09` (`KK1`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-09` (`KK1`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-07` (`P3`), `CPL-11` (`KK3`) | — | — | 25% | — | 25% |
| CPMK-4 | `CPL-07` (`P3`), `CPL-09` (`KK1`), `CPL-11` (`KK3`) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan arsitektur Smart Surveillance dan analitik video Edge AI (C2) | Pengantar Smart Surveillance, Arsitektur CCTV IP, Edge vs Cloud Video Analytics | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 2 | Mampu memproses stream video real-time via OpenCV VideoCapture & RTSP (C3) | Real-Time Video Ingestion: Protokol RTSP, WebRTC, OpenCV Pipeline | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 3 | Mampu mengimplementasikan deteksi objek real-time via YOLOv8/YOLOv10 (C3) | Object Detection Pipeline: Arsitektur YOLOv8, Inference Engine, NMS | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 4 | Mampu menganotasi data dan melatih baseline deteksi pada split yang terpisah (C4) | Dataset Curation dan Pelatihan Awal YOLO: Anotasi Bounding Box, Augmentasi Data, Split dan Baseline | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 20% |
| 5 | Mampu melatih custom model YOLO untuk deteksi APD (Helm/Rompi) (C4) | Custom YOLO Training: Loss Curve Analysis, mAP50, mAP50-95 Optimization | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 6 | Mampu mengimplementasikan Multi-Object Tracking via ByteTrack / DeepSORT (C4) | Multi-Object Tracking (MOT): Kalmann Filter, Hungarian Matching, ByteTrack | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 7 | Mampu menerapkan deteksi intrusi zona terlarang dan Line Crossing (C4) | Behavioral Analytics: Virtual Tripwire, Polygon Zone Intrusion, Crowd Density | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Custom YOLO Training & Multi-Object Tracking Pipeline | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS 25% |
| 9 | Mampu mengimplementasikan pengenalan wajah biometrik via ArcFace/FaceNet (C4) | Face Recognition: Face Detection (RetinaFace), Embedding, Cosine Verification | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 10 | Mampu menguraikan tantangan komputasi tepi (Edge AI) & efisiensi daya (C2) | Edge AI Computing: Keterbatasan Memori, Disipasi Panas, Latensi | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 11 | Mampu mengoptimalkan model via Kuantisasi INT8/FP16 & TensorRT Engine (C5) | Model Compression: Post-Training Quantization, Pruning, TensorRT Engine | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 12 | Mampu mendeploy model inferensi pada hardware NVIDIA Jetson / RPi 5 (C6) | Edge Deployment: Setup NVIDIA Jetson Nano / Orin, CSI Camera Interface | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 25% |
| 13 | Mampu menghubungkan deteksi visual AI ke broker MQTT untuk memicu alarm (C4) | Edge IoT Integration: MQTT Alert Triggering, Relay Alarm, WhatsApp Alert | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 14 | Mampu mengimplementasikan sistem Automatic License Plate Recognition (ALPR) (C4) | Studi Kasus Industri: ALPR OCR (Plat Nomor Kendaraan) & Smart Parking | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 15 | Mampu membangun sistem smart surveillance terpadu pada area kampus/pabrik (C6) | PjBL Surveillance Studio: Integrasi Kamera CCTV, Edge AI, Alarm, & Dasbor | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Sistem Smart Surveillance Edge AI Terpadu | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Anotasi citra berizin dan latih/evaluasi deteksi objek pada split terpisah. Bukti: dataset sintetis/berizin, model dan metrik mAP |
| UTS | 8 | 25% | CPMK-2 | Terapkan pelacakan multiobjek pada video uji dan evaluasi frame rate. Bukti: kode tracking, video contoh dan hasil uji |
| Tugas 2 | 12 | 25% | CPMK-3 | Konversi model untuk edge, ukur latensi dan jelaskan batas perangkat. Bukti: artefak model, konfigurasi dan benchmark |
| UAS | 16 | 30% | CPMK-4 | Integrasikan deteksi, alarm MQTT dan dashboard; uji privasi dan keandalan. Bukti: kode, diagram, hasil uji dan demo |

## Pustaka utama dan pendukung

Dokumentasi [Ultralytics YOLO](https://docs.ultralytics.com/) dan [OpenCV](https://docs.opencv.org/).

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS16` *Artificial Intelligence*, `BK-IT14` *IoT & Smart Systems*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Video Analytics Real-Time, Deteksi Objek Edge (YOLO/MobileNet pada Jetson/Raspberry Pi), Multi-Camera Tracking, Analitik Aliran Sensor IoT Cerdas, Smart City Surveillance Privacy.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang pengkabelan mikrokontroler sensor dasar dari nol, perancangan dashboard BI finansial, training arsitektur transformer teks.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan sistem pengawasan cerdas terintegrasi AI edge dan jaringan IoT otonom.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Biometrik hanya pada data sintetis atau data yang memiliki persetujuan eksplisit; mAP/FPS adalah target Dok 043, bukan hasil yang dijamin. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
