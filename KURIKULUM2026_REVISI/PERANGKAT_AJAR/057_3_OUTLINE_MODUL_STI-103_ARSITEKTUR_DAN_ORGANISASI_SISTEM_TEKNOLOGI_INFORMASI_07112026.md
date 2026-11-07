# OUTLINE BUKU MODUL PEMBELAJARAN
## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI

> **Jenis dokumen:** Kerangka (*outline*) buku modul ajar yang diturunkan dari RPS
> **Dokumen induk:** `057_1_RPS_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`
> **Rujukan kurikulum:** Dokumen 005, 007, 043 (Sub-CPMK & Boundary Guardrails), 003 (CPL)
> **Tanggal:** 07 November 2026

---

## 1. METADATA MODUL

| Atribut | Keterangan |
|---|---|
| Judul modul | *Arsitektur dan Organisasi Sistem TI: Dari Bit ke Data Center* |
| Kode MK | `STI-103` |
| Penulis | Tim Pengampu Rumpun Infrastruktur & Arsitektur Komputer (Core STI) |
| Penelaah | Koordinator RMK Infrastruktur & Arsitektur Komputer; Unit Penjaminan Mutu FSTI |
| Jenjang / Semester | S1 / Semester 1 |
| Bobot | 3 SKS Teori (TM 150′ + PT 180′ + BM 180′ per pekan) |
| Prasyarat | — |
| Target pembaca | Mahasiswa S1 SISTEKIN tahun pertama; dosen pengampu; asisten tutorial |
| Estimasi tebal | 260–300 halaman A5 (atau 200–230 halaman A4) |
| Bahasa | Indonesia, dengan istilah teknis Inggris dalam tanda kurung miring |
| Bentuk | Buku modul cetak + e-modul (PDF interaktif dengan simulator Logisim/Digital) |
| Status ISBN | Dalam pengajuan Perpustakaan Nasional RI |
| Edisi | Edisi 1 (2027) |

---

## 2. DASAR DAN BATAS PENYUSUNAN

| Aspek | Ketentuan |
|---|---|
| Sumber capaian | CPMK-1 s.d. CPMK-4 dan Sub-CPMK-1.1 s.d. 4.2 dari Dokumen 043 |
| Sumber materi | Pokok bahasan Tabel C Dokumen 007 dan BoK `BK-IS03`, `BK-IT01`, `BK-IT05` |
| Batas isi (*in-scope*) | Arsitektur Von Neumann, ALU, register, siklus *Fetch-Decode-Execute*, hierarki memori (SRAM, DRAM, cache), bus I/O, set instruksi *assembly* dasar |
| Batas larangan (*out-of-scope*) | Logika predikat matematika murni (→ `STI-204`), aljabar relasional basis data (→ `FST-207`), konfigurasi *routing* jaringan komputer (→ `STI-312`) |
| Titik serah terima | Logika matematika diskrit → `STI-204`; abstraksi sistem operasi → `STI-310`; jaringan & *routing* → `STI-312` |

---

## 3. CAPAIAN MODUL

Setelah menuntaskan modul ini, mahasiswa mampu:

1. **Menerapkan** representasi data biner, heksadesimal, *floating point* IEEE 754, dan siklus eksekusi instruksi Von Neumann pada arsitektur prosesor secara tepat (CPMK-1, C3).
2. **Menganalisis** rancangan rangkaian logika kombinasional dan sekuensial menggunakan gerbang logika biner dan flip-flop sebagai dasar operasi ALU (CPMK-2, C4).
3. **Membandingkan** karakteristik arsitektur CISC (x86_64) vs RISC (ARM64/RISC-V), hierarki memori cache L1/L2/L3, dan akselerator GPU/NPU dalam skenario beban kerja nyata (CPMK-3, C4).
4. **Mengevaluasi** mekanisme bus sistem, interupsi I/O, abstraksi virtualisasi *hardware*, dan organisasi server *data center* untuk mendukung infrastruktur *cloud* modern (CPMK-4, C5).

---

## 4. PETA BAB ↔ SUB-CPMK ↔ PEKAN ↔ ASESMEN

