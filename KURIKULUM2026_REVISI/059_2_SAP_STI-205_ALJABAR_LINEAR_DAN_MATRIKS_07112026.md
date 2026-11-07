# 059_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-205 — ALJABAR LINEAR DAN MATRIKS (*Linear Algebra and Matrices*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI205`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` · Dok 032 (Modalitas Pembelajaran SCL KPT 2024) · Dok 043 (Boundary Guardrails).

---

## BAGIAN I — IDENTITAS & REKAPITULASI OPERASIONAL PERKULIAHAN

| Atribut Operasional | Ketentuan Pelaksanaan di Kelas |
|---|---|
| **Kode & Nama Mata Kuliah** | `STI-205` — Aljabar Linear dan Matriks (*Linear Algebra and Matrices*) — Kurikulum OBE SISTEKIN 2026 |
| **Bobot & Tipe Perkuliahan** | **3 SKS Teori** (`T=3, P=0`) · Semester 2 (Genap) · Prasyarat: `STI-102` Kalkulus |
| **CPL & CPMK Dibebankan** | `CPL-05` (`P1` — Level *Introduce*) · `CPMK-1` (C3), `CPMK-2` (C4), `CPMK-3` (C3), `CPMK-4` (C4) |
| **Durasi per Pertemuan (SN-Dikti)** | **Tatap Muka (TM): 150 menit** ($3 \times 50'$) · **Penugasan Terstruktur (PT): 180 menit** ($3 \times 60'$) · **Belajar Mandiri (BM): 180 menit** ($3 \times 60'$) |
| **Struktur Baku Waktu Tatap Muka** | **Pendahuluan & Intuisi Geometri/AI:** `20 menit` · **Kegiatan Inti (Penurunan Aljabar + *Guided Matrix / Eigen / SVD Workshop*):** `110 menit` · **Penutup, Cek Pemahaman & Tindak Lanjut:** `20 menit` |
| **Media & Alat Bantu Komputasi** | Papan Tulis Lebar, Proyektor, GeoGebra 2D/3D Vector & Linear Transformation Applet, serta *Zero-Install Browser Notebook* (Google Colab / JupyterLite khusus Pekan 15 untuk komputasi matriks primitif `numpy.linalg`), LMS Edlink. |
| **Pagar Pembatas Kelas (*Guardrails*)** | 🟢 Fokus pada SPL, Gauss-Jordan, matriks invers, ruang vektor $\mathbb{R}^n$, basis-dimensi, nilai/vektor eigen, diagonalisasi, serta formulasi SVD dan PCA berbantuan `NumPy` murni.<br>❌ **Larangan Kelas:** Dilarang mengajarkan pelatihan model *Machine Learning* dengan `scikit-learn` (`STI-413 Pembelajaran Mesin`), jaringan saraf mendalam (`STI-624`), koding aplikasi web (`STI-311`/`STI-416`), atau mengulang limit-integral kalkulus (`STI-102`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Fokus Sesi Perkuliahan | Strategi SCL Utama | Durasi TM | Evaluasi |
|:---:|:---:|---|---|:---:|:---:|
| **1** | `Sub-CPMK-1.1` | Kontrak Belajar, Vektor $\mathbb{R}^n$, *Dot Product*, *Cosine Similarity*, & Operasi Matriks | *Interactive Lecture & Matrix Drill* | 150' | Formatif |
| **2** | `Sub-CPMK-1.1, 1.2` | Pemodelan SPL, Eliminasi Gauss & Gauss-Jordan, serta 3 Jenis Solusi Eselon Baris | *Collaborative Problem Solving* | 150' | Formatif |
| **3** | `Sub-CPMK-1.1, 1.2` | Determinan Matriks, Matriks Invers ($A^{-1}$), & Penyelesaian SPL $x = A^{-1}b$ | *Problem-Based Learning (PBL)* | 150' | Formatif (Rilis Tugas 1) |
| **4** | `Sub-CPMK-2.1` | Ruang Vektor Riil $\mathbb{R}^n$, Uji Subruang, Kombinasi Linier, & Rentang (*Span*) | *Geometric & Algebraic Discovery* | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1, 2.2` | Kebebasan Linier (*Linear Independence*), Basis, & Dimensi Ruang Vektor $\mathbb{R}^n$ | *Problem-Solving Class* | 150' | Formatif |
| **6** | `Sub-CPMK-2.1, 2.2` | Ruang Baris, Ruang Kolom, Ruang Nol (*Null Space*), & Teorema Rank-Nullitas | *Case-Based Data Rank Analysis* | 150' | Formatif |
| **7** | `Sub-CPMK-2.2` | Ortogonalitas, Proyeksi Ortogonal, Proses *Gram-Schmidt*, & Review Pra-UTS | *Problem-Solving Workshop* | 150' | Formatif |
| **8** | `CPMK-2` (& `CPMK-1`) | **Ujian Tengah Semester (UTS) — Ruang Vektor, Kebebasan Linier, Basis, & Dimensi** | *Analytical Written Exam* | 150' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.2` | Matriks Transformasi Linier Geometri (Rotasi, Refleksi, Skala, Geser), Kernel, & *Range* | *Visual Transformation Workshop* | 150' | Formatif |
| **10** | `Sub-CPMK-3.1` | Polinomial Karakteristik, Nilai Eigen (*Eigenvalues*), & Vektor Eigen (*Eigenvectors*) | *Problem-Solving Class* | 150' | Formatif (Rilis Tugas 2) |
| **11** | `Sub-CPMK-3.1, 3.2` | Diagonalisasi Matriks ($A=PDP^{-1}$), Perpangkatan $A^k$, & Rantai *Markov/PageRank* | *Case-Based Markov Modeling* | 150' | Formatif |
| **12** | `Sub-CPMK-3.1, 3.2` | Matriks Simetris Riil & Diagonalisasi Ortogonal ($A=Q\Lambda Q^T$ — Teorema Spektral) | *Problem-Solving Class* | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-4.1` | Formulasi Analitis *Singular Value Decomposition* ($A=U\Sigma V^T$) & *Low-Rank* | *Case-Based SVD Workshop* | 150' | Formatif |
| **14** | `Sub-CPMK-4.1, 4.2` | Matematika *Principal Component Analysis* (PCA): Kovarians, Proyeksi, & Variansi | *Problem-Solving AI Math Class* | 150' | Formatif |
| **15** | `Sub-CPMK-4.2` | Komputasi SVD & Reduksi Dimensi PCA dengan Python `NumPy` Murni + Review UAS | *Interactive NumPy Math Clinic* | 150' | Formatif |
| **16** | `CPMK-4` (& `1–3`) | **Ujian Akhir Semester (UAS) — Perumusan SVD, PCA (`NumPy`), & Sintesis** | *Hybrid NumPy Check + Written Exam* | 150' | **UAS (30%)** |

---

## BAGIAN II — RINCIAN SATUAN ACARA PERKULIAHAN PER PERTEMUAN (PERTEMUAN 1 s.d. 16)

---

### PERTEMUAN 1 — Kontrak Belajar, Vektor di Ruang $\mathbb{R}^n$, *Cosine Similarity*, & Aljabar Matriks
* **Kemampuan Akhir (`Sub-CPMK-1.1` [C3]):** Melakukan operasi aljabar vektor pada ruang $\mathbb{R}^n$ dan operasi aljabar matriks dengan tepat.
* **Indikator Capaian:** (1) Menghitung kombinasi vektor, *dot product* $\mathbf{u}\cdot\mathbf{v}$, norma $\|\mathbf{u}\|_2$, dan kemiripan sudut *cosine similarity* $\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}$; (2) Melakukan penjumlahan matriks, perkalian matriks $AB$ (pandangan baris-kali-kolom dan kombinasi linier kolom), serta transpos $(AB)^T = B^T A^T$.
* **Pokok Bahasan:** Orientasi RPS OBE, Mengapa Semua Data di AI Adalah Vektor & Matriks, Vektor di $\mathbb{R}^n$, *Dot Product & Cosine Similarity*, serta Operasi & Sifat Aljabar Matriks.
* **Metode & Media:** *Interactive Lecture & Matrix Drill*; Papan Tulis, Slide Kasus *Vector Search/Recommender*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memperkenalkan RPS `STI-205`, kaitan prasyarat `STI-102` dan *handoff* menuju `STI-413 Pembelajaran Mesin`, lalu memantik kasus modern: *"Bagaimana mesin pencari AI atau Spotify mengetahui bahwa dua dokumen atau selera lagu pengguna sangat mirip?"* | Menyimak kontrak belajar dan mengamati bagaimana profil selera pengguna diubah menjadi vektor angka di $\mathbb{R}^n$. | 20' | RPS `STI-205` & Slide |
| **Kegiatan Inti** | Menguraikan geometri dan aljabar vektor di $\mathbb{R}^n$, menghitung *dot product*, jarak Euclidean, dan *cosine similarity* pada 3 vektor profil dokumen; melanjutkan operasi matriks, mengapa secara umum $AB \neq BA$, aturan transpos perkalian $(AB)^T = B^T A^T$, serta matriks khusus (identitas, diagonal, segitiga, simetris). | Berlatih menghitung *cosine similarity* antar-vektor fitur secara manual untuk menentukan pasangan dokumen paling mirip, serta mengerjakan 6 soal operasi perkalian dan transpos matriks. | 110' | `[1]` Bab 1.3–1.4 & 3.1–3.2, `[5]` Bab 1–3 |
| **Penutup** | Merangkum dua cara memandang $A\mathbf{x}$ (perkalian baris dengan $\mathbf{x}$ vs kombinasi linier kolom-kolom $A$) sebagai kunci memahami Pekan 2–6. | Mengerjakan kuis singkat 4 soal dimensi perkalian matriks di Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 10 soal aljabar vektor, *cosine similarity*, dan perkalian blok matriks pada Bab 1 Modul Ajar.

---

### PERTEMUAN 2 — Pemodelan SPL, Eliminasi Gauss & Gauss-Jordan, serta Klasifikasi Solusi Eselon Baris
* **Kemampuan Akhir (`Sub-CPMK-1.1` & `Sub-CPMK-1.2` [C3]):** Menyelesaikan Sistem Persamaan Linear (SPL) dengan eliminasi Gauss-Jordan dan menentukan jenis solusi SPL dari bentuk eselon baris.
* **Indikator Capaian:** (1) Menyusun matriks *augmented* $[A \mid \mathbf{b}]$ dan mengeksekusi tiga Operasi Baris Elementer (OBE) menuju *Row Echelon Form* (`REF`) dan *Reduced Row Echelon Form* (`RREF`); (2) Mengidentifikasi variabel utama (*pivot*) dan variabel bebas untuk menentukan secara pasti apakah SPL memiliki **solusi tunggal**, **tak hingga banyak solusi** (dalam bentuk vektor berparameter), atau **tidak memiliki solusi**.
* **Pokok Bahasan:** Geometri Perpotongan Hiperbidang SPL, Tiga Operasi Baris Elementer, Eliminasi Gauss (Substitusi Balik) vs Eliminasi Gauss-Jordan (`RREF`), dan Kriteria 3 Jenis Solusi SPL.
* **Metode & Media:** *Collaborative Problem Solving*; Papan Tulis, Studi Kasus Keseimbangan Arus Trafik Jaringan, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan diagram persimpangan 4 jalur *router* jaringan data (hukum kekekalan arus masuk = arus keluar) yang melahirkan sistem 4 persamaan linear dengan 4 variabel. | Merumuskan persamaan keseimbangan tiap simpul menjadi matriks *augmented* $[A \mid \mathbf{b}]$. | 20' | Slide Kasus Arus Trafik |
| **Kegiatan Inti** | Melatih disiplin urutan OBE agar tidak berputar-putar tanpa akhir (bekerja kolom demi kolom dari kiri ke kanan membentuk utama `1` lalu mengenolkan elemen di bawah/atasnya), membedakan ciri baris kontradiktif `[0 0 ... 0 | c ≠ 0]` (tak ada solusi) vs adanya kolom tanpa *pivot* (tak hingga solusi berparameter bebas $t, s$), serta menganalisis SPL berparameter $k$. | Kelompok menyelesaikan 6 variasi SPL (termasuk sistem *underdetermined* dan sistem berparameter $k$) dengan Gauss-Jordan dan mempresentasikan langkah OBE-nya di papan tulis. | 110' | `[1]` Bab 1.1–1.2, `[3]` Bab 1.1–1.2 |
| **Penutup** | Merangkum tabel ringkas 3 kemungkinan solusi SPL berdasarkan posisi *pivot* pada matriks eselon baris. | Mengunggah hasil latihan kelompok ke LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan 10 soal eliminasi Gauss-Jordan dan analisis parameter solusi SPL.

---

### PERTEMUAN 3 — Determinan Matriks, Matriks Invers ($A^{-1}$), & Penyelesaian SPL $x = A^{-1}b$
* **Kemampuan Akhir (`Sub-CPMK-1.1` & `Sub-CPMK-1.2` [C3]):** Menghitung determinan dan matriks invers untuk menyelesaikan SPL serta menganalisis keterkaitan invertibilitas matriks dengan ketunggalan solusi.
* **Indikator Capaian:** (1) Menghitung $\det(A)$ menggunakan ekspansi kofaktor baris/kolom maupun reduksi baris ke matriks segitiga; (2) Menghitung matriks invers $A^{-1}$ menggunakan metode Gauss-Jordan bergandeng $[A \mid I] \to [I \mid A^{-1}]$ serta matriks adjoin, dan menyelesaikan $Ax=b$ melalui $x=A^{-1}b$.
* **Pokok Bahasan:** Determinan & Tafsir Geometri Faktor Skala Luas/Volume, Sifat-Sifat Determinan terhadap OBE, Matriks Invers ($A^{-1}$), Syarat Matriks Singular ($\det(A)=0$), dan Teorema Ekuivalensi Matriks Invertibel.
* **Metode & Media:** *Problem-Based Learning* (PBL); GeoGebra 2D Area Determinant, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memvisualisasikan di layar bagaimana sebuah persegi satuan berubah menjadi jajargenjang seluas $|\det(A)|$ saat dikalikan matriks $A$, dan mengempis menjadi garis gepeng berluas **nol** saat $\det(A)=0$ (itulah sebabnya transformasi tersebut tak dapat dibalik / tak punya invers!). | Mengamati makna geometris mengapa $\det(A)=0$ membuat informasi dimensi hilang sehingga $A^{-1}$ tidak ada. | 20' | GeoGebra Applet |
| **Kegiatan Inti** | Melatih perhitungan determinan cerdas (memanfaatkan OBE agar banyak nol sebelum ekspansi kofaktor), mencari invers matriks $3\times 3$ dengan skema $[A \mid I] \to [I \mid A^{-1}]$, menyelesaikan $x = A^{-1}b$ untuk beberapa vektor ruas kanan $\mathbf{b}$ sekaligus, serta merangkai Teorema Ekuivalensi ($A$ invertibel $\iff \det(A)\neq 0 \iff \text{RREF}(A)=I \iff Ax=b$ punya solusi tunggal). | Berlatih mencari determinan, menguji invertibilitas, menghitung $A^{-1}$, dan memverifikasi $AA^{-1}=I$ secara teliti. | 110' | `[1]` Bab 1.5–1.6 & Bab 2, `[3]` Bab 2–3 |
| **Penutup** | Merangkum ketuntasan penuh `CPMK-1` dan **merilis resmi naskah RTM-1 (Tugas 1 — Bobot 20%)** di LMS Edlink untuk dikumpulkan pada Pekan 4. | Mengunduh instruksi Tugas 1 berparameter NIM di Edlink. | 20' | Dokumen RTM-1 di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan secara mandiri seluruh 4 masalah pada **Tugas 1 (`CPMK-1`)**.

---

### PERTEMUAN 4 — Ruang Vektor Riil $\mathbb{R}^n$, Subruang, Kombinasi Linier, & Rentang (*Span*) + Evaluasi Tugas 1
* **Kemampuan Akhir (`Sub-CPMK-2.1` [C4]):** Menganalisis struktur ruang vektor riil, menguji subruang vektor, serta menganalisis kombinasi linier dan rentang (*span*) pada $\mathbb{R}^n$, sekaligus menuntaskan evaluasi sumatif **Tugas 1 (20%)**.
* **Indikator Capaian:** (1) Membuktikan apakah suatu himpunan vektor merupakan subruang dari $\mathbb{R}^n$ menggunakan 3 syarat subruang (memuat $\mathbf{0}$, tertutup penjumlahan, tertutup perkalian skalar); (2) Menganalisis apakah suatu vektor $\mathbf{b}$ berada di dalam $\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ dan mendeskripsikan bentuk geometris ruang rentang tersebut.
* **Pokok Bahasan:** Aksioma Ruang Vektor, Kriteria Uji Subruang pada $\mathbb{R}^n$ (dan contoh himpunan yang gagal menjadi subruang), Kombinasi Linier, serta Ruang Rentang (*Span*).
* **Metode & Media:** *Geometric & Algebraic Discovery*; GeoGebra 3D Span Plane, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memverifikasi pengumpulan **Tugas 1 (20%)** di LMS Edlink dan mengadakan kuis verifikasi singkat 10 menit (1 soal eselon baris/determinan) di kelas. | Memastikan Tugas 1 terunggah dan menyelesaikan soal verifikasi individu. | 20' | LMS Edlink & Kertas Kuis |
| **Kegiatan Inti** | Memperkenalkan konsep ruang vektor dan cara cepat menguji subruang di $\mathbb{R}^n$ (mengapa bidang yang tidak melewati titik asal $(0,0,0)$ **bukan** subruang!); menghubungkan pertanyaan abstrak *"Apakah $\mathbf{w}$ kombinasi linier dari $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$?"* secara langsung ke pemeriksaan konsistensi SPL $[\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_3 \mid \mathbf{w}]$ yang sudah dikuasai di Pekan 2! | Menguji 5 kandidat himpunan bagian $\mathbb{R}^3$ (mana subruang vs bukan subruang beserta contoh penyangkalnya) dan menentukan syarat agar kumpulan vektor merentang seluruh $\mathbb{R}^3$. | 110' | `[1]` Bab 4.1–4.3, `[4]` Bab 2.4–2.5 |
| **Penutup** | Menyimpulkan jembatan antara bahasa SPL dan bahasa geometri ruang vektor, lalu mengantar konsep kebebasan linier Pekan 5. | Mencatat ringkasan uji subruang 3 langkah. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 10 soal pengujian subruang, kombinasi linier, dan *span* pada Bab 4 Modul Ajar.
* **Evaluasi Sumatif Pekan Ini:** **Tugas 1 (Bobot 20%)** dinilai menggunakan Rubrik Analitik Tugas 1 (`059_5`).

---

### PERTEMUAN 5 — Kebebasan Linier (*Linear Independence*), Basis, & Dimensi Ruang Vektor $\mathbb{R}^n$
* **Kemampuan Akhir (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]):** Menganalisis kebebasan linier himpunan vektor serta menentukan basis dan dimensi ruang vektor $\mathbb{R}^n$.
* **Indikator Capaian:** (1) Menguji secara formal kebebasan linier persamaan homogen $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{0}$ dan menafsirkan ketergantungan linier sebagai redundansi informasi; (2) Menentukan basis (merentang **dan** bebas linier) serta dimensi suatu ruang vektor/subruang pada $\mathbb{R}^n$.
* **Pokok Bahasan:** Kebebasan Linier vs Ketergantungan Linier, Fenomena *Multicollinearity* Fitur Data, Definisi Basis sebagai Kerangka Koordinat Minimal, Dimensi Ruang Vektor, dan Vektor Koordinat $[\mathbf{x}]_{\mathcal{B}}$.
* **Metode & Media:** *Problem-Solving Class*; Papan Tulis, Kasus Tabel Fitur Redundan, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membagikan umpan balik Tugas 1, lalu memperlihatkan tabel dataset properti yang memuat kolom `Luas_m2`, `Luas_sqft` ($= 10,764 \times \text{Luas\_m2}$), dan `Harga`: mengapa menyertakan kedua kolom luas tersebut membuat matriks fitur menjadi bergantung linier dan merusak perhitungan invers? | Menyadari makna praktis kebebasan linier dalam rekayasa fitur data (*feature engineering*). | 20' | Slide Kasus Kolom Redundan |
| **Kegiatan Inti** | Menguraikan prosedur uji kebebasan linier via SPL homogen, teorema bahwa lebih dari $n$ vektor di $\mathbb{R}^n$ pasti bergantung linier, cara memangkas himpunan perentang yang berlebih menjadi **Basis** (atau memperluas himpunan bebas linier menjadi basis $\mathbb{R}^n$), penentuan **Dimensi** sebagai kardinalitas basis, serta perhitungan koordinat vektor terhadap basis non-standar. | Kelompok menganalisis kebebasan linier berbagai himpunan vektor di $\mathbb{R}^3$ dan $\mathbb{R}^4$, mengekstrak basisnya, dan menghitung dimensi subruang yang dibentuk. | 110' | `[1]` Bab 4.4–4.6, `[4]` Bab 2.6 |
| **Penutup** | Merangkum dua syarat mutlak Basis (*Spanning* + *Linearly Independent*) dan mengantar Pekan 6 (Empat Subruang Fundamental Matriks). | Menyelesaikan kuis singkat 3 soal kebebasan linier dan dimensi di Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan mandiri 10 soal kebebasan linier, basis, dan dimensi pada $\mathbb{R}^n$.

---

### PERTEMUAN 6 — Ruang Baris, Ruang Kolom, Ruang Nol (*Null Space*), & Teorema Rank-Nullitas
* **Kemampuan Akhir (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]):** Menganalisis basis dan dimensi dari ruang baris, ruang kolom, dan ruang nol suatu matriks menggunakan kaidah aljabar formal.
* **Indikator Capaian:** (1) Menentukan basis untuk $\text{Row}(A)$ (baris tak-nol dari `RREF`), $\text{Col}(A)$ (**kolom-kolom asli matriks $A$** yang bersesuaian dengan kolom *pivot*!), dan $\text{Null}(A)$ (solusi umum $Ax=\mathbf{0}$); (2) Menghitung $\text{rank}(A)$ serta $\text{nullity}(A)$ dan memverifikasi $\text{rank}(A) + \text{nullity}(A) = n$.
* **Pokok Bahasan:** Ruang Baris, Ruang Kolom, & Ruang Nol Matriks $m\times n$, Kesamaan Dimensi Baris dan Kolom ($\text{rank}(A)$), serta Teorema Rank-Nullitas.
* **Metode & Media:** *Case-Based Data Rank Analysis*; Papan Tulis, Lembar Kerja Matriks $4\times 5$, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memperingatkan satu jebakan paling terkenal di aljabar linear: *"Mengapa kita tidak boleh mengambil kolom langsung dari matriks RREF sebagai basis Ruang Kolom, melainkan harus kembali mengambil kolom dari matriks asli $A$?"* | Membuktikan dengan contoh $2\times 2$ sederhana bahwa OBE mengubah ruang kolom meskipun mempertahankan hubungan ketergantungan antar-kolom. | 20' | Papan Tulis |
| **Kegiatan Inti** | Memandu prosedur terpadu satu kali reduksi `RREF` pada matriks $4\times 5$ untuk sekaligus mengekstrak: (a) basis & dimensi Ruang Baris, (b) basis & dimensi Ruang Kolom, (c) basis & dimensi Ruang Nol, dan (d) verifikasi $\text{rank}(A) + \text{nullity}(A) = 5$. Mengaitkan konsep *low-rank matrix* dengan kompresi pola pada tabel rekomendasi pengguna. | Kelompok membedah matriks berukuran $3\times 5$ dan $4\times 4$ hingga mendapatkan ketiga basis subruang secara lengkap dan akurat. | 110' | `[1]` Bab 4.7–4.8, `[2]` Bab 3 |
| **Penutup** | Merangkum cara cepat memeriksa kebenaran dimensi ketiga subruang melalui Teorema Rank-Nullitas. | Mengunggah lembar hasil analisis subruang kelompok ke Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 8 soal penentuan basis ruang baris/kolom/nol dan *rank* matriks.

---

### PERTEMUAN 7 — Ortogonalitas, Proyeksi Ortogonal, Proses *Gram-Schmidt*, & Review Pra-UTS
* **Kemampuan Akhir (`Sub-CPMK-2.2` [C3/C4]):** Menerapkan konsep ortogonalitas dan proses *Gram-Schmidt* untuk membentuk basis ortonormal pada $\mathbb{R}^n$, serta mengonsolidasikan materi `CPMK-2` menjelang UTS.
* **Indikator Capaian:** (1) Memeriksa keortogonalan himpunan vektor dan menghitung koordinat terhadap basis ortonormal dengan sangat mudah melalui *dot product* tanpa menyelesaikan SPL; (2) Menghitung proyeksi ortogonal vektor $\mathbf{y}$ pada subruang $W$ dan menerapkan algoritma **Gram-Schmidt** langkah demi langkah untuk menghasilkan basis ortonormal $\{\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3\}$.
* **Pokok Bahasan:** Keunggulan Basis Ortonormal, Proyeksi Ortogonal pada Garis & Subruang (Intuisi Geometri Pendekatan *Least Squares*), Algoritma Ortogonalisasi *Gram-Schmidt* (& pengantar $A=QR$), serta Klinik Persiapan UTS.
* **Metode & Media:** *Problem-Solving Workshop*; GeoGebra 3D Projection, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan betapa melelahkannya mencari koordinat vektor pada basis miring sembarang (harus Gauss-Jordan!) vs betapa mudahnya pada **basis ortonormal** (cukup $c_i = \mathbf{x}\cdot\mathbf{q}_i$!). Bagaimana mengubah basis miring apa pun menjadi tegak lurus satuan? | Memahami motivasi praktis mengapa basis ortonormal menjadi tulang punggung komputasi matriks stabil (termasuk matriks $Q$ pada diagonalisasi ortogonal & SVD nanti). | 20' | GeoGebra 3D & Papan |
| **Kegiatan Inti** | Bagian 1 (60'): Menurunkan rumus proyeksi ortogonal dan memandu eksekusi langkah demi langkah **Proses Gram-Schmidt** pada 3 vektor di $\mathbb{R}^3$ diikuti normalisasi panjang menjadi $1$. Bagian 2 (50'): Klinik bedah soal latihan simulasi komprehensif persiapan **UTS Pekan 8** (`Sub-CPMK-2.1` & `2.2`). | Menghitung basis ortonormal dari 3 vektor bebas linier, mengecek ulang bahwa $\mathbf{q}_i \cdot \mathbf{q}_j = 0$ untuk $i \neq j$ dan $\|\mathbf{q}_i\|=1$, lalu membahas soal simulasi UTS. | 110' | `[1]` Bab 6.1–6.3, `[4]` Bab 3.8 |
| **Penutup** | Membagikan kisi-kisi resmi, bobot soal, dan kriteria Rubrik Analitik **UTS Pekan 8 (Bobot 30%)**. | Mencatat kisi-kisi UTS dan menanyakan klarifikasi konsep ruang vektor yang belum mantap. | 20' | Kisi-Kisi UTS di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan mandiri paket simulasi soal UTS di LMS Edlink.

---

### PERTEMUAN 8 — EVALUASI TENGAH SEMESTER (UTS)
* **Kemampuan Akhir Diuji (`CPMK-2` [C4] & penguatan `CPMK-1`):** Menganalisis struktur ruang vektor, kombinasi linier, kebebasan linier, basis, dimensi, *rank-nullitas*, dan ortogonalisasi pada ruang $\mathbb{R}^n$ dengan kaidah aljabar formal.
* **Bentuk & Durasi:** Ujian Tertulis Analisis Ruang Vektor Terjadwal (*Closed-Book*), **150 menit**.
* **Bobot Penilaian Sumatif:** **30%** terhadap Nilai Akhir Mata Kuliah.

| Tahap | Aktivitas Pengawas / Dosen | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan daftar hadir berita acara UTS, pengaturan ruang kelas, pembacaan tata tertib kejujuran akademik, dan pembagian naskah soal UTS. | Menandatangani daftar hadir dan menyiapkan alat tulis. | 10' | Berita Acara & Naskah UTS |
| **Pelaksanaan Ujian** | Mengawasi pelaksanaan ujian secara tertib. | Mengerjakan 4 butir soal utama (uji subruang & *span*, kebebasan linier & ekstraksi basis, basis/dimensi ruang baris-kolom-nol & *rank-nullitas*, serta proyeksi ortogonal & *Gram-Schmidt*). | 135' | Lembar Jawaban UTS |
| **Pengumpulan** | Mengumpulkan dan memverifikasi kelengkapan berkas jawaban. | Menyerahkan lembar jawaban secara tertib. | 5' | Bundel Jawaban UTS |

---

### PERTEMUAN 9 — Matriks Transformasi Linier Geometri, Komposisi, Kernel, & *Range*
* **Kemampuan Akhir (`Sub-CPMK-3.2` [C3/C4]):** Menganalisis pemetaan/transformasi linier melalui matriks representasi standarnya beserta sifat geometri, kernel, dan jangkauannya.
* **Indikator Capaian:** (1) Menguji kelinearan fungsi $T: \mathbb{R}^n \to \mathbb{R}^m$ dan menyusun matriks standar $[T] = [T(\mathbf{e}_1)\ \dots\ T(\mathbf{e}_n)]$ untuk rotasi sudut $\theta$, refleksi, penskalaan, geseran (*shear*), dan proyeksi; (2) Menghitung matriks komposisi transformasi berurutan $[T_2 \circ T_1] = [T_2][T_1]$ dan menganalisis Kernel serta *Range*.
* **Pokok Bahasan:** Definisi Transformasi Linier, Cara Cepat Menyusun Matriks Standar dari Efek pada Basis $\mathbf{e}_1, \mathbf{e}_2$, Transformasi Geometri 2D/3D (Dasar Augmentasi Citra pada Visi Komputer), Perkalian Matriks sebagai Komposisi Transformasi, serta Kernel & *Range*.
* **Metode & Media:** *Visual Transformation Workshop*; Applet Interaktif Transformasi Kisi 2D, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membahas evaluasi umum UTS, lalu mendemonstrasikan bagaimana fitur memutar, mencerminkan, dan memiringkan foto pada pra-pemrosesan data pelatihan AI sesungguhnya hanyalah perkalian koordinat piksel dengan matriks $2\times 2$! | Menyimak umpan balik UTS dan mengamati pergerakan vektor basis $\mathbf{e}_1=(1,0)^T$ dan $\mathbf{e}_2=(0,1)^T$ pada layar. | 20' | Pembahasan UTS & Applet 2D |
| **Kegiatan Inti** | Membuktikan aturan emas bahwa kolom ke-$j$ matriks standar $[T]$ hanyalah bayangan vektor basis standar $T(\mathbf{e}_j)$! Melatih penyusunan matriks rotasi, refleksi, dan *shear*, membuktikan bahwa urutan komposisi tidak komutatif (rotasi lalu cermin $\neq$ cermin lalu rotasi!), serta menghubungkan $\ker(T)$ dengan $\text{Null}(A)$ dan $\text{Range}(T)$ dengan $\text{Col}(A)$. | Kelompok merancang matriks komposisi untuk memindahkan bangun datar ke posisi target dan menentukan apakah transformasi tersebut satu-ke-satu (*injective*) atau pada (*onto*). | 110' | `[1]` Bab 4.9–4.10 & 8.1–8.2, `[4]` Bab 2.7 |
| **Penutup** | Memantik pertanyaan kunci menuju Pekan 10: *"Saat seluruh bidang diputar/diregangkan oleh matriks $A$, adakah vektor istimewa yang arahnya TIDAK ikut berbelok, melainkan hanya memanjang/memendek sebesar $\lambda$ kali?"* | Menangkap intuisi lahirnya konsep Vektor Eigen ($A\mathbf{v}=\lambda\mathbf{v}$). | 20' | Slide Pengantar Eigen |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 10 soal penyusunan matriks transformasi linier, komposisi, dan kernel/*range* di Bab 8 Modul Ajar.

---

### PERTEMUAN 10 — Polinomial Karakteristik, Nilai Eigen (*Eigenvalues*), & Vektor Eigen (*Eigenvectors*)
* **Kemampuan Akhir (`Sub-CPMK-3.1` [C3]):** Menghitung nilai eigen dan vektor eigen suatu matriks bujursangkar secara presisi.
* **Indikator Capaian:** (1) Menurunkan persamaan karakteristik $\det(A - \lambda I) = 0$ (atau $\det(\lambda I - A) = 0$) dan menghitung seluruh akar nilai eigen $\lambda$ beserta cek konsistensi $\sum \lambda_i = \text{tr}(A)$ dan $\prod \lambda_i = \det(A)$; (2) Menyelesaikan ruang nol $(A - \lambda I)\mathbf{v} = \mathbf{0}$ untuk memperoleh basis vektor eigen tiap ruang eigen.
* **Pokok Bahasan:** Geometri Sumbu Invarian $A\mathbf{v} = \lambda\mathbf{v}$, Persamaan & Polinomial Karakteristik, Perhitungan Ruang Eigen, Multiplisitas Aljabar vs Multiplisitas Geometri, serta Nilai Eigen Matriks Segitiga & Perpangkatan.
* **Metode & Media:** *Problem-Solving Class*; Applet Visual Vektor Eigen 2D, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan animasi lingkaran penuh panah vektor yang dikenai matriks $A$: hampir semua panah berbelok arah, kecuali dua garis sumbu yang tetap lurus sejajar dirinya sendiri! | Mengidentifikasi secara visual sumbu vektor eigen dan faktor regangan nilai eigen $\lambda$. | 20' | Applet Vektor Eigen |
| **Kegiatan Inti** | Menurunkan syarat $(A - \lambda I)\mathbf{v} = \mathbf{0}$ punya solusi tak-nol $\iff \det(A - \lambda I) = 0$; melatih teknik pemfaktoran polinomial karakteristik derajat 2 dan derajat 3 (memanfaatkan operasi baris/kolom pada determinan agar mudah difaktorkan!), mencari basis ruang eigen dengan Gauss-Jordan, serta mengajarkan trik verifikasi cepat: jumlah seluruh nilai eigen **wajib sama dengan jejak (*trace*) diagonal matriks**, dan hasil kalinya **wajib sama dengan determinan**! | Menyelesaikan 6 soal perhitungan nilai eigen dan basis ruang eigen matriks $2\times 2$ dan $3\times 3$, selalu memverifikasi kebenaran $A\mathbf{v} = \lambda\mathbf{v}$ secara langsung. | 110' | `[1]` Bab 5.1, `[2]` Bab 6.1 |
| **Penutup** | Merangkum langkah baku pencarian eigen dan **merilis resmi naskah RTM-2 (Tugas 2 — Bobot 20%)** di LMS Edlink untuk dikumpulkan pada Pekan 12. | Mengunduh naskah studi kasus Tugas 2 di Edlink. | 20' | Dokumen RTM-2 di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mulai mengerjakan Bagian 1 & 2 laporan **Tugas 2** (matriks transformasi linier dan nilai/vektor eigen).

---

### PERTEMUAN 11 — Diagonalisasi Matriks ($A = PDP^{-1}$) & Aplikasi Transformasi Berulang / *Markov PageRank*
* **Kemampuan Akhir (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C3]):** Menghitung diagonalisasi matriks dan menerapkannya pada transformasi linier berulang serta analisis kondisi tunak rantai *Markov*.
* **Indikator Capaian:** (1) Menguji apakah matriks $n\times n$ dapat didiagonalisasi (memiliki $n$ vektor eigen bebas linier) dan mengonstruksi matriks $P$ serta matriks diagonal $D$ sehingga $A = PDP^{-1}$; (2) Menghitung perpangkatan tinggi $A^k = PD^kP^{-1}$ secara analitis dan menentukan vektor keadaan tunak (*steady-state* untuk $\lambda = 1$) pada matriks transisi *Markov / PageRank* sederhana.
* **Pokok Bahasan:** Syarat Keterdiagonalan (Multiplisitas Geometri = Multiplisitas Aljabar), Konstruksi $A = PDP^{-1}$, Rumus Cepat $A^k = PD^kP^{-1}$, dan Studi Kasus Rantai Transisi *Markov* / Prinsip Dasar *PageRank*.
* **Metode & Media:** *Case-Based Markov Modeling*; Studi Kasus Perpindahan Pelanggan 3 Layanan Digital, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengajukan tantangan komputasi: *"Jika kita harus menghitung $A^{100}$ untuk memprediksi pangsa pasar pengguna 100 pekan ke depan, mengalikan matriks 100 kali secara manual sangat melelahkan—bagaimana menyelesaikannya hanya dalam 3 langkah lewat diagonalisasi?"* | Melihat keajaiban penyederhanaan $(PDP^{-1})(PDP^{-1})\dots = PD^{100}P^{-1}$ di mana memangkatkan matriks diagonal $D$ hanyalah memangkatkan angka diagonalnya! | 20' | Papan Tulis |
| **Kegiatan Inti** | Melatih pengujian keterdiagonalan (termasuk contoh matriks geser *shear* yang **gagal** didiagonalisasi karena kekurangan vektor eigen!), konstruksi pasangan $(P, D)$ yang bersesuaian urutannya, perhitungan $A^k$, serta bedah studi kasus matriks stokastik *Markov* & graf mini 3 halaman web (*PageRank*) di mana pangsa jangka panjang merupakan vektor eigen ternormalisasi milik $\lambda = 1$. | Kelompok memodelkan matriks transisi perpindahan pengguna antar-platform, mendiagonalisasikannya, dan menentukan persentase pangsa pengguna kondisi tunak (*steady-state*). | 110' | `[1]` Bab 5.2 & 10.5, `[2]` Bab 6.2 & 10.3 |
| **Penutup** | Merangkum manfaat diagonalisasi dan mengantar kasus paling indah di aljabar linear pada Pekan 12: matriks simetris riil. | Melanjutkan pengerjaan Bagian 3 draf Tugas 2. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan Bagian 3 **Tugas 2** dan membaca materi diagonalisasi ortogonal matriks simetris untuk Pekan 12.

---

### PERTEMUAN 12 — Matriks Simetris Riil & Diagonalisasi Ortogonal ($A = Q\Lambda Q^T$) + Evaluasi Tugas 2
* **Kemampuan Akhir (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C3/C4]):** Menghitung diagonalisasi ortogonal matriks simetris riil sebagai jembatan langsung menuju SVD dan matriks kovarians PCA, serta menuntaskan evaluasi sumatif **Tugas 2 (20%)**.
* **Indikator Capaian:** (1) Memanfaatkan sifat Teorema Spektral bahwa matriks simetris riil ($A^T=A$) selalu dapat didiagonalisasi secara ortogonal dengan nilai eigen riil; (2) Mengonstruksi matriks ortogonal $Q$ (kolom-kolomnya vektor eigen satuan yang saling tegak lurus, sehingga $Q^{-1}=Q^T$ tanpa perlu menghitung invers!) untuk memfaktorkan $A = Q\Lambda Q^T = \sum \lambda_i \mathbf{q}_i\mathbf{q}_i^T$.
* **Pokok Bahasan:** Matriks Ortogonal ($Q^TQ=I$), Sifat Vektor Eigen Matriks Simetris, **Teorema Spektral**, Prosedur Diagonalisasi Ortogonal $A = Q\Lambda Q^T$, dan Sifat Matriks $A^TA$ yang Selalu Simetris Positif Semidefinit.
* **Metode & Media:** *Problem-Solving Class*; Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memverifikasi pengumpulan **Tugas 2 (20%)** di LMS Edlink dan mengadakan kuis verifikasi singkat 10 menit (1 soal eigen matriks $2\times 2$) di kelas. | Memastikan Tugas 2 terunggah dan mengerjakan soal verifikasi individu. | 20' | LMS Edlink & Kertas Kuis |
| **Kegiatan Inti** | Membuktikan mengapa pada matriks simetris $A^T=A$, dua vektor eigen dari nilai eigen berbeda **otomatis saling tegak lurus**, dan jika ada nilai eigen kembar kita cukup memakai *Gram-Schmidt* (Pekan 7) pada ruang eigennya! Melatih konstruksi $A = Q\Lambda Q^T$, lalu membuktikan fakta kunci pembuka Bagian IV: untuk matriks persegi panjang ukuran $m\times n$ apa pun, hasil kali **$A^TA$ selalu simetris dan positif semidefinit ($\lambda_i \ge 0$)**! | Menyelesaikan latihan diagonalisasi ortogonal matriks simetris $3\times 3$ (termasuk kasus nilai eigen kembar) dan memverifikasi $Q^TQ = I$ serta $Q\Lambda Q^T = A$. | 110' | `[1]` Bab 7.1–7.2, `[4]` Bab 4.4 |
| **Penutup** | Merangkum tuntas `CPMK-3` dan menunjukkan bahwa dengan menguasai $Q\Lambda Q^T$ pada $A^TA$ hari ini, mahasiswa sudah menggenggam 80% kunci rahasia **SVD** dan **PCA** pada Pekan 13–15! | Mencatat benang merah Teorema Spektral menuju SVD dan PCA. | 20' | Salindia Jembatan `CPMK-4` |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Membaca Bab 12 Modul Ajar tentang konstruksi analitis *Singular Value Decomposition* (SVD).
* **Evaluasi Sumatif Pekan Ini:** **Tugas 2 (Bobot 20%)** dinilai menggunakan Rubrik Analitik Tugas 2 (`059_5`).

---

### PERTEMUAN 13 — Formulasi Matematis *Singular Value Decomposition* (SVD) & Aproksimasi *Low-Rank*
* **Kemampuan Akhir (`Sub-CPMK-4.1` [C4]):** Merumuskan dekomposisi nilai singular ($A = U\Sigma V^T$) suatu matriks sembarang dan menganalisis aproksimasi matriks berperingkat rendah.
* **Indikator Capaian:** (1) Menghitung nilai eigen dari $A^TA$, mengambil nilai singular $\sigma_1 \ge \sigma_2 \ge \dots > 0$ ($\sigma_i = \sqrt{\lambda_i}$), menentukan vektor singular kanan $\mathbf{v}_i$ (ortonormal) dan vektor singular kiri $\mathbf{u}_i = \frac{1}{\sigma_i}A\mathbf{v}_i$ untuk menyusun faktorisasi lengkap $A = U\Sigma V^T$; (2) Merumuskan ekspansi *outer product* $A = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^T$ dan menghitung aproksimasi peringkat-$k$ terbaik $A_k$ untuk kompresi data/rekomendasi.
* **Pokok Bahasan:** Geometri SVD (Rotasi $V^T \to$ Regangan Sumbu $\Sigma \to$ Rotasi $U$), Prosedur Analitis 4 Langkah Menghitung SVD Matriks $m\times n$, Bentuk Penuh vs *Reduced SVD*, serta Teorema *Eckart-Young Low-Rank Approximation*.
* **Metode & Media:** *Case-Based SVD Workshop*; GeoGebra/Slide Visualisasi Kompresi Citra SVD, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membagikan umpan balik Tugas 2, lalu mendemonstrasikan sebuah foto hitam-putih $1000\times 1000$ piksel ($1.000.000$ angka) yang direkonstruksi hanya dari 20 nilai singular terbesarnya ($40.020$ angka — hemat $>95\%$!) namun wajah pada foto tetap terlihat tajam! | Mengamati kekuatan luar biasa representasi jumlahan suku $\sigma_i \mathbf{u}_i \mathbf{v}_i^T$ yang diurutkan menurut besarnya energi informasi $\sigma_i$. | 20' | Demo Visual Kompresi SVD |
| **Kegiatan Inti** | Menurunkan hubungan $A^TA = V(\Sigma^T\Sigma)V^T$ dan $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$, lalu menuntun seluruh kelas menghitung tangan dari awal sampai tuntas faktorisasi SVD untuk matriks tak bujursangkar $3\times 2$ dan $2\times 3$ (termasuk cara melengkapi kolom ortonormal terakhir $U$ atau $V$ jika $m \neq n$), diikuti perhitungan matriks hampiran *rank-1* $A_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T$ beserta besar galat Frobenius-nya. | Menghitung secara manual faktorisasi $A = U\Sigma V^T$ pada lembar kerja, mengalikan kembali $U\Sigma V^T$ untuk membuktikan hasilnya kembali tepat menjadi matriks $A$, dan menghitung hampiran *rank-1*. | 110' | `[2]` Bab 7, `[4]` Bab 4.5 |
| **Penutup** | Menyimpulkan mengapa Gilbert Strang menjuluki SVD sebagai puncak tertinggi (*the fundamental theorem/crown jewel*) dari seluruh mata kuliah Aljabar Linear. | Mengunggah lembar kerja perhitungan SVD kelas ke Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 6 soal dekomposisi SVD manual matriks $2\times 3$ / $3\times 2$ dan aproksimasi *rank-1*.

---

### PERTEMUAN 14 — Matematika Reduksi Dimensi *Principal Component Analysis* (PCA)
* **Kemampuan Akhir (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C4]):** Merumuskan prosedur matematis reduksi dimensi *Principal Component Analysis* (PCA) menggunakan matriks kovarians maupun SVD.
* **Indikator Capaian:** (1) Melakukan pemusatan rata-rata kolom (*mean-centering* $\tilde{X}$) pada matriks data $X \in \mathbb{R}^{n \times d}$ dan menghitung matriks kovarians $S = \frac{1}{n-1}\tilde{X}^T\tilde{X}$; (2) Menentukan komponen utama $\mathbf{w}_1, \dots, \mathbf{w}_k$ (vektor eigen satuan dari nilai eigen terbesar $S$, yang identik dengan kolom-kolom pertama $V$ pada SVD dari $\tilde{X}$!), menghitung koordinat berdimensi rendah $Z = \tilde{X}W_k$, merekonstruksi $\hat{X}$, dan menghitung *Explained Variance Ratio* $\frac{\lambda_j}{\sum \lambda_i}$.
* **Pokok Bahasan:** Masalah Kutukan Dimensi (*Curse of Dimensionality*) pada Data AI, *Mean-Centering*, Matriks Kovarians sebagai Ukuran Sebaran Bersama, Bukti Sumbu Variansi Maksimum = Vektor Eigen Utama, Jembatan SVD $\leftrightarrow$ PCA, dan Rasio Variansi Terjelaskan.
* **Metode & Media:** *Problem-Solving AI Math Class*; Grafik Awan Titik Data 2D & Sumbu PC1/PC2, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan tabel data pasien/pelanggan dengan 50 kolom fitur numerik: bagaimana memvisualisasikannya di layar datar 2D dengan kehilangan informasi (variansi) sekecil mungkin? | Mengamati secara geometris bahwa sumbu terbaik (PC1) adalah garis tempat bayangan proyeksi titik-titik data memiliki sebaran terlebar (dan jarak tegak lurus galat terkecil!). | 20' | Grafik Geometri PCA |
| **Kegiatan Inti** | Memandu penurunan matematis 5 langkah baku PCA: (1) Kurangi tiap kolom dengan rata-ratanya ($\tilde{X}$), (2) Hitung $S = \frac{1}{n-1}\tilde{X}^T\tilde{X}$, (3) Cari nilai eigen $\lambda_1 \ge \lambda_2 \dots$ dan vektor eigen ortonormal $\mathbf{w}_i$ (atau langsung ambil $V$ dan $\frac{\sigma_i^2}{n-1}$ dari SVD $\tilde{X} = U\Sigma V^T$!), (4) Proyeksikan $Z = \tilde{X}W_k$, dan (5) Hitung proporsi informasi $\frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^d \lambda_i}$. Seluruh kelas menghitung tangan reduksi dataset 4 titik 2D $\to$ 1D hingga tuntas. | Menghitung secara manual *mean-centering*, matriks kovarians $2\times 2$, PC1, skor proyeksi 1D ke-4 sampel data, dan persentase variansi yang berhasil dipertahankan (mis. $94\%$). | 110' | `[4]` Bab 10.1–10.4, `[6]` Bab 1.8 |
| **Penutup** | Merilis panduan pengerjaan *Mini-Computational Worksheet* `NumPy` (komponen 30% dari UAS) yang akan dikonsolidasikan pada klinik komputasi Pekan 15. | Mengunduh lembar kerja verifikasi `NumPy` di LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan perhitungan manual PCA dataset mini dan menyiapkan draf ekspresi matriks Python `NumPy`.

---

### PERTEMUAN 15 — Komputasi Matriks SVD & Reduksi Dimensi PCA dengan Python `NumPy` Murni + Review Pra-UAS
* **Kemampuan Akhir (`Sub-CPMK-4.2` [C4]):** Menerapkan formulasi SVD dan reduksi dimensi PCA menggunakan pustaka matriks dasar Python `NumPy` untuk pemrosesan data AI serta menyintesiskan seluruh `CPMK-1..4`.
* **Indikator Capaian:** (1) Menulis dan menelusuri operasi aljabar matriks ringkas di Python `NumPy` (`X_c = X - np.mean(X, axis=0)`, `U, S, Vt = np.linalg.svd(X_c, full_matrices=False)`, `W_k = Vt[:k].T`, `Z = X_c @ W_k`, `evr = (S**2) / np.sum(S**2)`) untuk mereduksi dimensi tabel fitur AI dan mengompresi matriks citra; (2) Memverifikasi kesesuaian 100% antara hasil hitungan kertas Pekan 13–14 dengan keluaran `NumPy` (termasuk memahami ambiguitas tanda $\pm$ pada arah vektor eigen/singular!).
* **Pokok Bahasan:** Pemetaan Notasi Aljabar Linear ke Operasi Array `NumPy` (`@`, `.T`, `np.linalg.solve`, `eigh`, `svd`, `norm`), Eksperimen Reduksi Fitur Data AI & Kompresi Matriks Citra **Murni dengan `NumPy` (Tanpa `scikit-learn`!)**, serta Klinik Sintesis Pra-UAS.
* **Metode & Media:** *Interactive NumPy Math Clinic*; Google Colab / JupyterLite di Peramban, Proyektor, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menegaskan filosofi akademik SISTEKIN: *"Di Semester 4 (`STI-413`) Anda akan memanggil pustaka ML siap pakai, tetapi seorang insinyur AI sejati mampu menulis sendiri mesin SVD & PCA hanya dalam 6 baris aljabar matriks `NumPy` karena memahami matematikanya!"* | Membuka lingkungan *notebook* peramban dan mencocokkan matriks latihan tangan Pekan 14 dengan hasil `NumPy`. | 20' | Google Colab / JupyterLite |
| **Kegiatan Inti** | Bagian 1 (65'): Membedah korespondensi baris demi baris antara rumus matematika buku teks dengan ekspresi vektorisasi `NumPy` (tanpa `for-loop` lambat dan **dilarang keras mengimpor `sklearn`** sesuai *guardrail*!), mendiskusikan mengapa `(-\mathbf{u}_i)(-\mathbf{v}_i)^T = \mathbf{u}_i\mathbf{v}_i^T$ (invariansi tanda vektor singular), serta mengamati kurva *scree plot* nilai singular pada matriks citra dan tabel fitur berdimensi-10. Bagian 2 (45'): Klinik review sintesis persiapan **UAS Pekan 16**. | Menjalankan dan memodifikasi perhitungan matriks `NumPy` untuk menentukan jumlah komponen minimum $k$ agar variansi terjelaskan mencapai $\ge 90\%$, serta membahas soal simulasi tertulis UAS. | 110' | `[4]` Bab 4 & 10, `[5]` |
| **Penutup** | Membagikan kisi-kisi resmi **UAS Pekan 16 (Bobot 30%)**, tenggat pengumpulan lampiran verifikasi `NumPy`, dan memandu pengisian survei refleksi ketercapaian `Sub-CPMK` di Edlink. | Mengisi kuesioner refleksi diri `STI-205` di Edlink dan mencatat kisi-kisi UAS. | 20' | Kisi-Kisi UAS & Survei Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Merampungkan *Mini-Worksheet* `NumPy` dan berlatih paket soal komprehensif pra-UAS pada Unit Evaluasi E2 Modul Ajar.

---

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **Kemampuan Akhir Diuji (`CPMK-4` [C4] & Sintesis Komprehensif `CPMK-1` s.d. `CPMK-4`):** Merumuskan dekomposisi matriks SVD dan reduksi dimensi PCA menggunakan pustaka Python `NumPy` untuk pemrosesan data AI secara matematis, presisi, dan terverifikasi.
* **Bentuk & Durasi:** Verifikasi *Mini-Worksheet* `NumPy` Pra-Ujian (30% UAS) + Ujian Tertulis Komprehensif Terjadwal di Kelas (*Closed-Book*, **150 menit**, 70% UAS).
* **Bobot Penilaian Sumatif:** **30%** terhadap Nilai Akhir Mata Kuliah.

| Tahap | Aktivitas Pengawas / Dosen | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan daftar hadir berita acara UAS, verifikasi status unggahan lembar `NumPy` di Edlink, pembacaan tata tertib, dan pembagian naskah soal tertulis UAS. | Menandatangani daftar hadir dan menyiapkan peralatan ujian. | 10' | Berita Acara & Naskah UAS |
| **Pelaksanaan Ujian** | Mengawasi jalannya ujian tertulis secara objektif dan tertib. | Menyelesaikan 3 kelompok soal komprehensif (perhitungan analitis SVD $A=U\Sigma V^T$ & hampiran *rank-1*, penurunan manual PCA dari *mean-centering* hingga proyeksi & *explained variance*, serta perumusan/penelusuran kode matriks `NumPy` dan sintesis lintas-materi aljabar linear). | 135' | Lembar Jawaban UAS |
| **Penutupan** | Mengumpulkan lembar jawaban, menutup rangkaian perkuliahan semester secara resmi, dan menginformasikan jadwal publikasi rincian nilai per CPMK di Edlink/SIAKAD. | Menyerahkan lembar jawaban dan mengakhiri perkuliahan semester. | 5' | Bundel Jawaban UAS |

---

## BAGIAN III — PROTOKOL PENGELOLAAN KELAS, ATURAN KOMPUTASI `NUMPY`, & PENJAGAAN GUARDRAIL

1. **Keseimbangan Tangan-dan-Komputasi (*Hand-First, NumPy-Verified*):** Sebagai mata kuliah **3 SKS Teori (`P=0`)** pada Klaster Sains Dasar (`K-1`), seluruh konsep pada Pekan 1–14 wajib dikuasai terlebih dahulu secara analitis di atas kertas pada matriks berukuran kecil ($2\times 2$ s.d. $4\times 4$). Penggunaan `NumPy` pada Pekan 15–16 berfungsi murni untuk membumikan perumusan SVD dan PCA pada matriks fitur data AI tanpa terjebak hitung aritmetika panjang.
2. **Penegakan Ketat Guardrail Anti-Overlap `STI-413`:** Pada setiap contoh maupun tugas `NumPy`, mahasiswa **hanya diizinkan memakai fungsi operasi matriks dan aljabar linear dasar (`numpy` & `numpy.linalg`)**; pemakaian pustaka *Machine Learning* tingkat tinggi (`scikit-learn`, `TensorFlow`, `PyTorch`) secara eksplisit dilarang dan diserahkan penuh ke `STI-413 Pembelajaran Mesin` (Semester 4) serta `STI-624 Pembelajaran Mendalam & Jaringan Saraf` (Semester 6).
