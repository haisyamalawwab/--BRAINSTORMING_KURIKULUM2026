# 065_4 — RENCANA EVALUASI DAN ASESMEN

## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Identitas:** `STI-311` Pengembangan Web Front End (*Web Front End Development*) · Core STI · Semester 3 · 3 SKS (+P, 2T+1P) · Prasyarat `FST-102` Algoritma dan Pemrograman.

> **Revisi 7 November 2026 — rancangan:** diselaraskan dengan Dok 005 dan dokumen turunan 043; belum disahkan koordinator atau prodi. Tidak mengubah identitas/SKS/prasyarat.

## Pemetaan dan bobot

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

## Rencana tugas dan proyek

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

### Tugas 1 — HTML (minggu 4, 20%, CPMK-1)

Buat halaman informasi berisi struktur semantik, navigasi, gambar berizin dan alt, daftar, tabel, serta formulir berlabel. Kumpulkan berkas dan cek tautan/label. CSS yang dipelajari minggu ini tidak dinilai pada Tugas 1.

### UTS — CSS/Flexbox (minggu 8, 25%, CPMK-2)

Pada HTML yang disediakan, terapkan selektor, box model, Flexbox dan media query untuk dua ukuran layar. Selesaikan latihan singkat mengenali atau menggunakan kelas dasar pada kedua framework. Bukti berupa berkas dan tangkapan kedua ukuran layar.

### Tugas 2 dan UAS

Ketentuan, kasus uji dan bukti kalkulator (minggu 12, 25%, CPMK-3) dan landing page (minggu 16, 30%, CPMK-4) tercantum di atas. Semua kriteria berbobot pada 065_5; pengumpulan disertai penjelasan individual.

## Ketercapaian dan tindak lanjut

Skor CPMK berasal dari instrumen yang dipetakan. Rekap skor, umpan balik dan perbaikan menggunakan Dok 008; keputusan remedial dan batas ketuntasan mengikuti peraturan prodi. Rencana kasus/proyek 75% membutuhkan bukti metode aktif, bukan otomatis klaim realisasi IKU.

## Lingkup dan fasilitas

**Dalam lingkup:** HTML/CSS dasar–menengah, Flexbox lanjutan, Bootstrap dan Tailwind CSS dasar, JavaScript dasar dan DOM/event, proyek kalkulator dan landing page. **Di luar lingkup:** React/Vue/SPA, Fetch/asinkron/API, backend, database dan build pipeline. Validasi klien bukan keamanan server; data harus dummy atau berizin.

Gunakan editor dan browser; dosen menyiapkan CSS Bootstrap dan stylesheet Tailwind dengan semua kelas yang dipakai agar latihan dapat dijalankan tanpa internet, Node.js atau konfigurasi build. Pengenalan dilakukan pada kedua framework; kalkulator memakai salah satu.
