# 069_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-415 — GUDANG DATA & KECERDASAN BISNIS (*Data Warehouse & Business Intelligence*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.3.RPS-STI415` · **Klaster Rubrik Master (Dok 018):** Klaster 2 (`K-2`)  
**CPL:** `CPL-06` (`P2` = 45%) & `CPL-10` (`KK2` = 55%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN REKAYASA GUDANG DATA & KECERDASAN BISNIS (`K-2`)

Mengacu **Dokumen 018 §3 (Klaster `K-2`)**, penilaian pada `STI-415` mengukur ketepatan perancangan skema dimensi yang bebas pencampuran granularitas (*grain*), integritas dan otomasi *pipeline* ETL (*zero silent data loss / zero duplicate inflation*), ketepatan kueri analitik OLAP & *SQL Window Functions*, serta kejujuran visual dan daya dukung keputusan dari *dashboard* KPI eksekutif.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-06` [C4])
**Objek Penilaian:** Analisis OLTP vs OLAP, Rancangan **Star & Snowflake Schema**, DDL DWH, & Simulasi **SCD**.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Analisis OLTP vs OLAP, *Bus Matrix*, & Deklarasi *Grain*** | **25%** | Menganalisis tajam hambatan OLTP, menyusun *Kimball Bus Matrix* utuh, dan mendeklarasikan *Grain* setiap tabel fakta secara atomik dan tak-ambigu. | Membedakan OLTP vs OLAP dengan tepat dan menetapkan *Grain* tabel fakta secara jelas. | Penjelasan perbedaan OLTP vs OLAP cukup benar, namun deklarasi *Grain* masih agak umum. | Mencampuradukkan dua tingkat granularitas berbeda (*header* faktur & baris item) ke dalam satu tabel fakta yang sama! | Tidak mampu membedakan skema OLTP dan OLAP. |
| **2. Rancangan **Star & Snowflake Schema** (*Fact & Dimension*)**<br>(`Sub-CPMK-1.1`) | **45%** | Skema **Star & Snowflake** sangat bersih memakai *surrogate keys*, pemisahan ukuran fakta (*additive/semi-additive*) tepat, `dim_date` kaya atribut, dan DDL PostgreSQL berjalan mulus. | Rancangan tabel fakta, tabel dimensi, relasi FK, dan implementasi DDL *Star/Snowflake* benar dan lengkap. | Skema bintang dasar terbentuk, namun masih menggunakan *natural key* string panjang sebagai PK dimensi. | Skema yang dibuat masih berupa ERD OLTP 3NF (bukan *Dimensional Modeling*). | Gagal menyusun skema fakta dan dimensi. |
| **3. Pengelolaan **Slowly Changing Dimensions (SCD)****<br>(`Sub-CPMK-1.2`) | **30%** | Mengimplementasikan **SCD Type 1 & Type 2** (`valid_from, valid_to, is_current`) secara akurat beserta bukti kueri yang menjaga kebenaran histori transaksi masa lalu. | Mekanisme kolom dan pembaruan baris pada SCD Type 2 berjalan benar sesuai skenario perubahan atribut. | Memahami perbedaan konsep SCD Type 1, 2, dan 3, namun skrip simulasi penutupan tanggal baris lama kurang rapi. | Menimpa atribut historis penting begitu saja (*Type 1* salah tempat) sehingga merusak laporan masa lalu. | Tidak mengimplementasikan mekanisme SCD. |

$$\text{Skor Tugas 1} = 0,25(K_1) + 0,45(K_2) + 0,30(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-10` [C6])
**Objek Penilaian:** Ujian Praktik 150 Menit: Pembangunan **Pipeline ETL Otomatis Multi-Sumber** & **Data Cleaning**.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Otomasi Ekstraksi Multi-Sumber & *Staging Area***<br>(`Sub-CPMK-2.1`) | **30%** | Pipeline mengekstrak ketiga sumber heterogen (*DB, CSV, JSON*) secara otomatis dan idempoten menuju *Staging Area* lengkap pencatatan log eksekusi. | Aliran ekstraksi ketiga sumber ke *Staging* berjalan otomatis tanpa intervensi manual di tengah jalan. | Berhasil mengekstrak minimal 2 dari 3 sumber secara otomatis, sumber ketiga masih dibantu langkah manual. | Menyunting berkas sumber CSV/JSON secara manual di Excel alih-alih membangun aliran ETL! | Pipeline ekstraksi gagal berjalan. |
| **2. Konsistensi Aturan **Data Cleaning** & *Quarantine***<br>(`Sub-CPMK-2.2`) | **35%** | Seluruh aturan pembersihan (standardisasi format, konversi tipe, penghapusan duplikat, `Unknown -1`, dan pengalihan baris rusak ke *quarantine table*) bekerja 100% konsisten. | Aturan *data cleaning* utama dan deduplikasi berjalan benar sehingga data bersih masuk ke gudang data. | Pembersihan *null* dan format dasar berjalan, namun deduplikasi entitas cabang/pelanggan belum tuntas penuh. | Data kotor/ganda lolos mentah-mentah ke tabel fakta sehingga menggandakan nilai total penjualan! | Tidak menerapkan tahapan *data cleaning*. |
| **3. *Surrogate Key Lookup*, Pemuatan SCD, & Rekonsiliasi** | **35%** | Urutan pemuatan dimensi (**SCD Type 2**) $\rightarrow$ *Surrogate Key Lookup* tabel fakta akurat 100%, dan hasil kueri rekonsiliasi omzet cocok persis dengan kunci jawaban. | Pemetaan *surrogate key* dan pemuatan tabel fakta berjalan benar dengan selisih rekonsiliasi nol/sangat minimal. | Tabel dimensi dan fakta terisi, namun terdapat sedikit baris fakta yang gagal terpetakan *surrogate key*-nya. | Memasukkan *natural key* mentah ke tabel fakta atau gagal menjaga integritas referensial FK. | Tabel fakta target kosong atau rusak. |

