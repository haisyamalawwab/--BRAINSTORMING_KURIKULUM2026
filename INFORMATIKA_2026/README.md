# Ekstraksi KPT Teknik Informatika UWG 2026

Berkas `001`–`004` diekstrak dari [Buku KPT OBE Teknik Informatika UWG 2026 (11 September 2026)](https://github.com/rozanhaisyam/--BRAINSTORMING_KURIKULUM2026/blob/91b793377cd4b051f7bdcb89d3c19427ff344f9d/KPT_FIX_3PRODI/KPT%20Program%20Studi/Buku%20KPT%20OBE%20Teknik%20Informatika%20UWG%202026%20%5BUpdate%2011%20September%202026%5D.docx), bukan dari panduan APTIKOM umum atau kurikulum SISTEKIN. Berkas `005`–`007` merupakan kajian pembanding; `008` menyalin Tabel 4 dari panduan APTIKOM Informatika; `009` merangkum inventaris dan analisis tiga MK; `010` adalah rancangan matriks untuk ketiga MK.

| Hasil | Isi |
|---|---|
| [CPL](001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md) | 10 CPL, profil lulusan terkait, dan matriks CPL–BK sumber. |
| [CPMK dan Sub-CPMK](002_CPMK_TEKNIK_INFORMATIKA_07112026_0859.md) | Kodifikasi, prinsip, dan contoh asesmen; batas ketersediaan rumusan per MK. |
| [BoK dan bahan kajian](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md) | 10 BK, ruang lingkup, matriks CPL–BK dan contoh MK pengampu. |
| [Pemetaan MK–CPL–BK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md) | Tabel 18 per semester serta 83 baris unik Tabel 15. |
| [005 — pemetaan APTIKOM](005_PEMETAAN_APTIKOM_MK_INFORMATIKA_07112026_0910.md) | Kandidat 22 BK APTIKOM untuk 83 MK berdasarkan judul; bukan validasi isi. |
| [006 — analisis dan survei pustaka](006_ANALISIS_DAN_SURVEI_PUSTAKA_INFORMATIKA_07112026_0910.md) | Analisis hubungan tabel, perbedaan rujukan dan tindak lanjut. |
| [007 — instrumen survei](007_INSTRUMEN_SURVEI_VALIDASI_INFORMATIKA_07112026_0910.md) | Rancangan survei dan validasi; belum ada respons. |
| [008 — Tabel 4 BK APTIKOM Informatika](008_TABEL_4_RUMUSAN_BAHAN_KAJIAN_APTIKOM_INFORMATIKA_07112026_0942.md) | Transkripsi 22 BK beserta bobot dan referensi. |
| [009 — inventaris dan analisis tiga MK](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) | Daftar MK serta CPL, CPMK, BK dan catatan Tabel 19 untuk KOM-312, KOM-526 dan KFC-506. |
| [010 — rancangan matriks tiga MK](010_MATRIKS_CPL_CPMK_BOK_TIGA_MK_INFORMATIKA_07112026_1303.md) | Usulan CPMK/Sub-CPMK, rencana 16 pertemuan, asesmen dan guardrails; belum disahkan. |
| [011 — indeks perangkat ajar Informatika](011_INDEKS_PERANGKAT_AJAR_INFORMATIKA_07112026_1328.md) | Paket rancangan RPS, SAP, outline modul, asesmen dan rubrik untuk tiga MK, termasuk empat jalur KOM-526 dan dua jalur teknis KFC-506 (Dart + Flutter; React Native + Expo). |

## Identitas dan keterlacakan sumber

- Berkas: `KPT_FIX_3PRODI/KPT Program Studi/Buku KPT OBE Teknik Informatika UWG 2026 [Update 11 September 2026].docx`.
- Commit sumber: `91b793377cd4b051f7bdcb89d3c19427ff344f9d` pada `main` saat pengambilan. Tautan di atas dipatok ke commit ini; file sumber tidak disalin ke folder hasil.
- SHA-256 DOCX: `a54a570150d0f7d38d633e72104b326062981818599101017dd3a7b4dfb2601d`.
- Ekstraksi dilakukan dari teks dan tabel tubuh DOCX menggunakan `python-docx`; spasi dan pemisah baris dalam sel dirapikan, kode dan isi dipertahankan. Nomor tabel/bab lebih stabil daripada nomor halaman DOCX yang dapat berubah saat dirender. Gambar tidak di-OCR; isi visual dan workbook/RPS eksternal tidak diperiksa.

## Temuan dan batasan

1. Bab V Tabel 11 dan Lampiran A Tabel 35 sama-sama memuat 10 rumusan CPL; teksnya sesuai setelah perapian spasi.
2. Bab VI Tabel 13 memuat 10 kelompok BK. Tabel 14 memetakan CPL–BK; Tabel 15 memuat tiga salinan identik dari 83 baris MK, ditampilkan satu kali dalam hasil. Dokumen sendiri menyatakan pemetaan rinci BK–MK masih perlu validasi kelompok bidang keahlian.
3. Bab IX memberi prinsip pemetaan CPMK, tetapi tidak ditemukan rumusan per MK dalam teks dan tabel utama. Tabel 29 Bab XI hanya memuat **contoh** label dan bobot; tidak digunakan untuk menciptakan CPMK per MK.
4. Ekstraksi awal `python-docx` tidak menampilkan tanda relasi Tabel 12/19; jangan menyimpulkan bahwa sel sumber kosong. Pemeriksaan XML Tabel 19 menemukan tanda CPL04 pada tiga MK yang diperiksa dalam content control. Audit penuh Tabel 12/19 belum dilakukan; rincian di [009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md).
5. Hasil ini merupakan transkripsi rujukan dan **tidak membuktikan validasi atau pengesahan akademik**. Dokumen sumber menyebut 146 SKS dalam Bab VII; angka tersebut untuk Teknik Informatika dan tidak otomatis menggantikan statistik prodi lain.

## Penamaan

Berkas hasil ekstraksi menggunakan format `00x_NAMA_DDMMYYYY_HHMM.md`. Nomor, tanggal, dan waktu pada nama ditetapkan untuk versi hasil ini agar regenerasi tidak membuat duplikat; `README.md` tetap sebagai indeks folder.

## Reproduksi

Unduh DOCX pada tautan sumber, lalu (setelah memasang `python-docx`):

```bash
python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/to/sumber.docx
python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/to/sumber.docx --check
```

Skrip menolak sumber dengan SHA-256 berbeda agar perubahan versi tidak secara diam-diam mengganti hasil. Pemeriksaan ini tidak menggantikan pembandingan visual terhadap DOCX.
