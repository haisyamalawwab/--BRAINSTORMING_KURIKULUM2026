# RUBRIK PENILAIAN
## STI-205 — ALJABAR LINEAR DAN MATRIKS

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Dokumen induk:** `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md` dan `059_4_RENCANA_EVALUASI_ASESMEN_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`
> **Rujukan rubrik master:** Dokumen 008 (Rubrik 1–3) dan Dokumen 018 (4 klaster rubrik)
> **Tanggal:** 07 November 2026

---

## 1. PRINSIP DAN CAKUPAN

| Aspek | Ketentuan |
|---|---|
| Jenis rubrik | **Analitik** untuk seluruh asesmen sumatif (kriteria terpisah, skor teragregasi) |
| Jumlah level | 4 level: Sangat Baik (4), Baik (3), Cukup (2), Kurang (1) |
| Skala skor | 0–100 per dimensi |
| Transparansi | Rubrik dibagikan sebelum asesmen dilaksanakan |
| Konsistensi | Digunakan sama pada seluruh kelas paralel |
| Fokus | Penilaian **proses komputasi aljabar**, bukan hanya hasil akhir |

**Daftar rubrik dalam dokumen ini:**

| Kode | Rubrik | Digunakan pada | Bobot |
|:---:|---|:---:|:---:|
| R-A | Tugas 1 — SPL, Matriks, dan Struktur Ruang Vektor | Pekan 4 | 20% |
| R-B | UTS — Matriks, SPL, Ruang Vektor, dan Eigen | Pekan 8 | 30% |
| R-C | Tugas 2 — Aljabar Linear untuk Reduksi Dimensi Data | Pekan 12–13 | 20% |
| R-D | UAS — Evaluasi Komprehensif | Pekan 16 | 30% |
| R-E | Presentasi & Partisipasi (formatif → komponen proses) | Pekan 12 & 15 | Formatif |
| R-F | Sikap, Etika, dan Integritas Akademik (formatif → syarat kelulusan) | Sepanjang semester | Syarat |

---

## 2. PANDUAN PENSKORAN UMUM

### 2.1 Skor Level

| Level | Label | Rentang Skor | Deskripsi Umum |
|:---:|---|:---:|---|
| **4** | Sangat Baik | 86–100 | Komputasi lengkap dan benar; setiap langkah terjustifikasi; hasil diverifikasi ulang |
| **3** | Baik | 76–85 | Benar dengan kekeliruan minor pada notasi atau satu langkah yang diringkas |
| **2** | Cukup | 60–75 | Prosedur ada tetapi tidak lengkap; ada kekeliruan yang tidak fatal |
| **1** | Kurang | 0–59 | Tidak memenuhi tuntutan minimal; prosedur tidak dikuasai |

### 2.2 Rumus Skor Rubrik

$$Skor_{rubrik} = \sum_{d=1}^{D} (w_d \times s_d)$$

dengan $w_d$ = bobot dimensi ke-$d$ (jumlah = 1,0) dan $s_d$ = skor dimensi ke-$d$ (0–100).

### 2.3 Prinsip Penilaian Komputasi Aljabar (Wajib)

| Aturan | Ketentuan |
|---|---|
| **Skor per langkah** | Langkah OBE/derivasi yang valid tetap memperoleh skor meskipun hasil akhir keliru |
| **Hasil tanpa langkah** | Maksimal 40% poin butir, meskipun hasil akhirnya benar |
| **Kesalahan yang menular** | Satu baris OBE yang salah menggugurkan skor baris itu dan seluruh baris turunannya; skor baris sebelumnya dipertahankan |
| **Verifikasi wajib** | Hasil SPL wajib diverifikasi substitusi balik; invers wajib diverifikasi $AA^{-1}=I$; diagonalisasi wajib diverifikasi $AP=PD$; tanpa verifikasi skor dimensi ketepatan maksimal 70% |
| **Kode + manual** | Pada CPMK-4, hasil NumPy wajib disertai verifikasi manual pada minimal satu sampel (mis. matriks 2×2); tanpa verifikasi skor dimensi implementasi maksimal 50% |
| **Notasi** | $A^T$, $A^{-1}$, $\lambda$, $\sigma$, $\det(A)$, $\mathrm{rank}(A)$; notasi non-standar tanpa definisi mengurangi skor dimensi kerapian |
| **Kalkulator** | Diizinkan pada Tugas 1 & Tugas 2 untuk verifikasi aritmetika; tidak pada UTS/UAS dan tidak menggantikan OBE |
| **Pustaka terlarang** | scikit-learn/tensorflow/pytorch pada Tugas 2 menggugurkan skor dimensi implementasi |

