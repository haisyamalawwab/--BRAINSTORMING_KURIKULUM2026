# 034 — Rencana evaluasi dan asesmen

## KFC-506 — Sistem Aplikasi Lintas Platform

> **Status [U]: draf, belum disahkan.** Data MK, CPL dan BK bersumber dari buku KPT Teknik Informatika UWG; isi, asesmen dan contoh bersifat usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) dan [paket RPS/SAP](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md). Label KOM-526a–d (jika digunakan) adalah usulan jalur, bukan kode MK/KRS resmi. Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: daftar perlengkapan dummy dengan satu basis kode untuk dua target berbeda (misalnya browser desktop dan emulator Android jika tersedia); gunakan mock lokal.

## Matriks asesmen dan ketentuan

| Instrumen | Pekan | CPMK | Bobot MK | Teknik/bukti |
|---|---:|---|---:|---|
| Tugas 1 | 4 | 04.1 | 20% | Produk/rancangan dan penjelasan sesuai kasus |
| UTS | 8 | 04.2 | 25% | Unjuk kerja/ujian praktik dan hasil uji |
| Tugas 2 | 12 | 04.3 | 25% | Unjuk kerja dan lima hasil uji |
| UAS | 16 | 04.4 | 30% | Produk terintegrasi, demonstrasi dan hasil uji |
| **Total** | | | **100%** | |

Bobot, instrumen, kasus, target dan kondisi di bawah adalah usulan, bukan keputusan resmi. Contoh input dapat disesuaikan pengampu sebelum diberitahukan kepada mahasiswa; jangan menambah butir atau bobot tanpa revisi kisi-kisi. Durasi, moda, individu/kelompok, akses alat, penyerahan dan remedial [K] diputuskan prodi/pengampu. Proyek kelompok tetap menyertakan penjelasan individu. Data harus dummy/berizin.

### Tugas 1, pekan 4 — 04.1 / 20%

**Instruksi mahasiswa:** Siapkan satu proyek dengan aksi sederhana pada dua target yang disepakati; serahkan kode bersama, konfigurasi dan bukti berjalan pada masing-masing target.

**Keluaran:** Satu proyek, petunjuk menjalankan dan bukti dua target.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | target A berjalan. | Jalankan satu proyek pada target A yang ditetapkan. | Aplikasi berjalan pada A. | Diisi penilai. |
| 2 | target B berjalan. | Jalankan proyek yang sama pada target B berbeda. | Aplikasi berjalan pada B. | Diisi penilai. |
| 3 | aksi sederhana berjalan pada A. | Lakukan aksi sederhana pada A. | Aksi bekerja sesuai kasus di A. | Diisi penilai. |
| 4 | aksi sama berjalan pada B. | Lakukan aksi yang sama pada B. | Aksi bekerja sesuai kasus di B. | Diisi penilai. |
| 5 | kode bersama dan konfigurasi kedua target dapat ditunjukkan. | Tunjukkan source dan konfigurasi kedua target. | Kode bersama dan konfigurasi A/B dapat ditunjukkan. | Diisi penilai. |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi mahasiswa:** Buat UI adaptif pada dua target dan buktikan label, fokus/keyboard pada target yang mendukung, serta umpan balik interaksi sesuai lima cek.

**Keluaran:** Proyek UI, tangkapan dua target dan daftar hasil uji.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | layout target A terbaca. | Tampilkan layout pada target A. | Layout terbaca pada A. | Diisi penilai. |
| 2 | layout target B terbaca. | Tampilkan layout pada target B. | Layout terbaca pada B. | Diisi penilai. |
| 3 | kontrol memiliki label. | Periksa kontrol interaktif pada kedua target. | Kontrol memiliki label sesuai kasus. | Diisi penilai. |
| 4 | fokus/keyboard dasar diuji pada target yang mendukung. | Uji fokus/keyboard pada target yang mendukung. | Hasil pengujian fokus/keyboard dasar tercatat. | Diisi penilai. |
| 5 | interaksi memberi umpan balik yang jelas pada kedua target. | Lakukan aksi pada A dan B. | Interaksi memberi umpan balik jelas pada kedua target. | Diisi penilai. |

### Tugas 2, pekan 12 — 04.3 / 25%

**Instruksi mahasiswa:** Bangun navigasi, state dan penyimpanan lokal dengan penanganan data invalid/kegagalan; serahkan proyek dan lima uji, termasuk pemulihan setelah aplikasi dibuka ulang.

**Keluaran:** Proyek, data dummy, tabel lima uji dan penjelasan individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | state berubah sesuai aksi. | Lakukan aksi tambah item. | State berubah sesuai aksi. | Diisi penilai. |
| 2 | navigasi maju/kembali bekerja. | Masuk ke halaman lain lalu kembali. | Navigasi maju/kembali bekerja. | Diisi penilai. |
| 3 | data tersimpan lokal. | Simpan data dummy secara lokal. | Data tersimpan pada mekanisme yang dipilih. | Diisi penilai. |
| 4 | data dipulihkan saat aplikasi dibuka ulang. | Tutup dan buka kembali aplikasi pada kondisi uji. | Data dummy dipulihkan. | Diisi penilai. |
| 5 | kegagalan penyimpanan atau data invalid memberi pesan yang dapat dipahami. | Simulasikan kegagalan penyimpanan atau input invalid. | Pesan yang dapat dipahami ditampilkan. | Diisi penilai. |

### UAS, pekan 16 — 04.4 / 30%

**Instruksi mahasiswa:** Integrasikan aplikasi satu basis kode pada dua target; serahkan proyek, petunjuk, hasil uji lintas target, keterbatasan, perbaikan dan demonstrasi individu.

**Keluaran:** Satu proyek, bukti dua target, matriks uji dan demonstrasi individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | basis kode bersama terintegrasi. | Tunjukkan proyek terintegrasi. | Fitur dibangun dalam basis kode bersama. | Diisi penilai. |
| 2 | fitur utama berjalan pada target A. | Jalankan fitur utama pada target A. | Fitur utama berjalan pada A. | Diisi penilai. |
| 3 | fitur utama berjalan pada target B. | Jalankan fitur utama pada target B. | Fitur utama berjalan pada B. | Diisi penilai. |
| 4 | hasil uji/perbedaan target dan perbaikan dicatat. | Periksa matriks uji dan catatan target. | Hasil, perbedaan dan perbaikan dicatat. | Diisi penilai. |
| 5 | petunjuk menjalankan dan demonstrasi tersedia. | Periksa langkah menjalankan dan demonstrasi. | Petunjuk dan demonstrasi tersedia. | Diisi penilai. |

## Bukti, skor dan umpan balik

Catat untuk setiap butir kondisi, input, langkah, hasil aktual dan bukti; nilai menggunakan [rubrik biner](035_RUBRIK_PENILAIAN_KFC-506_07112026_1332.md). Sediakan akses dan alat yang setara; jangan unggah rahasia. Skor instrumen = jumlah lima skor butir / 5. Nilai MK = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Target usulan CPMK adalah ≥4 cek terpenuhi dari 5; bukan standar kelulusan resmi. Rekap capaian individu, umpan balik dan hambatan untuk CQI tanpa mengklaim hasil sebelum pengukuran.

**Sebelum digunakan [K]:** verifikasi kesesuaian soal dengan CPMK dan jumlah cek, coba simulasi waktu dan fasilitas, tentukan alternatif akses, sahkan jadwal dan rubrik serta kebijakan remedial. Lima cek dan masing-masing 20% dari skor instrumen tetap sama dengan 010.
