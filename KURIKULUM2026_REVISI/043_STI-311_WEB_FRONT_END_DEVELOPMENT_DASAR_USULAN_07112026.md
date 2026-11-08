# 043 — USULAN TURUNAN STI-311: WEB FRONT END DEVELOPMENT
## HTML dan CSS dasar–menengah, Flexbox lanjutan, pengenalan Bootstrap dan Tailwind, serta JavaScript dasar

**Program Studi S1 Sistem dan Teknologi Informasi — FSTI Universitas Widyagama Malang**

**Tanggal penyusunan/pembaruan:** 7 November 2026

**Status:** Rancangan yang diselaraskan pada dokumen terkait; belum disahkan secara akademik.

> Dokumen ini adalah **dokumen baru turunan**, bukan ekstraksi verbatim dan bukan revisi otomatis terhadap Dokumen 043 induk. Usulan ini mencakup HTML dasar–menengah, CSS dasar–menengah dan Flexbox lanjutan, pengenalan dasar Bootstrap dan Tailwind CSS, serta JavaScript dasar. **React dan framework JavaScript sejenis tidak diajarkan.** Rumusan CPMK, Sub-CPMK, asesmen, dan rencana pertemuan adalah usulan baru yang perlu persetujuan koordinator dan program studi sebelum digunakan sebagai rujukan resmi.
>
> Dokumen 043 induk, varian aktif, ekstraksi, Dokumen 007/037, buku kompilasi dan paket `PERANGKAT_AJAR/065_*` telah diselaraskan pada lingkup ini. Pengesahan koordinator/prodi dan penanganan materi lanjutan pada MK hilir masih diperlukan; backup dan RPS pilot lama ditandai sebagai arsip.

---

## 1. Identitas dan posisi mata kuliah

| Atribut | Keterangan |
|---|---|
| Kode / nama resmi | `STI-311` — Pengembangan Web Front End (*Web Front End Development*) |
| Program / rumpun | Core STI, rekayasa perangkat lunak dan platform |
| Semester / beban / tipe | Semester 3 / 3 SKS / +P, terdiri atas 2 SKS teori dan 1 SKS praktikum |
| Prasyarat | `FST-102` Algoritma dan Pemrograman |
| CPL dibebankan | `CPL-08` (`P4`) dan `CPL-13` (`KK5`); tingkat **R** (*reinforce*) |
| Profil lulusan / PEO | `PL-3`; `PEO-1` dan `PEO-2` |
| BoK asal Dok 043 | `BK-IS12` *Web and Mobile Application Development* dan `BK-IT04` *Platform Technologies*; bagian yang dibahas dalam usulan ini adalah front-end web sisi klien |
| Acuan identitas | Dokumen 005; pemetaan CPL, PL, PEO dan IRM mengikuti Dokumen 004 |

### Deskripsi singkat

Mahasiswa membangun halaman web menggunakan HTML dasar hingga menengah, CSS dasar hingga menengah, serta Flexbox lanjutan untuk tata letak responsif. Mahasiswa mengenal cara menggunakan Bootstrap dan Tailwind CSS pada tingkat dasar dan menambahkan interaksi menggunakan JavaScript dasar. Latihan terapan meliputi **kalkulator sederhana dengan Bootstrap atau Tailwind** dan **landing page responsif dengan JavaScript sederhana**. Seluruh hasil dapat diuji secara lokal tanpa backend, database, layanan API, maupun React.

### CPL yang dibebankan

Rumusan resmi berikut dipertahankan dari Dokumen 003; kontribusi STI-311 pada `CPL-13` adalah **fondasi** pengembangan web, bukan pembuktian bahwa mahasiswa telah menguasai seluruh aspek platform skalabel yang tercakup dalam CPL tersebut.

| Kode | Rumusan resmi CPL | Peran STI-311 dalam usulan |
|---|---|---|
| `CPL-08` (`P4`) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | Menerapkan prinsip struktur halaman, tampilan, tata letak, dan pemrograman dasar sisi klien. |
| `CPL-13` (`KK5`) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | Membangun antarmuka web dasar yang responsif dan interaktif; kemampuan platform lanjutan dikembangkan pada MK lain. |

---

## 2. Lingkup, tingkat kedalaman, dan perbedaan dari Dokumen 043

