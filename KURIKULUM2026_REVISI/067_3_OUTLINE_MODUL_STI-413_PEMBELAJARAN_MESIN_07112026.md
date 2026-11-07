# 067_3 — OUTLINE BUKU MODUL PEMBELAJARAN & PRAKTIKUM BERBASIS OBE
## STI-413 — PEMBELAJARAN MESIN (*Machine Learning*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI413` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 4  
**CPL:** `CPL-06` (`P2` = 45%) & `CPL-09` (`KK1` = 55%) [Level `R`] · **BoK:** `BK-IS18`, `BK-IT02`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR + PRAKTIKUM

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Pembelajaran Mesin Tabular dengan Python & Scikit-Learn: Pipeline Bebas Leakage, Pemodelan Supervised & Unsupervised, Evaluasi ROC-AUC, hingga Purwarupa Inferensi* |
| **Target Tebal Naskah** | 14 Bab Materi + 14 Modul Praktikum Notebook + 2 Unit Evaluasi ($\pm 220\text{–}255\text{ halaman}$ A4 dilengkapi intuisi matematis ringkas, arsitektur `ColumnTransformer`, kurva evaluasi, dan kode purwarupa `Streamlit`) |
| **Pagar Pembatas Buku (*Guardrail*)** | Fokus tuntas pada *Classical/Tabular Machine Learning* menggunakan `Scikit-Learn`; tidak membahas *Deep Learning* `PyTorch/TensorFlow` (`STI-624`), NLP teks (`STI-414`), maupun orkestrasi MLOps klaster produksi (`STA-701`). |

---

## 2. PETA KESELARASAN 14 BAB & 14 MODUL PRAKTIKUM TERHADAP CPMK & SUB-CPMK

