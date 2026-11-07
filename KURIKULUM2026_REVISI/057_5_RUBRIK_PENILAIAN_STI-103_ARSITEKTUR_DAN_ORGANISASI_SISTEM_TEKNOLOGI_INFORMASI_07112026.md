# 057_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI (*Information Technology Systems Architecture and Organization*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 1 — Tahap Fondasi)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI103`  
**Klaster Rubrik Master (Dok 018):** Klaster 1 (`K-1`) dipadukan Dimensi Evaluasi Infrastruktur  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** Panduan KPT 2024 Dikti (Tabel 18, 19, 20) · Dok 008 §4 · Dok 018 §3 · Dok 033 · `057_1_RPS_STI-103_...md` · `057_4_RENCANA_EVALUASI_ASESMEN_STI-103_...md`.

---

## BAGIAN I — KERANGKA RUBRIK & GRADASI PENILAIAN

Perangkat rubrik pada `STI-103` mengukur progresi kognitif dari **ketepatan representasi bit & penelusuran register (`C3` pada `CPMK-1`)**, **analisis rangkaian logika & *datapath* ALU (`C4` pada `CPMK-2`)**, **komparasi kritis prosesor, memori, & akselerator (`C4` pada `CPMK-3`)**, hingga **evaluasi komprehensif interkoneksi bus/DMA, *Hypervisor*, & server *data center* (`C5` pada `CPMK-4`)**.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1`: `Sub-CPMK-1.1` & `1.2`)
**Objek Penilaian:** Lembar Kerja Terstruktur Berparameter NIM: Konversi Biner/Hex, *Two's Complement*, IEEE 754 32-bit, dan Penelusuran Siklus Instruksi Von Neumann.

| Dimensi Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konversi Basis Bilangan & Aritmetika *Two's Complement***<br>(`Sub-CPMK-1.1`) | **30%** | Seluruh konversi biner/oktal/hex dan operasi *Two's Complement* 8-bit benar 100% sesuai parameter NIM; pembuktian ada/tidaknya *overflow* sangat tepat. | Langkah konversi dan operasi *Two's Complement* benar dengan maks. 1 selip hitung bit minor; analisis *overflow* tepat. | Prosedur *Two's Complement* dipahami dengan benar, namun terdapat kesalahan bit pada 1 soal atau penjelasan syarat *overflow* kurang rinci. | Mencampuradukkan *One's Complement* dengan *Two's Complement* atau gagal mendeteksi kondisi *overflow*. | Hanya menulis hasil konversi kalkulator tanpa langkah pembagian/inversi bit, atau memakai parameter NIM milik orang lain. |
| **2. Pengkodean IEEE 754 32-bit & Analisis Presisi Pecahan**<br>(`Sub-CPMK-1.1`) | **35%** | Menentukan bit *Sign*, *Biased Exponent* ($E+127$), dan 23-bit *Mantissa* (serta representasi hex 8-digit) secara presisi; menjelaskan penyebab galat pembulatan pecahan biner dengan sangat jernih. | Langkah normalisasi $1,M \times 2^E$ dan penentuan *bias* $+127$ tepat; hanya terdapat selip 1 bit di ujung *mantissa* atau konversi hex akhir. | Memahami struktur 1–8–23 bit IEEE 754, namun sempat keliru 1 langkah saat menggeser koma biner atau menjelaskan galat pembulatan secara singkat. | Salah menghitung *Biased Exponent* (lupa menambahkan 127) atau menyertakan angka `1` di depan koma ke dalam 23-bit *mantissa*. | Tidak mampu menguraikan format IEEE 754 sama sekali. |
| **3. Penelusuran Register Siklus `Fetch-Decode-Execute` Von Neumann**<br>(`Sub-CPMK-1.2`) | **35%** | Tabel perubahan nilai `PC, MAR, MBR, IR,` dan `ACC` pada ke-4 siklus instruksi terisi lengkap, berurutan tepat waktu (termasuk inkremen `PC`), dan konsisten penuh dengan isi memori akhir. | Penelusuran siklus instruksi dan hasil akhir `ACC`/memori benar; hanya terdapat 1 sel tabel antara `MAR/MBR` yang kurang rinci pada 1 sub-siklus. | Alur utama pengambilan instruksi dan eksekusi di `ACC` benar, namun pencatatan saat `PC` bertambah $+1$ sedikit bergeser fasenya. | Tertukar peran antara register alamat (`MAR`/`PC`) dengan register penampung data/instruksi (`MBR`/`IR`). | Tabel penelusuran register kosong atau diisi angka acak yang tidak mengikuti eksekusi program. |

$$\text{Skor Tugas 1} = 0,30(K_1) + 0,35(K_2) + 0,35(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2`: `Sub-CPMK-2.1` & `2.2`)
**Objek Penilaian:** Jawaban Ujian Tertulis 150 Menit: Minimasi Gerbang K-Map, Rangkaian Kombinasional & *Flags* ALU, *Timing Diagram Flip-Flop*/Register, dan *CPU Datapath*.

