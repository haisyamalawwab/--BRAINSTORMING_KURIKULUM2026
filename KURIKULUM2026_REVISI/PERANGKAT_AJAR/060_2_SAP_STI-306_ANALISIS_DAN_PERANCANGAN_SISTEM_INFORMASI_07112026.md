# 060_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-306 — ANALISIS DAN PERANCANGAN SISTEM INFORMASI (*Information Systems Analysis and Design*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI306` · **Bobot:** 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · **Semester:** 3  
**Prasyarat:** `STI-101` Pengantar Sistem dan Teknologi Informasi (Kurikulum OBE SISTEKIN 2026), `FST-207` Sistem Basis Data  
**CPL:** `CPL-02` (`KU1` = 20%) & `CPL-06` (`P2` = 80%) [Level `R`] · **Klaster Rubrik:** `K-4`  
**Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu `STI-306` |
|---|---|
| **Struktur Waktu per Sesi** | **Pendahuluan `20'` · Kegiatan Inti `110'` · Penutup & Refleksi `20'`** (Total Tatap Muka = `150 menit`), diikuti `PT 180'` dan `BM 180'`. |
| **Fokus Keilmuan (*In-Scope*)** | Elisitasi kebutuhan pemangku kepentingan, dokumen SRS IEEE 830 / ISO 29148, pemodelan proses bisnis BPMN 2.0 (*As-Is* & *To-Be*), pemodelan UML 2.5 fungsional & struktural, serta penyusunan dokumen cetak biru arsitektur SDD IEEE 1016. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ Dosen **dilarang** menugaskan koding aplikasi/*source code* atau *unit testing* (`STI-309 Rekayasa Perangkat Lunak`); dilarang membahas perhitungan biaya EVM/kontrak proyek (`STI-523 Manajemen Proyek TI`); dilarang mengeksekusi otomasi bot RPA/*Camunda engine* (`STC-601`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Perkuliahan | Metode Utama | Waktu TM | Evaluasi |
|:---:|:---:|---|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Kontrak Belajar, Krisis Kebutuhan Sistem, Siklus SDLC, & Peran *System Analyst* | Kuliah Interaktif & Studi Kasus | 150' | Formatif |
| **2** | `Sub-CPMK-1.1` | Teknik Elisitasi Kebutuhan (*Interview, Observation, JAD*) & Klasifikasi FR/NFR | *Role-Play Stakeholder Interview* | 150' | Formatif |
| **3** | `Sub-CPMK-1.2` | Penyusunan Dokumen *Software Requirements Specification* (SRS IEEE 830 / ISO 29148) | Workshop Dokumen & *Peer Review* | 150' | Formatif |
| **4** | `Sub-CPMK-2.1` | Standar Notasi Pemodelan Proses Bisnis **BPMN 2.0** (*Pools, Lanes, Events, Gateways*) | *Problem-Solving Class* BPMN | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.2` | Analisis Efisiensi Proses Bisnis *As-Is* vs *To-Be* & *Business Process Redesign* | *Case Method Workshop* | 150' | Formatif |
| **6** | `Sub-CPMK-3.1` | Pemodelan Fungsional UML 2.5: *Use Case Diagram* & Spesifikasi Skenario Naratif | *Case-Based Learning* UML | 150' | Formatif |
| **7** | `Sub-CPMK-3.1` | Pemodelan Alur Aktivitas Kompleks: *Activity Diagram* UML 2.5 & Audit Pra-UTS | *Problem-Solving* & Klinik UTS | 150' | Formatif |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** Studi Kasus Pemodelan BPMN 2.0 & Analisis *As-Is/To-Be* | *Case-Method Written Exam* | 150' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.2` | Pemodelan Struktural Statis UML 2.5: *Domain & Design Class Diagram* | *Case Method Class* | 150' | Formatif |
| **10** | `Sub-CPMK-3.2` | Pemodelan Interaksi Objek Dinamis UML 2.5: *Sequence Diagram* & *Combined Fragments* | *Problem-Solving Workshop* | 150' | Formatif |
| **11** | `Sub-CPMK-3.2` | Pemodelan Siklus Status Objek Kompleks: *State Machine Diagram* UML 2.5 | *Case-Based Learning* | 150' | Formatif |
| **12** | `Sub-CPMK-4.1` | Pemodelan Arsitektur Sistem: *Package Diagram* & *Deployment Diagram* | Ceramah & Latihan Arsitektur | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-4.2` | Perancangan *Dialog Navigation Diagram* & Penyelarasan Desain terhadap NFR Bisnis | *Case Method* & *Walkthrough* | 150' | Formatif |
| **14** | `Sub-CPMK-4.1` | Pemetaan *Class-to-Database Schema* & Spesifikasi Kontrak Antarmuka REST API pada SDD | Workshop Spesifikasi Teknis SDD | 150' | Formatif |
| **15** | `Sub-CPMK-4.2` | Audit *End-to-End Traceability* (SRS–BPMN–UML–SDD) & Simulasi Sidang Stakeholder | *Mock Review* & *Coaching Clinic* | 150' | Formatif |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Dokumen Desain Sistem (SDD) & Pertahanan Individu | Sidang SDD & Tanya-Jawab Kritis | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Pengantar SDLC, Peran *System Analyst*, & Kontrak Proyek Mitra
* **Sub-CPMK:** `Sub-CPMK-1.1` (Pengantar, C2→C4) · **Media:** Proyektor, LMS Edlink, Contoh Artefak SRS/SDD Nyata.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Memaparkan kontrak belajar, skema 4 evaluasi OBE, dan kisah nyata kegagalan proyek TI bernilai miliaran rupiah bukan karena koding buruk, melainkan karena salah menangkap kebutuhan pengguna. | Menyimak, menyepakati aturan akademik, dan mengerjakan kuis pemantik 5 soal di LMS Edlink. | 20' | RPS `060_1` |
| **Kegiatan Inti** | Menguraikan fase SDLC (*Planning, Analysis, Design, Implementation*), posisi strategis *System Analyst* sebagai penerjemah bisnis-ke-teknis, perbandingan pendekatan *Plan-Driven* vs *Iterative/Agile*, serta batas tegas antara cetak biru `STI-306` dengan konstruksi kode `STI-309`. | Membentuk kelompok studi kasus 3–4 mahasiswa, mendiskusikan kandidat organisasi mitra nyata (UMKM, klinik, koperasi, sekolah, atau unit layanan publik Malang Raya), dan memetakan gejala masalah awalnya. | 110' | `[1]` Bab 1; `[2]` Bab 1 |
| **Penutup** | Merangkum benang merah artefak semester (`SRS → BPMN → UML → SDD`) dan menugaskan survei profil mitra. | Mencatat agenda kunjungan/wawancara awal mitra studi kasus untuk Pekan 2. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Menyusun lembar profil organisasi mitra (1 halaman) dan membaca Dennis Bab 3 tentang elisitasi kebutuhan.

---

### PERTEMUAN 2 — Teknik Elisitasi Kebutuhan & Klasifikasi Kebutuhan Fungsional / Non-Fungsional
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Media:** Panduan Wawancara, Matriks PIECES/FURPS+, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan contoh kalimat permintaan klien yang kabur (*"Saya ingin sistem yang cepat dan mudah"*) dan menantang kelas mengubahnya menjadi spesifikasi terukur. | Mengidentifikasi celah ambiguitas pada pernyataan klien dan mengusulkan metrik kuantitatif. | 20' | `[1]` Bab 3 |
| **Kegiatan Inti** | Menjelaskan 5 teknik elisitasi (*Interview, Questionnaire, Observation, Document Analysis, JAD*), kerangka identifikasi masalah PIECES, serta pemilahan tegas *Functional Requirements* (FR) vs *Non-Functional Requirements* (NFR: kinerja, keamanan, keandalan, kegunaan, kepatuhan regulasi). Memandu simulasi *role-play* wawancara analis–klien di kelas. | Melakukan *role-play* berpasangan (1 grup menjadi manajemen klinik/toko, 1 grup menjadi tim analis sistem), menggali kebutuhan tersembunyi, lalu menuliskan daftar FR dan NFR terukur. | 110' | `[1]` Bab 3; `[2]` Bab 3; `[5]` |
| **Penutup** | Mengevaluasi 3 kesalahan umum pewawancara pemula (pertanyaan mengarahkan, melompat ke solusi teknis terlalu dini). | Menyempurnakan protokol wawancara untuk diterapkan ke mitra riil pekan ini. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Melaksanakan wawancara/observasi pada mitra studi kasus dan menyusun daftar minimal 15 butir kebutuhan mentah beserta bukti dokumentasi.

---

### PERTEMUAN 3 — Penyusunan Dokumen *Software Requirements Specification* (SRS IEEE 830 / ISO 29148)
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] · **Media:** Templat Resmi SRS IEEE 830, Contoh RTM, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengulas temuan lapangan mahasiswa dari Pekan 2 dan menjelaskan fungsi hukum/teknis dokumen SRS sebagai "kontrak spesifikasi" antara pemilik bisnis dan pengembang. | Berbagi temuan unik dari wawancara mitra masing-masing. | 20' | `[5]` |
| **Kegiatan Inti** | Membedah anatomi standar **IEEE 830 / ISO 29148** (Pendahuluan & Ruang Lingkup, Deskripsi Umum & Karakteristik Pengguna, Spesifikasi Kebutuhan Fungsional berkode `FR-01..n`, Kebutuhan Antarmuka Eksternal, Atribut Kualitas `NFR-01..n`), kriteria kualitas SRS (*complete, consistent, unambiguous, verifiable, traceable*), serta penyusunan *Requirements Traceability Matrix* (RTM) awal. | Menulis butir-butir SRS modul masing-masing pada templat standar, lalu melakukan *peer-audit* silang antar-rekan untuk mencoret kata-kata terlarang yang tak teruji (*"cukup cepat", "user-friendly", "fleksibel"* tanpa angka). | 110' | `[1]` Bab 3; `[5]` |
| **Penutup** | Merilis instruksi resmi **Tugas 1 (RTM-1)** yang wajib dikumpulkan dan diverifikasi pada Pekan 4. | Mencatat rubrik penilaian Tugas 1 dan membagi tanggung jawab sub-modul individu. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Menyelesaikan penyusunan dokumen SRS IEEE 830 lengkap untuk pengumpulan **Tugas 1**.

---

### PERTEMUAN 4 — Pemodelan Proses Bisnis BPMN 2.0 & Verifikasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Media:** *Camunda Modeler* / *bpmn.io*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Melaksanakan kuis verifikasi tertulis 20 menit atas dokumen **Tugas 1 (SRS IEEE 830)** yang telah diunggah ke Edlink untuk menjamin keaslian karya individu. | Mengerjakan kuis verifikasi elisitasi & spesifikasi SRS secara mandiri (*closed-book*). | 25' | Instrumen T1 |
| **Kegiatan Inti** | Mengajarkan tata bahasa visual **BPMN 2.0**: perbedaan *Pool* (organisasi/entitas otonom) vs *Lane* (peran internal), *Task* (*User, Service, Manual*), *Start/Intermediate/End Event* (pesan, pewaktu), aturan percabangan & penggabungan *Gateway* (`XOR` keputusan tunggal, `AND` paralel simultan, `OR` inklusif), serta aturan emas *Sequence Flow* (dalam 1 *Pool*) vs *Message Flow* (antar-*Pool*). | Mempraktikkan pemodelan studi kasus proses pengadaan barang lintas divisi dan pemasok menggunakan *bpmn.io* / *Camunda Modeler*, sambil memeriksa bebasnya model dari jebakan *deadlock* (mis. membuka dengan `XOR` tetapi menutup dengan `AND`). | 105' | `[3]` Bab 3–4; `[4]` |
| **Penutup** | Meninjau 2 diagram BPMN mahasiswa di layar proyektor dan memberi koreksi sintaks langsung. | Menyimpan berkas `.bpmn` latihan dan menyiapkan pemodelan proses *As-Is* mitra. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Memodelkan alur proses bisnis berjalan (*As-Is*) organisasi mitra dalam standar BPMN 2.0.

---

### PERTEMUAN 5 — Analisis Efisiensi Proses Bisnis *As-Is* vs *To-Be* (*Process Redesign*)
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] · **Media:** *Camunda Modeler* / *bpmn.io*, Lembar Analisis Nilai Tambah.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan prinsip klasik rekayasa proses: *"Mengotomasi proses bisnis yang buruk hanya akan menghasilkan kekacauan yang lebih cepat."* | Mengamati contoh proses birokrasi berbelit yang gagal meskipun sudah dibuatkan aplikasi web. | 20' | `[3]` Bab 6 |
| **Kegiatan Inti** | Memaparkan teknik analisis kualitatif & kuantitatif proses bisnis: klasifikasi aktivitas *Value-Adding* (VA), *Business Value-Adding* (BVA), dan *Non-Value-Adding / Waste* (NVA), identifikasi *bottleneck* persetujuan sekuensial, heuristik perancangan ulang (*task elimination, parallelism, triage, automation*), serta cara menurunkan setiap *User Task* & *Service Task* pada BPMN *To-Be* menjadi kandidat fitur sistem. | Menganalisis diagram BPMN *As-Is* mitra, menandai langkah NVA/*bottleneck*, merancang ulang diagram **BPMN *To-Be*** yang lebih ramping, dan menyusun tabel komparasi efisiensi (*jumlah langkah, aktor terlibat, & estimasi waktu layanan sebelum vs sesudah*). | 110' | `[3]` Bab 6–8 |
| **Penutup** | Menegaskan *boundary*: eksekusi *workflow engine Camunda* secara teknis akan dipelajari mendalam bagi peminat jalur P3 pada `STC-601`. | Mengunggah pasangan diagram BPMN *As-Is* & *To-Be* formatif ke LMS Edlink. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Menyempurnakan tabel analisis kesenjangan (*gap analysis*) *As-Is* ke *To-Be* dan membaca Dennis Bab 4 tentang *Use Case*.

---

### PERTEMUAN 6 — Pemodelan Fungsional UML 2.5: *Use Case Diagram* & Spesifikasi Skenario Naratif
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Media:** *StarUML* / *PlantUML* / *draw.io*, Templat *Use Case Specification*.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan bagaimana setiap aktivitas bertanda *User/Service Task* pada BPMN *To-Be* Pekan 5 bertransformasi langsung menjadi butir *Use Case* di dalam batas sistem (*System Boundary*). | Menelusuri korespondensi 1-ke-1 antara langkah BPMN *To-Be* dan daftar *Use Case*. | 20' | `[1]` Bab 4 |
| **Kegiatan Inti** | Menjelaskan elemen *Use Case Diagram* UML 2.5 (*Primary/Secondary Actor, System Boundary, Use Case, Generalization*), membedah miskonsepsi paling sering terjadi pada `<<include>>` (sub-fungsi wajib yang selalu dipanggil, panah putus-putus menuju yang di-*include*) vs `<<extend>>` (perilaku opsional bersyarat, panah putus-putus **menuju use case dasar**!), serta struktur *Fully Dressed Use Case Description* (*Precondition, Trigger, Normal Flow, Alternative/Exception Flows, Postcondition*). | Menggambar *Use Case Diagram* utuh sistem studi kasus dan menyusun minimal 3 tabel spesifikasi skenario *fully dressed* yang memuat penanganan alur gagal/pengecualian (*exception flow*). | 110' | `[1]` Bab 4; `[6]` Bab 6 |
| **Penutup** | Mengadakan kuis kilat 5 kasus penentuan arah panah `<<include>>` vs `<<extend>>`. | Memperbaiki kesalahan arah panah relasi pada draf *Use Case Diagram* masing-masing. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Melengkapi spesifikasi naratif seluruh *Use Case* inti modul masing-masing.

---

### PERTEMUAN 7 — *Activity Diagram* UML 2.5 & Klinik Konsolidasi Pra-UTS
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Media:** *StarUML* / *PlantUML*, Paket Simulasi Kasus UTS.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Membandingkan peran BPMN 2.0 (memodelkan alur proses bisnis lintas organisasi/unit) dengan *Activity Diagram* UML 2.5 (memodelkan alur logika internal satu *Use Case* antara pengguna dan sistem). | Membedakan level abstraksi BPMN vs *Activity Diagram* agar tidak menggambar dua diagram yang identik. | 20' | `[1]` Bab 5 |
| **Kegiatan Inti** | Menguraikan notasi *Activity Diagram* UML 2.5 (*Initial/Activity Final Node, Flow Final, Swimlane Actor vs System, Decision & Merge Diamond, Fork & Join Bar, Object Node*), dilanjutkan latihan simulasi studi kasus terpadu persiapan **UTS Pekan 8** (pemodelan BPMN 2.0 *As-Is*, analisis inefisiensi, BPMN *To-Be*, dan ekstraksi layanan sistem). | Mengerjakan pembuatan *Activity Diagram* untuk 2 *Use Case* kompleks dan berlatih menyelesaikan studi kasus simulasi UTS dalam batas waktu terukur. | 110' | `[1]` Bab 5; `[4]` |
| **Penutup** | Menyampaikan kisi-kisi, aturan pelaksanaan, dan kriteria rubrik penilaian **UTS (`CPMK-2`, 30%)**. | Mencatat hal-hal kritis sintaks BPMN 2.0 yang wajib dipatuhi saat UTS. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Belajar mandiri persiapan UTS atas materi Pekan 4–7.

---

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]) · **Bobot:** **30%** · **Durasi:** `150 menit` (Tertulis Luring Terjadwal).

| Tahap | Aktivitas Pengawasan & Pelaksanaan | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan kartu ujian, pembagian lembar studi kasus & kertas gambar berpetak/polos, serta pembacaan tata tertib. | Menyiapkan alat tulis/penggaris dan mengisi identitas pada lembar jawab. | 10' | Tata Tertib UTS |
| **Pelaksanaan** | Mengawasi pengerjaan 3 bagian soal studi kasus terpadu: (1) Pemodelan BPMN 2.0 *As-Is* yang valid secara sintaks; (2) Analisis 4 titik inefisiensi & perancangan ulang BPMN 2.0 *To-Be* beserta metrik penghematan tahap; (3) Pemetaan aktivitas *To-Be* ke daftar fungsional sistem. | Menganalisis kasus dan menggambar solusi model proses bisnis secara mandiri dan rapi. | 135' | Naskah Soal UTS `STI-306` |
| **Pengumpulan** | Mengumpulkan lembar jawaban dan menandatangani berita acara pelaksanaan UTS. | Menyerahkan berkas ujian secara tertib. | 5' | Berita Acara |
* **PT & BM:** Evaluasi mandiri pasca-UTS dan membaca Dennis Bab 6 (*Structural Modeling / Class Diagram*).

---

### PERTEMUAN 9 — Pemodelan Struktural Statis UML 2.5: *Domain & Design Class Diagram*
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] · **Media:** *StarUML* / *PlantUML*, Umpan Balik Hasil UTS.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Membahas umpan balik umum hasil UTS, lalu memperkenalkan peralihan dari pemodelan perilaku (*behavior*) menuju pemodelan struktur objek (*Class Diagram*) yang melampaui ERD dasar di `FST-207` karena memuat perilaku/operasi metode! | Menyimak perbedaan mendasar antara ERD (hanya data statis) dengan *Class Diagram* (atribut + operasi + enkapsulasi). | 20' | `[1]` Bab 6 |
| **Kegiatan Inti** | Menjelaskan teknik identifikasi kelas (analisis kata benda pada skenario *Use Case* & stereotip arsitektur *Boundary–Control–Entity*), penulisan *visibility* (`+ public`, `- private`, `# protected`), tipe parameter/kembalian operasi, *Multiplicity* (`1`, `0..1`, `1..*`, `*`), serta perbedaan konseptual tajam antara **Association**, **Aggregation** (belah ketupat kosong — bagian tetap hidup walau induk dihapus), **Composition** (belah ketupat hitam — siklus hidup bagian terikat mutlak pada induk, mis. `Invoice` dan `InvoiceLineItem`), dan **Generalization/Inheritance**. | Mengekstrak kelas-kelas dari skenario *Use Case* sistem proyek, menentukan atribut beserta metode operasinya, dan menyusun *Class Diagram* lengkap dengan ketepatan kardinalitas dan komposisi. | 110' | `[1]` Bab 6; `[6]` Bab 9 & 16 |
| **Penutup** | Membedah 3 contoh salah kaprah antara *Aggregation* vs *Composition*. | Memvalidasi ketepatan jenis garis relasi pada draf *Class Diagram* kelompok. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Merampungkan *Design Class Diagram* sistem studi kasus (minimal 8–12 kelas saling berelasi).

---

### PERTEMUAN 10 — Pemodelan Interaksi Objek Dinamis UML 2.5: *Sequence Diagram*
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] · **Media:** *PlantUML* / *StarUML*, Ceklis Konsistensi Kelas–Sekuens.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan bagaimana sebaris interaksi pengguna di layar memicu rangkaian panggilan pesan berurutan antar-objek (*Boundary → Controller → Entity*) sepanjang sumbu waktu vertikal. | Mengamati urutan aliran pesan pada contoh transaksi pembayaran pesanan. | 20' | `[1]` Bab 7 |
| **Kegiatan Inti** | Menguraikan komponen **Sequence Diagram** UML 2.5 (*Actor, Object Lifeline, Execution/Activation Bar, Synchronous Call, Asynchronous Message, Reply/Return Dashed Arrow, Self-Call*), penggunaan *Combined Fragments* (`alt/else` untuk percabangan kondisi, `opt` untuk opsional, `loop` untuk perulangan item keranjang), serta **Hukum Besi Konsistensi UML**: *setiap pesan `namaMetode()` yang diterima oleh suatu Lifeline Kelas X WAJIB tercatat sebagai operasi pada Kelas X di Class Diagram!* | Menyusun *Sequence Diagram* untuk 3 *Use Case* inti proyek, lalu melakukan audit silang (*cross-check*) dengan *Class Diagram* Pekan 9 untuk memperbarui operasi kelas yang belum tertulis. | 110' | `[1]` Bab 7; `[6]` Bab 15 |
| **Penutup** | Merilis instruksi resmi **Tugas 2 (RTM-2)** (dikumpulkan Pekan 12). | Mencatat spesifikasi paket pemodelan UML 2.5 yang diwajibkan pada Tugas 2. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Menyusun minimal 3 *Sequence Diagram* lengkap per modul dan menyelaraskannya dengan *Class Diagram*.

---

### PERTEMUAN 11 — Pemodelan Siklus Status Objek Kompleks: *State Machine Diagram*
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] · **Media:** *PlantUML* / *StarUML*, Studi Kasus Status Transaksi.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengajukan pertanyaan kritis: *"Bolehkah pesanan berstatus `Dibatalkan` tiba-tiba berubah menjadi `Dikirim`?"* — memperkenalkan perlunya memodelkan aturan transisi status sah suatu objek. | Mengidentifikasi objek-objek di dalam sistem mitra yang memiliki daur hidup status ketat. | 20' | `[1]` Bab 7 |
| **Kegiatan Inti** | Menjelaskan notasi **State Machine Diagram** UML 2.5 (*Initial Pseudostate, Simple & Composite State, Final State, Transition Arrow* berformat `event [guard] / action`, aktivitas internal `entry/`, `do/`, `exit/`), perbedaannya dengan *Activity Diagram* (berpusat pada status 1 objek vs alur kerja lintas aktor), serta klinik pengecekan konsistensi 5 diagram UML jelang pengumpulan **Tugas 2**. | Merancang *State Machine Diagram* untuk objek utama sistem (mis. `Pesanan`, `TiketPengaduan`, `PengajuanCuti`, `RekamKunjungan`) dan memverifikasi keutuhan paket UML Tugas 2. | 110' | `[1]` Bab 7; `[4]` |
| **Penutup** | Mengingatkan tenggat unggah **Tugas 2 (`CPMK-3`, 20%)** sebelum sesi Pekan 12 dimulai. | Melakukan pengecekan akhir kelengkapan dan konsistensi berkas Tugas 2. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Finalisasi dan pengunggahan paket pemodelan UML 2.5 untuk **Tugas 2**.

---

### PERTEMUAN 12 — Arsitektur Sistem (*Package & Deployment Diagram*) & Verifikasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-4.1` [C4→C5] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 20%)** · **Media:** Templat SDD IEEE 1016, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Melaksanakan verifikasi singkat tertulis/lisan 20 menit atas paket UML **Tugas 2** (menguji pemahaman konsistensi antara *Use Case, Class, Sequence,* dan *State Machine*). | Menjawab pertanyaan konfirmasi atas diagram UML yang telah dibuatnya sendiri. | 25' | Instrumen T2 |
| **Kegiatan Inti** | Memperkenalkan struktur dokumen **Software Design Document (SDD — IEEE 1016)** sebagai artefak puncak mata kuliah, lalu mengajarkan pemodelan arsitektur tingkat tinggi: **Package Diagram** (pengelompokan kelas ke lapisan *Presentation, Application/Service, Domain, Data Access* beserta aturan arah ketergantungan `<<import>>`) dan **Deployment Diagram** (node server web, server aplikasi, server basis data, perangkat klien, protokol komunikasi `HTTPS`, `TCP/IP`, `REST/JSON`). | Menyusun *Package Diagram* dan *Deployment Diagram* untuk sistem studi kasus tim, serta mulai mengisi Bab 1–3 pada templat dokumen SDD proyek akhir. | 105' | `[1]` Bab 8–9; `[5]` |
| **Penutup** | Menjelaskan jadwal tonggak pengerjaan SDD menuju sidang **UAS Pekan 16**. | Membagi bagian tanggung jawab penyusunan SDD di dalam tim. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Menyusun Bab Arsitektur Perangkat Lunak & Lingkungan *Deployment* pada draf SDD.

---

### PERTEMUAN 13 — *Dialog Navigation Diagram* & Penyelarasan Desain terhadap Kebutuhan Bisnis
* **Sub-CPMK:** `Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5] · **Media:** Peta Navigasi Layar, Matriks NFR-ke-Arsitektur.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menegaskan perbedaan antara desain estetika/interaksi mikro UI/UX (`STI-308`) dengan spesifikasi struktur navigasi dialog & kontrol akses peran pengguna di dalam dokumen SDD (`STI-306`). | Memahami cara merujuk purwarupa antarmuka tanpa menduplikasi pekerjaan mata kuliah `STI-308`. | 20' | `[1]` Bab 10 |
| **Kegiatan Inti** | Mengajarkan penyusunan **Windows/Dialog Navigation Diagram** (peta transisi antar-layar menurut hak akses *Actor*), spesifikasi validasi masukan/keluaran formulir kritis, serta evaluasi keselarasan keputusan desain terhadap kebutuhan bisnis & NFR (mis. mekanisme *audit trail*, otorisasi berbasis peran *RBAC*, pencadangan data, dan batasan waktu tanggap). | Menyusun *Dialog Navigation Diagram* per aktor dan membuat matriks keputusan desain terhadap NFR bisnis di dalam draf SDD tim, dilanjutkan *walkthrough* umpan balik antar-kelompok. | 110' | `[1]` Bab 10; `[2]` Bab 8 |
| **Penutup** | Menyimpulkan hasil *walkthrough* dan memberi arahan persiapan spesifikasi data & kontrak API pekan depan. | Mencatat perbaikan navigasi dan kontrol otorisasi pada SDD. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Merampungkan Bab Desain Antarmuka Navigasi & Kontrol Keamanan Fungsional pada SDD.

---

### PERTEMUAN 14 — Pemetaan *Class-to-Relational Schema* & Spesifikasi Kontrak REST API dalam SDD
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5] · **Media:** Templat Kamus Data & Tabel Spesifikasi REST API.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan apa yang paling dibutuhkan oleh programmer *front-end* (`STI-311`) dan *back-end* (`STI-416`) saat menerima SDD: skema tabel yang presisi dan kontrak endpoint API yang tidak multitafsir! | Menyadari fungsi SDD sebagai jembatan langsung menuju mata kuliah rekayasa kode. | 20' | `[1]` Bab 11 |
| **Kegiatan Inti** | Menguraikan aturan pemetaan **Object-to-Relational Mapping** dari *Class Diagram* ke skema tabel relasional 3NF (pemetaan relasi `1:N`, tabel penghubung asosiasi `M:N`, serta 3 strategi pemetaan pewarisan: *Single Table, Class Table,* atau *Concrete Table Inheritance*), dilanjutkan cara menulis **Spesifikasi Kontrak Antarmuka Layanan / REST API** di SDD (*Endpoint URI, HTTP Verb, Auth Role, Request JSON Schema, Success/Error Response Payload & HTTP Status Codes*) — **tanpa menulis kode program server**. | Memetakan *Class Diagram* proyek menjadi skema relasional & kamus data lengkap, serta menyusun minimal 8 spesifikasi kontrak endpoint REST API utama di dalam dokumen SDD. | 110' | `[1]` Bab 11; `[5]` |
| **Penutup** | Memeriksa sampel kontrak API mahasiswa agar konsisten dengan nama atribut pada *Class Diagram* dan tabel basis data. | Menyelaraskan penamaan kolom tabel, atribut kelas, dan *field* JSON kontrak API. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Menyelesaikan Bab Desain Data & Spesifikasi Antarmuka Modul/API pada SDD.

---

### PERTEMUAN 15 — Audit *End-to-End Traceability* & Simulasi Sidang Dokumen SDD
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Media:** Ceklis Audit IEEE 1016, Draf Penuh SDD Kelompok.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Memperkenalkan konsep **End-to-End Traceability Matrix**: setiap satu baris `FR-xx` pada SRS wajib memiliki jejak utuh ke aktivitas BPMN *To-Be* → `UC-xx` → Kelas/Sekuens → Tabel DB & Endpoint API pada SDD. | Membuka matriks keterlacakan draf SDD masing-masing untuk diaudit. | 20' | `[5]` |
| **Kegiatan Inti** | Memfasilitasi sesi **Mock Design Review & Coaching Clinic**: setiap kelompok memaparkan ringkasan arsitektur SDD selama 10 menit, sementara dosen dan tim penelaah menguji adanya celah konsistensi (*orphan requirement*, metode tak bertuan, tabel tanpa kelas, atau fitur di luar ruang lingkup). | Mempresentasikan draf SDD, menerima kritik tajam layaknya rapat *Architecture Review Board* industri, dan mencatat daftar revisi wajib sebelum UAS. | 110' | `[1]` Bab 12; `[5]` |
| **Penutup** | Menjelaskan mekanisme penilaian **UAS Pekan 16 (`CPMK-4`, 30%)** yang menggabungkan kualitas naskah SDD (60%) dan tanya-jawab individu (40%). | Mengunggah draf pra-sidang dan memfinalisasi pembagian penguasaan seluruh bab SDD oleh tiap anggota. | 20' | LMS Edlink |
* **PT (`180'`) & BM (`180'`):** Penyempurnaan akhir naskah **Software Design Document (SDD)** versi final siap sidang.

---

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS): SIDANG DOKUMEN SDD
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) · **Bobot:** **30%** · **Durasi:** `150 menit`.

| Tahap | Aktivitas Dosen / Penguji | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Pembukaan** | Memverifikasi kelengkapan unggahan berkas final `SRS + SDD` seluruh tim di LMS Edlink dan mengatur urutan giliran sidang. | Menyiapkan tayangan ringkas arsitektur & dokumen SDD lengkap untuk dibuka saat sesi tanya-jawab. | 10' | Berita Acara UAS |
| **Sidang & Pertahanan Kritis** | Menilai presentasi cetak biru SDD tiap tim dan mengajukan pertanyaan uji silang **secara langsung kepada setiap individu anggota** (mis. meminta Anggota A menelusuri jejak `FR-04` dari BPMN hingga kontrak JSON API dan skema tabelnya) guna memastikan akuntabilitas kompetensi individu. | Mempresentasikan rancangan arsitektur SDD secara profesional dan mempertanggungjawabkan keputusan desain, konsistensi model, serta kesiapan *handoff* ke tahap konstruksi perangkat lunak. | 130' | Rubrik Analitik UAS `STI-306` |
| **Penutupan** | Menyampaikan rangkuman evaluasi akhir semester dan menutup perkuliahan. | Menandatangani daftar hadir UAS dan mengarsipkan portofolio final di LMS Edlink. | 10' | Portal OBE |
