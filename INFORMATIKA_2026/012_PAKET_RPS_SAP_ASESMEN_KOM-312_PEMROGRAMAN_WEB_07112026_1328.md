# 012 — Paket bahan RPS, SAP, modul dan asesmen Informatika

## KOM-312 — Pemrograman Web

> **DRAF [U] — belum disahkan.** Bahan siap ditinjau untuk penyusunan RPS dan perangkat ajar, bukan dokumen pelaksanaan resmi. Identitas MK/CPL/BK bertanda [S] bersumber dari UWG; CPMK, Sub-CPMK, jadwal, instrumen, bobot, teknologi dan kasus adalah usulan. [K] memerlukan konfirmasi. Sumber kerja: [010](<010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md>), [009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) dan buku KPT Teknik Informatika sebagaimana daftar 010; contoh struktur [PERANGKAT_AJAR STI-311](../KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md) tidak menjadi sumber aturan TI.

## 1. RPS — identitas dan otorisasi

| Komponen | Isian / status |
|---|---|
| Institusi / program studi | Universitas Widyagama Malang / S1 Teknik Informatika [S]; nama fakultas pada RPS [K]. |
| MK / kode resmi | Pemrograman Web (+P); KOM-312; 3 SKS; semester 3 [S]. |
| Label jalur | Tidak berlaku; bukan varian KOM-526. |
| Prasyarat | Formal **belum terverifikasi** [K]; usulan FST-102 Algoritma dan Pemrograman [U], tidak membatasi KRS sebelum keputusan prodi. |
| Teori / praktik / PT / BM | Belum ditetapkan [K]; `+P` tidak menentukan T/P. Skenario A/E di bawah hanya simulasi. |
| Tahun ajaran, kelas, rumpun, nomor dokumen | Belum ditetapkan [K]. |
| Pengembang, dosen, koordinator RMK, kaprodi, penjaminan mutu, tanggal / tanda tangan | Belum ditetapkan [K]. |
| CPL dan BK | CPL04 [S]; BK Tabel 15: BK02, BK09, BK10 [S]. Pemetaan dan relevansi BK tambahan mengikuti catatan 010 bagian 3.1. |

**CPL04 [S]:** Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

**Deskripsi [U]:** Membangun dasar antarmuka web melalui HTML semantik dan formulir, CSS/Flexbox responsif, JavaScript dan DOM/event, serta menguji halaman lokal.

**Fasilitas dan batas [U/K]:** Editor, browser dan alat pengembang; konten dummy atau berizin; lihat 010 bagian 3.5. Persiapan alat, versi, aksesibilitas, bahan offline dan ketersediaan disetujui pengampu. PT/BM serta moda dan durasi penugasan menunggu kebijakan prodi.

### CPMK dan Sub-CPMK [U]

**Rumusan ABCD dan level Bloom [U].** Setiap capaian ditulis lengkap (Audience–Behaviour–Condition–Degree) dan diberi level Bloom C2–C6. Kerangka, kata kerja, bukti asesmen dan aturan konsistensinya ada di [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u). Penambahan kolom ini **tidak mengubah** bobot maupun lima cek instrumen.

**CPMK — rumusan ABCD dan level Bloom**

| Kode | Rumusan lengkap (A–D) dan level Bloom | Bloom |
|---|---|---|
| CPMK04.1 | Mahasiswa mampu **menyusun** halaman HTML semantik yang memuat heading, konten, tabel, gambar, navigasi dan formulir berlabel untuk kasus halaman profil yang disediakan, dengan memenuhi minimal 4 dari 5 cek Tugas 1. | C3 |
| CPMK04.2 | Mahasiswa mampu **menerapkan** CSS dan tata letak responsif dengan Flexbox serta media query pada halaman HTML yang disediakan, dengan memenuhi minimal 4 dari 5 cek UTS pada dua lebar layar. | C3 |
| CPMK04.3 | Mahasiswa mampu **mengimplementasikan dan menganalisis** interaksi JavaScript serta validasi masukan sisi klien pada kasus formulir yang disediakan, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C4 |
| CPMK04.4 | Mahasiswa mampu **membangun dan menguji** halaman web responsif interaktif beserta dokumentasi hasil uji pada kasus yang disepakati, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 |

