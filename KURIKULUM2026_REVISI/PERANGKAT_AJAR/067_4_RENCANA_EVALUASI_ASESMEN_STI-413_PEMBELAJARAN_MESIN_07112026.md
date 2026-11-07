# 067_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-413 — PEMBELAJARAN MESIN (*Machine Learning*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI413` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 4  
**Klaster Asesmen MK (Dok 018):** Klaster 3 (`K-3`) — Kecerdasan Artifisial, Cloud & Cybersecurity  
**CPL Dibebankan:** `CPL-06` (`P2` = **45%**) & `CPL-09` (`KK1` = **55%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 008, 018,** dan **043**, mata kuliah `STI-413 Pembelajaran Mesin` (3 SKS `+P`) menerapkan skema bobot baku Klaster `K-3` (`20% / 25% / 25% / 30%`) dengan pemetaan 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-06` / `P2`)** — *Case-Based Anti-Leakage Scikit-Learn Preprocessing Pipeline*.
* **UTS (Pekan 8 — 25%) → `CPMK-2` (`CPL-09` / `KK1`)** — *Live Lab Exam: Supervised Tabular Model Construction & Hyperparameter Tuning*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-06` / `P2`)** — *Case-Based Unsupervised Clustering (K-Means, Hierarchical) & PCA with Silhouette Validation*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-09` / `KK1`)** — *Project-Based Model Performance Evaluation (Confusion Matrix, F1, ROC-AUC) & Integrated Inference Prototype + Blind Test Defense*.
* **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-3` Dok 018):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75%` berbasis studi kasus sains data nyata dan proyek purwarupa inferensi terintegrasi *(selaras penuh dengan target IKU 7 Dokumen 004 untuk `STI-413`)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-06`**<br>(`P2` — 45%)<br>*Level: R* | **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus dataset kotor: EDA, *imputation, encoding,* & *scaling* tepat sesuai distribusi | **RTM-1 (Tugas 1)** + Verifikasi Kode Lab + Rubrik T1 | Sumatif | 10% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Studi kasus dataset kotor: Penyusunan `ColumnTransformer` + `Pipeline` **bebas *data leakage*** | **RTM-1 (Tugas 1)** + Audit Anti-Leakage + Rubrik T1 | Sumatif | 10% | |
| **`CPL-09`**<br>(`KK1` — 55%)<br>*Level: R* | **`CPMK-2`**<br>(C5) | `Sub-CPMK-2.1` | Mg 8 | Ujian praktik pemodelan lab 150': Konstruksi, komparasi, & *tuning* parameter model *Supervised* (*Linear/Logistic, Tree, RF, SVM*) | **Dataset & Soal Praktik UTS** + Rubrik Analitik UTS | Sumatif | 25% | **25%** |
| **`CPL-06`**<br>(`P2` — 45%)<br>*Level: R* | **`CPMK-3`**<br>(C5) | `Sub-CPMK-2.2` | Mg 12 | Studi kasus analitik organisasi: Konstruksi model *Unsupervised* (**K-Means, Hierarchical, PCA**) & validasi **Silhouette Score** | **RTM-2 (Tugas 2)** + Demo Analisis Lab + Rubrik T2 | Sumatif | 25% | **25%** |
| **`CPL-09`**<br>(`KK1` — 55%)<br>*Level: R* | **`CPMK-4`**<br>(C5, C6) | `Sub-CPMK-3.1` | Mg 16 | Proyek akhir + sidang: Evaluasi performa mendalam (**Confusion Matrix, F1-Score, ROC-AUC**, *Stratified CV*, *Feature Importance*) | **Laporan Eksperimen & Notebook UAS** + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-3.2` | Mg 16 | Proyek akhir + uji *blind test*: Pembangunan **Purwarupa Inferensi Terintegrasi** (`joblib` + `Streamlit`) dengan data baru | **Aplikasi Purwarupa Inferensi** & Sidang Individu UAS | Sumatif | 15% | |
| **TOTAL** | **4 CPMK** | **6 Sub-CPMK (`043`)** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN PRAKTIK

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Pipeline Rekayasa Data ML Bebas *Data Leakage*)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Verifikasi Lab **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-06`).
* **Spesifikasi Pengerjaan Individu:**
  1. Diberikan dataset tabular berantakan ($\pm 5.000$ baris, 18 kolom campuran numerik miring, kategorikal berkardinalitas rendah/tinggi, nilai hilang 8–20%, serta 2 kolom jebakan *target leakage*).
  2. Mahasiswa wajib mendokumentasikan EDA, mengidentifikasi dan menghapus kolom *target leakage* beserta alasannya, melakukan `train_test_split` terstratifikasi sebelum transformasi apa pun, serta merakit objek `ColumnTransformer` + `Pipeline` `scikit-learn` yang lolos uji `cross_val_score` tanpa galat dan tanpa *leakage*.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Pemodelan & Optimasi *Supervised Learning*)
