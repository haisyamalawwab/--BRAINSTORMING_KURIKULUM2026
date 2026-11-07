# 062_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN STUDIO & TEORI
## STI-308 — DESAIN & PROTOTYPING UI/UX (*UI/UX Design & Prototyping*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI308` · **Bobot:** 3 SKS `+P` (`100' Teori + 170' Studio Lab = 270'`, `PT 120'`, `BM 120'`) · **Semester:** 3  
**Prasyarat:** `FST-101` Dasar Teknologi Digital · **CPL:** `CPL-13` (`KK5` = 100%) [Level `R`] · **Klaster Rubrik:** `K-2`  
**Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP STUDIO `3 SKS +P` & PAGAR PEMBATAS KELAS

| Atribut Pelaksanaan | Ketentuan Baku Studio `STI-308` |
|---|---|
| **Format Sesi Mingguan (`270'`)** | **Sesi Teori & Bedah Kasus (`100'`):** Pengantar konsep, bedah pola antarmuka nyata, & demonstrasi prinsip.<br>**Sesi Praktikum Studio Lab (`170'`):** Praktik langsung terbimbing di **FigJam / Figma**, *peer critique*, dan pemeriksaan progres artefak. |
| **Fokus Keilmuan (*In-Scope*)** | *Design Thinking*, riset pengguna dasar (*Persona, Journey Map*), *Information Architecture*, *Wireframe*, prinsip visual (*Gestalt, warna, tipografi, 8pt Grid*), *Design System & Interactive Prototype* Figma berstandar **WCAG 2.1 AA**, serta uji **SUS** & **10 Heuristik Nielsen**. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ Dilarang menugaskan koding *HTML/CSS/JS/React* (ranah **`STI-311 Pengembangan Web Front End`**); dilarang membebani mahasiswa dengan eksperimen statistik *multivariate A/B Testing* atau etnografi panjang (ranah **`STC-501 Riset & Desain Pengalaman Pengguna (UX)`**). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Teori (`100'`) & Praktikum Studio (`170'`) | Metode Utama | Waktu | Evaluasi |
|:---:|:---:|---|---|:---:|---|
| **1** | `Sub-CPMK-1.1, 1.2` | Prinsip HCI (Norman), UI vs UX, 5 Tahap *Design Thinking*, & *Setup* FigJam | Kuliah + Lab FigJam | 270' | Formatif |
| **2** | `Sub-CPMK-1.1, 1.2` | Wawancara Kontekstual, *Affinity Diagram*, *User Persona*, & *Journey Map* | *Case Method* + Sintesis Lab | 270' | Formatif |
| **3** | `Sub-CPMK-2.1` | *Information Architecture*, Praktik *Card Sorting*, *Sitemap*, & *User Flow* | Kuliah + *Workshop* IA | 270' | Formatif |
| **4** | `Sub-CPMK-2.2` | Ideasi *Crazy 8s*, *Low-Fidelity Wireframing*, & Evaluasi **Tugas 1** | Verifikasi T1 + Lab *Wireframe* | 270' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1, 2.2` | Psikologi Gestalt, Hukum UX, Skala Tipografi, Warna, & Sistem Kisi *8pt Grid* | Kuliah + Lab *UI Refactoring* | 270' | Formatif |
| **6** | `Sub-CPMK-3.1` | *Figma Masterclass*: *Frames, Constraints,* & *Nested Auto-Layout* Responsif | *Hands-on Studio Workshop* | 270' | Formatif |
| **7** | `Sub-CPMK-2.2, 3.1` | *Atomic Design*, *Figma Components & Variants*, & Klinik Persiapan UTS | Studio Lab & *Design Critique* | 270' | Formatif |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** Ujian Praktik *Flow/Wireframe* & Validasi Proyek | Ujian Praktik Studio Figma | 170' | **UTS (25%)** |
| **9** | `Sub-CPMK-3.1` | Arsitektur **Design System** & *Figma Variables / Design Tokens* | Kuliah + PjBL Studio Lab | 270' | Formatif |
| **10** | `Sub-CPMK-3.1` | *High-Fidelity Interactive Prototyping*, *Overlays*, & *Smart Animate* | Kuliah + Lab *Prototyping* | 270' | Formatif |
| **11** | `Sub-CPMK-3.2` | Aksesibilitas Digital **WCAG 2.1 Level AA**: Kontras, *Touch Target*, & *Focus State* | Kuliah + Audit Plugin WCAG | 270' | Formatif |
| **12** | `Sub-CPMK-4.1` | Inspeksi Studio **Tugas 2** & Penyusunan *Usability Testing Plan / Scenarios* | Inspeksi T2 + Lab *Test Plan* | 270' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-4.1` | Eksekusi Sesi *Moderated Usability Testing* & Perhitungan Skor **SUS** | Kuliah + Sesi Uji Pengguna | 270' | Formatif |
| **14** | `Sub-CPMK-4.2` | Audit **10 Heuristik Usability Nielsen**, *Severity Rating*, & Iterasi v2.0 | *Peer Heuristic Audit* + Lab | 270' | Formatif |
| **15** | `Sub-CPMK-4.2` | Spesifikasi *Developer Handoff* (ke `STI-311`) & *UI/UX Case Study Portfolio* | Studio PjBL & *Rehearsal* | 270' | Formatif |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** *Demo Day* Purwarupa Final, Laporan SUS, & Sidang | Pameran & Pertahanan Individu | 170' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Prinsip Dasar HCI, UI vs UX, & 5 Tahap *Design Thinking*
* **Sub-CPMK:** `Sub-CPMK-1.1` & `1.2` [C2→C4] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Memaparkan kontrak studio, membedah konsep *Norman Doors* (*Affordance, Signifier, Mapping, Feedback, Conceptual Model*), membedakan cakupan UI vs UX, serta menguraikan alur non-linier 5 tahap **Design Thinking**. | Menganalisis 3 contoh antarmuka aplikasi sehari-hari di Indonesia yang membingungkan pengguna akibat buruknya *signifier* dan *feedback*. | 100' | `[1]` Bab 1–2; `[2]` Bab 1 |
| **Praktikum Studio** | Memandu aktivasi lisensi akademik *Figma Education*, pengenalan ruang kerja **FigJam**, pembentukan tim studio (3 orang), dan lokakarya pemilihan masalah layanan digital nyata (layanan kampus, UMKM lokal, kesehatan, atau mobilitas publik). | Menyiapkan berkas kolaborasi FigJam tim, memetakan asumsi masalah awal, dan menentukan segmen calon pengguna nyata yang akan diwawancarai pekan ini. | 170' | FigJam, LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyusun draf 10 pertanyaan wawancara kontekstual terbuka (bebas pertanyaan mengarahkan/*leading questions*).