| Kode | A — Audience | B — Behaviour | C — Condition | D — Degree |
|---|---|---|---|---|
| CPMK04.1 | Mahasiswa | menyusun | untuk kasus halaman profil yang disediakan | dengan memenuhi minimal 4 dari 5 cek Tugas 1 |
| CPMK04.2 | Mahasiswa | menerapkan | pada halaman HTML yang disediakan | dengan memenuhi minimal 4 dari 5 cek UTS pada dua lebar layar |
| CPMK04.3 | Mahasiswa | mengimplementasikan dan menganalisis | pada kasus formulir yang disediakan | dengan minimal 4 dari 5 kasus Tugas 2 lulus |
| CPMK04.4 | Mahasiswa | membangun dan menguji | pada kasus yang disepakati | dengan minimal 4 dari 5 cek UAS terpenuhi |

**Sub-CPMK — rumusan ABCD dan level Bloom**

| Kode | CPMK | A — Audience | B — Behaviour | C — Condition | Bloom |
|---|---|---|---|---|---|
| Sub-CPMK04.1.1 | CPMK04.1 | Sub-CPMK04.1.1 | Mahasiswa | mengklasifikasikan | untuk kasus halaman profil yang disediakan | C2 |
| Sub-CPMK04.1.2 | CPMK04.1 | Sub-CPMK04.1.2 | Mahasiswa | membuat | sesuai kasus yang diberikan | C3 |
| Sub-CPMK04.2.1 | CPMK04.2 | Sub-CPMK04.2.1 | Mahasiswa | menerapkan | pada halaman kasus yang disediakan | C3 |
| Sub-CPMK04.2.2 | CPMK04.2 | Sub-CPMK04.2.2 | Mahasiswa | menggunakan | untuk dua lebar layar yang ditetapkan | C3 |
| Sub-CPMK04.3.1 | CPMK04.3 | Sub-CPMK04.3.1 | Mahasiswa | menulis | untuk membaca serta memvalidasi masukan pengguna | C3 |
| Sub-CPMK04.3.2 | CPMK04.3 | Sub-CPMK04.3.2 | Mahasiswa | menganalisis | melalui pengujian formulir pada halaman yang disediakan | C4 |
| Sub-CPMK04.4.1 | CPMK04.4 | Sub-CPMK04.4.1 | Mahasiswa | mengintegrasikan | pada satu halaman sesuai kasus yang disepakati | C6 |
| Sub-CPMK04.4.2 | CPMK04.4 | Sub-CPMK04.4.2 | Mahasiswa | mengevaluasi | kemudian memilih prioritas perbaikan bersama pengampu | C5 |

### Taksonomi Bloom C2–C6 dan rumusan ABCD pada RPS [U]

**Status [U]:** kerangka ini adalah **usulan penyusun berbasis praktik OBE**, bukan kutipan buku KPT Teknik Informatika UWG. Pemeriksaan dokumen sumber tidak menemukan tabel taksonomi Bloom dan CPL04 tidak diberi kode Bloom di sana; pemetaan level adalah tafsiran atas kata kerja CPL04 (*menganalisis*; *merancang, mengimplementasikan, menguji, mengintegrasikan, memelihara*) dan harus disahkan prodi/RMK.

**ABCD.** Setiap capaian ditulis lengkap agar terukur: **A** *Audience* — selalu "Mahasiswa"; **B** *Behaviour* — satu kata kerja terukur sesuai level Bloom; **C** *Condition* — kasus, alat, batasan atau konteks pengerjaan; **D** *Degree* — ambang ketercapaian. Pada rancangan ini **D diseragamkan: minimal 4 dari 5 cek instrumen terpenuhi** (target usulan, bukan standar kelulusan) dan **C** memuat kasus/alat yang memang sudah ditetapkan pada instrumen terkait.

**Level yang dipakai: C2, C3, C4, C5, C6.** C1 (mengingat) tidak dijadikan capaian MK karena bukan bukti kompetensi lulusan.

