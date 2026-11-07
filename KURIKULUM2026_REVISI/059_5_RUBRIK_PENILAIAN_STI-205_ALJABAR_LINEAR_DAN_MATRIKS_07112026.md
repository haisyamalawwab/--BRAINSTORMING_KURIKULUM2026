# 059_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-205 — ALJABAR LINEAR DAN MATRIKS (*Linear Algebra and Matrices*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI205`  
**Klaster Rubrik Master (Dok 018):** Klaster 1 (`K-1`) — Sains Dasar & Teori Formal  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** Panduan KPT 2024 Dikti (Tabel 18, 19, 20) · Dok 008 §4 · Dok 018 §3 · Dok 033 · `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` · `059_4_RENCANA_EVALUASI_ASESMEN_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`.

---

## BAGIAN I — PEDOMAN PENSKORAN RUBRIK KLASTER SAINS DASAR (`K-1`)

Sesuai **Dokumen 018 §3**, penilaian pada `STI-205 Aljabar Linear dan Matriks` menekankan keseimbangan antara **ketepatan konsep/teorema aljabar linear (35%–40%)**, **keruntutan prosedur reduksi/dekomposisi matriks (35%–40%)**, dan **presisi hasil numerik maupun verifikasi komputasi `NumPy` (20%–30%)**.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1`: `Sub-CPMK-1.1` & `1.2`)
**Objek Penilaian:** *Problem-Based Matrix Set* Berparameter NIM: *Cosine Similarity*, Eliminasi Gauss-Jordan (`RREF`), Analisis 3 Jenis Solusi SPL Berparameter, Determinan, dan Matriks Invers (+ Verifikasi Kelas).

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Pemodelan Matriks SPL & Analisis 3 Jenis Solusi Eselon Baris**<br>(`Sub-CPMK-1.1 & 1.2`) | **35%** | Memodelkan masalah aliran jaringan ke matriks *augmented* tanpa cacat dan menentukan syarat batas parameter $k$ untuk solusi tunggal, tak hingga banyak solusi, serta tak konsisten secara lengkap dan tepat. | Pemodelan SPL benar dan klasifikasi 3 jenis solusi dari eselon baris tepat; hanya kurang merinci penulisan bentuk vektor parameter bebas pada 1 kasus. | Pemodelan matriks dasar benar, namun sempat melewatkan salah satu akar pembuat nol pada analisis parameter $k$ (mis. hanya menemukan 2 dari 3 kasus solusi). | Bingung membedakan baris nol penuh `[0 0 0 | 0]` (tak hingga solusi) dengan baris kontradiktif `[0 0 0 | c]` (tak ada solusi). | Gagal memodelkan SPL maupun menafsirkan bentuk eselon baris. |
| **2. Keruntutan Langkah Operasi Baris Elementer (Gauss-Jordan) & Matriks Invers**<br>(`Sub-CPMK-1.1`) | **40%** | Setiap tahap transformasi menuju `RREF` dan pencarian $[A \mid I] \to [I \mid A^{-1}]$ dilengkapi notasi operasi baris yang sah, sistematis, dan konsisten dengan hasil kuis verifikasi kelas. | Urutan OBE menuju `RREF` dan perhitungan $A^{-1}$/determinan benar dan jelas diikuti, meskipun 1–2 label operasi baris tidak ditulis eksplisit. | Memahami algoritma Gauss-Jordan dan ekspansi kofaktor, namun mengalami selip tanda minus/pecahan di tengah langkah OBE pada 1 soal. | Melakukan operasi baris ilegal (mis. mengalikan baris dengan nol atau menggunakan nilai baris yang sudah diubah pada langkah simultan yang keliru). | Hanya menuliskan matriks akhir instan tanpa langkah OBE (*indikasi menyalin kalkulator matriks*) atau memakai NIM orang lain. |
| **3. Presisi Hasil Akhir & Verifikasi Substitusi Balik ($AA^{-1}=I, Ax=b$)** | **25%** | Seluruh nilai *cosine similarity*, determinan, entri $A^{-1}$, dan solusi $x$ eksak serta disertai pembuktian perkalian balik $AA^{-1}=I$ dan $Ax=b$. | Hasil numerik tepat pada hampir seluruh butir (maks. 1 selip aritmetika ringan) dan menyertakan verifikasi substitusi. | Minimal 65% hasil akhir benar; verifikasi substitusi balik dilakukan sebagian. | Banyak kesalahan hitung pecahan sehingga $AA^{-1} \neq I$ namun dibiarkan tanpa pemeriksaan ulang. | Hasil akhir salah seluruhnya dan tanpa verifikasi. |

$$\text{Skor Tugas 1} = 0,35(K_1) + 0,40(K_2) + 0,25(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2`: `Sub-CPMK-2.1` & `2.2`)
**Objek Penilaian:** Jawaban Ujian Tertulis 150 Menit: Uji Subruang & *Span*, Kebebasan Linier, Basis & Dimensi Ruang Baris/Kolom/Nol (*Rank-Nullitas*), serta *Gram-Schmidt*.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Kaidah Formal Uji Subruang, Kombinasi Linier, & Kebebasan Linier**<br>(Soal 1 & 2 — `Sub-CPMK-2.1`) | **40%** | Membuktikan/menyangkal subruang dengan ke-3 syarat penutupan secara ketat, serta tepat menguji kombinasi linier, *span*, dan kebebasan linier melalui sistem persamaan yang sesuai. | Pengujian subruang, *span*, dan kebebasan linier tepat secara konsep dan aljabar; hanya terdapat kekuranglengkapan penulisan notasi kuantor vektor sembarang. | Mampu menguji kebebasan linier dan kombinasi linier dengan benar, namun pada uji subruang hanya memeriksa keberadaan vektor nol tanpa menguji penutupan lengkap. | Salah menyusun matriks pengujian (menaruh vektor baris padahal seharusnya vektor kolom) atau menyamakan kebebasan linier dua vektor dengan uji kelipatan untuk $>2$ vektor. | Tidak memahami definisi subruang, kombinasi linier, maupun kebebasan linier. |
| **2. Penentuan Basis, Dimensi, *Rank-Nullitas*, & Langkah *Gram-Schmidt***<br>(Soal 2, 3, & 4 — `Sub-CPMK-2.2`) | **40%** | Tepat mengekstrak basis $\text{Row}(A)$, $\text{Col}(A)$ (mengambil kolom asli $A$!), dan $\text{Null}(A)$, memverifikasi $\text{rank}+\text{nullity}=n$, serta mengeksekusi rumus proyeksi **Gram-Schmidt** secara akurat. | Penentuan ketiga basis subruang, dimensi, dan prosedur *Gram-Schmidt* benar; hanya terdapat 1 selip kecil pada skalar proyeksi $\frac{\mathbf{u}_3\cdot\mathbf{v}_2}{\|\mathbf{v}_2\|^2}$. | Memahami konsep basis, dimensi, dan *rank*, namun sempat mengambil kolom dari matriks `RREF` (bukan matriks asli $A$) saat menuliskan basis $\text{Col}(A)$. | Gagal menentukan ruang nol $Ax=\mathbf{0}$ atau salah menuliskan rumus pengurangan komponen proyeksi pada *Gram-Schmidt*. | Tidak mampu menentukan basis maupun dimensi ruang vektor. |
| **3. Presisi Vektor Akhir & Normalisasi Ortonormal** | **20%** | Seluruh vektor basis ortonormal memiliki panjang satuan ($\|\mathbf{q}_i\|=1$) dan saling tegak lurus ($\mathbf{q}_i\cdot\mathbf{q}_j=0$) secara presisi dalam bentuk akar eksak. | Perhitungan komponen vektor hampir seluruhnya benar; normalisasi panjang satuan dilakukan dengan tepat. | Langkah ortogonalisasi menghasilkan vektor tegak lurus, namun lupa membagi dengan norma $\|\mathbf{v}_i\|$ di tahap akhir normalisasi. | Banyak kesalahan hitung *dot product* sehingga vektor hasil tidak saling tegak lurus. | Perhitungan tidak tuntas atau kosong. |

