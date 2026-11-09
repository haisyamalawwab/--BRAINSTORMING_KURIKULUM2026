# 015 — Paket bahan RPS, SAP, modul dan asesmen Informatika

## KOM-526c — Sistem Aplikasi Web PHP Laravel

> **DRAF [U] — belum disahkan.** Bahan siap ditinjau untuk penyusunan RPS dan perangkat ajar, bukan dokumen pelaksanaan resmi. Identitas MK/CPL/BK bertanda [S] bersumber dari UWG; CPMK, Sub-CPMK, jadwal, instrumen, bobot, teknologi dan kasus adalah usulan. [K] memerlukan konfirmasi. Sumber kerja: [010](<010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md>), [009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) dan buku KPT Teknik Informatika sebagaimana daftar 010; contoh struktur [PERANGKAT_AJAR STI-311](../KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md) tidak menjadi sumber aturan TI.

## 1. RPS — identitas dan otorisasi

| Komponen | Isian / status |
|---|---|
| Institusi / program studi | Universitas Widyagama Malang / S1 Teknik Informatika [S]; nama fakultas pada RPS [K]. |
| MK / kode resmi | Sistem Aplikasi Web (+P); KOM-526; 3 SKS; semester 5 [S]. |
| Label jalur | KOM-526c — label usulan internal, **bukan kode KRS resmi** [U]. |
| Prasyarat | Formal **belum terverifikasi** [K]; usulan KOM-312 Pemrograman Web dan FST-207 Basis Data [U], tidak membatasi KRS sebelum keputusan prodi. |
| Teori / praktik / PT / BM | Belum ditetapkan [K]; `+P` tidak menentukan T/P. Skenario A/E di bawah hanya simulasi. |
| Tahun ajaran, kelas, rumpun, nomor dokumen | Belum ditetapkan [K]. |
| Pengembang, dosen, koordinator RMK, kaprodi, penjaminan mutu, tanggal / tanda tangan | Belum ditetapkan [K]. |
| CPL dan BK | CPL04 [S]; BK Tabel 15: BK02–BK08 [S]. Pemetaan dan relevansi BK tambahan mengikuti catatan 010 bagian 4.1. |

**CPL04 [S]:** Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

**Deskripsi [U]:** Merancang kebutuhan/model data, membangun rute server dan CRUD, menerapkan autentikasi, peran dan validasi, serta mengintegrasikan dan menguji sistem web lokal. Jalur ini menerapkan PHP LARAVEL.

**Fasilitas dan batas [U/K]:** Server dan database lokal, data dummy, runtime dan alat sesuai jalur; tidak menggunakan data/kredensial nyata. Lihat 010 bagian 13.2 untuk keamanan dasar dan batas produksi. Persiapan alat, versi, aksesibilitas, bahan offline dan ketersediaan disetujui pengampu. PT/BM serta moda dan durasi penugasan menunggu kebijakan prodi.

