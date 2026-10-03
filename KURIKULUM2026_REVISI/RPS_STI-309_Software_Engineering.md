# RPS STI-309 — REKAYASA PERANGKAT LUNAK (*Software Engineering*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Nomor Dokumen:** 071030.B4.5.2.RPS-STI309  
**Tanggal Penyusunan:** 30 September 2026  
**Sumber:** Template Master RPS Generator FSTI UWG (`Template_RPS_GEN_2026_20092026-SWO.docx`) — seluruh 18 tag `{{...}}` + 25 tag `[...]` terisi; data dari Dok 003/005/007/008/043.  
**Keluaran pendamping:** `DOCX/RPS_STI-309_Software_Engineering.docx`

---

## HALAMAN 1 — IDENTITAS MATA KULIAH

| Atribut | Isi |
|---|---|
| Mata Kuliah (MK) | Rekayasa Perangkat Lunak (Software Engineering) |
| Kode | STI-309 |
| Rumpun MK | Rekayasa Perangkat Lunak & Platform (Core STI) |
| Bobot (sks) | T= 3, P= 0 (Total 3 SKS, Tipe Teori) |
| Semester | 3 (Ganjil) |
| Tgl Penyusunan | 30 September 2026 |
| Pengembang RPS | Tim KBK Rekayasa Perangkat Lunak & Platform |
| Koordinator RMK | Dr. Roni Wahyu, S.Kom., M.T. |
| Ketua Program Studi | [Nama Ketua Prodi SISTEKIN] |
| Matakuliah Syarat | FST-203 Struktur Data dan Algoritma |
| Dosen Pengampu | 1. [Nama Dosen Pengampu 1] (Koordinator MK)<br>2. [Nama Dosen Pengampu 2] |

## HALAMAN 2 — CAPAIAN PEMBELAJARAN (CP)

### CPL-PRODI yang Dibebankan pada MK

| No | Capaian Pembelajaran Lulusan (Dok 003) |
|:--:|---|
| **P4** | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). |
| **KK5** | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (Microservices, Web/Mobile, API, SaaS, BPA). |

### Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Bloom (Dok 043/007)

| No | Rumusan CPMK |
|:--:|---|
| **CPMK-1** | Mahasiswa (A) mampu memilih model proses pengembangan perangkat lunak (Waterfall, V-Model, Scrum, Kanban) (B) yang sesuai dengan karakteristik proyek industri (C) secara terjustifikasi (D). [C4] |
| **CPMK-2** | Mahasiswa (A) mampu menerapkan arsitektur perangkat lunak modular dan prinsip SOLID (B) pada perancangan subsistem software (C) dengan coupling rendah dan cohesion tinggi (D). [C3] |
| **CPMK-3** | Mahasiswa (A) mampu merancang skenario pengujian perangkat lunak White-Box (Basis Path, Cyclomatic Complexity) dan Black-Box (BVA, Equivalence Partitioning) (B) berdasarkan spesifikasi sistem (C) secara komprehensif (D). [C4] |
| **CPMK-4** | Mahasiswa (A) mampu mengevaluasi kualitas perangkat lunak (B) berdasarkan standar ISO/IEC 25010 dan metrik pengujian otomatis (C) secara objektif (D). [C5] |

### Tahapan Belajar (Sub-CPMK) — Dok 043

| No | Sub-CPMK |
|:--:|---|
| **Sub-CPMK-1.1** | Memilih model proses pengembangan perangkat lunak (Waterfall, V-Model, Scrum, Kanban) yang tepat. (C4) |
| **Sub-CPMK-1.2** | Membandingkan karakteristik model proses pengembangan untuk proyek industri. (C4) |
| **Sub-CPMK-2.1** | Menerapkan arsitektur perangkat lunak modular dan prinsip SOLID dengan coupling rendah. (C3) |
| **Sub-CPMK-2.2** | Menerapkan design pattern (GoF) pada perancangan subsistem perangkat lunak. (C3) |
| **Sub-CPMK-3.1** | Merancang skenario pengujian White-Box (basis path, cyclomatic complexity). (C4) |
| **Sub-CPMK-3.2** | Merancang skenario pengujian Black-Box (BVA, equivalence partitioning) berdasarkan spesifikasi. (C4) |
| **Sub-CPMK-4.1** | Mengevaluasi kualitas perangkat lunak berdasarkan standar ISO/IEC 25010. (C5) |
| **Sub-CPMK-4.2** | Mengevaluasi hasil pengujian unit dan integrasi secara otomatis dan objektif. (C5) |

