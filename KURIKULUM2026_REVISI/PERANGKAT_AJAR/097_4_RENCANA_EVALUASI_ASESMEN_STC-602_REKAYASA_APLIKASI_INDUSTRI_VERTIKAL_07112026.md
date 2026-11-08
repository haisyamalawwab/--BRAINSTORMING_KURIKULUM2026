# 097_4 — RENCANA EVALUASI DAN ASESMEN

## STC-602 — Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech)

**Identitas:** `STC-602` Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) · Semester 7 · 3 SKS (+P) · Prasyarat `STI-416` · PL PL-3 · PEO PEO-1, PEO-2 · IRM M.

## Empat titik evaluasi

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Rancang alur payment gateway sandbox dengan pengamanan transaksi. Bukti: diagram transaksi, request dan threat notes |
| UTS | 8 | 25% | CPMK-1 | Implementasikan payment sandbox dan double-entry ledger serta uji idempotensi. Bukti: kode individual, log transaksi dan hasil uji |
| Tugas 2 | 12 | 25% | CPMK-2 | Implementasikan SCORM/xAPI pada lingkungan LMS contoh. Bukti: paket pembelajaran, statement xAPI dan log uji |
| UAS | 16 | 30% | CPMK-3 | Bangun solusi vertikal dengan transaksi idempotent dan evaluasi keamanan. Bukti: repo, demo, hasil uji dan batas kepatuhan |

## Pemetaan CPMK

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-08` (`P4`), `CPL-13` (`KK5`) | 20% | 25% | — | — | 45% |
| CPMK-2 | `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | — | 25% | — | 25% |
| CPMK-3 | `CPL-13` (`KK5`) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Skor instrumen = jumlah skor kriteria × bobot rubrik. Nilai akhir = jumlah bobot instrumen × skor instrumen / 100. Skor CPMK = jumlah bobot instrumen terkait × skor instrumen / jumlah bobot instrumen terkait. Skor CPL prodi menggunakan agregasi lintas MK sesuai Dok 008, bukan penjumlahan CPL pada tabel ini.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana tugas dan kisi-kisi

### Tugas 1 — pekan 4, 20%

**CPMK-1 / `CPL-08` (`P4`), `CPL-13` (`KK5`).** Rancang alur payment gateway sandbox dengan pengamanan transaksi. **Bukti:** diagram transaksi, request dan threat notes.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UTS — pekan 8, 25%

**CPMK-1 / `CPL-08` (`P4`), `CPL-13` (`KK5`).** Implementasikan payment sandbox dan double-entry ledger serta uji idempotensi. **Bukti:** kode individual, log transaksi dan hasil uji.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Ujian individual dengan klarifikasi lisan. Rubrik ada pada dokumen 5.

### Tugas 2 — pekan 12, 25%

**CPMK-2 / `CPL-08` (`P4`), `CPL-13` (`KK5`).** Implementasikan SCORM/xAPI pada lingkungan LMS contoh. **Bukti:** paket pembelajaran, statement xAPI dan log uji.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UAS — pekan 16, 30%

**CPMK-3 / `CPL-13` (`KK5`).** Bangun solusi vertikal dengan transaksi idempotent dan evaluasi keamanan. **Bukti:** repo, demo, hasil uji dan batas kepatuhan.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

## Umpan balik dan PPEPP

Dosen mencatat skor tiap CPMK dan umpan balik, memberikan remediasi sesuai peraturan institusi, merekap ketercapaian dan menindaklanjuti penyebab capaian rendah melalui siklus PPEPP. Jadwal dan nilai resmi ditetapkan pengampu.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS12` *Web & Mobile*, `BK-IT04` *Platform Technologies*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Sistem Industri Vertikal, Layanan FinTech (Sistem Pembayaran, Payment Gateway, Fraud Detection Dasar, Regulasi BI/OJK), Layanan EdTech (LMS, Learning Analytics), Keamanan Transaksi Finansial.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang audit kepatuhan perbankan legal murni, pembuatan game edukasi 3D mendalam, setup hardware server fisik data center.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun sistem aplikasi industri bernilai ekonomi tinggi yang patuh pada standar regulasi sektoral.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
