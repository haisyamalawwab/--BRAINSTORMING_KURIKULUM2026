# 043 — Rubrik penilaian pembelajaran KFC-506b

## KFC-506b — Sistem Aplikasi Lintas Platform (jalur React Native + Expo)

> **Status [U]: draf, belum disahkan.** Identitas MK, CPL04 dan BK02 bersumber dari buku KPT Teknik Informatika UWG; CPMK, isi, urutan, asesmen dan contoh adalah usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) bagian 14 dan [paket netral KFC-506](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md). Label **a–b adalah usulan jalur di bawah satu MK resmi KFC-506**, bukan kode KRS baru; lihat 010 bagian 14.1. Jalur lain: [KFC-506a — Dart + Flutter](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md). Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: daftar perlengkapan dummy dengan satu basis kode; dua target berbeda adalah **target web di browser desktop dan target Android di emulator/perangkat**. Dua ukuran layar pada satu target bukan dua target.

## Penggunaan rubrik [U]

Gunakan lima cek untuk setiap instrumen; masing-masing **20% dari skor instrumen**. Skor cek **100** jika semua unsur cek dan hasil yang diharapkan terpenuhi serta dapat diverifikasi; **0** jika satu unsur gagal atau bukti tidak ada/tidak dapat diverifikasi. Butir gabungan mensyaratkan semua unsur. Kondisi contoh pada [rencana evaluasi](042_RENCANA_EVALUASI_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) adalah usulan operasional yang harus disepakati sebelum penilaian.

Untuk T1, cek terkait dibuktikan dengan menjalankan kedua build/target dari satu basis kode; untuk UTS/T2/UAS, cek dibuktikan pada aplikasi berjalan dan, bila digunakan, hasil `jest-expo` dan uji manual per target. T1 tidak menilai estetika atau kompleksitas kode. Kondisi ini bukan cek berbobot tambahan.

### Tugas 1, pekan 4 — 04.1 / 20%

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. proyek Expo berjalan di target web. | 20% | Aplikasi berjalan di target web. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. proyek yang sama berjalan di target Android. | 20% | Aplikasi berjalan di target Android. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. aksi sederhana berjalan di target web. | 20% | Aksi bekerja sesuai kasus di target web. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. aksi yang sama berjalan di target Android. | 20% | Aksi bekerja sesuai kasus di target Android. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. kode bersama dan konfigurasi dua target dapat ditunjukkan. | 20% | Satu basis kode React Native dan konfigurasi target web/Android dapat ditunjukkan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

### UTS, pekan 8 — 04.2 / 25%

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. layout daftar terbaca di target web. | 20% | Layout terbaca di target web. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. layout daftar yang sama terbaca di target Android. | 20% | Layout terbaca di target Android. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. kontrol memiliki label aksesibilitas. | 20% | Kontrol memiliki label yang dapat dibacakan pembaca layar. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. fokus/pembaca layar diuji pada target yang mendukung. | 20% | Hasil pengujian fokus/pembaca layar tercatat. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. interaksi memberi umpan balik yang jelas di kedua target. | 20% | Umpan balik interaksi terlihat jelas di kedua target. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

### Tugas 2, pekan 12 — 04.3 / 25%

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. state berubah sesuai aksi. | 20% | State daftar berubah dan tampilan diperbarui. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. navigasi maju/kembali bekerja. | 20% | Navigasi Expo Router/React Navigation bekerja dan state kasus tetap konsisten. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. data tersimpan lokal. | 20% | Data tersimpan pada mekanisme yang dipilih. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. data dipulihkan saat aplikasi dibuka ulang. | 20% | Data dummy dipulihkan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. kegagalan penyimpanan atau data invalid memberi pesan yang dapat dipahami. | 20% | Pesan yang dapat dipahami ditampilkan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

### UAS, pekan 16 — 04.4 / 30%

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. satu basis kode Expo/React Native terintegrasi. | 20% | Fitur dibangun dalam satu basis kode React Native. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. fitur utama berjalan di target web. | 20% | Fitur utama berjalan di target web. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. fitur utama berjalan di target Android. | 20% | Fitur utama berjalan di target Android. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. hasil uji, perbedaan target dan perbaikan dicatat. | 20% | Hasil uji, perbedaan dan perbaikan dicatat. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. petunjuk menjalankan dan demonstrasi tersedia. | 20% | Petunjuk dan demonstrasi tersedia. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

## Formatif, rekap dan CQI

Formatif: catat **terpenuhi / perlu perbaikan / belum ditunjukkan**, beri umpan balik; tidak menambah bobot nilai akhir. Skor instrumen = jumlah lima skor cek / 5; target usulan CPMK ≥4 cek terpenuhi. Contoh empat cek terpenuhi dan satu gagal → `(100+100+100+100+0)/5 = 80`. Bobot MK tetap T1 20%, UTS 25%, T2 25%, UAS 30%; bobot cek tidak dikalikan dua kali.

| Identitas mahasiswa | T1: lulus cek / skor | UTS: lulus cek / skor | T2: lulus cek / skor | UAS: lulus cek / skor | Nilai akhir | Umpan balik / perbaikan |
|---|---|---|---|---|---|---|
| Diisi dosen | — | — | — | — | — | — |

Nilai akhir = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Kode CPMK lokal per MK; jangan menghitung bobot asesmen sebagai capaian CPL otomatis. Simpan bukti individu dan ringkas pola kesulitan untuk CQI; remedial dan pelaporan menunggu keputusan prodi. Jika ingin skala bertingkat seperti contoh SISTEKIN, rumuskan ulang rubrik, bobot dan ambang serta dapatkan persetujuan terlebih dahulu; jangan mencampur skala itu dengan checklist biner ini.
