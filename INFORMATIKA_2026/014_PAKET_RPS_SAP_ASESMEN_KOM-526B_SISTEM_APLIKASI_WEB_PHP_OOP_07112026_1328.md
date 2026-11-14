# 014 — Paket bahan RPS, SAP, modul dan asesmen Informatika

## KOM-526b — Sistem Aplikasi Web PHP OOP

> **DRAF [U] — belum disahkan.** Bahan siap ditinjau untuk penyusunan RPS dan perangkat ajar, bukan dokumen pelaksanaan resmi. Identitas MK/CPL/BK bertanda [S] bersumber dari UWG; CPMK, Sub-CPMK, jadwal, instrumen, bobot, teknologi dan kasus adalah usulan. [K] memerlukan konfirmasi. Sumber kerja: [010](<010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md>), [009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) dan buku KPT Teknik Informatika sebagaimana daftar 010; contoh struktur [PERANGKAT_AJAR STI-311](../KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md) tidak menjadi sumber aturan TI.

## 1. RPS — identitas dan otorisasi

| Komponen | Isian / status |
|---|---|
| Institusi / program studi | Universitas Widyagama Malang / S1 Teknik Informatika [S]; nama fakultas pada RPS [K]. |
| MK / kode resmi | Sistem Aplikasi Web (+P); KOM-526; 3 SKS; semester 5 [S]. |
| Label jalur | KOM-526b — label usulan internal, **bukan kode KRS resmi** [U]. |
| Prasyarat | Formal **belum terverifikasi** [K]; usulan KOM-312 Pemrograman Web dan FST-207 Basis Data [U], tidak membatasi KRS sebelum keputusan prodi. |
| Teori / praktik / PT / BM | Belum ditetapkan [K]; `+P` tidak menentukan T/P. Skenario A/E di bawah hanya simulasi. |
| Tahun ajaran, kelas, rumpun, nomor dokumen | Belum ditetapkan [K]. |
| Pengembang, dosen, koordinator RMK, kaprodi, penjaminan mutu, tanggal / tanda tangan | Belum ditetapkan [K]. |
| CPL dan BK | CPL04 [S]; BK Tabel 15: BK02–BK08 [S]. Pemetaan dan relevansi BK tambahan mengikuti catatan 010 bagian 4.1. |

**CPL04 [S]:** Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

**Deskripsi [U]:** Merancang kebutuhan/model data, membangun rute server dan CRUD, menerapkan autentikasi, peran dan validasi, serta mengintegrasikan dan menguji sistem web lokal. Jalur ini menerapkan PHP OOP.

**Fasilitas dan batas [U/K]:** Server dan database lokal, data dummy, runtime dan alat sesuai jalur; tidak menggunakan data/kredensial nyata. Lihat 010 bagian 13.2 untuk keamanan dasar dan batas produksi. Persiapan alat, versi, aksesibilitas, bahan offline dan ketersediaan disetujui pengampu. PT/BM serta moda dan durasi penugasan menunggu kebijakan prodi.

**Penempatan dan strategi jalur [U]:** Jalur 2 bagi mahasiswa yang pernah mempelajari dasar jalur 1 atau setaranya; OOP bukan prasyarat KRS resmi. Diagnostik dan dukungan sesuai 010 bagian 13.1A; tidak mengubah prasyarat formal/KRS.

### CPMK dan Sub-CPMK [U]

**Rumusan ABCD dan level Bloom [U].** Setiap capaian ditulis lengkap (Audience–Behaviour–Condition–Degree) dan diberi level Bloom C2–C6. Kerangka, kata kerja, bukti asesmen dan aturan konsistensinya ada di [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u). Penambahan kolom ini **tidak mengubah** bobot maupun lima cek instrumen.

**CPMK — rumusan ABCD dan level Bloom**

