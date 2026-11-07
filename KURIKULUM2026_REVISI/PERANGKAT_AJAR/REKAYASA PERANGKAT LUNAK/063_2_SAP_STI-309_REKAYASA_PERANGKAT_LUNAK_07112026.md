# 063_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-309 — REKAYASA PERANGKAT LUNAK (*Software Engineering*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI309` · **Bobot:** 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · **Semester:** 3  
**Prasyarat:** `FST-203` Struktur Data dan Algoritma · **CPL:** `CPL-08` (`P4` = 50%) & `CPL-13` (`KK5` = 50%) [Level `R`]  
**Klaster Rubrik:** `K-4` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu `STI-309` |
|---|---|
| **Struktur Waktu per Sesi** | **Pendahuluan `20'` · Kegiatan Inti `110'` · Penutup & Refleksi `20'`** (Total Tatap Muka = `150 menit`), diikuti `PT 180'` dan `BM 180'`. |
| **Fokus Keilmuan (*In-Scope*)** | *How to build and test software correctly*: pemilihan model proses (*Waterfall, V-Model, Scrum, Kanban*), arsitektur modular, prinsip **SOLID**, *Refactoring Code Smells*, **GoF Design Patterns**, perancangan uji **White-Box** & **Black-Box**, otomasi *Unit/Integration Testing* & TDD, serta evaluasi mutu **ISO/IEC 25010**. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** menugaskan ulang elisitasi kebutuhan bisnis/BPMN/SRS dari nol (sudah diampu **`STI-306 Analisis dan Perancangan Sistem Informasi`** — luaran proyek `STI-309` wajib berupa kode ter-*refactor*, *automated test suite*, & laporan SQA ISO/IEC 25010!). Dilarang membahas EVM/anggaran/kontrak proyek (**`STI-523 Manajemen Proyek TI`**). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Perkuliahan | Metode Utama | Waktu TM | Evaluasi |
|:---:|:---:|---|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Krisis Perangkat Lunak, *Technical Debt*, & Standar **IEEE SWEBOK** | Kuliah Interaktif & Bedah Insiden | 150' | Formatif |
| **2** | `Sub-CPMK-1.1` | Model Proses *Plan-Driven*: *Waterfall*, *Incremental*, *Spiral*, & **V-Model** | Ceramah & Analisis Kasus | 150' | Formatif |
| **3** | `Sub-CPMK-1.2` | Pengembangan Adaptif: *Agile Manifesto*, **Scrum**, **Kanban**, & Matriks Pemilihan | *Case Method* & Simulasi Sprint | 150' | Formatif |
| **4** | `Sub-CPMK-2.1` | Arsitektur Modular (*Layered, MVC, Event-Driven*) & *Coupling/Cohesion* | *Problem-Solving* + Verifikasi T1 | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Konstruksi Bersih & Penerapan **5 Prinsip Desain SOLID** | *Case-Based Code Workshop* | 150' | Formatif |
| **6** | `Sub-CPMK-2.1, 2.2` | Deteksi **Code Smells** & Teknik **Refactoring** Sistematis | *Problem-Based Learning* | 150' | Formatif |
| **7** | `Sub-CPMK-2.2` | **GoF Design Patterns** (*Creational, Structural, Behavioral*) & Klinik UTS | *Case Method Class* | 150' | Formatif |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** Arsitektur Modular, **SOLID**, *Refactoring*, & **GoF** | Ujian Tertulis Studi Kasus Kode | 150' | **UTS (30%)** |
| **9** | `Sub-CPMK-4.1` | *Software Quality Assurance* (SQA) & 8 Karakteristik Standar **ISO/IEC 25010** | Kuliah Interaktif & Studi Mutu | 150' | Formatif |
| **10** | `Sub-CPMK-3.1` | **White-Box Testing**: *Control Flow Graph*, **Cyclomatic Complexity $V(G)$**, & *Basis Path* | *Problem-Solving Class* | 150' | Formatif |
| **11** | `Sub-CPMK-3.2` | **Black-Box Testing**: **Equivalence Partitioning**, **BVA**, & *Decision Table* | *Case-Based Learning* | 150' | Formatif |
| **12** | `Sub-CPMK-4.2` | Otomasi **Unit Testing** (*AAA*), **TDD**, **Mocking**, & Verifikasi **Tugas 2** | *Workshop* Pengujian + T2 | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-4.2` | **Integration Testing**, *Regression Testing*, & Analisis *Code Coverage* | *Problem-Solving Class* | 150' | Formatif |
| **14** | `Sub-CPMK-4.1, 4.2` | *Software Configuration Management* (Git Branch/PR) & *Automated Test Gate* CI | Ceramah & Demo Repositori | 150' | Formatif |
| **15** | `Sub-CPMK-4.1, 4.2` | Penyusunan Laporan Audit Kualitas **ISO/IEC 25010** & Simulasi Sidang SQA | Presentasi & Klinik Pra-UAS | 150' | Formatif |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Demo *Automated Testing* & Evaluasi ISO/IEC 25010 | Sidang Mutu & Ujian Individu | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Krisis Perangkat Lunak, *Technical Debt*, & Standar IEEE SWEBOK
* **Sub-CPMK:** `Sub-CPMK-1.1` (Pengantar, C2→C4) · **Media:** Salindia Bab 1, Studi Kasus Insiden Perangkat Lunak, LMS Edlink.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Memaparkan kontrak belajar dan membedah insiden nyata kegagalan rekayasa perangkat lunak (*Therac-25, Ariane 5, Knight Capital $440M bug*) yang membuktikan bahwa sekadar "kode bisa jalan" tidak sama dengan perangkat lunak berkualitas rekayasa.
  - **Kegiatan Inti (110'):** Menguraikan konsep *Technical Debt* Ward Cunningham, 15+ *Knowledge Areas* pada **IEEE SWEBOK**, perbedaan tegas peran `STI-306` (menghasilkan spesifikasi SRS & SDD) dengan `STI-309` (merancang struktur kode bersih, mengonstruksi secara modular, dan memverifikasi mutu secara terukur), serta pembagian kelompok audit & rekayasa kode (3 mahasiswa/tim).
  - **Penutup (20'):** Merangkum peta kompetensi semester dan menugaskan pembacaan bab model proses Pressman.
* **PT (`180'`) & BM (`180'`):** Merangkum perbandingan masalah biaya pemeliharaan perangkat lunak pada sistem tanpa disiplin rekayasa.

### PERTEMUAN 2 — Model Proses *Plan-Driven*: *Waterfall*, *Incremental*, *Spiral*, & **V-Model**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Media:** Diagram Alir Proses SDLC, Matriks Risiko Proyek.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menanyakan apakah membangun perangkat lunak kontrol alat pacu jantung dapat memakai cara kerja yang sama dengan membangun fitur eksperimen aplikasi sosial media.
  - **Kegiatan Inti (110'):** Menganalisis anatomi, asumsi dasar, kelebihan, dan kondisi gagal dari **Waterfall**, **Incremental Delivery**, **Risk-Driven Spiral Model** Barry Boehm, serta **V-Model** (menunjukkan korespondensi ketat antara *Requirements ↔ Acceptance Test*, *Architecture ↔ System/Integration Test*, dan *Module Design ↔ Unit Test*).
  - **Penutup (20'):** Kuis cepat 5 skenario penentuan kapan model *Plan-Driven* mutlak diperlukan.
* **PT (`180'`) & BM (`180'`):** Menganalisis studi kasus proyek pemerintah/perbankan dan mengevaluasi kecocokan *V-Model*.

### PERTEMUAN 3 — Metodologi Adaptif: *Agile Manifesto*, **Scrum**, & **Kanban**
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] · **Media:** *The Scrum Guide 2020*, Papan Simulasi Kanban, LMS Edlink.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Membedah 4 nilai dan 12 prinsip *Agile Manifesto* serta meluruskan kesalahpahaman bahwa *"Agile berarti koding langsung tanpa desain dan tanpa dokumentasi"*.
  - **Kegiatan Inti (110'):** Menguraikan secara presisi kerangka **Scrum** (*Product Owner, Scrum Master, Developers*; *Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective*; *Product Backlog, Sprint Backlog, Increment* + **Definition of Done**), aliran tarik **Kanban** (*Visualize Workflow, Limit Work-in-Progress / WIP, Manage Flow*), serta matriks multi-kriteria pemilihan proses (*kejelasan kebutuhan, kritikalitas keselamatan, ukuran tim, budaya klien*). Merilis resmi **Tugas 1 (RTM-1)**.
  - **Penutup (20'):** Menjelaskan rubrik penilaian Tugas 1 yang dikumpulkan pekan depan.
* **PT (`180'`) & BM (`180'`):** Menyusun makalah analisis pemilihan & justifikasi model proses untuk 3 skenario industri (**Tugas 1**).

### PERTEMUAN 4 — Arsitektur Perangkat Lunak Modular (*Coupling & Cohesion*) + Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Media:** Diagram Arsitektur, LMS Edlink.
* **Skenario (`25' / 105' / 20'`):**
  - **Pendahuluan (25'):** Melaksanakan kuis verifikasi tertulis 20 menit atas makalah **Tugas 1 (`CPMK-1`)**.
  - **Kegiatan Inti (105'):** Mengajarkan pola arsitektur perangkat lunak (*Monolithic vs Modular Monolith, Layered Architecture [Presentation–Application–Domain–Infrastructure], MVC, Pipe-and-Filter,* dan *Event-Driven*), serta ukuran fundamental kualitas desain struktural: **Low Coupling** (meminimalkan ketergantungan silang antar-modul) dan **High Cohesion** (satu modul fokus mengerjakan satu tanggung jawab yang utuh).
  - **Penutup (20'):** Bedah cepat contoh aplikasi yang mencampur kueri basis data langsung di dalam kode tampilan UI (*pelanggaran parah pemisahan lapisan!*).
* **PT (`180'`) & BM (`180'`):** Memetakan ulang struktur direktori & lapisan sebuah subsistem contoh agar ber-*coupling* rendah.

### PERTEMUAN 5 — Konstruksi Bersih & Penerapan **5 Prinsip Desain SOLID**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Media:** Potongan Kode Studi Kasus OOP (Python/TypeScript/Java), Proyektor.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menampilkan kelas `OrderManager` raksasa 300 baris yang menghitung pajak, menyimpan SQL, mencetak PDF, sekaligus mengirim email — apa yang terjadi setiap kali aturan diskon berubah?
  - **Kegiatan Inti (110'):** Membedah dan melatih penerapan satu per satu kelima prinsip **SOLID** Robert C. Martin: **S**ingle Responsibility Principle, **O**pen/Closed Principle, **L**iskov Substitution Principle, **I**nterface Segregation Principle, dan **D**ependency Inversion Principle (*bergantung pada abstraksi/interface, bukan kelas konkret sehingga mudah diuji unit test!*).
  - **Penutup (20'):** Menyimpulkan hubungan langsung antara kepatuhan SOLID (khususnya DIP & SRP) dengan kemudahan pengujian otomatis di paruh kedua semester.
* **PT (`180'`) & BM (`180'`):** Mengerjakan lembar kerja perbaikan 5 kasus pelanggaran SOLID.

### PERTEMUAN 6 — Deteksi **Code Smells** & Teknik **Refactoring** Sistematis
* **Sub-CPMK:** `Sub-CPMK-2.1` & `2.2` [C3→C4] · **Media:** Repositori Latihan *Refactoring Kata*, Buku Fowler.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Memperkenalkan definisi tegas **Refactoring**: *mengubah struktur internal kode agar lebih bersih dan mudah dipelihara TANPA mengubah perilaku eksternal yang diamati pengguna*.
  - **Kegiatan Inti (110'):** Mengajarkan deteksi katalog **Code Smells** (*Long Method, Large/God Class, Long Parameter List, Divergent Change, Shotgun Surgery, Feature Envy, Switch Statements, Duplicate Code*) serta langkah aman mengeksekusi *Extract Function/Method, Introduce Parameter Object, Move Method,* dan *Replace Conditional with Polymorphism*.
  - **Penutup (20'):** Meninjau hasil *refactoring* dua pasangan mahasiswa di layar kelas.
* **PT (`180'`) & BM (`180'`):** Mengaudit dan me-*refactor* kode modul studi kasus tim untuk persiapan proyek mutu semester.

### PERTEMUAN 7 — **GoF Design Patterns** (*Creational, Structural, Behavioral*) & Klinik Pra-UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` [C3] · **Media:** Diagram UML Pola GoF & Contoh Implementasi Kode.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Mengingatkan prinsip bijak rekayasa: *Design Pattern adalah obat untuk masalah desain spesifik, bukan hiasan yang dipaksakan ke semua kelas!*
  - **Kegiatan Inti (110'):** Membedah konteks masalah, struktur kelas, dan penerapan kode dari 6 **Gang of Four (GoF) Design Patterns** paling esensial di industri: *Creational* (**Singleton**, **Factory Method**), *Structural* (**Adapter** untuk membungkus API pihak ketiga yang tak seragam, **Facade** untuk menyederhanakan subsistem rumit), dan *Behavioral* (**Strategy** untuk menukar algoritma ongkir/pembayaran saat *runtime*, **Observer** untuk notifikasi terlepas-erat), dilanjutkan klinik simulasi soal **UTS Pekan 8**.
  - **Penutup (20'):** Menyampaikan kisi-kisi resmi dan rubrik penilaian **UTS (`CPMK-2`, 30%)**.
* **PT (`180'`) & BM (`180'`):** Belajar mandiri persiapan UTS atas materi Pekan 4–7.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3/C4]) · **Bobot:** **30%** · **Durasi:** `150 menit` (Tertulis Luring Terjadwal).
* **Pelaksanaan:** Mahasiswa mengerjakan 3 studi kasus rekayasa desain kode secara mandiri (*closed-book*): (1) Dekomposisi arsitektur berlapis ber-*coupling* rendah; (2) Diagnosis *Code Smells* & penulisan ulang kode patuh **SOLID**; (3) Perancangan solusi ekstensi subsistem menggunakan **GoF Design Pattern**.

### PERTEMUAN 9 — *Software Quality Assurance* (SQA) & Standar Kualitas **ISO/IEC 25010**
* **Sub-CPMK:** `Sub-CPMK-4.1` [C2→C5] · **Media:** Bagan Taksonomi ISO/IEC 25010, LMS Edlink.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Membahas umpan balik hasil UTS dan membedakan secara tajam pertanyaan Boehm: **Verification** (*"Are we building the product right?"*) vs **Validation** (*"Are we building the right product?"*).
  - **Kegiatan Inti (110'):** Menguraikan model kualitas produk **ISO/IEC 25010** beserta 8 karakteristik utamanya (*Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability*) dan 31 sub-karakteristiknya, serta cara menerjemahkan setiap karakteristik menjadi metrik rekayasa yang objektif (mis. *Maintainability* $\leftarrow$ *Cyclomatic Complexity* rata-rata $\le 10$, duplikasi $< 3\%$, *test coverage* $\ge 80\%$).
  - **Penutup (20'):** Menugaskan tim memilih 5 karakteristik prioritas ISO/IEC 25010 untuk diaudit pada proyek akhir UAS.
* **PT (`180'`) & BM (`180'`):** Menyusun draf matriks kualitas ISO/IEC 25010 untuk subsistem perangkat lunak proyek tim.

### PERTEMUAN 10 — **White-Box Testing**: *Control Flow Graph*, **Cyclomatic Complexity $V(G)$**, & *Basis Path*
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Media:** Papan Tulis, Lembar Kerja CFG, LMS Edlink.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menunjukkan sebuah fungsi 25 baris dengan `if-elif-while` bersarang yang tampak "sudah dites 2 kali dan berhasil", padahal 40% cabangnya belum pernah tersentuh eksekusi dan menyimpan *bug* pembagian nol!
  - **Kegiatan Inti (110'):** Mengajarkan metode **Basis Path Testing** Tom McCabe: menerjemahkan kode prosedural/metode kelas ke **Control Flow Graph (CFG)** (memecah kondisi majemuk `A and B` menjadi simpul predikat terpisah!), menghitung **Cyclomatic Complexity** dengan 3 cara ($V(G) = E - N + 2P$, jumlah *region* tertutup $+1$, dan jumlah simpul predikat sederhana $+1$), menentukan himpunan jalur independen linier, serta menurunkan data uji konkret untuk setiap jalur hingga mencapai 100% *Branch Coverage*. Merilis resmi **Tugas 2 (RTM-2)**.
  - **Penutup (20'):** Memeriksa hasil penggambaran CFG dan nilai $V(G)$ latihan kelas.
* **PT (`180'`) & BM (`180'`):** Mengerjakan bagian perancangan uji *White-Box* pada **Tugas 2**.

### PERTEMUAN 11 — **Black-Box Testing**: **Equivalence Partitioning**, **BVA**, & *Decision Table*
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] · **Media:** Spesifikasi Aturan Bisnis SRS, Templat Tabel Kasus Uji.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Mengapa *bug* paling sering bersembunyi tepat di angka batas (`0`, `1`, `min-1`, `max`, `max+1`) akibat kesalahan operator `<` vs `<=`?
  - **Kegiatan Inti (110'):** Mengajarkan teknik perancangan skenario uji berbasis spesifikasi fungsional tanpa melihat kode internal (**Black-Box**): pembagian partisi valid & tidak valid pada **Equivalence Partitioning (EP)**, pemilihan titik uji tajam **Boundary Value Analysis (BVA)** (`min-1, min, min+1` dan `max-1, max, max+1`), serta **Decision Table Testing** untuk menguji interaksi kombinasi aturan bisnis (mis. aturan diskon anggota × metode bayar × kuota promo).
  - **Penutup (20'):** Mengingatkan tenggat pengumpulan **Tugas 2 (`CPMK-3`, 20%)** pekan depan.
* **PT (`180'`) & BM (`180'`):** Menyelesaikan dokumen spesifikasi pengujian *White-Box & Black-Box* untuk **Tugas 2**.

### PERTEMUAN 12 — Otomasi **Unit Testing**, **TDD**, **Mocking**, & Verifikasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-4.2` [C4→C5] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 20%)** · **Media:** `Pytest` / `Jest`, Proyektor.
* **Skenario (`25' / 105' / 20'`):**
  - **Pendahuluan (25'):** Melaksanakan kuis verifikasi tertulis 20 menit atas dokumen **Tugas 2 (`CPMK-3`)**.
  - **Kegiatan Inti (105'):** Mendemonstrasikan transformasi tabel kasus uji manual Pekan 10–11 menjadi skrip **Automated Unit Tests** berpola **Arrange–Act–Assert (AAA)** dan prinsip **F.I.R.S.T.** (*Fast, Isolated/Independent, Repeatable, Self-Validating, Timely*), mempraktikkan siklus **Test-Driven Development (TDD: *Red → Green → Refactor*)**, serta teknik **Mocking / Stubbing** agar pengujian logika domain berjalan dalam milidetik tanpa menyentuh server basis data atau gerbang pembayaran asli.
  - **Penutup (20'):** Menugaskan konversi kasus uji Tugas 2 ke dalam *automated test suite* repositori tim.
* **PT (`180'`) & BM (`180'`):** Menulis minimal 20 fungsi *automated unit test* (termasuk *mocking* & pengujian eksepsi batas) pada repositori proyek.

### PERTEMUAN 13 — **Integration Testing**, *Regression Testing*, & Evaluasi Metrik *Code Coverage*
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Media:** Laporan `pytest-cov` / `c8`, Piramida Pengujian Mike Cohn.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menampilkan meme klasik rekayasa perangkat lunak: *"2 unit tests, 0 integration tests"* — dua pintu geser bekerja sempurna sendiri-sendiri, tetapi saling bertabrakan saat dipasang bersama!
  - **Kegiatan Inti (110'):** Mengajarkan **Testing Pyramid** (*Unit → Integration → E2E*), strategi integrasi (*Top-Down* dengan *Stubs*, *Bottom-Up* dengan *Drivers*, serta pengujian integrasi lapisan *Service–Repository*), pentingnya *Automated Regression Suite* saat *refactoring*, serta cara membaca kritis metrik **Statement Coverage vs Branch Coverage** (mengapa 90% *line coverage* tanpa *assertion* yang bermakna tetap berbahaya!).
  - **Penutup (20'):** Mengevaluasi laporan *coverage* awal dari 2 kelompok di kelas.
* **PT (`180'`) & BM (`180'`):** Menambahkan *integration tests* dan meningkatkan *branch coverage* proyek hingga $\ge 80\%$.

### PERTEMUAN 14 — *Software Configuration Management* (Git Workflow) & *Automated Test Gate* CI Dasar
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C4→C5] · **Media:** GitHub Repository, *GitHub Actions* Ringan.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Bagaimana mencegah anggota tim menggabungkan (*merge*) kode rusak ke cabang `main` pada pukul 23:55 malam sebelum rilis?
  - **Kegiatan Inti (110'):** Menguraikan prinsip **Software Configuration Management (SCM)**: *baseline*, *Semantic Versioning* (`MAJOR.MINOR.PATCH`), alur kolaborasi *Feature Branch + Pull Request + Peer Code Review Checklist*, serta pemasangan skrip **Automated Test Gate** sederhana pada *GitHub Actions* yang otomatis menjalankan seluruh *unit & integration tests* setiap ada *Pull Request* *(menjaga guardrail: orkestrasi kontainer/cloud lanjut dibahas di `STI-417` dan `STB-601`)*.
  - **Penutup (20'):** Memeriksa kebersihan riwayat *commit* dan status centang hijau (*passing tests*) repositori tim.
* **PT (`180'`) & BM (`180'`):** Merapikan alur *Pull Request*, dokumentasi `README.md`, dan mengaktifkan eksekusi pengujian otomatis di repositori proyek.

### PERTEMUAN 15 — Penyusunan Laporan Evaluasi Mutu **ISO/IEC 25010** & Klinik Pra-UAS
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C5] · **Media:** Templat *SQA & ISO/IEC 25010 Quality Evaluation Report*.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menjelaskan struktur laporan akhir evaluasi mutu perangkat lunak yang menyatukan seluruh bukti kuantitatif semester.
  - **Kegiatan Inti (110'):** Melaksanakan *Mock SQA Audit & Coaching Clinic*: setiap tim memaparkan ringkasan perubahan *coupling/Cyclomatic Complexity* sebelum vs sesudah *refactoring* SOLID/GoF, hasil eksekusi *automated unit & integration tests*, persentase *branch coverage*, catatan *defect log*, dan penilaian objektif terhadap karakteristik **ISO/IEC 25010**.
  - **Penutup (20'):** Menjelaskan tata tertib pelaksanaan **UAS Pekan 16 (`CPMK-4`, 30%)**.
* **PT (`180'`) & BM (`180'`):** Finalisasi bundel repositori Git dan **Laporan Evaluasi Kualitas ISO/IEC 25010** siap diuji.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Bundel Repositori Kode Ter-*Refactor*, *Automated Test Suite*, & Laporan Evaluasi Mutu ISO/IEC 25010 (50% nilai UAS)** dengan **Sidang *Live Test Execution* & Ujian Verifikasi Individu (50% nilai UAS)** di mana dosen menguji kemampuan setiap mahasiswa menjelaskan metrik ISO/IEC 25010, menulis/memodifikasi *unit test/mock* langsung, dan menafsirkan laporan *branch coverage*.
