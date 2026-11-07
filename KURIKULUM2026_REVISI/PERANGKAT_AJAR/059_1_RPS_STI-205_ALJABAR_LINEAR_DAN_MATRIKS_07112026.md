# RENCANA PEMBELAJARAN SEMESTER (RPS)

## STI-205 — ALJABAR LINEAR DAN MATRIKS
### *Linear Algebra and Matrices*

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)
> **Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang
> **Nomor Dokumen SPMI:** 071030.B4.5.2.RPS-STI205
> **Tanggal Penyusunan:** 07 November 2026
> **Sumber Data:** Dokumen 005 (struktur & identitas), 007 (silabus), 043 (CPMK/Sub-CPMK/Boundary Guardrails), 003 (CPL), 008 & 018 (skema asesmen dan rubrik)

---

## HALAMAN 1 — SAMPUL DEPAN (LANDSCAPE)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                            UNIVERSITAS WIDYAGAMA                             │
│                    FAKULTAS SAINS DAN TEKNOLOGI INFORMASI                    │
│                                                                              │
│                                                                              │
│                  RENCANA PEMBELAJARAN SEMESTER (RPS)                         │
│                                                                              │
│                                                                              │
│                     STI-205 — ALJABAR LINEAR DAN MATRIKS                     │
│                         Linear Algebra and Matrices                          │
│                                                                              │
│                            BOBOT: 3 SKS (TEORI)                              │
│                                                                              │
│                                                                              │
│                    Penyusun: Tim Pengembang RPS SISTEKIN                     │
│                    Koordinator RMK Matematika & Sains Komputasi              │
│                                                                              │
│                                                                              │
│                            MALANG, NOVEMBER 2026                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## HALAMAN 2 — IDENTITAS, OTORISASI, DAN CAPAIAN PEMBELAJARAN (LANDSCAPE)

### A. Tabel Identitas Mata Kuliah

| Atribut | Spesifikasi |
|---|---|
| **MATA KULIAH (MK)** | Aljabar Linear dan Matriks / *Linear Algebra and Matrices* |
| **KODE** | `STI-205` |
| **RUMPUN MK** | Matematika & Sains Komputasi (Core STI) |
| **BOBOT (sks)** | **T = 3** · **P = 0** — Total 3 SKS |
| **SEMESTER** | 2 (Genap) |
| **TGL PENYUSUNAN** | 07 November 2026 |
| **MATA KULIAH SYARAT** | `STI-102` Kalkulus |
| **DOSEN PENGAMPU** | Tim Pengampu Rumpun Matematika & Sains Komputasi (Core STI) |
| **BODY OF KNOWLEDGE** | `BK-IS10` *Applied Mathematics and Logic*; `BK-IT02` *Applied AI* |

### B. Blok Otorisasi

| Pengembang RPS | Koordinator RMK | Ketua Program Studi |
|:---:|:---:|:---:|
| Tim Pengembang RPS SISTEKIN | Koordinator RMK Matematika & Sains Komputasi | Ketua Prodi SISTEKIN FSTI |
| .......................... | .......................... | .......................... |

### C. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada MK

| Kode Baku (Alias) | Rumusan CPL (verbatim Dokumen 003) |
|:---:|---|
| **CPL-05** (`P1`) | Menguasai konsep dasar sains, matematika terapan (kalkulus, aljabar linear, statistika, matematika diskrit, logika) sebagai fondasi pemecahan masalah rekayasa sistem informasi dan komputasi cerdas yang kompleks. |

Bobot kontribusi MK terhadap CPL-05 (P1): **3 SKS** dari total MK pembina CPL-05 (P1).

### D. Capaian Pembelajaran Mata Kuliah (CPMK)

| Kode | Rumusan CPMK (Format ABCD) | Bloom | CPL |
|:---:|---|:---:|:---:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menyelesaikan** Sistem Persamaan Linear (SPL) (*B*) menggunakan eliminasi Gauss-Jordan dan matriks invers (*C*) secara tepat (*D*). | **C3** | `CPL-05` (`P1`) |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis** struktur ruang vektor, kombinasi linier, kebebasan linier, basis, dan dimensi (*B*) pada ruang $\mathbb{R}^n$ (*C*) dengan kaidah aljabar formal (*D*). | **C4** | `CPL-05` (`P1`) |
| **CPMK-3** | Mahasiswa (*A*) mampu **menghitung** nilai eigen (Eigenvalues), vektor eigen (Eigenvectors), dan diagonalisasi matriks (*B*) pada matriks transformasi linier (*C*) secara presisi (*D*). | **C3** | `CPL-05` (`P1`) |
| **CPMK-4** | Mahasiswa (*A*) mampu **merumuskan** dekomposisi matriks SVD (Singular Value Decomposition) dan reduksi dimensi PCA (*B*) menggunakan pustaka Python NumPy (*C*) untuk pemrosesan data AI (*D*). | **C4** | `CPL-05` (`P1`) |

### E. Sub-Capaian Pembelajaran Mata Kuliah (Sub-CPMK)

