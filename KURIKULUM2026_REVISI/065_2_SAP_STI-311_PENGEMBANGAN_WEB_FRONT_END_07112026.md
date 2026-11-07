# 065_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI311` · **Bobot:** 3 SKS `+P` (`TM 100'`, `Prak 170'`, `PT 120'`, `BM 120'`) · **Semester:** 3  
**Prasyarat:** `FST-102` Algoritma dan Pemrograman · **CPL:** `CPL-08` (`P4` = 45%) & `CPL-13` (`KK5` = 55%) [Level `R`]  
**Klaster Rubrik:** `K-2` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu & Asisten Laboratorium `STI-311` |
|---|---|
| **Struktur Waktu per Sesi** | **Sesi Teori (`100'`):** Pendahuluan `15'` · Inti & *Live Coding* `70'` · Penutup `15'`<br>**Sesi Praktikum Lab (`170'`):** *Briefing* `15'` · Praktik Koding Terbimbing `135'` · Inspeksi *Browser DevTools* & *Git Commit* `20'`, diikuti `PT 120'` & `BM 120'`. |
| **Fokus Keilmuan (*In-Scope*)** | Konstruksi antarmuka klien modern: **HTML5 Semantik & Aksesibilitas**, **CSS3 Flexbox & Grid Responsif**, **JavaScript ES6+ / DOM / Fetch Async-Await**, **React SPA** (*Components, Props, State, Hooks, Router, Context*), integrasi **RESTful API** eksternal, dan optimasi **Lighthouse $\ge 85$**. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** menugaskan pembuatan server *back-end* Node.js/Express/SQL dari nol (ranah **`STI-416 Pengembangan Web Back End`** — wajib gunakan *public REST API* atau *JSON Server mock* siap pakai!) dan dilarang mengulang riset wawancara *Persona/SUS* dari nol (ranah **`STI-308 Desain & Prototyping UI/UX`**). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Teori (`100'`) & Modul Praktikum (`170'`) | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Teori: Arsitektur Browser & **HTML5 Semantik** · Lab 1: Markup Semantik & Validasi W3C | 270' | Formatif Lab |
| **2** | `Sub-CPMK-1.1, 1.2` | Teori: Formulir Aksesibel (**ARIA**) & **CSS3 Box Model** · Lab 2: Form & *Design Tokens* CSS | 270' | Formatif Lab |
| **3** | `Sub-CPMK-1.2` | Teori: **CSS3 Flexbox** & **CSS Grid** · Lab 3: Tata Letak 1D & 2D Kompleks | 270' | Formatif Lab |
| **4** | `Sub-CPMK-1.2` | Teori: **Mobile-First Responsive** & *Tailwind* · Lab 4: Verifikasi **Tugas 1** | 270' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Teori: **JavaScript ES6+** & *Array HOF* · Lab 5: Transformasi Data Imutabel & *Modules* | 270' | Formatif Lab |
| **6** | `Sub-CPMK-2.1` | Teori: Manipulasi **DOM**, *Events*, & Anti-XSS · Lab 6: Aplikasi Interaktif DOM + Storage | 270' | Formatif Lab |
| **7** | `Sub-CPMK-2.2` | Teori: *Event Loop*, **Fetch API**, & **`async/await`** · Lab 7: Konsumsi JSON API & Klinik UTS | 270' | Formatif Lab |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** *Live Coding* JavaScript ES6+, DOM, & Fetch Async/Await | 150' | **UTS (25%)** |
| **9** | `Sub-CPMK-3.1` | Teori: Arsitektur **SPA** & **React Components/Props** · Lab 8: Vite + Pustaka Komponen UI | 270' | Formatif Lab |
| **10** | `Sub-CPMK-3.1` | Teori: **React Hooks (`useState`, `useEffect`)** & Form · Lab 9: State Interaktif & Efek | 270' | Formatif Lab |
| **11** | `Sub-CPMK-3.2` | Teori: **React Router**, **Context API**, & *Custom Hooks* · Lab 10: SPA Multi-Rute | 270' | Formatif Lab |
| **12** | `Sub-CPMK-3.1, 3.2` | Teori: Pola Komposisi Komponen Skalabel · Lab 11: Demo & Bedah Kode **Tugas 2** | 270' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-4.1` | Teori: Lapisan Klien **RESTful API** & *UI States* · Lab 12: Integrasi CRUD API Eksternal | 270' | Formatif Lab |
| **14** | `Sub-CPMK-4.1, 4.2` | Teori: *Protected Routes* & **`React.lazy` Splitting** · Lab 13: Route Guard & Optimasi Bundle | 270' | Formatif Lab |
| **15** | `Sub-CPMK-4.2` | Teori: **Core Web Vitals** & Audit **Lighthouse** · Lab 14: Optimasi Performa $\ge 85$ | 270' | Formatif Lab |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Aplikasi React + API & Audit *Lighthouse* Langsung | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (TEORI + PRAKTIKUM)

