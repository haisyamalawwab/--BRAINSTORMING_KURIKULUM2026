# 043 — STI-311 PENGEMBANGAN WEB FRONT END

> Ekstraksi awal 30 September 2026 direvisi 7 November 2026; isi berikut bukan lagi ekstraksi verbatim historis. Lihat riwayat Git untuk versi sebelumnya. Pengesahan prodi masih diperlukan.

#### STI-311 — Web Front End Development
* **Beban / Tipe / Prasyarat:** Semester 3 / 3 SKS / +P / Prasyarat: `FST-102`
* **CPL yang Dibebankan:** `CPL-08` (`P4`), `CPL-13` (`KK5`); IRM R
* **Body of Knowledge (BoK):** `BK-IS12` *Web and Mobile Application Development*, `BK-IT04` *Platform Technologies*

**Formulasi CPMK (format ABCD dan Bloom):**

| Kode | Rumusan usulan: mahasiswa (A) | Bloom | CPL |
|---|---|:---:|---|
| `CPMK-1` | mampu **menyusun** halaman HTML dasar–menengah yang memuat struktur semantik, konten, tabel dan formulir (B) berdasarkan kebutuhan kasus yang diberikan (C), dengan struktur elemen, label dan tautan yang sesuai (D). | C3 | `CPL-08` (`P4`) |
| `CPMK-2` | mampu **menerapkan** CSS dasar–menengah dan Flexbox termasuk pengaturan flex item dan responsivitas (B) pada kasus antarmuka yang diberikan, serta mengenali penggunaan kelas Bootstrap dan Tailwind dasar (C), dengan tampilan rapi dan terbaca pada sedikitnya dua ukuran layar (D). | C3 | `CPL-08` (`P4`) |
| `CPMK-3` | mampu **membangun** kalkulator aritmetika sederhana (B) menggunakan JavaScript dasar dan styling **Bootstrap atau Tailwind CSS** (C), dengan operasi dan penanganan input sesuai kasus uji yang diberikan (D). | C3 | `CPL-13` (`KK5`) |
| `CPMK-4` | mampu **membangun dan menguji** landing page responsif dengan interaksi sederhana (B) menggunakan HTML, CSS dan JavaScript dasar, dengan Bootstrap atau Tailwind sebagai pilihan (C), serta mendokumentasikan navigasi, interaksi dan hasil pengujian (D). | C6 | `CPL-13` (`KK5`) |

**Sub-CPMK:**

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

**Rencana 16 pertemuan dan asesmen:**

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

**Boundary Guardrails:**

* 🟢 **IN-SCOPE:** HTML dan CSS dasar–menengah; Flexbox lanjutan; responsivitas; pengenalan Bootstrap dan Tailwind; JavaScript dasar, DOM dan event; kalkulator serta landing page.
* ❌ **OUT-OF-SCOPE:** React/Vue dan SPA; Fetch, async/await dan integrasi API; backend, database, pipeline build, optimasi produksi dan Lighthouse sebagai target.
* 🔄 **HANDOFF:** dasar antarmuka responsif dan interaktif; `STI-416` mengajarkan rekayasa backend dan konsep komunikasi HTTP. Kemampuan integrasi klien/API dan framework JavaScript belum dijamin, sehingga perlu keputusan prodi untuk penempatan dan sumber daya.

---
