# SATUAN ACARA PERKULIAHAN (SAP)

## STI-205 — ALJABAR LINEAR DAN MATRIKS
### *Linear Algebra and Matrices*

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Semester:** 2 (Genap) | **Bobot:** 3 SKS Teori | **Pertemuan:** 16 pekan
> **Dokumen induk:** `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`
> **Tanggal:** 07 November 2026

---

## 1. IDENTITAS DAN KEDUDUKAN DOKUMEN

| Atribut | Keterangan |
|---|---|
| Nama MK / Kode | Aljabar Linear dan Matriks / `STI-205` |
| Rumpun MK | Matematika & Sains Komputasi (Core STI) |
| Prasyarat | `STI-102` Kalkulus |
| Dosen Pengampu | Tim Pengampu Rumpun Matematika & Sains Komputasi |
| Hari / Jam | Sesuai jadwal akademik fakultas |
| Ruang | Kelas teori (kapasitas ≥ 40 mahasiswa) |
| Media utama | LCD proyektor, papan tulis, LMS (Edlink/Moodle), Python + NumPy (notebook daring pada perangkat mahasiswa) |
| Alokasi waktu | TM 150′/pekan; PT 180′/pekan; BM 180′/pekan |
| Fungsi dokumen | Menjabarkan RPS menjadi rencana operasional tiap pertemuan (kegiatan, media, waktu, penilaian) |

**Kedudukan dalam rantai dokumen:** RPS (055_1) → **SAP (055_2)** → Buku Modul (055_3) → Rencana Evaluasi (055_4) → Rubrik (055_5). SAP tidak boleh menyimpang dari RPS; seluruh Sub-CPMK, materi, dan titik asesmen mengikuti RPS dan Dokumen 043.

**Catatan prasyarat:** `STI-102` Kalkulus dibutuhkan sebagai bekal **manipulasi aljabar elementer dan pengertian fungsi** yang dipakai dalam transformasi linier serta dalam pemahaman limit/turunan pada penurunan PCA (pekan 10). SAP ini **tidak** mengulang materi kalkulus sesuai pagar *Out-of-Scope* Dokumen 043.

---

## 2. CAPAIAN DAN INDIKATOR RINGKAS

| Kode | Rumusan | Bloom | Pekan Pencapaian | Instrumen Ukur |
|:---:|---|:---:|:---:|---|
| CPMK-1 | Menyelesaikan SPL dengan eliminasi Gauss–Jordan dan matriks invers | C3 | 2–3, 8 | Tugas 1, UTS |
| CPMK-2 | Menganalisis struktur ruang vektor, kombinasi/kebebasan linier, basis, dan dimensi pada $\mathbb{R}^n$ | C4 | 4–5, 8 | Tugas 1, UTS |
| CPMK-3 | Menghitung nilai eigen, vektor eigen, dan diagonalisasi matriks transformasi linier | C3 | 6–7, 8, 12, 16 | UTS, Tugas 2, UAS |
| CPMK-4 | Merumuskan SVD dan reduksi dimensi PCA menggunakan Python NumPy | C4 | 9–11, 12, 16 | Tugas 2, UAS |

**Indikator kinerja kunci (IKK):**

1. ≥ 80% mahasiswa mampu menyelesaikan SPL dengan OBE hingga bentuk eselon tereduksi tanpa kekeliruan prosedural.
2. ≥ 75% mahasiswa mampu mengklasifikasikan jenis solusi SPL (tunggal, tak hingga, tak ada) dengan justifikasi rank.
3. ≥ 75% mahasiswa mampu menguji kombinasi linier, kebebasan linier, serta menentukan basis dan dimensi dengan benar.
4. ≥ 70% mahasiswa mampu menghitung nilai eigen, vektor eigen, dan melakukan diagonalisasi beserta verifikasinya.
5. ≥ 70% mahasiswa mampu merumuskan SVD dan mengimplementasikan PCA dengan NumPy, serta menginterpretasikan *explained variance*.
6. Rata-rata ketercapaian CPL-05 (P1) dari MK ini ≥ 65,0 (ambang Dokumen 008).