### Korelasi CPL terhadap CPMK

| CPL | CPMK-1 | CPMK-2 | CPMK-3 | CPMK-4 | Instrumen & Bobot Asesmen |
|:--:|:--:|:--:|:--:|:--:|:--:|
| P4 | ✓ | ✓ |   |   | Tugas 1 (20%) + UTS (30%) = 50% |
| KK5 |   |   | ✓ | ✓ | Tugas 2 (20%) + UAS (30%) = 50% |

Skema 4x Titik Evaluasi Baku (Dok 008, tipe Teori): Tugas 1 Pekan 4 (20%), UTS Pekan 8 (30%), Tugas 2 Pekan 12 (20%), UAS Pekan 16 (30%) — total 100%.

### Deskripsi Singkat MK

Rekayasa Perangkat Lunak (STI-309) adalah mata kuliah wajib Core STI pada Semester 3 yang membekali mahasiswa dengan prinsip dan praktik rekayasa perangkat lunak modern. Mahasiswa memilih dan menjustifikasi model proses pengembangan (Waterfall, V-Model, Scrum, Kanban) sesuai karakteristik proyek industri; menerapkan arsitektur perangkat lunak modular (Layered, Client-Server, Event-Driven) dan prinsip SOLID dengan coupling rendah dan cohesion tinggi; menerapkan design patterns GoF; serta mendeteksi code smells dan melakukan refactoring. Pembelajaran menekankan kualitas: merancang skenario pengujian White-Box (basis path, cyclomatic complexity) dan Black-Box (equivalence partitioning, boundary value analysis), otomasi pengujian (unit testing, TDD, mocking), evaluasi kualitas perangkat lunak berdasarkan standar ISO/IEC 25010, manajemen konfigurasi perangkat lunak (Git branching & CI/CD), hingga penyusunan dokumen SQA Plan dan Test Execution Report. Sesuai Boundary Guardrails Dok 043, mata kuliah ini menerima dokumen spesifikasi analisis dan desain (SRS & SDD) dari STI-306 Analisis dan Perancangan Sistem Informasi, serta menyerahkan integrasi arsitektur cloud kepada STI-417 Komputasi Awan dan penjaminan mutu formal kepada FST-712.

### Bahan Kajian: Materi Pembelajaran

1. BK-IS07 Systems Analysis and Design — prinsip rekayasa perangkat lunak, model proses pengembangan, arsitektur dan desain modular perangkat lunak.

2. BK-IT11 Software Development Practices — praktik pengembangan perangkat lunak: clean code, refactoring, design patterns, pengujian, dan manajemen konfigurasi.

Pokok Bahasan: (1) Pengantar RPL, krisis software & SWEBOK; (2) Model Proses Tradisional: Waterfall, Incremental, V-Model; (3) Model Proses Adaptif: Agile Manifesto, Scrum Sprint, Kanban; (4) Arsitektur Perangkat Lunak: Monolitik, Layered, Client-Server, Pipe-Filter; (5) Refactoring & Kepatuhan 5 Prinsip SOLID; (6) Code Smells & Teknik Refactoring; (7) Design Patterns GoF (Creational, Structural, Behavioral); (8) SQA & Standar ISO/IEC 25010; (9) White-Box Testing: Flow Graph, Cyclomatic Complexity, Coverage; (10) Black-Box Testing: Equivalence Partitioning & Boundary Value Analysis; (11) Otomasi Pengujian: Unit Testing, TDD, Mocking Framework; (12) Integration, Regression & Stress/Load Testing; (13) Software Configuration Management: Git Branching & CI/CD; (14) SQA Plan & Test Execution Report.

