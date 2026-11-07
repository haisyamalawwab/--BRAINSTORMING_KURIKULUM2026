# 061_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-307 — SISTEM CERDAS (*Intelligent Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI307` · **Klaster Rubrik Master (Dok 018):** Klaster 3 (`K-3`)  
**CPL:** `CPL-06` (`P2` = 50%) & `CPL-09` (`KK1` = 50%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN KLASTER KECERDASAN ARTIFISIAL (`K-3`)

Mengacu pada **Dokumen 018 §3 (Klaster `K-3`)**, penilaian pada `STI-307 Sistem Cerdas` mengukur ketepatan metodologi formulasi masalah/aturan/fungsi keanggotaan, akurasi penelusuran algoritma & metrik inferensi, ketajaman interpretasi hasil keputusan, serta keterulangan eksekusi (*reproducibility*) skrip simulasi Python `scikit-fuzzy`.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-06` [C3])
**Objek Penilaian:** *Problem Set* Berparameter NIM: Penelusuran *Greedy Best-First*, **A\***, Pembuktian Heuristik *Admissible*, serta Pohon **Minimax & Alpha-Beta Pruning** (+ Kuis Verifikasi).

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Formulasi Ruang Status & Pembuktian Sifat Heuristik**<br>(`Sub-CPMK-1.1`) | **30%** | Tupel ruang status lengkap dan pengujian syarat *admissible* ($h(n)\le h^*(n)$) serta *consistent* pada seluruh simpul/tepi dibuktikan secara matematis tanpa celah. | Formulasi ruang status tepat dan pembuktian *admissibility* benar; hanya kurang mengecek ketaksamaan segitiga pada 1–2 tepi. | Formulasi dasar tepat dan memahami arti *admissible*, namun hanya memeriksa sebagian simpul secara intuitif. | Keliru membedakan biaya riil $g(n)$ dengan estimasi $h(n)$ saat menguji *admissibility*. | Gagal merumuskan ruang status dan konsep heuristik. |
| **2. Keruntutan Jejak Ekspansi *Greedy, A\*,* & Pemangkasan *Alpha-Beta***<br>(`Sub-CPMK-1.1 & 1.2`) | **45%** | Tabel iterasi `OPEN`/`CLOSED` pada *Greedy* & *A\** serta pembaruan batas $[\alpha,\beta]$ dan penandaan cabang terpotong pada *Minimax* 100% runtut dan konsisten dengan kuis verifikasi kelas. | Langkah ekspansi *A\** dan pemangkasan *Alpha-Beta* benar dan jelas; terdapat maks. 1 selip kecil penulisan antrean sekunder. | Alur utama *A\** dan *Minimax* benar, namun sempat terlewat memangkas 1 cabang saat $\alpha = \beta$. | Mencampur aturan evaluasi *Greedy* ($h(n)$) ke dalam *A\** atau salah mempropagasi giliran `MAX`/`MIN`. | Hanya menulis rute akhir tanpa jejak ekspansi atau tidak sesuai parameter NIM sendiri. |
| **3. Presisi Solusi Optimal & Analisis Kompleksitas Ruang/Waktu** | **25%** | Jalur dan total biaya optimal eksak disertai perbandingan tajam jumlah simpul diekspansi serta kompleksitas ruang/waktu kedua algoritma. | Biaya solusi tepat dan analisis perbandingan efisiensi ruang/waktu disajikan dengan benar. | Jalur solusi benar, tetapi analisis kompleksitas $O(b^d)$ vs $O(b^{m/2})$ masih bersifat hafalan umum. | Solusi jalur meleset akibat kesalahan penjumlahan bobot tepi. | Solusi dan analisis kompleksitas salah total. |

$$\text{Skor Tugas 1} = 0,30(K_1) + 0,45(K_2) + 0,25(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2` [C4])
**Objek Penilaian:** Jawaban Ujian Tertulis 100 Menit: Perancangan Basis Aturan Sistem Pakar, Jejak *Forward & Backward Chaining*, serta Perhitungan *Certainty Factor*.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Struktur & Konsistensi Basis Pengetahuan Aturan `IF–THEN`**<br>(`Sub-CPMK-2.1`) | **35%** | Minimal 10 aturan berantai multi-level tersusun logis, simbol fakta konsisten, graf ketergantungan jelas, dan 100% bebas aturan kontradiktif maupun siklus. | Basis aturan berantai lengkap, logis, dan konsisten; hanya terdapat 1 ketidakrapian penamaan simbol fakta antara. | Aturan memenuhi jumlah minimal, namun sebagian besar masih datar (1 lapis langsung ke konklusi tanpa kesimpulan antara). | Terdapat aturan yang saling bertabrakan atau siklus tak berujung pada basis pengetahuan. | Gagal menyusun aturan produksi `IF–THEN` yang bermakna. |
| **2. Ketepatan Penelusuran *Forward* & *Backward Chaining***<br>(`Sub-CPMK-2.1 & 2.2`) | **40%** | Tabel siklus *Working Memory / Conflict Set* pada *Forward Chaining* dan pohon rekursif sub-tujuan *Backward Chaining* 100% akurat beserta justifikasi pemilihan metode yang tajam. | Jejak kedua mesin inferensi benar dan argumen pemilihan metode relevan dengan bentuk graf aturan. | Penelusuran *Forward Chaining* tepat, namun penelusuran *Backward Chaining* belum menuliskan urutan tumpukan sub-tujuan secara utuh. | Tertukar antara arah penelusuran *Forward* dengan *Backward Chaining*. | Tidak mampu menelusuri jalannya mesin inferensi. |
| **3. Akurasi Perhitungan *Certainty Factor (CF)* & Interpretasi** | **25%** | Penggunaan $\min/\max$ premis majemuk dan rumus kombinasi $CF_{\text{combine}}$ multi-jalur 100% presisi dengan kesimpulan yang diinterpretasikan secara tepat. | Rumus dan tahapan perhitungan $CF$ benar; hanya terdapat 1 selip pembulatan desimal kecil. | Perhitungan $CF$ aturan tunggal benar, namun keliru saat menggabungkan dua bukti paralel ($CF_1 + CF_2$ dijumlahkan langsung tanpa $(1-CF_1)$). | Salah memilih rumus kombinasi $CF$ untuk tanda berlawanan/sama. | Bagian *Certainty Factor* kosong atau salah seluruhnya. |