---

## 3. MATRIKS JADWAL PERKULIAHAN

| Pekan | Sub-CPMK | Pokok Bahasan | Metode | Asesmen |
|:--:|---|---|---|---|
| 1 | Orientasi | Ruang lingkup, kontrak belajar, peta CPL–CPMK, vektor di $\mathbb{R}^n$ | Kuliah interaktif | Formatif |
| 2 | 1.1 | Matriks, operasi matriks, transpose, matriks diperbesar, OBE | Kuliah + latihan terbimbing | Formatif (kuis LMS) |
| 3 | 1.2 | Bentuk eselon baris, jenis solusi, determinan, Cramer, invers | Ceramah + latihan terstruktur | Formatif |
| 4 | 2.1 | Aksioma ruang vektor, subruang, kombinasi linier, span | Case-based learning | **Tugas 1 (20%)** |
| 5 | 2.2 | Kebebasan linier, basis, dimensi, rank, Gram–Schmidt | Kuliah + latihan bertingkat | Formatif |
| 6 | 3.1 | Transformasi linier, kernel & range, polinomial karakteristik, eigen | Ceramah & latihan | Formatif (kuis) |
| 7 | 3.2 | Diagonalisasi, multiplisitas, matriks simetris, teorema spektral | Case method | Formatif (studi kasus) |
| 8 | — | **UTS** (CPMK-1, 2, 3) | Ujian tertulis | **UTS (30%)** |
| 9 | 4.1 | Nilai singular, SVD $A = U\Sigma V^T$, aproksimasi rank-$k$ | Ceramah & derivasi bersama | Formatif |
| 10 | 4.2 | Standarisasi, kovarians, PCA via NumPy, explained variance | Demo & praktik komputasi | Formatif (notebook) |
| 11 | 4.3 | Studi kasus reduksi dimensi & kompresi matriks | PjBL / case method | Formatif (konsultasi) |
| 12 | 4.4 | Proyek terapan lanjut & presentasi antara | PjBL / presentasi | **Tugas 2 (20%)** |
| 13 | Semua | Penyempurnaan proyek | PjBL / konsultasi | Formatif (checklist) |
| 14 | Semua | Review & konsolidasi | Diskusi / konsultasi | Formatif |
| 15 | Semua | Presentasi final | Presentasi | Formatif (rubrik presentasi) |
| 16 | — | **UAS** (komprehensif) | Ujian tertulis | **UAS (30%)** |

---

## 4. RINCIAN KEGIATAN PER PERTEMUAN

### Pertemuan 1 — Orientasi, Kontrak Belajar, dan Vektor di $\mathbb{R}^n$

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Orientasi (fondasi CPMK-1) |
| Indikator | Mahasiswa mampu menjelaskan ruang lingkup MK, capaian pembelajaran, dan skema asesmen |
| Materi | Ruang lingkup aljabar linear untuk komputasi cerdas; peta CPL-05 (P1) → CPMK-1..4 → Sub-CPMK; skema 4 titik asesmen; aturan akademik & etika AI; vektor di $\mathbb{R}^n$, operasi vektor, *dot product*, norma, jarak Euclidean, sudut antar-vektor |
| Metode | Kuliah interaktif, tanya-jawab, diagnostik awal |
| Media | Slide pengantar, kontrak belajar, LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** salam, presensi, apersepsi "mengapa gambar dan suara bisa dipadatkan tanpa terlihat rusak?". **Inti (120′):** (1) pemaparan ruang lingkup & capaian 30′; (2) skema asesmen & bobot 20′; (3) kontrak belajar & etika AI 20′; (4) vektor, dot product, norma 35′; (5) tes diagnostik 15′. **Penutup (15′):** rangkuman, penugasan membaca [1] Bab 1 & 6, pengarahan unduh materi LMS |
| Penilaian | Formatif — tes diagnostik (non-graded), kehadiran & partisipasi |
| Referensi | [1] Bab 1 & 6; [2] Bab 1 |

