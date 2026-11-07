# 063_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-309 — REKAYASA PERANGKAT LUNAK (*Software Engineering*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017 · IEEE SWEBOK v4)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI309`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, 043, & Pilot `STI-309`) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Rekayasa Perangkat Lunak / *Software Engineering* |
| **Kode Mata Kuliah** | `STI-309` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Rekayasa Perangkat Lunak & Platform (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS Teori** (`T = 3, P = 0`) — Tatap Muka `3×50' = 150'`, Penugasan Terstruktur `3×60' = 180'`, Belajar Mandiri `3×60' = 180'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Arsitektur, Konstruksi, & Penjaminan Mutu (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `FST-203` Struktur Data dan Algoritma |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Menerima cetak biru SRS/SDD dari `STI-306` Analisis dan Perancangan Sistem Informasi; menyerahkan ke `STI-416` Pengembangan Web Back End, `STI-523` Manajemen Proyek TI, `STI-625` Rekayasa Platform Digital, & `FST-610` Capstone Project FSTI |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-08` (`P4` = **50%**) dan `CPL-13` (`KK5` = **50%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 4 (`K-4`)** — Sintesis, Rekayasa Sistem & Mutu Perangkat Lunak (Bobot: Tugas 1 `20%` · UTS `30%` · Tugas 2 `20%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Rekayasa Perangkat Lunak & Platform |
| **Koordinator RMK** | Dr. Roni Wahyu, S.Kom., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-08`** (`P4`) | Pengetahuan | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | **R** (*Reinforce*) | **50%** |
| **`CPL-13`** (`KK5`) | Keterampilan Khusus | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | **R** (*Reinforce*) | **50%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **memilih** model proses pengembangan perangkat lunak (*Waterfall, V-Model, Scrum, Kanban*) (*B*) yang sesuai dengan karakteristik proyek industri (*C*) secara terjustifikasi (*D*). | **C4** (*Analyze*) | `CPL-08` (`P4`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **menerapkan** arsitektur perangkat lunak modular dan prinsip **SOLID** (*B*) pada perancangan subsistem software (*C*) dengan *coupling* rendah dan *cohesion* tinggi (*D*). | **C3** (*Apply*) | `CPL-08` (`P4`) | **UTS — Pekan 8 (30%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **merancang** skenario pengujian perangkat lunak *White-Box* (*Basis Path, Cyclomatic Complexity*) dan *Black-Box* (*BVA, Equivalence Partitioning*) (*B*) berdasarkan spesifikasi sistem (*C*) secara komprehensif (*D*). | **C4** (*Analyze*) | `CPL-13` (`KK5`) | **Tugas 2 — Pekan 12 (20%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **mengevaluasi** kualitas perangkat lunak (*B*) berdasarkan standar **ISO/IEC 25010** dan metrik pengujian otomatis (*C*) secara objektif (*D*). | **C5** (*Evaluate*) | `CPL-13` (`KK5`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Memilih model proses pengembangan perangkat lunak (*Waterfall, V-Model, Scrum, Kanban*) yang tepat. | `CPMK-1` | **C4** | Mg 1–2 |
| **`Sub-CPMK-1.2`** | Membandingkan karakteristik model proses pengembangan untuk proyek industri. | `CPMK-1` | **C4** | Mg 3 |
| **`Sub-CPMK-2.1`** | Menerapkan arsitektur perangkat lunak modular dan prinsip **SOLID** dengan *coupling* rendah. | `CPMK-2` | **C3** | Mg 4–6 |
| **`Sub-CPMK-2.2`** | Menerapkan *design pattern* (**GoF**) pada perancangan subsistem perangkat lunak. | `CPMK-2` | **C3** | Mg 6–7 |
| **`Sub-CPMK-3.1`** | Merancang skenario pengujian *White-Box* (*basis path, cyclomatic complexity*). | `CPMK-3` | **C4** | Mg 10 |
| **`Sub-CPMK-3.2`** | Merancang skenario pengujian *Black-Box* (*BVA, equivalence partitioning*) berdasarkan spesifikasi. | `CPMK-3` | **C4** | Mg 11 |
| **`Sub-CPMK-4.1`** | Mengevaluasi kualitas perangkat lunak berdasarkan standar **ISO/IEC 25010**. | `CPMK-4` | **C5** | Mg 9 & 14–15 |
| **`Sub-CPMK-4.2`** | Mengevaluasi hasil pengujian unit dan integrasi secara otomatis dan objektif. | `CPMK-4` | **C5** | Mg 12–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Evaluasi Kualitas Perangkat Lunak ISO/IEC 25010 & Metrik Pengujian Otomatis (C5) — Mg 9 & 12–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: 8 Karakteristik Mutu ISO/IEC 25010 & SQA Plan | Sub-CPMK-4.2: Unit/Integration Testing, TDD, Mocking, Coverage)
      │
[CPMK-3: Perancangan Skenario Uji White-Box & Black-Box Komprehensif (C4) — Mg 10–12 (Tugas 2 20%)]
      ▲  (Sub-CPMK-3.1: Control Flow Graph, Cyclomatic Complexity V(G), Basis Path | Sub-CPMK-3.2: Equivalence Partitioning & BVA)
      │
[CPMK-2: Arsitektur Modular, Prinsip SOLID, Refactoring, & Design Patterns GoF (C3) — Mg 4–8 (UTS 30%)]
      ▲  (Sub-CPMK-2.1: Layered/MVC/Event-Driven, Low Coupling-High Cohesion, SOLID | Sub-CPMK-2.2: Code Smells & GoF Patterns)
      │
[CPMK-1: Pemilihan & Justifikasi Model Proses Pengembangan Perangkat Lunak (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: SWEBOK, Waterfall, Incremental, V-Model | Sub-CPMK-1.2: Agile Manifesto, Scrum Sprint, & Kanban)
      ▲
[Fondasi Prasyarat: FST-203 Struktur Data dan Algoritma + Sinergi Cetak Biru SRS/SDD dari STI-306]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-08`** (`P4`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-08` = 50%** |
| **`CPL-08`** (`P4`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **30%** | — | — | **30%** | *(20% + 30%)* |
| **`CPL-13`** (`KK5`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **20%** | — | **20%** | **`CPL-13` = 50%** |
| **`CPL-13`** (`KK5`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | *(20% + 30%)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **30%** | **20%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 50\%$):** `Tugas 1 (20% — Case-Based Process Model Justification) + UTS Studi Kasus Refactoring SOLID/GoF (atau 5% komponen kasus) + Tugas 2 (20% — Case-Based White/Black-Box Test Suite Design) + UAS (30% — Team-Based SQA Audit, Automated Unit/Integration Test Report & Defense)` = **75%** *(persis selaras dengan angka tabel IKU 7 Dokumen 004 untuk `STI-309` = 75%)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-309 Rekayasa Perangkat Lunak` (3 SKS Teori) berfokus pada **bagaimana membangun, menata arsitektur kode, dan menguji kualitas perangkat lunak secara benar dan terukur (*How to build and test software correctly*)**. Mahasiswa mempelajari standar profesi **IEEE SWEBOK**, analisis pemilihan model proses pengembangan (*Waterfall, V-Model, Spiral, Agile Scrum, Kanban*), pola arsitektur perangkat lunak (*Monolithic, Layered, MVC, Event-Driven*), prinsip kualitas konstruksi **Clean Code & SOLID** (*Low Coupling, High Cohesion*), deteksi *Code Smells* dan *Refactoring*, penerapan **GoF Design Patterns** (*Creational, Structural, Behavioral*), perancangan pengujian sistematis **White-Box** (*Control Flow Graph, Cyclomatic Complexity $V(G)$, Basis Path*) dan **Black-Box** (*Equivalence Partitioning, Boundary Value Analysis, Decision Table*), otomasi **Unit & Integration Testing** (*TDD, Mocking, Code Coverage*), manajemen konfigurasi **Git Branching & CI Dasar**, hingga evaluasi mutu komprehensif berstandar **ISO/IEC 25010**.

* **🟢 IN-SCOPE (Wajib Diajarkan):** Model proses SDLC & *Agile Scrum/Kanban*, pola arsitektur perangkat lunak, *Clean Code*, 5 prinsip **SOLID**, *Code Smells & Refactoring*, **GoF Design Patterns**, *Software Quality Assurance* (**ISO/IEC 25010**), pengujian **White-Box** & **Black-Box**, otomasi *Unit/Integration Testing* (`Pytest`/`Jest`/`JUnit`, TDD, *Mocking*, *Code Coverage*), *Git SCM Workflow*, dan penyusunan **SQA Plan & Automated Test Execution Report**.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. **Dilarang mengulang** elisitasi wawancara pemangku kepentingan, pemodelan BPMN 2.0, maupun penyusunan dokumen SRS dari nol (ranah eksklusif **`STI-306 Analisis dan Perancangan Sistem Informasi`**; proyek `STI-309` wajib bertolak dari spesifikasi siap pakai dan menghasilkan *Refactored Code + Test Suite & SQA Report*, bukan dokumen SRS!).
  2. Dilarang membahas penganggaran biaya proyek, *Earned Value Management* (EVM), *Critical Path Method* (CPM), serta manajemen pengadaan/kontrak hukum TI (ranah eksklusif **`STI-523 Manajemen Proyek TI`**).
* **🔄 HANDOFF ANCHOR:** Menerima spesifikasi SRS/SDD dari `STI-306`, memperkuat disiplin rekayasa kode bagi `STI-311` dan `STI-416 Pengembangan Web Back End`, serta menyerahkan tata kelola jadwal/biaya proyek ke **`STI-523 Manajemen Proyek TI`** dan rekayasa *microservices* skala besar ke **`STI-625 Rekayasa Platform Digital`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS07` (*Systems Analysis and Design*) & `BK-IT11` (*Software Development Practices*).

**Pustaka Utama:**
1. Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.
2. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson.
3. Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design* & *Clean Code* (2008). Prentice Hall.
4. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.

**Pustaka Pendukung & Standar Internasional:**
5. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994) / Freeman, E., & Robson, E. (2020). *Head First Design Patterns* (2nd ed.). O'Reilly.
6. ISO/IEC 25010:2011 / 2023 — *Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE)*; IEEE Computer Society *SWEBOK Guide v4.0* (2024); Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Pengantar):** Menguraikan krisis perangkat lunak, area pengetahuan **IEEE SWEBOK**, dan posisi `STI-309` [C2→C4] | 1.1.1 Ketepatan menganalisis penyebab kegagalan konstruksi & mutu *software* (*technical debt*).<br>1.1.2 Ketepatan membedakan lingkup `STI-306` (*What to build*) vs `STI-309` (*How to build & verify quality*). | **Kriteria:** Kuis diagnostik formatif.<br>**Teknik:** Diskusi kasus kegagalan kualitas perangkat lunak kritis (*Ariane 5 / Knight Capital / CrowdStrike*). | **Kuliah Interaktif & Bedah Insiden Industri**<br>`[TM: 3×50' = 150']`<br>Telaah ringkas area pengetahuan IEEE SWEBOK:<br>`[PT: 180']` · `[BM: 180']` | Kontrak belajar, unduh modul & repositori *legacy code* studi kasus di LMS Edlink. | Krisis Kualitas Perangkat Lunak, *Technical Debt*, Standar Profesi **IEEE SWEBOK**, & Kontrak Belajar `[1] Bab 1; [2] Bab 1; [6]` | — |
| **2** | **`Sub-CPMK-1.1`:** Memilih dan menganalisis model proses tradisional/terencana (*Waterfall, Incremental, Spiral, & V-Model*) [C4] | 1.1.3 Ketepatan membandingkan kekuatan dan kelemahan *Waterfall, Incremental, Spiral* (berbasis risiko), serta **V-Model** (korespondensi tiap fase desain dengan level pengujian). | **Kriteria:** Ketepatan matriks kesesuaian proyek.<br>**Teknik:** Analisis kasus pemilihan model proses untuk sistem regulasi ketat/keselamatan kritis. | **Ceramah Interaktif & Analisis Kasus**<br>`[TM: 3×50' = 150']`<br>Pemetaan karakteristik proyek ke model *Plan-Driven*:<br>`[PT: 180']` · `[BM: 180']` | Kuis pemahaman korespondensi uji pada *V-Model* di LMS Edlink. | Model Proses *Plan-Driven*: *Waterfall*, *Incremental*, *Risk-Driven Spiral*, & **V-Model** `[1] Bab 2 & 4; [2] Bab 2` | — |
| **3** | **`Sub-CPMK-1.2`:** Membandingkan dan menerapkan kerangka proses adaptif (**Agile Manifesto, Scrum Framework, & Kanban**) untuk proyek industri [C4] | 1.2.1 Ketepatan menguraikan 3 peran, 5 acara (*Sprint, Sprint Planning, Daily Scrum, Sprint Review, Retrospective*), 3 artefak Scrum + *Definition of Done* (DoD), serta *WIP Limit* pada Kanban.<br>1.2.2 Ketepatan menjustifikasi pilihan model proses (*Plan-Driven vs Agile vs Hybrid*) berdasarkan matriks ketidakpastian kebutuhan, risiko, dan skala tim. | **Kriteria:** Ketajaman argumen justifikasi.<br>**Teknik:** Simulasi *Sprint Planning & Kanban WIP* di kelas. | **Case Method Class (*Agile vs Plan-Driven*)**<br>`[TM: 3×50' = 150']`<br>Penyusunan makalah analisis pemilihan model proses untuk **Tugas 1**:<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi instruksi **Tugas 1 (RTM-1)** di LMS Edlink. | *Agile Software Development*: *Agile Manifesto*, **Scrum Guide 2020** (*Roles, Events, Artifacts, DoD*), **Kanban** (*WIP Limits, Lead/Cycle Time*), & Matriks Keputusan Pemilihan Proses `[1] Bab 3; [2] Bab 3; [6]` | — |
| **4** | **`Sub-CPMK-2.1`:** Menerapkan gaya arsitektur perangkat lunak modular (*Monolithic, Layered, MVC, Client-Server, Event-Driven*) dengan *low coupling* & *high cohesion* [C3]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 2.1.1 Ketepatan mengevaluasi *trade-off* arsitektur *Modular Monolith, Layered Architecture, MVC,* dan *Event-Driven*.<br>2.1.2 Ketepatan mengukur dan memperbaiki tingkat *coupling* dan *cohesion* antar-modul. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-4`)**.<br>**Teknik:** Pengumpulan Studi Kasus Justifikasi Model Proses + Kuis Verifikasi Kelas 20'. | **Problem-Solving Arsitektur & Verifikasi Tugas 1**<br>`[TM: 3×50' = 150']`<br>Dekomposisi subsistem *spaghetti* ke arsitektur berlapis:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Gaya Arsitektur Perangkat Lunak (*Layered, MVC, Pipe-and-Filter, Event-Driven*) & Prinsip Modularitas (*Low Coupling, High Cohesion*) `[1] Bab 10; [2] Bab 6; [3]` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1`:** Menerapkan 5 prinsip desain berorientasi objek **SOLID** pada perancangan dan perbaikan subsistem perangkat lunak [C3] | 2.1.3 Ketepatan mendiagnosis pelanggaran **SRP, OCP, LSP, ISP,** dan **DIP** pada potongan kode berorientasi objek.<br>2.1.4 Ketepatan merancang ulang antarmuka/kelas agar mematuhi *Dependency Inversion* & *Open-Closed Principle*. | **Kriteria:** Ketepatan perbaikan struktur kelas SOLID.<br>**Teknik:** *Workshop* bedah 5 potongan kode pelanggar SOLID. | **Case-Based Workshop Prinsip SOLID**<br>`[TM: 3×50' = 150']`<br>Latihan perbaikan struktur kelas sesuai ke-5 prinsip SOLID:<br>`[PT: 180']` · `[BM: 180']` | Unduh lembar contoh *Before–After SOLID Principles* di LMS Edlink. | Konstruksi Bersih & **5 Prinsip Desain SOLID**: *Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion* `[3]` | — |
| **6** | **`Sub-CPMK-2.1` & `2.2`:** Menganalisis **Code Smells** (*Long Method, God Class, Feature Envy, Duplicate Code*) dan menerapkan teknik **Refactoring** sistematis [C3→C4] | 2.1.5 Ketepatan mengidentifikasi katalog *Code Smells* Martin Fowler.<br>2.2.1 Ketepatan mengeksekusi teknik *Extract Method, Extract Class, Replace Conditional with Polymorphism* tanpa mengubah perilaku eksternal program. | **Kriteria:** Hilangnya *code smell* dengan perilaku fungsional tetap identik.<br>**Teknik:** Latihan *Refactoring Kata* di kelas. | **Problem-Based Learning (*Code Smells & Refactoring*)**<br>`[TM: 3×50' = 150']`<br>Audit & *refactoring* modul kasus proyek tim:<br>`[PT: 180']` · `[BM: 180']` | Kuis identifikasi jenis *Code Smell* di LMS Edlink. | Katalog **Code Smells** (*Bloaters, Couplers, Dispensables*) & Katalog **Refactoring** Sistematis `[4] Bab 1–3` | — |
| **7** | **`Sub-CPMK-2.2`:** Menerapkan **GoF Design Patterns** (*Creational: Singleton/Factory; Structural: Adapter/Facade; Behavioral: Strategy/Observer*) & Klinik Pra-UTS [C3] | 2.2.2 Ketepatan memilih dan merancang struktur kelas *Design Pattern* **GoF** yang tepat untuk memecahkan masalah desain berulang (*tanpa over-engineering!*). | **Kriteria:** Kesesuaian pola GoF dengan masalah *coupling* yang dihadapi.<br>**Teknik:** Bedah kasus perubahan algoritma pembayaran/notifikasi dengan *Strategy & Observer*. | **Case Method Class *Design Patterns* & Klinik UTS**<br>`[TM: 3×50' = 150']`<br>Persiapan komprehensif menghadapi UTS Pekan 8:<br>`[PT: 180']` · `[BM: 180']` | Simulasi studi kasus UTS (*Architecture + SOLID + GoF*) di LMS Edlink. | **Gang of Four (GoF) Design Patterns**: *Factory Method, Singleton, Adapter, Facade, Strategy,* & *Observer* `[1] Bab 14; [5]` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C3/C4]** | Ketepatan menerapkan arsitektur modular (*low coupling, high cohesion*), mendiagnosis serta me-*refactor* pelanggaran prinsip **SOLID** & *Code Smells*, serta merancang solusi dengan **GoF Design Patterns**. | **Kriteria:** **Rubrik Analitik UTS (`K-4`)**.<br>**Teknik:** Ujian tertulis studi kasus kode & arsitektur terjadwal (*Case-Method Exam*). | **Ujian Tertulis Studi Kasus Luring Terjadwal**<br>`[150 menit]` | Pengarsipan nilai `CPMK-2` pada portal OBE/Edlink. | Materi Arsitektur Modular, *Coupling/Cohesion*, Prinsip **SOLID**, *Refactoring*, & **GoF Design Patterns** (Pekan 4–7) | **30%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-4.1`:** Menguraikan dan merumuskan metrik **Software Quality Assurance (SQA)** berdasarkan 8 karakteristik standar **ISO/IEC 25010** [C2→C5] | 4.1.1 Ketepatan memetakan 8 karakteristik mutu produk **ISO/IEC 25010** (*Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability*) ke metrik kuantitatif yang dapat diukur. | **Kriteria:** Ketepatan indikator metrik tiap dimensi ISO/IEC 25010.<br>**Teknik:** Latihan penyusunan matriks target mutu produk. | **Kuliah Interaktif & Analisis Standar ISO/IEC 25010**<br>`[TM: 3×50' = 150']`<br>Penyusunan matriks target mutu ISO/IEC 25010 untuk sistem objek uji tim:<br>`[PT: 180']` · `[BM: 180']` | Unduh ringkasan standar **ISO/IEC 25010** & templat *SQA Test Plan* di LMS Edlink. | Konsep *Verification vs Validation* (V&V), Biaya Cacat, *Software Quality Assurance* (SQA), & 8 Karakteristik Standar **ISO/IEC 25010** `[1] Bab 19; [6]` | — |
| **10** | **`Sub-CPMK-3.1`:** Merancang skenario pengujian **White-Box**: *Control Flow Graph* (CFG), **Cyclomatic Complexity $V(G)$**, & **Basis Path Testing** [C4] | 3.1.1 Ketepatan menggambar *Control Flow Graph* dari fungsi bercabang/berulang.<br>3.1.2 Ketepatan menghitung $V(G) = E - N + 2P = P_{\text{predikat}} + 1$, menentukan himpunan *Independent Basis Paths*, dan menyusun *Test Cases* yang mencapai 100% *Statement & Branch Coverage*. | **Kriteria:** Akurasi graf CFG, nilai $V(G)$, dan kecukupan jalur independen.<br>**Teknik:** Latihan perhitungan *Basis Path* atas 3 prosedur logika bisnis kompleks. | **Problem-Solving Class *White-Box Testing***<br>`[TM: 3×50' = 150']`<br>Penyusunan CFG, $V(G)$, dan kasus uji *White-Box* untuk Tugas 2:<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi instruksi **Tugas 2 (RTM-2)** di LMS Edlink. | **White-Box Testing**: *Control Flow Graph* (CFG), Rumus McCabe **Cyclomatic Complexity $V(G)$**, *Independent Basis Paths*, & *Statement/Branch Coverage* `[1] Bab 20` | — |
| **11** | **`Sub-CPMK-3.2`:** Merancang skenario pengujian **Black-Box**: **Equivalence Partitioning (EP)**, **Boundary Value Analysis (BVA)**, & *Decision Table Testing* [C4] | 3.2.1 Ketepatan mempartisi kelas ekuivalensi valid/invalid (**EP**) dan menentukan titik batas kritis 2-nilai/3-nilai (**BVA**: `min-1, min, min+1, max-1, max, max+1`).<br>3.2.2 Ketepatan menyusun *Decision Table Test Cases* untuk kombinasi aturan bisnis majemuk. | **Kriteria:** Kelengkapan cakupan batas & bebas redundansi kasus uji.<br>**Teknik:** *Workshop* perancangan matriks *Test Case ID, Precondition, Test Data, Expected Result*. | **Case-Based Learning *Black-Box Testing***<br>`[TM: 3×50' = 150']`<br>Finalisasi paket perancangan skenario uji *White-Box + Black-Box* untuk **Tugas 2**:<br>`[PT: 180']` · `[BM: 180']` | Templat standar IEEE 829 / ISO 29119 *Test Case Specification* di LMS Edlink. | **Black-Box Testing**: *Equivalence Partitioning* (EP), *Boundary Value Analysis* (BVA), *Decision Table*, & *State-Transition Testing* `[1] Bab 20; [2] Bab 8` | — |
| **12** | **`Sub-CPMK-4.2`:** Menerapkan otomasi **Unit Testing**, siklus **Test-Driven Development (TDD)**, & **Mocking/Stubbing** [C4→C5]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 4.2.1 Ketepatan menulis *Automated Unit Tests* berpola **Arrange–Act–Assert (AAA)** menggunakan kerangka uji (`Pytest` / `Jest` / `JUnit`).<br>4.2.2 Ketepatan mengisolasi ketergantungan basis data/API eksternal menggunakan *Test Doubles / Mocking* serta menerapkan siklus *Red–Green–Refactor* (TDD). | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-4`)**.<br>**Teknik:** Pengumpulan Dokumen Rancangan Uji *White-Box & Black-Box* + Kuis Konfirmasi 20'. | **Workshop Otomasi *Unit Testing* & Verifikasi Tugas 2**<br>`[TM: 3×50' = 150']`<br>Implementasi skrip *automated unit tests* atas skenario Tugas 2:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 2 (`CPMK-3`)** di LMS Edlink. | Otomasi Pengujian Perangkat Lunak: Pola *AAA*, Prinsip *FIRST*, Siklus **TDD (*Red–Green–Refactor*)**, *Mocking*, & *Code Coverage* `[1] Bab 20; [2] Bab 8; [3]` | **20%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.2`:** Merancang dan mengevaluasi **Integration Testing**, *Regression Testing*, & pengenalan pengujian beban (*Smoke/Load Testing*) [C5] | 4.2.3 Ketepatan membandingkan strategi integrasi *Top-Down, Bottom-Up,* & *Sandwich* serta mengeksekusi pengujian integrasi antar-modul/kontrak layanan.<br>4.2.4 Ketepatan menganalisis laporan *Line & Branch Coverage* serta temuan regresi. | **Kriteria:** Keberhasilan eksekusi rangkaian uji integrasi & ketajaman analisis *coverage*.<br>**Teknik:** Bedah laporan hasil eksekusi pengujian otomatis proyek tim. | **Problem-Solving Class *Integration & Regression Testing***<br>`[TM: 3×50' = 150']`<br>Perluasan *test suite* proyek mencakup pengujian integrasi & pengukuran *coverage*:<br>`[PT: 180']` · `[BM: 180']` | Panduan pembacaan laporan `pytest-cov` / `Istanbul coverage` di LMS Edlink. | *Integration Testing*, *Regression Testing*, Pengantar Pengujian Non-Fungsional (*Performance/Security Smoke Check*), & Analisis Metrik *Coverage* `[1] Bab 21; [2] Bab 8` | — |
| **14** | **`Sub-CPMK-4.1` & `4.2`:** Menerapkan **Software Configuration Management (SCM)** dengan *Git Branching* & otomasi eksekusi pengujian pada *CI Pipeline* dasar [C4→C5] | 4.2.5 Ketepatan menerapkan alur *Feature Branch + Pull Request Code Review* dan menjalankan pengujian otomatis setiap *push/PR* menggunakan *GitHub Actions* sederhana *(tanpa masuk ke orkestrasi cloud/Kubernetes ranah `STB-601`)*. | **Kriteria:** Riwayat commit Git bersih & status eksekusi *automated test* hijau/terlacak.<br>**Teknik:** Pemeriksaan repositori Git kelompok oleh dosen. | **Ceramah & Demo *Git SCM & Automated Test Gate***<br>`[TM: 3×50' = 150']`<br>Penataan repositori proyek audit mutu & otomatisasi eksekusi *test suite*:<br>`[PT: 180']` · `[BM: 180']` | Contoh berkas `.github/workflows/run-tests.yml` 15 baris di LMS Edlink. | *Software Configuration Management* (SCM): *Semantic Versioning*, *Git Feature-Branch & PR Review*, & *Automated Test Gate* pada CI Dasar `[1] Bab 22; [2] Bab 25` | — |
| **15** | **`Sub-CPMK-4.1` & `4.2`:** Menyusun **SQA Plan, Defect Log, & ISO/IEC 25010 Quality Evaluation Report** serta simulasi presentasi audit mutu [C5] | 4.1.2 Ketepatan menyintesis skor *Cyclomatic Complexity*, *Code Smells*, *Test Pass Rate*, *Branch Coverage*, dan *Defect Density* menjadi evaluasi objektif berstandar **ISO/IEC 25010**. | **Kriteria:** Objektivitas bukti metrik & kelengkapan rekomendasi perbaikan.<br>**Teknik:** *Mock SQA Review* & klinik pra-UAS di kelas. | **Presentasi Kelompok & Klinik Pra-UAS**<br>`[TM: 3×50' = 150']`<br>Finalisasi repositori kode ter-*refactor*, *automated test suite*, & Laporan Evaluasi ISO/IEC 25010:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan draf laporan audit kualitas perangkat lunak di LMS Edlink. | Penyusunan Dokumen *Test Execution Report*, Pelaporan *Bug/Defect Lifecycle*, & Evaluasi Objektif **ISO/IEC 25010** `[1] Bab 19–21; [6]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C5]** | Ketajaman dan objektivitas evaluasi kualitas perangkat lunak berdasarkan **ISO/IEC 25010** dan metrik eksekusi **Automated Unit/Integration Testing** (repositori & laporan tim 50% UAS + ujian tertulis/pertahanan individu 50% UAS). | **Kriteria:** **Rubrik Analitik UAS (`K-4`)**.<br>**Teknik:** Penilaian Bundel Repositori *Refactored Subsystem + Automated Test Suite + Laporan Evaluasi ISO/IEC 25010* (50%) & Ujian/Sidang Verifikasi Individu (50%). | **Sidang Demonstrasi Pengujian Otomatis & Ujian Evaluasi Mutu**<br>`[150 menit]` | Pengarsipan portofolio mutu perangkat lunak & rekap nilai `CPL-08` dan `CPL-13` pada portal OBE. | Evaluasi Komprehensif Kualitas Perangkat Lunak **ISO/IEC 25010**, Otomasi Pengujian, & Rekayasa Konstruksi Bersih | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-08` [C4])
* **Bentuk Instrumen:** Makalah Analisis Kasus Industri Mandiri (3 skenario proyek kontras: sistem rekam medis regulasi ketat, platform *marketplace* rintisan cepat berubah, dan tim pemeliharaan tiket operasional berkelanjutan) — mahasiswa membandingkan *Waterfall, V-Model, Scrum,* dan *Kanban*, memilih model paling tepat untuk tiap kasus dengan matriks justifikasi multi-kriteria, merancang *Sprint/Workflow Ceremony* & *Definition of Done*, serta mengikuti kuis verifikasi 20 menit di kelas.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Ketepatan analisis karakteristik risiko, ketidakpastian, & skala proyek = **30%**; (2) Ketajaman komparasi & justifikasi pemilihan model (*Waterfall, V-Model, Scrum, Kanban*) = **40%**; (3) Ketepatan rancangan artefak operasional (*Backlog/DoD/WIP/V-Mapping*) = **20%**; (4) Kerapian argumen ilmiah & rujukan SWEBOK/Scrum Guide = **10%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 30% · Mengukur `CPMK-2` / `CPL-08` [C3/C4])
* **Bentuk Instrumen:** Ujian Tertulis Studi Kasus Kode & Arsitektur Luring Terjadwal (*Closed-Book*, 150 menit):
  1. **(30%)** Evaluasi arsitektur subsistem yang memiliki *tight coupling* tinggi dan rancang ulang dekomposisi modul berlapisnya (*low coupling, high cohesion*).
  2. **(40%)** Diberikan potongan kode berorientasi objek ($\pm 50$ baris) yang sarat *Code Smells* dan melanggar minimal 3 prinsip **SOLID**: identifikasi pelanggarannya secara tepat dan tuliskan rancangan kelas/kode hasil *refactoring*-nya.
  3. **(30%)** Pilih dan terapkan **GoF Design Pattern** yang paling tepat (*Strategy / Observer / Factory / Adapter*) lengkap diagram kelas dan kerangka implementasinya untuk kasus ekstensi fitur tanpa memodifikasi kode inti.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Ketepatan modularitas arsitektur (*low coupling & high cohesion*) = **30%**; (2) Ketepatan diagnosis & penerapan prinsip **SOLID** serta *refactoring* = **40%**; (3) Ketepatan pemilihan & struktur penerapan **GoF Design Pattern** = **30%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 20% · Mengukur `CPMK-3` / `CPL-13` [C4])
* **Bentuk Instrumen:** Dokumen **Comprehensive Software Test Design Specification** (individu per modul logika bisnis berparameter NIM + kuis konfirmasi 20 menit): (1) Menggambar *Control Flow Graph* (CFG), menghitung **Cyclomatic Complexity $V(G)$** dengan 3 rumus ekuivalen McCabe, menentukan *Independent Basis Paths*, dan merancang kasus uji **White-Box**; (2) Merancang kasus uji **Black-Box** lengkap menggunakan **Equivalence Partitioning (EP)**, **Boundary Value Analysis (BVA)**, dan *Decision Table* berdasarkan spesifikasi aturan sistem.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Akurasi *Control Flow Graph*, perhitungan $V(G)$, & *Basis Path White-Box* = **45%**; (2) Kelengkapan & ketepatan partisi **EP**, titik batas **BVA**, & *Decision Table Black-Box* = **40%**; (3) Standar penulisan tabel spesifikasi kasus uji & verifikasi kelas = **15%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-13` [C5])
* **Bentuk Instrumen:** **Proyek Audit Kualitas & Otomasi Pengujian Subsistem Perangkat Lunak** (50% nilai UAS: repositori Git memuat kode subsistem bersih berprinsip SOLID, rangkaian *Automated Unit & Integration Tests* ber-*coverage* $\ge 80\%$, dan **Laporan Evaluasi Kualitas Berstandar ISO/IEC 25010**) + **Ujian/Sidang Verifikasi Individu Terjadwal** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-4`):** (1) Ketajaman evaluasi kualitas objektif berbasis **ISO/IEC 25010** & analisis metrik cacat = **35%**; (2) Kualitas & cakupan *Automated Unit/Integration Testing* (AAA, *Mocking*, *Branch Coverage*) = **35%**; (3) Disiplin *Clean Code*, SOLID, & riwayat kolaborasi Git SCM = **15%**; (4) Penguasaan individu saat sidang/ujian akhir = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Rekayasa Perangkat Lunak & Platform**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Roni Wahyu, S.Kom., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