### 2.4 Prinsip Anti-Kekeliruan Umum

| Kekeliruan | Pencegahan |
|---|---|
| *Halo effect* | Nilai tiap dimensi terpisah pada lembar skor per dimensi |
| *Central tendency* | Wajib memilih level, bukan angka bebas di tengah |
| *Leniency/severity* | Moderasi antar-kelas dan *double marking* pada 10% sampel |
| Penilaian berdasarkan panjang jawaban | Skor hanya berdasarkan bukti langkah komputasi, bukan volume tulisan |
| Terpukau hasil NumPy | Verifikasi manual wajib; jawaban "kode berjalan" bukan bukti pemahaman |

---

## 3. RUBRIK A — TUGAS 1: SPL, MATRIKS, DAN STRUKTUR RUANG VEKTOR (20%)

**Cakupan CPMK:** CPMK-1 (50%), CPMK-2 (50%) | **Sub-CPMK:** 1.1, 1.2, 2.1

| Dimensi (Bobot) | Level 4 — Sangat Baik (86–100) | Level 3 — Baik (76–85) | Level 2 — Cukup (60–75) | Level 1 — Kurang (< 60) |
|---|---|---|---|---|
| **A1. Ketepatan OBE & penyelesaian SPL (25%)** | Setiap langkah OBE ditulis, pivot dinormalisasi, RREF benar; jenis solusi disimpulkan dari rank dan diverifikasi substitusi balik | Satu langkah diringkas; hasil dan kesimpulan benar | Ada kekeliruan aritmetika yang memengaruhi satu butir | Prosedur OBE tidak dikuasai |
| **A2. Ketepatan determinan & invers (25%)** | Determinan, adjoin, dan verifikasi OBE seluruhnya benar; aturan Cramer konsisten dengan hasil invers | Tepat dengan satu kekeliruan aritmetika minor | Invers benar sebagian; verifikasi tidak dilakukan | Tidak mampu menentukan invers |
| **A3. Ketepatan analisis ruang vektor (30%)** | Uji kombinasi linier, kebebasan linier, span, subruang, basis, dan dimensi seluruhnya benar dengan justifikasi | Tepat; satu justifikasi diringkas | Satu konsep keliru (mis. basis yang tidak bebas linier) | Tidak membedakan span, basis, dan dimensi |
| **A4. Kerapian & tata tulis matematis (20%)** | Notasi vektor/matriks konsisten; langkah runtut; seluruh butir dijawab dan diverifikasi | Notasi konsisten; beberapa langkah diringkas | Notasi tidak konsisten; ada butir tidak dijawab | Jawaban tidak terbaca |

**Contoh perhitungan:**
A1 = 90, A2 = 78, A3 = 84, A4 = 88
→ Skor = (0,25×90) + (0,25×78) + (0,30×84) + (0,20×88) = 22,50 + 19,50 + 25,20 + 17,60 = **84,8 (Baik)**

**Ambang minimal kelulusan komponen:** 60. Skor < 60 wajib revisi dan dinilai ulang maksimal 7 hari setelah umpan balik.

---

## 4. RUBRIK B — UTS: MATRIKS, SPL, RUANG VEKTOR, DAN EIGEN (30%)

**Cakupan CPMK:** CPMK-1 (30%), CPMK-2 (35%), CPMK-3 (25%), studi kasus (10%) | **Bentuk:** 4 bagian

### 4.1 Alokasi Poin per Bagian

| Bagian | Fokus | Poin | CPMK |
|:--:|---|:--:|:--:|
| I | SPL, OBE, determinan, invers | 30 | CPMK-1 |
| II | Ruang vektor, basis, dimensi | 35 | CPMK-2 |
| III | Eigen & diagonalisasi | 25 | CPMK-3 |
| IV | Studi kasus pemodelan matriks | 10 | CPMK-1, CPMK-2 |

