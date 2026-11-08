# 065_3 — OUTLINE MODUL DAN PRAKTIKUM — 14 BAB

## STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)

**Identitas:** `STI-311` Pengembangan Web Front End (*Web Front End Development*) · Core STI · Semester 3 · 3 SKS (+P, 2T+1P) · Prasyarat `FST-102` Algoritma dan Pemrograman.

> **Revisi 7 November 2026 — rancangan:** diselaraskan dengan Dok 005 dan dokumen turunan 043; belum disahkan koordinator atau prodi. Tidak mengubah identitas/SKS/prasyarat.

Beban per pekan pembelajaran: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit = 510 menit; 270 menit pertama adalah tatap muka dan praktik. Pekan ujian mengikuti jadwal lembaga.

## Lingkup dan fasilitas

**Dalam lingkup:** HTML/CSS dasar–menengah, Flexbox lanjutan, Bootstrap dan Tailwind CSS dasar, JavaScript dasar dan DOM/event, proyek kalkulator dan landing page. **Di luar lingkup:** React/Vue/SPA, Fetch/asinkron/API, backend, database dan build pipeline. Validasi klien bukan keamanan server; data harus dummy atau berizin.

Gunakan editor dan browser; dosen menyiapkan CSS Bootstrap dan stylesheet Tailwind dengan semua kelas yang dipakai agar latihan dapat dijalankan tanpa internet, Node.js atau konfigurasi build. Pengenalan dilakukan pada kedua framework; kalkulator memakai salah satu.

Bab mengikuti pekan 1–7 dan 9–15; pekan 8 dan 16 untuk evaluasi. Setiap bab memuat konsep, latihan praktik, bukti dan refleksi.

### Bab 1 — HTML: dokumen, teks, heading dan daftar (pekan 1)

- **Materi:** Identifikasi doctype, html, head, body, hierarki heading serta daftar.
- **Praktikum:** Buat halaman profil dengan judul, paragraf dan dua jenis daftar; buka langsung pada browser.
- **Latihan & bukti:** Jelaskan perbedaan head dan body serta alasan urutan heading.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan HTML: dokumen, teks, heading dan daftar, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 2 — HTML semantik, tautan dan gambar (pekan 2)

- **Materi:** Bedakan header, nav, main, section dan footer; path relatif, atribut href, src dan alt.
- **Praktikum:** Buat navigasi ke bagian halaman dan tampilkan gambar berizin dengan alt bermakna.
- **Latihan & bukti:** Uji tautan dan jelaskan manfaat elemen semantik dan alt.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan HTML semantik, tautan dan gambar, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 3 — Tabel dan formulir HTML (pekan 3)

- **Materi:** Susun table dengan header, label dan input; gunakan tipe masukan dan validasi bawaan.
- **Praktikum:** Tambahkan tabel agenda dan formulir simulasi dengan label, required dan tombol.
- **Latihan & bukti:** Buktikan label terhubung dan validasi bawaan bekerja tanpa pengiriman data.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Tabel dan formulir HTML, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 4 — Tugas HTML dan pengantar CSS (pekan 4)

- **Materi:** Periksa HTML tugas; jelaskan stylesheet terpisah, selector, color dan font.
- **Praktikum:** Kumpulkan halaman HTML; setelah penilaian, hubungkan stylesheet dan ubah teks serta warna.
- **Latihan & bukti:** Tugas 1 dinilai hanya pada struktur/konten HTML, bukan pada CSS.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Tugas HTML dan pengantar CSS, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 5 — CSS dasar–menengah dan box model (pekan 5)

- **Materi:** Periksa cascade, spesifisitas dasar, ukuran, margin, padding, border, display dan position sederhana.
- **Praktikum:** Buat kartu informasi yang konsisten dan jelaskan perhitungan ruang padding, border dan margin.
- **Latihan & bukti:** Bandingkan aturan selector yang bersaing dan cek hasil pada browser.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan CSS dasar–menengah dan box model, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 6 — Flexbox dasar dan lanjutan (pekan 6)

- **Materi:** Bedakan sumbu; direction, justify-content, align-items, wrap, gap, align-content, grow/shrink/basis, align-self dan order.
- **Praktikum:** Buat navigasi dan kartu dengan wrap, grow/basis serta nested flex; bandingkan ukuran layar.
- **Latihan & bukti:** Jelaskan beda grow, shrink dan basis; pastikan urutan visual tidak merusak urutan baca.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Flexbox dasar dan lanjutan, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 7 — Responsivitas serta Bootstrap dan Tailwind dasar (pekan 7)