$$\text{Skor UTS} = 0,40(K_1) + 0,40(K_2) + 0,20(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3`: `Sub-CPMK-3.1` & `3.2`)
**Objek Penilaian:** Studi Kasus Mandiri Berparameter NIM: Matriks Transformasi Linier, Nilai & Vektor Eigen, Diagonalisasi $PDP^{-1}$ (*Markov/PageRank*), dan Diagonalisasi Ortogonal $Q\Lambda Q^T$.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Polinomial Karakteristik, Nilai Eigen, & Basis Vektor Eigen**<br>(`Sub-CPMK-3.1`) | **35%** | Ekspansi $\det(A-\lambda I)=0$ tepat, seluruh nilai eigen terverifikasi cocok dengan $\text{tr}(A)$ & $\det(A)$, dan basis ruang eigen $(A-\lambda I)\mathbf{v}=\mathbf{0}$ ditemukan tanpa kesalahan. | Nilai eigen dan basis ruang eigen benar; hanya terdapat kekurangan minor dalam menuliskan cek jejak/determinan. | Nilai eigen ditemukan dengan benar, namun mengalami sedikit kekeliruan saat mereduksi $(A-\lambda I)\mathbf{v}=\mathbf{0}$ untuk salah satu nilai eigen. | Salah tanda saat menyusun $(A-\lambda I)$ sehingga polinomial karakteristik dan seluruh nilai eigen ikut meleset, atau menghasilkan "vektor eigen nol" $\mathbf{v}=\mathbf{0}$. | Tidak mampu menghitung nilai eigen maupun vektor eigen. |
| **2. Prosedur Diagonalisasi ($PDP^{-1}$) & Diagonalisasi Ortogonal ($Q\Lambda Q^T$)**<br>(`Sub-CPMK-3.1 & 3.2`) | **40%** | Urutan kolom $P$ dan diagonal $D$ bersesuaian presisi, perhitungan $P^{-1}$ dan $A^k = PD^kP^{-1}$ akurat, serta pada matriks simetris menyusun matriks ortogonal $Q$ ($Q^TQ=I$) secara sempurna. | Prosedur konstruksi $PDP^{-1}$ dan $Q\Lambda Q^T$ runtut dan benar; terdapat maks. 1 selip aritmetika kecil pada perkalian matriks akhir. | Berhasil menyusun $P$ dan $D$ dengan benar, namun pada matriks simetris lupa menormalisasi kolom-kolom $Q$ menjadi panjang satuan. | Menukar urutan $P^{-1}DP$ dengan $PDP^{-1}$ secara tidak konsisten atau memangkatkan elemen matriks $A$ satu per satu secara naif tanpa diagonalisasi. | Gagal melakukan diagonalisasi biasa maupun ortogonal. |
| **3. Pemodelan Komposisi Transformasi Geometri & Kondisi Tunak *Markov***<br>(`Sub-CPMK-3.2`) | **25%** | Urutan perkalian komposisi $[T_3][T_2][T_1]$ tepat (dari kanan ke kiri!), sketsa bayangan poligon akurat, dan vektor probabilitas tunak *Markov* ($\sum p_i = 1$ untuk $\lambda=1$) ditafsirkan dengan tajam. | Pemodelan transformasi dan vektor keadaan tunak *Markov* benar dengan penjelasan konteks yang jelas. | Matriks tiap transformasi tunggal benar, tetapi urutan pengalian komposisinya terbalik atau lupa menormalisasi jumlah peluang *Markov* menjadi $1$. | Salah menyusun matriks dasar rotasi/refleksi dan tidak memahami hubungan keadaan tunak *Markov* dengan $\lambda=1$. | Bagian aplikasi transformasi dan *Markov* tidak dikerjakan. |

$$\text{Skor Tugas 2} = 0,35(K_1) + 0,40(K_2) + 0,25(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4`: `Sub-CPMK-4.1` & `4.2`)
**Objek Penilaian:** Bundel *Mini-Worksheet* Python `NumPy` Murni (30%) + Jawaban Ujian Tertulis Komprehensif 150 Menit: SVD, PCA Manual, & Sintesis Ekspresi `NumPy` (70%).

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Perumusan Analitis Faktorisasi SVD ($A=U\Sigma V^T$) & Hampiran *Low-Rank***<br>(Ujian Soal 1 — `Sub-CPMK-4.1`) | **35%** | Menghitung nilai singular $\sigma_i = \sqrt{\lambda_i}$ secara berurut menurun, membangun matriks ortogonal $V$ dan $U$ dengan tanda konsisten ($A\mathbf{v}_i = \sigma_i\mathbf{u}_i$), serta menghitung matriks hampiran *rank-1* dengan presisi penuh. | Prosedur penentuan $\Sigma, V,$ dan $U$ serta hampiran *rank-1* benar; hanya terdapat kekurangan kecil saat melengkapi kolom basis ruang nol pelengkap $U$. | Mampu menghitung nilai singular $\sigma_i$ dan vektor $V$ dari $A^TA$ dengan benar, namun mengalami selip tanda/normalisasi saat menghitung $\mathbf{u}_i = \frac{1}{\sigma_i}A\mathbf{v}_i$. | Menuliskan $\sigma_i = \lambda_i$ (lupa mengakarkan!) atau mencampuradukkan SVD matriks persegi panjang dengan diagonalisasi biasa. | Tidak mampu merumuskan faktorisasi SVD secara analitis. |
| **2. Penurunan Matematis Kovarians, Proyeksi PCA, & *Explained Variance***<br>(Ujian Soal 2 — `Sub-CPMK-4.1 & 4.2`) | **35%** | Melakukan *mean-centering* $\tilde{X}$ dengan tepat, menghitung matriks kovarians $S$, menemukan vektor satuan PC1, memproyeksikan data $Z=\tilde{X}\mathbf{w}_1$, dan menghitung persentase *explained variance* secara akurat. | Lima langkah perhitungan manual PCA dilakukan secara runtut dan benar dengan maks. 1 selip hitung desimal ringan. | Memahami alur kovarians ke vektor eigen utama dan rasio variansi, namun sempat lupa mengurangi kolom data dengan rata-ratanya (*mean-centering*) di langkah pertama. | Menghitung nilai eigen dari matriks data mentah tak bujursangkar secara keliru tanpa membentuk matriks kovarians atau SVD. | Gagal menurunkan langkah matematis PCA. |
| **3. Komputasi Matriks Python `NumPy` Murni & Konsistensi Sintesis Ujian**<br>(*Worksheet* + Ujian Soal 3 — `Sub-CPMK-4.2`) | **30%** | Kode *Mini-Worksheet* bersih 100% menggunakan operasi matriks `NumPy` (`@`, `svd`/`eigh`, bebas `scikit-learn`), analisis galat kompresi/reduksi tajam, **dan** mampu menulis/menjelaskan ulang ekspresi `NumPy` dengan akurat saat ujian tertulis di kelas. | Implementasi `NumPy` berjalan akurat sesuai *guardrail* dan jawaban penelusuran kode pada ujian tertulis konsisten baik. | *Mini-Worksheet* `NumPy` berfungsi untuk kasus dasar dan mahasiswa memahami fungsi utama `np.linalg.svd` saat ujian tertulis, walau masih memakai `for-loop` yang kurang ter-vektorisasi. | Terdapat ketidaksesuaian mencolok antara kualitas kode *worksheet* dengan ketidakmampuan menjelaskan baris `NumPy` dasar saat ujian luring, atau sempat memakai fungsi terlarang di luar `NumPy`. | Tidak mengumpulkan *worksheet* `NumPy`, menyalin kode rekan, atau melanggar integritas akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,30(K_3)$$