### Pustaka

**Utama:**

1. Sommerville, I. (2016). Software Engineering (10th ed.). Boston: Pearson.
2. Pressman, R. S., & Maxim, B. R. (2020). Software Engineering: A Practitioner's Approach (9th ed.). New York: McGraw-Hill Education.
3. ISO/IEC (2011). ISO/IEC 25010:2011 — Systems and Software Quality Requirements and Evaluation (SQuaRE): System and Software Quality Models. Geneva: ISO.
4. Bourque, P., & Fairley, R. E. (2014). Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) Version 3.0. IEEE Computer Society. https://www.computer.org/education/bodies-of-knowledge/software-engineering
5. Martin, R. C. (2018). Clean Architecture: A Craftsman's Guide to Software Structure and Design. Boston: Prentice Hall.

**Pendukung:**

6. Martin, R. C. (2008). Clean Code: A Handbook of Agile Software Craftsmanship. Boston: Prentice Hall.
7. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). Design Patterns: Elements of Reusable Object-Oriented Software. Boston: Addison-Wesley.
8. Beck, K. (2003). Test-Driven Development: By Example. Boston: Addison-Wesley.
9. Chacon, S., & Straub, B. (2014). Pro Git (2nd ed.). New York: Apress. https://git-scm.com/book
10. Myers, G. J., Sandler, C., & Badgett, T. (2011). The Art of Software Testing (3rd ed.). Hoboken: John Wiley & Sons.
11. Fowler, M. (2018). Refactoring: Improving the Design of Existing Code (2nd ed.). Boston: Addison-Wesley.
12. Schwaber, K., & Sutherland, J. (2020). The Scrum Guide: The Definitive Guide to Scrum. https://scrumguides.org

---

## HALAMAN 3-4 — RENCANA PEMBELAJARAN 16 PEKAN

