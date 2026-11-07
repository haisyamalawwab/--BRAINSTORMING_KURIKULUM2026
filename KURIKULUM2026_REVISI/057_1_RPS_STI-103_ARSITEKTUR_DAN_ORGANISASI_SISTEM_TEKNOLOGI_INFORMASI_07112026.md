# RENCANA PEMBELAJARAN SEMESTER (RPS)

## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI
### *Information Technology Systems Architecture and Organization*

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)
> **Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang
> **Nomor Dokumen SPMI:** 071030.B4.5.2.RPS-STI103
> **Tanggal Penyusunan:** 07 November 2026
> **Sumber Data:** Dokumen 005 (struktur & identitas), 007 (silabus), 043 (CPMK/Sub-CPMK/Boundary Guardrails), 003 (CPL), 008 & 018 (skema asesmen dan rubrik)

---

## HALAMAN 1 — SAMPUL DEPAN (LANDSCAPE)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                            UNIVERSITAS WIDYAGAMA                             │
│                    FAKULTAS SAINS DAN TEKNOLOGI INFORMASI                    │
│                                                                              │
│                                                                              │
│                  RENCANA PEMBELAJARAN SEMESTER (RPS)                         │
│                                                                              │
│                                                                              │
│      STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI          │
│   Information Technology Systems Architecture and Organization            │
│                                                                              │
│                            BOBOT: 3 SKS (TEORI)                              │
│                                                                              │
│                                                                              │
│                    Penyusun: Tim Pengembang RPS SISTEKIN                     │
│                    Koordinator RMK Infrastruktur & Arsitektur Komputer       │
│                                                                              │
│                                                                              │
│                            MALANG, NOVEMBER 2026                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## HALAMAN 2 — IDENTITAS, OTORISASI, DAN CAPAIAN PEMBELAJARAN (LANDSCAPE)

### A. Tabel Identitas Mata Kuliah

| Atribut | Spesifikasi |
|---|---|
| **MATA KULIAH (MK)** | Arsitektur dan Organisasi Sistem Teknologi Informasi / *Information Technology Systems Architecture and Organization* |
| **KODE** | `STI-103` |
| **RUMPUN MK** | Infrastruktur & Arsitektur Komputer (Core STI) |
| **BOBOT (sks)** | **T = 3** · **P = 0** — Total 3 SKS |
| **SEMESTER** | 1 (Gasal) |
| **TGL PENYUSUNAN** | 07 November 2026 |
| **MATA KULIAH SYARAT** | — (tidak ada prasyarat) |
| **DOSEN PENGAMPU** | Tim Pengampu Rumpun Infrastruktur & Arsitektur Komputer (Core STI) |
| **BODY OF KNOWLEDGE** | `BK-IS03` *IT Infrastructure*; `BK-IT01` *IT Fundamentals*; `BK-IT05` *Computer Architecture* |

### B. Blok Otorisasi

| Pengembang RPS | Koordinator RMK | Ketua Program Studi |
|:---:|:---:|:---:|
| Tim Pengembang RPS SISTEKIN | Koordinator RMK Infrastruktur & Arsitektur Komputer | Ketua Prodi SISTEKIN FSTI |
| .......................... | .......................... | .......................... |

### C. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada MK

| Kode Baku (Alias) | Rumusan CPL (verbatim Dokumen 003) |
|:---:|---|
| **CPL-05** (`P1`) | Menguasai konsep dasar sains, matematika terapan (kalkulus, aljabar linear, statistika, matematika diskrit, logika) sebagai fondasi pemecahan masalah rekayasa sistem informasi dan komputasi cerdas yang kompleks. |
| **CPL-07** (`P3`) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. |
| **CPL-02** (`KU1`) | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam menganalisis permasalahan komputasi serta mengkaji implikasi pengembangan atau implementasi iptek sesuai kaidah, tata cara, dan etika ilmiah. |

Bobot kontribusi MK terhadap ketiga CPL tersebut: **3 SKS** dari total MK pembina masing-masing CPL.

### D. Capaian Pembelajaran Mata Kuliah (CPMK)

| Kode | Rumusan CPMK (Format ABCD) | Bloom | CPL |
|:---:|---|:---:|:---:|
| **CPMK-1** | Mahasiswa (*A*) mampu **menerapkan** representasi data biner, heksadesimal, *floating point* IEEE 754, dan siklus eksekusi instruksi Von Neumann (*B*) pada arsitektur prosesor (*C*) secara tepat dan akurat (*D*). | **C3** | `CPL-05` (`P1`), `CPL-07` (`P3`) |
| **CPMK-2** | Mahasiswa (*A*) mampu **menganalisis** rancangan rangkaian logika kombinasional dan sekuensial (*B*) menggunakan gerbang logika biner dan flip-flop (*C*) sebagai dasar operasi *Arithmetic Logic Unit* (ALU) (*D*). | **C4** | `CPL-05` (`P1`), `CPL-02` (`KU1`) |
| **CPMK-3** | Mahasiswa (*A*) mampu **membandingkan** karakteristik arsitektur prosesor CISC (x86_64) vs RISC (ARM64/RISC-V), hierarki memori cache L1/L2/L3, dan akselerator komputasi GPU/NPU (*B*) dalam skenario beban kerja komputasi nyata (*C*) secara kritis (*D*). | **C4** | `CPL-07` (`P3`), `CPL-02` (`KU1`) |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengevaluasi** mekanisme bus sistem, interupsi I/O, abstraksi virtualisasi *hardware* (Hypervisor), dan organisasi server *data center* (*B*) untuk mendukung infrastruktur *cloud* modern (*C*) secara komprehensif (*D*). | **C5** | `CPL-07` (`P3`), `CPL-02` (`KU1`) |

