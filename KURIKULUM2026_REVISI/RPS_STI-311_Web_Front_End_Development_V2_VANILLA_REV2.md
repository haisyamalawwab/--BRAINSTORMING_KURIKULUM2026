# RPS STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*) — V2 VANILLA

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Nomor Dokumen:** 071030.B4.5.2.RPS-STI311  
**Tanggal Penyusunan:** 2 Oktober 2026  
**Sumber:** Template Master RPS Generator FSTI UWG (`Template_RPS_GEN_2026_20092026-SWO.docx`) — seluruh 18 tag `{{...}}` + 25 tag `[...]` terisi. **V2 VANILLA (downgrade terarah):** tanpa framework React — SPA dibangun dengan Vanilla JavaScript; API hanya dikonsumsi dari API publik yang endpoint & dokumentasinya tersedia. CPMK-1/2 & Sub-CPMK 1.x/2.x/4.2 verbatim Dok 043/007; CPMK-3, Sub-CPMK 3.1/3.2/4.1 adalah **deviasi terarah** dari Dok 043/007 (menunggu ratifikasi Tim Kurikulum). Jangkar CPL `KK5 (SPA)` tetap terampu via SPA vanilla.  
**Keluaran pendamping:** `DOCX/RPS_STI-311_Web_Front_End_Development_V2_VANILLA.docx`

---

## HALAMAN 1 — IDENTITAS MATA KULIAH

| Atribut | Isi |
|---|---|
| Mata Kuliah (MK) | Pengembangan Web Front End (Web Front End Development) |
| Kode | STI-311 |
| Rumpun MK | Rekayasa Perangkat Lunak & Platform (Core STI) |
| Bobot (sks) | T= 2, P= 1 (Total 3 SKS, Tipe +P) |
| Semester | 3 (Ganjil) |
| Tgl Penyusunan | 2 Oktober 2026 |
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
| **CPMK-3** | Mahasiswa (A) mampu membangun aplikasi Single Page Application (SPA) berbasis komponen fungsi (B) menggunakan Vanilla JavaScript (modul ES6+, pola Store & Pub/Sub untuk state terpusat, Hash Router/History API untuk routing) (C) tanpa framework (D). [C6] |
| **CPMK-4** | Mahasiswa (A) mampu mengintegrasikan aplikasi front-end dengan RESTful API publik eksternal yang endpoint dan dokumentasinya tersedia (B) serta mengoptimalkan performa loading (C) dengan skor Google Lighthouse ≥ 85 (D). [C5] |

### Tahapan Belajar (Sub-CPMK)

| No | Sub-CPMK |
|:--:|---|
| **Sub-CPMK-1.1** | Membangun struktur halaman web responsif menggunakan HTML5 semantik. (C3) |
| **Sub-CPMK-1.2** | Mengimplementasikan tata letak responsif menggunakan CSS3 Flexbox, Grid, dan variabel CSS. (C3) |
| **Sub-CPMK-2.1** | Mengimplementasikan interaktivitas client-side menggunakan JavaScript ES6+ (DOM, Async/Await). (C3) |
| **Sub-CPMK-2.2** | Mengelola state dan komunikasi data menggunakan Fetch API secara modular. (C3) |
| **Sub-CPMK-3.1** | Membangun Single Page Application berbasis komponen fungsi dengan Vanilla JavaScript (render terkontrol, state terpusat pola Store). (C6) |
| **Sub-CPMK-3.2** | Mengimplementasikan routing antar halaman SPA menggunakan Hash Router / History API. (C6) |
| **Sub-CPMK-4.1** | Mengonsumsi RESTful API publik terdokumentasi dengan penanganan loading dan error state. (C5) |
| **Sub-CPMK-4.2** | Mengoptimalkan performa loading aplikasi dengan skor Google Lighthouse minimal 85. (C5) |

### Korelasi CPL terhadap CPMK

| CPL | CPMK-1 | CPMK-2 | CPMK-3 | CPMK-4 | Instrumen & Bobot Asesmen |
|:--:|:--:|:--:|:--:|:--:|:--:|
| P4 | ✓ | ✓ |   |   | Tugas 1 (20%) + UTS (25%) = 45% |
| KK5 |   |   | ✓ | ✓ | Tugas 2 (25%) + UAS (30%) = 55% |

Skema 4x Titik Evaluasi Baku (Dok 008): Tugas 1 Pekan 4 (20%), UTS Pekan 8 (25%), Tugas 2 Pekan 12 (25%), UAS Pekan 16 (30%) — total 100%.