| Level | Proses kognitif | Kata kerja operasional | Bukti/asesmen yang cocok | Penempatan pada RPS |
|---|---|---|---|---|
| **C2** | Memahami | menjelaskan, mengklasifikasikan, membandingkan, mengilustrasikan, merangkum, memberi contoh | penjelasan lisan/tertulis, diagram, kuis/tanya jawab formatif | pekan 1–3: menjelaskan alur, peran dan istilah teknis (formatif) |
| **C3** | Menerapkan | menerapkan, menggunakan, mengimplementasikan, menjalankan, membuat, menyusun | unjuk kerja, kode/produk berjalan, studi kasus terarah | pekan 2–12: praktik terbimbing serta T1/UTS/T2 |
| **C4** | Menganalisis | menganalisis, membedakan, menelusuri, memeriksa, menguji, mendiagnosis | analisis kebutuhan, laporan uji, tabel hasil diharapkan vs aktual | pekan 3–15: analisis kebutuhan dan diagnosis kegagalan |
| **C5** | Mengevaluasi | menilai, memvalidasi, mengkritisi, memilih, memutuskan, membandingkan dengan kriteria | justifikasi perbaikan berprioritas, reviu hasil uji terhadap kriteria | pekan 15–16: menilai hasil uji dan memilih perbaikan (masuk lima cek UAS) |
| **C6** | Menciptakan | merancang, membangun, menyusun, mengintegrasikan, mengembangkan, memproduksi | produk/proyek terintegrasi, rancangan, dokumentasi, demonstrasi | pekan 4 dan 13–16: rancangan T1 dan integrasi UAS |

**Pola capaian pada rancangan ini:** T1 = **C6** untuk perancangan (KOM-526/KFC-506) atau **C3** untuk penyusunan artefak terarah (KOM-312); UTS dan T2 = **C3–C4** (menerapkan serta menganalisis/menguji); **UAS = C6** (mengintegrasikan) dengan **C5** dinilai di dalam lima cek UAS melalui penilaian hasil uji dan pemilihan perbaikan. Dengan pola ini kelima level C2–C6 terpakai: C2 secara formatif pada pekan awal, C3 pada penerapan alat, C4 pada analisis dan pengujian, C5 pada evaluasi hasil uji, C6 pada perancangan dan integrasi.

**Aturan konsistensi** (dapat diperiksa pada tabel CPMK/Sub-CPMK setiap paket):

1. **Level Sub-CPMK tidak melebihi level CPMK-nya**, dan setiap CPMK memiliki Sub-CPMK pada level yang sama atau lebih rendah.
2. **Level tertinggi CPMK tercermin pada instrumennya**: CPMK berlevel C6 dinilai melalui produk/rancangan, bukan kuis; C5 dinilai melalui justifikasi perbaikan, bukan sekadar melaporkan hasil.
3. **Kata kerja pada tabel level dipakai konsisten**; kata kerja kabur ("memahami", "mengetahui", "mengerti") tidak dipakai pada rumusan capaian.
4. **Setiap Sub-CPMK terlacak** ke satu CPMK, satu instrumen dan satu pekan pada tabel 16 minggu.
5. **ABCD bukan butir penilaian baru**: bobot T1/UTS/T2/UAS (20/25/25/30), lima cek biner per instrumen dan target ≥4/5 tidak berubah.

**Telaah C5 [K]:** C5 pada rancangan ini melekat pada Sub-CPMK 04.4.2 (mengevaluasi hasil uji dan memilih perbaikan) dan dinilai sebagai bagian cek UAS/T2 yang sudah ada, bukan butir berbobot baru. Bila prodi menghendaki C5 sebagai CPMK tersendiri dengan instrumen terpisah, revisi kisi-kisi, rubrik dan bobot lebih dahulu dan sahkan sebelum perkuliahan.

### Peta evaluasi [U]

| CPMK | Instrumen / minggu | Bloom | Bobot terhadap nilai akhir | CPL |
|---|---|---|---:|---|
| 04.1 | Tugas 1 / 4 | C3 | 20% | CPL04 |
| 04.2 | UTS / 8 | C3 | 25% | CPL04 |
| 04.3 | Tugas 2 / 12 | C4 | 25% | CPL04 |
| 04.4 | UAS / 16 | C6 | 30% | CPL04 |
| **Total** | | | **100%** | |