---

### PERTEMUAN 2 — Riset Pengguna Kontekstual, *Persona*, & *Customer Journey Map*
* **Sub-CPMK:** `Sub-CPMK-1.1` & `1.2` [C4] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Mengajarkan etika dan teknik wawancara pengguna (*5 Whys*, observasi perilaku nyata vs opini), cara mengklaster temuan lapangan dengan *Affinity Diagram*, penyusunan *User Persona* berbasis data (bukan karangan fiktif!), *Customer Journey Map*, serta perumusan kalimat *Point-of-View* (POV) dan *How Might We* (HMW). | Mengkritisi contoh *fake persona* yang hanya berisi biodata demografis tanpa tujuan, perilaku, dan *frustrations* nyata. | 100' | `[1]` Bab 8 & 11 |
| **Praktikum Studio** | Membimbing tim mengelompokkan catatan hasil wawancara awal di FigJam menjadi klaster tema menggunakan *sticky notes*, lalu merakit papan *Empathy Map*, *User Persona*, dan *Customer Journey Map*. | Menyintesis data lapangan di FigJam, merumuskan 3 pernyataan HMW prioritas, dan mempresentasikannya selama 5 menit untuk *studio critique*. | 170' | FigJam, Rekaman Wawancara |
* **PT (`120'`) & BM (`120'`):** Melengkapi wawancara hingga minimal 5 responden sasaran dan memoles kanvas riset pengguna.