### E. Sub-Capaian Pembelajaran Mata Kuliah (Sub-CPMK)

| Kode | Kompetensi Spesifik | CPMK | Bloom |
|---:|---|:--:|:--:|
| **Sub-CPMK-1.1** | Mengonversi representasi bilangan biner, heksadesimal, dan *floating point* IEEE 754. | CPMK-1 | **C3** |
| **Sub-CPMK-1.2** | Menjelaskan siklus eksekusi instruksi *Fetch-Decode-Execute* pada arsitektur Von Neumann. | CPMK-1 | **C3** |
| **Sub-CPMK-2.1** | Menganalisis gerbang logika biner dan rangkaian kombinasional sebagai dasar ALU. | CPMK-2 | **C4** |
| **Sub-CPMK-2.2** | Menganalisis flip-flop dan rangkaian logika sekuensial dasar. | CPMK-2 | **C4** |
| **Sub-CPMK-3.1** | Membandingkan karakteristik arsitektur prosesor CISC (x86_64) dan RISC (ARM64/RISC-V). | CPMK-3 | **C4** |
| **Sub-CPMK-3.2** | Menganalisis hierarki memori dan cache (L1/L2/L3) serta akselerator GPU/NPU. | CPMK-3 | **C4** |
| **Sub-CPMK-4.1** | Mengevaluasi mekanisme bus sistem dan interupsi I/O. | CPMK-4 | **C5** |
| **Sub-CPMK-4.2** | Mengevaluasi abstraksi virtualisasi *hardware* (Hypervisor) dan organisasi server *data center* untuk *cloud*. | CPMK-4 | **C5** |

### F. Matriks Korelasi CPL ↔ CPMK dan Bobot Penilaian

| CPMK | CPL | Pekan | Tugas 1 (20%) | UTS (30%) | Tugas 2 (20%) | UAS (30%) | Bobot CPMK |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CPMK-1 | `CPL-05` (`P1`), `CPL-07` (`P3`) | 1–3, 8 | **50%** | **50%** | — | — | 100% |
| CPMK-2 | `CPL-05` (`P1`), `CPL-02` (`KU1`) | 4–5, 8, 16 | **50%** | **40%** | — | **10%** | 100% |
| CPMK-3 | `CPL-07` (`P3`), `CPL-02` (`KU1`) | 6–7, 8, 11, 16 | — | **10%** | **40%** | **50%** | 100% |
| CPMK-4 | `CPL-07` (`P3`), `CPL-02` (`KU1`) | 9–12, 16 | — | — | **60%** | **40%** | 100% |
| **Total instrumen** | | | **20%** | **30%** | **20%** | **30%** | **100%** |

*Cara baca:* Skor CPMK-1 = 0,50 × Tugas 1 + 0,50 × UTS. Skor CPMK-2 = 0,50 × Tugas 1 + 0,40 × UTS + 0,10 × UAS. Skor CPMK-3 = 0,10 × UTS + 0,40 × Tugas 2 + 0,50 × UAS. Skor CPMK-4 = 0,60 × Tugas 2 + 0,40 × UAS. Nilai Akhir = 0,20×T1 + 0,30×UTS + 0,20×T2 + 0,30×UAS.

**Kontribusi terhadap CPL:** MK ini membina tiga CPL sekaligus. Bobot distribusi internal: `CPL-05` (`P1`) 25%, `CPL-07` (`P3`) 45%, `CPL-02` (`KU1`) 30% (ditetapkan berdasarkan dominasi indikator tiap CPMK).

### G. Deskripsi Singkat Mata Kuliah

Mata kuliah ini membuka "kotak hitam" mesin komputasi: dari bit hingga *data center*. Pembahasan dimulai dari representasi data pada level mesin — biner, heksadesimal, komplemen dua, dan standar *floating point* IEEE 754 — lalu bergerak ke arsitektur Von Neumann dan siklus *Fetch-Decode-Execute* yang menjadi kontrak dasar antara perangkat keras dan perangkat lunak. Bagian kedua menurunkan prosesor dari bawah: gerbang logika, aljabar Boolean terapan, rangkaian kombinasional (penjumlah, multiplekser, dekoder) sebagai bahan dasar ALU, hingga rangkaian sekuensial berbasis flip-flop dan register. Bagian ketiga membandingkan pilihan desain nyata: CISC (x86_64) versus RISC (ARM64/RISC-V), hierarki memori SRAM–DRAM–cache L1/L2/L3 dengan analisis lokalitas, serta peran akselerator GPU/NPU pada beban kerja kecerdasan artifisial. Bagian akhir mengevaluasi tulang punggung infrastruktur: bus sistem, mekanisme interupsi dan DMA, *hypervisor* Tipe 1 dan Tipe 2, serta organisasi server, rak, pendinginan, dan konsumsi daya di *data center* yang menopang layanan *cloud*. Seluruh pembahasan berada pada **level abstraksi perangkat keras mesin**; logika matematika formal diserahkan ke `STI-204` dan abstraksi sistem operasi ke `STI-310`. MK ini menjadi fondasi langsung bagi `STI-312` (Jaringan Komputer), `STI-310` (Sistem Operasi), dan `STI-417` (Komputasi Awan).

