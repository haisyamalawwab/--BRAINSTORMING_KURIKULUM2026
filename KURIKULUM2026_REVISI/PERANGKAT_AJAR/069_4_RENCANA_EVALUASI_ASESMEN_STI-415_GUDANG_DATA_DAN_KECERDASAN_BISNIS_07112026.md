# 069_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-415 — GUDANG DATA & KECERDASAN BISNIS (*Data Warehouse & Business Intelligence*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.3.RPS-STI415` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 4  
**Klaster Asesmen MK (Dok 018):** Klaster 2 (`K-2`) — Rekayasa Perangkat Lunak, Data & Sistem Enterprise  
**CPL Dibebankan:** `CPL-06` (`P2` = **45%**) & `CPL-10` (`KK2` = **55%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 008, 018,** dan **043**, mata kuliah `STI-415 Gudang Data & Kecerdasan Bisnis` (3 SKS `+P`) menggunakan skema bobot baku Klaster `K-2` (`20% / 25% / 25% / 30%`) dengan pemetaan presisi 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-06` / `P2`)** — *Case-Based Enterprise Dimensional Modeling (Star/Snowflake Schema & SCD)*.
* **UTS (Pekan 8 — 25%) → `CPMK-2` (`CPL-10` / `KK2`)** — *Live Lab Exam: Multi-Source Automated ETL Pipeline & Data Cleaning*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-06` / `P2`)** — *Case-Based OLAP Cube Investigation & Executive SQL Window Functions Portfolio*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-10` / `KK2`)** — *Project-Based Executive Business Intelligence Dashboard (Power BI / Tableau), KPI Design, & Boardroom Defense*.
* **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-2` Dok 018; Target Dok 004 `70%`):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75%` berbasis studi kasus analitik enterprise dan proyek *dashboard* BI nyata.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-06`**<br>(`P2` — 45%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus enterprise: Analisis OLTP vs OLAP & rancangan **Star/Snowflake Schema** | **RTM-1 (Tugas 1)** Bagian Skema + DDL + Rubrik Analitik T1 | Sumatif | 12% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Studi kasus enterprise: Pengelolaan **Slowly Changing Dimensions (SCD Type 1/2/3)** | **RTM-1 (Tugas 1)** Bagian Simulasi SCD + Verifikasi Lab + Rubrik T1 | Sumatif | 8% | |
| **`CPL-10`**<br>(`KK2` — 55%)<br>*Level: R* | **`CPMK-2`**<br>(C6) | `Sub-CPMK-2.1` | Mg 8 | Ujian praktik lab 150': Pembangunan **pipeline ETL otomatis** multi-sumber (*Pentaho/Airflow/Python*) | **Soal Praktik UTS** (Aliran Ekstraksi & Pemuatan) + Rubrik UTS | Sumatif | 13% | **25%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian praktik lab 150': Penerapan aturan **data cleaning**, deduplikasi, & rekonsiliasi konsisten | **Soal Praktik UTS** (Transformasi Kualitas Data) + Rubrik UTS | Sumatif | 12% | |
| **`CPL-06`**<br>(`P2` — 45%)<br>*Level: R* | **`CPMK-3`**<br>(C3) | `Sub-CPMK-3.1` | Mg 12 | Studi kasus analitik bisnis: Implementasi operasi kubus **OLAP** & agregasi `ROLLUP/CUBE` | **RTM-2 (Tugas 2)** Bagian Kubus OLAP + Rubrik Analitik T2 | Sumatif | 11% | **25%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Studi kasus analitik bisnis: Kueri kinerja bisnis menggunakan **SQL Window Functions** | **RTM-2 (Tugas 2)** Bagian *Window SQL* + Uji Modifikasi Lab + Rubrik T2 | Sumatif | 14% | |
| **`CPL-10`**<br>(`KK2` — 55%)<br>*Level: R* | **`CPMK-4`**<br>(C6) | `Sub-CPMK-4.1` | Mg 16 | Proyek akhir BI + sidang: Perancangan **dashboard BI** interaktif (*Power BI / Tableau*) | **Artefak Proyek `.pbix/.twbx`** + Demo Interaktif + Rubrik UAS | Sumatif | 16% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek akhir BI + sidang: Perumusan & visualisasi **KPI** pendukung keputusan eksekutif | **Dokumen *KPI Book* & Sidang Rapat Direksi UAS** + Rubrik UAS | Sumatif | 14% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN PRAKTIK

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Perancangan Dimensional Modeling & SCD Enterprise)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Verifikasi Lab **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-06`).
* **Spesifikasi Pengerjaan Individu:**
  1. Diberikan skema ERD OLTP ternormalisasi dari sebuah perusahaan multi-cabang; mahasiswa menganalisis hambatan pelaporan OLTP, menyusun *Kimball Bus Matrix*, mendeklarasikan *Grain*, serta merancang **Star Schema** dan varian **Snowflake Schema** lengkap skrip DDL PostgreSQL.
  2. Mendemonstrasikan mekanisme **Slowly Changing Dimensions (SCD Type 1 & Type 2)** dengan menyertakan skenario nyata perubahan atribut dimensi dan kueri pembuktian bahwa laporan historis tetap utuh.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Rekayasa Pipeline ETL Otomatis Multi-Sumber)
* **Format & Bobot:** Ujian Praktik *Live Engineering* di Laboratorium (**150 menit**, individu) · Bobot **25%** (`CPMK-2` → `CPL-10`).
* **Spesifikasi Soal Praktik:**
  1. Diberikan 3 sumber data mentah berderau (tabel transaksi PostgreSQL OLTP, berkas CSV daftar cabang/pelanggan dengan duplikat & penulisan tidak seragam, serta berkas JSON katalog produk); mahasiswa membangun **pipeline ETL otomatis** menggunakan *Pentaho Data Integration* atau *Python ETL + Airflow DAG*.
  2. Pipeline wajib menerapkan *data cleaning* konsisten, memisahkan baris cacat ke *quarantine table*, melakukan *surrogate key lookup* dan pembaruan **SCD Type 2**, serta lulus kueri rekonsiliasi jumlah omzet terhadap sumber bersih.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Investigasi Kubus OLAP & Kueri Analitik SQL Window Functions)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Uji Lab **Pekan 12** · Bobot **25%** (`CPMK-3` → `CPL-06`).
* **Spesifikasi Teknis Individu:**
  1. Menjawab 12 pertanyaan kinerja bisnis direksi di atas *Data Mart* 500.000 baris dengan mengimplementasikan operasi kubus **OLAP** (*Roll-up, Drill-down, Slice, Dice, Pivot*), `GROUP BY ROLLUP/CUBE/GROUPING SETS`, serta **SQL Window Functions** (`DENSE_RANK`, `NTILE`, kontribusi Pareto, pertumbuhan *YoY/MoM* dengan `LAG`, dan *3-Month Moving Average*).
  2. Saat sesi praktikum Pekan 12, dosen memberikan 1 variasi kueri mendadak selama 10 menit untuk memverifikasi penguasaan asli mahasiswa.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Proyek Dashboard Business Intelligence Eksekutif)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-10`), memadukan **Proyek Tim Solusi DWH & Dashboard BI (50% nilai UAS)** + **Sidang Simulasi Rapat Direksi & Uji *Drill-Down* Individu (50% nilai UAS, 150 menit)**:
  1. Tim (maks. 3 orang) membangun solusi BI utuh di atas *Star Schema* nyata menggunakan **Microsoft Power BI** atau **Tableau** yang minimal memuat 3 layar saling terhubung (*Executive KPI Overview*, *Commercial/Operational Performance Analysis*, dan *Root-Cause Drill-Through*).
  2. Menyertakan **KPI Dictionary** (minimal 6 SMART KPI dengan formula *DAX / Tableau LOD* eksplisit dan pembanding target/*YoY*) serta mempresentasikan 3 rekomendasi keputusan bisnis berbasis bukti data di hadapan penguji.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-415}}$)
$$NA_{\text{STI-415}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
1. **Ketercapaian `CPL-06` (`P2` — bobot 45% MK dari `CPMK-1` [20%] + `CPMK-3` [25%]):**
   $$\text{Score}_{\text{CPL-06, STI-415}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,25\,S_{\text{Tugas 2}}(i)}{0,45}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,45 = 1,35\text{ SKS}$).*
2. **Ketercapaian `CPL-10` (`KK2` — bobot 55% MK dari `CPMK-2` [25%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-10, STI-415}}(i) = \frac{0,25\,S_{\text{UTS}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,55}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,55 = 1,65\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**; remedial diberikan maksimal 1 kali bagi mahasiswa dengan skor CPMK $< 65,0$ dengan nilai plafon pasca-remedial **70,0 (B)**.
