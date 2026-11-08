# Generator RPS berbasis template (Markdown dan DOCX)

`generate_rps_md.py` membuat **Markdown** dengan urutan isi dan tabel delapan kolom dari `Template_RPS_GEN_2026_20092026-SWO.docx`: sampul; identitas dan otorisasi; CPL, CPMK, Sub-CPMK dan korelasi; deskripsi, bahan kajian dan pustaka; 16 pertemuan; pemetaan asesmen; empat soal dan rubrik; serta validasi. Markdown tidak mempertahankan logo, orientasi atau tata letak cetak. `generate_rps_docx.py` mengisi template DOCX SWO asli menggunakan data JSON yang sama dan mempertahankan dua orientasi halaman; generator tidak membuat PDF. Karena panjang isi setiap MK berbeda, periksa ulang tata letak, pemenggalan tabel dan jumlah halaman di Word sebelum diedarkan. Format rubrik diambil dari data MK; contoh STI-311 memakai **empat tingkat** sesuai `065_5`, bukan menambahkan tingkat kelima tanpa persetujuan.

## STI-311

- [RPS DOCX hasil pengisian template](../DOCX/RPS_STI-311_TEMPLATE_REVISI_07112026.docx) — rancangan; validasi visual dan akademik diperlukan.
- Data terkurasi: [`PERANGKAT_AJAR/_data/065_STI-311_RPS.json`](../PERANGKAT_AJAR/_data/065_STI-311_RPS.json).
- Hasil: [`065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md`](../PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md).
- Sumber substansi: 065_1–065_5 **di direktori utama** `PERANGKAT_AJAR`, terutama SAP (`065_2`), outline modul (`065_3`), soal (`065_4`) dan rubrik (`065_5`), bersama Dok 003/005 dan turunan 043. Salinan `WEB FRONT END/065_*` dan pilot lama berisi cakupan berbeda dan tidak dijadikan sumber.
- Rencana daring, pengelompokan pustaka utama/pendukung dan pemilihan nomor pustaka mingguan merupakan **usulan untuk melengkapi template**, bukan keputusan institusi. Daring adalah alternatif, bukan beban tambahan. Personel dan tanggal yang belum diketahui dibiarkan belum ditetapkan.
- Bila ada perubahan akademik, rekonsiliasi juga `065_2`–`065_5`, ubah JSON, hasilkan ulang RPS, dan minta peninjauan RMK/prodi. Skrip **tidak membaca atau menyinkronkan otomatis** dokumen-dokumen sumber itu.

## Cara menjalankan

Dari root repositori, gunakan Python 3 tanpa paket eksternal:

```bash
# Validasi data dan pastikan RPS yang tersimpan identik dengan hasil generator.
python3 -B KURIKULUM2026_REVISI/_tools/generate_rps_md.py \
  KURIKULUM2026_REVISI/PERANGKAT_AJAR/_data/065_STI-311_RPS.json \
  --check -o KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md

# Untuk pembangkitan pertama ke berkas BARU:
python3 -B KURIKULUM2026_REVISI/_tools/generate_rps_md.py \
  KURIKULUM2026_REVISI/PERANGKAT_AJAR/_data/065_STI-311_RPS.json \
  -o KURIKULUM2026_REVISI/PERANGKAT_AJAR/nama-keluaran-baru.md

# Jika sengaja memperbarui RPS yang sudah ada, tambahkan --force
# setelah memeriksa perubahan JSON dan meninjau dampaknya.
python3 -B KURIKULUM2026_REVISI/_tools/generate_rps_md.py \
  KURIKULUM2026_REVISI/PERANGKAT_AJAR/_data/065_STI-311_RPS.json \
  -o KURIKULUM2026_REVISI/PERANGKAT_AJAR/065_1_RPS_STI-311_PENGEMBANGAN_WEB_FRONT_END_07112026.md --force

python3 -B KURIKULUM2026_REVISI/_tools/generate_rps_md.py --help
python3 -B KURIKULUM2026_REVISI/_tools/test_generate_rps_md.py -v
python3 -B KURIKULUM2026_REVISI/_tools/verify_sti311_alignment.py
```

Secara default generator Markdown menolak menimpa berkas, membutuhkan `-o`, dan hanya menerima keluaran `.md`. `--check` tanpa `-o` hanya memeriksa data; dengan `-o` juga membandingkan isi berkas tanpa menulis. `--force` hanya untuk menimpa secara sengaja. Buat cadangan/review diff saat mengubah dokumen yang telah ada.

## Pengisian template DOCX

Pasang dependensi `python-docx` (misalnya dalam virtual environment), lalu gunakan JSON yang sama:

```bash
python3 -m pip install -r KURIKULUM2026_REVISI/_tools/requirements-rps-docx.txt
python3 -B KURIKULUM2026_REVISI/_tools/generate_rps_docx.py \
  KURIKULUM2026_REVISI/PERANGKAT_AJAR/_data/065_STI-311_RPS.json \
  -o KURIKULUM2026_REVISI/DOCX/RPS_STI-311_TEMPLATE_REVISI_07112026.docx --force
python3 -B KURIKULUM2026_REVISI/_tools/test_generate_rps_docx.py -v
```