| Kode | Kompetensi Spesifik | CPMK | Bloom |
|---:|---|:--:|:--:|
| **Sub-CPMK-1.1** | Menyelesaikan Sistem Persamaan Linear (SPL) menggunakan eliminasi Gauss-Jordan dan matriks invers. | CPMK-1 | **C3** |
| **Sub-CPMK-1.2** | Menentukan jenis solusi SPL (tunggal, tak hingga, atau tak ada) dari bentuk eselon baris. | CPMK-1 | **C3** |
| **Sub-CPMK-2.1** | Menganalisis kombinasi linier, kebebasan linier, dan rentang (span) pada ruang vektor. | CPMK-2 | **C4** |
| **Sub-CPMK-2.2** | Menentukan basis dan dimensi ruang vektor R^n. | CPMK-2 | **C4** |
| **Sub-CPMK-3.1** | Menghitung nilai eigen, vektor eigen, dan diagonalisasi matriks. | CPMK-3 | **C3** |
| **Sub-CPMK-3.2** | Menerapkan diagonalisasi matriks pada transformasi linier. | CPMK-3 | **C3** |
| **Sub-CPMK-4.1** | Merumuskan dekomposisi SVD (Singular Value Decomposition) suatu matriks. | CPMK-4 | **C4** |
| **Sub-CPMK-4.2** | Menerapkan PCA (NumPy) untuk reduksi dimensi pada pemrosesan data AI. | CPMK-4 | **C4** |

### F. Matriks Korelasi CPL ↔ CPMK dan Bobot Penilaian

| CPMK | CPL | Pekan | Tugas 1 (20%) | UTS (30%) | Tugas 2 (20%) | UAS (30%) | Bobot CPMK |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CPMK-1 | `CPL-05` (`P1`) | 2–3, 8 | **50%** | **50%** | — | — | 100% |
| CPMK-2 | `CPL-05` (`P1`) | 4–5, 8 | **50%** | **50%** | — | — | 100% |
| CPMK-3 | `CPL-05` (`P1`) | 6–7, 8, 12, 16 | — | **20%** | **30%** | **50%** | 100% |
| CPMK-4 | `CPL-05` (`P1`) | 9–11, 12, 16 | — | — | **60%** | **40%** | 100% |
| **Total instrumen** | | | **20%** | **30%** | **20%** | **30%** | **100%** |

*Cara baca:* Skor CPMK-1 = 0,50 × Tugas 1 + 0,50 × UTS. Skor CPMK-2 = 0,50 × Tugas 1 + 0,50 × UTS. Skor CPMK-3 = 0,20 × UTS + 0,30 × Tugas 2 + 0,50 × UAS. Skor CPMK-4 = 0,60 × Tugas 2 + 0,40 × UAS. Nilai Akhir = 0,20×T1 + 0,30×UTS + 0,20×T2 + 0,30×UAS.

### G. Deskripsi Singkat Mata Kuliah

Mata kuliah ini membangun **bahasa aljabar bagi komputasi numerik dan kecerdasan artifisial**. Pembahasan dimulai dari objek paling dasar: vektor di $\mathbb{R}^n$ dengan operasi *dot product* dan norma, lalu matriks dengan operasi dan sifat-sifatnya. Dari sana dibangun Sistem Persamaan Linear (SPL) sebagai masalah pusat aljabar linear — dimodelkan sebagai matriks diperbesar (*augmented matrix*), diselesaikan dengan Operasi Baris Elementer (OBE), eliminasi Gauss dan Gauss–Jordan, serta matriks invers; jenis solusi (tunggal, tak hingga, tak ada) ditentukan dari bentuk eselon baris. Bagian kedua menggeneralisasi SPL menjadi **struktur ruang vektor**: aksioma ruang vektor riil, subruang, kombinasi linier, rentang (*span*), kebebasan linier, basis, dimensi, ruang baris dan kolom, serta proses ortogonalisasi Gram–Schmidt pada ruang hasil kali dalam. Bagian ketiga membahas **transformasi linier** sebagai objek yang menyatukan semua konsep sebelumnya: matriks representasi, kernel dan *range*, polinomial karakteristik, nilai eigen dan vektor eigen, serta diagonalisasi matriks bujursangkar dan matriks simetris. Bagian akhir menjembatani aljabar linear murni dengan pemrosesan data AI: **Singular Value Decomposition** (SVD) dan **Principal Component Analysis** (PCA) yang diimplementasikan dengan pustaka Python NumPy untuk reduksi dimensi. Seluruh pembahasan berada pada **level matematis dan implementasi dasar**; pelatihan model *machine learning* dan pengembangan aplikasi web berada di luar kewenangan MK ini sesuai pagar *Out-of-Scope* Dokumen 043. MK ini menjadi prasyarat langsung bagi `FST-408` (Probabilitas dan Statistika) dan penopang `STI-413` (Machine Learning) serta MK deep learning.

### H. Bahan Kajian (Body of Knowledge)

| Kode | Nomenklatur BoK | Cakupan dalam MK |
|:---:|---|---|
| `BK-IS10` | *Applied Mathematics and Logic* | Vektor, matriks, SPL, determinan, ruang vektor, transformasi linier, eigen, SVD |
| `BK-IT02` | *Applied AI* | Reduksi dimensi PCA, representasi data matriks, dasar komputasi numerik dengan NumPy |

