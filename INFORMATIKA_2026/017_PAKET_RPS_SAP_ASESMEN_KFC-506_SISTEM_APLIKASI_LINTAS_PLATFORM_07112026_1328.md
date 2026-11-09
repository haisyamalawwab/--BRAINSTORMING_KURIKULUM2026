# 017 — Paket bahan RPS, SAP, modul dan asesmen Informatika

## KFC-506 — Sistem Aplikasi Lintas Platform

> **DRAF [U] — belum disahkan.** Bahan siap ditinjau untuk penyusunan RPS dan perangkat ajar, bukan dokumen pelaksanaan resmi. Identitas MK/CPL/BK bertanda [S] bersumber dari UWG; CPMK, Sub-CPMK, jadwal, instrumen, bobot, teknologi dan kasus adalah usulan. [K] memerlukan konfirmasi. Sumber kerja: [010](<010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md>), [009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) dan buku KPT Teknik Informatika sebagaimana daftar 010; contoh struktur [PERANGKAT_AJAR STI-311](../KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md) tidak menjadi sumber aturan TI.

## 1. RPS — identitas dan otorisasi

| Komponen | Isian / status |
|---|---|
| Institusi / program studi | Universitas Widyagama Malang / S1 Teknik Informatika [S]; nama fakultas pada RPS [K]. |
| MK / kode resmi | Sistem Aplikasi Lintas Platform (+P); KFC-506; 3 SKS; semester 5; wajib konsentrasi MC [S]. |
| Label jalur | Usulan **dua jalur**: KFC-506a Dart + Flutter ([037](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md)) atau KFC-506b React Native + Expo ([041](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md)); bukan kode KRS. Dokumen ini tetap rencana dasar netral. |
| Prasyarat | Formal **belum terverifikasi** [K]; usulan FST-102 Algoritma dan Pemrograman dan KOM-311 Pemrograman Berorientasi Objek [U], tidak membatasi KRS sebelum keputusan prodi. |
| Teori / praktik / PT / BM | Belum ditetapkan [K]; `+P` tidak menentukan T/P. Skenario A/E di bawah hanya simulasi. |
| Tahun ajaran, kelas, rumpun, nomor dokumen | Belum ditetapkan [K]. |
| Pengembang, dosen, koordinator RMK, kaprodi, penjaminan mutu, tanggal / tanda tangan | Belum ditetapkan [K]. |
| CPL dan BK | CPL04 [S]; BK Tabel 15: BK02 [S]. Pemetaan dan relevansi BK tambahan mengikuti catatan 010 bagian 5.1. |

**CPL04 [S]:** Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

**Deskripsi [U]:** Membangun satu basis kode untuk dua target berbeda melalui setup, antarmuka adaptif, aksesibilitas, navigasi/state, penyimpanan lokal dan uji lintas target.

**Fasilitas dan batas [U/K]:** Editor, SDK dan dua target berbeda yang tersedia (contoh browser desktop dan emulator Android); mock lokal, data dummy. R7/R8 hanya contoh jika Flutter dipilih. Bila pengampu memilih jalur teknis, gunakan paket turunan **KFC-506a Dart + Flutter** ([037](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md)) atau **KFC-506b React Native + Expo** ([041](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md)); lihat 010 bagian 14. Persiapan alat, versi, aksesibilitas, bahan offline dan ketersediaan disetujui pengampu. PT/BM serta moda dan durasi penugasan menunggu kebijakan prodi.

### CPMK dan Sub-CPMK [U]

**Rumusan ABCD dan level Bloom [U].** Setiap capaian ditulis lengkap (Audience–Behaviour–Condition–Degree) dan diberi level Bloom C2–C6. Kerangka, kata kerja, bukti asesmen dan aturan konsistensinya ada di [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u). Penambahan kolom ini **tidak mengubah** bobot maupun lima cek instrumen.

**CPMK — rumusan ABCD dan level Bloom**

