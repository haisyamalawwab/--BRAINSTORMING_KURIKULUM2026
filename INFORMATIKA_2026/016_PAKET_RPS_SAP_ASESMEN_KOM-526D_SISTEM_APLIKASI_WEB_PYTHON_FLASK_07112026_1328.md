# 016 — Paket bahan RPS, SAP, modul dan asesmen Informatika

## KOM-526d — Sistem Aplikasi Web Python Flask

> **DRAF [U] — belum disahkan.** Bahan siap ditinjau untuk penyusunan RPS dan perangkat ajar, bukan dokumen pelaksanaan resmi. Identitas MK/CPL/BK bertanda [S] bersumber dari UWG; CPMK, Sub-CPMK, jadwal, instrumen, bobot, teknologi dan kasus adalah usulan. [K] memerlukan konfirmasi. Sumber kerja: [010](<010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md>), [009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) dan buku KPT Teknik Informatika sebagaimana daftar 010; contoh struktur [PERANGKAT_AJAR STI-311](../KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md) tidak menjadi sumber aturan TI.

## 1. RPS — identitas dan otorisasi

| Komponen | Isian / status |
|---|---|
| Institusi / program studi | Universitas Widyagama Malang / S1 Teknik Informatika [S]; nama fakultas pada RPS [K]. |
| MK / kode resmi | Sistem Aplikasi Web (+P); KOM-526; 3 SKS; semester 5 [S]. |
| Label jalur | KOM-526d — label usulan internal, **bukan kode KRS resmi** [U]. |
| Prasyarat | Formal **belum terverifikasi** [K]; usulan KOM-312 Pemrograman Web dan FST-207 Basis Data [U], tidak membatasi KRS sebelum keputusan prodi. |
| Teori / praktik / PT / BM | Belum ditetapkan [K]; `+P` tidak menentukan T/P. Skenario A/E di bawah hanya simulasi. |
| Tahun ajaran, kelas, rumpun, nomor dokumen | Belum ditetapkan [K]. |
| Pengembang, dosen, koordinator RMK, kaprodi, penjaminan mutu, tanggal / tanda tangan | Belum ditetapkan [K]. |
| CPL dan BK | CPL04 [S]; BK Tabel 15: BK02–BK08 [S]. Pemetaan dan relevansi BK tambahan mengikuti catatan 010 bagian 4.1. |

**CPL04 [S]:** Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

**Deskripsi [U]:** Merancang kebutuhan/model data, membangun rute server dan CRUD, menerapkan autentikasi, peran dan validasi, serta mengintegrasikan dan menguji sistem web lokal. Jalur ini menerapkan PYTHON FLASK.

**Fasilitas dan batas [U/K]:** Server dan database lokal, data dummy, runtime dan alat sesuai jalur; tidak menggunakan data/kredensial nyata. Lihat 010 bagian 13.2 untuk keamanan dasar dan batas produksi. Persiapan alat, versi, aksesibilitas, bahan offline dan ketersediaan disetujui pengampu. PT/BM serta moda dan durasi penugasan menunggu kebijakan prodi.

**Penempatan dan strategi jalur [U]:** Jalur 4 untuk mahasiswa yang berminat meningkatkan keterampilan secara mandiri; kesiapan Python/web atau pengayaan, perencanaan dan konsultasi disepakati dengan dosen. Diagnostik dan dukungan sesuai 010 bagian 13.1A; tidak mengubah prasyarat formal/KRS.

### CPMK dan Sub-CPMK [U]

| Kode lokal | CPMK terukur | Bloom | CPL |
|---|---|---|---|
| CPMK04.1 | Mahasiswa mampu **merancang** kebutuhan, alur dan model data untuk kasus sistem web yang diberikan, dengan minimal 4 dari 5 cek rancangan Tugas 1 terpenuhi. | C6 | CPL04 |
| CPMK04.2 | Mahasiswa mampu **mengimplementasikan** rute dan operasi CRUD server–basis data pada kasus yang diberikan, dengan minimal 4 dari 5 kasus UTS lulus. | C3 | CPL04 |
| CPMK04.3 | Mahasiswa mampu **menerapkan dan menguji** autentikasi, pembatasan akses dan validasi server dasar pada aplikasi latihan, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C3 | CPL04 |
| CPMK04.4 | Mahasiswa mampu **mengintegrasikan dan menguji** sistem web sesuai rancangan serta mendokumentasikan hasil, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 | CPL04 |

