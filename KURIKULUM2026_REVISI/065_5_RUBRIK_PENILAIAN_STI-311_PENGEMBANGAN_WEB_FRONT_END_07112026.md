# 065_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI311` · **Klaster Rubrik Master (Dok 018):** Klaster 2 (`K-2`)  
**CPL:** `CPL-08` (`P4` = 45%) & `CPL-13` (`KK5` = 55%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN REKAYASA KODE & PLATFORM WEB (`K-2`)

Selaras **Dokumen 018 §3**, penilaian Klaster 2 (`K-2`) pada `STI-311 Pengembangan Web Front End` berbasis bukti kode dan kinerja terukur: validitas semantik W3C, adaptivitas lintas resolusi, eksekusi JavaScript bebas *error* konsol, *reusability* arsitektur komponen **React SPA**, ketangguhan integrasi **RESTful API**, serta pembuktian langsung skor **Google Lighthouse $\ge 85$**.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-08` [C3])
**Objek Penilaian:** Antarmuka Web Responsif **HTML5 Semantik** & **CSS3 Modern (*Flexbox, Grid*)** Beraksesibilitas Dasar.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Struktur **HTML5 Semantik** & Validitas W3C**<br>(`Sub-CPMK-1.1`) | **25%** | Memakai tag HTML5 semantik secara tepat di seluruh bagian halaman, hierarki `h1–h6` tertib, dan lolos *W3C Validator* dengan **0 error & 0 warning**. | Struktur HTML5 semantik tepat dan lolos validasi W3C (0 *error*, maksimal 1–2 peringatan sepele). | Menggunakan tag semantik utama (`header, main, footer`), namun bagian konten dalam masih didominasi `<div>` generik. | Struktur dokumen tidak semantik (*div-soup*) dan menghasilkan beberapa *error* pada W3C Validator. | Dokumen HTML rusak atau menyalin templat jadi pihak lain. |
| **2. Penerapan **CSS3 Modern (*Flexbox & Grid*)** & *Design Tokens***<br>(`Sub-CPMK-1.2`) | **35%** | Memadukan **CSS Grid** (2D) dan **Flexbox** (1D) secara elegan, variabel `:root` tertata rapi, kode CSS modular tanpa `!important` liar. | Tata letak Flexbox dan CSS Grid diterapkan tepat menghasilkan tampilan visual yang bersih dan konsisten. | Mampu menggunakan Flexbox dengan baik, namun penerapan CSS Grid masih sangat sederhana atau kurang rapi. | Tata letak kaku berbasis piksel tetap/`position: absolute` berlebih sehingga elemen saling bertumpuk. | Gagal menata tampilan menggunakan CSS3 modern. |
| **3. Responsivitas Lintas Resolusi (*Mobile, Tablet, Desktop*)**<br>(`Sub-CPMK-1.2`) | **25%** | Tampilan beradaptasi mulus pada `360px`, `768px`, dan `1440px` (*mobile-first*), gambar proporsional, dan **0 horizontal overflow** di semua ukuran layar. | Tampilan adaptif dan nyaman dibaca di tiga titik resolusi utama tanpa elemen terpotong. | Responsif pada layar ponsel dan desktop, namun terdapat ketidakteraturan spasi kecil pada ukuran tablet. | Halaman melebar keluar layar (*horizontal scroll*) atau teks terlalu kecil saat dibuka di layar ponsel `360px`. | Halaman hanya dibuat untuk satu ukuran layar desktop saja. |
| **4. Standar Aksesibilitas Dasar (*WCAG / ARIA*)**<br>(`Sub-CPMK-1.1`) | **15%** | Seluruh input ber-`<label>`, gambar informatif ber-`alt` jelas, indikator `:focus-visible` nyata untuk *keyboard*, kontras lolos WCAG AA, skor *Lighthouse A11y* $\ge 95$. | Label formulir, teks `alt`, dan kontras warna terpenuhi baik (*Lighthouse Accessibility* 88–94). | Sebagian besar atribut aksesibilitas dasar ada (*Lighthouse Accessibility* 80–87), walau 1–2 tombol ikon belum ber-`aria-label`. | Banyak input tanpa `<label>`, gambar tanpa `alt`, dan kontras teks kabur (*A11y* $< 80$). | Mengabaikan seluruh aspek aksesibilitas dasar. |

$$\text{Skor Tugas 1} = 0,25(K_1) + 0,35(K_2) + 0,25(K_3) + 0,15(K_4)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-08` [C3])
**Objek Penilaian:** Ujian Praktik *Live Coding* 150 Menit: **JavaScript ES6+**, Manipulasi **DOM**, & **Fetch API (`async/await`)**.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Implementasi **JavaScript ES6+** & Pengolahan Data**<br>(`Sub-CPMK-2.1`) | **30%** | Kode modular memakai sintaks ES6+ bersih (`const/let`, *destructuring*, `map/filter/toSorted` imutabel); pencarian, filter, dan pengurutan bekerja akurat seketika. | Fitur pencarian dan pemfilteran berjalan akurat menggunakan sintaks ES6+ yang rapi. | Pencarian atau filter dasar berjalan, namun masih mencampur mutasi larik langsung dan perulangan imperatif panjang. | Logika filter/pencarian menghasilkan keluaran salah saat dikombinasikan. | Tidak mampu menulis logika dasar JavaScript ES6+. |
| **2. Manipulasi **DOM**, *Events*, & `localStorage`**<br>(`Sub-CPMK-2.1`) | **30%** | Perenderan **DOM** dinamis aman dari injeksi XSS, memakai *event delegation* efisien, dan sinkronisasi `localStorage` berjalan mulus saat halaman dimuat ulang. | Pembaruan DOM interaktif dan penyimpanan `localStorage` berjalan sesuai spesifikasi soal. | Perenderan kartu dan klik tombol berjalan, namun fitur simpan/hapus `localStorage` belum sinkron sempurna. | Pembaruan tampilan menduplikasi elemen lama berkali-kali atau menyuntikkan `innerHTML` mentah berbahaya. | Gagal menampilkan data ke halaman DOM. |
| **3. Komunikasi Asinkron **Fetch API & `async/await`****<br>(`Sub-CPMK-2.2`) | **30%** | Menggunakan `async/await` + `try/catch/finally` dengan pemeriksaan `if (!res.ok)`, menampilkan *Loading Indicator* dan penanganan gagal jaringan dengan sangat bersih. | Pengambilan data via `fetch` + `async/await` berhasil dan menyertakan indikator *loading* serta blok `catch`. | Berhasil mengambil dan menampilkan data dari *endpoint*, namun tidak memeriksa status `res.ok` atau belum ada *loading state*. | Salah memakai `fetch` tanpa `await` sehingga merender `[object Promise]` ke layar. | Tidak mampu melakukan pengambilan data asinkron. |
| **4. Kebersihan Eksekusi (*Zero Console Errors*)** | **10%** | Berjalan mulus pada seluruh skenario uji termasuk input kosong/ekstrem dengan **0 error di Browser Console**. | Berjalan lancar tanpa *error* konsol pada alur pemakaian normal. | Muncul 1 peringatan/galat minor pada kondisi batas kosong namun aplikasi tidak macet. | Muncul *Uncaught TypeError* berulang di konsol yang memutus interaktivitas halaman. | Kode gagal dijalankan karena *SyntaxError*. |