Target usulan tiap CPMK ≥4 dari 5 cek instrumen, bukan ketentuan resmi. Level Bloom mengikuti tabel CPMK dan tidak menambah bobot. Kode CPMK/Sub-CPMK bersifat lokal per MK. Bobot instrumen bukan bobot CPL lintas MK.

### Rencana mingguan RPS — 8 kolom [U]

`A`: simulasi 100 menit tatap muka + 170 menit praktik **hanya jika** disetujui 2T+1P; `E`: usulan slot evaluasi sampai 270 menit, bukan tambahan A. T/P, PT/BM dan durasi E belum terverifikasi. Bobot hanya pada T1/UTS/T2/UAS. Kolom **Bloom** mengikuti level Sub-CPMK yang dinilai minggu tersebut (010 bagian 15); level ini bukan bobot tambahan.

| Minggu | Sub-CPMK | Bloom | Indikator | Kriteria & teknik penilaian | Bentuk/metode dan waktu | Materi / kegiatan | Pustaka | Bobot |
|---:|---|---|---|---|---|---|---|---:|
| 1 | 04.1.1 | C2 | Struktur dasar dokumen dan hierarki heading tampak pada halaman profil. | Observasi dan umpan balik formatif; tanpa bobot. | Kuliah, demonstrasi, praktik — A | Orientasi web, browser, struktur dokumen, teks dan heading. | R1 | 0% |
| 2 | 04.1.1 | C2 | Elemen semantik, tautan dan gambar dengan alt berfungsi sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, umpan balik — A | Elemen semantik, tautan, navigasi dan gambar ber-alt. | R1, R9 | 0% |
| 3 | 04.1.2 | C3 | Tabel memiliki header dan label terhubung ke input; validasi HTML diuji. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Tabel, formulir, label, tipe input dan validasi HTML. | R1 | 0% |
| 4 | 04.1.1, 04.1.2, 04.2.1 | C3 | Lima butir HTML Tugas 1 dapat diperiksa; CSS tidak dinilai pada T1. | Lima cek instrumen; bukti dan rubrik bagian 4. | Penugasan, praktik — A | Tugas HTML dan pengantar CSS; penilaian T1 hanya pada HTML. | R1, R2 | 20% |
| 5 | 04.2.1 | C3 | Selektor dan box model menghasilkan kartu sesuai spesifikasi. | Observasi dan umpan balik formatif; tanpa bobot. | Kuliah, praktik — A | Selektor, cascade dasar, warna, tipografi dan box model. | R2 | 0% |
| 6 | 04.2.2 | C3 | Pengaturan container/item Flexbox menghasilkan navigasi dan kartu fleksibel. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Flexbox: container, item, alignment, wrap dan gap. | R2 | 0% |
| 7 | 04.2.2 | C3 | Layout terbaca dan overflow utama diuji pada dua lebar. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, diskusi — A | Media query, pengujian dua lebar layar dan perbaikan overflow. | R2 | 0% |
| 8 | 04.2.1, 04.2.2 | C3 | Lima cek UTS CSS, Flexbox dan dua lebar dapat dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian praktik — E | Evaluasi CSS dan layout responsif. | R2 | 25% |
| 9 | 04.3.1 | C3 | Fungsi menggunakan variabel dan operator menghasilkan nilai sesuai contoh. | Observasi dan umpan balik formatif; tanpa bobot. | Kuliah, latihan — A | JavaScript dasar: nilai, tipe, operator dan fungsi. | R3 | 0% |
| 10 | 04.3.1 | C3 | Fungsi membedakan masukan valid, kosong dan tidak valid. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji kasus — A | Percabangan dan validasi masukan, termasuk nilai kosong/tidak valid. | R3 | 0% |
| 11 | 04.3.2 | C4 | Event membaca input dan memperbarui elemen keluaran DOM. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | DOM/event, membaca input dan memperbarui keluaran secara aman. | R3 | 0% |
| 12 | 04.3.1, 04.3.2 | C4 | Lima kasus interaksi dan validasi Tugas 2 dijalankan dan dicatat. | Lima cek instrumen; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Menyelesaikan dan menguji interaksi berbasis formulir. | R1, R3 | 25% |
| 13 | 04.4.1 | C6 | Sketsa, konten berizin dan kerangka HTML sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus, diskusi — A | Perencanaan kasus halaman, konten berizin dan sketsa. | R1, R9 | 0% |
| 14 | 04.4.1 | C6 | HTML, CSS dan JavaScript terhubung pada purwarupa. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik proyek — A | Integrasi HTML, CSS dan interaksi JavaScript. | R1, R2, R3 | 0% |
| 15 | 04.4.2 | C5 | Hasil uji navigasi, interaksi, keyboard dan dua lebar mencatat perbaikan. | Observasi dan umpan balik formatif; tanpa bobot. | Pengujian, umpan balik — A | Uji navigasi, interaksi, keyboard dan dua lebar; perbaikan. | R2, R3, R9 | 0% |
| 16 | 04.4.1, 04.4.2 | C6 | Lima cek integrasi, fungsi dan dokumentasi UAS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian proyek — E | Demonstrasi, penjelasan kode dan penyerahan halaman. | R1, R2, R3, R9 | 30% |