| Kode lokal | Sub-CPMK operasional | CPMK | Bloom |
|---|---|---|---|
| Sub-CPMK04.1.1 | Menganalisis aktor, kebutuhan dan alur kasus yang dapat diuji. | CPMK04.1 | C4 |
| Sub-CPMK04.1.2 | Merancang entitas, relasi dan keterkaitan kebutuhan–data. | CPMK04.1 | C6 |
| Sub-CPMK04.2.1 | Mengimplementasikan rute, handler dan respons server sesuai kasus. | CPMK04.2 | C3 |
| Sub-CPMK04.2.2 | Menghubungkan operasi create, read, update dan delete dengan penyimpanan data. | CPMK04.2 | C3 |
| Sub-CPMK04.3.1 | Menerapkan login, logout, sesi dan pembatasan akses berdasarkan peran. | CPMK04.3 | C3 |
| Sub-CPMK04.3.2 | Menerapkan validasi server dan penggunaan kueri terparameter pada data masukan. | CPMK04.3 | C3 |
| Sub-CPMK04.4.1 | Mengintegrasikan rute, data, antarmuka dan akses sesuai rancangan. | CPMK04.4 | C6 |
| Sub-CPMK04.4.2 | Menguji alur normal dan kesalahan serta mendokumentasikan hasil dan perbaikan. | CPMK04.4 | C4 |

### Konteks capaian spesifik jalur [U]

| Jalur | CPMK04.1 / Sub .1.1–.1.2 | CPMK04.2 / Sub .2.1–.2.2 | CPMK04.3 / Sub .3.1–.3.2 | CPMK04.4 / Sub .4.1–.4.2 |
|---|---|---|---|---|
| **d Flask** | Merancang kebutuhan dan data untuk proyek Flask yang dipelajari secara mandiri terarah: identifikasi aktor/kebutuhan/alur / modelkan entitas dan relasi SQLite. | Mengimplementasikan rute dan CRUD Flask: route/view function dan respons / `sqlite3` untuk CRUD dan ID hilang. | Menerapkan akses dan validasi Flask: login/logout, sesi dan pemeriksaan peran / validasi server dan query `sqlite3` terparameter. | Mengintegrasikan dan menguji proyek Flask: hubungkan Jinja, route, data dan akses / uji alur serta dokumentasikan perbaikan dan proses belajar. |

Gunakan redaksi kontekstual ini sebagai usulan RPS jalur; 4 CPMK dan 8 Sub-CPMK adalah versi kontekstual kerangka di atas, bukan capaian tambahan. Seluruh target dan rubrik inti tetap berlaku.

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

`A`: simulasi 100 menit tatap muka + 170 menit praktik **hanya jika** disetujui 2T+1P; `E`: usulan slot evaluasi sampai 270 menit, bukan tambahan A. T/P, PT/BM dan durasi E belum terverifikasi. Bobot hanya pada T1/UTS/T2/UAS. Pustaka sesuai daftar di bagian 5.

