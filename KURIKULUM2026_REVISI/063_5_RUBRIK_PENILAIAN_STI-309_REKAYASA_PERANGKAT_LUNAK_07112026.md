# 063_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-309 — REKAYASA PERANGKAT LUNAK (*Software Engineering*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI309` · **Klaster Rubrik Master (Dok 018):** Klaster 4 (`K-4`)  
**CPL:** `CPL-08` (`P4` = 50%) & `CPL-13` (`KK5` = 50%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN REKAYASA PERANGKAT LUNAK (`K-4`)

Selaras **Dokumen 018 §3**, penilaian pada `STI-309 Rekayasa Perangkat Lunak` menekankan ketajaman justifikasi rekayasa proses, kebersihan arsitektur modular berprinsip **SOLID** & **GoF**, presisi matematis/analitis perancangan skenario pengujian **White-Box** & **Black-Box**, serta objektivitas evaluasi kualitas perangkat lunak berstandar **ISO/IEC 25010** dan pengujian otomatis.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-08` [C4])
**Objek Penilaian:** Studi Kasus Pemilihan & Justifikasi Model Proses (*Waterfall, V-Model, Scrum, Kanban*) + Kuis Verifikasi Kelas.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Analisis Karakteristik Risiko, Regulasi, & Kebutuhan Proyek**<br>(`Sub-CPMK-1.1`) | **30%** | Mengidentifikasi secara tajam tingkat volatilitas kebutuhan, risiko keselamatan/regulasi, ukuran tim, dan pola rilis pada ketiga kasus proyek tanpa celah. | Analisis karakteristik ketiga proyek tepat dan relevan sebagai dasar pemilihan metodologi. | Karakteristik utama proyek teridentifikasi, namun aspek risiko atau kendala regulasi dibahas sekilas. | Salah membaca konteks proyek (mis. menganggap sistem medis kritis sama dengan aplikasi prototipe). | Tidak melakukan analisis konteks proyek. |
| **2. Komparasi & Justifikasi Pemilihan Model Proses**<br>(`Sub-CPMK-1.1 & 1.2`) | **40%** | Matriks perbandingan *Waterfall, V-Model, Scrum,* dan *Kanban* sangat objektif; pilihan model untuk tiap kasus dijustifikasi secara kritis beserta analisis *trade-off*-nya dan selaras kuis kelas. | Pemilihan model proses tepat untuk seluruh kasus dengan argumen perbandingan yang logis dan kuat. | Pilihan model proses cukup masuk akal, namun argumen pembandingnya masih bersifat definisi buku teks umum. | Memaksakan satu model proses yang sama (mis. "Scrum untuk segalanya") tanpa justifikasi konteks. | Salah memahami prinsip dasar keempat model proses. |
| **3. Perancangan Mekanisme Operasional (*V-Mapping / DoD / WIP*)**<br>(`Sub-CPMK-1.2`) | **20%** | Merancang peta verifikasi *V-Model*, siklus acara & *Definition of Done* Scrum, atau papan *WIP Limit* Kanban yang spesifik dan langsung operasional bagi kasusnya. | Rancangan artefak operasional metodologi sesuai aturan *Scrum Guide / V-Model* dengan baik. | Mencantumkan tahapan kerja umum namun belum spesifik ke domain proyek yang dibahas. | Mencampuradukkan istilah Scrum dan Kanban secara keliru (mis. *Sprint* kaku di dalam Kanban murni tanpa penjelasan). | Tidak menyertakan rancangan operasional proses. |
| **4. Tata Tulis Ilmiah & Rujukan Standar (SWEBOK / Scrum Guide)** | **10%** | Naskah sangat terstruktur, ringkas-padat, dan merujuk tepat pada standar SWEBOK / Scrum Guide. | Struktur laporan rapi dan menyertakan rujukan pustaka yang relevan. | Laporan cukup rapi walau format sitasi belum seragam. | Tata tulis kurang teratur dan minim rujukan. | Terindikasi salin-tempel tanpa pengolahan mandiri. |

$$\text{Skor Tugas 1} = 0,30(K_1) + 0,40(K_2) + 0,20(K_3) + 0,10(K_4)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2` / `CPL-08` [C3/C4])
**Objek Penilaian:** Jawaban Ujian Tertulis Studi Kasus 150 Menit: Dekomposisi Arsitektur Modular, *Refactoring* **SOLID**, & **GoF Design Patterns**.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Dekomposisi Arsitektur Modular (*Low Coupling & High Cohesion*)**<br>(Soal 1 — `Sub-CPMK-2.1`) | **30%** | Tepat membongkar ketergantungan melingkar/*tight coupling* dan merancang pemisahan lapisan/modul dengan tanggung jawab kohesif dan arah dependensi satu arah yang bersih. | Pemisahan lapisan arsitektur tepat, *coupling* berkurang nyata, dan tanggung jawab tiap modul jelas. | Mampu membagi sistem ke beberapa modul/lapisan dasar, namun masih tersisa 1 ketergantungan langsung ke detail basis data. | Pembagian modul masih semu (sekadar memecah berkas tanpa menurunkan *coupling*). | Gagal merancang dekomposisi arsitektur modular. |
| **2. Diagnosis *Code Smells* & Penerapan Prinsip **SOLID****<br>(Soal 2 — `Sub-CPMK-2.1 & 2.2`) | **40%** | Tepat menunjuk baris pelanggar **SRP, OCP, LSP, ISP, / DIP** serta menulis ulang antarmuka & kelas ter-*refactor* yang bersih, polimorfik, dan mudah disuntik dependensi (*DI*). | Diagnosis pelanggaran SOLID tepat dan rancangan kode hasil *refactoring* menyelesaikan masalah utama dengan baik. | Mengenali pelanggaran SRP/OCP dengan benar, namun pada *refactoring* DIP masih menginstansiasi kelas konkret `new` di dalam logika inti. | Hanya menyebutkan singkatan SOLID secara hafalan tanpa mampu memperbaiki kode studi kasus. | Tidak mampu mengidentifikasi maupun memperbaiki pelanggaran SOLID. |
| **3. Pemilihan & Struktur Penerapan **GoF Design Pattern****<br>(Soal 3 — `Sub-CPMK-2.2`) | **30%** | Memilih pola **GoF** paling tepat sesuai konteks masalah, menggambar diagram kelas peran pola dengan akurat, dan menulis kerangka implementasi yang bersih tanpa *over-engineering*. | Pemilihan pola GoF tepat, struktur antarmuka/kelas benar, hanya terdapat kekurangan sintaks minor pada kerangka kode. | Pola GoF yang dipilih relevan, namun peran salah satu kelas peserta pola (*Context / ConcreteStrategy / Subject*) kurang lengkap. | Salah memilih pola (mis. memakai *Singleton* untuk masalah variasi algoritma *Strategy*). | Bagian *Design Pattern* kosong atau salah konsep total. |

$$\text{Skor UTS} = 0,30(K_1) + 0,40(K_2) + 0,30(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3` / `CPL-13` [C4])
**Objek Penilaian:** Dokumen Perancangan Pengujian **White-Box** (*CFG, $V(G)$, Basis Path*) & **Black-Box** (*EP, BVA, Decision Table*) + Kuis Verifikasi.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. *Control Flow Graph*, **Cyclomatic Complexity $V(G)$**, & *Basis Path***<br>(`Sub-CPMK-3.1`) | **45%** | CFG akurat (termasuk pemecahan kondisi majemuk `AND/OR`), ketiga rumus $V(G)$ menghasilkan nilai konsisten eksak, seluruh *Independent Basis Paths* valid, dan data uji mencapai 100% *Branch Coverage*. | CFG, perhitungan $V(G)$, dan daftar *Basis Paths* benar; hanya terdapat 1 kekurangan minor pada pemisahan simpul kondisi majemuk. | Menggambar CFG dasar dan menghitung $V(G)$ dengan benar, namun terdapat 1 jalur pada daftar *Basis Paths* yang sebenarnya kombinasi jalur lain (tidak independen). | Salah menggambar panah *loop* pada CFG sehingga nilai $V(G)$ dan seluruh jalur uji ikut keliru. | Tidak mampu menyusun CFG maupun menghitung *Cyclomatic Complexity*. |
| **2. Partisi **EP**, Titik Batas **BVA**, & *Decision Table Black-Box***<br>(`Sub-CPMK-3.2`) | **40%** | Seluruh kelas ekuivalensi valid & invalid (**EP**) terpetakan lengkap, titik uji tepi **BVA** (`min-1, min, min+1, max-1, max, max+1`) presisi tanpa terlewat, dan *Decision Table* mencakup seluruh aturan kombinatorial. | Partisi EP, nilai batas BVA, dan *Decision Table* dirancang akurat dengan cakupan skenario negatif yang baik. | Partisi EP valid/invalid benar, namun pada BVA hanya menguji nilai `min` dan `max` tanpa menguji tepat di luar batas (`min-1`, `max+1`). | Kasus uji dipilih secara acak/tebakan tanpa metodologi EP maupun BVA. | Gagal merancang skenario pengujian *Black-Box*. |
| **3. Standar Spesifikasi Kasus Uji & Konsistensi Verifikasi Kelas** | **15%** | Tabel kasus uji berstandar industri (`TC-ID, Tujuan, Precondition, Input, Expected Result` eksak) dan mahasiswa menjawab kuis verifikasi dengan sempurna. | Format spesifikasi kasus uji rapi-lengkap dan hasil kuis verifikasi selaras baik. | Tabel kasus uji cukup lengkap walau kolom *Expected Result* pada 1–2 butir masih kurang spesifik. | Banyak kasus uji menulis *"Berhasil / Error"* secara kabur tanpa nilai keluaran yang diharapkan. | Tidak mengikuti parameter NIM sendiri atau gagal saat verifikasi. |

$$\text{Skor Tugas 2} = 0,45(K_1) + 0,40(K_2) + 0,15(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-13` [C5])
**Objek Penilaian:** Repositori Git *Refactored Code + Automated Unit/Integration Tests* + Laporan Evaluasi **ISO/IEC 25010** (50%) & Sidang/Ujian Individu (50%).

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Evaluasi Objektif Kualitas Berstandar **ISO/IEC 25010****<br>(`Sub-CPMK-4.1`) | **35%** | Mengevaluasi $\ge 5$ karakteristik ISO/IEC 25010 menggunakan bukti metrik kuantitatif nyata (*$V(G)$, coupling, defect density, pass rate, coverage, response time*) disertai rekomendasi rekayasa yang tajam. | Evaluasi ISO/IEC 25010 didukung data pengujian nyata dan analisis kekuatan/kelemahan subsistem yang objektif. | Memetakan evaluasi ke karakteristik ISO/IEC 25010 dengan benar, namun sebagian penilaian masih kualitatif deskriptif. | Hanya menyalin definisi 8 karakteristik ISO/IEC 25010 tanpa mengukur subsistem yang diuji. | Laporan evaluasi kualitas ISO/IEC 25010 tidak ada atau fiktif. |
| **2. Kualitas & Cakupan *Automated Unit & Integration Testing***<br>(`Sub-CPMK-4.2`) | **35%** | Seluruh tes otomatis berjalan hijau (*CI passing*), berpola AAA bersih, tepat menggunakan *Mocking* untuk isolasi eksternal, mencakup *happy & edge/exception paths*, dengan *Branch Coverage* $\ge 80\%$ dan *assertions* bermakna. | Rangkaian *unit & integration tests* otomatis berjalan lancar, menggunakan *mocking* dasar, dan mencapai target *coverage* yang baik. | *Unit tests* otomatis berjalan untuk fungsi utama (*coverage* 65–79%), namun pengujian integrasi atau *mocking* masih terbatas. | Jumlah tes sangat sedikit, menguji hal sepele (*getter/setter*), atau gagal dieksekusi (*failing/broken tests*). | Tidak ada pengujian otomatis yang dapat dijalankan. |
| **3. Kualitas *Refactoring* SOLID & Kolaborasi Git SCM** | **15%** | Kode subsistem bersih patuh SOLID, *Pull Request* & *commit history* tiap anggota merata dan deskriptif, serta dilengkapi *workflow* pengujian otomatis. | Struktur kode rapi setelah *refactoring* dan riwayat *commit* Git seluruh anggota tim terverifikasi jelas. | Kode cukup modular namun sebagian commit dilakukan menumpuk menjelang tenggat (*bulk commit*). | Kode masih sarat *code smells* dan riwayat Git timpang hanya dikerjakan 1 orang. | Tidak menggunakan Git atau menyalin repositori pihak lain. |
| **4. Penguasaan Verifikasi *Live Testing* & Sidang Individu** | **15%** | Mahasiswa sigap menulis/memodifikasi *unit test* secara langsung saat diuji dan fasih menjelaskan hubungan metrik pengujian dengan standar ISO/IEC 25010. | Mahasiswa mampu mendemonstrasikan eksekusi tes dan menjawab pertanyaan penguji atas modulnya dengan tepat. | Mahasiswa mampu menjelaskan alur dasar kode uji yang ditulisnya dengan sedikit bantuan. | Tidak mampu menjelaskan cara kerja *assertion/mock* yang tertulis pada repositori timnya sendiri. | Tidak hadir sidang UAS atau melanggar kejujuran akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,15(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF BEDAH KODE (*CODE REVIEW*) & LATIHAN PENGUJIAN

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketajaman *Peer Code Review*** | Menemukan *code smells*, pelanggaran SOLID, dan celah kasus uji batas rekan secara spesifik dan santun. | Memberikan komentar *code review* yang relevan dan membantu perbaikan kode. | Mengikuti sesi *review* namun hanya memberi komentar permukaan (penamaan/indentasi). | Tidak berpartisipasi dalam latihan *code review* kelas. |
| **Disiplin *Test-First / TDD Mindset*** | Membiasakan menulis spesifikasi *assertion* gagal (*Red*) sebelum menulis implementasi fungsi (*Green*) lalu merapikan (*Refactor*). | Menulis *unit test* segera setelah merancang tiap fungsi modul. | Menulis *unit test* hanya di akhir pekan secara terburu-buru. | Enggan menulis skrip pengujian otomatis pada latihan mingguan. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-309` (`CPL-08` & `CPL-13` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa mampu menjustifikasi model proses proyek secara matang, merancang kode berarsitektur bersih patuh SOLID & GoF, merumuskan pengujian *White-Box* & *Black-Box* tanpa celah, serta membangun otomasi pengujian dan evaluasi mutu **ISO/IEC 25010** berstandar industri. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa menguasai pemilihan metodologi SDLC/Agile, penerapan arsitektur modular/SOLID/GoF, perancangan *Basis Path* & EP/BVA, serta eksekusi *automated testing* dan evaluasi ISO/IEC 25010 dengan akurat. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam memilih model proses, menerapkan prinsip modularitas dasar, menyusun skenario uji standar, dan menjalankan pengujian unit otomatis. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih menghasilkan rancangan ber-*coupling* tinggi, keliru menghitung *Cyclomatic Complexity* / batas BVA, dan belum mampu mengevaluasi mutu perangkat lunak secara objektif. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai prinsip dasar konstruksi dan pengujian perangkat lunak atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-309` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu memilih model proses pengembangan (*Waterfall, V-Model, Scrum, Kanban*) yang tepat sesuai risiko proyek. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu membandingkan dan menjustifikasi metodologi *Plan-Driven* vs *Agile* untuk kebutuhan industri. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu merancang arsitektur perangkat lunak modular dan menerapkan 5 prinsip **SOLID** dengan *coupling* rendah. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu me-*refactor Code Smells* dan menerapkan **GoF Design Patterns** secara proporsional. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu menggambar *Control Flow Graph*, menghitung **Cyclomatic Complexity**, dan menyusun uji **White-Box**. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu merancang skenario pengujian **Black-Box** menggunakan **Equivalence Partitioning** dan **BVA**. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu mengevaluasi kualitas perangkat lunak secara objektif berdasarkan 8 karakteristik **ISO/IEC 25010**. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu menulis dan mengevaluasi pengujian unit serta integrasi otomatis (*TDD, Mocking, Code Coverage*). | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-309`)

```text
==============================================================================================================================
             LEMBAR REKAPITULASI PENILAIAN OBE — STI-309 REKAYASA PERANGKAT LUNAK (3 SKS TEORI)
==============================================================================================================================
Semester / TA  : Semester 3 (Ganjil) / 2026-2027     CPL Dibebankan : CPL-08 (P4: 50%) & CPL-13 (KK5: 50%) [Level: Reinforce]
Klaster Rubrik : K-4 (Rekayasa & Mutu Software)      Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (30%)   | T2 (20%)    | UAS (30%)   | NA    | CPL-08 | CPL-13 | Huruf
   |           |                  | [CPMK-1:C4] | [CPMK-2:C3] | [CPMK-3:C4] | [CPMK-4:C5] | Akhir | (50%)  | (50%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 85.0        | 84.0        | 88.0        | 86.0        | 85.60 | 84.40  | 86.80  | A
2  | 250101002 | [Nama Mhs 2]     | 76.0        | 72.0        | 78.0        | 76.0        | 75.20 | 73.60  | 76.80  | B
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 67.80 | 66.80  | 68.80  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 76.33       | 74.00       | 78.67       | 76.67       | 76.20 | 74.93  | 77.47  | >=65:100%
==============================================================================================================================
```