| Bidang | Cakupan usulan | Batas kedalaman |
|---|---|---|
| **HTML dasar** | Struktur dokumen, elemen semantik, heading, paragraf, daftar, tautan, gambar dan atribut. | Menyusun beberapa bagian halaman yang jelas dan dapat dinavigasi. |
| **HTML menengah** | Tabel dan formulir: label, tipe input, pengelompokan sederhana, validasi HTML bawaan; teks alternatif dan navigasi keyboard dasar. | Formulir simulasi tidak mengirim data ke server; tidak membahas aplikasi server. |
| **CSS dasar–menengah** | Cara memuat stylesheet, selektor, cascade dan specificity dasar, warna, tipografi, box model, display, ukuran, position sederhana, media query dan responsivitas. | CSS Grid kompleks, animasi lanjutan dan sistem desain skala besar tidak diwajibkan. |
| **Flexbox lanjutan** | Sumbu utama/silang, `display: flex`, `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`, `align-content`, `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`, dan `order`; tata letak responsif dan *nested flex* sederhana. | Menyusun navigasi, kartu dan susunan dua bagian responsif; tidak menjadikan Grid kompleks sebagai prasyarat. |
| **Bootstrap dasar** | Menghubungkan stylesheet yang disediakan; pengenalan container, grid dasar, tombol, kartu, formulir, dan utilitas responsif. | Pengenalan dan penggunaan kelas bawaan; tidak membuat tema atau plugin lanjutan. |
| **Tailwind CSS dasar** | Menghubungkan stylesheet yang disediakan; pengenalan *utility class* untuk warna, spacing, ukuran, teks, Flexbox dan responsivitas. | Pengenalan kelas bawaan; tidak membahas konfigurasi/build pipeline atau kustomisasi tema lanjutan. |
| **JavaScript dasar** | Variabel, tipe data, operator, percabangan, perulangan sederhana, fungsi, array sederhana, DOM, event, input dan validasi dasar. | Interaksi browser sederhana; tidak membahas Fetch, Promise, async/await, REST API, framework JS atau state management lanjutan. |

### Perbedaan utama dari Dok 043 induk

- **Dipertahankan dan diperdalam:** HTML, CSS, responsivitas, dan interaktivitas sisi klien; Flexbox mendapat ruang khusus hingga tingkat lanjutan.
- **Ditambahkan sebagai pengenalan:** Bootstrap dan Tailwind CSS dasar. Mahasiswa mengenal keduanya, tetapi memilih **salah satu** untuk proyek kalkulator.
- **Dikeluarkan dari capaian dan asesmen:** React, Vue, SPA, Hooks, Context API dan React Router; integrasi REST API, Fetch dan pemrograman asinkron; target Lighthouse ≥ 85 dan optimasi produksi lanjutan.
- **Diganti hasil akhirnya:** aplikasi React terhubung API menjadi kalkulator dasar dan landing page responsif dengan JavaScript sederhana.

### Boundary guardrails usulan

- **IN-SCOPE:** semua materi pada tabel di atas, latihan dengan Bootstrap **dan** Tailwind, kalkulator dasar, landing page, pengujian manual dan aksesibilitas dasar.
- **OUT-OF-SCOPE:** React/Vue dan framework JavaScript sejenis; SPA dan routing framework; Fetch/AJAX, Promise, async/await, konsumsi REST API; backend, database, autentikasi server, deployment cloud; build pipeline dan konfigurasi Tailwind lanjutan; optimasi performa lanjutan dan target Lighthouse. Riset UX mendalam tetap di luar MK ini.
- **HANDOFF:** menghasilkan antarmuka responsif dengan HTML, CSS, Flexbox dan JavaScript dasar serta pengalaman memakai kelas Bootstrap dan Tailwind. `STI-416` melanjutkan backend dan penyediaan API; integrasi client–server dan materi front-end lanjutan harus direncanakan secara eksplisit oleh MK hilir/prodi. `STI-522` dan `STC-701` menerima bekal dasar web, bukan kompetensi React atau WebXR.

**Batas keamanan:** validasi formulir JavaScript hanya untuk pengalaman pengguna, bukan jaminan keamanan atau pengganti validasi server. Gunakan data contoh, bukan data pribadi nyata. Interaksi proyek ditulis dengan JavaScript dasar; penggunaan JavaScript/plugin Bootstrap tidak diwajibkan, dan Tailwind CSS sendiri tidak memerlukan JavaScript untuk styling.

