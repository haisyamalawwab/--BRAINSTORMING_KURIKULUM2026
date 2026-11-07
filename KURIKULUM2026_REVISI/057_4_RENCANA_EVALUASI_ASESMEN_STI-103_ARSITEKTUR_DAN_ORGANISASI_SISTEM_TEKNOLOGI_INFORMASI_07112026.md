# 057_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI (*Information Technology Systems Architecture and Organization*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 1 — Tahap Fondasi)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI103`  
**Klaster Asesmen MK (Dok 018):** Klaster 1 (`K-1`) — Sains Dasar, Teori Formal, & Fondasi Arsitektur Komputasi  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** Panduan KPT 2024 Dikti (Tabel 16–21, Tabel 26, & Lampiran RTM) · Dok 004 · Dok 007 §5 · Dok 008 (Formula Multi-CPL Attainment & Skema 4x Evaluasi) · Dok 018 · Dok 041 Lampiran 23 · `057_1_RPS_STI-103_...md`.

---

## 1. ARSITEKTUR PENILAIAN MULTI-CPL & KEPATUHAN IKU 7

Mata kuliah `STI-103` (3 SKS Teori) memiliki karakteristik unik di Semester 1 karena menjembatani **fondasi logika biner/representasi data (`CPL-05` / `P1`)**, **prinsip arsitektur komputer & infrastruktur cloud (`CPL-07` / `P3`)**, serta **penalaran analitis-kritis sistematis (`CPL-02` / `KU1`)**, seluruhnya pada level penguasaan **Introduce (`I`)**:
* **Pemetaan 1-ke-1 Instrumen ke CPMK:** Keempat `CPMK` (`CPMK-1` [C3], `CPMK-2` [C4], `CPMK-3` [C4], `CPMK-4` [C5]) terpetakan tepat 1-ke-1 ke 4 titik evaluasi baku (`Tugas 1 = 20%`, `UTS = 30%`, `Tugas 2 = 20%`, `UAS = 30%`).
* **Verifikasi Kepatuhan IKU 7 (*Case Method / Problem-Based* $\ge 50\%$):** Komponen berbasis pemecahan masalah & evaluasi studi kasus meliputi **Tugas 1 (20% — *Problem-Based Bit/Register Tracing*), Tugas 2 (20% — *Case-Method Architecture Benchmarking*), dan UAS (30% — *Case-Based Server & Cloud Infrastructure Evaluation*) = 70%**, melampaui batas minimal IKU 7 (**50%**).

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP MULTI-CPL, CPMK, & SUB-CPMK (STANDAR KPT 2024 TABEL 26)

| Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Instrumen Penilaian | `CPL-05` (`P1`) | `CPL-07` (`P3`) | `CPL-02` (`KU1`) | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|
| **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | **RTM-1 (Tugas 1)** Bagian A & B: Konversi Biner/Hex, *Two's Complement*, & IEEE 754 | 7% | 3% | 0% | 10% | **20%** |
| | `Sub-CPMK-1.2` | Mg 4 | **RTM-1 (Tugas 1)** Bagian C: Penelusuran Register Siklus `Fetch-Decode-Execute` Von Neumann | 3% | 7% | 0% | 10% | |
| **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.1` | Mg 8 | **Naskah Soal UTS** (Soal 1, 2, & separuh 4): Minimasi Gerbang K-Map, Rangkaian Kombinasional, & ALU | 10% | 0% | 8% | 18% | **30%** |
| | `Sub-CPMK-2.2` | Mg 8 | **Naskah Soal UTS** (Soal 3 & separuh 4): Analisis *Flip-Flop*, *Timing Diagram*, Register, & *Datapath* | 5% | 0% | 7% | 12% | |
| **`CPMK-3`**<br>(C4) | `Sub-CPMK-3.1` | Mg 12 | **RTM-2 (Tugas 2)** Bagian A & C: Studi Kasus Komparasi CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`) | 0% | 5% | 4% | 9% | **20%** |
| | `Sub-CPMK-3.2` | Mg 12 | **RTM-2 (Tugas 2)** Bagian B & C: Analisis *Cache* `L1/L2/L3` (EAT), NVMe RAID, & Akselerator GPU/NPU | 0% | 7% | 4% | 11% | |
| **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1` | Mg 16 | **Naskah Soal UAS** (Kasus 1 & separuh 4): Evaluasi Jalur Bus PCIe, *Interrupt-Driven I/O*, & DMA | 0% | 6% | 4% | 10% | **30%** |
| | `Sub-CPMK-4.2` | Mg 16 | **Naskah Soal UAS** (Kasus 2, 3, & separuh 4): Evaluasi *Hypervisor* Tipe 1/2 & Audit *Server Data Center* Cloud | 0% | 12% | 8% | 20% | |
| **TOTAL** | **8 Sub-CPMK** | **16 Pekan** | **4 Paket Instrumen Sumatif (+ Aktivitas Formatif Mingguan 0%)** | **25%** | **40%** | **35%** | **100%** | **100%** |

---

## 3. KISI-KISI INSTRUMEN EVALUASI (*ASSESSMENT BLUEPRINT*)

| Titik Evaluasi | Pekan | Durasi / Format | Sub-CPMK Diuji | Level Bloom | Rincian Butir / Komponen Penilaian | Bobot Internal | Bobot MK |
|---|:---:|---|---|:---:|---|:---:|:---:|
| **1. Tugas 1** | Mg 4 | Penugasan Mandiri Terstruktur (1 pekan) + Verifikasi Kelas 10' | `Sub-CPMK-1.1`<br>`Sub-CPMK-1.2` | C3 | • Bagian A: Konversi Biner/Hex, operasi *Two's Complement* 8-bit, & deteksi *overflow*<br>• Bagian B: Pengkodean/dekode IEEE 754 32-bit & analisis galat pecahan biner<br>• Bagian C: Tabel penelusuran perubahan nilai `PC, MAR, MBR, IR, ACC` untuk 4 instruksi mesin | 30%<br>35%<br>35% | **20%** |
| **2. UTS** | Mg 8 | Ujian Tertulis Luring Terjadwal (*Closed-Book*, 150 menit) | `Sub-CPMK-2.1`<br>`Sub-CPMK-2.2` | C4 | • Soal 1: Penyusunan tabel kebenaran & penyederhanaan gerbang biner dengan K-Map 4 variabel<br>• Soal 2: Analisis skema *Full Adder* + MUX pada ALU 4-bit & penentuan *flags* (`Z, N, C, V`)<br>• Soal 3: Analisis *Timing Diagram* keluaran $Q$ pada *D/JK Flip-Flop* & *Register*<br>• Soal 4: Penelusuran aliran data antara *Register File* sekuensial & ALU pada *datapath* CPU | 25%<br>30%<br>25%<br>20% | **30%** |
| **3. Tugas 2** | Mg 12 | Laporan Studi Kasus *Benchmarking* Arsitektur (6–8 hal. A4, waktu kerja 2 pekan) | `Sub-CPMK-3.1`<br>`Sub-CPMK-3.2` | C4 | • Bagian A: Komparasi kritis spesifikasi CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`) untuk 3 profil beban<br>• Bagian B: Perhitungan *Effective Access Time* (EAT) *Cache* `L1/L2/L3` & pemilihan skema NVMe RAID<br>• Bagian C: Justifikasi pemilihan CPU vs GPU vs NPU pada beban kerja transaksi vs AI<br>• Bagian D: Kualitas sitasi *datasheet* resmi & keruntutan tata tulis teknis | 30%<br>35%<br>25%<br>10% | **20%** |
| **4. UAS** | Mg 16 | Ujian Tertulis Evaluasi Studi Kasus Luring (*Closed-Book*, 150 menit) | `Sub-CPMK-4.1`<br>`Sub-CPMK-4.2`<br>*(+ Sintesis)* | C5 | • Kasus 1: Evaluasi kemacetan *bandwidth* bus PCIe & efisiensi *Interrupt-Driven I/O* + DMA<br>• Kasus 2: Evaluasi konsolidasi server fisik ke *Hypervisor* Tipe 1 (`VT-x/EPT/IOMMU`) & *sizing* VM<br>• Kasus 3: Audit kritis kelemahan *Single Point of Failure*, PUE, & *Tier* pada proposal *server data center*<br>• Kasus 4: Sintesis lintas-lapisan arsitektur (IEEE 754/`FP16` $\to$ *Cache* $\to$ GPU $\to$ PCIe/DMA $\to$ Cloud VM) | 25%<br>25%<br>30%<br>20% | **30%** |