### H. Bahan Kajian (Body of Knowledge)

| Kode | Nomenklatur BoK | Cakupan dalam MK |
|:---:|---|---|
| `BK-IS03` | *IT Infrastructure* | Organisasi server, *data center*, virtualisasi, dasar *cloud infrastructure* |
| `BK-IT01` | *IT Fundamentals* | Representasi data, system unit, periferal, konsep dasar I/O |
| `BK-IT05` | *Computer Architecture* | Von Neumann, ALU, register, siklus instruksi, bus, hierarki memori, CISC/RISC |

**Pokok bahasan:** (1) sistem bilangan & representasi data; (2) IEEE 754 & aritmetika *floating point*; (3) arsitektur Von Neumann & siklus instruksi; (4) gerbang logika & aljabar Boolean terapan; (5) rangkaian kombinasional & ALU; (6) flip-flop & rangkaian sekuensial; (7) CISC vs RISC & *instruction set*; (8) hierarki memori & cache; (9) evaluasi tengah semester; (10) bus sistem & interupsi I/O; (11) virtualisasi & *hypervisor*; (12) organisasi *data center*; (13) studi kasus beban kerja & pemilihan arsitektur; (14) proyek terapan & presentasi; (15) presentasi final; (16) evaluasi akhir semester.

### I. Pustaka

**Pustaka Utama**

| No | Referensi |
|:---:|---|
| [1] | Patterson, D.A. & Hennessy, J.L. (2020). *Computer Organization and Design: The Hardware/Software Interface*, RISC-V Edition, 2nd ed. Morgan Kaufmann. ISBN 978-0-12-820331-6. |
| [2] | Stallings, W. (2022). *Computer Organization and Architecture: Designing for Performance*, 11th ed. Pearson. ISBN 978-0-13-518200-5. |
| [3] | Tanenbaum, A.S. & Austin, T. (2013). *Structured Computer Organization*, 6th ed. Pearson. ISBN 978-0-13-291652-3. |

**Pustaka Pendukung**

| No | Referensi |
|:---:|---|
| [4] | Harris, S.L. & Harris, D.M. (2021). *Digital Design and Computer Architecture*, RISC-V Edition, 2nd ed. Morgan Kaufmann. ISBN 978-0-12-820064-3. |
| [5] | Null, L. & Lobur, J. (2018). *The Essentials of Computer Organization and Architecture*, 5th ed. Jones & Bartlett. ISBN 978-1-284-12303-6. |
| [6] | IEEE (2019). *IEEE Standard for Floating-Point Arithmetic (IEEE 754-2019)*. IEEE. |
| [7] | Silberschatz, A., Galvin, P.B. & Gagne, G. (2018). *Operating System Concepts*, 10th ed., Bab 16–17 (Virtual Machines & Cloud). Wiley. ISBN 978-1-118-06333-0. |
| [8] | Hennessy, J.L. & Patterson, D.A. (2019). *Computer Architecture: A Quantitative Approach*, 6th ed. Morgan Kaufmann. ISBN 978-0-12-811905-1. |

---

## HALAMAN 3–4 — MATRIKS RENCANA PEMBELAJARAN 16 PEKAN (LANDSCAPE)

**Identitas waktu:** 3 SKS Teori → TM = 150 menit/pekan; PT = 180 menit/pekan; BM = 180 menit/pekan.

