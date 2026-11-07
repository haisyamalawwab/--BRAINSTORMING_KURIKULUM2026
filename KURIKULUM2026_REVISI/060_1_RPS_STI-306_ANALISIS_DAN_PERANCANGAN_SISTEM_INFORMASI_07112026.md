# 060_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-306 — ANALISIS DAN PERANCANGAN SISTEM INFORMASI (*Information Systems Analysis and Design*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI306`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Analisis dan Perancangan Sistem Informasi / *Information Systems Analysis and Design* |
| **Kode Mata Kuliah** | `STI-306` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Sistem Informasi & Tata Kelola (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS Teori** (`T = 3, P = 0`) — Tatap Muka `3×50' = 150'`, Penugasan Terstruktur `3×60' = 180'`, Belajar Mandiri `3×60' = 180'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Rekayasa Sistem (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-101` Pengantar Sistem dan Teknologi Informasi (Kurikulum OBE SISTEKIN 2026), `FST-207` Sistem Basis Data |
| **Mata Kuliah Hilir (*Handoff*)** | `STI-309` Rekayasa Perangkat Lunak, `STI-523` Manajemen Proyek TI, `STC-601` Rekayasa & Otomasi Proses Bisnis (BPA), `STB-703` Arsitektur Enterprise (TOGAF), `FST-610` Capstone Project FSTI |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-06` (`P2`) dan `CPL-02` (`KU1`) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 4 (`K-4`)** — Sintesis, Manajemen, Startup & Capstone (Bobot: Tugas 1 `20%` · UTS `30%` · Tugas 2 `20%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Sistem Informasi, Proses Bisnis & Tata Kelola TI |
| **Koordinator RMK** | Dr. Roni Wahyu, S.Kom., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-02`** (`KU1`) | Keterampilan Umum | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam menganalisis permasalahan komputasi serta mengkaji implikasi pengembangan atau implementasi iptek sesuai kaidah, tata cara, dan etika ilmiah. | **R** (*Reinforce*) | **20%** |
| **`CPL-06`** (`P2`) | Pengetahuan | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | **R** (*Reinforce*) | **80%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **mengelisitasi** kebutuhan fungsional dan non-fungsional perangkat lunak (*B*) dari pemangku kepentingan industri (*C*) dalam bentuk dokumen spesifikasi kebutuhan SRS IEEE 830 (*D*). | **C4** (*Analyze*) | `CPL-02` (`KU1`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **memodelkan** alur proses bisnis organisasi (*B*) menggunakan standar notasi BPMN 2.0 (*C*) dengan analisis efisiensi proses *As-Is* vs *To-Be* (*D*). | **C4** (*Analyze*) | `CPL-06` (`P2`) | **UTS — Pekan 8 (30%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **merancang** pemodelan berorientasi objek (*Use Case, Activity, Class, Sequence, State Machine*) (*B*) menggunakan *Unified Modeling Language* (UML 2.5) (*C*) secara konsisten (*D*). | **C4** (*Analyze*) | `CPL-06` (`P2`) | **Tugas 2 — Pekan 12 (20%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **menyusun** dokumen arsitektur dan desain perangkat lunak komprehensif (SDD) (*B*) untuk persiapan implementasi teknis (*C*) secara profesional (*D*). | **C5** (*Evaluate*) | `CPL-06` (`P2`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Mengelisitasi kebutuhan fungsional dan non-fungsional dari pemangku kepentingan. | `CPMK-1` | **C4** | Mg 1–2 |
| **`Sub-CPMK-1.2`** | Menyusun dokumen spesifikasi kebutuhan sistem (SRS) sesuai standar IEEE 830. | `CPMK-1` | **C4** | Mg 3–4 |
| **`Sub-CPMK-2.1`** | Memodelkan alur proses bisnis dengan notasi BPMN 2.0. | `CPMK-2` | **C4** | Mg 4–5 |
| **`Sub-CPMK-2.2`** | Menganalisis efisiensi proses *As-Is* vs *To-Be* pada rantai proses bisnis organisasi. | `CPMK-2` | **C4** | Mg 5–7 |
| **`Sub-CPMK-3.1`** | Merancang pemodelan fungsional UML (*Use Case* dan *Activity*) secara konsisten. | `CPMK-3` | **C4** | Mg 6–7 |
| **`Sub-CPMK-3.2`** | Merancang pemodelan struktural dan interaksi dinamis UML (*Class, Sequence, State Machine*) secara konsisten. | `CPMK-3` | **C4** | Mg 9–12 |
| **`Sub-CPMK-4.1`** | Menyusun dokumen arsitektur perangkat lunak (SDD) yang siap diimplementasikan. | `CPMK-4` | **C5** | Mg 12–14 |
| **`Sub-CPMK-4.2`** | Menyusun rencana desain perangkat lunak yang selaras dengan kebutuhan bisnis. | `CPMK-4` | **C5** | Mg 13–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Menyusun Dokumen Arsitektur & Desain Sistem Komprehensif / SDD (C5) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: Pemetaan Skema DB, Kontrak API, & Deployment SDD | Sub-CPMK-4.2: Penyelarasan Desain ke Bisnis & Sidang SDD)
      │
[CPMK-3: Merancang Pemodelan Berorientasi Objek UML 2.5 Konsisten (C4) — Mg 6–7 & 9–12 (Tugas 2 20%)]
      ▲  (Sub-CPMK-3.1: Use Case & Activity Diagram | Sub-CPMK-3.2: Class, Sequence, State Machine, & Package Diagram)
      │
[CPMK-2: Memodelkan Proses Bisnis BPMN 2.0 & Analisis As-Is vs To-Be (C4) — Mg 4–8 (UTS 30%)]
      ▲  (Sub-CPMK-2.1: Pool, Lane, Task, Event, Gateway BPMN 2.0 | Sub-CPMK-2.2: Analisis Bottleneck & Reengineering Proses)
      │
[CPMK-1: Mengelisitasi Kebutuhan & Menyusun Dokumen SRS IEEE 830 / ISO 29148 (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Teknik Wawancara, Observasi, JAD, FR/NFR | Sub-CPMK-1.2: Spesifikasi SRS Terukur & Matriks Keterlacakan)
      ▲
[Fondasi Prasyarat: STI-101 Pengantar Sistem dan Teknologi Informasi (Kurikulum OBE SISTEKIN 2026) & FST-207 Sistem Basis Data]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-02`** (`KU1`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-02` = 20%** |
| **`CPL-06`** (`P2`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **30%** | — | — | **30%** | **`CPL-06` = 80%** |
| **`CPL-06`** (`P2`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **20%** | — | **20%** | *(30% + 20% + 30%)* |
| **`CPL-06`** (`P2`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **30%** | **20%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 (Metode Kasus & Proyek Tim $\ge 50\%$):** `Tugas 1 (20% — Case-Based Stakeholder Elicitation & SRS) + Tugas 2 (20% — Case-Based UML Structural & Interaction Modeling) + UAS (30% — Team-Based Project SDD Blueprint & Defense)` = **70%** ($\ge 50\%$, selaras target Dokumen 004 sebesar 70%).

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-306 Analisis dan Perancangan Sistem Informasi` (3 SKS Teori) membekali mahasiswa kemampuan rekayasa analisis kebutuhan dan perancangan cetak biru (*blueprint*) sistem informasi berorientasi objek (*Focus: What the system should do & how components interact structurally*). Mahasiswa mempelajari siklus hidup pengembangan sistem (SDLC), teknik elisitasi kebutuhan pemangku kepentingan (wawancara, observasi, *Joint Application Development* / JAD), penyusunan dokumen *Software Requirements Specification* (SRS berstandar IEEE 830 / ISO/IEC/IEEE 29148), pemodelan proses bisnis organisasi dengan notasi **BPMN 2.0** beserta analisis kesenjangan *As-Is* ke *To-Be*, pemodelan fungsional dan struktural **UML 2.5** (*Use Case, Activity, Class, Sequence, State Machine, Package, & Deployment Diagram*), hingga penyusunan dokumen komprehensif *Software Design Document* (SDD) yang mencakup pemetaan skema relasional dan kontrak antarmuka REST API.

* **🟢 IN-SCOPE (Wajib Diajarkan):** Siklus SDLC & peran *System Analyst*, teknik elisitasi kebutuhan fungsional & non-fungsional, dokumen SRS IEEE 830, pemodelan proses bisnis BPMN 2.0 & analisis *As-Is vs To-Be*, pemodelan UML 2.5 fungsional & struktural (*Use Case, Activity, Class, Sequence, State Machine, Package, Deployment*), pemetaan kelas ke skema tabel & spesifikasi kontrak antarmuka dalam dokumen SDD.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan untuk Mencegah Tumpang Tindih):**
  1. Dilarang menugaskan penulisan kode program aplikasi (*source code*), implementasi *design pattern* pada bahasa pemrograman, atau *unit testing* otomatis (ranah **`STI-309 Rekayasa Perangkat Lunak`** dan **`STI-311`/`STI-416`**).
  2. Dilarang membahas perhitungan anggaran proyek terperinci (*Earned Value Management* / EVM), jadwal jalur kritis *Gantt/CPM*, maupun kontrak pengadaan TI (ranah **`STI-523 Manajemen Proyek TI`**).
  3. Dilarang mengeksekusi otomasi alur kerja *Camunda BPM engine* atau bot *Robotic Process Automation* (ranah **`STC-601 Rekayasa & Otomasi Proses Bisnis (BPA)`**).
* **🔄 HANDOFF ANCHOR:** Menerima konsep proses bisnis organisasi dari `STI-101` dan pemodelan relasional ERD dari `FST-207`, lalu menyerahkan cetak biru SRS & SDD siap konstruksi ke **`STI-309 Rekayasa Perangkat Lunak`**, tata kelola proyek ke **`STI-523 Manajemen Proyek TI`**, otomasi alur kerja ke **`STC-601`**, dan arsitektur tingkat korporat ke **`STB-703 Arsitektur Enterprise (TOGAF)`**.

### 7. Bahan Kajian (*Body of Knowledge* APTIKOM) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS07` (*Systems Analysis and Design*) & `BK-IS09` (*Business Process Management*).
* **Bahan Kajian Sekunder:** `BK-IS01` (*Foundations of Information Systems*) & `BK-IS04` (*Enterprise Architecture*).

**Pustaka Utama:**
1. Dennis, A., Wixom, B. H., & Tegarden, D. (2021). *Systems Analysis and Design: An Object-Oriented Approach with UML* (6th ed.). Wiley.
2. Tilley, S. (2020). *Systems Analysis and Design* (12th ed.). Cengage Learning.
3. Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of Business Process Management* (2nd ed.). Springer.
4. Object Management Group (OMG). (2017). *Unified Modeling Language (UML) Specification Version 2.5.1* & *Business Process Model and Notation (BPMN) Version 2.0.2*.

**Pustaka Pendukung & Standar Industri:**
5. ISO/IEC/IEEE 29148:2018 (pengganti IEEE Std 830-1998) — *Systems and Software Engineering — Life Cycle Processes — Requirements Engineering*; IEEE Std 1016-2009 — *Software Design Descriptions (SDD)*.
6. Larman, C. (2012). *Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design* (3rd ed.). Pearson.
7. Perangkat Lunak Pemodelan Gratis/Akademik: *Camunda Modeler* / *bpmn.io* (BPMN 2.0), *PlantUML* / *StarUML* / *Visual Paradigm CE* / *draw.io* (UML 2.5).

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Pengantar):** Menguraikan siklus hidup pengembangan sistem (SDLC) dan peran strategis *System Analyst* [C2→C4] | 1.1.1 Ketepatan membandingkan fase *Planning, Analysis, Design, Implementation* pada pendekatan prediktif vs adaptif.<br>1.1.2 Ketepatan memetakan artefak keluaran analis sistem serta *boundary* `STI-306` vs `STI-309`. | **Kriteria:** Kuis diagnostik formatif.<br>**Teknik:** Non-tes (diskusi kasus kegagalan sistem akibat salah spesifikasi kebutuhan). | **Kuliah Interaktif & Diskusi Kasus**<br>`[TM: 3×50' = 150']`<br>Pembentukan kelompok proyek mitra (3–4 mhs) & pemilihan organisasi studi kasus:<br>`[PT: 180']` · `[BM: 180']` | Kontrak perkuliahan, unduh templat SRS IEEE 830 & SDD di LMS Edlink. | Kontrak Belajar, Kegagalan Proyek SI Akibat *Poor Requirements*, Siklus SDLC, Peran *Business/System Analyst* `[1] Bab 1; [2] Bab 1` | — |
| **2** | **`Sub-CPMK-1.1`:** Mengelisitasi kebutuhan fungsional dan non-fungsional dari pemangku kepentingan [C4] | 1.1.3 Ketepatan menyusun instrumen elisitasi (wawancara, observasi lapangan, kuesioner, & lokakarya JAD).<br>1.1.4 Ketepatan memilah *Business Requirements*, *User Requirements*, *Functional Requirements* (FR), dan *Non-Functional Requirements* (NFR — kerangka FURPS+/PIECES). | **Kriteria:** Rubrik formatif ketajaman elisitasi.<br>**Teknik:** Simulasi *role-play stakeholder interview* di kelas. | **Case-Based Learning & Role-Play Wawancara**<br>`[TM: 3×50' = 150']`<br>Eksekusi wawancara/observasi awal pada mitra studi kasus:<br>`[PT: 180']` · `[BM: 180']` | Unggah draf transkrip elisitasi & daftar masalah PIECES di LMS Edlink. | Teknik Elisitasi Kebutuhan (*Interview, Observation, Document Analysis, JAD*), Klasifikasi FR vs NFR Terukur `[1] Bab 3; [2] Bab 3; [5]` | — |
| **3** | **`Sub-CPMK-1.2`:** Menyusun dokumen spesifikasi kebutuhan sistem (SRS) sesuai standar IEEE 830 [C4] | 1.2.1 Ketepatan merumuskan butir kebutuhan yang bebas ambiguitas, dapat diuji (*testable*), dan bernomor unik.<br>1.2.2 Ketepatan menyusun struktur dokumen SRS IEEE 830 / ISO 29148 beserta *Requirements Traceability Matrix* (RTM) awal. | **Kriteria:** Rubrik formatif kualitas SRS.<br>**Teknik:** *Peer-review* pemeriksaan kata ambigu pada draf SRS. | **Workshop Dokumen SRS**<br>`[TM: 3×50' = 150']`<br>Penyusunan dokumen SRS versi 1.0 untuk evaluasi Tugas 1:<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi instruksi **Tugas 1 (RTM-1)** di LMS Edlink. | Standar Dokumen SRS IEEE 830 / ISO 29148, Kriteria Kebutuhan Berkualitas (*Unambiguous, Verifiable, Traceable*), Matriks RTM `[1] Bab 3; [5]` | — |
| **4** | **`Sub-CPMK-2.1`:** Memodelkan alur proses bisnis dengan notasi BPMN 2.0 [C4]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 2.1.1 Ketepatan menggunakan elemen inti BPMN 2.0 (*Pool, Lane, Task, Start/Intermediate/End Event*).<br>2.1.2 Ketepatan memodelkan percabangan *Exclusive (XOR), Parallel (AND),* dan *Inclusive (OR) Gateway* bebas *deadlock* token. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-4`)**.<br>**Teknik:** Pengumpulan Dokumen SRS IEEE 830 + Kuis Verifikasi Elisitasi 20'. | **Problem-Solving Class BPMN 2.0 & Verifikasi Tugas 1**<br>`[TM: 3×50' = 150']`<br>Pemodelan 2 proses bisnis inti mitra dengan *Camunda Modeler* / *bpmn.io*:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink; unduh *cheat-sheet* BPMN 2.0. | Standar Notasi BPMN 2.0: *Pools, Lanes, Activities, Gateways (XOR/AND/OR), Message Flow vs Sequence Flow* `[3] Bab 3–4; [4]` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.2`:** Menganalisis efisiensi proses *As-Is* vs *To-Be* pada rantai proses bisnis organisasi [C4] | 2.2.1 Ketepatan mengidentifikasi *bottleneck*, duplikasi entri manual, dan serah-terima (*handoff*) berlebih pada BPMN *As-Is*.<br>2.2.2 Ketepatan merancang BPMN *To-Be* dan menghitung estimasi pengurangan *cycle time* / langkah proses. | **Kriteria:** Rubrik formatif analisis proses.<br>**Teknik:** Bedah komparatif model BPMN *As-Is* vs *To-Be* di kelas. | **Case Method Workshop (*Process Redesign*)**<br>`[TM: 3×50' = 150']`<br>Analisis nilai tambah (*Value-Added Analysis*) & penyusunan BPMN *To-Be*:<br>`[PT: 180']` · `[BM: 180']` | Forum diskusi kesalahan sintaks umum BPMN 2.0 di LMS Edlink. | *Business Process Analysis & Reengineering*: Identifikasi *Bottleneck*, Analisis *As-Is* ke *To-Be*, Jembatan BPMN ke Kebutuhan Sistem `[3] Bab 6–8` | — |
| **6** | **`Sub-CPMK-3.1`:** Merancang pemodelan fungsional UML (*Use Case Diagram* dan skenario naratif) secara konsisten [C4] | 3.1.1 Ketepatan menurunkan aktivitas terotomasi pada BPMN *To-Be* menjadi *Use Case* dan hierarki *Actor*.<br>3.1.2 Ketepatan membedakan relasi `<<include>>` vs `<<extend>>` serta menulis *Fully Dressed Use Case Specification* (alur normal & alternatif). | **Kriteria:** Rubrik formatif konsistensi UML.<br>**Teknik:** Penilaian silang diagram *Use Case* & tabel skenario. | **Case-Based Learning UML Fungsional**<br>`[TM: 3×50' = 150']`<br>Penyusunan *Use Case Diagram* & 5 spesifikasi skenario naratif lengkap:<br>`[PT: 180']` · `[BM: 180']` | Latihan bedah miskonsepsi `<<include>>` vs `<<extend>>` di LMS Edlink. | Pemodelan Fungsional UML 2.5: *System Boundary*, *Actor*, *Use Case Diagram*, Relasi `<<include>>`/`<<extend>>`, & *Use Case Description* `[1] Bab 4–5; [6] Bab 6` | — |
| **7** | **`Sub-CPMK-3.1` (Lanjutan) & Integrasi Pra-UTS:** Merancang *Activity Diagram* untuk skenario kompleks dan mengaudit konsistensi SRS–BPMN–Use Case [C4] | 3.1.3 Ketepatan memodelkan *Swimlane/Partition, Decision/Merge, Fork/Join,* dan *Object Node* pada *Activity Diagram* UML.<br>3.1.4 Ketepatan menelusuri konsistensi antar-artefak paruh semester pertama. | **Kriteria:** Kelengkapan latihan integratif pra-UTS.<br>**Teknik:** *Walkthrough* studi kasus simulasi UTS. | **Problem-Solving Class & Klinik Pra-UTS**<br>`[TM: 3×50' = 150']`<br>Persiapan menghadapi evaluasi tengah semester:<br>`[PT: 180']` · `[BM: 180']` | Simulasi kasus komprehensif BPMN *As-Is/To-Be* di LMS Edlink. | *Activity Diagram* UML 2.5 (*Fork/Join, Swimlane, Exception Flow*) & Audit Konsistensi BPMN ↔ SRS `[1] Bab 5; [4]` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C4]** | Ketepatan memodelkan proses bisnis organisasi dengan notasi BPMN 2.0 yang valid secara sintaks/semantik serta ketajaman menganalisis efisiensi *As-Is* vs *To-Be* dan pemetaan fungsionalnya. | **Kriteria:** **Rubrik Analitik UTS (`K-4`)**.<br>**Teknik:** Tes tertulis studi kasus terjadwal (*Case-Method Exam*). | **Ujian Tertulis Studi Kasus Luring Terjadwal**<br>`[150 menit]` | Pengarsipan berita acara & lembar nilai `CPMK-2` pada portal OBE/Edlink. | Materi Komprehensif Pemodelan Proses Bisnis BPMN 2.0 & Analisis Efisiensi *As-Is* vs *To-Be* (Pekan 4–7) | **30%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.2`:** Merancang pemodelan struktural statis sistem menggunakan *Class Diagram* UML 2.5 [C4] | 3.2.1 Ketepatan mengidentifikasi kelas domain & kelas analisis (*Boundary–Control–Entity* / MVC konseptual) beserta atribut, tipe, operasi, dan *visibility* (`+`, `-`, `#`).<br>3.2.2 Ketepatan membedakan relasi *Association, Multiplicity, Aggregation, Composition,* dan *Generalization*. | **Kriteria:** Rubrik formatif pemodelan kelas.<br>**Teknik:** Latihan ekstraksi *Class Diagram* dari narasi *Use Case*. | **Case Method Class (*Domain & Design Class Modeling*)**<br>`[TM: 3×50' = 150']`<br>Perancangan *Class Diagram* sistem proyek tim:<br>`[PT: 180']` · `[BM: 180']` | Unggah berkas *PlantUML/StarUML* *Class Diagram* di LMS Edlink. | *Class Diagram* UML 2.5: Stereotip *Boundary–Control–Entity*, Atribut & Operasi, *Multiplicity*, *Aggregation vs Composition*, *Inheritance* `[1] Bab 6; [6] Bab 9 & 16` | — |
| **10** | **`Sub-CPMK-3.2`:** Merancang pemodelan interaksi objek dinamis menggunakan *Sequence Diagram* UML 2.5 [C4] | 3.2.3 Ketepatan menyusun *Lifeline*, *Activation Bar*, pesan sinkron/asinkron, *Return Message*, serta *Combined Fragments* (`alt`, `opt`, `loop`).<br>3.2.4 Konsistensi 100% antara nama metode yang dipanggil di *Sequence Diagram* dengan daftar operasi pada *Class Diagram*. | **Kriteria:** Rubrik formatif konsistensi silang.<br>**Teknik:** Audit berpasangan (*Class ↔ Sequence Consistency Check*). | **Problem-Solving Workshop *Sequence Diagram***<br>`[TM: 3×50' = 150']`<br>Pembuatan 4 *Sequence Diagram* utama proyek sistem:<br>`[PT: 180']` · `[BM: 180']` | Rilis instruksi resmi **Tugas 2 (RTM-2)** di LMS Edlink. | Interaksi Dinamis UML 2.5: *Sequence Diagram*, *Lifeline*, *Messages*, *Combined Fragments* (`alt`, `opt`, `loop`), & Aturan Konsistensi Metode Kelas `[1] Bab 7; [6] Bab 15` | — |
| **11** | **`Sub-CPMK-3.2`:** Merancang siklus status objek kompleks dengan *State Machine Diagram* UML 2.5 [C4] | 3.2.5 Ketepatan memodelkan *State*, *Event*, *Guard Condition* `[...]`, dan *Action* `/` untuk entitas berstatus kompleks (mis. pesanan, tiket layanan, pengajuan kredit). | **Kriteria:** Ketepatan transisi status tanpa *dead-end state*.<br>**Teknik:** Latihan pemodelan siklus status transaksi e-commerce/akademik. | **Case-Based Learning *State Machine***<br>`[TM: 3×50' = 150']`<br>Penyelesaian paket model UML utuh untuk pengumpulan Tugas 2:<br>`[PT: 180']` · `[BM: 180']` | Klinik daring pemeriksaan konsistensi 5 diagram UML di LMS Edlink. | *State Machine Diagram* & *Communication Diagram* UML 2.5: *Initial/Final State, Transition, Event, Guard, Action* `[1] Bab 7; [4]` | — |
| **12** | **`Sub-CPMK-4.1` (Pengantar Arsitektur) & Evaluasi Tugas 2 (`CPMK-3`):** Merancang *Package Diagram* dan *Deployment Diagram* sistem [C4→C5] | 4.1.1 Ketepatan mengelompokkan kelas ke dalam paket berlapis (*Layered Package Diagram*) dan memetakan topologi penempatan komponen fisik/awan pada *Deployment Diagram*. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-4`)**.<br>**Teknik:** Pengumpulan Paket Pemodelan UML 2.5 Konsisten + Ujian Verifikasi Lisan/Tertulis Singkat 20'. | **Ceramah Arsitektur UML & Verifikasi Tugas 2**<br>`[TM: 3×50' = 150']`<br>Penyusunan bab arsitektur pada dokumen SDD:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 2 (`CPMK-3`)** di LMS Edlink; rilis kerangka final proyek SDD UAS. | Pemodelan Arsitektur Sistem pada SDD: *Package Diagram*, *Component Diagram*, & *Deployment Diagram* `[1] Bab 8–9; [5]` | **20%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1` & `Sub-CPMK-4.2`:** Merancang peta navigasi dialog antarmuka (*Screen Flow*) dan menyelaraskan desain sistem dengan proses bisnis [C5] | 4.2.1 Ketepatan menyusun *Dialog Navigation Diagram* dan sketsa tata letak konseptual layar yang tertelusur ke setiap *Use Case*.<br>4.2.2 Ketepatan menjustifikasi keputusan arsitektur terhadap kebutuhan non-fungsional bisnis (keamanan akses, waktu respons, skalabilitas). | **Kriteria:** Rubrik formatif penyelarasan bisnis-desain.<br>**Teknik:** *Design Walkthrough* antar-tim di kelas. | **Case Method Class (*Navigation & Business Alignment*)**<br>`[TM: 3×50' = 150']`<br>Penyusunan bab navigasi layar & matriks keselarasan NFR pada SDD:<br>`[PT: 180']` · `[BM: 180']` | Unggah draf *Dialog Navigation Map* di LMS Edlink *(menjaga guardrail: high-fi Figma & uji SUS diampu `STI-308`)*. | *User Interface Dialog Navigation Diagram*, Perancangan Kontrol Masukan/Keluaran, & Penyelarasan Desain dengan NFR Bisnis `[1] Bab 10; [2] Bab 8` | — |
| **14** | **`Sub-CPMK-4.1`:** Merancang pemetaan *Object-Relational Mapping* (Class ke Skema Basis Data) dan spesifikasi kontrak antarmuka REST API dalam SDD [C5] | 4.1.2 Ketepatan memetakan *Class Diagram* (termasuk asosiasi *many-to-many* dan pewarisan) menjadi skema tabel relasional siap pakai.<br>4.1.3 Ketepatan menyusun spesifikasi kontrak antarmuka layanan (*Endpoint URL, HTTP Method, Request/Response JSON Payload, Status Code*) tanpa menulis kode *backend*. | **Kriteria:** Rubrik formatif kelengkapan spesifikasi teknis SDD.<br>**Teknik:** Bedah kontrak REST API & kamus data SDD. | **Workshop Desain Data & Kontrak API pada SDD**<br>`[TM: 3×50' = 150']`<br>Finalisasi kamus data relasional & tabel kontrak API pada dokumen SDD:<br>`[PT: 180']` · `[BM: 180']` | Contoh templat *OpenAPI/REST Contract Table* untuk SDD di LMS Edlink. | Pemetaan *Class-to-Relational Database Schema* & Spesifikasi Kontrak Antarmuka Modul / REST API dalam Dokumen SDD `[1] Bab 11; [5]` | — |
| **15** | **`Sub-CPMK-4.2`:** Mengevaluasi keterlacakan ujung-ke-ujung (*End-to-End Traceability* SRS ↔ BPMN ↔ UML ↔ SDD) dan simulasi sidang pemangku kepentingan [C5] | 4.2.3 Tidak adanya kebutuhan fungsional yatim (*orphan requirement*) antara SRS, BPMN *To-Be*, UML, skema data, dan kontrak API.<br>4.2.4 Kesiapan tim mempertahankan cetak biru SDD secara profesional. | **Kriteria:** Daftar periksa kualitas SDD IEEE 1016.<br>**Teknik:** *Mock Design Review* & *Coaching Clinic* pra-UAS. | **Presentasi Pra-Sidang & Audit Keterlacakan SDD**<br>`[TM: 3×50' = 150']`<br>Penyempurnaan naskah final SDD berdasarkan catatan dosen:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan draf pra-sidang dokumen SDD di LMS Edlink. | Standar IEEE 1016 *Software Design Description* (SDD), Audit *End-to-End Traceability Matrix*, & Persiapan Serah Terima (*Handoff*) ke `STI-309` `[1] Bab 12; [5]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C5]** | Ketepatan, kelengkapan, konsistensi internal, dan kelayakan implementasi dokumen **Software Design Document (SDD)** komprehensif beserta ketajaman pertahanan individu pada sidang review kritis. | **Kriteria:** **Rubrik Analitik UAS (`K-4`)**.<br>**Teknik:** Penilaian Dokumen SDD Tim (60% UAS) + Sidang Tanya-Jawab Kritis Individu per Anggota (40% UAS). | **Sidang Presentasi & Pertahanan Dokumen SDD Terjadwal**<br>`[150 menit]` | Unggah bundel final `SRS + SDD` ke repositori portofolio OBE LMS Edlink. | Sintesis Utuh Dokumen Arsitektur & Desain Perangkat Lunak (SDD) Siap Konstruksi (Pekan 9–15) | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-02` [C4])
* **Bentuk Instrumen:** Penyusunan Dokumen **Software Requirements Specification (SRS) Berstandar IEEE 830 / ISO 29148** (Individu/Pasangan pada sub-modul berbeda dari organisasi studi kasus nyata) dilengkapi bukti instrumen elisitasi (daftar pertanyaan & ringkasan hasil wawancara/observasi), analisis masalah PIECES, minimal 12 butir *Functional Requirements* terukur, minimal 6 butir *Non-Functional Requirements* kuantitatif, serta kuis verifikasi tertulis 20 menit di kelas.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Ketajaman elisitasi masalah & relevansi konteks pemangku kepentingan nyata = **30%**; (2) Kualitas spesifikasi FR & NFR berstandar IEEE 830 (spesifik, terukur, bebas ambigu) = **35%**; (3) Keterlacakan kebutuhan (*Traceability*) & konsistensi kuis verifikasi = **20%**; (4) Kerapian struktur dokumen formal rekayasa = **15%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 30% · Mengukur `CPMK-2` / `CPL-06` [C4])
* **Bentuk Instrumen:** Ujian Tertulis Studi Kasus Luring Terjadwal (*Case-Method Exam*, 150 menit). Diberikan narasi rinci proses operasional sebuah rumah sakit / perusahaan logistik yang masih sarat antrean manual dan persetujuan berlapis:
  1. **(35%)** Gambar diagram **BPMN 2.0 *As-Is*** lengkap (*Pool, Lane, Task, Event, XOR/AND/OR Gateway, Message Flow*) sesuai aturan sintaks OMG BPMN 2.0.
  2. **(35%)** Analisis minimal 4 titik inefisiensi/*bottleneck* pada alur *As-Is*, lalu rancang diagram **BPMN 2.0 *To-Be*** terotomasi disertai perhitungan ringkas efisiensi tahapan proses.
  3. **(30%)** Petakan aktivitas sistem pada BPMN *To-Be* menjadi daftar layanan sistem & spesifikasi kebutuhan fungsional yang konsisten.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Kepatuhan aturan sintaks & semantik notasi BPMN 2.0 = **35%**; (2) Ketajaman analisis efisiensi proses *As-Is* vs *To-Be* = **35%**; (3) Konsistensi jembatan proses bisnis ke layanan sistem = **20%**; (4) Kejelasan tata letak & keterbacaan diagram = **10%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 20% · Mengukur `CPMK-3` / `CPL-06` [C4])
* **Bentuk Instrumen:** Paket Pemodelan Berorientasi Objek **UML 2.5 Terpadu** atas studi kasus sistem (dikerjakan per modul tanggung jawab individu dalam tim + verifikasi lisan 20 menit): mencakup *Use Case Diagram* + 3 spesifikasi naratif *fully dressed*, *Activity Diagram*, *Class Diagram* lengkap (atribut, tipe, operasi, *visibility*, *multiplicity*), *Sequence Diagram* (dengan *combined fragment* `alt`/`loop`), serta *State Machine Diagram* untuk objek berstatus kompleks.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Ketepatan pemodelan fungsional (*Use Case* & *Activity*) = **25%**; (2) Ketepatan pemodelan struktural & dinamis (*Class, Sequence, State Machine*) = **35%**; (3) **Konsistensi silang antar-diagram UML** (nama kelas, operasi, dan alur pesan selaras 100%) = **25%**; (4) Kerapian notasi UML 2.5 & penguasaan saat verifikasi = **15%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-06` [C5])
* **Bentuk Instrumen:** Bundel **Software Design Document (SDD) Komprehensif Berstandar IEEE 1016** (60% nilai UAS) + **Sidang Presentasi & Tanya-Jawab Kritis Individu** (40% nilai UAS, 150 menit). Dokumen SDD wajib memuat arsitektur paket/penempatan (*Package & Deployment Diagram*), konsolidasi UML, pemetaan skema basis data relasional, spesifikasi kontrak REST API, peta navigasi dialog antarmuka, dan matriks keterlacakan ujung-ke-ujung (*SRS ↔ BPMN ↔ UML ↔ DB/API*) yang siap diserahkan (*handoff*) ke tim pengembang pada `STI-309 Rekayasa Perangkat Lunak` **(tanpa kode program aplikasi)**.
* **Bobot Kriteria Rubrik (`K-4`):** (1) Relevansi solusi desain & keselarasan dengan kebutuhan bisnis/SRS = **30%**; (2) Kelengkapan & ketepatan teknis arsitektur SDD (paket, skema DB, kontrak API, navigasi) = **30%**; (3) Konsistensi keterlacakan (*end-to-end traceability*) & manajemen kolaborasi tim = **20%**; (4) Kualitas dokumen formal IEEE 1016 & ketajaman pertahanan individu saat sidang = **20%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Sistem Informasi, Proses Bisnis & Tata Kelola TI**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Roni Wahyu, S.Kom., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
