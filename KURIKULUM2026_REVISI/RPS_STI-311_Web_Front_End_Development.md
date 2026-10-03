# RPS STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Nomor Dokumen:** 071030.B4.5.2.RPS-STI311  
**Tanggal Penyusunan:** 30 September 2026  
**Sumber:** Template Master RPS Generator FSTI UWG (`Template_RPS_GEN_2026_20092026-SWO.docx`) — seluruh 18 tag `{{...}}` + 25 tag `[...]` terisi; data dari Dok 003/005/007/008/043.  
**Keluaran pendamping:** `DOCX/RPS_STI-311_Web_Front_End_Development.docx`

---

## HALAMAN 1 — IDENTITAS MATA KULIAH

| Atribut | Isi |
|---|---|
| Mata Kuliah (MK) | Pengembangan Web Front End (Web Front End Development) |
| Kode | STI-311 |
| Rumpun MK | Rekayasa Perangkat Lunak & Platform (Core STI) |
| Bobot (sks) | T= 2, P= 1 (Total 3 SKS, Tipe +P) |
| Semester | 3 (Ganjil) |
| Tgl Penyusunan | 30 September 2026 |
| Pengembang RPS | Tim KBK Rekayasa Perangkat Lunak & Platform |
| Koordinator RMK | Dr. Roni Wahyu, S.Kom., M.T. |
| Ketua Program Studi | [Nama Ketua Prodi SISTEKIN] |
| Matakuliah Syarat | FST-102 Algoritma dan Pemrograman |
| Dosen Pengampu | 1. [Nama Dosen Pengampu 1] (Koordinator MK)<br>2. [Nama Dosen Pengampu 2] |

## HALAMAN 2 — CAPAIAN PEMBELAJARAN (CP)

### CPL-PRODI yang Dibebankan pada MK

| No | Capaian Pembelajaran Lulusan (Dok 003) |
|:--:|---|
| **P4** | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). |
| **KK5** | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (Microservices, Web/Mobile, API, SaaS, BPA). |

### Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Bloom

| No | Rumusan CPMK |
|:--:|---|
| **CPMK-1** | Mahasiswa (A) mampu membangun struktur halaman web responsif multi-device (B) menggunakan HTML5 Semantik, CSS3 Flexbox/Grid, dan Variabel CSS (C) dengan tampilan estetik (D). [C3] |
| **CPMK-2** | Mahasiswa (A) mampu mengimplementasikan logika interaktivitas client-side (B) menggunakan JavaScript Modern (ES6+, DOM Manipulation, Async/Await, Fetch API) (C) secara modular (D). [C3] |
| **CPMK-3** | Mahasiswa (A) mampu membangun aplikasi Single Page Application (SPA) berbasis komponen (B) menggunakan framework React.js (Hooks, Context API, React Router) (C) dengan arsitektur state terpusat (D). [C6] |
| **CPMK-4** | Mahasiswa (A) mampu mengintegrasikan aplikasi front-end dengan RESTful API eksternal (B) serta mengoptimalkan performa loading (C) dengan skor Google Lighthouse ≥ 85 (D). [C5] |

### Tahapan Belajar (Sub-CPMK)

| No | Sub-CPMK |
|:--:|---|
| **Sub-CPMK-1.1** | Membangun struktur halaman web responsif menggunakan HTML5 semantik. (C3) |
| **Sub-CPMK-1.2** | Mengimplementasikan tata letak responsif menggunakan CSS3 Flexbox, Grid, dan variabel CSS. (C3) |
| **Sub-CPMK-2.1** | Mengimplementasikan interaktivitas client-side menggunakan JavaScript ES6+ (DOM, Async/Await). (C3) |
| **Sub-CPMK-2.2** | Mengelola state dan komunikasi data menggunakan Fetch API secara modular. (C3) |
| **Sub-CPMK-3.1** | Membangun Single Page Application berbasis komponen menggunakan React (Hooks, Context API). (C6) |
| **Sub-CPMK-3.2** | Mengimplementasikan routing antar halaman pada aplikasi SPA. (C6) |
| **Sub-CPMK-4.1** | Mengintegrasikan front-end dengan RESTful API eksternal. (C5) |
| **Sub-CPMK-4.2** | Mengoptimalkan performa loading aplikasi dengan skor Google Lighthouse minimal 85. (C5) |

