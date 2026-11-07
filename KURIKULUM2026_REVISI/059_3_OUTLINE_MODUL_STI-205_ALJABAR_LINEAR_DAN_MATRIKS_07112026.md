# OUTLINE BUKU MODUL PEMBELAJARAN
## STI-205 — ALJABAR LINEAR DAN MATRIKS

> **Jenis dokumen:** Kerangka (*outline*) buku modul ajar yang diturunkan dari RPS
> **Dokumen induk:** `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`
> **Rujukan kurikulum:** Dokumen 005, 007, 043 (Sub-CPMK & Boundary Guardrails), 003 (CPL)
> **Tanggal:** 07 November 2026

---

## 1. METADATA MODUL

| Atribut | Keterangan |
|---|---|
| Judul modul | *Aljabar Linear dan Matriks: dari Sistem Persamaan Linier hingga SVD dan PCA* |
| Kode MK | `STI-205` |
| Penulis | Tim Pengampu Rumpun Matematika & Sains Komputasi (Core STI) |
| Penelaah | Koordinator RMK Matematika & Sains Komputasi; Unit Penjaminan Mutu FSTI |
| Jenjang / Semester | S1 / Semester 2 |
| Bobot | 3 SKS Teori (TM 150′ + PT 180′ + BM 180′ per pekan) |
| Prasyarat | `STI-102` Kalkulus |
| Target pembaca | Mahasiswa S1 SISTEKIN tahun pertama; dosen pengampu; asisten tutorial |
| Estimasi tebal | 240–280 halaman A5 (atau 185–215 halaman A4) |
| Bahasa | Indonesia, dengan istilah teknis Inggris dalam tanda kurung miring |
| Bentuk | Buku modul cetak + e-modul (PDF interaktif dengan notebook NumPy yang dapat dijalankan) |
| Status ISBN | Dalam pengajuan Perpustakaan Nasional RI |
| Edisi | Edisi 1 (2027) |

---

## 2. DASAR DAN BATAS PENYUSUNAN

| Aspek | Ketentuan |
|---|---|
| Sumber capaian | CPMK-1 s.d. CPMK-4 dan Sub-CPMK-1.1 s.d. 4.2 dari Dokumen 043 |
| Sumber materi | Pokok bahasan Tabel 10.C Dokumen 007 dan BoK `BK-IS10`, `BK-IT02` |
| Batas isi (*in-scope*) | SPL, eliminasi Gauss–Jordan, aljabar matriks, vektor ruang $\mathbb{R}^n$, determinan, invers, nilai eigen dan vektor eigen, dekomposisi PCA dasar |
| Batas larangan (*out-of-scope*) | Pelatihan algoritma *machine learning* (scikit-learn/tensorflow) → `STI-413`; pengodean aplikasi web → `STI-416`; analisis limit–diferensial–integral kalkulus → `STI-102` |
| Titik serah terima | Pemodelan *machine learning* tabular → `STI-413`; *deep learning* → `STI-624`; kalkulus → `STI-102` |

> **Catatan rujukan kode:** Dokumen 043 menulis titik serah terima *deep learning* sebagai `STI-726`. Menurut Dokumen 005, MK *deep learning* Semester 6 berkode **`STI-624`**; `STI-726` adalah MK Semester 7. Dokumen ini memakai `STI-624`; ketidaksesuaian Dokumen 043 telah dicatat sebagai temuan terbuka (kode ganda `STI-726`/`STI-727`).

---

## 3. CAPAIAN MODUL

Setelah menuntaskan modul ini, mahasiswa mampu:

1. **Menyelesaikan** Sistem Persamaan Linear (SPL) menggunakan eliminasi Gauss–Jordan dan matriks invers secara tepat (CPMK-1, C3).
2. **Menganalisis** struktur ruang vektor, kombinasi linier, kebebasan linier, basis, dan dimensi pada ruang $\mathbb{R}^n$ dengan kaidah aljabar formal (CPMK-2, C4).
3. **Menghitung** nilai eigen, vektor eigen, dan diagonalisasi matriks pada matriks transformasi linier secara presisi (CPMK-3, C3).
4. **Merumuskan** dekomposisi matriks SVD dan reduksi dimensi PCA menggunakan pustaka Python NumPy untuk pemrosesan data AI (CPMK-4, C4).