| Bab | Judul Bab | Sub-CPMK | Pekan | CPMK | Asesmen Terkait |
|:--:|---|---|:--:|:--:|---|
| 1 | Representasi Data pada Level Mesin | 1.1 | 2 | CPMK-1 | **Tugas 1**, UTS |
| 2 | Arsitektur Von Neumann dan Siklus Instruksi | 1.2 | 3 | CPMK-1 | Tugas 1, UTS |
| 3 | Gerbang Logika, Aljabar Boolean, dan Rangkaian Kombinasional | 2.1 | 4 | CPMK-2 | **Tugas 1**, UTS |
| 4 | Flip-Flop dan Rangkaian Sekuensial | 2.2 | 5 | CPMK-2 | UTS, UAS |
| 5 | Instruction Set Architecture: CISC versus RISC | 3.1 | 6 | CPMK-3 | UTS, Tugas 2 |
| 6 | Hierarki Memori, Cache, dan Akselerator | 3.2 | 7 | CPMK-3 | UTS, Tugas 2, UAS |
| 7 | Bus Sistem, Interupsi I/O, dan DMA | 4.1 | 9 | CPMK-4 | Tugas 2, UAS |
| 8 | Virtualisasi, Hypervisor, dan Organisasi Data Center | 4.2 | 10 | CPMK-4 | **Tugas 2**, UAS |
| 9 | Merancang Platform Komputasi untuk Beban Kerja Nyata | 4.3, 4.4 | 11–12 | CPMK-3, CPMK-4 | **Tugas 2**, UAS |
| Lampiran A | Glosarium dan Tabel Referensi Cepat | — | — | — | — |
| Lampiran B | Lembar Kerja Simulasi Logika dan Soal Terpandu | — | — | — | — |

**Total bab inti:** 9 bab. Setiap bab setara 1–2 pekan pertemuan (16 pekan termasuk UTS & UAS).

---

## 5. STRUKTUR BAKU SETIAP BAB

Setiap bab wajib memuat tujuh komponen berikut, dengan urutan tetap:

| No | Komponen | Isi Wajib | Estimasi |
|:--:|---|---|:--:|
| 1 | **Peta Kompetensi** | Sub-CPMK yang dibina, CPMK induk, indikator kinerja | 0,5 hlm |
| 2 | **Uraian Materi** | 3–6 sub-bab, masing-masing dengan diagram blok dan contoh perhitungan | 12–20 hlm |
| 3 | **Sorotan Kasus (Case Spotlight)** | Satu kasus rekayasa nyata (prosesor, server, atau *data center*) + pertanyaan analitis | 1,5 hlm |
| 4 | **Rangkuman** | 5–8 butir kunci dalam bentuk poin bernomor | 0,5 hlm |
| 5 | **Latihan Terbimbing** | 8–12 soal bertingkat (C2–C5) dengan petunjuk pengerjaan | 1,5 hlm |
| 6 | **Tes Formatif Mandiri** | 10 soal pilihan ganda + 3 esai pendek, kunci di lampiran daring | 2 hlm |
| 7 | **Rujukan Bab** | 3–6 sitasi IEEE, sinkron dengan daftar pustaka RPS | 0,3 hlm |

---

## 6. OUTLINE RINCI PER BAB

### BAB 1 — Representasi Data pada Level Mesin
**Sub-CPMK:** 1.1 | **Pekan:** 2 | **Estimasi:** 28 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 1.1 | Sistem bilangan posisional: desimal, biner, oktal, heksadesimal |
| 1.2 | Konversi antar-basis dan aritmetika dasar pada basis-2 |
| 1.3 | Representasi bilangan bertanda: *sign-magnitude*, *one's complement*, komplemen dua |
| 1.4 | Rentang representasi dan *overflow* |
| 1.5 | Standar IEEE 754: format *single* dan *double precision*, bias eksponen, *mantissa* tersembunyi |
| 1.6 | Kasus khusus: *denormal*, nol, Infinity, NaN |
| 1.7 | Mengapa $0{,}1 + 0{,}2 \ne 0{,}3$: galat representasi dan implikasinya pada perangkat lunak |
| 1.8 | Representasi karakter: ASCII, UTF-8, dan isu *endianness* |

**Kegiatan belajar:** latihan konversi (PT 120′), eksperimen galat *floating point* (PT 60′), diskusi implikasi (TM 35′).
**Tes formatif:** 12 butir konversi + 3 butir analisis galat numerik.

---

### BAB 2 — Arsitektur Von Neumann dan Siklus Instruksi
**Sub-CPMK:** 1.2 | **Pekan:** 3 | **Estimasi:** 26 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 2.1 | Model Von Neumann dan *bottleneck* memori |
| 2.2 | Model Harvard dan perbandingannya |
| 2.3 | Komponen CPU: unit kontrol, ALU, dan register |
| 2.4 | Register khusus: PC, IR, MAR, MDR, SP, *flags* |
| 2.5 | Siklus *Fetch–Decode–Execute* dan *write-back* |
| 2.6 | Contoh penelusuran instruksi `ADD`, `LOAD`, `STORE`, `BRANCH` |
| 2.7 | Pengantar *pipelining* dan *hazard* (level konseptual) |
| 2.8 | Set instruksi *assembly* dasar dan hubungannya dengan kode mesin |