Hapus `--force` saat membuat berkas baru; secara default generator menolak menimpa. Generator juga menolak output yang sama dengan input atau template, serta memeriksa placeholder. Opsi `--template` tersedia untuk template lain **dengan struktur SWO yang sama**; bukan importer untuk template Word sembarang. Bentuk data, asesmen, minggu dan validasi sama dengan generator Markdown. Uji mengonfirmasi elemen dan teks, bukan kerapian saat dirender atau pengesahan akademik.

## MK lain: kontrak data JSON

Salin data contoh ke file JSON **baru**, kurasi seluruh isinya dari kurikulum dan paket MK tujuan, lalu berikan jalur JSON dan output ke perintah di atas. Mengganti nama/kode saja tidak cukup: semua CPMK, sub-CPMK, minggu, soal, rubrik, bobot, pustaka dan catatan evaluasi juga harus diganti. Periksa kembali otoritas, beban, sumber dan statusnya. Generator bukan parser otomatis paket Markdown, tidak membuat konten akademik dan tidak menetapkan kebijakan penilaian.

Semua properti berikut wajib; teks yang belum diketahui isi `"Belum ditetapkan"`, bukan identitas fiktif. Contoh lengkap sintaks ada di JSON STI-311.

| Properti | Isi dan hubungan |
|---|---|
| `judul`, `status`, `sumber`, `konteks`, `deskripsi`, `bahan_kajian`, `lingkup`, `catatan_beban`, `catatan_evaluasi` | Teks sesuai MK; sertakan batas dan status persetujuan. `catatan_evaluasi` juga harus sesuai dengan bobot dan cara pemetaan MK tersebut. |
| `identitas` | Teks: `universitas`, `fakultas`, `prodi`, `no_dokumen`, `mk`, `kode`, `rumpun`, `tanggal_penyusunan`, `penyusun`, `nuptk`, `pengembang`, `koordinator`, `ketua_prodi`, `pengampu`, `prasyarat`, `periode`. Bilangan bulat: `sks_teori`, `sks_praktik`, `semester`. |
| `cpl` | Daftar objek `id`, `display`, `rumusan`, `irm`; `display` dapat memuat kode/alias sebagaimana ingin ditampilkan. |
| `cpmk` | Daftar objek `id`, `rumusan`, `bloom`, `cpl` (daftar ID CPL). |
| `subcpmk` | Daftar objek `id`, `rumusan`, `cpmk` (satu ID induk), `bloom`. |
| `referensi` | Daftar objek `id` (nomor bulat unik), `nama`, `url`, `jenis` (`utama` atau `pendukung`). |
| `minggu` | Tepat 16 objek berurutan: `week` (1–16), `subcpmk` (daftar ID), `indikator`, `kriteria_teknik`, `luring`, `daring`, `materi`, `referensi` (daftar nomor pustaka) dan `asesmen` (daftar ID asesmen atau `[]`). Cantumkan estimasi waktu pada kegiatan. Pekan asesmen harus cocok dengan `asesmen.week`, dan semua CPMK asesmen harus terwakili oleh induk Sub-CPMK pada pekan tersebut. |
| `level_rubrik` | Daftar label tingkat kinerja unik (minimal dua), sesuai sumber MK. |
| `asesmen` | Tepat empat objek ber-ID `tugas1`, `uts`, `tugas2`, `uas` sesuai empat lampiran template; tiap objek memiliki `nama`, `week`, `bobot` (persen bulat), `cpmk` (daftar ID CPMK), `soal`, dan `rubrik`. Bobot instrumen total 100%; UTS minggu 8, UAS minggu 16. Untuk satu instrumen dengan beberapa CPMK, matriks menampilkan tanda korelasi tanpa menduplikasi bobot ke tiap CPMK; tata cara ketercapaian dijelaskan di `catatan_evaluasi`. |
| `asesmen[].rubrik` | Daftar objek `kriteria`, `bobot` (persen bulat), `deskriptor` (daftar teks dengan urutan dan jumlah sama dengan `level_rubrik`). Bobot tiap rubrik total 100%. |
| `validasi` | Teks `tempat_tanggal`, `upm`, `upm_nuptk`, `dosen`, `dosen_nuptk`, `ketua_prodi`, `ketua_prodi_nuptk`; gunakan nilai sebenarnya hanya setelah ditetapkan. |

Generator memeriksa isian wajib, ID unik, rujukan CPL/CPMK/Sub-CPMK/pustaka/asesmen, 16 minggu, bobot total dan rubrik, kesesuaian pekan, serta placeholder template yang umum. Uji juga menggunakan MK fiktif berbeda dengan lima CPMK, pemetaan banyak CPMK, skala dan bobot berbeda. Pemeriksaan struktural ini **bukan** validasi isi, penjaminan keselarasan seluruh referensi, pengesahan akademik, atau pengganti review visual dan akademik.
