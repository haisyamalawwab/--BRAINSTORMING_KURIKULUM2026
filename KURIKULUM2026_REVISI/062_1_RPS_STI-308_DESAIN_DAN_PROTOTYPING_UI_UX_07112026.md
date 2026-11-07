# 062_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-308 — DESAIN & PROTOTYPING UI/UX (*UI/UX Design & Prototyping*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI308`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Desain & Prototyping UI/UX / *UI/UX Design & Prototyping* |
| **Kode Mata Kuliah** | `STI-308` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Interaksi Manusia-Komputer, Desain Pengalaman Pengguna & Platform (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS Praktikum (`+P`: `T = 2, P = 1`)** — Tatap Muka Teori `2×50' = 100'`, Praktikum Studio Lab `1×170' = 170'` (Total Kontak Terjadwal `270'`), `PT = 120'`, `BM = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Desain Interaksi & Platform (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `FST-101` Dasar Teknologi Digital |
| **Mata Kuliah Hilir (*Handoff*)** | `STI-311` Pengembangan Web Front End (ko-semester/hilir implementasi kode), `STC-501` Riset & Desain Pengalaman Pengguna (UX), `STI-522` Pemrograman Aplikasi Mobile, `FST-610` Capstone Project FSTI |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-13` (`KK5` = **100%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 2 (`K-2` — Rekayasa Platform & Desain Produk Digital)** · Skema Baku `+P`: Tugas 1 `20%` · UTS `25%` · Tugas 2 `25%` · UAS `30%` |
| **Pengembang RPS** | Tim KBK Interaksi Manusia-Komputer (HCI) & Rekayasa Platform Digital |
| **Koordinator RMK** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. Ahmad Fairuzabadi, S.Kom., M.Kom. *(Koordinator MK — Bidang HCI)*<br>2. [Nama Dosen Pengampu 2 / Instruktur Studio Lab] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-13`** (`KK5`) | Keterampilan Khusus | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | **R** (*Reinforce*) | **100%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **melakukan** riset pengguna (*User Research*) melalui wawancara, observasi, dan persona (*B*) menggunakan metodologi *Design Thinking* (*C*) dengan empati mendalam (*D*). | **C4** (*Analyze*) | `CPL-13` (`KK5`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **merancang** arsitektur informasi, alur pengguna (*User Flow*), dan *Wireframe* (*B*) pada aplikasi web/mobile (*C*) secara terstruktur (*D*). | **C4** (*Analyze*) | `CPL-13` (`KK5`) | **UTS — Pekan 8 (25%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **membangun** purwarupa interaktif *High-Fidelity* dan *Design System* (*B*) menggunakan perangkat lunak Figma (*C*) dengan kepatuhan standar aksesibilitas WCAG (*D*). | **C6** (*Create*) | `CPL-13` (`KK5`) | **Tugas 2 — Pekan 12 (25%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **mengevaluasi** kegunaan antarmuka (*Usability Testing*) (*B*) menggunakan *System Usability Scale* (SUS) dan *Heuristic Evaluation* (*C*) dengan analisis kuantitatif/kualitatif (*D*). | **C5** (*Evaluate*) | `CPL-13` (`KK5`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Melakukan riset pengguna (*user research*) melalui wawancara, observasi, dan persona. | `CPMK-1` | **C4** | Mg 1–3 |
| **`Sub-CPMK-1.2`** | Menerapkan metodologi *Design Thinking* pada proses perancangan antarmuka. | `CPMK-1` | **C4** | Mg 1–4 |
| **`Sub-CPMK-2.1`** | Merancang arsitektur informasi dan alur pengguna (*user flow*) pada aplikasi web/mobile. | `CPMK-2` | **C4** | Mg 3–5 |
| **`Sub-CPMK-2.2`** | Membangun *wireframe low-fidelity* yang terstruktur berdasarkan arsitektur informasi. | `CPMK-2` | **C4** | Mg 4 & 6–7 |
| **`Sub-CPMK-3.1`** | Membangun *prototype high-fidelity* interaktif dan *design system* menggunakan Figma. | `CPMK-3` | **C6** | Mg 6–7 & 9–10 |
| **`Sub-CPMK-3.2`** | Menerapkan kepatuhan standar aksesibilitas WCAG pada desain antarmuka. | `CPMK-3` | **C6** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Mengevaluasi kegunaan antarmuka menggunakan *System Usability Scale* (SUS). | `CPMK-4` | **C5** | Mg 12–13 |
| **`Sub-CPMK-4.2`** | Mengevaluasi kegunaan antarmuka menggunakan *Heuristic Evaluation* dengan analisis kualitatif serta menyusun studi kasus portofolio. | `CPMK-4` | **C5** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Evaluasi Usability Testing (SUS) & 10 Heuristics Nielsen + Portofolio UI/UX (C5) — Mg 12–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: Skenario Uji Pengguna & Skor Kuantitatif SUS | Sub-CPMK-4.2: Audit 10 Heuristik & Iterasi Perbaikan)
      │
[CPMK-3: Design System, High-Fidelity Interactive Prototype Figma, & Aksesibilitas WCAG (C6) — Mg 9–12 (Tugas 2 25%)]
      ▲  (Sub-CPMK-3.1: Design Tokens, Auto-Layout, Variants, Smart Animate | Sub-CPMK-3.2: Audit Kontras & Fokus WCAG 2.1 AA)
      │
[CPMK-2: Arsitektur Informasi (IA), User Flow, & Low-Fidelity Wireframing (C4) — Mg 3–8 (UTS 25%)]
      ▲  (Sub-CPMK-2.1: Card Sorting, Sitemap, & Task/User Flow | Sub-CPMK-2.2: Wireframe 8pt Grid & Prinsip Gestalt)
      │
[CPMK-1: Riset Pengguna & Metodologi Design Thinking Berbasis Empati (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Wawancara Kontekstual, Empathy Map, User Persona | Sub-CPMK-1.2: Customer Journey & HMW Problem Framing)
      ▲
[Fondasi Prasyarat: FST-101 Dasar Teknologi Digital]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-13`** (`KK5`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | |
| **`CPL-13`** (`KK5`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **25%** | — | — | **25%** | **`CPL-13` = 100%** |
| **`CPL-13`** (`KK5`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **25%** | — | **25%** | |
| **`CPL-13`** (`KK5`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **25%** | **25%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 50\%$):** `Tugas 1 (20% — Case-Based User Research & Design Thinking Brief) + Tugas 2 (25% — Project Milestone Design System & WCAG Hi-Fi Prototype) + UAS (30% — Final UI/UX Showcase, SUS Usability Report & Defense)` = **75%** *(persis selaras dengan angka tabel IKU 7 Dokumen 004 untuk `STI-308` = 75%)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah studio praktikum `STI-308 Desain & Prototyping UI/UX` (3 SKS `+P`) membekali mahasiswa keterampilan merancang antarmuka dan pengalaman pengguna produk digital web/mobile yang berpusat pada manusia (*Human-Centered Design*). Melalui proyek studio berkesinambungan dari Pekan 1 hingga 16, mahasiswa menerapkan tahapan **Design Thinking** (*Empathize, Define, Ideate, Prototype, Test*), menyusun *User Persona* dan *Customer Journey Map*, menata **Information Architecture** dan *User Flow*, membangun *Low-Fidelity Wireframe*, menerapkan psikologi visual Gestalt, teori warna, tipografi, dan sistem kisi *8pt Grid*, merakit **Design System** modular (*Design Tokens, Auto-Layout, Component Variants*) serta **High-Fidelity Interactive Prototype** berstandar aksesibilitas **WCAG 2.1 Level AA** menggunakan **Figma**, hingga memvalidasi kegunaan produk melalui pengujian *System Usability Scale* (**SUS**) dan *10 Usability Heuristics* Jakob Nielsen.

* **🟢 IN-SCOPE (Wajib Diajarkan):** Prinsip dasar HCI & psikologi persepsi Gestalt, 5 tahap *Design Thinking*, wawancara pengguna dasar, *Persona & Journey Map*, *Information Architecture* (*Card Sorting, Sitemap, User Flow*), *Low-Fi Wireframing*, teori warna/tipografi/*8pt Grid*, penguasaan studio **Figma** (*Auto-Layout, Variables/Tokens, Components & Variants, Interactive Prototyping*), standar aksesibilitas **WCAG 2.1 AA**, serta evaluasi kegunaan dasar (**SUS** & **10 Heuristik Nielsen**).
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan):**
  1. Dilarang menugaskan penulisan kode program *HTML5, CSS3, JavaScript,* atau *React.js* (ranah eksklusif **`STI-311 Pengembangan Web Front End`** dan **`STI-522 Pemrograman Aplikasi Mobile`**).
  2. Dilarang mengajarkan metode riset etnografi kualitatif lanjut, *diary study*, *biometric eye-tracking*, atau analisis inferensial eksperimen *multivariate A/B Testing* skala produksi (ranah mata kuliah peminatan P3 **`STC-501 Riset & Desain Pengalaman Pengguna (UX)`**).
* **🔄 HANDOFF ANCHOR:** Menghasilkan *Design System* terdokumentasi dan purwarupa interaktif Figma tervalidasi SUS yang siap di-*handoff* (*Figma Dev Mode / Design Tokens*) untuk dikodekan pada **`STI-311 Pengembangan Web Front End`** dan **`STI-522`**, serta menjadi pijakan riset UX mendalam pada **`STC-501`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS17` (*Human-Computer Interaction & UX*) & `BK-IT10` (*User Experience & Interaction Design*).

**Pustaka Utama:**
1. Sharp, H., Preece, J., & Rogers, Y. (2023). *Interaction Design: Beyond Human-Computer Interaction* (6th ed.). Wiley.
2. Norman, D. A. (2013). *The Design of Everyday Things* (Revised & Expanded ed.). Basic Books.
3. Krug, S. (2014). *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability* (3rd ed.). New Riders.
4. Tidwell, J., Brewer, C., & Valencia, A. (2020). *Designing Interfaces: Patterns for Effective Interaction Design* (3rd ed.). O'Reilly Media.

**Pustaka Pendukung & Standar Industri:**
5. W3C. (2018/2023). *Web Content Accessibility Guidelines (WCAG) 2.1 / 2.2 Specification* — Level AA Criteria.
6. Nielsen, J. (1994/2020). *10 Usability Heuristics for User Interface Design* (Nielsen Norman Group); Brooke, J. (1996). *SUS: A Quick and Dirty Usability Scale*.
7. Google *Material Design 3 Guidelines*, Apple *Human Interface Guidelines (HIG)*, & Dokumentasi Resmi **Figma** (*Variables, Auto-Layout v5, Prototyping*).

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN (`3 SKS +P`: `100' Teori + 170' Studio Lab`)

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (`100' Kuliah + 170' Lab`) | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **`Sub-CPMK-1.1` & `1.2` (Pengantar):** Menguraikan prinsip dasar HCI (*Affordance, Signifier, Feedback*) dan 5 tahap *Design Thinking* [C2→C4] | 1.1.1 Ketepatan membedakan UI vs UX serta menganalisis contoh desain baik/buruk menurut prinsip Don Norman.<br>1.2.1 Ketepatan memetakan alur *Empathize–Define–Ideate–Prototype–Test* dan penyiapan ruang kerja kolaboratif Figma/FigJam. | **Kriteria:** Rubrik observasi studio formatif.<br>**Teknik:** Bedah produk aplikasi populer & *setup workspace* FigJam. | **Kuliah (100') + Lab Studio FigJam (170')**<br>Pembentukan tim studio (3 mhs) & pemilihan masalah produk digital nyata:<br>`[PT: 120']` · `[BM: 120']` | Kontrak belajar, aktivasi akun *Figma Education*, & tautan kanvas kolaborasi di LMS Edlink. | Pengantar HCI, *Affordances & Signifiers* (Norman), Perbedaan UI vs UX, & 5 Tahap *Design Thinking* `[1] Bab 1–2; [2] Bab 1` | — |
| **2** | **`Sub-CPMK-1.1` & `1.2`:** Melakukan riset pengguna (*User Research*) dan menyusun *Empathy Map*, *User Persona*, serta *Customer Journey Map* [C4] | 1.1.2 Ketepatan menyusun panduan wawancara kontekstual terbuka (non-bias) dan mengobservasi minimal 5 calon pengguna.<br>1.2.2 Ketepatan menyintesis temuan menjadi *Empathy Map*, *Persona* berbasis bukti, *Customer Journey Map*, dan rumusan *Point-of-View / How Might We* (HMW). | **Kriteria:** Ketajaman empati berbasis data wawancara nyata.<br>**Teknik:** *Studio Critique* atas draf Persona & Journey Map di FigJam. | **Case Method (100') + Lab FigJam Synthesis (170')**<br>Wawancara lapangan 5 responden sasaran & pemetaan *pain points*:<br>`[PT: 120']` · `[BM: 120']` | Unggah rekaman/catatan wawancara & kanvas *Empathy Map* di LMS Edlink. | Fase *Empathize & Define*: Wawancara Kontekstual, *Affinity Diagram*, *User Persona*, *Customer Journey Map*, & *HMW Statement* `[1] Bab 8 & 11` | — |
| **3** | **`Sub-CPMK-2.1`:** Merancang **Arsitektur Informasi (*Information Architecture*)**, *Card Sorting*, *Sitemap*, dan *User Flow* aplikasi [C4] | 2.1.1 Ketepatan mengorganisasikan hierarki konten/fitur melalui uji *Open/Closed Card Sorting*.<br>2.1.2 Ketepatan merancang *Sitemap* dan diagram *User Flow / Task Flow* bebas jalan buntu (*dead-end*) termasuk kondisi gagal (*empty/error state*). | **Kriteria:** Kejelasan taksonomi menu & kelengkapan *User Flow*.<br>**Teknik:** Praktikum *Card Sorting* silang antar-kelompok di studio. | **Kuliah IA (100') + Lab Workshop Card Sorting & Flow (170')**<br>Penyusunan berkas riset pengguna untuk pengumpulan Tugas 1:<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi instruksi **Tugas 1 (RTM-1)** di LMS Edlink. | *Information Architecture* (IA), *Mental Models*, *Card Sorting*, Hierarki *Sitemap*, & Pemetaan *User/Task Flow* `[3] Bab 2–6; [4] Bab 2` | — |
| **4** | **`Sub-CPMK-2.2`:** Membangun sketsa *Crazy 8s* dan **Low-Fidelity Wireframe** terstruktur [C4]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 2.2.1 Ketepatan mengeksplorasi alternatif tata letak cepat (*Crazy 8s*) lalu menerjemahkan *User Flow* menjadi rangkaian layar *Low-Fi Wireframe* tanpa distraksi warna.<br>2.2.2 Ketepatan hierarki informasi dan kejelasan label aksi (*microcopy* awal). | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-2`)**.<br>**Teknik:** Pengumpulan & Presentasi Kilat Laporan *User Research & Design Thinking Brief* (`CPMK-1`). | **Verifikasi Tugas 1 (100') + Lab Wireframing di Figma (170')**<br>Pembuatan 10–12 layar *Low-Fi Wireframe* alur utama:<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas & tautan FigJam **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Ideasi Visual (*Crazy 8s*), Prinsip *Low-Fidelity Wireframing*, Hierarki Konten, & Alur Navigasi Layar `[3] Bab 7; [4] Bab 3` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1` & `2.2` (Fondasi Visual):** Menerapkan psikologi persepsi **Gestalt**, skala tipografi, harmoni warna, dan sistem kisi **8pt Grid** [C3→C4] | 2.2.3 Ketepatan menerapkan hukum *Proximity, Similarity, Enclosure, Continuity,* & hukum HCI (*Fitts's Law, Hick's Law, Jakob's Law*).<br>2.2.4 Ketepatan menyusun skala tipografi modular, palet warna semantik (`Primary, Neutral, Success, Warning, Error`), dan perataan *8-Point Grid System*. | **Kriteria:** Keteraturan ritme visual & spasi *8pt Grid*.<br>**Teknik:** Latihan *UI Refactoring* memperbaiki layar yang padat & semrawut. | **Kuliah Desain Visual (100') + Lab Hands-on Grid & Typography (170')**<br>Penataan ulang spasi & kisi pada *wireframe* proyek:<br>`[PT: 120']` · `[BM: 120']` | Kuis visual identifikasi pelanggaran Gestalt & *Fitts's Law* di LMS Edlink. | Psikologi Gestalt, Hukum UX (*Fitts, Hick, Miller, Jakob*), Skala Tipografi, Teori Warna UI, & *8pt Spatial Grid* `[1] Bab 4; [4] Bab 4; [7]` | — |
| **6** | **`Sub-CPMK-3.1` (Pengantar Studio Figma):** Mengoperasikan **Figma Frames, Constraints, & Auto-Layout** untuk tata letak responsif multi-layar [C4→C6] | 3.1.1 Ketepatan membangun kartu, bilah navigasi, dan formulir menggunakan *Nested Auto-Layout* (`Hug, Fill Container, Fixed`, *Gap, Padding, Wrap*).<br>3.1.2 Ketahanan tata letak saat ukuran *frame* diregangkan dari layar *Mobile* (`390px`) ke *Desktop* (`1440px`). | **Kriteria:** Bebas posisi mutlak kacau saat *frame* diubah ukuran.<br>**Teknik:** Uji *live resize frame* oleh instruktur lab. | **Kuliah (100') + Workshop Intensif Figma Auto-Layout (170')**<br>Konversi kerangka *wireframe* menggunakan *Auto-Layout*:<br>`[PT: 120']` · `[BM: 120']` | Unduh berkas latihan `.fig` *Auto-Layout Drills* di LMS Edlink. | Penguasaan Studio Figma: *Frames vs Groups*, *Constraints*, *Nested Auto-Layout*, & *Responsive Breakpoints* `[7]` | — |
| **7** | **`Sub-CPMK-2.2` & `3.1`:** Merancang arsitektur komponen dapat-pakai-ulang (*Component-Driven Design: Properties & Variants*) & Klinik Pra-UTS [C4] | 3.1.3 Ketepatan membuat *Master Component*, *Boolean/Text/Instance Swap Properties*, dan *Component Variants* (`Default, Hover, Focused, Disabled, Error`).<br>2.2.5 Kesiapan paket IA, *User Flow*, dan *Mid-Fi Structured Wireframe* untuk diuji pada UTS. | **Kriteria:** Kerapian struktur *layer* & kelengkapan alur *wireframe*.<br>**Teknik:** *Design Critique* pra-UTS di studio. | **Kuliah (100') + Lab Component Variants & Klinik UTS (170')**<br>Finalisasi paket *Sitemap, User Flow,* & *Structured Wireframe*:<br>`[PT: 120']` · `[BM: 120']` | Unggah tautan kanvas persiapan UTS di LMS Edlink. | *Atomic Design* Brad Frost (*Atoms, Molecules, Organisms*) & *Figma Components/Variants* `[4]; [7]` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C4]** | Ketepatan merancang **Arsitektur Informasi (*Sitemap*)**, **User Flow** bercabang lengkap (termasuk *empty/error states*), dan rangkaian **Wireframe Terstruktur** berstandar *8pt Grid* pada tantangan kasus praktik terjadwal + validasi proyek paruh semester. | **Kriteria:** **Rubrik Analitik UTS (`K-2`)**.<br>**Teknik:** Ujian Praktik Studio Terjadwal (50% nilai UTS) + Evaluasi Validasi IA & *Wireframe* Proyek (50% nilai UTS). | **Ujian Praktik Studio & Sidang Validasi Wireframe**<br>`[170 menit]` | Pengarsipan artefak & nilai `CPMK-2` pada portal OBE/Edlink. | Evaluasi Terpadu Arsitektur Informasi, *User Flow*, Prinsip Gestalt/*8pt Grid*, & *Wireframing* (Pekan 3–7) | **25%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1`:** Membangun **Design System** dan **Design Tokens / Figma Variables** (*Color, Spacing, Radius, Typography, Dark/Light Mode*) [C6] | 3.1.4 Ketepatan membangun *Primitive Tokens* dan *Semantic Tokens* menggunakan *Figma Variables* serta pustaka komponen UI yang terdokumentasi.<br>3.1.5 Konsistensi perubahan tema otomatis tanpa mengganti warna manual satu per satu. | **Kriteria:** Kepatuhan penggunaan *tokens/styles* 100% tanpa *hardcoded hex*.<br>**Teknik:** Pemeriksaan panel *Variables & Assets* Figma di lab. | **Kuliah (100') + Studio PjBL Design System (170')**<br>Pembangunan halaman *Design System Foundation & UI Kit* proyek:<br>`[PT: 120']` · `[BM: 120']` | Contoh struktur *Material 3 / Polaris Design System* di LMS Edlink. | Arsitektur *Design System*: *Primitive vs Semantic Design Tokens*, *Figma Variables*, Dokumentasi *UI Library* `[7]` | — |
| **10** | **`Sub-CPMK-3.1`:** Membangun **High-Fidelity Interactive Prototype** (*Flows, Overlays, Variables/Conditional Logic, & Micro-interactions*) [C6] | 3.1.6 Ketepatan merangkai layar *High-Fidelity* menjadi purwarupa dapat-diklik utuh dari awal hingga tuntas (*end-to-end clickable tasks*) menggunakan *Smart Animate*, *Sticky Scroll*, dan *Interactive Components*. | **Kriteria:** Kelancaran interaksi tanpa tautan mati (*broken prototype links*).<br>**Teknik:** Uji klik silang purwarupa *High-Fi* di studio. | **Kuliah Interaksi Mikro (100') + Lab Prototyping Figma (170')**<br>Perakitan aliran interaksi *High-Fidelity* untuk 3 skenario tugas utama:<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi instruksi **Tugas 2 (RTM-2)** di LMS Edlink. | *High-Fidelity UI Design*, *Micro-interactions*, *Smart Animate*, *Modal/Drawer Overlays*, & *Interactive Flows* `[1] Bab 12; [7]` | — |
| **11** | **`Sub-CPMK-3.2`:** Mengaudit dan menerapkan standar **Aksesibilitas Digital WCAG 2.1 Level AA** pada desain antarmuka [C6] | 3.2.1 Ketepatan memenuhi rasio kontras warna minimum **4,5:1** (teks normal) dan **3:1** (teks besar & komponen UI), ukuran target sentuh minimal `44×44 px` / `48×48 dp`, indikator *focus state* papan ketik, serta tidak bergantung pada warna semata untuk pesan galat. | **Kriteria:** Lulus 100% audit *Contrast & Accessibility Plugin* pada layar inti.<br>**Teknik:** Audit aksesibilitas langsung di Figma menggunakan *Stark / Contrast Checker* & simulasi buta warna. | **Kuliah WCAG (100') + Lab Accessibility Audit & Remediation (170')**<br>Perbaikan warna, ukuran sentuh, & anotasi aksesibilitas untuk Tugas 2:<br>`[PT: 120']` · `[BM: 120']` | Ceklis wajib WCAG 2.1 AA untuk desainer UI/UX di LMS Edlink. | *Inclusive Design & Web Content Accessibility Guidelines* (**WCAG 2.1 Level AA**): Kontras, Tipografi Terbaca, *Touch Target*, *Focus Order*, & Buta Warna `[5]` | — |
| **12** | **`Sub-CPMK-4.1` (Perencanaan Uji) & Evaluasi Tugas 2 (`CPMK-3`):** Menyusun protokol *Usability Testing Plan* & skenario tugas uji pengguna [C5]<br>*(+ Penilaian Milestone Tugas 2)* | 4.1.1 Ketepatan menyusun *Moderator Script*, kriteria partisipan, metrik keberhasilan tugas (*Task Completion Rate, Time-on-Task, Error Count*), dan skenario tugas non-mengarahkan (*non-leading tasks*). | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-2`)**.<br>**Teknik:** Inspeksi langsung berkas Figma *Design System + WCAG Hi-Fi Prototype* (`CPMK-3`) oleh dosen di studio. | **Inspeksi Studio Tugas 2 (120') + Kuliah/Lab Usability Plan (150')**<br>Rekrutmen minimal 5 partisipan sasaran untuk uji kebergunaan pekan depan:<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan tautan terproteksi versi **Tugas 2 (`CPMK-3`)** & unduh lembar kuesioner **SUS** di LMS Edlink. | Metodologi *Moderated Usability Testing*: Penyusunan *Task Scenarios*, Protokol *Think-Aloud*, & Etika Persetujuan Partisipan `[1] Bab 14–15; [3] Bab 9` | **25%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1`:** Mengeksekusi sesi **Usability Testing** dan menghitung serta menafsirkan skor **System Usability Scale (SUS)** [C5] | 4.1.2 Ketepatan memfasilitasi sesi *Think-Aloud Usability Testing* pada $\ge 5$ pengguna sasaran.<br>4.1.3 Ketepatan menghitung skor **SUS** ($\sum$ butir ganjil $(x_i - 1)$ dan butir genap $(5 - x_i)$ dikali $2,5$) beserta interpretasi predikat persentil/grade (*Acceptable / Marginal / Not Acceptable*). | **Kriteria:** Keakuratan tabulasi rumus SUS & pencatatan kendala observasi.<br>**Teknik:** Praktikum eksekusi uji pengguna & pengolahan lembar kerja SUS. | **Kuliah Analisis SUS (100') + Lab Usability Testing Session (170')**<br>Tabulasi kuantitatif skor SUS & matriks temuan kendala pengguna:<br>`[PT: 120']` · `[BM: 120']` | Unggah lembar skor mentah SUS & bukti dokumentasi pengujian di LMS Edlink. | Eksekusi *Usability Testing*, Perhitungan Kuantitatif **System Usability Scale (SUS)** John Brooke, & Pemetaan *Rainbow Spreadsheet* `[1] Bab 15; [6]` | — |
| **14** | **`Sub-CPMK-4.2`:** Melakukan audit ahli menggunakan **10 Usability Heuristics Jakob Nielsen** & prioritisasi tingkat keparahan (*Severity Rating* 0–4) [C5] | 4.2.1 Ketepatan mengidentifikasi pelanggaran spesifik terhadap ke-10 heuristik Nielsen (*Visibility of System Status, Match with Real World, User Control, Consistency, Error Prevention, Recognition vs Recall, Flexibility, Minimalist Design, Error Recovery, Help*).<br>4.2.2 Ketepatan menetapkan *Severity Rating* (`0–4`) dan merancang iterasi perbaikan *Before vs After* pada purwarupa Figma. | **Kriteria:** Ketajaman diagnosis heuristik & kualitas desain perbaikan.<br>**Teknik:** Audit silang (*Peer Expert Heuristic Evaluation*) antar-tim di lab. | **Kuliah 10 Heuristik (100') + Lab Heuristic Audit & Redesign (170')**<br>Iterasi perbaikan *High-Fi Prototype v2.0* berdasarkan temuan SUS & Heuristik:<br>`[PT: 120']` · `[BM: 120']` | Templat matriks audit 10 Heuristik Nielsen & *Severity Rating* di LMS Edlink. | Evaluasi Inspeksi Ahli: **10 Usability Heuristics Jakob Nielsen**, Skala Keparahan *Severity 0–4*, & Siklus Iterasi Desain *Before–After* `[6]` | — |
| **15** | **`Sub-CPMK-4.2` & Handoff:** Menyusun spesifikasi *Developer Handoff* menuju `STI-311` dan naskah **UI/UX Case Study Portfolio** berstandar industri [C5→C6] | 4.2.3 Ketepatan menyiapkan anotasi spesifikasi komponen/spasi/token untuk diserahkan ke pengembang *front-end* (`STI-311`).<br>4.2.4 Kelengkapan narasi studi kasus portofolio (*Problem → Research → IA/Wireframe → Design System & WCAG → SUS & Heuristic Iteration*). | **Kriteria:** Kesiapan pameran & kelengkapan bukti data evaluasi.<br>**Teknik:** *Portfolio Rehearsal* & klinik akhir di studio. | **Studio PjBL Portfolio & Dev-Handoff Prep (270')**<br>Penyelesaian laporan evaluasi kebergunaan & dek pameran UAS:<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan draf laporan uji SUS/Heuristik & tautan purwarupa final v2.0 di LMS Edlink. | *Design-to-Developer Handoff* (Menuju `STI-311 Pengembangan Web Front End`) & Struktur Penulisan *UI/UX Case Study Portfolio* `[4]; [7]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C5]** | Ketajaman evaluasi kegunaan antarmuka berbasis bukti kuantitatif **SUS** dan analisis kualitatif **10 Heuristik Nielsen**, kualitas iterasi perbaikan purwarupa *Before–After*, serta penguasaan individu saat *Demo Day & Defense*. | **Kriteria:** **Rubrik Analitik UAS (`K-2`)**.<br>**Teknik:** Penilaian Laporan Uji SUS & Heuristik + Iterasi Purwarupa Final + *Demo Day & Individual Defense*. | **UI/UX Showcase, Live Prototype Walkthrough, & Sidang Individu**<br>`[170 menit]` | Pengarsipan portofolio UI/UX final & rekap ketercapaian `CPL-13` pada portal OBE. | Evaluasi Komprehensif *Usability Testing* (SUS), *Heuristic Evaluation*, Iterasi Desain, & Portofolio Studi Kasus UI/UX | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-13` [C4])
* **Bentuk Instrumen:** Laporan & Kanvas FigJam **User Research & Design Thinking Discovery Brief** (wawancara nyata minimal 5 calon pengguna, *Affinity Diagram*, *Empathy Map*, 2 *User Persona* berbasis data, *Customer Journey Map* saat ini, dan perumusan masalah *Point-of-View / How Might We*) disertai verifikasi kontribusi individu di studio.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kualitas protokol & kedalaman bukti wawancara/observasi lapangan = **35%**; (2) Ketajaman sintesis *Persona* & *Customer Journey Map* berbasis bukti = **35%**; (3) Ketepatan pembingkaian masalah *Design Thinking* (POV & HMW) = **20%**; (4) Kerapian dokumentasi kanvas riset & etika persetujuan responden = **10%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 25% · Mengukur `CPMK-2` / `CPL-13` [C4])
* **Bentuk Instrumen:** Kombinasi **Ujian Praktik Studio Terjadwal Individu di Figma (50% nilai UTS)** — merancang *User Flow* dan 4 layar *Low-Fi Wireframe* ber-*8pt Grid* untuk sebuah skenario kasus baru dalam 120 menit — dan **Validasi Paket IA (*Card Sorting + Sitemap*), *User Flow*, & *Wireframe* Proyek (50% nilai UTS)**.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kelogisan struktur *Information Architecture* (*Sitemap*) & kelengkapan *User Flow* = **35%**; (2) Kualitas hierarki visual, prinsip Gestalt, & disiplin *8pt Grid* pada *Wireframe* = **35%**; (3) Penanganan skenario tepi (*empty state, confirmation, error state*) = **20%**; (4) Kerapian penamaan *frame/layer* & kejelasan anotasi navigasi = **10%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 25% · Mengukur `CPMK-3` / `CPL-13` [C6])
* **Bentuk Instrumen:** Inspeksi Studio atas berkas Figma **Design System & WCAG-Compliant High-Fidelity Interactive Prototype** (memuat *Figma Variables/Design Tokens*, komponen ber-*Auto-Layout* & *Variants*, minimal 14–18 layar *High-Fidelity* yang terhubung interaktif untuk 3 alur tugas utama, serta lembar bukti kelulusan audit aksesibilitas **WCAG 2.1 Level AA**).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Arsitektur *Design System* (*Tokens/Variables, Nested Auto-Layout, Component Variants*) = **35%**; (2) Kualitas estetika visual & kelancaran interaksi purwarupa *High-Fidelity* = **30%**; (3) Kepatuhan terukur standar aksesibilitas **WCAG 2.1 Level AA** (kontras $\ge 4,5:1$, *touch target*, *focus/error states*) = **25%**; (4) Keteraturan organisasi berkas Figma & kesiapan *dev-handoff* = **10%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-13` [C5])
* **Bentuk Instrumen:** **Laporan Evaluasi Kebergunaan (SUS & 10 Heuristik Nielsen) + Purwarupa Iterasi v2.0 (*Before–After*) + Portofolio Studi Kasus UI/UX** yang dipamerkan dan dipertahankan secara individu pada sesi *Demo Day & Defense* (170 menit).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Metodologi eksekusi *Usability Testing* & ketepatan perhitungan/interpretasi kuantitatif **SUS** = **30%**; (2) Ketajaman diagnosis kualitatif **10 Heuristik Nielsen** & penetapan *Severity Rating* = **30%**; (3) Kualitas perbaikan desain iteratif (*Before vs After*) berbasis bukti temuan = **25%**; (4) Kualitas naskah portofolio studi kasus & pertahanan individu saat sidang = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK HCI & Rekayasa Platform Digital**<br><br><br>*(Tanda Tangan)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
