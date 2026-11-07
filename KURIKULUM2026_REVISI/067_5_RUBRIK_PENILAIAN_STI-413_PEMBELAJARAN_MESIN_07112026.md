# 067_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-413 — PEMBELAJARAN MESIN (*Machine Learning*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI413` · **Klaster Rubrik Master (Dok 018):** Klaster 3 (`K-3`)  
**CPL:** `CPL-06` (`P2` = 45%) & `CPL-09` (`KK1` = 55%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN SAINS DATA & PEMBELAJARAN MESIN (`K-3`)

Mengacu **Dokumen 018 §3 (Klaster `K-3`)**, penilaian pada `STI-413 Pembelajaran Mesin` menilai kejujuran metodologis eksperimen (**bebas *data leakage***), ketepatan pemilihan algoritma dan optimasi hiperparameter, validitas statistik evaluasi metrik (*F1-Score, ROC-AUC, Silhouette Score*), serta keandalan purwarupa inferensi saat menerima data baru yang belum pernah dilihat model.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-06` [C3])
**Objek Penilaian:** *Notebook* Alur Kerja Rekayasa Data ML (*EDA, Imputation, Encoding, Scaling*) & `Pipeline` Bebas *Data Leakage*.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Kedalaman EDA & Deteksi Kolom *Target Leakage***<br>(`Sub-CPMK-1.1`) | **25%** | Mengungkap pola distribusi, nilai hilang, pencilan, dan berhasil menemukan seluruh kolom jebakan *target leakage* dengan argumen domain yang sangat tajam. | EDA informatif dan berhasil mendeteksi kolom *target leakage* utama dengan alasan yang tepat. | Menampilkan statistik deskriptif dan grafik dasar, namun salah satu kolom *leakage* halus belum disadari tanpa petunjuk. | EDA sekadar mencetak `.head()` dan `.info()` tanpa interpretasi distribusi maupun pemeriksaan *leakage*. | Tidak melakukan EDA sebelum transformasi data. |
| **2. Ketepatan *Imputation, Encoding,* & *Scaling***<br>(`Sub-CPMK-1.1`) | **35%** | Pemilihan strategi imputasi (median/modus), `OneHotEncoder(handle_unknown='ignore')` / `OrdinalEncoder`, dan `Standard/RobustScaler` 100% tepat sesuai karakteristik tiap kolom. | Seluruh tipe kolom numerik dan kategorikal ditransformasikan dengan transformer `scikit-learn` yang sesuai. | Transformasi berjalan tanpa galat, namun menyamakan perlakuan *mean imputation* pada kolom yang sangat menceng ber-pencilan. | Menggunakan `LabelEncoder` untuk fitur input nominal multi-kategori sehingga menciptakan urutan angka palsu. | Gagal menangani nilai hilang dan fitur kategorikal. |
| **3. Arsitektur `Pipeline` Bebas **Data Leakage****<br>(`Sub-CPMK-1.2`) | **30%** | Pembagian data dilakukan paling awal (`stratify=y`), seluruh langkah terbungkus rapi dalam `ColumnTransformer` + `Pipeline`, dan **0% *data leakage*** saat diuji `cross_val_score`. | Menggunakan `ColumnTransformer` + `Pipeline` dengan benar (`fit` hanya pada `X_train`, `transform` pada `X_test`). | Pemisahan `fit(X_train)` dan `transform(X_test)` benar, namun masih ditulis terpisah manual belum utuh menjadi satu objek `Pipeline`. | **Terjadi *Data Leakage***: memanggil `fit_transform` pada keseluruhan dataset sebelum `train_test_split`! | Seluruh alur pra-pemrosesan bocor atau gagal dieksekusi. |
| **4. Reproduksibilitas *Notebook* & Verifikasi Lab** | **10%** | `Run All` berjalan mulus dari atas ke bawah dengan `random_state` tetap dan mahasiswa menjawab verifikasi lab dengan tepat. | *Notebook* terstruktur rapi, reproduksibel, dan hasil verifikasi kelas baik. | *Notebook* berjalan baik walau komentar penjelasan masih ringkas. | Sel *notebook* dieksekusi acak tidak berurutan sehingga gagal saat di-*Run All*. | Menyalin *notebook* rekan lain. |

$$\text{Skor Tugas 1} = 0,25(K_1) + 0,35(K_2) + 0,30(K_3) + 0,10(K_4)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-09` [C5])
**Objek Penilaian:** Ujian Praktik 150 Menit: Konstruksi & Optimasi Model *Supervised Learning* (*Linear/Logistic, Decision Tree, Random Forest, SVM*).

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Validitas `Pipeline` Pelatihan & Disiplin Anti-Leakage** | **25%** | Seluruh kandidat model dilatih di dalam `Pipeline` yang bersih (termasuk penskalaan fitur wajib untuk SVM/Regresi Regularisasi) tanpa kebocoran data uji. | `Pipeline` pra-pemrosesan dan pembagian *train/test* dibangun benar untuk seluruh model yang diuji. | Pembagian data benar, namun penskalaan fitur untuk SVM dilakukan terpisah di luar objek `Pipeline`. | Melatih model tanpa menangani fitur kategorikal/skala sehingga SVM berkinerja sangat buruk, atau mengintip data uji saat *tuning*. | `Pipeline` gagal berjalan pada dataset ujian. |
| **2. Konstruksi 4 Keluarga Model *Supervised***<br>(`Sub-CPMK-2.1`) | **35%** | Berhasil mengonstruksi dan melatih keempat model (*Linear/Logistic, Decision Tree, Random Forest, SVM*) dengan konfigurasi dasar yang tepat dan perbandingan apel-ke-apel yang adil. | Keempat model berhasil dilatih dan dievaluasi pada skema validasi yang seragam. | Berhasil melatih minimal 3 dari 4 keluarga model dengan benar. | Hanya berhasil melatih 1–2 model sederhana karena kesalahan pemanggilan API `scikit-learn`. | Tidak mampu melatih model *Supervised Learning* secara mandiri. |
| **3. Optimasi Parameter (`GridSearchCV` / `RandomizedSearchCV`)** | **30%** | Ruang pencarian hiperparameter masuk akal secara teoretis, dieksekusi bersih via `GridSearchCV`/`RandomizedSearchCV` di atas data latih, dan terbukti meningkatkan generalisasi tanpa *overfitting*. | `GridSearchCV` berjalan benar pada model kandidat utama dan menghasilkan parameter terbaik yang valid. | Menjalankan pencarian parameter sederhana (hanya 1 parameter dengan 2 nilai) namun secara sintaks benar. | Menjalankan `GridSearchCV` menggunakan `X_test` atau salah penamaan prefix `step__param` sehingga gagal berjalan. | Tidak melakukan optimasi parameter sama sekali. |
| **4. Justifikasi Pemilihan Model Terbaik** | **10%** | Memilih model pemenang dengan menimbang selisih skor *train vs validation/test*, kecepatan inferensi, dan interpretabilitas secara tajam. | Pemilihan model akhir didukung tabel perbandingan metrik yang jelas dan logis. | Memilih model dengan skor tertinggi namun belum mengomentari jarak *train–test gap*. | Memilih model yang jelas mengalami *severe overfitting* (skor latih 100%, skor uji rendah). | Tidak menyertakan kesimpulan pemilihan model. |