---

## 3. Usulan formulasi CPMK (ABCD dan Bloom)

| Kode | Rumusan usulan: mahasiswa (A) | Bloom | CPL |
|---|---|:---:|---|
| `CPMK-1` | mampu **menyusun** halaman HTML dasar–menengah yang memuat struktur semantik, konten, tabel dan formulir (B) berdasarkan kebutuhan kasus yang diberikan (C), dengan struktur elemen, label dan tautan yang sesuai (D). | C3 | `CPL-08` (`P4`) |
| `CPMK-2` | mampu **menerapkan** CSS dasar–menengah dan Flexbox termasuk pengaturan flex item dan responsivitas (B) pada kasus antarmuka yang diberikan, serta mengenali penggunaan kelas Bootstrap dan Tailwind dasar (C), dengan tampilan rapi dan terbaca pada sedikitnya dua ukuran layar (D). | C3 | `CPL-08` (`P4`) |
| `CPMK-3` | mampu **membangun** kalkulator aritmetika sederhana (B) menggunakan JavaScript dasar dan styling **Bootstrap atau Tailwind CSS** (C), dengan operasi dan penanganan input sesuai kasus uji yang diberikan (D). | C3 | `CPL-13` (`KK5`) |
| `CPMK-4` | mampu **membangun dan menguji** landing page responsif dengan interaksi sederhana (B) menggunakan HTML, CSS dan JavaScript dasar, dengan Bootstrap atau Tailwind sebagai pilihan (C), serta mendokumentasikan navigasi, interaksi dan hasil pengujian (D). | C6 | `CPL-13` (`KK5`) |

### Sub-CPMK usulan

| Kode | Kemampuan operasional | CPMK | Bloom |
|---|---|---|:---:|
| `Sub-CPMK-1.1` | Menyusun struktur dokumen semantik dan konten: teks, gambar, daftar serta tautan. | `CPMK-1` | C3 |
| `Sub-CPMK-1.2` | Membuat tabel dan formulir berlabel dengan tipe masukan dan validasi HTML dasar. | `CPMK-1` | C3 |
| `Sub-CPMK-2.1` | Menerapkan selektor, cascade dasar, warna, tipografi, box model, display, position dan media query. | `CPMK-2` | C3 |
| `Sub-CPMK-2.2` | Menggunakan properti container dan item Flexbox, termasuk wrap, grow/shrink/basis dan nested flex, untuk tata letak responsif. | `CPMK-2` | C3 |
| `Sub-CPMK-2.3` | Menerapkan kelas dasar Bootstrap dan utility Tailwind pada latihan antarmuka sederhana. | `CPMK-2` | C3 |
| `Sub-CPMK-3.1` | Menggunakan variabel, tipe data, operator, percabangan, perulangan dan fungsi dalam latihan aritmetika. | `CPMK-3` | C3 |
| `Sub-CPMK-3.2` | Menghubungkan input dan tombol kalkulator dengan fungsi JavaScript melalui DOM dan event, memakai styling Bootstrap atau Tailwind. | `CPMK-3` | C3 |
| `Sub-CPMK-4.1` | Menggabungkan HTML, CSS/Flexbox dan JavaScript dasar menjadi landing page responsif; framework CSS boleh digunakan. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Menyusun dan menjalankan kasus uji navigasi, interaksi, dan tampilan; memperbaiki masalah dan mencatat hasilnya. | `CPMK-4` | C4 |

---

## 4. Rencana 16 pertemuan dan asesmen

Rencana beban per minggu mengikuti konvensi paket perangkat ajar 3 SKS `+P`: **TM 100 menit + praktikum terbimbing 170 menit + penugasan terstruktur 120 menit + belajar mandiri 120 menit**. TM dan praktikum berjumlah 270 menit (4,5 jam); termasuk tugas terstruktur dan mandiri menjadi 510 menit (8,5 jam). Alokasi minggu ujian mengikuti jadwal institusi dan dapat menggunakan waktu tatap muka/praktikum untuk evaluasi.

