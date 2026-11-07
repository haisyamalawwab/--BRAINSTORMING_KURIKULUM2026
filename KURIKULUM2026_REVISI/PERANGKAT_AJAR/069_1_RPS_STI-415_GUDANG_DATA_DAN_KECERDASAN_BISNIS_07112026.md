# 069_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-415 — GUDANG DATA & KECERDASAN BISNIS (*Data Warehouse & Business Intelligence*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.3.RPS-STI415`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Gudang Data & Kecerdasan Bisnis / *Data Warehouse & Business Intelligence* |
| **Kode Mata Kuliah** | `STI-415` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Rekayasa Data, Sistem Enterprise & Analitik Bisnis (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS (`+P`)** (`T = 2, P = 1`) — Tatap Muka `2×50' = 100'`, Praktikum Terbimbing `1×170' = 170'`, Penugasan Terstruktur `2×60' = 120'`, Belajar Mandiri `2×60' = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 4 (Genap) — Tahap Penguatan Analitik Enterprise (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `FST-207` Basis Data |
| **Mata Kuliah Hilir (*Handoff*)** | `STI-520` Penambangan Data & Visualisasi Data (Sem 5), `STA-601` Rekayasa Big Data dan Komputasi Terdistribusi (Sem 6), & `STC-501` Sistem Enterprise Terintegrasi (ERP/CRM/SCM) (Sem 5) |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-06` (`P2` = **45%**) dan `CPL-10` (`KK2` = **55%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 2 (`K-2`)** — Rekayasa Perangkat Lunak, Data & Sistem Enterprise (Bobot MK `+P`: Tugas 1 `20%` · UTS `25%` · Tugas 2 `25%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Rekayasa Data & Sistem Informasi Enterprise |
| **Koordinator RMK** | Dr. Istiadi, S.T., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-06`** (`P2`) | Pengetahuan | Menguasai konsep sistem informasi, analisis & pemodelan proses bisnis, arsitektur enterprise, manajemen proyek TI, serta konsep dasar kecerdasan artifisial dan pembelajaran mesin. | **R** (*Reinforce*) | **45%** |
| **`CPL-10`** (`KK2`) | Keterampilan Khusus | Mampu merancang arsitektur data, membangun *pipeline* rekayasa data (*ETL/ELT, Data Warehouse, Big Data*), serta menghasilkan visualisasi analitik untuk mendukung keputusan organisasi. | **R** (*Reinforce*) | **55%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menganalisis perbedaan OLTP vs OLAP serta merancang skema *Dimensional Modeling*** (*Star Schema, Snowflake Schema, Fact & Dimension Tables, Slowly Changing Dimensions*) (*B*) untuk kebutuhan analitik enterprise (*C*) secara tepat (*D*). | **C4** (*Analyze*) | `CPL-06` (`P2`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **membangun *pipeline* ETL (*Extract, Transform, Load*) otomatis** (*B*) dari multi-sumber data menggunakan perangkat ETL (*Pentaho / Apache Airflow / Python*) (*C*) dengan aturan *data cleaning* yang konsisten (*D*). | **C6** (*Create*) | `CPL-10` (`KK2`) | **UTS — Pekan 8 (25%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengimplementasikan operasi kubus OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*) dan kueri analitik *SQL Window Functions* (*B*) untuk menghasilkan ringkasan kinerja bisnis (*C*) secara cepat dan akurat (*D*). | **C3** (*Apply*) | `CPL-06` (`P2`) | **Tugas 2 — Pekan 12 (25%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **merancang *dashboard Business Intelligence* interaktif** (*Power BI / Tableau*) dan visualisasi **KPI** (*Key Performance Indicators*) (*B*) sebagai pendukung keputusan eksekutif (*C*) yang informatif (*D*). | **C6** (*Create*) | `CPL-10` (`KK2`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Merancang skema *Dimensional Modeling* (**Star & Snowflake Schema**) untuk gudang data. | `CPMK-1` | **C4** | Mg 1–3 |
| **`Sub-CPMK-1.2`** | Mengelola **Slowly Changing Dimensions (SCD)** (*Type 0, 1, 2, 3*) pada tabel dimensi historis. | `CPMK-1` | **C4** | Mg 3–4 |
| **`Sub-CPMK-2.1`** | Membangun *pipeline* **ETL** otomatis dari multi-sumber (*CSV, JSON, RDBMS OLTP*) dengan *Pentaho / Airflow / Python*. | `CPMK-2` | **C6** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Menerapkan aturan *data cleaning*, deduplikasi, pemetaan *surrogate key*, dan penjaminan kualitas data konsisten. | `CPMK-2` | **C6** | Mg 6–7 |
| **`Sub-CPMK-3.1`** | Mengimplementasikan operasi kubus **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*) pada *Data Mart*. | `CPMK-3` | **C3** | Mg 9–10 |
| **`Sub-CPMK-3.2`** | Menulis kueri analitik menggunakan **SQL Window Functions** (`OVER, PARTITION BY, RANK, LAG/LEAD`) & `ROLLUP/CUBE`. | `CPMK-3` | **C3** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Merancang **dashboard BI** interaktif menggunakan *Power BI / Tableau* berlandaskan prinsip komunikasi visual. | `CPMK-4` | **C6** | Mg 13–14 |
| **`Sub-CPMK-4.2`** | Merumuskan dan memvisualisasikan **KPI** sebagai pendukung keputusan eksekutif yang dapat ditindaklanjuti. | `CPMK-4` | **C6** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Siklus Utuh DWH & BI)

```text
[CPMK-4: Dashboard Business Intelligence Interaktif & Visualisasi KPI Eksekutif (Power BI / Tableau) (C6) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: DAX/Calculated Measures & Interactive BI Dashboard | Sub-CPMK-4.2: SMART KPIs & Executive Data Storytelling)
      │
[CPMK-3: Operasi Kubus Multidimensi OLAP & Kueri Analitik SQL Window Functions (C3) — Mg 9–12 (Tugas 2 25%)]
      ▲  (Sub-CPMK-3.1: Roll-up, Drill-down, Slice, Dice, Pivot | Sub-CPMK-3.2: GROUPING SETS, RANK, LAG/LEAD, Moving Average)
      │
[CPMK-2: Rekayasa Pipeline ETL Otomatis Multi-Sumber & Konsistensi Data Cleaning (C6) — Mg 5–8 (UTS 25%)]
      ▲  (Sub-CPMK-2.1: Staging & Multi-Source Extraction Pentaho/Airflow/Python | Sub-CPMK-2.2: Cleansing, Surrogate Key & SCD Load)
      │
[CPMK-1: Analisis OLTP vs OLAP, Dimensional Modeling (Star/Snowflake), & SCD (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Kimball Bus Matrix, Grain, Fact & Dimension Tables | Sub-CPMK-1.2: Slowly Changing Dimensions Type 1/2/3)
      ▲
[Fondasi Prasyarat: FST-207 Basis Data (OLTP 3NF & SQL Dasar) + Proses Bisnis FST-309]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-06`** (`P2`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-06` = 45%** |
| **`CPL-10`** (`KK2`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **25%** | — | — | **25%** | **`CPL-10` = 55%** *(25%+30%)* |
| **`CPL-06`** (`P2`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **25%** | — | **25%** | *(ke `CPL-06`: 20%+25%=45%)* |
| **`CPL-10`** (`KK2`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | *(ke `CPL-10`: 25%+30%=55%)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **25%** | **25%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-2` Dok 018; Target Dok 004 `70%`):** `Tugas 1 (20% — Case-Based Enterprise Dimensional Modeling) + Tugas 2 (25% — Case-Based OLAP & Executive Analytical SQL Investigation) + UAS (30% — Project-Based End-to-End DWH & BI Dashboard Solution)` = **75%** *(melampaui target 70% Dokumen 004)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-415 Gudang Data & Kecerdasan Bisnis` (3 SKS `+P`) membekali mahasiswa dengan kompetensi merancang arsitektur repositori data analitik terpusat serta mentransformasi data operasional lintas sistem menjadi wawasan strategis organisasi. Mahasiswa mendalami perbedaan fundamental basis data transaksional (**OLTP**) vs analitik (**OLAP**), arsitektur gudang data **Kimball (*Bottom-Up Bus Matrix*) vs Inmon (*Top-Down Enterprise*)**, pemodelan dimensi (*Grain, Fact Tables, Conformed/Degenerate Dimensions, Star vs Snowflake Schema,* & **Slowly Changing Dimensions [SCD Type 1, 2, 3]**), pembangunan **pipeline ETL otomatis** multi-sumber beserta aturan *data profiling, cleansing, deduplication,* dan *surrogate key lookup* menggunakan **Pentaho Data Integration / Apache Airflow / Python**, kueri analitik kubus **OLAP** & **SQL Window Functions**, hingga perancangan **dashboard Business Intelligence** interaktif dan perumusan **KPI** eksekutif menggunakan **Power BI / Tableau**.

* **🟢 IN-SCOPE (Wajib Diajarkan):** OLTP vs OLAP, Metodologi Kimball 4-Langkah, **Star & Snowflake Schema**, **Slowly Changing Dimensions (SCD)**, rekayasa **ETL/ELT** otomatis & *data cleaning*, operasi kubus **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*), **SQL Window Functions** (`OVER, PARTITION BY, RANK, LAG/LEAD, ROLLUP, CUBE`), *DAX / Calculated Measures*, desain **KPI**, dan **Dashboard BI** interaktif.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. Dilarang mengulang perancangan ERD transaksional dan normalisasi 1NF–3NF dasar (sudah tuntas di **`FST-207 Basis Data`**).
  2. Dilarang mengajarkan algoritma *Association Rule Mining* (*Apriori/FP-Growth*) atau *Clustering* eksploratif lanjutan (ranah **`STI-520 Penambangan Data & Visualisasi Data`**).
  3. Dilarang melatih model prediktif *Machine Learning* (ranah ko-semester **`STI-413 Pembelajaran Mesin`**) maupun pemrosesan *stream/cluster Big Data* terdistribusi Apache Spark/Kafka (ranah **`STA-601 Rekayasa Big Data dan Komputasi Terdistribusi`**).
* **🔄 HANDOFF ANCHOR:** Menghasilkan *Data Warehouse / Data Mart* bersih berstandar *Star Schema* yang siap ditambang polanya pada **`STI-520 Penambangan Data & Visualisasi Data`** dan diskalakan ke *Data Lakehouse* pada **`STA-601 Rekayasa Big Data dan Komputasi Terdistribusi`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS02` (*Data & Information Management*), `BK-IS13` (*Business Intelligence & Analytics*), & `BK-IT09` (*Data Warehousing*).

**Pustaka Utama:**
1. Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). Wiley. *(Rujukan Utama Standar Industri Dimensional Modeling)*
2. Vaisman, A., & Zimányi, E. (2022). *Data Warehouse Systems: Design and Implementation* (2nd ed.). Springer.
3. Sharda, R., Delen, D., & Turban, E. (2020). *Analytics, Data Science, & Artificial Intelligence: Systems for Decision Support* (11th ed.). Pearson.

**Pustaka Pendukung:**
4. Russo, M., & Ferrari, A. (2020). *The Definitive Guide to DAX: Business Intelligence for Microsoft Power BI, SQL Server Analysis Services, and Excel* (2nd ed.). Microsoft Press.
5. Dokumentasi Resmi PostgreSQL *Window Functions & Grouping Sets*, Pentaho Data Integration (Kettle) / Apache Airflow, Microsoft Power BI, & Tableau Public.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Teori + Praktikum) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Bagian I):** Menganalisis perbedaan beban kerja **OLTP vs OLAP** serta membandingkan arsitektur **Kimball vs Inmon** [C4] | 1.1.1 Ketepatan membedakan karakteristik transaksi OLTP (3NF, *write-heavy*, baris tunggal) vs analitik OLAP (denormalisasi dimensi, *read-heavy*, agregasi historis jutaan baris).<br>1.1.2 Ketepatan memetakan *Enterprise Data Warehouse Bus Matrix* lintas proses bisnis organisasi. | **Kriteria:** Analisis alasan kegagalan pelaporan langsung di atas DB OLTP tepat.<br>**Teknik:** Studi kasus kemacetan pelaporan *e-commerce* + praktikum tolok ukur kueri 3NF vs Star di PostgreSQL. | **Interactive Lecture** `[TM: 100']`<br>**Praktikum Lab 1:** Eksperimen Perbandingan Kecepatan Kueri Analitik di Atas Skema OLTP 3NF vs OLAP `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kontrak belajar, unduh basis data sampel OLTP ritel (*Northwind/AdventureWorks*) di LMS Edlink. | Ekosistem Kecerdasan Bisnis, Perbedaan **OLTP vs OLAP**, Arsitektur *Staging–DWH–Data Mart*, & **Kimball vs Inmon** `[1] Bab 1; [2] Bab 2` | — |
| **2** | **`Sub-CPMK-1.1` (Bagian II):** Merancang **Star Schema** dengan metodologi **4 Langkah Kimball** (*Business Process, Grain, Dimensions, Facts*) [C4] | 1.1.3 Ketepatan menetapkan tingkat rincian baris fakta (**Grain**) secara eksplisit sebelum memilih dimensi dan ukuran fakta (*Additive, Semi-Additive, Non-Additive Facts*).<br>1.1.4 Ketepatan merancang *Surrogate Keys*, *Date Dimension* kaya atribut kalender, dan *Degenerate Dimension*. | **Kriteria:** Deklarasi *Grain* tidak ambigu dan tabel fakta bersih dari pencampuran granularitas.<br>**Teknik:** Latihan perancangan *Star Schema* penjualan & inventori + implementasi DDL DWH. | **Case-Based Modeling** `[TM: 100']`<br>**Praktikum Lab 2:** Perancangan Fisik **Star Schema** & Pembangkitan *Enterprise Date Dimension* di PostgreSQL `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis penetapan *Grain* & jenis fakta (*Additive vs Semi-Additive* saldo stok!) di LMS Edlink. | Metodologi 4 Langkah Kimball, Penetapan **Grain**, *Fact Table Types* (*Transaction, Periodic Snapshot, Accumulating Snapshot*), & **Star Schema** `[1] Bab 2–3` | — |
| **3** | **`Sub-CPMK-1.1` & `1.2` (Bagian I):** Membandingkan **Star vs Snowflake Schema**, *Conformed/Junk/Role-Playing Dimensions*, & konsep perubahan atribut historis [C4] | 1.1.5 Ketepatan mengevaluasi kapan normalisasi hierarki dimensi (**Snowflake Schema**) dibenarkan vs kapan harus dihindari demi kesederhanaan *join* BI.<br>1.2.1 Ketepatan merancang *Role-Playing Dimension* (mis. `order_date_key`, `ship_date_key` merujuk 1 `dim_date`). | **Kriteria:** Pemilihan Star vs Snowflake memiliki justifikasi performa & pemeliharaan yang kuat.<br>**Teknik:** Review desain skema *Data Mart* lintas departemen di lab. | **Comparative Design Lecture** `[TM: 100']`<br>**Praktikum Lab 3:** Implementasi **Snowflake vs Star Schema**, *Conformed Dimensions*, & *Factless Fact Table* `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi studi kasus enterprise **Tugas 1 (RTM-1)** di LMS Edlink. | **Star vs Snowflake Schema**, *Conformed, Role-Playing, & Junk Dimensions*, serta *Factless Fact Tables* `[1] Bab 4–6` | — |
| **4** | **`Sub-CPMK-1.2` (Bagian II):** Mengelola **Slowly Changing Dimensions (SCD Type 0, 1, 2, 3)** untuk pelacakan kebenaran historis [C4]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.2 Ketepatan mengimplementasikan **SCD Type 2** lengkap kolom `surrogate_key`, `natural_key`, `effective_start_date`, `effective_end_date`, dan `is_current` agar histori wilayah pelanggan tidak tertimpa. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-2`)**.<br>**Teknik:** Pengumpulan Dokumen & DDL Skema *Dimensional Modeling* + Presentasi/Uji Kasus SCD di Lab. | **Problem-Solving SCD & Uji Tugas 1** `[TM: 100']`<br>**Praktikum Lab 4:** Simulasi Perubahan Historis **SCD Type 1, 2, & 3** serta Verifikasi **Tugas 1 (`CPMK-1`)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Strategi Pelacakan Historis: **Slowly Changing Dimensions (SCD Type 0, 1, 2, 3, & Hybrid)** `[1] Bab 5` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1`:** Merancang arsitektur **ETL vs ELT**, *Staging Area*, & ekstraksi otomatis multi-sumber (*RDBMS OLTP, CSV/Excel, REST JSON*) [C5→C6] | 2.1.1 Ketepatan membangun alur ekstraksi multi-sumber menuju *Staging Area* menggunakan perangkat ETL (**Pentaho Data Integration / Python SQLAlchemy-Pandas**) tanpa membebani DB operasional. | **Kriteria:** Ekstraksi multi-sumber berjalan idempoten dan tercatat pada tabel *ETL Audit Log*.<br>**Teknik:** Praktikum pembangunan aliran ekstraksi 3 sumber heterogen di lab. | **Interactive Lecture ETL** `[TM: 100']`<br>**Praktikum Lab 5:** Pembangunan *Staging Area* & Ekstraksi Multi-Sumber dengan **Pentaho (Kettle) / Python ETL** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Unduh paket data mentah multi-sumber berderau di LMS Edlink. | Arsitektur **ETL vs ELT**, Peran *Staging Area*, Ekstraksi Penuh vs *Incremental (CDC)*, & Pengantar Perangkat ETL `[1] Bab 19; [2] Bab 8` | — |
| **6** | **`Sub-CPMK-2.2` (Bagian I):** Menerapkan aturan **Data Cleaning**, standardisasi format, deduplikasi entitas, & penanganan *missing/invalid records* (*Reject/Quarantine Table*) [C6] | 2.2.1 Ketepatan membangun transformasi pembersihan otomatis (standardisasi kode provinsi, konversi mata uang/tanggal tidak seragam, deduplikasi pelanggan ganda, dan isolasi baris cacat ke *quarantine table* alih-alih menggagalkan seluruh *batch*!). | **Kriteria:** 100% data yang lolos ke tabel dimensi/fakta memenuhi aturan kualitas skema.<br>**Teknik:** Praktikum transformasi kualitas data di lab. | **Case-Based Data Quality** `[TM: 100']`<br>**Praktikum Lab 6:** Transformasi **Data Cleaning**, Deduplikasi, & *Error Quarantine Handling* pada Pipeline ETL `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis penanganan *Late Arriving Dimension / Inferred Member* di LMS Edlink. | *Data Profiling*, Dimensi Kualitas Data, Aturan **Data Cleaning**, Deduplikasi, & Penanganan Anomali ETL `[1] Bab 19` | — |
| **7** | **`Sub-CPMK-2.1` & `2.2` (Bagian II):** Pemuatan (*Loading*) Tabel Dimensi (**SCD Lookup**) & Tabel Fakta (*Surrogate Key Pipeline*) serta Orkestrasi Penjadwalan **Apache Airflow / Cron Job** + Klinik UTS [C6] | 2.2.2 Ketepatan menyusun urutan pemuatan (*Dimension Load* lebih dulu $\rightarrow$ *Surrogate Key Lookup* $\rightarrow$ *Fact Table Bulk Insert*) dan mendefinisikan DAG alur ketergantungan tugas pada **Apache Airflow** / *Job Pentaho*. | **Kriteria:** Pipeline ETL berjalan otomatis satu klik dari sumber mentah hingga *Star Schema* terisi utuh.<br>**Teknik:** Uji jalan *end-to-end automated ETL* & klinik persiapan UTS di lab. | **ETL Orchestration & Klinik UTS** `[TM: 100']`<br>**Praktikum Lab 7:** *Surrogate Key Lookup*, Otomasi **DAG Apache Airflow / Pentaho Job**, & Simulasi UTS `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Latihan simulasi ujian praktik ETL multi-sumber di LMS Edlink. | Pemuatan Dimensi (**SCD Type 2 Lookup**), *Surrogate Key Pipeline* Fakta, & Orkestrasi **Apache Airflow** `[1] Bab 19–20; [5]` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C6]** | Keberhasilan membangun secara mandiri **Pipeline ETL Otomatis** yang mengekstrak 3 sumber data kotor berbeda format, menerapkan aturan *data cleaning* konsisten, memetakan *surrogate keys* & pembaruan **SCD**, serta memuatnya ke dalam skema gudang data target tanpa kehilangan/duplikasi transaksi. | **Kriteria:** **Rubrik Analitik UTS Praktik (`K-2`)**.<br>**Teknik:** Ujian Praktik *Live Engineering* Pipeline ETL Terawasi di Laboratorium. | **Ujian Praktik Pembangunan Pipeline ETL di Lab**<br>`[150 menit]` | Pengarsipan artefak *pipeline* ETL & nilai `CPMK-2` pada portal OBE. | Materi Ekstraksi Multi-Sumber, *Data Cleaning*, *Surrogate Key & SCD Lookup*, serta Otomasi ETL (Pekan 5–7) | **25%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1`:** Mengimplementasikan konsep kubus multidimensi (**OLAP Cube**) dan lima operasi analitik inti (**Roll-up, Drill-down, Slice, Dice, Pivot**) [C3] | 3.1.1 Ketepatan membedakan arsitektur penyimpanan *MOLAP, ROLAP, & HOLAP*.<br>3.1.2 Ketepatan mengeksekusi dan menginterpretasikan operasi **Roll-up** (kota $\rightarrow$ provinsi $\rightarrow$ nasional), **Drill-down**, **Slice**, **Dice**, dan **Pivot** (*cross-tabulation*) di atas *Star Schema*. | **Kriteria:** Setiap operasi kubus OLAP menjawab pertanyaan analitik manajemen secara tepat.<br>**Teknik:** Praktikum eksplorasi kubus OLAP di PostgreSQL & Pivot Analitik. | **Interactive Lecture OLAP** `[TM: 100']`<br>**Praktikum Lab 8:** Eksplorasi Kubus Multidimensi **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*) `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Unduh basis data *Data Mart* 500.000 baris transaksi untuk lab paruh kedua di LMS Edlink. | Model Multidimensi (*MOLAP/ROLAP*), Hierarki Dimensi, & Operasi Kubus **OLAP** `[2] Bab 3 & 6` | — |
| **10** | **`Sub-CPMK-3.1` & `3.2` (Bagian I):** Menulis kueri agregasi multidimensi lanjut menggunakan ekstensi SQL OLAP (`GROUP BY ROLLUP`, `CUBE`, `GROUPING SETS`, & `FILTER`) [C3] | 3.2.1 Ketepatan menggantikan puluhan kueri `UNION ALL` manual dengan satu ekspresi `GROUPING SETS / ROLLUP / CUBE` lengkap fungsi `GROUPING()` penanda baris subtotal & *grand total*. | **Kriteria:** Kueri menghasilkan tabel laporan berjenjang lengkap subtotal dalam satu kali pemindaian.<br>**Teknik:** Praktikum kueri pelaporan keuangan/penjualan berjenjang di lab. | **Problem-Based SQL OLAP** `[TM: 100']`<br>**Praktikum Lab 9:** Kueri Agregasi Multidimensi **`ROLLUP`, `CUBE`, & `GROUPING SETS`** di PostgreSQL `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi spesifikasi studi kasus analitik **Tugas 2 (RTM-2)** di LMS Edlink. | Ekstensi SQL Analitik: **`GROUP BY ROLLUP`, `CUBE`, `GROUPING SETS`**, & Optimasi *Materialized Views* `[2] Bab 7; [5]` | — |
| **11** | **`Sub-CPMK-3.2` (Bagian II):** Menguasai **SQL Window Functions** (`OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`) untuk pemeringkatan dan segmentasi bisnis [C3] | 3.2.2 Ketepatan menulis kueri analitik peringkat *Top-N produk per kategori per kuartal*, analisis kontribusi **Pareto 80/20** kumulatif, dan kuartil pelanggan tanpa merusak rincian baris. | **Kriteria:** Pemakaian `PARTITION BY` dan `ORDER BY` pada klausa `OVER(...)` akurat dan bebas *subquery* berbelit.<br>**Teknik:** Tantangan 10 kueri bisnis *Window Ranking* di laboratorium. | **Live SQL Coding Lecture** `[TM: 100']`<br>**Praktikum Lab 10:** Kueri Pemeringkatan & Pareto Bisnis dengan **SQL Window Functions (`RANK`, `NTILE`, Kumulatif)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis perbedaan hasil `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` saat nilai seri di LMS Edlink. | **SQL Window Functions** Bagian I: Partisi Jendela, Fungsi Pemeringkatan, & Distribusi Kumulatif `[2] Bab 7; [5]` | — |
| **12** | **`Sub-CPMK-3.2` (Bagian III):** Kueri analitik deret waktu dengan **SQL Window Frames** (`LAG`, `LEAD`, *Year-over-Year / Month-over-Month Growth*, & *Moving Average*) [C3]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.3 Ketepatan menghitung pertumbuhan *MoM/YoY* (`LAG`), rata-rata bergerak 3/7 periode (`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`), dan retensi kohor pelanggan. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-2`)**.<br>**Teknik:** Pengumpulan Portofolio Kueri OLAP & *SQL Window Functions* + Uji Modifikasi Kueri Langsung di Lab. | **Time-Series SQL & Uji Tugas 2** `[TM: 100']`<br>**Praktikum Lab 11:** Pertumbuhan *YoY/MoM* (`LAG/LEAD`), *Moving Average*, & Verifikasi **Tugas 2 (`CPMK-3`)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas **Tugas 2 (`CPMK-3`)** di LMS Edlink. | **SQL Window Functions** Bagian II: `LAG`, `LEAD`, *Window Framing* (`ROWS/RANGE`), & Analitik Pertumbuhan Waktu `[2] Bab 7; [5]` | **25%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.2` & `4.1` (Bagian I):** Merancang kerangka **Key Performance Indicators (KPI)** eksekutif (*SMART KPIs, Leading vs Lagging Indicators, Balanced Scorecard*) & pemilihan visual yang jujur [C5→C6] | 4.2.1 Ketepatan membedakan *Vanity Metrics* (mis. total unduhan kumulatif) vs **Actionable KPIs** (mis. *Net Revenue Retention, Gross Margin %, On-Time In-Full Delivery %* terhadap target!).<br>4.1.1 Ketepatan memilih jenis bagan yang sesuai kaidah persepsi visual Stephen Few (anti-*3D Pie Chart* berlebihan). | **Kriteria:** Setiap KPI memiliki definisi rumus, target ambang (*threshold*), pembanding periode, dan pemilik keputusan.<br>**Teknik:** Lokakarya penyusunan *KPI Dictionary* & *Dashboard Wireframe* proyek UAS. | **Executive BI Design Lecture** `[TM: 100']`<br>**Praktikum Lab 12:** Penyusunan *KPI Dictionary*, Koneksi Gudang Data ke **Power BI / Tableau**, & *Semantic Model* `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Panduan & rubrik proyek akhir **Dashboard BI Eksekutif (UAS)** dirilis di LMS Edlink. | Manajemen Kinerja Bisnis, Perancangan **SMART KPI**, Prinsip Persepsi Visual, & Pemodelan Semantik BI `[3] Bab 3 & 9` | — |
| **14** | **`Sub-CPMK-4.1` (Bagian II):** Membangun ukuran terhitung dinamis (**DAX / Tableau Calculated Fields & Time Intelligence**) serta interaktivitas *Cross-Filtering & Drill-Through* [C6] | 4.1.2 Ketepatan menulis ekspresi **DAX** (`CALCULATE`, `DIVIDE`, `TOTALYTD`, `SAMEPERIODLASTYEAR`) atau *Tableau LOD Expressions* serta merancang halaman **Drill-Through** dari ringkasan direksi ke detail cabang/produk. | **Kriteria:** Ukuran KPI merespons dinamis seluruh *slicer* waktu/wilayah/segmen tanpa salah agregasi rasio!<br>**Teknik:** Praktikum pembangunan *Measures* & interaksi *dashboard* di **Power BI / Tableau**. | **Hands-On BI Engineering** `[TM: 100']`<br>**Praktikum Lab 13:** Formula **DAX / LOD Expressions**, *Time Intelligence*, & Interaktivitas **Power BI / Tableau** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Unduh *cheat-sheet* DAX & *Tableau LOD* di LMS Edlink. | Bahasa Analitik **DAX** / *Tableau Calculated Fields*, *Time Intelligence*, *Dynamic Slicers*, & *Drill-Through* `[4] Bab 1–5` | — |
| **15** | **`Sub-CPMK-4.1` & `4.2` (Sintesis):** *Executive Data Storytelling*, tata kelola akses baris (*Row-Level Security* dasar), & *Usability Review* **Dashboard BI** Pra-UAS [C6] | 4.2.2 Ketepatan menyusun narasi rekomendasi bisnis berbasis temuan anomali pada *dashboard* serta memastikan keterbacaan eksekutif dalam aturan **5-Second Rule**. | **Kriteria:** Eksekutif dapat menangkap status kesehatan bisnis dalam 5 detik pertama melihat layar utama.<br>**Teknik:** *Peer Executive Walkthrough* & klinik penyempurnaan proyek UAS di lab. | **Storytelling & Klinik UAS** `[TM: 100']`<br>**Praktikum Lab 14:** *Row-Level Security* Dasar, Audit Keterbacaan **Dashboard BI**, & Klinik Akhir Proyek UAS `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas paket proyek DWH–ETL–Dashboard BI UAS di LMS Edlink. | *Executive Data Storytelling*, Tata Kelola BI (*Single Source of Truth & RLS*), serta *Handoff* ke `STI-520` & `STA-601` `[3] Bab 9; [4]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C6]** | Kualitas perancangan **Dashboard Business Intelligence Interaktif** (*Power BI / Tableau*) di atas *Star Schema* gudang data, ketepatan perumusan & visualisasi **KPI**, serta ketajaman rekomendasi keputusan eksekutif. | **Kriteria:** **Rubrik Analitik UAS (`K-2`)**.<br>**Teknik:** Penilaian Artefak Proyek BI & *KPI Book* (50% UAS) + Sidang *Executive Boardroom Simulation* & Uji *Drill-Down* Langsung (50% UAS). | **Sidang Presentasi Eksekutif *Dashboard Business Intelligence* & Verifikasi Teknis**<br>`[150 menit]` | Pengarsipan berkas proyek BI & nilai akhir `CPL-06` dan `CPL-10` pada portal OBE. | Integrasi Menyeluruh Gudang Data, Analitik KPI, & *Executive Business Intelligence Dashboard* | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-06` [C4])
* **Bentuk Instrumen:** Studi Kasus **Perancangan Arsitektur Gudang Data & Dimensional Modeling Enterprise** (mis. Jaringan Ritel Omnichannel / Rumah Sakit Rujukan / Logistik Nasional): mahasiswa menganalisis kelemahan skema OLTP sumber, menyusun *Kimball Bus Matrix*, menetapkan *Grain*, merancang **Star & Snowflake Schema** lengkap implementasi DDL PostgreSQL, serta menyimulasikan pelacakan perubahan historis **Slowly Changing Dimensions (SCD Type 1 & Type 2)**.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Ketajaman analisis OLTP vs OLAP & penetapan *Bus Matrix / Grain* = **25%**; (2) Ketepatan rancangan **Star/Snowflake Schema** (*Fact & Dimension Tables*) (`Sub-CPMK-1.1`) = **45%**; (3) Ketepatan mekanisme **SCD Type 1/2/3** (`Sub-CPMK-1.2`) = **30%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 25% · Mengukur `CPMK-2` / `CPL-10` [C6])
* **Bentuk Instrumen:** **Ujian Praktik *Live Engineering* Pipeline ETL di Laboratorium** (150 menit, individu): diberikan 3 sumber data heterogen berderau (tabel OLTP PostgreSQL, berkas CSV cabang, dan JSON produk/kurs), mahasiswa membangun **pipeline ETL otomatis** (*Pentaho / Python ETL*) dengan aturan *data cleaning* konsisten, isolasi baris cacat, pemetaan *surrogate key*, dan pemuatan **SCD Type 2** ke skema DWH target.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Otomasi ekstraksi multi-sumber & struktur *Staging* (`Sub-CPMK-2.1`) = **30%**; (2) Konsistensi aturan **Data Cleaning**, deduplikasi, & *quarantine* (`Sub-CPMK-2.2`) = **35%**; (3) Kebenaran *Surrogate Key Lookup*, pemuatan **SCD**, & rekonsiliasi jumlah transaksi = **35%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 25% · Mengukur `CPMK-3` / `CPL-06` [C3])
* **Bentuk Instrumen:** Studi Kasus Analitik **Eksplorasi Kubus OLAP & Portofolio 12 Kueri Bisnis SQL Window Functions** (diverifikasi langsung di lab): mahasiswa menjawab 12 pertanyaan strategis manajemen (analisis *Roll-up/Drill-down/Slice/Dice/Pivot*, subtotal `ROLLUP/CUBE`, *Top-3* per wilayah `DENSE_RANK`, Pareto 80/20, pertumbuhan *YoY/MoM* `LAG`, dan *3-Month Moving Average*) di atas *Data Mart* ratusan ribu baris secara cepat dan akurat.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Ketepatan implementasi operasi kubus **OLAP** & `ROLLUP/CUBE/GROUPING SETS` (`Sub-CPMK-3.1`) = **40%**; (2) Ketepatan & efisiensi kueri **SQL Window Functions** (`Sub-CPMK-3.2`) = **40%**; (3) Interpretasi ringkasan kinerja bisnis & uji modifikasi kueri di lab = **20%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-10` [C6])
* **Bentuk Instrumen:** **Proyek Akhir Solusi Gudang Data & Dashboard Business Intelligence Eksekutif** (50% nilai UAS: proyek kelompok maks. 3 mahasiswa membangun *Data Mart* terisi bersih + **Dashboard Interaktif Power BI / Tableau** multi-halaman lengkap *KPI Dictionary*, formula *DAX/LOD*, dan laporan rekomendasi eksekutif) + **Sidang Simulasi Rapat Direksi & Uji *Drill-Down* Individu** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kualitas desain visual, struktur informasi, & interaktivitas **Dashboard BI** (`Sub-CPMK-4.1`) = **35%**; (2) Ketepatan perumusan **KPI**, kebenaran rumus *DAX/Calculated Measures*, & integritas data DWH (`Sub-CPMK-4.2`) = **35%**; (3) Ketajaman *data storytelling* & rekomendasi keputusan eksekutif = **15%**; (4) Penguasaan teknis individu saat sidang tanya-jawab = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Rekayasa Data & SI Enterprise**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Istiadi, S.T., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