$$\text{Skor UTS} = 0,30(K_1) + 0,30(K_2) + 0,30(K_3) + 0,10(K_4)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-13` [C6])
**Objek Penilaian:** Proyek **Single Page Application (SPA)** Berbasis **React** (*Reusable Components, Props, State, Hooks, Router, Context*).

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Arsitektur Komponen *Reusable* & **Props****<br>(`Sub-CPMK-3.1`) | **35%** | Antarmuka didekomposisi menjadi $\ge 6$ komponen *reusable* berkohesi tinggi dengan kontrak **Props** & `children` bersih, tanpa duplikasi UI dan tanpa peringatan `key`. | Komponen terpecah rapi, dipakai ulang lintas halaman dengan *props* yang jelas dan bebas peringatan konsol. | Komponen utama sudah dipisahkan, namun masih ada 1–2 komponen halaman besar yang terlalu gemuk (*monolithic page component*). | Seluruh halaman ditulis dalam 1–2 berkas JSX raksasa tanpa komponen yang benar-benar *reusable*. | Gagal membangun aplikasi berbasis komponen React. |
| **2. Pengelolaan **State, Controlled Forms, & Hooks****<br>(`Sub-CPMK-3.1`) | **30%** | Penggunaan `useState`, `useEffect` (lengkap dependensi tepat & *cleanup*), *Controlled Forms* bervalidasi, dan $\ge 1$ **Custom Hook** sangat bersih dan imutabel. | Manajemen *state*, formulir terkendali, dan *Hooks* berjalan akurat tanpa *infinite render loop*. | `useState` dan formulir dasar berjalan baik, namun terdapat peringatan *missing dependency* pada `useEffect` atau *Custom Hook* sangat sederhana. | Memutasi variabel *state* secara langsung (`state.push(...)`) sehingga UI gagal memperbarui diri secara konsisten. | Tidak memahami mekanisme *State* dan *Hooks* React. |
| **3. Navigasi **React Router** & **Context API****<br>(`Sub-CPMK-3.2`) | **25%** | $\ge 4$ rute dengan `<Outlet />` *layout*, parameter dinamis `:id`, halaman 404, serta **Context API** global bekerja mulus tanpa *full-page reload* (`<a href>` keliru). | *React Router* multi-halaman dan *Context Provider* berjalan fungsional dengan baik. | Navigasi dasar *React Router* berjalan, namun pemanfaatan parameter dinamis atau *Context API* masih minimal. | Menggunakan `<a href="...">` biasa yang memuat ulang seluruh aplikasi atau rute rusak saat di-*refresh*. | Aplikasi hanya satu tampilan tanpa *React Router*. |
| **4. Kerapian Kode & Verifikasi *Walkthrough* Lab** | **10%** | Struktur folder sangat rapi, riwayat Git bersih, dan mahasiswa fasih menjelaskan aliran *props/state* saat diuji di lab. | Struktur proyek rapi dan mahasiswa mampu menjawab pertanyaan bedah kode dengan tepat. | Struktur proyek cukup rapi dan lulus verifikasi dasar kode. | Kesulitan menjelaskan cara kerja komponen yang terdapat di dalam proyeknya sendiri. | Menyalin repositori jadi tanpa kontribusi nyata. |

$$\text{Skor Tugas 2} = 0,35(K_1) + 0,30(K_2) + 0,25(K_3) + 0,10(K_4)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-13` [C5])
**Objek Penilaian:** Aplikasi Produksi **React + RESTful API Eksternal** + Verifikasi Langsung **Google Lighthouse $\ge 85$** + Sidang Individu.

