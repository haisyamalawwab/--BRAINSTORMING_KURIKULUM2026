# 065_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Identitas:** `STI-311` Pengembangan Web Front End (*Web Front End Development*) · Core STI · Semester 3 · 3 SKS (+P, 2T+1P) · Prasyarat `FST-102` Algoritma dan Pemrograman.

> **Revisi 7 November 2026 — rancangan:** diselaraskan dengan Dok 005 dan dokumen turunan 043; belum disahkan koordinator atau prodi. Tidak mengubah identitas/SKS/prasyarat.

## Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Pengampu, koordinator dan tanggal pengesahan diisi setelah peninjauan prodi. PL-3; PEO-1 dan PEO-2; BoK `BK-IS12`, `BK-IT04`.

Beban per pekan pembelajaran: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit = 510 menit; 270 menit pertama adalah tatap muka dan praktik. Pekan ujian mengikuti jadwal lembaga.

## CPL dibebankan

| CPL dibebankan | Rumusan resmi Dok 003 | IRM |
|---|---|---|
| `CPL-08` (`P4`) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | R |
| `CPL-13` (`KK5`) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | R |

Kontribusi pada CPL-13 terbatas pada dasar web, tidak mengklaim penguasaan keseluruhan platform skalabel.

## CPMK dan Sub-CPMK

| Kode | Rumusan usulan: mahasiswa (A) | Bloom | CPL |
|---|---|:---:|---|
| `CPMK-1` | mampu **menyusun** halaman HTML dasar–menengah yang memuat struktur semantik, konten, tabel dan formulir (B) berdasarkan kebutuhan kasus yang diberikan (C), dengan struktur elemen, label dan tautan yang sesuai (D). | C3 | `CPL-08` (`P4`) |
| `CPMK-2` | mampu **menerapkan** CSS dasar–menengah dan Flexbox termasuk pengaturan flex item dan responsivitas (B) pada kasus antarmuka yang diberikan, serta mengenali penggunaan kelas Bootstrap dan Tailwind dasar (C), dengan tampilan rapi dan terbaca pada sedikitnya dua ukuran layar (D). | C3 | `CPL-08` (`P4`) |
| `CPMK-3` | mampu **membangun** kalkulator aritmetika sederhana (B) menggunakan JavaScript dasar dan styling **Bootstrap atau Tailwind CSS** (C), dengan operasi dan penanganan input sesuai kasus uji yang diberikan (D). | C3 | `CPL-13` (`KK5`) |
| `CPMK-4` | mampu **membangun dan menguji** landing page responsif dengan interaksi sederhana (B) menggunakan HTML, CSS dan JavaScript dasar, dengan Bootstrap atau Tailwind sebagai pilihan (C), serta mendokumentasikan navigasi, interaksi dan hasil pengujian (D). | C6 | `CPL-13` (`KK5`) |

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

## Rencana 16 pertemuan

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

## Evaluasi dan pemetaan

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

## Lingkup dan fasilitas

**Dalam lingkup:** HTML/CSS dasar–menengah, Flexbox lanjutan, Bootstrap dan Tailwind CSS dasar, JavaScript dasar dan DOM/event, proyek kalkulator dan landing page. **Di luar lingkup:** React/Vue/SPA, Fetch/asinkron/API, backend, database dan build pipeline. Validasi klien bukan keamanan server; data harus dummy atau berizin.

Gunakan editor dan browser; dosen menyiapkan CSS Bootstrap dan stylesheet Tailwind dengan semua kelas yang dipakai agar latihan dapat dijalankan tanpa internet, Node.js atau konfigurasi build. Pengenalan dilakukan pada kedua framework; kalkulator memakai salah satu.

## Pustaka

[HTML MDN](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS MDN](https://developer.mozilla.org/en-US/docs/Web/CSS), [Flexbox MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout), [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Bootstrap](https://getbootstrap.com/docs/), [Tailwind CSS](https://tailwindcss.com/docs/).

Rujukan kurikulum: Dok 003/004/005/007/008/018/037/043 dan dokumen turunan 043 STI-311. Rincian tugas dan rubrik pada 065_4 dan 065_5.