$$\text{Skor UTS} = 0,30(K_1) + 0,35(K_2) + 0,35(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-06` [C3])
**Objek Penilaian:** Studi Kasus Operasi Kubus **OLAP** & Portofolio Kueri Analitik **SQL Window Functions**.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Operasi Kubus **OLAP** & `ROLLUP/CUBE/GROUPING SETS`**<br>(`Sub-CPMK-3.1`) | **40%** | Mengimplementasikan *Roll-up, Drill-down, Slice, Dice, Pivot* serta `ROLLUP/CUBE/GROUPING SETS` dengan ringkas, cepat, dan pelabelan baris subtotal `GROUPING()` yang rapi. | Seluruh operasi kubus OLAP dan agregasi multidimensi menghasilkan angka ringkasan bisnis yang akurat. | Operasi *Roll-up/Slice/Dice* benar, namun penulisan subtotal masih memakai `UNION ALL` panjang alih-alih `ROLLUP`. | Salah mengagregasi ukuran *semi-additive* (menjumlahkan saldo stok lintas bulan!) atau hasil *join* menggembung (*fan trap*). | Kueri agregasi OLAP keliru atau tidak berjalan. |
| **2. Ketepatan & Efisiensi **SQL Window Functions****<br>(`Sub-CPMK-3.2`) | **40%** | Seluruh kueri `DENSE_RANK`, `NTILE`, Pareto kumulatif, pertumbuhan *YoY/MoM* (`LAG`), dan *Moving Average* (`ROWS BETWEEN`) akurat 100%, elegan, dan berkinerja cepat. | Sebagian besar ($\ge 85\%$) kueri *Window Functions* menghasilkan jawaban analitik yang benar dan bersih. | Kueri peringkat dasar (`RANK`) berjalan, namun perhitungan *Moving Average* atau pertumbuhan `LAG` kurang tepat pada batas partisi. | Tidak memakai *Window Functions* (memaksakan perhitungan manual di luar SQL atau *self-join* lambat yang salah hasil). | Gagal menulis kueri *SQL Window Functions*. |
| **3. Interpretasi Kinerja Bisnis & Verifikasi Lab** | **20%** | Menarik kesimpulan bisnis tajam dari setiap hasil kueri dan menyelesaikan tantangan modifikasi kueri 10 menit di lab dengan lancar. | Interpretasi angka tepat dan lulus uji modifikasi kueri saat verifikasi laboratorium. | Menyertakan penjelasan hasil kueri secara deskriptif cukup benar. | Hanya menempel tangkapan layar tabel angka tanpa interpretasi makna bisnisnya. | Tidak mampu memodifikasi kueri sendiri saat diuji di lab. |

$$\text{Skor Tugas 2} = 0,40(K_1) + 0,40(K_2) + 0,20(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-10` [C6])
**Objek Penilaian:** Proyek **Dashboard Business Intelligence Interaktif** (*Power BI / Tableau*), **KPI Book**, & Sidang Rapat Eksekutif.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Desain Visual & Interaktivitas **Dashboard BI****<br>(`Sub-CPMK-4.1`) | **35%** | Tata letak eksekutif memenuhi **5-Second Rule**, pemilihan bagan tepat secara kognitif, palet konsisten, serta fitur *cross-filtering, dynamic slicer,* dan **Drill-Through** bekerja sangat mulus. | Dashboard multi-halaman informatif, rapi, bebas distorsi visual, dan fitur interaktif berjalan baik. | Dashboard menampilkan bagan standar dengan fungsionalitas filter dasar, namun tata letak masih agak padat. | Penuh bagan tidak tepat (*3D Pie Chart* 15 irisan!), warna menyilaukan, dan tidak ada alur *drill-down*. | Dashboard tidak fungsional atau hanya berupa gambar statis. |
| **2. Perumusan **KPI**, Formula *DAX/LOD*, & Integritas Angka**<br>(`Sub-CPMK-4.2`) | **35%** | Minimal 6 **SMART KPI** relevan dilengkapi target & varians *YoY/MoM*; formula *Explicit Measures* (**DAX / LOD**) menangani agregasi rasio secara benar 100% dan angkanya cocok persis dengan SQL DWH. | KPI terdefinisi baik, perhitungan ukuran kustom akurat, dan model relasi *Star Schema* di perangkat BI bersih. | KPI dasar tersedia dan terhitung benar untuk tampilan utama, namun beberapa ukuran rasio belum tahan terhadap perubahan *slicer*. | Salah agregasi fatal (merata-rata persentase tanpa pembobotan!) atau angka *dashboard* tidak cocok dengan isi gudang data. | Tidak merumuskan KPI maupun formula analitik. |
| **3. *Executive Data Storytelling* & Rekomendasi Keputusan** | **15%** | Mengungkapkan temuan anomali bisnis nyata melalui penelusuran *drill-down* langsung dan merumuskan rekomendasi tindakan yang spesifik serta terukur dampaknya. | Menyampaikan cerita data yang runtut dan rekomendasi keputusan manajemen yang logis. | Presentasi menjelaskan isi grafik dengan cukup baik namun rekomendasi masih bersifat umum. | Sekadar membacakan judul grafik di layar tanpa wawasan pendukung keputusan. | Tidak menyertakan laporan/rekomendasi bisnis. |
| **4. Penguasaan Teknis Individu saat Sidang** | **15%** | Setiap anggota tim mampu membuat/memodifikasi ukuran *DAX/Calculated Field* atau menjawab pertanyaan *drill-down* spontan dari penguji secara cepat dan tepat. | Anggota tim menguasai bagian pemodelan data, rumus KPI, dan visualisasinya dengan baik. | Anggota mampu menjawab pertanyaan dasar mengenai sumber data dan grafik yang dibuatnya. | Anggota pasif dan gagal menjelaskan asal-usul perhitungan KPI pada *dashboard* kelompoknya. | Tidak hadir sidang UAS atau melanggar integritas akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,15(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF PRAKTIKUM LABORATORIUM MINGGUAN (LAB 1–14)

| Kriteria Formatif Lab | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketelitian Skema, ETL, & Rekonsiliasi Angka** | Selalu memvalidasi jumlah baris & total nilai uang sebelum dan sesudah proses ETL/OLAP sehingga bebas selisih. | Menyelesaikan seluruh tahapan modul praktikum tepat waktu dengan angka akurat. | Menyelesaikan minimal 75% instruksi praktikum dengan bimbingan asisten. | Gagal menuntaskan latihan dasar praktikum mingguan. |
| **Kerapian SQL & Dokumentasi Model BI** | Penamaan tabel/kolom (`dim_*`, `fact_*`), skrip SQL, dan *Measures* BI sangat terstandar serta terdokumentasi. | Kode SQL dan berkas praktikum tertata rapi dan mudah diperiksa. | Penamaan objek cukup terbaca namun format penulisan kueri belum konsisten. | Skrip berantakan dan tidak terdokumentasi. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-415` (`CPL-06` & `CPL-10` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai secara utuh perancangan **Dimensional Modeling & SCD**, rekayasa **pipeline ETL otomatis** berkualitas tinggi, kueri analitik **OLAP & SQL Window Functions** kompleks, serta pembuatan **Dashboard BI & KPI** eksekutif yang siap pakai di industri. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa mampu merancang *Star/Snowflake Schema*, membangun *pipeline* ETL multi-sumber bersih, menulis kueri analitik OLAP/Window SQL akurat, dan menyajikan *dashboard* KPI interaktif di Power BI/Tableau. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar minimal ketuntasan OBE ($\ge 65,0$) dalam pemodelan skema bintang dasar, aliran ETL standar, operasi kubus OLAP, dan pembuatan *dashboard* BI fungsional. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih mencampur skema OLTP dengan OLAP, meloloskan duplikat/data kotor pada ETL, keliru mengagregasi rasio/stok, atau membuat visualisasi tanpa nilai KPI. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal mencapai capaian dasar gudang data dan kecerdasan bisnis atau melakukan kecurangan akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-415` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menganalisis perbedaan OLTP vs OLAP serta merancang **Star & Snowflake Schema** gudang data. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu mengelola pelacakan perubahan historis menggunakan **Slowly Changing Dimensions (SCD)**. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu membangun **pipeline ETL otomatis** dari multi-sumber menggunakan *Pentaho / Airflow / Python*. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menerapkan aturan **data cleaning**, deduplikasi, dan penjaminan kualitas data yang konsisten. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengimplementasikan operasi kubus **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*). | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menulis kueri analitik bisnis menggunakan **SQL Window Functions** dan `ROLLUP/CUBE`. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu merancang **dashboard Business Intelligence** interaktif menggunakan *Power BI / Tableau*. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu merumuskan dan memvisualisasikan **KPI** sebagai pendukung keputusan eksekutif. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-415`)

```text
==============================================================================================================================
     LEMBAR REKAPITULASI PENILAIAN OBE — STI-415 GUDANG DATA & KECERDASAN BISNIS (3 SKS: T=2, P=1)
==============================================================================================================================
Semester / TA  : Semester 4 (Genap) / 2026-2027      CPL Dibebankan : CPL-06 (P2: 45%) & CPL-10 (KK2: 55%) [Level: Reinforce]
Klaster Rubrik : K-2 (RPL, Data & Enterprise)        Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2 (25%)    | UAS (30%)   | NA    | CPL-06 | CPL-10 | Huruf
   |           |                  | [CPMK-1:C4] | [CPMK-2:C6] | [CPMK-3:C3] | [CPMK-4:C6] | Akhir | (45%)  | (55%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 86.0        | 90.0        | 88.0        | 88.00 | 89.11  | 87.09  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 76.0        | 80.0        | 78.0        | 78.00 | 79.11  | 77.09  | B+
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 68.00 | 69.11  | 67.09  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 78.00       | 76.00       | 80.00       | 78.00       | 78.00 | 79.11  | 77.09  | >=65:100%
==============================================================================================================================
```