**Penempatan dan strategi jalur [U]:** Jalur 3 bagi mahasiswa yang pernah mempelajari dasar jalur 1 atau setaranya; jalur 2 bukan prasyarat. Diagnostik dan dukungan sesuai 010 bagian 13.1A; tidak mengubah prasyarat formal/KRS.

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
| 1 | 04.1.1 | C2 | Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. | Observasi dan umpan balik formatif; tanpa bobot. | Diskusi, demonstrasi — A | Diagnostik PHP/OOP dan Composer; orientasi proyek Laravel dan rute sederhana. | R4, R11 | 0% |
| 2 | 04.1.1 | C2 | Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus, lokakarya — A | Aktor/kebutuhan inventaris; konvensi controller, view dan struktur proyek. | R4, R11 | 0% |
| 3 | 04.1.2 | C6 | Entitas, relasi dan contoh data konsisten dengan kebutuhan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik perancangan — A | Model kategori–barang, relasi dan rancangan migration dari kebutuhan. | R5, R11 | 0% |
| 4 | 04.1.1, 04.1.2, 04.2.1 | C6 | Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. | Lima cek instrumen; bukti dan rubrik bagian 4. | Presentasi, praktik — A | Presentasi Tugas 1; pengantar route dan controller Laravel. | R4, R5, R11 | 20% |
| 5 | 04.2.1 | C3 | Rute menerima permintaan dan memberi respons sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Kuliah, praktik — A | Route web, controller, request/response dan Blade. | R4, R11 | 0% |
| 6 | 04.2.2 | C3 | Data dummy dapat dibuat dan dibaca melalui server dan database. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Konfigurasi database, migration dan Eloquent create/read. | R4, R5, R11 | 0% |
| 7 | 04.2.2 | C3 | Update/delete serta kondisi data tidak ditemukan diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji — A | Eloquent update/delete, validasi dasar dan penanganan not-found. | R4, R5, R11 | 0% |
| 8 | 04.2.1, 04.2.2 | C3 | Lima kasus CRUD dan data tidak ditemukan pada UTS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian praktik — E | UTS praktik: route/controller, Eloquent dan lima kasus CRUD/not-found. | R4, R5, R11 | 25% |
| 9 | 04.3.1 | C3 | Login valid/tidak valid dan logout dapat didemonstrasikan. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Fasilitas autentikasi Laravel atau starter kit pilihan; login/logout dan sesi. | R6, R11 | 0% |
| 10 | 04.3.1 | C3 | Peran yang tidak berwenang ditolak mengakses fitur terbatas. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus, praktik — A | Middleware/otorisasi peran admin dan petugas pada route/controller. | R6, R11 | 0% |
| 11 | 04.3.2 | C4 | Input invalid ditolak server dan kueri menggunakan parameter. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji kasus — A | Validasi Request, Eloquent/query builder dan CSRF pada Blade. | R5, R6, R11 | 0% |
| 12 | 04.3.1, 04.3.2 | C4 | Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Tugas 2: demonstrasi autentikasi, peran dan validasi dengan Laravel. | R5, R6, R11 | 25% |
| 13 | 04.4.1 | C6 | Antarmuka, rute, data dan akses terhubung pada purwarupa. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik proyek — A | Integrasi Blade, route, controller, model dan otorisasi. | R4, R5, R6, R11 | 0% |
| 14 | 04.4.1 | C6 | Alur end-to-end menggunakan data dummy sesuai kebutuhan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, konsultasi — A | Penyelesaian alur dan penjelasan kontribusi kode sendiri serta komponen framework. | R4, R5, R11 | 0% |
| 15 | 04.4.2 | C5 | Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. | Observasi dan umpan balik formatif; tanpa bobot. | Pengujian, umpan balik — A | Feature test atau uji terdokumentasi normal/gagal; cek CSRF pengayaan dan setup. | R4, R6, R11 | 0% |
| 16 | 04.4.1, 04.4.2 | C6 | Lima cek integrasi, akses, data dan dokumentasi UAS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian proyek — E | UAS: demonstrasi proyek Laravel dan bukti lima cek integrasi. | R4, R5, R6, R11 | 30% |

## 2. SAP — Satuan Acara Pertemuan [U]

**Pola pelaksanaan:** pembuka—diagnostik singkat/prasyarat dan tujuan; inti—dosen memodelkan langkah atau memberi sumber, mahasiswa mempraktikkan kegiatan khusus pertemuan; penutup—uji indikator, berikan umpan balik, catat hambatan dan perbaikan. Distribusi menit per fase, PT dan BM **belum ditetapkan**; tidak menambah durasi A/E. Untuk minggu evaluasi gunakan sesi ujian, bukan kegiatan materi tambahan. Bukti formatif tidak menambah nilai sumatif. Rencana berikut merupakan SAP pertemuan siap dikembangkan, bukan modul berisi naskah lengkap.

### Pertemuan 1 — 04.1.1

**Waktu/metode:** A / Diskusi, demonstrasi. **Materi:** Diagnostik PHP/OOP dan Composer; orientasi proyek Laravel dan rute sederhana.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Diagnostik PHP/OOP dan Composer; orientasi proyek Laravel dan rute sederhana. **Penutup:** Periksa indikator: Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Diagnostik, pengayaan bahasa dan bukti lingkungan. **Rujukan:** R4, R11.