---

### PERTEMUAN 3 — *Information Architecture*, *Card Sorting*, *Sitemap*, & *User Flow*
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Menjelaskan konsep *Mental Model* pengguna vs struktur sistem, prinsip *Information Architecture* (IA), metode *Open & Closed Card Sorting*, penyusunan hierarki *Sitemap*, serta cara menggambar **User Flow** lengkap dengan titik keputusan dan kondisi gagal. | Mengamati bagaimana struktur menu yang mengikuti struktur divisi internal perusahaan sering membingungkan pengguna luar. | 100' | `[3]` Bab 2–6; `[4]` Bab 2 |
| **Praktikum Studio** | Memfasilitasi praktik *Card Sorting* silang antar-kelompok (kelompok A menguji 25 kartu fitur kepada anggota kelompok B sebagai responden), dilanjutkan pembuatan *Sitemap* dan 3 *User Flow* utama di FigJam. Merilis instruksi resmi **Tugas 1 (RTM-1)**. | Menjalankan uji *Card Sorting*, merancang *Sitemap* aplikasi, dan menggambar *User Flow* end-to-end bebas jalan buntu. | 170' | Kartu Fitur, FigJam |
* **PT (`120'`) & BM (`120'`):** Finalisasi laporan & kanvas **Tugas 1 (*User Research & Design Thinking Brief*)** untuk Pekan 4.

---

### PERTEMUAN 4 — Verifikasi Tugas 1, Ideasi *Crazy 8s*, & *Low-Fidelity Wireframing*
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alokasi:** `100' Evaluasi/Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Evaluasi Tugas 1 & Teori** | Menilai presentasi kilat & tanya-jawab verifikasi individu atas **Tugas 1 (`CPMK-1`)**, lalu memaparkan kaidah **Low-Fidelity Wireframing** (fokus pada tata letak, prioritas konten, dan kejelasan alur — dilarang memakai warna dekoratif dan foto penuh di tahap ini!). | Mempertanggungjawabkan hasil riset pengguna masing-masing, lalu melakukan pemanasan sketsa cepat *Crazy 8s* di kertas selama 8 menit. | 100' | Instrumen T1; `[3]` Bab 7 |
| **Praktikum Studio** | Membimbing penerjemahan sketsa terpilih dan *User Flow* Pekan 3 menjadi 10–12 layar **Low-Fidelity Wireframe** skala abu-abu (*grayscale*) di kanvas Figma. | Membangun kerangka *Low-Fi Wireframe* untuk 3 alur tugas utama dengan label tombol dan struktur informasi yang jelas. | 170' | Kertas Sketsa, Figma |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan seluruh layar *Low-Fi Wireframe* termasuk layar kosong (*empty state*) dan konfirmasi.

---

### PERTEMUAN 5 — Psikologi Gestalt, Hukum UX, Tipografi, Warna, & *8pt Grid System*
* **Sub-CPMK:** `Sub-CPMK-2.1` & `2.2` [C3→C4] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Menguraikan prinsip persepsi visual **Gestalt** (*Proximity, Similarity, Common Region, Figure-Ground*), 4 Hukum UX utama (*Fitts's Law, Hick's Law, Jakob's Law, Miller's Law*), anatomi skala tipografi (`12/14/16/20/24/32px`), aturan warna **60–30–10** + warna semantik status, serta disiplin **8-Point Spatial Grid System**. | Mendiagnosis kesalahan spasi, ukuran tombol terlalu kecil di sudut sulit dijangkau ibu jari, dan hierarki teks yang datar pada contoh layar buruk. | 100' | `[1]` Bab 4; `[4]` Bab 4; `[7]` |
| **Praktikum Studio** | Memandu latihan *Visual UI Refactoring*: mengambil 2 layar *wireframe* lalu menata ulang *layout grid* kolom (`4-col mobile` / `12-col desktop`), ritme jarak kelipatan `8px` (`8, 16, 24, 32, 48px`), dan hierarki tipografi di Figma. | Menerapkan *Layout Grid* dan aturan spasi *8pt* secara presisi pada kerangka layar proyek masing-masing. | 170' | Figma |
* **PT (`120'`) & BM (`120'`):** Merapikan seluruh *wireframe* proyek agar patuh terhadap *8pt Grid* dan hukum Gestalt.

---

### PERTEMUAN 6 — *Figma Masterclass*: *Frames, Constraints,* & *Nested Auto-Layout*
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4→C6] · **Alokasi:** `100' Demo Konsep + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Demo** | Menjelaskan model kotak modern pada desain antarmuka (yang kelak berkorespondensi langsung dengan *CSS Flexbox* di `STI-311`!): cara kerja *Frames*, *Constraints*, arah **Auto-Layout** vertikal/horizontal/*wrap*, pengaturan *Resizing* (`Hug Contents, Fill Container, Fixed`), serta *Absolute Positioning* terbatas untuk lencana notifikasi. | Mengamati bagaimana kartu produk yang dibangun dengan *Nested Auto-Layout* otomatis menyesuaikan tinggi saat judul teks bertambah panjang. | 100' | `[7]` Dokumentasi Figma |
| **Praktikum Studio** | Memandu pengerjaan 6 tantangan latihan (*Auto-Layout Drills*: tombol responsif, bilah navigasi, kartu produk, daftar obrolan, formulir input, dan header dashboard), lalu menguji *live frame stretching* pada karya mahasiswa. | Membangun ulang komponen layar utama proyek menggunakan *Nested Auto-Layout* murni tanpa *Group* acak. | 170' | Berkas `.fig` Latihan |
* **PT (`120'`) & BM (`120'`):** Mengonversi minimal 8 layar proyek ke struktur *Auto-Layout* rapi.