### 4.2 Rubrik Uraian (diterapkan pada seluruh bagian)

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **B1. Penguasaan konsep & prosedur (25%)** | Definisi, teorema, dan prosedur diterapkan tepat; syarat keberlakuan disebut (mis. $\det A \ne 0$ untuk Cramer) | Tepat dengan 1–2 kekeliruan minor | Konsep dasar dipahami; ada kesalahan prosedur | Salah memahami konsep inti |
| **B2. Keruntutan alur komputasi (30%)** | Setiap langkah OBE/substitusi terjustifikasi dan dapat diikuti baris demi baris | Sebagian besar runtut; ada lompatan kecil | Alur terputus-putus | Tidak ada alur penyelesaian |
| **B3. Ketepatan hasil & justifikasi (30%)** | Seluruh hasil benar; kesimpulan (jenis solusi, basis, diagonalisasi) tepat dan terjustifikasi | Hasil benar; justifikasi ringkas | Sebagian besar hasil keliru | Hasil tidak relevan |
| **B4. Kelengkapan & kerapian jawaban (15%)** | Seluruh butir dijawab lengkap dan terbaca; notasi konsisten | Seluruh butir dijawab; beberapa kurang rinci | Ada butir tidak dijawab | Banyak butir kosong |

### 4.3 Kunci Berlapis Bagian IV (Studi Kasus Pemodelan Matriks, 10 poin)

| Elemen Jawaban | Poin | Kriteria |
|---|:--:|---|
| Penyusunan matriks diperbesar dari sistem | 2 | 2 poin bila seluruh koefisien dan konstanta tepat |
| Perhitungan rank matriks koefisien | 2 | 2 poin bila OBE benar dan rank dibaca dari jumlah pivot |
| Perhitungan rank matriks diperbesar | 2 | 2 poin bila dinyatakan perbandingan kedua rank |
| Kesimpulan konsistensi via Rouché–Capelli | 2 | 2 poin bila kesimpulan disertai alasan (rank sama atau berbeda) |
| Derajat kebebasan & interpretasi fisis | 2 | 2 poin bila jumlah variabel bebas dihitung ($n - \mathrm{rank}$) dan dikaitkan dengan makna jaringan |

---

## 5. RUBRIK C — TUGAS 2: ALJABAR LINEAR UNTUK REDUKSI DIMENSI DATA (20%)

**Cakupan CPMK:** CPMK-3 (30%), CPMK-4 (70%) | **Sub-CPMK:** 3.1, 3.2, 4.1, 4.2, 4.3, 4.4 | **Bentuk:** Laporan + notebook + visualisasi + presentasi

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **C1. Ketepatan formulasi aljabar (30%)** | Formulasi matriks lengkap dan konsisten (data, standarisasi, kovarians/SVD, rekonstruksi); seluruh asumsi dinyatakan dan dibenarkan | Formulasi benar; satu komponen kurang eksplisit | Formulasi benar sebagian; asumsi tidak jelas | Formulasi tidak terbentuk |
| **C2. Ketepatan implementasi & verifikasi (25%)** | Implementasi NumPy murni benar; ≥ 2 eksperimen parameter; hasil diverifikasi manual pada sampel kecil | Implementasi benar; verifikasi sebagian | Implementasi berjalan tetapi hasil tidak diverifikasi | Kode tidak berjalan atau hasil tidak relevan |
| **C3. Kualitas visualisasi & interpretasi (25%)** | Visualisasi akurat dan berlabel (scree plot/galat rekonstruksi); interpretasi komponen menghubungkan matematika dengan domain data secara kritis | Visualisasi benar; interpretasi memadai | Visualisasi kurang informatif; interpretasi dangkal | Tanpa visualisasi atau grafik salah |
| **C4. Analisis keterbatasan & tata tulis (20%)** | Keterbatasan dianalisis kritis (linearitas, skala, interpretabilitas, biaya komputasi); laporan rapi; ≥ 8 rujukan IEEE; kode terdokumentasi | Analisis memadai; 6–7 rujukan | Analisis umum; < 6 rujukan | Tanpa analisis keterbatasan |

### 5.1 Penilaian Kontribusi Tim (anti-*free-rider*)

