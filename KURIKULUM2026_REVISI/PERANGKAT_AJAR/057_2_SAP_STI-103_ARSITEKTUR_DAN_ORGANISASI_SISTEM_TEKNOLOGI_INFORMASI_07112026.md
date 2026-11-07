# SATUAN ACARA PERKULIAHAN (SAP)

## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI
### *Information Technology Systems Architecture and Organization*

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Semester:** 1 (Gasal) | **Bobot:** 3 SKS Teori | **Pertemuan:** 16 pekan
> **Dokumen induk:** `057_1_RPS_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`
> **Tanggal:** 07 November 2026

---

## 1. IDENTITAS DAN KEDUDUKAN DOKUMEN

| Atribut | Keterangan |
|---|---|
| Nama MK / Kode | Arsitektur dan Organisasi Sistem Teknologi Informasi / `STI-103` |
| Rumpun MK | Infrastruktur & Arsitektur Komputer (Core STI) |
| Prasyarat | — |
| Dosen Pengampu | Tim Pengampu Rumpun Infrastruktur & Arsitektur Komputer |
| Hari / Jam | Sesuai jadwal akademik fakultas |
| Ruang | Kelas teori (kapasitas ≥ 40 mahasiswa) |
| Media utama | LCD proyektor, papan tulis, LMS (Edlink/Moodle), perangkat lunak simulasi logika (Logisim Evolution / Digital) |
| Alokasi waktu | TM 150′/pekan; PT 180′/pekan; BM 180′/pekan |
| Fungsi dokumen | Menjabarkan RPS menjadi rencana operasional tiap pertemuan (kegiatan, media, waktu, penilaian) |

**Kedudukan dalam rantai dokumen:** RPS (055_1) → **SAP (055_2)** → Buku Modul (055_3) → Rencana Evaluasi (055_4) → Rubrik (055_5). SAP tidak boleh menyimpang dari RPS; seluruh Sub-CPMK, materi, dan titik asesmen mengikuti RPS dan Dokumen 043.

---

## 2. CAPAIAN DAN INDIKATOR RINGKAS

| Kode | Rumusan | Bloom | Pekan Pencapaian | Instrumen Ukur |
|:---:|---|:---:|:---:|---|
| CPMK-1 | Menerapkan representasi data biner/hex/IEEE 754 dan siklus eksekusi Von Neumann | C3 | 2–3, 8 | Tugas 1, UTS |
| CPMK-2 | Menganalisis rangkaian logika kombinasional & sekuensial sebagai dasar ALU | C4 | 4–5, 8, 16 | Tugas 1, UTS, UAS |
| CPMK-3 | Membandingkan CISC vs RISC, hierarki memori cache, dan akselerator GPU/NPU | C4 | 6–7, 8, 12, 16 | UTS, Tugas 2, UAS |
| CPMK-4 | Mengevaluasi bus sistem, interupsi I/O, virtualisasi, dan organisasi *data center* | C5 | 9–12, 16 | Tugas 2, UAS |

**Indikator kinerja kunci (IKK):**

1. ≥ 80% mahasiswa mampu mengonversi bilangan antar-basis dan menyusun format IEEE 754 secara tepat.
2. ≥ 75% mahasiswa mampu menyederhanakan fungsi Boolean dan merancang rangkaian kombinasional ekuivalen.
3. ≥ 75% mahasiswa mampu menghitung AMAT dan menafsirkan dampak hierarki memori terhadap performa.
4. ≥ 70% mahasiswa mampu membandingkan CISC vs RISC dengan argumen teknis multi-dimensi.
5. ≥ 70% mahasiswa mampu mengevaluasi konfigurasi virtualisasi dan *data center* dengan mempertimbangkan daya, biaya, dan risiko.
6. Rata-rata ketercapaian CPL-07 (P3) dari MK ini ≥ 65,0 (ambang Dokumen 008).

---

## 3. MATRIKS JADWAL PERKULIAHAN