| Dimensi Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Tabel Kebenaran & Minimasi Rangkaian Gerbang via K-Map**<br>(Soal 1 — `Sub-CPMK-2.1`) | **25%** | Tabel kebenaran akurat, pengelompokan * Gray code* pada K-Map 4 variabel menghasilkan suku paling minimal, dan diagram gerbang logika digambar bersih sesuai standar simbol. | Tabel kebenaran dan pemetaan K-Map benar; pengelompokan sah namun masih menyisakan 1 suku yang sebenarnya bisa digabung lebih besar. | Tabel kebenaran benar dan memahami cara kerja dasar K-Map, namun terdapat kekeliruan urutan kolom `00-01-11-10` atau gambar gerbang kurang rapi. | Menyusun ekspresi SOP mentah yang panjang tanpa mampu melakukan penyederhanaan Boole/K-Map. | Tabel kebenaran maupun rangkaian gerbang salah total. |
| **2. Analisis Rangkaian Kombinasional & *Status Flags* ALU**<br>(Soal 2 — `Sub-CPMK-2.1`) | **30%** | Menelusuri jalur *Full Adder-Subtractor* dan pemilih *Multiplexer* pada ALU 4-bit secara tepat untuk seluruh skenario, serta akurat menentukan ke-4 *flags* (`Zero, Negative, Carry, Overflow`). | Hasil keluaran 4-bit ALU tepat seluruhnya dan minimal 3 dari 4 *status flags* dianalisis dengan benar (hanya selip kecil membedakan *Carry* vs *Signed Overflow*). | Mampu menelusuri operasi `AND/OR/ADD` dasar pada ALU, namun kurang tepat saat menelusuri mode pengurangan (`SUB`) atau penentuan bendera `Overflow`. | Gagal memahami fungsi sinyal pemilih (*select lines*) pada *Multiplexer* di dalam ALU. | Tidak mampu menganalisis skema rangkaian kombinasional ALU. |
| **3. Analisis Sekuensial *Flip-Flop*, *Timing Diagram*, & Register**<br>(Soal 3 — `Sub-CPMK-2.2`) | **25%** | Gelombang keluaran $Q$ pada *Timing Diagram* tepat berubah hanya pada tepi aktif *clock* (*rising/falling edge*) dengan memperhatikan sinyal `Reset`/`Enable`, serta isi *Shift/Parallel Register* akurat. | *Timing Diagram* hampir seluruhnya presisi; hanya terdapat 1 transisi pulsa yang sedikit bergeser namun prinsip *edge-triggered* dipahami kuat. | Memahami perbedaan *latch* vs *flip-flop* dan mampu mengisi tabel status dasar, tetapi sempat mengubah nilai $Q$ di tengah level *clock* tinggi (tertukar perilaku *latch*). | Tidak memperhatikan sinyal *clock* atau `Write Enable` saat menentukan perubahan isi register. | Gagal membaca maupun menggambar diagram waktu rangkaian sekuensial. |
| **4. Analisis Integrasi *CPU Datapath***<br>(Soal 4 — `Sub-CPMK-2.1 & 2.2`) | **20%** | Menjelaskan secara sistematis aliran pembacaan dua register dari *Register File*, pengolahan di ALU, dan penulisan balik saat tepi *clock* berikutnya beserta peran sinyal kontrol. | Alur *datapath* dari register ke ALU dan kembali ke register tujuan diuraikan tepat dan runtut. | Menjelaskan fungsi bagian *Register File* dan ALU secara benar namun hubungan sinkronisasi waktu tulisnya masih dijelaskan secara umum. | Penjelasan terpotong-potong tanpa menghubungkan peran elemen sekuensial dan kombinasional. | Kosong atau salah konsep secara mendasar. |