---

### PERTEMUAN 7 — *Atomic Design*, *Components & Variants*, serta Klinik Pra-UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` & `3.1` [C4] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Memperkenalkan metodologi **Atomic Design** (*Atoms → Molecules → Organisms → Templates → Pages*) dan fitur **Figma Components, Component Properties, & Variants** untuk mengelola status elemen (`Default, Hover, Pressed, Focused, Disabled, Error`). | Memahami efisiensi merawat satu *Master Button Component* dibanding ratusan duplikat manual. | 100' | `[4]`; `[7]` |
| **Praktikum Studio** | Membimbing pembuatan set komponen dasar ber-varian, dilanjutkan **Klinik Pra-UTS**: mengaudit kesiapan *Sitemap*, *User Flow*, dan *Structured Wireframe* setiap tim serta simulasi latihan soal praktik cepat persiapan UTS Pekan 8. | Menyusun komponen dasar dan memfinalisasi paket *IA + User Flow + Wireframe* proyek untuk penilaian tengah semester. | 170' | Figma |
* **PT (`120'`) & BM (`120'`):** Persiapan menghadapi ujian praktik studio UTS Pekan 8.

---

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]) · **Bobot:** **25%** · **Durasi:** `170 menit` (Studio Lab Terjadwal).

| Tahap | Aktivitas Dosen / Penguji | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Bagian 1: Ujian Praktik Individu** | Membagikan 1 brief masalah aplikasi baru (1 halaman) dan mengawasi setiap mahasiswa secara individu di Figma merancang *User Flow* + 4 layar *Structured Wireframe* ber-*8pt Grid* & *Auto-Layout* (termasuk 1 *error/empty state*). | Mengerjakan tantangan perancangan *User Flow* dan *Wireframe* secara mandiri di kanvas ujian masing-masing. | 115' | Soal Praktik UTS `STI-308` |
| **Bagian 2: Validasi Proyek** | Memeriksa dan memvalidasi paket lengkap *Information Architecture, User Flow,* dan *Wireframe* proyek tim beserta kontribusi individu tiap anggota. | Menunjukkan jejak *layer/version history* dan menjelaskan alur arsitektur informasi proyeknya. | 55' | Rubrik Analitik UTS |
* **PT & BM:** Evaluasi umpan balik UTS dan persiapan penyusunan *Design System* warna/tipografi.

---