| Kode | Rumusan lengkap (A–D) dan level Bloom | Bloom |
|---|---|---|
| CPMK04.1 | Mahasiswa mampu **membangun dan menjalankan** aplikasi sederhana dari satu basis kode pada dua target yang disepakati pada kasus aplikasi lintas platform yang disediakan, dengan minimal 4 dari 5 cek Tugas 1 terpenuhi. | C3 |
| CPMK04.2 | Mahasiswa mampu **menerapkan dan menguji** antarmuka adaptif dan aksesibel dasar pada dua target pada kasus yang diberikan, dengan minimal 4 dari 5 cek UTS terpenuhi. | C4 |
| CPMK04.3 | Mahasiswa mampu **mengimplementasikan dan menguji** navigasi, state dan penyimpanan lokal pada aplikasi lintas platform pada kasus aplikasi yang disediakan, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C4 |
| CPMK04.4 | Mahasiswa mampu **mengintegrasikan dan menguji** aplikasi lintas platform beserta dokumentasi hasil uji sesuai kasus yang disepakati, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 |

| Kode | A — Audience | B — Behaviour | C — Condition | D — Degree |
|---|---|---|---|---|
| CPMK04.1 | Mahasiswa | membangun dan menjalankan | pada kasus aplikasi lintas platform yang disediakan | dengan minimal 4 dari 5 cek Tugas 1 terpenuhi |
| CPMK04.2 | Mahasiswa | menerapkan dan menguji | pada kasus yang diberikan | dengan minimal 4 dari 5 cek UTS terpenuhi |
| CPMK04.3 | Mahasiswa | mengimplementasikan dan menguji | pada kasus aplikasi yang disediakan | dengan minimal 4 dari 5 kasus Tugas 2 lulus |
| CPMK04.4 | Mahasiswa | mengintegrasikan dan menguji | sesuai kasus yang disepakati | dengan minimal 4 dari 5 cek UAS terpenuhi |

**Sub-CPMK — rumusan ABCD dan level Bloom**