| Mg ke- | Kemampuan Akhir Tahapan Belajar (Sub-CPMK) | Indikator | Kriteria & Teknik | Luring (offline) | Daring (online) | Materi Pembelajaran [Pustaka] | Bobot Penilaian (%) |
|:--:|---|---|---|---|---|---|:--:|
| 1 | Pengantar MK & Orientasi — Mampu menguraikan krisis software dan standar IEEE SWEBOK (C2) | Peta konsep RPL & SWEBOK tersusun; kontrak belajar dan skema asesmen disepakati | Checklist formatif; observasi partisipasi | Kuliah & Diskusi 150' | Edlink: modul pengantar & kontrak belajar; forum diskusi | Pengantar Rekayasa Perangkat Lunak, Evolusi Kualitas Software, SWEBOK [1][4] | — |
| 2 | Sub-CPMK-1.1: Mampu memilih model proses pengembangan yang tepat (C4) | Matriks karakteristik Waterfall, Incremental, V-Model (kelebihan/kekurangan/konteks) benar | Rubrik kompilasi formatif; kuis Edlink | Ceramah & Analisis Kasus 150' | Edlink: studi kasus proyek industri; forum analisis | Model Proses Tradisional: Waterfall, Incremental, V-Model [1][2] | — |
| 3 | Sub-CPMK-1.2: Mampu membandingkan karakteristik model proses tradisional dan adaptif untuk proyek industri (C4) | Pemetaan peran, artefak, dan sprint Scrum/Kanban pada studi kasus tepat | Rubrik kompilasi formatif; presentasi kasus singkat | Case Method Class 150' | Edlink: video Agile/Scrum; tugas analisis kasus | Model Proses Adaptif: Agile Manifesto, Scrum Sprint, Kanban [2][12] | — |
| 4 | Sub-CPMK-2.1: Mampu menganalisis pola arsitektur Layered, Client-Server, Event-Driven (C4) | Justifikasi pemilihan pola arsitektur untuk studi kasus diterima (rubrik Tugas 1) | Rubrik analitik Tugas 1 | Problem-Solving Class 150' | Edlink: pengumpulan Tugas 1 via Edlink | Arsitektur Perangkat Lunak: Monolitik, Layered, Client-Server, Pipe-Filter [1][5] | Tugas 1: 20% (Problem Solving Model Proses & Arsitektur — evaluasi Sub-CPMK Pekan 2–4) |
| 5 | Sub-CPMK-2.1: Mampu menerapkan prinsip SOLID pada desain kode perangkat lunak (C3) | Kode studi kasus patuh 5 prinsip SOLID tanpa pelanggaran kritis | Rubrik kompilasi formatif; review kode | Case-Based Workshop 150' | Edlink: starter code; commit repo mingguan | Refactoring Kode & Kepatuhan 5 Prinsip Desain SOLID [6][11] | — |
| 6 | Sub-CPMK-2.1: Mampu menganalisis code smells dan teknik refactoring sistematis (C4) | Minimal 3 code smell terdeteksi dan direfaktor dengan alasan terdokumentasi | Rubrik kompilasi formatif; demo refactoring | Problem-Based Learning 150' | Edlink: latihan code smell; forum review kode | Mendeteksi Code Smells: Long Method, Large Class, Duplikasi [11] | — |
| 7 | Sub-CPMK-2.2: Mampu menerapkan pola desain GoF (Creational, Structural, Behavioral) (C3) | Minimal 2 design pattern GoF diterapkan tepat konteks pada studi kasus | Rubrik kompilasi formatif; presentasi pola | Case Method Class 150' | Edlink: contoh kasus pattern; forum diskusi | Design Patterns dalam Arsitektur Software Skala Besar [7] | — |
| **8** | Evaluasi Tengah Semester (UTS) — Ujian Tertulis Terjadwal: Analisis Model Proses, Arsitektur Software, & Prinsip SOLID (CPMK-1 s.d. CPMK-2) | Indikator: Skor ujian tertulis ≥ 70; jawaban analisis model proses, arsitektur, dan SOLID memenuhi rubrik.<br>Kriteria & Teknik: Rubrik analitik UTS; ujian tertulis terjadwal (150').<br>Luring: Ujian Tertulis Terjadwal (150').<br>Daring: Edlink — pengumuman ruang ujian & unggah berkas.<br>Materi: Cakupan Mg 1–7 — model proses, arsitektur, SOLID, code smells, design patterns [1][2][5][7].<br>Bobot Penilaian: UTS 30%. |
| 9 | Sub-CPMK-4.1: Mampu menguraikan 8 karakteristik kualitas standar ISO/IEC 25010 (C2) | 8 karakteristik kualitas dipetakan ke contoh produk software nyata | Rubrik kompilasi formatif; kuis Edlink | Kuliah & Diskusi 150' | Edlink: modul SQA; forum diskusi | Software Quality Assurance (SQA) & Standar ISO/IEC 25010 [3] | — |
| 10 | Sub-CPMK-3.1: Mampu menghitung Cyclomatic Complexity dan merancang Basis Path Testing (C4) | Flow graph dan V(G) dihitung benar; test case basis path lengkap | Rubrik kompilasi formatif; penilaian latihan | Problem-Solving Class 150' | Edlink: latihan flow graph; kuis | White-Box Testing: Flow Graph, Cyclomatic Complexity, Coverage [10] | — |
| 11 | Sub-CPMK-3.2: Mampu merancang uji Black-Box via Equivalence Partitioning dan BVA (C4) | Kelas ekuivalensi dan nilai batas dirancang lengkap dari spesifikasi | Rubrik kompilasi formatif; penilaian latihan | Case-Based Learning 150' | Edlink: spesifikasi kasus uji; forum diskusi | Black-Box Testing: Equivalence Partitioning & Boundary Value Analysis [10] | — |
| 12 | Sub-CPMK-3.1 & 4.2: Mampu menerapkan strategi Unit Testing dan Test-Driven Development (C3) | Siklus TDD (red-green-refactor) didemonstrasikan; unit test lulus | Rubrik analitik Tugas 2 | Workshop Koding 150' | Edlink: pengumpulan Tugas 2 via Edlink | Otomasi Pengujian: Unit Testing, TDD, Mocking Framework [8] | Tugas 2: 20% (Studi Kasus Otomasi Pengujian & TDD — evaluasi Sub-CPMK Pekan 9–12) |
| 13 | Sub-CPMK-4.2: Mampu merancang pengujian integrasi dan System Stress Testing (C4) | Skenario integration/regression/stress test dirancang untuk studi kasus | Rubrik kompilasi formatif; review rancangan | Problem-Solving Class 150' | Edlink: studi kasus integrasi; forum | Integration Testing, Regression Testing, Stress/Load Testing [2][10] | — |
| 14 | Sub-CPMK-4.2: Mampu menguraikan manajemen konfigurasi perangkat lunak (SCM) dan Git (C2) | Alur branching Git dan pipeline CI/CD konsep dijelaskan benar | Rubrik kompilasi formatif; demonstrasi Git | Ceramah & Demo 150' | Edlink: tutorial Git; demo pipeline | Software Configuration Management: Git Branching & CI/CD Konsep [9] | — |
| 15 | Sub-CPMK-4.1 & 4.2: Mampu menyusun Test Plan dan laporan audit kualitas software tim (C5) | Dokumen SQA Plan dan Test Execution Report tersusun dan dipresentasikan | Rubrik kompilasi presentasi; penilaian antar-tim | Presentasi Kelompok 150' | Edlink: unggah dokumen SQA Plan; umpan balik | Penyusunan Dokumen SQA Plan & Test Execution Report [2][3] | — |
| **16** | Evaluasi Akhir Semester (UAS) — Ujian Tertulis Komprehensif: Desain Arsitektur, Pengujian White/Black Box, & SQA (Seluruh CPMK) | Indikator: Skor ujian komprehensif ≥ 70; jawaban desain arsitektur, pengujian, dan audit kualitas memenuhi rubrik.<br>Kriteria & Teknik: Rubrik analitik UAS; ujian tertulis komprehensif (150').<br>Luring: Ujian Tertulis Akhir (150').<br>Daring: Edlink — pengumuman ruang ujian & unggah berkas.<br>Materi: Cakupan seluruh Sub-CPMK — desain arsitektur, pengujian White/Black Box, SQA [1][2][3][10].<br>Bobot Penilaian: UAS 30%. |
| | **Total bobot penilaian** | | | | | | **100%** |