| Kode | Rumusan lengkap (A–D) dan level Bloom | Bloom |
|---|---|---|
| CPMK04.1 | Mahasiswa mampu **merancang** kebutuhan, alur dan model data (aktor, entitas dan relasi) untuk kasus sistem web yang disediakan, dengan minimal 4 dari 5 cek rancangan Tugas 1 terpenuhi. | C6 |
| CPMK04.2 | Mahasiswa mampu **mengimplementasikan** rute dan operasi CRUD server–basis data pada kasus yang diberikan, dengan minimal 4 dari 5 kasus UTS lulus. | C3 |
| CPMK04.3 | Mahasiswa mampu **menerapkan dan menguji** autentikasi, pembatasan akses berbasis peran dan validasi server dasar pada aplikasi latihan, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C4 |
| CPMK04.4 | Mahasiswa mampu **mengintegrasikan dan menguji** sistem web terintegrasi beserta dokumentasi hasil uji sesuai rancangan yang disepakati, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 |

| Kode | A — Audience | B — Behaviour | C — Condition | D — Degree |
|---|---|---|---|---|
| CPMK04.1 | Mahasiswa | merancang | untuk kasus sistem web yang disediakan | dengan minimal 4 dari 5 cek rancangan Tugas 1 terpenuhi |
| CPMK04.2 | Mahasiswa | mengimplementasikan | pada kasus yang diberikan | dengan minimal 4 dari 5 kasus UTS lulus |
| CPMK04.3 | Mahasiswa | menerapkan dan menguji | pada aplikasi latihan | dengan minimal 4 dari 5 kasus Tugas 2 lulus |
| CPMK04.4 | Mahasiswa | mengintegrasikan dan menguji | sesuai rancangan yang disepakati | dengan minimal 4 dari 5 cek UAS terpenuhi |

**Sub-CPMK — rumusan ABCD dan level Bloom**

| Kode | CPMK | A — Audience | B — Behaviour | C — Condition | Bloom |
|---|---|---|---|---|---|
| Sub-CPMK04.1.1 | CPMK04.1 | Sub-CPMK04.1.1 | Mahasiswa | mengklasifikasikan | sebelum menyusun kebutuhan yang dapat diuji | C2 |
| Sub-CPMK04.1.2 | CPMK04.1 | Sub-CPMK04.1.2 | Mahasiswa | merancang | untuk kasus sistem web yang disediakan | C6 |
| Sub-CPMK04.2.1 | CPMK04.2 | Sub-CPMK04.2.1 | Mahasiswa | mengimplementasikan | sesuai kasus yang diberikan | C3 |
| Sub-CPMK04.2.2 | CPMK04.2 | Sub-CPMK04.2.2 | Mahasiswa | menghubungkan | menggunakan data dummy | C3 |
| Sub-CPMK04.3.1 | CPMK04.3 | Sub-CPMK04.3.1 | Mahasiswa | menerapkan | pada aplikasi latihan | C3 |
| Sub-CPMK04.3.2 | CPMK04.3 | Sub-CPMK04.3.2 | Mahasiswa | menganalisis | lalu menerapkan validasi server dan kueri terparameter pada data masukan aplikasi | C4 |
| Sub-CPMK04.4.1 | CPMK04.4 | Sub-CPMK04.4.1 | Mahasiswa | mengintegrasikan | sesuai rancangan yang disepakati | C6 |
| Sub-CPMK04.4.2 | CPMK04.4 | Sub-CPMK04.4.2 | Mahasiswa | mengevaluasi | kemudian memilih prioritas perbaikan bersama pengampu | C5 |

### Peta evaluasi [U]

| CPMK | Instrumen / minggu | Bobot terhadap nilai akhir | CPL |
|---|---|---:|---|
| 04.1 | Tugas 1 / 4 | 20% | CPL04 |
| 04.2 | UTS / 8 | 25% | CPL04 |
| 04.3 | Tugas 2 / 12 | 25% | CPL04 |
| 04.4 | UAS / 16 | 30% | CPL04 |
| **Total** | | **100%** | |