| Mg | Sub-CPMK (Kemampuan Akhir) | Indikator Penilaian | Kriteria & Teknik | Luring (TM/PT/BM) | Daring | Materi Pembelajaran [Pustaka] | Bobot |
|:--:|---|---|---|---|---|---|:--:|
| 1 | Orientasi MK & kontrak belajar (fondasi CPMK-1) | Ketepatan menjelaskan ruang lingkup, capaian, dan skema asesmen | Kriteria: kelengkapan jawaban; Teknik: tanya-jawab lisan | Kuliah interaktif; TM 150′ / PT 180′ / BM 180′ | Forum perkenalan di LMS; unduh kontrak belajar | Ruang lingkup arsitektur komputer, peta CPL–CPMK, aturan akademik & etika AI [1] Bab 1 | — |
| 2 | **Sub-CPMK-1.1** — Mengonversi bilangan biner, heksadesimal, dan *floating point* IEEE 754 | 1.1.1 Ketepatan konversi antar-basis; 1.1.2 Ketepatan penyusunan format IEEE 754 *single precision* | Kriteria: ketepatan hasil konversi; Teknik: kuis formatif, latihan terbimbing | Kuliah & latihan; TM 150′ / PT 180′ / BM 180′ | Kuis LMS (formatif, non-graded) | Sistem bilangan posisional, komplemen dua, *sign–exponent–mantissa* [1] Bab 3; [6] | — |
| 3 | **Sub-CPMK-1.2** — Menjelaskan siklus *Fetch-Decode-Execute* pada arsitektur Von Neumann | 1.2.1 Ketepatan urutan siklus; 1.2.2 Ketepatan peran PC, IR, MAR, MDR | Kriteria: ketepatan urutan & fungsi register; Teknik: latihan pemetaan siklus | Ceramah interaktif + latihan; TM 150′ / PT 180′ / BM 180′ | Simulasi *single-cycle datapath* daring | Model Von Neumann, unit kontrol, register, *datapath* [2] Bab 1–3; [3] Bab 1–2 | — |
| **4** | **Sub-CPMK-2.1** — Menganalisis gerbang logika biner dan rangkaian kombinasional sebagai dasar ALU | 2.1.1 Ketepatan tabel kebenaran; 2.1.2 Ketepatan penyederhanaan dan perancangan rangkaian | Kriteria: rubrik analitik (4 dimensi); Teknik: **Tugas 1** — kuis + problem solving rangkaian | Case-based learning; TM 150′ / PT 180′ / BM 180′ | Submit Tugas 1 via LMS (PDF) | Gerbang AND/OR/NOT/NAND/NOR/XOR, aljabar Boolean, K-map, *adder*, MUX, dekoder [4] Bab 2–3; [2] Bab 10 | **20%** |
| 5 | **Sub-CPMK-2.2** — Menganalisis flip-flop dan rangkaian logika sekuensial dasar | 2.2.1 Ketepatan analisis SR/JK/D flip-flop; 2.2.2 Ketepatan diagram waktu dan *state table* | Kriteria: ketepatan analisis; Teknik: latihan terstruktur | Ceramah & latihan; TM 150′ / PT 180′ / BM 180′ | Lembar kerja *timing diagram* di LMS | Latch vs flip-flop, *clocking*, register, pencacah (*counter*) [4] Bab 4; [5] Bab 3 | — |
| 6 | **Sub-CPMK-3.1** — Membandingkan arsitektur CISC (x86_64) dan RISC (ARM64/RISC-V) | 3.1.1 Ketepatan komparasi filosofi desain; 3.1.2 Ketepatan analisis konsekuensi performa | Kriteria: kedalaman komparasi; Teknik: diskusi kelompok & presentasi singkat | Diskusi kelompok & *gallery walk*; TM 150′ / PT 180′ / BM 180′ | Peer feedback di forum LMS | *Instruction set architecture*, *addressing mode*, x86_64 vs ARM64 vs RISC-V [1] Bab 2; [8] Bab 1 | — |
| 7 | **Sub-CPMK-3.2** — Menganalisis hierarki memori, cache L1/L2/L3, dan akselerator GPU/NPU | 3.2.1 Ketepatan analisis lokalitas; 3.2.2 Ketepatan hitung *hit/miss ratio* dan AMAT | Kriteria: ketajaman analisis kuantitatif; Teknik: latihan perhitungan & studi kasus | Ceramah & latihan kuantitatif; TM 150′ / PT 180′ / BM 180′ | Latihan AMAT interaktif di LMS | SRAM/DRAM, lokalitas temporal–spasial, *mapping* cache, AMAT, arsitektur GPU/NPU [1] Bab 5; [8] Bab 2 | — |
| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | Ketuntasan CPMK-1, CPMK-2, CPMK-3 (tahap awal) | Kriteria: kunci jawaban terstandar; Teknik: ujian tertulis terjadwal | Ujian; TM 150′ | — | Materi pekan 1–7 | **30%** |
| 9 | **Sub-CPMK-4.1** — Mengevaluasi mekanisme bus sistem dan interupsi I/O | 4.1.1 Ketepatan analisis arbitrase bus; 4.1.2 Ketepatan pembedaan *polling*, interupsi, dan DMA | Kriteria: ketepatan evaluasi; Teknik: studi kasus terstruktur | Case method; TM 150′ / PT 180′ / BM 180′ | Analisis kasus I/O di LMS | Bus data/alamat/kontrol, arbitrase, interupsi bertingkat, DMA, PCIe [2] Bab 3 & 7; [3] Bab 3 | — |
| 10 | **Sub-CPMK-4.2** — Mengevaluasi virtualisasi *hardware* (*hypervisor*) dan organisasi server *data center* | 4.2.1 Ketepatan pembedaan *hypervisor* Tipe 1 vs Tipe 2; 4.2.2 Ketepatan evaluasi trade-off *data center* | Kriteria: kedalaman evaluasi; Teknik: studi kasus & diskusi | Ceramah & studi kasus; TM 150′ / PT 180′ / BM 180′ | Diskusi studi kasus *cloud* di LMS | Virtualisasi CPU/memori/I/O, *hypervisor*, kontainer vs VM, rak, PUE, redundansi [7] Bab 16–17; [2] Bab 20 | — |
| 11 | Penguatan CPMK-3 & CPMK-4 — studi kasus beban kerja & pemilihan arsitektur | 4.3.1 Ketepatan *profiling* beban kerja; 4.3.2 Ketepatan justifikasi pemilihan platform | Kriteria: ketepatan justifikasi; Teknik: kerja kelompok terpandu | PjBL / Case Method; TM 150′ / PT 180′ / BM 180′ | Konsultasi asinkron | Studi kasus: *inference* AI, *web serving*, basis data, HPC [8] Bab 1 & 6 | — |
| **12** | **Sub-CPMK-4.1 & 4.2 (integrasi)** — Proyek terapan lanjut & presentasi antara | 4.4.1 Kelayakan rancangan; 4.4.2 Kejelasan argumentasi teknis | Kriteria: rubrik analitik (4 dimensi); Teknik: **Tugas 2** — laporan proyek + presentasi | PjBL / Presentasi; TM 150′ / PT 180′ / BM 180′ | Submit Tugas 2 via LMS | Integrasi arsitektur–virtualisasi–*data center* pada kasus nyata [2]; [7] | **20%** |
| 13 | Penyempurnaan proyek berdasarkan umpan balik | 4.4.3 Ketepatan revisi; 4.4.4 Kualitas dokumentasi | Kriteria: checklist revisi; Teknik: konsultasi klinis | PjBL / Konsultasi; TM 150′ / PT 180′ / BM 180′ | Konsultasi asinkron | Seluruh materi CPMK-3 & CPMK-4 | — |
| 14 | Review & konsolidasi seluruh CPMK | Ketepatan identifikasi kesenjangan pemahaman | Kriteria: kelengkapan peta konsep; Teknik: review bersama | Diskusi / Konsultasi; TM 150′ / PT 180′ / BM 180′ | Pembahasan soal terpilih di LMS | Rekapitulasi pekan 1–13 | — |
| 15 | Presentasi final / demonstrasi hasil | 4.4.5 Kualitas komunikasi teknis; 4.4.6 Penguasaan saat tanya jawab | Kriteria: rubrik presentasi; Teknik: presentasi tim | Presentasi & pleno; TM 150′ / PT 180′ / BM 180′ | Unggah slide & rekaman | Seluruh materi CPMK-1 s.d. CPMK-4 | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS)** | Ketuntasan komprehensif CPMK-1 s.d. CPMK-4 | Kriteria: kunci jawaban & rubrik esai; Teknik: ujian komprehensif | Ujian; TM 150′ | — | Materi pekan 1–15 | **30%** |
| | **TOTAL BOBOT PENILAIAN** | | | | | | **100%** |

