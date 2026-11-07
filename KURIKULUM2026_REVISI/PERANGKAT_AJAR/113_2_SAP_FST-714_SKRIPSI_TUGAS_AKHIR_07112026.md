# 113_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## FST-714 — SKRIPSI / TUGAS AKHIR (*Undergraduate Thesis / Final Project*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-FST714` · **Bobot:** 6 SKS `Mandiri` (`Bimbingan & Riset Mandiri 480'`, `PT 0'`, `BM 0'` per pekan) · **Semester:** 8 — Tahap *Mastery*  
**Prasyarat:** Lulus `FST-613` Pra-Skripsi (Proposal Sah Bab 1–3) · ≥ 120 SKS · Kartu bimbingan minimal 8 pertemuan sebelum UTS  
**CPL:** `CPL-01`–`CPL-14` (14 CPL menyeluruh, Level **M**) · **4 Jalur Setara (Dok 009)**  
**Klaster Rubrik:** `K-4` (Tugas Akhir & Publikasi) · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pembimbing & Mahasiswa `FST-714` |
|---|---|
| **Struktur Waktu per Pekan** | **Riset Mandiri `400'–480'`:** Eksekusi riset sesuai logbook (coding, eksperimen, analisis, penulisan).<br>**Bimbingan Tatap Muka `80'–120'`:** Review artefak mingguan + arahan korektif (wajib bawa logbook, kode terbaru, draf tulisan).<br>**Administrasi LMS:** Unggah artefak + presensi bimbingan (kartu bimbingan digital) tiap pekan. |
| **Lokasi & Moda Bimbingan** | Bimbingan terjadwal di Lab KBK / Ruang Dosen (luring) + sinkron daring (Zoom/GMeet) bila mahasiswa magang di luar kota. Hybrid diperbolehkan maksimal 50% pertemuan bimbingan dengan persetujuan pembimbing. |
| **Perangkat & Akses Wajib** | Repo GitLab Prodi (private), MLflow/W&B untuk log eksperimen, Overleaf/Google Docs untuk naskah, Turnitin kampus, akun e-HKI DJKI, akses dataset/mitra (izin tertulis). |
| **Kewajiban Mahasiswa** | (1) Isi logbook harian (tanggal, jam kerja, aktivitas, kendala).<br>(2) Bawa artefak siap review tiap bimbingan (bukan datang kosong!).<br>(3) Patuh etika: tidak plagiasi, tidak fabrikasi data, lapor kegagalan eksperimen secara jujur.<br>(4) Jaga komunikasi proaktif (maks. balas pesan pembimbing 2×24 jam). |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** mengganti topik/judul tanpa persetujuan tertulis pembimbing & Kaprodi (mengulang siklus `FST-613`).<br>❌ **Dilarang** bimbingan tanpa kartu bimbingan yang ditandatangani.<br>❌ **Dilarang** sidang tanpa Turnitin <20% & tanpa persetujuan 2 pembimbing (atau 1 bila hanya 1 pembimbing). |
| **4 Jalur Diferensiasi** | SAP ini berlaku untuk semua jalur; penekanan artefak menyesuaikan: **J1 Riset** (eksperimen SOTA) · **J2 Industri** (TRL≥6 + surat mitra) · **J3 Startup** (MVP + traksi) · **J4 Publikasi** (artikel accepted). Detail artefak jalur lihat kolom Tugas 1/2/UAS. |

### Tabel Peta Cepat 16 Pertemuan SAP (Riset Mandiri 480' + Bimbingan)