**Pokok bahasan:** (1) vektor di $\mathbb{R}^n$, dot product, norma; (2) matriks, operasi, transpose; (3) SPL, matriks diperbesar, OBE, Gauss & Gauss–Jordan; (4) bentuk eselon, jenis solusi, determinan, aturan Cramer, invers; (5) ruang vektor, subruang, kombinasi linier, span; (6) kebebasan linier, basis, dimensi, Gram–Schmidt; (7) transformasi linier, kernel, range, polinomial karakteristik, eigen; (8) diagonalisasi & matriks simetris; (9) evaluasi tengah semester; (10) SVD; (11) PCA via NumPy; (12) studi kasus reduksi dimensi; (13) proyek terapan & presentasi antara; (14) penyempurnaan proyek; (15) review, presentasi final; (16) evaluasi akhir semester.

### I. Pustaka

**Pustaka Utama**

| No | Referensi |
|:---:|---|
| [1] | Lay, D.C., Lay, S.R. & McDonald, J.J. (2021). *Linear Algebra and Its Applications*, 6th ed. Pearson. ISBN 978-0-13-585926-9. |
| [2] | Strang, G. (2016). *Introduction to Linear Algebra*, 5th ed. Wellesley-Cambridge Press. ISBN 978-0-9802327-7-6. |
| [3] | Anton, H. & Rorres, C. (2019). *Elementary Linear Algebra: Applications Version*, 12th ed. Wiley. ISBN 978-1-119-24322-6. |

**Pustaka Pendukung**

| No | Referensi |
|:---:|---|
| [4] | Golub, G.H. & Van Loan, C.F. (2013). *Matrix Computations*, 4th ed. Johns Hopkins University Press. ISBN 978-1-4214-0794-4. |
| [5] | Deisenroth, M.P., Faisal, A.A. & Ong, C.S. (2020). *Mathematics for Machine Learning*, Bab 2–4 & 10. Cambridge University Press. ISBN 978-1-108-45514-5. |
| [6] | Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*, Bab 2 (Linear Algebra). MIT Press. ISBN 978-0-262-03561-3. |
| [7] | Harris, C.R. et al. (2020). "Array programming with NumPy". *Nature*, 585, 357–362. doi:10.1038/s41586-020-2649-2. |
| [8] | Meyer, C.D. (2000). *Matrix Analysis and Applied Linear Algebra*. SIAM. ISBN 978-0-89871-454-8. |

---

## HALAMAN 3–4 — MATRIKS RENCANA PEMBELAJARAN 16 PEKAN (LANDSCAPE)

**Identitas waktu:** 3 SKS Teori → TM = 150 menit/pekan; PT = 180 menit/pekan; BM = 180 menit/pekan.

