# 040 — Outline modul dan praktikum KFC-506b

## KFC-506b — Sistem Aplikasi Lintas Platform (jalur React Native + Expo)

> **Status [U]: draf, belum disahkan.** Identitas MK, CPL04 dan BK02 bersumber dari buku KPT Teknik Informatika UWG; CPMK, isi, urutan, asesmen dan contoh adalah usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) bagian 14 dan [paket netral KFC-506](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md). Label **a–b adalah usulan jalur di bawah satu MK resmi KFC-506**, bukan kode KRS baru; lihat 010 bagian 14.1. Jalur lain: [KFC-506a — Dart + Flutter](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md). Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: daftar perlengkapan dummy dengan satu basis kode; dua target berbeda adalah **target web di browser desktop dan target Android di emulator/perangkat**. Dua ukuran layar pada satu target bukan dua target.

**Lingkungan jalur [U]:** satu basis kode JavaScript/TypeScript dengan komponen React Native dalam proyek Expo; target web dan Android dijalankan dari proyek yang sama. Persiapan: Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`) dan Expo Go atau development build pada emulator/perangkat Android; versi SDK Expo dicatat. Versi SDK, paket dan kanal rilis dicatat pengampu sebelum kuliah; tidak ada versi yang diwajibkan di sini.

**Pemakaian:** tiap bab adalah outline, bukan modul lengkap. Gunakan pertemuan 1–7 dan 9–15; minggu 8 dan 16 untuk evaluasi. Untuk tiap praktikum dosen menyiapkan alat, contoh, akses dan petunjuk; mahasiswa mencatat bukti serta refleksi. PT/BM dan pembagian waktu belum ditetapkan; semua contoh adalah usulan yang perlu disepakati sebelum penilaian. Perangkat terkait: [paket RPS/SAP](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) · [rencana evaluasi](042_RENCANA_EVALUASI_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) · [rubrik](043_RUBRIK_PENILAIAN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) · [netral 017](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md).

### Bab 1 — Diagnostik dan konsep satu basis kode dua target (pekan 1)

- **Sub-CPMK:** 04.1.1.
- **Materi:** Diagnostik JavaScript/TypeScript (React) dan web; konsep satu basis kode, dua target dan batas framework.
- **Praktikum:** Lakukan diagnostik JavaScript/TypeScript (React)/web dan buat proyek dengan `create-expo-app` lalu jalankan `npx expo start`; identifikasi satu basis kode, target web serta target Android, dan alat yang dibutuhkan.
- **Bukti/cek formatif:** Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R13; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 2 — Menyiapkan proyek dan konfigurasi target (pekan 2)

- **Sub-CPMK:** 04.1.1.
- **Materi:** Pembuatan proyek Expo/React Native, struktur berkas, dependensi dan konfigurasi target web serta Android.
- **Praktikum:** Buat proyek Expo/React Native; catat versi SDK/dependensi, siapkan konfigurasi target web dan Android, lalu catat langkah setup serta hambatan.
- **Bukti/cek formatif:** Proyek dan konfigurasi untuk dua target dapat disiapkan. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R13, R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 3 — Menjalankan aksi pertama pada dua target (pekan 3)

- **Sub-CPMK:** 04.1.2.
- **Materi:** Menjalankan aplikasi, input sederhana dan perbedaan perilaku antara target web dan Android.
- **Praktikum:** Jalankan aksi tambah data dummy pada kedua target dari basis kode yang sama; catat perbedaan hasil dan penyebabnya.
- **Bukti/cek formatif:** Aksi sederhana dijalankan pada kedua target. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R13, R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 4 — Menyiapkan bukti Tugas 1 (pekan 4)

- **Sub-CPMK:** 04.1.1, 04.1.2.
- **Materi:** Konsolidasi bukti kode bersama, konfigurasi dan hasil berjalan pada dua target untuk Tugas 1.
- **Praktikum:** Susun T1: tunjukkan kode bersama, konfigurasi, bukti berjalan dan aksi pada masing-masing target; lengkapi penjelasan individu.
- **Bukti/indikator asesmen:** Lima cek basis kode/aksi pada dua target Tugas 1 dibuktikan. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R13, R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.
- **Asesmen:** penilaian hanya pada lima cek instrumen Tugas 1; pengantar/pengayaan bukan kriteria tambahan.

### Bab 5 — Layout adaptif dan komponen lintas platform (pekan 5)

- **Sub-CPMK:** 04.2.1.
- **Materi:** Layout adaptif dan komponen lintas platform pada Expo/React Native.
- **Praktikum:** Bangun tampilan daftar perlengkapan memakai komponen Expo/React Native; jalankan pada kedua target dan catat penyesuaian.
- **Bukti/cek formatif:** Layout dan komponen menyesuaikan target yang disepakati. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 6 — Adaptasi ukuran, orientasi dan batas platform (pekan 6)

- **Sub-CPMK:** 04.2.1.
- **Materi:** Adaptasi ukuran layar, orientasi dan batas kemampuan tiap target.
- **Praktikum:** Bandingkan ukuran, orientasi dan kemampuan kedua target; catat perbedaan layout serta penyesuaian yang dilakukan.
- **Bukti/cek formatif:** Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 7 — Aksesibilitas dasar dan umpan balik interaksi (pekan 7)

- **Sub-CPMK:** 04.2.2.
- **Materi:** Label kontrol, fokus/pembaca layar dan umpan balik interaksi pada Expo/React Native.
- **Praktikum:** Terapkan `accessibilityLabel`/`accessibilityRole`/`accessibilityHint`; uji pada target yang mendukung dan dokumentasikan keterbatasan.
- **Bukti/cek formatif:** Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R15; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 8 — State dan pemutakhiran tampilan (pekan 9)

- **Sub-CPMK:** 04.3.1.
- **Materi:** State pada Expo/React Native dan pemutakhiran tampilan setelah aksi.
- **Praktikum:** Buat state daftar dan aksi tambah; buktikan perubahan state memperbarui tampilan pada kedua target.
- **Bukti/cek formatif:** Aksi mengubah state dan tampilan sesuai contoh. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R14, R15; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 9 — Navigasi antardua halaman (pekan 10)

- **Sub-CPMK:** 04.3.1.
- **Materi:** Navigasi Expo Router atau React Navigation dan konsistensi state antarhalaman.
- **Praktikum:** Tambahkan navigasi maju/kembali antara dua halaman dan uji konsistensi state pada kedua target.
- **Bukti/cek formatif:** Navigasi maju/kembali mempertahankan state sesuai kasus. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 10 — Penyimpanan lokal dan penanganan kegagalan (pekan 11)

- **Sub-CPMK:** 04.3.2.
- **Materi:** Penyimpanan lokal pada Expo/React Native, pemulihan data dan penanganan data invalid/kegagalan.
- **Praktikum:** Simpan data dummy memakai `expo-sqlite` atau async storage; uji pemulihan setelah aplikasi ditutup lalu dibuka ulang, serta kondisi gagal.
- **Bukti/cek formatif:** Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R15; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 11 — Menyiapkan bukti Tugas 2 (pekan 12)

- **Sub-CPMK:** 04.3.1, 04.3.2.
- **Materi:** Konsolidasi bukti state, navigasi dan penyimpanan lokal untuk Tugas 2.
- **Praktikum:** Demonstrasikan T2: state, navigasi, simpan, buka ulang dan pesan invalid/gagal; catat lima hasil uji.
- **Bukti/indikator asesmen:** Lima kasus state, navigasi dan persistensi Tugas 2 dicatat. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R14, R15; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.
- **Asesmen:** penilaian hanya pada lima cek instrumen Tugas 2; pengantar/pengayaan bukan kriteria tambahan.

### Bab 12 — Rancangan proyek terintegrasi (pekan 13)

- **Sub-CPMK:** 04.4.1.
- **Materi:** Rancangan kasus proyek dan integrasi fitur dalam satu basis kode.
- **Praktikum:** Rancang proyek dan fitur bersama; siapkan data mock lokal agar tidak bergantung pada MK lain.
- **Bukti/cek formatif:** Rancangan proyek menunjukkan kasus dan fitur bersama. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R13, R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 13 — Integrasi proyek pada dua target (pekan 14)

- **Sub-CPMK:** 04.4.1.
- **Materi:** Integrasi antarmuka, state dan data lokal, lalu menjalankannya pada dua target.
- **Praktikum:** Integrasikan fitur utama dan jalankan pada target web serta Android; catat perbaikan yang diperlukan.
- **Bukti/cek formatif:** Fitur terintegrasi berjalan pada dua target berbeda. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R13, R14; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

### Bab 14 — Uji lintas target dan dokumentasi keterbatasan (pekan 15)

- **Sub-CPMK:** 04.4.2.
- **Materi:** Uji lintas target, dokumentasi perbedaan perilaku dan perbaikan.
- **Praktikum:** Buat matriks uji dua target (`jest-expo` dan uji manual per target); catat hasil aktual, perbedaan, perbaikan dan petunjuk menjalankan.
- **Bukti/cek formatif:** Matriks hasil uji, perbedaan target dan perbaikan tersedia. Simpan hasil, langkah dan satu kesulitan/perbaikan.
- **Refleksi:** Jelaskan hubungan hasil praktikum dengan indikator dan satu hal yang masih perlu diperbaiki.
- **Pustaka:** R14, R15; tautan lengkap pada [paket RPS/SAP jalur ini](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) bagian 5.

## Perbedaan jalur a dan b [U]

| Aspek | Jalur a — Dart + Flutter | Jalur b — React Native + Expo |
|---|---|---|
| Bahasa dan UI | Dart; widget dan render engine Flutter | JavaScript/TypeScript; komponen React Native |
| Alat utama | Flutter SDK, `flutter doctor`, editor dengan ekstensi Flutter | Node.js LTS, `create-expo-app`, Expo CLI, Expo Go/development build |
| Navigasi | `Navigator` dan route Flutter | Expo Router atau React Navigation |
| State | `StatefulWidget`, `setState` | `useState`/`useReducer` |
| Penyimpanan lokal | `sqflite`/`path` di Android; alternatif untuk web dicatat keterbatasannya | `expo-sqlite` atau async storage (key-value, tidak terenkripsi) |
| Aksesibilitas | `Semantics`, label dan urutan fokus | `accessibilityLabel`, `accessibilityRole`, `accessibilityHint` |
| Uji | `flutter test`, integration test | `jest-expo`, Testing Library, uji manual per target |
| Pustaka | R13–R15 | R16–R18 |

Kesamaan yang dipertahankan: CPMK04.1–04.4 beserta Sub-CPMK yang sama polanya, empat instrumen T1/UTS/T2/UAS 20/25/25/30, lima cek biner bernilai sama per instrumen, target usulan ≥4/5, kasus dummy, dan dua target web + Android. Perbedaan hanya pada teknologi, alat dan bukti yang wajar untuk jalur tersebut — bukan tambahan butir atau bobot.

## Tindak lanjut

Pengampu mengembangkan penjelasan konsep, lembar kerja, contoh input, bahan yang dapat diakses dan alternatif bila SDK/emulator tidak tersedia; uji kelayakan fasilitas dan waktu sebelum mengunci jalur. Gunakan [rencana evaluasi](042_RENCANA_EVALUASI_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) dan [rubrik](043_RUBRIK_PENILAIAN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) untuk penilaian.