| Pekan | Sub-CPMK | Pokok Bahasan | Metode | Asesmen |
|:--:|---|---|---|---|
| 1 | Orientasi | Ruang lingkup, kontrak belajar, peta CPL–CPMK | Kuliah interaktif | Formatif |
| 2 | 1.1 | Sistem bilangan, komplemen dua, IEEE 754 | Kuliah + latihan | Formatif (kuis LMS) |
| 3 | 1.2 | Arsitektur Von Neumann & siklus instruksi | Ceramah + simulasi datapath | Formatif |
| 4 | 2.1 | Gerbang logika, aljabar Boolean, rangkaian kombinasional & ALU | Case-based learning | **Tugas 1 (20%)** |
| 5 | 2.2 | Flip-flop & rangkaian sekuensial | Ceramah + latihan timing | Formatif |
| 6 | 3.1 | CISC (x86_64) vs RISC (ARM64/RISC-V) | Diskusi kelompok & gallery walk | Formatif (peer feedback) |
| 7 | 3.2 | Hierarki memori, cache L1/L2/L3, AMAT, GPU/NPU | Ceramah + latihan kuantitatif | Formatif (kuis) |
| 8 | — | **UTS** (CPMK-1, 2, 3) | Ujian tertulis | **UTS (30%)** |
| 9 | 4.1 | Bus sistem, arbitrase, interupsi, DMA | Case method | Formatif |
| 10 | 4.2 | Virtualisasi, hypervisor, organisasi data center | Ceramah + studi kasus | Formatif |
| 11 | 4.3 | Studi kasus beban kerja & pemilihan arsitektur | PjBL / case method | Formatif (konsultasi) |
| 12 | 4.4 | Proyek terapan lanjut & presentasi antara | PjBL / presentasi | **Tugas 2 (20%)** |
| 13 | Semua | Penyempurnaan proyek | PjBL / konsultasi | Formatif (checklist) |
| 14 | Semua | Review & konsolidasi | Diskusi / konsultasi | Formatif |
| 15 | Semua | Presentasi final | Presentasi | Formatif (rubrik presentasi) |
| 16 | — | **UAS** (komprehensif) | Ujian tertulis | **UAS (30%)** |

---

## 4. RINCIAN KEGIATAN PER PERTEMUAN

### Pertemuan 1 — Orientasi dan Kontrak Belajar

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Orientasi (fondasi CPMK-1) |
| Indikator | Mahasiswa mampu menjelaskan ruang lingkup MK, capaian pembelajaran, dan skema asesmen |
| Materi | Ruang lingkup arsitektur komputer; peta CPL-05 (P1)/P3/KU1 → CPMK-1..4 → Sub-CPMK; skema 4 titik asesmen; aturan akademik & etika AI |
| Metode | Kuliah interaktif, tanya-jawab, demonstrasi singkat "apa isi dalam CPU" |
| Media | Slide pengantar, foto *die* prosesor, kontrak belajar, LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** salam, presensi, apersepsi "mengapa perlu tahu isi mesin?". **Inti (120′):** (1) pemaparan ruang lingkup & capaian 30′; (2) pemaparan skema asesmen & bobot 25′; (3) kontrak belajar & etika akademik 25′; (4) demonstrasi *disassembly* singkat 40′. **Penutup (15′):** rangkuman, penugasan membaca Bab 1 [1], pengarahan unduh materi LMS |
| Penilaian | Formatif — kehadiran & partisipasi (non-graded) |
| Referensi | [1] Bab 1 |

### Pertemuan 2 — Sistem Bilangan, Komplemen Dua, dan IEEE 754

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-1.1** |
| Indikator | 1.1.1 Ketepatan konversi antar-basis; 1.1.2 Ketepatan penyusunan format IEEE 754 |
| Materi | Sistem bilangan posisional; konversi desimal–biner–heksadesimal; *sign-magnitude*, *one's complement*, komplemen dua; format IEEE 754 (sign, exponent bias 127, mantissa); *denormal*, NaN, Infinity |
| Metode | Kuliah & latihan terbimbing |
| Media | Slide, papan tulis, kalkulator basis daring, lembar latihan |
| **Kegiatan (150′)** | **Pendahuluan (15′):** review tugas baca, pertanyaan pemantik "mengapa 0,1 + 0,2 ≠ 0,3 di komputer?". **Inti (120′):** (1) konversi antar-basis 35′; (2) komplemen dua & rentang representasi 30′; (3) format IEEE 754 & contoh penyusunan 35′; (4) latihan 6 soal 20′. **Penutup (15′):** rangkuman, kuis formatif LMS, penugasan |
| Penilaian | Formatif — kuis LMS (non-graded), observasi latihan |
| Referensi | [1] Bab 3; [6] |