| Pertemuan | Sub-CPMK | Topik Inti Riset & Bimbingan | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `1.1` | Finalisasi Pengumpulan & Pembersihan Dataset Etis + Setup Komputasi | 480' | Formatif (log) |
| **2** | `1.2` | Pembangunan Baseline Architecture / Pipeline Awal yang Reproduksibel | 480' | Formatif (repo) |
| **3** | `1.3` | Implementasi Algoritma Usulan / Modifikasi Metode Inti (Novelty) | 480' | Formatif |
| **4** | `1.3` | Eksperimen Batch-1 & Hyperparameter Tuning + **Pengumpulan Tugas 1 (20%)** | 480' | **Tugas 1 (20%)** |
| **5** | `2.1` | Benchmarking Komparatif vs SOTA (fair comparison) | 480' | Formatif |
| **6** | `2.2` | Analisis Statistik Signifikansi & Visualisasi Matriks Evaluasi | 480' | Formatif |
| **7** | `2.3` | Penulisan Draf Bab 4 (Hasil & Pembahasan Kritis) | 480' | Formatif (Bab 4) |
| **8** | `CPMK-2` | **Monev Tengah Semester — Kemajuan 50% (UTS 25%)** | 150' | **UTS Monev (25%)** |
| **9** | `3.1` | Penulisan Draf Bab 5 (Kesimpulan & Saran) + Sinkronisasi Bab 1–5 | 480' | Formatif |
| **10** | `3.2` | Penyusunan Artikel Ilmiah IMRAD (siap submit) | 480' | Formatif |
| **11** | `3.3` | Pendaftaran HKI Hak Cipta Program Komputer (DJKI) | 480' | Formatif (EC) |
| **12** | `3.4` | Uji Turnitin Final + **Pengumpulan Tugas 2 (25%)** | 480' | **Tugas 2 (25%)** |
| **13** | `4.1` | Verifikasi Administratif & Persetujuan Sidang oleh Pembimbing | 480' | Formatif |
| **14** | `4.2` | Penyusunan Slide Sidang + Skenario Live Demo + Geladi Bersih | 480' | Formatif (dry run) |
| **15** | `4.2` | Sidang Pendadaran Sesi Presentasi & Demo (20') | 20' + 40' QA | Formatif |
| **16** | `CPMK-4` | **Ujian Sidang Pendadaran Sarjana — Tanya Jawab 40' (UAS 30%)** | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (BIMBINGAN + RISET MANDIRI)

### PERTEMUAN 1 — Finalisasi Pengumpulan & Pembersihan Dataset Etis (Sub-CPMK-1.1)
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Alat:** Python/pandas, OpenRefine, Label Studio, util anonimisasi UU PDP.
* **Riset Mandiri (`400'`):** Menuntaskan pengumpulan dataset primer (kuesioner, sensor IoT, wawancara, log mitra) atau sekunder (benchmark publik: Kaggle, UCI, HuggingFace). Lakukan *data cleaning*: tangani missing value, outlier detection, deduplikasi, konsistensi label. Susun *dataset card*: sumber, ukuran, distribusi kelas, keterbatasan, lisensi, dan bukti izin etik/mitra (surat izin, informed consent). Anonimisasi data personal sesuai UU PDP (nik, nama, alamat → hash/pseudonim).
* **Bimbingan-1 (`80'`):** Pembimbing memverifikasi etika data (bukan data curian, bukan scraping ilegal tanpa izin), kepatuhan UU PDP, dan kesiapan dataset → paraf kartu bimbingan-1.
* **Daring LMS:** Unggah dataset card + log preprocessing + surat izin etik/mitra + kartu bimbingan-1.

### PERTEMUAN 2 — Pembangunan Baseline Architecture yang Reproduksibel (Sub-CPMK-1.2)
* **Sub-CPMK:** `Sub-CPMK-1.2` [C6] · **Alat:** Git/GitLab, conda/pip env, Docker (opsional), MLflow.
* **Riset Mandiri (`400'`):** Implementasi baseline — sistem/model pembanding yang sudah ada (mis. YOLOv8 original, BERT baseline, CRUD monolit, atau heuristik sederhana). Struktur repo rapi: `README.md` (cara instalasi & reproduksi), `requirements.txt/environment.yml`, `src/`, `data/`, `experiments/`, `docs/`. Pastikan dapat dilatih/diuji end-to-end dari 0 (`git clone + pip install + python train.py` → hasil).
* **Bimbingan-2 (`80'`):** Review arsitektur: apakah modular, terdokumentasi, dan reproduksibel? Pembimbing cek praktik *reproducible research* (seed fixed, env tercatat).
* **PT/BM:** Lengkapi README + diagram arsitektur (draw.io/Mermaid) + unggah repo snapshot ke LMS.

### PERTEMUAN 3 — Implementasi Algoritma Usulan / Modifikasi Metode Inti (Sub-CPMK-1.3 Bag I)
* **Sub-CPMK:** `Sub-CPMK-1.3` [C6] · **Alat:** VS Code, PyTorch/TensorFlow/Scikit-learn atau stack web/cloud/platform sesuai topik.
* **Riset Mandiri (`400'`):** Realisasikan kebaruan: modifikasi arsitektur model (mis. attention baru), algoritma optimasi, protokol keamanan, fitur IoT, atau platform SaaS. Tulis pseudocode + komentar kode yang menjelaskan *why*, bukan hanya *what*. Lakukan unit test minimal untuk fungsi kritis.
* **Bimbingan-3 (`80'`):** Diskusi kebaruan: apakah klaim novelty kuat vs literatur Bab 2? Apakah feasible? Pembimbing beri arahan scope (jangan over-engineering).
* **Daring LMS:** Logbook harian + pseudocode + link commit Git terbaru.

### PERTEMUAN 4 — Eksperimen Batch-1 & Hyperparameter Tuning + Tugas 1 (Sub-CPMK-1.3 Bag II)
* **Sub-CPMK:** `Sub-CPMK-1.3` [C4] + **Tugas 1 (CPMK-1, 20%)** · **Alat:** MLflow/W&B, Optuna/Grid Search, TensorBoard.
* **Riset Mandiri (`400'`):** Eksekusi Batch-1: latih/evaluasi model/sistem usulan pada split validasi, catat metrik (akurasi, F1, mAP, latensi, TRL checklist untuk J2). Lakukan tuning hyperparameter terstruktur (grid/random/Bayesian) dengan pencatatan lengkap: param, seed, waktu, hardware. JANGAN cherry-pick hasil terbaik saja — catat semua run.
* **Bimbingan-4 (`80'`):** Review log eksperimen Batch-1 (pembimbing cek kejujuran pelaporan), pengarahan penulisan draf awal Bab 4 §Hasil Awal. Verifikasi Tugas 1.
* **Tugas 1 (20%):** Kumpulkan di LMS: (1) Laporan kemajuan 3–5 hal (dataset, baseline, novelty, Batch-1), (2) Repo Git (tag `tugas1`), (3) Log MLflow/W&B (CSV/URL), (4) Draf Bab 4 §1 (opsional).

### PERTEMUAN 5 — Benchmarking Komparatif vs SOTA (Sub-CPMK-2.1)
* **Sub-CPMK:** `Sub-CPMK-2.1` [C5] · **Alat:** Script evaluasi terpadu, leaderboard publik.
* **Riset Mandiri (`400'`):** Implementasi/jalankan 2–3 metode baseline SOTA (dari 3 tahun terakhir) pada *exact same* dataset split, seed, hardware, dan metrik. Contoh: untuk topik deteksi penyakit daun, bandingkan usulan vs YOLOv8 vs EfficientDet vs DETR pada mAP@0.5 yang sama. Catat waktu inferensi & ukuran model.
* **Bimbingan-5 (`80'`):** Validasi fairness: apakah baseline tidak dirugikan (mis. hyperparam baseline tidak dioptimasi sementara usulan dioptimasi berlebihan)? Koreksi bila perlu.
* **Jalur Diferensiasi:**
  - *J2 Industri:* Tambahkan bukti uji di lingkungan mitra (log deploy, screenshot).
  - *J3 Startup:* Tambahkan metrik bisnis (retensi, NPS, konversi).
  - *J4 Publikasi:* Pastikan baseline mencakup metode dari jurnal target.

### PERTEMUAN 6 — Analisis Statistik Signifikansi & Visualisasi (Sub-CPMK-2.2)
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] · **Alat:** SciPy, statsmodels, R, matplotlib/seaborn/Plotly, Tableau.
* **Riset Mandiri (`400'`):** Uji signifikansi perbedaan performa (paired t-test untuk 5-fold CV, Wilcoxon untuk non-parametrik, McNemar untuk klasifikasi). Hitung interval kepercayaan 95%. Buat visualisasi: bar chart perbandingan, kurva ROC/PR, confusion matrix, ablation chart, latency vs accuracy tradeoff.
* **Bimbingan-6 (`80'`):** Review statistik: apakah klaim "lebih baik" didukung p < 0,05? Apakah visual informatif (label jelas, tidak menyesatkan, color-blind friendly)?
* **Daring LMS:** Notebook analisis (Jupyter) + 3–5 grafik final.

