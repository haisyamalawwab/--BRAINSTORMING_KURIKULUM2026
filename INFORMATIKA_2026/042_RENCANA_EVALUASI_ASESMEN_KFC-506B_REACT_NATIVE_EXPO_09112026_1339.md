# 042 — Rencana evaluasi dan asesmen KFC-506b

## KFC-506b — Sistem Aplikasi Lintas Platform (jalur React Native + Expo)

> **Status [U]: draf, belum disahkan.** Identitas MK, CPL04 dan BK02 bersumber dari buku KPT Teknik Informatika UWG; CPMK, isi, urutan, asesmen dan contoh adalah usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) bagian 14 dan [paket netral KFC-506](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md). Label **a–b adalah usulan jalur di bawah satu MK resmi KFC-506**, bukan kode KRS baru; lihat 010 bagian 14.1. Jalur lain: [KFC-506a — Dart + Flutter](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md). Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: daftar perlengkapan dummy dengan satu basis kode; dua target berbeda adalah **target web di browser desktop dan target Android di emulator/perangkat**. Dua ukuran layar pada satu target bukan dua target.

**Lingkungan uji jalur [U]:** satu basis kode JavaScript/TypeScript dengan komponen React Native dalam proyek Expo; target web dan Android dijalankan dari proyek yang sama. Alat: Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`) dan Expo Go atau development build pada emulator/perangkat Android; versi SDK Expo dicatat. Dua target wajib berbeda runtime/platform (web dan Android), bukan dua ukuran layar. Butir, bobot dan ambang **sama** dengan [KFC-506 netral](034_RENCANA_EVALUASI_ASESMEN_KFC-506_07112026_1332.md) dan 010; yang berubah hanya alat, kondisi uji dan istilah teknis yang wajar untuk jalur ini.

## Matriks asesmen dan ketentuan

| Instrumen | Pekan | CPMK | Bobot MK | Teknik/bukti |
|---|---:|---|---:|---|
| Tugas 1 | 4 | 04.1 | 20% | Produk/rancangan dan penjelasan sesuai kasus |
| UTS | 8 | 04.2 | 25% | Unjuk kerja/ujian praktik dan hasil uji |
| Tugas 2 | 12 | 04.3 | 25% | Unjuk kerja dan lima hasil uji |
| UAS | 16 | 04.4 | 30% | Produk terintegrasi, demonstrasi dan hasil uji |
| **Total** | | | **100%** | |

Bobot, instrumen, kasus, target dan kondisi di bawah adalah usulan, bukan keputusan resmi. Contoh input dapat disesuaikan pengampu sebelum diberitahukan kepada mahasiswa; jangan menambah butir atau bobot tanpa revisi kisi-kisi. Durasi, moda, individu/kelompok, akses alat, penyerahan dan remedial [K] diputuskan prodi/pengampu. Proyek kelompok tetap menyertakan penjelasan individu. Data harus dummy/berizin; jangan menyimpan rahasia atau data pribadi nyata pada penyimpanan lokal.

### Tugas 1, pekan 4 — 04.1 / 20%

**Instruksi mahasiswa:** Siapkan proyek React Native + Expo dengan satu aksi sederhana pada dua target (web dan Android); serahkan kode bersama, konfigurasi, petunjuk menjalankan dan bukti berjalan pada masing-masing target.

**Keluaran:** Satu proyek, petunjuk menjalankan dan bukti dua target.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | proyek Expo berjalan di target web. | Jalankan `npx expo start` lalu buka target web di browser. | Aplikasi berjalan di target web. | Diisi penilai |
| 2 | proyek yang sama berjalan di target Android. | Buka proyek yang sama di Expo Go atau development build pada Android. | Aplikasi berjalan di target Android. | Diisi penilai |
| 3 | aksi sederhana berjalan di target web. | Lakukan aksi tambah data dummy di target web. | Aksi bekerja sesuai kasus di target web. | Diisi penilai |
| 4 | aksi yang sama berjalan di target Android. | Lakukan aksi tambah yang sama di target Android. | Aksi bekerja sesuai kasus di target Android. | Diisi penilai |
| 5 | kode bersama dan konfigurasi dua target dapat ditunjukkan. | Tunjukkan direktori `app`, `package.json` dan konfigurasi kedua target. | Satu basis kode React Native dan konfigurasi target web/Android dapat ditunjukkan. | Diisi penilai |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi mahasiswa:** Buat UI adaptif pada dua target dan buktikan label aksesibilitas, fokus/pembaca layar pada target yang mendukung, serta umpan balik interaksi sesuai lima cek.

**Keluaran:** Proyek UI, tangkapan dua target dan daftar hasil uji.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | layout daftar terbaca di target web. | Tampilkan daftar perlengkapan pada lebar browser desktop. | Layout terbaca di target web. | Diisi penilai |
| 2 | layout daftar yang sama terbaca di target Android. | Tampilkan daftar yang sama di emulator atau perangkat Android. | Layout terbaca di target Android. | Diisi penilai |
| 3 | kontrol memiliki label aksesibilitas. | Periksa `accessibilityLabel`/`accessibilityRole` pada kontrol interaktif kedua target. | Kontrol memiliki label yang dapat dibacakan pembaca layar. | Diisi penilai |
| 4 | fokus/pembaca layar diuji pada target yang mendukung. | Uji fokus keyboard di web dan TalkBack di Android; catat hasilnya. | Hasil pengujian fokus/pembaca layar tercatat. | Diisi penilai |
| 5 | interaksi memberi umpan balik yang jelas di kedua target. | Lakukan aksi tambah atau hapus dan amati umpan balik pada kedua target. | Umpan balik interaksi terlihat jelas di kedua target. | Diisi penilai |

### Tugas 2, pekan 12 — 04.3 / 25%

**Instruksi mahasiswa:** Bangun navigasi, state dan penyimpanan lokal dengan penanganan data invalid/kegagalan; serahkan proyek dan lima uji, termasuk pemulihan setelah aplikasi dibuka ulang.

**Keluaran:** Proyek, data dummy, tabel lima uji dan penjelasan individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | state berubah sesuai aksi. | Tambah satu item lewat form lalu amati daftar. | State daftar berubah dan tampilan diperbarui. | Diisi penilai |
| 2 | navigasi maju/kembali bekerja. | Buka halaman detail lalu kembali ke daftar. | Navigasi Expo Router/React Navigation bekerja dan state kasus tetap konsisten. | Diisi penilai |
| 3 | data tersimpan lokal. | Simpan data dummy memakai `expo-sqlite` atau async storage. | Data tersimpan pada mekanisme yang dipilih. | Diisi penilai |
| 4 | data dipulihkan saat aplikasi dibuka ulang. | Tutup dan buka ulang aplikasi pada target yang diuji. | Data dummy dipulihkan. | Diisi penilai |
| 5 | kegagalan penyimpanan atau data invalid memberi pesan yang dapat dipahami. | Kirim stok negatif atau simulasikan kegagalan penyimpanan. | Pesan yang dapat dipahami ditampilkan. | Diisi penilai |

### UAS, pekan 16 — 04.4 / 30%

**Instruksi mahasiswa:** Integrasikan aplikasi satu basis kode pada dua target; serahkan proyek, petunjuk, hasil uji lintas target, keterbatasan, perbaikan dan demonstrasi individu.

**Keluaran:** Satu proyek, bukti dua target, matriks uji dan demonstrasi individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | satu basis kode Expo/React Native terintegrasi. | Tunjukkan proyek dengan fitur kasus saling terhubung. | Fitur dibangun dalam satu basis kode React Native. | Diisi penilai |
| 2 | fitur utama berjalan di target web. | Jalankan fitur utama pada build web. | Fitur utama berjalan di target web. | Diisi penilai |
| 3 | fitur utama berjalan di target Android. | Jalankan fitur utama di Expo Go atau development build Android. | Fitur utama berjalan di target Android. | Diisi penilai |
| 4 | hasil uji, perbedaan target dan perbaikan dicatat. | Periksa hasil `jest-expo` dan catatan perbedaan modul/Expo Go. | Hasil uji, perbedaan dan perbaikan dicatat. | Diisi penilai |
| 5 | petunjuk menjalankan dan demonstrasi tersedia. | Ikuti petunjuk menjalankan lalu lakukan demonstrasi individu. | Petunjuk dan demonstrasi tersedia. | Diisi penilai |

## Bukti, skor dan umpan balik

Catat untuk setiap butir kondisi, input, langkah, hasil aktual dan bukti; nilai menggunakan [rubrik biner](043_RUBRIK_PENILAIAN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md). Sediakan akses dan alat yang setara, termasuk perangkat/emulator pinjaman bila komputer mahasiswa tidak mampu; jangan menuntut perangkat pribadi. Skor instrumen = jumlah lima skor butir / 5. Nilai MK = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Target usulan CPMK adalah ≥4 cek terpenuhi dari 5; bukan standar kelulusan resmi. Rekap capaian individu, umpan balik dan hambatan untuk CQI tanpa mengklaim hasil sebelum pengukuran.

**Sebelum digunakan [K]:** verifikasi kesesuaian soal dengan CPMK dan jumlah cek, coba simulasi waktu dan fasilitas (termasuk waktu build/refresh pada kedua target), tentukan alternatif akses, sahkan jadwal dan rubrik serta kebijakan remedial. Lima cek dan masing-masing 20% dari skor instrumen tetap sama dengan 010 dan 034.