**Keterangan waktu:** TM = tatap muka (1 SKS = 50 menit/pekan); PT = penugasan terstruktur (1 SKS = 60 menit/pekan); BM = belajar mandiri (1 SKS = 60 menit/pekan). Mata kuliah ini tidak memiliki komponen praktikum (P = 0); latihan rangkaian dilakukan secara simulasi/logika di atas kertas dan perangkat lunak simulasi daring.

---

## HALAMAN 5 — LAMPIRAN 1: NASKAH TUGAS 1 + RUBRIK (PORTRAIT)

### A. Naskah Tugas 1 — Kuis & Problem Solving "Dari Bit ke ALU"

**Pekan:** 4 | **Bobot:** 20% | **CPMK:** CPMK-1 & CPMK-2 | **Bentuk:** Individu | **Durasi:** 150 menit

**Instruksi:**

1. Konversikan bilangan berikut dan tuliskan langkahnya: (a) $2451_{10}$ → biner dan heksadesimal; (b) $\text{0xBE3A}$ → desimal; (c) $-37_{10}$ → komplemen dua 8-bit.
2. Nyatakan $-12{,}375_{10}$ dalam format IEEE 754 *single precision* (32-bit). Tuliskan bagian *sign*, *exponent* (dengan bias 127), dan *mantissa*, lalu nyatakan kembali dalam heksadesimal.
3. Susun tabel kebenaran untuk fungsi $F(A,B,C) = \Sigma m(1,3,5,7)$ dan sederhanakan dengan K-map. Gambarkan rangkaian hasil penyederhanaan.
4. Rancang **penjumlah penuh (*full adder*)** dari dua *half adder* dan satu gerbang OR. Tuliskan tabel kebenaran dan persamaan *Sum* serta *Carry*.
5. Jelaskan dengan diagram alur bagaimana instruksi `ADD R1, R2, R3` melewati siklus *Fetch-Decode-Execute* pada arsitektur Von Neumann, sebutkan peran PC, IR, MAR, dan MDR.

**Ketentuan:** dikerjakan individual; seluruh langkah wajib ditulis; jawaban akhir tanpa langkah dinilai maksimal 40% poin butir.

**Deliverable:** berkas PDF jawaban bertahap + gambar rangkaian.