### Pertemuan 2 — 04.1.1

**Waktu/metode:** A / Studi kasus, lokakarya. **Materi:** Aktor/kebutuhan inventaris; konvensi controller, view dan struktur proyek.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Aktor/kebutuhan inventaris; konvensi controller, view dan struktur proyek. **Penutup:** Periksa indikator: Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Aktor dan kebutuhan awal. **Rujukan:** R4, R11.

### Pertemuan 3 — 04.1.2

**Waktu/metode:** A / Praktik perancangan. **Materi:** Model kategori–barang, relasi dan rancangan migration dari kebutuhan.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Model kategori–barang, relasi dan rancangan migration dari kebutuhan. **Penutup:** Periksa indikator: Entitas, relasi dan contoh data konsisten dengan kebutuhan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Diagram/model data dan jejak kebutuhan. **Rujukan:** R5, R11.

### Pertemuan 4 — 04.1.1, 04.1.2, 04.2.1

**Waktu/metode:** A / Presentasi, praktik. **Materi:** Presentasi Tugas 1; pengantar route dan controller Laravel.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Presentasi Tugas 1; pengantar route dan controller Laravel. **Penutup:** Periksa indikator: Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 1: 20% — CPMK04.1.** **Rujukan:** R4, R5, R11. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 5 — 04.2.1

**Waktu/metode:** A / Kuliah, praktik. **Materi:** Route web, controller, request/response dan Blade.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Route web, controller, request/response dan Blade. **Penutup:** Periksa indikator: Rute menerima permintaan dan memberi respons sesuai kasus. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti request dan respons. **Rujukan:** R4, R11.

### Pertemuan 6 — 04.2.2

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Konfigurasi database, migration dan Eloquent create/read.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Konfigurasi database, migration dan Eloquent create/read. **Penutup:** Periksa indikator: Data dummy dapat dibuat dan dibaca melalui server dan database. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti create/read menggunakan data dummy. **Rujukan:** R4, R5, R11.

### Pertemuan 7 — 04.2.2

**Waktu/metode:** A / Praktik, uji. **Materi:** Eloquent update/delete, validasi dasar dan penanganan not-found.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Eloquent update/delete, validasi dasar dan penanganan not-found. **Penutup:** Periksa indikator: Update/delete serta kondisi data tidak ditemukan diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti update/delete dan not-found. **Rujukan:** R4, R5, R11.

### Pertemuan 8 — 04.2.1, 04.2.2

**Waktu/metode:** E / Ujian praktik. **Materi:** UTS praktik: route/controller, Eloquent dan lima kasus CRUD/not-found.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UTS: 25% — CPMK04.2.** **Rujukan:** R4, R5, R11. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 9 — 04.3.1

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Fasilitas autentikasi Laravel atau starter kit pilihan; login/logout dan sesi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Fasilitas autentikasi Laravel atau starter kit pilihan; login/logout dan sesi. **Penutup:** Periksa indikator: Login valid/tidak valid dan logout dapat didemonstrasikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti login/logout dengan data dummy. **Rujukan:** R6, R11.

### Pertemuan 10 — 04.3.1

**Waktu/metode:** A / Studi kasus, praktik. **Materi:** Middleware/otorisasi peran admin dan petugas pada route/controller.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Middleware/otorisasi peran admin dan petugas pada route/controller. **Penutup:** Periksa indikator: Peran yang tidak berwenang ditolak mengakses fitur terbatas. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti uji dua peran. **Rujukan:** R6, R11.

### Pertemuan 11 — 04.3.2

**Waktu/metode:** A / Praktik, uji kasus. **Materi:** Validasi Request, Eloquent/query builder dan CSRF pada Blade.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Validasi Request, Eloquent/query builder dan CSRF pada Blade. **Penutup:** Periksa indikator: Input invalid ditolak server dan kueri menggunakan parameter. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti validasi, parameterisasi dan penjelasan kontrol. **Rujukan:** R5, R6, R11.