| Kondisi | Penyesuaian Skor Individu |
|---|---|
| Kontribusi merata, terdokumentasi (log pertemuan, riwayat *commit*/dokumen) | 100% dari skor kelompok |
| Kontribusi terbukti pada ≥ 3 dari 4 dimensi | 90–100% |
| Kontribusi parsial, tidak terdokumentasi | 70–89% |
| Kontribusi minimal / tidak dapat menjelaskan satu baris kode saat verifikasi 3 menit | ≤ 50% |
| Tidak berkontribusi | 0% |

---

## 6. RUBRIK D — UAS: EVALUASI KOMPREHENSIF (30%)

**Cakupan CPMK:** CPMK-1 s.d. CPMK-4 | **Bentuk:** 4 bagian

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **D1. Penguasaan konsep komprehensif (25%)** | Mengaitkan SPL–ruang vektor–transformasi–eigen–SVD secara utuh; batas keberlakuan setiap konsep disebut | Konsep benar; keterkaitan antar-bagian sebagian | Konsep terpisah-pisah; keterkaitan lemah | Salah konsep mendasar |
| **D2. Ketepatan komputasi simbolik (30%)** | Seluruh komputasi benar; notasi matriks konsisten; langkah lengkap dan efisien | 1–2 kekeliruan minor | Beberapa kekeliruan yang memengaruhi hasil | Komputasi tidak dapat diikuti |
| **D3. Kedalaman analisis & justifikasi (30%)** | Justifikasi setiap kesimpulan (eksistensi, ketunggalan, syarat diagonalisasi, keberadaan SVD) tepat dan mendalam | Justifikasi tepat; kurang mendalam | Justifikasi deskriptif | Tanpa justifikasi |
| **D4. Struktur & komunikasi matematis (15%)** | Uraian runtut; definisi dipakai tepat; kesimpulan eksplisit | Uraian jelas; kesimpulan ada | Uraian kurang runtut | Tidak terstruktur |

### 6.1 Kunci Berlapis Bagian III — Eigen, Diagonalisasi, dan SVD (30 poin)

**Contoh matriks acuan:** $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$

| Elemen | Poin | Kriteria |
|---|:--:|---|
| Polinomial karakteristik | 4 | 4 poin bila $\lambda^2 - 7\lambda + 10 = 0$ diturunkan dari $\det(A-\lambda I)$ dengan ekspansi benar |
| Nilai eigen | 3 | 3 poin bila $\lambda_1 = 5$, $\lambda_2 = 2$ tepat (urutan bebas) |
| Vektor eigen | 4 | 2 poin per vektor eigen; vektor harus tak nol dan memenuhi $A\mathbf{x}=\lambda\mathbf{x}$ (verifikasi disarankan) |
| Matriks $P$ dan $D$ | 4 | 2 poin $P$ (kolom = vektor eigen), 2 poin $D$ diagonal dengan urutan sesuai kolom $P$ |
| Verifikasi $AP = PD$ | 2 | 2 poin bila perkalian matriks ditulis dan hasilnya identik |
| Nilai singular dari $A^TA$ | 4 | 4 poin bila $A^TA$ dihitung benar dan $\sigma_i = \sqrt{\lambda_i(A^TA)}$ diurutkan menurun |
| Penulisan $A = U\Sigma V^T$ | 5 | 5 poin bila ukuran ketiga matriks tepat, $\Sigma$ memuat nilai singular pada diagonal, dan $U$, $V$ ortogonal |
| Penjelasan eksistensi SVD vs diagonalisasi | 4 | 4 poin bila dinyatakan SVD selalu ada untuk matriks sembarang (termasuk tak persegi/tak terdiagonalkan) sedangkan diagonalisasi memerlukan $n$ vektor eigen bebas linier |

### 6.2 Kunci Berlapis Bagian IV — Pemodelan Terbuka (25 poin)

| Elemen | Poin | Kriteria |
|---|:--:|---|
| Identifikasi entitas & penyusunan model | 6 | 6 poin bila variabel, matriks, dan batas domain didefinisikan eksplisit |
| Formulasi aljabar | 6 | 6 poin bila formulasi tepat, konsisten, dan dapat dioperasikan |
| Prosedur komputasi | 7 | 7 poin bila prosedur tepat dengan urutan langkah lengkap dan dapat diverifikasi |
| Interpretasi & validasi hasil | 6 | 6 poin bila hasil diuji terhadap kasus batas/konteks dan keterbatasan disebut |