| Mg | Sub-CPMK | Pokok bahasan dan kegiatan | Bukti / asesmen |
|:---:|---|---|---|
| 1 | 1.1 | Orientasi front-end; peran HTML/CSS/JS dan browser; struktur HTML, teks, heading dan daftar. | Formatif: halaman profil HTML awal. |
| 2 | 1.1 | HTML semantik: header, nav, main, section dan footer; tautan dan gambar dengan teks alternatif. | Formatif: halaman informasi dengan navigasi. |
| 3 | 1.2 | HTML menengah: tabel, formulir, label, input, tombol dan validasi HTML bawaan. | Formatif: formulir simulasi dan tabel berstruktur. |
| 4 | 1.1–1.2, 2.1 | Review HTML dan **Tugas 1**; pengantar stylesheet, selektor, warna dan tipografi CSS. Penilaian Tugas 1 hanya pada HTML. | **Tugas 1 — 20%:** halaman HTML untuk kasus yang disepakati. |
| 5 | 2.1 | CSS dasar–menengah: cascade/spesifisitas dasar, box model, display, ukuran dan position sederhana. | Formatif: stylesheet dan tata letak kartu. |
| 6 | 2.2 | Flexbox: sumbu, direction, alignment, wrap, gap; flex item grow/shrink/basis, align-self, order dan nested flex. | Formatif: navigasi dan kartu responsif menggunakan Flexbox. |
| 7 | 2.1–2.3 | Media query dan latihan dua ukuran layar; pengenalan **Bootstrap** (container, tombol, kartu, grid dasar) dan **Tailwind** (spacing, warna, Flexbox, breakpoint dasar). | Formatif: komponen sederhana menggunakan masing-masing framework. |
| 8 | 2.1–2.3 | Ujian praktik CSS/Flexbox responsif; pengenalan kelas Bootstrap dan Tailwind diuji melalui latihan singkat. | **UTS — 25%:** CSS/Flexbox, dua ukuran layar dan pemilihan kelas framework dasar. |
| 9 | 3.1 | JavaScript di browser: script, variabel, tipe data, operator aritmetika dan konsol. | Formatif: operasi hitung dan keluaran sederhana. |
| 10 | 3.1 | Percabangan, perulangan, fungsi dan array sederhana; konversi input menjadi angka dan kondisi pembagi nol. | Formatif: fungsi kalkulasi dengan contoh input valid/tidak valid. |
| 11 | 3.2 | DOM dan event: membaca input, tombol, menampilkan hasil dan pesan; terapkan kelas Bootstrap atau Tailwind pada rancangan kalkulator. | Formatif: purwarupa kalkulator dengan styling framework pilihan. |
| 12 | 3.1–3.2 | Praktikum dan demonstrasi kalkulator dasar menggunakan JavaScript serta Bootstrap **atau** Tailwind CSS. | **Tugas 2 — 25%:** kalkulator dan hasil uji. |
| 13 | 4.1 | Merencanakan landing page: struktur semantik, hero, manfaat/fitur, call-to-action dan footer; siapkan konten berizin. | Formatif: sketsa dan kerangka HTML. |
| 14 | 4.1 | Tata landing page responsif dengan CSS/Flexbox; Bootstrap atau Tailwind boleh digunakan. Tambahkan interaksi JS sederhana, misalnya menu atau tombol. | Formatif: purwarupa responsif dan interaktif. |
| 15 | 4.2 | Uji navigasi, interaksi, keyboard dan tampilan; perbaiki masalah serta dokumentasikan hasil. | Formatif: daftar kasus uji dan perbaikan. |
| 16 | 4.1–4.2 | Demonstrasi landing page, penjelasan kode individual dan penyerahan berkas. | **UAS — 30%:** landing page, dokumentasi dan demonstrasi. |

### Kebutuhan praktik dan sumber daya

Editor teks, browser modern dan DevTools sudah cukup untuk HTML/CSS/JavaScript. Dosen menyiapkan contoh berkas CSS Bootstrap dan stylesheet Tailwind yang sudah siap pakai untuk latihan lokal, termasuk kelas yang dibutuhkan, atau menyediakan tautan CDN jika jaringan tersedia. **Tidak mewajibkan instalasi Node.js, konfigurasi Tailwind, build pipeline, akun layanan atau koneksi internet saat penilaian.** Catat cara memuat stylesheet pada dokumentasi proyek. Jika memakai CDN, siapkan salinan lokal yang sesuai untuk demonstrasi offline.

---

## 5. Rancangan proyek dasar

