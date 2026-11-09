# 041 — Paket RPS, SAP, modul dan asesmen KFC-506b

## KFC-506b — Sistem Aplikasi Lintas Platform (jalur React Native + Expo)

> **Status [U]: draf, belum disahkan.** Identitas MK, CPL04 dan BK02 bersumber dari buku KPT Teknik Informatika UWG; CPMK, isi, urutan, asesmen dan contoh adalah usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) bagian 14 dan [paket netral KFC-506](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md). Label **a–b adalah usulan jalur di bawah satu MK resmi KFC-506**, bukan kode KRS baru; lihat 010 bagian 14.1. Jalur lain: [KFC-506a — Dart + Flutter](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md). Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: daftar perlengkapan dummy dengan satu basis kode; dua target berbeda adalah **target web di browser desktop dan target Android di emulator/perangkat**. Dua ukuran layar pada satu target bukan dua target.

## 1. RPS — identitas dan otorisasi

| Komponen | Isian / status |
|---|---|
| Institusi / program studi | Universitas Widyagama Malang / S1 Teknik Informatika [S]; nama fakultas pada RPS [K]. |
| MK / kode resmi | Sistem Aplikasi Lintas Platform (+P); **KFC-506**; 3 SKS; semester 5; wajib konsentrasi MC [S]. |
| Label jalur | **KFC-506b — React Native + Expo** [U]; label usulan, bukan kode KRS. Kode resmi yang dicatat tetap KFC-506. |
| Prasyarat | Formal **belum terverifikasi** [K]; usulan FST-102 Algoritma dan Pemrograman dan KOM-311 Pemrograman Berorientasi Objek [U], tidak membatasi KRS sebelum keputusan prodi. |
| Teori / praktik / PT / BM | Belum ditetapkan [K]; `+P` tidak menentukan T/P. Skenario A/E di bawah hanya simulasi. |
| Tahun ajaran, kelas, rumpun, nomor dokumen | Belum ditetapkan [K]. |
| Pengembang, dosen, koordinator RMK, kaprodi, penjaminan mutu, tanggal / tanda tangan | Belum ditetapkan [K]. |
| CPL dan BK | CPL04 [S]; BK Tabel 15: BK02 [S]. Pemetaan dan relevansi BK tambahan mengikuti catatan 010 bagian 5.1. |
| Lingkungan teknis | [U] satu basis kode JavaScript/TypeScript dengan komponen React Native dalam proyek Expo; target web dan Android dijalankan dari proyek yang sama. Persiapan: Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`) dan Expo Go atau development build pada emulator/perangkat Android; versi SDK Expo dicatat. |

**CPL04 [S]:** Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

**Deskripsi [U]:** Membangun satu basis kode React Native + Expo untuk dua target berbeda melalui setup, antarmuka adaptif, aksesibilitas dasar, navigasi/state, penyimpanan lokal dan uji lintas target.

**Fasilitas dan batas [U/K]:** satu basis kode JavaScript/TypeScript dengan komponen React Native dalam proyek Expo; target web dan Android dijalankan dari proyek yang sama. Alat: Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`) dan Expo Go atau development build pada emulator/perangkat Android; versi SDK Expo dicatat. Data dummy dan mock lokal. R7–R9 pada [017](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md) tetap berlaku sebagai rujukan konsep KFC-506; R16, R17 dan R18 adalah rujukan teknis jalur ini. Persiapan alat, versi, aksesibilitas, bahan offline dan ketersediaan disetujui pengampu. PT/BM serta moda dan durasi penugasan menunggu kebijakan prodi.

### CPMK dan Sub-CPMK [U]

| Kode lokal | CPMK terukur | Bloom | CPL |
|---|---|---|---|
| CPMK04.1 | Mahasiswa mampu **membangun dan menjalankan** aplikasi sederhana dari satu basis kode pada dua target yang disepakati, dengan minimal 4 dari 5 cek Tugas 1 terpenuhi. | C3 | CPL04 |
| CPMK04.2 | Mahasiswa mampu **menerapkan** antarmuka adaptif dan aksesibel dasar pada dua target kasus yang diberikan, dengan minimal 4 dari 5 cek UTS terpenuhi. | C3 | CPL04 |
| CPMK04.3 | Mahasiswa mampu **mengimplementasikan dan menguji** navigasi, state dan penyimpanan lokal pada kasus aplikasi, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C3 | CPL04 |
| CPMK04.4 | Mahasiswa mampu **mengintegrasikan dan menguji** aplikasi lintas platform sesuai kasus serta mendokumentasikan hasil, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 | CPL04 |

