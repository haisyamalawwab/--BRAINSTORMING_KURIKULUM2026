# 069_3 — OUTLINE BUKU MODUL PEMBELAJARAN & PRAKTIKUM BERBASIS OBE
## STI-415 — GUDANG DATA & KECERDASAN BISNIS (*Data Warehouse & Business Intelligence*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.3.RPS-STI415` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 4  
**CPL:** `CPL-06` (`P2` = 45%) & `CPL-10` (`KK2` = 55%) [Level `R`] · **BoK:** `BK-IS02`, `BK-IS13`, `BK-IT09`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR + PRAKTIKUM

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Gudang Data & Kecerdasan Bisnis Modern: Dimensional Modeling Kimball, Pipeline ETL Otomatis, Analitik Kubus OLAP, hingga Executive Dashboard Power BI & Tableau* |
| **Target Tebal Naskah** | 14 Bab Materi + 14 Modul Praktikum Laboratorium + 2 Unit Evaluasi ($\pm 235\text{–}265\text{ halaman}$ A4) |
| **Pagar Pembatas Buku (*Guardrail*)** | Melanjutkan fondasi OLTP `FST-207` menuju arsitektur analitik OLAP, ETL, dan Dashboard KPI; tidak membahas *Data Mining* asosiasi/klasterisasi (`STI-520`), pelatihan ML (`STI-413`), maupun pemrosesan terdistribusi Spark/Kafka (`STA-601`). |

---

## 2. PETA KESELARASAN 14 BAB & 14 MODUL PRAKTIKUM TERHADAP CPMK & SUB-CPMK