---

## 4. PETA BAB ↔ SUB-CPMK ↔ PEKAN ↔ ASESMEN

| Bab | Judul Bab | Sub-CPMK | Pekan | CPMK | Asesmen Terkait |
|:--:|---|---|:--:|:--:|---|
| 1 | Vektor, Matriks, dan Operasi Matriks | 1.1 (dasar) | 1–2 | CPMK-1 | **Tugas 1**, UTS |
| 2 | Sistem Persamaan Linear dan Eliminasi Gauss–Jordan | 1.1 | 2 | CPMK-1 | **Tugas 1**, UTS |
| 3 | Jenis Solusi SPL, Determinan, dan Invers Matriks | 1.2 | 3 | CPMK-1 | Tugas 1, UTS |
| 4 | Ruang Vektor, Subruang, Kombinasi Linier, dan Span | 2.1 | 4 | CPMK-2 | **Tugas 1**, UTS |
| 5 | Kebebasan Linier, Basis, Dimensi, dan Ortogonalisasi | 2.2 | 5 | CPMK-2 | UTS, UAS |
| 6 | Transformasi Linier dan Nilai Eigen | 3.1 | 6 | CPMK-3 | UTS, UAS |
| 7 | Diagonalisasi dan Matriks Simetris | 3.2 | 7, 12 | CPMK-3 | UTS, Tugas 2, UAS |
| 8 | Nilai Singular dan Dekomposisi SVD | 4.1 | 9 | CPMK-4 | Tugas 2, UAS |
| 9 | PCA dan Reduksi Dimensi dengan NumPy | 4.2 | 10–11 | CPMK-4 | **Tugas 2**, UAS |
| Lampiran A | Glosarium, Tabel Sifat Determinan, dan Rumus Eigen–SVD | — | — | — | — |
| Lampiran B | Kumpulan Soal Komputasi Terpandu dan Kunci | — | — | — | — |

**Total bab inti:** 9 bab. Setiap bab setara 1–2 pekan pertemuan (16 pekan termasuk UTS & UAS).

---

## 5. STRUKTUR BAKU SETIAP BAB

Setiap bab wajib memuat tujuh komponen berikut, dengan urutan tetap:

| No | Komponen | Isi Wajib | Estimasi |
|:--:|---|---|:--:|
| 1 | **Peta Kompetensi** | Sub-CPMK yang dibina, CPMK induk, indikator kinerja | 0,5 hlm |
| 2 | **Uraian Materi** | 3–6 sub-bab, masing-masing dengan definisi formal, contoh kerja langkah demi langkah, dan **jebakan komputasi** | 12–20 hlm |
| 3 | **Sorotan Kasus (Case Spotlight)** | Satu penerapan komputasi nyata + pertanyaan analitis | 1,5 hlm |
| 4 | **Rangkuman** | 5–8 butir kunci dalam bentuk poin bernomor | 0,5 hlm |
| 5 | **Latihan Terbimbing** | 8–12 soal bertingkat (C2–C4) dengan petunjuk pengerjaan | 1,5 hlm |
| 6 | **Tes Formatif Mandiri** | 10 soal pilihan ganda + 3 esai pendek, kunci di lampiran daring | 2 hlm |
| 7 | **Rujukan Bab** | 3–6 sitasi IEEE, sinkron dengan daftar pustaka RPS | 0,3 hlm |

**Kekhususan modul ini:**

