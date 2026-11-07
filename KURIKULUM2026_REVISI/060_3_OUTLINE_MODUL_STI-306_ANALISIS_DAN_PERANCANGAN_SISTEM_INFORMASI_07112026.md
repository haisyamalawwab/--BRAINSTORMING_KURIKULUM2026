# 060_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-306 — ANALISIS DAN PERANCANGAN SISTEM INFORMASI (*Information Systems Analysis and Design*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI306` · **Bobot:** 3 SKS Teori · **Semester:** 3  
**CPL:** `CPL-02` (`KU1` = 20%) & `CPL-06` (`P2` = 80%) [Level `R`] · **BoK:** `BK-IS07`, `BK-IS09`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & KARAKTERISTIK BUKU MODUL AJAR

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Analisis Kebutuhan, Pemodelan Proses Bisnis BPMN 2.0, & Perancangan Sistem Berorientasi Objek (UML 2.5 & SDD)* |
| **Target Tebal Naskah** | 14 Bab Materi Inti + 2 Unit Evaluasi Studi Kasus ($\pm 200\text{–}240\text{ halaman}$ A4 dilengkapi templat siap pakai IEEE 830 SRS, *Cheat-Sheet* BPMN 2.0 & UML 2.5, serta IEEE 1016 SDD) |
| **Benang Merah Studi Kasus Buku** | Satu studi kasus terpadu (*Sistem Manajemen Rantai Pasok & Layanan Klinik Jejaring*) ditelusuri secara utuh dari Bab 1 (masalah awal) → Bab 3 (SRS) → Bab 5 (BPMN *As-Is/To-Be*) → Bab 6–10 (UML 2.5) → Bab 14 (Dokumen SDD Final). |
| **Anatomi Baku Setiap Bab** | (1) *Sub-CPMK & Indikator*; (2) *Kasus Pembuka Industri*; (3) *Paparan Konsep, Standar Notasi, & Aturan Validasi*; (4) *Contoh Artefak Benar vs Salah (Anti-Patterns)*; (5) *Kotak Boundary Guardrail*; (6) *Rangkuman*; (7) *Latihan Pemodelan Mandiri*. |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Rekayasa Kebutuhan & SRS** | **Bab 1** | Siklus Hidup Pengembangan Sistem (SDLC), Krisis Spesifikasi, & Peran *System Analyst* | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Teknik Elisitasi Kebutuhan Pemangku Kepentingan & Analisis Masalah (PIECES / FURPS+) | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Penyusunan *Software Requirements Specification* (SRS IEEE 830 / ISO 29148) & Matriks RTM | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Pemodelan Proses Bisnis BPMN 2.0** | **Bab 4** | Tata Bahasa & Sintaks Pemodelan Proses Bisnis Standar OMG **BPMN 2.0** | Mg 4 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 5** | Analisis Inefisiensi *Bottleneck* & Rekayasa Ulang Proses Bisnis (*As-Is* ke *To-Be*) | Mg 5 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| **Bagian III:<br>Pemodelan Fungsional & Dinamis UML 2.5** | **Bab 6** | Pemodelan Fungsional UML 2.5: *Use Case Diagram* & *Fully Dressed Scenario* | Mg 6 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 7** | Pemodelan Alur Kerja & Logika Percabangan dengan *Activity Diagram* UML 2.5 | Mg 7 | `CPMK-3` | `Sub-CPMK-3.1` | UTS / Tugas 2 |
| *Evaluasi I* | *Unit E1* | *Studi Kasus Komprehensif SRS & BPMN 2.0 As-Is/To-Be (Persiapan UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| | **Bab 8** | Pemodelan Struktural Statis UML 2.5: *Domain & Design Class Diagram* | Mg 9 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 9** | Pemodelan Interaksi Objek Dinamis UML 2.5: *Sequence Diagram* & *Combined Fragments* | Mg 10 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 10** | Pemodelan Daur Hidup Objek Kompleks dengan *State Machine Diagram* UML 2.5 | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Arsitektur Sistem & Dokumen SDD** | **Bab 11** | Pemodelan Arsitektur Sistem: *Package Diagram*, *Component*, & *Deployment Diagram* | Mg 12 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 12** | Perancangan *Dialog Navigation Diagram* & Penyelarasan Arsitektur terhadap NFR Bisnis | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 13** | Pemetaan *Class-to-Relational Database Schema* & Spesifikasi Kontrak REST API | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 14** | Perakitan *Software Design Document* (SDD IEEE 1016) & Audit *End-to-End Traceability* | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Sidang Desain Arsitektur SDD & Checklist Serah Terima ke `STI-309`* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB

#### BAB 1: Siklus Hidup Pengembangan Sistem (SDLC), Krisis Spesifikasi, & Peran *System Analyst* (Pekan 1)
* **Sub-Pokok Bahasan:** (1.1) Anatomi Kegagalan Proyek SI Akibat Cacat Kebutuhan (*Standish Chaos Insights*); (1.2) Empat Fase Inti SDLC & Artefaknya; (1.3) Perbandingan Pendekatan *Waterfall, Iterative, Prototyping,* & *Agile* dari Kacamata Analis Sistem; (1.4) Kompetensi *Business/System Analyst* dan Batas Tegas `STI-306` vs `STI-309 Rekayasa Perangkat Lunak`.
* **Gambar & Tabel Wajib:** Gambar 1.1 Kurva Eksponensial Biaya Perbaikan Cacat Spesifikasi di Tiap Fase SDLC; Tabel 1.1 Peta Artefak `STI-306` (SRS & SDD) Menuju `STI-309` (Kode & Pengujian).

#### BAB 2: Teknik Elisitasi Kebutuhan Pemangku Kepentingan & Analisis Masalah (PIECES / FURPS+) (Pekan 2)
* **Sub-Pokok Bahasan:** (2.1) Identifikasi Peta *Stakeholder* (Sponsor, Pengguna Operasional, Manajer, Regulator); (2.2) Teknik Wawancara Terstruktur, Observasi *Gemba*, Kuesioner, Analisis Dokumen, dan Lokakarya JAD; (2.3) Diagnosis Akar Masalah dengan Kerangka PIECES; (2.4) Pemilahan Tegas *Business, User, Functional (FR),* dan *Non-Functional Requirements (NFR — FURPS+)*.
* **Gambar & Tabel Wajib:** Tabel 2.1 Perbandingan Kelebihan & Kelemahan 5 Teknik Elisitasi; Tabel 2.2 Contoh Transformasi Keluhan Kabur Pengguna Menjadi FR & NFR Kuantitatif.

#### BAB 3: Penyusunan *Software Requirements Specification* (SRS IEEE 830 / ISO 29148) & Matriks RTM (Pekan 3)
* **Sub-Pokok Bahasan:** (3.1) Struktur Baku Dokumen SRS menurut IEEE Std 830 & ISO/IEC/IEEE 29148; (3.2) Kaidah Penulisan Kalimat Spesifikasi yang Tegas (*Atomic, Unambiguous, Verifiable*); (3.3) Penomoran Hierarkis Kebutuhan dan Prioritas MoSCoW (*Must, Should, Could, Won't*); (3.4) Penyusunan *Requirements Traceability Matrix* (RTM) Tahap Awal.
* **Gambar & Tabel Wajib:** Gambar 3.1 Anatomi Dokumen SRS Standar Industri; Tabel 3.1 Daftar Kata Ambigu Terlarang dalam SRS beserta Padanan Terukurnya.

#### BAB 4: Tata Bahasa & Sintaks Pemodelan Proses Bisnis Standar OMG BPMN 2.0 (Pekan 4)
* **Sub-Pokok Bahasan:** (4.1) Konsep Dasar Manajemen Proses Bisnis (BPM); (4.2) *Swimlanes*: Kapan Memakai *Pool* Terpisah vs *Lane* Internal; (4.3) *Flow Objects*: *Events* (*Start, Intermediate Timer/Message, End*), *Activities* (*User, Service, Manual Task, Sub-Process*), dan *Gateways* (`XOR`, `AND`, `OR`); (4.4) Aturan Sintaks *Sequence Flow* vs *Message Flow* dan Pencegahan *Deadlock/Livelock* pada Gateway.
* **Gambar & Tabel Wajib:** Gambar 4.1 Poster Rujukan Cepat Simbol Inti BPMN 2.0; Gambar 4.2 Empat Kesalahan Sintaks BPMN Paling Umum (*Anti-Patterns*) dan Cara Memperbaikinya.

#### BAB 5: Analisis Inefisiensi *Bottleneck* & Rekayasa Ulang Proses Bisnis (*As-Is* ke *To-Be*) (Pekan 5)
* **Sub-Pokok Bahasan:** (5.1) Pemetaan Proses Aktual (*As-Is Discovery*); (5.2) Analisis Nilai Tambah (*Value-Added, Business Value-Added, Non-Value-Added/Waste*); (5.3) Sepuluh Heuristik Perancangan Ulang Proses Bisnis Dumas (*Elimination, Triage, Parallelism, Integral Technology*); (5.4) Merancang BPMN *To-Be* dan Menurunkan *User/Service Task* Menjadi Daftar Layanan Sistem Informasi.
* **Gambar & Tabel Wajib:** Gambar 5.1 Sandingan Visual BPMN *As-Is* vs BPMN *To-Be* pada Studi Kasus Klinik; Tabel 5.1 Lembar Kerja Evaluasi Pengurangan Waktu Siklus (*Cycle Time*).

#### BAB 6: Pemodelan Fungsional UML 2.5: *Use Case Diagram* & *Fully Dressed Scenario* (Pekan 6)
* **Sub-Pokok Bahasan:** (6.1) Menurunkan Aktivitas BPMN *To-Be* ke *Use Case*; (6.2) *Primary vs Secondary Actor* & Batas Sistem (*System Boundary*); (6.3) Aturan Tegas Relasi `<<include>>`, `<<extend>>` (beserta *extension point*), dan Generalisasi Aktor; (6.4) Menyusun Tabel *Fully Dressed Use Case Specification* (Kondisi Awal, Alur Utama Aktor–Sistem, Alur Alternatif/Eksepsi, Kondisi Akhir).
* **Gambar & Tabel Wajib:** Gambar 6.1 Perbandingan Tepat Arah Panah `<<include>>` vs `<<extend>>`; Tabel 6.1 Templat Baku *Fully Dressed Use Case Specification*.

#### BAB 7: Pemodelan Alur Kerja & Logika Percabangan dengan *Activity Diagram* UML 2.5 (Pekan 7)
* **Sub-Pokok Bahasan:** (7.1) Perbedaan Fokus BPMN 2.0 vs *Activity Diagram* UML 2.5; (7.2) Elemen *Initial Node, Action, Decision/Merge, Fork/Join Paralel, Object Node, Activity Final* vs *Flow Final*; (7.3) Pemodelan Alur Interaksi Lintas *Partition/Swimlane* (Pengguna ↔ Antarmuka ↔ Sistem); (7.4) Audit Konsistensi Skenario Naratif ke *Activity Diagram*.
* **Gambar & Tabel Wajib:** Gambar 7.1 Pemetaan Alur Normal dan Eksepsi Use Case ke *Activity Diagram* Ber-Swimlane.

#### BAB 8: Pemodelan Struktural Statis UML 2.5: *Domain & Design Class Diagram* (Pekan 9)
* **Sub-Pokok Bahasan:** (8.1) Transisi dari Model Fungsional ke Objek: Teknik *Noun-Verb Extraction* dan Pola *Boundary–Control–Entity* (BCE); (8.2) Spesifikasi Atribut, Tipe Data, Metode Operasi, dan *Visibility* (`+`, `-`, `#`); (8.3) Kardinalitas/*Multiplicity* dan Pembedaan Tajam *Association, Aggregation, Composition, Dependency,* serta *Generalization*.
* **Gambar & Tabel Wajib:** Gambar 8.1 Sandingan *Domain Model* vs *Design Class Diagram*; Tabel 8.1 Panduan Memilih *Association, Aggregation,* atau *Composition*.

#### BAB 9: Pemodelan Interaksi Objek Dinamis UML 2.5: *Sequence Diagram* & *Combined Fragments* (Pekan 10)
* **Sub-Pokok Bahasan:** (9.1) Anatomi Sumbu Objek Horizontal dan Sumbu Waktu Vertikal (*Lifeline & Activation Bar*); (9.2) Pola Aliran Pesan BCE (*Actor → Boundary → Controller → Entity*); (9.3) Pesan Sinkron, Asinkron, *Reply Message*, *Create/Destroy*, dan *Self-Delegation*; (9.4) *Combined Fragments* (`alt`, `opt`, `loop`) serta Aturan Konsistensi Metode terhadap *Class Diagram*.
* **Gambar & Tabel Wajib:** Gambar 9.1 Pola Interaksi *Sequence Diagram* dengan Fragmen `loop` dan `alt`; Tabel 9.1 Ceklis Audit Konsistensi *Sequence Diagram* ↔ *Class Diagram*.

#### BAB 10: Pemodelan Daur Hidup Objek Kompleks dengan *State Machine Diagram* UML 2.5 (Pekan 11)
* **Sub-Pokok Bahasan:** (10.1) Kapan Suatu Kelas Membutuhkan *State Machine Diagram*?; (10.2) Notasi *State, Initial/Final Pseudostate, Self-Transition,* dan *Composite State*; (10.3) Format Transisi Lengkap `event [guard condition] / action` dan Aktivitas Internal (`entry/`, `do/`, `exit/`); (10.4) Pencegahan *Trap State* Tak Disengaja dan Transisi Ilegal.
* **Gambar & Tabel Wajib:** Gambar 10.1 *State Machine Diagram* Daur Hidup Pesanan *E-Commerce* dan Tiket Layanan.

#### BAB 11: Pemodelan Arsitektur Sistem: *Package Diagram*, *Component*, & *Deployment Diagram* (Pekan 12)
* **Sub-Pokok Bahasan:** (11.1) Pengorganisasian Kelas Berskala Besar dengan *Layered Package Diagram* dan Aturan Arah Ketergantungan; (11.2) Pengantar *Component Diagram* dan Antarmuka *Provided/Required* (*Lollipop & Socket*); (11.3) *Deployment Diagram*: Pemetaan Artefak Perangkat Lunak ke Node Fisik/Cloud, Kontainer, Basis Data, dan Protokol Jaringan.
* **Gambar & Tabel Wajib:** Gambar 11.1 *Layered Package Diagram* 4 Lapis; Gambar 11.2 *Deployment Diagram* Arsitektur Aplikasi Web/Cloud Modern.

#### BAB 12: Perancangan *Dialog Navigation Diagram* & Penyelarasan Arsitektur terhadap NFR Bisnis (Pekan 13)
* **Sub-Pokok Bahasan:** (12.1) Menyusun Peta Navigasi Layar (*Dialog Navigation Diagram*) Berdasarkan Matriks Hak Akses Aktor (*RBAC*); (12.2) Spesifikasi Aturan Validasi Masukan dan Penanganan Pesan Kesalahan pada SDD; (12.3) Menurunkan Kebutuhan Non-Fungsional (Keamanan, Kinerja, Ketersediaan, Kepatuhan UU PDP) Menjadi Keputusan Arsitektur Konkret. *(Guardrail: estetika visual Figma & uji SUS diampu `STI-308`)*.
* **Gambar & Tabel Wajib:** Gambar 12.1 Contoh *Dialog Navigation Diagram* Multi-Peran; Tabel 12.1 Matriks Pemetaan NFR ke Taktik Arsitektur Sistem.

#### BAB 13: Pemetaan *Class-to-Relational Database Schema* & Spesifikasi Kontrak REST API (Pekan 14)
* **Sub-Pokok Bahasan:** (13.1) Aturan Transformasi *Design Class Diagram* menjadi Skema Relasional 3NF (Kunci Tamu `1:N`, Tabel Asosiasi `M:N`, & 3 Strategi Pemetaan Pewarisan); (13.2) Penyusunan Kamus Data (*Data Dictionary*) pada SDD; (13.3) Merancang Kontrak Antarmuka Modul / **REST API Specification** (*Endpoint, Method, Auth, JSON Request/Response Schema, Error Codes*) sebagai Pegangan Pengembang. *(Guardrail: implementasi kode SQL/ORM & server API diampu `FST-207` dan `STI-416`)*.
* **Gambar & Tabel Wajib:** Gambar 13.1 Tiga Pola Transformasi Pewarisan Kelas ke Tabel Relasional; Tabel 13.1 Templat Baku Spesifikasi Kontrak Endpoint REST API pada SDD.

#### BAB 14: Perakitan *Software Design Document* (SDD IEEE 1016) & Audit *End-to-End Traceability* (Pekan 15)
* **Sub-Pokok Bahasan:** (14.1) Struktur Lengkap Dokumen SDD Berstandar IEEE Std 1016 (*Design Viewpoints: Context, Composition, Logical, Dependency, Information, Interface, Interaction*); (14.2) Menyusun *End-to-End Traceability Matrix* (`SRS ↔ BPMN ↔ Use Case ↔ Class/Sequence ↔ Tabel DB & API`); (14.3) Daftar Periksa Audit Mutu Cetak Biru sebelum Diserahterimakan (*Handoff*) ke `STI-309 Rekayasa Perangkat Lunak` dan `STI-523 Manajemen Proyek TI`.
* **Gambar & Tabel Wajib:** Gambar 14.1 Rantai Keterlacakan Utuh Artefak `STI-306`; Tabel 14.1 Ceklis Audit Kelayakan SDD Siap Konstruksi (20 Butir).