### Pertemuan 3 — Arsitektur Von Neumann dan Siklus Instruksi

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-1.2** |
| Indikator | 1.2.1 Ketepatan urutan siklus; 1.2.2 Ketepatan peran PC, IR, MAR, MDR |
| Materi | Model Von Neumann vs Harvard; komponen CPU (unit kontrol, ALU, register); register PC, IR, MAR, MDR, *general purpose*; siklus *Fetch–Decode–Execute*; pengantar *pipelining* |
| Metode | Ceramah interaktif + simulasi *datapath* |
| Media | Slide, simulator Logisim, diagram *datapath* |
| **Kegiatan (150′)** | **Pendahuluan (15′):** kaitkan representasi data dengan instruksi. **Inti (120′):** (1) model Von Neumann & Harvard 25′; (2) peran register 30′; (3) simulasi siklus untuk instruksi `ADD` 40′; (4) latihan pemetaan siklus 25′. **Penutup (15′):** rangkuman, penugasan membaca [2] Bab 3 |
| Penilaian | Formatif — lembar pemetaan siklus |
| Referensi | [2] Bab 1–3; [3] Bab 1–2 |

### Pertemuan 4 — Gerbang Logika, Aljabar Boolean, dan ALU  ⟶ **TUGAS 1 (20%)**

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-2.1** |
| Indikator | 2.1.1 Ketepatan tabel kebenaran; 2.1.2 Ketepatan penyederhanaan dan perancangan rangkaian |
| Materi | Gerbang AND, OR, NOT, NAND, NOR, XOR, XNOR; hukum aljabar Boolean; K-map; *half adder*, *full adder*; multiplekser, dekoder; struktur dasar ALU |
| Metode | Case-based learning, kerja individu terpandu |
| Media | Slide, simulator logika, formulir Tugas 1 |
| **Kegiatan (150′)** | **Pendahuluan (15′):** pengantar asesmen Tugas 1. **Inti (120′):** (1) gerbang & hukum Boolean 35′; (2) K-map & penyederhanaan 30′; (3) perancangan *full adder* & ALU 25′; (4) pengerjaan Tugas 1 di kelas 30′. **Penutup (15′):** pengumpulan, penjelasan revisi, penugasan lanjutan |
| Penilaian | **Sumatif — Tugas 1 (20%)**, rubrik 4 dimensi (055_5) |
| Referensi | [4] Bab 2–3; [2] Bab 10 |

### Pertemuan 5 — Flip-Flop dan Rangkaian Sekuensial

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-2.2** |
| Indikator | 2.2.1 Ketepatan analisis SR/JK/D flip-flop; 2.2.2 Ketepatan diagram waktu dan *state table* |
| Materi | *Latch* SR vs flip-flop berklok; SR, JK, D, T; *edge-triggered* vs *level-triggered*; register; pencacah (*counter*) sinkron dan asinkron; *state diagram* & *state table* |
| Metode | Ceramah & latihan terstruktur |
| Media | Slide, simulator logika, lembar *timing diagram* |
| **Kegiatan (150′)** | **Pendahuluan (15′):** refleksi Tugas 1. **Inti (120′):** (1) *latch* & flip-flop 35′; (2) analisis *timing* 30′; (3) register & pencacah 30′; (4) latihan 25′. **Penutup (15′):** rangkuman, penugasan membaca [4] Bab 4 |
| Penilaian | Formatif — lembar *timing diagram* |
| Referensi | [4] Bab 4; [5] Bab 3 |