### Proyek 1 — Kalkulator sederhana: Tugas 2, minggu 12

- **Tujuan:** menerapkan JavaScript dasar untuk membaca masukan, menjalankan operasi dan menampilkan hasil di halaman.
- **Teknologi wajib:** HTML, JavaScript dasar, dan **pilih satu** CSS framework: Bootstrap **atau** Tailwind CSS. CSS buatan sendiri boleh dipakai sebagai pendamping.
- **Fungsi minimum:** dua input angka; pilihan operasi tambah, kurang, kali dan bagi; tombol hitung dan reset; hasil ditampilkan di halaman.
- **Penanganan minimum:** masukan kosong/tidak valid dan pembagian dengan nol menampilkan pesan yang dapat dipahami, bukan hasil yang menyesatkan.
- **Uji minimum:** penjumlahan `2 + 3 = 5`, pengurangan `5 − 3 = 2`, perkalian `2 × 3 = 6`, pembagian `6 ÷ 3 = 2`, serta kasus input kosong dan pembagi nol. Tambahkan kasus lain sesuai kebutuhan.
- **Bukti:** berkas HTML/CSS/JS dan stylesheet framework yang diperlukan atau tautan yang dicatat, petunjuk menjalankan, serta tabel input–operasi–hasil yang diharapkan–hasil aktual.

### Proyek 2 — Landing page dengan JavaScript sederhana: UAS, minggu 16

- **Tujuan:** mengintegrasikan kemampuan HTML, CSS/Flexbox, responsivitas dan JavaScript dasar pada satu halaman presentasi produk/kegiatan.
- **Teknologi wajib:** HTML, CSS dan JavaScript dasar; Bootstrap **atau** Tailwind boleh digunakan, tetapi tidak wajib. Tidak menggunakan React, backend, database atau API.
- **Isi minimum:** header/navigasi, hero, sedikitnya dua bagian konten (misalnya manfaat dan fitur), call-to-action dan footer; konten dan gambar berizin.
- **Interaksi minimum:** sedikitnya satu interaksi bermakna, misalnya tombol membuka/menutup menu, tombol menampilkan pesan, atau validasi formulir simulasi tanpa pengiriman data. Gunakan DOM dan event dasar.
- **Uji minimum:** tautan/navigasi, interaksi JavaScript termasuk input valid dan tidak valid bila ada formulir, tampilan pada sedikitnya dua lebar layar, label dan navigasi keyboard dasar. Catat hasil dan perbaikan.
- **Bukti:** berkas proyek yang berjalan lokal, petunjuk menjalankan, daftar kasus uji dan hasil, serta demonstrasi dan penjelasan kode individual.

---

## 6. Matriks asesmen dan bukti ketercapaian usulan

Pemetaan berikut merupakan **usulan** dengan satu CPMK utama untuk setiap instrumen. Keterampilan sebelumnya boleh digunakan sebagai prasyarat pengerjaan, tetapi penilaian tiap instrumen difokuskan pada CPMK yang dipetakan agar bobot tidak dihitung dua kali.

| CPMK / CPL | Tugas 1 Mg 4 | UTS Mg 8 | Tugas 2 Mg 12 | UAS Mg 16 | Total |
|---|---:|---:|---:|---:|---:|
| `CPMK-1` / `CPL-08` | 20% | — | — | — | 20% |
| `CPMK-2` / `CPL-08` | — | 25% | — | — | 25% |
| `CPMK-3` / `CPL-13` | — | — | 25% | — | 25% |
| `CPMK-4` / `CPL-13` | — | — | — | 30% | 30% |
| **Total nilai MK** | **20%** | **25%** | **25%** | **30%** | **100%** |