### Pertemuan 2 — Matriks, Operasi Matriks, dan Eliminasi Gauss–Jordan

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-1.1** |
| Indikator | 1.1.1 Ketepatan operasi matriks & OBE; 1.1.2 Ketepatan langkah Gauss–Jordan hingga bentuk eselon tereduksi |
| Materi | Notasi matriks dan ukuran; penjumlahan, perkalian skalar, perkalian matriks; transpose dan sifatnya; matriks identitas, segitiga, diagonal; matriks diperbesar (*augmented matrix*); tiga Operasi Baris Elementer (OBE); eliminasi Gauss; eliminasi Gauss–Jordan; bentuk eselon baris dan bentuk eselon baris tereduksi |
| Metode | Kuliah & latihan terbimbing |
| Media | Slide, papan tulis, lembar latihan OBE |
| **Kegiatan (150′)** | **Pendahuluan (15′):** review tugas baca, pertanyaan pemantik "bagaimana komputer menyelesaikan ribuan persamaan sekaligus?". **Inti (120′):** (1) operasi matriks & transpose 30′; (2) matriks diperbesar & tiga OBE 25′; (3) eliminasi Gauss 30′; (4) Gauss–Jordan hingga eselon tereduksi 35′. **Penutup (15′):** rangkuman, kuis formatif LMS, penugasan 4 SPL |
| Penilaian | Formatif — kuis LMS (non-graded), observasi latihan |
| Referensi | [1] Bab 1–2; [3] Bab 1 |

### Pertemuan 3 — Jenis Solusi SPL, Determinan, dan Invers Matriks

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-1.2** |
| Indikator | 1.2.1 Ketepatan klasifikasi solusi (tunggal/tak hingga/tak ada); 1.2.2 Ketepatan determinan & invers |
| Materi | Variabel bebas dan variabel terikat; teorema keberadaan–ketunggalan solusi; rank matriks koefisien vs rank matriks diperbesar (Rouché–Capelli); SPL homogen dan ruang solusinya; determinan: definisi kofaktor, sifat-sifat, determinan matriks segitiga; aturan Cramer; invers matriks: metode adjoin dan metode OBE; hubungan $\det(A) \ne 0 \iff A$ invertibel |
| Metode | Ceramah interaktif + latihan terstruktur |
| Media | Slide, papan tulis, bank soal SPL di LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** kaitkan hasil eselon pertemuan 2 dengan jumlah solusi. **Inti (120′):** (1) klasifikasi solusi & rank 30′; (2) determinan & sifatnya 30′; (3) aturan Cramer 20′; (4) invers via adjoin dan OBE + verifikasi 40′. **Penutup (15′):** rangkuman, penugasan membaca [1] Bab 2–3 |
| Penilaian | Formatif — lembar latihan terstruktur |
| Referensi | [1] Bab 2–3; [8] Bab 1 |