Target usulan tiap CPMK ≥4 dari 5 cek instrumen, bukan ketentuan resmi. Kode CPMK/Sub-CPMK bersifat lokal per MK. Bobot instrumen bukan bobot CPL lintas MK.

### Rencana mingguan RPS — 8 kolom [U]

`A`: simulasi 100 menit tatap muka + 170 menit praktik **hanya jika** disetujui 2T+1P; `E`: usulan slot evaluasi sampai 270 menit, bukan tambahan A. T/P, PT/BM dan durasi E belum terverifikasi. Bobot hanya pada T1/UTS/T2/UAS. Kolom **Bloom** mengikuti level Sub-CPMK yang dinilai minggu tersebut (010 bagian 15); level bukan bobot tambahan. Pustaka sesuai daftar di bagian 5.

| Minggu | Sub-CPMK | Bloom | Indikator | Kriteria & teknik penilaian | Bentuk/metode dan waktu | Materi / kegiatan | Pustaka | Bobot |
|---:|---|---|---|---|---|---|---|---:|
| 1 | 04.1.1 | C2 | Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. | Observasi dan umpan balik formatif; tanpa bobot. | Diskusi, demonstrasi — A | Diagnostik web, sintaks PHP dan konsep kelas/objek; jalankan contoh kelas lokal. | R4, R10 | 0% |
| 2 | 04.1.1 | C2 | Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus, lokakarya — A | Aktor/kebutuhan inventaris; atribut, metode dan pembagian tanggung jawab kelas. | R4, R10 | 0% |
| 3 | 04.1.2 | C6 | Entitas, relasi dan contoh data konsisten dengan kebutuhan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik perancangan — A | Entitas/relasi kategori–barang dan usulan kelas model/repository. | R5, R10 | 0% |
| 4 | 04.1.1, 04.1.2, 04.2.1 | C6 | Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. | Lima cek instrumen; bukti dan rubrik bagian 4. | Presentasi, praktik — A | Presentasi Tugas 1; pengantar controller/endpoint dan siklus request. | R4, R5, R10 | 20% |
| 5 | 04.2.1 | C3 | Rute menerima permintaan dan memberi respons sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Kuliah, praktik — A | Controller/handler, request/response dan pemisahan view; autoload sederhana. | R4, R10 | 0% |
| 6 | 04.2.2 | C3 | Data dummy dapat dibuat dan dibaca melalui server dan database. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Repository PDO: koneksi terpisah dan operasi create/read terparameter. | R4, R5, R10 | 0% |
| 7 | 04.2.2 | C3 | Update/delete serta kondisi data tidak ditemukan diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji — A | Metode update/delete repository dan exception/not-found pada controller. | R4, R5, R10 | 0% |
| 8 | 04.2.1, 04.2.2 | C3 | Lima kasus CRUD dan data tidak ditemukan pada UTS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian praktik — E | UTS praktik: controller, repository PDO dan lima kasus CRUD/not-found. | R4, R5, R10 | 25% |
| 9 | 04.3.1 | C3 | Login valid/tidak valid dan logout dapat didemonstrasikan. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Kelas layanan autentikasi dengan password_hash/password_verify dan sesi. | R6, R10 | 0% |
| 10 | 04.3.1 | C3 | Peran yang tidak berwenang ditolak mengakses fitur terbatas. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus, praktik — A | Penjagaan peran admin/petugas dalam controller atau middleware sederhana. | R6, R10 | 0% |
| 11 | 04.3.2 | C4 | Input invalid ditolak server dan kueri menggunakan parameter. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji kasus — A | Validator dan repository: validasi server, binding, escape output dan token CSRF. | R5, R6, R10 | 0% |
| 12 | 04.3.1, 04.3.2 | C4 | Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Tugas 2: demonstrasi layanan autentikasi, peran dan validasi berbasis kelas. | R5, R6, R10 | 25% |
| 13 | 04.4.1 | C6 | Antarmuka, rute, data dan akses terhubung pada purwarupa. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik proyek — A | Integrasi controller, service/repository, view, data dan akses. | R4, R5, R6, R10 | 0% |
| 14 | 04.4.1 | C6 | Alur end-to-end menggunakan data dummy sesuai kebutuhan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, konsultasi — A | Penyelesaian alur dan penjelasan enkapsulasi serta tanggung jawab kelas. | R4, R5, R10 | 0% |
| 15 | 04.4.2 | C5 | Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. | Observasi dan umpan balik formatif; tanpa bobot. | Pengujian, umpan balik — A | Uji normal/gagal kelas dan alur aplikasi; cek CSRF pengayaan dan dokumentasi. | R4, R6, R10 | 0% |
| 16 | 04.4.1, 04.4.2 | C6 | Lima cek integrasi, akses, data dan dokumentasi UAS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian proyek — E | UAS: demonstrasi proyek OOP dan bukti lima cek integrasi. | R4, R5, R6, R10 | 30% |

