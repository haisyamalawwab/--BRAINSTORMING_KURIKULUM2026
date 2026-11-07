# 069_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-415 — GUDANG DATA & KECERDASAN BISNIS (*Data Warehouse & Business Intelligence*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.3.RPS-STI415` · **Bobot:** 3 SKS `+P` (`TM 100'`, `Prak 170'`, `PT 120'`, `BM 120'`) · **Semester:** 4  
**Prasyarat:** `FST-207` Basis Data · **CPL:** `CPL-06` (`P2` = 45%) & `CPL-10` (`KK2` = 55%) [Level `R`]  
**Klaster Rubrik:** `K-2` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu & Asisten Laboratorium `STI-415` |
|---|---|
| **Struktur Waktu per Sesi** | **Sesi Teori (`100'`):** Pendahuluan Kasus Bisnis `15'` · Inti Arsitektur DWH/BI `70'` · Sintesis `15'`<br>**Sesi Praktikum Lab (`170'`):** *Briefing* Skema/Data `15'` · Rekayasa Skema/ETL/OLAP/BI Terbimbing `135'` · Verifikasi Rekonsiliasi Angka `20'`, diikuti `PT 120'` & `BM 120'`. |
| **Perangkat Lunak Lab** | PostgreSQL 16 + DBeaver/pgAdmin, Pentaho Data Integration (Kettle) / Apache Airflow / Python ETL, Microsoft Power BI Desktop / Tableau Public. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** mengulang materi normalisasi OLTP 3NF dasar (`FST-207`), dilarang mengajarkan algoritma *Apriori/Clustering* (`STI-520`) maupun pelatihan model ML (`STI-413`), serta dilarang membahas klaster terdistribusi Spark/Kafka (`STA-601`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Teori (`100'`) & Modul Praktikum (`170'`) | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Teori: **OLTP vs OLAP** & Arsitektur Kimball vs Inmon · Lab 1: Benchmark Kueri 3NF vs Star | 270' | Formatif Lab |
| **2** | `Sub-CPMK-1.1` | Teori: Metodologi 4 Langkah Kimball & **Star Schema** · Lab 2: DDL Fakta & *Date Dimension* | 270' | Formatif Lab |
| **3** | `Sub-CPMK-1.1, 1.2` | Teori: **Star vs Snowflake**, *Conformed & Role-Playing Dim* · Lab 3: Pemodelan Multi-Mart | 270' | Formatif Lab |
| **4** | `Sub-CPMK-1.2` | Teori: **Slowly Changing Dimensions (SCD 0/1/2/3)** · Lab 4: Simulasi SCD & Uji **Tugas 1** | 270' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Teori: Arsitektur **ETL vs ELT** & *Staging Area* · Lab 5: Ekstraksi Multi-Sumber Pentaho/Python | 270' | Formatif Lab |
| **6** | `Sub-CPMK-2.2` | Teori: **Data Cleaning**, Deduplikasi, & *Quarantine* · Lab 6: Transformasi Kualitas Data | 270' | Formatif Lab |
| **7** | `Sub-CPMK-2.1, 2.2` | Teori: *Surrogate Key Lookup*, SCD Load, & **Airflow** · Lab 7: Otomasi DAG & Klinik UTS | 270' | Formatif Lab |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** *Live Engineering* Pipeline ETL Otomatis Multi-Sumber | 150' | **UTS (25%)** |
| **9** | `Sub-CPMK-3.1` | Teori: Kubus **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*) · Lab 8: Eksplorasi Kubus | 270' | Formatif Lab |
| **10** | `Sub-CPMK-3.1, 3.2` | Teori: SQL Analitik `ROLLUP`, `CUBE`, `GROUPING SETS` · Lab 9: Laporan Subtotal Multidimensi | 270' | Formatif Lab |
| **11** | `Sub-CPMK-3.2` | Teori: **SQL Window Functions** (`RANK, NTILE`, Pareto) · Lab 10: Kueri Peringkat & Segmen | 270' | Formatif Lab |
| **12** | `Sub-CPMK-3.2` | Teori: `LAG/LEAD`, *YoY/MoM Growth*, & *Moving Avg* · Lab 11: Analitik Waktu & Uji **Tugas 2** | 270' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-4.1, 4.2` | Teori: Desain **SMART KPI** & Prinsip Persepsi Visual · Lab 12: *Semantic Model* Power BI/Tableau | 270' | Formatif Lab |
| **14** | `Sub-CPMK-4.1` | Teori: Formula **DAX / LOD** & *Time Intelligence* · Lab 13: *Dynamic Measures & Drill-Through* | 270' | Formatif Lab |
| **15** | `Sub-CPMK-4.1, 4.2` | Teori: *Executive Data Storytelling* & Tata Kelola BI · Lab 14: *RLS* & Audit Proyek UAS | 270' | Formatif Lab |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Eksekutif *Dashboard BI* & Uji *Drill-Down* Langsung | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (TEORI + PRAKTIKUM)