---

## 7. RUBRIK E — PRESENTASI DAN PARTISIPASI (FORMATIF)

**Digunakan:** Pekan 11 (konsultasi), Pekan 12 (presentasi antara), Pekan 15 (presentasi final)

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **E1. Penguasaan materi (40%)** | Menguasai penuh; mampu menurunkan ulang satu langkah SVD atau menjelaskan satu baris kode saat ditanya | Memahami materi; jawaban tepat dan logis | Pemahaman cukup; ragu saat tanya jawab | Tidak menguasai materi |
| **E2. Kualitas media visual (30%)** | Grafik dan matriks tertata profesional; label sumbu, satuan, dan notasi formal benar | Slide rapi; label sebagian besar ada | Slide terlalu padat; label sering hilang | Slide buruk/tidak berstruktur |
| **E3. Artikulasi & alokasi waktu (30%)** | Lugas, percaya diri, kontak mata baik, tepat waktu | Komunikasi jelas; intonasi baik; waktu pas | Suara monoton; melebihi batas waktu | Komunikasi pasif; tidak terkontrol |

---

## 8. RUBRIK F — SIKAP, ETIKA, DAN INTEGRITAS AKADEMIK (SYARAT)

| Aspek | Indikator Terpenuhi | Indikator Tidak Terpenuhi |
|---|---|---|
| Kehadiran | ≥ 75% pertemuan | < 75% pertemuan → nilai maksimum D |
| Ketepatan pengumpulan | ≥ 80% tugas tepat waktu | < 50% tugas terlambat berat |
| Deklarasi AI | Seluruh tugas menyertakan deklarasi penggunaan AI | Ada tugas tanpa deklarasi |
| Orisinalitas | Kemiripan ≤ 25%; dapat menjelaskan komputasi/kode karyanya | Kemiripan > 25% atau tidak dapat menjelaskan karya |
| Sitasi kode | Potongan kode dari dokumentasi resmi disitasi | Kode disalin tanpa sitasi |
| Etika kelas | Menghormati dosen dan sesama; aktif konstruktif | Mengganggu, tidak menghormati, atau manipulatif |

**Konsekuensi:** pelanggaran integritas akademik berat (plagiarisme, pemalsuan hasil komputasi, penggunaan pustaka terlarang yang disamarkan) dikenakan nilai 0 pada komponen terkait dan diproses sesuai Peraturan Akademik Universitas.

---

## 9. REKAPITULASI BOBOT DAN KONVERSI

### 9.1 Rekap Bobot Asesmen

| Rubrik | Bobot terhadap NA | Skor Maksimum |
|:---:|:---:|:---:|
| R-A Tugas 1 | 20% | 100 |
| R-B UTS | 30% | 100 |
| R-C Tugas 2 | 20% | 100 |
| R-D UAS | 30% | 100 |
| **Total** | **100%** | |

### 9.2 Konversi Nilai

| NA | Huruf | Bobot | Status |
|:---:|:---:|:---:|:---:|
| 86–100 | A | 4,00 | Lulus |
| 76–85 | B+ | 3,50 | Lulus |
| 70–75 | B | 3,00 | Lulus |
| 66–69 | C+ | 2,50 | Lulus |
| 60–65 | C | 2,00 | Lulus (batas) |
| 56–59 | D | 1,00 | Tidak lulus |
| 0–55 | E | 0,00 | Tidak lulus |

### 9.3 Contoh Perhitungan Lengkap

| Komponen | Skor | Bobot | Kontribusi |
|:---:|:---:|:---:|:---:|
| Tugas 1 | 84,8 | 20% | 16,96 |
| UTS | 71 | 30% | 21,30 |
| Tugas 2 | 89 | 20% | 17,80 |
| UAS | 78 | 30% | 23,40 |
| **Nilai Akhir** | | | **79,46 → B+** |

Ketercapaian CPMK mahasiswa tersebut:

- CPMK-1 = 0,50×84,8 + 0,50×71 = 42,40 + 35,50 = **77,9**
- CPMK-2 = 0,50×84,8 + 0,50×71 = 42,40 + 35,50 = **77,9**
- CPMK-3 = 0,20×71 + 0,30×89 + 0,50×78 = 14,20 + 26,70 + 39,00 = **79,9**
- CPMK-4 = 0,60×89 + 0,40×78 = 53,40 + 31,20 = **84,6**

Seluruh CPMK ≥ 60 → **tuntas CPMK**. Ketercapaian CPL:

- `CPL-05` (`P1`) = 1,00 × 79,46 = **79,46**

> **Catatan pembacaan:** nilai berbobot di atas adalah **kontribusi parsial** MK ini terhadap CPL-05 (P1). Ketercapaian CPL penuh dihitung pada tingkat prodi dengan mengagregasi kontribusi seluruh MK pembina CPL tersebut (Dokumen 008 Bagian 3.3–3.4). Nilai 79,46 bukan nilai CPL mahasiswa secara keseluruhan.

---

## 10. LEMBAR REKAP PENILAIAN (SPEED GRADING SHEET)

```
================================================================================
LEMBAR ASESMEN OBE CEPAT — STI-205 ALJABAR LINEAR DAN MATRIKS
Kelas: ____ | Semester: 2 | Tahun Akademik: ____ | Dosen: __________________
--------------------------------------------------------------------------------
No | NIM | Nama | T1 (20%)  | UTS (30%)   | T2 (20%)  | UAS (30%) | NA | Grade
   |     |      | [CPMK-1,2]| [CPMK-1,2,3]| [CPMK-3,4]| [Komp.]   |    |
--------------------------------------------------------------------------------
 1 |     |      |           |             |           |           |    |
 2 |     |      |           |             |           |           |    |
 3 |     |      |           |             |           |           |    |
--------------------------------------------------------------------------------
RATA-RATA CPMK-1: ____ | CPMK-2: ____ | CPMK-3: ____ | CPMK-4: ____
KETERCAPAIAN CPL: CPL-05 (P1) ____
================================================================================
```

**Petunjuk pengisian:** isi skor 0–100 per komponen; NA dihitung otomatis dengan rumus 9.1; kolom Grade diisi berdasarkan tabel 9.2; rekap CPMK dihitung dengan rumus Bagian 6.2 dokumen 055_4. Kolom verifikasi manual (C2) wajib diisi sebelum skor Tugas 2 dinyatakan final.

---

## 11. MODERASI, VALIDASI, DAN TINDAK LANJUT

| Aktivitas | Ketentuan |
|---|---|
| Validasi rubrik sebelum digunakan | Ditelaah Koordinator RMK dan UPM FSTI |
| Verifikasi kunci jawaban | Setiap kunci (urutan OBE, nilai eigen, matriks $U\Sigma V^T$) diperiksa penelaah kedua sebelum ujian |
| Verifikasi kode | Seluruh notebook contoh dijalankan ulang pada lingkungan bersih sebelum dijadikan acuan penilaian |
| Moderasi antar-kelas | 10% sampel dinilai ulang oleh dosen kedua; selisih > 10 poin dibahas bersama |
| Kalibrasi penilai | Sesi kalibrasi 60 menit sebelum penilaian tugas besar, menggunakan 3 sampel jawaban |
| Dokumentasi | Lembar skor per dimensi diarsipkan bersama artefak mahasiswa (termasuk notebook) |
| Revisi rubrik | Dilakukan bila > 20% mahasiswa memperoleh level 1 pada dimensi yang sama |
| Pelaporan | Rekap ke Koordinator RMK paling lambat 7 hari setelah asesmen |

---

## 12. RIWAYAT REVISI

| Versi | Tanggal | Perubahan | Penyusun |
|:---:|:---:|---|---|
| 1.0 | 07 November 2026 | Penyusunan awal; 6 rubrik (A–F) untuk 4 CPMK, dilengkapi kunci berlapis, verifikasi manual–komputasi, dan penanganan CPL tunggal | Tim Pengembang RPS SISTEKIN |

---

*Rubrik ini merupakan turunan langsung dari CPMK/Sub-CPMK Dokumen 043 dan skema asesmen Dokumen 008. Setiap perubahan bobot atau dimensi wajib disertai revisi dokumen 055_1 dan 055_4.*