| Mg | Sub-CPMK (Kemampuan Akhir) | Indikator Penilaian | Kriteria & Teknik | Luring (TM/PT/BM) | Daring | Materi Pembelajaran [Pustaka] | Bobot |
|:--:|---|---|---|---|---|---|:--:|
| 1 | Orientasi MK & kontrak belajar (fondasi vektor) | Ketepatan menjelaskan ruang lingkup, capaian, dan skema asesmen | Kriteria: kelengkapan jawaban; Teknik: tanya-jawab lisan | Kuliah interaktif; TM 150′ / PT 180′ / BM 180′ | Forum perkenalan di LMS; unduh kontrak belajar | Ruang lingkup aljabar linear, peta CPL–CPMK, vektor di $\mathbb{R}^n$, dot product, norma, jarak [1] Bab 1 & 6; [2] Bab 1 | — |
| 2 | **Sub-CPMK-1.1** — Menyelesaikan SPL dengan eliminasi Gauss-Jordan | 1.1.1 Ketepatan operasi matriks & OBE; 1.1.2 Ketepatan langkah Gauss–Jordan hingga bentuk eselon tereduksi | Kriteria: ketepatan prosedur; Teknik: kuis formatif, latihan terbimbing | Kuliah & latihan; TM 150′ / PT 180′ / BM 180′ | Kuis LMS (formatif, non-graded) | Matriks, operasi matriks, transpose, matriks diperbesar, OBE, eliminasi Gauss, Gauss–Jordan [1] Bab 1–2; [3] Bab 1 | — |
| 3 | **Sub-CPMK-1.2** — Menentukan jenis solusi SPL dari bentuk eselon baris | 1.2.1 Ketepatan klasifikasi solusi (tunggal/tak hingga/tak ada); 1.2.2 Ketepatan determinan & invers | Kriteria: ketepatan analisis; Teknik: latihan terstruktur | Ceramah interaktif + latihan; TM 150′ / PT 180′ / BM 180′ | Bank soal SPL di LMS | Bentuk eselon baris & tereduksi, variabel bebas, determinan, sifat determinan, aturan Cramer, invers via adjoin & OBE [1] Bab 2–3; [8] Bab 1 | — |
| **4** | **Sub-CPMK-2.1** — Menganalisis kombinasi linier, kebebasan linier, dan span | 2.1.1 Ketepatan uji kombinasi linier; 2.1.2 Ketepatan penentuan span & subruang | Kriteria: rubrik analitik (4 dimensi); Teknik: **Tugas 1** — kuis + problem solving | Case-based learning; TM 150′ / PT 180′ / BM 180′ | Submit Tugas 1 via LMS (PDF) | Aksioma ruang vektor riil, subruang, kombinasi linier, rentang (*span*), himpunan perentang [1] Bab 4; [2] Bab 3 | **20%** |
| 5 | **Sub-CPMK-2.2** — Menentukan basis dan dimensi ruang vektor $\mathbb{R}^n$ | 2.2.1 Ketepatan uji kebebasan linier; 2.2.2 Ketepatan penentuan basis, dimensi, dan Gram–Schmidt | Kriteria: ketepatan hasil & justifikasi; Teknik: latihan bertingkat | Kuliah & latihan; TM 150′ / PT 180′ / BM 180′ | Latihan bertingkat di LMS | Kebebasan linier, basis, dimensi, ruang baris & kolom, rank, ruang hasil kali dalam, ortogonalisasi Gram–Schmidt [1] Bab 4 & 6; [3] Bab 4–5 | — |
| 6 | **Sub-CPMK-3.1** — Menghitung nilai eigen, vektor eigen, dan diagonalisasi | 3.1.1 Ketepatan polinomial karakteristik; 3.1.2 Ketepatan penentuan ruang eigen | Kriteria: ketepatan komputasi; Teknik: latihan terstruktur | Ceramah & latihan; TM 150′ / PT 180′ / BM 180′ | Lembar latihan eigen di LMS | Transformasi linier, matriks representasi, kernel & range, polinomial karakteristik, nilai & vektor eigen [1] Bab 5; [8] Bab 7 | — |
| 7 | **Sub-CPMK-3.2** — Menerapkan diagonalisasi pada transformasi linier | 3.2.1 Ketepatan syarat diagonalisasi; 3.2.2 Ketepatan diagonalisasi matriks simetris | Kriteria: ketepatan syarat & hasil; Teknik: studi kasus terstruktur | Case method; TM 150′ / PT 180′ / BM 180′ | Analisis kasus di LMS | Diagonalisasi, multiplisitas aljabar vs geometrik, matriks simetris & ortogonal, teorema spektral (pengantar) [1] Bab 5 & 7; [2] Bab 6 | — |
| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | Ketuntasan CPMK-1, CPMK-2, CPMK-3 (tahap awal) | Kriteria: kunci jawaban terstandar; Teknik: ujian tertulis terjadwal | Ujian; TM 150′ | — | Materi pekan 1–7 | **30%** |
| 9 | **Sub-CPMK-4.1** — Merumuskan dekomposisi SVD | 4.1.1 Ketepatan langkah SVD; 4.1.2 Ketepatan interpretasi nilai singular & rank | Kriteria: ketepatan formulasi; Teknik: latihan terbimbing | Ceramah & derivasi bersama; TM 150′ / PT 180′ / BM 180′ | Video + lembar derivasi di LMS | Nilai singular, dekomposisi $A = U\Sigma V^T$, rank terpotong, aproksimasi rank-$k$ [4] Bab 2; [5] Bab 10 | — |
| 10 | **Sub-CPMK-4.2** — Menerapkan PCA via NumPy untuk reduksi dimensi | 4.2.1 Ketepatan alur PCA; 4.2.2 Ketepatan interpretasi varians terjelaskan | Kriteria: ketepatan implementasi & interpretasi; Teknik: praktik terpandu | Demo & praktik komputasi; TM 150′ / PT 180′ / BM 180′ | Notebook NumPy di LMS | Standarisasi data, matriks kovarians, eigen/SVD, komponen utama, *explained variance ratio*, rekonstruksi [5] Bab 10; [7] | — |
| 11 | Penguatan CPMK-3 & CPMK-4 — studi kasus reduksi dimensi | 4.3.1 Ketepatan pemilihan jumlah komponen; 4.3.2 Ketepatan justifikasi trade-off | Kriteria: ketajaman analisis; Teknik: kerja kelompok terpandu | PjBL / Case Method; TM 150′ / PT 180′ / BM 180′ | Konsultasi asinkron | Studi kasus: reduksi dimensi data tabular & citra, kompresi matriks, analisis galat rekonstruksi [5]; [4] | — |
| **12** | **Sub-CPMK-4.2 (integrasi)** — Proyek terapan lanjut & presentasi antara | 4.4.1 Kelayakan model aljabar; 4.4.2 Kejelasan argumentasi kuantitatif | Kriteria: rubrik analitik (4 dimensi); Teknik: **Tugas 2** — laporan proyek + presentasi | PjBL / Presentasi; TM 150′ / PT 180′ / BM 180′ | Submit Tugas 2 via LMS | Integrasi SPL–ruang vektor–eigen–SVD/PCA pada kasus nyata [1]; [5] | **20%** |
| 13 | Penyempurnaan proyek berdasarkan umpan balik | 4.4.3 Ketepatan revisi; 4.4.4 Kualitas dokumentasi | Kriteria: checklist revisi; Teknik: konsultasi klinis | PjBL / Konsultasi; TM 150′ / PT 180′ / BM 180′ | Konsultasi asinkron | Seluruh materi CPMK-3 & CPMK-4 | — |
| 14 | Review & konsolidasi seluruh CPMK | Ketepatan identifikasi kesenjangan pemahaman | Kriteria: kelengkapan peta konsep; Teknik: review bersama | Diskusi / Konsultasi; TM 150′ / PT 180′ / BM 180′ | Pembahasan soal terpilih di LMS | Rekapitulasi pekan 1–13 | — |
| 15 | Presentasi final / demonstrasi hasil | 4.4.5 Kualitas komunikasi teknis; 4.4.6 Penguasaan saat tanya jawab | Kriteria: rubrik presentasi; Teknik: presentasi tim | Presentasi & pleno; TM 150′ / PT 180′ / BM 180′ | Unggah slide & rekaman | Seluruh materi CPMK-1 s.d. CPMK-4 | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS)** | Ketuntasan komprehensif CPMK-1 s.d. CPMK-4 | Kriteria: kunci jawaban & rubrik esai; Teknik: ujian komprehensif | Ujian; TM 150′ | — | Materi pekan 1–15 | **30%** |
| | **TOTAL BOBOT PENILAIAN** | | | | | | **100%** |