$$\text{Skor UTS} = 0,35(K_1) + 0,40(K_2) + 0,25(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3` / `CPL-09` [C4])
**Objek Penilaian:** Studi Kasus Mandiri Berparameter NIM: Perhitungan Analitis Komparatif **FIS Mamdani** vs **FIS Sugeno** (+ Kuis Verifikasi).

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Perancangan Fungsi Keanggotaan & Ketepatan *Fuzzifikasi***<br>(`Sub-CPMK-3.1`) | **30%** | Grafik partisi domain proporsional (bahu di ujung, segitiga/trapesium tumpang-tindih), persamaan *piecewise* eksak, dan seluruh nilai $\mu(x_0), \mu(y_0)$ dihitung tanpa cacat. | Grafik, rumus fungsi keanggotaan, dan perhitungan derajat keanggotaan benar; hanya kurang melabeli 1 titik batas pada grafik. | Partisi himpunan *fuzzy* benar, namun terjadi 1 kekeliruan substitusi penyebut $(b-a)$ saat menghitung $\mu$. | Kurva antar-himpunan tidak tumpang-tindih atau keluar dari rentang $[0,1]$. | Tidak mampu merumuskan fungsi keanggotaan maupun *fuzzifikasi*. |
| **2. Inferensi Aturan & Defuzzifikasi Mamdani (*Centroid*) vs Sugeno**<br>(`Sub-CPMK-3.1 & 3.2`) | **45%** | Evaluasi $\alpha\text{-predikat}$ seluruh aturan aktif, agregasi daerah terpotong Mamdani, perhitungan *Centroid*, dan *Weighted Average* Sugeno 100% akurat serta selaras dengan kuis verifikasi. | Prosedur inferensi dan defuzzifikasi kedua metode benar; hanya terdapat selip aritmetika ringan pada penjumlahan momen *Centroid*. | Perhitungan Sugeno benar, namun pada Mamdani salah menentukan batas tinggi pemotongan pada daerah transisi antar-himpunan keluaran. | Mencampur rumus *Weighted Average* Sugeno untuk menyelesaikan Mamdani tanpa agregasi kurva keluaran. | Gagal menyelesaikan tahapan inferensi dan defuzzifikasi. |
| **3. Ketajaman Analisis Komparatif Mamdani vs Sugeno** | **25%** | Membandingkan hasil keputusan, karakteristik permukaan keluaran, interpretabilitas aturan, dan kompleksitas komputasi kedua metode secara kritis pada konteks kasus. | Analisis perbandingan kedua metode jelas, logis, dan didukung angka hasil perhitungan. | Menyajikan perbandingan singkat angka keluaran kedua metode namun belum membahas implikasi komputasinya. | Kesimpulan hanya mengulang angka tanpa analisis pembandingan. | Tidak menyertakan analisis perbandingan. |

$$\text{Skor Tugas 2} = 0,30(K_1) + 0,45(K_2) + 0,25(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-3` & Sintesis [C4])
**Objek Penilaian:** Purwarupa Notebook Python **`scikit-fuzzy`** Individu (40% UAS) + Ujian Tertulis Komprehensif 100 Menit (60% UAS).

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Metodologi Pemodelan Sistem Cerdas & Kepatuhan *Guardrail*** | **35%** | Arsitektur variabel linguistik, kelengkapan aturan *fuzzy*, dan integrasi *rule-screening* dirancang sangat solid serta 100% mematuhi *guardrail* simbolik/fuzzy (bebas ML/`scikit-learn`). | Pemodelan variabel dan basis aturan di `scikit-fuzzy` lengkap, logis, dan mematuhi *guardrail* mata kuliah. | Sistem *fuzzy* dasar berjalan untuk kasus normal, namun masih terdapat kombinasi aturan yang terlewat pada sudut ekstrem semesta. | Basis aturan tidak lengkap sehingga simulasi mengalami *error* defuzzifikasi area nol pada beberapa masukan. | Melanggar *guardrail* (menyerahkan proyek klasifikasi ML instan) atau gagal membangun model. |
| **2. Akurasi Komputasi `scikit-fuzzy` & Presisi Ujian Tertulis** | **35%** | Keluaran simulasi Python terekonsiliasi akurat dengan hitungan kertas, dan jawaban perhitungan serta penelusuran kode pada ujian tertulis luring sangat presisi. | Simulasi `scikit-fuzzy` akurat dan jawaban ujian tertulis luring konsisten baik dengan kualitas notebook. | Notebook berjalan baik dan mahasiswa mencapai ambang minimal pada soal perhitungan & penelusuran kode saat ujian luring. | Terdapat jurang mencolok antara kode notebook yang canggih dengan ketidakmampuan menjawab sintaks dasar `skfuzzy` saat ujian luring. | Gagal pada ujian tertulis maupun eksekusi simulasi. |
| **3. Analisis Sensitivitas Kurva, *3D Surface*, & Skenario Uji Batas** | **20%** | Menampilkan visualisasi *3D control surface* serta menganalisis secara tajam dampak perubahan parameter kurva pada minimal 8 skenario batas (*edge cases*). | Visualisasi kurva/permukaan kontrol lengkap dengan pembahasan skenario uji yang tepat. | Menampilkan grafik keluaran standar `scikit-fuzzy` dengan penjelasan tekstual seperlunya. | Hanya menampilkan angka keluaran tunggal tanpa grafik dan tanpa pengujian skenario batas. | Tidak ada pengujian maupun interpretasi hasil. |
| **4. *Reproducibility* & Dokumentasi Notebook (`K-3`)** | **10%** | Notebook bersih, terurut rapi dari atas ke bawah (*Run All* tanpa galat), beranotasi Markdown jelas, dan menyertakan spesifikasi versi pustaka. | Notebook dapat dijalankan ulang dengan mulus dan terdokumentasi rapi. | Notebook dapat dijalankan namun penjelasan tiap sel masih minim. | Urutan eksekusi sel berantakan sehingga memunculkan `NameError` saat dijalankan ulang. | Berkas rusak/kosong atau terindikasi salin-tempel karya rekan. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,20(K_3) + 0,10(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF LATIHAN PENELUSURAN & SIMULASI KELAS

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketelitian Jejak Tabel Algoritma** | Menuliskan setiap iterasi `OPEN`/`CLOSED` dan perubahan *Working Memory* tanpa melompati langkah. | Jejak iterasi rapi dengan selip notasi sangat minim. | Kadang melompati langkah antara saat menelusuri pohon/aturan. | Menebak hasil tanpa membuat tabel penelusuran. |
| **Eksperimen Mandiri `scikit-fuzzy`** | Aktif menguji variasi bentuk kurva (`trimf`, `trapmf`, `gaussmf`) dan mengamati perubahan permukaan keputusan. | Menjalankan seluruh contoh kode modul dengan benar. | Hanya menyalin contoh kode tanpa mencoba memodifikasi parameter. | Tidak menyiapkan lingkungan kerja Python di sesi demonstrasi. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-307` (`CPL-06` & `CPL-09` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai secara mendalam pencarian ruang status heuristik (*A\*, Minimax Alpha-Beta*), perancangan sistem pakar (*Forward/Backward Chaining, CF*), serta mampu merancang dan memvalidasi sistem inferensi logika *fuzzy* (*Mamdani & Sugeno*) berbasis Python `scikit-fuzzy` untuk pemecahan masalah bisnis nyata. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa terampil menerapkan algoritma pencarian heuristik, menyusun basis aturan sistem pakar yang konsisten, serta mengimplementasikan inferensi *fuzzy* secara akurat baik analitis maupun komputasional. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) pada penelusuran pencarian heuristik dasar, inferensi aturan sistem pakar, dan perhitungan/simulasi dasar logika *fuzzy*. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih sering keliru dalam penelusuran simpul heuristik, menyusun aturan yang tidak konsisten, atau belum tuntas memahami proses inferensi dan defuzzifikasi. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai konsep dasar pencarian, sistem pakar, maupun logika *fuzzy*, atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-307` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menerapkan algoritma pencarian *Greedy Best-First* dan **A\*** beserta evaluasi heuristik *admissible* pada optimasi rute. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menelusuri pohon keputusan kompetitif menggunakan **Minimax** dan **Alpha-Beta Pruning**. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu menyusun basis aturan `IF–THEN` yang konsisten dan menelusuri inferensi **Forward Chaining**. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menelusuri **Backward Chaining** dan menghitung derajat keyakinan kesimpulan dengan **Certainty Factor**. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu merancang fungsi keanggotaan dan menyelesaikan inferensi logika *fuzzy* metode **Mamdani**. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menyelesaikan inferensi logika *fuzzy* metode **Sugeno** serta mengimplementasikannya dengan Python **`scikit-fuzzy`**. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-307`)

```text
==============================================================================================================================
                 LEMBAR REKAPITULASI PENILAIAN OBE — STI-307 SISTEM CERDAS (2 SKS TEORI)
==============================================================================================================================
Semester / TA  : Semester 3 (Ganjil) / 2026-2027     CPL Dibebankan : CPL-06 (P2: 50%) & CPL-09 (KK1: 50%) [Level: Reinforce]
Klaster Rubrik : K-3 (Kecerdasan Artifisial)         Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (30%)   | T2 (20%)    | UAS (30%)   | NA    | CPL-06 | CPL-09 | Huruf
   |           |                  | [CPMK-1:C3] | [CPMK-2:C4] | [CPMK-3:C4] | [Sintesis]  | Akhir | (50%)  | (50%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 84.0        | 86.0        | 86.0        | 85.80 | 86.20  | 85.40  | A
2  | 250101002 | [Nama Mhs 2]     | 76.0        | 74.0        | 78.0        | 75.0        | 75.50 | 75.10  | 75.90  | B
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 67.80 | 67.40  | 68.20  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 77.33       | 74.67       | 78.00       | 76.33       | 76.37 | 76.23  | 76.50  | >=65:100%
==============================================================================================================================
```