## 2. SAP — Satuan Acara Pertemuan [U]

**Pola pelaksanaan:** pembuka—diagnostik singkat/prasyarat dan tujuan; inti—dosen memodelkan langkah atau memberi sumber, mahasiswa mempraktikkan kegiatan khusus pertemuan; penutup—uji indikator, berikan umpan balik, catat hambatan dan perbaikan. Distribusi menit per fase, PT dan BM **belum ditetapkan**; tidak menambah durasi A/E. Untuk minggu evaluasi gunakan sesi ujian, bukan kegiatan materi tambahan. Bukti formatif tidak menambah nilai sumatif. Rencana berikut merupakan SAP pertemuan siap dikembangkan, bukan modul berisi naskah lengkap.

### Pertemuan 1 — 04.1.1

**Waktu/metode:** A / Kuliah, demonstrasi, praktik. **Materi:** Orientasi web, browser, struktur dokumen, teks dan heading.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Orientasi web, browser, struktur dokumen, teks dan heading. **Penutup:** Periksa indikator: Struktur dasar dokumen dan hierarki heading tampak pada halaman profil. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: halaman profil awal. **Rujukan:** R1.

### Pertemuan 2 — 04.1.1

**Waktu/metode:** A / Praktik, umpan balik. **Materi:** Elemen semantik, tautan, navigasi dan gambar ber-alt.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Elemen semantik, tautan, navigasi dan gambar ber-alt. **Penutup:** Periksa indikator: Elemen semantik, tautan dan gambar dengan alt berfungsi sesuai kasus. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: halaman informasi dan cek navigasi. **Rujukan:** R1, R9.

### Pertemuan 3 — 04.1.2

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Tabel, formulir, label, tipe input dan validasi HTML.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Tabel, formulir, label, tipe input dan validasi HTML. **Penutup:** Periksa indikator: Tabel memiliki header dan label terhubung ke input; validasi HTML diuji. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: tabel dan formulir simulasi. **Rujukan:** R1.

### Pertemuan 4 — 04.1.1, 04.1.2, 04.2.1

**Waktu/metode:** A / Penugasan, praktik. **Materi:** Tugas HTML dan pengantar CSS; penilaian T1 hanya pada HTML.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Tugas HTML dan pengantar CSS; penilaian T1 hanya pada HTML. **Penutup:** Periksa indikator: Lima butir HTML Tugas 1 dapat diperiksa; CSS tidak dinilai pada T1. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 1: 20%, CPMK04.1.** **Rujukan:** R1, R2. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 5 — 04.2.1

**Waktu/metode:** A / Kuliah, praktik. **Materi:** Selektor, cascade dasar, warna, tipografi dan box model.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Selektor, cascade dasar, warna, tipografi dan box model. **Penutup:** Periksa indikator: Selektor dan box model menghasilkan kartu sesuai spesifikasi. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: stylesheet dan kartu. **Rujukan:** R2.