## 2. SAP — Satuan Acara Pertemuan [U]

**Pola pelaksanaan:** pembuka—diagnostik singkat/prasyarat dan tujuan; inti—dosen memodelkan langkah atau memberi sumber, mahasiswa mempraktikkan kegiatan khusus pertemuan; penutup—uji indikator, berikan umpan balik, catat hambatan dan perbaikan. Distribusi menit per fase, PT dan BM **belum ditetapkan**; tidak menambah durasi A/E. Untuk minggu evaluasi gunakan sesi ujian, bukan kegiatan materi tambahan. Bukti formatif tidak menambah nilai sumatif. Rencana berikut merupakan SAP pertemuan siap dikembangkan, bukan modul berisi naskah lengkap.

### Pertemuan 1 — 04.1.1

**Waktu/metode:** A / Diskusi, demonstrasi. **Materi:** Diagnostik web, sintaks PHP dan konsep kelas/objek; jalankan contoh kelas lokal.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Diagnostik web, sintaks PHP dan konsep kelas/objek; jalankan contoh kelas lokal. **Penutup:** Periksa indikator: Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Diagnostik, pengayaan bahasa dan bukti lingkungan. **Rujukan:** R4, R10.

### Pertemuan 2 — 04.1.1

**Waktu/metode:** A / Studi kasus, lokakarya. **Materi:** Aktor/kebutuhan inventaris; atribut, metode dan pembagian tanggung jawab kelas.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Aktor/kebutuhan inventaris; atribut, metode dan pembagian tanggung jawab kelas. **Penutup:** Periksa indikator: Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Aktor dan kebutuhan awal. **Rujukan:** R4, R10.

### Pertemuan 3 — 04.1.2

**Waktu/metode:** A / Praktik perancangan. **Materi:** Entitas/relasi kategori–barang dan usulan kelas model/repository.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Entitas/relasi kategori–barang dan usulan kelas model/repository. **Penutup:** Periksa indikator: Entitas, relasi dan contoh data konsisten dengan kebutuhan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Diagram/model data dan jejak kebutuhan. **Rujukan:** R5, R10.

### Pertemuan 4 — 04.1.1, 04.1.2, 04.2.1

**Waktu/metode:** A / Presentasi, praktik. **Materi:** Presentasi Tugas 1; pengantar controller/endpoint dan siklus request.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Presentasi Tugas 1; pengantar controller/endpoint dan siklus request. **Penutup:** Periksa indikator: Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 1: 20% — CPMK04.1.** **Rujukan:** R4, R5, R10. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 5 — 04.2.1