**Keterangan waktu:** TM = tatap muka (1 SKS = 50 menit/pekan); PT = penugasan terstruktur (1 SKS = 60 menit/pekan); BM = belajar mandiri (1 SKS = 60 menit/pekan). Mata kuliah ini tidak memiliki komponen praktikum (P = 0); sesi praktik komputasi NumPy pada pekan 10 dilakukan dengan notebook daring pada perangkat mahasiswa, bukan praktikum laboratorium terjadwal.

---

## HALAMAN 5 — LAMPIRAN 1: NASKAH TUGAS 1 + RUBRIK (PORTRAIT)

### A. Naskah Tugas 1 — Kuis & Problem Solving "SPL, Matriks, dan Struktur Ruang Vektor"

**Pekan:** 4 | **Bobot:** 20% | **CPMK:** CPMK-1 & CPMK-2 | **Bentuk:** Individu | **Durasi:** 150 menit

**Instruksi:**

1. Diberikan sistem persamaan linear:
   $$\begin{cases} 2x_1 - x_2 + 3x_3 = 5 \\ x_1 + 2x_2 - x_3 = 1 \\ 3x_1 + x_2 + 2x_3 = 6 \end{cases}$$
   (a) Tuliskan matriks diperbesar dan lakukan eliminasi Gauss–Jordan. (10 poin)
   (b) Tentukan jenis solusinya (tunggal, tak hingga, atau tak ada) beserta alasannya. (5 poin)
2. Diberikan $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
   (a) Hitung $\det(A)$ dan tentukan apakah $A$ invertibel. (5 poin)
   (b) Tentukan $A^{-1}$ dengan metode adjoin **dan** verifikasi dengan OBE. (10 poin)
   (c) Selesaikan $Ax = b$ untuk $b = \begin{pmatrix} 5 \\ 11 \end{pmatrix}$ menggunakan $A^{-1}$, lalu bandingkan dengan hasil aturan Cramer. (5 poin)
3. Diberikan $\mathbf{u} = (1,2,-1)$, $\mathbf{v} = (2,-1,3)$, dan $\mathbf{w} = (5,3,1)$ pada $\mathbb{R}^3$.
   (a) Periksa apakah $\mathbf{w}$ merupakan kombinasi linier dari $\mathbf{u}$ dan $\mathbf{v}$. Tunjukkan sistem yang harus diselesaikan. (10 poin)
   (b) Tentukan apakah $\{\mathbf{u}, \mathbf{v}\}$ bebas linier. (5 poin)
4. Diberikan $S = \{(1,0,1), (0,1,1), (1,1,2)\}$ pada $\mathbb{R}^3$.
   (a) Tentukan apakah $S$ merentang $\mathbb{R}^3$. (10 poin)
   (b) Bila tidak, tentukan $\mathrm{span}(S)$ secara eksplisit sebagai bidang/garis dalam $\mathbb{R}^3$. (10 poin)
5. Diberikan subruang $W = \{(x,y,z) \in \mathbb{R}^3 \mid x + 2y - z = 0\}$.
   (a) Tunjukkan bahwa $W$ adalah subruang (uji ketiga syarat). (10 poin)
   (b) Tentukan basis dan dimensi $W$. (10 poin)

**Ketentuan:** dikerjakan individual; seluruh langkah OBE wajib ditulis lengkap (jangan melompati baris); jawaban akhir tanpa langkah dinilai maksimal 40% poin butir; kalkulator ilmiah diperbolehkan untuk verifikasi aritmetika, **tidak** untuk menggantikan OBE.

**Deliverable:** berkas PDF jawaban bertahap.

### B. Rubrik Penilaian Tugas 1 (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Ketepatan OBE & penyelesaian SPL (25%)** | Setiap langkah OBE ditulis dan valid; bentuk eselon tereduksi benar; jenis solusi disimpulkan tepat | Satu langkah diringkas; hasil dan kesimpulan benar | Ada kekeliruan aritmetika yang memengaruhi satu butir | Prosedur OBE tidak dikuasai |
| **2. Ketepatan determinan & invers (25%)** | Determinan, adjoin, dan verifikasi OBE seluruhnya benar; Cramer konsisten | Tepat dengan 1 kekeliruan aritmetika minor | Invers benar sebagian; verifikasi tidak dilakukan | Tidak mampu menentukan invers |
| **3. Ketepatan analisis ruang vektor (30%)** | Uji kombinasi linier, kebebasan linier, span, subruang, basis, dan dimensi seluruhnya benar dengan justifikasi | Tepat; satu justifikasi diringkas | Satu konsep keliru (mis. basis tidak bebas linier) | Tidak membedakan span, basis, dan dimensi |
| **4. Kerapian & tata tulis matematis (20%)** | Notasi vektor/matriks konsisten; langkah runtut; seluruh butir dijawab | Notasi konsisten; beberapa langkah diringkas | Notasi tidak konsisten; ada butir tidak dijawab | Jawaban tidak terbaca |

