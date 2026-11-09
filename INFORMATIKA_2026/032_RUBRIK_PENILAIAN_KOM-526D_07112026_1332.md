# 032 — Rubrik penilaian pembelajaran

## KOM-526d — Sistem Aplikasi Web Python Flask

> **Status [U]: draf, belum disahkan.** Data MK, CPL dan BK bersumber dari buku KPT Teknik Informatika UWG; isi, asesmen dan contoh bersifat usulan pada [010](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) dan [paket RPS/SAP](016_PAKET_RPS_SAP_ASESMEN_KOM-526D_SISTEM_APLIKASI_WEB_PYTHON_FLASK_07112026_1328.md). Label KOM-526a–d (jika digunakan) adalah usulan jalur, bukan kode MK/KRS resmi. Gunakan struktur perangkat SISTEKIN hanya sebagai contoh, bukan sumber kebijakan Informatika. Prasyarat resmi, T/P, PT/BM dan pengesahan belum terverifikasi.


## Penggunaan rubrik [U]

Gunakan lima cek untuk setiap instrumen; masing-masing **20% dari skor instrumen**. Skor cek **100** jika semua unsur cek dan hasil yang diharapkan terpenuhi serta dapat diverifikasi; **0** jika satu unsur gagal atau bukti tidak ada/tidak dapat diverifikasi. Butir gabungan mensyaratkan semua unsur. Kondisi contoh pada [rencana evaluasi](031_RENCANA_EVALUASI_ASESMEN_KOM-526D_07112026_1332.md) adalah usulan operasional yang harus disepakati sebelum penilaian.

Untuk UTS/T2/UAS, cek terkait dibuktikan menggunakan route/view Flask dan sqlite3; pemeriksaan peran pada aplikasi Flask. T1 menilai rancangan, bukan kode; kondisi ini bukan cek berbobot tambahan.

### Tugas 1, pekan 4 — 04.1 / 20% · Bloom C6

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. aktor dan peran teridentifikasi. | 20% | Admin dan petugas beserta peran teridentifikasi. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. minimal tiga kebutuhan dapat diuji. | 20% | Sekurang-kurangnya tiga kebutuhan dapat diuji. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. alur utama tergambar. | 20% | Alur utama tergambar dan dapat dijelaskan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. minimal dua entitas dan relasinya terdefinisi. | 20% | Kategori dan barang (atau dua entitas setara) serta relasinya terdefinisi. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. kebutuhan terhubung ke data/alur. | 20% | Keterkaitan kebutuhan dengan data/alur tampak. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

### UTS, pekan 8 — 04.2 / 25% · Bloom C3

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. create. | 20% | Barang dibuat melalui alur server dan database. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. read. | 20% | Barang terambil dan ditampilkan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. update. | 20% | Stok baru tersimpan dan terbaca. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. delete. | 20% | Barang terhapus dan tidak lagi tersedia. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. permintaan untuk data yang tidak ditemukan ditangani. | 20% | Respons atau pesan tidak ditemukan ditangani. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

### Tugas 2, pekan 12 — 04.3 / 25% · Bloom C4

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. login valid. | 20% | Akses terlindungi sesuai peran admin diperoleh. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. login tidak valid ditolak. | 20% | Login ditolak. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. akses peran tidak berwenang ditolak. | 20% | Server menolak perubahan oleh peran tidak berwenang. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. logout mengakhiri akses sesi. | 20% | Browser yang diuji tidak lagi memperoleh akses terlindungi. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. masukan invalid ditolak server dan data diproses dengan kueri terparameter. | 20% | Masukan invalid ditolak server dan nilai query diparameterisasi. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

### UAS, pekan 16 — 04.4 / 30% · Bloom C6

| No. / kriteria | Bobot instrumen | Terpenuhi — skor 100 | Belum terpenuhi — skor 0 | Bukti/umpan balik |
|---|---:|---|---|---|
| 1. alur sesuai rancangan terintegrasi. | 20% | Alur terintegrasi sesuai rancangan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 2. data tersimpan dan terbaca. | 20% | Data tersimpan dan dapat dibaca. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 3. pembatasan akses bekerja. | 20% | Pembatasan akses sesuai peran bekerja. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 4. alur salah ditangani dan dicatat. | 20% | Kegagalan ditangani dan dicatat. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |
| 5. petunjuk lokal, hasil uji dan perbaikan tersedia. | 20% | Ketiganya tersedia dan dapat dijelaskan. | Hasil tersebut gagal/tidak lengkap atau tidak terbukti. | Hasil aktual dan umpan balik diisi penilai. |

## Pemetaan level Bloom [U]

Level tiap instrumen mengikuti CPMK yang dinilai: lihat tabel peta evaluasi pada paket [016](016_PAKET_RPS_SAP_ASESMEN_KOM-526D_SISTEM_APLIKASI_WEB_PYTHON_FLASK_07112026_1328.md). Rubrik ini **tidak menambah bobot atau butir**: level menjelaskan kognisi yang dibuktikan, sedangkan penilaian tetap biner 100/0 pada lima cek (20% per cek) dengan target usulan ≥4/5. Rujukan kerangka dan kata kerja ada pada [010 bagian 15](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md#15-taksonomi-bloom-c2c6-dan-rumusan-abcd-pada-rps-u).

## Formatif, rekap dan CQI

Formatif: catat **terpenuhi / perlu perbaikan / belum ditunjukkan**, beri umpan balik; tidak menambah bobot nilai akhir. Skor instrumen = jumlah lima skor cek / 5; target usulan CPMK ≥4 cek terpenuhi. Contoh empat cek terpenuhi dan satu gagal → `(100+100+100+100+0)/5 = 80`. Bobot MK tetap T1 20%, UTS 25%, T2 25%, UAS 30%; bobot cek tidak dikalikan dua kali.

| Identitas mahasiswa | T1: lulus cek / skor | UTS: lulus cek / skor | T2: lulus cek / skor | UAS: lulus cek / skor | Nilai akhir | Umpan balik / perbaikan |
|---|---|---|---|---|---|---|
| Diisi dosen | — | — | — | — | — | — |

Nilai akhir = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`. Kode CPMK lokal per MK; jangan menghitung bobot asesmen sebagai capaian CPL otomatis. Simpan bukti individu dan ringkas pola kesulitan untuk CQI; remedial dan pelaporan menunggu keputusan prodi. Jika ingin skala bertingkat seperti contoh SISTEKIN, rumuskan ulang rubrik, bobot dan ambang serta dapatkan persetujuan terlebih dahulu; jangan mencampur skala itu dengan checklist biner ini.
