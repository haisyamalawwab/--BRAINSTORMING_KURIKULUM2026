# 057_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI (*Information Technology Systems Architecture and Organization*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 1 — Tahap Fondasi)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI103`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `057_1_RPS_STI-103_...md` · `057_2_SAP_STI-103_...md` · Dok 007 §5 · Dok 043.

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Buku Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Arsitektur dan Organisasi Sistem Teknologi Informasi: Dari Gerbang Biner hingga Infrastruktur Server Cloud & AI* |
| **Kode & Bobot MK** | `STI-103` · 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · Semester 1 |
| **CPL & BoK Didukung** | `CPL-05` (`P1`), `CPL-07` (`P3`), `CPL-02` (`KU1`) [Level *Introduce*] · `BK-IS03` (*IT Infrastructure*), `BK-IT01` (*IT Fundamentals*), `BK-IT05` (*Platform Technologies*) |
| **Target Tebal Naskah Utuh** | 14 Bab Materi Inti + 2 Unit Evaluasi Komprehensif ($\pm 190\text{–}230\text{ halaman}$ A4/B5 dilengkapi diagram skema blok, tabel penelusuran register, dan lembar *benchmarking* industri) |
| **Anatomi Baku Setiap Bab** | (1) *Sub-CPMK & Indikator*; (2) *Kasus Pemicu Infrastruktur TI Modern*; (3) *Uraian Konsep & Diagram Organisasi Perangkat Keras*; (4) *Panduan Eksplorasi Simulator Web Ringan*; (5) *Studi Kasus Teknis & Perhitungan Kinerja*; (6) *Kotak Boundary Guardrail*; (7) *Rangkuman & Soal Evaluasi Mandiri*. |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen Terkait |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Mesin Von Neumann & Representasi Data** | **Bab 1** | Evolusi Komputasi, Arsitektur vs Organisasi, & Model Von Neumann vs Harvard | Mg 1 | `CPMK-1` | `Sub-CPMK-1.2` | Tugas 1 (20%) |
| | **Bab 2** | Sistem Bilangan Biner/Heksadesimal, *Two's Complement*, & Kode Karakter | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Representasi *Floating Point* IEEE 754 & Penelusuran Siklus `Fetch-Decode-Execute` | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Logika Digital, Sekuensial, & Organisasi ALU** | **Bab 4** | Gerbang Logika Biner, Aljabar Boole Perangkat Keras, & Peta Karnaugh | Mg 4 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 5** | Rangkaian Logika Kombinasional (*Adder, MUX, Decoder*) & Konstruksi ALU | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 6** | Rangkaian Sekuensial: *Latch*, *Flip-Flop*, Register Perangkat Keras, & *Counter* | Mg 6 | `CPMK-2` | `Sub-CPMK-2.2` | UTS (30%) |
| | **Bab 7** | Integrasi *CPU Datapath* (Register + ALU + Kontrol) & Pengantar *Pipelining* | Mg 7 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Simulasi Analisis Rangkaian Kombinasional, Sekuensial, & ALU (Persiapan UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Arsitektur Prosesor, Memori, & Akselerator AI** | **Bab 8** | Arsitektur Set Instruksi: Komparasi Kritis CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`) | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 9** | Hierarki Memori (SRAM vs DRAM), Lokalitas, & Kinerja *Cache* `L1/L2/L3` | Mg 10 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 10** | Penyimpanan Sekunder Modern (NVMe SSD, HDD, RAID) & Peran Hardware MMU/TLB | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 11** | Komputasi Paralel & Akselerator Domain-Spesifik: CPU vs GPU vs NPU/TPU | Mg 12 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Bus/I-O, Virtualisasi, & Server Data Center** | **Bab 12** | Sistem Interkoneksi Bus (PCIe), *Interrupt-Driven I/O*, & *Direct Memory Access* (DMA) | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13** | Abstraksi Virtualisasi Perangkat Keras (`VT-x/AMD-V`) & Evaluasi *Hypervisor* | Mg 14 | `CPMK-4` | `Sub-CPMK-4.2` | UAS (30%) |
| | **Bab 14** | Organisasi Infrastruktur *Server Data Center* Modern untuk Komputasi Awan | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Studi Kasus Audit Arsitektur Infrastruktur Sistem TI & Persiapan UAS* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2` & Sintesis* | *UAS (30%)* |

---

## 3. RINCIAN OUTLINE SUBSTANSI TIAP BAB

### BAGIAN I — MESIN VON NEUMANN DAN REPRESENTASI DATA (`CPMK-1`)

#### BAB 1: Evolusi Komputasi, Arsitektur vs Organisasi, & Model Von Neumann vs Harvard (Pekan 1)
* **Sub-CPMK:** `Sub-CPMK-1.2` (C2/C3) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  1.1 Peran Pemahaman Arsitektur Sistem TI bagi *System Integrator* dan *Cloud Specialist*  
  1.2 Pembedaan Tegas: *Computer Architecture* (Kontrak ISA) vs *Computer Organization* (Implementasi Mikroarsitektur)  
  1.3 Evolusi Generasi Komputasi, Hukum Moore, Penskalakan Dennard, dan Era *Domain-Specific Hardware*  
  1.4 Konsep *Stored-Program* Arsitektur Von Neumann (CPU, Memori Utama, Modul I/O, Interkoneksi) dan *Von Neumann Bottleneck*  
  1.5 Perbandingan dengan Arsitektur Harvard dan *Modified Harvard Architecture* pada Prosesor Modern
* **Studi Kasus Teknis:** Membedah lembar spesifikasi teknis prosesor laptop vs prosesor ponsel pintar untuk memisahkan mana atribut arsitektur dan mana atribut organisasi.
* **Latihan Bab 1:** 8 soal analisis konseptual dan pemetaan diagram blok subsistem komputer.

#### BAB 2: Sistem Bilangan Biner/Heksadesimal, *Two's Complement*, & Kode Karakter (Pekan 2)
* **Sub-CPMK:** `Sub-CPMK-1.1` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  2.1 Sistem Bilangan Posisional (Desimal, Biner, Oktal, Heksadesimal) dan Konversi Cepat Kelompok Bit  
  2.2 Satuan Kapasitas Komputasi: Standar Desimal SI (`KB, MB, GB, TB`) vs Biner IEC (`KiB, MiB, GiB, TiB`)  
  2.3 Representasi Bilangan Bulat Tak Bertanda (*Unsigned*) vs Bertanda (*Sign-Magnitude*, *One's Complement*, & *Two's Complement*)  
  2.4 Penjumlahan/Pengurangan *Two's Complement* serta Aturan Deteksi *Arithmetic Overflow*  
  2.5 Representasi Teks & Simbol: Standar ASCII 7/8-bit, Unicode, dan Pengkodean Variabel UTF-8
* **Studi Kasus Teknis:** Bedah insiden klasik kegagalan perangkat lunak akibat *integer overflow* 16-bit/32-bit dan perbedaan pembacaan kapasitas disk 1 TB di sistem operasi (`931 GiB`).
* **Latihan Bab 2:** 12 soal konversi basis bilangan, operasi *Two's Complement*, dan dekode *hex dump* UTF-8.

#### BAB 3: Representasi *Floating Point* IEEE 754 & Penelusuran Siklus `Fetch-Decode-Execute` (Pekan 3)
* **Sub-CPMK:** `Sub-CPMK-1.1` & `Sub-CPMK-1.2` (C3) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  3.1 Keterbatasan *Fixed-Point* dan Konsep Normalisasi Saintifik Biner ($\pm 1,M \times 2^{E}$)  
  3.2 Anatomi Standar IEEE 754: *Single Precision* (`FP32`: 1–8–23 bit, *Bias* 127) dan *Double Precision* (`FP64`: 1–11–52 bit, *Bias* 1023)  
  3.3 Nilai Khusus IEEE 754 ($\pm 0$, *Denormalized*, $\pm\infty$, `NaN`), Galat Pembulatan Pecahan Biner, serta Format Presisi AI (`FP16` & `BF16`)  
  3.4 Register Internal Utama CPU Von Neumann: `PC`, `IR`, `MAR`, `MBR/MDR`, `ACC`, dan *General-Purpose Registers*  
  3.5 Penelusuran Langkah Mikro Siklus Eksekusi Instruksi (`Fetch` $\to$ `Decode` $\to$ `Operand Fetch` $\to$ `Execute` $\to$ `Write-Back`)
* **Eksplorasi Simulator:** Simulasi eksekusi program mesin 5 instruksi pada *Little Man Computer* (LMC) dan verifikasi pola bit di *IEEE-754 Visualizer*.
* **Latihan Bab 3 & Panduan Tugas 1:** 10 soal konversi IEEE 754 dan tabel jejak isi register + panduan pengerjaan **RTM-1 (Tugas 1)**.

---

### BAGIAN II — LOGIKA DIGITAL, SEKUENSIAL, DAN ORGANISASI ALU (`CPMK-2`)

#### BAB 4: Gerbang Logika Biner, Aljabar Boole Perangkat Keras, & Peta Karnaugh (Pekan 4)
* **Sub-CPMK:** `Sub-CPMK-2.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  4.1 Dari Sakelar Transistor CMOS ke Level Logika Digital `0` dan `1`  
  4.2 Tujuh Gerbang Logika Biner (`AND, OR, NOT, NAND, NOR, XOR, XNOR`): Simbol, Tabel Kebenaran, dan Fungsi  
  4.3 Sifat Universalitas Gerbang `NAND` dan `NOR` dalam Manufaktur Sirkuit Terpadu  
  4.4 Identitas Aljabar Boole untuk Penyederhanaan Sirkuit dan Teorema De Morgan  
  4.5 Bentuk Kanonik *Sum-of-Products* (SOP) dan Minimasi Gerbang Menggunakan Peta Karnaugh (K-Map 3 & 4 Variabel)
* **Guardrail Bab 4:** Fokus 100% pada penyederhanaan gerbang logika perangkat keras; logika kalimat proposisional umum, tabel implikasi/biimplikasi linguistik, logika predikat berkuantor ($\forall, \exists$), serta induksi matematika diserahkan penuh ke `STI-204 Matematika Diskrit dan Logika`.
* **Latihan Bab 4:** 10 soal analisis gerbang dan minimasi K-Map menjadi rangkaian `NAND` minimal.

#### BAB 5: Rangkaian Logika Kombinasional (*Adder, MUX, Decoder*) & Konstruksi ALU (Pekan 5)
* **Sub-CPMK:** `Sub-CPMK-2.1` (C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  5.1 Prinsip Rangkaian Kombinasional (Keluaran Murni Fungsi dari Masukan Saat Ini)  
  5.2 Rangkaian Aritmetika Biner: *Half Adder*, *Full Adder*, dan *4-bit Ripple-Carry Adder*  
  5.3 Rangkaian Penjumlah–Pengurang Terpadu (*Adder-Subtractor*) Berbasis *Two's Complement* & Gerbang Kontrol `XOR`  
  5.4 Rangkaian Pengarah Data: *Multiplexer* (MUX), *Demultiplexer*, *Decoder* Alamat Memori, dan *Encoder*  
  5.5 Merakit *Arithmetic Logic Unit* (ALU) Sederhana: Integrasi Unit Logika, Unit Aritmetika, Pemilih Operasi MUX, dan Pembangkitan *Status Flags* (`Z, N, C, V`)
* **Eksplorasi Simulator:** Menelusuri skema interaktif ALU 4-bit di *CircuitVerse*.
* **Latihan Bab 5:** 10 soal analisis rangkaian kombinasional dan penentuan keluaran + *flags* ALU.

#### BAB 6: Rangkaian Sekuensial: *Latch*, *Flip-Flop*, Register Perangkat Keras, & *Counter* (Pekan 6)
* **Sub-CPMK:** `Sub-CPMK-2.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  6.1 Mengapa Komputer Membutuhkan Umpan Balik? Perbedaan Rangkaian Kombinasional vs Sekuensial  
  6.2 Sinyal *Clock* Sistem, Siklus Waktu, Frekuensi (Hz/GHz), dan Pemicuan Tepi (*Edge-Triggered*)  
  6.3 Elemen Penyimpan 1-Bit: *SR Latch*, *Gated D Latch*, *D Flip-Flop*, dan *JK/T Flip-Flop*  
  6.4 Pembacaan Tabel Karakteristik dan Analisis Diagram Pewaktuan (*Timing Diagram*)  
  6.5 Merakit *Parallel Load Register* (dengan sinyal *Write Enable*), *Shift Register*, dan *Binary Counter*
* **Studi Kasus Teknis:** Bagaimana *Program Counter* (`PC`) dicacah naik otomatis setiap siklus dan bagaimana sel SRAM dibuat dari rangkaian penyimpan bistabil cepat.
* **Latihan Bab 6:** 10 soal *Timing Diagram* dan analisis perubahan status register 4-bit.

#### BAB 7: Integrasi *CPU Datapath* (Register + ALU + Kontrol) & Pengantar *Pipelining* (Pekan 7)
* **Sub-CPMK:** `Sub-CPMK-2.1` & `Sub-CPMK-2.2` (C4) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  7.1 Organisasi *Register File* (Port Baca Ganda & Port Tulis Tunggal)  
  7.2 Penelusuran *Single-Cycle Datapath*: Menghubungkan `PC`, Memori Instruksi, *Register File*, ALU, dan Unit Kontrol  
  7.3 Prinsip *Instruction Pipelining* 5-Tahap (`IF, ID, EX, MEM, WB`): Peningkatan *Throughput* Instruksi  
  7.4 Pengenalan Konseptual Kendala *Pipeline Hazards* (*Structural, Data,* dan *Control/Branch Hazard*)
* **Latihan Bab 7 & Unit Evaluasi E1:** 8 soal penelusuran jalur sinyal kontrol *datapath* & perhitungan *speedup pipeline* + **Paket Simulasi Lengkap UTS (`CPMK-2`)**.

---

### BAGIAN III — ARSITEKTUR PROSESOR, HIERARKI MEMORI, DAN AKSELERATOR AI (`CPMK-3`)

#### BAB 8: Arsitektur Set Instruksi: Komparasi Kritis CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`) (Pekan 9)
* **Sub-CPMK:** `Sub-CPMK-3.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  8.1 Peran *Instruction Set Architecture* (ISA) sebagai Batas Antara Perangkat Lunak/Kompilator dengan Perangkat Keras  
  8.2 Karakteristik Filosofi CISC (`Intel/AMD x86_64`): Instruksi Kompleks Panjang Variabel, Mode Pengalamatan Kaya, & Kompatibilitas Historis  
  8.3 Karakteristik Filosofi RISC (`ARM64` & Standar Terbuka `RISC-V`): Instruksi Panjang Tetap, *Load-Store Architecture*, Register Banyak, & Efisiensi Dekoder  
  8.4 Konvergensi Mikroarsitektur Modern: Penerjemahan Instruksi `x86` ke *Micro-ops* Internal  
  8.5 Analisis Pergeseran Industri: Dominasi `ARM64` di Mobile/Laptop Hemat Daya & Ekspansi `AWS Graviton`/`Ampere`/`RISC-V` di *Cloud Data Center*
* **Studi Kasus Teknis:** Membandingkan rasio performa-per-watt dan biaya sewa bulanan antara *cloud instance* berbasis `x86_64` vs `ARM64` untuk layanan *microservice* web.
* **Latihan Bab 8:** 8 soal analisis komparatif CISC vs RISC pada berbagai skenario bisnis.

#### BAB 9: Hierarki Memori (SRAM vs DRAM), Lokalitas, & Kinerja *Cache* `L1/L2/L3` (Pekan 10)
* **Sub-CPMK:** `Sub-CPMK-3.2` (C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  9.1 Masalah *Memory Wall* dan Piramida *Trade-Off* Kapasitas–Kecepatan–Biaya per Bit  
  9.2 Teknologi Memori Semikonduktor: SRAM vs DRAM (`DDR4/DDR5`), Memori *ECC* Server, dan *High Bandwidth Memory* (`HBM`)  
  9.3 Prinsip Lokalitas Referensi (*Temporal Locality* & *Spatial Locality*) dalam Eksekusi Program  
  9.4 Organisasi Multi-Level *Cache* (`L1i/L1d` Privat, `L2`, dan `L3` *Shared*), *Cache Line*, serta Metode Pemetaan (*Direct, Fully Associative, k-Way Set-Associative*)  
  9.5 Kebijakan Penggantian (*LRU*) & Penulisan (*Write-Through* vs *Write-Back*), serta Perhitungan *Effective Access Time* (EAT)
* **Studi Kasus Teknis:** Menghitung lonjakan waktu eksekusi kueri *in-memory* ketika ukuran struktur data melampaui kapasitas `L3 Cache` sehingga sering memicu *cache miss* ke DRAM.
* **Latihan Bab 9:** 10 soal perhitungan EAT bertingkat dan analisis skema pemetaan *cache*.

#### BAB 10: Penyimpanan Sekunder Modern (NVMe SSD, HDD, RAID) & Peran Hardware MMU/TLB (Pekan 11)
* **Sub-CPMK:** `Sub-CPMK-3.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  10.1 Karakteristik Penyimpanan Sekunder: HDD Mekanis (Latensi *Seek/Rotational*) vs *NAND Flash* SSD (`SLC/TLC/QLC`)  
  10.2 Antarmuka Penyimpanan: Mengapa Protokol NVMe di Atas Jalur PCIe Jauh Melampaui SATA/AHCI Klasik (IOPS & Antrean Paralel)  
  10.3 Arsitektur Redundansi & Kinerja Penyimpanan: Analisis `RAID 0, RAID 1, RAID 5, RAID 6,` dan `RAID 10`  
  10.4 Dukungan Perangkat Keras untuk Memori Virtual: Peran *Memory Management Unit* (MMU) dan *Translation Lookaside Buffer* (TLB) di Dalam Prosesor
* **Guardrail Bab 10:** Pembahasan memori virtual dibatasi pada komponen perangkat keras penerjemah alamat (MMU & TLB); struktur tabel halaman OS, *thrashing*, dan algoritma *page replacement* (`FIFO/LRU/Clock`) diserahkan ke `STI-310 Sistem Operasi`.
* **Latihan Bab 10:** 10 soal perhitungan kapasitas efektif/toleransi gagal disk RAID dan analisis latensi NVMe vs HDD.

#### BAB 11: Komputasi Paralel & Akselerator Domain-Spesifik: CPU vs GPU vs NPU/TPU (Pekan 12)
* **Sub-CPMK:** `Sub-CPMK-3.1` & `Sub-CPMK-3.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  11.1 Batas Termal (*Power Wall*), Hukum Amdahl Pengantar, dan Taksonomi Paralelisme Flynn (`SISD, SIMD, MISD, MIMD`)  
  11.2 Prosesor *Multicore*, *Simultaneous Multithreading* (SMT/*Hyper-Threading*), dan Unit Vektor SIMD (`AVX / NEON`)  
  11.3 Anatomi Arsitektural CPU (*Latency-Optimized*) vs GPU (*Throughput-Optimized SIMT & Tensor Cores*)  
  11.4 Kebangkitan *Neural Processing Unit* (NPU) pada Perangkat *Edge/AI PC* dan *Tensor Processing Unit* (TPU) di *Data Center*  
  11.5 Matriks Keputusan Pemilihan Komputasi (CPU vs GPU vs NPU) Berdasarkan Profil Beban Kerja Organisasi
* **Latihan Bab 11 & Panduan Tugas 2:** 8 soal komparasi beban kerja paralel & perhitungan Hukum Amdahl sederhana + panduan finalisasi **RTM-2 (Tugas 2)**.

---

### BAGIAN IV — INTERKONEKSI BUS/I-O, VIRTUALISASI, DAN SERVER DATA CENTER (`CPMK-4`)

#### BAB 12: Sistem Interkoneksi Bus (PCIe), *Interrupt-Driven I/O*, & *Direct Memory Access* (DMA) (Pekan 13)
* **Sub-CPMK:** `Sub-CPMK-4.1` (C5) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  12.1 Struktur Interkoneksi Sistem: Jalur Data, Alamat, dan Kontrol serta Pergeseran dari Bus Paralel ke *Point-to-Point Serial*  
  12.2 Arsitektur *PCI Express* (PCIe `Gen 3/4/5/6`): Konfigurasi *Lanes* (`x1, x4, x8, x16`), Perhitungan *Bandwidth* Dua Arah, & Topologi Jalur CPU–Chipset  
  12.3 Struktur Modul/Kontroler I/O dan Kelemahan Teknik *Programmed I/O* (*Polling*)  
  12.4 Mekanisme *Interrupt-Driven I/O*: Alur Sinyal Permintaan Interupsi (`INTR`), Vektor Interupsi, dan Pelestarian Konteks Register  
  12.5 Evaluasi Arsitektur *Direct Memory Access* (DMA) & *RDMA* Konseptual untuk Transfer Data Berkecepatan Tinggi Tanpa Membebani CPU
* **Studi Kasus Teknis:** Mengevaluasi topologi jalur PCIe sebuah server AI multi-GPU dan menghitung efisiensi pembebasan siklus CPU oleh pengontrol DMA.
* **Latihan Bab 12:** 10 soal perhitungan *bandwidth* PCIe dan evaluasi perbandingan 3 teknik I/O.

#### BAB 13: Abstraksi Virtualisasi Perangkat Keras (`VT-x/AMD-V`) & Evaluasi *Hypervisor* (Pekan 14)
* **Sub-CPMK:** `Sub-CPMK-4.2` (C5) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  13.1 Dari Server Fisik Tunggal ke Abstraksi Sumber Daya Virtual: Motivasi Efisiensi, Isolasi, dan Ketersediaan  
  13.2 Tantangan Instruksi *Privileged* (`Ring 0`) dan Peran Ekstensi Silikon `Intel VT-x / AMD-V / ARM-VE`  
  13.3 Akselerasi Hardware Memori & I/O pada Virtualisasi: *Extended Page Tables* (`EPT/SLAT`) dan `IOMMU / SR-IOV` (*GPU/NIC Passthrough*)  
  13.4 Evaluasi Komparatif *Hypervisor* Tipe 1 (*Bare-Metal*: KVM, VMware ESXi, Xen, Hyper-V) vs Tipe 2 (*Hosted*)  
  13.5 Perbedaan Batas Abstraksi Perangkat Keras antara *Virtual Machine* vs *OS-Level Container* serta Evaluasi Kapasitas Konsolidasi Server
* **Guardrail Bab 13:** Fokus pada bagaimana perangkat keras dan *Hypervisor* mengabstraksikan CPU/RAM/I-O; praktik administrasi sistem operasi kontainer, Docker, dan orkestrasi Kubernetes dibahas pada `STI-520 Infrastruktur dan Komputasi Awan`.
* **Latihan Bab 13:** 8 soal evaluasi arsitektur *Hypervisor* dan perencanaan kapasitas konsolidasi VM (*vCPU/RAM sizing*).

#### BAB 14: Organisasi Infrastruktur *Server Data Center* Modern untuk Komputasi Awan (Pekan 15)
* **Sub-CPMK:** `Sub-CPMK-4.2` (C5) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  14.1 Anatomi Perangkat Keras Kelas Server vs PC Konsumen: *Dual-Socket CPU*, *ECC RAM*, *Hot-Swap Drive Bays*, *Redundant PSU*, & *Out-of-Band Management* (`IPMI/BMC`)  
  14.2 Evaluasi Faktor Bentuk (*Form Factor*): *Tower Server* vs *Rackmount Server* (`1U, 2U, 4U`) vs *Blade/Modular Server*  
  14.3 Pengantar Arsitektur Penyimpanan Pusat Data: *Direct-Attached Storage* (`DAS`), *Network-Attached Storage* (`NAS`), dan *Storage Area Network* (`SAN`)  
  14.4 Infrastruktur Pendukung Fisik: Redundansi Daya ($N+1, 2N$ UPS/Genset), Manajemen Termal *Hot/Cold Aisle*, & Perhitungan *Power Usage Effectiveness* (`PUE`)  
  14.5 Evaluasi Klasifikasi Ketersediaan *Data Center* (*Uptime Tier I s.d. Tier IV*) dan Bagaimana Seluruh Komponen Fisik Menopang Layanan *Cloud IaaS/PaaS/SaaS*
* **Guardrail Bab 14:** Tidak membahas protokol *routing* BGP/OSPF atau desain *VLAN/subnetting* jaringan *data center* (ranah `STI-312 Jaringan Komputer dan Komunikasi Data`).
* **Latihan Bab 14 & Unit Evaluasi E2:** 10 soal evaluasi spesifikasi rak server, perhitungan PUE/*downtime Tier*, + **Paket Studi Kasus Lengkap Persiapan UAS (`CPMK-4` & Sintesis)**.