### Pertemuan 6 — CISC (x86_64) versus RISC (ARM64/RISC-V)

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-3.1** |
| Indikator | 3.1.1 Ketepatan komparasi filosofi desain; 3.1.2 Ketepatan analisis konsekuensi performa |
| Materi | *Instruction Set Architecture*; format instruksi; *addressing mode*; filosofi CISC (mikrokode, instruksi kompleks) vs RISC (instruksi sederhana, *load-store*, banyak register); x86_64, ARM64, RISC-V; dampak ke *compiler* dan konsumsi daya |
| Metode | Diskusi kelompok & *gallery walk* |
| Media | Slide, kartu kasus, kertas plano, sticky notes |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "mengapa ponsel memakai ARM, server memakai x86?". **Inti (120′):** (1) penjelasan ISA & CISC/RISC 35′; (2) kerja kelompok menyusun matriks komparasi 40′; (3) *gallery walk* & umpan balik 30′; (4) sintesis 15′. **Penutup (15′):** rangkuman, penugasan |
| Penilaian | Formatif — matriks komparasi & *peer feedback* |
| Referensi | [1] Bab 2; [8] Bab 1 |

### Pertemuan 7 — Hierarki Memori, Cache, dan Akselerator

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-3.2** |
| Indikator | 3.2.1 Ketepatan analisis lokalitas; 3.2.2 Ketepatan hitung *hit/miss ratio* dan AMAT |
| Materi | Hierarki register–cache–DRAM–*storage*; SRAM vs DRAM; lokalitas temporal & spasial; *direct mapped*, *set associative*, *fully associative*; kebijakan *write-through/back*; AMAT = *hit time* + *miss rate* × *miss penalty*; arsitektur GPU (SIMT) dan NPU |
| Metode | Ceramah & latihan kuantitatif |
| Media | Slide, tabel parameter cache, lembar latihan AMAT |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "mengapa cache menentukan performa?". **Inti (120′):** (1) hierarki & lokalitas 30′; (2) organisasi cache 35′; (3) latihan hitung AMAT 35′; (4) pengantar GPU/NPU 20′. **Penutup (15′):** kuis formatif, penugasan |
| Penilaian | Formatif — kuis LMS + lembar AMAT |
| Referensi | [1] Bab 5; [8] Bab 2 |

### Pertemuan 8 — Evaluasi Tengah Semester (UTS)  ⟶ **UTS (30%)**

| Komponen | Uraian |
|---|---|
| Cakupan | CPMK-1, CPMK-2, CPMK-3 (tahap awal) — materi pekan 1–7 |
| Bentuk | Bagian I representasi data (20); II siklus instruksi (15); III rangkaian (30); IV studi kasus komparatif (35) |
| Durasi | 150 menit, *closed book* |
| Pengawasan | Dosen + 1 pengawas; tata tertib ujian fakultas |
| Penilaian | Rubrik UTS (055_5), kunci jawaban terstandar |
| Tindak lanjut | Analisis butir soal; pengumuman nilai ≤ 7 hari; remedial sesuai kebijakan prodi |

### Pertemuan 9 — Bus Sistem dan Interupsi I/O

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.1** |
| Indikator | 4.1.1 Ketepatan analisis arbitrase bus; 4.1.2 Ketepatan pembedaan *polling*, interupsi, dan DMA |
| Materi | Bus data, alamat, kontrol; *synchronous* vs *asynchronous*; arbitrase terpusat & terdistribusi; *vectored interrupt*, prioritas, *masking*; DMA dan *cycle stealing*; PCI Express |
| Metode | Case method |
| Media | Slide, diagram bus, studi kasus server I/O-*bound* |
| **Kegiatan (150′)** | **Pendahuluan (15′):** refleksi UTS & rencana perbaikan. **Inti (120′):** (1) struktur bus & arbitrase 35′; (2) mekanisme interupsi 30′; (3) DMA & studi kasus 35′; (4) latihan klasifikasi 20′. **Penutup (15′):** rangkuman, penugasan |
| Penilaian | Formatif — lembar analisis kasus |
| Referensi | [2] Bab 3 & 7; [3] Bab 3 |