---

## LAMPIRAN — INSTRUMEN ASESMEN

> Seluruh instrumen lampiran (4 soal + 4 rubrik) merupakan **komposisi baru** mengikuti gaya pilot RPS — Dok 007 tidak menyediakan naskah soal/rubrik; wajib validasi KBK/GPM.

TUGAS 1 — PROBLEM SOLVING: MODEL PROSES & ARSITEKTUR PERANGKAT LUNAK (Pekan 4, Bobot 20%)

Mahasiswa menganalisis satu studi kasus proyek perangkat lunak industri yang diberikan dosen (mis. sistem informasi layanan publik), membandingkan model proses pengembangan, dan merancang arsitektur perangkat lunak modular.

Spesifikasi wajib: (1) matriks perbandingan minimal 3 model proses (Waterfall, V-Model, Scrum, Kanban) menurut minimal 4 dimensi (ruang lingkup, keterlibatan pengguna, toleransi perubahan, risiko); (2) justifikasi pemilihan model proses terhadap karakteristik proyek; (3) diagram arsitektur (Layered/Client-Server/Event-Driven) lengkap dengan tanggung jawab tiap lapisan; (4) pemetaan prinsip SOLID pada rancangan subsistem; (5) laporan maksimal 6 halaman.

Deliverable: dokumen PDF laporan + diagram. Cakupan evaluasi: Sub-CPMK-1.1, 1.2, dan 2.1 (Pekan 2–4) → CPMK-1 dan CPMK-2 (CPL P4). Penilaian menggunakan rubrik analitik berikut. (Instrumen komposisi baru — perlu validasi KBK/GPM.)