### PERTEMUAN 7 — Penulisan Draf Bab 4 (Hasil & Pembahasan Kritis) (Sub-CPMK-2.3)
* **Sub-CPMK:** `Sub-CPMK-2.3` [C5] · **Alat:** Mendeley/Zotero, Grammarly, Overleaf.
* **Bimbingan Intensif (`120'`) + Mandiri (`360'`):** Menulis Bab 4 (15–30 hal): §4.1 Setup eksperimen (dataset, hardware, metrik), §4.2 Hasil utama (tabel + grafik), §4.3 Pembahasan (mengapa unggul/gagal — analisis error case), §4.4 Ablation/limitasi, §4.5 Ancaman validitas (internal/external/construct). Jaga koherensi dengan Bab 2 (landasan teori) & Bab 3 (metode).
* **Bimbingan-7:** Bedah draf Bab 4: apakah argumentasi kausal, bukan sekadar laporan angka?
* **Formasi J2/J3:** Tambahkan §Implementasi di Mitra / Validasi Pasar.

### PERTEMUAN 8 — MONEV TENGAH SEMESTER — Kemajuan 50% (UTS Monev, 25%)
* **CPMK Diuji:** `CPMK-2` (Sub-CPMK-2.1 s.d. 2.3) [C5] · **Bobot:** 25% · **Durasi:** 150 menit.
* **Pelaksanaan:** Presentasi monev 10 menit (slide 8–10 hal: masalah → metode → hasil 50% → kendala → rencana) + tanya jawab 15 menit di hadapan Tim Pembimbing. Koordinator TA/KBK dapat diundang sebagai *second opinion* untuk deteksi dini risiko gagal.
* **Kriteria Lulus Monev:** Minimal 50% riset tercapai (data siap, baseline+usulan berjalan, benchmark & analisis awal ada, draf Bab 4 ≥ 50%). Jika <50%, mahasiswa mendapat surat peringatan + rencana percepatan (remedial timeline 2 minggu).
* **Pasca-Monev:** Berita acara ditandatangani + nilai UTS diinput ke portal OBE.