### PERTEMUAN 9 — Arsitektur **Design System** & *Figma Variables / Design Tokens*
* **Sub-CPMK:** `Sub-CPMK-3.1` [C6] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Mengajarkan struktur **Enterprise Design System**: pemisahan *Primitive Tokens* (`orange-500: #F26A21`) vs *Semantic Tokens* (`color-bg-brand-primary`), *Typography Styles*, *Elevation/Shadow*, sistem ikon konsisten, serta pengelolaan multi-mode (*Light/Dark Mode*) memakai *Figma Variables*. | Menganalisis halaman fondasi *Google Material 3* dan *Shopify Polaris* di Figma Community. | 100' | `[7]` |
| **Praktikum Studio** | Membimbing tim membangun halaman khusus `01 — Design System & UI Kit` di dalam berkas Figma proyek yang memuat seluruh *Variables* warna/angka spasi, *Text Styles*, dan komponen ber-varian yang terdokumentasi rapi. | Membangun *Design Tokens* dan pustaka minimal 10 keluarga komponen UI siap pakai tanpa satu pun kode warna mentah (*hardcoded hex*) yang tercecer. | 170' | Figma Variables |
* **PT (`120'`) & BM (`120'`):** Melengkapi komponen *Form Input, Card, Modal, Toast, Navigation Bar,* dan *Badge* pada *Design System* tim.

---

### PERTEMUAN 10 — *High-Fidelity Interactive Prototyping* & *Micro-interactions*
* **Sub-CPMK:** `Sub-CPMK-3.1` [C6] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Menjelaskan prinsip *High-Fidelity Visual Polish*, penggunaan *Micro-interactions* yang fungsional (umpan balik status tombol, *skeleton loading*, transisi konteks *Smart Animate* berdurasi `150–300ms` — tidak berlebihan sehingga memperlambat pengguna!), serta *Component-Level Interactions*. | Membedakan animasi fungsional yang membantu orientasi pengguna vs animasi kosmetik yang mengganggu. | 100' | `[1]` Bab 12; `[7]` |
| **Praktikum Studio** | Membimbing transformasi seluruh layar *Wireframe* menjadi layar **High-Fidelity** menggunakan *Design System* Pekan 9, lalu merangkai kabel interaksi (*Prototype Flows, Overlays, Scroll Behavior, Interactive Components*) untuk 3 skenario tugas utama. Merilis resmi **Tugas 2 (RTM-2)**. | Merakit purwarupa interaktif *High-Fidelity* dan menguji coba mode *Present* di layar perangkat nyata (*Figma Mirror*). | 170' | Figma Prototyping |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan seluruh alur klik purwarupa *High-Fidelity* tanpa jalan buntu.

---