---

## HALAMAN 6 — LAMPIRAN 2: NASKAH UTS + RUBRIK (PORTRAIT)

### A. Naskah UTS — Ujian Tertulis Matriks, SPL, Ruang Vektor, dan Eigen

**Pekan:** 8 | **Bobot:** 30% | **CPMK:** CPMK-1, CPMK-2, CPMK-3 | **Bentuk:** Individu, *closed book* | **Durasi:** 150 menit

**Struktur soal:**

| Bagian | Bentuk | Jumlah | Poin | Cakupan |
|:--:|---|:--:|:--:|---|
| I | Uraian terstruktur (SPL, OBE, determinan, invers) | 3 | 30 | CPMK-1 |
| II | Uraian analitis (ruang vektor, basis, dimensi) | 3 | 35 | CPMK-2 |
| III | Uraian komputasi (eigen & diagonalisasi) | 2 | 25 | CPMK-3 |
| IV | Studi kasus terapan (pemodelan matriks) | 1 | 10 | CPMK-1, CPMK-2 |

**Contoh butir Bagian IV:**
> Sebuah jaringan pipa distribusi air memiliki tiga titik pertemuan. Laju aliran (dalam liter/detik) memenuhi sistem:
> $$x_1 - x_2 = 4, \qquad x_2 - x_3 = 1, \qquad x_1 - x_3 = 5$$
> (a) Tuliskan matriks diperbesar dan tentukan rank matriks koefisien serta rank matriks diperbesar. (4 poin)
> (b) Berdasarkan teorema Rouché–Capelli (bandingkan rank), tentukan apakah sistem konsisten, dan bila konsisten tentukan derajat kebebasan solusinya. Jelaskan makna fisisnya bagi jaringan pipa. (6 poin)

**Ketentuan:** *closed book*; kalkulator ilmiah tidak diperlukan; seluruh langkah OBE wajib ditulis; jawaban akhir tanpa langkah dinilai maksimal 40% poin butir.

### B. Rubrik Penilaian UTS (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Penguasaan konsep & prosedur (25%)** | Definisi, teorema, dan prosedur diterapkan tepat; syarat keberlakuan disebut | Tepat dengan 1–2 kekeliruan minor | Konsep dasar dipahami; ada kesalahan prosedur | Salah memahami konsep inti |
| **2. Keruntutan alur komputasi (30%)** | Setiap langkah OBE/substitusi terjustifikasi dan dapat diikuti | Sebagian besar runtut; ada lompatan kecil | Alur terputus-putus | Tidak ada alur penyelesaian |
| **3. Ketepatan hasil & justifikasi (30%)** | Seluruh hasil benar; kesimpulan (jenis solusi, basis, diagonalisasi) tepat dan terjustifikasi | Hasil benar; justifikasi ringkas | Sebagian besar hasil keliru | Hasil tidak relevan |
| **4. Kelengkapan & kerapian jawaban (15%)** | Seluruh butir dijawab lengkap dan terbaca; notasi konsisten | Seluruh butir dijawab; beberapa kurang rinci | Ada butir tidak dijawab | Banyak butir kosong |

---

## HALAMAN 7 — LAMPIRAN 3: NASKAH TUGAS 2 + RUBRIK (PORTRAIT)

### A. Naskah Tugas 2 — Proyek Terapan "Aljabar Linear untuk Reduksi Dimensi Data"

**Pekan:** 12 | **Bobot:** 20% | **CPMK:** CPMK-3 & CPMK-4 | **Bentuk:** Kelompok 3–4 orang | **Durasi:** 3 pekan

**Instruksi:**

1. Pilih **satu** dari tiga tema berikut:
   - **T1:** Reduksi dimensi data tabular akademik (mis. 20 indikator kinerja mahasiswa) menjadi 2–3 komponen utama, disertai interpretasi setiap komponen.
   - **T2:** Kompresi citra *grayscale* menggunakan SVD aproksimasi rank-$k$; analisis kurva galat rekonstruksi terhadap $k$.
   - **T3:** Analisis sistem persamaan pada model rangkaian/jaringan sederhana: pembentukan SPL, penentuan rank, dan interpretasi solusi (tunggal vs tak hingga).
2. Sajikan **formulasi aljabar lengkap**: matriks data, standarisasi, matriks kovarians atau SVD, serta persamaan rekonstruksi.
3. Implementasikan dengan **Python NumPy murni** (bukan pustaka *machine learning* tingkat tinggi seperti scikit-learn) dan lampirkan kode sumber yang dapat dijalankan.
4. Sertakan **minimal dua eksperimen** dengan parameter berbeda (mis. $k = 1, 3, 5$) dan bandingkan hasilnya secara kuantitatif.
5. Buat **visualisasi**: *scree plot explained variance*, grafik galat rekonstruksi, atau scatter plot dua komponen utama.
6. Analisis **keterbatasan**: asumsi linearitas, sensitivitas terhadap skala, interpretabilitas komponen, biaya komputasi.
7. Format: laporan 12–16 halaman, sitasi IEEE minimal 8 rujukan (≥ 3 buku/artikel aljabar linear), font 11 pt, spasi 1,15.
8. Wajib menyertakan **Deklarasi Transparansi AI** dan pembagian peran tim.