---

## 4. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN (STANDAR KPT 2024 LAMPIRAN 23)

### 4.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Kode / SKS** | Arsitektur dan Organisasi Sistem Teknologi Informasi / `STI-103` / 3 SKS Teori |
| **Minggu Rilis & Batas Kumpul** | Dirilis: **Pekan 3** · Batas Pengumpulan: **Pekan 4** (melalui LMS Edlink + cek verifikasi 10 menit di kelas) |
| **Bobot Penilaian** | **20%** dari Nilai Akhir Mata Kuliah |
| **CPMK & Sub-CPMK Tujuan** | **`CPMK-1`** (`Sub-CPMK-1.1` & `Sub-CPMK-1.2`): Menerapkan representasi data biner, heksadesimal, *floating point* IEEE 754, dan siklus eksekusi instruksi Von Neumann secara tepat dan akurat. |
| **1. Tujuan Tugas** | Membentuk ketelitian mahasiswa dalam memetakan bagaimana angka bulat, angka pecahan *floating point*, dan instruksi program disimpan serta dieksekusi langkah demi langkah di dalam register prosesor. |
| **2. Objek Garapan** | Satu lembar kerja terstruktur (*Structured Tracing Worksheet*) yang memiliki parameter angka unik berbasis 3 digit terakhir NIM masing-masing mahasiswa (mencegah salin-tempel antar-mahasiswa). |
| **3. Batasan yang Harus Dikerjakan** | 1. **Bagian A:** Mengonversi bilangan berparameter NIM ke biner/heksadesimal, melakukan 3 operasi pengurangan 8-bit menggunakan *Two's Complement*, dan membuktikan secara matematis terjadi atau tidaknya *overflow*.<br>2. **Bagian B:** Mengonversi 2 bilangan riil bertanda ke format biner & heksadesimal 8-digit **IEEE 754 Single Precision (32-bit)** dengan menuliskan pemisahan bit *Sign*, *Biased Exponent*, dan *Mantissa*, serta menjelaskan mengapa pecahan desimal tertentu mengalami pembulatan di biner.<br>3. **Bagian C:** Diberikan peta awal alamat memori dan program 4 instruksi (`LOAD, SUB, ADD, STORE`), mahasiswa wajib melengkapi tabel isi heksadesimal register `PC, MAR, MBR, IR,` dan `ACC` pada setiap sub-siklus `Fetch`, `Decode`, dan `Execute`. |
| **4. Metode / Cara Pengerjaan** | Dikerjakan **secara individu**; seluruh langkah pembagian/perkalian basis dan normalisasi eksponen wajib dituliskan lengkap (simulator web hanya boleh dipakai untuk mengecek ulang kebenaran hasil akhir). |
| **5. Deskripsi Luaran Tugas** | Berkas `.pdf` bernama `STI103_T1_[NIM]_[Nama].pdf` (4–6 halaman A4) beserta deklarasi kejujuran akademik. |
| **6. Kriteria & Bobot Penilaian** | Dinilai dengan **Rubrik Analitik Tugas 1 (`057_5`)**: (1) Akurasi konversi biner/hex & *Two's Complement* (30%); (2) Ketepatan konversi IEEE 754 & analisis presisi (35%); (3) Ketepatan penelusuran tabel register siklus Von Neumann (35%). |

