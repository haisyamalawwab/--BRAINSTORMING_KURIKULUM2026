# 065_3 — OUTLINE BUKU MODUL PEMBELAJARAN & PRAKTIKUM BERBASIS OBE
## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI311` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 3  
**CPL:** `CPL-08` (`P4` = 45%) & `CPL-13` (`KK5` = 55%) [Level `R`] · **BoK:** `BK-IS12`, `BK-IT04`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR + PRAKTIKUM

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Web Front-End Modern: HTML5 Semantik, CSS3 Responsif, JavaScript ES6+, Arsitektur React SPA, Integrasi RESTful API, & Optimasi Performa Lighthouse* |
| **Target Tebal Naskah** | 14 Bab Materi + 14 Modul Praktikum Laboratorium + 2 Unit Evaluasi ($\pm 215\text{–}250\text{ halaman}$ A4 dilengkapi diagram *DOM/Rendering Pipeline*, sandingan kode bersih ES6+ & React Hooks, serta daftar periksa audit **Lighthouse $\ge 85$**) |
| **Pagar Pembatas Buku (*Guardrail*)** | Fokus murni pada arsitektur & performa sisi klien (*client-side web engineering*); tidak membangun server *back-end*/SQL produksi (`STI-416`) dan tidak mengulang riset pengguna awal (`STI-308`). |

---

## 2. PETA KESELARASAN 14 BAB & 14 MODUL PRAKTIKUM TERHADAP CPMK & SUB-CPMK