| Bagian | Bab & Lab | Judul Bab Materi & Modul Praktikum | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Rekayasa Data & Pipeline Bebas Leakage** | **Bab 1 / Lab 1** | Paradigma *Machine Learning*, Siklus CRISP-DM, & *Bias–Variance Trade-Off* | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2 / Lab 2** | *Exploratory Data Analysis* (EDA), *Imputation*, *Encoding*, & *Feature Scaling* | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3 / Lab 3** | Anatomi **Data Leakage** & Arsitektur `ColumnTransformer` + `Pipeline` di `scikit-learn` | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Pembelajaran Terbimbing (Supervised Learning)** | **Bab 4 / Lab 4** | Rekayasa Fitur Tabular & Pemodelan **Linear Regression** (*OLS & Gradient Descent*) | Mg 4 | `CPMK-2` | `Sub-CPMK-1.2, 2.1` | UTS (25%) |
| | **Bab 5 / Lab 5** | Regularisasi Linier (*Ridge, Lasso, ElasticNet*) & Klasifikasi **Logistic Regression** | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 6 / Lab 6** | Pohon Keputusan (**Decision Tree**) & *Ensemble Learning* (**Random Forest & Boosting**) | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 7 / Lab 7** | **Support Vector Machine (SVM)** & Optimasi Parameter (`GridSearchCV / RandomizedSearchCV`) | Mg 7 | `CPMK-2` | `Sub-CPMK-2.1` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Simulasi Ujian Praktik Pemodelan & Hyperparameter Tuning Supervised ML (UTS)* | *Mg 8* | *`CPMK-2`* | *`Sub-CPMK-2.1`* | *UTS (25%)* |
| **Bagian III:<br>Pembelajaran Tak-Terbimbing (Unsupervised)** | **Bab 8 / Lab 8** | Klasterisasi Partisi **K-Means / K-Means++**, *Elbow Method*, & Segmentasi Bisnis | Mg 9 | `CPMK-3` | `Sub-CPMK-2.2` | Tugas 2 (25%) |
| | **Bab 9 / Lab 9** | **Agglomerative Hierarchical Clustering**, *Dendrogram*, & Validasi **Silhouette Score** | Mg 10 | `CPMK-3` | `Sub-CPMK-2.2` | Tugas 2 (25%) |
| | **Bab 10 / Lab 10** | Reduksi Dimensi **Principal Component Analysis (PCA)** & Visualisasi Ruang Laten | Mg 11 | `CPMK-3` | `Sub-CPMK-2.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Evaluasi Model & Purwarupa Inferensi** | **Bab 11 / Lab 11** | Evaluasi Ketat Klasifikasi: **Confusion Matrix, F1-Score, PR-Curve,** & **ROC-AUC** | Mg 12 | `CPMK-4` | `Sub-CPMK-3.1` | UAS (30%) |
| | **Bab 12 / Lab 12** | *Stratified Cross-Validation*, *Error Slicing*, & Interpretabilitas Model (*Explainable ML*) | Mg 13 | `CPMK-4` | `Sub-CPMK-3.1` | UAS (30%) |
| | **Bab 13 / Lab 13** | Serialisasi Artefak `Pipeline` (`joblib`), Validasi Skema Data Baru, & Modul Inferensi | Mg 14 | `CPMK-4` | `Sub-CPMK-3.2` | UAS (30%) |
| | **Bab 14 / Lab 14** | Pembangunan **Purwarupa Inferensi Terintegrasi** (`Streamlit`) & *Handoff* ke `STI-624`/`STA-701` | Mg 15 | `CPMK-4` | `Sub-CPMK-3.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Akhir ML & Protokol Pengujian Unseen Holdout Data (UAS)* | *Mg 16* | *`CPMK-4`* | *`3.1–3.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB & MODUL PRAKTIKUM

#### BAB 1 & LAB 1: Paradigma *Machine Learning*, Siklus CRISP-DM, & *Bias–Variance Trade-Off* (Pekan 1)
* **Materi & Praktikum:** Perumusan tugas prediktif/deskriptif, kapasitas model, dekomposisi galat generalisasi (*Bias + Variance + Irreducible Noise*), serta penyiapan alur eksperimen reproduksibel di Python.

#### BAB 2 & LAB 2: *Exploratory Data Analysis* (EDA), *Imputation*, *Encoding*, & *Feature Scaling* (Pekan 2)
* **Materi & Praktikum:** Analisis univariat/bivariat, pola *MCAR/MAR/MNAR*, `SimpleImputer` & `KNNImputer`, `OneHotEncoder` vs `OrdinalEncoder`, serta perbandingan `StandardScaler`, `MinMaxScaler`, dan `RobustScaler`.

#### BAB 3 & LAB 3: Anatomi Data Leakage & Arsitektur `ColumnTransformer` + `Pipeline` (Pekan 3)
* **Materi & Praktikum:** Studi kasus kegagalan industri akibat *preprocessing leakage* dan *target leakage*, perancangan `ColumnTransformer` heterogen, pembungkusan `Pipeline`, dan *Stratified Split*.

#### BAB 4 & LAB 4: Rekayasa Fitur Tabular & Pemodelan Linear Regression (Pekan 4)
* **Materi & Praktikum:** Penciptaan fitur rasio/interaksi/polinomial, persamaan normal vs *Gradient Descent*, asumsi residual, dan evaluasi regresi (`MAE, RMSE, MAPE, R²`).

#### BAB 5 & LAB 5: Regularisasi Linier (*Ridge, Lasso, ElasticNet*) & Klasifikasi Logistic Regression (Pekan 5)
* **Materi & Praktikum:** Geometri penalti $L_2$ dan $L_1$, fungsi sigmoid & *Cross-Entropy Loss*, batas keputusan linier, serta klasifikasi multikelas.

#### BAB 6 & LAB 6: Pohon Keputusan (Decision Tree) & *Ensemble Learning* (Random Forest & Boosting) (Pekan 6)
* **Materi & Praktikum:** Pembelahan rekursif *Gini / Entropy*, pengendalian *overfitting* pohon, mekanisme *Bagging + Out-of-Bag Score* pada **Random Forest**, serta *Gradient Boosted Decision Trees*.

#### BAB 7 & LAB 7: Support Vector Machine (SVM) & Optimasi Parameter (`GridSearchCV`) (Pekan 7)
* **Materi & Praktikum:** *Maximum Margin Classifier*, parameter regularisasi $C$, transformasi **RBF Kernel** ($\gamma$), serta pencarian parameter bersarang pada `Pipeline` dengan `GridSearchCV` dan `RandomizedSearchCV`.

#### BAB 8 & LAB 8: Klasterisasi Partisi K-Means / K-Means++, *Elbow Method*, & Segmentasi Bisnis (Pekan 9)
* **Materi & Praktikum:** Minimisasi inersia dalam-klaster, algoritma **K-Means++**, penskalaan fitur wajib pra-klaster, dan penerjemahan *centroid* menjadi persona segmen bisnis.

#### BAB 9 & LAB 9: Agglomerative Hierarchical Clustering, *Dendrogram*, & Validasi Silhouette Score (Pekan 10)
* **Materi & Praktikum:** Matriks ketidaksamaan, perbandingan *Ward / Complete / Average Linkage*, pemotongan *Dendrogram*, pengenalan *DBSCAN*, serta perhitungan dan visualisasi **Silhouette Score**.

#### BAB 10 & LAB 10: Reduksi Dimensi Principal Component Analysis (PCA) & Visualisasi Ruang Laten (Pekan 11)
* **Materi & Praktikum:** Dekomposisi nilai singular/eigen untuk mencari arah varians maksimum, pemilihan komponen via *Cumulative Explained Variance*, interpretasi *loadings*, dan proyeksi klaster 2D/3D.

#### BAB 11 & LAB 11: Evaluasi Ketat Klasifikasi: Confusion Matrix, F1-Score, PR-Curve, & ROC-AUC (Pekan 12)
* **Materi & Praktikum:** Evaluasi pada ketidakseimbangan kelas ekstrem, penalaan *decision threshold* berbasis matriks biaya bisnis, perbandingan kurva **ROC-AUC** dan **Precision–Recall**, serta `class_weight`.

#### BAB 12 & LAB 12: *Stratified Cross-Validation*, *Error Slicing*, & Interpretabilitas Model (Pekan 13)
* **Materi & Praktikum:** Pelaporan rata-rata dan simpangan baku *K-Fold CV*, kurva kalibrasi probabilitas, analisis kelompok gagal prediksi, serta *Permutation Feature Importance*.

#### BAB 13 & LAB 13: Serialisasi Artefak `Pipeline` (`joblib`), Validasi Skema Data Baru, & Modul Inferensi (Pekan 14)
* **Materi & Praktikum:** Pengemasan utuh `preprocessor + model` menjadi satu berkas `.joblib`, pembekuan dependensi, dan validasi defensif terhadap input data baru yang tak lengkap/ekstrem.

#### BAB 14 & LAB 14: Pembangunan Purwarupa Inferensi Terintegrasi (`Streamlit`) & *Handoff* (Pekan 15)
* **Materi & Praktikum:** Rekayasa antarmuka inferensi tunggal dan *batch CSV* interaktif lengkap tampilan probabilitas dan kontribusi fitur, serta peta *handoff* menuju `STI-520`, `STI-624`, `STI-726`, dan `STA-701`.