### PERTEMUAN 9 — Penulisan Draf Bab 5 (Kesimpulan & Saran) (Sub-CPMK-3.1)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C5] · **Alat:** Panduan Skripsi FSTI.
* **Bimbingan (`120'`) + Mandiri (`360'`):** Menulis Bab 5 (5–10 hal): §5.1 Kesimpulan (menjawab tiap rumusan masalah Bab 1 secara eksplisit, maksimal 5 poin temuan utama), §5.2 Implikasi (teoretis & praktis), §5.3 Keterbatasan, §5.4 Saran riset/produk lanjutan (spesifik, bukan "perlu penelitian lebih lanjut" generik). Sinkronisasi Bab 1–5: pastikan istilah, notasi, dan klaim konsisten.
* **Bimbingan-9:** Review Bab 5: apakah setiap rumusan masalah terjawab? Apakah saran orisinal?
* **Daring LMS:** Draf Bab 5 + matriks keterlacakan Rumusan Masalah → Temuan → Bab.

### PERTEMUAN 10 — Penyusunan Artikel Ilmiah IMRAD (Sub-CPMK-3.2)
* **Sub-CPMK:** `Sub-CPMK-3.2` [C6] · **Alat:** Template IEEE/ACM, Mendeley, Turnitin.
* **Bimbingan Penulisan (`120'`) + Mandiri (`360'`):** Alih wahana skripsi 80 hal → artikel 6–10 hal: Title, Abstract (150–250 kata, struktur Background-Method-Result-Conclusion), Keywords, 1 Introduction, 2 Related Work, 3 Method, 4 Experiment & Result, 5 Discussion, 6 Conclusion, References (IEEE style, ≥ 15 sumber, 70% 5 tahun terakhir). Pilih jurnal target: SINTA 1/2 atau Scopus Q1–Q4 (cek SJR) atau prosiding internasional bereputasi.
* **Bimbingan-10:** Bedah artikel: apakah kontribusi jelas (1 kalimat novelty)? Apakah abstrak menjual?
* **Jalur 4:** Artikel ini adalah luaran utama — harus siap submit (bahkan submitted) sebelum sidang.