### Pertemuan 4 — Ruang Vektor, Subruang, Kombinasi Linier, dan Span  ⟶ **TUGAS 1 (20%)**

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-2.1** |
| Indikator | 2.1.1 Ketepatan uji kombinasi linier; 2.1.2 Ketepatan penentuan span & subruang |
| Materi | Aksioma ruang vektor riil (10 aksioma); contoh ruang vektor ($\mathbb{R}^n$, ruang matriks, ruang polinomial); subruang dan tiga syarat ujinya; kombinasi linier; rentang (*span*) dan himpunan perentang; hubungan span dengan SPL (kapan $\mathbf{b} \in \mathrm{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$) |
| Metode | Case-based learning, kerja individu terpandu |
| Media | Slide, formulir Tugas 1, lembar uji subruang |
| **Kegiatan (150′)** | **Pendahuluan (15′):** pengantar asesmen Tugas 1. **Inti (120′):** (1) aksioma & contoh ruang vektor 25′; (2) uji subruang 25′; (3) kombinasi linier & span 35′; (4) pengerjaan Tugas 1 di kelas 35′. **Penutup (15′):** pengumpulan, penjelasan revisi, penugasan lanjutan |
| Penilaian | **Sumatif — Tugas 1 (20%)**, rubrik 4 dimensi (055_5) |
| Referensi | [1] Bab 4; [2] Bab 3 |

### Pertemuan 5 — Kebebasan Linier, Basis, Dimensi, dan Gram–Schmidt

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-2.2** |
| Indikator | 2.2.1 Ketepatan uji kebebasan linier; 2.2.2 Ketepatan penentuan basis, dimensi, dan Gram–Schmidt |
| Materi | Definisi kebebasan linier dan ketergantungan linier; uji kebebasan melalui SPL homogen; basis dan sifat ketunggalan representasi; dimensi; basis standar $\mathbb{R}^n$; ruang baris, ruang kolom, dan rank; teorema rank–nullity; ruang hasil kali dalam, ortogonalitas, proyeksi; proses ortogonalisasi Gram–Schmidt |
| Metode | Kuliah & latihan bertingkat |
| Media | Slide, papan tulis, lembar latihan bertingkat |
| **Kegiatan (150′)** | **Pendahuluan (15′):** refleksi Tugas 1, pertanyaan "berapa vektor minimum untuk membangun ruang?". **Inti (120′):** (1) kebebasan & ketergantungan linier 30′; (2) basis & dimensi 30′; (3) rank–nullity 20′; (4) Gram–Schmidt 40′. **Penutup (15′):** rangkuman, penugasan membaca [3] Bab 4–5 |
| Penilaian | Formatif — lembar latihan bertingkat |
| Referensi | [1] Bab 4 & 6; [3] Bab 4–5 |

### Pertemuan 6 — Transformasi Linier, Kernel, Range, dan Nilai Eigen

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-3.1** |
| Indikator | 3.1.1 Ketepatan polinomial karakteristik; 3.1.2 Ketepatan penentuan ruang eigen |
| Materi | Definisi transformasi linier dan sifat kelinearan; matriks representasi terhadap basis standar; kernel dan range; teorema dimensi untuk transformasi linier; nilai eigen dan vektor eigen sebagai vektor tak nol yang dipertahankan arahnya; persamaan karakteristik $\det(A - \lambda I) = 0$; polinomial karakteristik; ruang eigen (*eigenspace*) |
| Metode | Ceramah & latihan terstruktur |
| Media | Slide, papan tulis, lembar latihan eigen di LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "apa yang tidak berubah saat sebuah transformasi diterapkan?". **Inti (120′):** (1) transformasi linier & matriks representasi 30′; (2) kernel & range 20′; (3) persamaan karakteristik 30′; (4) latihan eigen 2×2 dan 3×3 40′. **Penutup (15′):** rangkuman, penugasan membaca [8] Bab 7 |
| Penilaian | Formatif — lembar latihan eigen |
| Referensi | [1] Bab 5; [8] Bab 7 |

### Pertemuan 7 — Diagonalisasi dan Matriks Simetris

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-3.2** |
| Indikator | 3.2.1 Ketepatan syarat diagonalisasi; 3.2.2 Ketepatan diagonalisasi matriks simetris |
| Materi | Matriks similar dan sifat invariannya (determinan, trace, polinomial karakteristik); syarat cukup diagonalisasi ($n$ vektor eigen bebas linier); multiplisitas aljabar vs geometrik; matriks simetris riil dan ortogonalitas vektor eigen; teorema spektral (pengantar); dekomposisi $A = PDP^{-1}$ dan $A = PDP^T$ untuk matriks simetris; penerapan pada perhitungan pangkat matriks dan sistem dinamik diskret |
| Metode | Case method |
| Media | Slide, studi kasus diagonalisasi, lembar kerja |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "mengapa pangkat matriks ke-1000 bisa dihitung cepat?". **Inti (120′)** (1) similaritas & invarian 25′; (2) syarat & prosedur diagonalisasi 35′; (3) kasus gagal didiagonalkan 20′; (4) matriks simetris & teorema spektral 40′. **Penutup (15′):** sintesis, penugasan membaca [2] Bab 6 |
| Penilaian | Formatif — lembar kerja diagonalisasi |
| Referensi | [1] Bab 5 & 7; [2] Bab 6 |

### Pertemuan 8 — Evaluasi Tengah Semester (UTS)  ⟶ **UTS (30%)**

| Komponen | Uraian |
|---|---|
| Cakupan | CPMK-1, CPMK-2, CPMK-3 (tahap awal) — materi pekan 1–7 |
| Bentuk | Bagian I SPL/OBE/determinan/invers (30); II ruang vektor/basis/dimensi (35); III eigen & diagonalisasi (25); IV studi kasus pemodelan matriks (10) |
| Durasi | 150 menit, *closed book* |
| Pengawasan | Dosen + 1 pengawas; tata tertib ujian fakultas |
| Penilaian | Rubrik UTS (055_5), kunci jawaban terstandar |
| Tindak lanjut | Analisis butir soal; pengumuman nilai ≤ 7 hari; remedial sesuai kebijakan prodi |

### Pertemuan 9 — Nilai Singular dan Dekomposisi SVD

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.1** |
| Indikator | 4.1.1 Ketepatan langkah SVD; 4.1.2 Ketepatan interpretasi nilai singular & rank |
| Materi | Keterbatasan diagonalisasi untuk matriks tak persegi dan matriks tak terdiagonalkan; matriks $A^TA$ dan $AA^T$; nilai singular $\sigma_i = \sqrt{\lambda_i(A^TA)}$; vektor singular kiri dan kanan; dekomposisi $A = U\Sigma V^T$; bentuk *full* vs *reduced* SVD; rank dan rank terpotong; teorema Eckart–Young dan aproksimasi rank-$k$; hubungan SVD dengan norma spektral dan norma Frobenius |
| Metode | Ceramah & derivasi bersama |
| Media | Slide, papan tulis, video + lembar derivasi di LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** refleksi UTS & rencana perbaikan; "bagaimana satu matriks bisa diringkas menjadi tiga?". **Inti (120′)** (1) motivasi & keterbatasan eigen 20′; (2) nilai singular dari $A^TA$ 30′; (3) konstruksi $U$, $\Sigma$, $V$ 40′; (4) aproksimasi rank-$k$ 30′. **Penutup (15′):** rangkuman, penugasan membaca [4] Bab 2 |
| Penilaian | Formatif — lembar derivasi SVD |
| Referensi | [4] Bab 2; [5] Bab 10 |

### Pertemuan 10 — PCA dengan Python NumPy

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.2** |
| Indikator | 4.2.1 Ketepatan alur PCA; 4.2.2 Ketepatan interpretasi varians terjelaskan |
| Materi | Motivasi reduksi dimensi; standarisasi (z-score) dan sensitivitas skala; matriks kovarians dan sifat semidefinit positif; dua jalur ekuivalen PCA (eigen-dekomposisi kovarians vs SVD matriks data terpusat); komponen utama; *explained variance ratio*; *scree plot*; pemilihan jumlah komponen; rekonstruksi dan galat rekonstruksi; implementasi `numpy.linalg.svd`, `numpy.cov`, `numpy.mean`, `numpy.std` |
| Metode | Demo & praktik komputasi terpandu |
| Media | Proyektor, notebook NumPy di LMS, perangkat mahasiswa |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "mengapa 784 kolom piksel bisa diringkas jadi 50 angka?". **Inti (120′)** (1) standarisasi & kovarians 25′; (2) PCA via SVD dengan NumPy 45′; (3) explained variance & scree plot 25′; (4) latihan mandiri terpandu 25′. **Penutup (15′):** rangkuman, penugasan notebook |
| Penilaian | Formatif — notebook latihan (jalankan & interpretasi) |
| Referensi | [5] Bab 10; [7] |

### Pertemuan 11 — Studi Kasus Reduksi Dimensi dan Kompresi Matriks

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.3** (penguatan CPMK-3 & CPMK-4) |
| Indikator | 4.3.1 Ketepatan pemilihan jumlah komponen; 4.3.2 Ketepatan justifikasi *trade-off* |
| Materi | Studi kasus terpadu: (a) reduksi indikator kinerja akademik menjadi 2–3 komponen; (b) kompresi citra *grayscale* dengan SVD rank-$k$; (c) analisis *trade-off* antara rasio kompresi, galat rekonstruksi, dan biaya komputasi; (d) jebakan: standarisasi yang salah, kebocoran informasi uji ke pelatihan, interpretasi komponen yang berlebihan |
| Metode | PjBL & case method |
| Media | Slide, template laporan, konsultasi asinkron |
| **Kegiatan (150′)** | **Pendahuluan (15′):** pengantar tugas proyek & pengelompokan. **Inti (120′)** (1) pembahasan tiga kasus 40′; (2) pembentukan kelompok & pemilihan tema 20′; (3) penyusunan draf formulasi 40′; (4) konsultasi 20′. **Penutup (15′):** tenggat draf, arahan lanjutan |
| Penilaian | Formatif — draf formulasi aljabar |
| Referensi | [5]; [4] |

### Pertemuan 12 — Proyek Terapan dan Presentasi Antara  ⟶ **TUGAS 2 (20%)**

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.4** (integrasi 4.1 & 4.2) |
| Indikator | 4.4.1 Kelayakan model aljabar; 4.4.2 Kejelasan argumentasi kuantitatif |
| Materi | Presentasi progres proyek: formulasi matriks, standarisasi, SVD/PCA, dua eksperimen parameter, visualisasi, analisis galat |
| Metode | PjBL & presentasi |
| Media | Proyektor, timer, lembar penilaian presentasi |
| **Kegiatan (150′)** | **Pendahuluan (15′):** tata tertib presentasi & rubrik. **Inti (120′):** 4 kelompok × 25′ (15′ presentasi + 10′ tanya jawab & umpan balik). **Penutup (15′):** umpan balik menyeluruh, arahan revisi |
| Penilaian | **Sumatif — Tugas 2 (20%)**, rubrik 4 dimensi (055_5) |
| Referensi | [1]; [5] |

### Pertemuan 13 — Penyempurnaan Proyek

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK (penyempurnaan) |
| Indikator | 4.4.3 Ketepatan revisi; 4.4.4 Kualitas dokumentasi |
| Materi | Revisi berdasarkan umpan balik: kelengkapan formulasi, kebenaran implementasi NumPy, verifikasi manual pada sampel kecil, penajaman visualisasi, analisis keterbatasan |
| Metode | PjBL & konsultasi klinis |
| Media | Lembar konsultasi, repositori dokumen kelompok |
| **Kegiatan (150′)** | **Pendahuluan (15′):** rekap umpan balik agregat. **Inti (120′):** konsultasi bergilir per kelompok 15′ × 8, diselingi kerja mandiri kelompok. **Penutup (15′):** kesepakatan tenggat final |
| Penilaian | Formatif — checklist revisi |
| Referensi | Seluruh materi CPMK-3 & CPMK-4 |

### Pertemuan 14 — Review dan Konsolidasi

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK |
| Indikator | Ketepatan identifikasi kesenjangan pemahaman |
| Materi | Rekapitulasi pekan 1–13; peta konsep terpadu vektor → matriks → SPL → ruang vektor → transformasi → eigen → SVD → PCA; pembahasan soal terpilih |
| Metode | Diskusi & konsultasi |
| Media | Peta konsep besar, bank soal terpilih |
| **Kegiatan (150′)** | **Pendahuluan (15′):** penjelasan mekanisme review. **Inti (120′)** (1) penyusunan peta konsep bersama 40′; (2) pembahasan 8 soal kunci 50′; (3) tanya-jawab terbuka 30′. **Penutup (15′):** arahan UAS, penegasan cakupan |
| Penilaian | Formatif — partisipasi |
| Referensi | Rekapitulasi pekan 1–13 |

### Pertemuan 15 — Presentasi Final

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK |
| Indikator | 4.4.5 Kualitas komunikasi teknis; 4.4.6 Penguasaan saat tanya jawab |
| Materi | Presentasi hasil akhir proyek: formulasi, implementasi, hasil eksperimen, visualisasi, keterbatasan, kesimpulan |
| Metode | Presentasi tim & pleno |
| Media | Proyektor, timer, lembar penilaian |
| **Kegiatan (150′)** | **Pendahuluan (15′):** tata tertib. **Inti (120′):** 4 kelompok × 25′ (15′ presentasi + 10′ tanya jawab). **Penutup (15′):** apresiasi, arahan UAS |
| Penilaian | Formatif — rubrik presentasi (masuk komponen proses) |
| Referensi | Seluruh materi |

### Pertemuan 16 — Evaluasi Akhir Semester (UAS)  ⟶ **UAS (30%)**

| Komponen | Uraian |
|---|---|
| Cakupan | Komprehensif CPMK-1 s.d. CPMK-4 |
| Bentuk | I SPL/matriks/determinan/invers (20); II ruang vektor/basis/ortogonalitas (25); III eigen/diagonalisasi/SVD (30); IV pemodelan terbuka (25) |
| Durasi | 150 menit, *closed book* |
| Penilaian | Rubrik UAS (055_5) |
| Tindak lanjut | Rekap nilai akhir, analisis ketercapaian CPMK/CPL, input SIAKAD ≤ 7 hari |

---

## 5. LEMBAR MONITORING PELAKSANAAN

| Pekan | Tanggal | Materi Terlaksana | Jumlah Hadir | Catatan Kejadian | Paraf Dosen |
|:--:|---|---|:--:|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |
| 13 | | | | | |
| 14 | | | | | |
| 15 | | | | | |
| 16 | | | | | |

---

## 6. CATATAN PELAKSANAAN DAN RENCANA KONTINGENSI

1. **Kehadiran minimum:** 75% dari 16 pertemuan (12 pertemuan) sebagai syarat mengikuti UAS.
2. **Pertemuan pengganti:** diselenggarakan jika terjadi hari libur nasional atau kegiatan fakultas, dengan materi setara dan bukti dokumentasi.
3. **Pembelajaran daring darurat:** seluruh materi tersedia di LMS; sesi sinkron melalui konferensi video dengan rekaman wajib diunggah.
4. **Keterbatasan laboratorium:** MK ini bertipe Teori (P = 0). Sesi komputasi NumPy pada pekan 10–13 dilaksanakan dengan **notebook daring** (Google Colab/JupyterLite) pada perangkat mahasiswa; tidak memerlukan lab terjadwal.
5. **Kebutuhan komputasi:** NumPy bersifat ringan dan tersedia gratis. Mahasiswa tanpa perangkat memadai dapat menggunakan komputer laboratorium fakultas pada jam layanan atau berpasangan dengan persetujuan dosen.
6. **Mahasiswa dengan kebutuhan khusus:** penyesuaian waktu asesmen dan format materi (sesuai kebijakan layanan disabilitas universitas).
7. **Integritas akademik:** setiap tugas wajib menyertakan Deklarasi Transparansi AI; dosen berhak melakukan verifikasi lisan 3 menit, termasuk meminta mahasiswa menjalankan ulang satu langkah OBE atau satu baris kode NumPy.
8. **Umpan balik:** hasil asesmen dikembalikan maksimal 7 hari kerja dengan komentar per dimensi rubrik.
9. **Kalkulator:** diperbolehkan pada latihan dan Tugas 1/Tugas 2 untuk verifikasi aritmetika, **tidak** pada UTS/UAS dan tidak untuk menggantikan langkah OBE.

---

*Dokumen ini merupakan penjabaran operasional dari `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` dan konsisten dengan Dokumen 043 (Sub-CPMK & Boundary Guardrails).*