### B. Rubrik Penilaian Tugas 1 (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Ketepatan representasi data (25%)** | Seluruh konversi dan format IEEE 754 tepat; langkah dan bias ditulis eksplisit | Tepat dengan 1 kekeliruan minor pada *mantissa* | Ada kesalahan konversi pada 2 butir | Tidak menguasai sistem bilangan |
| **2. Ketepatan analisis rangkaian logika (30%)** | Tabel kebenaran, K-map, dan persamaan benar; rangkaian ekuivalen secara fungsional | Persamaan benar; gambar rangkaian kurang rapi | Penyederhanaan benar sebagian | Tabel kebenaran salah |
| **3. Pemahaman siklus instruksi (30%)** | Seluruh register dan urutan siklus tepat; diagram alur jelas dan konsisten dengan datapath | Urutan benar, 1–2 peran register kurang tepat | Urutan benar sebagian; peran register tertukar | Tidak memahami siklus instruksi |
| **4. Kerapian & tata tulis teknis (15%)** | Notasi biner/heksadesimal konsisten; gambar rapi dan berlabel | Notasi konsisten; gambar kurang berlabel | Notasi tidak konsisten | Jawaban tidak terbaca |

---

## HALAMAN 6 — LAMPIRAN 2: NASKAH UTS + RUBRIK (PORTRAIT)

### A. Naskah UTS — Ujian Tertulis Representasi Data, Logika Digital, dan Arsitektur

**Pekan:** 8 | **Bobot:** 30% | **CPMK:** CPMK-1, CPMK-2, CPMK-3 | **Bentuk:** Individu, *closed book* | **Durasi:** 150 menit

**Struktur soal:**

| Bagian | Bentuk | Jumlah | Poin | Cakupan |
|:--:|---|:--:|:--:|---|
| I | Uraian singkat (representasi data & IEEE 754) | 3 | 20 | CPMK-1 |
| II | Uraian terstruktur (siklus instruksi & *datapath*) | 2 | 15 | CPMK-1 |
| III | Uraian analitis (rangkaian kombinasional & sekuensial) | 3 | 30 | CPMK-2 |
| IV | Studi kasus komparatif (CISC vs RISC, hierarki memori) | 2 | 35 | CPMK-3 |

**Contoh butir Bagian IV:**
> Sebuah tim engineering harus memilih prosesor untuk dua beban kerja: (i) server basis data transaksional dengan banyak operasi baca/tulis memori dan instruksi bercabang kompleks; (ii) perangkat *edge* bertenaga baterai yang menjalankan model *inference* kecil.
> (a) Bandingkan kesesuaian CISC x86_64 dan RISC ARM64 untuk masing-masing beban kerja, dengan minimal tiga argumen teknis per pilihan. (20 poin)
> (b) Untuk beban kerja (i), cache L1 sebesar 32 KB memiliki *hit rate* 92% dan *hit time* 1 ns, sedangkan memori utama berakses 60 ns. Hitung AMAT dan jelaskan dampaknya terhadap keputusan desain. (15 poin)

**Ketentuan:** *closed book*; kalkulator ilmiah tidak diperlukan; seluruh langkah perhitungan wajib ditulis.