**Kegiatan belajar:** penelusuran siklus (PT 120′), simulasi *datapath* (TM 40′), latihan *disassembly* (PT 60′).
**Tes formatif:** penelusuran lengkap 3 instruksi melalui siklus lima tahap.

---

### BAB 3 — Gerbang Logika, Aljabar Boolean, dan Rangkaian Kombinasional
**Sub-CPMK:** 2.1 | **Pekan:** 4 | **Estimasi:** 34 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 3.1 | Gerbang dasar: AND, OR, NOT; gerbang turunan: NAND, NOR, XOR, XNOR |
| 3.2 | Hukum dan identitas aljabar Boolean |
| 3.3 | Bentuk kanonik SOP dan POS |
| 3.4 | Penyederhanaan dengan K-map (2, 3, 4 variabel) |
| 3.5 | Rangkaian kombinasional: *half adder*, *full adder*, *ripple carry*, *carry look-ahead* |
| 3.6 | Multiplekser, demultiplekser, dekoder, enkoder |
| 3.7 | Perbandingan dan struktur dasar ALU |
| 3.8 | *Hazard* pada rangkaian kombinasional dan *glitch* |

**Kegiatan belajar:** penyederhanaan K-map (PT 150′), perancangan rangkaian di simulator (PT 90′), diskusi ALU (TM 40′).
**Tes formatif:** penyederhanaan 4 fungsi + rancangan *full adder* dari NAND saja.

---

### BAB 4 — Flip-Flop dan Rangkaian Sekuensial
**Sub-CPMK:** 2.2 | **Pekan:** 5 | **Estimasi:** 28 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 4.1 | Perbedaan kombinasional vs sekuensial; peran sinyal jam (*clock*) |
| 4.2 | *Latch* SR berbasis NOR dan NAND |
| 4.3 | Flip-flop berklok: SR, JK, D, T |
| 4.4 | *Edge-triggered* vs *level-triggered*; *setup* dan *hold time* |
| 4.5 | Register dan *register file* |
| 4.6 | Pencacah sinkron dan asinkron |
| 4.7 | Mesin status berhingga (*finite state machine*): *state diagram*, *state table*, implementasi |
| 4.8 | Diagram waktu dan analisis *timing* |

**Kegiatan belajar:** analisis *timing* (PT 120′), perancangan FSM sederhana (PT 120′), diskusi *clock skew* (TM 30′).
**Tes formatif:** gambar diagram waktu 4 flip-flop + rancang pencacah modulo-6.

---

### BAB 5 — Instruction Set Architecture: CISC versus RISC
**Sub-CPMK:** 3.1 | **Pekan:** 6 | **Estimasi:** 28 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 5.1 | Definisi ISA dan posisinya antara *hardware* dan *compiler* |
| 5.2 | Format instruksi: *fixed-length* vs *variable-length* |
| 5.3 | *Addressing mode*: langsung, tidak langsung, terindeks, relatif |
| 5.4 | Filosofi CISC: instruksi kompleks, mikrokode, x86_64 |
| 5.5 | Filosofi RISC: instruksi sederhana, *load-store*, banyak register, ARM64 dan RISC-V |
| 5.6 | Konsekuensi terhadap *pipelining*, konsumsi daya, dan luas *die* |
| 5.7 | Posisi pasar: *server/desktop* vs *mobile/embedded* vs *edge AI* |
| 5.8 | Studi kasus: mengapa Apple Silicon dan AWS Graviton memilih ARM64 |

**Kegiatan belajar:** matriks komparasi kelompok (PT 150′), *gallery walk* (TM 50′), analisis studi kasus (PT 60′).
**Tes formatif:** komparasi lima dimensi antara x86_64, ARM64, dan RISC-V.

---

### BAB 6 — Hierarki Memori, Cache, dan Akselerator
**Sub-CPMK:** 3.2 | **Pekan:** 7 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 6.1 | Hierarki memori: register, cache, DRAM, *storage* |
| 6.2 | Karakteristik SRAM vs DRAM; *refresh* dan latensi |
| 6.3 | Prinsip lokalitas: temporal dan spasial |
| 6.4 | Organisasi cache: *direct mapped*, *set associative*, *fully associative* |
| 6.5 | Kebijakan penggantian dan penulisan (*write-through*, *write-back*) |
| 6.6 | *Average Memory Access Time* (AMAT) dan perhitungannya |
| 6.7 | Memori virtual dan *Translation Lookaside Buffer* (pengantar) |
| 6.8 | Arsitektur GPU (SIMT) dan NPU: kapan lebih unggul dari CPU |
| 6.9 | Studi kasus: dampak ukuran cache pada *inference* model |