| Minggu | Sub-CPMK | Indikator | Kriteria & teknik penilaian | Bentuk/metode dan waktu | Materi / kegiatan | Pustaka | Bobot |
|---:|---|---|---|---|---|---|---:|
| 1 | 04.1.1 | Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. | Observasi dan umpan balik formatif; tanpa bobot. | Diagnostik, kontrak belajar dan konsultasi — A | Diagnostik sintaks Python dan web; siapkan virtual environment dan respons Flask; sepakati rencana belajar dan jadwal konsultasi. | R4, R12 | 0% |
| 2 | 04.1.1 | Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Studi mandiri, lokakarya bimbingan — A | Aktor/kebutuhan inventaris; variabel, kondisi dan fungsi Python pada data dummy. | R4, R12 | 0% |
| 3 | 04.1.2 | Entitas, relasi dan contoh data konsisten dengan kebutuhan. | Observasi dan umpan balik formatif; tanpa bobot. | Rancang mandiri, konsultasi — A | Model kategori–barang, relasi dan rancangan penyimpanan SQLite. | R5, R12 | 0% |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. | Lima cek instrumen; bukti dan rubrik bagian 4. | Presentasi rancangan dan umpan balik — A | Presentasi Tugas 1; pengantar route dan view function Flask. | R4, R5, R12 | 20% |
| 5 | 04.2.1 | Rute menerima permintaan dan memberi respons sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Studi dokumentasi, praktik dan konsultasi — A | Flask route, metode GET/POST, request/response dan template Jinja; baca dokumentasi dan catat eksperimen. | R4, R12 | 0% |
| 6 | 04.2.2 | Data dummy dapat dibuat dan dibaca melalui server dan database. | Observasi dan umpan balik formatif; tanpa bobot. | Eksperimen mandiri, bimbingan — A | SQLite via sqlite3: koneksi, create/read dan placeholder parameter. | R4, R5, R12 | 0% |
| 7 | 04.2.2 | Update/delete serta kondisi data tidak ditemukan diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik mandiri, uji dan konsultasi — A | Update/delete, penanganan ID tidak ditemukan dan respons 404 Flask. | R4, R5, R12 | 0% |
| 8 | 04.2.1, 04.2.2 | Lima kasus CRUD dan data tidak ditemukan pada UTS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian praktik — E | UTS praktik: route Flask/sqlite3 dan lima kasus CRUD/not-found. | R4, R5, R12 | 25% |
| 9 | 04.3.1 | Login valid/tidak valid dan logout dapat didemonstrasikan. | Observasi dan umpan balik formatif; tanpa bobot. | Studi dokumentasi, praktik dan konsultasi — A | Hash/verifikasi kata sandi Werkzeug, login/logout dan sesi Flask. | R6, R12 | 0% |
| 10 | 04.3.1 | Peran yang tidak berwenang ditolak mengakses fitur terbatas. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus mandiri, konsultasi — A | Dekorator atau pemeriksaan peran admin/petugas pada route terlindungi. | R6, R12 | 0% |
| 11 | 04.3.2 | Input invalid ditolak server dan kueri menggunakan parameter. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik mandiri, uji dan umpan balik — A | Validasi server, sqlite3 parameter binding, autoescape Jinja dan Flask-WTF CSRF. | R5, R6, R12 | 0% |
| 12 | 04.3.1, 04.3.2 | Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Praktik dan demonstrasi — A | Tugas 2: demonstrasi login, peran, validasi dan sesi browser dengan Flask. | R5, R6, R12 | 25% |
| 13 | 04.4.1 | Antarmuka, rute, data dan akses terhubung pada purwarupa. | Observasi dan umpan balik formatif; tanpa bobot. | Proyek mandiri terarah, konsultasi — A | Integrasi route, Jinja, data dan akses dalam proyek inventaris. | R4, R5, R6, R12 | 0% |
| 14 | 04.4.1 | Alur end-to-end menggunakan data dummy sesuai kebutuhan. | Observasi dan umpan balik formatif; tanpa bobot. | Proyek mandiri terarah, konsultasi — A | Penyelesaian alur dan pemisahan fungsi akses data serta handler. | R4, R5, R12 | 0% |
| 15 | 04.4.2 | Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. | Observasi dan umpan balik formatif; tanpa bobot. | Uji mandiri dan umpan balik — A | Flask test client atau uji terdokumentasi normal/gagal; cek CSRF pengayaan, setup dan refleksi proses belajar. | R4, R6, R12 | 0% |
| 16 | 04.4.1, 04.4.2 | Lima cek integrasi, akses, data dan dokumentasi UAS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian proyek — E | UAS: demonstrasi proyek Flask dan bukti lima cek integrasi. | R4, R5, R6, R12 | 30% |

## 2. SAP — Satuan Acara Pertemuan [U]

**Pola pelaksanaan:** pembuka—diagnostik singkat/prasyarat dan tujuan; inti—dosen memodelkan langkah atau memberi sumber, mahasiswa mempraktikkan kegiatan khusus pertemuan; penutup—uji indikator, berikan umpan balik, catat hambatan dan perbaikan. Distribusi menit per fase, PT dan BM **belum ditetapkan**; tidak menambah durasi A/E. Untuk minggu evaluasi gunakan sesi ujian, bukan kegiatan materi tambahan. Bukti formatif tidak menambah nilai sumatif. Rencana berikut merupakan SAP pertemuan siap dikembangkan, bukan modul berisi naskah lengkap.