**Waktu/metode:** A / Kuliah, praktik. **Materi:** Controller/handler, request/response dan pemisahan view; autoload sederhana.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Controller/handler, request/response dan pemisahan view; autoload sederhana. **Penutup:** Periksa indikator: Rute menerima permintaan dan memberi respons sesuai kasus. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti request dan respons. **Rujukan:** R4, R10.

### Pertemuan 6 — 04.2.2

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Repository PDO: koneksi terpisah dan operasi create/read terparameter.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Repository PDO: koneksi terpisah dan operasi create/read terparameter. **Penutup:** Periksa indikator: Data dummy dapat dibuat dan dibaca melalui server dan database. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti create/read menggunakan data dummy. **Rujukan:** R4, R5, R10.

### Pertemuan 7 — 04.2.2

**Waktu/metode:** A / Praktik, uji. **Materi:** Metode update/delete repository dan exception/not-found pada controller.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Metode update/delete repository dan exception/not-found pada controller. **Penutup:** Periksa indikator: Update/delete serta kondisi data tidak ditemukan diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti update/delete dan not-found. **Rujukan:** R4, R5, R10.

### Pertemuan 8 — 04.2.1, 04.2.2

**Waktu/metode:** E / Ujian praktik. **Materi:** UTS praktik: controller, repository PDO dan lima kasus CRUD/not-found.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UTS: 25% — CPMK04.2.** **Rujukan:** R4, R5, R10. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 9 — 04.3.1

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Kelas layanan autentikasi dengan password_hash/password_verify dan sesi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Kelas layanan autentikasi dengan password_hash/password_verify dan sesi. **Penutup:** Periksa indikator: Login valid/tidak valid dan logout dapat didemonstrasikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti login/logout dengan data dummy. **Rujukan:** R6, R10.

### Pertemuan 10 — 04.3.1

**Waktu/metode:** A / Studi kasus, praktik. **Materi:** Penjagaan peran admin/petugas dalam controller atau middleware sederhana.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Penjagaan peran admin/petugas dalam controller atau middleware sederhana. **Penutup:** Periksa indikator: Peran yang tidak berwenang ditolak mengakses fitur terbatas. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti uji dua peran. **Rujukan:** R6, R10.

### Pertemuan 11 — 04.3.2

**Waktu/metode:** A / Praktik, uji kasus. **Materi:** Validator dan repository: validasi server, binding, escape output dan token CSRF.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Validator dan repository: validasi server, binding, escape output dan token CSRF. **Penutup:** Periksa indikator: Input invalid ditolak server dan kueri menggunakan parameter. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti validasi, parameterisasi dan penjelasan kontrol. **Rujukan:** R5, R6, R10.

### Pertemuan 12 — 04.3.1, 04.3.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Tugas 2: demonstrasi layanan autentikasi, peran dan validasi berbasis kelas.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Tugas 2: demonstrasi layanan autentikasi, peran dan validasi berbasis kelas. **Penutup:** Periksa indikator: Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 2: 25% — CPMK04.3.** **Rujukan:** R5, R6, R10. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 13 — 04.4.1

**Waktu/metode:** A / Praktik proyek. **Materi:** Integrasi controller, service/repository, view, data dan akses.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Integrasi controller, service/repository, view, data dan akses. **Penutup:** Periksa indikator: Antarmuka, rute, data dan akses terhubung pada purwarupa. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Purwarupa terintegrasi. **Rujukan:** R4, R5, R6, R10.

### Pertemuan 14 — 04.4.1

**Waktu/metode:** A / Praktik, konsultasi. **Materi:** Penyelesaian alur dan penjelasan enkapsulasi serta tanggung jawab kelas.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Penyelesaian alur dan penjelasan enkapsulasi serta tanggung jawab kelas. **Penutup:** Periksa indikator: Alur end-to-end menggunakan data dummy sesuai kebutuhan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Alur kasus dan penjelasan kode. **Rujukan:** R4, R5, R10.

### Pertemuan 15 — 04.4.2

