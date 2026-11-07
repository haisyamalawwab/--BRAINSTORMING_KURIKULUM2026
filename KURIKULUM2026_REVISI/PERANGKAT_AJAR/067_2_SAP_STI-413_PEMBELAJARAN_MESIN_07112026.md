# 067_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-413 — PEMBELAJARAN MESIN (*Machine Learning*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI413` · **Bobot:** 3 SKS `+P` (`TM 100'`, `Prak 170'`, `PT 120'`, `BM 120'`) · **Semester:** 4  
**Prasyarat:** `STI-205` Aljabar Linear dan Matriks, `STI-307` Sistem Cerdas · **CPL:** `CPL-06` (`P2` = 45%) & `CPL-09` (`KK1` = 55%) [Level `R`]  
**Klaster Rubrik:** `K-3` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu & Asisten Laboratorium `STI-413` |
|---|---|
| **Struktur Waktu per Sesi** | **Sesi Teori (`100'`):** Pendahuluan `15'` · Inti Intuisi Matematis & Algoritma `70'` · Penutup `15'`<br>**Sesi Praktikum Lab (`170'`):** *Briefing* Dataset `15'` · Eksperimen `Scikit-Learn` Terbimbing `135'` · Verifikasi Metrik & *Git Commit* `20'`, diikuti `PT 120'` & `BM 120'`. |
| **Fokus Keilmuan (*In-Scope*)** | Pemodelan **data tabular terstruktur** secara utuh: EDA, `scikit-learn` `Pipeline` bebas *data leakage*, *Supervised* (*Linear/Logistic, Decision Tree, Random Forest, Boosting, SVM*), *Unsupervised* (*K-Means, Hierarchical, PCA + Silhouette*), evaluasi (*Confusion Matrix, F1, ROC-AUC*), dan purwarupa inferensi interaktif. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** melompat ke jaringan saraf mendalam `PyTorch`/`TensorFlow`, CNN, atau RNN (ranah **`STI-624 Pembelajaran Mendalam & Jaringan Saraf`**), dilarang membahas TF-IDF/BM25 teks (ko-semester **`STI-414`**), dan dilarang melebar ke klaster MLOps produksi penuh (**`STA-701`**). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Teori (`100'`) & Modul Praktikum (`170'`) | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Teori: Taksonomi ML & *Bias–Variance* · Lab 1: Ekosistem Python Ilmiah & Eksplorasi Tabular | 270' | Formatif Lab |
| **2** | `Sub-CPMK-1.1` | Teori: *EDA, Imputation, Encoding, & Scaling* · Lab 2: Transformasi Fitur `scikit-learn` | 270' | Formatif Lab |
| **3** | `Sub-CPMK-1.2` | Teori: Anatomi **Data Leakage** & `Pipeline` · Lab 3: `ColumnTransformer` + `Pipeline` Aman | 270' | Formatif Lab |
| **4** | `Sub-CPMK-1.2, 2.1` | Teori: Rekayasa Fitur & **Linear Regression** · Lab 4: Regresi & Verifikasi **Tugas 1** | 270' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Teori: Regularisasi *Ridge/Lasso* & **Logistic Regression** · Lab 5: Klasifikasi Linier | 270' | Formatif Lab |
| **6** | `Sub-CPMK-2.1` | Teori: **Decision Tree** & *Ensemble* (**Random Forest**) · Lab 6: Pohon vs Hutan Acak | 270' | Formatif Lab |
| **7** | `Sub-CPMK-2.1` | Teori: **SVM** (*Kernel Trick*) & `GridSearchCV` · Lab 7: Optimasi Parameter & Klinik UTS | 270' | Formatif Lab |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** *Live Modeling* & Optimasi *Supervised ML* di Lab | 150' | **UTS (25%)** |
| **9** | `Sub-CPMK-2.2` | Teori: Klasterisasi **K-Means** & *Elbow Method* · Lab 8: Segmentasi Pelanggan RFM | 270' | Formatif Lab |
| **10** | `Sub-CPMK-2.2` | Teori: **Hierarchical Clustering** & **Silhouette Score** · Lab 9: *Dendrogram* & Validasi | 270' | Formatif Lab |
| **11** | `Sub-CPMK-2.2` | Teori: Reduksi Dimensi **PCA** (*Eigen/Variance*) · Lab 10: Kompresi & Visualisasi PCA | 270' | Formatif Lab |
| **12** | `Sub-CPMK-3.1` | Teori: **Confusion Matrix, F1-Score, & ROC-AUC** · Lab 11: Data Timpang & Uji **Tugas 2** | 270' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-3.1` | Teori: *Cross-Validation*, *Error Analysis*, & *Explainability* · Lab 12: *Feature Importance* | 270' | Formatif Lab |
| **14** | `Sub-CPMK-3.2` | Teori: Serialisasi `Pipeline` (`joblib`) & Validasi Input · Lab 13: Modul Inferensi Andal | 270' | Formatif Lab |
| **15** | `Sub-CPMK-3.2` | Teori: Desain Aplikasi Inferensi Interaktif · Lab 14: Purwarupa `Streamlit` & Klinik UAS | 270' | Formatif Lab |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Purwarupa Inferensi & Uji *Unseen Holdout Data* | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (TEORI + PRAKTIKUM)