### PERTEMUAN 1 — Arsitektur Browser & Konstruksi **HTML5 Semantik**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C2→C3] · **Alat:** *VS Code*, Chrome/Firefox *DevTools*, *W3C Markup Validation Service*.
* **Sesi Teori (`100'`):** Menguraikan alur *Critical Rendering Path* peramban (*HTML → DOM, CSS → CSSOM, Render Tree, Layout, Paint*) dan mengapa penggunaan tag **HTML5 semantik** (`header, nav, main, article, section, aside, footer, figure`) krusial bagi pembaca layar (*Accessibility Tree*) maupun mesin pencari dibanding tumpukan `<div>`.
* **Sesi Praktikum Lab 1 (`170'`):** Menyiapkan repositori Git dan menyusun halaman portal akademik utuh dengan HTML5 semantik murni hingga 100% lolos *W3C Validator* tanpa peringatan.
* **PT (`120'`) & BM (`120'`):** Memperbaiki berkas latihan *div-soup* menjadi struktur HTML5 semantik bersih.

### PERTEMUAN 2 — Formulir HTML5 Aksesibel (**WCAG/ARIA**) & **CSS3 Box Model / Design Tokens**
* **Sub-CPMK:** `Sub-CPMK-1.1` & `1.2` [C3] · **Alat:** *Chrome Lighthouse Accessibility Panel*, *CSS Variables*.
* **Sesi Teori (`100'`):** Membahas pembuatan formulir web yang ramah *keyboard* & pembaca layar (`<label>`, `<fieldset>`, validasi bawaan, atribut `aria-live`/`aria-invalid` seperlunya), dilanjutkan aturan emas **CSS3** (`box-sizing: border-box`, perhitungan spesifisitas selektor, satuan relatif `rem`/`em`/`clamp()`, dan penerjemahan palet `STI-308` ke `:root` *CSS Custom Properties*).
* **Sesi Praktikum Lab 2 (`170'`):** Membangun halaman pendaftaran aksesibel bertoken CSS dan memverifikasi navigasi penuh tanpa tetikus (*keyboard-only test*).
* **PT (`120'`) & BM (`120'`):** Merancang berkas `tokens.css` standar untuk proyek Tugas 1.

### PERTEMUAN 3 — Tata Letak Modern: **CSS3 Flexbox** & **CSS Grid**
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] · **Alat:** *Chrome DevTools Flexbox & Grid Inspector Badges*.
* **Sesi Teori (`100'`):** Membedakan secara tajam kapan memakai **Flexbox** (aliran komponen 1 dimensi: *navbar, button group, card footer alignment*) dan kapan memakai **CSS Grid** (kerangka halaman 2 dimensi: `grid-template-columns`, satuan `fr`, `minmax()`, `auto-fit`, dan `grid-template-areas`). Merilis resmi **Tugas 1 (RTM-1)**.
* **Sesi Praktikum Lab 3 (`170'`):** Membangun antarmuka *analytics dashboard* yang memadukan kerangka utama *CSS Grid* dengan komponen internal *Flexbox*.
* **PT (`120'`) & BM (`120'`):** Mengerjakan *slicing* struktur utama halaman pada **Tugas 1**.