**Rubrik Penilaian Tugas 1 (Total 100)**

| Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (66–75) | Kurang (56–65) | Sangat Kurang (0–55) |
|---|---|---|---|---|---|---|
| Matriks Perbandingan Model Proses | 20% | ≥ 3 model × ≥ 4 dimensi lengkap & tepat | Perbandingan tepat, 1 dimensi kurang | Perbandingan dasar berfungsi | Perbandingan dangkal | Tidak ada matriks |
| Justifikasi Pemilihan Model Proses | 20% | Justifikasi terukur & berbasis karakteristik proyek | Justifikasi logis, argumen kurang tajam | Justifikasi dapat diterima | Justifikasi lemah | Tanpa justifikasi |
| Diagram Arsitektur & Demarkasi Lapisan | 25% | Arsitektur modular tepat, tanggung jawab lapisan jelas | Diagram benar, 1 lapisan kabur | Diagram dasar berfungsi | Lapisan tercampur | Tidak ada diagram |
| Pemetaan Prinsip SOLID | 20% | 5 prinsip terpetakan tepat ke rancangan | 4 prinsip tepat | 3 prinsip tepat | Pemetaan salah arah | Tidak memetakan |
| Kualitas Dokumentasi | 15% | Laporan rapi, sitasi pustaka lengkap | Laporan baik, minor kelalaian | Laporan dapat dipahami | Laporan berantakan | Tidak ada laporan |

UJIAN TENGAH SEMESTER (Pekan 8, Bobot 30%) — UJIAN TERTULIS TERJADWAL (150 MENIT)

Cakupan: Mg 1–7 — model proses pengembangan, arsitektur perangkat lunak, prinsip SOLID, code smells & refactoring, design patterns (CPMK-1 s.d. CPMK-2).

Soal: (1) analisis kasus: pilih dan justifikasi model proses untuk proyek yang dideskripsikan (essay); (2) sketsa arsitektur Layered untuk studi kasus beserta tanggung jawab tiap lapisan; (3) identifikasi pelanggaran SOLID pada potongan kode yang diberikan dan usulkan refactoring; (4) pilih design pattern GoF yang tepat untuk dua kasus dan gambarkan strukturnya; (5) daftar code smells pada potongan kode dan tindakan perbaikannya.

Ketentuan: ujian tertulis individual, tertutup; kriteria ketuntasan minimal skor 70. (Instrumen komposisi baru — perlu validasi KBK/GPM.)

**Rubrik Penilaian UTS (Total 100)**

| Kriteria | Bobot | Poin Penuh | Poin Sebagian | Poin Minimal | Tidak Ada |
|---|---|---|---|---|---|
| Analisis & Pemilihan Model Proses | 25% | 25 | 17 | 9 | 0 |
| Diagram Arsitektur Layered | 25% | 25 | 17 | 9 | 0 |
| Analisis SOLID & Usulan Refactoring | 20% | 20 | 13 | 7 | 0 |
| Penerapan Design Pattern GoF | 15% | 15 | 10 | 5 | 0 |
| Deteksi Code Smell | 15% | 15 | 10 | 5 | 0 |

TUGAS 2 — STUDI KASUS OTOMASI PENGUJIAN & TEST-DRIVEN DEVELOPMENT (Pekan 12, Bobot 20%)

Mahasiswa merancang dan mengimplementasikan pengujian otomatis untuk satu modul studi kasus perangkat lunak menggunakan pendekatan Test-Driven Development, lalu mengevaluasi hasilnya terhadap standar kualitas.

Spesifikasi wajib: (1) siklus TDD (red-green-refactor) terdokumentasi untuk minimal 5 fitur/unit; (2) perhitungan cyclomatic complexity dan perancangan test case basis path untuk satu fungsi kunci; (3) perancangan kelas ekuivalensi dan Boundary Value Analysis untuk satu fungsi berbasis spesifikasi; (4) evaluasi kualitas hasil pengujian terhadap minimal 4 karakteristik ISO/IEC 25010; (5) versi kode dikelola dengan Git (commit terstruktur).

