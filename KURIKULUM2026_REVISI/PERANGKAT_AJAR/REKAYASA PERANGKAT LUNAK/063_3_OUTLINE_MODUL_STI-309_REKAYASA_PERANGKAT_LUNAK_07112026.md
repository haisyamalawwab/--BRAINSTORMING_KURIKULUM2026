# 063_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-309 — REKAYASA PERANGKAT LUNAK (*Software Engineering*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI309` · **Bobot:** 3 SKS Teori · **Semester:** 3  
**CPL:** `CPL-08` (`P4` = 50%) & `CPL-13` (`KK5` = 50%) [Level `R`] · **BoK:** `BK-IS07`, `BK-IT11`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Perangkat Lunak Modern: Proses Agile, Arsitektur Bersih SOLID, Design Patterns, Otomasi Pengujian, & Evaluasi Kualitas ISO/IEC 25010* |
| **Target Tebal Naskah** | 14 Bab Materi Inti + 2 Unit Evaluasi ($\pm 200\text{–}235\text{ halaman}$ A4 dilengkapi sandingan kode *Before–After Refactoring*, diagram *Control Flow Graph*, skrip *Automated Unit Testing*, dan templat audit **ISO/IEC 25010**) |
| **Pagar Pembatas Buku (*Guardrail*)** | Berfokus penuh pada konstruksi modular, arsitektur kode, dan penjaminan mutu pengujian; tidak mengulang elisitasi kebutuhan/BPMN/SRS (`STI-306`) dan tidak membahas penganggaran EVM/kontrak proyek (`STI-523`). |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Model Proses Rekayasa Perangkat Lunak** | **Bab 1** | Krisis Mutu Perangkat Lunak, *Technical Debt*, & Kerangka Profesi **IEEE SWEBOK** | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Model Proses *Plan-Driven*: *Waterfall, Incremental, Spiral,* & **V-Model** | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Rekayasa Adaptif: *Agile Manifesto*, **Scrum Framework**, **Kanban**, & Pemilihan Proses | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Arsitektur Modular, SOLID, & Design Patterns** | **Bab 4** | Gaya Arsitektur Perangkat Lunak Modular & Prinsip *Low Coupling – High Cohesion* | Mg 4 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 5** | Konstruksi Berorientasi Objek Bersih dengan **5 Prinsip Desain SOLID** | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 6** | Katalog **Code Smells** & Disiplin **Refactoring** Sistematis Tanpa Merusak Perilaku | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | UTS (30%) |
| | **Bab 7** | Penerapan **Gang of Four (GoF) Design Patterns** pada Perancangan Subsistem | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Studi Kasus Refactoring Arsitektur, SOLID, & Design Patterns (Persiapan UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Standar Mutu & Perancangan Skenario Pengujian** | **Bab 8** | *Software Quality Assurance* (SQA) & 8 Karakteristik Kualitas **ISO/IEC 25010** | Mg 9 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 9** | Pengujian **White-Box**: *Control Flow Graph*, **Cyclomatic Complexity $V(G)$**, & *Basis Path* | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 10** | Pengujian **Black-Box**: **Equivalence Partitioning**, **BVA**, & *Decision Table* | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Otomasi Pengujian, SCM, & Audit Kualitas** | **Bab 11** | Otomasi **Unit Testing** (*AAA, FIRST*), **Test-Driven Development (TDD)**, & **Mocking** | Mg 12 | `CPMK-4` | `Sub-CPMK-4.2` | UAS (30%) |
| | **Bab 12** | **Integration Testing**, *Regression Suite*, & Evaluasi Kritis *Branch Coverage* | Mg 13 | `CPMK-4` | `Sub-CPMK-4.2` | UAS (30%) |
| | **Bab 13** | *Software Configuration Management* (Git Workflow, PR Review, & *Automated Test Gate*) | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 14** | Penyusunan Laporan Audit Mutu **ISO/IEC 25010** & Serah Terima ke `STI-523`/`STI-625` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Otomasi Pengujian & Sidang Evaluasi Kualitas Perangkat Lunak (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB

#### BAB 1: Krisis Mutu Perangkat Lunak, *Technical Debt*, & Kerangka Profesi IEEE SWEBOK (Pekan 1)
* **Sub-Pokok Bahasan:** Evolusi rekayasa perangkat lunak, studi post-mortem kegagalan *software* terkenal, taksonomi *Technical Debt*, 15 area pengetahuan **IEEE SWEBOK v4**, dan sinergi cetak biru `STI-306` menuju konstruksi `STI-309`.

#### BAB 2: Model Proses *Plan-Driven*: *Waterfall, Incremental, Spiral,* & V-Model (Pekan 2)
* **Sub-Pokok Bahasan:** Anatomi *Waterfall* klasik dan kondisinya yang tepat, pengiriman bertahap *Incremental*, manajemen risiko pada *Boehm's Spiral Model*, serta korespondensi desain–pengujian pada **V-Model**.

#### BAB 3: Rekayasa Adaptif: *Agile Manifesto*, Scrum Framework, Kanban, & Pemilihan Proses (Pekan 3)
* **Sub-Pokok Bahasan:** Empat nilai & 12 prinsip Agile, aturan resmi **Scrum Guide** (3 peran, 5 acara, 3 artefak + *Definition of Done*), aliran tarik **Kanban** (*WIP Limits, Cycle Time*), serta matriks multi-kriteria memilih model proses yang terjustifikasi untuk konteks industri.

#### BAB 4: Gaya Arsitektur Perangkat Lunak Modular & Prinsip *Low Coupling – High Cohesion* (Pekan 4)
* **Sub-Pokok Bahasan:** *Monolithic vs Modular Monolith*, *Layered Architecture*, *Model-View-Controller* (MVC), *Pipe-and-Filter*, *Event-Driven*, jenis-jenis *coupling* & *cohesion*, serta aturan arah ketergantungan antar-lapisan.

#### BAB 5: Konstruksi Berorientasi Objek Bersih dengan 5 Prinsip Desain SOLID (Pekan 5)
* **Sub-Pokok Bahasan:** Prinsip *Clean Code* (penamaan bermakna, fungsi terfokus, penanganan eksepsi) dan pembedahan kode *Before–After* untuk **SRP, OCP, LSP, ISP,** serta **DIP** (*Dependency Injection* untuk keterujian modul).

#### BAB 6: Katalog Code Smells & Disiplin Refactoring Sistematis Tanpa Merusak Perilaku (Pekan 6)
* **Sub-Pokok Bahasan:** Pendeteksian *Bloaters* (*Long Method, Large Class*), *Object-Orientation Abusers* (*Switch Statements*), *Change Preventers* (*Shotgun Surgery*), *Dispensables*, dan *Couplers* (*Feature Envy*), beserta prosedur aman *Refactoring* Martin Fowler.

#### BAB 7: Penerapan Gang of Four (GoF) Design Patterns pada Perancangan Subsistem (Pekan 7)
* **Sub-Pokok Bahasan:** Kapan memakai dan kapan menghindari *Design Patterns*; bedah mendalam **Singleton**, **Factory Method**, **Adapter**, **Facade**, **Strategy**, dan **Observer** lengkap diagram UML dan implementasi kodenya.

#### BAB 8: *Software Quality Assurance* (SQA) & 8 Karakteristik Kualitas ISO/IEC 25010 (Pekan 9)
* **Sub-Pokok Bahasan:** Perbedaan *Quality Control* vs *Quality Assurance* dan *Verification* vs *Validation*; bedah lengkap 8 dimensi **ISO/IEC 25010** (*Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability*) beserta rumus metrik pengukurannya.

#### BAB 9: Pengujian White-Box: *Control Flow Graph*, Cyclomatic Complexity $V(G)$, & *Basis Path* (Pekan 10)
* **Sub-Pokok Bahasan:** Transformasi struktur kendali kode ke **Control Flow Graph (CFG)**, pemecahan predikat majemuk (*short-circuit boolean*), 3 rumus **Cyclomatic Complexity McCabe**, ekstraksi *Independent Basis Paths*, dan penyusunan kasus uji pencapai *Statement & Branch Coverage*.

#### BAB 10: Pengujian Black-Box: Equivalence Partitioning, BVA, & *Decision Table* (Pekan 11)
* **Sub-Pokok Bahasan:** Partisi kelas valid dan tidak valid pada **Equivalence Partitioning (EP)**, pengujian tepi tajam 2-nilai dan 3-nilai pada **Boundary Value Analysis (BVA)**, penyusunan **Decision Table Testing** untuk aturan bisnis kombinatorial, serta standar dokumentasi kasus uji.

#### BAB 11: Otomasi Unit Testing (*AAA, FIRST*), Test-Driven Development (TDD), & Mocking (Pekan 12)
* **Sub-Pokok Bahasan:** Anatomi pengujian unit otomatis (*Arrange–Act–Assert*), prinsip **F.I.R.S.T.**, parameterisasi uji, pengujian eksepsi, siklus **TDD (*Red–Green–Refactor*)**, serta isolasi dependensi eksternal menggunakan *Stub, Fake, Spy,* dan *Mock*.

#### BAB 12: Integration Testing, *Regression Suite*, & Evaluasi Kritis *Branch Coverage* (Pekan 13)
* **Sub-Pokok Bahasan:** Piramida pengujian perangkat lunak, strategi integrasi *Top-Down, Bottom-Up,* dan *Contract/API Layer Integration*, pemeliharaan *Regression Test Suite*, serta analisis kritis *Line Coverage vs Branch Coverage vs Mutation Mindset*.

#### BAB 13: *Software Configuration Management* (Git Workflow, PR Review, & *Automated Test Gate*) (Pekan 14)
* **Sub-Pokok Bahasan:** Konsep *Baseline* & *Semantic Versioning*, alur kerja *Feature-Branch & Pull Request*, daftar periksa *Peer Code Review*, dan konfigurasi ringkas *GitHub Actions* sebagai penjaga gerbang pengujian otomatis (*Automated Test Gate*).

#### BAB 14: Penyusunan Laporan Audit Mutu ISO/IEC 25010 & Serah Terima ke `STI-523`/`STI-625` (Pekan 15)
* **Sub-Pokok Bahasan:** Siklus hidup pelaporan cacat (*Defect Severity vs Priority*), penyusunan **SQA Plan & Test Execution Report**, agregasi metrik statis + dinamis ke rapor evaluasi **ISO/IEC 25010**, serta peta *handoff* menuju `STI-523 Manajemen Proyek TI` dan `STI-625 Rekayasa Platform Digital`.