| Kode lokal | Sub-CPMK operasional | CPMK | Bloom |
|---|---|---|---|
| Sub-CPMK04.1.1 | Menyiapkan proyek Expo, mengenali struktur `app`/`package.json` dan mengidentifikasi kode bersama serta konfigurasi target web dan Android. | CPMK04.1 | C3 |
| Sub-CPMK04.1.2 | Menjalankan dan menguji satu aksi sederhana React Native pada target web dan Android dari basis kode yang sama. | CPMK04.1 | C3 |
| Sub-CPMK04.2.1 | Menyusun layout adaptif dengan komponen React Native serta `useWindowDimensions`/`Platform` sesuai ukuran dan platform. | CPMK04.2 | C3 |
| Sub-CPMK04.2.2 | Menguji label aksesibilitas, urutan fokus dan umpan balik interaksi dasar pada target yang mendukung. | CPMK04.2 | C4 |
| Sub-CPMK04.3.1 | Mengelola state React dan navigasi antardua halaman sesuai kasus. | CPMK04.3 | C3 |
| Sub-CPMK04.3.2 | Menyimpan dan memulihkan data lokal memakai `expo-sqlite` atau async storage serta menangani kegagalan sederhana. | CPMK04.3 | C3 |
| Sub-CPMK04.4.1 | Mengintegrasikan fitur kasus ke dalam satu basis kode Expo/React Native dan menjalankannya pada target web dan Android. | CPMK04.4 | C6 |
| Sub-CPMK04.4.2 | Menyusun uji lintas target, mencatat perbedaan perilaku dan keterbatasan modul/Expo Go serta perbaikannya. | CPMK04.4 | C4 |

### Peta evaluasi [U]

| CPMK | Instrumen / minggu | Bobot terhadap nilai akhir | CPL |
|---|---|---:|---|
| 04.1 | Tugas 1 / 4 | 20% | CPL04 |
| 04.2 | UTS / 8 | 25% | CPL04 |
| 04.3 | Tugas 2 / 12 | 25% | CPL04 |
| 04.4 | UAS / 16 | 30% | CPL04 |
| **Total** | | **100%** | |

Target usulan tiap CPMK ≥4 dari 5 cek instrumen, bukan ketentuan resmi. Kode CPMK/Sub-CPMK bersifat lokal per MK dan sama polanya dengan KFC-506 netral; bobot instrumen bukan bobot CPL lintas MK.

### Rencana mingguan RPS — 8 kolom [U]

`A`: simulasi 100 menit tatap muka + 170 menit praktik **hanya jika** disetujui 2T+1P; `E`: usulan slot evaluasi sampai 270 menit, bukan tambahan A. T/P, PT/BM dan durasi E belum terverifikasi. Bobot hanya pada T1/UTS/T2/UAS. Pustaka sesuai bagian 5.