---

## BAGIAN III — RUBRIK FORMATIF PENYELESAIAN MATRIKS DI KELAS & KLINIK `NUMPY`

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Disiplin Pemeriksaan Dimensi Matriks (*Shape Sanity Check*)** | Selalu memeriksa kecocokan ukuran $(m\times k)(k\times n) \to (m\times n)$ sebelum mengalikan atau menulis ekspresi `NumPy`. | Jarang melakukan kesalahan dimensi dan mampu mengoreksi sendiri saat diingatkan. | Kadang mencoba mengalikan dua matriks yang dimensinya tidak selaras (lupa transpos `.T`). | Tidak memperhatikan ukuran baris dan kolom matriks sama sekali. |
| **Kebiasaan Verifikasi Invarian Aljabar** | Secara otomatis mengecek $AA^{-1}=I$, $\mathbf{q}_i\cdot\mathbf{q}_j=0$, dan $\sum\lambda_i = \text{tr}(A)$ untuk memastikan hasil hitungannya bebas galat. | Melakukan cek verifikasi akhir pada sebagian besar latihan soal. | Berhenti segera setelah memperoleh angka tanpa mengecek apakah sifat matriks terpenuhi. | Tidak memahami cara memverifikasi kebenaran solusi matriks. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat Capaian | Deskriptor Integratif Penguasaan `STI-205` (`CPL-05` / `P1` — Level *Introduce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai secara utuh dan mendalam penyelesaian SPL, struktur formal ruang vektor $\mathbb{R}^n$, spektrum nilai/vektor eigen & diagonalisasi, serta mampu menurunkan dan mengimplementasikan sendiri SVD dan PCA murni menggunakan operasi matriks `NumPy` untuk pemrosesan data AI. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa terampil mengeksekusi Gauss-Jordan, menganalisis kebebasan linier/basis/dimensi/*Gram-Schmidt*, menghitung diagonalisasi matriks, serta merumuskan SVD dan PCA dengan akurat baik di atas kertas maupun dengan `NumPy`. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam menyelesaikan SPL, menentukan basis ruang vektor dasar, menghitung nilai/vektor eigen standar, serta mengikuti prosedur SVD dan PCA berbantuan `NumPy`. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih sering keliru dalam operasi baris elementer, bingung membedakan konsep basis/dimensi/*rank*, dan belum mampu merangkai langkah nilai eigen menuju dekomposisi SVD/PCA. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai operasi dasar matriks dan ruang vektor atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20 & DOK 033)

**Skala Persepsi:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-205` | Rujukan Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menyelesaikan Sistem Persamaan Linear (SPL) menggunakan eliminasi Gauss-Jordan dan matriks invers secara teliti. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menentukan apakah suatu SPL memiliki solusi tunggal, tak hingga banyak solusi, atau tidak ada solusi dari bentuk eselon baris. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu menganalisis subruang, kombinasi linier, rentang (*span*), dan kebebasan linier himpunan vektor. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menentukan basis, dimensi, *rank* matriks, serta membentuk basis ortonormal dengan proses *Gram-Schmidt* pada $\mathbb{R}^n$. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu menghitung polinomial karakteristik, nilai eigen, vektor eigen, dan mendiagonalisasi matriks. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menyusun matriks transformasi linier dan menerapkan diagonalisasi pada transisi berulang (*Markov/PageRank*). | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu merumuskan secara matematis faktorisasi *Singular Value Decomposition* (SVD) dan hampiran *low-rank*. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu menurunkan langkah matematis PCA dan menerapkannya menggunakan operasi matriks Python `NumPy` untuk mereduksi dimensi data AI. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-205`)

```text
========================================================================================================================
                 LEMBAR REKAPITULASI PENILAIAN OBE — STI-205 ALJABAR LINEAR DAN MATRIKS (3 SKS TEORI)
========================================================================================================================
Semester / Tahun Akademik : Semester 2 (Genap) / 2026-2027            CPL Dibebankan : CPL-05 (P1) [Level: Introduce]
Klaster Rubrik            : K-1 (Sains Dasar & Teori Formal)          Ambang OBE     : >= 65.0 (Target Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------
No | NIM        | Nama Mahasiswa     | Tugas 1 (20%) | UTS (30%)     | Tugas 2 (20%) | UAS (30%)     | Nilai | Huruf | OBE
   |            |                    | [CPMK-1: C3]  | [CPMK-2: C4]  | [CPMK-3: C3]  | [CPMK-4: C4]  | Akhir | Mutu  | >=65
------------------------------------------------------------------------------------------------------------------------
1  | 260101001  | [Nama Mhs 1]       | 86.0          | 84.0          | 85.0          | 88.0          | 85.80 | A     | YA
2  | 260101002  | [Nama Mhs 2]       | 76.0          | 72.0          | 74.0          | 75.0          | 74.10 | B     | YA
3  | 260101003  | [Nama Mhs 3]       | 68.0          | 66.0          | 68.0          | 70.0          | 68.00 | C+    | YA
------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS PER KOMPONEN         | 76.67         | 74.00         | 75.67         | 77.67         | 75.97 | % >=65: 100%
========================================================================================================================
```