- Setiap bab yang memuat prosedur komputasi wajib menyertakan kotak **"Alur Komputasi Baku"** (masukan → langkah berurutan → keluaran → verifikasi).
- Bab 8–9 wajib menyertakan **potongan kode NumPy yang dapat dijalankan** beserta *output* yang diharapkan, agar mahasiswa dapat membandingkan hasil manual dengan hasil komputasi.
- Setiap kotak kode mengikuti konvensi: satu sel kode = satu tujuan, komentar singkat berbahasa Indonesia, dan tidak menggunakan pustaka *machine learning* tingkat tinggi.

---

## 6. OUTLINE RINCI PER BAB

### BAB 1 — Vektor, Matriks, dan Operasi Matriks
**Sub-CPMK:** 1.1 (dasar) | **Pekan:** 1–2 | **Estimasi:** 26 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 1.1 | Vektor di $\mathbb{R}^n$: notasi, penjumlahan, perkalian skalar |
| 1.2 | *Dot product*, norma, jarak, sudut antar-vektor, ortogonalitas |
| 1.3 | Matriks: notasi, ukuran, matriks khusus (identitas, nol, diagonal, segitiga, simetris) |
| 1.4 | Operasi matriks: penjumlahan, perkalian skalar, perkalian matriks, sifat non-komutatif |
| 1.5 | Transpose, *trace*, dan sifat-sifatnya |
| 1.6 | Matriks elementer dan kaitannya dengan OBE |
| 1.7 | Kesalahan umum: menganggap $AB = BA$; salah urutan perkalian pada perkalian berantai |

**Kegiatan belajar:** latihan operasi matriks (PT 120′), latihan dot product & norma (PT 90′), diskusi interpretasi geometris vektor (TM 30′).
**Tes formatif:** 6 soal operasi matriks + 4 soal dot product/norma.

---

### BAB 2 — Sistem Persamaan Linear dan Eliminasi Gauss–Jordan
**Sub-CPMK:** 1.1 | **Pekan:** 2 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 2.1 | Bentuk umum SPL; representasi matriks $A\mathbf{x} = \mathbf{b}$ |
| 2.2 | Matriks diperbesar (*augmented matrix*) dan penyusunannya |
| 2.3 | Tiga Operasi Baris Elementer (OBE) dan invariannya |
| 2.4 | Eliminasi Gauss menuju bentuk eselon baris |
| 2.5 | Eliminasi Gauss–Jordan menuju bentuk eselon baris tereduksi (RREF) |
| 2.6 | Algoritma sistematis: pivot, normalisasi, eliminasi atas–bawah |
| 2.7 | Penyelesaian balik (*back substitution*) dan pembacaan solusi dari RREF |
| 2.8 | Verifikasi solusi dengan substitusi balik |
| 2.9 | Kesalahan umum: lupa menormalisasi pivot; menghapus baris nol yang sebenarnya informatif; salah membaca variabel bebas |

**Kegiatan belajar:** latihan OBE bertingkat (PT 180′), penyelesaian 6 SPL 3×3 dengan verifikasi (PT 120′), demonstrasi galat umum (TM 25′).
**Tes formatif:** 4 SPL diselesaikan hingga RREF + verifikasi.

---

### BAB 3 — Jenis Solusi SPL, Determinan, dan Invers Matriks
**Sub-CPMK:** 1.2 | **Pekan:** 3 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 3.1 | Variabel bebas dan terikat; parameterisasi solusi |
| 3.2 | Klasifikasi solusi: tunggal, tak hingga, tak ada |
| 3.3 | Rank matriks koefisien dan rank matriks diperbesar; teorema Rouché–Capelli |
| 3.4 | SPL homogen, ruang solusi trivial dan non-trivial |
| 3.5 | Determinan: definisi kofaktor, ekspansi baris/kolom |
| 3.6 | Sifat determinan: perkalian, transpose, baris bergantung linier, operasi baris |
| 3.7 | Aturan Cramer dan batas keberlakuannya ($\det A \ne 0$) |
| 3.8 | Invers matriks: metode adjoin dan metode OBE (Gauss–Jordan) |
| 3.9 | Invers matriks 2×2 dan 3×3: rumus cepat dan verifikasi |
| 3.10 | Kesalahan umum: memakai Cramer pada sistem tak konsisten; salah tanda kofaktor |