**Kegiatan belajar:** latihan AMAT (PT 150′), analisis lokalitas kode (PT 90′), diskusi GPU/NPU (TM 40′).
**Tes formatif:** 4 soal perhitungan AMAT + 2 soal pemilihan akselerator.

---

### BAB 7 — Bus Sistem, Interupsi I/O, dan DMA
**Sub-CPMK:** 4.1 | **Pekan:** 9 | **Estimasi:** 26 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 7.1 | Struktur bus: data, alamat, kontrol |
| 7.2 | Bus *synchronous* vs *asynchronous*; *bus width* dan *bandwidth* |
| 7.3 | Arbitrase bus: terpusat (*daisy chain*, *polling*) dan terdistribusi |
| 7.4 | Mekanisme I/O: *programmed I/O*, *interrupt-driven*, DMA |
| 7.5 | Interupsi: *vectored*, prioritas, *masking*, *nested interrupt* |
| 7.6 | DMA dan *cycle stealing*; dampak pada performa sistem |
| 7.7 | Bus modern: PCI Express, *lane*, dan skalabilitas |
| 7.8 | Studi kasus: server I/O-*bound* dengan *storage* NVMe |

**Kegiatan belajar:** analisis kasus (PT 150′), perhitungan *bandwidth* bus (PT 60′), diskusi prioritas interupsi (TM 40′).
**Tes formatif:** hitung *bandwidth* efektif + usulan strategi I/O untuk skenario.

---

### BAB 8 — Virtualisasi, Hypervisor, dan Organisasi Data Center
**Sub-CPMK:** 4.2 | **Pekan:** 10 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 8.1 | Konsep virtualisasi dan lapisan abstraksi |
| 8.2 | Virtualisasi CPU: *time-sharing* dan penjadwalan vCPU |
| 8.3 | Virtualisasi memori: *shadow page table*, EPT/NPT |
| 8.4 | Virtualisasi I/O: *emulation*, *paravirtualization*, *passthrough* |
| 8.5 | *Hypervisor* Tipe 1 (bare-metal) vs Tipe 2 (hosted) |
| 8.6 | Kontainer vs mesin virtual: isolasi, kepadatan, *startup time* |
| 8.7 | Organisasi *data center*: rak, *top-of-rack switch*, redundansi N+1, jalur daya |
| 8.8 | Pendinginan dan PUE (*Power Usage Effectiveness*) |
| 8.9 | Studi kasus: konsolidasi 40 VM ke 5 server fisik |

**Kegiatan belajar:** analisis kasus konsolidasi (PT 150′), perhitungan PUE dan daya (PT 90′), diskusi risiko *overcommitment* (TM 40′).
**Tes formatif:** evaluasi *trade-off* VM vs kontainer + perhitungan daya tahunan.

---

### BAB 9 — Merancang Platform Komputasi untuk Beban Kerja Nyata
**Sub-CPMK:** 4.3, 4.4 | **Pekan:** 11–12 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 9.1 | Karakterisasi beban kerja: CPU-*bound*, memori-*bound*, I/O-*bound* |
| 9.2 | Teknik *profiling* dan metrik kunci (*throughput*, latensi, *utilization*) |
| 9.3 | Model Roofline (pengantar kualitatif) |
| 9.4 | Pemilihan prosesor: x86_64, ARM64, GPU, NPU |
| 9.5 | Dimensi memori dan penyimpanan |
| 9.6 | Strategi virtualisasi dan orkestrasi |
| 9.7 | Analisis TCO: biaya pengadaan, daya, dan operasional |
| 9.8 | Penyusunan rekomendasi berbasis bukti |

**Kegiatan belajar:** penyusunan karakterisasi (TM 50′), estimasi kuantitatif (PT 120′), penyusunan laporan proyek (PT 180′).
**Tes formatif:** rekomendasi platform untuk tiga skenario berbeda dengan justifikasi.

---

### LAMPIRAN A — Glosarium dan Tabel Referensi Cepat
**Estimasi:** 14 halaman. Memuat ≥ 90 entri istilah (ISA, ALU, cache, DMA, *hypervisor*, PUE, dan lain-lain) beserta padanan Inggris; tabel konversi basis; tabel gerbang logika; tabel parameter cache tipikal; tabel perbandingan ISA.