### Deskripsi Singkat MK

Pengembangan Web Front End (STI-311) adalah mata kuliah wajib Core STI pada Semester 3 yang membekali mahasiswa dengan kemampuan membangun antarmuka web modern, responsif, aksesibel, dan interaktif tanpa framework, dengan porsi terbesar pada pendalaman HTML5 dan CSS3 sesuai jangkar BoK BK-IS12 & BK-IT04. Mahasiswa membangun struktur halaman semantik dengan HTML5 secara mendalam — metadata & SEO dasar, media & gambar responsif (picture/srcset, lazy loading), forms, serta aksesibilitas (WCAG dasar & ARIA) — lalu menata layout responsif multi-device dengan CSS3 modern secara bertahap: Box Model, unit & fungsi, Custom Properties, Flexbox & Media Queries, Grid System untuk dashboard, hingga transisi/animasi halus. Logika interaktivitas dibangun dengan Vanilla JavaScript modern (ES6+, DOM & Event, Async/Await, Fetch API), berlanjut ke Single Page Application (SPA) berbasis komponen fungsi — state Store & Pub/Sub serta Hash Router/History API — dan konsumsi RESTful API publik yang endpoint dan dokumentasinya sudah tersedia (mahasiswa tidak membangun API), form dengan Constraint Validation API, optimasi performa Google Lighthouse (skor minimal 85), dan deployment ke platform cloud (GitHub Pages/Vercel/Netlify). Pembelajaran menekankan praktikum dan project-based learning melalui milestone proyek SPA berkesinambungan. Sesuai Boundary Guardrails Dok 043, mata kuliah ini menyerahkan penyediaan data backend API kepada STI-416 Web Back End Development.

### Bahan Kajian: Materi Pembelajaran

1. BK-IS12 Web and Mobile Application Development — fondasi web front-end: HTML5 semantik, media & forms, aksesibilitas, UI responsif CSS3, client-side scripting, dan SPA.

2. BK-IT04 Platform Technologies — platform web modern, tooling front-end, build & deployment cloud (GitHub Pages/Vercel/Netlify).

Pokok Bahasan: (1) Pengantar Web Frontend & arsitektur client-server; (2) Semantic HTML5: Struktur Dokumen, Metadata & SEO Dasar; (3) HTML5 Media & Gambar Responsif: Audio/Video, picture/srcset, Lazy Loading; (4) HTML5 Forms & Aksesibilitas: Input Types, WCAG Dasar, ARIA; (5) CSS3 Modern I: Box Model, Unit & Fungsi, Custom Properties & Theming; (6) CSS3 Modern II: Flexbox, Media Queries & Responsive Layout; (7) CSS3 Modern III: Grid System & Responsive Dashboard; (8) JavaScript ES6+: DOM Manipulation & Event Handling; (9) JavaScript Modular & Asynchronous: Modules, Async/Await, Fetch API; (10) SPA Vanilla: Komponen Fungsi, Template Literal & State Store; (11) Routing SPA & Konsumsi API Publik Terdokumentasi: Hash Router/History API, Fetch, Loading & Error State; (12) Form & Constraint Validation API; (13) Web Performance: Code Splitting, Lazy Loading, Lighthouse; (14) Production Build & Cloud Deployment.

### Pustaka

**Utama:**

1. Duckett, J. (2011). HTML and CSS: Design and Build Websites. Indianapolis: John Wiley & Sons.
2. Robbins, J. N. (2018). Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, and Web Graphics (5th ed.). Sebastopol: O'Reilly Media.
3. Mikowski, M. S., & Powell, J. M. (2013). Single Page Web Applications: JavaScript End-to-End. Shelter Island: Manning Publications.
4. Haverbeke, M. (2018). Eloquent JavaScript: A Modern Introduction to Programming (3rd ed.). San Francisco: No Starch Press. https://eloquentjavascript.net
5. MDN Web Docs (2024). MDN Web Docs — Resources for Developers. https://developer.mozilla.org

**Pendukung:**

1. Marcotte, E. (2018). Responsive Web Design (4th ed.). New York: A Book Apart.
2. Grant, K. (2018). CSS in Depth. Shelter Island: Manning Publications.
3. W3C (2018). Web Content Accessibility Guidelines (WCAG) 2.1. https://www.w3.org/TR/WCAG21/
4. REST Countries (2024). REST Countries — API Documentation. https://restcountries.com
5. TheMealDB (2024). TheMealDB — Open API Documentation. https://www.themealdb.com/api.php
6. Google Chrome Team (2024). Lighthouse — Performance Auditing. https://developer.chrome.com/docs/lighthouse
7. Vercel (2024). Vercel Documentation. https://vercel.com/docs