| Minggu | Sub-CPMK | Indikator | Kriteria & teknik penilaian | Bentuk/metode dan waktu | Materi / kegiatan | Pustaka | Bobot |
|---:|---|---|---|---|---|---|---:|
| 1 | 04.1.1 | Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Diagnostik JavaScript/TypeScript (React) dan web; konsep satu basis kode, dua target dan batas framework. | R13 | 0% |
| 2 | 04.1.1 | Proyek dan konfigurasi untuk dua target dapat disiapkan. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Pembuatan proyek Expo/React Native, struktur berkas, dependensi dan konfigurasi target web serta Android. | R13, R14 | 0% |
| 3 | 04.1.2 | Aksi sederhana dijalankan pada kedua target. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Menjalankan aplikasi, input sederhana dan perbedaan perilaku antara target web dan Android. | R13, R14 | 0% |
| 4 | 04.1.1, 04.1.2 | Lima cek basis kode/aksi pada dua target Tugas 1 dibuktikan. | Lima cek instrumen Tugas 1; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Konsolidasi bukti kode bersama, konfigurasi dan hasil berjalan pada dua target untuk Tugas 1. | R13, R14 | 20% |
| 5 | 04.2.1 | Layout dan komponen menyesuaikan target yang disepakati. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Layout adaptif dan komponen lintas platform pada Expo/React Native. | R14 | 0% |
| 6 | 04.2.1 | Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Adaptasi ukuran layar, orientasi dan batas kemampuan tiap target. | R14 | 0% |
| 7 | 04.2.2 | Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Label kontrol, fokus/pembaca layar dan umpan balik interaksi pada Expo/React Native. | R15 | 0% |
| 8 | 04.2.1, 04.2.2 | Lima cek UI adaptif dan aksesibilitas dasar UTS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian praktik — E | Evaluasi antarmuka adaptif pada dua target. | R17, R18 | 25% |
| 9 | 04.3.1 | Aksi mengubah state dan tampilan sesuai contoh. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | State pada Expo/React Native dan pemutakhiran tampilan setelah aksi. | R14, R15 | 0% |
| 10 | 04.3.1 | Navigasi maju/kembali mempertahankan state sesuai kasus. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Navigasi Expo Router atau React Navigation dan konsistensi state antarhalaman. | R14 | 0% |
| 11 | 04.3.2 | Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Penyimpanan lokal pada Expo/React Native, pemulihan data dan penanganan data invalid/kegagalan. | R15 | 0% |
| 12 | 04.3.1, 04.3.2 | Lima kasus state, navigasi dan persistensi Tugas 2 dicatat. | Lima cek instrumen Tugas 2; bukti dan rubrik bagian 4. | Praktik, demonstrasi — A | Konsolidasi bukti state, navigasi dan penyimpanan lokal untuk Tugas 2. | R14, R15 | 25% |
| 13 | 04.4.1 | Rancangan proyek menunjukkan kasus dan fitur bersama. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Rancangan kasus proyek dan integrasi fitur dalam satu basis kode. | R13, R14 | 0% |
| 14 | 04.4.1 | Fitur terintegrasi berjalan pada dua target berbeda. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Integrasi antarmuka, state dan data lokal, lalu menjalankannya pada dua target. | R13, R14 | 0% |
| 15 | 04.4.2 | Matriks hasil uji, perbedaan target dan perbaikan tersedia. | Observasi dan umpan balik formatif; tanpa bobot. | Praktik terbimbing — A | Uji lintas target, dokumentasi perbedaan perilaku dan perbaikan. | R14, R15 | 0% |
| 16 | 04.4.1, 04.4.2 | Lima cek integrasi lintas target dan dokumentasi UAS dibuktikan. | Lima cek instrumen; bukti dan rubrik bagian 4. | Ujian proyek — E | Demonstrasi dua target, hasil uji dan penjelasan individu. | R16, R17, R18 | 30% |

## 2. SAP — Satuan Acara Pertemuan [U]

**Pola pelaksanaan:** pembuka—diagnostik singkat dan tujuan; inti—dosen memodelkan langkah atau memberi sumber, mahasiswa mengerjakan kegiatan khusus pertemuan; penutup—uji indikator, beri umpan balik, catat hambatan dan perbaikan. Distribusi menit per fase, PT dan BM **belum ditetapkan**; tidak menambah durasi A/E. Untuk minggu evaluasi gunakan sesi ujian, bukan kegiatan materi tambahan. Bukti formatif tidak menambah nilai sumatif.

### Pertemuan 1 — 04.1.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Diagnostik JavaScript/TypeScript (React) dan web; konsep satu basis kode, dua target dan batas framework.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Lakukan diagnostik JavaScript/TypeScript (React)/web dan buat proyek dengan `create-expo-app` lalu jalankan `npx expo start`; identifikasi satu basis kode, target web serta target Android, dan alat yang dibutuhkan. **Penutup:** Periksa indikator "**Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. Rujukan: R13.