### Pertemuan 12 — 04.3.1, 04.3.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Tugas 2: demonstrasi autentikasi, peran dan validasi dengan Laravel.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Tugas 2: demonstrasi autentikasi, peran dan validasi dengan Laravel. **Penutup:** Periksa indikator: Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 2: 25% — CPMK04.3.** **Rujukan:** R5, R6, R11. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 13 — 04.4.1

**Waktu/metode:** A / Praktik proyek. **Materi:** Integrasi Blade, route, controller, model dan otorisasi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Integrasi Blade, route, controller, model dan otorisasi. **Penutup:** Periksa indikator: Antarmuka, rute, data dan akses terhubung pada purwarupa. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Purwarupa terintegrasi. **Rujukan:** R4, R5, R6, R11.

### Pertemuan 14 — 04.4.1

**Waktu/metode:** A / Praktik, konsultasi. **Materi:** Penyelesaian alur dan penjelasan kontribusi kode sendiri serta komponen framework.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Penyelesaian alur dan penjelasan kontribusi kode sendiri serta komponen framework. **Penutup:** Periksa indikator: Alur end-to-end menggunakan data dummy sesuai kebutuhan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Alur kasus dan penjelasan kode. **Rujukan:** R4, R5, R11.

### Pertemuan 15 — 04.4.2

**Waktu/metode:** A / Pengujian, umpan balik. **Materi:** Feature test atau uji terdokumentasi normal/gagal; cek CSRF pengayaan dan setup.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Feature test atau uji terdokumentasi normal/gagal; cek CSRF pengayaan dan setup. **Penutup:** Periksa indikator: Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Hasil uji, temuan, perbaikan dan petunjuk lokal. **Rujukan:** R4, R6, R11.

### Pertemuan 16 — 04.4.1, 04.4.2

**Waktu/metode:** E / Ujian proyek. **Materi:** UAS: demonstrasi proyek Laravel dan bukti lima cek integrasi.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UAS: 30% — CPMK04.4.** **Rujukan:** R4, R5, R6, R11. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

**Perangkat rinci:** [outline modul](027_OUTLINE_MODUL_KOM-526C_07112026_1332.md) · [rencana evaluasi dan asesmen](028_RENCANA_EVALUASI_ASESMEN_KOM-526C_07112026_1332.md) · [rubrik penilaian](029_RUBRIK_PENILAIAN_KOM-526C_07112026_1332.md).

## 3. Outline modul dan praktikum — 14 topik [U]

Topik mengikuti pertemuan pembelajaran selain UTS dan UAS; pertemuan 4 dan 12 tetap memuat T1/T2. Kolom Bloom mengikuti level Sub-CPMK minggu tersebut atau level CPMK pada minggu instrumen (010 bagian 15). Sumber mengikuti bagian 5; isi modul lengkap dan aksesibilitas perlu disiapkan pengampu.