$$\text{Skor UTS} = 0,25(K_1) + 0,30(K_2) + 0,25(K_3) + 0,20(K_4)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3`: `Sub-CPMK-3.1` & `3.2`)
**Objek Penilaian:** Laporan Studi Kasus *Benchmarking* Arsitektur (6–8 hal.): CISC vs RISC, Perhitungan EAT *Cache* & RAID, serta Akselerator CPU vs GPU vs NPU.

| Dimensi Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Komparasi Kritis Arsitektur CISC (`x86_64`) vs RISC (`ARM64`/`RISC-V`)**<br>(`Sub-CPMK-3.1`) | **30%** | Membandingkan spesifikasi prosesor nyata secara tajam (arsitektur ISA, jumlah *core*, TDP watt, ekosistem) dan memberikan rekomendasi yang sangat tepat bagi ke-3 skenario beban kerja. | Perbandingan CISC vs RISC menggunakan data spesifikasi nyata dengan argumen teknis kuat dan sesuai konteks beban kerja. | Membandingkan ciri umum CISC vs RISC dengan benar, namun pengaitan dengan angka spesifikasi prosesor yang dipilih masih bersifat deskriptif permukaan. | Perbandingan berisi klaim usang/keliru (mis. menganggap RISC tidak sanggup menjalankan beban server berat) tanpa data spesifikasi nyata. | Menyalin deskripsi pemasaran brosur tanpa analisis arsitektural. |
| **2. Analisis Hierarki Memori, Perhitungan EAT *Cache*, & Konfigurasi RAID**<br>(`Sub-CPMK-3.2`) | **35%** | Rumus dan perhitungan *Effective Access Time* (EAT) `L1/L2/L3/RAM` tepat dan diinterpretasikan dampaknya; rekomendasi NVMe + skema RAID (kapasitas bersih, IOPS, toleransi gagal disk) sangat akurat. | Perhitungan EAT benar dan pemilihan skema RAID untuk server transaksi tepat disertai alasan keandalan yang jelas. | Perhitungan EAT dasar benar dan menyebutkan jenis RAID yang wajar, namun perhitungan kapasitas bersih atau analisis penalti tulis RAID kurang lengkap. | Rumus EAT salah susun atau memilih `RAID 0` (tanpa redundansi!) untuk server basis data kritis rumah sakit. | Tidak menyertakan perhitungan *cache* maupun analisis penyimpanan RAID. |
| **3. Ketepatan Analisis Beban Kerja Akselerator CPU vs GPU vs NPU**<br>(`Sub-CPMK-3.2`) | **25%** | Menguraikan secara presisi perbedaan mikroarsitektur CPU (*latency/branch*), GPU (*parallel throughput/Tensor Cores/HBM*), dan NPU (*low-power edge AI inference*) sesuai tuntutan Skenario 2 & 3. | Penjelasan alasan kapan memakai CPU, GPU, dan NPU akurat secara arsitektural dan relevan dengan skenario kasus. | Mampu membedakan bahwa GPU untuk komputasi paralel besar dan NPU untuk efisiensi daya, namun belum mengaitkan dengan struktur ALU/*memory bandwidth*. | Hanya menyebut "GPU lebih cepat dari CPU untuk semua hal" tanpa memahami batas beban kerja sekuensial. | Gagal menjelaskan fungsi dan perbedaan GPU maupun NPU. |
| **4. Rujukan *Datasheet* Resmi, Kerapian Matriks, & Deklarasi AI** | **10%** | Mengutip $\ge 3$ *datasheet/whitepaper* resmi terverifikasi, tabel perbandingan sangat informatif, deklarasi AI jujur dan lengkap. | Rujukan resmi valid, tata tulis rapi, deklarasi AI terisi lengkap. | Rujukan ada namun sebagian diambil dari situs ulasan sekunder; format laporan cukup rapi. | Klaim angka spesifikasi tidak mencantumkan sumber rujukan teknis. | Memfabrikasi tipe prosesor/angka spesifikasi palsu hasil halusinasi AI atau plagiasi. |

$$\text{Skor Tugas 2} = 0,30(K_1) + 0,35(K_2) + 0,25(K_3) + 0,10(K_4)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4`: `Sub-CPMK-4.1` & `4.2`)
**Objek Penilaian:** Jawaban Ujian Evaluasi Studi Kasus Infrastruktur Sistem TI (150 menit): Bus PCIe/Interupsi/DMA, Virtualisasi *Hypervisor*, Audit *Server Data Center*, & Sintesis.