---

## HALAMAN 3-4 — RENCANA PEMBELAJARAN 16 PEKAN

| Mg ke- | Kemampuan Akhir Tahapan Belajar (Sub-CPMK) | Indikator | Kriteria & Teknik | Luring (offline) | Daring (online) | Materi Pembelajaran [Pustaka] | Bobot Penilaian (%) |
|:--:|---|---|---|---|---|---|:--:|
| 1 | Pengantar MK & Orientasi — Sub-CPMK-1.1: Mampu menguraikan arsitektur web client-server dan Semantic HTML5 (C2) | Diagram arsitektur client-server benar; halaman HTML5 semantik lolos validator W3C | Checklist praktikum formatif; observasi lab | Kuliah Interaktif 100'; Lab Setup & Praktikum 170' | Edlink: modul pengantar & kontrak belajar; GitHub Classroom: setup repo | Pengantar Web Frontend, Protokol HTTP, DOM, Semantic HTML5 [1][5] | — |
| 2 | Sub-CPMK-1.1: Mampu menyusun dokumen HTML5 semantik dengan metadata & SEO dasar (C3) | Dokumen lolos validator W3C; metadata (description, Open Graph) lengkap | Checklist praktikum formatif; observasi lab | Kuliah Interaktif 100'; Lab Praktikum 170' | Edlink: modul HTML5; GitHub Classroom: setup repo | Semantic HTML5: Struktur Dokumen, Metadata & SEO Dasar [1][5] | — |
| 3 | Sub-CPMK-1.1: Mampu menyematkan media & gambar responsif HTML5 (C3) | Gambar responsif (srcset/sizes + lazy loading) dan audio/video dengan track berfungsi | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: contoh media; forum diskusi | HTML5 Media & Gambar Responsif: picture/srcset, Lazy Loading [2][5] | — |
| 4 | Sub-CPMK-1.1: Mampu membangun form semantik & halaman aksesibel (C3) | Form dengan input types & label tepat; audit mandiri WCAG dasar & ARIA lolos | Rubrik analitik Tugas 1; penilaian milestone proyek | Kuliah 100'; Lab Hands-on 170' | Edlink: kuis HTML; pengumpulan Tugas 1 via Edlink | HTML5 Forms & Aksesibilitas: Input Types, WCAG Dasar, ARIA [1][8] | Tugas 1: 20% (Milestone Proyek 1 — evaluasi Sub-CPMK Pekan 2–3) |
| 5 | Sub-CPMK-1.2: Mampu menata dasar visual dengan Box Model, Unit & Fungsi, dan Custom Properties (C3) | Tema via custom properties; layout stabil dengan unit relatif (clamp/calc) | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: video tutorial CSS; commit repo mingguan | CSS3 Modern I: Box Model, Unit & Fungsi, Custom Properties & Theming [1][7] | — |
| 6 | Sub-CPMK-1.2: Mampu membangun layout responsif via Flexbox & Media Queries (C3) | Layout multi-kolom adaptif pada ≥ 3 breakpoint (mobile/tablet/desktop) | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: video tutorial CSS; commit repo mingguan | CSS3 Modern II: Flexbox, Media Queries & Responsive Layout [2][6] | — |
| 7 | Sub-CPMK-1.2: Mampu merancang dashboard responsif multi-layar dengan CSS Grid System (C3) | Dashboard responsif grid 12-kolom berfungsi di multi-layar | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: contoh kasus dashboard; forum diskusi | CSS3 Modern III: Grid System & Responsive Dashboard [5][7] | — |
| **8** | Evaluasi Tengah Semester (UTS) — Ujian Praktik Terjadwal: Semantic HTML5 & Responsive CSS Grid (CPMK-1) | Indikator: Skor ujian praktik ≥ 70; halaman semantik-aksesibel + dashboard responsive Grid berjalan tanpa error.<br>Kriteria & Teknik: Rubrik analitik UTS; ujian praktik live coding (170').<br>Luring: Live Coding Lab Test (170').<br>Daring: Edlink — pengumuman ruang ujian & unggah berkas.<br>Materi: Cakupan Mg 1–7 — HTML5 Semantik & Aksesibilitas, CSS3 Flexbox/Grid/Custom Properties (CPMK-1) [1][2][7].<br>Bobot Penilaian: UTS 25%. | UTS 25% |
| 9 | Sub-CPMK-2.1: Mampu membangun interaktivitas client-side dengan ES6+: DOM & Event Handling (C3) | Aplikasi interaktif (to-do) berfungsi: manipulasi DOM & event tanpa error console | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: starter code; GitHub Classroom: latihan DOM | JavaScript ES6+: DOM Manipulation & Event Handling [4][5] | — |
| 10 | Sub-CPMK-2.2: Mampu memodularisasi kode & mengonsumsi data via Fetch API (Async/Await) (C3) | Modul ES6 terpisah; konsumsi data API tanpa blocking UI; error fetch tertangani | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: studi kasus API publik; forum troubleshooting | JavaScript Modular & Asynchronous: Modules, Async/Await, Fetch API [4][5] | — |
| 11 | Sub-CPMK-3.1: Mampu membangun SPA vanilla dengan komponen fungsi, template literal & state store (C4) | Aplikasi satu halaman merender ≥ 5 komponen fungsi dari state tanpa reload | Rubrik kompilasi praktikum formatif | Case Method 100'; Lab Coding 170' | Edlink: modul SPA; repo proyek SPA dimulai | SPA Vanilla: Komponen Fungsi, Template Literal & State Store [3][5] | — |
| 12 | Sub-CPMK-3.2 & 4.1: Mampu mengonfigurasi routing SPA (Hash Router/History API) dan mengonsumsi API publik terdokumentasi (C4) | Rute multi-halaman & protected route berfungsi; loading skeleton & error state pada ≥ 2 endpoint | Rubrik analitik Tugas 2; penilaian milestone integrasi sistem | Case Method 100'; Lab Coding 170' | Edlink: spesifikasi milestone; pengumpulan Tugas 2 | Routing SPA & Konsumsi API Publik Terdokumentasi: Hash Router, History API, Fetch [3][9] | Tugas 2: 25% (Milestone Proyek 2 — evaluasi Sub-CPMK Pekan 9–11) |
| 13 | Sub-CPMK-4.1: Mampu mengelola form kompleks dengan Constraint Validation API (C4) | Form multi-field tervalidasi native; pesan error aksesibel | Rubrik kompilasi praktikum formatif | Kuliah 100'; Lab Hands-on 170' | Edlink: dokumentasi MDN form; konsultasi proyek | Form & Constraint Validation API [4][5] | — |
| 14 | Sub-CPMK-4.2: Mampu mengoptimalkan performa web SPA dan audit Google Lighthouse (C5) | Skor Lighthouse Performance ≥ 85 pada build produksi | Rubrik kompilasi audit Lighthouse | Case Method Workshop 270' | Edlink: laporan audit performa; forum optimasi | Web Performance Optimization: Code Splitting, Lazy Loading, Lighthouse [5][11] | — |
| 15 | Sub-CPMK-4.2: Mampu mendeploy aplikasi SPA ke platform cloud Vercel/Netlify (C4) | URL produksi aktif; pipeline build otomatis dari repo GitHub | Rubrik kompilasi deployment; verifikasi URL produksi | PjBL Studio 270' | Edlink: panduan deploy; submission URL produksi | Production Build & Cloud Deployment (GitHub Pages/Vercel/Netlify) [12] | — |
| **16** | Evaluasi Akhir Semester (UAS) — Sidang Demonstrasi Produk Aplikasi Web Single Page Application / SPA (Seluruh CPMK) | Indikator: Produk SPA terdeploy dan terintegrasi API publik; skor demo & portofolio ≥ 70.<br>Kriteria & Teknik: Rubrik analitik UAS; Demo Day & defense (170').<br>Luring: Sidang demonstrasi produk SPA.<br>Daring: Edlink — berkas final proyek & tautan deploy.<br>Materi: Cakupan seluruh Sub-CPMK — SPA Vanilla JavaScript terintegrasi API publik, optimal, terdeploy [3][9][12].<br>Bobot Penilaian: UAS 30%. | UAS 30% |
| | **Total bobot penilaian** | | | | | | **100%** |

---

## LAMPIRAN — INSTRUMEN ASESMEN

TUGAS 1 — MILESTONE PROYEK 1: DOKUMEN HTML5 SEMANTIK, MEDIA & AKSESIBEL (Pekan 4, Bobot 20%)

Mahasiswa membangun satu halaman web (artikel/landing) semantik, kaya media, dan aksesibel menggunakan HTML5 murni (tanpa framework CSS/JS wajib; styling dasar boleh).

Spesifikasi wajib: (1) struktur semantic minimal 5 area (header, nav, main, section, footer) dan lolos validator W3C; (2) metadata & SEO dasar (meta description, Open Graph); (3) media & gambar responsif (picture/srcset/sizes, lazy loading, audio/video dengan track); (4) form semantik dengan input types & label yang tepat; (5) aksesibilitas dasar (alt text, kontras, ARIA dasar, navigasi keyboard).

Deliverable: repository GitHub + halaman live (GitHub Pages) + laporan singkat 1–2 halaman (keputusan struktur, media, dan aksesibilitas). Penilaian menggunakan rubrik analitik berikut; cakupan Sub-CPMK-1.1 (Pekan 2–3) (CPMK-1 → CPL P4).

**Rubrik Penilaian Tugas 1 (Total 100)**

| Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (66–75) | Kurang (56–65) | Sangat Kurang (0–55) |
|---|---|---|---|---|---|---|
| Semantic HTML5 & Validitas W3C | 20% | Struktur semantic lengkap & valid | Semantic tepat, 1–2 warning | Semantic dasar, beberapa error | Banyak div/span tanpa makna | Tidak semantic & tidak valid |
| Metadata & SEO Dasar | 10% | Meta description & Open Graph lengkap | Metadata utama ada | Sebagian metadata | Metadata minim | Tanpa metadata |
| Gambar & Media Responsif (srcset, Lazy) | 20% | Semua media adaptif & optimal | srcset tepat, 1 media kurang | Media dasar berfungsi | Media tidak responsif | Tanpa penanganan media |
| Form Semantik & Input Types | 10% | Input types & label tepat di semua field | 1–2 field kurang tepat | Form dasar berfungsi | Banyak field tak semantik | Form tak semantik |
| Aksesibilitas (WCAG Dasar, ARIA, Keyboard) | 25% | Audit WCAG dasar lolos penuh | 1–2 temuan aksesibilitas | Sebagian terpenuhi | Banyak temuan | Tidak diperhatikan |
| Dokumentasi & Deployment | 15% | Repo rapi + live + laporan lengkap | Repo & live ada, laporan singkat | Repo ada | Hanya repo tanpa laporan | Tidak ada deliverable |

UJIAN TENGAH SEMESTER (Pekan 8, Bobot 25%) — UJIAN PRAKTIK LIVE CODING (170 MENIT)

Studi kasus: membangun halaman web semantik, aksesibel, dan responsif dalam satu proyek. Cakupan: Mg 1–7 — HTML5 & CSS3 (CPMK-1).

Soal: (1) bangun struktur semantik & aksesibel sesuai mockup (landmark HTML5, ARIA dasar, navigasi keyboard); (2) bangun layout dashboard CSS Grid 12-kolom responsif (3 breakpoint) dengan Custom Properties untuk theming; (3) implementasi komponen kartu Flexbox, gambar responsif (srcset/sizes + lazy loading), dan transisi/animasi halus.

Ketentuan: open documentation resmi (MDN/WCAG 2.1), dilarang kolaborasi dan AI code generator; submit repository GitHub pribadi pada akhir sesi. Kriteria ketuntasan minimal skor 70.

**Rubrik Penilaian UTS (Total 100)**

| Kriteria | Bobot | Poin Penuh | Poin Sebagian | Poin Minimal | Tidak Ada |
|---|---|---|---|---|---|
| Semantic HTML5 & Aksesibilitas (ARIA, Keyboard) | 30% | 30 | 20 | 10 | 0 |
| CSS Grid Responsive (3 breakpoint) | 30% | 30 | 20 | 10 | 0 |
| Custom Properties & Theming | 15% | 15 | 10 | 5 | 0 |
| Gambar Responsif & Media (srcset, Lazy) | 15% | 15 | 10 | 5 | 0 |
| Kualitas Kode & Organisasi CSS | 10% | 10 | 7 | 4 | 0 |

TUGAS 2 — MILESTONE PROYEK 2: SPA VANILLA JAVASCRIPT TERINTEGRASI API PUBLIK (Pekan 12, Bobot 25%)

Melanjutkan proyek SPA dari Pekan 7, mahasiswa menambahkan: (1) state lokal dengan re-render terkontrol dan state global dengan pola Store & Pub/Sub (tanpa duplikasi state); (2) navigasi multi-halaman menggunakan Hash Router / History API termasuk dynamic route dan protected route; (3) konsumsi minimal dua endpoint dari SATU API publik yang endpoint dan dokumentasinya tersedia (REST Countries, TheMealDB, atau setara — mahasiswa TIDAK membangun API) dengan loading skeleton dan error state; (4) satu form kompleks dengan Constraint Validation API.

Deliverable: repository GitHub + deployment preview (GitHub Pages/Vercel/Netlify) + demo video maksimal 5 menit. Cakupan evaluasi: Sub-CPMK-2.1, 2.2, dan 3.1 (Pekan 9–11) → CPMK-2 (P4) dan CPMK-3 (KK5). Penilaian menggunakan rubrik analitik berikut.

**Rubrik Penilaian Tugas 2 (Total 100)**

| Kriteria | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (66–75) | Kurang (56–65) | Sangat Kurang (0–55) |
|---|---|---|---|---|---|---|
| Arsitektur Komponen Vanilla & Rendering | 20% | Komposisi komponen fungsi bersih & reusable | Komponen tepat, minor duplikasi | Komponen dasar berfungsi | Kode monolitik satu berkas | Tanpa pemisahan komponen |
| State Terpusat (Store & Pub/Sub) | 25% | State global tepat tanpa duplikasi | Store benar, minor re-render berlebih | State lokal berfungsi | State tersebar tak terkelola | Tidak ada manajemen state |
| Routing SPA (Dynamic & Protected) | 15% | Semua rute + guard berfungsi | Rute lengkap, guard sebagian | Rute dasar berfungsi | Rute tidak konsisten | Tanpa routing |
| Integrasi API Publik & UX State | 25% | Loading skeleton & error state sempurna pada ≥ 2 endpoint | Integrasi benar, 1 UX state kurang | Integrasi dasar berfungsi | Error tidak tertangani | Tidak terintegrasi |
| Kualitas Kode & Deployment | 15% | Kode bersih + preview aktif | Kode baik, deploy ada isu minor | Deploy aktif | Deploy gagal | Tidak deploy |

UJIAN AKHIR SEMESTER (Pekan 16, Bobot 30%) — SIDANG DEMONSTRASI PRODUK SPA (DEMO DAY & DEFENSE, 170 MENIT)

Mahasiswa (individu/kelompok kecil) mempresentasikan produk akhir SPA Vanilla JavaScript hasil pengembangan berkesinambungan Mg 4–15: aplikasi Single Page Application berbasis komponen fungsi — state global pola Store & Pub/Sub, routing Hash Router/History API, integrasi API publik terdokumentasi, form tervalidasi Constraint Validation API, skor Google Lighthouse ≥ 85, dan terdeploy di GitHub Pages/Vercel/Netlify.

Format sidang: demo live 15 menit (alur utama aplikasi, penanganan error, performa) + tanya jawab 5 menit. Deliverable akhir: URL produksi aktif, repository GitHub, slide presentasi, dan write-up portofolio 2–3 halaman (arsitektur, keputusan teknis, hasil audit Lighthouse). Kriteria ketuntasan minimal skor 70.

**Rubrik Penilaian UAS (Total 100)**

| Kriteria | Bobot | Poin |
|---|---|---|
| Fungsionalitas SPA vanilla & kelengkapan fitur | 25% | 25 |
| Integrasi API publik & penanganan data | 20% | 20 |
| Performa (Lighthouse ≥ 85) | 15% | 15 |
| Manajemen form & validasi native | 10% | 10 |
| Deployment produksi aktif | 10% | 10 |
| Presentasi & defense | 15% | 15 |
| Kualitas kode & struktur proyek | 5% | 5 |

---

## PENGESAHAN

| Memvalidasi, Unit Penjaminan Mutu FSTI | Malang, 2 Oktober 2026 — Dosen Pengampu |
|---|---|
| Nama Pejabat UPM: [Nama Kepala UPM FSTI] | [Nama Dosen Pengampu STI-311] / NUPTK. [NUPTK Dosen] |

Mengesahkan, Ketua Program Studi Sistem dan Teknologi Informasi: [Nama Ketua Prodi SISTEKIN]

---

*RPS STI-311 V2 VANILLA dibangkitkan dari Template Master RPS Generator FSTI UWG oleh `_tools/generate_rps_sti311_v2_vanilla_docx.py` — downgrade terarah: SPA vanilla tanpa framework, konsumsi API publik terdokumentasi (bukan membangun API).*