---

### 4.2 Spesifikasi Instrumen Ujian Tengah Semester (UTS — Pekan 8)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Bentuk & Durasi Ujian** | Ujian Tertulis Luring Terjadwal (*Closed-Book*), durasi **150 menit**. |
| **Bobot & Target Capaian** | **30%** dari Nilai Akhir · Mengukur **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]). |
| **Rincian 4 Butir Soal** | 1. **(25% — `Sub-CPMK-2.1`)** Dari narasi spesifikasi sistem pengaman perangkat keras 4 sensor input, susun tabel kebenaran, sederhanakan ekspresi SOP menggunakan **Peta Karnaugh 4 variabel**, dan gambarkan skema gerbang logika minimalnya.<br>2. **(30% — `Sub-CPMK-2.1`)** Diberikan skema blok **ALU 4-bit** yang memuat *Full Adder-Subtractor*, gerbang `AND`/`OR`, dan *4-to-1 Multiplexer*: tentukan keluaran 4-bit dan nilai ke-4 bendera status (`Zero, Negative, Carry, Overflow`) untuk 3 pasang input dan sinyal kontrol yang berbeda.<br>3. **(25% — `Sub-CPMK-2.2`)** Diberikan rangkaian *positive-edge-triggered D Flip-Flop* dan *4-bit Shift/Parallel Register* beserta gelombang sinyal `Clock`, `Reset`, `Enable`, dan `D`: gambarkan secara presisi diagram pewaktuan (*Timing Diagram*) sinyal keluaran $Q$ dan status isi register tiap detak *clock*.<br>4. **(20% — `Sub-CPMK-2.1 & 2.2`)** Jelaskan dan telusuri pada diagram *CPU Datapath* bagaimana komponen sekuensial (*Register File* & `PC`) bekerja sama dengan komponen kombinasional (ALU & MUX) dalam mengeksekusi instruksi penjumlahan dua register. |

---