**Kegiatan belajar:** latihan klasifikasi solusi (PT 120′), latihan determinan–invers (PT 150′), studi kasus interpretasi fisis SPL (TM 30′).
**Tes formatif:** 3 klasifikasi solusi + 2 determinan 4×4 + 2 invers dengan verifikasi.

---

### BAB 4 — Ruang Vektor, Subruang, Kombinasi Linier, dan Span
**Sub-CPMK:** 2.1 | **Pekan:** 4 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 4.1 | Aksioma ruang vektor riil (10 aksioma) dan konsekuensinya |
| 4.2 | Contoh ruang vektor: $\mathbb{R}^n$, $\mathbb{R}^{m\times n}$, polinomial $\mathcal{P}_n$, fungsi kontinu |
| 4.3 | Subruang dan tiga syarat uji subruang |
| 4.4 | Subruang yang dibangun oleh himpunan vektor |
| 4.5 | Kombinasi linier: definisi dan uji melalui SPL |
| 4.6 | Rentang (*span*) dan himpunan perentang |
| 4.7 | Kapan $\mathbf{b} \in \mathrm{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$: kaitan langsung dengan konsistensi SPL |
| 4.8 | Interpretasi geometris span di $\mathbb{R}^2$ dan $\mathbb{R}^3$ (titik, garis, bidang, ruang) |
| 4.9 | Kesalahan umum: menganggap gabungan dua subruang selalu subruang |

**Kegiatan belajar:** uji subruang (PT 120′), latihan kombinasi linier & span (PT 150′), persiapan Tugas 1 (TM 35′).
**Tes formatif:** 3 uji subruang + 3 uji span dengan justifikasi.

---

### BAB 5 — Kebebasan Linier, Basis, Dimensi, dan Ortogonalisasi
**Sub-CPMK:** 2.2 | **Pekan:** 5 | **Estimasi:** 34 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 5.1 | Kebebasan linier dan ketergantungan linier |
| 5.2 | Uji kebebasan melalui SPL homogen $A\mathbf{c} = \mathbf{0}$ |
| 5.3 | Basis: definisi dan ketunggalan koordinat relatif basis |
| 5.4 | Basis standar $\mathbb{R}^n$ dan basis ruang polinomial |
| 5.5 | Dimensi dan invariansinya |
| 5.6 | Ruang baris, ruang kolom, dan rank matriks |
| 5.7 | Teorema rank–nullity dan ruang nol (*null space*) |
| 5.8 | Ruang hasil kali dalam; panjang, sudut, ortogonalitas |
| 5.9 | Himpunan ortogonal dan ortonormal; koordinat terhadap basis ortonormal |
| 5.10 | Proses ortogonalisasi Gram–Schmidt langkah demi langkah |
| 5.11 | Kesalahan umum: menyimpulkan bebas linier hanya dari jumlah vektor; lupa menormalkan hasil Gram–Schmidt |

**Kegiatan belajar:** latihan uji kebebasan (PT 150′), latihan basis–dimensi–rank (PT 120′), latihan Gram–Schmidt (PT 90′).
**Tes formatif:** 2 uji kebebasan + 2 penentuan basis/dimensi + 1 Gram–Schmidt lengkap.

---

### BAB 6 — Transformasi Linier dan Nilai Eigen
**Sub-CPMK:** 3.1 | **Pekan:** 6 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 6.1 | Definisi transformasi linier dan uji kelinearan |
| 6.2 | Contoh: rotasi, refleksi, skala, proyeksi, turunan (level konseptual) |
| 6.3 | Matriks representasi terhadap basis standar |
| 6.4 | Kernel dan range; hubungan dengan rank dan nullity |
| 6.5 | Teorema dimensi untuk transformasi linier |
| 6.6 | Nilai eigen dan vektor eigen: definisi $A\mathbf{x} = \lambda\mathbf{x}$, $\mathbf{x} \ne \mathbf{0}$ |
| 6.7 | Persamaan karakteristik $\det(A - \lambda I) = 0$ dan polinomial karakteristik |
| 6.8 | Ruang eigen (*eigenspace*) dan basisnya |
| 6.9 | Interpretasi geometris eigen: arah yang dipertahankan transformasi |
| 6.10 | Kesalahan umum: menerima $\mathbf{x} = \mathbf{0}$ sebagai vektor eigen; salah tanda pada $\det(A - \lambda I)$ |

**Kegiatan belajar:** latihan transformasi & matriks representasi (PT 120′), latihan eigen 2×2 dan 3×3 (PT 180′), diskusi interpretasi geometris (TM 30′).
**Tes formatif:** 2 transformasi linier + 3 perhitungan eigen lengkap dengan ruang eigen.

---

### BAB 7 — Diagonalisasi dan Matriks Simetris
**Sub-CPMK:** 3.2 | **Pekan:** 7, 12 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 7.1 | Matriks similar dan invarian (determinan, trace, polinomial karakteristik) |
| 7.2 | Syarat cukup diagonalisasi: $n$ vektor eigen bebas linier |
| 7.3 | Multiplisitas aljabar vs geometrik |
| 7.4 | Prosedur diagonalisasi: $P^{-1}AP = D$ dan $A = PDP^{-1}$ |
| 7.5 | Kasus matriks tak terdiagonalkan dan contoh konkretnya |
| 7.6 | Pangkat matriks melalui diagonalisasi ($A^k = PD^kP^{-1}$) |
| 7.7 | Matriks simetris riil: vektor eigen orthogonal |
| 7.8 | Teorema spektral (pengantar): $A = PDP^T$ dengan $P$ ortogonal |
| 7.9 | Penerapan: sistem dinamik diskret $\mathbf{x}_{k+1} = A\mathbf{x}_k$ |
| 7.10 | Kesalahan umum: menganggap setiap matriks dapat didiagonalkan; lupa menormalkan kolom $P$ pada matriks simetris |

**Kegiatan belajar:** latihan diagonalisasi (PT 150′), latihan matriks simetris & ortogonal (PT 120′), studi kasus sistem dinamik (TM 30′).
**Tes formatif:** 2 diagonalisasi penuh + 1 verifikasi $A^k$ + 1 kasus matriks simetris.

---

### BAB 8 — Nilai Singular dan Dekomposisi SVD
**Sub-CPMK:** 4.1 | **Pekan:** 9 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 8.1 | Keterbatasan diagonalisasi: matriks tak persegi dan matriks tak terdiagonalkan |
| 8.2 | Matriks $A^TA$ dan $AA^T$ serta sifat semidefinit positifnya |
| 8.3 | Nilai singular $\sigma_i = \sqrt{\lambda_i(A^TA)}$ |
| 8.4 | Vektor singular kanan (dari $A^TA$) dan kiri (dari $AA^T$) |
| 8.5 | Konstruksi dekomposisi $A = U\Sigma V^T$ langkah demi langkah |
| 8.6 | Bentuk *full* vs *reduced* SVD; ukuran setiap matriks |
| 8.7 | Hubungan nilai singular dengan rank, norma spektral, dan norma Frobenius |
| 8.8 | Teorema Eckart–Young dan aproksimasi rank-$k$ |
| 8.9 | Implementasi NumPy: `np.linalg.svd`, verifikasi manual pada matriks 2×2 |
| 8.10 | Kesalahan umum: salah mengurutkan nilai singular; lupa bahwa $U$ dan $V$ ortogonal |

**Kegiatan belajar:** derivasi SVD manual (PT 180′), latihan aproksimasi rank-$k$ (PT 120′), verifikasi NumPy (TM 30′).
**Tes formatif:** 1 SVD lengkap 2×2 + 1 aproksimasi rank-1 dengan hitung galat.

---

### BAB 9 — PCA dan Reduksi Dimensi dengan NumPy
**Sub-CPMK:** 4.2 | **Pekan:** 10–11 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 9.1 | Motivasi reduksi dimensi: kutukan dimensi, redundansi, biaya komputasi |
| 9.2 | Standarisasi z-score dan sensitivitas PCA terhadap skala |
| 9.3 | Matriks kovarians dan sifat semidefinit positif |
| 9.4 | Jalur A: eigen-dekomposisi matriks kovarians |
| 9.5 | Jalur B: SVD matriks data terpusat (dan mengapa keduanya ekuivalen) |
| 9.6 | Komponen utama dan skor komponen |
| 9.7 | *Explained variance ratio* dan *scree plot* |
| 9.8 | Pemilihan jumlah komponen: aturan Kaiser, elbow, ambang varians kumulatif |
| 9.9 | Rekonstruksi data dan galat rekonstruksi |
| 9.10 | Implementasi lengkap NumPy: `mean`, `std`, `cov`, `linalg.svd`, `argsort` |
| 9.11 | Jebakan metodologis: kebocoran data uji, standarisasi setelah pemisahan data, interpretasi berlebihan |
| 9.12 | Kesalahan umum: memakai PCA pada data kategorikal tanpa transformasi; membandingkan explained variance antar-dataset berbeda skala |

**Kegiatan belajar:** praktik notebook NumPy (PT 150′), latihan interpretasi scree plot (PT 90′), studi kasus kompresi citra & data tabular (TM 40′).
**Tes formatif:** 1 alur PCA lengkap pada dataset kecil + 3 soal interpretasi.

---

### LAMPIRAN A — Glosarium, Tabel Sifat Determinan, dan Rumus Eigen–SVD
**Estimasi:** 14 halaman. Memuat ≥ 80 entri istilah (pivot, RREF, rank, nullity, span, basis, ortogonal, eigen, nilai singular, explained variance, dan lain-lain) beserta padanan Inggris; tabel lengkap sifat determinan dan operasi baris; tabel sifat eigen (trace = jumlah eigen, determinan = hasil kali eigen); ringkasan rumus SVD dan PCA dua jalur; tabel perbandingan kompleksitas komputasi.

### LAMPIRAN B — Kumpulan Soal Komputasi Terpandu dan Kunci
**Estimasi:** 30 halaman. Memuat 60 soal bertingkat (C2–C4) lengkap dengan petunjuk dan alur komputasi baku, 6 soal SVD/PCA dengan verifikasi NumPy, serta 4 paket latihan UTS/UAS mandiri dengan kunci ringkas.

---

## 7. SPESIFIKASI TEKNIS PENULISAN

| Aspek | Ketentuan |
|---|---|
| Ukuran halaman | A5 (148 × 210 mm), margin 2 cm |
| Tipografi | Body 10,5 pt *serif* (Times New Roman / Book Antiqua); judul sans-serif; spasi 1,15 |
| Tata letak | Satu kolom untuk matriks, alur komputasi, dan kode; dua kolom untuk uraian naratif |
| Notasi | Vektor tebal huruf kecil ($\mathbf{v}$); matriks huruf kapital ($A$); transpose $A^T$; invers $A^{-1}$; nilai eigen $\lambda$; nilai singular $\sigma$; norma $\lVert\mathbf{v}\rVert$ |
| Kode | *Monospace* 9,5 pt; latar abu terang; keluaran (*output*) diberi label `OUT:` dengan warna berbeda |
| Diagram | Digambar vektor (SVG); ilustrasi geometris span, kernel/range, dan arah eigen wajib konsisten gayanya |
| Sitasi | IEEE *numbered*, konsisten dengan daftar pustaka RPS |
| Istilah asing | Ditulis miring pada kemunculan pertama, disertai padanan Indonesia |
| Warna | Aksen biru tua untuk kotak definisi; hijau untuk kotak "Alur Komputasi Baku"; abu untuk kotak galat umum |
| Aksesibilitas | Kontras teks ≥ 4,5:1; diagram memiliki teks alternatif; notasi matriks diberi penjelasan verbal |

---

## 8. RENCANA PRODUKSI DAN KENDALI MUTU

| Tahap | Aktivitas | Keluaran | Penanggung Jawab | Durasi |
|:--:|---|---|---|---|
| P1 | Finalisasi outline & alokasi penulis per bab | Dokumen outline ini | Koordinator RMK | 1 pekan |
| P2 | Penulisan draf bab 1–5 | Draf 55% | Tim penulis | 8 pekan |
| P3 | Penulisan draf bab 6–9 + lampiran | Draf 100% | Tim penulis | 6 pekan |
| P4 | Verifikasi matematis (cek ulang setiap perhitungan & kunci) | Lembar verifikasi | Dua penelaah internal | 3 pekan |
| P5 | Uji seluruh kode NumPy di bab 8–9 pada 3 versi NumPy berbeda | Laporan uji kode | Asisten laboratorium | 2 pekan |
| P6 | Telaah sejawat & uji keterbacaan mahasiswa | Laporan telaah + uji 20 responden | Tim penulis | 2 pekan |
| P7 | Penyuntingan bahasa & tata letak | Naskah siap cetak | Penyunting | 2 pekan |
| P8 | Pengajuan ISBN & pencetakan terbatas | ISBN + 50 eksemplar | Prodi & perpustakaan | 3 pekan |

### Checklist mutu sebelum cetak

- [ ] Seluruh Sub-CPMK RPS memiliki bab/sub-bab pembina yang eksplisit.
- [ ] Tidak ada materi *out-of-scope* Dokumen 043 (tidak ada pelatihan scikit-learn/tensorflow, tidak ada kode aplikasi web, tidak ada kalkulus diferensial–integral).
- [ ] Setiap prosedur komputasi memiliki kotak "Alur Komputasi Baku" dengan langkah terverifikasi.
- [ ] Seluruh hasil OBE, determinan, invers, eigen, dan SVD telah dihitung ulang oleh penelaah kedua.
- [ ] Setiap potongan kode NumPy dapat dijalankan tanpa galat dan *output* di modul sesuai hasil aktual.
- [ ] Tidak ada kode yang bergantung pada pustaka *machine learning* tingkat tinggi.
- [ ] Setiap grafik (scree plot, galat rekonstruksi) dibangkitkan dari data contoh yang disertakan.
- [ ] Setiap bab memiliki peta kompetensi, kasus, rangkuman, latihan, dan tes formatif.
- [ ] Seluruh sitasi IEEE valid dan dapat ditelusuri; tidak ada rujukan fiktif.
- [ ] Notasi konsisten lintas bab (mis. selalu $A^T$, bukan $A'$).
- [ ] Uji keterbacaan: ≥ 80% responden menilai materi mudah diikuti.

---

## 9. KETERKAITAN DENGAN DOKUMEN LAIN

| Dokumen | Keterkaitan |
|---|---|
| `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` | Sumber capaian, materi, dan titik asesmen |
| `059_2_SAP_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` | Sumber alokasi waktu dan urutan kegiatan per pekan |
| `059_4_RENCANA_EVALUASI_ASESMEN_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` | Sumber bobot dan jadwal evaluasi |
| `059_5_RUBRIK_PENILAIAN_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` | Sumber kriteria penilaian latihan dan tes formatif |
| Dokumen 043 | Batas isi (*in-scope*, *out-of-scope*, *handoff anchor*) |
| Dokumen 037 | Demarkasi silabus antar-MK |

---

*Outline ini merupakan rancangan kerja penulisan modul; perubahan judul bab wajib melalui persetujuan Koordinator RMK dan dicatat dalam riwayat revisi.*