**Khusus jalur d:** minggu 1 sepakati rencana belajar, sumber dan konsultasi; tiap minggu mahasiswa menunjukkan log sumber/percobaan/hambatan, dosen memberi umpan balik dan bantuan. Log untuk pembimbingan, bukan nilai ekstra.

### Pertemuan 1 — 04.1.1

**Waktu/metode:** A / Diagnostik, kontrak belajar dan konsultasi. **Materi:** Diagnostik sintaks Python dan web; siapkan virtual environment dan respons Flask; sepakati rencana belajar dan jadwal konsultasi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Diagnostik sintaks Python dan web; siapkan virtual environment dan respons Flask; sepakati rencana belajar dan jadwal konsultasi. **Penutup:** Periksa indikator: Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Diagnostik, pengayaan bahasa dan bukti lingkungan. **Rujukan:** R4, R12.

### Pertemuan 2 — 04.1.1

**Waktu/metode:** A / Studi mandiri, lokakarya bimbingan. **Materi:** Aktor/kebutuhan inventaris; variabel, kondisi dan fungsi Python pada data dummy.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Aktor/kebutuhan inventaris; variabel, kondisi dan fungsi Python pada data dummy. **Penutup:** Periksa indikator: Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Aktor dan kebutuhan awal. **Rujukan:** R4, R12.

### Pertemuan 3 — 04.1.2

**Waktu/metode:** A / Rancang mandiri, konsultasi. **Materi:** Model kategori–barang, relasi dan rancangan penyimpanan SQLite.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Model kategori–barang, relasi dan rancangan penyimpanan SQLite. **Penutup:** Periksa indikator: Entitas, relasi dan contoh data konsisten dengan kebutuhan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Diagram/model data dan jejak kebutuhan. **Rujukan:** R5, R12.

### Pertemuan 4 — 04.1.1, 04.1.2, 04.2.1

**Waktu/metode:** A / Presentasi rancangan dan umpan balik. **Materi:** Presentasi Tugas 1; pengantar route dan view function Flask.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Presentasi Tugas 1; pengantar route dan view function Flask. **Penutup:** Periksa indikator: Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 1: 20% — CPMK04.1.** **Rujukan:** R4, R5, R12. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 5 — 04.2.1

**Waktu/metode:** A / Studi dokumentasi, praktik dan konsultasi. **Materi:** Flask route, metode GET/POST, request/response dan template Jinja; baca dokumentasi dan catat eksperimen.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Flask route, metode GET/POST, request/response dan template Jinja; baca dokumentasi dan catat eksperimen. **Penutup:** Periksa indikator: Rute menerima permintaan dan memberi respons sesuai kasus. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti request dan respons. **Rujukan:** R4, R12.

### Pertemuan 6 — 04.2.2

**Waktu/metode:** A / Eksperimen mandiri, bimbingan. **Materi:** SQLite via sqlite3: koneksi, create/read dan placeholder parameter.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: SQLite via sqlite3: koneksi, create/read dan placeholder parameter. **Penutup:** Periksa indikator: Data dummy dapat dibuat dan dibaca melalui server dan database. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti create/read menggunakan data dummy. **Rujukan:** R4, R5, R12.

### Pertemuan 7 — 04.2.2

**Waktu/metode:** A / Praktik mandiri, uji dan konsultasi. **Materi:** Update/delete, penanganan ID tidak ditemukan dan respons 404 Flask.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Update/delete, penanganan ID tidak ditemukan dan respons 404 Flask. **Penutup:** Periksa indikator: Update/delete serta kondisi data tidak ditemukan diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti update/delete dan not-found. **Rujukan:** R4, R5, R12.

### Pertemuan 8 — 04.2.1, 04.2.2

**Waktu/metode:** E / Ujian praktik. **Materi:** UTS praktik: route Flask/sqlite3 dan lima kasus CRUD/not-found.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UTS: 25% — CPMK04.2.** **Rujukan:** R4, R5, R12. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 9 — 04.3.1

**Waktu/metode:** A / Studi dokumentasi, praktik dan konsultasi. **Materi:** Hash/verifikasi kata sandi Werkzeug, login/logout dan sesi Flask.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Hash/verifikasi kata sandi Werkzeug, login/logout dan sesi Flask. **Penutup:** Periksa indikator: Login valid/tidak valid dan logout dapat didemonstrasikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti login/logout dengan data dummy. **Rujukan:** R6, R12.

