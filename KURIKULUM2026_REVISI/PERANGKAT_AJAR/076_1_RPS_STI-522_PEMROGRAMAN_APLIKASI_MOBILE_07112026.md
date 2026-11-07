# 076_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STI-522 — Pemrograman Aplikasi Mobile

**Identitas:** `STI-522` Pemrograman Aplikasi Mobile · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-311`, `STI-416` · PL-3 · PEO-1, PEO-2 · IRM R · Rubrik K-2.

## 1. Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tanggal dan tanda tangan: **diisi pada pengesahan**. Beban per minggu: **TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit**; PT = penugasan terstruktur, BM = belajar mandiri.

## 2. CPL yang dibebankan

| CPL | Rumusan Dok 003 | IRM |
| --- | --- | --- |
| `CPL-08` (`P4`) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | R |
| `CPL-13` (`KK5`) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | R |

## 3. CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD (Dok 043) | Bloom | CPL (Dok 004) |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **membangun** antarmuka aplikasi mobile responsif multi-device (*B*) menggunakan framework Flutter dan bahasa Dart (*C*) dengan prinsip Material Design 3 (*D*). | C3 | CPL-08 (P4) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengimplementasikan** arsitektur state management yang scalable (*B*) menggunakan Business Logic Component (BLoC) Pattern (*C*) secara terstruktur (*D*). | C4 | CPL-13 (KK5) |
| `CPMK-3` | Mahasiswa (*A*) mampu **mengintegrasikan** persistensi data lokal (SQLite/SharedPreferences) dan sinkronisasi RESTful API (*B*) pada aplikasi mobile (*C*) dengan penanganan offline-mode yang andal (*D*). | C4 | CPL-13 (KK5) |
| `CPMK-4` | Mahasiswa (*A*) mampu **membangun dan merilis** aplikasi mobile (*B*) dengan integrasi sensor perangkat keras (Kamera, GPS Geolocation) dan push notification Firebase (*C*) ke dalam paket APK/AAB rilis (*D*). | C6 | CPL-13 (KK5) |

| Kode | Kompetensi spesifik Dok 043 | CPMK menurut Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Membangun aplikasi mobile cross-platform menggunakan Flutter/Dart. | `CPMK-1` | C3 |
| `Sub-CPMK-1.2` | Menerapkan konsep lifecycle dan UI widget pada pengembangan antarmuka mobile. | `CPMK-1` | C3 |
| `Sub-CPMK-2.1` | Mengimplementasikan akses sensor perangkat (GPS, kamera, push notification). | `CPMK-2` | C4 |
| `Sub-CPMK-2.2` | Menerapkan penyimpanan lokal SQLite/Hive pada aplikasi mobile. | `CPMK-2` | C4 |
| `Sub-CPMK-3.1` | Mengintegrasikan aplikasi mobile dengan REST API untuk sinkronisasi offline-to-online. | `CPMK-3` | C4 |
| `Sub-CPMK-3.2` | Mengelola state aplikasi mobile secara konsisten. | `CPMK-3` | C4 |
| `Sub-CPMK-4.1` | Menguji dan merilis aplikasi mobile pada perangkat nyata. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Membangun aplikasi mobile end-to-end yang terintegrasi dan siap rilis. | `CPMK-4` | C6 |

## 4. Analisis pembelajaran dan korelasi penilaian

Alur belajar: pengenalan dan pemodelan → penerapan dan analisis → integrasi serta evaluasi. Penilaian bersifat kumulatif; pengalokasian nilai CPMK berikut merupakan rancangan operasional, bukan bobot resmi CPL prodi.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-08 (P4) | 20% | — | — | — | 20% |
| CPMK-2 | CPL-13 (KK5) | — | 25% | — | — | 25% |
| CPMK-3 | CPL-13 (KK5) | — | — | 25% | — | 25% |
| CPMK-4 | CPL-13 (KK5) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

CPL yang didukung bersama oleh sebuah CPMK menggunakan **bukti yang sama**; nilai tidak dijumlahkan ulang sebagai persentase nilai akhir. Cara menghitung capaian masing-masing CPL dijelaskan di dokumen 4.

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 5. Deskripsi dan rencana 16 pertemuan

Mata kuliah mengembangkan kompetensi sesuai CPMK melalui kasus di atas dengan Flutter, Dart, emulator, flutter_bloc, SQLite dan REST API mock. Teknik penilaian dan indikator spesifik tiap instrumen ada pada dokumen 4 dan 5.

| Mg | Sub-CPMK terkait | Kemampuan / indikator | Materi | Metode | Alokasi belajar per minggu | Asesmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sub-CPMK-1.1 | Mampu menguraikan ekosistem mobile multi-platform dan setup Flutter (C2) | Pengantar Mobile Development, Flutter SDK, Dart Syntax, Null Safety | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 2 | Sub-CPMK-1.2 | Mampu mengonstruksi Stateless Widget vs Stateful Widget (C3) | Widget Fundamentals: MaterialApp, Scaffold, AppBar, Lifecycle Widget | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 3 | Sub-CPMK-1.2 | Mampu merancang layout responsif multi-layar (Row, Column, Stack, Grid) (C3) | Layouting Mobile: Container, Flexbox-like Row/Col, ListView, GridView | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 4 | Sub-CPMK-1.1 | Mampu menerapkan tema visual dinamis Material Design 3 & aset (C3) | Styling & Assets: Custom Fonts, Vector SVG, Material Design 3 Theme | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 (20%) |
| 5 | Sub-CPMK-1.2 | Mampu mengonfigurasi navigasi multi-halaman via Navigator 2.0 / GoRouter (C3) | Routing & Navigation: Deep Linking, Parameter Passing, Navigation Stack | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 6 | Sub-CPMK-3.2 | Mampu menerapkan state management lokal setState dan InheritedWidget (C3) | State Management Fundamental: Ephemeral State vs App State | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 7 | Sub-CPMK-3.2 | Mampu mengimplementasikan State Management BLoC (Events, States, Bloc) (C4) | BLoC Architecture: Reactive Programming with RxDart & Flutter Bloc | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 8 | Sub-CPMK-3.2 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal UI Mobile Responsif & State Management BLoC | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS (25%) |
| 9 | Sub-CPMK-2.2 | Mampu mengimplementasikan persistensi database lokal SQLite (sqflite) (C4) | Local Data Storage: SQLite CRUD, Object Mapping, Secure Storage | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 10 | Sub-CPMK-3.1 | Mampu mengintegrasikan konsumsi REST API backend menggunakan HTTP client (C4) | Networking: Dio Client, JSON Parsing to Dart Model, Interceptors | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 11 | Sub-CPMK-3.1 | Mampu menangani caching data lokal dan strategi sinkronisasi offline (C4) | Offline-First Architecture: Local Caching & Background Sync | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 12 | Sub-CPMK-3.1 | Menguji penyimpanan lokal, API mock dan pemulihan koneksi. | Sinkronisasi offline dan pengujian integrasi | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 (25%) |
| 13 | Sub-CPMK-2.1 | Mampu mengintegrasikan peta interaktif Google Maps SDK (C4) | Map Integration: Google Maps Widget, Custom Markers, Polyline Routing | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 14 | Sub-CPMK-2.1 | Mampu mengintegrasikan Firebase Auth dan Firebase Cloud Messaging (FCM) (C4) | Cloud Integration: Firebase Authentication & Push Notifications | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 15 | Sub-CPMK-4.1 | Mampu melakukan testing aplikasi dan generate bundle rilis APK/AAB (C6) | Unit/Widget Testing, App Signing Key, ProGuard, Generate AAB Release | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 16 | Sub-CPMK-4.1, Sub-CPMK-4.2 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Aplikasi Mobile Terpadu & Ujian Portofolio | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS (30%) |

## 6. Ringkasan instrumen

- **Tugas 1 (20%, pekan 4): Antarmuka responsif** — Bangun layar daftar dan detail dengan widget stateful/stateless, navigasi dan tema Material 3. Bukti: Kode, tangkapan layar dua ukuran dan petunjuk menjalankan. Cek: responsivitas, navigasi, konsistensi tema dan validasi input.
- **UTS (25%, pekan 8): Ujian BLoC** — Implementasikan satu alur event-state untuk memuat dan memfilter daftar; demonstrasikan state loading, sukses dan gagal. Bukti: Kode individual, diagram event-state dan hasil uji. Cek: pemisahan state, transisi benar dan penanganan galat.
- **Tugas 2 (25%, pekan 12): Sinkronisasi luring** — Hubungkan API mock dengan cache SQLite dan tentukan strategi antrean sinkronisasi saat koneksi kembali. Bukti: Kode, skema data, uji online/offline dan penjelasan konflik. Cek: ketahanan offline, parsing, privasi dan bukti uji.
- **UAS (30%, pekan 16): Aplikasi siap rilis** — Integrasikan fitur kamera/GPS dan notifikasi simulasi dengan persetujuan pengguna; uji dan hasilkan paket debug/release sesuai lingkungan. Bukti: Repositori, test report, paket atau bukti build, demo dan daftar izin. Cek: fungsionalitas, pengujian, pengelolaan izin dan instruksi rilis.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS12` *Web and Mobile App Development*, `BK-IT04` *Platform Technologies*. Klasifikasi pembina menurut Dok 004: primer BK-IS12 dan BK-IT04.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Pengembangan Aplikasi Mobile Cross-Platform (Flutter / React Native), State Management Mobile, Integrasi REST API, Penyimpanan Lokal (SQLite/Preferences), Akses Fitur Hardware (Kamera, GPS).
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang native iOS Swift / Android Kotlin murni tingkat rendah, arsitektur backend server, desain grafis UI/UX dari nol.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan aplikasi bergerak terhubung; menyerahkan rekayasa platform skala enterprise ke `STI-727`.

**Catatan rekonsiliasi:** Dok 043 mengaitkan sensor dan SQLite dengan Sub-CPMK-2, serta state dengan Sub-CPMK-3, meski rumusan CPMK menempatkannya pada CPMK-4, CPMK-3 dan CPMK-2. Bukti dinilai menurut rumusan CPMK, kode sub sumber dipertahankan. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** Aplikasi layanan kampus memungkinkan pengguna melihat dan menyimpan agenda secara luring dan menyinkronkan kembali saat daring.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: Dokumentasi Flutter, Dart, flutter_bloc dan SQLite.