### PERTEMUAN 11 — Aksesibilitas Digital **WCAG 2.1 Level AA** & Desain Inklusif
* **Sub-CPMK:** `Sub-CPMK-3.2` [C6] · **Alokasi:** `100' Teori + 170' Studio Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Memaparkan 4 pilar **WCAG (POUR: *Perceivable, Operable, Understandable, Robust*)** dan syarat wajib **Level AA** bagi desainer UI/UX: rasio kontras teks normal $\ge \mathbf{4,5:1}$, teks besar & batas input/ikon $\ge \mathbf{3:1}$, ukuran bidang sentuh minimal `44×44 px`, larangan menyampaikan status hanya lewat warna (wajib + ikon/teks bagi penyandang buta warna *deuteranopia/protanopia*), serta kejelasan status fokus. | Menguji contoh tombol putih di atas oranye terang atau abu-abu pucat yang gagal memenuhi kontras WCAG 2.1 AA dan mempelajari cara memperbaikinya lewat *Semantic Tokens*. | 100' | `[5]` WCAG 2.1 AA |
| **Praktikum Studio** | Memandu pelaksanaan **Audit Aksesibilitas Menyeluruh** atas draf *High-Fi Prototype* menggunakan plugin pemeriksa kontras & simulator buta warna di Figma, lalu mendokumentasikan lembar kepatuhan WCAG pada halaman khusus berkas proyek. | Mengaudit seluruh layar inti, memperbaiki *token* warna/ukuran teks/bidang sentuh yang belum lulus AA, dan menyiapkan pengumpulan **Tugas 2** untuk Pekan 12. | 170' | Figma + Contrast Checker |
* **PT (`120'`) & BM (`120'`):** Finalisasi berkas Figma **Tugas 2 (`Design System + WCAG Hi-Fi Prototype`)**.

---

### PERTEMUAN 12 — Inspeksi Studio Tugas 2 & Perencanaan *Usability Testing*
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alokasi:** `120' Inspeksi Studio + 150' Kuliah/Lab`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Inspeksi Studio Tugas 2** | Menginspeksi langsung berkas Figma setiap tim & kontribusi individu (`Variables, Auto-Layout, Variants, Prototype Flows, & WCAG Audit Sheet`) serta menguji klik langsung purwarupa untuk penilaian **Tugas 2 (`CPMK-3`)**. | Mendemonstrasikan arsitektur *Design System*, fleksibilitas *Auto-Layout*, hasil audit WCAG, dan alur purwarupa bagian tanggung jawab masing-masing. | 120' | Instrumen & Rubrik T2 |
| **Kuliah & Lab Usability Plan** | Mengajarkan cara menyusun **Usability Testing Plan**: merancang skenario tugas realistis yang tidak membocorkan nama menu (*non-leading task prompts*), protokol *Think-Aloud*, pencatatan metrik tugas (*Success Rate, Time, Misclicks*), serta pengenalan instrumen baku 10 butir **System Usability Scale (SUS)**. | Menyusun dokumen *Moderator Guide*, 4 skenario tugas uji, dan formulir kuesioner SUS dwibahasa siap pakai untuk pengujian lapangan pekan depan. | 150' | `[1]` Bab 14–15; `[3]` Bab 9 |
* **PT (`120'`) & BM (`120'`):** Merekrut minimal 5 calon pengguna sasaran (di luar anggota kelas sendiri!) untuk sesi pengujian.

---

### PERTEMUAN 13 — Eksekusi *Usability Testing* & Analisis Skor Kuantitatif **SUS**
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5] · **Alokasi:** `100' Teori Rumus SUS + 170' Lab Pengujian & Analisis`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Mengajarkan prosedur fasilitasi uji pengguna yang netral (tidak membela desain sendiri saat responden bingung!), pencatatan observasi pada *Rainbow Spreadsheet*, serta rumus resmi perhitungan **System Usability Scale (SUS)** John Brooke (butir ganjil $x_i - 1$, butir genap $5 - x_i$, jumlah dikali $2,5 \to$ skala $0\text{–}100$, patokan rata-rata industri $\approx 68$, *Good* $\ge 75\text{–}80,3$). | Berlatih menghitung skor SUS pada dataset contoh 6 responden dan membedakan arti skor SUS (bukan persentase!). | 100' | `[1]` Bab 15; `[6]` |
| **Praktikum Studio** | Memantau sesi pengujian kebergunaan terbimbing (*moderated usability testing* luring/daring) dan membimbing pengolahan matriks tingkat keberhasilan tugas serta perhitungan rata-rata skor SUS proyek tim. | Melaksanakan/merampungkan pengujian pada $\ge 5$ partisipan, merekap tingkat keberhasilan tiap tugas, menghitung skor SUS akhir, dan mengidentifikasi 5 hambatan utama pengguna. | 170' | Purwarupa Figma, Lembar SUS |
* **PT (`120'`) & BM (`120'`):** Menyusun bagian laporan kuantitatif *Usability Testing* & rekaman bukti ringkas temuan pengguna.

---

### PERTEMUAN 14 — Audit **10 Heuristik Nielsen**, *Severity Rating*, & Iterasi Desain v2.0
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Alokasi:** `100' Teori + 170' Studio Audit & Redesign`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Teori & Konsep** | Membedah satu per satu **10 Usability Heuristics Jakob Nielsen** disertai contoh konkret pada aplikasi modern, skala keparahan **Severity Rating (`0 = Bukan masalah` s.d. `4 = Usability catastrophe`)**, serta cara menggabungkan temuan inspeksi ahli (Heuristik) dengan temuan uji pengguna nyata (SUS) untuk menentukan prioritas perbaikan. | Mengidentifikasi heuristik mana yang dilanggar pada 5 studi kasus tangkapan layar aplikasi nyata. | 100' | `[6]` Nielsen Norman Group |
| **Praktikum Studio** | Memfasilitasi sesi **Cross-Team Heuristic Evaluation** (setiap mahasiswa mengaudit purwarupa tim lain secara independen menggunakan lembar kerja 10 Heuristik + *Severity 0–4*), dilanjutkan pengerjaan **Iterasi Purwarupa v2.0 (*Before vs After*)** untuk menuntaskan masalah ber-keparahan `3` dan `4`. | Menyusun tabel temuan pelanggaran heuristik lengkap dengan tangkapan layar beranotasi, lalu memodifikasi desain menjadi versi `v2.0` disertai halaman sandingan *Before vs After*. | 170' | Figma, Matriks Heuristik |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan seluruh perbaikan desain pada purwarupa final `v2.0`.

---

### PERTEMUAN 15 — Spesifikasi *Developer Handoff* (ke `STI-311`) & *UI/UX Case Study Portfolio*
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5→C6] · **Alokasi:** `270' Studio PjBL & Rehearsal`.