| Kode | CPMK | A — Audience | B — Behaviour | C — Condition | Bloom |
|---|---|---|---|---|---|
| Sub-CPMK04.1.1 | CPMK04.1 | Sub-CPMK04.1.1 | Mahasiswa | mengklasifikasikan | pada proyek yang disiapkan pengampu | C2 |
| Sub-CPMK04.1.2 | CPMK04.1 | Sub-CPMK04.1.2 | Mahasiswa | menjalankan dan menguji | pada dua target berbeda dari satu basis kode | C3 |
| Sub-CPMK04.2.1 | CPMK04.2 | Sub-CPMK04.2.1 | Mahasiswa | menyusun | sesuai ukuran dan platform target | C3 |
| Sub-CPMK04.2.2 | CPMK04.2 | Sub-CPMK04.2.2 | Mahasiswa | menguji | pada target yang mendukung | C4 |
| Sub-CPMK04.3.1 | CPMK04.3 | Sub-CPMK04.3.1 | Mahasiswa | mengelola | sesuai kasus aplikasi | C3 |
| Sub-CPMK04.3.2 | CPMK04.3 | Sub-CPMK04.3.2 | Mahasiswa | menganalisis | lalu menyimpan dan memulihkan data lokal pada kedua target yang diuji | C4 |
| Sub-CPMK04.4.1 | CPMK04.4 | Sub-CPMK04.4.1 | Mahasiswa | mengintegrasikan | dan menjalankannya pada dua target | C6 |
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
| 1 | 04.1.1 | C2 | Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. | Observasi dan umpan balik formatif; tanpa bobot. | Diskusi, demonstrasi — A | Diagnostik pemrograman; konsep basis kode bersama dan dua target. | R7 | 0% |
| 2 | 04.1.1 | C2 | Proyek dan konfigurasi untuk dua target dapat disiapkan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Menyiapkan proyek dan konfigurasi dua target. | R7 | 0% |
| 3 | 04.1.2 | C3 | Aksi sederhana dijalankan pada kedua target. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | Menjalankan contoh, input sederhana dan perbedaan target. | R7 | 0% |
| 4 | 04.1.1, 04.1.2 | C3 | Lima cek basis kode/aksi pada dua target Tugas 1 dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Menyerahkan contoh satu basis kode dan demonstrasi dua target. | R7 | 20% |
| 5 | 04.2.1 | C3 | Layout dan komponen menyesuaikan target yang disepakati. | Observasi dan umpan balik formatif; tanpa bobot. | Kuliah, praktik — A | Layout adaptif dan komponen lintas platform. | R7 | 0% |
| 6 | 04.2.1 | C3 | Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, diskusi — A | Adaptasi ukuran, orientasi dan batas kemampuan target. | R7 | 0% |
| 7 | 04.2.2 | C4 | Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji — A | Label, fokus keyboard, umpan balik dan uji aksesibilitas dasar. | R7, R9 | 0% |
| 8 | 04.2.1, 04.2.2 | C4 | Lima cek UI adaptif dan aksesibilitas dasar UTS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian praktik — E | Evaluasi antarmuka adaptif pada dua target. | R7, R9 | 25% |
| 9 | 04.3.1 | C3 | Aksi mengubah state dan tampilan sesuai contoh. | Observasi dan umpan balik formatif; tanpa bobot. | Demonstrasi, praktik — A | State, perubahan data dan pemutakhiran tampilan. | R8 | 0% |
| 10 | 04.3.1 | C3 | Navigasi maju/kembali mempertahankan state sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, uji — A | Navigasi antarhalaman dan konsistensi state. | R8 | 0% |
| 11 | 04.3.2 | C4 | Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik, studi kasus — A | Penyimpanan lokal, pemulihan data dan penanganan kesalahan. | R8 | 0% |
| 12 | 04.3.1, 04.3.2 | C4 | Lima kasus state, navigasi dan persistensi Tugas 2 dicatat. | Lima cek instrumen; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Penyelesaian fitur state/navigasi dan data lokal. | R8 | 25% |
| 13 | 04.4.1 | C6 | Rancangan proyek menunjukkan kasus dan fitur bersama. | Observasi dan umpan balik formatif; tanpa bobot. | Studi kasus, praktik — A | Rancang kasus proyek dan integrasi fitur satu basis kode. | R7, R8 | 0% |
| 14 | 04.4.1 | C6 | Fitur terintegrasi berjalan pada dua target berbeda. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik proyek — A | Adaptasi proyek untuk dua target; mock lokal opsional. | R7, R8 | 0% |
| 15 | 04.4.2 | C5 | Matriks hasil uji, perbedaan target dan perbaikan tersedia. | Observasi dan umpan balik formatif; tanpa bobot. | Pengujian, umpan balik — A | Uji lintas target, dokumentasi perbedaan dan perbaikan. | R7, R8 | 0% |
| 16 | 04.4.1, 04.4.2 | C6 | Lima cek integrasi lintas target dan dokumentasi UAS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian proyek — E | Demonstrasi dua target, hasil uji dan penjelasan individu. | R7, R8 | 30% |

## 2. SAP — Satuan Acara Pertemuan [U]

**Pola pelaksanaan:** pembuka—diagnostik singkat/prasyarat dan tujuan; inti—dosen memodelkan langkah atau memberi sumber, mahasiswa mempraktikkan kegiatan khusus pertemuan; penutup—uji indikator, berikan umpan balik, catat hambatan dan perbaikan. Distribusi menit per fase, PT dan BM **belum ditetapkan**; tidak menambah durasi A/E. Untuk minggu evaluasi gunakan sesi ujian, bukan kegiatan materi tambahan. Bukti formatif tidak menambah nilai sumatif. Rencana berikut merupakan SAP pertemuan siap dikembangkan, bukan modul berisi naskah lengkap.