$$\text{Skor UTS} = 0,25(K_1) + 0,35(K_2) + 0,30(K_3) + 0,10(K_4)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-06` [C5])
**Objek Penilaian:** Studi Kasus *Unsupervised Learning* (**K-Means, Hierarchical Clustering, & PCA**) dengan Validasi **Silhouette Score**.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Penskalaan & Konstruksi **K-Means + Hierarchical****<br>(`Sub-CPMK-2.2`) | **35%** | Menerapkan penskalaan yang tepat sebelum perhitungan jarak, membandingkan secara sistematis **K-Means** (*Elbow*) dan **Hierarchical Clustering** (*Dendrogram* berbagai *linkage*) dengan sangat akurat. | Konstruksi model K-Means dan Hierarchical Clustering beserta visualisasi *Elbow* dan *Dendrogram* tepat. | Berhasil menjalankan K-Means dan membuat *Dendrogram* dasar, namun hanya menguji 1 jenis *linkage*. | **Lupa menstandarkan skala fitur** sebelum K-Means sehingga klaster didominasi satu kolom berangka jutaan! | Gagal mengonstruksi model klasterisasi tak-terbimbing. |
| **2. Reduksi Dimensi **PCA** & Proyeksi Visual**<br>(`Sub-CPMK-2.2`) | **25%** | Menganalisis kurva *Cumulative Explained Variance Ratio* secara tepat, menafsirkan *loadings* komponen utama, dan menyajikan visualisasi sebaran klaster di ruang 2D/3D PCA yang sangat jernih. | Penerapan PCA, pemilihan komponen, dan plot sebaran klaster pada PC1–PC2 akurat dan informatif. | Menjalankan PCA 2 komponen untuk plot sebaran, namun belum membahas proporsi varians yang berhasil dipertahankan. | Salah menerapkan PCA pada kolom ID/kategorikal mentah tanpa pra-pemrosesan. | Tidak menyertakan analisis reduksi dimensi PCA. |
| **3. Validasi Kuantitatif **Silhouette Score****<br>(`Sub-CPMK-2.2`) | **25%** | Mengevaluasi **Silhouette Score** rata-rata sekaligus distribusi *Silhouette Plot* per klaster pada rentang nilai $K$, menjustifikasi titik $K$ optimal secara tajam dan objektif. | Menghitung dan memplot *Silhouette Score* lintas nilai $K$ untuk memvalidasi jumlah klaster terpilih dengan benar. | Mencantumkan angka *Silhouette Score* untuk satu nilai $K$ saja tanpa membandingkan beberapa kandidat $K$. | Memilih jumlah klaster secara sembarang meskipun nilai *Silhouette Score*-nya mendekati nol/negatif. | Tidak melakukan validasi siluet terhadap hasil klasterisasi. |
| **4. Interpretasi Profil Segmen & Rekomendasi Bisnis** | **15%** | Menerjemahkan rata-rata/median fitur tiap klaster menjadi nama persona segmen yang tajam beserta rekomendasi tindakan bisnis yang spesifik. | Profil karakteristik tiap klaster dijelaskan dengan jelas dan relevan bagi konteks organisasi. | Menjelaskan perbedaan angka rata-rata antar-klaster secara deskriptif dasar. | Biarkan klaster hanya bernama `"Cluster 0, Cluster 1, Cluster 2"` tanpa interpretasi makna domain. | Gagal menjelaskan hasil kerjanya saat verifikasi di lab. |

$$\text{Skor Tugas 2} = 0,35(K_1) + 0,25(K_2) + 0,25(K_3) + 0,15(K_4)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-09` [C5, C6])
**Objek Penilaian:** Evaluasi Performa Model (**Confusion Matrix, F1-Score, ROC-AUC**) & **Purwarupa Inferensi Terintegrasi** + Sidang Uji *Blind Data*.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Evaluasi Performa Komprehensif (*Confusion Matrix, F1, ROC-AUC*)**<br>(`Sub-CPMK-3.1`) | **35%** | Evaluasi memakai *Stratified K-Fold CV*, membedah **Confusion Matrix, Precision, Recall, F1-Score, PR/ROC-AUC**, penalaan *threshold* biaya kesalahan, *error slicing*, dan *Feature Importance* secara tajam. | Evaluasi metrik *Confusion Matrix, F1-Score,* dan *ROC-AUC* lengkap, akurat, dan disertai analisis kesalahan yang logis. | Melaporkan *Confusion Matrix, F1-Score,* dan *ROC-AUC* pada data uji dengan benar, namun analisis penalaan *threshold* atau *feature importance* masih ringkas. | Hanya melaporkan angka *Accuracy* pada dataset yang jelas timpang tanpa menganalisis *False Negative / False Positive*. | Evaluasi model keliru secara metodologis atau terindikasi *data leakage*. |
| **2. Keandalan **Purwarupa Inferensi Terintegrasi** pada Data Baru**<br>(`Sub-CPMK-3.2`) | **35%** | `Pipeline` utuh terserialisasi rapi, aplikasi `Streamlit` menangani input satuan & unggah *blind CSV* penguji dengan **0 error**, menampilkan prediksi + probabilitas + faktor penjelas secara instan dan andal. | Purwarupa inferensi terintegrasi berjalan mulus memproses data baru (*single & batch*) saat diuji langsung oleh penguji. | Aplikasi purwarupa inferensi berjalan baik untuk input formulir satuan, namun fitur *batch CSV* atau validasi input batas masih sederhana. | Purwarupa langsung *crash* (`ValueError` kolom/skala tidak cocok) saat diberi baris data baru dari penguji karena hanya menyimpan model tanpa `Pipeline`! | Tidak berhasil membangun purwarupa inferensi yang berjalan. |
| **3. Reproduksibilitas Repositori Git & Dokumentasi** | **15%** | Struktur repositori standar (`data/`, `notebooks/`, `models/`, `app.py`, `requirements.txt`, `README.md`), riwayat *commit* seluruh anggota tim merata dan transparan. | Repositori rapi, dapat dijalankan ulang dengan mudah, dan kontribusi Git tiap anggota terverifikasi. | Repositori cukup lengkap walau `requirements.txt` atau *commit* sebagian anggota kurang rapi. | Kode berantakan tanpa struktur pemisahan eksperimen vs aplikasi inferensi. | Plagiarisme proyek publik tanpa rekayasa mandiri. |
| **4. Penguasaan Sidang & Tanya-Jawab Individu** | **15%** | Setiap anggota fasih menjawab pertanyaan penguji mengenai intuisi algoritma, makna kurva ROC-AUC, dan alur kode inferensi tanpa keraguan. | Anggota mampu menjelaskan bagian eksperimen dan modul inferensi tanggung jawabnya dengan akurat. | Anggota memahami alur utama proyek dengan sedikit bantuan klarifikasi. | Tidak mampu menjelaskan arti angka *F1-Score* atau cara `Pipeline` memproses data baru pada proyeknya sendiri. | Tidak hadir sidang UAS atau melanggar kejujuran akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,15(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF EKSPERIMEN NOTEBOOK LABORATORIUM MINGGUAN

| Kriteria Formatif Lab | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Disiplin Metodologi Eksperimen** | Selalu memisahkan *train/test* di awal, mencatat `random_state`, dan menuliskan interpretasi sel Markdown di setiap akhir eksperimen. | Menyelesaikan seluruh *notebook* praktikum tepat waktu dengan alur bersih. | Menyelesaikan kode utama praktikum namun minim catatan analisis Markdown. | Sering mencampur data uji ke proses pelatihan atau tidak menyelesaikan lab. |
| **Kemandirian Eksplorasi Dokumentasi `scikit-learn`** | Aktif membaca parameter dokumentasi resmi `scikit-learn` dan menguji variasi parameter sendiri. | Mampu menyesuaikan parameter estimator sesuai instruksi modul. | Bergantung penuh pada kode contoh tanpa mencoba variasi parameter. | Pasif menyalin sel kode tanpa memahami masukannya. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-413` (`CPL-06` & `CPL-09` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai penuh rekayasa `Pipeline` bebas *data leakage*, konstruksi dan optimasi model *Supervised* & *Unsupervised* tabular, evaluasi tajam berbasis biaya bisnis (*F1, ROC-AUC, Silhouette*), serta mampu menghadirkan purwarupa inferensi terintegrasi yang tahan banting terhadap data baru. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa terampil membangun alur `scikit-learn Pipeline`, melatih dan menala model prediktif maupun klasterisasi/PCA, mengevaluasi metrik secara tepat, dan mengintegrasikan model ke aplikasi inferensi fungsional. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam pra-pemrosesan bebas *leakage*, pelatihan model standar *Supervised/Unsupervised*, pembacaan *Confusion Matrix*, dan serialisasi model dasar. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih melakukan kesalahan metodologis (*data leakage*, lupa penskalaan pada jarak/SVM, hanya melihat *Accuracy* pada kelas timpang) dan gagal membungkus model untuk inferensi data baru. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal membangun alur dasar pemodelan *Machine Learning* atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-413` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menerapkan alur kerja rekayasa data ML (*EDA, imputation, encoding, scaling*) menggunakan `scikit-learn`. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menyusun `ColumnTransformer` dan `Pipeline` *Machine Learning* yang 100% bebas *data leakage*. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengonstruksi dan mengoptimalkan model *Supervised* (*Linear/Logistic, Decision Tree, Random Forest, SVM*). | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu mengonstruksi model *Unsupervised* (*K-Means, Hierarchical, PCA*) dengan validasi **Silhouette Score** yang valid. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengevaluasi performa model secara kritis menggunakan **Confusion Matrix, F1-Score,** dan **ROC-AUC**. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu membangun purwarupa aplikasi inferensi model terintegrasi yang andal memproses data baru. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-413`)

```text
==============================================================================================================================
             LEMBAR REKAPITULASI PENILAIAN OBE — STI-413 PEMBELAJARAN MESIN (3 SKS: T=2, P=1)
==============================================================================================================================
Semester / TA  : Semester 4 (Genap) / 2026-2027      CPL Dibebankan : CPL-06 (P2: 45%) & CPL-09 (KK1: 55%) [Level: Reinforce]
Klaster Rubrik : K-3 (AI, Cloud & Cybersecurity)     Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2 (25%)    | UAS (30%)      | NA    | CPL-06 | CPL-09 | Huruf
   |           |                  | [CPMK-1:C3] | [CPMK-2:C5] | [CPMK-3:C5] | [CPMK-4:C5/C6] | Akhir | (45%)  | (55%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 86.0        | 88.0        | 90.0           | 88.10 | 88.00  | 88.18  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 74.0        | 76.0        | 78.0           | 76.50 | 76.89  | 76.18  | B+
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0           | 68.00 | 69.11  | 67.09  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 78.00       | 75.33       | 78.00       | 78.67          | 77.53 | 78.00  | 77.15  | >=65:100%
==============================================================================================================================
```