### Pertemuan 10 — 04.3.1

**Waktu/metode:** A / Studi kasus mandiri, konsultasi. **Materi:** Dekorator atau pemeriksaan peran admin/petugas pada route terlindungi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Dekorator atau pemeriksaan peran admin/petugas pada route terlindungi. **Penutup:** Periksa indikator: Peran yang tidak berwenang ditolak mengakses fitur terbatas. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti uji dua peran. **Rujukan:** R6, R12.

### Pertemuan 11 — 04.3.2

**Waktu/metode:** A / Praktik mandiri, uji dan umpan balik. **Materi:** Validasi server, sqlite3 parameter binding, autoescape Jinja dan Flask-WTF CSRF.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Validasi server, sqlite3 parameter binding, autoescape Jinja dan Flask-WTF CSRF. **Penutup:** Periksa indikator: Input invalid ditolak server dan kueri menggunakan parameter. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Bukti validasi, parameterisasi dan penjelasan kontrol. **Rujukan:** R5, R6, R12.

### Pertemuan 12 — 04.3.1, 04.3.2

**Waktu/metode:** A / Praktik dan demonstrasi. **Materi:** Tugas 2: demonstrasi login, peran, validasi dan sesi browser dengan Flask.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Tugas 2: demonstrasi login, peran, validasi dan sesi browser dengan Flask. **Penutup:** Periksa indikator: Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 2: 25% — CPMK04.3.** **Rujukan:** R5, R6, R12. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 13 — 04.4.1

**Waktu/metode:** A / Proyek mandiri terarah, konsultasi. **Materi:** Integrasi route, Jinja, data dan akses dalam proyek inventaris.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Integrasi route, Jinja, data dan akses dalam proyek inventaris. **Penutup:** Periksa indikator: Antarmuka, rute, data dan akses terhubung pada purwarupa. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Purwarupa terintegrasi. **Rujukan:** R4, R5, R6, R12.

### Pertemuan 14 — 04.4.1

**Waktu/metode:** A / Proyek mandiri terarah, konsultasi. **Materi:** Penyelesaian alur dan pemisahan fungsi akses data serta handler.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Penyelesaian alur dan pemisahan fungsi akses data serta handler. **Penutup:** Periksa indikator: Alur end-to-end menggunakan data dummy sesuai kebutuhan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Alur kasus dan penjelasan kode. **Rujukan:** R4, R5, R12.

### Pertemuan 15 — 04.4.2

**Waktu/metode:** A / Uji mandiri dan umpan balik. **Materi:** Flask test client atau uji terdokumentasi normal/gagal; cek CSRF pengayaan, setup dan refleksi proses belajar.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Flask test client atau uji terdokumentasi normal/gagal; cek CSRF pengayaan, setup dan refleksi proses belajar. **Penutup:** Periksa indikator: Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Hasil uji, temuan, perbaikan dan petunjuk lokal. **Rujukan:** R4, R6, R12.

### Pertemuan 16 — 04.4.1, 04.4.2

**Waktu/metode:** E / Ujian proyek. **Materi:** UAS: demonstrasi proyek Flask dan bukti lima cek integrasi.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UAS: 30% — CPMK04.4.** **Rujukan:** R4, R5, R6, R12. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

**Perangkat rinci:** [outline modul](030_OUTLINE_MODUL_KOM-526D_07112026_1332.md) · [rencana evaluasi dan asesmen](031_RENCANA_EVALUASI_ASESMEN_KOM-526D_07112026_1332.md) · [rubrik penilaian](032_RUBRIK_PENILAIAN_KOM-526D_07112026_1332.md).

## 3. Outline modul dan praktikum — 14 topik [U]

Topik mengikuti pertemuan pembelajaran selain UTS dan UAS; pertemuan 4 dan 12 tetap memuat T1/T2. Sumber mengikuti bagian 5; isi modul lengkap dan aksesibilitas perlu disiapkan pengampu.