### Pertemuan 1 — 04.1.1

**Waktu/metode:** A / Diskusi, demonstrasi. **Materi:** Diagnostik pemrograman; konsep basis kode bersama dan dua target.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Diagnostik pemrograman; konsep basis kode bersama dan dua target. **Penutup:** Periksa indikator: Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: daftar kebutuhan alat dan kemampuan awal. **Rujukan:** R7.

### Pertemuan 2 — 04.1.1

**Waktu/metode:** A / Praktik terbimbing. **Materi:** Menyiapkan proyek dan konfigurasi dua target.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Menyiapkan proyek dan konfigurasi dua target. **Penutup:** Periksa indikator: Proyek dan konfigurasi untuk dua target dapat disiapkan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: proyek awal dan panduan setup. **Rujukan:** R7.

### Pertemuan 3 — 04.1.2

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** Menjalankan contoh, input sederhana dan perbedaan target.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Menjalankan contoh, input sederhana dan perbedaan target. **Penutup:** Periksa indikator: Aksi sederhana dijalankan pada kedua target. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: hasil berjalan pada kedua target. **Rujukan:** R7.

### Pertemuan 4 — 04.1.1, 04.1.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Menyerahkan contoh satu basis kode dan demonstrasi dua target.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Menyerahkan contoh satu basis kode dan demonstrasi dua target. **Penutup:** Periksa indikator: Lima cek basis kode/aksi pada dua target Tugas 1 dibuktikan. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 1: 20%, CPMK04.1.** **Rujukan:** R7. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 5 — 04.2.1

**Waktu/metode:** A / Kuliah, praktik. **Materi:** Layout adaptif dan komponen lintas platform.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Layout adaptif dan komponen lintas platform. **Penutup:** Periksa indikator: Layout dan komponen menyesuaikan target yang disepakati. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: tampilan pada dua target. **Rujukan:** R7.

### Pertemuan 6 — 04.2.1

**Waktu/metode:** A / Praktik, diskusi. **Materi:** Adaptasi ukuran, orientasi dan batas kemampuan target.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Adaptasi ukuran, orientasi dan batas kemampuan target. **Penutup:** Periksa indikator: Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: perbandingan hasil dua target. **Rujukan:** R7.

### Pertemuan 7 — 04.2.2

**Waktu/metode:** A / Praktik, uji. **Materi:** Label, fokus keyboard, umpan balik dan uji aksesibilitas dasar.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Label, fokus keyboard, umpan balik dan uji aksesibilitas dasar. **Penutup:** Periksa indikator: Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: daftar cek aksesibilitas. **Rujukan:** R7, R9.

### Pertemuan 8 — 04.2.1, 04.2.2

**Waktu/metode:** E / Ujian praktik. **Materi:** Evaluasi antarmuka adaptif pada dua target.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UTS: 25%, CPMK04.2.** **Rujukan:** R7, R9. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 9 — 04.3.1

**Waktu/metode:** A / Demonstrasi, praktik. **Materi:** State, perubahan data dan pemutakhiran tampilan.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: State, perubahan data dan pemutakhiran tampilan. **Penutup:** Periksa indikator: Aksi mengubah state dan tampilan sesuai contoh. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: state dan perubahan UI. **Rujukan:** R8.

### Pertemuan 10 — 04.3.1

**Waktu/metode:** A / Praktik, uji. **Materi:** Navigasi antarhalaman dan konsistensi state.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Navigasi antarhalaman dan konsistensi state. **Penutup:** Periksa indikator: Navigasi maju/kembali mempertahankan state sesuai kasus. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: alur dua halaman. **Rujukan:** R8.

### Pertemuan 11 — 04.3.2

