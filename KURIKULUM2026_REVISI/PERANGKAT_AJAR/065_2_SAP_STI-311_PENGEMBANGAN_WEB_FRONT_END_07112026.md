# 065_2 — SATUAN ACARA PERKULIAHAN 16 PERTEMUAN

## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Identitas:** `STI-311` Pengembangan Web Front End (*Web Front End Development*) · Core STI · Semester 3 · 3 SKS (+P, 2T+1P) · Prasyarat `FST-102` Algoritma dan Pemrograman.

> **Revisi 7 November 2026 — rancangan:** diselaraskan dengan Dok 005 dan dokumen turunan 043; belum disahkan koordinator atau prodi. Tidak mengubah identitas/SKS/prasyarat.

Beban per pekan pembelajaran: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit = 510 menit; 270 menit pertama adalah tatap muka dan praktik. Pekan ujian mengikuti jadwal lembaga.

## Lingkup dan fasilitas

**Dalam lingkup:** HTML/CSS dasar–menengah, Flexbox lanjutan, Bootstrap dan Tailwind CSS dasar, JavaScript dasar dan DOM/event, proyek kalkulator dan landing page. **Di luar lingkup:** React/Vue/SPA, Fetch/asinkron/API, backend, database dan build pipeline. Validasi klien bukan keamanan server; data harus dummy atau berizin.

Gunakan editor dan browser; dosen menyiapkan CSS Bootstrap dan stylesheet Tailwind dengan semua kelas yang dipakai agar latihan dapat dijalankan tanpa internet, Node.js atau konfigurasi build. Pengenalan dilakukan pada kedua framework; kalkulator memakai salah satu.

## Skema kegiatan

Untuk minggu materi: teori 100 menit (pembuka 10, konsep/demonstrasi 45, diskusi 35, penutup 10) dan praktik 170 menit (orientasi 20, pengerjaan 120, verifikasi/umpan balik 30). PT dan BM di luar sesi; alokasi evaluasi mengikuti pengampu.

### Pertemuan 1 — HTML: dokumen, teks, heading dan daftar

**Capaian:** 1.1. **Materi:** Orientasi front-end; peran HTML/CSS/JS dan browser; struktur HTML, teks, heading dan daftar.

**Teori:** Identifikasi doctype, html, head, body, hierarki heading serta daftar. **Praktik:** Buat halaman profil dengan judul, paragraf dan dua jenis daftar; buka langsung pada browser.

**Penutup/pengecekan:** Jelaskan perbedaan head dan body serta alasan urutan heading. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: halaman profil HTML awal.

### Pertemuan 2 — HTML semantik, tautan dan gambar

**Capaian:** 1.1. **Materi:** HTML semantik: header, nav, main, section dan footer; tautan dan gambar dengan teks alternatif.

**Teori:** Bedakan header, nav, main, section dan footer; path relatif, atribut href, src dan alt. **Praktik:** Buat navigasi ke bagian halaman dan tampilkan gambar berizin dengan alt bermakna.

**Penutup/pengecekan:** Uji tautan dan jelaskan manfaat elemen semantik dan alt. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: halaman informasi dengan navigasi.

### Pertemuan 3 — Tabel dan formulir HTML

**Capaian:** 1.2. **Materi:** HTML menengah: tabel, formulir, label, input, tombol dan validasi HTML bawaan.

**Teori:** Susun table dengan header, label dan input; gunakan tipe masukan dan validasi bawaan. **Praktik:** Tambahkan tabel agenda dan formulir simulasi dengan label, required dan tombol.

**Penutup/pengecekan:** Buktikan label terhubung dan validasi bawaan bekerja tanpa pengiriman data. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: formulir simulasi dan tabel berstruktur.

### Pertemuan 4 — Tugas HTML dan pengantar CSS

**Capaian:** 1.1–1.2, 2.1. **Materi:** Review HTML dan **Tugas 1**; pengantar stylesheet, selektor, warna dan tipografi CSS. Penilaian Tugas 1 hanya pada HTML.

**Teori:** Periksa HTML tugas; jelaskan stylesheet terpisah, selector, color dan font. **Praktik:** Kumpulkan halaman HTML; setelah penilaian, hubungkan stylesheet dan ubah teks serta warna.