| Modul | Pekan | Materi/pengalaman | Latihan dan bukti | Bloom | Rujukan |
|---:|---:|---|---|---|---|
| 1 | 1 | Diagnostik PHP/OOP dan Composer; orientasi proyek Laravel dan rute sederhana. | Diagnostik, pengayaan bahasa dan bukti lingkungan. | C2 | R4, R11 |
| 2 | 2 | Aktor/kebutuhan inventaris; konvensi controller, view dan struktur proyek. | Aktor dan kebutuhan awal. | C2 | R4, R11 |
| 3 | 3 | Model kategori–barang, relasi dan rancangan migration dari kebutuhan. | Diagram/model data dan jejak kebutuhan. | C6 | R5, R11 |
| 4 | 4 | Presentasi Tugas 1; pengantar route dan controller Laravel. | **Tugas 1: 20% — CPMK04.1.** | C6 | R4, R5, R11 |
| 5 | 5 | Route web, controller, request/response dan Blade. | Bukti request dan respons. | C3 | R4, R11 |
| 6 | 6 | Konfigurasi database, migration dan Eloquent create/read. | Bukti create/read menggunakan data dummy. | C3 | R4, R5, R11 |
| 7 | 7 | Eloquent update/delete, validasi dasar dan penanganan not-found. | Bukti update/delete dan not-found. | C3 | R4, R5, R11 |
| 8 | 9 | Fasilitas autentikasi Laravel atau starter kit pilihan; login/logout dan sesi. | Bukti login/logout dengan data dummy. | C3 | R6, R11 |
| 9 | 10 | Middleware/otorisasi peran admin dan petugas pada route/controller. | Bukti uji dua peran. | C3 | R6, R11 |
| 10 | 11 | Validasi Request, Eloquent/query builder dan CSRF pada Blade. | Bukti validasi, parameterisasi dan penjelasan kontrol. | C4 | R5, R6, R11 |
| 11 | 12 | Tugas 2: demonstrasi autentikasi, peran dan validasi dengan Laravel. | **Tugas 2: 25% — CPMK04.3.** | C4 | R5, R6, R11 |
| 12 | 13 | Integrasi Blade, route, controller, model dan otorisasi. | Purwarupa terintegrasi. | C6 | R4, R5, R6, R11 |
| 13 | 14 | Penyelesaian alur dan penjelasan kontribusi kode sendiri serta komponen framework. | Alur kasus dan penjelasan kode. | C6 | R4, R5, R11 |
| 14 | 15 | Feature test atau uji terdokumentasi normal/gagal; cek CSRF pengayaan dan setup. | Hasil uji, temuan, perbaikan dan petunjuk lokal. | C5 | R4, R6, R11 |

## 4. Rencana evaluasi, instrumen dan rubrik [U]

**Kasus contoh:** inventaris peralatan dummy dengan kategori–barang berelasi (nama dan stok); admin mengelola dan petugas membaca. T1: minimal tiga kebutuhan teruji, dua entitas berelasi dan keterlacakan. UTS dalam lingkungan terisolasi: buat, baca, ubah stok, hapus dan minta ID yang tidak ada; autentikasi belum dinilai. T2: login admin valid, sandi salah, petugas ditolak mengubah, logout browser saat ini, stok negatif ditolak server dan kueri input terparameter. UAS: integrasi dan uji alur normal/gagal. Rincian dan batas keamanan pada 010 bagian 13.2–13.3.

**Kondisi jalur untuk UTS/T2/UAS:** Rute/controller Laravel dan Eloquent dipakai pada alur data yang diuji; cek akses menggunakan mekanisme Laravel yang dipilih. Ini kondisi cek terkait, bukan butir nilai tambahan; T1 tidak mensyaratkan kode. Rincian keamanan dan lima skenario: 010 bagian 13.2–13.3.

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

- **R11 — Laravel:** [Routing Laravel 12.x](https://laravel.com/docs/12.x/routing) dan [Authentication Laravel 12.x](https://laravel.com/docs/12.x/authentication). Halaman versi ini adalah **contoh rujukan**, bukan mandat memakai Laravel 12; cocokkan dengan versi terpilih dan status dukungannya.

**R19 — Taksonomi Bloom dan ABCD:** Anderson & Krathwohl (eds.), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives* (Longman, 2001) untuk dimensi proses kognitif C1–C6; struktur ABCD mengikuti praktik penyusunan capaian OBE. Rujukan ini **usulan penyusun**, bukan daftar pustaka resmi prodi, dan pengampu perlu memverifikasi edisi serta ketersediaannya. Penerapan ada pada [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u).

**Sebelum finalisasi:** periksa buku KPT/RPS atau workbook terkait, CPL/BK dan kode jalur; tetapkan dosen, tahun, format, prasyarat formal, T/P, PT/BM dan durasi evaluasi; tinjau kesiapan alat, akses dan instrumen bersama RMK; lengkapi identitas/pengesahan dan kebijakan remedial/CQI. Periksa 010 bagian 8–13. Tidak ada uji coba instrumen pada mahasiswa atau pengesahan akademik yang diklaim.
