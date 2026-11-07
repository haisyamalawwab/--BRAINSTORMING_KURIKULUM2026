# 065_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017 · Standar W3C / MDN)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI311`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, 043, & Pilot `STI-311`) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Pengembangan Web Front End / *Web Front End Development* |
| **Kode Mata Kuliah** | `STI-311` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Rekayasa Perangkat Lunak & Platform (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS (`+P`)** (`T = 2, P = 1`) — Tatap Muka `2×50' = 100'`, Praktikum Terbimbing `1×170' = 170'`, Penugasan Terstruktur `2×60' = 120'`, Belajar Mandiri `2×60' = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Konstruksi Antarmuka Web Modern (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `FST-102` Algoritma dan Pemrograman |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Menerima *Design System* & prototipe dari `STI-308` Desain & Prototyping UI/UX; menyerahkan integrasi penuh *client–server* ke `STI-416` Pengembangan Web Back End, `STI-522` Pemrograman Aplikasi Mobile, & `STI-625` Rekayasa Platform Digital |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-08` (`P4` = **45%**) dan `CPL-13` (`KK5` = **55%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 2 (`K-2`)** — Pemrograman, Algoritma, Basis Data, & Platform Web/Mobile (Bobot MK `+P`: Tugas 1 `20%` · UTS `25%` · Tugas 2 `25%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Rekayasa Perangkat Lunak & Platform |
| **Koordinator RMK** | Dr. Roni Wahyu, S.Kom., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-08`** (`P4`) | Pengetahuan | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | **R** (*Reinforce*) | **45%** |
| **`CPL-13`** (`KK5`) | Keterampilan Khusus | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | **R** (*Reinforce*) | **55%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **membangun** antarmuka web responsif menggunakan **HTML5 semantik** dan **CSS3 modern (*Flexbox, Grid*)** (*B*) yang adaptif lintas resolusi perangkat (*C*) dengan standar aksesibilitas dasar (*D*). | **C3** (*Apply*) | `CPL-08` (`P4`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **mengimplementasikan** interaktivitas halaman web menggunakan **JavaScript ES6+**, manipulasi **DOM**, dan komunikasi asinkron (*Fetch API, Async/Await*) (*B*) secara bersih dan bebas *error* (*C, D*). | **C3** (*Apply*) | `CPL-08` (`P4`) | **UTS — Pekan 8 (25%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **membangun** aplikasi *Single Page Application* (**SPA**) menggunakan kerangka kerja **React** (*Component, Props, State, Hooks, Router*) (*B*) dengan arsitektur komponen yang *reusable* (*C, D*). | **C6** (*Create*) | `CPL-13` (`KK5`) | **Tugas 2 — Pekan 12 (25%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **mengintegrasikan** aplikasi *front-end* dengan **RESTful API** eksternal dan **mengoptimasi** performa muat (*Lighthouse score* $\ge 85$) (*B, C*) secara terverifikasi (*D*). | **C5** (*Evaluate*) | `CPL-13` (`KK5`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Membangun halaman web menggunakan **HTML5 semantik** dengan standar aksesibilitas dasar. | `CPMK-1` | **C3** | Mg 1–2 |
| **`Sub-CPMK-1.2`** | Menerapkan **CSS3 modern (*Flexbox, Grid*)** yang responsif lintas resolusi perangkat. | `CPMK-1` | **C3** | Mg 2–4 |
| **`Sub-CPMK-2.1`** | Mengimplementasikan interaktivitas web menggunakan **JavaScript ES6+** dan manipulasi **DOM**. | `CPMK-2` | **C3** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Mengimplementasikan komunikasi asinkron menggunakan **Fetch API** dan **Async/Await**. | `CPMK-2` | **C3** | Mg 7 |
| **`Sub-CPMK-3.1`** | Membangun komponen **React** (*Component, Props, State, Hooks*) yang *reusable*. | `CPMK-3` | **C6** | Mg 9–10 |
| **`Sub-CPMK-3.2`** | Mengonfigurasi **React Router** dan *state management* pada aplikasi **SPA**. | `CPMK-3` | **C6** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Mengintegrasikan aplikasi *front-end* dengan **RESTful API** eksternal secara terverifikasi. | `CPMK-4` | **C5** | Mg 13–14 |
| **`Sub-CPMK-4.2`** | Mengoptimasi performa muat aplikasi web hingga mencapai **Lighthouse score $\ge 85$**. | `CPMK-4` | **C5** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Integrasi RESTful API Eksternal & Optimasi Performa Lighthouse >= 85 (C5) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: Fetch/Axios CRUD, Auth State, Error/Skeleton UI | Sub-CPMK-4.2: Lazy Loading, Core Web Vitals, Lighthouse >= 85)
      │
[CPMK-3: Rekayasa Single Page Application (SPA) dengan React Reusable Components (C6) — Mg 9–12 (Tugas 2 25%)]
      ▲  (Sub-CPMK-3.1: JSX, Props, useState, useEffect, Controlled Forms | Sub-CPMK-3.2: React Router, Context API, Custom Hooks)
      │
[CPMK-2: Interaktivitas JavaScript ES6+, Manipulasi DOM, & Asinkroni Fetch/Async-Await (C3) — Mg 5–8 (UTS 25%)]
      ▲  (Sub-CPMK-2.1: ES6+ Modules/HOF, DOM Tree, Event Delegation | Sub-CPMK-2.2: Event Loop, Promises, Async/Await, Fetch JSON)
      │
[CPMK-1: Fondasi Antarmuka Web Responsif HTML5 Semantik & CSS3 Flexbox/Grid (C3) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: W3C HTML5 Semantic, Form Validation, ARIA Dasar | Sub-CPMK-1.2: Box Model, Flexbox, Grid, Mobile-First)
      ▲
[Fondasi Prasyarat: FST-102 Algoritma dan Pemrograman + Sinergi Design Tokens/Prototipe dari STI-308]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-08`** (`P4`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-08` = 45%** |
| **`CPL-08`** (`P4`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **25%** | — | — | **25%** | *(20% + 25%)* |
| **`CPL-13`** (`KK5`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **25%** | — | **25%** | **`CPL-13` = 55%** |
| **`CPL-13`** (`KK5`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | *(25% + 30%)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **25%** | **25%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 70\%$ untuk Klaster `K-2` Dok 018):** `Tugas 1 (20% — Case-Based Responsive Accessible Slicing) + Tugas 2 (25% — Project-Based Multi-View React SPA Component Architecture) + UAS (30% — Project-Based API-Connected Optimized Production Web App & Live Defense)` = **75%** *(persis selaras dengan tabel IKU 7 Dokumen 004 untuk `STI-311` = 75%)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-311 Pengembangan Web Front End` (3 SKS `+P`) membekali mahasiswa dengan keahlian rekayasa antarmuka aplikasi web sisi klien berstandar industri modern. Pembelajaran dimulai dari konstruksi dokumen **HTML5 semantik** beraksesibilitas dasar (**WAI-ARIA / WCAG**), tata letak adaptif *mobile-first* menggunakan **CSS3 modern (*Custom Properties, Flexbox, CSS Grid*, & *Utility CSS*)**, pemrograman interaktif **JavaScript ES6+** (*destructuring, modules, array higher-order functions*), manipulasi **DOM**, serta komunikasi data asinkron via **Fetch API & `async/await`**. Pada paruh kedua semester, mahasiswa merekayasa **Single Page Application (SPA)** berbasis **React** (*Component-Driven Architecture, Props, State, Hooks, Controlled Forms, React Router, Context API*), mengintegrasikannya dengan **RESTful API** eksternal, serta mengoptimasi *Core Web Vitals* hingga terverifikasi mencapai skor **Google Lighthouse $\ge 85$**.

* **🟢 IN-SCOPE (Wajib Diajarkan):** HTML5 Semantik & Aksesibilitas Dasar, CSS3 *Box Model / Flexbox / Grid / Media Queries / Tailwind Utility*, JavaScript ES6+, DOM & *Events*, *Fetch API & Async/Await*, **React SPA** (*Components, Props, State, Hooks, Router, Context*), konsumsi **RESTful API** eksternal, mitigasi dasar *client-side XSS*, optimasi aset/*lazy loading*, *deployment* statis, dan audit **Lighthouse $\ge 85$**.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. **Dilarang membangun server *back-end* produksi** (Node.js/Express/FastAPI), perancangan tabel SQL, maupun pembuatan server otentikasi JWT dari nol (ranah eksklusif **`STI-416 Pengembangan Web Back End`** di Semester 4; pada `STI-311` mahasiswa wajib mengonsumsi *public REST API* terkurasi atau *mock API server* seperti `JSON Server / DummyJSON / ReqRes` siap pakai!).
  2. Dilarang mengulang proses riset pengguna awal (*User Interview, Persona, Empathy Map*) dari nol (ranah ko-semester **`STI-308 Desain & Prototyping UI/UX`**; pada `STI-311` mahasiswa fokus menerjemahkan desain ke kode antarmuka berkinerja tinggi).
* **🔄 HANDOFF ANCHOR:** Menerima prototipe & *Design Tokens* dari `STI-308`, bersinergi dengan disiplin *Clean Code* `STI-309`, lalu menyerahkan fondasi klien SPA ke **`STI-416 Pengembangan Web Back End`** (integrasi *Full-Stack*), **`STI-522 Pemrograman Aplikasi Mobile`**, dan **`STI-625 Rekayasa Platform Digital`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS12` (*User Experience Design*) & `BK-IT04` (*Web and Mobile Systems*).

**Pustaka Utama:**
1. MDN Web Docs (Mozilla Developer Network). (2024–2026). *HTML, CSS, JavaScript, Web Accessibility, & Fetch API Documentation*.
2. Haverbeke, M. (2024). *Eloquent JavaScript: A Modern Introduction to Programming* (4th ed.). No Starch Press.
3. React Core Team (Meta). (2024–2026). *Official React Documentation (react.dev — Modern Hooks & Component Architecture)*.

**Pustaka Pendukung:**
4. Grant, K. J. (2024). *CSS in Depth* (2nd ed.). Manning Publications.
5. Osmani, A. (2024). *Learning JavaScript Design Patterns* (2nd ed.) & Google *web.dev Core Web Vitals / Lighthouse Guide*.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Teori + Praktikum) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1`:** Membangun dokumen **HTML5 semantik** yang valid berdasarkan cara kerja HTTP, *DOM Tree*, dan aksesibilitas dasar [C2→C3] | 1.1.1 Ketepatan menggunakan elemen semantik (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) dibanding penyalahgunaan `<div>` (*div-soup*).<br>1.1.2 Ketepatan menyusun hierarki *heading* `h1–h6`, atribut `alt`, dan struktur dokumen lolos *W3C Markup Validator*. | **Kriteria:** Validasi W3C bebas *error*.<br>**Teknik:** Pemeriksaan hasil praktikum *markup* semantik di lab. | **Kuliah Interaktif** `[TM: 100']`<br>**Praktikum Lab 1:** Penyiapan *VS Code, Browser DevTools, Git*, & pembangunan kerangka HTML5 semantik `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kontrak belajar, unduh panduan kakas & starter kit di LMS Edlink. | Arsitektur Web Klien (*HTTP, Browser Rendering Pipeline*), **HTML5 Semantik**, & Standar Validasi W3C `[1]` | — |
| **2** | **`Sub-CPMK-1.1` & `1.2` (Awal):** Membangun formulir HTML5 aksesibel (*native validation, `<label>`, ARIA dasar*) serta fondasi **CSS3 Box Model & Custom Properties** [C3] | 1.1.3 Ketepatan menautkan `<label for>`, atribut validasi HTML5, *keyboard focus*, dan rasio kontras WCAG AA.<br>1.2.1 Ketepatan menerapkan `box-sizing: border-box`, spesifisitas selektor, tipografi `rem/clamp()`, dan variabel token CSS (`--color-*`, `--space-*` dari `STI-308`). | **Kriteria:** Formulir dapat dinavigasi penuh menggunakan *keyboard Tab* & skor Accessibility awal $\ge 90$.<br>**Teknik:** Cek modul praktikum formulir & *design tokens* CSS. | **Ceramah & Live Coding** `[TM: 100']`<br>**Praktikum Lab 2:** Formulir HTML5 Aksesibel + Sistem Variabel *Design Tokens* CSS3 `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis spesifisitas CSS & *Box Model* di LMS Edlink. | Formulir HTML5, Dasar Aksesibilitas Web (**WCAG / ARIA**), **CSS3 Box Model**, Selektor, & *CSS Custom Properties* `[1]; [4]` | — |
| **3** | **`Sub-CPMK-1.2`:** Menerapkan tata letak modern **CSS3 Flexbox** (1 dimensi) dan **CSS Grid** (2 dimensi) [C3] | 1.2.2 Ketepatan menata komponen baris/kolom menggunakan properti induk & anak **Flexbox** (`justify-content`, `align-items`, `flex-wrap`, `gap`).<br>1.2.3 Ketepatan membangun tata letak halaman 2 dimensi menggunakan **CSS Grid** (`grid-template-columns`, `repeat(auto-fit, minmax(...))`, `grid-template-areas`). | **Kriteria:** Tata letak presisi tanpa *hack* `float` usang.<br>**Teknik:** Tantangan praktikum membangun *Dashboard & Card Gallery* dengan Flexbox + Grid. | **Problem-Based Coding** `[TM: 100']`<br>**Praktikum Lab 3:** Konstruksi Tata Letak Kompleks dengan **CSS3 Flexbox & CSS Grid** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi spesifikasi **Tugas 1 (RTM-1)** di LMS Edlink. | Tata Letak Modern: **CSS3 Flexbox** vs **CSS3 Grid** & *Intrinsic Responsive Design* `[1]; [4]` | — |
| **4** | **`Sub-CPMK-1.2`:** Membangun desain web responsif **Mobile-First** (*Media Queries, Fluid Images*) & pengenalan *Utility-First CSS* (`Tailwind CSS`) [C3]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.4 Ketepatan mengadaptasi tampilan lintas *viewport* (*Mobile `360px` → Tablet `768px` → Desktop `1280px+`*) bebas *horizontal overflow*.<br>1.2.5 Ketepatan menggunakan utilitas *styling* modern secara konsisten. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-2`)**.<br>**Teknik:** Pengumpulan Repositori & Demo Slicing Antarmuka Responsif Aksesibel + Inspeksi *DevTools Responsive Mode*. | **Demo & Verifikasi Praktikum Tugas 1** `[TM: 100']`<br>**Praktikum Lab 4:** *Mobile-First Media Queries*, Pengenalan *Tailwind CSS*, & Uji Tugas 1 `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan tautan repositori & halaman hidup **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Strategi **Mobile-First Responsive Design**, Gambar Adaptif (`srcset`, `<picture>`), & *Utility-First CSS* `[1]; [4]` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1` (Bagian I):** Mengimplementasikan logika **JavaScript Modern (ES6+)** secara modular dan imutabel [C3] | 2.1.1 Ketepatan menggunakan `let/const`, *template literals*, *arrow functions*, *destructuring*, *spread/rest operator*, *optional chaining* (`?.`), serta *ES Modules* (`import/export`).<br>2.1.2 Ketepatan mengolah koleksi data menggunakan fungsi orde tinggi (`map`, `filter`, `reduce`, `find`, `some`) tanpa mutasi liar. | **Kriteria:** Kode ES6+ berjalan bersih bebas galat di konsol.<br>**Teknik:** Latihan praktikum transformasi larik objek JSON. | **Ceramah & Live Coding ES6+** `[TM: 100']`<br>**Praktikum Lab 5:** Latihan Intensif **JavaScript ES6+**, *Array HOF*, & *ES Modules* `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis transformasi `map/filter/reduce` di LMS Edlink. | **JavaScript ES6+**: Cakupan Variabel, *Destructuring*, *Spread/Rest*, *Higher-Order Array Methods*, & *ES Modules* `[1]; [2] Bab 4–6` | — |
| **6** | **`Sub-CPMK-2.1` (Bagian II):** Mengimplementasikan manipulasi **DOM**, *Event Handling / Delegation*, validasi interaktif, & penyimpanan lokal (`localStorage`) [C3] | 2.1.3 Ketepatan merender elemen **DOM** secara dinamis dan aman (`textContent` / pembuatan elemen aman mencegah *DOM-based XSS*, bukan `innerHTML` mentah dari input pengguna!).<br>2.1.4 Ketepatan menerapkan *Event Bubbling & Delegation* serta persistensi *state* ringan di `localStorage`. | **Kriteria:** Antarmuka interaktif bebas *error console* & aman dari injeksi skrip input.<br>**Teknik:** Praktikum membangun aplikasi katalog/keranjang belanja interaktif murni DOM. | **Case-Based Coding DOM** `[TM: 100']`<br>**Praktikum Lab 6:** Manipulasi **DOM** Aman, *Event Delegation*, & `localStorage` `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan kode praktikum interaktivitas DOM di LMS Edlink. | *Document Object Model* (**DOM**), *Event Propagation & Delegation*, Mitigasi Dasar *DOM XSS*, & *Web Storage API* `[1]; [2] Bab 14–15` | — |
| **7** | **`Sub-CPMK-2.2`:** Mengimplementasikan pemrograman asinkron JavaScript (*Event Loop, Promises*, **`async/await`**, & **Fetch API**) dengan penanganan *loading/error* bersih [C3] | 2.2.1 Ketepatan menjelaskan mekanisme *Call Stack, Web APIs, Task/Microtask Queue* pada *Event Loop*.<br>2.2.2 Ketepatan mengambil & mengirim data JSON melalui **Fetch API + `async/await` + `try/catch/finally`** lengkap indikator *loading* dan pesan gagal ramah pengguna. | **Kriteria:** Permintaan HTTP terkelola bersih pada sukses (`2xx`), gagal (`4xx/5xx`), maupun jaringan putus.<br>**Teknik:** Praktikum konsumsi REST API publik + klinik pra-UTS. | **Problem-Solving Asinkroni & Klinik UTS** `[TM: 100']`<br>**Praktikum Lab 7:** Konsumsi **Fetch API** dengan `async/await` & Penanganan Galat `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Simulasi kisi-kisi ujian praktik UTS di LMS Edlink. | Asinkroni JavaScript: *Event Loop*, *Promises*, **`async/await`**, **Fetch API**, JSON, & *Error Handling* `[1]; [2] Bab 11` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C3]** | Keberhasilan membangun halaman web interaktif secara langsung (*live coding*) menggunakan **JavaScript ES6+**, manipulasi **DOM**, pencarian/penyaringan dinamis, dan konsumsi data asinkron **Fetch API (`async/await`)** secara bersih dan bebas *error*. | **Kriteria:** **Rubrik Analitik UTS Praktik (`K-2`)**.<br>**Teknik:** Ujian Praktik *Live Coding* Terawasi di Laboratorium. | **Ujian Praktik Pemrograman Luring di Lab**<br>`[150 menit]` | Pengarsipan kode ujian & nilai `CPMK-2` pada portal OBE. | Materi **JavaScript ES6+**, Manipulasi **DOM**, *Events*, & **Fetch API / `async/await`** (Pekan 5–7) | **25%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1` (Bagian I):** Membangun arsitektur **Single Page Application (SPA)** dengan **React** (*Vite Tooling, JSX, Functional Components, & Props*) [C3→C6] | 3.1.1 Ketepatan memecah antarmuka menjadi hierarki komponen **React** yang kecil, kohesif, dan *reusable* (*Button, Card, Badge, Modal*).<br>3.1.2 Ketepatan mengalirkan data satu arah melalui **Props**, *children composition*, dan merender daftar dengan `key` unik stabil. | **Kriteria:** Komponen modular dapat dipakai ulang dengan variasi *props* tanpa duplikasi markup.<br>**Teknik:** Praktikum inisialisasi proyek React + Vite & pembuatan pustaka komponen UI dasar. | **Interactive Lecture React** `[TM: 100']`<br>**Praktikum Lab 8:** Arsitektur **SPA**, *Vite*, **JSX**, *Reusable Components*, & **Props** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Unduh struktur arsitektur folder React bersih di LMS Edlink. | Paradigma Deklaratif **SPA vs MPA**, *Virtual DOM*, **JSX**, *Functional Components*, & **Props** `[3]` | — |
| **10** | **`Sub-CPMK-3.1` (Bagian II):** Mengelola interaktivitas komponen **React** menggunakan **State (`useState`)**, *Controlled Forms*, *Lifting State Up*, & efek samping **`useEffect`** [C6] | 3.1.3 Ketepatan mengelola pembaruan *state* imutabel dengan **`useState`**, formulir terkendali (*controlled inputs*), dan komunikasi anak-ke-induk (*lifting state up*).<br>3.1.4 Ketepatan mengelola siklus efek samping dan fungsi pembersih (*cleanup function*) pada **`useEffect`** tanpa *infinite loop*. | **Kriteria:** Aliran *state* reaktif bersih tanpa mutasi langsung variabel *state*.<br>**Teknik:** Praktikum membangun fitur formulir dinamis, filter multi-kriteria, dan sinkronisasi efek di React. | **Case-Based Coding React Hooks** `[TM: 100']`<br>**Praktikum Lab 9:** **`useState`**, *Controlled Forms*, *Lifting State Up*, & **`useEffect`** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi spesifikasi proyek **Tugas 2 (RTM-2)** di LMS Edlink. | Manajemen *State* Komponen (**`useState`**), Imutabilitas, *Controlled Components*, & Siklus **`useEffect`** `[3]` | — |
| **11** | **`Sub-CPMK-3.2`:** Mengonfigurasi navigasi multi-halaman **React Router** (*Nested Routes, Dynamic Params*) dan manajemen *state* lintas-komponen (**Context API & Custom Hooks**) [C6] | 3.2.1 Ketepatan mengonfigurasi rute deklaratif **React Router** (`Outlet` tata letak bersama, parameter URL `:id`, navigasi terprogram, & halaman `404 Not Found`).<br>3.2.2 Ketepatan menghilangkan *prop drilling* menggunakan **`useContext` / `useReducer`** (mis. *Theme / Cart / Auth Context*) dan mengekstrak logika berulang menjadi **Custom Hooks** (`useFetch`, `useDebounce`). | **Kriteria:** Navigasi SPA instan tanpa *full-page reload* & *Custom Hook* bersih dipakai lintas halaman.<br>**Teknik:** Praktikum perutean multi-tampilan & *Context Provider*. | **Problem-Based Coding SPA Architecture** `[TM: 100']`<br>**Praktikum Lab 10:** **React Router**, **Context API**, & **Custom Hooks** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Panduan pola *Context + Custom Hook* di LMS Edlink. | *Client-Side Routing* (**React Router**), *Layout Routes*, **Context API**, & Abstraksi **Custom Hooks** `[3]; [5]` | — |
| **12** | **`Sub-CPMK-3.1` & `3.2` (Evaluasi SPA):** Penataan arsitektur komponen **React SPA** yang *reusable* & pengantar pola pengambilan data modern [C6]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.3 Ketepatan menstrukturkan repositori SPA (`components/ui`, `features`, `pages`, `hooks`, `context`) yang teruji fungsionalitas dan *reusability*-nya. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-2`)**.<br>**Teknik:** Demo Langsung & *Code Walkthrough* Proyek **React SPA** di Laboratorium. | **Review Arsitektur Komponen & Uji Tugas 2** `[TM: 100']`<br>**Praktikum Lab 11:** Verifikasi Demo & Bedah Kode **Tugas 2 (`CPMK-3`)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan repositori Git **Tugas 2 (`CPMK-3`)** di LMS Edlink. | Pola Komposisi Komponen Lanjut (*Compound/Presentational-Container*), Struktur Proyek Skalabel, & Evaluasi SPA `[3]; [5]` | **25%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1`:** Mengintegrasikan aplikasi **React SPA** dengan **RESTful API** eksternal secara penuh (*CRUD Operations, Search/Pagination Query, Loading Skeleton, & Error Boundary*) [C5] | 4.1.1 Ketepatan mengintegrasikan operasi `GET, POST, PUT/PATCH, DELETE` terhadap **RESTful API** eksternal/mock menggunakan lapisan layanan terpusat (`apiClient` + variabel `.env`).<br>4.1.2 Ketepatan menyajikan status antarmuka lengkap (*Empty State, Skeleton Loading, Toast Feedback, & Retry Error State*). | **Kriteria:** Seluruh alur transaksi data dengan REST API berjalan mulus dan tahan gangguan jaringan.<br>**Teknik:** Praktikum integrasi penuh CRUD ke *Mock/Public REST API* *(tanpa menulis kode server DB ranah `STI-416`)*. | **Interactive Lecture API Integration** `[TM: 100']`<br>**Praktikum Lab 12:** Integrasi Penuh **RESTful API** Eksternal, Paginasi, & *UI States* `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Daftar *Public / Mock REST API* resmi proyek UAS di LMS Edlink. | Arsitektur Layanan Klien HTTP, Integrasi **RESTful API** (*Headers, Query Params, Status Codes*), *Debounced Search*, & *Resilient UI States* `[1]; [3]` | — |
| **14** | **`Sub-CPMK-4.1` & `4.2` (Awal):** Mengimplementasikan alur *Client-Side Protected Routes*, keamanan antarmuka dasar, serta teknik optimasi **Code Splitting & Memoization** [C5] | 4.1.3 Ketepatan mengamankan rute privat sisi klien (*Protected Route Wrapper*), pengelolaan sesi aman di sisi klien, dan sanitasi tampilan.<br>4.2.1 Ketepatan memangkas ukuran *initial JS bundle* menggunakan **`React.lazy()` + `<Suspense>`** serta mencegah *re-render* berat dengan `useMemo`/`useCallback` secara terukur. | **Kriteria:** Ukuran *bundle* awal turun nyata pada *build* produksi.<br>**Teknik:** Praktikum *Route Guard* & inspeksi ukuran *chunk* `vite build`. | **Case-Based Optimization Lecture** `[TM: 100']`<br>**Praktikum Lab 13:** *Protected Routes*, **`React.lazy` Code Splitting**, & Optimasi Render `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Panduan pembacaan *Vite Bundle Visualizer* di LMS Edlink. | *Protected Routes* Sisi Klien, Keamanan *Front-End* Dasar (*XSS/CORS Awareness*), **`React.lazy` & `Suspense`**, serta Memoisasi Terukur `[3]; [5]` | — |
| **15** | **`Sub-CPMK-4.2`:** Mengaudit dan mengoptimasi **Core Web Vitals** (*LCP, INP, CLS*), gambar modern (`WebP/AVIF`, `loading="lazy"`), SEO/Meta dasar, hingga terverifikasi **Google Lighthouse $\ge 85$** [C5] | 4.2.2 Ketepatan mendiagnosis penghambat **LCP, INP,** dan **CLS** pada mode *Production Build / Deployed URL* serta mengoptimasi aset, *font*, kontras, dan atribut semantik hingga skor **Lighthouse** (*Performance, Accessibility, Best Practices, SEO*) mencapai **$\ge 85$**. | **Kriteria:** Bukti audit *Lighthouse Production Mode* mencapai **$\ge 85$** secara konsisten.<br>**Teknik:** Klinik audit *Lighthouse* silang antar-kelompok & persiapan sidang UAS. | **Workshop Audit *Lighthouse* & Klinik UAS** `[TM: 100']`<br>**Praktikum Lab 14:** Optimasi **Core Web Vitals**, *Production Build*, & Verifikasi **Lighthouse $\ge 85$** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan draf URL produksi & laporan *Before–After Lighthouse* di LMS Edlink. | **Core Web Vitals** (*LCP, INP, CLS*), Optimasi Aset (`WebP`, Dimensi Eksplisit Anti-CLS), *Production Build*, & Audit **Google Lighthouse** `[5]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C5]** | Keberhasilan integrasi aplikasi *front-end* **React SPA** dengan **RESTful API** eksternal secara terverifikasi serta pembuktian optimasi performa muat mencapai **Lighthouse score $\ge 85$** pada pengujian langsung. | **Kriteria:** **Rubrik Analitik UAS (`K-2`)**.<br>**Teknik:** Penilaian Aplikasi Produksi & Laporan Optimasi *Before–After Lighthouse* (50% UAS) + Sidang Audit *Lighthouse* Langsung & *Live Code Modification* Individu (50% UAS). | **Sidang Demo Aplikasi Web, Audit *Lighthouse* Langsung, & Uji Kode Individu**<br>`[150 menit]` | Pengarsipan repositori, laporan *Lighthouse*, & rekap nilai `CPL-08` dan `CPL-13` pada portal OBE. | Integrasi Komprehensif **React SPA + RESTful API Eksternal** & Verifikasi Performa **Google Lighthouse $\ge 85$** | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-08` [C3])
* **Bentuk Instrumen:** Proyek Individu **Responsive & Accessible Multi-Section Web Interface** (menerjemahkan spesifikasi visual/prototipe UI menjadi kode **HTML5 semantik** murni + **CSS3 Flexbox & Grid** *mobile-first* tanpa *framework JS*, lolos *W3C Validator*, mendukung navigasi *keyboard*, dan mencapai skor awal *Lighthouse Accessibility* $\ge 90$).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Ketepatan struktur **HTML5 semantik** & validitas W3C = **25%**; (2) Penguasaan tata letak **CSS3 Flexbox & Grid** = **35%**; (3) Kualitas responsivitas lintas resolusi (*Mobile, Tablet, Desktop*) = **25%**; (4) Pemenuhan standar aksesibilitas dasar (*label, alt, contrast, focus*) = **15%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 25% · Mengukur `CPMK-2` / `CPL-08` [C3])
* **Bentuk Instrumen:** **Ujian Praktik *Live Coding* di Laboratorium** (150 menit, individu): mahasiswa membangun aplikasi katalog interaktif satu halaman menggunakan **Vanilla JavaScript ES6+** yang mengambil daftar data JSON secara asinkron dari *endpoint* lokal via **Fetch API + `async/await`**, merender kartu ke **DOM** secara aman, menyediakan fitur pencarian + filter + pengurutan *real-time* (`filter/map/sort`), menyimpan daftar favorit ke `localStorage`, dan menangani kondisi *loading/error* tanpa satu pun *uncaught error* di konsol.
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kebersihan kode **JavaScript ES6+** & pengolahan data imutabel = **30%**; (2) Ketepatan manipulasi **DOM** & *Event Handling* = **30%**; (3) Ketepatan komunikasi asinkron **Fetch API (`async/await`)** & *loading/error state* = **30%**; (4) Bebas galat konsol (*zero runtime errors*) = **10%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 25% · Mengukur `CPMK-3` / `CPL-13` [C6])
* **Bentuk Instrumen:** Proyek Pengembangan **Multi-Page React Single Page Application (SPA)** (minimal 4 rute halaman berbeda dengan **React Router**, pustaka minimal 6 *reusable UI components* ber-**Props** bersih, pengelolaan formulir terkendali & **Hooks (`useState`, `useEffect`, Custom Hook)**, serta manajemen *state* lintas-halaman menggunakan **Context API**, didemonstrasikan langsung beserta tanya-jawab kode di laboratorium).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Modularitas & *reusability* arsitektur komponen **React** = **35%**; (2) Ketepatan pengelolaan *State*, *Controlled Forms*, & **Hooks** = **30%**; (3) Fungsionalitas **React Router** & **Context API** = **25%**; (4) Kerapian struktur kode & penguasaan verifikasi kode di lab = **10%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-13` [C5])
* **Bentuk Instrumen:** **Proyek Akhir Aplikasi Front-End Terintegrasi RESTful API & Teroptimasi Produksi** (50% nilai UAS: repositori Git + URL *production build* yang terhubung penuh ke **RESTful API** eksternal + laporan perbandingan metrik **Before vs After Optimization** dengan skor **Google Lighthouse $\ge 85$**) + **Sidang Audit *Lighthouse* Langsung & Uji Modifikasi Kode Individu** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-2`):** (1) Kelengkapan & ketangguhan integrasi **RESTful API** eksternal (*CRUD/Query, Loading Skeleton, Error Handling* — `Sub-CPMK-4.1`) = **35%**; (2) Verifikasi langsung performa **Google Lighthouse $\ge 85$** & penerapan teknik optimasi (*Code Splitting, Lazy Asset, Zero CLS* — `Sub-CPMK-4.2`) = **35%**; (3) Kualitas arsitektur kode React, keamanan sisi klien, & kolaborasi Git = **15%**; (4) Ketepatan *live code modification* & tanya-jawab individu saat sidang = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Rekayasa Perangkat Lunak & Platform**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Roni Wahyu, S.Kom., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