### PERTEMUAN 1 — Taksonomi *Machine Learning*, Siklus CRISP-DM, & *Bias–Variance Trade-Off*
* **Sub-CPMK:** `Sub-CPMK-1.1` [C2→C3] · **Alat:** Python 3.11+, JupyterLab/VS Code, `numpy, pandas, scikit-learn`.
* **Sesi Teori (`100'`):** Menyambungkan materi pencarian heuristik & aturan eksplisit dari `STI-307 Sistem Cerdas` menuju pembelajaran induktif dari data: perumusan matematis $y \approx f(\mathbf{x})$, perbedaan *Supervised, Unsupervised,* dan *Reinforcement Learning*, serta intuisi fundamental *Underfitting (High Bias)* vs *Overfitting (High Variance)*.
* **Sesi Praktikum Lab 1 (`170'`):** Menyiapkan lingkungan virtual Python, memuat dataset tabular pertama ke `pandas.DataFrame`, dan menjalankan alur dasar `train_test_split` dengan `random_state` reproduksibel.
* **PT (`120'`) & BM (`120'`):** Merumuskan 3 masalah bisnis nyata ke dalam spesifikasi fitur $\mathbf{X}$, target $y$, dan metrik keberhasilan.

### PERTEMUAN 2 — *Exploratory Data Analysis* (EDA), *Imputation*, *Encoding*, & *Feature Scaling*
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Alat:** `pandas, seaborn, sklearn.impute, sklearn.preprocessing`.
* **Sesi Teori (`100'`):** Membahas diagnosis distribusi, kemencengan (*skewness*), korelasi, serta aturan memilih teknik pra-pemrosesan yang tepat: kapan memakai `median` vs `mean` pada `SimpleImputer`, kapan memakai `OrdinalEncoder` vs `OneHotEncoder(handle_unknown='ignore')`, serta mengapa algoritma berbasis jarak/gradien (SVM, K-Means, Regresi Regularisasi, PCA) wajib memakai `StandardScaler`/`RobustScaler` sementara pohon keputusan tidak peka skala.
* **Sesi Praktikum Lab 2 (`170'`):** Melaksanakan EDA visual dan mempraktikkan seluruh transformer `sklearn.preprocessing` pada dataset kredit/properti yang mengandung nilai hilang dan pencilan.
* **PT (`120'`) & BM (`120'`):** Mengerjakan latihan komparasi distribusi sebelum vs sesudah `StandardScaler` dan `RobustScaler`.

### PERTEMUAN 3 — Pencegahan **Data Leakage** & Arsitektur `ColumnTransformer` + `Pipeline`
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] · **Alat:** `sklearn.compose.ColumnTransformer`, `sklearn.pipeline.Pipeline`.
* **Sesi Teori (`100'`):** Membongkar dosa paling fatal praktisi ML pemula — **Data Leakage** (menjalankan `scaler.fit_transform(X)` pada seluruh data sebelum `train_test_split`, atau memasukkan fitur yang nilainya baru muncul setelah kejadian target terjadi, sehingga akurasi di *notebook* tampak 99% tetapi hancur total di dunia nyata!). Mengajarkan perancangan objek `ColumnTransformer` dan `Pipeline` terpadu. Merilis resmi **Tugas 1 (RTM-1)**.
* **Sesi Praktikum Lab 3 (`170'`):** Mendebug sebuah *notebook* yang bocor dan merakit ulang `Pipeline` bersih yang menangani kolom numerik dan kategorikal secara terpisah dan aman di dalam setiap lipatan validasi silang.
* **PT (`120'`) & BM (`120'`):** Menyelesaikan proyek `Pipeline` bebas *data leakage* untuk **Tugas 1**.