### Korelasi CPL terhadap CPMK

| CPL | CPMK-1 | CPMK-2 | CPMK-3 | CPMK-4 | Instrumen & Bobot Asesmen |
|:--:|:--:|:--:|:--:|:--:|:--:|
| P4 | ✓ | ✓ |   |   | Tugas 1 (20%) + UTS (25%) = 45% |
| KK5 |   |   | ✓ | ✓ | Tugas 2 (25%) + UAS (30%) = 55% |

Skema 4x Titik Evaluasi Baku (Dok 008): Tugas 1 Pekan 4 (20%), UTS Pekan 8 (25%), Tugas 2 Pekan 12 (25%), UAS Pekan 16 (30%) — total 100%.

### Deskripsi Singkat MK

Pengembangan Web Front End (STI-311) adalah mata kuliah wajib Core STI pada Semester 3 yang membekali mahasiswa dengan kemampuan membangun antarmuka web modern, responsif, dan interaktif. Mahasiswa membangun struktur halaman semantik dengan HTML5, tata letak responsif multi-device dengan CSS3 (Flexbox, Grid, variabel CSS), serta logika interaktivitas client-side dengan JavaScript modern (ES6+, DOM Manipulation, Async/Await, Fetch API). Pembelajaran berlanjut ke pembangunan Single Page Application (SPA) berbasis komponen menggunakan React.js — Hooks, Context API untuk state global, dan React Router untuk navigasi client-side — hingga integrasi dengan RESTful API eksternal, manajemen form kompleks (React Hook Form & Zod), optimasi performa berbasis Google Lighthouse (skor minimal 85), dan deployment ke platform cloud (Vercel/Netlify). Pembelajaran menekankan praktikum dan project-based learning melalui milestone proyek SPA berkesinambungan. Sesuai Boundary Guardrails Dok 043, mata kuliah ini menyerahkan penyediaan data backend API kepada STI-416 Web Back End Development.

### Bahan Kajian: Materi Pembelajaran

1. BK-IS12 Web and Mobile Application Development — pemrograman web sisi klien (client-side), arsitektur web client-server, UI responsif, dan SPA.

2. BK-IT04 Platform Technologies — platform web modern, tooling front-end, build & deployment cloud (Vercel/Netlify).

Pokok Bahasan: (1) Pengantar Web Frontend & arsitektur client-server; (2) Semantic HTML5 & DOM; (3) CSS3 Modern: Box Model, Flexbox, Media Queries, CSS Tokens; (4) CSS Grid System & Responsive Dashboard; (5) JavaScript ES6+: Scope, Closure, Modules; (6) DOM Manipulation, Event Handling & Form Validation; (7) Asynchronous JavaScript: Promises, Async/Await, Fetch API; (8) React.js: JSX, Virtual DOM, Components, Props; (9) React Hooks: useState, useEffect, useRef; (10) Global State: Context API & Custom Hooks; (11) React Router v6: Dynamic & Protected Routes; (12) REST API Integration: Axios, Loading Skeletons, Error Boundary; (13) React Hook Form & Validasi Skema Zod; (14) Web Performance: Code Splitting, Lazy Loading, Lighthouse; (15) Production Build & Cloud Deployment.

### Pustaka

**Utama:**

1. Duckett, J. (2011). HTML and CSS: Design and Build Websites. Indianapolis: John Wiley & Sons.
2. Robbins, J. N. (2018). Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, and Web Graphics (5th ed.). Sebastopol: O'Reilly Media.
3. Banks, A., & Porcello, E. (2020). Learning React: Modern Patterns for Developing React Apps (2nd ed.). Sebastopol: O'Reilly Media.
4. MDN Web Docs (2024). MDN Web Docs — Resources for Developers. https://developer.mozilla.org
5. React Team (2024). React — The Library for Web and Native User Interfaces. https://react.dev

**Pendukung:**