### Pertemuan 6 — 04.2.2

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Flexbox: container, item, alignment, wrap dan gap.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Flexbox: container, item, alignment, wrap dan gap. **Penutup:** Periksa indikator: Pengaturan container/item Flexbox menghasilkan navigasi dan kartu fleksibel. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: navigasi dan kartu fleksibel. **Rujukan:** R2.

### Pertemuan 7 — 04.2.2

**Waktu/metode:** A / Praktik, diskusi. **Materi:** Media query, pengujian dua lebar layar dan perbaikan overflow.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Media query, pengujian dua lebar layar dan perbaikan overflow. **Penutup:** Periksa indikator: Layout terbaca dan overflow utama diuji pada dua lebar. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: tangkapan layar dua lebar. **Rujukan:** R2.

### Pertemuan 8 — 04.2.1, 04.2.2

**Waktu/metode:** E / Ujian praktik. **Materi:** Evaluasi CSS dan layout responsif.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UTS: 25%, CPMK04.2.** **Rujukan:** R2. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 9 — 04.3.1

**Waktu/metode:** A / Kuliah, latihan. **Materi:** JavaScript dasar: nilai, tipe, operator dan fungsi.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: JavaScript dasar: nilai, tipe, operator dan fungsi. **Penutup:** Periksa indikator: Fungsi menggunakan variabel dan operator menghasilkan nilai sesuai contoh. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: fungsi dan keluaran sederhana. **Rujukan:** R3.

### Pertemuan 10 — 04.3.1

**Waktu/metode:** A / Praktik, uji kasus. **Materi:** Percabangan dan validasi masukan, termasuk nilai kosong/tidak valid.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Percabangan dan validasi masukan, termasuk nilai kosong/tidak valid. **Penutup:** Periksa indikator: Fungsi membedakan masukan valid, kosong dan tidak valid. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: fungsi dengan kasus valid dan invalid. **Rujukan:** R3.

### Pertemuan 11 — 04.3.2

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** DOM/event, membaca input dan memperbarui keluaran secara aman.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: DOM/event, membaca input dan memperbarui keluaran secara aman. **Penutup:** Periksa indikator: Event membaca input dan memperbarui elemen keluaran DOM. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: purwarupa interaksi. **Rujukan:** R3.

### Pertemuan 12 — 04.3.1, 04.3.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Menyelesaikan dan menguji interaksi berbasis formulir.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Menyelesaikan dan menguji interaksi berbasis formulir. **Penutup:** Periksa indikator: Lima kasus interaksi dan validasi Tugas 2 dijalankan dan dicatat. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 2: 25%, CPMK04.3.** **Rujukan:** R1, R3. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 13 — 04.4.1

**Waktu/metode:** A / Studi kasus, diskusi. **Materi:** Perencanaan kasus halaman, konten berizin dan sketsa.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Perencanaan kasus halaman, konten berizin dan sketsa. **Penutup:** Periksa indikator: Sketsa, konten berizin dan kerangka HTML sesuai kasus. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: rancangan dan kerangka halaman. **Rujukan:** R1, R9.

### Pertemuan 14 — 04.4.1

**Waktu/metode:** A / Praktik proyek. **Materi:** Integrasi HTML, CSS dan interaksi JavaScript.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Integrasi HTML, CSS dan interaksi JavaScript. **Penutup:** Periksa indikator: HTML, CSS dan JavaScript terhubung pada purwarupa. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: purwarupa. **Rujukan:** R1, R2, R3.

### Pertemuan 15 — 04.4.2

**Waktu/metode:** A / Pengujian, umpan balik. **Materi:** Uji navigasi, interaksi, keyboard dan dua lebar; perbaikan.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Uji navigasi, interaksi, keyboard dan dua lebar; perbaikan. **Penutup:** Periksa indikator: Hasil uji navigasi, interaksi, keyboard dan dua lebar mencatat perbaikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: catatan kasus dan perbaikan. **Rujukan:** R2, R3, R9.

### Pertemuan 16 — 04.4.1, 04.4.2

**Waktu/metode:** E / Ujian proyek. **Materi:** Demonstrasi, penjelasan kode dan penyerahan halaman.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UAS: 30%, CPMK04.4.** **Rujukan:** R1, R2, R3, R9. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

