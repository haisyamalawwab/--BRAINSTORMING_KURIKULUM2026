# 031 — Rencana evaluasi dan asesmen

## KOM-526d — Sistem Aplikasi Web Python Flask

> **Status [U]: draf, belum disahkan.** Data MK, CPL dan BK bersumber dari buku KPT Teknik Informatika UWG; isi, asesmen dan contoh bersifat usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) dan [paket RPS/SAP](016_PAKET_RPS_SAP_ASESMEN_KOM-526D_SISTEM_APLIKASI_WEB_PYTHON_FLASK_07112026_1328.md). Label KOM-526a–d (jika digunakan) adalah usulan jalur, bukan kode MK/KRS resmi. Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: inventaris peralatan dummy dengan kategori–barang, nama/stok, admin yang mengelola dan petugas yang membaca.

**Kondisi implementasi jalur [U]:** route/view Flask dan sqlite3; pemeriksaan peran pada aplikasi Flask. Pada UTS/T2/UAS terapkan kondisi ini pada butir yang relevan, bukan butir tambahan; T1 tidak menilai kode. Ketentuan lengkap pada 010 bagian 13.3.

**Batas sesi:** logout mengakhiri akses browser yang diuji; tidak otomatis membatalkan salinan cookie Flask yang lama. Rencana belajar dan log merupakan formatif, tidak berbobot tambahan.

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

**Instruksi mahasiswa:** Rancang kebutuhan dan model data untuk kasus sistem yang disediakan; serahkan aktor, kebutuhan, alur, entitas/relasi dan keterlacakan rancangan.

**Keluaran:** Dokumen kebutuhan, alur, model data dan penjelasan individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | aktor dan peran teridentifikasi. | Periksa daftar aktor pada rancangan inventaris. | Admin dan petugas beserta peran teridentifikasi. | Diisi penilai. |
| 2 | minimal tiga kebutuhan dapat diuji. | Periksa daftar kebutuhan. | Sekurang-kurangnya tiga kebutuhan dapat diuji. | Diisi penilai. |
| 3 | alur utama tergambar. | Telusuri alur utama dari aktor ke hasil. | Alur utama tergambar dan dapat dijelaskan. | Diisi penilai. |
| 4 | minimal dua entitas dan relasinya terdefinisi. | Periksa model data. | Kategori dan barang (atau dua entitas setara) serta relasinya terdefinisi. | Diisi penilai. |
| 5 | kebutuhan terhubung ke data/alur. | Telusuri kebutuhan menuju alur/data. | Keterkaitan kebutuhan dengan data/alur tampak. | Diisi penilai. |

### UTS, pekan 8 — 04.2 / 25%

**Instruksi mahasiswa:** Implementasikan rute server dan CRUD pada database dummy; perlihatkan empat operasi serta penanganan data yang tidak ditemukan, disertai lima uji.

**Keluaran:** Server, database dummy dan hasil lima uji CRUD.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | create. | Pada database dummy, kirim data barang baru. | Barang dibuat melalui alur server dan database. | Diisi penilai. |
| 2 | read. | Baca barang yang dibuat. | Barang terambil dan ditampilkan. | Diisi penilai. |
| 3 | update. | Ubah stok barang dan baca ulang. | Stok baru tersimpan dan terbaca. | Diisi penilai. |
| 4 | delete. | Hapus barang lalu baca ulang. | Barang terhapus dan tidak lagi tersedia. | Diisi penilai. |
| 5 | permintaan untuk data yang tidak ditemukan ditangani. | Minta ID yang tidak ada. | Respons atau pesan tidak ditemukan ditangani. | Diisi penilai. |

UTS dilaksanakan di lab terisolasi dengan database dummy; login/peran belum dipersyaratkan pada UTS.

### Tugas 2, pekan 12 — 04.3 / 25%

**Instruksi mahasiswa:** Terapkan login, logout, sesi/peran dan validasi server pada aplikasi latihan; gunakan kueri terparameter, data dummy, matriks peran dan lima uji.

**Keluaran:** Kode, matriks peran dan hasil uji; gunakan pustaka pengelolaan kata sandi yang aman dan data dummy.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | login valid. | Login admin menggunakan kredensial dummy valid. | Akses terlindungi sesuai peran admin diperoleh. | Diisi penilai. |
| 2 | login tidak valid ditolak. | Coba login dengan sandi salah. | Login ditolak. | Diisi penilai. |
| 3 | akses peran tidak berwenang ditolak. | Login petugas dan kirim permintaan mengubah data admin. | Server menolak perubahan oleh peran tidak berwenang. | Diisi penilai. |
| 4 | logout mengakhiri akses sesi. | Logout lalu minta akses terlindungi dari browser yang sama. | Browser yang diuji tidak lagi memperoleh akses terlindungi. | Diisi penilai. |
| 5 | masukan invalid ditolak server dan data diproses dengan kueri terparameter. | Kirim stok negatif; periksa query yang memproses input. | Masukan invalid ditolak server dan nilai query diparameterisasi. | Diisi penilai. |

### UAS, pekan 16 — 04.4 / 30%

**Instruksi mahasiswa:** Integrasikan antarmuka, server, data dan akses sesuai rancangan; serahkan aplikasi lokal, petunjuk, uji alur normal/gagal dan demonstrasi individu.

**Keluaran:** Aplikasi lokal, data dummy, hasil uji dan demonstrasi individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | alur sesuai rancangan terintegrasi. | Jalankan alur utama sesuai rancangan, dari antarmuka ke server. | Alur terintegrasi sesuai rancangan. | Diisi penilai. |
| 2 | data tersimpan dan terbaca. | Simpan data dummy lalu baca kembali. | Data tersimpan dan dapat dibaca. | Diisi penilai. |
| 3 | pembatasan akses bekerja. | Coba akses kedua peran pada fitur yang dibatasi. | Pembatasan akses sesuai peran bekerja. | Diisi penilai. |
| 4 | alur salah ditangani dan dicatat. | Coba satu alur gagal dan periksa catatan. | Kegagalan ditangani dan dicatat. | Diisi penilai. |
| 5 | petunjuk lokal, hasil uji dan perbaikan tersedia. | Periksa petunjuk, uji dan catatan perbaikan. | Ketiganya tersedia dan dapat dijelaskan. | Diisi penilai. |

## Bukti, skor dan umpan balik

Catat untuk setiap butir kondisi, input, langkah, hasil aktual dan bukti; nilai menggunakan [rubrik biner](032_RUBRIK_PENILAIAN_KOM-526D_07112026_1332.md). Sediakan akses dan alat yang setara; jangan unggah rahasia. Skor instrumen = jumlah lima skor butir / 5. Nilai MK = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Target usulan CPMK adalah ≥4 cek terpenuhi dari 5; bukan standar kelulusan resmi. Rekap capaian individu, umpan balik dan hambatan untuk CQI tanpa mengklaim hasil sebelum pengukuran.

**Sebelum digunakan [K]:** verifikasi kesesuaian soal dengan CPMK dan jumlah cek, coba simulasi waktu dan fasilitas, tentukan alternatif akses, sahkan jadwal dan rubrik serta kebijakan remedial. Lima cek dan masing-masing 20% dari skor instrumen tetap sama dengan 010.