### Pertemuan 2 — 04.1.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Pembuatan proyek Expo/React Native, struktur berkas, dependensi dan konfigurasi target web serta Android.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Buat proyek Expo/React Native; catat versi SDK/dependensi, siapkan konfigurasi target web dan Android, lalu catat langkah setup serta hambatan. **Penutup:** Periksa indikator "**Proyek dan konfigurasi untuk dua target dapat disiapkan.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Proyek dan konfigurasi untuk dua target dapat disiapkan. Rujukan: R13, R14.

### Pertemuan 3 — 04.1.2

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Menjalankan aplikasi, input sederhana dan perbedaan perilaku antara target web dan Android.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Jalankan aksi tambah data dummy pada kedua target dari basis kode yang sama; catat perbedaan hasil dan penyebabnya. **Penutup:** Periksa indikator "**Aksi sederhana dijalankan pada kedua target.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Aksi sederhana dijalankan pada kedua target. Rujukan: R13, R14.

### Pertemuan 4 — 04.1.1, 04.1.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Konsolidasi bukti kode bersama, konfigurasi dan hasil berjalan pada dua target untuk Tugas 1.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat dan data dummy. **Inti:** Dosen memodelkan langkah singkat, lalu mahasiswa mengerjakan: Susun T1: tunjukkan kode bersama, konfigurasi, bukti berjalan dan aksi pada masing-masing target; lengkapi penjelasan individu. **Penutup:** Periksa indikator "**Lima cek basis kode/aksi pada dua target Tugas 1 dibuktikan.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 1: 20%, CPMK04.1.** Instrumen sumatif: gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 5 — 04.2.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Layout adaptif dan komponen lintas platform pada Expo/React Native.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Bangun tampilan daftar perlengkapan memakai komponen Expo/React Native; jalankan pada kedua target dan catat penyesuaian. **Penutup:** Periksa indikator "**Layout dan komponen menyesuaikan target yang disepakati.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Layout dan komponen menyesuaikan target yang disepakati. Rujukan: R14.

### Pertemuan 6 — 04.2.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Adaptasi ukuran layar, orientasi dan batas kemampuan tiap target.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Bandingkan ukuran, orientasi dan kemampuan kedua target; catat perbedaan layout serta penyesuaian yang dilakukan. **Penutup:** Periksa indikator "**Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. Rujukan: R14.

### Pertemuan 7 — 04.2.2

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Label kontrol, fokus/pembaca layar dan umpan balik interaksi pada Expo/React Native.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Terapkan `accessibilityLabel`/`accessibilityRole`/`accessibilityHint`; uji pada target yang mendukung dan dokumentasikan keterbatasan. **Penutup:** Periksa indikator "**Label, fokus dan umpan balik dasar diuji sesuai kemampuan target.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. Rujukan: R15.

### Pertemuan 8 — 04.2.1, 04.2.2