* **Format & Bobot:** Ujian Praktik Pemodelan Terawasi di Laboratorium (**150 menit**, individu) · Bobot **25%** (`CPMK-2` → `CPL-09`).
* **Spesifikasi Soal Praktik:**
  1. Diberikan dataset tabular baru di laboratorium; mahasiswa wajib membangun `Pipeline` pra-pemrosesan dan melatih minimal 4 algoritma **Supervised Learning** (*Linear/Logistic Regression, Decision Tree, Random Forest,* dan *SVM*).
  2. Melakukan optimasi hiperparameter menggunakan `GridSearchCV` atau `RandomizedSearchCV` pada minimal 2 model teratas, membandingkan skor validasi vs uji untuk membuktikan tidak terjadinya *overfitting*, dan menyimpulkan model terpilih.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Segmentasi Tak-Terbimbing & Reduksi Dimensi PCA)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Demo Lab **Pekan 12** · Bobot **25%** (`CPMK-3` → `CPL-06`).
* **Spesifikasi Teknis:**
  1. Menggunakan dataset operasional/pelanggan multi-dimensi ($\ge 12$ fitur numerik tanpa label), mahasiswa melakukan standarisasi fitur, reduksi dimensi **PCA** (menganalisis kurva *Cumulative Explained Variance* & bobot komponen), serta membandingkan klasterisasi **K-Means** dan **Agglomerative Hierarchical Clustering** (*Dendrogram*).
  2. Wajib membuktikan pemilihan jumlah klaster optimal menggunakan **Silhouette Score & Silhouette Plot**, memvisualisasikan sebaran klaster pada ruang 2D PCA, serta merumuskan profil dan rekomendasi kebijakan untuk setiap klaster.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Evaluasi Model & Purwarupa Inferensi Terintegrasi)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-09`), memadukan **Bundel Proyek Tim (50% nilai UAS)** + **Sidang Uji *Blind Holdout Set* & Tanya-Jawab Individu (50% nilai UAS, 150 menit)**:
  1. **Evaluasi Performa Mendalam (`Sub-CPMK-3.1`):** Membandingkan minimal 4 model kandidat dengan *Stratified 5-Fold CV*, melaporkan **Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC** (dan penalaan *threshold* pada data timpang), serta menyajikan interpretasi faktor terpenting (*Permutation Importance*).
  2. **Purwarupa Inferensi Terintegrasi (`Sub-CPMK-3.2`):** Menyimpan `Pipeline` utuh ke `.joblib` dan membangun aplikasi inferensi interaktif (`Streamlit`) yang mendukung prediksi satuan maupun unggah CSV *batch*. Saat sidang, penguji mengunggah berkas CSV *unseen holdout* ke aplikasi tim untuk menilai stabilitas eksekusi dan akurasi generalisasi nyata.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-413}}$)
$$NA_{\text{STI-413}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
1. **Ketercapaian `CPL-06` (`P2` — bobot 45% MK dari `CPMK-1` [20%] + `CPMK-3` [25%]):**
   $$\text{Score}_{\text{CPL-06, STI-413}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,25\,S_{\text{Tugas 2}}(i)}{0,45}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,45 = 1,35\text{ SKS}$).*
2. **Ketercapaian `CPL-09` (`KK1` — bobot 55% MK dari `CPMK-2` [25%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-09, STI-413}}(i) = \frac{0,25\,S_{\text{UTS}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,55}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,55 = 1,65\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Penalti *Data Leakage*
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**.
* **Aturan Ketat Metodologi Sains Data:** Eksperimen yang terbukti mengalami *data leakage* (mis. menge-*fit* scaler pada seluruh dataset sebelum *split* atau menyertakan kolom target terselubung) dikenakan plafon nilai maksimal **60,0** pada kriteria metodologi hingga diperbaiki pada sesi remedial (maksimal 1 kali remedial dengan plafon nilai **70,0 / B**).
