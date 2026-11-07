# 059_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-205 — ALJABAR LINEAR DAN MATRIKS (*Linear Algebra and Matrices*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI205`  
**Klaster Asesmen MK (Dok 018):** Klaster 1 (`K-1`) — Sains Dasar & Teori Formal  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** Panduan KPT 2024 Dikti (Tabel 16–21, Tabel 26, & Lampiran RTM) · Dok 004 · Dok 007 §10 · Dok 008 (Formula CPL Attainment & Skema 4x Evaluasi) · Dok 018 · Dok 041 Lampiran 23 · `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`.

---

## 1. ARSITEKTUR PENILAIAN KLASTER SAINS DASAR (`K-1`) & KEPATUHAN IKU 7

Mata kuliah `STI-205 Aljabar Linear dan Matriks` (3 SKS Teori) termasuk dalam **Klaster 1 (`K-1`)** dengan seluruh bobot penilaian mendukung **`CPL-05` (`P1`)** pada level *Introduce* (`I`):
* **Pemetaan 1-ke-1 Instrumen ke CPMK:** `Tugas 1 (20%) → CPMK-1`, `UTS (30%) → CPMK-2`, `Tugas 2 (20%) → CPMK-3`, dan `UAS (30%) → CPMK-4`.
* **Verifikasi Kepatuhan IKU 7 (*Case-Based / Problem-Solving Method* $\ge 50\%$):** Komponen evaluasi berbasis pemecahan kasus & pemodelan terapan mencakup **Tugas 1 (20% — *Network Flow SPL & Vector Similarity Case*), Tugas 2 (20% — *Geometric Transformation & Markov/PageRank Eigen Case*), dan UAS (30% — *SVD Matrix Compression & NumPy PCA Dimensionality Reduction Case*) = 70%**, melampaui standar minimal nasional IKU 7 (**50%**).

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (STANDAR KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat Evaluasi | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-05`**<br>(`P1`)<br>*Level: I* | **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | Penugasan terstruktur: Penyelesaian SPL via eliminasi Gauss-Jordan & matriks invers + kuis konfirmasi 10' | **RTM-1 (Tugas 1)** (Masalah 1, 2, 4) + Rubrik Analitik Tugas 1 | Sumatif | 12% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Penugasan terstruktur: Penentuan jenis solusi SPL berparameter dari bentuk eselon baris | **RTM-1 (Tugas 1)** (Masalah 2, 3) + Rubrik Analitik Tugas 1 | Sumatif | 8% | |
| **`CPL-05`**<br>(`P1`)<br>*Level: I* | **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.1` | Mg 8 | Tes tertulis terjadwal: Uji subruang, kombinasi linier, *span*, & kebebasan linier | **Naskah Soal UTS** (Soal 1 & 2) + Rubrik Analitik UTS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Tes tertulis terjadwal: Penentuan basis, dimensi, *rank-nullity*, & *Gram-Schmidt* pada $\mathbb{R}^n$ | **Naskah Soal UTS** (Soal 2, 3, & 4) + Rubrik Analitik UTS | Sumatif | 15% | |
| **`CPL-05`**<br>(`P1`)<br>*Level: I* | **`CPMK-3`**<br>(C3) | `Sub-CPMK-3.1` | Mg 12 | Penugasan studi masalah: Perhitungan nilai eigen, vektor eigen, & diagonalisasi ($PDP^{-1}$ & $Q\Lambda Q^T$) | **RTM-2 (Tugas 2)** (Masalah 2, 3, 4) + Rubrik Analitik Tugas 2 | Sumatif | 11% | **20%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Penugasan studi kasus: Matriks transformasi linier & aplikasi diagonalisasi rantai *Markov/PageRank* | **RTM-2 (Tugas 2)** (Masalah 1 & 3) + Rubrik Analitik Tugas 2 | Sumatif | 9% | |
| **`CPL-05`**<br>(`P1`)<br>*Level: I* | **`CPMK-4`**<br>(C4) | `Sub-CPMK-4.1` | Mg 16 | Evaluasi terpadu UAS: Perumusan analitis faktorisasi SVD ($A=U\Sigma V^T$) & *low-rank approximation* | **Naskah Soal UAS** (Soal 1) & bagian SVD *Mini-Worksheet* + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Evaluasi terpadu UAS: Penurunan matematis PCA & implementasi/penelusuran matriks Python `NumPy` | **Naskah Soal UAS** (Soal 2 & 3) + *Mini-Worksheet* `NumPy` + Rubrik UAS | Sumatif | 15% | |
| — | *Seluruh CPMK* | *Seluruh Sub-CPMK* | Mg 1–3, 5–7, 9–11, 13–15 | Latihan papan tulis, kuis Edlink, visualisasi transformasi 2D/3D, klinik *notebook* `NumPy` | Umpan balik langkah pengerjaan | Formatif *(Non-Graded)* | 0% | **0%** |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (1-to-1 CPMK)** | **4 Paket Instrumen Lengkap** | **Sumatif + Formatif** | **100%** | **100%** |

---

## 3. KISI-KISI INSTRUMEN EVALUASI (*ASSESSMENT BLUEPRINT*)

| Titik Evaluasi | Pekan | Durasi / Format | Sub-CPMK Diuji | Level Bloom | Rincian Butir / Bagian Penilaian | Bobot Internal | Bobot MK |
|---|:---:|---|---|:---:|---|:---:|:---:|
| **1. Tugas 1** | Mg 4 | Penugasan Mandiri Berparameter NIM (1 pekan) + Kuis Konfirmasi 10' | `Sub-CPMK-1.1`<br>`Sub-CPMK-1.2` | C3 | • Masalah 1: Perhitungan *dot product*, norma, & *cosine similarity* vektor fitur<br>• Masalah 2: Pemodelan arus jaringan ke SPL & penyelesaian **Eliminasi Gauss-Jordan (`RREF`)**<br>• Masalah 3: Analisis nilai parameter $k$ untuk 3 jenis solusi SPL (tunggal, $\infty$, tak ada)<br>• Masalah 4: Determinan, matriks invers $A^{-1}$ ($3\times 3$), & penyelesaian $x = A^{-1}b$ | 15%<br>30%<br>25%<br>30% | **20%** |
| **2. UTS** | Mg 8 | Ujian Tertulis Luring Terjadwal (*Closed-Book*, 150 menit) | `Sub-CPMK-2.1`<br>`Sub-CPMK-2.2` | C4 | • Soal 1: Pembuktian formal syarat subruang vektor & analisis kombinasi linier/*span*<br>• Soal 2: Pengujian kebebasan linier & ekstraksi basis ruang vektor pada $\mathbb{R}^n$<br>• Soal 3: Basis & dimensi Ruang Baris, Ruang Kolom, Ruang Nol, & Teorema Rank-Nullitas<br>• Soal 4: Proyeksi ortogonal & konstruksi basis ortonormal dengan **Gram-Schmidt** | 25%<br>25%<br>25%<br>25% | **30%** |
| **3. Tugas 2** | Mg 12 | Penugasan Studi Kasus Mandiri Berparameter NIM (2 pekan) + Kuis Konfirmasi 10' | `Sub-CPMK-3.1`<br>`Sub-CPMK-3.2` | C3 | • Masalah 1: Matriks komposisi transformasi geometri 2D & penentuan kernel/*range*<br>• Masalah 2: Polinomial karakteristik, nilai eigen, & basis ruang eigen matriks $3\times 3$<br>• Masalah 3: Diagonalisasi $A=PDP^{-1}$, rumus $A^k$, & keadaan tunak rantai *Markov/PageRank*<br>• Masalah 4: Diagonalisasi ortogonal matriks simetris riil $A=Q\Lambda Q^T$ | 20%<br>25%<br>30%<br>25% | **20%** |
| **4. UAS** | Mg 16 | *Mini-Worksheet* `NumPy` Terverifikasi (30% UAS) + Ujian Tertulis Luring (150', 70% UAS) | `Sub-CPMK-4.1`<br>`Sub-CPMK-4.2`<br>*(+ Sintesis)* | C4 | • Komponen `NumPy` (30%): Implementasi murni `numpy.linalg` untuk kompresi matriks SVD & reduksi fitur PCA $d \to 2$ (tanpa `scikit-learn`)<br>• Soal Ujian 1 (25%): Perhitungan analitis faktorisasi **SVD ($A=U\Sigma V^T$)** & hampiran *rank-1*<br>• Soal Ujian 2 (25%): Penurunan tangan lengkap **PCA** (*mean-centering*, kovarians $S$, proyeksi, *explained variance*)<br>• Soal Ujian 3 (20%): Perumusan/penelusuran ekspresi matriks `NumPy` & sintesis *rank*–eigen–singular | 30%<br><br>25%<br>25%<br>20% | **30%** |

---

## 4. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN (STANDAR KPT 2024 LAMPIRAN 23)

### 4.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Kode / SKS** | Aljabar Linear dan Matriks / `STI-205` / 3 SKS Teori |
| **Minggu Rilis & Batas Kumpul** | Dirilis: **Pekan 3** · Batas Pengumpulan: **Pekan 4** (melalui LMS Edlink + kuis konfirmasi 10 menit di kelas) |
| **Bobot Penilaian** | **20%** dari Nilai Akhir Mata Kuliah |
| **CPMK & Sub-CPMK Tujuan** | **`CPMK-1`** (`Sub-CPMK-1.1` & `Sub-CPMK-1.2`): Menyelesaikan Sistem Persamaan Linear (SPL) menggunakan eliminasi Gauss-Jordan dan matriks invers serta menentukan jenis solusi SPL dari bentuk eselon baris secara tepat. |
| **1. Tujuan Tugas** | Menguji ketelitian algoritmis mahasiswa dalam mengeksekusi Operasi Baris Elementer (OBE), menentukan matriks invers, dan menganalisis struktur solusi SPL pada konteks jaringan dan vektor fitur. |
| **2. Objek Garapan** | Empat masalah aljabar matriks terstruktur (Bab 1–3) dengan konstanta ruas kanan/elemen diagonal yang diparameterisasi menurut 2 digit terakhir NIM mahasiswa. |
| **3. Batasan yang Harus Dikerjakan** | 1. Setiap langkah Operasi Baris Elementer wajib menuliskan notasi operasi baris secara eksplisit (contoh: $R_2 \leftarrow R_2 - 3R_1$, $R_1 \leftrightarrow R_3$).<br>2. Pada soal SPL berparameter $k$, wajib menuliskan syarat aljabar eksplisit nilai $k$ untuk ketiga rezim solusi (tunggal, tak hingga banyak solusi, dan tak konsisten).<br>3. Pada soal matriks invers $3\times 3$, wajib menyertakan pemeriksaan perkalian balik $AA^{-1} = I$ dan $Ax = b$. |
| **4. Metode / Cara Pengerjaan** | Dikerjakan **secara individu** (tulisan tangan rapi terbaca jelas dipindai ke `.pdf` atau ketik $\LaTeX$ / *Equation Editor*). |
| **5. Deskripsi Luaran Tugas** | Berkas tunggal `STI205_T1_[NIM]_[Nama].pdf` berisi langkah pengerjaan lengkap Masalah 1–4 dan pernyataan kejujuran akademik. |
| **6. Kriteria & Bobot Penilaian** | Dinilai dengan **Rubrik Analitik Tugas 1 (`059_5`)**: (1) Ketepatan pemodelan SPL & analisis 3 jenis solusi eselon baris (35%); (2) Keruntutan notasi & langkah OBE Gauss-Jordan serta invers (40%); (3) Presisi hasil akhir & cek substitusi balik (25%). |

---

### 4.2 Spesifikasi Instrumen Ujian Tengah Semester (UTS — Pekan 8)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Bentuk & Durasi Ujian** | Ujian Tertulis Luring Terjadwal (*Closed-Book*), durasi **150 menit**. |
| **Bobot & Target Capaian** | **30%** dari Nilai Akhir · Mengukur **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]). |
| **Rincian 4 Butir Soal** | 1. **(25% — `Sub-CPMK-2.1`)** Uji secara formal dengan 3 kriteria subruang apakah dua himpunan bagian dari $\mathbb{R}^3$ merupakan subruang vektor, serta periksa apakah suatu vektor target berada pada $\text{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$.<br>2. **(25% — `Sub-CPMK-2.1 & 2.2`)** Diberikan 4 vektor kolom fitur di $\mathbb{R}^4$: uji kebebasan liniernya, tentukan hubungan ketergantungan linier antar-vektor (jika ada), dan tentukan basis beserta dimensi ruang yang direntangnya.<br>3. **(25% — `Sub-CPMK-2.2`)** Diberikan matriks $A$ berukuran $4\times 5$: tentukan basis dan dimensi dari $\text{Row}(A)$, $\text{Col}(A)$, dan $\text{Null}(A)$, serta tunjukkan berlakunya Teorema Rank-Nullitas.<br>4. **(25% — `Sub-CPMK-2.2`)** Terapkan proses **Gram-Schmidt** untuk mengubah basis $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ di $\mathbb{R}^3$ menjadi basis ortonormal $\{\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3\}$ dan hitung proyeksi ortogonal suatu vektor $\mathbf{y}$ ke subruang $\text{Span}\{\mathbf{q}_1, \mathbf{q}_2\}$. |

---

### 4.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Kode / SKS** | Aljabar Linear dan Matriks / `STI-205` / 3 SKS Teori |
| **Minggu Rilis & Batas Kumpul** | Dirilis: **Pekan 10** · Batas Pengumpulan: **Pekan 12** (melalui LMS Edlink + kuis konfirmasi 10 menit di kelas) |
| **Bobot Penilaian** | **20%** dari Nilai Akhir Mata Kuliah |
| **CPMK & Sub-CPMK Tujuan** | **`CPMK-3`** (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C3]): Menghitung nilai eigen, vektor eigen, dan diagonalisasi matriks serta menerapkannya pada matriks transformasi linier secara presisi. |
| **1. Tujuan Tugas** | Melatih ketepatan perhitungan spektral matriks (nilai eigen, vektor eigen, diagonalisasi biasa, dan diagonalisasi ortogonal) serta penerapannya pada geometri transformasi dan dinamika rantai *Markov*. |
| **2. Objek Garapan** | Empat studi masalah terapan (Bab 8–11) dengan elemen matriks berparameter NIM. |
| **3. Batasan yang Harus Dikerjakan** | 1. **Masalah 1:** Menyusun matriks tunggal komposisi 3 transformasi geometri berurutan pada $\mathbb{R}^2$, menghitung bayangan titik sudut poligon, dan menentukan kernel/*range*.<br>2. **Masalah 2:** Menurunkan polinomial karakteristik secara aljabar, menghitung seluruh nilai eigen (disertai cek $\text{tr}(A)$ dan $\det(A)$), serta menentukan basis ruang eigen matriks $3\times 3$.<br>3. **Masalah 3:** Mendiagonalisasi matriks transisi perpindahan pengguna $A = PDP^{-1}$, merumuskan ekspresi tertutup $A^k = PD^kP^{-1}$, dan menghitung distribusi pangsa pengguna tunak (*steady-state* saat $k \to \infty$).<br>4. **Masalah 4:** Melakukan diagonalisasi ortogonal $A = Q\Lambda Q^T$ pada suatu matriks simetris riil $3\times 3$ dan memverifikasi bahwa $Q^TQ = I$. |
| **4. Metode / Cara Pengerjaan** | Dikerjakan **secara individu** (tulisan tangan rapi dipindai ke `.pdf` atau ketik $\LaTeX$ / *Equation Editor*). |
| **5. Deskripsi Luaran Tugas** | Berkas tunggal `STI205_T2_[NIM]_[Nama].pdf` memuat langkah penurunan lengkap, sketsa efek transformasi geometri Masalah 1, dan deklarasi kejujuran akademik. |
| **6. Kriteria & Bobot Penilaian** | Dinilai dengan **Rubrik Analitik Tugas 2 (`059_5`)**: (1) Ketepatan polinomial karakteristik, nilai eigen, & basis vektor eigen (35%); (2) Keruntutan diagonalisasi $PDP^{-1}$ & diagonalisasi ortogonal $Q\Lambda Q^T$ (40%); (3) Ketepatan pemodelan transformasi/*Markov* & cek verifikasi (25%). |

---

### 4.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Arsitektur Penilaian Terpadu** | Memadukan **Mini-Worksheet Verifikasi `NumPy` Individu (30% dari nilai UAS)** dan **Ujian Tertulis Komprehensif Luring di Kelas (70% dari nilai UAS, *Closed-Book*, 150 menit)** untuk mengukur secara otentik penguasaan matematis sekaligus komputasi `NumPy` pada **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`). |
| **Bagian A — *Mini-Worksheet* Python `NumPy` (30% UAS)** | Mahasiswa mengumpulkan 1 berkas notebook/laporan singkat (`.ipynb` + `.pdf`) yang mengimplementasikan murni dengan **`import numpy as np` (tanpa `scikit-learn`!)**:<br>1. Fungsi aproksimasi matriks/citra peringkat-$k$ menggunakan `np.linalg.svd` beserta perhitungan galat relatif Frobenius untuk $k = 1, 5, 20$.<br>2. Fungsi reduksi dimensi **PCA dari nol** (`mean-centering`, matriks kovarians / SVD, proyeksi ke 2 komponen utama, dan perhitungan *explained variance ratio*) pada matriks fitur berdimensi-6, serta pencocokan hasilnya dengan perhitungan tangan pada sub-sampel kecil. |
| **Bagian B — Ujian Tertulis Luring 150 Menit (70% UAS)** | 1. **(25% total UAS — `Sub-CPMK-4.1`)** Hitung secara analitis faktorisasi **SVD ($A = U\Sigma V^T$)** dari suatu matriks $3\times 2$ (atau $2\times 3$) beserta matriks hampiran *rank-1*-nya $A_1 = \sigma_1\mathbf{u}_1\mathbf{v}_1^T$.<br>2. **(25% total UAS — `Sub-CPMK-4.1 & 4.2`)** Diberikan matriks data mini 4 pengamatan $\times$ 2 fitur: hitung secara manual matriks terpusat $\tilde{X}$, matriks kovarians sampel $S$, vektor arah Komponen Utama ke-1 ($\mathbf{w}_1$), koordinat proyeksi 1D ke-4 data, dan persentase variansi yang terjelaskan oleh PC1.<br>3. **(20% total UAS — `Sub-CPMK-4.2` & Sintesis)** Tuliskan ekspresi vektorisasi Python `NumPy` yang setara dengan langkah matematis Soal 2 (serta jelaskan fungsi setiap dimensinya untuk memastikan kemandirian atas *Mini-Worksheet*), dan jawab pertanyaan sintesis hubungan antara *rank*, ruang nol, nilai eigen $A^TA$, serta nilai singular $\sigma_i$. |

---

## 5. FORMULA PERHITUNGAN NILAI, KETERCAPAIAN CPMK/CPL, & KONVERSI MUTU

### 5.1 Rumus Nilai per CPMK dan Nilai Akhir Mata Kuliah ($NA_{\text{STI-205}}$)

Sesuai pemetaan 1-ke-1 **Dokumen 008 §3**:
$$\text{Score}_{\text{CPMK-1}} = S_{\text{Tugas 1}}, \quad \text{Score}_{\text{CPMK-2}} = S_{\text{UTS}}, \quad \text{Score}_{\text{CPMK-3}} = S_{\text{Tugas 2}}, \quad \text{Score}_{\text{CPMK-4}} = S_{\text{UAS}}$$

Nilai Akhir Mata Kuliah ($0\text{–}100$):
$$NA_{\text{STI-205}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 5.2 Kontribusi Mata Kuliah terhadap `CPL-05` (`P1`)

Seluruh 100% bobot `STI-205` (3 SKS) mendukung **`CPL-05` (`P1`)** pada level *Introduce* (`I`), sehingga:
$$\text{Contribution}_{\text{STI-205} \to \text{CPL-05}}(i) = NA_{\text{STI-205}}(i) \quad \text{dengan bobot kredit } SKS_k \times W_{k,\text{CPL-05}} = 3 \times 1,0 = 3,0$$

*(Bersama `STI-102 Kalkulus`, `STI-103`, dan `STI-204 Matematika Diskrit dan Logika`, ketuntasan `STI-205` melengkapi seluruh fondasi `CPL-05` tahun pertama sebelum berlanjut ke penguatan `FST-408 Probabilitas dan Statistika` di Semester 4).*

### 5.3 Tabel Konversi Huruf Mutu & Ambang Ketuntasan OBE

| Rentang Skor ($0\text{–}100$) | Huruf Mutu | Angka Mutu | Status Kelulusan MK | Status Ketercapaian CPL/CPMK OBE ($\ge 65,0$) |
|:---:|:---:|:---:|:---:|:---:|
| $81,00 \text{ – } 100,00$ | **A** | 4,00 | Lulus | **Tercapai (Exemplary)** |
| $76,00 \text{ – } 80,99$ | **B+** | 3,50 | Lulus | **Tercapai (Proficient)** |
| $70,00 \text{ – } 75,99$ | **B** | 3,00 | Lulus | **Tercapai (Satisfactory)** |
| $65,00 \text{ – } 69,99$ | **C+** | 2,50 | Lulus | **Tercapai Minimum Ambang OBE ($\ge 65,0$)** |
| $56,00 \text{ – } 64,99$ | **C** | 2,00 | Lulus Administratif | *Belum Mencapai Target OBE (< 65,0 — Remedial CPMK Terkait)* |
| $45,00 \text{ – } 55,99$ | **D** | 1,00 | Tidak Lulus | **Tidak Tercapai** |
| $0,00 \text{ – } 44,99$ | **E** | 0,00 | Tidak Lulus | **Tidak Tercapai** |

---

## 6. PROTOKOL REMEDIAL, AUDIT GUARDRAIL `NUMPY`, & SIKLUS PPEPP

1. **Audit Kepatuhan Guardrail & Keaslian *Mini-Worksheet* `NumPy`:** Berkas `NumPy` pada UAS yang mengimpor `sklearn` / pustaka ML instan dikembalikan untuk diperbaiki ke operasi matriks `NumPy` murni; selain itu, Soal 3 pada ujian tertulis luring secara langsung menguji apakah mahasiswa benar-benar memahami makna dimensi dan ekspresi `NumPy` yang ditulisnya sendiri.
2. **Remedial Berbasis CPMK Spesifik:** Mahasiswa dengan skor $< 65,0$ pada salah satu `CPMK-1..4` diberikan 1 kali kesempatan ujian/tugas perbaikan terarah dengan nilai plafon remedial maksimal **70,0 (B)**.
3. **Evaluasi PPEPP & Handoff ke `STI-413 Pembelajaran Mesin`:** Profil penguasaan ruang vektor (`CPMK-2`) serta SVD/PCA (`CPMK-4`) didokumentasikan dalam laporan portofolio MK sebagai acuan kesiapan matematika kohor saat memasuki `STI-413 Pembelajaran Mesin` di Semester 4.
