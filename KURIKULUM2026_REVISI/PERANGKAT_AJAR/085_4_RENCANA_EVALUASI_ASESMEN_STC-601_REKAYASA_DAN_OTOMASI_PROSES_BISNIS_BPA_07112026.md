# 085_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STC-601 — Rekayasa & Otomasi Proses Bisnis (BPA) (*Business Process Engineering & Automation (BPA)*)

**Identitas:** `STC-601` Rekayasa & Otomasi Proses Bisnis (BPA) · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-306` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-4 (adaptasi BPA).

## 1. Arsitektur asesmen dan bukti

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Event log, model, perhitungan KPI dan rekomendasi |
| UTS | 8 | 25% | `CPMK-2` | BPMN, DMN, bukti eksekusi dan jawaban individual |
| Tugas 2 | 12 | 25% | `CPMK-3` | Bot, data dummy, hasil OCR dan log pengujian |
| UAS | 16 | 30% | `CPMK-3` | Diagram, workflow, bot, KPI, bukti uji dan demo tim |

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 2. Matriks CPMK dan CPL

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-06` (`P2`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-06` (`P2`), `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-13` (`KK5`) | — | — | 25% | 30% | 55% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UAS sama-sama mengukur CPMK-3.

### Formula dan batas interpretasi

- **Skor instrumen:** jumlah skor kriteria × bobot kriteria dalam rubrik dokumen 5, skala 0–100. **Nilai akhir MK:** 0,20 × T1 + 0,25 × UTS + 0,25 × T2 + 0,30 × UAS.
- **Skor CPMK:** jumlah (bobot instrumen terkait × skor instrumen) dibagi jumlah bobot instrumen CPMK itu; misal skor 80 pada 25% dan 70 pada 30% menghasilkan (25×80 + 30×70)/55 = 74,55.
- **Diagnostik CPL pada mata kuliah:** rata-rata berbobot CPMK yang mendukung CPL, dengan total bobot CPMK sebagai bobot. Ini sarana diagnostik lokal dan bukan pengganti formula agregasi resmi prodi.
- **CPL individu lintas MK menurut Dok 008:** Σ(SKS MK × bobot MK terhadap CPL × nilai akhir MK) / Σ(SKS MK × bobot MK terhadap CPL), pada seluruh MK pembina CPL; bobot ditetapkan prodi. Dok 008 menetapkan ambang 65 serta target 80% kohor mencapai ambang; nilai MK ini saja belum bisa menentukan capaian CPL lulusan.

## 3. Rencana Tugas Mahasiswa dan kisi-kisi ujian

### 3.1 Tugas 1 — Analisis proses dan conformance

- **Waktu dan bobot:** pekan 4, 20% nilai MK; **CPMK:** `CPMK-1`; **CPL:** `CPL-06` (`P2`).
- **Tujuan:** Mahasiswa (*A*) mampu **menganalisis** performa proses bisnis dan mendeteksi kesenjangan (*Conformance Checking*) (*B*) menggunakan teknik Process Mining (*C*) secara empiris (*D*).
- **Kasus & instruksi:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Gunakan log sintetis untuk discovery, pengukuran cycle time dan analisis deviasi terhadap model.
- **Bukti wajib:** Event log, model, perhitungan KPI dan rekomendasi.
- **Indikator penilaian:** Validitas log; ketepatan discovery; analisis deviasi; rekomendasi dan batas data. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.2 UTS — Workflow BPMN dan DMN

- **Waktu dan bobot:** pekan 8, 25% nilai MK; **CPMK:** `CPMK-2`; **CPL:** `CPL-06` (`P2`), `CPL-08` (`P4`), `CPL-13` (`KK5`).
- **Tujuan:** Mahasiswa (*A*) mampu **merancang dan mengeksekusi** alur kerja otomatis (*B*) menggunakan Workflow Engine (Camunda BPMN 8 / Temporal) dan Decision Model and Notation (DMN) (*C*) secara terstandarisasi (*D*).
- **Kasus & instruksi:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Implementasikan workflow dan tabel keputusan dengan service task mock dan jalur exception.
- **Bukti wajib:** BPMN, DMN, bukti eksekusi dan jawaban individual.
- **Indikator penilaian:** Ketepatan model; aturan keputusan; penanganan exception; ketertelusuran uji. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** ujian praktik individual; dosen memberi dataset atau konfigurasi uji dan menilai hasil serta penjelasan. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.3 Tugas 2 — Bot RPA dan OCR

- **Waktu dan bobot:** pekan 12, 25% nilai MK; **CPMK:** `CPMK-3`; **CPL:** `CPL-13` (`KK5`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengembangkan** bot Robotic Process Automation (RPA) (*B*) menggunakan Python RPA / UiPath (*C*) untuk otomasi tugas repetitif dan ekstraksi dokumen OCR (*D*).
- **Kasus & instruksi:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Bangun bot untuk input formulir latihan dan ekstraksi dokumen sintetis dengan fallback manual.
- **Bukti wajib:** Bot, data dummy, hasil OCR dan log pengujian.
- **Indikator penilaian:** Fungsi bot; kualitas ekstraksi; penanganan gagal; keamanan data dan replikasi. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.4 UAS — Solusi BPA end-to-end

- **Waktu dan bobot:** pekan 16, 30% nilai MK; **CPMK:** `CPMK-3`; **CPL:** `CPL-13` (`KK5`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengembangkan** bot Robotic Process Automation (RPA) (*B*) menggunakan Python RPA / UiPath (*C*) untuk otomasi tugas repetitif dan ekstraksi dokumen OCR (*D*).
- **Kasus & instruksi:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Integrasikan workflow BPMN/DMN dengan bot; ukur KPI simulasi dan uji jalur exception.
- **Bukti wajib:** Diagram, workflow, bot, KPI, bukti uji dan demo tim.
- **Indikator penilaian:** Integrasi berfungsi; validitas KPI; keandalan exception; dokumentasi dan handoff. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

## 4. Umpan balik, remediasi dan PPEPP

Dosen menyimpan bukti per mahasiswa, hasil tiap kriteria dan nilai CPMK; menyampaikan umpan balik serta mengatur remediasi sesuai peraturan prodi tanpa menciptakan komponen nilai kelima. Pada akhir semester, hitung capaian, identifikasi indikator bermasalah, analisis penyebab, usulkan perubahan materi/asesmen dan catat penanggung jawab, tenggat serta hasil tindak lanjut pada siklus PPEPP.

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS09` *Business Process Management*, `BK-IS07` *Systems Analysis and Design*. **Pembina Dok 004:** BK-IS09 primer dan BK-IS07 sekunder; Dok 037 juga menyebut BK-IT11.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Rekayasa Proses Bisnis Enterprise, Simulasi Alur Kerja Bisnis (BPMN), Robotic Process Automation (RPA dasar: UiPath / Camunda), Integrasi Alur Kerja Antar-Departemen, Pengukuran Efisiensi Proses.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding antarmuka visual grafis aplikasi dari nol, audit pembukuan keuangan korporat, perancangan firewall jaringan.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Mengotomatisasi proses bisnis organisasi; menyerahkan integrasi platform vertikal ke `STC-602`.

Batas tambahan Dok 037: tidak mengembangkan full-stack aplikasi dari nol atau audit COBIT.

**Catatan sumber:** Dok 037 memberi empat CPMK serta P2/KK4/KK5; Dok 043 memberi tiga CPMK dan P2/P4/KK5, selaras pembebanan Dok 004. Dok 043 menempatkan RPA pada Sub-CPMK-2.1 dan integrasi pada Sub-CPMK-3.1 meski rumusan CPMK-3 berfokus RPA; bukti dinilai menurut rumusan CPMK. OCR menggunakan data sintetis, bukan identitas nyata. Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UAS sama-sama mengukur CPMK-3. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** Dumas et al., *Fundamentals of Business Process Management*, 2nd ed. (2018); OMG BPMN 2.0.2 dan DMN; dokumentasi Camunda dan PM4Py.