### PERTEMUAN 1 — Beban Kerja **OLTP vs OLAP** & Arsitektur Gudang Data (**Kimball vs Inmon**)
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Alat:** PostgreSQL 16, DBeaver.
* **Sesi Teori (`100'`):** Membuka kuliah dengan kasus nyata: mengapa kueri laporan tahunan direksi pada pukul 10.00 pagi membuat mesin kasir (POS OLTP) melambat drastis? Membedah kontras **OLTP vs OLAP**, lapisan *Source $\rightarrow$ Staging $\rightarrow$ Enterprise DWH $\rightarrow$ Data Mart*, perbandingan paradigma **Ralph Kimball** (*Dimensional Data Mart Bus*) vs **Bill Inmon** (*Corporate Information Factory*), dan menyusun *Enterprise Bus Matrix*.
* **Sesi Praktikum Lab 1 (`170'`):** Menjalankan kueri agregasi penjualan 8-*table join* di atas basis data OLTP 3NF vs 2-*table join* di atas skema dimensi menggunakan `EXPLAIN ANALYZE` untuk melihat selisih biaya eksekusi secara nyata.
* **PT (`120'`) & BM (`120'`):** Menyusun *Bus Matrix* 5 proses bisnis × 7 dimensi bersama untuk studi kasus universitas/rumah sakit.

### PERTEMUAN 2 — Metodologi 4 Langkah Kimball & Perancangan **Star Schema**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Alat:** PostgreSQL, `dbdiagram.io` / Draw.io.
* **Sesi Teori (`100'`):** Membedah empat keputusan wajib Kimball: (1) Pilih proses bisnis, (2) Deklarasikan **Grain** sejelas satu kalimat atomik, (3) Identifikasi dimensi (*who, what, where, when, why, how*), (4) Identifikasi ukuran fakta (*Additive, Semi-Additive* seperti saldo rekening/stok gudang yang tidak boleh dijumlah lintas tanggal!, dan *Non-Additive* seperti persentase margin), serta alasan wajib memakai **Surrogate Key** integer dibanding *Natural Key* operasional.
* **Sesi Praktikum Lab 2 (`170'`):** Merancang dan mengeksekusi DDL **Star Schema** ritel beserta skrip SQL pembangkit `dim_date` 10 tahun lengkap atribut kuartal fiskal, akhir pekan, dan hari libur nasional Indonesia.
* **PT (`120'`) & BM (`120'`):** Merancang tabel fakta *Periodic Snapshot* untuk pemantauan stok harian gudang.

### PERTEMUAN 3 — **Star vs Snowflake Schema**, *Conformed, Role-Playing, & Junk Dimensions*
* **Sub-CPMK:** `Sub-CPMK-1.1` & `1.2` [C4] · **Alat:** PostgreSQL & Perangkat Pemodelan Skema.
* **Sesi Teori (`100'`):** Menganalisis kapan dimensi dinormalisasi menjadi **Snowflake Schema** dan konsekuensi penalti *join*-nya pada mesin BI; membahas pola lanjutan Kimball: *Conformed Dimensions* (jembatan *drill-across* antar *Data Mart*), *Role-Playing Dimensions*, *Junk Dimensions* (penggabungan bendera status kecil), dan *Factless Fact Tables* (mis. presensi kuliah / cakupan promosi). Merilis resmi **Tugas 1 (RTM-1)**.
* **Sesi Praktikum Lab 3 (`170'`):** Mengimplementasikan skema multi-*Data Mart* (*Sales Fact* & *Shipment Fact*) yang berbagi *Conformed Dimensions* serta melakukan kueri *drill-across*.
* **PT (`120'`) & BM (`120'`):** Mengerjakan rancangan skema dimensi pada **Tugas 1**.