| Modul | Pekan | Materi/pengalaman | Latihan dan bukti | Rujukan |
|---:|---:|---|---|---|
| 1 | 1 | Diagnostik sintaks Python dan web; siapkan virtual environment dan respons Flask; sepakati rencana belajar dan jadwal konsultasi. | Diagnostik, pengayaan bahasa dan bukti lingkungan. | R4, R12 |
| 2 | 2 | Aktor/kebutuhan inventaris; variabel, kondisi dan fungsi Python pada data dummy. | Aktor dan kebutuhan awal. | R4, R12 |
| 3 | 3 | Model kategori–barang, relasi dan rancangan penyimpanan SQLite. | Diagram/model data dan jejak kebutuhan. | R5, R12 |
| 4 | 4 | Presentasi Tugas 1; pengantar route dan view function Flask. | **Tugas 1: 20% — CPMK04.1.** | R4, R5, R12 |
| 5 | 5 | Flask route, metode GET/POST, request/response dan template Jinja; baca dokumentasi dan catat eksperimen. | Bukti request dan respons. | R4, R12 |
| 6 | 6 | SQLite via sqlite3: koneksi, create/read dan placeholder parameter. | Bukti create/read menggunakan data dummy. | R4, R5, R12 |
| 7 | 7 | Update/delete, penanganan ID tidak ditemukan dan respons 404 Flask. | Bukti update/delete dan not-found. | R4, R5, R12 |
| 8 | 9 | Hash/verifikasi kata sandi Werkzeug, login/logout dan sesi Flask. | Bukti login/logout dengan data dummy. | R6, R12 |
| 9 | 10 | Dekorator atau pemeriksaan peran admin/petugas pada route terlindungi. | Bukti uji dua peran. | R6, R12 |
| 10 | 11 | Validasi server, sqlite3 parameter binding, autoescape Jinja dan Flask-WTF CSRF. | Bukti validasi, parameterisasi dan penjelasan kontrol. | R5, R6, R12 |
| 11 | 12 | Tugas 2: demonstrasi login, peran, validasi dan sesi browser dengan Flask. | **Tugas 2: 25% — CPMK04.3.** | R5, R6, R12 |
| 12 | 13 | Integrasi route, Jinja, data dan akses dalam proyek inventaris. | Purwarupa terintegrasi. | R4, R5, R6, R12 |
| 13 | 14 | Penyelesaian alur dan pemisahan fungsi akses data serta handler. | Alur kasus dan penjelasan kode. | R4, R5, R12 |
| 14 | 15 | Flask test client atau uji terdokumentasi normal/gagal; cek CSRF pengayaan, setup dan refleksi proses belajar. | Hasil uji, temuan, perbaikan dan petunjuk lokal. | R4, R6, R12 |

## 4. Rencana evaluasi, instrumen dan rubrik [U]

**Kasus contoh:** inventaris peralatan dummy dengan kategori–barang berelasi (nama dan stok); admin mengelola dan petugas membaca. T1: minimal tiga kebutuhan teruji, dua entitas berelasi dan keterlacakan. UTS dalam lingkungan terisolasi: buat, baca, ubah stok, hapus dan minta ID yang tidak ada; autentikasi belum dinilai. T2: login admin valid, sandi salah, petugas ditolak mengubah, logout browser saat ini, stok negatif ditolak server dan kueri input terparameter. UAS: integrasi dan uji alur normal/gagal. Rincian dan batas keamanan pada 010 bagian 13.2–13.3.

**Kondisi jalur untuk UTS/T2/UAS:** Route/view Flask dan `sqlite3` digunakan pada alur data yang diuji; cek akses dibuktikan pada aplikasi Flask. Kemandirian/log tidak diberi skor tambahan. Ini kondisi cek terkait, bukan butir nilai tambahan; T1 tidak mensyaratkan kode. Rincian keamanan dan lima skenario: 010 bagian 13.2–13.3.

Pada Flask, logout membuktikan akses browser yang diuji berakhir; sesi cookie bertanda tangan tidak otomatis membatalkan salinan cookie lama.

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

- **R12 — Flask:** [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) dan [Flask-WTF CSRF Protection 1.2.x](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/); cocokkan versi yang terpasang. Flask-WTF memerlukan secret key untuk token.

**Sebelum finalisasi:** periksa buku KPT/RPS atau workbook terkait, CPL/BK dan kode jalur; tetapkan dosen, tahun, format, prasyarat formal, T/P, PT/BM dan durasi evaluasi; tinjau kesiapan alat, akses dan instrumen bersama RMK; lengkapi identitas/pengesahan dan kebijakan remedial/CQI. Periksa 010 bagian 8–13. Tidak ada uji coba instrumen pada mahasiswa atau pengesahan akademik yang diklaim.
