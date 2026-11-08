# 099_4 — RENCANA EVALUASI DAN ASESMEN

## STC-702 — Arsitektur SaaS & Multi-Tenansi

**Identitas:** `STC-702` Arsitektur SaaS & Multi-Tenansi · Semester 7 · 3 SKS (+P) · Prasyarat `STI-416` · PL PL-3 · PEO PEO-1, PEO-2 · IRM M.

## Empat titik evaluasi

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Rancang isolasi tenant dan uji akses lintas tenant pada data dummy. Bukti: skema, kebijakan RLS dan hasil negative test |
| UTS | 8 | 25% | CPMK-2 | Bangun langganan dengan Stripe test mode dan penanganan webhook. Bukti: kode, event sandbox dan bukti transaksi |
| Tugas 2 | 12 | 25% | CPMK-3 | Implementasikan feature flag per plan dan micro-frontends. Bukti: kode, konfigurasi dan hasil uji akses |
| UAS | 16 | 30% | CPMK-3 | Integrasikan SaaS dan lakukan uji isolasi, akses plan, billing dan pemulihan. Bukti: repo, demo, hasil uji keamanan dan dokumentasi |

## Pemetaan CPMK

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | — | 25% | 30% | 55% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Skor instrumen = jumlah skor kriteria × bobot rubrik. Nilai akhir = jumlah bobot instrumen × skor instrumen / 100. Skor CPMK = jumlah bobot instrumen terkait × skor instrumen / jumlah bobot instrumen terkait. Skor CPL prodi menggunakan agregasi lintas MK sesuai Dok 008, bukan penjumlahan CPL pada tabel ini.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana tugas dan kisi-kisi

### Tugas 1 — pekan 4, 20%

**CPMK-1 / `CPL-08` (`P4`).** Rancang isolasi tenant dan uji akses lintas tenant pada data dummy. **Bukti:** skema, kebijakan RLS dan hasil negative test.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UTS — pekan 8, 25%

**CPMK-2 / `CPL-13` (`KK5`).** Bangun langganan dengan Stripe test mode dan penanganan webhook. **Bukti:** kode, event sandbox dan bukti transaksi.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Ujian individual dengan klarifikasi lisan. Rubrik ada pada dokumen 5.

### Tugas 2 — pekan 12, 25%

**CPMK-3 / `CPL-08` (`P4`), `CPL-13` (`KK5`).** Implementasikan feature flag per plan dan micro-frontends. **Bukti:** kode, konfigurasi dan hasil uji akses.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UAS — pekan 16, 30%

**CPMK-3 / `CPL-08` (`P4`), `CPL-13` (`KK5`).** Integrasikan SaaS dan lakukan uji isolasi, akses plan, billing dan pemulihan. **Bukti:** repo, demo, hasil uji keamanan dan dokumentasi.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

## Umpan balik dan PPEPP

Dosen mencatat skor tiap CPMK dan umpan balik, memberikan remediasi sesuai peraturan institusi, merekap ketercapaian dan menindaklanjuti penyebab capaian rendah melalui siklus PPEPP. Jadwal dan nilai resmi ditetapkan pengampu.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS12` *Web & Mobile*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Software-as-a-Service (SaaS), Pola Multi-Tenancy (Database per Tenant, Shared Database Shared Schema), Tenant Isolation, Sistem Penagihan Berlangganan (Stripe API), Skalabilitas Horisontal Layanan SaaS.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding driver perangkat keras, audit pajak korporat, perancangan sensor IoT fisik.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan platform SaaS multi-penyewa yang siap dipasarkan secara komersial dan skalabel.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Gunakan akun pembayaran sandbox, dan uji negatif antar-tenant; hasil uji tidak membuktikan isolasi mutlak. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