**Waktu/metode:** E / Ujian praktik. **Materi:** Evaluasi antarmuka adaptif pada dua target.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat (Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`) dan Expo Go atau development build pada emulator/perangkat Android; versi SDK Expo dicatat.) tanpa memberi petunjuk jawaban. **Inti:** Mahasiswa mengerjakan instrumen UTS bagian 4 dan mendemonstrasikannya; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UTS: 25%, CPMK04.2.** Instrumen sumatif: gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 9 — 04.3.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** State pada Expo/React Native dan pemutakhiran tampilan setelah aksi.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Buat state daftar dan aksi tambah; buktikan perubahan state memperbarui tampilan pada kedua target. **Penutup:** Periksa indikator "**Aksi mengubah state dan tampilan sesuai contoh.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Aksi mengubah state dan tampilan sesuai contoh. Rujukan: R14, R15.

### Pertemuan 10 — 04.3.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Navigasi Expo Router atau React Navigation dan konsistensi state antarhalaman.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Tambahkan navigasi maju/kembali antara dua halaman dan uji konsistensi state pada kedua target. **Penutup:** Periksa indikator "**Navigasi maju/kembali mempertahankan state sesuai kasus.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Navigasi maju/kembali mempertahankan state sesuai kasus. Rujukan: R14.

### Pertemuan 11 — 04.3.2

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Penyimpanan lokal pada Expo/React Native, pemulihan data dan penanganan data invalid/kegagalan.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Simpan data dummy memakai `expo-sqlite` atau async storage; uji pemulihan setelah aplikasi ditutup lalu dibuka ulang, serta kondisi gagal. **Penutup:** Periksa indikator "**Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. Rujukan: R15.

### Pertemuan 12 — 04.3.1, 04.3.2

**Waktu/metode:** A / Praktik, demonstrasi. **Materi:** Konsolidasi bukti state, navigasi dan penyimpanan lokal untuk Tugas 2.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat dan data dummy. **Inti:** Dosen memodelkan langkah singkat, lalu mahasiswa mengerjakan: Demonstrasikan T2: state, navigasi, simpan, buka ulang dan pesan invalid/gagal; catat lima hasil uji. **Penutup:** Periksa indikator "**Lima kasus state, navigasi dan persistensi Tugas 2 dicatat.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** **Tugas 2: 25%, CPMK04.3.** Instrumen sumatif: gunakan ketentuan bagian 4; jangan menambah butir berbobot.

### Pertemuan 13 — 04.4.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Rancangan kasus proyek dan integrasi fitur dalam satu basis kode.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Rancang proyek dan fitur bersama; siapkan data mock lokal agar tidak bergantung pada MK lain. **Penutup:** Periksa indikator "**Rancangan proyek menunjukkan kasus dan fitur bersama.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Rancangan proyek menunjukkan kasus dan fitur bersama. Rujukan: R13, R14.

### Pertemuan 14 — 04.4.1

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Integrasi antarmuka, state dan data lokal, lalu menjalankannya pada dua target.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Integrasikan fitur utama dan jalankan pada target web serta Android; catat perbaikan yang diperlukan. **Penutup:** Periksa indikator "**Fitur terintegrasi berjalan pada dua target berbeda.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Fitur terintegrasi berjalan pada dua target berbeda. Rujukan: R13, R14.

### Pertemuan 15 — 04.4.2

**Waktu/metode:** A / Kuliah singkat, praktik terbimbing. **Materi:** Uji lintas target, dokumentasi perbedaan perilaku dan perbaikan.

**Pembuka:** Kaitkan tujuan dengan hasil pekan sebelumnya; cek kesiapan alat. **Inti:** Demonstrasi singkat oleh dosen, lalu mahasiswa mengerjakan: Buat matriks uji dua target (`jest-expo` dan uji manual per target); catat hasil aktual, perbedaan, perbaikan dan petunjuk menjalankan. **Penutup:** Periksa indikator "**Matriks hasil uji, perbedaan target dan perbaikan tersedia.**", beri umpan balik dan catat satu perbaikan.

**Bukti:** Formatif: Matriks hasil uji, perbedaan target dan perbaikan tersedia. Rujukan: R14, R15.

### Pertemuan 16 — 04.4.1, 04.4.2

**Waktu/metode:** E / Ujian proyek. **Materi:** Demonstrasi dua target, hasil uji dan penjelasan individu.

**Pembuka:** Jelaskan ketentuan dan siapkan lingkungan/alat (Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`) dan Expo Go atau development build pada emulator/perangkat Android; versi SDK Expo dicatat.) tanpa memberi petunjuk jawaban. **Inti:** Mahasiswa mengerjakan instrumen UAS bagian 4 dan mendemonstrasikannya; pengampu mencatat hasil aktual per butir. **Penutup:** Kumpulkan bukti dan catatan lima cek; umpan balik mengikuti aturan pengampu.

**Bukti:** **UAS: 30%, CPMK04.4.** Instrumen sumatif: gunakan ketentuan bagian 4; jangan menambah butir berbobot.

**Perangkat rinci:** [outline modul](040_OUTLINE_MODUL_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) · [rencana evaluasi dan asesmen](042_RENCANA_EVALUASI_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) · [rubrik penilaian](043_RUBRIK_PENILAIAN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md).

## 3. Outline modul dan praktikum — 14 topik [U]

Topik mengikuti pertemuan pembelajaran selain UTS dan UAS; pertemuan 4 dan 12 tetap memuat T1/T2. Rincian langkah, bukti dan refleksi ada di [outline modul](040_OUTLINE_MODUL_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md).