**Deliverable:** laporan PDF + notebook Python (`.ipynb`) + slide ringkas 7 halaman.

### B. Rubrik Penilaian Tugas 2 (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Ketepatan formulasi aljabar (30%)** | Formulasi matriks lengkap dan konsisten; asumsi dinyatakan; notasi tepat | Formulasi benar; satu komponen kurang eksplisit | Formulasi benar sebagian; asumsi tidak jelas | Formulasi tidak terbentuk |
| **2. Ketepatan implementasi & verifikasi (25%)** | Implementasi NumPy benar; ≥ 2 eksperimen; hasil diverifikasi manual pada sampel kecil | Implementasi benar; verifikasi sebagian | Implementasi berjalan tetapi hasil tidak diverifikasi | Kode tidak berjalan atau hasil tidak relevan |
| **3. Kualitas visualisasi & interpretasi (25%)** | Visualisasi akurat dan berlabel; interpretasi komponen menghubungkan matematika dengan domain data | Visualisasi benar; interpretasi memadai | Visualisasi kurang informatif; interpretasi dangkal | Tanpa visualisasi |
| **4. Analisis keterbatasan & tata tulis (20%)** | Keterbatasan dianalisis kritis; laporan rapi; ≥ 8 rujukan IEEE; kode terdokumentasi | Analisis memadai; 6–7 rujukan | Analisis umum; < 6 rujukan | Tanpa analisis keterbatasan |

---

## HALAMAN 8 — LAMPIRAN 4: NASKAH UAS + RUBRIK (PORTRAIT)

### A. Naskah UAS — Evaluasi Komprehensif Aljabar Linear dan Matriks

**Pekan:** 16 | **Bobot:** 30% | **CPMK:** CPMK-1, CPMK-2, CPMK-3, CPMK-4 | **Bentuk:** Individu | **Durasi:** 150 menit

**Struktur soal:**

| Bagian | Bentuk | Poin | Cakupan |
|:--:|---|:--:|---|
| I | Uraian: SPL, matriks, determinan, invers | 20 | CPMK-1 |
| II | Uraian: ruang vektor, basis, dimensi, ortogonalitas | 25 | CPMK-2 |
| III | Uraian: eigen, diagonalisasi, dan SVD | 30 | CPMK-3, CPMK-4 |
| IV | Pemodelan terbuka: perancangan solusi aljabar untuk kasus baru | 25 | CPMK-3, CPMK-4 |

**Contoh butir Bagian III:**
> Diberikan matriks $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$.
> (a) Tentukan polinomial karakteristik, nilai eigen, dan vektor eigen $A$. (12 poin)
> (b) Tentukan matriks $P$ dan $D$ sehingga $A = PDP^{-1}$, lalu verifikasi hasilnya. (8 poin)
> (c) Hitung nilai singular $A$ dari $\sigma_i = \sqrt{\lambda_i(A^TA)}$ dan tuliskan bentuk dekomposisi SVD $A = U\Sigma V^T$. (6 poin)
> (d) Jelaskan mengapa SVD selalu ada untuk matriks sembarang, sedangkan diagonalisasi tidak. (4 poin)

### B. Rubrik Penilaian UAS (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Penguasaan konsep komprehensif (25%)** | Mengaitkan SPL–ruang vektor–transformasi–eigen–SVD secara utuh dan koheren | Konsep benar; keterkaitan sebagian | Konsep terpisah-pisah | Salah konsep mendasar |
| **2. Ketepatan komputasi simbolik (30%)** | Seluruh komputasi benar; notasi matriks konsisten; langkah lengkap dan efisien | 1–2 kekeliruan minor | Beberapa kekeliruan yang memengaruhi hasil | Komputasi tidak dapat diikuti |
| **3. Kedalaman analisis & justifikasi (30%)** | Justifikasi setiap kesimpulan (eksistensi, ketunggalan, syarat diagonalisasi) tepat dan mendalam | Justifikasi tepat; kurang mendalam | Justifikasi deskriptif | Tanpa justifikasi |
| **4. Struktur & komunikasi matematis (15%)** | Uraian runtut; definisi dipakai tepat; kesimpulan eksplisit | Uraian jelas; kesimpulan ada | Uraian kurang runtut | Tidak terstruktur |

---

## HALAMAN 9 — LEMBAR VALIDASI DAN PENGESAHAN (PORTRAIT)

| Memvalidasi,<br>Unit Penjaminan Mutu FSTI | Malang, 07 November 2026<br>Dosen Pengampu Mata Kuliah |
|:---:|:---:|
| ..........................<br>NUPTK. .......................... | ..........................<br>NIDN/NUPTK. .......................... |

<br>

| Mengesahkan,<br>Ketua Program Studi S1 Sistem dan Teknologi Informasi |
|:---:|
| ..........................<br>NUPTK. .......................... |

---