1. Grant, K. (2018). CSS in Depth. Shelter Island: Manning Publications.
2. Haverbeke, M. (2018). Eloquent JavaScript: A Modern Introduction to Programming (3rd ed.). San Francisco: No Starch Press. https://eloquentjavascript.net
3. React Router Team (2024). React Router Documentation. https://reactrouter.com
4. Hookform (2024). React Hook Form Documentation. https://react-hook-form.com
5. Zod (2024). Zod — TypeScript-first Schema Validation. https://zod.dev
6. Google Chrome Team (2024). Lighthouse — Performance Auditing. https://developer.chrome.com/docs/lighthouse
7. Vercel (2024). Vercel Documentation. https://vercel.com/docs

---

## HALAMAN 3-4 — RENCANA PEMBELAJARAN 16 PEKAN

| Mg ke- | Kemampuan Akhir Tahapan Belajar (Sub-CPMK) | Indikator | Kriteria & Teknik | Luring (offline) | Daring (online) | Materi Pembelajaran [Pustaka] | Bobot Penilaian (%) |
|:--:|---|---|---|---|---|---|:--:|
| 1 | Pengantar MK & Orientasi — Sub-CPMK-1.1: Mampu menguraikan arsitektur web client-server dan Semantic HTML5 (C2) | Diagram arsitektur client-server benar; halaman HTML5 semantik lolos validator W3C | Checklist praktikum formatif; observasi lab | Kuliah Interaktif 100'; Lab Setup & Praktikum 170' | Edlink: modul pengantar & kontrak belajar; GitHub Classroom: setup repo | Pengantar Web Frontend, Protokol HTTP, DOM, Semantic HTML5 [1][4] | — |
| 2 | Sub-CPMK-1.2: Mampu merancang layout responsif via CSS Flexbox dan Media Queries (C3) | Layout multi-kolom adaptif pada ≥ 3 breakpoint (mobile/tablet/desktop) | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: video tutorial CSS; commit repo mingguan | CSS3 Modern: Box Model, Flexbox, Media Queries, CSS Tokens [1][2] | — |
| 3 | Sub-CPMK-1.2: Mampu merancang grid kompleks multi-layar dengan CSS Grid System (C3) | Dashboard responsif grid 12-kolom berfungsi di multi-layar | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: contoh kasus dashboard; forum diskusi | Advanced Layout: CSS Grid System & Responsive Dashboard Layout [1][2] | — |
| 4 | Sub-CPMK-2.1: Mampu menerapkan sintaks ES6+: Arrow Functions, Destructuring, Modules (C3) | Skrip JS modular memakai fitur ES6+ tanpa error console | Rubrik analitik Tugas 1; penilaian milestone proyek | Kuliah 100'; Lab Hands-on 170' | Edlink: kuis sintaks; pengumpulan Tugas 1 via Edlink | JavaScript Modern: ES6+ Features, Scope, Closure, Modules [3][4] | Tugas 1: 20% (Milestone Proyek 1 — evaluasi Sub-CPMK Pekan 2–3) |
| 5 | Sub-CPMK-2.1: Mampu memanipulasi DOM secara dinamis dan menangani event interaktif (C3) | Aplikasi interaktif (to-do) berfungsi: manipulasi DOM, event, validasi form client-side | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: starter code; GitHub Classroom: latihan DOM | DOM Manipulation, Event Handling, Form Validation Client-Side [3][4] | — |
| 6 | Sub-CPMK-2.2: Mampu menangani operasi asinkron via Promises dan Async/Await (C3) | Aplikasi konsumsi API publik menampilkan data tanpa blocking UI; error fetch tertangani | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: studi kasus API publik; forum troubleshooting | Asynchronous JavaScript: Promises, Async/Await, Fetch API [3][4] | — |
| 7 | Sub-CPMK-3.1: Mampu merancang komponen antarmuka modular dalam React.js (C3) | UI tersusun ≥ 5 functional components dengan aliran props yang benar | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: modul React dasar; repo proyek SPA dimulai | Pengantar React.js: JSX, Virtual DOM, Functional Components, Props [5][6] | — |
| **8** | Evaluasi Tengah Semester (UTS) — Ujian Koding Terjadwal: Responsive Layout CSS Grid & JavaScript ES6+ (CPMK-1 s.d. CPMK-3) | Indikator: Skor ujian praktik ≥ 70; solusi responsive layout + skrip ES6+ berjalan tanpa error.<br>Kriteria & Teknik: Rubrik analitik UTS; ujian praktik live coding (170').<br>Luring: Live Coding Lab Test (170').<br>Daring: Edlink — pengumuman ruang ujian & unggah berkas.<br>Materi: Cakupan Mg 1–7 — HTML5, CSS3 Flexbox/Grid, JavaScript ES6+ [1][2][3].<br>Bobot Penilaian: UTS 25%. | UTS 25% |
| 9 | Sub-CPMK-3.1: Mampu mengelola state lokal komponen via React Hook useState & useEffect (C3) | Komponen stateful bereaksi benar terhadap perubahan data (re-render tepat) | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: modul React Hooks; commit repo proyek | React Hooks Fundamental: useState, useEffect, useRef [5][6] | — |
| 10 | Sub-CPMK-3.1: Mampu mengelola state global lintas komponen via Context API (C4) | State global (tema/otentikasi) terbagi lintas ≥ 3 komponen tanpa prop drilling | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: studi kasus state global; forum diskusi | Global State Management: Context API & Custom Hooks [5][6] | — |
| 11 | Sub-CPMK-3.2: Mampu mengonfigurasi navigasi SPA via React Router (C3) | Rute multi-halaman, dynamic route, dan protected route berfungsi | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: modul routing; repo proyek diperbarui | Client-Side Routing: React Router v6, Dynamic & Protected Routes [6][7] | — |
| 12 | Sub-CPMK-4.1: Mampu mengonsumsi REST API backend, menangani loading & error state (C4) | SPA terintegrasi API eksternal: loading skeleton & error boundary berfungsi | Rubrik analitik Tugas 2; penilaian milestone integrasi sistem | Case Method 100'; Lab Coding 170' | Edlink: spesifikasi milestone; pengumpulan Tugas 2 | REST API Integration: Axios, Loading Skeletons, Error Boundary [5][6] | Tugas 2: 25% (Milestone Proyek 2 — evaluasi Sub-CPMK Pekan 9–11) |
| 13 | Sub-CPMK-4.1: Mampu mengelola form kompleks menggunakan React Hook Form & Zod (C4) | Form multi-field tervalidasi skema Zod; pesan error aksesibel | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: dokumentasi RHF & Zod; konsultasi proyek | Form Management: React Hook Form & Validasi Skema Zod [5][8] | — |
| 14 | Sub-CPMK-4.2: Mampu mengoptimalkan performa web SPA dan audit Google Lighthouse (C5) | Skor Lighthouse Performance ≥ 85 pada build produksi | Rubrik kompilasi audit Lighthouse | Case Method Workshop 270' | Edlink: laporan audit performa; forum optimasi | Web Performance Optimization: Code Splitting, Lazy Loading, Lighthouse [4][9] | — |
| 15 | Sub-CPMK-4.2: Mampu mendeploy aplikasi SPA ke platform cloud Vercel/Netlify (C4) | URL produksi aktif; pipeline build otomatis dari repo GitHub | Rubrik kompilasi deployment; verifikasi URL produksi | PjBL Studio 270' | Edlink: panduan deploy; submission URL produksi | Production Build & Cloud Deployment (Vercel/Netlify/GitHub Actions) [9][10] | — |
| **16** | Evaluasi Akhir Semester (UAS) — Sidang Demonstrasi Produk Aplikasi Web Single Page Application / SPA (Seluruh CPMK) | Indikator: Produk SPA terdeploy dan terintegrasi API; skor demo & portofolio ≥ 70.<br>Kriteria & Teknik: Rubrik analitik UAS; Demo Day & defense (170').<br>Luring: Sidang demonstrasi produk SPA.<br>Daring: Edlink — berkas final proyek & tautan deploy.<br>Materi: Cakupan seluruh Sub-CPMK — SPA React terintegrasi, optimal, terdeploy [5][6][9].<br>Bobot Penilaian: UAS 30%. | UAS 30% |
| | **Total bobot penilaian** | | | | | | **100%** |

---

## LAMPIRAN — INSTRUMEN ASESMEN

TUGAS 1 — MILESTONE PROYEK 1: HALAMAN WEB RESPONSIF MULTI-DEVICE (Pekan 4, Bobot 20%)

Mahasiswa membangun satu halaman web (landing/dashboard) responsif multi-device menggunakan Semantic HTML5 dan CSS3 modern (Flexbox, Grid, Variabel CSS) tanpa framework CSS wajib.

Spesifikasi wajib: (1) struktur semantic minimal 5 area (header, nav, main, section, footer) dan lolos validator W3C; (2) layout dashboard responsif berbasis CSS Grid 12-kolom dengan minimal 3 breakpoint (mobile ≤ 640px, tablet ≤ 1024px, desktop); (3) komponen kartu/daftar menggunakan Flexbox; (4) theming via CSS custom properties; (5) aksesibilitas dasar (alt text, kontras, label form).

Deliverable: repository GitHub + halaman live (GitHub Pages) + laporan singkat 1–2 halaman (keputusan layout, breakpoint, screenshot 3 viewport). Penilaian menggunakan rubrik analitik berikut; cakupan Sub-CPMK-1.1 & 1.2 (CPMK-1 → CPL P4).

**Rubrik Penilaian Tugas 1 (Total 100)**

| Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (66–75) | Kurang (56–65) | Sangat Kurang (0–55) |
|---|---|---|---|---|---|---|
| Semantic HTML5 & Validitas W3C | 20% | Struktur semantic lengkap & valid | Semantic tepat, 1–2 warning | Semantic dasar, beberapa error | Banyak div/span tanpa makna | Tidak semantic & tidak valid |
| Layout Flexbox | 20% | Komponen fleksibel rapi di semua ukuran | Flexbox tepat, minor misalignment | Flexbox dasar berfungsi | Layout sering bergeser | Tidak menggunakan Flexbox |
| CSS Grid & Responsive 3 Breakpoint | 25% | Grid 12-kolom adaptif sempurna | Grid benar, 1 breakpoint kurang | Grid dasar berfungsi | Responsif tidak konsisten | Tidak responsif |
| Kualitas Kode & Organisasi CSS | 15% | CSS terstruktur, custom properties rapi | Terstruktur, minor duplikasi | Dapat dipahami | Berantakan | Tidak terstruktur |
| Aksesibilitas Dasar | 10% | Alt, kontras, label lengkap | 1–2 temuan aksesibilitas | Sebagian terpenuhi | Banyak temuan | Tidak diperhatikan |
| Dokumentasi & Deployment | 10% | Repo rapi + live + laporan lengkap | Repo & live ada, laporan singkat | Repo ada | Hanya repo tanpa laporan | Tidak ada deliverable |

UJIAN TENGAH SEMESTER (Pekan 8, Bobot 25%) — UJIAN PRAKTIK LIVE CODING (170 MENIT)

Studi kasus: membangun halaman dashboard responsif dan aplikasi interaktif kecil dalam satu proyek. Cakupan: Mg 1–7 (CPMK-1 s.d. CPMK-3 fase awal).

Soal: (1) Bangun layout dashboard CSS Grid 12-kolom responsif (3 breakpoint) sesuai mockup yang diberikan; (2) implementasi fitur interaktif menggunakan JavaScript ES6+ modul (arrow function, destructuring, import/export): manipulasi DOM, event handling, dan validasi form client-side; (3) konsumsi satu REST API publik menggunakan Fetch API dengan Async/Await lengkap dengan penanganan error dan loading state sederhana.

Ketentuan: open documentation resmi (MDN/react.dev), dilarang kolaborasi dan AI code generator; submit repository GitHub pribadi pada akhir sesi. Kriteria ketuntasan minimal skor 70.

**Rubrik Penilaian UTS (Total 100)**

| Kriteria | Bobot | Poin Penuh | Poin Sebagian | Poin Minimal | Tidak Ada |
|---|---|---|---|---|---|
| Responsive Layout CSS Grid (3 breakpoint) | 30% | 30 | 20 | 10 | 0 |
| JavaScript ES6+ & Modularitas | 25% | 25 | 17 | 9 | 0 |
| DOM Manipulation & Event Handling | 15% | 15 | 10 | 5 | 0 |
| Async/Await, Fetch API & Error Handling | 20% | 20 | 13 | 7 | 0 |
| Kualitas Kode & Organisasi | 10% | 10 | 7 | 4 | 0 |

TUGAS 2 — MILESTONE PROYEK 2: SPA REACT TERINTEGRASI REST API (Pekan 12, Bobot 25%)

Melanjutkan proyek SPA dari Pekan 7, mahasiswa menambahkan: (1) state lokal dengan useState/useEffect dan state global dengan Context API + custom hooks (tanpa prop drilling); (2) navigasi multi-halaman React Router v6 termasuk dynamic route dan protected route; (3) integrasi REST API eksternal menggunakan Axios dengan loading skeleton dan error boundary; (4) satu form kompleks dengan React Hook Form + validasi skema Zod.

Deliverable: repository GitHub + deployment preview (Vercel/Netlify) + demo video maksimal 5 menit. Cakupan evaluasi: Sub-CPMK-3.1, 3.2, dan 4.1 (Pekan 9–11) → CPMK-3 (KK5) dan CPMK-4 (KK5). Penilaian menggunakan rubrik analitik berikut.

**Rubrik Penilaian Tugas 2 (Total 100)**

| Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (66–75) | Kurang (56–65) | Sangat Kurang (0–55) |
|---|---|---|---|---|---|---|
| Arsitektur Komponen React | 20% | Komposisi komponen bersih & reusable | Komponen tepat, minor duplikasi | Komponen dasar berfungsi | Komponen monolitik | Tidak berbasis komponen |
| State Management (Hooks & Context) | 25% | State global tepat tanpa prop drilling | Context benar, minor re-render | State lokal berfungsi | State tersebar tak terkelola | Tidak ada manajemen state |
| Routing SPA (Dynamic & Protected) | 15% | Semua rute + guard berfungsi | Rute lengkap, guard sebagian | Rute dasar berfungsi | Rute tidak konsisten | Tanpa routing |
| Integrasi REST API & UX State | 25% | Loading skeleton & error boundary sempurna | Integrasi benar, 1 UX state kurang | Integrasi dasar berfungsi | Error tidak tertangani | Tidak terintegrasi |
| Kualitas Kode & Deployment | 15% | Kode bersih + preview aktif | Kode baik, deploy ada isu minor | Deploy aktif | Deploy gagal | Tidak deploy |

UJIAN AKHIR SEMESTER (Pekan 16, Bobot 30%) — SIDANG DEMONSTRASI PRODUK SPA (DEMO DAY & DEFENSE, 170 MENIT)

Mahasiswa (individu/kelompok kecil) mempresentasikan produk akhir SPA hasil pengembangan berkesinambungan Mg 4–15: aplikasi Single Page Application React lengkap — komponen modular, state global Context API, routing protected, integrasi REST API, form tervalidasi Zod, skor Google Lighthouse ≥ 85, dan terdeploy di Vercel/Netlify.

Format sidang: demo live 15 menit (alur utama aplikasi, penanganan error, performa) + tanya jawab 5 menit. Deliverable akhir: URL produksi aktif, repository GitHub, slide presentasi, dan write-up portofolio 2–3 halaman (arsitektur, keputusan teknis, hasil audit Lighthouse). Kriteria ketuntasan minimal skor 70.

**Rubrik Penilaian UAS (Total 100)**

| Kriteria | Bobot | Poin |
|---|---|---|
| Fungsionalitas SPA & kelengkapan fitur | 25% | 25 |
| Integrasi REST API & penanganan data | 20% | 20 |
| Performa (Lighthouse ≥ 85) | 15% | 15 |
| Manajemen form & validasi (Zod) | 10% | 10 |
| Deployment produksi aktif | 10% | 10 |
| Presentasi & defense | 15% | 15 |
| Kualitas kode & struktur proyek | 5% | 5 |

---

## PENGESAHAN

| Memvalidasi, Unit Penjaminan Mutu FSTI | Malang, 30 September 2026 — Dosen Pengampu |
|---|---|
| Nama Pejabat UPM: [Nama Kepala UPM FSTI] | [Nama Dosen Pengampu STI-311] / NUPTK. [NUPTK Dosen] |

Mengesahkan, Ketua Program Studi Sistem dan Teknologi Informasi: [Nama Ketua Prodi SISTEKIN]

---

*RPS STI-311 dibangkitkan dari Template Master RPS Generator FSTI UWG oleh `_tools/generate_rps_sti311_docx.py` — unit pilot ke-2 RPS Batch Generator (setelah STI-416 V2).*