**Waktu/metode:** A / Praktik, studi kasus. **Materi:** Penyimpanan lokal, pemulihan data dan penanganan kesalahan.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Penyimpanan lokal, pemulihan data dan penanganan kesalahan. **Penutup:** Periksa indikator: Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: uji persistensi dan kegagalan. **Rujukan:** R8.

### Pertemuan 12 — 04.3.1, 04.3.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Penyelesaian fitur state/navigasi dan data lokal.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Penyelesaian fitur state/navigasi dan data lokal. **Penutup:** Periksa indikator: Lima kasus state, navigasi dan persistensi Tugas 2 dicatat. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 2: 25%, CPMK04.3.** **Rujukan:** R8. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 13 — 04.4.1

**Waktu/metode:** A / Studi kasus, praktik. **Materi:** Rancang kasus proyek dan integrasi fitur satu basis kode.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Rancang kasus proyek dan integrasi fitur satu basis kode. **Penutup:** Periksa indikator: Rancangan proyek menunjukkan kasus dan fitur bersama. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: rancangan dan purwarupa. **Rujukan:** R7, R8.

### Pertemuan 14 — 04.4.1

**Waktu/metode:** A / Praktik proyek. **Materi:** Adaptasi proyek untuk dua target; mock lokal opsional.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Adaptasi proyek untuk dua target; mock lokal opsional. **Penutup:** Periksa indikator: Fitur terintegrasi berjalan pada dua target berbeda. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: proyek berjalan pada dua target. **Rujukan:** R7, R8.

### Pertemuan 15 — 04.4.2

**Waktu/metode:** A / Pengujian, umpan balik. **Materi:** Uji lintas target, dokumentasi perbedaan dan perbaikan.

**Pembuka:** Hubungkan capaian dan indikator dengan hasil pertemuan sebelumnya; cek kesiapan dan alat. **Inti:** Dosen memandu atau memberi sumber sesuai metode; mahasiswa mengerjakan: Uji lintas target, dokumentasi perbedaan dan perbaikan. **Penutup:** Periksa indikator: Matriks hasil uji, perbedaan target dan perbaikan tersedia. Berikan umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: matriks uji dan keterbatasan. **Rujukan:** R7, R8.

### Pertemuan 16 — 04.4.1, 04.4.2

**Waktu/metode:** E / Ujian proyek. **Materi:** Demonstrasi dua target, hasil uji dan penjelasan individu.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat; tidak memberikan petunjuk jawaban saat ujian. **Inti:** Mahasiswa mengerjakan dan mendemonstrasikan instrumen pada bagian 4; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UAS: 30%, CPMK04.4.** **Rujukan:** R7, R8. **Instrumen sumatif:** gunakan ketentuan bagian 4; jangan menambah butir berbobot.

**Jalur teknis:** [KFC-506a Dart + Flutter](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md) · [KFC-506b React Native + Expo](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md). Dokumen ini adalah rencana dasar netral; jangan mencampur dua jalur dalam satu kelas tanpa keputusan prodi.

**Perangkat rinci:** [outline modul](033_OUTLINE_MODUL_KFC-506_07112026_1332.md) · [rencana evaluasi dan asesmen](034_RENCANA_EVALUASI_ASESMEN_KFC-506_07112026_1332.md) · [rubrik penilaian](035_RUBRIK_PENILAIAN_KFC-506_07112026_1332.md).

## 3. Outline modul dan praktikum — 14 topik [U]

Topik mengikuti pertemuan pembelajaran selain UTS dan UAS; pertemuan 4 dan 12 tetap memuat T1/T2. Kolom Bloom mengikuti level Sub-CPMK minggu tersebut atau level CPMK pada minggu instrumen (010 bagian 15). Sumber mengikuti bagian 5; isi modul lengkap dan aksesibilitas perlu disiapkan pengampu.

