# 057_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI (*Information Technology Systems Architecture and Organization*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 1 — Tahap Fondasi)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI103`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `057_1_RPS_STI-103_...md` · Dok 032 (Modalitas Pembelajaran SCL KPT 2024) · Dok 043 (Boundary Guardrails).

---

## BAGIAN I — IDENTITAS & REKAPITULASI OPERASIONAL PERKULIAHAN

| Atribut Operasional | Ketentuan Pelaksanaan di Kelas |
|---|---|
| **Kode & Nama Mata Kuliah** | `STI-103` — Arsitektur dan Organisasi Sistem Teknologi Informasi — Kurikulum OBE SISTEKIN 2026 |
| **Bobot & Tipe Perkuliahan** | **3 SKS Teori** (`T=3, P=0`) · Semester 1 (Ganjil) · Prasyarat: `-` |
| **CPL & CPMK Dibebankan** | `CPL-05` (`P1`), `CPL-07` (`P3`), `CPL-02` (`KU1`) [Level *Introduce*] · `CPMK-1` (C3), `CPMK-2` (C4), `CPMK-3` (C4), `CPMK-4` (C5) |
| **Durasi per Pertemuan (SN-Dikti)** | **Tatap Muka (TM): 150 menit** ($3 \times 50'$) · **Penugasan Terstruktur (PT): 180 menit** ($3 \times 60'$) · **Belajar Mandiri (BM): 180 menit** ($3 \times 60'$) |
| **Struktur Baku Waktu Tatap Muka** | **Pendahuluan & Pemicu Teknis:** `20 menit` · **Kegiatan Inti (Eksplorasi Arsitektur + Simulasi Visual / *Case Analysis*):** `110 menit` · **Penutup, Refleksi & Tindak Lanjut:** `20 menit` |
| **Media & Simulator Konseptual** | Proyektor, Papan Tulis, Simulator Ringan Berbasis Peramban (*Little Man Computer / CPUlator* untuk siklus Von Neumann, *IEEE-754 Floating Point Visualizer*, *CircuitVerse* untuk gerbang & ALU), Lembar *Datasheet* Prosesor/Server Nyata, LMS Edlink. |
| **Pagar Pembatas Kelas (*Guardrails*)** | 🟢 Fokus pada representasi bit/IEEE 754, gerbang & rangkaian logika pembentuk ALU/register, arsitektur prosesor CISC/RISC, *cache*, akselerator GPU/NPU, bus/DMA, *Hypervisor*, dan organisasi server *data center*.<br>❌ **Larangan Kelas:** Dilarang membahas logika predikat kuantor/himpunan/graf (`STI-204 Matematika Diskrit dan Logika`), aljabar relasional DB (`FST-207`), penjadwalan *process/thread* OS (`STI-310`), *routing* TCP/IP (`STI-312`), atau administrasi klaster Kubernetes (`STI-520`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Fokus Sesi Perkuliahan | Strategi SCL Utama | Durasi TM | Evaluasi |
|:---:|:---:|---|---|:---:|:---:|
| **1** | `Sub-CPMK-1.2` | Kontrak Belajar, Arsitektur vs Organisasi, Model Von Neumann vs Harvard | *Interactive Lecture & Teardown* | 150' | Formatif |
| **2** | `Sub-CPMK-1.1` | Sistem Bilangan Biner/Hex, Aritmetika *Two's Complement*, & ASCII/UTF-8 | *Guided Bitwise Problem Solving* | 150' | Formatif |
| **3** | `Sub-CPMK-1.1, 1.2` | *Floating Point* IEEE 754 (*FP32/FP16*) & Penelusuran Siklus `Fetch-Decode-Execute` | *Simulator-Assisted Tracing* | 150' | Formatif (Rilis Tugas 1) |
| **4** | `Sub-CPMK-2.1` | Gerbang Logika Biner, Aljabar Boole Hardware, & Penyederhanaan K-Map | *Circuit Simplification Workshop* | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Rangkaian Kombinasional (*Adder, MUX, Decoder*) & Konstruksi Dasar ALU | *Collaborative ALU Tracing* | 150' | Formatif |
| **6** | `Sub-CPMK-2.2` | Rangkaian Sekuensial: *Latch*, *Flip-Flop* (`SR, D, JK`), Register, & *Counter* | *Timing Diagram Analysis* | 150' | Formatif |
| **7** | `Sub-CPMK-2.1, 2.2` | Integrasi *CPU Datapath* (Register + ALU + Kontrol) & *Pipelining* + Review UTS | *Datapath Walkthrough* | 150' | Formatif |
| **8** | `CPMK-2` (& `CPMK-1`) | **Ujian Tengah Semester (UTS) — Rangkaian Kombinasional, Sekuensial, & ALU** | *Analytical Circuit & ALU Exam* | 150' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.1` | Komparasi Kritis Arsitektur Set Instruksi CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`) | *Case Method & Tech Debate* | 150' | Formatif |
| **10** | `Sub-CPMK-3.2` | Hierarki Memori (SRAM vs DRAM), Lokalitas, & Kinerja *Cache* `L1/L2/L3` | *Problem-Based Cache Analysis* | 150' | Formatif (Rilis Tugas 2) |
| **11** | `Sub-CPMK-3.2` | Penyimpanan Eksternal (NVMe SSD, HDD, `RAID 0/1/5/10`) & Peran Hardware MMU/TLB | *Case-Based Storage Sizing* | 150' | Formatif |
| **12** | `Sub-CPMK-3.1, 3.2` | Komputasi Paralel & Akselerator Domain-Spesifik: CPU vs GPU vs NPU/TPU | *Case Method Seminar* | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-4.1` | Sistem Interkoneksi Bus (PCIe), *Interrupt-Driven I/O*, & *Direct Memory Access* (DMA) | *Bottleneck Diagnosis Case* | 150' | Formatif |
| **14** | `Sub-CPMK-4.2` | Abstraksi Virtualisasi Hardware (`VT-x/AMD-V`) & Evaluasi *Hypervisor* Tipe 1 vs 2 | *Server Consolidation Case* | 150' | Formatif |
| **15** | `Sub-CPMK-4.2` | Organisasi *Server Data Center* (*Rack/Blade*, *PUE*, *Tier I–IV*) & Review UAS | *Architecture Audit Clinic* | 150' | Formatif |
| **16** | `CPMK-4` (& `1–3`) | **Ujian Akhir Semester (UAS) — Evaluasi Bus/DMA, *Hypervisor*, & *Data Center*** | *Comprehensive Case Exam* | 150' | **UAS (30%)** |

---

## BAGIAN II — RINCIAN SATUAN ACARA PERKULIAHAN PER PERTEMUAN (PERTEMUAN 1 s.d. 16)

---

### PERTEMUAN 1 — Kontrak Belajar, Arsitektur vs Organisasi, & Model Von Neumann vs Harvard
* **Kemampuan Akhir (`Sub-CPMK-1.2` [C2/C3]):** Membedakan arsitektur dengan organisasi sistem komputer serta menjelaskan struktur dan prinsip kerja mesin Von Neumann.
* **Indikator Capaian:** (1) Memberikan contoh konkret pembedaan atribut arsitektur (set instruksi, lebar bit data) vs organisasi (sinyal kontrol, teknologi memori); (2) Memetakan 4 subsistem utama Von Neumann, membandingkannya dengan arsitektur Harvard, dan mengidentifikasi masalah *Von Neumann Bottleneck*.
* **Pokok Bahasan:** Kontrak Belajar OBE, Evolusi Komputasi dari Tabung Vakum ke *Cloud/AI Chip*, Arsitektur vs Organisasi, Model *Stored-Program* Von Neumann vs Harvard, dan Pengantar Siklus Eksekusi Instruksi.
* **Metode & Media:** *Interactive Lecture & Spec Teardown*; Foto *Motherboard/Die Shot* CPU, Proyektor, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memaparkan RPS `STI-103` (3 SKS), pemetaan ke `CPL-05`, `CPL-07`, dan `CPL-02`, serta menunjukkan dua lembar spesifikasi nyata (laptop `x86_64` vs ponsel `ARM64`): *"Mengapa program yang sama kadang tidak bisa langsung dijalankan lintas-prosesor, tetapi di generasi prosesor keluarga yang sama tetap berjalan walau kecepatannya berbeda?"* | Menyimak kontrak belajar dan menebak perbedaan antara "kontrak antarmuka perangkat keras" (arsitektur) dan "cara merakit bagian dalamnya" (organisasi). | 20' | RPS `STI-103` & *Spec Sheet* |
| **Kegiatan Inti** | Menguraikan sejarah singkat hukum Moore & pergeseran arsitektur modern, pembedaan tegas *Architecture vs Organization* (Stallings Bab 1), prinsip *Stored-Program Concept* John von Neumann (instruksi dan data berbagi memori & bus tunggal), perbandingan dengan arsitektur Harvard (memori instruksi & data terpisah), serta pengenalan awal 3 fase siklus `Fetch–Decode–Execute`. | Dalam kelompok kecil membedah diagram blok *motherboard* server/PC, memberi label jalur data antara CPU, RAM, dan I/O, serta mendiskusikan mengapa jalur tunggal antara CPU dan RAM memicu kemacetan (*Von Neumann Bottleneck*). | 110' | `[1]` Bab 1–2, `[3]` Bab 1 & 6 |
| **Penutup** | Menyimpulkan fondasi Pekan 1 dan memberi jembatan ke Pekan 2: bagaimana seluruh instruksi dan data di dalam memori Von Neumann direpresentasikan murni sebagai deretan tegangan biner `0` dan `1`. | Mengerjakan kuis kilat 5 soal di LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Membaca Bab 1 Modul Ajar dan mengidentifikasi spesifikasi prosesor, ukuran cache, RAM, dan tipe penyimpanan pada perangkat komputasi masing-masing.

---

### PERTEMUAN 2 — Sistem Bilangan Biner/Heksadesimal, *Two's Complement*, & Kode Karakter
* **Kemampuan Akhir (`Sub-CPMK-1.1` [C3]):** Mengonversi sistem bilangan biner, oktal, heksadesimal, dan menerapkan representasi bilangan bulat bertanda *Two's Complement*.
* **Indikator Capaian:** (1) Mengonversi bilangan bulat dan pecahan antar-basis 2, 8, 10, dan 16 secara cepat dan akurat; (2) Melakukan penjumlahan/pengurangan biner dengan *Two's Complement*, mendeteksi *overflow*, serta menjelaskan pengkodean ASCII dan UTF-8.
* **Pokok Bahasan:** Sistem Bilangan Posisional, Konversi Cepat Biner $\leftrightarrow$ Heksadesimal, Representasi *Unsigned* vs *Two's Complement*, Aturan *Arithmetic Overflow*, dan Representasi Teks (ASCII/Unicode).
* **Metode & Media:** *Guided Bitwise Problem Solving*; Papan Tulis, Tabel Heksadesimal, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan tangkapan layar *memory hex dump* (`0x7FFF5FBFF8C0`) dan kasus klasik bug permainan/penerbangan ketika variabel *signed integer* melampaui nilai maksimumnya lalu berubah menjadi negatif (*integer overflow*). | Menganalisis mengapa insinyur sistem wajib memahami batas bit bilangan bertanda. | 20' | Slide Kasus *Integer Overflow* |
| **Kegiatan Inti** | Melatih metode konversi basis bilangan dan pengelompokan 4-bit biner ke 1 digit heksadesimal; membandingkan kelemahan *Sign-Magnitude* & *One's Complement* (masalah angka nol ganda) terhadap keunggulan *Two's Complement* (penjumlahan dan pengurangan dapat dieksekusi oleh satu sirkuit penjumlah yang sama!); melatih deteksi *overflow* serta pemetaan string pendek ke kode heksadesimal ASCII/UTF-8. | Menyelesaikan 10 soal latihan konversi dan operasi pengurangan biner 8-bit via *Two's Complement* secara berpasangan, lalu menguji hasilnya di papan tulis. | 110' | `[1]` Bab 9–10, `[3]` Bab 3–4 |
| **Penutup** | Merangkum rumus rentang nilai *Two's Complement* $n$-bit ($-2^{n-1}$ s.d. $2^{n-1}-1$) dan mengantar pertanyaan Pekan 3: bagaimana menyimpan angka desimal berkoma seperti `3,14159` atau `0,000045` di dalam 32 bit? | Mencatat ringkasan aturan *overflow* dan mengunduh lembar latihan mandiri Pekan 2. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan paket latihan 12 soal konversi biner/hex dan operasi *Two's Complement*.

---

### PERTEMUAN 3 — Standar *Floating Point* IEEE 754 & Penelusuran Rinci Siklus `Fetch-Decode-Execute`
* **Kemampuan Akhir (`Sub-CPMK-1.1` & `Sub-CPMK-1.2` [C3]):** Mengonversi representasi *floating point* IEEE 754 dan menelusuri perpindahan data antar-register pada siklus eksekusi instruksi Von Neumann.
* **Indikator Capaian:** (1) Mengonversi bilangan desimal ke IEEE 754 *Single Precision* 32-bit (1 bit *Sign*, 8 bit *Biased Exponent* $+127$, 23 bit *Mantissa*) dan sebaliknya, serta menjelaskan perbedaan presisi `FP64, FP32, FP16, BF16`; (2) Menelusuri isi register `PC, MAR, MBR, IR,` dan `ACC` pada setiap langkah mikro `Fetch-Decode-Execute`.
* **Pokok Bahasan:** Normalisasi Saintifik Biner, Struktur IEEE 754 (Nilai Normal, Nol, $\pm\infty$, `NaN`), Galat Pembulatan Pecahan Biner & Format `FP16/BF16` untuk AI, serta Simulasi Register Siklus Instruksi Von Neumann.
* **Metode & Media:** *Simulator-Assisted Tracing*; *IEEE-754 Web Converter* (untuk verifikasi akhir), *Little Man Computer* (LMC) Simulator, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan ekspresi `0.1 + 0.2` yang menghasilkan `0.30000000000000004` pada hampir semua bahasa pemrograman modern: memantik rasa ingin tahu mengapa komputer "salah hitung" desimal sederhana. | Mengamati fenomena pecahan berulang tak-berhingga ketika $0,1_{10}$ diubah ke basis 2 ($0,000110011\dots_2$). | 20' | Proyektor Demo & Slide |
| **Kegiatan Inti** | Bagian 1 (55'): Memandu langkah demi langkah konversi angka bertanda berkoma ke format IEEE 754 32-bit (dalam biner dan heksadesimal 8 digit) serta mengulas singkat mengapa pelatihan model AI modern memanfaatkan `BF16` (rentang eksponen sama dengan `FP32` dengan mantissa lebih ringkas). Bagian 2 (55'): Menelusuri eksekusi program 4 instruksi (`LOAD, ADD, STORE, HALT`) pada register internal CPU (`PC -> MAR -> Memori -> MBR -> IR`, dekode opcode, eksekusi di `ACC`). | Berlatih mengonversi 3 bilangan pecahan ke IEEE 754 secara manual dan mengisi tabel jejak isi register `PC, MAR, MBR, IR, ACC` untuk setiap siklus instruksi. | 110' | `[1]` Bab 3 & 10, `[3]` Bab 5 & 7, LMC Simulator |
| **Penutup** | Merangkum ketuntasan penuh materi `CPMK-1` dan **merilis resmi naskah RTM-1 (Tugas 1 — Bobot 20%)** di LMS Edlink yang wajib dikumpulkan pada Pekan 4. | Mengunduh instruksi Tugas 1 dan memastikan pemahaman format tabel penelusuran register. | 20' | Dokumen RTM-1 di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan secara mandiri laporan **Tugas 1 (`CPMK-1`: Konversi Biner/Hex, IEEE 754, & Penelusuran Siklus Von Neumann)**.

---

### PERTEMUAN 4 — Gerbang Logika Biner & Penyederhanaan Rangkaian Dasar + Evaluasi Tugas 1
* **Kemampuan Akhir (`Sub-CPMK-2.1` [C4]):** Menganalisis operasi gerbang logika biner dan menyederhanakan rangkaian logika perangkat keras menggunakan aljabar Boole dan Peta Karnaugh, serta menuntaskan evaluasi sumatif **Tugas 1 (20%)**.
* **Indikator Capaian:** (1) Menganalisis tabel kebenaran dan fungsi gerbang `AND, OR, NOT, NAND, NOR, XOR, XNOR` termasuk perwujudan gerbang apa pun menggunakan gerbang universal `NAND`; (2) Menyederhanakan fungsi Boole *Sum-of-Products* (SOP) dengan Peta Karnaugh (K-Map 3 dan 4 variabel) untuk meminimalkan jumlah gerbang fisik pada chip.
* **Pokok Bahasan:** Sakelar Transistor CMOS ke Gerbang Logika, 7 Gerbang Logika Biner, Hukum Aljabar Boole Perangkat Keras (De Morgan), Bentuk Kanonik SOP, dan Minimasi Peta Karnaugh.
* **Metode & Media:** *Circuit Simplification Workshop*; Simulator Web *CircuitVerse*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memverifikasi pengumpulan **Tugas 1 (20%)** di LMS Edlink dan mengadakan cek konfirmasi singkat 10 menit atas pengerjaan IEEE 754/register mahasiswa. | Memastikan Tugas 1 telah terunggah dan mengerjakan soal verifikasi singkat secara mandiri. | 20' | LMS Edlink |
| **Kegiatan Inti** | Menjelaskan bagaimana tegangan tinggi/rendah pada transistor membentuk gerbang logika, menganalisis keunikan gerbang `XOR` (detektor perbedaan bit/paritas) dan universalitas `NAND`/`NOR` di pabrik semikonduktor, lalu melatih penyederhanaan rangkaian menggunakan K-Map 3 dan 4 variabel untuk menghemat luas silikon dan konsumsi daya. *(Menjaga guardrail: tidak melebar ke logika kalimat berkuantor $\forall, \exists$ yang merupakan ranah `STI-204`)*. | Mengonversi spesifikasi masalah kontrol sensor perangkat keras menjadi tabel kebenaran, menyederhanakannya dengan K-Map, dan menggambar rangkaian gerbang sebelum vs sesudah disederhanakan. | 110' | `[1]` Bab 11, `[4]` Bab 2–3, CircuitVerse |
| **Penutup** | Membandingkan jumlah gerbang yang berhasil dihemat oleh kelompok mahasiswa dan mengantar Pekan 5: bagaimana gerbang-gerbang ini dirangkai menjadi mesin penjumlah biner dan ALU. | Menyimpan skema rangkaian hasil latihan dan mencatat poin kunci K-Map. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 8 soal penyederhanaan gerbang logika dan K-Map 4 variabel pada Bab 4 Modul Ajar.
* **Evaluasi Sumatif Pekan Ini:** **Tugas 1 (Bobot 20%)** dinilai menggunakan Rubrik Analitik Tugas 1 (`057_5`).

---

### PERTEMUAN 5 — Rangkaian Logika Kombinasional & Organisasi Dasar *Arithmetic Logic Unit* (ALU)
* **Kemampuan Akhir (`Sub-CPMK-2.1` [C4]):** Menganalisis rancangan rangkaian logika kombinasional (*Adder, Multiplexer, Decoder*) sebagai dasar operasi *Arithmetic Logic Unit* (ALU).
* **Indikator Capaian:** (1) Menganalisis tabel kebenaran dan skema gerbang *Half Adder* (`XOR` + `AND`), *Full Adder*, serta *4-bit Adder-Subtractor* berbasis kontrol `XOR` (*Two's Complement*); (2) Menganalisis peran *Multiplexer* (MUX) dan *Decoder* dalam menyatukan fungsi `AND, OR, ADD, SUB` menjadi satu blok ALU lengkap dengan keluaran *Status Flags* (`Zero, Negative, Carry, Overflow`).
* **Pokok Bahasan:** Karakteristik Rangkaian Kombinasional, *Half & Full Adder*, *Ripple-Carry Adder-Subtractor*, *Decoder & Multiplexer*, serta Anatomi Internal ALU 4-bit/32-bit.
* **Metode & Media:** *Collaborative ALU Tracing*; Skema Blok ALU Interaktif di *CircuitVerse*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membagikan umpan balik Tugas 1, lalu mengajukan tantangan desain: *"Dengan bermodalkan gerbang `AND, OR, NOT, XOR` dari pekan lalu, bagaimana kita merakit sirkuit yang sanggup menjumlahkan dua angka biner?"* | Menemukan sendiri bahwa penjumlahan 1-bit menghasilkan kolom `Sum` = `A XOR B` dan `Carry` = `A AND B` (*Half Adder*!). | 20' | Papan Tulis |
| **Kegiatan Inti** | Mengembangkan *Half Adder* menjadi *Full Adder* (dengan `Carry-In`), merangkainya menjadi penjumlah-pengurang 4-bit menggunakan gerbang `XOR` terkendali sinyal `ModeSub`, lalu memperkenalkan *Multiplexer* sebagai "sakelar pemilih jalur" untuk merakit sebuah **ALU 4-bit** yang memilih antara operasi `AND`, `OR`, `ADD`, dan `SUB` berdasarkan jalur *Opcode/ALUOp*, disertai pembangkitan bit status `Zero (Z)` dan `Overflow (V)`. | Dalam kelompok menelusuri nilai bit pada setiap titik kabel internal skema ALU untuk 4 kombinasi input dan kode operasi yang berbeda, termasuk membuktikan kapan bendera `Zero` dan `Overflow` menyala (`1`). | 110' | `[2]` Lampiran B, `[4]` Bab 4, CircuitVerse |
| **Penutup** | Menyimpulkan keterbatasan rangkaian kombinasional: *"ALU sanggup menghitung cepat, tetapi begitu arus input dicabut, hasilnya lenyap—bagaimana komputer mengingat hasil hitungan?"* (pengantar rangkaian sekuensial Pekan 6). | Mengumpulkan lembar jejak bit ALU kelompok ke LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan analisis skema *4-to-1 Multiplexer* dan perancangan blok ALU 1-bit dengan 4 operasi.

---

### PERTEMUAN 6 — Rangkaian Logika Sekuensial: *Latch*, *Flip-Flop*, Register, & *Counter*
* **Kemampuan Akhir (`Sub-CPMK-2.2` [C4]):** Menganalisis cara kerja *latch*, *flip-flop*, dan rangkaian sekuensial dasar sebagai elemen memori perangkat keras.
* **Indikator Capaian:** (1) Menganalisis mekanisme umpan balik (*feedback loop*) pada *SR Latch* serta transisi status tepi pulsa *clock* (*edge-triggered*) pada *D Flip-Flop* dan *JK Flip-Flop*; (2) Menganalisis bagaimana kumpulan *D Flip-Flop* dengan sinyal *Write Enable* membentuk *Hardware Register* paralel, *Shift Register*, dan *Program Counter*.
* **Pokok Bahasan:** Kombinasional vs Sekuensial, Sinyal *Clock* & Frekuensi GHz, *SR Latch*, *Edge-Triggered D & JK Flip-Flop*, Tabel Karakteristik & *Timing Diagram*, serta Konstruksi Register & *Counter*.
* **Metode & Media:** *Timing Diagram Analysis*; Simulator *CircuitVerse*, Papan Tulis, Lembar Gelombang *Clock*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengaitkan istilah sehari-hari "kecepatan prosesor 3,5 GHz" dengan detak jantung sinyal persegi (*Clock*) yang menyinkronkan jutaan *Flip-Flop* di dalam CPU miliaran kali per detik. | Mengamati ilustrasi gelombang *clock* (tepi naik *rising edge* vs tepi turun *falling edge*). | 20' | Slide Gelombang *Clock* |
| **Kegiatan Inti** | Menelusuri cara sepasang gerbang `NOR`/`NAND` bersilang menyimpan 1 bit informasi (*SR Latch*), mengatasi kondisi terlarang melalui *D Flip-Flop* dan *JK Flip-Flop* berpicu tepi *clock*, melatih pembacaan dan penggambaran *Timing Diagram* keluaran $Q(t+1)$, serta merangkai 8 buah *D Flip-Flop* menjadi sebuah **Register 8-bit** dan pencacah biner (*Counter* pembentuk `PC`). | Menggambar gelombang keluaran $Q$ pada lembar latihan *Timing Diagram* untuk serangkaian perubahan sinyal `D`, `Clock`, dan `Enable`, serta menganalisis pergeseran bit pada *Shift Register*. | 110' | `[1]` Bab 11, `[4]` Bab 5–6 |
| **Penutup** | Menunjukkan benang merah: *Flip-Flop* adalah sel dasar pembentuk **Register CPU** sekaligus sel penyimpan **SRAM (*Cache Memory*)** yang akan dianalisis lebih dalam setelah UTS. | Mengerjakan kuis singkat 3 soal tabel karakteristik *Flip-Flop*. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan 8 soal analisis *Timing Diagram* dan tabel status rangkaian sekuensial sederhana.

---

### PERTEMUAN 7 — Integrasi *CPU Datapath*, Pengantar *Pipelining*, & Review Komprehensif Pra-UTS
* **Kemampuan Akhir (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]):** Menganalisis kerja terpadu *Register File* (sekuensial) dan ALU (kombinasional) di dalam *datapath* prosesor serta konsep dasar *instruction pipelining*.
* **Indikator Capaian:** (1) Menelusuri jalur pembacaan dua register sumber, eksekusi operasi di ALU, dan penulisan balik ke register tujuan pada tepi *clock* berikutnya; (2) Menganalisis analogi lini perakitan *5-stage instruction pipeline* (`IF–ID–EX–MEM–WB`) dan mengenali penyebab kemacetan *structural/data/control hazard* secara konseptual.
* **Pokok Bahasan:** Arsitektur *Single-Cycle Datapath* Sederhana, Koordinasi Unit Kontrol, Konsep *Instruction Pipelining* & *Speedup*, serta Konsolidasi Materi Pekan 1–7.
* **Metode & Media:** *Datapath Walkthrough*; Diagram Blok *CPU Datapath*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan skema utuh gabungan *Register File* (Pekan 6) + *Multiplexer* + *ALU* (Pekan 5): memperlihatkan bagaimana seluruh kepingan materi paruh pertama semester menyatu menjadi inti sebuah CPU! | Mengamati keterhubungan antara elemen sekuensial penyimpan data dan elemen kombinasional pengolah data. | 20' | Diagram *CPU Datapath* |
| **Kegiatan Inti** | Bagian 1 (60'): Menelusuri eksekusi instruksi tipe-R (`ADD R1, R2, R3`) dan instruksi *Load/Branch* pada diagram *datapath*, dilanjutkan pengenalan *pipelining* 5-tahap beserta contoh *data hazard* ketika instruksi kedua langsung membutuhkan hasil instruksi pertama. Bagian 2 (50'): Klinik bedah latihan soal komprehensif persiapan **UTS Pekan 8**. | Menelusuri aktif-tidaknya jalur sinyal kontrol pada skema *datapath*, menghitung waktu eksekusi non-pipeline vs pipeline sederhana, dan mendiskusikan soal simulasi UTS. | 110' | `[1]` Bab 14, `[2]` Bab 4 |
| **Penutup** | Membagikan kisi-kisi resmi, alokasi bobot butir soal, dan kriteria Rubrik Analitik **UTS Pekan 8 (Bobot 30%)**. | Mencatat kisi-kisi UTS dan menanyakan klarifikasi atas topik K-Map, ALU, atau *Flip-Flop*. | 20' | Kisi-Kisi UTS di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan mandiri paket simulasi UTS pada LMS Edlink.

---

### PERTEMUAN 8 — EVALUASI TENGAH SEMESTER (UTS)
* **Kemampuan Akhir Diuji (`CPMK-2` [C4] & penguatan `CPMK-1`):** Menganalisis rancangan rangkaian logika kombinasional dan sekuensial menggunakan gerbang logika biner serta *flip-flop* sebagai dasar operasi *Arithmetic Logic Unit* (ALU) dan *datapath* prosesor.
* **Bentuk & Durasi:** Ujian Tertulis Analisis Rangkaian & Arsitektur ALU Terjadwal (*Closed-Book*), **150 menit**.
* **Bobot Penilaian Sumatif:** **30%** terhadap Nilai Akhir Mata Kuliah.

| Tahap | Aktivitas Pengawas / Dosen | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan daftar hadir berita acara UTS, pengaturan ruang ujian, pembacaan tata tertib kejujuran akademik, dan pembagian naskah soal UTS. | Menandatangani presensi dan menyiapkan alat tulis/penggaris skema rangkaian. | 10' | Berita Acara & Naskah UTS |
| **Pelaksanaan Ujian** | Mengawasi jalannya ujian secara tertib. | Mengerjakan 4 butir soal analisis (minimasi gerbang K-Map, analisis rangkaian kombinasional & *flags* ALU, *Timing Diagram Flip-Flop*/Register, dan penelusuran *datapath* CPU). | 135' | Lembar Jawaban UTS |
| **Pengumpulan** | Mengumpulkan dan memverifikasi kelengkapan lembar jawaban. | Menyerahkan lembar jawaban secara tertib. | 5' | Bundel Jawaban UTS |

---

### PERTEMUAN 9 — Komparasi Kritis Arsitektur Prosesor CISC (`x86_64`) vs RISC (`ARM64` / `RISC-V`)
* **Kemampuan Akhir (`Sub-CPMK-3.1` [C4]):** Membandingkan secara kritis karakteristik arsitektur set instruksi CISC (`x86_64`) dan RISC (`ARM64` / `RISC-V`) dalam skenario beban kerja komputasi nyata.
* **Indikator Capaian:** (1) Membandingkan CISC dan RISC pada minimal 6 dimensi teknis (format panjang instruksi variabel vs tetap, akses memori *register-memory* vs *load-store*, kompleksitas dekoder *micro-ops*, jumlah register umum, luas *die*, dan performa per watt); (2) Menganalisis alasan teknis adopsi `ARM64` (Apple M-series, AWS Graviton, Ampere) dan standar terbuka `RISC-V` dibandingkan `x86_64` (Intel Xeon, AMD EPYC) di era komputasi mobile, IoT, dan *cloud*.
* **Pokok Bahasan:** Pengertian *Instruction Set Architecture* (ISA), Karakteristik CISC (`x86_64`), Karakteristik RISC (`ARM64` & *Open-Source ISA* `RISC-V`), Konvergensi Internal Modern (*Micro-ops* di dalam chip `x86`), dan Analisis Beban Kerja Nyata.
* **Metode & Media:** *Case Method & Technical Debate*; Artikel Industri/Datasheet `AWS Graviton vs x86 Instance`, Proyektor, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membahas umpan balik hasil UTS, lalu memantik diskusi hangat industri: *"Mengapa Apple meninggalkan prosesor Intel x86 ke chip ARM buatannya sendiri, dan mengapa penyedia cloud raksasa merancang prosesor server ARM sendiri?"* | Mengemukakan pengamatan tentang daya tahan baterai, suhu panas, dan biaya listrik server. | 20' | Pembahasan UTS & Slide Industri |
| **Kegiatan Inti** | Mengupas perbedaan mendasar filosofi CISC vs RISC, meluruskan mitos populer (bahwa chip `x86_64` modern secara internal juga memecah instruksi kompleks menjadi *RISC-like micro-operations*, namun tetap menanggung beban dekoder instruksi panjang-variabel), serta memperkenalkan kebangkitan ekosistem terbuka `RISC-V` untuk mikrokontroler IoT hingga akselerator khusus. Memandu diskusi kasus terstruktur membandingkan pemilihan instance cloud berbasis `x86_64` vs `ARM64`. | Kelompok menyusun matriks perbandingan kritis CISC vs RISC dan mempertahankan argumen pemilihan arsitektur untuk kasus server web berkapasitas tinggi vs *workstation* aplikasi warisan (*legacy Windows binaries*). | 110' | `[1]` Bab 12–13, `[2]` Bab 2, `[6]` |
| **Penutup** | Merangkum kesimpulan objektif (kapan `x86_64` tetap unggul kompatibilitas/ekosistem vs kapan `ARM64`/`RISC-V` unggul efisiensi energi/kepadatan *core*). | Mengunggah ringkasan matriks debat kelompok ke LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Membaca artikel Hennessy & Patterson (`[6]`) dan membandingkan lembar spesifikasi nyata 1 prosesor server `x86_64` dengan 1 prosesor server `ARM64`.

---

### PERTEMUAN 10 — Hierarki Memori, Lokalitas Referensi, & Kinerja *Cache* `L1/L2/L3`
* **Kemampuan Akhir (`Sub-CPMK-3.2` [C4]):** Menganalisis hierarki memori serta pengaruh organisasi *cache* `L1/L2/L3` terhadap performa komputasi.
* **Indikator Capaian:** (1) Menganalisis kesenjangan kecepatan CPU vs DRAM (*Memory Wall*) dan perbedaan fisik SRAM (berbasis *flip-flop* cepat & mahal) vs DRAM (berbasis kapasitor padat & butuh *refresh*); (2) Menganalisis prinsip lokalitas temporal & spasial, pemetaan *Direct/Associative/Set-Associative*, serta menghitung *Effective Access Time* (EAT) bertingkat `L1 → L2 → L3 → RAM`.
* **Pokok Bahasan:** Piramida Hierarki Memori, *Memory Wall*, SRAM vs DRAM (DDR4/DDR5/HBM), Prinsip Lokalitas Referensi, Struktur *Cache Line/Block*, Organisasi Multi-Level `L1i/L1d, L2, L3`, dan Perhitungan *Hit/Miss Penalty*.
* **Metode & Media:** *Problem-Based Cache Analysis*; Diagram *CPU Die Cache*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan dua potongan pseudocode penelusuran tabel 2D berukuran besar—satu membaca baris demi baris, satu lagi melompat kolom demi kolom—dengan jumlah operasi sama persis namun waktu eksekusi berbeda hingga $10\times$ lipat! | Menganalisis mengapa pola akses memori yang berurutan (*spatial locality*) jauh lebih ramah terhadap perangkat keras. | 20' | Demo Konseptual *Row vs Column Traversal* |
| **Kegiatan Inti** | Menguraikan struktur piramida memori, kontras teknologi SRAM vs DRAM (serta pengenalan *High Bandwidth Memory / HBM* pada chip AI), mekanisme penyalinan blok *cache line*, komparasi *Direct-Mapped* vs *N-Way Set-Associative* vs *Fully Associative*, kebijakan penulisan (*Write-Through* vs *Write-Back*), serta perhitungan matematis *Effective Access Time* (EAT) pada *cache* bertingkat. | Menghitung EAT sistem memori 2–3 level pada berbagai nilai *hit ratio* (mis. beda drastis antara *hit ratio* $98\%$ vs $90\%$!) dan menganalisis pembagian *Cache* `L1` privat per-*core* vs `L3` bersama (*shared*). | 110' | `[1]` Bab 4–5, `[2]` Bab 5 |
| **Penutup** | Merangkum dampak *cache* terhadap rekayasa perangkat lunak/basis data dan **merilis resmi naskah RTM-2 (Tugas 2 — Bobot 20%)** di LMS Edlink untuk dikumpulkan pada Pekan 12. | Mengunduh instruksi studi kasus *benchmarking* Tugas 2 di Edlink. | 20' | Dokumen RTM-2 di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mulai menyusun Bagian 1 & 2 laporan **Tugas 2** (komparasi CISC vs RISC dan analisis kinerja *cache* `L1/L2/L3`).

---

### PERTEMUAN 11 — Penyimpanan Sekunder Modern (NVMe SSD, HDD, RAID) & Peran Hardware MMU/TLB
* **Kemampuan Akhir (`Sub-CPMK-3.2` [C4]):** Menganalisis karakteristik penyimpanan sekunder modern, redundansi RAID, dan dukungan perangkat keras memori virtual.
* **Indikator Capaian:** (1) Membandingkan arsitektur *NAND Flash* NVMe SSD (jalur PCIe langsung) vs SATA SSD vs HDD magnetik dari sisi latensi, IOPS acak, dan *wear-leveling*; (2) Menganalisis kapasitas bersih, kecepatan baca/tulis, dan ketahanan gagal disk (*fault tolerance*) pada `RAID 0, RAID 1, RAID 5, RAID 6,` dan `RAID 10`, serta menjelaskan peran perangkat keras MMU & TLB.
* **Pokok Bahasan:** Arsitektur HDD vs SATA SSD vs NVMe M.2/U.2 Enterprise SSD, Konsep *Striping, Mirroring,* & *Parity* pada RAID, serta Dukungan Hardware *Memory Management Unit* (MMU) & *Translation Lookaside Buffer* (TLB).
* **Metode & Media:** *Case-Based Storage Sizing*; Studi Kasus Server Database, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengajukan skenario insiden nyata: *"Sebuah rumah sakit menyimpan seluruh rekam medis pada satu keping SSD 4 TB cepat tanpa cadangan redundan; suatu pagi keping SSD tersebut rusak pengontrolnya—apa dampaknya bagi layanan?"* | Menyadari bahwa kecepatan tinggi saja tidak cukup untuk infrastruktur TI bisnis tanpa keandalan (*availability*). | 20' | Skenario Insiden *Storage* |
| **Kegiatan Inti** | Membandingkan mekanika piringan magnetik HDD vs sel *Flash* SSD dan protokol antrean paralel NVMe; membedah matriks konfigurasi `RAID 0, 1, 5, 6, 10` (jumlah minimum disk, persentase kapasitas terpakai, penalti tulis paritas, dan jumlah disk yang boleh mati bersamaan tanpa kehilangan data); serta menjelaskan secara ringkas bagaimana unit perangkat keras **MMU** dan *cache* alamat **TLB** di dalam CPU membantu sistem operasi menerjemahkan alamat virtual ke alamat RAM fisik *(menjaga guardrail: algoritma page replacement OS diserahkan ke `STI-310`)*. | Menghitung kapasitas efektif dan menganalisis *trade-off* biaya-performa-keamanan berbagai opsi RAID untuk studi kasus 4–8 keping SSD server enterprise. | 110' | `[1]` Bab 6 & 8, `[3]` Bab 10 |
| **Penutup** | Menyimpulkan rekomendasi praktis pemilihan RAID industri (mengapa `RAID 10` disukai untuk basis data bertransaksi tulis tinggi dibandingkan `RAID 5`). | Melengkapi rancangan bagian penyimpanan pada draf laporan Tugas 2. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Melanjutkan pengerjaan **Tugas 2** dan membaca materi arsitektur akselerator GPU/NPU untuk Pekan 12.

---

### PERTEMUAN 12 — Arsitektur Paralel & Akselerator Komputasi (CPU vs GPU vs NPU/TPU) + Evaluasi Tugas 2
* **Kemampuan Akhir (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C4]):** Membandingkan arsitektur komputasi paralel serta akselerator GPU/NPU/TPU terhadap CPU dalam skenario beban kerja komputasi nyata, serta menuntaskan evaluasi sumatif **Tugas 2 (20%)**.
* **Indikator Capaian:** (1) Mengklasifikasikan arsitektur menurut *Flynn's Taxonomy* (`SISD, SIMD, MISD, MIMD`) dan menjelaskan perbedaan *multicore* vs *hardware multithreading* (SMT); (2) Membandingkan anatomi internal CPU (*few powerful cores*, *cache* & unit prediksi cabang besar) vs GPU (*thousands of throughput cores / Tensor Cores* + memori HBM/GDDR berlebar pita masif) vs NPU/TPU (*systolic array* hemat daya untuk inferensi AI).
* **Pokok Bahasan:** Batas Frekuensi Termal (*Power Wall*) & Lahirnya *Multicore*, Taksonomi Flynn & Instruksi Vektor SIMD, serta Komparasi Arsitektural CPU vs GPU vs NPU/TPU pada Beban Kerja Nyata.
* **Metode & Media:** *Case Method Seminar*; Diagram *Die Layout* CPU vs GPU vs NPU, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memverifikasi pengumpulan **Tugas 2 (20%)** di LMS Edlink, lalu memperlihatkan perbandingan diagram *layout* silikon CPU (didominasi *Control* & *Cache*) vs GPU (didominasi ribuan ALU kecil berjajar): *"Mengapa kartu grafis game justru menjadi mesin utama revolusi ChatGPT dan Deep Learning?"* | Memastikan Tugas 2 terunggah dan mengamati kontras mencolok proporsi ALU pada diagram CPU vs GPU. | 20' | LMS Edlink & Diagram CPU vs GPU |
| **Kegiatan Inti** | Menguraikan *Power Wall*, paralelisme data SIMD, perbedaan filosofi *Latency-Oriented Processor* (CPU) vs *Throughput-Oriented Accelerator* (GPU) vs *Domain-Specific Neural Accelerator* (NPU di laptop/ponsel *AI PC* dan TPU di *data center*), dilengkapi Hukum Amdahl sederhana tentang batas percepatan paralel. Memfasilitasi seminar singkat di mana 4 perwakilan mahasiswa memaparkan temuan menarik dari laporan *benchmarking* **Tugas 2** mereka. | Menganalisis beban kerja mana yang cocok dieksekusi di CPU (logika bisnis bercabang/OS), di GPU (pelatihan matriks besar), dan di NPU (inferensi AI lokal hemat baterai), serta mendiskusikan studi kasus Tugas 2. | 110' | `[1]` Bab 17–18, `[6]` |
| **Penutup** | Merangkum tuntas `CPMK-3` dan membuka cakrawala `CPMK-4` (Pekan 13–15): bagaimana CPU, RAM, NVMe, dan GPU dihubungkan oleh jalur bus cepat, diabstraksikan oleh *Hypervisor*, dan ditata di dalam *Data Center Cloud*. | Mencatat rangkuman perbandingan CPU–GPU–NPU. | 20' | Salindia Jembatan `CPMK-4` |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Membaca Bab 12 Modul Ajar tentang interkoneksi bus PCIe, interupsi I/O, dan DMA.
* **Evaluasi Sumatif Pekan Ini:** **Tugas 2 (Bobot 20%)** dinilai menggunakan Rubrik Analitik Tugas 2 (`057_5`).

---

### PERTEMUAN 13 — Sistem Interkoneksi Bus (PCIe), *Interrupt-Driven I/O*, & *Direct Memory Access* (DMA)
* **Kemampuan Akhir (`Sub-CPMK-4.1` [C5]):** Mengevaluasi mekanisme bus sistem, interupsi perangkat keras I/O, dan *Direct Memory Access* (DMA) dalam mencegah kemacetan kinerja sistem.
* **Indikator Capaian:** (1) Mengevaluasi kapasitas lebar pita (*bandwidth*) jalur antarmuka PCIe (`Gen 3/4/5`, konfigurasi `x1, x4, x8, x16 lanes`) ketika melayani kartu jaringan cepat, NVMe SSD, dan akselerator GPU; (2) Mengevaluasi perbandingan mekanisme *Programmed I/O* (*busy-waiting/polling*), *Interrupt-Driven I/O*, dan *Direct Memory Access* (DMA) terhadap utilisasi CPU dan *throughput* transfer data.
* **Pokok Bahasan:** Evolusi Bus Bersama ke Interkoneksi *Point-to-Point* Seri Cepat (PCIe), Perhitungan *Bandwidth* Jalur PCIe, Fungsi Modul/Kontroler I/O, Siklus Penanganan Interupsi Perangkat Keras, dan Arsitektur Transfer *Direct Memory Access* (DMA).
* **Metode & Media:** *Bottleneck Diagnosis Case*; Diagram Topologi *Motherboard/Server PCIe Lanes*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membagikan umpan balik Tugas 2, lalu menyajikan kasus nyata: seorang teknisi memasang GPU mutakhir dan 3 SSD NVMe ke sebuah *board* yang jalur PCIe-nya terbagi ke mode `x4` generasi lama, sehingga performa pelatihan AI anjlok separuhnya—mengapa hal itu terjadi? | Mendiagnosis bahwa kehebatan GPU percuma apabila "jalan tol" pengumpan datanya (bus PCIe) menyempit. | 20' | Studi Kasus *PCIe Bottleneck* |
| **Kegiatan Inti** | Menguraikan arsitektur *lanes* dua arah (*full-duplex*) pada generasi PCIe beserta perhitungan laju transfer GB/detik; kemudian membedah 3 evolusi teknik I/O: mengapa *Programmed I/O* memboroskan 100% waktu CPU untuk menunggu perangkat lambat, bagaimana *Interrupt-Driven I/O* membebaskan CPU bekerja hingga perangkat memberi sinyal interupsi, dan mengapa untuk blok data besar (disk NVMe / jaringan 100GbE / memori GPU) pengontrol **DMA** wajib mengambil alih penyalinan langsung ke RAM tanpa membebani CPU per kata data. | Mengevaluasi skenario topologi jalur PCIe server dan menghitung perbandingan beban siklus CPU antara *Interrupt I/O* murni vs *DMA* saat memindahkan berkas 4 GB dari NVMe ke RAM. | 110' | `[1]` Bab 3 & 7, `[3]` Bab 9 |
| **Penutup** | Menyimpulkan kriteria evaluasi keseimbangan antara kecepatan prosesor, memori, bus PCIe, dan mekanisme DMA pada server berkinerja tinggi. | Menyelesaikan kuis singkat evaluasi skenario I/O di LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan evaluasi *diagram blok server topology* (menemukan leher botol lebar pita antara CPU, RAM, NIC, NVMe, dan GPU).

---

### PERTEMUAN 14 — Abstraksi Virtualisasi Perangkat Keras & Evaluasi Arsitektur *Hypervisor*
* **Kemampuan Akhir (`Sub-CPMK-4.2` [C5]):** Mengevaluasi mekanisme abstraksi virtualisasi perangkat keras (*Hardware-Assisted Virtualization*) dan arsitektur *Hypervisor* untuk efisiensi infrastruktur TI.
* **Indikator Capaian:** (1) Mengevaluasi peran dukungan perangkat keras pada CPU (`Intel VT-x / AMD-V`, *Ring/-1 Root Mode*), memori (`EPT / RVI` *Second-Level Address Translation*), dan I/O (`VT-d / IOMMU GPU Passthrough*) dalam menghilangkan *overhead* virtualisasi klasik; (2) Mengevaluasi perbandingan *Hypervisor* Tipe 1 (*Bare-Metal*: KVM/Proxmox, VMware ESXi, Xen, Hyper-V) vs Tipe 2 (*Hosted*: VirtualBox/Workstation) serta merencanakan alokasi sumber daya konsolidasi server fisik ke *Virtual Machine* (VM).
* **Pokok Bahasan:** Masalah *Underutilization* Server Fisik Tunggal, Konsep Abstraksi Mesin Virtual, Dukungan Ekstensi Hardware CPU/MMU/IOMMU, Evaluasi *Hypervisor* Tipe 1 vs Tipe 2, Perbedaan Batas Abstraksi Hardware VM vs Kontainer, serta Risiko *Resource Overcommitment*.
* **Metode & Media:** *Server Consolidation Case Study*; Diagram Lapisan *Hypervisor*, Lembar Kasus Konsolidasi Server, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menyajikan fakta audit ruang server tradisional: 8 unit server fisik menyala 24 jam menghabiskan listrik dan AC besar, padahal rata-rata utilisasi CPU tiap server hanya $8\%\text{–}12\%$! Bagaimana arsitektur perangkat keras modern menyelesaikannya? | Mengidentifikasi konsep penyatuan banyak mesin virtual terisolasi di atas sedikit server fisik (*server consolidation*). | 20' | Slide Audit Utilisasi Server |
| **Kegiatan Inti** | Menjelaskan bagaimana instruksi istimewa (*privileged instructions*) dari OS tamu ditangani oleh ekstensi silikon `Intel VT-x / AMD-V` tanpa emulasi perangkat lunak lambat, bagaimana `EPT` mempercepat pemetaan memori tamu, dan bagaimana `IOMMU / SR-IOV` mengizinkan sebuah VM mengakses langsung kartu jaringan/GPU fisik. Membandingkan kritis *Hypervisor* Tipe 1 vs Tipe 2 (mengapa *cloud provider* seperti AWS/GCP selalu memakai *Bare-Metal Hypervisor* seperti KVM/Nitro) serta memandu studi kasus perhitungan kapasitas *vCPU, RAM,* dan *Storage* saat mengonsolidasi 6 aplikasi server organisasi ke 2 *host* fisik redundan. *(Menjaga guardrail: konfigurasi manajemen cloud/Kubernetes praktis diserahkan ke `STI-520`)*. | Kelompok mengevaluasi kelayakan skema konsolidasi 6 server fisik ke 2 server *host* *Hypervisor* Tipe 1, menghitung cadangan kapasitas saat 1 *host* mengalami pemeliharaan (*failover*), dan mengkritisi bahaya *RAM overcommitment*. | 110' | `[3]` Bab 12 & 15, `[5]` Bab 9 |
| **Penutup** | Merangkum posisi *Hypervisor* sebagai jembatan kunci yang mengubah perangkat keras fisik kaku menjadi sumber daya *elastic cloud*. | Mengunggah lembar hasil evaluasi konsolidasi server kelompok ke LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Membaca Bab 14 Modul Ajar mengenai organisasi fisik *server data center*, redundansi, dan klasifikasi *Tier*.

---

### PERTEMUAN 15 — Organisasi *Server Data Center* Modern untuk Infrastruktur Cloud & Review Pra-UAS
* **Kemampuan Akhir (`Sub-CPMK-4.2` [C5]):** Mengevaluasi organisasi server *data center* modern (*form factor*, redundansi daya/pendinginan, penyimpanan terpusat, dan klasifikasi *Tier*) untuk mendukung infrastruktur *cloud*, serta menyintesiskan seluruh `CPMK-1..4`.
* **Indikator Capaian:** (1) Mengevaluasi pemilihan faktor bentuk server (*Tower* vs *Rackmount 1U/2U/4U* vs *Blade*), pasokan daya redundan ($N+1 / 2N$ PSU & UPS), manajemen aliran udara panas-dingin & metrik efisiensi energi *Power Usage Effectiveness* ($\text{PUE} = \frac{\text{Total Facility Power}}{\text{IT Equipment Power}}$), serta pengantar konsep *DAS vs NAS vs SAN*; (2) Mengevaluasi tingkat ketersediaan pusat data (*Uptime Institute Tier I s.d. Tier IV* dan makna *99,9% vs 99,995% availability* dalam menit *downtime* per tahun).
* **Pokok Bahasan:** Anatomi Rak *Data Center* Modern, *Form Factor* Server, Arsitektur Penyimpanan Konseptual (`DAS, NAS, SAN`), Redundansi Daya & Pendinginan (*PUE*), Standar Klasifikasi *Data Center Tier I–IV*, Fondasi Fisik di Balik *Cloud Computing*, dan Klinik Sintesis Pra-UAS.
* **Metode & Media:** *Architecture Audit Clinic*; Studi Kasus Dokumen Spesifikasi Pengadaan Server, Proyektor, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menegaskan kenyataan fisik kepada mahasiswa: *"Tidak ada yang benar-benar melayang di awan—Cloud Computing sesungguhnya adalah ribuan rak server fisik, memori ECC, SSD NVMe, Hypervisor, sistem daya redundan, dan pendingin raksasa di sebuah Data Center!"* | Menyadari keterhubungan utuh perjalanan materi dari bit biner (Pekan 1) hingga pusat data awan (Pekan 15). | 20' | Foto Interior *Hyperscale Data Center* |
| **Kegiatan Inti** | Bagian 1 (65'): Membedah organisasi rak server (`1U/2U`, memori *ECC Registered RAM* pengoreksi galat bit, *dual redundant PSU*, manajemen jarak jauh *IPMI/BMC*), menghitung metrik efisiensi energi **PUE** dan durasi *downtime* tahunan tiap level **Tier I–IV**, serta memetakan perbedaan konseptual penyimpanan `DAS, NAS,` dan `SAN`. Bagian 2 (45'): Klinik bedah studi kasus simulasi **UAS Pekan 16** (mengaudit proposal pengadaan server yang cacat desain). | Mengevaluasi satu contoh proposal spesifikasi ruang server organisasi, menemukan titik kegagalan tunggal (*Single Point of Failure / SPOF*), menghitung PUE & target *availability*, serta mendiskusikan soal latihan pra-UAS. | 110' | `[3]` Bab 12 & 18 |
| **Penutup** | Membagikan kisi-kisi resmi **UAS Pekan 16 (Bobot 30%)**, kriteria Rubrik Analitik UAS, dan memandu pengisian survei refleksi ketercapaian `Sub-CPMK` di LMS Edlink. | Mengisi survei refleksi diri `STI-103` di Edlink dan mencatat kisi-kisi UAS. | 20' | Kisi-Kisi UAS & Survei Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Persiapan komprehensif menghadapi UAS menggunakan paket studi kasus sintesis pada Unit Evaluasi E2 Modul Ajar.

---

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **Kemampuan Akhir Diuji (`CPMK-4` [C5] & Sintesis Komprehensif `CPMK-1` s.d. `CPMK-4`):** Mengevaluasi secara komprehensif mekanisme bus sistem, interupsi I/O & DMA, abstraksi virtualisasi perangkat keras (*Hypervisor*), serta organisasi server *data center* untuk mendukung infrastruktur *cloud* modern.
* **Bentuk & Durasi:** Ujian Tertulis Evaluasi Studi Kasus Infrastruktur Sistem TI Terjadwal (*Closed-Book*), **150 menit**.
* **Bobot Penilaian Sumatif:** **30%** terhadap Nilai Akhir Mata Kuliah.

| Tahap | Aktivitas Pengawas / Dosen | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan daftar hadir berita acara UAS, pembacaan tata tertib integritas akademik, dan pembagian naskah soal studi kasus UAS. | Menandatangani daftar hadir dan menyiapkan peralatan ujian. | 10' | Berita Acara & Naskah UAS |
| **Pelaksanaan Ujian** | Mengawasi jalannya ujian secara objektif dan tertib. | Mengerjakan 4 studi kasus evaluatif (evaluasi jalur bus PCIe & DMA, evaluasi konsolidasi *Hypervisor* Tipe 1, audit & perbaikan spesifikasi *server data center* berstandar ketersediaan tinggi, dan sintesis lintas-lapisan arsitektur sistem TI untuk beban kerja cerdas). | 135' | Lembar Jawaban UAS |
| **Penutupan** | Mengumpulkan lembar jawaban, menutup rangkaian perkuliahan semester secara resmi, dan menyampaikan alur publikasi rincian capaian `CPL-05`, `CPL-07`, & `CPL-02` di Edlink/SIAKAD. | Menyerahkan lembar jawaban dan mengakhiri perkuliahan semester. | 5' | Bundel Jawaban UAS |

---

## BAGIAN III — PROTOKOL OPERASIONAL SIMULATOR KONSEPTUAL & PENJAGAAN GUARDRAIL

1. **Pemanfaatan Simulator Tanpa Beban Praktikum Berat:** Karena `STI-103` berstatus **3 SKS Teori (`P=0`)**, penggunaan alat bantu seperti *Little Man Computer*, *IEEE-754 Visualizer*, dan *CircuitVerse* difungsikan murni sebagai **media visualisasi konseptual berbasis peramban (*zero-install browser tools*)** untuk memperjelas cara kerja register, bit, dan gerbang logika—bukan praktikum penyolderan perangkat keras elektronika maupun penulisan bahasa rakitan (*assembly*) panjang yang rumit.
2. **Disiplin Penjagaan Batas *Handoff* Lintas-Semester:**
   - Saat membahas gerbang logika biner (Pekan 4), dosen secara tegas membatasi materi pada sirkuit biner perangkat keras dan menyerahkan logika proposisional formal, logika predikat berkuantor, himpunan, serta graf ke **`STI-204 Matematika Diskrit dan Logika`** (Semester 2).
   - Saat membahas interupsi perangkat keras dan MMU/TLB (Pekan 11 & 13), fokus dibatasi pada mekanisme dukungan silikon/kontroler perangkat keras, sedangkan penjadwalan proses, *deadlock*, dan manajemen memori kernel diserahkan ke **`STI-310 Sistem Operasi`** (Semester 3).
   - Saat membahas *Hypervisor* dan organisasi rak server (Pekan 14–15), fokus dibatasi pada evaluasi arsitektur perangkat keras dan abstraksi virtualisasi dasar, sedangkan penyediaan layanan IaaS/PaaS, *container orchestration*, dan arsitektur *cloud-native* diserahkan ke **`STI-520 Infrastruktur dan Komputasi Awan`** (Semester 5).