### PERTEMUAN 4 — Desain Responsif **Mobile-First** & Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alat:** *DevTools Device Mode*, *Tailwind CSS*.
* **Sesi Teori (`100'`):** Mengajarkan pendekatan **Mobile-First** (`min-width` *breakpoints*: `640px, 768px, 1024px, 1280px`), teknik gambar responsif (`max-width: 100%`, `aspect-ratio`, `object-fit`), serta pengenalan efisiensi *Utility-First CSS* (**Tailwind CSS**) setelah fondasi CSS murni kokoh.
* **Sesi Praktikum Lab 4 (`170'`):** Verifikasi dan pengujian langsung hasil **Tugas 1 (`CPMK-1`)** di laboratorium pada resolusi `360px`, `768px`, dan `1440px` + pengecekan skor aksesibilitas dasar.
* **PT (`120'`) & BM (`120'`):** Mempelajari dasar sintaks modern JavaScript ES6+.

### PERTEMUAN 5 — Pemrograman **JavaScript Modern (ES6+)** & Pengolahan Data Imutabel
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Alat:** *Browser Console*, *ES Modules*.
* **Sesi Teori (`100'`):** Membahas fitur inti **ES6+** yang menjadi prasyarat mutlak pengembangan React modern: `const/let`, *arrow functions*, *template literals*, *object/array destructuring*, *spread/rest*, *optional chaining* (`?.`) & *nullish coalescing* (`??`), *ES Modules* (`import/export`), serta rantai transformasi data deklaratif (`map`, `filter`, `reduce`, `toSorted`).
* **Sesi Praktikum Lab 5 (`170'`):** Menyelesaikan 10 tantangan pengolahan larik objek JSON transaksi tanpa memakai perulangan mutatif yang merusak data asli.
* **PT (`120'`) & BM (`120'`):** Membangun modul utilitas kalkulasi & pemfilteran data dengan ES Modules.

### PERTEMUAN 6 — Manipulasi **DOM**, *Event Delegation*, & Mitigasi *DOM XSS*
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Alat:** *DOM Inspector*, *Application Tab (`localStorage`)*.
* **Sesi Teori (`100'`):** Menguraikan seleksi & modifikasi simpul **DOM**, bahaya keamanan menyuntikkan masukan pengguna ke `innerHTML` (*DOM-based XSS*) vs penggunaan aman `textContent` / `createElement`, mekanisme *Event Bubbling & Event Delegation*, serta penyimpanan preferensi klien di `localStorage`.
* **Sesi Praktikum Lab 6 (`170'`):** Membangun halaman pengelola tugas/keranjang belanja dinamis lengkap pencarian instan, filter kategori, dan penyimpanan `localStorage` bebas galat konsol.
* **PT (`120'`) & BM (`120'`):** Menambahkan validasi formulir interaktif waktu nyata pada aplikasi latihan.

### PERTEMUAN 7 — Komunikasi Asinkron: *Event Loop*, **Fetch API**, & **`async/await`**
* **Sub-CPMK:** `Sub-CPMK-2.2` [C3] · **Alat:** *Browser Network Inspector* (simulasi *Slow 3G* & *Offline*).
* **Sesi Teori (`100'`):** Membedah cara kerja *Single-Threaded JavaScript Event Loop* (*Call Stack, Microtask Queue, Callback Queue*), evolusi *Callback → Promise → **`async/await`***, penggunaan **Fetch API** (`response.ok`, penguraian `await response.json()`), serta pola wajib mengelola 3 keadaan antarmuka (*Loading*, *Success*, dan *Error*) di dalam blok `try / catch / finally`.
* **Sesi Praktikum Lab 7 (`170'`):** Menghubungkan antarmuka katalog ke *endpoint* JSON asinkron, menguji ketangguhan tampilan saat mode *Slow 3G* / *Offline* diaktifkan di *Network Tab*, dan klinik persiapan UTS.
* **PT (`120'`) & BM (`120'`):** Latihan mandiri menghadapi ujian praktik *live coding* UTS Pekan 8.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3]) · **Bobot:** **25%** · **Durasi:** `150 menit` (*Live Coding* di Laboratorium).
* **Pelaksanaan:** Mahasiswa membangun secara mandiri halaman web interaktif menggunakan **JavaScript ES6+**, manipulasi **DOM**, dan pengambilan data asinkron **Fetch API (`async/await`)** lengkap pencarian/filter dinamis dan penanganan *loading/error* yang bersih dan bebas *error* konsol.