| Instrumen | Kriteria dan bobot di dalam instrumen | Bukti minimal |
|---|---|---|
| **Tugas 1 — HTML** | Struktur dan semantik 35%; kelengkapan konten, tabel dan tautan 25%; formulir dan label 25%; kerapian berkas 15%. | Berkas HTML, aset lokal berizin, dan daftar pengecekan elemen. |
| **UTS — CSS, Flexbox dan pengenalan framework** | Selektor dan box model 20%; properti Flexbox container/item 35%; responsivitas dua ukuran layar 25%; pengenalan kelas Bootstrap dan Tailwind 20%. | Halaman dan stylesheet, tangkapan dua ukuran layar, serta latihan kelas dasar kedua framework. |
| **Tugas 2 — kalkulator** | Operasi aritmetika dan logika JS 30%; DOM dan event 20%; penanganan input dan pembagi nol 20%; penggunaan kelas Bootstrap atau Tailwind 15%; kode dan hasil uji 15%. | Berkas kalkulator dan tabel uji operasi, input kosong serta pembagi nol. |
| **UAS — landing page** | Struktur HTML dan konten 20%; CSS/Flexbox dan responsivitas 25%; interaksi JavaScript dasar 20%; pengujian dan perbaikan 20%; dokumentasi dan demonstrasi individual 15%. | Landing page lokal, petunjuk menjalankan, kasus uji dengan hasil, dan demonstrasi. |

Setiap kriteria dinilai 0–100; skor instrumen adalah jumlah nilai kriteria dikalikan bobotnya. **Nilai akhir MK** = (20 × skor Tugas 1 + 25 × skor UTS + 25 × skor Tugas 2 + 30 × skor UAS) / 100. Bukti CPMK diambil dari instrumen utama masing-masing; agregasi ketercapaian CPL lintas MK tetap mengikuti Dokumen 008 dan kebijakan prodi, bukan sekadar menjumlahkan 45% dan 55% sebagai nilai CPL.

Tugas 1, Tugas 2, dan UAS direncanakan berbasis kasus/proyek (75% bobot); kalkulator dan landing page adalah dua proyek berbeda. Jika dikerjakan berkelompok, simpan bukti kontribusi dan lakukan demonstrasi/pertanyaan individual. Realisasi metode aktif dan aturan penilaian harus diverifikasi oleh pengampu.

---

## 7. Dampak perubahan dan langkah validasi

| Dokumen / MK terdampak | Tindak lanjut setelah usulan disetujui |
|---|---|
| Dokumen 043 induk dan varian/ekstraksi 043 | Telah diselaraskan; riwayat sebelumnya tersedia di Git. Pengesahan tetap diperlukan. |
| Dokumen 007 dan 037 | Silabus dan batas STI-311 telah diselaraskan; validasi prodi diperlukan. |
| `PERANGKAT_AJAR/065_1`–`065_5` | Telah diselaraskan dengan rancangan baru; pengesahan dosen dan prodi masih diperlukan. |
| `STI-416`, `STI-522`, `STC-701` dan MK hilir lain | Audit asumsi prasyarat, materi, waktu dan asesmen. Tentukan secara eksplisit apakah materi yang dihapus perlu diajarkan pada MK lanjutan atau kegiatan pengayaan terpisah. Jangan menetapkan penambahan beban sebagai keputusan otomatis. |
| Koordinator RMK / prodi | Tinjau kesesuaian kontribusi CPL dan tingkat IRM, kelayakan SKS dan materi termasuk pengenalan dua framework, asesmen serta konsekuensi kurikuler; catat keputusan dan tanggal pengesahan. |

## 8. Sumber

1. [`043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md`](043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md), bagian `STI-311` — sumber awal yang disederhanakan.
2. [`043_STI-311_WEB_FRONT_END_DEVELOPMENT_30092026.md`](043_STI-311_WEB_FRONT_END_DEVELOPMENT_30092026.md) — ekstraksi yang diperbarui; versi historis tersedia pada Git.
3. [`003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md`](003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md), [`004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md`](004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md), dan [`005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md`](005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md) — identitas dan CPL.
4. [`007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md`](007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md), [`008_SISTEM_ASESMEN_OBE_FORMULA_CPL_DAN_RUBRIK_MASTER.md`](008_SISTEM_ASESMEN_OBE_FORMULA_CPL_DAN_RUBRIK_MASTER.md), [`037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md`](037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md) dan [`PERANGKAT_AJAR/README.md`](PERANGKAT_AJAR/README.md) — acuan pembanding dan konvensi beban/asesmen.
5. MDN Web Docs: [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout), dan [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript). Gunakan bagian yang sesuai batas di atas.
6. Dokumentasi resmi [Bootstrap](https://getbootstrap.com/docs/) dan [Tailwind CSS](https://tailwindcss.com/docs/) — pengenalan komponen/utilitas dasar; versi stylesheet dan cara penyiapan lokal ditetapkan pengampu.