| Segmen | Aktivitas Dosen / Instruktur | Aktivitas Mahasiswa | Durasi | Media/Rujukan |
|---|---|---|:---:|---|
| **Konsep Handoff & Portofolio** | Menjelaskan praktik industri **Design-to-Developer Handoff** (bagaimana menata anotasi spasi, perilaku responsif, status komponen, dan ekspor aset SVG/token sehingga siap dikodekan pada mata kuliah `STI-311 Pengembangan Web Front End`), serta anatomi penulisan **UI/UX Case Study Portfolio** yang memikat perekrut industri. | Memeriksa kesiapan berkas Figma proyek agar dapat dibaca mulus oleh programmer *front-end*. | 90' | `[4]`; `[7]` |
| **Studio Rehearsal** | Melaksanakan gladi bersih pameran & *coaching clinic* atas laporan akhir evaluasi kebergunaan (SUS + Heuristik) dan purwarupa `v2.0` jelang **UAS Pekan 16**. | Mempresentasikan draf studi kasus utuh, menerima masukan akhir dosen, dan memfinalisasi bundel UAS. | 180' | Figma, Draf Portofolio |
* **PT (`120'`) & BM (`120'`):** Mengunggah laporan evaluasi kebergunaan, studi kasus portofolio, dan tautan purwarupa final `v2.0` ke LMS Edlink.

---

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS): *DEMO DAY* & PERTAHANAN INDIVIDU
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) · **Bobot:** **30%** · **Durasi:** `170 menit`.

| Tahap | Aktivitas Dosen / Panel Penguji | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Pembukaan Showcase** | Memverifikasi kelengkapan unggahan berkas laporan SUS/Heuristik, studi kasus portofolio, dan tautan Figma final seluruh tim. | Menyiapkan tampilan purwarupa interaktif `v2.0` dan tayangan ringkas hasil evaluasi kebergunaan. | 10' | Berita Acara UAS |
| **Demo & Pertahanan Individu** | Menilai presentasi hasil evaluasi kebergunaan (**SUS** & **10 Heuristik Nielsen**), membedah bukti perbaikan *Before–After*, serta menguji tanya-jawab kritis kepada setiap anggota secara individu mengenai perhitungan SUS, alasan penetapan *Severity Rating*, dan keputusan desainnya. | Mendemonstrasikan purwarupa final secara langsung, memaparkan bukti kuantitatif/kualitatif pengujian, dan menjawab pertanyaan penguji secara objektif dan profesional. | 150' | Rubrik Analitik UAS `STI-308` |
| **Penutupan** | Menyampaikan apresiasi karya terbaik studio dan menutup perkuliahan semester. | Menandatangani daftar hadir UAS dan mengarsipkan tautan portofolio final pada portal OBE. | 10' | Portal OBE |