### PERTEMUAN 9 — Paradigma **SPA** & Arsitektur Komponen *Reusable* **React** (*JSX & Props*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C3→C6] · **Alat:** Node.js LTS, *Vite*, *React Developer Tools*.
* **Sesi Teori (`100'`):** Membahas umpan balik UTS dan menjelaskan mengapa antarmuka berskala besar beralih dari manipulasi DOM imperatif ke pendekatan deklaratif berbasis komponen (**React SPA**): konsep *UI as a Function of State*, aturan **JSX**, dekomposisi antarmuka menjadi komponen kecil yang *reusable*, aliran data satu arah via **Props**, komposisi `children`, dan perenderan daftar ber-`key` unik.
* **Sesi Praktikum Lab 8 (`170'`):** Menginisialisasi proyek React + Vite dan membangun sistem komponen *reusable* (`Button`, `Badge`, `InputField`, `ProductCard`, `Modal`).
* **PT (`120'`) & BM (`120'`):** Merancang pohon hierarki komponen (*Component Tree*) untuk rencana aplikasi SPA Tugas 2.

### PERTEMUAN 10 — Manajemen *State* Interaktif (**`useState`**), *Controlled Forms*, & **`useEffect`**
* **Sub-CPMK:** `Sub-CPMK-3.1` [C6] · **Alat:** *React DevTools Profiler & Components Inspector*.
* **Sesi Teori (`100'`):** Mengajarkan aturan **React Hooks**, pembaruan objek/larik secara imutabel pada **`useState`**, pola *Controlled Forms*, penaikan *state* ke induk terdekat (*Lifting State Up*), *Derived State* (jangan menyimpan hal yang bisa dihitung langsung di dalam *state*!), serta penggunaan tepat **`useEffect`** beserta larik dependensi dan fungsi *cleanup* (`AbortController` / `clearInterval`). Merilis resmi **Tugas 2 (RTM-2)**.
* **Sesi Praktikum Lab 9 (`170'`):** Membangun halaman interaktif multi-komponen dengan formulir terkendali, validasi instan, dan sinkronisasi efek yang bersih.
* **PT (`120'`) & BM (`120'`):** Mengembangkan fitur inti komponen dan *state* pada proyek **Tugas 2**.

### PERTEMUAN 11 — Navigasi **React Router**, **Context API**, & Abstraksi **Custom Hooks**
* **Sub-CPMK:** `Sub-CPMK-3.2` [C6] · **Alat:** `react-router-dom`, *React DevTools*.
* **Sesi Teori (`100'`):** Mengajarkan perutean sisi klien pada **SPA** menggunakan **React Router** (`BrowserRouter / createBrowserRouter`, tata letak bersama `<Outlet />`, tautan aktif `<NavLink>`, parameter dinamis `useParams`, *query string* `useSearchParams`), pemecahan *prop drilling* dengan **Context API (`createContext`, `useContext`)**, serta ekstraksi logika *reusable* menjadi **Custom Hooks** (`useLocalStorage`, `useDebounce`, `useFetch`).
* **Sesi Praktikum Lab 10 (`170'`):** Mengonfigurasi aplikasi SPA 4 rute dengan *Shared Layout*, tema/keranjang global berbasis *Context*, dan minimal 1 *Custom Hook* buatan sendiri.
* **PT (`120'`) & BM (`120'`):** Menyelesaikan keseluruhan arsitektur aplikasi **React SPA** untuk **Tugas 2**.

### PERTEMUAN 12 — Evaluasi Arsitektur Komponen Skalabel & Penilaian Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.1` & `3.2` [C6] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alat:** Repositori Git & Proyektor Lab.
* **Sesi Teori (`100'`):** Membahas penataan struktur folder berbasis fitur (*Feature-Based Architecture*), pemisahan komponen tampilan murni (*Presentational*) vs pengelola logika, dan anti-pola umum React yang wajib dihindari sebelum masuk tahap integrasi API penuh.
* **Sesi Praktikum Lab 11 (`170'`):** Demonstrasi langsung & *code walkthrough* proyek **Tugas 2 (`CPMK-3`)** di laboratorium — dosen/asisten menguji *reusability* komponen, ketepatan Hooks, dan navigasi React Router setiap mahasiswa/tim.
* **PT (`120'`) & BM (`120'`):** Memilih *Public REST API* / menyiapkan skema *JSON Server mock* untuk proyek integrasi akhir UAS.

