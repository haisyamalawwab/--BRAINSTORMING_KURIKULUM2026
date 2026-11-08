# 090_4 — RENCANA EVALUASI DAN ASESMEN

## STA-701 — MLOps dan Alur Pipa AI

**Identitas:** `STA-701` MLOps dan Alur Pipa AI · Semester 7 · 3 SKS (+P) · Prasyarat `STI-413`, `STI-726` · PL PL-1 · PEO PEO-1, PEO-3 · IRM M.

## Empat titik evaluasi

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Versikan data dan lacak eksperimen MLflow; jelaskan sumber data dan model. Bukti: repositori DVC, eksperimen dan model card |
| UTS | 8 | 25% | CPMK-2 | Susun DAG continuous training, validasi data dan uji trigger retraining. Bukti: DAG, bukti eksekusi dan hasil validasi |
| Tugas 2 | 12 | 25% | CPMK-3 | Simulasikan canary/shadow dan deteksi drift dengan data yang terkendali. Bukti: konfigurasi serving, metrik dan hasil uji drift |
| UAS | 16 | 30% | CPMK-3 | Integrasikan registry, serving dan monitoring; jelaskan prosedur rollback. Bukti: pipeline, log, laporan dan demonstrasi |

## Pemetaan CPMK

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-10` (`KK2`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-08` (`P4`), `CPL-09` (`KK1`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-09` (`KK1`) | — | — | 25% | 30% | 55% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Skor instrumen = jumlah skor kriteria × bobot rubrik. Nilai akhir = jumlah bobot instrumen × skor instrumen / 100. Skor CPMK = jumlah bobot instrumen terkait × skor instrumen / jumlah bobot instrumen terkait. Skor CPL prodi menggunakan agregasi lintas MK sesuai Dok 008, bukan penjumlahan CPL pada tabel ini.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana tugas dan kisi-kisi

### Tugas 1 — pekan 4, 20%

**CPMK-1 / `CPL-10` (`KK2`).** Versikan data dan lacak eksperimen MLflow; jelaskan sumber data dan model. **Bukti:** repositori DVC, eksperimen dan model card.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UTS — pekan 8, 25%

**CPMK-2 / `CPL-08` (`P4`), `CPL-09` (`KK1`).** Susun DAG continuous training, validasi data dan uji trigger retraining. **Bukti:** DAG, bukti eksekusi dan hasil validasi.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Ujian individual dengan klarifikasi lisan. Rubrik ada pada dokumen 5.

### Tugas 2 — pekan 12, 25%

**CPMK-3 / `CPL-09` (`KK1`).** Simulasikan canary/shadow dan deteksi drift dengan data yang terkendali. **Bukti:** konfigurasi serving, metrik dan hasil uji drift.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UAS — pekan 16, 30%

**CPMK-3 / `CPL-09` (`KK1`).** Integrasikan registry, serving dan monitoring; jelaskan prosedur rollback. **Bukti:** pipeline, log, laporan dan demonstrasi.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

## Umpan balik dan PPEPP

Dosen mencatat skor tiap CPMK dan umpan balik, memberikan remediasi sesuai peraturan institusi, merekap ketercapaian dan menindaklanjuti penyebab capaian rendah melalui siklus PPEPP. Jadwal dan nilai resmi ditetapkan pengampu.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS18` *Machine Learning*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Lifecycle MLOps, Experiment Tracking (MLflow), Data Versioning (DVC), Containerization Model (Docker), Model Serving (FastAPI/Triton), CI/CD Pipeline for ML, Monitoring Data & Concept Drift.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang merancang arsitektur jaringan saraf tiruan CNN baru dari nol, pengembangan antarmuka grafis UI/UX bisnis.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menjamin model kecerdasan buatan dapat dideploy, dipantau, dan di-retrain secara otomatis di lingkungan produksi.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