### PERTEMUAN 4 — **Slowly Changing Dimensions (SCD Type 0, 1, 2, 3)** & Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alat:** PostgreSQL.
* **Sesi Teori (`100'`):** Jika seorang pelanggan pindah domisili dari Malang ke Surabaya pada 2026, apakah histori pembelian tahun 2025-nya ikut berubah menjadi penjualan cabang Surabaya? Membedah solusi **SCD Type 0** (*Retain Original*), **Type 1** (*Overwrite*), **Type 2** (*Add New Row* dengan `surrogate_key`, `valid_from`, `valid_to`, `is_current`), dan **Type 3** (*Add New Attribute*).
* **Sesi Praktikum Lab 4 (`170'`):** Menulis prosedur pembaruan **SCD Type 2** di SQL serta melaksanakan verifikasi dan presentasi singkat pengumpulan **Tugas 1 (`CPMK-1`)**.
* **PT (`120'`) & BM (`120'`):** Menyiapkan lingkungan Pentaho Data Integration / Python ETL untuk modul rekayasa *pipeline*.

### PERTEMUAN 5 — Arsitektur **ETL vs ELT**, *Staging Area*, & Ekstraksi Multi-Sumber
* **Sub-CPMK:** `Sub-CPMK-2.1` [C5→C6] · **Alat:** Pentaho Data Integration (Kettle) / Python `SQLAlchemy` + `pandas`.
* **Sesi Teori (`100'`):** Membandingkan pola **ETL** klasik vs **ELT** gudang data modern, aturan emas *Staging Area* (dilarang mengekstrak ulang dari DB produksi berulang kali jika transformasi gagal di tengah jalan!), serta strategi *Full Load* vs *Incremental Extraction / Change Data Capture (CDC)* berbasis kolom `updated_at`.
* **Sesi Praktikum Lab 5 (`170'`):** Membangun aliran ekstraksi otomatis yang menarik data dari 3 sumber berbeda (tabel PostgreSQL OLTP, berkas CSV logistik cabang, dan JSON katalog harga) ke dalam skema `staging` lengkap tabel pencatatan *ETL Run Audit*.
* **PT (`120'`) & BM (`120'`):** Menambahkan mekanisme pengambilan inkremental berdasarkan cap waktu terakhir (*watermark*).

### PERTEMUAN 6 — Konsistensi **Data Cleaning**, Deduplikasi, & *Quarantine Table*
* **Sub-CPMK:** `Sub-CPMK-2.2` [C6] · **Alat:** Pentaho / Python ETL.
* **Sesi Teori (`100'`):** *"Garbage In, Executive Disaster Out"* — membedah 6 dimensi kualitas data (*Completeness, Uniqueness, Validity, Consistency, Timeliness, Accuracy*) dan pola rekayasa transformasi pembersihan: standardisasi penulisan kota (`"MLG", "Kota Malang", "malang"` $\rightarrow$ `"KOTA MALANG"`), konversi tipe aman, deduplikasi rekaman ganda, penanganan *Unknown/Not Applicable Member* (`surrogate_key = -1`), serta penyaluran baris rusak ke tabel `etl_quarantine`.
* **Sesi Praktikum Lab 6 (`170'`):** Mengimplementasikan modul transformasi *data cleaning* komprehensif yang menyaring 8 jenis cacat data sengaja diinjeksikan pada berkas sumber.
* **PT (`120'`) & BM (`120'`):** Menyusun kueri pemeriksaan rekonsiliasi jumlah nilai transaksi antara sumber bersih dan target.

### PERTEMUAN 7 — *Surrogate Key Lookup*, Pemuatan SCD, & Orkestrasi **Apache Airflow** + Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-2.1` & `2.2` [C6] · **Alat:** Apache Airflow / Pentaho Job Scheduler, PostgreSQL.
* **Sesi Teori (`100'`):** Menguraikan urutan kritis pemuatan gudang data: muat seluruh tabel dimensi terlebih dahulu (*Dimension Lookup/Update SCD Type 2*), lalu jalankan **Surrogate Key Pipeline** pada aliran fakta untuk menukar *natural keys* menjadi *surrogate keys* berkecepatan tinggi, dan mengorkestrasikan ketergantungan tugas (*DAG: Extract $\rightarrow$ Cleanse $\rightarrow$ Load_Dims $\rightarrow$ Load_Facts $\rightarrow$ Data_Quality_Check*) menggunakan **Apache Airflow** / *Pentaho Job*.
* **Sesi Praktikum Lab 7 (`170'`):** Menjalankan *pipeline* ETL otomatis ujung-ke-ujung hingga seluruh *Star Schema* terisi valid, diikuti simulasi ujian praktik **UTS Pekan 8**.
* **PT (`120'`) & BM (`120'`):** Persiapan mandiri menghadapi ujian praktik rekayasa ETL pada UTS.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C6]) · **Bobot:** **25%** · **Durasi:** `150 menit` (*Live Engineering* di Lab).
* **Pelaksanaan:** Mahasiswa membangun secara mandiri **pipeline ETL otomatis** dari 3 sumber data heterogen berderau menuju skema DWH target, menerapkan aturan *data cleaning* konsisten, *surrogate key lookup*, dan pembaruan **SCD Type 2**, yang dinilai langsung berdasarkan kebenaran isi tabel target dan rekonsiliasi total transaksi.