**Perangkat rinci:** [outline modul](018_OUTLINE_MODUL_KOM-312_07112026_1332.md) · [rencana evaluasi dan asesmen](019_RENCANA_EVALUASI_ASESMEN_KOM-312_07112026_1332.md) · [rubrik penilaian](020_RUBRIK_PENILAIAN_KOM-312_07112026_1332.md).

## 3. Outline modul dan praktikum — 14 topik [U]

Topik mengikuti pertemuan pembelajaran selain UTS dan UAS; pertemuan 4 dan 12 tetap memuat T1/T2. Sumber mengikuti bagian 5; isi modul lengkap dan aksesibilitas perlu disiapkan pengampu.

| Modul | Pekan | Materi/pengalaman | Latihan dan bukti | Bloom | Rujukan |
|---:|---:|---|---|---|---|
| 1 | 1 | Orientasi web, browser, struktur dokumen, teks dan heading. | Formatif: halaman profil awal. | C2 | R1 |
| 2 | 2 | Elemen semantik, tautan, navigasi dan gambar ber-alt. | Formatif: halaman informasi dan cek navigasi. | C2 | R1, R9 |
| 3 | 3 | Tabel, formulir, label, tipe input dan validasi HTML. | Formatif: tabel dan formulir simulasi. | C3 | R1 |
| 4 | 4 | Tugas HTML dan pengantar CSS; penilaian T1 hanya pada HTML. | **Tugas 1: 20%, CPMK04.1.** | C3 | R1, R2 |
| 5 | 5 | Selektor, cascade dasar, warna, tipografi dan box model. | Formatif: stylesheet dan kartu. | C3 | R2 |
| 6 | 6 | Flexbox: container, item, alignment, wrap dan gap. | Formatif: navigasi dan kartu fleksibel. | C3 | R2 |
| 7 | 7 | Media query, pengujian dua lebar layar dan perbaikan overflow. | Formatif: tangkapan layar dua lebar. | C3 | R2 |
| 8 | 9 | JavaScript dasar: nilai, tipe, operator dan fungsi. | Formatif: fungsi dan keluaran sederhana. | C3 | R3 |
| 9 | 10 | Percabangan dan validasi masukan, termasuk nilai kosong/tidak valid. | Formatif: fungsi dengan kasus valid dan invalid. | C3 | R3 |
| 10 | 11 | DOM/event, membaca input dan memperbarui keluaran secara aman. | Formatif: purwarupa interaksi. | C4 | R3 |
| 11 | 12 | Menyelesaikan dan menguji interaksi berbasis formulir. | **Tugas 2: 25%, CPMK04.3.** | C4 | R1, R3 |
| 12 | 13 | Perencanaan kasus halaman, konten berizin dan sketsa. | Formatif: rancangan dan kerangka halaman. | C6 | R1, R9 |
| 13 | 14 | Integrasi HTML, CSS dan interaksi JavaScript. | Formatif: purwarupa. | C6 | R1, R2, R3 |
| 14 | 15 | Uji navigasi, interaksi, keyboard dan dua lebar; perbaikan. | Formatif: catatan kasus dan perbaikan. | C5 | R2, R3, R9 |

## 4. Rencana evaluasi, instrumen dan rubrik [U]

**Kasus contoh:** halaman informasi kegiatan kampus fiktif berisi judul, navigasi, gambar berizin/alt, tabel jadwal dan formulir berlabel. CSS dinilai pada UTS, bukan T1. Untuk T2, contoh input jumlah peserta 1–10: masukan valid menghasilkan pesan, kosong dan di luar rentang ditolak, event memperbarui keluaran dan reset mengembalikan kondisi awal. Nilai ini contoh kasus; pengampu dapat menggantinya sebelum asesmen dengan kriteria tetap. Untuk UAS integrasikan halaman, navigasi dan interaksi; uji keyboard serta dua lebar yang ditetapkan sebelum ujian (contoh 375 dan 1024 piksel). Validasi klien bukan keamanan server.

### Tugas 1, pekan 4 — 04.1 / 20%