| Modul | Pekan | Materi/pengalaman | Latihan dan bukti | Bloom | Rujukan |
|---:|---:|---|---|---|---|
| 1 | 1 | Diagnostik pemrograman; konsep basis kode bersama dan dua target. | Formatif: daftar kebutuhan alat dan kemampuan awal. | C2 | R7 |
| 2 | 2 | Menyiapkan proyek dan konfigurasi dua target. | Formatif: proyek awal dan panduan setup. | C2 | R7 |
| 3 | 3 | Menjalankan contoh, input sederhana dan perbedaan target. | Formatif: hasil berjalan pada kedua target. | C3 | R7 |
| 4 | 4 | Menyerahkan contoh satu basis kode dan demonstrasi dua target. | **Tugas 1: 20%, CPMK04.1.** | C3 | R7 |
| 5 | 5 | Layout adaptif dan komponen lintas platform. | Formatif: tampilan pada dua target. | C3 | R7 |
| 6 | 6 | Adaptasi ukuran, orientasi dan batas kemampuan target. | Formatif: perbandingan hasil dua target. | C3 | R7 |
| 7 | 7 | Label, fokus keyboard, umpan balik dan uji aksesibilitas dasar. | Formatif: daftar cek aksesibilitas. | C4 | R7, R9 |
| 8 | 9 | State, perubahan data dan pemutakhiran tampilan. | Formatif: state dan perubahan UI. | C3 | R8 |
| 9 | 10 | Navigasi antarhalaman dan konsistensi state. | Formatif: alur dua halaman. | C3 | R8 |
| 10 | 11 | Penyimpanan lokal, pemulihan data dan penanganan kesalahan. | Formatif: uji persistensi dan kegagalan. | C4 | R8 |
| 11 | 12 | Penyelesaian fitur state/navigasi dan data lokal. | **Tugas 2: 25%, CPMK04.3.** | C4 | R8 |
| 12 | 13 | Rancang kasus proyek dan integrasi fitur satu basis kode. | Formatif: rancangan dan purwarupa. | C6 | R7, R8 |
| 13 | 14 | Adaptasi proyek untuk dua target; mock lokal opsional. | Formatif: proyek berjalan pada dua target. | C6 | R7, R8 |
| 14 | 15 | Uji lintas target, dokumentasi perbedaan dan perbaikan. | Formatif: matriks uji dan keterbatasan. | C5 | R7, R8 |

## 4. Rencana evaluasi, instrumen dan rubrik [U]

**Kasus contoh:** aplikasi daftar perlengkapan dummy dengan satu basis kode, dua target berbeda dan aksi tambah item. Pilih pasangan yang tersedia sebelum ujian, misalnya browser desktop dan emulator Android; dua ukuran layar pada satu platform bukan dua target. T1 demonstrasikan aksi sama pada dua target; UTS uji layout, label, fokus/keyboard jika didukung dan umpan balik; T2 gunakan dua halaman, state dan penyimpanan lokal, uji buka ulang dan simulasi kegagalan/data invalid; UAS dokumentasikan hasil/perbedaan kedua target. Pastikan mekanisme persistensi mendukung target, gunakan mock lokal dan jangan memakai data sensitif.

### Tugas 1, pekan 4 — 04.1 / 20%

**Instruksi:** Siapkan satu proyek dengan aksi sederhana pada dua target yang disepakati; serahkan kode bersama, konfigurasi dan bukti berjalan pada masing-masing target.

**Serahkan:** Satu proyek, petunjuk menjalankan dan bukti dua target. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | target A berjalan. | Diisi penilai | — | — |
| 2 | target B berjalan. | Diisi penilai | — | — |
| 3 | aksi sederhana berjalan pada A. | Diisi penilai | — | — |
| 4 | aksi sama berjalan pada B. | Diisi penilai | — | — |
| 5 | kode bersama dan konfigurasi kedua target dapat ditunjukkan. | Diisi penilai | — | — |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi:** Buat UI adaptif pada dua target dan buktikan label, fokus/keyboard pada target yang mendukung, serta umpan balik interaksi sesuai lima cek.