**Waktu/metode:** A / Pengujian, umpan balik. **Materi:** Uji normal/gagal kelas dan alur aplikasi; cek CSRF pengayaan dan dokumentasi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Uji normal/gagal kelas dan alur aplikasi; cek CSRF pengayaan dan dokumentasi. **Penutup:** Periksa indikator: Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Hasil uji, temuan, perbaikan dan petunjuk lokal. **Rujukan:** R4, R6, R10.

### Pertemuan 16 — 04.4.1, 04.4.2

**Waktu/metode:** E / Ujian proyek. **Materi:** UAS: demonstrasi proyek OOP dan bukti lima cek integrasi.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UAS: 30% — CPMK04.4.** **Rujukan:** R4, R5, R6, R10. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

**Perangkat rinci:** [outline modul](024_OUTLINE_MODUL_KOM-526B_07112026_1332.md) · [rencana evaluasi dan asesmen](025_RENCANA_EVALUASI_ASESMEN_KOM-526B_07112026_1332.md) · [rubrik penilaian](026_RUBRIK_PENILAIAN_KOM-526B_07112026_1332.md).

## 3. Outline modul dan praktikum — 14 topik [U]

Topik mengikuti pertemuan pembelajaran selain UTS dan UAS; pertemuan 4 dan 12 tetap memuat T1/T2. Kolom Bloom mengikuti level Sub-CPMK minggu tersebut atau level CPMK pada minggu instrumen (010 bagian 15). Sumber mengikuti bagian 5; isi modul lengkap dan aksesibilitas perlu disiapkan pengampu.

| Modul | Pekan | Materi/pengalaman | Latihan dan bukti | Bloom | Rujukan |
|---:|---:|---|---|---|---|
| 1 | 1 | Diagnostik web, sintaks PHP dan konsep kelas/objek; jalankan contoh kelas lokal. | Diagnostik, pengayaan bahasa dan bukti lingkungan. | C2 | R4, R10 |
| 2 | 2 | Aktor/kebutuhan inventaris; atribut, metode dan pembagian tanggung jawab kelas. | Aktor dan kebutuhan awal. | C2 | R4, R10 |
| 3 | 3 | Entitas/relasi kategori–barang dan usulan kelas model/repository. | Diagram/model data dan jejak kebutuhan. | C6 | R5, R10 |
| 4 | 4 | Presentasi Tugas 1; pengantar controller/endpoint dan siklus request. | **Tugas 1: 20% — CPMK04.1.** | C6 | R4, R5, R10 |
| 5 | 5 | Controller/handler, request/response dan pemisahan view; autoload sederhana. | Bukti request dan respons. | C3 | R4, R10 |
| 6 | 6 | Repository PDO: koneksi terpisah dan operasi create/read terparameter. | Bukti create/read menggunakan data dummy. | C3 | R4, R5, R10 |
| 7 | 7 | Metode update/delete repository dan exception/not-found pada controller. | Bukti update/delete dan not-found. | C3 | R4, R5, R10 |
| 8 | 9 | Kelas layanan autentikasi dengan password_hash/password_verify dan sesi. | Bukti login/logout dengan data dummy. | C3 | R6, R10 |
| 9 | 10 | Penjagaan peran admin/petugas dalam controller atau middleware sederhana. | Bukti uji dua peran. | C3 | R6, R10 |
| 10 | 11 | Validator dan repository: validasi server, binding, escape output dan token CSRF. | Bukti validasi, parameterisasi dan penjelasan kontrol. | C4 | R5, R6, R10 |
| 11 | 12 | Tugas 2: demonstrasi layanan autentikasi, peran dan validasi berbasis kelas. | **Tugas 2: 25% — CPMK04.3.** | C4 | R5, R6, R10 |
| 12 | 13 | Integrasi controller, service/repository, view, data dan akses. | Purwarupa terintegrasi. | C6 | R4, R5, R6, R10 |
| 13 | 14 | Penyelesaian alur dan penjelasan enkapsulasi serta tanggung jawab kelas. | Alur kasus dan penjelasan kode. | C6 | R4, R5, R10 |
| 14 | 15 | Uji normal/gagal kelas dan alur aplikasi; cek CSRF pengayaan dan dokumentasi. | Hasil uji, temuan, perbaikan dan petunjuk lokal. | C5 | R4, R6, R10 |