### LAMPIRAN B — Lembar Kerja Simulasi Logika dan Soal Terpandu
**Estimasi:** 30 halaman. Memuat 10 lembar kerja simulator (dari gerbang dasar hingga FSM), 60 soal bertingkat (C2–C5) dengan petunjuk, serta 4 paket latihan UTS/UAS mandiri.

---

## 7. SPESIFIKASI TEKNIS PENULISAN

| Aspek | Ketentuan |
|---|---|
| Ukuran halaman | A5 (148 × 210 mm), margin 2 cm |
| Tipografi | Body 10,5 pt *serif* (Times New Roman / Book Antiqua); judul sans-serif; spasi 1,15 |
| Tata letak | Satu kolom untuk diagram blok (lebar penuh); dua kolom untuk uraian naratif |
| Diagram | Digambar vektor (SVG); setiap blok diberi label; tabel kebenaran berformat konsisten |
| Notasi | Biner ditulis dengan subskrip 2 (mis. $1011_2$), heksadesimal dengan awalan `0x` |
| Sitasi | IEEE *numbered*, konsisten dengan daftar pustaka RPS |
| Istilah asing | Ditulis miring pada kemunculan pertama, disertai padanan Indonesia |
| Warna | Aksen biru tua untuk kotak definisi; oranye untuk kotak "kesalahan umum"; abu untuk catatan teknis |
| Aksesibilitas | Kontras teks ≥ 4,5:1; tabel memiliki header yang jelas; diagram memiliki teks alternatif |

---

## 8. RENCANA PRODUKSI DAN KENDALI MUTU

| Tahap | Aktivitas | Keluaran | Penanggung Jawab | Durasi |
|:--:|---|---|---|---|
| P1 | Finalisasi outline & alokasi penulis per bab | Dokumen outline ini | Koordinator RMK | 1 pekan |
| P2 | Penulisan draf bab 1–5 | Draf 55% | Tim penulis | 8 pekan |
| P3 | Penulisan draf bab 6–9 + lampiran | Draf 100% | Tim penulis | 6 pekan |
| P4 | Verifikasi teknis (cek ulang diagram, tabel kebenaran, perhitungan AMAT) | Lembar verifikasi | Dua penelaah internal | 3 pekan |
| P5 | Uji simulasi (semua lembar kerja dijalankan di Logisim/Digital) | Laporan uji simulator | Asisten laboratorium | 2 pekan |
| P6 | Telaah sejawat & uji keterbacaan mahasiswa | Laporan telaah + uji 20 responden | Tim penulis | 2 pekan |
| P7 | Penyuntingan bahasa & tata letak | Naskah siap cetak | Penyunting | 2 pekan |
| P8 | Pengajuan ISBN & pencetakan terbatas | ISBN + 50 eksemplar | Prodi & perpustakaan | 3 pekan |

### Checklist mutu sebelum cetak

- [ ] Seluruh Sub-CPMK RPS memiliki bab/sub-bab pembina yang eksplisit.
- [ ] Tidak ada materi yang masuk kategori *out-of-scope* Dokumen 043 (tidak ada logika predikat formal, aljabar relasional, atau konfigurasi *routing*).
- [ ] Setiap tabel kebenaran dan diagram rangkaian telah diverifikasi ulang.
- [ ] Seluruh perhitungan AMAT dan PUE di bab 6 dan 8 terverifikasi.
- [ ] Setiap bab memiliki peta kompetensi, kasus, rangkuman, latihan, dan tes formatif.
- [ ] Seluruh sitasi IEEE valid dan dapat ditelusuri; tidak ada rujukan fiktif.
- [ ] Notasi konsisten lintas bab (biner, heksadesimal, dan nama register).
- [ ] Semua lembar kerja simulator dapat dijalankan tanpa galat.
- [ ] Uji keterbacaan: ≥ 80% responden menilai materi mudah diikuti.

---

## 9. KETERKAITAN DENGAN DOKUMEN LAIN

| Dokumen | Keterkaitan |
|---|---|
| `057_1_RPS_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md` | Sumber capaian, materi, dan titik asesmen |
| `057_2_SAP_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md` | Sumber alokasi waktu dan urutan kegiatan per pekan |
| `057_4_RENCANA_EVALUASI_ASESMEN_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md` | Sumber bobot dan jadwal evaluasi |
| `057_5_RUBRIK_PENILAIAN_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md` | Sumber kriteria penilaian latihan dan tes formatif |
| Dokumen 043 | Batas isi (*in-scope*, *out-of-scope*, *handoff anchor*) |
| Dokumen 037 | Demarkasi silabus antar-MK |

---

*Outline ini merupakan rancangan kerja penulisan modul; perubahan judul bab wajib melalui persetujuan Koordinator RMK dan dicatat dalam riwayat revisi.*