### 4.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Kode / SKS** | Arsitektur dan Organisasi Sistem Teknologi Informasi / `STI-103` / 3 SKS Teori |
| **Minggu Rilis & Batas Kumpul** | Dirilis: **Pekan 10** · Batas Pengumpulan: **Pekan 12** (melalui LMS Edlink dalam format `.pdf`) |
| **Bobot Penilaian** | **20%** dari Nilai Akhir Mata Kuliah |
| **CPMK & Sub-CPMK Tujuan** | **`CPMK-3`** (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C4]): Membandingkan secara kritis karakteristik arsitektur prosesor CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`), hierarki memori *cache* `L1/L2/L3`, dan akselerator GPU/NPU dalam skenario beban kerja nyata. |
| **1. Tujuan Tugas** | Melatih ketajaman mahasiswa membaca lembar spesifikasi perangkat keras resmi (*real processor/accelerator datasheets*) dan membandingkannya secara objektif berdasarkan tuntutan beban kerja sistem informasi dan AI nyata. |
| **2. Objek Garapan** | Tiga skenario beban kerja organisasi: **(Skenario 1)** Server Basis Data OLTP Rumah Sakit 24/7; **(Skenario 2)** Perangkat *Edge/Mobile Terminal* Hemat Daya untuk Petugas Gudang Cerdas; **(Skenario 3)** *Workstation/Server* Pelatihan & Inferensi Model Visi Komputer AI. |
| **3. Batasan yang Harus Dikerjakan** | 1. Memilih dan membandingkan spesifikasi nyata minimal 1 prosesor keluarga **CISC (`x86_64`)** dan 1 prosesor keluarga **RISC (`ARM64` atau `RISC-V`)** yang relevan menggunakan data resmi pabrikan (*core count, TDP/wattage, ISA features, L1/L2/L3 cache size*).<br>2. Melakukan perhitungan kuantitatif simulasi **Effective Access Time (EAT)** sistem memori bertingkat (`L1 → L2 → L3 → DDR5`) serta merekomendasikan konfigurasi penyimpanan **NVMe SSD + RAID** yang tepat untuk Skenario 1.<br>3. Menganalisis secara kritis mengapa Skenario 3 membutuhkan akselerator **GPU (`Tensor Cores` + memori `VRAM/HBM`)** sedangkan inferensi ringan pada Skenario 2 lebih optimal dijalankan pada **NPU** terintegrasi.<br>4. **Batasan Guardrail:** Fokus pada evaluasi arsitektur perangkat keras; tidak menyusun konfigurasi jaringan router atau skrip instalasi OS. |
| **4. Metode / Cara Pengerjaan** | Dikerjakan secara **individu atau berpasangan (maks. 2 orang)** dengan merujuk minimal 3 *technical datasheet / whitepaper* resmi pabrikan (Intel/AMD/ARM/NVIDIA/RISC-V International) dan buku teks utama, panjang 6–8 halaman A4. |
| **5. Deskripsi Luaran Tugas** | Laporan teknis `STI103_T2_[NIM].pdf` memuat matriks perbandingan spesifikasi, perhitungan EAT & kapasitas RAID, argumen rekomendasi per skenario, daftar rujukan teknis, dan *AI Transparency Declaration*. |
| **6. Kriteria & Bobot Penilaian** | Dinilai dengan **Rubrik Analitik Tugas 2 (`057_5`)**: (1) Ketajaman komparasi CISC vs RISC (30%); (2) Akurasi analisis *Cache* EAT & penyimpanan NVMe/RAID (35%); (3) Ketepatan analisis peran akselerator CPU vs GPU vs NPU (25%); (4) Kualitas sitasi *datasheet* & tata tulis (10%). |

---

### 4.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Bentuk & Durasi Ujian** | Ujian Tertulis Evaluasi Studi Kasus Luring Terjadwal (*Closed-Book*), durasi **150 menit**. |
| **Bobot & Target Capaian** | **30%** dari Nilai Akhir · Mengukur **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) dan sintesis arsitektur sistem TI. |
| **Rincian 4 Studi Kasus Soal** | 1. **(25% — `Sub-CPMK-4.1`)** Diberikan diagram jalur interkoneksi server yang menghubungkan CPU, RAM, 4 keping NVMe SSD, NIC 25GbE, dan 2 kartu GPU melalui jalur PCIe: evaluasi letak *bandwidth bottleneck*, hitung kapasitas laju transfer maksimum jalur tersebut, dan bandingkan beban siklus CPU antara mekanisme *Programmed I/O*, *Interrupt-Driven I/O*, dan *DMA*.<br>2. **(25% — `Sub-CPMK-4.2`)** Sebuah perusahaan ingin mengonsolidasikan 8 server aplikasi fisik lama (utilisasi rata-rata 10%) menjadi mesin virtual: evaluasi mengapa **Hypervisor Tipe 1 (*Bare-Metal*)** dengan dukungan ekstensi `VT-x/AMD-V`, `EPT`, dan `IOMMU` harus dipilih dibandingkan Tipe 2, lalu hitung kebutuhan *host* fisik (dengan toleransi *failover* $N+1$) agar tidak terjebak *memory overcommitment*.<br>3. **(30% — `Sub-CPMK-4.2`)** Diberikan draf proposal pengadaan ruang server *on-premise / private cloud* sebuah institusi yang mengandung sejumlah kelemahan desain (memori non-ECC, disk tunggal tanpa RAID, PSU tunggal, nilai PUE $2,4$, klaim setara *Tier III* yang tidak valid): lakukan evaluasi audit kritis dan susun rekomendasi revisi spesifikasi server *data center* yang memenuhi keandalan *cloud* modern.<br>4. **(20% — Sintesis `CPMK-1..4`)** Uraikan secara runtut perjalanan eksekusi sebuah permintaan layanan inferensi AI di *cloud* mulai dari tingkat virtualisasi VM/*passthrough*, transfer data DMA lewat bus PCIe, pemuatan blok memori ke *cache*/VRAM, hingga pengolahan matriks format *floating point* (`FP16`/IEEE 754) di dalam unit komputasi. |

---

## 5. FORMULA PERHITUNGAN NILAI, MULTI-CPL ATTAINMENT, & KONVERSI MUTU

### 5.1 Rumus Nilai per CPMK dan Nilai Akhir Mata Kuliah ($NA_{\text{STI-103}}$)

Sesuai pemetaan 1-ke-1 **Dokumen 008 §3**:
$$\text{Score}_{\text{CPMK-1}} = S_{\text{Tugas 1}}, \quad \text{Score}_{\text{CPMK-2}} = S_{\text{UTS}}, \quad \text{Score}_{\text{CPMK-3}} = S_{\text{Tugas 2}}, \quad \text{Score}_{\text{CPMK-4}} = S_{\text{UAS}}$$

Nilai Akhir Mata Kuliah ($0\text{–}100$):
$$NA_{\text{STI-103}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 5.2 Formula Skor Ketercapaian Masing-Masing dari 3 CPL pada `STI-103`

Mengacu matriks proporsi bobot pada Bagian 2 (`CPL-05` = 25%, `CPL-07` = 40%, `CPL-02` = 35%), buku nilai OBE SIAKAD menghitung skor spesifik per CPL untuk mahasiswa $i$ secara presisi sebagai rata-rata tertimbang dari CPMK pendukungnya:

1. **Skor Ketercapaian `CPL-05` (`P1` — Bobot Kredit $3 \times 0,25 = 0,75\text{ SKS}$):** Didukung oleh `CPMK-1` (10%) dan `CPMK-2` (15%):
   $$\text{Score}_{\text{CPL-05}}(i) = \frac{10 \times S_{\text{Tugas 1}}(i) + 15 \times S_{\text{UTS}}(i)}{25} = 0,40\,S_{\text{Tugas 1}}(i) + 0,60\,S_{\text{UTS}}(i)$$

2. **Skor Ketercapaian `CPL-07` (`P3` — Bobot Kredit $3 \times 0,40 = 1,20\text{ SKS}$):** Didukung oleh `CPMK-1` (10%), `CPMK-3` (12%), dan `CPMK-4` (18%):
   $$\text{Score}_{\text{CPL-07}}(i) = \frac{10 \times S_{\text{Tugas 1}}(i) + 12 \times S_{\text{Tugas 2}}(i) + 18 \times S_{\text{UAS}}(i)}{40} = 0,25\,S_{\text{Tugas 1}}(i) + 0,30\,S_{\text{Tugas 2}}(i) + 0,45\,S_{\text{UAS}}(i)$$

3. **Skor Ketercapaian `CPL-02` (`KU1` — Bobot Kredit $3 \times 0,35 = 1,05\text{ SKS}$):** Didukung oleh `CPMK-2` (15%), `CPMK-3` (8%), dan `CPMK-4` (12%):
   $$\text{Score}_{\text{CPL-02}}(i) = \frac{15 \times S_{\text{UTS}}(i) + 8 \times S_{\text{Tugas 2}}(i) + 12 \times S_{\text{UAS}}(i)}{35}$$

*(Verifikasi Konsistensi Aljabar: $0,25\,\text{Score}_{\text{CPL-05}} + 0,40\,\text{Score}_{\text{CPL-07}} + 0,35\,\text{Score}_{\text{CPL-02}} \equiv 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}} = NA_{\text{STI-103}}$ — tepat 100% konsisten tanpa selisih pembulatan!)*

### 5.3 Contoh Simulasi Buku Nilai Multi-CPL `STI-103`

| Mahasiswa | T1 (20%)<br>`CPMK-1` | UTS (30%)<br>`CPMK-2` | T2 (20%)<br>`CPMK-3` | UAS (30%)<br>`CPMK-4` | Skor `CPL-05` (`P1`) | Skor `CPL-07` (`P3`) | Skor `CPL-02` (`KU1`) | Nilai Akhir `NA` | Status OBE ($\ge 65$) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mhs-01 | 85 | 80 | 84 | 82 | 82,00 | 83,35 | 81,60 | **82,40 (A)** | ✅ Semua CPL Tercapai |
| Mhs-02 | 76 | 70 | 72 | 74 | 72,40 | 73,90 | 71,83 | **72,80 (B)** | ✅ Semua CPL Tercapai |
| Mhs-03 | 72 | 58 | 70 | 68 | *63,60* | 69,60 | *64,17* | **65,80 (C+)** | ⚠️ Remedial `CPMK-2` (agar `P1` & `KU1` $\ge 65$) |

### 5.4 Tabel Konversi Huruf Mutu & Ambang Ketuntasan OBE

| Rentang Skor ($0\text{–}100$) | Huruf Mutu | Angka Mutu | Status Kelulusan MK | Status Ketercapaian CPL/CPMK OBE ($\ge 65,0$) |
|:---:|:---:|:---:|:---:|:---:|
| $81,00 \text{ – } 100,00$ | **A** | 4,00 | Lulus | **Tercapai (Exemplary)** |
| $76,00 \text{ – } 80,99$ | **B+** | 3,50 | Lulus | **Tercapai (Proficient)** |
| $70,00 \text{ – } 75,99$ | **B** | 3,00 | Lulus | **Tercapai (Satisfactory)** |
| $65,00 \text{ – } 69,99$ | **C+** | 2,50 | Lulus | **Tercapai Minimum Ambang OBE ($\ge 65,0$)** |
| $56,00 \text{ – } 64,99$ | **C** | 2,00 | Lulus Administratif | *Belum Mencapai Target OBE (< 65,0 — Remedial CPMK Terkait)* |
| $45,00 \text{ – } 55,99$ | **D** | 1,00 | Tidak Lulus | **Tidak Tercapai** |
| $0,00 \text{ – } 44,99$ | **E** | 0,00 | Tidak Lulus | **Tidak Tercapai** |

---

## 6. PROTOKOL REMEDIAL, INTEGRITAS PARAMETER UNIK & AI, SERTA SIKLUS PPEPP

1. **Parameterisasi NIM & Anti-Fabrikasi Spesifikasi:** Tugas 1 menggunakan parameter angka berbasis 3 digit akhir NIM agar setiap mahasiswa melakukan perhitungan biner/IEEE 754 sendiri; sedangkan pada Tugas 2, setiap klaim jumlah *core*, ukuran *cache*, atau TDP prosesor **wajib menyertakan tautan/kutipan *datasheet* resmi** (mencegah halusinasi angka spesifikasi dari LLM).
2. **Remedial Terarah per CPMK:** Seperti tampak pada simulasi `Mhs-03` di atas, meskipun Nilai Akhir mata kuliah mencapai `65,80`, nilai `CPMK-2` (`58`) menarik skor `CPL-05` dan `CPL-02` ke bawah ambang `65,0`. Sistem OBE memfasilitasi 1 kali remedial khusus pada `CPMK-2` (batas skor maksimal remedial **70,0**) sehingga ke-3 CPL tuntas merata.
3. **Evaluasi PPEPP & Serah Terima Lintas-Semester:** Rekapitulasi ketercapaian `CPMK-1..4` dilaporkan ke KBK Infrastruktur, Sistem & Komputasi Awan untuk menjadi data awal bagi pengampu `STI-204 Matematika Diskrit dan Logika` (Sem 2), `STI-310 Sistem Operasi` (Sem 3), dan `STI-520 Infrastruktur dan Komputasi Awan` (Sem 5).