| Modul | Pekan | Materi/pengalaman | Latihan dan bukti | Rujukan |
|---:|---:|---|---|---|
| 1 | 1 | Diagnostik dan konsep satu basis kode dua target. | Formatif: Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. | R13 |
| 2 | 2 | Menyiapkan proyek dan konfigurasi target. | Formatif: Proyek dan konfigurasi untuk dua target dapat disiapkan. | R13, R14 |
| 3 | 3 | Menjalankan aksi pertama pada dua target. | Formatif: Aksi sederhana dijalankan pada kedua target. | R13, R14 |
| 4 | 4 | Menyiapkan bukti Tugas 1. | **Tugas 1: 20%, CPMK04.1.** | R13, R14 |
| 5 | 5 | Layout adaptif dan komponen lintas platform. | Formatif: Layout dan komponen menyesuaikan target yang disepakati. | R14 |
| 6 | 6 | Adaptasi ukuran, orientasi dan batas platform. | Formatif: Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. | R14 |
| 7 | 7 | Aksesibilitas dasar dan umpan balik interaksi. | Formatif: Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. | R15 |
| 8 | 9 | State dan pemutakhiran tampilan. | Formatif: Aksi mengubah state dan tampilan sesuai contoh. | R14, R15 |
| 9 | 10 | Navigasi antardua halaman. | Formatif: Navigasi maju/kembali mempertahankan state sesuai kasus. | R14 |
| 10 | 11 | Penyimpanan lokal dan penanganan kegagalan. | Formatif: Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. | R15 |
| 11 | 12 | Menyiapkan bukti Tugas 2. | **Tugas 2: 25%, CPMK04.3.** | R14, R15 |
| 12 | 13 | Rancangan proyek terintegrasi. | Formatif: Rancangan proyek menunjukkan kasus dan fitur bersama. | R13, R14 |
| 13 | 14 | Integrasi proyek pada dua target. | Formatif: Fitur terintegrasi berjalan pada dua target berbeda. | R13, R14 |
| 14 | 15 | Uji lintas target dan dokumentasi keterbatasan. | Formatif: Matriks hasil uji, perbedaan target dan perbaikan tersedia. | R14, R15 |

## 4. Rencana evaluasi, instrumen dan rubrik [U]

**Kasus contoh:** aplikasi daftar perlengkapan dummy dengan satu basis kode, dua target (web dan Android) dan aksi tambah item. Kondisi uji di bawah memakai alat jalur ini pada lima butir yang sama dengan KFC-506 netral dan 010: bukan butir tambahan. Pastikan mekanisme yang dipilih benar-benar berjalan pada kedua target; bila tidak, catat keterbatasan dan pilih mekanisme lain sebelum ujian.

### Tugas 1, pekan 4 — 04.1 / 20%

**Instruksi:** Siapkan proyek React Native + Expo dengan satu aksi sederhana pada dua target (web dan Android); serahkan kode bersama, konfigurasi, petunjuk menjalankan dan bukti berjalan pada masing-masing target.

**Serahkan:** Satu proyek, petunjuk menjalankan dan bukti dua target. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | proyek Expo berjalan di target web. | Diisi penilai | — | — |
| 2 | proyek yang sama berjalan di target Android. | Diisi penilai | — | — |
| 3 | aksi sederhana berjalan di target web. | Diisi penilai | — | — |
| 4 | aksi yang sama berjalan di target Android. | Diisi penilai | — | — |
| 5 | kode bersama dan konfigurasi dua target dapat ditunjukkan. | Diisi penilai | — | — |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi:** Buat UI adaptif pada dua target dan buktikan label aksesibilitas, fokus/pembaca layar pada target yang mendukung, serta umpan balik interaksi sesuai lima cek.

**Serahkan:** Proyek UI, tangkapan dua target dan daftar hasil uji. **Waktu, moda, batas pengumpulan:** [K] ditentukan pengampu sebelum penilaian.