### PERTEMUAN 11 — Pendaftaran HKI Hak Cipta Program Komputer (Sub-CPMK-3.3)
* **Sub-CPMK:** `Sub-CPMK-3.3` [C3] · **Alat:** e-Hak Cipta DJKI (https://e-hakcipta.dgip.go.id), Sentra HKI UWG.
* **Proses HKI (`400'`) + Bimbingan (`80'`):** Siapkan berkas: (1) Surat pernyataan pencipta, (2) Scan KTP mahasiswa + pembimbing, (3) Manual/petunjuk penggunaan 5–10 hal, (4) Cuplikan source code 10–20 hal (header + fungsi inti), (5) Surat pengalihan hak (bila ada mitra). Isi e-HKI: judul ciptaan, jenis (Program Komputer), tanggal publikasi pertama, uraian ciptaan. Konsultasi Sentra HKI UWG untuk validasi. Target: dapat Nomor Permohonan / EC (Electronic Certificate) sebelum Pekan 12.
* **Bimbingan-11:** Review kelengkapan berkas + penentuan nama pencipta (mahasiswa sebagai pencipta utama, pembimbing sebagai pembimbing — bukan pencipta bila tidak menulis kode bersama).
* **Daring LMS:** Upload bukti permohonan HKI (PDF).

### PERTEMUAN 12 — Uji Turnitin Final + Pengumpulan Tugas 2 (Sub-CPMK-3.4)
* **Sub-CPMK:** `Sub-CPMK-3.4` [A3] + **Tugas 2 (CPMK-3, 25%)** · **Alat:** Turnitin kampus, paraphrasing tool etis.
* **Uji Plagiasi (`400'`) + Bimbingan (`80'`):** Submit naskah lengkap Bab 1–5 (tanpa lampiran kode) ke Turnitin via operator prodi. Target: Similarity <20% (exclude bibliography & quotes). AI-writing detection <15% bila tersedia. Jika >20%, lakukan parafrasa etis: kutip langsung diberi tanda kutip + sitasi, perbaiki sitasi, bukan sekadar ganti sinonim acak (hindari *patchwriting*). Maksimal 2x uji ulang dalam 1 minggu.
* **Tugas 2 (25%):** Kumpulkan di LMS: (1) Naskah lengkap Bab 1–5 (PDF, 80–120 hal), (2) Naskah artikel IMRAD (PDF), (3) Bukti pendaftaran HKI (PDF EC/permohonan), (4) Lembar hasil Turnitin (<20%), (5) Repo Git final (tag `tugas2`).
* **Penilaian:** Rubrik Tugas 2 (K-4) — lihat RPS Lampiran 3.

### PERTEMUAN 13 — Verifikasi Administratif & Persetujuan Sidang (Sub-CPMK-4.1)
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5] · **Alat:** Formulir pendaftaran sidang, kartu bimbingan, ceklis yudisium.
* **Konsultasi Persetujuan (`480'`):** Finalisasi revisi minor pasca-Tugas 2, lengkapi ceklis: (1) Lembar persetujuan pembimbing (2 tanda tangan), (2) Kartu bimbingan minimal 8x pertemuan (termasuk monev), (3) Bukti HKI, (4) Lembar Turnitin <20%, (5) Transkrip sementara ≥ 120 SKS, (6) Bebas pustaka & keuangan, (7) Artikel (minimal draf siap submit, untuk J4: bukti accepted). Daftar sidang ke Panitia TA (sekretariat prodi) — dapat jadwal sidang (H-7).
* **Bimbingan-13:** Pembimbing tanda tangan lembar persetujuan bila naskah layak sidang. Jika belum layak, beri daftar perbaikan 1 minggu (remedial).
* **Daring LMS:** Upload berkas pendaftaran sidang (PDF terpadu).