**Penutup/pengecekan:** Tugas 1 dinilai hanya pada struktur/konten HTML, bukan pada CSS. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** **Tugas 1 — 20%:** halaman HTML untuk kasus yang disepakati.

### Pertemuan 5 — CSS dasar–menengah dan box model

**Capaian:** 2.1. **Materi:** CSS dasar–menengah: cascade/spesifisitas dasar, box model, display, ukuran dan position sederhana.

**Teori:** Periksa cascade, spesifisitas dasar, ukuran, margin, padding, border, display dan position sederhana. **Praktik:** Buat kartu informasi yang konsisten dan jelaskan perhitungan ruang padding, border dan margin.

**Penutup/pengecekan:** Bandingkan aturan selector yang bersaing dan cek hasil pada browser. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: stylesheet dan tata letak kartu.

### Pertemuan 6 — Flexbox dasar dan lanjutan

**Capaian:** 2.2. **Materi:** Flexbox: sumbu, direction, alignment, wrap, gap; flex item grow/shrink/basis, align-self, order dan nested flex.

**Teori:** Bedakan sumbu; direction, justify-content, align-items, wrap, gap, align-content, grow/shrink/basis, align-self dan order. **Praktik:** Buat navigasi dan kartu dengan wrap, grow/basis serta nested flex; bandingkan ukuran layar.

**Penutup/pengecekan:** Jelaskan beda grow, shrink dan basis; pastikan urutan visual tidak merusak urutan baca. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: navigasi dan kartu responsif menggunakan Flexbox.

### Pertemuan 7 — Responsivitas serta Bootstrap dan Tailwind dasar

**Capaian:** 2.1–2.3. **Materi:** Media query dan latihan dua ukuran layar; pengenalan **Bootstrap** (container, tombol, kartu, grid dasar) dan **Tailwind** (spacing, warna, Flexbox, breakpoint dasar).

**Teori:** Gunakan media query dan dua breakpoint; bedakan komponen Bootstrap dari utility Tailwind. **Praktik:** Buat satu kartu Bootstrap dan satu kartu Tailwind dengan stylesheet siap pakai; uji dua lebar layar.

**Penutup/pengecekan:** Identifikasi container/tombol Bootstrap dan utility spacing/responsive Tailwind. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: komponen sederhana menggunakan masing-masing framework.

### Pertemuan 8 — UTS

**Capaian:** 2.1–2.3. **Materi:** Ujian praktik CSS/Flexbox responsif; pengenalan kelas Bootstrap dan Tailwind diuji melalui latihan singkat.

**Pembuka:** jelaskan petunjuk, kriteria, integritas akademik dan alat yang diperbolehkan. **Inti:** uji praktik CSS/Flexbox dan kelas dasar dua framework pada kasus yang disediakan. **Penutup:** kumpulkan berkas, bukti dan berikan umpan balik. **Evaluasi:** **UTS — 25%:** CSS/Flexbox, dua ukuran layar dan pemilihan kelas framework dasar.

### Pertemuan 9 — JavaScript dasar dan operasi aritmetika

**Capaian:** 3.1. **Materi:** JavaScript di browser: script, variabel, tipe data, operator aritmetika dan konsol.

**Teori:** Hubungkan script; gunakan let/const, string, number, operator dan console. **Praktik:** Tulis fungsi untuk empat operasi sederhana dengan angka contoh.

**Penutup/pengecekan:** Jelaskan perbedaan teks angka dan nilai number. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: operasi hitung dan keluaran sederhana.

### Pertemuan 10 — Percabangan, perulangan, fungsi dan array

**Capaian:** 3.1. **Materi:** Percabangan, perulangan, fungsi dan array sederhana; konversi input menjadi angka dan kondisi pembagi nol.

**Teori:** Gunakan if/else, loop, function dan array sederhana; konversi nilai input. **Praktik:** Bangun fungsi hitung yang menolak input kosong, nilai bukan angka dan pembagi nol.

**Penutup/pengecekan:** Jalankan contoh valid dan tidak valid lalu jelaskan keluaran. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: fungsi kalkulasi dengan contoh input valid/tidak valid.

### Pertemuan 11 — DOM dan event untuk kalkulator