| No. | Cek / hasil yang diharapkan | Bukti/hasil aktual | Skor (0/100) | Umpan balik |
|---:|---|---|---:|---|
| 1 | layout daftar terbaca di target web. | Diisi penilai | — | — |
| 2 | layout daftar yang sama terbaca di target Android. | Diisi penilai | — | — |
| 3 | kontrol memiliki label aksesibilitas. | Diisi penilai | — | — |
| 4 | fokus/pembaca layar diuji pada target yang mendukung. | Diisi penilai | — | — |
| 5 | interaksi memberi umpan balik yang jelas di kedua target. | Diisi penilai | — | — |

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
| 1 | satu basis kode Expo/React Native terintegrasi. | Diisi penilai | — | — |
| 2 | fitur utama berjalan di target web. | Diisi penilai | — | — |
| 3 | fitur utama berjalan di target Android. | Diisi penilai | — | — |
| 4 | hasil uji, perbedaan target dan perbaikan dicatat. | Diisi penilai | — | — |
| 5 | petunjuk menjalankan dan demonstrasi tersedia. | Diisi penilai | — | — |

### Aturan rubrik, rekap dan tindak lanjut [U]

- Setiap cek bernilai **100** jika seluruh unsur terpenuhi dan bukti terverifikasi, atau **0** jika ada unsur gagal/tidak ditunjukkan. Setiap cek berbobot 20% dari skor instrumen. Butir gabungan mensyaratkan semua komponennya.
- Skor instrumen = `(cek1 + cek2 + cek3 + cek4 + cek5) / 5`; nilai akhir = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Contoh 100,100,100,100,0 → 80/100 dan target ≥4/5 tercapai; semua ini usulan.
- Untuk setiap cek catat kondisi/input, langkah, hasil diharapkan dan hasil aktual, bukti dan umpan balik. Tidak ada bobot tambahan untuk formatif, penggunaan alat tertentu, atau kompleksitas kode.
- Rekap per CPMK: simpan skor instrumen terkait, jumlah cek lulus, hambatan dan perbaikan. Dosen meninjau pola kesulitan untuk CQI; remedial, ambang final, pengolahan CPL dan kelulusan menunggu kebijakan prodi.

| Mahasiswa/identitas | T1 / cek lulus | UTS / cek lulus | T2 / cek lulus | UAS / cek lulus | Nilai akhir | Umpan balik / CQI |
|---|---|---|---|---|---|---|
| Diisi dosen | — | — | — | — | — | — |

## 5. Sumber dan kesiapan [U/K]

Rujukan teknis jalur ini: R13–R15 untuk Flutter, R16–R18 untuk React Native + Expo; rujukan konsep KFC-506 netral R7–R9 tetap pada [017](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md).

| Nomor | Pustaka | Keterangan |
|---|---|---|
| R16 | Expo, [Create a project](https://docs.expo.dev/get-started/create-a-project/) dan [Set up your environment](https://docs.expo.dev/get-started/set-up-your-environment/) — `create-expo-app`, `expo start`, Expo Go dan development build. | Utama jalur b |
| R17 | Expo, [Introduction to Expo Router](https://docs.expo.dev/router/introduction/) dan React Native, [Accessibility](https://reactnative.dev/docs/accessibility) — rute berbasis berkas, `accessibilityLabel`/`accessibilityRole`. | Utama jalur b |
| R18 | Expo, [SQLite](https://docs.expo.dev/versions/latest/sdk/sqlite/), [AsyncStorage](https://docs.expo.dev/versions/latest/sdk/async-storage/) dan [Unit testing with Jest](https://docs.expo.dev/develop/unit-testing/) — persistensi lokal dan `jest-expo`. | Pendukung jalur b |

**Sebelum finalisasi:** periksa buku KPT/RPS atau workbook terkait, CPL/BK dan kode jalur; tetapkan dosen, tahun, format, prasyarat formal, T/P, PT/BM dan durasi evaluasi; tinjau kesiapan alat, akses, lisensi SDK, ketersediaan emulator/perangkat dan instrumen bersama RMK; lengkapi identitas/pengesahan dan kebijakan remedial/CQI. Periksa 010 bagian 8–14. Tidak ada uji coba instrumen pada mahasiswa atau pengesahan akademik yang diklaim. Rujukan daring dapat berubah; cocokkan versi dengan SDK yang dipakai.