## 4. Rencana evaluasi, instrumen dan rubrik [U]

**Kasus contoh:** inventaris peralatan dummy dengan kategori–barang berelasi (nama dan stok); admin mengelola dan petugas membaca. T1: minimal tiga kebutuhan teruji, dua entitas berelasi dan keterlacakan. UTS dalam lingkungan terisolasi: buat, baca, ubah stok, hapus dan minta ID yang tidak ada; autentikasi belum dinilai. T2: login admin valid, sandi salah, petugas ditolak mengubah, logout browser saat ini, stok negatif ditolak server dan kueri input terparameter. UAS: integrasi dan uji alur normal/gagal. Rincian dan batas keamanan pada 010 bagian 13.2–13.3.

**Kondisi jalur untuk UTS/T2/UAS:** Handler/controller dan repository berbasis kelas PHP/PDO digunakan dalam alur yang sedang diuji; cek akses dibuktikan pada aplikasi OOP. Ini kondisi cek terkait, bukan butir nilai tambahan; T1 tidak mensyaratkan kode. Rincian keamanan dan lima skenario: 010 bagian 13.2–13.3.

### Tugas 1, pekan 4 — 04.1 / 20%

**Instruksi:** Rancang kebutuhan dan model data untuk kasus sistem yang disediakan; serahkan aktor, kebutuhan, alur, entitas/relasi dan keterlacakan rancangan.

**Serahkan:** Dokumen kebutuhan, alur, model data dan penjelasan individu. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | aktor dan peran teridentifikasi. | Diisi penilai | — | — |
| 2 | minimal tiga kebutuhan dapat diuji. | Diisi penilai | — | — |
| 3 | alur utama tergambar. | Diisi penilai | — | — |
| 4 | minimal dua entitas dan relasinya terdefinisi. | Diisi penilai | — | — |
| 5 | kebutuhan terhubung ke data/alur. | Diisi penilai | — | — |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi:** Implementasikan rute server dan CRUD pada database dummy; perlihatkan empat operasi serta penanganan data yang tidak ditemukan, disertai lima uji.

**Serahkan:** Server, database dummy dan hasil lima uji CRUD. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | create. | Diisi penilai | — | — |
| 2 | read. | Diisi penilai | — | — |
| 3 | update. | Diisi penilai | — | — |
| 4 | delete. | Diisi penilai | — | — |
| 5 | permintaan untuk data yang tidak ditemukan ditangani. | Diisi penilai | — | — |

### Tugas 2, pekan 12 — 04.3 / 25%

**Instruksi:** Terapkan login, logout, sesi/peran dan validasi server pada aplikasi latihan; gunakan kueri terparameter, data dummy, matriks peran dan lima uji.

**Serahkan:** Kode, matriks peran dan hasil uji; gunakan pustaka pengelolaan kata sandi yang aman dan data dummy. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | login valid. | Diisi penilai | — | — |
| 2 | login tidak valid ditolak. | Diisi penilai | — | — |
| 3 | akses peran tidak berwenang ditolak. | Diisi penilai | — | — |
| 4 | logout mengakhiri akses sesi. | Diisi penilai | — | — |
| 5 | masukan invalid ditolak server dan data diproses dengan kueri terparameter. | Diisi penilai | — | — |

### UAS, pekan 16 — 04.4 / 30%

**Instruksi:** Integrasikan antarmuka, server, data dan akses sesuai rancangan; serahkan aplikasi lokal, petunjuk, uji alur normal/gagal dan demonstrasi individu.