### PERTEMUAN 9 — Kubus Multidimensi **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C3] · **Alat:** PostgreSQL *Star Schema* (500.000 baris transaksi) & DBeaver.
* **Sesi Teori (`100'`):** Evaluasi hasil UTS lalu beralih ke pemanfaatan gudang data: arsitektur **MOLAP, ROLAP, HOLAP** dan kelima manuver navigasi kubus **OLAP** (*Roll-up* naik hierarki, *Drill-down* turun ke rincian penyebab, *Slice* memotong 1 dimensi tunggal, *Dice* memfilter sub-kubus multi-dimensi, serta *Pivot* memutar sumbu baris-kolom).
* **Sesi Praktikum Lab 8 (`170'`):** Mengeksekusi kelima operasi kubus OLAP secara sistematis untuk mendiagnosis penurunan laba kuartalan suatu lini produk hingga menemukan cabang pemicunya.
* **PT (`120'`) & BM (`120'`):** Latihan menyusun matriks *Pivot* penjualan per kategori × kuartal di SQL.

### PERTEMUAN 10 — Ekstensi SQL Analitik: `ROLLUP`, `CUBE`, `GROUPING SETS`, & *Materialized Views*
* **Sub-CPMK:** `Sub-CPMK-3.1` & `3.2` [C3] · **Alat:** PostgreSQL 16.
* **Sesi Teori (`100'`):** Mengajarkan sintaks standar ISO SQL OLAP (`GROUP BY ROLLUP(...)`, `CUBE(...)`, `GROUPING SETS(...)`, fungsi `GROUPING()`, dan klausa `FILTER (WHERE ...)`) untuk menghasilkan laporan agregasi berjenjang super cepat, serta penggunaan **Materialized Views** untuk pra-agregasi *Data Mart*. Merilis resmi **Tugas 2 (RTM-2)**.
* **Sesi Praktikum Lab 9 (`170'`):** Membangun kueri laporan eksekutif berjenjang wilayah–cabang–kategori lengkap subtotal dan *Materialized View* terindeks.
* **PT (`120'`) & BM (`120'`):** Mengerjakan soal bagian kubus OLAP pada **Tugas 2**.

### PERTEMUAN 11 — **SQL Window Functions** Bagian I: Pemeringkatan, Kuartil, & Analisis Pareto
* **Sub-CPMK:** `Sub-CPMK-3.2` [C3] · **Alat:** PostgreSQL 16.
* **Sesi Teori (`100'`):** Membedah anatomi fungsi jendela `fungsi() OVER (PARTITION BY ... ORDER BY ...)`: mengapa `GROUP BY` menghilangkan baris detail sedangkan *Window Function* tidak; perbandingan perilaku seri pada `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, segmentasi kuartil `NTILE(4)`, dan perhitungan proporsi kumulatif **Pareto 80/20**.
* **Sesi Praktikum Lab 10 (`170'`):** Menyelesaikan 10 skenario kueri analitik bisnis (termasuk *Top-3 produk terlaris di setiap provinsi* dan identifikasi *20% pelanggan penyumbang 80% omzet*).
* **PT (`120'`) & BM (`120'`):** Melanjutkan penulisan portofolio kueri analitik pada **Tugas 2**.