| Dimensi Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Evaluasi Interkoneksi Bus PCIe, Interupsi I/O, & Efisiensi DMA**<br>(Kasus 1 — `Sub-CPMK-4.1`) | **25%** | Menemukan secara presisi letak *bottleneck* jalur PCIe (lengkap dengan hitungan GB/s) dan mengevaluasi keunggulan kuantitatif mekanisme *Interrupt* + DMA terhadap beban siklus CPU secara tajam. | Identifikasi *bottleneck* PCIe dan evaluasi perbandingan *Polling* vs *Interrupt* vs DMA tepat dan logis. | Memahami fungsi dasar interupsi dan DMA dalam meringankan CPU, namun perhitungan lebar pita jalur PCIe kurang presisi. | Tertukar cara kerja *Interrupt-Driven I/O* dengan *Direct Memory Access* (DMA) atau gagal melihat penyempitan jalur bus. | Tidak mampu mengevaluasi mekanisme bus maupun I/O. |
| **2. Evaluasi Virtualisasi Hardware & Perencanaan Konsolidasi *Hypervisor***<br>(Kasus 2 — `Sub-CPMK-4.2`) | **25%** | Mengevaluasi secara komprehensif peran `VT-x/AMD-V`, `EPT`, & `IOMMU`, alasan pemilihan *Hypervisor* Tipe 1, serta menghitung *sizing* konsolidasi *host* dengan cadangan *failover* $N+1$ tanpa cacat. | Evaluasi *Hypervisor* Tipe 1 vs Tipe 2 dan peran ekstensi virtualisasi CPU tepat; perhitungan alokasi *vCPU/RAM* rasional. | Mampu membedakan *Hypervisor* Tipe 1 dan Tipe 2 dengan benar serta menyusun alokasi VM dasar, namun lupa memperhitungkan cadangan kapasitas saat 1 *host* gagal. | Mengusulkan *Hypervisor* Tipe 2 di atas OS desktop untuk server produksi kritis atau melakukan *RAM overcommitment* ekstrem. | Gagal menjelaskan konsep virtualisasi perangkat keras dan *Hypervisor*. |
| **3. Audit Kritis & Rekomendasi Organisasi *Server Data Center* Cloud**<br>(Kasus 3 — `Sub-CPMK-4.2`) | **30%** | Berhasil menemukan seluruh titik kegagalan tunggal (*SPOF*: non-ECC, non-RAID, PSU tunggal, PUE buruk, klaim *Tier* keliru) pada kasus dan merumuskan revisi spesifikasi rak server yang koheren & realistis. | Mengidentifikasi mayoritas kelemahan desain server *data center*, menghitung PUE dengan benar, dan memberikan rekomendasi perbaikan yang tepat. | Menemukan minimal 2–3 kelemahan utama (mis. perlunya RAID dan PSU ganda) serta memahami konsep dasar *Tier*, namun analisis PUE/memori ECC masih singkat. | Hanya memberi saran umum ("beli server yang lebih mahal") tanpa mengevaluasi komponen redundansi spesifik. | Tidak mampu mengaudit kelemahan desain infrastruktur server. |
| **4. Keutuhan Sintesis Lintas-Lapisan Arsitektur Sistem TI**<br>(Kasus 4 — Sintesis `CPMK-1..4`) | **20%** | Merangkai alur kerja dari abstraksi VM/*Hypervisor*, jalur PCIe/DMA, hierarki *Cache*/VRAM, hingga eksekusi aritmetika `FP16`/IEEE 754 di ALU/Tensor Core secara utuh, sistematis, dan akurat. | Menghubungkan minimal 4 lapisan arsitektur dari level infrastruktur cloud hingga eksekusi prosesor/akselerator secara runtut. | Menjelaskan tahapan utama dengan cukup benar walau transisi antar-komponen (mis. dari DMA ke *cache*) masih bersifat garis besar. | Penjelasan melompat-lompat dan mencampuradukkan lapisan perangkat keras dengan protokol aplikasi tingkat tinggi. | Kosong atau tidak menunjukkan pemahaman keterkaitan antar-materi. |