Deliverable: repository Git + laporan pengujian maksimal 6 halaman. Cakupan evaluasi: Sub-CPMK-3.1, 3.2, 4.1, dan 4.2 (Pekan 9–12) → CPMK-3 dan CPMK-4 (CPL KK5). Penilaian menggunakan rubrik analitik berikut. (Instrumen komposisi baru — perlu validasi KBK/GPM.)

**Rubrik Penilaian Tugas 2 (Total 100)**

| Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (66–75) | Kurang (56–65) | Sangat Kurang (0–55) |
|---|---|---|---|---|---|---|
| Siklus TDD & Kelengkapan Unit Test | 25% | Siklus terdokumentasi utuh, ≥ 5 unit teruji | Siklus utuh, 4 unit | 3 unit teruji | Test tidak berkala | Tanpa unit test |
| Cyclomatic Complexity & Basis Path | 20% | V(G) benar, test case lengkap | V(G) benar, test case kurang 1 | V(G) sebagian benar | Perhitungan salah | Tidak menghitung |
| Kelas Ekuivalensi & BVA | 20% | Partisi & nilai batas lengkap dan tepat | Partisi tepat, 1–2 BVA kurang | Partisi dasar berfungsi | Partisi salah | Tidak dirancang |
| Evaluasi Kualitas ISO/IEC 25010 | 15% | ≥ 4 karakteristik dievaluasi berbukti | 4 karakteristik, bukti kurang | 3 karakteristik | Evaluasi dangkal | Tidak dievaluasi |
| Kualitas Kode & SCM (Git) | 20% | Commit terstruktur, kode bersih | Commit teratur, minor isu | Repo ada dan jalan | Riwayat commit kacau | Tanpa version control |

UJIAN AKHIR SEMESTER (Pekan 16, Bobot 30%) — UJIAN TERTULIS KOMPREHENSIF (150 MENIT)

Cakupan: seluruh CPMK — desain arsitektur perangkat lunak, pengujian White-Box dan Black-Box, serta Software Quality Assurance.

Soal: (1) studi kasus: rancang arsitektur modular untuk sistem yang dideskripsikan dan pilih design pattern yang mendukungnya (essay + diagram); (2) soal pengujian White-Box: bangun flow graph, hitung cyclomatic complexity, dan susun test case basis path; (3) soal pengujian Black-Box: rancang kelas ekuivalensi dan BVA dari spesifikasi yang diberikan; (4) audit kualitas: nilai produk software terhadap 8 karakteristik ISO/IEC 25010 dan usulkan perbaikan; (5) susun kerangka SQA Plan singkat untuk proyek studi kasus.

Ketentuan: ujian tertulis individual, tertutup; kriteria ketuntasan minimal skor 70. (Instrumen komposisi baru — perlu validasi KBK/GPM.)

**Rubrik Penilaian UAS (Total 100)**

| Kriteria | Bobot | Poin |
|---|---|---|
| Desain arsitektur modular & design pattern | 25% | 25 |
| Pengujian White-Box (flow graph, V(G), basis path) | 25% | 25 |
| Pengujian Black-Box (equivalence partitioning, BVA) | 20% | 20 |
| SQA & audit ISO/IEC 25010 | 20% | 20 |
| Kerangka SQA Plan & SCM/CI-CD konsep | 10% | 10 |

---

## PENGESAHAN

| Memvalidasi, Unit Penjaminan Mutu FSTI | Malang, 30 September 2026 — Dosen Pengampu |
|---|---|
| Nama Pejabat UPM: [Nama Kepala UPM FSTI] | [Nama Dosen Pengampu STI-309] / NUPTK. [NUPTK Dosen] |

Mengesahkan, Ketua Program Studi Sistem dan Teknologi Informasi: [Nama Ketua Prodi SISTEKIN]

---

*RPS STI-309 dibangkitkan dari Template Master RPS Generator FSTI UWG oleh `_tools/generate_rps_sti309_docx.py` — unit ke-3 RPS Batch Generator (setelah STI-416 V2 & STI-311).*
