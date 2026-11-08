# Ekstraksi KPT Teknik Informatika UWG 2026

Ekstraksi dari [Buku KPT OBE Teknik Informatika UWG 2026 (11 September 2026)](https://github.com/rozanhaisyam/--BRAINSTORMING_KURIKULUM2026/blob/91b793377cd4b051f7bdcb89d3c19427ff344f9d/KPT_FIX_3PRODI/KPT%20Program%20Studi/Buku%20KPT%20OBE%20Teknik%20Informatika%20UWG%202026%20%5BUpdate%2011%20September%202026%5D.docx), bukan panduan Informatika APTIKOM umum dan bukan kurikulum SISTEKIN.

| Hasil | Isi |
|---|---|
| [CPL](CPL.md) | 10 CPL, profil lulusan terkait, dan matriks CPL–BK sumber. |
| [CPMK dan Sub-CPMK](CPMK.md) | Kodifikasi, prinsip, dan contoh asesmen; batas ketersediaan rumusan per MK. |
| [BoK dan bahan kajian](BOK_DAN_BAHAN_KAJIAN.md) | 10 BK, ruang lingkup, matriks CPL–BK dan contoh MK pengampu. |
| [Pemetaan MK–CPL–BK](PEMETAAN_MK_CPL_BK.md) | Tabel 18 per semester serta 83 baris unik Tabel 15. |

## Identitas dan keterlacakan sumber

- Berkas: `KPT_FIX_3PRODI/KPT Program Studi/Buku KPT OBE Teknik Informatika UWG 2026 [Update 11 September 2026].docx`.
- Commit sumber: `91b793377cd4b051f7bdcb89d3c19427ff344f9d` pada `main` saat pengambilan. Tautan di atas dipatok ke commit ini; file sumber tidak disalin ke folder hasil.
- SHA-256 DOCX: `a54a570150d0f7d38d633e72104b326062981818599101017dd3a7b4dfb2601d`.
- Ekstraksi dilakukan dari teks dan tabel tubuh DOCX menggunakan `python-docx`; spasi dan pemisah baris dalam sel dirapikan, kode dan isi dipertahankan. Nomor tabel/bab lebih stabil daripada nomor halaman DOCX yang dapat berubah saat dirender. Gambar tidak di-OCR; isi visual dan workbook/RPS eksternal tidak diperiksa.

## Temuan dan batasan

1. Bab V Tabel 11 dan Lampiran A Tabel 35 sama-sama memuat 10 rumusan CPL; teksnya sesuai setelah perapian spasi.
2. Bab VI Tabel 13 memuat 10 kelompok BK. Tabel 14 memetakan CPL–BK; Tabel 15 memuat tiga salinan identik dari 83 baris MK, ditampilkan satu kali dalam hasil. Dokumen sendiri menyatakan pemetaan rinci BK–MK masih perlu validasi kelompok bidang keahlian.
3. Bab IX memberi prinsip pemetaan CPMK, tetapi tidak ditemukan rumusan per MK dalam teks dan tabel utama. Tabel 29 Bab XI hanya memuat **contoh** label dan bobot; tidak digunakan untuk menciptakan CPMK per MK.
4. Sel relasi pada Tabel 12 (CPL–PL) dan Tabel 19 (CPL–MK) kosong dalam teks DOCX. Tabel 11 dan Tabel 18 diekstrak apa adanya sebagai sumber relasi yang eksplisit; ketidaksesuaian antartabel belum direkonsiliasi.
5. Hasil ini merupakan transkripsi rujukan dan **tidak membuktikan validasi atau pengesahan akademik**. Dokumen sumber menyebut 146 SKS dalam Bab VII; angka tersebut untuk Teknik Informatika dan tidak otomatis menggantikan statistik prodi lain.

## Reproduksi

Unduh DOCX pada tautan sumber, lalu (setelah memasang `python-docx`):

```bash
python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/to/sumber.docx
python3 -B INFORMATIKA_2026/ekstraksi_kpt.py /path/to/sumber.docx --check
```

Skrip menolak sumber dengan SHA-256 berbeda agar perubahan versi tidak secara diam-diam mengganti hasil. Pemeriksaan ini tidak menggantikan pembandingan visual terhadap DOCX.