| Dimensi Kriteria (`K-2`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Integrasi **RESTful API** Eksternal & Ketangguhan UI**<br>(`Sub-CPMK-4.1`) | **35%** | Klien HTTP terpusat bersih (`.env`), mengintegrasikan operasi baca/tulis/pencarian parameter terhadap REST API secara mulus lengkap *Skeleton Loading, Empty State,* dan pemulihan *Error State* elegan. | Integrasi ke beberapa *endpoint* RESTful API eksternal berjalan akurat dengan penanganan *loading* dan *error* yang baik. | Aplikasi berhasil menampilkan dan memfilter data dari REST API eksternal, namun alur pengiriman data (`POST/PUT`) atau tampilan gagalnya masih sederhana. | Sebagian besar data masih *hardcoded* statis di berkas lokal dan panggilan API gagal saat diuji. | Aplikasi tidak terhubung ke RESTful API mana pun. |
| **2. Optimasi Performa & Verifikasi **Lighthouse $\ge 85$****<br>(`Sub-CPMK-4.2`) | **35%** | Audit langsung *Lighthouse* (*Production/Incognito*) membuktikan **Performance $\ge 90$** (dan A11y/Best Practices/SEO $\ge 90$), didukung bukti nyata *Code Splitting (`React.lazy`)*, aset `WebP`, CLS $\approx 0$, serta laporan *Before–After* tajam. | Audit langsung *Lighthouse* terverifikasi mencapai **$\ge 85$** dengan penerapan teknik optimasi aset dan *bundle* yang jelas. | Skor *Lighthouse Performance* berada tepat di ambang kelulusan (**85** pada desktop atau **80–84** pada simulasi *throttled mobile*) dengan upaya optimasi dasar terverifikasi. | Tidak menerapkan optimasi (*gambar mentah multi-MB, bundle raksasa*) sehingga skor *Lighthouse Performance* jatuh di rentang **60–79**. | Aplikasi gagal di-*build* produksi atau skor *Lighthouse* $< 60$. |
| **3. Kualitas Kode, Keamanan Klien, & Kolaborasi Git** | **15%** | Kode bersih modular, tidak membocorkan kredensial rahasia, bebas *error* konsol, dan riwayat *commit/PR* seluruh anggota tim merata. | Kode rapi, bebas galat konsol di produksi, dan kontribusi Git tiap anggota jelas. | Kode berjalan baik walau masih ada sedikit kode tak terpakai atau *commit* kurang merata. | Banyak galat konsol pada *production build* atau riwayat Git timpang. | Plagiarisme kode proyek pihak lain. |
| **4. Sidang *Live Code Modification* & Tanya-Jawab Individu** | **15%** | Mahasiswa sigap menyelesaikan tantangan modifikasi kecil komponen/pemanggilan API langsung di depan penguji dan fasih menjelaskan metrik *Core Web Vitals*. | Mahasiswa berhasil melakukan modifikasi yang diminta dan menjawab pertanyaan teknis dengan akurat. | Mahasiswa menyelesaikan sebagian modifikasi langsung dengan sedikit arahan sintaks. | Tidak mampu mengubah komponen sederhana atau menjelaskan alur `fetch` pada kodenya sendiri. | Tidak hadir sidang UAS atau melanggar kejujuran akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,15(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF PRAKTIKUM LABORATORIUM MINGGUAN (LAB 1–14)

| Kriteria Formatif Lab | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketuntasan & Kebersihan Kode Lab** | Modul praktikum selesai di sesi lab, bebas galat *DevTools Console*, dan ter-*commit* rapi ke Git. | Modul praktikum selesai tepat waktu dengan tampilan dan fungsi benar. | Modul selesai minimal 75% di lab dan dituntaskan mandiri. | Gagal menyelesaikan latihan dasar praktikum. |
| **Kemandirian Debugging di *Browser DevTools*** | Terampil menggunakan *Elements, Console, Network,* dan *React DevTools* untuk melacak masalah sendiri. | Mampu menemukan dan memperbaiki galat sintaks/jaringan dengan *DevTools*. | Masih sering meminta bantuan asisten untuk membaca pesan galat konsol jelas. | Pasif menyalin kode tanpa memeriksa *DevTools*. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-311` (`CPL-08` & `CPL-13` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa mampu merekayasa aplikasi *front-end* **React SPA** produksi yang semantik, aksesibel, responsif lintas perangkat, bersih secara komponen, terintegrasi tangguh dengan **RESTful API**, dan teroptimasi melampaui **Lighthouse $\ge 90$**. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa menguasai HTML5/CSS3 Flexbox-Grid, JavaScript ES6+/DOM/Fetch, pembangunan komponen *reusable* React SPA, integrasi RESTful API, serta mencapai target performa **Lighthouse $\ge 85$**. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam membangun antarmuka web responsif, interaktivitas JS asinkron, aplikasi SPA React dasar, dan integrasi API fungsional. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih menghasilkan tampilan pecah di perangkat bergerak, galat *runtime* asinkron, komponen React monolitik, atau performa muat yang buruk. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal membangun antarmuka web yang berfungsi atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-311` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu membangun halaman web **HTML5 semantik** yang valid dengan standar aksesibilitas dasar. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menata antarmuka responsif lintas resolusi menggunakan **CSS3 Flexbox dan CSS Grid**. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengimplementasikan interaktivitas halaman menggunakan **JavaScript ES6+** dan manipulasi **DOM**. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu mengambil dan mengelola data asinkron menggunakan **Fetch API** dan **`async/await`** bebas *error*. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu membangun komponen **React** (*Component, Props, State, Hooks*) yang modular dan *reusable*. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu mengonfigurasi navigasi **React Router** dan manajemen *state* lintas-komponen pada **SPA**. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu mengintegrasikan aplikasi *front-end* dengan **RESTful API** eksternal lengkap penanganan *loading/error*. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu mengoptimasi performa muat aplikasi web hingga terverifikasi mencapai **Lighthouse score $\ge 85$**. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-311`)

```text
==============================================================================================================================
         LEMBAR REKAPITULASI PENILAIAN OBE — STI-311 PENGEMBANGAN WEB FRONT END (3 SKS: T=2, P=1)
==============================================================================================================================
Semester / TA  : Semester 3 (Ganjil) / 2026-2027     CPL Dibebankan : CPL-08 (P4: 45%) & CPL-13 (KK5: 55%) [Level: Reinforce]
Klaster Rubrik : K-2 (Pemrograman & Platform Web)    Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2 (25%)    | UAS (30%)   | NA    | CPL-08 | CPL-13 | Huruf
   |           |                  | [CPMK-1:C3] | [CPMK-2:C3] | [CPMK-3:C6] | [CPMK-4:C5] | Akhir | (45%)  | (55%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 85.0        | 88.0        | 90.0        | 87.85 | 86.33  | 89.09  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 74.0        | 78.0        | 80.0        | 77.60 | 75.78  | 79.09  | B+
3  | 250101003 | [Nama Mhs 3]     | 70.0        | 66.0        | 68.0        | 70.0        | 68.50 | 67.78  | 69.09  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 78.67       | 75.00       | 78.00       | 80.00       | 77.98 | 76.63  | 79.09  | >=65:100%
==============================================================================================================================
```