### Pertemuan 10 — Virtualisasi dan Organisasi Data Center

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.2** |
| Indikator | 4.2.1 Ketepatan pembedaan *hypervisor* Tipe 1 vs Tipe 2; 4.2.2 Ketepatan evaluasi *trade-off* *data center* |
| Materi | Virtualisasi CPU (time-sharing), memori (*shadow page table*, EPT/NPT), I/O; *hypervisor* Tipe 1 (bare-metal) vs Tipe 2 (hosted); kontainer vs VM; organisasi *data center*: rak, *top-of-rack switch*, redundansi N+1, pendinginan, PUE |
| Metode | Ceramah & studi kasus |
| Media | Slide, diagram arsitektur *hypervisor*, studi kasus konsolidasi server |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "satu server, sepuluh mesin?". **Inti (120′):** (1) mekanisme virtualisasi 40′; (2) Tipe 1 vs Tipe 2 vs kontainer 30′; (3) organisasi *data center* & PUE 30′; (4) diskusi kasus 20′. **Penutup (15′):** rangkuman, penugasan |
| Penilaian | Formatif — lembar evaluasi kasus |
| Referensi | [7] Bab 16–17; [2] Bab 20 |

### Pertemuan 11 — Studi Kasus Beban Kerja dan Pemilihan Arsitektur

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.3** (penguatan CPMK-3 & CPMK-4) |
| Indikator | 4.3.1 Ketepatan *profiling* beban kerja; 4.3.2 Ketepatan justifikasi pemilihan platform |
| Materi | Karakterisasi beban kerja (CPU-*bound*, memori-*bound*, I/O-*bound*); Roofline model (pengantar); pemilihan x86_64 / ARM64 / GPU / NPU; pertimbangan TCO dan daya |
| Metode | PjBL & case method |
| Media | Slide, tabel spesifikasi platform, template karakterisasi |
| **Kegiatan (150′)** | **Pendahuluan (15′):** pengantar tugas proyek. **Inti (120′):** (1) teknik *profiling* 30′; (2) pembentukan kelompok & pemilihan skenario 20′; (3) penyusunan draf karakterisasi beban 50′; (4) konsultasi 20′. **Penutup (15′):** tenggat draf, arahan lanjutan |
| Penilaian | Formatif — draf karakterisasi |
| Referensi | [8] Bab 1 & 6 |

### Pertemuan 12 — Proyek Terapan dan Presentasi Antara  ⟶ **TUGAS 2 (20%)**

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.4** (integrasi 4.1 & 4.2) |
| Indikator | 4.4.1 Kelayakan rancangan; 4.4.2 Kejelasan argumentasi teknis |
| Materi | Presentasi progres proyek: karakterisasi beban, rancangan platform, estimasi kuantitatif, evaluasi *data center*, *trade-off* |
| Metode | PjBL & presentasi |
| Media | Proyektor, timer, lembar penilaian presentasi |
| **Kegiatan (150′)** | **Pendahuluan (15′):** tata tertib presentasi & rubrik. **Inti (120′):** 4 kelompok × 25′ (15′ presentasi + 10′ tanya jawab & umpan balik). **Penutup (15′):** umpan balik menyeluruh, arahan revisi |
| Penilaian | **Sumatif — Tugas 2 (20%)**, rubrik 4 dimensi (055_5) |
| Referensi | [2]; [7] |

### Pertemuan 13 — Penyempurnaan Proyek

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK (penyempurnaan) |
| Indikator | 4.4.3 Ketepatan revisi; 4.4.4 Kualitas dokumentasi |
| Materi | Revisi berdasarkan umpan balik: kelengkapan karakterisasi, ketepatan estimasi, penajaman evaluasi *data center*, kejelasan *trade-off* |
| Metode | PjBL & konsultasi klinis |
| Media | Lembar konsultasi, repositori dokumen kelompok |
| **Kegiatan (150′)** | **Pendahuluan (15′):** rekap umpan balik agregat. **Inti (120′):** konsultasi bergilir per kelompok 15′ × 8, diselingi kerja mandiri kelompok. **Penutup (15′):** kesepakatan tenggat final |
| Penilaian | Formatif — checklist revisi |
| Referensi | Seluruh materi CPMK-3 & CPMK-4 |