**Capaian:** 3.2. **Materi:** DOM dan event: membaca input, tombol, menampilkan hasil dan pesan; terapkan kelas Bootstrap atau Tailwind pada rancangan kalkulator.

**Teori:** Pilih elemen, baca value, gunakan addEventListener dan textContent untuk hasil. **Praktik:** Hubungkan dua input, operasi dan tombol hitung/reset; style dengan Bootstrap atau Tailwind.

**Penutup/pengecekan:** Uji klik, reset dan input tidak valid; hindari memasukkan HTML mentah dari input. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: purwarupa kalkulator dengan styling framework pilihan.

### Pertemuan 12 — Proyek kalkulator: penyelesaian dan uji

**Capaian:** 3.1–3.2. **Materi:** Praktikum dan demonstrasi kalkulator dasar menggunakan JavaScript serta Bootstrap **atau** Tailwind CSS.

**Teori:** Uji empat operasi, reset dan penanganan kesalahan; cek tampilan dan styling framework. **Praktik:** Selesaikan kalkulator, jalankan kasus uji, kumpulkan berkas dan demonstrasikan logika.

**Penutup/pengecekan:** Tugas 2 dinilai pada fungsi, event, kesalahan, framework pilihan dan bukti uji. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** **Tugas 2 — 25%:** kalkulator dan hasil uji.

### Pertemuan 13 — Perencanaan landing page

**Capaian:** 4.1. **Materi:** Merencanakan landing page: struktur semantik, hero, manfaat/fitur, call-to-action dan footer; siapkan konten berizin.

**Teori:** Susun tujuan halaman, struktur semantik, hero, manfaat, CTA dan footer; pilih aset berizin. **Praktik:** Buat sketsa dan kerangka HTML landing page untuk produk/kegiatan fiktif.

**Penutup/pengecekan:** Cek hierarki heading, tautan dan atribut alt. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: sketsa dan kerangka HTML.

### Pertemuan 14 — Landing page responsif dan interaktif

**Capaian:** 4.1. **Materi:** Tata landing page responsif dengan CSS/Flexbox; Bootstrap atau Tailwind boleh digunakan. Tambahkan interaksi JS sederhana, misalnya menu atau tombol.

**Teori:** Gunakan CSS/Flexbox dan media query; framework CSS opsional; satu interaksi JS sederhana. **Praktik:** Tata layout pada dua lebar dan tambahkan menu buka/tutup atau tombol tampil pesan.

**Penutup/pengecekan:** Uji fungsi tombol dan navigasi keyboard pada kedua ukuran layar. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: purwarupa responsif dan interaktif.

### Pertemuan 15 — Uji dan penyempurnaan landing page

**Capaian:** 4.2. **Materi:** Uji navigasi, interaksi, keyboard dan tampilan; perbaiki masalah serta dokumentasikan hasil.

**Teori:** Susun uji navigasi, tampilan, interaksi, label dan akses keyboard; catat temuan. **Praktik:** Jalankan uji, perbaiki hasil gagal dan tuliskan langkah menjalankan secara lokal.

**Penutup/pengecekan:** Pastikan bukti uji mencantumkan hasil yang diharapkan dan aktual. **PT:** dokumentasikan hasil dan satu koreksi. **BM:** baca sumber terkait dan coba variasi input/layout. **Bukti:** Formatif: daftar kasus uji dan perbaikan.

### Pertemuan 16 — UAS

**Capaian:** 4.1–4.2. **Materi:** Demonstrasi landing page, penjelasan kode individual dan penyerahan berkas.

**Pembuka:** jelaskan petunjuk, kriteria, integritas akademik dan alat yang diperbolehkan. **Inti:** demonstrasi landing page, periksa uji dan tanyakan kode kepada setiap mahasiswa. **Penutup:** kumpulkan berkas, bukti dan berikan umpan balik. **Evaluasi:** **UAS — 30%:** landing page, dokumentasi dan demonstrasi.

## Sumber

[HTML MDN](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS MDN](https://developer.mozilla.org/en-US/docs/Web/CSS), [Flexbox MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout), [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Bootstrap](https://getbootstrap.com/docs/), [Tailwind CSS](https://tailwindcss.com/docs/).