### PERTEMUAN 4 — Rekayasa Fitur, **Linear Regression**, & Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` & `2.1` [C3→C5] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alat:** `LinearRegression`, `PolynomialFeatures`.
* **Sesi Teori (`100'`):** Mengaitkan perkalian matriks & persamaan normal $\hat{\boldsymbol{\theta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ dari `STI-205` dengan optimasi *Gradient Descent* pada **Linear Regression**, penciptaan fitur interaksi/polinomial, serta pembacaan kritis metrik regresi (**MAE, RMSE,** dan **$R^2$**).
* **Sesi Praktikum Lab 4 (`170'`):** Verifikasi kode langsung 20 menit atas pengumpulan **Tugas 1 (`CPMK-1`)**, dilanjutkan praktikum pelatihan model regresi harga/permintaan dan analisis plot residual.
* **PT (`120'`) & BM (`120'`):** Mengevaluasi dampak penambahan fitur interaksi terhadap RMSE validasi.

### PERTEMUAN 5 — Regularisasi (*Ridge $L_2$, Lasso $L_1$*) & Klasifikasi **Logistic Regression**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C5] · **Alat:** `Ridge, Lasso, ElasticNet, LogisticRegression`.
* **Sesi Teori (`100'`):** Menunjukkan bagaimana penalti $L_2$ (**Ridge**) menyusutkan bobot fitur multikolinear dan penalti $L_1$ (**Lasso**) melakukan seleksi fitur otomatis menjadi nol, kemudian membedah fungsi logistik sigmoid $\sigma(z) = \frac{1}{1+e^{-z}}$, fungsi kerugian *Binary Cross-Entropy (Log-Loss)*, dan perluasan *Multinomial Softmax* pada **Logistic Regression**.
* **Sesi Praktikum Lab 5 (`170'`):** Melatih model regresi ter-regularisasi dan membangun pengklasifikasi *churn* pelanggan menggunakan *Logistic Regression* di dalam `Pipeline`.
* **PT (`120'`) & BM (`120'`):** Menafsirkan bobot koefisien fitur paling berpengaruh pada model *Logistic Regression*.

### PERTEMUAN 6 — **Decision Tree**, *Bagging* (**Random Forest**), & Pengenalan *Gradient Boosting*
* **Sub-CPMK:** `Sub-CPMK-2.1` [C5] · **Alat:** `DecisionTreeClassifier/Regressor`, `RandomForestClassifier`, `HistGradientBoostingClassifier`.
* **Sesi Teori (`100'`):** Membedah algoritma CART (**Gini Impurity** vs **Entropy**), mengapa pohon tanpa batas kedalaman pasti menghafal derau (*high variance*), serta bagaimana **Random Forest** (*Bootstrap Aggregating + Random Feature Subspace*) dan **Gradient Boosting** menggabungkan pembelajar lemah menjadi model terkuat di industri untuk data tabular.
* **Sesi Praktikum Lab 6 (`170'`):** Memvisualisasikan batas keputusan pohon tunggal vs *Random Forest* dan membandingkan akurasi generalisasi keduanya pada dataset tabular menengah.
* **PT (`120'`) & BM (`120'`):** Mengeksplorasi pengaruh `n_estimators`, `max_depth`, dan `min_samples_leaf`.

### PERTEMUAN 7 — **Support Vector Machine (SVM)**, *Hyperparameter Tuning* (`GridSearchCV`), & Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-2.1` [C5] · **Alat:** `SVC, SVR, GridSearchCV, RandomizedSearchCV`.
* **Sesi Teori (`100'`):** Menguraikan intuisi geometri *Maximum Margin Hyperplane*, variabel longgar (*Soft Margin $C$*), serta kekuatan **Kernel Trick** (*Linear, Polynomial, Radial Basis Function $\gamma$*) memisahkan data non-linier, dilanjutkan prosedur sistematis mencari kombinasi parameter optimal di dalam `Pipeline` menggunakan **`GridSearchCV` / `RandomizedSearchCV`** (`param_grid={'clf__C': ..., 'clf__gamma': ...}`).
* **Sesi Praktikum Lab 7 (`170'`):** Menjalankan turnamen komparasi 5 algoritma *Supervised* lengkap *tuning* parameter dan klinik simulasi ujian praktik **UTS Pekan 8**.
* **PT (`120'`) & BM (`120'`):** Latihan mandiri membangun skrip *benchmarking* multi-model siap pakai untuk konsep UTS.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` [C5]) · **Bobot:** **25%** · **Durasi:** `150 menit` (*Live Notebook Modeling* di Lab).
* **Pelaksanaan:** Mahasiswa menerima dataset tabular baru di laboratorium, membangun `Pipeline` bersih, melatih serta mengoptimalkan parameter model **Supervised Learning** (*Linear/Logistic, Decision Tree, Random Forest, SVM*), dan menyajikan evaluasi pemilihan model terbaik secara mandiri.

### PERTEMUAN 9 — Klasterisasi Partisi **K-Means** (*K-Means++, Inertia, Elbow Method*)
* **Sub-CPMK:** `Sub-CPMK-2.2` [C5] · **Alat:** `KMeans, MiniBatchKMeans`.
* **Sesi Teori (`100'`):** Membahas umpan balik hasil UTS dan memasuki dunia data tanpa label (**Unsupervised Learning**): cara kerja iterasi pembaruan *centroid* **K-Means**, perbaikan inisialisasi **K-Means++**, keterbatasan bentuk klaster bulat/sensitivitas skala & pencilan, serta pembacaan grafik *Within-Cluster Sum of Squares* (**Elbow Method**).
* **Sesi Praktikum Lab 8 (`170'`):** Melakukan segmentasi perilaku transaksi pelanggan (*Recency, Frequency, Monetary — RFM*) menggunakan `Pipeline(StandardScaler + KMeans)` dan menyusun profil persona tiap klaster.
* **PT (`120'`) & BM (`120'`):** Menguji stabilitas hasil klaster pada beberapa nilai inisialisasi berbeda.

### PERTEMUAN 10 — **Hierarchical Clustering** (*Dendrogram*) & Validasi **Silhouette Score**
* **Sub-CPMK:** `Sub-CPMK-2.2` [C5] · **Alat:** `AgglomerativeClustering`, `scipy.cluster.hierarchy.dendrogram`, `silhouette_score`.
* **Sesi Teori (`100'`):** Mengajarkan klasterisasi berjenjang *bottom-up* (**Agglomerative Hierarchical Clustering**) dengan kriteria jarak *Ward, Complete, Average,* dan *Single Linkage* (beserta pengenalan ringkas *DBSCAN* untuk bentuk tak beraturan dan pendeteksi derau), lalu membedah rumus matematis **Silhouette Coefficient** $s(i) = \frac{b(i)-a(i)}{\max(a(i), b(i))} \in [-1, +1]$ sebagai tolok ukur objektif ketepatan klasterisasi. Merilis resmi **Tugas 2 (RTM-2)**.
* **Sesi Praktikum Lab 9 (`170'`):** Menggambar *Dendrogram*, memplot diagram pisau **Silhouette** per klaster untuk $K=2..7$, dan memilih segmentasi paling valid secara kuantitatif.
* **PT (`120'`) & BM (`120'`):** Mengerjakan tahap klasterisasi dan validasi siluet pada **Tugas 2**.

### PERTEMUAN 11 — Reduksi Dimensi **Principal Component Analysis (PCA)**
* **Sub-CPMK:** `Sub-CPMK-2.2` [C5] · **Alat:** `sklearn.decomposition.PCA`.
* **Sesi Teori (`100'`):** Menghidupkan kembali materi dekomposisi nilai eigen matriks kovarians & SVD dari `STI-205 Aljabar Linear dan Matriks` menjadi alat kompresi dimensi paling populer di sains data (**PCA**): konsep proyeksi ke sumbu varians maksimum ortogonal, kurva **Cumulative Explained Variance Ratio**, pembacaan bobot *loadings* komponen utama, serta kombinasi **PCA + K-Means** untuk memvisualisasikan klaster 20+ dimensi ke bidang 2D/3D.
* **Sesi Praktikum Lab 10 (`170'`):** Mereduksi dataset berdimensi tinggi menggunakan PCA dengan target retensi varians 95%, memetakan sebaran segmen klaster di ruang PC1–PC2, dan merampungkan eksperimen **Tugas 2**.
* **PT (`120'`) & BM (`120'`):** Menyelesaikan laporan dan *notebook* analisis **Tugas 2 (`CPMK-3`)**.

### PERTEMUAN 12 — Evaluasi Ketat Klasifikasi (**Confusion Matrix, F1-Score, ROC-AUC**) & Verifikasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.1` [C5] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alat:** `confusion_matrix, classification_report, roc_auc_score, RocCurveDisplay, PrecisionRecallDisplay`.
* **Sesi Teori (`100'`):** Mengapa model pendeteksi penipuan yang selalu menebak *"Bukan Penipuan"* mendapat *Accuracy* 99,2% tetapi bernilai bisnis **nol besar**? Membedah tuntas **Confusion Matrix** (*TP, FP, TN, FN*), makna biaya bisnis di balik **Precision** vs **Recall**, rata-rata harmonik **F1-Score**, penggeseran ambang probabilitas `predict_proba`, kurva **ROC-AUC** vs **PR-AUC**, serta penanganan kelas timpang (`class_weight='balanced'`).
* **Sesi Praktikum Lab 11 (`170'`):** Verifikasi demo & tanya-jawab **Tugas 2 (`CPMK-3`)** di laboratorium, dilanjutkan latihan evaluasi klasifikasi kelas timpang dan pemilihan *threshold* optimal berbasis biaya kesalahan.
* **PT (`120'`) & BM (`120'`):** Menentukan topik dan dataset tabular dunia nyata untuk proyek akhir tim UAS.

### PERTEMUAN 13 — *Cross-Validation* Ketat, *Error Slicing*, & Interpretabilitas Model (*Explainable ML*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C5] · **Alat:** `StratifiedKFold`, `permutation_importance`, `CalibrationDisplay`.
* **Sesi Teori (`100'`):** Mengajarkan evaluasi reliabilitas lintas lipatan (**Stratified K-Fold Cross-Validation** melaporkan $\mu \pm \sigma$ metrik, bukan satu angka keberuntungan pembagian!), analisis irisan kesalahan (*error slicing* — di segmen mana model paling sering meleset?), serta teknik menjelaskan prediksi kotak hitam *ensemble* menggunakan **Permutation Feature Importance** dan pengenalan nilai kontribusi lokal (*SHAP mindset*).
* **Sesi Praktikum Lab 12 (`170'`):** Menjalankan evaluasi *5-Fold Stratified CV*, bedah kasus *False Positive / False Negative* terburuk, dan visualisasi peringkat kontribusi fitur pada model proyek akhir tim.
* **PT (`120'`) & BM (`120'`):** Menyusun bab evaluasi performa mendalam pada laporan proyek akhir UAS.

### PERTEMUAN 14 — Serialisasi `Pipeline` Utuh (`joblib`) & Rekayasa Modul Inferensi Andal
* **Sub-CPMK:** `Sub-CPMK-3.2` [C6] · **Alat:** `joblib`, `pydantic` / validasi skema Python.
* **Sesi Teori (`100'`):** Menjelaskan mengapa menyimpan hanya objek model `rf_model.pkl` tanpa ikut membungkus *imputer/encoder/scaler* di dalam satu objek `Pipeline` pasti memicu bencana saat memprediksi data baru! Mengajarkan pembungkusan artefak `full_pipeline.joblib`, pencatatan versi pustaka (`requirements.txt` & metadata fitur), serta penulisan fungsi pembungkus inferensi yang memvalidasi tipe dan rentang masukan data baru secara defensif.
* **Sesi Praktikum Lab 13 (`170'`):** Mengekspor `Pipeline` terbaik tim ke `.joblib` dan mengujinya pada skrip Python bersih terpisah dengan skenario data valid, nilai kosong, maupun kategori baru tak dikenal.
* **PT (`120'`) & BM (`120'`):** Merancang tata letak antarmuka pengguna untuk aplikasi purwarupa inferensi.

### PERTEMUAN 15 — Pembangunan **Purwarupa Aplikasi Inferensi Terintegrasi** (`Streamlit`) & Klinik UAS
* **Sub-CPMK:** `Sub-CPMK-3.2` [C6] · **Alat:** `Streamlit` / `Gradio`, Git Repository.
* **Sesi Teori (`100'`):** Mengajarkan prinsip menyajikan model *Machine Learning* agar langsung bernilai pakai bagi pengambil keputusan: formulir input tervalidasi untuk prediksi tunggal (*single inference* lengkap probabilitas keyakinan & 3 faktor pendorong utama), fitur unggah CSV untuk prediksi massal (*batch inference*) beserta unduhan hasil, serta penjelasan jembatan menuju `STI-624` (*Deep Learning*), `STI-726` (*Integrasi AI*), dan `STA-701` (*MLOps*).
* **Sesi Praktikum Lab 14 (`170'`):** Membangun dan menguji silang aplikasi purwarupa inferensi `Streamlit` antar-kelompok di laboratorium (mencoba memasukkan kasus batas untuk menguji keandalan sebelum UAS).
* **PT (`120'`) & BM (`120'`):** Finalisasi repositori Git, laporan evaluasi model, dan kesiapan aplikasi inferensi untuk UAS Pekan 16.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C5, C6]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Repositori, Laporan Evaluasi Model (Confusion Matrix, F1-Score, ROC-AUC), & Purwarupa Inferensi (50% nilai UAS)** dengan **Sidang Uji *Unseen Holdout Data* Langsung & Verifikasi Individu (50% nilai UAS)** — penguji memasukkan berkas uji rahasia (*blind test set*) langsung ke purwarupa inferensi tim untuk memverifikasi keandalan dan ketiadaan *overfitting/leakage*, serta menguji setiap anggota secara individu.
