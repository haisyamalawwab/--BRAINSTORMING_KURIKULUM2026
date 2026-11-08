# 092_4 — RENCANA EVALUASI DAN ASESMEN

## STA-703 — Pengawasan Cerdas dan Analitika IoT

**Identitas:** `STA-703` Pengawasan Cerdas dan Analitika IoT · Semester 7 · 3 SKS (+P) · Prasyarat `STI-624`, `STI-521` · PL PL-1, PL-2 · PEO PEO-1, PEO-3 · IRM M.

## Empat titik evaluasi

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Anotasi citra berizin dan latih/evaluasi deteksi objek pada split terpisah. Bukti: dataset sintetis/berizin, model dan metrik mAP |
| UTS | 8 | 25% | CPMK-2 | Terapkan pelacakan multiobjek pada video uji dan evaluasi frame rate. Bukti: kode tracking, video contoh dan hasil uji |
| Tugas 2 | 12 | 25% | CPMK-3 | Konversi model untuk edge, ukur latensi dan jelaskan batas perangkat. Bukti: artefak model, konfigurasi dan benchmark |
| UAS | 16 | 30% | CPMK-4 | Integrasikan deteksi, alarm MQTT dan dashboard; uji privasi dan keandalan. Bukti: kode, diagram, hasil uji dan demo |

## Pemetaan CPMK

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-09` (`KK1`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-09` (`KK1`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-07` (`P3`), `CPL-11` (`KK3`) | — | — | 25% | — | 25% |
| CPMK-4 | `CPL-07` (`P3`), `CPL-09` (`KK1`), `CPL-11` (`KK3`) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Skor instrumen = jumlah skor kriteria × bobot rubrik. Nilai akhir = jumlah bobot instrumen × skor instrumen / 100. Skor CPMK = jumlah bobot instrumen terkait × skor instrumen / jumlah bobot instrumen terkait. Skor CPL prodi menggunakan agregasi lintas MK sesuai Dok 008, bukan penjumlahan CPL pada tabel ini.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana tugas dan kisi-kisi

### Tugas 1 — pekan 4, 20%

**CPMK-1 / `CPL-09` (`KK1`).** Anotasi citra berizin dan latih/evaluasi deteksi objek pada split terpisah. **Bukti:** dataset sintetis/berizin, model dan metrik mAP.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UTS — pekan 8, 25%

**CPMK-2 / `CPL-09` (`KK1`).** Terapkan pelacakan multiobjek pada video uji dan evaluasi frame rate. **Bukti:** kode tracking, video contoh dan hasil uji.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Ujian individual dengan klarifikasi lisan. Rubrik ada pada dokumen 5.

### Tugas 2 — pekan 12, 25%

**CPMK-3 / `CPL-07` (`P3`), `CPL-11` (`KK3`).** Konversi model untuk edge, ukur latensi dan jelaskan batas perangkat. **Bukti:** artefak model, konfigurasi dan benchmark.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UAS — pekan 16, 30%

**CPMK-4 / `CPL-07` (`P3`), `CPL-09` (`KK1`), `CPL-11` (`KK3`).** Integrasikan deteksi, alarm MQTT dan dashboard; uji privasi dan keandalan. **Bukti:** kode, diagram, hasil uji dan demo.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

## Umpan balik dan PPEPP

Dosen mencatat skor tiap CPMK dan umpan balik, memberikan remediasi sesuai peraturan institusi, merekap ketercapaian dan menindaklanjuti penyebab capaian rendah melalui siklus PPEPP. Jadwal dan nilai resmi ditetapkan pengampu.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS16` *Artificial Intelligence*, `BK-IT14` *IoT & Smart Systems*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Video Analytics Real-Time, Deteksi Objek Edge (YOLO/MobileNet pada Jetson/Raspberry Pi), Multi-Camera Tracking, Analitik Aliran Sensor IoT Cerdas, Smart City Surveillance Privacy.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang pengkabelan mikrokontroler sensor dasar dari nol, perancangan dashboard BI finansial, training arsitektur transformer teks.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan sistem pengawasan cerdas terintegrasi AI edge dan jaringan IoT otonom.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Biometrik hanya pada data sintetis atau data yang memiliki persetujuan eksplisit; mAP/FPS adalah target Dok 043, bukan hasil yang dijamin. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
