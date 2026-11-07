# 059_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-205 — ALJABAR LINEAR DAN MATRIKS (*Linear Algebra and Matrices*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI205`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` · `059_2_SAP_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` · Dok 007 §10 · Dok 043.

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Buku Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Aljabar Linear dan Matriks untuk Sistem Cerdas & Pemrosesan Data Kecerdasan Artifisial* |
| **Kode & Bobot MK** | `STI-205` · 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · Semester 2 · Prasyarat: `STI-102` |
| **CPL & BoK Didukung** | `CPL-05` (`P1` — Level *Introduce*) · `BK-IS10` (*Applied Mathematics and Logic*), `BK-IT02` (*Applied AI*) |
| **Target Tebal Naskah Utuh** | 14 Bab Materi Inti + 2 Unit Evaluasi Komprehensif ($\pm 190\text{–}225\text{ halaman}$ A4/B5 dilengkapi ilustrasi geometri vektor/transformasi dan cuplikan verifikasi `NumPy` di Bab 14) |
| **Anatomi Baku Setiap Bab** | (1) *Sub-CPMK & Indikator*; (2) *Motivasi Representasi Data AI/Sistem TI*; (3) *Uraian Teori, Intuisi Geometri, & Algoritma Aljabar*; (4) *Contoh Soal Bertingkat*; (5) *Kotak Kesalahan Umum & Boundary Guardrail*; (6) *Rangkuman Teorema Kunci*; (7) *Latihan Mandiri Berjenjang (10–14 Soal)*. |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen Terkait |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Vektor, Matriks, & Sistem Persamaan Linear** | **Bab 1** | Vektor di Ruang $\mathbb{R}^n$, *Cosine Similarity*, & Operasi Aljabar Matriks | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Eliminasi Gauss, Gauss-Jordan (`RREF`), & Tiga Jenis Solusi SPL | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | Tugas 1 (20%) |
| | **Bab 3** | Determinan, Matriks Invers ($A^{-1}$), & Syarat Invertibilitas SPL | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Struktur Ruang Vektor $\mathbb{R}^n$ & Ortogonalitas** | **Bab 4** | Ruang Vektor Riil $\mathbb{R}^n$, Subruang, Kombinasi Linier, & Rentang (*Span*) | Mg 4 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 5** | Kebebasan Linier (*Linear Independence*), Basis, & Dimensi Ruang Vektor | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | UTS (30%) |
| | **Bab 6** | Ruang Baris, Ruang Kolom, Ruang Nol, & Teorema Rank-Nullitas | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | UTS (30%) |
| | **Bab 7** | Ruang Hasilkali Dalam, Proyeksi Ortogonal, & Proses *Gram-Schmidt* | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Paket Latihan Analisis SPL & Ruang Vektor $\mathbb{R}^n$ (Persiapan UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Transformasi Linier, Eigen, & Diagonalisasi** | **Bab 8** | Pemetaan & Matriks Transformasi Linier Geometri, Kernel, serta *Range* | Mg 9 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 9** | Polinomial Karakteristik, Nilai Eigen, & Vektor Eigen | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 10** | Diagonalisasi Matriks ($A=PDP^{-1}$) & Rantai Transisi *Markov/PageRank* | Mg 11 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | Tugas 2 (20%) |
| | **Bab 11** | Matriks Simetris Riil & Diagonalisasi Ortogonal ($A=Q\Lambda Q^T$) | Mg 12 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Dekomposisi SVD & Reduksi Dimensi PCA (`NumPy`)** | **Bab 12** | Formulasi Matematis *Singular Value Decomposition* (SVD) & *Low-Rank* | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13** | Matematika *Principal Component Analysis* (PCA) Berbasis Kovarians & SVD | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 14** | Komputasi Matriks SVD & Reduksi Dimensi PCA dengan Python `NumPy` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Paket Sintesis Eigen, SVD, & PCA Komputasi `NumPy` (Persiapan UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2` & Sintesis* | *UAS (30%)* |

---

## 3. RINCIAN OUTLINE SUBSTANSI TIAP BAB

### BAGIAN I — VEKTOR, MATRIKS, DAN SISTEM PERSAMAAN LINEAR (`CPMK-1`)

#### BAB 1: Vektor di Ruang $\mathbb{R}^n$, *Cosine Similarity*, & Operasi Aljabar Matriks (Pekan 1)
* **Sub-CPMK:** `Sub-CPMK-1.1` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  1.1 Representasi Entitas Dunia Nyata (Dokumen, Transaksi, Citra Piksel) sebagai Vektor dan Matriks  
  1.2 Operasi Vektor di $\mathbb{R}^n$, *Dot Product*, Norma Euclidean $\|\mathbf{x}\|_2$, dan Jarak Antar-Vektor  
  1.3 Sudut Antar-Vektor dan Ukuran Kemiripan *Cosine Similarity* dalam Temu Balik Informasi & *Vector Embedding*  
  1.4 Jenis-Jenis Matriks, Penjumlahan, Perkalian Matriks $AB$ (Pandangan Baris, Kolom, & *Outer Product*), serta Transpos  
  1.5 Sifat Aljabar Matriks dan Jejak (*Trace*) Matriks Bujursangkar
* **Latihan Bab 1:** 12 soal perhitungan *cosine similarity* fitur dan operasi perkalian/transpos matriks.

#### BAB 2: Eliminasi Gauss, Gauss-Jordan (`RREF`), & Tiga Jenis Solusi SPL (Pekan 2)
* **Sub-CPMK:** `Sub-CPMK-1.1` & `Sub-CPMK-1.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  2.1 Sistem Persamaan Linear (SPL): Tafsir Perpotongan Hiperbidang vs Kombinasi Kolom  
  2.2 Matriks *Augmented* $[A \mid \mathbf{b}]$ dan Tiga Operasi Baris Elementer (OBE)  
  2.3 Bentuk Eselon Baris (`REF` — Eliminasi Gauss) dan Eselon Baris Tereduksi (`RREF` — Eliminasi Gauss-Jordan)  
  2.4 Analisis *Pivot* dan Klasifikasi Lengkap 3 Kemungkinan Solusi SPL (Solusi Tunggal, Tak Hingga Solusi Berparameter, atau Tak Konsisten)  
  2.5 Pemodelan Keseimbangan Aliran Jaringan (*Network Flow*) dan Alokasi Sumber Daya dengan SPL
* **Latihan Bab 2:** 12 soal eliminasi Gauss-Jordan dan analisis nilai parameter $k$ pada SPL.

#### BAB 3: Determinan, Matriks Invers ($A^{-1}$), & Syarat Invertibilitas SPL (Pekan 3)
* **Sub-CPMK:** `Sub-CPMK-1.1` & `Sub-CPMK-1.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  3.1 Determinan Orde $2\times 2, 3\times 3,$ dan $n\times n$ melalui Ekspansi Kofaktor serta Reduksi Baris Segitiga  
  3.2 Sifat-Sifat Determinan ($\det(AB)=\det(A)\det(B)$, Efek OBE) dan Tafsir Geometri Skala Volume  
  3.3 Matriks Balikan (*Inverse* $A^{-1}$): Rumus Adjoin dan Algoritma Gauss-Jordan $[A \mid I] \to [I \mid A^{-1}]$  
  3.4 Penyelesaian SPL $x = A^{-1}b$, Aturan Cramer Pengantar, dan **Teorema Ekuivalensi Matriks Invertibel**
* **Latihan Bab 3 & Panduan Tugas 1:** 12 soal determinan, invers, dan penyelesaian SPL + panduan **RTM-1 (Tugas 1)**.

---

### BAGIAN II — STRUKTUR RUANG VEKTOR $\mathbb{R}^n$ DAN ORTOGONALITAS (`CPMK-2`)

#### BAB 4: Ruang Vektor Riil $\mathbb{R}^n$, Subruang, Kombinasi Linier, & Rentang (*Span*) (Pekan 4)
* **Sub-CPMK:** `Sub-CPMK-2.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  4.1 Pengertian Ruang Vektor Riil dan Ruang Euclides $\mathbb{R}^n$  
  4.2 Subruang Vektor: Tiga Syarat Penutupan dan Geometri Subruang pada $\mathbb{R}^2$ serta $\mathbb{R}^3$  
  4.3 Kombinasi Linier Vektor dan Keterkaitannya dengan Konsistensi SPL  
  4.4 Himpunan Merentang (*Spanning Set*) dan Ruang Rentang $\text{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$
* **Latihan Bab 4:** 10 soal pembuktian/penyangkalan subruang dan pengujian kombinasi linier/*span*.

#### BAB 5: Kebebasan Linier (*Linear Independence*), Basis, & Dimensi Ruang Vektor (Pekan 5)
* **Sub-CPMK:** `Sub-CPMK-2.1` & `Sub-CPMK-2.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  5.1 Definisi Formal Kebebasan Linier vs Ketergantungan Linier melalui Persamaan Homogen  
  5.2 Makna Ketergantungan Linier pada Tabel Data: Masalah Kolom Fitur Kolinear (*Multicollinearity*)  
  5.3 Pengertian **Basis** sebagai Himpunan Merentang Minimal yang Bebas Linier  
  5.4 **Dimensi** Ruang Vektor/Subruang dan Teorema Pemangkasan/Perluasan Basis pada $\mathbb{R}^n$  
  5.5 Vektor Koordinat $[\mathbf{x}]_{\mathcal{B}}$ dan Matriks Perubahan Basis
* **Latihan Bab 5:** 12 soal uji kebebasan linier, konstruksi basis, dan perhitungan dimensi.

#### BAB 6: Ruang Baris, Ruang Kolom, Ruang Nol, & Teorema Rank-Nullitas (Pekan 6)
* **Sub-CPMK:** `Sub-CPMK-2.1` & `Sub-CPMK-2.2` (C4) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  6.1 Empat Subruang Fundamental Suatu Matriks $A \in \mathbb{R}^{m \times n}$  
  6.2 Prosedur Penentuan Basis Ruang Baris, Ruang Kolom (Aturan Kolom *Pivot* Matriks Asli!), dan Ruang Nol (*Null Space*)  
  6.3 Kesamaan Dimensi Ruang Baris & Kolom (**Rank** Matriks) serta Makna Matriks *Full-Rank* vs *Rank-Deficient*  
  6.4 **Teorema Rank-Nullitas** ($\text{rank}(A) + \text{nullity}(A) = n$) dan Implikasinya pada Sistem Persamaan Linear
* **Latihan Bab 6:** 10 soal penentuan basis ke-3 subruang dan analisis *rank-nullity*.

#### BAB 7: Ruang Hasilkali Dalam, Proyeksi Ortogonal, & Proses *Gram-Schmidt* (Pekan 7)
* **Sub-CPMK:** `Sub-CPMK-2.2` (C3/C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  7.1 Ortogonalitas Vektor, Komplemen Ortogonal, dan Keistimewaan Basis Ortonormal  
  7.2 Proyeksi Ortogonal Vektor pada Garis dan Subruang $W$  
  7.3 Intuisi Geometri Aproksimasi Terdekat (*Least Squares* $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$) tanpa Kalkulus Turunan  
  7.4 Algoritma Ortogonalisasi **Gram-Schmidt** dan Pengantar Faktorisasi Matriks $A = QR$
* **Latihan Bab 7 & Unit Evaluasi E1:** 10 soal proyeksi ortogonal & *Gram-Schmidt* + **Paket Simulasi Lengkap UTS (`CPMK-2`)**.

---

### BAGIAN III — TRANSFORMASI LINIER, NILAI EIGEN, DAN DIAGONALISASI (`CPMK-3`)

#### BAB 8: Pemetaan & Matriks Transformasi Linier Geometri, Kernel, serta *Range* (Pekan 9)
* **Sub-CPMK:** `Sub-CPMK-3.2` (C3/C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  8.1 Definisi dan Sifat Pemetaan/Transformasi Linier $T: \mathbb{R}^n \to \mathbb{R}^m$  
  8.2 Menyusun Matriks Standar $[T]$ dari Bayangan Vektor Basis Standar  
  8.3 Transformasi Geometri pada Bidang & Ruang: Rotasi, Refleksi, Dilatasi/Skala, Geseran (*Shear*), dan Proyeksi  
  8.4 Komposisi Transformasi Linier (Perkalian Matriks) pada Grafika & Pra-pemrosesan Citra  
  8.5 Kernel (Inti) dan *Range* (Jangkauan) Transformasi Linier
* **Latihan Bab 8:** 10 soal konstruksi matriks komposisi transformasi geometri dan penentuan kernel/*range*.

#### BAB 9: Polinomial Karakteristik, Nilai Eigen, & Vektor Eigen (Pekan 10)
* **Sub-CPMK:** `Sub-CPMK-3.1` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  9.1 Masalah Nilai Eigen $A\mathbf{v} = \lambda\mathbf{v}$ dan Tafsir Geometri Sumbu Regangan Invarian  
  9.2 Persamaan Karakteristik $\det(A - \lambda I) = 0$ dan Pencarian Akar Polinomial Karakteristik  
  9.3 Penentuan Basis Ruang Eigen $E_\lambda = \text{Null}(A - \lambda I)$  
  9.4 Hubungan Nilai Eigen dengan Jejak ($\text{tr}(A) = \sum \lambda_i$), Determinan ($\det(A) = \prod \lambda_i$), dan Matriks Segitiga/Invers
* **Latihan Bab 9:** 12 soal perhitungan nilai eigen dan basis ruang eigen matriks $2\times 2$ dan $3\times 3$.

#### BAB 10: Diagonalisasi Matriks ($A=PDP^{-1}$) & Rantai Transisi *Markov/PageRank* (Pekan 11)
* **Sub-CPMK:** `Sub-CPMK-3.1` & `Sub-CPMK-3.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  10.1 Kemiripan Matriks (*Matrix Similarity*) dan Kriteria Keterdiagonalan (Multiplisitas Aljabar vs Geometri)  
  10.2 Prosedur Langkah demi Langkah Diagonalisasi $A = PDP^{-1}$  
  10.3 Komputasi Analitis Perpangkatan Matriks $A^k = PD^kP^{-1}$  
  10.4 Studi Kasus Sistem Informasi: Matriks Stokastik Rantai *Markov* dan Vektor Eigen Utama $\lambda=1$ pada Algoritma Pemeringkatan Web (*PageRank*)
* **Latihan Bab 10:** 10 soal uji keterdiagonalan, perhitungan $A^k$, dan distribusi tunak rantai *Markov*.

#### BAB 11: Matriks Simetris Riil & Diagonalisasi Ortogonal ($A=Q\Lambda Q^T$) (Pekan 12)
* **Sub-CPMK:** `Sub-CPMK-3.1` & `Sub-CPMK-3.2` (C3/C4) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  11.1 Matriks Ortogonal ($Q^TQ = I \iff Q^{-1} = Q^T$) dan Pelestarian Panjang/Sudut Vektor  
  11.2 Sifat Istimewa Matriks Simetris Riil ($A^T=A$): Nilai Eigen Selalu Riil & Ruang Eigen Saling Tegak Lurus  
  11.3 **Teorema Spektral** dan Prosedur Diagonalisasi Ortogonal $A = Q\Lambda Q^T = \sum_{i=1}^n \lambda_i \mathbf{q}_i\mathbf{q}_i^T$  
  11.4 Matriks Positif Definit / Positif Semidefinit ($A^TA$) sebagai Pintu Masuk Dekomposisi SVD & Kovarians
* **Latihan Bab 11 & Panduan Tugas 2:** 10 soal diagonalisasi ortogonal + panduan finalisasi **RTM-2 (Tugas 2)**.

---

### BAGIAN IV — DEKOMPOSISI SVD DAN REDUKSI DIMENSI PCA DENGAN `NUMPY` (`CPMK-4`)

#### BAB 12: Formulasi Matematis *Singular Value Decomposition* (SVD) & *Low-Rank* (Pekan 13)
* **Sub-CPMK:** `Sub-CPMK-4.1` (C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  12.1 Mengapa Kita Membutuhkan Dekomposisi yang Berlaku untuk **Semua** Matriks $m\times n$?  
  12.2 Teorema dan Geometri **SVD** ($A = U\Sigma V^T$): Vektor Singular Kanan ($V$), Nilai Singular ($\sigma_i = \sqrt{\lambda_i(A^TA)}$), dan Vektor Singular Kiri ($U$)  
  12.3 Algoritma Analitis Menghitung *Full SVD* dan *Reduced/Compact SVD* di Atas Kertas  
  12.4 Ekspansi Jumlahan *Rank-1* ($A = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^T$), Norma Frobenius, dan **Teorema Aproksimasi Peringkat-$k$ Terbaik Eckart-Young**  
  12.5 Konteks Aplikasi Sistem Cerdas: Kompresi Matriks Citra dan Konsep Dasar Faktorisasi Matriks Sistem Rekomendasi
* **Latihan Bab 12:** 10 soal perhitungan SVD manual matriks persegi panjang dan hampiran *low-rank*.

#### BAB 13: Matematika *Principal Component Analysis* (PCA) Berbasis Kovarians & SVD (Pekan 14)
* **Sub-CPMK:** `Sub-CPMK-4.1` & `Sub-CPMK-4.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  13.1 Representasi Matriks Fitur Data $X \in \mathbb{R}^{n \times d}$ dan Tantangan Dimensi Tinggi  
  13.2 Pemusatan Rata-Rata Kolom (*Mean-Centering* $\tilde{X}$) dan Konstruksi Matriks Kovarians Sampel $S = \frac{1}{n-1}\tilde{X}^T\tilde{X}$  
  13.3 Penurunan Komponen Utama (*Principal Components*) sebagai Vektor Eigen Ortogonal Terbesar dari $S$  
  13.4 Koneksi Langsung SVD dengan PCA: Mengapa Komputasi Modern Menghitung PCA lewat SVD atas $\tilde{X}$ ($\lambda_i = \frac{\sigma_i^2}{n-1}$)  
  13.5 Proyeksi Reduksi Dimensi ($Z = \tilde{X}W_k$), Rekonstruksi Hampiran ($\hat{X}$), dan Perhitungan *Explained Variance Ratio*
* **Latihan Bab 13:** 8 soal perhitungan tangan lengkap PCA dari *mean-centering* hingga rasio variansi terjelaskan.

#### BAB 14: Komputasi Matriks SVD & Reduksi Dimensi PCA dengan Python `NumPy` (Pekan 15)
* **Sub-CPMK:** `Sub-CPMK-4.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  14.1 Pemetaan 1-ke-1 Notasi Aljabar Linear ke Array `NumPy` (`ndarray`, `@`, `.T`, *broadcasting* pengurangan vektor rata-rata)  
  14.2 Primitif `numpy.linalg` untuk Aljabar Linear (`solve`, `det`, `inv`, `matrix_rank`, `eigh`, dan `svd`)  
  14.3 Merakit Fungsi **SVD Low-Rank Matrix/Image Approximation** Murni dalam 5 Baris `NumPy`  
  14.4 Merakit Fungsi **PCA Dimensionality Reduction** Murni dalam 6 Baris `NumPy` & Memverifikasi Hasil Hitungan Kertas Bab 13  
  14.5 Peta *Handoff* Aljabar Linear menuju `STI-413 Pembelajaran Mesin` dan `STI-624 Pembelajaran Mendalam & Jaringan Saraf`
* **Guardrail Bab 14:** Seluruh kode contoh **wajib murni memakai `import numpy as np`**; dilarang keras memakai `sklearn.decomposition.PCA` atau melatih model klasifikasi/regresi `scikit-learn` (ranah `STI-413`).
* **Latihan Bab 14 & Unit Evaluasi E2:** 8 soal penelusuran/implementasi ekspresi matriks `NumPy` + **Paket Simulasi Lengkap UAS (`CPMK-4` & Sintesis)**.