- **Materi:** Gunakan media query dan dua breakpoint; bedakan komponen Bootstrap dari utility Tailwind.
- **Praktikum:** Buat satu kartu Bootstrap dan satu kartu Tailwind dengan stylesheet siap pakai; uji dua lebar layar.
- **Latihan & bukti:** Identifikasi container/tombol Bootstrap dan utility spacing/responsive Tailwind.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Responsivitas serta Bootstrap dan Tailwind dasar, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 8 — JavaScript dasar dan operasi aritmetika (pekan 9)

- **Materi:** Hubungkan script; gunakan let/const, string, number, operator dan console.
- **Praktikum:** Tulis fungsi untuk empat operasi sederhana dengan angka contoh.
- **Latihan & bukti:** Jelaskan perbedaan teks angka dan nilai number.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan JavaScript dasar dan operasi aritmetika, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 9 — Percabangan, perulangan, fungsi dan array (pekan 10)

- **Materi:** Gunakan if/else, loop, function dan array sederhana; konversi nilai input.
- **Praktikum:** Bangun fungsi hitung yang menolak input kosong, nilai bukan angka dan pembagi nol.
- **Latihan & bukti:** Jalankan contoh valid dan tidak valid lalu jelaskan keluaran.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Percabangan, perulangan, fungsi dan array, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 10 — DOM dan event untuk kalkulator (pekan 11)

- **Materi:** Pilih elemen, baca value, gunakan addEventListener dan textContent untuk hasil.
- **Praktikum:** Hubungkan dua input, operasi dan tombol hitung/reset; style dengan Bootstrap atau Tailwind.
- **Latihan & bukti:** Uji klik, reset dan input tidak valid; hindari memasukkan HTML mentah dari input.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan DOM dan event untuk kalkulator, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 11 — Proyek kalkulator: penyelesaian dan uji (pekan 12)

- **Materi:** Uji empat operasi, reset dan penanganan kesalahan; cek tampilan dan styling framework.
- **Praktikum:** Selesaikan kalkulator, jalankan kasus uji, kumpulkan berkas dan demonstrasikan logika.
- **Latihan & bukti:** Tugas 2 dinilai pada fungsi, event, kesalahan, framework pilihan dan bukti uji.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Proyek kalkulator: penyelesaian dan uji, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 12 — Perencanaan landing page (pekan 13)

- **Materi:** Susun tujuan halaman, struktur semantik, hero, manfaat, CTA dan footer; pilih aset berizin.
- **Praktikum:** Buat sketsa dan kerangka HTML landing page untuk produk/kegiatan fiktif.
- **Latihan & bukti:** Cek hierarki heading, tautan dan atribut alt.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Perencanaan landing page, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 13 — Landing page responsif dan interaktif (pekan 14)

- **Materi:** Gunakan CSS/Flexbox dan media query; framework CSS opsional; satu interaksi JS sederhana.
- **Praktikum:** Tata layout pada dua lebar dan tambahkan menu buka/tutup atau tombol tampil pesan.
- **Latihan & bukti:** Uji fungsi tombol dan navigasi keyboard pada kedua ukuran layar.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Landing page responsif dan interaktif, dengan panah input–proses–hasil, tanpa data pribadi.

### Bab 14 — Uji dan penyempurnaan landing page (pekan 15)

- **Materi:** Susun uji navigasi, tampilan, interaksi, label dan akses keyboard; catat temuan.
- **Praktikum:** Jalankan uji, perbaiki hasil gagal dan tuliskan langkah menjalankan secara lokal.
- **Latihan & bukti:** Pastikan bukti uji mencantumkan hasil yang diharapkan dan aktual.
- **Studi kasus:** gunakan informasi dan aset berizin untuk profil organisasi, kalkulator, atau landing page sesuai konteks bab.
- **Prompt ilustrasi:** diagram edukasi berlabel bahasa Indonesia yang menjelaskan Uji dan penyempurnaan landing page, dengan panah input–proses–hasil, tanpa data pribadi.

## Pustaka

[HTML MDN](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS MDN](https://developer.mozilla.org/en-US/docs/Web/CSS), [Flexbox MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout), [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Bootstrap](https://getbootstrap.com/docs/), [Tailwind CSS](https://tailwindcss.com/docs/).