$$\text{Skor UAS} = 0,25(K_1) + 0,25(K_2) + 0,30(K_3) + 0,20(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF DISKUSI KASUS ARSITEKTUR & PENELUSURAN SIMULATOR

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketelitian Eksplorasi Simulator (LMC / CircuitVerse)** | Mandiri membangun/menelusuri skema dan mampu memprediksi perubahan nilai bit/register sebelum tombol langkah ditekan. | Menjalankan simulasi sesuai panduan dengan hasil akurat dan mencatat pengamatan secara lengkap. | Menyelesaikan simulasi dasar dengan bantuan rekan namun masih pasif menafsirkan hasilnya. | Tidak menjalankan penelusuran atau sekadar menyalin tangkapan layar rekan. |
| **Kualitas Argumen Teknis pada Debat Kasus (CISC/RISC, RAID, Cloud)** | Argumen berbasis metrik kuantitatif (*latency, throughput, watt, fault tolerance*) dan bebas salah kaprah pemasaran. | Argumen logis dan merujuk konsep arsitektur yang relevan. | Argumen benar secara umum tetapi belum didukung perbandingan metrik teknis. | Argumen subjektif tanpa landasan arsitektur perangkat keras. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat Capaian | Deskriptor Integratif Penguasaan `STI-103` (`CPL-05`, `CPL-07`, & `CPL-02` — Level *Introduce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa memiliki penguasaan sistemik dari bit biner/IEEE 754 dan rangkaian ALU hingga evaluasi kritis CPU CISC/RISC, *cache*, akselerator GPU/NPU, bus PCIe/DMA, *Hypervisor*, dan desain *server data center* berstandar ketersediaan *cloud*. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa mampu menerapkan konversi data, menganalisis rangkaian kombinasional-sekuensial, membandingkan spesifikasi prosesor/memori/akselerator secara objektif, dan mengevaluasi arsitektur virtualisasi serta server dengan tepat. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa menguasai prinsip dasar representasi data, siklus Von Neumann, gerbang logika/ALU, hierarki memori, serta fungsi dasar I/O, *Hypervisor*, dan komponen server sesuai ambang ketuntasan OBE ($\ge 65,0$). |
| **2** | **Kurang (*Developing*)** | Mahasiswa memahami komponen komputer secara terpisah-pisah namun lemah dalam analisis rangkaian logika, perhitungan *cache*/RAID, dan evaluasi kemacetan infrastruktur. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai konsep fundamental arsitektur dan organisasi sistem TI atau melanggar kejujuran akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20 & DOK 033)

**Skala Persepsi:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-103` | Rujukan Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu mengonversi bilangan biner, heksadesimal, *Two's Complement*, dan format *floating point* IEEE 754 secara akurat. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menjelaskan dan menelusuri perubahan register pada siklus eksekusi instruksi `Fetch-Decode-Execute` Von Neumann. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu menganalisis gerbang logika biner, Peta Karnaugh, dan rangkaian kombinasional pembentuk ALU. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menganalisis cara kerja *flip-flop* dan rangkaian logika sekuensial penyimpan status register. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu membandingkan kelebihan dan keterbatasan arsitektur prosesor CISC (`x86_64`) terhadap RISC (`ARM64`/`RISC-V`). | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menganalisis pengaruh hierarki memori *cache* `L1/L2/L3`, penyimpanan NVMe/RAID, dan akselerator GPU/NPU pada kinerja sistem. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu mengevaluasi potensi *bottleneck* pada bus PCIe serta efisiensi *Interrupt-Driven I/O* dan DMA. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu mengevaluasi peran *Hypervisor* dan kelayakan spesifikasi organisasi *server data center* untuk mendukung layanan *cloud*. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-103`)

```text
====================================================================================================================================
        LEMBAR REKAPITULASI PENILAIAN OBE MULTI-CPL — STI-103 ARSITEKTUR & ORGANISASI SISTEM TI (3 SKS TEORI)
====================================================================================================================================
Semester / Tahun Akademik : Semester 1 (Ganjil) / 2026-2027     CPL : CPL-05 (P1: 25%), CPL-07 (P3: 40%), CPL-02 (KU1: 35%) [Level I]
Klaster Rubrik            : K-1 (Arsitektur & Sains Komputasi)  Ambang OBE : >= 65.0 per CPMK & CPL (Target Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mhs     | T1(20%) | UTS(30%)| T2(20%) | UAS(30%)| CPL-05 | CPL-07 | CPL-02 | Nilai | Huruf | Status OBE
   |           |              | [CPMK1] | [CPMK2] | [CPMK3] | [CPMK4] |  (P1)  |  (P3)  |  (KU1) | Akhir | Mutu  | Semua CPL >=65
------------------------------------------------------------------------------------------------------------------------------------
1  | 260101001 | [Nama Mhs 1] |  85.0   |  80.0   |  84.0   |  82.0   |  82.00 |  83.35 |  81.60 | 82.40 |   A   | YA
2  | 260101002 | [Nama Mhs 2] |  76.0   |  70.0   |  72.0   |  74.0   |  72.40 |  73.90 |  71.83 | 72.80 |   B   | YA
3  | 260101003 | [Nama Mhs 3] |  68.0   |  66.0   |  70.0   |  68.0   |  66.80 |  68.60 |  67.60 | 67.80 |   C+  | YA
------------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS               |  76.33  |  72.00  |  75.33  |  74.67  |  73.73 |  75.28 |  73.68 | 74.33 | % >=65: 100%
====================================================================================================================================
```