**Serahkan:** Aplikasi lokal, data dummy, hasil uji dan demonstrasi individu. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | alur sesuai rancangan terintegrasi. | Diisi penilai | — | — |
| 2 | data tersimpan dan terbaca. | Diisi penilai | — | — |
| 3 | pembatasan akses bekerja. | Diisi penilai | — | — |
| 4 | alur salah ditangani dan dicatat. | Diisi penilai | — | — |
| 5 | petunjuk lokal, hasil uji dan perbaikan tersedia. | Diisi penilai | — | — |

### Aturan rubrik, rekap dan tindak lanjut [U]

- Setiap cek bernilai **100** jika seluruh unsur terpenuhi dan bukti terverifikasi, atau **0** jika ada unsur gagal/tidak ditunjukkan. Setiap cek berbobot 20% dari skor instrumen. Butir gabungan mensyaratkan semua komponennya.
- Skor instrumen = `(cek1 + cek2 + cek3 + cek4 + cek5) / 5`; nilai akhir = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Contoh 100,100,100,100,0 → 80/100 dan target ≥4/5 tercapai; semua ini usulan.
- Untuk setiap cek catat kondisi/input, langkah, hasil diharapkan dan hasil aktual, bukti dan umpan balik. Tidak ada bobot tambahan untuk formatif. Untuk kelompok, pastikan demonstrasi/penjelasan individu.
- Rekap per CPMK: simpan skor instrumen terkait, jumlah cek lulus, hambatan dan perbaikan. Dosen meninjau pola kesulitan untuk CQI; remedial, ambang final, pengolahan CPL dan kelulusan menunggu kebijakan prodi. Jangan mengklaim capaian kelas sebelum ada data.

| Mahasiswa/identitas | T1 / cek lulus | UTS / cek lulus | T2 / cek lulus | UAS / cek lulus | Nilai akhir | Umpan balik / CQI |
|---|---|---|---|---|---|---|
| Diisi dosen | — | — | — | — | — | — |

## 5. Sumber dan kesiapan [U/K]

| Nomor | Pustaka | Keterangan |
|---|---|---|
| R4 | MDN, [Introduction to the server side](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction) — interaksi klien, server dan data. | Utama KOM-526 |
| R5 | [SQLite Documentation](https://www.sqlite.org/docs.html) — contoh basis data lokal dan referensi SQL; pengampu dapat mengganti sesuai DB yang dipilih. | Pendukung KOM-526 |
| R6 | OWASP, [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) dan [SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — autentikasi dan parameterisasi. | Pendukung KOM-526 |

- **R10 — PHP dasar dan PDO:** [PHP Manual: PDO](https://www.php.net/manual/en/book.pdo.php); [PHP Manual: Classes and Objects](https://www.php.net/manual/en/language.oop5.php). PDO memerlukan driver untuk database yang dipilih.

**R19 — Taksonomi Bloom dan ABCD:** Anderson & Krathwohl (eds.), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives* (Longman, 2001) untuk dimensi proses kognitif C1–C6; struktur ABCD mengikuti praktik penyusunan capaian OBE. Rujukan ini **usulan penyusun**, bukan daftar pustaka resmi prodi, dan pengampu perlu memverifikasi edisi serta ketersediaannya. Penerapan ada pada [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u).

**Sebelum finalisasi:** periksa buku KPT/RPS atau workbook terkait, CPL/BK dan kode jalur; tetapkan dosen, tahun, format, prasyarat formal, T/P, PT/BM dan durasi evaluasi; tinjau kesiapan alat, akses dan instrumen bersama RMK; lengkapi identitas/pengesahan dan kebijakan remedial/CQI. Periksa 010 bagian 8–13. Tidak ada uji coba instrumen pada mahasiswa atau pengesahan akademik yang diklaim.