### Pertemuan 14 — Review dan Konsolidasi

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK |
| Indikator | Ketepatan identifikasi kesenjangan pemahaman |
| Materi | Rekapitulasi pekan 1–13; peta konsep terpadu bit → gerbang → ALU → ISA → memori → I/O → virtualisasi; pembahasan soal terpilih |
| Metode | Diskusi & konsultasi |
| Media | Peta konsep besar, bank soal terpilih |
| **Kegiatan (150′)** | **Pendahuluan (15′):** penjelasan mekanisme review. **Inti (120′):** (1) penyusunan peta konsep bersama 40′; (2) pembahasan 8 soal kunci 50′; (3) tanya-jawab terbuka 30′. **Penutup (15′):** arahan UAS, penegasan cakupan |
| Penilaian | Formatif — partisipasi |
| Referensi | Rekapitulasi pekan 1–13 |

### Pertemuan 15 — Presentasi Final

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK |
| Indikator | 4.4.5 Kualitas komunikasi teknis; 4.4.6 Penguasaan saat tanya jawab |
| Materi | Presentasi hasil akhir proyek: karakterisasi, rancangan, estimasi, evaluasi, rekomendasi |
| Metode | Presentasi tim & pleno |
| Media | Proyektor, timer, lembar penilaian |
| **Kegiatan (150′)** | **Pendahuluan (15′):** tata tertib. **Inti (120′):** 4 kelompok × 25′ (15′ presentasi + 10′ tanya jawab). **Penutup (15′):** apresiasi, arahan UAS |
| Penilaian | Formatif — rubrik presentasi (masuk komponen proses) |
| Referensi | Seluruh materi |

### Pertemuan 16 — Evaluasi Akhir Semester (UAS)  ⟶ **UAS (30%)**

| Komponen | Uraian |
|---|---|
| Cakupan | Komprehensif CPMK-1 s.d. CPMK-4 |
| Bentuk | I uraian terpadu representasi/instruksi/ALU (30); II analisis komparatif arsitektur & memori (25); III evaluasi I/O, virtualisasi, *data center* (25); IV perancangan solusi terbuka (20) |
| Durasi | 150 menit, *closed book* |
| Penilaian | Rubrik UAS (055_5) |
| Tindak lanjut | Rekap nilai akhir, analisis ketercapaian CPMK/CPL, input SIAKAD ≤ 7 hari |

---

## 5. LEMBAR MONITORING PELAKSANAAN

| Pekan | Tanggal | Materi Terlaksana | Jumlah Hadir | Catatan Kejadian | Paraf Dosen |
|:--:|---|---|:--:|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |
| 13 | | | | | |
| 14 | | | | | |
| 15 | | | | | |
| 16 | | | | | |

---

## 6. CATATAN PELAKSANAAN DAN RENCANA KONTINGENSI

1. **Kehadiran minimum:** 75% dari 16 pertemuan (12 pertemuan) sebagai syarat mengikuti UAS.
2. **Pertemuan pengganti:** diselenggarakan jika terjadi hari libur nasional atau kegiatan fakultas, dengan materi setara dan bukti dokumentasi.
3. **Pembelajaran daring darurat:** seluruh materi tersedia di LMS; sesi sinkron melalui konferensi video dengan rekaman wajib diunggah.
4. **Keterbatasan laboratorium:** karena MK ini bertipe Teori (P = 0), latihan rangkaian dilakukan dengan simulator daring (Logisim Evolution/Digital) yang dapat dijalankan pada perangkat mahasiswa; tidak diperlukan lab khusus.
5. **Mahasiswa dengan kebutuhan khusus:** penyesuaian waktu asesmen dan format materi (sesuai kebijakan layanan disabilitas universitas).
6. **Integritas akademik:** setiap tugas wajib menyertakan Deklarasi Transparansi AI; dosen berhak melakukan verifikasi lisan 3 menit.
7. **Umpan balik:** hasil asesmen dikembalikan maksimal 7 hari kerja dengan komentar per dimensi rubrik.
8. **Kontingensi perangkat:** untuk mahasiswa tanpa perangkat memadai, disediakan sesi simulasi bersama di laboratorium komputer fakultas dengan jadwal terpisah.

---

*Dokumen ini merupakan penjabaran operasional dari `057_1_RPS_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md` dan konsisten dengan Dokumen 043 (Sub-CPMK & Boundary Guardrails).*
