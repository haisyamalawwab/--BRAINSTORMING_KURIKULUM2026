# 065_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI311` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 3  
**Klaster Asesmen MK (Dok 018):** Klaster 2 (`K-2`) — Pemrograman, Algoritma, Basis Data, & Platform Web/Mobile  
**CPL Dibebankan:** `CPL-08` (`P4` = **45%**) & `CPL-13` (`KK5` = **55%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 008, 018, 043,** dan unit perintis kanonis `RPS_STI-311_Web_Front_End_Development.md`, mata kuliah berpraktikum `STI-311` (3 SKS `+P`) menggunakan skema bobot baku MK `+P` (`20% / 25% / 25% / 30%`) dengan pemetaan 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-08` / `P4`)** — *Responsive & Accessible HTML5 + CSS3 Flexbox/Grid Web Slicing*.
* **UTS (Pekan 8 — 25%) → `CPMK-2` (`CPL-08` / `P4`)** — *Live Coding Exam: JavaScript ES6+, DOM Manipulation, & Async/Await Fetch API*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-13` / `KK5`)** — *Project-Based Reusable Component React SPA (Hooks, Router, Context)*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-13` / `KK5`)** — *Project-Based RESTful API Integrated Web App + Verified Lighthouse $\ge 85$ & Live Defense*.
* **Kepatuhan IKU 7 ($\ge 70\%$ untuk Klaster `K-2` Dok 018):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75%` berbasis studi kasus implementasi dan proyek aplikasi web nyata *(persis selaras dengan tabel IKU 7 Dokumen 004 untuk `STI-311` = 75%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-08`**<br>(`P4` — 45%)<br>*Level: R* | **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | Proyek individu: Konstruksi halaman **HTML5 semantik** valid W3C berstandar aksesibilitas dasar | **RTM-1 (Tugas 1)** + Uji *W3C Validator & Lighthouse A11y* + Rubrik T1 | Sumatif | 8% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Proyek individu: Tata letak **CSS3 Flexbox & Grid** responsif adaptif lintas resolusi (*360px–1440px*) | **RTM-1 (Tugas 1)** + Uji *DevTools Responsive* + Rubrik T1 | Sumatif | 12% | |
| **`CPL-08`**<br>(`P4` — 45%)<br>*Level: R* | **`CPMK-2`**<br>(C3) | `Sub-CPMK-2.1` | Mg 8 | Ujian praktik *live coding* lab: Interaktivitas halaman dengan **JavaScript ES6+** & manipulasi **DOM** bersih | **Soal Praktik UTS** (Bagian ES6+ & DOM) + Rubrik Analitik UTS | Sumatif | 13% | **25%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian praktik *live coding* lab: Konsumsi data JSON asinkron **Fetch API & `async/await`** bebas *error* | **Soal Praktik UTS** (Bagian Async Fetch) + Rubrik Analitik UTS | Sumatif | 12% | |
| **`CPL-13`**<br>(`KK5` — 55%)<br>*Level: R* | **`CPMK-3`**<br>(C6) | `Sub-CPMK-3.1` | Mg 12 | Proyek aplikasi **React SPA**: Arsitektur komponen *reusable* (*Component, Props, State, Hooks*) | **RTM-2 (Tugas 2)** + *Code Walkthrough* Lab + Rubrik T2 | Sumatif | 14% | **25%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Proyek aplikasi **React SPA**: Navigasi multi-rute **React Router**, **Context API**, & *Custom Hook* | **RTM-2 (Tugas 2)** + Demo Lab + Rubrik Analitik T2 | Sumatif | 11% | |
| **`CPL-13`**<br>(`KK5` — 55%)<br>*Level: R* | **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1` | Mg 16 | Proyek produksi + sidang: Integrasi penuh **RESTful API** eksternal (*CRUD/Query, Loading, Error States*) | **Repositori & Live App UAS** + Uji *Network Tab* + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek produksi + sidang: Optimasi *Code Splitting & Core Web Vitals* terverifikasi **Lighthouse $\ge 85$** | **Audit Lighthouse Langsung** & Uji Modifikasi Kode + Rubrik UAS | Sumatif | 15% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN PRAKTIK

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Antarmuka Web Responsif HTML5 & CSS3)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Uji Lab **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-08`).
* **Spesifikasi Teknis Individu:**
  1. Membangun antarmuka web multi-bagian (*Hero, Feature Grid, Interactive Pricing/Schedule Table, Accessible Contact/Registration Form, & Footer*) murni menggunakan **HTML5 semantik** dan **CSS3 (*Custom Properties, Flexbox, CSS Grid, Media Queries*)** tanpa *framework* JS.
  2. Wajib lolos *W3C HTML Validator* (0 *error*), bebas *horizontal scrollbar* dari lebar `360px` hingga `1440px`, dapat dinavigasi penuh dengan tombol `Tab`, dan meraih skor awal *Lighthouse Accessibility* $\ge 90$.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: *Live Coding* JavaScript ES6+, DOM, & Fetch)
* **Format & Bobot:** Ujian Praktik *Live Coding* Terawasi di Laboratorium (**150 menit**, individu) · Bobot **25%** (`CPMK-2` → `CPL-08`).
* **Spesifikasi Soal Praktik:**
  1. Mengambil koleksi data JSON dari *endpoint* REST lokal yang disediakan penguji di jaringan lab menggunakan **Fetch API** dan **`async/await`** di dalam blok `try/catch/finally`.
  2. Menampilkan indikator *Loading* saat memuat, pesan ramah saat gagal, dan merender daftar kartu item ke **DOM** secara aman (tanpa celah `innerHTML` tidak aman).
  3. Mengimplementasikan fitur pencarian kata kunci, filter kategori, pengurutan harga/skor menggunakan metode **ES6+** (`filter`, `map`, `toSorted`), serta penyimpanan daftar item pilihan ke `localStorage` tanpa satu pun galat di *Browser Console*.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Aplikasi Single Page Application Berbasis React)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Demo & *Code Walkthrough* Lab **Pekan 12** · Bobot **25%** (`CPMK-3` → `CPL-13`).
* **Spesifikasi Teknis:**
  1. Membangun aplikasi **React SPA** minimal 4 halaman terhubung via **React Router** (*Beranda/Eksplorasi, Detail Dinamis `:id`, Formulir Tambah/Kelola Terkendali, & Halaman Favorit/Ringkasan + 404 Page*).
  2. Wajib membangun minimal 6 komponen UI *reusable* ber-**Props** bersih, menggunakan **`useState`**, **`useEffect`**, minimal 1 **Custom Hook** buatan sendiri, dan 1 **Context API** untuk *state* lintas-komponen.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Integrasi RESTful API & Optimasi Lighthouse $\ge 85$)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-13`), terdiri atas **Aplikasi Produksi & Laporan Optimasi (50% nilai UAS)** + **Sidang Audit Langsung & Uji Kode Individu (50% nilai UAS, 150 menit)**:
  1. **Integrasi RESTful API (`Sub-CPMK-4.1`):** Aplikasi React terintegrasi penuh dengan *Public REST API* atau *Mock REST Server* terstruktur (mendukung pembacaan daftar/detail parameter, mutasi data/interaksi API, *Skeleton Loading*, *Empty State*, dan penanganan galat HTTP yang rapi).
  2. **Optimasi Performa Terverifikasi (`Sub-CPMK-4.2`):** Menerapkan *Code Splitting* (`React.lazy`), optimasi gambar `WebP` berdimensi eksplisit, dan menjalankan *Production Build / Live Deployment*. Saat sidang, penguji menjalankan langsung **Google Lighthouse** (*Navigation Mode, Incognito*) dan memverifikasi skor **Performance $\ge 85$** (serta Accessibility, Best Practices, & SEO $\ge 85$), ditambah tantangan modifikasi kecil komponen/API secara langsung per anggota tim.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-311}}$)
$$NA_{\text{STI-311}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Selaras Pilot `RPS_STI-311` & Dok 004/008)
1. **Ketercapaian `CPL-08` (`P4` — bobot 45% MK dari `CPMK-1` [20%] + `CPMK-2` [25%]):**
   $$\text{Score}_{\text{CPL-08, STI-311}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,25\,S_{\text{UTS}}(i)}{0,45}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,45 = 1,35\text{ SKS}$).*
2. **Ketercapaian `CPL-13` (`KK5` — bobot 55% MK dari `CPMK-3` [25%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-13, STI-311}}(i) = \frac{0,25\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,55}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,55 = 1,65\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**.
* **Aturan Verifikasi Keaslian Kode:** Setiap mahasiswa pada proyek tim wajib memiliki jejak *commit* Git bermakna dan mampu memodifikasi komponen tanggung jawabnya secara langsung saat sidang; ketidakmampuan menjelaskan kode sendiri menggugurkan nilai individu pada komponen terkait. Remedial diberikan maksimal 1 kali dengan plafon nilai **70,0 (B)**.
