# 076_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STI-522 — Pemrograman Aplikasi Mobile

**Identitas:** `STI-522` Pemrograman Aplikasi Mobile · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-311`, `STI-416` · PL-3 · PEO-1, PEO-2 · IRM R · Rubrik K-2.

## 1. Rancangan empat titik asesmen

| Instrumen | Pekan | Bobot MK | Alokasi CPMK dari bobot MK | Bukti utama | Produk |
| --- | --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 20% | Antarmuka responsif | Kode, tangkapan layar dua ukuran dan petunjuk menjalankan |
| UTS | 8 | 25% | CPMK-2 25% | Ujian BLoC | Kode individual, diagram event-state dan hasil uji |
| Tugas 2 | 12 | 25% | CPMK-3 25% | Sinkronisasi luring | Kode, skema data, uji online/offline dan penjelasan konflik |
| UAS | 16 | 30% | CPMK-4 30% | Aplikasi siap rilis | Repositori, test report, paket atau bukti build, demo dan daftar izin |

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 2. Matriks alokasi per CPMK

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-08 (P4) | 20% | — | — | — | 20% |
| CPMK-2 | CPL-13 (KK5) | — | 25% | — | — | 25% |
| CPMK-3 | CPL-13 (KK5) | — | — | 25% | — | 25% |
| CPMK-4 | CPL-13 (KK5) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

### Cara penghitungan ketercapaian

Nilai setiap instrumen (0–100) dihitung dari rubrik dokumen 5. Nilai akhir = jumlah (bobot instrumen / 100 × nilai instrumen). Bila satu instrumen mengukur lebih dari satu CPMK, penguji memberi **skor butir terpisah per CPMK**, bukan menyalin skor total. Skor instrumen = Σ(alokasi bobot MK tiap CPMK pada instrumen × skor bagian CPMK) / bobot instrumen; ini juga mencegah hitung ganda. Nilai CPMK j = Σ(alokasi bobot instrumen untuk j × skor butir j) / Σ(alokasi bobot instrumen untuk j). Nilai CPL = rata-rata tertimbang nilai CPMK yang mendukung CPL tersebut, memakai total alokasi masing-masing CPMK sebagai bobot; hasil antar-CPL tidak dijumlahkan sebagai nilai akhir. Ini rancangan lokal untuk pemantauan, bukan persentase CPL yang telah disahkan.

Contoh operasional: skor butir 80 pada alokasi 20% dan 70 pada alokasi 10% menghasilkan (20×80 + 10×70)/30 = 76,67 untuk CPMK itu. Ambang awal pemantauan 70/100 **usulan**; batas lulus, remedial, proporsi dan kebijakan resmi ditetapkan prodi.

## 3. Kisi-kisi dan rencana tugas

### Tugas 1 — Antarmuka responsif

- **Waktu/bobot:** pekan 4, 20% nilai MK. **Kisi-kisi CPMK:** CPMK-1 (20 poin bobot MK).
- **Masalah dan instruksi:** Bangun layar daftar dan detail dengan widget stateful/stateless, navigasi dan tema Material 3.
- **Bukti wajib:** Kode, tangkapan layar dua ukuran dan petunjuk menjalankan.
- **Indikator:** responsivitas, navigasi, konsistensi tema dan validasi input.
- **Pelaksanaan:** kerja berbasis kasus/proyek; penilaian individual melalui kontribusi dan tanya jawab; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### UTS — Ujian BLoC

- **Waktu/bobot:** pekan 8, 25% nilai MK. **Kisi-kisi CPMK:** CPMK-2 (25 poin bobot MK).
- **Masalah dan instruksi:** Implementasikan satu alur event-state untuk memuat dan memfilter daftar; demonstrasikan state loading, sukses dan gagal.
- **Bukti wajib:** Kode individual, diagram event-state dan hasil uji.
- **Indikator:** pemisahan state, transisi benar dan penanganan galat.
- **Pelaksanaan:** ujian individual dengan bukti dan klarifikasi lisan; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### Tugas 2 — Sinkronisasi luring

- **Waktu/bobot:** pekan 12, 25% nilai MK. **Kisi-kisi CPMK:** CPMK-3 (25 poin bobot MK).
- **Masalah dan instruksi:** Hubungkan API mock dengan cache SQLite dan tentukan strategi antrean sinkronisasi saat koneksi kembali.
- **Bukti wajib:** Kode, skema data, uji online/offline dan penjelasan konflik.
- **Indikator:** ketahanan offline, parsing, privasi dan bukti uji.
- **Pelaksanaan:** kerja berbasis kasus/proyek; penilaian individual melalui kontribusi dan tanya jawab; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### UAS — Aplikasi siap rilis

- **Waktu/bobot:** pekan 16, 30% nilai MK. **Kisi-kisi CPMK:** CPMK-4 (30 poin bobot MK).
- **Masalah dan instruksi:** Integrasikan fitur kamera/GPS dan notifikasi simulasi dengan persetujuan pengguna; uji dan hasilkan paket debug/release sesuai lingkungan.
- **Bukti wajib:** Repositori, test report, paket atau bukti build, demo dan daftar izin.
- **Indikator:** fungsionalitas, pengujian, pengelolaan izin dan instruksi rilis.
- **Pelaksanaan:** proyek tim dengan bukti kolaborasi, demonstrasi dan pembelaan individual; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

## 4. Integritas, umpan balik dan CQI

Nilai kelompok dikonfirmasi dengan kontribusi dan pembelaan individual. Dosen mencatat skor per butir/CPMK dan umpan balik, memberi kesempatan klarifikasi dan remediasi sesuai peraturan prodi; remediasi tidak otomatis menambah komponen nilai kelima. Pada akhir semester, rekap sebaran capaian tiap CPMK dan CPL, analisis soal/bukti dengan capaian rendah, catat penyebab, rencana perbaikan, penanggung jawab dan tindak lanjut pada siklus PPEPP. Jaga data pribadi dan arsipkan bukti sesuai kebijakan institusi.

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