## LAMPIRAN TEKNIS — KESESUAIAN DENGAN TEMPLATE MASTER RPS FSTI UWG

### A. Pemetaan 18 Tag Nilai Tunggal (`{{...}}`)

| Tag | Nilai Terisi |
|---|---|
| `{{namamk}}` | Aljabar Linear dan Matriks |
| `{{kodemk}}` | STI-205 |
| `{{rumpunmk}}` | Matematika & Sains Komputasi (Core STI) |
| `{{skst}}` | 3 |
| `{{sksp}}` | 0 |
| `{{sms}}` | 2 (Genap) |
| `{{tglsusun}}` | 07 November 2026 |
| `{{pengembangrps}}` | Tim Pengembang RPS SISTEKIN |
| `{{koordinatormk}}` | Koordinator RMK Matematika & Sains Komputasi |
| `{{ketuaprodi}}` | Ketua Prodi SISTEKIN FSTI |
| `{{kodeprodi}}` | B4.5.2.RPS-STI205 |
| `{{prodi}}` | Sistem dan Teknologi Informasi |
| `{{namadosen}}` | Tim Pengampu Rumpun Matematika & Sains Komputasi |
| `{{nuptk}}` | .......................... |
| `{{deskripsimk}}` | Lihat Bagian G Halaman 2 |
| `{{bahankajian}}` | BK-IS10, BK-IT02 — lihat Bagian H Halaman 2 |
| `{{dosenpengampu}}` | Tim Pengampu Rumpun Matematika & Sains Komputasi (Core STI) |
| `{{mkprasyarat}}` | STI-102 |

### B. Pemetaan 25 Tag Blok Isi (`[...]`)

| Tag | Lokasi | Sumber Isi |
|---|---|---|
| `[nocpl]`, `[cpl]` | Hal 2 | Bagian C (1 baris CPL: CPL-05 (P1)) |
| `[nocpmk]`, `[cpmk]` | Hal 2 | Bagian D (4 CPMK) |
| `[nosubcpmk]`, `[subcpmk]` | Hal 2 | Bagian E (8 Sub-CPMK) |
| `[tabelkolerasi]` | Hal 2 | Bagian F (matriks CPL×CPMK, total 100%) |
| `[pustakautama]` | Hal 2 | Bagian I — 3 pustaka utama |
| `[pustakapendukung]` | Hal 2 | Bagian I — 5 pustaka pendukung |
| `[mingguke]` … `[bobot_nilai]` | Hal 3–4 | Kolom 1–8 tabel 16 pekan |
| `[penugasan1]`, `[rubriktugas1]` | Hal 5 | Lampiran 1 |
| `[soaluts]`, `[rubrikuts]` | Hal 6 | Lampiran 2 |
| `[tugas2]`, `[rubriktugas2]` | Hal 7 | Lampiran 3 |
| `[soaluas]`, `[rubrikuas]` | Hal 8 | Lampiran 4 |

### C. Pernyataan Kepatuhan Skema Asesmen

| Komponen | Pekan | Bobot | Target CPMK | Status |
|:---:|:---:|:---:|:---:|:---:|
| Tugas 1 | 4 | 20% | CPMK-1 & CPMK-2 | Sesuai |
| UTS | 8 | 30% | CPMK-1, CPMK-2, CPMK-3 | Sesuai |
| Tugas 2 | 12 | 20% | CPMK-3 & CPMK-4 | Sesuai |
| UAS | 16 | 30% | CPMK-1 s.d. CPMK-4 (komprehensif) | Sesuai |
| **Total** | | **100%** | | **Lulus** |

### D. Kepatuhan Boundary Guardrails (Dokumen 043)

| Kategori | Isi |
|---|---|
| **In-Scope (diajarkan)** | Sistem Persamaan Linier (SPL), eliminasi Gauss–Jordan, aljabar matriks, vektor ruang $\mathbb{R}^n$, determinan, invers, nilai eigen dan vektor eigen, dekomposisi PCA dasar |
| **Out-of-Scope (tidak diajarkan)** | Pelatihan algoritma *machine learning* (scikit-learn), pengodean aplikasi web, analisis limit–diferensial–integral kalkulus |
| **Handoff Anchor** | Menguasai manipulasi aljabar linear matriks; menyerahkan pemodelan *machine learning* tabular ke `STI-413` dan *deep learning* ke `STI-624` |

> **Catatan rujukan kode:** Dokumen 043 menulis titik serah terima *deep learning* sebagai `STI-726`. Menurut Dokumen 005 (daftar MK berkesinambungan), `STI-726` adalah MK Semester 7, sedangkan MK *deep learning* Semester 6 berkode **`STI-624`**. Karena itu dokumen ini memakai `STI-624`. Ketidaksesuaian pada Dokumen 043 telah dicatat sebagai temuan terbuka (kode ganda `STI-726`/`STI-727`) dan menunggu perbaikan.

---

*Dokumen ini disusun dari Dokumen 005, 007, 043, 003, 008, dan 018. Rujukan pustaka merupakan usulan standar bidang ilmu dan tetap terbuka untuk validasi KBK/GPM. Dokumen pendamping: `059_2_SAP_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`, `059_3_OUTLINE_MODUL_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`, `059_4_RENCANA_EVALUASI_ASESMEN_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`, `059_5_RUBRIK_PENILAIAN_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`.*
