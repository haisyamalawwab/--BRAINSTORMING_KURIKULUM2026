# 019 — Rencana evaluasi dan asesmen

## KOM-312 — Pemrograman Web

> **Status [U]: draf, belum disahkan.** Data MK, CPL dan BK bersumber dari buku KPT Teknik Informatika UWG; isi, asesmen dan contoh bersifat usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) dan [paket RPS/SAP](012_PAKET_RPS_SAP_ASESMEN_KOM-312_PEMROGRAMAN_WEB_07112026_1328.md). Label KOM-526a–d (jika digunakan) adalah usulan jalur, bukan kode MK/KRS resmi. Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.

Kasus: halaman informasi kegiatan kampus fiktif; formulir dengan contoh jumlah peserta 1–10. Gunakan aset berizin dan data dummy.

## Matriks asesmen dan ketentuan

| Instrumen | Pekan | CPMK | Bloom | Bobot MK | Teknik/bukti |
|---|---:|---|---|---:|---|
| Tugas 1 | 4 | 04.1 | C3 | 20% | Produk/rancangan dan penjelasan sesuai kasus |
| UTS | 8 | 04.2 | C3 | 25% | Unjuk kerja/ujian praktik dan hasil uji |
| Tugas 2 | 12 | 04.3 | C4 | 25% | Unjuk kerja dan lima hasil uji |
| UAS | 16 | 04.4 | C6 | 30% | Produk terintegrasi, demonstrasi dan hasil uji |
| **Total** | | | | **100%** | |

Bobot, instrumen, kasus, target dan kondisi di bawah adalah usulan, bukan keputusan resmi. Contoh input dapat disesuaikan pengampu sebelum diberitahukan kepada mahasiswa; jangan menambah butir atau bobot tanpa revisi kisi-kisi. Durasi, moda, individu/kelompok, akses alat, penyerahan dan remedial [K] diputuskan prodi/pengampu. Proyek kelompok tetap menyertakan penjelasan individu. Data harus dummy/berizin.

### Tugas 1, pekan 4 — 04.1 / 20% · Bloom C3

**Instruksi mahasiswa:** Buat halaman informasi HTML untuk kasus yang disediakan; sertakan konten, navigasi, tabel dan formulir. Serahkan HTML, aset dan daftar cek; CSS tidak dinilai.

**Keluaran:** HTML, aset berizin dan daftar cek; CSS tidak dinilai.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | struktur semantik. | Buka halaman kegiatan; periksa struktur dokumen dan bagian semantik. | Struktur semantik sesuai kasus dan dapat diidentifikasi. | Diisi penilai. |
| 2 | hierarki heading. | Amati urutan heading halaman. | Hierarki heading menunjukkan struktur konten yang logis. | Diisi penilai. |
| 3 | navigasi dan gambar ber-alt. | Aktifkan navigasi dan periksa gambar. | Tautan menuju tujuan dan gambar memiliki alt sesuai isi. | Diisi penilai. |
| 4 | tabel berheader. | Periksa tabel agenda. | Tabel memiliki header terkait data sesuai kasus. | Diisi penilai. |
| 5 | formulir berlabel dan validasi HTML. | Coba formulir berlabel dan masukan kosong. | Label terhubung dan validasi HTML dasar berfungsi. | Diisi penilai. |

T1 menilai HTML; pengantar CSS tidak dinilai pada T1.

### UTS, pekan 8 — 04.2 / 25% · Bloom C3

**Instruksi mahasiswa:** Terapkan CSS/Flexbox dan media query pada HTML yang disediakan; tampilkan dua lebar layar. Serahkan berkas dan tangkapan yang mendukung lima cek UTS pada bagian 4 (sumber: 010 bagian 3.4).

**Keluaran:** Berkas HTML/CSS dan tangkapan dua lebar.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | selektor/tipografi. | Periksa aturan selektor dan hasil tipografi. | Selektor bekerja dan teks mengikuti spesifikasi kasus. | Diisi penilai. |
| 2 | box model. | Amati margin, padding dan border kartu. | Box model diterapkan sesuai spesifikasi. | Diisi penilai. |
| 3 | Flexbox. | Amati struktur dan hasil navigasi/kartu. | Flexbox digunakan dan layout sesuai kasus. | Diisi penilai. |
| 4 | tampilan lebar terbaca. | Buka halaman pada lebar yang disepakati sebagai lebar. | Konten utama terbaca pada lebar tersebut. | Diisi penilai. |
| 5 | tampilan sempit terbaca tanpa overflow utama. | Buka pada lebar sempit yang disepakati. | Konten utama terbaca tanpa overflow utama. | Diisi penilai. |