| Bagian | Bab & Lab | Judul Bab Materi & Modul Praktikum | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Arsitektur DWH & Dimensional Modeling** | **Bab 1 / Lab 1** | Paradigma **OLTP vs OLAP** & Arsitektur Gudang Data (**Kimball vs Inmon**) | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2 / Lab 2** | Metodologi 4 Langkah Kimball, Penetapan **Grain**, & Perancangan **Star Schema** | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3 / Lab 3** | **Star vs Snowflake Schema**, *Conformed, Role-Playing,* & *Factless Fact Tables* | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | Tugas 1 (20%) |
| | **Bab 4 / Lab 4** | Pelacakan Kebenaran Historis dengan **Slowly Changing Dimensions (SCD Type 0–3)** | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Rekayasa Pipeline ETL & Kualitas Data** | **Bab 5 / Lab 5** | Arsitektur **ETL vs ELT**, *Staging Area*, & Ekstraksi Multi-Sumber Heterogen | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 6 / Lab 6** | Konsistensi **Data Cleaning**, Deduplikasi Entitas, & Penanganan *Quarantine Table* | Mg 6 | `CPMK-2` | `Sub-CPMK-2.2` | UTS (25%) |
| | **Bab 7 / Lab 7** | *Surrogate Key Lookup*, Pemuatan SCD, & Orkestrasi **Apache Airflow / Pentaho** | Mg 7 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Simulasi Ujian Praktik Pembangunan Pipeline ETL Multi-Sumber ke Star Schema (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (25%)* |
| **Bagian III:<br>Kubus OLAP & SQL Window Functions** | **Bab 8 / Lab 8** | Model Multidimensi & Operasi Kubus **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*) | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 9 / Lab 9** | Kueri Agregasi Multidimensi Lanjut (`ROLLUP`, `CUBE`, `GROUPING SETS`, & *Materialized View*) | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | Tugas 2 (25%) |
| | **Bab 10 / Lab 10** | **SQL Window Functions** Bagian I: Pemeringkatan, Segmentasi `NTILE`, & Pareto 80/20 | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (25%) |
| | **Bab 11 / Lab 11** | **SQL Window Functions** Bagian II: `LAG/LEAD`, *YoY/MoM Growth*, & *Moving Average* | Mg 12 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>KPI & Dashboard Business Intelligence** | **Bab 12 / Lab 12** | Kerangka **SMART KPI** Eksekutif, Prinsip Persepsi Visual, & Pemodelan Semantik BI | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 13 / Lab 13** | Rekayasa Ukuran Analitik (**DAX / Tableau LOD**), *Time Intelligence*, & *Drill-Through* | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 14 / Lab 14** | *Executive Data Storytelling*, Tata Kelola *Row-Level Security*, & *Handoff* ke `STI-520` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Akhir Solusi DWH–BI & Protokol Sidang Rapat Eksekutif (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB & MODUL PRAKTIKUM

#### BAB 1 & LAB 1: Paradigma OLTP vs OLAP & Arsitektur Gudang Data (Pekan 1)
* **Materi & Praktikum:** Konflik transaksi operasional vs kueri historis, perbandingan arsitektur *Enterprise Bus Kimball* vs *CIF Inmon*, penyusunan *Bus Matrix*, dan pengujian `EXPLAIN ANALYZE` 3NF vs *Star Schema*.

#### BAB 2 & LAB 2: Metodologi 4 Langkah Kimball, Penetapan Grain, & Star Schema (Pekan 2)
* **Materi & Praktikum:** Deklarasi *Grain*, jenis ukuran fakta (*Additive, Semi-Additive, Non-Additive*), *Surrogate Key* vs *Natural Key*, serta skrip pembangkitan `dim_date` kalender bisnis Indonesia.

#### BAB 3 & LAB 3: Star vs Snowflake Schema, Conformed Dimensions, & Factless Facts (Pekan 3)
* **Materi & Praktikum:** Kompromi normalisasi hierarki *Snowflake*, *Conformed Dimensions* untuk *drill-across* lintas *Data Mart*, *Role-Playing*, *Junk Dimensions*, dan *Factless Fact Tables*.

#### BAB 4 & LAB 4: Pelacakan Kebenaran Historis dengan Slowly Changing Dimensions (Pekan 4)
* **Materi & Praktikum:** Mekanisme teknis **SCD Type 0, 1, 2, 3,** dan *Hybrid*, pengelolaan tanggal masa berlaku baris (`valid_from`, `valid_to`, `is_current`), serta kueri titik-waktu historis.

#### BAB 5 & LAB 5: Arsitektur ETL vs ELT, Staging Area, & Ekstraksi Multi-Sumber (Pekan 5)
* **Materi & Praktikum:** Desain *Staging Area* idempoten, *Full vs Incremental Extraction (CDC)*, dan konektor ekstraksi RDBMS/CSV/JSON di *Pentaho Data Integration* dan Python.

#### BAB 6 & LAB 6: Konsistensi Data Cleaning, Deduplikasi Entitas, & Quarantine Table (Pekan 6)
* **Materi & Praktikum:** *Data Profiling*, standardisasi referensi master, penghapusan duplikat, anggota dimensi `Unknown (-1)`, dan isolasi baris cacat ke *error quarantine table*.

#### BAB 7 & LAB 7: Surrogate Key Lookup, Pemuatan SCD, & Orkestrasi Apache Airflow (Pekan 7)
* **Materi & Praktikum:** Aliran *Dimension Lookup/Update* $\rightarrow$ *Fact Surrogate Key Pipeline*, rekonsiliasi audit jumlah, serta penjadwalan **DAG Apache Airflow** / *Pentaho Job*.

#### BAB 8 & LAB 8: Model Multidimensi & Operasi Kubus OLAP (Pekan 9)
* **Materi & Praktikum:** Penyimpanan *MOLAP, ROLAP, HOLAP*, hierarki dimensi waktu/geografi/produk, dan implementasi praktis **Roll-up, Drill-down, Slice, Dice,** serta **Pivot**.

#### BAB 9 & LAB 9: Kueri Agregasi Multidimensi Lanjut (`ROLLUP`, `CUBE`, `GROUPING SETS`) (Pekan 10)
* **Materi & Praktikum:** Pembentukan subtotal dan *grand total* multi-poros dalam satu pemindaian tabel, fungsi penanda `GROUPING()`, dan akselerasi kueri dengan *Materialized Views*.

#### BAB 10 & LAB 10: SQL Window Functions Bagian I — Pemeringkatan & Analisis Pareto (Pekan 11)
* **Materi & Praktikum:** Klausa `OVER (PARTITION BY ... ORDER BY ...)`, perbedaan `ROW_NUMBER, RANK, DENSE_RANK`, pembagian kuartil `NTILE`, dan kurva kontribusi kumulatif **Pareto 80/20**.

#### BAB 11 & LAB 11: SQL Window Functions Bagian II — Analitik Deret Waktu Bisnis (Pekan 12)
* **Materi & Praktikum:** Pergeseran baris `LAG` dan `LEAD` untuk pertumbuhan **MoM / YoY**, *Window Frames* untuk rata-rata bergerak (*Moving Average*), serta analisis kohor retensi.

#### BAB 12 & LAB 12: Kerangka SMART KPI Eksekutif, Persepsi Visual, & Pemodelan Semantik BI (Pekan 13)
* **Materi & Praktikum:** Perumusan *KPI Dictionary* (*Balanced Scorecard, Leading vs Lagging*), prinsip desain kognitif *dashboard* Stephen Few, dan pemodelan relasi *Star Schema* di **Power BI / Tableau**.

#### BAB 13 & LAB 13: Rekayasa Ukuran Analitik (DAX / Tableau LOD) & Interaktivitas Dashboard (Pekan 14)
* **Materi & Praktikum:** Pembuatan *Explicit Measures* rasio aman, fungsi konteks **DAX** (`CALCULATE`, `SAMEPERIODLASTYEAR`, `TOTALYTD`) / *Tableau LOD*, *Dynamic Slicers*, dan **Drill-Through**.

#### BAB 14 & LAB 14: Executive Data Storytelling, Row-Level Security, & Handoff Kurikulum (Pekan 15)
* **Materi & Praktikum:** Struktur narasi rekomendasi eksekutif, penerapan **Row-Level Security (RLS)**, audit keterbacaan 5 detik, serta penyiapan *Data Mart* bagi `STI-520 Penambangan Data & Visualisasi Data`.