**Instruksi:** Buat halaman informasi HTML untuk kasus yang disediakan; sertakan konten, navigasi, tabel dan formulir. Serahkan HTML, aset dan daftar cek; CSS tidak dinilai.

**Serahkan:** HTML, aset berizin dan daftar cek; CSS tidak dinilai. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | struktur semantik. | Diisi penilai | — | — |
| 2 | hierarki heading. | Diisi penilai | — | — |
| 3 | navigasi dan gambar ber-alt. | Diisi penilai | — | — |
| 4 | tabel berheader. | Diisi penilai | — | — |
| 5 | formulir berlabel dan validasi HTML. | Diisi penilai | — | — |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi:** Terapkan CSS/Flexbox dan media query pada HTML yang disediakan; tampilkan dua lebar layar. Serahkan berkas dan tangkapan yang mendukung lima cek UTS pada bagian 4 (sumber: 010 bagian 3.4).

**Serahkan:** Berkas HTML/CSS dan tangkapan dua lebar. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | selektor/tipografi. | Diisi penilai | — | — |
| 2 | box model. | Diisi penilai | — | — |
| 3 | Flexbox. | Diisi penilai | — | — |
| 4 | tampilan lebar terbaca. | Diisi penilai | — | — |
| 5 | tampilan sempit terbaca tanpa overflow utama. | Diisi penilai | — | — |

### Tugas 2, pekan 12 — 04.3 / 25%

**Instruksi:** Buat formulir interaktif dengan JavaScript untuk input valid, kosong dan tidak valid, aksi dan reset. Sertakan lima hasil uji dan jelaskan kode.

**Serahkan:** HTML/JS, tabel lima uji dan penjelasan individu. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | input valid menghasilkan keluaran benar. | Diisi penilai | — | — |
| 2 | input kosong ditolak. | Diisi penilai | — | — |
| 3 | input tidak valid ditolak. | Diisi penilai | — | — |
| 4 | event tombol memperbarui DOM. | Diisi penilai | — | — |
| 5 | reset memulihkan kondisi awal. | Diisi penilai | — | — |

### UAS, pekan 16 — 04.4 / 30%

**Instruksi:** Bangun halaman responsif interaktif dari kasus yang disepakati; serahkan proyek lokal, petunjuk, hasil uji/perbaikan dan demonstrasi individu.

**Serahkan:** Halaman berjalan lokal, dokumentasi dan demonstrasi individu. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | HTML/CSS/JS terintegrasi. | Diisi penilai | — | — |
| 2 | navigasi berfungsi. | Diisi penilai | — | — |
| 3 | interaksi berfungsi. | Diisi penilai | — | — |
| 4 | dua lebar dan keyboard diuji. | Diisi penilai | — | — |
| 5 | hasil uji, perbaikan dan langkah menjalankan dicatat. | Diisi penilai | — | — |

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
| R1 | MDN, [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) — struktur, konten dan formulir. | Utama KOM-312 |
| R2 | MDN, [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) — layout, Flexbox dan responsivitas. | Utama KOM-312 |
| R3 | MDN, [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) — fungsi, kontrol alur dan bahasa. | Utama KOM-312 |
| R9 | MDN, [Accessibility on the web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) — label dan interaksi keyboard pada konten web. | Pendukung KOM-312; konsep umum untuk KFC-506 |

**R19 — Taksonomi Bloom dan ABCD:** Anderson & Krathwohl (eds.), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives* (Longman, 2001) untuk dimensi proses kognitif C1–C6; struktur ABCD mengikuti praktik penyusunan capaian OBE. Rujukan ini **usulan penyusun**, bukan daftar pustaka resmi prodi, dan pengampu perlu memverifikasi edisi serta ketersediaannya. Penerapan ada pada [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u).

**Sebelum finalisasi:** periksa buku KPT/RPS atau workbook terkait, CPL/BK dan kode jalur; tetapkan dosen, tahun, format, prasyarat formal, T/P, PT/BM dan durasi evaluasi; tinjau kesiapan alat, akses dan instrumen bersama RMK; lengkapi identitas/pengesahan dan kebijakan remedial/CQI. Periksa 010 bagian 8–13. Tidak ada uji coba instrumen pada mahasiswa atau pengesahan akademik yang diklaim.