| Bagian | Bab & Lab | Judul Bab Materi & Modul Praktikum | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>HTML5 Semantik, Aksesibilitas, & CSS3 Responsif** | **Bab 1 / Lab 1** | Arsitektur Rendering Peramban & Konstruksi Dokumen **HTML5 Semantik** Valid W3C | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2 / Lab 2** | Formulir HTML5 Aksesibel (**WCAG/ARIA**) & Fondasi **CSS3 Box Model / Design Tokens** | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | Tugas 1 (20%) |
| | **Bab 3 / Lab 3** | Tata Letak Web Modern 1D & 2D dengan **CSS3 Flexbox** dan **CSS Grid** | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | Tugas 1 (20%) |
| | **Bab 4 / Lab 4** | Desain Responsif **Mobile-First**, Gambar Adaptif, & Pengenalan *Utility-First CSS* | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>JavaScript ES6+, DOM, & Asinkroni Fetch API** | **Bab 5 / Lab 5** | Pemrograman **JavaScript Modern (ES6+)**, *ES Modules*, & Transformasi Data Imutabel | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 6 / Lab 6** | Manipulasi **DOM** Dinamis, *Event Delegation*, Mitigasi XSS, & `localStorage` | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 7 / Lab 7** | Mekanisme *Event Loop*, *Promises*, **`async/await`**, & Komunikasi **Fetch API** | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Simulasi Ujian Praktik Live Coding Interaktivitas JavaScript ES6+ & Fetch API (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (25%)* |
| **Bagian III:<br>Rekayasa Single Page Application (React)** | **Bab 8 / Lab 8** | Arsitektur **SPA**, Ekosistem *Vite*, **JSX**, *Functional Components*, & **Props** | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 9 / Lab 9** | Manajemen *State* Reaktif (**`useState`**), *Controlled Forms*, & Efek **`useEffect`** | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 10 / Lab 10** | Navigasi Multi-Halaman **React Router**, **Context API**, & Abstraksi **Custom Hooks** | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (25%) |
| | **Bab 11 / Lab 11** | Pola Komposisi Komponen *Reusable* & Struktur Repositori **React SPA** Skalabel | Mg 12 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Integrasi RESTful API & Optimasi Lighthouse** | **Bab 12 / Lab 12** | Lapisan Klien HTTP & Integrasi Penuh **RESTful API** Eksternal (*CRUD & UI States*) | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13 / Lab 13** | *Protected Routes* Sisi Klien, Keamanan Antarmuka, & **`React.lazy` Code Splitting** | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 14 / Lab 14** | Optimasi **Core Web Vitals**, Audit **Google Lighthouse $\ge 85$**, & *Handoff* ke `STI-416` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Produksi React + API & Protokol Sidang Audit Lighthouse (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB & MODUL PRAKTIKUM

#### BAB 1 & LAB 1: Arsitektur Rendering Peramban & Konstruksi Dokumen HTML5 Semantik (Pekan 1)
* **Materi & Praktikum:** Tahapan *DOM, CSSOM, Accessibility Tree, Layout, Paint*; elemen struktural **HTML5 semantik**, hierarki judul, metadata dokumen, dan pengujian *W3C Markup Validator*.

#### BAB 2 & LAB 2: Formulir HTML5 Aksesibel (WCAG/ARIA) & CSS3 Box Model / Design Tokens (Pekan 2)
* **Materi & Praktikum:** Konstruksi formulir aksesibel (`label`, tipe masukan semantik, navigasi `Tab`, rasio kontras WCAG AA), **CSS3 Box Model**, spesifisitas selektor, tipografi fluida `clamp()`, dan deklarasi *CSS Custom Properties*.

#### BAB 3 & LAB 3: Tata Letak Web Modern 1D & 2D dengan CSS3 Flexbox dan CSS Grid (Pekan 3)
* **Materi & Praktikum:** Sumbu utama/silang **Flexbox**, perataan dan distribusi ruang, matriks baris-kolom **CSS Grid** (`fr`, `minmax`, `auto-fit/auto-fill`, `grid-template-areas`), dan penggabungan harmonis keduanya.

#### BAB 4 & LAB 4: Desain Responsif Mobile-First, Gambar Adaptif, & Utility-First CSS (Pekan 4)
* **Materi & Praktikum:** Strategi `min-width` *breakpoints*, pencegahan *horizontal scroll*, atribut gambar responsif (`srcset`, `sizes`, `aspect-ratio`), serta alur kerja *Utility-First CSS* (`Tailwind CSS`).

#### BAB 5 & LAB 5: Pemrograman JavaScript Modern (ES6+), *ES Modules*, & Transformasi Data Imutabel (Pekan 5)
* **Materi & Praktikum:** Cakupan blok `let/const`, *arrow functions*, *destructuring*, *spread/rest*, *optional chaining*, pemecahan berkas *ES Modules*, dan pengolahan larik deklaratif (`map, filter, reduce, find`).

#### BAB 6 & LAB 6: Manipulasi DOM Dinamis, *Event Delegation*, Mitigasi XSS, & `localStorage` (Pekan 6)
* **Materi & Praktikum:** Pembacaan & pembuatan elemen **DOM** secara aman (menghindari *DOM XSS*), *Event Bubbling & Delegation*, pencegahan perilaku bawaan formulir, dan serialisasi JSON ke `localStorage`.

#### BAB 7 & LAB 7: Mekanisme *Event Loop*, *Promises*, `async/await`, & Komunikasi Fetch API (Pekan 7)
* **Materi & Praktikum:** Visualisasi *Call Stack & Microtask Queue*, sintaks **`async/await`**, konsumsi **Fetch API** (`GET/POST`, pemeriksaan `response.ok`), serta pengelolaan *Loading, Empty,* dan *Error State*.

#### BAB 8 & LAB 8: Arsitektur SPA, Ekosistem *Vite*, JSX, *Functional Components*, & Props (Pekan 9)
* **Materi & Praktikum:** Perbandingan arsitektur MPA vs **SPA**, mekanisme rekonsiliasi *Virtual DOM*, aturan kompilasi **JSX**, perancangan komponen *reusable* ber-**Props**, komposisi `children`, dan perenderan koleksi ber-`key`.

#### BAB 9 & LAB 9: Manajemen *State* Reaktif (`useState`), *Controlled Forms*, & Efek `useEffect` (Pekan 10)
* **Materi & Praktikum:** Pembaruan *state* objek/larik secara imutabel pada **`useState`**, pola *Controlled Inputs*, *Lifting State Up*, aturan ketat dependensi **`useEffect`**, dan pembersihan efek samping (*cleanup*).

#### BAB 10 & LAB 10: Navigasi Multi-Halaman React Router, Context API, & Custom Hooks (Pekan 11)
* **Materi & Praktikum:** Rute bersarang (`<Outlet />`), parameter dinamis, halaman 404 pada **React Router**; berbagi *state* lintas pohon komponen dengan **Context API**; serta pembuatan **Custom Hooks** yang bersih.

#### BAB 11 & LAB 11: Pola Komposisi Komponen *Reusable* & Struktur Repositori React SPA Skalabel (Pekan 12)
* **Materi & Praktikum:** Pemisahan *UI Primitives* dan *Feature Modules*, penghindaran anti-pola *redundant state*, serta audit kualitas kode proyek SPA.

#### BAB 12 & LAB 12: Lapisan Klien HTTP & Integrasi Penuh RESTful API Eksternal (Pekan 13)
* **Materi & Praktikum:** Pembuatan modul klien API terpusat dengan variabel lingkungan `.env`, integrasi siklus penuh `GET/POST/PUT/DELETE`, pencarian ber-*debounce*, paginasi, dan *Skeleton Loader*.

#### BAB 13 & LAB 13: *Protected Routes* Sisi Klien, Keamanan Antarmuka, & `React.lazy` Code Splitting (Pekan 14)
* **Materi & Praktikum:** Pembungkus rute privat, pemahaman *Same-Origin Policy & CORS*, pemecahan bundel per-rute dengan **`React.lazy` & `<Suspense>`**, serta penggunaan bijak `useMemo`/`useCallback`.

#### BAB 14 & LAB 14: Optimasi Core Web Vitals, Audit Google Lighthouse $\ge 85$, & *Handoff* ke `STI-416` (Pekan 15)
* **Materi & Praktikum:** Teknik optimasi **LCP, INP, & CLS**, format gambar modern `WebP/AVIF`, atribut `loading="lazy"` & `fetchpriority="high"`, *deployment* statis produksi, pembuktian skor **Lighthouse $\ge 85$**, dan kesiapan integrasi menuju **`STI-416 Pengembangan Web Back End`**.