### PERTEMUAN 12 — **SQL Window Functions** Bagian II: `LAG/LEAD`, *YoY/MoM Growth*, *Moving Average*, & Evaluasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.2` [C3] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alat:** PostgreSQL 16.
* **Sesi Teori (`100'`):** Menguasai analitik deret waktu murni di dalam SQL: perbandingan periode sebelumnya (`LAG`, `LEAD`) untuk menghitung persentase pertumbuhan **Month-over-Month (MoM)** dan **Year-over-Year (YoY)**, penghalusan fluktuasi dengan *Moving Average* (`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`), dan retensi pelanggan.
* **Sesi Praktikum Lab 11 (`170'`):** Uji modifikasi kueri langsung dan verifikasi pengumpulan **Tugas 2 (`CPMK-3`)** di laboratorium, dilanjutkan penetapan kelompok dan domain bisnis proyek **Dashboard BI UAS**.
* **PT (`120'`) & BM (`120'`):** Menyusun daftar pertanyaan keputusan eksekutif untuk proyek UAS.

### PERTEMUAN 13 — Perancangan **SMART KPI** Eksekutif & Koneksi Gudang Data ke **Power BI / Tableau**
* **Sub-CPMK:** `Sub-CPMK-4.2` & `4.1` [C5→C6] · **Alat:** Microsoft Power BI Desktop / Tableau Public + PostgreSQL DWH.
* **Sesi Teori (`100'`):** Mengajarkan kerangka perumusan **Key Performance Indicators (KPI)** yang bernilai strategis (*Leading vs Lagging Indicators*, perbandingan aktual vs target vs periode lalu) dan kaidah desain kognitif Stephen Few (tata letak hierarki Z/F, rasio *data-ink* tinggi, palet warna ramah buta warna, larangan *gauge/3D pie* membingungkan).
* **Sesi Praktikum Lab 12 (`170'`):** Menghubungkan **Power BI / Tableau** langsung ke skema *Star Schema* PostgreSQL, memvalidasi arah kardinalitas relasi `1:*` (*Single-Direction Star Filter*), dan menyusun *KPI Wireframe*.
* **PT (`120'`) & BM (`120'`):** Merampungkan *KPI Dictionary* 6–8 metrik utama proyek akhir tim.

### PERTEMUAN 14 — Formula **DAX / Tableau LOD**, *Time Intelligence*, & Interaktivitas *Drill-Through*
* **Sub-CPMK:** `Sub-CPMK-4.1` [C6] · **Alat:** Power BI (*DAX*) / Tableau (*Calculated Fields & LOD*).
* **Sesi Teori (`100'`):** Mengapa menjumlahkan kolom persentase margin di laporan BI adalah dosa fatal analitik? Mengajarkan pembuatan **Explicit Measures** dengan **DAX** (`SUMX`, `DIVIDE`, `CALCULATE`, `ALL`, `TOTALYTD`, `SAMEPERIODLASTYEAR`) atau *Tableau Level of Detail (`FIXED/INCLUDE`)*, *Conditional Formatting* ambang KPI, *Bookmark*, dan halaman **Drill-Through**.
* **Sesi Praktikum Lab 13 (`170'`):** Membangun halaman utama *Executive Overview* dan halaman *Operational Drill-Through* interaktif pada proyek *dashboard* BI kelompok.
* **PT (`120'`) & BM (`120'`):** Menuntaskan pembangunan visualisasi seluruh halaman *dashboard* UAS.

### PERTEMUAN 15 — *Executive Data Storytelling*, Tata Kelola *Row-Level Security*, & Klinik Pra-UAS
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C6] · **Alat:** Power BI / Tableau.
* **Sesi Teori (`100'`):** Mengajarkan teknik *Data Storytelling* (*Context $\rightarrow$ Conflict/Anomaly $\rightarrow$ Root-Cause Drill-Down $\rightarrow$ Actionable Recommendation*), konfigurasi dasar **Row-Level Security (RLS)** agar kepala cabang hanya melihat data cabangnya sendiri, serta penjelasan *handoff* menuju `STI-520 Penambangan Data & Visualisasi Data` dan `STA-601`.
* **Sesi Praktikum Lab 14 (`170'`):** Audit keterbacaan **5-Second Rule** antar-kelompok, pengujian konsistensi angka *dashboard* terhadap kueri SQL gudang data (wajib cocok 100%!), dan gladi bersih presentasi direksi.
* **PT (`120'`) & BM (`120'`):** Finalisasi berkas `.pbix`/`.twbx`, skrip DWH-ETL, dan dek rekomendasi eksekutif UAS.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C6]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Artefak Dashboard BI Interaktif, *KPI Book*, & Skema Gudang Data (50% nilai UAS)** dengan **Sidang Simulasi Rapat Eksekutif & Pengujian *Drill-Down* Individu (50% nilai UAS)** di laboratorium.