### PERTEMUAN 13 — Integrasi Penuh Aplikasi **React** dengan **RESTful API** Eksternal
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5] · **Alat:** *Mock/Public REST API*, *Browser Network Inspector*.
* **Sesi Teori (`100'`):** Mengajarkan arsitektur lapisan komunikasi HTTP terpusat di sisi *front-end* (konfigurasi `VITE_API_BASE_URL`, abstraksi fungsi layanan `GET / POST / PUT / DELETE`, pembatalan permintaan usang dengan `AbortController`, *debounced search*, paginasi, serta desain pengalaman pengguna tangguh: *Skeleton Loader, Empty State, Optimistic/Toast Feedback,* dan *Error Recovery*) — dengan tetap menjaga pagar kurikulum: kode server basis data akan dibangun di `STI-416`.
* **Sesi Praktikum Lab 12 (`170'`):** Menghubungkan aplikasi React SPA proyek UAS ke **RESTful API** eksternal secara terverifikasi dan menguji skenario sukses maupun kegagalan jaringan.
* **PT (`120'`) & BM (`120'`):** Menyelesaikan seluruh integrasi *endpoint* API pada aplikasi proyek UAS.

### PERTEMUAN 14 — *Client-Side Protected Routes*, Keamanan Antarmuka, & **Code Splitting**
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C5] · **Alat:** *Vite Production Build*, *Bundle Analyzer*.
* **Sesi Teori (`100'`):** Membahas mekanisme pembungkus rute terproteksi (*Protected Route Wrapper*) di sisi klien, pemahaman perilaku **CORS** di peramban, pencegahan kebocoran kunci rahasia di bundel klien, serta teknik pemangkasan beban JavaScript awal menggunakan **Route-Based Code Splitting (`React.lazy` + `<Suspense>`)** dan evaluasi kritis kapan `useMemo`/`React.memo` benar-benar dibutuhkan.
* **Sesi Praktikum Lab 13 (`170'`):** Menerapkan *lazy-loaded routes* pada proyek aplikasi, menjalankan `npm run build && npm run preview`, dan membandingkan ukuran berkas `.js` sebelum vs sesudah *code splitting*.
* **PT (`120'`) & BM (`120'`):** Mengukur skor awal (*baseline*) Google Lighthouse pada *production preview* aplikasi masing-masing.

### PERTEMUAN 15 — Optimasi **Core Web Vitals** & Verifikasi **Google Lighthouse $\ge 85$**
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Alat:** *Chrome Lighthouse (Incognito / Production Mode)*, *PageSpeed Insights*.
* **Sesi Teori (`100'`):** Membedah tiga metrik utama **Core Web Vitals** Google — **Largest Contentful Paint (LCP $\le 2,5\text{ s}$)**, **Interaction to Next Paint (INP $\le 200\text{ ms}$)**, dan **Cumulative Layout Shift (CLS $\le 0,1$)** — beserta teknik konkret mendongkrak skor **Lighthouse** melampaui **85**: konversi gambar ke `WebP/AVIF`, pemberian `width` & `height` eksplisit pencegah pergeseran tata letak (CLS), `loading="lazy"` untuk gambar di bawah lipatan, `fetchpriority="high"` pada elemen LCP utama, perbaikan kontras/label aksesibilitas, serta kelengkapan tag `<title>` dan `<meta name="description">`.
* **Sesi Praktikum Lab 14 (`170'`):** *Optimization Sprint* di laboratorium — mahasiswa mengaudit silang aplikasi rekan pada mode *Production Build / Live Deployed URL* hingga seluruh 4 kategori (terutama **Performance $\ge 85$** dan **Accessibility $\ge 90$**) terbukti hijau/tuntas.
* **PT (`120'`) & BM (`120'`):** Finalisasi *deployment* publik, repositori Git, dan laporan metrik *Before–After Optimization* untuk UAS Pekan 16.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Aplikasi Produksi React + RESTful API & Laporan Optimasi (50% nilai UAS)** dengan **Sidang Audit *Google Lighthouse* Langsung di Mode Incognito & Uji Modifikasi Kode Individu (50% nilai UAS)** — penguji menjalankan langsung audit *Lighthouse* di depan mahasiswa untuk memverifikasi skor **$\ge 85$** secara autentik dan menguji penguasaan kode setiap individu.