**Serahkan:** Proyek UI, tangkapan dua target dan daftar hasil uji. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | layout target A terbaca. | Diisi penilai | — | — |
| 2 | layout target B terbaca. | Diisi penilai | — | — |
| 3 | kontrol memiliki label. | Diisi penilai | — | — |
| 4 | fokus/keyboard dasar diuji pada target yang mendukung. | Diisi penilai | — | — |
| 5 | interaksi memberi umpan balik yang jelas pada kedua target. | Diisi penilai | — | — |

### Tugas 2, pekan 12 — 04.3 / 25%

**Instruksi:** Bangun navigasi, state dan penyimpanan lokal dengan penanganan data invalid/kegagalan; serahkan proyek dan lima uji, termasuk pemulihan setelah aplikasi dibuka ulang.

**Serahkan:** Proyek, data dummy, tabel lima uji dan penjelasan individu. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | state berubah sesuai aksi. | Diisi penilai | — | — |
| 2 | navigasi maju/kembali bekerja. | Diisi penilai | — | — |
| 3 | data tersimpan lokal. | Diisi penilai | — | — |
| 4 | data dipulihkan saat aplikasi dibuka ulang. | Diisi penilai | — | — |
| 5 | kegagalan penyimpanan atau data invalid memberi pesan yang dapat dipahami. | Diisi penilai | — | — |

### UAS, pekan 16 — 04.4 / 30%

**Instruksi:** Integrasikan aplikasi satu basis kode pada dua target; serahkan proyek, petunjuk, hasil uji lintas target, keterbatasan, perbaikan dan demonstrasi individu.

**Serahkan:** Satu proyek, bukti dua target, matriks uji dan demonstrasi individu. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | basis kode bersama terintegrasi. | Diisi penilai | — | — |
| 2 | fitur utama berjalan pada target A. | Diisi penilai | — | — |
| 3 | fitur utama berjalan pada target B. | Diisi penilai | — | — |
| 4 | hasil uji/perbedaan target dan perbaikan dicatat. | Diisi penilai | — | — |
| 5 | petunjuk menjalankan dan demonstrasi tersedia. | Diisi penilai | — | — |

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
| R7 | Flutter, [Adaptive and responsive design](https://docs.flutter.dev/ui/adaptive-responsive) dan [Web support](https://docs.flutter.dev/platform-integration/web) — contoh satu framework dengan target berbeda. | Contoh utama KFC-506 jika Flutter dipilih |
| R8 | Flutter, [Navigation basics](https://docs.flutter.dev/cookbook/navigation/navigation-basics) dan [Store key-value data on disk](https://docs.flutter.dev/cookbook/persistence/key-value) — contoh navigasi dan penyimpanan lokal. | Contoh pendukung KFC-506 jika Flutter dipilih |
| R9 | MDN, [Accessibility on the web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) — label dan interaksi keyboard pada konten web. | Pendukung KOM-312; konsep umum untuk KFC-506 |

**R19 — Taksonomi Bloom dan ABCD:** Anderson & Krathwohl (eds.), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives* (Longman, 2001) untuk dimensi proses kognitif C1–C6; struktur ABCD mengikuti praktik penyusunan capaian OBE. Rujukan ini **usulan penyusun**, bukan daftar pustaka resmi prodi, dan pengampu perlu memverifikasi edisi serta ketersediaannya. Penerapan ada pada [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u).

**Sebelum finalisasi:** periksa buku KPT/RPS atau workbook terkait, CPL/BK dan kode jalur; tetapkan dosen, tahun, format, prasyarat formal, T/P, PT/BM dan durasi evaluasi; tinjau kesiapan alat, akses dan instrumen bersama RMK; lengkapi identitas/pengesahan dan kebijakan remedial/CQI. Periksa 010 bagian 8–13. Tidak ada uji coba instrumen pada mahasiswa atau pengesahan akademik yang diklaim.