### Tugas 2, pekan 12 — 04.3 / 25% · Bloom C4

**Instruksi mahasiswa:** Buat formulir interaktif dengan JavaScript untuk input valid, kosong dan tidak valid, aksi dan reset. Sertakan lima hasil uji dan jelaskan kode.

**Keluaran:** HTML/JS, tabel lima uji dan penjelasan individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | input valid menghasilkan keluaran benar. | Isi jumlah peserta dengan nilai valid, contoh 3; aktifkan tombol. | Keluaran sesuai ketentuan contoh. | Diisi penilai. |
| 2 | input kosong ditolak. | Kosongkan input lalu aktifkan tombol. | Input kosong ditolak dengan umpan balik. | Diisi penilai. |
| 3 | input tidak valid ditolak. | Masukkan nilai invalid, contoh 0 atau 11; aktifkan tombol. | Nilai invalid ditolak. | Diisi penilai. |
| 4 | event tombol memperbarui DOM. | Ubah input lalu aktifkan event tombol. | Elemen hasil DOM diperbarui sesuai aksi. | Diisi penilai. |
| 5 | reset memulihkan kondisi awal. | Setelah input dan hasil terisi, aktifkan reset. | Input dan keluaran kembali ke kondisi awal. | Diisi penilai. |

### UAS, pekan 16 — 04.4 / 30% · Bloom C6

**Instruksi mahasiswa:** Bangun halaman responsif interaktif dari kasus yang disepakati; serahkan proyek lokal, petunjuk, hasil uji/perbaikan dan demonstrasi individu.

**Keluaran:** Halaman berjalan lokal, dokumentasi dan demonstrasi individu.

| No. | Kriteria | Kondisi, input dan langkah uji contoh | Hasil diharapkan | Hasil aktual / bukti |
|---:|---|---|---|---|
| 1 | HTML/CSS/JS terintegrasi. | Buka proyek pada browser dan telusuri berkasnya. | HTML, CSS dan JS terhubung dan berjalan. | Diisi penilai. |
| 2 | navigasi berfungsi. | Aktifkan navigasi pada halaman. | Tautan utama mencapai tujuan. | Diisi penilai. |
| 3 | interaksi berfungsi. | Gunakan interaksi yang disepakati. | Aksi menghasilkan respons sesuai kasus. | Diisi penilai. |
| 4 | dua lebar dan keyboard diuji. | Uji dua lebar yang disepakati dan gunakan keyboard. | Kedua lebar dan interaksi keyboard diuji serta hasil dicatat. | Diisi penilai. |
| 5 | hasil uji, perbaikan dan langkah menjalankan dicatat. | Periksa dokumentasi proyek. | Langkah lokal, hasil uji dan perbaikan tersedia. | Diisi penilai. |

## Bukti, skor dan umpan balik

Catat untuk setiap butir kondisi, input, langkah, hasil aktual dan bukti; nilai menggunakan [rubrik biner](020_RUBRIK_PENILAIAN_KOM-312_07112026_1332.md). Sediakan akses dan alat yang setara; jangan unggah rahasia. Skor instrumen = jumlah lima skor butir / 5. Nilai MK = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Target usulan CPMK adalah ≥4 cek terpenuhi dari 5; bukan standar kelulusan resmi. Rekap capaian individu, umpan balik dan hambatan untuk CQI tanpa mengklaim hasil sebelum pengukuran.

**Sebelum digunakan [K]:** verifikasi kesesuaian soal dengan CPMK dan jumlah cek, coba simulasi waktu dan fasilitas, tentukan alternatif akses, sahkan jadwal dan rubrik serta kebijakan remedial. Lima cek dan masing-masing 20% dari skor instrumen tetap sama dengan 010.