### B. Rubrik Penilaian UTS (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Penguasaan konsep arsitektur (25%)** | Definisi, register, dan mekanisme dijelaskan tepat dan saling terkait | Tepat dengan 1–2 kekeliruan minor | Beberapa kekeliruan konseptual | Salah memahami konsep inti |
| **2. Ketepatan analisis rangkaian (25%)** | Analisis kombinasional dan sekuensial tepat, *timing* konsisten | Sebagian besar tepat, satu kesalahan kecil | Analisis dangkal atau ada kesalahan fungsional | Tidak mampu menganalisis |
| **3. Kualitas analisis komparatif (30%)** | Komparasi multidimensi (ISA, performa, daya, biaya) dengan *trade-off* eksplisit | Komparasi jelas, dua dimensi utama tercakup | Komparasi dangkal, satu dimensi | Tidak ada komparasi |
| **4. Ketepatan kuantitatif & kelengkapan (20%)** | Perhitungan AMAT/*hit ratio* benar dengan interpretasi | Perhitungan benar, interpretasi ringkas | Ada kesalahan hitung | Tidak menjawab perhitungan |

---

## HALAMAN 7 — LAMPIRAN 3: NASKAH TUGAS 2 + RUBRIK (PORTRAIT)

### A. Naskah Tugas 2 — Proyek Terapan "Rancangan Platform Komputasi untuk Beban Kerja Nyata"

**Pekan:** 12 | **Bobot:** 20% | **CPMK:** CPMK-3 & CPMK-4 | **Bentuk:** Kelompok 3–4 orang | **Durasi:** 3 pekan

**Instruksi:**

1. Pilih **satu** skenario beban kerja nyata:
   - **T1:** Layanan *web* kampus dengan 5.000 pengguna bersamaan pada jam sibuk.
   - **T2:** *Inference* model visi komputer untuk 200 kamera pemantau kampus.
   - **T3:** Klaster basis data akademik dengan 200 GB data dan kebutuhan ketersediaan 99,9%.
2. Lakukan **karakterisasi beban kerja**: sifat komputasi (CPU-*bound* / memori-*bound* / I/O-*bound*), pola akses memori, dan kebutuhan paralelisme.
3. Rancang **konfigurasi platform**: pilihan arsitektur prosesor (x86_64 / ARM64 / akselerator GPU-NPU), kapasitas dan hierarki memori, subsistem I/O, serta strategi virtualisasi (VM vs kontainer).
4. Hitung **estimasi kuantitatif** minimal untuk: kebutuhan inti CPU, kebutuhan memori, dan perkiraan AMAT atau *throughput*.
5. Evaluasi **organisasi *data center***: jumlah rak, redundansi daya, perkiraan PUE, dan skenario kegagalan.
6. Analisis **trade-off** biaya–performa–daya, lalu berikan rekomendasi akhir dengan justifikasi.
7. Format: laporan 12–16 halaman, sitasi IEEE minimal 8 rujukan (≥ 3 buku/standar), font 11 pt, spasi 1,15.
8. Wajib menyertakan **Deklarasi Transparansi AI** dan pembagian peran tim.

**Deliverable:** laporan PDF + diagram arsitektur + slide ringkas 7 halaman.

### B. Rubrik Penilaian Tugas 2 (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Karakterisasi beban kerja (25%)** | Profil beban kerja dikuantifikasi (CPU/memori/I/O) dengan asumsi eksplisit dan realistis | Profil memadai, asumsi sebagian tersurat | Profil generik, asumsi tidak jelas | Tidak ada karakterisasi |
| **2. Kelayakan rancangan platform (30%)** | Rancangan konsisten dengan profil beban; pilihan arsitektur dan virtualisasi terjustifikasi teknis | Rancangan layak, justifikasi memadai | Rancangan generik, justifikasi lemah | Rancangan tidak dapat diimplementasikan |
| **3. Ketepatan estimasi kuantitatif (25%)** | Seluruh estimasi (inti, memori, AMAT/*throughput*) dihitung benar dan diinterpretasikan | Estimasi benar, interpretasi ringkas | Ada kesalahan hitung atau estimasi tidak lengkap | Tidak ada estimasi |
| **4. Evaluasi *data center* & trade-off (20%)** | Analisis daya, PUE, redundansi, dan trade-off biaya–performa kritis dan terukur | Analisis memadai, trade-off disebut | Analisis umum | Mengabaikan aspek *data center* |

---

## HALAMAN 8 — LAMPIRAN 4: NASKAH UAS + RUBRIK (PORTRAIT)

### A. Naskah UAS — Evaluasi Komprehensif Arsitektur dan Infrastruktur

**Pekan:** 16 | **Bobot:** 30% | **CPMK:** CPMK-1, CPMK-2, CPMK-3, CPMK-4 | **Bentuk:** Individu | **Durasi:** 150 menit

**Struktur soal:**

| Bagian | Bentuk | Poin | Cakupan |
|:--:|---|:--:|---|
| I | Uraian terpadu: representasi data, siklus instruksi, dan ALU | 30 | CPMK-1, CPMK-2 |
| II | Analisis komparatif arsitektur dan hierarki memori | 25 | CPMK-3 |
| III | Evaluasi sistem I/O, virtualisasi, dan *data center* | 25 | CPMK-4 |
| IV | Perancangan solusi terbuka: pemilihan platform terintegrasi | 20 | CPMK-3, CPMK-4 |

**Contoh butir Bagian III:**
> Sebuah institusi menjalankan 40 mesin virtual di atas 5 server fisik. Pemanfaatan CPU rata-rata 18%, memori 62%, dan *storage* 71%. Rencana perluasan menambah 15 VM baru, sementara anggaran pengadaan terbatas pada 2 server.
> (a) Evaluasi apakah *overcommitment* memori layak dilakukan, dan sebutkan risiko teknisnya. (10 poin)
> (b) Bandingkan *hypervisor* Tipe 1 dan Tipe 2 untuk kebutuhan ini, serta pertimbangkan alternatif kontainer. (8 poin)
> (c) Usulkan strategi konsolidasi dan ukur dampaknya terhadap PUE serta biaya daya. (7 poin)

### B. Rubrik Penilaian UAS (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Penguasaan konsep komprehensif (25%)** | Mengaitkan representasi data, ALU, ISA, memori, I/O, dan virtualisasi secara utuh | Konsep benar, keterkaitan sebagian | Konsep terpisah-pisah | Salah konsep mendasar |
| **2. Ketepatan analisis teknis (30%)** | Analisis kuantitatif tepat dengan interpretasi implikasi desain | Analisis tepat, interpretasi ringkas | Analisis umum | Analisis tidak berdasar |
| **3. Kedalaman evaluasi & *trade-off* (30%)** | Evaluasi kritis multi-kriteria, mempertimbangkan biaya, daya, performa, risiko | Evaluasi jelas, dua kriteria utama | Evaluasi dangkal | Tidak ada evaluasi |
| **4. Struktur & komunikasi teknis (15%)** | Uraian runtut, terminologi tepat, kesimpulan eksplisit | Uraian jelas, kesimpulan ada | Uraian kurang runtut | Tidak terstruktur |

---

## HALAMAN 9 — LEMBAR VALIDASI DAN PENGESAHAN (PORTRAIT)

| Memvalidasi,<br>Unit Penjaminan Mutu FSTI | Malang, 07 November 2026<br>Dosen Pengampu Mata Kuliah |
|:---:|:---:|
| ..........................<br>NUPTK. .......................... | ..........................<br>NIDN/NUPTK. .......................... |

<br>

| Mengesahkan,<br>Ketua Program Studi S1 Sistem dan Teknologi Informasi |
|:---:|
| ..........................<br>NUPTK. .......................... |

---

## LAMPIRAN TEKNIS — KESESUAIAN DENGAN TEMPLATE MASTER RPS FSTI UWG

### A. Pemetaan 18 Tag Nilai Tunggal (`{{...}}`)

| Tag | Nilai Terisi |
|---|---|
| `{{namamk}}` | Arsitektur dan Organisasi Sistem Teknologi Informasi |
| `{{kodemk}}` | STI-103 |
| `{{rumpunmk}}` | Infrastruktur & Arsitektur Komputer (Core STI) |
| `{{skst}}` | 3 |
| `{{sksp}}` | 0 |
| `{{sms}}` | 1 (Gasal) |
| `{{tglsusun}}` | 07 November 2026 |
| `{{pengembangrps}}` | Tim Pengembang RPS SISTEKIN |
| `{{koordinatormk}}` | Koordinator RMK Infrastruktur & Arsitektur Komputer |
| `{{ketuaprodi}}` | Ketua Prodi SISTEKIN FSTI |
| `{{kodeprodi}}` | B4.5.2.RPS-STI103 |
| `{{prodi}}` | Sistem dan Teknologi Informasi |
| `{{namadosen}}` | Tim Pengampu Rumpun Infrastruktur & Arsitektur Komputer |
| `{{nuptk}}` | .......................... |
| `{{deskripsimk}}` | Lihat Bagian G Halaman 2 |
| `{{bahankajian}}` | BK-IS03, BK-IT01, BK-IT05 — lihat Bagian H Halaman 2 |
| `{{dosenpengampu}}` | Tim Pengampu Rumpun Infrastruktur & Arsitektur Komputer (Core STI) |
| `{{mkprasyarat}}` | — |

### B. Pemetaan 25 Tag Blok Isi (`[...]`)

| Tag | Lokasi | Sumber Isi |
|---|---|---|
| `[nocpl]`, `[cpl]` | Hal 2 | Bagian C (3 baris CPL: CPL-05 (P1), CPL-07 (P3), CPL-02 (KU1)) |
| `[nocpmk]`, `[cpmk]` | Hal 2 | Bagian D (4 CPMK) |
| `[nosubcpmk]`, `[subcpmk]` | Hal 2 | Bagian E (8 Sub-CPMK) |
| `[tabelkolerasi]` | Hal 2 | Bagian F (matriks CPL×CPMK, total 100%) |
| `[pustakautama]` | Hal 2 | Bagian I — 3 pustaka utama |
| `[pustakapendukung]` | Hal 2 | Bagian I — 5 pustaka pendukung |
| `[mingguke]` … `[bobot_nilai]` | Hal 3–4 | Kolom 1–8 tabel 16 pekan |
| `[penugasan1]`, `[rubriktugas1]` | Hal 5 | Lampiran 1 |
| `[soaluts]`, `[rubrikuts]` | Hal 6 | Lampiran 2 |
| `[tugas2]`, `[rubriktugas2]` | Hal 7 | Lampiran 3 |
| `[soaluas]`, `[rubrikuas]` | Hal 8 | Lampiran 4 |

### C. Pernyataan Kepatuhan Skema Asesmen

| Komponen | Pekan | Bobot | Target CPMK | Status |
|:---:|:---:|:---:|:---:|:---:|
| Tugas 1 | 4 | 20% | CPMK-1 & CPMK-2 | Sesuai |
| UTS | 8 | 30% | CPMK-1, CPMK-2, CPMK-3 | Sesuai |
| Tugas 2 | 12 | 20% | CPMK-3 & CPMK-4 | Sesuai |
| UAS | 16 | 30% | CPMK-1 s.d. CPMK-4 (komprehensif) | Sesuai |
| **Total** | | **100%** | | **Lulus** |

### D. Kepatuhan Boundary Guardrails (Dokumen 043)

| Kategori | Isi |
|---|---|
| **In-Scope (diajarkan)** | Arsitektur Von Neumann, ALU, register, siklus *Fetch-Decode-Execute*, hierarki memori (SRAM, DRAM, cache), bus I/O, set instruksi *assembly* dasar |
| **Out-of-Scope (tidak diajarkan)** | Logika predikat matematika murni, aljabar relasional basis data, konfigurasi *routing* jaringan komputer |
| **Handoff Anchor** | Menyerahkan logika matematika diskrit ke `STI-204`; abstraksi sistem operasi ke `STI-310`; konfigurasi jaringan ke `STI-312` |

---

*Dokumen ini disusun dari Dokumen 005, 007, 043, 003, 008, dan 018. Rujukan pustaka merupakan usulan standar bidang ilmu dan tetap terbuka untuk validasi KBK/GPM. Dokumen pendamping: `057_2_SAP_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`, `057_3_OUTLINE_MODUL_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`, `057_4_RENCANA_EVALUASI_ASESMEN_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`, `057_5_RUBRIK_PENILAIAN_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`.*