### PERTEMUAN 14 — Penyusunan Slide Sidang + Live Demo + Geladi Bersih (Sub-CPMK-4.2 Bag I)
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Alat:** PowerPoint/Beamer, OBS Studio (rekam demo cadangan).
* **Geladi Bersih (`400'`) + Bimbingan (`80'`):** Susun slide 15–20 halaman: Cover (judul, nama, pembimbing), 1 Problem & Research Gap (1 slide), 2 Tujuan & Kontribusi (1 slide), 3 Tinjauan Pustaka ringkas (1–2 slide), 4 Metode/Arsitektur (2–3 slide + diagram), 5 Hasil Utama (3–4 slide: tabel, grafik, screenshot), 6 Demo Langsung (1 slide + live app), 7 Kesimpulan & Saran (1 slide). Aturan slide: maksimal 6 baris/slide, 6 kata/baris, visual > teks. Siapkan demo: skenario *happy path* + 1 kasus tepi (edge case). Rekam video demo cadangan (2 menit) antisipasi gagal jaringan. Latihan presentasi 20 menit + simulasi tanya jawab 15 menit.
* **Bimbingan-14:** Dry run di hadapan pembimbing: feedback tempo, artikulasi, kontak mata, transisi slide, kelancaran demo.
* **Daring LMS:** Slide final (PPTX+PDF) + video demo cadangan (MP4, opsional).

### PERTEMUAN 15 — Sidang Pendadaran Sesi Presentasi & Demo (20') (CPMK-4 Bag I)
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Alat:** Ruang sidang, proyektor, laptop, aplikasi siap demo.
* **Sidang Sesi-1 (`20'`):** Mahasiswa presentasikan temuan riset & demo langsung di hadapan Dewan Penguji (3 dosen: 1 Pembimbing Utama + 2 Penguji Independen, salah satu dapat dari industri/mitra untuk J2/J3). Manajemen waktu ketat: 20 menit (bel di 15' & 19'). Demo harus *live* (bukan hanya screenshot) — penguji dapat minta input acak.
* **Penilaian Sesi-1 (50% UAS):** Kriteria presentasi & demo (kejelasan, manajemen waktu, kelancaran demo) — lihat Rubrik UAS.
* **Jalur Diferensiasi:** J2 tunjukkan surat mitra + TRL checklist; J3 tunjukkan dashboard traksi; J4 tunjukkan bukti accepted jurnal.

### PERTEMUAN 16 — UJIAN SIDANG PENDADARAN SARJANA — Tanya Jawab 40' (UAS 30%)
* **CPMK Diuji:** `CPMK-4` (Sub-CPMK-4.1 & 4.2) [C5] · **Bobot:** 30% · **Durasi:** 150 menit total (20' presentasi + 40' QA + 30' deliberasi + 60' administrasi yudisium).
* **Pelaksanaan:** Tanya jawab komprehensif 40 menit: penguji gali kedalaman metodologi, kebaruan, alternatif desain, limitasi, etika, dan wawasan ke depan. Pembimbing tidak boleh menjawab untuk mahasiswa. Mahasiswa wajib mempertahankan argumen secara ilmiah (boleh mengakui keterbatasan dengan jujur). Setelah QA, dewan berdeliberasi (mahasiswa keluar ruangan 10'), lalu pengumuman hasil (Lulus / Lulus dengan Revisi / Mengulang Sidang) + berita acara.
* **Administrasi Pasca-Sidang:** Nilai 14 CPL diinput ke portal OBE, berita acara yudisium ditandatangani, revisi pasca-sidang (maks. 2 minggu) disetorkan sebelum yudisium fakultas.
